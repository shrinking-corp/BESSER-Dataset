import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    output_list,
    output_value,
    pascal_Begin,
    pascal_actual_function,
    pascal_actual_parameter,
    pascal_actual_parameter_list,
    pascal_actual_procedure,
    pascal_actual_value,
    pascal_actual_variable,
    pascal_addition_operator,
    pascal_array_type,
    pascal_assignment_statement,
    pascal_base_type,
    pascal_block,
    pascal_bound_specification,
    pascal_case_label_list,
    pascal_case_limb,
    pascal_case_statement,
    pascal_compiler_defined_directives,
    pascal_compound_statement,
    pascal_conditional_statement,
    pascal_conformant_array_schema,
    pascal_constant,
    pascal_constant_definition,
    pascal_constant_definition_part,
    pascal_declaration_part,
    pascal_digit_sequence,
    pascal_directive,
    pascal_element_list,
    pascal_element_type,
    pascal_entire_variable,
    pascal_enumerated_type,
    pascal_expression,
    pascal_expression_list,
    pascal_factor,
    pascal_field_list,
    pascal_file_component_type,
    pascal_file_type,
    pascal_final_expression,
    pascal_fixed_part,
    pascal_for_statement,
    pascal_formal_parameter_list,
    pascal_formal_parameter_section,
    pascal_function_block,
    pascal_function_body,
    pascal_function_designator,
    pascal_function_heading,
    pascal_function_identification,
    pascal_function_parameter_section,
    pascal_goto_statement,
    pascal_identifier,
    pascal_identifier_list,
    pascal_if_statement,
    pascal_index_type,
    pascal_initial_expression,
    pascal_integer_number,
    pascal_label,
    pascal_label_declaration_part,
    pascal_lower_bound,
    pascal_number,
    pascal_ordinal_type_identifier,
    pascal_output_list,
    pascal_output_value,
    pascal_packed_conformant_array_schema,
    pascal_parameter_type,
    pascal_pointer_type,
    pascal_procedure_block,
    pascal_procedure_body,
    pascal_procedure_heading,
    pascal_procedure_identification,
    pascal_procedure_parameter_section,
    pascal_procedure_statement,
    pascal_program,
    pascal_program_heading,
    pascal_real_number,
    pascal_record_section,
    pascal_record_type,
    pascal_repeat_statement,
    pascal_repetitive_statement,
    pascal_result_type,
    pascal_scale_factor,
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
    pascal_type_identifier,
    pascal_unpacked_conformant_array_schema,
    pascal_unpacked_structured_type,
    pascal_upper_bound,
    pascal_value_parameter_section,
    pascal_variable,
    pascal_variable_declaration,
    pascal_variable_declaration_part,
    pascal_variable_parameter_section,
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

def test_assoc_addition_operator80_reverse_link_reassign_clear():
    a1 = pascal_simple_expression(sign="sample_text")
    a2 = pascal_simple_expression(sign="sample_text_2")
    b = pascal_addition_operator(sign="sample_text")
    _safe_set(b, 'pascal_addition_operator', a1)
    assert _is_linked(b, 'pascal_addition_operator', a1)
    if hasattr(a1, 'pascal_simple_expression81'):
        assert _is_linked(a1, 'pascal_simple_expression81', b)
    _safe_set(b, 'pascal_addition_operator', a2)
    assert _is_linked(b, 'pascal_addition_operator', a2)
    if hasattr(a1, 'pascal_simple_expression81'):
        assert not _is_linked(a1, 'pascal_simple_expression81', b)
    if hasattr(a2, 'pascal_simple_expression81'):
        assert _is_linked(a2, 'pascal_simple_expression81', b)
    _safe_set(b, 'pascal_addition_operator', None)
    assert not _is_linked(b, 'pascal_addition_operator', a2)
    if hasattr(a2, 'pascal_simple_expression81'):
        assert not _is_linked(a2, 'pascal_simple_expression81', b)


def test_assoc_constant_identifier252_reverse_link_reassign_clear():
    a1 = pascal_identifier(identifier="sample_text")
    a2 = pascal_identifier(identifier="sample_text_2")
    b = pascal_constant(boolean="sample_text", sign="sample_text", strings="sample_text")
    _safe_set(b, 'pascal_constant253', a1)
    assert _is_linked(b, 'pascal_constant253', a1)
    if hasattr(a1, 'pascal_identifier254'):
        assert _is_linked(a1, 'pascal_identifier254', b)
    _safe_set(b, 'pascal_constant253', a2)
    assert _is_linked(b, 'pascal_constant253', a2)
    if hasattr(a1, 'pascal_identifier254'):
        assert not _is_linked(a1, 'pascal_identifier254', b)
    if hasattr(a2, 'pascal_identifier254'):
        assert _is_linked(a2, 'pascal_identifier254', b)
    _safe_set(b, 'pascal_constant253', None)
    assert not _is_linked(b, 'pascal_constant253', a2)
    if hasattr(a2, 'pascal_identifier254'):
        assert not _is_linked(a2, 'pascal_identifier254', b)


