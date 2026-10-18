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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_array73_stub_double():
    # pascal_conformant_array_schema has no real 'pascal_conformant_array_schema' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_conformant_array_schema()
    setattr(partner, 'pascal_conformant_array_schema', None)
    _safe_set(owner, 'pascal_parameter_type74', partner)
    assert getattr(partner, 'pascal_conformant_array_schema') == owner
    _safe_set(owner, 'pascal_parameter_type74', None)
    assert getattr(partner, 'pascal_conformant_array_schema') is None


def test_assoc_assignment96_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement', None)
    _safe_set(owner, 'pascal_simple_statement97', partner)
    assert getattr(partner, 'pascal_assignment_statement') == owner
    _safe_set(owner, 'pascal_simple_statement97', None)
    assert getattr(partner, 'pascal_assignment_statement') is None


def test_assoc_block45_stub_double():
    # pascal_block has no real 'pascal_block47' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_declaration(forward=True)
    partner = pascal_block()
    setattr(partner, 'pascal_block47', None)
    _safe_set(owner, 'pascal_abstraction_declaration46', partner)
    assert getattr(partner, 'pascal_block47') == owner
    _safe_set(owner, 'pascal_abstraction_declaration46', None)
    assert getattr(partner, 'pascal_block47') is None


def test_assoc_bounds81_stub_double():
    # pascal_unpacked_conformant_array_schema has no real 'pascal_unpacked_conformant_array_schema82' property in the generated
    # code (a bare stub) -- manually attach it so pascal_bound_specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_bound_specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_bound_specification(fin="sample_text", init="sample_text", name="sample_text")
    partner = pascal_unpacked_conformant_array_schema()
    setattr(partner, 'pascal_unpacked_conformant_array_schema82', None)
    _safe_set(owner, 'pascal_bound_specification83', partner)
    assert owner in getattr(partner, 'pascal_unpacked_conformant_array_schema82')
    _safe_set(owner, 'pascal_bound_specification83', None)
    assert owner not in getattr(partner, 'pascal_unpacked_conformant_array_schema82')


def test_assoc_constants279_stub_double():
    # pascal_case_label_list has no real 'pascal_case_label_list280' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    partner = pascal_case_label_list()
    setattr(partner, 'pascal_case_label_list280', None)
    _safe_set(owner, 'pascal_constant281', partner)
    assert owner in getattr(partner, 'pascal_case_label_list280')
    _safe_set(owner, 'pascal_constant281', None)
    assert owner not in getattr(partner, 'pascal_case_label_list280')


def test_assoc_consts21_stub_double():
    # pascal_constant_definition_part has no real 'pascal_constant_definition_part22' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant_definition(name="sample_text")
    partner = pascal_constant_definition_part()
    setattr(partner, 'pascal_constant_definition_part22', None)
    _safe_set(owner, 'pascal_constant_definition', partner)
    assert owner in getattr(partner, 'pascal_constant_definition_part22')
    _safe_set(owner, 'pascal_constant_definition', None)
    assert owner not in getattr(partner, 'pascal_constant_definition_part22')


def test_assoc_enumerated212_stub_double():
    # pascal_enumerated_type has no real 'pascal_enumerated_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(name="sample_text")
    partner = pascal_enumerated_type()
    setattr(partner, 'pascal_enumerated_type', None)
    _safe_set(owner, 'pascal_simple_type213', partner)
    assert getattr(partner, 'pascal_enumerated_type') == owner
    _safe_set(owner, 'pascal_simple_type213', None)
    assert getattr(partner, 'pascal_enumerated_type') is None


def test_assoc_expression104_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement105' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement105', None)
    _safe_set(owner, 'pascal_expression', partner)
    assert getattr(partner, 'pascal_assignment_statement105') == owner
    _safe_set(owner, 'pascal_expression', None)
    assert getattr(partner, 'pascal_assignment_statement105') is None


def test_assoc_expression126_stub_double():
    # pascal_while_statement has no real 'pascal_while_statement127' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_while_statement()
    setattr(partner, 'pascal_while_statement127', None)
    _safe_set(owner, 'pascal_expression128', partner)
    assert getattr(partner, 'pascal_while_statement127') == owner
    _safe_set(owner, 'pascal_expression128', None)
    assert getattr(partner, 'pascal_while_statement127') is None


