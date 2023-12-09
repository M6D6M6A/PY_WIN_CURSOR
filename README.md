# PyWinCursor

PyWinCursor is a Python package for managing and customizing mouse cursors in a Windows environment.
This package provides an easy-to-use interface for changing the system cursor, allowing customization of the cursor appearance with
cursor appearance with custom .cur or .ani files.

## Features

-   **Custom Cursor Management**: Set custom cursors for different cursor types (e.g., arrow, I-beam) in Windows.
-   **Context Management**: Safely manage cursor changes within a context, ensuring cursors are reset to default upon exit.
-   **Multiple Cursor Support**: Simultaneously manage multiple cursor types, changing them as needed in a grouped fashion.
-   **Robust Error Handling**: Graceful handling of errors such as missing cursor files or unsupported cursor types.

## Components

1. **CustomCursor**: A class to manage a single custom cursor type.
2. **CursorManager**: A class to manage multiple `CustomCursor` instances, allowing grouped cursor changes and resets.

## Installation

To use PyWinCursor in your project, clone the repository or download the source code and import the necessary classes.

## Usage

Here's a simple example of how to use PyWinCursor to change the default arrow and I-beam cursors to custom ones:

```python
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
```

## License

PyWinCursor is released under the [MIT License](https://opensource.org/licenses/MIT).
