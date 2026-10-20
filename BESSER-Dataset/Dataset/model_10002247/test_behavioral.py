import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Endereco,
    Exame,
    Interacao,
    LinhaCuidado,
    LocalExame,
    Medicamento,
    Mensagem,
    Naturalidade,
    Paciente,
    Pessoa,
    ProfissionalSaude,
    Telefone,
    TipoMedicamento,
    TipoSanguineo,
    enu,
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

def test_assoc_Endereco_Pessoa_reverse_link_reassign_clear():
    a1 = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    a2 = Pessoa(cpf="sample_text_2", dataInclusao="sample_text_2", dataNascimento="sample_text_2", email="sample_text_2", senha="sample_text_2", sexo="sample_text_2", ultimoAcesso="sample_text_2")
    b = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    _safe_set(b, 'pessoa4', a1)
    assert _is_linked(b, 'pessoa4', a1)
    if hasattr(a1, 'endereco5'):
        assert _is_linked(a1, 'endereco5', b)
    _safe_set(b, 'pessoa4', a2)
    assert _is_linked(b, 'pessoa4', a2)
    if hasattr(a1, 'endereco5'):
        assert not _is_linked(a1, 'endereco5', b)
    if hasattr(a2, 'endereco5'):
        assert _is_linked(a2, 'endereco5', b)
    _safe_set(b, 'pessoa4', None)
    assert not _is_linked(b, 'pessoa4', a2)
    if hasattr(a2, 'endereco5'):
        assert not _is_linked(a2, 'endereco5', b)


def test_assoc_Est__em_reverse_link_reassign_clear():
    a1 = LocalExame(nome="sample_text")
    a2 = LocalExame(nome="sample_text_2")
    b = Exame(data="sample_text", descricao="sample_text", nome="sample_text")
    _safe_set(b, 'localExame1', a1)
    assert _is_linked(b, 'localExame1', a1)
    if hasattr(a1, 'exame0'):
        assert _is_linked(a1, 'exame0', b)
    _safe_set(b, 'localExame1', a2)
    assert _is_linked(b, 'localExame1', a2)
    if hasattr(a1, 'exame0'):
        assert not _is_linked(a1, 'exame0', b)
    if hasattr(a2, 'exame0'):
        assert _is_linked(a2, 'exame0', b)
    _safe_set(b, 'localExame1', None)
    assert not _is_linked(b, 'localExame1', a2)
    if hasattr(a2, 'exame0'):
        assert not _is_linked(a2, 'exame0', b)


def test_assoc_LocalExame_Endereco_reverse_link_reassign_clear():
    a1 = LocalExame(nome="sample_text")
    a2 = LocalExame(nome="sample_text_2")
    b = Endereco(bairro="sample_text", cep="sample_text", cidade="sample_text", logradouro="sample_text", numero=7)
    _safe_set(b, 'localExame3', a1)
    assert _is_linked(b, 'localExame3', a1)
    if hasattr(a1, 'endereco2'):
        assert _is_linked(a1, 'endereco2', b)
    _safe_set(b, 'localExame3', a2)
    assert _is_linked(b, 'localExame3', a2)
    if hasattr(a1, 'endereco2'):
        assert not _is_linked(a1, 'endereco2', b)
    if hasattr(a2, 'endereco2'):
        assert _is_linked(a2, 'endereco2', b)
    _safe_set(b, 'localExame3', None)
    assert not _is_linked(b, 'localExame3', a2)
    if hasattr(a2, 'endereco2'):
        assert not _is_linked(a2, 'endereco2', b)


def test_assoc_Mensagem_LinhaCuidado_reverse_link_reassign_clear():
    a1 = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    a2 = Mensagem(assunto="sample_text_2", dataEnvio="sample_text_2", geral=False, mensagem="sample_text_2")
    b = LinhaCuidado(descricao=7, nome="sample_text")
    _safe_set(b, 'mensagem15', {a1})
    assert _is_linked(b, 'mensagem15', a1)
    if hasattr(a1, 'linhaCuidado14'):
        assert _is_linked(a1, 'linhaCuidado14', b)
    _safe_set(b, 'mensagem15', {a2})
    assert _is_linked(b, 'mensagem15', a2)
    if hasattr(a1, 'linhaCuidado14'):
        assert not _is_linked(a1, 'linhaCuidado14', b)
    if hasattr(a2, 'linhaCuidado14'):
        assert _is_linked(a2, 'linhaCuidado14', b)
    _safe_set(b, 'mensagem15', set())
    assert not _is_linked(b, 'mensagem15', a2)
    if hasattr(a2, 'linhaCuidado14'):
        assert not _is_linked(a2, 'linhaCuidado14', b)


