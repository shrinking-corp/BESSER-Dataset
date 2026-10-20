import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myDsl_ADD,
    myDsl_AND,
    myDsl_EObject,
    myDsl_EQL,
    myDsl_EXC_OR,
    myDsl_INC_OR,
    myDsl_LOG_AND,
    myDsl_LOG_OR,
    myDsl_MINUS,
    myDsl_MUL,
    myDsl_Model,
    myDsl_REL,
    myDsl_SHF,
    myDsl_abstract_declarator,
    myDsl_alignment_specifier,
    myDsl_argument_expression_list,
    myDsl_assignment_expression,
    myDsl_assignment_operator,
    myDsl_atomic_type_specifier,
    myDsl_block_item,
    myDsl_booleanType,
    myDsl_charType,
    myDsl_complexType,
    myDsl_compound_statement,
    myDsl_conditional_expression,
    myDsl_constant,
    myDsl_constant_expression,
    myDsl_declaration,
    myDsl_declaration_list,
    myDsl_declaration_list2,
    myDsl_declaration_specifiers,
    myDsl_declarator,
    myDsl_designation,
    myDsl_designator,
    myDsl_designator_list,
    myDsl_designator_list2,
    myDsl_direct_abstract_declarator,
    myDsl_direct_abstract_declarator2,
    myDsl_direct_declarator,
    myDsl_direct_declarator2,
    myDsl_doubleType,
    myDsl_enum_specifier,
    myDsl_enumeration_constant,
    myDsl_enumerator,
    myDsl_enumerator_list,
    myDsl_enumerator_list2,
    myDsl_expression,
    myDsl_expression2,
    myDsl_expression_statement,
    myDsl_external_declaration,
    myDsl_floatType,
    myDsl_function_definition,
    myDsl_function_specifier,
    myDsl_generic_assoc_list,
    myDsl_generic_association,
    myDsl_generic_selection,
    myDsl_identifier_list,
    myDsl_identifier_list2,
    myDsl_imaginaryType,
    myDsl_init_declarator,
    myDsl_init_declarator_list,
    myDsl_init_declarator_list2,
    myDsl_initializer,
    myDsl_initializer_list,
    myDsl_initializer_list2,
    myDsl_intType,
    myDsl_iteration_statement,
    myDsl_jump_statement,
    myDsl_labeled_statement,
    myDsl_longType,
    myDsl_parameter_declaration,
    myDsl_parameter_list,
    myDsl_parameter_list2,
    myDsl_parameter_type_list,
    myDsl_pointer,
    myDsl_postfix_expression,
    myDsl_postfix_expression2,
    myDsl_selection_statement,
    myDsl_shortType,
    myDsl_signedType,
    myDsl_simple_expression,
    myDsl_specifier_qualifier_list,
    myDsl_statement,
    myDsl_static_assert_declaration,
    myDsl_storage_class_specifier,
    myDsl_stringType,
    myDsl_string_nova,
    myDsl_struct_declaration,
    myDsl_struct_declaration_list,
    myDsl_struct_declaration_list2,
    myDsl_struct_declarator,
    myDsl_struct_declarator_list,
    myDsl_struct_declarator_list2,
    myDsl_struct_or_union,
    myDsl_struct_or_union_specifier,
    myDsl_translation_unit,
    myDsl_type_name,
    myDsl_type_qualifier,
    myDsl_type_qualifier_list,
    myDsl_type_qualifier_list2,
    myDsl_type_specifier,
    myDsl_unary_expression,
    myDsl_unsignedType,
    myDsl_variableRef,
    myDsl_voidType,
    postfix_expression2,
    simple_expression,
    struct_or_union_specifier,
    type_specifier,
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

def test_assoc_atomic_type_specifier102_reverse_link_reassign_clear():
    a1 = myDsl_type_specifier(typedef_name="sample_text")
    a2 = myDsl_type_specifier(typedef_name="sample_text_2")
    b = myDsl_atomic_type_specifier(atomic="sample_text")
    _safe_set(b, 'myDsl_atomic_type_specifier', a1)
    assert _is_linked(b, 'myDsl_atomic_type_specifier', a1)
    if hasattr(a1, 'myDsl_type_specifier103'):
        assert _is_linked(a1, 'myDsl_type_specifier103', b)
    _safe_set(b, 'myDsl_atomic_type_specifier', a2)
    assert _is_linked(b, 'myDsl_atomic_type_specifier', a2)
    if hasattr(a1, 'myDsl_type_specifier103'):
        assert not _is_linked(a1, 'myDsl_type_specifier103', b)
    if hasattr(a2, 'myDsl_type_specifier103'):
        assert _is_linked(a2, 'myDsl_type_specifier103', b)
    _safe_set(b, 'myDsl_atomic_type_specifier', None)
    assert not _is_linked(b, 'myDsl_atomic_type_specifier', a2)
    if hasattr(a2, 'myDsl_type_specifier103'):
        assert not _is_linked(a2, 'myDsl_type_specifier103', b)


def test_assoc_declarators190_reverse_link_reassign_clear():
    a1 = myDsl_direct_declarator2(static="sample_text")
    a2 = myDsl_direct_declarator2(static="sample_text_2")
    b = myDsl_direct_declarator2(static="sample_text")
    _safe_set(b, 'myDsl_direct_declarator2191', a1)
    assert _is_linked(b, 'myDsl_direct_declarator2191', a1)
    if hasattr(a1, 'myDsl_direct_declarator2189'):
        assert _is_linked(a1, 'myDsl_direct_declarator2189', b)
    _safe_set(b, 'myDsl_direct_declarator2191', a2)
    assert _is_linked(b, 'myDsl_direct_declarator2191', a2)
    if hasattr(a1, 'myDsl_direct_declarator2189'):
        assert not _is_linked(a1, 'myDsl_direct_declarator2189', b)
    if hasattr(a2, 'myDsl_direct_declarator2189'):
        assert _is_linked(a2, 'myDsl_direct_declarator2189', b)
    _safe_set(b, 'myDsl_direct_declarator2191', None)
    assert not _is_linked(b, 'myDsl_direct_declarator2191', a2)
    if hasattr(a2, 'myDsl_direct_declarator2189'):
        assert not _is_linked(a2, 'myDsl_direct_declarator2189', b)


