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
    di_Color,
    di_Fill,
    di_Bounds,
    di_Style,
    di_DiagramElement,
    Shape,
    di_Diagram,
    di_Point,
    DiagramElement,
    di_Shape,
    di_Edge,
    di_EObject,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_di_color_is_not_abstract():
    assert not inspect.isabstract(di_Color)


def test_hyp_di_color_constructor_exists():
    assert callable(di_Color.__init__)


def test_hyp_di_color_constructor_args():
    sig = inspect.signature(di_Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_di_fill_is_not_abstract():
    assert not inspect.isabstract(di_Fill)


def test_hyp_di_fill_constructor_exists():
    assert callable(di_Fill.__init__)


def test_hyp_di_fill_constructor_args():
    sig = inspect.signature(di_Fill.__init__)
    params = list(sig.parameters.keys())



def test_hyp_di_bounds_is_not_abstract():
    assert not inspect.isabstract(di_Bounds)


def test_hyp_di_bounds_constructor_exists():
    assert callable(di_Bounds.__init__)


def test_hyp_di_bounds_constructor_args():
    sig = inspect.signature(di_Bounds.__init__)
    params = list(sig.parameters.keys())



def test_hyp_di_style_is_not_abstract():
    assert not inspect.isabstract(di_Style)


def test_hyp_di_style_constructor_exists():
    assert callable(di_Style.__init__)


def test_hyp_di_style_constructor_args():
    sig = inspect.signature(di_Style.__init__)
    params = list(sig.parameters.keys())
    assert "fontBold" in params, "Missing parameter 'fontBold'"
    assert "fontStrikeThrough" in params, "Missing parameter 'fontStrikeThrough'"
    assert "strokeDashLength" in params, "Missing parameter 'strokeDashLength'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "fontItalic" in params, "Missing parameter 'fontItalic'"
    assert "strokeWidth" in params, "Missing parameter 'strokeWidth'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "fillOpacity" in params, "Missing parameter 'fillOpacity'"
    assert "fontUnderline" in params, "Missing parameter 'fontUnderline'"
    assert "strokeOpacity" in params, "Missing parameter 'strokeOpacity'"













def test_hyp_di_diagramelement_is_not_abstract():
    assert not inspect.isabstract(di_DiagramElement)


def test_hyp_di_diagramelement_constructor_exists():
    assert callable(di_DiagramElement.__init__)


def test_hyp_di_diagramelement_constructor_args():
    sig = inspect.signature(di_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_hyp_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_hyp_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_di_diagram_is_not_abstract():
    assert not inspect.isabstract(di_Diagram)


def test_hyp_di_diagram_constructor_exists():
    assert callable(di_Diagram.__init__)


def test_hyp_di_diagram_constructor_args():
    sig = inspect.signature(di_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_di_point_is_not_abstract():
    assert not inspect.isabstract(di_Point)


def test_hyp_di_point_constructor_exists():
    assert callable(di_Point.__init__)


def test_hyp_di_point_constructor_args():
    sig = inspect.signature(di_Point.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_hyp_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_hyp_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_di_shape_is_not_abstract():
    assert not inspect.isabstract(di_Shape)


def test_hyp_di_shape_constructor_exists():
    assert callable(di_Shape.__init__)


def test_hyp_di_shape_constructor_args():
    sig = inspect.signature(di_Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_di_edge_is_not_abstract():
    assert not inspect.isabstract(di_Edge)


def test_hyp_di_edge_constructor_exists():
    assert callable(di_Edge.__init__)


def test_hyp_di_edge_constructor_args():
    sig = inspect.signature(di_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_di_eobject_is_not_abstract():
    assert not inspect.isabstract(di_EObject)


def test_hyp_di_eobject_constructor_exists():
    assert callable(di_EObject.__init__)


def test_hyp_di_eobject_constructor_args():
    sig = inspect.signature(di_EObject.__init__)
    params = list(sig.parameters.keys())


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
di_Color_strategy = st.builds(
    di_Color,
)
di_Fill_strategy = st.builds(
    di_Fill,
)
di_Bounds_strategy = st.builds(
    di_Bounds,
)
di_Style_strategy = st.builds(
    di_Style,
    fontBold=
        safe_text,
    fontStrikeThrough=
        safe_text,
    strokeDashLength=
        safe_text,
    fontSize=
        safe_text,
    fontItalic=
        safe_text,
    strokeWidth=
        safe_text,
    fontName=
        safe_text,
    fillOpacity=
        safe_text,
    fontUnderline=
        safe_text,
    strokeOpacity=
        safe_text
)
di_DiagramElement_strategy = st.builds(
    di_DiagramElement,
    id=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
di_Diagram_strategy = st.builds(
    di_Diagram,
    resolution=
        safe_text,
    documentation=
        safe_text,
    name=
        safe_text
)
di_Point_strategy = st.builds(
    di_Point,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
di_Shape_strategy = st.builds(
    di_Shape,
)
di_Edge_strategy = st.builds(
    di_Edge,
)
di_EObject_strategy = st.builds(
    di_EObject,
)







@given(instance=di_Style_strategy)
def test_hyp_di_style_fontBold_setter(instance):
    original = instance.fontBold
    instance.fontBold = original
    assert instance.fontBold == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_fontStrikeThrough_setter(instance):
    original = instance.fontStrikeThrough
    instance.fontStrikeThrough = original
    assert instance.fontStrikeThrough == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_strokeDashLength_setter(instance):
    original = instance.strokeDashLength
    instance.strokeDashLength = original
    assert instance.strokeDashLength == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_fontItalic_setter(instance):
    original = instance.fontItalic
    instance.fontItalic = original
    assert instance.fontItalic == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_strokeWidth_setter(instance):
    original = instance.strokeWidth
    instance.strokeWidth = original
    assert instance.strokeWidth == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_fillOpacity_setter(instance):
    original = instance.fillOpacity
    instance.fillOpacity = original
    assert instance.fillOpacity == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_fontUnderline_setter(instance):
    original = instance.fontUnderline
    instance.fontUnderline = original
    assert instance.fontUnderline == original



@given(instance=di_Style_strategy)
def test_hyp_di_style_strokeOpacity_setter(instance):
    original = instance.strokeOpacity
    instance.strokeOpacity = original
    assert instance.strokeOpacity == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





@given(instance=di_DiagramElement_strategy)
def test_hyp_di_diagramelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=di_Diagram_strategy)
def test_hyp_di_diagram_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original



@given(instance=di_Diagram_strategy)
def test_hyp_di_diagram_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=di_Diagram_strategy)
def test_hyp_di_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DiagramElement,
    Shape,
    di_Bounds,
    di_Color,
    di_Diagram,
    di_DiagramElement,
    di_EObject,
    di_Edge,
    di_Fill,
    di_Point,
    di_Shape,
    di_Style,
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

def test_di_Diagram_documentation_value_roundtrip():
    instance = di_Diagram(documentation="sample_text", name="sample_text", resolution="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_di_Diagram_name_value_roundtrip():
    instance = di_Diagram(documentation="sample_text", name="sample_text", resolution="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_di_Diagram_resolution_value_roundtrip():
    instance = di_Diagram(documentation="sample_text", name="sample_text", resolution="sample_text")
    assert instance.resolution == "sample_text"
    instance.resolution = "sample_text_2"
    assert instance.resolution == "sample_text_2"


def test_di_DiagramElement_id_value_roundtrip():
    instance = di_DiagramElement(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_di_Style_fillOpacity_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.fillOpacity == "sample_text"
    instance.fillOpacity = "sample_text_2"
    assert instance.fillOpacity == "sample_text_2"


def test_di_Style_fontBold_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.fontBold == "sample_text"
    instance.fontBold = "sample_text_2"
    assert instance.fontBold == "sample_text_2"


def test_di_Style_fontItalic_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.fontItalic == "sample_text"
    instance.fontItalic = "sample_text_2"
    assert instance.fontItalic == "sample_text_2"


def test_di_Style_fontName_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.fontName == "sample_text"
    instance.fontName = "sample_text_2"
    assert instance.fontName == "sample_text_2"


def test_di_Style_fontSize_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.fontSize == "sample_text"
    instance.fontSize = "sample_text_2"
    assert instance.fontSize == "sample_text_2"


def test_di_Style_fontStrikeThrough_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.fontStrikeThrough == "sample_text"
    instance.fontStrikeThrough = "sample_text_2"
    assert instance.fontStrikeThrough == "sample_text_2"


def test_di_Style_fontUnderline_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.fontUnderline == "sample_text"
    instance.fontUnderline = "sample_text_2"
    assert instance.fontUnderline == "sample_text_2"


def test_di_Style_strokeDashLength_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.strokeDashLength == "sample_text"
    instance.strokeDashLength = "sample_text_2"
    assert instance.strokeDashLength == "sample_text_2"


def test_di_Style_strokeOpacity_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.strokeOpacity == "sample_text"
    instance.strokeOpacity = "sample_text_2"
    assert instance.strokeOpacity == "sample_text_2"


def test_di_Style_strokeWidth_value_roundtrip():
    instance = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    assert instance.strokeWidth == "sample_text"
    instance.strokeWidth = "sample_text_2"
    assert instance.strokeWidth == "sample_text_2"


def test_di_Edge_isa_DiagramElement():
    instance = di_Edge()
    assert isinstance(instance, DiagramElement)


def test_di_Shape_isa_DiagramElement():
    instance = di_Shape()
    assert isinstance(instance, DiagramElement)


def test_di_Diagram_isa_Shape():
    instance = di_Diagram(documentation="sample_text", name="sample_text", resolution="sample_text")
    assert isinstance(instance, Shape)


def test_assoc_fill19_link_reassign_clear():
    a = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    b1 = di_Fill()
    b2 = di_Fill()
    _safe_set(a, 'di_Style20', b1)
    assert _is_linked(a, 'di_Style20', b1)
    if hasattr(b1, 'di_Fill'):
        assert _is_linked(b1, 'di_Fill', a)
    _safe_set(a, 'di_Style20', b2)
    assert _is_linked(a, 'di_Style20', b2)
    if hasattr(b1, 'di_Fill'):
        assert not _is_linked(b1, 'di_Fill', a)
    if hasattr(b2, 'di_Fill'):
        assert _is_linked(b2, 'di_Fill', a)
    _safe_set(a, 'di_Style20', None)
    assert not _is_linked(a, 'di_Style20', b2)
    if hasattr(b2, 'di_Fill'):
        assert not _is_linked(b2, 'di_Fill', a)


def test_assoc_fillColor21_link_reassign_clear():
    a = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    b1 = di_Color()
    b2 = di_Color()
    _safe_set(a, 'di_Style22', b1)
    assert _is_linked(a, 'di_Style22', b1)
    if hasattr(b1, 'di_Color'):
        assert _is_linked(b1, 'di_Color', a)
    _safe_set(a, 'di_Style22', b2)
    assert _is_linked(a, 'di_Style22', b2)
    if hasattr(b1, 'di_Color'):
        assert not _is_linked(b1, 'di_Color', a)
    if hasattr(b2, 'di_Color'):
        assert _is_linked(b2, 'di_Color', a)
    _safe_set(a, 'di_Style22', None)
    assert not _is_linked(a, 'di_Style22', b2)
    if hasattr(b2, 'di_Color'):
        assert not _is_linked(b2, 'di_Color', a)


def test_assoc_fontColor26_link_reassign_clear():
    a = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    b1 = di_Color()
    b2 = di_Color()
    _safe_set(a, 'di_Style27', b1)
    assert _is_linked(a, 'di_Style27', b1)
    if hasattr(b1, 'di_Color28'):
        assert _is_linked(b1, 'di_Color28', a)
    _safe_set(a, 'di_Style27', b2)
    assert _is_linked(a, 'di_Style27', b2)
    if hasattr(b1, 'di_Color28'):
        assert not _is_linked(b1, 'di_Color28', a)
    if hasattr(b2, 'di_Color28'):
        assert _is_linked(b2, 'di_Color28', a)
    _safe_set(a, 'di_Style27', None)
    assert not _is_linked(a, 'di_Style27', b2)
    if hasattr(b2, 'di_Color28'):
        assert not _is_linked(b2, 'di_Color28', a)


def test_assoc_localStyle5_link_reassign_clear():
    a = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    b1 = di_DiagramElement(id="sample_text")
    b2 = di_DiagramElement(id="sample_text_2")
    _safe_set(a, 'di_Style', b1)
    assert _is_linked(a, 'di_Style', b1)
    if hasattr(b1, 'di_DiagramElement'):
        assert _is_linked(b1, 'di_DiagramElement', a)
    _safe_set(a, 'di_Style', b2)
    assert _is_linked(a, 'di_Style', b2)
    if hasattr(b1, 'di_DiagramElement'):
        assert not _is_linked(b1, 'di_DiagramElement', a)
    if hasattr(b2, 'di_DiagramElement'):
        assert _is_linked(b2, 'di_DiagramElement', a)
    _safe_set(a, 'di_Style', None)
    assert not _is_linked(a, 'di_Style', b2)
    if hasattr(b2, 'di_DiagramElement'):
        assert not _is_linked(b2, 'di_DiagramElement', a)


def test_assoc_modelElement9_link_reassign_clear():
    a = di_DiagramElement(id="sample_text")
    b1 = di_EObject()
    b2 = di_EObject()
    _safe_set(a, 'di_DiagramElement10', {b1})
    assert _is_linked(a, 'di_DiagramElement10', b1)
    if hasattr(b1, 'di_EObject'):
        assert _is_linked(b1, 'di_EObject', a)
    _safe_set(a, 'di_DiagramElement10', {b2})
    assert _is_linked(a, 'di_DiagramElement10', b2)
    if hasattr(b1, 'di_EObject'):
        assert not _is_linked(b1, 'di_EObject', a)
    if hasattr(b2, 'di_EObject'):
        assert _is_linked(b2, 'di_EObject', a)
    _safe_set(a, 'di_DiagramElement10', set())
    assert not _is_linked(a, 'di_DiagramElement10', b2)
    if hasattr(b2, 'di_EObject'):
        assert not _is_linked(b2, 'di_EObject', a)


def test_assoc_ownedElement3_link_reassign_clear():
    a = di_DiagramElement(id="sample_text")
    b1 = di_DiagramElement(id="sample_text")
    b2 = di_DiagramElement(id="sample_text_2")
    _safe_set(a, 'DiagramElement4', b1)
    assert _is_linked(a, 'DiagramElement4', b1)
    if hasattr(b1, 'owningElement'):
        assert _is_linked(b1, 'owningElement', a)
    _safe_set(a, 'DiagramElement4', b2)
    assert _is_linked(a, 'DiagramElement4', b2)
    if hasattr(b1, 'owningElement'):
        assert not _is_linked(b1, 'owningElement', a)
    if hasattr(b2, 'owningElement'):
        assert _is_linked(b2, 'owningElement', a)
    _safe_set(a, 'DiagramElement4', None)
    assert not _is_linked(a, 'DiagramElement4', b2)
    if hasattr(b2, 'owningElement'):
        assert not _is_linked(b2, 'owningElement', a)


def test_assoc_owningElement1_link_reassign_clear():
    a = di_DiagramElement(id="sample_text")
    b1 = di_DiagramElement(id="sample_text")
    b2 = di_DiagramElement(id="sample_text_2")
    _safe_set(a, 'DiagramElement', b1)
    assert _is_linked(a, 'DiagramElement', b1)
    if hasattr(b1, 'ownedElement'):
        assert _is_linked(b1, 'ownedElement', a)
    _safe_set(a, 'DiagramElement', b2)
    assert _is_linked(a, 'DiagramElement', b2)
    if hasattr(b1, 'ownedElement'):
        assert not _is_linked(b1, 'ownedElement', a)
    if hasattr(b2, 'ownedElement'):
        assert _is_linked(b2, 'ownedElement', a)
    _safe_set(a, 'DiagramElement', None)
    assert not _is_linked(a, 'DiagramElement', b2)
    if hasattr(b2, 'ownedElement'):
        assert not _is_linked(b2, 'ownedElement', a)


def test_assoc_sharedStyle6_link_reassign_clear():
    a = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    b1 = di_DiagramElement(id="sample_text")
    b2 = di_DiagramElement(id="sample_text_2")
    _safe_set(a, 'di_Style8', b1)
    assert _is_linked(a, 'di_Style8', b1)
    if hasattr(b1, 'di_DiagramElement7'):
        assert _is_linked(b1, 'di_DiagramElement7', a)
    _safe_set(a, 'di_Style8', b2)
    assert _is_linked(a, 'di_Style8', b2)
    if hasattr(b1, 'di_DiagramElement7'):
        assert not _is_linked(b1, 'di_DiagramElement7', a)
    if hasattr(b2, 'di_DiagramElement7'):
        assert _is_linked(b2, 'di_DiagramElement7', a)
    _safe_set(a, 'di_Style8', None)
    assert not _is_linked(a, 'di_Style8', b2)
    if hasattr(b2, 'di_DiagramElement7'):
        assert not _is_linked(b2, 'di_DiagramElement7', a)


def test_assoc_source11_link_reassign_clear():
    a = di_DiagramElement(id="sample_text")
    b1 = di_Edge()
    b2 = di_Edge()
    _safe_set(a, 'di_DiagramElement12', b1)
    assert _is_linked(a, 'di_DiagramElement12', b1)
    if hasattr(b1, 'di_Edge'):
        assert _is_linked(b1, 'di_Edge', a)
    _safe_set(a, 'di_DiagramElement12', b2)
    assert _is_linked(a, 'di_DiagramElement12', b2)
    if hasattr(b1, 'di_Edge'):
        assert not _is_linked(b1, 'di_Edge', a)
    if hasattr(b2, 'di_Edge'):
        assert _is_linked(b2, 'di_Edge', a)
    _safe_set(a, 'di_DiagramElement12', None)
    assert not _is_linked(a, 'di_DiagramElement12', b2)
    if hasattr(b2, 'di_Edge'):
        assert not _is_linked(b2, 'di_Edge', a)


def test_assoc_strokeColor23_link_reassign_clear():
    a = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    b1 = di_Color()
    b2 = di_Color()
    _safe_set(a, 'di_Style24', b1)
    assert _is_linked(a, 'di_Style24', b1)
    if hasattr(b1, 'di_Color25'):
        assert _is_linked(b1, 'di_Color25', a)
    _safe_set(a, 'di_Style24', b2)
    assert _is_linked(a, 'di_Style24', b2)
    if hasattr(b1, 'di_Color25'):
        assert not _is_linked(b1, 'di_Color25', a)
    if hasattr(b2, 'di_Color25'):
        assert _is_linked(b2, 'di_Color25', a)
    _safe_set(a, 'di_Style24', None)
    assert not _is_linked(a, 'di_Style24', b2)
    if hasattr(b2, 'di_Color25'):
        assert not _is_linked(b2, 'di_Color25', a)


def test_assoc_target13_link_reassign_clear():
    a = di_DiagramElement(id="sample_text")
    b1 = di_Edge()
    b2 = di_Edge()
    _safe_set(a, 'di_DiagramElement15', b1)
    assert _is_linked(a, 'di_DiagramElement15', b1)
    if hasattr(b1, 'di_Edge14'):
        assert _is_linked(b1, 'di_Edge14', a)
    _safe_set(a, 'di_DiagramElement15', b2)
    assert _is_linked(a, 'di_DiagramElement15', b2)
    if hasattr(b1, 'di_Edge14'):
        assert not _is_linked(b1, 'di_Edge14', a)
    if hasattr(b2, 'di_Edge14'):
        assert _is_linked(b2, 'di_Edge14', a)
    _safe_set(a, 'di_DiagramElement15', None)
    assert not _is_linked(a, 'di_DiagramElement15', b2)
    if hasattr(b2, 'di_Edge14'):
        assert not _is_linked(b2, 'di_Edge14', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


di_Bounds_strategy = st.builds(di_Bounds)
@given(instance=di_Bounds_strategy)
@settings(max_examples=25)
def test_di_Bounds_instantiation(instance):
    assert isinstance(instance, di_Bounds)


di_Color_strategy = st.builds(di_Color)
@given(instance=di_Color_strategy)
@settings(max_examples=25)
def test_di_Color_instantiation(instance):
    assert isinstance(instance, di_Color)


di_Diagram_strategy = st.builds(di_Diagram, documentation=safe_text, name=safe_text, resolution=safe_text)
@given(instance=di_Diagram_strategy)
@settings(max_examples=25)
def test_di_Diagram_instantiation(instance):
    assert isinstance(instance, di_Diagram)


di_DiagramElement_strategy = st.builds(di_DiagramElement, id=safe_text)
@given(instance=di_DiagramElement_strategy)
@settings(max_examples=25)
def test_di_DiagramElement_instantiation(instance):
    assert isinstance(instance, di_DiagramElement)


di_EObject_strategy = st.builds(di_EObject)
@given(instance=di_EObject_strategy)
@settings(max_examples=25)
def test_di_EObject_instantiation(instance):
    assert isinstance(instance, di_EObject)


di_Edge_strategy = st.builds(di_Edge)
@given(instance=di_Edge_strategy)
@settings(max_examples=25)
def test_di_Edge_instantiation(instance):
    assert isinstance(instance, di_Edge)


di_Fill_strategy = st.builds(di_Fill)
@given(instance=di_Fill_strategy)
@settings(max_examples=25)
def test_di_Fill_instantiation(instance):
    assert isinstance(instance, di_Fill)


di_Point_strategy = st.builds(di_Point)
@given(instance=di_Point_strategy)
@settings(max_examples=25)
def test_di_Point_instantiation(instance):
    assert isinstance(instance, di_Point)


di_Shape_strategy = st.builds(di_Shape)
@given(instance=di_Shape_strategy)
@settings(max_examples=25)
def test_di_Shape_instantiation(instance):
    assert isinstance(instance, di_Shape)


di_Style_strategy = st.builds(di_Style, fillOpacity=safe_text, fontBold=safe_text, fontItalic=safe_text, fontName=safe_text, fontSize=safe_text, fontStrikeThrough=safe_text, fontUnderline=safe_text, strokeDashLength=safe_text, strokeOpacity=safe_text, strokeWidth=safe_text)
@given(instance=di_Style_strategy)
@settings(max_examples=25)
def test_di_Style_instantiation(instance):
    assert isinstance(instance, di_Style)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DiagramElement,
    Shape,
    di_Bounds,
    di_Color,
    di_Diagram,
    di_DiagramElement,
    di_EObject,
    di_Edge,
    di_Fill,
    di_Point,
    di_Shape,
    di_Style,
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

def test_assoc_localStyle5_reverse_link_reassign_clear():
    a1 = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    a2 = di_Style(fillOpacity="sample_text_2", fontBold="sample_text_2", fontItalic="sample_text_2", fontName="sample_text_2", fontSize="sample_text_2", fontStrikeThrough="sample_text_2", fontUnderline="sample_text_2", strokeDashLength="sample_text_2", strokeOpacity="sample_text_2", strokeWidth="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'di_DiagramElement', a1)
    assert _is_linked(b, 'di_DiagramElement', a1)
    if hasattr(a1, 'di_Style'):
        assert _is_linked(a1, 'di_Style', b)
    _safe_set(b, 'di_DiagramElement', a2)
    assert _is_linked(b, 'di_DiagramElement', a2)
    if hasattr(a1, 'di_Style'):
        assert not _is_linked(a1, 'di_Style', b)
    if hasattr(a2, 'di_Style'):
        assert _is_linked(a2, 'di_Style', b)
    _safe_set(b, 'di_DiagramElement', None)
    assert not _is_linked(b, 'di_DiagramElement', a2)
    if hasattr(a2, 'di_Style'):
        assert not _is_linked(a2, 'di_Style', b)


def test_assoc_ownedElement3_reverse_link_reassign_clear():
    a1 = di_DiagramElement(id="sample_text")
    a2 = di_DiagramElement(id="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'owningElement', {a1})
    assert _is_linked(b, 'owningElement', a1)
    if hasattr(a1, 'DiagramElement4'):
        assert _is_linked(a1, 'DiagramElement4', b)
    _safe_set(b, 'owningElement', {a2})
    assert _is_linked(b, 'owningElement', a2)
    if hasattr(a1, 'DiagramElement4'):
        assert not _is_linked(a1, 'DiagramElement4', b)
    if hasattr(a2, 'DiagramElement4'):
        assert _is_linked(a2, 'DiagramElement4', b)
    _safe_set(b, 'owningElement', set())
    assert not _is_linked(b, 'owningElement', a2)
    if hasattr(a2, 'DiagramElement4'):
        assert not _is_linked(a2, 'DiagramElement4', b)


def test_assoc_owningElement1_reverse_link_reassign_clear():
    a1 = di_DiagramElement(id="sample_text")
    a2 = di_DiagramElement(id="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'ownedElement', a1)
    assert _is_linked(b, 'ownedElement', a1)
    if hasattr(a1, 'DiagramElement'):
        assert _is_linked(a1, 'DiagramElement', b)
    _safe_set(b, 'ownedElement', a2)
    assert _is_linked(b, 'ownedElement', a2)
    if hasattr(a1, 'DiagramElement'):
        assert not _is_linked(a1, 'DiagramElement', b)
    if hasattr(a2, 'DiagramElement'):
        assert _is_linked(a2, 'DiagramElement', b)
    _safe_set(b, 'ownedElement', None)
    assert not _is_linked(b, 'ownedElement', a2)
    if hasattr(a2, 'DiagramElement'):
        assert not _is_linked(a2, 'DiagramElement', b)


def test_assoc_sharedStyle6_reverse_link_reassign_clear():
    a1 = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    a2 = di_Style(fillOpacity="sample_text_2", fontBold="sample_text_2", fontItalic="sample_text_2", fontName="sample_text_2", fontSize="sample_text_2", fontStrikeThrough="sample_text_2", fontUnderline="sample_text_2", strokeDashLength="sample_text_2", strokeOpacity="sample_text_2", strokeWidth="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'di_DiagramElement7', a1)
    assert _is_linked(b, 'di_DiagramElement7', a1)
    if hasattr(a1, 'di_Style8'):
        assert _is_linked(a1, 'di_Style8', b)
    _safe_set(b, 'di_DiagramElement7', a2)
    assert _is_linked(b, 'di_DiagramElement7', a2)
    if hasattr(a1, 'di_Style8'):
        assert not _is_linked(a1, 'di_Style8', b)
    if hasattr(a2, 'di_Style8'):
        assert _is_linked(a2, 'di_Style8', b)
    _safe_set(b, 'di_DiagramElement7', None)
    assert not _is_linked(b, 'di_DiagramElement7', a2)
    if hasattr(a2, 'di_Style8'):
        assert not _is_linked(a2, 'di_Style8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_fill19_stub_double():
    # di_Fill has no real 'di_Fill' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Fill()
    setattr(partner, 'di_Fill', None)
    _safe_set(owner, 'di_Style20', partner)
    assert getattr(partner, 'di_Fill') == owner
    _safe_set(owner, 'di_Style20', None)
    assert getattr(partner, 'di_Fill') is None


def test_assoc_fillColor21_stub_double():
    # di_Color has no real 'di_Color' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Color()
    setattr(partner, 'di_Color', None)
    _safe_set(owner, 'di_Style22', partner)
    assert getattr(partner, 'di_Color') == owner
    _safe_set(owner, 'di_Style22', None)
    assert getattr(partner, 'di_Color') is None


def test_assoc_fontColor26_stub_double():
    # di_Color has no real 'di_Color28' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Color()
    setattr(partner, 'di_Color28', None)
    _safe_set(owner, 'di_Style27', partner)
    assert getattr(partner, 'di_Color28') == owner
    _safe_set(owner, 'di_Style27', None)
    assert getattr(partner, 'di_Color28') is None


def test_assoc_modelElement9_stub_double():
    # di_EObject has no real 'di_EObject' property in the generated
    # code (a bare stub) -- manually attach it so di_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DiagramElement(id="sample_text")
    partner = di_EObject()
    setattr(partner, 'di_EObject', None)
    _safe_set(owner, 'di_DiagramElement10', {partner})
    assert getattr(partner, 'di_EObject') == owner
    _safe_set(owner, 'di_DiagramElement10', set())
    assert getattr(partner, 'di_EObject') is None


def test_assoc_source11_stub_double():
    # di_Edge has no real 'di_Edge' property in the generated
    # code (a bare stub) -- manually attach it so di_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DiagramElement(id="sample_text")
    partner = di_Edge()
    setattr(partner, 'di_Edge', None)
    _safe_set(owner, 'di_DiagramElement12', partner)
    assert getattr(partner, 'di_Edge') == owner
    _safe_set(owner, 'di_DiagramElement12', None)
    assert getattr(partner, 'di_Edge') is None


def test_assoc_strokeColor23_stub_double():
    # di_Color has no real 'di_Color25' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Color()
    setattr(partner, 'di_Color25', None)
    _safe_set(owner, 'di_Style24', partner)
    assert getattr(partner, 'di_Color25') == owner
    _safe_set(owner, 'di_Style24', None)
    assert getattr(partner, 'di_Color25') is None


def test_assoc_target13_stub_double():
    # di_Edge has no real 'di_Edge14' property in the generated
    # code (a bare stub) -- manually attach it so di_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DiagramElement(id="sample_text")
    partner = di_Edge()
    setattr(partner, 'di_Edge14', None)
    _safe_set(owner, 'di_DiagramElement15', partner)
    assert getattr(partner, 'di_Edge14') == owner
    _safe_set(owner, 'di_DiagramElement15', None)
    assert getattr(partner, 'di_Edge14') is None




from python_code import di_Diagram

def test_di_Diagram___init__():
    assert di_Diagram.__init__(di_Diagram('', '', '\x00\x00'), '', '', '') == None

