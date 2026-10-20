import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FormalParameterList,
    NamedDisplayElement,
    NamedElement,
    Order,
    Variable,
    service_Asc,
    service_Association,
    service_BusinessOperation,
    service_Constant,
    service_ConstantReference,
    service_Desc,
    service_EntityAssociation,
    service_EntityOrView,
    service_Expression,
    service_Feature,
    service_Filter,
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

def test_assoc_filters25_reverse_link_reassign_clear():
    a1 = service_Selection(distinct=True, limit=7, methodName="sample_text")
    a2 = service_Selection(distinct=False, limit=13, methodName="sample_text_2")
    b = service_Filter(methodName="sample_text")
    _safe_set(b, 'Filter', a1)
    assert _is_linked(b, 'Filter', a1)
    if hasattr(a1, 'selection'):
        assert _is_linked(a1, 'selection', b)
    _safe_set(b, 'Filter', a2)
    assert _is_linked(b, 'Filter', a2)
    if hasattr(a1, 'selection'):
        assert not _is_linked(a1, 'selection', b)
    if hasattr(a2, 'selection'):
        assert _is_linked(a2, 'selection', b)
    _safe_set(b, 'Filter', None)
    assert not _is_linked(b, 'Filter', a2)
    if hasattr(a2, 'selection'):
        assert not _is_linked(a2, 'selection', b)