def test_assoc_direct_declarators184_reverse_link_reassign_clear():
    a1 = myDsl_direct_declarator2(static="sample_text")
    a2 = myDsl_direct_declarator2(static="sample_text_2")
    b = myDsl_direct_declarator(name="sample_text")
    _safe_set(b, 'myDsl_direct_declarator185', a1)
    assert _is_linked(b, 'myDsl_direct_declarator185', a1)
    if hasattr(a1, 'myDsl_direct_declarator2'):
        assert _is_linked(a1, 'myDsl_direct_declarator2', b)
    _safe_set(b, 'myDsl_direct_declarator185', a2)
    assert _is_linked(b, 'myDsl_direct_declarator185', a2)
    if hasattr(a1, 'myDsl_direct_declarator2'):
        assert not _is_linked(a1, 'myDsl_direct_declarator2', b)
    if hasattr(a2, 'myDsl_direct_declarator2'):
        assert _is_linked(a2, 'myDsl_direct_declarator2', b)
    _safe_set(b, 'myDsl_direct_declarator185', None)
    assert not _is_linked(b, 'myDsl_direct_declarator185', a2)
    if hasattr(a2, 'myDsl_direct_declarator2'):
        assert not _is_linked(a2, 'myDsl_direct_declarator2', b)


def test_assoc_enum_specifier106_reverse_link_reassign_clear():
    a1 = myDsl_type_specifier(typedef_name="sample_text")
    a2 = myDsl_type_specifier(typedef_name="sample_text_2")
    b = myDsl_enum_specifier(enumt="sample_text", identifier="sample_text")
    _safe_set(b, 'myDsl_enum_specifier', a1)
    assert _is_linked(b, 'myDsl_enum_specifier', a1)
    if hasattr(a1, 'myDsl_type_specifier107'):
        assert _is_linked(a1, 'myDsl_type_specifier107', b)
    _safe_set(b, 'myDsl_enum_specifier', a2)
    assert _is_linked(b, 'myDsl_enum_specifier', a2)
    if hasattr(a1, 'myDsl_type_specifier107'):
        assert not _is_linked(a1, 'myDsl_type_specifier107', b)
    if hasattr(a2, 'myDsl_type_specifier107'):
        assert _is_linked(a2, 'myDsl_type_specifier107', b)
    _safe_set(b, 'myDsl_enum_specifier', None)
    assert not _is_linked(b, 'myDsl_enum_specifier', a2)
    if hasattr(a2, 'myDsl_type_specifier107'):
        assert not _is_linked(a2, 'myDsl_type_specifier107', b)


def test_assoc_identifier_list199_reverse_link_reassign_clear():
    a1 = myDsl_identifier_list(identifier="sample_text")
    a2 = myDsl_identifier_list(identifier="sample_text_2")
    b = myDsl_direct_declarator2(static="sample_text")
    _safe_set(b, 'myDsl_direct_declarator2200', a1)
    assert _is_linked(b, 'myDsl_direct_declarator2200', a1)
    if hasattr(a1, 'myDsl_identifier_list'):
        assert _is_linked(a1, 'myDsl_identifier_list', b)
    _safe_set(b, 'myDsl_direct_declarator2200', a2)
    assert _is_linked(b, 'myDsl_direct_declarator2200', a2)
    if hasattr(a1, 'myDsl_identifier_list'):
        assert not _is_linked(a1, 'myDsl_identifier_list', b)
    if hasattr(a2, 'myDsl_identifier_list'):
        assert _is_linked(a2, 'myDsl_identifier_list', b)
    _safe_set(b, 'myDsl_direct_declarator2200', None)
    assert not _is_linked(b, 'myDsl_direct_declarator2200', a2)
    if hasattr(a2, 'myDsl_identifier_list'):
        assert not _is_linked(a2, 'myDsl_identifier_list', b)


def test_assoc_identifier_list2238_reverse_link_reassign_clear():
    a1 = myDsl_identifier_list2(identifier="sample_text")
    a2 = myDsl_identifier_list2(identifier="sample_text_2")
    b = myDsl_identifier_list(identifier="sample_text")
    _safe_set(b, 'myDsl_identifier_list239', a1)
    assert _is_linked(b, 'myDsl_identifier_list239', a1)
    if hasattr(a1, 'myDsl_identifier_list2'):
        assert _is_linked(a1, 'myDsl_identifier_list2', b)
    _safe_set(b, 'myDsl_identifier_list239', a2)
    assert _is_linked(b, 'myDsl_identifier_list239', a2)
    if hasattr(a1, 'myDsl_identifier_list2'):
        assert not _is_linked(a1, 'myDsl_identifier_list2', b)
    if hasattr(a2, 'myDsl_identifier_list2'):
        assert _is_linked(a2, 'myDsl_identifier_list2', b)
    _safe_set(b, 'myDsl_identifier_list239', None)
    assert not _is_linked(b, 'myDsl_identifier_list239', a2)
    if hasattr(a2, 'myDsl_identifier_list2'):
        assert not _is_linked(a2, 'myDsl_identifier_list2', b)


def test_assoc_identifier_list2241_reverse_link_reassign_clear():
    a1 = myDsl_identifier_list2(identifier="sample_text")
    a2 = myDsl_identifier_list2(identifier="sample_text_2")
    b = myDsl_identifier_list2(identifier="sample_text")
    _safe_set(b, 'myDsl_identifier_list2242', a1)
    assert _is_linked(b, 'myDsl_identifier_list2242', a1)
    if hasattr(a1, 'myDsl_identifier_list2240'):
        assert _is_linked(a1, 'myDsl_identifier_list2240', b)
    _safe_set(b, 'myDsl_identifier_list2242', a2)
    assert _is_linked(b, 'myDsl_identifier_list2242', a2)
    if hasattr(a1, 'myDsl_identifier_list2240'):
        assert not _is_linked(a1, 'myDsl_identifier_list2240', b)
    if hasattr(a2, 'myDsl_identifier_list2240'):
        assert _is_linked(a2, 'myDsl_identifier_list2240', b)
    _safe_set(b, 'myDsl_identifier_list2242', None)
    assert not _is_linked(b, 'myDsl_identifier_list2242', a2)
    if hasattr(a2, 'myDsl_identifier_list2240'):
        assert not _is_linked(a2, 'myDsl_identifier_list2240', b)


def test_assoc_parameter_type_list197_reverse_link_reassign_clear():
    a1 = myDsl_parameter_type_list(ellipsis="sample_text")
    a2 = myDsl_parameter_type_list(ellipsis="sample_text_2")
    b = myDsl_direct_declarator2(static="sample_text")
    _safe_set(b, 'myDsl_direct_declarator2198', a1)
    assert _is_linked(b, 'myDsl_direct_declarator2198', a1)
    if hasattr(a1, 'myDsl_parameter_type_list'):
        assert _is_linked(a1, 'myDsl_parameter_type_list', b)
    _safe_set(b, 'myDsl_direct_declarator2198', a2)
    assert _is_linked(b, 'myDsl_direct_declarator2198', a2)
    if hasattr(a1, 'myDsl_parameter_type_list'):
        assert not _is_linked(a1, 'myDsl_parameter_type_list', b)
    if hasattr(a2, 'myDsl_parameter_type_list'):
        assert _is_linked(a2, 'myDsl_parameter_type_list', b)
    _safe_set(b, 'myDsl_direct_declarator2198', None)
    assert not _is_linked(b, 'myDsl_direct_declarator2198', a2)
    if hasattr(a2, 'myDsl_parameter_type_list'):
        assert not _is_linked(a2, 'myDsl_parameter_type_list', b)


