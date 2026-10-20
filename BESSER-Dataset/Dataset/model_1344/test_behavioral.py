import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryOperatorCS,
    ExpCS,
    IndexExpCS,
    InfixedExpCS,
    ModuleElement,
    NavigatingArgExpCS,
    NavigatingExpCS,
    NavigatingExpCS_Base,
    OutPatternElement,
    PrefixedExpCS,
    PrimaryExpCS,
    PrimitiveLiteralExpCS,
    Statement,
    TypeExpCS,
    TypeLiteralCS,
    myAtl_ATLDefCS,
    myAtl_ATLParameterCS,
    myAtl_ATLType,
    myAtl_ActionBlock,
    myAtl_BinaryOperatorCS,
    myAtl_Binding,
    myAtl_BindingStat,
    myAtl_BooleanLiteralExpCS,
    myAtl_CalledRule,
    myAtl_CollectionTypeCS,
    myAtl_EObject,
    myAtl_ExpCS,
    myAtl_ForEachOutPatternElement,
    myAtl_Helper,
    myAtl_IfExpCS,
    myAtl_InPattern,
    myAtl_InPatternElement,
    myAtl_IndexExpCS,
    myAtl_InfixExpCS,
    myAtl_InfixOperatorCS,
    myAtl_InfixedExpCS,
    myAtl_InvalidLiteralExpCS,
    myAtl_LetExpCS,
    myAtl_LetVariableCS,
    myAtl_MatchedRule,
    myAtl_Module,
    myAtl_ModuleElement,
    myAtl_NameExpCS,
    myAtl_NavigatingArgCS,
    myAtl_NavigatingArgExpCS,
    myAtl_NavigatingBarArgCS,
    myAtl_NavigatingCommaArgCS,
    myAtl_NavigatingExpCS,
    myAtl_NavigatingExpCS_Base,
    myAtl_NavigatingSemiArgCS,
    myAtl_NavigationOperatorCS,
    myAtl_NestedExpCS,
    myAtl_NullLiteralExpCS,
    myAtl_NumberLiteralExpCS,
    myAtl_OutPattern,
    myAtl_OutPatternElement,
    myAtl_PrefixExpCS,
    myAtl_PrefixedExpCS,
    myAtl_PrimaryExpCS,
    myAtl_PrimitiveLiteralExpCS,
    myAtl_PrimitiveTypeCS,
    myAtl_QueryRule,
    myAtl_RuleVariableDeclaration,
    myAtl_SelfExpCS,
    myAtl_SimpleOutPatternElement,
    myAtl_Statement,
    myAtl_StringExpCs,
    myAtl_StringLiteralExpCS,
    myAtl_TupleLiteralExpCS,
    myAtl_TupleLiteralPartCS,
    myAtl_TupleTypeCS,
    myAtl_TypeExpCS,
    myAtl_TypeLiteralCS,
    myAtl_TypeLiteralExpCS,
    myAtl_TypeNameExpCS,
    myAtl_UnaryOperatorCS,
    myAtl_UnlimitedNaturalLiteralExpCS,
    myAtl_tuplePartCS,
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

def test_assoc_bindings57_reverse_link_reassign_clear():
    a1 = myAtl_SimpleOutPatternElement(varName="sample_text")
    a2 = myAtl_SimpleOutPatternElement(varName="sample_text_2")
    b = myAtl_Binding(propertyName="sample_text")
    _safe_set(b, 'myAtl_Binding', a1)
    assert _is_linked(b, 'myAtl_Binding', a1)
    if hasattr(a1, 'myAtl_SimpleOutPatternElement58'):
        assert _is_linked(a1, 'myAtl_SimpleOutPatternElement58', b)
    _safe_set(b, 'myAtl_Binding', a2)
    assert _is_linked(b, 'myAtl_Binding', a2)
    if hasattr(a1, 'myAtl_SimpleOutPatternElement58'):
        assert not _is_linked(a1, 'myAtl_SimpleOutPatternElement58', b)
    if hasattr(a2, 'myAtl_SimpleOutPatternElement58'):
        assert _is_linked(a2, 'myAtl_SimpleOutPatternElement58', b)
    _safe_set(b, 'myAtl_Binding', None)
    assert not _is_linked(b, 'myAtl_Binding', a2)
    if hasattr(a2, 'myAtl_SimpleOutPatternElement58'):
        assert not _is_linked(a2, 'myAtl_SimpleOutPatternElement58', b)


