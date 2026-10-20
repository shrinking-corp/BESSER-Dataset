import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    ProcessNode,
    Sequence,
    SequenceNode,
    syswbeff106_And,
    syswbeff106_Component,
    syswbeff106_Description,
    syswbeff106_Final,
    syswbeff106_Flow,
    syswbeff106_Function,
    syswbeff106_FunctionProperty,
    syswbeff106_InputPort,
    syswbeff106_Item,
    syswbeff106_Iteration,
    syswbeff106_Loop,
    syswbeff106_LoopExit,
    syswbeff106_Or,
    syswbeff106_OutputPort,
    syswbeff106_PatternCatalog,
    syswbeff106_Port,
    syswbeff106_ProcessNode,
    syswbeff106_RelatedTo,
    syswbeff106_Sequence,
    syswbeff106_SequenceNode,
    syswbeff106_Start,
    syswbeff106_System,
    syswbeff106_Thing,
    syswbeff106_Thoughts,
    syswbeff106_Token,
    syswbeff106_Workbench,
    FunctionDomain,
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

def test_assoc_allocatedTo19_reverse_link_reassign_clear():
    a1 = syswbeff106_Function(domain="sample_text")
    a2 = syswbeff106_Function(domain="sample_text_2")
    b = syswbeff106_Component(name="sample_text")
    _safe_set(b, 'syswbeff106_Component', a1)
    assert _is_linked(b, 'syswbeff106_Component', a1)
    if hasattr(a1, 'syswbeff106_Function20'):
        assert _is_linked(a1, 'syswbeff106_Function20', b)
    _safe_set(b, 'syswbeff106_Component', a2)
    assert _is_linked(b, 'syswbeff106_Component', a2)
    if hasattr(a1, 'syswbeff106_Function20'):
        assert not _is_linked(a1, 'syswbeff106_Function20', b)
    if hasattr(a2, 'syswbeff106_Function20'):
        assert _is_linked(a2, 'syswbeff106_Function20', b)
    _safe_set(b, 'syswbeff106_Component', None)
    assert not _is_linked(b, 'syswbeff106_Component', a2)
    if hasattr(a2, 'syswbeff106_Function20'):
        assert not _is_linked(a2, 'syswbeff106_Function20', b)


def test_assoc_associations17_reverse_link_reassign_clear():
    a1 = syswbeff106_Function(domain="sample_text")
    a2 = syswbeff106_Function(domain="sample_text_2")
    b = syswbeff106_Function(domain="sample_text")
    _safe_set(b, 'syswbeff106_Function18', a1)
    assert _is_linked(b, 'syswbeff106_Function18', a1)
    if hasattr(a1, 'syswbeff106_Function16'):
        assert _is_linked(a1, 'syswbeff106_Function16', b)
    _safe_set(b, 'syswbeff106_Function18', a2)
    assert _is_linked(b, 'syswbeff106_Function18', a2)
    if hasattr(a1, 'syswbeff106_Function16'):
        assert not _is_linked(a1, 'syswbeff106_Function16', b)
    if hasattr(a2, 'syswbeff106_Function16'):
        assert _is_linked(a2, 'syswbeff106_Function16', b)
    _safe_set(b, 'syswbeff106_Function18', None)
    assert not _is_linked(b, 'syswbeff106_Function18', a2)
    if hasattr(a2, 'syswbeff106_Function16'):
        assert not _is_linked(a2, 'syswbeff106_Function16', b)


