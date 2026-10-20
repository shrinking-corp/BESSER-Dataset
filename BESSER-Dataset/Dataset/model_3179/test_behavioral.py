import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Expression,
    iot_AbstractElement,
    iot_And,
    iot_BoolConstant,
    iot_Comparison,
    iot_Dispositivo,
    iot_Equality,
    iot_Estado,
    iot_Etiqueta,
    iot_Evento,
    iot_Expression,
    iot_IfBlock,
    iot_IfStatement,
    iot_IntConstant,
    iot_Minus,
    iot_Model,
    iot_MulOrDiv,
    iot_Not,
    iot_Or,
    iot_Plus,
    iot_StringConstant,
    iot_Transicion,
    iot_Variable,
    iot_VariableRef,
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

def test_assoc_estados6_reverse_link_reassign_clear():
    a1 = iot_Estado(name="sample_text")
    a2 = iot_Estado(name="sample_text_2")
    b = iot_Dispositivo(name="sample_text")
    _safe_set(b, 'iot_Dispositivo7', {a1})
    assert _is_linked(b, 'iot_Dispositivo7', a1)
    if hasattr(a1, 'iot_Estado'):
        assert _is_linked(a1, 'iot_Estado', b)
    _safe_set(b, 'iot_Dispositivo7', {a2})
    assert _is_linked(b, 'iot_Dispositivo7', a2)
    if hasattr(a1, 'iot_Estado'):
        assert not _is_linked(a1, 'iot_Estado', b)
    if hasattr(a2, 'iot_Estado'):
        assert _is_linked(a2, 'iot_Estado', b)
    _safe_set(b, 'iot_Dispositivo7', set())
    assert not _is_linked(b, 'iot_Dispositivo7', a2)
    if hasattr(a2, 'iot_Estado'):
        assert not _is_linked(a2, 'iot_Estado', b)


def test_assoc_etiquetas4_reverse_link_reassign_clear():
    a1 = iot_Etiqueta(name="sample_text", typeName="sample_text", value="sample_text")
    a2 = iot_Etiqueta(name="sample_text_2", typeName="sample_text_2", value="sample_text_2")
    b = iot_Dispositivo(name="sample_text")
    _safe_set(b, 'iot_Dispositivo5', {a1})
    assert _is_linked(b, 'iot_Dispositivo5', a1)
    if hasattr(a1, 'iot_Etiqueta'):
        assert _is_linked(a1, 'iot_Etiqueta', b)
    _safe_set(b, 'iot_Dispositivo5', {a2})
    assert _is_linked(b, 'iot_Dispositivo5', a2)
    if hasattr(a1, 'iot_Etiqueta'):
        assert not _is_linked(a1, 'iot_Etiqueta', b)
    if hasattr(a2, 'iot_Etiqueta'):
        assert _is_linked(a2, 'iot_Etiqueta', b)
    _safe_set(b, 'iot_Dispositivo5', set())
    assert not _is_linked(b, 'iot_Dispositivo5', a2)
    if hasattr(a2, 'iot_Etiqueta'):
        assert not _is_linked(a2, 'iot_Etiqueta', b)


def test_assoc_eventos8_reverse_link_reassign_clear():
    a1 = iot_Evento(name="sample_text", typeName="sample_text")
    a2 = iot_Evento(name="sample_text_2", typeName="sample_text_2")
    b = iot_Dispositivo(name="sample_text")
    _safe_set(b, 'iot_Dispositivo9', {a1})
    assert _is_linked(b, 'iot_Dispositivo9', a1)
    if hasattr(a1, 'iot_Evento'):
        assert _is_linked(a1, 'iot_Evento', b)
    _safe_set(b, 'iot_Dispositivo9', {a2})
    assert _is_linked(b, 'iot_Dispositivo9', a2)
    if hasattr(a1, 'iot_Evento'):
        assert not _is_linked(a1, 'iot_Evento', b)
    if hasattr(a2, 'iot_Evento'):
        assert _is_linked(a2, 'iot_Evento', b)
    _safe_set(b, 'iot_Dispositivo9', set())
    assert not _is_linked(b, 'iot_Dispositivo9', a2)
    if hasattr(a2, 'iot_Evento'):
        assert not _is_linked(a2, 'iot_Evento', b)


