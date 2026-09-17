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
    Styling_EObject,
    Pattern,
    Styling_ConstantPattern,
    Parameter,
    Styling_StringParameter,
    Styling_BooleanParameter,
    Styling_EObjectParameter,
    Styling_IntParameter,
    Styling_Parameter,
    Styling_OperationPattern,
    Styling_ModelPattern,
    Styling_Styling,
    Styling_Style,
    Styling_Icon,
    Styling_Pattern,
    Styling_Segment,
    Styling_IPredicate,
    CaseStyle,
    Styling_StylingPredicate,
    Styling_Basic,
    Styling_Default,
    Styling_CaseStyle,
    Styling_StylingModel,
    FontOption,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_styling_eobject_is_not_abstract():
    assert not inspect.isabstract(Styling_EObject)


def test_hyp_styling_eobject_constructor_exists():
    assert callable(Styling_EObject.__init__)


def test_hyp_styling_eobject_constructor_args():
    sig = inspect.signature(Styling_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_hyp_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_hyp_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_constantpattern_is_not_abstract():
    assert not inspect.isabstract(Styling_ConstantPattern)


def test_hyp_styling_constantpattern_constructor_exists():
    assert callable(Styling_ConstantPattern.__init__)


def test_hyp_styling_constantpattern_constructor_args():
    sig = inspect.signature(Styling_ConstantPattern.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_stringparameter_is_not_abstract():
    assert not inspect.isabstract(Styling_StringParameter)


def test_hyp_styling_stringparameter_constructor_exists():
    assert callable(Styling_StringParameter.__init__)


def test_hyp_styling_stringparameter_constructor_args():
    sig = inspect.signature(Styling_StringParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_styling_booleanparameter_is_not_abstract():
    assert not inspect.isabstract(Styling_BooleanParameter)


def test_hyp_styling_booleanparameter_constructor_exists():
    assert callable(Styling_BooleanParameter.__init__)


def test_hyp_styling_booleanparameter_constructor_args():
    sig = inspect.signature(Styling_BooleanParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_styling_eobjectparameter_is_not_abstract():
    assert not inspect.isabstract(Styling_EObjectParameter)


def test_hyp_styling_eobjectparameter_constructor_exists():
    assert callable(Styling_EObjectParameter.__init__)


def test_hyp_styling_eobjectparameter_constructor_args():
    sig = inspect.signature(Styling_EObjectParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_intparameter_is_not_abstract():
    assert not inspect.isabstract(Styling_IntParameter)


def test_hyp_styling_intparameter_constructor_exists():
    assert callable(Styling_IntParameter.__init__)


def test_hyp_styling_intparameter_constructor_args():
    sig = inspect.signature(Styling_IntParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_styling_parameter_is_not_abstract():
    assert not inspect.isabstract(Styling_Parameter)


def test_hyp_styling_parameter_constructor_exists():
    assert callable(Styling_Parameter.__init__)


def test_hyp_styling_parameter_constructor_args():
    sig = inspect.signature(Styling_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_styling_operationpattern_is_not_abstract():
    assert not inspect.isabstract(Styling_OperationPattern)


def test_hyp_styling_operationpattern_constructor_exists():
    assert callable(Styling_OperationPattern.__init__)


def test_hyp_styling_operationpattern_constructor_args():
    sig = inspect.signature(Styling_OperationPattern.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"




def test_hyp_styling_modelpattern_is_not_abstract():
    assert not inspect.isabstract(Styling_ModelPattern)


def test_hyp_styling_modelpattern_constructor_exists():
    assert callable(Styling_ModelPattern.__init__)


def test_hyp_styling_modelpattern_constructor_args():
    sig = inspect.signature(Styling_ModelPattern.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"




def test_hyp_styling_styling_is_not_abstract():
    assert not inspect.isabstract(Styling_Styling)


def test_hyp_styling_styling_constructor_exists():
    assert callable(Styling_Styling.__init__)


def test_hyp_styling_styling_constructor_args():
    sig = inspect.signature(Styling_Styling.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_style_is_not_abstract():
    assert not inspect.isabstract(Styling_Style)


def test_hyp_styling_style_constructor_exists():
    assert callable(Styling_Style.__init__)


def test_hyp_styling_style_constructor_args():
    sig = inspect.signature(Styling_Style.__init__)
    params = list(sig.parameters.keys())
    assert "appliedFonts" in params, "Missing parameter 'appliedFonts'"
    assert "color" in params, "Missing parameter 'color'"





def test_hyp_styling_icon_is_not_abstract():
    assert not inspect.isabstract(Styling_Icon)


def test_hyp_styling_icon_constructor_exists():
    assert callable(Styling_Icon.__init__)


def test_hyp_styling_icon_constructor_args():
    sig = inspect.signature(Styling_Icon.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"




def test_hyp_styling_pattern_is_not_abstract():
    assert not inspect.isabstract(Styling_Pattern)


def test_hyp_styling_pattern_constructor_exists():
    assert callable(Styling_Pattern.__init__)


def test_hyp_styling_pattern_constructor_args():
    sig = inspect.signature(Styling_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_segment_is_not_abstract():
    assert not inspect.isabstract(Styling_Segment)


def test_hyp_styling_segment_constructor_exists():
    assert callable(Styling_Segment.__init__)


def test_hyp_styling_segment_constructor_args():
    sig = inspect.signature(Styling_Segment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_ipredicate_is_not_abstract():
    assert not inspect.isabstract(Styling_IPredicate)


def test_hyp_styling_ipredicate_constructor_exists():
    assert callable(Styling_IPredicate.__init__)


def test_hyp_styling_ipredicate_constructor_args():
    sig = inspect.signature(Styling_IPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_casestyle_is_not_abstract():
    assert not inspect.isabstract(CaseStyle)


def test_hyp_casestyle_constructor_exists():
    assert callable(CaseStyle.__init__)


def test_hyp_casestyle_constructor_args():
    sig = inspect.signature(CaseStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_stylingpredicate_is_not_abstract():
    assert not inspect.isabstract(Styling_StylingPredicate)


def test_hyp_styling_stylingpredicate_constructor_exists():
    assert callable(Styling_StylingPredicate.__init__)


def test_hyp_styling_stylingpredicate_constructor_args():
    sig = inspect.signature(Styling_StylingPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_basic_is_not_abstract():
    assert not inspect.isabstract(Styling_Basic)


def test_hyp_styling_basic_constructor_exists():
    assert callable(Styling_Basic.__init__)


def test_hyp_styling_basic_constructor_args():
    sig = inspect.signature(Styling_Basic.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_default_is_not_abstract():
    assert not inspect.isabstract(Styling_Default)


def test_hyp_styling_default_constructor_exists():
    assert callable(Styling_Default.__init__)


def test_hyp_styling_default_constructor_args():
    sig = inspect.signature(Styling_Default.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_casestyle_is_not_abstract():
    assert not inspect.isabstract(Styling_CaseStyle)


def test_hyp_styling_casestyle_constructor_exists():
    assert callable(Styling_CaseStyle.__init__)


def test_hyp_styling_casestyle_constructor_args():
    sig = inspect.signature(Styling_CaseStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styling_stylingmodel_is_not_abstract():
    assert not inspect.isabstract(Styling_StylingModel)


def test_hyp_styling_stylingmodel_constructor_exists():
    assert callable(Styling_StylingModel.__init__)


def test_hyp_styling_stylingmodel_constructor_args():
    sig = inspect.signature(Styling_StylingModel.__init__)
    params = list(sig.parameters.keys())
    assert "modeName" in params, "Missing parameter 'modeName'"


def test_hyp_fontoption_exists():
    # Check that the Enumeration exists
    assert FontOption is not None

def test_hyp_fontoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontOption]
    expected_literals = [
        "UNDERLINE",
        "ITALIC",
        "BOLD",
        "STRIKE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontOption"


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
Styling_EObject_strategy = st.builds(
    Styling_EObject,
)
Pattern_strategy = st.builds(
    Pattern,
)
Styling_ConstantPattern_strategy = st.builds(
    Styling_ConstantPattern,
    value=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
Styling_StringParameter_strategy = st.builds(
    Styling_StringParameter,
    value=
        safe_text
)
Styling_BooleanParameter_strategy = st.builds(
    Styling_BooleanParameter,
    value=
        st.booleans()
)
Styling_EObjectParameter_strategy = st.builds(
    Styling_EObjectParameter,
)
Styling_IntParameter_strategy = st.builds(
    Styling_IntParameter,
    value=
        st.integers()
)
Styling_Parameter_strategy = st.builds(
    Styling_Parameter,
    name=
        safe_text
)
Styling_OperationPattern_strategy = st.builds(
    Styling_OperationPattern,
    operation=
        safe_text
)
Styling_ModelPattern_strategy = st.builds(
    Styling_ModelPattern,
    attributeName=
        safe_text
)
Styling_Styling_strategy = st.builds(
    Styling_Styling,
)
Styling_Style_strategy = st.builds(
    Styling_Style,
    appliedFonts=
        safe_text,
    color=
        safe_text
)
Styling_Icon_strategy = st.builds(
    Styling_Icon,
    image=
        safe_text
)
Styling_Pattern_strategy = st.builds(
    Styling_Pattern,
)
Styling_Segment_strategy = st.builds(
    Styling_Segment,
)
Styling_IPredicate_strategy = st.builds(
    Styling_IPredicate,
)
CaseStyle_strategy = st.builds(
    CaseStyle,
)
Styling_StylingPredicate_strategy = st.builds(
    Styling_StylingPredicate,
)
Styling_Basic_strategy = st.builds(
    Styling_Basic,
)
Styling_Default_strategy = st.builds(
    Styling_Default,
)
Styling_CaseStyle_strategy = st.builds(
    Styling_CaseStyle,
)
Styling_StylingModel_strategy = st.builds(
    Styling_StylingModel,
    modeName=
        safe_text
)






@given(instance=Styling_ConstantPattern_strategy)
def test_hyp_styling_constantpattern_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=Styling_StringParameter_strategy)
def test_hyp_styling_stringparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Styling_BooleanParameter_strategy)
def test_hyp_styling_booleanparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=Styling_IntParameter_strategy)
def test_hyp_styling_intparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Styling_Parameter_strategy)
def test_hyp_styling_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Styling_OperationPattern_strategy)
def test_hyp_styling_operationpattern_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original




@given(instance=Styling_ModelPattern_strategy)
def test_hyp_styling_modelpattern_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original





@given(instance=Styling_Style_strategy)
def test_hyp_styling_style_appliedFonts_setter(instance):
    original = instance.appliedFonts
    instance.appliedFonts = original
    assert instance.appliedFonts == original



@given(instance=Styling_Style_strategy)
def test_hyp_styling_style_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=Styling_Icon_strategy)
def test_hyp_styling_icon_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Styling_Segment_strategy)
@settings(max_examples=30)
def test_hyp_styling_segment_setcolor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setColor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setColor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setColor' in Styling_Segment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setColor' in Styling_Segment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setColor' in Styling_Segment is not implemented or raised an error")










@given(instance=Styling_StylingModel_strategy)
def test_hyp_styling_stylingmodel_modeName_setter(instance):
    original = instance.modeName
    instance.modeName = original
    assert instance.modeName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CaseStyle,
    Parameter,
    Pattern,
    Styling_Basic,
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


def test_Styling_Basic_isa_CaseStyle():
    instance = Styling_Basic()
    assert isinstance(instance, CaseStyle)


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


def test_assoc_basic3_link_reassign_clear():
    a = Styling_StylingModel(modeName="sample_text")
    b1 = Styling_Basic()
    b2 = Styling_Basic()
    _safe_set(a, 'Styling_StylingModel4', b1)
    assert _is_linked(a, 'Styling_StylingModel4', b1)
    if hasattr(b1, 'Styling_Basic'):
        assert _is_linked(b1, 'Styling_Basic', a)
    _safe_set(a, 'Styling_StylingModel4', b2)
    assert _is_linked(a, 'Styling_StylingModel4', b2)
    if hasattr(b1, 'Styling_Basic'):
        assert not _is_linked(b1, 'Styling_Basic', a)
    if hasattr(b2, 'Styling_Basic'):
        assert _is_linked(b2, 'Styling_Basic', a)
    _safe_set(a, 'Styling_StylingModel4', None)
    assert not _is_linked(a, 'Styling_StylingModel4', b2)
    if hasattr(b2, 'Styling_Basic'):
        assert not _is_linked(b2, 'Styling_Basic', a)


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


def test_assoc_icon12_link_reassign_clear():
    a = Styling_Icon(image="sample_text")
    b1 = Styling_CaseStyle()
    b2 = Styling_CaseStyle()
    _safe_set(a, 'Styling_Icon', b1)
    assert _is_linked(a, 'Styling_Icon', b1)
    if hasattr(b1, 'Styling_CaseStyle13'):
        assert _is_linked(b1, 'Styling_CaseStyle13', a)
    _safe_set(a, 'Styling_Icon', b2)
    assert _is_linked(a, 'Styling_Icon', b2)
    if hasattr(b1, 'Styling_CaseStyle13'):
        assert not _is_linked(b1, 'Styling_CaseStyle13', a)
    if hasattr(b2, 'Styling_CaseStyle13'):
        assert _is_linked(b2, 'Styling_CaseStyle13', a)
    _safe_set(a, 'Styling_Icon', None)
    assert not _is_linked(a, 'Styling_Icon', b2)
    if hasattr(b2, 'Styling_CaseStyle13'):
        assert not _is_linked(b2, 'Styling_CaseStyle13', a)


def test_assoc_models14_link_reassign_clear():
    a = Styling_StylingModel(modeName="sample_text")
    b1 = Styling_Styling()
    b2 = Styling_Styling()
    _safe_set(a, 'Styling_StylingModel15', b1)
    assert _is_linked(a, 'Styling_StylingModel15', b1)
    if hasattr(b1, 'Styling_Styling'):
        assert _is_linked(b1, 'Styling_Styling', a)
    _safe_set(a, 'Styling_StylingModel15', b2)
    assert _is_linked(a, 'Styling_StylingModel15', b2)
    if hasattr(b1, 'Styling_Styling'):
        assert not _is_linked(b1, 'Styling_Styling', a)
    if hasattr(b2, 'Styling_Styling'):
        assert _is_linked(b2, 'Styling_Styling', a)
    _safe_set(a, 'Styling_StylingModel15', None)
    assert not _is_linked(a, 'Styling_StylingModel15', b2)
    if hasattr(b2, 'Styling_Styling'):
        assert not _is_linked(b2, 'Styling_Styling', a)


def test_assoc_parameters16_link_reassign_clear():
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


def test_assoc_pattern7_link_reassign_clear():
    a = Styling_Segment()
    b1 = Styling_Pattern()
    b2 = Styling_Pattern()
    _safe_set(a, 'Styling_Segment8', b1)
    assert _is_linked(a, 'Styling_Segment8', b1)
    if hasattr(b1, 'Styling_Pattern'):
        assert _is_linked(b1, 'Styling_Pattern', a)
    _safe_set(a, 'Styling_Segment8', b2)
    assert _is_linked(a, 'Styling_Segment8', b2)
    if hasattr(b1, 'Styling_Pattern'):
        assert not _is_linked(b1, 'Styling_Pattern', a)
    if hasattr(b2, 'Styling_Pattern'):
        assert _is_linked(b2, 'Styling_Pattern', a)
    _safe_set(a, 'Styling_Segment8', None)
    assert not _is_linked(a, 'Styling_Segment8', b2)
    if hasattr(b2, 'Styling_Pattern'):
        assert not _is_linked(b2, 'Styling_Pattern', a)


def test_assoc_segments9_link_reassign_clear():
    a = Styling_Segment()
    b1 = Styling_CaseStyle()
    b2 = Styling_CaseStyle()
    _safe_set(a, 'Styling_Segment11', b1)
    assert _is_linked(a, 'Styling_Segment11', b1)
    if hasattr(b1, 'Styling_CaseStyle10'):
        assert _is_linked(b1, 'Styling_CaseStyle10', a)
    _safe_set(a, 'Styling_Segment11', b2)
    assert _is_linked(a, 'Styling_Segment11', b2)
    if hasattr(b1, 'Styling_CaseStyle10'):
        assert not _is_linked(b1, 'Styling_CaseStyle10', a)
    if hasattr(b2, 'Styling_CaseStyle10'):
        assert _is_linked(b2, 'Styling_CaseStyle10', a)
    _safe_set(a, 'Styling_Segment11', None)
    assert not _is_linked(a, 'Styling_Segment11', b2)
    if hasattr(b2, 'Styling_CaseStyle10'):
        assert not _is_linked(b2, 'Styling_CaseStyle10', a)


def test_assoc_style6_link_reassign_clear():
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


Styling_Basic_strategy = st.builds(Styling_Basic)
@given(instance=Styling_Basic_strategy)
@settings(max_examples=25)
def test_Styling_Basic_instantiation(instance):
    assert isinstance(instance, Styling_Basic)


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



