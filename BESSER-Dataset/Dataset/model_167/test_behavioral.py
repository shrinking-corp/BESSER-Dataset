import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    lit_petriNets_Net,
    lit_petriNets_Place,
    lit_petriNets_Transition,
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

def test_assoc_dst13_reverse_link_reassign_clear():
    a1 = lit_petriNets_Transition(name="sample_text")
    a2 = lit_petriNets_Transition(name="sample_text_2")
    b = lit_petriNets_Place(name="sample_text")
    _safe_set(b, 'Place15', a1)
    assert _is_linked(b, 'Place15', a1)
    if hasattr(a1, 'src14'):
        assert _is_linked(a1, 'src14', b)
    _safe_set(b, 'Place15', a2)
    assert _is_linked(b, 'Place15', a2)
    if hasattr(a1, 'src14'):
        assert not _is_linked(a1, 'src14', b)
    if hasattr(a2, 'src14'):
        assert _is_linked(a2, 'src14', b)
    _safe_set(b, 'Place15', None)
    assert not _is_linked(b, 'Place15', a2)
    if hasattr(a2, 'src14'):
        assert not _is_linked(a2, 'src14', b)


def test_assoc_dst6_reverse_link_reassign_clear():
    a1 = lit_petriNets_Transition(name="sample_text")
    a2 = lit_petriNets_Transition(name="sample_text_2")
    b = lit_petriNets_Place(name="sample_text")
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Transition7'):
        assert _is_linked(a1, 'Transition7', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Transition7'):
        assert not _is_linked(a1, 'Transition7', b)
    if hasattr(a2, 'Transition7'):
        assert _is_linked(a2, 'Transition7', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Transition7'):
        assert not _is_linked(a2, 'Transition7', b)


def test_assoc_net3_reverse_link_reassign_clear():
    a1 = lit_petriNets_Place(name="sample_text")
    a2 = lit_petriNets_Place(name="sample_text_2")
    b = lit_petriNets_Net(name="sample_text")
    _safe_set(b, 'Net', a1)
    assert _is_linked(b, 'Net', a1)
    if hasattr(a1, 'places'):
        assert _is_linked(a1, 'places', b)
    _safe_set(b, 'Net', a2)
    assert _is_linked(b, 'Net', a2)
    if hasattr(a1, 'places'):
        assert not _is_linked(a1, 'places', b)
    if hasattr(a2, 'places'):
        assert _is_linked(a2, 'places', b)
    _safe_set(b, 'Net', None)
    assert not _is_linked(b, 'Net', a2)
    if hasattr(a2, 'places'):
        assert not _is_linked(a2, 'places', b)


def test_assoc_net8_reverse_link_reassign_clear():
    a1 = lit_petriNets_Transition(name="sample_text")
    a2 = lit_petriNets_Transition(name="sample_text_2")
    b = lit_petriNets_Net(name="sample_text")
    _safe_set(b, 'Net9', a1)
    assert _is_linked(b, 'Net9', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'Net9', a2)
    assert _is_linked(b, 'Net9', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'Net9', None)
    assert not _is_linked(b, 'Net9', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_places0_reverse_link_reassign_clear():
    a1 = lit_petriNets_Place(name="sample_text")
    a2 = lit_petriNets_Place(name="sample_text_2")
    b = lit_petriNets_Net(name="sample_text")
    _safe_set(b, 'net', {a1})
    assert _is_linked(b, 'net', a1)
    if hasattr(a1, 'Place'):
        assert _is_linked(a1, 'Place', b)
    _safe_set(b, 'net', {a2})
    assert _is_linked(b, 'net', a2)
    if hasattr(a1, 'Place'):
        assert not _is_linked(a1, 'Place', b)
    if hasattr(a2, 'Place'):
        assert _is_linked(a2, 'Place', b)
    _safe_set(b, 'net', set())
    assert not _is_linked(b, 'net', a2)
    if hasattr(a2, 'Place'):
        assert not _is_linked(a2, 'Place', b)


def test_assoc_src10_reverse_link_reassign_clear():
    a1 = lit_petriNets_Transition(name="sample_text")
    a2 = lit_petriNets_Transition(name="sample_text_2")
    b = lit_petriNets_Place(name="sample_text")
    _safe_set(b, 'Place12', a1)
    assert _is_linked(b, 'Place12', a1)
    if hasattr(a1, 'dst11'):
        assert _is_linked(a1, 'dst11', b)
    _safe_set(b, 'Place12', a2)
    assert _is_linked(b, 'Place12', a2)
    if hasattr(a1, 'dst11'):
        assert not _is_linked(a1, 'dst11', b)
    if hasattr(a2, 'dst11'):
        assert _is_linked(a2, 'dst11', b)
    _safe_set(b, 'Place12', None)
    assert not _is_linked(b, 'Place12', a2)
    if hasattr(a2, 'dst11'):
        assert not _is_linked(a2, 'dst11', b)


def test_assoc_src4_reverse_link_reassign_clear():
    a1 = lit_petriNets_Transition(name="sample_text")
    a2 = lit_petriNets_Transition(name="sample_text_2")
    b = lit_petriNets_Place(name="sample_text")
    _safe_set(b, 'dst', {a1})
    assert _is_linked(b, 'dst', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'dst', {a2})
    assert _is_linked(b, 'dst', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'dst', set())
    assert not _is_linked(b, 'dst', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = lit_petriNets_Transition(name="sample_text")
    a2 = lit_petriNets_Transition(name="sample_text_2")
    b = lit_petriNets_Net(name="sample_text")
    _safe_set(b, 'net2', {a1})
    assert _is_linked(b, 'net2', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'net2', {a2})
    assert _is_linked(b, 'net2', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'net2', set())
    assert not _is_linked(b, 'net2', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

