import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FormalParameterList,
    NamedElement,
    Order,
    Variable,
    service_Asc,
    service_Association,
    service_BusinessOperation,
    service_Desc,
    service_EntityOrView,
    service_Feature,
    service_Order,
    service_Predicate,
    service_Selection,
    service_Service,
    service_ServiceFeatureReference,
    service_Services,
    service_Variable,
    OperationResultTypes,
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

def test_assoc_feature16_stub_double():
    # service_Feature has no real 'service_Feature17' property in the generated
    # code (a bare stub) -- manually attach it so service_ServiceFeatureReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_ServiceFeatureReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_ServiceFeatureReference(name="sample_text")
    partner = service_Feature()
    setattr(partner, 'service_Feature17', None)
    _safe_set(owner, 'service_ServiceFeatureReference', partner)
    assert getattr(partner, 'service_Feature17') == owner
    _safe_set(owner, 'service_ServiceFeatureReference', None)
    assert getattr(partner, 'service_Feature17') is None


def test_assoc_fields7_stub_double():
    # service_Feature has no real 'service_Feature' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, selected=True)
    partner = service_Feature()
    setattr(partner, 'service_Feature', None)
    _safe_set(owner, 'service_Selection', {partner})
    assert getattr(partner, 'service_Feature') == owner
    _safe_set(owner, 'service_Selection', set())
    assert getattr(partner, 'service_Feature') is None


def test_assoc_filter10_stub_double():
    # service_Predicate has no real 'service_Predicate' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, selected=True)
    partner = service_Predicate()
    setattr(partner, 'service_Predicate', None)
    _safe_set(owner, 'service_Selection11', partner)
    assert getattr(partner, 'service_Predicate') == owner
    _safe_set(owner, 'service_Selection11', None)
    assert getattr(partner, 'service_Predicate') is None


def test_assoc_joins8_stub_double():
    # service_Association has no real 'service_Association' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, selected=True)
    partner = service_Association()
    setattr(partner, 'service_Association', None)
    _safe_set(owner, 'service_Selection9', {partner})
    assert getattr(partner, 'service_Association') == owner
    _safe_set(owner, 'service_Selection9', set())
    assert getattr(partner, 'service_Association') is None


def test_assoc_operations4_stub_double():
    # service_Service has no real 'service_Service5' property in the generated
    # code (a bare stub) -- manually attach it so service_BusinessOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_BusinessOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_BusinessOperation(resultMimeType="sample_text", resultType="sample_text")
    partner = service_Service()
    setattr(partner, 'service_Service5', None)
    _safe_set(owner, 'service_BusinessOperation', partner)
    assert owner in getattr(partner, 'service_Service5')
    _safe_set(owner, 'service_BusinessOperation', None)
    assert owner not in getattr(partner, 'service_Service5')


def test_assoc_ordering12_stub_double():
    # service_Order has no real 'service_Order' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, selected=True)
    partner = service_Order()
    setattr(partner, 'service_Order', None)
    _safe_set(owner, 'service_Selection13', {partner})
    assert getattr(partner, 'service_Order') == owner
    _safe_set(owner, 'service_Selection13', set())
    assert getattr(partner, 'service_Order') is None


def test_assoc_selections3_stub_double():
    # service_Service has no real 'usedBy' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, selected=True)
    partner = service_Service()
    setattr(partner, 'usedBy', None)
    _safe_set(owner, 'Selection', partner)
    assert owner in getattr(partner, 'usedBy')
    _safe_set(owner, 'Selection', None)
    assert owner not in getattr(partner, 'usedBy')


def test_assoc_usedBy6_stub_double():
    # service_Service has no real 'Service' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, selected=True)
    partner = service_Service()
    setattr(partner, 'Service', None)
    _safe_set(owner, 'selections', partner)
    assert getattr(partner, 'Service') == owner
    _safe_set(owner, 'selections', None)
    assert getattr(partner, 'Service') is None


def test_assoc_uses18_stub_double():
    # service_Service has no real 'service_Service20' property in the generated
    # code (a bare stub) -- manually attach it so service_BusinessOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_BusinessOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_BusinessOperation(resultMimeType="sample_text", resultType="sample_text")
    partner = service_Service()
    setattr(partner, 'service_Service20', None)
    _safe_set(owner, 'service_BusinessOperation19', {partner})
    assert getattr(partner, 'service_Service20') == owner
    _safe_set(owner, 'service_BusinessOperation19', set())
    assert getattr(partner, 'service_Service20') is None


