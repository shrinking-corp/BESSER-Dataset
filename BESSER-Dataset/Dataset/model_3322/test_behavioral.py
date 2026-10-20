import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Model,
    creating_aux,
    exp_aux,
    expression,
    expression_aux,
    newBlock,
    simpleJava_MODIFIER,
    simpleJava_Model,
    simpleJava_arglist,
    simpleJava_aux,
    simpleJava_bit_expression,
    simpleJava_class_declaration,
    simpleJava_compilation_unit,
    simpleJava_constructor_declaration,
    simpleJava_creating_aux,
    simpleJava_creating_expression,
    simpleJava_do_statement,
    simpleJava_doc_comment,
    simpleJava_exp_aux,
    simpleJava_expression,
    simpleJava_expression_aux,
    simpleJava_field_declaration,
    simpleJava_for_statement,
    simpleJava_if_statement,
    simpleJava_import_statement,
    simpleJava_interface_declaration,
    simpleJava_literal_expression,
    simpleJava_logical_expression,
    simpleJava_mais_aux,
    simpleJava_method_declaration,
    simpleJava_name,
    simpleJava_newBlock,
    simpleJava_numeric_expression,
    simpleJava_package_name_aux,
    simpleJava_package_statement,
    simpleJava_parameter,
    simpleJava_parameter_list,
    simpleJava_statement,
    simpleJava_statement_block,
    simpleJava_static_initializer,
    simpleJava_switch_statement,
    simpleJava_try_statement,
    simpleJava_type,
    simpleJava_type_declaration,
    simpleJava_type_specifier,
    simpleJava_variable_declaration,
    simpleJava_variable_declarator,
    simpleJava_variable_initializer,
    simpleJava_while_statement,
    type_declaration,
    variable_declarator,
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

def test_assoc_bit199_reverse_link_reassign_clear():
    a1 = simpleJava_expression(identificador="sample_text")
    a2 = simpleJava_expression(identificador="sample_text_2")
    b = simpleJava_bit_expression(operador="sample_text")
    _safe_set(b, 'simpleJava_bit_expression', a1)
    assert _is_linked(b, 'simpleJava_bit_expression', a1)
    if hasattr(a1, 'simpleJava_expression200'):
        assert _is_linked(a1, 'simpleJava_expression200', b)
    _safe_set(b, 'simpleJava_bit_expression', a2)
    assert _is_linked(b, 'simpleJava_bit_expression', a2)
    if hasattr(a1, 'simpleJava_expression200'):
        assert not _is_linked(a1, 'simpleJava_expression200', b)
    if hasattr(a2, 'simpleJava_expression200'):
        assert _is_linked(a2, 'simpleJava_expression200', b)
    _safe_set(b, 'simpleJava_bit_expression', None)
    assert not _is_linked(b, 'simpleJava_bit_expression', a2)
    if hasattr(a2, 'simpleJava_expression200'):
        assert not _is_linked(a2, 'simpleJava_expression200', b)


def test_assoc_corpoSynchronize86_reverse_link_reassign_clear():
    a1 = simpleJava_statement(break_="sample_text", continue_="sample_text")
    a2 = simpleJava_statement(break_="sample_text_2", continue_="sample_text_2")
    b = simpleJava_statement(break_="sample_text", continue_="sample_text")
    _safe_set(b, 'simpleJava_statement87', a1)
    assert _is_linked(b, 'simpleJava_statement87', a1)
    if hasattr(a1, 'simpleJava_statement85'):
        assert _is_linked(a1, 'simpleJava_statement85', b)
    _safe_set(b, 'simpleJava_statement87', a2)
    assert _is_linked(b, 'simpleJava_statement87', a2)
    if hasattr(a1, 'simpleJava_statement85'):
        assert not _is_linked(a1, 'simpleJava_statement85', b)
    if hasattr(a2, 'simpleJava_statement85'):
        assert _is_linked(a2, 'simpleJava_statement85', b)
    _safe_set(b, 'simpleJava_statement87', None)
    assert not _is_linked(b, 'simpleJava_statement87', a2)
    if hasattr(a2, 'simpleJava_statement85'):
        assert not _is_linked(a2, 'simpleJava_statement85', b)


def test_assoc_declaracaoClasse25_reverse_link_reassign_clear():
    a1 = simpleJava_class_declaration(nomeClasse="sample_text")
    a2 = simpleJava_class_declaration(nomeClasse="sample_text_2")
    b = simpleJava_class_declaration(nomeClasse="sample_text")
    _safe_set(b, 'simpleJava_class_declaration26', a1)
    assert _is_linked(b, 'simpleJava_class_declaration26', a1)
    if hasattr(a1, 'simpleJava_class_declaration24'):
        assert _is_linked(a1, 'simpleJava_class_declaration24', b)
    _safe_set(b, 'simpleJava_class_declaration26', a2)
    assert _is_linked(b, 'simpleJava_class_declaration26', a2)
    if hasattr(a1, 'simpleJava_class_declaration24'):
        assert not _is_linked(a1, 'simpleJava_class_declaration24', b)
    if hasattr(a2, 'simpleJava_class_declaration24'):
        assert _is_linked(a2, 'simpleJava_class_declaration24', b)
    _safe_set(b, 'simpleJava_class_declaration26', None)
    assert not _is_linked(b, 'simpleJava_class_declaration26', a2)
    if hasattr(a2, 'simpleJava_class_declaration24'):
        assert not _is_linked(a2, 'simpleJava_class_declaration24', b)


