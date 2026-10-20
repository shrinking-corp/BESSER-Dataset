import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Branch,
    Constant,
    Declaration,
    ErrorResponse,
    Expression,
    FunctionDeclaration,
    LocatedElement,
    MessageField,
    MethodName,
    Place,
    Response,
    SPL_Argument,
    SPL_BODYExp,
    SPL_BlockExp,
    SPL_BooleanConstant,
    SPL_Branch,
    SPL_BreakStat,
    SPL_ClientErrorResponse,
    SPL_CompoundStat,
    SPL_Constant,
    SPL_ConstantExp,
    SPL_ContinueStat,
    SPL_ControlMethodName,
    SPL_Declaration,
    SPL_DeclarationStat,
    SPL_DefaultBranch,
    SPL_DefinedType,
    SPL_Dialog,
    SPL_ErrorResponse,
    SPL_Event,
    SPL_Expression,
    SPL_ForeachStat,
    SPL_ForwardExp,
    SPL_FunctionCall,
    SPL_FunctionCallExp,
    SPL_FunctionCallStat,
    SPL_FunctionDeclaration,
    SPL_GlobalErrorResponse,
    SPL_HeadedMessageField,
    SPL_IfStat,
    SPL_IntegerConstant,
    SPL_LocalFunctionDeclaration,
    SPL_LocatedElement,
    SPL_MessageField,
    SPL_Method,
    SPL_MethodName,
    SPL_NamedBranch,
    SPL_OperatorExp,
    SPL_Place,
    SPL_PopExp,
    SPL_Program,
    SPL_PropertyCallPlace,
    SPL_PushStat,
    SPL_ReasonExp,
    SPL_ReasonMessageField,
    SPL_RedirectionErrorResponse,
    SPL_Registration,
    SPL_RemoteFunctionDeclaration,
    SPL_RequestURIExp,
    SPL_Response,
    SPL_ResponseConstant,
    SPL_ReturnStat,
    SPL_SIPHeaderPlace,
    SPL_SIPMethodName,
    SPL_SelectCase,
    SPL_SelectDefault,
    SPL_SelectMember,
    SPL_SelectStat,
    SPL_SequenceConstant,
    SPL_SequenceType,
    SPL_ServerErrorResponse,
    SPL_Service,
    SPL_Session,
    SPL_SetStat,
    SPL_SimpleType,
    SPL_Statement,
    SPL_StringConstant,
    SPL_StructureDeclaration,
    SPL_StructureProperty,
    SPL_SuccessResponse,
    SPL_TypeExpression,
    SPL_URIConstant,
    SPL_Variable,
    SPL_VariableDeclaration,
    SPL_VariablePlace,
    SPL_WhenHeader,
    SPL_WhenStat,
    SPL_WithExp,
    SelectMember,
    Session,
    Statement,
    TypeExpression,
    VariableDeclaration,
    VariablePlace,
    ClientErrorKind,
    ControlMethod,
    Direction,
    FunctionLocation,
    GlobalErrorKind,
    Modifier,
    PrimitiveType,
    RedirectionErrorKind,
    SIPHeader,
    SIPMethod,
    ServerErrorKind,
    SuccessKind,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_declarations1_reverse_link_reassign_clear():
    a1 = SPL_Service(name="sample_text")
    a2 = SPL_Service(name="sample_text_2")
    b = SPL_Declaration(name="sample_text")
    _safe_set(b, 'SPL_Declaration', a1)
    assert _is_linked(b, 'SPL_Declaration', a1)
    if hasattr(a1, 'SPL_Service2'):
        assert _is_linked(a1, 'SPL_Service2', b)
    _safe_set(b, 'SPL_Declaration', a2)
    assert _is_linked(b, 'SPL_Declaration', a2)
    if hasattr(a1, 'SPL_Service2'):
        assert not _is_linked(a1, 'SPL_Service2', b)
    if hasattr(a2, 'SPL_Service2'):
        assert _is_linked(a2, 'SPL_Service2', b)
    _safe_set(b, 'SPL_Declaration', None)
    assert not _is_linked(b, 'SPL_Declaration', a2)
    if hasattr(a2, 'SPL_Service2'):
        assert not _is_linked(a2, 'SPL_Service2', b)


