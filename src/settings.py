from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QColor
import sys


class Settings:
    # FONT #
    UTF8 = True
    if sys.platform == 'linux':
        FONT_FAMILY = "DejaVu Sans Mono"
    else:
        FONT_FAMILY = "Consolas, 'Courier New', monospace"
    FONT_SIZE = 14

    # Tab
    INDENTATION_GUIDES = True
    INDENTATIONS_USE_TABS = False
    TAB_WIDTH = 4
    AUTO_INDENT = True
    SCROLL_WIDTH = 1

    # WarpMode
    WRAP_MODE = QsciScintilla.WrapCharacter

    # Cursor
    CARET_LINE_VISIBLE = True
    CARET_LINE_BG_COLOR = QColor("#e0e0e0")

    # MARGIN #
    MARGINS_BG_COLOR = QColor("#e0e0e0")
    
    # EDGE #
    EDGE_MODE = QsciScintilla.EdgeMode.EdgeLine
    EDGE_COLUMN = 80
    EDGE_COLOR = QColor("#ff6376")

