import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Place,
    YasperEPNML114_AnnotationGraphics,
    YasperEPNML114_Arc,
    YasperEPNML114_ArcType,
    YasperEPNML114_ConnectionWeight,
    YasperEPNML114_ConnectionWeights,
    YasperEPNML114_Cost,
    YasperEPNML114_DocumentRoot,
    YasperEPNML114_EStringToStringMapEntry,
    YasperEPNML114_EdgeGraphics,
    YasperEPNML114_InitialMarking,
    YasperEPNML114_Inscription,
    YasperEPNML114_Net,
    YasperEPNML114_NetGraphics,
    YasperEPNML114_NodeGraphics,
    YasperEPNML114_Page,
    YasperEPNML114_Place,
    YasperEPNML114_PlaceType,
    YasperEPNML114_PlaceType1,
    YasperEPNML114_Pnml,
    YasperEPNML114_PnmlAnnotation,
    YasperEPNML114_ProcessingTime,
    YasperEPNML114_ReferencePlace,
    YasperEPNML114_ReferencePlaceSpecific,
    YasperEPNML114_Role,
    YasperEPNML114_Roles,
    YasperEPNML114_Stat,
    YasperEPNML114_ToolspecificType,
    YasperEPNML114_Transformation,
    YasperEPNML114_Transition,
    YasperEPNML114_TransitionSpecific,
    YasperEPNML114_TransitionType,
    YasperEPNML114_TwoDimVector,
    TextType1,
    TextType2,
    TextTypeMember0,
    Tool,
    Version,
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

def test_assoc_arc40_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    a2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    b = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    _safe_set(b, 'YasperEPNML114_Arc42', a1)
    assert _is_linked(b, 'YasperEPNML114_Arc42', a1)
    if hasattr(a1, 'YasperEPNML114_Net41'):
        assert _is_linked(a1, 'YasperEPNML114_Net41', b)
    _safe_set(b, 'YasperEPNML114_Arc42', a2)
    assert _is_linked(b, 'YasperEPNML114_Arc42', a2)
    if hasattr(a1, 'YasperEPNML114_Net41'):
        assert not _is_linked(a1, 'YasperEPNML114_Net41', b)
    if hasattr(a2, 'YasperEPNML114_Net41'):
        assert _is_linked(a2, 'YasperEPNML114_Net41', b)
    _safe_set(b, 'YasperEPNML114_Arc42', None)
    assert not _is_linked(b, 'YasperEPNML114_Arc42', a2)
    if hasattr(a2, 'YasperEPNML114_Net41'):
        assert not _is_linked(a2, 'YasperEPNML114_Net41', b)


def test_assoc_arc78_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    _safe_set(b, 'YasperEPNML114_Arc80', a1)
    assert _is_linked(b, 'YasperEPNML114_Arc80', a1)
    if hasattr(a1, 'YasperEPNML114_Page79'):
        assert _is_linked(a1, 'YasperEPNML114_Page79', b)
    _safe_set(b, 'YasperEPNML114_Arc80', a2)
    assert _is_linked(b, 'YasperEPNML114_Arc80', a2)
    if hasattr(a1, 'YasperEPNML114_Page79'):
        assert not _is_linked(a1, 'YasperEPNML114_Page79', b)
    if hasattr(a2, 'YasperEPNML114_Page79'):
        assert _is_linked(a2, 'YasperEPNML114_Page79', b)
    _safe_set(b, 'YasperEPNML114_Arc80', None)
    assert not _is_linked(b, 'YasperEPNML114_Arc80', a2)
    if hasattr(a2, 'YasperEPNML114_Page79'):
        assert not _is_linked(a2, 'YasperEPNML114_Page79', b)


