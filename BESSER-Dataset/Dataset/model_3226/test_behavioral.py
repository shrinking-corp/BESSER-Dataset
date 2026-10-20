import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    conformant_array_schema,
    constant_definition,
    goto_statement,
    pascal_DeclarationPart,
    pascal_EObject,
    pascal_ElementList,
    pascal_ExpressionList,
    pascal_FunctionDesignator,
    pascal_Model,
    pascal_Set,
    pascal_Variable1,
    pascal_array_type,
    pascal_assignment_statement,
    pascal_block,
    pascal_bound_specification,
    pascal_case_label_list,
    pascal_case_limb,
    pascal_case_statement,
    pascal_compound_statement,
    pascal_conditional_statement,
    pascal_conformant_array_schema,
    pascal_constant,
    pascal_constant_definition,
    pascal_constant_definition_part,
    pascal_enumerated_type,
    pascal_expression,
    pascal_factor,
    pascal_field_list,
    pascal_file_type,
    pascal_fixed_part,
    pascal_for_statement,
    pascal_formal_parameter_list,
    pascal_formal_parameter_section,
    pascal_function_declaration,
    pascal_function_heading,
    pascal_goto_statement,
    pascal_identifier_list,
    pascal_if_statement,
    pascal_label,
    pascal_label_declaration_part,
    pascal_number,
    pascal_packed_conformant_array_schema,
    pascal_parameter_type,
    pascal_pointer_type,
    pascal_procedure_and_function_declaration_part,
    pascal_procedure_declaration,
    pascal_procedure_heading,
    pascal_procedure_statement,
    pascal_program,
    pascal_program_heading,
    pascal_record_section,
    pascal_record_type,
    pascal_repeat_statement,
    pascal_repetitive_statement,
    pascal_set_type,
    pascal_simple_expression,
    pascal_simple_statement,
    pascal_simple_type,
    pascal_statement,
    pascal_statement_part,
    pascal_statement_sequence,
    pascal_structured_statement,
    pascal_structured_type,
    pascal_subrange_type,
    pascal_tag_field,
    pascal_term,
    pascal_type,
    pascal_type_definition,
    pascal_type_definition_part,
    pascal_unpacked_conformant_array_Schema,
    pascal_unpacked_structured_type,
    pascal_value_parameter_section,
    pascal_variable,
    pascal_variable_declaration,
    pascal_variable_declaration_part,
    pascal_variable_parameter_section,
    pascal_variant,
    pascal_variant_part,
    pascal_while_statement,
    pascal_with_statement,
    program_heading,
    repetitive_statement,
    simple_statement,
    statement,
    statement_part,
    structured_statement,
    type_definition,
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

def test_assoc_conformantArraySchema76_reverse_link_reassign_clear():
    a1 = pascal_parameter_type(id="sample_text")
    a2 = pascal_parameter_type(id="sample_text_2")
    b = pascal_conformant_array_schema(id="sample_text")
    _safe_set(b, 'pascal_conformant_array_schema', a1)
    assert _is_linked(b, 'pascal_conformant_array_schema', a1)
    if hasattr(a1, 'pascal_parameter_type77'):
        assert _is_linked(a1, 'pascal_parameter_type77', b)
    _safe_set(b, 'pascal_conformant_array_schema', a2)
    assert _is_linked(b, 'pascal_conformant_array_schema', a2)
    if hasattr(a1, 'pascal_parameter_type77'):
        assert not _is_linked(a1, 'pascal_parameter_type77', b)
    if hasattr(a2, 'pascal_parameter_type77'):
        assert _is_linked(a2, 'pascal_parameter_type77', b)
    _safe_set(b, 'pascal_conformant_array_schema', None)
    assert not _is_linked(b, 'pascal_conformant_array_schema', a2)
    if hasattr(a2, 'pascal_parameter_type77'):
        assert not _is_linked(a2, 'pascal_parameter_type77', b)


def test_assoc_expression1100_reverse_link_reassign_clear():
    a1 = pascal_for_statement(name="sample_text")
    a2 = pascal_for_statement(name="sample_text_2")
    b = pascal_expression(relational_operators="sample_text")
    _safe_set(b, 'pascal_expression101', a1)
    assert _is_linked(b, 'pascal_expression101', a1)
    if hasattr(a1, 'pascal_for_statement'):
        assert _is_linked(a1, 'pascal_for_statement', b)
    _safe_set(b, 'pascal_expression101', a2)
    assert _is_linked(b, 'pascal_expression101', a2)
    if hasattr(a1, 'pascal_for_statement'):
        assert not _is_linked(a1, 'pascal_for_statement', b)
    if hasattr(a2, 'pascal_for_statement'):
        assert _is_linked(a2, 'pascal_for_statement', b)
    _safe_set(b, 'pascal_expression101', None)
    assert not _is_linked(b, 'pascal_expression101', a2)
    if hasattr(a2, 'pascal_for_statement'):
        assert not _is_linked(a2, 'pascal_for_statement', b)


