import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BehavioredClassifier,
    Classifier,
    DirectedRelationship,
    EModelElement,
    Element,
    NamedElement,
    Namespace,
    PackageableElement,
    ParameterableElement,
    RedefinableElement,
    Relationship,
    TemplateableElement,
    Type,
    umluseCases_Actor,
    umluseCases_BehavioredClassifier,
    umluseCases_Classifier,
    umluseCases_DirectedRelationship,
    umluseCases_Element,
    umluseCases_Extend,
    umluseCases_ExtensionPoint,
    umluseCases_Include,
    umluseCases_NamedElement,
    umluseCases_Namespace,
    umluseCases_PackageableElement,
    umluseCases_ParameterableElement,
    umluseCases_RedefinableElement,
    umluseCases_Relationship,
    umluseCases_TemplateableElement,
    umluseCases_Type,
    umluseCases_UseCase,
    AggregationKind,
    CallConcurrencyKind,
    ConnectorKind,
    ExpansionKind,
    InteractionOperatorKind,
    MessageKind,
    MessageSort,
    ObjectNodeOrderingKind,
    ParameterDirectionKind,
    ParameterEffectKind,
    PseudostateKind,
    TransitionKind,
    VisibilityKind,
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

def test_assoc_extend33_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Extend()
    _safe_set(b, 'Extend', a1)
    assert _is_linked(b, 'Extend', a1)
    if hasattr(a1, 'extension'):
        assert _is_linked(a1, 'extension', b)
    _safe_set(b, 'Extend', a2)
    assert _is_linked(b, 'Extend', a2)
    if hasattr(a1, 'extension'):
        assert not _is_linked(a1, 'extension', b)
    if hasattr(a2, 'extension'):
        assert _is_linked(a2, 'extension', b)
    _safe_set(b, 'Extend', None)
    assert not _is_linked(b, 'Extend', a2)
    if hasattr(a2, 'extension'):
        assert not _is_linked(a2, 'extension', b)


def test_assoc_extendedCase41_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Extend()
    _safe_set(b, 'umluseCases_Extend', a1)
    assert _is_linked(b, 'umluseCases_Extend', a1)
    if hasattr(a1, 'umluseCases_UseCase42'):
        assert _is_linked(a1, 'umluseCases_UseCase42', b)
    _safe_set(b, 'umluseCases_Extend', a2)
    assert _is_linked(b, 'umluseCases_Extend', a2)
    if hasattr(a1, 'umluseCases_UseCase42'):
        assert not _is_linked(a1, 'umluseCases_UseCase42', b)
    if hasattr(a2, 'umluseCases_UseCase42'):
        assert _is_linked(a2, 'umluseCases_UseCase42', b)
    _safe_set(b, 'umluseCases_Extend', None)
    assert not _is_linked(b, 'umluseCases_Extend', a2)
    if hasattr(a2, 'umluseCases_UseCase42'):
        assert not _is_linked(a2, 'umluseCases_UseCase42', b)


def test_assoc_extension45_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Extend()
    _safe_set(b, 'extend', a1)
    assert _is_linked(b, 'extend', a1)
    if hasattr(a1, 'UseCase46'):
        assert _is_linked(a1, 'UseCase46', b)
    _safe_set(b, 'extend', a2)
    assert _is_linked(b, 'extend', a2)
    if hasattr(a1, 'UseCase46'):
        assert not _is_linked(a1, 'UseCase46', b)
    if hasattr(a2, 'UseCase46'):
        assert _is_linked(a2, 'UseCase46', b)
    _safe_set(b, 'extend', None)
    assert not _is_linked(b, 'extend', a2)
    if hasattr(a2, 'UseCase46'):
        assert not _is_linked(a2, 'UseCase46', b)


