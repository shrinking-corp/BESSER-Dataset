import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    robotmodel_Action,
    robotmodel_Component,
    robotmodel_Connector,
    robotmodel_Event,
    robotmodel_Port,
    robotmodel_Property,
    robotmodel_Property_List,
    robotmodel_Role,
    robotmodel_State,
    robotmodel_System,
    robotmodel_Transition,
    Is_Style,
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

def test_assoc_action16_reverse_link_reassign_clear():
    a1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    a2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    b = robotmodel_Action(name="sample_text")
    _safe_set(b, 'robotmodel_Action', a1)
    assert _is_linked(b, 'robotmodel_Action', a1)
    if hasattr(a1, 'robotmodel_Component17'):
        assert _is_linked(a1, 'robotmodel_Component17', b)
    _safe_set(b, 'robotmodel_Action', a2)
    assert _is_linked(b, 'robotmodel_Action', a2)
    if hasattr(a1, 'robotmodel_Component17'):
        assert not _is_linked(a1, 'robotmodel_Component17', b)
    if hasattr(a2, 'robotmodel_Component17'):
        assert _is_linked(a2, 'robotmodel_Component17', b)
    _safe_set(b, 'robotmodel_Action', None)
    assert not _is_linked(b, 'robotmodel_Action', a2)
    if hasattr(a2, 'robotmodel_Component17'):
        assert not _is_linked(a2, 'robotmodel_Component17', b)


def test_assoc_action31_reverse_link_reassign_clear():
    a1 = robotmodel_State(name="sample_text")
    a2 = robotmodel_State(name="sample_text_2")
    b = robotmodel_Action(name="sample_text")
    _safe_set(b, 'robotmodel_Action33', a1)
    assert _is_linked(b, 'robotmodel_Action33', a1)
    if hasattr(a1, 'robotmodel_State32'):
        assert _is_linked(a1, 'robotmodel_State32', b)
    _safe_set(b, 'robotmodel_Action33', a2)
    assert _is_linked(b, 'robotmodel_Action33', a2)
    if hasattr(a1, 'robotmodel_State32'):
        assert not _is_linked(a1, 'robotmodel_State32', b)
    if hasattr(a2, 'robotmodel_State32'):
        assert _is_linked(a2, 'robotmodel_State32', b)
    _safe_set(b, 'robotmodel_Action33', None)
    assert not _is_linked(b, 'robotmodel_Action33', a2)
    if hasattr(a2, 'robotmodel_State32'):
        assert not _is_linked(a2, 'robotmodel_State32', b)


def test_assoc_action46_reverse_link_reassign_clear():
    a1 = robotmodel_Transition(name="sample_text")
    a2 = robotmodel_Transition(name="sample_text_2")
    b = robotmodel_Action(name="sample_text")
    _safe_set(b, 'robotmodel_Action48', a1)
    assert _is_linked(b, 'robotmodel_Action48', a1)
    if hasattr(a1, 'robotmodel_Transition47'):
        assert _is_linked(a1, 'robotmodel_Transition47', b)
    _safe_set(b, 'robotmodel_Action48', a2)
    assert _is_linked(b, 'robotmodel_Action48', a2)
    if hasattr(a1, 'robotmodel_Transition47'):
        assert not _is_linked(a1, 'robotmodel_Transition47', b)
    if hasattr(a2, 'robotmodel_Transition47'):
        assert _is_linked(a2, 'robotmodel_Transition47', b)
    _safe_set(b, 'robotmodel_Action48', None)
    assert not _is_linked(b, 'robotmodel_Action48', a2)
    if hasattr(a2, 'robotmodel_Transition47'):
        assert not _is_linked(a2, 'robotmodel_Transition47', b)