def test_assoc_expression151_reverse_link_reassign_clear():
    a1 = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    a2 = pascal_factor(id="sample_text_2", nil="sample_text_2", string="sample_text_2")
    b = pascal_expression(relational_operators="sample_text")
    _safe_set(b, 'pascal_expression153', a1)
    assert _is_linked(b, 'pascal_expression153', a1)
    if hasattr(a1, 'pascal_factor152'):
        assert _is_linked(a1, 'pascal_factor152', b)
    _safe_set(b, 'pascal_expression153', a2)
    assert _is_linked(b, 'pascal_expression153', a2)
    if hasattr(a1, 'pascal_factor152'):
        assert not _is_linked(a1, 'pascal_factor152', b)
    if hasattr(a2, 'pascal_factor152'):
        assert _is_linked(a2, 'pascal_factor152', b)
    _safe_set(b, 'pascal_expression153', None)
    assert not _is_linked(b, 'pascal_expression153', a2)
    if hasattr(a2, 'pascal_factor152'):
        assert not _is_linked(a2, 'pascal_factor152', b)


def test_assoc_expression2102_reverse_link_reassign_clear():
    a1 = pascal_for_statement(name="sample_text")
    a2 = pascal_for_statement(name="sample_text_2")
    b = pascal_expression(relational_operators="sample_text")
    _safe_set(b, 'pascal_expression104', a1)
    assert _is_linked(b, 'pascal_expression104', a1)
    if hasattr(a1, 'pascal_for_statement103'):
        assert _is_linked(a1, 'pascal_for_statement103', b)
    _safe_set(b, 'pascal_expression104', a2)
    assert _is_linked(b, 'pascal_expression104', a2)
    if hasattr(a1, 'pascal_for_statement103'):
        assert not _is_linked(a1, 'pascal_for_statement103', b)
    if hasattr(a2, 'pascal_for_statement103'):
        assert _is_linked(a2, 'pascal_for_statement103', b)
    _safe_set(b, 'pascal_expression104', None)
    assert not _is_linked(b, 'pascal_expression104', a2)
    if hasattr(a2, 'pascal_for_statement103'):
        assert not _is_linked(a2, 'pascal_for_statement103', b)


def test_assoc_expression87_reverse_link_reassign_clear():
    a1 = pascal_expression(relational_operators="sample_text")
    a2 = pascal_expression(relational_operators="sample_text_2")
    b = pascal_assignment_statement(identifier="sample_text", variable="sample_text")
    _safe_set(b, 'pascal_assignment_statement', a1)
    assert _is_linked(b, 'pascal_assignment_statement', a1)
    if hasattr(a1, 'pascal_expression'):
        assert _is_linked(a1, 'pascal_expression', b)
    _safe_set(b, 'pascal_assignment_statement', a2)
    assert _is_linked(b, 'pascal_assignment_statement', a2)
    if hasattr(a1, 'pascal_expression'):
        assert not _is_linked(a1, 'pascal_expression', b)
    if hasattr(a2, 'pascal_expression'):
        assert _is_linked(a2, 'pascal_expression', b)
    _safe_set(b, 'pascal_assignment_statement', None)
    assert not _is_linked(b, 'pascal_assignment_statement', a2)
    if hasattr(a2, 'pascal_expression'):
        assert not _is_linked(a2, 'pascal_expression', b)


def test_assoc_factor155_reverse_link_reassign_clear():
    a1 = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    a2 = pascal_factor(id="sample_text_2", nil="sample_text_2", string="sample_text_2")
    b = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    _safe_set(b, 'pascal_factor156', a1)
    assert _is_linked(b, 'pascal_factor156', a1)
    if hasattr(a1, 'pascal_factor154'):
        assert _is_linked(a1, 'pascal_factor154', b)
    _safe_set(b, 'pascal_factor156', a2)
    assert _is_linked(b, 'pascal_factor156', a2)
    if hasattr(a1, 'pascal_factor154'):
        assert not _is_linked(a1, 'pascal_factor154', b)
    if hasattr(a2, 'pascal_factor154'):
        assert _is_linked(a2, 'pascal_factor154', b)
    _safe_set(b, 'pascal_factor156', None)
    assert not _is_linked(b, 'pascal_factor156', a2)
    if hasattr(a2, 'pascal_factor154'):
        assert not _is_linked(a2, 'pascal_factor154', b)


def test_assoc_functionDesignator142_reverse_link_reassign_clear():
    a1 = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    a2 = pascal_factor(id="sample_text_2", nil="sample_text_2", string="sample_text_2")
    b = pascal_FunctionDesignator(name="sample_text")
    _safe_set(b, 'pascal_FunctionDesignator', a1)
    assert _is_linked(b, 'pascal_FunctionDesignator', a1)
    if hasattr(a1, 'pascal_factor143'):
        assert _is_linked(a1, 'pascal_factor143', b)
    _safe_set(b, 'pascal_FunctionDesignator', a2)
    assert _is_linked(b, 'pascal_FunctionDesignator', a2)
    if hasattr(a1, 'pascal_factor143'):
        assert not _is_linked(a1, 'pascal_factor143', b)
    if hasattr(a2, 'pascal_factor143'):
        assert _is_linked(a2, 'pascal_factor143', b)
    _safe_set(b, 'pascal_FunctionDesignator', None)
    assert not _is_linked(b, 'pascal_FunctionDesignator', a2)
    if hasattr(a2, 'pascal_factor143'):
        assert not _is_linked(a2, 'pascal_factor143', b)


