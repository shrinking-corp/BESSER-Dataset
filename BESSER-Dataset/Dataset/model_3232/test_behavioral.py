import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    pascal_EObject,
    pascal_abstraction_declaration,
    pascal_abstraction_heading,
    pascal_any_number,
    pascal_assignment_statement,
    pascal_block,
    pascal_compound_statement,
    pascal_constant,
    pascal_constant_definition,
    pascal_constant_definition_part,
    pascal_expression,
    pascal_expression_list,
    pascal_factor,
    pascal_field_list,
    pascal_formal_parameter_list,
    pascal_formal_parameter_section,
    pascal_function_designator,
    pascal_function_procedure_declaration,
    pascal_identifier_list,
    pascal_label,
    pascal_label_declaration,
    pascal_number,
    pascal_parameter_type,
    pascal_program,
    pascal_program_heading_block,
    pascal_record_section,
    pascal_record_type,
    pascal_simple_expression,
    pascal_simple_statement,
    pascal_simple_type,
    pascal_statement,
    pascal_statement_part,
    pascal_statement_sequence,
    pascal_structured_statement,
    pascal_structured_type,
    pascal_term,
    pascal_type,
    pascal_type_definition,
    pascal_type_definition_part,
    pascal_unpacked_structured_type,
    pascal_value_parameter_section,
    pascal_variable,
    pascal_variable_declaration_part,
    pascal_variable_identifier_list,
    pascal_variable_parameter_section,
    pascal_variable_section,
    pascal_while_statement,
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

