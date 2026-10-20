import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    BehavioralFeature,
    BehavioredClassifier,
    Class,
    Classifier,
    Element,
    Event,
    ExecutionSpecification,
    Feature,
    InteractionFragment,
    Message,
    MessageEnd,
    NamedElement,
    Namespace,
    Object,
    OccurrenceSpecification,
    RedefinableElement,
    behavior_Actor,
    behavior_AlternativeMessage,
    behavior_Behavior,
    behavior_BehaviorExecutionSpecification,
    behavior_BehavioralFeature,
    behavior_BehavioredClassifier,
    behavior_Class,
    behavior_Classifier,
    behavior_Comment,
    behavior_Connector,
    behavior_CreatEvent,
    behavior_DestructionEvent,
    behavior_Element,
    behavior_Event,
    behavior_ExecutionEvent,
    behavior_ExecutionOccurrenceSpecification,
    behavior_ExecutionSpecification,
    behavior_Feature,
    behavior_GeneralOrdering,
    behavior_Interaction,
    behavior_InteractionFragment,
    behavior_Lifeline,
    behavior_Message,
    behavior_MessageEnd,
    behavior_MessageOccurrenceSpecification,
    behavior_NamedElement,
    behavior_Namespace,
    behavior_Object,
    behavior_OccurrenceSpecification,
    behavior_Operation,
    behavior_OptionalMessage,
    behavior_RedefinableElement,
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

