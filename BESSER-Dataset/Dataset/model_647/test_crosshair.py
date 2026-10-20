from python_code import cellsheet_Ast
from python_code import cellsheet_AstEval

def test_cellsheet_AstEval___init__():
    assert cellsheet_AstEval.__init__(cellsheet_AstEval('', '', False, cellsheet_AstEval=cellsheet_Ast()), '\x00', '', False, cellsheet_AstEval=cellsheet_Ast()) == None


from python_code import cellsheet_BlankCell

def test_cellsheet_BlankCell___init__():
    assert cellsheet_BlankCell.__init__(cellsheet_BlankCell(''), '') == None


from python_code import cellsheet_BooleanCell

def test_cellsheet_BooleanCell___init__():
    assert cellsheet_BooleanCell.__init__(cellsheet_BooleanCell(''), '') == None


import datetime as _ch_datetime
from python_code import cellsheet_DateCell

def test_cellsheet_DateCell___init__():
    assert cellsheet_DateCell.__init__(cellsheet_DateCell(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import cellsheet_FormulaCell

def test_cellsheet_FormulaCell___init__():
    assert cellsheet_FormulaCell.__init__(cellsheet_FormulaCell(''), '') == None


from python_code import cellsheet_HasA1

def test_cellsheet_HasA1___init__():
    assert cellsheet_HasA1.__init__(cellsheet_HasA1(''), '') == None


from python_code import cellsheet_HasId

def test_cellsheet_HasId___init__():
    assert cellsheet_HasId.__init__(cellsheet_HasId(''), '') == None


from python_code import cellsheet_NumericCell

def test_cellsheet_NumericCell___init__():
    assert cellsheet_NumericCell.__init__(cellsheet_NumericCell(''), '') == None


from python_code import cellsheet_TextCell

def test_cellsheet_TextCell___init__():
    assert cellsheet_TextCell.__init__(cellsheet_TextCell(''), '') == None