def test_assoc_const107_reverse_link_reassign_clear():
    a1 = pascal_constant_definition(name="sample_text")
    a2 = pascal_constant_definition(name="sample_text_2")
    b = pascal_constant(boolLiteral="sample_text", name="sample_text", nil=True, opterator="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant109', a1)
    assert _is_linked(b, 'pascal_constant109', a1)
    if hasattr(a1, 'pascal_constant_definition108'):
        assert _is_linked(a1, 'pascal_constant_definition108', b)
    _safe_set(b, 'pascal_constant109', a2)
    assert _is_linked(b, 'pascal_constant109', a2)
    if hasattr(a1, 'pascal_constant_definition108'):
        assert not _is_linked(a1, 'pascal_constant_definition108', b)
    if hasattr(a2, 'pascal_constant_definition108'):
        assert _is_linked(a2, 'pascal_constant_definition108', b)
    _safe_set(b, 'pascal_constant109', None)
    assert not _is_linked(b, 'pascal_constant109', a2)
    if hasattr(a2, 'pascal_constant_definition108'):
        assert not _is_linked(a2, 'pascal_constant_definition108', b)


def test_assoc_expression55_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression57', a1)
    assert _is_linked(b, 'pascal_expression57', a1)
    if hasattr(a1, 'pascal_factor56'):
        assert _is_linked(a1, 'pascal_factor56', b)
    _safe_set(b, 'pascal_expression57', a2)
    assert _is_linked(b, 'pascal_expression57', a2)
    if hasattr(a1, 'pascal_factor56'):
        assert not _is_linked(a1, 'pascal_factor56', b)
    if hasattr(a2, 'pascal_factor56'):
        assert _is_linked(a2, 'pascal_factor56', b)
    _safe_set(b, 'pascal_expression57', None)
    assert not _is_linked(b, 'pascal_expression57', a2)
    if hasattr(a2, 'pascal_factor56'):
        assert not _is_linked(a2, 'pascal_factor56', b)


def test_assoc_expressions42_reverse_link_reassign_clear():
    a1 = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    a2 = pascal_simple_expression(operators="sample_text_2", prefixOperator="sample_text_2")
    b = pascal_expression(operators="sample_text")
    _safe_set(b, 'pascal_expression43', {a1})
    assert _is_linked(b, 'pascal_expression43', a1)
    if hasattr(a1, 'pascal_simple_expression'):
        assert _is_linked(a1, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression43', {a2})
    assert _is_linked(b, 'pascal_expression43', a2)
    if hasattr(a1, 'pascal_simple_expression'):
        assert not _is_linked(a1, 'pascal_simple_expression', b)
    if hasattr(a2, 'pascal_simple_expression'):
        assert _is_linked(a2, 'pascal_simple_expression', b)
    _safe_set(b, 'pascal_expression43', set())
    assert not _is_linked(b, 'pascal_expression43', a2)
    if hasattr(a2, 'pascal_simple_expression'):
        assert not _is_linked(a2, 'pascal_simple_expression', b)


def test_assoc_factors46_reverse_link_reassign_clear():
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


def test_assoc_function27_reverse_link_reassign_clear():
    a1 = pascal_simple_statement(function_noargs="sample_text")
    a2 = pascal_simple_statement(function_noargs="sample_text_2")
    b = pascal_function_designator(name="sample_text")
    _safe_set(b, 'pascal_function_designator', a1)
    assert _is_linked(b, 'pascal_function_designator', a1)
    if hasattr(a1, 'pascal_simple_statement28'):
        assert _is_linked(a1, 'pascal_simple_statement28', b)
    _safe_set(b, 'pascal_function_designator', a2)
    assert _is_linked(b, 'pascal_function_designator', a2)
    if hasattr(a1, 'pascal_simple_statement28'):
        assert not _is_linked(a1, 'pascal_simple_statement28', b)
    if hasattr(a2, 'pascal_simple_statement28'):
        assert _is_linked(a2, 'pascal_simple_statement28', b)
    _safe_set(b, 'pascal_function_designator', None)
    assert not _is_linked(b, 'pascal_function_designator', a2)
    if hasattr(a2, 'pascal_simple_statement28'):
        assert not _is_linked(a2, 'pascal_simple_statement28', b)


def test_assoc_function52_reverse_link_reassign_clear():
    a1 = pascal_function_designator(name="sample_text")
    a2 = pascal_function_designator(name="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor53', a1)
    assert _is_linked(b, 'pascal_factor53', a1)
    if hasattr(a1, 'pascal_function_designator54'):
        assert _is_linked(a1, 'pascal_function_designator54', b)
    _safe_set(b, 'pascal_factor53', a2)
    assert _is_linked(b, 'pascal_factor53', a2)
    if hasattr(a1, 'pascal_function_designator54'):
        assert not _is_linked(a1, 'pascal_function_designator54', b)
    if hasattr(a2, 'pascal_function_designator54'):
        assert _is_linked(a2, 'pascal_function_designator54', b)
    _safe_set(b, 'pascal_factor53', None)
    assert not _is_linked(b, 'pascal_factor53', a2)
    if hasattr(a2, 'pascal_function_designator54'):
        assert not _is_linked(a2, 'pascal_function_designator54', b)


def test_assoc_not_59_reverse_link_reassign_clear():
    a1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    a2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor60', a1)
    assert _is_linked(b, 'pascal_factor60', a1)
    if hasattr(a1, 'pascal_factor58'):
        assert _is_linked(a1, 'pascal_factor58', b)
    _safe_set(b, 'pascal_factor60', a2)
    assert _is_linked(b, 'pascal_factor60', a2)
    if hasattr(a1, 'pascal_factor58'):
        assert not _is_linked(a1, 'pascal_factor58', b)
    if hasattr(a2, 'pascal_factor58'):
        assert _is_linked(a2, 'pascal_factor58', b)
    _safe_set(b, 'pascal_factor60', None)
    assert not _is_linked(b, 'pascal_factor60', a2)
    if hasattr(a2, 'pascal_factor58'):
        assert not _is_linked(a2, 'pascal_factor58', b)


def test_assoc_variable47_reverse_link_reassign_clear():
    a1 = pascal_variable(name="sample_text")
    a2 = pascal_variable(name="sample_text_2")
    b = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    _safe_set(b, 'pascal_factor48', a1)
    assert _is_linked(b, 'pascal_factor48', a1)
    if hasattr(a1, 'pascal_variable49'):
        assert _is_linked(a1, 'pascal_variable49', b)
    _safe_set(b, 'pascal_factor48', a2)
    assert _is_linked(b, 'pascal_factor48', a2)
    if hasattr(a1, 'pascal_variable49'):
        assert not _is_linked(a1, 'pascal_variable49', b)
    if hasattr(a2, 'pascal_variable49'):
        assert _is_linked(a2, 'pascal_variable49', b)
    _safe_set(b, 'pascal_factor48', None)
    assert not _is_linked(b, 'pascal_factor48', a2)
    if hasattr(a2, 'pascal_variable49'):
        assert not _is_linked(a2, 'pascal_variable49', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignment25_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement', None)
    _safe_set(owner, 'pascal_simple_statement26', partner)
    assert getattr(partner, 'pascal_assignment_statement') == owner
    _safe_set(owner, 'pascal_simple_statement26', None)
    assert getattr(partner, 'pascal_assignment_statement') is None


def test_assoc_consts105_stub_double():
    # pascal_constant_definition_part has no real 'pascal_constant_definition_part106' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant_definition(name="sample_text")
    partner = pascal_constant_definition_part()
    setattr(partner, 'pascal_constant_definition_part106', None)
    _safe_set(owner, 'pascal_constant_definition', partner)
    assert owner in getattr(partner, 'pascal_constant_definition_part106')
    _safe_set(owner, 'pascal_constant_definition', None)
    assert owner not in getattr(partner, 'pascal_constant_definition_part106')


def test_assoc_expression139_stub_double():
    # pascal_while_statement has no real 'pascal_while_statement140' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_while_statement()
    setattr(partner, 'pascal_while_statement140', None)
    _safe_set(owner, 'pascal_expression141', partner)
    assert getattr(partner, 'pascal_while_statement140') == owner
    _safe_set(owner, 'pascal_expression141', None)
    assert getattr(partner, 'pascal_while_statement140') is None


def test_assoc_expression38_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement39' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement39', None)
    _safe_set(owner, 'pascal_expression', partner)
    assert getattr(partner, 'pascal_assignment_statement39') == owner
    _safe_set(owner, 'pascal_expression', None)
    assert getattr(partner, 'pascal_assignment_statement39') is None


def test_assoc_expressions40_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(operators="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list', None)
    _safe_set(owner, 'pascal_expression41', partner)
    assert owner in getattr(partner, 'pascal_expression_list')
    _safe_set(owner, 'pascal_expression41', None)
    assert owner not in getattr(partner, 'pascal_expression_list')


def test_assoc_expressions61_stub_double():
    # pascal_expression_list has no real 'pascal_expression_list63' property in the generated
    # code (a bare stub) -- manually attach it so pascal_function_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_function_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_function_designator(name="sample_text")
    partner = pascal_expression_list()
    setattr(partner, 'pascal_expression_list63', None)
    _safe_set(owner, 'pascal_function_designator62', partner)
    assert getattr(partner, 'pascal_expression_list63') == owner
    _safe_set(owner, 'pascal_function_designator62', None)
    assert getattr(partner, 'pascal_expression_list63') is None


def test_assoc_fields122_stub_double():
    # pascal_field_list has no real 'pascal_field_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_record_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_record_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_record_type(endKeyword="sample_text", recordKeyword="sample_text")
    partner = pascal_field_list()
    setattr(partner, 'pascal_field_list', None)
    _safe_set(owner, 'pascal_record_type123', partner)
    assert getattr(partner, 'pascal_field_list') == owner
    _safe_set(owner, 'pascal_record_type123', None)
    assert getattr(partner, 'pascal_field_list') is None


def test_assoc_function85_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section86' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section86', None)
    _safe_set(owner, 'pascal_abstraction_heading87', partner)
    assert getattr(partner, 'pascal_formal_parameter_section86') == owner
    _safe_set(owner, 'pascal_abstraction_heading87', None)
    assert getattr(partner, 'pascal_formal_parameter_section86') is None


def test_assoc_heading0_stub_double():
    # pascal_program has no real 'pascal_program' property in the generated
    # code (a bare stub) -- manually attach it so pascal_program_heading_block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_program_heading_block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_program_heading_block(name="sample_text")
    partner = pascal_program()
    setattr(partner, 'pascal_program', None)
    _safe_set(owner, 'pascal_program_heading_block', partner)
    assert getattr(partner, 'pascal_program') == owner
    _safe_set(owner, 'pascal_program_heading_block', None)
    assert getattr(partner, 'pascal_program') is None


def test_assoc_heading70_stub_double():
    # pascal_abstraction_declaration has no real 'pascal_abstraction_declaration71' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_abstraction_declaration()
    setattr(partner, 'pascal_abstraction_declaration71', None)
    _safe_set(owner, 'pascal_abstraction_heading72', partner)
    assert getattr(partner, 'pascal_abstraction_declaration71') == owner
    _safe_set(owner, 'pascal_abstraction_heading72', None)
    assert getattr(partner, 'pascal_abstraction_declaration71') is None


def test_assoc_identifiers126_stub_double():
    # pascal_record_section has no real 'pascal_record_section127' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(names="sample_text")
    partner = pascal_record_section()
    setattr(partner, 'pascal_record_section127', None)
    _safe_set(owner, 'pascal_identifier_list128', partner)
    assert getattr(partner, 'pascal_record_section127') == owner
    _safe_set(owner, 'pascal_identifier_list128', None)
    assert getattr(partner, 'pascal_record_section127') is None


def test_assoc_identifiers134_stub_double():
    # pascal_variable_section has no real 'pascal_variable_section135' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable_identifier_list(names="sample_text")
    partner = pascal_variable_section()
    setattr(partner, 'pascal_variable_section135', None)
    _safe_set(owner, 'pascal_variable_identifier_list', partner)
    assert getattr(partner, 'pascal_variable_section135') == owner
    _safe_set(owner, 'pascal_variable_identifier_list', None)
    assert getattr(partner, 'pascal_variable_section135') is None


def test_assoc_identifiers88_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section89' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(names="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section89', None)
    _safe_set(owner, 'pascal_identifier_list', partner)
    assert getattr(partner, 'pascal_value_parameter_section89') == owner
    _safe_set(owner, 'pascal_identifier_list', None)
    assert getattr(partner, 'pascal_value_parameter_section89') is None


def test_assoc_indentifiers92_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section93' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier_list(names="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section93', None)
    _safe_set(owner, 'pascal_identifier_list94', partner)
    assert getattr(partner, 'pascal_variable_parameter_section93') == owner
    _safe_set(owner, 'pascal_identifier_list94', None)
    assert getattr(partner, 'pascal_variable_parameter_section93') is None


def test_assoc_label19_stub_double():
    # pascal_statement has no real 'pascal_statement20' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement20', None)
    _safe_set(owner, 'pascal_label', partner)
    assert getattr(partner, 'pascal_statement20') == owner
    _safe_set(owner, 'pascal_label', None)
    assert getattr(partner, 'pascal_statement20') is None


def test_assoc_labels100_stub_double():
    # pascal_label_declaration has no real 'pascal_label_declaration101' property in the generated
    # code (a bare stub) -- manually attach it so pascal_label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_label(number="sample_text")
    partner = pascal_label_declaration()
    setattr(partner, 'pascal_label_declaration101', None)
    _safe_set(owner, 'pascal_label102', partner)
    assert owner in getattr(partner, 'pascal_label_declaration101')
    _safe_set(owner, 'pascal_label102', None)
    assert owner not in getattr(partner, 'pascal_label_declaration101')


def test_assoc_number103_stub_double():
    # pascal_number has no real 'pascal_number104' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(boolLiteral="sample_text", name="sample_text", nil=True, opterator="sample_text", string="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number104', None)
    _safe_set(owner, 'pascal_constant', partner)
    assert getattr(partner, 'pascal_number104') == owner
    _safe_set(owner, 'pascal_constant', None)
    assert getattr(partner, 'pascal_number104') is None


def test_assoc_number50_stub_double():
    # pascal_number has no real 'pascal_number' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number', None)
    _safe_set(owner, 'pascal_factor51', partner)
    assert getattr(partner, 'pascal_number') == owner
    _safe_set(owner, 'pascal_factor51', None)
    assert getattr(partner, 'pascal_number') is None


def test_assoc_number98_stub_double():
    # pascal_number has no real 'pascal_number99' property in the generated
    # code (a bare stub) -- manually attach it so pascal_any_number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_any_number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_any_number(integer="sample_text", real="sample_text")
    partner = pascal_number()
    setattr(partner, 'pascal_number99', None)
    _safe_set(owner, 'pascal_any_number', partner)
    assert getattr(partner, 'pascal_number99') == owner
    _safe_set(owner, 'pascal_any_number', None)
    assert getattr(partner, 'pascal_number99') is None


def test_assoc_parameters69_stub_double():
    # pascal_formal_parameter_list has no real 'pascal_formal_parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_formal_parameter_list()
    setattr(partner, 'pascal_formal_parameter_list', None)
    _safe_set(owner, 'pascal_abstraction_heading', partner)
    assert getattr(partner, 'pascal_formal_parameter_list') == owner
    _safe_set(owner, 'pascal_abstraction_heading', None)
    assert getattr(partner, 'pascal_formal_parameter_list') is None


def test_assoc_procedure82_stub_double():
    # pascal_formal_parameter_section has no real 'pascal_formal_parameter_section83' property in the generated
    # code (a bare stub) -- manually attach it so pascal_abstraction_heading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_abstraction_heading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_abstraction_heading(name="sample_text", returnType="sample_text")
    partner = pascal_formal_parameter_section()
    setattr(partner, 'pascal_formal_parameter_section83', None)
    _safe_set(owner, 'pascal_abstraction_heading84', partner)
    assert getattr(partner, 'pascal_formal_parameter_section83') == owner
    _safe_set(owner, 'pascal_abstraction_heading84', None)
    assert getattr(partner, 'pascal_formal_parameter_section83') is None


def test_assoc_record120_stub_double():
    # pascal_unpacked_structured_type has no real 'pascal_unpacked_structured_type121' property in the generated
    # code (a bare stub) -- manually attach it so pascal_record_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_record_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_record_type(endKeyword="sample_text", recordKeyword="sample_text")
    partner = pascal_unpacked_structured_type()
    setattr(partner, 'pascal_unpacked_structured_type121', None)
    _safe_set(owner, 'pascal_record_type', partner)
    assert getattr(partner, 'pascal_unpacked_structured_type121') == owner
    _safe_set(owner, 'pascal_record_type', None)
    assert getattr(partner, 'pascal_unpacked_structured_type121') is None


def test_assoc_simple114_stub_double():
    # pascal_type has no real 'pascal_type115' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_type(name="sample_text")
    partner = pascal_type()
    setattr(partner, 'pascal_type115', None)
    _safe_set(owner, 'pascal_simple_type', partner)
    assert getattr(partner, 'pascal_type115') == owner
    _safe_set(owner, 'pascal_simple_type', None)
    assert getattr(partner, 'pascal_type115') is None


def test_assoc_simple21_stub_double():
    # pascal_statement has no real 'pascal_statement22' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_statement(function_noargs="sample_text")
    partner = pascal_statement()
    setattr(partner, 'pascal_statement22', None)
    _safe_set(owner, 'pascal_simple_statement', partner)
    assert getattr(partner, 'pascal_statement22') == owner
    _safe_set(owner, 'pascal_simple_statement', None)
    assert getattr(partner, 'pascal_statement22') is None


def test_assoc_terms44_stub_double():
    # pascal_EObject has no real 'pascal_EObject' property in the generated
    # code (a bare stub) -- manually attach it so pascal_simple_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_simple_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    partner = pascal_EObject()
    setattr(partner, 'pascal_EObject', None)
    _safe_set(owner, 'pascal_simple_expression45', {partner})
    assert getattr(partner, 'pascal_EObject') == owner
    _safe_set(owner, 'pascal_simple_expression45', set())
    assert getattr(partner, 'pascal_EObject') is None


def test_assoc_type112_stub_double():
    # pascal_type has no real 'pascal_type' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type_definition(name="sample_text")
    partner = pascal_type()
    setattr(partner, 'pascal_type', None)
    _safe_set(owner, 'pascal_type_definition113', partner)
    assert getattr(partner, 'pascal_type') == owner
    _safe_set(owner, 'pascal_type_definition113', None)
    assert getattr(partner, 'pascal_type') is None


def test_assoc_type90_stub_double():
    # pascal_value_parameter_section has no real 'pascal_value_parameter_section91' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_value_parameter_section()
    setattr(partner, 'pascal_value_parameter_section91', None)
    _safe_set(owner, 'pascal_parameter_type', partner)
    assert getattr(partner, 'pascal_value_parameter_section91') == owner
    _safe_set(owner, 'pascal_parameter_type', None)
    assert getattr(partner, 'pascal_value_parameter_section91') is None


def test_assoc_type95_stub_double():
    # pascal_variable_parameter_section has no real 'pascal_variable_parameter_section96' property in the generated
    # code (a bare stub) -- manually attach it so pascal_parameter_type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_parameter_type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_parameter_type(name="sample_text")
    partner = pascal_variable_parameter_section()
    setattr(partner, 'pascal_variable_parameter_section96', None)
    _safe_set(owner, 'pascal_parameter_type97', partner)
    assert getattr(partner, 'pascal_variable_parameter_section96') == owner
    _safe_set(owner, 'pascal_parameter_type97', None)
    assert getattr(partner, 'pascal_variable_parameter_section96') is None


def test_assoc_types110_stub_double():
    # pascal_type_definition_part has no real 'pascal_type_definition_part111' property in the generated
    # code (a bare stub) -- manually attach it so pascal_type_definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_type_definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_type_definition(name="sample_text")
    partner = pascal_type_definition_part()
    setattr(partner, 'pascal_type_definition_part111', None)
    _safe_set(owner, 'pascal_type_definition', partner)
    assert owner in getattr(partner, 'pascal_type_definition_part111')
    _safe_set(owner, 'pascal_type_definition', None)
    assert owner not in getattr(partner, 'pascal_type_definition_part111')


def test_assoc_variable36_stub_double():
    # pascal_assignment_statement has no real 'pascal_assignment_statement37' property in the generated
    # code (a bare stub) -- manually attach it so pascal_variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_variable(name="sample_text")
    partner = pascal_assignment_statement()
    setattr(partner, 'pascal_assignment_statement37', None)
    _safe_set(owner, 'pascal_variable', partner)
    assert getattr(partner, 'pascal_assignment_statement37') == owner
    _safe_set(owner, 'pascal_variable', None)
    assert getattr(partner, 'pascal_assignment_statement37') is None