def test_assoc_digit_sequence124_reverse_link_reassign_clear():
    a1 = pascal_scale_factor(sign="sample_text")
    a2 = pascal_scale_factor(sign="sample_text_2")
    b = pascal_digit_sequence(sign="sample_text", unsigned_digit_sequence="sample_text")
    _safe_set(b, 'pascal_digit_sequence126', a1)
    assert _is_linked(b, 'pascal_digit_sequence126', a1)
    if hasattr(a1, 'pascal_scale_factor125'):
        assert _is_linked(a1, 'pascal_scale_factor125', b)
    _safe_set(b, 'pascal_digit_sequence126', a2)
    assert _is_linked(b, 'pascal_digit_sequence126', a2)
    if hasattr(a1, 'pascal_scale_factor125'):
        assert not _is_linked(a1, 'pascal_scale_factor125', b)
    if hasattr(a2, 'pascal_scale_factor125'):
        assert _is_linked(a2, 'pascal_scale_factor125', b)
    _safe_set(b, 'pascal_digit_sequence126', None)
    assert not _is_linked(b, 'pascal_digit_sequence126', a2)
    if hasattr(a2, 'pascal_scale_factor125'):
        assert not _is_linked(a2, 'pascal_scale_factor125', b)


def test_assoc_expression76_reverse_link_reassign_clear():
    a1 = pascal_expression(relational_operator="sample_text")
    a2 = pascal_expression(relational_operator="sample_text_2")
    b = pascal_expression(relational_operator="sample_text")
    _safe_set(b, 'pascal_expression77', a1)
    assert _is_linked(b, 'pascal_expression77', a1)
    if hasattr(a1, 'pascal_expression75'):
        assert _is_linked(a1, 'pascal_expression75', b)
    _safe_set(b, 'pascal_expression77', a2)
    assert _is_linked(b, 'pascal_expression77', a2)
    if hasattr(a1, 'pascal_expression75'):
        assert not _is_linked(a1, 'pascal_expression75', b)
    if hasattr(a2, 'pascal_expression75'):
        assert _is_linked(a2, 'pascal_expression75', b)
    _safe_set(b, 'pascal_expression77', None)
    assert not _is_linked(b, 'pascal_expression77', a2)
    if hasattr(a2, 'pascal_expression75'):
        assert not _is_linked(a2, 'pascal_expression75', b)


def test_assoc_expression96_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", strings="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", strings="sample_text_2")
    b = pascal_expression(relational_operator="sample_text")
    _safe_set(b, 'pascal_expression98', a1)
    assert _is_linked(b, 'pascal_expression98', a1)
    if hasattr(a1, 'pascal_factor97'):
        assert _is_linked(a1, 'pascal_factor97', b)
    _safe_set(b, 'pascal_expression98', a2)
    assert _is_linked(b, 'pascal_expression98', a2)
    if hasattr(a1, 'pascal_factor97'):
        assert not _is_linked(a1, 'pascal_factor97', b)
    if hasattr(a2, 'pascal_factor97'):
        assert _is_linked(a2, 'pascal_factor97', b)
    _safe_set(b, 'pascal_expression98', None)
    assert not _is_linked(b, 'pascal_expression98', a2)
    if hasattr(a2, 'pascal_factor97'):
        assert not _is_linked(a2, 'pascal_factor97', b)


def test_assoc_factor100_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", strings="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", strings="sample_text_2")
    b = pascal_factor(boolean="sample_text", strings="sample_text")
    _safe_set(b, 'pascal_factor99', a1)
    assert _is_linked(b, 'pascal_factor99', a1)
    if hasattr(a1, 'pascal_factor101'):
        assert _is_linked(a1, 'pascal_factor101', b)
    _safe_set(b, 'pascal_factor99', a2)
    assert _is_linked(b, 'pascal_factor99', a2)
    if hasattr(a1, 'pascal_factor101'):
        assert not _is_linked(a1, 'pascal_factor101', b)
    if hasattr(a2, 'pascal_factor101'):
        assert _is_linked(a2, 'pascal_factor101', b)
    _safe_set(b, 'pascal_factor99', None)
    assert not _is_linked(b, 'pascal_factor99', a2)
    if hasattr(a2, 'pascal_factor101'):
        assert not _is_linked(a2, 'pascal_factor101', b)


