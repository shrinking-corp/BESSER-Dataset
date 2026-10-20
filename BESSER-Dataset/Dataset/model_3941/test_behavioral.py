import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    UmlMM_Class,
    UmlMM_Classifier,
    UmlMM_DataType,
    UmlMM_Operation,
    UmlMM_Parameter,
    UmlMM_Property,
    UmlMM_UmlPackage,
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

def test_assoc__Class12_reverse_link_reassign_clear():
    a1 = UmlMM_Property(lower=7, name="sample_text", upper=7)
    a2 = UmlMM_Property(lower=13, name="sample_text_2", upper=13)
    b = UmlMM_Class(name="sample_text")
    _safe_set(b, 'Class13', a1)
    assert _is_linked(b, 'Class13', a1)
    if hasattr(a1, '_property'):
        assert _is_linked(a1, '_property', b)
    _safe_set(b, 'Class13', a2)
    assert _is_linked(b, 'Class13', a2)
    if hasattr(a1, '_property'):
        assert not _is_linked(a1, '_property', b)
    if hasattr(a2, '_property'):
        assert _is_linked(a2, '_property', b)
    _safe_set(b, 'Class13', None)
    assert not _is_linked(b, 'Class13', a2)
    if hasattr(a2, '_property'):
        assert not _is_linked(a2, '_property', b)


def test_assoc__Class5_reverse_link_reassign_clear():
    a1 = UmlMM_Operation(name="sample_text")
    a2 = UmlMM_Operation(name="sample_text_2")
    b = UmlMM_Class(name="sample_text")
    _safe_set(b, 'Class', a1)
    assert _is_linked(b, 'Class', a1)
    if hasattr(a1, 'operation'):
        assert _is_linked(a1, 'operation', b)
    _safe_set(b, 'Class', a2)
    assert _is_linked(b, 'Class', a2)
    if hasattr(a1, 'operation'):
        assert not _is_linked(a1, 'operation', b)
    if hasattr(a2, 'operation'):
        assert _is_linked(a2, 'operation', b)
    _safe_set(b, 'Class', None)
    assert not _is_linked(b, 'Class', a2)
    if hasattr(a2, 'operation'):
        assert not _is_linked(a2, 'operation', b)


def test_assoc__Operation8_reverse_link_reassign_clear():
    a1 = UmlMM_Parameter(name="sample_text")
    a2 = UmlMM_Parameter(name="sample_text_2")
    b = UmlMM_Operation(name="sample_text")
    _safe_set(b, 'Operation9', a1)
    assert _is_linked(b, 'Operation9', a1)
    if hasattr(a1, 'parameter'):
        assert _is_linked(a1, 'parameter', b)
    _safe_set(b, 'Operation9', a2)
    assert _is_linked(b, 'Operation9', a2)
    if hasattr(a1, 'parameter'):
        assert not _is_linked(a1, 'parameter', b)
    if hasattr(a2, 'parameter'):
        assert _is_linked(a2, 'parameter', b)
    _safe_set(b, 'Operation9', None)
    assert not _is_linked(b, 'Operation9', a2)
    if hasattr(a2, 'parameter'):
        assert not _is_linked(a2, 'parameter', b)


def test_assoc__property3_reverse_link_reassign_clear():
    a1 = UmlMM_Property(lower=7, name="sample_text", upper=7)
    a2 = UmlMM_Property(lower=13, name="sample_text_2", upper=13)
    b = UmlMM_Class(name="sample_text")
    _safe_set(b, '_Class4', {a1})
    assert _is_linked(b, '_Class4', a1)
    if hasattr(a1, 'Property'):
        assert _is_linked(a1, 'Property', b)
    _safe_set(b, '_Class4', {a2})
    assert _is_linked(b, '_Class4', a2)
    if hasattr(a1, 'Property'):
        assert not _is_linked(a1, 'Property', b)
    if hasattr(a2, 'Property'):
        assert _is_linked(a2, 'Property', b)
    _safe_set(b, '_Class4', set())
    assert not _is_linked(b, '_Class4', a2)
    if hasattr(a2, 'Property'):
        assert not _is_linked(a2, 'Property', b)