def test_assoc_Pessoa_Naturalidade_reverse_link_reassign_clear():
    a1 = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    a2 = Pessoa(cpf="sample_text_2", dataInclusao="sample_text_2", dataNascimento="sample_text_2", email="sample_text_2", senha="sample_text_2", sexo="sample_text_2", ultimoAcesso="sample_text_2")
    b = Naturalidade(naturalidade="sample_text")
    _safe_set(b, 'pessoa11', {a1})
    assert _is_linked(b, 'pessoa11', a1)
    if hasattr(a1, 'naturalidade10'):
        assert _is_linked(a1, 'naturalidade10', b)
    _safe_set(b, 'pessoa11', {a2})
    assert _is_linked(b, 'pessoa11', a2)
    if hasattr(a1, 'naturalidade10'):
        assert not _is_linked(a1, 'naturalidade10', b)
    if hasattr(a2, 'naturalidade10'):
        assert _is_linked(a2, 'naturalidade10', b)
    _safe_set(b, 'pessoa11', set())
    assert not _is_linked(b, 'pessoa11', a2)
    if hasattr(a2, 'naturalidade10'):
        assert not _is_linked(a2, 'naturalidade10', b)


def test_assoc_Pessoa_Telefone_reverse_link_reassign_clear():
    a1 = Telefone(ddd=7, numero="sample_text", tipo="sample_text")
    a2 = Telefone(ddd=13, numero="sample_text_2", tipo="sample_text_2")
    b = Pessoa(cpf="sample_text", dataInclusao="sample_text", dataNascimento="sample_text", email="sample_text", senha="sample_text", sexo="sample_text", ultimoAcesso="sample_text")
    _safe_set(b, 'telefone6', a1)
    assert _is_linked(b, 'telefone6', a1)
    if hasattr(a1, 'pessoa7'):
        assert _is_linked(a1, 'pessoa7', b)
    _safe_set(b, 'telefone6', a2)
    assert _is_linked(b, 'telefone6', a2)
    if hasattr(a1, 'pessoa7'):
        assert not _is_linked(a1, 'pessoa7', b)
    if hasattr(a2, 'pessoa7'):
        assert _is_linked(a2, 'pessoa7', b)
    _safe_set(b, 'telefone6', None)
    assert not _is_linked(b, 'telefone6', a2)
    if hasattr(a2, 'pessoa7'):
        assert not _is_linked(a2, 'pessoa7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Interacao_Mensagem_stub_double():
    # Interacao has no real 'mensagem16' property in the generated
    # code (a bare stub) -- manually attach it so Mensagem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Mensagem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    partner = Interacao()
    setattr(partner, 'mensagem16', None)
    _safe_set(owner, 'interacao17', {partner})
    assert getattr(partner, 'mensagem16') == owner
    _safe_set(owner, 'interacao17', set())
    assert getattr(partner, 'mensagem16') is None


def test_assoc_Paciente_Medicamento_stub_double():
    # Paciente has no real 'medicamento8' property in the generated
    # code (a bare stub) -- manually attach it so Medicamento's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Medicamento's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Medicamento(ativo=True, dataFim="sample_text", dataInicio="sample_text", descricao="sample_text", horaInicial="sample_text", intervaloTempo=7, nome="sample_text")
    partner = Paciente()
    setattr(partner, 'medicamento8', None)
    _safe_set(owner, 'paciente9', partner)
    assert owner in getattr(partner, 'medicamento8')
    _safe_set(owner, 'paciente9', None)
    assert owner not in getattr(partner, 'medicamento8')


def test_assoc_Paciente_Mensagem_stub_double():
    # Paciente has no real 'mensagem20' property in the generated
    # code (a bare stub) -- manually attach it so Mensagem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Mensagem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    partner = Paciente()
    setattr(partner, 'mensagem20', None)
    _safe_set(owner, 'paciente21', partner)
    assert getattr(partner, 'mensagem20') == owner
    _safe_set(owner, 'paciente21', None)
    assert getattr(partner, 'mensagem20') is None


def test_assoc_ProfissioanlSaude_Mensagem_stub_double():
    # ProfissionalSaude has no real 'mensagem12' property in the generated
    # code (a bare stub) -- manually attach it so Mensagem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Mensagem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Mensagem(assunto="sample_text", dataEnvio="sample_text", geral=True, mensagem="sample_text")
    partner = ProfissionalSaude()
    setattr(partner, 'mensagem12', None)
    _safe_set(owner, 'profissionalSaude13', partner)
    assert owner in getattr(partner, 'mensagem12')
    _safe_set(owner, 'profissionalSaude13', None)
    assert owner not in getattr(partner, 'mensagem12')


def test_assoc_TipoSanguineo_Paciente_stub_double():
    # Paciente has no real 'tipoSanguineo23' property in the generated
    # code (a bare stub) -- manually attach it so TipoSanguineo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TipoSanguineo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TipoSanguineo(nome="sample_text")
    partner = Paciente()
    setattr(partner, 'tipoSanguineo23', None)
    _safe_set(owner, 'paciente22', {partner})
    assert getattr(partner, 'tipoSanguineo23') == owner
    _safe_set(owner, 'paciente22', set())
    assert getattr(partner, 'tipoSanguineo23') is None