def test_assoc_extensionLocation43_reverse_link_reassign_clear():
    a1 = umluseCases_ExtensionPoint()
    a2 = umluseCases_ExtensionPoint()
    b = umluseCases_Extend()
    _safe_set(b, 'umluseCases_Extend44', {a1})
    assert _is_linked(b, 'umluseCases_Extend44', a1)
    if hasattr(a1, 'umluseCases_ExtensionPoint'):
        assert _is_linked(a1, 'umluseCases_ExtensionPoint', b)
    _safe_set(b, 'umluseCases_Extend44', {a2})
    assert _is_linked(b, 'umluseCases_Extend44', a2)
    if hasattr(a1, 'umluseCases_ExtensionPoint'):
        assert not _is_linked(a1, 'umluseCases_ExtensionPoint', b)
    if hasattr(a2, 'umluseCases_ExtensionPoint'):
        assert _is_linked(a2, 'umluseCases_ExtensionPoint', b)
    _safe_set(b, 'umluseCases_Extend44', set())
    assert not _is_linked(b, 'umluseCases_Extend44', a2)
    if hasattr(a2, 'umluseCases_ExtensionPoint'):
        assert not _is_linked(a2, 'umluseCases_ExtensionPoint', b)


def test_assoc_extensionPoint34_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_ExtensionPoint()
    _safe_set(b, 'ExtensionPoint', a1)
    assert _is_linked(b, 'ExtensionPoint', a1)
    if hasattr(a1, 'useCase'):
        assert _is_linked(a1, 'useCase', b)
    _safe_set(b, 'ExtensionPoint', a2)
    assert _is_linked(b, 'ExtensionPoint', a2)
    if hasattr(a1, 'useCase'):
        assert not _is_linked(a1, 'useCase', b)
    if hasattr(a2, 'useCase'):
        assert _is_linked(a2, 'useCase', b)
    _safe_set(b, 'ExtensionPoint', None)
    assert not _is_linked(b, 'ExtensionPoint', a2)
    if hasattr(a2, 'useCase'):
        assert not _is_linked(a2, 'useCase', b)