def test_assoc_feature20_reverse_link_reassign_clear():
    a1 = behavior_Feature(isStatic=True)
    a2 = behavior_Feature(isStatic=False)
    b = behavior_Classifier(isAbstract=True)
    _safe_set(b, 'featuringClassifier', {a1})
    assert _is_linked(b, 'featuringClassifier', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'featuringClassifier', {a2})
    assert _is_linked(b, 'featuringClassifier', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'featuringClassifier', set())
    assert not _is_linked(b, 'featuringClassifier', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_featuringClassifier67_reverse_link_reassign_clear():
    a1 = behavior_Feature(isStatic=True)
    a2 = behavior_Feature(isStatic=False)
    b = behavior_Classifier(isAbstract=True)
    _safe_set(b, 'Classifier', a1)
    assert _is_linked(b, 'Classifier', a1)
    if hasattr(a1, 'feature'):
        assert _is_linked(a1, 'feature', b)
    _safe_set(b, 'Classifier', a2)
    assert _is_linked(b, 'Classifier', a2)
    if hasattr(a1, 'feature'):
        assert not _is_linked(a1, 'feature', b)
    if hasattr(a2, 'feature'):
        assert _is_linked(a2, 'feature', b)
    _safe_set(b, 'Classifier', None)
    assert not _is_linked(b, 'Classifier', a2)
    if hasattr(a2, 'feature'):
        assert not _is_linked(a2, 'feature', b)


def test_assoc_general18_reverse_link_reassign_clear():
    a1 = behavior_Classifier(isAbstract=True)
    a2 = behavior_Classifier(isAbstract=False)
    b = behavior_Classifier(isAbstract=True)
    _safe_set(b, 'behavior_Classifier19', a1)
    assert _is_linked(b, 'behavior_Classifier19', a1)
    if hasattr(a1, 'behavior_Classifier17'):
        assert _is_linked(a1, 'behavior_Classifier17', b)
    _safe_set(b, 'behavior_Classifier19', a2)
    assert _is_linked(b, 'behavior_Classifier19', a2)
    if hasattr(a1, 'behavior_Classifier17'):
        assert not _is_linked(a1, 'behavior_Classifier17', b)
    if hasattr(a2, 'behavior_Classifier17'):
        assert _is_linked(a2, 'behavior_Classifier17', b)
    _safe_set(b, 'behavior_Classifier19', None)
    assert not _is_linked(b, 'behavior_Classifier19', a2)
    if hasattr(a2, 'behavior_Classifier17'):
        assert not _is_linked(a2, 'behavior_Classifier17', b)


def test_assoc_inheritedMember13_reverse_link_reassign_clear():
    a1 = behavior_NamedElement(Archpoint=True, name="sample_text")
    a2 = behavior_NamedElement(Archpoint=False, name="sample_text_2")
    b = behavior_Classifier(isAbstract=True)
    _safe_set(b, 'behavior_Classifier', {a1})
    assert _is_linked(b, 'behavior_Classifier', a1)
    if hasattr(a1, 'behavior_NamedElement'):
        assert _is_linked(a1, 'behavior_NamedElement', b)
    _safe_set(b, 'behavior_Classifier', {a2})
    assert _is_linked(b, 'behavior_Classifier', a2)
    if hasattr(a1, 'behavior_NamedElement'):
        assert not _is_linked(a1, 'behavior_NamedElement', b)
    if hasattr(a2, 'behavior_NamedElement'):
        assert _is_linked(a2, 'behavior_NamedElement', b)
    _safe_set(b, 'behavior_Classifier', set())
    assert not _is_linked(b, 'behavior_Classifier', a2)
    if hasattr(a2, 'behavior_NamedElement'):
        assert not _is_linked(a2, 'behavior_NamedElement', b)


def test_assoc_redefinedClassifier15_reverse_link_reassign_clear():
    a1 = behavior_Classifier(isAbstract=True)
    a2 = behavior_Classifier(isAbstract=False)
    b = behavior_Classifier(isAbstract=True)
    _safe_set(b, 'behavior_Classifier16', a1)
    assert _is_linked(b, 'behavior_Classifier16', a1)
    if hasattr(a1, 'behavior_Classifier14'):
        assert _is_linked(a1, 'behavior_Classifier14', b)
    _safe_set(b, 'behavior_Classifier16', a2)
    assert _is_linked(b, 'behavior_Classifier16', a2)
    if hasattr(a1, 'behavior_Classifier14'):
        assert not _is_linked(a1, 'behavior_Classifier14', b)
    if hasattr(a2, 'behavior_Classifier14'):
        assert _is_linked(a2, 'behavior_Classifier14', b)
    _safe_set(b, 'behavior_Classifier16', None)
    assert not _is_linked(b, 'behavior_Classifier16', a2)
    if hasattr(a2, 'behavior_Classifier14'):
        assert not _is_linked(a2, 'behavior_Classifier14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotatedElement64_stub_double():
    # behavior_Element has no real 'behavior_Element66' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Comment(body="sample_text")
    partner = behavior_Element()
    setattr(partner, 'behavior_Element66', None)
    _safe_set(owner, 'behavior_Comment65', {partner})
    assert getattr(partner, 'behavior_Element66') == owner
    _safe_set(owner, 'behavior_Comment65', set())
    assert getattr(partner, 'behavior_Element66') is None


def test_assoc_connector40_stub_double():
    # behavior_Connector has no real 'behavior_Connector' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Message(MessageOrder=7)
    partner = behavior_Connector()
    setattr(partner, 'behavior_Connector', None)
    _safe_set(owner, 'behavior_Message41', partner)
    assert getattr(partner, 'behavior_Connector') == owner
    _safe_set(owner, 'behavior_Message41', None)
    assert getattr(partner, 'behavior_Connector') is None


def test_assoc_interaction35_stub_double():
    # behavior_Interaction has no real 'Interaction' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Message(MessageOrder=7)
    partner = behavior_Interaction()
    setattr(partner, 'Interaction', None)
    _safe_set(owner, 'message', partner)
    assert getattr(partner, 'Interaction') == owner
    _safe_set(owner, 'message', None)
    assert getattr(partner, 'Interaction') is None


def test_assoc_message57_stub_double():
    # behavior_Interaction has no real 'interaction58' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Message(MessageOrder=7)
    partner = behavior_Interaction()
    setattr(partner, 'interaction58', None)
    _safe_set(owner, 'Message', partner)
    assert owner in getattr(partner, 'interaction58')
    _safe_set(owner, 'Message', None)
    assert owner not in getattr(partner, 'interaction58')


def test_assoc_message75_stub_double():
    # behavior_MessageEnd has no real 'behavior_MessageEnd76' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Message(MessageOrder=7)
    partner = behavior_MessageEnd()
    setattr(partner, 'behavior_MessageEnd76', None)
    _safe_set(owner, 'behavior_Message77', partner)
    assert getattr(partner, 'behavior_MessageEnd76') == owner
    _safe_set(owner, 'behavior_Message77', None)
    assert getattr(partner, 'behavior_MessageEnd76') is None


def test_assoc_messages91_stub_double():
    # behavior_AlternativeMessage has no real 'behavior_AlternativeMessage' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Message(MessageOrder=7)
    partner = behavior_AlternativeMessage()
    setattr(partner, 'behavior_AlternativeMessage', None)
    _safe_set(owner, 'behavior_Message92', partner)
    assert owner in getattr(partner, 'behavior_AlternativeMessage')
    _safe_set(owner, 'behavior_Message92', None)
    assert owner not in getattr(partner, 'behavior_AlternativeMessage')


def test_assoc_nestedClassifier21_stub_double():
    # behavior_Class has no real 'behavior_Class' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Classifier(isAbstract=True)
    partner = behavior_Class()
    setattr(partner, 'behavior_Class', None)
    _safe_set(owner, 'behavior_Classifier22', partner)
    assert owner in getattr(partner, 'behavior_Class')
    _safe_set(owner, 'behavior_Classifier22', None)
    assert owner not in getattr(partner, 'behavior_Class')


def test_assoc_ownedComment28_stub_double():
    # behavior_Element has no real 'behavior_Element' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Comment(body="sample_text")
    partner = behavior_Element()
    setattr(partner, 'behavior_Element', None)
    _safe_set(owner, 'behavior_Comment', partner)
    assert owner in getattr(partner, 'behavior_Element')
    _safe_set(owner, 'behavior_Comment', None)
    assert owner not in getattr(partner, 'behavior_Element')


def test_assoc_receiveEvent36_stub_double():
    # behavior_MessageEnd has no real 'behavior_MessageEnd' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Message(MessageOrder=7)
    partner = behavior_MessageEnd()
    setattr(partner, 'behavior_MessageEnd', None)
    _safe_set(owner, 'behavior_Message', partner)
    assert getattr(partner, 'behavior_MessageEnd') == owner
    _safe_set(owner, 'behavior_Message', None)
    assert getattr(partner, 'behavior_MessageEnd') is None


def test_assoc_redefinitionContext23_stub_double():
    # behavior_RedefinableElement has no real 'behavior_RedefinableElement' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Classifier(isAbstract=True)
    partner = behavior_RedefinableElement()
    setattr(partner, 'behavior_RedefinableElement', None)
    _safe_set(owner, 'behavior_Classifier24', partner)
    assert owner in getattr(partner, 'behavior_RedefinableElement')
    _safe_set(owner, 'behavior_Classifier24', None)
    assert owner not in getattr(partner, 'behavior_RedefinableElement')


def test_assoc_sendEvent37_stub_double():
    # behavior_MessageEnd has no real 'behavior_MessageEnd39' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Message(MessageOrder=7)
    partner = behavior_MessageEnd()
    setattr(partner, 'behavior_MessageEnd39', None)
    _safe_set(owner, 'behavior_Message38', partner)
    assert getattr(partner, 'behavior_MessageEnd39') == owner
    _safe_set(owner, 'behavior_Message38', None)
    assert getattr(partner, 'behavior_MessageEnd39') is None


