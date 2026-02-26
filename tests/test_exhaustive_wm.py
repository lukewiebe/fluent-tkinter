"""Exhaustive tests for every wrapped method on tkinter.Wm.

Tests both getter mode (no args) and setter mode (with args) where applicable.
Wm methods are tested on a Toplevel widget.
"""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class WmMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Wm."""

    def setUp(self):
        super().setUp()
        self.toplevel = tkinter.Toplevel(self.root)
        self.toplevel.withdraw()
        self.root.update_idletasks()

    def tearDown(self):
        self.toplevel.destroy()
        super().tearDown()

    # ---- wm_aspect / aspect ----
    # _getints-based: getter returns self when unset (None→self), tuple when set

    def test_wm_aspect_getter_unset_returns_self(self):
        result = self.toplevel.wm_aspect()
        self.assertIs(result, self.toplevel)

    def test_wm_aspect_setter_returns_self(self):
        result = self.toplevel.wm_aspect(1, 1, 2, 1)
        self.assertIs(result, self.toplevel)

    def test_aspect_getter_unset_returns_self(self):
        result = self.toplevel.aspect()
        self.assertIs(result, self.toplevel)

    def test_aspect_setter_returns_self(self):
        result = self.toplevel.aspect(1, 1, 2, 1)
        self.assertIs(result, self.toplevel)

    # ---- wm_attributes / attributes ----
    # getter returns tuple, setter returns ''

    def test_wm_attributes_getter_returns_tuple(self):
        result = self.toplevel.wm_attributes()
        self.assertIsInstance(result, tuple)

    def test_wm_attributes_setter_returns_str(self):
        result = self.toplevel.wm_attributes("-topmost", True)
        self.assertEqual(result, '')

    def test_attributes_getter_returns_tuple(self):
        result = self.toplevel.attributes()
        self.assertIsInstance(result, tuple)

    def test_attributes_setter_returns_str(self):
        result = self.toplevel.attributes("-topmost", True)
        self.assertEqual(result, '')

    # ---- wm_client / client ----
    # getter returns '', setter returns ''

    def test_wm_client_getter_returns_str(self):
        result = self.toplevel.wm_client()
        self.assertIsInstance(result, str)

    def test_wm_client_setter_returns_str(self):
        result = self.toplevel.wm_client("testclient")
        self.assertEqual(result, '')

    def test_client_getter_returns_str(self):
        result = self.toplevel.client()
        self.assertIsInstance(result, str)

    def test_client_setter_returns_str(self):
        result = self.toplevel.client("testclient")
        self.assertEqual(result, '')

    # ---- wm_colormapwindows / colormapwindows ----
    # getter returns list, setter returns self (None→self)

    def test_wm_colormapwindows_getter_returns_list(self):
        result = self.toplevel.wm_colormapwindows()
        self.assertIsInstance(result, list)

    def test_wm_colormapwindows_setter_returns_self(self):
        result = self.toplevel.wm_colormapwindows([self.toplevel])
        self.assertIs(result, self.toplevel)

    def test_colormapwindows_getter_returns_list(self):
        result = self.toplevel.colormapwindows()
        self.assertIsInstance(result, list)

    def test_colormapwindows_setter_returns_self(self):
        result = self.toplevel.colormapwindows([self.toplevel])
        self.assertIs(result, self.toplevel)

    # ---- wm_command / command ----
    # getter returns '', setter returns ''

    def test_wm_command_getter_returns_str(self):
        result = self.toplevel.wm_command()
        self.assertIsInstance(result, str)

    def test_wm_command_setter_returns_str(self):
        result = self.toplevel.wm_command("test")
        self.assertEqual(result, '')

    def test_command_getter_returns_str(self):
        result = self.toplevel.command()
        self.assertIsInstance(result, str)

    def test_command_setter_returns_str(self):
        result = self.toplevel.command("test")
        self.assertEqual(result, '')

    # ---- wm_deiconify / deiconify ----
    # returns ''

    def test_wm_deiconify_returns_str(self):
        result = self.toplevel.wm_deiconify()
        self.assertEqual(result, '')

    def test_deiconify_returns_str(self):
        result = self.toplevel.deiconify()
        self.assertEqual(result, '')

    # ---- wm_focusmodel / focusmodel ----
    # getter returns str, setter returns ''

    def test_wm_focusmodel_getter_returns_str(self):
        result = self.toplevel.wm_focusmodel()
        self.assertIsInstance(result, str)

    def test_wm_focusmodel_setter_returns_str(self):
        result = self.toplevel.wm_focusmodel("active")
        self.assertEqual(result, '')

    def test_focusmodel_getter_returns_str(self):
        result = self.toplevel.focusmodel()
        self.assertIsInstance(result, str)

    def test_focusmodel_setter_returns_str(self):
        result = self.toplevel.focusmodel("active")
        self.assertEqual(result, '')

    # ---- wm_forget / forget ----
    # Dangerous to test in isolation; it converts a toplevel to a frame.
    # We test wm_manage to bring it back.

    def test_wm_forget_and_wm_manage(self):
        t = tkinter.Toplevel(self.root)
        t.withdraw()
        self.root.update_idletasks()
        path = str(t)
        t.wm_forget(path)
        result = t.wm_manage(path)
        self.assertIs(result, t)
        t.destroy()

    def test_forget_alias_exists(self):
        # forget on Wm is wm_forget; just verify it's callable
        self.assertTrue(callable(self.toplevel.forget))

    # ---- wm_frame / frame ----
    # returns str (window id)

    def test_wm_frame_returns_str(self):
        result = self.toplevel.wm_frame()
        self.assertIsInstance(result, str)

    def test_frame_returns_str(self):
        result = self.toplevel.frame()
        self.assertIsInstance(result, str)

    # ---- wm_geometry / geometry ----
    # getter returns str, setter returns ''

    def test_wm_geometry_getter_returns_str(self):
        result = self.toplevel.wm_geometry()
        self.assertIsInstance(result, str)

    def test_wm_geometry_setter_returns_str(self):
        result = self.toplevel.wm_geometry("100x100+0+0")
        self.assertEqual(result, '')

    def test_geometry_getter_returns_str(self):
        result = self.toplevel.geometry()
        self.assertIsInstance(result, str)

    def test_geometry_setter_returns_str(self):
        result = self.toplevel.geometry("100x100+0+0")
        self.assertEqual(result, '')

    # ---- wm_grid / grid ----
    # _getints-based: getter returns self when unset, setter returns self

    def test_wm_grid_getter_unset_returns_self(self):
        result = self.toplevel.wm_grid()
        self.assertIs(result, self.toplevel)

    def test_wm_grid_setter_returns_self(self):
        result = self.toplevel.wm_grid(1, 1, 10, 10)
        self.assertIs(result, self.toplevel)

    def test_grid_on_toplevel_getter_unset_returns_self(self):
        # On Toplevel, grid comes from Wm (= wm_grid), not Grid
        result = self.toplevel.grid()
        self.assertIs(result, self.toplevel)

    def test_grid_on_toplevel_setter_returns_self(self):
        result = self.toplevel.grid(1, 1, 10, 10)
        self.assertIs(result, self.toplevel)

    # ---- wm_group / group ----
    # getter returns '', setter returns ''

    def test_wm_group_getter_returns_str(self):
        result = self.toplevel.wm_group()
        self.assertIsInstance(result, str)

    def test_wm_group_setter_returns_str(self):
        result = self.toplevel.wm_group(self.root)
        self.assertEqual(result, '')

    def test_group_getter_returns_str(self):
        result = self.toplevel.group()
        self.assertIsInstance(result, str)

    def test_group_setter_returns_str(self):
        result = self.toplevel.group(self.root)
        self.assertEqual(result, '')

    # ---- wm_iconbitmap / iconbitmap ----
    # getter returns '', setter returns ''

    def test_wm_iconbitmap_getter_returns_str(self):
        result = self.toplevel.wm_iconbitmap()
        self.assertIsInstance(result, str)

    def test_wm_iconbitmap_setter_returns_str(self):
        result = self.toplevel.wm_iconbitmap("")
        self.assertEqual(result, '')

    def test_iconbitmap_getter_returns_str(self):
        result = self.toplevel.iconbitmap()
        self.assertIsInstance(result, str)

    def test_iconbitmap_setter_returns_str(self):
        result = self.toplevel.iconbitmap("")
        self.assertEqual(result, '')

    # ---- wm_iconify / iconify ----
    # returns ''

    def test_wm_iconify_returns_str(self):
        self.toplevel.deiconify()
        self.root.update_idletasks()
        result = self.toplevel.wm_iconify()
        self.assertEqual(result, '')

    def test_iconify_returns_str(self):
        self.toplevel.deiconify()
        self.root.update_idletasks()
        result = self.toplevel.iconify()
        self.assertEqual(result, '')

    # ---- wm_iconmask / iconmask ----
    # getter returns '', setter returns ''

    def test_wm_iconmask_getter_returns_str(self):
        result = self.toplevel.wm_iconmask()
        self.assertIsInstance(result, str)

    def test_wm_iconmask_setter_returns_str(self):
        result = self.toplevel.wm_iconmask("")
        self.assertEqual(result, '')

    def test_iconmask_getter_returns_str(self):
        result = self.toplevel.iconmask()
        self.assertIsInstance(result, str)

    def test_iconmask_setter_returns_str(self):
        result = self.toplevel.iconmask("")
        self.assertEqual(result, '')

    # ---- wm_iconname / iconname ----
    # getter returns '', setter returns ''

    def test_wm_iconname_getter_returns_str(self):
        result = self.toplevel.wm_iconname()
        self.assertIsInstance(result, str)

    def test_wm_iconname_setter_returns_str(self):
        result = self.toplevel.wm_iconname("test")
        self.assertEqual(result, '')

    def test_iconname_getter_returns_str(self):
        result = self.toplevel.iconname()
        self.assertIsInstance(result, str)

    def test_iconname_setter_returns_str(self):
        result = self.toplevel.iconname("test")
        self.assertEqual(result, '')

    # ---- wm_iconphoto / iconphoto ----

    def test_wm_iconphoto_returns_self(self):
        photo = tkinter.PhotoImage(master=self.root, width=16, height=16)
        result = self.toplevel.wm_iconphoto(True, photo)
        self.assertIs(result, self.toplevel)

    def test_iconphoto_returns_self(self):
        photo = tkinter.PhotoImage(master=self.root, width=16, height=16)
        result = self.toplevel.iconphoto(True, photo)
        self.assertIs(result, self.toplevel)

    # ---- wm_iconposition / iconposition ----
    # _getints-based: getter returns self when unset, setter returns self

    def test_wm_iconposition_getter_unset_returns_self(self):
        result = self.toplevel.wm_iconposition()
        self.assertIs(result, self.toplevel)

    def test_wm_iconposition_setter_returns_self(self):
        result = self.toplevel.wm_iconposition(10, 10)
        self.assertIs(result, self.toplevel)

    def test_iconposition_getter_unset_returns_self(self):
        result = self.toplevel.iconposition()
        self.assertIs(result, self.toplevel)

    def test_iconposition_setter_returns_self(self):
        result = self.toplevel.iconposition(10, 10)
        self.assertIs(result, self.toplevel)

    # ---- wm_iconwindow / iconwindow ----
    # getter returns '', setter returns ''

    def test_wm_iconwindow_getter_returns_str(self):
        result = self.toplevel.wm_iconwindow()
        self.assertIsInstance(result, str)

    def test_iconwindow_getter_returns_str(self):
        result = self.toplevel.iconwindow()
        self.assertIsInstance(result, str)

    # ---- wm_manage / manage ----
    # Tested together with wm_forget above

    # ---- wm_maxsize / maxsize ----
    # getter returns tuple (always set), setter returns self (_getints-based)

    def test_wm_maxsize_getter_returns_tuple(self):
        result = self.toplevel.wm_maxsize()
        self.assertIsInstance(result, tuple)

    def test_wm_maxsize_setter_returns_self(self):
        result = self.toplevel.wm_maxsize(1000, 1000)
        self.assertIs(result, self.toplevel)

    def test_maxsize_getter_returns_tuple(self):
        result = self.toplevel.maxsize()
        self.assertIsInstance(result, tuple)

    def test_maxsize_setter_returns_self(self):
        result = self.toplevel.maxsize(1000, 1000)
        self.assertIs(result, self.toplevel)

    # ---- wm_minsize / minsize ----
    # getter returns tuple (always set), setter returns self

    def test_wm_minsize_getter_returns_tuple(self):
        result = self.toplevel.wm_minsize()
        self.assertIsInstance(result, tuple)

    def test_wm_minsize_setter_returns_self(self):
        result = self.toplevel.wm_minsize(100, 100)
        self.assertIs(result, self.toplevel)

    def test_minsize_getter_returns_tuple(self):
        result = self.toplevel.minsize()
        self.assertIsInstance(result, tuple)

    def test_minsize_setter_returns_self(self):
        result = self.toplevel.minsize(100, 100)
        self.assertIs(result, self.toplevel)

    # ---- wm_positionfrom / positionfrom ----
    # getter returns '', setter returns ''

    def test_wm_positionfrom_getter_returns_str(self):
        result = self.toplevel.wm_positionfrom()
        self.assertIsInstance(result, str)

    def test_wm_positionfrom_setter_returns_str(self):
        result = self.toplevel.wm_positionfrom("user")
        self.assertEqual(result, '')

    def test_positionfrom_getter_returns_str(self):
        result = self.toplevel.positionfrom()
        self.assertIsInstance(result, str)

    def test_positionfrom_setter_returns_str(self):
        result = self.toplevel.positionfrom("user")
        self.assertEqual(result, '')

    # ---- wm_protocol / protocol ----
    # no-arg getter returns tuple, one-arg getter returns '',
    # two-arg setter returns ''

    def test_wm_protocol_list_returns_tuple(self):
        result = self.toplevel.wm_protocol()
        self.assertIsInstance(result, tuple)

    def test_wm_protocol_setter_returns_str(self):
        result = self.toplevel.wm_protocol("WM_DELETE_WINDOW", lambda: None)
        self.assertEqual(result, '')

    def test_protocol_list_returns_tuple(self):
        result = self.toplevel.protocol()
        self.assertIsInstance(result, tuple)

    def test_protocol_setter_returns_str(self):
        result = self.toplevel.protocol("WM_DELETE_WINDOW", lambda: None)
        self.assertEqual(result, '')

    # ---- wm_resizable / resizable ----
    # getter returns tuple, setter returns ''

    def test_wm_resizable_getter_returns_tuple(self):
        result = self.toplevel.wm_resizable()
        self.assertIsInstance(result, tuple)

    def test_wm_resizable_setter_returns_str(self):
        result = self.toplevel.wm_resizable(True, True)
        self.assertEqual(result, '')

    def test_resizable_getter_returns_tuple(self):
        result = self.toplevel.resizable()
        self.assertIsInstance(result, tuple)

    def test_resizable_setter_returns_str(self):
        result = self.toplevel.resizable(True, True)
        self.assertEqual(result, '')

    # ---- wm_sizefrom / sizefrom ----
    # getter returns '', setter returns ''

    def test_wm_sizefrom_getter_returns_str(self):
        result = self.toplevel.wm_sizefrom()
        self.assertIsInstance(result, str)

    def test_wm_sizefrom_setter_returns_str(self):
        result = self.toplevel.wm_sizefrom("user")
        self.assertEqual(result, '')

    def test_sizefrom_getter_returns_str(self):
        result = self.toplevel.sizefrom()
        self.assertIsInstance(result, str)

    def test_sizefrom_setter_returns_str(self):
        result = self.toplevel.sizefrom("user")
        self.assertEqual(result, '')

    # ---- wm_state / state ----
    # getter returns str, setter returns ''

    def test_wm_state_getter_returns_str(self):
        result = self.toplevel.wm_state()
        self.assertIsInstance(result, str)

    def test_wm_state_setter_returns_str(self):
        result = self.toplevel.wm_state("normal")
        self.assertEqual(result, '')

    def test_state_getter_returns_str(self):
        result = self.toplevel.state()
        self.assertIsInstance(result, str)

    def test_state_setter_returns_str(self):
        result = self.toplevel.state("normal")
        self.assertEqual(result, '')

    # ---- wm_title / title ----
    # getter returns str, setter returns ''

    def test_wm_title_getter_returns_str(self):
        result = self.toplevel.wm_title()
        self.assertIsInstance(result, str)

    def test_wm_title_setter_returns_str(self):
        result = self.toplevel.wm_title("Test Title")
        self.assertEqual(result, '')

    def test_title_getter_returns_str(self):
        result = self.toplevel.title()
        self.assertIsInstance(result, str)

    def test_title_setter_returns_str(self):
        result = self.toplevel.title("Test Title")
        self.assertEqual(result, '')

    # ---- wm_transient / transient ----
    # getter returns '', setter returns ''

    def test_wm_transient_getter_returns_str(self):
        result = self.toplevel.wm_transient()
        self.assertIsInstance(result, str)

    def test_wm_transient_setter_returns_str(self):
        result = self.toplevel.wm_transient(self.root)
        self.assertEqual(result, '')

    def test_transient_getter_returns_str(self):
        result = self.toplevel.transient()
        self.assertIsInstance(result, str)

    def test_transient_setter_returns_str(self):
        result = self.toplevel.transient(self.root)
        self.assertEqual(result, '')

    # ---- wm_withdraw / withdraw ----
    # returns ''

    def test_wm_withdraw_returns_str(self):
        result = self.toplevel.wm_withdraw()
        self.assertEqual(result, '')

    def test_withdraw_returns_str(self):
        result = self.toplevel.withdraw()
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