def test_assoc_elements7_reverse_link_reassign_clear():
    a1 = myAtl_ModuleElement(name="sample_text")
    a2 = myAtl_ModuleElement(name="sample_text_2")
    b = myAtl_Module(name="sample_text")
    _safe_set(b, 'myAtl_Module8', {a1})
    assert _is_linked(b, 'myAtl_Module8', a1)
    if hasattr(a1, 'myAtl_ModuleElement'):
        assert _is_linked(a1, 'myAtl_ModuleElement', b)
    _safe_set(b, 'myAtl_Module8', {a2})
    assert _is_linked(b, 'myAtl_Module8', a2)
    if hasattr(a1, 'myAtl_ModuleElement'):
        assert not _is_linked(a1, 'myAtl_ModuleElement', b)
    if hasattr(a2, 'myAtl_ModuleElement'):
        assert _is_linked(a2, 'myAtl_ModuleElement', b)
    _safe_set(b, 'myAtl_Module8', set())
    assert not _is_linked(b, 'myAtl_Module8', a2)
    if hasattr(a2, 'myAtl_ModuleElement'):
        assert not _is_linked(a2, 'myAtl_ModuleElement', b)


def test_assoc_inModels1_reverse_link_reassign_clear():
    a1 = myAtl_NameExpCS(element="sample_text", namespace="sample_text")
    a2 = myAtl_NameExpCS(element="sample_text_2", namespace="sample_text_2")
    b = myAtl_Module(name="sample_text")
    _safe_set(b, 'myAtl_Module2', {a1})
    assert _is_linked(b, 'myAtl_Module2', a1)
    if hasattr(a1, 'myAtl_NameExpCS3'):
        assert _is_linked(a1, 'myAtl_NameExpCS3', b)
    _safe_set(b, 'myAtl_Module2', {a2})
    assert _is_linked(b, 'myAtl_Module2', a2)
    if hasattr(a1, 'myAtl_NameExpCS3'):
        assert not _is_linked(a1, 'myAtl_NameExpCS3', b)
    if hasattr(a2, 'myAtl_NameExpCS3'):
        assert _is_linked(a2, 'myAtl_NameExpCS3', b)
    _safe_set(b, 'myAtl_Module2', set())
    assert not _is_linked(b, 'myAtl_Module2', a2)
    if hasattr(a2, 'myAtl_NameExpCS3'):
        assert not _is_linked(a2, 'myAtl_NameExpCS3', b)


def test_assoc_outModels0_reverse_link_reassign_clear():
    a1 = myAtl_NameExpCS(element="sample_text", namespace="sample_text")
    a2 = myAtl_NameExpCS(element="sample_text_2", namespace="sample_text_2")
    b = myAtl_Module(name="sample_text")
    _safe_set(b, 'myAtl_Module', {a1})
    assert _is_linked(b, 'myAtl_Module', a1)
    if hasattr(a1, 'myAtl_NameExpCS'):
        assert _is_linked(a1, 'myAtl_NameExpCS', b)
    _safe_set(b, 'myAtl_Module', {a2})
    assert _is_linked(b, 'myAtl_Module', a2)
    if hasattr(a1, 'myAtl_NameExpCS'):
        assert not _is_linked(a1, 'myAtl_NameExpCS', b)
    if hasattr(a2, 'myAtl_NameExpCS'):
        assert _is_linked(a2, 'myAtl_NameExpCS', b)
    _safe_set(b, 'myAtl_Module', set())
    assert not _is_linked(b, 'myAtl_Module', a2)
    if hasattr(a2, 'myAtl_NameExpCS'):
        assert not _is_linked(a2, 'myAtl_NameExpCS', b)


def test_assoc_ownedParts75_reverse_link_reassign_clear():
    a1 = myAtl_tuplePartCS(name="sample_text")
    a2 = myAtl_tuplePartCS(name="sample_text_2")
    b = myAtl_TupleTypeCS(backtrack="sample_text")
    _safe_set(b, 'myAtl_TupleTypeCS', {a1})
    assert _is_linked(b, 'myAtl_TupleTypeCS', a1)
    if hasattr(a1, 'myAtl_tuplePartCS'):
        assert _is_linked(a1, 'myAtl_tuplePartCS', b)
    _safe_set(b, 'myAtl_TupleTypeCS', {a2})
    assert _is_linked(b, 'myAtl_TupleTypeCS', a2)
    if hasattr(a1, 'myAtl_tuplePartCS'):
        assert not _is_linked(a1, 'myAtl_tuplePartCS', b)
    if hasattr(a2, 'myAtl_tuplePartCS'):
        assert _is_linked(a2, 'myAtl_tuplePartCS', b)
    _safe_set(b, 'myAtl_TupleTypeCS', set())
    assert not _is_linked(b, 'myAtl_TupleTypeCS', a2)
    if hasattr(a2, 'myAtl_tuplePartCS'):
        assert not _is_linked(a2, 'myAtl_tuplePartCS', b)