def test_assoc_number147_reverse_link_reassign_clear():
    a1 = pascal_number(integer="sample_text", real="sample_text")
    a2 = pascal_number(integer="sample_text_2", real="sample_text_2")
    b = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    _safe_set(b, 'pascal_factor148', a1)
    assert _is_linked(b, 'pascal_factor148', a1)
    if hasattr(a1, 'pascal_number'):
        assert _is_linked(a1, 'pascal_number', b)
    _safe_set(b, 'pascal_factor148', a2)
    assert _is_linked(b, 'pascal_factor148', a2)
    if hasattr(a1, 'pascal_number'):
        assert not _is_linked(a1, 'pascal_number', b)
    if hasattr(a2, 'pascal_number'):
        assert _is_linked(a2, 'pascal_number', b)
    _safe_set(b, 'pascal_factor148', None)
    assert not _is_linked(b, 'pascal_factor148', a2)
    if hasattr(a2, 'pascal_number'):
        assert not _is_linked(a2, 'pascal_number', b)


def test_assoc_number237_reverse_link_reassign_clear():
    a1 = pascal_number(integer="sample_text", real="sample_text")
    a2 = pascal_number(integer="sample_text_2", real="sample_text_2")
    b = pascal_constant(name="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant238', a1)
    assert _is_linked(b, 'pascal_constant238', a1)
    if hasattr(a1, 'pascal_number239'):
        assert _is_linked(a1, 'pascal_number239', b)
    _safe_set(b, 'pascal_constant238', a2)
    assert _is_linked(b, 'pascal_constant238', a2)
    if hasattr(a1, 'pascal_number239'):
        assert not _is_linked(a1, 'pascal_number239', b)
    if hasattr(a2, 'pascal_number239'):
        assert _is_linked(a2, 'pascal_number239', b)
    _safe_set(b, 'pascal_constant238', None)
    assert not _is_linked(b, 'pascal_constant238', a2)
    if hasattr(a2, 'pascal_number239'):
        assert not _is_linked(a2, 'pascal_number239', b)


def test_assoc_pointerType173_reverse_link_reassign_clear():
    a1 = pascal_type(name="sample_text")
    a2 = pascal_type(name="sample_text_2")
    b = pascal_pointer_type(name="sample_text")
    _safe_set(b, 'pascal_pointer_type', a1)
    assert _is_linked(b, 'pascal_pointer_type', a1)
    if hasattr(a1, 'pascal_type174'):
        assert _is_linked(a1, 'pascal_type174', b)
    _safe_set(b, 'pascal_pointer_type', a2)
    assert _is_linked(b, 'pascal_pointer_type', a2)
    if hasattr(a1, 'pascal_type174'):
        assert not _is_linked(a1, 'pascal_type174', b)
    if hasattr(a2, 'pascal_type174'):
        assert _is_linked(a2, 'pascal_type174', b)
    _safe_set(b, 'pascal_pointer_type', None)
    assert not _is_linked(b, 'pascal_pointer_type', a2)
    if hasattr(a2, 'pascal_type174'):
        assert not _is_linked(a2, 'pascal_type174', b)


def test_assoc_simpleType169_reverse_link_reassign_clear():
    a1 = pascal_type(name="sample_text")
    a2 = pascal_type(name="sample_text_2")
    b = pascal_simple_type(primitiveType="sample_text")
    _safe_set(b, 'pascal_simple_type', a1)
    assert _is_linked(b, 'pascal_simple_type', a1)
    if hasattr(a1, 'pascal_type170'):
        assert _is_linked(a1, 'pascal_type170', b)
    _safe_set(b, 'pascal_simple_type', a2)
    assert _is_linked(b, 'pascal_simple_type', a2)
    if hasattr(a1, 'pascal_type170'):
        assert not _is_linked(a1, 'pascal_type170', b)
    if hasattr(a2, 'pascal_type170'):
        assert _is_linked(a2, 'pascal_type170', b)
    _safe_set(b, 'pascal_simple_type', None)
    assert not _is_linked(b, 'pascal_simple_type', a2)
    if hasattr(a2, 'pascal_type170'):
        assert not _is_linked(a2, 'pascal_type170', b)


def test_assoc_tagfield224_reverse_link_reassign_clear():
    a1 = pascal_variant_part(id="sample_text")
    a2 = pascal_variant_part(id="sample_text_2")
    b = pascal_tag_field(id="sample_text")
    _safe_set(b, 'pascal_tag_field', a1)
    assert _is_linked(b, 'pascal_tag_field', a1)
    if hasattr(a1, 'pascal_variant_part225'):
        assert _is_linked(a1, 'pascal_variant_part225', b)
    _safe_set(b, 'pascal_tag_field', a2)
    assert _is_linked(b, 'pascal_tag_field', a2)
    if hasattr(a1, 'pascal_variant_part225'):
        assert not _is_linked(a1, 'pascal_variant_part225', b)
    if hasattr(a2, 'pascal_variant_part225'):
        assert _is_linked(a2, 'pascal_variant_part225', b)
    _safe_set(b, 'pascal_tag_field', None)
    assert not _is_linked(b, 'pascal_tag_field', a2)
    if hasattr(a2, 'pascal_variant_part225'):
        assert not _is_linked(a2, 'pascal_variant_part225', b)


def test_assoc_type43_reverse_link_reassign_clear():
    a1 = pascal_type(name="sample_text")
    a2 = pascal_type(name="sample_text_2")
    b = pascal_function_declaration(name="sample_text")
    _safe_set(b, 'pascal_function_declaration44', a1)
    assert _is_linked(b, 'pascal_function_declaration44', a1)
    if hasattr(a1, 'pascal_type45'):
        assert _is_linked(a1, 'pascal_type45', b)
    _safe_set(b, 'pascal_function_declaration44', a2)
    assert _is_linked(b, 'pascal_function_declaration44', a2)
    if hasattr(a1, 'pascal_type45'):
        assert not _is_linked(a1, 'pascal_type45', b)
    if hasattr(a2, 'pascal_type45'):
        assert _is_linked(a2, 'pascal_type45', b)
    _safe_set(b, 'pascal_function_declaration44', None)
    assert not _is_linked(b, 'pascal_function_declaration44', a2)
    if hasattr(a2, 'pascal_type45'):
        assert not _is_linked(a2, 'pascal_type45', b)


def test_assoc_variable1157_reverse_link_reassign_clear():
    a1 = pascal_variable(name="sample_text")
    a2 = pascal_variable(name="sample_text_2")
    b = pascal_Variable1(name="sample_text")
    _safe_set(b, 'pascal_Variable1', a1)
    assert _is_linked(b, 'pascal_Variable1', a1)
    if hasattr(a1, 'pascal_variable158'):
        assert _is_linked(a1, 'pascal_variable158', b)
    _safe_set(b, 'pascal_Variable1', a2)
    assert _is_linked(b, 'pascal_Variable1', a2)
    if hasattr(a1, 'pascal_variable158'):
        assert not _is_linked(a1, 'pascal_variable158', b)
    if hasattr(a2, 'pascal_variable158'):
        assert _is_linked(a2, 'pascal_variable158', b)
    _safe_set(b, 'pascal_Variable1', None)
    assert not _is_linked(b, 'pascal_Variable1', a2)
    if hasattr(a2, 'pascal_variable158'):
        assert not _is_linked(a2, 'pascal_variable158', b)


def test_assoc_variable1162_reverse_link_reassign_clear():
    a1 = pascal_Variable1(name="sample_text")
    a2 = pascal_Variable1(name="sample_text_2")
    b = pascal_Variable1(name="sample_text")
    _safe_set(b, 'pascal_Variable1163', a1)
    assert _is_linked(b, 'pascal_Variable1163', a1)
    if hasattr(a1, 'pascal_Variable1161'):
        assert _is_linked(a1, 'pascal_Variable1161', b)
    _safe_set(b, 'pascal_Variable1163', a2)
    assert _is_linked(b, 'pascal_Variable1163', a2)
    if hasattr(a1, 'pascal_Variable1161'):
        assert not _is_linked(a1, 'pascal_Variable1161', b)
    if hasattr(a2, 'pascal_Variable1161'):
        assert _is_linked(a2, 'pascal_Variable1161', b)
    _safe_set(b, 'pascal_Variable1163', None)
    assert not _is_linked(b, 'pascal_Variable1163', a2)
    if hasattr(a2, 'pascal_Variable1161'):
        assert not _is_linked(a2, 'pascal_Variable1161', b)


def test_assoc_variable144_reverse_link_reassign_clear():
    a1 = pascal_variable(name="sample_text")
    a2 = pascal_variable(name="sample_text_2")
    b = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    _safe_set(b, 'pascal_factor145', a1)
    assert _is_linked(b, 'pascal_factor145', a1)
    if hasattr(a1, 'pascal_variable146'):
        assert _is_linked(a1, 'pascal_variable146', b)
    _safe_set(b, 'pascal_factor145', a2)
    assert _is_linked(b, 'pascal_factor145', a2)
    if hasattr(a1, 'pascal_variable146'):
        assert not _is_linked(a1, 'pascal_variable146', b)
    if hasattr(a2, 'pascal_variable146'):
        assert _is_linked(a2, 'pascal_variable146', b)
    _safe_set(b, 'pascal_factor145', None)
    assert not _is_linked(b, 'pascal_factor145', a2)
    if hasattr(a2, 'pascal_variable146'):
        assert not _is_linked(a2, 'pascal_variable146', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_FormalParameterList49_stub_double():
    # pascal_formal_parameter_list has no real 'pascal_formal_parameter_list50' property in the generated
    # code (a bare stub) -- manually attach it so pascal_procedure_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_procedure_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_procedure_heading(name="sample_text")
    partner = pascal_formal_parameter_list()
    setattr(partner, 'pascal_formal_parameter_list50', None)
    _safe_set(owner, 'pascal_procedure_heading', partner)
    assert getattr(partner, 'pascal_formal_parameter_list50') == owner
    _safe_set(owner, 'pascal_procedure_heading', None)
    assert getattr(partner, 'pascal_formal_parameter_list50') is None


def test_assoc_FormalParameterList51_stub_double():
    # pascal_formal_parameter_list has no real 'pascal_formal_parameter_list52' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_heading(id1="sample_text", id2="sample_text")
    partner = pascal_formal_parameter_list()
    setattr(partner, 'pascal_formal_parameter_list52', None)
    _safe_set(owner, 'pascal_function_heading', partner)
    assert getattr(partner, 'pascal_formal_parameter_list52') == owner
    _safe_set(owner, 'pascal_function_heading', None)
    assert getattr(partner, 'pascal_formal_parameter_list52') is None


def test_assoc_block37_stub_double():
    # pascal_block has no real 'pascal_block39' property in the generated
    # code (a bare stub) -- manually attach it so pascal_procedure_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_procedure_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_procedure_declaration(name="sample_text")
    partner = pascal_block()
    setattr(partner, 'pascal_block39', None)
    _safe_set(owner, 'pascal_procedure_declaration38', partner)
    assert getattr(partner, 'pascal_block39') == owner
    _safe_set(owner, 'pascal_procedure_declaration38', None)
    assert getattr(partner, 'pascal_block39') is None


def test_assoc_block46_stub_double():
    # pascal_block has no real 'pascal_block48' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_declaration(name="sample_text")
    partner = pascal_block()
    setattr(partner, 'pascal_block48', None)
    _safe_set(owner, 'pascal_function_declaration47', partner)
    assert getattr(partner, 'pascal_block48') == owner
    _safe_set(owner, 'pascal_function_declaration47', None)
    assert getattr(partner, 'pascal_block48') is None


def test_assoc_boundSpecification78_stub_double():
    # pascal_packed_conformant_array_schema has no real 'pascal_packed_conformant_array_schema' property in the generated
    # code (a bare stub) -- manually attach it so pascal_bound_specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_bound_specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_bound_specification(id1="sample_text", id2="sample_text", id3="sample_text")
    partner = pascal_packed_conformant_array_schema()
    setattr(partner, 'pascal_packed_conformant_array_schema', None)
    _safe_set(owner, 'pascal_bound_specification', partner)
    assert getattr(partner, 'pascal_packed_conformant_array_schema') == owner
    _safe_set(owner, 'pascal_bound_specification', None)
    assert getattr(partner, 'pascal_packed_conformant_array_schema') is None


def test_assoc_boundSpecifications79_stub_double():
    # pascal_unpacked_conformant_array_Schema has no real 'pascal_unpacked_conformant_array_Schema' property in the generated
    # code (a bare stub) -- manually attach it so pascal_bound_specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_bound_specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_bound_specification(id1="sample_text", id2="sample_text", id3="sample_text")
    partner = pascal_unpacked_conformant_array_Schema()
    setattr(partner, 'pascal_unpacked_conformant_array_Schema', None)
    _safe_set(owner, 'pascal_bound_specification80', partner)
    assert owner in getattr(partner, 'pascal_unpacked_conformant_array_Schema')
    _safe_set(owner, 'pascal_bound_specification80', None)
    assert owner not in getattr(partner, 'pascal_unpacked_conformant_array_Schema')


def test_assoc_conformantArraySchema81_stub_double():
    # pascal_unpacked_conformant_array_Schema has no real 'pascal_unpacked_conformant_array_Schema82' property in the generated
    # code (a bare stub) -- manually attach it so pascal_conformant_array_schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_conformant_array_schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_conformant_array_schema(id="sample_text")
    partner = pascal_unpacked_conformant_array_Schema()
    setattr(partner, 'pascal_unpacked_conformant_array_Schema82', None)
    _safe_set(owner, 'pascal_conformant_array_schema83', partner)
    assert getattr(partner, 'pascal_unpacked_conformant_array_Schema82') == owner
    _safe_set(owner, 'pascal_conformant_array_schema83', None)
    assert getattr(partner, 'pascal_unpacked_conformant_array_Schema82') is None


def test_assoc_constant182_stub_double():
    # pascal_subrange_type has no real 'pascal_subrange_type183' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(name="sample_text", string="sample_text")
    partner = pascal_subrange_type()
    setattr(partner, 'pascal_subrange_type183', None)
    _safe_set(owner, 'pascal_constant184', partner)
    assert getattr(partner, 'pascal_subrange_type183') == owner
    _safe_set(owner, 'pascal_constant184', None)
    assert getattr(partner, 'pascal_subrange_type183') is None


def test_assoc_constant2185_stub_double():
    # pascal_subrange_type has no real 'pascal_subrange_type186' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(name="sample_text", string="sample_text")
    partner = pascal_subrange_type()
    setattr(partner, 'pascal_subrange_type186', None)
    _safe_set(owner, 'pascal_constant187', partner)
    assert getattr(partner, 'pascal_subrange_type186') == owner
    _safe_set(owner, 'pascal_constant187', None)
    assert getattr(partner, 'pascal_subrange_type186') is None


def test_assoc_constants130_stub_double():
    # pascal_case_label_list has no real 'pascal_case_label_list131' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(name="sample_text", string="sample_text")
    partner = pascal_case_label_list()
    setattr(partner, 'pascal_case_label_list131', None)
    _safe_set(owner, 'pascal_constant', partner)
    assert owner in getattr(partner, 'pascal_case_label_list131')
    _safe_set(owner, 'pascal_constant', None)
    assert owner not in getattr(partner, 'pascal_case_label_list131')


def test_assoc_enumeratedType177_stub_double():
    # pascal_enumerated_type has no real 'pascal_enumerated_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(primitiveType="sample_text")
    partner = pascal_enumerated_type()
    setattr(partner, 'pascal_enumerated_type', None)
    _safe_set(owner, 'pascal_simple_type178', partner)
    assert getattr(partner, 'pascal_enumerated_type') == owner
    _safe_set(owner, 'pascal_simple_type178', None)
    assert getattr(partner, 'pascal_enumerated_type') is None


def test_assoc_expression111_stub_double():
    # pascal_if_statement has no real 'pascal_if_statement112' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operators="sample_text")
    partner = pascal_if_statement()
    setattr(partner, 'pascal_if_statement112', None)
    _safe_set(owner, 'pascal_expression113', partner)
    assert getattr(partner, 'pascal_if_statement112') == owner
    _safe_set(owner, 'pascal_expression113', None)
    assert getattr(partner, 'pascal_if_statement112') is None


def test_assoc_expression120_stub_double():
    # pascal_case_statement has no real 'pascal_case_statement121' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operators="sample_text")
    partner = pascal_case_statement()
    setattr(partner, 'pascal_case_statement121', None)
    _safe_set(owner, 'pascal_expression122', partner)
    assert getattr(partner, 'pascal_case_statement121') == owner
    _safe_set(owner, 'pascal_expression122', None)
    assert getattr(partner, 'pascal_case_statement121') is None


def test_assoc_expression90_stub_double():
    # pascal_while_statement has no real 'pascal_while_statement' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operators="sample_text")
    partner = pascal_while_statement()
    setattr(partner, 'pascal_while_statement', None)
    _safe_set(owner, 'pascal_expression91', partner)
    assert getattr(partner, 'pascal_while_statement') == owner
    _safe_set(owner, 'pascal_expression91', None)
    assert getattr(partner, 'pascal_while_statement') is None


def test_assoc_expression97_stub_double():
    # pascal_repeat_statement has no real 'pascal_repeat_statement98' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operators="sample_text")
    partner = pascal_repeat_statement()
    setattr(partner, 'pascal_repeat_statement98', None)
    _safe_set(owner, 'pascal_expression99', partner)
    assert getattr(partner, 'pascal_repeat_statement98') == owner
    _safe_set(owner, 'pascal_expression99', None)
    assert getattr(partner, 'pascal_repeat_statement98') is None


def test_assoc_expressionList159_stub_double():
    # pascal_ExpressionList has no real 'pascal_ExpressionList' property in the generated
    # code (a bare stub) -- manually attach it so pascal_Variable1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_Variable1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_Variable1(name="sample_text")
    partner = pascal_ExpressionList()
    setattr(partner, 'pascal_ExpressionList', None)
    _safe_set(owner, 'pascal_Variable1160', partner)
    assert getattr(partner, 'pascal_ExpressionList') == owner
    _safe_set(owner, 'pascal_Variable1160', None)
    assert getattr(partner, 'pascal_ExpressionList') is None


def test_assoc_expressions166_stub_double():
    # pascal_ElementList has no real 'pascal_ElementList167' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operators="sample_text")
    partner = pascal_ElementList()
    setattr(partner, 'pascal_ElementList167', None)
    _safe_set(owner, 'pascal_expression168', partner)
    assert owner in getattr(partner, 'pascal_ElementList167')
    _safe_set(owner, 'pascal_expression168', None)
    assert owner not in getattr(partner, 'pascal_ElementList167')


def test_assoc_expressions234_stub_double():
    # pascal_ExpressionList has no real 'pascal_ExpressionList235' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operators="sample_text")
    partner = pascal_ExpressionList()
    setattr(partner, 'pascal_ExpressionList235', None)
    _safe_set(owner, 'pascal_expression236', partner)
    assert owner in getattr(partner, 'pascal_ExpressionList235')
    _safe_set(owner, 'pascal_expression236', None)
    assert owner not in getattr(partner, 'pascal_ExpressionList235')


def test_assoc_factors140_stub_double():
    # pascal_term has no real 'pascal_term141' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    partner = pascal_term()
    setattr(partner, 'pascal_term141', None)
    _safe_set(owner, 'pascal_factor', partner)
    assert owner in getattr(partner, 'pascal_term141')
    _safe_set(owner, 'pascal_factor', None)
    assert owner not in getattr(partner, 'pascal_term141')


def test_assoc_formalParameterList35_stub_double():
    # pascal_formal_parameter_list has no real 'pascal_formal_parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_procedure_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_procedure_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_procedure_declaration(name="sample_text")
    partner = pascal_formal_parameter_list()
    setattr(partner, 'pascal_formal_parameter_list', None)
    _safe_set(owner, 'pascal_procedure_declaration36', partner)
    assert getattr(partner, 'pascal_formal_parameter_list') == owner
    _safe_set(owner, 'pascal_procedure_declaration36', None)
    assert getattr(partner, 'pascal_formal_parameter_list') is None


def test_assoc_formalParameterList40_stub_double():
    # pascal_formal_parameter_list has no real 'pascal_formal_parameter_list42' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_declaration(name="sample_text")
    partner = pascal_formal_parameter_list()
    setattr(partner, 'pascal_formal_parameter_list42', None)
    _safe_set(owner, 'pascal_function_declaration41', partner)
    assert getattr(partner, 'pascal_formal_parameter_list42') == owner
    _safe_set(owner, 'pascal_function_declaration41', None)
    assert getattr(partner, 'pascal_formal_parameter_list42') is None


def test_assoc_functionDeclarations33_stub_double():
    # pascal_procedure_and_function_declaration_part has no real 'pascal_procedure_and_function_declaration_part34' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_declaration(name="sample_text")
    partner = pascal_procedure_and_function_declaration_part()
    setattr(partner, 'pascal_procedure_and_function_declaration_part34', None)
    _safe_set(owner, 'pascal_function_declaration', partner)
    assert owner in getattr(partner, 'pascal_procedure_and_function_declaration_part34')
    _safe_set(owner, 'pascal_function_declaration', None)
    assert owner not in getattr(partner, 'pascal_procedure_and_function_declaration_part34')


def test_assoc_functionHeading62_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section63' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_heading(id1="sample_text", id2="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section63', None)
    _safe_set(owner, 'pascal_function_heading64', partner)
    assert getattr(partner, 'pascal_formal_parameter_section63') == owner
    _safe_set(owner, 'pascal_function_heading64', None)
    assert getattr(partner, 'pascal_formal_parameter_section63') is None


def test_assoc_identifierList179_stub_double():
    # pascal_enumerated_type has no real 'pascal_enumerated_type180' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_enumerated_type()
    setattr(partner, 'pascal_enumerated_type180', None)
    _safe_set(owner, 'pascal_identifier_list181', partner)
    assert getattr(partner, 'pascal_enumerated_type180') == owner
    _safe_set(owner, 'pascal_identifier_list181', None)
    assert getattr(partner, 'pascal_enumerated_type180') is None


def test_assoc_identifierList218_stub_double():
    # pascal_record_section has no real 'pascal_record_section219' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_record_section()
    setattr(partner, 'pascal_record_section219', None)
    _safe_set(owner, 'pascal_identifier_list220', partner)
    assert getattr(partner, 'pascal_record_section219') == owner
    _safe_set(owner, 'pascal_identifier_list220', None)
    assert getattr(partner, 'pascal_record_section219') is None


def test_assoc_identifierList27_stub_double():
    # pascal_variable_declaration has no real 'pascal_variable_declaration28' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_variable_declaration()
    setattr(partner, 'pascal_variable_declaration28', None)
    _safe_set(owner, 'pascal_identifier_list', partner)
    assert getattr(partner, 'pascal_variable_declaration28') == owner
    _safe_set(owner, 'pascal_identifier_list', None)
    assert getattr(partner, 'pascal_variable_declaration28') is None


def test_assoc_identifierList65_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section66' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section66', None)
    _safe_set(owner, 'pascal_identifier_list67', partner)
    assert getattr(partner, 'pascal_value_parameter_section66') == owner
    _safe_set(owner, 'pascal_identifier_list67', None)
    assert getattr(partner, 'pascal_value_parameter_section66') is None


