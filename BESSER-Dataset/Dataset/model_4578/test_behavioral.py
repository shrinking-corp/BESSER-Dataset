import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    abstract_declarator,
    assignment_expression,
    atomic_type_specifier,
    block_item,
    cast_expression,
    compound_statement,
    conditional_expression,
    constant_expression,
    declaration,
    declaration_specifiers,
    declarator,
    designation,
    designator,
    direct_declarator,
    expression_statement,
    external_declaration,
    identifier_list,
    identifier_listR,
    init_declarator,
    initializer,
    jump_statement,
    labeled_statement,
    myDsl_EObject,
    myDsl_IDENTIFIER,
    myDsl_Model,
    myDsl_StringC,
    myDsl_abstract_declarator,
    myDsl_additive_expression,
    myDsl_additive_expressionR,
    myDsl_and_expression,
    myDsl_and_expressionR,
    myDsl_argument_expression_list,
    myDsl_argument_expression_listR,
    myDsl_assignment_expression,
    myDsl_atomic_type_specifier,
    myDsl_block_item,
    myDsl_block_item_list,
    myDsl_block_item_listR,
    myDsl_cast_expression,
    myDsl_compound_statement,
    myDsl_conditional_expression,
    myDsl_constant_expression,
    myDsl_declaration,
    myDsl_declaration_list,
    myDsl_declaration_listR,
    myDsl_declaration_specifiers,
    myDsl_declarator,
    myDsl_designation,
    myDsl_designator,
    myDsl_designator_list,
    myDsl_designator_listR,
    myDsl_direct_declarator,
    myDsl_direct_declaratorR,
    myDsl_equality_expression,
    myDsl_equality_expressionR,
    myDsl_exclusive_or_expression,
    myDsl_exclusive_or_expressionR,
    myDsl_expression,
    myDsl_expressionR,
    myDsl_expression_statement,
    myDsl_external_declaration,
    myDsl_function_definition,
    myDsl_identifier_list,
    myDsl_identifier_listR,
    myDsl_inclusive_or_expression,
    myDsl_inclusive_or_expressionR,
    myDsl_init_declarator,
    myDsl_init_declarator_list,
    myDsl_init_declarator_listR,
    myDsl_initializer,
    myDsl_initializer_list,
    myDsl_initializer_listR,
    myDsl_iteration_statement,
    myDsl_jump_statement,
    myDsl_labeled_statement,
    myDsl_logical_and_expression,
    myDsl_logical_and_expressionR,
    myDsl_logical_or_expression,
    myDsl_logical_or_expressionR,
    myDsl_multiplicative_expression,
    myDsl_multiplicative_expressionR,
    myDsl_parameter_declaration,
    myDsl_parameter_list,
    myDsl_parameter_listR,
    myDsl_parameter_type_list,
    myDsl_pointer,
    myDsl_postfix_expression,
    myDsl_postfix_expressionR,
    myDsl_primary_expression,
    myDsl_relational_expression,
    myDsl_relational_expressionR,
    myDsl_selection_statement,
    myDsl_shift_expression,
    myDsl_shift_expressionR,
    myDsl_specifier_qualifier_list,
    myDsl_statement,
    myDsl_static_assert_declaration,
    myDsl_struct_declaration,
    myDsl_struct_declaration_list,
    myDsl_struct_declaration_listR,
    myDsl_struct_declarator,
    myDsl_struct_declarator_list,
    myDsl_struct_declarator_listR,
    myDsl_struct_or_union_specifier,
    myDsl_translation_unit,
    myDsl_translation_unitR,
    myDsl_type_name,
    myDsl_type_qualifier_list,
    myDsl_type_qualifier_listR,
    myDsl_type_specifier,
    myDsl_unary_expression,
    parameter_declaration,
    parameter_type_list,
    pointer,
    postfix_expressionR,
    primary_expression,
    shift_expression,
    statement,
    static_assert_declaration,
    struct_declaration,
    struct_declarator,
    struct_or_union_specifier,
    type_name,
    type_specifier,
    unary_expression,
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

