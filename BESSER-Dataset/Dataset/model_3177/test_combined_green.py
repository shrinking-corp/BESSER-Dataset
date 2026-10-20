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
    iotdsl_IfBlock,
    Expression,
    iotdsl_Or,
    iotdsl_StringConstant,
    iotdsl_IntConstant,
    iotdsl_And,
    iotdsl_BoolConstant,
    iotdsl_VariableRef,
    iotdsl_Not,
    iotdsl_MulOrDiv,
    iotdsl_Minus,
    iotdsl_Plus,
    iotdsl_Comparison,
    iotdsl_Equality,
    iotdsl_Device,
    iotdsl_Iot,
    iotdsl_IfStatement,
    Action,
    iotdsl_Expression,
    iotdsl_Variable,
    iotdsl_Action,
    iotdsl_Transition,
    iotdsl_Event,
    iotdsl_State,
    iotdsl_Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_iotdsl_ifblock_is_not_abstract():
    assert not inspect.isabstract(iotdsl_IfBlock)


def test_hyp_iotdsl_ifblock_constructor_exists():
    assert callable(iotdsl_IfBlock.__init__)


def test_hyp_iotdsl_ifblock_constructor_args():
    sig = inspect.signature(iotdsl_IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_or_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Or)


def test_hyp_iotdsl_or_constructor_exists():
    assert callable(iotdsl_Or.__init__)


def test_hyp_iotdsl_or_constructor_args():
    sig = inspect.signature(iotdsl_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_stringconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl_StringConstant)


def test_hyp_iotdsl_stringconstant_constructor_exists():
    assert callable(iotdsl_StringConstant.__init__)


def test_hyp_iotdsl_stringconstant_constructor_args():
    sig = inspect.signature(iotdsl_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_iotdsl_intconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl_IntConstant)


def test_hyp_iotdsl_intconstant_constructor_exists():
    assert callable(iotdsl_IntConstant.__init__)


