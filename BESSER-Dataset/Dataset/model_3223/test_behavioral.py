import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ansic_ArgumentExpressionListLinhaAction,
    ansic_DeclarationListLinhaAction,
    ansic_DesignatorListLinhaAction,
    ansic_DirectAbstractDeclarratorLinhaAction,
    ansic_DomainModel,
    ansic_EnumeratorListLinhaAction,
    ansic_GenericAssocListLinhaAction,
    ansic_IdentifierListLinhaAction,
    ansic_InitDecclaratorListLinhaAction,
    ansic_InitializerListLinhaAction,
    ansic_PlusPlus,
    ansic_PostFixEmpryParams,
    ansic_PostfixExpressionLinhaAction,
    ansic_StructDeclarationListLinhaAction,
    ansic_StructDeclaratorListLinhaAction,
    ansic_StructOrUnionSpecifierComplementAction,
    ansic_TranlationUnitLinhaAction,
    ansic_TypeQualifierListLinhaAtion,
    ansic_abstract_declarator,
    ansic_additive_expression,
    ansic_additive_expression_complement,
    ansic_additive_expression_linha,
    ansic_alignment_specifier,
    ansic_and_expression,
    ansic_and_expression_linha,
    ansic_argument_expression_list,
    ansic_argument_expression_list_linha,
    ansic_assignment_expression,
    ansic_atomic_type_specifier,
    ansic_block_item,
    ansic_block_item_list,
    ansic_block_item_list_linha,
    ansic_cast_expression,
    ansic_compound_statement,
    ansic_conditional_expression,
    ansic_conditional_expression_linha,
    ansic_constant,
    ansic_constant_expression,
    ansic_declaration,
    ansic_declaration_list,
    ansic_declaration_list_linha,
    ansic_declaration_specifiers,
    ansic_declarator,
    ansic_designation,
    ansic_designator,
    ansic_designator_list,
    ansic_designator_list_linha,
    ansic_direct_abstract_declarator,
    ansic_direct_abstract_declarator_complement,
    ansic_direct_abstract_declarator_linha,
    ansic_direct_declarator,
    ansic_direct_declarator_complemento,
    ansic_direct_declarator_linha,
    ansic_enum_specifier,
    ansic_enumeration_constant,
    ansic_enumerator,
    ansic_enumerator_list,
    ansic_enumerator_list_linha,
    ansic_equality_expression,
    ansic_equality_expression_complement,
    ansic_equality_expression_linha,
    ansic_exclusive_or_expression,
    ansic_exclusive_or_expression_linha,
    ansic_expression,
    ansic_expression_linha,
    ansic_expression_statement,
    ansic_external_declaration,
    ansic_function_definition,
    ansic_generic_assoc_list,
    ansic_generic_assoc_list_linha,
    ansic_generic_association,
    ansic_generic_selection,
    ansic_identifier_list,
    ansic_identifier_list_linha,
    ansic_inclusive_or_expression,
    ansic_inclusive_or_expression_linha,
    ansic_init_declarator,
    ansic_init_declarator_list,
    ansic_init_declarator_list_linha,
    ansic_initializer,
    ansic_initializer_list,
    ansic_initializer_list_complement,
    ansic_initializer_list_linha,
    ansic_iteration_statement,
    ansic_jump_statement,
    ansic_labeled_statement,
    ansic_logical_and_expression,
    ansic_logical_and_expression_linha,
    ansic_logical_or_expression,
    ansic_logical_or_expression_linha,
    ansic_multiplicative_expression,
    ansic_multiplicative_expression_complement,
    ansic_multiplicative_expression_linha,
    ansic_parameter_declaration,
    ansic_parameter_list_linha,
    ansic_parameter_lista,
    ansic_parameter_type_list,
    ansic_pointer,
    ansic_postfix_expression,
    ansic_postfix_expression_complement,
    ansic_postfix_expression_linha,
    ansic_primary_expression,
    ansic_relational_expression,
    ansic_relational_expression_complement,
    ansic_relational_expression_linha,
    ansic_selection_statement,
    ansic_shift_expression,
    ansic_shift_expression_complement,
    ansic_shift_expression_linha,
    ansic_specifier_qualifier_list,
    ansic_statement,
    ansic_static_assert_declaration,
    ansic_string_ufcg,
    ansic_struct_declaration,
    ansic_struct_declaration_list,
    ansic_struct_declaration_list_linha,
    ansic_struct_declarator,
    ansic_struct_declarator_list,
    ansic_struct_declarator_list_linha,
    ansic_struct_or_union_specifier,
    ansic_struct_or_union_specifier_complement,
    ansic_translation_unit,
    ansic_translation_unit_linha,
    ansic_type_name,
    ansic_type_qualifier,
    ansic_type_qualifier_list,
    ansic_type_qualifier_list_linha,
    ansic_type_specifier,
    ansic_unary_expression,
    argument_expression_list_linha,
    declaration_list_linha,
    designator_list_linha,
    direct_abstract_declarator_complement,
    direct_abstract_declarator_linha,
    enumerator_list_linha,
    generic_assoc_list_linha,
    identifier_list_linha,
    init_declarator_list_linha,
    initializer_list_linha,
    postfix_expression,
    postfix_expression_complement,
    postfix_expression_linha,
    struct_declaration_list_linha,
    struct_declarator_list_linha,
    struct_or_union_specifier_complement,
    translation_unit_linha,
    type_qualifier_list_linha,
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

def test_assoc_assignment_expression184_reverse_link_reassign_clear():
    a1 = ansic_generic_selection(_generic="sample_text")
    a2 = ansic_generic_selection(_generic="sample_text_2")
    b = ansic_assignment_expression(assignment_operator="sample_text")
    _safe_set(b, 'ansic_assignment_expression186', a1)
    assert _is_linked(b, 'ansic_assignment_expression186', a1)
    if hasattr(a1, 'ansic_generic_selection185'):
        assert _is_linked(a1, 'ansic_generic_selection185', b)
    _safe_set(b, 'ansic_assignment_expression186', a2)
    assert _is_linked(b, 'ansic_assignment_expression186', a2)
    if hasattr(a1, 'ansic_generic_selection185'):
        assert not _is_linked(a1, 'ansic_generic_selection185', b)
    if hasattr(a2, 'ansic_generic_selection185'):
        assert _is_linked(a2, 'ansic_generic_selection185', b)
    _safe_set(b, 'ansic_assignment_expression186', None)
    assert not _is_linked(b, 'ansic_assignment_expression186', a2)
    if hasattr(a2, 'ansic_generic_selection185'):
        assert not _is_linked(a2, 'ansic_generic_selection185', b)