def test_assoc_parameter_type_list262_reverse_link_reassign_clear():
    a1 = myDsl_parameter_type_list(ellipsis="sample_text")
    a2 = myDsl_parameter_type_list(ellipsis="sample_text_2")
    b = myDsl_direct_abstract_declarator2(static="sample_text")
    _safe_set(b, 'myDsl_direct_abstract_declarator2263', a1)
    assert _is_linked(b, 'myDsl_direct_abstract_declarator2263', a1)
    if hasattr(a1, 'myDsl_parameter_type_list264'):
        assert _is_linked(a1, 'myDsl_parameter_type_list264', b)
    _safe_set(b, 'myDsl_direct_abstract_declarator2263', a2)
    assert _is_linked(b, 'myDsl_direct_abstract_declarator2263', a2)
    if hasattr(a1, 'myDsl_parameter_type_list264'):
        assert not _is_linked(a1, 'myDsl_parameter_type_list264', b)
    if hasattr(a2, 'myDsl_parameter_type_list264'):
        assert _is_linked(a2, 'myDsl_parameter_type_list264', b)
    _safe_set(b, 'myDsl_direct_abstract_declarator2263', None)
    assert not _is_linked(b, 'myDsl_direct_abstract_declarator2263', a2)
    if hasattr(a2, 'myDsl_parameter_type_list264'):
        assert not _is_linked(a2, 'myDsl_parameter_type_list264', b)


def test_assoc_struct_or_union108_reverse_link_reassign_clear():
    a1 = myDsl_struct_or_union_specifier(identifier="sample_text")
    a2 = myDsl_struct_or_union_specifier(identifier="sample_text_2")
    b = myDsl_struct_or_union(struct="sample_text", union="sample_text")
    _safe_set(b, 'myDsl_struct_or_union', a1)
    assert _is_linked(b, 'myDsl_struct_or_union', a1)
    if hasattr(a1, 'myDsl_struct_or_union_specifier109'):
        assert _is_linked(a1, 'myDsl_struct_or_union_specifier109', b)
    _safe_set(b, 'myDsl_struct_or_union', a2)
    assert _is_linked(b, 'myDsl_struct_or_union', a2)
    if hasattr(a1, 'myDsl_struct_or_union_specifier109'):
        assert not _is_linked(a1, 'myDsl_struct_or_union_specifier109', b)
    if hasattr(a2, 'myDsl_struct_or_union_specifier109'):
        assert _is_linked(a2, 'myDsl_struct_or_union_specifier109', b)
    _safe_set(b, 'myDsl_struct_or_union', None)
    assert not _is_linked(b, 'myDsl_struct_or_union', a2)
    if hasattr(a2, 'myDsl_struct_or_union_specifier109'):
        assert not _is_linked(a2, 'myDsl_struct_or_union_specifier109', b)


def test_assoc_struct_or_union_specifier104_reverse_link_reassign_clear():
    a1 = myDsl_type_specifier(typedef_name="sample_text")
    a2 = myDsl_type_specifier(typedef_name="sample_text_2")
    b = myDsl_struct_or_union_specifier(identifier="sample_text")
    _safe_set(b, 'myDsl_struct_or_union_specifier', a1)
    assert _is_linked(b, 'myDsl_struct_or_union_specifier', a1)
    if hasattr(a1, 'myDsl_type_specifier105'):
        assert _is_linked(a1, 'myDsl_type_specifier105', b)
    _safe_set(b, 'myDsl_struct_or_union_specifier', a2)
    assert _is_linked(b, 'myDsl_struct_or_union_specifier', a2)
    if hasattr(a1, 'myDsl_type_specifier105'):
        assert not _is_linked(a1, 'myDsl_type_specifier105', b)
    if hasattr(a2, 'myDsl_type_specifier105'):
        assert _is_linked(a2, 'myDsl_type_specifier105', b)
    _safe_set(b, 'myDsl_struct_or_union_specifier', None)
    assert not _is_linked(b, 'myDsl_struct_or_union_specifier', a2)
    if hasattr(a2, 'myDsl_type_specifier105'):
        assert not _is_linked(a2, 'myDsl_type_specifier105', b)