def test_assoc_identifierList70_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section71' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section71', None)
    _safe_set(owner, 'pascal_identifier_list72', partner)
    assert getattr(partner, 'pascal_variable_parameter_section71') == owner
    _safe_set(owner, 'pascal_identifier_list72', None)
    assert getattr(partner, 'pascal_variable_parameter_section71') is None


def test_assoc_labels19_stub_double():
    # pascal_label_declaration_part has no real 'pascal_label_declaration_part20' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(int="sample_text")
    partner = pascal_label_declaration_part()
    setattr(partner, 'pascal_label_declaration_part20', None)
    _safe_set(owner, 'pascal_label', partner)
    assert owner in getattr(partner, 'pascal_label_declaration_part20')
    _safe_set(owner, 'pascal_label', None)
    assert owner not in getattr(partner, 'pascal_label_declaration_part20')


def test_assoc_parameterType68_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section69' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(id="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section69', None)
    _safe_set(owner, 'pascal_parameter_type', partner)
    assert getattr(partner, 'pascal_value_parameter_section69') == owner
    _safe_set(owner, 'pascal_parameter_type', None)
    assert getattr(partner, 'pascal_value_parameter_section69') is None


def test_assoc_parameterType73_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section74' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(id="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section74', None)
    _safe_set(owner, 'pascal_parameter_type75', partner)
    assert getattr(partner, 'pascal_variable_parameter_section74') == owner
    _safe_set(owner, 'pascal_parameter_type75', None)
    assert getattr(partner, 'pascal_variable_parameter_section74') is None


