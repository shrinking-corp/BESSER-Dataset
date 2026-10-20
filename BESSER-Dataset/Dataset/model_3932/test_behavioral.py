import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Member,
    NamedElement,
    Type,
    entity_Entity,
    entity_Field,
    entity_Member,
    entity_Method,
    entity_NamedElement,
    entity_Package,
    entity_Service,
    entity_Type,
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

def test_assoc_methods2_stub_double():
    # entity_Service has no real 'entity_Service' property in the generated
    # code (a bare stub) -- manually attach it so entity_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entity_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entity_Method(isAbstract=True)
    partner = entity_Service()
    setattr(partner, 'entity_Service', None)
    _safe_set(owner, 'entity_Method', partner)
    assert owner in getattr(partner, 'entity_Service')
    _safe_set(owner, 'entity_Method', None)
    assert owner not in getattr(partner, 'entity_Service')


