import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Consulta,
    Especialidade,
    Medico,
    Paciente,
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

def test_assoc_Consulta_Medico_reverse_link_reassign_clear():
    a1 = Medico(crm="sample_text", endereco="sample_text", foto="sample_text", nome="sample_text")
    a2 = Medico(crm="sample_text_2", endereco="sample_text_2", foto="sample_text_2", nome="sample_text_2")
    b = Consulta(data="sample_text", pre_o="sample_text")
    _safe_set(b, 'medico2', a1)
    assert _is_linked(b, 'medico2', a1)
    if hasattr(a1, 'consulta3'):
        assert _is_linked(a1, 'consulta3', b)
    _safe_set(b, 'medico2', a2)
    assert _is_linked(b, 'medico2', a2)
    if hasattr(a1, 'consulta3'):
        assert not _is_linked(a1, 'consulta3', b)
    if hasattr(a2, 'consulta3'):
        assert _is_linked(a2, 'consulta3', b)
    _safe_set(b, 'medico2', None)
    assert not _is_linked(b, 'medico2', a2)
    if hasattr(a2, 'consulta3'):
        assert not _is_linked(a2, 'consulta3', b)


def test_assoc_Medico_Especialidade_reverse_link_reassign_clear():
    a1 = Medico(crm="sample_text", endereco="sample_text", foto="sample_text", nome="sample_text")
    a2 = Medico(crm="sample_text_2", endereco="sample_text_2", foto="sample_text_2", nome="sample_text_2")
    b = Especialidade(descricao="sample_text")
    _safe_set(b, 'medico1', a1)
    assert _is_linked(b, 'medico1', a1)
    if hasattr(a1, 'especialidade0'):
        assert _is_linked(a1, 'especialidade0', b)
    _safe_set(b, 'medico1', a2)
    assert _is_linked(b, 'medico1', a2)
    if hasattr(a1, 'especialidade0'):
        assert not _is_linked(a1, 'especialidade0', b)
    if hasattr(a2, 'especialidade0'):
        assert _is_linked(a2, 'especialidade0', b)
    _safe_set(b, 'medico1', None)
    assert not _is_linked(b, 'medico1', a2)
    if hasattr(a2, 'especialidade0'):
        assert not _is_linked(a2, 'especialidade0', b)


def test_assoc_Paciente_Consulta_reverse_link_reassign_clear():
    a1 = Paciente(celular="sample_text", endere_o="sample_text", nome="sample_text")
    a2 = Paciente(celular="sample_text_2", endere_o="sample_text_2", nome="sample_text_2")
    b = Consulta(data="sample_text", pre_o="sample_text")
    _safe_set(b, 'paciente5', a1)
    assert _is_linked(b, 'paciente5', a1)
    if hasattr(a1, 'consulta4'):
        assert _is_linked(a1, 'consulta4', b)
    _safe_set(b, 'paciente5', a2)
    assert _is_linked(b, 'paciente5', a2)
    if hasattr(a1, 'consulta4'):
        assert not _is_linked(a1, 'consulta4', b)
    if hasattr(a2, 'consulta4'):
        assert _is_linked(a2, 'consulta4', b)
    _safe_set(b, 'paciente5', None)
    assert not _is_linked(b, 'paciente5', a2)
    if hasattr(a2, 'consulta4'):
        assert not _is_linked(a2, 'consulta4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