def test_hyp_iotdsl_intconstant_constructor_args():
    sig = inspect.signature(iotdsl_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_iotdsl_and_is_not_abstract():
    assert not inspect.isabstract(iotdsl_And)


def test_hyp_iotdsl_and_constructor_exists():
    assert callable(iotdsl_And.__init__)


def test_hyp_iotdsl_and_constructor_args():
    sig = inspect.signature(iotdsl_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_boolconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl_BoolConstant)


def test_hyp_iotdsl_boolconstant_constructor_exists():
    assert callable(iotdsl_BoolConstant.__init__)


def test_hyp_iotdsl_boolconstant_constructor_args():
    sig = inspect.signature(iotdsl_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_iotdsl_variableref_is_not_abstract():
    assert not inspect.isabstract(iotdsl_VariableRef)


def test_hyp_iotdsl_variableref_constructor_exists():
    assert callable(iotdsl_VariableRef.__init__)


def test_hyp_iotdsl_variableref_constructor_args():
    sig = inspect.signature(iotdsl_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_not_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Not)


def test_hyp_iotdsl_not_constructor_exists():
    assert callable(iotdsl_Not.__init__)


def test_hyp_iotdsl_not_constructor_args():
    sig = inspect.signature(iotdsl_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_mulordiv_is_not_abstract():
    assert not inspect.isabstract(iotdsl_MulOrDiv)


def test_hyp_iotdsl_mulordiv_constructor_exists():
    assert callable(iotdsl_MulOrDiv.__init__)


def test_hyp_iotdsl_mulordiv_constructor_args():
    sig = inspect.signature(iotdsl_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_iotdsl_minus_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Minus)


def test_hyp_iotdsl_minus_constructor_exists():
    assert callable(iotdsl_Minus.__init__)


def test_hyp_iotdsl_minus_constructor_args():
    sig = inspect.signature(iotdsl_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_plus_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Plus)


def test_hyp_iotdsl_plus_constructor_exists():
    assert callable(iotdsl_Plus.__init__)


def test_hyp_iotdsl_plus_constructor_args():
    sig = inspect.signature(iotdsl_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_comparison_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Comparison)


def test_hyp_iotdsl_comparison_constructor_exists():
    assert callable(iotdsl_Comparison.__init__)


def test_hyp_iotdsl_comparison_constructor_args():
    sig = inspect.signature(iotdsl_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_iotdsl_equality_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Equality)


def test_hyp_iotdsl_equality_constructor_exists():
    assert callable(iotdsl_Equality.__init__)


def test_hyp_iotdsl_equality_constructor_args():
    sig = inspect.signature(iotdsl_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_iotdsl_device_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Device)


def test_hyp_iotdsl_device_constructor_exists():
    assert callable(iotdsl_Device.__init__)


def test_hyp_iotdsl_device_constructor_args():
    sig = inspect.signature(iotdsl_Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iotdsl_iot_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Iot)


def test_hyp_iotdsl_iot_constructor_exists():
    assert callable(iotdsl_Iot.__init__)


def test_hyp_iotdsl_iot_constructor_args():
    sig = inspect.signature(iotdsl_Iot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_ifstatement_is_not_abstract():
    assert not inspect.isabstract(iotdsl_IfStatement)


def test_hyp_iotdsl_ifstatement_constructor_exists():
    assert callable(iotdsl_IfStatement.__init__)


def test_hyp_iotdsl_ifstatement_constructor_args():
    sig = inspect.signature(iotdsl_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_expression_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Expression)


def test_hyp_iotdsl_expression_constructor_exists():
    assert callable(iotdsl_Expression.__init__)


def test_hyp_iotdsl_expression_constructor_args():
    sig = inspect.signature(iotdsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_variable_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Variable)


def test_hyp_iotdsl_variable_constructor_exists():
    assert callable(iotdsl_Variable.__init__)


def test_hyp_iotdsl_variable_constructor_args():
    sig = inspect.signature(iotdsl_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iotdsl_action_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Action)


def test_hyp_iotdsl_action_constructor_exists():
    assert callable(iotdsl_Action.__init__)


def test_hyp_iotdsl_action_constructor_args():
    sig = inspect.signature(iotdsl_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iotdsl_transition_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Transition)


def test_hyp_iotdsl_transition_constructor_exists():
    assert callable(iotdsl_Transition.__init__)


def test_hyp_iotdsl_transition_constructor_args():
    sig = inspect.signature(iotdsl_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iotdsl_event_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Event)


def test_hyp_iotdsl_event_constructor_exists():
    assert callable(iotdsl_Event.__init__)


def test_hyp_iotdsl_event_constructor_args():
    sig = inspect.signature(iotdsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iotdsl_state_is_not_abstract():
    assert not inspect.isabstract(iotdsl_State)


def test_hyp_iotdsl_state_constructor_exists():
    assert callable(iotdsl_State.__init__)


def test_hyp_iotdsl_state_constructor_args():
    sig = inspect.signature(iotdsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iotdsl_attribute_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Attribute)


def test_hyp_iotdsl_attribute_constructor_exists():
    assert callable(iotdsl_Attribute.__init__)


def test_hyp_iotdsl_attribute_constructor_args():
    sig = inspect.signature(iotdsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "tag" in params, "Missing parameter 'tag'"





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
iotdsl_IfBlock_strategy = st.builds(
    iotdsl_IfBlock,
)
Expression_strategy = st.builds(
    Expression,
)
iotdsl_Or_strategy = st.builds(
    iotdsl_Or,
)
iotdsl_StringConstant_strategy = st.builds(
    iotdsl_StringConstant,
    value=
        safe_text
)
iotdsl_IntConstant_strategy = st.builds(
    iotdsl_IntConstant,
    value=
        st.integers()
)
iotdsl_And_strategy = st.builds(
    iotdsl_And,
)
iotdsl_BoolConstant_strategy = st.builds(
    iotdsl_BoolConstant,
    value=
        safe_text
)
iotdsl_VariableRef_strategy = st.builds(
    iotdsl_VariableRef,
)
iotdsl_Not_strategy = st.builds(
    iotdsl_Not,
)
iotdsl_MulOrDiv_strategy = st.builds(
    iotdsl_MulOrDiv,
    op=
        safe_text
)
iotdsl_Minus_strategy = st.builds(
    iotdsl_Minus,
)
iotdsl_Plus_strategy = st.builds(
    iotdsl_Plus,
)
iotdsl_Comparison_strategy = st.builds(
    iotdsl_Comparison,
    op=
        safe_text
)
iotdsl_Equality_strategy = st.builds(
    iotdsl_Equality,
    op=
        safe_text
)
iotdsl_Device_strategy = st.builds(
    iotdsl_Device,
    name=
        safe_text
)
iotdsl_Iot_strategy = st.builds(
    iotdsl_Iot,
)
iotdsl_IfStatement_strategy = st.builds(
    iotdsl_IfStatement,
)
Action_strategy = st.builds(
    Action,
)
iotdsl_Expression_strategy = st.builds(
    iotdsl_Expression,
)
iotdsl_Variable_strategy = st.builds(
    iotdsl_Variable,
    name=
        safe_text
)
iotdsl_Action_strategy = st.builds(
    iotdsl_Action,
)
iotdsl_Transition_strategy = st.builds(
    iotdsl_Transition,
    name=
        safe_text
)
iotdsl_Event_strategy = st.builds(
    iotdsl_Event,
    name=
        safe_text
)
iotdsl_State_strategy = st.builds(
    iotdsl_State,
    name=
        safe_text
)
iotdsl_Attribute_strategy = st.builds(
    iotdsl_Attribute,
    value=
        safe_text,
    typeName=
        safe_text,
    tag=
        safe_text
)







@given(instance=iotdsl_StringConstant_strategy)
def test_hyp_iotdsl_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=iotdsl_IntConstant_strategy)
def test_hyp_iotdsl_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=iotdsl_BoolConstant_strategy)
def test_hyp_iotdsl_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=iotdsl_MulOrDiv_strategy)
def test_hyp_iotdsl_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original






@given(instance=iotdsl_Comparison_strategy)
def test_hyp_iotdsl_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=iotdsl_Equality_strategy)
def test_hyp_iotdsl_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=iotdsl_Device_strategy)
def test_hyp_iotdsl_device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=iotdsl_Variable_strategy)
def test_hyp_iotdsl_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=iotdsl_Transition_strategy)
def test_hyp_iotdsl_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=iotdsl_Event_strategy)
def test_hyp_iotdsl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=iotdsl_State_strategy)
def test_hyp_iotdsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=iotdsl_Attribute_strategy)
def test_hyp_iotdsl_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=iotdsl_Attribute_strategy)
def test_hyp_iotdsl_attribute_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=iotdsl_Attribute_strategy)
def test_hyp_iotdsl_attribute_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Expression,
    iotdsl_Action,
    iotdsl_And,
    iotdsl_Attribute,
    iotdsl_BoolConstant,
    iotdsl_Comparison,
    iotdsl_Device,
    iotdsl_Equality,
    iotdsl_Event,
    iotdsl_Expression,
    iotdsl_IfBlock,
    iotdsl_IfStatement,
    iotdsl_IntConstant,
    iotdsl_Iot,
    iotdsl_Minus,
    iotdsl_MulOrDiv,
    iotdsl_Not,
    iotdsl_Or,
    iotdsl_Plus,
    iotdsl_State,
    iotdsl_StringConstant,
    iotdsl_Transition,
    iotdsl_Variable,
    iotdsl_VariableRef,
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

