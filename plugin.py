import imp
import sys

# ###----------------------------------------------------------------------------


def reload(prefix, modules=[""]):
    prefix = "FileWatcher.%s." % prefix

    for module in modules:
        module = (prefix + module).rstrip(".")
        if module in sys.modules:
            imp.reload(sys.modules[module])

# ###----------------------------------------------------------------------------


reload("src")

from .src import *


# ###----------------------------------------------------------------------------

def plugin_loaded():
    register_all_watchers()


def plugin_unloaded():
    clear_all_watchers()
