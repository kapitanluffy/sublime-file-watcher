# File Watcher

## Usage:

Create an event listener in your package

```py
import sublime
from FileWatcher.src.file_event_listener import FileEventListener

class CompassFileEventListener(FileEventListener):
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