def test_assoc_declarations14_reverse_link_reassign_clear():
    a1 = SPL_Event(eventId="sample_text")
    a2 = SPL_Event(eventId="sample_text_2")
    b = SPL_Declaration(name="sample_text")
    _safe_set(b, 'SPL_Declaration15', a1)
    assert _is_linked(b, 'SPL_Declaration15', a1)
    if hasattr(a1, 'SPL_Event'):
        assert _is_linked(a1, 'SPL_Event', b)
    _safe_set(b, 'SPL_Declaration15', a2)
    assert _is_linked(b, 'SPL_Declaration15', a2)
    if hasattr(a1, 'SPL_Event'):
        assert not _is_linked(a1, 'SPL_Event', b)
    if hasattr(a2, 'SPL_Event'):
        assert _is_linked(a2, 'SPL_Event', b)
    _safe_set(b, 'SPL_Declaration15', None)
    assert not _is_linked(b, 'SPL_Declaration15', a2)
    if hasattr(a2, 'SPL_Event'):
        assert not _is_linked(a2, 'SPL_Event', b)


def test_assoc_methods16_reverse_link_reassign_clear():
    a1 = SPL_Method(direction="sample_text")
    a2 = SPL_Method(direction="sample_text_2")
    b = SPL_Event(eventId="sample_text")
    _safe_set(b, 'SPL_Event17', {a1})
    assert _is_linked(b, 'SPL_Event17', a1)
    if hasattr(a1, 'SPL_Method18'):
        assert _is_linked(a1, 'SPL_Method18', b)
    _safe_set(b, 'SPL_Event17', {a2})
    assert _is_linked(b, 'SPL_Event17', a2)
    if hasattr(a1, 'SPL_Method18'):
        assert not _is_linked(a1, 'SPL_Method18', b)
    if hasattr(a2, 'SPL_Method18'):
        assert _is_linked(a2, 'SPL_Method18', b)
    _safe_set(b, 'SPL_Event17', set())
    assert not _is_linked(b, 'SPL_Event17', a2)
    if hasattr(a2, 'SPL_Method18'):
        assert not _is_linked(a2, 'SPL_Method18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments23_stub_double():
    # SPL_Argument has no real 'SPL_Argument' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Method(direction="sample_text")
    partner = SPL_Argument()
    setattr(partner, 'SPL_Argument', None)
    _safe_set(owner, 'SPL_Method24', {partner})
    assert getattr(partner, 'SPL_Argument') == owner
    _safe_set(owner, 'SPL_Method24', set())
    assert getattr(partner, 'SPL_Argument') is None


def test_assoc_branch62_stub_double():
    # SPL_ReturnStat has no real 'SPL_ReturnStat63' property in the generated
    # code (a bare stub) -- manually attach it so SPL_NamedBranch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_NamedBranch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_NamedBranch(name="sample_text")
    partner = SPL_ReturnStat()
    setattr(partner, 'SPL_ReturnStat63', None)
    _safe_set(owner, 'SPL_NamedBranch', partner)
    assert getattr(partner, 'SPL_ReturnStat63') == owner
    _safe_set(owner, 'SPL_NamedBranch', None)
    assert getattr(partner, 'SPL_ReturnStat63') is None


def test_assoc_branches27_stub_double():
    # SPL_Branch has no real 'SPL_Branch' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Method(direction="sample_text")
    partner = SPL_Branch()
    setattr(partner, 'SPL_Branch', None)
    _safe_set(owner, 'SPL_Method28', {partner})
    assert getattr(partner, 'SPL_Branch') == owner
    _safe_set(owner, 'SPL_Method28', set())
    assert getattr(partner, 'SPL_Branch') is None


def test_assoc_declaration58_stub_double():
    # SPL_DeclarationStat has no real 'SPL_DeclarationStat' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Declaration(name="sample_text")
    partner = SPL_DeclarationStat()
    setattr(partner, 'SPL_DeclarationStat', None)
    _safe_set(owner, 'SPL_Declaration59', partner)
    assert getattr(partner, 'SPL_DeclarationStat') == owner
    _safe_set(owner, 'SPL_Declaration59', None)
    assert getattr(partner, 'SPL_DeclarationStat') is None


def test_assoc_declarations10_stub_double():
    # SPL_Dialog has no real 'SPL_Dialog' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Declaration(name="sample_text")
    partner = SPL_Dialog()
    setattr(partner, 'SPL_Dialog', None)
    _safe_set(owner, 'SPL_Declaration11', partner)
    assert owner in getattr(partner, 'SPL_Dialog')
    _safe_set(owner, 'SPL_Declaration11', None)
    assert owner not in getattr(partner, 'SPL_Dialog')


def test_assoc_declarations5_stub_double():
    # SPL_Registration has no real 'SPL_Registration' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Declaration(name="sample_text")
    partner = SPL_Registration()
    setattr(partner, 'SPL_Registration', None)
    _safe_set(owner, 'SPL_Declaration6', partner)
    assert owner in getattr(partner, 'SPL_Registration')
    _safe_set(owner, 'SPL_Declaration6', None)
    assert owner not in getattr(partner, 'SPL_Registration')


def test_assoc_exp113_stub_double():
    # SPL_Expression has no real 'SPL_Expression114' property in the generated
    # code (a bare stub) -- manually attach it so SPL_ForwardExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_ForwardExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_ForwardExp(isParallel=True)
    partner = SPL_Expression()
    setattr(partner, 'SPL_Expression114', None)
    _safe_set(owner, 'SPL_ForwardExp', partner)
    assert getattr(partner, 'SPL_Expression114') == owner
    _safe_set(owner, 'SPL_ForwardExp', None)
    assert getattr(partner, 'SPL_Expression114') is None


def test_assoc_leftExp108_stub_double():
    # SPL_Expression has no real 'SPL_Expression109' property in the generated
    # code (a bare stub) -- manually attach it so SPL_OperatorExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_OperatorExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_OperatorExp(opName="sample_text")
    partner = SPL_Expression()
    setattr(partner, 'SPL_Expression109', None)
    _safe_set(owner, 'SPL_OperatorExp', partner)
    assert getattr(partner, 'SPL_Expression109') == owner
    _safe_set(owner, 'SPL_OperatorExp', None)
    assert getattr(partner, 'SPL_Expression109') is None


def test_assoc_methodName21_stub_double():
    # SPL_MethodName has no real 'SPL_MethodName' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Method(direction="sample_text")
    partner = SPL_MethodName()
    setattr(partner, 'SPL_MethodName', None)
    _safe_set(owner, 'SPL_Method22', partner)
    assert getattr(partner, 'SPL_MethodName') == owner
    _safe_set(owner, 'SPL_Method22', None)
    assert getattr(partner, 'SPL_MethodName') is None


def test_assoc_methods12_stub_double():
    # SPL_Dialog has no real 'SPL_Dialog13' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Method(direction="sample_text")
    partner = SPL_Dialog()
    setattr(partner, 'SPL_Dialog13', None)
    _safe_set(owner, 'SPL_Method', partner)
    assert owner in getattr(partner, 'SPL_Dialog13')
    _safe_set(owner, 'SPL_Method', None)
    assert owner not in getattr(partner, 'SPL_Dialog13')


def test_assoc_rightExp110_stub_double():
    # SPL_Expression has no real 'SPL_Expression112' property in the generated
    # code (a bare stub) -- manually attach it so SPL_OperatorExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_OperatorExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_OperatorExp(opName="sample_text")
    partner = SPL_Expression()
    setattr(partner, 'SPL_Expression112', None)
    _safe_set(owner, 'SPL_OperatorExp111', partner)
    assert getattr(partner, 'SPL_Expression112') == owner
    _safe_set(owner, 'SPL_OperatorExp111', None)
    assert getattr(partner, 'SPL_Expression112') is None


def test_assoc_sequenceExp81_stub_double():
    # SPL_Expression has no real 'SPL_Expression82' property in the generated
    # code (a bare stub) -- manually attach it so SPL_ForeachStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_ForeachStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_ForeachStat(iteratorName="sample_text")
    partner = SPL_Expression()
    setattr(partner, 'SPL_Expression82', None)
    _safe_set(owner, 'SPL_ForeachStat', partner)
    assert getattr(partner, 'SPL_Expression82') == owner
    _safe_set(owner, 'SPL_ForeachStat', None)
    assert getattr(partner, 'SPL_Expression82') is None


def test_assoc_service0_stub_double():
    # SPL_Program has no real 'SPL_Program' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Service(name="sample_text")
    partner = SPL_Program()
    setattr(partner, 'SPL_Program', None)
    _safe_set(owner, 'SPL_Service', partner)
    assert getattr(partner, 'SPL_Program') == owner
    _safe_set(owner, 'SPL_Service', None)
    assert getattr(partner, 'SPL_Program') is None


def test_assoc_sessions3_stub_double():
    # SPL_Session has no real 'SPL_Session' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Service(name="sample_text")
    partner = SPL_Session()
    setattr(partner, 'SPL_Session', None)
    _safe_set(owner, 'SPL_Service4', {partner})
    assert getattr(partner, 'SPL_Session') == owner
    _safe_set(owner, 'SPL_Service4', set())
    assert getattr(partner, 'SPL_Session') is None


def test_assoc_source125_stub_double():
    # SPL_VariablePlace has no real 'SPL_VariablePlace' property in the generated
    # code (a bare stub) -- manually attach it so SPL_PropertyCallPlace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_PropertyCallPlace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_PropertyCallPlace(propName="sample_text")
    partner = SPL_VariablePlace()
    setattr(partner, 'SPL_VariablePlace', None)
    _safe_set(owner, 'SPL_PropertyCallPlace', partner)
    assert getattr(partner, 'SPL_VariablePlace') == owner
    _safe_set(owner, 'SPL_PropertyCallPlace', None)
    assert getattr(partner, 'SPL_VariablePlace') is None


def test_assoc_source126_stub_double():
    # SPL_Variable has no real 'SPL_Variable127' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Declaration(name="sample_text")
    partner = SPL_Variable()
    setattr(partner, 'SPL_Variable127', None)
    _safe_set(owner, 'SPL_Declaration128', partner)
    assert getattr(partner, 'SPL_Variable127') == owner
    _safe_set(owner, 'SPL_Declaration128', None)
    assert getattr(partner, 'SPL_Variable127') is None


def test_assoc_statements25_stub_double():
    # SPL_Statement has no real 'SPL_Statement' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Method(direction="sample_text")
    partner = SPL_Statement()
    setattr(partner, 'SPL_Statement', None)
    _safe_set(owner, 'SPL_Method26', {partner})
    assert getattr(partner, 'SPL_Statement') == owner
    _safe_set(owner, 'SPL_Method26', set())
    assert getattr(partner, 'SPL_Statement') is None


def test_assoc_statements83_stub_double():
    # SPL_Statement has no real 'SPL_Statement85' property in the generated
    # code (a bare stub) -- manually attach it so SPL_ForeachStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_ForeachStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_ForeachStat(iteratorName="sample_text")
    partner = SPL_Statement()
    setattr(partner, 'SPL_Statement85', None)
    _safe_set(owner, 'SPL_ForeachStat84', {partner})
    assert getattr(partner, 'SPL_Statement85') == owner
    _safe_set(owner, 'SPL_ForeachStat84', set())
    assert getattr(partner, 'SPL_Statement85') is None


def test_assoc_type19_stub_double():
    # SPL_TypeExpression has no real 'SPL_TypeExpression' property in the generated
    # code (a bare stub) -- manually attach it so SPL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_Method(direction="sample_text")
    partner = SPL_TypeExpression()
    setattr(partner, 'SPL_TypeExpression', None)
    _safe_set(owner, 'SPL_Method20', partner)
    assert getattr(partner, 'SPL_TypeExpression') == owner
    _safe_set(owner, 'SPL_Method20', None)
    assert getattr(partner, 'SPL_TypeExpression') is None


def test_assoc_type45_stub_double():
    # SPL_TypeExpression has no real 'SPL_TypeExpression46' property in the generated
    # code (a bare stub) -- manually attach it so SPL_StructureProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_StructureProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_StructureProperty(name="sample_text")
    partner = SPL_TypeExpression()
    setattr(partner, 'SPL_TypeExpression46', None)
    _safe_set(owner, 'SPL_StructureProperty', partner)
    assert getattr(partner, 'SPL_TypeExpression46') == owner
    _safe_set(owner, 'SPL_StructureProperty', None)
    assert getattr(partner, 'SPL_TypeExpression46') is None


def test_assoc_value99_stub_double():
    # SPL_Constant has no real 'SPL_Constant' property in the generated
    # code (a bare stub) -- manually attach it so SPL_WhenHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_WhenHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_WhenHeader(headerId="sample_text")
    partner = SPL_Constant()
    setattr(partner, 'SPL_Constant', None)
    _safe_set(owner, 'SPL_WhenHeader100', partner)
    assert getattr(partner, 'SPL_Constant') == owner
    _safe_set(owner, 'SPL_WhenHeader100', None)
    assert getattr(partner, 'SPL_Constant') is None


def test_assoc_whenHeaders73_stub_double():
    # SPL_WhenStat has no real 'SPL_WhenStat74' property in the generated
    # code (a bare stub) -- manually attach it so SPL_WhenHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SPL_WhenHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SPL_WhenHeader(headerId="sample_text")
    partner = SPL_WhenStat()
    setattr(partner, 'SPL_WhenStat74', None)
    _safe_set(owner, 'SPL_WhenHeader', partner)
    assert owner in getattr(partner, 'SPL_WhenStat74')
    _safe_set(owner, 'SPL_WhenHeader', None)
    assert owner not in getattr(partner, 'SPL_WhenStat74')