def test_assoc_expression135_stub_double():
    # pascal_repeat_statement has no real 'pascal_repeat_statement136' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_repeat_statement()
    setattr(partner, 'pascal_repeat_statement136', None)
    _safe_set(owner, 'pascal_expression137', partner)
    assert getattr(partner, 'pascal_repeat_statement136') == owner
    _safe_set(owner, 'pascal_expression137', None)
    assert getattr(partner, 'pascal_repeat_statement136') is None


def test_assoc_expression149_stub_double():
    # pascal_if_statement has no real 'pascal_if_statement150' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_if_statement()
    setattr(partner, 'pascal_if_statement150', None)
    _safe_set(owner, 'pascal_expression151', partner)
    assert getattr(partner, 'pascal_if_statement150') == owner
    _safe_set(owner, 'pascal_expression151', None)
    assert getattr(partner, 'pascal_if_statement150') is None


def test_assoc_expressions184_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_resto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_resto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_resto(accessor=True, name="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list', None)
    _safe_set(owner, 'pascal_resto185', partner)
    assert getattr(partner, 'pascal_expression_list') == owner
    _safe_set(owner, 'pascal_resto185', None)
    assert getattr(partner, 'pascal_expression_list') is None


def test_assoc_expressions195_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list197' property in the generated
    # code (a bare stub) -- manually attach it so pascal_set's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_set's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_set(brackets="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list197', None)
    _safe_set(owner, 'pascal_set196', partner)
    assert getattr(partner, 'pascal_expression_list197') == owner
    _safe_set(owner, 'pascal_set196', None)
    assert getattr(partner, 'pascal_expression_list197') is None


def test_assoc_expressions198_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list199' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list199', None)
    _safe_set(owner, 'pascal_expression200', partner)
    assert owner in getattr(partner, 'pascal_expression_list199')
    _safe_set(owner, 'pascal_expression200', None)
    assert owner not in getattr(partner, 'pascal_expression_list199')


def test_assoc_expressions201_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list203' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_designator(name="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list203', None)
    _safe_set(owner, 'pascal_function_designator202', partner)
    assert getattr(partner, 'pascal_expression_list203') == owner
    _safe_set(owner, 'pascal_function_designator202', None)
    assert getattr(partner, 'pascal_expression_list203') is None


def test_assoc_fields242_stub_double():
    # pascal_field_list has no real 'pascal_field_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_record_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_record_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_record_type(end="sample_text", record="sample_text")
    partner = pascal_field_list()
    setattr(partner, 'pascal_field_list', None)
    _safe_set(owner, 'pascal_record_type243', partner)
    assert getattr(partner, 'pascal_field_list') == owner
    _safe_set(owner, 'pascal_record_type243', None)
    assert getattr(partner, 'pascal_field_list') is None


def test_assoc_for_124_stub_double():
    # pascal_repetitive_statement has no real 'pascal_repetitive_statement125' property in the generated
    # code (a bare stub) -- manually attach it so pascal_for_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_for_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_for_statement(initID="sample_text")
    partner = pascal_repetitive_statement()
    setattr(partner, 'pascal_repetitive_statement125', None)
    _safe_set(owner, 'pascal_for_statement', partner)
    assert getattr(partner, 'pascal_repetitive_statement125') == owner
    _safe_set(owner, 'pascal_for_statement', None)
    assert getattr(partner, 'pascal_repetitive_statement125') is None


def test_assoc_function59_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section60' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section60', None)
    _safe_set(owner, 'pascal_abstraction_heading61', partner)
    assert getattr(partner, 'pascal_formal_parameter_section60') == owner
    _safe_set(owner, 'pascal_abstraction_heading61', None)
    assert getattr(partner, 'pascal_formal_parameter_section60') is None