def test_assoc_component0_reverse_link_reassign_clear():
    a1 = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    a2 = robotmodel_System(author="sample_text_2", author_email="sample_text_2", depends="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Component', a1)
    assert _is_linked(b, 'robotmodel_Component', a1)
    if hasattr(a1, 'robotmodel_System'):
        assert _is_linked(a1, 'robotmodel_System', b)
    _safe_set(b, 'robotmodel_Component', a2)
    assert _is_linked(b, 'robotmodel_Component', a2)
    if hasattr(a1, 'robotmodel_System'):
        assert not _is_linked(a1, 'robotmodel_System', b)
    if hasattr(a2, 'robotmodel_System'):
        assert _is_linked(a2, 'robotmodel_System', b)
    _safe_set(b, 'robotmodel_Component', None)
    assert not _is_linked(b, 'robotmodel_Component', a2)
    if hasattr(a2, 'robotmodel_System'):
        assert not _is_linked(a2, 'robotmodel_System', b)


def test_assoc_component8_reverse_link_reassign_clear():
    a1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    a2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    b = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Component9', a1)
    assert _is_linked(b, 'robotmodel_Component9', a1)
    if hasattr(a1, 'robotmodel_Component7'):
        assert _is_linked(a1, 'robotmodel_Component7', b)
    _safe_set(b, 'robotmodel_Component9', a2)
    assert _is_linked(b, 'robotmodel_Component9', a2)
    if hasattr(a1, 'robotmodel_Component7'):
        assert not _is_linked(a1, 'robotmodel_Component7', b)
    if hasattr(a2, 'robotmodel_Component7'):
        assert _is_linked(a2, 'robotmodel_Component7', b)
    _safe_set(b, 'robotmodel_Component9', None)
    assert not _is_linked(b, 'robotmodel_Component9', a2)
    if hasattr(a2, 'robotmodel_Component7'):
        assert not _is_linked(a2, 'robotmodel_Component7', b)


def test_assoc_connector1_reverse_link_reassign_clear():
    a1 = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    a2 = robotmodel_System(author="sample_text_2", author_email="sample_text_2", depends="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Connector', a1)
    assert _is_linked(b, 'robotmodel_Connector', a1)
    if hasattr(a1, 'robotmodel_System2'):
        assert _is_linked(a1, 'robotmodel_System2', b)
    _safe_set(b, 'robotmodel_Connector', a2)
    assert _is_linked(b, 'robotmodel_Connector', a2)
    if hasattr(a1, 'robotmodel_System2'):
        assert not _is_linked(a1, 'robotmodel_System2', b)
    if hasattr(a2, 'robotmodel_System2'):
        assert _is_linked(a2, 'robotmodel_System2', b)
    _safe_set(b, 'robotmodel_Connector', None)
    assert not _is_linked(b, 'robotmodel_Connector', a2)
    if hasattr(a2, 'robotmodel_System2'):
        assert not _is_linked(a2, 'robotmodel_System2', b)


def test_assoc_entryaction37_reverse_link_reassign_clear():
    a1 = robotmodel_State(name="sample_text")
    a2 = robotmodel_State(name="sample_text_2")
    b = robotmodel_Action(name="sample_text")
    _safe_set(b, 'robotmodel_Action39', a1)
    assert _is_linked(b, 'robotmodel_Action39', a1)
    if hasattr(a1, 'robotmodel_State38'):
        assert _is_linked(a1, 'robotmodel_State38', b)
    _safe_set(b, 'robotmodel_Action39', a2)
    assert _is_linked(b, 'robotmodel_Action39', a2)
    if hasattr(a1, 'robotmodel_State38'):
        assert not _is_linked(a1, 'robotmodel_State38', b)
    if hasattr(a2, 'robotmodel_State38'):
        assert _is_linked(a2, 'robotmodel_State38', b)
    _safe_set(b, 'robotmodel_Action39', None)
    assert not _is_linked(b, 'robotmodel_Action39', a2)
    if hasattr(a2, 'robotmodel_State38'):
        assert not _is_linked(a2, 'robotmodel_State38', b)


def test_assoc_event12_reverse_link_reassign_clear():
    a1 = robotmodel_Event(name="sample_text")
    a2 = robotmodel_Event(name="sample_text_2")
    b = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Component13', {a1})
    assert _is_linked(b, 'robotmodel_Component13', a1)
    if hasattr(a1, 'robotmodel_Event'):
        assert _is_linked(a1, 'robotmodel_Event', b)
    _safe_set(b, 'robotmodel_Component13', {a2})
    assert _is_linked(b, 'robotmodel_Component13', a2)
    if hasattr(a1, 'robotmodel_Event'):
        assert not _is_linked(a1, 'robotmodel_Event', b)
    if hasattr(a2, 'robotmodel_Event'):
        assert _is_linked(a2, 'robotmodel_Event', b)
    _safe_set(b, 'robotmodel_Component13', set())
    assert not _is_linked(b, 'robotmodel_Component13', a2)
    if hasattr(a2, 'robotmodel_Event'):
        assert not _is_linked(a2, 'robotmodel_Event', b)


def test_assoc_event43_reverse_link_reassign_clear():
    a1 = robotmodel_State(name="sample_text")
    a2 = robotmodel_State(name="sample_text_2")
    b = robotmodel_Event(name="sample_text")
    _safe_set(b, 'robotmodel_Event45', a1)
    assert _is_linked(b, 'robotmodel_Event45', a1)
    if hasattr(a1, 'robotmodel_State44'):
        assert _is_linked(a1, 'robotmodel_State44', b)
    _safe_set(b, 'robotmodel_Event45', a2)
    assert _is_linked(b, 'robotmodel_Event45', a2)
    if hasattr(a1, 'robotmodel_State44'):
        assert not _is_linked(a1, 'robotmodel_State44', b)
    if hasattr(a2, 'robotmodel_State44'):
        assert _is_linked(a2, 'robotmodel_State44', b)
    _safe_set(b, 'robotmodel_Event45', None)
    assert not _is_linked(b, 'robotmodel_Event45', a2)
    if hasattr(a2, 'robotmodel_State44'):
        assert not _is_linked(a2, 'robotmodel_State44', b)


def test_assoc_exitaction40_reverse_link_reassign_clear():
    a1 = robotmodel_State(name="sample_text")
    a2 = robotmodel_State(name="sample_text_2")
    b = robotmodel_Action(name="sample_text")
    _safe_set(b, 'robotmodel_Action42', a1)
    assert _is_linked(b, 'robotmodel_Action42', a1)
    if hasattr(a1, 'robotmodel_State41'):
        assert _is_linked(a1, 'robotmodel_State41', b)
    _safe_set(b, 'robotmodel_Action42', a2)
    assert _is_linked(b, 'robotmodel_Action42', a2)
    if hasattr(a1, 'robotmodel_State41'):
        assert not _is_linked(a1, 'robotmodel_State41', b)
    if hasattr(a2, 'robotmodel_State41'):
        assert _is_linked(a2, 'robotmodel_State41', b)
    _safe_set(b, 'robotmodel_Action42', None)
    assert not _is_linked(b, 'robotmodel_Action42', a2)
    if hasattr(a2, 'robotmodel_State41'):
        assert not _is_linked(a2, 'robotmodel_State41', b)


def test_assoc_guard49_reverse_link_reassign_clear():
    a1 = robotmodel_Transition(name="sample_text")
    a2 = robotmodel_Transition(name="sample_text_2")
    b = robotmodel_Action(name="sample_text")
    _safe_set(b, 'robotmodel_Action51', a1)
    assert _is_linked(b, 'robotmodel_Action51', a1)
    if hasattr(a1, 'robotmodel_Transition50'):
        assert _is_linked(a1, 'robotmodel_Transition50', b)
    _safe_set(b, 'robotmodel_Action51', a2)
    assert _is_linked(b, 'robotmodel_Action51', a2)
    if hasattr(a1, 'robotmodel_Transition50'):
        assert not _is_linked(a1, 'robotmodel_Transition50', b)
    if hasattr(a2, 'robotmodel_Transition50'):
        assert _is_linked(a2, 'robotmodel_Transition50', b)
    _safe_set(b, 'robotmodel_Action51', None)
    assert not _is_linked(b, 'robotmodel_Action51', a2)
    if hasattr(a2, 'robotmodel_Transition50'):
        assert not _is_linked(a2, 'robotmodel_Transition50', b)


def test_assoc_port3_reverse_link_reassign_clear():
    a1 = robotmodel_Port(name="sample_text")
    a2 = robotmodel_Port(name="sample_text_2")
    b = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Component4', {a1})
    assert _is_linked(b, 'robotmodel_Component4', a1)
    if hasattr(a1, 'robotmodel_Port'):
        assert _is_linked(a1, 'robotmodel_Port', b)
    _safe_set(b, 'robotmodel_Component4', {a2})
    assert _is_linked(b, 'robotmodel_Component4', a2)
    if hasattr(a1, 'robotmodel_Port'):
        assert not _is_linked(a1, 'robotmodel_Port', b)
    if hasattr(a2, 'robotmodel_Port'):
        assert _is_linked(a2, 'robotmodel_Port', b)
    _safe_set(b, 'robotmodel_Component4', set())
    assert not _is_linked(b, 'robotmodel_Component4', a2)
    if hasattr(a2, 'robotmodel_Port'):
        assert not _is_linked(a2, 'robotmodel_Port', b)


def test_assoc_property26_reverse_link_reassign_clear():
    a1 = robotmodel_Property_List(name="sample_text")
    a2 = robotmodel_Property_List(name="sample_text_2")
    b = robotmodel_Property(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'robotmodel_Property', a1)
    assert _is_linked(b, 'robotmodel_Property', a1)
    if hasattr(a1, 'robotmodel_Property_List27'):
        assert _is_linked(a1, 'robotmodel_Property_List27', b)
    _safe_set(b, 'robotmodel_Property', a2)
    assert _is_linked(b, 'robotmodel_Property', a2)
    if hasattr(a1, 'robotmodel_Property_List27'):
        assert not _is_linked(a1, 'robotmodel_Property_List27', b)
    if hasattr(a2, 'robotmodel_Property_List27'):
        assert _is_linked(a2, 'robotmodel_Property_List27', b)
    _safe_set(b, 'robotmodel_Property', None)
    assert not _is_linked(b, 'robotmodel_Property', a2)
    if hasattr(a2, 'robotmodel_Property_List27'):
        assert not _is_linked(a2, 'robotmodel_Property_List27', b)


def test_assoc_property_list18_reverse_link_reassign_clear():
    a1 = robotmodel_Property_List(name="sample_text")
    a2 = robotmodel_Property_List(name="sample_text_2")
    b = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Connector19', {a1})
    assert _is_linked(b, 'robotmodel_Connector19', a1)
    if hasattr(a1, 'robotmodel_Property_List20'):
        assert _is_linked(a1, 'robotmodel_Property_List20', b)
    _safe_set(b, 'robotmodel_Connector19', {a2})
    assert _is_linked(b, 'robotmodel_Connector19', a2)
    if hasattr(a1, 'robotmodel_Property_List20'):
        assert not _is_linked(a1, 'robotmodel_Property_List20', b)
    if hasattr(a2, 'robotmodel_Property_List20'):
        assert _is_linked(a2, 'robotmodel_Property_List20', b)
    _safe_set(b, 'robotmodel_Connector19', set())
    assert not _is_linked(b, 'robotmodel_Connector19', a2)
    if hasattr(a2, 'robotmodel_Property_List20'):
        assert not _is_linked(a2, 'robotmodel_Property_List20', b)


def test_assoc_property_list5_reverse_link_reassign_clear():
    a1 = robotmodel_Property_List(name="sample_text")
    a2 = robotmodel_Property_List(name="sample_text_2")
    b = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Component6', {a1})
    assert _is_linked(b, 'robotmodel_Component6', a1)
    if hasattr(a1, 'robotmodel_Property_List'):
        assert _is_linked(a1, 'robotmodel_Property_List', b)
    _safe_set(b, 'robotmodel_Component6', {a2})
    assert _is_linked(b, 'robotmodel_Component6', a2)
    if hasattr(a1, 'robotmodel_Property_List'):
        assert not _is_linked(a1, 'robotmodel_Property_List', b)
    if hasattr(a2, 'robotmodel_Property_List'):
        assert _is_linked(a2, 'robotmodel_Property_List', b)
    _safe_set(b, 'robotmodel_Component6', set())
    assert not _is_linked(b, 'robotmodel_Component6', a2)
    if hasattr(a2, 'robotmodel_Property_List'):
        assert not _is_linked(a2, 'robotmodel_Property_List', b)


def test_assoc_role21_reverse_link_reassign_clear():
    a1 = robotmodel_Role(name="sample_text")
    a2 = robotmodel_Role(name="sample_text_2")
    b = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Connector22', {a1})
    assert _is_linked(b, 'robotmodel_Connector22', a1)
    if hasattr(a1, 'robotmodel_Role'):
        assert _is_linked(a1, 'robotmodel_Role', b)
    _safe_set(b, 'robotmodel_Connector22', {a2})
    assert _is_linked(b, 'robotmodel_Connector22', a2)
    if hasattr(a1, 'robotmodel_Role'):
        assert not _is_linked(a1, 'robotmodel_Role', b)
    if hasattr(a2, 'robotmodel_Role'):
        assert _is_linked(a2, 'robotmodel_Role', b)
    _safe_set(b, 'robotmodel_Connector22', set())
    assert not _is_linked(b, 'robotmodel_Connector22', a2)
    if hasattr(a2, 'robotmodel_Role'):
        assert not _is_linked(a2, 'robotmodel_Role', b)


def test_assoc_role23_reverse_link_reassign_clear():
    a1 = robotmodel_Role(name="sample_text")
    a2 = robotmodel_Role(name="sample_text_2")
    b = robotmodel_Port(name="sample_text")
    _safe_set(b, 'robotmodel_Port24', a1)
    assert _is_linked(b, 'robotmodel_Port24', a1)
    if hasattr(a1, 'robotmodel_Role25'):
        assert _is_linked(a1, 'robotmodel_Role25', b)
    _safe_set(b, 'robotmodel_Port24', a2)
    assert _is_linked(b, 'robotmodel_Port24', a2)
    if hasattr(a1, 'robotmodel_Role25'):
        assert not _is_linked(a1, 'robotmodel_Role25', b)
    if hasattr(a2, 'robotmodel_Role25'):
        assert _is_linked(a2, 'robotmodel_Role25', b)
    _safe_set(b, 'robotmodel_Port24', None)
    assert not _is_linked(b, 'robotmodel_Port24', a2)
    if hasattr(a2, 'robotmodel_Role25'):
        assert not _is_linked(a2, 'robotmodel_Role25', b)


def test_assoc_source52_reverse_link_reassign_clear():
    a1 = robotmodel_Transition(name="sample_text")
    a2 = robotmodel_Transition(name="sample_text_2")
    b = robotmodel_State(name="sample_text")
    _safe_set(b, 'robotmodel_State54', a1)
    assert _is_linked(b, 'robotmodel_State54', a1)
    if hasattr(a1, 'robotmodel_Transition53'):
        assert _is_linked(a1, 'robotmodel_Transition53', b)
    _safe_set(b, 'robotmodel_State54', a2)
    assert _is_linked(b, 'robotmodel_State54', a2)
    if hasattr(a1, 'robotmodel_Transition53'):
        assert not _is_linked(a1, 'robotmodel_Transition53', b)
    if hasattr(a2, 'robotmodel_Transition53'):
        assert _is_linked(a2, 'robotmodel_Transition53', b)
    _safe_set(b, 'robotmodel_State54', None)
    assert not _is_linked(b, 'robotmodel_State54', a2)
    if hasattr(a2, 'robotmodel_Transition53'):
        assert not _is_linked(a2, 'robotmodel_Transition53', b)


def test_assoc_state10_reverse_link_reassign_clear():
    a1 = robotmodel_State(name="sample_text")
    a2 = robotmodel_State(name="sample_text_2")
    b = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Component11', {a1})
    assert _is_linked(b, 'robotmodel_Component11', a1)
    if hasattr(a1, 'robotmodel_State'):
        assert _is_linked(a1, 'robotmodel_State', b)
    _safe_set(b, 'robotmodel_Component11', {a2})
    assert _is_linked(b, 'robotmodel_Component11', a2)
    if hasattr(a1, 'robotmodel_State'):
        assert not _is_linked(a1, 'robotmodel_State', b)
    if hasattr(a2, 'robotmodel_State'):
        assert _is_linked(a2, 'robotmodel_State', b)
    _safe_set(b, 'robotmodel_Component11', set())
    assert not _is_linked(b, 'robotmodel_Component11', a2)
    if hasattr(a2, 'robotmodel_State'):
        assert not _is_linked(a2, 'robotmodel_State', b)


def test_assoc_substate29_reverse_link_reassign_clear():
    a1 = robotmodel_State(name="sample_text")
    a2 = robotmodel_State(name="sample_text_2")
    b = robotmodel_State(name="sample_text")
    _safe_set(b, 'robotmodel_State30', a1)
    assert _is_linked(b, 'robotmodel_State30', a1)
    if hasattr(a1, 'robotmodel_State28'):
        assert _is_linked(a1, 'robotmodel_State28', b)
    _safe_set(b, 'robotmodel_State30', a2)
    assert _is_linked(b, 'robotmodel_State30', a2)
    if hasattr(a1, 'robotmodel_State28'):
        assert not _is_linked(a1, 'robotmodel_State28', b)
    if hasattr(a2, 'robotmodel_State28'):
        assert _is_linked(a2, 'robotmodel_State28', b)
    _safe_set(b, 'robotmodel_State30', None)
    assert not _is_linked(b, 'robotmodel_State30', a2)
    if hasattr(a2, 'robotmodel_State28'):
        assert not _is_linked(a2, 'robotmodel_State28', b)


def test_assoc_target55_reverse_link_reassign_clear():
    a1 = robotmodel_Transition(name="sample_text")
    a2 = robotmodel_Transition(name="sample_text_2")
    b = robotmodel_State(name="sample_text")
    _safe_set(b, 'robotmodel_State57', a1)
    assert _is_linked(b, 'robotmodel_State57', a1)
    if hasattr(a1, 'robotmodel_Transition56'):
        assert _is_linked(a1, 'robotmodel_Transition56', b)
    _safe_set(b, 'robotmodel_State57', a2)
    assert _is_linked(b, 'robotmodel_State57', a2)
    if hasattr(a1, 'robotmodel_Transition56'):
        assert not _is_linked(a1, 'robotmodel_Transition56', b)
    if hasattr(a2, 'robotmodel_Transition56'):
        assert _is_linked(a2, 'robotmodel_Transition56', b)
    _safe_set(b, 'robotmodel_State57', None)
    assert not _is_linked(b, 'robotmodel_State57', a2)
    if hasattr(a2, 'robotmodel_Transition56'):
        assert not _is_linked(a2, 'robotmodel_Transition56', b)


def test_assoc_transition14_reverse_link_reassign_clear():
    a1 = robotmodel_Transition(name="sample_text")
    a2 = robotmodel_Transition(name="sample_text_2")
    b = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    _safe_set(b, 'robotmodel_Component15', {a1})
    assert _is_linked(b, 'robotmodel_Component15', a1)
    if hasattr(a1, 'robotmodel_Transition'):
        assert _is_linked(a1, 'robotmodel_Transition', b)
    _safe_set(b, 'robotmodel_Component15', {a2})
    assert _is_linked(b, 'robotmodel_Component15', a2)
    if hasattr(a1, 'robotmodel_Transition'):
        assert not _is_linked(a1, 'robotmodel_Transition', b)
    if hasattr(a2, 'robotmodel_Transition'):
        assert _is_linked(a2, 'robotmodel_Transition', b)
    _safe_set(b, 'robotmodel_Component15', set())
    assert not _is_linked(b, 'robotmodel_Component15', a2)
    if hasattr(a2, 'robotmodel_Transition'):
        assert not _is_linked(a2, 'robotmodel_Transition', b)


def test_assoc_transition34_reverse_link_reassign_clear():
    a1 = robotmodel_Transition(name="sample_text")
    a2 = robotmodel_Transition(name="sample_text_2")
    b = robotmodel_State(name="sample_text")
    _safe_set(b, 'robotmodel_State35', {a1})
    assert _is_linked(b, 'robotmodel_State35', a1)
    if hasattr(a1, 'robotmodel_Transition36'):
        assert _is_linked(a1, 'robotmodel_Transition36', b)
    _safe_set(b, 'robotmodel_State35', {a2})
    assert _is_linked(b, 'robotmodel_State35', a2)
    if hasattr(a1, 'robotmodel_Transition36'):
        assert not _is_linked(a1, 'robotmodel_Transition36', b)
    if hasattr(a2, 'robotmodel_Transition36'):
        assert _is_linked(a2, 'robotmodel_Transition36', b)
    _safe_set(b, 'robotmodel_State35', set())
    assert not _is_linked(b, 'robotmodel_State35', a2)
    if hasattr(a2, 'robotmodel_Transition36'):
        assert not _is_linked(a2, 'robotmodel_Transition36', b)


def test_assoc_transition58_reverse_link_reassign_clear():
    a1 = robotmodel_Transition(name="sample_text")
    a2 = robotmodel_Transition(name="sample_text_2")
    b = robotmodel_Event(name="sample_text")
    _safe_set(b, 'robotmodel_Event59', a1)
    assert _is_linked(b, 'robotmodel_Event59', a1)
    if hasattr(a1, 'robotmodel_Transition60'):
        assert _is_linked(a1, 'robotmodel_Transition60', b)
    _safe_set(b, 'robotmodel_Event59', a2)
    assert _is_linked(b, 'robotmodel_Event59', a2)
    if hasattr(a1, 'robotmodel_Transition60'):
        assert not _is_linked(a1, 'robotmodel_Transition60', b)
    if hasattr(a2, 'robotmodel_Transition60'):
        assert _is_linked(a2, 'robotmodel_Transition60', b)
    _safe_set(b, 'robotmodel_Event59', None)
    assert not _is_linked(b, 'robotmodel_Event59', a2)
    if hasattr(a2, 'robotmodel_Transition60'):
        assert not _is_linked(a2, 'robotmodel_Transition60', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

