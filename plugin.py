import sys

# clear modules cache if package is reloaded (after update?)
prefix = __package__ + ".src"  # don't clear the base package
for module_name in [
    module_name
    for module_name in sys.modules
    if module_name.startswith(prefix)
]:
    del sys.modules[module_name]
del prefix

from .src import *  # noqa


def plugin_loaded():
    register_all_watchers()


def plugin_unloaded():
    clear_all_watchers()
