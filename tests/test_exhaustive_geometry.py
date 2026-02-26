"""Exhaustive tests for wrapped methods on Grid, Pack, Place, BaseWidget, Tk.

These are the geometry manager mixins and core base classes.
"""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class GridMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Grid."""

    def setUp(self):
        super().setUp()
        self.container = tkinter.Frame(self.root)
        self.container.pack()
        self.widget = tkinter.Frame(self.container)

    # grid_configure / grid / configure / config (all aliases for grid placement)

    def test_grid_configure_returns_self(self):
        result = self.widget.grid_configure(row=0, column=0)
        self.assertIs(result, self.widget)

    def test_grid_alias_returns_self(self):
        # grid is an alias for grid_configure on Grid class
        result = self.widget.grid(row=0, column=0)
        self.assertIs(result, self.widget)

    # grid_forget / forget

    def test_grid_forget_returns_self(self):
        self.widget.grid(row=0, column=0)
        result = self.widget.grid_forget()
        self.assertIs(result, self.widget)

    # grid_info / info — returns dict

    def test_grid_info_returns_dict(self):
        self.widget.grid(row=0, column=0)
        result = self.widget.grid_info()
        self.assertIsInstance(result, dict)

    def test_grid_info_on_ungridded_returns_dict(self):
        result = self.widget.grid_info()
        self.assertIsInstance(result, dict)

    # grid_remove

    def test_grid_remove_returns_self(self):
        self.widget.grid(row=0, column=0)
        result = self.widget.grid_remove()
        self.assertIs(result, self.widget)

    # grid_columnconfigure / columnconfigure

    def test_grid_columnconfigure_setter_returns_self(self):
        result = self.container.grid_columnconfigure(0, weight=1)
        self.assertIs(result, self.container)

    def test_columnconfigure_setter_returns_self(self):
        result = self.container.columnconfigure(0, weight=1)
        self.assertIs(result, self.container)

    # grid_rowconfigure / rowconfigure

    def test_grid_rowconfigure_setter_returns_self(self):
        result = self.container.grid_rowconfigure(0, weight=1)
        self.assertIs(result, self.container)

    def test_rowconfigure_setter_returns_self(self):
        result = self.container.rowconfigure(0, weight=1)
        self.assertIs(result, self.container)

    # grid_slaves / slaves — returns list

    def test_grid_slaves_returns_list(self):
        self.widget.grid(row=0, column=0)
        result = self.container.grid_slaves()
        self.assertIsInstance(result, list)

    def test_slaves_on_grid_returns_list(self):
        self.widget.grid(row=0, column=0)
        result = self.container.slaves()
        self.assertIsInstance(result, list)


class PackMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Pack."""

    def setUp(self):
        super().setUp()
        self.widget = tkinter.Frame(self.root)

    # pack_configure / pack / configure / config

    def test_pack_configure_returns_self(self):
        result = self.widget.pack_configure()
        self.assertIs(result, self.widget)

    def test_pack_alias_returns_self(self):
        self.widget.pack_forget()
        result = self.widget.pack()
        self.assertIs(result, self.widget)

    # pack_forget / forget

    def test_pack_forget_returns_self(self):
        self.widget.pack()
        result = self.widget.pack_forget()
        self.assertIs(result, self.widget)

    # pack_info / info — returns dict

    def test_pack_info_returns_dict(self):
        self.widget.pack()
        result = self.widget.pack_info()
        self.assertIsInstance(result, dict)

    # pack_slaves / slaves — returns list

    def test_pack_slaves_returns_list(self):
        result = self.root.pack_slaves()
        self.assertIsInstance(result, list)


class PlaceMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Place."""

    def setUp(self):
        super().setUp()
        self.widget = tkinter.Frame(self.root)

    # place_configure / place / configure / config

    def test_place_configure_returns_self(self):
        result = self.widget.place_configure(x=0, y=0)
        self.assertIs(result, self.widget)

    def test_place_alias_returns_self(self):
        result = self.widget.place(x=10, y=10)
        self.assertIs(result, self.widget)

    # place_forget / forget

    def test_place_forget_returns_self(self):
        self.widget.place(x=0, y=0)
        result = self.widget.place_forget()
        self.assertIs(result, self.widget)

    # place_info / info — returns dict

    def test_place_info_returns_dict(self):
        self.widget.place(x=0, y=0)
        result = self.widget.place_info()
        self.assertIsInstance(result, dict)

    # place_slaves / slaves — returns list

    def test_place_slaves_returns_list(self):
        result = self.root.place_slaves()
        self.assertIsInstance(result, list)


class BaseWidgetMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on tkinter.BaseWidget."""

    def test_destroy_returns_self(self):
        f = tkinter.Frame(self.root)
        result = f.destroy()
        self.assertIs(result, f)


class TkMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on tkinter.Tk."""

    def test_loadtk_returns_self(self):
        result = self.root.loadtk()
        self.assertIs(result, self.root)

    def test_readprofile_returns_self(self):
        result = self.root.readprofile("nonexistent", "nonexistent")
        self.assertIs(result, self.root)

    def test_report_callback_exception_returns_self(self):
        result = self.root.report_callback_exception(
            ValueError, ValueError("test"), None
        )
        self.assertIs(result, self.root)

    def test_destroy_returns_self(self):
        # Tk.destroy is its own method, distinct from BaseWidget.destroy
        # We can't easily destroy self.root (test harness needs it),
        # so create a second Tk and destroy it.
        tk2 = tkinter.Tk()
        tk2.withdraw()
        result = tk2.destroy()
        self.assertIs(result, tk2)


class ToplevelMethodsTest(AbstractTkTest, unittest.TestCase):
    """Toplevel defines no methods beyond inherited ones.

    This test verifies that Toplevel inherits fluent behavior correctly.
    """

    def test_toplevel_configure_returns_self(self):
        t = tkinter.Toplevel(self.root)
        t.withdraw()
        result = t.configure(width=200)
        self.assertIs(result, t)
        t.destroy()


class OptionMenuMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on tkinter.OptionMenu."""

    def test_destroy_returns_self(self):
        var = tkinter.StringVar(self.root, "opt1")
        om = tkinter.OptionMenu(self.root, var, "opt1", "opt2")
        result = om.destroy()
        self.assertIs(result, om)


if __name__ == '__main__':
    unittest.main()