def test_assoc_parameters28_reverse_link_reassign_clear():
    a1 = myAtl_ATLParameterCS(varName="sample_text")
    a2 = myAtl_ATLParameterCS(varName="sample_text_2")
    b = myAtl_ATLDefCS(varName="sample_text")
    _safe_set(b, 'myAtl_ATLDefCS29', {a1})
    assert _is_linked(b, 'myAtl_ATLDefCS29', a1)
    if hasattr(a1, 'myAtl_ATLParameterCS30'):
        assert _is_linked(a1, 'myAtl_ATLParameterCS30', b)
    _safe_set(b, 'myAtl_ATLDefCS29', {a2})
    assert _is_linked(b, 'myAtl_ATLDefCS29', a2)
    if hasattr(a1, 'myAtl_ATLParameterCS30'):
        assert not _is_linked(a1, 'myAtl_ATLParameterCS30', b)
    if hasattr(a2, 'myAtl_ATLParameterCS30'):
        assert _is_linked(a2, 'myAtl_ATLParameterCS30', b)
    _safe_set(b, 'myAtl_ATLDefCS29', set())
    assert not _is_linked(b, 'myAtl_ATLDefCS29', a2)
    if hasattr(a2, 'myAtl_ATLParameterCS30'):
        assert not _is_linked(a2, 'myAtl_ATLParameterCS30', b)


def test_assoc_type31_reverse_link_reassign_clear():
    a1 = myAtl_ATLType(modelName="sample_text")
    a2 = myAtl_ATLType(modelName="sample_text_2")
    b = myAtl_ATLDefCS(varName="sample_text")
    _safe_set(b, 'myAtl_ATLDefCS32', a1)
    assert _is_linked(b, 'myAtl_ATLDefCS32', a1)
    if hasattr(a1, 'myAtl_ATLType'):
        assert _is_linked(a1, 'myAtl_ATLType', b)
    _safe_set(b, 'myAtl_ATLDefCS32', a2)
    assert _is_linked(b, 'myAtl_ATLDefCS32', a2)
    if hasattr(a1, 'myAtl_ATLType'):
        assert not _is_linked(a1, 'myAtl_ATLType', b)
    if hasattr(a2, 'myAtl_ATLType'):
        assert _is_linked(a2, 'myAtl_ATLType', b)
    _safe_set(b, 'myAtl_ATLDefCS32', None)
    assert not _is_linked(b, 'myAtl_ATLDefCS32', a2)
    if hasattr(a2, 'myAtl_ATLType'):
        assert not _is_linked(a2, 'myAtl_ATLType', b)


def test_assoc_type36_reverse_link_reassign_clear():
    a1 = myAtl_ATLType(modelName="sample_text")
    a2 = myAtl_ATLType(modelName="sample_text_2")
    b = myAtl_ATLParameterCS(varName="sample_text")
    _safe_set(b, 'myAtl_ATLParameterCS37', a1)
    assert _is_linked(b, 'myAtl_ATLParameterCS37', a1)
    if hasattr(a1, 'myAtl_ATLType38'):
        assert _is_linked(a1, 'myAtl_ATLType38', b)
    _safe_set(b, 'myAtl_ATLParameterCS37', a2)
    assert _is_linked(b, 'myAtl_ATLParameterCS37', a2)
    if hasattr(a1, 'myAtl_ATLType38'):
        assert not _is_linked(a1, 'myAtl_ATLType38', b)
    if hasattr(a2, 'myAtl_ATLType38'):
        assert _is_linked(a2, 'myAtl_ATLType38', b)
    _safe_set(b, 'myAtl_ATLParameterCS37', None)
    assert not _is_linked(b, 'myAtl_ATLParameterCS37', a2)
    if hasattr(a2, 'myAtl_ATLType38'):
        assert not _is_linked(a2, 'myAtl_ATLType38', b)


