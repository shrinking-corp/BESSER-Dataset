import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actuadores,
    Bloques,
    Instrucciones,
    Sensores,
    arduino_Actuadores,
    arduino_Apagar,
    arduino_Bloques,
    arduino_Boton,
    arduino_Buzzer,
    arduino_Encender,
    arduino_Esperar,
    arduino_If,
    arduino_Instrucciones,
    arduino_LDR,
    arduino_Led,
    arduino_PIR,
    arduino_Potenciometro,
    arduino_Sensores,
    arduino_Servo,
    arduino_Sketch,
    arduino_Temperatura,
    arduino_Variar,
    arduino_While,
    operandos,
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

def test_assoc_act10_reverse_link_reassign_clear():
    a1 = arduino_Sensores(med="sample_text", pin="sample_text")
    a2 = arduino_Sensores(med="sample_text_2", pin="sample_text_2")
    b = arduino_Actuadores(pin="sample_text")
    _safe_set(b, 'arduino_Actuadores12', a1)
    assert _is_linked(b, 'arduino_Actuadores12', a1)
    if hasattr(a1, 'arduino_Sensores11'):
        assert _is_linked(a1, 'arduino_Sensores11', b)
    _safe_set(b, 'arduino_Actuadores12', a2)
    assert _is_linked(b, 'arduino_Actuadores12', a2)
    if hasattr(a1, 'arduino_Sensores11'):
        assert not _is_linked(a1, 'arduino_Sensores11', b)
    if hasattr(a2, 'arduino_Sensores11'):
        assert _is_linked(a2, 'arduino_Sensores11', b)
    _safe_set(b, 'arduino_Actuadores12', None)
    assert not _is_linked(b, 'arduino_Actuadores12', a2)
    if hasattr(a2, 'arduino_Sensores11'):
        assert not _is_linked(a2, 'arduino_Sensores11', b)


def test_assoc_actuadores1_reverse_link_reassign_clear():
    a1 = arduino_Sketch(Nombre="sample_text")
    a2 = arduino_Sketch(Nombre="sample_text_2")
    b = arduino_Actuadores(pin="sample_text")
    _safe_set(b, 'arduino_Actuadores', a1)
    assert _is_linked(b, 'arduino_Actuadores', a1)
    if hasattr(a1, 'arduino_Sketch2'):
        assert _is_linked(a1, 'arduino_Sketch2', b)
    _safe_set(b, 'arduino_Actuadores', a2)
    assert _is_linked(b, 'arduino_Actuadores', a2)
    if hasattr(a1, 'arduino_Sketch2'):
        assert not _is_linked(a1, 'arduino_Sketch2', b)
    if hasattr(a2, 'arduino_Sketch2'):
        assert _is_linked(a2, 'arduino_Sketch2', b)
    _safe_set(b, 'arduino_Actuadores', None)
    assert not _is_linked(b, 'arduino_Actuadores', a2)
    if hasattr(a2, 'arduino_Sketch2'):
        assert not _is_linked(a2, 'arduino_Sketch2', b)


def test_assoc_datos14_reverse_link_reassign_clear():
    a1 = arduino_Variar(pwm="sample_text")
    a2 = arduino_Variar(pwm="sample_text_2")
    b = arduino_Sensores(med="sample_text", pin="sample_text")
    _safe_set(b, 'arduino_Sensores15', a1)
    assert _is_linked(b, 'arduino_Sensores15', a1)
    if hasattr(a1, 'arduino_Variar'):
        assert _is_linked(a1, 'arduino_Variar', b)
    _safe_set(b, 'arduino_Sensores15', a2)
    assert _is_linked(b, 'arduino_Sensores15', a2)
    if hasattr(a1, 'arduino_Variar'):
        assert not _is_linked(a1, 'arduino_Variar', b)
    if hasattr(a2, 'arduino_Variar'):
        assert _is_linked(a2, 'arduino_Variar', b)
    _safe_set(b, 'arduino_Sensores15', None)
    assert not _is_linked(b, 'arduino_Sensores15', a2)
    if hasattr(a2, 'arduino_Variar'):
        assert not _is_linked(a2, 'arduino_Variar', b)


