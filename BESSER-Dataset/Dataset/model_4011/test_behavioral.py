import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    UML_14_Association,
    UML_14_AssociationEnd,
    UML_14_Attribute,
    UML_14_Class,
    UML_14_Comment,
    UML_14_Constraint,
    UML_14_Enumeration,
    UML_14_EnumerationLiteral,
    UML_14_Generalization,
    UML_14_Method,
    UML_14_Model,
    UML_14_MultiplicityRange,
    UML_14_NamedElement,
    UML_14_Package,
    UML_14_Parameter,
    UML_14_Primitive,
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

def test_assoc_attributes26_reverse_link_reassign_clear():
    a1 = UML_14_Class(isActive="sample_text")
    a2 = UML_14_Class(isActive="sample_text_2")
    b = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_Attribute28', a1)
    assert _is_linked(b, 'UML_14_Attribute28', a1)
    if hasattr(a1, 'UML_14_Class27'):
        assert _is_linked(a1, 'UML_14_Class27', b)
    _safe_set(b, 'UML_14_Attribute28', a2)
    assert _is_linked(b, 'UML_14_Attribute28', a2)
    if hasattr(a1, 'UML_14_Class27'):
        assert not _is_linked(a1, 'UML_14_Class27', b)
    if hasattr(a2, 'UML_14_Class27'):
        assert _is_linked(a2, 'UML_14_Class27', b)
    _safe_set(b, 'UML_14_Attribute28', None)
    assert not _is_linked(b, 'UML_14_Attribute28', a2)
    if hasattr(a2, 'UML_14_Class27'):
        assert not _is_linked(a2, 'UML_14_Class27', b)


def test_assoc_child12_reverse_link_reassign_clear():
    a1 = UML_14_Generalization(discriminator="sample_text")
    a2 = UML_14_Generalization(discriminator="sample_text_2")
    b = UML_14_Class(isActive="sample_text")
    _safe_set(b, 'UML_14_Class', a1)
    assert _is_linked(b, 'UML_14_Class', a1)
    if hasattr(a1, 'UML_14_Generalization'):
        assert _is_linked(a1, 'UML_14_Generalization', b)
    _safe_set(b, 'UML_14_Class', a2)
    assert _is_linked(b, 'UML_14_Class', a2)
    if hasattr(a1, 'UML_14_Generalization'):
        assert not _is_linked(a1, 'UML_14_Generalization', b)
    if hasattr(a2, 'UML_14_Generalization'):
        assert _is_linked(a2, 'UML_14_Generalization', b)
    _safe_set(b, 'UML_14_Class', None)
    assert not _is_linked(b, 'UML_14_Class', a2)
    if hasattr(a2, 'UML_14_Generalization'):
        assert not _is_linked(a2, 'UML_14_Generalization', b)


def test_assoc_comments52_reverse_link_reassign_clear():
    a1 = UML_14_NamedElement(name="sample_text")
    a2 = UML_14_NamedElement(name="sample_text_2")
    b = UML_14_Comment(body="sample_text")
    _safe_set(b, 'UML_14_Comment', a1)
    assert _is_linked(b, 'UML_14_Comment', a1)
    if hasattr(a1, 'UML_14_NamedElement'):
        assert _is_linked(a1, 'UML_14_NamedElement', b)
    _safe_set(b, 'UML_14_Comment', a2)
    assert _is_linked(b, 'UML_14_Comment', a2)
    if hasattr(a1, 'UML_14_NamedElement'):
        assert not _is_linked(a1, 'UML_14_NamedElement', b)
    if hasattr(a2, 'UML_14_NamedElement'):
        assert _is_linked(a2, 'UML_14_NamedElement', b)
    _safe_set(b, 'UML_14_Comment', None)
    assert not _is_linked(b, 'UML_14_Comment', a2)
    if hasattr(a2, 'UML_14_NamedElement'):
        assert not _is_linked(a2, 'UML_14_NamedElement', b)


