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

        event_create = []
        event_change = []
        event_delete = []

        for e in events:
            event, file = e

            if event == 'create':
                event_create.append(file)
                continue

            if event == 'change':
                event_change.append(file)
                continue

            if event == 'delete':
                event_delete.append(file)
                continue

            # if there are unknown events, just broadcast them
            window.run_command("file_watcher_broadcast_event", {"_event": event, "files": [file]})

        if len(event_create) > 0:
            window.run_command("file_watcher_broadcast_event", {"_event": 'create', "files": [event_create]})

        if len(event_change) > 0:
            window.run_command("file_watcher_broadcast_event", {"_event": 'change', "files": [event_change]})

        if len(event_delete) > 0:
            window.run_command("file_watcher_broadcast_event", {"_event": 'delete', "files": [event_delete]})
