"""Exhaustive tests for wrapped methods on tkinter.Spinbox."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class SpinboxMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Spinbox.

    Note: Spinbox defines its own scan/selection subcommand methods that
    go through _getints-based dispatchers, returning () instead of None
    for void operations. These are pass-through values, not chainable.
    """

    def setUp(self):
        super().setUp()
        self.spinbox = tkinter.Spinbox(self.root, from_=0, to=100)
        self.spinbox.pack()
        self.root.update_idletasks()

    def test_get_returns_str(self):
        result = self.spinbox.get()
        self.assertIsInstance(result, str)

    def test_icursor_returns_str(self):
        # Spinbox.icursor returns '' (tk.call pass-through)
        result = self.spinbox.icursor(0)
        self.assertEqual(result, '')

    def test_identify_returns_str(self):
        result = self.spinbox.identify(10, 10)
        self.assertIsInstance(result, str)

    def test_insert_returns_str(self):
        # Spinbox.insert returns '' (tk.call pass-through)
        result = self.spinbox.insert(0, "5")
        self.assertEqual(result, '')

    def test_invoke_returns_str(self):
        # Spinbox.invoke returns '' or the result
        result = self.spinbox.invoke("buttonup")
        self.assertIsInstance(result, str)

    def test_scan_mark_returns_tuple(self):
        # Goes through scan() → _getints() or ()
        result = self.spinbox.scan_mark(0)
        self.assertIsInstance(result, tuple)

    def test_scan_dragto_returns_tuple(self):
        self.spinbox.scan_mark(0)
        result = self.spinbox.scan_dragto(10)
        self.assertIsInstance(result, tuple)

    def test_selection_adjust_returns_tuple(self):
        # Goes through selection() → _getints() or ()
        result = self.spinbox.selection_adjust(0)
        self.assertIsInstance(result, tuple)

    def test_selection_clear_returns_tuple(self):
        result = self.spinbox.selection_clear()
        self.assertIsInstance(result, tuple)

    def test_selection_element_getter_returns_str(self):
        result = self.spinbox.selection_element()
        self.assertIsInstance(result, str)

    def test_selection_element_setter_returns_str(self):
        result = self.spinbox.selection_element("buttonup")
        self.assertIsInstance(result, str)

    def test_selection_from_returns_self(self):
        result = self.spinbox.selection_from(0)
        self.assertIs(result, self.spinbox)

    def test_selection_present_returns_bool(self):
        result = self.spinbox.selection_present()
        self.assertIsInstance(result, bool)

    def test_selection_range_returns_self(self):
        result = self.spinbox.selection_range(0, 1)
        self.assertIs(result, self.spinbox)

    def test_selection_to_returns_self(self):
        result = self.spinbox.selection_to(1)
        self.assertIs(result, self.spinbox)


if __name__ == '__main__':
    unittest.main()
