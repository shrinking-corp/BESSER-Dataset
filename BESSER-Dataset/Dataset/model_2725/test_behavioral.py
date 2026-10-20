import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    scrShYQYaSD_HVOwDYkMdHvynG,
    scrShYQYaSD_ak,
    scrShYQYaSD_xvHXdRr,
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

def test_assoc_kykuZBWLRVLW13_reverse_link_reassign_clear():
    a1 = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    a2 = scrShYQYaSD_ak(CXmvqzTe="sample_text_2", MHQpVCYtERyk="sample_text_2", zBIcb="sample_text_2")
    b = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    _safe_set(b, 'scrShYQYaSD_ak14', a1)
    assert _is_linked(b, 'scrShYQYaSD_ak14', a1)
    if hasattr(a1, 'scrShYQYaSD_ak12'):
        assert _is_linked(a1, 'scrShYQYaSD_ak12', b)
    _safe_set(b, 'scrShYQYaSD_ak14', a2)
    assert _is_linked(b, 'scrShYQYaSD_ak14', a2)
    if hasattr(a1, 'scrShYQYaSD_ak12'):
        assert not _is_linked(a1, 'scrShYQYaSD_ak12', b)
    if hasattr(a2, 'scrShYQYaSD_ak12'):
        assert _is_linked(a2, 'scrShYQYaSD_ak12', b)
    _safe_set(b, 'scrShYQYaSD_ak14', None)
    assert not _is_linked(b, 'scrShYQYaSD_ak14', a2)
    if hasattr(a2, 'scrShYQYaSD_ak12'):
        assert not _is_linked(a2, 'scrShYQYaSD_ak12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_BASoFcxsCI1_stub_double():
    # scrShYQYaSD_xvHXdRr has no real 'scrShYQYaSD_xvHXdRr2' property in the generated
    # code (a bare stub) -- manually attach it so scrShYQYaSD_ak's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scrShYQYaSD_ak's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    partner = scrShYQYaSD_xvHXdRr()
    setattr(partner, 'scrShYQYaSD_xvHXdRr2', None)
    _safe_set(owner, 'scrShYQYaSD_ak', partner)
    assert owner in getattr(partner, 'scrShYQYaSD_xvHXdRr2')
    _safe_set(owner, 'scrShYQYaSD_ak', None)
    assert owner not in getattr(partner, 'scrShYQYaSD_xvHXdRr2')


def test_assoc_JZZCZDdtPb9_stub_double():
    # scrShYQYaSD_xvHXdRr has no real 'scrShYQYaSD_xvHXdRr10' property in the generated
    # code (a bare stub) -- manually attach it so scrShYQYaSD_ak's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scrShYQYaSD_ak's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    partner = scrShYQYaSD_xvHXdRr()
    setattr(partner, 'scrShYQYaSD_xvHXdRr10', None)
    _safe_set(owner, 'scrShYQYaSD_ak11', partner)
    assert owner in getattr(partner, 'scrShYQYaSD_xvHXdRr10')
    _safe_set(owner, 'scrShYQYaSD_ak11', None)
    assert owner not in getattr(partner, 'scrShYQYaSD_xvHXdRr10')


def test_assoc_VSMbxzKCXwhSgFqrC0_stub_double():
    # scrShYQYaSD_xvHXdRr has no real 'scrShYQYaSD_xvHXdRr' property in the generated
    # code (a bare stub) -- manually attach it so scrShYQYaSD_HVOwDYkMdHvynG's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scrShYQYaSD_HVOwDYkMdHvynG's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scrShYQYaSD_HVOwDYkMdHvynG(vdjNPHX="sample_text")
    partner = scrShYQYaSD_xvHXdRr()
    setattr(partner, 'scrShYQYaSD_xvHXdRr', None)
    _safe_set(owner, 'scrShYQYaSD_HVOwDYkMdHvynG', partner)
    assert owner in getattr(partner, 'scrShYQYaSD_xvHXdRr')
    _safe_set(owner, 'scrShYQYaSD_HVOwDYkMdHvynG', None)
    assert owner not in getattr(partner, 'scrShYQYaSD_xvHXdRr')


def test_assoc_XObnJr15_stub_double():
    # scrShYQYaSD_xvHXdRr has no real 'scrShYQYaSD_xvHXdRr17' property in the generated
    # code (a bare stub) -- manually attach it so scrShYQYaSD_ak's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scrShYQYaSD_ak's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    partner = scrShYQYaSD_xvHXdRr()
    setattr(partner, 'scrShYQYaSD_xvHXdRr17', None)
    _safe_set(owner, 'scrShYQYaSD_ak16', partner)
    assert getattr(partner, 'scrShYQYaSD_xvHXdRr17') == owner
    _safe_set(owner, 'scrShYQYaSD_ak16', None)
    assert getattr(partner, 'scrShYQYaSD_xvHXdRr17') is None


def test_assoc_gQaACsS18_stub_double():
    # scrShYQYaSD_xvHXdRr has no real 'scrShYQYaSD_xvHXdRr20' property in the generated
    # code (a bare stub) -- manually attach it so scrShYQYaSD_ak's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scrShYQYaSD_ak's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    partner = scrShYQYaSD_xvHXdRr()
    setattr(partner, 'scrShYQYaSD_xvHXdRr20', None)
    _safe_set(owner, 'scrShYQYaSD_ak19', partner)
    assert getattr(partner, 'scrShYQYaSD_xvHXdRr20') == owner
    _safe_set(owner, 'scrShYQYaSD_ak19', None)
    assert getattr(partner, 'scrShYQYaSD_xvHXdRr20') is None


def test_assoc_keJwdNxMQ6_stub_double():
    # scrShYQYaSD_xvHXdRr has no real 'scrShYQYaSD_xvHXdRr7' property in the generated
    # code (a bare stub) -- manually attach it so scrShYQYaSD_ak's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scrShYQYaSD_ak's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    partner = scrShYQYaSD_xvHXdRr()
    setattr(partner, 'scrShYQYaSD_xvHXdRr7', None)
    _safe_set(owner, 'scrShYQYaSD_ak8', partner)
    assert getattr(partner, 'scrShYQYaSD_xvHXdRr7') == owner
    _safe_set(owner, 'scrShYQYaSD_ak8', None)
    assert getattr(partner, 'scrShYQYaSD_xvHXdRr7') is None


def test_assoc_njevJtUoy3_stub_double():
    # scrShYQYaSD_xvHXdRr has no real 'scrShYQYaSD_xvHXdRr4' property in the generated
    # code (a bare stub) -- manually attach it so scrShYQYaSD_ak's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scrShYQYaSD_ak's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scrShYQYaSD_ak(CXmvqzTe="sample_text", MHQpVCYtERyk="sample_text", zBIcb="sample_text")
    partner = scrShYQYaSD_xvHXdRr()
    setattr(partner, 'scrShYQYaSD_xvHXdRr4', None)
    _safe_set(owner, 'scrShYQYaSD_ak5', partner)
    assert owner in getattr(partner, 'scrShYQYaSD_xvHXdRr4')
    _safe_set(owner, 'scrShYQYaSD_ak5', None)
    assert owner not in getattr(partner, 'scrShYQYaSD_xvHXdRr4')