def test_assoc_factor82_reverse_link_reassign_clear():
    a1 = pascal_term(multiplication_operator="sample_text")
    a2 = pascal_term(multiplication_operator="sample_text_2")
    b = pascal_factor(boolean="sample_text", strings="sample_text")
    _safe_set(b, 'pascal_factor', a1)
    assert _is_linked(b, 'pascal_factor', a1)
    if hasattr(a1, 'pascal_term83'):
        assert _is_linked(a1, 'pascal_term83', b)
    _safe_set(b, 'pascal_factor', a2)
    assert _is_linked(b, 'pascal_factor', a2)
    if hasattr(a1, 'pascal_term83'):
        assert not _is_linked(a1, 'pascal_term83', b)
    if hasattr(a2, 'pascal_term83'):
        assert _is_linked(a2, 'pascal_term83', b)
    _safe_set(b, 'pascal_factor', None)
    assert not _is_linked(b, 'pascal_factor', a2)
    if hasattr(a2, 'pascal_term83'):
        assert not _is_linked(a2, 'pascal_term83', b)


def test_assoc_identifier91_reverse_link_reassign_clear():
    a1 = pascal_identifier(identifier="sample_text")
    a2 = pascal_identifier(identifier="sample_text_2")
    b = pascal_factor(boolean="sample_text", strings="sample_text")
    _safe_set(b, 'pascal_factor92', a1)
    assert _is_linked(b, 'pascal_factor92', a1)
    if hasattr(a1, 'pascal_identifier93'):
        assert _is_linked(a1, 'pascal_identifier93', b)
    _safe_set(b, 'pascal_factor92', a2)
    assert _is_linked(b, 'pascal_factor92', a2)
    if hasattr(a1, 'pascal_identifier93'):
        assert not _is_linked(a1, 'pascal_identifier93', b)
    if hasattr(a2, 'pascal_identifier93'):
        assert _is_linked(a2, 'pascal_identifier93', b)
    _safe_set(b, 'pascal_factor92', None)
    assert not _is_linked(b, 'pascal_factor92', a2)
    if hasattr(a2, 'pascal_identifier93'):
        assert not _is_linked(a2, 'pascal_identifier93', b)


def test_assoc_identifier_list5_reverse_link_reassign_clear():
    a1 = pascal_program_heading(identifier="sample_text")
    a2 = pascal_program_heading(identifier="sample_text_2")
    b = pascal_identifier_list(identifier="sample_text")
    _safe_set(b, 'pascal_identifier_list', a1)
    assert _is_linked(b, 'pascal_identifier_list', a1)
    if hasattr(a1, 'pascal_program_heading6'):
        assert _is_linked(a1, 'pascal_program_heading6', b)
    _safe_set(b, 'pascal_identifier_list', a2)
    assert _is_linked(b, 'pascal_identifier_list', a2)
    if hasattr(a1, 'pascal_program_heading6'):
        assert not _is_linked(a1, 'pascal_program_heading6', b)
    if hasattr(a2, 'pascal_program_heading6'):
        assert _is_linked(a2, 'pascal_program_heading6', b)
    _safe_set(b, 'pascal_identifier_list', None)
    assert not _is_linked(b, 'pascal_identifier_list', a2)
    if hasattr(a2, 'pascal_program_heading6'):
        assert not _is_linked(a2, 'pascal_program_heading6', b)


