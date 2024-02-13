import sublime
import sublime_plugin


class FileEventListener(sublime_plugin.EventListener):
    def on_window_command(self, window: sublime.Window, command_name: str, args):
        if command_name != "file_watcher_broadcast_event":
            return

        event = args['_event']
        file = args['file']

        if event == "create":
            self.on_create(file, window)

        if event == "change":
            self.on_change(file, window)

        if event == "delete":
            self.on_delete(file, window)

        pass

    def on_create(self, file, window):
        pass

    def on_change(self, file, window):
        pass

    def on_delete(self, file, window):
        pass
