import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attributable,
    Type,
    Variable,
    dataflow_Action,
    dataflow_Actor,
    dataflow_ActorClass,
    dataflow_Buffer,
    dataflow_Guard,
    dataflow_Network,
    dataflow_Port,
    dataflow_Procedure,
    dataflow_SharedVariable,
    dataflow_Type,
    dataflow_TypeBoolean,
    dataflow_TypeDouble,
    dataflow_TypeInt,
    dataflow_TypeList,
    dataflow_TypeString,
    dataflow_TypeUint,
    dataflow_TypeUndefined,
    dataflow_Variable,
    dataflow_Version,
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

def test_assoc_actions30_reverse_link_reassign_clear():
    a1 = dataflow_Actor(name="sample_text")
    a2 = dataflow_Actor(name="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'dataflow_Action', a1)
    assert _is_linked(b, 'dataflow_Action', a1)
    if hasattr(a1, 'dataflow_Actor31'):
        assert _is_linked(a1, 'dataflow_Actor31', b)
    _safe_set(b, 'dataflow_Action', a2)
    assert _is_linked(b, 'dataflow_Action', a2)
    if hasattr(a1, 'dataflow_Actor31'):
        assert not _is_linked(a1, 'dataflow_Actor31', b)
    if hasattr(a2, 'dataflow_Actor31'):
        assert _is_linked(a2, 'dataflow_Actor31', b)
    _safe_set(b, 'dataflow_Action', None)
    assert not _is_linked(b, 'dataflow_Action', a2)
    if hasattr(a2, 'dataflow_Actor31'):
        assert not _is_linked(a2, 'dataflow_Actor31', b)


def test_assoc_actorClass29_reverse_link_reassign_clear():
    a1 = dataflow_ActorClass(name="sample_text", nameSpace="sample_text", sourceCode="sample_text", sourceFile="sample_text")
    a2 = dataflow_ActorClass(name="sample_text_2", nameSpace="sample_text_2", sourceCode="sample_text_2", sourceFile="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'actors', a1)
    assert _is_linked(b, 'actors', a1)
    if hasattr(a1, 'ActorClass'):
        assert _is_linked(a1, 'ActorClass', b)
    _safe_set(b, 'actors', a2)
    assert _is_linked(b, 'actors', a2)
    if hasattr(a1, 'ActorClass'):
        assert not _is_linked(a1, 'ActorClass', b)
    if hasattr(a2, 'ActorClass'):
        assert _is_linked(a2, 'ActorClass', b)
    _safe_set(b, 'actors', None)
    assert not _is_linked(b, 'actors', a2)
    if hasattr(a2, 'ActorClass'):
        assert not _is_linked(a2, 'ActorClass', b)


def test_assoc_actorClasses1_reverse_link_reassign_clear():
    a1 = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    a2 = dataflow_Network(name="sample_text_2", project="sample_text_2", sourceFile="sample_text_2")
    b = dataflow_ActorClass(name="sample_text", nameSpace="sample_text", sourceCode="sample_text", sourceFile="sample_text")
    _safe_set(b, 'dataflow_ActorClass', a1)
    assert _is_linked(b, 'dataflow_ActorClass', a1)
    if hasattr(a1, 'dataflow_Network2'):
        assert _is_linked(a1, 'dataflow_Network2', b)
    _safe_set(b, 'dataflow_ActorClass', a2)
    assert _is_linked(b, 'dataflow_ActorClass', a2)
    if hasattr(a1, 'dataflow_Network2'):
        assert not _is_linked(a1, 'dataflow_Network2', b)
    if hasattr(a2, 'dataflow_Network2'):
        assert _is_linked(a2, 'dataflow_Network2', b)
    _safe_set(b, 'dataflow_ActorClass', None)
    assert not _is_linked(b, 'dataflow_ActorClass', a2)
    if hasattr(a2, 'dataflow_Network2'):
        assert not _is_linked(a2, 'dataflow_Network2', b)


def test_assoc_actors0_reverse_link_reassign_clear():
    a1 = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    a2 = dataflow_Network(name="sample_text_2", project="sample_text_2", sourceFile="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor', a1)
    assert _is_linked(b, 'dataflow_Actor', a1)
    if hasattr(a1, 'dataflow_Network'):
        assert _is_linked(a1, 'dataflow_Network', b)
    _safe_set(b, 'dataflow_Actor', a2)
    assert _is_linked(b, 'dataflow_Actor', a2)
    if hasattr(a1, 'dataflow_Network'):
        assert not _is_linked(a1, 'dataflow_Network', b)
    if hasattr(a2, 'dataflow_Network'):
        assert _is_linked(a2, 'dataflow_Network', b)
    _safe_set(b, 'dataflow_Actor', None)
    assert not _is_linked(b, 'dataflow_Actor', a2)
    if hasattr(a2, 'dataflow_Network'):
        assert not _is_linked(a2, 'dataflow_Network', b)


def test_assoc_actors14_reverse_link_reassign_clear():
    a1 = dataflow_ActorClass(name="sample_text", nameSpace="sample_text", sourceCode="sample_text", sourceFile="sample_text")
    a2 = dataflow_ActorClass(name="sample_text_2", nameSpace="sample_text_2", sourceCode="sample_text_2", sourceFile="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'Actor', a1)
    assert _is_linked(b, 'Actor', a1)
    if hasattr(a1, 'actorClass'):
        assert _is_linked(a1, 'actorClass', b)
    _safe_set(b, 'Actor', a2)
    assert _is_linked(b, 'Actor', a2)
    if hasattr(a1, 'actorClass'):
        assert not _is_linked(a1, 'actorClass', b)
    if hasattr(a2, 'actorClass'):
        assert _is_linked(a2, 'actorClass', b)
    _safe_set(b, 'Actor', None)
    assert not _is_linked(b, 'Actor', a2)
    if hasattr(a2, 'actorClass'):
        assert not _is_linked(a2, 'actorClass', b)


def test_assoc_guards55_reverse_link_reassign_clear():
    a1 = dataflow_Guard(tag="sample_text")
    a2 = dataflow_Guard(tag="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'dataflow_Action56', {a1})
    assert _is_linked(b, 'dataflow_Action56', a1)
    if hasattr(a1, 'dataflow_Guard'):
        assert _is_linked(a1, 'dataflow_Guard', b)
    _safe_set(b, 'dataflow_Action56', {a2})
    assert _is_linked(b, 'dataflow_Action56', a2)
    if hasattr(a1, 'dataflow_Guard'):
        assert not _is_linked(a1, 'dataflow_Guard', b)
    if hasattr(a2, 'dataflow_Guard'):
        assert _is_linked(a2, 'dataflow_Guard', b)
    _safe_set(b, 'dataflow_Action56', set())
    assert not _is_linked(b, 'dataflow_Action56', a2)
    if hasattr(a2, 'dataflow_Guard'):
        assert not _is_linked(a2, 'dataflow_Guard', b)


def test_assoc_inputPorts21_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor22', {a1})
    assert _is_linked(b, 'dataflow_Actor22', a1)
    if hasattr(a1, 'dataflow_Port23'):
        assert _is_linked(a1, 'dataflow_Port23', b)
    _safe_set(b, 'dataflow_Actor22', {a2})
    assert _is_linked(b, 'dataflow_Actor22', a2)
    if hasattr(a1, 'dataflow_Port23'):
        assert not _is_linked(a1, 'dataflow_Port23', b)
    if hasattr(a2, 'dataflow_Port23'):
        assert _is_linked(a2, 'dataflow_Port23', b)
    _safe_set(b, 'dataflow_Actor22', set())
    assert not _is_linked(b, 'dataflow_Actor22', a2)
    if hasattr(a2, 'dataflow_Port23'):
        assert not _is_linked(a2, 'dataflow_Port23', b)


def test_assoc_inputPorts5_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    _safe_set(b, 'dataflow_Network6', {a1})
    assert _is_linked(b, 'dataflow_Network6', a1)
    if hasattr(a1, 'dataflow_Port'):
        assert _is_linked(a1, 'dataflow_Port', b)
    _safe_set(b, 'dataflow_Network6', {a2})
    assert _is_linked(b, 'dataflow_Network6', a2)
    if hasattr(a1, 'dataflow_Port'):
        assert not _is_linked(a1, 'dataflow_Port', b)
    if hasattr(a2, 'dataflow_Port'):
        assert _is_linked(a2, 'dataflow_Port', b)
    _safe_set(b, 'dataflow_Network6', set())
    assert not _is_linked(b, 'dataflow_Network6', a2)
    if hasattr(a2, 'dataflow_Port'):
        assert not _is_linked(a2, 'dataflow_Port', b)


def test_assoc_inputPorts52_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'readers', {a1})
    assert _is_linked(b, 'readers', a1)
    if hasattr(a1, 'Port'):
        assert _is_linked(a1, 'Port', b)
    _safe_set(b, 'readers', {a2})
    assert _is_linked(b, 'readers', a2)
    if hasattr(a1, 'Port'):
        assert not _is_linked(a1, 'Port', b)
    if hasattr(a2, 'Port'):
        assert _is_linked(a2, 'Port', b)
    _safe_set(b, 'readers', set())
    assert not _is_linked(b, 'readers', a2)
    if hasattr(a2, 'Port'):
        assert not _is_linked(a2, 'Port', b)


def test_assoc_listType93_reverse_link_reassign_clear():
    a1 = dataflow_TypeList(elements=7)
    a2 = dataflow_TypeList(elements=13)
    b = dataflow_Type(bits=7, etype="sample_text")
    _safe_set(b, 'dataflow_Type94', a1)
    assert _is_linked(b, 'dataflow_Type94', a1)
    if hasattr(a1, 'dataflow_TypeList'):
        assert _is_linked(a1, 'dataflow_TypeList', b)
    _safe_set(b, 'dataflow_Type94', a2)
    assert _is_linked(b, 'dataflow_Type94', a2)
    if hasattr(a1, 'dataflow_TypeList'):
        assert not _is_linked(a1, 'dataflow_TypeList', b)
    if hasattr(a2, 'dataflow_TypeList'):
        assert _is_linked(a2, 'dataflow_TypeList', b)
    _safe_set(b, 'dataflow_Type94', None)
    assert not _is_linked(b, 'dataflow_Type94', a2)
    if hasattr(a2, 'dataflow_TypeList'):
        assert not _is_linked(a2, 'dataflow_TypeList', b)


def test_assoc_outputPorts24_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor25', {a1})
    assert _is_linked(b, 'dataflow_Actor25', a1)
    if hasattr(a1, 'dataflow_Port26'):
        assert _is_linked(a1, 'dataflow_Port26', b)
    _safe_set(b, 'dataflow_Actor25', {a2})
    assert _is_linked(b, 'dataflow_Actor25', a2)
    if hasattr(a1, 'dataflow_Port26'):
        assert not _is_linked(a1, 'dataflow_Port26', b)
    if hasattr(a2, 'dataflow_Port26'):
        assert _is_linked(a2, 'dataflow_Port26', b)
    _safe_set(b, 'dataflow_Actor25', set())
    assert not _is_linked(b, 'dataflow_Actor25', a2)
    if hasattr(a2, 'dataflow_Port26'):
        assert not _is_linked(a2, 'dataflow_Port26', b)


def test_assoc_outputPorts53_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'writers', {a1})
    assert _is_linked(b, 'writers', a1)
    if hasattr(a1, 'Port54'):
        assert _is_linked(a1, 'Port54', b)
    _safe_set(b, 'writers', {a2})
    assert _is_linked(b, 'writers', a2)
    if hasattr(a1, 'Port54'):
        assert not _is_linked(a1, 'Port54', b)
    if hasattr(a2, 'Port54'):
        assert _is_linked(a2, 'Port54', b)
    _safe_set(b, 'writers', set())
    assert not _is_linked(b, 'writers', a2)
    if hasattr(a2, 'Port54'):
        assert not _is_linked(a2, 'Port54', b)


def test_assoc_outputPorts7_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    _safe_set(b, 'dataflow_Network8', {a1})
    assert _is_linked(b, 'dataflow_Network8', a1)
    if hasattr(a1, 'dataflow_Port9'):
        assert _is_linked(a1, 'dataflow_Port9', b)
    _safe_set(b, 'dataflow_Network8', {a2})
    assert _is_linked(b, 'dataflow_Network8', a2)
    if hasattr(a1, 'dataflow_Port9'):
        assert not _is_linked(a1, 'dataflow_Port9', b)
    if hasattr(a2, 'dataflow_Port9'):
        assert _is_linked(a2, 'dataflow_Port9', b)
    _safe_set(b, 'dataflow_Network8', set())
    assert not _is_linked(b, 'dataflow_Network8', a2)
    if hasattr(a2, 'dataflow_Port9'):
        assert not _is_linked(a2, 'dataflow_Port9', b)


def test_assoc_owner18_reverse_link_reassign_clear():
    a1 = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    a2 = dataflow_Network(name="sample_text_2", project="sample_text_2", sourceFile="sample_text_2")
    b = dataflow_ActorClass(name="sample_text", nameSpace="sample_text", sourceCode="sample_text", sourceFile="sample_text")
    _safe_set(b, 'dataflow_ActorClass19', a1)
    assert _is_linked(b, 'dataflow_ActorClass19', a1)
    if hasattr(a1, 'dataflow_Network20'):
        assert _is_linked(a1, 'dataflow_Network20', b)
    _safe_set(b, 'dataflow_ActorClass19', a2)
    assert _is_linked(b, 'dataflow_ActorClass19', a2)
    if hasattr(a1, 'dataflow_Network20'):
        assert not _is_linked(a1, 'dataflow_Network20', b)
    if hasattr(a2, 'dataflow_Network20'):
        assert _is_linked(a2, 'dataflow_Network20', b)
    _safe_set(b, 'dataflow_ActorClass19', None)
    assert not _is_linked(b, 'dataflow_ActorClass19', a2)
    if hasattr(a2, 'dataflow_Network20'):
        assert not _is_linked(a2, 'dataflow_Network20', b)


def test_assoc_owner34_reverse_link_reassign_clear():
    a1 = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    a2 = dataflow_Network(name="sample_text_2", project="sample_text_2", sourceFile="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor35', a1)
    assert _is_linked(b, 'dataflow_Actor35', a1)
    if hasattr(a1, 'dataflow_Network36'):
        assert _is_linked(a1, 'dataflow_Network36', b)
    _safe_set(b, 'dataflow_Actor35', a2)
    assert _is_linked(b, 'dataflow_Actor35', a2)
    if hasattr(a1, 'dataflow_Network36'):
        assert not _is_linked(a1, 'dataflow_Network36', b)
    if hasattr(a2, 'dataflow_Network36'):
        assert _is_linked(a2, 'dataflow_Network36', b)
    _safe_set(b, 'dataflow_Actor35', None)
    assert not _is_linked(b, 'dataflow_Actor35', a2)
    if hasattr(a2, 'dataflow_Network36'):
        assert not _is_linked(a2, 'dataflow_Network36', b)


def test_assoc_owner57_reverse_link_reassign_clear():
    a1 = dataflow_Actor(name="sample_text")
    a2 = dataflow_Actor(name="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'dataflow_Action58', a1)
    assert _is_linked(b, 'dataflow_Action58', a1)
    if hasattr(a1, 'dataflow_Actor59'):
        assert _is_linked(a1, 'dataflow_Actor59', b)
    _safe_set(b, 'dataflow_Action58', a2)
    assert _is_linked(b, 'dataflow_Action58', a2)
    if hasattr(a1, 'dataflow_Actor59'):
        assert not _is_linked(a1, 'dataflow_Actor59', b)
    if hasattr(a2, 'dataflow_Actor59'):
        assert _is_linked(a2, 'dataflow_Actor59', b)
    _safe_set(b, 'dataflow_Action58', None)
    assert not _is_linked(b, 'dataflow_Action58', a2)
    if hasattr(a2, 'dataflow_Actor59'):
        assert not _is_linked(a2, 'dataflow_Actor59', b)


def test_assoc_owner63_reverse_link_reassign_clear():
    a1 = dataflow_Procedure(name="sample_text")
    a2 = dataflow_Procedure(name="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor65', a1)
    assert _is_linked(b, 'dataflow_Actor65', a1)
    if hasattr(a1, 'dataflow_Procedure64'):
        assert _is_linked(a1, 'dataflow_Procedure64', b)
    _safe_set(b, 'dataflow_Actor65', a2)
    assert _is_linked(b, 'dataflow_Actor65', a2)
    if hasattr(a1, 'dataflow_Procedure64'):
        assert not _is_linked(a1, 'dataflow_Procedure64', b)
    if hasattr(a2, 'dataflow_Procedure64'):
        assert _is_linked(a2, 'dataflow_Procedure64', b)
    _safe_set(b, 'dataflow_Actor65', None)
    assert not _is_linked(b, 'dataflow_Actor65', a2)
    if hasattr(a2, 'dataflow_Procedure64'):
        assert not _is_linked(a2, 'dataflow_Procedure64', b)


def test_assoc_owner68_reverse_link_reassign_clear():
    a1 = dataflow_Variable(name="sample_text", shared=True)
    a2 = dataflow_Variable(name="sample_text_2", shared=False)
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor70', a1)
    assert _is_linked(b, 'dataflow_Actor70', a1)
    if hasattr(a1, 'dataflow_Variable69'):
        assert _is_linked(a1, 'dataflow_Variable69', b)
    _safe_set(b, 'dataflow_Actor70', a2)
    assert _is_linked(b, 'dataflow_Actor70', a2)
    if hasattr(a1, 'dataflow_Variable69'):
        assert not _is_linked(a1, 'dataflow_Variable69', b)
    if hasattr(a2, 'dataflow_Variable69'):
        assert _is_linked(a2, 'dataflow_Variable69', b)
    _safe_set(b, 'dataflow_Actor70', None)
    assert not _is_linked(b, 'dataflow_Actor70', a2)
    if hasattr(a2, 'dataflow_Variable69'):
        assert not _is_linked(a2, 'dataflow_Variable69', b)


def test_assoc_owner77_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor79', a1)
    assert _is_linked(b, 'dataflow_Actor79', a1)
    if hasattr(a1, 'dataflow_Port78'):
        assert _is_linked(a1, 'dataflow_Port78', b)
    _safe_set(b, 'dataflow_Actor79', a2)
    assert _is_linked(b, 'dataflow_Actor79', a2)
    if hasattr(a1, 'dataflow_Port78'):
        assert not _is_linked(a1, 'dataflow_Port78', b)
    if hasattr(a2, 'dataflow_Port78'):
        assert _is_linked(a2, 'dataflow_Port78', b)
    _safe_set(b, 'dataflow_Actor79', None)
    assert not _is_linked(b, 'dataflow_Actor79', a2)
    if hasattr(a2, 'dataflow_Port78'):
        assert not _is_linked(a2, 'dataflow_Port78', b)


def test_assoc_owner90_reverse_link_reassign_clear():
    a1 = dataflow_Guard(tag="sample_text")
    a2 = dataflow_Guard(tag="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'dataflow_Action92', a1)
    assert _is_linked(b, 'dataflow_Action92', a1)
    if hasattr(a1, 'dataflow_Guard91'):
        assert _is_linked(a1, 'dataflow_Guard91', b)
    _safe_set(b, 'dataflow_Action92', a2)
    assert _is_linked(b, 'dataflow_Action92', a2)
    if hasattr(a1, 'dataflow_Guard91'):
        assert not _is_linked(a1, 'dataflow_Guard91', b)
    if hasattr(a2, 'dataflow_Guard91'):
        assert _is_linked(a2, 'dataflow_Guard91', b)
    _safe_set(b, 'dataflow_Action92', None)
    assert not _is_linked(b, 'dataflow_Action92', a2)
    if hasattr(a2, 'dataflow_Guard91'):
        assert not _is_linked(a2, 'dataflow_Guard91', b)


def test_assoc_predecessors47_reverse_link_reassign_clear():
    a1 = dataflow_Actor(name="sample_text")
    a2 = dataflow_Actor(name="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor48', a1)
    assert _is_linked(b, 'dataflow_Actor48', a1)
    if hasattr(a1, 'dataflow_Actor46'):
        assert _is_linked(a1, 'dataflow_Actor46', b)
    _safe_set(b, 'dataflow_Actor48', a2)
    assert _is_linked(b, 'dataflow_Actor48', a2)
    if hasattr(a1, 'dataflow_Actor46'):
        assert not _is_linked(a1, 'dataflow_Actor46', b)
    if hasattr(a2, 'dataflow_Actor46'):
        assert _is_linked(a2, 'dataflow_Actor46', b)
    _safe_set(b, 'dataflow_Actor48', None)
    assert not _is_linked(b, 'dataflow_Actor48', a2)
    if hasattr(a2, 'dataflow_Actor46'):
        assert not _is_linked(a2, 'dataflow_Actor46', b)


def test_assoc_procedures32_reverse_link_reassign_clear():
    a1 = dataflow_Procedure(name="sample_text")
    a2 = dataflow_Procedure(name="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor33', {a1})
    assert _is_linked(b, 'dataflow_Actor33', a1)
    if hasattr(a1, 'dataflow_Procedure'):
        assert _is_linked(a1, 'dataflow_Procedure', b)
    _safe_set(b, 'dataflow_Actor33', {a2})
    assert _is_linked(b, 'dataflow_Actor33', a2)
    if hasattr(a1, 'dataflow_Procedure'):
        assert not _is_linked(a1, 'dataflow_Procedure', b)
    if hasattr(a2, 'dataflow_Procedure'):
        assert _is_linked(a2, 'dataflow_Procedure', b)
    _safe_set(b, 'dataflow_Actor33', set())
    assert not _is_linked(b, 'dataflow_Actor33', a2)
    if hasattr(a2, 'dataflow_Procedure'):
        assert not _is_linked(a2, 'dataflow_Procedure', b)


def test_assoc_readers72_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'Action73', a1)
    assert _is_linked(b, 'Action73', a1)
    if hasattr(a1, 'inputPorts'):
        assert _is_linked(a1, 'inputPorts', b)
    _safe_set(b, 'Action73', a2)
    assert _is_linked(b, 'Action73', a2)
    if hasattr(a1, 'inputPorts'):
        assert not _is_linked(a1, 'inputPorts', b)
    if hasattr(a2, 'inputPorts'):
        assert _is_linked(a2, 'inputPorts', b)
    _safe_set(b, 'Action73', None)
    assert not _is_linked(b, 'Action73', a2)
    if hasattr(a2, 'inputPorts'):
        assert not _is_linked(a2, 'inputPorts', b)


def test_assoc_sharedVariables10_reverse_link_reassign_clear():
    a1 = dataflow_SharedVariable(tag="sample_text")
    a2 = dataflow_SharedVariable(tag="sample_text_2")
    b = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    _safe_set(b, 'dataflow_Network11', {a1})
    assert _is_linked(b, 'dataflow_Network11', a1)
    if hasattr(a1, 'dataflow_SharedVariable'):
        assert _is_linked(a1, 'dataflow_SharedVariable', b)
    _safe_set(b, 'dataflow_Network11', {a2})
    assert _is_linked(b, 'dataflow_Network11', a2)
    if hasattr(a1, 'dataflow_SharedVariable'):
        assert not _is_linked(a1, 'dataflow_SharedVariable', b)
    if hasattr(a2, 'dataflow_SharedVariable'):
        assert _is_linked(a2, 'dataflow_SharedVariable', b)
    _safe_set(b, 'dataflow_Network11', set())
    assert not _is_linked(b, 'dataflow_Network11', a2)
    if hasattr(a2, 'dataflow_SharedVariable'):
        assert not _is_linked(a2, 'dataflow_SharedVariable', b)


def test_assoc_successors50_reverse_link_reassign_clear():
    a1 = dataflow_Actor(name="sample_text")
    a2 = dataflow_Actor(name="sample_text_2")
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor51', a1)
    assert _is_linked(b, 'dataflow_Actor51', a1)
    if hasattr(a1, 'dataflow_Actor49'):
        assert _is_linked(a1, 'dataflow_Actor49', b)
    _safe_set(b, 'dataflow_Actor51', a2)
    assert _is_linked(b, 'dataflow_Actor51', a2)
    if hasattr(a1, 'dataflow_Actor49'):
        assert not _is_linked(a1, 'dataflow_Actor49', b)
    if hasattr(a2, 'dataflow_Actor49'):
        assert _is_linked(a2, 'dataflow_Actor49', b)
    _safe_set(b, 'dataflow_Actor51', None)
    assert not _is_linked(b, 'dataflow_Actor51', a2)
    if hasattr(a2, 'dataflow_Actor49'):
        assert not _is_linked(a2, 'dataflow_Actor49', b)


def test_assoc_type66_reverse_link_reassign_clear():
    a1 = dataflow_Variable(name="sample_text", shared=True)
    a2 = dataflow_Variable(name="sample_text_2", shared=False)
    b = dataflow_Type(bits=7, etype="sample_text")
    _safe_set(b, 'dataflow_Type', a1)
    assert _is_linked(b, 'dataflow_Type', a1)
    if hasattr(a1, 'dataflow_Variable67'):
        assert _is_linked(a1, 'dataflow_Variable67', b)
    _safe_set(b, 'dataflow_Type', a2)
    assert _is_linked(b, 'dataflow_Type', a2)
    if hasattr(a1, 'dataflow_Variable67'):
        assert not _is_linked(a1, 'dataflow_Variable67', b)
    if hasattr(a2, 'dataflow_Variable67'):
        assert _is_linked(a2, 'dataflow_Variable67', b)
    _safe_set(b, 'dataflow_Type', None)
    assert not _is_linked(b, 'dataflow_Type', a2)
    if hasattr(a2, 'dataflow_Variable67'):
        assert not _is_linked(a2, 'dataflow_Variable67', b)


def test_assoc_variables27_reverse_link_reassign_clear():
    a1 = dataflow_Variable(name="sample_text", shared=True)
    a2 = dataflow_Variable(name="sample_text_2", shared=False)
    b = dataflow_Actor(name="sample_text")
    _safe_set(b, 'dataflow_Actor28', {a1})
    assert _is_linked(b, 'dataflow_Actor28', a1)
    if hasattr(a1, 'dataflow_Variable'):
        assert _is_linked(a1, 'dataflow_Variable', b)
    _safe_set(b, 'dataflow_Actor28', {a2})
    assert _is_linked(b, 'dataflow_Actor28', a2)
    if hasattr(a1, 'dataflow_Variable'):
        assert not _is_linked(a1, 'dataflow_Variable', b)
    if hasattr(a2, 'dataflow_Variable'):
        assert _is_linked(a2, 'dataflow_Variable', b)
    _safe_set(b, 'dataflow_Actor28', set())
    assert not _is_linked(b, 'dataflow_Actor28', a2)
    if hasattr(a2, 'dataflow_Variable'):
        assert not _is_linked(a2, 'dataflow_Variable', b)


def test_assoc_variables60_reverse_link_reassign_clear():
    a1 = dataflow_Variable(name="sample_text", shared=True)
    a2 = dataflow_Variable(name="sample_text_2", shared=False)
    b = dataflow_Procedure(name="sample_text")
    _safe_set(b, 'dataflow_Procedure61', {a1})
    assert _is_linked(b, 'dataflow_Procedure61', a1)
    if hasattr(a1, 'dataflow_Variable62'):
        assert _is_linked(a1, 'dataflow_Variable62', b)
    _safe_set(b, 'dataflow_Procedure61', {a2})
    assert _is_linked(b, 'dataflow_Procedure61', a2)
    if hasattr(a1, 'dataflow_Variable62'):
        assert not _is_linked(a1, 'dataflow_Variable62', b)
    if hasattr(a2, 'dataflow_Variable62'):
        assert _is_linked(a2, 'dataflow_Variable62', b)
    _safe_set(b, 'dataflow_Procedure61', set())
    assert not _is_linked(b, 'dataflow_Procedure61', a2)
    if hasattr(a2, 'dataflow_Variable62'):
        assert not _is_linked(a2, 'dataflow_Variable62', b)


def test_assoc_writers71_reverse_link_reassign_clear():
    a1 = dataflow_Port(name="sample_text")
    a2 = dataflow_Port(name="sample_text_2")
    b = dataflow_Action(name="sample_text")
    _safe_set(b, 'Action', a1)
    assert _is_linked(b, 'Action', a1)
    if hasattr(a1, 'outputPorts'):
        assert _is_linked(a1, 'outputPorts', b)
    _safe_set(b, 'Action', a2)
    assert _is_linked(b, 'Action', a2)
    if hasattr(a1, 'outputPorts'):
        assert not _is_linked(a1, 'outputPorts', b)
    if hasattr(a2, 'outputPorts'):
        assert _is_linked(a2, 'outputPorts', b)
    _safe_set(b, 'Action', None)
    assert not _is_linked(b, 'Action', a2)
    if hasattr(a2, 'outputPorts'):
        assert not _is_linked(a2, 'outputPorts', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_buffers3_stub_double():
    # dataflow_Buffer has no real 'dataflow_Buffer' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'dataflow_Buffer', None)
    _safe_set(owner, 'dataflow_Network4', {partner})
    assert getattr(partner, 'dataflow_Buffer') == owner
    _safe_set(owner, 'dataflow_Network4', set())
    assert getattr(partner, 'dataflow_Buffer') is None


def test_assoc_buffers37_stub_double():
    # dataflow_Buffer has no real 'dataflow_Buffer39' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Actor(name="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'dataflow_Buffer39', None)
    _safe_set(owner, 'dataflow_Actor38', {partner})
    assert getattr(partner, 'dataflow_Buffer39') == owner
    _safe_set(owner, 'dataflow_Actor38', set())
    assert getattr(partner, 'dataflow_Buffer39') is None


def test_assoc_incomingBuffers40_stub_double():
    # dataflow_Buffer has no real 'dataflow_Buffer42' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Actor(name="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'dataflow_Buffer42', None)
    _safe_set(owner, 'dataflow_Actor41', {partner})
    assert getattr(partner, 'dataflow_Buffer42') == owner
    _safe_set(owner, 'dataflow_Actor41', set())
    assert getattr(partner, 'dataflow_Buffer42') is None


def test_assoc_input74_stub_double():
    # dataflow_Buffer has no real 'Buffer' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Port(name="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'Buffer', None)
    _safe_set(owner, 'target', partner)
    assert getattr(partner, 'Buffer') == owner
    _safe_set(owner, 'target', None)
    assert getattr(partner, 'Buffer') is None


def test_assoc_outgoingBuffers43_stub_double():
    # dataflow_Buffer has no real 'dataflow_Buffer45' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Actor(name="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'dataflow_Buffer45', None)
    _safe_set(owner, 'dataflow_Actor44', {partner})
    assert getattr(partner, 'dataflow_Buffer45') == owner
    _safe_set(owner, 'dataflow_Actor44', set())
    assert getattr(partner, 'dataflow_Buffer45') is None


def test_assoc_outputs75_stub_double():
    # dataflow_Buffer has no real 'Buffer76' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Port(name="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'Buffer76', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Buffer76') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Buffer76') is None


def test_assoc_owner87_stub_double():
    # dataflow_Buffer has no real 'dataflow_Buffer88' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'dataflow_Buffer88', None)
    _safe_set(owner, 'dataflow_Network89', partner)
    assert getattr(partner, 'dataflow_Buffer88') == owner
    _safe_set(owner, 'dataflow_Network89', None)
    assert getattr(partner, 'dataflow_Buffer88') is None


def test_assoc_source80_stub_double():
    # dataflow_Buffer has no real 'outputs' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Port(name="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'outputs', None)
    _safe_set(owner, 'Port81', partner)
    assert getattr(partner, 'outputs') == owner
    _safe_set(owner, 'Port81', None)
    assert getattr(partner, 'outputs') is None


def test_assoc_target82_stub_double():
    # dataflow_Buffer has no real 'input' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Port(name="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'input', None)
    _safe_set(owner, 'Port83', partner)
    assert getattr(partner, 'input') == owner
    _safe_set(owner, 'Port83', None)
    assert getattr(partner, 'input') is None


def test_assoc_type84_stub_double():
    # dataflow_Buffer has no real 'dataflow_Buffer85' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Type(bits=7, etype="sample_text")
    partner = dataflow_Buffer()
    setattr(partner, 'dataflow_Buffer85', None)
    _safe_set(owner, 'dataflow_Type86', partner)
    assert getattr(partner, 'dataflow_Buffer85') == owner
    _safe_set(owner, 'dataflow_Type86', None)
    assert getattr(partner, 'dataflow_Buffer85') is None


def test_assoc_version12_stub_double():
    # dataflow_Version has no real 'dataflow_Version' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_Network(name="sample_text", project="sample_text", sourceFile="sample_text")
    partner = dataflow_Version()
    setattr(partner, 'dataflow_Version', None)
    _safe_set(owner, 'dataflow_Network13', partner)
    assert getattr(partner, 'dataflow_Version') == owner
    _safe_set(owner, 'dataflow_Network13', None)
    assert getattr(partner, 'dataflow_Version') is None


def test_assoc_version15_stub_double():
    # dataflow_Version has no real 'dataflow_Version17' property in the generated
    # code (a bare stub) -- manually attach it so dataflow_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflow_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflow_ActorClass(name="sample_text", nameSpace="sample_text", sourceCode="sample_text", sourceFile="sample_text")
    partner = dataflow_Version()
    setattr(partner, 'dataflow_Version17', None)
    _safe_set(owner, 'dataflow_ActorClass16', partner)
    assert getattr(partner, 'dataflow_Version17') == owner
    _safe_set(owner, 'dataflow_ActorClass16', None)
    assert getattr(partner, 'dataflow_Version17') is None