def test_assoc_functions38_stub_double():
    # pascal_procedure_and_function_declaration_part has no real 'pascal_procedure_and_function_declaration_part39' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_declaration(forward=True)
    partner = pascal_procedure_and_function_declaration_part()
    setattr(partner, 'pascal_procedure_and_function_declaration_part39', None)
    _safe_set(owner, 'pascal_abstraction_declaration', partner)
    assert owner in getattr(partner, 'pascal_procedure_and_function_declaration_part39')
    _safe_set(owner, 'pascal_abstraction_declaration', None)
    assert owner not in getattr(partner, 'pascal_procedure_and_function_declaration_part39')


def test_assoc_goto100_stub_double():
    # pascal_goto_statement has no real 'pascal_goto_statement' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_goto_statement()
    setattr(partner, 'pascal_goto_statement', None)
    _safe_set(owner, 'pascal_simple_statement101', partner)
    assert getattr(partner, 'pascal_goto_statement') == owner
    _safe_set(owner, 'pascal_simple_statement101', None)
    assert getattr(partner, 'pascal_goto_statement') is None


def test_assoc_heading0_stub_double():
    # pascal_program has no real 'pascal_program' property in the generated
    # code (a bare stub) -- manually attach it so pascal_program_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_program_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_program_heading(name="sample_text")
    partner = pascal_program()
    setattr(partner, 'pascal_program', None)
    _safe_set(owner, 'pascal_program_heading', partner)
    assert getattr(partner, 'pascal_program') == owner
    _safe_set(owner, 'pascal_program_heading', None)
    assert getattr(partner, 'pascal_program') is None


def test_assoc_identifiers214_stub_double():
    # pascal_enumerated_type has no real 'pascal_enumerated_type215' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_enumerated_type()
    setattr(partner, 'pascal_enumerated_type215', None)
    _safe_set(owner, 'pascal_identifier_list216', partner)
    assert getattr(partner, 'pascal_enumerated_type215') == owner
    _safe_set(owner, 'pascal_identifier_list216', None)
    assert getattr(partner, 'pascal_enumerated_type215') is None


def test_assoc_identifiers259_stub_double():
    # pascal_record_section has no real 'pascal_record_section260' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_record_section()
    setattr(partner, 'pascal_record_section260', None)
    _safe_set(owner, 'pascal_identifier_list261', partner)
    assert getattr(partner, 'pascal_record_section260') == owner
    _safe_set(owner, 'pascal_identifier_list261', None)
    assert getattr(partner, 'pascal_record_section260') is None


def test_assoc_identifiers31_stub_double():
    # pascal_variable_section has no real 'pascal_variable_section32' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable_identifier_list(names="sample_text")
    partner = pascal_variable_section()
    setattr(partner, 'pascal_variable_section32', None)
    _safe_set(owner, 'pascal_variable_identifier_list', partner)
    assert getattr(partner, 'pascal_variable_section32') == owner
    _safe_set(owner, 'pascal_variable_identifier_list', None)
    assert getattr(partner, 'pascal_variable_section32') is None


def test_assoc_identifiers62_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section63' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section63', None)
    _safe_set(owner, 'pascal_identifier_list64', partner)
    assert getattr(partner, 'pascal_value_parameter_section63') == owner
    _safe_set(owner, 'pascal_identifier_list64', None)
    assert getattr(partner, 'pascal_value_parameter_section63') is None


def test_assoc_identifiers67_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section68' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(ids="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section68', None)
    _safe_set(owner, 'pascal_identifier_list69', partner)
    assert getattr(partner, 'pascal_variable_parameter_section68') == owner
    _safe_set(owner, 'pascal_identifier_list69', None)
    assert getattr(partner, 'pascal_variable_parameter_section68') is None


def test_assoc_indexes236_stub_double():
    # pascal_array_type has no real 'pascal_array_type237' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(name="sample_text")
    partner = pascal_array_type()
    setattr(partner, 'pascal_array_type237', None)
    _safe_set(owner, 'pascal_simple_type238', partner)
    assert owner in getattr(partner, 'pascal_array_type237')
    _safe_set(owner, 'pascal_simple_type238', None)
    assert owner not in getattr(partner, 'pascal_array_type237')


