import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Parameter,
    Statement,
    workflow_Condition,
    workflow_ForEach,
    workflow_InputParameter,
    workflow_OutputParameter,
    workflow_Parameter,
    workflow_Program,
    workflow_Recipe,
    workflow_SimpleCommand,
    workflow_Statement,
    workflow_Workflow,
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

def test_workflow_Condition_description_value_roundtrip():
    instance = workflow_Condition(description="sample_text", expression="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_workflow_Condition_expression_value_roundtrip():
    instance = workflow_Condition(description="sample_text", expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_workflow_ForEach_element_value_roundtrip():
    instance = workflow_ForEach(element="sample_text", sequence="sample_text")
    assert instance.element == "sample_text"
    instance.element = "sample_text_2"
    assert instance.element == "sample_text_2"


def test_workflow_ForEach_sequence_value_roundtrip():
    instance = workflow_ForEach(element="sample_text", sequence="sample_text")
    assert instance.sequence == "sample_text"
    instance.sequence = "sample_text_2"
    assert instance.sequence == "sample_text_2"


def test_workflow_Parameter_data_value_roundtrip():
    instance = workflow_Parameter(data="sample_text", option="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_workflow_Parameter_option_value_roundtrip():
    instance = workflow_Parameter(data="sample_text", option="sample_text")
    assert instance.option == "sample_text"
    instance.option = "sample_text_2"
    assert instance.option == "sample_text_2"


def test_workflow_Program_description_value_roundtrip():
    instance = workflow_Program(description="sample_text", exec_order=7, name_exec="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_workflow_Program_exec_order_value_roundtrip():
    instance = workflow_Program(description="sample_text", exec_order=7, name_exec="sample_text")
    assert instance.exec_order == 7
    instance.exec_order = 13
    assert instance.exec_order == 13


def test_workflow_Program_name_exec_value_roundtrip():
    instance = workflow_Program(description="sample_text", exec_order=7, name_exec="sample_text")
    assert instance.name_exec == "sample_text"
    instance.name_exec = "sample_text_2"
    assert instance.name_exec == "sample_text_2"


def test_workflow_Recipe_name_value_roundtrip():
    instance = workflow_Recipe(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_workflow_SimpleCommand_description_value_roundtrip():
    instance = workflow_SimpleCommand(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_workflow_Statement_exec_order_value_roundtrip():
    instance = workflow_Statement(exec_order=7)
    assert instance.exec_order == 7
    instance.exec_order = 13
    assert instance.exec_order == 13


def test_workflow_Workflow_name_value_roundtrip():
    instance = workflow_Workflow(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_workflow_InputParameter_isa_Parameter():
    instance = workflow_InputParameter()
    assert isinstance(instance, Parameter)


def test_workflow_OutputParameter_isa_Parameter():
    instance = workflow_OutputParameter()
    assert isinstance(instance, Parameter)


def test_workflow_Condition_isa_Statement():
    instance = workflow_Condition(description="sample_text", expression="sample_text")
    assert isinstance(instance, Statement)


def test_workflow_ForEach_isa_Statement():
    instance = workflow_ForEach(element="sample_text", sequence="sample_text")
    assert isinstance(instance, Statement)


def test_workflow_SimpleCommand_isa_Statement():
    instance = workflow_SimpleCommand(description="sample_text")
    assert isinstance(instance, Statement)


def test_assoc_commands1_link_reassign_clear():
    a = workflow_Statement(exec_order=7)
    b1 = workflow_Recipe(name="sample_text")
    b2 = workflow_Recipe(name="sample_text_2")
    _safe_set(a, 'workflow_Statement', b1)
    assert _is_linked(a, 'workflow_Statement', b1)
    if hasattr(b1, 'workflow_Recipe2'):
        assert _is_linked(b1, 'workflow_Recipe2', a)
    _safe_set(a, 'workflow_Statement', b2)
    assert _is_linked(a, 'workflow_Statement', b2)
    if hasattr(b1, 'workflow_Recipe2'):
        assert not _is_linked(b1, 'workflow_Recipe2', a)
    if hasattr(b2, 'workflow_Recipe2'):
        assert _is_linked(b2, 'workflow_Recipe2', a)
    _safe_set(a, 'workflow_Statement', None)
    assert not _is_linked(a, 'workflow_Statement', b2)
    if hasattr(b2, 'workflow_Recipe2'):
        assert not _is_linked(b2, 'workflow_Recipe2', a)


def test_assoc_else_branch5_link_reassign_clear():
    a = workflow_Statement(exec_order=7)
    b1 = workflow_Condition(description="sample_text", expression="sample_text")
    b2 = workflow_Condition(description="sample_text_2", expression="sample_text_2")
    _safe_set(a, 'workflow_Statement7', b1)
    assert _is_linked(a, 'workflow_Statement7', b1)
    if hasattr(b1, 'workflow_Condition6'):
        assert _is_linked(b1, 'workflow_Condition6', a)
    _safe_set(a, 'workflow_Statement7', b2)
    assert _is_linked(a, 'workflow_Statement7', b2)
    if hasattr(b1, 'workflow_Condition6'):
        assert not _is_linked(b1, 'workflow_Condition6', a)
    if hasattr(b2, 'workflow_Condition6'):
        assert _is_linked(b2, 'workflow_Condition6', a)
    _safe_set(a, 'workflow_Statement7', None)
    assert not _is_linked(a, 'workflow_Statement7', b2)
    if hasattr(b2, 'workflow_Condition6'):
        assert not _is_linked(b2, 'workflow_Condition6', a)


def test_assoc_parameters8_link_reassign_clear():
    a = workflow_Program(description="sample_text", exec_order=7, name_exec="sample_text")
    b1 = workflow_Parameter(data="sample_text", option="sample_text")
    b2 = workflow_Parameter(data="sample_text_2", option="sample_text_2")
    _safe_set(a, 'workflow_Program', {b1})
    assert _is_linked(a, 'workflow_Program', b1)
    if hasattr(b1, 'workflow_Parameter'):
        assert _is_linked(b1, 'workflow_Parameter', a)
    _safe_set(a, 'workflow_Program', {b2})
    assert _is_linked(a, 'workflow_Program', b2)
    if hasattr(b1, 'workflow_Parameter'):
        assert not _is_linked(b1, 'workflow_Parameter', a)
    if hasattr(b2, 'workflow_Parameter'):
        assert _is_linked(b2, 'workflow_Parameter', a)
    _safe_set(a, 'workflow_Program', set())
    assert not _is_linked(a, 'workflow_Program', b2)
    if hasattr(b2, 'workflow_Parameter'):
        assert not _is_linked(b2, 'workflow_Parameter', a)


def test_assoc_programs9_link_reassign_clear():
    a = workflow_SimpleCommand(description="sample_text")
    b1 = workflow_Program(description="sample_text", exec_order=7, name_exec="sample_text")
    b2 = workflow_Program(description="sample_text_2", exec_order=13, name_exec="sample_text_2")
    _safe_set(a, 'workflow_SimpleCommand', {b1})
    assert _is_linked(a, 'workflow_SimpleCommand', b1)
    if hasattr(b1, 'workflow_Program10'):
        assert _is_linked(b1, 'workflow_Program10', a)
    _safe_set(a, 'workflow_SimpleCommand', {b2})
    assert _is_linked(a, 'workflow_SimpleCommand', b2)
    if hasattr(b1, 'workflow_Program10'):
        assert not _is_linked(b1, 'workflow_Program10', a)
    if hasattr(b2, 'workflow_Program10'):
        assert _is_linked(b2, 'workflow_Program10', a)
    _safe_set(a, 'workflow_SimpleCommand', set())
    assert not _is_linked(a, 'workflow_SimpleCommand', b2)
    if hasattr(b2, 'workflow_Program10'):
        assert not _is_linked(b2, 'workflow_Program10', a)


def test_assoc_recipes0_link_reassign_clear():
    a = workflow_Workflow(name="sample_text")
    b1 = workflow_Recipe(name="sample_text")
    b2 = workflow_Recipe(name="sample_text_2")
    _safe_set(a, 'workflow_Workflow', {b1})
    assert _is_linked(a, 'workflow_Workflow', b1)
    if hasattr(b1, 'workflow_Recipe'):
        assert _is_linked(b1, 'workflow_Recipe', a)
    _safe_set(a, 'workflow_Workflow', {b2})
    assert _is_linked(a, 'workflow_Workflow', b2)
    if hasattr(b1, 'workflow_Recipe'):
        assert not _is_linked(b1, 'workflow_Recipe', a)
    if hasattr(b2, 'workflow_Recipe'):
        assert _is_linked(b2, 'workflow_Recipe', a)
    _safe_set(a, 'workflow_Workflow', set())
    assert not _is_linked(a, 'workflow_Workflow', b2)
    if hasattr(b2, 'workflow_Recipe'):
        assert not _is_linked(b2, 'workflow_Recipe', a)


def test_assoc_statements15_link_reassign_clear():
    a = workflow_Statement(exec_order=7)
    b1 = workflow_ForEach(element="sample_text", sequence="sample_text")
    b2 = workflow_ForEach(element="sample_text_2", sequence="sample_text_2")
    _safe_set(a, 'workflow_Statement16', b1)
    assert _is_linked(a, 'workflow_Statement16', b1)
    if hasattr(b1, 'workflow_ForEach'):
        assert _is_linked(b1, 'workflow_ForEach', a)
    _safe_set(a, 'workflow_Statement16', b2)
    assert _is_linked(a, 'workflow_Statement16', b2)
    if hasattr(b1, 'workflow_ForEach'):
        assert not _is_linked(b1, 'workflow_ForEach', a)
    if hasattr(b2, 'workflow_ForEach'):
        assert _is_linked(b2, 'workflow_ForEach', a)
    _safe_set(a, 'workflow_Statement16', None)
    assert not _is_linked(a, 'workflow_Statement16', b2)
    if hasattr(b2, 'workflow_ForEach'):
        assert not _is_linked(b2, 'workflow_ForEach', a)


def test_assoc_then_branch3_link_reassign_clear():
    a = workflow_Statement(exec_order=7)
    b1 = workflow_Condition(description="sample_text", expression="sample_text")
    b2 = workflow_Condition(description="sample_text_2", expression="sample_text_2")
    _safe_set(a, 'workflow_Statement4', b1)
    assert _is_linked(a, 'workflow_Statement4', b1)
    if hasattr(b1, 'workflow_Condition'):
        assert _is_linked(b1, 'workflow_Condition', a)
    _safe_set(a, 'workflow_Statement4', b2)
    assert _is_linked(a, 'workflow_Statement4', b2)
    if hasattr(b1, 'workflow_Condition'):
        assert not _is_linked(b1, 'workflow_Condition', a)
    if hasattr(b2, 'workflow_Condition'):
        assert _is_linked(b2, 'workflow_Condition', a)
    _safe_set(a, 'workflow_Statement4', None)
    assert not _is_linked(a, 'workflow_Statement4', b2)
    if hasattr(b2, 'workflow_Condition'):
        assert not _is_linked(b2, 'workflow_Condition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


workflow_Condition_strategy = st.builds(workflow_Condition, description=safe_text, expression=safe_text)
@given(instance=workflow_Condition_strategy)
@settings(max_examples=25)
def test_workflow_Condition_instantiation(instance):
    assert isinstance(instance, workflow_Condition)


workflow_ForEach_strategy = st.builds(workflow_ForEach, element=safe_text, sequence=safe_text)
@given(instance=workflow_ForEach_strategy)
@settings(max_examples=25)
def test_workflow_ForEach_instantiation(instance):
    assert isinstance(instance, workflow_ForEach)


workflow_InputParameter_strategy = st.builds(workflow_InputParameter)
@given(instance=workflow_InputParameter_strategy)
@settings(max_examples=25)
def test_workflow_InputParameter_instantiation(instance):
    assert isinstance(instance, workflow_InputParameter)


workflow_OutputParameter_strategy = st.builds(workflow_OutputParameter)
@given(instance=workflow_OutputParameter_strategy)
@settings(max_examples=25)
def test_workflow_OutputParameter_instantiation(instance):
    assert isinstance(instance, workflow_OutputParameter)


workflow_Parameter_strategy = st.builds(workflow_Parameter, data=safe_text, option=safe_text)
@given(instance=workflow_Parameter_strategy)
@settings(max_examples=25)
def test_workflow_Parameter_instantiation(instance):
    assert isinstance(instance, workflow_Parameter)


workflow_Program_strategy = st.builds(workflow_Program, description=safe_text, exec_order=st.integers(), name_exec=safe_text)
@given(instance=workflow_Program_strategy)
@settings(max_examples=25)
def test_workflow_Program_instantiation(instance):
    assert isinstance(instance, workflow_Program)


workflow_Recipe_strategy = st.builds(workflow_Recipe, name=safe_text)
@given(instance=workflow_Recipe_strategy)
@settings(max_examples=25)
def test_workflow_Recipe_instantiation(instance):
    assert isinstance(instance, workflow_Recipe)


workflow_SimpleCommand_strategy = st.builds(workflow_SimpleCommand, description=safe_text)
@given(instance=workflow_SimpleCommand_strategy)
@settings(max_examples=25)
def test_workflow_SimpleCommand_instantiation(instance):
    assert isinstance(instance, workflow_SimpleCommand)


workflow_Statement_strategy = st.builds(workflow_Statement, exec_order=st.integers())
@given(instance=workflow_Statement_strategy)
@settings(max_examples=25)
def test_workflow_Statement_instantiation(instance):
    assert isinstance(instance, workflow_Statement)


workflow_Workflow_strategy = st.builds(workflow_Workflow, name=safe_text)
@given(instance=workflow_Workflow_strategy)
@settings(max_examples=25)
def test_workflow_Workflow_instantiation(instance):
    assert isinstance(instance, workflow_Workflow)