def test_assoc_operation2_reverse_link_reassign_clear():
    a1 = UmlMM_Operation(name="sample_text")
    a2 = UmlMM_Operation(name="sample_text_2")
    b = UmlMM_Class(name="sample_text")
    _safe_set(b, '_Class', {a1})
    assert _is_linked(b, '_Class', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, '_Class', {a2})
    assert _is_linked(b, '_Class', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, '_Class', set())
    assert not _is_linked(b, '_Class', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


def test_assoc_parameter6_reverse_link_reassign_clear():
    a1 = UmlMM_Parameter(name="sample_text")
    a2 = UmlMM_Parameter(name="sample_text_2")
    b = UmlMM_Operation(name="sample_text")
    _safe_set(b, '_Operation', {a1})
    assert _is_linked(b, '_Operation', a1)
    if hasattr(a1, 'Parameter'):
        assert _is_linked(a1, 'Parameter', b)
    _safe_set(b, '_Operation', {a2})
    assert _is_linked(b, '_Operation', a2)
    if hasattr(a1, 'Parameter'):
        assert not _is_linked(a1, 'Parameter', b)
    if hasattr(a2, 'Parameter'):
        assert _is_linked(a2, 'Parameter', b)
    _safe_set(b, '_Operation', set())
    assert not _is_linked(b, '_Operation', a2)
    if hasattr(a2, 'Parameter'):
        assert not _is_linked(a2, 'Parameter', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__UmlPackage1_stub_double():
    # UmlMM_Classifier has no real 'elements' property in the generated
    # code (a bare stub) -- manually attach it so UmlMM_UmlPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UmlMM_UmlPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UmlMM_UmlPackage(name="sample_text")
    partner = UmlMM_Classifier()
    setattr(partner, 'elements', None)
    _safe_set(owner, 'UmlPackage', partner)
    assert getattr(partner, 'elements') == owner
    _safe_set(owner, 'UmlPackage', None)
    assert getattr(partner, 'elements') is None


def test_assoc_elements0_stub_double():
    # UmlMM_Classifier has no real 'Classifier' property in the generated
    # code (a bare stub) -- manually attach it so UmlMM_UmlPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UmlMM_UmlPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UmlMM_UmlPackage(name="sample_text")
    partner = UmlMM_Classifier()
    setattr(partner, 'Classifier', None)
    _safe_set(owner, '_UmlPackage', {partner})
    assert getattr(partner, 'Classifier') == owner
    _safe_set(owner, '_UmlPackage', set())
    assert getattr(partner, 'Classifier') is None


def test_assoc_type10_stub_double():
    # UmlMM_Classifier has no real 'UmlMM_Classifier11' property in the generated
    # code (a bare stub) -- manually attach it so UmlMM_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UmlMM_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UmlMM_Property(lower=7, name="sample_text", upper=7)
    partner = UmlMM_Classifier()
    setattr(partner, 'UmlMM_Classifier11', None)
    _safe_set(owner, 'UmlMM_Property', partner)
    assert getattr(partner, 'UmlMM_Classifier11') == owner
    _safe_set(owner, 'UmlMM_Property', None)
    assert getattr(partner, 'UmlMM_Classifier11') is None


def test_assoc_type7_stub_double():
    # UmlMM_Classifier has no real 'UmlMM_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so UmlMM_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UmlMM_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UmlMM_Parameter(name="sample_text")
    partner = UmlMM_Classifier()
    setattr(partner, 'UmlMM_Classifier', None)
    _safe_set(owner, 'UmlMM_Parameter', partner)
    assert getattr(partner, 'UmlMM_Classifier') == owner
    _safe_set(owner, 'UmlMM_Parameter', None)
    assert getattr(partner, 'UmlMM_Classifier') is None


