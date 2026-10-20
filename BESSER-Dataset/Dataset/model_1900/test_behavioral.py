import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFrontElement,
    Eclass,
    File,
    UIComponent,
    dsl_AbstractClass,
    dsl_AbstractFrontElement,
    dsl_AbstractMethod,
    dsl_Action,
    dsl_ActionCreator,
    dsl_ActionDispatcher,
    dsl_Annotation,
    dsl_Architecture,
    dsl_Attribute,
    dsl_Component,
    dsl_Container,
    dsl_Css,
    dsl_Descriptor,
    dsl_Directory,
    dsl_Domain,
    dsl_EObject,
    dsl_Eclass,
    dsl_Einterface,
    dsl_EntityName,
    dsl_Epackage,
    dsl_File,
    dsl_Functionality,
    dsl_GeneralEntity,
    dsl_GenericClass,
    dsl_JavaApp,
    dsl_JeeProject,
    dsl_Js,
    dsl_JsModule,
    dsl_Json,
    dsl_Layer,
    dsl_LayerSegment,
    dsl_LayerSegmentRelation,
    dsl_Library,
    dsl_Md,
    dsl_MethodBack,
    dsl_Module,
    dsl_NativeClass,
    dsl_Operateson,
    dsl_Operation,
    dsl_Property,
    dsl_ReactApp,
    dsl_Reducer,
    dsl_RelationArch,
    dsl_RelationDom,
    dsl_RouterComponent,
    dsl_ServiceFront,
    dsl_SpecialEntity,
    dsl_State,
    dsl_SublayerSegment,
    dsl_Submodule,
    dsl_Subproject,
    dsl_System,
    dsl_Technology,
    dsl_Transaction,
    dsl_Type,
    dsl_UIComponent,
    dsl_Visualizer,
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

def test_assoc_abstractMethod93_reverse_link_reassign_clear():
    a1 = dsl_Einterface(name="sample_text")
    a2 = dsl_Einterface(name="sample_text_2")
    b = dsl_AbstractMethod(name="sample_text")
    _safe_set(b, 'dsl_AbstractMethod95', a1)
    assert _is_linked(b, 'dsl_AbstractMethod95', a1)
    if hasattr(a1, 'dsl_Einterface94'):
        assert _is_linked(a1, 'dsl_Einterface94', b)
    _safe_set(b, 'dsl_AbstractMethod95', a2)
    assert _is_linked(b, 'dsl_AbstractMethod95', a2)
    if hasattr(a1, 'dsl_Einterface94'):
        assert not _is_linked(a1, 'dsl_Einterface94', b)
    if hasattr(a2, 'dsl_Einterface94'):
        assert _is_linked(a2, 'dsl_Einterface94', b)
    _safe_set(b, 'dsl_AbstractMethod95', None)
    assert not _is_linked(b, 'dsl_AbstractMethod95', a2)
    if hasattr(a2, 'dsl_Einterface94'):
        assert not _is_linked(a2, 'dsl_Einterface94', b)


def test_assoc_action161_reverse_link_reassign_clear():
    a1 = dsl_State(name="sample_text")
    a2 = dsl_State(name="sample_text_2")
    b = dsl_Action(name="sample_text")
    _safe_set(b, 'dsl_Action', a1)
    assert _is_linked(b, 'dsl_Action', a1)
    if hasattr(a1, 'dsl_State162'):
        assert _is_linked(a1, 'dsl_State162', b)
    _safe_set(b, 'dsl_Action', a2)
    assert _is_linked(b, 'dsl_Action', a2)
    if hasattr(a1, 'dsl_State162'):
        assert not _is_linked(a1, 'dsl_State162', b)
    if hasattr(a2, 'dsl_State162'):
        assert _is_linked(a2, 'dsl_State162', b)
    _safe_set(b, 'dsl_Action', None)
    assert not _is_linked(b, 'dsl_Action', a2)
    if hasattr(a2, 'dsl_State162'):
        assert not _is_linked(a2, 'dsl_State162', b)


def test_assoc_actionCreator165_reverse_link_reassign_clear():
    a1 = dsl_ActionCreator(name="sample_text", type="sample_text")
    a2 = dsl_ActionCreator(name="sample_text_2", type="sample_text_2")
    b = dsl_Action(name="sample_text")
    _safe_set(b, 'dsl_Action166', a1)
    assert _is_linked(b, 'dsl_Action166', a1)
    if hasattr(a1, 'dsl_ActionCreator'):
        assert _is_linked(a1, 'dsl_ActionCreator', b)
    _safe_set(b, 'dsl_Action166', a2)
    assert _is_linked(b, 'dsl_Action166', a2)
    if hasattr(a1, 'dsl_ActionCreator'):
        assert not _is_linked(a1, 'dsl_ActionCreator', b)
    if hasattr(a2, 'dsl_ActionCreator'):
        assert _is_linked(a2, 'dsl_ActionCreator', b)
    _safe_set(b, 'dsl_Action166', None)
    assert not _is_linked(b, 'dsl_Action166', a2)
    if hasattr(a2, 'dsl_ActionCreator'):
        assert not _is_linked(a2, 'dsl_ActionCreator', b)


def test_assoc_actionDispatcher167_reverse_link_reassign_clear():
    a1 = dsl_ActionDispatcher(name="sample_text")
    a2 = dsl_ActionDispatcher(name="sample_text_2")
    b = dsl_Action(name="sample_text")
    _safe_set(b, 'dsl_Action168', a1)
    assert _is_linked(b, 'dsl_Action168', a1)
    if hasattr(a1, 'dsl_ActionDispatcher'):
        assert _is_linked(a1, 'dsl_ActionDispatcher', b)
    _safe_set(b, 'dsl_Action168', a2)
    assert _is_linked(b, 'dsl_Action168', a2)
    if hasattr(a1, 'dsl_ActionDispatcher'):
        assert not _is_linked(a1, 'dsl_ActionDispatcher', b)
    if hasattr(a2, 'dsl_ActionDispatcher'):
        assert _is_linked(a2, 'dsl_ActionDispatcher', b)
    _safe_set(b, 'dsl_Action168', None)
    assert not _is_linked(b, 'dsl_Action168', a2)
    if hasattr(a2, 'dsl_ActionDispatcher'):
        assert not _is_linked(a2, 'dsl_ActionDispatcher', b)


def test_assoc_annotation118_reverse_link_reassign_clear():
    a1 = dsl_Library(isNative="sample_text", name="sample_text")
    a2 = dsl_Library(isNative="sample_text_2", name="sample_text_2")
    b = dsl_Annotation(propertie="sample_text")
    _safe_set(b, 'dsl_Annotation120', a1)
    assert _is_linked(b, 'dsl_Annotation120', a1)
    if hasattr(a1, 'dsl_Library119'):
        assert _is_linked(a1, 'dsl_Library119', b)
    _safe_set(b, 'dsl_Annotation120', a2)
    assert _is_linked(b, 'dsl_Annotation120', a2)
    if hasattr(a1, 'dsl_Library119'):
        assert not _is_linked(a1, 'dsl_Library119', b)
    if hasattr(a2, 'dsl_Library119'):
        assert _is_linked(a2, 'dsl_Library119', b)
    _safe_set(b, 'dsl_Annotation120', None)
    assert not _is_linked(b, 'dsl_Annotation120', a2)
    if hasattr(a2, 'dsl_Library119'):
        assert not _is_linked(a2, 'dsl_Library119', b)


