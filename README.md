# 👁 File Watcher

Sublime Text unfortunately does not automatically detect changes in the loaded folders.
This package adds support to it by leveraging `LSP` features and broadcasting an event where other packages can subscribe

## Requirements:

This package requires [LSP](https://packagecontrol.io/packages/LSP) and [`LSP-file-watcher-chokidar`](https://packagecontrol.io/packages/LSP-file-watcher-chokidar)

## Usage:

Create an event listener inside your package subscribing to `file_watcher_broadcast_event`

```py
import sublime
import sublime_plugin

class MyFileEventListener(sublime_plugin.EventListener):
    def on_window_command(self, window: sublime.Window, command_name: str, args):
        if command_name != "file_watcher_broadcast_event":
            return

        event = args['_event']
        files = args['files']

        if event == "create":
            self.on_create(files, window)
        if event == "change":
            self.on_change(files, window)
        if event == "delete":
            self.on_delete(files, window)

    def on_create(self, files, window):
        # do something when files are created
        pass

    def on_change(self, files, window):
        # do something when files are changed
        pass

    def on_delete(self, files, window):
        # do something when files are deleted
        pass
```
