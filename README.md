# File Watcher

Adds support to broadcasting file events to Sublime Text 

## Requires:

This package requires [`LSP-file-watcher-chokidar`](https://packagecontrol.io/packages/LSP-file-watcher-chokidar). 
It should be available already if you are using LSP packages

## Usage:

Create an event listener in your package

```py
import sublime
from FileWatcher.src.file_event_listener import FileEventListener

class MyFileEventListener(FileEventListener):
    def on_window_command(self, window: sublime.Window, command_name: str, args):
        super().on_window_command(window, command_name, args)

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