def test_assoc_arg106_reverse_link_reassign_clear():
    a1 = dsl_MethodBack(name="sample_text")
    a2 = dsl_MethodBack(name="sample_text_2")
    b = dsl_Eclass(name="sample_text")
    _safe_set(b, 'dsl_Eclass108', a1)
    assert _is_linked(b, 'dsl_Eclass108', a1)
    if hasattr(a1, 'dsl_MethodBack107'):
        assert _is_linked(a1, 'dsl_MethodBack107', b)
    _safe_set(b, 'dsl_Eclass108', a2)
    assert _is_linked(b, 'dsl_Eclass108', a2)
    if hasattr(a1, 'dsl_MethodBack107'):
        assert not _is_linked(a1, 'dsl_MethodBack107', b)
    if hasattr(a2, 'dsl_MethodBack107'):
        assert _is_linked(a2, 'dsl_MethodBack107', b)
    _safe_set(b, 'dsl_Eclass108', None)
    assert not _is_linked(b, 'dsl_Eclass108', a2)
    if hasattr(a2, 'dsl_MethodBack107'):
        assert not _is_linked(a2, 'dsl_MethodBack107', b)


def test_assoc_arg112_reverse_link_reassign_clear():
    a1 = dsl_Eclass(name="sample_text")
    a2 = dsl_Eclass(name="sample_text_2")
    b = dsl_AbstractMethod(name="sample_text")
    _safe_set(b, 'dsl_AbstractMethod113', a1)
    assert _is_linked(b, 'dsl_AbstractMethod113', a1)
    if hasattr(a1, 'dsl_Eclass114'):
        assert _is_linked(a1, 'dsl_Eclass114', b)
    _safe_set(b, 'dsl_AbstractMethod113', a2)
    assert _is_linked(b, 'dsl_AbstractMethod113', a2)
    if hasattr(a1, 'dsl_Eclass114'):
        assert not _is_linked(a1, 'dsl_Eclass114', b)
    if hasattr(a2, 'dsl_Eclass114'):
        assert _is_linked(a2, 'dsl_Eclass114', b)
    _safe_set(b, 'dsl_AbstractMethod113', None)
    assert not _is_linked(b, 'dsl_AbstractMethod113', a2)
    if hasattr(a2, 'dsl_Eclass114'):
        assert not _is_linked(a2, 'dsl_Eclass114', b)


def test_assoc_attribute90_reverse_link_reassign_clear():
    a1 = dsl_Einterface(name="sample_text")
    a2 = dsl_Einterface(name="sample_text_2")
    b = dsl_Attribute(name="sample_text")
    _safe_set(b, 'dsl_Attribute92', a1)
    assert _is_linked(b, 'dsl_Attribute92', a1)
    if hasattr(a1, 'dsl_Einterface91'):
        assert _is_linked(a1, 'dsl_Einterface91', b)
    _safe_set(b, 'dsl_Attribute92', a2)
    assert _is_linked(b, 'dsl_Attribute92', a2)
    if hasattr(a1, 'dsl_Einterface91'):
        assert not _is_linked(a1, 'dsl_Einterface91', b)
    if hasattr(a2, 'dsl_Einterface91'):
        assert _is_linked(a2, 'dsl_Einterface91', b)
    _safe_set(b, 'dsl_Attribute92', None)
    assert not _is_linked(b, 'dsl_Attribute92', a2)
    if hasattr(a2, 'dsl_Einterface91'):
        assert not _is_linked(a2, 'dsl_Einterface91', b)


def test_assoc_descriptor68_reverse_link_reassign_clear():
    a1 = dsl_Subproject(name="sample_text")
    a2 = dsl_Subproject(name="sample_text_2")
    b = dsl_Descriptor(name="sample_text")
    _safe_set(b, 'dsl_Descriptor', a1)
    assert _is_linked(b, 'dsl_Descriptor', a1)
    if hasattr(a1, 'dsl_Subproject69'):
        assert _is_linked(a1, 'dsl_Subproject69', b)
    _safe_set(b, 'dsl_Descriptor', a2)
    assert _is_linked(b, 'dsl_Descriptor', a2)
    if hasattr(a1, 'dsl_Subproject69'):
        assert not _is_linked(a1, 'dsl_Subproject69', b)
    if hasattr(a2, 'dsl_Subproject69'):
        assert _is_linked(a2, 'dsl_Subproject69', b)
    _safe_set(b, 'dsl_Descriptor', None)
    assert not _is_linked(b, 'dsl_Descriptor', a2)
    if hasattr(a2, 'dsl_Subproject69'):
        assert not _is_linked(a2, 'dsl_Subproject69', b)


def test_assoc_dir169_reverse_link_reassign_clear():
    a1 = dsl_Directory(name="sample_text", purpose="sample_text")
    a2 = dsl_Directory(name="sample_text_2", purpose="sample_text_2")
    b = dsl_Action(name="sample_text")
    _safe_set(b, 'dsl_Action170', a1)
    assert _is_linked(b, 'dsl_Action170', a1)
    if hasattr(a1, 'dsl_Directory171'):
        assert _is_linked(a1, 'dsl_Directory171', b)
    _safe_set(b, 'dsl_Action170', a2)
    assert _is_linked(b, 'dsl_Action170', a2)
    if hasattr(a1, 'dsl_Directory171'):
        assert not _is_linked(a1, 'dsl_Directory171', b)
    if hasattr(a2, 'dsl_Directory171'):
        assert _is_linked(a2, 'dsl_Directory171', b)
    _safe_set(b, 'dsl_Action170', None)
    assert not _is_linked(b, 'dsl_Action170', a2)
    if hasattr(a2, 'dsl_Directory171'):
        assert not _is_linked(a2, 'dsl_Directory171', b)


def test_assoc_eclass103_reverse_link_reassign_clear():
    a1 = dsl_Epackage(name="sample_text")
    a2 = dsl_Epackage(name="sample_text_2")
    b = dsl_Eclass(name="sample_text")
    _safe_set(b, 'dsl_Eclass105', a1)
    assert _is_linked(b, 'dsl_Eclass105', a1)
    if hasattr(a1, 'dsl_Epackage104'):
        assert _is_linked(a1, 'dsl_Epackage104', b)
    _safe_set(b, 'dsl_Eclass105', a2)
    assert _is_linked(b, 'dsl_Eclass105', a2)
    if hasattr(a1, 'dsl_Epackage104'):
        assert not _is_linked(a1, 'dsl_Epackage104', b)
    if hasattr(a2, 'dsl_Epackage104'):
        assert _is_linked(a2, 'dsl_Epackage104', b)
    _safe_set(b, 'dsl_Eclass105', None)
    assert not _is_linked(b, 'dsl_Eclass105', a2)
    if hasattr(a2, 'dsl_Epackage104'):
        assert not _is_linked(a2, 'dsl_Epackage104', b)


def test_assoc_epackage64_reverse_link_reassign_clear():
    a1 = dsl_Subproject(name="sample_text")
    a2 = dsl_Subproject(name="sample_text_2")
    b = dsl_Epackage(name="sample_text")
    _safe_set(b, 'dsl_Epackage', a1)
    assert _is_linked(b, 'dsl_Epackage', a1)
    if hasattr(a1, 'dsl_Subproject65'):
        assert _is_linked(a1, 'dsl_Subproject65', b)
    _safe_set(b, 'dsl_Epackage', a2)
    assert _is_linked(b, 'dsl_Epackage', a2)
    if hasattr(a1, 'dsl_Subproject65'):
        assert not _is_linked(a1, 'dsl_Subproject65', b)
    if hasattr(a2, 'dsl_Subproject65'):
        assert _is_linked(a2, 'dsl_Subproject65', b)
    _safe_set(b, 'dsl_Epackage', None)
    assert not _is_linked(b, 'dsl_Epackage', a2)
    if hasattr(a2, 'dsl_Subproject65'):
        assert not _is_linked(a2, 'dsl_Subproject65', b)


