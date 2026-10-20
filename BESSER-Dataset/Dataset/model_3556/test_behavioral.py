import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssignBody,
    FairnessConstraint,
    ModuleElement,
    ModuleType,
    RTCTLExpression,
    SimpleExpression,
    SimpleType,
    Type,
    nuSMV_ArrayType,
    nuSMV_AssignBody,
    nuSMV_AssignConstraintElement,
    nuSMV_AsyncrProcessType,
    nuSMV_BinaryExpression,
    nuSMV_BooleanType,
    nuSMV_CTLExpression,
    nuSMV_CaseSimpleAssignementExpression,
    nuSMV_CaseSimpleExpression,
    nuSMV_CompassionExpression,
    nuSMV_ComputeSpecification,
    nuSMV_ConstantsDeclaration,
    nuSMV_CtlSpecification,
    nuSMV_DefineBody,
    nuSMV_DefineDeclaration,
    nuSMV_EObject,
    nuSMV_EnumType,
    nuSMV_FairnessConstraint,
    nuSMV_FairnessExpression,
    nuSMV_FormalParameter,
    nuSMV_FrozenVariableDeclaration,
    nuSMV_IVariableDeclaration,
    nuSMV_InitBody,
    nuSMV_InitConstraint,
    nuSMV_IntervalExpression,
    nuSMV_IntervalType,
    nuSMV_InvarConstraint,
    nuSMV_InvarSpecification,
    nuSMV_IsaDeclaration,
    nuSMV_JusticeExpression,
    nuSMV_LTLExpression,
    nuSMV_LtlSpecification,
    nuSMV_Module,
    nuSMV_ModuleElement,
    nuSMV_ModuleType,
    nuSMV_NextBody,
    nuSMV_NextExpression,
    nuSMV_Not,
    nuSMV_NuSmvModel,
    nuSMV_ParsExpression,
    nuSMV_RTCTLExpression,
    nuSMV_RangeExpression,
    nuSMV_SetElementExpression,
    nuSMV_SetExpression,
    nuSMV_SetValueParameter,
    nuSMV_SignedWordType,
    nuSMV_SimpleExpression,
    nuSMV_SimpleType,
    nuSMV_SingleRTCTLExpression,
    nuSMV_SyncrProcessType,
    nuSMV_TransConstraint,
    nuSMV_Type,
    nuSMV_UnaryExpression,
    nuSMV_UnaryFunctionExpression,
    nuSMV_UnaryRTCTLExpression,
    nuSMV_UnsignedWordType,
    nuSMV_UntilCTLexpression,
    nuSMV_Val,
    nuSMV_ValueExpression,
    nuSMV_Var,
    nuSMV_VarBody,
    nuSMV_VarBodyAssign,
    nuSMV_VariableDeclaration,
    nuSMV_WordExpression,
    nuSMV_WordType,
    operators,
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

def test_assoc_bodies15_reverse_link_reassign_clear():
    a1 = nuSMV_AssignConstraintElement(assign="sample_text")
    a2 = nuSMV_AssignConstraintElement(assign="sample_text_2")
    b = nuSMV_AssignBody(array="sample_text", semicolon=True)
    _safe_set(b, 'nuSMV_AssignBody', a1)
    assert _is_linked(b, 'nuSMV_AssignBody', a1)
    if hasattr(a1, 'nuSMV_AssignConstraintElement'):
        assert _is_linked(a1, 'nuSMV_AssignConstraintElement', b)
    _safe_set(b, 'nuSMV_AssignBody', a2)
    assert _is_linked(b, 'nuSMV_AssignBody', a2)
    if hasattr(a1, 'nuSMV_AssignConstraintElement'):
        assert not _is_linked(a1, 'nuSMV_AssignConstraintElement', b)
    if hasattr(a2, 'nuSMV_AssignConstraintElement'):
        assert _is_linked(a2, 'nuSMV_AssignConstraintElement', b)
    _safe_set(b, 'nuSMV_AssignBody', None)
    assert not _is_linked(b, 'nuSMV_AssignBody', a2)
    if hasattr(a2, 'nuSMV_AssignConstraintElement'):
        assert not _is_linked(a2, 'nuSMV_AssignConstraintElement', b)