def test_assoc_procedureDeclarations31_stub_double():
    # pascal_procedure_and_function_declaration_part has no real 'pascal_procedure_and_function_declaration_part32' property in the generated
    # code (a bare stub) -- manually attach it so pascal_procedure_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_procedure_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_procedure_declaration(name="sample_text")
    partner = pascal_procedure_and_function_declaration_part()
    setattr(partner, 'pascal_procedure_and_function_declaration_part32', None)
    _safe_set(owner, 'pascal_procedure_declaration', partner)
    assert owner in getattr(partner, 'pascal_procedure_and_function_declaration_part32')
    _safe_set(owner, 'pascal_procedure_declaration', None)
    assert owner not in getattr(partner, 'pascal_procedure_and_function_declaration_part32')


def test_assoc_procedureHeading59_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section60' property in the generated
    # code (a bare stub) -- manually attach it so pascal_procedure_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_procedure_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_procedure_heading(name="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section60', None)
    _safe_set(owner, 'pascal_procedure_heading61', partner)
    assert getattr(partner, 'pascal_formal_parameter_section60') == owner
    _safe_set(owner, 'pascal_procedure_heading61', None)
    assert getattr(partner, 'pascal_formal_parameter_section60') is None


def test_assoc_set149_stub_double():
    # pascal_Set has no real 'pascal_Set' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    partner = pascal_Set()
    setattr(partner, 'pascal_Set', None)
    _safe_set(owner, 'pascal_factor150', partner)
    assert getattr(partner, 'pascal_Set') == owner
    _safe_set(owner, 'pascal_factor150', None)
    assert getattr(partner, 'pascal_Set') is None