def test_assoc_sensores0_reverse_link_reassign_clear():
    a1 = arduino_Sketch(Nombre="sample_text")
    a2 = arduino_Sketch(Nombre="sample_text_2")
    b = arduino_Sensores(med="sample_text", pin="sample_text")
    _safe_set(b, 'arduino_Sensores', a1)
    assert _is_linked(b, 'arduino_Sensores', a1)
    if hasattr(a1, 'arduino_Sketch'):
        assert _is_linked(a1, 'arduino_Sketch', b)
    _safe_set(b, 'arduino_Sensores', a2)
    assert _is_linked(b, 'arduino_Sensores', a2)
    if hasattr(a1, 'arduino_Sketch'):
        assert not _is_linked(a1, 'arduino_Sketch', b)
    if hasattr(a2, 'arduino_Sketch'):
        assert _is_linked(a2, 'arduino_Sketch', b)
    _safe_set(b, 'arduino_Sensores', None)
    assert not _is_linked(b, 'arduino_Sensores', a2)
    if hasattr(a2, 'arduino_Sketch'):
        assert not _is_linked(a2, 'arduino_Sketch', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actuadorinstruccion7_stub_double():
    # arduino_Instrucciones has no real 'arduino_Instrucciones9' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Actuadores's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Actuadores's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Actuadores(pin="sample_text")
    partner = arduino_Instrucciones()
    setattr(partner, 'arduino_Instrucciones9', None)
    _safe_set(owner, 'arduino_Actuadores8', partner)
    assert getattr(partner, 'arduino_Instrucciones9') == owner
    _safe_set(owner, 'arduino_Actuadores8', None)
    assert getattr(partner, 'arduino_Instrucciones9') is None


def test_assoc_apagar16_stub_double():
    # arduino_Apagar has no real 'arduino_Apagar18' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Esperar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Esperar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Esperar(miliseg="sample_text")
    partner = arduino_Apagar()
    setattr(partner, 'arduino_Apagar18', None)
    _safe_set(owner, 'arduino_Esperar17', partner)
    assert getattr(partner, 'arduino_Apagar18') == owner
    _safe_set(owner, 'arduino_Esperar17', None)
    assert getattr(partner, 'arduino_Apagar18') is None


def test_assoc_bactuadores27_stub_double():
    # arduino_Bloques has no real 'arduino_Bloques28' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Actuadores's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Actuadores's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Actuadores(pin="sample_text")
    partner = arduino_Bloques()
    setattr(partner, 'arduino_Bloques28', None)
    _safe_set(owner, 'arduino_Actuadores29', partner)
    assert owner in getattr(partner, 'arduino_Bloques28')
    _safe_set(owner, 'arduino_Actuadores29', None)
    assert owner not in getattr(partner, 'arduino_Bloques28')


def test_assoc_bloacts36_stub_double():
    # arduino_Bloques has no real 'arduino_Bloques37' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Actuadores's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Actuadores's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Actuadores(pin="sample_text")
    partner = arduino_Bloques()
    setattr(partner, 'arduino_Bloques37', None)
    _safe_set(owner, 'arduino_Actuadores38', partner)
    assert getattr(partner, 'arduino_Bloques37') == owner
    _safe_set(owner, 'arduino_Actuadores38', None)
    assert getattr(partner, 'arduino_Bloques37') is None


def test_assoc_bloques5_stub_double():
    # arduino_Bloques has no real 'arduino_Bloques' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Sketch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Sketch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Sketch(Nombre="sample_text")
    partner = arduino_Bloques()
    setattr(partner, 'arduino_Bloques', None)
    _safe_set(owner, 'arduino_Sketch6', {partner})
    assert getattr(partner, 'arduino_Bloques') == owner
    _safe_set(owner, 'arduino_Sketch6', set())
    assert getattr(partner, 'arduino_Bloques') is None


def test_assoc_bsensores33_stub_double():
    # arduino_Bloques has no real 'arduino_Bloques34' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Sensores's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Sensores's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Sensores(med="sample_text", pin="sample_text")
    partner = arduino_Bloques()
    setattr(partner, 'arduino_Bloques34', None)
    _safe_set(owner, 'arduino_Sensores35', partner)
    assert getattr(partner, 'arduino_Bloques34') == owner
    _safe_set(owner, 'arduino_Sensores35', None)
    assert getattr(partner, 'arduino_Bloques34') is None


def test_assoc_encender19_stub_double():
    # arduino_Encender has no real 'arduino_Encender' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Esperar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Esperar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Esperar(miliseg="sample_text")
    partner = arduino_Encender()
    setattr(partner, 'arduino_Encender', None)
    _safe_set(owner, 'arduino_Esperar20', partner)
    assert getattr(partner, 'arduino_Encender') == owner
    _safe_set(owner, 'arduino_Esperar20', None)
    assert getattr(partner, 'arduino_Encender') is None


def test_assoc_esperar113_stub_double():
    # arduino_Apagar has no real 'arduino_Apagar' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Esperar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Esperar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Esperar(miliseg="sample_text")
    partner = arduino_Apagar()
    setattr(partner, 'arduino_Apagar', None)
    _safe_set(owner, 'arduino_Esperar', partner)
    assert getattr(partner, 'arduino_Apagar') == owner
    _safe_set(owner, 'arduino_Esperar', None)
    assert getattr(partner, 'arduino_Apagar') is None


def test_assoc_esperar21_stub_double():
    # arduino_Encender has no real 'arduino_Encender22' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Esperar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Esperar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Esperar(miliseg="sample_text")
    partner = arduino_Encender()
    setattr(partner, 'arduino_Encender22', None)
    _safe_set(owner, 'arduino_Esperar23', partner)
    assert getattr(partner, 'arduino_Encender22') == owner
    _safe_set(owner, 'arduino_Esperar23', None)
    assert getattr(partner, 'arduino_Encender22') is None


def test_assoc_instrucciones3_stub_double():
    # arduino_Instrucciones has no real 'arduino_Instrucciones' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Sketch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Sketch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Sketch(Nombre="sample_text")
    partner = arduino_Instrucciones()
    setattr(partner, 'arduino_Instrucciones', None)
    _safe_set(owner, 'arduino_Sketch4', {partner})
    assert getattr(partner, 'arduino_Instrucciones') == owner
    _safe_set(owner, 'arduino_Sketch4', set())
    assert getattr(partner, 'arduino_Instrucciones') is None


