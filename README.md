# 👁 File Watcher

Sublime Text unfortunately does not automatically detect changes in the loaded folders.
This package adds support to it by leveraging `LSP` features and broadcasting an event where other packages can subscribe

## Requirements:

This package requires [`LSP-file-watcher-chokidar`](https://packagecontrol.io/packages/LSP-file-watcher-chokidar)

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
        file = args['file']

        if event == "create":
            self.on_create(file, window)
        if event == "change":
            self.on_change(file, window)
        if event == "delete":
            self.on_delete(file, window)

    def on_create(self, file, window):
        # do something when a file is created
        pass

    def on_change(self, file, window):
        # do something when a file is changed
        pass

    def on_delete(self, file, window):
        # do something when a file is deleted
        pass
```
