from python_code import spreadsheetGrammarLanguage_Block
from python_code import spreadsheetGrammarLanguage_Column
from python_code import spreadsheetGrammarLanguage_ColumnDefinition

def test_spreadsheetGrammarLanguage_Column___init__():
    assert spreadsheetGrammarLanguage_Column.__init__(spreadsheetGrammarLanguage_Column('', False, spreadsheetGrammarLanguage_Column=spreadsheetGrammarLanguage_Block(), spreadsheetGrammarLanguage_Column6=spreadsheetGrammarLanguage_ColumnDefinition()), '', False, spreadsheetGrammarLanguage_Column=spreadsheetGrammarLanguage_Block(), spreadsheetGrammarLanguage_Column6=spreadsheetGrammarLanguage_ColumnDefinition()) == None


from python_code import spreadsheetGrammarLanguage_Block
from python_code import spreadsheetGrammarLanguage_Grammar

def test_spreadsheetGrammarLanguage_Grammar___init__():
    assert spreadsheetGrammarLanguage_Grammar.__init__(spreadsheetGrammarLanguage_Grammar('\x00', spreadsheetGrammarLanguage_Grammar=spreadsheetGrammarLanguage_Block(), spreadsheetGrammarLanguage_Grammar2=set()), '', spreadsheetGrammarLanguage_Grammar=spreadsheetGrammarLanguage_Block(), spreadsheetGrammarLanguage_Grammar2=set()) == None

