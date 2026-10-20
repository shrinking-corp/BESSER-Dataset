from python_code import nuSMV_ArrayType
from python_code import nuSMV_SimpleType

def test_nuSMV_ArrayType___init__():
    assert nuSMV_ArrayType.__init__(nuSMV_ArrayType('', '\x00', nuSMV_ArrayType=nuSMV_SimpleType()), '\x00\x00', '', nuSMV_ArrayType=nuSMV_SimpleType()) == None


from python_code import nuSMV_AssignConstraintElement

def test_nuSMV_AssignConstraintElement___init__():
    assert nuSMV_AssignConstraintElement.__init__(nuSMV_AssignConstraintElement('', nuSMV_AssignConstraintElement=set()), '', nuSMV_AssignConstraintElement=set()) == None


from python_code import nuSMV_BinaryExpression
from python_code import nuSMV_SimpleExpression

def test_nuSMV_BinaryExpression___init__():
    assert nuSMV_BinaryExpression.__init__(nuSMV_BinaryExpression('', '\x00', nuSMV_BinaryExpression=nuSMV_SimpleExpression(), nuSMV_BinaryExpression78=nuSMV_SimpleExpression()), '\x00\x00', '', nuSMV_BinaryExpression=nuSMV_SimpleExpression(), nuSMV_BinaryExpression78=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_ComputeSpecification
from python_code import nuSMV_RTCTLExpression

def test_nuSMV_ComputeSpecification___init__():
    assert nuSMV_ComputeSpecification.__init__(nuSMV_ComputeSpecification('', nuSMV_ComputeSpecification=nuSMV_RTCTLExpression(), nuSMV_ComputeSpecification71=nuSMV_RTCTLExpression()), '', nuSMV_ComputeSpecification=nuSMV_RTCTLExpression(), nuSMV_ComputeSpecification71=nuSMV_RTCTLExpression()) == None


from python_code import nuSMV_ConstantsDeclaration

def test_nuSMV_ConstantsDeclaration___init__():
    assert nuSMV_ConstantsDeclaration.__init__(nuSMV_ConstantsDeclaration('', False), '', False) == None


from python_code import nuSMV_CTLExpression
from python_code import nuSMV_CtlSpecification

def test_nuSMV_CtlSpecification___init__():
    assert nuSMV_CtlSpecification.__init__(nuSMV_CtlSpecification('\x00\x00', False, '', True, nuSMV_CtlSpecification=nuSMV_CTLExpression()), '', False, '', False, nuSMV_CtlSpecification=nuSMV_CTLExpression()) == None


from python_code import nuSMV_DefineDeclaration

def test_nuSMV_DefineDeclaration___init__():
    assert nuSMV_DefineDeclaration.__init__(nuSMV_DefineDeclaration('', nuSMV_DefineDeclaration=set()), '', nuSMV_DefineDeclaration=set()) == None


from python_code import nuSMV_FairnessConstraint

def test_nuSMV_FairnessConstraint___init__():
    assert nuSMV_FairnessConstraint.__init__(nuSMV_FairnessConstraint(True), False) == None


from python_code import nuSMV_InitConstraint
from python_code import nuSMV_SimpleExpression

def test_nuSMV_InitConstraint___init__():
    assert nuSMV_InitConstraint.__init__(nuSMV_InitConstraint(True, nuSMV_InitConstraint=nuSMV_SimpleExpression()), False, nuSMV_InitConstraint=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_IntervalExpression

def test_nuSMV_IntervalExpression___init__():
    assert nuSMV_IntervalExpression.__init__(nuSMV_IntervalExpression('', '\x00'), '\x00\x00', '') == None


from python_code import nuSMV_IntervalType

def test_nuSMV_IntervalType___init__():
    assert nuSMV_IntervalType.__init__(nuSMV_IntervalType('', '\x00'), '\x00\x00', '') == None


from python_code import nuSMV_InvarConstraint
from python_code import nuSMV_SimpleExpression

def test_nuSMV_InvarConstraint___init__():
    assert nuSMV_InvarConstraint.__init__(nuSMV_InvarConstraint(True, nuSMV_InvarConstraint=nuSMV_SimpleExpression()), False, nuSMV_InvarConstraint=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_InvarSpecification
from python_code import nuSMV_NextExpression

def test_nuSMV_InvarSpecification___init__():
    assert nuSMV_InvarSpecification.__init__(nuSMV_InvarSpecification('', False, nuSMV_InvarSpecification=nuSMV_NextExpression()), '', False, nuSMV_InvarSpecification=nuSMV_NextExpression()) == None


from python_code import nuSMV_IsaDeclaration

def test_nuSMV_IsaDeclaration___init__():
    assert nuSMV_IsaDeclaration.__init__(nuSMV_IsaDeclaration(''), '') == None


from python_code import nuSMV_LTLExpression
from python_code import nuSMV_LtlSpecification

def test_nuSMV_LtlSpecification___init__():
    assert nuSMV_LtlSpecification.__init__(nuSMV_LtlSpecification(False, '', False, nuSMV_LtlSpecification=nuSMV_LTLExpression()), False, '', False, nuSMV_LtlSpecification=nuSMV_LTLExpression()) == None


from python_code import nuSMV_Module
from python_code import nuSMV_ModuleType
from python_code import nuSMV_NuSmvModel

def test_nuSMV_Module___init__():
    assert nuSMV_Module.__init__(nuSMV_Module('', nuSMV_Module=nuSMV_NuSmvModel(), nuSMV_Module2=set(), nuSMV_Module4=set(), nuSMV_Module46=nuSMV_ModuleType()), '', nuSMV_Module=nuSMV_NuSmvModel(), nuSMV_Module2=set(), nuSMV_Module4=set(), nuSMV_Module46=nuSMV_ModuleType()) == None


from python_code import nuSMV_ParsExpression
from python_code import nuSMV_SimpleExpression

def test_nuSMV_ParsExpression___init__():
    assert nuSMV_ParsExpression.__init__(nuSMV_ParsExpression(True, nuSMV_ParsExpression=nuSMV_SimpleExpression()), False, nuSMV_ParsExpression=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_SignedWordType

def test_nuSMV_SignedWordType___init__():
    assert nuSMV_SignedWordType.__init__(nuSMV_SignedWordType(''), '') == None


from python_code import nuSMV_SimpleExpression
from python_code import nuSMV_TransConstraint

def test_nuSMV_TransConstraint___init__():
    assert nuSMV_TransConstraint.__init__(nuSMV_TransConstraint(True, nuSMV_TransConstraint=nuSMV_SimpleExpression()), False, nuSMV_TransConstraint=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_SimpleExpression
from python_code import nuSMV_UnaryExpression

def test_nuSMV_UnaryExpression___init__():
    assert nuSMV_UnaryExpression.__init__(nuSMV_UnaryExpression('', nuSMV_UnaryExpression=nuSMV_SimpleExpression()), '', nuSMV_UnaryExpression=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_SimpleExpression
from python_code import nuSMV_UnaryFunctionExpression

def test_nuSMV_UnaryFunctionExpression___init__():
    assert nuSMV_UnaryFunctionExpression.__init__(nuSMV_UnaryFunctionExpression('', nuSMV_UnaryFunctionExpression=nuSMV_SimpleExpression()), '', nuSMV_UnaryFunctionExpression=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_UnsignedWordType

def test_nuSMV_UnsignedWordType___init__():
    assert nuSMV_UnsignedWordType.__init__(nuSMV_UnsignedWordType(''), '') == None


from python_code import nuSMV_SimpleExpression
from python_code import nuSMV_UntilCTLexpression

def test_nuSMV_UntilCTLexpression___init__():
    assert nuSMV_UntilCTLexpression.__init__(nuSMV_UntilCTLexpression('', nuSMV_UntilCTLexpression=nuSMV_SimpleExpression()), '', nuSMV_UntilCTLexpression=nuSMV_SimpleExpression()) == None


from python_code import nuSMV_EnumType
from python_code import nuSMV_SetElementExpression
from python_code import nuSMV_Val

def test_nuSMV_Val___init__():
    assert nuSMV_Val.__init__(nuSMV_Val('', '\x00', nuSMV_Val=nuSMV_EnumType(), nuSMV_Val92=nuSMV_SetElementExpression()), '\x00\x00', '', nuSMV_Val=nuSMV_EnumType(), nuSMV_Val92=nuSMV_SetElementExpression()) == None


from python_code import nuSMV_ValueExpression

def test_nuSMV_ValueExpression___init__():
    assert nuSMV_ValueExpression.__init__(nuSMV_ValueExpression(''), '') == None


from python_code import nuSMV_FrozenVariableDeclaration
from python_code import nuSMV_IVariableDeclaration
from python_code import nuSMV_ModuleType
from python_code import nuSMV_Type
from python_code import nuSMV_Var
from python_code import nuSMV_VarBody
from python_code import nuSMV_VariableDeclaration

def test_nuSMV_VarBody___init__():
    assert nuSMV_VarBody.__init__(nuSMV_VarBody('', False, nuSMV_VarBody=nuSMV_VariableDeclaration(), nuSMV_VarBody7=nuSMV_IVariableDeclaration(), nuSMV_VarBody52=nuSMV_ModuleType(), nuSMV_VarBody87=nuSMV_Var(), nuSMV_VarBody9=nuSMV_FrozenVariableDeclaration(), nuSMV_VarBody11=nuSMV_Type()), '', False, nuSMV_VarBody=nuSMV_VariableDeclaration(), nuSMV_VarBody7=nuSMV_IVariableDeclaration(), nuSMV_VarBody52=nuSMV_ModuleType(), nuSMV_VarBody87=nuSMV_Var(), nuSMV_VarBody9=nuSMV_FrozenVariableDeclaration(), nuSMV_VarBody11=nuSMV_Type()) == None


from python_code import nuSMV_WordExpression

def test_nuSMV_WordExpression___init__():
    assert nuSMV_WordExpression.__init__(nuSMV_WordExpression(''), '') == None


from python_code import nuSMV_WordType

def test_nuSMV_WordType___init__():
    assert nuSMV_WordType.__init__(nuSMV_WordType(''), '') == None

