# File Watcher

## Usage:

Extend `FileEventListener` and override the following methods

- `on_create(self, file: string, window: sublime.Window)`
- `on_change(self, file: string, window: sublime.Window)`
- `on_delete(self, file: string, window: sublime.Window)`
