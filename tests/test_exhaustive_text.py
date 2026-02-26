"""Exhaustive tests for every wrapped method on tkinter.Text."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class TextMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Text."""

    def setUp(self):
        super().setUp()
        self.text = tkinter.Text(self.root, undo=True)
        self.text.pack()
        self.text.insert("1.0", "Hello World\nSecond Line\n")
        self.root.update_idletasks()

    # -- Methods that return values --

    def test_compare_returns_bool(self):
        result = self.text.compare("1.0", "<", "2.0")
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_debug_getter_returns_bool(self):
        result = self.text.debug()
        self.assertIsInstance(result, bool)

    def test_debug_setter_returns_self(self):
        result = self.text.debug(True)
        self.assertIs(result, self.text)

    def test_dump_returns_list(self):
        result = self.text.dump("1.0", "end")
        self.assertIsInstance(result, list)

    def test_edit_modified_getter_returns_int(self):
        result = self.text.edit_modified()
        self.assertIsInstance(result, int)

    def test_edit_modified_setter_returns_str(self):
        result = self.text.edit_modified(False)
        self.assertEqual(result, '')

    def test_edit_reset_returns_str(self):
        result = self.text.edit_reset()
        self.assertEqual(result, '')

    def test_edit_separator_returns_str(self):
        result = self.text.edit_separator()
        self.assertEqual(result, '')

    def test_get_returns_str(self):
        result = self.text.get("1.0", "1.5")
        self.assertEqual(result, "Hello")

    def test_image_names_returns_tuple(self):
        # With no embedded images, image_names returns '' (empty string)
        # With images, it returns a tuple
        result = self.text.image_names()
        self.assertIsInstance(result, (str, tuple))

    def test_mark_gravity_getter_returns_str(self):
        result = self.text.mark_gravity("insert")
        self.assertIsInstance(result, str)

    def test_mark_names_returns_tuple(self):
        result = self.text.mark_names()
        self.assertIsInstance(result, tuple)

    def test_peer_names_returns_tuple(self):
        result = self.text.peer_names()
        self.assertIsInstance(result, tuple)

    def test_search_returns_str(self):
        result = self.text.search("World", "1.0")
        self.assertEqual(result, "1.6")

    def test_tag_cget_returns_str(self):
        self.text.tag_add("mytag", "1.0", "1.5")
        result = self.text.tag_cget("mytag", "foreground")
        self.assertIsInstance(result, str)

    def test_tag_names_returns_tuple(self):
        result = self.text.tag_names()
        self.assertIsInstance(result, tuple)

    def test_tag_nextrange_returns_tuple(self):
        result = self.text.tag_nextrange("sel", "1.0")
        self.assertIsInstance(result, tuple)

    def test_tag_prevrange_returns_tuple(self):
        result = self.text.tag_prevrange("sel", "end")
        self.assertIsInstance(result, tuple)

    def test_tag_ranges_returns_tuple(self):
        result = self.text.tag_ranges("sel")
        self.assertIsInstance(result, tuple)

    def test_window_names_returns_tuple(self):
        result = self.text.window_names()
        self.assertIsInstance(result, tuple)

    # -- Methods that return self (chainable) --

    def test_insert_returns_self(self):
        result = self.text.insert("end", "more text")
        self.assertIs(result, self.text)

    def test_mark_set_returns_self(self):
        result = self.text.mark_set("mymark", "1.0")
        self.assertIs(result, self.text)

    def test_mark_unset_returns_self(self):
        self.text.mark_set("mymark", "1.0")
        result = self.text.mark_unset("mymark")
        self.assertIs(result, self.text)

    def test_replace_returns_self(self):
        result = self.text.replace("1.0", "1.5", "Howdy")
        self.assertIs(result, self.text)

    def test_scan_mark_returns_self(self):
        result = self.text.scan_mark(0, 0)
        self.assertIs(result, self.text)

    def test_scan_dragto_returns_self(self):
        self.text.scan_mark(0, 0)
        result = self.text.scan_dragto(10, 10)
        self.assertIs(result, self.text)

    def test_see_returns_self(self):
        result = self.text.see("1.0")
        self.assertIs(result, self.text)

    def test_tag_add_returns_self(self):
        result = self.text.tag_add("mytag", "1.0", "1.5")
        self.assertIs(result, self.text)

    def test_tag_bind_returns_funcid(self):
        result = self.text.tag_bind("mytag", "<Button-1>", lambda e: None)
        self.assertIsInstance(result, str)

    def test_tag_config_setter_returns_self(self):
        self.text.tag_add("mytag", "1.0", "1.5")
        result = self.text.tag_config("mytag", foreground="red")
        self.assertIs(result, self.text)

    def test_tag_configure_setter_returns_self(self):
        self.text.tag_add("mytag", "1.0", "1.5")
        result = self.text.tag_configure("mytag", foreground="blue")
        self.assertIs(result, self.text)

    def test_tag_delete_returns_self(self):
        self.text.tag_add("deltag", "1.0", "1.5")
        result = self.text.tag_delete("deltag")
        self.assertIs(result, self.text)

    def test_tag_lower_returns_self(self):
        result = self.text.tag_lower("sel")
        self.assertIs(result, self.text)

    def test_tag_raise_returns_self(self):
        result = self.text.tag_raise("sel")
        self.assertIs(result, self.text)

    def test_tag_remove_returns_self(self):
        self.text.tag_add("rmtag", "1.0", "1.5")
        result = self.text.tag_remove("rmtag", "1.0", "end")
        self.assertIs(result, self.text)

    def test_tag_unbind_returns_self(self):
        self.text.tag_bind("sel", "<Button-1>", lambda e: None)
        result = self.text.tag_unbind("sel", "<Button-1>")
        self.assertIs(result, self.text)

    def test_yview_pickplace_returns_self(self):
        result = self.text.yview_pickplace("1.0")
        self.assertIs(result, self.text)

    # -- image_* methods --

    def test_image_create_returns_str(self):
        photo = tkinter.PhotoImage(master=self.root, width=10, height=10)
        result = self.text.image_create("1.0", image=photo)
        self.assertIsInstance(result, str)

    def test_image_cget_returns_str(self):
        photo = tkinter.PhotoImage(master=self.root, width=10, height=10)
        name = self.text.image_create("1.0", image=photo)
        result = self.text.image_cget(name, "image")
        self.assertIsInstance(result, str)

    def test_image_configure_setter_returns_self(self):
        photo = tkinter.PhotoImage(master=self.root, width=10, height=10)
        name = self.text.image_create("1.0", image=photo)
        result = self.text.image_configure(name, padx=5)
        self.assertIs(result, self.text)

    def test_image_configure_getter_returns_dict(self):
        photo = tkinter.PhotoImage(master=self.root, width=10, height=10)
        name = self.text.image_create("1.0", image=photo)
        result = self.text.image_configure(name)
        self.assertIsInstance(result, dict)

    # -- window_* methods --

    def test_window_create_returns_self(self):
        f = tkinter.Frame(self.text)
        result = self.text.window_create("1.0", window=f)
        self.assertIs(result, self.text)

    def test_window_cget_returns_str(self):
        f = tkinter.Frame(self.text)
        self.text.window_create("1.0", window=f)
        result = self.text.window_cget(f, "window")
        self.assertIsInstance(result, str)

    def test_window_configure_setter_returns_self(self):
        f = tkinter.Frame(self.text)
        self.text.window_create("1.0", window=f)
        result = self.text.window_configure(f, padx=5)
        self.assertIs(result, self.text)

    def test_window_config_setter_returns_self(self):
        f = tkinter.Frame(self.text)
        self.text.window_create("1.0", window=f)
        result = self.text.window_config(f, padx=5)
        self.assertIs(result, self.text)

    def test_window_configure_getter_returns_dict(self):
        f = tkinter.Frame(self.text)
        self.text.window_create("1.0", window=f)
        result = self.text.window_configure(f)
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
