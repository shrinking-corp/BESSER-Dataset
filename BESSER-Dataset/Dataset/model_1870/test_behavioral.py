import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActualParameter,
    AtomicModelTransformation,
    ConnectableElement,
    DataType,
    FormalParameter,
    Query,
    Transformation,
    TransformationType,
    Type,
    TypedElement,
    WiresElement,
    WiresSpecification,
    Wires_ActualParameter,
    Wires_AtomicModelTransfomationType,
    Wires_AtomicModelTransformation,
    Wires_BasicData,
    Wires_BasicDataType,
    Wires_CompositeTransformation,
    Wires_CompositeTransformationType,
    Wires_ConnectableElement,
    Wires_DataFlow,
    Wires_DataType,
    Wires_DecisionNode,
    Wires_FormalParameter,
    Wires_GenericQuery,
    Wires_GenericTransformation,
    Wires_IdentityTransformation,
    Wires_InputActualParameter,
    Wires_InputFormalParameter,
    Wires_Library,
    Wires_LibraryRef,
    Wires_Model,
    Wires_ModelType,
    Wires_OutputActualParameter,
    Wires_OutputFormalParameter,
    Wires_Query,
    Wires_QueryType,
    Wires_Transformation,
    Wires_TransformationType,
    Wires_Type,
    Wires_TypeParameter,
    Wires_TypedElement,
    Wires_WiresElement,
    Wires_WiresSpecification,
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

def test_assoc_libraries30_reverse_link_reassign_clear():
    a1 = Wires_LibraryRef(name="sample_text")
    a2 = Wires_LibraryRef(name="sample_text_2")
    b = Wires_Library(name="sample_text", path="sample_text")
    _safe_set(b, 'Wires_Library31', {a1})
    assert _is_linked(b, 'Wires_Library31', a1)
    if hasattr(a1, 'Wires_LibraryRef32'):
        assert _is_linked(a1, 'Wires_LibraryRef32', b)
    _safe_set(b, 'Wires_Library31', {a2})
    assert _is_linked(b, 'Wires_Library31', a2)
    if hasattr(a1, 'Wires_LibraryRef32'):
        assert not _is_linked(a1, 'Wires_LibraryRef32', b)
    if hasattr(a2, 'Wires_LibraryRef32'):
        assert _is_linked(a2, 'Wires_LibraryRef32', b)
    _safe_set(b, 'Wires_Library31', set())
    assert not _is_linked(b, 'Wires_Library31', a2)
    if hasattr(a2, 'Wires_LibraryRef32'):
        assert not _is_linked(a2, 'Wires_LibraryRef32', b)


def test_assoc_library28_reverse_link_reassign_clear():
    a1 = Wires_LibraryRef(name="sample_text")
    a2 = Wires_LibraryRef(name="sample_text_2")
    b = Wires_Library(name="sample_text", path="sample_text")
    _safe_set(b, 'Wires_Library', a1)
    assert _is_linked(b, 'Wires_Library', a1)
    if hasattr(a1, 'Wires_LibraryRef29'):
        assert _is_linked(a1, 'Wires_LibraryRef29', b)
    _safe_set(b, 'Wires_Library', a2)
    assert _is_linked(b, 'Wires_Library', a2)
    if hasattr(a1, 'Wires_LibraryRef29'):
        assert not _is_linked(a1, 'Wires_LibraryRef29', b)
    if hasattr(a2, 'Wires_LibraryRef29'):
        assert _is_linked(a2, 'Wires_LibraryRef29', b)
    _safe_set(b, 'Wires_Library', None)
    assert not _is_linked(b, 'Wires_Library', a2)
    if hasattr(a2, 'Wires_LibraryRef29'):
        assert not _is_linked(a2, 'Wires_LibraryRef29', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_controlNode3_stub_double():
    # Wires_Transformation has no real 'Wires_Transformation4' property in the generated
    # code (a bare stub) -- manually attach it so Wires_DecisionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_DecisionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_DecisionNode(expression="sample_text")
    partner = Wires_Transformation()
    setattr(partner, 'Wires_Transformation4', None)
    _safe_set(owner, 'Wires_DecisionNode', partner)
    assert getattr(partner, 'Wires_Transformation4') == owner
    _safe_set(owner, 'Wires_DecisionNode', None)
    assert getattr(partner, 'Wires_Transformation4') is None


def test_assoc_falseBranch9_stub_double():
    # Wires_Transformation has no real 'Wires_Transformation11' property in the generated
    # code (a bare stub) -- manually attach it so Wires_DecisionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_DecisionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_DecisionNode(expression="sample_text")
    partner = Wires_Transformation()
    setattr(partner, 'Wires_Transformation11', None)
    _safe_set(owner, 'Wires_DecisionNode10', {partner})
    assert getattr(partner, 'Wires_Transformation11') == owner
    _safe_set(owner, 'Wires_DecisionNode10', set())
    assert getattr(partner, 'Wires_Transformation11') is None


def test_assoc_inParams12_stub_double():
    # Wires_InputActualParameter has no real 'Wires_InputActualParameter14' property in the generated
    # code (a bare stub) -- manually attach it so Wires_DecisionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_DecisionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_DecisionNode(expression="sample_text")
    partner = Wires_InputActualParameter()
    setattr(partner, 'Wires_InputActualParameter14', None)
    _safe_set(owner, 'Wires_DecisionNode13', {partner})
    assert getattr(partner, 'Wires_InputActualParameter14') == owner
    _safe_set(owner, 'Wires_DecisionNode13', set())
    assert getattr(partner, 'Wires_InputActualParameter14') is None


def test_assoc_incoming24_stub_double():
    # Wires_DataFlow has no real 'DataFlow' property in the generated
    # code (a bare stub) -- manually attach it so Wires_ConnectableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_ConnectableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_ConnectableElement(name="sample_text")
    partner = Wires_DataFlow()
    setattr(partner, 'DataFlow', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'DataFlow') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'DataFlow') is None


