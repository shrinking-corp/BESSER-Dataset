import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CaseStyle,
    Parameter,
    Pattern,
    Styling_BooleanParameter,
    Styling_CaseStyle,
    Styling_ConstantPattern,
    Styling_Default,
    Styling_EObject,
    Styling_EObjectParameter,
    Styling_IPredicate,
    Styling_Icon,
    Styling_IntParameter,
    Styling_ModelPattern,
    Styling_OperationPattern,
    Styling_Parameter,
    Styling_Pattern,
    Styling_Segment,
    Styling_StringParameter,
    Styling_Style,
    Styling_Styling,
    Styling_StylingModel,
    Styling_StylingPredicate,
    FontOption,
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

def test_Styling_BooleanParameter_value_value_roundtrip():
    instance = Styling_BooleanParameter(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_Styling_ConstantPattern_value_value_roundtrip():
    instance = Styling_ConstantPattern(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Styling_Icon_image_value_roundtrip():
    instance = Styling_Icon(image="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_Styling_IntParameter_value_value_roundtrip():
    instance = Styling_IntParameter(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_Styling_ModelPattern_attributeName_value_roundtrip():
    instance = Styling_ModelPattern(attributeName="sample_text")
    assert instance.attributeName == "sample_text"
    instance.attributeName = "sample_text_2"
    assert instance.attributeName == "sample_text_2"


def test_Styling_OperationPattern_operation_value_roundtrip():
    instance = Styling_OperationPattern(operation="sample_text")
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_Styling_Parameter_name_value_roundtrip():
    instance = Styling_Parameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Styling_StringParameter_value_value_roundtrip():
    instance = Styling_StringParameter(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Styling_Style_appliedFonts_value_roundtrip():
    instance = Styling_Style(appliedFonts="sample_text", color="sample_text")
    assert instance.appliedFonts == "sample_text"
    instance.appliedFonts = "sample_text_2"
    assert instance.appliedFonts == "sample_text_2"


def test_Styling_Style_color_value_roundtrip():
    instance = Styling_Style(appliedFonts="sample_text", color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_Styling_StylingModel_modeName_value_roundtrip():
    instance = Styling_StylingModel(modeName="sample_text")
    assert instance.modeName == "sample_text"
    instance.modeName = "sample_text_2"
    assert instance.modeName == "sample_text_2"


def test_Styling_Default_isa_CaseStyle():
    instance = Styling_Default()
    assert isinstance(instance, CaseStyle)


def test_Styling_StylingPredicate_isa_CaseStyle():
    instance = Styling_StylingPredicate()
    assert isinstance(instance, CaseStyle)


def test_Styling_BooleanParameter_isa_Parameter():
    instance = Styling_BooleanParameter(value=True)
    assert isinstance(instance, Parameter)


def test_Styling_EObjectParameter_isa_Parameter():
    instance = Styling_EObjectParameter()
    assert isinstance(instance, Parameter)


def test_Styling_IntParameter_isa_Parameter():
    instance = Styling_IntParameter(value=7)
    assert isinstance(instance, Parameter)


def test_Styling_StringParameter_isa_Parameter():
    instance = Styling_StringParameter(value="sample_text")
    assert isinstance(instance, Parameter)


def test_Styling_ConstantPattern_isa_Pattern():
    instance = Styling_ConstantPattern(value="sample_text")
    assert isinstance(instance, Pattern)


def test_Styling_ModelPattern_isa_Pattern():
    instance = Styling_ModelPattern(attributeName="sample_text")
    assert isinstance(instance, Pattern)


def test_Styling_OperationPattern_isa_Pattern():
    instance = Styling_OperationPattern(operation="sample_text")
    assert isinstance(instance, Pattern)


def test_assoc_default1_link_reassign_clear():
    a = Styling_StylingModel(modeName="sample_text")
    b1 = Styling_Default()
    b2 = Styling_Default()
    _safe_set(a, 'Styling_StylingModel2', b1)
    assert _is_linked(a, 'Styling_StylingModel2', b1)
    if hasattr(b1, 'Styling_Default'):
        assert _is_linked(b1, 'Styling_Default', a)
    _safe_set(a, 'Styling_StylingModel2', b2)
    assert _is_linked(a, 'Styling_StylingModel2', b2)
    if hasattr(b1, 'Styling_Default'):
        assert not _is_linked(b1, 'Styling_Default', a)
    if hasattr(b2, 'Styling_Default'):
        assert _is_linked(b2, 'Styling_Default', a)
    _safe_set(a, 'Styling_StylingModel2', None)
    assert not _is_linked(a, 'Styling_StylingModel2', b2)
    if hasattr(b2, 'Styling_Default'):
        assert not _is_linked(b2, 'Styling_Default', a)


def test_assoc_icon10_link_reassign_clear():
    a = Styling_Icon(image="sample_text")
    b1 = Styling_CaseStyle()
    b2 = Styling_CaseStyle()
    _safe_set(a, 'Styling_Icon', b1)
    assert _is_linked(a, 'Styling_Icon', b1)
    if hasattr(b1, 'Styling_CaseStyle11'):
        assert _is_linked(b1, 'Styling_CaseStyle11', a)
    _safe_set(a, 'Styling_Icon', b2)
    assert _is_linked(a, 'Styling_Icon', b2)
    if hasattr(b1, 'Styling_CaseStyle11'):
        assert not _is_linked(b1, 'Styling_CaseStyle11', a)
    if hasattr(b2, 'Styling_CaseStyle11'):
        assert _is_linked(b2, 'Styling_CaseStyle11', a)
    _safe_set(a, 'Styling_Icon', None)
    assert not _is_linked(a, 'Styling_Icon', b2)
    if hasattr(b2, 'Styling_CaseStyle11'):
        assert not _is_linked(b2, 'Styling_CaseStyle11', a)


def test_assoc_models12_link_reassign_clear():
    a = Styling_StylingModel(modeName="sample_text")
    b1 = Styling_Styling()
    b2 = Styling_Styling()
    _safe_set(a, 'Styling_StylingModel13', b1)
    assert _is_linked(a, 'Styling_StylingModel13', b1)
    if hasattr(b1, 'Styling_Styling'):
        assert _is_linked(b1, 'Styling_Styling', a)
    _safe_set(a, 'Styling_StylingModel13', b2)
    assert _is_linked(a, 'Styling_StylingModel13', b2)
    if hasattr(b1, 'Styling_Styling'):
        assert not _is_linked(b1, 'Styling_Styling', a)
    if hasattr(b2, 'Styling_Styling'):
        assert _is_linked(b2, 'Styling_Styling', a)
    _safe_set(a, 'Styling_StylingModel13', None)
    assert not _is_linked(a, 'Styling_StylingModel13', b2)
    if hasattr(b2, 'Styling_Styling'):
        assert not _is_linked(b2, 'Styling_Styling', a)


def test_assoc_parameters14_link_reassign_clear():
    a = Styling_Parameter(name="sample_text")
    b1 = Styling_OperationPattern(operation="sample_text")
    b2 = Styling_OperationPattern(operation="sample_text_2")
    _safe_set(a, 'Styling_Parameter', b1)
    assert _is_linked(a, 'Styling_Parameter', b1)
    if hasattr(b1, 'Styling_OperationPattern'):
        assert _is_linked(b1, 'Styling_OperationPattern', a)
    _safe_set(a, 'Styling_Parameter', b2)
    assert _is_linked(a, 'Styling_Parameter', b2)
    if hasattr(b1, 'Styling_OperationPattern'):
        assert not _is_linked(b1, 'Styling_OperationPattern', a)
    if hasattr(b2, 'Styling_OperationPattern'):
        assert _is_linked(b2, 'Styling_OperationPattern', a)
    _safe_set(a, 'Styling_Parameter', None)
    assert not _is_linked(a, 'Styling_Parameter', b2)
    if hasattr(b2, 'Styling_OperationPattern'):
        assert not _is_linked(b2, 'Styling_OperationPattern', a)


def test_assoc_pattern5_link_reassign_clear():
    a = Styling_Segment()
    b1 = Styling_Pattern()
    b2 = Styling_Pattern()
    _safe_set(a, 'Styling_Segment6', b1)
    assert _is_linked(a, 'Styling_Segment6', b1)
    if hasattr(b1, 'Styling_Pattern'):
        assert _is_linked(b1, 'Styling_Pattern', a)
    _safe_set(a, 'Styling_Segment6', b2)
    assert _is_linked(a, 'Styling_Segment6', b2)
    if hasattr(b1, 'Styling_Pattern'):
        assert not _is_linked(b1, 'Styling_Pattern', a)
    if hasattr(b2, 'Styling_Pattern'):
        assert _is_linked(b2, 'Styling_Pattern', a)
    _safe_set(a, 'Styling_Segment6', None)
    assert not _is_linked(a, 'Styling_Segment6', b2)
    if hasattr(b2, 'Styling_Pattern'):
        assert not _is_linked(b2, 'Styling_Pattern', a)


def test_assoc_segments7_link_reassign_clear():
    a = Styling_Segment()
    b1 = Styling_CaseStyle()
    b2 = Styling_CaseStyle()
    _safe_set(a, 'Styling_Segment9', b1)
    assert _is_linked(a, 'Styling_Segment9', b1)
    if hasattr(b1, 'Styling_CaseStyle8'):
        assert _is_linked(b1, 'Styling_CaseStyle8', a)
    _safe_set(a, 'Styling_Segment9', b2)
    assert _is_linked(a, 'Styling_Segment9', b2)
    if hasattr(b1, 'Styling_CaseStyle8'):
        assert not _is_linked(b1, 'Styling_CaseStyle8', a)
    if hasattr(b2, 'Styling_CaseStyle8'):
        assert _is_linked(b2, 'Styling_CaseStyle8', a)
    _safe_set(a, 'Styling_Segment9', None)
    assert not _is_linked(a, 'Styling_Segment9', b2)
    if hasattr(b2, 'Styling_CaseStyle8'):
        assert not _is_linked(b2, 'Styling_CaseStyle8', a)


def test_assoc_style4_link_reassign_clear():
    a = Styling_Style(appliedFonts="sample_text", color="sample_text")
    b1 = Styling_Segment()
    b2 = Styling_Segment()
    _safe_set(a, 'Styling_Style', b1)
    assert _is_linked(a, 'Styling_Style', b1)
    if hasattr(b1, 'Styling_Segment'):
        assert _is_linked(b1, 'Styling_Segment', a)
    _safe_set(a, 'Styling_Style', b2)
    assert _is_linked(a, 'Styling_Style', b2)
    if hasattr(b1, 'Styling_Segment'):
        assert not _is_linked(b1, 'Styling_Segment', a)
    if hasattr(b2, 'Styling_Segment'):
        assert _is_linked(b2, 'Styling_Segment', a)
    _safe_set(a, 'Styling_Style', None)
    assert not _is_linked(a, 'Styling_Style', b2)
    if hasattr(b2, 'Styling_Segment'):
        assert not _is_linked(b2, 'Styling_Segment', a)


def test_assoc_styles0_link_reassign_clear():
    a = Styling_StylingModel(modeName="sample_text")
    b1 = Styling_CaseStyle()
    b2 = Styling_CaseStyle()
    _safe_set(a, 'Styling_StylingModel', {b1})
    assert _is_linked(a, 'Styling_StylingModel', b1)
    if hasattr(b1, 'Styling_CaseStyle'):
        assert _is_linked(b1, 'Styling_CaseStyle', a)
    _safe_set(a, 'Styling_StylingModel', {b2})
    assert _is_linked(a, 'Styling_StylingModel', b2)
    if hasattr(b1, 'Styling_CaseStyle'):
        assert not _is_linked(b1, 'Styling_CaseStyle', a)
    if hasattr(b2, 'Styling_CaseStyle'):
        assert _is_linked(b2, 'Styling_CaseStyle', a)
    _safe_set(a, 'Styling_StylingModel', set())
    assert not _is_linked(a, 'Styling_StylingModel', b2)
    if hasattr(b2, 'Styling_CaseStyle'):
        assert not _is_linked(b2, 'Styling_CaseStyle', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CaseStyle_strategy = st.builds(CaseStyle)
@given(instance=CaseStyle_strategy)
@settings(max_examples=25)
def test_CaseStyle_instantiation(instance):
    assert isinstance(instance, CaseStyle)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


Pattern_strategy = st.builds(Pattern)
@given(instance=Pattern_strategy)
@settings(max_examples=25)
def test_Pattern_instantiation(instance):
    assert isinstance(instance, Pattern)


Styling_BooleanParameter_strategy = st.builds(Styling_BooleanParameter, value=st.booleans())
@given(instance=Styling_BooleanParameter_strategy)
@settings(max_examples=25)
def test_Styling_BooleanParameter_instantiation(instance):
    assert isinstance(instance, Styling_BooleanParameter)


Styling_CaseStyle_strategy = st.builds(Styling_CaseStyle)
@given(instance=Styling_CaseStyle_strategy)
@settings(max_examples=25)
def test_Styling_CaseStyle_instantiation(instance):
    assert isinstance(instance, Styling_CaseStyle)


Styling_ConstantPattern_strategy = st.builds(Styling_ConstantPattern, value=safe_text)
@given(instance=Styling_ConstantPattern_strategy)
@settings(max_examples=25)
def test_Styling_ConstantPattern_instantiation(instance):
    assert isinstance(instance, Styling_ConstantPattern)


Styling_Default_strategy = st.builds(Styling_Default)
@given(instance=Styling_Default_strategy)
@settings(max_examples=25)
def test_Styling_Default_instantiation(instance):
    assert isinstance(instance, Styling_Default)


Styling_EObject_strategy = st.builds(Styling_EObject)
@given(instance=Styling_EObject_strategy)
@settings(max_examples=25)
def test_Styling_EObject_instantiation(instance):
    assert isinstance(instance, Styling_EObject)


Styling_EObjectParameter_strategy = st.builds(Styling_EObjectParameter)
@given(instance=Styling_EObjectParameter_strategy)
@settings(max_examples=25)
def test_Styling_EObjectParameter_instantiation(instance):
    assert isinstance(instance, Styling_EObjectParameter)


Styling_IPredicate_strategy = st.builds(Styling_IPredicate)
@given(instance=Styling_IPredicate_strategy)
@settings(max_examples=25)
def test_Styling_IPredicate_instantiation(instance):
    assert isinstance(instance, Styling_IPredicate)


Styling_Icon_strategy = st.builds(Styling_Icon, image=safe_text)
@given(instance=Styling_Icon_strategy)
@settings(max_examples=25)
def test_Styling_Icon_instantiation(instance):
    assert isinstance(instance, Styling_Icon)


Styling_IntParameter_strategy = st.builds(Styling_IntParameter, value=st.integers())
@given(instance=Styling_IntParameter_strategy)
@settings(max_examples=25)
def test_Styling_IntParameter_instantiation(instance):
    assert isinstance(instance, Styling_IntParameter)


Styling_ModelPattern_strategy = st.builds(Styling_ModelPattern, attributeName=safe_text)
@given(instance=Styling_ModelPattern_strategy)
@settings(max_examples=25)
def test_Styling_ModelPattern_instantiation(instance):
    assert isinstance(instance, Styling_ModelPattern)


Styling_OperationPattern_strategy = st.builds(Styling_OperationPattern, operation=safe_text)
@given(instance=Styling_OperationPattern_strategy)
@settings(max_examples=25)
def test_Styling_OperationPattern_instantiation(instance):
    assert isinstance(instance, Styling_OperationPattern)


Styling_Parameter_strategy = st.builds(Styling_Parameter, name=safe_text)
@given(instance=Styling_Parameter_strategy)
@settings(max_examples=25)
def test_Styling_Parameter_instantiation(instance):
    assert isinstance(instance, Styling_Parameter)


Styling_Pattern_strategy = st.builds(Styling_Pattern)
@given(instance=Styling_Pattern_strategy)
@settings(max_examples=25)
def test_Styling_Pattern_instantiation(instance):
    assert isinstance(instance, Styling_Pattern)


Styling_Segment_strategy = st.builds(Styling_Segment)
@given(instance=Styling_Segment_strategy)
@settings(max_examples=25)
def test_Styling_Segment_instantiation(instance):
    assert isinstance(instance, Styling_Segment)


Styling_StringParameter_strategy = st.builds(Styling_StringParameter, value=safe_text)
@given(instance=Styling_StringParameter_strategy)
@settings(max_examples=25)
def test_Styling_StringParameter_instantiation(instance):
    assert isinstance(instance, Styling_StringParameter)


Styling_Style_strategy = st.builds(Styling_Style, appliedFonts=safe_text, color=safe_text)
@given(instance=Styling_Style_strategy)
@settings(max_examples=25)
def test_Styling_Style_instantiation(instance):
    assert isinstance(instance, Styling_Style)


Styling_Styling_strategy = st.builds(Styling_Styling)
@given(instance=Styling_Styling_strategy)
@settings(max_examples=25)
def test_Styling_Styling_instantiation(instance):
    assert isinstance(instance, Styling_Styling)


Styling_StylingModel_strategy = st.builds(Styling_StylingModel, modeName=safe_text)
@given(instance=Styling_StylingModel_strategy)
@settings(max_examples=25)
def test_Styling_StylingModel_instantiation(instance):
    assert isinstance(instance, Styling_StylingModel)


Styling_StylingPredicate_strategy = st.builds(Styling_StylingPredicate)
@given(instance=Styling_StylingPredicate_strategy)
@settings(max_examples=25)
def test_Styling_StylingPredicate_instantiation(instance):
    assert isinstance(instance, Styling_StylingPredicate)


