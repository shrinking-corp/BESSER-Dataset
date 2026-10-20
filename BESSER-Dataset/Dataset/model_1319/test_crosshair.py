from python_code import stateMachineDsl_BoolExp

def test_stateMachineDsl_BoolExp___init__():
    assert stateMachineDsl_BoolExp.__init__(stateMachineDsl_BoolExp(''), '') == None


from python_code import stateMachineDsl_Comparison
from python_code import stateMachineDsl_Expression

def test_stateMachineDsl_Comparison___init__():
    assert stateMachineDsl_Comparison.__init__(stateMachineDsl_Comparison('', stateMachineDsl_Comparison=stateMachineDsl_Expression(), stateMachineDsl_Comparison117=stateMachineDsl_Expression()), '', stateMachineDsl_Comparison=stateMachineDsl_Expression(), stateMachineDsl_Comparison117=stateMachineDsl_Expression()) == None


from python_code import stateMachineDsl_DoubleExp

def test_stateMachineDsl_DoubleExp___init__():
    assert stateMachineDsl_DoubleExp.__init__(stateMachineDsl_DoubleExp(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import stateMachineDsl_Equality
from python_code import stateMachineDsl_Expression

def test_stateMachineDsl_Equality___init__():
    assert stateMachineDsl_Equality.__init__(stateMachineDsl_Equality('', stateMachineDsl_Equality=stateMachineDsl_Expression(), stateMachineDsl_Equality112=stateMachineDsl_Expression()), '', stateMachineDsl_Equality=stateMachineDsl_Expression(), stateMachineDsl_Equality112=stateMachineDsl_Expression()) == None


from python_code import stateMachineDsl_Condition
from python_code import stateMachineDsl_Declaration
from python_code import stateMachineDsl_Event
from python_code import stateMachineDsl_Transition

def test_stateMachineDsl_Event___init__():
    assert stateMachineDsl_Event.__init__(stateMachineDsl_Event('', stateMachineDsl_Event=stateMachineDsl_Declaration(), stateMachineDsl_Event30=stateMachineDsl_Transition(), stateMachineDsl_Event45=stateMachineDsl_Condition(), stateMachineDsl_Event48=set()), '', stateMachineDsl_Event=stateMachineDsl_Declaration(), stateMachineDsl_Event30=stateMachineDsl_Transition(), stateMachineDsl_Event45=stateMachineDsl_Condition(), stateMachineDsl_Event48=set()) == None


from python_code import stateMachineDsl_Declaration
from python_code import stateMachineDsl_ExtDeclaration

def test_stateMachineDsl_ExtDeclaration___init__():
    assert stateMachineDsl_ExtDeclaration.__init__(stateMachineDsl_ExtDeclaration('', stateMachineDsl_ExtDeclaration=stateMachineDsl_Declaration(), stateMachineDsl_ExtDeclaration43=set()), '', stateMachineDsl_ExtDeclaration=stateMachineDsl_Declaration(), stateMachineDsl_ExtDeclaration43=set()) == None


from python_code import stateMachineDsl_Expression
from python_code import stateMachineDsl_MulOrDiv

def test_stateMachineDsl_MulOrDiv___init__():
    assert stateMachineDsl_MulOrDiv.__init__(stateMachineDsl_MulOrDiv('', stateMachineDsl_MulOrDiv=stateMachineDsl_Expression(), stateMachineDsl_MulOrDiv132=stateMachineDsl_Expression()), '', stateMachineDsl_MulOrDiv=stateMachineDsl_Expression(), stateMachineDsl_MulOrDiv132=stateMachineDsl_Expression()) == None


from python_code import stateMachineDsl_NumberExp

def test_stateMachineDsl_NumberExp___init__():
    assert stateMachineDsl_NumberExp.__init__(stateMachineDsl_NumberExp('', 0), '', 0) == None


from python_code import stateMachineDsl_Condition
from python_code import stateMachineDsl_Declaration
from python_code import stateMachineDsl_Procedure
from python_code import stateMachineDsl_ProcedureUse

def test_stateMachineDsl_Procedure___init__():
    assert stateMachineDsl_Procedure.__init__(stateMachineDsl_Procedure('', stateMachineDsl_Procedure92=stateMachineDsl_ProcedureUse(), stateMachineDsl_Procedure=stateMachineDsl_Declaration(), stateMachineDsl_Procedure50=set(), stateMachineDsl_Procedure52=stateMachineDsl_Condition(), stateMachineDsl_Procedure55=set()), '', stateMachineDsl_Procedure92=stateMachineDsl_ProcedureUse(), stateMachineDsl_Procedure=stateMachineDsl_Declaration(), stateMachineDsl_Procedure50=set(), stateMachineDsl_Procedure52=stateMachineDsl_Condition(), stateMachineDsl_Procedure55=set()) == None


from python_code import stateMachineDsl_StringExp

def test_stateMachineDsl_StringExp___init__():
    assert stateMachineDsl_StringExp.__init__(stateMachineDsl_StringExp(''), '') == None


from python_code import stateMachineDsl_ChangeAction
from python_code import stateMachineDsl_Parameter
from python_code import stateMachineDsl_SetAction
from python_code import stateMachineDsl_VarParName
from python_code import stateMachineDsl_VarRef
from python_code import stateMachineDsl_Variable

def test_stateMachineDsl_VarParName___init__():
    assert stateMachineDsl_VarParName.__init__(stateMachineDsl_VarParName('', stateMachineDsl_VarParName80=stateMachineDsl_SetAction(), stateMachineDsl_VarParName85=stateMachineDsl_ChangeAction(), stateMachineDsl_VarParName62=stateMachineDsl_Parameter(), stateMachineDsl_VarParName=stateMachineDsl_Variable(), stateMachineDsl_VarParName137=stateMachineDsl_VarRef()), '', stateMachineDsl_VarParName80=stateMachineDsl_SetAction(), stateMachineDsl_VarParName85=stateMachineDsl_ChangeAction(), stateMachineDsl_VarParName62=stateMachineDsl_Parameter(), stateMachineDsl_VarParName=stateMachineDsl_Variable(), stateMachineDsl_VarParName137=stateMachineDsl_VarRef()) == None

