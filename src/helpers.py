from typing import Optional, cast, List
import sublime
import posixpath
from .__globals import FILE_WATCHER_WINDOWS, FILE_WATCHER_HANDLERS
from .file_watcher_handler import FileWatcherHandler, get_chokidar, get_watcher


def sublime_pattern_to_glob(pattern: str, is_directory_pattern: bool, root_path: Optional[str] = None) -> str:
    """
    Convert a Sublime Text pattern (http://www.sublimetext.com/docs/file_patterns.html)
    to a glob pattern that utilizes globstar extension.

    @see https://github.com/sublimelsp/LSP/blob/main/plugin/core/types.py#L75
    """
    glob = pattern
    if '/' not in glob:  # basic pattern: compared against exact file or directory name
        glob = '**/{}'.format(glob)
        if is_directory_pattern:
            glob += '/**'
    else:  # complex pattern
        # With '*/' prefix or '/*' suffix, the '*' matches '/' characters.
        if glob.startswith('*/'):
            glob = '*{}'.format(glob)
        if glob.endswith('/*'):
            glob += '*'
        # If a pattern ends in '/' it will be treated as a directory pattern, and will match both a directory with that
        # name and any contained files or subdirectories.
        if glob.endswith('/'):
            glob += '**'
        # If pattern begins with '//', it will be compared as a relative path from the project root.
        if glob.startswith('//') and root_path:
            glob = posixpath.join(root_path, glob[2:])
        # If a pattern begins with a single /, it will be treated as an absolute path.
        if not glob.startswith('/') and not glob.startswith('**/'):
            glob = '**/{}'.format(glob)
        if is_directory_pattern and not glob.endswith('/**'):
            glob += '/**'
    return glob


def get_global_ignore_globs(root_path: str) -> List[str]:
    global_settings = sublime.load_settings("Preferences.sublime-settings")

    folder_exclude_patterns = cast(List[str], global_settings.get('folder_exclude_patterns'))
    folder_excludes = [
        sublime_pattern_to_glob(pattern, is_directory_pattern=True, root_path=root_path)
        for pattern in folder_exclude_patterns
    ]
    file_exclude_patterns = cast(List[str], global_settings.get('file_exclude_patterns'))
    file_excludes = [
        sublime_pattern_to_glob(pattern, is_directory_pattern=False, root_path=root_path)
        for pattern in file_exclude_patterns
    ]
    return folder_excludes + file_excludes + ['**/node_modules/**']


def register_watcher(window: sublime.Window):
    _watcher = get_watcher()
    if _watcher is None:
        return

    _chokidar = get_chokidar()
    controller_id = _chokidar._last_controller_id

    wid = window.id()
    # print("Register {}".format(wid))
    folders = window.folders()
    file_watchers = {}

    for index, folder in enumerate(folders):
        controller_id = controller_id + 1
        FILE_WATCHER_HANDLERS[controller_id] = FileWatcherHandler(wid)
        # print('Register {} {} {}'.format(controller_id, wid, fid))
        ignores = get_global_ignore_globs(folder)
        watcher = _watcher.create(
            folder, [''], ignores, ['create', 'change', 'delete'], FILE_WATCHER_HANDLERS[controller_id])
        file_watchers[controller_id] = watcher

    if len(file_watchers.keys()) > 0:
        FILE_WATCHER_WINDOWS[wid] = file_watchers
    pass


def remove_watcher(window: sublime.Window):
    wid = window.id()
    # print("Unregister {}".format(wid))
    file_watchers = FILE_WATCHER_WINDOWS.pop(wid, None)

    FILE_WATCHER_HANDLERS.pop(wid, None)

    if file_watchers:
        for file_watcher in file_watchers:
            try:
                file_watcher.destroy()
            except Exception as e:
                print("ERROR: {}".format(e))
        pass


def register_all_watchers():
    windows = sublime.windows()
    for window in windows:
        register_watcher(window)


def clear_all_watchers():
    for wid, file_watchers in FILE_WATCHER_WINDOWS.items():
        if file_watchers:
            for cid, file_watcher in file_watchers.items():
                # print("Unregister {}".format(cid))
                try:
                    file_watcher.destroy()
                except Exception as e:
                    print("ERROR: {}".format(e))

    FILE_WATCHER_WINDOWS.clear()
    FILE_WATCHER_HANDLERS.clear()
    pass