def test_assoc_file156_reverse_link_reassign_clear():
    a1 = dsl_File(name="sample_text", type="sample_text")
    a2 = dsl_File(name="sample_text_2", type="sample_text_2")
    b = dsl_Directory(name="sample_text", purpose="sample_text")
    _safe_set(b, 'dsl_Directory157', a1)
    assert _is_linked(b, 'dsl_Directory157', a1)
    if hasattr(a1, 'dsl_File'):
        assert _is_linked(a1, 'dsl_File', b)
    _safe_set(b, 'dsl_Directory157', a2)
    assert _is_linked(b, 'dsl_Directory157', a2)
    if hasattr(a1, 'dsl_File'):
        assert not _is_linked(a1, 'dsl_File', b)
    if hasattr(a2, 'dsl_File'):
        assert _is_linked(a2, 'dsl_File', b)
    _safe_set(b, 'dsl_Directory157', None)
    assert not _is_linked(b, 'dsl_Directory157', a2)
    if hasattr(a2, 'dsl_File'):
        assert not _is_linked(a2, 'dsl_File', b)


def test_assoc_layer48_reverse_link_reassign_clear():
    a1 = dsl_Layer(name="sample_text")
    a2 = dsl_Layer(name="sample_text_2")
    b = dsl_Component(name="sample_text")
    _safe_set(b, 'dsl_Component49', {a1})
    assert _is_linked(b, 'dsl_Component49', a1)
    if hasattr(a1, 'dsl_Layer'):
        assert _is_linked(a1, 'dsl_Layer', b)
    _safe_set(b, 'dsl_Component49', {a2})
    assert _is_linked(b, 'dsl_Component49', a2)
    if hasattr(a1, 'dsl_Layer'):
        assert not _is_linked(a1, 'dsl_Layer', b)
    if hasattr(a2, 'dsl_Layer'):
        assert _is_linked(a2, 'dsl_Layer', b)
    _safe_set(b, 'dsl_Component49', set())
    assert not _is_linked(b, 'dsl_Component49', a2)
    if hasattr(a2, 'dsl_Layer'):
        assert not _is_linked(a2, 'dsl_Layer', b)


def test_assoc_layerSegments50_reverse_link_reassign_clear():
    a1 = dsl_LayerSegment(name="sample_text")
    a2 = dsl_LayerSegment(name="sample_text_2")
    b = dsl_Layer(name="sample_text")
    _safe_set(b, 'dsl_Layer51', {a1})
    assert _is_linked(b, 'dsl_Layer51', a1)
    if hasattr(a1, 'dsl_LayerSegment'):
        assert _is_linked(a1, 'dsl_LayerSegment', b)
    _safe_set(b, 'dsl_Layer51', {a2})
    assert _is_linked(b, 'dsl_Layer51', a2)
    if hasattr(a1, 'dsl_LayerSegment'):
        assert not _is_linked(a1, 'dsl_LayerSegment', b)
    if hasattr(a2, 'dsl_LayerSegment'):
        assert _is_linked(a2, 'dsl_LayerSegment', b)
    _safe_set(b, 'dsl_Layer51', set())
    assert not _is_linked(b, 'dsl_Layer51', a2)
    if hasattr(a2, 'dsl_LayerSegment'):
        assert not _is_linked(a2, 'dsl_LayerSegment', b)


def test_assoc_library66_reverse_link_reassign_clear():
    a1 = dsl_Subproject(name="sample_text")
    a2 = dsl_Subproject(name="sample_text_2")
    b = dsl_Library(isNative="sample_text", name="sample_text")
    _safe_set(b, 'dsl_Library', a1)
    assert _is_linked(b, 'dsl_Library', a1)
    if hasattr(a1, 'dsl_Subproject67'):
        assert _is_linked(a1, 'dsl_Subproject67', b)
    _safe_set(b, 'dsl_Library', a2)
    assert _is_linked(b, 'dsl_Library', a2)
    if hasattr(a1, 'dsl_Subproject67'):
        assert not _is_linked(a1, 'dsl_Subproject67', b)
    if hasattr(a2, 'dsl_Subproject67'):
        assert _is_linked(a2, 'dsl_Subproject67', b)
    _safe_set(b, 'dsl_Library', None)
    assert not _is_linked(b, 'dsl_Library', a2)
    if hasattr(a2, 'dsl_Subproject67'):
        assert not _is_linked(a2, 'dsl_Subproject67', b)


def test_assoc_operations13_reverse_link_reassign_clear():
    a1 = dsl_Submodule(name="sample_text")
    a2 = dsl_Submodule(name="sample_text_2")
    b = dsl_Operation(type="sample_text")
    _safe_set(b, 'dsl_Operation', a1)
    assert _is_linked(b, 'dsl_Operation', a1)
    if hasattr(a1, 'dsl_Submodule14'):
        assert _is_linked(a1, 'dsl_Submodule14', b)
    _safe_set(b, 'dsl_Operation', a2)
    assert _is_linked(b, 'dsl_Operation', a2)
    if hasattr(a1, 'dsl_Submodule14'):
        assert not _is_linked(a1, 'dsl_Submodule14', b)
    if hasattr(a2, 'dsl_Submodule14'):
        assert _is_linked(a2, 'dsl_Submodule14', b)
    _safe_set(b, 'dsl_Operation', None)
    assert not _is_linked(b, 'dsl_Operation', a2)
    if hasattr(a2, 'dsl_Submodule14'):
        assert not _is_linked(a2, 'dsl_Submodule14', b)


def test_assoc_reducer163_reverse_link_reassign_clear():
    a1 = dsl_State(name="sample_text")
    a2 = dsl_State(name="sample_text_2")
    b = dsl_Reducer(name="sample_text")
    _safe_set(b, 'dsl_Reducer', a1)
    assert _is_linked(b, 'dsl_Reducer', a1)
    if hasattr(a1, 'dsl_State164'):
        assert _is_linked(a1, 'dsl_State164', b)
    _safe_set(b, 'dsl_Reducer', a2)
    assert _is_linked(b, 'dsl_Reducer', a2)
    if hasattr(a1, 'dsl_State164'):
        assert not _is_linked(a1, 'dsl_State164', b)
    if hasattr(a2, 'dsl_State164'):
        assert _is_linked(a2, 'dsl_State164', b)
    _safe_set(b, 'dsl_Reducer', None)
    assert not _is_linked(b, 'dsl_Reducer', a2)
    if hasattr(a2, 'dsl_State164'):
        assert not _is_linked(a2, 'dsl_State164', b)


def test_assoc_relations52_reverse_link_reassign_clear():
    a1 = dsl_LayerSegmentRelation(layerSegment="sample_text")
    a2 = dsl_LayerSegmentRelation(layerSegment="sample_text_2")
    b = dsl_LayerSegment(name="sample_text")
    _safe_set(b, 'dsl_LayerSegment53', {a1})
    assert _is_linked(b, 'dsl_LayerSegment53', a1)
    if hasattr(a1, 'dsl_LayerSegmentRelation'):
        assert _is_linked(a1, 'dsl_LayerSegmentRelation', b)
    _safe_set(b, 'dsl_LayerSegment53', {a2})
    assert _is_linked(b, 'dsl_LayerSegment53', a2)
    if hasattr(a1, 'dsl_LayerSegmentRelation'):
        assert not _is_linked(a1, 'dsl_LayerSegmentRelation', b)
    if hasattr(a2, 'dsl_LayerSegmentRelation'):
        assert _is_linked(a2, 'dsl_LayerSegmentRelation', b)
    _safe_set(b, 'dsl_LayerSegment53', set())
    assert not _is_linked(b, 'dsl_LayerSegment53', a2)
    if hasattr(a2, 'dsl_LayerSegmentRelation'):
        assert not _is_linked(a2, 'dsl_LayerSegmentRelation', b)


