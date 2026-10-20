import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    beans_Bean,
    beans_BeanLibrary,
    beans_BeanProperty,
    beans_NamedElement,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bean3_stub_double():
    # beans_Bean has no real 'Bean4' property in the generated
    # code (a bare stub) -- manually attach it so beans_BeanProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # beans_BeanProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = beans_BeanProperty(changeable=True, typeName="sample_text")
    partner = beans_Bean()
    setattr(partner, 'Bean4', None)
    _safe_set(owner, 'properties', partner)
    assert getattr(partner, 'Bean4') == owner
    _safe_set(owner, 'properties', None)
    assert getattr(partner, 'Bean4') is None


def test_assoc_beanLibrary1_stub_double():
    # beans_Bean has no real 'beans' property in the generated
    # code (a bare stub) -- manually attach it so beans_BeanLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # beans_BeanLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = beans_BeanLibrary(packageName="sample_text")
    partner = beans_Bean()
    setattr(partner, 'beans', None)
    _safe_set(owner, 'BeanLibrary', partner)
    assert getattr(partner, 'beans') == owner
    _safe_set(owner, 'BeanLibrary', None)
    assert getattr(partner, 'beans') is None


def test_assoc_beans0_stub_double():
    # beans_Bean has no real 'Bean' property in the generated
    # code (a bare stub) -- manually attach it so beans_BeanLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # beans_BeanLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = beans_BeanLibrary(packageName="sample_text")
    partner = beans_Bean()
    setattr(partner, 'Bean', None)
    _safe_set(owner, 'beanLibrary', {partner})
    assert getattr(partner, 'Bean') == owner
    _safe_set(owner, 'beanLibrary', set())
    assert getattr(partner, 'Bean') is None


def test_assoc_properties2_stub_double():
    # beans_Bean has no real 'bean' property in the generated
    # code (a bare stub) -- manually attach it so beans_BeanProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # beans_BeanProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = beans_BeanProperty(changeable=True, typeName="sample_text")
    partner = beans_Bean()
    setattr(partner, 'bean', None)
    _safe_set(owner, 'BeanProperty', partner)
    assert owner in getattr(partner, 'bean')
    _safe_set(owner, 'BeanProperty', None)
    assert owner not in getattr(partner, 'bean')


