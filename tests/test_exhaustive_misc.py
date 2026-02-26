"""Exhaustive tests for every wrapped method on tkinter.Misc.

Each test calls a single wrapped method and asserts whether it returns
``self`` (chainable) or passes through a value (non-chainable).
"""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class MiscMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Misc."""

    def setUp(self):
        super().setUp()
        self.frame = tkinter.Frame(self.root, width=100, height=100)
        self.frame.pack()
        self.root.update_idletasks()

    # -- Methods that return self (chainable) --

    def test_after_cancel_returns_self(self):
        aid = self.frame.after(10000, lambda: None)
        result = self.frame.after_cancel(aid)
        self.assertIs(result, self.frame)

    def test_anchor_returns_self(self):
        result = self.frame.anchor("nw")
        self.assertIs(result, self.frame)

    def test_bell_returns_self(self):
        result = self.frame.bell()
        self.assertIs(result, self.frame)

    def test_clipboard_append_returns_self(self):
        self.frame.clipboard_clear()
        result = self.frame.clipboard_append("test")
        self.assertIs(result, self.frame)

    def test_clipboard_clear_returns_self(self):
        result = self.frame.clipboard_clear()
        self.assertIs(result, self.frame)

    def test_columnconfigure_returns_self(self):
        result = self.frame.columnconfigure(0, weight=1)
        self.assertIs(result, self.frame)

    def test_config_setter_returns_self(self):
        result = self.frame.config(width=50)
        self.assertIs(result, self.frame)

    def test_configure_setter_returns_self(self):
        result = self.frame.configure(width=50)
        self.assertIs(result, self.frame)

    def test_event_add_returns_self(self):
        result = self.frame.event_add("<<Test>>", "<Control-t>")
        self.assertIs(result, self.frame)
        self.frame.event_delete("<<Test>>")

    def test_event_delete_returns_self(self):
        self.frame.event_add("<<Test>>", "<Control-t>")
        result = self.frame.event_delete("<<Test>>")
        self.assertIs(result, self.frame)

    def test_event_generate_returns_self(self):
        result = self.frame.event_generate("<Button-1>")
        self.assertIs(result, self.frame)

    def test_focus_returns_self(self):
        result = self.frame.focus()
        self.assertIs(result, self.frame)

    def test_focus_force_returns_self(self):
        result = self.frame.focus_force()
        self.assertIs(result, self.frame)

    def test_focus_set_returns_self(self):
        result = self.frame.focus_set()
        self.assertIs(result, self.frame)

    def test_grab_release_returns_self(self):
        result = self.frame.grab_release()
        self.assertIs(result, self.frame)

    def test_grab_set_returns_self(self):
        result = self.frame.grab_set()
        self.assertIs(result, self.frame)
        self.frame.grab_release()

    def test_grid_anchor_returns_self(self):
        result = self.frame.grid_anchor("nw")
        self.assertIs(result, self.frame)

    def test_grid_columnconfigure_returns_self(self):
        result = self.frame.grid_columnconfigure(0, weight=1)
        self.assertIs(result, self.frame)

    def test_grid_rowconfigure_returns_self(self):
        result = self.frame.grid_rowconfigure(0, weight=1)
        self.assertIs(result, self.frame)

    def test_lift_returns_self(self):
        result = self.frame.lift()
        self.assertIs(result, self.frame)

    def test_lower_returns_self(self):
        result = self.frame.lower()
        self.assertIs(result, self.frame)

    def test_option_add_returns_self(self):
        result = self.frame.option_add("*Font", "Courier")
        self.assertIs(result, self.frame)

    def test_option_clear_returns_self(self):
        result = self.frame.option_clear()
        self.assertIs(result, self.frame)

    def test_rowconfigure_returns_self(self):
        result = self.frame.rowconfigure(0, weight=1)
        self.assertIs(result, self.frame)

    def test_selection_clear_returns_self(self):
        result = self.frame.selection_clear()
        self.assertIs(result, self.frame)

    def test_selection_handle_returns_self(self):
        result = self.frame.selection_handle(lambda offset, length: "")
        self.assertIs(result, self.frame)

    def test_selection_own_returns_self(self):
        result = self.frame.selection_own()
        self.assertIs(result, self.frame)

    def test_setvar_returns_self(self):
        v = tkinter.StringVar(self.root, name="testvar")
        result = self.frame.setvar("testvar", "hello")
        self.assertIs(result, self.frame)

    def test_tk_bisque_returns_self(self):
        result = self.frame.tk_bisque()
        self.assertIs(result, self.frame)

    def test_tk_focusFollowsMouse_returns_self(self):
        result = self.frame.tk_focusFollowsMouse()
        self.assertIs(result, self.frame)

    def test_tk_setPalette_returns_self(self):
        result = self.frame.tk_setPalette("background", "#ffffff")
        self.assertIs(result, self.frame)

    def test_tkraise_returns_self(self):
        result = self.frame.tkraise()
        self.assertIs(result, self.frame)

    def test_unbind_returns_self(self):
        self.frame.bind("<Button-1>", lambda e: None)
        result = self.frame.unbind("<Button-1>")
        self.assertIs(result, self.frame)

    def test_unbind_all_returns_self(self):
        result = self.frame.unbind_all("<Button-1>")
        self.assertIs(result, self.frame)

    def test_unbind_class_returns_self(self):
        result = self.frame.unbind_class("Frame", "<Button-1>")
        self.assertIs(result, self.frame)

    def test_update_returns_self(self):
        result = self.frame.update()
        self.assertIs(result, self.frame)

    def test_update_idletasks_returns_self(self):
        result = self.frame.update_idletasks()
        self.assertIs(result, self.frame)

    # -- Methods that return values (pass-through) --

    def test_after_idle_returns_str(self):
        result = self.frame.after_idle(lambda: None)
        self.assertIsInstance(result, str)

    def test_bind_returns_funcid(self):
        result = self.frame.bind("<Button-1>", lambda e: None)
        self.assertIsInstance(result, str)
        self.frame.unbind("<Button-1>")

    def test_bind_all_returns_funcid(self):
        result = self.frame.bind_all("<Button-1>", lambda e: None)
        self.assertIsInstance(result, str)
        self.frame.unbind_all("<Button-1>")

    def test_bind_class_returns_funcid(self):
        result = self.frame.bind_class("Frame", "<Button-1>", lambda e: None)
        self.assertIsInstance(result, str)
        self.frame.unbind_class("Frame", "<Button-1>")

    def test_bindtags_returns_tuple(self):
        result = self.frame.bindtags()
        self.assertIsInstance(result, tuple)

    def test_cget_returns_value(self):
        result = self.frame.cget("width")
        self.assertIsNotNone(result)

    def test_clipboard_get_returns_str(self):
        self.frame.clipboard_clear()
        self.frame.clipboard_append("test_data")
        result = self.frame.clipboard_get()
        self.assertEqual(result, "test_data")

    def test_configure_getter_returns_dict(self):
        result = self.frame.configure()
        self.assertIsInstance(result, dict)

    def test_deletecommand_returns_self(self):
        name = self.frame.register(lambda: None)
        result = self.frame.deletecommand(name)
        self.assertIs(result, self.frame)

    def test_event_info_returns_tuple(self):
        result = self.frame.event_info()
        self.assertIsInstance(result, tuple)

    def test_getboolean_returns_bool(self):
        result = self.frame.getboolean(1)
        self.assertIsInstance(result, bool)

    def test_getdouble_returns_float(self):
        result = self.frame.getdouble("3.14")
        self.assertIsInstance(result, float)

    def test_getint_returns_int(self):
        result = self.frame.getint("42")
        self.assertIsInstance(result, int)

    def test_getvar_returns_value(self):
        v = tkinter.StringVar(self.root, name="gv_test", value="hello")
        result = self.frame.getvar("gv_test")
        self.assertEqual(result, "hello")

    def test_grid_slaves_returns_list(self):
        result = self.frame.grid_slaves()
        self.assertIsInstance(result, list)

    def test_image_names_returns_tuple(self):
        result = self.frame.image_names()
        self.assertIsInstance(result, tuple)

    def test_image_types_returns_tuple(self):
        result = self.frame.image_types()
        self.assertIsInstance(result, tuple)

    def test_info_patchlevel_returns_value(self):
        result = self.frame.info_patchlevel()
        self.assertIsNotNone(result)

    def test_keys_returns_list(self):
        result = self.frame.keys()
        self.assertIsInstance(result, list)

    def test_nametowidget_returns_widget(self):
        result = self.frame.nametowidget(".")
        self.assertIs(result, self.root)

    def test_option_get_returns_str(self):
        result = self.frame.option_get("font", "Font")
        self.assertIsInstance(result, str)

    def test_pack_slaves_returns_list(self):
        result = self.frame.pack_slaves()
        self.assertIsInstance(result, list)

    def test_place_slaves_returns_list(self):
        result = self.frame.place_slaves()
        self.assertIsInstance(result, list)

    def test_register_returns_str(self):
        result = self.frame.register(lambda: None)
        self.assertIsInstance(result, str)

    def test_slaves_returns_list(self):
        result = self.frame.slaves()
        self.assertIsInstance(result, list)

    def test_tk_strictMotif_returns_bool(self):
        result = self.frame.tk_strictMotif(False)
        self.assertIsInstance(result, bool)

    # -- winfo methods (all return values) --

    def test_winfo_atom_returns_int(self):
        result = self.frame.winfo_atom("WM_DELETE_WINDOW")
        self.assertIsInstance(result, int)

    def test_winfo_atomname_returns_str(self):
        result = self.frame.winfo_atomname(1)
        self.assertIsInstance(result, str)

    def test_winfo_cells_returns_int(self):
        result = self.frame.winfo_cells()
        self.assertIsInstance(result, int)

    def test_winfo_children_returns_list(self):
        result = self.frame.winfo_children()
        self.assertIsInstance(result, list)

    def test_winfo_class_returns_str(self):
        result = self.frame.winfo_class()
        self.assertEqual(result, "Frame")

    def test_winfo_colormapfull_returns_bool(self):
        result = self.frame.winfo_colormapfull()
        self.assertIsInstance(result, bool)

    def test_winfo_depth_returns_int(self):
        result = self.frame.winfo_depth()
        self.assertIsInstance(result, int)

    def test_winfo_exists_returns_int(self):
        result = self.frame.winfo_exists()
        self.assertIsInstance(result, int)

    def test_winfo_fpixels_returns_float(self):
        result = self.frame.winfo_fpixels("1i")
        self.assertIsInstance(result, float)

    def test_winfo_geometry_returns_str(self):
        result = self.frame.winfo_geometry()
        self.assertIsInstance(result, str)

    def test_winfo_height_returns_int(self):
        result = self.frame.winfo_height()
        self.assertIsInstance(result, int)

    def test_winfo_id_returns_int(self):
        result = self.frame.winfo_id()
        self.assertIsInstance(result, int)

    def test_winfo_interps_returns_tuple(self):
        result = self.frame.winfo_interps()
        self.assertIsInstance(result, tuple)

    def test_winfo_ismapped_returns_int(self):
        result = self.frame.winfo_ismapped()
        self.assertIsInstance(result, int)

    def test_winfo_manager_returns_str(self):
        result = self.frame.winfo_manager()
        self.assertIsInstance(result, str)

    def test_winfo_name_returns_str(self):
        result = self.frame.winfo_name()
        self.assertIsInstance(result, str)

    def test_winfo_parent_returns_str(self):
        result = self.frame.winfo_parent()
        self.assertIsInstance(result, str)

    def test_winfo_pathname_returns_str(self):
        result = self.frame.winfo_pathname(self.frame.winfo_id())
        self.assertIsInstance(result, str)

    def test_winfo_pixels_returns_int(self):
        result = self.frame.winfo_pixels("1i")
        self.assertIsInstance(result, int)

    def test_winfo_pointerx_returns_int(self):
        result = self.frame.winfo_pointerx()
        self.assertIsInstance(result, int)

    def test_winfo_pointerxy_returns_tuple(self):
        result = self.frame.winfo_pointerxy()
        self.assertIsInstance(result, tuple)

    def test_winfo_pointery_returns_int(self):
        result = self.frame.winfo_pointery()
        self.assertIsInstance(result, int)

    def test_winfo_reqheight_returns_int(self):
        result = self.frame.winfo_reqheight()
        self.assertIsInstance(result, int)

    def test_winfo_reqwidth_returns_int(self):
        result = self.frame.winfo_reqwidth()
        self.assertIsInstance(result, int)

    def test_winfo_rgb_returns_tuple(self):
        result = self.frame.winfo_rgb("red")
        self.assertIsInstance(result, tuple)

    def test_winfo_rootx_returns_int(self):
        result = self.frame.winfo_rootx()
        self.assertIsInstance(result, int)

    def test_winfo_rooty_returns_int(self):
        result = self.frame.winfo_rooty()
        self.assertIsInstance(result, int)

    def test_winfo_screen_returns_str(self):
        result = self.frame.winfo_screen()
        self.assertIsInstance(result, str)

    def test_winfo_screencells_returns_int(self):
        result = self.frame.winfo_screencells()
        self.assertIsInstance(result, int)

    def test_winfo_screendepth_returns_int(self):
        result = self.frame.winfo_screendepth()
        self.assertIsInstance(result, int)

    def test_winfo_screenheight_returns_int(self):
        result = self.frame.winfo_screenheight()
        self.assertIsInstance(result, int)

    def test_winfo_screenmmheight_returns_int(self):
        result = self.frame.winfo_screenmmheight()
        self.assertIsInstance(result, int)

    def test_winfo_screenmmwidth_returns_int(self):
        result = self.frame.winfo_screenmmwidth()
        self.assertIsInstance(result, int)

    def test_winfo_screenvisual_returns_str(self):
        result = self.frame.winfo_screenvisual()
        self.assertIsInstance(result, str)

    def test_winfo_screenwidth_returns_int(self):
        result = self.frame.winfo_screenwidth()
        self.assertIsInstance(result, int)

    def test_winfo_server_returns_str(self):
        result = self.frame.winfo_server()
        self.assertIsInstance(result, str)

    def test_winfo_toplevel_returns_widget(self):
        result = self.frame.winfo_toplevel()
        self.assertIs(result, self.root)

    def test_winfo_viewable_returns_int(self):
        result = self.frame.winfo_viewable()
        self.assertIsInstance(result, int)

    def test_winfo_visual_returns_str(self):
        result = self.frame.winfo_visual()
        self.assertIsInstance(result, str)

    def test_winfo_visualid_returns_str(self):
        result = self.frame.winfo_visualid()
        self.assertIsInstance(result, str)

    def test_winfo_visualsavailable_returns_list(self):
        result = self.frame.winfo_visualsavailable()
        self.assertIsInstance(result, list)

    def test_winfo_vrootheight_returns_int(self):
        result = self.frame.winfo_vrootheight()
        self.assertIsInstance(result, int)

    def test_winfo_vrootwidth_returns_int(self):
        result = self.frame.winfo_vrootwidth()
        self.assertIsInstance(result, int)

    def test_winfo_vrootx_returns_int(self):
        result = self.frame.winfo_vrootx()
        self.assertIsInstance(result, int)

    def test_winfo_vrooty_returns_int(self):
        result = self.frame.winfo_vrooty()
        self.assertIsInstance(result, int)

    def test_winfo_width_returns_int(self):
        result = self.frame.winfo_width()
        self.assertIsInstance(result, int)

    def test_winfo_x_returns_int(self):
        result = self.frame.winfo_x()
        self.assertIsInstance(result, int)

    def test_winfo_y_returns_int(self):
        result = self.frame.winfo_y()
        self.assertIsInstance(result, int)

    # -- Blocking / dangerous methods skipped with reason --
    # mainloop, quit: block or exit the event loop
    # wait_variable, wait_visibility, wait_window, waitvar: block
    # send: inter-application communication, typically disabled
    # option_readfile: needs a real option file
    # grab_set_global: needs viewable window, may interfere with other tests


if __name__ == '__main__':
    unittest.main()