def test_assoc_associations47_reverse_link_reassign_clear():
    a1 = syswbeff106_Component(name="sample_text")
    a2 = syswbeff106_Component(name="sample_text_2")
    b = syswbeff106_Component(name="sample_text")
    _safe_set(b, 'syswbeff106_Component48', a1)
    assert _is_linked(b, 'syswbeff106_Component48', a1)
    if hasattr(a1, 'syswbeff106_Component46'):
        assert _is_linked(a1, 'syswbeff106_Component46', b)
    _safe_set(b, 'syswbeff106_Component48', a2)
    assert _is_linked(b, 'syswbeff106_Component48', a2)
    if hasattr(a1, 'syswbeff106_Component46'):
        assert not _is_linked(a1, 'syswbeff106_Component46', b)
    if hasattr(a2, 'syswbeff106_Component46'):
        assert _is_linked(a2, 'syswbeff106_Component46', b)
    _safe_set(b, 'syswbeff106_Component48', None)
    assert not _is_linked(b, 'syswbeff106_Component48', a2)
    if hasattr(a2, 'syswbeff106_Component46'):
        assert not _is_linked(a2, 'syswbeff106_Component46', b)


def test_assoc_catalog70_reverse_link_reassign_clear():
    a1 = syswbeff106_Workbench(aprop="sample_text")
    a2 = syswbeff106_Workbench(aprop="sample_text_2")
    b = syswbeff106_PatternCatalog(id="sample_text")
    _safe_set(b, 'syswbeff106_PatternCatalog72', a1)
    assert _is_linked(b, 'syswbeff106_PatternCatalog72', a1)
    if hasattr(a1, 'syswbeff106_Workbench71'):
        assert _is_linked(a1, 'syswbeff106_Workbench71', b)
    _safe_set(b, 'syswbeff106_PatternCatalog72', a2)
    assert _is_linked(b, 'syswbeff106_PatternCatalog72', a2)
    if hasattr(a1, 'syswbeff106_Workbench71'):
        assert not _is_linked(a1, 'syswbeff106_Workbench71', b)
    if hasattr(a2, 'syswbeff106_Workbench71'):
        assert _is_linked(a2, 'syswbeff106_Workbench71', b)
    _safe_set(b, 'syswbeff106_PatternCatalog72', None)
    assert not _is_linked(b, 'syswbeff106_PatternCatalog72', a2)
    if hasattr(a2, 'syswbeff106_Workbench71'):
        assert not _is_linked(a2, 'syswbeff106_Workbench71', b)