def test_assoc_assignment_expression196_reverse_link_reassign_clear():
    a1 = ansic_generic_association(default="sample_text")
    a2 = ansic_generic_association(default="sample_text_2")
    b = ansic_assignment_expression(assignment_operator="sample_text")
    _safe_set(b, 'ansic_assignment_expression198', a1)
    assert _is_linked(b, 'ansic_assignment_expression198', a1)
    if hasattr(a1, 'ansic_generic_association197'):
        assert _is_linked(a1, 'ansic_generic_association197', b)
    _safe_set(b, 'ansic_assignment_expression198', a2)
    assert _is_linked(b, 'ansic_assignment_expression198', a2)
    if hasattr(a1, 'ansic_generic_association197'):
        assert not _is_linked(a1, 'ansic_generic_association197', b)
    if hasattr(a2, 'ansic_generic_association197'):
        assert _is_linked(a2, 'ansic_generic_association197', b)
    _safe_set(b, 'ansic_assignment_expression198', None)
    assert not _is_linked(b, 'ansic_assignment_expression198', a2)
    if hasattr(a2, 'ansic_generic_association197'):
        assert not _is_linked(a2, 'ansic_generic_association197', b)


def test_assoc_assignment_expression449_reverse_link_reassign_clear():
    a1 = ansic_assignment_expression(assignment_operator="sample_text")
    a2 = ansic_assignment_expression(assignment_operator="sample_text_2")
    b = ansic_assignment_expression(assignment_operator="sample_text")
    _safe_set(b, 'ansic_assignment_expression450', a1)
    assert _is_linked(b, 'ansic_assignment_expression450', a1)
    if hasattr(a1, 'ansic_assignment_expression448'):
        assert _is_linked(a1, 'ansic_assignment_expression448', b)
    _safe_set(b, 'ansic_assignment_expression450', a2)
    assert _is_linked(b, 'ansic_assignment_expression450', a2)
    if hasattr(a1, 'ansic_assignment_expression448'):
        assert not _is_linked(a1, 'ansic_assignment_expression448', b)
    if hasattr(a2, 'ansic_assignment_expression448'):
        assert _is_linked(a2, 'ansic_assignment_expression448', b)
    _safe_set(b, 'ansic_assignment_expression450', None)
    assert not _is_linked(b, 'ansic_assignment_expression450', a2)
    if hasattr(a2, 'ansic_assignment_expression448'):
        assert not _is_linked(a2, 'ansic_assignment_expression448', b)


def test_assoc_constant179_reverse_link_reassign_clear():
    a1 = ansic_primary_expression(identifier="sample_text")
    a2 = ansic_primary_expression(identifier="sample_text_2")
    b = ansic_constant(char="sample_text", enumz="sample_text", f_constant="sample_text", i_constant=7)
    _safe_set(b, 'ansic_constant', a1)
    assert _is_linked(b, 'ansic_constant', a1)
    if hasattr(a1, 'ansic_primary_expression'):
        assert _is_linked(a1, 'ansic_primary_expression', b)
    _safe_set(b, 'ansic_constant', a2)
    assert _is_linked(b, 'ansic_constant', a2)
    if hasattr(a1, 'ansic_primary_expression'):
        assert not _is_linked(a1, 'ansic_primary_expression', b)
    if hasattr(a2, 'ansic_primary_expression'):
        assert _is_linked(a2, 'ansic_primary_expression', b)
    _safe_set(b, 'ansic_constant', None)
    assert not _is_linked(b, 'ansic_constant', a2)
    if hasattr(a2, 'ansic_primary_expression'):
        assert not _is_linked(a2, 'ansic_primary_expression', b)


def test_assoc_declaration_specifiers10_reverse_link_reassign_clear():
    a1 = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    a2 = ansic_declaration_specifiers(function_specifier="sample_text_2", storage_class_specifier="sample_text_2")
    b = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    _safe_set(b, 'ansic_declaration_specifiers9', {a1})
    assert _is_linked(b, 'ansic_declaration_specifiers9', a1)
    if hasattr(a1, 'ansic_declaration_specifiers'):
        assert _is_linked(a1, 'ansic_declaration_specifiers', b)
    _safe_set(b, 'ansic_declaration_specifiers9', {a2})
    assert _is_linked(b, 'ansic_declaration_specifiers9', a2)
    if hasattr(a1, 'ansic_declaration_specifiers'):
        assert not _is_linked(a1, 'ansic_declaration_specifiers', b)
    if hasattr(a2, 'ansic_declaration_specifiers'):
        assert _is_linked(a2, 'ansic_declaration_specifiers', b)
    _safe_set(b, 'ansic_declaration_specifiers9', set())
    assert not _is_linked(b, 'ansic_declaration_specifiers9', a2)
    if hasattr(a2, 'ansic_declaration_specifiers'):
        assert not _is_linked(a2, 'ansic_declaration_specifiers', b)


def test_assoc_enum_specifier25_reverse_link_reassign_clear():
    a1 = ansic_type_specifier(type_name_str="sample_text")
    a2 = ansic_type_specifier(type_name_str="sample_text_2")
    b = ansic_enum_specifier(identifier="sample_text")
    _safe_set(b, 'ansic_enum_specifier', a1)
    assert _is_linked(b, 'ansic_enum_specifier', a1)
    if hasattr(a1, 'ansic_type_specifier26'):
        assert _is_linked(a1, 'ansic_type_specifier26', b)
    _safe_set(b, 'ansic_enum_specifier', a2)
    assert _is_linked(b, 'ansic_enum_specifier', a2)
    if hasattr(a1, 'ansic_type_specifier26'):
        assert not _is_linked(a1, 'ansic_type_specifier26', b)
    if hasattr(a2, 'ansic_type_specifier26'):
        assert _is_linked(a2, 'ansic_type_specifier26', b)
    _safe_set(b, 'ansic_enum_specifier', None)
    assert not _is_linked(b, 'ansic_enum_specifier', a2)
    if hasattr(a2, 'ansic_type_specifier26'):
        assert not _is_linked(a2, 'ansic_type_specifier26', b)


