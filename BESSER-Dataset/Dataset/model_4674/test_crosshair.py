from python_code import Maude_Constant

def test_Maude_Constant___init__():
    assert Maude_Constant.__init__(Maude_Constant(''), '') == None


from python_code import Maude_LabelMapping

def test_Maude_LabelMapping___init__():
    assert Maude_LabelMapping.__init__(Maude_LabelMapping('', '\x00'), '\x00\x00', '') == None


from python_code import Maude_MaudeSpec
from python_code import Maude_MaudeTopEl

def test_Maude_MaudeTopEl___init__():
    assert Maude_MaudeTopEl.__init__(Maude_MaudeTopEl('', Maude_MaudeTopEl=Maude_MaudeSpec(), Maude_MaudeTopEl3=Maude_MaudeSpec()), '', Maude_MaudeTopEl=Maude_MaudeSpec(), Maude_MaudeTopEl3=Maude_MaudeSpec()) == None


from python_code import Maude_ModExpression
from python_code import Maude_Module
from python_code import Maude_Parameter

def test_Maude_Parameter___init__():
    assert Maude_Parameter.__init__(Maude_Parameter('', Maude_Parameter=Maude_ModExpression(), Maude_Parameter22=Maude_Module()), '', Maude_Parameter=Maude_ModExpression(), Maude_Parameter22=Maude_Module()) == None


from python_code import Maude_RecTerm

def test_Maude_RecTerm___init__():
    assert Maude_RecTerm.__init__(Maude_RecTerm('', Maude_RecTerm=set()), '', Maude_RecTerm=set()) == None


from python_code import Maude_Sort
from python_code import Maude_SortMapping

def test_Maude_SortMapping___init__():
    assert Maude_SortMapping.__init__(Maude_SortMapping('', Maude_SortMapping=Maude_Sort()), '', Maude_SortMapping=Maude_Sort()) == None


from python_code import Maude_Statement

def test_Maude_Statement___init__():
    assert Maude_Statement.__init__(Maude_Statement('\x00\x00', '', Maude_Statement=set()), '', '', Maude_Statement=set()) == None


from python_code import Maude_Variable

def test_Maude_Variable___init__():
    assert Maude_Variable.__init__(Maude_Variable(''), '') == None

