"""Exhaustive tests for wrapped methods on all ttk widget classes."""

import unittest
import tkinter
from tkinter import ttk
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class TtkWidgetMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Widget."""

    def setUp(self):
        super().setUp()
        self.widget = ttk.Button(self.root, text="test")
        self.widget.pack()
        self.root.update_idletasks()

    def test_identify_returns_str(self):
        result = self.widget.identify(10, 10)
        self.assertIsInstance(result, str)

    def test_instate_returns_bool(self):
        result = self.widget.instate(("!disabled",))
        self.assertIsInstance(result, bool)

    def test_state_getter_returns_tuple(self):
        result = self.widget.state()
        self.assertIsInstance(result, tuple)


class TtkButtonMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Button."""

    def setUp(self):
        super().setUp()
        self.button = ttk.Button(self.root, text="test")

    def test_invoke_returns_value(self):
        # ttk.Button.invoke returns the command result (a Tcl_Obj or '')
        result = self.button.invoke()
        self.assertIsNotNone(result)


class TtkCheckbuttonMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Checkbutton."""

    def setUp(self):
        super().setUp()
        self.cb = ttk.Checkbutton(self.root, text="test")

    def test_invoke_returns_value(self):
        result = self.cb.invoke()
        self.assertIsNotNone(result)


class TtkComboboxMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Combobox."""

    def setUp(self):
        super().setUp()
        self.combo = ttk.Combobox(self.root, values=["a", "b", "c"])

    def test_current_returns_int(self):
        result = self.combo.current()
        self.assertIsInstance(result, int)

    def test_set_returns_self(self):
        result = self.combo.set("b")
        self.assertIs(result, self.combo)


class TtkEntryMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Entry."""

    def setUp(self):
        super().setUp()
        self.entry = ttk.Entry(self.root)
        self.entry.pack()
        self.root.update_idletasks()

    def test_identify_returns_str(self):
        result = self.entry.identify(10, 10)
        self.assertIsInstance(result, str)

    def test_validate_returns_bool(self):
        result = self.entry.validate()
        self.assertIsInstance(result, bool)


class TtkNotebookMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Notebook."""

    def setUp(self):
        super().setUp()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Tab1")
        self.notebook.add(self.tab2, text="Tab2")
        self.root.update_idletasks()

    def test_add_returns_self(self):
        tab3 = ttk.Frame(self.notebook)
        result = self.notebook.add(tab3, text="Tab3")
        self.assertIs(result, self.notebook)

    def test_enable_traversal_returns_self(self):
        result = self.notebook.enable_traversal()
        self.assertIs(result, self.notebook)

    def test_forget_returns_self(self):
        result = self.notebook.forget(self.tab2)
        self.assertIs(result, self.notebook)

    def test_hide_returns_self(self):
        result = self.notebook.hide(0)
        self.assertIs(result, self.notebook)

    def test_identify_returns_str(self):
        result = self.notebook.identify(10, 10)
        self.assertIsInstance(result, str)

    def test_insert_returns_self(self):
        result = self.notebook.insert(0, self.tab1, text="Tab1x")
        self.assertIs(result, self.notebook)

    def test_select_getter_returns_str(self):
        result = self.notebook.select()
        self.assertIsInstance(result, str)

    def test_select_setter_returns_str(self):
        # ttk Notebook.select(tab_id) returns '' via tk.call, not None
        result = self.notebook.select(0)
        self.assertEqual(result, '')

    def test_tab_getter_returns_dict(self):
        result = self.notebook.tab(0)
        self.assertIsInstance(result, dict)

    def test_tab_setter_returns_dict(self):
        # ttk Notebook.tab(tab_id, **kw) returns {} (empty dict) via _val_or_dict
        result = self.notebook.tab(0, text="NewTab")
        self.assertIsInstance(result, dict)

    def test_tabs_returns_tuple(self):
        result = self.notebook.tabs()
        self.assertIsInstance(result, tuple)


class TtkPanedwindowMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Panedwindow."""

    def setUp(self):
        super().setUp()
        self.pw = ttk.Panedwindow(self.root, orient="horizontal")
        self.pw.pack()
        self.pane1 = ttk.Frame(self.pw)
        self.pane2 = ttk.Frame(self.pw)
        self.pw.add(self.pane1)
        self.pw.add(self.pane2)
        self.root.update_idletasks()

    def test_forget_returns_self(self):
        result = self.pw.forget(self.pane2)
        self.assertIs(result, self.pw)

    def test_insert_returns_self(self):
        result = self.pw.insert(0, self.pane1)
        self.assertIs(result, self.pw)

    def test_pane_getter_returns_dict(self):
        result = self.pw.pane(0)
        self.assertIsInstance(result, dict)

    def test_pane_setter_returns_dict(self):
        # ttk Panedwindow.pane(child, **kw) returns {} via _val_or_dict
        result = self.pw.pane(0, weight=1)
        self.assertIsInstance(result, dict)

    def test_sashpos_getter_returns_int(self):
        result = self.pw.sashpos(0)
        self.assertIsInstance(result, int)


class TtkProgressbarMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Progressbar."""

    def setUp(self):
        super().setUp()
        self.pb = ttk.Progressbar(self.root, maximum=100)

    def test_start_returns_self(self):
        result = self.pb.start()
        self.assertIs(result, self.pb)
        self.pb.stop()

    def test_step_returns_self(self):
        result = self.pb.step(10)
        self.assertIs(result, self.pb)

    def test_stop_returns_self(self):
        self.pb.start()
        result = self.pb.stop()
        self.assertIs(result, self.pb)


class TtkRadiobuttonMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Radiobutton."""

    def setUp(self):
        super().setUp()
        self.rb = ttk.Radiobutton(self.root, text="test")

    def test_invoke_returns_value(self):
        result = self.rb.invoke()
        self.assertIsNotNone(result)


class TtkScaleMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Scale."""

    def setUp(self):
        super().setUp()
        self.scale = ttk.Scale(self.root, from_=0, to=100)

    def test_configure_setter_returns_self(self):
        result = self.scale.configure(from_=0)
        self.assertIs(result, self.scale)

    def test_get_returns_number(self):
        result = self.scale.get()
        self.assertIsInstance(result, (int, float))


class TtkSpinboxMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Spinbox."""

    def setUp(self):
        super().setUp()
        self.spinbox = ttk.Spinbox(self.root, from_=0, to=100)

    def test_set_returns_self(self):
        result = self.spinbox.set("50")
        self.assertIs(result, self.spinbox)


class TtkTreeviewMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Treeview."""

    def setUp(self):
        super().setUp()
        self.tv = ttk.Treeview(self.root)
        self.tv.pack()
        self.item1 = self.tv.insert("", "end", text="Item 1")
        self.item2 = self.tv.insert("", "end", text="Item 2")
        self.root.update_idletasks()

    # -- Value-returning methods --

    def test_column_getter_returns_dict(self):
        result = self.tv.column("#0")
        self.assertIsInstance(result, dict)

    def test_column_setter_returns_dict(self):
        # ttk Treeview.column(col, **kw) returns {} via _val_or_dict
        result = self.tv.column("#0", width=100)
        self.assertIsInstance(result, dict)

    def test_exists_returns_bool(self):
        result = self.tv.exists(self.item1)
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_focus_getter_returns_str(self):
        result = self.tv.focus()
        self.assertIsInstance(result, str)

    def test_focus_setter_returns_str(self):
        # Treeview.focus(item) returns '' (tk.call pass-through)
        result = self.tv.focus(self.item1)
        self.assertEqual(result, '')

    def test_get_children_returns_tuple(self):
        result = self.tv.get_children()
        self.assertIsInstance(result, tuple)

    def test_heading_getter_returns_dict(self):
        result = self.tv.heading("#0")
        self.assertIsInstance(result, dict)

    def test_heading_setter_returns_dict(self):
        # ttk Treeview.heading(col, **kw) returns {} via _val_or_dict
        result = self.tv.heading("#0", text="Name")
        self.assertIsInstance(result, dict)

    def test_identify_returns_str(self):
        # ttk.Treeview.identify takes (component, x, y), not (x, y)
        result = self.tv.identify("row", 10, 10)
        self.assertIsInstance(result, str)

    def test_identify_column_returns_str(self):
        result = self.tv.identify_column(10)
        self.assertIsInstance(result, str)

    def test_identify_element_returns_str(self):
        result = self.tv.identify_element(10, 10)
        self.assertIsInstance(result, str)

    def test_identify_region_returns_str(self):
        result = self.tv.identify_region(10, 10)
        self.assertIsInstance(result, str)

    def test_identify_row_returns_str(self):
        result = self.tv.identify_row(10)
        self.assertIsInstance(result, str)

    def test_insert_returns_str(self):
        result = self.tv.insert("", "end", text="Item 3")
        self.assertIsInstance(result, str)

    def test_item_getter_returns_dict(self):
        result = self.tv.item(self.item1)
        self.assertIsInstance(result, dict)

    def test_item_setter_returns_dict(self):
        # ttk Treeview.item(item, **kw) returns {} via _val_or_dict
        result = self.tv.item(self.item1, text="Modified")
        self.assertIsInstance(result, dict)

    def test_next_returns_str(self):
        result = self.tv.next(self.item1)
        self.assertIsInstance(result, str)

    def test_parent_returns_str(self):
        result = self.tv.parent(self.item1)
        self.assertIsInstance(result, str)

    def test_prev_returns_str(self):
        result = self.tv.prev(self.item2)
        self.assertIsInstance(result, str)

    def test_selection_returns_tuple(self):
        result = self.tv.selection()
        self.assertIsInstance(result, tuple)

    def test_set_getter_returns_dict(self):
        result = self.tv.set(self.item1)
        self.assertIsInstance(result, dict)

    def test_tag_configure_getter_returns_dict(self):
        result = self.tv.tag_configure("mytag")
        self.assertIsInstance(result, dict)

    def test_tag_has_returns_tuple(self):
        result = self.tv.tag_has("mytag")
        self.assertIsInstance(result, tuple)

    # -- Self-returning methods (chainable) --

    def test_detach_returns_self(self):
        result = self.tv.detach(self.item2)
        self.assertIs(result, self.tv)

    def test_move_returns_self(self):
        result = self.tv.move(self.item1, "", 0)
        self.assertIs(result, self.tv)

    def test_reattach_returns_self(self):
        self.tv.detach(self.item2)
        result = self.tv.reattach(self.item2, "", "end")
        self.assertIs(result, self.tv)

    def test_see_returns_self(self):
        result = self.tv.see(self.item1)
        self.assertIs(result, self.tv)

    def test_selection_add_returns_self(self):
        result = self.tv.selection_add(self.item1)
        self.assertIs(result, self.tv)

    def test_selection_remove_returns_self(self):
        self.tv.selection_set(self.item1)
        result = self.tv.selection_remove(self.item1)
        self.assertIs(result, self.tv)

    def test_selection_set_returns_self(self):
        result = self.tv.selection_set(self.item1)
        self.assertIs(result, self.tv)

    def test_selection_toggle_returns_self(self):
        result = self.tv.selection_toggle(self.item1)
        self.assertIs(result, self.tv)

    def test_set_children_returns_self(self):
        result = self.tv.set_children("")
        self.assertIs(result, self.tv)

    def test_tag_bind_returns_self(self):
        result = self.tv.tag_bind("mytag", "<Button-1>", lambda e: None)
        self.assertIs(result, self.tv)

    def test_tag_configure_setter_returns_dict(self):
        # ttk Treeview.tag_configure(tag, **kw) returns {} via _val_or_dict
        result = self.tv.tag_configure("mytag", foreground="red")
        self.assertIsInstance(result, dict)


class TtkLabeledScaleMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on ttk.LabeledScale."""

    def test_destroy_returns_self(self):
        ls = ttk.LabeledScale(self.root)
        result = ls.destroy()
        self.assertIs(result, ls)


class TtkOptionMenuMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on ttk.OptionMenu."""

    def setUp(self):
        super().setUp()
        self.var = tkinter.StringVar(self.root, "opt1")
        self.om = ttk.OptionMenu(self.root, self.var, "opt1", "opt1", "opt2")

    def test_destroy_returns_self(self):
        om = ttk.OptionMenu(self.root, self.var, "opt1", "opt1")
        result = om.destroy()
        self.assertIs(result, om)

    def test_set_menu_returns_self(self):
        result = self.om.set_menu("opt1", "opt1", "opt2")
        self.assertIs(result, self.om)


if __name__ == '__main__':
    unittest.main()
