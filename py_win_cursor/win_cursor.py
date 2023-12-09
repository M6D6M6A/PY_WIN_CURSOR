import ctypes

from .win_cursor_type import WinCursorType


class WinCursor:
    """ Manages a single custom cursor type in a Windows environment. """

    def __init__(self, cursor_path, cursor_type=WinCursorType.IDC_ARROW):
        """ Initialize the CustomCursor instance.

        Args:
            cursor_path (str): The file path to the custom cursor (.cur or .ani file).
            cursor_type (int): The type of cursor to change.
        """
        self.cursor_path = cursor_path
        self.cursor_type = cursor_type
        self.original_cursor = ctypes.windll.user32.LoadCursorW(0, cursor_type)
        self.custom_cursor = None
        self._load_custom_cursor()

    def _load_custom_cursor(self):
        """ Load the custom cursor from the specified file path. """
        self.custom_cursor = ctypes.windll.user32.LoadCursorFromFileW(
            self.cursor_path)
        if not self.custom_cursor:
            print("Failed to load custom cursor.")

    def set_cursor(self):
        """ Set the custom cursor as the current system cursor. """
        if self.custom_cursor:
            ctypes.windll.user32.SetSystemCursor(
                self.custom_cursor, self.cursor_type)

    def reset_cursor(self, win_default=True):
        """ 
        Reset the system cursor.

        Args:
            win_default (bool): If True, resets the cursor to the Windows default settings. 
                                If False, resets the cursor to the original cursor stored 
                                during the initialization of this instance.

        This method allows the user to either revert to the original cursor that was 
        active before this instance made any changes, or to reset to the default cursor 
        as defined by the Windows system settings.
        """
        if win_default:
            ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0)
        else:
            ctypes.windll.user32.SetSystemCursor(
                self.original_cursor, self.cursor_type)
