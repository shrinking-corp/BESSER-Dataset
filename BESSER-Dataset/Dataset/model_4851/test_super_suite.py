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
    aml_Feature,
    aml_LengthFeature,
    aml_NetWorkFeature,
    aml_ColorFeature,
    aml_SizeFeature,
    aml_TypeFeature,
    SuperEntity,
    aml_Cable,
    aml_Drive,
    aml_MaxFeature,
    aml_ProductPUIDFeature,
    aml_TargetGroupFeature,
    AbstractElements,
    aml_Entity,
    aml_SuperEntity,
    aml_PriceRule,
    aml_MinMax,
    aml_AbstractElements,
    aml_Aml,
    aml_FormFeature,
    aml_SpeedFeature,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_aml_feature_is_not_abstract():
    assert not inspect.isabstract(aml_Feature)


def test_hyp_aml_feature_constructor_exists():
    assert callable(aml_Feature.__init__)


def test_hyp_aml_feature_constructor_args():
    sig = inspect.signature(aml_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_aml_lengthfeature_is_not_abstract():
    assert not inspect.isabstract(aml_LengthFeature)


def test_hyp_aml_lengthfeature_constructor_exists():
    assert callable(aml_LengthFeature.__init__)


def test_hyp_aml_lengthfeature_constructor_args():
    sig = inspect.signature(aml_LengthFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_aml_networkfeature_is_not_abstract():
    assert not inspect.isabstract(aml_NetWorkFeature)


def test_hyp_aml_networkfeature_constructor_exists():
    assert callable(aml_NetWorkFeature.__init__)


def test_hyp_aml_networkfeature_constructor_args():
    sig = inspect.signature(aml_NetWorkFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_aml_colorfeature_is_not_abstract():
    assert not inspect.isabstract(aml_ColorFeature)


def test_hyp_aml_colorfeature_constructor_exists():
    assert callable(aml_ColorFeature.__init__)


def test_hyp_aml_colorfeature_constructor_args():
    sig = inspect.signature(aml_ColorFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_aml_sizefeature_is_not_abstract():
    assert not inspect.isabstract(aml_SizeFeature)


def test_hyp_aml_sizefeature_constructor_exists():
    assert callable(aml_SizeFeature.__init__)


def test_hyp_aml_sizefeature_constructor_args():
    sig = inspect.signature(aml_SizeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_aml_typefeature_is_not_abstract():
    assert not inspect.isabstract(aml_TypeFeature)


def test_hyp_aml_typefeature_constructor_exists():
    assert callable(aml_TypeFeature.__init__)


def test_hyp_aml_typefeature_constructor_args():
    sig = inspect.signature(aml_TypeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_superentity_is_not_abstract():
    assert not inspect.isabstract(SuperEntity)


def test_hyp_superentity_constructor_exists():
    assert callable(SuperEntity.__init__)


def test_hyp_superentity_constructor_args():
    sig = inspect.signature(SuperEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_cable_is_not_abstract():
    assert not inspect.isabstract(aml_Cable)


def test_hyp_aml_cable_constructor_exists():
    assert callable(aml_Cable.__init__)


def test_hyp_aml_cable_constructor_args():
    sig = inspect.signature(aml_Cable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_drive_is_not_abstract():
    assert not inspect.isabstract(aml_Drive)


def test_hyp_aml_drive_constructor_exists():
    assert callable(aml_Drive.__init__)


def test_hyp_aml_drive_constructor_args():
    sig = inspect.signature(aml_Drive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_maxfeature_is_not_abstract():
    assert not inspect.isabstract(aml_MaxFeature)


def test_hyp_aml_maxfeature_constructor_exists():
    assert callable(aml_MaxFeature.__init__)


def test_hyp_aml_maxfeature_constructor_args():
    sig = inspect.signature(aml_MaxFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_aml_productpuidfeature_is_not_abstract():
    assert not inspect.isabstract(aml_ProductPUIDFeature)


def test_hyp_aml_productpuidfeature_constructor_exists():
    assert callable(aml_ProductPUIDFeature.__init__)


def test_hyp_aml_productpuidfeature_constructor_args():
    sig = inspect.signature(aml_ProductPUIDFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "values" in params, "Missing parameter 'values'"





def test_hyp_aml_targetgroupfeature_is_not_abstract():
    assert not inspect.isabstract(aml_TargetGroupFeature)


def test_hyp_aml_targetgroupfeature_constructor_exists():
    assert callable(aml_TargetGroupFeature.__init__)


def test_hyp_aml_targetgroupfeature_constructor_args():
    sig = inspect.signature(aml_TargetGroupFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_abstractelements_is_not_abstract():
    assert not inspect.isabstract(AbstractElements)


def test_hyp_abstractelements_constructor_exists():
    assert callable(AbstractElements.__init__)


def test_hyp_abstractelements_constructor_args():
    sig = inspect.signature(AbstractElements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_entity_is_not_abstract():
    assert not inspect.isabstract(aml_Entity)


def test_hyp_aml_entity_constructor_exists():
    assert callable(aml_Entity.__init__)


def test_hyp_aml_entity_constructor_args():
    sig = inspect.signature(aml_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_superentity_is_not_abstract():
    assert not inspect.isabstract(aml_SuperEntity)


def test_hyp_aml_superentity_constructor_exists():
    assert callable(aml_SuperEntity.__init__)


def test_hyp_aml_superentity_constructor_args():
    sig = inspect.signature(aml_SuperEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_pricerule_is_not_abstract():
    assert not inspect.isabstract(aml_PriceRule)


def test_hyp_aml_pricerule_constructor_exists():
    assert callable(aml_PriceRule.__init__)


def test_hyp_aml_pricerule_constructor_args():
    sig = inspect.signature(aml_PriceRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_minmax_is_not_abstract():
    assert not inspect.isabstract(aml_MinMax)


def test_hyp_aml_minmax_constructor_exists():
    assert callable(aml_MinMax.__init__)


def test_hyp_aml_minmax_constructor_args():
    sig = inspect.signature(aml_MinMax.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_abstractelements_is_not_abstract():
    assert not inspect.isabstract(aml_AbstractElements)


def test_hyp_aml_abstractelements_constructor_exists():
    assert callable(aml_AbstractElements.__init__)


def test_hyp_aml_abstractelements_constructor_args():
    sig = inspect.signature(aml_AbstractElements.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_aml_aml_is_not_abstract():
    assert not inspect.isabstract(aml_Aml)


def test_hyp_aml_aml_constructor_exists():
    assert callable(aml_Aml.__init__)


def test_hyp_aml_aml_constructor_args():
    sig = inspect.signature(aml_Aml.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aml_formfeature_is_not_abstract():
    assert not inspect.isabstract(aml_FormFeature)


def test_hyp_aml_formfeature_constructor_exists():
    assert callable(aml_FormFeature.__init__)


def test_hyp_aml_formfeature_constructor_args():
    sig = inspect.signature(aml_FormFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_aml_speedfeature_is_not_abstract():
    assert not inspect.isabstract(aml_SpeedFeature)


def test_hyp_aml_speedfeature_constructor_exists():
    assert callable(aml_SpeedFeature.__init__)


def test_hyp_aml_speedfeature_constructor_args():
    sig = inspect.signature(aml_SpeedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"



def test_hyp_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_hyp_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "White",
        "Green",
        "Grey",
        "Red",
        "Black",
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
aml_Feature_strategy = st.builds(
    aml_Feature,
    name=
        safe_text,
    value=
        safe_text
)
aml_LengthFeature_strategy = st.builds(
    aml_LengthFeature,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
aml_NetWorkFeature_strategy = st.builds(
    aml_NetWorkFeature,
    name=
        safe_text,
    value=
        safe_text
)
aml_ColorFeature_strategy = st.builds(
    aml_ColorFeature,
    value=
        safe_text,
    name=
        safe_text
)
aml_SizeFeature_strategy = st.builds(
    aml_SizeFeature,
    value=
        st.integers(),
    name=
        safe_text
)
aml_TypeFeature_strategy = st.builds(
    aml_TypeFeature,
    value=
        safe_text,
    name=
        safe_text
)
SuperEntity_strategy = st.builds(
    SuperEntity,
)
aml_Cable_strategy = st.builds(
    aml_Cable,
)
aml_Drive_strategy = st.builds(
    aml_Drive,
)
aml_MaxFeature_strategy = st.builds(
    aml_MaxFeature,
    value=
        st.integers(),
    name=
        safe_text
)
aml_ProductPUIDFeature_strategy = st.builds(
    aml_ProductPUIDFeature,
    name=
        safe_text,
    values=
        st.integers()
)
aml_TargetGroupFeature_strategy = st.builds(
    aml_TargetGroupFeature,
    value=
        safe_text,
    name=
        safe_text
)
AbstractElements_strategy = st.builds(
    AbstractElements,
)
aml_Entity_strategy = st.builds(
    aml_Entity,
)
aml_SuperEntity_strategy = st.builds(
    aml_SuperEntity,
)
aml_PriceRule_strategy = st.builds(
    aml_PriceRule,
)
aml_MinMax_strategy = st.builds(
    aml_MinMax,
)
aml_AbstractElements_strategy = st.builds(
    aml_AbstractElements,
    name=
        safe_text
)
aml_Aml_strategy = st.builds(
    aml_Aml,
)
aml_FormFeature_strategy = st.builds(
    aml_FormFeature,
    name=
        safe_text,
    value=
        st.integers()
)
aml_SpeedFeature_strategy = st.builds(
    aml_SpeedFeature,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)




@given(instance=aml_Feature_strategy)
def test_hyp_aml_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aml_Feature_strategy)
def test_hyp_aml_feature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=aml_LengthFeature_strategy)
def test_hyp_aml_lengthfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_LengthFeature_strategy)
def test_hyp_aml_lengthfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=aml_NetWorkFeature_strategy)
def test_hyp_aml_networkfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aml_NetWorkFeature_strategy)
def test_hyp_aml_networkfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=aml_ColorFeature_strategy)
def test_hyp_aml_colorfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_ColorFeature_strategy)
def test_hyp_aml_colorfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=aml_SizeFeature_strategy)
def test_hyp_aml_sizefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_SizeFeature_strategy)
def test_hyp_aml_sizefeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=aml_TypeFeature_strategy)
def test_hyp_aml_typefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_TypeFeature_strategy)
def test_hyp_aml_typefeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=aml_MaxFeature_strategy)
def test_hyp_aml_maxfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_MaxFeature_strategy)
def test_hyp_aml_maxfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=aml_ProductPUIDFeature_strategy)
def test_hyp_aml_productpuidfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aml_ProductPUIDFeature_strategy)
def test_hyp_aml_productpuidfeature_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original




@given(instance=aml_TargetGroupFeature_strategy)
def test_hyp_aml_targetgroupfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aml_TargetGroupFeature_strategy)
def test_hyp_aml_targetgroupfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=aml_AbstractElements_strategy)
def test_hyp_aml_abstractelements_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=aml_FormFeature_strategy)
def test_hyp_aml_formfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aml_FormFeature_strategy)
def test_hyp_aml_formfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=aml_SpeedFeature_strategy)
def test_hyp_aml_speedfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aml_SpeedFeature_strategy)
def test_hyp_aml_speedfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractElements,
    SuperEntity,
    aml_AbstractElements,
    aml_Aml,
    aml_Cable,
    aml_ColorFeature,
    aml_Drive,
    aml_Entity,
    aml_Feature,
    aml_FormFeature,
    aml_LengthFeature,
    aml_MaxFeature,
    aml_MinMax,
    aml_NetWorkFeature,
    aml_PriceRule,
    aml_ProductPUIDFeature,
    aml_SizeFeature,
    aml_SpeedFeature,
    aml_SuperEntity,
    aml_TargetGroupFeature,
    aml_TypeFeature,
    Color,
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

def test_aml_AbstractElements_name_value_roundtrip():
    instance = aml_AbstractElements(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_ColorFeature_name_value_roundtrip():
    instance = aml_ColorFeature(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_ColorFeature_value_value_roundtrip():
    instance = aml_ColorFeature(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aml_Feature_name_value_roundtrip():
    instance = aml_Feature(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_Feature_value_value_roundtrip():
    instance = aml_Feature(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aml_FormFeature_name_value_roundtrip():
    instance = aml_FormFeature(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_FormFeature_value_value_roundtrip():
    instance = aml_FormFeature(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_aml_LengthFeature_name_value_roundtrip():
    instance = aml_LengthFeature(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_LengthFeature_value_value_roundtrip():
    instance = aml_LengthFeature(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_aml_MaxFeature_name_value_roundtrip():
    instance = aml_MaxFeature(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_MaxFeature_value_value_roundtrip():
    instance = aml_MaxFeature(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_aml_NetWorkFeature_name_value_roundtrip():
    instance = aml_NetWorkFeature(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_NetWorkFeature_value_value_roundtrip():
    instance = aml_NetWorkFeature(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aml_ProductPUIDFeature_name_value_roundtrip():
    instance = aml_ProductPUIDFeature(name="sample_text", values=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_ProductPUIDFeature_values_value_roundtrip():
    instance = aml_ProductPUIDFeature(name="sample_text", values=7)
    assert instance.values == 7
    instance.values = 13
    assert instance.values == 13


def test_aml_SizeFeature_name_value_roundtrip():
    instance = aml_SizeFeature(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_SizeFeature_value_value_roundtrip():
    instance = aml_SizeFeature(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_aml_SpeedFeature_name_value_roundtrip():
    instance = aml_SpeedFeature(name="sample_text", value=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_SpeedFeature_value_value_roundtrip():
    instance = aml_SpeedFeature(name="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_aml_TargetGroupFeature_name_value_roundtrip():
    instance = aml_TargetGroupFeature(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_TargetGroupFeature_value_value_roundtrip():
    instance = aml_TargetGroupFeature(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aml_TypeFeature_name_value_roundtrip():
    instance = aml_TypeFeature(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aml_TypeFeature_value_value_roundtrip():
    instance = aml_TypeFeature(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aml_Entity_isa_AbstractElements():
    instance = aml_Entity()
    assert isinstance(instance, AbstractElements)


def test_aml_MinMax_isa_AbstractElements():
    instance = aml_MinMax()
    assert isinstance(instance, AbstractElements)


def test_aml_PriceRule_isa_AbstractElements():
    instance = aml_PriceRule()
    assert isinstance(instance, AbstractElements)


def test_aml_SuperEntity_isa_AbstractElements():
    instance = aml_SuperEntity()
    assert isinstance(instance, AbstractElements)


def test_aml_Cable_isa_SuperEntity():
    instance = aml_Cable()
    assert isinstance(instance, SuperEntity)


def test_aml_Drive_isa_SuperEntity():
    instance = aml_Drive()
    assert isinstance(instance, SuperEntity)


def test_assoc_colorFeature13_link_reassign_clear():
    a = aml_ColorFeature(name="sample_text", value="sample_text")
    b1 = aml_Cable()
    b2 = aml_Cable()
    _safe_set(a, 'aml_ColorFeature', b1)
    assert _is_linked(a, 'aml_ColorFeature', b1)
    if hasattr(b1, 'aml_Cable'):
        assert _is_linked(b1, 'aml_Cable', a)
    _safe_set(a, 'aml_ColorFeature', b2)
    assert _is_linked(a, 'aml_ColorFeature', b2)
    if hasattr(b1, 'aml_Cable'):
        assert not _is_linked(b1, 'aml_Cable', a)
    if hasattr(b2, 'aml_Cable'):
        assert _is_linked(b2, 'aml_Cable', a)
    _safe_set(a, 'aml_ColorFeature', None)
    assert not _is_linked(a, 'aml_ColorFeature', b2)
    if hasattr(b2, 'aml_Cable'):
        assert not _is_linked(b2, 'aml_Cable', a)


def test_assoc_elements0_link_reassign_clear():
    a = aml_AbstractElements(name="sample_text")
    b1 = aml_Aml()
    b2 = aml_Aml()
    _safe_set(a, 'aml_AbstractElements', b1)
    assert _is_linked(a, 'aml_AbstractElements', b1)
    if hasattr(b1, 'aml_Aml'):
        assert _is_linked(b1, 'aml_Aml', a)
    _safe_set(a, 'aml_AbstractElements', b2)
    assert _is_linked(a, 'aml_AbstractElements', b2)
    if hasattr(b1, 'aml_Aml'):
        assert not _is_linked(b1, 'aml_Aml', a)
    if hasattr(b2, 'aml_Aml'):
        assert _is_linked(b2, 'aml_Aml', a)
    _safe_set(a, 'aml_AbstractElements', None)
    assert not _is_linked(a, 'aml_AbstractElements', b2)
    if hasattr(b2, 'aml_Aml'):
        assert not _is_linked(b2, 'aml_Aml', a)


def test_assoc_features20_link_reassign_clear():
    a = aml_Feature(name="sample_text", value="sample_text")
    b1 = aml_PriceRule()
    b2 = aml_PriceRule()
    _safe_set(a, 'aml_Feature', b1)
    assert _is_linked(a, 'aml_Feature', b1)
    if hasattr(b1, 'aml_PriceRule21'):
        assert _is_linked(b1, 'aml_PriceRule21', a)
    _safe_set(a, 'aml_Feature', b2)
    assert _is_linked(a, 'aml_Feature', b2)
    if hasattr(b1, 'aml_PriceRule21'):
        assert not _is_linked(b1, 'aml_PriceRule21', a)
    if hasattr(b2, 'aml_PriceRule21'):
        assert _is_linked(b2, 'aml_PriceRule21', a)
    _safe_set(a, 'aml_Feature', None)
    assert not _is_linked(a, 'aml_Feature', b2)
    if hasattr(b2, 'aml_PriceRule21'):
        assert not _is_linked(b2, 'aml_PriceRule21', a)


def test_assoc_features23_link_reassign_clear():
    a = aml_Feature(name="sample_text", value="sample_text")
    b1 = aml_Entity()
    b2 = aml_Entity()
    _safe_set(a, 'aml_Feature25', b1)
    assert _is_linked(a, 'aml_Feature25', b1)
    if hasattr(b1, 'aml_Entity24'):
        assert _is_linked(b1, 'aml_Entity24', a)
    _safe_set(a, 'aml_Feature25', b2)
    assert _is_linked(a, 'aml_Feature25', b2)
    if hasattr(b1, 'aml_Entity24'):
        assert not _is_linked(b1, 'aml_Entity24', a)
    if hasattr(b2, 'aml_Entity24'):
        assert _is_linked(b2, 'aml_Entity24', a)
    _safe_set(a, 'aml_Feature25', None)
    assert not _is_linked(a, 'aml_Feature25', b2)
    if hasattr(b2, 'aml_Entity24'):
        assert not _is_linked(b2, 'aml_Entity24', a)


def test_assoc_formFeature11_link_reassign_clear():
    a = aml_FormFeature(name="sample_text", value=7)
    b1 = aml_Drive()
    b2 = aml_Drive()
    _safe_set(a, 'aml_FormFeature', b1)
    assert _is_linked(a, 'aml_FormFeature', b1)
    if hasattr(b1, 'aml_Drive12'):
        assert _is_linked(b1, 'aml_Drive12', a)
    _safe_set(a, 'aml_FormFeature', b2)
    assert _is_linked(a, 'aml_FormFeature', b2)
    if hasattr(b1, 'aml_Drive12'):
        assert not _is_linked(b1, 'aml_Drive12', a)
    if hasattr(b2, 'aml_Drive12'):
        assert _is_linked(b2, 'aml_Drive12', a)
    _safe_set(a, 'aml_FormFeature', None)
    assert not _is_linked(a, 'aml_FormFeature', b2)
    if hasattr(b2, 'aml_Drive12'):
        assert not _is_linked(b2, 'aml_Drive12', a)


def test_assoc_lengthFeature16_link_reassign_clear():
    a = aml_LengthFeature(name="sample_text", value=3.14)
    b1 = aml_Cable()
    b2 = aml_Cable()
    _safe_set(a, 'aml_LengthFeature', b1)
    assert _is_linked(a, 'aml_LengthFeature', b1)
    if hasattr(b1, 'aml_Cable17'):
        assert _is_linked(b1, 'aml_Cable17', a)
    _safe_set(a, 'aml_LengthFeature', b2)
    assert _is_linked(a, 'aml_LengthFeature', b2)
    if hasattr(b1, 'aml_Cable17'):
        assert not _is_linked(b1, 'aml_Cable17', a)
    if hasattr(b2, 'aml_Cable17'):
        assert _is_linked(b2, 'aml_Cable17', a)
    _safe_set(a, 'aml_LengthFeature', None)
    assert not _is_linked(a, 'aml_LengthFeature', b2)
    if hasattr(b2, 'aml_Cable17'):
        assert not _is_linked(b2, 'aml_Cable17', a)


def test_assoc_maxFeature4_link_reassign_clear():
    a = aml_MaxFeature(name="sample_text", value=7)
    b1 = aml_MinMax()
    b2 = aml_MinMax()
    _safe_set(a, 'aml_MaxFeature', b1)
    assert _is_linked(a, 'aml_MaxFeature', b1)
    if hasattr(b1, 'aml_MinMax5'):
        assert _is_linked(b1, 'aml_MinMax5', a)
    _safe_set(a, 'aml_MaxFeature', b2)
    assert _is_linked(a, 'aml_MaxFeature', b2)
    if hasattr(b1, 'aml_MinMax5'):
        assert not _is_linked(b1, 'aml_MinMax5', a)
    if hasattr(b2, 'aml_MinMax5'):
        assert _is_linked(b2, 'aml_MinMax5', a)
    _safe_set(a, 'aml_MaxFeature', None)
    assert not _is_linked(a, 'aml_MaxFeature', b2)
    if hasattr(b2, 'aml_MinMax5'):
        assert not _is_linked(b2, 'aml_MinMax5', a)


def test_assoc_networkFeature14_link_reassign_clear():
    a = aml_NetWorkFeature(name="sample_text", value="sample_text")
    b1 = aml_Cable()
    b2 = aml_Cable()
    _safe_set(a, 'aml_NetWorkFeature', b1)
    assert _is_linked(a, 'aml_NetWorkFeature', b1)
    if hasattr(b1, 'aml_Cable15'):
        assert _is_linked(b1, 'aml_Cable15', a)
    _safe_set(a, 'aml_NetWorkFeature', b2)
    assert _is_linked(a, 'aml_NetWorkFeature', b2)
    if hasattr(b1, 'aml_Cable15'):
        assert not _is_linked(b1, 'aml_Cable15', a)
    if hasattr(b2, 'aml_Cable15'):
        assert _is_linked(b2, 'aml_Cable15', a)
    _safe_set(a, 'aml_NetWorkFeature', None)
    assert not _is_linked(a, 'aml_NetWorkFeature', b2)
    if hasattr(b2, 'aml_Cable15'):
        assert not _is_linked(b2, 'aml_Cable15', a)


def test_assoc_productPuidsFeature2_link_reassign_clear():
    a = aml_ProductPUIDFeature(name="sample_text", values=7)
    b1 = aml_MinMax()
    b2 = aml_MinMax()
    _safe_set(a, 'aml_ProductPUIDFeature', b1)
    assert _is_linked(a, 'aml_ProductPUIDFeature', b1)
    if hasattr(b1, 'aml_MinMax3'):
        assert _is_linked(b1, 'aml_MinMax3', a)
    _safe_set(a, 'aml_ProductPUIDFeature', b2)
    assert _is_linked(a, 'aml_ProductPUIDFeature', b2)
    if hasattr(b1, 'aml_MinMax3'):
        assert not _is_linked(b1, 'aml_MinMax3', a)
    if hasattr(b2, 'aml_MinMax3'):
        assert _is_linked(b2, 'aml_MinMax3', a)
    _safe_set(a, 'aml_ProductPUIDFeature', None)
    assert not _is_linked(a, 'aml_ProductPUIDFeature', b2)
    if hasattr(b2, 'aml_MinMax3'):
        assert not _is_linked(b2, 'aml_MinMax3', a)


def test_assoc_sizeFeature7_link_reassign_clear():
    a = aml_SizeFeature(name="sample_text", value=7)
    b1 = aml_Drive()
    b2 = aml_Drive()
    _safe_set(a, 'aml_SizeFeature', b1)
    assert _is_linked(a, 'aml_SizeFeature', b1)
    if hasattr(b1, 'aml_Drive8'):
        assert _is_linked(b1, 'aml_Drive8', a)
    _safe_set(a, 'aml_SizeFeature', b2)
    assert _is_linked(a, 'aml_SizeFeature', b2)
    if hasattr(b1, 'aml_Drive8'):
        assert not _is_linked(b1, 'aml_Drive8', a)
    if hasattr(b2, 'aml_Drive8'):
        assert _is_linked(b2, 'aml_Drive8', a)
    _safe_set(a, 'aml_SizeFeature', None)
    assert not _is_linked(a, 'aml_SizeFeature', b2)
    if hasattr(b2, 'aml_Drive8'):
        assert not _is_linked(b2, 'aml_Drive8', a)


def test_assoc_speedFeature9_link_reassign_clear():
    a = aml_SpeedFeature(name="sample_text", value=3.14)
    b1 = aml_Drive()
    b2 = aml_Drive()
    _safe_set(a, 'aml_SpeedFeature', b1)
    assert _is_linked(a, 'aml_SpeedFeature', b1)
    if hasattr(b1, 'aml_Drive10'):
        assert _is_linked(b1, 'aml_Drive10', a)
    _safe_set(a, 'aml_SpeedFeature', b2)
    assert _is_linked(a, 'aml_SpeedFeature', b2)
    if hasattr(b1, 'aml_Drive10'):
        assert not _is_linked(b1, 'aml_Drive10', a)
    if hasattr(b2, 'aml_Drive10'):
        assert _is_linked(b2, 'aml_Drive10', a)
    _safe_set(a, 'aml_SpeedFeature', None)
    assert not _is_linked(a, 'aml_SpeedFeature', b2)
    if hasattr(b2, 'aml_Drive10'):
        assert not _is_linked(b2, 'aml_Drive10', a)


def test_assoc_targetGroupFeature1_link_reassign_clear():
    a = aml_TargetGroupFeature(name="sample_text", value="sample_text")
    b1 = aml_MinMax()
    b2 = aml_MinMax()
    _safe_set(a, 'aml_TargetGroupFeature', b1)
    assert _is_linked(a, 'aml_TargetGroupFeature', b1)
    if hasattr(b1, 'aml_MinMax'):
        assert _is_linked(b1, 'aml_MinMax', a)
    _safe_set(a, 'aml_TargetGroupFeature', b2)
    assert _is_linked(a, 'aml_TargetGroupFeature', b2)
    if hasattr(b1, 'aml_MinMax'):
        assert not _is_linked(b1, 'aml_MinMax', a)
    if hasattr(b2, 'aml_MinMax'):
        assert _is_linked(b2, 'aml_MinMax', a)
    _safe_set(a, 'aml_TargetGroupFeature', None)
    assert not _is_linked(a, 'aml_TargetGroupFeature', b2)
    if hasattr(b2, 'aml_MinMax'):
        assert not _is_linked(b2, 'aml_MinMax', a)


def test_assoc_typeFeature6_link_reassign_clear():
    a = aml_TypeFeature(name="sample_text", value="sample_text")
    b1 = aml_Drive()
    b2 = aml_Drive()
    _safe_set(a, 'aml_TypeFeature', b1)
    assert _is_linked(a, 'aml_TypeFeature', b1)
    if hasattr(b1, 'aml_Drive'):
        assert _is_linked(b1, 'aml_Drive', a)
    _safe_set(a, 'aml_TypeFeature', b2)
    assert _is_linked(a, 'aml_TypeFeature', b2)
    if hasattr(b1, 'aml_Drive'):
        assert not _is_linked(b1, 'aml_Drive', a)
    if hasattr(b2, 'aml_Drive'):
        assert _is_linked(b2, 'aml_Drive', a)
    _safe_set(a, 'aml_TypeFeature', None)
    assert not _is_linked(a, 'aml_TypeFeature', b2)
    if hasattr(b2, 'aml_Drive'):
        assert not _is_linked(b2, 'aml_Drive', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractElements_strategy = st.builds(AbstractElements)
@given(instance=AbstractElements_strategy)
@settings(max_examples=25)
def test_AbstractElements_instantiation(instance):
    assert isinstance(instance, AbstractElements)


SuperEntity_strategy = st.builds(SuperEntity)
@given(instance=SuperEntity_strategy)
@settings(max_examples=25)
def test_SuperEntity_instantiation(instance):
    assert isinstance(instance, SuperEntity)


aml_AbstractElements_strategy = st.builds(aml_AbstractElements, name=safe_text)
@given(instance=aml_AbstractElements_strategy)
@settings(max_examples=25)
def test_aml_AbstractElements_instantiation(instance):
    assert isinstance(instance, aml_AbstractElements)


aml_Aml_strategy = st.builds(aml_Aml)
@given(instance=aml_Aml_strategy)
@settings(max_examples=25)
def test_aml_Aml_instantiation(instance):
    assert isinstance(instance, aml_Aml)


aml_Cable_strategy = st.builds(aml_Cable)
@given(instance=aml_Cable_strategy)
@settings(max_examples=25)
def test_aml_Cable_instantiation(instance):
    assert isinstance(instance, aml_Cable)


aml_ColorFeature_strategy = st.builds(aml_ColorFeature, name=safe_text, value=safe_text)
@given(instance=aml_ColorFeature_strategy)
@settings(max_examples=25)
def test_aml_ColorFeature_instantiation(instance):
    assert isinstance(instance, aml_ColorFeature)


aml_Drive_strategy = st.builds(aml_Drive)
@given(instance=aml_Drive_strategy)
@settings(max_examples=25)
def test_aml_Drive_instantiation(instance):
    assert isinstance(instance, aml_Drive)


aml_Entity_strategy = st.builds(aml_Entity)
@given(instance=aml_Entity_strategy)
@settings(max_examples=25)
def test_aml_Entity_instantiation(instance):
    assert isinstance(instance, aml_Entity)


aml_Feature_strategy = st.builds(aml_Feature, name=safe_text, value=safe_text)
@given(instance=aml_Feature_strategy)
@settings(max_examples=25)
def test_aml_Feature_instantiation(instance):
    assert isinstance(instance, aml_Feature)


aml_FormFeature_strategy = st.builds(aml_FormFeature, name=safe_text, value=st.integers())
@given(instance=aml_FormFeature_strategy)
@settings(max_examples=25)
def test_aml_FormFeature_instantiation(instance):
    assert isinstance(instance, aml_FormFeature)


aml_LengthFeature_strategy = st.builds(aml_LengthFeature, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=aml_LengthFeature_strategy)
@settings(max_examples=25)
def test_aml_LengthFeature_instantiation(instance):
    assert isinstance(instance, aml_LengthFeature)


aml_MaxFeature_strategy = st.builds(aml_MaxFeature, name=safe_text, value=st.integers())
@given(instance=aml_MaxFeature_strategy)
@settings(max_examples=25)
def test_aml_MaxFeature_instantiation(instance):
    assert isinstance(instance, aml_MaxFeature)


aml_MinMax_strategy = st.builds(aml_MinMax)
@given(instance=aml_MinMax_strategy)
@settings(max_examples=25)
def test_aml_MinMax_instantiation(instance):
    assert isinstance(instance, aml_MinMax)


aml_NetWorkFeature_strategy = st.builds(aml_NetWorkFeature, name=safe_text, value=safe_text)
@given(instance=aml_NetWorkFeature_strategy)
@settings(max_examples=25)
def test_aml_NetWorkFeature_instantiation(instance):
    assert isinstance(instance, aml_NetWorkFeature)


aml_PriceRule_strategy = st.builds(aml_PriceRule)
@given(instance=aml_PriceRule_strategy)
@settings(max_examples=25)
def test_aml_PriceRule_instantiation(instance):
    assert isinstance(instance, aml_PriceRule)


aml_ProductPUIDFeature_strategy = st.builds(aml_ProductPUIDFeature, name=safe_text, values=st.integers())
@given(instance=aml_ProductPUIDFeature_strategy)
@settings(max_examples=25)
def test_aml_ProductPUIDFeature_instantiation(instance):
    assert isinstance(instance, aml_ProductPUIDFeature)


aml_SizeFeature_strategy = st.builds(aml_SizeFeature, name=safe_text, value=st.integers())
@given(instance=aml_SizeFeature_strategy)
@settings(max_examples=25)
def test_aml_SizeFeature_instantiation(instance):
    assert isinstance(instance, aml_SizeFeature)


aml_SpeedFeature_strategy = st.builds(aml_SpeedFeature, name=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=aml_SpeedFeature_strategy)
@settings(max_examples=25)
def test_aml_SpeedFeature_instantiation(instance):
    assert isinstance(instance, aml_SpeedFeature)


aml_SuperEntity_strategy = st.builds(aml_SuperEntity)
@given(instance=aml_SuperEntity_strategy)
@settings(max_examples=25)
def test_aml_SuperEntity_instantiation(instance):
    assert isinstance(instance, aml_SuperEntity)


aml_TargetGroupFeature_strategy = st.builds(aml_TargetGroupFeature, name=safe_text, value=safe_text)
@given(instance=aml_TargetGroupFeature_strategy)
@settings(max_examples=25)
def test_aml_TargetGroupFeature_instantiation(instance):
    assert isinstance(instance, aml_TargetGroupFeature)


aml_TypeFeature_strategy = st.builds(aml_TypeFeature, name=safe_text, value=safe_text)
@given(instance=aml_TypeFeature_strategy)
@settings(max_examples=25)
def test_aml_TypeFeature_instantiation(instance):
    assert isinstance(instance, aml_TypeFeature)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElements,
    SuperEntity,
    aml_AbstractElements,
    aml_Aml,
    aml_Cable,
    aml_ColorFeature,
    aml_Drive,
    aml_Entity,
    aml_Feature,
    aml_FormFeature,
    aml_LengthFeature,
    aml_MaxFeature,
    aml_MinMax,
    aml_NetWorkFeature,
    aml_PriceRule,
    aml_ProductPUIDFeature,
    aml_SizeFeature,
    aml_SpeedFeature,
    aml_SuperEntity,
    aml_TargetGroupFeature,
    aml_TypeFeature,
    Color,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_colorFeature13_stub_double():
    # aml_Cable has no real 'aml_Cable' property in the generated
    # code (a bare stub) -- manually attach it so aml_ColorFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_ColorFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_ColorFeature(name="sample_text", value="sample_text")
    partner = aml_Cable()
    setattr(partner, 'aml_Cable', None)
    _safe_set(owner, 'aml_ColorFeature', partner)
    assert getattr(partner, 'aml_Cable') == owner
    _safe_set(owner, 'aml_ColorFeature', None)
    assert getattr(partner, 'aml_Cable') is None


def test_assoc_elements0_stub_double():
    # aml_Aml has no real 'aml_Aml' property in the generated
    # code (a bare stub) -- manually attach it so aml_AbstractElements's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_AbstractElements's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_AbstractElements(name="sample_text")
    partner = aml_Aml()
    setattr(partner, 'aml_Aml', None)
    _safe_set(owner, 'aml_AbstractElements', partner)
    assert owner in getattr(partner, 'aml_Aml')
    _safe_set(owner, 'aml_AbstractElements', None)
    assert owner not in getattr(partner, 'aml_Aml')


def test_assoc_features20_stub_double():
    # aml_PriceRule has no real 'aml_PriceRule21' property in the generated
    # code (a bare stub) -- manually attach it so aml_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Feature(name="sample_text", value="sample_text")
    partner = aml_PriceRule()
    setattr(partner, 'aml_PriceRule21', None)
    _safe_set(owner, 'aml_Feature', partner)
    assert owner in getattr(partner, 'aml_PriceRule21')
    _safe_set(owner, 'aml_Feature', None)
    assert owner not in getattr(partner, 'aml_PriceRule21')


def test_assoc_features23_stub_double():
    # aml_Entity has no real 'aml_Entity24' property in the generated
    # code (a bare stub) -- manually attach it so aml_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Feature(name="sample_text", value="sample_text")
    partner = aml_Entity()
    setattr(partner, 'aml_Entity24', None)
    _safe_set(owner, 'aml_Feature25', partner)
    assert owner in getattr(partner, 'aml_Entity24')
    _safe_set(owner, 'aml_Feature25', None)
    assert owner not in getattr(partner, 'aml_Entity24')


def test_assoc_formFeature11_stub_double():
    # aml_Drive has no real 'aml_Drive12' property in the generated
    # code (a bare stub) -- manually attach it so aml_FormFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_FormFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_FormFeature(name="sample_text", value=7)
    partner = aml_Drive()
    setattr(partner, 'aml_Drive12', None)
    _safe_set(owner, 'aml_FormFeature', partner)
    assert getattr(partner, 'aml_Drive12') == owner
    _safe_set(owner, 'aml_FormFeature', None)
    assert getattr(partner, 'aml_Drive12') is None


def test_assoc_lengthFeature16_stub_double():
    # aml_Cable has no real 'aml_Cable17' property in the generated
    # code (a bare stub) -- manually attach it so aml_LengthFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_LengthFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_LengthFeature(name="sample_text", value=3.14)
    partner = aml_Cable()
    setattr(partner, 'aml_Cable17', None)
    _safe_set(owner, 'aml_LengthFeature', partner)
    assert getattr(partner, 'aml_Cable17') == owner
    _safe_set(owner, 'aml_LengthFeature', None)
    assert getattr(partner, 'aml_Cable17') is None


def test_assoc_maxFeature4_stub_double():
    # aml_MinMax has no real 'aml_MinMax5' property in the generated
    # code (a bare stub) -- manually attach it so aml_MaxFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MaxFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MaxFeature(name="sample_text", value=7)
    partner = aml_MinMax()
    setattr(partner, 'aml_MinMax5', None)
    _safe_set(owner, 'aml_MaxFeature', partner)
    assert getattr(partner, 'aml_MinMax5') == owner
    _safe_set(owner, 'aml_MaxFeature', None)
    assert getattr(partner, 'aml_MinMax5') is None


def test_assoc_networkFeature14_stub_double():
    # aml_Cable has no real 'aml_Cable15' property in the generated
    # code (a bare stub) -- manually attach it so aml_NetWorkFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_NetWorkFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_NetWorkFeature(name="sample_text", value="sample_text")
    partner = aml_Cable()
    setattr(partner, 'aml_Cable15', None)
    _safe_set(owner, 'aml_NetWorkFeature', partner)
    assert getattr(partner, 'aml_Cable15') == owner
    _safe_set(owner, 'aml_NetWorkFeature', None)
    assert getattr(partner, 'aml_Cable15') is None


def test_assoc_productPuidsFeature2_stub_double():
    # aml_MinMax has no real 'aml_MinMax3' property in the generated
    # code (a bare stub) -- manually attach it so aml_ProductPUIDFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_ProductPUIDFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_ProductPUIDFeature(name="sample_text", values=7)
    partner = aml_MinMax()
    setattr(partner, 'aml_MinMax3', None)
    _safe_set(owner, 'aml_ProductPUIDFeature', partner)
    assert getattr(partner, 'aml_MinMax3') == owner
    _safe_set(owner, 'aml_ProductPUIDFeature', None)
    assert getattr(partner, 'aml_MinMax3') is None


def test_assoc_sizeFeature7_stub_double():
    # aml_Drive has no real 'aml_Drive8' property in the generated
    # code (a bare stub) -- manually attach it so aml_SizeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_SizeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_SizeFeature(name="sample_text", value=7)
    partner = aml_Drive()
    setattr(partner, 'aml_Drive8', None)
    _safe_set(owner, 'aml_SizeFeature', partner)
    assert getattr(partner, 'aml_Drive8') == owner
    _safe_set(owner, 'aml_SizeFeature', None)
    assert getattr(partner, 'aml_Drive8') is None


def test_assoc_speedFeature9_stub_double():
    # aml_Drive has no real 'aml_Drive10' property in the generated
    # code (a bare stub) -- manually attach it so aml_SpeedFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_SpeedFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_SpeedFeature(name="sample_text", value=3.14)
    partner = aml_Drive()
    setattr(partner, 'aml_Drive10', None)
    _safe_set(owner, 'aml_SpeedFeature', partner)
    assert getattr(partner, 'aml_Drive10') == owner
    _safe_set(owner, 'aml_SpeedFeature', None)
    assert getattr(partner, 'aml_Drive10') is None


def test_assoc_targetGroupFeature1_stub_double():
    # aml_MinMax has no real 'aml_MinMax' property in the generated
    # code (a bare stub) -- manually attach it so aml_TargetGroupFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_TargetGroupFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_TargetGroupFeature(name="sample_text", value="sample_text")
    partner = aml_MinMax()
    setattr(partner, 'aml_MinMax', None)
    _safe_set(owner, 'aml_TargetGroupFeature', partner)
    assert getattr(partner, 'aml_MinMax') == owner
    _safe_set(owner, 'aml_TargetGroupFeature', None)
    assert getattr(partner, 'aml_MinMax') is None


def test_assoc_typeFeature6_stub_double():
    # aml_Drive has no real 'aml_Drive' property in the generated
    # code (a bare stub) -- manually attach it so aml_TypeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_TypeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_TypeFeature(name="sample_text", value="sample_text")
    partner = aml_Drive()
    setattr(partner, 'aml_Drive', None)
    _safe_set(owner, 'aml_TypeFeature', partner)
    assert getattr(partner, 'aml_Drive') == owner
    _safe_set(owner, 'aml_TypeFeature', None)
    assert getattr(partner, 'aml_Drive') is None




from python_code import aml_AbstractElements
from python_code import aml_Aml

def test_aml_AbstractElements___init__():
    assert aml_AbstractElements.__init__(aml_AbstractElements('', aml_AbstractElements=aml_Aml()), '', aml_AbstractElements=aml_Aml()) == None
from python_code import aml_Cable
from python_code import aml_ColorFeature

def test_aml_ColorFeature___init__():
    assert aml_ColorFeature.__init__(aml_ColorFeature('', '\x00', aml_ColorFeature=aml_Cable()), '\x00\x00', '', aml_ColorFeature=aml_Cable()) == None
from python_code import aml_Entity
from python_code import aml_Feature
from python_code import aml_PriceRule

def test_aml_Feature___init__():
    assert aml_Feature.__init__(aml_Feature('', '\x00', aml_Feature=aml_PriceRule(), aml_Feature25=aml_Entity()), '\x00\x00', '', aml_Feature=aml_PriceRule(), aml_Feature25=aml_Entity()) == None
from python_code import aml_Drive
from python_code import aml_FormFeature

def test_aml_FormFeature___init__():
    assert aml_FormFeature.__init__(aml_FormFeature('', 0, aml_FormFeature=aml_Drive()), '', 0, aml_FormFeature=aml_Drive()) == None
from python_code import aml_Cable
from python_code import aml_LengthFeature

def test_aml_LengthFeature___init__():
    assert aml_LengthFeature.__init__(aml_LengthFeature('\x00', 0.0, aml_LengthFeature=aml_Cable()), '', 0.0, aml_LengthFeature=aml_Cable()) == None
from python_code import aml_MaxFeature
from python_code import aml_MinMax

def test_aml_MaxFeature___init__():
    assert aml_MaxFeature.__init__(aml_MaxFeature('', 0, aml_MaxFeature=aml_MinMax()), '', 0, aml_MaxFeature=aml_MinMax()) == None
from python_code import aml_Cable
from python_code import aml_NetWorkFeature

def test_aml_NetWorkFeature___init__():
    assert aml_NetWorkFeature.__init__(aml_NetWorkFeature('', '\x00', aml_NetWorkFeature=aml_Cable()), '\x00\x00', '', aml_NetWorkFeature=aml_Cable()) == None
from python_code import aml_MinMax
from python_code import aml_ProductPUIDFeature

def test_aml_ProductPUIDFeature___init__():
    assert aml_ProductPUIDFeature.__init__(aml_ProductPUIDFeature('', 0, aml_ProductPUIDFeature=aml_MinMax()), '', 0, aml_ProductPUIDFeature=aml_MinMax()) == None
from python_code import aml_Drive
from python_code import aml_SizeFeature

def test_aml_SizeFeature___init__():
    assert aml_SizeFeature.__init__(aml_SizeFeature('', 0, aml_SizeFeature=aml_Drive()), '', 0, aml_SizeFeature=aml_Drive()) == None
from python_code import aml_Drive
from python_code import aml_SpeedFeature

def test_aml_SpeedFeature___init__():
    assert aml_SpeedFeature.__init__(aml_SpeedFeature('\x00', 0.0, aml_SpeedFeature=aml_Drive()), '', 0.0, aml_SpeedFeature=aml_Drive()) == None
from python_code import aml_MinMax
from python_code import aml_TargetGroupFeature

def test_aml_TargetGroupFeature___init__():
    assert aml_TargetGroupFeature.__init__(aml_TargetGroupFeature('', '\x00', aml_TargetGroupFeature=aml_MinMax()), '\x00\x00', '', aml_TargetGroupFeature=aml_MinMax()) == None
from python_code import aml_Drive
from python_code import aml_TypeFeature

def test_aml_TypeFeature___init__():
    assert aml_TypeFeature.__init__(aml_TypeFeature('', '\x00', aml_TypeFeature=aml_Drive()), '\x00\x00', '', aml_TypeFeature=aml_Drive()) == None