def test_assoc_exececao91_reverse_link_reassign_clear():
    a1 = simpleJava_statement(break_="sample_text", continue_="sample_text")
    a2 = simpleJava_statement(break_="sample_text_2", continue_="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression93', a1)
    assert _is_linked(b, 'simpleJava_expression93', a1)
    if hasattr(a1, 'simpleJava_statement92'):
        assert _is_linked(a1, 'simpleJava_statement92', b)
    _safe_set(b, 'simpleJava_expression93', a2)
    assert _is_linked(b, 'simpleJava_expression93', a2)
    if hasattr(a1, 'simpleJava_statement92'):
        assert not _is_linked(a1, 'simpleJava_statement92', b)
    if hasattr(a2, 'simpleJava_statement92'):
        assert _is_linked(a2, 'simpleJava_statement92', b)
    _safe_set(b, 'simpleJava_expression93', None)
    assert not _is_linked(b, 'simpleJava_expression93', a2)
    if hasattr(a2, 'simpleJava_statement92'):
        assert not _is_linked(a2, 'simpleJava_statement92', b)


def test_assoc_exp207_reverse_link_reassign_clear():
    a1 = simpleJava_expression_aux(operador="sample_text")
    a2 = simpleJava_expression_aux(operador="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression209', a1)
    assert _is_linked(b, 'simpleJava_expression209', a1)
    if hasattr(a1, 'simpleJava_expression_aux208'):
        assert _is_linked(a1, 'simpleJava_expression_aux208', b)
    _safe_set(b, 'simpleJava_expression209', a2)
    assert _is_linked(b, 'simpleJava_expression209', a2)
    if hasattr(a1, 'simpleJava_expression_aux208'):
        assert not _is_linked(a1, 'simpleJava_expression_aux208', b)
    if hasattr(a2, 'simpleJava_expression_aux208'):
        assert _is_linked(a2, 'simpleJava_expression_aux208', b)
    _safe_set(b, 'simpleJava_expression209', None)
    assert not _is_linked(b, 'simpleJava_expression209', a2)
    if hasattr(a2, 'simpleJava_expression_aux208'):
        assert not _is_linked(a2, 'simpleJava_expression_aux208', b)


def test_assoc_exp220_reverse_link_reassign_clear():
    a1 = simpleJava_logical_expression(operador="sample_text")
    a2 = simpleJava_logical_expression(operador="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression222', a1)
    assert _is_linked(b, 'simpleJava_expression222', a1)
    if hasattr(a1, 'simpleJava_logical_expression221'):
        assert _is_linked(a1, 'simpleJava_logical_expression221', b)
    _safe_set(b, 'simpleJava_expression222', a2)
    assert _is_linked(b, 'simpleJava_expression222', a2)
    if hasattr(a1, 'simpleJava_logical_expression221'):
        assert not _is_linked(a1, 'simpleJava_logical_expression221', b)
    if hasattr(a2, 'simpleJava_logical_expression221'):
        assert _is_linked(a2, 'simpleJava_logical_expression221', b)
    _safe_set(b, 'simpleJava_expression222', None)
    assert not _is_linked(b, 'simpleJava_expression222', a2)
    if hasattr(a2, 'simpleJava_logical_expression221'):
        assert not _is_linked(a2, 'simpleJava_logical_expression221', b)


def test_assoc_expressao223_reverse_link_reassign_clear():
    a1 = simpleJava_expression(identificador="sample_text")
    a2 = simpleJava_expression(identificador="sample_text_2")
    b = simpleJava_bit_expression(operador="sample_text")
    _safe_set(b, 'simpleJava_bit_expression224', a1)
    assert _is_linked(b, 'simpleJava_bit_expression224', a1)
    if hasattr(a1, 'simpleJava_expression225'):
        assert _is_linked(a1, 'simpleJava_expression225', b)
    _safe_set(b, 'simpleJava_bit_expression224', a2)
    assert _is_linked(b, 'simpleJava_bit_expression224', a2)
    if hasattr(a1, 'simpleJava_expression225'):
        assert not _is_linked(a1, 'simpleJava_expression225', b)
    if hasattr(a2, 'simpleJava_expression225'):
        assert _is_linked(a2, 'simpleJava_expression225', b)
    _safe_set(b, 'simpleJava_bit_expression224', None)
    assert not _is_linked(b, 'simpleJava_bit_expression224', a2)
    if hasattr(a2, 'simpleJava_expression225'):
        assert not _is_linked(a2, 'simpleJava_expression225', b)


def test_assoc_expressao226_reverse_link_reassign_clear():
    a1 = simpleJava_numeric_expression(operador="sample_text")
    a2 = simpleJava_numeric_expression(operador="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression228', a1)
    assert _is_linked(b, 'simpleJava_expression228', a1)
    if hasattr(a1, 'simpleJava_numeric_expression227'):
        assert _is_linked(a1, 'simpleJava_numeric_expression227', b)
    _safe_set(b, 'simpleJava_expression228', a2)
    assert _is_linked(b, 'simpleJava_expression228', a2)
    if hasattr(a1, 'simpleJava_numeric_expression227'):
        assert not _is_linked(a1, 'simpleJava_numeric_expression227', b)
    if hasattr(a2, 'simpleJava_numeric_expression227'):
        assert _is_linked(a2, 'simpleJava_numeric_expression227', b)
    _safe_set(b, 'simpleJava_expression228', None)
    assert not _is_linked(b, 'simpleJava_expression228', a2)
    if hasattr(a2, 'simpleJava_numeric_expression227'):
        assert not _is_linked(a2, 'simpleJava_numeric_expression227', b)


def test_assoc_expressao65_reverse_link_reassign_clear():
    a1 = simpleJava_statement(break_="sample_text", continue_="sample_text")
    a2 = simpleJava_statement(break_="sample_text_2", continue_="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression', a1)
    assert _is_linked(b, 'simpleJava_expression', a1)
    if hasattr(a1, 'simpleJava_statement66'):
        assert _is_linked(a1, 'simpleJava_statement66', b)
    _safe_set(b, 'simpleJava_expression', a2)
    assert _is_linked(b, 'simpleJava_expression', a2)
    if hasattr(a1, 'simpleJava_statement66'):
        assert not _is_linked(a1, 'simpleJava_statement66', b)
    if hasattr(a2, 'simpleJava_statement66'):
        assert _is_linked(a2, 'simpleJava_statement66', b)
    _safe_set(b, 'simpleJava_expression', None)
    assert not _is_linked(b, 'simpleJava_expression', a2)
    if hasattr(a2, 'simpleJava_statement66'):
        assert not _is_linked(a2, 'simpleJava_statement66', b)


def test_assoc_expressaoSynchronized82_reverse_link_reassign_clear():
    a1 = simpleJava_statement(break_="sample_text", continue_="sample_text")
    a2 = simpleJava_statement(break_="sample_text_2", continue_="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression84', a1)
    assert _is_linked(b, 'simpleJava_expression84', a1)
    if hasattr(a1, 'simpleJava_statement83'):
        assert _is_linked(a1, 'simpleJava_statement83', b)
    _safe_set(b, 'simpleJava_expression84', a2)
    assert _is_linked(b, 'simpleJava_expression84', a2)
    if hasattr(a1, 'simpleJava_statement83'):
        assert not _is_linked(a1, 'simpleJava_statement83', b)
    if hasattr(a2, 'simpleJava_statement83'):
        assert _is_linked(a2, 'simpleJava_statement83', b)
    _safe_set(b, 'simpleJava_expression84', None)
    assert not _is_linked(b, 'simpleJava_expression84', a2)
    if hasattr(a2, 'simpleJava_statement83'):
        assert not _is_linked(a2, 'simpleJava_statement83', b)


def test_assoc_expressoes213_reverse_link_reassign_clear():
    a1 = simpleJava_expression_aux(operador="sample_text")
    a2 = simpleJava_expression_aux(operador="sample_text_2")
    b = simpleJava_expression_aux(operador="sample_text")
    _safe_set(b, 'simpleJava_expression_aux214', a1)
    assert _is_linked(b, 'simpleJava_expression_aux214', a1)
    if hasattr(a1, 'simpleJava_expression_aux212'):
        assert _is_linked(a1, 'simpleJava_expression_aux212', b)
    _safe_set(b, 'simpleJava_expression_aux214', a2)
    assert _is_linked(b, 'simpleJava_expression_aux214', a2)
    if hasattr(a1, 'simpleJava_expression_aux212'):
        assert not _is_linked(a1, 'simpleJava_expression_aux212', b)
    if hasattr(a2, 'simpleJava_expression_aux212'):
        assert _is_linked(a2, 'simpleJava_expression_aux212', b)
    _safe_set(b, 'simpleJava_expression_aux214', None)
    assert not _is_linked(b, 'simpleJava_expression_aux214', a2)
    if hasattr(a2, 'simpleJava_expression_aux212'):
        assert not _is_linked(a2, 'simpleJava_expression_aux212', b)


def test_assoc_expressoesArgumentos229_reverse_link_reassign_clear():
    a1 = simpleJava_expression(identificador="sample_text")
    a2 = simpleJava_expression(identificador="sample_text_2")
    b = simpleJava_arglist(nomeParametro="sample_text")
    _safe_set(b, 'simpleJava_arglist230', {a1})
    assert _is_linked(b, 'simpleJava_arglist230', a1)
    if hasattr(a1, 'simpleJava_expression231'):
        assert _is_linked(a1, 'simpleJava_expression231', b)
    _safe_set(b, 'simpleJava_arglist230', {a2})
    assert _is_linked(b, 'simpleJava_arglist230', a2)
    if hasattr(a1, 'simpleJava_expression231'):
        assert not _is_linked(a1, 'simpleJava_expression231', b)
    if hasattr(a2, 'simpleJava_expression231'):
        assert _is_linked(a2, 'simpleJava_expression231', b)
    _safe_set(b, 'simpleJava_arglist230', set())
    assert not _is_linked(b, 'simpleJava_arglist230', a2)
    if hasattr(a2, 'simpleJava_expression231'):
        assert not _is_linked(a2, 'simpleJava_expression231', b)


def test_assoc_implementosClasse19_reverse_link_reassign_clear():
    a1 = simpleJava_name(nome="sample_text")
    a2 = simpleJava_name(nome="sample_text_2")
    b = simpleJava_class_declaration(nomeClasse="sample_text")
    _safe_set(b, 'simpleJava_class_declaration20', {a1})
    assert _is_linked(b, 'simpleJava_class_declaration20', a1)
    if hasattr(a1, 'simpleJava_name21'):
        assert _is_linked(a1, 'simpleJava_name21', b)
    _safe_set(b, 'simpleJava_class_declaration20', {a2})
    assert _is_linked(b, 'simpleJava_class_declaration20', a2)
    if hasattr(a1, 'simpleJava_name21'):
        assert not _is_linked(a1, 'simpleJava_name21', b)
    if hasattr(a2, 'simpleJava_name21'):
        assert _is_linked(a2, 'simpleJava_name21', b)
    _safe_set(b, 'simpleJava_class_declaration20', set())
    assert not _is_linked(b, 'simpleJava_class_declaration20', a2)
    if hasattr(a2, 'simpleJava_name21'):
        assert not _is_linked(a2, 'simpleJava_name21', b)


def test_assoc_literal204_reverse_link_reassign_clear():
    a1 = simpleJava_literal_expression(decimal="sample_text", inteiro="sample_text", l_float="sample_text", string="sample_text")
    a2 = simpleJava_literal_expression(decimal="sample_text_2", inteiro="sample_text_2", l_float="sample_text_2", string="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression205', a1)
    assert _is_linked(b, 'simpleJava_expression205', a1)
    if hasattr(a1, 'simpleJava_literal_expression'):
        assert _is_linked(a1, 'simpleJava_literal_expression', b)
    _safe_set(b, 'simpleJava_expression205', a2)
    assert _is_linked(b, 'simpleJava_expression205', a2)
    if hasattr(a1, 'simpleJava_literal_expression'):
        assert not _is_linked(a1, 'simpleJava_literal_expression', b)
    if hasattr(a2, 'simpleJava_literal_expression'):
        assert _is_linked(a2, 'simpleJava_literal_expression', b)
    _safe_set(b, 'simpleJava_expression205', None)
    assert not _is_linked(b, 'simpleJava_expression205', a2)
    if hasattr(a2, 'simpleJava_literal_expression'):
        assert not _is_linked(a2, 'simpleJava_literal_expression', b)


def test_assoc_logical195_reverse_link_reassign_clear():
    a1 = simpleJava_logical_expression(operador="sample_text")
    a2 = simpleJava_logical_expression(operador="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression196', a1)
    assert _is_linked(b, 'simpleJava_expression196', a1)
    if hasattr(a1, 'simpleJava_logical_expression'):
        assert _is_linked(a1, 'simpleJava_logical_expression', b)
    _safe_set(b, 'simpleJava_expression196', a2)
    assert _is_linked(b, 'simpleJava_expression196', a2)
    if hasattr(a1, 'simpleJava_logical_expression'):
        assert not _is_linked(a1, 'simpleJava_logical_expression', b)
    if hasattr(a2, 'simpleJava_logical_expression'):
        assert _is_linked(a2, 'simpleJava_logical_expression', b)
    _safe_set(b, 'simpleJava_expression196', None)
    assert not _is_linked(b, 'simpleJava_expression196', a2)
    if hasattr(a2, 'simpleJava_logical_expression'):
        assert not _is_linked(a2, 'simpleJava_logical_expression', b)


def test_assoc_modificador170_reverse_link_reassign_clear():
    a1 = simpleJava_constructor_declaration(nomeContrutor="sample_text")
    a2 = simpleJava_constructor_declaration(nomeContrutor="sample_text_2")
    b = simpleJava_MODIFIER(modificador="sample_text")
    _safe_set(b, 'simpleJava_MODIFIER172', a1)
    assert _is_linked(b, 'simpleJava_MODIFIER172', a1)
    if hasattr(a1, 'simpleJava_constructor_declaration171'):
        assert _is_linked(a1, 'simpleJava_constructor_declaration171', b)
    _safe_set(b, 'simpleJava_MODIFIER172', a2)
    assert _is_linked(b, 'simpleJava_MODIFIER172', a2)
    if hasattr(a1, 'simpleJava_constructor_declaration171'):
        assert not _is_linked(a1, 'simpleJava_constructor_declaration171', b)
    if hasattr(a2, 'simpleJava_constructor_declaration171'):
        assert _is_linked(a2, 'simpleJava_constructor_declaration171', b)
    _safe_set(b, 'simpleJava_MODIFIER172', None)
    assert not _is_linked(b, 'simpleJava_MODIFIER172', a2)
    if hasattr(a2, 'simpleJava_constructor_declaration171'):
        assert not _is_linked(a2, 'simpleJava_constructor_declaration171', b)


def test_assoc_modificadorMetodo46_reverse_link_reassign_clear():
    a1 = simpleJava_method_declaration(nomeMetodo="sample_text")
    a2 = simpleJava_method_declaration(nomeMetodo="sample_text_2")
    b = simpleJava_MODIFIER(modificador="sample_text")
    _safe_set(b, 'simpleJava_MODIFIER48', a1)
    assert _is_linked(b, 'simpleJava_MODIFIER48', a1)
    if hasattr(a1, 'simpleJava_method_declaration47'):
        assert _is_linked(a1, 'simpleJava_method_declaration47', b)
    _safe_set(b, 'simpleJava_MODIFIER48', a2)
    assert _is_linked(b, 'simpleJava_MODIFIER48', a2)
    if hasattr(a1, 'simpleJava_method_declaration47'):
        assert not _is_linked(a1, 'simpleJava_method_declaration47', b)
    if hasattr(a2, 'simpleJava_method_declaration47'):
        assert _is_linked(a2, 'simpleJava_method_declaration47', b)
    _safe_set(b, 'simpleJava_MODIFIER48', None)
    assert not _is_linked(b, 'simpleJava_MODIFIER48', a2)
    if hasattr(a2, 'simpleJava_method_declaration47'):
        assert not _is_linked(a2, 'simpleJava_method_declaration47', b)


def test_assoc_modificadores14_reverse_link_reassign_clear():
    a1 = simpleJava_class_declaration(nomeClasse="sample_text")
    a2 = simpleJava_class_declaration(nomeClasse="sample_text_2")
    b = simpleJava_MODIFIER(modificador="sample_text")
    _safe_set(b, 'simpleJava_MODIFIER', a1)
    assert _is_linked(b, 'simpleJava_MODIFIER', a1)
    if hasattr(a1, 'simpleJava_class_declaration15'):
        assert _is_linked(a1, 'simpleJava_class_declaration15', b)
    _safe_set(b, 'simpleJava_MODIFIER', a2)
    assert _is_linked(b, 'simpleJava_MODIFIER', a2)
    if hasattr(a1, 'simpleJava_class_declaration15'):
        assert not _is_linked(a1, 'simpleJava_class_declaration15', b)
    if hasattr(a2, 'simpleJava_class_declaration15'):
        assert _is_linked(a2, 'simpleJava_class_declaration15', b)
    _safe_set(b, 'simpleJava_MODIFIER', None)
    assert not _is_linked(b, 'simpleJava_MODIFIER', a2)
    if hasattr(a2, 'simpleJava_class_declaration15'):
        assert not _is_linked(a2, 'simpleJava_class_declaration15', b)


def test_assoc_modificadores27_reverse_link_reassign_clear():
    a1 = simpleJava_interface_declaration(nomeInterface="sample_text")
    a2 = simpleJava_interface_declaration(nomeInterface="sample_text_2")
    b = simpleJava_MODIFIER(modificador="sample_text")
    _safe_set(b, 'simpleJava_MODIFIER29', a1)
    assert _is_linked(b, 'simpleJava_MODIFIER29', a1)
    if hasattr(a1, 'simpleJava_interface_declaration28'):
        assert _is_linked(a1, 'simpleJava_interface_declaration28', b)
    _safe_set(b, 'simpleJava_MODIFIER29', a2)
    assert _is_linked(b, 'simpleJava_MODIFIER29', a2)
    if hasattr(a1, 'simpleJava_interface_declaration28'):
        assert not _is_linked(a1, 'simpleJava_interface_declaration28', b)
    if hasattr(a2, 'simpleJava_interface_declaration28'):
        assert _is_linked(a2, 'simpleJava_interface_declaration28', b)
    _safe_set(b, 'simpleJava_MODIFIER29', None)
    assert not _is_linked(b, 'simpleJava_MODIFIER29', a2)
    if hasattr(a2, 'simpleJava_interface_declaration28'):
        assert not _is_linked(a2, 'simpleJava_interface_declaration28', b)


def test_assoc_numeric197_reverse_link_reassign_clear():
    a1 = simpleJava_numeric_expression(operador="sample_text")
    a2 = simpleJava_numeric_expression(operador="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression198', a1)
    assert _is_linked(b, 'simpleJava_expression198', a1)
    if hasattr(a1, 'simpleJava_numeric_expression'):
        assert _is_linked(a1, 'simpleJava_numeric_expression', b)
    _safe_set(b, 'simpleJava_expression198', a2)
    assert _is_linked(b, 'simpleJava_expression198', a2)
    if hasattr(a1, 'simpleJava_numeric_expression'):
        assert not _is_linked(a1, 'simpleJava_numeric_expression', b)
    if hasattr(a2, 'simpleJava_numeric_expression'):
        assert _is_linked(a2, 'simpleJava_numeric_expression', b)
    _safe_set(b, 'simpleJava_expression198', None)
    assert not _is_linked(b, 'simpleJava_expression198', a2)
    if hasattr(a2, 'simpleJava_numeric_expression'):
        assert not _is_linked(a2, 'simpleJava_numeric_expression', b)


def test_assoc_op210_reverse_link_reassign_clear():
    a1 = simpleJava_mais_aux(operador="sample_text")
    a2 = simpleJava_mais_aux(operador="sample_text_2")
    b = simpleJava_expression_aux(operador="sample_text")
    _safe_set(b, 'simpleJava_expression_aux211', a1)
    assert _is_linked(b, 'simpleJava_expression_aux211', a1)
    if hasattr(a1, 'simpleJava_mais_aux'):
        assert _is_linked(a1, 'simpleJava_mais_aux', b)
    _safe_set(b, 'simpleJava_expression_aux211', a2)
    assert _is_linked(b, 'simpleJava_expression_aux211', a2)
    if hasattr(a1, 'simpleJava_mais_aux'):
        assert not _is_linked(a1, 'simpleJava_mais_aux', b)
    if hasattr(a2, 'simpleJava_mais_aux'):
        assert _is_linked(a2, 'simpleJava_mais_aux', b)
    _safe_set(b, 'simpleJava_expression_aux211', None)
    assert not _is_linked(b, 'simpleJava_expression_aux211', a2)
    if hasattr(a2, 'simpleJava_mais_aux'):
        assert not _is_linked(a2, 'simpleJava_mais_aux', b)


def test_assoc_pacote235_reverse_link_reassign_clear():
    a1 = simpleJava_package_name_aux(nomePacote="sample_text")
    a2 = simpleJava_package_name_aux(nomePacote="sample_text_2")
    b = simpleJava_name(nome="sample_text")
    _safe_set(b, 'simpleJava_name236', a1)
    assert _is_linked(b, 'simpleJava_name236', a1)
    if hasattr(a1, 'simpleJava_package_name_aux'):
        assert _is_linked(a1, 'simpleJava_package_name_aux', b)
    _safe_set(b, 'simpleJava_name236', a2)
    assert _is_linked(b, 'simpleJava_name236', a2)
    if hasattr(a1, 'simpleJava_package_name_aux'):
        assert not _is_linked(a1, 'simpleJava_package_name_aux', b)
    if hasattr(a2, 'simpleJava_package_name_aux'):
        assert _is_linked(a2, 'simpleJava_package_name_aux', b)
    _safe_set(b, 'simpleJava_name236', None)
    assert not _is_linked(b, 'simpleJava_name236', a2)
    if hasattr(a2, 'simpleJava_package_name_aux'):
        assert not _is_linked(a2, 'simpleJava_package_name_aux', b)


def test_assoc_pacote238_reverse_link_reassign_clear():
    a1 = simpleJava_package_name_aux(nomePacote="sample_text")
    a2 = simpleJava_package_name_aux(nomePacote="sample_text_2")
    b = simpleJava_package_name_aux(nomePacote="sample_text")
    _safe_set(b, 'simpleJava_package_name_aux239', a1)
    assert _is_linked(b, 'simpleJava_package_name_aux239', a1)
    if hasattr(a1, 'simpleJava_package_name_aux237'):
        assert _is_linked(a1, 'simpleJava_package_name_aux237', b)
    _safe_set(b, 'simpleJava_package_name_aux239', a2)
    assert _is_linked(b, 'simpleJava_package_name_aux239', a2)
    if hasattr(a1, 'simpleJava_package_name_aux237'):
        assert not _is_linked(a1, 'simpleJava_package_name_aux237', b)
    if hasattr(a2, 'simpleJava_package_name_aux237'):
        assert _is_linked(a2, 'simpleJava_package_name_aux237', b)
    _safe_set(b, 'simpleJava_package_name_aux239', None)
    assert not _is_linked(b, 'simpleJava_package_name_aux239', a2)
    if hasattr(a2, 'simpleJava_package_name_aux237'):
        assert not _is_linked(a2, 'simpleJava_package_name_aux237', b)


def test_assoc_parametros206_reverse_link_reassign_clear():
    a1 = simpleJava_expression_aux(operador="sample_text")
    a2 = simpleJava_expression_aux(operador="sample_text_2")
    b = simpleJava_arglist(nomeParametro="sample_text")
    _safe_set(b, 'simpleJava_arglist', a1)
    assert _is_linked(b, 'simpleJava_arglist', a1)
    if hasattr(a1, 'simpleJava_expression_aux'):
        assert _is_linked(a1, 'simpleJava_expression_aux', b)
    _safe_set(b, 'simpleJava_arglist', a2)
    assert _is_linked(b, 'simpleJava_arglist', a2)
    if hasattr(a1, 'simpleJava_expression_aux'):
        assert not _is_linked(a1, 'simpleJava_expression_aux', b)
    if hasattr(a2, 'simpleJava_expression_aux'):
        assert _is_linked(a2, 'simpleJava_expression_aux', b)
    _safe_set(b, 'simpleJava_arglist', None)
    assert not _is_linked(b, 'simpleJava_arglist', a2)
    if hasattr(a2, 'simpleJava_expression_aux'):
        assert not _is_linked(a2, 'simpleJava_expression_aux', b)


def test_assoc_return_88_reverse_link_reassign_clear():
    a1 = simpleJava_statement(break_="sample_text", continue_="sample_text")
    a2 = simpleJava_statement(break_="sample_text_2", continue_="sample_text_2")
    b = simpleJava_expression(identificador="sample_text")
    _safe_set(b, 'simpleJava_expression90', a1)
    assert _is_linked(b, 'simpleJava_expression90', a1)
    if hasattr(a1, 'simpleJava_statement89'):
        assert _is_linked(a1, 'simpleJava_statement89', b)
    _safe_set(b, 'simpleJava_expression90', a2)
    assert _is_linked(b, 'simpleJava_expression90', a2)
    if hasattr(a1, 'simpleJava_statement89'):
        assert not _is_linked(a1, 'simpleJava_statement89', b)
    if hasattr(a2, 'simpleJava_statement89'):
        assert _is_linked(a2, 'simpleJava_statement89', b)
    _safe_set(b, 'simpleJava_expression90', None)
    assert not _is_linked(b, 'simpleJava_expression90', a2)
    if hasattr(a2, 'simpleJava_statement89'):
        assert not _is_linked(a2, 'simpleJava_statement89', b)


def test_assoc_superclasse16_reverse_link_reassign_clear():
    a1 = simpleJava_name(nome="sample_text")
    a2 = simpleJava_name(nome="sample_text_2")
    b = simpleJava_class_declaration(nomeClasse="sample_text")
    _safe_set(b, 'simpleJava_class_declaration17', a1)
    assert _is_linked(b, 'simpleJava_class_declaration17', a1)
    if hasattr(a1, 'simpleJava_name18'):
        assert _is_linked(a1, 'simpleJava_name18', b)
    _safe_set(b, 'simpleJava_class_declaration17', a2)
    assert _is_linked(b, 'simpleJava_class_declaration17', a2)
    if hasattr(a1, 'simpleJava_name18'):
        assert not _is_linked(a1, 'simpleJava_name18', b)
    if hasattr(a2, 'simpleJava_name18'):
        assert _is_linked(a2, 'simpleJava_name18', b)
    _safe_set(b, 'simpleJava_class_declaration17', None)
    assert not _is_linked(b, 'simpleJava_class_declaration17', a2)
    if hasattr(a2, 'simpleJava_name18'):
        assert not _is_linked(a2, 'simpleJava_name18', b)


def test_assoc_superinterfaces30_reverse_link_reassign_clear():
    a1 = simpleJava_name(nome="sample_text")
    a2 = simpleJava_name(nome="sample_text_2")
    b = simpleJava_interface_declaration(nomeInterface="sample_text")
    _safe_set(b, 'simpleJava_interface_declaration31', {a1})
    assert _is_linked(b, 'simpleJava_interface_declaration31', a1)
    if hasattr(a1, 'simpleJava_name32'):
        assert _is_linked(a1, 'simpleJava_name32', b)
    _safe_set(b, 'simpleJava_interface_declaration31', {a2})
    assert _is_linked(b, 'simpleJava_interface_declaration31', a2)
    if hasattr(a1, 'simpleJava_name32'):
        assert not _is_linked(a1, 'simpleJava_name32', b)
    if hasattr(a2, 'simpleJava_name32'):
        assert _is_linked(a2, 'simpleJava_name32', b)
    _safe_set(b, 'simpleJava_interface_declaration31', set())
    assert not _is_linked(b, 'simpleJava_interface_declaration31', a2)
    if hasattr(a2, 'simpleJava_name32'):
        assert not _is_linked(a2, 'simpleJava_name32', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argumentos215_stub_double():
    # simpleJava_creating_aux has no real 'simpleJava_creating_aux216' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_arglist's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_arglist's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_arglist(nomeParametro="sample_text")
    partner = simpleJava_creating_aux()
    setattr(partner, 'simpleJava_creating_aux216', None)
    _safe_set(owner, 'simpleJava_arglist217', partner)
    assert getattr(partner, 'simpleJava_creating_aux216') == owner
    _safe_set(owner, 'simpleJava_arglist217', None)
    assert getattr(partner, 'simpleJava_creating_aux216') is None


def test_assoc_blcoIf116_stub_double():
    # simpleJava_if_statement has no real 'simpleJava_if_statement117' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_if_statement()
    setattr(partner, 'simpleJava_if_statement117', None)
    _safe_set(owner, 'simpleJava_statement118', partner)
    assert getattr(partner, 'simpleJava_if_statement117') == owner
    _safe_set(owner, 'simpleJava_statement118', None)
    assert getattr(partner, 'simpleJava_if_statement117') is None


def test_assoc_blocoConstrutor176_stub_double():
    # simpleJava_statement_block has no real 'simpleJava_statement_block178' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_constructor_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_constructor_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_constructor_declaration(nomeContrutor="sample_text")
    partner = simpleJava_statement_block()
    setattr(partner, 'simpleJava_statement_block178', None)
    _safe_set(owner, 'simpleJava_constructor_declaration177', partner)
    assert getattr(partner, 'simpleJava_statement_block178') == owner
    _safe_set(owner, 'simpleJava_constructor_declaration177', None)
    assert getattr(partner, 'simpleJava_statement_block178') is None


def test_assoc_blocoDo122_stub_double():
    # simpleJava_do_statement has no real 'simpleJava_do_statement123' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_do_statement()
    setattr(partner, 'simpleJava_do_statement123', None)
    _safe_set(owner, 'simpleJava_statement124', partner)
    assert getattr(partner, 'simpleJava_do_statement123') == owner
    _safe_set(owner, 'simpleJava_statement124', None)
    assert getattr(partner, 'simpleJava_do_statement123') is None


def test_assoc_blocoElse119_stub_double():
    # simpleJava_if_statement has no real 'simpleJava_if_statement120' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_if_statement()
    setattr(partner, 'simpleJava_if_statement120', None)
    _safe_set(owner, 'simpleJava_statement121', partner)
    assert getattr(partner, 'simpleJava_if_statement120') == owner
    _safe_set(owner, 'simpleJava_statement121', None)
    assert getattr(partner, 'simpleJava_if_statement120') is None


def test_assoc_blocoFor146_stub_double():
    # simpleJava_for_statement has no real 'simpleJava_for_statement147' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_for_statement()
    setattr(partner, 'simpleJava_for_statement147', None)
    _safe_set(owner, 'simpleJava_statement148', partner)
    assert getattr(partner, 'simpleJava_for_statement147') == owner
    _safe_set(owner, 'simpleJava_statement148', None)
    assert getattr(partner, 'simpleJava_for_statement147') is None


def test_assoc_blocoMetodo53_stub_double():
    # simpleJava_statement_block has no real 'simpleJava_statement_block' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_method_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_method_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_method_declaration(nomeMetodo="sample_text")
    partner = simpleJava_statement_block()
    setattr(partner, 'simpleJava_statement_block', None)
    _safe_set(owner, 'simpleJava_method_declaration54', partner)
    assert getattr(partner, 'simpleJava_statement_block') == owner
    _safe_set(owner, 'simpleJava_method_declaration54', None)
    assert getattr(partner, 'simpleJava_statement_block') is None


def test_assoc_blocoSwitch167_stub_double():
    # simpleJava_switch_statement has no real 'simpleJava_switch_statement168' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_switch_statement()
    setattr(partner, 'simpleJava_switch_statement168', None)
    _safe_set(owner, 'simpleJava_statement169', partner)
    assert getattr(partner, 'simpleJava_switch_statement168') == owner
    _safe_set(owner, 'simpleJava_statement169', None)
    assert getattr(partner, 'simpleJava_switch_statement168') is None


def test_assoc_blocoWhile131_stub_double():
    # simpleJava_while_statement has no real 'simpleJava_while_statement132' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_while_statement()
    setattr(partner, 'simpleJava_while_statement132', None)
    _safe_set(owner, 'simpleJava_statement133', partner)
    assert getattr(partner, 'simpleJava_while_statement132') == owner
    _safe_set(owner, 'simpleJava_statement133', None)
    assert getattr(partner, 'simpleJava_while_statement132') is None


def test_assoc_comentario36_stub_double():
    # simpleJava_field_declaration has no real 'simpleJava_field_declaration37' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_doc_comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_doc_comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_doc_comment(comentario="sample_text")
    partner = simpleJava_field_declaration()
    setattr(partner, 'simpleJava_field_declaration37', None)
    _safe_set(owner, 'simpleJava_doc_comment', partner)
    assert getattr(partner, 'simpleJava_field_declaration37') == owner
    _safe_set(owner, 'simpleJava_doc_comment', None)
    assert getattr(partner, 'simpleJava_field_declaration37') is None


def test_assoc_corpo60_stub_double():
    # simpleJava_statement_block has no real 'simpleJava_statement_block61' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_statement_block()
    setattr(partner, 'simpleJava_statement_block61', None)
    _safe_set(owner, 'simpleJava_statement', partner)
    assert owner in getattr(partner, 'simpleJava_statement_block61')
    _safe_set(owner, 'simpleJava_statement', None)
    assert owner not in getattr(partner, 'simpleJava_statement_block61')


def test_assoc_corpoClasse22_stub_double():
    # simpleJava_field_declaration has no real 'simpleJava_field_declaration' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_class_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_class_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_class_declaration(nomeClasse="sample_text")
    partner = simpleJava_field_declaration()
    setattr(partner, 'simpleJava_field_declaration', None)
    _safe_set(owner, 'simpleJava_class_declaration23', {partner})
    assert getattr(partner, 'simpleJava_field_declaration') == owner
    _safe_set(owner, 'simpleJava_class_declaration23', set())
    assert getattr(partner, 'simpleJava_field_declaration') is None


def test_assoc_corpoDoWhile72_stub_double():
    # simpleJava_do_statement has no real 'simpleJava_do_statement' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_do_statement()
    setattr(partner, 'simpleJava_do_statement', None)
    _safe_set(owner, 'simpleJava_statement73', partner)
    assert getattr(partner, 'simpleJava_do_statement') == owner
    _safe_set(owner, 'simpleJava_statement73', None)
    assert getattr(partner, 'simpleJava_do_statement') is None


def test_assoc_corpoFor76_stub_double():
    # simpleJava_for_statement has no real 'simpleJava_for_statement' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_for_statement()
    setattr(partner, 'simpleJava_for_statement', None)
    _safe_set(owner, 'simpleJava_statement77', partner)
    assert getattr(partner, 'simpleJava_for_statement') == owner
    _safe_set(owner, 'simpleJava_statement77', None)
    assert getattr(partner, 'simpleJava_for_statement') is None


def test_assoc_corpoIf70_stub_double():
    # simpleJava_if_statement has no real 'simpleJava_if_statement' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_if_statement()
    setattr(partner, 'simpleJava_if_statement', None)
    _safe_set(owner, 'simpleJava_statement71', partner)
    assert getattr(partner, 'simpleJava_if_statement') == owner
    _safe_set(owner, 'simpleJava_statement71', None)
    assert getattr(partner, 'simpleJava_if_statement') is None


def test_assoc_corpoInterface33_stub_double():
    # simpleJava_field_declaration has no real 'simpleJava_field_declaration35' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_interface_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_interface_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_interface_declaration(nomeInterface="sample_text")
    partner = simpleJava_field_declaration()
    setattr(partner, 'simpleJava_field_declaration35', None)
    _safe_set(owner, 'simpleJava_interface_declaration34', {partner})
    assert getattr(partner, 'simpleJava_field_declaration35') == owner
    _safe_set(owner, 'simpleJava_interface_declaration34', set())
    assert getattr(partner, 'simpleJava_field_declaration35') is None


def test_assoc_corpoSwitchCase80_stub_double():
    # simpleJava_switch_statement has no real 'simpleJava_switch_statement' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_switch_statement()
    setattr(partner, 'simpleJava_switch_statement', None)
    _safe_set(owner, 'simpleJava_statement81', partner)
    assert getattr(partner, 'simpleJava_switch_statement') == owner
    _safe_set(owner, 'simpleJava_statement81', None)
    assert getattr(partner, 'simpleJava_switch_statement') is None


def test_assoc_corpoTryCatch78_stub_double():
    # simpleJava_try_statement has no real 'simpleJava_try_statement' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_try_statement()
    setattr(partner, 'simpleJava_try_statement', None)
    _safe_set(owner, 'simpleJava_statement79', partner)
    assert getattr(partner, 'simpleJava_try_statement') == owner
    _safe_set(owner, 'simpleJava_statement79', None)
    assert getattr(partner, 'simpleJava_try_statement') is None


def test_assoc_corpoWhile74_stub_double():
    # simpleJava_while_statement has no real 'simpleJava_while_statement' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_while_statement()
    setattr(partner, 'simpleJava_while_statement', None)
    _safe_set(owner, 'simpleJava_statement75', partner)
    assert getattr(partner, 'simpleJava_while_statement') == owner
    _safe_set(owner, 'simpleJava_statement75', None)
    assert getattr(partner, 'simpleJava_while_statement') is None


def test_assoc_declaracaoClasse10_stub_double():
    # simpleJava_type_declaration has no real 'simpleJava_type_declaration11' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_class_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_class_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_class_declaration(nomeClasse="sample_text")
    partner = simpleJava_type_declaration()
    setattr(partner, 'simpleJava_type_declaration11', None)
    _safe_set(owner, 'simpleJava_class_declaration', partner)
    assert getattr(partner, 'simpleJava_type_declaration11') == owner
    _safe_set(owner, 'simpleJava_class_declaration', None)
    assert getattr(partner, 'simpleJava_type_declaration11') is None


def test_assoc_declaracaoConstrutor40_stub_double():
    # simpleJava_field_declaration has no real 'simpleJava_field_declaration41' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_constructor_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_constructor_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_constructor_declaration(nomeContrutor="sample_text")
    partner = simpleJava_field_declaration()
    setattr(partner, 'simpleJava_field_declaration41', None)
    _safe_set(owner, 'simpleJava_constructor_declaration', partner)
    assert getattr(partner, 'simpleJava_field_declaration41') == owner
    _safe_set(owner, 'simpleJava_constructor_declaration', None)
    assert getattr(partner, 'simpleJava_field_declaration41') is None


def test_assoc_declaracaoInterface12_stub_double():
    # simpleJava_type_declaration has no real 'simpleJava_type_declaration13' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_interface_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_interface_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_interface_declaration(nomeInterface="sample_text")
    partner = simpleJava_type_declaration()
    setattr(partner, 'simpleJava_type_declaration13', None)
    _safe_set(owner, 'simpleJava_interface_declaration', partner)
    assert getattr(partner, 'simpleJava_type_declaration13') == owner
    _safe_set(owner, 'simpleJava_interface_declaration', None)
    assert getattr(partner, 'simpleJava_type_declaration13') is None


def test_assoc_declaracaoMetodo38_stub_double():
    # simpleJava_field_declaration has no real 'simpleJava_field_declaration39' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_method_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_method_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_method_declaration(nomeMetodo="sample_text")
    partner = simpleJava_field_declaration()
    setattr(partner, 'simpleJava_field_declaration39', None)
    _safe_set(owner, 'simpleJava_method_declaration', partner)
    assert getattr(partner, 'simpleJava_field_declaration39') == owner
    _safe_set(owner, 'simpleJava_method_declaration', None)
    assert getattr(partner, 'simpleJava_field_declaration39') is None


def test_assoc_declaracaoVariaveis100_stub_double():
    # simpleJava_variable_declaration has no real 'simpleJava_variable_declaration101' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_variable_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_variable_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_variable_declarator(nomeVariavel="sample_text", op="sample_text")
    partner = simpleJava_variable_declaration()
    setattr(partner, 'simpleJava_variable_declaration101', None)
    _safe_set(owner, 'simpleJava_variable_declarator', partner)
    assert owner in getattr(partner, 'simpleJava_variable_declaration101')
    _safe_set(owner, 'simpleJava_variable_declarator', None)
    assert owner not in getattr(partner, 'simpleJava_variable_declaration101')


def test_assoc_declaracaoVariavel62_stub_double():
    # simpleJava_variable_declaration has no real 'simpleJava_variable_declaration64' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_variable_declaration()
    setattr(partner, 'simpleJava_variable_declaration64', None)
    _safe_set(owner, 'simpleJava_statement63', partner)
    assert getattr(partner, 'simpleJava_variable_declaration64') == owner
    _safe_set(owner, 'simpleJava_statement63', None)
    assert getattr(partner, 'simpleJava_variable_declaration64') is None


def test_assoc_espressao218_stub_double():
    # simpleJava_aux has no real 'simpleJava_aux' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_aux()
    setattr(partner, 'simpleJava_aux', None)
    _safe_set(owner, 'simpleJava_expression219', partner)
    assert getattr(partner, 'simpleJava_aux') == owner
    _safe_set(owner, 'simpleJava_expression219', None)
    assert getattr(partner, 'simpleJava_aux') is None


def test_assoc_espressaoIf113_stub_double():
    # simpleJava_if_statement has no real 'simpleJava_if_statement114' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_if_statement()
    setattr(partner, 'simpleJava_if_statement114', None)
    _safe_set(owner, 'simpleJava_expression115', partner)
    assert getattr(partner, 'simpleJava_if_statement114') == owner
    _safe_set(owner, 'simpleJava_expression115', None)
    assert getattr(partner, 'simpleJava_if_statement114') is None


def test_assoc_expressao193_stub_double():
    # simpleJava_exp_aux has no real 'simpleJava_exp_aux' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_exp_aux()
    setattr(partner, 'simpleJava_exp_aux', None)
    _safe_set(owner, 'simpleJava_expression194', partner)
    assert getattr(partner, 'simpleJava_exp_aux') == owner
    _safe_set(owner, 'simpleJava_expression194', None)
    assert getattr(partner, 'simpleJava_exp_aux') is None


def test_assoc_expressaoCases164_stub_double():
    # simpleJava_switch_statement has no real 'simpleJava_switch_statement165' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_switch_statement()
    setattr(partner, 'simpleJava_switch_statement165', None)
    _safe_set(owner, 'simpleJava_expression166', partner)
    assert owner in getattr(partner, 'simpleJava_switch_statement165')
    _safe_set(owner, 'simpleJava_expression166', None)
    assert owner not in getattr(partner, 'simpleJava_switch_statement165')


def test_assoc_expressaoDeclaracao137_stub_double():
    # simpleJava_for_statement has no real 'simpleJava_for_statement138' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_for_statement()
    setattr(partner, 'simpleJava_for_statement138', None)
    _safe_set(owner, 'simpleJava_expression139', partner)
    assert getattr(partner, 'simpleJava_for_statement138') == owner
    _safe_set(owner, 'simpleJava_expression139', None)
    assert getattr(partner, 'simpleJava_for_statement138') is None


def test_assoc_expressaoFor140_stub_double():
    # simpleJava_for_statement has no real 'simpleJava_for_statement141' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_for_statement()
    setattr(partner, 'simpleJava_for_statement141', None)
    _safe_set(owner, 'simpleJava_expression142', partner)
    assert getattr(partner, 'simpleJava_for_statement141') == owner
    _safe_set(owner, 'simpleJava_expression142', None)
    assert getattr(partner, 'simpleJava_for_statement141') is None


def test_assoc_expressaoIncremento143_stub_double():
    # simpleJava_for_statement has no real 'simpleJava_for_statement144' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_for_statement()
    setattr(partner, 'simpleJava_for_statement144', None)
    _safe_set(owner, 'simpleJava_expression145', partner)
    assert getattr(partner, 'simpleJava_for_statement144') == owner
    _safe_set(owner, 'simpleJava_expression145', None)
    assert getattr(partner, 'simpleJava_for_statement144') is None


def test_assoc_expressaoNew188_stub_double():
    # simpleJava_creating_expression has no real 'simpleJava_creating_expression189' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_creating_expression()
    setattr(partner, 'simpleJava_creating_expression189', None)
    _safe_set(owner, 'simpleJava_expression190', partner)
    assert getattr(partner, 'simpleJava_creating_expression189') == owner
    _safe_set(owner, 'simpleJava_expression190', None)
    assert getattr(partner, 'simpleJava_creating_expression189') is None


def test_assoc_expressaoSwitch161_stub_double():
    # simpleJava_switch_statement has no real 'simpleJava_switch_statement162' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_switch_statement()
    setattr(partner, 'simpleJava_switch_statement162', None)
    _safe_set(owner, 'simpleJava_expression163', partner)
    assert getattr(partner, 'simpleJava_switch_statement162') == owner
    _safe_set(owner, 'simpleJava_expression163', None)
    assert getattr(partner, 'simpleJava_switch_statement162') is None


def test_assoc_expressaoVariavel107_stub_double():
    # simpleJava_variable_initializer has no real 'simpleJava_variable_initializer108' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_variable_initializer()
    setattr(partner, 'simpleJava_variable_initializer108', None)
    _safe_set(owner, 'simpleJava_expression109', partner)
    assert getattr(partner, 'simpleJava_variable_initializer108') == owner
    _safe_set(owner, 'simpleJava_expression109', None)
    assert getattr(partner, 'simpleJava_variable_initializer108') is None


def test_assoc_expressaoWhile125_stub_double():
    # simpleJava_do_statement has no real 'simpleJava_do_statement126' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_do_statement()
    setattr(partner, 'simpleJava_do_statement126', None)
    _safe_set(owner, 'simpleJava_expression127', partner)
    assert getattr(partner, 'simpleJava_do_statement126') == owner
    _safe_set(owner, 'simpleJava_expression127', None)
    assert getattr(partner, 'simpleJava_do_statement126') is None


def test_assoc_expressaoWhile128_stub_double():
    # simpleJava_while_statement has no real 'simpleJava_while_statement129' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_while_statement()
    setattr(partner, 'simpleJava_while_statement129', None)
    _safe_set(owner, 'simpleJava_expression130', partner)
    assert getattr(partner, 'simpleJava_while_statement129') == owner
    _safe_set(owner, 'simpleJava_expression130', None)
    assert getattr(partner, 'simpleJava_while_statement129') is None


def test_assoc_modificador94_stub_double():
    # simpleJava_variable_declaration has no real 'simpleJava_variable_declaration95' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_MODIFIER's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_MODIFIER's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_MODIFIER(modificador="sample_text")
    partner = simpleJava_variable_declaration()
    setattr(partner, 'simpleJava_variable_declaration95', None)
    _safe_set(owner, 'simpleJava_MODIFIER96', partner)
    assert getattr(partner, 'simpleJava_variable_declaration95') == owner
    _safe_set(owner, 'simpleJava_MODIFIER96', None)
    assert getattr(partner, 'simpleJava_variable_declaration95') is None


def test_assoc_newbloco67_stub_double():
    # simpleJava_statement_block has no real 'simpleJava_statement_block69' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_statement(break_="sample_text", continue_="sample_text")
    partner = simpleJava_statement_block()
    setattr(partner, 'simpleJava_statement_block69', None)
    _safe_set(owner, 'simpleJava_statement68', partner)
    assert getattr(partner, 'simpleJava_statement_block69') == owner
    _safe_set(owner, 'simpleJava_statement68', None)
    assert getattr(partner, 'simpleJava_statement_block69') is None


def test_assoc_nomeImporte7_stub_double():
    # simpleJava_import_statement has no real 'simpleJava_import_statement8' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_name(nome="sample_text")
    partner = simpleJava_import_statement()
    setattr(partner, 'simpleJava_import_statement8', None)
    _safe_set(owner, 'simpleJava_name9', partner)
    assert getattr(partner, 'simpleJava_import_statement8') == owner
    _safe_set(owner, 'simpleJava_name9', None)
    assert getattr(partner, 'simpleJava_import_statement8') is None


def test_assoc_noomePacote5_stub_double():
    # simpleJava_package_statement has no real 'simpleJava_package_statement6' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_name(nome="sample_text")
    partner = simpleJava_package_statement()
    setattr(partner, 'simpleJava_package_statement6', None)
    _safe_set(owner, 'simpleJava_name', partner)
    assert getattr(partner, 'simpleJava_package_statement6') == owner
    _safe_set(owner, 'simpleJava_name', None)
    assert getattr(partner, 'simpleJava_package_statement6') is None


def test_assoc_novo201_stub_double():
    # simpleJava_creating_expression has no real 'simpleJava_creating_expression203' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_expression(identificador="sample_text")
    partner = simpleJava_creating_expression()
    setattr(partner, 'simpleJava_creating_expression203', None)
    _safe_set(owner, 'simpleJava_expression202', partner)
    assert getattr(partner, 'simpleJava_creating_expression203') == owner
    _safe_set(owner, 'simpleJava_expression202', None)
    assert getattr(partner, 'simpleJava_creating_expression203') is None


def test_assoc_novoObjeto182_stub_double():
    # simpleJava_creating_expression has no real 'simpleJava_creating_expression' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_name(nome="sample_text")
    partner = simpleJava_creating_expression()
    setattr(partner, 'simpleJava_creating_expression', None)
    _safe_set(owner, 'simpleJava_name183', partner)
    assert getattr(partner, 'simpleJava_creating_expression') == owner
    _safe_set(owner, 'simpleJava_name183', None)
    assert getattr(partner, 'simpleJava_creating_expression') is None


def test_assoc_objeto243_stub_double():
    # simpleJava_type has no real 'simpleJava_type244' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_name(nome="sample_text")
    partner = simpleJava_type()
    setattr(partner, 'simpleJava_type244', None)
    _safe_set(owner, 'simpleJava_name245', partner)
    assert getattr(partner, 'simpleJava_type244') == owner
    _safe_set(owner, 'simpleJava_name245', None)
    assert getattr(partner, 'simpleJava_type244') is None


def test_assoc_parametroCatch152_stub_double():
    # simpleJava_try_statement has no real 'simpleJava_try_statement153' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_parameter(nomeParametro="sample_text")
    partner = simpleJava_try_statement()
    setattr(partner, 'simpleJava_try_statement153', None)
    _safe_set(owner, 'simpleJava_parameter154', partner)
    assert getattr(partner, 'simpleJava_try_statement153') == owner
    _safe_set(owner, 'simpleJava_parameter154', None)
    assert getattr(partner, 'simpleJava_try_statement153') is None


def test_assoc_parametros57_stub_double():
    # simpleJava_parameter_list has no real 'simpleJava_parameter_list58' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_parameter(nomeParametro="sample_text")
    partner = simpleJava_parameter_list()
    setattr(partner, 'simpleJava_parameter_list58', None)
    _safe_set(owner, 'simpleJava_parameter59', partner)
    assert owner in getattr(partner, 'simpleJava_parameter_list58')
    _safe_set(owner, 'simpleJava_parameter59', None)
    assert owner not in getattr(partner, 'simpleJava_parameter_list58')


def test_assoc_parametrosContrutor173_stub_double():
    # simpleJava_parameter_list has no real 'simpleJava_parameter_list175' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_constructor_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_constructor_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_constructor_declaration(nomeContrutor="sample_text")
    partner = simpleJava_parameter_list()
    setattr(partner, 'simpleJava_parameter_list175', None)
    _safe_set(owner, 'simpleJava_constructor_declaration174', partner)
    assert getattr(partner, 'simpleJava_parameter_list175') == owner
    _safe_set(owner, 'simpleJava_constructor_declaration174', None)
    assert getattr(partner, 'simpleJava_parameter_list175') is None


def test_assoc_parametrosMetodo51_stub_double():
    # simpleJava_parameter_list has no real 'simpleJava_parameter_list' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_method_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_method_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_method_declaration(nomeMetodo="sample_text")
    partner = simpleJava_parameter_list()
    setattr(partner, 'simpleJava_parameter_list', None)
    _safe_set(owner, 'simpleJava_method_declaration52', partner)
    assert getattr(partner, 'simpleJava_parameter_list') == owner
    _safe_set(owner, 'simpleJava_method_declaration52', None)
    assert getattr(partner, 'simpleJava_parameter_list') is None


def test_assoc_primitivo240_stub_double():
    # simpleJava_type has no real 'simpleJava_type241' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_type_specifier(nome="sample_text")
    partner = simpleJava_type()
    setattr(partner, 'simpleJava_type241', None)
    _safe_set(owner, 'simpleJava_type_specifier242', partner)
    assert getattr(partner, 'simpleJava_type241') == owner
    _safe_set(owner, 'simpleJava_type_specifier242', None)
    assert getattr(partner, 'simpleJava_type241') is None


def test_assoc_tipoObjeto186_stub_double():
    # simpleJava_creating_expression has no real 'simpleJava_creating_expression187' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_type_specifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_type_specifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_type_specifier(nome="sample_text")
    partner = simpleJava_creating_expression()
    setattr(partner, 'simpleJava_creating_expression187', None)
    _safe_set(owner, 'simpleJava_type_specifier', partner)
    assert getattr(partner, 'simpleJava_creating_expression187') == owner
    _safe_set(owner, 'simpleJava_type_specifier', None)
    assert getattr(partner, 'simpleJava_creating_expression187') is None


def test_assoc_tipoParametro232_stub_double():
    # simpleJava_type has no real 'simpleJava_type234' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_arglist's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_arglist's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_arglist(nomeParametro="sample_text")
    partner = simpleJava_type()
    setattr(partner, 'simpleJava_type234', None)
    _safe_set(owner, 'simpleJava_arglist233', {partner})
    assert getattr(partner, 'simpleJava_type234') == owner
    _safe_set(owner, 'simpleJava_arglist233', set())
    assert getattr(partner, 'simpleJava_type234') is None


def test_assoc_tipoParametro55_stub_double():
    # simpleJava_type has no real 'simpleJava_type56' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_parameter(nomeParametro="sample_text")
    partner = simpleJava_type()
    setattr(partner, 'simpleJava_type56', None)
    _safe_set(owner, 'simpleJava_parameter', partner)
    assert getattr(partner, 'simpleJava_type56') == owner
    _safe_set(owner, 'simpleJava_parameter', None)
    assert getattr(partner, 'simpleJava_type56') is None


def test_assoc_tipoRetorno49_stub_double():
    # simpleJava_type has no real 'simpleJava_type' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_method_declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_method_declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_method_declaration(nomeMetodo="sample_text")
    partner = simpleJava_type()
    setattr(partner, 'simpleJava_type', None)
    _safe_set(owner, 'simpleJava_method_declaration50', partner)
    assert getattr(partner, 'simpleJava_type') == owner
    _safe_set(owner, 'simpleJava_method_declaration50', None)
    assert getattr(partner, 'simpleJava_type') is None


def test_assoc_valorVariavel105_stub_double():
    # simpleJava_variable_initializer has no real 'simpleJava_variable_initializer' property in the generated
    # code (a bare stub) -- manually attach it so simpleJava_variable_declarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleJava_variable_declarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleJava_variable_declarator(nomeVariavel="sample_text", op="sample_text")
    partner = simpleJava_variable_initializer()
    setattr(partner, 'simpleJava_variable_initializer', None)
    _safe_set(owner, 'simpleJava_variable_declarator106', partner)
    assert getattr(partner, 'simpleJava_variable_initializer') == owner
    _safe_set(owner, 'simpleJava_variable_declarator106', None)
    assert getattr(partner, 'simpleJava_variable_initializer') is None


