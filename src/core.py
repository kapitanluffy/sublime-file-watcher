from .helpers import register_watcher, remove_watcher
from .file_watcher_handler import get_chokidar
import sublime
import sublime_plugin


class FileWatcherEventListener(sublime_plugin.EventListener):
    def on_init(self, views):
        windows = sublime.windows()
        for window in windows:
            register_watcher(window)
        pass

    def on_load_project_async(self, window: sublime.Window):
        register_watcher(window)
        pass

    def on_new_window_async(self, window: sublime.Window):
        register_watcher(window)
        pass

    def on_pre_close_project(self, window: sublime.Window):
        remove_watcher(window)
        pass

    def on_pre_close_window(self, window: sublime.Window):
        remove_watcher(window)
        pass

    def on_pre_save_project(self, window: sublime.Window):
        # @todo handle new folder added
        pass

    def on_activated_async(self, view: sublime.View):
        # cids = []
        # for c in GLOBAL_FILE_WATCHERS:
        #     cids.append(GLOBAL_FILE_WATCHERS[c][0]._controller_id)
        # print("controllers>", cids)

        # chokidar = get_chokidar()
        # if chokidar is None:
        #     return

        # removables = []

        # for hid in chokidar._handlers:
        #     handler, root_path = chokidar._handlers[hid]
        #     handle = handler()
        #     if handle is None:
        #         removables.append(hid)
        #         print("remove choki handlers>", hid)

        # for rid in removables:
        #     chokidar._on_watcher_removed(hid)
        pass
