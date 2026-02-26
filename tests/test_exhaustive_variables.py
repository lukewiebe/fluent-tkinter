"""Exhaustive tests for wrapped methods on tkinter Variable classes."""

import unittest
import tkinter
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class VariableMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on tkinter.Variable."""

    def setUp(self):
        super().setUp()
        self.var = tkinter.Variable(self.root, value="initial")

    def test_get_returns_value(self):
        result = self.var.get()
        self.assertEqual(result, "initial")

    def test_initialize_returns_self(self):
        result = self.var.initialize("new_value")
        self.assertIs(result, self.var)

    def test_set_returns_self(self):
        result = self.var.set("test")
        self.assertIs(result, self.var)

    def test_trace_add_returns_str(self):
        result = self.var.trace_add("write", lambda *a: None)
        self.assertIsInstance(result, str)

    def test_trace_info_returns_list(self):
        self.var.trace_add("write", lambda *a: None)
        result = self.var.trace_info()
        self.assertIsInstance(result, list)

    def test_trace_remove_returns_self(self):
        tid = self.var.trace_add("write", lambda *a: None)
        result = self.var.trace_remove("write", tid)
        self.assertIs(result, self.var)

    # Deprecated trace methods

    def test_trace_returns_str(self):
        result = self.var.trace("w", lambda *a: None)
        self.assertIsInstance(result, str)

    def test_trace_variable_returns_str(self):
        result = self.var.trace_variable("w", lambda *a: None)
        self.assertIsInstance(result, str)

    def test_trace_vinfo_returns_list(self):
        self.var.trace("w", lambda *a: None)
        result = self.var.trace_vinfo()
        self.assertIsInstance(result, list)

    def test_trace_vdelete_returns_self(self):
        tid = self.var.trace("w", lambda *a: None)
        result = self.var.trace_vdelete("w", tid)
        self.assertIs(result, self.var)


class StringVarMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on tkinter.StringVar."""

    def test_get_returns_str(self):
        var = tkinter.StringVar(self.root, value="hello")
        result = var.get()
        self.assertEqual(result, "hello")


class IntVarMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on tkinter.IntVar."""

    def test_get_returns_int(self):
        var = tkinter.IntVar(self.root, value=42)
        result = var.get()
        self.assertEqual(result, 42)


class DoubleVarMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on tkinter.DoubleVar."""

    def test_get_returns_float(self):
        var = tkinter.DoubleVar(self.root, value=3.14)
        result = var.get()
        self.assertAlmostEqual(result, 3.14)


class BooleanVarMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test wrapped methods defined on tkinter.BooleanVar."""

    def test_get_returns_bool(self):
        var = tkinter.BooleanVar(self.root, value=True)
        result = var.get()
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_initialize_returns_self(self):
        var = tkinter.BooleanVar(self.root)
        result = var.initialize(True)
        self.assertIs(result, var)

    def test_set_returns_self(self):
        var = tkinter.BooleanVar(self.root)
        result = var.set(False)
        self.assertIs(result, var)


if __name__ == '__main__':
    unittest.main()
