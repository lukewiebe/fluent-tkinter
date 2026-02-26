"""Exhaustive tests for wrapped methods on tkinter.Button and tkinter.Checkbutton,
tkinter.Radiobutton.
"""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class ButtonMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Button."""

    def setUp(self):
        super().setUp()
        self.button = tkinter.Button(self.root, text="test")

    def test_flash_returns_self(self):
        result = self.button.flash()
        self.assertIs(result, self.button)

    def test_invoke_returns_str(self):
        # invoke returns the command's return value; '' when no command
        result = self.button.invoke()
        self.assertEqual(result, '')

    def test_invoke_returns_command_result(self):
        btn = tkinter.Button(self.root, text="test", command=lambda: "clicked")
        result = btn.invoke()
        self.assertEqual(result, "clicked")


class CheckbuttonMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Checkbutton."""

    def setUp(self):
        super().setUp()
        self.cb = tkinter.Checkbutton(self.root, text="test")

    def test_deselect_returns_self(self):
        result = self.cb.deselect()
        self.assertIs(result, self.cb)

    def test_flash_returns_self(self):
        result = self.cb.flash()
        self.assertIs(result, self.cb)

    def test_invoke_returns_str(self):
        result = self.cb.invoke()
        self.assertEqual(result, '')

    def test_select_returns_self(self):
        result = self.cb.select()
        self.assertIs(result, self.cb)

    def test_toggle_returns_self(self):
        result = self.cb.toggle()
        self.assertIs(result, self.cb)


class RadiobuttonMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Radiobutton."""

    def setUp(self):
        super().setUp()
        self.rb = tkinter.Radiobutton(self.root, text="test")

    def test_deselect_returns_self(self):
        result = self.rb.deselect()
        self.assertIs(result, self.rb)

    def test_flash_returns_self(self):
        result = self.rb.flash()
        self.assertIs(result, self.rb)

    def test_invoke_returns_str(self):
        result = self.rb.invoke()
        self.assertEqual(result, '')

    def test_select_returns_self(self):
        result = self.rb.select()
        self.assertIs(result, self.rb)


if __name__ == '__main__':
    unittest.main()