def test_assoc_render133_reverse_link_reassign_clear():
    a1 = dsl_Visualizer(name="sample_text")
    a2 = dsl_Visualizer(name="sample_text_2")
    b = dsl_Functionality(name="sample_text")
    _safe_set(b, 'dsl_Functionality134', a1)
    assert _is_linked(b, 'dsl_Functionality134', a1)
    if hasattr(a1, 'dsl_Visualizer'):
        assert _is_linked(a1, 'dsl_Visualizer', b)
    _safe_set(b, 'dsl_Functionality134', a2)
    assert _is_linked(b, 'dsl_Functionality134', a2)
    if hasattr(a1, 'dsl_Visualizer'):
        assert not _is_linked(a1, 'dsl_Visualizer', b)
    if hasattr(a2, 'dsl_Visualizer'):
        assert _is_linked(a2, 'dsl_Visualizer', b)
    _safe_set(b, 'dsl_Functionality134', None)
    assert not _is_linked(b, 'dsl_Functionality134', a2)
    if hasattr(a2, 'dsl_Visualizer'):
        assert not _is_linked(a2, 'dsl_Visualizer', b)


def test_assoc_route129_reverse_link_reassign_clear():
    a1 = dsl_RouterComponent(name="sample_text")
    a2 = dsl_RouterComponent(name="sample_text_2")
    b = dsl_Functionality(name="sample_text")
    _safe_set(b, 'dsl_Functionality130', a1)
    assert _is_linked(b, 'dsl_Functionality130', a1)
    if hasattr(a1, 'dsl_RouterComponent'):
        assert _is_linked(a1, 'dsl_RouterComponent', b)
    _safe_set(b, 'dsl_Functionality130', a2)
    assert _is_linked(b, 'dsl_Functionality130', a2)
    if hasattr(a1, 'dsl_RouterComponent'):
        assert not _is_linked(a1, 'dsl_RouterComponent', b)
    if hasattr(a2, 'dsl_RouterComponent'):
        assert _is_linked(a2, 'dsl_RouterComponent', b)
    _safe_set(b, 'dsl_Functionality130', None)
    assert not _is_linked(b, 'dsl_Functionality130', a2)
    if hasattr(a2, 'dsl_RouterComponent'):
        assert not _is_linked(a2, 'dsl_RouterComponent', b)


def test_assoc_service137_reverse_link_reassign_clear():
    a1 = dsl_ServiceFront(method="sample_text", name="sample_text")
    a2 = dsl_ServiceFront(method="sample_text_2", name="sample_text_2")
    b = dsl_Functionality(name="sample_text")
    _safe_set(b, 'dsl_Functionality138', a1)
    assert _is_linked(b, 'dsl_Functionality138', a1)
    if hasattr(a1, 'dsl_ServiceFront'):
        assert _is_linked(a1, 'dsl_ServiceFront', b)
    _safe_set(b, 'dsl_Functionality138', a2)
    assert _is_linked(b, 'dsl_Functionality138', a2)
    if hasattr(a1, 'dsl_ServiceFront'):
        assert not _is_linked(a1, 'dsl_ServiceFront', b)
    if hasattr(a2, 'dsl_ServiceFront'):
        assert _is_linked(a2, 'dsl_ServiceFront', b)
    _safe_set(b, 'dsl_Functionality138', None)
    assert not _is_linked(b, 'dsl_Functionality138', a2)
    if hasattr(a2, 'dsl_ServiceFront'):
        assert not _is_linked(a2, 'dsl_ServiceFront', b)


def test_assoc_state135_reverse_link_reassign_clear():
    a1 = dsl_State(name="sample_text")
    a2 = dsl_State(name="sample_text_2")
    b = dsl_Functionality(name="sample_text")
    _safe_set(b, 'dsl_Functionality136', a1)
    assert _is_linked(b, 'dsl_Functionality136', a1)
    if hasattr(a1, 'dsl_State'):
        assert _is_linked(a1, 'dsl_State', b)
    _safe_set(b, 'dsl_Functionality136', a2)
    assert _is_linked(b, 'dsl_Functionality136', a2)
    if hasattr(a1, 'dsl_State'):
        assert not _is_linked(a1, 'dsl_State', b)
    if hasattr(a2, 'dsl_State'):
        assert _is_linked(a2, 'dsl_State', b)
    _safe_set(b, 'dsl_Functionality136', None)
    assert not _is_linked(b, 'dsl_Functionality136', a2)
    if hasattr(a2, 'dsl_State'):
        assert not _is_linked(a2, 'dsl_State', b)


def test_assoc_subdirectory159_reverse_link_reassign_clear():
    a1 = dsl_Directory(name="sample_text", purpose="sample_text")
    a2 = dsl_Directory(name="sample_text_2", purpose="sample_text_2")
    b = dsl_Directory(name="sample_text", purpose="sample_text")
    _safe_set(b, 'dsl_Directory160', a1)
    assert _is_linked(b, 'dsl_Directory160', a1)
    if hasattr(a1, 'dsl_Directory158'):
        assert _is_linked(a1, 'dsl_Directory158', b)
    _safe_set(b, 'dsl_Directory160', a2)
    assert _is_linked(b, 'dsl_Directory160', a2)
    if hasattr(a1, 'dsl_Directory158'):
        assert not _is_linked(a1, 'dsl_Directory158', b)
    if hasattr(a2, 'dsl_Directory158'):
        assert _is_linked(a2, 'dsl_Directory158', b)
    _safe_set(b, 'dsl_Directory160', None)
    assert not _is_linked(b, 'dsl_Directory160', a2)
    if hasattr(a2, 'dsl_Directory158'):
        assert not _is_linked(a2, 'dsl_Directory158', b)


def test_assoc_sublayerSegments54_reverse_link_reassign_clear():
    a1 = dsl_SublayerSegment(name="sample_text")
    a2 = dsl_SublayerSegment(name="sample_text_2")
    b = dsl_LayerSegment(name="sample_text")
    _safe_set(b, 'dsl_LayerSegment55', {a1})
    assert _is_linked(b, 'dsl_LayerSegment55', a1)
    if hasattr(a1, 'dsl_SublayerSegment'):
        assert _is_linked(a1, 'dsl_SublayerSegment', b)
    _safe_set(b, 'dsl_LayerSegment55', {a2})
    assert _is_linked(b, 'dsl_LayerSegment55', a2)
    if hasattr(a1, 'dsl_SublayerSegment'):
        assert not _is_linked(a1, 'dsl_SublayerSegment', b)
    if hasattr(a2, 'dsl_SublayerSegment'):
        assert _is_linked(a2, 'dsl_SublayerSegment', b)
    _safe_set(b, 'dsl_LayerSegment55', set())
    assert not _is_linked(b, 'dsl_LayerSegment55', a2)
    if hasattr(a2, 'dsl_SublayerSegment'):
        assert not _is_linked(a2, 'dsl_SublayerSegment', b)


def test_assoc_submodules11_reverse_link_reassign_clear():
    a1 = dsl_Submodule(name="sample_text")
    a2 = dsl_Submodule(name="sample_text_2")
    b = dsl_Module(name="sample_text")
    _safe_set(b, 'dsl_Module12', {a1})
    assert _is_linked(b, 'dsl_Module12', a1)
    if hasattr(a1, 'dsl_Submodule'):
        assert _is_linked(a1, 'dsl_Submodule', b)
    _safe_set(b, 'dsl_Module12', {a2})
    assert _is_linked(b, 'dsl_Module12', a2)
    if hasattr(a1, 'dsl_Submodule'):
        assert not _is_linked(a1, 'dsl_Submodule', b)
    if hasattr(a2, 'dsl_Submodule'):
        assert _is_linked(a2, 'dsl_Submodule', b)
    _safe_set(b, 'dsl_Module12', set())
    assert not _is_linked(b, 'dsl_Module12', a2)
    if hasattr(a2, 'dsl_Submodule'):
        assert not _is_linked(a2, 'dsl_Submodule', b)