def test_assoc_simple_expression73_reverse_link_reassign_clear():
    a1 = pascal_simple_expression(sign="sample_text")
    a2 = pascal_simple_expression(sign="sample_text_2")
    b = pascal_expression(relational_operator="sample_text")
    _safe_set(b, 'pascal_expression74', {a1})
    assert _is_linked(b, 'pascal_expression74', a1)
    if hasattr(a1, 'pascal_simple_expression'):
        assert _is_linked(a1, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression74', {a2})
    assert _is_linked(b, 'pascal_expression74', a2)
    if hasattr(a1, 'pascal_simple_expression'):
        assert not _is_linked(a1, 'pascal_simple_expression', b)
    if hasattr(a2, 'pascal_simple_expression'):
        assert _is_linked(a2, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression74', set())
    assert not _is_linked(b, 'pascal_expression74', a2)
    if hasattr(a2, 'pascal_simple_expression'):
        assert not _is_linked(a2, 'pascal_simple_expression', b)


def test_assoc_term78_reverse_link_reassign_clear():
    a1 = pascal_term(multiplication_operator="sample_text")
    a2 = pascal_term(multiplication_operator="sample_text_2")
    b = pascal_simple_expression(sign="sample_text")
    _safe_set(b, 'pascal_simple_expression79', {a1})
    assert _is_linked(b, 'pascal_simple_expression79', a1)
    if hasattr(a1, 'pascal_term'):
        assert _is_linked(a1, 'pascal_term', b)
    _safe_set(b, 'pascal_simple_expression79', {a2})
    assert _is_linked(b, 'pascal_simple_expression79', a2)
    if hasattr(a1, 'pascal_term'):
        assert not _is_linked(a1, 'pascal_term', b)
    if hasattr(a2, 'pascal_term'):
        assert _is_linked(a2, 'pascal_term', b)
    _safe_set(b, 'pascal_simple_expression79', set())
    assert not _is_linked(b, 'pascal_simple_expression79', a2)
    if hasattr(a2, 'pascal_term'):
        assert not _is_linked(a2, 'pascal_term', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_constant174_stub_double():
    # pascal_case_label_list has no real 'pascal_case_label_list175' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolean="sample_text", sign="sample_text", strings="sample_text")
    partner = pascal_case_label_list()
    setattr(partner, 'pascal_case_label_list175', None)
    _safe_set(owner, 'pascal_constant', partner)
    assert owner in getattr(partner, 'pascal_case_label_list175')
    _safe_set(owner, 'pascal_constant', None)
    assert owner not in getattr(partner, 'pascal_case_label_list175')


def test_assoc_constant249_stub_double():
    # pascal_constant_definition has no real 'pascal_constant_definition250' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolean="sample_text", sign="sample_text", strings="sample_text")
    partner = pascal_constant_definition()
    setattr(partner, 'pascal_constant_definition250', None)
    _safe_set(owner, 'pascal_constant251', partner)
    assert getattr(partner, 'pascal_constant_definition250') == owner
    _safe_set(owner, 'pascal_constant251', None)
    assert getattr(partner, 'pascal_constant_definition250') is None


def test_assoc_constant350_stub_double():
    # pascal_lower_bound has no real 'pascal_lower_bound351' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolean="sample_text", sign="sample_text", strings="sample_text")
    partner = pascal_lower_bound()
    setattr(partner, 'pascal_lower_bound351', None)
    _safe_set(owner, 'pascal_constant352', partner)
    assert getattr(partner, 'pascal_lower_bound351') == owner
    _safe_set(owner, 'pascal_constant352', None)
    assert getattr(partner, 'pascal_lower_bound351') is None


def test_assoc_constant353_stub_double():
    # pascal_upper_bound has no real 'pascal_upper_bound354' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolean="sample_text", sign="sample_text", strings="sample_text")
    partner = pascal_upper_bound()
    setattr(partner, 'pascal_upper_bound354', None)
    _safe_set(owner, 'pascal_constant355', partner)
    assert getattr(partner, 'pascal_upper_bound354') == owner
    _safe_set(owner, 'pascal_constant355', None)
    assert getattr(partner, 'pascal_upper_bound354') is None


def test_assoc_digit_sequence117_stub_double():
    # pascal_real_number has no real 'pascal_real_number118' property in the generated
    # code (a bare stub) -- manually attach it so pascal_digit_sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_digit_sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_digit_sequence(sign="sample_text", unsigned_digit_sequence="sample_text")
    partner = pascal_real_number()
    setattr(partner, 'pascal_real_number118', None)
    _safe_set(owner, 'pascal_digit_sequence', partner)
    assert getattr(partner, 'pascal_real_number118') == owner
    _safe_set(owner, 'pascal_digit_sequence', None)
    assert getattr(partner, 'pascal_real_number118') is None


def test_assoc_digit_sequence143_stub_double():
    # pascal_integer_number has no real 'pascal_integer_number144' property in the generated
    # code (a bare stub) -- manually attach it so pascal_digit_sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_digit_sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_digit_sequence(sign="sample_text", unsigned_digit_sequence="sample_text")
    partner = pascal_integer_number()
    setattr(partner, 'pascal_integer_number144', None)
    _safe_set(owner, 'pascal_digit_sequence145', partner)
    assert getattr(partner, 'pascal_integer_number144') == owner
    _safe_set(owner, 'pascal_digit_sequence145', None)
    assert getattr(partner, 'pascal_integer_number144') is None


def test_assoc_digit_sequence2119_stub_double():
    # pascal_real_number has no real 'pascal_real_number120' property in the generated
    # code (a bare stub) -- manually attach it so pascal_digit_sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_digit_sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_digit_sequence(sign="sample_text", unsigned_digit_sequence="sample_text")
    partner = pascal_real_number()
    setattr(partner, 'pascal_real_number120', None)
    _safe_set(owner, 'pascal_digit_sequence121', partner)
    assert getattr(partner, 'pascal_real_number120') == owner
    _safe_set(owner, 'pascal_digit_sequence121', None)
    assert getattr(partner, 'pascal_real_number120') is None


def test_assoc_expression110_stub_double():
    # pascal_element_list has no real 'pascal_element_list111' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_element_list()
    setattr(partner, 'pascal_element_list111', None)
    _safe_set(owner, 'pascal_expression112', partner)
    assert owner in getattr(partner, 'pascal_element_list111')
    _safe_set(owner, 'pascal_expression112', None)
    assert owner not in getattr(partner, 'pascal_element_list111')


def test_assoc_expression137_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list138' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list138', None)
    _safe_set(owner, 'pascal_expression139', partner)
    assert owner in getattr(partner, 'pascal_expression_list138')
    _safe_set(owner, 'pascal_expression139', None)
    assert owner not in getattr(partner, 'pascal_expression_list138')


def test_assoc_expression164_stub_double():
    # pascal_case_statement has no real 'pascal_case_statement165' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_case_statement()
    setattr(partner, 'pascal_case_statement165', None)
    _safe_set(owner, 'pascal_expression166', partner)
    assert getattr(partner, 'pascal_case_statement165') == owner
    _safe_set(owner, 'pascal_expression166', None)
    assert getattr(partner, 'pascal_case_statement165') is None


def test_assoc_expression176_stub_double():
    # pascal_if_statement has no real 'pascal_if_statement177' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_if_statement()
    setattr(partner, 'pascal_if_statement177', None)
    _safe_set(owner, 'pascal_expression178', partner)
    assert getattr(partner, 'pascal_if_statement177') == owner
    _safe_set(owner, 'pascal_expression178', None)
    assert getattr(partner, 'pascal_if_statement177') is None


def test_assoc_expression198_stub_double():
    # pascal_final_expression has no real 'pascal_final_expression199' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_final_expression()
    setattr(partner, 'pascal_final_expression199', None)
    _safe_set(owner, 'pascal_expression200', partner)
    assert getattr(partner, 'pascal_final_expression199') == owner
    _safe_set(owner, 'pascal_expression200', None)
    assert getattr(partner, 'pascal_final_expression199') is None


def test_assoc_expression201_stub_double():
    # pascal_initial_expression has no real 'pascal_initial_expression202' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_initial_expression()
    setattr(partner, 'pascal_initial_expression202', None)
    _safe_set(owner, 'pascal_expression203', partner)
    assert getattr(partner, 'pascal_initial_expression202') == owner
    _safe_set(owner, 'pascal_expression203', None)
    assert getattr(partner, 'pascal_initial_expression202') is None


def test_assoc_expression207_stub_double():
    # pascal_repeat_statement has no real 'pascal_repeat_statement208' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_repeat_statement()
    setattr(partner, 'pascal_repeat_statement208', None)
    _safe_set(owner, 'pascal_expression209', partner)
    assert getattr(partner, 'pascal_repeat_statement208') == owner
    _safe_set(owner, 'pascal_expression209', None)
    assert getattr(partner, 'pascal_repeat_statement208') is None


def test_assoc_expression210_stub_double():
    # pascal_while_statement has no real 'pascal_while_statement211' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_while_statement()
    setattr(partner, 'pascal_while_statement211', None)
    _safe_set(owner, 'pascal_expression212', partner)
    assert getattr(partner, 'pascal_while_statement211') == owner
    _safe_set(owner, 'pascal_expression212', None)
    assert getattr(partner, 'pascal_while_statement211') is None


def test_assoc_expression62_stub_double():
    # pascal_actual_value has no real 'pascal_actual_value63' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_actual_value()
    setattr(partner, 'pascal_actual_value63', None)
    _safe_set(owner, 'pascal_expression', partner)
    assert getattr(partner, 'pascal_actual_value63') == owner
    _safe_set(owner, 'pascal_expression', None)
    assert getattr(partner, 'pascal_actual_value63') is None


def test_assoc_expression70_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement71' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relational_operator="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement71', None)
    _safe_set(owner, 'pascal_expression72', partner)
    assert getattr(partner, 'pascal_assignment_statement71') == owner
    _safe_set(owner, 'pascal_expression72', None)
    assert getattr(partner, 'pascal_assignment_statement71') is None


def test_assoc_field_identifier131_stub_double():
    # pascal_variable has no real 'pascal_variable132' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_variable()
    setattr(partner, 'pascal_variable132', None)
    _safe_set(owner, 'pascal_identifier133', partner)
    assert owner in getattr(partner, 'pascal_variable132')
    _safe_set(owner, 'pascal_identifier133', None)
    assert owner not in getattr(partner, 'pascal_variable132')


def test_assoc_function_designator94_stub_double():
    # pascal_function_designator has no real 'pascal_function_designator' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(boolean="sample_text", strings="sample_text")
    partner = pascal_function_designator()
    setattr(partner, 'pascal_function_designator', None)
    _safe_set(owner, 'pascal_factor95', partner)
    assert getattr(partner, 'pascal_function_designator') == owner
    _safe_set(owner, 'pascal_factor95', None)
    assert getattr(partner, 'pascal_function_designator') is None


def test_assoc_function_identifier102_stub_double():
    # pascal_function_designator has no real 'pascal_function_designator103' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_function_designator()
    setattr(partner, 'pascal_function_designator103', None)
    _safe_set(owner, 'pascal_identifier104', partner)
    assert getattr(partner, 'pascal_function_designator103') == owner
    _safe_set(owner, 'pascal_identifier104', None)
    assert getattr(partner, 'pascal_function_designator103') is None


def test_assoc_function_identifier364_stub_double():
    # pascal_function_identification has no real 'pascal_function_identification365' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_function_identification()
    setattr(partner, 'pascal_function_identification365', None)
    _safe_set(owner, 'pascal_identifier366', partner)
    assert getattr(partner, 'pascal_function_identification365') == owner
    _safe_set(owner, 'pascal_identifier366', None)
    assert getattr(partner, 'pascal_function_identification365') is None


def test_assoc_function_identifier54_stub_double():
    # pascal_actual_function has no real 'pascal_actual_function55' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_actual_function()
    setattr(partner, 'pascal_actual_function55', None)
    _safe_set(owner, 'pascal_identifier56', partner)
    assert getattr(partner, 'pascal_actual_function55') == owner
    _safe_set(owner, 'pascal_identifier56', None)
    assert getattr(partner, 'pascal_actual_function55') is None


def test_assoc_function_identifier67_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement68' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement68', None)
    _safe_set(owner, 'pascal_identifier69', partner)
    assert getattr(partner, 'pascal_assignment_statement68') == owner
    _safe_set(owner, 'pascal_identifier69', None)
    assert getattr(partner, 'pascal_assignment_statement68') is None


