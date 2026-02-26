"""Exhaustive tests for wrapped methods on tkinter.PanedWindow."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class PanedWindowMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.PanedWindow."""

    def setUp(self):
        super().setUp()
        self.pw = tkinter.PanedWindow(self.root, orient="horizontal")
        self.pw.pack(fill="both", expand=True)
        self.pane1 = tkinter.Frame(self.pw, width=50, height=50)
        self.pane2 = tkinter.Frame(self.pw, width=50, height=50)
        self.pw.add(self.pane1)
        self.pw.add(self.pane2)
        self.root.update_idletasks()

    def test_add_returns_self(self):
        pane3 = tkinter.Frame(self.pw)
        result = self.pw.add(pane3)
        self.assertIs(result, self.pw)

    def test_forget_returns_self(self):
        result = self.pw.forget(self.pane2)
        self.assertIs(result, self.pw)

    def test_identify_returns_str(self):
        result = self.pw.identify(10, 10)
        # Returns '' or a string description
        self.assertIsInstance(result, str)

    def test_panecget_returns_str(self):
        result = self.pw.panecget(self.pane1, "width")
        self.assertIsInstance(result, str)

    def test_paneconfig_setter_returns_self(self):
        result = self.pw.paneconfig(self.pane1, width=50)
        self.assertIs(result, self.pw)

    def test_paneconfigure_setter_returns_self(self):
        result = self.pw.paneconfigure(self.pane1, width=60)
        self.assertIs(result, self.pw)

    def test_panes_returns_tuple(self):
        result = self.pw.panes()
        self.assertIsInstance(result, tuple)

    def test_proxy_coord_returns_tuple(self):
        result = self.pw.proxy_coord()
        self.assertIsInstance(result, tuple)

    def test_proxy_forget_returns_tuple(self):
        result = self.pw.proxy_forget()
        self.assertIsInstance(result, tuple)

    def test_proxy_place_returns_tuple(self):
        result = self.pw.proxy_place(50, 50)
        self.assertIsInstance(result, tuple)

    def test_remove_returns_self(self):
        result = self.pw.remove(self.pane2)
        self.assertIs(result, self.pw)

    def test_sash_coord_returns_tuple(self):
        result = self.pw.sash_coord(0)
        self.assertIsInstance(result, tuple)

    def test_sash_place_returns_tuple(self):
        result = self.pw.sash_place(0, 50, 0)
        self.assertIsInstance(result, tuple)


if __name__ == '__main__':
    unittest.main()
