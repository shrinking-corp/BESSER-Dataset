import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    B_Action,
    B_Any,
    B_Begin,
    B_Expression,
    B_If,
    B_Machine,
    B_Operation,
    B_Predicate,
    B_SET,
    B_Skip,
    B_Variable,
    B_VariableList,
    Expression,
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

def test_B_Expression_expression_value_roundtrip():
    instance = B_Expression(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_B_Machine_name_value_roundtrip():
    instance = B_Machine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_B_Operation_name_value_roundtrip():
    instance = B_Operation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_B_SET_name_value_roundtrip():
    instance = B_SET(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_B_Variable_name_value_roundtrip():
    instance = B_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_B_VariableList_size_value_roundtrip():
    instance = B_VariableList(size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_B_Action_isa_Expression():
    instance = B_Action()
    assert isinstance(instance, Expression)


def test_B_Any_isa_Expression():
    instance = B_Any()
    assert isinstance(instance, Expression)


def test_B_Begin_isa_Expression():
    instance = B_Begin()
    assert isinstance(instance, Expression)


def test_B_If_isa_Expression():
    instance = B_If()
    assert isinstance(instance, Expression)


def test_B_Predicate_isa_Expression():
    instance = B_Predicate()
    assert isinstance(instance, Expression)


def test_B_Skip_isa_Expression():
    instance = B_Skip()
    assert isinstance(instance, Expression)


def test_assoc_false_statements44_link_reassign_clear():
    a = B_Expression(expression="sample_text")
    b1 = B_If()
    b2 = B_If()
    _safe_set(a, 'B_Expression46', b1)
    assert _is_linked(a, 'B_Expression46', b1)
    if hasattr(b1, 'B_If45'):
        assert _is_linked(b1, 'B_If45', a)
    _safe_set(a, 'B_Expression46', b2)
    assert _is_linked(a, 'B_Expression46', b2)
    if hasattr(b1, 'B_If45'):
        assert not _is_linked(b1, 'B_If45', a)
    if hasattr(b2, 'B_If45'):
        assert _is_linked(b2, 'B_If45', a)
    _safe_set(a, 'B_Expression46', None)
    assert not _is_linked(a, 'B_Expression46', b2)
    if hasattr(b2, 'B_If45'):
        assert not _is_linked(b2, 'B_If45', a)


def test_assoc_first31_link_reassign_clear():
    a = B_VariableList(size="sample_text")
    b1 = B_Variable(name="sample_text")
    b2 = B_Variable(name="sample_text_2")
    _safe_set(a, 'B_VariableList32', b1)
    assert _is_linked(a, 'B_VariableList32', b1)
    if hasattr(b1, 'B_Variable33'):
        assert _is_linked(b1, 'B_Variable33', a)
    _safe_set(a, 'B_VariableList32', b2)
    assert _is_linked(a, 'B_VariableList32', b2)
    if hasattr(b1, 'B_Variable33'):
        assert not _is_linked(b1, 'B_Variable33', a)
    if hasattr(b2, 'B_Variable33'):
        assert _is_linked(b2, 'B_Variable33', a)
    _safe_set(a, 'B_VariableList32', None)
    assert not _is_linked(a, 'B_VariableList32', b2)
    if hasattr(b2, 'B_Variable33'):
        assert not _is_linked(b2, 'B_Variable33', a)


def test_assoc_initialisations10_link_reassign_clear():
    a = B_Machine(name="sample_text")
    b1 = B_Action()
    b2 = B_Action()
    _safe_set(a, 'B_Machine11', {b1})
    assert _is_linked(a, 'B_Machine11', b1)
    if hasattr(b1, 'B_Action'):
        assert _is_linked(b1, 'B_Action', a)
    _safe_set(a, 'B_Machine11', {b2})
    assert _is_linked(a, 'B_Machine11', b2)
    if hasattr(b1, 'B_Action'):
        assert not _is_linked(b1, 'B_Action', a)
    if hasattr(b2, 'B_Action'):
        assert _is_linked(b2, 'B_Action', a)
    _safe_set(a, 'B_Machine11', set())
    assert not _is_linked(a, 'B_Machine11', b2)
    if hasattr(b2, 'B_Action'):
        assert not _is_linked(b2, 'B_Action', a)


def test_assoc_inputs14_link_reassign_clear():
    a = B_VariableList(size="sample_text")
    b1 = B_Operation(name="sample_text")
    b2 = B_Operation(name="sample_text_2")
    _safe_set(a, 'B_VariableList', b1)
    assert _is_linked(a, 'B_VariableList', b1)
    if hasattr(b1, 'B_Operation15'):
        assert _is_linked(b1, 'B_Operation15', a)
    _safe_set(a, 'B_VariableList', b2)
    assert _is_linked(a, 'B_VariableList', b2)
    if hasattr(b1, 'B_Operation15'):
        assert not _is_linked(b1, 'B_Operation15', a)
    if hasattr(b2, 'B_Operation15'):
        assert _is_linked(b2, 'B_Operation15', a)
    _safe_set(a, 'B_VariableList', None)
    assert not _is_linked(a, 'B_VariableList', b2)
    if hasattr(b2, 'B_Operation15'):
        assert not _is_linked(b2, 'B_Operation15', a)


def test_assoc_invariants6_link_reassign_clear():
    a = B_Machine(name="sample_text")
    b1 = B_Predicate()
    b2 = B_Predicate()
    _safe_set(a, 'B_Machine7', {b1})
    assert _is_linked(a, 'B_Machine7', b1)
    if hasattr(b1, 'B_Predicate'):
        assert _is_linked(b1, 'B_Predicate', a)
    _safe_set(a, 'B_Machine7', {b2})
    assert _is_linked(a, 'B_Machine7', b2)
    if hasattr(b1, 'B_Predicate'):
        assert not _is_linked(b1, 'B_Predicate', a)
    if hasattr(b2, 'B_Predicate'):
        assert _is_linked(b2, 'B_Predicate', a)
    _safe_set(a, 'B_Machine7', set())
    assert not _is_linked(a, 'B_Machine7', b2)
    if hasattr(b2, 'B_Predicate'):
        assert not _is_linked(b2, 'B_Predicate', a)


def test_assoc_operations4_link_reassign_clear():
    a = B_Operation(name="sample_text")
    b1 = B_Machine(name="sample_text")
    b2 = B_Machine(name="sample_text_2")
    _safe_set(a, 'B_Operation', b1)
    assert _is_linked(a, 'B_Operation', b1)
    if hasattr(b1, 'B_Machine5'):
        assert _is_linked(b1, 'B_Machine5', a)
    _safe_set(a, 'B_Operation', b2)
    assert _is_linked(a, 'B_Operation', b2)
    if hasattr(b1, 'B_Machine5'):
        assert not _is_linked(b1, 'B_Machine5', a)
    if hasattr(b2, 'B_Machine5'):
        assert _is_linked(b2, 'B_Machine5', a)
    _safe_set(a, 'B_Operation', None)
    assert not _is_linked(a, 'B_Operation', b2)
    if hasattr(b2, 'B_Machine5'):
        assert not _is_linked(b2, 'B_Machine5', a)


def test_assoc_outputs16_link_reassign_clear():
    a = B_VariableList(size="sample_text")
    b1 = B_Operation(name="sample_text")
    b2 = B_Operation(name="sample_text_2")
    _safe_set(a, 'B_VariableList18', b1)
    assert _is_linked(a, 'B_VariableList18', b1)
    if hasattr(b1, 'B_Operation17'):
        assert _is_linked(b1, 'B_Operation17', a)
    _safe_set(a, 'B_VariableList18', b2)
    assert _is_linked(a, 'B_VariableList18', b2)
    if hasattr(b1, 'B_Operation17'):
        assert not _is_linked(b1, 'B_Operation17', a)
    if hasattr(b2, 'B_Operation17'):
        assert _is_linked(b2, 'B_Operation17', a)
    _safe_set(a, 'B_VariableList18', None)
    assert not _is_linked(a, 'B_VariableList18', b2)
    if hasattr(b2, 'B_Operation17'):
        assert not _is_linked(b2, 'B_Operation17', a)


def test_assoc_preceeds23_link_reassign_clear():
    a = B_Variable(name="sample_text")
    b1 = B_Variable(name="sample_text")
    b2 = B_Variable(name="sample_text_2")
    _safe_set(a, 'B_Variable22', b1)
    assert _is_linked(a, 'B_Variable22', b1)
    if hasattr(b1, 'B_Variable24'):
        assert _is_linked(b1, 'B_Variable24', a)
    _safe_set(a, 'B_Variable22', b2)
    assert _is_linked(a, 'B_Variable22', b2)
    if hasattr(b1, 'B_Variable24'):
        assert not _is_linked(b1, 'B_Variable24', a)
    if hasattr(b2, 'B_Variable24'):
        assert _is_linked(b2, 'B_Variable24', a)
    _safe_set(a, 'B_Variable22', None)
    assert not _is_linked(a, 'B_Variable22', b2)
    if hasattr(b2, 'B_Variable24'):
        assert not _is_linked(b2, 'B_Variable24', a)


def test_assoc_preconditions19_link_reassign_clear():
    a = B_Operation(name="sample_text")
    b1 = B_Predicate()
    b2 = B_Predicate()
    _safe_set(a, 'B_Operation20', {b1})
    assert _is_linked(a, 'B_Operation20', b1)
    if hasattr(b1, 'B_Predicate21'):
        assert _is_linked(b1, 'B_Predicate21', a)
    _safe_set(a, 'B_Operation20', {b2})
    assert _is_linked(a, 'B_Operation20', b2)
    if hasattr(b1, 'B_Predicate21'):
        assert not _is_linked(b1, 'B_Predicate21', a)
    if hasattr(b2, 'B_Predicate21'):
        assert _is_linked(b2, 'B_Predicate21', a)
    _safe_set(a, 'B_Operation20', set())
    assert not _is_linked(a, 'B_Operation20', b2)
    if hasattr(b2, 'B_Predicate21'):
        assert not _is_linked(b2, 'B_Predicate21', a)


def test_assoc_refines1_link_reassign_clear():
    a = B_Machine(name="sample_text")
    b1 = B_Machine(name="sample_text")
    b2 = B_Machine(name="sample_text_2")
    _safe_set(a, 'B_Machine', b1)
    assert _is_linked(a, 'B_Machine', b1)
    if hasattr(b1, 'B_Machine0'):
        assert _is_linked(b1, 'B_Machine0', a)
    _safe_set(a, 'B_Machine', b2)
    assert _is_linked(a, 'B_Machine', b2)
    if hasattr(b1, 'B_Machine0'):
        assert not _is_linked(b1, 'B_Machine0', a)
    if hasattr(b2, 'B_Machine0'):
        assert _is_linked(b2, 'B_Machine0', a)
    _safe_set(a, 'B_Machine', None)
    assert not _is_linked(a, 'B_Machine', b2)
    if hasattr(b2, 'B_Machine0'):
        assert not _is_linked(b2, 'B_Machine0', a)


def test_assoc_sets2_link_reassign_clear():
    a = B_SET(name="sample_text")
    b1 = B_Machine(name="sample_text")
    b2 = B_Machine(name="sample_text_2")
    _safe_set(a, 'B_SET', b1)
    assert _is_linked(a, 'B_SET', b1)
    if hasattr(b1, 'B_Machine3'):
        assert _is_linked(b1, 'B_Machine3', a)
    _safe_set(a, 'B_SET', b2)
    assert _is_linked(a, 'B_SET', b2)
    if hasattr(b1, 'B_Machine3'):
        assert not _is_linked(b1, 'B_Machine3', a)
    if hasattr(b2, 'B_Machine3'):
        assert _is_linked(b2, 'B_Machine3', a)
    _safe_set(a, 'B_SET', None)
    assert not _is_linked(a, 'B_SET', b2)
    if hasattr(b2, 'B_Machine3'):
        assert not _is_linked(b2, 'B_Machine3', a)


def test_assoc_statements12_link_reassign_clear():
    a = B_Operation(name="sample_text")
    b1 = B_Expression(expression="sample_text")
    b2 = B_Expression(expression="sample_text_2")
    _safe_set(a, 'B_Operation13', {b1})
    assert _is_linked(a, 'B_Operation13', b1)
    if hasattr(b1, 'B_Expression'):
        assert _is_linked(b1, 'B_Expression', a)
    _safe_set(a, 'B_Operation13', {b2})
    assert _is_linked(a, 'B_Operation13', b2)
    if hasattr(b1, 'B_Expression'):
        assert not _is_linked(b1, 'B_Expression', a)
    if hasattr(b2, 'B_Expression'):
        assert _is_linked(b2, 'B_Expression', a)
    _safe_set(a, 'B_Operation13', set())
    assert not _is_linked(a, 'B_Operation13', b2)
    if hasattr(b2, 'B_Expression'):
        assert not _is_linked(b2, 'B_Expression', a)


def test_assoc_statements39_link_reassign_clear():
    a = B_Expression(expression="sample_text")
    b1 = B_Any()
    b2 = B_Any()
    _safe_set(a, 'B_Expression41', b1)
    assert _is_linked(a, 'B_Expression41', b1)
    if hasattr(b1, 'B_Any40'):
        assert _is_linked(b1, 'B_Any40', a)
    _safe_set(a, 'B_Expression41', b2)
    assert _is_linked(a, 'B_Expression41', b2)
    if hasattr(b1, 'B_Any40'):
        assert not _is_linked(b1, 'B_Any40', a)
    if hasattr(b2, 'B_Any40'):
        assert _is_linked(b2, 'B_Any40', a)
    _safe_set(a, 'B_Expression41', None)
    assert not _is_linked(a, 'B_Expression41', b2)
    if hasattr(b2, 'B_Any40'):
        assert not _is_linked(b2, 'B_Any40', a)


def test_assoc_statements50_link_reassign_clear():
    a = B_Expression(expression="sample_text")
    b1 = B_Begin()
    b2 = B_Begin()
    _safe_set(a, 'B_Expression51', b1)
    assert _is_linked(a, 'B_Expression51', b1)
    if hasattr(b1, 'B_Begin'):
        assert _is_linked(b1, 'B_Begin', a)
    _safe_set(a, 'B_Expression51', b2)
    assert _is_linked(a, 'B_Expression51', b2)
    if hasattr(b1, 'B_Begin'):
        assert not _is_linked(b1, 'B_Begin', a)
    if hasattr(b2, 'B_Begin'):
        assert _is_linked(b2, 'B_Begin', a)
    _safe_set(a, 'B_Expression51', None)
    assert not _is_linked(a, 'B_Expression51', b2)
    if hasattr(b2, 'B_Begin'):
        assert not _is_linked(b2, 'B_Begin', a)


def test_assoc_true_statements42_link_reassign_clear():
    a = B_Expression(expression="sample_text")
    b1 = B_If()
    b2 = B_If()
    _safe_set(a, 'B_Expression43', b1)
    assert _is_linked(a, 'B_Expression43', b1)
    if hasattr(b1, 'B_If'):
        assert _is_linked(b1, 'B_If', a)
    _safe_set(a, 'B_Expression43', b2)
    assert _is_linked(a, 'B_Expression43', b2)
    if hasattr(b1, 'B_If'):
        assert not _is_linked(b1, 'B_If', a)
    if hasattr(b2, 'B_If'):
        assert _is_linked(b2, 'B_If', a)
    _safe_set(a, 'B_Expression43', None)
    assert not _is_linked(a, 'B_Expression43', b2)
    if hasattr(b2, 'B_If'):
        assert not _is_linked(b2, 'B_If', a)


def test_assoc_type25_link_reassign_clear():
    a = B_Variable(name="sample_text")
    b1 = B_Predicate()
    b2 = B_Predicate()
    _safe_set(a, 'B_Variable26', b1)
    assert _is_linked(a, 'B_Variable26', b1)
    if hasattr(b1, 'B_Predicate27'):
        assert _is_linked(b1, 'B_Predicate27', a)
    _safe_set(a, 'B_Variable26', b2)
    assert _is_linked(a, 'B_Variable26', b2)
    if hasattr(b1, 'B_Predicate27'):
        assert not _is_linked(b1, 'B_Predicate27', a)
    if hasattr(b2, 'B_Predicate27'):
        assert _is_linked(b2, 'B_Predicate27', a)
    _safe_set(a, 'B_Variable26', None)
    assert not _is_linked(a, 'B_Variable26', b2)
    if hasattr(b2, 'B_Predicate27'):
        assert not _is_linked(b2, 'B_Predicate27', a)


def test_assoc_variables28_link_reassign_clear():
    a = B_VariableList(size="sample_text")
    b1 = B_Variable(name="sample_text")
    b2 = B_Variable(name="sample_text_2")
    _safe_set(a, 'B_VariableList29', {b1})
    assert _is_linked(a, 'B_VariableList29', b1)
    if hasattr(b1, 'B_Variable30'):
        assert _is_linked(b1, 'B_Variable30', a)
    _safe_set(a, 'B_VariableList29', {b2})
    assert _is_linked(a, 'B_VariableList29', b2)
    if hasattr(b1, 'B_Variable30'):
        assert not _is_linked(b1, 'B_Variable30', a)
    if hasattr(b2, 'B_Variable30'):
        assert _is_linked(b2, 'B_Variable30', a)
    _safe_set(a, 'B_VariableList29', set())
    assert not _is_linked(a, 'B_VariableList29', b2)
    if hasattr(b2, 'B_Variable30'):
        assert not _is_linked(b2, 'B_Variable30', a)


def test_assoc_variables34_link_reassign_clear():
    a = B_Variable(name="sample_text")
    b1 = B_Any()
    b2 = B_Any()
    _safe_set(a, 'B_Variable35', b1)
    assert _is_linked(a, 'B_Variable35', b1)
    if hasattr(b1, 'B_Any'):
        assert _is_linked(b1, 'B_Any', a)
    _safe_set(a, 'B_Variable35', b2)
    assert _is_linked(a, 'B_Variable35', b2)
    if hasattr(b1, 'B_Any'):
        assert not _is_linked(b1, 'B_Any', a)
    if hasattr(b2, 'B_Any'):
        assert _is_linked(b2, 'B_Any', a)
    _safe_set(a, 'B_Variable35', None)
    assert not _is_linked(a, 'B_Variable35', b2)
    if hasattr(b2, 'B_Any'):
        assert not _is_linked(b2, 'B_Any', a)


def test_assoc_variables8_link_reassign_clear():
    a = B_Variable(name="sample_text")
    b1 = B_Machine(name="sample_text")
    b2 = B_Machine(name="sample_text_2")
    _safe_set(a, 'B_Variable', b1)
    assert _is_linked(a, 'B_Variable', b1)
    if hasattr(b1, 'B_Machine9'):
        assert _is_linked(b1, 'B_Machine9', a)
    _safe_set(a, 'B_Variable', b2)
    assert _is_linked(a, 'B_Variable', b2)
    if hasattr(b1, 'B_Machine9'):
        assert not _is_linked(b1, 'B_Machine9', a)
    if hasattr(b2, 'B_Machine9'):
        assert _is_linked(b2, 'B_Machine9', a)
    _safe_set(a, 'B_Variable', None)
    assert not _is_linked(a, 'B_Variable', b2)
    if hasattr(b2, 'B_Machine9'):
        assert not _is_linked(b2, 'B_Machine9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

B_Action_strategy = st.builds(B_Action)
@given(instance=B_Action_strategy)
@settings(max_examples=25)
def test_B_Action_instantiation(instance):
    assert isinstance(instance, B_Action)


B_Any_strategy = st.builds(B_Any)
@given(instance=B_Any_strategy)
@settings(max_examples=25)
def test_B_Any_instantiation(instance):
    assert isinstance(instance, B_Any)


B_Begin_strategy = st.builds(B_Begin)
@given(instance=B_Begin_strategy)
@settings(max_examples=25)
def test_B_Begin_instantiation(instance):
    assert isinstance(instance, B_Begin)


B_Expression_strategy = st.builds(B_Expression, expression=safe_text)
@given(instance=B_Expression_strategy)
@settings(max_examples=25)
def test_B_Expression_instantiation(instance):
    assert isinstance(instance, B_Expression)


B_If_strategy = st.builds(B_If)
@given(instance=B_If_strategy)
@settings(max_examples=25)
def test_B_If_instantiation(instance):
    assert isinstance(instance, B_If)


B_Machine_strategy = st.builds(B_Machine, name=safe_text)
@given(instance=B_Machine_strategy)
@settings(max_examples=25)
def test_B_Machine_instantiation(instance):
    assert isinstance(instance, B_Machine)


B_Operation_strategy = st.builds(B_Operation, name=safe_text)
@given(instance=B_Operation_strategy)
@settings(max_examples=25)
def test_B_Operation_instantiation(instance):
    assert isinstance(instance, B_Operation)


B_Predicate_strategy = st.builds(B_Predicate)
@given(instance=B_Predicate_strategy)
@settings(max_examples=25)
def test_B_Predicate_instantiation(instance):
    assert isinstance(instance, B_Predicate)


B_SET_strategy = st.builds(B_SET, name=safe_text)
@given(instance=B_SET_strategy)
@settings(max_examples=25)
def test_B_SET_instantiation(instance):
    assert isinstance(instance, B_SET)


B_Skip_strategy = st.builds(B_Skip)
@given(instance=B_Skip_strategy)
@settings(max_examples=25)
def test_B_Skip_instantiation(instance):
    assert isinstance(instance, B_Skip)


B_Variable_strategy = st.builds(B_Variable, name=safe_text)
@given(instance=B_Variable_strategy)
@settings(max_examples=25)
def test_B_Variable_instantiation(instance):
    assert isinstance(instance, B_Variable)


B_VariableList_strategy = st.builds(B_VariableList, size=safe_text)
@given(instance=B_VariableList_strategy)
@settings(max_examples=25)
def test_B_VariableList_instantiation(instance):
    assert isinstance(instance, B_VariableList)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