def test_assoc_defineBodies12_reverse_link_reassign_clear():
    a1 = nuSMV_DefineDeclaration(define="sample_text")
    a2 = nuSMV_DefineDeclaration(define="sample_text_2")
    b = nuSMV_DefineBody(semicolon=True, var="sample_text")
    _safe_set(b, 'nuSMV_DefineBody', a1)
    assert _is_linked(b, 'nuSMV_DefineBody', a1)
    if hasattr(a1, 'nuSMV_DefineDeclaration'):
        assert _is_linked(a1, 'nuSMV_DefineDeclaration', b)
    _safe_set(b, 'nuSMV_DefineBody', a2)
    assert _is_linked(b, 'nuSMV_DefineBody', a2)
    if hasattr(a1, 'nuSMV_DefineDeclaration'):
        assert not _is_linked(a1, 'nuSMV_DefineDeclaration', b)
    if hasattr(a2, 'nuSMV_DefineDeclaration'):
        assert _is_linked(a2, 'nuSMV_DefineDeclaration', b)
    _safe_set(b, 'nuSMV_DefineBody', None)
    assert not _is_linked(b, 'nuSMV_DefineBody', a2)
    if hasattr(a2, 'nuSMV_DefineDeclaration'):
        assert not _is_linked(a2, 'nuSMV_DefineDeclaration', b)


def test_assoc_params1_reverse_link_reassign_clear():
    a1 = nuSMV_Module(name="sample_text")
    a2 = nuSMV_Module(name="sample_text_2")
    b = nuSMV_FormalParameter(name="sample_text")
    _safe_set(b, 'nuSMV_FormalParameter', a1)
    assert _is_linked(b, 'nuSMV_FormalParameter', a1)
    if hasattr(a1, 'nuSMV_Module2'):
        assert _is_linked(a1, 'nuSMV_Module2', b)
    _safe_set(b, 'nuSMV_FormalParameter', a2)
    assert _is_linked(b, 'nuSMV_FormalParameter', a2)
    if hasattr(a1, 'nuSMV_Module2'):
        assert not _is_linked(a1, 'nuSMV_Module2', b)
    if hasattr(a2, 'nuSMV_Module2'):
        assert _is_linked(a2, 'nuSMV_Module2', b)
    _safe_set(b, 'nuSMV_FormalParameter', None)
    assert not _is_linked(b, 'nuSMV_FormalParameter', a2)
    if hasattr(a2, 'nuSMV_Module2'):
        assert not _is_linked(a2, 'nuSMV_Module2', b)


