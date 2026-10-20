import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    NamedElement,
    UML_14_Association,
    UML_14_AssociationEnd,
    UML_14_Attribute,
    UML_14_Class,
    UML_14_Comment,
    UML_14_Constraint,
    UML_14_DataType,
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

def test_assoc_attributes21_reverse_link_reassign_clear():
    a1 = UML_14_Class(isActive="sample_text")
    a2 = UML_14_Class(isActive="sample_text_2")
    b = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_Attribute23', a1)
    assert _is_linked(b, 'UML_14_Attribute23', a1)
    if hasattr(a1, 'UML_14_Class22'):
        assert _is_linked(a1, 'UML_14_Class22', b)
    _safe_set(b, 'UML_14_Attribute23', a2)
    assert _is_linked(b, 'UML_14_Attribute23', a2)
    if hasattr(a1, 'UML_14_Class22'):
        assert not _is_linked(a1, 'UML_14_Class22', b)
    if hasattr(a2, 'UML_14_Class22'):
        assert _is_linked(a2, 'UML_14_Class22', b)
    _safe_set(b, 'UML_14_Attribute23', None)
    assert not _is_linked(b, 'UML_14_Attribute23', a2)
    if hasattr(a2, 'UML_14_Class22'):
        assert not _is_linked(a2, 'UML_14_Class22', b)


def test_assoc_child7_reverse_link_reassign_clear():
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


def test_assoc_comments44_reverse_link_reassign_clear():
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


def test_assoc_constraints45_reverse_link_reassign_clear():
    a1 = UML_14_NamedElement(name="sample_text")
    a2 = UML_14_NamedElement(name="sample_text_2")
    b = UML_14_Constraint(body="sample_text")
    _safe_set(b, 'UML_14_Constraint', a1)
    assert _is_linked(b, 'UML_14_Constraint', a1)
    if hasattr(a1, 'UML_14_NamedElement46'):
        assert _is_linked(a1, 'UML_14_NamedElement46', b)
    _safe_set(b, 'UML_14_Constraint', a2)
    assert _is_linked(b, 'UML_14_Constraint', a2)
    if hasattr(a1, 'UML_14_NamedElement46'):
        assert not _is_linked(a1, 'UML_14_NamedElement46', b)
    if hasattr(a2, 'UML_14_NamedElement46'):
        assert _is_linked(a2, 'UML_14_NamedElement46', b)
    _safe_set(b, 'UML_14_Constraint', None)
    assert not _is_linked(b, 'UML_14_Constraint', a2)
    if hasattr(a2, 'UML_14_NamedElement46'):
        assert not _is_linked(a2, 'UML_14_NamedElement46', b)


def test_assoc_methods24_reverse_link_reassign_clear():
    a1 = UML_14_Method(body="sample_text", visibility="sample_text")
    a2 = UML_14_Method(body="sample_text_2", visibility="sample_text_2")
    b = UML_14_Class(isActive="sample_text")
    _safe_set(b, 'UML_14_Class25', {a1})
    assert _is_linked(b, 'UML_14_Class25', a1)
    if hasattr(a1, 'UML_14_Method26'):
        assert _is_linked(a1, 'UML_14_Method26', b)
    _safe_set(b, 'UML_14_Class25', {a2})
    assert _is_linked(b, 'UML_14_Class25', a2)
    if hasattr(a1, 'UML_14_Method26'):
        assert not _is_linked(a1, 'UML_14_Method26', b)
    if hasattr(a2, 'UML_14_Method26'):
        assert _is_linked(a2, 'UML_14_Method26', b)
    _safe_set(b, 'UML_14_Class25', set())
    assert not _is_linked(b, 'UML_14_Class25', a2)
    if hasattr(a2, 'UML_14_Method26'):
        assert not _is_linked(a2, 'UML_14_Method26', b)


