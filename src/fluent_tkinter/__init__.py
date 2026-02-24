"""Monkey patch for Python's tkinter that enables fluent-style method chaining.

Usage:
    import fluent_tkinter  # patches tkinter on import

After importing, any tkinter method that normally returns None will return
``self`` instead, allowing chaining::

    import fluent_tkinter
    import tkinter as tk

    root = tk.Tk()
    (tk.Label(root, text="Hello")
        .pack(padx=10, pady=10)
        .configure(fg="blue"))
"""

from fluent_tkinter._patch import patch

patch()