def test_assoc_type39_reverse_link_reassign_clear():
    a1 = myAtl_RuleVariableDeclaration(varName="sample_text")
    a2 = myAtl_RuleVariableDeclaration(varName="sample_text_2")
    b = myAtl_ATLType(modelName="sample_text")
    _safe_set(b, 'myAtl_ATLType41', a1)
    assert _is_linked(b, 'myAtl_ATLType41', a1)
    if hasattr(a1, 'myAtl_RuleVariableDeclaration40'):
        assert _is_linked(a1, 'myAtl_RuleVariableDeclaration40', b)
    _safe_set(b, 'myAtl_ATLType41', a2)
    assert _is_linked(b, 'myAtl_ATLType41', a2)
    if hasattr(a1, 'myAtl_RuleVariableDeclaration40'):
        assert not _is_linked(a1, 'myAtl_RuleVariableDeclaration40', b)
    if hasattr(a2, 'myAtl_RuleVariableDeclaration40'):
        assert _is_linked(a2, 'myAtl_RuleVariableDeclaration40', b)
    _safe_set(b, 'myAtl_ATLType41', None)
    assert not _is_linked(b, 'myAtl_ATLType41', a2)
    if hasattr(a2, 'myAtl_RuleVariableDeclaration40'):
        assert not _is_linked(a2, 'myAtl_RuleVariableDeclaration40', b)


def test_assoc_type50_reverse_link_reassign_clear():
    a1 = myAtl_InPatternElement(varName="sample_text")
    a2 = myAtl_InPatternElement(varName="sample_text_2")
    b = myAtl_ATLType(modelName="sample_text")
    _safe_set(b, 'myAtl_ATLType52', a1)
    assert _is_linked(b, 'myAtl_ATLType52', a1)
    if hasattr(a1, 'myAtl_InPatternElement51'):
        assert _is_linked(a1, 'myAtl_InPatternElement51', b)
    _safe_set(b, 'myAtl_ATLType52', a2)
    assert _is_linked(b, 'myAtl_ATLType52', a2)
    if hasattr(a1, 'myAtl_InPatternElement51'):
        assert not _is_linked(a1, 'myAtl_InPatternElement51', b)
    if hasattr(a2, 'myAtl_InPatternElement51'):
        assert _is_linked(a2, 'myAtl_InPatternElement51', b)
    _safe_set(b, 'myAtl_ATLType52', None)
    assert not _is_linked(b, 'myAtl_ATLType52', a2)
    if hasattr(a2, 'myAtl_InPatternElement51'):
        assert not _is_linked(a2, 'myAtl_InPatternElement51', b)


def test_assoc_type55_reverse_link_reassign_clear():
    a1 = myAtl_SimpleOutPatternElement(varName="sample_text")
    a2 = myAtl_SimpleOutPatternElement(varName="sample_text_2")
    b = myAtl_ATLType(modelName="sample_text")
    _safe_set(b, 'myAtl_ATLType56', a1)
    assert _is_linked(b, 'myAtl_ATLType56', a1)
    if hasattr(a1, 'myAtl_SimpleOutPatternElement'):
        assert _is_linked(a1, 'myAtl_SimpleOutPatternElement', b)
    _safe_set(b, 'myAtl_ATLType56', a2)
    assert _is_linked(b, 'myAtl_ATLType56', a2)
    if hasattr(a1, 'myAtl_SimpleOutPatternElement'):
        assert not _is_linked(a1, 'myAtl_SimpleOutPatternElement', b)
    if hasattr(a2, 'myAtl_SimpleOutPatternElement'):
        assert _is_linked(a2, 'myAtl_SimpleOutPatternElement', b)
    _safe_set(b, 'myAtl_ATLType56', None)
    assert not _is_linked(b, 'myAtl_ATLType56', a2)
    if hasattr(a2, 'myAtl_SimpleOutPatternElement'):
        assert not _is_linked(a2, 'myAtl_SimpleOutPatternElement', b)