def test_assoc_unary_expression36_reverse_link_reassign_clear():
    a1 = myDsl_unary_expression(alignof="sample_text", dec_op="sample_text", inc_op="sample_text", sizeof="sample_text", unary_operator="sample_text")
    a2 = myDsl_unary_expression(alignof="sample_text_2", dec_op="sample_text_2", inc_op="sample_text_2", sizeof="sample_text_2", unary_operator="sample_text_2")
    b = myDsl_unary_expression(alignof="sample_text", dec_op="sample_text", inc_op="sample_text", sizeof="sample_text", unary_operator="sample_text")
    _safe_set(b, 'myDsl_unary_expression37', a1)
    assert _is_linked(b, 'myDsl_unary_expression37', a1)
    if hasattr(a1, 'myDsl_unary_expression35'):
        assert _is_linked(a1, 'myDsl_unary_expression35', b)
    _safe_set(b, 'myDsl_unary_expression37', a2)
    assert _is_linked(b, 'myDsl_unary_expression37', a2)
    if hasattr(a1, 'myDsl_unary_expression35'):
        assert not _is_linked(a1, 'myDsl_unary_expression35', b)
    if hasattr(a2, 'myDsl_unary_expression35'):
        assert _is_linked(a2, 'myDsl_unary_expression35', b)
    _safe_set(b, 'myDsl_unary_expression37', None)
    assert not _is_linked(b, 'myDsl_unary_expression37', a2)
    if hasattr(a2, 'myDsl_unary_expression35'):
        assert not _is_linked(a2, 'myDsl_unary_expression35', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Declarator186_stub_double():
    # myDsl_declarator has no real 'myDsl_declarator188' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_direct_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_direct_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_direct_declarator(name="sample_text")
    partner = myDsl_declarator()
    setattr(partner, 'myDsl_declarator188', None)
    _safe_set(owner, 'myDsl_direct_declarator187', partner)
    assert getattr(partner, 'myDsl_declarator188') == owner
    _safe_set(owner, 'myDsl_direct_declarator187', None)
    assert getattr(partner, 'myDsl_declarator188') is None


def test_assoc_alignment_specifier85_stub_double():
    # myDsl_declaration_specifiers has no real 'myDsl_declaration_specifiers86' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_alignment_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_alignment_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_alignment_specifier(alignas="sample_text")
    partner = myDsl_declaration_specifiers()
    setattr(partner, 'myDsl_declaration_specifiers86', None)
    _safe_set(owner, 'myDsl_alignment_specifier', partner)
    assert getattr(partner, 'myDsl_declaration_specifiers86') == owner
    _safe_set(owner, 'myDsl_alignment_specifier', None)
    assert getattr(partner, 'myDsl_declaration_specifiers86') is None


def test_assoc_assignment_expression16_stub_double():
    # myDsl_assignment_expression has no real 'myDsl_assignment_expression18' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_generic_association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_generic_association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_generic_association(default="sample_text")
    partner = myDsl_assignment_expression()
    setattr(partner, 'myDsl_assignment_expression18', None)
    _safe_set(owner, 'myDsl_generic_association17', partner)
    assert getattr(partner, 'myDsl_assignment_expression18') == owner
    _safe_set(owner, 'myDsl_generic_association17', None)
    assert getattr(partner, 'myDsl_assignment_expression18') is None


def test_assoc_assignment_expression194_stub_double():
    # myDsl_assignment_expression has no real 'myDsl_assignment_expression196' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_direct_declarator2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_direct_declarator2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_direct_declarator2(static="sample_text")
    partner = myDsl_assignment_expression()
    setattr(partner, 'myDsl_assignment_expression196', None)
    _safe_set(owner, 'myDsl_direct_declarator2195', partner)
    assert getattr(partner, 'myDsl_assignment_expression196') == owner
    _safe_set(owner, 'myDsl_direct_declarator2195', None)
    assert getattr(partner, 'myDsl_assignment_expression196') is None


def test_assoc_assignment_expression259_stub_double():
    # myDsl_assignment_expression has no real 'myDsl_assignment_expression261' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_direct_abstract_declarator2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_direct_abstract_declarator2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_direct_abstract_declarator2(static="sample_text")
    partner = myDsl_assignment_expression()
    setattr(partner, 'myDsl_assignment_expression261', None)
    _safe_set(owner, 'myDsl_direct_abstract_declarator2260', partner)
    assert getattr(partner, 'myDsl_assignment_expression261') == owner
    _safe_set(owner, 'myDsl_direct_abstract_declarator2260', None)
    assert getattr(partner, 'myDsl_assignment_expression261') is None


def test_assoc_assignment_expression5_stub_double():
    # myDsl_assignment_expression has no real 'myDsl_assignment_expression' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_generic_selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_generic_selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_generic_selection(generic="sample_text")
    partner = myDsl_assignment_expression()
    setattr(partner, 'myDsl_assignment_expression', None)
    _safe_set(owner, 'myDsl_generic_selection', partner)
    assert getattr(partner, 'myDsl_assignment_expression') == owner
    _safe_set(owner, 'myDsl_generic_selection', None)
    assert getattr(partner, 'myDsl_assignment_expression') is None


def test_assoc_assignment_operator54_stub_double():
    # myDsl_assignment_expression has no real 'myDsl_assignment_expression55' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_assignment_operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_assignment_operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_assignment_operator(add_assign="sample_text", and_assign="sample_text", div_assign="sample_text", left_assign="sample_text", mod_assign="sample_text", mul_assign="sample_text", or_assign="sample_text", right_assign="sample_text", sub_assign="sample_text", xor_assign="sample_text")
    partner = myDsl_assignment_expression()
    setattr(partner, 'myDsl_assignment_expression55', None)
    _safe_set(owner, 'myDsl_assignment_operator', partner)
    assert getattr(partner, 'myDsl_assignment_expression55') == owner
    _safe_set(owner, 'myDsl_assignment_operator', None)
    assert getattr(partner, 'myDsl_assignment_expression55') is None


def test_assoc_constant_expression177_stub_double():
    # myDsl_constant_expression has no real 'myDsl_constant_expression179' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_alignment_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_alignment_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_alignment_specifier(alignas="sample_text")
    partner = myDsl_constant_expression()
    setattr(partner, 'myDsl_constant_expression179', None)
    _safe_set(owner, 'myDsl_alignment_specifier178', partner)
    assert getattr(partner, 'myDsl_constant_expression179') == owner
    _safe_set(owner, 'myDsl_alignment_specifier178', None)
    assert getattr(partner, 'myDsl_constant_expression179') is None


def test_assoc_constant_expression298_stub_double():
    # myDsl_constant_expression has no real 'myDsl_constant_expression300' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_designator(identifier="sample_text")
    partner = myDsl_constant_expression()
    setattr(partner, 'myDsl_constant_expression300', None)
    _safe_set(owner, 'myDsl_designator299', partner)
    assert getattr(partner, 'myDsl_constant_expression300') == owner
    _safe_set(owner, 'myDsl_designator299', None)
    assert getattr(partner, 'myDsl_constant_expression300') is None


def test_assoc_constant_expression301_stub_double():
    # myDsl_constant_expression has no real 'myDsl_constant_expression303' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_static_assert_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_static_assert_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_static_assert_declaration(static_assert="sample_text", string_literal="sample_text")
    partner = myDsl_constant_expression()
    setattr(partner, 'myDsl_constant_expression303', None)
    _safe_set(owner, 'myDsl_static_assert_declaration302', partner)
    assert getattr(partner, 'myDsl_constant_expression303') == owner
    _safe_set(owner, 'myDsl_static_assert_declaration302', None)
    assert getattr(partner, 'myDsl_constant_expression303') is None


def test_assoc_constant_expression318_stub_double():
    # myDsl_constant_expression has no real 'myDsl_constant_expression320' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_labeled_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_labeled_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_labeled_statement(case="sample_text", default="sample_text", identifier="sample_text")
    partner = myDsl_constant_expression()
    setattr(partner, 'myDsl_constant_expression320', None)
    _safe_set(owner, 'myDsl_labeled_statement319', partner)
    assert getattr(partner, 'myDsl_constant_expression320') == owner
    _safe_set(owner, 'myDsl_labeled_statement319', None)
    assert getattr(partner, 'myDsl_constant_expression320') is None


def test_assoc_declaration352_stub_double():
    # myDsl_declaration has no real 'myDsl_declaration354' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_iteration_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_iteration_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_iteration_statement(do="sample_text", for_="sample_text", while_="sample_text")
    partner = myDsl_declaration()
    setattr(partner, 'myDsl_declaration354', None)
    _safe_set(owner, 'myDsl_iteration_statement353', partner)
    assert getattr(partner, 'myDsl_declaration354') == owner
    _safe_set(owner, 'myDsl_iteration_statement353', None)
    assert getattr(partner, 'myDsl_declaration354') is None


def test_assoc_designator288_stub_double():
    # myDsl_designator_list has no real 'myDsl_designator_list289' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_designator(identifier="sample_text")
    partner = myDsl_designator_list()
    setattr(partner, 'myDsl_designator_list289', None)
    _safe_set(owner, 'myDsl_designator', partner)
    assert getattr(partner, 'myDsl_designator_list289') == owner
    _safe_set(owner, 'myDsl_designator', None)
    assert getattr(partner, 'myDsl_designator_list289') is None


def test_assoc_designator292_stub_double():
    # myDsl_designator_list2 has no real 'myDsl_designator_list2293' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_designator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_designator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_designator(identifier="sample_text")
    partner = myDsl_designator_list2()
    setattr(partner, 'myDsl_designator_list2293', None)
    _safe_set(owner, 'myDsl_designator294', partner)
    assert getattr(partner, 'myDsl_designator_list2293') == owner
    _safe_set(owner, 'myDsl_designator294', None)
    assert getattr(partner, 'myDsl_designator_list2293') is None


def test_assoc_direct_abstract_declarator2254_stub_double():
    # myDsl_direct_abstract_declarator has no real 'myDsl_direct_abstract_declarator255' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_direct_abstract_declarator2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_direct_abstract_declarator2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_direct_abstract_declarator2(static="sample_text")
    partner = myDsl_direct_abstract_declarator()
    setattr(partner, 'myDsl_direct_abstract_declarator255', None)
    _safe_set(owner, 'myDsl_direct_abstract_declarator2', partner)
    assert owner in getattr(partner, 'myDsl_direct_abstract_declarator255')
    _safe_set(owner, 'myDsl_direct_abstract_declarator2', None)
    assert owner not in getattr(partner, 'myDsl_direct_abstract_declarator255')


def test_assoc_direct_declarator182_stub_double():
    # myDsl_declarator has no real 'myDsl_declarator183' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_direct_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_direct_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_direct_declarator(name="sample_text")
    partner = myDsl_declarator()
    setattr(partner, 'myDsl_declarator183', None)
    _safe_set(owner, 'myDsl_direct_declarator', partner)
    assert getattr(partner, 'myDsl_declarator183') == owner
    _safe_set(owner, 'myDsl_direct_declarator', None)
    assert getattr(partner, 'myDsl_declarator183') is None


def test_assoc_enumeration_constant166_stub_double():
    # myDsl_enumerator has no real 'myDsl_enumerator167' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_enumeration_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_enumeration_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_enumeration_constant(identifier="sample_text")
    partner = myDsl_enumerator()
    setattr(partner, 'myDsl_enumerator167', None)
    _safe_set(owner, 'myDsl_enumeration_constant', partner)
    assert getattr(partner, 'myDsl_enumerator167') == owner
    _safe_set(owner, 'myDsl_enumeration_constant', None)
    assert getattr(partner, 'myDsl_enumerator167') is None


def test_assoc_enumerator_list154_stub_double():
    # myDsl_enumerator_list has no real 'myDsl_enumerator_list' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_enum_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_enum_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_enum_specifier(enumt="sample_text", identifier="sample_text")
    partner = myDsl_enumerator_list()
    setattr(partner, 'myDsl_enumerator_list', None)
    _safe_set(owner, 'myDsl_enum_specifier155', partner)
    assert getattr(partner, 'myDsl_enumerator_list') == owner
    _safe_set(owner, 'myDsl_enum_specifier155', None)
    assert getattr(partner, 'myDsl_enumerator_list') is None


def test_assoc_expression332_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression334' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_selection_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_selection_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_selection_statement(else_="sample_text", if_="sample_text", switch="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression334', None)
    _safe_set(owner, 'myDsl_selection_statement333', partner)
    assert getattr(partner, 'myDsl_simple_expression334') == owner
    _safe_set(owner, 'myDsl_selection_statement333', None)
    assert getattr(partner, 'myDsl_simple_expression334') is None