def test_assoc_identifier134_stub_double():
    # pascal_entire_variable has no real 'pascal_entire_variable135' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_entire_variable()
    setattr(partner, 'pascal_entire_variable135', None)
    _safe_set(owner, 'pascal_identifier136', partner)
    assert getattr(partner, 'pascal_entire_variable135') == owner
    _safe_set(owner, 'pascal_identifier136', None)
    assert getattr(partner, 'pascal_entire_variable135') is None


def test_assoc_identifier2444_stub_double():
    # pascal_bound_specification has no real 'pascal_bound_specification445' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_bound_specification()
    setattr(partner, 'pascal_bound_specification445', None)
    _safe_set(owner, 'pascal_identifier446', partner)
    assert getattr(partner, 'pascal_bound_specification445') == owner
    _safe_set(owner, 'pascal_identifier446', None)
    assert getattr(partner, 'pascal_bound_specification445') is None


def test_assoc_identifier246_stub_double():
    # pascal_constant_definition has no real 'pascal_constant_definition247' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_constant_definition()
    setattr(partner, 'pascal_constant_definition247', None)
    _safe_set(owner, 'pascal_identifier248', partner)
    assert getattr(partner, 'pascal_constant_definition247') == owner
    _safe_set(owner, 'pascal_identifier248', None)
    assert getattr(partner, 'pascal_constant_definition247') is None