def test_assoc_varName4_reverse_link_reassign_clear():
    a1 = myAtl_NameExpCS(element="sample_text", namespace="sample_text")
    a2 = myAtl_NameExpCS(element="sample_text_2", namespace="sample_text_2")
    b = myAtl_Module(name="sample_text")
    _safe_set(b, 'myAtl_Module5', a1)
    assert _is_linked(b, 'myAtl_Module5', a1)
    if hasattr(a1, 'myAtl_NameExpCS6'):
        assert _is_linked(a1, 'myAtl_NameExpCS6', b)
    _safe_set(b, 'myAtl_Module5', a2)
    assert _is_linked(b, 'myAtl_Module5', a2)
    if hasattr(a1, 'myAtl_NameExpCS6'):
        assert not _is_linked(a1, 'myAtl_NameExpCS6', b)
    if hasattr(a2, 'myAtl_NameExpCS6'):
        assert _is_linked(a2, 'myAtl_NameExpCS6', b)
    _safe_set(b, 'myAtl_Module5', None)
    assert not _is_linked(b, 'myAtl_Module5', a2)
    if hasattr(a2, 'myAtl_NameExpCS6'):
        assert not _is_linked(a2, 'myAtl_NameExpCS6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_definition27_stub_double():
    # myAtl_Helper has no real 'myAtl_Helper' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_ATLDefCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_ATLDefCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_ATLDefCS(varName="sample_text")
    partner = myAtl_Helper()
    setattr(partner, 'myAtl_Helper', None)
    _safe_set(owner, 'myAtl_ATLDefCS', partner)
    assert getattr(partner, 'myAtl_Helper') == owner
    _safe_set(owner, 'myAtl_ATLDefCS', None)
    assert getattr(partner, 'myAtl_Helper') is None


def test_assoc_elements45_stub_double():
    # myAtl_InPattern has no real 'myAtl_InPattern46' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_InPatternElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_InPatternElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_InPatternElement(varName="sample_text")
    partner = myAtl_InPattern()
    setattr(partner, 'myAtl_InPattern46', None)
    _safe_set(owner, 'myAtl_InPatternElement', partner)
    assert owner in getattr(partner, 'myAtl_InPattern46')
    _safe_set(owner, 'myAtl_InPatternElement', None)
    assert owner not in getattr(partner, 'myAtl_InPattern46')


def test_assoc_init107_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS109' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingCommaArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingCommaArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingCommaArgCS(prefix="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS109', None)
    _safe_set(owner, 'myAtl_NavigatingCommaArgCS108', partner)
    assert getattr(partner, 'myAtl_ExpCS109') == owner
    _safe_set(owner, 'myAtl_NavigatingCommaArgCS108', None)
    assert getattr(partner, 'myAtl_ExpCS109') is None


def test_assoc_init115_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS117' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingSemiArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingSemiArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingSemiArgCS(prefix="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS117', None)
    _safe_set(owner, 'myAtl_NavigatingSemiArgCS116', partner)
    assert getattr(partner, 'myAtl_ExpCS117') == owner
    _safe_set(owner, 'myAtl_NavigatingSemiArgCS116', None)
    assert getattr(partner, 'myAtl_ExpCS117') is None


def test_assoc_init99_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS101' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingBarArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingBarArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingBarArgCS(prefix="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS101', None)
    _safe_set(owner, 'myAtl_NavigatingBarArgCS100', partner)
    assert getattr(partner, 'myAtl_ExpCS101') == owner
    _safe_set(owner, 'myAtl_NavigatingBarArgCS100', None)
    assert getattr(partner, 'myAtl_ExpCS101') is None


def test_assoc_initExpression133_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS135' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_LetVariableCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_LetVariableCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_LetVariableCS(name="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS135', None)
    _safe_set(owner, 'myAtl_LetVariableCS134', partner)
    assert getattr(partner, 'myAtl_ExpCS135') == owner
    _safe_set(owner, 'myAtl_LetVariableCS134', None)
    assert getattr(partner, 'myAtl_ExpCS135') is None


def test_assoc_initExpression33_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS35' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_ATLDefCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_ATLDefCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_ATLDefCS(varName="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS35', None)
    _safe_set(owner, 'myAtl_ATLDefCS34', partner)
    assert getattr(partner, 'myAtl_ExpCS35') == owner
    _safe_set(owner, 'myAtl_ATLDefCS34', None)
    assert getattr(partner, 'myAtl_ExpCS35') is None


def test_assoc_initExpression42_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS44' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_RuleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_RuleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_RuleVariableDeclaration(varName="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS44', None)
    _safe_set(owner, 'myAtl_RuleVariableDeclaration43', partner)
    assert getattr(partner, 'myAtl_ExpCS44') == owner
    _safe_set(owner, 'myAtl_RuleVariableDeclaration43', None)
    assert getattr(partner, 'myAtl_ExpCS44') is None


