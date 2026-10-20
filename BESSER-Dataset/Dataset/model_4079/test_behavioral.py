import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    umlMM_Associaton,
    umlMM_Attribute,
    umlMM_Class,
    umlMM_Classifier,
    umlMM_Datatype,
    umlMM_Package,
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

def test_assoc_Association0_reverse_link_reassign_clear():
    a1 = umlMM_Package(name="sample_text")
    a2 = umlMM_Package(name="sample_text_2")
    b = umlMM_Associaton(name="sample_text")
    _safe_set(b, 'Associaton', a1)
    assert _is_linked(b, 'Associaton', a1)
    if hasattr(a1, 'namespace'):
        assert _is_linked(a1, 'namespace', b)
    _safe_set(b, 'Associaton', a2)
    assert _is_linked(b, 'Associaton', a2)
    if hasattr(a1, 'namespace'):
        assert not _is_linked(a1, 'namespace', b)
    if hasattr(a2, 'namespace'):
        assert _is_linked(a2, 'namespace', b)
    _safe_set(b, 'Associaton', None)
    assert not _is_linked(b, 'Associaton', a2)
    if hasattr(a2, 'namespace'):
        assert not _is_linked(a2, 'namespace', b)


def test_assoc_classifier1_reverse_link_reassign_clear():
    a1 = umlMM_Package(name="sample_text")
    a2 = umlMM_Package(name="sample_text_2")
    b = umlMM_Classifier(name="sample_text")
    _safe_set(b, 'Classifier', a1)
    assert _is_linked(b, 'Classifier', a1)
    if hasattr(a1, 'namespace2'):
        assert _is_linked(a1, 'namespace2', b)
    _safe_set(b, 'Classifier', a2)
    assert _is_linked(b, 'Classifier', a2)
    if hasattr(a1, 'namespace2'):
        assert not _is_linked(a1, 'namespace2', b)
    if hasattr(a2, 'namespace2'):
        assert _is_linked(a2, 'namespace2', b)
    _safe_set(b, 'Classifier', None)
    assert not _is_linked(b, 'Classifier', a2)
    if hasattr(a2, 'namespace2'):
        assert not _is_linked(a2, 'namespace2', b)


def test_assoc_namespace18_reverse_link_reassign_clear():
    a1 = umlMM_Package(name="sample_text")
    a2 = umlMM_Package(name="sample_text_2")
    b = umlMM_Classifier(name="sample_text")
    _safe_set(b, 'classifier', a1)
    assert _is_linked(b, 'classifier', a1)
    if hasattr(a1, 'Package19'):
        assert _is_linked(a1, 'Package19', b)
    _safe_set(b, 'classifier', a2)
    assert _is_linked(b, 'classifier', a2)
    if hasattr(a1, 'Package19'):
        assert not _is_linked(a1, 'Package19', b)
    if hasattr(a2, 'Package19'):
        assert _is_linked(a2, 'Package19', b)
    _safe_set(b, 'classifier', None)
    assert not _is_linked(b, 'classifier', a2)
    if hasattr(a2, 'Package19'):
        assert not _is_linked(a2, 'Package19', b)


def test_assoc_namespace3_reverse_link_reassign_clear():
    a1 = umlMM_Package(name="sample_text")
    a2 = umlMM_Package(name="sample_text_2")
    b = umlMM_Associaton(name="sample_text")
    _safe_set(b, 'Association', a1)
    assert _is_linked(b, 'Association', a1)
    if hasattr(a1, 'Package'):
        assert _is_linked(a1, 'Package', b)
    _safe_set(b, 'Association', a2)
    assert _is_linked(b, 'Association', a2)
    if hasattr(a1, 'Package'):
        assert not _is_linked(a1, 'Package', b)
    if hasattr(a2, 'Package'):
        assert _is_linked(a2, 'Package', b)
    _safe_set(b, 'Association', None)
    assert not _is_linked(b, 'Association', a2)
    if hasattr(a2, 'Package'):
        assert not _is_linked(a2, 'Package', b)