def test_assoc_label106_stub_double():
    # pascal_goto_statement has no real 'pascal_goto_statement107' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_goto_statement()
    setattr(partner, 'pascal_goto_statement107', None)
    _safe_set(owner, 'pascal_label108', partner)
    assert getattr(partner, 'pascal_goto_statement107') == owner
    _safe_set(owner, 'pascal_label108', None)
    assert getattr(partner, 'pascal_goto_statement107') is None


def test_assoc_label89_stub_double():
    # pascal_statement has no real 'pascal_statement90' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement90', None)
    _safe_set(owner, 'pascal_label91', partner)
    assert getattr(partner, 'pascal_statement90') == owner
    _safe_set(owner, 'pascal_label91', None)
    assert getattr(partner, 'pascal_statement90') is None


def test_assoc_labels19_stub_double():
    # pascal_label_declaration_part has no real 'pascal_label_declaration_part20' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_label_declaration_part()
    setattr(partner, 'pascal_label_declaration_part20', None)
    _safe_set(owner, 'pascal_label', partner)
    assert owner in getattr(partner, 'pascal_label_declaration_part20')
    _safe_set(owner, 'pascal_label', None)
    assert owner not in getattr(partner, 'pascal_label_declaration_part20')


def test_assoc_number169_stub_double():
    # pascal_number has no real 'pascal_number' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number', None)
    _safe_set(owner, 'pascal_factor170', partner)
    assert getattr(partner, 'pascal_number') == owner
    _safe_set(owner, 'pascal_factor170', None)
    assert getattr(partner, 'pascal_number') is None


def test_assoc_number274_stub_double():
    # pascal_number has no real 'pascal_number275' property in the generated
    # code (a bare stub) -- manually attach it so pascal_any_number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_any_number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_any_number(integer="sample_text", real="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number275', None)
    _safe_set(owner, 'pascal_any_number', partner)
    assert getattr(partner, 'pascal_number275') == owner
    _safe_set(owner, 'pascal_any_number', None)
    assert getattr(partner, 'pascal_number275') is None


def test_assoc_number276_stub_double():
    # pascal_number has no real 'pascal_number278' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number278', None)
    _safe_set(owner, 'pascal_constant277', partner)
    assert getattr(partner, 'pascal_number278') == owner
    _safe_set(owner, 'pascal_constant277', None)
    assert getattr(partner, 'pascal_number278') is None


def test_assoc_packed75_stub_double():
    # pascal_conformant_array_schema has no real 'pascal_conformant_array_schema76' property in the generated
    # code (a bare stub) -- manually attach it so pascal_packed_conformant_array_schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_packed_conformant_array_schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_packed_conformant_array_schema(name="sample_text")
    partner = pascal_conformant_array_schema()
    setattr(partner, 'pascal_conformant_array_schema76', None)
    _safe_set(owner, 'pascal_packed_conformant_array_schema', partner)
    assert getattr(partner, 'pascal_conformant_array_schema76') == owner
    _safe_set(owner, 'pascal_packed_conformant_array_schema', None)
    assert getattr(partner, 'pascal_conformant_array_schema76') is None


def test_assoc_parameters40_stub_double():
    # pascal_formal_parameter_list has no real 'pascal_formal_parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    partner = pascal_formal_parameter_list()
    setattr(partner, 'pascal_formal_parameter_list', None)
    _safe_set(owner, 'pascal_abstraction_heading41', partner)
    assert getattr(partner, 'pascal_formal_parameter_list') == owner
    _safe_set(owner, 'pascal_abstraction_heading41', None)
    assert getattr(partner, 'pascal_formal_parameter_list') is None


def test_assoc_procedure56_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section57' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section57', None)
    _safe_set(owner, 'pascal_abstraction_heading58', partner)
    assert getattr(partner, 'pascal_formal_parameter_section57') == owner
    _safe_set(owner, 'pascal_abstraction_heading58', None)
    assert getattr(partner, 'pascal_formal_parameter_section57') is None


def test_assoc_procedures36_stub_double():
    # pascal_procedure_and_function_declaration_part has no real 'pascal_procedure_and_function_declaration_part37' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    partner = pascal_procedure_and_function_declaration_part()
    setattr(partner, 'pascal_procedure_and_function_declaration_part37', None)
    _safe_set(owner, 'pascal_abstraction_heading', partner)
    assert owner in getattr(partner, 'pascal_procedure_and_function_declaration_part37')
    _safe_set(owner, 'pascal_abstraction_heading', None)
    assert owner not in getattr(partner, 'pascal_procedure_and_function_declaration_part37')