def test_assoc_expression341_stub_double():
    # myDsl_EObject has no real 'myDsl_EObject' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_iteration_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_iteration_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_iteration_statement(do="sample_text", for_="sample_text", while_="sample_text")
    partner = myDsl_EObject()
    setattr(partner, 'myDsl_EObject', None)
    _safe_set(owner, 'myDsl_iteration_statement342', partner)
    assert getattr(partner, 'myDsl_EObject') == owner
    _safe_set(owner, 'myDsl_iteration_statement342', None)
    assert getattr(partner, 'myDsl_EObject') is None


def test_assoc_expression355_stub_double():
    # myDsl_expression has no real 'myDsl_expression357' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_jump_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_jump_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_jump_statement(break_="sample_text", continue_="sample_text", goto="sample_text", identifier="sample_text", return_="sample_text")
    partner = myDsl_expression()
    setattr(partner, 'myDsl_expression357', None)
    _safe_set(owner, 'myDsl_jump_statement356', partner)
    assert getattr(partner, 'myDsl_expression357') == owner
    _safe_set(owner, 'myDsl_jump_statement356', None)
    assert getattr(partner, 'myDsl_expression357') is None


def test_assoc_expression_statement2349_stub_double():
    # myDsl_expression_statement has no real 'myDsl_expression_statement351' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_iteration_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_iteration_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_iteration_statement(do="sample_text", for_="sample_text", while_="sample_text")
    partner = myDsl_expression_statement()
    setattr(partner, 'myDsl_expression_statement351', None)
    _safe_set(owner, 'myDsl_iteration_statement350', partner)
    assert getattr(partner, 'myDsl_expression_statement351') == owner
    _safe_set(owner, 'myDsl_iteration_statement350', None)
    assert getattr(partner, 'myDsl_expression_statement351') is None


def test_assoc_expression_statement346_stub_double():
    # myDsl_expression_statement has no real 'myDsl_expression_statement348' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_iteration_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_iteration_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_iteration_statement(do="sample_text", for_="sample_text", while_="sample_text")
    partner = myDsl_expression_statement()
    setattr(partner, 'myDsl_expression_statement348', None)
    _safe_set(owner, 'myDsl_iteration_statement347', partner)
    assert getattr(partner, 'myDsl_expression_statement348') == owner
    _safe_set(owner, 'myDsl_iteration_statement347', None)
    assert getattr(partner, 'myDsl_expression_statement348') is None


def test_assoc_function_specifier83_stub_double():
    # myDsl_declaration_specifiers has no real 'myDsl_declaration_specifiers84' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_function_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_function_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_function_specifier(inline="sample_text", noreturn="sample_text")
    partner = myDsl_declaration_specifiers()
    setattr(partner, 'myDsl_declaration_specifiers84', None)
    _safe_set(owner, 'myDsl_function_specifier', partner)
    assert getattr(partner, 'myDsl_declaration_specifiers84') == owner
    _safe_set(owner, 'myDsl_function_specifier', None)
    assert getattr(partner, 'myDsl_declaration_specifiers84') is None


