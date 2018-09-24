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
from .settings import Settings as S


class TextArea(QsciScintilla):

    extension_to_lang = {
        'sh': "Bash",
        'bash': "Bash",
        'zsh': "Bash",
        'bat': "Bash",
        'cmd': "Bash",
        'c': "CPP",
        'cc': "CPP",
        'cpp': "CPP",
        'cxx': "CPP",
        'h': "CPP",
        'hh': "CPP",
        'hpp': "CPP",
        'hxx': "CPP",
        'cs': "CSharp",
        'java': "Java",
        'js': "JavaScript",
        'json': "JavaScript",
        'css': "CSS",
        'd': "D",
        'f': "Fortran",
        'html': "HTML",
        'htm': "HTML",
        'xml': "XML",
        'lua': "Lua",
        'Makefile': "Makefile",
        'pas': "Pascal",
        'pl': "Perl",
        'pm': "Perl",
        'po': "PO",
        'pot': "PO",
        'ps': "PostScript",
        'pov': "POV",
        'inc': "POV",
        'properties': "Properties",
        'ini': "Properties",
        'py': "Python",
        'rb': "Ruby",
        'sql': "SQL",
        'tcl': "TCL",
        'tex': "TeX",
        'yaml': "YAML",
        'yml': "YAML"
    }
    lang_lexer = {
        'Bash': QsciLexerBash,
        'CPP': QsciLexerCPP,
        'CSharp': QsciLexerCSharp,
        'Java': QsciLexerJava,
        'JavaScript': QsciLexerJavaScript,
        'CSS': QsciLexerCSS,
        'D': QsciLexerD,
        'Fortran': QsciLexerFortran,
        'HTML': QsciLexerHTML,
        'XML': QsciLexerXML,
        'Lua': QsciLexerLua,
        'Makefile': QsciLexerMakefile,
        'Pascal': QsciLexerPascal,
        'Perl': QsciLexerPerl,
        'PO': QsciLexerPO,
        'Postscript': QsciLexerPostScript,
        'POV': QsciLexerPOV,
        'Properties': QsciLexerProperties,
        'Python': QsciLexerPython,
        'Ruby': QsciLexerRuby,
        'SQL': QsciLexerSQL,
        'TCL': QsciLexerTCL,
        'TeX': QsciLexerTeX,
        'YAML': QsciLexerYAML
    }

    def __init__(self,
                 name: str = "Untilted",
                 data: str = "",
                 path: str = None):
        super().__init__()

        tmp = name.split(".")
        self.file_path = path
        self.full_name = name
        if len(tmp) > 1:
            self.extension = tmp[-1]
        else:
            self.extension = None
        self.current_lang = None
        self.__font = QFont("Consolas, 'Courier New', monospace", 18)
        self.setup_editor()

    def setup_editor(self):
        # FONT #
        self.setUtf8(S.UTF8)
        lang = self.extension_to_lang.get(self.extension)
        self.set_lexer(lang)

        # Tab
        self.setIndentationGuides(S.INDENTATION_GUIDES)
        self.setIndentationsUseTabs(S.INDENTATIONS_USE_TABS)
        self.setTabWidth(S.TAB_WIDTH)
        self.setAutoIndent(S.AUTO_INDENT)
        self.setScrollWidth(S.SCROLL_WIDTH)

        # WarpMode
        self.setWrapMode(S.WRAP_MODE)

        # Cursor
        self.setCaretLineVisible(S.CARET_LINE_VISIBLE)
        self.setCaretLineBackgroundColor(S.CARET_LINE_BG_COLOR)

        # MARGIN #
        self.setMarginType(0, self.NumberMargin)
        self.set_margin_num_width()
        self.setMarginsBackgroundColor(S.MARGINS_BG_COLOR)

    def set_lexer(self, lexer: str):
        if lexer not in self.lang_lexer:
            new_lexer = None
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
