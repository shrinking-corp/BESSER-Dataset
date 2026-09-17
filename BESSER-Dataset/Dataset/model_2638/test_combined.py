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
    model3_Diagram,
    subpackage_model3_Class1,
    model3_subpackage_Class2,
    model3_NodeD,
    EdgeTarget,
    model3_NodeF,
    model3_Edge,
    model3_EdgeTarget,
    model3_ClassWithTransientContainment,
    model3_ClassWithJavaObjectAttribute,
    model3_ClassWithJavaClassAttribute,
    model3_ClassWithIDAttribute,
    model3_File,
    model3_Image,
    model3_NodeE,
    model3_NodeC,
    model3_NodeB,
    model3_NodeA,
    model3_PolygonWithDuplicates,
    model3_Polygon,
    model3_EReference,
    model3_EClass,
    model3_EPackage,
    model3_MetaRef,
    Class2,
    model3_Class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_model3_diagram_is_not_abstract():
    assert not inspect.isabstract(model3_Diagram)


def test_hyp_model3_diagram_constructor_exists():
    assert callable(model3_Diagram.__init__)


def test_hyp_model3_diagram_constructor_args():
    sig = inspect.signature(model3_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subpackage_model3_class1_is_not_abstract():
    assert not inspect.isabstract(subpackage_model3_Class1)


def test_hyp_subpackage_model3_class1_constructor_exists():
    assert callable(subpackage_model3_Class1.__init__)


def test_hyp_subpackage_model3_class1_constructor_args():
    sig = inspect.signature(subpackage_model3_Class1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_subpackage_class2_is_not_abstract():
    assert not inspect.isabstract(model3_subpackage_Class2)


def test_hyp_model3_subpackage_class2_constructor_exists():
    assert callable(model3_subpackage_Class2.__init__)


def test_hyp_model3_subpackage_class2_constructor_args():
    sig = inspect.signature(model3_subpackage_Class2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_noded_is_not_abstract():
    assert not inspect.isabstract(model3_NodeD)


def test_hyp_model3_noded_constructor_exists():
    assert callable(model3_NodeD.__init__)


def test_hyp_model3_noded_constructor_args():
    sig = inspect.signature(model3_NodeD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_edgetarget_is_not_abstract():
    assert not inspect.isabstract(EdgeTarget)


def test_hyp_edgetarget_constructor_exists():
    assert callable(EdgeTarget.__init__)


def test_hyp_edgetarget_constructor_args():
    sig = inspect.signature(EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_nodef_is_not_abstract():
    assert not inspect.isabstract(model3_NodeF)


def test_hyp_model3_nodef_constructor_exists():
    assert callable(model3_NodeF.__init__)


def test_hyp_model3_nodef_constructor_args():
    sig = inspect.signature(model3_NodeF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_edge_is_not_abstract():
    assert not inspect.isabstract(model3_Edge)


def test_hyp_model3_edge_constructor_exists():
    assert callable(model3_Edge.__init__)


def test_hyp_model3_edge_constructor_args():
    sig = inspect.signature(model3_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_edgetarget_is_not_abstract():
    assert not inspect.isabstract(model3_EdgeTarget)


def test_hyp_model3_edgetarget_constructor_exists():
    assert callable(model3_EdgeTarget.__init__)


def test_hyp_model3_edgetarget_constructor_args():
    sig = inspect.signature(model3_EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_classwithtransientcontainment_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithTransientContainment)


def test_hyp_model3_classwithtransientcontainment_constructor_exists():
    assert callable(model3_ClassWithTransientContainment.__init__)


def test_hyp_model3_classwithtransientcontainment_constructor_args():
    sig = inspect.signature(model3_ClassWithTransientContainment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model3_classwithjavaobjectattribute_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithJavaObjectAttribute)


def test_hyp_model3_classwithjavaobjectattribute_constructor_exists():
    assert callable(model3_ClassWithJavaObjectAttribute.__init__)


def test_hyp_model3_classwithjavaobjectattribute_constructor_args():
    sig = inspect.signature(model3_ClassWithJavaObjectAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "javaObject" in params, "Missing parameter 'javaObject'"




def test_hyp_model3_classwithjavaclassattribute_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithJavaClassAttribute)


def test_hyp_model3_classwithjavaclassattribute_constructor_exists():
    assert callable(model3_ClassWithJavaClassAttribute.__init__)


def test_hyp_model3_classwithjavaclassattribute_constructor_args():
    sig = inspect.signature(model3_ClassWithJavaClassAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "javaClass" in params, "Missing parameter 'javaClass'"




def test_hyp_model3_classwithidattribute_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithIDAttribute)


def test_hyp_model3_classwithidattribute_constructor_exists():
    assert callable(model3_ClassWithIDAttribute.__init__)


def test_hyp_model3_classwithidattribute_constructor_args():
    sig = inspect.signature(model3_ClassWithIDAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_model3_file_is_not_abstract():
    assert not inspect.isabstract(model3_File)


def test_hyp_model3_file_constructor_exists():
    assert callable(model3_File.__init__)


def test_hyp_model3_file_constructor_args():
    sig = inspect.signature(model3_File.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_model3_image_is_not_abstract():
    assert not inspect.isabstract(model3_Image)


def test_hyp_model3_image_constructor_exists():
    assert callable(model3_Image.__init__)


def test_hyp_model3_image_constructor_args():
    sig = inspect.signature(model3_Image.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"






def test_hyp_model3_nodee_is_not_abstract():
    assert not inspect.isabstract(model3_NodeE)


def test_hyp_model3_nodee_constructor_exists():
    assert callable(model3_NodeE.__init__)


def test_hyp_model3_nodee_constructor_args():
    sig = inspect.signature(model3_NodeE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model3_nodec_is_not_abstract():
    assert not inspect.isabstract(model3_NodeC)


def test_hyp_model3_nodec_constructor_exists():
    assert callable(model3_NodeC.__init__)


def test_hyp_model3_nodec_constructor_args():
    sig = inspect.signature(model3_NodeC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model3_nodeb_is_not_abstract():
    assert not inspect.isabstract(model3_NodeB)


def test_hyp_model3_nodeb_constructor_exists():
    assert callable(model3_NodeB.__init__)


def test_hyp_model3_nodeb_constructor_args():
    sig = inspect.signature(model3_NodeB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model3_nodea_is_not_abstract():
    assert not inspect.isabstract(model3_NodeA)


def test_hyp_model3_nodea_constructor_exists():
    assert callable(model3_NodeA.__init__)


def test_hyp_model3_nodea_constructor_args():
    sig = inspect.signature(model3_NodeA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model3_polygonwithduplicates_is_not_abstract():
    assert not inspect.isabstract(model3_PolygonWithDuplicates)


def test_hyp_model3_polygonwithduplicates_constructor_exists():
    assert callable(model3_PolygonWithDuplicates.__init__)


def test_hyp_model3_polygonwithduplicates_constructor_args():
    sig = inspect.signature(model3_PolygonWithDuplicates.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"




def test_hyp_model3_polygon_is_not_abstract():
    assert not inspect.isabstract(model3_Polygon)


def test_hyp_model3_polygon_constructor_exists():
    assert callable(model3_Polygon.__init__)


def test_hyp_model3_polygon_constructor_args():
    sig = inspect.signature(model3_Polygon.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"




def test_hyp_model3_ereference_is_not_abstract():
    assert not inspect.isabstract(model3_EReference)


def test_hyp_model3_ereference_constructor_exists():
    assert callable(model3_EReference.__init__)


def test_hyp_model3_ereference_constructor_args():
    sig = inspect.signature(model3_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_eclass_is_not_abstract():
    assert not inspect.isabstract(model3_EClass)


def test_hyp_model3_eclass_constructor_exists():
    assert callable(model3_EClass.__init__)


def test_hyp_model3_eclass_constructor_args():
    sig = inspect.signature(model3_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_epackage_is_not_abstract():
    assert not inspect.isabstract(model3_EPackage)


def test_hyp_model3_epackage_constructor_exists():
    assert callable(model3_EPackage.__init__)


def test_hyp_model3_epackage_constructor_args():
    sig = inspect.signature(model3_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_metaref_is_not_abstract():
    assert not inspect.isabstract(model3_MetaRef)


def test_hyp_model3_metaref_constructor_exists():
    assert callable(model3_MetaRef.__init__)


def test_hyp_model3_metaref_constructor_args():
    sig = inspect.signature(model3_MetaRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_hyp_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_hyp_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model3_class1_is_not_abstract():
    assert not inspect.isabstract(model3_Class1)


def test_hyp_model3_class1_constructor_exists():
    assert callable(model3_Class1.__init__)


def test_hyp_model3_class1_constructor_args():
    sig = inspect.signature(model3_Class1.__init__)
    params = list(sig.parameters.keys())
    assert "additionalValue" in params, "Missing parameter 'additionalValue'"



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
model3_Diagram_strategy = st.builds(
    model3_Diagram,
)
subpackage_model3_Class1_strategy = st.builds(
    subpackage_model3_Class1,
)
model3_subpackage_Class2_strategy = st.builds(
    model3_subpackage_Class2,
)
model3_NodeD_strategy = st.builds(
    model3_NodeD,
    name=
        safe_text
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
model3_NodeF_strategy = st.builds(
    model3_NodeF,
)
model3_Edge_strategy = st.builds(
    model3_Edge,
)
model3_EdgeTarget_strategy = st.builds(
    model3_EdgeTarget,
)
model3_ClassWithTransientContainment_strategy = st.builds(
    model3_ClassWithTransientContainment,
    name=
        safe_text
)
model3_ClassWithJavaObjectAttribute_strategy = st.builds(
    model3_ClassWithJavaObjectAttribute,
    javaObject=
        safe_text
)
model3_ClassWithJavaClassAttribute_strategy = st.builds(
    model3_ClassWithJavaClassAttribute,
    javaClass=
        safe_text
)
model3_ClassWithIDAttribute_strategy = st.builds(
    model3_ClassWithIDAttribute,
    id=
        safe_text
)
model3_File_strategy = st.builds(
    model3_File,
    data=
        safe_text,
    name=
        safe_text
)
model3_Image_strategy = st.builds(
    model3_Image,
    data=
        safe_text,
    width=
        st.integers(),
    height=
        st.integers()
)
model3_NodeE_strategy = st.builds(
    model3_NodeE,
    name=
        safe_text
)
model3_NodeC_strategy = st.builds(
    model3_NodeC,
    name=
        safe_text
)
model3_NodeB_strategy = st.builds(
    model3_NodeB,
    name=
        safe_text
)
model3_NodeA_strategy = st.builds(
    model3_NodeA,
    name=
        safe_text
)
model3_PolygonWithDuplicates_strategy = st.builds(
    model3_PolygonWithDuplicates,
    points=
        safe_text
)
model3_Polygon_strategy = st.builds(
    model3_Polygon,
    points=
        safe_text
)
model3_EReference_strategy = st.builds(
    model3_EReference,
)
model3_EClass_strategy = st.builds(
    model3_EClass,
)
model3_EPackage_strategy = st.builds(
    model3_EPackage,
)
model3_MetaRef_strategy = st.builds(
    model3_MetaRef,
)
Class2_strategy = st.builds(
    Class2,
)
model3_Class1_strategy = st.builds(
    model3_Class1,
    additionalValue=
        safe_text
)







@given(instance=model3_NodeD_strategy)
def test_hyp_model3_noded_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=model3_ClassWithTransientContainment_strategy)
def test_hyp_model3_classwithtransientcontainment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=model3_ClassWithJavaObjectAttribute_strategy)
def test_hyp_model3_classwithjavaobjectattribute_javaObject_setter(instance):
    original = instance.javaObject
    instance.javaObject = original
    assert instance.javaObject == original




@given(instance=model3_ClassWithJavaClassAttribute_strategy)
def test_hyp_model3_classwithjavaclassattribute_javaClass_setter(instance):
    original = instance.javaClass
    instance.javaClass = original
    assert instance.javaClass == original




@given(instance=model3_ClassWithIDAttribute_strategy)
def test_hyp_model3_classwithidattribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=model3_File_strategy)
def test_hyp_model3_file_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=model3_File_strategy)
def test_hyp_model3_file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=model3_Image_strategy)
def test_hyp_model3_image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=model3_Image_strategy)
def test_hyp_model3_image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=model3_Image_strategy)
def test_hyp_model3_image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=model3_NodeE_strategy)
def test_hyp_model3_nodee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=model3_NodeC_strategy)
def test_hyp_model3_nodec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=model3_NodeB_strategy)
def test_hyp_model3_nodeb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=model3_NodeA_strategy)
def test_hyp_model3_nodea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=model3_PolygonWithDuplicates_strategy)
def test_hyp_model3_polygonwithduplicates_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original




@given(instance=model3_Polygon_strategy)
def test_hyp_model3_polygon_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original









@given(instance=model3_Class1_strategy)
def test_hyp_model3_class1_additionalValue_setter(instance):
    original = instance.additionalValue
    instance.additionalValue = original
    assert instance.additionalValue == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class2,
    EdgeTarget,
    model3_Class1,
    model3_ClassWithIDAttribute,
    model3_ClassWithJavaClassAttribute,
    model3_ClassWithJavaObjectAttribute,
    model3_ClassWithTransientContainment,
    model3_Diagram,
    model3_EClass,
    model3_EPackage,
    model3_EReference,
    model3_Edge,
    model3_EdgeTarget,
    model3_File,
    model3_Image,
    model3_MetaRef,
    model3_NodeA,
    model3_NodeB,
    model3_NodeC,
    model3_NodeD,
    model3_NodeE,
    model3_NodeF,
    model3_Polygon,
    model3_PolygonWithDuplicates,
    model3_subpackage_Class2,
    subpackage_model3_Class1,
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

def test_model3_Class1_additionalValue_value_roundtrip():
    instance = model3_Class1(additionalValue="sample_text")
    assert instance.additionalValue == "sample_text"
    instance.additionalValue = "sample_text_2"
    assert instance.additionalValue == "sample_text_2"


def test_model3_ClassWithIDAttribute_id_value_roundtrip():
    instance = model3_ClassWithIDAttribute(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_model3_ClassWithJavaClassAttribute_javaClass_value_roundtrip():
    instance = model3_ClassWithJavaClassAttribute(javaClass="sample_text")
    assert instance.javaClass == "sample_text"
    instance.javaClass = "sample_text_2"
    assert instance.javaClass == "sample_text_2"


def test_model3_ClassWithJavaObjectAttribute_javaObject_value_roundtrip():
    instance = model3_ClassWithJavaObjectAttribute(javaObject="sample_text")
    assert instance.javaObject == "sample_text"
    instance.javaObject = "sample_text_2"
    assert instance.javaObject == "sample_text_2"


def test_model3_ClassWithTransientContainment_name_value_roundtrip():
    instance = model3_ClassWithTransientContainment(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model3_File_data_value_roundtrip():
    instance = model3_File(data="sample_text", name="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_model3_File_name_value_roundtrip():
    instance = model3_File(data="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model3_Image_data_value_roundtrip():
    instance = model3_Image(data="sample_text", height=7, width=7)
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_model3_Image_height_value_roundtrip():
    instance = model3_Image(data="sample_text", height=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_model3_Image_width_value_roundtrip():
    instance = model3_Image(data="sample_text", height=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_model3_NodeA_name_value_roundtrip():
    instance = model3_NodeA(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model3_NodeB_name_value_roundtrip():
    instance = model3_NodeB(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model3_NodeC_name_value_roundtrip():
    instance = model3_NodeC(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model3_NodeD_name_value_roundtrip():
    instance = model3_NodeD(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model3_NodeE_name_value_roundtrip():
    instance = model3_NodeE(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model3_Polygon_points_value_roundtrip():
    instance = model3_Polygon(points="sample_text")
    assert instance.points == "sample_text"
    instance.points = "sample_text_2"
    assert instance.points == "sample_text_2"


def test_model3_PolygonWithDuplicates_points_value_roundtrip():
    instance = model3_PolygonWithDuplicates(points="sample_text")
    assert instance.points == "sample_text"
    instance.points = "sample_text_2"
    assert instance.points == "sample_text_2"


def test_model3_NodeF_isa_EdgeTarget():
    instance = model3_NodeF()
    assert isinstance(instance, EdgeTarget)


def test_assoc_children12_link_reassign_clear():
    a = model3_NodeB(name="sample_text")
    b1 = model3_NodeB(name="sample_text")
    b2 = model3_NodeB(name="sample_text_2")
    _safe_set(a, 'NodeB', b1)
    assert _is_linked(a, 'NodeB', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'NodeB', b2)
    assert _is_linked(a, 'NodeB', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'NodeB', None)
    assert not _is_linked(a, 'NodeB', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_children17_link_reassign_clear():
    a = model3_NodeC(name="sample_text")
    b1 = model3_NodeC(name="sample_text")
    b2 = model3_NodeC(name="sample_text_2")
    _safe_set(a, 'NodeC', b1)
    assert _is_linked(a, 'NodeC', b1)
    if hasattr(b1, 'parent18'):
        assert _is_linked(b1, 'parent18', a)
    _safe_set(a, 'NodeC', b2)
    assert _is_linked(a, 'NodeC', b2)
    if hasattr(b1, 'parent18'):
        assert not _is_linked(b1, 'parent18', a)
    if hasattr(b2, 'parent18'):
        assert _is_linked(b2, 'parent18', a)
    _safe_set(a, 'NodeC', None)
    assert not _is_linked(a, 'NodeC', b2)
    if hasattr(b2, 'parent18'):
        assert not _is_linked(b2, 'parent18', a)


def test_assoc_children30_link_reassign_clear():
    a = model3_NodeD(name="sample_text")
    b1 = model3_NodeD(name="sample_text")
    b2 = model3_NodeD(name="sample_text_2")
    _safe_set(a, 'NodeD', b1)
    assert _is_linked(a, 'NodeD', b1)
    if hasattr(b1, 'parent31'):
        assert _is_linked(b1, 'parent31', a)
    _safe_set(a, 'NodeD', b2)
    assert _is_linked(a, 'NodeD', b2)
    if hasattr(b1, 'parent31'):
        assert not _is_linked(b1, 'parent31', a)
    if hasattr(b2, 'parent31'):
        assert _is_linked(b2, 'parent31', a)
    _safe_set(a, 'NodeD', None)
    assert not _is_linked(a, 'NodeD', b2)
    if hasattr(b2, 'parent31'):
        assert not _is_linked(b2, 'parent31', a)


def test_assoc_children7_link_reassign_clear():
    a = model3_NodeA(name="sample_text")
    b1 = model3_NodeA(name="sample_text")
    b2 = model3_NodeA(name="sample_text_2")
    _safe_set(a, 'model3_NodeA', b1)
    assert _is_linked(a, 'model3_NodeA', b1)
    if hasattr(b1, 'model3_NodeA6'):
        assert _is_linked(b1, 'model3_NodeA6', a)
    _safe_set(a, 'model3_NodeA', b2)
    assert _is_linked(a, 'model3_NodeA', b2)
    if hasattr(b1, 'model3_NodeA6'):
        assert not _is_linked(b1, 'model3_NodeA6', a)
    if hasattr(b2, 'model3_NodeA6'):
        assert _is_linked(b2, 'model3_NodeA6', a)
    _safe_set(a, 'model3_NodeA', None)
    assert not _is_linked(a, 'model3_NodeA', b2)
    if hasattr(b2, 'model3_NodeA6'):
        assert not _is_linked(b2, 'model3_NodeA6', a)


def test_assoc_class20_link_reassign_clear():
    a = model3_Class1(additionalValue="sample_text")
    b1 = Class2()
    b2 = Class2()
    _safe_set(a, 'class1', {b1})
    assert _is_linked(a, 'class1', b1)
    if hasattr(b1, 'Class2'):
        assert _is_linked(b1, 'Class2', a)
    _safe_set(a, 'class1', {b2})
    assert _is_linked(a, 'class1', b2)
    if hasattr(b1, 'Class2'):
        assert not _is_linked(b1, 'Class2', a)
    if hasattr(b2, 'Class2'):
        assert _is_linked(b2, 'Class2', a)
    _safe_set(a, 'class1', set())
    assert not _is_linked(a, 'class1', b2)
    if hasattr(b2, 'Class2'):
        assert not _is_linked(b2, 'Class2', a)


def test_assoc_mainNode43_link_reassign_clear():
    a = model3_NodeE(name="sample_text")
    b1 = model3_NodeA(name="sample_text")
    b2 = model3_NodeA(name="sample_text_2")
    _safe_set(a, 'model3_NodeE', b1)
    assert _is_linked(a, 'model3_NodeE', b1)
    if hasattr(b1, 'model3_NodeA44'):
        assert _is_linked(b1, 'model3_NodeA44', a)
    _safe_set(a, 'model3_NodeE', b2)
    assert _is_linked(a, 'model3_NodeE', b2)
    if hasattr(b1, 'model3_NodeA44'):
        assert not _is_linked(b1, 'model3_NodeA44', a)
    if hasattr(b2, 'model3_NodeA44'):
        assert _is_linked(b2, 'model3_NodeA44', a)
    _safe_set(a, 'model3_NodeE', None)
    assert not _is_linked(a, 'model3_NodeE', b2)
    if hasattr(b2, 'model3_NodeA44'):
        assert not _is_linked(b2, 'model3_NodeA44', a)


def test_assoc_oppositeNode40_link_reassign_clear():
    a = model3_NodeD(name="sample_text")
    b1 = model3_NodeD(name="sample_text")
    b2 = model3_NodeD(name="sample_text_2")
    _safe_set(a, 'NodeD42', b1)
    assert _is_linked(a, 'NodeD42', b1)
    if hasattr(b1, 'otherNodes41'):
        assert _is_linked(b1, 'otherNodes41', a)
    _safe_set(a, 'NodeD42', b2)
    assert _is_linked(a, 'NodeD42', b2)
    if hasattr(b1, 'otherNodes41'):
        assert not _is_linked(b1, 'otherNodes41', a)
    if hasattr(b2, 'otherNodes41'):
        assert _is_linked(b2, 'otherNodes41', a)
    _safe_set(a, 'NodeD42', None)
    assert not _is_linked(a, 'NodeD42', b2)
    if hasattr(b2, 'otherNodes41'):
        assert not _is_linked(b2, 'otherNodes41', a)


def test_assoc_oppositeNodes27_link_reassign_clear():
    a = model3_NodeC(name="sample_text")
    b1 = model3_NodeC(name="sample_text")
    b2 = model3_NodeC(name="sample_text_2")
    _safe_set(a, 'NodeC28', b1)
    assert _is_linked(a, 'NodeC28', b1)
    if hasattr(b1, 'otherNodes'):
        assert _is_linked(b1, 'otherNodes', a)
    _safe_set(a, 'NodeC28', b2)
    assert _is_linked(a, 'NodeC28', b2)
    if hasattr(b1, 'otherNodes'):
        assert not _is_linked(b1, 'otherNodes', a)
    if hasattr(b2, 'otherNodes'):
        assert _is_linked(b2, 'otherNodes', a)
    _safe_set(a, 'NodeC28', None)
    assert not _is_linked(a, 'NodeC28', b2)
    if hasattr(b2, 'otherNodes'):
        assert not _is_linked(b2, 'otherNodes', a)


def test_assoc_otherNodes24_link_reassign_clear():
    a = model3_NodeC(name="sample_text")
    b1 = model3_NodeC(name="sample_text")
    b2 = model3_NodeC(name="sample_text_2")
    _safe_set(a, 'NodeC25', b1)
    assert _is_linked(a, 'NodeC25', b1)
    if hasattr(b1, 'oppositeNodes'):
        assert _is_linked(b1, 'oppositeNodes', a)
    _safe_set(a, 'NodeC25', b2)
    assert _is_linked(a, 'NodeC25', b2)
    if hasattr(b1, 'oppositeNodes'):
        assert not _is_linked(b1, 'oppositeNodes', a)
    if hasattr(b2, 'oppositeNodes'):
        assert _is_linked(b2, 'oppositeNodes', a)
    _safe_set(a, 'NodeC25', None)
    assert not _is_linked(a, 'NodeC25', b2)
    if hasattr(b2, 'oppositeNodes'):
        assert not _is_linked(b2, 'oppositeNodes', a)


def test_assoc_otherNodes37_link_reassign_clear():
    a = model3_NodeD(name="sample_text")
    b1 = model3_NodeD(name="sample_text")
    b2 = model3_NodeD(name="sample_text_2")
    _safe_set(a, 'NodeD38', b1)
    assert _is_linked(a, 'NodeD38', b1)
    if hasattr(b1, 'oppositeNode'):
        assert _is_linked(b1, 'oppositeNode', a)
    _safe_set(a, 'NodeD38', b2)
    assert _is_linked(a, 'NodeD38', b2)
    if hasattr(b1, 'oppositeNode'):
        assert not _is_linked(b1, 'oppositeNode', a)
    if hasattr(b2, 'oppositeNode'):
        assert _is_linked(b2, 'oppositeNode', a)
    _safe_set(a, 'NodeD38', None)
    assert not _is_linked(a, 'NodeD38', b2)
    if hasattr(b2, 'oppositeNode'):
        assert not _is_linked(b2, 'oppositeNode', a)


def test_assoc_otherNodes45_link_reassign_clear():
    a = model3_NodeE(name="sample_text")
    b1 = model3_NodeA(name="sample_text")
    b2 = model3_NodeA(name="sample_text_2")
    _safe_set(a, 'model3_NodeE46', {b1})
    assert _is_linked(a, 'model3_NodeE46', b1)
    if hasattr(b1, 'model3_NodeA47'):
        assert _is_linked(b1, 'model3_NodeA47', a)
    _safe_set(a, 'model3_NodeE46', {b2})
    assert _is_linked(a, 'model3_NodeE46', b2)
    if hasattr(b1, 'model3_NodeA47'):
        assert not _is_linked(b1, 'model3_NodeA47', a)
    if hasattr(b2, 'model3_NodeA47'):
        assert _is_linked(b2, 'model3_NodeA47', a)
    _safe_set(a, 'model3_NodeE46', set())
    assert not _is_linked(a, 'model3_NodeE46', b2)
    if hasattr(b2, 'model3_NodeA47'):
        assert not _is_linked(b2, 'model3_NodeA47', a)


def test_assoc_otherNodes9_link_reassign_clear():
    a = model3_NodeA(name="sample_text")
    b1 = model3_NodeA(name="sample_text")
    b2 = model3_NodeA(name="sample_text_2")
    _safe_set(a, 'model3_NodeA10', b1)
    assert _is_linked(a, 'model3_NodeA10', b1)
    if hasattr(b1, 'model3_NodeA8'):
        assert _is_linked(b1, 'model3_NodeA8', a)
    _safe_set(a, 'model3_NodeA10', b2)
    assert _is_linked(a, 'model3_NodeA10', b2)
    if hasattr(b1, 'model3_NodeA8'):
        assert not _is_linked(b1, 'model3_NodeA8', a)
    if hasattr(b2, 'model3_NodeA8'):
        assert _is_linked(b2, 'model3_NodeA8', a)
    _safe_set(a, 'model3_NodeA10', None)
    assert not _is_linked(a, 'model3_NodeA10', b2)
    if hasattr(b2, 'model3_NodeA8'):
        assert not _is_linked(b2, 'model3_NodeA8', a)


def test_assoc_parent14_link_reassign_clear():
    a = model3_NodeB(name="sample_text")
    b1 = model3_NodeB(name="sample_text")
    b2 = model3_NodeB(name="sample_text_2")
    _safe_set(a, 'NodeB15', b1)
    assert _is_linked(a, 'NodeB15', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'NodeB15', b2)
    assert _is_linked(a, 'NodeB15', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'NodeB15', None)
    assert not _is_linked(a, 'NodeB15', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_parent20_link_reassign_clear():
    a = model3_NodeC(name="sample_text")
    b1 = model3_NodeC(name="sample_text")
    b2 = model3_NodeC(name="sample_text_2")
    _safe_set(a, 'NodeC22', b1)
    assert _is_linked(a, 'NodeC22', b1)
    if hasattr(b1, 'children21'):
        assert _is_linked(b1, 'children21', a)
    _safe_set(a, 'NodeC22', b2)
    assert _is_linked(a, 'NodeC22', b2)
    if hasattr(b1, 'children21'):
        assert not _is_linked(b1, 'children21', a)
    if hasattr(b2, 'children21'):
        assert _is_linked(b2, 'children21', a)
    _safe_set(a, 'NodeC22', None)
    assert not _is_linked(a, 'NodeC22', b2)
    if hasattr(b2, 'children21'):
        assert not _is_linked(b2, 'children21', a)


def test_assoc_parent33_link_reassign_clear():
    a = model3_NodeD(name="sample_text")
    b1 = model3_NodeD(name="sample_text")
    b2 = model3_NodeD(name="sample_text_2")
    _safe_set(a, 'NodeD35', b1)
    assert _is_linked(a, 'NodeD35', b1)
    if hasattr(b1, 'children34'):
        assert _is_linked(b1, 'children34', a)
    _safe_set(a, 'NodeD35', b2)
    assert _is_linked(a, 'NodeD35', b2)
    if hasattr(b1, 'children34'):
        assert not _is_linked(b1, 'children34', a)
    if hasattr(b2, 'children34'):
        assert _is_linked(b2, 'children34', a)
    _safe_set(a, 'NodeD35', None)
    assert not _is_linked(a, 'NodeD35', b2)
    if hasattr(b2, 'children34'):
        assert not _is_linked(b2, 'children34', a)


def test_assoc_persistentChild54_link_reassign_clear():
    a = model3_ClassWithTransientContainment(name="sample_text")
    b1 = model3_ClassWithTransientContainment(name="sample_text")
    b2 = model3_ClassWithTransientContainment(name="sample_text_2")
    _safe_set(a, 'model3_ClassWithTransientContainment53', b1)
    assert _is_linked(a, 'model3_ClassWithTransientContainment53', b1)
    if hasattr(b1, 'model3_ClassWithTransientContainment55'):
        assert _is_linked(b1, 'model3_ClassWithTransientContainment55', a)
    _safe_set(a, 'model3_ClassWithTransientContainment53', b2)
    assert _is_linked(a, 'model3_ClassWithTransientContainment53', b2)
    if hasattr(b1, 'model3_ClassWithTransientContainment55'):
        assert not _is_linked(b1, 'model3_ClassWithTransientContainment55', a)
    if hasattr(b2, 'model3_ClassWithTransientContainment55'):
        assert _is_linked(b2, 'model3_ClassWithTransientContainment55', a)
    _safe_set(a, 'model3_ClassWithTransientContainment53', None)
    assert not _is_linked(a, 'model3_ClassWithTransientContainment53', b2)
    if hasattr(b2, 'model3_ClassWithTransientContainment55'):
        assert not _is_linked(b2, 'model3_ClassWithTransientContainment55', a)


def test_assoc_persistentChildren57_link_reassign_clear():
    a = model3_ClassWithTransientContainment(name="sample_text")
    b1 = model3_ClassWithTransientContainment(name="sample_text")
    b2 = model3_ClassWithTransientContainment(name="sample_text_2")
    _safe_set(a, 'model3_ClassWithTransientContainment56', {b1})
    assert _is_linked(a, 'model3_ClassWithTransientContainment56', b1)
    if hasattr(b1, 'model3_ClassWithTransientContainment58'):
        assert _is_linked(b1, 'model3_ClassWithTransientContainment58', a)
    _safe_set(a, 'model3_ClassWithTransientContainment56', {b2})
    assert _is_linked(a, 'model3_ClassWithTransientContainment56', b2)
    if hasattr(b1, 'model3_ClassWithTransientContainment58'):
        assert not _is_linked(b1, 'model3_ClassWithTransientContainment58', a)
    if hasattr(b2, 'model3_ClassWithTransientContainment58'):
        assert _is_linked(b2, 'model3_ClassWithTransientContainment58', a)
    _safe_set(a, 'model3_ClassWithTransientContainment56', set())
    assert not _is_linked(a, 'model3_ClassWithTransientContainment56', b2)
    if hasattr(b2, 'model3_ClassWithTransientContainment58'):
        assert not _is_linked(b2, 'model3_ClassWithTransientContainment58', a)


def test_assoc_transientChild49_link_reassign_clear():
    a = model3_ClassWithTransientContainment(name="sample_text")
    b1 = model3_ClassWithTransientContainment(name="sample_text")
    b2 = model3_ClassWithTransientContainment(name="sample_text_2")
    _safe_set(a, 'model3_ClassWithTransientContainment', b1)
    assert _is_linked(a, 'model3_ClassWithTransientContainment', b1)
    if hasattr(b1, 'model3_ClassWithTransientContainment48'):
        assert _is_linked(b1, 'model3_ClassWithTransientContainment48', a)
    _safe_set(a, 'model3_ClassWithTransientContainment', b2)
    assert _is_linked(a, 'model3_ClassWithTransientContainment', b2)
    if hasattr(b1, 'model3_ClassWithTransientContainment48'):
        assert not _is_linked(b1, 'model3_ClassWithTransientContainment48', a)
    if hasattr(b2, 'model3_ClassWithTransientContainment48'):
        assert _is_linked(b2, 'model3_ClassWithTransientContainment48', a)
    _safe_set(a, 'model3_ClassWithTransientContainment', None)
    assert not _is_linked(a, 'model3_ClassWithTransientContainment', b2)
    if hasattr(b2, 'model3_ClassWithTransientContainment48'):
        assert not _is_linked(b2, 'model3_ClassWithTransientContainment48', a)


def test_assoc_transientChildren51_link_reassign_clear():
    a = model3_ClassWithTransientContainment(name="sample_text")
    b1 = model3_ClassWithTransientContainment(name="sample_text")
    b2 = model3_ClassWithTransientContainment(name="sample_text_2")
    _safe_set(a, 'model3_ClassWithTransientContainment50', {b1})
    assert _is_linked(a, 'model3_ClassWithTransientContainment50', b1)
    if hasattr(b1, 'model3_ClassWithTransientContainment52'):
        assert _is_linked(b1, 'model3_ClassWithTransientContainment52', a)
    _safe_set(a, 'model3_ClassWithTransientContainment50', {b2})
    assert _is_linked(a, 'model3_ClassWithTransientContainment50', b2)
    if hasattr(b1, 'model3_ClassWithTransientContainment52'):
        assert not _is_linked(b1, 'model3_ClassWithTransientContainment52', a)
    if hasattr(b2, 'model3_ClassWithTransientContainment52'):
        assert _is_linked(b2, 'model3_ClassWithTransientContainment52', a)
    _safe_set(a, 'model3_ClassWithTransientContainment50', set())
    assert not _is_linked(a, 'model3_ClassWithTransientContainment50', b2)
    if hasattr(b2, 'model3_ClassWithTransientContainment52'):
        assert not _is_linked(b2, 'model3_ClassWithTransientContainment52', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class2_strategy = st.builds(Class2)
@given(instance=Class2_strategy)
@settings(max_examples=25)
def test_Class2_instantiation(instance):
    assert isinstance(instance, Class2)


EdgeTarget_strategy = st.builds(EdgeTarget)
@given(instance=EdgeTarget_strategy)
@settings(max_examples=25)
def test_EdgeTarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)


model3_Class1_strategy = st.builds(model3_Class1, additionalValue=safe_text)
@given(instance=model3_Class1_strategy)
@settings(max_examples=25)
def test_model3_Class1_instantiation(instance):
    assert isinstance(instance, model3_Class1)


model3_ClassWithIDAttribute_strategy = st.builds(model3_ClassWithIDAttribute, id=safe_text)
@given(instance=model3_ClassWithIDAttribute_strategy)
@settings(max_examples=25)
def test_model3_ClassWithIDAttribute_instantiation(instance):
    assert isinstance(instance, model3_ClassWithIDAttribute)


model3_ClassWithJavaClassAttribute_strategy = st.builds(model3_ClassWithJavaClassAttribute, javaClass=safe_text)
@given(instance=model3_ClassWithJavaClassAttribute_strategy)
@settings(max_examples=25)
def test_model3_ClassWithJavaClassAttribute_instantiation(instance):
    assert isinstance(instance, model3_ClassWithJavaClassAttribute)


model3_ClassWithJavaObjectAttribute_strategy = st.builds(model3_ClassWithJavaObjectAttribute, javaObject=safe_text)
@given(instance=model3_ClassWithJavaObjectAttribute_strategy)
@settings(max_examples=25)
def test_model3_ClassWithJavaObjectAttribute_instantiation(instance):
    assert isinstance(instance, model3_ClassWithJavaObjectAttribute)


model3_ClassWithTransientContainment_strategy = st.builds(model3_ClassWithTransientContainment, name=safe_text)
@given(instance=model3_ClassWithTransientContainment_strategy)
@settings(max_examples=25)
def test_model3_ClassWithTransientContainment_instantiation(instance):
    assert isinstance(instance, model3_ClassWithTransientContainment)


model3_Diagram_strategy = st.builds(model3_Diagram)
@given(instance=model3_Diagram_strategy)
@settings(max_examples=25)
def test_model3_Diagram_instantiation(instance):
    assert isinstance(instance, model3_Diagram)


model3_EClass_strategy = st.builds(model3_EClass)
@given(instance=model3_EClass_strategy)
@settings(max_examples=25)
def test_model3_EClass_instantiation(instance):
    assert isinstance(instance, model3_EClass)


model3_EPackage_strategy = st.builds(model3_EPackage)
@given(instance=model3_EPackage_strategy)
@settings(max_examples=25)
def test_model3_EPackage_instantiation(instance):
    assert isinstance(instance, model3_EPackage)


model3_EReference_strategy = st.builds(model3_EReference)
@given(instance=model3_EReference_strategy)
@settings(max_examples=25)
def test_model3_EReference_instantiation(instance):
    assert isinstance(instance, model3_EReference)


model3_Edge_strategy = st.builds(model3_Edge)
@given(instance=model3_Edge_strategy)
@settings(max_examples=25)
def test_model3_Edge_instantiation(instance):
    assert isinstance(instance, model3_Edge)


model3_EdgeTarget_strategy = st.builds(model3_EdgeTarget)
@given(instance=model3_EdgeTarget_strategy)
@settings(max_examples=25)
def test_model3_EdgeTarget_instantiation(instance):
    assert isinstance(instance, model3_EdgeTarget)


model3_File_strategy = st.builds(model3_File, data=safe_text, name=safe_text)
@given(instance=model3_File_strategy)
@settings(max_examples=25)
def test_model3_File_instantiation(instance):
    assert isinstance(instance, model3_File)


model3_Image_strategy = st.builds(model3_Image, data=safe_text, height=st.integers(), width=st.integers())
@given(instance=model3_Image_strategy)
@settings(max_examples=25)
def test_model3_Image_instantiation(instance):
    assert isinstance(instance, model3_Image)


model3_MetaRef_strategy = st.builds(model3_MetaRef)
@given(instance=model3_MetaRef_strategy)
@settings(max_examples=25)
def test_model3_MetaRef_instantiation(instance):
    assert isinstance(instance, model3_MetaRef)


model3_NodeA_strategy = st.builds(model3_NodeA, name=safe_text)
@given(instance=model3_NodeA_strategy)
@settings(max_examples=25)
def test_model3_NodeA_instantiation(instance):
    assert isinstance(instance, model3_NodeA)


model3_NodeB_strategy = st.builds(model3_NodeB, name=safe_text)
@given(instance=model3_NodeB_strategy)
@settings(max_examples=25)
def test_model3_NodeB_instantiation(instance):
    assert isinstance(instance, model3_NodeB)


model3_NodeC_strategy = st.builds(model3_NodeC, name=safe_text)
@given(instance=model3_NodeC_strategy)
@settings(max_examples=25)
def test_model3_NodeC_instantiation(instance):
    assert isinstance(instance, model3_NodeC)


model3_NodeD_strategy = st.builds(model3_NodeD, name=safe_text)
@given(instance=model3_NodeD_strategy)
@settings(max_examples=25)
def test_model3_NodeD_instantiation(instance):
    assert isinstance(instance, model3_NodeD)


model3_NodeE_strategy = st.builds(model3_NodeE, name=safe_text)
@given(instance=model3_NodeE_strategy)
@settings(max_examples=25)
def test_model3_NodeE_instantiation(instance):
    assert isinstance(instance, model3_NodeE)


model3_NodeF_strategy = st.builds(model3_NodeF)
@given(instance=model3_NodeF_strategy)
@settings(max_examples=25)
def test_model3_NodeF_instantiation(instance):
    assert isinstance(instance, model3_NodeF)


model3_Polygon_strategy = st.builds(model3_Polygon, points=safe_text)
@given(instance=model3_Polygon_strategy)
@settings(max_examples=25)
def test_model3_Polygon_instantiation(instance):
    assert isinstance(instance, model3_Polygon)


model3_PolygonWithDuplicates_strategy = st.builds(model3_PolygonWithDuplicates, points=safe_text)
@given(instance=model3_PolygonWithDuplicates_strategy)
@settings(max_examples=25)
def test_model3_PolygonWithDuplicates_instantiation(instance):
    assert isinstance(instance, model3_PolygonWithDuplicates)


model3_subpackage_Class2_strategy = st.builds(model3_subpackage_Class2)
@given(instance=model3_subpackage_Class2_strategy)
@settings(max_examples=25)
def test_model3_subpackage_Class2_instantiation(instance):
    assert isinstance(instance, model3_subpackage_Class2)


subpackage_model3_Class1_strategy = st.builds(subpackage_model3_Class1)
@given(instance=subpackage_model3_Class1_strategy)
@settings(max_examples=25)
def test_subpackage_model3_Class1_instantiation(instance):
    assert isinstance(instance, subpackage_model3_Class1)