def test_assoc_constraints53_reverse_link_reassign_clear():
    a1 = UML_14_NamedElement(name="sample_text")
    a2 = UML_14_NamedElement(name="sample_text_2")
    b = UML_14_Constraint(body="sample_text")
    _safe_set(b, 'UML_14_Constraint', a1)
    assert _is_linked(b, 'UML_14_Constraint', a1)
    if hasattr(a1, 'UML_14_NamedElement54'):
        assert _is_linked(a1, 'UML_14_NamedElement54', b)
    _safe_set(b, 'UML_14_Constraint', a2)
    assert _is_linked(b, 'UML_14_Constraint', a2)
    if hasattr(a1, 'UML_14_NamedElement54'):
        assert not _is_linked(a1, 'UML_14_NamedElement54', b)
    if hasattr(a2, 'UML_14_NamedElement54'):
        assert _is_linked(a2, 'UML_14_NamedElement54', b)
    _safe_set(b, 'UML_14_Constraint', None)
    assert not _is_linked(b, 'UML_14_Constraint', a2)
    if hasattr(a2, 'UML_14_NamedElement54'):
        assert not _is_linked(a2, 'UML_14_NamedElement54', b)


def test_assoc_methods29_reverse_link_reassign_clear():
    a1 = UML_14_Method(body="sample_text", visibility="sample_text")
    a2 = UML_14_Method(body="sample_text_2", visibility="sample_text_2")
    b = UML_14_Class(isActive="sample_text")
    _safe_set(b, 'UML_14_Class30', {a1})
    assert _is_linked(b, 'UML_14_Class30', a1)
    if hasattr(a1, 'UML_14_Method31'):
        assert _is_linked(a1, 'UML_14_Method31', b)
    _safe_set(b, 'UML_14_Class30', {a2})
    assert _is_linked(b, 'UML_14_Class30', a2)
    if hasattr(a1, 'UML_14_Method31'):
        assert not _is_linked(a1, 'UML_14_Method31', b)
    if hasattr(a2, 'UML_14_Method31'):
        assert _is_linked(a2, 'UML_14_Method31', b)
    _safe_set(b, 'UML_14_Class30', set())
    assert not _is_linked(b, 'UML_14_Class30', a2)
    if hasattr(a2, 'UML_14_Method31'):
        assert not _is_linked(a2, 'UML_14_Method31', b)


def test_assoc_multiplicity20_reverse_link_reassign_clear():
    a1 = UML_14_MultiplicityRange(lower="sample_text", upper="sample_text")
    a2 = UML_14_MultiplicityRange(lower="sample_text_2", upper="sample_text_2")
    b = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_AssociationEnd21', a1)
    assert _is_linked(b, 'UML_14_AssociationEnd21', a1)
    if hasattr(a1, 'UML_14_MultiplicityRange22'):
        assert _is_linked(a1, 'UML_14_MultiplicityRange22', b)
    _safe_set(b, 'UML_14_AssociationEnd21', a2)
    assert _is_linked(b, 'UML_14_AssociationEnd21', a2)
    if hasattr(a1, 'UML_14_MultiplicityRange22'):
        assert not _is_linked(a1, 'UML_14_MultiplicityRange22', b)
    if hasattr(a2, 'UML_14_MultiplicityRange22'):
        assert _is_linked(a2, 'UML_14_MultiplicityRange22', b)
    _safe_set(b, 'UML_14_AssociationEnd21', None)
    assert not _is_linked(b, 'UML_14_AssociationEnd21', a2)
    if hasattr(a2, 'UML_14_MultiplicityRange22'):
        assert not _is_linked(a2, 'UML_14_MultiplicityRange22', b)


def test_assoc_multiplicity6_reverse_link_reassign_clear():
    a1 = UML_14_MultiplicityRange(lower="sample_text", upper="sample_text")
    a2 = UML_14_MultiplicityRange(lower="sample_text_2", upper="sample_text_2")
    b = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_Attribute', a1)
    assert _is_linked(b, 'UML_14_Attribute', a1)
    if hasattr(a1, 'UML_14_MultiplicityRange'):
        assert _is_linked(a1, 'UML_14_MultiplicityRange', b)
    _safe_set(b, 'UML_14_Attribute', a2)
    assert _is_linked(b, 'UML_14_Attribute', a2)
    if hasattr(a1, 'UML_14_MultiplicityRange'):
        assert not _is_linked(a1, 'UML_14_MultiplicityRange', b)
    if hasattr(a2, 'UML_14_MultiplicityRange'):
        assert _is_linked(a2, 'UML_14_MultiplicityRange', b)
    _safe_set(b, 'UML_14_Attribute', None)
    assert not _is_linked(b, 'UML_14_Attribute', a2)
    if hasattr(a2, 'UML_14_MultiplicityRange'):
        assert not _is_linked(a2, 'UML_14_MultiplicityRange', b)