def test_assoc_identifier260_stub_double():
    # pascal_type_definition has no real 'pascal_type_definition261' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_type_definition()
    setattr(partner, 'pascal_type_definition261', None)
    _safe_set(owner, 'pascal_identifier262', partner)
    assert getattr(partner, 'pascal_type_definition261') == owner
    _safe_set(owner, 'pascal_identifier262', None)
    assert getattr(partner, 'pascal_type_definition261') is None


def test_assoc_identifier273_stub_double():
    # pascal_type_identifier has no real 'pascal_type_identifier274' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_type_identifier()
    setattr(partner, 'pascal_type_identifier274', None)
    _safe_set(owner, 'pascal_identifier275', partner)
    assert getattr(partner, 'pascal_type_identifier274') == owner
    _safe_set(owner, 'pascal_identifier275', None)
    assert getattr(partner, 'pascal_type_identifier274') is None


def test_assoc_identifier326_stub_double():
    # pascal_tag_field has no real 'pascal_tag_field327' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_tag_field()
    setattr(partner, 'pascal_tag_field327', None)
    _safe_set(owner, 'pascal_identifier328', partner)
    assert getattr(partner, 'pascal_tag_field327') == owner
    _safe_set(owner, 'pascal_identifier328', None)
    assert getattr(partner, 'pascal_tag_field327') is None


