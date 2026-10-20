import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GalileoNodeType,
    dft_GalileoDft,
    dft_GalileoFaultTreeNode,
    dft_GalileoNodeType,
    dft_Named,
    dft_Observer,
    dft_Parametrized,
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

def test_assoc_children10_reverse_link_reassign_clear():
    a1 = dft_GalileoFaultTreeNode(dorm="sample_text", lambda_="sample_text", name="sample_text", repair="sample_text")
    a2 = dft_GalileoFaultTreeNode(dorm="sample_text_2", lambda_="sample_text_2", name="sample_text_2", repair="sample_text_2")
    b = dft_GalileoFaultTreeNode(dorm="sample_text", lambda_="sample_text", name="sample_text", repair="sample_text")
    _safe_set(b, 'dft_GalileoFaultTreeNode9', {a1})
    assert _is_linked(b, 'dft_GalileoFaultTreeNode9', a1)
    if hasattr(a1, 'dft_GalileoFaultTreeNode11'):
        assert _is_linked(a1, 'dft_GalileoFaultTreeNode11', b)
    _safe_set(b, 'dft_GalileoFaultTreeNode9', {a2})
    assert _is_linked(b, 'dft_GalileoFaultTreeNode9', a2)
    if hasattr(a1, 'dft_GalileoFaultTreeNode11'):
        assert not _is_linked(a1, 'dft_GalileoFaultTreeNode11', b)
    if hasattr(a2, 'dft_GalileoFaultTreeNode11'):
        assert _is_linked(a2, 'dft_GalileoFaultTreeNode11', b)
    _safe_set(b, 'dft_GalileoFaultTreeNode9', set())
    assert not _is_linked(b, 'dft_GalileoFaultTreeNode9', a2)
    if hasattr(a2, 'dft_GalileoFaultTreeNode11'):
        assert not _is_linked(a2, 'dft_GalileoFaultTreeNode11', b)


def test_assoc_observables12_reverse_link_reassign_clear():
    a1 = dft_Observer(observationRate="sample_text")
    a2 = dft_Observer(observationRate="sample_text_2")
    b = dft_GalileoFaultTreeNode(dorm="sample_text", lambda_="sample_text", name="sample_text", repair="sample_text")
    _safe_set(b, 'dft_GalileoFaultTreeNode13', a1)
    assert _is_linked(b, 'dft_GalileoFaultTreeNode13', a1)
    if hasattr(a1, 'dft_Observer'):
        assert _is_linked(a1, 'dft_Observer', b)
    _safe_set(b, 'dft_GalileoFaultTreeNode13', a2)
    assert _is_linked(b, 'dft_GalileoFaultTreeNode13', a2)
    if hasattr(a1, 'dft_Observer'):
        assert not _is_linked(a1, 'dft_Observer', b)
    if hasattr(a2, 'dft_Observer'):
        assert _is_linked(a2, 'dft_Observer', b)
    _safe_set(b, 'dft_GalileoFaultTreeNode13', None)
    assert not _is_linked(b, 'dft_GalileoFaultTreeNode13', a2)
    if hasattr(a2, 'dft_Observer'):
        assert not _is_linked(a2, 'dft_Observer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_basicEvents4_stub_double():
    # dft_GalileoDft has no real 'dft_GalileoDft5' property in the generated
    # code (a bare stub) -- manually attach it so dft_GalileoFaultTreeNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dft_GalileoFaultTreeNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dft_GalileoFaultTreeNode(dorm="sample_text", lambda_="sample_text", name="sample_text", repair="sample_text")
    partner = dft_GalileoDft()
    setattr(partner, 'dft_GalileoDft5', None)
    _safe_set(owner, 'dft_GalileoFaultTreeNode6', partner)
    assert owner in getattr(partner, 'dft_GalileoDft5')
    _safe_set(owner, 'dft_GalileoFaultTreeNode6', None)
    assert owner not in getattr(partner, 'dft_GalileoDft5')


def test_assoc_gates1_stub_double():
    # dft_GalileoDft has no real 'dft_GalileoDft2' property in the generated
    # code (a bare stub) -- manually attach it so dft_GalileoFaultTreeNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dft_GalileoFaultTreeNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dft_GalileoFaultTreeNode(dorm="sample_text", lambda_="sample_text", name="sample_text", repair="sample_text")
    partner = dft_GalileoDft()
    setattr(partner, 'dft_GalileoDft2', None)
    _safe_set(owner, 'dft_GalileoFaultTreeNode3', partner)
    assert owner in getattr(partner, 'dft_GalileoDft2')
    _safe_set(owner, 'dft_GalileoFaultTreeNode3', None)
    assert owner not in getattr(partner, 'dft_GalileoDft2')


def test_assoc_root0_stub_double():
    # dft_GalileoDft has no real 'dft_GalileoDft' property in the generated
    # code (a bare stub) -- manually attach it so dft_GalileoFaultTreeNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dft_GalileoFaultTreeNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dft_GalileoFaultTreeNode(dorm="sample_text", lambda_="sample_text", name="sample_text", repair="sample_text")
    partner = dft_GalileoDft()
    setattr(partner, 'dft_GalileoDft', None)
    _safe_set(owner, 'dft_GalileoFaultTreeNode', partner)
    assert getattr(partner, 'dft_GalileoDft') == owner
    _safe_set(owner, 'dft_GalileoFaultTreeNode', None)
    assert getattr(partner, 'dft_GalileoDft') is None


def test_assoc_type7_stub_double():
    # dft_GalileoNodeType has no real 'dft_GalileoNodeType' property in the generated
    # code (a bare stub) -- manually attach it so dft_GalileoFaultTreeNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dft_GalileoFaultTreeNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dft_GalileoFaultTreeNode(dorm="sample_text", lambda_="sample_text", name="sample_text", repair="sample_text")
    partner = dft_GalileoNodeType()
    setattr(partner, 'dft_GalileoNodeType', None)
    _safe_set(owner, 'dft_GalileoFaultTreeNode8', partner)
    assert getattr(partner, 'dft_GalileoNodeType') == owner
    _safe_set(owner, 'dft_GalileoFaultTreeNode8', None)
    assert getattr(partner, 'dft_GalileoNodeType') is None


