from python_code import hlp_Condition
from python_code import hlp_ConditionalLoop
from python_code import hlp_Expression
from python_code import hlp_IfStatement

def test_hlp_Condition___init__():
    assert hlp_Condition.__init__(hlp_Condition('', hlp_Condition=hlp_IfStatement(), hlp_Condition29=hlp_Expression(), hlp_Condition32=hlp_Expression(), hlp_Condition39=hlp_ConditionalLoop()), '', hlp_Condition=hlp_IfStatement(), hlp_Condition29=hlp_Expression(), hlp_Condition32=hlp_Expression(), hlp_Condition39=hlp_ConditionalLoop()) == None


from python_code import hlp_Expression
from python_code import hlp_ForLoop
from python_code import hlp_VariableReference

def test_hlp_ForLoop___init__():
    assert hlp_ForLoop.__init__(hlp_ForLoop(True, hlp_ForLoop=hlp_VariableReference(), hlp_ForLoop43=hlp_Expression(), hlp_ForLoop46=hlp_Expression()), False, hlp_ForLoop=hlp_VariableReference(), hlp_ForLoop43=hlp_Expression(), hlp_ForLoop46=hlp_Expression()) == None


from python_code import hlp_LiteralValue

def test_hlp_LiteralValue___init__():
    assert hlp_LiteralValue.__init__(hlp_LiteralValue(''), '') == None


from python_code import hlp_Nameable

def test_hlp_Nameable___init__():
    assert hlp_Nameable.__init__(hlp_Nameable(''), '') == None

