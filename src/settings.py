from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QColor


class Settings:

    UTF8 = True
    FONT_FAMILY = "Consolas, 'Courier New', monospace"
    FONT_SIZE = 18

    # Tab
    INDENTATION_GUIDES = True
    INDENTATIONS_USE_TABS = False
    TAB_WIDTH = 4
    AUTO_INDENT = True
    SCROLL_WIDTH = 1

    # WarpMode
    WRAP_MODE = QsciScintilla.WrapWhitespace

    # Cursor
    CARET_LINE_VISIBLE = True
    CARET_LINE_BG_COLOR = QColor("#e0e0e0")

    # MARGIN #
    MARGINS_BG_COLOR = QColor("#e0e0e0")
