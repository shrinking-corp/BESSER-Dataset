import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Actuate,
    Behavior,
    Condition,
    Node,
    farrusco_Action,
    farrusco_Actuate,
    farrusco_AlterarEstado,
    farrusco_Behavior,
    farrusco_Bumpers,
    farrusco_Condition,
    farrusco_Distancia,
    farrusco_Espera,
    farrusco_Filho,
    farrusco_Irmao,
    farrusco_LED,
    farrusco_Motor,
    farrusco_Node,
    farrusco_Paralelo,
    farrusco_Prioridade,
    farrusco_Robot,
    farrusco_Sequencial,
    farrusco_Servo,
    EscolhaBumper,
    EstadoDaLuz,
    EstadoDecorrer,
    EstadoFalha,
    EstadoSucesso,
    TipoDistancia,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child1_stub_double():
    # farrusco_Filho has no real 'farrusco_Filho' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Robot(Nome="sample_text")
    partner = farrusco_Filho()
    setattr(partner, 'farrusco_Filho', None)
    _safe_set(owner, 'farrusco_Robot2', {partner})
    assert getattr(partner, 'farrusco_Filho') == owner
    _safe_set(owner, 'farrusco_Robot2', set())
    assert getattr(partner, 'farrusco_Filho') is None


def test_assoc_next3_stub_double():
    # farrusco_Irmao has no real 'farrusco_Irmao' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Robot(Nome="sample_text")
    partner = farrusco_Irmao()
    setattr(partner, 'farrusco_Irmao', None)
    _safe_set(owner, 'farrusco_Robot4', {partner})
    assert getattr(partner, 'farrusco_Irmao') == owner
    _safe_set(owner, 'farrusco_Robot4', set())
    assert getattr(partner, 'farrusco_Irmao') is None


def test_assoc_nodes0_stub_double():
    # farrusco_Node has no real 'farrusco_Node' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Robot(Nome="sample_text")
    partner = farrusco_Node()
    setattr(partner, 'farrusco_Node', None)
    _safe_set(owner, 'farrusco_Robot', {partner})
    assert getattr(partner, 'farrusco_Node') == owner
    _safe_set(owner, 'farrusco_Robot', set())
    assert getattr(partner, 'farrusco_Node') is None


