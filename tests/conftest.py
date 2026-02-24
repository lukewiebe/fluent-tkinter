import os
import subprocess


def _setup_display():
    """Ensure DISPLAY is set, starting Xvfb if necessary."""
    if os.environ.get("DISPLAY"):
        return
    try:
        subprocess.Popen(
            ["Xvfb", ":99", "-screen", "0", "1024x768x24", "-ac"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        os.environ["DISPLAY"] = ":99"
        import time
        time.sleep(0.5)
    except FileNotFoundError:
        pass


def _setup_tcl_tk_env():
    """Set TCL_LIBRARY and TK_LIBRARY for standalone Python builds (e.g. uv)
    that bundle their own Tcl/Tk."""
    import sys
    real_exe = os.path.realpath(sys.executable)
    base = os.path.dirname(os.path.dirname(real_exe))
    for varname, subdir in [("TCL_LIBRARY", "tcl8.6"), ("TK_LIBRARY", "tk8.6")]:
        path = os.path.join(base, "lib", subdir)
        if os.path.isdir(path) and varname not in os.environ:
            os.environ[varname] = path


_setup_display()
_setup_tcl_tk_env()

# Activate the fluent tkinter monkey-patch so all tests run with it active
import fluent_tkinter  # noqa: E402, F401
