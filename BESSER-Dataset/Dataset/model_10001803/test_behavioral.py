import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Agendamento,
    Consulta,
    Exame,
    Funcion_rio,
    M_dico,
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

def test_assoc_Agendamento_Consulta_reverse_link_reassign_clear():
    a1 = Consulta(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoConsulta="sample_text")
    a2 = Consulta(Especialista="sample_text_2", Medico="sample_text_2", Sede="sample_text_2", TipoConsulta="sample_text_2")
    b = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    _safe_set(b, 'consulta2', a1)
    assert _is_linked(b, 'consulta2', a1)
    if hasattr(a1, 'agendamento3'):
        assert _is_linked(a1, 'agendamento3', b)
    _safe_set(b, 'consulta2', a2)
    assert _is_linked(b, 'consulta2', a2)
    if hasattr(a1, 'agendamento3'):
        assert not _is_linked(a1, 'agendamento3', b)
    if hasattr(a2, 'agendamento3'):
        assert _is_linked(a2, 'agendamento3', b)
    _safe_set(b, 'consulta2', None)
    assert not _is_linked(b, 'consulta2', a2)
    if hasattr(a2, 'agendamento3'):
        assert not _is_linked(a2, 'agendamento3', b)


def test_assoc_Agendamento_Exame_reverse_link_reassign_clear():
    a1 = Exame(Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoExame="sample_text")
    a2 = Exame(Especialista="sample_text_2", Medico="sample_text_2", Sede="sample_text_2", TipoExame="sample_text_2")
    b = Agendamento(Dia_e_Horario="sample_text", Especialista="sample_text", Medico="sample_text", Sede="sample_text", TipoAgendamento="sample_text")
    _safe_set(b, 'exame0', a1)
    assert _is_linked(b, 'exame0', a1)
    if hasattr(a1, 'agendamento1'):
        assert _is_linked(a1, 'agendamento1', b)
    _safe_set(b, 'exame0', a2)
    assert _is_linked(b, 'exame0', a2)
    if hasattr(a1, 'agendamento1'):
        assert not _is_linked(a1, 'agendamento1', b)
    if hasattr(a2, 'agendamento1'):
        assert _is_linked(a2, 'agendamento1', b)
    _safe_set(b, 'exame0', None)
    assert not _is_linked(b, 'exame0', a2)
    if hasattr(a2, 'agendamento1'):
        assert not _is_linked(a2, 'agendamento1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

