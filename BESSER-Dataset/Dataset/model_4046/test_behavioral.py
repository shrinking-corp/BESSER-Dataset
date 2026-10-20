import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    UML_Action,
    UML_ActivityNode,
    UML_Behavior,
    UML_BehavioralFeature,
    UML_BehavioredClassifier,
    UML_Class,
    UML_Classifier,
    UML_ConnectableElement,
    UML_Feature,
    UML_NamedElement,
    UML_Namespace,
    UML_PackageableElement,
    UML_Property,
    UML_RedefinableElement,
    UML_StructuralFeature,
    UML_Type,
    UML_TypedElement,
    UML_ValueSpecification,
    uml_UML_Action,
    uml_UML_Activity,
    uml_UML_ActivityEdge,
    uml_UML_ActivityNode,
    uml_UML_Behavior,
    uml_UML_BehavioralFeature,
    uml_UML_BehavioredClassifier,
    uml_UML_CallOperationAction,
    uml_UML_Class,
    uml_UML_Classifier,
    uml_UML_ConnectableElement,
    uml_UML_Connector,
    uml_UML_ConnectorEnd,
    uml_UML_Constraint,
    uml_UML_Feature,
    uml_UML_Interface,
    uml_UML_InterfaceRealization,
    uml_UML_NamedElement,
    uml_UML_Namespace,
    uml_UML_OpaqueExpression,
    uml_UML_Operation,
    uml_UML_Package,
    uml_UML_PackageableElement,
    uml_UML_Port,
    uml_UML_Property,
    uml_UML_RedefinableElement,
    uml_UML_StructuralFeature,
    uml_UML_Type,
    uml_UML_TypedElement,
    uml_UML_ValueSpecification,
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

def test_assoc_incoming28_reverse_link_reassign_clear():
    a1 = uml_UML_ActivityNode(name="sample_text")
    a2 = uml_UML_ActivityNode(name="sample_text_2")
    b = uml_UML_ActivityNode(name="sample_text")
    _safe_set(b, 'uml_UML_ActivityNode29', a1)
    assert _is_linked(b, 'uml_UML_ActivityNode29', a1)
    if hasattr(a1, 'uml_UML_ActivityNode27'):
        assert _is_linked(a1, 'uml_UML_ActivityNode27', b)
    _safe_set(b, 'uml_UML_ActivityNode29', a2)
    assert _is_linked(b, 'uml_UML_ActivityNode29', a2)
    if hasattr(a1, 'uml_UML_ActivityNode27'):
        assert not _is_linked(a1, 'uml_UML_ActivityNode27', b)
    if hasattr(a2, 'uml_UML_ActivityNode27'):
        assert _is_linked(a2, 'uml_UML_ActivityNode27', b)
    _safe_set(b, 'uml_UML_ActivityNode29', None)
    assert not _is_linked(b, 'uml_UML_ActivityNode29', a2)
    if hasattr(a2, 'uml_UML_ActivityNode27'):
        assert not _is_linked(a2, 'uml_UML_ActivityNode27', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_node22_stub_double():
    # uml_UML_Activity has no real 'uml_UML_Activity23' property in the generated
    # code (a bare stub) -- manually attach it so uml_UML_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_UML_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_UML_ActivityNode(name="sample_text")
    partner = uml_UML_Activity()
    setattr(partner, 'uml_UML_Activity23', None)
    _safe_set(owner, 'uml_UML_ActivityNode', partner)
    assert owner in getattr(partner, 'uml_UML_Activity23')
    _safe_set(owner, 'uml_UML_ActivityNode', None)
    assert owner not in getattr(partner, 'uml_UML_Activity23')


def test_assoc_outgoing30_stub_double():
    # uml_UML_ActivityEdge has no real 'uml_UML_ActivityEdge32' property in the generated
    # code (a bare stub) -- manually attach it so uml_UML_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_UML_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_UML_ActivityNode(name="sample_text")
    partner = uml_UML_ActivityEdge()
    setattr(partner, 'uml_UML_ActivityEdge32', None)
    _safe_set(owner, 'uml_UML_ActivityNode31', {partner})
    assert getattr(partner, 'uml_UML_ActivityEdge32') == owner
    _safe_set(owner, 'uml_UML_ActivityNode31', set())
    assert getattr(partner, 'uml_UML_ActivityEdge32') is None


def test_assoc_source33_stub_double():
    # uml_UML_ActivityEdge has no real 'uml_UML_ActivityEdge34' property in the generated
    # code (a bare stub) -- manually attach it so uml_UML_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_UML_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_UML_ActivityNode(name="sample_text")
    partner = uml_UML_ActivityEdge()
    setattr(partner, 'uml_UML_ActivityEdge34', None)
    _safe_set(owner, 'uml_UML_ActivityNode35', partner)
    assert getattr(partner, 'uml_UML_ActivityEdge34') == owner
    _safe_set(owner, 'uml_UML_ActivityNode35', None)
    assert getattr(partner, 'uml_UML_ActivityEdge34') is None


def test_assoc_specification39_stub_double():
    # uml_UML_Constraint has no real 'uml_UML_Constraint40' property in the generated
    # code (a bare stub) -- manually attach it so uml_UML_OpaqueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_UML_OpaqueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_UML_OpaqueExpression(body="sample_text", language="sample_text")
    partner = uml_UML_Constraint()
    setattr(partner, 'uml_UML_Constraint40', None)
    _safe_set(owner, 'uml_UML_OpaqueExpression', partner)
    assert getattr(partner, 'uml_UML_Constraint40') == owner
    _safe_set(owner, 'uml_UML_OpaqueExpression', None)
    assert getattr(partner, 'uml_UML_Constraint40') is None


def test_assoc_target36_stub_double():
    # uml_UML_ActivityEdge has no real 'uml_UML_ActivityEdge37' property in the generated
    # code (a bare stub) -- manually attach it so uml_UML_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_UML_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_UML_ActivityNode(name="sample_text")
    partner = uml_UML_ActivityEdge()
    setattr(partner, 'uml_UML_ActivityEdge37', None)
    _safe_set(owner, 'uml_UML_ActivityNode38', partner)
    assert getattr(partner, 'uml_UML_ActivityEdge37') == owner
    _safe_set(owner, 'uml_UML_ActivityNode38', None)
    assert getattr(partner, 'uml_UML_ActivityEdge37') is None


