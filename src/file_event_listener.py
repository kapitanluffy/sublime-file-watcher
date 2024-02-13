import sublime
import sublime_plugin
from .__globals import GLOBAL_FILE_WATCHERS, GLOBAL_FILE_WATCHER_HANDLERS


class FileEventListener(sublime_plugin.EventListener):
    def on_window_command(self, window: sublime.Window, command_name: str, args):
        if command_name != "file_watcher_broadcast_event":
            return

        print('>>', GLOBAL_FILE_WATCHER_HANDLERS)

        event = args['_event']
        file = args['file']

        if event == "create":
            self.on_create(file)

        if event == "change":
            self.on_change(file)

        if event == "delete":
            self.on_delete(file)

        pass

    def on_create(self, file):
        pass

    def on_change(self, file):
        pass

    def on_delete(self, file):
        pass
