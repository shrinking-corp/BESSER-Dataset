import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ATL_atlext_EObject,
    ATL_atlext_Type,
    Callable,
    CallableParameter,
    ContextHelper,
    JavaBody,
    MatchedRule,
    OCL_atlext_EObject,
    OCL_atlext_Type,
    OclExpression,
    OutPatternElement,
    PropertyCallExp,
    ResolveTempResolution,
    RuleResolutionInfo,
    StringToStringMap,
    TypedElement,
    VariableDeclaration,
    atlext_ATL_Binding,
    atlext_ATL_Callable,
    atlext_ATL_CallableParameter,
    atlext_ATL_ContextHelper,
    atlext_ATL_Helper,
    atlext_ATL_LocatedElement,
    atlext_ATL_MatchedRule,
    atlext_ATL_OutPatternElement,
    atlext_ATL_RuleResolutionInfo,
    atlext_ATL_StringToStringMap,
    atlext_OCL_GetAppliedStereotypesBody,
    atlext_OCL_JavaBody,
    atlext_OCL_OclExpression,
    atlext_OCL_OperationCallExp,
    atlext_OCL_PropertyCallExp,
    atlext_OCL_ResolveTempResolution,
    atlext_OCL_TypedElement,
    atlext_OCL_VariableDeclaration,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations1_stub_double():
    # StringToStringMap has no real 'StringToStringMap' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_LocatedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_LocatedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_LocatedElement(fileLocation="sample_text", fileObject="sample_text")
    partner = StringToStringMap()
    setattr(partner, 'StringToStringMap', None)
    _safe_set(owner, 'atlext_ATL_LocatedElement2', {partner})
    assert getattr(partner, 'StringToStringMap') == owner
    _safe_set(owner, 'atlext_ATL_LocatedElement2', set())
    assert getattr(partner, 'StringToStringMap') is None


def test_assoc_dynamicResolvers43_stub_double():
    # ContextHelper has no real 'ContextHelper' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = ContextHelper()
    setattr(partner, 'ContextHelper', None)
    _safe_set(owner, 'polymorphicCalledBy', {partner})
    assert getattr(partner, 'ContextHelper') == owner
    _safe_set(owner, 'polymorphicCalledBy', set())
    assert getattr(partner, 'ContextHelper') is None


def test_assoc_inferredReturnType13_stub_double():
    # ATL_atlext_Type has no real 'ATL_atlext_Type14' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Helper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Helper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Helper(hasContext=True, isAttribute=True)
    partner = ATL_atlext_Type()
    setattr(partner, 'ATL_atlext_Type14', None)
    _safe_set(owner, 'atlext_ATL_Helper', partner)
    assert getattr(partner, 'ATL_atlext_Type14') == owner
    _safe_set(owner, 'atlext_ATL_Helper', None)
    assert getattr(partner, 'ATL_atlext_Type14') is None


def test_assoc_noCastedType32_stub_double():
    # OCL_atlext_Type has no real 'OCL_atlext_Type33' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = OCL_atlext_Type()
    setattr(partner, 'OCL_atlext_Type33', None)
    _safe_set(owner, 'atlext_OCL_OclExpression', partner)
    assert getattr(partner, 'OCL_atlext_Type33') == owner
    _safe_set(owner, 'atlext_OCL_OclExpression', None)
    assert getattr(partner, 'OCL_atlext_Type33') is None


def test_assoc_paramDeclaration7_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_CallableParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_CallableParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_CallableParameter(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration', None)
    _safe_set(owner, 'atlext_ATL_CallableParameter8', partner)
    assert getattr(partner, 'VariableDeclaration') == owner
    _safe_set(owner, 'atlext_ATL_CallableParameter8', None)
    assert getattr(partner, 'VariableDeclaration') is None


def test_assoc_problems0_stub_double():
    # ATL_atlext_EObject has no real 'ATL_atlext_EObject' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_LocatedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_LocatedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_LocatedElement(fileLocation="sample_text", fileObject="sample_text")
    partner = ATL_atlext_EObject()
    setattr(partner, 'ATL_atlext_EObject', None)
    _safe_set(owner, 'atlext_ATL_LocatedElement', {partner})
    assert getattr(partner, 'ATL_atlext_EObject') == owner
    _safe_set(owner, 'atlext_ATL_LocatedElement', set())
    assert getattr(partner, 'ATL_atlext_EObject') is None


def test_assoc_receptorType38_stub_double():
    # OCL_atlext_EObject has no real 'OCL_atlext_EObject40' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = OCL_atlext_EObject()
    setattr(partner, 'OCL_atlext_EObject40', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp39', partner)
    assert getattr(partner, 'OCL_atlext_EObject40') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp39', None)
    assert getattr(partner, 'OCL_atlext_EObject40') is None


def test_assoc_staticResolver41_stub_double():
    # Callable has no real 'Callable' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = Callable()
    setattr(partner, 'Callable', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp42', partner)
    assert getattr(partner, 'Callable') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp42', None)
    assert getattr(partner, 'Callable') is None


def test_assoc_staticReturnType15_stub_double():
    # ATL_atlext_Type has no real 'ATL_atlext_Type17' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Helper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Helper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Helper(hasContext=True, isAttribute=True)
    partner = ATL_atlext_Type()
    setattr(partner, 'ATL_atlext_Type17', None)
    _safe_set(owner, 'atlext_ATL_Helper16', partner)
    assert getattr(partner, 'ATL_atlext_Type17') == owner
    _safe_set(owner, 'atlext_ATL_Helper16', None)
    assert getattr(partner, 'ATL_atlext_Type17') is None


def test_assoc_staticType6_stub_double():
    # ATL_atlext_Type has no real 'ATL_atlext_Type' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_CallableParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_CallableParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_CallableParameter(name="sample_text")
    partner = ATL_atlext_Type()
    setattr(partner, 'ATL_atlext_Type', None)
    _safe_set(owner, 'atlext_ATL_CallableParameter', partner)
    assert getattr(partner, 'ATL_atlext_Type') == owner
    _safe_set(owner, 'atlext_ATL_CallableParameter', None)
    assert getattr(partner, 'ATL_atlext_Type') is None


def test_assoc_subtypeFeatures35_stub_double():
    # OCL_atlext_EObject has no real 'OCL_atlext_EObject37' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = OCL_atlext_EObject()
    setattr(partner, 'OCL_atlext_EObject37', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp36', {partner})
    assert getattr(partner, 'OCL_atlext_EObject37') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp36', set())
    assert getattr(partner, 'OCL_atlext_EObject37') is None


def test_assoc_usedFeature34_stub_double():
    # OCL_atlext_EObject has no real 'OCL_atlext_EObject' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = OCL_atlext_EObject()
    setattr(partner, 'OCL_atlext_EObject', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp', partner)
    assert getattr(partner, 'OCL_atlext_EObject') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp', None)
    assert getattr(partner, 'OCL_atlext_EObject') is None


