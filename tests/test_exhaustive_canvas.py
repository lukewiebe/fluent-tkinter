"""Exhaustive tests for every wrapped method on tkinter.Canvas."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class CanvasMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Canvas."""

    def setUp(self):
        super().setUp()
        self.canvas = tkinter.Canvas(self.root, width=200, height=200)
        self.canvas.pack()
        self.root.update_idletasks()
        self.rect = self.canvas.create_rectangle(10, 10, 50, 50)
        self.text_item = self.canvas.create_text(100, 100, text="hello")

    # -- addtag family: all return self --

    def test_addtag_returns_self(self):
        result = self.canvas.addtag("tag1", "all")
        self.assertIs(result, self.canvas)

    def test_addtag_above_returns_self(self):
        result = self.canvas.addtag_above("tag2", self.rect)
        self.assertIs(result, self.canvas)

    def test_addtag_all_returns_self(self):
        result = self.canvas.addtag_all("tag3")
        self.assertIs(result, self.canvas)

    def test_addtag_below_returns_self(self):
        result = self.canvas.addtag_below("tag4", self.rect)
        self.assertIs(result, self.canvas)

    def test_addtag_closest_returns_self(self):
        result = self.canvas.addtag_closest("tag5", 25, 25)
        self.assertIs(result, self.canvas)

    def test_addtag_enclosed_returns_self(self):
        result = self.canvas.addtag_enclosed("tag6", 0, 0, 100, 100)
        self.assertIs(result, self.canvas)

    def test_addtag_overlapping_returns_self(self):
        result = self.canvas.addtag_overlapping("tag7", 0, 0, 100, 100)
        self.assertIs(result, self.canvas)

    def test_addtag_withtag_returns_self(self):
        result = self.canvas.addtag_withtag("tag8", self.rect)
        self.assertIs(result, self.canvas)

    # -- canvasx / canvasy: return float --

    def test_canvasx_returns_float(self):
        result = self.canvas.canvasx(10)
        self.assertIsInstance(result, float)

    def test_canvasy_returns_float(self):
        result = self.canvas.canvasy(10)
        self.assertIsInstance(result, float)

    # -- coords: getter returns list --

    def test_coords_getter_returns_list(self):
        result = self.canvas.coords(self.rect)
        self.assertIsInstance(result, list)

    # -- create_* methods: all return int (item id) --

    def test_create_arc_returns_int(self):
        result = self.canvas.create_arc(10, 10, 50, 50)
        self.assertIsInstance(result, int)

    def test_create_bitmap_returns_int(self):
        result = self.canvas.create_bitmap(50, 50, bitmap="error")
        self.assertIsInstance(result, int)

    def test_create_image_returns_int(self):
        result = self.canvas.create_image(50, 50)
        self.assertIsInstance(result, int)

    def test_create_line_returns_int(self):
        result = self.canvas.create_line(0, 0, 100, 100)
        self.assertIsInstance(result, int)

    def test_create_oval_returns_int(self):
        result = self.canvas.create_oval(10, 10, 50, 50)
        self.assertIsInstance(result, int)

    def test_create_polygon_returns_int(self):
        result = self.canvas.create_polygon(0, 0, 50, 50, 100, 0)
        self.assertIsInstance(result, int)

    def test_create_rectangle_returns_int(self):
        result = self.canvas.create_rectangle(10, 10, 50, 50)
        self.assertIsInstance(result, int)

    def test_create_text_returns_int(self):
        result = self.canvas.create_text(50, 50, text="test")
        self.assertIsInstance(result, int)

    def test_create_window_returns_int(self):
        f = tkinter.Frame(self.canvas)
        result = self.canvas.create_window(50, 50, window=f)
        self.assertIsInstance(result, int)

    # -- dchars / dtag: return self --

    def test_dchars_returns_self(self):
        result = self.canvas.dchars(self.rect, 0)
        self.assertIs(result, self.canvas)

    def test_dtag_returns_self(self):
        self.canvas.addtag_withtag("removeme", self.rect)
        result = self.canvas.dtag(self.rect, "removeme")
        self.assertIs(result, self.canvas)

    # -- find family: return tuples --

    def test_find_above_returns_tuple(self):
        result = self.canvas.find_above(self.rect)
        self.assertIsInstance(result, tuple)

    def test_find_all_returns_tuple(self):
        result = self.canvas.find_all()
        self.assertIsInstance(result, tuple)

    def test_find_below_returns_tuple(self):
        result = self.canvas.find_below(self.rect)
        self.assertIsInstance(result, tuple)

    def test_find_closest_returns_tuple(self):
        result = self.canvas.find_closest(25, 25)
        self.assertIsInstance(result, tuple)

    def test_find_enclosed_returns_tuple(self):
        result = self.canvas.find_enclosed(0, 0, 1000, 1000)
        self.assertIsInstance(result, tuple)

    def test_find_overlapping_returns_tuple(self):
        result = self.canvas.find_overlapping(0, 0, 1000, 1000)
        self.assertIsInstance(result, tuple)

    def test_find_withtag_returns_tuple(self):
        result = self.canvas.find_withtag(self.rect)
        self.assertIsInstance(result, tuple)

    # -- focus: setter returns '' (pass-through) --

    def test_focus_returns_str(self):
        result = self.canvas.focus(self.text_item)
        self.assertIsInstance(result, str)

    # -- gettags: returns tuple --

    def test_gettags_returns_tuple(self):
        result = self.canvas.gettags(self.rect)
        self.assertIsInstance(result, tuple)

    # -- icursor / insert: return self --

    def test_icursor_returns_self(self):
        result = self.canvas.icursor(self.text_item, 0)
        self.assertIs(result, self.canvas)

    def test_insert_returns_self(self):
        result = self.canvas.insert(self.text_item, 0, "x")
        self.assertIs(result, self.canvas)

    # -- itemcget: returns str --

    def test_itemcget_returns_str(self):
        result = self.canvas.itemcget(self.rect, "fill")
        self.assertIsInstance(result, str)

    # -- itemconfig / itemconfigure (setter): return self --

    def test_itemconfig_setter_returns_self(self):
        result = self.canvas.itemconfig(self.rect, fill="red")
        self.assertIs(result, self.canvas)

    def test_itemconfigure_setter_returns_self(self):
        result = self.canvas.itemconfigure(self.rect, fill="blue")
        self.assertIs(result, self.canvas)

    # -- lift / lower / tkraise (canvas item ordering): return self --

    def test_lift_returns_self(self):
        result = self.canvas.lift(self.rect)
        self.assertIs(result, self.canvas)

    def test_lower_returns_self(self):
        result = self.canvas.lower(self.rect)
        self.assertIs(result, self.canvas)

    def test_tkraise_returns_self(self):
        result = self.canvas.tkraise(self.rect)
        self.assertIs(result, self.canvas)

    # -- move / moveto: return self --

    def test_move_returns_self(self):
        result = self.canvas.move(self.rect, 5, 5)
        self.assertIs(result, self.canvas)

    def test_moveto_returns_self(self):
        result = self.canvas.moveto(self.rect, 20, 20)
        self.assertIs(result, self.canvas)

    # -- postscript: returns str --

    def test_postscript_returns_str(self):
        result = self.canvas.postscript()
        self.assertIsInstance(result, str)

    # -- scale: returns self --

    def test_scale_returns_self(self):
        result = self.canvas.scale(self.rect, 0, 0, 1.5, 1.5)
        self.assertIs(result, self.canvas)

    # -- scan_mark / scan_dragto: return self --

    def test_scan_mark_returns_self(self):
        result = self.canvas.scan_mark(0, 0)
        self.assertIs(result, self.canvas)

    def test_scan_dragto_returns_self(self):
        self.canvas.scan_mark(0, 0)
        result = self.canvas.scan_dragto(10, 10)
        self.assertIs(result, self.canvas)

    # -- select_adjust / select_clear / select_from / select_to --
    # select_clear returns self; select_from/to/adjust return self on text items

    def test_select_clear_returns_self(self):
        result = self.canvas.select_clear()
        self.assertIs(result, self.canvas)

    def test_select_from_returns_self(self):
        result = self.canvas.select_from(self.text_item, 0)
        self.assertIs(result, self.canvas)

    def test_select_to_returns_self(self):
        self.canvas.select_from(self.text_item, 0)
        result = self.canvas.select_to(self.text_item, 3)
        self.assertIs(result, self.canvas)

    def test_select_adjust_returns_self(self):
        self.canvas.select_from(self.text_item, 0)
        result = self.canvas.select_adjust(self.text_item, 2)
        self.assertIs(result, self.canvas)

    # -- tag_bind: returns funcid str --

    def test_tag_bind_returns_str(self):
        result = self.canvas.tag_bind(self.rect, "<Button-1>", lambda e: None)
        self.assertIsInstance(result, str)

    # -- tag_lower / tag_raise: return self --

    def test_tag_lower_returns_self(self):
        result = self.canvas.tag_lower(self.rect)
        self.assertIs(result, self.canvas)

    def test_tag_raise_returns_self(self):
        result = self.canvas.tag_raise(self.rect)
        self.assertIs(result, self.canvas)

    # -- tag_unbind: returns self --

    def test_tag_unbind_returns_self(self):
        self.canvas.tag_bind(self.rect, "<Button-1>", lambda e: None)
        result = self.canvas.tag_unbind(self.rect, "<Button-1>")
        self.assertIs(result, self.canvas)


if __name__ == '__main__':
    unittest.main()
