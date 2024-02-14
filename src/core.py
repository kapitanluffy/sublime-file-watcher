from .helpers import register_watcher, remove_watcher
import sublime
import sublime_plugin


class FileWatcherEventListener(sublime_plugin.EventListener):
    def on_init(self, views):
        windows = sublime.windows()
        for window in windows:
            register_watcher(window)

    def on_load_project_async(self, window: sublime.Window):
        register_watcher(window)

    def on_new_window_async(self, window: sublime.Window):
        register_watcher(window)

    def on_pre_close_project(self, window: sublime.Window):
        remove_watcher(window)

    def on_pre_close_window(self, window: sublime.Window):
        remove_watcher(window)

    def on_pre_save_project(self, window: sublime.Window):
        # @todo handle new folder added
        pass
