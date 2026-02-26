"""Exhaustive tests for wrapped methods on tkinter.Entry and tkinter.Listbox."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class EntryMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Entry."""

    def setUp(self):
        super().setUp()
        self.entry = tkinter.Entry(self.root)
        self.entry.pack()
        self.entry.insert(0, "test text")
        self.root.update_idletasks()

    def test_get_returns_str(self):
        result = self.entry.get()
        self.assertEqual(result, "test text")

    def test_icursor_returns_self(self):
        result = self.entry.icursor(0)
        self.assertIs(result, self.entry)

    def test_insert_returns_self(self):
        result = self.entry.insert(0, "x")
        self.assertIs(result, self.entry)

    def test_scan_mark_returns_self(self):
        result = self.entry.scan_mark(0)
        self.assertIs(result, self.entry)

    def test_scan_dragto_returns_self(self):
        self.entry.scan_mark(0)
        result = self.entry.scan_dragto(10)
        self.assertIs(result, self.entry)

    # select_* methods (Entry defines its own)

    def test_select_adjust_returns_self(self):
        self.entry.select_range(0, 3)
        result = self.entry.select_adjust(0)
        self.assertIs(result, self.entry)

    def test_select_clear_returns_self(self):
        result = self.entry.select_clear()
        self.assertIs(result, self.entry)

    def test_select_from_returns_self(self):
        result = self.entry.select_from(0)
        self.assertIs(result, self.entry)

    def test_select_present_returns_bool(self):
        result = self.entry.select_present()
        self.assertIsInstance(result, bool)

    def test_select_range_returns_self(self):
        result = self.entry.select_range(0, 3)
        self.assertIs(result, self.entry)

    def test_select_to_returns_self(self):
        self.entry.select_from(0)
        result = self.entry.select_to(3)
        self.assertIs(result, self.entry)

    # selection_* aliases

    def test_selection_adjust_returns_self(self):
        self.entry.selection_range(0, 3)
        result = self.entry.selection_adjust(0)
        self.assertIs(result, self.entry)

    def test_selection_clear_returns_self(self):
        result = self.entry.selection_clear()
        self.assertIs(result, self.entry)

    def test_selection_from_returns_self(self):
        result = self.entry.selection_from(0)
        self.assertIs(result, self.entry)

    def test_selection_present_returns_bool(self):
        result = self.entry.selection_present()
        self.assertIsInstance(result, bool)

    def test_selection_range_returns_self(self):
        result = self.entry.selection_range(0, 3)
        self.assertIs(result, self.entry)

    def test_selection_to_returns_self(self):
        self.entry.selection_from(0)
        result = self.entry.selection_to(3)
        self.assertIs(result, self.entry)


class ListboxMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Listbox."""

    def setUp(self):
        super().setUp()
        self.listbox = tkinter.Listbox(self.root)
        self.listbox.pack()
        self.listbox.insert(0, "item1", "item2", "item3")
        self.root.update_idletasks()

    def test_curselection_returns_tuple(self):
        result = self.listbox.curselection()
        self.assertIsInstance(result, tuple)

    def test_get_returns_str(self):
        result = self.listbox.get(0)
        self.assertEqual(result, "item1")

    def test_insert_returns_self(self):
        result = self.listbox.insert("end", "item4")
        self.assertIs(result, self.listbox)

    def test_itemcget_returns_str(self):
        result = self.listbox.itemcget(0, "background")
        self.assertIsInstance(result, str)

    def test_itemconfig_setter_returns_self(self):
        result = self.listbox.itemconfig(0, background="white")
        self.assertIs(result, self.listbox)

    def test_itemconfigure_setter_returns_self(self):
        result = self.listbox.itemconfigure(0, background="white")
        self.assertIs(result, self.listbox)

    def test_nearest_returns_int(self):
        result = self.listbox.nearest(0)
        self.assertIsInstance(result, int)

    def test_scan_mark_returns_self(self):
        result = self.listbox.scan_mark(0, 0)
        self.assertIs(result, self.listbox)

    def test_scan_dragto_returns_self(self):
        self.listbox.scan_mark(0, 0)
        result = self.listbox.scan_dragto(10, 10)
        self.assertIs(result, self.listbox)

    def test_see_returns_self(self):
        result = self.listbox.see(0)
        self.assertIs(result, self.listbox)

    # select_* methods

    def test_select_anchor_returns_self(self):
        result = self.listbox.select_anchor(0)
        self.assertIs(result, self.listbox)

    def test_select_clear_returns_self(self):
        result = self.listbox.select_clear(0)
        self.assertIs(result, self.listbox)

    def test_select_includes_returns_bool(self):
        result = self.listbox.select_includes(0)
        self.assertIsInstance(result, bool)

    def test_select_set_returns_self(self):
        result = self.listbox.select_set(0)
        self.assertIs(result, self.listbox)

    # selection_* aliases

    def test_selection_anchor_returns_self(self):
        result = self.listbox.selection_anchor(0)
        self.assertIs(result, self.listbox)

    def test_selection_clear_returns_self(self):
        result = self.listbox.selection_clear(0)
        self.assertIs(result, self.listbox)

    def test_selection_includes_returns_bool(self):
        result = self.listbox.selection_includes(0)
        self.assertIsInstance(result, bool)

    def test_selection_set_returns_self(self):
        result = self.listbox.selection_set(0)
        self.assertIs(result, self.listbox)


if __name__ == '__main__':
    unittest.main()
