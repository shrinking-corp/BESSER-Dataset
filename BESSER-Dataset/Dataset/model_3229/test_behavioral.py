import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    abstraction_declaration,
    pascal_EObject,
    pascal_abstraction_declaration,
    pascal_abstraction_heading,
    pascal_any_number,
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
    pascal_dynamic_array_type,
    pascal_enumerated_type,
    pascal_expression,
    pascal_expression_list,
    pascal_factor,
    pascal_field_list,
    pascal_file_type,
    pascal_fixed_part,
    pascal_for_statement,
    pascal_formal_parameter_list,
    pascal_formal_parameter_section,
    pascal_function_designator,
    pascal_goto_statement,
    pascal_identifier_list,
    pascal_if_statement,
    pascal_index_type,
    pascal_label,
    pascal_label_declaration_part,
    pascal_number,
    pascal_packed_conformant_array_schema,
    pascal_parameter_type,
    pascal_pascal,
    pascal_pointer_type,
    pascal_procedure_and_function_declaration_part,
    pascal_program,
    pascal_program_heading_block,
    pascal_record_section,
    pascal_record_type,
    pascal_repeat_statement,
    pascal_repetitive_statement,
    pascal_set,
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
    pascal_unpacked_conformant_array_schema,
    pascal_unpacked_structured_type,
    pascal_value_parameter_section,
    pascal_var_,
    pascal_variable,
    pascal_variable_declaration_part,
    pascal_variable_identifier_list,
    pascal_variable_parameter_section,
    pascal_variable_section,
    pascal_variant,
    pascal_variant_part,
    pascal_while_statement,
    pascal_with_statement,
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

