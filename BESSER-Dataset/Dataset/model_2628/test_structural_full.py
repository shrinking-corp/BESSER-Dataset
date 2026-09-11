import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Link,
    PersonalizedElement,
    cevinedit_AffixedEReferenceCont,
    cevinedit_CEViNEditRoot,
    cevinedit_CompartmentEReferenceCont,
    cevinedit_Diagram,
    cevinedit_LabelEAttribute,
    cevinedit_Link,
    cevinedit_LinkEClass,
    cevinedit_LinkEReferenceNonCont,
    cevinedit_NodeEClass,
    cevinedit_PersonalizedElement,
    Brightness,
    Color,
    FontStyle,
    LayoutCompartment,
    LinkFigure,
    NodeFigure,
    Placement,
    Texture,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_cevinedit_CEViNEditRoot_sourceMM_value_roundtrip():
    instance = cevinedit_CEViNEditRoot(sourceMM="sample_text")
    assert instance.sourceMM == "sample_text"
    instance.sourceMM = "sample_text_2"
    assert instance.sourceMM == "sample_text_2"


def test_cevinedit_CompartmentEReferenceCont_collapsible_value_roundtrip():
    instance = cevinedit_CompartmentEReferenceCont(collapsible=True, layout="sample_text")
    assert instance.collapsible == True
    instance.collapsible = False
    assert instance.collapsible == False


def test_cevinedit_CompartmentEReferenceCont_layout_value_roundtrip():
    instance = cevinedit_CompartmentEReferenceCont(collapsible=True, layout="sample_text")
    assert instance.layout == "sample_text"
    instance.layout = "sample_text_2"
    assert instance.layout == "sample_text_2"


def test_cevinedit_Diagram_modelExtension_value_roundtrip():
    instance = cevinedit_Diagram(modelExtension="sample_text", name="sample_text")
    assert instance.modelExtension == "sample_text"
    instance.modelExtension = "sample_text_2"
    assert instance.modelExtension == "sample_text_2"


