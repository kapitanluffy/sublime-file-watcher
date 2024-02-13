from .src import *


def plugin_loaded():
    register_all_watchers()


def plugin_unloaded():
    clear_all_watchers()