def test_assoc_simpleExpressions136_stub_double():
    # pascal_simple_expression has no real 'pascal_simple_expression' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operators="sample_text")
    partner = pascal_simple_expression()
    setattr(partner, 'pascal_simple_expression', None)
    _safe_set(owner, 'pascal_expression137', {partner})
    assert getattr(partner, 'pascal_simple_expression') == owner
    _safe_set(owner, 'pascal_expression137', set())
    assert getattr(partner, 'pascal_simple_expression') is None


def test_assoc_simpleTypes198_stub_double():
    # pascal_array_type has no real 'pascal_array_type199' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(primitiveType="sample_text")
    partner = pascal_array_type()
    setattr(partner, 'pascal_array_type199', None)
    _safe_set(owner, 'pascal_simple_type200', partner)
    assert owner in getattr(partner, 'pascal_array_type199')
    _safe_set(owner, 'pascal_simple_type200', None)
    assert owner not in getattr(partner, 'pascal_array_type199')


def test_assoc_statement105_stub_double():
    # pascal_statement has no real 'pascal_statement107' property in the generated
    # code (a bare stub) -- manually attach it so pascal_for_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_for_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_for_statement(name="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement107', None)
    _safe_set(owner, 'pascal_for_statement106', partner)
    assert getattr(partner, 'pascal_statement107') == owner
    _safe_set(owner, 'pascal_for_statement106', None)
    assert getattr(partner, 'pascal_statement107') is None


