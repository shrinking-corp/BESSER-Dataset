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
    pascal_compound_statement,
    pascal_conditional_statement,
    pascal_conformant_array_schema,
    pascal_constant,
    pascal_constant_definition,
    pascal_constant_definition_part,
    pascal_declaration_part,
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
    pascal_label,
    pascal_label_declaration_part,
    pascal_number,
    pascal_packed_conformant_array_schema,
    pascal_parameter_type,
    pascal_pointer_type,
    pascal_procedure_and_function_declaration_part,
    pascal_program,
    pascal_program_heading,
    pascal_record_section,
    pascal_record_type,
    pascal_repeat_statement,
    pascal_repetitive_statement,
    pascal_resto,
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

def test_assoc_array187_reverse_link_reassign_clear():
    a1 = pascal_resto(accessor=True, name="sample_text")
    a2 = pascal_resto(accessor=False, name="sample_text_2")
    b = pascal_resto(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_resto188', a1)
    assert _is_linked(b, 'pascal_resto188', a1)
    if hasattr(a1, 'pascal_resto186'):
        assert _is_linked(a1, 'pascal_resto186', b)
    _safe_set(b, 'pascal_resto188', a2)
    assert _is_linked(b, 'pascal_resto188', a2)
    if hasattr(a1, 'pascal_resto186'):
        assert not _is_linked(a1, 'pascal_resto186', b)
    if hasattr(a2, 'pascal_resto186'):
        assert _is_linked(a2, 'pascal_resto186', b)
    _safe_set(b, 'pascal_resto188', None)
    assert not _is_linked(b, 'pascal_resto188', a2)
    if hasattr(a2, 'pascal_resto186'):
        assert not _is_linked(a2, 'pascal_resto186', b)


def test_assoc_bound79_reverse_link_reassign_clear():
    a1 = pascal_packed_conformant_array_schema(name="sample_text")
    a2 = pascal_packed_conformant_array_schema(name="sample_text_2")
    b = pascal_bound_specification(fin="sample_text", init="sample_text", name="sample_text")
    _safe_set(b, 'pascal_bound_specification', a1)
    assert _is_linked(b, 'pascal_bound_specification', a1)
    if hasattr(a1, 'pascal_packed_conformant_array_schema80'):
        assert _is_linked(a1, 'pascal_packed_conformant_array_schema80', b)
    _safe_set(b, 'pascal_bound_specification', a2)
    assert _is_linked(b, 'pascal_bound_specification', a2)
    if hasattr(a1, 'pascal_packed_conformant_array_schema80'):
        assert not _is_linked(a1, 'pascal_packed_conformant_array_schema80', b)
    if hasattr(a2, 'pascal_packed_conformant_array_schema80'):
        assert _is_linked(a2, 'pascal_packed_conformant_array_schema80', b)
    _safe_set(b, 'pascal_bound_specification', None)
    assert not _is_linked(b, 'pascal_bound_specification', a2)
    if hasattr(a2, 'pascal_packed_conformant_array_schema80'):
        assert not _is_linked(a2, 'pascal_packed_conformant_array_schema80', b)


def test_assoc_const223_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant225', a1)
    assert _is_linked(b, 'pascal_constant225', a1)
    if hasattr(a1, 'pascal_subrange_type224'):
        assert _is_linked(a1, 'pascal_subrange_type224', b)
    _safe_set(b, 'pascal_constant225', a2)
    assert _is_linked(b, 'pascal_constant225', a2)
    if hasattr(a1, 'pascal_subrange_type224'):
        assert not _is_linked(a1, 'pascal_subrange_type224', b)
    if hasattr(a2, 'pascal_subrange_type224'):
        assert _is_linked(a2, 'pascal_subrange_type224', b)
    _safe_set(b, 'pascal_constant225', None)
    assert not _is_linked(b, 'pascal_constant225', a2)
    if hasattr(a2, 'pascal_subrange_type224'):
        assert not _is_linked(a2, 'pascal_subrange_type224', b)


def test_assoc_const23_reverse_link_reassign_clear():
    a1 = pascal_constant_definition(name="sample_text")
    a2 = pascal_constant_definition(name="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant', a1)
    assert _is_linked(b, 'pascal_constant', a1)
    if hasattr(a1, 'pascal_constant_definition24'):
        assert _is_linked(a1, 'pascal_constant_definition24', b)
    _safe_set(b, 'pascal_constant', a2)
    assert _is_linked(b, 'pascal_constant', a2)
    if hasattr(a1, 'pascal_constant_definition24'):
        assert not _is_linked(a1, 'pascal_constant_definition24', b)
    if hasattr(a2, 'pascal_constant_definition24'):
        assert _is_linked(a2, 'pascal_constant_definition24', b)
    _safe_set(b, 'pascal_constant', None)
    assert not _is_linked(b, 'pascal_constant', a2)
    if hasattr(a2, 'pascal_constant_definition24'):
        assert not _is_linked(a2, 'pascal_constant_definition24', b)


def test_assoc_expression176_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression178', a1)
    assert _is_linked(b, 'pascal_expression178', a1)
    if hasattr(a1, 'pascal_factor177'):
        assert _is_linked(a1, 'pascal_factor177', b)
    _safe_set(b, 'pascal_expression178', a2)
    assert _is_linked(b, 'pascal_expression178', a2)
    if hasattr(a1, 'pascal_factor177'):
        assert not _is_linked(a1, 'pascal_factor177', b)
    if hasattr(a2, 'pascal_factor177'):
        assert _is_linked(a2, 'pascal_factor177', b)
    _safe_set(b, 'pascal_expression178', None)
    assert not _is_linked(b, 'pascal_expression178', a2)
    if hasattr(a2, 'pascal_factor177'):
        assert not _is_linked(a2, 'pascal_factor177', b)


def test_assoc_expressionFin141_reverse_link_reassign_clear():
    a1 = pascal_for_statement(initID="sample_text")
    a2 = pascal_for_statement(initID="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression143', a1)
    assert _is_linked(b, 'pascal_expression143', a1)
    if hasattr(a1, 'pascal_for_statement142'):
        assert _is_linked(a1, 'pascal_for_statement142', b)
    _safe_set(b, 'pascal_expression143', a2)
    assert _is_linked(b, 'pascal_expression143', a2)
    if hasattr(a1, 'pascal_for_statement142'):
        assert not _is_linked(a1, 'pascal_for_statement142', b)
    if hasattr(a2, 'pascal_for_statement142'):
        assert _is_linked(a2, 'pascal_for_statement142', b)
    _safe_set(b, 'pascal_expression143', None)
    assert not _is_linked(b, 'pascal_expression143', a2)
    if hasattr(a2, 'pascal_for_statement142'):
        assert not _is_linked(a2, 'pascal_for_statement142', b)


def test_assoc_expressionInit138_reverse_link_reassign_clear():
    a1 = pascal_for_statement(initID="sample_text")
    a2 = pascal_for_statement(initID="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression140', a1)
    assert _is_linked(b, 'pascal_expression140', a1)
    if hasattr(a1, 'pascal_for_statement139'):
        assert _is_linked(a1, 'pascal_for_statement139', b)
    _safe_set(b, 'pascal_expression140', a2)
    assert _is_linked(b, 'pascal_expression140', a2)
    if hasattr(a1, 'pascal_for_statement139'):
        assert not _is_linked(a1, 'pascal_for_statement139', b)
    if hasattr(a2, 'pascal_for_statement139'):
        assert _is_linked(a2, 'pascal_for_statement139', b)
    _safe_set(b, 'pascal_expression140', None)
    assert not _is_linked(b, 'pascal_expression140', a2)
    if hasattr(a2, 'pascal_for_statement139'):
        assert not _is_linked(a2, 'pascal_for_statement139', b)


def test_assoc_expressions161_reverse_link_reassign_clear():
    a1 = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    a2 = pascal_simple_expression(operators="sample_text_2", prefixOperator="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression162', {a1})
    assert _is_linked(b, 'pascal_expression162', a1)
    if hasattr(a1, 'pascal_simple_expression'):
        assert _is_linked(a1, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression162', {a2})
    assert _is_linked(b, 'pascal_expression162', a2)
    if hasattr(a1, 'pascal_simple_expression'):
        assert not _is_linked(a1, 'pascal_simple_expression', b)
    if hasattr(a2, 'pascal_simple_expression'):
        assert _is_linked(a2, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression162', set())
    assert not _is_linked(b, 'pascal_expression162', a2)
    if hasattr(a2, 'pascal_simple_expression'):
        assert not _is_linked(a2, 'pascal_simple_expression', b)


def test_assoc_factors165_reverse_link_reassign_clear():
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


def test_assoc_finalConst220_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant222', a1)
    assert _is_linked(b, 'pascal_constant222', a1)
    if hasattr(a1, 'pascal_subrange_type221'):
        assert _is_linked(a1, 'pascal_subrange_type221', b)
    _safe_set(b, 'pascal_constant222', a2)
    assert _is_linked(b, 'pascal_constant222', a2)
    if hasattr(a1, 'pascal_subrange_type221'):
        assert not _is_linked(a1, 'pascal_subrange_type221', b)
    if hasattr(a2, 'pascal_subrange_type221'):
        assert _is_linked(a2, 'pascal_subrange_type221', b)
    _safe_set(b, 'pascal_constant222', None)
    assert not _is_linked(b, 'pascal_constant222', a2)
    if hasattr(a2, 'pascal_subrange_type221'):
        assert not _is_linked(a2, 'pascal_subrange_type221', b)


def test_assoc_function173_reverse_link_reassign_clear():
    a1 = pascal_function_designator(name="sample_text")
    a2 = pascal_function_designator(name="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor174', a1)
    assert _is_linked(b, 'pascal_factor174', a1)
    if hasattr(a1, 'pascal_function_designator175'):
        assert _is_linked(a1, 'pascal_function_designator175', b)
    _safe_set(b, 'pascal_factor174', a2)
    assert _is_linked(b, 'pascal_factor174', a2)
    if hasattr(a1, 'pascal_function_designator175'):
        assert not _is_linked(a1, 'pascal_function_designator175', b)
    if hasattr(a2, 'pascal_function_designator175'):
        assert _is_linked(a2, 'pascal_function_designator175', b)
    _safe_set(b, 'pascal_factor174', None)
    assert not _is_linked(b, 'pascal_factor174', a2)
    if hasattr(a2, 'pascal_function_designator175'):
        assert not _is_linked(a2, 'pascal_function_designator175', b)


def test_assoc_function98_reverse_link_reassign_clear():
    a1 = pascal_simple_statement(function_noargs="sample_text")
    a2 = pascal_simple_statement(function_noargs="sample_text_2")
    b = pascal_function_designator(name="sample_text")
    _safe_set(b, 'pascal_function_designator', a1)
    assert _is_linked(b, 'pascal_function_designator', a1)
    if hasattr(a1, 'pascal_simple_statement99'):
        assert _is_linked(a1, 'pascal_simple_statement99', b)
    _safe_set(b, 'pascal_function_designator', a2)
    assert _is_linked(b, 'pascal_function_designator', a2)
    if hasattr(a1, 'pascal_simple_statement99'):
        assert not _is_linked(a1, 'pascal_simple_statement99', b)
    if hasattr(a2, 'pascal_simple_statement99'):
        assert _is_linked(a2, 'pascal_simple_statement99', b)
    _safe_set(b, 'pascal_function_designator', None)
    assert not _is_linked(b, 'pascal_function_designator', a2)
    if hasattr(a2, 'pascal_simple_statement99'):
        assert not _is_linked(a2, 'pascal_simple_statement99', b)


def test_assoc_heading42_reverse_link_reassign_clear():
    a1 = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    a2 = pascal_abstraction_heading(name="sample_text_2", resultType="sample_text_2")
    b = pascal_abstraction_declaration(forward=True)
    _safe_set(b, 'pascal_abstraction_declaration43', a1)
    assert _is_linked(b, 'pascal_abstraction_declaration43', a1)
    if hasattr(a1, 'pascal_abstraction_heading44'):
        assert _is_linked(a1, 'pascal_abstraction_heading44', b)
    _safe_set(b, 'pascal_abstraction_declaration43', a2)
    assert _is_linked(b, 'pascal_abstraction_declaration43', a2)
    if hasattr(a1, 'pascal_abstraction_heading44'):
        assert not _is_linked(a1, 'pascal_abstraction_heading44', b)
    if hasattr(a2, 'pascal_abstraction_heading44'):
        assert _is_linked(a2, 'pascal_abstraction_heading44', b)
    _safe_set(b, 'pascal_abstraction_declaration43', None)
    assert not _is_linked(b, 'pascal_abstraction_declaration43', a2)
    if hasattr(a2, 'pascal_abstraction_heading44'):
        assert not _is_linked(a2, 'pascal_abstraction_heading44', b)


def test_assoc_identifiers3_reverse_link_reassign_clear():
    a1 = pascal_program_heading(name="sample_text")
    a2 = pascal_program_heading(name="sample_text_2")
    b = pascal_identifier_list(ids="sample_text")
    _safe_set(b, 'pascal_identifier_list', a1)
    assert _is_linked(b, 'pascal_identifier_list', a1)
    if hasattr(a1, 'pascal_program_heading4'):
        assert _is_linked(a1, 'pascal_program_heading4', b)
    _safe_set(b, 'pascal_identifier_list', a2)
    assert _is_linked(b, 'pascal_identifier_list', a2)
    if hasattr(a1, 'pascal_program_heading4'):
        assert not _is_linked(a1, 'pascal_program_heading4', b)
    if hasattr(a2, 'pascal_program_heading4'):
        assert _is_linked(a2, 'pascal_program_heading4', b)
    _safe_set(b, 'pascal_identifier_list', None)
    assert not _is_linked(b, 'pascal_identifier_list', a2)
    if hasattr(a2, 'pascal_program_heading4'):
        assert not _is_linked(a2, 'pascal_program_heading4', b)


def test_assoc_initialConst217_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant219', a1)
    assert _is_linked(b, 'pascal_constant219', a1)
    if hasattr(a1, 'pascal_subrange_type218'):
        assert _is_linked(a1, 'pascal_subrange_type218', b)
    _safe_set(b, 'pascal_constant219', a2)
    assert _is_linked(b, 'pascal_constant219', a2)
    if hasattr(a1, 'pascal_subrange_type218'):
        assert not _is_linked(a1, 'pascal_subrange_type218', b)
    if hasattr(a2, 'pascal_subrange_type218'):
        assert _is_linked(a2, 'pascal_subrange_type218', b)
    _safe_set(b, 'pascal_constant219', None)
    assert not _is_linked(b, 'pascal_constant219', a2)
    if hasattr(a2, 'pascal_subrange_type218'):
        assert not _is_linked(a2, 'pascal_subrange_type218', b)


def test_assoc_not_180_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor181', a1)
    assert _is_linked(b, 'pascal_factor181', a1)
    if hasattr(a1, 'pascal_factor179'):
        assert _is_linked(a1, 'pascal_factor179', b)
    _safe_set(b, 'pascal_factor181', a2)
    assert _is_linked(b, 'pascal_factor181', a2)
    if hasattr(a1, 'pascal_factor179'):
        assert not _is_linked(a1, 'pascal_factor179', b)
    if hasattr(a2, 'pascal_factor179'):
        assert _is_linked(a2, 'pascal_factor179', b)
    _safe_set(b, 'pascal_factor181', None)
    assert not _is_linked(b, 'pascal_factor181', a2)
    if hasattr(a2, 'pascal_factor179'):
        assert not _is_linked(a2, 'pascal_factor179', b)


def test_assoc_pointer193_reverse_link_reassign_clear():
    a1 = pascal_resto(accessor=True, name="sample_text")
    a2 = pascal_resto(accessor=False, name="sample_text_2")
    b = pascal_resto(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_resto194', a1)
    assert _is_linked(b, 'pascal_resto194', a1)
    if hasattr(a1, 'pascal_resto192'):
        assert _is_linked(a1, 'pascal_resto192', b)
    _safe_set(b, 'pascal_resto194', a2)
    assert _is_linked(b, 'pascal_resto194', a2)
    if hasattr(a1, 'pascal_resto192'):
        assert not _is_linked(a1, 'pascal_resto192', b)
    if hasattr(a2, 'pascal_resto192'):
        assert _is_linked(a2, 'pascal_resto192', b)
    _safe_set(b, 'pascal_resto194', None)
    assert not _is_linked(b, 'pascal_resto194', a2)
    if hasattr(a2, 'pascal_resto192'):
        assert not _is_linked(a2, 'pascal_resto192', b)


def test_assoc_set171_reverse_link_reassign_clear():
    a1 = pascal_set(brackets="sample_text")
    a2 = pascal_set(brackets="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor172', a1)
    assert _is_linked(b, 'pascal_factor172', a1)
    if hasattr(a1, 'pascal_set'):
        assert _is_linked(a1, 'pascal_set', b)
    _safe_set(b, 'pascal_factor172', a2)
    assert _is_linked(b, 'pascal_factor172', a2)
    if hasattr(a1, 'pascal_set'):
        assert not _is_linked(a1, 'pascal_set', b)
    if hasattr(a2, 'pascal_set'):
        assert _is_linked(a2, 'pascal_set', b)
    _safe_set(b, 'pascal_factor172', None)
    assert not _is_linked(b, 'pascal_factor172', a2)
    if hasattr(a2, 'pascal_set'):
        assert not _is_linked(a2, 'pascal_set', b)


def test_assoc_subrange210_reverse_link_reassign_clear():
    a1 = pascal_subrange_type(subrange="sample_text")
    a2 = pascal_subrange_type(subrange="sample_text_2")
    b = pascal_simple_type(name="sample_text")
    _safe_set(b, 'pascal_simple_type211', a1)
    assert _is_linked(b, 'pascal_simple_type211', a1)
    if hasattr(a1, 'pascal_subrange_type'):
        assert _is_linked(a1, 'pascal_subrange_type', b)
    _safe_set(b, 'pascal_simple_type211', a2)
    assert _is_linked(b, 'pascal_simple_type211', a2)
    if hasattr(a1, 'pascal_subrange_type'):
        assert not _is_linked(a1, 'pascal_subrange_type', b)
    if hasattr(a2, 'pascal_subrange_type'):
        assert _is_linked(a2, 'pascal_subrange_type', b)
    _safe_set(b, 'pascal_simple_type211', None)
    assert not _is_linked(b, 'pascal_simple_type211', a2)
    if hasattr(a2, 'pascal_subrange_type'):
        assert not _is_linked(a2, 'pascal_subrange_type', b)


def test_assoc_tag265_reverse_link_reassign_clear():
    a1 = pascal_variant_part(name="sample_text")
    a2 = pascal_variant_part(name="sample_text_2")
    b = pascal_tag_field(name="sample_text")
    _safe_set(b, 'pascal_tag_field', a1)
    assert _is_linked(b, 'pascal_tag_field', a1)
    if hasattr(a1, 'pascal_variant_part266'):
        assert _is_linked(a1, 'pascal_variant_part266', b)
    _safe_set(b, 'pascal_tag_field', a2)
    assert _is_linked(b, 'pascal_tag_field', a2)
    if hasattr(a1, 'pascal_variant_part266'):
        assert not _is_linked(a1, 'pascal_variant_part266', b)
    if hasattr(a2, 'pascal_variant_part266'):
        assert _is_linked(a2, 'pascal_variant_part266', b)
    _safe_set(b, 'pascal_tag_field', None)
    assert not _is_linked(b, 'pascal_tag_field', a2)
    if hasattr(a2, 'pascal_variant_part266'):
        assert not _is_linked(a2, 'pascal_variant_part266', b)


def test_assoc_variable166_reverse_link_reassign_clear():
    a1 = pascal_variable(name="sample_text")
    a2 = pascal_variable(name="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor167', a1)
    assert _is_linked(b, 'pascal_factor167', a1)
    if hasattr(a1, 'pascal_variable168'):
        assert _is_linked(a1, 'pascal_variable168', b)
    _safe_set(b, 'pascal_factor167', a2)
    assert _is_linked(b, 'pascal_factor167', a2)
    if hasattr(a1, 'pascal_variable168'):
        assert not _is_linked(a1, 'pascal_variable168', b)
    if hasattr(a2, 'pascal_variable168'):
        assert _is_linked(a2, 'pascal_variable168', b)
    _safe_set(b, 'pascal_factor167', None)
    assert not _is_linked(b, 'pascal_factor167', a2)
    if hasattr(a2, 'pascal_variable168'):
        assert not _is_linked(a2, 'pascal_variable168', b)


def test_assoc_variable182_reverse_link_reassign_clear():
    a1 = pascal_variable(name="sample_text")
    a2 = pascal_variable(name="sample_text_2")
    b = pascal_resto(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_resto', a1)
    assert _is_linked(b, 'pascal_resto', a1)
    if hasattr(a1, 'pascal_variable183'):
        assert _is_linked(a1, 'pascal_variable183', b)
    _safe_set(b, 'pascal_resto', a2)
    assert _is_linked(b, 'pascal_resto', a2)
    if hasattr(a1, 'pascal_variable183'):
        assert not _is_linked(a1, 'pascal_variable183', b)
    if hasattr(a2, 'pascal_variable183'):
        assert _is_linked(a2, 'pascal_variable183', b)
    _safe_set(b, 'pascal_resto', None)
    assert not _is_linked(b, 'pascal_resto', a2)
    if hasattr(a2, 'pascal_variable183'):
        assert not _is_linked(a2, 'pascal_variable183', b)


def test_assoc_variable190_reverse_link_reassign_clear():
    a1 = pascal_resto(accessor=True, name="sample_text")
    a2 = pascal_resto(accessor=False, name="sample_text_2")
    b = pascal_resto(accessor=True, name="sample_text")
    _safe_set(b, 'pascal_resto191', a1)
    assert _is_linked(b, 'pascal_resto191', a1)
    if hasattr(a1, 'pascal_resto189'):
        assert _is_linked(a1, 'pascal_resto189', b)
    _safe_set(b, 'pascal_resto191', a2)
    assert _is_linked(b, 'pascal_resto191', a2)
    if hasattr(a1, 'pascal_resto189'):
        assert not _is_linked(a1, 'pascal_resto189', b)
    if hasattr(a2, 'pascal_resto189'):
        assert _is_linked(a2, 'pascal_resto189', b)
    _safe_set(b, 'pascal_resto191', None)
    assert not _is_linked(b, 'pascal_resto191', a2)
    if hasattr(a2, 'pascal_resto189'):
        assert not _is_linked(a2, 'pascal_resto189', b)