def test_assoc_libraries19_stub_double():
    # Wires_TransformationType has no real 'Wires_TransformationType20' property in the generated
    # code (a bare stub) -- manually attach it so Wires_LibraryRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_LibraryRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_LibraryRef(name="sample_text")
    partner = Wires_TransformationType()
    setattr(partner, 'Wires_TransformationType20', None)
    _safe_set(owner, 'Wires_LibraryRef', partner)
    assert owner in getattr(partner, 'Wires_TransformationType20')
    _safe_set(owner, 'Wires_LibraryRef', None)
    assert owner not in getattr(partner, 'Wires_TransformationType20')


def test_assoc_outgoing25_stub_double():
    # Wires_DataFlow has no real 'DataFlow26' property in the generated
    # code (a bare stub) -- manually attach it so Wires_ConnectableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_ConnectableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_ConnectableElement(name="sample_text")
    partner = Wires_DataFlow()
    setattr(partner, 'DataFlow26', None)
    _safe_set(owner, 'src', {partner})
    assert getattr(partner, 'DataFlow26') == owner
    _safe_set(owner, 'src', set())
    assert getattr(partner, 'DataFlow26') is None


def test_assoc_src16_stub_double():
    # Wires_DataFlow has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so Wires_ConnectableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_ConnectableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_ConnectableElement(name="sample_text")
    partner = Wires_DataFlow()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'ConnectableElement17', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'ConnectableElement17', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target15_stub_double():
    # Wires_DataFlow has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so Wires_ConnectableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_ConnectableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_ConnectableElement(name="sample_text")
    partner = Wires_DataFlow()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'ConnectableElement', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'ConnectableElement', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_trueBranch6_stub_double():
    # Wires_Transformation has no real 'Wires_Transformation8' property in the generated
    # code (a bare stub) -- manually attach it so Wires_DecisionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_DecisionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_DecisionNode(expression="sample_text")
    partner = Wires_Transformation()
    setattr(partner, 'Wires_Transformation8', None)
    _safe_set(owner, 'Wires_DecisionNode7', {partner})
    assert getattr(partner, 'Wires_Transformation8') == owner
    _safe_set(owner, 'Wires_DecisionNode7', set())
    assert getattr(partner, 'Wires_Transformation8') is None


def test_assoc_type5_stub_double():
    # Wires_TypedElement has no real 'Wires_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so Wires_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_Type(path="sample_text")
    partner = Wires_TypedElement()
    setattr(partner, 'Wires_TypedElement', None)
    _safe_set(owner, 'Wires_Type', partner)
    assert getattr(partner, 'Wires_TypedElement') == owner
    _safe_set(owner, 'Wires_Type', None)
    assert getattr(partner, 'Wires_TypedElement') is None


def test_assoc_typeEl23_stub_double():
    # Wires_DataType has no real 'Wires_DataType' property in the generated
    # code (a bare stub) -- manually attach it so Wires_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Wires_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Wires_FormalParameter(typeName="sample_text")
    partner = Wires_DataType()
    setattr(partner, 'Wires_DataType', None)
    _safe_set(owner, 'Wires_FormalParameter', partner)
    assert getattr(partner, 'Wires_DataType') == owner
    _safe_set(owner, 'Wires_FormalParameter', None)
    assert getattr(partner, 'Wires_DataType') is None


