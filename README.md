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

        # _events is an array of tuples `(event, file)[]`
        # "event" can be create, change or delete
        events = args['_events']

        # do something...
```
