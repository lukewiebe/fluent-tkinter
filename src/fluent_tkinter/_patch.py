"""Core monkey-patching logic for fluent tkinter."""

from __future__ import annotations

import functools
import tkinter
import tkinter.ttk as ttk

# Methods where ``None`` is a meaningful return value (e.g. "not found",
# "not visible", "no active element") rather than a void/setter indicator.
# These must NOT be wrapped because replacing ``None`` with ``self`` would
# break their query semantics.
#
# The list was compiled by auditing every public method in
# ``tkinter/__init__.py`` and ``tkinter/ttk.py`` that explicitly returns
# ``None`` or uses the ``… or None`` / ``_getboolean`` patterns.
_EXCLUDED_METHODS: frozenset[str] = frozenset({
    # Misc – timer / focus / grab / selection queries
    "after",              # sleep-mode (no callback) deliberately returns None
    "focus_get",          # None when application has no focus
    "focus_displayof",    # None when display has no focused widget
    "focus_lastfor",      # None sentinel for no last-focus widget
    "tk_focusNext",       # None when no next widget in focus order
    "tk_focusPrev",       # None when no previous widget in focus order
    "grab_current",       # None when no widget holds a grab
    "grab_status",        # None / "local" / "global"
    "selection_own_get",  # None when no widget owns the selection
    "winfo_containing",   # None when no widget at given coordinates

    # Grid geometry manager – queries that return None for empty grids
    "grid_bbox",
    "grid_location",
    "grid_size",
    "grid_propagate",     # getter uses _getboolean(0) → None for False

    # Pack geometry manager
    "pack_propagate",     # same _getboolean issue as grid_propagate

    # Aliases shared by Grid / Pack
    "propagate",          # alias for grid_propagate / pack_propagate
    "size",               # alias for grid_size
    "bbox",               # Canvas/Listbox/Text/Spinbox – None when not visible

    # Canvas queries
    "select_item",        # None when no canvas item has a text selection
    "type",               # None when tag/ID matches no item

    # Listbox / Menu / Treeview
    "index",              # None for "none" / empty menu
    "delete",             # stdlib tests assert falsy return

    # Scrollbar
    "activate",           # None when no scrollbar element is active (getter)

    # Text widget queries
    "count",              # None for empty range or no options
    "dlineinfo",          # None when line is not visible
    "mark_next",          # None when no mark after index
    "mark_previous",      # None when no mark before index

    # Wm – override redirect getter uses _getboolean
    "wm_overrideredirect",
    "overrideredirect",
})


def _make_fluent(method):
    """Wrap *method* so that it returns *self* when the original returns None."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if result is None:
            return self
        return result
    return wrapper


def _patch_class(cls):
    """Patch all public methods of *cls* that are defined directly on it."""
    for name in list(vars(cls)):
        if name.startswith("_"):
            continue
        if name in _EXCLUDED_METHODS:
            continue
        obj = vars(cls)[name]
        if callable(obj) and not isinstance(obj, (classmethod, staticmethod, type)):
            setattr(cls, name, _make_fluent(obj))


_patched = False


def patch():
    """Apply the fluent monkey-patch to tkinter.

    Safe to call multiple times; only patches once.
    """
    global _patched
    if _patched:
        return
    _patched = True

    # Patch the core tkinter class hierarchy.
    # We patch each class in the MRO so that methods defined at every
    # level get the fluent wrapper.
    _tkinter_classes = [
        tkinter.Misc,
        tkinter.Wm,
        tkinter.Grid,
        tkinter.Pack,
        tkinter.Place,
        tkinter.BaseWidget,
        tkinter.Widget,
        tkinter.Tk,
        tkinter.Toplevel,
        tkinter.Button,
        tkinter.Canvas,
        tkinter.Checkbutton,
        tkinter.Entry,
        tkinter.Frame,
        tkinter.Label,
        tkinter.LabelFrame,
        tkinter.Listbox,
        tkinter.Menu,
        tkinter.Menubutton,
        tkinter.Message,
        tkinter.OptionMenu,
        tkinter.PanedWindow,
        tkinter.Radiobutton,
        tkinter.Scale,
        tkinter.Scrollbar,
        tkinter.Spinbox,
        tkinter.Text,
        tkinter.Variable,
        tkinter.StringVar,
        tkinter.IntVar,
        tkinter.DoubleVar,
        tkinter.BooleanVar,
    ]

    _ttk_classes = [
        ttk.Widget,
        ttk.Button,
        ttk.Checkbutton,
        ttk.Combobox,
        ttk.Entry,
        ttk.Frame,
        ttk.Label,
        ttk.LabelFrame,
        ttk.Labelframe,
        ttk.Menubutton,
        ttk.Notebook,
        ttk.Panedwindow,
        ttk.PanedWindow,
        ttk.Progressbar,
        ttk.Radiobutton,
        ttk.Scale,
        ttk.Scrollbar,
        ttk.Separator,
        ttk.Sizegrip,
        ttk.Spinbox,
        ttk.Treeview,
        ttk.LabeledScale,
        ttk.OptionMenu,
    ]

    for cls in _tkinter_classes + _ttk_classes:
        _patch_class(cls)