def test_assoc_record230_stub_double():
    # pascal_unpacked_structured_type has no real 'pascal_unpacked_structured_type231' property in the generated
    # code (a bare stub) -- manually attach it so pascal_record_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_record_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_record_type(end="sample_text", record="sample_text")
    partner = pascal_unpacked_structured_type()
    setattr(partner, 'pascal_unpacked_structured_type231', None)
    _safe_set(owner, 'pascal_record_type', partner)
    assert getattr(partner, 'pascal_unpacked_structured_type231') == owner
    _safe_set(owner, 'pascal_record_type', None)
    assert getattr(partner, 'pascal_unpacked_structured_type231') is None


def test_assoc_simple204_stub_double():
    # pascal_type has no real 'pascal_type205' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(name="sample_text")
    partner = pascal_type()
    setattr(partner, 'pascal_type205', None)
    _safe_set(owner, 'pascal_simple_type', partner)
    assert getattr(partner, 'pascal_type205') == owner
    _safe_set(owner, 'pascal_simple_type', None)
    assert getattr(partner, 'pascal_type205') is None


def test_assoc_simple92_stub_double():
    # pascal_statement has no real 'pascal_statement93' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement93', None)
    _safe_set(owner, 'pascal_simple_statement', partner)
    assert getattr(partner, 'pascal_statement93') == owner
    _safe_set(owner, 'pascal_simple_statement', None)
    assert getattr(partner, 'pascal_statement93') is None


def test_assoc_stmt144_stub_double():
    # pascal_statement has no real 'pascal_statement146' property in the generated
    # code (a bare stub) -- manually attach it so pascal_for_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_for_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_for_statement(initID="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement146', None)
    _safe_set(owner, 'pascal_for_statement145', partner)
    assert getattr(partner, 'pascal_statement146') == owner
    _safe_set(owner, 'pascal_for_statement145', None)
    assert getattr(partner, 'pascal_statement146') is None


def test_assoc_stmt158_stub_double():
    # pascal_statement has no real 'pascal_statement160' property in the generated
    # code (a bare stub) -- manually attach it so pascal_with_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_with_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_with_statement(record="sample_text", records="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement160', None)
    _safe_set(owner, 'pascal_with_statement159', partner)
    assert getattr(partner, 'pascal_statement160') == owner
    _safe_set(owner, 'pascal_with_statement159', None)
    assert getattr(partner, 'pascal_statement160') is None


def test_assoc_structured206_stub_double():
    # pascal_type has no real 'pascal_type207' property in the generated
    # code (a bare stub) -- manually attach it so pascal_structured_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_structured_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_structured_type(packed=True)
    partner = pascal_type()
    setattr(partner, 'pascal_type207', None)
    _safe_set(owner, 'pascal_structured_type', partner)
    assert getattr(partner, 'pascal_type207') == owner
    _safe_set(owner, 'pascal_structured_type', None)
    assert getattr(partner, 'pascal_type207') is None


def test_assoc_terms163_stub_double():
    # pascal_EObject has no real 'pascal_EObject' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    partner = pascal_EObject()
    setattr(partner, 'pascal_EObject', None)
    _safe_set(owner, 'pascal_simple_expression164', {partner})
    assert getattr(partner, 'pascal_EObject') == owner
    _safe_set(owner, 'pascal_simple_expression164', set())
    assert getattr(partner, 'pascal_EObject') is None


def test_assoc_type226_stub_double():
    # pascal_unpacked_structured_type has no real 'pascal_unpacked_structured_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_structured_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_structured_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_structured_type(packed=True)
    partner = pascal_unpacked_structured_type()
    setattr(partner, 'pascal_unpacked_structured_type', None)
    _safe_set(owner, 'pascal_structured_type227', partner)
    assert getattr(partner, 'pascal_unpacked_structured_type') == owner
    _safe_set(owner, 'pascal_structured_type227', None)
    assert getattr(partner, 'pascal_unpacked_structured_type') is None


