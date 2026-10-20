from python_code import debugSeq_Assignment
from python_code import debugSeq_Expression

def test_debugSeq_Assignment___init__():
    assert debugSeq_Assignment.__init__(debugSeq_Assignment('', debugSeq_Assignment=debugSeq_Expression(), debugSeq_Assignment23=debugSeq_Expression()), '', debugSeq_Assignment=debugSeq_Expression(), debugSeq_Assignment23=debugSeq_Expression()) == None


from python_code import debugSeq_Block

def test_debugSeq_Block___init__():
    assert debugSeq_Block.__init__(debugSeq_Block('', debugSeq_Block=set()), '', debugSeq_Block=set()) == None


from python_code import debugSeq_Comparison
from python_code import debugSeq_Expression

def test_debugSeq_Comparison___init__():
    assert debugSeq_Comparison.__init__(debugSeq_Comparison('', debugSeq_Comparison=debugSeq_Expression(), debugSeq_Comparison66=debugSeq_Expression()), '', debugSeq_Comparison=debugSeq_Expression(), debugSeq_Comparison66=debugSeq_Expression()) == None


from python_code import debugSeq_Control
from python_code import debugSeq_Expression

def test_debugSeq_Control___init__():
    assert debugSeq_Control.__init__(debugSeq_Control('\x00', debugSeq_Control=debugSeq_Expression(), debugSeq_Control15=debugSeq_Expression(), debugSeq_Control18=set()), '', debugSeq_Control=debugSeq_Expression(), debugSeq_Control15=debugSeq_Expression(), debugSeq_Control18=set()) == None


from python_code import debugSeq_DebugSeqModel
from python_code import debugSeq_DebugVars

def test_debugSeq_DebugVars___init__():
    assert debugSeq_DebugVars.__init__(debugSeq_DebugVars('', '', '', debugSeq_DebugVars=debugSeq_DebugSeqModel(), debugSeq_DebugVars4=set()), '', '', '', debugSeq_DebugVars=debugSeq_DebugSeqModel(), debugSeq_DebugVars4=set()) == None


from python_code import debugSeq_Equality
from python_code import debugSeq_Expression

def test_debugSeq_Equality___init__():
    assert debugSeq_Equality.__init__(debugSeq_Equality('', debugSeq_Equality61=debugSeq_Expression(), debugSeq_Equality=debugSeq_Expression()), '', debugSeq_Equality61=debugSeq_Expression(), debugSeq_Equality=debugSeq_Expression()) == None


from python_code import debugSeq_IntConstant

def test_debugSeq_IntConstant___init__():
    assert debugSeq_IntConstant.__init__(debugSeq_IntConstant(''), '') == None


from python_code import debugSeq_LoadDebugInfo

def test_debugSeq_LoadDebugInfo___init__():
    assert debugSeq_LoadDebugInfo.__init__(debugSeq_LoadDebugInfo(''), '') == None


from python_code import debugSeq_Expression
from python_code import debugSeq_Message

def test_debugSeq_Message___init__():
    assert debugSeq_Message.__init__(debugSeq_Message('', debugSeq_Message=debugSeq_Expression(), debugSeq_Message112=set()), '', debugSeq_Message=debugSeq_Expression(), debugSeq_Message112=set()) == None


from python_code import debugSeq_Expression
from python_code import debugSeq_Query

def test_debugSeq_Query___init__():
    assert debugSeq_Query.__init__(debugSeq_Query('', debugSeq_Query105=debugSeq_Expression(), debugSeq_Query=debugSeq_Expression()), '', debugSeq_Query105=debugSeq_Expression(), debugSeq_Query=debugSeq_Expression()) == None


from python_code import debugSeq_Expression
from python_code import debugSeq_QueryValue

def test_debugSeq_QueryValue___init__():
    assert debugSeq_QueryValue.__init__(debugSeq_QueryValue('', debugSeq_QueryValue=debugSeq_Expression()), '', debugSeq_QueryValue=debugSeq_Expression()) == None


from python_code import debugSeq_Sequence
from python_code import debugSeq_Sequences

def test_debugSeq_Sequence___init__():
    assert debugSeq_Sequence.__init__(debugSeq_Sequence('', '', '', '', debugSeq_Sequence=debugSeq_Sequences(), debugSeq_Sequence9=set()), '', '', '', '', debugSeq_Sequence=debugSeq_Sequences(), debugSeq_Sequence9=set()) == None


from python_code import debugSeq_SequenceCall

def test_debugSeq_SequenceCall___init__():
    assert debugSeq_SequenceCall.__init__(debugSeq_SequenceCall(''), '') == None


from python_code import debugSeq_Expression
from python_code import debugSeq_Shift

def test_debugSeq_Shift___init__():
    assert debugSeq_Shift.__init__(debugSeq_Shift('', debugSeq_Shift=debugSeq_Expression(), debugSeq_Shift71=debugSeq_Expression()), '', debugSeq_Shift=debugSeq_Expression(), debugSeq_Shift71=debugSeq_Expression()) == None


from python_code import debugSeq_StringConstant

def test_debugSeq_StringConstant___init__():
    assert debugSeq_StringConstant.__init__(debugSeq_StringConstant(''), '') == None


from python_code import debugSeq_Expression
from python_code import debugSeq_VariableDeclaration
from python_code import debugSeq_VariableRef

def test_debugSeq_VariableDeclaration___init__():
    assert debugSeq_VariableDeclaration.__init__(debugSeq_VariableDeclaration('', debugSeq_VariableDeclaration=debugSeq_Expression(), debugSeq_VariableDeclaration183=debugSeq_VariableRef()), '', debugSeq_VariableDeclaration=debugSeq_Expression(), debugSeq_VariableDeclaration183=debugSeq_VariableRef()) == None