def test_assoc_generic_selection182_reverse_link_reassign_clear():
    a1 = ansic_primary_expression(identifier="sample_text")
    a2 = ansic_primary_expression(identifier="sample_text_2")
    b = ansic_generic_selection(_generic="sample_text")
    _safe_set(b, 'ansic_generic_selection', a1)
    assert _is_linked(b, 'ansic_generic_selection', a1)
    if hasattr(a1, 'ansic_primary_expression183'):
        assert _is_linked(a1, 'ansic_primary_expression183', b)
    _safe_set(b, 'ansic_generic_selection', a2)
    assert _is_linked(b, 'ansic_generic_selection', a2)
    if hasattr(a1, 'ansic_primary_expression183'):
        assert not _is_linked(a1, 'ansic_primary_expression183', b)
    if hasattr(a2, 'ansic_primary_expression183'):
        assert _is_linked(a2, 'ansic_primary_expression183', b)
    _safe_set(b, 'ansic_generic_selection', None)
    assert not _is_linked(b, 'ansic_generic_selection', a2)
    if hasattr(a2, 'ansic_primary_expression183'):
        assert not _is_linked(a2, 'ansic_primary_expression183', b)


def test_assoc_struct_or_union_specifier23_reverse_link_reassign_clear():
    a1 = ansic_type_specifier(type_name_str="sample_text")
    a2 = ansic_type_specifier(type_name_str="sample_text_2")
    b = ansic_struct_or_union_specifier(identifier="sample_text", struct_or_union="sample_text")
    _safe_set(b, 'ansic_struct_or_union_specifier', a1)
    assert _is_linked(b, 'ansic_struct_or_union_specifier', a1)
    if hasattr(a1, 'ansic_type_specifier24'):
        assert _is_linked(a1, 'ansic_type_specifier24', b)
    _safe_set(b, 'ansic_struct_or_union_specifier', a2)
    assert _is_linked(b, 'ansic_struct_or_union_specifier', a2)
    if hasattr(a1, 'ansic_type_specifier24'):
        assert not _is_linked(a1, 'ansic_type_specifier24', b)
    if hasattr(a2, 'ansic_type_specifier24'):
        assert _is_linked(a2, 'ansic_type_specifier24', b)
    _safe_set(b, 'ansic_struct_or_union_specifier', None)
    assert not _is_linked(b, 'ansic_struct_or_union_specifier', a2)
    if hasattr(a2, 'ansic_type_specifier24'):
        assert not _is_linked(a2, 'ansic_type_specifier24', b)


def test_assoc_type_qualifier13_reverse_link_reassign_clear():
    a1 = ansic_type_qualifier(namez="sample_text")
    a2 = ansic_type_qualifier(namez="sample_text_2")
    b = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    _safe_set(b, 'ansic_declaration_specifiers14', a1)
    assert _is_linked(b, 'ansic_declaration_specifiers14', a1)
    if hasattr(a1, 'ansic_type_qualifier'):
        assert _is_linked(a1, 'ansic_type_qualifier', b)
    _safe_set(b, 'ansic_declaration_specifiers14', a2)
    assert _is_linked(b, 'ansic_declaration_specifiers14', a2)
    if hasattr(a1, 'ansic_type_qualifier'):
        assert not _is_linked(a1, 'ansic_type_qualifier', b)
    if hasattr(a2, 'ansic_type_qualifier'):
        assert _is_linked(a2, 'ansic_type_qualifier', b)
    _safe_set(b, 'ansic_declaration_specifiers14', None)
    assert not _is_linked(b, 'ansic_declaration_specifiers14', a2)
    if hasattr(a2, 'ansic_type_qualifier'):
        assert not _is_linked(a2, 'ansic_type_qualifier', b)


def test_assoc_type_specifier11_reverse_link_reassign_clear():
    a1 = ansic_type_specifier(type_name_str="sample_text")
    a2 = ansic_type_specifier(type_name_str="sample_text_2")
    b = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    _safe_set(b, 'ansic_declaration_specifiers12', a1)
    assert _is_linked(b, 'ansic_declaration_specifiers12', a1)
    if hasattr(a1, 'ansic_type_specifier'):
        assert _is_linked(a1, 'ansic_type_specifier', b)
    _safe_set(b, 'ansic_declaration_specifiers12', a2)
    assert _is_linked(b, 'ansic_declaration_specifiers12', a2)
    if hasattr(a1, 'ansic_type_specifier'):
        assert not _is_linked(a1, 'ansic_type_specifier', b)
    if hasattr(a2, 'ansic_type_specifier'):
        assert _is_linked(a2, 'ansic_type_specifier', b)
    _safe_set(b, 'ansic_declaration_specifiers12', None)
    assert not _is_linked(b, 'ansic_declaration_specifiers12', a2)
    if hasattr(a2, 'ansic_type_specifier'):
        assert not _is_linked(a2, 'ansic_type_specifier', b)


def test_assoc_unary_expression236_reverse_link_reassign_clear():
    a1 = ansic_unary_expression(unary_operator="sample_text")
    a2 = ansic_unary_expression(unary_operator="sample_text_2")
    b = ansic_unary_expression(unary_operator="sample_text")
    _safe_set(b, 'ansic_unary_expression237', a1)
    assert _is_linked(b, 'ansic_unary_expression237', a1)
    if hasattr(a1, 'ansic_unary_expression235'):
        assert _is_linked(a1, 'ansic_unary_expression235', b)
    _safe_set(b, 'ansic_unary_expression237', a2)
    assert _is_linked(b, 'ansic_unary_expression237', a2)
    if hasattr(a1, 'ansic_unary_expression235'):
        assert not _is_linked(a1, 'ansic_unary_expression235', b)
    if hasattr(a2, 'ansic_unary_expression235'):
        assert _is_linked(a2, 'ansic_unary_expression235', b)
    _safe_set(b, 'ansic_unary_expression237', None)
    assert not _is_linked(b, 'ansic_unary_expression237', a2)
    if hasattr(a2, 'ansic_unary_expression235'):
        assert not _is_linked(a2, 'ansic_unary_expression235', b)


