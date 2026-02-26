"""Exhaustive tests for wrapped methods on tkinter.Menu."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class MenuMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Menu."""

    def setUp(self):
        super().setUp()
        self.menu = tkinter.Menu(self.root, tearoff=0)
        self.menu.add_command(label="test_item")

    def test_add_returns_self(self):
        result = self.menu.add("command", label="added")
        self.assertIs(result, self.menu)

    def test_add_cascade_returns_self(self):
        result = self.menu.add_cascade(label="cascade")
        self.assertIs(result, self.menu)

    def test_add_checkbutton_returns_self(self):
        result = self.menu.add_checkbutton(label="check")
        self.assertIs(result, self.menu)

    def test_add_command_returns_self(self):
        result = self.menu.add_command(label="cmd")
        self.assertIs(result, self.menu)

    def test_add_radiobutton_returns_self(self):
        result = self.menu.add_radiobutton(label="radio")
        self.assertIs(result, self.menu)

    def test_add_separator_returns_self(self):
        result = self.menu.add_separator()
        self.assertIs(result, self.menu)

    def test_entrycget_returns_str(self):
        result = self.menu.entrycget(0, "label")
        self.assertEqual(result, "test_item")

    def test_entryconfig_setter_returns_self(self):
        result = self.menu.entryconfig(0, label="new_label")
        self.assertIs(result, self.menu)

    def test_entryconfigure_setter_returns_self(self):
        result = self.menu.entryconfigure(0, label="new_label2")
        self.assertIs(result, self.menu)

    def test_insert_returns_self(self):
        result = self.menu.insert(0, "command", label="inserted")
        self.assertIs(result, self.menu)

    def test_insert_cascade_returns_self(self):
        result = self.menu.insert_cascade(0, label="cas")
        self.assertIs(result, self.menu)

    def test_insert_checkbutton_returns_self(self):
        result = self.menu.insert_checkbutton(0, label="chk")
        self.assertIs(result, self.menu)

    def test_insert_command_returns_self(self):
        result = self.menu.insert_command(0, label="cmd")
        self.assertIs(result, self.menu)

    def test_insert_radiobutton_returns_self(self):
        result = self.menu.insert_radiobutton(0, label="rad")
        self.assertIs(result, self.menu)

    def test_insert_separator_returns_self(self):
        result = self.menu.insert_separator(0)
        self.assertIs(result, self.menu)

    def test_invoke_returns_str(self):
        result = self.menu.invoke(0)
        self.assertEqual(result, '')

    def test_post_returns_self(self):
        result = self.menu.post(0, 0)
        self.assertIs(result, self.menu)

    def test_tk_popup_returns_self(self):
        result = self.menu.tk_popup(0, 0)
        self.assertIs(result, self.menu)

    def test_unpost_returns_self(self):
        result = self.menu.unpost()
        self.assertIs(result, self.menu)

    def test_xposition_returns_int(self):
        result = self.menu.xposition(0)
        self.assertIsInstance(result, int)

    def test_yposition_returns_int(self):
        result = self.menu.yposition(0)
        self.assertIsInstance(result, int)


if __name__ == '__main__':
    unittest.main()