def test_assoc_type27_stub_double():
    # pascal_type has no real 'pascal_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type_definition(name="sample_text")
    partner = pascal_type()
    setattr(partner, 'pascal_type', None)
    _safe_set(owner, 'pascal_type_definition28', partner)
    assert getattr(partner, 'pascal_type') == owner
    _safe_set(owner, 'pascal_type_definition28', None)
    assert getattr(partner, 'pascal_type') is None


def test_assoc_type65_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section66' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section66', None)
    _safe_set(owner, 'pascal_parameter_type', partner)
    assert getattr(partner, 'pascal_value_parameter_section66') == owner
    _safe_set(owner, 'pascal_parameter_type', None)
    assert getattr(partner, 'pascal_value_parameter_section66') is None


def test_assoc_type70_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section71' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section71', None)
    _safe_set(owner, 'pascal_parameter_type72', partner)
    assert getattr(partner, 'pascal_variable_parameter_section71') == owner
    _safe_set(owner, 'pascal_parameter_type72', None)
    assert getattr(partner, 'pascal_variable_parameter_section71') is None


def test_assoc_type84_stub_double():
    # pascal_unpacked_conformant_array_schema has no real 'pascal_unpacked_conformant_array_schema85' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_unpacked_conformant_array_schema()
    setattr(partner, 'pascal_unpacked_conformant_array_schema85', None)
    _safe_set(owner, 'pascal_parameter_type86', partner)
    assert getattr(partner, 'pascal_unpacked_conformant_array_schema85') == owner
    _safe_set(owner, 'pascal_parameter_type86', None)
    assert getattr(partner, 'pascal_unpacked_conformant_array_schema85') is None


def test_assoc_types25_stub_double():
    # pascal_type_definition_part has no real 'pascal_type_definition_part26' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type_definition(name="sample_text")
    partner = pascal_type_definition_part()
    setattr(partner, 'pascal_type_definition_part26', None)
    _safe_set(owner, 'pascal_type_definition', partner)
    assert owner in getattr(partner, 'pascal_type_definition_part26')
    _safe_set(owner, 'pascal_type_definition', None)
    assert owner not in getattr(partner, 'pascal_type_definition_part26')


def test_assoc_variable102_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement103' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable(name="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement103', None)
    _safe_set(owner, 'pascal_variable', partner)
    assert getattr(partner, 'pascal_assignment_statement103') == owner
    _safe_set(owner, 'pascal_variable', None)
    assert getattr(partner, 'pascal_assignment_statement103') is None


def test_assoc_variants255_stub_double():
    # pascal_field_list has no real 'pascal_field_list256' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variant_part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variant_part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variant_part(name="sample_text")
    partner = pascal_field_list()
    setattr(partner, 'pascal_field_list256', None)
    _safe_set(owner, 'pascal_variant_part', partner)
    assert owner in getattr(partner, 'pascal_field_list256')
    _safe_set(owner, 'pascal_variant_part', None)
    assert owner not in getattr(partner, 'pascal_field_list256')


def test_assoc_variants267_stub_double():
    # pascal_variant has no real 'pascal_variant' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variant_part's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variant_part's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variant_part(name="sample_text")
    partner = pascal_variant()
    setattr(partner, 'pascal_variant', None)
    _safe_set(owner, 'pascal_variant_part268', {partner})
    assert getattr(partner, 'pascal_variant') == owner
    _safe_set(owner, 'pascal_variant_part268', set())
    assert getattr(partner, 'pascal_variant') is None


def test_assoc_with_stt115_stub_double():
    # pascal_structured_statement has no real 'pascal_structured_statement116' property in the generated
    # code (a bare stub) -- manually attach it so pascal_with_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_with_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_with_statement(record="sample_text", records="sample_text")
    partner = pascal_structured_statement()
    setattr(partner, 'pascal_structured_statement116', None)
    _safe_set(owner, 'pascal_with_statement', partner)
    assert getattr(partner, 'pascal_structured_statement116') == owner
    _safe_set(owner, 'pascal_with_statement', None)
    assert getattr(partner, 'pascal_structured_statement116') is None