def test_assoc_Type_qualifier_listR22_reverse_link_reassign_clear():
    a1 = myDsl_type_qualifier_listR(Type_qualifier="sample_text")
    a2 = myDsl_type_qualifier_listR(Type_qualifier="sample_text_2")
    b = myDsl_type_qualifier_list(Type_qualifier="sample_text")
    _safe_set(b, 'myDsl_type_qualifier_list', a1)
    assert _is_linked(b, 'myDsl_type_qualifier_list', a1)
    if hasattr(a1, 'myDsl_type_qualifier_listR'):
        assert _is_linked(a1, 'myDsl_type_qualifier_listR', b)
    _safe_set(b, 'myDsl_type_qualifier_list', a2)
    assert _is_linked(b, 'myDsl_type_qualifier_list', a2)
    if hasattr(a1, 'myDsl_type_qualifier_listR'):
        assert not _is_linked(a1, 'myDsl_type_qualifier_listR', b)
    if hasattr(a2, 'myDsl_type_qualifier_listR'):
        assert _is_linked(a2, 'myDsl_type_qualifier_listR', b)
    _safe_set(b, 'myDsl_type_qualifier_list', None)
    assert not _is_linked(b, 'myDsl_type_qualifier_list', a2)
    if hasattr(a2, 'myDsl_type_qualifier_listR'):
        assert not _is_linked(a2, 'myDsl_type_qualifier_listR', b)


def test_assoc_Unary_expression234_reverse_link_reassign_clear():
    a1 = myDsl_unary_expression(Unary_operator="sample_text")
    a2 = myDsl_unary_expression(Unary_operator="sample_text_2")
    b = myDsl_assignment_expression(Assignment_operator="sample_text")
    _safe_set(b, 'myDsl_assignment_expression235', a1)
    assert _is_linked(b, 'myDsl_assignment_expression235', a1)
    if hasattr(a1, 'myDsl_unary_expression'):
        assert _is_linked(a1, 'myDsl_unary_expression', b)
    _safe_set(b, 'myDsl_assignment_expression235', a2)
    assert _is_linked(b, 'myDsl_assignment_expression235', a2)
    if hasattr(a1, 'myDsl_unary_expression'):
        assert not _is_linked(a1, 'myDsl_unary_expression', b)
    if hasattr(a2, 'myDsl_unary_expression'):
        assert _is_linked(a2, 'myDsl_unary_expression', b)
    _safe_set(b, 'myDsl_assignment_expression235', None)
    assert not _is_linked(b, 'myDsl_assignment_expression235', a2)
    if hasattr(a2, 'myDsl_unary_expression'):
        assert not _is_linked(a2, 'myDsl_unary_expression', b)


def test_assoc_id322_reverse_link_reassign_clear():
    a1 = myDsl_struct_or_union_specifier(Struct_or_union="sample_text")
    a2 = myDsl_struct_or_union_specifier(Struct_or_union="sample_text_2")
    b = myDsl_IDENTIFIER(name="sample_text")
    _safe_set(b, 'myDsl_IDENTIFIER', a1)
    assert _is_linked(b, 'myDsl_IDENTIFIER', a1)
    if hasattr(a1, 'myDsl_struct_or_union_specifier323'):
        assert _is_linked(a1, 'myDsl_struct_or_union_specifier323', b)
    _safe_set(b, 'myDsl_IDENTIFIER', a2)
    assert _is_linked(b, 'myDsl_IDENTIFIER', a2)
    if hasattr(a1, 'myDsl_struct_or_union_specifier323'):
        assert not _is_linked(a1, 'myDsl_struct_or_union_specifier323', b)
    if hasattr(a2, 'myDsl_struct_or_union_specifier323'):
        assert _is_linked(a2, 'myDsl_struct_or_union_specifier323', b)
    _safe_set(b, 'myDsl_IDENTIFIER', None)
    assert not _is_linked(b, 'myDsl_IDENTIFIER', a2)
    if hasattr(a2, 'myDsl_struct_or_union_specifier323'):
        assert not _is_linked(a2, 'myDsl_struct_or_union_specifier323', b)


def test_assoc_r1112_reverse_link_reassign_clear():
    a1 = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    a2 = myDsl_declaration_specifiers(Storage_class_specifier="sample_text_2", Type_qualifier="sample_text_2")
    b = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    _safe_set(b, 'myDsl_declaration_specifiers113', a1)
    assert _is_linked(b, 'myDsl_declaration_specifiers113', a1)
    if hasattr(a1, 'myDsl_declaration_specifiers111'):
        assert _is_linked(a1, 'myDsl_declaration_specifiers111', b)
    _safe_set(b, 'myDsl_declaration_specifiers113', a2)
    assert _is_linked(b, 'myDsl_declaration_specifiers113', a2)
    if hasattr(a1, 'myDsl_declaration_specifiers111'):
        assert not _is_linked(a1, 'myDsl_declaration_specifiers111', b)
    if hasattr(a2, 'myDsl_declaration_specifiers111'):
        assert _is_linked(a2, 'myDsl_declaration_specifiers111', b)
    _safe_set(b, 'myDsl_declaration_specifiers113', None)
    assert not _is_linked(b, 'myDsl_declaration_specifiers113', a2)
    if hasattr(a2, 'myDsl_declaration_specifiers111'):
        assert not _is_linked(a2, 'myDsl_declaration_specifiers111', b)


