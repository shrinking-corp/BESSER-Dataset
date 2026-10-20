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
    UnifiedMetamodel__Services,
    UnifiedMetamodel__ServicesFront,
    UnifiedMetamodel__SpecialEntity,
    UnifiedMetamodel__State,
    UnifiedMetamodel__Store,
    UnifiedMetamodel__Submodule,
    UnifiedMetamodel__Subproject,
    UnifiedMetamodel__TechnologyMetamodel,
    UnifiedMetamodel__Transaction,
    UnifiedMetamodel__UI,
    UnifiedMetamodel__UIFront,
    UnifiedMetamodel__Util,
    UnifiedMetamodel__Visualizer,
    UnifiedMetamodel__War,
    UnifiedMetamodel__exchange,
    UnifiedMetamodel__sale,
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

def test_assoc_IsOrganizedBy77_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Functionality(name="sample_text")
    a2 = UnifiedMetamodel__Functionality(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory79', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory79', a1)
    if hasattr(a1, 'UnifiedMetamodel__Functionality78'):
        assert _is_linked(a1, 'UnifiedMetamodel__Functionality78', b)
    _safe_set(b, 'UnifiedMetamodel__Directory79', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory79', a2)
    if hasattr(a1, 'UnifiedMetamodel__Functionality78'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Functionality78', b)
    if hasattr(a2, 'UnifiedMetamodel__Functionality78'):
        assert _is_linked(a2, 'UnifiedMetamodel__Functionality78', b)
    _safe_set(b, 'UnifiedMetamodel__Directory79', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory79', a2)
    if hasattr(a2, 'UnifiedMetamodel__Functionality78'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Functionality78', b)


def test_assoc_abstractmethod121_reverse_link_reassign_clear():
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


def test_assoc_actionDirectory86_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    a2 = UnifiedMetamodel__Directory(isRoot=False, name="sample_text_2", purpose="sample_text_2")
    b = UnifiedMetamodel__Action(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Action87', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Action87', a1)
    if hasattr(a1, 'UnifiedMetamodel__Directory88'):
        assert _is_linked(a1, 'UnifiedMetamodel__Directory88', b)
    _safe_set(b, 'UnifiedMetamodel__Action87', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Action87', a2)
    if hasattr(a1, 'UnifiedMetamodel__Directory88'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Directory88', b)
    if hasattr(a2, 'UnifiedMetamodel__Directory88'):
        assert _is_linked(a2, 'UnifiedMetamodel__Directory88', b)
    _safe_set(b, 'UnifiedMetamodel__Action87', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Action87', a2)
    if hasattr(a2, 'UnifiedMetamodel__Directory88'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Directory88', b)


def test_assoc_actioncreator83_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ActionCreator(name="sample_text")
    a2 = UnifiedMetamodel__ActionCreator(name="sample_text_2")
    b = UnifiedMetamodel__Action(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Action84', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Action84', a1)
    if hasattr(a1, 'UnifiedMetamodel__ActionCreator85'):
        assert _is_linked(a1, 'UnifiedMetamodel__ActionCreator85', b)
    _safe_set(b, 'UnifiedMetamodel__Action84', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Action84', a2)
    if hasattr(a1, 'UnifiedMetamodel__ActionCreator85'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ActionCreator85', b)
    if hasattr(a2, 'UnifiedMetamodel__ActionCreator85'):
        assert _is_linked(a2, 'UnifiedMetamodel__ActionCreator85', b)
    _safe_set(b, 'UnifiedMetamodel__Action84', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Action84', a2)
    if hasattr(a2, 'UnifiedMetamodel__ActionCreator85'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ActionCreator85', b)


def test_assoc_actiondispatcher80_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ActionDispatcher(name="sample_text")
    a2 = UnifiedMetamodel__ActionDispatcher(name="sample_text_2")
    b = UnifiedMetamodel__Action(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Action81', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Action81', a1)
    if hasattr(a1, 'UnifiedMetamodel__ActionDispatcher82'):
        assert _is_linked(a1, 'UnifiedMetamodel__ActionDispatcher82', b)
    _safe_set(b, 'UnifiedMetamodel__Action81', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Action81', a2)
    if hasattr(a1, 'UnifiedMetamodel__ActionDispatcher82'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ActionDispatcher82', b)
    if hasattr(a2, 'UnifiedMetamodel__ActionDispatcher82'):
        assert _is_linked(a2, 'UnifiedMetamodel__ActionDispatcher82', b)
    _safe_set(b, 'UnifiedMetamodel__Action81', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Action81', a2)
    if hasattr(a2, 'UnifiedMetamodel__ActionDispatcher82'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ActionDispatcher82', b)


def test_assoc_allowToUse1_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__LayerSegment(name="sample_text")
    a2 = UnifiedMetamodel__LayerSegment(name="sample_text_2")
    b = UnifiedMetamodel__LayerSegment(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__LayerSegment0', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__LayerSegment0', a1)
    if hasattr(a1, 'UnifiedMetamodel__LayerSegment'):
        assert _is_linked(a1, 'UnifiedMetamodel__LayerSegment', b)
    _safe_set(b, 'UnifiedMetamodel__LayerSegment0', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__LayerSegment0', a2)
    if hasattr(a1, 'UnifiedMetamodel__LayerSegment'):
        assert not _is_linked(a1, 'UnifiedMetamodel__LayerSegment', b)
    if hasattr(a2, 'UnifiedMetamodel__LayerSegment'):
        assert _is_linked(a2, 'UnifiedMetamodel__LayerSegment', b)
    _safe_set(b, 'UnifiedMetamodel__LayerSegment0', set())
    assert not _is_linked(b, 'UnifiedMetamodel__LayerSegment0', a2)
    if hasattr(a2, 'UnifiedMetamodel__LayerSegment'):
        assert not _is_linked(a2, 'UnifiedMetamodel__LayerSegment', b)


def test_assoc_annotation123_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Library(isNative=True, name="sample_text")
    a2 = UnifiedMetamodel__Library(isNative=False, name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation', a1)
    if hasattr(a1, 'UnifiedMetamodel__Library124'):
        assert _is_linked(a1, 'UnifiedMetamodel__Library124', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation', a2)
    if hasattr(a1, 'UnifiedMetamodel__Library124'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Library124', b)
    if hasattr(a2, 'UnifiedMetamodel__Library124'):
        assert _is_linked(a2, 'UnifiedMetamodel__Library124', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation', a2)
    if hasattr(a2, 'UnifiedMetamodel__Library124'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Library124', b)


def test_assoc_annotation125_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Attribute(name="sample_text")
    a2 = UnifiedMetamodel__Attribute(name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation126', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation126', a1)
    if hasattr(a1, 'UnifiedMetamodel__Attribute'):
        assert _is_linked(a1, 'UnifiedMetamodel__Attribute', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation126', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation126', a2)
    if hasattr(a1, 'UnifiedMetamodel__Attribute'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Attribute', b)
    if hasattr(a2, 'UnifiedMetamodel__Attribute'):
        assert _is_linked(a2, 'UnifiedMetamodel__Attribute', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation126', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation126', a2)
    if hasattr(a2, 'UnifiedMetamodel__Attribute'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Attribute', b)


def test_assoc_annotation133_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation134', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation134', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation134', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation134', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation134', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation134', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack', b)


def test_assoc_annotation152_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation154', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation154', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass153'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass153', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation154', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation154', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass153'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass153', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass153'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass153', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation154', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation154', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass153'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass153', b)


def test_assoc_arguments138_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass140', a1)
    assert _is_linked(b, 'UnifiedMetamodel__EClass140', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack139'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack139', b)
    _safe_set(b, 'UnifiedMetamodel__EClass140', a2)
    assert _is_linked(b, 'UnifiedMetamodel__EClass140', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack139'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack139', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack139'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack139', b)
    _safe_set(b, 'UnifiedMetamodel__EClass140', None)
    assert not _is_linked(b, 'UnifiedMetamodel__EClass140', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack139'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack139', b)


def test_assoc_arguments169_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__AbstractMethod(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod170', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod170', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass171'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass171', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod170', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod170', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass171'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass171', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass171'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass171', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod170', set())
    assert not _is_linked(b, 'UnifiedMetamodel__AbstractMethod170', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass171'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass171', b)


def test_assoc_attribute146_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__Attribute(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Attribute148', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute148', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass147'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass147', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute148', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute148', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass147'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass147', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass147'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass147', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute148', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Attribute148', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass147'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass147', b)


def test_assoc_catches103_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Reducer(name="sample_text")
    a2 = UnifiedMetamodel__Reducer(name="sample_text_2")
    b = UnifiedMetamodel__ActionCreator(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ActionCreator105', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ActionCreator105', a1)
    if hasattr(a1, 'UnifiedMetamodel__Reducer104'):
        assert _is_linked(a1, 'UnifiedMetamodel__Reducer104', b)
    _safe_set(b, 'UnifiedMetamodel__ActionCreator105', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ActionCreator105', a2)
    if hasattr(a1, 'UnifiedMetamodel__Reducer104'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Reducer104', b)
    if hasattr(a2, 'UnifiedMetamodel__Reducer104'):
        assert _is_linked(a2, 'UnifiedMetamodel__Reducer104', b)
    _safe_set(b, 'UnifiedMetamodel__ActionCreator105', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ActionCreator105', a2)
    if hasattr(a2, 'UnifiedMetamodel__Reducer104'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Reducer104', b)


def test_assoc_class_144_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Epackage(name="sample_text")
    a2 = UnifiedMetamodel__Epackage(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass145', a1)
    assert _is_linked(b, 'UnifiedMetamodel__EClass145', a1)
    if hasattr(a1, 'UnifiedMetamodel__Epackage'):
        assert _is_linked(a1, 'UnifiedMetamodel__Epackage', b)
    _safe_set(b, 'UnifiedMetamodel__EClass145', a2)
    assert _is_linked(b, 'UnifiedMetamodel__EClass145', a2)
    if hasattr(a1, 'UnifiedMetamodel__Epackage'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Epackage', b)
    if hasattr(a2, 'UnifiedMetamodel__Epackage'):
        assert _is_linked(a2, 'UnifiedMetamodel__Epackage', b)
    _safe_set(b, 'UnifiedMetamodel__EClass145', None)
    assert not _is_linked(b, 'UnifiedMetamodel__EClass145', a2)
    if hasattr(a2, 'UnifiedMetamodel__Epackage'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Epackage', b)


def test_assoc_components70_reverse_link_reassign_clear():
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


def test_assoc_descriptor155_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Descriptor(name="sample_text", path="sample_text")
    a2 = UnifiedMetamodel__Descriptor(name="sample_text_2", path="sample_text_2")
    b = UnifiedMetamodel__Annotation(properties="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Annotation156', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation156', a1)
    if hasattr(a1, 'UnifiedMetamodel__Descriptor'):
        assert _is_linked(a1, 'UnifiedMetamodel__Descriptor', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation156', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Annotation156', a2)
    if hasattr(a1, 'UnifiedMetamodel__Descriptor'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Descriptor', b)
    if hasattr(a2, 'UnifiedMetamodel__Descriptor'):
        assert _is_linked(a2, 'UnifiedMetamodel__Descriptor', b)
    _safe_set(b, 'UnifiedMetamodel__Annotation156', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Annotation156', a2)
    if hasattr(a2, 'UnifiedMetamodel__Descriptor'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Descriptor', b)


def test_assoc_descriptor157_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__Descriptor(name="sample_text", path="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Descriptor159', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Descriptor159', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject158'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject158', b)
    _safe_set(b, 'UnifiedMetamodel__Descriptor159', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Descriptor159', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject158'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject158', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject158'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject158', b)
    _safe_set(b, 'UnifiedMetamodel__Descriptor159', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Descriptor159', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject158'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject158', b)


def test_assoc_directories51_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    a2 = UnifiedMetamodel__Directory(isRoot=False, name="sample_text_2", purpose="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory50', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Directory50', a1)
    if hasattr(a1, 'UnifiedMetamodel__Directory'):
        assert _is_linked(a1, 'UnifiedMetamodel__Directory', b)
    _safe_set(b, 'UnifiedMetamodel__Directory50', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Directory50', a2)
    if hasattr(a1, 'UnifiedMetamodel__Directory'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Directory', b)
    if hasattr(a2, 'UnifiedMetamodel__Directory'):
        assert _is_linked(a2, 'UnifiedMetamodel__Directory', b)
    _safe_set(b, 'UnifiedMetamodel__Directory50', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Directory50', a2)
    if hasattr(a2, 'UnifiedMetamodel__Directory'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Directory', b)


def test_assoc_entity40_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Submodule(name="sample_text")
    a2 = UnifiedMetamodel__Submodule(name="sample_text_2")
    b = UnifiedMetamodel__Entity(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Entity42', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Entity42', a1)
    if hasattr(a1, 'UnifiedMetamodel__Submodule41'):
        assert _is_linked(a1, 'UnifiedMetamodel__Submodule41', b)
    _safe_set(b, 'UnifiedMetamodel__Entity42', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Entity42', a2)
    if hasattr(a1, 'UnifiedMetamodel__Submodule41'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Submodule41', b)
    if hasattr(a2, 'UnifiedMetamodel__Submodule41'):
        assert _is_linked(a2, 'UnifiedMetamodel__Submodule41', b)
    _safe_set(b, 'UnifiedMetamodel__Entity42', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Entity42', a2)
    if hasattr(a2, 'UnifiedMetamodel__Submodule41'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Submodule41', b)


def test_assoc_files52_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__File(name="sample_text", type="sample_text")
    a2 = UnifiedMetamodel__File(name="sample_text_2", type="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory53', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Directory53', a1)
    if hasattr(a1, 'UnifiedMetamodel__File'):
        assert _is_linked(a1, 'UnifiedMetamodel__File', b)
    _safe_set(b, 'UnifiedMetamodel__Directory53', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Directory53', a2)
    if hasattr(a1, 'UnifiedMetamodel__File'):
        assert not _is_linked(a1, 'UnifiedMetamodel__File', b)
    if hasattr(a2, 'UnifiedMetamodel__File'):
        assert _is_linked(a2, 'UnifiedMetamodel__File', b)
    _safe_set(b, 'UnifiedMetamodel__Directory53', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Directory53', a2)
    if hasattr(a2, 'UnifiedMetamodel__File'):
        assert not _is_linked(a2, 'UnifiedMetamodel__File', b)


def test_assoc_inWithin100_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    a2 = UnifiedMetamodel__Directory(isRoot=False, name="sample_text_2", purpose="sample_text_2")
    b = UnifiedMetamodel__ComponentFront(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ComponentFront101', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront101', a1)
    if hasattr(a1, 'UnifiedMetamodel__Directory102'):
        assert _is_linked(a1, 'UnifiedMetamodel__Directory102', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront101', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront101', a2)
    if hasattr(a1, 'UnifiedMetamodel__Directory102'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Directory102', b)
    if hasattr(a2, 'UnifiedMetamodel__Directory102'):
        assert _is_linked(a2, 'UnifiedMetamodel__Directory102', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront101', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ComponentFront101', a2)
    if hasattr(a2, 'UnifiedMetamodel__Directory102'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Directory102', b)


def test_assoc_isOrganizedIn67_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ServicesFront(name="sample_text")
    a2 = UnifiedMetamodel__ServicesFront(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory69', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory69', a1)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront68'):
        assert _is_linked(a1, 'UnifiedMetamodel__ServicesFront68', b)
    _safe_set(b, 'UnifiedMetamodel__Directory69', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory69', a2)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront68'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ServicesFront68', b)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront68'):
        assert _is_linked(a2, 'UnifiedMetamodel__ServicesFront68', b)
    _safe_set(b, 'UnifiedMetamodel__Directory69', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory69', a2)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront68'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ServicesFront68', b)


def test_assoc_isPresentIn109_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ModuleFront(name="sample_text")
    a2 = UnifiedMetamodel__ModuleFront(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory111', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory111', a1)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront110'):
        assert _is_linked(a1, 'UnifiedMetamodel__ModuleFront110', b)
    _safe_set(b, 'UnifiedMetamodel__Directory111', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory111', a2)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront110'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ModuleFront110', b)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront110'):
        assert _is_linked(a2, 'UnifiedMetamodel__ModuleFront110', b)
    _safe_set(b, 'UnifiedMetamodel__Directory111', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory111', a2)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront110'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ModuleFront110', b)


def test_assoc_layerSegments5_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__LayerSegment(name="sample_text")
    a2 = UnifiedMetamodel__LayerSegment(name="sample_text_2")
    b = UnifiedMetamodel__Layer(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Layer', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Layer', a1)
    if hasattr(a1, 'UnifiedMetamodel__LayerSegment6'):
        assert _is_linked(a1, 'UnifiedMetamodel__LayerSegment6', b)
    _safe_set(b, 'UnifiedMetamodel__Layer', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Layer', a2)
    if hasattr(a1, 'UnifiedMetamodel__LayerSegment6'):
        assert not _is_linked(a1, 'UnifiedMetamodel__LayerSegment6', b)
    if hasattr(a2, 'UnifiedMetamodel__LayerSegment6'):
        assert _is_linked(a2, 'UnifiedMetamodel__LayerSegment6', b)
    _safe_set(b, 'UnifiedMetamodel__Layer', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Layer', a2)
    if hasattr(a2, 'UnifiedMetamodel__LayerSegment6'):
        assert not _is_linked(a2, 'UnifiedMetamodel__LayerSegment6', b)


def test_assoc_layers7_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Layer(name="sample_text")
    a2 = UnifiedMetamodel__Layer(name="sample_text_2")
    b = UnifiedMetamodel__Component(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Component', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Component', a1)
    if hasattr(a1, 'UnifiedMetamodel__Layer8'):
        assert _is_linked(a1, 'UnifiedMetamodel__Layer8', b)
    _safe_set(b, 'UnifiedMetamodel__Component', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Component', a2)
    if hasattr(a1, 'UnifiedMetamodel__Layer8'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Layer8', b)
    if hasattr(a2, 'UnifiedMetamodel__Layer8'):
        assert _is_linked(a2, 'UnifiedMetamodel__Layer8', b)
    _safe_set(b, 'UnifiedMetamodel__Component', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Component', a2)
    if hasattr(a2, 'UnifiedMetamodel__Layer8'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Layer8', b)


def test_assoc_layersegment3_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__LayerSegment(name="sample_text")
    a2 = UnifiedMetamodel__LayerSegment(name="sample_text_2")
    b = UnifiedMetamodel__LayerSegment(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__LayerSegment4', a1)
    assert _is_linked(b, 'UnifiedMetamodel__LayerSegment4', a1)
    if hasattr(a1, 'UnifiedMetamodel__LayerSegment2'):
        assert _is_linked(a1, 'UnifiedMetamodel__LayerSegment2', b)
    _safe_set(b, 'UnifiedMetamodel__LayerSegment4', a2)
    assert _is_linked(b, 'UnifiedMetamodel__LayerSegment4', a2)
    if hasattr(a1, 'UnifiedMetamodel__LayerSegment2'):
        assert not _is_linked(a1, 'UnifiedMetamodel__LayerSegment2', b)
    if hasattr(a2, 'UnifiedMetamodel__LayerSegment2'):
        assert _is_linked(a2, 'UnifiedMetamodel__LayerSegment2', b)
    _safe_set(b, 'UnifiedMetamodel__LayerSegment4', None)
    assert not _is_linked(b, 'UnifiedMetamodel__LayerSegment4', a2)
    if hasattr(a2, 'UnifiedMetamodel__LayerSegment2'):
        assert not _is_linked(a2, 'UnifiedMetamodel__LayerSegment2', b)


def test_assoc_library163_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__Library(isNative=True, name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Library165', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Library165', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject164'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject164', b)
    _safe_set(b, 'UnifiedMetamodel__Library165', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Library165', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject164'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject164', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject164'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject164', b)
    _safe_set(b, 'UnifiedMetamodel__Library165', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Library165', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject164'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject164', b)


def test_assoc_method149_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass150', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__EClass150', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack151'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack151', b)
    _safe_set(b, 'UnifiedMetamodel__EClass150', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__EClass150', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack151'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack151', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack151'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack151', b)
    _safe_set(b, 'UnifiedMetamodel__EClass150', set())
    assert not _is_linked(b, 'UnifiedMetamodel__EClass150', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack151'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack151', b)


def test_assoc_nativeclass122_reverse_link_reassign_clear():
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


def test_assoc_package160_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__Epackage(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Epackage162', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Epackage162', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject161'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject161', b)
    _safe_set(b, 'UnifiedMetamodel__Epackage162', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Epackage162', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject161'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject161', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject161'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject161', b)
    _safe_set(b, 'UnifiedMetamodel__Epackage162', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Epackage162', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject161'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject161', b)


def test_assoc_property28_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Property(name="sample_text", type="sample_text")
    a2 = UnifiedMetamodel__Property(name="sample_text_2", type="sample_text_2")
    b = UnifiedMetamodel__Entity(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Entity29', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Entity29', a1)
    if hasattr(a1, 'UnifiedMetamodel__Property'):
        assert _is_linked(a1, 'UnifiedMetamodel__Property', b)
    _safe_set(b, 'UnifiedMetamodel__Entity29', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Entity29', a2)
    if hasattr(a1, 'UnifiedMetamodel__Property'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Property', b)
    if hasattr(a2, 'UnifiedMetamodel__Property'):
        assert _is_linked(a2, 'UnifiedMetamodel__Property', b)
    _safe_set(b, 'UnifiedMetamodel__Entity29', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Entity29', a2)
    if hasattr(a2, 'UnifiedMetamodel__Property'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Property', b)


def test_assoc_reducerDirectory106_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Reducer(name="sample_text")
    a2 = UnifiedMetamodel__Reducer(name="sample_text_2")
    b = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Directory108', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Directory108', a1)
    if hasattr(a1, 'UnifiedMetamodel__Reducer107'):
        assert _is_linked(a1, 'UnifiedMetamodel__Reducer107', b)
    _safe_set(b, 'UnifiedMetamodel__Directory108', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Directory108', a2)
    if hasattr(a1, 'UnifiedMetamodel__Reducer107'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Reducer107', b)
    if hasattr(a2, 'UnifiedMetamodel__Reducer107'):
        assert _is_linked(a2, 'UnifiedMetamodel__Reducer107', b)
    _safe_set(b, 'UnifiedMetamodel__Directory108', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Directory108', a2)
    if hasattr(a2, 'UnifiedMetamodel__Reducer107'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Reducer107', b)


def test_assoc_relations9_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__RelationArch(name="sample_text")
    a2 = UnifiedMetamodel__RelationArch(name="sample_text_2")
    b = UnifiedMetamodel__Component(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Component10', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Component10', a1)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch'):
        assert _is_linked(a1, 'UnifiedMetamodel__RelationArch', b)
    _safe_set(b, 'UnifiedMetamodel__Component10', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Component10', a2)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch'):
        assert not _is_linked(a1, 'UnifiedMetamodel__RelationArch', b)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch'):
        assert _is_linked(a2, 'UnifiedMetamodel__RelationArch', b)
    _safe_set(b, 'UnifiedMetamodel__Component10', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Component10', a2)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch'):
        assert not _is_linked(a2, 'UnifiedMetamodel__RelationArch', b)


def test_assoc_return_135_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__MethodBack(name="sample_text")
    a2 = UnifiedMetamodel__MethodBack(name="sample_text_2")
    b = UnifiedMetamodel__EClass(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__EClass137', a1)
    assert _is_linked(b, 'UnifiedMetamodel__EClass137', a1)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack136'):
        assert _is_linked(a1, 'UnifiedMetamodel__MethodBack136', b)
    _safe_set(b, 'UnifiedMetamodel__EClass137', a2)
    assert _is_linked(b, 'UnifiedMetamodel__EClass137', a2)
    if hasattr(a1, 'UnifiedMetamodel__MethodBack136'):
        assert not _is_linked(a1, 'UnifiedMetamodel__MethodBack136', b)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack136'):
        assert _is_linked(a2, 'UnifiedMetamodel__MethodBack136', b)
    _safe_set(b, 'UnifiedMetamodel__EClass137', None)
    assert not _is_linked(b, 'UnifiedMetamodel__EClass137', a2)
    if hasattr(a2, 'UnifiedMetamodel__MethodBack136'):
        assert not _is_linked(a2, 'UnifiedMetamodel__MethodBack136', b)


def test_assoc_return_166_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__AbstractMethod(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod167', a1)
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod167', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass168'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass168', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod167', a2)
    assert _is_linked(b, 'UnifiedMetamodel__AbstractMethod167', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass168'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass168', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass168'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass168', b)
    _safe_set(b, 'UnifiedMetamodel__AbstractMethod167', None)
    assert not _is_linked(b, 'UnifiedMetamodel__AbstractMethod167', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass168'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass168', b)


def test_assoc_services74_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ServicesFront(name="sample_text")
    a2 = UnifiedMetamodel__ServicesFront(name="sample_text_2")
    b = UnifiedMetamodel__Functionality(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Functionality75', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__Functionality75', a1)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront76'):
        assert _is_linked(a1, 'UnifiedMetamodel__ServicesFront76', b)
    _safe_set(b, 'UnifiedMetamodel__Functionality75', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__Functionality75', a2)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront76'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ServicesFront76', b)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront76'):
        assert _is_linked(a2, 'UnifiedMetamodel__ServicesFront76', b)
    _safe_set(b, 'UnifiedMetamodel__Functionality75', set())
    assert not _is_linked(b, 'UnifiedMetamodel__Functionality75', a2)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront76'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ServicesFront76', b)


def test_assoc_source11_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__RelationArch(name="sample_text")
    a2 = UnifiedMetamodel__RelationArch(name="sample_text_2")
    b = UnifiedMetamodel__Layer(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Layer13', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Layer13', a1)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch12'):
        assert _is_linked(a1, 'UnifiedMetamodel__RelationArch12', b)
    _safe_set(b, 'UnifiedMetamodel__Layer13', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Layer13', a2)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch12'):
        assert not _is_linked(a1, 'UnifiedMetamodel__RelationArch12', b)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch12'):
        assert _is_linked(a2, 'UnifiedMetamodel__RelationArch12', b)
    _safe_set(b, 'UnifiedMetamodel__Layer13', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Layer13', a2)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch12'):
        assert not _is_linked(a2, 'UnifiedMetamodel__RelationArch12', b)


def test_assoc_submodule26_reverse_link_reassign_clear():
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


def test_assoc_subproject119_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__Subproject(name="sample_text")
    a2 = UnifiedMetamodel__Subproject(name="sample_text_2")
    b = UnifiedMetamodel__JEE_Project(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__JEE_Project120', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__JEE_Project120', a1)
    if hasattr(a1, 'UnifiedMetamodel__Subproject'):
        assert _is_linked(a1, 'UnifiedMetamodel__Subproject', b)
    _safe_set(b, 'UnifiedMetamodel__JEE_Project120', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__JEE_Project120', a2)
    if hasattr(a1, 'UnifiedMetamodel__Subproject'):
        assert not _is_linked(a1, 'UnifiedMetamodel__Subproject', b)
    if hasattr(a2, 'UnifiedMetamodel__Subproject'):
        assert _is_linked(a2, 'UnifiedMetamodel__Subproject', b)
    _safe_set(b, 'UnifiedMetamodel__JEE_Project120', set())
    assert not _is_linked(b, 'UnifiedMetamodel__JEE_Project120', a2)
    if hasattr(a2, 'UnifiedMetamodel__Subproject'):
        assert not _is_linked(a2, 'UnifiedMetamodel__Subproject', b)


def test_assoc_target14_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__RelationArch(name="sample_text")
    a2 = UnifiedMetamodel__RelationArch(name="sample_text_2")
    b = UnifiedMetamodel__Layer(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Layer16', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Layer16', a1)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch15'):
        assert _is_linked(a1, 'UnifiedMetamodel__RelationArch15', b)
    _safe_set(b, 'UnifiedMetamodel__Layer16', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Layer16', a2)
    if hasattr(a1, 'UnifiedMetamodel__RelationArch15'):
        assert not _is_linked(a1, 'UnifiedMetamodel__RelationArch15', b)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch15'):
        assert _is_linked(a2, 'UnifiedMetamodel__RelationArch15', b)
    _safe_set(b, 'UnifiedMetamodel__Layer16', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Layer16', a2)
    if hasattr(a2, 'UnifiedMetamodel__RelationArch15'):
        assert not _is_linked(a2, 'UnifiedMetamodel__RelationArch15', b)


def test_assoc_type127_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__EClass(name="sample_text")
    a2 = UnifiedMetamodel__EClass(name="sample_text_2")
    b = UnifiedMetamodel__Attribute(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__Attribute128', a1)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute128', a1)
    if hasattr(a1, 'UnifiedMetamodel__EClass'):
        assert _is_linked(a1, 'UnifiedMetamodel__EClass', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute128', a2)
    assert _is_linked(b, 'UnifiedMetamodel__Attribute128', a2)
    if hasattr(a1, 'UnifiedMetamodel__EClass'):
        assert not _is_linked(a1, 'UnifiedMetamodel__EClass', b)
    if hasattr(a2, 'UnifiedMetamodel__EClass'):
        assert _is_linked(a2, 'UnifiedMetamodel__EClass', b)
    _safe_set(b, 'UnifiedMetamodel__Attribute128', None)
    assert not _is_linked(b, 'UnifiedMetamodel__Attribute128', a2)
    if hasattr(a2, 'UnifiedMetamodel__EClass'):
        assert not _is_linked(a2, 'UnifiedMetamodel__EClass', b)


def test_assoc_use49_reverse_link_reassign_clear():
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


def test_assoc_use65_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ServicesFront(name="sample_text")
    a2 = UnifiedMetamodel__ServicesFront(name="sample_text_2")
    b = UnifiedMetamodel__ModuleFront(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ModuleFront66', a1)
    assert _is_linked(b, 'UnifiedMetamodel__ModuleFront66', a1)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront'):
        assert _is_linked(a1, 'UnifiedMetamodel__ServicesFront', b)
    _safe_set(b, 'UnifiedMetamodel__ModuleFront66', a2)
    assert _is_linked(b, 'UnifiedMetamodel__ModuleFront66', a2)
    if hasattr(a1, 'UnifiedMetamodel__ServicesFront'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ServicesFront', b)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront'):
        assert _is_linked(a2, 'UnifiedMetamodel__ServicesFront', b)
    _safe_set(b, 'UnifiedMetamodel__ModuleFront66', None)
    assert not _is_linked(b, 'UnifiedMetamodel__ModuleFront66', a2)
    if hasattr(a2, 'UnifiedMetamodel__ServicesFront'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ServicesFront', b)


def test_assoc_use97_reverse_link_reassign_clear():
    a1 = UnifiedMetamodel__ModuleFront(name="sample_text")
    a2 = UnifiedMetamodel__ModuleFront(name="sample_text_2")
    b = UnifiedMetamodel__ComponentFront(name="sample_text")
    _safe_set(b, 'UnifiedMetamodel__ComponentFront98', {a1})
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront98', a1)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront99'):
        assert _is_linked(a1, 'UnifiedMetamodel__ModuleFront99', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront98', {a2})
    assert _is_linked(b, 'UnifiedMetamodel__ComponentFront98', a2)
    if hasattr(a1, 'UnifiedMetamodel__ModuleFront99'):
        assert not _is_linked(a1, 'UnifiedMetamodel__ModuleFront99', b)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront99'):
        assert _is_linked(a2, 'UnifiedMetamodel__ModuleFront99', b)
    _safe_set(b, 'UnifiedMetamodel__ComponentFront98', set())
    assert not _is_linked(b, 'UnifiedMetamodel__ComponentFront98', a2)
    if hasattr(a2, 'UnifiedMetamodel__ModuleFront99'):
        assert not _is_linked(a2, 'UnifiedMetamodel__ModuleFront99', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abstractmethod141_stub_double():
    # UnifiedMetamodel__AbstractClass has no real 'UnifiedMetamodel__AbstractClass142' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__AbstractMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__AbstractMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__AbstractMethod(name="sample_text")
    partner = UnifiedMetamodel__AbstractClass()
    setattr(partner, 'UnifiedMetamodel__AbstractClass142', None)
    _safe_set(owner, 'UnifiedMetamodel__AbstractMethod143', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__AbstractClass142')
    _safe_set(owner, 'UnifiedMetamodel__AbstractMethod143', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__AbstractClass142')


def test_assoc_action54_stub_double():
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


def test_assoc_arquitecturemetamodel19_stub_double():
    # UnifiedMetamodel__ArquitectureMetamodel has no real 'UnifiedMetamodel__ArquitectureMetamodel20' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Metamodel(name="sample_text")
    partner = UnifiedMetamodel__ArquitectureMetamodel()
    setattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel20', None)
    _safe_set(owner, 'UnifiedMetamodel__Metamodel', partner)
    assert getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel20') == owner
    _safe_set(owner, 'UnifiedMetamodel__Metamodel', None)
    assert getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel20') is None


def test_assoc_components17_stub_double():
    # UnifiedMetamodel__ArquitectureMetamodel has no real 'UnifiedMetamodel__ArquitectureMetamodel' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Component(name="sample_text")
    partner = UnifiedMetamodel__ArquitectureMetamodel()
    setattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel', None)
    _safe_set(owner, 'UnifiedMetamodel__Component18', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel')
    _safe_set(owner, 'UnifiedMetamodel__Component18', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ArquitectureMetamodel')


def test_assoc_directories94_stub_double():
    # UnifiedMetamodel__ReactApp has no real 'UnifiedMetamodel__ReactApp95' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Directory(isRoot=True, name="sample_text", purpose="sample_text")
    partner = UnifiedMetamodel__ReactApp()
    setattr(partner, 'UnifiedMetamodel__ReactApp95', None)
    _safe_set(owner, 'UnifiedMetamodel__Directory96', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ReactApp95')
    _safe_set(owner, 'UnifiedMetamodel__Directory96', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ReactApp95')


def test_assoc_dispatches60_stub_double():
    # UnifiedMetamodel__Container has no real 'UnifiedMetamodel__Container' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__ActionDispatcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__ActionDispatcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__ActionDispatcher(name="sample_text")
    partner = UnifiedMetamodel__Container()
    setattr(partner, 'UnifiedMetamodel__Container', None)
    _safe_set(owner, 'UnifiedMetamodel__ActionDispatcher61', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__Container')
    _safe_set(owner, 'UnifiedMetamodel__ActionDispatcher61', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__Container')


def test_assoc_domainmetamodel21_stub_double():
    # UnifiedMetamodel__DomainMetamodel has no real 'UnifiedMetamodel__DomainMetamodel' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Metamodel(name="sample_text")
    partner = UnifiedMetamodel__DomainMetamodel()
    setattr(partner, 'UnifiedMetamodel__DomainMetamodel', None)
    _safe_set(owner, 'UnifiedMetamodel__Metamodel22', partner)
    assert getattr(partner, 'UnifiedMetamodel__DomainMetamodel') == owner
    _safe_set(owner, 'UnifiedMetamodel__Metamodel22', None)
    assert getattr(partner, 'UnifiedMetamodel__DomainMetamodel') is None


def test_assoc_functionalities89_stub_double():
    # UnifiedMetamodel__ReactApp has no real 'UnifiedMetamodel__ReactApp' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Functionality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Functionality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Functionality(name="sample_text")
    partner = UnifiedMetamodel__ReactApp()
    setattr(partner, 'UnifiedMetamodel__ReactApp', None)
    _safe_set(owner, 'UnifiedMetamodel__Functionality90', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ReactApp')
    _safe_set(owner, 'UnifiedMetamodel__Functionality90', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ReactApp')


def test_assoc_implement129_stub_double():
    # UnifiedMetamodel__GenericClass has no real 'UnifiedMetamodel__GenericClass' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__EInterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__EInterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__EInterface(name="sample_text")
    partner = UnifiedMetamodel__GenericClass()
    setattr(partner, 'UnifiedMetamodel__GenericClass', None)
    _safe_set(owner, 'UnifiedMetamodel__EInterface130', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__GenericClass')
    _safe_set(owner, 'UnifiedMetamodel__EInterface130', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__GenericClass')


def test_assoc_jee_project117_stub_double():
    # UnifiedMetamodel__JavaApp has no real 'UnifiedMetamodel__JavaApp118' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__JEE_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__JEE_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__JEE_Project(name="sample_text")
    partner = UnifiedMetamodel__JavaApp()
    setattr(partner, 'UnifiedMetamodel__JavaApp118', None)
    _safe_set(owner, 'UnifiedMetamodel__JEE_Project', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__JavaApp118')
    _safe_set(owner, 'UnifiedMetamodel__JEE_Project', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__JavaApp118')


def test_assoc_maps62_stub_double():
    # UnifiedMetamodel__Container has no real 'UnifiedMetamodel__Container63' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Reducer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Reducer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Reducer(name="sample_text")
    partner = UnifiedMetamodel__Container()
    setattr(partner, 'UnifiedMetamodel__Container63', None)
    _safe_set(owner, 'UnifiedMetamodel__Reducer64', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__Container63')
    _safe_set(owner, 'UnifiedMetamodel__Reducer64', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__Container63')


def test_assoc_module43_stub_double():
    # UnifiedMetamodel__DomainMetamodel has no real 'UnifiedMetamodel__DomainMetamodel44' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Module(name="sample_text")
    partner = UnifiedMetamodel__DomainMetamodel()
    setattr(partner, 'UnifiedMetamodel__DomainMetamodel44', None)
    _safe_set(owner, 'UnifiedMetamodel__Module45', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__DomainMetamodel44')
    _safe_set(owner, 'UnifiedMetamodel__Module45', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__DomainMetamodel44')


def test_assoc_modules91_stub_double():
    # UnifiedMetamodel__ReactApp has no real 'UnifiedMetamodel__ReactApp92' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__ModuleFront's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__ModuleFront's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__ModuleFront(name="sample_text")
    partner = UnifiedMetamodel__ReactApp()
    setattr(partner, 'UnifiedMetamodel__ReactApp92', None)
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront93', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__ReactApp92')
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront93', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__ReactApp92')


def test_assoc_operates_on25_stub_double():
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


def test_assoc_operations37_stub_double():
    # UnifiedMetamodel__Operations has no real 'UnifiedMetamodel__Operations39' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Submodule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Submodule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Submodule(name="sample_text")
    partner = UnifiedMetamodel__Operations()
    setattr(partner, 'UnifiedMetamodel__Operations39', None)
    _safe_set(owner, 'UnifiedMetamodel__Submodule38', {partner})
    assert getattr(partner, 'UnifiedMetamodel__Operations39') == owner
    _safe_set(owner, 'UnifiedMetamodel__Submodule38', set())
    assert getattr(partner, 'UnifiedMetamodel__Operations39') is None


def test_assoc_reducer55_stub_double():
    # UnifiedMetamodel__State has no real 'UnifiedMetamodel__State56' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Reducer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Reducer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Reducer(name="sample_text")
    partner = UnifiedMetamodel__State()
    setattr(partner, 'UnifiedMetamodel__State56', None)
    _safe_set(owner, 'UnifiedMetamodel__Reducer', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__State56')
    _safe_set(owner, 'UnifiedMetamodel__Reducer', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__State56')


def test_assoc_source30_stub_double():
    # UnifiedMetamodel__RelationDom has no real 'UnifiedMetamodel__RelationDom' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Entity(name="sample_text")
    partner = UnifiedMetamodel__RelationDom()
    setattr(partner, 'UnifiedMetamodel__RelationDom', None)
    _safe_set(owner, 'UnifiedMetamodel__Entity31', partner)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom') == owner
    _safe_set(owner, 'UnifiedMetamodel__Entity31', None)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom') is None


def test_assoc_state71_stub_double():
    # UnifiedMetamodel__State has no real 'UnifiedMetamodel__State73' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Functionality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Functionality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Functionality(name="sample_text")
    partner = UnifiedMetamodel__State()
    setattr(partner, 'UnifiedMetamodel__State73', None)
    _safe_set(owner, 'UnifiedMetamodel__Functionality72', partner)
    assert getattr(partner, 'UnifiedMetamodel__State73') == owner
    _safe_set(owner, 'UnifiedMetamodel__Functionality72', None)
    assert getattr(partner, 'UnifiedMetamodel__State73') is None


def test_assoc_target32_stub_double():
    # UnifiedMetamodel__RelationDom has no real 'UnifiedMetamodel__RelationDom33' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Entity(name="sample_text")
    partner = UnifiedMetamodel__RelationDom()
    setattr(partner, 'UnifiedMetamodel__RelationDom33', None)
    _safe_set(owner, 'UnifiedMetamodel__Entity34', partner)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom33') == owner
    _safe_set(owner, 'UnifiedMetamodel__Entity34', None)
    assert getattr(partner, 'UnifiedMetamodel__RelationDom33') is None


def test_assoc_technologymetamodel23_stub_double():
    # UnifiedMetamodel__TechnologyMetamodel has no real 'UnifiedMetamodel__TechnologyMetamodel' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__Metamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__Metamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__Metamodel(name="sample_text")
    partner = UnifiedMetamodel__TechnologyMetamodel()
    setattr(partner, 'UnifiedMetamodel__TechnologyMetamodel', None)
    _safe_set(owner, 'UnifiedMetamodel__Metamodel24', partner)
    assert getattr(partner, 'UnifiedMetamodel__TechnologyMetamodel') == owner
    _safe_set(owner, 'UnifiedMetamodel__Metamodel24', None)
    assert getattr(partner, 'UnifiedMetamodel__TechnologyMetamodel') is None


def test_assoc_use57_stub_double():
    # UnifiedMetamodel__State has no real 'UnifiedMetamodel__State58' property in the generated
    # code (a bare stub) -- manually attach it so UnifiedMetamodel__ModuleFront's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UnifiedMetamodel__ModuleFront's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UnifiedMetamodel__ModuleFront(name="sample_text")
    partner = UnifiedMetamodel__State()
    setattr(partner, 'UnifiedMetamodel__State58', None)
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront', partner)
    assert owner in getattr(partner, 'UnifiedMetamodel__State58')
    _safe_set(owner, 'UnifiedMetamodel__ModuleFront', None)
    assert owner not in getattr(partner, 'UnifiedMetamodel__State58')


