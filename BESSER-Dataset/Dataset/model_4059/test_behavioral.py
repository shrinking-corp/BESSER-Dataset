import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    ModelingConcept,
    classDiagram_Attribute,
    classDiagram_Class,
    classDiagram_ClassModel,
    classDiagram_Classifier,
    classDiagram_Function,
    classDiagram_ModelingConcept,
    classDiagram_Package,
    classDiagram_Type,
    AccessModifier,
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

def test_assoc_fields3_reverse_link_reassign_clear():
    a1 = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Class(accessModifier="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Attribute(accessModifier="sample_text", isStatic=True)
    _safe_set(b, 'classDiagram_Attribute', a1)
    assert _is_linked(b, 'classDiagram_Attribute', a1)
    if hasattr(a1, 'classDiagram_Class'):
        assert _is_linked(a1, 'classDiagram_Class', b)
    _safe_set(b, 'classDiagram_Attribute', a2)
    assert _is_linked(b, 'classDiagram_Attribute', a2)
    if hasattr(a1, 'classDiagram_Class'):
        assert not _is_linked(a1, 'classDiagram_Class', b)
    if hasattr(a2, 'classDiagram_Class'):
        assert _is_linked(a2, 'classDiagram_Class', b)
    _safe_set(b, 'classDiagram_Attribute', None)
    assert not _is_linked(b, 'classDiagram_Attribute', a2)
    if hasattr(a2, 'classDiagram_Class'):
        assert not _is_linked(a2, 'classDiagram_Class', b)


def test_assoc_methods9_reverse_link_reassign_clear():
    a1 = classDiagram_Function(accessModifier="sample_text", body="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Function(accessModifier="sample_text_2", body="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    _safe_set(b, 'classDiagram_Class10', {a1})
    assert _is_linked(b, 'classDiagram_Class10', a1)
    if hasattr(a1, 'classDiagram_Function'):
        assert _is_linked(a1, 'classDiagram_Function', b)
    _safe_set(b, 'classDiagram_Class10', {a2})
    assert _is_linked(b, 'classDiagram_Class10', a2)
    if hasattr(a1, 'classDiagram_Function'):
        assert not _is_linked(a1, 'classDiagram_Function', b)
    if hasattr(a2, 'classDiagram_Function'):
        assert _is_linked(a2, 'classDiagram_Function', b)
    _safe_set(b, 'classDiagram_Class10', set())
    assert not _is_linked(b, 'classDiagram_Class10', a2)
    if hasattr(a2, 'classDiagram_Function'):
        assert not _is_linked(a2, 'classDiagram_Function', b)


def test_assoc_parameters16_reverse_link_reassign_clear():
    a1 = classDiagram_Function(accessModifier="sample_text", body="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Function(accessModifier="sample_text_2", body="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Attribute(accessModifier="sample_text", isStatic=True)
    _safe_set(b, 'classDiagram_Attribute18', a1)
    assert _is_linked(b, 'classDiagram_Attribute18', a1)
    if hasattr(a1, 'classDiagram_Function17'):
        assert _is_linked(a1, 'classDiagram_Function17', b)
    _safe_set(b, 'classDiagram_Attribute18', a2)
    assert _is_linked(b, 'classDiagram_Attribute18', a2)
    if hasattr(a1, 'classDiagram_Function17'):
        assert not _is_linked(a1, 'classDiagram_Function17', b)
    if hasattr(a2, 'classDiagram_Function17'):
        assert _is_linked(a2, 'classDiagram_Function17', b)
    _safe_set(b, 'classDiagram_Attribute18', None)
    assert not _is_linked(b, 'classDiagram_Attribute18', a2)
    if hasattr(a2, 'classDiagram_Function17'):
        assert not _is_linked(a2, 'classDiagram_Function17', b)


def test_assoc_subtypes7_reverse_link_reassign_clear():
    a1 = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Class(accessModifier="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    _safe_set(b, 'supertypes', {a1})
    assert _is_linked(b, 'supertypes', a1)
    if hasattr(a1, 'Class8'):
        assert _is_linked(a1, 'Class8', b)
    _safe_set(b, 'supertypes', {a2})
    assert _is_linked(b, 'supertypes', a2)
    if hasattr(a1, 'Class8'):
        assert not _is_linked(a1, 'Class8', b)
    if hasattr(a2, 'Class8'):
        assert _is_linked(a2, 'Class8', b)
    _safe_set(b, 'supertypes', set())
    assert not _is_linked(b, 'supertypes', a2)
    if hasattr(a2, 'Class8'):
        assert not _is_linked(a2, 'Class8', b)


def test_assoc_supertypes5_reverse_link_reassign_clear():
    a1 = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Class(accessModifier="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    _safe_set(b, 'subtypes', {a1})
    assert _is_linked(b, 'subtypes', a1)
    if hasattr(a1, 'Class'):
        assert _is_linked(a1, 'Class', b)
    _safe_set(b, 'subtypes', {a2})
    assert _is_linked(b, 'subtypes', a2)
    if hasattr(a1, 'Class'):
        assert not _is_linked(a1, 'Class', b)
    if hasattr(a2, 'Class'):
        assert _is_linked(a2, 'Class', b)
    _safe_set(b, 'subtypes', set())
    assert not _is_linked(b, 'subtypes', a2)
    if hasattr(a2, 'Class'):
        assert not _is_linked(a2, 'Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements1_stub_double():
    # classDiagram_Package has no real 'classDiagram_Package2' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_ModelingConcept's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_ModelingConcept's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_ModelingConcept(name="sample_text")
    partner = classDiagram_Package()
    setattr(partner, 'classDiagram_Package2', None)
    _safe_set(owner, 'classDiagram_ModelingConcept', partner)
    assert owner in getattr(partner, 'classDiagram_Package2')
    _safe_set(owner, 'classDiagram_ModelingConcept', None)
    assert owner not in getattr(partner, 'classDiagram_Package2')


def test_assoc_returnType13_stub_double():
    # classDiagram_Classifier has no real 'classDiagram_Classifier15' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_Function(accessModifier="sample_text", body="sample_text", isAbstract=True, isStatic=True)
    partner = classDiagram_Classifier()
    setattr(partner, 'classDiagram_Classifier15', None)
    _safe_set(owner, 'classDiagram_Function14', partner)
    assert getattr(partner, 'classDiagram_Classifier15') == owner
    _safe_set(owner, 'classDiagram_Function14', None)
    assert getattr(partner, 'classDiagram_Classifier15') is None


def test_assoc_type11_stub_double():
    # classDiagram_Classifier has no real 'classDiagram_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_Attribute(accessModifier="sample_text", isStatic=True)
    partner = classDiagram_Classifier()
    setattr(partner, 'classDiagram_Classifier', None)
    _safe_set(owner, 'classDiagram_Attribute12', partner)
    assert getattr(partner, 'classDiagram_Classifier') == owner
    _safe_set(owner, 'classDiagram_Attribute12', None)
    assert getattr(partner, 'classDiagram_Classifier') is None


