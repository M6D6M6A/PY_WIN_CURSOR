from typing import List

from .win_cursor import WinCursor


class WinCursorManager:
    """ Manages multiple custom cursors. """

    def __init__(self, cursors: List[WinCursor], win_default=True):
        """ Initialize the CursorManager with multiple CustomCursor instances.

        Args:
            cursors (list of CustomCursor): A list of CustomCursor instances to manage.
            win_default (bool): If True, resets the cursor to the Windows default settings. 
                                If False, resets the cursor to the original cursor stored 
                                during the initialization of the instance.
        """
        self.win_default = win_default
        self.cursors = cursors

    def __enter__(self):
        for cursor in self.cursors:
            cursor.set_cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for cursor in self.cursors:
            cursor.reset_cursor(win_default=self.win_default)
