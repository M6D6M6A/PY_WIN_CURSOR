import time

from py_win_cursor import WinCursor, WinCursorType, WinCursorManager


arrow_cursor_path = "C:/Path/to/cursor.cur"
text_cursor_path = "C:/Path/to/cursor.cur"

cursors = [
    WinCursor(arrow_cursor_path, WinCursorType.IDC_ARROW),
    WinCursor(text_cursor_path, WinCursorType.IDC_IBEAM)
]

with WinCursorManager(cursors) as manager:
    # Both cursors will be custom within this block
    time.sleep(10)
    # Cursors will be reset to their original states after this block or if an exception occurs
