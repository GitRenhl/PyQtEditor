from PyQt5.Qsci import QsciScintilla, \
    QsciLexerMakefile,\
    QsciLexerBash, \
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
        self.__name = name
        self.__path = path
        self.setText(data)
        if data:
            self.setModified(False)
        self.extension = self.__get_extension(name)
        self.current_lang = None
        self.__font = QFont(S.FONT_FAMILY, S.FONT_SIZE)
        self.__setup_editor()

    def get_name(self) -> str:
        return self.__name

    def get_path(self) -> str:
        return self.__path

    @staticmethod
    def __get_extension(name: str) -> str:
        tmp = name.split(".")
        if len(tmp) > 1:
            return tmp[-1]
        return None

    @classmethod
    def get_language(cls, extension: str):
        if extension not in cls.extension_to_lang:
            return None

        return cls.extension_to_lang[extension]

    def get_lexer(self, language: str):
        if language not in self.lang_lexer:
            return None

        return self.lang_lexer[language](self)

    def __setup_editor(self):
        # FONT #
        self.setUtf8(S.UTF8)
        lang = self.get_language(self.extension)
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
        if lang is not None:
            self.setEdgeMode(S.EDGE_MODE)
            self.setEdgeColor(S.EDGE_COLOR)
            self.setEdgeColumn(S.EDGE_COLUMN)

    def set_lexer(self, lang: str):
        new_lexer = self.get_lexer(lang)
        self.setLexer(new_lexer)

        self.current_lang = lang if lang in self.lang_lexer else None
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

    def change_name(self, name: str):
        self.__name = name
        self.extension = self.__get_extension(name)
        lang = self.get_language(self.extension)
        self.set_lexer(lang)

    def change_path(self, path: str):
        self.__path = path

    def count(self, string: str, *, case: bool = False) -> int:
        if case:
            counter = self.text().count(string)
        else:
            counter = self.text().lower().count(string.lower())
        return counter
