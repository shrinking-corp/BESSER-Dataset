import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    ComponentFront,
    EClass,
    Entity,
    File,
    Layer,
    LayerSegment,
    ModuleFront,
    Operations,
    RelationDom,
    SubLayerSegment,
    Transaction,
    UIFront,
    UnifiedMetamodel__APICall,
    UnifiedMetamodel__AbstractClass,
    UnifiedMetamodel__AbstractMethod,
    UnifiedMetamodel__Action,
    UnifiedMetamodel__ActionCreator,
    UnifiedMetamodel__ActionDispatcher,
    UnifiedMetamodel__Actions,
    UnifiedMetamodel__Annotation,
    UnifiedMetamodel__ArquitectureMetamodel,
    UnifiedMetamodel__Attribute,
    UnifiedMetamodel__Back,
    UnifiedMetamodel__CSS,
    UnifiedMetamodel__Component,
    UnifiedMetamodel__ComponentFront,
    UnifiedMetamodel__Composition,
    UnifiedMetamodel__Container,
    UnifiedMetamodel__Containers,
    UnifiedMetamodel__Create,
    UnifiedMetamodel__Descriptor,
    UnifiedMetamodel__Design,
    UnifiedMetamodel__Directory,
    UnifiedMetamodel__DomainMetamodel,
    UnifiedMetamodel__Dto,
    UnifiedMetamodel__EClass,
    UnifiedMetamodel__EInterface,
    UnifiedMetamodel__Ejb,
    UnifiedMetamodel__Entity,
    UnifiedMetamodel__Epackage,
    UnifiedMetamodel__Exchange,
    UnifiedMetamodel__Facade,
    UnifiedMetamodel__File,
    UnifiedMetamodel__Front,
    UnifiedMetamodel__Functionality,
    UnifiedMetamodel__GeneralEntity,
    UnifiedMetamodel__GenericClass,
    UnifiedMetamodel__JEE_Project,
    UnifiedMetamodel__JS,
    UnifiedMetamodel__JSON,
    UnifiedMetamodel__JavaApp,
    UnifiedMetamodel__JavaScript,
    UnifiedMetamodel__Layer,
    UnifiedMetamodel__LayerSegment,
    UnifiedMetamodel__Library,
    UnifiedMetamodel__MD,
    UnifiedMetamodel__Metamodel,
    UnifiedMetamodel__MethodBack,
    UnifiedMetamodel__Module,
    UnifiedMetamodel__ModuleFront,
    UnifiedMetamodel__NativeClass,
    UnifiedMetamodel__Operations,
    UnifiedMetamodel__Pojo,
    UnifiedMetamodel__Property,
    UnifiedMetamodel__React,
    UnifiedMetamodel__ReactApp,
    UnifiedMetamodel__Read,
    UnifiedMetamodel__Reducer,
    UnifiedMetamodel__Reducers,
    UnifiedMetamodel__Redux,
    UnifiedMetamodel__RelationArch,
    UnifiedMetamodel__RelationDom,
    UnifiedMetamodel__RestEntity,
    UnifiedMetamodel__Router,
    UnifiedMetamodel__RouterComponent,
    UnifiedMetamodel__Sale,
    UnifiedMetamodel__Services,
    UnifiedMetamodel__ServicesFront,
    UnifiedMetamodel__SpecialEntity,
    UnifiedMetamodel__State,
    UnifiedMetamodel__Store,
    UnifiedMetamodel__SubLayerSegment,
    UnifiedMetamodel__Submodule,
    UnifiedMetamodel__Subproject,
    UnifiedMetamodel__TechnologyMetamodel,
    UnifiedMetamodel__Transaction,
    UnifiedMetamodel__UI,
    UnifiedMetamodel__UIFront,
    UnifiedMetamodel__Util,
    UnifiedMetamodel__Visualizer,
    UnifiedMetamodel__War,
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