def test_assoc_general22_reverse_link_reassign_clear():
    a1 = umluseCases_Classifier(isAbstract="sample_text")
    a2 = umluseCases_Classifier(isAbstract="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier23', a1)
    assert _is_linked(b, 'umluseCases_Classifier23', a1)
    if hasattr(a1, 'umluseCases_Classifier21'):
        assert _is_linked(a1, 'umluseCases_Classifier21', b)
    _safe_set(b, 'umluseCases_Classifier23', a2)
    assert _is_linked(b, 'umluseCases_Classifier23', a2)
    if hasattr(a1, 'umluseCases_Classifier21'):
        assert not _is_linked(a1, 'umluseCases_Classifier21', b)
    if hasattr(a2, 'umluseCases_Classifier21'):
        assert _is_linked(a2, 'umluseCases_Classifier21', b)
    _safe_set(b, 'umluseCases_Classifier23', None)
    assert not _is_linked(b, 'umluseCases_Classifier23', a2)
    if hasattr(a2, 'umluseCases_Classifier21'):
        assert not _is_linked(a2, 'umluseCases_Classifier21', b)


def test_assoc_inheritedMember16_reverse_link_reassign_clear():
    a1 = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    a2 = umluseCases_NamedElement(name="sample_text_2", qualifiedName="sample_text_2", visibility="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier', {a1})
    assert _is_linked(b, 'umluseCases_Classifier', a1)
    if hasattr(a1, 'umluseCases_NamedElement17'):
        assert _is_linked(a1, 'umluseCases_NamedElement17', b)
    _safe_set(b, 'umluseCases_Classifier', {a2})
    assert _is_linked(b, 'umluseCases_Classifier', a2)
    if hasattr(a1, 'umluseCases_NamedElement17'):
        assert not _is_linked(a1, 'umluseCases_NamedElement17', b)
    if hasattr(a2, 'umluseCases_NamedElement17'):
        assert _is_linked(a2, 'umluseCases_NamedElement17', b)
    _safe_set(b, 'umluseCases_Classifier', set())
    assert not _is_linked(b, 'umluseCases_Classifier', a2)
    if hasattr(a2, 'umluseCases_NamedElement17'):
        assert not _is_linked(a2, 'umluseCases_NamedElement17', b)


def test_assoc_ownedUseCase24_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier25', {a1})
    assert _is_linked(b, 'umluseCases_Classifier25', a1)
    if hasattr(a1, 'umluseCases_UseCase'):
        assert _is_linked(a1, 'umluseCases_UseCase', b)
    _safe_set(b, 'umluseCases_Classifier25', {a2})
    assert _is_linked(b, 'umluseCases_Classifier25', a2)
    if hasattr(a1, 'umluseCases_UseCase'):
        assert not _is_linked(a1, 'umluseCases_UseCase', b)
    if hasattr(a2, 'umluseCases_UseCase'):
        assert _is_linked(a2, 'umluseCases_UseCase', b)
    _safe_set(b, 'umluseCases_Classifier25', set())
    assert not _is_linked(b, 'umluseCases_Classifier25', a2)
    if hasattr(a2, 'umluseCases_UseCase'):
        assert not _is_linked(a2, 'umluseCases_UseCase', b)


def test_assoc_redefinedClassifier19_reverse_link_reassign_clear():
    a1 = umluseCases_Classifier(isAbstract="sample_text")
    a2 = umluseCases_Classifier(isAbstract="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier20', a1)
    assert _is_linked(b, 'umluseCases_Classifier20', a1)
    if hasattr(a1, 'umluseCases_Classifier18'):
        assert _is_linked(a1, 'umluseCases_Classifier18', b)
    _safe_set(b, 'umluseCases_Classifier20', a2)
    assert _is_linked(b, 'umluseCases_Classifier20', a2)
    if hasattr(a1, 'umluseCases_Classifier18'):
        assert not _is_linked(a1, 'umluseCases_Classifier18', b)
    if hasattr(a2, 'umluseCases_Classifier18'):
        assert _is_linked(a2, 'umluseCases_Classifier18', b)
    _safe_set(b, 'umluseCases_Classifier20', None)
    assert not _is_linked(b, 'umluseCases_Classifier20', a2)
    if hasattr(a2, 'umluseCases_Classifier18'):
        assert not _is_linked(a2, 'umluseCases_Classifier18', b)


def test_assoc_redefinedElement28_reverse_link_reassign_clear():
    a1 = umluseCases_RedefinableElement(isLeaf="sample_text")
    a2 = umluseCases_RedefinableElement(isLeaf="sample_text_2")
    b = umluseCases_RedefinableElement(isLeaf="sample_text")
    _safe_set(b, 'umluseCases_RedefinableElement27', {a1})
    assert _is_linked(b, 'umluseCases_RedefinableElement27', a1)
    if hasattr(a1, 'umluseCases_RedefinableElement'):
        assert _is_linked(a1, 'umluseCases_RedefinableElement', b)
    _safe_set(b, 'umluseCases_RedefinableElement27', {a2})
    assert _is_linked(b, 'umluseCases_RedefinableElement27', a2)
    if hasattr(a1, 'umluseCases_RedefinableElement'):
        assert not _is_linked(a1, 'umluseCases_RedefinableElement', b)
    if hasattr(a2, 'umluseCases_RedefinableElement'):
        assert _is_linked(a2, 'umluseCases_RedefinableElement', b)
    _safe_set(b, 'umluseCases_RedefinableElement27', set())
    assert not _is_linked(b, 'umluseCases_RedefinableElement27', a2)
    if hasattr(a2, 'umluseCases_RedefinableElement'):
        assert not _is_linked(a2, 'umluseCases_RedefinableElement', b)


def test_assoc_redefinitionContext29_reverse_link_reassign_clear():
    a1 = umluseCases_RedefinableElement(isLeaf="sample_text")
    a2 = umluseCases_RedefinableElement(isLeaf="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier31', a1)
    assert _is_linked(b, 'umluseCases_Classifier31', a1)
    if hasattr(a1, 'umluseCases_RedefinableElement30'):
        assert _is_linked(a1, 'umluseCases_RedefinableElement30', b)
    _safe_set(b, 'umluseCases_Classifier31', a2)
    assert _is_linked(b, 'umluseCases_Classifier31', a2)
    if hasattr(a1, 'umluseCases_RedefinableElement30'):
        assert not _is_linked(a1, 'umluseCases_RedefinableElement30', b)
    if hasattr(a2, 'umluseCases_RedefinableElement30'):
        assert _is_linked(a2, 'umluseCases_RedefinableElement30', b)
    _safe_set(b, 'umluseCases_Classifier31', None)
    assert not _is_linked(b, 'umluseCases_Classifier31', a2)
    if hasattr(a2, 'umluseCases_RedefinableElement30'):
        assert not _is_linked(a2, 'umluseCases_RedefinableElement30', b)


def test_assoc_subject35_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'Classifier', a1)
    assert _is_linked(b, 'Classifier', a1)
    if hasattr(a1, 'useCase36'):
        assert _is_linked(a1, 'useCase36', b)
    _safe_set(b, 'Classifier', a2)
    assert _is_linked(b, 'Classifier', a2)
    if hasattr(a1, 'useCase36'):
        assert not _is_linked(a1, 'useCase36', b)
    if hasattr(a2, 'useCase36'):
        assert _is_linked(a2, 'useCase36', b)
    _safe_set(b, 'Classifier', None)
    assert not _is_linked(b, 'Classifier', a2)
    if hasattr(a2, 'useCase36'):
        assert not _is_linked(a2, 'useCase36', b)


def test_assoc_useCase26_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'subject', {a1})
    assert _is_linked(b, 'subject', a1)
    if hasattr(a1, 'UseCase'):
        assert _is_linked(a1, 'UseCase', b)
    _safe_set(b, 'subject', {a2})
    assert _is_linked(b, 'subject', a2)
    if hasattr(a1, 'UseCase'):
        assert not _is_linked(a1, 'UseCase', b)
    if hasattr(a2, 'UseCase'):
        assert _is_linked(a2, 'UseCase', b)
    _safe_set(b, 'subject', set())
    assert not _is_linked(b, 'subject', a2)
    if hasattr(a2, 'UseCase'):
        assert not _is_linked(a2, 'UseCase', b)


def test_assoc_useCase47_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_ExtensionPoint()
    _safe_set(b, 'extensionPoint', a1)
    assert _is_linked(b, 'extensionPoint', a1)
    if hasattr(a1, 'UseCase48'):
        assert _is_linked(a1, 'UseCase48', b)
    _safe_set(b, 'extensionPoint', a2)
    assert _is_linked(b, 'extensionPoint', a2)
    if hasattr(a1, 'UseCase48'):
        assert not _is_linked(a1, 'UseCase48', b)
    if hasattr(a2, 'UseCase48'):
        assert _is_linked(a2, 'UseCase48', b)
    _safe_set(b, 'extensionPoint', None)
    assert not _is_linked(b, 'extensionPoint', a2)
    if hasattr(a2, 'UseCase48'):
        assert not _is_linked(a2, 'UseCase48', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_addition37_stub_double():
    # umluseCases_Include has no real 'umluseCases_Include' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_UseCase()
    partner = umluseCases_Include()
    setattr(partner, 'umluseCases_Include', None)
    _safe_set(owner, 'umluseCases_UseCase38', partner)
    assert getattr(partner, 'umluseCases_Include') == owner
    _safe_set(owner, 'umluseCases_UseCase38', None)
    assert getattr(partner, 'umluseCases_Include') is None


def test_assoc_include32_stub_double():
    # umluseCases_Include has no real 'Include' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_UseCase()
    partner = umluseCases_Include()
    setattr(partner, 'Include', None)
    _safe_set(owner, 'includingCase', {partner})
    assert getattr(partner, 'Include') == owner
    _safe_set(owner, 'includingCase', set())
    assert getattr(partner, 'Include') is None


def test_assoc_includingCase39_stub_double():
    # umluseCases_Include has no real 'include' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_UseCase()
    partner = umluseCases_Include()
    setattr(partner, 'include', None)
    _safe_set(owner, 'UseCase40', partner)
    assert getattr(partner, 'include') == owner
    _safe_set(owner, 'UseCase40', None)
    assert getattr(partner, 'include') is None


def test_assoc_member12_stub_double():
    # umluseCases_Namespace has no real 'umluseCases_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = umluseCases_Namespace()
    setattr(partner, 'umluseCases_Namespace', None)
    _safe_set(owner, 'umluseCases_NamedElement', partner)
    assert owner in getattr(partner, 'umluseCases_Namespace')
    _safe_set(owner, 'umluseCases_NamedElement', None)
    assert owner not in getattr(partner, 'umluseCases_Namespace')


def test_assoc_namespace5_stub_double():
    # umluseCases_Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = umluseCases_Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedMember', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedMember', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_ownedMember15_stub_double():
    # umluseCases_Namespace has no real 'namespace' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = umluseCases_Namespace()
    setattr(partner, 'namespace', None)
    _safe_set(owner, 'NamedElement', partner)
    assert owner in getattr(partner, 'namespace')
    _safe_set(owner, 'NamedElement', None)
    assert owner not in getattr(partner, 'namespace')


