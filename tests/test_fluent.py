"""Tests for fluent-tkinter monkey-patch behaviour.

These tests verify that:
1. Void (setter / action) methods return ``self`` instead of ``None``.
2. Methods that already return a meaningful value pass that value through
   unchanged (including empty strings and dicts from Tcl).
3. Excluded methods (where ``None`` is semantically meaningful) are not
   wrapped and continue to return ``None``.
4. Multi-step method chaining works end-to-end.

The test style mirrors the CPython ``test_tkinter`` suite: each test class
inherits from :class:`AbstractTkTest` for Tk lifecycle management and uses
plain :mod:`unittest` assertions.
"""

import unittest
import tkinter
from tkinter import ttk, TclError
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


# ---------------------------------------------------------------------------
# Patch machinery
# ---------------------------------------------------------------------------

class PatchMechanismTest(AbstractTkTest, unittest.TestCase):
    """Verify the low-level mechanics of _make_fluent / _patch_class."""

    def test_patched_void_method_returns_self(self):
        # configure() with keyword args is void; the wrapper returns self.
        f = tkinter.Frame(self.root)
        result = f.configure(width=100)
        self.assertIs(result, f)

    def test_patched_method_preserves_non_none_return(self):
        # cget() returns a value; the wrapper must pass it through.
        f = tkinter.Frame(self.root, width=42)
        result = f.cget('width')
        self.assertIsNotNone(result)

    def test_patched_method_preserves_empty_string_return(self):
        # Many Tcl commands return '' in setter mode.  The wrapper must
        # NOT convert '' to self (only None → self).
        self.root.wm_title('test')
        result = self.root.wm_title('new title')
        self.assertIsInstance(result, str)

    def test_patched_method_preserves_functools_wraps(self):
        self.assertEqual(tkinter.Frame.configure.__name__, 'configure')
        self.assertEqual(tkinter.Frame.pack_configure.__name__,
                         'pack_configure')

    def test_patch_is_idempotent(self):
        from fluent_tkinter._patch import patch
        patch()  # already patched via conftest; must not raise

    def test_private_methods_not_patched(self):
        f = tkinter.Frame(self.root)
        result = f._getints('')
        self.assertIsNone(result)

    def test_excluded_method_not_patched(self):
        from fluent_tkinter._patch import _EXCLUDED_METHODS
        f = tkinter.Frame(self.root)
        # Every excluded method name, if present on Frame, must not have
        # its None return replaced by self.
        for name in _EXCLUDED_METHODS:
            if hasattr(f, name):
                method = getattr(type(f), name)
                self.assertFalse(
                    hasattr(method, '__wrapped__') and
                    method.__wrapped__ is not method,
                    f'{name} should not be fluent-wrapped')


# ---------------------------------------------------------------------------
# Geometry managers: Pack, Grid, Place
# ---------------------------------------------------------------------------

class FluentPackTest(AbstractTkTest, unittest.TestCase):

    def test_pack_configure_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.pack_configure(side='top', padx=10)
        self.assertIs(result, f)

    def test_pack_alias_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.pack(side='left')
        self.assertIs(result, f)

    def test_pack_forget_returns_self(self):
        f = tkinter.Frame(self.root)
        f.pack()
        result = f.pack_forget()
        self.assertIs(result, f)

    def test_pack_info_returns_dict(self):
        f = tkinter.Frame(self.root)
        f.pack(side='top')
        info = f.pack_info()
        self.assertIsInstance(info, dict)
        self.assertIn('side', info)

    def test_pack_slaves_returns_list(self):
        a = tkinter.Frame(self.root)
        b = tkinter.Frame(self.root)
        a.pack()
        b.pack()
        slaves = self.root.pack_slaves()
        self.assertIsInstance(slaves, list)

    def test_pack_chaining(self):
        f = tkinter.Frame(self.root)
        result = f.pack(side='top').configure(bg='red')
        self.assertIs(result, f)
        self.assertEqual(f['bg'], 'red')


class FluentGridTest(AbstractTkTest, unittest.TestCase):

    def test_grid_configure_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.grid_configure(row=0, column=0)
        self.assertIs(result, f)

    def test_grid_alias_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.grid(row=0, column=0)
        self.assertIs(result, f)

    def test_grid_forget_returns_self(self):
        f = tkinter.Frame(self.root)
        f.grid(row=0, column=0)
        result = f.grid_forget()
        self.assertIs(result, f)

    def test_grid_remove_returns_self(self):
        f = tkinter.Frame(self.root)
        f.grid(row=0, column=0)
        result = f.grid_remove()
        self.assertIs(result, f)

    def test_grid_columnconfigure_setter_returns_self(self):
        result = self.root.grid_columnconfigure(0, weight=1)
        self.assertIs(result, self.root)

    def test_grid_rowconfigure_setter_returns_self(self):
        result = self.root.grid_rowconfigure(0, weight=1)
        self.assertIs(result, self.root)

    def test_grid_columnconfigure_getter_returns_dict(self):
        self.root.grid_columnconfigure(0, weight=1)
        info = self.root.grid_columnconfigure(0)
        self.assertIsInstance(info, dict)

    def test_grid_chaining(self):
        f = tkinter.Frame(self.root)
        result = f.grid(row=0, column=0).configure(bg='blue')
        self.assertIs(result, f)
        self.assertEqual(f['bg'], 'blue')


class FluentPlaceTest(AbstractTkTest, unittest.TestCase):

    def test_place_configure_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.place_configure(x=10, y=20)
        self.assertIs(result, f)

    def test_place_alias_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.place(x=0, y=0)
        self.assertIs(result, f)

    def test_place_forget_returns_self(self):
        f = tkinter.Frame(self.root)
        f.place(x=0, y=0)
        result = f.place_forget()
        self.assertIs(result, f)

    def test_place_info_returns_dict(self):
        f = tkinter.Frame(self.root)
        f.place(x=10, y=20)
        info = f.place_info()
        self.assertIsInstance(info, dict)

    def test_place_chaining(self):
        f = tkinter.Frame(self.root)
        result = f.place(x=0, y=0).configure(bg='green')
        self.assertIs(result, f)


