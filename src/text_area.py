from PyQt5.Qsci import QsciScintilla, \
    QsciLexerMakefile,\
    QsciLexerBash, \
    QsciLexerBatch, \
    QsciLexerCPP, \
    QsciLexerCSS, \
    QsciLexerCSharp, \
    QsciLexerD, \
    QsciLexerFortran, \
    QsciLexerHTML, \
    QsciLexerJava, \
    QsciLexerJavaScript, \
    QsciLexerLua, \
    QsciLexerPO, \
    QsciLexerPOV, \
    QsciLexerPascal, \
    QsciLexerPerl, \
    QsciLexerPostScript, \
    QsciLexerProperties, \
    QsciLexerPython, \
    QsciLexerRuby, \
    QsciLexerSQL, \
    QsciLexerTCL, \
    QsciLexerTeX, \
    QsciLexerXML, \
    QsciLexerYAML
from PyQt5.QtGui import QFont
# from PyQt5.QtWidgets import QTextEdit


class TextArea(QsciScintilla):

    def __init__(self,
                 name: str = "Untilted",
                 data: str = "",
                 path: str = None):
        super().__init__()

        self.lang_lexer = {
            'sh': QsciLexerBash,
            'bash': QsciLexerBash,
            'zsh': QsciLexerBash,
            'bat': QsciLexerBatch,
            'cmd': QsciLexerBatch,
            'c': QsciLexerCPP,
            'cc': QsciLexerCPP,
            'cpp': QsciLexerCPP,
            'cxx': QsciLexerCPP,
            'h': QsciLexerCPP,
            'hh': QsciLexerCPP,
            'hpp': QsciLexerCPP,
            'hxx': QsciLexerCPP,
            'cs': QsciLexerCSharp,
            'java': QsciLexerJava,
            'js': QsciLexerJavaScript,
            'json': QsciLexerJavaScript,
            'css': QsciLexerCSS,
            'd': QsciLexerD,
            'f': QsciLexerFortran,
            'html': QsciLexerHTML,
            'htm': QsciLexerHTML,
            'xml': QsciLexerXML,
            'lua': QsciLexerLua,
            'Makefile': QsciLexerMakefile,
            'pas': QsciLexerPascal,
            'pl': QsciLexerPerl,
            'pm': QsciLexerPerl,
            'po': QsciLexerPO,
            'pot': QsciLexerPO,
            'ps': QsciLexerPostScript,
            'pov': QsciLexerPOV,
            'inc': QsciLexerPOV,
            'properties': QsciLexerProperties,
            'ini': QsciLexerProperties,
            'py': QsciLexerPython,
            'rb': QsciLexerRuby,
            'sql': QsciLexerSQL,
            'tcl': QsciLexerTCL,
            'tex': QsciLexerTeX,
            'yaml': QsciLexerYAML,
            'yml': QsciLexerYAML
        }
        self.filePath = path
        self.name = name
        self.current_lang = None
        self.__font = QFont("Consolas, 'Courier New', monospace", 18)
        self.setup_editor()

    def setup_editor(self):
        # FONT #
        self.setUtf8(True)
        self.set_lexer("py")
        self.__update_font()

        # Tab
        self.setTabWidth(4)
        self.setIndentationsUseTabs(False)
        self.setAutoIndent(True)

        self.setScrollWidth(1)

        # WarpMode
        self.setWrapMode(QsciScintilla.WrapWhitespace)

        # MARGIN #
        self.setMarginType(0, self.NumberMargin)
        self.set_margin_num_width()

    def set_lexer(self, lexer: str):
        if lexer not in self.lang_lexer:
            new_lexer = None
            print("Lexer not found")
        else:
            new_lexer = self.lang_lexer[lexer](self)

        self.setLexer(new_lexer)

        self.current_lang = lexer if lexer in self.lang_lexer else None
        self.__update_font()

    def __update_font(self):
        if self.current_lang is None:
            self.setFont(self.__font)
        else:
            self.lexer().setFont(self.__font)

    def set_margin_num_width(self):
        size = len(str(self.lines()))
        if size < 2:
            size = 2
        self.setMarginWidth(0, "0" * size)

    def get_name(self):
        return self.name