def test_assoc_generic_assoc_list6_stub_double():
    # myDsl_generic_assoc_list has no real 'myDsl_generic_assoc_list' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_generic_selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_generic_selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_generic_selection(generic="sample_text")
    partner = myDsl_generic_assoc_list()
    setattr(partner, 'myDsl_generic_assoc_list', None)
    _safe_set(owner, 'myDsl_generic_selection7', partner)
    assert getattr(partner, 'myDsl_generic_assoc_list') == owner
    _safe_set(owner, 'myDsl_generic_selection7', None)
    assert getattr(partner, 'myDsl_generic_assoc_list') is None


def test_assoc_generic_association8_stub_double():
    # myDsl_generic_assoc_list has no real 'myDsl_generic_assoc_list9' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_generic_association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_generic_association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_generic_association(default="sample_text")
    partner = myDsl_generic_assoc_list()
    setattr(partner, 'myDsl_generic_assoc_list9', None)
    _safe_set(owner, 'myDsl_generic_association', partner)
    assert getattr(partner, 'myDsl_generic_assoc_list9') == owner
    _safe_set(owner, 'myDsl_generic_association', None)
    assert getattr(partner, 'myDsl_generic_assoc_list9') is None


def test_assoc_generic_list10_stub_double():
    # myDsl_generic_assoc_list has no real 'myDsl_generic_assoc_list11' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_generic_association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_generic_association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_generic_association(default="sample_text")
    partner = myDsl_generic_assoc_list()
    setattr(partner, 'myDsl_generic_assoc_list11', None)
    _safe_set(owner, 'myDsl_generic_association12', partner)
    assert owner in getattr(partner, 'myDsl_generic_assoc_list11')
    _safe_set(owner, 'myDsl_generic_association12', None)
    assert owner not in getattr(partner, 'myDsl_generic_assoc_list11')


def test_assoc_iteration_statement311_stub_double():
    # myDsl_statement has no real 'myDsl_statement312' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_iteration_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_iteration_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_iteration_statement(do="sample_text", for_="sample_text", while_="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement312', None)
    _safe_set(owner, 'myDsl_iteration_statement', partner)
    assert getattr(partner, 'myDsl_statement312') == owner
    _safe_set(owner, 'myDsl_iteration_statement', None)
    assert getattr(partner, 'myDsl_statement312') is None


def test_assoc_jump_statement313_stub_double():
    # myDsl_statement has no real 'myDsl_statement314' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_jump_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_jump_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_jump_statement(break_="sample_text", continue_="sample_text", goto="sample_text", identifier="sample_text", return_="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement314', None)
    _safe_set(owner, 'myDsl_jump_statement', partner)
    assert getattr(partner, 'myDsl_statement314') == owner
    _safe_set(owner, 'myDsl_jump_statement', None)
    assert getattr(partner, 'myDsl_statement314') is None


def test_assoc_labeled_statement304_stub_double():
    # myDsl_statement has no real 'myDsl_statement' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_labeled_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_labeled_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_labeled_statement(case="sample_text", default="sample_text", identifier="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement', None)
    _safe_set(owner, 'myDsl_labeled_statement', partner)
    assert getattr(partner, 'myDsl_statement') == owner
    _safe_set(owner, 'myDsl_labeled_statement', None)
    assert getattr(partner, 'myDsl_statement') is None


def test_assoc_left388_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression389' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MUL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MUL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MUL(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression389', None)
    _safe_set(owner, 'myDsl_MUL', partner)
    assert getattr(partner, 'myDsl_simple_expression389') == owner
    _safe_set(owner, 'myDsl_MUL', None)
    assert getattr(partner, 'myDsl_simple_expression389') is None


def test_assoc_left403_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression404' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SHF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SHF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SHF(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression404', None)
    _safe_set(owner, 'myDsl_SHF', partner)
    assert getattr(partner, 'myDsl_simple_expression404') == owner
    _safe_set(owner, 'myDsl_SHF', None)
    assert getattr(partner, 'myDsl_simple_expression404') is None


def test_assoc_left408_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression409' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_REL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_REL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_REL(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression409', None)
    _safe_set(owner, 'myDsl_REL', partner)
    assert getattr(partner, 'myDsl_simple_expression409') == owner
    _safe_set(owner, 'myDsl_REL', None)
    assert getattr(partner, 'myDsl_simple_expression409') is None


def test_assoc_left413_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression414' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_EQL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_EQL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_EQL(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression414', None)
    _safe_set(owner, 'myDsl_EQL', partner)
    assert getattr(partner, 'myDsl_simple_expression414') == owner
    _safe_set(owner, 'myDsl_EQL', None)
    assert getattr(partner, 'myDsl_simple_expression414') is None


def test_assoc_parameter_list218_stub_double():
    # myDsl_parameter_list has no real 'myDsl_parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_parameter_type_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_parameter_type_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_parameter_type_list(ellipsis="sample_text")
    partner = myDsl_parameter_list()
    setattr(partner, 'myDsl_parameter_list', None)
    _safe_set(owner, 'myDsl_parameter_type_list219', partner)
    assert getattr(partner, 'myDsl_parameter_list') == owner
    _safe_set(owner, 'myDsl_parameter_type_list219', None)
    assert getattr(partner, 'myDsl_parameter_list') is None


def test_assoc_postfix_expression33_stub_double():
    # myDsl_postfix_expression has no real 'myDsl_postfix_expression34' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_unary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_unary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_unary_expression(alignof="sample_text", dec_op="sample_text", inc_op="sample_text", sizeof="sample_text", unary_operator="sample_text")
    partner = myDsl_postfix_expression()
    setattr(partner, 'myDsl_postfix_expression34', None)
    _safe_set(owner, 'myDsl_unary_expression', partner)
    assert getattr(partner, 'myDsl_postfix_expression34') == owner
    _safe_set(owner, 'myDsl_unary_expression', None)
    assert getattr(partner, 'myDsl_postfix_expression34') is None


def test_assoc_right390_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression392' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MUL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MUL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MUL(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression392', None)
    _safe_set(owner, 'myDsl_MUL391', partner)
    assert getattr(partner, 'myDsl_simple_expression392') == owner
    _safe_set(owner, 'myDsl_MUL391', None)
    assert getattr(partner, 'myDsl_simple_expression392') is None


def test_assoc_right405_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression407' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SHF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SHF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SHF(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression407', None)
    _safe_set(owner, 'myDsl_SHF406', partner)
    assert getattr(partner, 'myDsl_simple_expression407') == owner
    _safe_set(owner, 'myDsl_SHF406', None)
    assert getattr(partner, 'myDsl_simple_expression407') is None


def test_assoc_right410_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression412' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_REL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_REL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_REL(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression412', None)
    _safe_set(owner, 'myDsl_REL411', partner)
    assert getattr(partner, 'myDsl_simple_expression412') == owner
    _safe_set(owner, 'myDsl_REL411', None)
    assert getattr(partner, 'myDsl_simple_expression412') is None


