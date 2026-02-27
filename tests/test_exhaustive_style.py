"""Exhaustive tests for wrapped methods on ttk.Style."""

import unittest
import tkinter
from tkinter import ttk
from test.support import requires

from tests.cpython_test_tkinter.support import AbstractTkTest

requires('gui')


class TtkStyleMethodsTest(AbstractTkTest, unittest.TestCase):
    """Test every wrapped method defined on ttk.Style."""

    def setUp(self):
        super().setUp()
        self.style = ttk.Style(self.root)

    # -- Setter methods that should return self (chainable) --

    def test_element_create_returns_self(self):
        result = self.style.element_create('fluent.bg', 'from', 'default')
        self.assertIs(result, self.style)

    def test_theme_create_returns_self(self):
        result = self.style.theme_create('fluenttest')
        self.assertIs(result, self.style)

    def test_theme_settings_returns_self(self):
        self.style.theme_create('fluenttest2')
        result = self.style.theme_settings('fluenttest2', {})
        self.assertIs(result, self.style)

    def test_theme_use_setter_returns_self(self):
        curr = self.style.theme_use()
        result = self.style.theme_use(curr)
        self.assertIs(result, self.style)

    # -- Query methods that should preserve return values --

    def test_configure_query_opt_returns_value(self):
        self.style.configure('TButton', background='yellow')
        result = self.style.configure('TButton', 'background')
        self.assertEqual(result, 'yellow')

    def test_configure_query_all_returns_dict(self):
        self.style.configure('TButton', background='yellow')
        result = self.style.configure('TButton')
        self.assertIsInstance(result, dict)

    def test_configure_query_unknown_returns_none(self):
        # Querying an unconfigured style returns None (not self)
        result = self.style.configure('C.FluentNonexistent')
        self.assertIsNone(result)

    def test_configure_setter_returns_none(self):
        # configure is excluded from patching on Style, so it still
        # returns None when used as a setter.
        result = self.style.configure('TButton', background='yellow')
        self.assertIsNone(result)

    def test_map_query_opt_returns_list(self):
        self.style.map('TButton', background=[('active', 'blue')])
        result = self.style.map('TButton', 'background')
        self.assertIsInstance(result, list)

    def test_map_query_all_returns_dict(self):
        result = self.style.map('TButton')
        self.assertIsInstance(result, dict)

    def test_lookup_returns_str(self):
        self.style.configure('TButton', background='yellow')
        result = self.style.lookup('TButton', 'background')
        self.assertIsInstance(result, str)

    def test_layout_query_returns_list(self):
        result = self.style.layout('TButton')
        self.assertIsInstance(result, list)

    def test_theme_use_query_returns_str(self):
        result = self.style.theme_use()
        self.assertIsInstance(result, str)

    def test_theme_names_returns_tuple(self):
        result = self.style.theme_names()
        self.assertIsInstance(result, tuple)

    def test_element_names_returns_tuple(self):
        result = self.style.element_names()
        self.assertIsInstance(result, tuple)

    def test_element_options_returns_tuple(self):
        result = self.style.element_options('Button.button')
        self.assertIsInstance(result, tuple)

    # -- Chaining --

    def test_chaining_theme_create_and_use(self):
        result = (self.style
                  .theme_create('chaintest')
                  .theme_use('chaintest'))
        self.assertIs(result, self.style)

    def test_chaining_element_create(self):
        result = (self.style
                  .element_create('chain.a', 'from', 'default')
                  .element_create('chain.b', 'from', 'default'))
        self.assertIs(result, self.style)


if __name__ == '__main__':
    unittest.main()
