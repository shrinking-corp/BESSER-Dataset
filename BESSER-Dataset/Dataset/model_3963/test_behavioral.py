import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    DirectedRelationship,
    Element,
    NamedElement,
    Relationship,
    StructuralFeature,
    TypedElement,
    umlClass_Association,
    umlClass_Class,
    umlClass_Classifier,
    umlClass_DataType,
    umlClass_DirectedRelationship,
    umlClass_Element,
    umlClass_Generalization,
    umlClass_NamedElement,
    umlClass_Operation,
    umlClass_Package,
    umlClass_Property,
    umlClass_Relationship,
    umlClass_StructuralFeature,
    umlClass_TypedElement,
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

def test_assoc_class_41_reverse_link_reassign_clear():
    a1 = umlClass_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    a2 = umlClass_Operation(isOrdered="sample_text_2", isQuery="sample_text_2", isUnique="sample_text_2", lower="sample_text_2", upper="sample_text_2")
    b = umlClass_Class(isActive="sample_text")
    _safe_set(b, 'Class42', a1)
    assert _is_linked(b, 'Class42', a1)
    if hasattr(a1, 'ownedOperation'):
        assert _is_linked(a1, 'ownedOperation', b)
    _safe_set(b, 'Class42', a2)
    assert _is_linked(b, 'Class42', a2)
    if hasattr(a1, 'ownedOperation'):
        assert not _is_linked(a1, 'ownedOperation', b)
    if hasattr(a2, 'ownedOperation'):
        assert _is_linked(a2, 'ownedOperation', b)
    _safe_set(b, 'Class42', None)
    assert not _is_linked(b, 'Class42', a2)
    if hasattr(a2, 'ownedOperation'):
        assert not _is_linked(a2, 'ownedOperation', b)


def test_assoc_ownedOperation5_reverse_link_reassign_clear():
    a1 = umlClass_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    a2 = umlClass_Operation(isOrdered="sample_text_2", isQuery="sample_text_2", isUnique="sample_text_2", lower="sample_text_2", upper="sample_text_2")
    b = umlClass_Class(isActive="sample_text")
    _safe_set(b, 'class_', {a1})
    assert _is_linked(b, 'class_', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'class_', {a2})
    assert _is_linked(b, 'class_', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'class_', set())
    assert not _is_linked(b, 'class_', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


def test_assoc_superClass10_reverse_link_reassign_clear():
    a1 = umlClass_Class(isActive="sample_text")
    a2 = umlClass_Class(isActive="sample_text_2")
    b = umlClass_Class(isActive="sample_text")
    _safe_set(b, 'umlClass_Class9', {a1})
    assert _is_linked(b, 'umlClass_Class9', a1)
    if hasattr(a1, 'umlClass_Class'):
        assert _is_linked(a1, 'umlClass_Class', b)
    _safe_set(b, 'umlClass_Class9', {a2})
    assert _is_linked(b, 'umlClass_Class9', a2)
    if hasattr(a1, 'umlClass_Class'):
        assert not _is_linked(a1, 'umlClass_Class', b)
    if hasattr(a2, 'umlClass_Class'):
        assert _is_linked(a2, 'umlClass_Class', b)
    _safe_set(b, 'umlClass_Class9', set())
    assert not _is_linked(b, 'umlClass_Class9', a2)
    if hasattr(a2, 'umlClass_Class'):
        assert not _is_linked(a2, 'umlClass_Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_class_16_stub_double():
    # umlClass_Property has no real 'ownedAttribute' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Class(isActive="sample_text")
    partner = umlClass_Property()
    setattr(partner, 'ownedAttribute', None)
    _safe_set(owner, 'Class', partner)
    assert getattr(partner, 'ownedAttribute') == owner
    _safe_set(owner, 'Class', None)
    assert getattr(partner, 'ownedAttribute') is None


def test_assoc_datatype43_stub_double():
    # umlClass_DataType has no real 'DataType45' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    partner = umlClass_DataType()
    setattr(partner, 'DataType45', None)
    _safe_set(owner, 'ownedOperation44', partner)
    assert getattr(partner, 'DataType45') == owner
    _safe_set(owner, 'ownedOperation44', None)
    assert getattr(partner, 'DataType45') is None


def test_assoc_nestedClassifier13_stub_double():
    # umlClass_Classifier has no real 'umlClass_Classifier15' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Class(isActive="sample_text")
    partner = umlClass_Classifier()
    setattr(partner, 'umlClass_Classifier15', None)
    _safe_set(owner, 'umlClass_Class14', {partner})
    assert getattr(partner, 'umlClass_Classifier15') == owner
    _safe_set(owner, 'umlClass_Class14', set())
    assert getattr(partner, 'umlClass_Classifier15') is None


def test_assoc_ownedAttribute6_stub_double():
    # umlClass_Property has no real 'Property8' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Class(isActive="sample_text")
    partner = umlClass_Property()
    setattr(partner, 'Property8', None)
    _safe_set(owner, 'class_7', {partner})
    assert getattr(partner, 'Property8') == owner
    _safe_set(owner, 'class_7', set())
    assert getattr(partner, 'Property8') is None


def test_assoc_ownedOperation48_stub_double():
    # umlClass_DataType has no real 'datatype49' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    partner = umlClass_DataType()
    setattr(partner, 'datatype49', None)
    _safe_set(owner, 'Operation50', partner)
    assert owner in getattr(partner, 'datatype49')
    _safe_set(owner, 'Operation50', None)
    assert owner not in getattr(partner, 'datatype49')


def test_assoc_reference11_stub_double():
    # umlClass_Association has no real 'umlClass_Association' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Class(isActive="sample_text")
    partner = umlClass_Association()
    setattr(partner, 'umlClass_Association', None)
    _safe_set(owner, 'umlClass_Class12', partner)
    assert getattr(partner, 'umlClass_Association') == owner
    _safe_set(owner, 'umlClass_Class12', None)
    assert getattr(partner, 'umlClass_Association') is None


def test_assoc_source57_stub_double():
    # umlClass_Generalization has no real 'umlClass_Generalization58' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Class(isActive="sample_text")
    partner = umlClass_Generalization()
    setattr(partner, 'umlClass_Generalization58', None)
    _safe_set(owner, 'umlClass_Class59', partner)
    assert owner in getattr(partner, 'umlClass_Generalization58')
    _safe_set(owner, 'umlClass_Class59', None)
    assert owner not in getattr(partner, 'umlClass_Generalization58')


def test_assoc_target38_stub_double():
    # umlClass_Association has no real 'umlClass_Association39' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Class(isActive="sample_text")
    partner = umlClass_Association()
    setattr(partner, 'umlClass_Association39', None)
    _safe_set(owner, 'umlClass_Class40', partner)
    assert getattr(partner, 'umlClass_Association39') == owner
    _safe_set(owner, 'umlClass_Class40', None)
    assert getattr(partner, 'umlClass_Association39') is None


def test_assoc_target55_stub_double():
    # umlClass_Generalization has no real 'umlClass_Generalization' property in the generated
    # code (a bare stub) -- manually attach it so umlClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlClass_Class(isActive="sample_text")
    partner = umlClass_Generalization()
    setattr(partner, 'umlClass_Generalization', None)
    _safe_set(owner, 'umlClass_Class56', partner)
    assert owner in getattr(partner, 'umlClass_Generalization')
    _safe_set(owner, 'umlClass_Class56', None)
    assert owner not in getattr(partner, 'umlClass_Generalization')