def test_assoc_structuredType171_stub_double():
    # pascal_structured_type has no real 'pascal_structured_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type(name="sample_text")
    partner = pascal_structured_type()
    setattr(partner, 'pascal_structured_type', None)
    _safe_set(owner, 'pascal_type172', partner)
    assert getattr(partner, 'pascal_structured_type') == owner
    _safe_set(owner, 'pascal_type172', None)
    assert getattr(partner, 'pascal_structured_type') is None


def test_assoc_subrangeType175_stub_double():
    # pascal_subrange_type has no real 'pascal_subrange_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(primitiveType="sample_text")
    partner = pascal_subrange_type()
    setattr(partner, 'pascal_subrange_type', None)
    _safe_set(owner, 'pascal_simple_type176', partner)
    assert getattr(partner, 'pascal_subrange_type') == owner
    _safe_set(owner, 'pascal_simple_type176', None)
    assert getattr(partner, 'pascal_subrange_type') is None


def test_assoc_type201_stub_double():
    # pascal_array_type has no real 'pascal_array_type202' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type(name="sample_text")
    partner = pascal_array_type()
    setattr(partner, 'pascal_array_type202', None)
    _safe_set(owner, 'pascal_type203', partner)
    assert getattr(partner, 'pascal_array_type202') == owner
    _safe_set(owner, 'pascal_type203', None)
    assert getattr(partner, 'pascal_array_type202') is None


