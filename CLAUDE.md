# CLAUDE.md

## Project Overview

fluent-tkinter is a Python library that monkey-patches `tkinter` to enable fluent-style method chaining. Methods that normally return `None` instead return `self`, allowing chains like:

```python
import fluent_tkinter
import tkinter as tk

root = tk.Tk()
tk.Label(root, text="Hello").pack(padx=10, pady=10).configure(fg="blue")
```

## Build & Setup

**Prerequisites:** `python3-tk` system package must be installed:
```bash
apt-get install -y python3-tk
```

**Install dependencies:**
```bash
uv sync
```

## Running Tests

```bash
uv run pytest
```

Tests require a display. The test `conftest.py` automatically starts Xvfb if no display is available.

**Test suite:** 1855 tests across three categories:
- `tests/test_fluent.py` — Core fluent behavior and end-to-end chaining tests
- `tests/test_exhaustive_*.py` — Per-widget exhaustive chainability tests (14 files)
- `tests/cpython_test_tkinter/`, `tests/cpython_test_ttk/` — CPython stdlib tkinter tests to verify patching doesn't break existing behavior

## Project Structure

```
src/fluent_tkinter/
  __init__.py       # Auto-calls patch() on import
  _patch.py         # Core monkey-patching logic (patches 56+ tkinter/ttk classes)
tests/
  conftest.py       # Xvfb setup, TCL/TK library paths, auto-imports fluent_tkinter
  test_fluent.py    # Main fluent behavior tests
  test_exhaustive_*.py  # Per-widget chainable method tests
  cpython_test_tkinter/ # CPython stdlib tkinter test suite subset
  cpython_test_ttk/     # CPython stdlib ttk test suite subset
```

## Key Architecture

- `_patch.py` defines `_EXCLUDED_METHODS` — 31 methods where `None` return is semantically meaningful (query methods, geometry info, etc.)
- `_make_fluent(method)` wraps methods to return `self` when the original returns `None`; preserves non-None returns including empty strings
- `_patch_class(cls)` applies fluent wrapping to all public, non-excluded methods on a class
- `patch()` is idempotent and patches 32 tkinter + 24 ttk classes

## Tech Stack

- **Python** >=3.12.3
- **Build system:** hatchling
- **Package manager:** uv
- **Test framework:** pytest + pytest-forked
- **Zero runtime dependencies** — only patches stdlib tkinter