# ---------------------------------------------------------------------------
# Misc methods
# ---------------------------------------------------------------------------

class FluentMiscTest(AbstractTkTest, unittest.TestCase):

    def test_configure_setter_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.configure(width=200)
        self.assertIs(result, f)

    def test_config_alias_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.config(width=200)
        self.assertIs(result, f)

    def test_configure_query_single_returns_tuple(self):
        f = tkinter.Frame(self.root, width=200)
        result = f.configure('width')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 5)

    def test_configure_query_all_returns_dict(self):
        f = tkinter.Frame(self.root)
        result = f.configure()
        self.assertIsInstance(result, dict)

    def test_bind_returns_funcid(self):
        # bind() with a handler returns a funcid string, not self.
        f = tkinter.Frame(self.root)
        result = f.bind('<Button-1>', lambda e: None)
        self.assertIsInstance(result, str)

    def test_unbind_returns_self(self):
        f = tkinter.Frame(self.root)
        f.bind('<Button-1>', lambda e: None)
        result = f.unbind('<Button-1>')
        self.assertIs(result, f)

    def test_event_add_returns_self(self):
        result = self.root.event_add('<<TestEvent>>', '<Control-t>')
        self.assertIs(result, self.root)

    def test_event_delete_returns_self(self):
        self.root.event_add('<<TestEvent>>', '<Control-t>')
        result = self.root.event_delete('<<TestEvent>>', '<Control-t>')
        self.assertIs(result, self.root)

    def test_event_generate_returns_self(self):
        f = tkinter.Frame(self.root)
        f.pack()
        self.root.update()
        result = f.event_generate('<Button-1>')
        self.assertIs(result, f)

    def test_focus_set_returns_self(self):
        f = tkinter.Frame(self.root)
        f.pack()
        result = f.focus_set()
        self.assertIs(result, f)

    def test_focus_force_returns_self(self):
        f = tkinter.Frame(self.root)
        f.pack()
        result = f.focus_force()
        self.assertIs(result, f)

    def test_grab_set_returns_self(self):
        f = tkinter.Frame(self.root)
        f.pack()
        self.root.update()
        result = f.grab_set()
        self.assertIs(result, f)
        f.grab_release()

    def test_grab_release_returns_self(self):
        f = tkinter.Frame(self.root)
        f.pack()
        self.root.update()
        f.grab_set()
        result = f.grab_release()
        self.assertIs(result, f)

    def test_selection_clear_returns_self(self):
        result = self.root.selection_clear()
        self.assertIs(result, self.root)

    def test_clipboard_clear_returns_self(self):
        result = self.root.clipboard_clear()
        self.assertIs(result, self.root)

    def test_clipboard_append_returns_self(self):
        self.root.clipboard_clear()
        result = self.root.clipboard_append('hello')
        self.assertIs(result, self.root)

    def test_lift_returns_self(self):
        result = self.root.lift()
        self.assertIs(result, self.root)

    def test_lower_returns_self(self):
        result = self.root.lower()
        self.assertIs(result, self.root)

    def test_tkraise_returns_self(self):
        result = self.root.tkraise()
        self.assertIs(result, self.root)

    def test_update_returns_self(self):
        result = self.root.update()
        self.assertIs(result, self.root)

    def test_update_idletasks_returns_self(self):
        result = self.root.update_idletasks()
        self.assertIs(result, self.root)

    def test_after_cancel_returns_self(self):
        timer_id = self.root.after(10000, lambda: None)
        result = self.root.after_cancel(timer_id)
        self.assertIs(result, self.root)

    def test_option_add_returns_self(self):
        result = self.root.option_add('*Font', 'Helvetica')
        self.assertIs(result, self.root)

    def test_option_clear_returns_self(self):
        result = self.root.option_clear()
        self.assertIs(result, self.root)

    def test_tk_setPalette_returns_self(self):
        result = self.root.tk_setPalette(background='white')
        self.assertIs(result, self.root)

    def test_tk_bisque_returns_self(self):
        result = self.root.tk_bisque()
        self.assertIs(result, self.root)

    def test_nametowidget_returns_widget(self):
        f = tkinter.Frame(self.root, name='child')
        result = self.root.nametowidget('.child')
        self.assertIs(result, f)


# ---------------------------------------------------------------------------
# Wm methods
#
# Most Wm setter methods use ``return self.tk.call(...)`` which returns the
# Tcl result (usually '').  Only wm_minsize and wm_maxsize omit the return
# statement in setter mode and thus become fluent (None → self).
# ---------------------------------------------------------------------------

class FluentWmTest(AbstractTkTest, unittest.TestCase):

    def test_wm_title_getter_returns_string(self):
        self.root.wm_title('test title')
        result = self.root.wm_title()
        self.assertEqual(result, 'test title')

    def test_wm_title_setter_passes_through_tcl_return(self):
        # The Tcl 'wm title' command returns '' on set.
        result = self.root.wm_title('test title')
        self.assertEqual(result, '')

    def test_wm_geometry_getter_returns_string(self):
        self.root.wm_geometry('200x100+0+0')
        result = self.root.wm_geometry()
        self.assertIsInstance(result, str)

    def test_wm_geometry_setter_passes_through_tcl_return(self):
        result = self.root.wm_geometry('200x100+0+0')
        self.assertEqual(result, '')

    def test_wm_minsize_setter_returns_self(self):
        result = self.root.wm_minsize(100, 100)
        self.assertIs(result, self.root)

    def test_wm_minsize_getter_returns_tuple(self):
        self.root.wm_minsize(100, 100)
        result = self.root.wm_minsize()
        self.assertIsInstance(result, tuple)

    def test_wm_maxsize_setter_returns_self(self):
        result = self.root.wm_maxsize(800, 600)
        self.assertIs(result, self.root)

    def test_wm_maxsize_getter_returns_tuple(self):
        result = self.root.wm_maxsize()
        self.assertIsInstance(result, tuple)

    def test_wm_state_getter_returns_string(self):
        result = self.root.wm_state()
        self.assertIn(result, ('normal', 'iconic', 'withdrawn', 'zoomed'))

    def test_wm_minsize_chaining(self):
        result = (self.root
                  .wm_minsize(50, 50)
                  .wm_maxsize(800, 600))
        self.assertIs(result, self.root)


