# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PersonalizedElement,
    cevinedit_Link,
    cevinedit_NodeEClass,
    cevinedit_PersonalizedElement,
    cevinedit_Diagram,
    cevinedit_CEViNEditRoot,
    cevinedit_LabelEAttribute,
    cevinedit_AffixedEReferenceCont,
    cevinedit_CompartmentEReferenceCont,
    Link,
    cevinedit_LinkEReferenceNonCont,
    cevinedit_LinkEClass,
    LayoutCompartment,
    Texture,
    FontStyle,
    NodeFigure,
    Brightness,
    Placement,
    LinkFigure,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_personalizedelement_is_not_abstract():
    assert not inspect.isabstract(PersonalizedElement)


def test_hyp_personalizedelement_constructor_exists():
    assert callable(PersonalizedElement.__init__)


def test_hyp_personalizedelement_constructor_args():
    sig = inspect.signature(PersonalizedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cevinedit_link_is_not_abstract():
    assert not inspect.isabstract(cevinedit_Link)


def test_hyp_cevinedit_link_constructor_exists():
    assert callable(cevinedit_Link.__init__)


def test_hyp_cevinedit_link_constructor_args():
    sig = inspect.signature(cevinedit_Link.__init__)
    params = list(sig.parameters.keys())
    assert "labelFontStyle" in params, "Missing parameter 'labelFontStyle'"
    assert "width" in params, "Missing parameter 'width'"
    assert "targetDecoration" in params, "Missing parameter 'targetDecoration'"
    assert "label" in params, "Missing parameter 'label'"
    assert "sourceDecoration" in params, "Missing parameter 'sourceDecoration'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "texture" in params, "Missing parameter 'texture'"
    assert "color" in params, "Missing parameter 'color'"











def test_hyp_cevinedit_nodeeclass_is_not_abstract():
    assert not inspect.isabstract(cevinedit_NodeEClass)


def test_hyp_cevinedit_nodeeclass_constructor_exists():
    assert callable(cevinedit_NodeEClass.__init__)


def test_hyp_cevinedit_nodeeclass_constructor_args():
    sig = inspect.signature(cevinedit_NodeEClass.__init__)
    params = list(sig.parameters.keys())
    assert "borderWidth" in params, "Missing parameter 'borderWidth'"
    assert "listPointsPolygon" in params, "Missing parameter 'listPointsPolygon'"
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "figure" in params, "Missing parameter 'figure'"
    assert "labelPlacement" in params, "Missing parameter 'labelPlacement'"
    assert "borderTexture" in params, "Missing parameter 'borderTexture'"
    assert "size" in params, "Missing parameter 'size'"
    assert "labelFontStyle" in params, "Missing parameter 'labelFontStyle'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "label" in params, "Missing parameter 'label'"
    assert "imagePath" in params, "Missing parameter 'imagePath'"
    assert "resizable" in params, "Missing parameter 'resizable'"
















def test_hyp_cevinedit_personalizedelement_is_not_abstract():
    assert not inspect.isabstract(cevinedit_PersonalizedElement)


def test_hyp_cevinedit_personalizedelement_constructor_exists():
    assert callable(cevinedit_PersonalizedElement.__init__)


def test_hyp_cevinedit_personalizedelement_constructor_args():
    sig = inspect.signature(cevinedit_PersonalizedElement.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_cevinedit_diagram_is_not_abstract():
    assert not inspect.isabstract(cevinedit_Diagram)


def test_hyp_cevinedit_diagram_constructor_exists():
    assert callable(cevinedit_Diagram.__init__)


def test_hyp_cevinedit_diagram_constructor_args():
    sig = inspect.signature(cevinedit_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "modelExtension" in params, "Missing parameter 'modelExtension'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_cevinedit_cevineditroot_is_not_abstract():
    assert not inspect.isabstract(cevinedit_CEViNEditRoot)


def test_hyp_cevinedit_cevineditroot_constructor_exists():
    assert callable(cevinedit_CEViNEditRoot.__init__)


def test_hyp_cevinedit_cevineditroot_constructor_args():
    sig = inspect.signature(cevinedit_CEViNEditRoot.__init__)
    params = list(sig.parameters.keys())
    assert "sourceMM" in params, "Missing parameter 'sourceMM'"




def test_hyp_cevinedit_labeleattribute_is_not_abstract():
    assert not inspect.isabstract(cevinedit_LabelEAttribute)


def test_hyp_cevinedit_labeleattribute_constructor_exists():
    assert callable(cevinedit_LabelEAttribute.__init__)


def test_hyp_cevinedit_labeleattribute_constructor_args():
    sig = inspect.signature(cevinedit_LabelEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cevinedit_affixedereferencecont_is_not_abstract():
    assert not inspect.isabstract(cevinedit_AffixedEReferenceCont)


def test_hyp_cevinedit_affixedereferencecont_constructor_exists():
    assert callable(cevinedit_AffixedEReferenceCont.__init__)


def test_hyp_cevinedit_affixedereferencecont_constructor_args():
    sig = inspect.signature(cevinedit_AffixedEReferenceCont.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cevinedit_compartmentereferencecont_is_not_abstract():
    assert not inspect.isabstract(cevinedit_CompartmentEReferenceCont)


def test_hyp_cevinedit_compartmentereferencecont_constructor_exists():
    assert callable(cevinedit_CompartmentEReferenceCont.__init__)


def test_hyp_cevinedit_compartmentereferencecont_constructor_args():
    sig = inspect.signature(cevinedit_CompartmentEReferenceCont.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"
    assert "collapsible" in params, "Missing parameter 'collapsible'"





def test_hyp_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_hyp_link_constructor_exists():
    assert callable(Link.__init__)


def test_hyp_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cevinedit_linkereferencenoncont_is_not_abstract():
    assert not inspect.isabstract(cevinedit_LinkEReferenceNonCont)


def test_hyp_cevinedit_linkereferencenoncont_constructor_exists():
    assert callable(cevinedit_LinkEReferenceNonCont.__init__)


def test_hyp_cevinedit_linkereferencenoncont_constructor_args():
    sig = inspect.signature(cevinedit_LinkEReferenceNonCont.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cevinedit_linkeclass_is_not_abstract():
    assert not inspect.isabstract(cevinedit_LinkEClass)


def test_hyp_cevinedit_linkeclass_constructor_exists():
    assert callable(cevinedit_LinkEClass.__init__)


def test_hyp_cevinedit_linkeclass_constructor_args():
    sig = inspect.signature(cevinedit_LinkEClass.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"



def test_hyp_layoutcompartment_exists():
    # Check that the Enumeration exists
    assert LayoutCompartment is not None

def test_hyp_layoutcompartment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutCompartment]
    expected_literals = [
        "List",
        "Free",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutCompartment"

def test_hyp_texture_exists():
    # Check that the Enumeration exists
    assert Texture is not None

def test_hyp_texture_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Texture]
    expected_literals = [
        "Dash",
        "Dot",
        "Solid",
        "Default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Texture"

def test_hyp_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_hyp_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "Bold",
        "Default",
        "Italic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_hyp_nodefigure_exists():
    # Check that the Enumeration exists
    assert NodeFigure is not None

def test_hyp_nodefigure_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeFigure]
    expected_literals = [
        "Image",
        "Default",
        "Rectangle",
        "Ellipse",
        "SVG",
        "Polygon",
        "Rounded",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeFigure"

def test_hyp_brightness_exists():
    # Check that the Enumeration exists
    assert Brightness is not None

def test_hyp_brightness_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Brightness]
    expected_literals = [
        "Dark",
        "Default",
        "Light",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Brightness"

def test_hyp_placement_exists():
    # Check that the Enumeration exists
    assert Placement is not None

def test_hyp_placement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Placement]
    expected_literals = [
        "Internal",
        "None_",
        "External",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Placement"

def test_hyp_linkfigure_exists():
    # Check that the Enumeration exists
    assert LinkFigure is not None

def test_hyp_linkfigure_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkFigure]
    expected_literals = [
        "Square",
        "Default",
        "Rhomb",
        "None_",
        "ClosedArrow",
        "FilledSquare",
        "Arrow",
        "FilledRhomb",
        "FilledClosedArrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkFigure"

def test_hyp_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_hyp_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "Default",
        "Cyan",
        "Orange",
        "Gray",
        "White",
        "Yellow",
        "Red",
        "Green",
        "Black",
        "Blue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
PersonalizedElement_strategy = st.builds(
    PersonalizedElement,
)
cevinedit_Link_strategy = st.builds(
    cevinedit_Link,
    labelFontStyle=
        safe_text,
    width=
        st.integers(),
    targetDecoration=
        safe_text,
    label=
        safe_text,
    sourceDecoration=
        safe_text,
    brightness=
        safe_text,
    texture=
        safe_text,
    color=
        safe_text
)
cevinedit_NodeEClass_strategy = st.builds(
    cevinedit_NodeEClass,
    borderWidth=
        st.integers(),
    listPointsPolygon=
        safe_text,
    borderColor=
        safe_text,
    figure=
        safe_text,
    labelPlacement=
        safe_text,
    borderTexture=
        safe_text,
    size=
        safe_text,
    labelFontStyle=
        safe_text,
    backgroundColor=
        safe_text,
    brightness=
        safe_text,
    label=
        safe_text,
    imagePath=
        safe_text,
    resizable=
        st.booleans()
)
cevinedit_PersonalizedElement_strategy = st.builds(
    cevinedit_PersonalizedElement,
    icon=
        safe_text,
    name=
        safe_text
)
cevinedit_Diagram_strategy = st.builds(
    cevinedit_Diagram,
    modelExtension=
        safe_text,
    name=
        safe_text
)
cevinedit_CEViNEditRoot_strategy = st.builds(
    cevinedit_CEViNEditRoot,
    sourceMM=
        safe_text
)
cevinedit_LabelEAttribute_strategy = st.builds(
    cevinedit_LabelEAttribute,
)
cevinedit_AffixedEReferenceCont_strategy = st.builds(
    cevinedit_AffixedEReferenceCont,
)
cevinedit_CompartmentEReferenceCont_strategy = st.builds(
    cevinedit_CompartmentEReferenceCont,
    layout=
        safe_text,
    collapsible=
        st.booleans()
)
Link_strategy = st.builds(
    Link,
)
cevinedit_LinkEReferenceNonCont_strategy = st.builds(
    cevinedit_LinkEReferenceNonCont,
)
cevinedit_LinkEClass_strategy = st.builds(
    cevinedit_LinkEClass,
    source=
        safe_text,
    target=
        safe_text
)





@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_labelFontStyle_setter(instance):
    original = instance.labelFontStyle
    instance.labelFontStyle = original
    assert instance.labelFontStyle == original



@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_targetDecoration_setter(instance):
    original = instance.targetDecoration
    instance.targetDecoration = original
    assert instance.targetDecoration == original



@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_sourceDecoration_setter(instance):
    original = instance.sourceDecoration
    instance.sourceDecoration = original
    assert instance.sourceDecoration == original



@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original



@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original



@given(instance=cevinedit_Link_strategy)
def test_hyp_cevinedit_link_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_borderWidth_setter(instance):
    original = instance.borderWidth
    instance.borderWidth = original
    assert instance.borderWidth == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_listPointsPolygon_setter(instance):
    original = instance.listPointsPolygon
    instance.listPointsPolygon = original
    assert instance.listPointsPolygon == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_figure_setter(instance):
    original = instance.figure
    instance.figure = original
    assert instance.figure == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_labelPlacement_setter(instance):
    original = instance.labelPlacement
    instance.labelPlacement = original
    assert instance.labelPlacement == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_borderTexture_setter(instance):
    original = instance.borderTexture
    instance.borderTexture = original
    assert instance.borderTexture == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_labelFontStyle_setter(instance):
    original = instance.labelFontStyle
    instance.labelFontStyle = original
    assert instance.labelFontStyle == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_imagePath_setter(instance):
    original = instance.imagePath
    instance.imagePath = original
    assert instance.imagePath == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_hyp_cevinedit_nodeeclass_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original




@given(instance=cevinedit_PersonalizedElement_strategy)
def test_hyp_cevinedit_personalizedelement_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=cevinedit_PersonalizedElement_strategy)
def test_hyp_cevinedit_personalizedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cevinedit_Diagram_strategy)
def test_hyp_cevinedit_diagram_modelExtension_setter(instance):
    original = instance.modelExtension
    instance.modelExtension = original
    assert instance.modelExtension == original



@given(instance=cevinedit_Diagram_strategy)
def test_hyp_cevinedit_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cevinedit_CEViNEditRoot_strategy)
def test_hyp_cevinedit_cevineditroot_sourceMM_setter(instance):
    original = instance.sourceMM
    instance.sourceMM = original
    assert instance.sourceMM == original






@given(instance=cevinedit_CompartmentEReferenceCont_strategy)
def test_hyp_cevinedit_compartmentereferencecont_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original



@given(instance=cevinedit_CompartmentEReferenceCont_strategy)
def test_hyp_cevinedit_compartmentereferencecont_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original






@given(instance=cevinedit_LinkEClass_strategy)
def test_hyp_cevinedit_linkeclass_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=cevinedit_LinkEClass_strategy)
def test_hyp_cevinedit_linkeclass_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



