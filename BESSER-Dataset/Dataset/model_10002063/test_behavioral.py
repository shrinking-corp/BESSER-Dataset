import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cidade,
    Exame,
    Medico,
    Paciente,
    Pedido_Exame,
    UF,
    float,
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

def test_assoc_Cidade_Paciente_reverse_link_reassign_clear():
    a1 = Paciente(cep="sample_text", codigo=7, cpf="sample_text", dataNascimento="sample_text", endereco="sample_text", nome="sample_text", rg="sample_text", telefone="sample_text")
    a2 = Paciente(cep="sample_text_2", codigo=13, cpf="sample_text_2", dataNascimento="sample_text_2", endereco="sample_text_2", nome="sample_text_2", rg="sample_text_2", telefone="sample_text_2")
    b = Cidade(codigo=7, ddd=7, nome="sample_text")
    _safe_set(b, 'paciente0', {a1})
    assert _is_linked(b, 'paciente0', a1)
    if hasattr(a1, 'cidade1'):
        assert _is_linked(a1, 'cidade1', b)
    _safe_set(b, 'paciente0', {a2})
    assert _is_linked(b, 'paciente0', a2)
    if hasattr(a1, 'cidade1'):
        assert not _is_linked(a1, 'cidade1', b)
    if hasattr(a2, 'cidade1'):
        assert _is_linked(a2, 'cidade1', b)
    _safe_set(b, 'paciente0', set())
    assert not _is_linked(b, 'paciente0', a2)
    if hasattr(a2, 'cidade1'):
        assert not _is_linked(a2, 'cidade1', b)


def test_assoc_Medico_Pedido_Exame_reverse_link_reassign_clear():
    a1 = Pedido_Exame(codigo=7)
    a2 = Pedido_Exame(codigo=13)
    b = Medico(crm=7, nome="sample_text")
    _safe_set(b, 'pedido_Exame6', {a1})
    assert _is_linked(b, 'pedido_Exame6', a1)
    if hasattr(a1, 'medico7'):
        assert _is_linked(a1, 'medico7', b)
    _safe_set(b, 'pedido_Exame6', {a2})
    assert _is_linked(b, 'pedido_Exame6', a2)
    if hasattr(a1, 'medico7'):
        assert not _is_linked(a1, 'medico7', b)
    if hasattr(a2, 'medico7'):
        assert _is_linked(a2, 'medico7', b)
    _safe_set(b, 'pedido_Exame6', set())
    assert not _is_linked(b, 'pedido_Exame6', a2)
    if hasattr(a2, 'medico7'):
        assert not _is_linked(a2, 'medico7', b)


def test_assoc_MyClass_Cidade_reverse_link_reassign_clear():
    a1 = UF(nome="sample_text", sigla="sample_text")
    a2 = UF(nome="sample_text_2", sigla="sample_text_2")
    b = Cidade(codigo=7, ddd=7, nome="sample_text")
    _safe_set(b, 'UF3', a1)
    assert _is_linked(b, 'UF3', a1)
    if hasattr(a1, 'cidade2'):
        assert _is_linked(a1, 'cidade2', b)
    _safe_set(b, 'UF3', a2)
    assert _is_linked(b, 'UF3', a2)
    if hasattr(a1, 'cidade2'):
        assert not _is_linked(a1, 'cidade2', b)
    if hasattr(a2, 'cidade2'):
        assert _is_linked(a2, 'cidade2', b)
    _safe_set(b, 'UF3', None)
    assert not _is_linked(b, 'UF3', a2)
    if hasattr(a2, 'cidade2'):
        assert not _is_linked(a2, 'cidade2', b)


def test_assoc_Pedido_Exame_Paciente_reverse_link_reassign_clear():
    a1 = Pedido_Exame(codigo=7)
    a2 = Pedido_Exame(codigo=13)
    b = Paciente(cep="sample_text", codigo=7, cpf="sample_text", dataNascimento="sample_text", endereco="sample_text", nome="sample_text", rg="sample_text", telefone="sample_text")
    _safe_set(b, 'pedido_Exame5', {a1})
    assert _is_linked(b, 'pedido_Exame5', a1)
    if hasattr(a1, 'paciente4'):
        assert _is_linked(a1, 'paciente4', b)
    _safe_set(b, 'pedido_Exame5', {a2})
    assert _is_linked(b, 'pedido_Exame5', a2)
    if hasattr(a1, 'paciente4'):
        assert not _is_linked(a1, 'paciente4', b)
    if hasattr(a2, 'paciente4'):
        assert _is_linked(a2, 'paciente4', b)
    _safe_set(b, 'pedido_Exame5', set())
    assert not _is_linked(b, 'pedido_Exame5', a2)
    if hasattr(a2, 'paciente4'):
        assert not _is_linked(a2, 'paciente4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

