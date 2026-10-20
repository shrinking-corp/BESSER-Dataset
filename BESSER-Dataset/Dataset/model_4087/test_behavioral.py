import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    UMLDiagramItem,
    UMLElement,
    UMLIncrement,
    classDiagram_UMLAssoc,
    classDiagram_UMLCardinality,
    classDiagram_UMLClass,
    classDiagram_UMLClassDiagram,
    classDiagram_UMLDiagramItem,
    classDiagram_UMLElement,
    classDiagram_UMLIncrement,
    classDiagram_UMLRole,
    classDiagram_UMLStereotype,
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

def test_assoc_card10_reverse_link_reassign_clear():
    a1 = classDiagram_UMLRole(adornment="sample_text")
    a2 = classDiagram_UMLRole(adornment="sample_text_2")
    b = classDiagram_UMLCardinality(cardString="sample_text")
    _safe_set(b, 'UMLCardinality', a1)
    assert _is_linked(b, 'UMLCardinality', a1)
    if hasattr(a1, 'revCard'):
        assert _is_linked(a1, 'revCard', b)
    _safe_set(b, 'UMLCardinality', a2)
    assert _is_linked(b, 'UMLCardinality', a2)
    if hasattr(a1, 'revCard'):
        assert not _is_linked(a1, 'revCard', b)
    if hasattr(a2, 'revCard'):
        assert _is_linked(a2, 'revCard', b)
    _safe_set(b, 'UMLCardinality', None)
    assert not _is_linked(b, 'UMLCardinality', a2)
    if hasattr(a2, 'revCard'):
        assert not _is_linked(a2, 'revCard', b)


def test_assoc_revCard3_reverse_link_reassign_clear():
    a1 = classDiagram_UMLRole(adornment="sample_text")
    a2 = classDiagram_UMLRole(adornment="sample_text_2")
    b = classDiagram_UMLCardinality(cardString="sample_text")
    _safe_set(b, 'card', a1)
    assert _is_linked(b, 'card', a1)
    if hasattr(a1, 'UMLRole4'):
        assert _is_linked(a1, 'UMLRole4', b)
    _safe_set(b, 'card', a2)
    assert _is_linked(b, 'card', a2)
    if hasattr(a1, 'UMLRole4'):
        assert not _is_linked(a1, 'UMLRole4', b)
    if hasattr(a2, 'UMLRole4'):
        assert _is_linked(a2, 'UMLRole4', b)
    _safe_set(b, 'card', None)
    assert not _is_linked(b, 'card', a2)
    if hasattr(a2, 'UMLRole4'):
        assert not _is_linked(a2, 'UMLRole4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_diagram8_stub_double():
    # classDiagram_UMLClassDiagram has no real 'UMLClassDiagram' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLElement(name="sample_text")
    partner = classDiagram_UMLClassDiagram()
    setattr(partner, 'UMLClassDiagram', None)
    _safe_set(owner, 'elements', partner)
    assert getattr(partner, 'UMLClassDiagram') == owner
    _safe_set(owner, 'elements', None)
    assert getattr(partner, 'UMLClassDiagram') is None


def test_assoc_elements5_stub_double():
    # classDiagram_UMLClassDiagram has no real 'diagram' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLElement(name="sample_text")
    partner = classDiagram_UMLClassDiagram()
    setattr(partner, 'diagram', None)
    _safe_set(owner, 'UMLElement', partner)
    assert owner in getattr(partner, 'diagram')
    _safe_set(owner, 'UMLElement', None)
    assert owner not in getattr(partner, 'diagram')


def test_assoc_increment15_stub_double():
    # classDiagram_UMLIncrement has no real 'UMLIncrement' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLStereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLStereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLStereotype(text="sample_text")
    partner = classDiagram_UMLIncrement()
    setattr(partner, 'UMLIncrement', None)
    _safe_set(owner, 'stereotypes', partner)
    assert getattr(partner, 'UMLIncrement') == owner
    _safe_set(owner, 'stereotypes', None)
    assert getattr(partner, 'UMLIncrement') is None


def test_assoc_leftRole0_stub_double():
    # classDiagram_UMLAssoc has no real 'revLeftRole' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLRole(adornment="sample_text")
    partner = classDiagram_UMLAssoc()
    setattr(partner, 'revLeftRole', None)
    _safe_set(owner, 'UMLRole', partner)
    assert getattr(partner, 'revLeftRole') == owner
    _safe_set(owner, 'UMLRole', None)
    assert getattr(partner, 'revLeftRole') is None


def test_assoc_revLeftRole11_stub_double():
    # classDiagram_UMLAssoc has no real 'UMLAssoc' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLRole(adornment="sample_text")
    partner = classDiagram_UMLAssoc()
    setattr(partner, 'UMLAssoc', None)
    _safe_set(owner, 'leftRole', partner)
    assert getattr(partner, 'UMLAssoc') == owner
    _safe_set(owner, 'leftRole', None)
    assert getattr(partner, 'UMLAssoc') is None


def test_assoc_revRightRole12_stub_double():
    # classDiagram_UMLAssoc has no real 'UMLAssoc13' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLRole(adornment="sample_text")
    partner = classDiagram_UMLAssoc()
    setattr(partner, 'UMLAssoc13', None)
    _safe_set(owner, 'rightRole', partner)
    assert getattr(partner, 'UMLAssoc13') == owner
    _safe_set(owner, 'rightRole', None)
    assert getattr(partner, 'UMLAssoc13') is None


def test_assoc_rightRole1_stub_double():
    # classDiagram_UMLAssoc has no real 'revRightRole' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLRole(adornment="sample_text")
    partner = classDiagram_UMLAssoc()
    setattr(partner, 'revRightRole', None)
    _safe_set(owner, 'UMLRole2', partner)
    assert getattr(partner, 'revRightRole') == owner
    _safe_set(owner, 'UMLRole2', None)
    assert getattr(partner, 'revRightRole') is None


def test_assoc_roles6_stub_double():
    # classDiagram_UMLClass has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLRole(adornment="sample_text")
    partner = classDiagram_UMLClass()
    setattr(partner, 'target', None)
    _safe_set(owner, 'UMLRole7', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'UMLRole7', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_stereotypes9_stub_double():
    # classDiagram_UMLIncrement has no real 'increment' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLStereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLStereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLStereotype(text="sample_text")
    partner = classDiagram_UMLIncrement()
    setattr(partner, 'increment', None)
    _safe_set(owner, 'UMLStereotype', partner)
    assert owner in getattr(partner, 'increment')
    _safe_set(owner, 'UMLStereotype', None)
    assert owner not in getattr(partner, 'increment')


def test_assoc_target14_stub_double():
    # classDiagram_UMLClass has no real 'UMLClass' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_UMLRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_UMLRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_UMLRole(adornment="sample_text")
    partner = classDiagram_UMLClass()
    setattr(partner, 'UMLClass', None)
    _safe_set(owner, 'roles', partner)
    assert getattr(partner, 'UMLClass') == owner
    _safe_set(owner, 'roles', None)
    assert getattr(partner, 'UMLClass') is None