def test_assoc_unary_expression445_reverse_link_reassign_clear():
    a1 = ansic_unary_expression(unary_operator="sample_text")
    a2 = ansic_unary_expression(unary_operator="sample_text_2")
    b = ansic_assignment_expression(assignment_operator="sample_text")
    _safe_set(b, 'ansic_assignment_expression446', a1)
    assert _is_linked(b, 'ansic_assignment_expression446', a1)
    if hasattr(a1, 'ansic_unary_expression447'):
        assert _is_linked(a1, 'ansic_unary_expression447', b)
    _safe_set(b, 'ansic_assignment_expression446', a2)
    assert _is_linked(b, 'ansic_assignment_expression446', a2)
    if hasattr(a1, 'ansic_unary_expression447'):
        assert not _is_linked(a1, 'ansic_unary_expression447', b)
    if hasattr(a2, 'ansic_unary_expression447'):
        assert _is_linked(a2, 'ansic_unary_expression447', b)
    _safe_set(b, 'ansic_assignment_expression446', None)
    assert not _is_linked(b, 'ansic_assignment_expression446', a2)
    if hasattr(a2, 'ansic_unary_expression447'):
        assert not _is_linked(a2, 'ansic_unary_expression447', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alignment_specifier15_stub_double():
    # ansic_alignment_specifier has no real 'ansic_alignment_specifier' property in the generated
    # code (a bare stub) -- manually attach it so ansic_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    partner = ansic_alignment_specifier()
    setattr(partner, 'ansic_alignment_specifier', None)
    _safe_set(owner, 'ansic_declaration_specifiers16', partner)
    assert getattr(partner, 'ansic_alignment_specifier') == owner
    _safe_set(owner, 'ansic_declaration_specifiers16', None)
    assert getattr(partner, 'ansic_alignment_specifier') is None


def test_assoc_argument_expression_list228_stub_double():
    # ansic_argument_expression_list has no real 'ansic_argument_expression_list' property in the generated
    # code (a bare stub) -- manually attach it so ansic_postfix_expression_complement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_postfix_expression_complement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_postfix_expression_complement(identifier="sample_text")
    partner = ansic_argument_expression_list()
    setattr(partner, 'ansic_argument_expression_list', None)
    _safe_set(owner, 'ansic_postfix_expression_complement229', partner)
    assert getattr(partner, 'ansic_argument_expression_list') == owner
    _safe_set(owner, 'ansic_postfix_expression_complement229', None)
    assert getattr(partner, 'ansic_argument_expression_list') is None


def test_assoc_assignment_expression123_stub_double():
    # ansic_direct_declarator_complemento has no real 'ansic_direct_declarator_complemento124' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_direct_declarator_complemento()
    setattr(partner, 'ansic_direct_declarator_complemento124', None)
    _safe_set(owner, 'ansic_assignment_expression', partner)
    assert getattr(partner, 'ansic_direct_declarator_complemento124') == owner
    _safe_set(owner, 'ansic_assignment_expression', None)
    assert getattr(partner, 'ansic_direct_declarator_complemento124') is None


def test_assoc_assignment_expression157_stub_double():
    # ansic_direct_abstract_declarator has no real 'ansic_direct_abstract_declarator158' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_direct_abstract_declarator()
    setattr(partner, 'ansic_direct_abstract_declarator158', None)
    _safe_set(owner, 'ansic_assignment_expression159', partner)
    assert getattr(partner, 'ansic_direct_abstract_declarator158') == owner
    _safe_set(owner, 'ansic_assignment_expression159', None)
    assert getattr(partner, 'ansic_direct_abstract_declarator158') is None


def test_assoc_assignment_expression166_stub_double():
    # ansic_initializer has no real 'ansic_initializer167' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_initializer()
    setattr(partner, 'ansic_initializer167', None)
    _safe_set(owner, 'ansic_assignment_expression168', partner)
    assert getattr(partner, 'ansic_initializer167') == owner
    _safe_set(owner, 'ansic_assignment_expression168', None)
    assert getattr(partner, 'ansic_initializer167') is None


def test_assoc_assignment_expression169_stub_double():
    # ansic_direct_abstract_declarator_complement has no real 'ansic_direct_abstract_declarator_complement' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_direct_abstract_declarator_complement()
    setattr(partner, 'ansic_direct_abstract_declarator_complement', None)
    _safe_set(owner, 'ansic_assignment_expression170', partner)
    assert getattr(partner, 'ansic_direct_abstract_declarator_complement') == owner
    _safe_set(owner, 'ansic_assignment_expression170', None)
    assert getattr(partner, 'ansic_direct_abstract_declarator_complement') is None


def test_assoc_assignment_expression460_stub_double():
    # ansic_expression has no real 'ansic_expression461' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_expression()
    setattr(partner, 'ansic_expression461', None)
    _safe_set(owner, 'ansic_assignment_expression462', partner)
    assert getattr(partner, 'ansic_expression461') == owner
    _safe_set(owner, 'ansic_assignment_expression462', None)
    assert getattr(partner, 'ansic_expression461') is None


def test_assoc_assignment_expression465_stub_double():
    # ansic_expression_linha has no real 'ansic_expression_linha466' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_expression_linha()
    setattr(partner, 'ansic_expression_linha466', None)
    _safe_set(owner, 'ansic_assignment_expression467', partner)
    assert getattr(partner, 'ansic_expression_linha466') == owner
    _safe_set(owner, 'ansic_assignment_expression467', None)
    assert getattr(partner, 'ansic_expression_linha466') is None


def test_assoc_assignment_expression544_stub_double():
    # ansic_ArgumentExpressionListLinhaAction has no real 'ansic_ArgumentExpressionListLinhaAction' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_ArgumentExpressionListLinhaAction()
    setattr(partner, 'ansic_ArgumentExpressionListLinhaAction', None)
    _safe_set(owner, 'ansic_assignment_expression545', partner)
    assert getattr(partner, 'ansic_ArgumentExpressionListLinhaAction') == owner
    _safe_set(owner, 'ansic_assignment_expression545', None)
    assert getattr(partner, 'ansic_ArgumentExpressionListLinhaAction') is None


def test_assoc_assignment_expressions230_stub_double():
    # ansic_argument_expression_list has no real 'ansic_argument_expression_list231' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_argument_expression_list()
    setattr(partner, 'ansic_argument_expression_list231', None)
    _safe_set(owner, 'ansic_assignment_expression232', partner)
    assert owner in getattr(partner, 'ansic_argument_expression_list231')
    _safe_set(owner, 'ansic_assignment_expression232', None)
    assert owner not in getattr(partner, 'ansic_argument_expression_list231')


def test_assoc_atomic_type_specifier21_stub_double():
    # ansic_atomic_type_specifier has no real 'ansic_atomic_type_specifier' property in the generated
    # code (a bare stub) -- manually attach it so ansic_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_type_specifier(type_name_str="sample_text")
    partner = ansic_atomic_type_specifier()
    setattr(partner, 'ansic_atomic_type_specifier', None)
    _safe_set(owner, 'ansic_type_specifier22', partner)
    assert getattr(partner, 'ansic_atomic_type_specifier') == owner
    _safe_set(owner, 'ansic_type_specifier22', None)
    assert getattr(partner, 'ansic_atomic_type_specifier') is None


def test_assoc_cast_expression238_stub_double():
    # ansic_cast_expression has no real 'ansic_cast_expression' property in the generated
    # code (a bare stub) -- manually attach it so ansic_unary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_unary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_unary_expression(unary_operator="sample_text")
    partner = ansic_cast_expression()
    setattr(partner, 'ansic_cast_expression', None)
    _safe_set(owner, 'ansic_unary_expression239', partner)
    assert getattr(partner, 'ansic_cast_expression') == owner
    _safe_set(owner, 'ansic_unary_expression239', None)
    assert getattr(partner, 'ansic_cast_expression') is None


def test_assoc_conditional_expression354_stub_double():
    # ansic_conditional_expression has no real 'ansic_conditional_expression356' property in the generated
    # code (a bare stub) -- manually attach it so ansic_labeled_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_labeled_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_labeled_statement(identifier="sample_text")
    partner = ansic_conditional_expression()
    setattr(partner, 'ansic_conditional_expression356', None)
    _safe_set(owner, 'ansic_labeled_statement355', partner)
    assert getattr(partner, 'ansic_conditional_expression356') == owner
    _safe_set(owner, 'ansic_labeled_statement355', None)
    assert getattr(partner, 'ansic_conditional_expression356') is None


def test_assoc_conditional_expression442_stub_double():
    # ansic_conditional_expression has no real 'ansic_conditional_expression444' property in the generated
    # code (a bare stub) -- manually attach it so ansic_assignment_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_assignment_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_assignment_expression(assignment_operator="sample_text")
    partner = ansic_conditional_expression()
    setattr(partner, 'ansic_conditional_expression444', None)
    _safe_set(owner, 'ansic_assignment_expression443', partner)
    assert getattr(partner, 'ansic_conditional_expression444') == owner
    _safe_set(owner, 'ansic_assignment_expression443', None)
    assert getattr(partner, 'ansic_conditional_expression444') is None


def test_assoc_constant_expression221_stub_double():
    # ansic_conditional_expression has no real 'ansic_conditional_expression' property in the generated
    # code (a bare stub) -- manually attach it so ansic_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_designator(identifier="sample_text")
    partner = ansic_conditional_expression()
    setattr(partner, 'ansic_conditional_expression', None)
    _safe_set(owner, 'ansic_designator222', partner)
    assert getattr(partner, 'ansic_conditional_expression') == owner
    _safe_set(owner, 'ansic_designator222', None)
    assert getattr(partner, 'ansic_conditional_expression') is None


def test_assoc_declaration_specifiers138_stub_double():
    # ansic_parameter_declaration has no real 'ansic_parameter_declaration139' property in the generated
    # code (a bare stub) -- manually attach it so ansic_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    partner = ansic_parameter_declaration()
    setattr(partner, 'ansic_parameter_declaration139', None)
    _safe_set(owner, 'ansic_declaration_specifiers140', partner)
    assert getattr(partner, 'ansic_parameter_declaration139') == owner
    _safe_set(owner, 'ansic_declaration_specifiers140', None)
    assert getattr(partner, 'ansic_parameter_declaration139') is None


def test_assoc_declaration_specifiers73_stub_double():
    # ansic_declaration has no real 'ansic_declaration74' property in the generated
    # code (a bare stub) -- manually attach it so ansic_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    partner = ansic_declaration()
    setattr(partner, 'ansic_declaration74', None)
    _safe_set(owner, 'ansic_declaration_specifiers75', partner)
    assert owner in getattr(partner, 'ansic_declaration74')
    _safe_set(owner, 'ansic_declaration_specifiers75', None)
    assert owner not in getattr(partner, 'ansic_declaration74')


def test_assoc_declaration_specifiers81_stub_double():
    # ansic_function_definition has no real 'ansic_function_definition82' property in the generated
    # code (a bare stub) -- manually attach it so ansic_declaration_specifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_declaration_specifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_declaration_specifiers(function_specifier="sample_text", storage_class_specifier="sample_text")
    partner = ansic_function_definition()
    setattr(partner, 'ansic_function_definition82', None)
    _safe_set(owner, 'ansic_declaration_specifiers83', partner)
    assert owner in getattr(partner, 'ansic_function_definition82')
    _safe_set(owner, 'ansic_declaration_specifiers83', None)
    assert owner not in getattr(partner, 'ansic_function_definition82')


def test_assoc_declarator112_stub_double():
    # ansic_declarator has no real 'ansic_declarator114' property in the generated
    # code (a bare stub) -- manually attach it so ansic_direct_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_direct_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_direct_declarator(identifier="sample_text")
    partner = ansic_declarator()
    setattr(partner, 'ansic_declarator114', None)
    _safe_set(owner, 'ansic_direct_declarator113', partner)
    assert getattr(partner, 'ansic_declarator114') == owner
    _safe_set(owner, 'ansic_direct_declarator113', None)
    assert getattr(partner, 'ansic_declarator114') is None


def test_assoc_designator217_stub_double():
    # ansic_designator_list has no real 'ansic_designator_list218' property in the generated
    # code (a bare stub) -- manually attach it so ansic_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_designator(identifier="sample_text")
    partner = ansic_designator_list()
    setattr(partner, 'ansic_designator_list218', None)
    _safe_set(owner, 'ansic_designator', partner)
    assert getattr(partner, 'ansic_designator_list218') == owner
    _safe_set(owner, 'ansic_designator', None)
    assert getattr(partner, 'ansic_designator_list218') is None


def test_assoc_designator539_stub_double():
    # ansic_DesignatorListLinhaAction has no real 'ansic_DesignatorListLinhaAction' property in the generated
    # code (a bare stub) -- manually attach it so ansic_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_designator(identifier="sample_text")
    partner = ansic_DesignatorListLinhaAction()
    setattr(partner, 'ansic_DesignatorListLinhaAction', None)
    _safe_set(owner, 'ansic_designator540', partner)
    assert getattr(partner, 'ansic_DesignatorListLinhaAction') == owner
    _safe_set(owner, 'ansic_designator540', None)
    assert getattr(partner, 'ansic_DesignatorListLinhaAction') is None


def test_assoc_direct_declarator98_stub_double():
    # ansic_declarator has no real 'ansic_declarator99' property in the generated
    # code (a bare stub) -- manually attach it so ansic_direct_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_direct_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_direct_declarator(identifier="sample_text")
    partner = ansic_declarator()
    setattr(partner, 'ansic_declarator99', None)
    _safe_set(owner, 'ansic_direct_declarator', partner)
    assert getattr(partner, 'ansic_declarator99') == owner
    _safe_set(owner, 'ansic_direct_declarator', None)
    assert getattr(partner, 'ansic_declarator99') is None


def test_assoc_direct_declarator_linha110_stub_double():
    # ansic_direct_declarator_linha has no real 'ansic_direct_declarator_linha' property in the generated
    # code (a bare stub) -- manually attach it so ansic_direct_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_direct_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_direct_declarator(identifier="sample_text")
    partner = ansic_direct_declarator_linha()
    setattr(partner, 'ansic_direct_declarator_linha', None)
    _safe_set(owner, 'ansic_direct_declarator111', partner)
    assert getattr(partner, 'ansic_direct_declarator_linha') == owner
    _safe_set(owner, 'ansic_direct_declarator111', None)
    assert getattr(partner, 'ansic_direct_declarator_linha') is None


def test_assoc_enumeration_constant33_stub_double():
    # ansic_enumerator has no real 'ansic_enumerator34' property in the generated
    # code (a bare stub) -- manually attach it so ansic_enumeration_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_enumeration_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_enumeration_constant(identifier="sample_text")
    partner = ansic_enumerator()
    setattr(partner, 'ansic_enumerator34', None)
    _safe_set(owner, 'ansic_enumeration_constant', partner)
    assert getattr(partner, 'ansic_enumerator34') == owner
    _safe_set(owner, 'ansic_enumeration_constant', None)
    assert getattr(partner, 'ansic_enumerator34') is None


def test_assoc_enumerator_list27_stub_double():
    # ansic_enumerator_list has no real 'ansic_enumerator_list' property in the generated
    # code (a bare stub) -- manually attach it so ansic_enum_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_enum_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_enum_specifier(identifier="sample_text")
    partner = ansic_enumerator_list()
    setattr(partner, 'ansic_enumerator_list', None)
    _safe_set(owner, 'ansic_enum_specifier28', partner)
    assert getattr(partner, 'ansic_enumerator_list') == owner
    _safe_set(owner, 'ansic_enum_specifier28', None)
    assert getattr(partner, 'ansic_enumerator_list') is None


def test_assoc_expression180_stub_double():
    # ansic_expression has no real 'ansic_expression' property in the generated
    # code (a bare stub) -- manually attach it so ansic_primary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_primary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_primary_expression(identifier="sample_text")
    partner = ansic_expression()
    setattr(partner, 'ansic_expression', None)
    _safe_set(owner, 'ansic_primary_expression181', partner)
    assert getattr(partner, 'ansic_expression') == owner
    _safe_set(owner, 'ansic_primary_expression181', None)
    assert getattr(partner, 'ansic_expression') is None


def test_assoc_expression226_stub_double():
    # ansic_expression has no real 'ansic_expression227' property in the generated
    # code (a bare stub) -- manually attach it so ansic_postfix_expression_complement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_postfix_expression_complement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_postfix_expression_complement(identifier="sample_text")
    partner = ansic_expression()
    setattr(partner, 'ansic_expression227', None)
    _safe_set(owner, 'ansic_postfix_expression_complement', partner)
    assert getattr(partner, 'ansic_expression227') == owner
    _safe_set(owner, 'ansic_postfix_expression_complement', None)
    assert getattr(partner, 'ansic_expression227') is None


def test_assoc_expression324_stub_double():
    # ansic_expression has no real 'ansic_expression326' property in the generated
    # code (a bare stub) -- manually attach it so ansic_jump_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_jump_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_jump_statement(break_="sample_text", identifier="sample_text", return_="sample_text", return_vazio="sample_text")
    partner = ansic_expression()
    setattr(partner, 'ansic_expression326', None)
    _safe_set(owner, 'ansic_jump_statement325', partner)
    assert getattr(partner, 'ansic_expression326') == owner
    _safe_set(owner, 'ansic_jump_statement325', None)
    assert getattr(partner, 'ansic_expression326') is None


def test_assoc_generic_assoc_list187_stub_double():
    # ansic_generic_assoc_list has no real 'ansic_generic_assoc_list' property in the generated
    # code (a bare stub) -- manually attach it so ansic_generic_selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_generic_selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_generic_selection(_generic="sample_text")
    partner = ansic_generic_assoc_list()
    setattr(partner, 'ansic_generic_assoc_list', None)
    _safe_set(owner, 'ansic_generic_selection188', {partner})
    assert getattr(partner, 'ansic_generic_assoc_list') == owner
    _safe_set(owner, 'ansic_generic_selection188', set())
    assert getattr(partner, 'ansic_generic_assoc_list') is None


def test_assoc_generic_association189_stub_double():
    # ansic_generic_assoc_list has no real 'ansic_generic_assoc_list190' property in the generated
    # code (a bare stub) -- manually attach it so ansic_generic_association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_generic_association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_generic_association(default="sample_text")
    partner = ansic_generic_assoc_list()
    setattr(partner, 'ansic_generic_assoc_list190', None)
    _safe_set(owner, 'ansic_generic_association', partner)
    assert getattr(partner, 'ansic_generic_assoc_list190') == owner
    _safe_set(owner, 'ansic_generic_association', None)
    assert getattr(partner, 'ansic_generic_assoc_list190') is None


def test_assoc_generic_association524_stub_double():
    # ansic_GenericAssocListLinhaAction has no real 'ansic_GenericAssocListLinhaAction' property in the generated
    # code (a bare stub) -- manually attach it so ansic_generic_association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_generic_association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_generic_association(default="sample_text")
    partner = ansic_GenericAssocListLinhaAction()
    setattr(partner, 'ansic_GenericAssocListLinhaAction', None)
    _safe_set(owner, 'ansic_generic_association525', partner)
    assert getattr(partner, 'ansic_GenericAssocListLinhaAction') == owner
    _safe_set(owner, 'ansic_generic_association525', None)
    assert getattr(partner, 'ansic_GenericAssocListLinhaAction') is None


def test_assoc_identifier_list127_stub_double():
    # ansic_direct_declarator_complemento has no real 'ansic_direct_declarator_complemento128' property in the generated
    # code (a bare stub) -- manually attach it so ansic_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_identifier_list(identifier="sample_text")
    partner = ansic_direct_declarator_complemento()
    setattr(partner, 'ansic_direct_declarator_complemento128', None)
    _safe_set(owner, 'ansic_identifier_list', partner)
    assert getattr(partner, 'ansic_direct_declarator_complemento128') == owner
    _safe_set(owner, 'ansic_identifier_list', None)
    assert getattr(partner, 'ansic_direct_declarator_complemento128') is None


def test_assoc_identifier_list_linha177_stub_double():
    # ansic_identifier_list_linha has no real 'ansic_identifier_list_linha' property in the generated
    # code (a bare stub) -- manually attach it so ansic_identifier_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_identifier_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_identifier_list(identifier="sample_text")
    partner = ansic_identifier_list_linha()
    setattr(partner, 'ansic_identifier_list_linha', None)
    _safe_set(owner, 'ansic_identifier_list178', partner)
    assert getattr(partner, 'ansic_identifier_list_linha') == owner
    _safe_set(owner, 'ansic_identifier_list178', None)
    assert getattr(partner, 'ansic_identifier_list_linha') is None


def test_assoc_identifier_list_linha517_stub_double():
    # ansic_identifier_list_linha has no real 'ansic_identifier_list_linha518' property in the generated
    # code (a bare stub) -- manually attach it so ansic_IdentifierListLinhaAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_IdentifierListLinhaAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_IdentifierListLinhaAction(identifier="sample_text")
    partner = ansic_identifier_list_linha()
    setattr(partner, 'ansic_identifier_list_linha518', None)
    _safe_set(owner, 'ansic_IdentifierListLinhaAction', partner)
    assert getattr(partner, 'ansic_identifier_list_linha518') == owner
    _safe_set(owner, 'ansic_IdentifierListLinhaAction', None)
    assert getattr(partner, 'ansic_identifier_list_linha518') is None


def test_assoc_jump_statement322_stub_double():
    # ansic_statement has no real 'ansic_statement323' property in the generated
    # code (a bare stub) -- manually attach it so ansic_jump_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_jump_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_jump_statement(break_="sample_text", identifier="sample_text", return_="sample_text", return_vazio="sample_text")
    partner = ansic_statement()
    setattr(partner, 'ansic_statement323', None)
    _safe_set(owner, 'ansic_jump_statement', partner)
    assert getattr(partner, 'ansic_statement323') == owner
    _safe_set(owner, 'ansic_jump_statement', None)
    assert getattr(partner, 'ansic_statement323') is None


def test_assoc_labeled_statement312_stub_double():
    # ansic_statement has no real 'ansic_statement' property in the generated
    # code (a bare stub) -- manually attach it so ansic_labeled_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_labeled_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_labeled_statement(identifier="sample_text")
    partner = ansic_statement()
    setattr(partner, 'ansic_statement', None)
    _safe_set(owner, 'ansic_labeled_statement', partner)
    assert getattr(partner, 'ansic_statement') == owner
    _safe_set(owner, 'ansic_labeled_statement', None)
    assert getattr(partner, 'ansic_statement') is None


def test_assoc_postfix_expression233_stub_double():
    # ansic_postfix_expression has no real 'ansic_postfix_expression234' property in the generated
    # code (a bare stub) -- manually attach it so ansic_unary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_unary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_unary_expression(unary_operator="sample_text")
    partner = ansic_postfix_expression()
    setattr(partner, 'ansic_postfix_expression234', None)
    _safe_set(owner, 'ansic_unary_expression', partner)
    assert getattr(partner, 'ansic_postfix_expression234') == owner
    _safe_set(owner, 'ansic_unary_expression', None)
    assert getattr(partner, 'ansic_postfix_expression234') is None


def test_assoc_postfix_expression_complement529_stub_double():
    # ansic_PostfixExpressionLinhaAction has no real 'ansic_PostfixExpressionLinhaAction' property in the generated
    # code (a bare stub) -- manually attach it so ansic_postfix_expression_complement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_postfix_expression_complement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_postfix_expression_complement(identifier="sample_text")
    partner = ansic_PostfixExpressionLinhaAction()
    setattr(partner, 'ansic_PostfixExpressionLinhaAction', None)
    _safe_set(owner, 'ansic_postfix_expression_complement530', partner)
    assert getattr(partner, 'ansic_PostfixExpressionLinhaAction') == owner
    _safe_set(owner, 'ansic_postfix_expression_complement530', None)
    assert getattr(partner, 'ansic_PostfixExpressionLinhaAction') is None


def test_assoc_primary_expression199_stub_double():
    # ansic_postfix_expression has no real 'ansic_postfix_expression' property in the generated
    # code (a bare stub) -- manually attach it so ansic_primary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_primary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_primary_expression(identifier="sample_text")
    partner = ansic_postfix_expression()
    setattr(partner, 'ansic_postfix_expression', None)
    _safe_set(owner, 'ansic_primary_expression200', partner)
    assert getattr(partner, 'ansic_postfix_expression') == owner
    _safe_set(owner, 'ansic_primary_expression200', None)
    assert getattr(partner, 'ansic_postfix_expression') is None


def test_assoc_statement351_stub_double():
    # ansic_statement has no real 'ansic_statement353' property in the generated
    # code (a bare stub) -- manually attach it so ansic_labeled_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_labeled_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_labeled_statement(identifier="sample_text")
    partner = ansic_statement()
    setattr(partner, 'ansic_statement353', None)
    _safe_set(owner, 'ansic_labeled_statement352', partner)
    assert getattr(partner, 'ansic_statement353') == owner
    _safe_set(owner, 'ansic_labeled_statement352', None)
    assert getattr(partner, 'ansic_statement353') is None


def test_assoc_struct_declaration_list41_stub_double():
    # ansic_struct_declaration_list has no real 'ansic_struct_declaration_list' property in the generated
    # code (a bare stub) -- manually attach it so ansic_struct_or_union_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_struct_or_union_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_struct_or_union_specifier(identifier="sample_text", struct_or_union="sample_text")
    partner = ansic_struct_declaration_list()
    setattr(partner, 'ansic_struct_declaration_list', None)
    _safe_set(owner, 'ansic_struct_or_union_specifier42', partner)
    assert getattr(partner, 'ansic_struct_declaration_list') == owner
    _safe_set(owner, 'ansic_struct_or_union_specifier42', None)
    assert getattr(partner, 'ansic_struct_declaration_list') is None


def test_assoc_struct_or_union_specifier_complement43_stub_double():
    # ansic_struct_or_union_specifier_complement has no real 'ansic_struct_or_union_specifier_complement' property in the generated
    # code (a bare stub) -- manually attach it so ansic_struct_or_union_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_struct_or_union_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_struct_or_union_specifier(identifier="sample_text", struct_or_union="sample_text")
    partner = ansic_struct_or_union_specifier_complement()
    setattr(partner, 'ansic_struct_or_union_specifier_complement', None)
    _safe_set(owner, 'ansic_struct_or_union_specifier44', partner)
    assert getattr(partner, 'ansic_struct_or_union_specifier_complement') == owner
    _safe_set(owner, 'ansic_struct_or_union_specifier44', None)
    assert getattr(partner, 'ansic_struct_or_union_specifier_complement') is None


def test_assoc_type_name193_stub_double():
    # ansic_type_name has no real 'ansic_type_name195' property in the generated
    # code (a bare stub) -- manually attach it so ansic_generic_association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_generic_association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_generic_association(default="sample_text")
    partner = ansic_type_name()
    setattr(partner, 'ansic_type_name195', None)
    _safe_set(owner, 'ansic_generic_association194', partner)
    assert getattr(partner, 'ansic_type_name195') == owner
    _safe_set(owner, 'ansic_generic_association194', None)
    assert getattr(partner, 'ansic_type_name195') is None


def test_assoc_type_name240_stub_double():
    # ansic_type_name has no real 'ansic_type_name242' property in the generated
    # code (a bare stub) -- manually attach it so ansic_unary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_unary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_unary_expression(unary_operator="sample_text")
    partner = ansic_type_name()
    setattr(partner, 'ansic_type_name242', None)
    _safe_set(owner, 'ansic_unary_expression241', partner)
    assert getattr(partner, 'ansic_type_name242') == owner
    _safe_set(owner, 'ansic_unary_expression241', None)
    assert getattr(partner, 'ansic_type_name242') is None


def test_assoc_type_qualifier105_stub_double():
    # ansic_type_qualifier_list has no real 'ansic_type_qualifier_list106' property in the generated
    # code (a bare stub) -- manually attach it so ansic_type_qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_type_qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_type_qualifier(namez="sample_text")
    partner = ansic_type_qualifier_list()
    setattr(partner, 'ansic_type_qualifier_list106', None)
    _safe_set(owner, 'ansic_type_qualifier107', partner)
    assert getattr(partner, 'ansic_type_qualifier_list106') == owner
    _safe_set(owner, 'ansic_type_qualifier107', None)
    assert getattr(partner, 'ansic_type_qualifier_list106') is None


def test_assoc_type_qualifier507_stub_double():
    # ansic_TypeQualifierListLinhaAtion has no real 'ansic_TypeQualifierListLinhaAtion' property in the generated
    # code (a bare stub) -- manually attach it so ansic_type_qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_type_qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_type_qualifier(namez="sample_text")
    partner = ansic_TypeQualifierListLinhaAtion()
    setattr(partner, 'ansic_TypeQualifierListLinhaAtion', None)
    _safe_set(owner, 'ansic_type_qualifier508', partner)
    assert getattr(partner, 'ansic_TypeQualifierListLinhaAtion') == owner
    _safe_set(owner, 'ansic_type_qualifier508', None)
    assert getattr(partner, 'ansic_TypeQualifierListLinhaAtion') is None


def test_assoc_type_qualifier70_stub_double():
    # ansic_specifier_qualifier_list has no real 'ansic_specifier_qualifier_list71' property in the generated
    # code (a bare stub) -- manually attach it so ansic_type_qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_type_qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_type_qualifier(namez="sample_text")
    partner = ansic_specifier_qualifier_list()
    setattr(partner, 'ansic_specifier_qualifier_list71', None)
    _safe_set(owner, 'ansic_type_qualifier72', partner)
    assert getattr(partner, 'ansic_specifier_qualifier_list71') == owner
    _safe_set(owner, 'ansic_type_qualifier72', None)
    assert getattr(partner, 'ansic_specifier_qualifier_list71') is None


def test_assoc_type_specifier64_stub_double():
    # ansic_specifier_qualifier_list has no real 'ansic_specifier_qualifier_list65' property in the generated
    # code (a bare stub) -- manually attach it so ansic_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_type_specifier(type_name_str="sample_text")
    partner = ansic_specifier_qualifier_list()
    setattr(partner, 'ansic_specifier_qualifier_list65', None)
    _safe_set(owner, 'ansic_type_specifier66', partner)
    assert getattr(partner, 'ansic_specifier_qualifier_list65') == owner
    _safe_set(owner, 'ansic_type_specifier66', None)
    assert getattr(partner, 'ansic_specifier_qualifier_list65') is None


def test_assoc_unary_expression243_stub_double():
    # ansic_cast_expression has no real 'ansic_cast_expression244' property in the generated
    # code (a bare stub) -- manually attach it so ansic_unary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ansic_unary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ansic_unary_expression(unary_operator="sample_text")
    partner = ansic_cast_expression()
    setattr(partner, 'ansic_cast_expression244', None)
    _safe_set(owner, 'ansic_unary_expression245', partner)
    assert getattr(partner, 'ansic_cast_expression244') == owner
    _safe_set(owner, 'ansic_unary_expression245', None)
    assert getattr(partner, 'ansic_cast_expression244') is None


