from typing import List
import importlib

import sublime
import sublime_plugin

Watcher = None
Chokidar = None

try:
    # https://github.com/sublimelsp/LSP-file-watcher-chokidar/blob/main/watcher.py
    Watcher = importlib.import_module("LSP-file-watcher-chokidar.watcher")
except Exception as e:
    print(str(e))


def get_chokidar():
    if Watcher:
        return Watcher.file_watcher
    return None


def get_watcher():
    if Watcher:
        return Watcher.FileWatcherController
    return None


class FileWatcherBroadcastEventCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        pass


class FileWatcherHandler():
    def __init__(self, wid: int):
        self.wid = wid
        pass

    def on_file_event_async(self, events) -> None:
        windows = sublime.windows()
        window = None

        for w in windows:
            if w.id() == self.wid:
                window = w
                break

        if window is None:
            return

        for event in events:
            window.run_command("file_watcher_broadcast_event", {"_event": event[0], "file": event[1]})
        pass