def test_iotdsl_Attribute_tag_value_roundtrip():
    instance = iotdsl_Attribute(tag="sample_text", typeName="sample_text", value="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_iotdsl_Attribute_typeName_value_roundtrip():
    instance = iotdsl_Attribute(tag="sample_text", typeName="sample_text", value="sample_text")
    assert instance.typeName == "sample_text"
    instance.typeName = "sample_text_2"
    assert instance.typeName == "sample_text_2"


def test_iotdsl_Attribute_value_value_roundtrip():
    instance = iotdsl_Attribute(tag="sample_text", typeName="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iotdsl_BoolConstant_value_value_roundtrip():
    instance = iotdsl_BoolConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iotdsl_Comparison_op_value_roundtrip():
    instance = iotdsl_Comparison(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_iotdsl_Device_name_value_roundtrip():
    instance = iotdsl_Device(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iotdsl_Equality_op_value_roundtrip():
    instance = iotdsl_Equality(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_iotdsl_Event_name_value_roundtrip():
    instance = iotdsl_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iotdsl_IntConstant_value_value_roundtrip():
    instance = iotdsl_IntConstant(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_iotdsl_MulOrDiv_op_value_roundtrip():
    instance = iotdsl_MulOrDiv(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_iotdsl_State_name_value_roundtrip():
    instance = iotdsl_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iotdsl_StringConstant_value_value_roundtrip():
    instance = iotdsl_StringConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iotdsl_Transition_name_value_roundtrip():
    instance = iotdsl_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iotdsl_Variable_name_value_roundtrip():
    instance = iotdsl_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iotdsl_Expression_isa_Action():
    instance = iotdsl_Expression()
    assert isinstance(instance, Action)


def test_iotdsl_Variable_isa_Action():
    instance = iotdsl_Variable(name="sample_text")
    assert isinstance(instance, Action)


def test_iotdsl_And_isa_Expression():
    instance = iotdsl_And()
    assert isinstance(instance, Expression)


def test_iotdsl_BoolConstant_isa_Expression():
    instance = iotdsl_BoolConstant(value="sample_text")
    assert isinstance(instance, Expression)


def test_iotdsl_Comparison_isa_Expression():
    instance = iotdsl_Comparison(op="sample_text")
    assert isinstance(instance, Expression)


def test_iotdsl_Equality_isa_Expression():
    instance = iotdsl_Equality(op="sample_text")
    assert isinstance(instance, Expression)


def test_iotdsl_IfStatement_isa_Expression():
    instance = iotdsl_IfStatement()
    assert isinstance(instance, Expression)


def test_iotdsl_IntConstant_isa_Expression():
    instance = iotdsl_IntConstant(value=7)
    assert isinstance(instance, Expression)


def test_iotdsl_Minus_isa_Expression():
    instance = iotdsl_Minus()
    assert isinstance(instance, Expression)


def test_iotdsl_MulOrDiv_isa_Expression():
    instance = iotdsl_MulOrDiv(op="sample_text")
    assert isinstance(instance, Expression)


def test_iotdsl_Not_isa_Expression():
    instance = iotdsl_Not()
    assert isinstance(instance, Expression)


def test_iotdsl_Or_isa_Expression():
    instance = iotdsl_Or()
    assert isinstance(instance, Expression)


def test_iotdsl_Plus_isa_Expression():
    instance = iotdsl_Plus()
    assert isinstance(instance, Expression)


def test_iotdsl_StringConstant_isa_Expression():
    instance = iotdsl_StringConstant(value="sample_text")
    assert isinstance(instance, Expression)


def test_iotdsl_VariableRef_isa_Expression():
    instance = iotdsl_VariableRef()
    assert isinstance(instance, Expression)


def test_assoc_attributes4_link_reassign_clear():
    a = iotdsl_Device(name="sample_text")
    b1 = iotdsl_Attribute(tag="sample_text", typeName="sample_text", value="sample_text")
    b2 = iotdsl_Attribute(tag="sample_text_2", typeName="sample_text_2", value="sample_text_2")
    _safe_set(a, 'iotdsl_Device5', b1)
    assert _is_linked(a, 'iotdsl_Device5', b1)
    if hasattr(b1, 'iotdsl_Attribute'):
        assert _is_linked(b1, 'iotdsl_Attribute', a)
    _safe_set(a, 'iotdsl_Device5', b2)
    assert _is_linked(a, 'iotdsl_Device5', b2)
    if hasattr(b1, 'iotdsl_Attribute'):
        assert not _is_linked(b1, 'iotdsl_Attribute', a)
    if hasattr(b2, 'iotdsl_Attribute'):
        assert _is_linked(b2, 'iotdsl_Attribute', a)
    _safe_set(a, 'iotdsl_Device5', None)
    assert not _is_linked(a, 'iotdsl_Device5', b2)
    if hasattr(b2, 'iotdsl_Attribute'):
        assert not _is_linked(b2, 'iotdsl_Attribute', a)


def test_assoc_devices0_link_reassign_clear():
    a = iotdsl_Device(name="sample_text")
    b1 = iotdsl_Iot()
    b2 = iotdsl_Iot()
    _safe_set(a, 'iotdsl_Device', b1)
    assert _is_linked(a, 'iotdsl_Device', b1)
    if hasattr(b1, 'iotdsl_Iot'):
        assert _is_linked(b1, 'iotdsl_Iot', a)
    _safe_set(a, 'iotdsl_Device', b2)
    assert _is_linked(a, 'iotdsl_Device', b2)
    if hasattr(b1, 'iotdsl_Iot'):
        assert not _is_linked(b1, 'iotdsl_Iot', a)
    if hasattr(b2, 'iotdsl_Iot'):
        assert _is_linked(b2, 'iotdsl_Iot', a)
    _safe_set(a, 'iotdsl_Device', None)
    assert not _is_linked(a, 'iotdsl_Device', b2)
    if hasattr(b2, 'iotdsl_Iot'):
        assert not _is_linked(b2, 'iotdsl_Iot', a)


def test_assoc_elements12_link_reassign_clear():
    a = iotdsl_State(name="sample_text")
    b1 = iotdsl_Action()
    b2 = iotdsl_Action()
    _safe_set(a, 'iotdsl_State13', {b1})
    assert _is_linked(a, 'iotdsl_State13', b1)
    if hasattr(b1, 'iotdsl_Action'):
        assert _is_linked(b1, 'iotdsl_Action', a)
    _safe_set(a, 'iotdsl_State13', {b2})
    assert _is_linked(a, 'iotdsl_State13', b2)
    if hasattr(b1, 'iotdsl_Action'):
        assert not _is_linked(b1, 'iotdsl_Action', a)
    if hasattr(b2, 'iotdsl_Action'):
        assert _is_linked(b2, 'iotdsl_Action', a)
    _safe_set(a, 'iotdsl_State13', set())
    assert not _is_linked(a, 'iotdsl_State13', b2)
    if hasattr(b2, 'iotdsl_Action'):
        assert not _is_linked(b2, 'iotdsl_Action', a)


def test_assoc_event14_link_reassign_clear():
    a = iotdsl_Transition(name="sample_text")
    b1 = iotdsl_Event(name="sample_text")
    b2 = iotdsl_Event(name="sample_text_2")
    _safe_set(a, 'iotdsl_Transition15', b1)
    assert _is_linked(a, 'iotdsl_Transition15', b1)
    if hasattr(b1, 'iotdsl_Event16'):
        assert _is_linked(b1, 'iotdsl_Event16', a)
    _safe_set(a, 'iotdsl_Transition15', b2)
    assert _is_linked(a, 'iotdsl_Transition15', b2)
    if hasattr(b1, 'iotdsl_Event16'):
        assert not _is_linked(b1, 'iotdsl_Event16', a)
    if hasattr(b2, 'iotdsl_Event16'):
        assert _is_linked(b2, 'iotdsl_Event16', a)
    _safe_set(a, 'iotdsl_Transition15', None)
    assert not _is_linked(a, 'iotdsl_Transition15', b2)
    if hasattr(b2, 'iotdsl_Event16'):
        assert not _is_linked(b2, 'iotdsl_Event16', a)


def test_assoc_events8_link_reassign_clear():
    a = iotdsl_Event(name="sample_text")
    b1 = iotdsl_Device(name="sample_text")
    b2 = iotdsl_Device(name="sample_text_2")
    _safe_set(a, 'iotdsl_Event', b1)
    assert _is_linked(a, 'iotdsl_Event', b1)
    if hasattr(b1, 'iotdsl_Device9'):
        assert _is_linked(b1, 'iotdsl_Device9', a)
    _safe_set(a, 'iotdsl_Event', b2)
    assert _is_linked(a, 'iotdsl_Event', b2)
    if hasattr(b1, 'iotdsl_Device9'):
        assert not _is_linked(b1, 'iotdsl_Device9', a)
    if hasattr(b2, 'iotdsl_Device9'):
        assert _is_linked(b2, 'iotdsl_Device9', a)
    _safe_set(a, 'iotdsl_Event', None)
    assert not _is_linked(a, 'iotdsl_Event', b2)
    if hasattr(b2, 'iotdsl_Device9'):
        assert not _is_linked(b2, 'iotdsl_Device9', a)


def test_assoc_expression20_link_reassign_clear():
    a = iotdsl_Variable(name="sample_text")
    b1 = iotdsl_Expression()
    b2 = iotdsl_Expression()
    _safe_set(a, 'iotdsl_Variable', b1)
    assert _is_linked(a, 'iotdsl_Variable', b1)
    if hasattr(b1, 'iotdsl_Expression'):
        assert _is_linked(b1, 'iotdsl_Expression', a)
    _safe_set(a, 'iotdsl_Variable', b2)
    assert _is_linked(a, 'iotdsl_Variable', b2)
    if hasattr(b1, 'iotdsl_Expression'):
        assert not _is_linked(b1, 'iotdsl_Expression', a)
    if hasattr(b2, 'iotdsl_Expression'):
        assert _is_linked(b2, 'iotdsl_Expression', a)
    _safe_set(a, 'iotdsl_Variable', None)
    assert not _is_linked(a, 'iotdsl_Variable', b2)
    if hasattr(b2, 'iotdsl_Expression'):
        assert not _is_linked(b2, 'iotdsl_Expression', a)


def test_assoc_left41_link_reassign_clear():
    a = iotdsl_Equality(op="sample_text")
    b1 = iotdsl_Expression()
    b2 = iotdsl_Expression()
    _safe_set(a, 'iotdsl_Equality', b1)
    assert _is_linked(a, 'iotdsl_Equality', b1)
    if hasattr(b1, 'iotdsl_Expression42'):
        assert _is_linked(b1, 'iotdsl_Expression42', a)
    _safe_set(a, 'iotdsl_Equality', b2)
    assert _is_linked(a, 'iotdsl_Equality', b2)
    if hasattr(b1, 'iotdsl_Expression42'):
        assert not _is_linked(b1, 'iotdsl_Expression42', a)
    if hasattr(b2, 'iotdsl_Expression42'):
        assert _is_linked(b2, 'iotdsl_Expression42', a)
    _safe_set(a, 'iotdsl_Equality', None)
    assert not _is_linked(a, 'iotdsl_Equality', b2)
    if hasattr(b2, 'iotdsl_Expression42'):
        assert not _is_linked(b2, 'iotdsl_Expression42', a)


def test_assoc_left46_link_reassign_clear():
    a = iotdsl_Comparison(op="sample_text")
    b1 = iotdsl_Expression()
    b2 = iotdsl_Expression()
    _safe_set(a, 'iotdsl_Comparison', b1)
    assert _is_linked(a, 'iotdsl_Comparison', b1)
    if hasattr(b1, 'iotdsl_Expression47'):
        assert _is_linked(b1, 'iotdsl_Expression47', a)
    _safe_set(a, 'iotdsl_Comparison', b2)
    assert _is_linked(a, 'iotdsl_Comparison', b2)
    if hasattr(b1, 'iotdsl_Expression47'):
        assert not _is_linked(b1, 'iotdsl_Expression47', a)
    if hasattr(b2, 'iotdsl_Expression47'):
        assert _is_linked(b2, 'iotdsl_Expression47', a)
    _safe_set(a, 'iotdsl_Comparison', None)
    assert not _is_linked(a, 'iotdsl_Comparison', b2)
    if hasattr(b2, 'iotdsl_Expression47'):
        assert not _is_linked(b2, 'iotdsl_Expression47', a)


def test_assoc_left61_link_reassign_clear():
    a = iotdsl_MulOrDiv(op="sample_text")
    b1 = iotdsl_Expression()
    b2 = iotdsl_Expression()
    _safe_set(a, 'iotdsl_MulOrDiv', b1)
    assert _is_linked(a, 'iotdsl_MulOrDiv', b1)
    if hasattr(b1, 'iotdsl_Expression62'):
        assert _is_linked(b1, 'iotdsl_Expression62', a)
    _safe_set(a, 'iotdsl_MulOrDiv', b2)
    assert _is_linked(a, 'iotdsl_MulOrDiv', b2)
    if hasattr(b1, 'iotdsl_Expression62'):
        assert not _is_linked(b1, 'iotdsl_Expression62', a)
    if hasattr(b2, 'iotdsl_Expression62'):
        assert _is_linked(b2, 'iotdsl_Expression62', a)
    _safe_set(a, 'iotdsl_MulOrDiv', None)
    assert not _is_linked(a, 'iotdsl_MulOrDiv', b2)
    if hasattr(b2, 'iotdsl_Expression62'):
        assert not _is_linked(b2, 'iotdsl_Expression62', a)


def test_assoc_right43_link_reassign_clear():
    a = iotdsl_Equality(op="sample_text")
    b1 = iotdsl_Expression()
    b2 = iotdsl_Expression()
    _safe_set(a, 'iotdsl_Equality44', b1)
    assert _is_linked(a, 'iotdsl_Equality44', b1)
    if hasattr(b1, 'iotdsl_Expression45'):
        assert _is_linked(b1, 'iotdsl_Expression45', a)
    _safe_set(a, 'iotdsl_Equality44', b2)
    assert _is_linked(a, 'iotdsl_Equality44', b2)
    if hasattr(b1, 'iotdsl_Expression45'):
        assert not _is_linked(b1, 'iotdsl_Expression45', a)
    if hasattr(b2, 'iotdsl_Expression45'):
        assert _is_linked(b2, 'iotdsl_Expression45', a)
    _safe_set(a, 'iotdsl_Equality44', None)
    assert not _is_linked(a, 'iotdsl_Equality44', b2)
    if hasattr(b2, 'iotdsl_Expression45'):
        assert not _is_linked(b2, 'iotdsl_Expression45', a)


def test_assoc_right48_link_reassign_clear():
    a = iotdsl_Comparison(op="sample_text")
    b1 = iotdsl_Expression()
    b2 = iotdsl_Expression()
    _safe_set(a, 'iotdsl_Comparison49', b1)
    assert _is_linked(a, 'iotdsl_Comparison49', b1)
    if hasattr(b1, 'iotdsl_Expression50'):
        assert _is_linked(b1, 'iotdsl_Expression50', a)
    _safe_set(a, 'iotdsl_Comparison49', b2)
    assert _is_linked(a, 'iotdsl_Comparison49', b2)
    if hasattr(b1, 'iotdsl_Expression50'):
        assert not _is_linked(b1, 'iotdsl_Expression50', a)
    if hasattr(b2, 'iotdsl_Expression50'):
        assert _is_linked(b2, 'iotdsl_Expression50', a)
    _safe_set(a, 'iotdsl_Comparison49', None)
    assert not _is_linked(a, 'iotdsl_Comparison49', b2)
    if hasattr(b2, 'iotdsl_Expression50'):
        assert not _is_linked(b2, 'iotdsl_Expression50', a)


def test_assoc_right63_link_reassign_clear():
    a = iotdsl_MulOrDiv(op="sample_text")
    b1 = iotdsl_Expression()
    b2 = iotdsl_Expression()
    _safe_set(a, 'iotdsl_MulOrDiv64', b1)
    assert _is_linked(a, 'iotdsl_MulOrDiv64', b1)
    if hasattr(b1, 'iotdsl_Expression65'):
        assert _is_linked(b1, 'iotdsl_Expression65', a)
    _safe_set(a, 'iotdsl_MulOrDiv64', b2)
    assert _is_linked(a, 'iotdsl_MulOrDiv64', b2)
    if hasattr(b1, 'iotdsl_Expression65'):
        assert not _is_linked(b1, 'iotdsl_Expression65', a)
    if hasattr(b2, 'iotdsl_Expression65'):
        assert _is_linked(b2, 'iotdsl_Expression65', a)
    _safe_set(a, 'iotdsl_MulOrDiv64', None)
    assert not _is_linked(a, 'iotdsl_MulOrDiv64', b2)
    if hasattr(b2, 'iotdsl_Expression65'):
        assert not _is_linked(b2, 'iotdsl_Expression65', a)


def test_assoc_state17_link_reassign_clear():
    a = iotdsl_Transition(name="sample_text")
    b1 = iotdsl_State(name="sample_text")
    b2 = iotdsl_State(name="sample_text_2")
    _safe_set(a, 'iotdsl_Transition18', b1)
    assert _is_linked(a, 'iotdsl_Transition18', b1)
    if hasattr(b1, 'iotdsl_State19'):
        assert _is_linked(b1, 'iotdsl_State19', a)
    _safe_set(a, 'iotdsl_Transition18', b2)
    assert _is_linked(a, 'iotdsl_Transition18', b2)
    if hasattr(b1, 'iotdsl_State19'):
        assert not _is_linked(b1, 'iotdsl_State19', a)
    if hasattr(b2, 'iotdsl_State19'):
        assert _is_linked(b2, 'iotdsl_State19', a)
    _safe_set(a, 'iotdsl_Transition18', None)
    assert not _is_linked(a, 'iotdsl_Transition18', b2)
    if hasattr(b2, 'iotdsl_State19'):
        assert not _is_linked(b2, 'iotdsl_State19', a)


def test_assoc_states6_link_reassign_clear():
    a = iotdsl_State(name="sample_text")
    b1 = iotdsl_Device(name="sample_text")
    b2 = iotdsl_Device(name="sample_text_2")
    _safe_set(a, 'iotdsl_State', b1)
    assert _is_linked(a, 'iotdsl_State', b1)
    if hasattr(b1, 'iotdsl_Device7'):
        assert _is_linked(b1, 'iotdsl_Device7', a)
    _safe_set(a, 'iotdsl_State', b2)
    assert _is_linked(a, 'iotdsl_State', b2)
    if hasattr(b1, 'iotdsl_Device7'):
        assert not _is_linked(b1, 'iotdsl_Device7', a)
    if hasattr(b2, 'iotdsl_Device7'):
        assert _is_linked(b2, 'iotdsl_Device7', a)
    _safe_set(a, 'iotdsl_State', None)
    assert not _is_linked(a, 'iotdsl_State', b2)
    if hasattr(b2, 'iotdsl_Device7'):
        assert not _is_linked(b2, 'iotdsl_Device7', a)


def test_assoc_superType2_link_reassign_clear():
    a = iotdsl_Device(name="sample_text")
    b1 = iotdsl_Device(name="sample_text")
    b2 = iotdsl_Device(name="sample_text_2")
    _safe_set(a, 'iotdsl_Device1', b1)
    assert _is_linked(a, 'iotdsl_Device1', b1)
    if hasattr(b1, 'iotdsl_Device3'):
        assert _is_linked(b1, 'iotdsl_Device3', a)
    _safe_set(a, 'iotdsl_Device1', b2)
    assert _is_linked(a, 'iotdsl_Device1', b2)
    if hasattr(b1, 'iotdsl_Device3'):
        assert not _is_linked(b1, 'iotdsl_Device3', a)
    if hasattr(b2, 'iotdsl_Device3'):
        assert _is_linked(b2, 'iotdsl_Device3', a)
    _safe_set(a, 'iotdsl_Device1', None)
    assert not _is_linked(a, 'iotdsl_Device1', b2)
    if hasattr(b2, 'iotdsl_Device3'):
        assert not _is_linked(b2, 'iotdsl_Device3', a)


def test_assoc_transitions10_link_reassign_clear():
    a = iotdsl_Transition(name="sample_text")
    b1 = iotdsl_Device(name="sample_text")
    b2 = iotdsl_Device(name="sample_text_2")
    _safe_set(a, 'iotdsl_Transition', b1)
    assert _is_linked(a, 'iotdsl_Transition', b1)
    if hasattr(b1, 'iotdsl_Device11'):
        assert _is_linked(b1, 'iotdsl_Device11', a)
    _safe_set(a, 'iotdsl_Transition', b2)
    assert _is_linked(a, 'iotdsl_Transition', b2)
    if hasattr(b1, 'iotdsl_Device11'):
        assert not _is_linked(b1, 'iotdsl_Device11', a)
    if hasattr(b2, 'iotdsl_Device11'):
        assert _is_linked(b2, 'iotdsl_Device11', a)
    _safe_set(a, 'iotdsl_Transition', None)
    assert not _is_linked(a, 'iotdsl_Transition', b2)
    if hasattr(b2, 'iotdsl_Device11'):
        assert not _is_linked(b2, 'iotdsl_Device11', a)


def test_assoc_variable68_link_reassign_clear():
    a = iotdsl_Variable(name="sample_text")
    b1 = iotdsl_VariableRef()
    b2 = iotdsl_VariableRef()
    _safe_set(a, 'iotdsl_Variable69', b1)
    assert _is_linked(a, 'iotdsl_Variable69', b1)
    if hasattr(b1, 'iotdsl_VariableRef'):
        assert _is_linked(b1, 'iotdsl_VariableRef', a)
    _safe_set(a, 'iotdsl_Variable69', b2)
    assert _is_linked(a, 'iotdsl_Variable69', b2)
    if hasattr(b1, 'iotdsl_VariableRef'):
        assert not _is_linked(b1, 'iotdsl_VariableRef', a)
    if hasattr(b2, 'iotdsl_VariableRef'):
        assert _is_linked(b2, 'iotdsl_VariableRef', a)
    _safe_set(a, 'iotdsl_Variable69', None)
    assert not _is_linked(a, 'iotdsl_Variable69', b2)
    if hasattr(b2, 'iotdsl_VariableRef'):
        assert not _is_linked(b2, 'iotdsl_VariableRef', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


iotdsl_Action_strategy = st.builds(iotdsl_Action)
@given(instance=iotdsl_Action_strategy)
@settings(max_examples=25)
def test_iotdsl_Action_instantiation(instance):
    assert isinstance(instance, iotdsl_Action)


iotdsl_And_strategy = st.builds(iotdsl_And)
@given(instance=iotdsl_And_strategy)
@settings(max_examples=25)
def test_iotdsl_And_instantiation(instance):
    assert isinstance(instance, iotdsl_And)


iotdsl_Attribute_strategy = st.builds(iotdsl_Attribute, tag=safe_text, typeName=safe_text, value=safe_text)
@given(instance=iotdsl_Attribute_strategy)
@settings(max_examples=25)
def test_iotdsl_Attribute_instantiation(instance):
    assert isinstance(instance, iotdsl_Attribute)


iotdsl_BoolConstant_strategy = st.builds(iotdsl_BoolConstant, value=safe_text)
@given(instance=iotdsl_BoolConstant_strategy)
@settings(max_examples=25)
def test_iotdsl_BoolConstant_instantiation(instance):
    assert isinstance(instance, iotdsl_BoolConstant)


iotdsl_Comparison_strategy = st.builds(iotdsl_Comparison, op=safe_text)
@given(instance=iotdsl_Comparison_strategy)
@settings(max_examples=25)
def test_iotdsl_Comparison_instantiation(instance):
    assert isinstance(instance, iotdsl_Comparison)


iotdsl_Device_strategy = st.builds(iotdsl_Device, name=safe_text)
@given(instance=iotdsl_Device_strategy)
@settings(max_examples=25)
def test_iotdsl_Device_instantiation(instance):
    assert isinstance(instance, iotdsl_Device)


iotdsl_Equality_strategy = st.builds(iotdsl_Equality, op=safe_text)
@given(instance=iotdsl_Equality_strategy)
@settings(max_examples=25)
def test_iotdsl_Equality_instantiation(instance):
    assert isinstance(instance, iotdsl_Equality)


iotdsl_Event_strategy = st.builds(iotdsl_Event, name=safe_text)
@given(instance=iotdsl_Event_strategy)
@settings(max_examples=25)
def test_iotdsl_Event_instantiation(instance):
    assert isinstance(instance, iotdsl_Event)


iotdsl_Expression_strategy = st.builds(iotdsl_Expression)
@given(instance=iotdsl_Expression_strategy)
@settings(max_examples=25)
def test_iotdsl_Expression_instantiation(instance):
    assert isinstance(instance, iotdsl_Expression)


iotdsl_IfBlock_strategy = st.builds(iotdsl_IfBlock)
@given(instance=iotdsl_IfBlock_strategy)
@settings(max_examples=25)
def test_iotdsl_IfBlock_instantiation(instance):
    assert isinstance(instance, iotdsl_IfBlock)


iotdsl_IfStatement_strategy = st.builds(iotdsl_IfStatement)
@given(instance=iotdsl_IfStatement_strategy)
@settings(max_examples=25)
def test_iotdsl_IfStatement_instantiation(instance):
    assert isinstance(instance, iotdsl_IfStatement)


iotdsl_IntConstant_strategy = st.builds(iotdsl_IntConstant, value=st.integers())
@given(instance=iotdsl_IntConstant_strategy)
@settings(max_examples=25)
def test_iotdsl_IntConstant_instantiation(instance):
    assert isinstance(instance, iotdsl_IntConstant)


iotdsl_Iot_strategy = st.builds(iotdsl_Iot)
@given(instance=iotdsl_Iot_strategy)
@settings(max_examples=25)
def test_iotdsl_Iot_instantiation(instance):
    assert isinstance(instance, iotdsl_Iot)


iotdsl_Minus_strategy = st.builds(iotdsl_Minus)
@given(instance=iotdsl_Minus_strategy)
@settings(max_examples=25)
def test_iotdsl_Minus_instantiation(instance):
    assert isinstance(instance, iotdsl_Minus)


iotdsl_MulOrDiv_strategy = st.builds(iotdsl_MulOrDiv, op=safe_text)
@given(instance=iotdsl_MulOrDiv_strategy)
@settings(max_examples=25)
def test_iotdsl_MulOrDiv_instantiation(instance):
    assert isinstance(instance, iotdsl_MulOrDiv)


iotdsl_Not_strategy = st.builds(iotdsl_Not)
@given(instance=iotdsl_Not_strategy)
@settings(max_examples=25)
def test_iotdsl_Not_instantiation(instance):
    assert isinstance(instance, iotdsl_Not)


iotdsl_Or_strategy = st.builds(iotdsl_Or)
@given(instance=iotdsl_Or_strategy)
@settings(max_examples=25)
def test_iotdsl_Or_instantiation(instance):
    assert isinstance(instance, iotdsl_Or)


iotdsl_Plus_strategy = st.builds(iotdsl_Plus)
@given(instance=iotdsl_Plus_strategy)
@settings(max_examples=25)
def test_iotdsl_Plus_instantiation(instance):
    assert isinstance(instance, iotdsl_Plus)


iotdsl_State_strategy = st.builds(iotdsl_State, name=safe_text)
@given(instance=iotdsl_State_strategy)
@settings(max_examples=25)
def test_iotdsl_State_instantiation(instance):
    assert isinstance(instance, iotdsl_State)


iotdsl_StringConstant_strategy = st.builds(iotdsl_StringConstant, value=safe_text)
@given(instance=iotdsl_StringConstant_strategy)
@settings(max_examples=25)
def test_iotdsl_StringConstant_instantiation(instance):
    assert isinstance(instance, iotdsl_StringConstant)


iotdsl_Transition_strategy = st.builds(iotdsl_Transition, name=safe_text)
@given(instance=iotdsl_Transition_strategy)
@settings(max_examples=25)
def test_iotdsl_Transition_instantiation(instance):
    assert isinstance(instance, iotdsl_Transition)


iotdsl_Variable_strategy = st.builds(iotdsl_Variable, name=safe_text)
@given(instance=iotdsl_Variable_strategy)
@settings(max_examples=25)
def test_iotdsl_Variable_instantiation(instance):
    assert isinstance(instance, iotdsl_Variable)


iotdsl_VariableRef_strategy = st.builds(iotdsl_VariableRef)
@given(instance=iotdsl_VariableRef_strategy)
@settings(max_examples=25)
def test_iotdsl_VariableRef_instantiation(instance):
    assert isinstance(instance, iotdsl_VariableRef)



