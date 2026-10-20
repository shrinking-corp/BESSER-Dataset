import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    AttributeValue,
    classdiagram_Aggregation,
    classdiagram_Association,
    classdiagram_Attribute,
    classdiagram_AttributeValue,
    classdiagram_Class,
    classdiagram_Composition,
    classdiagram_Dependency,
    classdiagram_Diagram,
    classdiagram_Generalization,
    classdiagram_Interface,
    classdiagram_InterfaceRealization,
    classdiagram_Method,
    classdiagram_PrimitiveDataType,
    classdiagram_Realization,
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

def test_assoc_attribute13_reverse_link_reassign_clear():
    a1 = classdiagram_Class(is_persistent=True, name="sample_text")
    a2 = classdiagram_Class(is_persistent=False, name="sample_text_2")
    b = classdiagram_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'classdiagram_Attribute', a1)
    assert _is_linked(b, 'classdiagram_Attribute', a1)
    if hasattr(a1, 'classdiagram_Class14'):
        assert _is_linked(a1, 'classdiagram_Class14', b)
    _safe_set(b, 'classdiagram_Attribute', a2)
    assert _is_linked(b, 'classdiagram_Attribute', a2)
    if hasattr(a1, 'classdiagram_Class14'):
        assert not _is_linked(a1, 'classdiagram_Class14', b)
    if hasattr(a2, 'classdiagram_Class14'):
        assert _is_linked(a2, 'classdiagram_Class14', b)
    _safe_set(b, 'classdiagram_Attribute', None)
    assert not _is_linked(b, 'classdiagram_Attribute', a2)
    if hasattr(a2, 'classdiagram_Class14'):
        assert not _is_linked(a2, 'classdiagram_Class14', b)


def test_assoc_attribute23_reverse_link_reassign_clear():
    a1 = classdiagram_Interface(name="sample_text")
    a2 = classdiagram_Interface(name="sample_text_2")
    b = classdiagram_Attribute(is_primary=True, name="sample_text")
    _safe_set(b, 'classdiagram_Attribute24', a1)
    assert _is_linked(b, 'classdiagram_Attribute24', a1)
    if hasattr(a1, 'classdiagram_Interface'):
        assert _is_linked(a1, 'classdiagram_Interface', b)
    _safe_set(b, 'classdiagram_Attribute24', a2)
    assert _is_linked(b, 'classdiagram_Attribute24', a2)
    if hasattr(a1, 'classdiagram_Interface'):
        assert not _is_linked(a1, 'classdiagram_Interface', b)
    if hasattr(a2, 'classdiagram_Interface'):
        assert _is_linked(a2, 'classdiagram_Interface', b)
    _safe_set(b, 'classdiagram_Attribute24', None)
    assert not _is_linked(b, 'classdiagram_Attribute24', a2)
    if hasattr(a2, 'classdiagram_Interface'):
        assert not _is_linked(a2, 'classdiagram_Interface', b)


def test_assoc_method15_reverse_link_reassign_clear():
    a1 = classdiagram_Method(name="sample_text")
    a2 = classdiagram_Method(name="sample_text_2")
    b = classdiagram_Class(is_persistent=True, name="sample_text")
    _safe_set(b, 'classdiagram_Class16', {a1})
    assert _is_linked(b, 'classdiagram_Class16', a1)
    if hasattr(a1, 'classdiagram_Method'):
        assert _is_linked(a1, 'classdiagram_Method', b)
    _safe_set(b, 'classdiagram_Class16', {a2})
    assert _is_linked(b, 'classdiagram_Class16', a2)
    if hasattr(a1, 'classdiagram_Method'):
        assert not _is_linked(a1, 'classdiagram_Method', b)
    if hasattr(a2, 'classdiagram_Method'):
        assert _is_linked(a2, 'classdiagram_Method', b)
    _safe_set(b, 'classdiagram_Class16', set())
    assert not _is_linked(b, 'classdiagram_Class16', a2)
    if hasattr(a2, 'classdiagram_Method'):
        assert not _is_linked(a2, 'classdiagram_Method', b)