# ---------------------------------------------------------------------------
# Button / Checkbutton / Radiobutton
# ---------------------------------------------------------------------------

class FluentButtonTest(AbstractTkTest, unittest.TestCase):

    def test_flash_returns_self(self):
        b = tkinter.Button(self.root, text='click')
        b.pack()
        result = b.flash()
        self.assertIs(result, b)

    def test_invoke_returns_value(self):
        b = tkinter.Button(self.root, text='click')
        result = b.invoke()
        self.assertEqual(result, '')

    def test_invoke_with_command_returns_value(self):
        b = tkinter.Button(self.root, text='click',
                           command=lambda: 'ok')
        result = b.invoke()
        self.assertEqual(result, 'ok')


class FluentCheckbuttonTest(AbstractTkTest, unittest.TestCase):

    def test_select_returns_self(self):
        cb = tkinter.Checkbutton(self.root)
        result = cb.select()
        self.assertIs(result, cb)

    def test_deselect_returns_self(self):
        cb = tkinter.Checkbutton(self.root)
        cb.select()
        result = cb.deselect()
        self.assertIs(result, cb)

    def test_toggle_returns_self(self):
        cb = tkinter.Checkbutton(self.root)
        result = cb.toggle()
        self.assertIs(result, cb)

    def test_flash_returns_self(self):
        cb = tkinter.Checkbutton(self.root, text='check')
        cb.pack()
        result = cb.flash()
        self.assertIs(result, cb)


class FluentRadiobuttonTest(AbstractTkTest, unittest.TestCase):

    def test_select_returns_self(self):
        rb = tkinter.Radiobutton(self.root, value=1)
        result = rb.select()
        self.assertIs(result, rb)

    def test_deselect_returns_self(self):
        rb = tkinter.Radiobutton(self.root, value=1)
        result = rb.deselect()
        self.assertIs(result, rb)

    def test_flash_returns_self(self):
        rb = tkinter.Radiobutton(self.root, text='radio')
        rb.pack()
        result = rb.flash()
        self.assertIs(result, rb)


# ---------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------

class FluentCanvasTest(AbstractTkTest, unittest.TestCase):

    def test_create_rectangle_returns_id(self):
        c = tkinter.Canvas(self.root)
        item = c.create_rectangle(0, 0, 50, 50)
        self.assertIsInstance(item, int)

    def test_create_line_returns_id(self):
        c = tkinter.Canvas(self.root)
        item = c.create_line(0, 0, 50, 50)
        self.assertIsInstance(item, int)

    def test_create_oval_returns_id(self):
        c = tkinter.Canvas(self.root)
        item = c.create_oval(0, 0, 50, 50)
        self.assertIsInstance(item, int)

    def test_create_text_returns_id(self):
        c = tkinter.Canvas(self.root)
        item = c.create_text(25, 25, text='hello')
        self.assertIsInstance(item, int)

    def test_move_returns_self(self):
        c = tkinter.Canvas(self.root)
        item = c.create_rectangle(0, 0, 50, 50)
        result = c.move(item, 10, 10)
        self.assertIs(result, c)

    def test_coords_setter_returns_list(self):
        # coords() always returns via ``return self.tk.call(...)``; when
        # called as a setter the Tcl result is an empty list [].
        c = tkinter.Canvas(self.root)
        item = c.create_rectangle(0, 0, 50, 50)
        result = c.coords(item, 10, 10, 60, 60)
        self.assertIsInstance(result, list)

    def test_coords_getter_returns_list(self):
        c = tkinter.Canvas(self.root)
        item = c.create_rectangle(0, 0, 50, 50)
        coords = c.coords(item)
        self.assertIsInstance(coords, list)
        self.assertEqual(len(coords), 4)

    def test_itemconfigure_setter_returns_self(self):
        c = tkinter.Canvas(self.root)
        item = c.create_rectangle(0, 0, 50, 50)
        result = c.itemconfigure(item, fill='red')
        self.assertIs(result, c)

    def test_tag_bind_returns_funcid(self):
        # tag_bind always returns via ``return self.tk.call(...)``.
        c = tkinter.Canvas(self.root)
        c.create_rectangle(0, 0, 50, 50, tags='rect')
        result = c.tag_bind('rect', '<Button-1>', lambda e: None)
        self.assertIsInstance(result, str)

    def test_tag_raise_returns_self(self):
        c = tkinter.Canvas(self.root)
        c.create_rectangle(0, 0, 50, 50, tags='a')
        c.create_rectangle(10, 10, 60, 60, tags='b')
        result = c.tag_raise('a')
        self.assertIs(result, c)

    def test_tag_lower_returns_self(self):
        c = tkinter.Canvas(self.root)
        c.create_rectangle(0, 0, 50, 50, tags='a')
        c.create_rectangle(10, 10, 60, 60, tags='b')
        result = c.tag_lower('a')
        self.assertIs(result, c)

    def test_addtag_withtag_returns_self(self):
        c = tkinter.Canvas(self.root)
        c.create_rectangle(0, 0, 50, 50, tags='old')
        result = c.addtag_withtag('new', 'old')
        self.assertIs(result, c)

    def test_dtag_returns_self(self):
        c = tkinter.Canvas(self.root)
        c.create_rectangle(0, 0, 50, 50, tags='tag1')
        result = c.dtag('tag1')
        self.assertIs(result, c)

    def test_find_returns_tuple(self):
        c = tkinter.Canvas(self.root)
        c.create_rectangle(0, 0, 50, 50, tags='r')
        result = c.find_withtag('r')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 1)

    def test_canvas_chaining(self):
        c = tkinter.Canvas(self.root)
        item = c.create_rectangle(0, 0, 50, 50)
        result = (c
                  .move(item, 5, 5)
                  .itemconfigure(item, fill='blue')
                  .configure(bg='white'))
        self.assertIs(result, c)


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------