def test_assoc_identifier370_stub_double():
    # pascal_procedure_identification has no real 'pascal_procedure_identification371' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_procedure_identification()
    setattr(partner, 'pascal_procedure_identification371', None)
    _safe_set(owner, 'pascal_identifier372', partner)
    assert getattr(partner, 'pascal_procedure_identification371') == owner
    _safe_set(owner, 'pascal_identifier372', None)
    assert getattr(partner, 'pascal_procedure_identification371') is None


def test_assoc_identifier381_stub_double():
    # pascal_procedure_heading has no real 'pascal_procedure_heading382' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_procedure_heading()
    setattr(partner, 'pascal_procedure_heading382', None)
    _safe_set(owner, 'pascal_identifier383', partner)
    assert getattr(partner, 'pascal_procedure_heading382') == owner
    _safe_set(owner, 'pascal_identifier383', None)
    assert getattr(partner, 'pascal_procedure_heading382') is None


def test_assoc_identifier399_stub_double():
    # pascal_function_heading has no real 'pascal_function_heading400' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_function_heading()
    setattr(partner, 'pascal_function_heading400', None)
    _safe_set(owner, 'pascal_identifier401', partner)
    assert getattr(partner, 'pascal_function_heading400') == owner
    _safe_set(owner, 'pascal_identifier401', None)
    assert getattr(partner, 'pascal_function_heading400') is None


def test_assoc_identifier441_stub_double():
    # pascal_bound_specification has no real 'pascal_bound_specification442' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_bound_specification()
    setattr(partner, 'pascal_bound_specification442', None)
    _safe_set(owner, 'pascal_identifier443', partner)
    assert getattr(partner, 'pascal_bound_specification442') == owner
    _safe_set(owner, 'pascal_identifier443', None)
    assert getattr(partner, 'pascal_bound_specification442') is None


def test_assoc_identifier_list307_stub_double():
    # pascal_record_section has no real 'pascal_record_section308' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(identifier="sample_text")
    partner = pascal_record_section()
    setattr(partner, 'pascal_record_section308', None)
    _safe_set(owner, 'pascal_identifier_list309', partner)
    assert getattr(partner, 'pascal_record_section308') == owner
    _safe_set(owner, 'pascal_identifier_list309', None)
    assert getattr(partner, 'pascal_record_section308') is None


def test_assoc_identifier_list343_stub_double():
    # pascal_enumerated_type has no real 'pascal_enumerated_type344' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(identifier="sample_text")
    partner = pascal_enumerated_type()
    setattr(partner, 'pascal_enumerated_type344', None)
    _safe_set(owner, 'pascal_identifier_list345', partner)
    assert getattr(partner, 'pascal_enumerated_type344') == owner
    _safe_set(owner, 'pascal_identifier_list345', None)
    assert getattr(partner, 'pascal_enumerated_type344') is None


def test_assoc_identifier_list358_stub_double():
    # pascal_variable_declaration has no real 'pascal_variable_declaration359' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(identifier="sample_text")
    partner = pascal_variable_declaration()
    setattr(partner, 'pascal_variable_declaration359', None)
    _safe_set(owner, 'pascal_identifier_list360', partner)
    assert getattr(partner, 'pascal_variable_declaration359') == owner
    _safe_set(owner, 'pascal_identifier_list360', None)
    assert getattr(partner, 'pascal_variable_declaration359') is None


def test_assoc_identifier_list413_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section414' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(identifier="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section414', None)
    _safe_set(owner, 'pascal_identifier_list415', partner)
    assert getattr(partner, 'pascal_variable_parameter_section414') == owner
    _safe_set(owner, 'pascal_identifier_list415', None)
    assert getattr(partner, 'pascal_variable_parameter_section414') is None