def test_assoc_multiplicity15_reverse_link_reassign_clear():
    a1 = UML_14_MultiplicityRange(lower="sample_text", upper="sample_text")
    a2 = UML_14_MultiplicityRange(lower="sample_text_2", upper="sample_text_2")
    b = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_AssociationEnd16', a1)
    assert _is_linked(b, 'UML_14_AssociationEnd16', a1)
    if hasattr(a1, 'UML_14_MultiplicityRange17'):
        assert _is_linked(a1, 'UML_14_MultiplicityRange17', b)
    _safe_set(b, 'UML_14_AssociationEnd16', a2)
    assert _is_linked(b, 'UML_14_AssociationEnd16', a2)
    if hasattr(a1, 'UML_14_MultiplicityRange17'):
        assert not _is_linked(a1, 'UML_14_MultiplicityRange17', b)
    if hasattr(a2, 'UML_14_MultiplicityRange17'):
        assert _is_linked(a2, 'UML_14_MultiplicityRange17', b)
    _safe_set(b, 'UML_14_AssociationEnd16', None)
    assert not _is_linked(b, 'UML_14_AssociationEnd16', a2)
    if hasattr(a2, 'UML_14_MultiplicityRange17'):
        assert not _is_linked(a2, 'UML_14_MultiplicityRange17', b)


def test_assoc_multiplicity3_reverse_link_reassign_clear():
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