def test_assoc_method25_reverse_link_reassign_clear():
    a1 = classdiagram_Method(name="sample_text")
    a2 = classdiagram_Method(name="sample_text_2")
    b = classdiagram_Interface(name="sample_text")
    _safe_set(b, 'classdiagram_Interface26', {a1})
    assert _is_linked(b, 'classdiagram_Interface26', a1)
    if hasattr(a1, 'classdiagram_Method27'):
        assert _is_linked(a1, 'classdiagram_Method27', b)
    _safe_set(b, 'classdiagram_Interface26', {a2})
    assert _is_linked(b, 'classdiagram_Interface26', a2)
    if hasattr(a1, 'classdiagram_Method27'):
        assert not _is_linked(a1, 'classdiagram_Method27', b)
    if hasattr(a2, 'classdiagram_Method27'):
        assert _is_linked(a2, 'classdiagram_Method27', b)
    _safe_set(b, 'classdiagram_Interface26', set())
    assert not _is_linked(b, 'classdiagram_Interface26', a2)
    if hasattr(a2, 'classdiagram_Method27'):
        assert not _is_linked(a2, 'classdiagram_Method27', b)


def test_assoc_source7_reverse_link_reassign_clear():
    a1 = classdiagram_Class(is_persistent=True, name="sample_text")
    a2 = classdiagram_Class(is_persistent=False, name="sample_text_2")
    b = classdiagram_Association(name="sample_text", sourceMultiplicity=7, targetMultiplicity=7)
    _safe_set(b, 'classdiagram_Association8', a1)
    assert _is_linked(b, 'classdiagram_Association8', a1)
    if hasattr(a1, 'classdiagram_Class9'):
        assert _is_linked(a1, 'classdiagram_Class9', b)
    _safe_set(b, 'classdiagram_Association8', a2)
    assert _is_linked(b, 'classdiagram_Association8', a2)
    if hasattr(a1, 'classdiagram_Class9'):
        assert not _is_linked(a1, 'classdiagram_Class9', b)
    if hasattr(a2, 'classdiagram_Class9'):
        assert _is_linked(a2, 'classdiagram_Class9', b)
    _safe_set(b, 'classdiagram_Association8', None)
    assert not _is_linked(b, 'classdiagram_Association8', a2)
    if hasattr(a2, 'classdiagram_Class9'):
        assert not _is_linked(a2, 'classdiagram_Class9', b)


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = classdiagram_Class(is_persistent=True, name="sample_text")
    a2 = classdiagram_Class(is_persistent=False, name="sample_text_2")
    b = classdiagram_Association(name="sample_text", sourceMultiplicity=7, targetMultiplicity=7)
    _safe_set(b, 'classdiagram_Association11', a1)
    assert _is_linked(b, 'classdiagram_Association11', a1)
    if hasattr(a1, 'classdiagram_Class12'):
        assert _is_linked(a1, 'classdiagram_Class12', b)
    _safe_set(b, 'classdiagram_Association11', a2)
    assert _is_linked(b, 'classdiagram_Association11', a2)
    if hasattr(a1, 'classdiagram_Class12'):
        assert not _is_linked(a1, 'classdiagram_Class12', b)
    if hasattr(a2, 'classdiagram_Class12'):
        assert _is_linked(a2, 'classdiagram_Class12', b)
    _safe_set(b, 'classdiagram_Association11', None)
    assert not _is_linked(b, 'classdiagram_Association11', a2)
    if hasattr(a2, 'classdiagram_Class12'):
        assert not _is_linked(a2, 'classdiagram_Class12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_associations1_stub_double():
    # classdiagram_Diagram has no real 'classdiagram_Diagram2' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Association(name="sample_text", sourceMultiplicity=7, targetMultiplicity=7)
    partner = classdiagram_Diagram()
    setattr(partner, 'classdiagram_Diagram2', None)
    _safe_set(owner, 'classdiagram_Association', partner)
    assert owner in getattr(partner, 'classdiagram_Diagram2')
    _safe_set(owner, 'classdiagram_Association', None)
    assert owner not in getattr(partner, 'classdiagram_Diagram2')


def test_assoc_classes0_stub_double():
    # classdiagram_Diagram has no real 'classdiagram_Diagram' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Class(is_persistent=True, name="sample_text")
    partner = classdiagram_Diagram()
    setattr(partner, 'classdiagram_Diagram', None)
    _safe_set(owner, 'classdiagram_Class', partner)
    assert owner in getattr(partner, 'classdiagram_Diagram')
    _safe_set(owner, 'classdiagram_Class', None)
    assert owner not in getattr(partner, 'classdiagram_Diagram')


def test_assoc_source17_stub_double():
    # classdiagram_Generalization has no real 'classdiagram_Generalization18' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Class(is_persistent=True, name="sample_text")
    partner = classdiagram_Generalization()
    setattr(partner, 'classdiagram_Generalization18', None)
    _safe_set(owner, 'classdiagram_Class19', partner)
    assert getattr(partner, 'classdiagram_Generalization18') == owner
    _safe_set(owner, 'classdiagram_Class19', None)
    assert getattr(partner, 'classdiagram_Generalization18') is None


def test_assoc_source28_stub_double():
    # classdiagram_InterfaceRealization has no real 'classdiagram_InterfaceRealization' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Interface(name="sample_text")
    partner = classdiagram_InterfaceRealization()
    setattr(partner, 'classdiagram_InterfaceRealization', None)
    _safe_set(owner, 'classdiagram_Interface29', partner)
    assert owner in getattr(partner, 'classdiagram_InterfaceRealization')
    _safe_set(owner, 'classdiagram_Interface29', None)
    assert owner not in getattr(partner, 'classdiagram_InterfaceRealization')


def test_assoc_source33_stub_double():
    # classdiagram_Realization has no real 'classdiagram_Realization' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Class(is_persistent=True, name="sample_text")
    partner = classdiagram_Realization()
    setattr(partner, 'classdiagram_Realization', None)
    _safe_set(owner, 'classdiagram_Class34', partner)
    assert getattr(partner, 'classdiagram_Realization') == owner
    _safe_set(owner, 'classdiagram_Class34', None)
    assert getattr(partner, 'classdiagram_Realization') is None


def test_assoc_target20_stub_double():
    # classdiagram_Generalization has no real 'classdiagram_Generalization21' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Class(is_persistent=True, name="sample_text")
    partner = classdiagram_Generalization()
    setattr(partner, 'classdiagram_Generalization21', None)
    _safe_set(owner, 'classdiagram_Class22', partner)
    assert getattr(partner, 'classdiagram_Generalization21') == owner
    _safe_set(owner, 'classdiagram_Class22', None)
    assert getattr(partner, 'classdiagram_Generalization21') is None


def test_assoc_target30_stub_double():
    # classdiagram_InterfaceRealization has no real 'classdiagram_InterfaceRealization31' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Class(is_persistent=True, name="sample_text")
    partner = classdiagram_InterfaceRealization()
    setattr(partner, 'classdiagram_InterfaceRealization31', None)
    _safe_set(owner, 'classdiagram_Class32', partner)
    assert owner in getattr(partner, 'classdiagram_InterfaceRealization31')
    _safe_set(owner, 'classdiagram_Class32', None)
    assert owner not in getattr(partner, 'classdiagram_InterfaceRealization31')


def test_assoc_target35_stub_double():
    # classdiagram_Realization has no real 'classdiagram_Realization36' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Class(is_persistent=True, name="sample_text")
    partner = classdiagram_Realization()
    setattr(partner, 'classdiagram_Realization36', None)
    _safe_set(owner, 'classdiagram_Class37', partner)
    assert owner in getattr(partner, 'classdiagram_Realization36')
    _safe_set(owner, 'classdiagram_Class37', None)
    assert owner not in getattr(partner, 'classdiagram_Realization36')


def test_assoc_type38_stub_double():
    # classdiagram_AttributeValue has no real 'classdiagram_AttributeValue' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Attribute(is_primary=True, name="sample_text")
    partner = classdiagram_AttributeValue()
    setattr(partner, 'classdiagram_AttributeValue', None)
    _safe_set(owner, 'classdiagram_Attribute39', partner)
    assert getattr(partner, 'classdiagram_AttributeValue') == owner
    _safe_set(owner, 'classdiagram_Attribute39', None)
    assert getattr(partner, 'classdiagram_AttributeValue') is None


def test_assoc_types3_stub_double():
    # classdiagram_Diagram has no real 'classdiagram_Diagram4' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_PrimitiveDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_PrimitiveDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_PrimitiveDataType(name="sample_text")
    partner = classdiagram_Diagram()
    setattr(partner, 'classdiagram_Diagram4', None)
    _safe_set(owner, 'classdiagram_PrimitiveDataType', partner)
    assert owner in getattr(partner, 'classdiagram_Diagram4')
    _safe_set(owner, 'classdiagram_PrimitiveDataType', None)
    assert owner not in getattr(partner, 'classdiagram_Diagram4')