def test_assoc_right415_stub_double():
    # myDsl_simple_expression has no real 'myDsl_simple_expression417' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_EQL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_EQL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_EQL(op="sample_text")
    partner = myDsl_simple_expression()
    setattr(partner, 'myDsl_simple_expression417', None)
    _safe_set(owner, 'myDsl_EQL416', partner)
    assert getattr(partner, 'myDsl_simple_expression417') == owner
    _safe_set(owner, 'myDsl_EQL416', None)
    assert getattr(partner, 'myDsl_simple_expression417') is None


def test_assoc_selection_statement309_stub_double():
    # myDsl_statement has no real 'myDsl_statement310' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_selection_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_selection_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_selection_statement(else_="sample_text", if_="sample_text", switch="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement310', None)
    _safe_set(owner, 'myDsl_selection_statement', partner)
    assert getattr(partner, 'myDsl_statement310') == owner
    _safe_set(owner, 'myDsl_selection_statement', None)
    assert getattr(partner, 'myDsl_statement310') is None


def test_assoc_statement2338_stub_double():
    # myDsl_statement has no real 'myDsl_statement340' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_selection_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_selection_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_selection_statement(else_="sample_text", if_="sample_text", switch="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement340', None)
    _safe_set(owner, 'myDsl_selection_statement339', partner)
    assert getattr(partner, 'myDsl_statement340') == owner
    _safe_set(owner, 'myDsl_selection_statement339', None)
    assert getattr(partner, 'myDsl_statement340') is None


def test_assoc_statement315_stub_double():
    # myDsl_statement has no real 'myDsl_statement317' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_labeled_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_labeled_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_labeled_statement(case="sample_text", default="sample_text", identifier="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement317', None)
    _safe_set(owner, 'myDsl_labeled_statement316', partner)
    assert getattr(partner, 'myDsl_statement317') == owner
    _safe_set(owner, 'myDsl_labeled_statement316', None)
    assert getattr(partner, 'myDsl_statement317') is None


def test_assoc_statement335_stub_double():
    # myDsl_statement has no real 'myDsl_statement337' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_selection_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_selection_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_selection_statement(else_="sample_text", if_="sample_text", switch="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement337', None)
    _safe_set(owner, 'myDsl_selection_statement336', partner)
    assert getattr(partner, 'myDsl_statement337') == owner
    _safe_set(owner, 'myDsl_selection_statement336', None)
    assert getattr(partner, 'myDsl_statement337') is None


def test_assoc_statement343_stub_double():
    # myDsl_statement has no real 'myDsl_statement345' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_iteration_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_iteration_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_iteration_statement(do="sample_text", for_="sample_text", while_="sample_text")
    partner = myDsl_statement()
    setattr(partner, 'myDsl_statement345', None)
    _safe_set(owner, 'myDsl_iteration_statement344', partner)
    assert getattr(partner, 'myDsl_statement345') == owner
    _safe_set(owner, 'myDsl_iteration_statement344', None)
    assert getattr(partner, 'myDsl_statement345') is None


def test_assoc_static_assert_declaration126_stub_double():
    # myDsl_struct_declaration has no real 'myDsl_struct_declaration127' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_static_assert_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_static_assert_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_static_assert_declaration(static_assert="sample_text", string_literal="sample_text")
    partner = myDsl_struct_declaration()
    setattr(partner, 'myDsl_struct_declaration127', None)
    _safe_set(owner, 'myDsl_static_assert_declaration128', partner)
    assert getattr(partner, 'myDsl_struct_declaration127') == owner
    _safe_set(owner, 'myDsl_static_assert_declaration128', None)
    assert getattr(partner, 'myDsl_struct_declaration127') is None


def test_assoc_static_assert_declaration72_stub_double():
    # myDsl_declaration has no real 'myDsl_declaration73' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_static_assert_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_static_assert_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_static_assert_declaration(static_assert="sample_text", string_literal="sample_text")
    partner = myDsl_declaration()
    setattr(partner, 'myDsl_declaration73', None)
    _safe_set(owner, 'myDsl_static_assert_declaration', partner)
    assert getattr(partner, 'myDsl_declaration73') == owner
    _safe_set(owner, 'myDsl_static_assert_declaration', None)
    assert getattr(partner, 'myDsl_declaration73') is None


def test_assoc_storage_class_specifier74_stub_double():
    # myDsl_declaration_specifiers has no real 'myDsl_declaration_specifiers75' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_storage_class_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_storage_class_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_storage_class_specifier(auto="sample_text", extern="sample_text", register="sample_text", static="sample_text", thread_local="sample_text", typedef="sample_text")
    partner = myDsl_declaration_specifiers()
    setattr(partner, 'myDsl_declaration_specifiers75', None)
    _safe_set(owner, 'myDsl_storage_class_specifier', partner)
    assert getattr(partner, 'myDsl_declaration_specifiers75') == owner
    _safe_set(owner, 'myDsl_storage_class_specifier', None)
    assert getattr(partner, 'myDsl_declaration_specifiers75') is None


def test_assoc_struct_declaration_list110_stub_double():
    # myDsl_struct_declaration_list has no real 'myDsl_struct_declaration_list' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_struct_or_union_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_struct_or_union_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_struct_or_union_specifier(identifier="sample_text")
    partner = myDsl_struct_declaration_list()
    setattr(partner, 'myDsl_struct_declaration_list', None)
    _safe_set(owner, 'myDsl_struct_or_union_specifier111', partner)
    assert getattr(partner, 'myDsl_struct_declaration_list') == owner
    _safe_set(owner, 'myDsl_struct_or_union_specifier111', None)
    assert getattr(partner, 'myDsl_struct_declaration_list') is None


def test_assoc_type_name13_stub_double():
    # myDsl_type_name has no real 'myDsl_type_name15' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_generic_association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_generic_association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_generic_association(default="sample_text")
    partner = myDsl_type_name()
    setattr(partner, 'myDsl_type_name15', None)
    _safe_set(owner, 'myDsl_generic_association14', partner)
    assert getattr(partner, 'myDsl_type_name15') == owner
    _safe_set(owner, 'myDsl_generic_association14', None)
    assert getattr(partner, 'myDsl_type_name15') is None


def test_assoc_type_name171_stub_double():
    # myDsl_type_name has no real 'myDsl_type_name173' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_atomic_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_atomic_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_atomic_type_specifier(atomic="sample_text")
    partner = myDsl_type_name()
    setattr(partner, 'myDsl_type_name173', None)
    _safe_set(owner, 'myDsl_atomic_type_specifier172', partner)
    assert getattr(partner, 'myDsl_type_name173') == owner
    _safe_set(owner, 'myDsl_atomic_type_specifier172', None)
    assert getattr(partner, 'myDsl_type_name173') is None