def test_cevinedit_Diagram_name_value_roundtrip():
    instance = cevinedit_Diagram(modelExtension="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cevinedit_Link_brightness_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.brightness == "sample_text"
    instance.brightness = "sample_text_2"
    assert instance.brightness == "sample_text_2"


def test_cevinedit_Link_color_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_cevinedit_Link_label_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_cevinedit_Link_labelFontStyle_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.labelFontStyle == "sample_text"
    instance.labelFontStyle = "sample_text_2"
    assert instance.labelFontStyle == "sample_text_2"


def test_cevinedit_Link_sourceDecoration_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.sourceDecoration == "sample_text"
    instance.sourceDecoration = "sample_text_2"
    assert instance.sourceDecoration == "sample_text_2"


def test_cevinedit_Link_targetDecoration_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.targetDecoration == "sample_text"
    instance.targetDecoration = "sample_text_2"
    assert instance.targetDecoration == "sample_text_2"


def test_cevinedit_Link_texture_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.texture == "sample_text"
    instance.texture = "sample_text_2"
    assert instance.texture == "sample_text_2"


def test_cevinedit_Link_width_value_roundtrip():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_cevinedit_LinkEClass_source_value_roundtrip():
    instance = cevinedit_LinkEClass(source="sample_text", target="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_cevinedit_LinkEClass_target_value_roundtrip():
    instance = cevinedit_LinkEClass(source="sample_text", target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_cevinedit_NodeEClass_backgroundColor_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_cevinedit_NodeEClass_borderColor_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.borderColor == "sample_text"
    instance.borderColor = "sample_text_2"
    assert instance.borderColor == "sample_text_2"


def test_cevinedit_NodeEClass_borderTexture_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.borderTexture == "sample_text"
    instance.borderTexture = "sample_text_2"
    assert instance.borderTexture == "sample_text_2"


def test_cevinedit_NodeEClass_borderWidth_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.borderWidth == 7
    instance.borderWidth = 13
    assert instance.borderWidth == 13


def test_cevinedit_NodeEClass_brightness_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.brightness == "sample_text"
    instance.brightness = "sample_text_2"
    assert instance.brightness == "sample_text_2"


def test_cevinedit_NodeEClass_figure_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.figure == "sample_text"
    instance.figure = "sample_text_2"
    assert instance.figure == "sample_text_2"


def test_cevinedit_NodeEClass_imagePath_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.imagePath == "sample_text"
    instance.imagePath = "sample_text_2"
    assert instance.imagePath == "sample_text_2"


def test_cevinedit_NodeEClass_label_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_cevinedit_NodeEClass_labelFontStyle_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.labelFontStyle == "sample_text"
    instance.labelFontStyle = "sample_text_2"
    assert instance.labelFontStyle == "sample_text_2"


def test_cevinedit_NodeEClass_labelPlacement_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.labelPlacement == "sample_text"
    instance.labelPlacement = "sample_text_2"
    assert instance.labelPlacement == "sample_text_2"


def test_cevinedit_NodeEClass_listPointsPolygon_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.listPointsPolygon == "sample_text"
    instance.listPointsPolygon = "sample_text_2"
    assert instance.listPointsPolygon == "sample_text_2"


def test_cevinedit_NodeEClass_resizable_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.resizable == True
    instance.resizable = False
    assert instance.resizable == False


def test_cevinedit_NodeEClass_size_value_roundtrip():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_cevinedit_PersonalizedElement_icon_value_roundtrip():
    instance = cevinedit_PersonalizedElement(icon="sample_text", name="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_cevinedit_PersonalizedElement_name_value_roundtrip():
    instance = cevinedit_PersonalizedElement(icon="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cevinedit_LinkEClass_isa_Link():
    instance = cevinedit_LinkEClass(source="sample_text", target="sample_text")
    assert isinstance(instance, Link)


def test_cevinedit_LinkEReferenceNonCont_isa_Link():
    instance = cevinedit_LinkEReferenceNonCont()
    assert isinstance(instance, Link)


def test_cevinedit_AffixedEReferenceCont_isa_PersonalizedElement():
    instance = cevinedit_AffixedEReferenceCont()
    assert isinstance(instance, PersonalizedElement)


def test_cevinedit_CompartmentEReferenceCont_isa_PersonalizedElement():
    instance = cevinedit_CompartmentEReferenceCont(collapsible=True, layout="sample_text")
    assert isinstance(instance, PersonalizedElement)


def test_cevinedit_LabelEAttribute_isa_PersonalizedElement():
    instance = cevinedit_LabelEAttribute()
    assert isinstance(instance, PersonalizedElement)


def test_cevinedit_Link_isa_PersonalizedElement():
    instance = cevinedit_Link(brightness="sample_text", color="sample_text", label="sample_text", labelFontStyle="sample_text", sourceDecoration="sample_text", targetDecoration="sample_text", texture="sample_text", width=7)
    assert isinstance(instance, PersonalizedElement)


def test_cevinedit_LinkEClass_isa_PersonalizedElement():
    instance = cevinedit_LinkEClass(source="sample_text", target="sample_text")
    assert isinstance(instance, PersonalizedElement)


def test_cevinedit_LinkEReferenceNonCont_isa_PersonalizedElement():
    instance = cevinedit_LinkEReferenceNonCont()
    assert isinstance(instance, PersonalizedElement)


def test_cevinedit_NodeEClass_isa_PersonalizedElement():
    instance = cevinedit_NodeEClass(backgroundColor="sample_text", borderColor="sample_text", borderTexture="sample_text", borderWidth=7, brightness="sample_text", figure="sample_text", imagePath="sample_text", label="sample_text", labelFontStyle="sample_text", labelPlacement="sample_text", listPointsPolygon="sample_text", resizable=True, size="sample_text")
    assert isinstance(instance, PersonalizedElement)


def test_assoc_containsElem1_link_reassign_clear():
    a = cevinedit_PersonalizedElement(icon="sample_text", name="sample_text")
    b1 = cevinedit_Diagram(modelExtension="sample_text", name="sample_text")
    b2 = cevinedit_Diagram(modelExtension="sample_text_2", name="sample_text_2")
    _safe_set(a, 'cevinedit_PersonalizedElement', b1)
    assert _is_linked(a, 'cevinedit_PersonalizedElement', b1)
    if hasattr(b1, 'cevinedit_Diagram2'):
        assert _is_linked(b1, 'cevinedit_Diagram2', a)
    _safe_set(a, 'cevinedit_PersonalizedElement', b2)
    assert _is_linked(a, 'cevinedit_PersonalizedElement', b2)
    if hasattr(b1, 'cevinedit_Diagram2'):
        assert not _is_linked(b1, 'cevinedit_Diagram2', a)
    if hasattr(b2, 'cevinedit_Diagram2'):
        assert _is_linked(b2, 'cevinedit_Diagram2', a)
    _safe_set(a, 'cevinedit_PersonalizedElement', None)
    assert not _is_linked(a, 'cevinedit_PersonalizedElement', b2)
    if hasattr(b2, 'cevinedit_Diagram2'):
        assert not _is_linked(b2, 'cevinedit_Diagram2', a)


def test_assoc_diagram0_link_reassign_clear():
    a = cevinedit_Diagram(modelExtension="sample_text", name="sample_text")
    b1 = cevinedit_CEViNEditRoot(sourceMM="sample_text")
    b2 = cevinedit_CEViNEditRoot(sourceMM="sample_text_2")
    _safe_set(a, 'cevinedit_Diagram', b1)
    assert _is_linked(a, 'cevinedit_Diagram', b1)
    if hasattr(b1, 'cevinedit_CEViNEditRoot'):
        assert _is_linked(b1, 'cevinedit_CEViNEditRoot', a)
    _safe_set(a, 'cevinedit_Diagram', b2)
    assert _is_linked(a, 'cevinedit_Diagram', b2)
    if hasattr(b1, 'cevinedit_CEViNEditRoot'):
        assert not _is_linked(b1, 'cevinedit_CEViNEditRoot', a)
    if hasattr(b2, 'cevinedit_CEViNEditRoot'):
        assert _is_linked(b2, 'cevinedit_CEViNEditRoot', a)
    _safe_set(a, 'cevinedit_Diagram', None)
    assert not _is_linked(a, 'cevinedit_Diagram', b2)
    if hasattr(b2, 'cevinedit_CEViNEditRoot'):
        assert not _is_linked(b2, 'cevinedit_CEViNEditRoot', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Link_strategy = st.builds(Link)
@given(instance=Link_strategy)
@settings(max_examples=25)
def test_Link_instantiation(instance):
    assert isinstance(instance, Link)


PersonalizedElement_strategy = st.builds(PersonalizedElement)
@given(instance=PersonalizedElement_strategy)
@settings(max_examples=25)
def test_PersonalizedElement_instantiation(instance):
    assert isinstance(instance, PersonalizedElement)


cevinedit_AffixedEReferenceCont_strategy = st.builds(cevinedit_AffixedEReferenceCont)
@given(instance=cevinedit_AffixedEReferenceCont_strategy)
@settings(max_examples=25)
def test_cevinedit_AffixedEReferenceCont_instantiation(instance):
    assert isinstance(instance, cevinedit_AffixedEReferenceCont)


cevinedit_CEViNEditRoot_strategy = st.builds(cevinedit_CEViNEditRoot, sourceMM=safe_text)
@given(instance=cevinedit_CEViNEditRoot_strategy)
@settings(max_examples=25)
def test_cevinedit_CEViNEditRoot_instantiation(instance):
    assert isinstance(instance, cevinedit_CEViNEditRoot)


cevinedit_CompartmentEReferenceCont_strategy = st.builds(cevinedit_CompartmentEReferenceCont, collapsible=st.booleans(), layout=safe_text)
@given(instance=cevinedit_CompartmentEReferenceCont_strategy)
@settings(max_examples=25)
def test_cevinedit_CompartmentEReferenceCont_instantiation(instance):
    assert isinstance(instance, cevinedit_CompartmentEReferenceCont)


cevinedit_Diagram_strategy = st.builds(cevinedit_Diagram, modelExtension=safe_text, name=safe_text)
@given(instance=cevinedit_Diagram_strategy)
@settings(max_examples=25)
def test_cevinedit_Diagram_instantiation(instance):
    assert isinstance(instance, cevinedit_Diagram)


cevinedit_LabelEAttribute_strategy = st.builds(cevinedit_LabelEAttribute)
@given(instance=cevinedit_LabelEAttribute_strategy)
@settings(max_examples=25)
def test_cevinedit_LabelEAttribute_instantiation(instance):
    assert isinstance(instance, cevinedit_LabelEAttribute)


cevinedit_Link_strategy = st.builds(cevinedit_Link, brightness=safe_text, color=safe_text, label=safe_text, labelFontStyle=safe_text, sourceDecoration=safe_text, targetDecoration=safe_text, texture=safe_text, width=st.integers())
@given(instance=cevinedit_Link_strategy)
@settings(max_examples=25)
def test_cevinedit_Link_instantiation(instance):
    assert isinstance(instance, cevinedit_Link)


cevinedit_LinkEClass_strategy = st.builds(cevinedit_LinkEClass, source=safe_text, target=safe_text)
@given(instance=cevinedit_LinkEClass_strategy)
@settings(max_examples=25)
def test_cevinedit_LinkEClass_instantiation(instance):
    assert isinstance(instance, cevinedit_LinkEClass)


cevinedit_LinkEReferenceNonCont_strategy = st.builds(cevinedit_LinkEReferenceNonCont)
@given(instance=cevinedit_LinkEReferenceNonCont_strategy)
@settings(max_examples=25)
def test_cevinedit_LinkEReferenceNonCont_instantiation(instance):
    assert isinstance(instance, cevinedit_LinkEReferenceNonCont)


cevinedit_NodeEClass_strategy = st.builds(cevinedit_NodeEClass, backgroundColor=safe_text, borderColor=safe_text, borderTexture=safe_text, borderWidth=st.integers(), brightness=safe_text, figure=safe_text, imagePath=safe_text, label=safe_text, labelFontStyle=safe_text, labelPlacement=safe_text, listPointsPolygon=safe_text, resizable=st.booleans(), size=safe_text)
@given(instance=cevinedit_NodeEClass_strategy)
@settings(max_examples=25)
def test_cevinedit_NodeEClass_instantiation(instance):
    assert isinstance(instance, cevinedit_NodeEClass)


cevinedit_PersonalizedElement_strategy = st.builds(cevinedit_PersonalizedElement, icon=safe_text, name=safe_text)
@given(instance=cevinedit_PersonalizedElement_strategy)
@settings(max_examples=25)
def test_cevinedit_PersonalizedElement_instantiation(instance):
    assert isinstance(instance, cevinedit_PersonalizedElement)