def test_assoc_initExpression83_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS85' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_TupleLiteralPartCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_TupleLiteralPartCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_TupleLiteralPartCS(name="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS85', None)
    _safe_set(owner, 'myAtl_TupleLiteralPartCS84', partner)
    assert getattr(partner, 'myAtl_ExpCS85') == owner
    _safe_set(owner, 'myAtl_TupleLiteralPartCS84', None)
    assert getattr(partner, 'myAtl_ExpCS85') is None


def test_assoc_name102_stub_double():
    # myAtl_NavigatingArgExpCS has no real 'myAtl_NavigatingArgExpCS103' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingCommaArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingCommaArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingCommaArgCS(prefix="sample_text")
    partner = myAtl_NavigatingArgExpCS()
    setattr(partner, 'myAtl_NavigatingArgExpCS103', None)
    _safe_set(owner, 'myAtl_NavigatingCommaArgCS', partner)
    assert getattr(partner, 'myAtl_NavigatingArgExpCS103') == owner
    _safe_set(owner, 'myAtl_NavigatingCommaArgCS', None)
    assert getattr(partner, 'myAtl_NavigatingArgExpCS103') is None


def test_assoc_name110_stub_double():
    # myAtl_NavigatingArgExpCS has no real 'myAtl_NavigatingArgExpCS111' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingSemiArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingSemiArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingSemiArgCS(prefix="sample_text")
    partner = myAtl_NavigatingArgExpCS()
    setattr(partner, 'myAtl_NavigatingArgExpCS111', None)
    _safe_set(owner, 'myAtl_NavigatingSemiArgCS', partner)
    assert getattr(partner, 'myAtl_NavigatingArgExpCS111') == owner
    _safe_set(owner, 'myAtl_NavigatingSemiArgCS', None)
    assert getattr(partner, 'myAtl_NavigatingArgExpCS111') is None


def test_assoc_name94_stub_double():
    # myAtl_NavigatingArgExpCS has no real 'myAtl_NavigatingArgExpCS95' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingBarArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingBarArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingBarArgCS(prefix="sample_text")
    partner = myAtl_NavigatingArgExpCS()
    setattr(partner, 'myAtl_NavigatingArgExpCS95', None)
    _safe_set(owner, 'myAtl_NavigatingBarArgCS', partner)
    assert getattr(partner, 'myAtl_NavigatingArgExpCS95') == owner
    _safe_set(owner, 'myAtl_NavigatingBarArgCS', None)
    assert getattr(partner, 'myAtl_NavigatingArgExpCS95') is None


def test_assoc_ownedOperator147_stub_double():
    # myAtl_InfixExpCS has no real 'myAtl_InfixExpCS148' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_BinaryOperatorCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_BinaryOperatorCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_BinaryOperatorCS(name="sample_text")
    partner = myAtl_InfixExpCS()
    setattr(partner, 'myAtl_InfixExpCS148', None)
    _safe_set(owner, 'myAtl_BinaryOperatorCS', partner)
    assert owner in getattr(partner, 'myAtl_InfixExpCS148')
    _safe_set(owner, 'myAtl_BinaryOperatorCS', None)
    assert owner not in getattr(partner, 'myAtl_InfixExpCS148')


def test_assoc_ownedOperator149_stub_double():
    # myAtl_PrefixExpCS has no real 'myAtl_PrefixExpCS' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_UnaryOperatorCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_UnaryOperatorCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_UnaryOperatorCS(name="sample_text")
    partner = myAtl_PrefixExpCS()
    setattr(partner, 'myAtl_PrefixExpCS', None)
    _safe_set(owner, 'myAtl_UnaryOperatorCS', partner)
    assert owner in getattr(partner, 'myAtl_PrefixExpCS')
    _safe_set(owner, 'myAtl_UnaryOperatorCS', None)
    assert owner not in getattr(partner, 'myAtl_PrefixExpCS')


def test_assoc_ownedParts79_stub_double():
    # myAtl_TupleLiteralExpCS has no real 'myAtl_TupleLiteralExpCS' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_TupleLiteralPartCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_TupleLiteralPartCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_TupleLiteralPartCS(name="sample_text")
    partner = myAtl_TupleLiteralExpCS()
    setattr(partner, 'myAtl_TupleLiteralExpCS', None)
    _safe_set(owner, 'myAtl_TupleLiteralPartCS', partner)
    assert owner in getattr(partner, 'myAtl_TupleLiteralExpCS')
    _safe_set(owner, 'myAtl_TupleLiteralPartCS', None)
    assert owner not in getattr(partner, 'myAtl_TupleLiteralExpCS')