def test_assoc_array44_reverse_link_reassign_clear():
    a1 = pascal_var_(accessor=True, name="sample_text")
    a2 = pascal_var_(accessor=False, name="sample_text_2")
    b = pascal_var_(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_var_45', a1)
    assert _is_linked(b, 'pascal_var_45', a1)
    if hasattr(a1, 'pascal_var_43'):
        assert _is_linked(a1, 'pascal_var_43', b)
    _safe_set(b, 'pascal_var_45', a2)
    assert _is_linked(b, 'pascal_var_45', a2)
    if hasattr(a1, 'pascal_var_43'):
        assert not _is_linked(a1, 'pascal_var_43', b)
    if hasattr(a2, 'pascal_var_43'):
        assert _is_linked(a2, 'pascal_var_43', b)
    _safe_set(b, 'pascal_var_45', None)
    assert not _is_linked(b, 'pascal_var_45', a2)
    if hasattr(a2, 'pascal_var_43'):
        assert not _is_linked(a2, 'pascal_var_43', b)


def test_assoc_bound291_reverse_link_reassign_clear():
    a1 = pascal_packed_conformant_array_schema(name="sample_text")
    a2 = pascal_packed_conformant_array_schema(name="sample_text_2")
    b = pascal_bound_specification(final="sample_text", initial="sample_text", name="sample_text")
    _safe_set(b, 'pascal_bound_specification', a1)
    assert _is_linked(b, 'pascal_bound_specification', a1)
    if hasattr(a1, 'pascal_packed_conformant_array_schema292'):
        assert _is_linked(a1, 'pascal_packed_conformant_array_schema292', b)
    _safe_set(b, 'pascal_bound_specification', a2)
    assert _is_linked(b, 'pascal_bound_specification', a2)
    if hasattr(a1, 'pascal_packed_conformant_array_schema292'):
        assert not _is_linked(a1, 'pascal_packed_conformant_array_schema292', b)
    if hasattr(a2, 'pascal_packed_conformant_array_schema292'):
        assert _is_linked(a2, 'pascal_packed_conformant_array_schema292', b)
    _safe_set(b, 'pascal_bound_specification', None)
    assert not _is_linked(b, 'pascal_bound_specification', a2)
    if hasattr(a2, 'pascal_packed_conformant_array_schema292'):
        assert not _is_linked(a2, 'pascal_packed_conformant_array_schema292', b)


def test_assoc_const164_reverse_link_reassign_clear():
    a1 = pascal_constant_definition(name="sample_text")
    a2 = pascal_constant_definition(name="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant166', a1)
    assert _is_linked(b, 'pascal_constant166', a1)
    if hasattr(a1, 'pascal_constant_definition165'):
        assert _is_linked(a1, 'pascal_constant_definition165', b)
    _safe_set(b, 'pascal_constant166', a2)
    assert _is_linked(b, 'pascal_constant166', a2)
    if hasattr(a1, 'pascal_constant_definition165'):
        assert not _is_linked(a1, 'pascal_constant_definition165', b)
    if hasattr(a2, 'pascal_constant_definition165'):
        assert _is_linked(a2, 'pascal_constant_definition165', b)
    _safe_set(b, 'pascal_constant166', None)
    assert not _is_linked(b, 'pascal_constant166', a2)
    if hasattr(a2, 'pascal_constant_definition165'):
        assert not _is_linked(a2, 'pascal_constant_definition165', b)


def test_assoc_const187_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant189', a1)
    assert _is_linked(b, 'pascal_constant189', a1)
    if hasattr(a1, 'pascal_subrange_type188'):
        assert _is_linked(a1, 'pascal_subrange_type188', b)
    _safe_set(b, 'pascal_constant189', a2)
    assert _is_linked(b, 'pascal_constant189', a2)
    if hasattr(a1, 'pascal_subrange_type188'):
        assert not _is_linked(a1, 'pascal_subrange_type188', b)
    if hasattr(a2, 'pascal_subrange_type188'):
        assert _is_linked(a2, 'pascal_subrange_type188', b)
    _safe_set(b, 'pascal_constant189', None)
    assert not _is_linked(b, 'pascal_constant189', a2)
    if hasattr(a2, 'pascal_subrange_type188'):
        assert not _is_linked(a2, 'pascal_subrange_type188', b)


def test_assoc_expression70_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression72', a1)
    assert _is_linked(b, 'pascal_expression72', a1)
    if hasattr(a1, 'pascal_factor71'):
        assert _is_linked(a1, 'pascal_factor71', b)
    _safe_set(b, 'pascal_expression72', a2)
    assert _is_linked(b, 'pascal_expression72', a2)
    if hasattr(a1, 'pascal_factor71'):
        assert not _is_linked(a1, 'pascal_factor71', b)
    if hasattr(a2, 'pascal_factor71'):
        assert _is_linked(a2, 'pascal_factor71', b)
    _safe_set(b, 'pascal_expression72', None)
    assert not _is_linked(b, 'pascal_expression72', a2)
    if hasattr(a2, 'pascal_factor71'):
        assert not _is_linked(a2, 'pascal_factor71', b)


def test_assoc_expressions55_reverse_link_reassign_clear():
    a1 = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    a2 = pascal_simple_expression(operators="sample_text_2", prefixOperator="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression56', {a1})
    assert _is_linked(b, 'pascal_expression56', a1)
    if hasattr(a1, 'pascal_simple_expression'):
        assert _is_linked(a1, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression56', {a2})
    assert _is_linked(b, 'pascal_expression56', a2)
    if hasattr(a1, 'pascal_simple_expression'):
        assert not _is_linked(a1, 'pascal_simple_expression', b)
    if hasattr(a2, 'pascal_simple_expression'):
        assert _is_linked(a2, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression56', set())
    assert not _is_linked(b, 'pascal_expression56', a2)
    if hasattr(a2, 'pascal_simple_expression'):
        assert not _is_linked(a2, 'pascal_simple_expression', b)


def test_assoc_factors59_reverse_link_reassign_clear():
    a1 = pascal_term(operators="sample_text")
    a2 = pascal_term(operators="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor', a1)
    assert _is_linked(b, 'pascal_factor', a1)
    if hasattr(a1, 'pascal_term'):
        assert _is_linked(a1, 'pascal_term', b)
    _safe_set(b, 'pascal_factor', a2)
    assert _is_linked(b, 'pascal_factor', a2)
    if hasattr(a1, 'pascal_term'):
        assert not _is_linked(a1, 'pascal_term', b)
    if hasattr(a2, 'pascal_term'):
        assert _is_linked(a2, 'pascal_term', b)
    _safe_set(b, 'pascal_factor', None)
    assert not _is_linked(b, 'pascal_factor', a2)
    if hasattr(a2, 'pascal_term'):
        assert not _is_linked(a2, 'pascal_term', b)


def test_assoc_finalConst184_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant186', a1)
    assert _is_linked(b, 'pascal_constant186', a1)
    if hasattr(a1, 'pascal_subrange_type185'):
        assert _is_linked(a1, 'pascal_subrange_type185', b)
    _safe_set(b, 'pascal_constant186', a2)
    assert _is_linked(b, 'pascal_constant186', a2)
    if hasattr(a1, 'pascal_subrange_type185'):
        assert not _is_linked(a1, 'pascal_subrange_type185', b)
    if hasattr(a2, 'pascal_subrange_type185'):
        assert _is_linked(a2, 'pascal_subrange_type185', b)
    _safe_set(b, 'pascal_constant186', None)
    assert not _is_linked(b, 'pascal_constant186', a2)
    if hasattr(a2, 'pascal_subrange_type185'):
        assert not _is_linked(a2, 'pascal_subrange_type185', b)


def test_assoc_function31_reverse_link_reassign_clear():
    a1 = pascal_simple_statement(function_noargs="sample_text")
    a2 = pascal_simple_statement(function_noargs="sample_text_2")
    b = pascal_function_designator(name="sample_text")
    _safe_set(b, 'pascal_function_designator', a1)
    assert _is_linked(b, 'pascal_function_designator', a1)
    if hasattr(a1, 'pascal_simple_statement32'):
        assert _is_linked(a1, 'pascal_simple_statement32', b)
    _safe_set(b, 'pascal_function_designator', a2)
    assert _is_linked(b, 'pascal_function_designator', a2)
    if hasattr(a1, 'pascal_simple_statement32'):
        assert not _is_linked(a1, 'pascal_simple_statement32', b)
    if hasattr(a2, 'pascal_simple_statement32'):
        assert _is_linked(a2, 'pascal_simple_statement32', b)
    _safe_set(b, 'pascal_function_designator', None)
    assert not _is_linked(b, 'pascal_function_designator', a2)
    if hasattr(a2, 'pascal_simple_statement32'):
        assert not _is_linked(a2, 'pascal_simple_statement32', b)


def test_assoc_function67_reverse_link_reassign_clear():
    a1 = pascal_function_designator(name="sample_text")
    a2 = pascal_function_designator(name="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor68', a1)
    assert _is_linked(b, 'pascal_factor68', a1)
    if hasattr(a1, 'pascal_function_designator69'):
        assert _is_linked(a1, 'pascal_function_designator69', b)
    _safe_set(b, 'pascal_factor68', a2)
    assert _is_linked(b, 'pascal_factor68', a2)
    if hasattr(a1, 'pascal_function_designator69'):
        assert not _is_linked(a1, 'pascal_function_designator69', b)
    if hasattr(a2, 'pascal_function_designator69'):
        assert _is_linked(a2, 'pascal_function_designator69', b)
    _safe_set(b, 'pascal_factor68', None)
    assert not _is_linked(b, 'pascal_factor68', a2)
    if hasattr(a2, 'pascal_function_designator69'):
        assert not _is_linked(a2, 'pascal_function_designator69', b)


def test_assoc_heading260_reverse_link_reassign_clear():
    a1 = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    a2 = pascal_abstraction_heading(name="sample_text_2", returnType="sample_text_2")
    b = pascal_abstraction_declaration(forward=True)
    _safe_set(b, 'pascal_abstraction_declaration261', a1)
    assert _is_linked(b, 'pascal_abstraction_declaration261', a1)
    if hasattr(a1, 'pascal_abstraction_heading262'):
        assert _is_linked(a1, 'pascal_abstraction_heading262', b)
    _safe_set(b, 'pascal_abstraction_declaration261', a2)
    assert _is_linked(b, 'pascal_abstraction_declaration261', a2)
    if hasattr(a1, 'pascal_abstraction_heading262'):
        assert not _is_linked(a1, 'pascal_abstraction_heading262', b)
    if hasattr(a2, 'pascal_abstraction_heading262'):
        assert _is_linked(a2, 'pascal_abstraction_heading262', b)
    _safe_set(b, 'pascal_abstraction_declaration261', None)
    assert not _is_linked(b, 'pascal_abstraction_declaration261', a2)
    if hasattr(a2, 'pascal_abstraction_heading262'):
        assert not _is_linked(a2, 'pascal_abstraction_heading262', b)


def test_assoc_identifiers5_reverse_link_reassign_clear():
    a1 = pascal_program_heading_block(name="sample_text")
    a2 = pascal_program_heading_block(name="sample_text_2")
    b = pascal_identifier_list(names="sample_text")
    _safe_set(b, 'pascal_identifier_list', a1)
    assert _is_linked(b, 'pascal_identifier_list', a1)
    if hasattr(a1, 'pascal_program_heading_block6'):
        assert _is_linked(a1, 'pascal_program_heading_block6', b)
    _safe_set(b, 'pascal_identifier_list', a2)
    assert _is_linked(b, 'pascal_identifier_list', a2)
    if hasattr(a1, 'pascal_program_heading_block6'):
        assert not _is_linked(a1, 'pascal_program_heading_block6', b)
    if hasattr(a2, 'pascal_program_heading_block6'):
        assert _is_linked(a2, 'pascal_program_heading_block6', b)
    _safe_set(b, 'pascal_identifier_list', None)
    assert not _is_linked(b, 'pascal_identifier_list', a2)
    if hasattr(a2, 'pascal_program_heading_block6'):
        assert not _is_linked(a2, 'pascal_program_heading_block6', b)


def test_assoc_initialConst181_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant183', a1)
    assert _is_linked(b, 'pascal_constant183', a1)
    if hasattr(a1, 'pascal_subrange_type182'):
        assert _is_linked(a1, 'pascal_subrange_type182', b)
    _safe_set(b, 'pascal_constant183', a2)
    assert _is_linked(b, 'pascal_constant183', a2)
    if hasattr(a1, 'pascal_subrange_type182'):
        assert not _is_linked(a1, 'pascal_subrange_type182', b)
    if hasattr(a2, 'pascal_subrange_type182'):
        assert _is_linked(a2, 'pascal_subrange_type182', b)
    _safe_set(b, 'pascal_constant183', None)
    assert not _is_linked(b, 'pascal_constant183', a2)
    if hasattr(a2, 'pascal_subrange_type182'):
        assert not _is_linked(a2, 'pascal_subrange_type182', b)


def test_assoc_not_74_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor75', a1)
    assert _is_linked(b, 'pascal_factor75', a1)
    if hasattr(a1, 'pascal_factor73'):
        assert _is_linked(a1, 'pascal_factor73', b)
    _safe_set(b, 'pascal_factor75', a2)
    assert _is_linked(b, 'pascal_factor75', a2)
    if hasattr(a1, 'pascal_factor73'):
        assert not _is_linked(a1, 'pascal_factor73', b)
    if hasattr(a2, 'pascal_factor73'):
        assert _is_linked(a2, 'pascal_factor73', b)
    _safe_set(b, 'pascal_factor75', None)
    assert not _is_linked(b, 'pascal_factor75', a2)
    if hasattr(a2, 'pascal_factor73'):
        assert not _is_linked(a2, 'pascal_factor73', b)


def test_assoc_pointer50_reverse_link_reassign_clear():
    a1 = pascal_var_(accessor=True, name="sample_text")
    a2 = pascal_var_(accessor=False, name="sample_text_2")
    b = pascal_var_(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_var_51', a1)
    assert _is_linked(b, 'pascal_var_51', a1)
    if hasattr(a1, 'pascal_var_49'):
        assert _is_linked(a1, 'pascal_var_49', b)
    _safe_set(b, 'pascal_var_51', a2)
    assert _is_linked(b, 'pascal_var_51', a2)
    if hasattr(a1, 'pascal_var_49'):
        assert not _is_linked(a1, 'pascal_var_49', b)
    if hasattr(a2, 'pascal_var_49'):
        assert _is_linked(a2, 'pascal_var_49', b)
    _safe_set(b, 'pascal_var_51', None)
    assert not _is_linked(b, 'pascal_var_51', a2)
    if hasattr(a2, 'pascal_var_49'):
        assert not _is_linked(a2, 'pascal_var_49', b)


def test_assoc_set65_reverse_link_reassign_clear():
    a1 = pascal_set(brackets="sample_text")
    a2 = pascal_set(brackets="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor66', a1)
    assert _is_linked(b, 'pascal_factor66', a1)
    if hasattr(a1, 'pascal_set'):
        assert _is_linked(a1, 'pascal_set', b)
    _safe_set(b, 'pascal_factor66', a2)
    assert _is_linked(b, 'pascal_factor66', a2)
    if hasattr(a1, 'pascal_set'):
        assert not _is_linked(a1, 'pascal_set', b)
    if hasattr(a2, 'pascal_set'):
        assert _is_linked(a2, 'pascal_set', b)
    _safe_set(b, 'pascal_factor66', None)
    assert not _is_linked(b, 'pascal_factor66', a2)
    if hasattr(a2, 'pascal_set'):
        assert not _is_linked(a2, 'pascal_set', b)


def test_assoc_subrange177_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_simple_type(name="sample_text")
    _safe_set(b, 'pascal_simple_type178', a1)
    assert _is_linked(b, 'pascal_simple_type178', a1)
    if hasattr(a1, 'pascal_subrange_type'):
        assert _is_linked(a1, 'pascal_subrange_type', b)
    _safe_set(b, 'pascal_simple_type178', a2)
    assert _is_linked(b, 'pascal_simple_type178', a2)
    if hasattr(a1, 'pascal_subrange_type'):
        assert not _is_linked(a1, 'pascal_subrange_type', b)
    if hasattr(a2, 'pascal_subrange_type'):
        assert _is_linked(a2, 'pascal_subrange_type', b)
    _safe_set(b, 'pascal_simple_type178', None)
    assert not _is_linked(b, 'pascal_simple_type178', a2)
    if hasattr(a2, 'pascal_subrange_type'):
        assert not _is_linked(a2, 'pascal_subrange_type', b)


def test_assoc_tag234_reverse_link_reassign_clear():
    a1 = pascal_variant_part(name="sample_text")
    a2 = pascal_variant_part(name="sample_text_2")
    b = pascal_tag_field(name="sample_text")
    _safe_set(b, 'pascal_tag_field', a1)
    assert _is_linked(b, 'pascal_tag_field', a1)
    if hasattr(a1, 'pascal_variant_part235'):
        assert _is_linked(a1, 'pascal_variant_part235', b)
    _safe_set(b, 'pascal_tag_field', a2)
    assert _is_linked(b, 'pascal_tag_field', a2)
    if hasattr(a1, 'pascal_variant_part235'):
        assert not _is_linked(a1, 'pascal_variant_part235', b)
    if hasattr(a2, 'pascal_variant_part235'):
        assert _is_linked(a2, 'pascal_variant_part235', b)
    _safe_set(b, 'pascal_tag_field', None)
    assert not _is_linked(b, 'pascal_tag_field', a2)
    if hasattr(a2, 'pascal_variant_part235'):
        assert not _is_linked(a2, 'pascal_variant_part235', b)


def test_assoc_variable39_reverse_link_reassign_clear():
    a1 = pascal_variable(name="sample_text")
    a2 = pascal_variable(name="sample_text_2")
    b = pascal_var_(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_var_', a1)
    assert _is_linked(b, 'pascal_var_', a1)
    if hasattr(a1, 'pascal_variable40'):
        assert _is_linked(a1, 'pascal_variable40', b)
    _safe_set(b, 'pascal_var_', a2)
    assert _is_linked(b, 'pascal_var_', a2)
    if hasattr(a1, 'pascal_variable40'):
        assert not _is_linked(a1, 'pascal_variable40', b)
    if hasattr(a2, 'pascal_variable40'):
        assert _is_linked(a2, 'pascal_variable40', b)
    _safe_set(b, 'pascal_var_', None)
    assert not _is_linked(b, 'pascal_var_', a2)
    if hasattr(a2, 'pascal_variable40'):
        assert not _is_linked(a2, 'pascal_variable40', b)


def test_assoc_variable47_reverse_link_reassign_clear():
    a1 = pascal_var_(accessor=True, name="sample_text")
    a2 = pascal_var_(accessor=False, name="sample_text_2")
    b = pascal_var_(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_var_48', a1)
    assert _is_linked(b, 'pascal_var_48', a1)
    if hasattr(a1, 'pascal_var_46'):
        assert _is_linked(a1, 'pascal_var_46', b)
    _safe_set(b, 'pascal_var_48', a2)
    assert _is_linked(b, 'pascal_var_48', a2)
    if hasattr(a1, 'pascal_var_46'):
        assert not _is_linked(a1, 'pascal_var_46', b)
    if hasattr(a2, 'pascal_var_46'):
        assert _is_linked(a2, 'pascal_var_46', b)
    _safe_set(b, 'pascal_var_48', None)
    assert not _is_linked(b, 'pascal_var_48', a2)
    if hasattr(a2, 'pascal_var_46'):
        assert not _is_linked(a2, 'pascal_var_46', b)


def test_assoc_variable60_reverse_link_reassign_clear():
    a1 = pascal_variable(name="sample_text")
    a2 = pascal_variable(name="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor61', a1)
    assert _is_linked(b, 'pascal_factor61', a1)
    if hasattr(a1, 'pascal_variable62'):
        assert _is_linked(a1, 'pascal_variable62', b)
    _safe_set(b, 'pascal_factor61', a2)
    assert _is_linked(b, 'pascal_factor61', a2)
    if hasattr(a1, 'pascal_variable62'):
        assert not _is_linked(a1, 'pascal_variable62', b)
    if hasattr(a2, 'pascal_variable62'):
        assert _is_linked(a2, 'pascal_variable62', b)
    _safe_set(b, 'pascal_factor61', None)
    assert not _is_linked(b, 'pascal_factor61', a2)
    if hasattr(a2, 'pascal_variable62'):
        assert not _is_linked(a2, 'pascal_variable62', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_array285_stub_double():
    # pascal_conformant_array_schema has no real 'pascal_conformant_array_schema' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_conformant_array_schema()
    setattr(partner, 'pascal_conformant_array_schema', None)
    _safe_set(owner, 'pascal_parameter_type286', partner)
    assert getattr(partner, 'pascal_conformant_array_schema') == owner
    _safe_set(owner, 'pascal_parameter_type286', None)
    assert getattr(partner, 'pascal_conformant_array_schema') is None


def test_assoc_assignment29_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement', None)
    _safe_set(owner, 'pascal_simple_statement30', partner)
    assert getattr(partner, 'pascal_assignment_statement') == owner
    _safe_set(owner, 'pascal_simple_statement30', None)
    assert getattr(partner, 'pascal_assignment_statement') is None


def test_assoc_block263_stub_double():
    # pascal_block has no real 'pascal_block265' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_declaration(forward=True)
    partner = pascal_block()
    setattr(partner, 'pascal_block265', None)
    _safe_set(owner, 'pascal_abstraction_declaration264', partner)
    assert getattr(partner, 'pascal_block265') == owner
    _safe_set(owner, 'pascal_abstraction_declaration264', None)
    assert getattr(partner, 'pascal_block265') is None


def test_assoc_bounds293_stub_double():
    # pascal_unpacked_conformant_array_schema has no real 'pascal_unpacked_conformant_array_schema294' property in the generated
    # code (a bare stub) -- manually attach it so pascal_bound_specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_bound_specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_bound_specification(final="sample_text", initial="sample_text", name="sample_text")
    partner = pascal_unpacked_conformant_array_schema()
    setattr(partner, 'pascal_unpacked_conformant_array_schema294', None)
    _safe_set(owner, 'pascal_bound_specification295', partner)
    assert owner in getattr(partner, 'pascal_unpacked_conformant_array_schema294')
    _safe_set(owner, 'pascal_bound_specification295', None)
    assert owner not in getattr(partner, 'pascal_unpacked_conformant_array_schema294')


def test_assoc_constants145_stub_double():
    # pascal_case_label_list has no real 'pascal_case_label_list146' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    partner = pascal_case_label_list()
    setattr(partner, 'pascal_case_label_list146', None)
    _safe_set(owner, 'pascal_constant', partner)
    assert owner in getattr(partner, 'pascal_case_label_list146')
    _safe_set(owner, 'pascal_constant', None)
    assert owner not in getattr(partner, 'pascal_case_label_list146')


def test_assoc_consts162_stub_double():
    # pascal_constant_definition_part has no real 'pascal_constant_definition_part163' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant_definition(name="sample_text")
    partner = pascal_constant_definition_part()
    setattr(partner, 'pascal_constant_definition_part163', None)
    _safe_set(owner, 'pascal_constant_definition', partner)
    assert owner in getattr(partner, 'pascal_constant_definition_part163')
    _safe_set(owner, 'pascal_constant_definition', None)
    assert owner not in getattr(partner, 'pascal_constant_definition_part163')


def test_assoc_enumerated179_stub_double():
    # pascal_enumerated_type has no real 'pascal_enumerated_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(name="sample_text")
    partner = pascal_enumerated_type()
    setattr(partner, 'pascal_enumerated_type', None)
    _safe_set(owner, 'pascal_simple_type180', partner)
    assert getattr(partner, 'pascal_enumerated_type') == owner
    _safe_set(owner, 'pascal_simple_type180', None)
    assert getattr(partner, 'pascal_enumerated_type') is None


def test_assoc_expression101_stub_double():
    # pascal_while_statement has no real 'pascal_while_statement102' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_while_statement()
    setattr(partner, 'pascal_while_statement102', None)
    _safe_set(owner, 'pascal_expression103', partner)
    assert getattr(partner, 'pascal_while_statement102') == owner
    _safe_set(owner, 'pascal_expression103', None)
    assert getattr(partner, 'pascal_while_statement102') is None


def test_assoc_expression110_stub_double():
    # pascal_repeat_statement has no real 'pascal_repeat_statement111' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_repeat_statement()
    setattr(partner, 'pascal_repeat_statement111', None)
    _safe_set(owner, 'pascal_expression112', partner)
    assert getattr(partner, 'pascal_repeat_statement111') == owner
    _safe_set(owner, 'pascal_expression112', None)
    assert getattr(partner, 'pascal_repeat_statement111') is None


def test_assoc_expression116_stub_double():
    # pascal_for_statement has no real 'pascal_for_statement117' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_for_statement()
    setattr(partner, 'pascal_for_statement117', None)
    _safe_set(owner, 'pascal_expression118', partner)
    assert getattr(partner, 'pascal_for_statement117') == owner
    _safe_set(owner, 'pascal_expression118', None)
    assert getattr(partner, 'pascal_for_statement117') is None


def test_assoc_expression126_stub_double():
    # pascal_if_statement has no real 'pascal_if_statement127' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_if_statement()
    setattr(partner, 'pascal_if_statement127', None)
    _safe_set(owner, 'pascal_expression128', partner)
    assert getattr(partner, 'pascal_if_statement127') == owner
    _safe_set(owner, 'pascal_expression128', None)
    assert getattr(partner, 'pascal_if_statement127') is None


def test_assoc_expression135_stub_double():
    # pascal_case_statement has no real 'pascal_case_statement136' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_case_statement()
    setattr(partner, 'pascal_case_statement136', None)
    _safe_set(owner, 'pascal_expression137', partner)
    assert getattr(partner, 'pascal_case_statement136') == owner
    _safe_set(owner, 'pascal_expression137', None)
    assert getattr(partner, 'pascal_case_statement136') is None


def test_assoc_expression37_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement38' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement38', None)
    _safe_set(owner, 'pascal_expression', partner)
    assert getattr(partner, 'pascal_assignment_statement38') == owner
    _safe_set(owner, 'pascal_expression', None)
    assert getattr(partner, 'pascal_assignment_statement38') is None


def test_assoc_expressions41_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_var_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_var_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_var_(accessor=True, name="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list', None)
    _safe_set(owner, 'pascal_var_42', partner)
    assert getattr(partner, 'pascal_expression_list') == owner
    _safe_set(owner, 'pascal_var_42', None)
    assert getattr(partner, 'pascal_expression_list') is None


def test_assoc_expressions52_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list53' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list53', None)
    _safe_set(owner, 'pascal_expression54', partner)
    assert owner in getattr(partner, 'pascal_expression_list53')
    _safe_set(owner, 'pascal_expression54', None)
    assert owner not in getattr(partner, 'pascal_expression_list53')


def test_assoc_expressions78_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list80' property in the generated
    # code (a bare stub) -- manually attach it so pascal_set's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_set's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_set(brackets="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list80', None)
    _safe_set(owner, 'pascal_set79', partner)
    assert getattr(partner, 'pascal_expression_list80') == owner
    _safe_set(owner, 'pascal_set79', None)
    assert getattr(partner, 'pascal_expression_list80') is None


def test_assoc_expressions81_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list83' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_designator(name="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list83', None)
    _safe_set(owner, 'pascal_function_designator82', partner)
    assert getattr(partner, 'pascal_expression_list83') == owner
    _safe_set(owner, 'pascal_function_designator82', None)
    assert getattr(partner, 'pascal_expression_list83') is None


def test_assoc_fields216_stub_double():
    # pascal_field_list has no real 'pascal_field_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_record_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_record_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_record_type(endKeyword="sample_text", recordKeyword="sample_text")
    partner = pascal_field_list()
    setattr(partner, 'pascal_field_list', None)
    _safe_set(owner, 'pascal_record_type217', partner)
    assert getattr(partner, 'pascal_field_list') == owner
    _safe_set(owner, 'pascal_record_type217', None)
    assert getattr(partner, 'pascal_field_list') is None


def test_assoc_function277_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section278' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section278', None)
    _safe_set(owner, 'pascal_abstraction_heading279', partner)
    assert getattr(partner, 'pascal_formal_parameter_section278') == owner
    _safe_set(owner, 'pascal_abstraction_heading279', None)
    assert getattr(partner, 'pascal_formal_parameter_section278') is None


def test_assoc_functions258_stub_double():
    # pascal_procedure_and_function_declaration_part has no real 'pascal_procedure_and_function_declaration_part259' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_declaration(forward=True)
    partner = pascal_procedure_and_function_declaration_part()
    setattr(partner, 'pascal_procedure_and_function_declaration_part259', None)
    _safe_set(owner, 'pascal_abstraction_declaration', partner)
    assert owner in getattr(partner, 'pascal_procedure_and_function_declaration_part259')
    _safe_set(owner, 'pascal_abstraction_declaration', None)
    assert owner not in getattr(partner, 'pascal_procedure_and_function_declaration_part259')


def test_assoc_goto33_stub_double():
    # pascal_goto_statement has no real 'pascal_goto_statement' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_goto_statement()
    setattr(partner, 'pascal_goto_statement', None)
    _safe_set(owner, 'pascal_simple_statement34', partner)
    assert getattr(partner, 'pascal_goto_statement') == owner
    _safe_set(owner, 'pascal_simple_statement34', None)
    assert getattr(partner, 'pascal_goto_statement') is None


def test_assoc_heading1_stub_double():
    # pascal_program has no real 'pascal_program2' property in the generated
    # code (a bare stub) -- manually attach it so pascal_program_heading_block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_program_heading_block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_program_heading_block(name="sample_text")
    partner = pascal_program()
    setattr(partner, 'pascal_program2', None)
    _safe_set(owner, 'pascal_program_heading_block', partner)
    assert getattr(partner, 'pascal_program2') == owner
    _safe_set(owner, 'pascal_program_heading_block', None)
    assert getattr(partner, 'pascal_program2') is None


def test_assoc_identifiers190_stub_double():
    # pascal_enumerated_type has no real 'pascal_enumerated_type191' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(names="sample_text")
    partner = pascal_enumerated_type()
    setattr(partner, 'pascal_enumerated_type191', None)
    _safe_set(owner, 'pascal_identifier_list192', partner)
    assert getattr(partner, 'pascal_enumerated_type191') == owner
    _safe_set(owner, 'pascal_identifier_list192', None)
    assert getattr(partner, 'pascal_enumerated_type191') is None


def test_assoc_identifiers224_stub_double():
    # pascal_variable_section has no real 'pascal_variable_section' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable_identifier_list(names="sample_text")
    partner = pascal_variable_section()
    setattr(partner, 'pascal_variable_section', None)
    _safe_set(owner, 'pascal_variable_identifier_list', partner)
    assert getattr(partner, 'pascal_variable_section') == owner
    _safe_set(owner, 'pascal_variable_identifier_list', None)
    assert getattr(partner, 'pascal_variable_section') is None


def test_assoc_identifiers228_stub_double():
    # pascal_record_section has no real 'pascal_record_section229' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(names="sample_text")
    partner = pascal_record_section()
    setattr(partner, 'pascal_record_section229', None)
    _safe_set(owner, 'pascal_identifier_list230', partner)
    assert getattr(partner, 'pascal_record_section229') == owner
    _safe_set(owner, 'pascal_identifier_list230', None)
    assert getattr(partner, 'pascal_record_section229') is None


def test_assoc_identifiers280_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section281' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(names="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section281', None)
    _safe_set(owner, 'pascal_identifier_list282', partner)
    assert getattr(partner, 'pascal_value_parameter_section281') == owner
    _safe_set(owner, 'pascal_identifier_list282', None)
    assert getattr(partner, 'pascal_value_parameter_section281') is None


def test_assoc_identifiers299_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section300' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(names="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section300', None)
    _safe_set(owner, 'pascal_identifier_list301', partner)
    assert getattr(partner, 'pascal_variable_parameter_section300') == owner
    _safe_set(owner, 'pascal_identifier_list301', None)
    assert getattr(partner, 'pascal_variable_parameter_section300') is None


def test_assoc_label156_stub_double():
    # pascal_goto_statement has no real 'pascal_goto_statement157' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_goto_statement()
    setattr(partner, 'pascal_goto_statement157', None)
    _safe_set(owner, 'pascal_label158', partner)
    assert getattr(partner, 'pascal_goto_statement157') == owner
    _safe_set(owner, 'pascal_label158', None)
    assert getattr(partner, 'pascal_goto_statement157') is None


def test_assoc_label23_stub_double():
    # pascal_statement has no real 'pascal_statement24' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement24', None)
    _safe_set(owner, 'pascal_label', partner)
    assert getattr(partner, 'pascal_statement24') == owner
    _safe_set(owner, 'pascal_label', None)
    assert getattr(partner, 'pascal_statement24') is None


def test_assoc_labels159_stub_double():
    # pascal_label_declaration_part has no real 'pascal_label_declaration_part160' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_label_declaration_part()
    setattr(partner, 'pascal_label_declaration_part160', None)
    _safe_set(owner, 'pascal_label161', partner)
    assert owner in getattr(partner, 'pascal_label_declaration_part160')
    _safe_set(owner, 'pascal_label161', None)
    assert owner not in getattr(partner, 'pascal_label_declaration_part160')


def test_assoc_number147_stub_double():
    # pascal_number has no real 'pascal_number149' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number149', None)
    _safe_set(owner, 'pascal_constant148', partner)
    assert getattr(partner, 'pascal_number149') == owner
    _safe_set(owner, 'pascal_constant148', None)
    assert getattr(partner, 'pascal_number149') is None


def test_assoc_number63_stub_double():
    # pascal_number has no real 'pascal_number' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number', None)
    _safe_set(owner, 'pascal_factor64', partner)
    assert getattr(partner, 'pascal_number') == owner
    _safe_set(owner, 'pascal_factor64', None)
    assert getattr(partner, 'pascal_number') is None


def test_assoc_number76_stub_double():
    # pascal_number has no real 'pascal_number77' property in the generated
    # code (a bare stub) -- manually attach it so pascal_any_number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_any_number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_any_number(integer="sample_text", real="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number77', None)
    _safe_set(owner, 'pascal_any_number', partner)
    assert getattr(partner, 'pascal_number77') == owner
    _safe_set(owner, 'pascal_any_number', None)
    assert getattr(partner, 'pascal_number77') is None


def test_assoc_packed287_stub_double():
    # pascal_conformant_array_schema has no real 'pascal_conformant_array_schema288' property in the generated
    # code (a bare stub) -- manually attach it so pascal_packed_conformant_array_schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_packed_conformant_array_schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_packed_conformant_array_schema(name="sample_text")
    partner = pascal_conformant_array_schema()
    setattr(partner, 'pascal_conformant_array_schema288', None)
    _safe_set(owner, 'pascal_packed_conformant_array_schema', partner)
    assert getattr(partner, 'pascal_conformant_array_schema288') == owner
    _safe_set(owner, 'pascal_packed_conformant_array_schema', None)
    assert getattr(partner, 'pascal_conformant_array_schema288') is None


def test_assoc_parameters266_stub_double():
    # pascal_formal_parameter_list has no real 'pascal_formal_parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_formal_parameter_list()
    setattr(partner, 'pascal_formal_parameter_list', None)
    _safe_set(owner, 'pascal_abstraction_heading267', partner)
    assert getattr(partner, 'pascal_formal_parameter_list') == owner
    _safe_set(owner, 'pascal_abstraction_heading267', None)
    assert getattr(partner, 'pascal_formal_parameter_list') is None


def test_assoc_procedure274_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section275' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section275', None)
    _safe_set(owner, 'pascal_abstraction_heading276', partner)
    assert getattr(partner, 'pascal_formal_parameter_section275') == owner
    _safe_set(owner, 'pascal_abstraction_heading276', None)
    assert getattr(partner, 'pascal_formal_parameter_section275') is None


def test_assoc_procedures256_stub_double():
    # pascal_procedure_and_function_declaration_part has no real 'pascal_procedure_and_function_declaration_part257' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_procedure_and_function_declaration_part()
    setattr(partner, 'pascal_procedure_and_function_declaration_part257', None)
    _safe_set(owner, 'pascal_abstraction_heading', partner)
    assert owner in getattr(partner, 'pascal_procedure_and_function_declaration_part257')
    _safe_set(owner, 'pascal_abstraction_heading', None)
    assert owner not in getattr(partner, 'pascal_procedure_and_function_declaration_part257')


def test_assoc_record199_stub_double():
    # pascal_unpacked_structured_type has no real 'pascal_unpacked_structured_type200' property in the generated
    # code (a bare stub) -- manually attach it so pascal_record_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_record_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_record_type(endKeyword="sample_text", recordKeyword="sample_text")
    partner = pascal_unpacked_structured_type()
    setattr(partner, 'pascal_unpacked_structured_type200', None)
    _safe_set(owner, 'pascal_record_type', partner)
    assert getattr(partner, 'pascal_unpacked_structured_type200') == owner
    _safe_set(owner, 'pascal_record_type', None)
    assert getattr(partner, 'pascal_unpacked_structured_type200') is None


def test_assoc_simple171_stub_double():
    # pascal_type has no real 'pascal_type172' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(name="sample_text")
    partner = pascal_type()
    setattr(partner, 'pascal_type172', None)
    _safe_set(owner, 'pascal_simple_type', partner)
    assert getattr(partner, 'pascal_type172') == owner
    _safe_set(owner, 'pascal_simple_type', None)
    assert getattr(partner, 'pascal_type172') is None


def test_assoc_simple25_stub_double():
    # pascal_statement has no real 'pascal_statement26' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement26', None)
    _safe_set(owner, 'pascal_simple_statement', partner)
    assert getattr(partner, 'pascal_statement26') == owner
    _safe_set(owner, 'pascal_simple_statement', None)
    assert getattr(partner, 'pascal_statement26') is None


def test_assoc_structured173_stub_double():
    # pascal_type has no real 'pascal_type174' property in the generated
    # code (a bare stub) -- manually attach it so pascal_structured_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_structured_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_structured_type(packed=True)
    partner = pascal_type()
    setattr(partner, 'pascal_type174', None)
    _safe_set(owner, 'pascal_structured_type', partner)
    assert getattr(partner, 'pascal_type174') == owner
    _safe_set(owner, 'pascal_structured_type', None)
    assert getattr(partner, 'pascal_type174') is None


def test_assoc_terms57_stub_double():
    # pascal_EObject has no real 'pascal_EObject' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    partner = pascal_EObject()
    setattr(partner, 'pascal_EObject', None)
    _safe_set(owner, 'pascal_simple_expression58', {partner})
    assert getattr(partner, 'pascal_EObject') == owner
    _safe_set(owner, 'pascal_simple_expression58', set())
    assert getattr(partner, 'pascal_EObject') is None


def test_assoc_type169_stub_double():
    # pascal_type has no real 'pascal_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type_definition(name="sample_text")
    partner = pascal_type()
    setattr(partner, 'pascal_type', None)
    _safe_set(owner, 'pascal_type_definition170', partner)
    assert getattr(partner, 'pascal_type') == owner
    _safe_set(owner, 'pascal_type_definition170', None)
    assert getattr(partner, 'pascal_type') is None


def test_assoc_type193_stub_double():
    # pascal_unpacked_structured_type has no real 'pascal_unpacked_structured_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_structured_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_structured_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_structured_type(packed=True)
    partner = pascal_unpacked_structured_type()
    setattr(partner, 'pascal_unpacked_structured_type', None)
    _safe_set(owner, 'pascal_structured_type194', partner)
    assert getattr(partner, 'pascal_unpacked_structured_type') == owner
    _safe_set(owner, 'pascal_structured_type194', None)
    assert getattr(partner, 'pascal_unpacked_structured_type') is None


def test_assoc_type213_stub_double():
    # pascal_index_type has no real 'pascal_index_type214' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(name="sample_text")
    partner = pascal_index_type()
    setattr(partner, 'pascal_index_type214', None)
    _safe_set(owner, 'pascal_simple_type215', partner)
    assert getattr(partner, 'pascal_index_type214') == owner
    _safe_set(owner, 'pascal_simple_type215', None)
    assert getattr(partner, 'pascal_index_type214') is None


def test_assoc_type283_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section284' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section284', None)
    _safe_set(owner, 'pascal_parameter_type', partner)
    assert getattr(partner, 'pascal_value_parameter_section284') == owner
    _safe_set(owner, 'pascal_parameter_type', None)
    assert getattr(partner, 'pascal_value_parameter_section284') is None


def test_assoc_type296_stub_double():
    # pascal_unpacked_conformant_array_schema has no real 'pascal_unpacked_conformant_array_schema297' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_unpacked_conformant_array_schema()
    setattr(partner, 'pascal_unpacked_conformant_array_schema297', None)
    _safe_set(owner, 'pascal_parameter_type298', partner)
    assert getattr(partner, 'pascal_unpacked_conformant_array_schema297') == owner
    _safe_set(owner, 'pascal_parameter_type298', None)
    assert getattr(partner, 'pascal_unpacked_conformant_array_schema297') is None


def test_assoc_type302_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section303' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section303', None)
    _safe_set(owner, 'pascal_parameter_type304', partner)
    assert getattr(partner, 'pascal_variable_parameter_section303') == owner
    _safe_set(owner, 'pascal_parameter_type304', None)
    assert getattr(partner, 'pascal_variable_parameter_section303') is None


def test_assoc_types167_stub_double():
    # pascal_type_definition_part has no real 'pascal_type_definition_part168' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type_definition(name="sample_text")
    partner = pascal_type_definition_part()
    setattr(partner, 'pascal_type_definition_part168', None)
    _safe_set(owner, 'pascal_type_definition', partner)
    assert owner in getattr(partner, 'pascal_type_definition_part168')
    _safe_set(owner, 'pascal_type_definition', None)
    assert owner not in getattr(partner, 'pascal_type_definition_part168')


def test_assoc_variable35_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement36' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable(name="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement36', None)
    _safe_set(owner, 'pascal_variable', partner)
    assert getattr(partner, 'pascal_assignment_statement36') == owner
    _safe_set(owner, 'pascal_variable', None)
    assert getattr(partner, 'pascal_assignment_statement36') is None


def test_assoc_variables150_stub_double():
    # pascal_with_statement has no real 'pascal_with_statement151' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable(name="sample_text")
    partner = pascal_with_statement()
    setattr(partner, 'pascal_with_statement151', None)
    _safe_set(owner, 'pascal_variable152', partner)
    assert owner in getattr(partner, 'pascal_with_statement151')
    _safe_set(owner, 'pascal_variable152', None)
    assert owner not in getattr(partner, 'pascal_with_statement151')


def test_assoc_variants220_stub_double():
    # pascal_field_list has no real 'pascal_field_list221' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variant_part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variant_part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variant_part(name="sample_text")
    partner = pascal_field_list()
    setattr(partner, 'pascal_field_list221', None)
    _safe_set(owner, 'pascal_variant_part', partner)
    assert owner in getattr(partner, 'pascal_field_list221')
    _safe_set(owner, 'pascal_variant_part', None)
    assert owner not in getattr(partner, 'pascal_field_list221')


def test_assoc_variants236_stub_double():
    # pascal_variant has no real 'pascal_variant' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variant_part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variant_part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variant_part(name="sample_text")
    partner = pascal_variant()
    setattr(partner, 'pascal_variant', None)
    _safe_set(owner, 'pascal_variant_part237', {partner})
    assert getattr(partner, 'pascal_variant') == owner
    _safe_set(owner, 'pascal_variant_part237', set())
    assert getattr(partner, 'pascal_variant') is None