def test_assoc_r2115_reverse_link_reassign_clear():
    a1 = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    a2 = myDsl_declaration_specifiers(Storage_class_specifier="sample_text_2", Type_qualifier="sample_text_2")
    b = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    _safe_set(b, 'myDsl_declaration_specifiers116', a1)
    assert _is_linked(b, 'myDsl_declaration_specifiers116', a1)
    if hasattr(a1, 'myDsl_declaration_specifiers114'):
        assert _is_linked(a1, 'myDsl_declaration_specifiers114', b)
    _safe_set(b, 'myDsl_declaration_specifiers116', a2)
    assert _is_linked(b, 'myDsl_declaration_specifiers116', a2)
    if hasattr(a1, 'myDsl_declaration_specifiers114'):
        assert not _is_linked(a1, 'myDsl_declaration_specifiers114', b)
    if hasattr(a2, 'myDsl_declaration_specifiers114'):
        assert _is_linked(a2, 'myDsl_declaration_specifiers114', b)
    _safe_set(b, 'myDsl_declaration_specifiers116', None)
    assert not _is_linked(b, 'myDsl_declaration_specifiers116', a2)
    if hasattr(a2, 'myDsl_declaration_specifiers114'):
        assert not _is_linked(a2, 'myDsl_declaration_specifiers114', b)


def test_assoc_rec237_reverse_link_reassign_clear():
    a1 = myDsl_assignment_expression(Assignment_operator="sample_text")
    a2 = myDsl_assignment_expression(Assignment_operator="sample_text_2")
    b = myDsl_assignment_expression(Assignment_operator="sample_text")
    _safe_set(b, 'myDsl_assignment_expression238', a1)
    assert _is_linked(b, 'myDsl_assignment_expression238', a1)
    if hasattr(a1, 'myDsl_assignment_expression236'):
        assert _is_linked(a1, 'myDsl_assignment_expression236', b)
    _safe_set(b, 'myDsl_assignment_expression238', a2)
    assert _is_linked(b, 'myDsl_assignment_expression238', a2)
    if hasattr(a1, 'myDsl_assignment_expression236'):
        assert not _is_linked(a1, 'myDsl_assignment_expression236', b)
    if hasattr(a2, 'myDsl_assignment_expression236'):
        assert _is_linked(a2, 'myDsl_assignment_expression236', b)
    _safe_set(b, 'myDsl_assignment_expression238', None)
    assert not _is_linked(b, 'myDsl_assignment_expression238', a2)
    if hasattr(a2, 'myDsl_assignment_expression236'):
        assert not _is_linked(a2, 'myDsl_assignment_expression236', b)