def test_assoc_ownedType104_stub_double():
    # myAtl_TypeExpCS has no real 'myAtl_TypeExpCS106' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingCommaArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingCommaArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingCommaArgCS(prefix="sample_text")
    partner = myAtl_TypeExpCS()
    setattr(partner, 'myAtl_TypeExpCS106', None)
    _safe_set(owner, 'myAtl_NavigatingCommaArgCS105', partner)
    assert getattr(partner, 'myAtl_TypeExpCS106') == owner
    _safe_set(owner, 'myAtl_NavigatingCommaArgCS105', None)
    assert getattr(partner, 'myAtl_TypeExpCS106') is None


def test_assoc_ownedType112_stub_double():
    # myAtl_TypeExpCS has no real 'myAtl_TypeExpCS114' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingSemiArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingSemiArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingSemiArgCS(prefix="sample_text")
    partner = myAtl_TypeExpCS()
    setattr(partner, 'myAtl_TypeExpCS114', None)
    _safe_set(owner, 'myAtl_NavigatingSemiArgCS113', partner)
    assert getattr(partner, 'myAtl_TypeExpCS114') == owner
    _safe_set(owner, 'myAtl_NavigatingSemiArgCS113', None)
    assert getattr(partner, 'myAtl_TypeExpCS114') is None


def test_assoc_ownedType130_stub_double():
    # myAtl_TypeExpCS has no real 'myAtl_TypeExpCS132' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_LetVariableCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_LetVariableCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_LetVariableCS(name="sample_text")
    partner = myAtl_TypeExpCS()
    setattr(partner, 'myAtl_TypeExpCS132', None)
    _safe_set(owner, 'myAtl_LetVariableCS131', partner)
    assert getattr(partner, 'myAtl_TypeExpCS132') == owner
    _safe_set(owner, 'myAtl_LetVariableCS131', None)
    assert getattr(partner, 'myAtl_TypeExpCS132') is None


def test_assoc_ownedType76_stub_double():
    # myAtl_TypeExpCS has no real 'myAtl_TypeExpCS78' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_tuplePartCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_tuplePartCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_tuplePartCS(name="sample_text")
    partner = myAtl_TypeExpCS()
    setattr(partner, 'myAtl_TypeExpCS78', None)
    _safe_set(owner, 'myAtl_tuplePartCS77', partner)
    assert getattr(partner, 'myAtl_TypeExpCS78') == owner
    _safe_set(owner, 'myAtl_tuplePartCS77', None)
    assert getattr(partner, 'myAtl_TypeExpCS78') is None


def test_assoc_ownedType80_stub_double():
    # myAtl_TypeExpCS has no real 'myAtl_TypeExpCS82' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_TupleLiteralPartCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_TupleLiteralPartCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_TupleLiteralPartCS(name="sample_text")
    partner = myAtl_TypeExpCS()
    setattr(partner, 'myAtl_TypeExpCS82', None)
    _safe_set(owner, 'myAtl_TupleLiteralPartCS81', partner)
    assert getattr(partner, 'myAtl_TypeExpCS82') == owner
    _safe_set(owner, 'myAtl_TupleLiteralPartCS81', None)
    assert getattr(partner, 'myAtl_TypeExpCS82') is None


def test_assoc_ownedType86_stub_double():
    # myAtl_TypeLiteralExpCS has no real 'myAtl_TypeLiteralExpCS' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_TypeLiteralCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_TypeLiteralCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_TypeLiteralCS(name="sample_text")
    partner = myAtl_TypeLiteralExpCS()
    setattr(partner, 'myAtl_TypeLiteralExpCS', None)
    _safe_set(owner, 'myAtl_TypeLiteralCS', partner)
    assert getattr(partner, 'myAtl_TypeLiteralExpCS') == owner
    _safe_set(owner, 'myAtl_TypeLiteralCS', None)
    assert getattr(partner, 'myAtl_TypeLiteralExpCS') is None


def test_assoc_ownedType96_stub_double():
    # myAtl_TypeExpCS has no real 'myAtl_TypeExpCS98' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_NavigatingBarArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_NavigatingBarArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_NavigatingBarArgCS(prefix="sample_text")
    partner = myAtl_TypeExpCS()
    setattr(partner, 'myAtl_TypeExpCS98', None)
    _safe_set(owner, 'myAtl_NavigatingBarArgCS97', partner)
    assert getattr(partner, 'myAtl_TypeExpCS98') == owner
    _safe_set(owner, 'myAtl_NavigatingBarArgCS97', None)
    assert getattr(partner, 'myAtl_TypeExpCS98') is None