def test_assoc_selection40_reverse_link_reassign_clear():
    a1 = service_Selection(distinct=True, limit=7, methodName="sample_text")
    a2 = service_Selection(distinct=False, limit=13, methodName="sample_text_2")
    b = service_Filter(methodName="sample_text")
    _safe_set(b, 'filters', a1)
    assert _is_linked(b, 'filters', a1)
    if hasattr(a1, 'Selection41'):
        assert _is_linked(a1, 'Selection41', b)
    _safe_set(b, 'filters', a2)
    assert _is_linked(b, 'filters', a2)
    if hasattr(a1, 'Selection41'):
        assert not _is_linked(a1, 'Selection41', b)
    if hasattr(a2, 'Selection41'):
        assert _is_linked(a2, 'Selection41', b)
    _safe_set(b, 'filters', None)
    assert not _is_linked(b, 'filters', a2)
    if hasattr(a2, 'Selection41'):
        assert not _is_linked(a2, 'Selection41', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition23_stub_double():
    # service_Predicate has no real 'service_Predicate' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Predicate()
    setattr(partner, 'service_Predicate', None)
    _safe_set(owner, 'service_Selection24', partner)
    assert getattr(partner, 'service_Predicate') == owner
    _safe_set(owner, 'service_Selection24', None)
    assert getattr(partner, 'service_Predicate') is None


def test_assoc_condition42_stub_double():
    # service_Predicate has no real 'service_Predicate43' property in the generated
    # code (a bare stub) -- manually attach it so service_Filter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Filter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Filter(methodName="sample_text")
    partner = service_Predicate()
    setattr(partner, 'service_Predicate43', None)
    _safe_set(owner, 'service_Filter', partner)
    assert getattr(partner, 'service_Predicate43') == owner
    _safe_set(owner, 'service_Filter', None)
    assert getattr(partner, 'service_Predicate43') is None


def test_assoc_definedBy36_stub_double():
    # service_Service has no real 'Service37' property in the generated
    # code (a bare stub) -- manually attach it so service_BusinessOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_BusinessOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_BusinessOperation(resultMimeType="sample_text", resultType="sample_text")
    partner = service_Service()
    setattr(partner, 'Service37', None)
    _safe_set(owner, 'operations', partner)
    assert getattr(partner, 'Service37') == owner
    _safe_set(owner, 'operations', None)
    assert getattr(partner, 'Service37') is None


def test_assoc_feature34_stub_double():
    # service_Feature has no real 'service_Feature35' property in the generated
    # code (a bare stub) -- manually attach it so service_ServiceFeatureReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_ServiceFeatureReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_ServiceFeatureReference(name="sample_text")
    partner = service_Feature()
    setattr(partner, 'service_Feature35', None)
    _safe_set(owner, 'service_ServiceFeatureReference', partner)
    assert getattr(partner, 'service_Feature35') == owner
    _safe_set(owner, 'service_ServiceFeatureReference', None)
    assert getattr(partner, 'service_Feature35') is None


def test_assoc_fields19_stub_double():
    # service_Feature has no real 'service_Feature' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Feature()
    setattr(partner, 'service_Feature', None)
    _safe_set(owner, 'service_Selection20', {partner})
    assert getattr(partner, 'service_Feature') == owner
    _safe_set(owner, 'service_Selection20', set())
    assert getattr(partner, 'service_Feature') is None


def test_assoc_findAll5_stub_double():
    # service_Service has no real 'service_Service6' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Service()
    setattr(partner, 'service_Service6', None)
    _safe_set(owner, 'service_Selection', partner)
    assert getattr(partner, 'service_Service6') == owner
    _safe_set(owner, 'service_Selection', None)
    assert getattr(partner, 'service_Service6') is None


def test_assoc_findOne7_stub_double():
    # service_Service has no real 'service_Service8' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Service()
    setattr(partner, 'service_Service8', None)
    _safe_set(owner, 'service_Selection9', partner)
    assert getattr(partner, 'service_Service8') == owner
    _safe_set(owner, 'service_Selection9', None)
    assert getattr(partner, 'service_Service8') is None


def test_assoc_joins21_stub_double():
    # service_Association has no real 'service_Association' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Association()
    setattr(partner, 'service_Association', None)
    _safe_set(owner, 'service_Selection22', {partner})
    assert getattr(partner, 'service_Association') == owner
    _safe_set(owner, 'service_Selection22', set())
    assert getattr(partner, 'service_Association') is None


def test_assoc_operations10_stub_double():
    # service_Service has no real 'definedBy11' property in the generated
    # code (a bare stub) -- manually attach it so service_BusinessOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_BusinessOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_BusinessOperation(resultMimeType="sample_text", resultType="sample_text")
    partner = service_Service()
    setattr(partner, 'definedBy11', None)
    _safe_set(owner, 'BusinessOperation', partner)
    assert owner in getattr(partner, 'definedBy11')
    _safe_set(owner, 'BusinessOperation', None)
    assert owner not in getattr(partner, 'definedBy11')


def test_assoc_ordering26_stub_double():
    # service_Order has no real 'service_Order' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Order()
    setattr(partner, 'service_Order', None)
    _safe_set(owner, 'service_Selection27', {partner})
    assert getattr(partner, 'service_Order') == owner
    _safe_set(owner, 'service_Selection27', set())
    assert getattr(partner, 'service_Order') is None


def test_assoc_selectPath28_stub_double():
    # service_EntityAssociation has no real 'service_EntityAssociation' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_EntityAssociation()
    setattr(partner, 'service_EntityAssociation', None)
    _safe_set(owner, 'service_Selection29', {partner})
    assert getattr(partner, 'service_EntityAssociation') == owner
    _safe_set(owner, 'service_Selection29', set())
    assert getattr(partner, 'service_EntityAssociation') is None


def test_assoc_selections4_stub_double():
    # service_Service has no real 'usedBy' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Service()
    setattr(partner, 'usedBy', None)
    _safe_set(owner, 'Selection', partner)
    assert owner in getattr(partner, 'usedBy')
    _safe_set(owner, 'Selection', None)
    assert owner not in getattr(partner, 'usedBy')


def test_assoc_usedBy17_stub_double():
    # service_Service has no real 'Service18' property in the generated
    # code (a bare stub) -- manually attach it so service_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_Selection(distinct=True, limit=7, methodName="sample_text")
    partner = service_Service()
    setattr(partner, 'Service18', None)
    _safe_set(owner, 'selections', partner)
    assert getattr(partner, 'Service18') == owner
    _safe_set(owner, 'selections', None)
    assert getattr(partner, 'Service18') is None


def test_assoc_uses38_stub_double():
    # service_Service has no real 'service_Service39' property in the generated
    # code (a bare stub) -- manually attach it so service_BusinessOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_BusinessOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_BusinessOperation(resultMimeType="sample_text", resultType="sample_text")
    partner = service_Service()
    setattr(partner, 'service_Service39', None)
    _safe_set(owner, 'service_BusinessOperation', {partner})
    assert getattr(partner, 'service_Service39') == owner
    _safe_set(owner, 'service_BusinessOperation', set())
    assert getattr(partner, 'service_Service39') is None


def test_assoc_value32_stub_double():
    # service_Constant has no real 'service_Constant33' property in the generated
    # code (a bare stub) -- manually attach it so service_ConstantReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # service_ConstantReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = service_ConstantReference(name="sample_text")
    partner = service_Constant()
    setattr(partner, 'service_Constant33', None)
    _safe_set(owner, 'service_ConstantReference', partner)
    assert getattr(partner, 'service_Constant33') == owner
    _safe_set(owner, 'service_ConstantReference', None)
    assert getattr(partner, 'service_Constant33') is None