class FluentEntryTest(AbstractTkTest, unittest.TestCase):

    def test_insert_returns_self(self):
        e = tkinter.Entry(self.root)
        result = e.insert(0, 'hello')
        self.assertIs(result, e)

    def test_icursor_returns_self(self):
        e = tkinter.Entry(self.root)
        e.insert(0, 'hello')
        result = e.icursor(2)
        self.assertIs(result, e)

    def test_selection_range_returns_self(self):
        e = tkinter.Entry(self.root)
        e.insert(0, 'hello world')
        result = e.selection_range(0, 5)
        self.assertIs(result, e)

    def test_selection_clear_returns_self(self):
        e = tkinter.Entry(self.root)
        e.insert(0, 'hello')
        result = e.selection_clear()
        self.assertIs(result, e)

    def test_get_returns_string(self):
        e = tkinter.Entry(self.root)
        e.insert(0, 'hello')
        result = e.get()
        self.assertEqual(result, 'hello')

    def test_entry_chaining(self):
        e = tkinter.Entry(self.root)
        result = e.insert(0, 'hello').icursor(3).selection_range(0, 5)
        self.assertIs(result, e)
        self.assertEqual(e.get(), 'hello')


# ---------------------------------------------------------------------------
# Listbox
# ---------------------------------------------------------------------------

class FluentListboxTest(AbstractTkTest, unittest.TestCase):

    def test_insert_returns_self(self):
        lb = tkinter.Listbox(self.root)
        result = lb.insert(0, 'item1')
        self.assertIs(result, lb)

    def test_selection_set_returns_self(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, 'item1', 'item2', 'item3')
        result = lb.selection_set(0)
        self.assertIs(result, lb)

    def test_selection_clear_returns_self(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, 'item1', 'item2')
        lb.selection_set(0)
        result = lb.selection_clear(0)
        self.assertIs(result, lb)

    def test_selection_anchor_returns_self(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, 'item1')
        result = lb.selection_anchor(0)
        self.assertIs(result, lb)

    def test_see_returns_self(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, *('item%d' % i for i in range(100)))
        result = lb.see(50)
        self.assertIs(result, lb)

    def test_itemconfigure_setter_returns_self(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, 'item1')
        result = lb.itemconfigure(0, bg='red')
        self.assertIs(result, lb)

    def test_curselection_returns_tuple(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, 'a', 'b', 'c')
        lb.selection_set(0, 2)
        result = lb.curselection()
        self.assertIsInstance(result, tuple)

    def test_get_returns_value(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, 'a', 'b', 'c')
        self.assertEqual(lb.get(0), 'a')
        self.assertEqual(lb.get(2), 'c')

    def test_listbox_chaining(self):
        lb = tkinter.Listbox(self.root)
        result = (lb
                  .insert(0, 'a', 'b', 'c')
                  .selection_set(0)
                  .see(0)
                  .configure(bg='white'))
        self.assertIs(result, lb)


# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------