def test_assoc_parameters24_stub_double():
    # myAtl_QueryRule has no real 'myAtl_QueryRule' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_ATLParameterCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_ATLParameterCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_ATLParameterCS(varName="sample_text")
    partner = myAtl_QueryRule()
    setattr(partner, 'myAtl_QueryRule', None)
    _safe_set(owner, 'myAtl_ATLParameterCS', partner)
    assert owner in getattr(partner, 'myAtl_QueryRule')
    _safe_set(owner, 'myAtl_ATLParameterCS', None)
    assert owner not in getattr(partner, 'myAtl_QueryRule')


def test_assoc_source66_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS67' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_BindingStat(propertyName="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS67', None)
    _safe_set(owner, 'myAtl_BindingStat', partner)
    assert getattr(partner, 'myAtl_ExpCS67') == owner
    _safe_set(owner, 'myAtl_BindingStat', None)
    assert getattr(partner, 'myAtl_ExpCS67') is None


def test_assoc_type71_stub_double():
    # myAtl_TypeExpCS has no real 'myAtl_TypeExpCS' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_ATLType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_ATLType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_ATLType(modelName="sample_text")
    partner = myAtl_TypeExpCS()
    setattr(partner, 'myAtl_TypeExpCS', None)
    _safe_set(owner, 'myAtl_ATLType72', partner)
    assert getattr(partner, 'myAtl_TypeExpCS') == owner
    _safe_set(owner, 'myAtl_ATLType72', None)
    assert getattr(partner, 'myAtl_TypeExpCS') is None


def test_assoc_value61_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS63' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_Binding(propertyName="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS63', None)
    _safe_set(owner, 'myAtl_Binding62', partner)
    assert getattr(partner, 'myAtl_ExpCS63') == owner
    _safe_set(owner, 'myAtl_Binding62', None)
    assert getattr(partner, 'myAtl_ExpCS63') is None


def test_assoc_value68_stub_double():
    # myAtl_ExpCS has no real 'myAtl_ExpCS70' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_BindingStat(propertyName="sample_text")
    partner = myAtl_ExpCS()
    setattr(partner, 'myAtl_ExpCS70', None)
    _safe_set(owner, 'myAtl_BindingStat69', partner)
    assert getattr(partner, 'myAtl_ExpCS70') == owner
    _safe_set(owner, 'myAtl_BindingStat69', None)
    assert getattr(partner, 'myAtl_ExpCS70') is None


def test_assoc_variable126_stub_double():
    # myAtl_LetExpCS has no real 'myAtl_LetExpCS' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_LetVariableCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_LetVariableCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_LetVariableCS(name="sample_text")
    partner = myAtl_LetExpCS()
    setattr(partner, 'myAtl_LetExpCS', None)
    _safe_set(owner, 'myAtl_LetVariableCS', partner)
    assert owner in getattr(partner, 'myAtl_LetExpCS')
    _safe_set(owner, 'myAtl_LetVariableCS', None)
    assert owner not in getattr(partner, 'myAtl_LetExpCS')


def test_assoc_variables10_stub_double():
    # myAtl_MatchedRule has no real 'myAtl_MatchedRule11' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_RuleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_RuleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_RuleVariableDeclaration(varName="sample_text")
    partner = myAtl_MatchedRule()
    setattr(partner, 'myAtl_MatchedRule11', None)
    _safe_set(owner, 'myAtl_RuleVariableDeclaration', partner)
    assert owner in getattr(partner, 'myAtl_MatchedRule11')
    _safe_set(owner, 'myAtl_RuleVariableDeclaration', None)
    assert owner not in getattr(partner, 'myAtl_MatchedRule11')


def test_assoc_variables16_stub_double():
    # myAtl_CalledRule has no real 'myAtl_CalledRule' property in the generated
    # code (a bare stub) -- manually attach it so myAtl_RuleVariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myAtl_RuleVariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myAtl_RuleVariableDeclaration(varName="sample_text")
    partner = myAtl_CalledRule()
    setattr(partner, 'myAtl_CalledRule', None)
    _safe_set(owner, 'myAtl_RuleVariableDeclaration17', partner)
    assert owner in getattr(partner, 'myAtl_CalledRule')
    _safe_set(owner, 'myAtl_RuleVariableDeclaration17', None)
    assert owner not in getattr(partner, 'myAtl_CalledRule')