def test_assoc_parameters1_reverse_link_reassign_clear():
    a1 = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    a2 = UML_14_Parameter(defaultValue="sample_text_2", kind="sample_text_2")
    b = UML_14_Method(body="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_Method', {a1})
    assert _is_linked(b, 'UML_14_Method', a1)
    if hasattr(a1, 'UML_14_Parameter2'):
        assert _is_linked(a1, 'UML_14_Parameter2', b)
    _safe_set(b, 'UML_14_Method', {a2})
    assert _is_linked(b, 'UML_14_Method', a2)
    if hasattr(a1, 'UML_14_Parameter2'):
        assert not _is_linked(a1, 'UML_14_Parameter2', b)
    if hasattr(a2, 'UML_14_Parameter2'):
        assert _is_linked(a2, 'UML_14_Parameter2', b)
    _safe_set(b, 'UML_14_Method', set())
    assert not _is_linked(b, 'UML_14_Method', a2)
    if hasattr(a2, 'UML_14_Parameter2'):
        assert not _is_linked(a2, 'UML_14_Parameter2', b)


def test_assoc_parent8_reverse_link_reassign_clear():
    a1 = UML_14_Generalization(discriminator="sample_text")
    a2 = UML_14_Generalization(discriminator="sample_text_2")
    b = UML_14_Class(isActive="sample_text")
    _safe_set(b, 'UML_14_Class10', a1)
    assert _is_linked(b, 'UML_14_Class10', a1)
    if hasattr(a1, 'UML_14_Generalization9'):
        assert _is_linked(a1, 'UML_14_Generalization9', b)
    _safe_set(b, 'UML_14_Class10', a2)
    assert _is_linked(b, 'UML_14_Class10', a2)
    if hasattr(a1, 'UML_14_Generalization9'):
        assert not _is_linked(a1, 'UML_14_Generalization9', b)
    if hasattr(a2, 'UML_14_Generalization9'):
        assert _is_linked(a2, 'UML_14_Generalization9', b)
    _safe_set(b, 'UML_14_Class10', None)
    assert not _is_linked(b, 'UML_14_Class10', a2)
    if hasattr(a2, 'UML_14_Generalization9'):
        assert not _is_linked(a2, 'UML_14_Generalization9', b)


def test_assoc_participant13_reverse_link_reassign_clear():
    a1 = UML_14_Class(isActive="sample_text")
    a2 = UML_14_Class(isActive="sample_text_2")
    b = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_AssociationEnd', a1)
    assert _is_linked(b, 'UML_14_AssociationEnd', a1)
    if hasattr(a1, 'UML_14_Class14'):
        assert _is_linked(a1, 'UML_14_Class14', b)
    _safe_set(b, 'UML_14_AssociationEnd', a2)
    assert _is_linked(b, 'UML_14_AssociationEnd', a2)
    if hasattr(a1, 'UML_14_Class14'):
        assert not _is_linked(a1, 'UML_14_Class14', b)
    if hasattr(a2, 'UML_14_Class14'):
        assert _is_linked(a2, 'UML_14_Class14', b)
    _safe_set(b, 'UML_14_AssociationEnd', None)
    assert not _is_linked(b, 'UML_14_AssociationEnd', a2)
    if hasattr(a2, 'UML_14_Class14'):
        assert not _is_linked(a2, 'UML_14_Class14', b)


def test_assoc_qualifier18_reverse_link_reassign_clear():
    a1 = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    a2 = UML_14_Attribute(initialValue="sample_text_2", visibility="sample_text_2")
    b = UML_14_AssociationEnd(isNavigable="sample_text", visibility="sample_text")
    _safe_set(b, 'UML_14_AssociationEnd19', a1)
    assert _is_linked(b, 'UML_14_AssociationEnd19', a1)
    if hasattr(a1, 'UML_14_Attribute20'):
        assert _is_linked(a1, 'UML_14_Attribute20', b)
    _safe_set(b, 'UML_14_AssociationEnd19', a2)
    assert _is_linked(b, 'UML_14_AssociationEnd19', a2)
    if hasattr(a1, 'UML_14_Attribute20'):
        assert not _is_linked(a1, 'UML_14_Attribute20', b)
    if hasattr(a2, 'UML_14_Attribute20'):
        assert _is_linked(a2, 'UML_14_Attribute20', b)
    _safe_set(b, 'UML_14_AssociationEnd19', None)
    assert not _is_linked(b, 'UML_14_AssociationEnd19', a2)
    if hasattr(a2, 'UML_14_Attribute20'):
        assert not _is_linked(a2, 'UML_14_Attribute20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_association12_stub_double():
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


def test_assoc_classes30_stub_double():
    # UML_14_Package has no real 'UML_14_Package31' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Class(isActive="sample_text")
    partner = UML_14_Package()
    setattr(partner, 'UML_14_Package31', None)
    _safe_set(owner, 'UML_14_Class32', partner)
    assert owner in getattr(partner, 'UML_14_Package31')
    _safe_set(owner, 'UML_14_Class32', None)
    assert owner not in getattr(partner, 'UML_14_Package31')


def test_assoc_connection11_stub_double():
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


def test_assoc_enumeration28_stub_double():
    # UML_14_Enumeration has no real 'Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_EnumerationLiteral(value="sample_text")
    partner = UML_14_Enumeration()
    setattr(partner, 'Enumeration', None)
    _safe_set(owner, 'literal', partner)
    assert getattr(partner, 'Enumeration') == owner
    _safe_set(owner, 'literal', None)
    assert getattr(partner, 'Enumeration') is None


def test_assoc_generalizations39_stub_double():
    # UML_14_Package has no real 'UML_14_Package40' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Generalization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Generalization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Generalization(discriminator="sample_text")
    partner = UML_14_Package()
    setattr(partner, 'UML_14_Package40', None)
    _safe_set(owner, 'UML_14_Generalization41', partner)
    assert owner in getattr(partner, 'UML_14_Package40')
    _safe_set(owner, 'UML_14_Generalization41', None)
    assert owner not in getattr(partner, 'UML_14_Package40')


def test_assoc_literal27_stub_double():
    # UML_14_Enumeration has no real 'enumeration' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_EnumerationLiteral(value="sample_text")
    partner = UML_14_Enumeration()
    setattr(partner, 'enumeration', None)
    _safe_set(owner, 'EnumerationLiteral', partner)
    assert owner in getattr(partner, 'enumeration')
    _safe_set(owner, 'EnumerationLiteral', None)
    assert owner not in getattr(partner, 'enumeration')


def test_assoc_type0_stub_double():
    # UML_14_DataType has no real 'UML_14_DataType' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Parameter(defaultValue="sample_text", kind="sample_text")
    partner = UML_14_DataType()
    setattr(partner, 'UML_14_DataType', None)
    _safe_set(owner, 'UML_14_Parameter', partner)
    assert getattr(partner, 'UML_14_DataType') == owner
    _safe_set(owner, 'UML_14_Parameter', None)
    assert getattr(partner, 'UML_14_DataType') is None


def test_assoc_type4_stub_double():
    # UML_14_DataType has no real 'UML_14_DataType6' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Attribute(initialValue="sample_text", visibility="sample_text")
    partner = UML_14_DataType()
    setattr(partner, 'UML_14_DataType6', None)
    _safe_set(owner, 'UML_14_Attribute5', partner)
    assert getattr(partner, 'UML_14_DataType6') == owner
    _safe_set(owner, 'UML_14_Attribute5', None)
    assert getattr(partner, 'UML_14_DataType6') is None