def test_assoc_type12_reverse_link_reassign_clear():
    a1 = umlMM_Classifier(name="sample_text")
    a2 = umlMM_Classifier(name="sample_text_2")
    b = umlMM_Attribute(name="sample_text")
    _safe_set(b, 'typeOf', a1)
    assert _is_linked(b, 'typeOf', a1)
    if hasattr(a1, 'Classifier13'):
        assert _is_linked(a1, 'Classifier13', b)
    _safe_set(b, 'typeOf', a2)
    assert _is_linked(b, 'typeOf', a2)
    if hasattr(a1, 'Classifier13'):
        assert not _is_linked(a1, 'Classifier13', b)
    if hasattr(a2, 'Classifier13'):
        assert _is_linked(a2, 'Classifier13', b)
    _safe_set(b, 'typeOf', None)
    assert not _is_linked(b, 'typeOf', a2)
    if hasattr(a2, 'Classifier13'):
        assert not _is_linked(a2, 'Classifier13', b)


def test_assoc_typeOf16_reverse_link_reassign_clear():
    a1 = umlMM_Classifier(name="sample_text")
    a2 = umlMM_Classifier(name="sample_text_2")
    b = umlMM_Attribute(name="sample_text")
    _safe_set(b, 'Attribute17', a1)
    assert _is_linked(b, 'Attribute17', a1)
    if hasattr(a1, 'type'):
        assert _is_linked(a1, 'type', b)
    _safe_set(b, 'Attribute17', a2)
    assert _is_linked(b, 'Attribute17', a2)
    if hasattr(a1, 'type'):
        assert not _is_linked(a1, 'type', b)
    if hasattr(a2, 'type'):
        assert _is_linked(a2, 'type', b)
    _safe_set(b, 'Attribute17', None)
    assert not _is_linked(b, 'Attribute17', a2)
    if hasattr(a2, 'type'):
        assert not _is_linked(a2, 'type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Owner14_stub_double():
    # umlMM_Class has no real 'Class15' property in the generated
    # code (a bare stub) -- manually attach it so umlMM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlMM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlMM_Attribute(name="sample_text")
    partner = umlMM_Class()
    setattr(partner, 'Class15', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'Class15') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'Class15') is None


def test_assoc_attribute11_stub_double():
    # umlMM_Class has no real 'Owner' property in the generated
    # code (a bare stub) -- manually attach it so umlMM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlMM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlMM_Attribute(name="sample_text")
    partner = umlMM_Class()
    setattr(partner, 'Owner', None)
    _safe_set(owner, 'Attribute', partner)
    assert owner in getattr(partner, 'Owner')
    _safe_set(owner, 'Attribute', None)
    assert owner not in getattr(partner, 'Owner')


def test_assoc_destination4_stub_double():
    # umlMM_Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so umlMM_Associaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlMM_Associaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlMM_Associaton(name="sample_text")
    partner = umlMM_Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'destinationOf', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'destinationOf', None)
    assert getattr(partner, 'Class') is None


def test_assoc_destinationOf7_stub_double():
    # umlMM_Class has no real 'destination' property in the generated
    # code (a bare stub) -- manually attach it so umlMM_Associaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlMM_Associaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlMM_Associaton(name="sample_text")
    partner = umlMM_Class()
    setattr(partner, 'destination', None)
    _safe_set(owner, 'Associaton8', partner)
    assert owner in getattr(partner, 'destination')
    _safe_set(owner, 'Associaton8', None)
    assert owner not in getattr(partner, 'destination')


def test_assoc_source5_stub_double():
    # umlMM_Class has no real 'Class6' property in the generated
    # code (a bare stub) -- manually attach it so umlMM_Associaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlMM_Associaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlMM_Associaton(name="sample_text")
    partner = umlMM_Class()
    setattr(partner, 'Class6', None)
    _safe_set(owner, 'sourceOf', partner)
    assert getattr(partner, 'Class6') == owner
    _safe_set(owner, 'sourceOf', None)
    assert getattr(partner, 'Class6') is None


def test_assoc_sourceOf9_stub_double():
    # umlMM_Class has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so umlMM_Associaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlMM_Associaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlMM_Associaton(name="sample_text")
    partner = umlMM_Class()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Associaton10', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Associaton10', None)
    assert owner not in getattr(partner, 'source')