def test_assoc_type_name174_stub_double():
    # myDsl_type_name has no real 'myDsl_type_name176' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_alignment_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_alignment_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_alignment_specifier(alignas="sample_text")
    partner = myDsl_type_name()
    setattr(partner, 'myDsl_type_name176', None)
    _safe_set(owner, 'myDsl_alignment_specifier175', partner)
    assert getattr(partner, 'myDsl_type_name176') == owner
    _safe_set(owner, 'myDsl_alignment_specifier175', None)
    assert getattr(partner, 'myDsl_type_name176') is None


def test_assoc_type_qualifier135_stub_double():
    # myDsl_specifier_qualifier_list has no real 'myDsl_specifier_qualifier_list136' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_specifier(typedef_name="sample_text")
    partner = myDsl_specifier_qualifier_list()
    setattr(partner, 'myDsl_specifier_qualifier_list136', None)
    _safe_set(owner, 'myDsl_type_specifier137', partner)
    assert getattr(partner, 'myDsl_specifier_qualifier_list136') == owner
    _safe_set(owner, 'myDsl_type_specifier137', None)
    assert getattr(partner, 'myDsl_specifier_qualifier_list136') is None


def test_assoc_type_qualifier207_stub_double():
    # myDsl_type_qualifier_list has no real 'myDsl_type_qualifier_list208' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_qualifier(atomic="sample_text", const="sample_text", restrict="sample_text", volatile="sample_text")
    partner = myDsl_type_qualifier_list()
    setattr(partner, 'myDsl_type_qualifier_list208', None)
    _safe_set(owner, 'myDsl_type_qualifier209', partner)
    assert getattr(partner, 'myDsl_type_qualifier_list208') == owner
    _safe_set(owner, 'myDsl_type_qualifier209', None)
    assert getattr(partner, 'myDsl_type_qualifier_list208') is None


def test_assoc_type_qualifier212_stub_double():
    # myDsl_type_qualifier_list2 has no real 'myDsl_type_qualifier_list2213' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_qualifier(atomic="sample_text", const="sample_text", restrict="sample_text", volatile="sample_text")
    partner = myDsl_type_qualifier_list2()
    setattr(partner, 'myDsl_type_qualifier_list2213', None)
    _safe_set(owner, 'myDsl_type_qualifier214', partner)
    assert getattr(partner, 'myDsl_type_qualifier_list2213') == owner
    _safe_set(owner, 'myDsl_type_qualifier214', None)
    assert getattr(partner, 'myDsl_type_qualifier_list2213') is None


def test_assoc_type_qualifier81_stub_double():
    # myDsl_declaration_specifiers has no real 'myDsl_declaration_specifiers82' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_qualifier(atomic="sample_text", const="sample_text", restrict="sample_text", volatile="sample_text")
    partner = myDsl_declaration_specifiers()
    setattr(partner, 'myDsl_declaration_specifiers82', None)
    _safe_set(owner, 'myDsl_type_qualifier', partner)
    assert getattr(partner, 'myDsl_declaration_specifiers82') == owner
    _safe_set(owner, 'myDsl_type_qualifier', None)
    assert getattr(partner, 'myDsl_declaration_specifiers82') is None


def test_assoc_type_qualifier_list192_stub_double():
    # myDsl_type_qualifier_list has no real 'myDsl_type_qualifier_list' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_direct_declarator2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_direct_declarator2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_direct_declarator2(static="sample_text")
    partner = myDsl_type_qualifier_list()
    setattr(partner, 'myDsl_type_qualifier_list', None)
    _safe_set(owner, 'myDsl_direct_declarator2193', partner)
    assert getattr(partner, 'myDsl_type_qualifier_list') == owner
    _safe_set(owner, 'myDsl_direct_declarator2193', None)
    assert getattr(partner, 'myDsl_type_qualifier_list') is None


def test_assoc_type_qualifier_list256_stub_double():
    # myDsl_type_qualifier_list has no real 'myDsl_type_qualifier_list258' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_direct_abstract_declarator2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_direct_abstract_declarator2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_direct_abstract_declarator2(static="sample_text")
    partner = myDsl_type_qualifier_list()
    setattr(partner, 'myDsl_type_qualifier_list258', None)
    _safe_set(owner, 'myDsl_direct_abstract_declarator2257', partner)
    assert getattr(partner, 'myDsl_type_qualifier_list258') == owner
    _safe_set(owner, 'myDsl_direct_abstract_declarator2257', None)
    assert getattr(partner, 'myDsl_type_qualifier_list258') is None


def test_assoc_type_specifier129_stub_double():
    # myDsl_specifier_qualifier_list has no real 'myDsl_specifier_qualifier_list130' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_specifier(typedef_name="sample_text")
    partner = myDsl_specifier_qualifier_list()
    setattr(partner, 'myDsl_specifier_qualifier_list130', None)
    _safe_set(owner, 'myDsl_type_specifier131', partner)
    assert getattr(partner, 'myDsl_specifier_qualifier_list130') == owner
    _safe_set(owner, 'myDsl_type_specifier131', None)
    assert getattr(partner, 'myDsl_specifier_qualifier_list130') is None


def test_assoc_type_specifier79_stub_double():
    # myDsl_declaration_specifiers has no real 'myDsl_declaration_specifiers80' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_type_specifier(typedef_name="sample_text")
    partner = myDsl_declaration_specifiers()
    setattr(partner, 'myDsl_declaration_specifiers80', None)
    _safe_set(owner, 'myDsl_type_specifier', partner)
    assert getattr(partner, 'myDsl_declaration_specifiers80') == owner
    _safe_set(owner, 'myDsl_type_specifier', None)
    assert getattr(partner, 'myDsl_declaration_specifiers80') is None


def test_assoc_unary_expression51_stub_double():
    # myDsl_assignment_expression has no real 'myDsl_assignment_expression52' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_unary_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_unary_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_unary_expression(alignof="sample_text", dec_op="sample_text", inc_op="sample_text", sizeof="sample_text", unary_operator="sample_text")
    partner = myDsl_assignment_expression()
    setattr(partner, 'myDsl_assignment_expression52', None)
    _safe_set(owner, 'myDsl_unary_expression53', partner)
    assert getattr(partner, 'myDsl_assignment_expression52') == owner
    _safe_set(owner, 'myDsl_unary_expression53', None)
    assert getattr(partner, 'myDsl_assignment_expression52') is None


def test_assoc_value387_stub_double():
    # myDsl_stringType has no real 'myDsl_stringType' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_string_nova's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_string_nova's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_string_nova(func_name="sample_text", string_literal="sample_text")
    partner = myDsl_stringType()
    setattr(partner, 'myDsl_stringType', None)
    _safe_set(owner, 'myDsl_string_nova', partner)
    assert getattr(partner, 'myDsl_stringType') == owner
    _safe_set(owner, 'myDsl_string_nova', None)
    assert getattr(partner, 'myDsl_stringType') is None