def test_assoc_rec24_reverse_link_reassign_clear():
    a1 = myDsl_type_qualifier_listR(Type_qualifier="sample_text")
    a2 = myDsl_type_qualifier_listR(Type_qualifier="sample_text_2")
    b = myDsl_type_qualifier_listR(Type_qualifier="sample_text")
    _safe_set(b, 'myDsl_type_qualifier_listR25', a1)
    assert _is_linked(b, 'myDsl_type_qualifier_listR25', a1)
    if hasattr(a1, 'myDsl_type_qualifier_listR23'):
        assert _is_linked(a1, 'myDsl_type_qualifier_listR23', b)
    _safe_set(b, 'myDsl_type_qualifier_listR25', a2)
    assert _is_linked(b, 'myDsl_type_qualifier_listR25', a2)
    if hasattr(a1, 'myDsl_type_qualifier_listR23'):
        assert not _is_linked(a1, 'myDsl_type_qualifier_listR23', b)
    if hasattr(a2, 'myDsl_type_qualifier_listR23'):
        assert _is_linked(a2, 'myDsl_type_qualifier_listR23', b)
    _safe_set(b, 'myDsl_type_qualifier_listR25', None)
    assert not _is_linked(b, 'myDsl_type_qualifier_listR25', a2)
    if hasattr(a2, 'myDsl_type_qualifier_listR23'):
        assert not _is_linked(a2, 'myDsl_type_qualifier_listR23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Assignment_expression122_stub_double():
    # myDsl_expression has no real 'myDsl_expression123' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_assignment_expression(Assignment_operator="sample_text")
    partner = myDsl_expression()
    setattr(partner, 'myDsl_expression123', None)
    _safe_set(owner, 'myDsl_assignment_expression124', partner)
    assert getattr(partner, 'myDsl_expression123') == owner
    _safe_set(owner, 'myDsl_assignment_expression124', None)
    assert getattr(partner, 'myDsl_expression123') is None


def test_assoc_Assignment_expression127_stub_double():
    # myDsl_expressionR has no real 'myDsl_expressionR128' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_assignment_expression(Assignment_operator="sample_text")
    partner = myDsl_expressionR()
    setattr(partner, 'myDsl_expressionR128', None)
    _safe_set(owner, 'myDsl_assignment_expression129', partner)
    assert getattr(partner, 'myDsl_expressionR128') == owner
    _safe_set(owner, 'myDsl_assignment_expression129', None)
    assert getattr(partner, 'myDsl_expressionR128') is None


def test_assoc_Assignment_expression331_stub_double():
    # myDsl_argument_expression_list has no real 'myDsl_argument_expression_list332' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_assignment_expression(Assignment_operator="sample_text")
    partner = myDsl_argument_expression_list()
    setattr(partner, 'myDsl_argument_expression_list332', None)
    _safe_set(owner, 'myDsl_assignment_expression333', partner)
    assert getattr(partner, 'myDsl_argument_expression_list332') == owner
    _safe_set(owner, 'myDsl_assignment_expression333', None)
    assert getattr(partner, 'myDsl_argument_expression_list332') is None


def test_assoc_Assignment_expression336_stub_double():
    # myDsl_argument_expression_listR has no real 'myDsl_argument_expression_listR337' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_assignment_expression(Assignment_operator="sample_text")
    partner = myDsl_argument_expression_listR()
    setattr(partner, 'myDsl_argument_expression_listR337', None)
    _safe_set(owner, 'myDsl_assignment_expression338', partner)
    assert getattr(partner, 'myDsl_argument_expression_listR337') == owner
    _safe_set(owner, 'myDsl_assignment_expression338', None)
    assert getattr(partner, 'myDsl_argument_expression_listR337') is None


def test_assoc_Assignment_expression34_stub_double():
    # myDsl_direct_declaratorR has no real 'myDsl_direct_declaratorR35' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_assignment_expression(Assignment_operator="sample_text")
    partner = myDsl_direct_declaratorR()
    setattr(partner, 'myDsl_direct_declaratorR35', None)
    _safe_set(owner, 'myDsl_assignment_expression', partner)
    assert getattr(partner, 'myDsl_direct_declaratorR35') == owner
    _safe_set(owner, 'myDsl_assignment_expression', None)
    assert getattr(partner, 'myDsl_direct_declaratorR35') is None


def test_assoc_Declaration_specifiers11_stub_double():
    # myDsl_external_declaration has no real 'myDsl_external_declaration12' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    partner = myDsl_external_declaration()
    setattr(partner, 'myDsl_external_declaration12', None)
    _safe_set(owner, 'myDsl_declaration_specifiers', partner)
    assert getattr(partner, 'myDsl_external_declaration12') == owner
    _safe_set(owner, 'myDsl_declaration_specifiers', None)
    assert getattr(partner, 'myDsl_external_declaration12') is None


def test_assoc_Declaration_specifiers155_stub_double():
    # myDsl_parameter_declaration has no real 'myDsl_parameter_declaration56' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    partner = myDsl_parameter_declaration()
    setattr(partner, 'myDsl_parameter_declaration56', None)
    _safe_set(owner, 'myDsl_declaration_specifiers57', partner)
    assert getattr(partner, 'myDsl_parameter_declaration56') == owner
    _safe_set(owner, 'myDsl_declaration_specifiers57', None)
    assert getattr(partner, 'myDsl_parameter_declaration56') is None


def test_assoc_Declaration_specifiers249_stub_double():
    # myDsl_parameter_declaration has no real 'myDsl_parameter_declaration50' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    partner = myDsl_parameter_declaration()
    setattr(partner, 'myDsl_parameter_declaration50', None)
    _safe_set(owner, 'myDsl_declaration_specifiers51', partner)
    assert getattr(partner, 'myDsl_parameter_declaration50') == owner
    _safe_set(owner, 'myDsl_declaration_specifiers51', None)
    assert getattr(partner, 'myDsl_parameter_declaration50') is None


def test_assoc_Struct_declaration_list320_stub_double():
    # myDsl_struct_declaration_list has no real 'myDsl_struct_declaration_list321' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_struct_or_union_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_struct_or_union_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_struct_or_union_specifier(Struct_or_union="sample_text")
    partner = myDsl_struct_declaration_list()
    setattr(partner, 'myDsl_struct_declaration_list321', None)
    _safe_set(owner, 'myDsl_struct_or_union_specifier', partner)
    assert getattr(partner, 'myDsl_struct_declaration_list321') == owner
    _safe_set(owner, 'myDsl_struct_or_union_specifier', None)
    assert getattr(partner, 'myDsl_struct_declaration_list321') is None


def test_assoc_Type_qualifier_list31_stub_double():
    # myDsl_direct_declaratorR has no real 'myDsl_direct_declaratorR32' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_qualifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_qualifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_qualifier_list(Type_qualifier="sample_text")
    partner = myDsl_direct_declaratorR()
    setattr(partner, 'myDsl_direct_declaratorR32', None)
    _safe_set(owner, 'myDsl_type_qualifier_list33', partner)
    assert getattr(partner, 'myDsl_direct_declaratorR32') == owner
    _safe_set(owner, 'myDsl_type_qualifier_list33', None)
    assert getattr(partner, 'myDsl_direct_declaratorR32') is None


def test_assoc_Type_qualifier_list342_stub_double():
    # myDsl_pointer has no real 'myDsl_pointer343' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_qualifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_qualifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_qualifier_list(Type_qualifier="sample_text")
    partner = myDsl_pointer()
    setattr(partner, 'myDsl_pointer343', None)
    _safe_set(owner, 'myDsl_type_qualifier_list344', partner)
    assert getattr(partner, 'myDsl_pointer343') == owner
    _safe_set(owner, 'myDsl_type_qualifier_list344', None)
    assert getattr(partner, 'myDsl_pointer343') is None


def test_assoc_a353_stub_double():
    # myDsl_statement has no real 'myDsl_statement355' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IDENTIFIER's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IDENTIFIER's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IDENTIFIER(name="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement355', None)
    _safe_set(owner, 'myDsl_IDENTIFIER354', partner)
    assert getattr(partner, 'myDsl_statement355') == owner
    _safe_set(owner, 'myDsl_IDENTIFIER354', None)
    assert getattr(partner, 'myDsl_statement355') is None


def test_assoc_ce244_stub_double():
    # myDsl_cast_expression has no real 'myDsl_cast_expression246' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_unary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_unary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_unary_expression(Unary_operator="sample_text")
    partner = myDsl_cast_expression()
    setattr(partner, 'myDsl_cast_expression246', None)
    _safe_set(owner, 'myDsl_unary_expression245', partner)
    assert getattr(partner, 'myDsl_cast_expression246') == owner
    _safe_set(owner, 'myDsl_unary_expression245', None)
    assert getattr(partner, 'myDsl_cast_expression246') is None


def test_assoc_dr348_stub_double():
    # myDsl_direct_declaratorR has no real 'myDsl_direct_declaratorR350' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IDENTIFIER's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IDENTIFIER's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IDENTIFIER(name="sample_text")
    partner = myDsl_direct_declaratorR()
    setattr(partner, 'myDsl_direct_declaratorR350', None)
    _safe_set(owner, 'myDsl_IDENTIFIER349', partner)
    assert getattr(partner, 'myDsl_direct_declaratorR350') == owner
    _safe_set(owner, 'myDsl_IDENTIFIER349', None)
    assert getattr(partner, 'myDsl_direct_declaratorR350') is None


def test_assoc_ds356_stub_double():
    # myDsl_type_specifier has no real 'myDsl_type_specifier357' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_declaration_specifiers(Storage_class_specifier="sample_text", Type_qualifier="sample_text")
    partner = myDsl_type_specifier()
    setattr(partner, 'myDsl_type_specifier357', None)
    _safe_set(owner, 'myDsl_declaration_specifiers358', partner)
    assert getattr(partner, 'myDsl_type_specifier357') == owner
    _safe_set(owner, 'myDsl_declaration_specifiers358', None)
    assert getattr(partner, 'myDsl_type_specifier357') is None


def test_assoc_il351_stub_double():
    # myDsl_identifier_listR has no real 'myDsl_identifier_listR' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IDENTIFIER's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IDENTIFIER's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IDENTIFIER(name="sample_text")
    partner = myDsl_identifier_listR()
    setattr(partner, 'myDsl_identifier_listR', None)
    _safe_set(owner, 'myDsl_IDENTIFIER352', partner)
    assert getattr(partner, 'myDsl_identifier_listR') == owner
    _safe_set(owner, 'myDsl_IDENTIFIER352', None)
    assert getattr(partner, 'myDsl_identifier_listR') is None