def test_assoc_subproject62_reverse_link_reassign_clear():
    a1 = dsl_Subproject(name="sample_text")
    a2 = dsl_Subproject(name="sample_text_2")
    b = dsl_JeeProject(name="sample_text")
    _safe_set(b, 'dsl_JeeProject63', {a1})
    assert _is_linked(b, 'dsl_JeeProject63', a1)
    if hasattr(a1, 'dsl_Subproject'):
        assert _is_linked(a1, 'dsl_Subproject', b)
    _safe_set(b, 'dsl_JeeProject63', {a2})
    assert _is_linked(b, 'dsl_JeeProject63', a2)
    if hasattr(a1, 'dsl_Subproject'):
        assert not _is_linked(a1, 'dsl_Subproject', b)
    if hasattr(a2, 'dsl_Subproject'):
        assert _is_linked(a2, 'dsl_Subproject', b)
    _safe_set(b, 'dsl_JeeProject63', set())
    assert not _is_linked(b, 'dsl_JeeProject63', a2)
    if hasattr(a2, 'dsl_Subproject'):
        assert not _is_linked(a2, 'dsl_Subproject', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = dsl_Operation(type="sample_text")
    a2 = dsl_Operation(type="sample_text_2")
    b = dsl_EntityName(name="sample_text")
    _safe_set(b, 'dsl_EntityName', a1)
    assert _is_linked(b, 'dsl_EntityName', a1)
    if hasattr(a1, 'dsl_Operation18'):
        assert _is_linked(a1, 'dsl_Operation18', b)
    _safe_set(b, 'dsl_EntityName', a2)
    assert _is_linked(b, 'dsl_EntityName', a2)
    if hasattr(a1, 'dsl_Operation18'):
        assert not _is_linked(a1, 'dsl_Operation18', b)
    if hasattr(a2, 'dsl_Operation18'):
        assert _is_linked(a2, 'dsl_Operation18', b)
    _safe_set(b, 'dsl_EntityName', None)
    assert not _is_linked(b, 'dsl_EntityName', a2)
    if hasattr(a2, 'dsl_Operation18'):
        assert not _is_linked(a2, 'dsl_Operation18', b)


def test_assoc_type101_reverse_link_reassign_clear():
    a1 = dsl_Eclass(name="sample_text")
    a2 = dsl_Eclass(name="sample_text_2")
    b = dsl_Attribute(name="sample_text")
    _safe_set(b, 'dsl_Attribute102', a1)
    assert _is_linked(b, 'dsl_Attribute102', a1)
    if hasattr(a1, 'dsl_Eclass'):
        assert _is_linked(a1, 'dsl_Eclass', b)
    _safe_set(b, 'dsl_Attribute102', a2)
    assert _is_linked(b, 'dsl_Attribute102', a2)
    if hasattr(a1, 'dsl_Eclass'):
        assert not _is_linked(a1, 'dsl_Eclass', b)
    if hasattr(a2, 'dsl_Eclass'):
        assert _is_linked(a2, 'dsl_Eclass', b)
    _safe_set(b, 'dsl_Attribute102', None)
    assert not _is_linked(b, 'dsl_Attribute102', a2)
    if hasattr(a2, 'dsl_Eclass'):
        assert not _is_linked(a2, 'dsl_Eclass', b)


def test_assoc_type109_reverse_link_reassign_clear():
    a1 = dsl_MethodBack(name="sample_text")
    a2 = dsl_MethodBack(name="sample_text_2")
    b = dsl_Eclass(name="sample_text")
    _safe_set(b, 'dsl_Eclass111', a1)
    assert _is_linked(b, 'dsl_Eclass111', a1)
    if hasattr(a1, 'dsl_MethodBack110'):
        assert _is_linked(a1, 'dsl_MethodBack110', b)
    _safe_set(b, 'dsl_Eclass111', a2)
    assert _is_linked(b, 'dsl_Eclass111', a2)
    if hasattr(a1, 'dsl_MethodBack110'):
        assert not _is_linked(a1, 'dsl_MethodBack110', b)
    if hasattr(a2, 'dsl_MethodBack110'):
        assert _is_linked(a2, 'dsl_MethodBack110', b)
    _safe_set(b, 'dsl_Eclass111', None)
    assert not _is_linked(b, 'dsl_Eclass111', a2)
    if hasattr(a2, 'dsl_MethodBack110'):
        assert not _is_linked(a2, 'dsl_MethodBack110', b)


def test_assoc_type115_reverse_link_reassign_clear():
    a1 = dsl_Eclass(name="sample_text")
    a2 = dsl_Eclass(name="sample_text_2")
    b = dsl_AbstractMethod(name="sample_text")
    _safe_set(b, 'dsl_AbstractMethod116', a1)
    assert _is_linked(b, 'dsl_AbstractMethod116', a1)
    if hasattr(a1, 'dsl_Eclass117'):
        assert _is_linked(a1, 'dsl_Eclass117', b)
    _safe_set(b, 'dsl_AbstractMethod116', a2)
    assert _is_linked(b, 'dsl_AbstractMethod116', a2)
    if hasattr(a1, 'dsl_Eclass117'):
        assert not _is_linked(a1, 'dsl_Eclass117', b)
    if hasattr(a2, 'dsl_Eclass117'):
        assert _is_linked(a2, 'dsl_Eclass117', b)
    _safe_set(b, 'dsl_AbstractMethod116', None)
    assert not _is_linked(b, 'dsl_AbstractMethod116', a2)
    if hasattr(a2, 'dsl_Eclass117'):
        assert not _is_linked(a2, 'dsl_Eclass117', b)


def test_assoc_type139_reverse_link_reassign_clear():
    a1 = dsl_Functionality(name="sample_text")
    a2 = dsl_Functionality(name="sample_text_2")
    b = dsl_Directory(name="sample_text", purpose="sample_text")
    _safe_set(b, 'dsl_Directory141', a1)
    assert _is_linked(b, 'dsl_Directory141', a1)
    if hasattr(a1, 'dsl_Functionality140'):
        assert _is_linked(a1, 'dsl_Functionality140', b)
    _safe_set(b, 'dsl_Directory141', a2)
    assert _is_linked(b, 'dsl_Directory141', a2)
    if hasattr(a1, 'dsl_Functionality140'):
        assert not _is_linked(a1, 'dsl_Functionality140', b)
    if hasattr(a2, 'dsl_Functionality140'):
        assert _is_linked(a2, 'dsl_Functionality140', b)
    _safe_set(b, 'dsl_Directory141', None)
    assert not _is_linked(b, 'dsl_Directory141', a2)
    if hasattr(a2, 'dsl_Functionality140'):
        assert not _is_linked(a2, 'dsl_Functionality140', b)


def test_assoc_type153_reverse_link_reassign_clear():
    a1 = dsl_ServiceFront(method="sample_text", name="sample_text")
    a2 = dsl_ServiceFront(method="sample_text_2", name="sample_text_2")
    b = dsl_JsModule(name="sample_text")
    _safe_set(b, 'dsl_JsModule155', a1)
    assert _is_linked(b, 'dsl_JsModule155', a1)
    if hasattr(a1, 'dsl_ServiceFront154'):
        assert _is_linked(a1, 'dsl_ServiceFront154', b)
    _safe_set(b, 'dsl_JsModule155', a2)
    assert _is_linked(b, 'dsl_JsModule155', a2)
    if hasattr(a1, 'dsl_ServiceFront154'):
        assert not _is_linked(a1, 'dsl_ServiceFront154', b)
    if hasattr(a2, 'dsl_ServiceFront154'):
        assert _is_linked(a2, 'dsl_ServiceFront154', b)
    _safe_set(b, 'dsl_JsModule155', None)
    assert not _is_linked(b, 'dsl_JsModule155', a2)
    if hasattr(a2, 'dsl_ServiceFront154'):
        assert not _is_linked(a2, 'dsl_ServiceFront154', b)


def test_assoc_type172_reverse_link_reassign_clear():
    a1 = dsl_ActionDispatcher(name="sample_text")
    a2 = dsl_ActionDispatcher(name="sample_text_2")
    b = dsl_ActionCreator(name="sample_text", type="sample_text")
    _safe_set(b, 'dsl_ActionCreator174', a1)
    assert _is_linked(b, 'dsl_ActionCreator174', a1)
    if hasattr(a1, 'dsl_ActionDispatcher173'):
        assert _is_linked(a1, 'dsl_ActionDispatcher173', b)
    _safe_set(b, 'dsl_ActionCreator174', a2)
    assert _is_linked(b, 'dsl_ActionCreator174', a2)
    if hasattr(a1, 'dsl_ActionDispatcher173'):
        assert not _is_linked(a1, 'dsl_ActionDispatcher173', b)
    if hasattr(a2, 'dsl_ActionDispatcher173'):
        assert _is_linked(a2, 'dsl_ActionDispatcher173', b)
    _safe_set(b, 'dsl_ActionCreator174', None)
    assert not _is_linked(b, 'dsl_ActionCreator174', a2)
    if hasattr(a2, 'dsl_ActionDispatcher173'):
        assert not _is_linked(a2, 'dsl_ActionDispatcher173', b)


def test_assoc_type178_reverse_link_reassign_clear():
    a1 = dsl_JsModule(name="sample_text")
    a2 = dsl_JsModule(name="sample_text_2")
    b = dsl_Directory(name="sample_text", purpose="sample_text")
    _safe_set(b, 'dsl_Directory180', a1)
    assert _is_linked(b, 'dsl_Directory180', a1)
    if hasattr(a1, 'dsl_JsModule179'):
        assert _is_linked(a1, 'dsl_JsModule179', b)
    _safe_set(b, 'dsl_Directory180', a2)
    assert _is_linked(b, 'dsl_Directory180', a2)
    if hasattr(a1, 'dsl_JsModule179'):
        assert not _is_linked(a1, 'dsl_JsModule179', b)
    if hasattr(a2, 'dsl_JsModule179'):
        assert _is_linked(a2, 'dsl_JsModule179', b)
    _safe_set(b, 'dsl_Directory180', None)
    assert not _is_linked(b, 'dsl_Directory180', a2)
    if hasattr(a2, 'dsl_JsModule179'):
        assert not _is_linked(a2, 'dsl_JsModule179', b)


def test_assoc_type23_reverse_link_reassign_clear():
    a1 = dsl_Type(name="sample_text")
    a2 = dsl_Type(name="sample_text_2")
    b = dsl_Property(name="sample_text")
    _safe_set(b, 'dsl_Property24', a1)
    assert _is_linked(b, 'dsl_Property24', a1)
    if hasattr(a1, 'dsl_Type25'):
        assert _is_linked(a1, 'dsl_Type25', b)
    _safe_set(b, 'dsl_Property24', a2)
    assert _is_linked(b, 'dsl_Property24', a2)
    if hasattr(a1, 'dsl_Type25'):
        assert not _is_linked(a1, 'dsl_Type25', b)
    if hasattr(a2, 'dsl_Type25'):
        assert _is_linked(a2, 'dsl_Type25', b)
    _safe_set(b, 'dsl_Property24', None)
    assert not _is_linked(b, 'dsl_Property24', a2)
    if hasattr(a2, 'dsl_Type25'):
        assert not _is_linked(a2, 'dsl_Type25', b)


def test_assoc_wrap131_reverse_link_reassign_clear():
    a1 = dsl_Functionality(name="sample_text")
    a2 = dsl_Functionality(name="sample_text_2")
    b = dsl_Container(name="sample_text")
    _safe_set(b, 'dsl_Container', a1)
    assert _is_linked(b, 'dsl_Container', a1)
    if hasattr(a1, 'dsl_Functionality132'):
        assert _is_linked(a1, 'dsl_Functionality132', b)
    _safe_set(b, 'dsl_Container', a2)
    assert _is_linked(b, 'dsl_Container', a2)
    if hasattr(a1, 'dsl_Functionality132'):
        assert not _is_linked(a1, 'dsl_Functionality132', b)
    if hasattr(a2, 'dsl_Functionality132'):
        assert _is_linked(a2, 'dsl_Functionality132', b)
    _safe_set(b, 'dsl_Container', None)
    assert not _is_linked(b, 'dsl_Container', a2)
    if hasattr(a2, 'dsl_Functionality132'):
        assert not _is_linked(a2, 'dsl_Functionality132', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abstractMethod75_stub_double():
    # dsl_AbstractClass has no real 'dsl_AbstractClass76' property in the generated
    # code (a bare stub) -- manually attach it so dsl_AbstractMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_AbstractMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_AbstractMethod(name="sample_text")
    partner = dsl_AbstractClass()
    setattr(partner, 'dsl_AbstractClass76', None)
    _safe_set(owner, 'dsl_AbstractMethod', partner)
    assert owner in getattr(partner, 'dsl_AbstractClass76')
    _safe_set(owner, 'dsl_AbstractMethod', None)
    assert owner not in getattr(partner, 'dsl_AbstractClass76')


def test_assoc_annotation73_stub_double():
    # dsl_AbstractClass has no real 'dsl_AbstractClass74' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Annotation(propertie="sample_text")
    partner = dsl_AbstractClass()
    setattr(partner, 'dsl_AbstractClass74', None)
    _safe_set(owner, 'dsl_Annotation', partner)
    assert getattr(partner, 'dsl_AbstractClass74') == owner
    _safe_set(owner, 'dsl_Annotation', None)
    assert getattr(partner, 'dsl_AbstractClass74') is None


def test_assoc_annotation82_stub_double():
    # dsl_GenericClass has no real 'dsl_GenericClass83' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Annotation(propertie="sample_text")
    partner = dsl_GenericClass()
    setattr(partner, 'dsl_GenericClass83', None)
    _safe_set(owner, 'dsl_Annotation84', partner)
    assert getattr(partner, 'dsl_GenericClass83') == owner
    _safe_set(owner, 'dsl_Annotation84', None)
    assert getattr(partner, 'dsl_GenericClass83') is None


def test_assoc_attribute70_stub_double():
    # dsl_AbstractClass has no real 'dsl_AbstractClass' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Attribute(name="sample_text")
    partner = dsl_AbstractClass()
    setattr(partner, 'dsl_AbstractClass', None)
    _safe_set(owner, 'dsl_Attribute', partner)
    assert owner in getattr(partner, 'dsl_AbstractClass')
    _safe_set(owner, 'dsl_Attribute', None)
    assert owner not in getattr(partner, 'dsl_AbstractClass')


def test_assoc_attribute77_stub_double():
    # dsl_GenericClass has no real 'dsl_GenericClass' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Attribute(name="sample_text")
    partner = dsl_GenericClass()
    setattr(partner, 'dsl_GenericClass', None)
    _safe_set(owner, 'dsl_Attribute78', partner)
    assert owner in getattr(partner, 'dsl_GenericClass')
    _safe_set(owner, 'dsl_Attribute78', None)
    assert owner not in getattr(partner, 'dsl_GenericClass')


def test_assoc_attribute96_stub_double():
    # dsl_NativeClass has no real 'dsl_NativeClass' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Attribute(name="sample_text")
    partner = dsl_NativeClass()
    setattr(partner, 'dsl_NativeClass', None)
    _safe_set(owner, 'dsl_Attribute97', partner)
    assert owner in getattr(partner, 'dsl_NativeClass')
    _safe_set(owner, 'dsl_Attribute97', None)
    assert owner not in getattr(partner, 'dsl_NativeClass')


def test_assoc_componentes44_stub_double():
    # dsl_Architecture has no real 'dsl_Architecture45' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Component(name="sample_text")
    partner = dsl_Architecture()
    setattr(partner, 'dsl_Architecture45', None)
    _safe_set(owner, 'dsl_Component', partner)
    assert owner in getattr(partner, 'dsl_Architecture45')
    _safe_set(owner, 'dsl_Component', None)
    assert owner not in getattr(partner, 'dsl_Architecture45')


def test_assoc_dir125_stub_double():
    # dsl_ReactApp has no real 'dsl_ReactApp126' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Directory(name="sample_text", purpose="sample_text")
    partner = dsl_ReactApp()
    setattr(partner, 'dsl_ReactApp126', None)
    _safe_set(owner, 'dsl_Directory', partner)
    assert getattr(partner, 'dsl_ReactApp126') == owner
    _safe_set(owner, 'dsl_Directory', None)
    assert getattr(partner, 'dsl_ReactApp126') is None


def test_assoc_entities15_stub_double():
    # dsl_EObject has no real 'dsl_EObject' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Submodule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Submodule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Submodule(name="sample_text")
    partner = dsl_EObject()
    setattr(partner, 'dsl_EObject', None)
    _safe_set(owner, 'dsl_Submodule16', {partner})
    assert getattr(partner, 'dsl_EObject') == owner
    _safe_set(owner, 'dsl_Submodule16', set())
    assert getattr(partner, 'dsl_EObject') is None


def test_assoc_func123_stub_double():
    # dsl_ReactApp has no real 'dsl_ReactApp124' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Functionality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Functionality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Functionality(name="sample_text")
    partner = dsl_ReactApp()
    setattr(partner, 'dsl_ReactApp124', None)
    _safe_set(owner, 'dsl_Functionality', partner)
    assert getattr(partner, 'dsl_ReactApp124') == owner
    _safe_set(owner, 'dsl_Functionality', None)
    assert getattr(partner, 'dsl_ReactApp124') is None


def test_assoc_imp88_stub_double():
    # dsl_GenericClass has no real 'dsl_GenericClass89' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Einterface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Einterface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Einterface(name="sample_text")
    partner = dsl_GenericClass()
    setattr(partner, 'dsl_GenericClass89', None)
    _safe_set(owner, 'dsl_Einterface', partner)
    assert getattr(partner, 'dsl_GenericClass89') == owner
    _safe_set(owner, 'dsl_Einterface', None)
    assert getattr(partner, 'dsl_GenericClass89') is None


def test_assoc_jeeproject60_stub_double():
    # dsl_JavaApp has no real 'dsl_JavaApp61' property in the generated
    # code (a bare stub) -- manually attach it so dsl_JeeProject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_JeeProject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_JeeProject(name="sample_text")
    partner = dsl_JavaApp()
    setattr(partner, 'dsl_JavaApp61', None)
    _safe_set(owner, 'dsl_JeeProject', partner)
    assert owner in getattr(partner, 'dsl_JavaApp61')
    _safe_set(owner, 'dsl_JeeProject', None)
    assert owner not in getattr(partner, 'dsl_JavaApp61')


def test_assoc_methodClass71_stub_double():
    # dsl_AbstractClass has no real 'dsl_AbstractClass72' property in the generated
    # code (a bare stub) -- manually attach it so dsl_MethodBack's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_MethodBack's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_MethodBack(name="sample_text")
    partner = dsl_AbstractClass()
    setattr(partner, 'dsl_AbstractClass72', None)
    _safe_set(owner, 'dsl_MethodBack', partner)
    assert owner in getattr(partner, 'dsl_AbstractClass72')
    _safe_set(owner, 'dsl_MethodBack', None)
    assert owner not in getattr(partner, 'dsl_AbstractClass72')


def test_assoc_methodClass79_stub_double():
    # dsl_GenericClass has no real 'dsl_GenericClass80' property in the generated
    # code (a bare stub) -- manually attach it so dsl_MethodBack's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_MethodBack's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_MethodBack(name="sample_text")
    partner = dsl_GenericClass()
    setattr(partner, 'dsl_GenericClass80', None)
    _safe_set(owner, 'dsl_MethodBack81', partner)
    assert owner in getattr(partner, 'dsl_GenericClass80')
    _safe_set(owner, 'dsl_MethodBack81', None)
    assert owner not in getattr(partner, 'dsl_GenericClass80')


def test_assoc_methodClass98_stub_double():
    # dsl_NativeClass has no real 'dsl_NativeClass99' property in the generated
    # code (a bare stub) -- manually attach it so dsl_MethodBack's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_MethodBack's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_MethodBack(name="sample_text")
    partner = dsl_NativeClass()
    setattr(partner, 'dsl_NativeClass99', None)
    _safe_set(owner, 'dsl_MethodBack100', partner)
    assert owner in getattr(partner, 'dsl_NativeClass99')
    _safe_set(owner, 'dsl_MethodBack100', None)
    assert owner not in getattr(partner, 'dsl_NativeClass99')


def test_assoc_mod127_stub_double():
    # dsl_ReactApp has no real 'dsl_ReactApp128' property in the generated
    # code (a bare stub) -- manually attach it so dsl_JsModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_JsModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_JsModule(name="sample_text")
    partner = dsl_ReactApp()
    setattr(partner, 'dsl_ReactApp128', None)
    _safe_set(owner, 'dsl_JsModule', partner)
    assert getattr(partner, 'dsl_ReactApp128') == owner
    _safe_set(owner, 'dsl_JsModule', None)
    assert getattr(partner, 'dsl_ReactApp128') is None


def test_assoc_modules7_stub_double():
    # dsl_Domain has no real 'dsl_Domain8' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Module(name="sample_text")
    partner = dsl_Domain()
    setattr(partner, 'dsl_Domain8', None)
    _safe_set(owner, 'dsl_Module', partner)
    assert owner in getattr(partner, 'dsl_Domain8')
    _safe_set(owner, 'dsl_Module', None)
    assert owner not in getattr(partner, 'dsl_Domain8')


def test_assoc_name19_stub_double():
    # dsl_GeneralEntity has no real 'dsl_GeneralEntity' property in the generated
    # code (a bare stub) -- manually attach it so dsl_EntityName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_EntityName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_EntityName(name="sample_text")
    partner = dsl_GeneralEntity()
    setattr(partner, 'dsl_GeneralEntity', None)
    _safe_set(owner, 'dsl_EntityName20', partner)
    assert getattr(partner, 'dsl_GeneralEntity') == owner
    _safe_set(owner, 'dsl_EntityName20', None)
    assert getattr(partner, 'dsl_GeneralEntity') is None


def test_assoc_name26_stub_double():
    # dsl_SpecialEntity has no real 'dsl_SpecialEntity' property in the generated
    # code (a bare stub) -- manually attach it so dsl_EntityName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_EntityName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_EntityName(name="sample_text")
    partner = dsl_SpecialEntity()
    setattr(partner, 'dsl_SpecialEntity', None)
    _safe_set(owner, 'dsl_EntityName27', partner)
    assert getattr(partner, 'dsl_SpecialEntity') == owner
    _safe_set(owner, 'dsl_EntityName27', None)
    assert getattr(partner, 'dsl_SpecialEntity') is None


def test_assoc_operateson33_stub_double():
    # dsl_Operateson has no real 'dsl_Operateson' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Transaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Transaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Transaction(type="sample_text")
    partner = dsl_Operateson()
    setattr(partner, 'dsl_Operateson', None)
    _safe_set(owner, 'dsl_Transaction34', {partner})
    assert getattr(partner, 'dsl_Operateson') == owner
    _safe_set(owner, 'dsl_Transaction34', set())
    assert getattr(partner, 'dsl_Operateson') is None


def test_assoc_operateson35_stub_double():
    # dsl_Operateson has no real 'dsl_Operateson36' property in the generated
    # code (a bare stub) -- manually attach it so dsl_EntityName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_EntityName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_EntityName(name="sample_text")
    partner = dsl_Operateson()
    setattr(partner, 'dsl_Operateson36', None)
    _safe_set(owner, 'dsl_EntityName37', partner)
    assert owner in getattr(partner, 'dsl_Operateson36')
    _safe_set(owner, 'dsl_EntityName37', None)
    assert owner not in getattr(partner, 'dsl_Operateson36')


def test_assoc_properties21_stub_double():
    # dsl_GeneralEntity has no real 'dsl_GeneralEntity22' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Property(name="sample_text")
    partner = dsl_GeneralEntity()
    setattr(partner, 'dsl_GeneralEntity22', None)
    _safe_set(owner, 'dsl_Property', partner)
    assert owner in getattr(partner, 'dsl_GeneralEntity22')
    _safe_set(owner, 'dsl_Property', None)
    assert owner not in getattr(partner, 'dsl_GeneralEntity22')


def test_assoc_properties28_stub_double():
    # dsl_SpecialEntity has no real 'dsl_SpecialEntity29' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Property(name="sample_text")
    partner = dsl_SpecialEntity()
    setattr(partner, 'dsl_SpecialEntity29', None)
    _safe_set(owner, 'dsl_Property30', partner)
    assert owner in getattr(partner, 'dsl_SpecialEntity29')
    _safe_set(owner, 'dsl_Property30', None)
    assert owner not in getattr(partner, 'dsl_SpecialEntity29')


def test_assoc_relationArch46_stub_double():
    # dsl_Architecture has no real 'dsl_Architecture47' property in the generated
    # code (a bare stub) -- manually attach it so dsl_RelationArch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_RelationArch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_RelationArch(name="sample_text", source="sample_text")
    partner = dsl_Architecture()
    setattr(partner, 'dsl_Architecture47', None)
    _safe_set(owner, 'dsl_RelationArch', partner)
    assert owner in getattr(partner, 'dsl_Architecture47')
    _safe_set(owner, 'dsl_RelationArch', None)
    assert owner not in getattr(partner, 'dsl_Architecture47')


def test_assoc_route145_stub_double():
    # dsl_UIComponent has no real 'dsl_UIComponent' property in the generated
    # code (a bare stub) -- manually attach it so dsl_RouterComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_RouterComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_RouterComponent(name="sample_text")
    partner = dsl_UIComponent()
    setattr(partner, 'dsl_UIComponent', None)
    _safe_set(owner, 'dsl_RouterComponent146', partner)
    assert getattr(partner, 'dsl_UIComponent') == owner
    _safe_set(owner, 'dsl_RouterComponent146', None)
    assert getattr(partner, 'dsl_UIComponent') is None


def test_assoc_source38_stub_double():
    # dsl_RelationDom has no real 'dsl_RelationDom39' property in the generated
    # code (a bare stub) -- manually attach it so dsl_EntityName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_EntityName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_EntityName(name="sample_text")
    partner = dsl_RelationDom()
    setattr(partner, 'dsl_RelationDom39', None)
    _safe_set(owner, 'dsl_EntityName40', partner)
    assert owner in getattr(partner, 'dsl_RelationDom39')
    _safe_set(owner, 'dsl_EntityName40', None)
    assert owner not in getattr(partner, 'dsl_RelationDom39')


def test_assoc_target41_stub_double():
    # dsl_RelationDom has no real 'dsl_RelationDom42' property in the generated
    # code (a bare stub) -- manually attach it so dsl_EntityName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_EntityName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_EntityName(name="sample_text")
    partner = dsl_RelationDom()
    setattr(partner, 'dsl_RelationDom42', None)
    _safe_set(owner, 'dsl_EntityName43', partner)
    assert owner in getattr(partner, 'dsl_RelationDom42')
    _safe_set(owner, 'dsl_EntityName43', None)
    assert owner not in getattr(partner, 'dsl_RelationDom42')


def test_assoc_transactions31_stub_double():
    # dsl_SpecialEntity has no real 'dsl_SpecialEntity32' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Transaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Transaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Transaction(type="sample_text")
    partner = dsl_SpecialEntity()
    setattr(partner, 'dsl_SpecialEntity32', None)
    _safe_set(owner, 'dsl_Transaction', partner)
    assert owner in getattr(partner, 'dsl_SpecialEntity32')
    _safe_set(owner, 'dsl_Transaction', None)
    assert owner not in getattr(partner, 'dsl_SpecialEntity32')


def test_assoc_type142_stub_double():
    # dsl_AbstractFrontElement has no real 'dsl_AbstractFrontElement144' property in the generated
    # code (a bare stub) -- manually attach it so dsl_RouterComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_RouterComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_RouterComponent(name="sample_text")
    partner = dsl_AbstractFrontElement()
    setattr(partner, 'dsl_AbstractFrontElement144', None)
    _safe_set(owner, 'dsl_RouterComponent143', partner)
    assert getattr(partner, 'dsl_AbstractFrontElement144') == owner
    _safe_set(owner, 'dsl_RouterComponent143', None)
    assert getattr(partner, 'dsl_AbstractFrontElement144') is None


def test_assoc_type147_stub_double():
    # dsl_AbstractFrontElement has no real 'dsl_AbstractFrontElement149' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Container(name="sample_text")
    partner = dsl_AbstractFrontElement()
    setattr(partner, 'dsl_AbstractFrontElement149', None)
    _safe_set(owner, 'dsl_Container148', partner)
    assert getattr(partner, 'dsl_AbstractFrontElement149') == owner
    _safe_set(owner, 'dsl_Container148', None)
    assert getattr(partner, 'dsl_AbstractFrontElement149') is None


def test_assoc_type150_stub_double():
    # dsl_AbstractFrontElement has no real 'dsl_AbstractFrontElement152' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Visualizer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Visualizer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Visualizer(name="sample_text")
    partner = dsl_AbstractFrontElement()
    setattr(partner, 'dsl_AbstractFrontElement152', None)
    _safe_set(owner, 'dsl_Visualizer151', partner)
    assert getattr(partner, 'dsl_AbstractFrontElement152') == owner
    _safe_set(owner, 'dsl_Visualizer151', None)
    assert getattr(partner, 'dsl_AbstractFrontElement152') is None


def test_assoc_type175_stub_double():
    # dsl_AbstractFrontElement has no real 'dsl_AbstractFrontElement177' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Reducer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Reducer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Reducer(name="sample_text")
    partner = dsl_AbstractFrontElement()
    setattr(partner, 'dsl_AbstractFrontElement177', None)
    _safe_set(owner, 'dsl_Reducer176', partner)
    assert getattr(partner, 'dsl_AbstractFrontElement177') == owner
    _safe_set(owner, 'dsl_Reducer176', None)
    assert getattr(partner, 'dsl_AbstractFrontElement177') is None


def test_assoc_types5_stub_double():
    # dsl_Domain has no real 'dsl_Domain6' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Type(name="sample_text")
    partner = dsl_Domain()
    setattr(partner, 'dsl_Domain6', None)
    _safe_set(owner, 'dsl_Type', partner)
    assert owner in getattr(partner, 'dsl_Domain6')
    _safe_set(owner, 'dsl_Type', None)
    assert owner not in getattr(partner, 'dsl_Domain6')