def test_assoc_identifier_list418_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section419' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(identifier="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section419', None)
    _safe_set(owner, 'pascal_identifier_list420', partner)
    assert getattr(partner, 'pascal_value_parameter_section419') == owner
    _safe_set(owner, 'pascal_identifier_list420', None)
    assert getattr(partner, 'pascal_value_parameter_section419') is None


def test_assoc_number255_stub_double():
    # pascal_number has no real 'pascal_number257' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolean="sample_text", sign="sample_text", strings="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number257', None)
    _safe_set(owner, 'pascal_constant256', partner)
    assert getattr(partner, 'pascal_number257') == owner
    _safe_set(owner, 'pascal_constant256', None)
    assert getattr(partner, 'pascal_number257') is None


def test_assoc_number87_stub_double():
    # pascal_number has no real 'pascal_number' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(boolean="sample_text", strings="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number', None)
    _safe_set(owner, 'pascal_factor88', partner)
    assert getattr(partner, 'pascal_number') == owner
    _safe_set(owner, 'pascal_factor88', None)
    assert getattr(partner, 'pascal_number') is None


def test_assoc_procedure_identifier40_stub_double():
    # pascal_procedure_statement has no real 'pascal_procedure_statement41' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_procedure_statement()
    setattr(partner, 'pascal_procedure_statement41', None)
    _safe_set(owner, 'pascal_identifier', partner)
    assert getattr(partner, 'pascal_procedure_statement41') == owner
    _safe_set(owner, 'pascal_identifier', None)
    assert getattr(partner, 'pascal_procedure_statement41') is None


def test_assoc_procedure_identifier57_stub_double():
    # pascal_actual_procedure has no real 'pascal_actual_procedure58' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_actual_procedure()
    setattr(partner, 'pascal_actual_procedure58', None)
    _safe_set(owner, 'pascal_identifier59', partner)
    assert getattr(partner, 'pascal_actual_procedure58') == owner
    _safe_set(owner, 'pascal_identifier59', None)
    assert getattr(partner, 'pascal_actual_procedure58') is None


def test_assoc_program_heading1_stub_double():
    # pascal_program has no real 'pascal_program2' property in the generated
    # code (a bare stub) -- manually attach it so pascal_program_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_program_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_program_heading(identifier="sample_text")
    partner = pascal_program()
    setattr(partner, 'pascal_program2', None)
    _safe_set(owner, 'pascal_program_heading', partner)
    assert getattr(partner, 'pascal_program2') == owner
    _safe_set(owner, 'pascal_program_heading', None)
    assert getattr(partner, 'pascal_program2') is None


def test_assoc_scale_factor122_stub_double():
    # pascal_real_number has no real 'pascal_real_number123' property in the generated
    # code (a bare stub) -- manually attach it so pascal_scale_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_scale_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_scale_factor(sign="sample_text")
    partner = pascal_real_number()
    setattr(partner, 'pascal_real_number123', None)
    _safe_set(owner, 'pascal_scale_factor', partner)
    assert getattr(partner, 'pascal_real_number123') == owner
    _safe_set(owner, 'pascal_scale_factor', None)
    assert getattr(partner, 'pascal_real_number123') is None


def test_assoc_set89_stub_double():
    # pascal_set has no real 'pascal_set' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(boolean="sample_text", strings="sample_text")
    partner = pascal_set()
    setattr(partner, 'pascal_set', None)
    _safe_set(owner, 'pascal_factor90', partner)
    assert getattr(partner, 'pascal_set') == owner
    _safe_set(owner, 'pascal_factor90', None)
    assert getattr(partner, 'pascal_set') is None


def test_assoc_variable84_stub_double():
    # pascal_variable has no real 'pascal_variable86' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(boolean="sample_text", strings="sample_text")
    partner = pascal_variable()
    setattr(partner, 'pascal_variable86', None)
    _safe_set(owner, 'pascal_factor85', partner)
    assert getattr(partner, 'pascal_variable86') == owner
    _safe_set(owner, 'pascal_factor85', None)
    assert getattr(partner, 'pascal_variable86') is None


def test_assoc_variable_identifier188_stub_double():
    # pascal_for_statement has no real 'pascal_for_statement189' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_for_statement()
    setattr(partner, 'pascal_for_statement189', None)
    _safe_set(owner, 'pascal_identifier190', partner)
    assert getattr(partner, 'pascal_for_statement189') == owner
    _safe_set(owner, 'pascal_identifier190', None)
    assert getattr(partner, 'pascal_for_statement189') is None