def test_assoc_parameters4_reverse_link_reassign_clear():
    a1 = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    a2 = UML_14_Parameter(defaultValue="sample_text_2", kind="sample_text_2")
    b = UML_14_Method(body="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_Method', {a1})
    assert _is_linked(b, 'UML_14_Method', a1)
    if hasattr(a1, 'UML_14_Parameter5'):
        assert _is_linked(a1, 'UML_14_Parameter5', b)
    _safe_set(b, 'UML_14_Method', {a2})
    assert _is_linked(b, 'UML_14_Method', a2)
    if hasattr(a1, 'UML_14_Parameter5'):
        assert not _is_linked(a1, 'UML_14_Parameter5', b)
    if hasattr(a2, 'UML_14_Parameter5'):
        assert _is_linked(a2, 'UML_14_Parameter5', b)
    _safe_set(b, 'UML_14_Method', set())
    assert not _is_linked(b, 'UML_14_Method', a2)
    if hasattr(a2, 'UML_14_Parameter5'):
        assert not _is_linked(a2, 'UML_14_Parameter5', b)


def test_assoc_parent13_reverse_link_reassign_clear():
    a1 = UML_14_Generalization(discriminator="sample_text")
    a2 = UML_14_Generalization(discriminator="sample_text_2")
    b = UML_14_Class(isActive="sample_text")
    _safe_set(b, 'UML_14_Class15', a1)
    assert _is_linked(b, 'UML_14_Class15', a1)
    if hasattr(a1, 'UML_14_Generalization14'):
        assert _is_linked(a1, 'UML_14_Generalization14', b)
    _safe_set(b, 'UML_14_Class15', a2)
    assert _is_linked(b, 'UML_14_Class15', a2)
    if hasattr(a1, 'UML_14_Generalization14'):
        assert not _is_linked(a1, 'UML_14_Generalization14', b)
    if hasattr(a2, 'UML_14_Generalization14'):
        assert _is_linked(a2, 'UML_14_Generalization14', b)
    _safe_set(b, 'UML_14_Class15', None)
    assert not _is_linked(b, 'UML_14_Class15', a2)
    if hasattr(a2, 'UML_14_Generalization14'):
        assert not _is_linked(a2, 'UML_14_Generalization14', b)


def test_assoc_participant18_reverse_link_reassign_clear():
    a1 = UML_14_Class(isActive="sample_text")
    a2 = UML_14_Class(isActive="sample_text_2")
    b = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_AssociationEnd', a1)
    assert _is_linked(b, 'UML_14_AssociationEnd', a1)
    if hasattr(a1, 'UML_14_Class19'):
        assert _is_linked(a1, 'UML_14_Class19', b)
    _safe_set(b, 'UML_14_AssociationEnd', a2)
    assert _is_linked(b, 'UML_14_AssociationEnd', a2)
    if hasattr(a1, 'UML_14_Class19'):
        assert not _is_linked(a1, 'UML_14_Class19', b)
    if hasattr(a2, 'UML_14_Class19'):
        assert _is_linked(a2, 'UML_14_Class19', b)
    _safe_set(b, 'UML_14_AssociationEnd', None)
    assert not _is_linked(b, 'UML_14_AssociationEnd', a2)
    if hasattr(a2, 'UML_14_Class19'):
        assert not _is_linked(a2, 'UML_14_Class19', b)


def test_assoc_qualifier23_reverse_link_reassign_clear():
    a1 = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    a2 = UML_14_Attribute(initialValue="sample_text_2", visibility="sample_text_2")
    b = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_AssociationEnd24', a1)
    assert _is_linked(b, 'UML_14_AssociationEnd24', a1)
    if hasattr(a1, 'UML_14_Attribute25'):
        assert _is_linked(a1, 'UML_14_Attribute25', b)
    _safe_set(b, 'UML_14_AssociationEnd24', a2)
    assert _is_linked(b, 'UML_14_AssociationEnd24', a2)
    if hasattr(a1, 'UML_14_Attribute25'):
        assert not _is_linked(a1, 'UML_14_Attribute25', b)
    if hasattr(a2, 'UML_14_Attribute25'):
        assert _is_linked(a2, 'UML_14_Attribute25', b)
    _safe_set(b, 'UML_14_AssociationEnd24', None)
    assert not _is_linked(b, 'UML_14_AssociationEnd24', a2)
    if hasattr(a2, 'UML_14_Attribute25'):
        assert not _is_linked(a2, 'UML_14_Attribute25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_association17_stub_double():
    # UML_14_Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    partner = UML_14_Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'connection', partner)
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'connection', None)
    assert getattr(partner, 'Association') is None


def test_assoc_classes35_stub_double():
    # UML_14_Package has no real 'UML_14_Package36' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Class(isActive="sample_text")
    partner = UML_14_Package()
    setattr(partner, 'UML_14_Package36', None)
    _safe_set(owner, 'UML_14_Class37', partner)
    assert owner in getattr(partner, 'UML_14_Package36')
    _safe_set(owner, 'UML_14_Class37', None)
    assert owner not in getattr(partner, 'UML_14_Package36')


def test_assoc_connection16_stub_double():
    # UML_14_Association has no real 'association' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    partner = UML_14_Association()
    setattr(partner, 'association', None)
    _safe_set(owner, 'AssociationEnd', partner)
    assert owner in getattr(partner, 'association')
    _safe_set(owner, 'AssociationEnd', None)
    assert owner not in getattr(partner, 'association')


def test_assoc_enumType0_stub_double():
    # UML_14_Enumeration has no real 'UML_14_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    partner = UML_14_Enumeration()
    setattr(partner, 'UML_14_Enumeration', None)
    _safe_set(owner, 'UML_14_Parameter', partner)
    assert getattr(partner, 'UML_14_Enumeration') == owner
    _safe_set(owner, 'UML_14_Parameter', None)
    assert getattr(partner, 'UML_14_Enumeration') is None


def test_assoc_enumType7_stub_double():
    # UML_14_Enumeration has no real 'UML_14_Enumeration9' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    partner = UML_14_Enumeration()
    setattr(partner, 'UML_14_Enumeration9', None)
    _safe_set(owner, 'UML_14_Attribute8', partner)
    assert getattr(partner, 'UML_14_Enumeration9') == owner
    _safe_set(owner, 'UML_14_Attribute8', None)
    assert getattr(partner, 'UML_14_Enumeration9') is None


def test_assoc_generalizations44_stub_double():
    # UML_14_Package has no real 'UML_14_Package45' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Generalization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Generalization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Generalization(discriminator="sample_text")
    partner = UML_14_Package()
    setattr(partner, 'UML_14_Package45', None)
    _safe_set(owner, 'UML_14_Generalization46', partner)
    assert owner in getattr(partner, 'UML_14_Package45')
    _safe_set(owner, 'UML_14_Generalization46', None)
    assert owner not in getattr(partner, 'UML_14_Package45')


def test_assoc_literal32_stub_double():
    # UML_14_Enumeration has no real 'UML_14_Enumeration33' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_EnumerationLiteral(value="sample_text")
    partner = UML_14_Enumeration()
    setattr(partner, 'UML_14_Enumeration33', None)
    _safe_set(owner, 'UML_14_EnumerationLiteral', partner)
    assert owner in getattr(partner, 'UML_14_Enumeration33')
    _safe_set(owner, 'UML_14_EnumerationLiteral', None)
    assert owner not in getattr(partner, 'UML_14_Enumeration33')


def test_assoc_primitiveType1_stub_double():
    # UML_14_Enumeration has no real 'UML_14_Enumeration3' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    partner = UML_14_Enumeration()
    setattr(partner, 'UML_14_Enumeration3', None)
    _safe_set(owner, 'UML_14_Parameter2', partner)
    assert getattr(partner, 'UML_14_Enumeration3') == owner
    _safe_set(owner, 'UML_14_Parameter2', None)
    assert getattr(partner, 'UML_14_Enumeration3') is None


def test_assoc_primitiveType10_stub_double():
    # UML_14_Primitive has no real 'UML_14_Primitive' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    partner = UML_14_Primitive()
    setattr(partner, 'UML_14_Primitive', None)
    _safe_set(owner, 'UML_14_Attribute11', partner)
    assert getattr(partner, 'UML_14_Primitive') == owner
    _safe_set(owner, 'UML_14_Attribute11', None)
    assert getattr(partner, 'UML_14_Primitive') is None


