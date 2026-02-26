"""Exhaustive tests for wrapped methods on tkinter.Scale and tkinter.Scrollbar."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class ScaleMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Scale."""

    def setUp(self):
        super().setUp()
        self.scale = tkinter.Scale(self.root, from_=0, to=100)
        self.scale.pack()
        self.root.update_idletasks()

    def test_coords_returns_tuple(self):
        result = self.scale.coords()
        self.assertIsInstance(result, tuple)

    def test_get_returns_number(self):
        result = self.scale.get()
        self.assertIsInstance(result, (int, float))

    def test_identify_returns_str(self):
        result = self.scale.identify(10, 10)
        self.assertIsInstance(result, str)

    def test_set_returns_self(self):
        result = self.scale.set(50)
        self.assertIs(result, self.scale)


class ScrollbarMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Scrollbar."""

    def setUp(self):
        super().setUp()
        self.scrollbar = tkinter.Scrollbar(self.root)
        self.scrollbar.pack()
        self.root.update_idletasks()

    def test_delta_returns_float(self):
        result = self.scrollbar.delta(10, 10)
        self.assertIsInstance(result, float)

    def test_fraction_returns_float(self):
        result = self.scrollbar.fraction(10, 10)
        self.assertIsInstance(result, float)

    def test_get_returns_tuple(self):
        result = self.scrollbar.get()
        self.assertIsInstance(result, tuple)

    def test_identify_returns_str(self):
        result = self.scrollbar.identify(10, 10)
        self.assertIsInstance(result, str)

    def test_set_returns_self(self):
        result = self.scrollbar.set(0.0, 1.0)
        self.assertIs(result, self.scrollbar)


if __name__ == '__main__':
    unittest.main()
