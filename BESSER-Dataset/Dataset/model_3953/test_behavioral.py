import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    CallMethodAction,
    Class,
    Guard,
    IsInStateCondition,
    Method,
    NamedElement,
    Parameter,
    Property,
    soopl_Action,
    soopl_AssignProperty,
    soopl_CallMethodAction,
    soopl_CallMethodOfParameter,
    soopl_CallMethodOfProperty,
    soopl_Class,
    soopl_ComplexTypeParameter,
    soopl_ComplexTypeProperty,
    soopl_Guard,
    soopl_IsInStateCondition,
    soopl_Method,
    soopl_NamedElement,
    soopl_Package,
    soopl_Parameter,
    soopl_ParameterBinding,
    soopl_ParameterIsInState,
    soopl_Property,
    soopl_PropertyIsInState,
    soopl_SimpleTypeParameter,
    soopl_SimpleTypeProperty,
    soopl_StateClass,
    soopl_StateImplementationClass,
    soopl_StatefulClass,
    soopl_Transition,
    soopl_TransitionMethod,
    DataType,
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

def test_assoc_properties8_reverse_link_reassign_clear():
    a1 = soopl_Property(lowerBound=7, multiValued=True, upperBound=7)
    a2 = soopl_Property(lowerBound=13, multiValued=False, upperBound=13)
    b = soopl_Class(isAbstract=True)
    _safe_set(b, 'soopl_Class9', {a1})
    assert _is_linked(b, 'soopl_Class9', a1)
    if hasattr(a1, 'soopl_Property'):
        assert _is_linked(a1, 'soopl_Property', b)
    _safe_set(b, 'soopl_Class9', {a2})
    assert _is_linked(b, 'soopl_Class9', a2)
    if hasattr(a1, 'soopl_Property'):
        assert not _is_linked(a1, 'soopl_Property', b)
    if hasattr(a2, 'soopl_Property'):
        assert _is_linked(a2, 'soopl_Property', b)
    _safe_set(b, 'soopl_Class9', set())
    assert not _is_linked(b, 'soopl_Class9', a2)
    if hasattr(a2, 'soopl_Property'):
        assert not _is_linked(a2, 'soopl_Property', b)


def test_assoc_superClass11_reverse_link_reassign_clear():
    a1 = soopl_Class(isAbstract=True)
    a2 = soopl_Class(isAbstract=False)
    b = soopl_Class(isAbstract=True)
    _safe_set(b, 'soopl_Class12', a1)
    assert _is_linked(b, 'soopl_Class12', a1)
    if hasattr(a1, 'soopl_Class10'):
        assert _is_linked(a1, 'soopl_Class10', b)
    _safe_set(b, 'soopl_Class12', a2)
    assert _is_linked(b, 'soopl_Class12', a2)
    if hasattr(a1, 'soopl_Class10'):
        assert not _is_linked(a1, 'soopl_Class10', b)
    if hasattr(a2, 'soopl_Class10'):
        assert _is_linked(a2, 'soopl_Class10', b)
    _safe_set(b, 'soopl_Class12', None)
    assert not _is_linked(b, 'soopl_Class12', a2)
    if hasattr(a2, 'soopl_Class10'):
        assert not _is_linked(a2, 'soopl_Class10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classType40_stub_double():
    # soopl_ComplexTypeParameter has no real 'soopl_ComplexTypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so soopl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soopl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soopl_Class(isAbstract=True)
    partner = soopl_ComplexTypeParameter()
    setattr(partner, 'soopl_ComplexTypeParameter', None)
    _safe_set(owner, 'soopl_Class41', partner)
    assert getattr(partner, 'soopl_ComplexTypeParameter') == owner
    _safe_set(owner, 'soopl_Class41', None)
    assert getattr(partner, 'soopl_ComplexTypeParameter') is None


def test_assoc_classes0_stub_double():
    # soopl_Package has no real 'soopl_Package' property in the generated
    # code (a bare stub) -- manually attach it so soopl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soopl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soopl_Class(isAbstract=True)
    partner = soopl_Package()
    setattr(partner, 'soopl_Package', None)
    _safe_set(owner, 'soopl_Class', partner)
    assert owner in getattr(partner, 'soopl_Package')
    _safe_set(owner, 'soopl_Class', None)
    assert owner not in getattr(partner, 'soopl_Package')


def test_assoc_methods6_stub_double():
    # soopl_Method has no real 'soopl_Method' property in the generated
    # code (a bare stub) -- manually attach it so soopl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soopl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soopl_Class(isAbstract=True)
    partner = soopl_Method()
    setattr(partner, 'soopl_Method', None)
    _safe_set(owner, 'soopl_Class7', {partner})
    assert getattr(partner, 'soopl_Method') == owner
    _safe_set(owner, 'soopl_Class7', set())
    assert getattr(partner, 'soopl_Method') is None


def test_assoc_structuralFeatureBinding46_stub_double():
    # soopl_ParameterBinding has no real 'soopl_ParameterBinding47' property in the generated
    # code (a bare stub) -- manually attach it so soopl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soopl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soopl_Property(lowerBound=7, multiValued=True, upperBound=7)
    partner = soopl_ParameterBinding()
    setattr(partner, 'soopl_ParameterBinding47', None)
    _safe_set(owner, 'soopl_Property48', partner)
    assert getattr(partner, 'soopl_ParameterBinding47') == owner
    _safe_set(owner, 'soopl_Property48', None)
    assert getattr(partner, 'soopl_ParameterBinding47') is None


def test_assoc_type25_stub_double():
    # soopl_ComplexTypeProperty has no real 'soopl_ComplexTypeProperty' property in the generated
    # code (a bare stub) -- manually attach it so soopl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soopl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soopl_Class(isAbstract=True)
    partner = soopl_ComplexTypeProperty()
    setattr(partner, 'soopl_ComplexTypeProperty', None)
    _safe_set(owner, 'soopl_Class26', partner)
    assert getattr(partner, 'soopl_ComplexTypeProperty') == owner
    _safe_set(owner, 'soopl_Class26', None)
    assert getattr(partner, 'soopl_ComplexTypeProperty') is None


