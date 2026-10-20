from python_code import graphbt_AlternativeClass

def test_graphbt_AlternativeClass___init__():
    assert graphbt_AlternativeClass.__init__(graphbt_AlternativeClass(''), '') == None


from python_code import graphbt_Author
from python_code import graphbt_AuthorList

def test_graphbt_Author___init__():
    assert graphbt_Author.__init__(graphbt_Author('', '', '\x00\x00', graphbt_Author=graphbt_AuthorList()), '', '', '', graphbt_Author=graphbt_AuthorList()) == None


from python_code import graphbt_Button

def test_graphbt_Button___init__():
    assert graphbt_Button.__init__(graphbt_Button(''), '') == None


from python_code import graphbt_EmptyNode

def test_graphbt_EmptyNode___init__():
    assert graphbt_EmptyNode.__init__(graphbt_EmptyNode(''), '') == None


from python_code import graphbt_Formula
from python_code import graphbt_FormulaList

def test_graphbt_Formula___init__():
    assert graphbt_Formula.__init__(graphbt_Formula('', graphbt_Formula=graphbt_FormulaList()), '', graphbt_Formula=graphbt_FormulaList()) == None


from python_code import graphbt_GUI

def test_graphbt_GUI___init__():
    assert graphbt_GUI.__init__(graphbt_GUI('', '\x00'), '\x00\x00', '') == None


from python_code import graphbt_Layout
from python_code import graphbt_LayoutList

def test_graphbt_Layout___init__():
    assert graphbt_Layout.__init__(graphbt_Layout('', 0, 0, 0, 0, 0, graphbt_Layout=graphbt_LayoutList()), '', 0, 0, 0, 0, 0, graphbt_Layout=graphbt_LayoutList()) == None


from python_code import graphbt_OperatorClass

def test_graphbt_OperatorClass___init__():
    assert graphbt_OperatorClass.__init__(graphbt_OperatorClass(''), '') == None


from python_code import graphbt_TraceabilityStatusClass

def test_graphbt_TraceabilityStatusClass___init__():
    assert graphbt_TraceabilityStatusClass.__init__(graphbt_TraceabilityStatusClass(''), '') == None