class FluentTextTest(AbstractTkTest, unittest.TestCase):

    def test_insert_returns_self(self):
        t = tkinter.Text(self.root)
        result = t.insert('1.0', 'hello')
        self.assertIs(result, t)

    def test_tag_add_returns_self(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello world')
        result = t.tag_add('sel', '1.0', '1.5')
        self.assertIs(result, t)

    def test_tag_remove_returns_self(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello world')
        t.tag_add('sel', '1.0', '1.5')
        result = t.tag_remove('sel', '1.0', '1.5')
        self.assertIs(result, t)

    def test_tag_configure_setter_returns_self(self):
        t = tkinter.Text(self.root)
        result = t.tag_configure('mytag', foreground='red')
        self.assertIs(result, t)

    def test_tag_bind_returns_funcid(self):
        # tag_bind returns via ``return self.tk.call(...)``.
        t = tkinter.Text(self.root)
        result = t.tag_bind('mytag', '<Button-1>', lambda e: None)
        self.assertIsInstance(result, str)

    def test_tag_raise_returns_self(self):
        t = tkinter.Text(self.root)
        result = t.tag_raise('sel')
        self.assertIs(result, t)

    def test_tag_lower_returns_self(self):
        t = tkinter.Text(self.root)
        result = t.tag_lower('sel')
        self.assertIs(result, t)

    def test_mark_set_returns_self(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        result = t.mark_set('mymark', '1.3')
        self.assertIs(result, t)

    def test_mark_unset_returns_self(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        t.mark_set('mymark', '1.3')
        result = t.mark_unset('mymark')
        self.assertIs(result, t)

    def test_mark_gravity_getter_returns_string(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        t.mark_set('mymark', '1.3')
        result = t.mark_gravity('mymark')
        self.assertIn(result, ('left', 'right'))

    def test_mark_gravity_setter_passes_through_tcl_return(self):
        # mark_gravity with two args uses ``return self.tk.call(...)``.
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        t.mark_set('mymark', '1.3')
        result = t.mark_gravity('mymark', 'left')
        self.assertEqual(result, '')

    def test_see_returns_self(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello\n' * 100)
        result = t.see('50.0')
        self.assertIs(result, t)

    def test_get_returns_string(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        result = t.get('1.0', '1.5')
        self.assertEqual(result, 'hello')

    def test_search_returns_index(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello world')
        result = t.search('world', '1.0')
        self.assertEqual(result, '1.6')

    def test_text_chaining(self):
        t = tkinter.Text(self.root)
        result = (t
                  .insert('1.0', 'hello world')
                  .tag_add('bold', '1.0', '1.5')
                  .tag_configure('bold', font='Helvetica 12 bold')
                  .see('1.0'))
        self.assertIs(result, t)


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------

class FluentMenuTest(AbstractTkTest, unittest.TestCase):

    def test_add_command_returns_self(self):
        m = tkinter.Menu(self.root, tearoff=0)
        result = m.add_command(label='Open')
        self.assertIs(result, m)

    def test_add_cascade_returns_self(self):
        m = tkinter.Menu(self.root, tearoff=0)
        sub = tkinter.Menu(m, tearoff=0)
        result = m.add_cascade(label='File', menu=sub)
        self.assertIs(result, m)

    def test_add_separator_returns_self(self):
        m = tkinter.Menu(self.root, tearoff=0)
        result = m.add_separator()
        self.assertIs(result, m)

    def test_add_checkbutton_returns_self(self):
        m = tkinter.Menu(self.root, tearoff=0)
        result = m.add_checkbutton(label='Check')
        self.assertIs(result, m)

    def test_add_radiobutton_returns_self(self):
        m = tkinter.Menu(self.root, tearoff=0)
        result = m.add_radiobutton(label='Radio')
        self.assertIs(result, m)

    def test_entryconfigure_setter_returns_self(self):
        m = tkinter.Menu(self.root, tearoff=0)
        m.add_command(label='Open')
        result = m.entryconfigure(0, label='Open File')
        self.assertIs(result, m)

    def test_menu_chaining(self):
        m = tkinter.Menu(self.root, tearoff=0)
        result = (m
                  .add_command(label='Open')
                  .add_command(label='Save')
                  .add_separator()
                  .add_command(label='Quit'))
        self.assertIs(result, m)


# ---------------------------------------------------------------------------
# Scrollbar
# ---------------------------------------------------------------------------

class FluentScrollbarTest(AbstractTkTest, unittest.TestCase):

    def test_set_returns_self(self):
        sb = tkinter.Scrollbar(self.root)
        result = sb.set(0.0, 0.5)
        self.assertIs(result, sb)

    def test_get_returns_tuple(self):
        sb = tkinter.Scrollbar(self.root)
        sb.set(0.2, 0.8)
        result = sb.get()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)


# ---------------------------------------------------------------------------
# Scale
# ---------------------------------------------------------------------------

class FluentScaleTest(AbstractTkTest, unittest.TestCase):

    def test_set_returns_self(self):
        s = tkinter.Scale(self.root, from_=0, to=100)
        result = s.set(50)
        self.assertIs(result, s)

    def test_get_returns_number(self):
        s = tkinter.Scale(self.root, from_=0, to=100)
        s.set(42)
        result = s.get()
        self.assertEqual(result, 42)


# ---------------------------------------------------------------------------
# Spinbox
#
# Spinbox methods use ``return self.tk.call(...)`` for most operations,
# so insert/icursor/selection return Tcl values ('', ()) rather than None.
# ---------------------------------------------------------------------------

class FluentSpinboxTest(AbstractTkTest, unittest.TestCase):

    def test_insert_passes_through_tcl_return(self):
        sb = tkinter.Spinbox(self.root, from_=0, to=100)
        result = sb.insert(0, '42')
        self.assertEqual(result, '')

    def test_icursor_passes_through_tcl_return(self):
        sb = tkinter.Spinbox(self.root, from_=0, to=100)
        sb.insert(0, '42')
        result = sb.icursor(1)
        self.assertEqual(result, '')

    def test_configure_returns_self(self):
        sb = tkinter.Spinbox(self.root, from_=0, to=100)
        result = sb.configure(bg='white')
        self.assertIs(result, sb)

    def test_get_returns_string(self):
        sb = tkinter.Spinbox(self.root, from_=0, to=100)
        result = sb.get()
        self.assertIsInstance(result, str)


# ---------------------------------------------------------------------------
# PanedWindow
# ---------------------------------------------------------------------------

class FluentPanedWindowTest(AbstractTkTest, unittest.TestCase):

    def test_add_returns_self(self):
        pw = tkinter.PanedWindow(self.root)
        f = tkinter.Frame(pw)
        result = pw.add(f)
        self.assertIs(result, pw)

    def test_remove_returns_self(self):
        pw = tkinter.PanedWindow(self.root)
        f = tkinter.Frame(pw)
        pw.add(f)
        result = pw.remove(f)
        self.assertIs(result, pw)

    def test_paneconfigure_setter_returns_self(self):
        pw = tkinter.PanedWindow(self.root)
        f = tkinter.Frame(pw)
        pw.add(f)
        result = pw.paneconfigure(f, width=100)
        self.assertIs(result, pw)


# ---------------------------------------------------------------------------
# Variable subclasses
# ---------------------------------------------------------------------------

class FluentVariableTest(AbstractTkTest, unittest.TestCase):

    def test_stringvar_set_returns_self(self):
        v = tkinter.StringVar(self.root)
        result = v.set('hello')
        self.assertIs(result, v)

    def test_intvar_set_returns_self(self):
        v = tkinter.IntVar(self.root)
        result = v.set(42)
        self.assertIs(result, v)

    def test_doublevar_set_returns_self(self):
        v = tkinter.DoubleVar(self.root)
        result = v.set(3.14)
        self.assertIs(result, v)

    def test_booleanvar_set_returns_self(self):
        v = tkinter.BooleanVar(self.root)
        result = v.set(True)
        self.assertIs(result, v)

    def test_stringvar_get_returns_value(self):
        v = tkinter.StringVar(self.root, value='hello')
        self.assertEqual(v.get(), 'hello')

    def test_intvar_get_returns_value(self):
        v = tkinter.IntVar(self.root, value=42)
        self.assertEqual(v.get(), 42)

    def test_doublevar_get_returns_value(self):
        v = tkinter.DoubleVar(self.root, value=3.14)
        self.assertAlmostEqual(v.get(), 3.14)

    def test_booleanvar_get_returns_value(self):
        v = tkinter.BooleanVar(self.root, value=True)
        self.assertTrue(v.get())

    def test_variable_chaining(self):
        v = tkinter.StringVar(self.root)
        result = v.set('hello')
        self.assertIs(result, v)
        self.assertEqual(v.get(), 'hello')


# ---------------------------------------------------------------------------
# ttk widgets
#
# Many ttk getter/setter methods use ``return self.tk.call(...)`` which
# returns the Tcl result (often {} or '' for setter mode).  Only methods
# that omit the return statement become fluent.
# ---------------------------------------------------------------------------

class FluentTtkButtonTest(AbstractTkTest, unittest.TestCase):

    def test_configure_returns_self(self):
        b = ttk.Button(self.root, text='click')
        result = b.configure(text='new')
        self.assertIs(result, b)

    def test_invoke_returns_value(self):
        # ttk.Button.invoke returns a Tcl result (not None).
        b = ttk.Button(self.root, text='click')
        result = b.invoke()
        self.assertIsNotNone(result)

    def test_state_returns_tuple(self):
        b = ttk.Button(self.root)
        result = b.state(['disabled'])
        self.assertIsInstance(result, tuple)


class FluentTtkEntryTest(AbstractTkTest, unittest.TestCase):

    def test_insert_returns_self(self):
        e = ttk.Entry(self.root)
        result = e.insert(0, 'hello')
        self.assertIs(result, e)

    def test_icursor_returns_self(self):
        e = ttk.Entry(self.root)
        e.insert(0, 'hello')
        result = e.icursor(2)
        self.assertIs(result, e)

    def test_selection_range_returns_self(self):
        e = ttk.Entry(self.root)
        e.insert(0, 'hello world')
        result = e.selection_range(0, 5)
        self.assertIs(result, e)

    def test_configure_returns_self(self):
        e = ttk.Entry(self.root)
        result = e.configure(width=30)
        self.assertIs(result, e)


class FluentTtkComboboxTest(AbstractTkTest, unittest.TestCase):

    def test_set_returns_self(self):
        cb = ttk.Combobox(self.root, values=['a', 'b', 'c'])
        result = cb.set('b')
        self.assertIs(result, cb)

    def test_get_returns_value(self):
        cb = ttk.Combobox(self.root, values=['a', 'b', 'c'])
        cb.set('b')
        result = cb.get()
        self.assertEqual(result, 'b')


class FluentTtkNotebookTest(AbstractTkTest, unittest.TestCase):

    def test_add_returns_self(self):
        nb = ttk.Notebook(self.root)
        f = ttk.Frame(nb)
        result = nb.add(f, text='Tab 1')
        self.assertIs(result, nb)

    def test_forget_returns_self(self):
        nb = ttk.Notebook(self.root)
        f = ttk.Frame(nb)
        nb.add(f, text='Tab 1')
        result = nb.forget(0)
        self.assertIs(result, nb)

    def test_hide_returns_self(self):
        nb = ttk.Notebook(self.root)
        f = ttk.Frame(nb)
        nb.add(f, text='Tab 1')
        result = nb.hide(0)
        self.assertIs(result, nb)

    def test_select_passes_through_tcl_return(self):
        # Notebook.select(tab_id) uses ``return self.tk.call(...)``.
        nb = ttk.Notebook(self.root)
        f1 = ttk.Frame(nb)
        f2 = ttk.Frame(nb)
        nb.add(f1, text='Tab 1')
        nb.add(f2, text='Tab 2')
        result = nb.select(0)
        self.assertEqual(result, '')

    def test_tab_getter_returns_dict(self):
        nb = ttk.Notebook(self.root)
        f = ttk.Frame(nb)
        nb.add(f, text='Tab 1')
        result = nb.tab(0)
        self.assertIsInstance(result, dict)

    def test_tab_setter_passes_through_tcl_return(self):
        # tab(idx, **kw) setter uses ``return self.tk.call(...)``.
        nb = ttk.Notebook(self.root)
        f = ttk.Frame(nb)
        nb.add(f, text='Tab 1')
        result = nb.tab(0, text='Renamed')
        self.assertIsInstance(result, dict)

    def test_notebook_chaining(self):
        nb = ttk.Notebook(self.root)
        f1 = ttk.Frame(nb)
        f2 = ttk.Frame(nb)
        result = (nb
                  .add(f1, text='Tab 1')
                  .add(f2, text='Tab 2')
                  .pack(fill='both', expand=True))
        self.assertIs(result, nb)


class FluentTtkTreeviewTest(AbstractTkTest, unittest.TestCase):

    def test_insert_returns_item_id(self):
        tv = ttk.Treeview(self.root)
        item = tv.insert('', 'end', text='item1')
        self.assertIsInstance(item, str)
        self.assertTrue(len(item) > 0)

    def test_heading_setter_passes_through_tcl_return(self):
        # heading() with keyword args uses ``return self.tk.call(...)``.
        tv = ttk.Treeview(self.root, columns=('name',))
        result = tv.heading('name', text='Name')
        self.assertIsInstance(result, dict)

    def test_heading_getter_returns_dict(self):
        tv = ttk.Treeview(self.root, columns=('name',))
        tv.heading('name', text='Name')
        result = tv.heading('name')
        self.assertIsInstance(result, dict)

    def test_column_setter_passes_through_tcl_return(self):
        tv = ttk.Treeview(self.root, columns=('name',))
        result = tv.column('name', width=100)
        self.assertIsInstance(result, dict)

    def test_column_getter_returns_dict(self):
        tv = ttk.Treeview(self.root, columns=('name',))
        result = tv.column('name')
        self.assertIsInstance(result, dict)

    def test_item_setter_passes_through_tcl_return(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item1')
        result = tv.item(iid, text='renamed')
        self.assertIsInstance(result, dict)

    def test_item_getter_returns_dict(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item1')
        result = tv.item(iid)
        self.assertIsInstance(result, dict)

    def test_move_returns_self(self):
        tv = ttk.Treeview(self.root)
        parent = tv.insert('', 'end', text='parent')
        child = tv.insert('', 'end', text='child')
        result = tv.move(child, parent, 0)
        self.assertIs(result, tv)

    def test_see_returns_self(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item')
        result = tv.see(iid)
        self.assertIs(result, tv)

    def test_set_getter_returns_dict(self):
        tv = ttk.Treeview(self.root, columns=('val',))
        iid = tv.insert('', 'end', values=('x',))
        result = tv.set(iid)
        self.assertIsInstance(result, dict)

    def test_set_setter_passes_through_tcl_return(self):
        tv = ttk.Treeview(self.root, columns=('val',))
        iid = tv.insert('', 'end', values=('x',))
        result = tv.set(iid, 'val', 'new')
        self.assertEqual(result, '')

    def test_tag_bind_returns_self(self):
        tv = ttk.Treeview(self.root)
        result = tv.tag_bind('mytag', '<Button-1>', lambda e: None)
        self.assertIs(result, tv)

    def test_selection_set_returns_self(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item')
        result = tv.selection_set(iid)
        self.assertIs(result, tv)

    def test_selection_add_returns_self(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item')
        result = tv.selection_add(iid)
        self.assertIs(result, tv)

    def test_selection_remove_returns_self(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item')
        tv.selection_set(iid)
        result = tv.selection_remove(iid)
        self.assertIs(result, tv)

    def test_selection_toggle_returns_self(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item')
        result = tv.selection_toggle(iid)
        self.assertIs(result, tv)

    def test_treeview_chaining_fluent_methods(self):
        tv = ttk.Treeview(self.root, columns=('val',))
        iid = tv.insert('', 'end', text='item', values=('x',))
        result = (tv
                  .see(iid)
                  .selection_set(iid)
                  .configure(height=10))
        self.assertIs(result, tv)


class FluentTtkProgressbarTest(AbstractTkTest, unittest.TestCase):

    def test_start_returns_self(self):
        pb = ttk.Progressbar(self.root)
        result = pb.start()
        self.assertIs(result, pb)
        pb.stop()

    def test_stop_returns_self(self):
        pb = ttk.Progressbar(self.root)
        pb.start()
        result = pb.stop()
        self.assertIs(result, pb)

    def test_step_returns_self(self):
        pb = ttk.Progressbar(self.root)
        result = pb.step(10)
        self.assertIs(result, pb)


class FluentTtkScaleTest(AbstractTkTest, unittest.TestCase):

    def test_set_returns_self(self):
        s = ttk.Scale(self.root, from_=0, to=100)
        result = s.set(50)
        self.assertIs(result, s)

    def test_get_returns_number(self):
        s = ttk.Scale(self.root, from_=0, to=100)
        s.set(50)
        result = s.get()
        self.assertAlmostEqual(result, 50.0)


# ---------------------------------------------------------------------------
# Excluded methods – verify None semantics are preserved
# ---------------------------------------------------------------------------

class ExcludedMethodTest(AbstractTkTest, unittest.TestCase):
    """Verify that excluded methods continue to return None when
    the underlying Tk command indicates 'not found' / 'not active'."""

    def test_after_sleep_returns_none(self):
        result = self.root.after(1)
        self.assertIsNone(result)

    def test_focus_get_returns_none_or_widget(self):
        result = self.root.focus_get()
        if result is not None:
            self.assertIsInstance(result, tkinter.Misc)

    def test_grab_status_returns_none(self):
        f = tkinter.Frame(self.root)
        result = f.grab_status()
        self.assertIsNone(result)

    def test_grab_current_returns_none(self):
        result = self.root.grab_current()
        self.assertIsNone(result)

    def test_grid_propagate_getter_false(self):
        self.root.grid_propagate(False)
        result = self.root.grid_propagate()
        self.assertFalse(result)
        self.assertNotIsInstance(result, tkinter.Misc)
        self.root.grid_propagate(True)

    def test_pack_propagate_getter_false(self):
        self.root.pack_propagate(False)
        result = self.root.pack_propagate()
        self.assertFalse(result)
        self.assertNotIsInstance(result, tkinter.Misc)
        self.root.pack_propagate(True)

    def test_overrideredirect_getter(self):
        result = self.root.overrideredirect()
        self.assertNotIsInstance(result, tkinter.Misc)

    def test_text_bbox_invisible_returns_none(self):
        t = tkinter.Text(self.root)
        t.pack()
        self.root.update()
        result = t.bbox('end')
        self.assertIsNone(result)

    def test_listbox_bbox_invalid_returns_none(self):
        lb = tkinter.Listbox(self.root)
        lb.insert(0, *('el%d' % i for i in range(8)))
        lb.pack()
        self.root.update()
        result = lb.bbox(-1)
        self.assertIsNone(result)

    def test_scrollbar_activate_getter_returns_none(self):
        sb = tkinter.Scrollbar(self.root)
        sb.pack()
        self.root.update()
        sb.activate('')
        result = sb.activate()
        self.assertIsNone(result)

    def test_menu_index_none_returns_none(self):
        m = tkinter.Menu(self.root, tearoff=0)
        result = m.index('none')
        self.assertIsNone(result)

    def test_text_mark_next_returns_none(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        result = t.mark_next('end')
        self.assertIsNone(result)

    def test_text_mark_previous_returns_none(self):
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        result = t.mark_previous('1.0')
        self.assertIsNone(result)

    def test_canvas_select_item_returns_none(self):
        c = tkinter.Canvas(self.root)
        result = c.select_item()
        self.assertIsNone(result)

    def test_winfo_containing_returns_none(self):
        result = self.root.winfo_containing(-99999, -99999)
        self.assertIsNone(result)

    def test_text_count_returns_none_for_empty(self):
        t = tkinter.Text(self.root)
        result = t.count('1.0', '1.0')
        self.assertIsNone(result)

    def test_delete_not_fluent(self):
        # delete is excluded; verify it returns a falsy value, not self.
        t = tkinter.Text(self.root)
        t.insert('1.0', 'hello')
        result = t.delete('1.0', '1.5')
        self.assertFalse(result)


# ---------------------------------------------------------------------------
# End-to-end chaining tests
# ---------------------------------------------------------------------------

class ChainingEndToEndTest(AbstractTkTest, unittest.TestCase):
    """Integration tests demonstrating realistic chaining patterns."""

    def test_label_pack_configure(self):
        lbl = tkinter.Label(self.root, text='hello')
        result = lbl.pack(side='top', padx=5).configure(fg='blue')
        self.assertIs(result, lbl)
        self.assertEqual(lbl['fg'], 'blue')

    def test_button_grid_configure_bind(self):
        clicks = []
        btn = tkinter.Button(self.root, text='Go')
        result = (btn
                  .grid(row=0, column=0, padx=5)
                  .configure(text='Click me')
                  .bind('<Enter>', lambda e: clicks.append('enter')))
        # bind returns a funcid, not self.
        self.assertIsInstance(result, str)
        self.assertEqual(btn['text'], 'Click me')

    def test_entry_insert_icursor(self):
        e = tkinter.Entry(self.root)
        result = e.pack().insert(0, 'world').insert(0, 'hello ').icursor(5)
        self.assertIs(result, e)
        self.assertEqual(e.get(), 'hello world')

    def test_text_insert_tag_see(self):
        t = tkinter.Text(self.root)
        result = (t
                  .pack(fill='both', expand=True)
                  .insert('1.0', 'Line 1\nLine 2\nLine 3')
                  .tag_add('highlight', '1.0', '1.6')
                  .tag_configure('highlight', background='yellow')
                  .see('1.0'))
        self.assertIs(result, t)
        self.assertEqual(t.get('1.0', '1.6'), 'Line 1')

    def test_canvas_create_and_modify(self):
        c = tkinter.Canvas(self.root, width=200, height=200)
        c.pack()
        item = c.create_rectangle(10, 10, 50, 50, fill='red')
        result = (c
                  .move(item, 20, 20)
                  .itemconfigure(item, fill='blue', outline='white'))
        self.assertIs(result, c)

    def test_menu_build(self):
        menubar = tkinter.Menu(self.root, tearoff=0)
        file_menu = tkinter.Menu(menubar, tearoff=0)
        result = (file_menu
                  .add_command(label='New')
                  .add_command(label='Open')
                  .add_separator()
                  .add_command(label='Exit'))
        self.assertIs(result, file_menu)
        self.assertIs(
            menubar.add_cascade(label='File', menu=file_menu),
            menubar)

    def test_variable_set_and_use(self):
        var = tkinter.StringVar(self.root)
        var.set('initial')
        lbl = tkinter.Label(self.root, textvariable=var)
        result = lbl.pack()
        self.assertIs(result, lbl)
        self.assertEqual(var.get(), 'initial')

    def test_listbox_populate(self):
        lb = tkinter.Listbox(self.root)
        result = (lb
                  .pack(fill='both', expand=True)
                  .insert('end', 'Alice')
                  .insert('end', 'Bob')
                  .insert('end', 'Charlie')
                  .selection_set(0)
                  .see(0))
        self.assertIs(result, lb)
        self.assertEqual(lb.get(0), 'Alice')
        self.assertEqual(lb.get(2), 'Charlie')
        self.assertEqual(lb.curselection(), (0,))

    def test_scrollbar_text_hookup(self):
        t = tkinter.Text(self.root, height=5)
        sb = tkinter.Scrollbar(self.root, command=t.yview)
        t.configure(yscrollcommand=sb.set)
        result_t = t.pack(side='left', fill='both', expand=True)
        result_sb = sb.pack(side='right', fill='y')
        self.assertIs(result_t, t)
        self.assertIs(result_sb, sb)

    def test_checkbutton_chain(self):
        var = tkinter.IntVar(self.root)
        cb = tkinter.Checkbutton(self.root, variable=var)
        result = (cb
                  .pack(side='left')
                  .select()
                  .configure(text='Accept'))
        self.assertIs(result, cb)
        self.assertEqual(var.get(), 1)
        self.assertEqual(cb['text'], 'Accept')

    def test_notebook_add_and_pack(self):
        nb = ttk.Notebook(self.root)
        tab1 = ttk.Frame(nb)
        tab2 = ttk.Frame(nb)
        result = (nb
                  .add(tab1, text='Tab 1')
                  .add(tab2, text='Tab 2')
                  .pack(fill='both', expand=True))
        self.assertIs(result, nb)

    def test_treeview_selection_workflow(self):
        tv = ttk.Treeview(self.root)
        iid = tv.insert('', 'end', text='item')
        result = (tv
                  .see(iid)
                  .selection_set(iid)
                  .pack(fill='both', expand=True))
        self.assertIs(result, tv)
        self.assertEqual(tv.selection(), (iid,))

    def test_panedwindow_build(self):
        pw = tkinter.PanedWindow(self.root, orient='horizontal')
        f1 = tkinter.Frame(pw, width=100, bg='red')
        f2 = tkinter.Frame(pw, width=100, bg='blue')
        result = (pw
                  .add(f1)
                  .add(f2)
                  .pack(fill='both', expand=True))
        self.assertIs(result, pw)
        panes = pw.panes()
        self.assertEqual(len(panes), 2)

    def test_scale_set_configure(self):
        s = tkinter.Scale(self.root, from_=0, to=100)
        result = s.pack().set(50).configure(label='Volume')
        self.assertIs(result, s)
        self.assertEqual(s.get(), 50)

    def test_progressbar_lifecycle(self):
        pb = ttk.Progressbar(self.root, maximum=100)
        result = pb.pack().step(25).step(25)
        self.assertIs(result, pb)