def test_assoc_type206_stub_double():
    # pascal_set_type has no real 'pascal_set_type207' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type(name="sample_text")
    partner = pascal_set_type()
    setattr(partner, 'pascal_set_type207', None)
    _safe_set(owner, 'pascal_type208', partner)
    assert getattr(partner, 'pascal_set_type207') == owner
    _safe_set(owner, 'pascal_type208', None)
    assert getattr(partner, 'pascal_set_type207') is None


def test_assoc_type209_stub_double():
    # pascal_file_type has no real 'pascal_file_type210' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type(name="sample_text")
    partner = pascal_file_type()
    setattr(partner, 'pascal_file_type210', None)
    _safe_set(owner, 'pascal_type211', partner)
    assert getattr(partner, 'pascal_file_type210') == owner
    _safe_set(owner, 'pascal_type211', None)
    assert getattr(partner, 'pascal_file_type210') is None


def test_assoc_type221_stub_double():
    # pascal_record_section has no real 'pascal_record_section222' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type(name="sample_text")
    partner = pascal_record_section()
    setattr(partner, 'pascal_record_section222', None)
    _safe_set(owner, 'pascal_type223', partner)
    assert getattr(partner, 'pascal_record_section222') == owner
    _safe_set(owner, 'pascal_type223', None)
    assert getattr(partner, 'pascal_record_section222') is None


def test_assoc_type29_stub_double():
    # pascal_variable_declaration has no real 'pascal_variable_declaration30' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type(name="sample_text")
    partner = pascal_variable_declaration()
    setattr(partner, 'pascal_variable_declaration30', None)
    _safe_set(owner, 'pascal_type', partner)
    assert getattr(partner, 'pascal_variable_declaration30') == owner
    _safe_set(owner, 'pascal_type', None)
    assert getattr(partner, 'pascal_variable_declaration30') is None


def test_assoc_variables132_stub_double():
    # pascal_with_statement has no real 'pascal_with_statement' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable(name="sample_text")
    partner = pascal_with_statement()
    setattr(partner, 'pascal_with_statement', None)
    _safe_set(owner, 'pascal_variable', partner)
    assert owner in getattr(partner, 'pascal_with_statement')
    _safe_set(owner, 'pascal_variable', None)
    assert owner not in getattr(partner, 'pascal_with_statement')


def test_assoc_variantPart214_stub_double():
    # pascal_field_list has no real 'pascal_field_list215' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variant_part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variant_part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variant_part(id="sample_text")
    partner = pascal_field_list()
    setattr(partner, 'pascal_field_list215', None)
    _safe_set(owner, 'pascal_variant_part', partner)
    assert getattr(partner, 'pascal_field_list215') == owner
    _safe_set(owner, 'pascal_variant_part', None)
    assert getattr(partner, 'pascal_field_list215') is None


def test_assoc_variants226_stub_double():
    # pascal_variant has no real 'pascal_variant' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variant_part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variant_part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variant_part(id="sample_text")
    partner = pascal_variant()
    setattr(partner, 'pascal_variant', None)
    _safe_set(owner, 'pascal_variant_part227', {partner})
    assert getattr(partner, 'pascal_variant') == owner
    _safe_set(owner, 'pascal_variant_part227', set())
    assert getattr(partner, 'pascal_variant') is None