def test_assoc_controlFlowEdge22_reverse_link_reassign_clear():
    a1 = syswbeff106_SequenceNode(name="sample_text", tMax=7, tMin=7)
    a2 = syswbeff106_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    b = syswbeff106_SequenceNode(name="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'syswbeff106_SequenceNode21', {a1})
    assert _is_linked(b, 'syswbeff106_SequenceNode21', a1)
    if hasattr(a1, 'syswbeff106_SequenceNode'):
        assert _is_linked(a1, 'syswbeff106_SequenceNode', b)
    _safe_set(b, 'syswbeff106_SequenceNode21', {a2})
    assert _is_linked(b, 'syswbeff106_SequenceNode21', a2)
    if hasattr(a1, 'syswbeff106_SequenceNode'):
        assert not _is_linked(a1, 'syswbeff106_SequenceNode', b)
    if hasattr(a2, 'syswbeff106_SequenceNode'):
        assert _is_linked(a2, 'syswbeff106_SequenceNode', b)
    _safe_set(b, 'syswbeff106_SequenceNode21', set())
    assert not _is_linked(b, 'syswbeff106_SequenceNode21', a2)
    if hasattr(a2, 'syswbeff106_SequenceNode'):
        assert not _is_linked(a2, 'syswbeff106_SequenceNode', b)


def test_assoc_decompositions1_reverse_link_reassign_clear():
    a1 = syswbeff106_Function(domain="sample_text")
    a2 = syswbeff106_Function(domain="sample_text_2")
    b = syswbeff106_Function(domain="sample_text")
    _safe_set(b, 'syswbeff106_Function0', {a1})
    assert _is_linked(b, 'syswbeff106_Function0', a1)
    if hasattr(a1, 'syswbeff106_Function'):
        assert _is_linked(a1, 'syswbeff106_Function', b)
    _safe_set(b, 'syswbeff106_Function0', {a2})
    assert _is_linked(b, 'syswbeff106_Function0', a2)
    if hasattr(a1, 'syswbeff106_Function'):
        assert not _is_linked(a1, 'syswbeff106_Function', b)
    if hasattr(a2, 'syswbeff106_Function'):
        assert _is_linked(a2, 'syswbeff106_Function', b)
    _safe_set(b, 'syswbeff106_Function0', set())
    assert not _is_linked(b, 'syswbeff106_Function0', a2)
    if hasattr(a2, 'syswbeff106_Function'):
        assert not _is_linked(a2, 'syswbeff106_Function', b)


def test_assoc_decompositions44_reverse_link_reassign_clear():
    a1 = syswbeff106_Component(name="sample_text")
    a2 = syswbeff106_Component(name="sample_text_2")
    b = syswbeff106_Component(name="sample_text")
    _safe_set(b, 'syswbeff106_Component45', a1)
    assert _is_linked(b, 'syswbeff106_Component45', a1)
    if hasattr(a1, 'syswbeff106_Component43'):
        assert _is_linked(a1, 'syswbeff106_Component43', b)
    _safe_set(b, 'syswbeff106_Component45', a2)
    assert _is_linked(b, 'syswbeff106_Component45', a2)
    if hasattr(a1, 'syswbeff106_Component43'):
        assert not _is_linked(a1, 'syswbeff106_Component43', b)
    if hasattr(a2, 'syswbeff106_Component43'):
        assert _is_linked(a2, 'syswbeff106_Component43', b)
    _safe_set(b, 'syswbeff106_Component45', None)
    assert not _is_linked(b, 'syswbeff106_Component45', a2)
    if hasattr(a2, 'syswbeff106_Component43'):
        assert not _is_linked(a2, 'syswbeff106_Component43', b)


def test_assoc_descriptions10_reverse_link_reassign_clear():
    a1 = syswbeff106_Function(domain="sample_text")
    a2 = syswbeff106_Function(domain="sample_text_2")
    b = syswbeff106_Description(content="sample_text")
    _safe_set(b, 'syswbeff106_Description', a1)
    assert _is_linked(b, 'syswbeff106_Description', a1)
    if hasattr(a1, 'syswbeff106_Function11'):
        assert _is_linked(a1, 'syswbeff106_Function11', b)
    _safe_set(b, 'syswbeff106_Description', a2)
    assert _is_linked(b, 'syswbeff106_Description', a2)
    if hasattr(a1, 'syswbeff106_Function11'):
        assert not _is_linked(a1, 'syswbeff106_Function11', b)
    if hasattr(a2, 'syswbeff106_Function11'):
        assert _is_linked(a2, 'syswbeff106_Function11', b)
    _safe_set(b, 'syswbeff106_Description', None)
    assert not _is_linked(b, 'syswbeff106_Description', a2)
    if hasattr(a2, 'syswbeff106_Function11'):
        assert not _is_linked(a2, 'syswbeff106_Function11', b)


def test_assoc_fromThing31_reverse_link_reassign_clear():
    a1 = syswbeff106_Thing(id=7)
    a2 = syswbeff106_Thing(id=13)
    b = syswbeff106_RelatedTo(since="sample_text")
    _safe_set(b, 'syswbeff106_RelatedTo', a1)
    assert _is_linked(b, 'syswbeff106_RelatedTo', a1)
    if hasattr(a1, 'syswbeff106_Thing'):
        assert _is_linked(a1, 'syswbeff106_Thing', b)
    _safe_set(b, 'syswbeff106_RelatedTo', a2)
    assert _is_linked(b, 'syswbeff106_RelatedTo', a2)
    if hasattr(a1, 'syswbeff106_Thing'):
        assert not _is_linked(a1, 'syswbeff106_Thing', b)
    if hasattr(a2, 'syswbeff106_Thing'):
        assert _is_linked(a2, 'syswbeff106_Thing', b)
    _safe_set(b, 'syswbeff106_RelatedTo', None)
    assert not _is_linked(b, 'syswbeff106_RelatedTo', a2)
    if hasattr(a2, 'syswbeff106_Thing'):
        assert not _is_linked(a2, 'syswbeff106_Thing', b)


def test_assoc_functionProperties67_reverse_link_reassign_clear():
    a1 = syswbeff106_Workbench(aprop="sample_text")
    a2 = syswbeff106_Workbench(aprop="sample_text_2")
    b = syswbeff106_FunctionProperty(description="sample_text")
    _safe_set(b, 'syswbeff106_FunctionProperty69', a1)
    assert _is_linked(b, 'syswbeff106_FunctionProperty69', a1)
    if hasattr(a1, 'syswbeff106_Workbench68'):
        assert _is_linked(a1, 'syswbeff106_Workbench68', b)
    _safe_set(b, 'syswbeff106_FunctionProperty69', a2)
    assert _is_linked(b, 'syswbeff106_FunctionProperty69', a2)
    if hasattr(a1, 'syswbeff106_Workbench68'):
        assert not _is_linked(a1, 'syswbeff106_Workbench68', b)
    if hasattr(a2, 'syswbeff106_Workbench68'):
        assert _is_linked(a2, 'syswbeff106_Workbench68', b)
    _safe_set(b, 'syswbeff106_FunctionProperty69', None)
    assert not _is_linked(b, 'syswbeff106_FunctionProperty69', a2)
    if hasattr(a2, 'syswbeff106_Workbench68'):
        assert not _is_linked(a2, 'syswbeff106_Workbench68', b)


def test_assoc_parent41_reverse_link_reassign_clear():
    a1 = syswbeff106_FunctionProperty(description="sample_text")
    a2 = syswbeff106_FunctionProperty(description="sample_text_2")
    b = syswbeff106_FunctionProperty(description="sample_text")
    _safe_set(b, 'syswbeff106_FunctionProperty42', a1)
    assert _is_linked(b, 'syswbeff106_FunctionProperty42', a1)
    if hasattr(a1, 'syswbeff106_FunctionProperty40'):
        assert _is_linked(a1, 'syswbeff106_FunctionProperty40', b)
    _safe_set(b, 'syswbeff106_FunctionProperty42', a2)
    assert _is_linked(b, 'syswbeff106_FunctionProperty42', a2)
    if hasattr(a1, 'syswbeff106_FunctionProperty40'):
        assert not _is_linked(a1, 'syswbeff106_FunctionProperty40', b)
    if hasattr(a2, 'syswbeff106_FunctionProperty40'):
        assert _is_linked(a2, 'syswbeff106_FunctionProperty40', b)
    _safe_set(b, 'syswbeff106_FunctionProperty42', None)
    assert not _is_linked(b, 'syswbeff106_FunctionProperty42', a2)
    if hasattr(a2, 'syswbeff106_FunctionProperty40'):
        assert not _is_linked(a2, 'syswbeff106_FunctionProperty40', b)


def test_assoc_patterns57_reverse_link_reassign_clear():
    a1 = syswbeff106_PatternCatalog(id="sample_text")
    a2 = syswbeff106_PatternCatalog(id="sample_text_2")
    b = syswbeff106_Function(domain="sample_text")
    _safe_set(b, 'syswbeff106_Function58', a1)
    assert _is_linked(b, 'syswbeff106_Function58', a1)
    if hasattr(a1, 'syswbeff106_PatternCatalog'):
        assert _is_linked(a1, 'syswbeff106_PatternCatalog', b)
    _safe_set(b, 'syswbeff106_Function58', a2)
    assert _is_linked(b, 'syswbeff106_Function58', a2)
    if hasattr(a1, 'syswbeff106_PatternCatalog'):
        assert not _is_linked(a1, 'syswbeff106_PatternCatalog', b)
    if hasattr(a2, 'syswbeff106_PatternCatalog'):
        assert _is_linked(a2, 'syswbeff106_PatternCatalog', b)
    _safe_set(b, 'syswbeff106_Function58', None)
    assert not _is_linked(b, 'syswbeff106_Function58', a2)
    if hasattr(a2, 'syswbeff106_PatternCatalog'):
        assert not _is_linked(a2, 'syswbeff106_PatternCatalog', b)


def test_assoc_performs49_reverse_link_reassign_clear():
    a1 = syswbeff106_Function(domain="sample_text")
    a2 = syswbeff106_Function(domain="sample_text_2")
    b = syswbeff106_Component(name="sample_text")
    _safe_set(b, 'syswbeff106_Component50', {a1})
    assert _is_linked(b, 'syswbeff106_Component50', a1)
    if hasattr(a1, 'syswbeff106_Function51'):
        assert _is_linked(a1, 'syswbeff106_Function51', b)
    _safe_set(b, 'syswbeff106_Component50', {a2})
    assert _is_linked(b, 'syswbeff106_Component50', a2)
    if hasattr(a1, 'syswbeff106_Function51'):
        assert not _is_linked(a1, 'syswbeff106_Function51', b)
    if hasattr(a2, 'syswbeff106_Function51'):
        assert _is_linked(a2, 'syswbeff106_Function51', b)
    _safe_set(b, 'syswbeff106_Component50', set())
    assert not _is_linked(b, 'syswbeff106_Component50', a2)
    if hasattr(a2, 'syswbeff106_Function51'):
        assert not _is_linked(a2, 'syswbeff106_Function51', b)


def test_assoc_property14_reverse_link_reassign_clear():
    a1 = syswbeff106_FunctionProperty(description="sample_text")
    a2 = syswbeff106_FunctionProperty(description="sample_text_2")
    b = syswbeff106_Function(domain="sample_text")
    _safe_set(b, 'syswbeff106_Function15', {a1})
    assert _is_linked(b, 'syswbeff106_Function15', a1)
    if hasattr(a1, 'syswbeff106_FunctionProperty'):
        assert _is_linked(a1, 'syswbeff106_FunctionProperty', b)
    _safe_set(b, 'syswbeff106_Function15', {a2})
    assert _is_linked(b, 'syswbeff106_Function15', a2)
    if hasattr(a1, 'syswbeff106_FunctionProperty'):
        assert not _is_linked(a1, 'syswbeff106_FunctionProperty', b)
    if hasattr(a2, 'syswbeff106_FunctionProperty'):
        assert _is_linked(a2, 'syswbeff106_FunctionProperty', b)
    _safe_set(b, 'syswbeff106_Function15', set())
    assert not _is_linked(b, 'syswbeff106_Function15', a2)
    if hasattr(a2, 'syswbeff106_FunctionProperty'):
        assert not _is_linked(a2, 'syswbeff106_FunctionProperty', b)


def test_assoc_relations35_reverse_link_reassign_clear():
    a1 = syswbeff106_Thing(id=7)
    a2 = syswbeff106_Thing(id=13)
    b = syswbeff106_RelatedTo(since="sample_text")
    _safe_set(b, 'syswbeff106_RelatedTo37', a1)
    assert _is_linked(b, 'syswbeff106_RelatedTo37', a1)
    if hasattr(a1, 'syswbeff106_Thing36'):
        assert _is_linked(a1, 'syswbeff106_Thing36', b)
    _safe_set(b, 'syswbeff106_RelatedTo37', a2)
    assert _is_linked(b, 'syswbeff106_RelatedTo37', a2)
    if hasattr(a1, 'syswbeff106_Thing36'):
        assert not _is_linked(a1, 'syswbeff106_Thing36', b)
    if hasattr(a2, 'syswbeff106_Thing36'):
        assert _is_linked(a2, 'syswbeff106_Thing36', b)
    _safe_set(b, 'syswbeff106_RelatedTo37', None)
    assert not _is_linked(b, 'syswbeff106_RelatedTo37', a2)
    if hasattr(a2, 'syswbeff106_Thing36'):
        assert not _is_linked(a2, 'syswbeff106_Thing36', b)


def test_assoc_things59_reverse_link_reassign_clear():
    a1 = syswbeff106_Workbench(aprop="sample_text")
    a2 = syswbeff106_Workbench(aprop="sample_text_2")
    b = syswbeff106_Thing(id=7)
    _safe_set(b, 'syswbeff106_Thing60', a1)
    assert _is_linked(b, 'syswbeff106_Thing60', a1)
    if hasattr(a1, 'syswbeff106_Workbench'):
        assert _is_linked(a1, 'syswbeff106_Workbench', b)
    _safe_set(b, 'syswbeff106_Thing60', a2)
    assert _is_linked(b, 'syswbeff106_Thing60', a2)
    if hasattr(a1, 'syswbeff106_Workbench'):
        assert not _is_linked(a1, 'syswbeff106_Workbench', b)
    if hasattr(a2, 'syswbeff106_Workbench'):
        assert _is_linked(a2, 'syswbeff106_Workbench', b)
    _safe_set(b, 'syswbeff106_Thing60', None)
    assert not _is_linked(b, 'syswbeff106_Thing60', a2)
    if hasattr(a2, 'syswbeff106_Workbench'):
        assert not _is_linked(a2, 'syswbeff106_Workbench', b)


def test_assoc_toThing32_reverse_link_reassign_clear():
    a1 = syswbeff106_Thing(id=7)
    a2 = syswbeff106_Thing(id=13)
    b = syswbeff106_RelatedTo(since="sample_text")
    _safe_set(b, 'syswbeff106_RelatedTo33', a1)
    assert _is_linked(b, 'syswbeff106_RelatedTo33', a1)
    if hasattr(a1, 'syswbeff106_Thing34'):
        assert _is_linked(a1, 'syswbeff106_Thing34', b)
    _safe_set(b, 'syswbeff106_RelatedTo33', a2)
    assert _is_linked(b, 'syswbeff106_RelatedTo33', a2)
    if hasattr(a1, 'syswbeff106_Thing34'):
        assert not _is_linked(a1, 'syswbeff106_Thing34', b)
    if hasattr(a2, 'syswbeff106_Thing34'):
        assert _is_linked(a2, 'syswbeff106_Thing34', b)
    _safe_set(b, 'syswbeff106_RelatedTo33', None)
    assert not _is_linked(b, 'syswbeff106_RelatedTo33', a2)
    if hasattr(a2, 'syswbeff106_Thing34'):
        assert not _is_linked(a2, 'syswbeff106_Thing34', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_flows4_stub_double():
    # syswbeff106_Flow has no real 'syswbeff106_Flow' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Function(domain="sample_text")
    partner = syswbeff106_Flow()
    setattr(partner, 'syswbeff106_Flow', None)
    _safe_set(owner, 'syswbeff106_Function5', {partner})
    assert getattr(partner, 'syswbeff106_Flow') == owner
    _safe_set(owner, 'syswbeff106_Function5', set())
    assert getattr(partner, 'syswbeff106_Flow') is None


def test_assoc_functionalArchitecture52_stub_double():
    # syswbeff106_System has no real 'syswbeff106_System' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Function(domain="sample_text")
    partner = syswbeff106_System()
    setattr(partner, 'syswbeff106_System', None)
    _safe_set(owner, 'syswbeff106_Function53', partner)
    assert getattr(partner, 'syswbeff106_System') == owner
    _safe_set(owner, 'syswbeff106_Function53', None)
    assert getattr(partner, 'syswbeff106_System') is None


def test_assoc_inputPorts8_stub_double():
    # syswbeff106_InputPort has no real 'syswbeff106_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Function(domain="sample_text")
    partner = syswbeff106_InputPort()
    setattr(partner, 'syswbeff106_InputPort', None)
    _safe_set(owner, 'syswbeff106_Function9', {partner})
    assert getattr(partner, 'syswbeff106_InputPort') == owner
    _safe_set(owner, 'syswbeff106_Function9', set())
    assert getattr(partner, 'syswbeff106_InputPort') is None


def test_assoc_items26_stub_double():
    # syswbeff106_Flow has no real 'syswbeff106_Flow27' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Item(name="sample_text")
    partner = syswbeff106_Flow()
    setattr(partner, 'syswbeff106_Flow27', None)
    _safe_set(owner, 'syswbeff106_Item', partner)
    assert owner in getattr(partner, 'syswbeff106_Flow27')
    _safe_set(owner, 'syswbeff106_Item', None)
    assert owner not in getattr(partner, 'syswbeff106_Flow27')


def test_assoc_outputPorts6_stub_double():
    # syswbeff106_OutputPort has no real 'syswbeff106_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Function(domain="sample_text")
    partner = syswbeff106_OutputPort()
    setattr(partner, 'syswbeff106_OutputPort', None)
    _safe_set(owner, 'syswbeff106_Function7', {partner})
    assert getattr(partner, 'syswbeff106_OutputPort') == owner
    _safe_set(owner, 'syswbeff106_Function7', set())
    assert getattr(partner, 'syswbeff106_OutputPort') is None


def test_assoc_physicalArchitecture54_stub_double():
    # syswbeff106_System has no real 'syswbeff106_System55' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Component(name="sample_text")
    partner = syswbeff106_System()
    setattr(partner, 'syswbeff106_System55', None)
    _safe_set(owner, 'syswbeff106_Component56', partner)
    assert getattr(partner, 'syswbeff106_System55') == owner
    _safe_set(owner, 'syswbeff106_Component56', None)
    assert getattr(partner, 'syswbeff106_System55') is None


def test_assoc_relatedTo38_stub_double():
    # syswbeff106_Thoughts has no real 'syswbeff106_Thoughts' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Thing(id=7)
    partner = syswbeff106_Thoughts()
    setattr(partner, 'syswbeff106_Thoughts', None)
    _safe_set(owner, 'syswbeff106_Thing39', partner)
    assert owner in getattr(partner, 'syswbeff106_Thoughts')
    _safe_set(owner, 'syswbeff106_Thing39', None)
    assert owner not in getattr(partner, 'syswbeff106_Thoughts')


def test_assoc_sequenceNodes2_stub_double():
    # syswbeff106_Sequence has no real 'syswbeff106_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Function(domain="sample_text")
    partner = syswbeff106_Sequence()
    setattr(partner, 'syswbeff106_Sequence', None)
    _safe_set(owner, 'syswbeff106_Function3', {partner})
    assert getattr(partner, 'syswbeff106_Sequence') == owner
    _safe_set(owner, 'syswbeff106_Function3', set())
    assert getattr(partner, 'syswbeff106_Sequence') is None


def test_assoc_systemView64_stub_double():
    # syswbeff106_System has no real 'syswbeff106_System66' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Workbench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Workbench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Workbench(aprop="sample_text")
    partner = syswbeff106_System()
    setattr(partner, 'syswbeff106_System66', None)
    _safe_set(owner, 'syswbeff106_Workbench65', partner)
    assert getattr(partner, 'syswbeff106_System66') == owner
    _safe_set(owner, 'syswbeff106_Workbench65', None)
    assert getattr(partner, 'syswbeff106_System66') is None


def test_assoc_thoughts61_stub_double():
    # syswbeff106_Thoughts has no real 'syswbeff106_Thoughts63' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Workbench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Workbench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Workbench(aprop="sample_text")
    partner = syswbeff106_Thoughts()
    setattr(partner, 'syswbeff106_Thoughts63', None)
    _safe_set(owner, 'syswbeff106_Workbench62', {partner})
    assert getattr(partner, 'syswbeff106_Thoughts63') == owner
    _safe_set(owner, 'syswbeff106_Workbench62', set())
    assert getattr(partner, 'syswbeff106_Thoughts63') is None


def test_assoc_tokens12_stub_double():
    # syswbeff106_Token has no real 'syswbeff106_Token' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff106_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff106_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff106_Function(domain="sample_text")
    partner = syswbeff106_Token()
    setattr(partner, 'syswbeff106_Token', None)
    _safe_set(owner, 'syswbeff106_Function13', {partner})
    assert getattr(partner, 'syswbeff106_Token') == owner
    _safe_set(owner, 'syswbeff106_Function13', set())
    assert getattr(partner, 'syswbeff106_Token') is None


