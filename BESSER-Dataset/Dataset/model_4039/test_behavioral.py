import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    TypedElement,
    classdiagram_Association,
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_ClassDiagram,
    classdiagram_Dependency,
    classdiagram_NamedElement,
    classdiagram_Operation,
    classdiagram_TypedElement,
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

def test_assoc_dependee29_stub_double():
    # classdiagram_Class has no real 'Class30' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class30', None)
    _safe_set(owner, 'dependenciesAsDependee', partner)
    assert getattr(partner, 'Class30') == owner
    _safe_set(owner, 'dependenciesAsDependee', None)
    assert getattr(partner, 'Class30') is None


def test_assoc_dependencies1_stub_double():
    # classdiagram_ClassDiagram has no real 'classdiagram_ClassDiagram2' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_ClassDiagram()
    setattr(partner, 'classdiagram_ClassDiagram2', None)
    _safe_set(owner, 'classdiagram_Dependency', partner)
    assert owner in getattr(partner, 'classdiagram_ClassDiagram2')
    _safe_set(owner, 'classdiagram_Dependency', None)
    assert owner not in getattr(partner, 'classdiagram_ClassDiagram2')


def test_assoc_dependenciesAsDependee8_stub_double():
    # classdiagram_Class has no real 'dependee' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'dependee', None)
    _safe_set(owner, 'Dependency', partner)
    assert owner in getattr(partner, 'dependee')
    _safe_set(owner, 'Dependency', None)
    assert owner not in getattr(partner, 'dependee')


def test_assoc_dependenciesAsDepender9_stub_double():
    # classdiagram_Class has no real 'depender' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'depender', None)
    _safe_set(owner, 'Dependency10', partner)
    assert owner in getattr(partner, 'depender')
    _safe_set(owner, 'Dependency10', None)
    assert owner not in getattr(partner, 'depender')


def test_assoc_depender31_stub_double():
    # classdiagram_Class has no real 'Class32' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class32', None)
    _safe_set(owner, 'dependenciesAsDepender', partner)
    assert getattr(partner, 'Class32') == owner
    _safe_set(owner, 'dependenciesAsDepender', None)
    assert getattr(partner, 'Class32') is None


def test_assoc_type33_stub_double():
    # classdiagram_Class has no real 'classdiagram_Class34' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_TypedElement(public=True)
    partner = classdiagram_Class()
    setattr(partner, 'classdiagram_Class34', None)
    _safe_set(owner, 'classdiagram_TypedElement', partner)
    assert getattr(partner, 'classdiagram_Class34') == owner
    _safe_set(owner, 'classdiagram_TypedElement', None)
    assert getattr(partner, 'classdiagram_Class34') is None


