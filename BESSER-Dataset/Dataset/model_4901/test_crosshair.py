from python_code import SPL_BooleanConstant

def test_SPL_BooleanConstant___init__():
    assert SPL_BooleanConstant.__init__(SPL_BooleanConstant(True), False) == None


from python_code import SPL_ClientErrorResponse

def test_SPL_ClientErrorResponse___init__():
    assert SPL_ClientErrorResponse.__init__(SPL_ClientErrorResponse(''), '') == None


from python_code import SPL_ControlMethodName

def test_SPL_ControlMethodName___init__():
    assert SPL_ControlMethodName.__init__(SPL_ControlMethodName(''), '') == None


from python_code import SPL_DefinedType

def test_SPL_DefinedType___init__():
    assert SPL_DefinedType.__init__(SPL_DefinedType(''), '') == None


from python_code import SPL_Event

def test_SPL_Event___init__():
    assert SPL_Event.__init__(SPL_Event('', SPL_Event=set(), SPL_Event17=set()), '', SPL_Event=set(), SPL_Event17=set()) == None


from python_code import SPL_Expression
from python_code import SPL_ForeachStat

def test_SPL_ForeachStat___init__():
    assert SPL_ForeachStat.__init__(SPL_ForeachStat('', SPL_ForeachStat=SPL_Expression(), SPL_ForeachStat84=set()), '', SPL_ForeachStat=SPL_Expression(), SPL_ForeachStat84=set()) == None


from python_code import SPL_Expression
from python_code import SPL_ForwardExp

def test_SPL_ForwardExp___init__():
    assert SPL_ForwardExp.__init__(SPL_ForwardExp(True, SPL_ForwardExp=SPL_Expression()), False, SPL_ForwardExp=SPL_Expression()) == None


from python_code import SPL_GlobalErrorResponse

def test_SPL_GlobalErrorResponse___init__():
    assert SPL_GlobalErrorResponse.__init__(SPL_GlobalErrorResponse(''), '') == None


from python_code import SPL_HeadedMessageField

def test_SPL_HeadedMessageField___init__():
    assert SPL_HeadedMessageField.__init__(SPL_HeadedMessageField(''), '') == None


from python_code import SPL_IntegerConstant

def test_SPL_IntegerConstant___init__():
    assert SPL_IntegerConstant.__init__(SPL_IntegerConstant(0), 0) == None


from python_code import SPL_LocatedElement

def test_SPL_LocatedElement___init__():
    assert SPL_LocatedElement.__init__(SPL_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import SPL_NamedBranch
from python_code import SPL_ReturnStat

def test_SPL_NamedBranch___init__():
    assert SPL_NamedBranch.__init__(SPL_NamedBranch('', SPL_NamedBranch=SPL_ReturnStat()), '', SPL_NamedBranch=SPL_ReturnStat()) == None


from python_code import SPL_Expression
from python_code import SPL_OperatorExp

def test_SPL_OperatorExp___init__():
    assert SPL_OperatorExp.__init__(SPL_OperatorExp('', SPL_OperatorExp=SPL_Expression(), SPL_OperatorExp111=SPL_Expression()), '', SPL_OperatorExp=SPL_Expression(), SPL_OperatorExp111=SPL_Expression()) == None


from python_code import SPL_PropertyCallPlace
from python_code import SPL_VariablePlace

def test_SPL_PropertyCallPlace___init__():
    assert SPL_PropertyCallPlace.__init__(SPL_PropertyCallPlace('', SPL_PropertyCallPlace=SPL_VariablePlace()), '', SPL_PropertyCallPlace=SPL_VariablePlace()) == None


from python_code import SPL_RedirectionErrorResponse

def test_SPL_RedirectionErrorResponse___init__():
    assert SPL_RedirectionErrorResponse.__init__(SPL_RedirectionErrorResponse(''), '') == None


from python_code import SPL_RemoteFunctionDeclaration

def test_SPL_RemoteFunctionDeclaration___init__():
    assert SPL_RemoteFunctionDeclaration.__init__(SPL_RemoteFunctionDeclaration(''), '') == None


from python_code import SPL_SIPHeaderPlace

def test_SPL_SIPHeaderPlace___init__():
    assert SPL_SIPHeaderPlace.__init__(SPL_SIPHeaderPlace(''), '') == None


from python_code import SPL_SIPMethodName

def test_SPL_SIPMethodName___init__():
    assert SPL_SIPMethodName.__init__(SPL_SIPMethodName(''), '') == None


from python_code import SPL_SequenceType

def test_SPL_SequenceType___init__():
    assert SPL_SequenceType.__init__(SPL_SequenceType('', '', 0), '\x00', '', 0) == None


from python_code import SPL_ServerErrorResponse

def test_SPL_ServerErrorResponse___init__():
    assert SPL_ServerErrorResponse.__init__(SPL_ServerErrorResponse(''), '') == None


from python_code import SPL_Program
from python_code import SPL_Service

def test_SPL_Service___init__():
    assert SPL_Service.__init__(SPL_Service('', SPL_Service=SPL_Program(), SPL_Service2=set(), SPL_Service4=set()), '', SPL_Service=SPL_Program(), SPL_Service2=set(), SPL_Service4=set()) == None


from python_code import SPL_SimpleType

def test_SPL_SimpleType___init__():
    assert SPL_SimpleType.__init__(SPL_SimpleType(''), '') == None


from python_code import SPL_StringConstant

def test_SPL_StringConstant___init__():
    assert SPL_StringConstant.__init__(SPL_StringConstant(''), '') == None


from python_code import SPL_StructureProperty
from python_code import SPL_TypeExpression

def test_SPL_StructureProperty___init__():
    assert SPL_StructureProperty.__init__(SPL_StructureProperty('', SPL_StructureProperty=SPL_TypeExpression()), '', SPL_StructureProperty=SPL_TypeExpression()) == None


from python_code import SPL_SuccessResponse

def test_SPL_SuccessResponse___init__():
    assert SPL_SuccessResponse.__init__(SPL_SuccessResponse(''), '') == None


from python_code import SPL_URIConstant

def test_SPL_URIConstant___init__():
    assert SPL_URIConstant.__init__(SPL_URIConstant(''), '') == None


from python_code import SPL_Constant
from python_code import SPL_WhenHeader
from python_code import SPL_WhenStat

def test_SPL_WhenHeader___init__():
    assert SPL_WhenHeader.__init__(SPL_WhenHeader('', SPL_WhenHeader=SPL_WhenStat(), SPL_WhenHeader100=SPL_Constant()), '', SPL_WhenHeader=SPL_WhenStat(), SPL_WhenHeader100=SPL_Constant()) == None