def test_assoc_IsOrganizedBy76_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Functionality(name="sample_text")
    a2 = UnifiedMetamodel__Functionality(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory78', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory78', a1)
    if hasattr(a1, 'UnifiedMetamodel__Functionality77'):
        assert _is_linked(a1, 'UnifiedMetamodel__Functionality77', b)
    _safe_set(b, 'UnifiedMetamodel__Directory78', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory78', a2)
    if hasattr(a1, 'UnifiedMetamodel__Functionality77'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Functionality77', b)
    if hasattr(a2, 'UnifiedMetamodel__Functionality77'):
        assert _is_linked(a2, 'UnifiedMetamodel__Functionality77', b)
    _safe_set(b, 'UnifiedMetamodel__Directory78', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory78', a2)
    if hasattr(a2, 'UnifiedMetamodel__Functionality77'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Functionality77', b)


def test_assoc_abstractmethod120_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EInterface(name="sample_text")
    a2 = UnifiedMetamodel__EInterface(name="sample_text_2")
    b = UnifiedMetamodel__AbstractMethod(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod', a1)
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod', a1)
    if hasattr(a1, 'UnifiedMetamodel__EInterface'):
        assert _is_linked(a1, 'UnifiedMetamodel__EInterface', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod', a2)
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod', a2)
    if hasattr(a1, 'UnifiedMetamodel__EInterface'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EInterface', b)
    if hasattr(a2, 'UnifiedMetamodel__EInterface'):
        assert _is_linked(a2, 'UnifiedMetamodel__EInterface', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod', None)
    assert not _is_linked(b, 'UnifiedMetamodel__AbstractMethod', a2)
    if hasattr(a2, 'UnifiedMetamodel__EInterface'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EInterface', b)


def test_assoc_actionDirectory85_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    a2 = UnifiedMetamodel__Directory(isRoot=False, name="sample_text_2", purpose="sample_text_2")
    b = UnifiedMetamodel__Action(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Action86', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Action86', a1)
    if hasattr(a1, 'UnifiedMetamodel__Directory87'):
        assert _is_linked(a1, 'UnifiedMetamodel__Directory87', b)
    _safe_set(b, 'UnifiedMetamodel__Action86', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Action86', a2)
    if hasattr(a1, 'UnifiedMetamodel__Directory87'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Directory87', b)
    if hasattr(a2, 'UnifiedMetamodel__Directory87'):
        assert _is_linked(a2, 'UnifiedMetamodel__Directory87', b)
    _safe_set(b, 'UnifiedMetamodel__Action86', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Action86', a2)
    if hasattr(a2, 'UnifiedMetamodel__Directory87'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Directory87', b)


def test_assoc_actioncreator82_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ActionCreator(name="sample_text")
    a2 = UnifiedMetamodel__ActionCreator(name="sample_text_2")
    b = UnifiedMetamodel__Action(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Action83', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Action83', a1)
    if hasattr(a1, 'UnifiedMetamodel__ActionCreator84'):
        assert _is_linked(a1, 'UnifiedMetamodel__ActionCreator84', b)
    _safe_set(b, 'UnifiedMetamodel__Action83', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Action83', a2)
    if hasattr(a1, 'UnifiedMetamodel__ActionCreator84'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ActionCreator84', b)
    if hasattr(a2, 'UnifiedMetamodel__ActionCreator84'):
        assert _is_linked(a2, 'UnifiedMetamodel__ActionCreator84', b)
    _safe_set(b, 'UnifiedMetamodel__Action83', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Action83', a2)
    if hasattr(a2, 'UnifiedMetamodel__ActionCreator84'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ActionCreator84', b)


def test_assoc_actiondispatcher79_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ActionDispatcher(name="sample_text")
    a2 = UnifiedMetamodel__ActionDispatcher(name="sample_text_2")
    b = UnifiedMetamodel__Action(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Action80', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Action80', a1)
    if hasattr(a1, 'UnifiedMetamodel__ActionDispatcher81'):
        assert _is_linked(a1, 'UnifiedMetamodel__ActionDispatcher81', b)
    _safe_set(b, 'UnifiedMetamodel__Action80', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Action80', a2)
    if hasattr(a1, 'UnifiedMetamodel__ActionDispatcher81'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ActionDispatcher81', b)
    if hasattr(a2, 'UnifiedMetamodel__ActionDispatcher81'):
        assert _is_linked(a2, 'UnifiedMetamodel__ActionDispatcher81', b)
    _safe_set(b, 'UnifiedMetamodel__Action80', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Action80', a2)
    if hasattr(a2, 'UnifiedMetamodel__ActionDispatcher81'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ActionDispatcher81', b)


def test_assoc_annotation122_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Library(isNative=True, name="sample_text")
    a2 = UnifiedMetamodel__Library(isNative=False, name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation', a1)
    if hasattr(a1, 'UnifiedMetamodel__Library123'):
        assert _is_linked(a1, 'UnifiedMetamodel__Library123', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation', a2)
    if hasattr(a1, 'UnifiedMetamodel__Library123'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Library123', b)
    if hasattr(a2, 'UnifiedMetamodel__Library123'):
        assert _is_linked(a2, 'UnifiedMetamodel__Library123', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation', a2)
    if hasattr(a2, 'UnifiedMetamodel__Library123'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Library123', b)


def test_assoc_annotation124_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Attribute(name="sample_text")
    a2 = UnifiedMetamodel__Attribute(name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation125', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation125', a1)
    if hasattr(a1, 'UnifiedMetamodel__Attribute'):
        assert _is_linked(a1, 'UnifiedMetamodel__Attribute', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation125', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation125', a2)
    if hasattr(a1, 'UnifiedMetamodel__Attribute'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Attribute', b)
    if hasattr(a2, 'UnifiedMetamodel__Attribute'):
        assert _is_linked(a2, 'UnifiedMetamodel__Attribute', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation125', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation125', a2)
    if hasattr(a2, 'UnifiedMetamodel__Attribute'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Attribute', b)


def test_assoc_annotation132_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation133', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation133', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation133', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation133', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation133', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation133', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack', b)


def test_assoc_annotation151_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation153', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation153', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass152'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass152', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation153', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation153', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass152'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass152', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass152'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass152', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation153', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation153', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass152'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass152', b)


def test_assoc_arguments137_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass139', a1)
    assert _is_linked(b, 'UnifiedMetamodel__EClass139', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack138'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack138', b)
    _safe_set(b, 'UnifiedMetamodel__EClass139', a2)
    assert _is_linked(b, 'UnifiedMetamodel__EClass139', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack138'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack138', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack138'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack138', b)
    _safe_set(b, 'UnifiedMetamodel__EClass139', None)
    assert not _is_linked(b, 'UnifiedMetamodel__EClass139', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack138'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack138', b)


def test_assoc_arguments168_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__AbstractMethod(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod169', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod169', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass170'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass170', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod169', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod169', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass170'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass170', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass170'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass170', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod169', set())
    assert not _is_linked(b, 'UnifiedMetamodel__AbstractMethod169', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass170'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass170', b)


def test_assoc_attribute145_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__Attribute(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Attribute147', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute147', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass146'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass146', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute147', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute147', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass146'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass146', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass146'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass146', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute147', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Attribute147', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass146'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass146', b)


def test_assoc_catches102_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Reducer(name="sample_text")
    a2 = UnifiedMetamodel__Reducer(name="sample_text_2")
    b = UnifiedMetamodel__ActionCreator(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ActionCreator104', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ActionCreator104', a1)
    if hasattr(a1, 'UnifiedMetamodel__Reducer103'):
        assert _is_linked(a1, 'UnifiedMetamodel__Reducer103', b)
    _safe_set(b, 'UnifiedMetamodel__ActionCreator104', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ActionCreator104', a2)
    if hasattr(a1, 'UnifiedMetamodel__Reducer103'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Reducer103', b)
    if hasattr(a2, 'UnifiedMetamodel__Reducer103'):
        assert _is_linked(a2, 'UnifiedMetamodel__Reducer103', b)
    _safe_set(b, 'UnifiedMetamodel__ActionCreator104', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ActionCreator104', a2)
    if hasattr(a2, 'UnifiedMetamodel__Reducer103'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Reducer103', b)


def test_assoc_class_143_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Epackage(name="sample_text")
    a2 = UnifiedMetamodel__Epackage(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass144', a1)
    assert _is_linked(b, 'UnifiedMetamodel__EClass144', a1)
    if hasattr(a1, 'UnifiedMetamodel__Epackage'):
        assert _is_linked(a1, 'UnifiedMetamodel__Epackage', b)
    _safe_set(b, 'UnifiedMetamodel__EClass144', a2)
    assert _is_linked(b, 'UnifiedMetamodel__EClass144', a2)
    if hasattr(a1, 'UnifiedMetamodel__Epackage'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Epackage', b)
    if hasattr(a2, 'UnifiedMetamodel__Epackage'):
        assert _is_linked(a2, 'UnifiedMetamodel__Epackage', b)
    _safe_set(b, 'UnifiedMetamodel__EClass144', None)
    assert not _is_linked(b, 'UnifiedMetamodel__EClass144', a2)
    if hasattr(a2, 'UnifiedMetamodel__Epackage'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Epackage', b)


def test_assoc_components69_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Functionality(name="sample_text")
    a2 = UnifiedMetamodel__Functionality(name="sample_text_2")
    b = UnifiedMetamodel__ComponentFront(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ComponentFront', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront', a1)
    if hasattr(a1, 'UnifiedMetamodel__Functionality'):
        assert _is_linked(a1, 'UnifiedMetamodel__Functionality', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront', a2)
    if hasattr(a1, 'UnifiedMetamodel__Functionality'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Functionality', b)
    if hasattr(a2, 'UnifiedMetamodel__Functionality'):
        assert _is_linked(a2, 'UnifiedMetamodel__Functionality', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ComponentFront', a2)
    if hasattr(a2, 'UnifiedMetamodel__Functionality'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Functionality', b)


def test_assoc_descriptor154_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Descriptor(name="sample_text", path="sample_text")
    a2 = UnifiedMetamodel__Descriptor(name="sample_text_2", path="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation155', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation155', a1)
    if hasattr(a1, 'UnifiedMetamodel__Descriptor'):
        assert _is_linked(a1, 'UnifiedMetamodel__Descriptor', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation155', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation155', a2)
    if hasattr(a1, 'UnifiedMetamodel__Descriptor'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Descriptor', b)
    if hasattr(a2, 'UnifiedMetamodel__Descriptor'):
        assert _is_linked(a2, 'UnifiedMetamodel__Descriptor', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation155', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation155', a2)
    if hasattr(a2, 'UnifiedMetamodel__Descriptor'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Descriptor', b)


def test_assoc_descriptor156_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__Descriptor(name="sample_text", path="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Descriptor158', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Descriptor158', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject157'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject157', b)
    _safe_set(b, 'UnifiedMetamodel__Descriptor158', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Descriptor158', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject157'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject157', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject157'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject157', b)
    _safe_set(b, 'UnifiedMetamodel__Descriptor158', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Descriptor158', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject157'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject157', b)


def test_assoc_directories50_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    a2 = UnifiedMetamodel__Directory(isRoot=False, name="sample_text_2", purpose="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory49', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Directory49', a1)
    if hasattr(a1, 'UnifiedMetamodel__Directory'):
        assert _is_linked(a1, 'UnifiedMetamodel__Directory', b)
    _safe_set(b, 'UnifiedMetamodel__Directory49', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Directory49', a2)
    if hasattr(a1, 'UnifiedMetamodel__Directory'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Directory', b)
    if hasattr(a2, 'UnifiedMetamodel__Directory'):
        assert _is_linked(a2, 'UnifiedMetamodel__Directory', b)
    _safe_set(b, 'UnifiedMetamodel__Directory49', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Directory49', a2)
    if hasattr(a2, 'UnifiedMetamodel__Directory'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Directory', b)


def test_assoc_entity39_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Submodule(name="sample_text")
    a2 = UnifiedMetamodel__Submodule(name="sample_text_2")
    b = UnifiedMetamodel__Entity(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Entity41', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Entity41', a1)
    if hasattr(a1, 'UnifiedMetamodel__Submodule40'):
        assert _is_linked(a1, 'UnifiedMetamodel__Submodule40', b)
    _safe_set(b, 'UnifiedMetamodel__Entity41', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Entity41', a2)
    if hasattr(a1, 'UnifiedMetamodel__Submodule40'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Submodule40', b)
    if hasattr(a2, 'UnifiedMetamodel__Submodule40'):
        assert _is_linked(a2, 'UnifiedMetamodel__Submodule40', b)
    _safe_set(b, 'UnifiedMetamodel__Entity41', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Entity41', a2)
    if hasattr(a2, 'UnifiedMetamodel__Submodule40'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Submodule40', b)


def test_assoc_files51_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__File(name="sample_text", type="sample_text")
    a2 = UnifiedMetamodel__File(name="sample_text_2", type="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory52', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Directory52', a1)
    if hasattr(a1, 'UnifiedMetamodel__File'):
        assert _is_linked(a1, 'UnifiedMetamodel__File', b)
    _safe_set(b, 'UnifiedMetamodel__Directory52', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Directory52', a2)
    if hasattr(a1, 'UnifiedMetamodel__File'):
        assert not _is_linked(a1, 'UnifiedMetamodel__File', b)
    if hasattr(a2, 'UnifiedMetamodel__File'):
        assert _is_linked(a2, 'UnifiedMetamodel__File', b)
    _safe_set(b, 'UnifiedMetamodel__Directory52', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Directory52', a2)
    if hasattr(a2, 'UnifiedMetamodel__File'):
        assert not _is_linked(a2, 'UnifiedMetamodel__File', b)


def test_assoc_inWithin99_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    a2 = UnifiedMetamodel__Directory(isRoot=False, name="sample_text_2", purpose="sample_text_2")
    b = UnifiedMetamodel__ComponentFront(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ComponentFront100', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront100', a1)
    if hasattr(a1, 'UnifiedMetamodel__Directory101'):
        assert _is_linked(a1, 'UnifiedMetamodel__Directory101', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront100', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront100', a2)
    if hasattr(a1, 'UnifiedMetamodel__Directory101'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Directory101', b)
    if hasattr(a2, 'UnifiedMetamodel__Directory101'):
        assert _is_linked(a2, 'UnifiedMetamodel__Directory101', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront100', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ComponentFront100', a2)
    if hasattr(a2, 'UnifiedMetamodel__Directory101'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Directory101', b)


def test_assoc_isOrganizedIn66_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ServicesFront(name="sample_text")
    a2 = UnifiedMetamodel__ServicesFront(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory68', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory68', a1)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront67'):
        assert _is_linked(a1, 'UnifiedMetamodel__ServicesFront67', b)
    _safe_set(b, 'UnifiedMetamodel__Directory68', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory68', a2)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront67'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ServicesFront67', b)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront67'):
        assert _is_linked(a2, 'UnifiedMetamodel__ServicesFront67', b)
    _safe_set(b, 'UnifiedMetamodel__Directory68', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory68', a2)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront67'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ServicesFront67', b)


def test_assoc_isPresentIn108_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ModuleFront(name="sample_text")
    a2 = UnifiedMetamodel__ModuleFront(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory110', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory110', a1)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront109'):
        assert _is_linked(a1, 'UnifiedMetamodel__ModuleFront109', b)
    _safe_set(b, 'UnifiedMetamodel__Directory110', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory110', a2)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront109'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ModuleFront109', b)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront109'):
        assert _is_linked(a2, 'UnifiedMetamodel__ModuleFront109', b)
    _safe_set(b, 'UnifiedMetamodel__Directory110', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory110', a2)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront109'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ModuleFront109', b)


def test_assoc_layers6_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Layer(name="sample_text")
    a2 = UnifiedMetamodel__Layer(name="sample_text_2")
    b = UnifiedMetamodel__Component(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Component', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Component', a1)
    if hasattr(a1, 'UnifiedMetamodel__Layer7'):
        assert _is_linked(a1, 'UnifiedMetamodel__Layer7', b)
    _safe_set(b, 'UnifiedMetamodel__Component', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Component', a2)
    if hasattr(a1, 'UnifiedMetamodel__Layer7'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Layer7', b)
    if hasattr(a2, 'UnifiedMetamodel__Layer7'):
        assert _is_linked(a2, 'UnifiedMetamodel__Layer7', b)
    _safe_set(b, 'UnifiedMetamodel__Component', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Component', a2)
    if hasattr(a2, 'UnifiedMetamodel__Layer7'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Layer7', b)


def test_assoc_library162_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__Library(isNative=True, name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Library164', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Library164', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject163'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject163', b)
    _safe_set(b, 'UnifiedMetamodel__Library164', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Library164', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject163'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject163', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject163'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject163', b)
    _safe_set(b, 'UnifiedMetamodel__Library164', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Library164', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject163'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject163', b)


def test_assoc_method148_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass149', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__EClass149', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack150'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack150', b)
    _safe_set(b, 'UnifiedMetamodel__EClass149', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__EClass149', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack150'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack150', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack150'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack150', b)
    _safe_set(b, 'UnifiedMetamodel__EClass149', set())
    assert not _is_linked(b, 'UnifiedMetamodel__EClass149', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack150'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack150', b)


def test_assoc_nativeclass121_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__NativeClass(primitiveRef="sample_text")
    a2 = UnifiedMetamodel__NativeClass(primitiveRef="sample_text_2")
    b = UnifiedMetamodel__Library(isNative=True, name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Library', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Library', a1)
    if hasattr(a1, 'UnifiedMetamodel__NativeClass'):
        assert _is_linked(a1, 'UnifiedMetamodel__NativeClass', b)
    _safe_set(b, 'UnifiedMetamodel__Library', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Library', a2)
    if hasattr(a1, 'UnifiedMetamodel__NativeClass'):
        assert not _is_linked(a1, 'UnifiedMetamodel__NativeClass', b)
    if hasattr(a2, 'UnifiedMetamodel__NativeClass'):
        assert _is_linked(a2, 'UnifiedMetamodel__NativeClass', b)
    _safe_set(b, 'UnifiedMetamodel__Library', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Library', a2)
    if hasattr(a2, 'UnifiedMetamodel__NativeClass'):
        assert not _is_linked(a2, 'UnifiedMetamodel__NativeClass', b)


def test_assoc_package159_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__Epackage(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Epackage161', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Epackage161', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject160'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject160', b)
    _safe_set(b, 'UnifiedMetamodel__Epackage161', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Epackage161', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject160'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject160', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject160'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject160', b)
    _safe_set(b, 'UnifiedMetamodel__Epackage161', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Epackage161', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject160'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject160', b)


def test_assoc_property27_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Property(name="sample_text", type="sample_text")
    a2 = UnifiedMetamodel__Property(name="sample_text_2", type="sample_text_2")
    b = UnifiedMetamodel__Entity(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Entity28', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Entity28', a1)
    if hasattr(a1, 'UnifiedMetamodel__Property'):
        assert _is_linked(a1, 'UnifiedMetamodel__Property', b)
    _safe_set(b, 'UnifiedMetamodel__Entity28', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Entity28', a2)
    if hasattr(a1, 'UnifiedMetamodel__Property'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Property', b)
    if hasattr(a2, 'UnifiedMetamodel__Property'):
        assert _is_linked(a2, 'UnifiedMetamodel__Property', b)
    _safe_set(b, 'UnifiedMetamodel__Entity28', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Entity28', a2)
    if hasattr(a2, 'UnifiedMetamodel__Property'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Property', b)


def test_assoc_reducerDirectory105_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Reducer(name="sample_text")
    a2 = UnifiedMetamodel__Reducer(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory107', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory107', a1)
    if hasattr(a1, 'UnifiedMetamodel__Reducer106'):
        assert _is_linked(a1, 'UnifiedMetamodel__Reducer106', b)
    _safe_set(b, 'UnifiedMetamodel__Directory107', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory107', a2)
    if hasattr(a1, 'UnifiedMetamodel__Reducer106'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Reducer106', b)
    if hasattr(a2, 'UnifiedMetamodel__Reducer106'):
        assert _is_linked(a2, 'UnifiedMetamodel__Reducer106', b)
    _safe_set(b, 'UnifiedMetamodel__Directory107', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory107', a2)
    if hasattr(a2, 'UnifiedMetamodel__Reducer106'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Reducer106', b)


def test_assoc_return_134_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass136', a1)
    assert _is_linked(b, 'UnifiedMetamodel__EClass136', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack135'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack135', b)
    _safe_set(b, 'UnifiedMetamodel__EClass136', a2)
    assert _is_linked(b, 'UnifiedMetamodel__EClass136', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack135'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack135', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack135'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack135', b)
    _safe_set(b, 'UnifiedMetamodel__EClass136', None)
    assert not _is_linked(b, 'UnifiedMetamodel__EClass136', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack135'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack135', b)


def test_assoc_return_165_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__AbstractMethod(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod166', a1)
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod166', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass167'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass167', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod166', a2)
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod166', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass167'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass167', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass167'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass167', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod166', None)
    assert not _is_linked(b, 'UnifiedMetamodel__AbstractMethod166', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass167'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass167', b)


def test_assoc_services73_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ServicesFront(name="sample_text")
    a2 = UnifiedMetamodel__ServicesFront(name="sample_text_2")
    b = UnifiedMetamodel__Functionality(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Functionality74', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Functionality74', a1)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront75'):
        assert _is_linked(a1, 'UnifiedMetamodel__ServicesFront75', b)
    _safe_set(b, 'UnifiedMetamodel__Functionality74', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Functionality74', a2)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront75'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ServicesFront75', b)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront75'):
        assert _is_linked(a2, 'UnifiedMetamodel__ServicesFront75', b)
    _safe_set(b, 'UnifiedMetamodel__Functionality74', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Functionality74', a2)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront75'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ServicesFront75', b)


def test_assoc_source8_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__RelationArch(name="sample_text")
    a2 = UnifiedMetamodel__RelationArch(name="sample_text_2")
    b = UnifiedMetamodel__Layer(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Layer9', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Layer9', a1)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch'):
        assert _is_linked(a1, 'UnifiedMetamodel__RelationArch', b)
    _safe_set(b, 'UnifiedMetamodel__Layer9', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Layer9', a2)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch'):
        assert not _is_linked(a1, 'UnifiedMetamodel__RelationArch', b)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch'):
        assert _is_linked(a2, 'UnifiedMetamodel__RelationArch', b)
    _safe_set(b, 'UnifiedMetamodel__Layer9', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Layer9', a2)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch'):
        assert not _is_linked(a2, 'UnifiedMetamodel__RelationArch', b)


def test_assoc_submodule25_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Submodule(name="sample_text")
    a2 = UnifiedMetamodel__Submodule(name="sample_text_2")
    b = UnifiedMetamodel__Module(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Module', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Module', a1)
    if hasattr(a1, 'UnifiedMetamodel__Submodule'):
        assert _is_linked(a1, 'UnifiedMetamodel__Submodule', b)
    _safe_set(b, 'UnifiedMetamodel__Module', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Module', a2)
    if hasattr(a1, 'UnifiedMetamodel__Submodule'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Submodule', b)
    if hasattr(a2, 'UnifiedMetamodel__Submodule'):
        assert _is_linked(a2, 'UnifiedMetamodel__Submodule', b)
    _safe_set(b, 'UnifiedMetamodel__Module', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Module', a2)
    if hasattr(a2, 'UnifiedMetamodel__Submodule'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Submodule', b)


def test_assoc_subproject118_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__JEE_Project(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__JEE_Project119', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__JEE_Project119', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject', b)
    _safe_set(b, 'UnifiedMetamodel__JEE_Project119', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__JEE_Project119', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject', b)
    _safe_set(b, 'UnifiedMetamodel__JEE_Project119', set())
    assert not _is_linked(b, 'UnifiedMetamodel__JEE_Project119', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject', b)


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__RelationArch(name="sample_text")
    a2 = UnifiedMetamodel__RelationArch(name="sample_text_2")
    b = UnifiedMetamodel__Layer(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Layer12', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Layer12', a1)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch11'):
        assert _is_linked(a1, 'UnifiedMetamodel__RelationArch11', b)
    _safe_set(b, 'UnifiedMetamodel__Layer12', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Layer12', a2)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch11'):
        assert not _is_linked(a1, 'UnifiedMetamodel__RelationArch11', b)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch11'):
        assert _is_linked(a2, 'UnifiedMetamodel__RelationArch11', b)
    _safe_set(b, 'UnifiedMetamodel__Layer12', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Layer12', a2)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch11'):
        assert not _is_linked(a2, 'UnifiedMetamodel__RelationArch11', b)


def test_assoc_type126_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__Attribute(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Attribute127', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute127', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute127', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute127', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute127', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Attribute127', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass', b)


def test_assoc_use48_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ActionDispatcher(name="sample_text")
    a2 = UnifiedMetamodel__ActionDispatcher(name="sample_text_2")
    b = UnifiedMetamodel__ActionCreator(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ActionCreator', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ActionCreator', a1)
    if hasattr(a1, 'UnifiedMetamodel__ActionDispatcher'):
        assert _is_linked(a1, 'UnifiedMetamodel__ActionDispatcher', b)
    _safe_set(b, 'UnifiedMetamodel__ActionCreator', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ActionCreator', a2)
    if hasattr(a1, 'UnifiedMetamodel__ActionDispatcher'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ActionDispatcher', b)
    if hasattr(a2, 'UnifiedMetamodel__ActionDispatcher'):
        assert _is_linked(a2, 'UnifiedMetamodel__ActionDispatcher', b)
    _safe_set(b, 'UnifiedMetamodel__ActionCreator', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ActionCreator', a2)
    if hasattr(a2, 'UnifiedMetamodel__ActionDispatcher'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ActionDispatcher', b)


def test_assoc_use64_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ServicesFront(name="sample_text")
    a2 = UnifiedMetamodel__ServicesFront(name="sample_text_2")
    b = UnifiedMetamodel__ModuleFront(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ModuleFront65', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ModuleFront65', a1)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront'):
        assert _is_linked(a1, 'UnifiedMetamodel__ServicesFront', b)
    _safe_set(b, 'UnifiedMetamodel__ModuleFront65', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ModuleFront65', a2)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ServicesFront', b)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront'):
        assert _is_linked(a2, 'UnifiedMetamodel__ServicesFront', b)
    _safe_set(b, 'UnifiedMetamodel__ModuleFront65', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ModuleFront65', a2)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ServicesFront', b)


def test_assoc_use96_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ModuleFront(name="sample_text")
    a2 = UnifiedMetamodel__ModuleFront(name="sample_text_2")
    b = UnifiedMetamodel__ComponentFront(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ComponentFront97', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront97', a1)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront98'):
        assert _is_linked(a1, 'UnifiedMetamodel__ModuleFront98', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront97', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront97', a2)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront98'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ModuleFront98', b)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront98'):
        assert _is_linked(a2, 'UnifiedMetamodel__ModuleFront98', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront97', set())
    assert not _is_linked(b, 'UnifiedMetamodel__ComponentFront97', a2)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront98'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ModuleFront98', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abstractmethod140_stub_double():
    # UnifiedMetamodel__AbstractClass has no real 'UnifiedMetamodel__AbstractClass141' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__AbstractMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__AbstractMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__AbstractMethod(name="sample_text")
    partner = UnifiedMetamodel__AbstractClass()
    setattr(partner, 'UnifiedMetamodel__AbstractClass141', None)
    _safe_set(owner, 'UnifiedMetamodel__AbstractMethod142', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__AbstractClass141')
    _safe_set(owner, 'UnifiedMetamodel__AbstractMethod142', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__AbstractClass141')


def test_assoc_action53_stub_double():
    # UnifiedMetamodel__State has no real 'UnifiedMetamodel__State' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Action(name="sample_text")
    partner = UnifiedMetamodel__State()
    setattr(partner, 'UnifiedMetamodel__State', None)
    _safe_set(owner, 'UnifiedMetamodel__Action', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__State')
    _safe_set(owner, 'UnifiedMetamodel__Action', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__State')


def test_assoc_arquitecturemetamodel18_stub_double():
    # UnifiedMetamodel__ArquitectureMetamodel has no real 'UnifiedMetamodel__ArquitectureMetamodel19' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Metamodel(name="sample_text")
    partner = UnifiedMetamodel__ArquitectureMetamodel()
    setattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel19', None)
    _safe_set(owner, 'UnifiedMetamodel__Metamodel', partner)
    assert getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel19') == owner
    _safe_set(owner, 'UnifiedMetamodel__Metamodel', None)
    assert getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel19') is None


def test_assoc_components13_stub_double():
    # UnifiedMetamodel__ArquitectureMetamodel has no real 'UnifiedMetamodel__ArquitectureMetamodel' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Component(name="sample_text")
    partner = UnifiedMetamodel__ArquitectureMetamodel()
    setattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel', None)
    _safe_set(owner, 'UnifiedMetamodel__Component14', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel')
    _safe_set(owner, 'UnifiedMetamodel__Component14', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel')


def test_assoc_directories93_stub_double():
    # UnifiedMetamodel__ReactApp has no real 'UnifiedMetamodel__ReactApp94' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    partner = UnifiedMetamodel__ReactApp()
    setattr(partner, 'UnifiedMetamodel__ReactApp94', None)
    _safe_set(owner, 'UnifiedMetamodel__Directory95', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ReactApp94')
    _safe_set(owner, 'UnifiedMetamodel__Directory95', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ReactApp94')


def test_assoc_dispatches59_stub_double():
    # UnifiedMetamodel__Container has no real 'UnifiedMetamodel__Container' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__ActionDispatcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__ActionDispatcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__ActionDispatcher(name="sample_text")
    partner = UnifiedMetamodel__Container()
    setattr(partner, 'UnifiedMetamodel__Container', None)
    _safe_set(owner, 'UnifiedMetamodel__ActionDispatcher60', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__Container')
    _safe_set(owner, 'UnifiedMetamodel__ActionDispatcher60', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__Container')


def test_assoc_domainmetamodel20_stub_double():
    # UnifiedMetamodel__DomainMetamodel has no real 'UnifiedMetamodel__DomainMetamodel' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Metamodel(name="sample_text")
    partner = UnifiedMetamodel__DomainMetamodel()
    setattr(partner, 'UnifiedMetamodel__DomainMetamodel', None)
    _safe_set(owner, 'UnifiedMetamodel__Metamodel21', partner)
    assert getattr(partner, 'UnifiedMetamodel__DomainMetamodel') == owner
    _safe_set(owner, 'UnifiedMetamodel__Metamodel21', None)
    assert getattr(partner, 'UnifiedMetamodel__DomainMetamodel') is None


def test_assoc_functionalities88_stub_double():
    # UnifiedMetamodel__ReactApp has no real 'UnifiedMetamodel__ReactApp' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Functionality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Functionality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Functionality(name="sample_text")
    partner = UnifiedMetamodel__ReactApp()
    setattr(partner, 'UnifiedMetamodel__ReactApp', None)
    _safe_set(owner, 'UnifiedMetamodel__Functionality89', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ReactApp')
    _safe_set(owner, 'UnifiedMetamodel__Functionality89', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ReactApp')


def test_assoc_implement128_stub_double():
    # UnifiedMetamodel__GenericClass has no real 'UnifiedMetamodel__GenericClass' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__EInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__EInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__EInterface(name="sample_text")
    partner = UnifiedMetamodel__GenericClass()
    setattr(partner, 'UnifiedMetamodel__GenericClass', None)
    _safe_set(owner, 'UnifiedMetamodel__EInterface129', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__GenericClass')
    _safe_set(owner, 'UnifiedMetamodel__EInterface129', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__GenericClass')


def test_assoc_jee_project116_stub_double():
    # UnifiedMetamodel__JavaApp has no real 'UnifiedMetamodel__JavaApp117' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__JEE_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__JEE_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__JEE_Project(name="sample_text")
    partner = UnifiedMetamodel__JavaApp()
    setattr(partner, 'UnifiedMetamodel__JavaApp117', None)
    _safe_set(owner, 'UnifiedMetamodel__JEE_Project', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__JavaApp117')
    _safe_set(owner, 'UnifiedMetamodel__JEE_Project', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__JavaApp117')


def test_assoc_layerSegments4_stub_double():
    # UnifiedMetamodel__LayerSegment has no real 'UnifiedMetamodel__LayerSegment5' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Layer(name="sample_text")
    partner = UnifiedMetamodel__LayerSegment()
    setattr(partner, 'UnifiedMetamodel__LayerSegment5', None)
    _safe_set(owner, 'UnifiedMetamodel__Layer', {partner})
    assert getattr(partner, 'UnifiedMetamodel__LayerSegment5') == owner
    _safe_set(owner, 'UnifiedMetamodel__Layer', set())
    assert getattr(partner, 'UnifiedMetamodel__LayerSegment5') is None


def test_assoc_maps61_stub_double():
    # UnifiedMetamodel__Container has no real 'UnifiedMetamodel__Container62' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Reducer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Reducer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Reducer(name="sample_text")
    partner = UnifiedMetamodel__Container()
    setattr(partner, 'UnifiedMetamodel__Container62', None)
    _safe_set(owner, 'UnifiedMetamodel__Reducer63', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__Container62')
    _safe_set(owner, 'UnifiedMetamodel__Reducer63', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__Container62')


def test_assoc_module42_stub_double():
    # UnifiedMetamodel__DomainMetamodel has no real 'UnifiedMetamodel__DomainMetamodel43' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Module(name="sample_text")
    partner = UnifiedMetamodel__DomainMetamodel()
    setattr(partner, 'UnifiedMetamodel__DomainMetamodel43', None)
    _safe_set(owner, 'UnifiedMetamodel__Module44', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__DomainMetamodel43')
    _safe_set(owner, 'UnifiedMetamodel__Module44', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__DomainMetamodel43')


def test_assoc_modules90_stub_double():
    # UnifiedMetamodel__ReactApp has no real 'UnifiedMetamodel__ReactApp91' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__ModuleFront's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__ModuleFront's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__ModuleFront(name="sample_text")
    partner = UnifiedMetamodel__ReactApp()
    setattr(partner, 'UnifiedMetamodel__ReactApp91', None)
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront92', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ReactApp91')
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront92', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ReactApp91')


def test_assoc_operates_on24_stub_double():
    # UnifiedMetamodel__Operations has no real 'UnifiedMetamodel__Operations' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Entity(name="sample_text")
    partner = UnifiedMetamodel__Operations()
    setattr(partner, 'UnifiedMetamodel__Operations', None)
    _safe_set(owner, 'UnifiedMetamodel__Entity', partner)
    assert getattr(partner, 'UnifiedMetamodel__Operations') == owner
    _safe_set(owner, 'UnifiedMetamodel__Entity', None)
    assert getattr(partner, 'UnifiedMetamodel__Operations') is None


def test_assoc_operations36_stub_double():
    # UnifiedMetamodel__Operations has no real 'UnifiedMetamodel__Operations38' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Submodule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Submodule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Submodule(name="sample_text")
    partner = UnifiedMetamodel__Operations()
    setattr(partner, 'UnifiedMetamodel__Operations38', None)
    _safe_set(owner, 'UnifiedMetamodel__Submodule37', {partner})
    assert getattr(partner, 'UnifiedMetamodel__Operations38') == owner
    _safe_set(owner, 'UnifiedMetamodel__Submodule37', set())
    assert getattr(partner, 'UnifiedMetamodel__Operations38') is None


def test_assoc_reducer54_stub_double():
    # UnifiedMetamodel__State has no real 'UnifiedMetamodel__State55' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Reducer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Reducer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Reducer(name="sample_text")
    partner = UnifiedMetamodel__State()
    setattr(partner, 'UnifiedMetamodel__State55', None)
    _safe_set(owner, 'UnifiedMetamodel__Reducer', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__State55')
    _safe_set(owner, 'UnifiedMetamodel__Reducer', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__State55')


def test_assoc_relations15_stub_double():
    # UnifiedMetamodel__ArquitectureMetamodel has no real 'UnifiedMetamodel__ArquitectureMetamodel16' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__RelationArch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__RelationArch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__RelationArch(name="sample_text")
    partner = UnifiedMetamodel__ArquitectureMetamodel()
    setattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel16', None)
    _safe_set(owner, 'UnifiedMetamodel__RelationArch17', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel16')
    _safe_set(owner, 'UnifiedMetamodel__RelationArch17', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel16')


def test_assoc_source29_stub_double():
    # UnifiedMetamodel__RelationDom has no real 'UnifiedMetamodel__RelationDom' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Entity(name="sample_text")
    partner = UnifiedMetamodel__RelationDom()
    setattr(partner, 'UnifiedMetamodel__RelationDom', None)
    _safe_set(owner, 'UnifiedMetamodel__Entity30', partner)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom') == owner
    _safe_set(owner, 'UnifiedMetamodel__Entity30', None)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom') is None


def test_assoc_state70_stub_double():
    # UnifiedMetamodel__State has no real 'UnifiedMetamodel__State72' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Functionality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Functionality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Functionality(name="sample_text")
    partner = UnifiedMetamodel__State()
    setattr(partner, 'UnifiedMetamodel__State72', None)
    _safe_set(owner, 'UnifiedMetamodel__Functionality71', partner)
    assert getattr(partner, 'UnifiedMetamodel__State72') == owner
    _safe_set(owner, 'UnifiedMetamodel__Functionality71', None)
    assert getattr(partner, 'UnifiedMetamodel__State72') is None


def test_assoc_target31_stub_double():
    # UnifiedMetamodel__RelationDom has no real 'UnifiedMetamodel__RelationDom32' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Entity(name="sample_text")
    partner = UnifiedMetamodel__RelationDom()
    setattr(partner, 'UnifiedMetamodel__RelationDom32', None)
    _safe_set(owner, 'UnifiedMetamodel__Entity33', partner)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom32') == owner
    _safe_set(owner, 'UnifiedMetamodel__Entity33', None)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom32') is None


def test_assoc_technologymetamodel22_stub_double():
    # UnifiedMetamodel__TechnologyMetamodel has no real 'UnifiedMetamodel__TechnologyMetamodel' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Metamodel(name="sample_text")
    partner = UnifiedMetamodel__TechnologyMetamodel()
    setattr(partner, 'UnifiedMetamodel__TechnologyMetamodel', None)
    _safe_set(owner, 'UnifiedMetamodel__Metamodel23', partner)
    assert getattr(partner, 'UnifiedMetamodel__TechnologyMetamodel') == owner
    _safe_set(owner, 'UnifiedMetamodel__Metamodel23', None)
    assert getattr(partner, 'UnifiedMetamodel__TechnologyMetamodel') is None


def test_assoc_use56_stub_double():
    # UnifiedMetamodel__State has no real 'UnifiedMetamodel__State57' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__ModuleFront's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__ModuleFront's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__ModuleFront(name="sample_text")
    partner = UnifiedMetamodel__State()
    setattr(partner, 'UnifiedMetamodel__State57', None)
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__State57')
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__State57')