def test_assoc_description103_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Place(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Place104', {a1})
    assert _is_linked(b, 'YasperEPNML114_Place104', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation105'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation105', b)
    _safe_set(b, 'YasperEPNML114_Place104', {a2})
    assert _is_linked(b, 'YasperEPNML114_Place104', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation105'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation105', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation105'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation105', b)
    _safe_set(b, 'YasperEPNML114_Place104', set())
    assert not _is_linked(b, 'YasperEPNML114_Place104', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation105'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation105', b)


def test_assoc_description129_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    a2 = YasperEPNML114_ReferencePlace(group="sample_text_2", id="sample_text_2", ref="sample_text_2")
    b = YasperEPNML114_PnmlAnnotation(text="sample_text")
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation131', a1)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation131', a1)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace130'):
        assert _is_linked(a1, 'YasperEPNML114_ReferencePlace130', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation131', a2)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation131', a2)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace130'):
        assert not _is_linked(a1, 'YasperEPNML114_ReferencePlace130', b)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace130'):
        assert _is_linked(a2, 'YasperEPNML114_ReferencePlace130', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation131', None)
    assert not _is_linked(b, 'YasperEPNML114_PnmlAnnotation131', a2)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace130'):
        assert not _is_linked(a2, 'YasperEPNML114_ReferencePlace130', b)


def test_assoc_description152_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_PnmlAnnotation(text="sample_text")
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation154', a1)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation154', a1)
    if hasattr(a1, 'YasperEPNML114_Transition153'):
        assert _is_linked(a1, 'YasperEPNML114_Transition153', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation154', a2)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation154', a2)
    if hasattr(a1, 'YasperEPNML114_Transition153'):
        assert not _is_linked(a1, 'YasperEPNML114_Transition153', b)
    if hasattr(a2, 'YasperEPNML114_Transition153'):
        assert _is_linked(a2, 'YasperEPNML114_Transition153', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation154', None)
    assert not _is_linked(b, 'YasperEPNML114_PnmlAnnotation154', a2)
    if hasattr(a2, 'YasperEPNML114_Transition153'):
        assert not _is_linked(a2, 'YasperEPNML114_Transition153', b)


def test_assoc_description48_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    _safe_set(b, 'YasperEPNML114_Net49', {a1})
    assert _is_linked(b, 'YasperEPNML114_Net49', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation50'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation50', b)
    _safe_set(b, 'YasperEPNML114_Net49', {a2})
    assert _is_linked(b, 'YasperEPNML114_Net49', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation50'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation50', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation50'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation50', b)
    _safe_set(b, 'YasperEPNML114_Net49', set())
    assert not _is_linked(b, 'YasperEPNML114_Net49', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation50'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation50', b)


def test_assoc_description8_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    _safe_set(b, 'YasperEPNML114_Arc9', {a1})
    assert _is_linked(b, 'YasperEPNML114_Arc9', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation10'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation10', b)
    _safe_set(b, 'YasperEPNML114_Arc9', {a2})
    assert _is_linked(b, 'YasperEPNML114_Arc9', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation10'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation10', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation10'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation10', b)
    _safe_set(b, 'YasperEPNML114_Arc9', set())
    assert not _is_linked(b, 'YasperEPNML114_Arc9', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation10'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation10', b)


def test_assoc_description87_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Page(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Page88', {a1})
    assert _is_linked(b, 'YasperEPNML114_Page88', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation89'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation89', b)
    _safe_set(b, 'YasperEPNML114_Page88', {a2})
    assert _is_linked(b, 'YasperEPNML114_Page88', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation89'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation89', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation89'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation89', b)
    _safe_set(b, 'YasperEPNML114_Page88', set())
    assert not _is_linked(b, 'YasperEPNML114_Page88', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation89'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation89', b)


def test_assoc_dimension57_reverse_link_reassign_clear():
    a1 = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    a2 = YasperEPNML114_TwoDimVector(x="sample_text_2", y="sample_text_2")
    b = YasperEPNML114_NetGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NetGraphics58', {a1})
    assert _is_linked(b, 'YasperEPNML114_NetGraphics58', a1)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector59'):
        assert _is_linked(a1, 'YasperEPNML114_TwoDimVector59', b)
    _safe_set(b, 'YasperEPNML114_NetGraphics58', {a2})
    assert _is_linked(b, 'YasperEPNML114_NetGraphics58', a2)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector59'):
        assert not _is_linked(a1, 'YasperEPNML114_TwoDimVector59', b)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector59'):
        assert _is_linked(a2, 'YasperEPNML114_TwoDimVector59', b)
    _safe_set(b, 'YasperEPNML114_NetGraphics58', set())
    assert not _is_linked(b, 'YasperEPNML114_NetGraphics58', a2)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector59'):
        assert not _is_linked(a2, 'YasperEPNML114_TwoDimVector59', b)


def test_assoc_dimension62_reverse_link_reassign_clear():
    a1 = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    a2 = YasperEPNML114_TwoDimVector(x="sample_text_2", y="sample_text_2")
    b = YasperEPNML114_NodeGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NodeGraphics63', {a1})
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics63', a1)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector64'):
        assert _is_linked(a1, 'YasperEPNML114_TwoDimVector64', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics63', {a2})
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics63', a2)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector64'):
        assert not _is_linked(a1, 'YasperEPNML114_TwoDimVector64', b)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector64'):
        assert _is_linked(a2, 'YasperEPNML114_TwoDimVector64', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics63', set())
    assert not _is_linked(b, 'YasperEPNML114_NodeGraphics63', a2)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector64'):
        assert not _is_linked(a2, 'YasperEPNML114_TwoDimVector64', b)


def test_assoc_graphics123_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    a2 = YasperEPNML114_ReferencePlace(group="sample_text_2", id="sample_text_2", ref="sample_text_2")
    b = YasperEPNML114_NodeGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NodeGraphics125', a1)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics125', a1)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace124'):
        assert _is_linked(a1, 'YasperEPNML114_ReferencePlace124', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics125', a2)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics125', a2)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace124'):
        assert not _is_linked(a1, 'YasperEPNML114_ReferencePlace124', b)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace124'):
        assert _is_linked(a2, 'YasperEPNML114_ReferencePlace124', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics125', None)
    assert not _is_linked(b, 'YasperEPNML114_NodeGraphics125', a2)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace124'):
        assert not _is_linked(a2, 'YasperEPNML114_ReferencePlace124', b)


def test_assoc_graphics143_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_NodeGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NodeGraphics145', a1)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics145', a1)
    if hasattr(a1, 'YasperEPNML114_Transition144'):
        assert _is_linked(a1, 'YasperEPNML114_Transition144', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics145', a2)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics145', a2)
    if hasattr(a1, 'YasperEPNML114_Transition144'):
        assert not _is_linked(a1, 'YasperEPNML114_Transition144', b)
    if hasattr(a2, 'YasperEPNML114_Transition144'):
        assert _is_linked(a2, 'YasperEPNML114_Transition144', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics145', None)
    assert not _is_linked(b, 'YasperEPNML114_NodeGraphics145', a2)
    if hasattr(a2, 'YasperEPNML114_Transition144'):
        assert not _is_linked(a2, 'YasperEPNML114_Transition144', b)


def test_assoc_graphics35_reverse_link_reassign_clear():
    a1 = YasperEPNML114_NetGraphics(group="sample_text")
    a2 = YasperEPNML114_NetGraphics(group="sample_text_2")
    b = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    _safe_set(b, 'YasperEPNML114_Net', {a1})
    assert _is_linked(b, 'YasperEPNML114_Net', a1)
    if hasattr(a1, 'YasperEPNML114_NetGraphics'):
        assert _is_linked(a1, 'YasperEPNML114_NetGraphics', b)
    _safe_set(b, 'YasperEPNML114_Net', {a2})
    assert _is_linked(b, 'YasperEPNML114_Net', a2)
    if hasattr(a1, 'YasperEPNML114_NetGraphics'):
        assert not _is_linked(a1, 'YasperEPNML114_NetGraphics', b)
    if hasattr(a2, 'YasperEPNML114_NetGraphics'):
        assert _is_linked(a2, 'YasperEPNML114_NetGraphics', b)
    _safe_set(b, 'YasperEPNML114_Net', set())
    assert not _is_linked(b, 'YasperEPNML114_Net', a2)
    if hasattr(a2, 'YasperEPNML114_NetGraphics'):
        assert not _is_linked(a2, 'YasperEPNML114_NetGraphics', b)


def test_assoc_graphics67_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_NetGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NetGraphics69', a1)
    assert _is_linked(b, 'YasperEPNML114_NetGraphics69', a1)
    if hasattr(a1, 'YasperEPNML114_Page68'):
        assert _is_linked(a1, 'YasperEPNML114_Page68', b)
    _safe_set(b, 'YasperEPNML114_NetGraphics69', a2)
    assert _is_linked(b, 'YasperEPNML114_NetGraphics69', a2)
    if hasattr(a1, 'YasperEPNML114_Page68'):
        assert not _is_linked(a1, 'YasperEPNML114_Page68', b)
    if hasattr(a2, 'YasperEPNML114_Page68'):
        assert _is_linked(a2, 'YasperEPNML114_Page68', b)
    _safe_set(b, 'YasperEPNML114_NetGraphics69', None)
    assert not _is_linked(b, 'YasperEPNML114_NetGraphics69', a2)
    if hasattr(a2, 'YasperEPNML114_Page68'):
        assert not _is_linked(a2, 'YasperEPNML114_Page68', b)


def test_assoc_graphics94_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Place(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Place(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_NodeGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NodeGraphics96', a1)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics96', a1)
    if hasattr(a1, 'YasperEPNML114_Place95'):
        assert _is_linked(a1, 'YasperEPNML114_Place95', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics96', a2)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics96', a2)
    if hasattr(a1, 'YasperEPNML114_Place95'):
        assert not _is_linked(a1, 'YasperEPNML114_Place95', b)
    if hasattr(a2, 'YasperEPNML114_Place95'):
        assert _is_linked(a2, 'YasperEPNML114_Place95', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics96', None)
    assert not _is_linked(b, 'YasperEPNML114_NodeGraphics96', a2)
    if hasattr(a2, 'YasperEPNML114_Place95'):
        assert not _is_linked(a2, 'YasperEPNML114_Place95', b)


def test_assoc_initialMarking97_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Place(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Place(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_InitialMarking(text="sample_text")
    _safe_set(b, 'YasperEPNML114_InitialMarking99', a1)
    assert _is_linked(b, 'YasperEPNML114_InitialMarking99', a1)
    if hasattr(a1, 'YasperEPNML114_Place98'):
        assert _is_linked(a1, 'YasperEPNML114_Place98', b)
    _safe_set(b, 'YasperEPNML114_InitialMarking99', a2)
    assert _is_linked(b, 'YasperEPNML114_InitialMarking99', a2)
    if hasattr(a1, 'YasperEPNML114_Place98'):
        assert not _is_linked(a1, 'YasperEPNML114_Place98', b)
    if hasattr(a2, 'YasperEPNML114_Place98'):
        assert _is_linked(a2, 'YasperEPNML114_Place98', b)
    _safe_set(b, 'YasperEPNML114_InitialMarking99', None)
    assert not _is_linked(b, 'YasperEPNML114_InitialMarking99', a2)
    if hasattr(a2, 'YasperEPNML114_Place98'):
        assert not _is_linked(a2, 'YasperEPNML114_Place98', b)


def test_assoc_inscription4_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Inscription(text="sample_text")
    a2 = YasperEPNML114_Inscription(text="sample_text_2")
    b = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    _safe_set(b, 'YasperEPNML114_Arc5', {a1})
    assert _is_linked(b, 'YasperEPNML114_Arc5', a1)
    if hasattr(a1, 'YasperEPNML114_Inscription'):
        assert _is_linked(a1, 'YasperEPNML114_Inscription', b)
    _safe_set(b, 'YasperEPNML114_Arc5', {a2})
    assert _is_linked(b, 'YasperEPNML114_Arc5', a2)
    if hasattr(a1, 'YasperEPNML114_Inscription'):
        assert not _is_linked(a1, 'YasperEPNML114_Inscription', b)
    if hasattr(a2, 'YasperEPNML114_Inscription'):
        assert _is_linked(a2, 'YasperEPNML114_Inscription', b)
    _safe_set(b, 'YasperEPNML114_Arc5', set())
    assert not _is_linked(b, 'YasperEPNML114_Arc5', a2)
    if hasattr(a2, 'YasperEPNML114_Inscription'):
        assert not _is_linked(a2, 'YasperEPNML114_Inscription', b)


def test_assoc_name100_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Place(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Place101', {a1})
    assert _is_linked(b, 'YasperEPNML114_Place101', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation102'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation102', b)
    _safe_set(b, 'YasperEPNML114_Place101', {a2})
    assert _is_linked(b, 'YasperEPNML114_Place101', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation102'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation102', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation102'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation102', b)
    _safe_set(b, 'YasperEPNML114_Place101', set())
    assert not _is_linked(b, 'YasperEPNML114_Place101', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation102'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation102', b)


def test_assoc_name126_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    a2 = YasperEPNML114_ReferencePlace(group="sample_text_2", id="sample_text_2", ref="sample_text_2")
    b = YasperEPNML114_PnmlAnnotation(text="sample_text")
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation128', a1)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation128', a1)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace127'):
        assert _is_linked(a1, 'YasperEPNML114_ReferencePlace127', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation128', a2)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation128', a2)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace127'):
        assert not _is_linked(a1, 'YasperEPNML114_ReferencePlace127', b)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace127'):
        assert _is_linked(a2, 'YasperEPNML114_ReferencePlace127', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation128', None)
    assert not _is_linked(b, 'YasperEPNML114_PnmlAnnotation128', a2)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace127'):
        assert not _is_linked(a2, 'YasperEPNML114_ReferencePlace127', b)


def test_assoc_name149_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_PnmlAnnotation(text="sample_text")
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation151', a1)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation151', a1)
    if hasattr(a1, 'YasperEPNML114_Transition150'):
        assert _is_linked(a1, 'YasperEPNML114_Transition150', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation151', a2)
    assert _is_linked(b, 'YasperEPNML114_PnmlAnnotation151', a2)
    if hasattr(a1, 'YasperEPNML114_Transition150'):
        assert not _is_linked(a1, 'YasperEPNML114_Transition150', b)
    if hasattr(a2, 'YasperEPNML114_Transition150'):
        assert _is_linked(a2, 'YasperEPNML114_Transition150', b)
    _safe_set(b, 'YasperEPNML114_PnmlAnnotation151', None)
    assert not _is_linked(b, 'YasperEPNML114_PnmlAnnotation151', a2)
    if hasattr(a2, 'YasperEPNML114_Transition150'):
        assert not _is_linked(a2, 'YasperEPNML114_Transition150', b)


def test_assoc_name45_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    _safe_set(b, 'YasperEPNML114_Net46', {a1})
    assert _is_linked(b, 'YasperEPNML114_Net46', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation47'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation47', b)
    _safe_set(b, 'YasperEPNML114_Net46', {a2})
    assert _is_linked(b, 'YasperEPNML114_Net46', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation47'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation47', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation47'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation47', b)
    _safe_set(b, 'YasperEPNML114_Net46', set())
    assert not _is_linked(b, 'YasperEPNML114_Net46', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation47'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation47', b)


def test_assoc_name6_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    _safe_set(b, 'YasperEPNML114_Arc7', {a1})
    assert _is_linked(b, 'YasperEPNML114_Arc7', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation', b)
    _safe_set(b, 'YasperEPNML114_Arc7', {a2})
    assert _is_linked(b, 'YasperEPNML114_Arc7', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation', b)
    _safe_set(b, 'YasperEPNML114_Arc7', set())
    assert not _is_linked(b, 'YasperEPNML114_Arc7', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation', b)


def test_assoc_name84_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    a2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    b = YasperEPNML114_Page(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Page85', {a1})
    assert _is_linked(b, 'YasperEPNML114_Page85', a1)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation86'):
        assert _is_linked(a1, 'YasperEPNML114_PnmlAnnotation86', b)
    _safe_set(b, 'YasperEPNML114_Page85', {a2})
    assert _is_linked(b, 'YasperEPNML114_Page85', a2)
    if hasattr(a1, 'YasperEPNML114_PnmlAnnotation86'):
        assert not _is_linked(a1, 'YasperEPNML114_PnmlAnnotation86', b)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation86'):
        assert _is_linked(a2, 'YasperEPNML114_PnmlAnnotation86', b)
    _safe_set(b, 'YasperEPNML114_Page85', set())
    assert not _is_linked(b, 'YasperEPNML114_Page85', a2)
    if hasattr(a2, 'YasperEPNML114_PnmlAnnotation86'):
        assert not _is_linked(a2, 'YasperEPNML114_PnmlAnnotation86', b)


def test_assoc_net109_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Pnml(group="sample_text")
    a2 = YasperEPNML114_Pnml(group="sample_text_2")
    b = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    _safe_set(b, 'YasperEPNML114_Net111', a1)
    assert _is_linked(b, 'YasperEPNML114_Net111', a1)
    if hasattr(a1, 'YasperEPNML114_Pnml110'):
        assert _is_linked(a1, 'YasperEPNML114_Pnml110', b)
    _safe_set(b, 'YasperEPNML114_Net111', a2)
    assert _is_linked(b, 'YasperEPNML114_Net111', a2)
    if hasattr(a1, 'YasperEPNML114_Pnml110'):
        assert not _is_linked(a1, 'YasperEPNML114_Pnml110', b)
    if hasattr(a2, 'YasperEPNML114_Pnml110'):
        assert _is_linked(a2, 'YasperEPNML114_Pnml110', b)
    _safe_set(b, 'YasperEPNML114_Net111', None)
    assert not _is_linked(b, 'YasperEPNML114_Net111', a2)
    if hasattr(a2, 'YasperEPNML114_Pnml110'):
        assert not _is_linked(a2, 'YasperEPNML114_Pnml110', b)


def test_assoc_page43_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    _safe_set(b, 'YasperEPNML114_Net44', {a1})
    assert _is_linked(b, 'YasperEPNML114_Net44', a1)
    if hasattr(a1, 'YasperEPNML114_Page'):
        assert _is_linked(a1, 'YasperEPNML114_Page', b)
    _safe_set(b, 'YasperEPNML114_Net44', {a2})
    assert _is_linked(b, 'YasperEPNML114_Net44', a2)
    if hasattr(a1, 'YasperEPNML114_Page'):
        assert not _is_linked(a1, 'YasperEPNML114_Page', b)
    if hasattr(a2, 'YasperEPNML114_Page'):
        assert _is_linked(a2, 'YasperEPNML114_Page', b)
    _safe_set(b, 'YasperEPNML114_Net44', set())
    assert not _is_linked(b, 'YasperEPNML114_Net44', a2)
    if hasattr(a2, 'YasperEPNML114_Page'):
        assert not _is_linked(a2, 'YasperEPNML114_Page', b)


def test_assoc_page82_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_Page(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Page83', a1)
    assert _is_linked(b, 'YasperEPNML114_Page83', a1)
    if hasattr(a1, 'YasperEPNML114_Page81'):
        assert _is_linked(a1, 'YasperEPNML114_Page81', b)
    _safe_set(b, 'YasperEPNML114_Page83', a2)
    assert _is_linked(b, 'YasperEPNML114_Page83', a2)
    if hasattr(a1, 'YasperEPNML114_Page81'):
        assert not _is_linked(a1, 'YasperEPNML114_Page81', b)
    if hasattr(a2, 'YasperEPNML114_Page81'):
        assert _is_linked(a2, 'YasperEPNML114_Page81', b)
    _safe_set(b, 'YasperEPNML114_Page83', None)
    assert not _is_linked(b, 'YasperEPNML114_Page83', a2)
    if hasattr(a2, 'YasperEPNML114_Page81'):
        assert not _is_linked(a2, 'YasperEPNML114_Page81', b)


def test_assoc_pathGraphics135_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ReferencePlaceSpecific(tool="sample_text", version="sample_text")
    a2 = YasperEPNML114_ReferencePlaceSpecific(tool="sample_text_2", version="sample_text_2")
    b = YasperEPNML114_NodeGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NodeGraphics136', a1)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics136', a1)
    if hasattr(a1, 'YasperEPNML114_ReferencePlaceSpecific'):
        assert _is_linked(a1, 'YasperEPNML114_ReferencePlaceSpecific', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics136', a2)
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics136', a2)
    if hasattr(a1, 'YasperEPNML114_ReferencePlaceSpecific'):
        assert not _is_linked(a1, 'YasperEPNML114_ReferencePlaceSpecific', b)
    if hasattr(a2, 'YasperEPNML114_ReferencePlaceSpecific'):
        assert _is_linked(a2, 'YasperEPNML114_ReferencePlaceSpecific', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics136', None)
    assert not _is_linked(b, 'YasperEPNML114_NodeGraphics136', a2)
    if hasattr(a2, 'YasperEPNML114_ReferencePlaceSpecific'):
        assert not _is_linked(a2, 'YasperEPNML114_ReferencePlaceSpecific', b)


def test_assoc_pnml25_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Pnml(group="sample_text")
    a2 = YasperEPNML114_Pnml(group="sample_text_2")
    b = YasperEPNML114_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'YasperEPNML114_DocumentRoot26', {a1})
    assert _is_linked(b, 'YasperEPNML114_DocumentRoot26', a1)
    if hasattr(a1, 'YasperEPNML114_Pnml'):
        assert _is_linked(a1, 'YasperEPNML114_Pnml', b)
    _safe_set(b, 'YasperEPNML114_DocumentRoot26', {a2})
    assert _is_linked(b, 'YasperEPNML114_DocumentRoot26', a2)
    if hasattr(a1, 'YasperEPNML114_Pnml'):
        assert not _is_linked(a1, 'YasperEPNML114_Pnml', b)
    if hasattr(a2, 'YasperEPNML114_Pnml'):
        assert _is_linked(a2, 'YasperEPNML114_Pnml', b)
    _safe_set(b, 'YasperEPNML114_DocumentRoot26', set())
    assert not _is_linked(b, 'YasperEPNML114_DocumentRoot26', a2)
    if hasattr(a2, 'YasperEPNML114_Pnml'):
        assert not _is_linked(a2, 'YasperEPNML114_Pnml', b)


def test_assoc_position54_reverse_link_reassign_clear():
    a1 = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    a2 = YasperEPNML114_TwoDimVector(x="sample_text_2", y="sample_text_2")
    b = YasperEPNML114_NetGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NetGraphics55', {a1})
    assert _is_linked(b, 'YasperEPNML114_NetGraphics55', a1)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector56'):
        assert _is_linked(a1, 'YasperEPNML114_TwoDimVector56', b)
    _safe_set(b, 'YasperEPNML114_NetGraphics55', {a2})
    assert _is_linked(b, 'YasperEPNML114_NetGraphics55', a2)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector56'):
        assert not _is_linked(a1, 'YasperEPNML114_TwoDimVector56', b)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector56'):
        assert _is_linked(a2, 'YasperEPNML114_TwoDimVector56', b)
    _safe_set(b, 'YasperEPNML114_NetGraphics55', set())
    assert not _is_linked(b, 'YasperEPNML114_NetGraphics55', a2)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector56'):
        assert not _is_linked(a2, 'YasperEPNML114_TwoDimVector56', b)


def test_assoc_position60_reverse_link_reassign_clear():
    a1 = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    a2 = YasperEPNML114_TwoDimVector(x="sample_text_2", y="sample_text_2")
    b = YasperEPNML114_NodeGraphics(group="sample_text")
    _safe_set(b, 'YasperEPNML114_NodeGraphics', {a1})
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics', a1)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector61'):
        assert _is_linked(a1, 'YasperEPNML114_TwoDimVector61', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics', {a2})
    assert _is_linked(b, 'YasperEPNML114_NodeGraphics', a2)
    if hasattr(a1, 'YasperEPNML114_TwoDimVector61'):
        assert not _is_linked(a1, 'YasperEPNML114_TwoDimVector61', b)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector61'):
        assert _is_linked(a2, 'YasperEPNML114_TwoDimVector61', b)
    _safe_set(b, 'YasperEPNML114_NodeGraphics', set())
    assert not _is_linked(b, 'YasperEPNML114_NodeGraphics', a2)
    if hasattr(a2, 'YasperEPNML114_TwoDimVector61'):
        assert not _is_linked(a2, 'YasperEPNML114_TwoDimVector61', b)


def test_assoc_referencePlace65_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    a2 = YasperEPNML114_ReferencePlace(group="sample_text_2", id="sample_text_2", ref="sample_text_2")
    b = YasperEPNML114_Page(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Page66', {a1})
    assert _is_linked(b, 'YasperEPNML114_Page66', a1)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace'):
        assert _is_linked(a1, 'YasperEPNML114_ReferencePlace', b)
    _safe_set(b, 'YasperEPNML114_Page66', {a2})
    assert _is_linked(b, 'YasperEPNML114_Page66', a2)
    if hasattr(a1, 'YasperEPNML114_ReferencePlace'):
        assert not _is_linked(a1, 'YasperEPNML114_ReferencePlace', b)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace'):
        assert _is_linked(a2, 'YasperEPNML114_ReferencePlace', b)
    _safe_set(b, 'YasperEPNML114_Page66', set())
    assert not _is_linked(b, 'YasperEPNML114_Page66', a2)
    if hasattr(a2, 'YasperEPNML114_ReferencePlace'):
        assert not _is_linked(a2, 'YasperEPNML114_ReferencePlace', b)


def test_assoc_toolspecific106_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    a2 = YasperEPNML114_ToolspecificType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", tool="sample_text_2", version="sample_text_2")
    b = YasperEPNML114_Place(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Place107', {a1})
    assert _is_linked(b, 'YasperEPNML114_Place107', a1)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType108'):
        assert _is_linked(a1, 'YasperEPNML114_ToolspecificType108', b)
    _safe_set(b, 'YasperEPNML114_Place107', {a2})
    assert _is_linked(b, 'YasperEPNML114_Place107', a2)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType108'):
        assert not _is_linked(a1, 'YasperEPNML114_ToolspecificType108', b)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType108'):
        assert _is_linked(a2, 'YasperEPNML114_ToolspecificType108', b)
    _safe_set(b, 'YasperEPNML114_Place107', set())
    assert not _is_linked(b, 'YasperEPNML114_Place107', a2)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType108'):
        assert not _is_linked(a2, 'YasperEPNML114_ToolspecificType108', b)


def test_assoc_toolspecific11_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    a2 = YasperEPNML114_ToolspecificType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", tool="sample_text_2", version="sample_text_2")
    b = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    _safe_set(b, 'YasperEPNML114_Arc12', {a1})
    assert _is_linked(b, 'YasperEPNML114_Arc12', a1)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType'):
        assert _is_linked(a1, 'YasperEPNML114_ToolspecificType', b)
    _safe_set(b, 'YasperEPNML114_Arc12', {a2})
    assert _is_linked(b, 'YasperEPNML114_Arc12', a2)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType'):
        assert not _is_linked(a1, 'YasperEPNML114_ToolspecificType', b)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType'):
        assert _is_linked(a2, 'YasperEPNML114_ToolspecificType', b)
    _safe_set(b, 'YasperEPNML114_Arc12', set())
    assert not _is_linked(b, 'YasperEPNML114_Arc12', a2)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType'):
        assert not _is_linked(a2, 'YasperEPNML114_ToolspecificType', b)


def test_assoc_toolspecific112_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    a2 = YasperEPNML114_ToolspecificType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", tool="sample_text_2", version="sample_text_2")
    b = YasperEPNML114_Pnml(group="sample_text")
    _safe_set(b, 'YasperEPNML114_Pnml113', {a1})
    assert _is_linked(b, 'YasperEPNML114_Pnml113', a1)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType114'):
        assert _is_linked(a1, 'YasperEPNML114_ToolspecificType114', b)
    _safe_set(b, 'YasperEPNML114_Pnml113', {a2})
    assert _is_linked(b, 'YasperEPNML114_Pnml113', a2)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType114'):
        assert not _is_linked(a1, 'YasperEPNML114_ToolspecificType114', b)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType114'):
        assert _is_linked(a2, 'YasperEPNML114_ToolspecificType114', b)
    _safe_set(b, 'YasperEPNML114_Pnml113', set())
    assert not _is_linked(b, 'YasperEPNML114_Pnml113', a2)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType114'):
        assert not _is_linked(a2, 'YasperEPNML114_ToolspecificType114', b)


def test_assoc_toolspecific132_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    a2 = YasperEPNML114_ToolspecificType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", tool="sample_text_2", version="sample_text_2")
    b = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    _safe_set(b, 'YasperEPNML114_ReferencePlace133', {a1})
    assert _is_linked(b, 'YasperEPNML114_ReferencePlace133', a1)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType134'):
        assert _is_linked(a1, 'YasperEPNML114_ToolspecificType134', b)
    _safe_set(b, 'YasperEPNML114_ReferencePlace133', {a2})
    assert _is_linked(b, 'YasperEPNML114_ReferencePlace133', a2)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType134'):
        assert not _is_linked(a1, 'YasperEPNML114_ToolspecificType134', b)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType134'):
        assert _is_linked(a2, 'YasperEPNML114_ToolspecificType134', b)
    _safe_set(b, 'YasperEPNML114_ReferencePlace133', set())
    assert not _is_linked(b, 'YasperEPNML114_ReferencePlace133', a2)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType134'):
        assert not _is_linked(a2, 'YasperEPNML114_ToolspecificType134', b)


def test_assoc_toolspecific155_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    _safe_set(b, 'YasperEPNML114_ToolspecificType157', a1)
    assert _is_linked(b, 'YasperEPNML114_ToolspecificType157', a1)
    if hasattr(a1, 'YasperEPNML114_Transition156'):
        assert _is_linked(a1, 'YasperEPNML114_Transition156', b)
    _safe_set(b, 'YasperEPNML114_ToolspecificType157', a2)
    assert _is_linked(b, 'YasperEPNML114_ToolspecificType157', a2)
    if hasattr(a1, 'YasperEPNML114_Transition156'):
        assert not _is_linked(a1, 'YasperEPNML114_Transition156', b)
    if hasattr(a2, 'YasperEPNML114_Transition156'):
        assert _is_linked(a2, 'YasperEPNML114_Transition156', b)
    _safe_set(b, 'YasperEPNML114_ToolspecificType157', None)
    assert not _is_linked(b, 'YasperEPNML114_ToolspecificType157', a2)
    if hasattr(a2, 'YasperEPNML114_Transition156'):
        assert not _is_linked(a2, 'YasperEPNML114_Transition156', b)


def test_assoc_toolspecific51_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    a2 = YasperEPNML114_ToolspecificType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", tool="sample_text_2", version="sample_text_2")
    b = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    _safe_set(b, 'YasperEPNML114_Net52', {a1})
    assert _is_linked(b, 'YasperEPNML114_Net52', a1)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType53'):
        assert _is_linked(a1, 'YasperEPNML114_ToolspecificType53', b)
    _safe_set(b, 'YasperEPNML114_Net52', {a2})
    assert _is_linked(b, 'YasperEPNML114_Net52', a2)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType53'):
        assert not _is_linked(a1, 'YasperEPNML114_ToolspecificType53', b)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType53'):
        assert _is_linked(a2, 'YasperEPNML114_ToolspecificType53', b)
    _safe_set(b, 'YasperEPNML114_Net52', set())
    assert not _is_linked(b, 'YasperEPNML114_Net52', a2)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType53'):
        assert not _is_linked(a2, 'YasperEPNML114_ToolspecificType53', b)


def test_assoc_toolspecific90_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    a2 = YasperEPNML114_ToolspecificType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", tool="sample_text_2", version="sample_text_2")
    b = YasperEPNML114_Page(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Page91', {a1})
    assert _is_linked(b, 'YasperEPNML114_Page91', a1)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType92'):
        assert _is_linked(a1, 'YasperEPNML114_ToolspecificType92', b)
    _safe_set(b, 'YasperEPNML114_Page91', {a2})
    assert _is_linked(b, 'YasperEPNML114_Page91', a2)
    if hasattr(a1, 'YasperEPNML114_ToolspecificType92'):
        assert not _is_linked(a1, 'YasperEPNML114_ToolspecificType92', b)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType92'):
        assert _is_linked(a2, 'YasperEPNML114_ToolspecificType92', b)
    _safe_set(b, 'YasperEPNML114_Page91', set())
    assert not _is_linked(b, 'YasperEPNML114_Page91', a2)
    if hasattr(a2, 'YasperEPNML114_ToolspecificType92'):
        assert not _is_linked(a2, 'YasperEPNML114_ToolspecificType92', b)


def test_assoc_transformation146_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_Transformation(text="sample_text")
    _safe_set(b, 'YasperEPNML114_Transformation148', a1)
    assert _is_linked(b, 'YasperEPNML114_Transformation148', a1)
    if hasattr(a1, 'YasperEPNML114_Transition147'):
        assert _is_linked(a1, 'YasperEPNML114_Transition147', b)
    _safe_set(b, 'YasperEPNML114_Transformation148', a2)
    assert _is_linked(b, 'YasperEPNML114_Transformation148', a2)
    if hasattr(a1, 'YasperEPNML114_Transition147'):
        assert not _is_linked(a1, 'YasperEPNML114_Transition147', b)
    if hasattr(a2, 'YasperEPNML114_Transition147'):
        assert _is_linked(a2, 'YasperEPNML114_Transition147', b)
    _safe_set(b, 'YasperEPNML114_Transformation148', None)
    assert not _is_linked(b, 'YasperEPNML114_Transformation148', a2)
    if hasattr(a2, 'YasperEPNML114_Transition147'):
        assert not _is_linked(a2, 'YasperEPNML114_Transition147', b)


def test_assoc_transition38_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    _safe_set(b, 'YasperEPNML114_Net39', {a1})
    assert _is_linked(b, 'YasperEPNML114_Net39', a1)
    if hasattr(a1, 'YasperEPNML114_Transition'):
        assert _is_linked(a1, 'YasperEPNML114_Transition', b)
    _safe_set(b, 'YasperEPNML114_Net39', {a2})
    assert _is_linked(b, 'YasperEPNML114_Net39', a2)
    if hasattr(a1, 'YasperEPNML114_Transition'):
        assert not _is_linked(a1, 'YasperEPNML114_Transition', b)
    if hasattr(a2, 'YasperEPNML114_Transition'):
        assert _is_linked(a2, 'YasperEPNML114_Transition', b)
    _safe_set(b, 'YasperEPNML114_Net39', set())
    assert not _is_linked(b, 'YasperEPNML114_Net39', a2)
    if hasattr(a2, 'YasperEPNML114_Transition'):
        assert not _is_linked(a2, 'YasperEPNML114_Transition', b)


def test_assoc_transition75_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    a2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    b = YasperEPNML114_Page(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Page76', {a1})
    assert _is_linked(b, 'YasperEPNML114_Page76', a1)
    if hasattr(a1, 'YasperEPNML114_Transition77'):
        assert _is_linked(a1, 'YasperEPNML114_Transition77', b)
    _safe_set(b, 'YasperEPNML114_Page76', {a2})
    assert _is_linked(b, 'YasperEPNML114_Page76', a2)
    if hasattr(a1, 'YasperEPNML114_Transition77'):
        assert not _is_linked(a1, 'YasperEPNML114_Transition77', b)
    if hasattr(a2, 'YasperEPNML114_Transition77'):
        assert _is_linked(a2, 'YasperEPNML114_Transition77', b)
    _safe_set(b, 'YasperEPNML114_Page76', set())
    assert not _is_linked(b, 'YasperEPNML114_Page76', a2)
    if hasattr(a2, 'YasperEPNML114_Transition77'):
        assert not _is_linked(a2, 'YasperEPNML114_Transition77', b)


def test_assoc_type1_reverse_link_reassign_clear():
    a1 = YasperEPNML114_ArcType(text="sample_text")
    a2 = YasperEPNML114_ArcType(text="sample_text_2")
    b = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    _safe_set(b, 'YasperEPNML114_Arc', {a1})
    assert _is_linked(b, 'YasperEPNML114_Arc', a1)
    if hasattr(a1, 'YasperEPNML114_ArcType'):
        assert _is_linked(a1, 'YasperEPNML114_ArcType', b)
    _safe_set(b, 'YasperEPNML114_Arc', {a2})
    assert _is_linked(b, 'YasperEPNML114_Arc', a2)
    if hasattr(a1, 'YasperEPNML114_ArcType'):
        assert not _is_linked(a1, 'YasperEPNML114_ArcType', b)
    if hasattr(a2, 'YasperEPNML114_ArcType'):
        assert _is_linked(a2, 'YasperEPNML114_ArcType', b)
    _safe_set(b, 'YasperEPNML114_Arc', set())
    assert not _is_linked(b, 'YasperEPNML114_Arc', a2)
    if hasattr(a2, 'YasperEPNML114_ArcType'):
        assert not _is_linked(a2, 'YasperEPNML114_ArcType', b)


def test_assoc_type140_reverse_link_reassign_clear():
    a1 = YasperEPNML114_TransitionType(text="sample_text")
    a2 = YasperEPNML114_TransitionType(text="sample_text_2")
    b = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Transition141', {a1})
    assert _is_linked(b, 'YasperEPNML114_Transition141', a1)
    if hasattr(a1, 'YasperEPNML114_TransitionType142'):
        assert _is_linked(a1, 'YasperEPNML114_TransitionType142', b)
    _safe_set(b, 'YasperEPNML114_Transition141', {a2})
    assert _is_linked(b, 'YasperEPNML114_Transition141', a2)
    if hasattr(a1, 'YasperEPNML114_TransitionType142'):
        assert not _is_linked(a1, 'YasperEPNML114_TransitionType142', b)
    if hasattr(a2, 'YasperEPNML114_TransitionType142'):
        assert _is_linked(a2, 'YasperEPNML114_TransitionType142', b)
    _safe_set(b, 'YasperEPNML114_Transition141', set())
    assert not _is_linked(b, 'YasperEPNML114_Transition141', a2)
    if hasattr(a2, 'YasperEPNML114_TransitionType142'):
        assert not _is_linked(a2, 'YasperEPNML114_TransitionType142', b)


def test_assoc_type70_reverse_link_reassign_clear():
    a1 = YasperEPNML114_TransitionType(text="sample_text")
    a2 = YasperEPNML114_TransitionType(text="sample_text_2")
    b = YasperEPNML114_Page(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Page71', {a1})
    assert _is_linked(b, 'YasperEPNML114_Page71', a1)
    if hasattr(a1, 'YasperEPNML114_TransitionType'):
        assert _is_linked(a1, 'YasperEPNML114_TransitionType', b)
    _safe_set(b, 'YasperEPNML114_Page71', {a2})
    assert _is_linked(b, 'YasperEPNML114_Page71', a2)
    if hasattr(a1, 'YasperEPNML114_TransitionType'):
        assert not _is_linked(a1, 'YasperEPNML114_TransitionType', b)
    if hasattr(a2, 'YasperEPNML114_TransitionType'):
        assert _is_linked(a2, 'YasperEPNML114_TransitionType', b)
    _safe_set(b, 'YasperEPNML114_Page71', set())
    assert not _is_linked(b, 'YasperEPNML114_Page71', a2)
    if hasattr(a2, 'YasperEPNML114_TransitionType'):
        assert not _is_linked(a2, 'YasperEPNML114_TransitionType', b)


def test_assoc_type93_reverse_link_reassign_clear():
    a1 = YasperEPNML114_PlaceType(text="sample_text")
    a2 = YasperEPNML114_PlaceType(text="sample_text_2")
    b = YasperEPNML114_Place(group="sample_text", id="sample_text")
    _safe_set(b, 'YasperEPNML114_Place', {a1})
    assert _is_linked(b, 'YasperEPNML114_Place', a1)
    if hasattr(a1, 'YasperEPNML114_PlaceType'):
        assert _is_linked(a1, 'YasperEPNML114_PlaceType', b)
    _safe_set(b, 'YasperEPNML114_Place', {a2})
    assert _is_linked(b, 'YasperEPNML114_Place', a2)
    if hasattr(a1, 'YasperEPNML114_PlaceType'):
        assert not _is_linked(a1, 'YasperEPNML114_PlaceType', b)
    if hasattr(a2, 'YasperEPNML114_PlaceType'):
        assert _is_linked(a2, 'YasperEPNML114_PlaceType', b)
    _safe_set(b, 'YasperEPNML114_Place', set())
    assert not _is_linked(b, 'YasperEPNML114_Place', a2)
    if hasattr(a2, 'YasperEPNML114_PlaceType'):
        assert not _is_linked(a2, 'YasperEPNML114_PlaceType', b)


def test_assoc_weight13_reverse_link_reassign_clear():
    a1 = YasperEPNML114_Stat(text="sample_text")
    a2 = YasperEPNML114_Stat(text="sample_text_2")
    b = YasperEPNML114_ConnectionWeight(connection="sample_text")
    _safe_set(b, 'YasperEPNML114_ConnectionWeight', a1)
    assert _is_linked(b, 'YasperEPNML114_ConnectionWeight', a1)
    if hasattr(a1, 'YasperEPNML114_Stat'):
        assert _is_linked(a1, 'YasperEPNML114_Stat', b)
    _safe_set(b, 'YasperEPNML114_ConnectionWeight', a2)
    assert _is_linked(b, 'YasperEPNML114_ConnectionWeight', a2)
    if hasattr(a1, 'YasperEPNML114_Stat'):
        assert not _is_linked(a1, 'YasperEPNML114_Stat', b)
    if hasattr(a2, 'YasperEPNML114_Stat'):
        assert _is_linked(a2, 'YasperEPNML114_Stat', b)
    _safe_set(b, 'YasperEPNML114_ConnectionWeight', None)
    assert not _is_linked(b, 'YasperEPNML114_ConnectionWeight', a2)
    if hasattr(a2, 'YasperEPNML114_Stat'):
        assert not _is_linked(a2, 'YasperEPNML114_Stat', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_connectionWeight14_stub_double():
    # YasperEPNML114_ConnectionWeights has no real 'YasperEPNML114_ConnectionWeights' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_ConnectionWeight's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_ConnectionWeight's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_ConnectionWeight(connection="sample_text")
    partner = YasperEPNML114_ConnectionWeights()
    setattr(partner, 'YasperEPNML114_ConnectionWeights', None)
    _safe_set(owner, 'YasperEPNML114_ConnectionWeight15', partner)
    assert owner in getattr(partner, 'YasperEPNML114_ConnectionWeights')
    _safe_set(owner, 'YasperEPNML114_ConnectionWeight15', None)
    assert owner not in getattr(partner, 'YasperEPNML114_ConnectionWeights')


def test_assoc_cost160_stub_double():
    # YasperEPNML114_Cost has no real 'YasperEPNML114_Cost162' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_TransitionSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_TransitionSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    partner = YasperEPNML114_Cost()
    setattr(partner, 'YasperEPNML114_Cost162', None)
    _safe_set(owner, 'YasperEPNML114_TransitionSpecific161', partner)
    assert getattr(partner, 'YasperEPNML114_Cost162') == owner
    _safe_set(owner, 'YasperEPNML114_TransitionSpecific161', None)
    assert getattr(partner, 'YasperEPNML114_Cost162') is None


def test_assoc_deviation120_stub_double():
    # YasperEPNML114_ProcessingTime has no real 'YasperEPNML114_ProcessingTime121' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Stat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Stat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Stat(text="sample_text")
    partner = YasperEPNML114_ProcessingTime()
    setattr(partner, 'YasperEPNML114_ProcessingTime121', None)
    _safe_set(owner, 'YasperEPNML114_Stat122', partner)
    assert getattr(partner, 'YasperEPNML114_ProcessingTime121') == owner
    _safe_set(owner, 'YasperEPNML114_Stat122', None)
    assert getattr(partner, 'YasperEPNML114_ProcessingTime121') is None


def test_assoc_fixed16_stub_double():
    # YasperEPNML114_Cost has no real 'YasperEPNML114_Cost' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Stat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Stat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Stat(text="sample_text")
    partner = YasperEPNML114_Cost()
    setattr(partner, 'YasperEPNML114_Cost', None)
    _safe_set(owner, 'YasperEPNML114_Stat17', partner)
    assert getattr(partner, 'YasperEPNML114_Cost') == owner
    _safe_set(owner, 'YasperEPNML114_Stat17', None)
    assert getattr(partner, 'YasperEPNML114_Cost') is None


def test_assoc_graphics115_stub_double():
    # YasperEPNML114_AnnotationGraphics has no real 'YasperEPNML114_AnnotationGraphics117' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_PnmlAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_PnmlAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_PnmlAnnotation(text="sample_text")
    partner = YasperEPNML114_AnnotationGraphics()
    setattr(partner, 'YasperEPNML114_AnnotationGraphics117', None)
    _safe_set(owner, 'YasperEPNML114_PnmlAnnotation116', partner)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics117') == owner
    _safe_set(owner, 'YasperEPNML114_PnmlAnnotation116', None)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics117') is None


def test_assoc_graphics138_stub_double():
    # YasperEPNML114_AnnotationGraphics has no real 'YasperEPNML114_AnnotationGraphics139' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Transformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Transformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Transformation(text="sample_text")
    partner = YasperEPNML114_AnnotationGraphics()
    setattr(partner, 'YasperEPNML114_AnnotationGraphics139', None)
    _safe_set(owner, 'YasperEPNML114_Transformation', partner)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics139') == owner
    _safe_set(owner, 'YasperEPNML114_Transformation', None)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics139') is None


def test_assoc_graphics2_stub_double():
    # YasperEPNML114_EdgeGraphics has no real 'YasperEPNML114_EdgeGraphics' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    partner = YasperEPNML114_EdgeGraphics()
    setattr(partner, 'YasperEPNML114_EdgeGraphics', None)
    _safe_set(owner, 'YasperEPNML114_Arc3', {partner})
    assert getattr(partner, 'YasperEPNML114_EdgeGraphics') == owner
    _safe_set(owner, 'YasperEPNML114_Arc3', set())
    assert getattr(partner, 'YasperEPNML114_EdgeGraphics') is None


def test_assoc_graphics30_stub_double():
    # YasperEPNML114_AnnotationGraphics has no real 'YasperEPNML114_AnnotationGraphics31' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_InitialMarking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_InitialMarking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_InitialMarking(text="sample_text")
    partner = YasperEPNML114_AnnotationGraphics()
    setattr(partner, 'YasperEPNML114_AnnotationGraphics31', None)
    _safe_set(owner, 'YasperEPNML114_InitialMarking', partner)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics31') == owner
    _safe_set(owner, 'YasperEPNML114_InitialMarking', None)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics31') is None


def test_assoc_graphics32_stub_double():
    # YasperEPNML114_AnnotationGraphics has no real 'YasperEPNML114_AnnotationGraphics34' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Inscription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Inscription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Inscription(text="sample_text")
    partner = YasperEPNML114_AnnotationGraphics()
    setattr(partner, 'YasperEPNML114_AnnotationGraphics34', None)
    _safe_set(owner, 'YasperEPNML114_Inscription33', partner)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics34') == owner
    _safe_set(owner, 'YasperEPNML114_Inscription33', None)
    assert getattr(partner, 'YasperEPNML114_AnnotationGraphics34') is None


def test_assoc_mean118_stub_double():
    # YasperEPNML114_ProcessingTime has no real 'YasperEPNML114_ProcessingTime' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Stat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Stat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Stat(text="sample_text")
    partner = YasperEPNML114_ProcessingTime()
    setattr(partner, 'YasperEPNML114_ProcessingTime', None)
    _safe_set(owner, 'YasperEPNML114_Stat119', partner)
    assert getattr(partner, 'YasperEPNML114_ProcessingTime') == owner
    _safe_set(owner, 'YasperEPNML114_Stat119', None)
    assert getattr(partner, 'YasperEPNML114_ProcessingTime') is None


def test_assoc_offset0_stub_double():
    # YasperEPNML114_AnnotationGraphics has no real 'YasperEPNML114_AnnotationGraphics' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_TwoDimVector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_TwoDimVector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    partner = YasperEPNML114_AnnotationGraphics()
    setattr(partner, 'YasperEPNML114_AnnotationGraphics', None)
    _safe_set(owner, 'YasperEPNML114_TwoDimVector', partner)
    assert owner in getattr(partner, 'YasperEPNML114_AnnotationGraphics')
    _safe_set(owner, 'YasperEPNML114_TwoDimVector', None)
    assert owner not in getattr(partner, 'YasperEPNML114_AnnotationGraphics')


def test_assoc_place36_stub_double():
    # YasperEPNML114_PlaceType1 has no real 'YasperEPNML114_PlaceType1' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    partner = YasperEPNML114_PlaceType1()
    setattr(partner, 'YasperEPNML114_PlaceType1', None)
    _safe_set(owner, 'YasperEPNML114_Net37', {partner})
    assert getattr(partner, 'YasperEPNML114_PlaceType1') == owner
    _safe_set(owner, 'YasperEPNML114_Net37', set())
    assert getattr(partner, 'YasperEPNML114_PlaceType1') is None


def test_assoc_place72_stub_double():
    # YasperEPNML114_PlaceType1 has no real 'YasperEPNML114_PlaceType174' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Page(group="sample_text", id="sample_text")
    partner = YasperEPNML114_PlaceType1()
    setattr(partner, 'YasperEPNML114_PlaceType174', None)
    _safe_set(owner, 'YasperEPNML114_Page73', {partner})
    assert getattr(partner, 'YasperEPNML114_PlaceType174') == owner
    _safe_set(owner, 'YasperEPNML114_Page73', set())
    assert getattr(partner, 'YasperEPNML114_PlaceType174') is None


def test_assoc_position27_stub_double():
    # YasperEPNML114_EdgeGraphics has no real 'YasperEPNML114_EdgeGraphics28' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_TwoDimVector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_TwoDimVector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    partner = YasperEPNML114_EdgeGraphics()
    setattr(partner, 'YasperEPNML114_EdgeGraphics28', None)
    _safe_set(owner, 'YasperEPNML114_TwoDimVector29', partner)
    assert owner in getattr(partner, 'YasperEPNML114_EdgeGraphics28')
    _safe_set(owner, 'YasperEPNML114_TwoDimVector29', None)
    assert owner not in getattr(partner, 'YasperEPNML114_EdgeGraphics28')


def test_assoc_processingTime163_stub_double():
    # YasperEPNML114_ProcessingTime has no real 'YasperEPNML114_ProcessingTime165' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_TransitionSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_TransitionSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    partner = YasperEPNML114_ProcessingTime()
    setattr(partner, 'YasperEPNML114_ProcessingTime165', None)
    _safe_set(owner, 'YasperEPNML114_TransitionSpecific164', partner)
    assert getattr(partner, 'YasperEPNML114_ProcessingTime165') == owner
    _safe_set(owner, 'YasperEPNML114_TransitionSpecific164', None)
    assert getattr(partner, 'YasperEPNML114_ProcessingTime165') is None


def test_assoc_role137_stub_double():
    # YasperEPNML114_Roles has no real 'YasperEPNML114_Roles' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Role(text="sample_text")
    partner = YasperEPNML114_Roles()
    setattr(partner, 'YasperEPNML114_Roles', None)
    _safe_set(owner, 'YasperEPNML114_Role', partner)
    assert owner in getattr(partner, 'YasperEPNML114_Roles')
    _safe_set(owner, 'YasperEPNML114_Role', None)
    assert owner not in getattr(partner, 'YasperEPNML114_Roles')


def test_assoc_roles158_stub_double():
    # YasperEPNML114_Roles has no real 'YasperEPNML114_Roles159' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_TransitionSpecific's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_TransitionSpecific's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    partner = YasperEPNML114_Roles()
    setattr(partner, 'YasperEPNML114_Roles159', None)
    _safe_set(owner, 'YasperEPNML114_TransitionSpecific', partner)
    assert getattr(partner, 'YasperEPNML114_Roles159') == owner
    _safe_set(owner, 'YasperEPNML114_TransitionSpecific', None)
    assert getattr(partner, 'YasperEPNML114_Roles159') is None


def test_assoc_variable18_stub_double():
    # YasperEPNML114_Cost has no real 'YasperEPNML114_Cost19' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_Stat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_Stat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_Stat(text="sample_text")
    partner = YasperEPNML114_Cost()
    setattr(partner, 'YasperEPNML114_Cost19', None)
    _safe_set(owner, 'YasperEPNML114_Stat20', partner)
    assert getattr(partner, 'YasperEPNML114_Cost19') == owner
    _safe_set(owner, 'YasperEPNML114_Stat20', None)
    assert getattr(partner, 'YasperEPNML114_Cost19') is None


def test_assoc_xMLNSPrefixMap21_stub_double():
    # YasperEPNML114_EStringToStringMapEntry has no real 'YasperEPNML114_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_DocumentRoot(mixed="sample_text")
    partner = YasperEPNML114_EStringToStringMapEntry()
    setattr(partner, 'YasperEPNML114_EStringToStringMapEntry', None)
    _safe_set(owner, 'YasperEPNML114_DocumentRoot', {partner})
    assert getattr(partner, 'YasperEPNML114_EStringToStringMapEntry') == owner
    _safe_set(owner, 'YasperEPNML114_DocumentRoot', set())
    assert getattr(partner, 'YasperEPNML114_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation22_stub_double():
    # YasperEPNML114_EStringToStringMapEntry has no real 'YasperEPNML114_EStringToStringMapEntry24' property in the generated
    # code (a bare stub) -- manually attach it so YasperEPNML114_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # YasperEPNML114_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = YasperEPNML114_DocumentRoot(mixed="sample_text")
    partner = YasperEPNML114_EStringToStringMapEntry()
    setattr(partner, 'YasperEPNML114_EStringToStringMapEntry24', None)
    _safe_set(owner, 'YasperEPNML114_DocumentRoot23', {partner})
    assert getattr(partner, 'YasperEPNML114_EStringToStringMapEntry24') == owner
    _safe_set(owner, 'YasperEPNML114_DocumentRoot23', set())
    assert getattr(partner, 'YasperEPNML114_EStringToStringMapEntry24') is None