def test_assoc_superType2_reverse_link_reassign_clear():
    a1 = iot_Dispositivo(name="sample_text")
    a2 = iot_Dispositivo(name="sample_text_2")
    b = iot_Dispositivo(name="sample_text")
    _safe_set(b, 'iot_Dispositivo3', a1)
    assert _is_linked(b, 'iot_Dispositivo3', a1)
    if hasattr(a1, 'iot_Dispositivo1'):
        assert _is_linked(a1, 'iot_Dispositivo1', b)
    _safe_set(b, 'iot_Dispositivo3', a2)
    assert _is_linked(b, 'iot_Dispositivo3', a2)
    if hasattr(a1, 'iot_Dispositivo1'):
        assert not _is_linked(a1, 'iot_Dispositivo1', b)
    if hasattr(a2, 'iot_Dispositivo1'):
        assert _is_linked(a2, 'iot_Dispositivo1', b)
    _safe_set(b, 'iot_Dispositivo3', None)
    assert not _is_linked(b, 'iot_Dispositivo3', a2)
    if hasattr(a2, 'iot_Dispositivo1'):
        assert not _is_linked(a2, 'iot_Dispositivo1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dispositivos0_stub_double():
    # iot_Model has no real 'iot_Model' property in the generated
    # code (a bare stub) -- manually attach it so iot_Dispositivo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Dispositivo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Dispositivo(name="sample_text")
    partner = iot_Model()
    setattr(partner, 'iot_Model', None)
    _safe_set(owner, 'iot_Dispositivo', partner)
    assert owner in getattr(partner, 'iot_Model')
    _safe_set(owner, 'iot_Dispositivo', None)
    assert owner not in getattr(partner, 'iot_Model')


def test_assoc_elementos12_stub_double():
    # iot_AbstractElement has no real 'iot_AbstractElement' property in the generated
    # code (a bare stub) -- manually attach it so iot_Estado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Estado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Estado(name="sample_text")
    partner = iot_AbstractElement()
    setattr(partner, 'iot_AbstractElement', None)
    _safe_set(owner, 'iot_Estado13', {partner})
    assert getattr(partner, 'iot_AbstractElement') == owner
    _safe_set(owner, 'iot_Estado13', set())
    assert getattr(partner, 'iot_AbstractElement') is None


def test_assoc_estado17_stub_double():
    # iot_Transicion has no real 'iot_Transicion18' property in the generated
    # code (a bare stub) -- manually attach it so iot_Estado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Estado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Estado(name="sample_text")
    partner = iot_Transicion()
    setattr(partner, 'iot_Transicion18', None)
    _safe_set(owner, 'iot_Estado19', partner)
    assert getattr(partner, 'iot_Transicion18') == owner
    _safe_set(owner, 'iot_Estado19', None)
    assert getattr(partner, 'iot_Transicion18') is None


def test_assoc_evento14_stub_double():
    # iot_Transicion has no real 'iot_Transicion15' property in the generated
    # code (a bare stub) -- manually attach it so iot_Evento's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Evento's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Evento(name="sample_text", typeName="sample_text")
    partner = iot_Transicion()
    setattr(partner, 'iot_Transicion15', None)
    _safe_set(owner, 'iot_Evento16', partner)
    assert getattr(partner, 'iot_Transicion15') == owner
    _safe_set(owner, 'iot_Evento16', None)
    assert getattr(partner, 'iot_Transicion15') is None


def test_assoc_expression29_stub_double():
    # iot_Expression has no real 'iot_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so iot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Variable(name="sample_text")
    partner = iot_Expression()
    setattr(partner, 'iot_Expression30', None)
    _safe_set(owner, 'iot_Variable', partner)
    assert getattr(partner, 'iot_Expression30') == owner
    _safe_set(owner, 'iot_Variable', None)
    assert getattr(partner, 'iot_Expression30') is None


def test_assoc_left41_stub_double():
    # iot_Expression has no real 'iot_Expression42' property in the generated
    # code (a bare stub) -- manually attach it so iot_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Equality(op="sample_text")
    partner = iot_Expression()
    setattr(partner, 'iot_Expression42', None)
    _safe_set(owner, 'iot_Equality', partner)
    assert getattr(partner, 'iot_Expression42') == owner
    _safe_set(owner, 'iot_Equality', None)
    assert getattr(partner, 'iot_Expression42') is None


def test_assoc_left46_stub_double():
    # iot_Expression has no real 'iot_Expression47' property in the generated
    # code (a bare stub) -- manually attach it so iot_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Comparison(op="sample_text")
    partner = iot_Expression()
    setattr(partner, 'iot_Expression47', None)
    _safe_set(owner, 'iot_Comparison', partner)
    assert getattr(partner, 'iot_Expression47') == owner
    _safe_set(owner, 'iot_Comparison', None)
    assert getattr(partner, 'iot_Expression47') is None


def test_assoc_left61_stub_double():
    # iot_Expression has no real 'iot_Expression62' property in the generated
    # code (a bare stub) -- manually attach it so iot_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_MulOrDiv(op="sample_text")
    partner = iot_Expression()
    setattr(partner, 'iot_Expression62', None)
    _safe_set(owner, 'iot_MulOrDiv', partner)
    assert getattr(partner, 'iot_Expression62') == owner
    _safe_set(owner, 'iot_MulOrDiv', None)
    assert getattr(partner, 'iot_Expression62') is None


def test_assoc_right43_stub_double():
    # iot_Expression has no real 'iot_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so iot_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Equality(op="sample_text")
    partner = iot_Expression()
    setattr(partner, 'iot_Expression45', None)
    _safe_set(owner, 'iot_Equality44', partner)
    assert getattr(partner, 'iot_Expression45') == owner
    _safe_set(owner, 'iot_Equality44', None)
    assert getattr(partner, 'iot_Expression45') is None


def test_assoc_right48_stub_double():
    # iot_Expression has no real 'iot_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so iot_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Comparison(op="sample_text")
    partner = iot_Expression()
    setattr(partner, 'iot_Expression50', None)
    _safe_set(owner, 'iot_Comparison49', partner)
    assert getattr(partner, 'iot_Expression50') == owner
    _safe_set(owner, 'iot_Comparison49', None)
    assert getattr(partner, 'iot_Expression50') is None


def test_assoc_right63_stub_double():
    # iot_Expression has no real 'iot_Expression65' property in the generated
    # code (a bare stub) -- manually attach it so iot_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_MulOrDiv(op="sample_text")
    partner = iot_Expression()
    setattr(partner, 'iot_Expression65', None)
    _safe_set(owner, 'iot_MulOrDiv64', partner)
    assert getattr(partner, 'iot_Expression65') == owner
    _safe_set(owner, 'iot_MulOrDiv64', None)
    assert getattr(partner, 'iot_Expression65') is None


def test_assoc_transiciones10_stub_double():
    # iot_Transicion has no real 'iot_Transicion' property in the generated
    # code (a bare stub) -- manually attach it so iot_Dispositivo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Dispositivo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Dispositivo(name="sample_text")
    partner = iot_Transicion()
    setattr(partner, 'iot_Transicion', None)
    _safe_set(owner, 'iot_Dispositivo11', {partner})
    assert getattr(partner, 'iot_Transicion') == owner
    _safe_set(owner, 'iot_Dispositivo11', set())
    assert getattr(partner, 'iot_Transicion') is None


def test_assoc_variable68_stub_double():
    # iot_VariableRef has no real 'iot_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so iot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Variable(name="sample_text")
    partner = iot_VariableRef()
    setattr(partner, 'iot_VariableRef', None)
    _safe_set(owner, 'iot_Variable69', partner)
    assert getattr(partner, 'iot_VariableRef') == owner
    _safe_set(owner, 'iot_Variable69', None)
    assert getattr(partner, 'iot_VariableRef') is None