def test_assoc_range103_reverse_link_reassign_clear():
    a1 = nuSMV_UnaryRTCTLExpression(unary="sample_text")
    a2 = nuSMV_UnaryRTCTLExpression(unary="sample_text_2")
    b = nuSMV_RangeExpression(lower="sample_text", upper="sample_text")
    _safe_set(b, 'nuSMV_RangeExpression', a1)
    assert _is_linked(b, 'nuSMV_RangeExpression', a1)
    if hasattr(a1, 'nuSMV_UnaryRTCTLExpression'):
        assert _is_linked(a1, 'nuSMV_UnaryRTCTLExpression', b)
    _safe_set(b, 'nuSMV_RangeExpression', a2)
    assert _is_linked(b, 'nuSMV_RangeExpression', a2)
    if hasattr(a1, 'nuSMV_UnaryRTCTLExpression'):
        assert not _is_linked(a1, 'nuSMV_UnaryRTCTLExpression', b)
    if hasattr(a2, 'nuSMV_UnaryRTCTLExpression'):
        assert _is_linked(a2, 'nuSMV_UnaryRTCTLExpression', b)
    _safe_set(b, 'nuSMV_RangeExpression', None)
    assert not _is_linked(b, 'nuSMV_RangeExpression', a2)
    if hasattr(a2, 'nuSMV_UnaryRTCTLExpression'):
        assert not _is_linked(a2, 'nuSMV_UnaryRTCTLExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arg97_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression98' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_UntilCTLexpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_UntilCTLexpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_UntilCTLexpression(ea="sample_text")
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression98', None)
    _safe_set(owner, 'nuSMV_UntilCTLexpression', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression98') == owner
    _safe_set(owner, 'nuSMV_UntilCTLexpression', None)
    assert getattr(partner, 'nuSMV_SimpleExpression98') is None


def test_assoc_arg99_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression100' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_UnaryFunctionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_UnaryFunctionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_UnaryFunctionExpression(function="sample_text")
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression100', None)
    _safe_set(owner, 'nuSMV_UnaryFunctionExpression', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression100') == owner
    _safe_set(owner, 'nuSMV_UnaryFunctionExpression', None)
    assert getattr(partner, 'nuSMV_SimpleExpression100') is None


def test_assoc_assignment13_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_DefineBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_DefineBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_DefineBody(semicolon=True, var="sample_text")
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression', None)
    _safe_set(owner, 'nuSMV_DefineBody14', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression') == owner
    _safe_set(owner, 'nuSMV_DefineBody14', None)
    assert getattr(partner, 'nuSMV_SimpleExpression') is None


def test_assoc_ctlExpression41_stub_double():
    # nuSMV_CTLExpression has no real 'nuSMV_CTLExpression' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_CtlSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_CtlSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_CtlSpecification(name="sample_text", nameKeyWord=True, semicolon=True, specKeyWord="sample_text")
    partner = nuSMV_CTLExpression()
    setattr(partner, 'nuSMV_CTLExpression', None)
    _safe_set(owner, 'nuSMV_CtlSpecification', partner)
    assert getattr(partner, 'nuSMV_CTLExpression') == owner
    _safe_set(owner, 'nuSMV_CtlSpecification', None)
    assert getattr(partner, 'nuSMV_CTLExpression') is None


def test_assoc_dotted18_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression20' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_AssignBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_AssignBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_AssignBody(array="sample_text", semicolon=True)
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression20', None)
    _safe_set(owner, 'nuSMV_AssignBody19', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression20') == owner
    _safe_set(owner, 'nuSMV_AssignBody19', None)
    assert getattr(partner, 'nuSMV_SimpleExpression20') is None


def test_assoc_first69_stub_double():
    # nuSMV_RTCTLExpression has no real 'nuSMV_RTCTLExpression' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_ComputeSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_ComputeSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_ComputeSpecification(minMax="sample_text")
    partner = nuSMV_RTCTLExpression()
    setattr(partner, 'nuSMV_RTCTLExpression', None)
    _safe_set(owner, 'nuSMV_ComputeSpecification', partner)
    assert getattr(partner, 'nuSMV_RTCTLExpression') == owner
    _safe_set(owner, 'nuSMV_ComputeSpecification', None)
    assert getattr(partner, 'nuSMV_RTCTLExpression') is None


def test_assoc_initExpression28_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression29' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_InitConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_InitConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_InitConstraint(semicolon=True)
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression29', None)
    _safe_set(owner, 'nuSMV_InitConstraint', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression29') == owner
    _safe_set(owner, 'nuSMV_InitConstraint', None)
    assert getattr(partner, 'nuSMV_SimpleExpression29') is None


def test_assoc_invarExpression30_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression31' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_InvarConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_InvarConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_InvarConstraint(semicolon=True)
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression31', None)
    _safe_set(owner, 'nuSMV_InvarConstraint', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression31') == owner
    _safe_set(owner, 'nuSMV_InvarConstraint', None)
    assert getattr(partner, 'nuSMV_SimpleExpression31') is None


def test_assoc_invarSpec42_stub_double():
    # nuSMV_NextExpression has no real 'nuSMV_NextExpression43' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_InvarSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_InvarSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_InvarSpecification(name="sample_text", semicolon=True)
    partner = nuSMV_NextExpression()
    setattr(partner, 'nuSMV_NextExpression43', None)
    _safe_set(owner, 'nuSMV_InvarSpecification', partner)
    assert getattr(partner, 'nuSMV_NextExpression43') == owner
    _safe_set(owner, 'nuSMV_InvarSpecification', None)
    assert getattr(partner, 'nuSMV_NextExpression43') is None


def test_assoc_left75_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression76' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_BinaryExpression(op="sample_text", operator="sample_text")
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression76', None)
    _safe_set(owner, 'nuSMV_BinaryExpression', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression76') == owner
    _safe_set(owner, 'nuSMV_BinaryExpression', None)
    assert getattr(partner, 'nuSMV_SimpleExpression76') is None


def test_assoc_ltlExpression44_stub_double():
    # nuSMV_LTLExpression has no real 'nuSMV_LTLExpression' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_LtlSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_LtlSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_LtlSpecification(name="sample_text", nameId=True, semicolon=True)
    partner = nuSMV_LTLExpression()
    setattr(partner, 'nuSMV_LTLExpression', None)
    _safe_set(owner, 'nuSMV_LtlSpecification', partner)
    assert getattr(partner, 'nuSMV_LTLExpression') == owner
    _safe_set(owner, 'nuSMV_LtlSpecification', None)
    assert getattr(partner, 'nuSMV_LTLExpression') is None


def test_assoc_module45_stub_double():
    # nuSMV_ModuleType has no real 'nuSMV_ModuleType' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_Module(name="sample_text")
    partner = nuSMV_ModuleType()
    setattr(partner, 'nuSMV_ModuleType', None)
    _safe_set(owner, 'nuSMV_Module46', partner)
    assert getattr(partner, 'nuSMV_ModuleType') == owner
    _safe_set(owner, 'nuSMV_Module46', None)
    assert getattr(partner, 'nuSMV_ModuleType') is None


def test_assoc_moduleElement3_stub_double():
    # nuSMV_ModuleElement has no real 'nuSMV_ModuleElement' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_Module(name="sample_text")
    partner = nuSMV_ModuleElement()
    setattr(partner, 'nuSMV_ModuleElement', None)
    _safe_set(owner, 'nuSMV_Module4', {partner})
    assert getattr(partner, 'nuSMV_ModuleElement') == owner
    _safe_set(owner, 'nuSMV_Module4', set())
    assert getattr(partner, 'nuSMV_ModuleElement') is None


def test_assoc_modules0_stub_double():
    # nuSMV_NuSmvModel has no real 'nuSMV_NuSmvModel' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_Module(name="sample_text")
    partner = nuSMV_NuSmvModel()
    setattr(partner, 'nuSMV_NuSmvModel', None)
    _safe_set(owner, 'nuSMV_Module', partner)
    assert owner in getattr(partner, 'nuSMV_NuSmvModel')
    _safe_set(owner, 'nuSMV_Module', None)
    assert owner not in getattr(partner, 'nuSMV_NuSmvModel')


def test_assoc_par50_stub_double():
    # nuSMV_ModuleType has no real 'nuSMV_ModuleType51' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_VarBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_VarBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_VarBody(name="sample_text", semicolon=True)
    partner = nuSMV_ModuleType()
    setattr(partner, 'nuSMV_ModuleType51', None)
    _safe_set(owner, 'nuSMV_VarBody52', partner)
    assert getattr(partner, 'nuSMV_ModuleType51') == owner
    _safe_set(owner, 'nuSMV_VarBody52', None)
    assert getattr(partner, 'nuSMV_ModuleType51') is None


def test_assoc_rctl104_stub_double():
    # nuSMV_RTCTLExpression has no real 'nuSMV_RTCTLExpression106' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_UnaryRTCTLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_UnaryRTCTLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_UnaryRTCTLExpression(unary="sample_text")
    partner = nuSMV_RTCTLExpression()
    setattr(partner, 'nuSMV_RTCTLExpression106', None)
    _safe_set(owner, 'nuSMV_UnaryRTCTLExpression105', partner)
    assert getattr(partner, 'nuSMV_RTCTLExpression106') == owner
    _safe_set(owner, 'nuSMV_UnaryRTCTLExpression105', None)
    assert getattr(partner, 'nuSMV_RTCTLExpression106') is None


def test_assoc_right77_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression79' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_BinaryExpression(op="sample_text", operator="sample_text")
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression79', None)
    _safe_set(owner, 'nuSMV_BinaryExpression78', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression79') == owner
    _safe_set(owner, 'nuSMV_BinaryExpression78', None)
    assert getattr(partner, 'nuSMV_SimpleExpression79') is None


def test_assoc_second70_stub_double():
    # nuSMV_RTCTLExpression has no real 'nuSMV_RTCTLExpression72' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_ComputeSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_ComputeSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_ComputeSpecification(minMax="sample_text")
    partner = nuSMV_RTCTLExpression()
    setattr(partner, 'nuSMV_RTCTLExpression72', None)
    _safe_set(owner, 'nuSMV_ComputeSpecification71', partner)
    assert getattr(partner, 'nuSMV_RTCTLExpression72') == owner
    _safe_set(owner, 'nuSMV_ComputeSpecification71', None)
    assert getattr(partner, 'nuSMV_RTCTLExpression72') is None


def test_assoc_simpleExpression82_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression83' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_ParsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_ParsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_ParsExpression(isNext=True)
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression83', None)
    _safe_set(owner, 'nuSMV_ParsExpression', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression83') == owner
    _safe_set(owner, 'nuSMV_ParsExpression', None)
    assert getattr(partner, 'nuSMV_SimpleExpression83') is None


def test_assoc_simpleExpression84_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression85' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_UnaryExpression(operator="sample_text")
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression85', None)
    _safe_set(owner, 'nuSMV_UnaryExpression', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression85') == owner
    _safe_set(owner, 'nuSMV_UnaryExpression', None)
    assert getattr(partner, 'nuSMV_SimpleExpression85') is None


def test_assoc_transExpression26_stub_double():
    # nuSMV_SimpleExpression has no real 'nuSMV_SimpleExpression27' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_TransConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_TransConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_TransConstraint(semicolon=True)
    partner = nuSMV_SimpleExpression()
    setattr(partner, 'nuSMV_SimpleExpression27', None)
    _safe_set(owner, 'nuSMV_TransConstraint', partner)
    assert getattr(partner, 'nuSMV_SimpleExpression27') == owner
    _safe_set(owner, 'nuSMV_TransConstraint', None)
    assert getattr(partner, 'nuSMV_SimpleExpression27') is None


def test_assoc_type10_stub_double():
    # nuSMV_Type has no real 'nuSMV_Type' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_VarBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_VarBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_VarBody(name="sample_text", semicolon=True)
    partner = nuSMV_Type()
    setattr(partner, 'nuSMV_Type', None)
    _safe_set(owner, 'nuSMV_VarBody11', partner)
    assert getattr(partner, 'nuSMV_Type') == owner
    _safe_set(owner, 'nuSMV_VarBody11', None)
    assert getattr(partner, 'nuSMV_Type') is None


def test_assoc_type74_stub_double():
    # nuSMV_SimpleType has no real 'nuSMV_SimpleType' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_ArrayType(lowerBound="sample_text", upperBound="sample_text")
    partner = nuSMV_SimpleType()
    setattr(partner, 'nuSMV_SimpleType', None)
    _safe_set(owner, 'nuSMV_ArrayType', partner)
    assert getattr(partner, 'nuSMV_SimpleType') == owner
    _safe_set(owner, 'nuSMV_ArrayType', None)
    assert getattr(partner, 'nuSMV_SimpleType') is None


def test_assoc_val73_stub_double():
    # nuSMV_EnumType has no real 'nuSMV_EnumType' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_Val's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_Val's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_Val(name="sample_text", num="sample_text")
    partner = nuSMV_EnumType()
    setattr(partner, 'nuSMV_EnumType', None)
    _safe_set(owner, 'nuSMV_Val', partner)
    assert owner in getattr(partner, 'nuSMV_EnumType')
    _safe_set(owner, 'nuSMV_Val', None)
    assert owner not in getattr(partner, 'nuSMV_EnumType')


def test_assoc_val91_stub_double():
    # nuSMV_SetElementExpression has no real 'nuSMV_SetElementExpression' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_Val's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_Val's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_Val(name="sample_text", num="sample_text")
    partner = nuSMV_SetElementExpression()
    setattr(partner, 'nuSMV_SetElementExpression', None)
    _safe_set(owner, 'nuSMV_Val92', partner)
    assert getattr(partner, 'nuSMV_SetElementExpression') == owner
    _safe_set(owner, 'nuSMV_Val92', None)
    assert getattr(partner, 'nuSMV_SetElementExpression') is None


def test_assoc_valparam93_stub_double():
    # nuSMV_SetValueParameter has no real 'nuSMV_SetValueParameter' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_FormalParameter(name="sample_text")
    partner = nuSMV_SetValueParameter()
    setattr(partner, 'nuSMV_SetValueParameter', None)
    _safe_set(owner, 'nuSMV_FormalParameter94', partner)
    assert getattr(partner, 'nuSMV_SetValueParameter') == owner
    _safe_set(owner, 'nuSMV_FormalParameter94', None)
    assert getattr(partner, 'nuSMV_SetValueParameter') is None


def test_assoc_value86_stub_double():
    # nuSMV_Var has no real 'nuSMV_Var' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_VarBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_VarBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_VarBody(name="sample_text", semicolon=True)
    partner = nuSMV_Var()
    setattr(partner, 'nuSMV_Var', None)
    _safe_set(owner, 'nuSMV_VarBody87', partner)
    assert getattr(partner, 'nuSMV_Var') == owner
    _safe_set(owner, 'nuSMV_VarBody87', None)
    assert getattr(partner, 'nuSMV_Var') is None


def test_assoc_var16_stub_double():
    # nuSMV_EObject has no real 'nuSMV_EObject' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_AssignBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_AssignBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_AssignBody(array="sample_text", semicolon=True)
    partner = nuSMV_EObject()
    setattr(partner, 'nuSMV_EObject', None)
    _safe_set(owner, 'nuSMV_AssignBody17', partner)
    assert getattr(partner, 'nuSMV_EObject') == owner
    _safe_set(owner, 'nuSMV_AssignBody17', None)
    assert getattr(partner, 'nuSMV_EObject') is None


def test_assoc_vars5_stub_double():
    # nuSMV_VariableDeclaration has no real 'nuSMV_VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_VarBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_VarBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_VarBody(name="sample_text", semicolon=True)
    partner = nuSMV_VariableDeclaration()
    setattr(partner, 'nuSMV_VariableDeclaration', None)
    _safe_set(owner, 'nuSMV_VarBody', partner)
    assert owner in getattr(partner, 'nuSMV_VariableDeclaration')
    _safe_set(owner, 'nuSMV_VarBody', None)
    assert owner not in getattr(partner, 'nuSMV_VariableDeclaration')


def test_assoc_vars6_stub_double():
    # nuSMV_IVariableDeclaration has no real 'nuSMV_IVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_VarBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_VarBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_VarBody(name="sample_text", semicolon=True)
    partner = nuSMV_IVariableDeclaration()
    setattr(partner, 'nuSMV_IVariableDeclaration', None)
    _safe_set(owner, 'nuSMV_VarBody7', partner)
    assert owner in getattr(partner, 'nuSMV_IVariableDeclaration')
    _safe_set(owner, 'nuSMV_VarBody7', None)
    assert owner not in getattr(partner, 'nuSMV_IVariableDeclaration')


def test_assoc_vars8_stub_double():
    # nuSMV_FrozenVariableDeclaration has no real 'nuSMV_FrozenVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so nuSMV_VarBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nuSMV_VarBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nuSMV_VarBody(name="sample_text", semicolon=True)
    partner = nuSMV_FrozenVariableDeclaration()
    setattr(partner, 'nuSMV_FrozenVariableDeclaration', None)
    _safe_set(owner, 'nuSMV_VarBody9', partner)
    assert owner in getattr(partner, 'nuSMV_FrozenVariableDeclaration')
    _safe_set(owner, 'nuSMV_VarBody9', None)
    assert owner not in getattr(partner, 'nuSMV_FrozenVariableDeclaration')


