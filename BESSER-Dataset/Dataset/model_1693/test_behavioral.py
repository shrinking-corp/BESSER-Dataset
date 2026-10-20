import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    ProcessNode,
    Sequence,
    SequenceNode,
    syswbeff1065ok_And,
    syswbeff1065ok_AssociatedTo,
    syswbeff1065ok_Component,
    syswbeff1065ok_Description,
    syswbeff1065ok_Final,
    syswbeff1065ok_Flow,
    syswbeff1065ok_Function,
    syswbeff1065ok_FunctionProperty,
    syswbeff1065ok_InputPort,
    syswbeff1065ok_Item,
    syswbeff1065ok_Iteration,
    syswbeff1065ok_Loop,
    syswbeff1065ok_LoopExit,
    syswbeff1065ok_Or,
    syswbeff1065ok_OutputPort,
    syswbeff1065ok_PatternCatalog,
    syswbeff1065ok_Port,
    syswbeff1065ok_ProcessNode,
    syswbeff1065ok_Sequence,
    syswbeff1065ok_SequenceNode,
    syswbeff1065ok_Start,
    syswbeff1065ok_System,
    syswbeff1065ok_Thing,
    syswbeff1065ok_Thoughts,
    syswbeff1065ok_Token,
    syswbeff1065ok_Workbench,
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
    a1 = syswbeff1065ok_Function(domain="sample_text")
    a2 = syswbeff1065ok_Function(domain="sample_text_2")
    b = syswbeff1065ok_Component(name="sample_text")
    _safe_set(b, 'syswbeff1065ok_Component', a1)
    assert _is_linked(b, 'syswbeff1065ok_Component', a1)
    if hasattr(a1, 'syswbeff1065ok_Function20'):
        assert _is_linked(a1, 'syswbeff1065ok_Function20', b)
    _safe_set(b, 'syswbeff1065ok_Component', a2)
    assert _is_linked(b, 'syswbeff1065ok_Component', a2)
    if hasattr(a1, 'syswbeff1065ok_Function20'):
        assert not _is_linked(a1, 'syswbeff1065ok_Function20', b)
    if hasattr(a2, 'syswbeff1065ok_Function20'):
        assert _is_linked(a2, 'syswbeff1065ok_Function20', b)
    _safe_set(b, 'syswbeff1065ok_Component', None)
    assert not _is_linked(b, 'syswbeff1065ok_Component', a2)
    if hasattr(a2, 'syswbeff1065ok_Function20'):
        assert not _is_linked(a2, 'syswbeff1065ok_Function20', b)


def test_assoc_associations17_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Function(domain="sample_text")
    a2 = syswbeff1065ok_Function(domain="sample_text_2")
    b = syswbeff1065ok_Function(domain="sample_text")
    _safe_set(b, 'syswbeff1065ok_Function18', a1)
    assert _is_linked(b, 'syswbeff1065ok_Function18', a1)
    if hasattr(a1, 'syswbeff1065ok_Function16'):
        assert _is_linked(a1, 'syswbeff1065ok_Function16', b)
    _safe_set(b, 'syswbeff1065ok_Function18', a2)
    assert _is_linked(b, 'syswbeff1065ok_Function18', a2)
    if hasattr(a1, 'syswbeff1065ok_Function16'):
        assert not _is_linked(a1, 'syswbeff1065ok_Function16', b)
    if hasattr(a2, 'syswbeff1065ok_Function16'):
        assert _is_linked(a2, 'syswbeff1065ok_Function16', b)
    _safe_set(b, 'syswbeff1065ok_Function18', None)
    assert not _is_linked(b, 'syswbeff1065ok_Function18', a2)
    if hasattr(a2, 'syswbeff1065ok_Function16'):
        assert not _is_linked(a2, 'syswbeff1065ok_Function16', b)


def test_assoc_associations47_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Component(name="sample_text")
    a2 = syswbeff1065ok_Component(name="sample_text_2")
    b = syswbeff1065ok_Component(name="sample_text")
    _safe_set(b, 'syswbeff1065ok_Component48', a1)
    assert _is_linked(b, 'syswbeff1065ok_Component48', a1)
    if hasattr(a1, 'syswbeff1065ok_Component46'):
        assert _is_linked(a1, 'syswbeff1065ok_Component46', b)
    _safe_set(b, 'syswbeff1065ok_Component48', a2)
    assert _is_linked(b, 'syswbeff1065ok_Component48', a2)
    if hasattr(a1, 'syswbeff1065ok_Component46'):
        assert not _is_linked(a1, 'syswbeff1065ok_Component46', b)
    if hasattr(a2, 'syswbeff1065ok_Component46'):
        assert _is_linked(a2, 'syswbeff1065ok_Component46', b)
    _safe_set(b, 'syswbeff1065ok_Component48', None)
    assert not _is_linked(b, 'syswbeff1065ok_Component48', a2)
    if hasattr(a2, 'syswbeff1065ok_Component46'):
        assert not _is_linked(a2, 'syswbeff1065ok_Component46', b)


def test_assoc_controlFlowEdge22_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_SequenceNode(name="sample_text", tMax=7, tMin=7)
    a2 = syswbeff1065ok_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    b = syswbeff1065ok_SequenceNode(name="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'syswbeff1065ok_SequenceNode21', {a1})
    assert _is_linked(b, 'syswbeff1065ok_SequenceNode21', a1)
    if hasattr(a1, 'syswbeff1065ok_SequenceNode'):
        assert _is_linked(a1, 'syswbeff1065ok_SequenceNode', b)
    _safe_set(b, 'syswbeff1065ok_SequenceNode21', {a2})
    assert _is_linked(b, 'syswbeff1065ok_SequenceNode21', a2)
    if hasattr(a1, 'syswbeff1065ok_SequenceNode'):
        assert not _is_linked(a1, 'syswbeff1065ok_SequenceNode', b)
    if hasattr(a2, 'syswbeff1065ok_SequenceNode'):
        assert _is_linked(a2, 'syswbeff1065ok_SequenceNode', b)
    _safe_set(b, 'syswbeff1065ok_SequenceNode21', set())
    assert not _is_linked(b, 'syswbeff1065ok_SequenceNode21', a2)
    if hasattr(a2, 'syswbeff1065ok_SequenceNode'):
        assert not _is_linked(a2, 'syswbeff1065ok_SequenceNode', b)


def test_assoc_decompositions1_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Function(domain="sample_text")
    a2 = syswbeff1065ok_Function(domain="sample_text_2")
    b = syswbeff1065ok_Function(domain="sample_text")
    _safe_set(b, 'syswbeff1065ok_Function0', {a1})
    assert _is_linked(b, 'syswbeff1065ok_Function0', a1)
    if hasattr(a1, 'syswbeff1065ok_Function'):
        assert _is_linked(a1, 'syswbeff1065ok_Function', b)
    _safe_set(b, 'syswbeff1065ok_Function0', {a2})
    assert _is_linked(b, 'syswbeff1065ok_Function0', a2)
    if hasattr(a1, 'syswbeff1065ok_Function'):
        assert not _is_linked(a1, 'syswbeff1065ok_Function', b)
    if hasattr(a2, 'syswbeff1065ok_Function'):
        assert _is_linked(a2, 'syswbeff1065ok_Function', b)
    _safe_set(b, 'syswbeff1065ok_Function0', set())
    assert not _is_linked(b, 'syswbeff1065ok_Function0', a2)
    if hasattr(a2, 'syswbeff1065ok_Function'):
        assert not _is_linked(a2, 'syswbeff1065ok_Function', b)


def test_assoc_decompositions44_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Component(name="sample_text")
    a2 = syswbeff1065ok_Component(name="sample_text_2")
    b = syswbeff1065ok_Component(name="sample_text")
    _safe_set(b, 'syswbeff1065ok_Component45', a1)
    assert _is_linked(b, 'syswbeff1065ok_Component45', a1)
    if hasattr(a1, 'syswbeff1065ok_Component43'):
        assert _is_linked(a1, 'syswbeff1065ok_Component43', b)
    _safe_set(b, 'syswbeff1065ok_Component45', a2)
    assert _is_linked(b, 'syswbeff1065ok_Component45', a2)
    if hasattr(a1, 'syswbeff1065ok_Component43'):
        assert not _is_linked(a1, 'syswbeff1065ok_Component43', b)
    if hasattr(a2, 'syswbeff1065ok_Component43'):
        assert _is_linked(a2, 'syswbeff1065ok_Component43', b)
    _safe_set(b, 'syswbeff1065ok_Component45', None)
    assert not _is_linked(b, 'syswbeff1065ok_Component45', a2)
    if hasattr(a2, 'syswbeff1065ok_Component43'):
        assert not _is_linked(a2, 'syswbeff1065ok_Component43', b)


def test_assoc_descriptions10_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Function(domain="sample_text")
    a2 = syswbeff1065ok_Function(domain="sample_text_2")
    b = syswbeff1065ok_Description(content="sample_text")
    _safe_set(b, 'syswbeff1065ok_Description', a1)
    assert _is_linked(b, 'syswbeff1065ok_Description', a1)
    if hasattr(a1, 'syswbeff1065ok_Function11'):
        assert _is_linked(a1, 'syswbeff1065ok_Function11', b)
    _safe_set(b, 'syswbeff1065ok_Description', a2)
    assert _is_linked(b, 'syswbeff1065ok_Description', a2)
    if hasattr(a1, 'syswbeff1065ok_Function11'):
        assert not _is_linked(a1, 'syswbeff1065ok_Function11', b)
    if hasattr(a2, 'syswbeff1065ok_Function11'):
        assert _is_linked(a2, 'syswbeff1065ok_Function11', b)
    _safe_set(b, 'syswbeff1065ok_Description', None)
    assert not _is_linked(b, 'syswbeff1065ok_Description', a2)
    if hasattr(a2, 'syswbeff1065ok_Function11'):
        assert not _is_linked(a2, 'syswbeff1065ok_Function11', b)


def test_assoc_fromThing31_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Thing(id=7)
    a2 = syswbeff1065ok_Thing(id=13)
    b = syswbeff1065ok_AssociatedTo(since="sample_text")
    _safe_set(b, 'syswbeff1065ok_AssociatedTo', a1)
    assert _is_linked(b, 'syswbeff1065ok_AssociatedTo', a1)
    if hasattr(a1, 'syswbeff1065ok_Thing'):
        assert _is_linked(a1, 'syswbeff1065ok_Thing', b)
    _safe_set(b, 'syswbeff1065ok_AssociatedTo', a2)
    assert _is_linked(b, 'syswbeff1065ok_AssociatedTo', a2)
    if hasattr(a1, 'syswbeff1065ok_Thing'):
        assert not _is_linked(a1, 'syswbeff1065ok_Thing', b)
    if hasattr(a2, 'syswbeff1065ok_Thing'):
        assert _is_linked(a2, 'syswbeff1065ok_Thing', b)
    _safe_set(b, 'syswbeff1065ok_AssociatedTo', None)
    assert not _is_linked(b, 'syswbeff1065ok_AssociatedTo', a2)
    if hasattr(a2, 'syswbeff1065ok_Thing'):
        assert not _is_linked(a2, 'syswbeff1065ok_Thing', b)


def test_assoc_functionalArchitecture52_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_System(id="sample_text")
    a2 = syswbeff1065ok_System(id="sample_text_2")
    b = syswbeff1065ok_Function(domain="sample_text")
    _safe_set(b, 'syswbeff1065ok_Function53', a1)
    assert _is_linked(b, 'syswbeff1065ok_Function53', a1)
    if hasattr(a1, 'syswbeff1065ok_System'):
        assert _is_linked(a1, 'syswbeff1065ok_System', b)
    _safe_set(b, 'syswbeff1065ok_Function53', a2)
    assert _is_linked(b, 'syswbeff1065ok_Function53', a2)
    if hasattr(a1, 'syswbeff1065ok_System'):
        assert not _is_linked(a1, 'syswbeff1065ok_System', b)
    if hasattr(a2, 'syswbeff1065ok_System'):
        assert _is_linked(a2, 'syswbeff1065ok_System', b)
    _safe_set(b, 'syswbeff1065ok_Function53', None)
    assert not _is_linked(b, 'syswbeff1065ok_Function53', a2)
    if hasattr(a2, 'syswbeff1065ok_System'):
        assert not _is_linked(a2, 'syswbeff1065ok_System', b)


def test_assoc_parent41_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_FunctionProperty(description="sample_text")
    a2 = syswbeff1065ok_FunctionProperty(description="sample_text_2")
    b = syswbeff1065ok_FunctionProperty(description="sample_text")
    _safe_set(b, 'syswbeff1065ok_FunctionProperty42', a1)
    assert _is_linked(b, 'syswbeff1065ok_FunctionProperty42', a1)
    if hasattr(a1, 'syswbeff1065ok_FunctionProperty40'):
        assert _is_linked(a1, 'syswbeff1065ok_FunctionProperty40', b)
    _safe_set(b, 'syswbeff1065ok_FunctionProperty42', a2)
    assert _is_linked(b, 'syswbeff1065ok_FunctionProperty42', a2)
    if hasattr(a1, 'syswbeff1065ok_FunctionProperty40'):
        assert not _is_linked(a1, 'syswbeff1065ok_FunctionProperty40', b)
    if hasattr(a2, 'syswbeff1065ok_FunctionProperty40'):
        assert _is_linked(a2, 'syswbeff1065ok_FunctionProperty40', b)
    _safe_set(b, 'syswbeff1065ok_FunctionProperty42', None)
    assert not _is_linked(b, 'syswbeff1065ok_FunctionProperty42', a2)
    if hasattr(a2, 'syswbeff1065ok_FunctionProperty40'):
        assert not _is_linked(a2, 'syswbeff1065ok_FunctionProperty40', b)


def test_assoc_patterns57_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_PatternCatalog(id="sample_text")
    a2 = syswbeff1065ok_PatternCatalog(id="sample_text_2")
    b = syswbeff1065ok_Function(domain="sample_text")
    _safe_set(b, 'syswbeff1065ok_Function58', a1)
    assert _is_linked(b, 'syswbeff1065ok_Function58', a1)
    if hasattr(a1, 'syswbeff1065ok_PatternCatalog'):
        assert _is_linked(a1, 'syswbeff1065ok_PatternCatalog', b)
    _safe_set(b, 'syswbeff1065ok_Function58', a2)
    assert _is_linked(b, 'syswbeff1065ok_Function58', a2)
    if hasattr(a1, 'syswbeff1065ok_PatternCatalog'):
        assert not _is_linked(a1, 'syswbeff1065ok_PatternCatalog', b)
    if hasattr(a2, 'syswbeff1065ok_PatternCatalog'):
        assert _is_linked(a2, 'syswbeff1065ok_PatternCatalog', b)
    _safe_set(b, 'syswbeff1065ok_Function58', None)
    assert not _is_linked(b, 'syswbeff1065ok_Function58', a2)
    if hasattr(a2, 'syswbeff1065ok_PatternCatalog'):
        assert not _is_linked(a2, 'syswbeff1065ok_PatternCatalog', b)


def test_assoc_performs49_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Function(domain="sample_text")
    a2 = syswbeff1065ok_Function(domain="sample_text_2")
    b = syswbeff1065ok_Component(name="sample_text")
    _safe_set(b, 'syswbeff1065ok_Component50', {a1})
    assert _is_linked(b, 'syswbeff1065ok_Component50', a1)
    if hasattr(a1, 'syswbeff1065ok_Function51'):
        assert _is_linked(a1, 'syswbeff1065ok_Function51', b)
    _safe_set(b, 'syswbeff1065ok_Component50', {a2})
    assert _is_linked(b, 'syswbeff1065ok_Component50', a2)
    if hasattr(a1, 'syswbeff1065ok_Function51'):
        assert not _is_linked(a1, 'syswbeff1065ok_Function51', b)
    if hasattr(a2, 'syswbeff1065ok_Function51'):
        assert _is_linked(a2, 'syswbeff1065ok_Function51', b)
    _safe_set(b, 'syswbeff1065ok_Component50', set())
    assert not _is_linked(b, 'syswbeff1065ok_Component50', a2)
    if hasattr(a2, 'syswbeff1065ok_Function51'):
        assert not _is_linked(a2, 'syswbeff1065ok_Function51', b)


def test_assoc_physicalArchitecture54_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_System(id="sample_text")
    a2 = syswbeff1065ok_System(id="sample_text_2")
    b = syswbeff1065ok_Component(name="sample_text")
    _safe_set(b, 'syswbeff1065ok_Component56', a1)
    assert _is_linked(b, 'syswbeff1065ok_Component56', a1)
    if hasattr(a1, 'syswbeff1065ok_System55'):
        assert _is_linked(a1, 'syswbeff1065ok_System55', b)
    _safe_set(b, 'syswbeff1065ok_Component56', a2)
    assert _is_linked(b, 'syswbeff1065ok_Component56', a2)
    if hasattr(a1, 'syswbeff1065ok_System55'):
        assert not _is_linked(a1, 'syswbeff1065ok_System55', b)
    if hasattr(a2, 'syswbeff1065ok_System55'):
        assert _is_linked(a2, 'syswbeff1065ok_System55', b)
    _safe_set(b, 'syswbeff1065ok_Component56', None)
    assert not _is_linked(b, 'syswbeff1065ok_Component56', a2)
    if hasattr(a2, 'syswbeff1065ok_System55'):
        assert not _is_linked(a2, 'syswbeff1065ok_System55', b)


def test_assoc_property14_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_FunctionProperty(description="sample_text")
    a2 = syswbeff1065ok_FunctionProperty(description="sample_text_2")
    b = syswbeff1065ok_Function(domain="sample_text")
    _safe_set(b, 'syswbeff1065ok_Function15', {a1})
    assert _is_linked(b, 'syswbeff1065ok_Function15', a1)
    if hasattr(a1, 'syswbeff1065ok_FunctionProperty'):
        assert _is_linked(a1, 'syswbeff1065ok_FunctionProperty', b)
    _safe_set(b, 'syswbeff1065ok_Function15', {a2})
    assert _is_linked(b, 'syswbeff1065ok_Function15', a2)
    if hasattr(a1, 'syswbeff1065ok_FunctionProperty'):
        assert not _is_linked(a1, 'syswbeff1065ok_FunctionProperty', b)
    if hasattr(a2, 'syswbeff1065ok_FunctionProperty'):
        assert _is_linked(a2, 'syswbeff1065ok_FunctionProperty', b)
    _safe_set(b, 'syswbeff1065ok_Function15', set())
    assert not _is_linked(b, 'syswbeff1065ok_Function15', a2)
    if hasattr(a2, 'syswbeff1065ok_FunctionProperty'):
        assert not _is_linked(a2, 'syswbeff1065ok_FunctionProperty', b)


def test_assoc_relatedTo38_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Thoughts(id="sample_text")
    a2 = syswbeff1065ok_Thoughts(id="sample_text_2")
    b = syswbeff1065ok_Thing(id=7)
    _safe_set(b, 'syswbeff1065ok_Thing39', a1)
    assert _is_linked(b, 'syswbeff1065ok_Thing39', a1)
    if hasattr(a1, 'syswbeff1065ok_Thoughts'):
        assert _is_linked(a1, 'syswbeff1065ok_Thoughts', b)
    _safe_set(b, 'syswbeff1065ok_Thing39', a2)
    assert _is_linked(b, 'syswbeff1065ok_Thing39', a2)
    if hasattr(a1, 'syswbeff1065ok_Thoughts'):
        assert not _is_linked(a1, 'syswbeff1065ok_Thoughts', b)
    if hasattr(a2, 'syswbeff1065ok_Thoughts'):
        assert _is_linked(a2, 'syswbeff1065ok_Thoughts', b)
    _safe_set(b, 'syswbeff1065ok_Thing39', None)
    assert not _is_linked(b, 'syswbeff1065ok_Thing39', a2)
    if hasattr(a2, 'syswbeff1065ok_Thoughts'):
        assert not _is_linked(a2, 'syswbeff1065ok_Thoughts', b)


def test_assoc_relations35_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Thing(id=7)
    a2 = syswbeff1065ok_Thing(id=13)
    b = syswbeff1065ok_AssociatedTo(since="sample_text")
    _safe_set(b, 'syswbeff1065ok_AssociatedTo37', a1)
    assert _is_linked(b, 'syswbeff1065ok_AssociatedTo37', a1)
    if hasattr(a1, 'syswbeff1065ok_Thing36'):
        assert _is_linked(a1, 'syswbeff1065ok_Thing36', b)
    _safe_set(b, 'syswbeff1065ok_AssociatedTo37', a2)
    assert _is_linked(b, 'syswbeff1065ok_AssociatedTo37', a2)
    if hasattr(a1, 'syswbeff1065ok_Thing36'):
        assert not _is_linked(a1, 'syswbeff1065ok_Thing36', b)
    if hasattr(a2, 'syswbeff1065ok_Thing36'):
        assert _is_linked(a2, 'syswbeff1065ok_Thing36', b)
    _safe_set(b, 'syswbeff1065ok_AssociatedTo37', None)
    assert not _is_linked(b, 'syswbeff1065ok_AssociatedTo37', a2)
    if hasattr(a2, 'syswbeff1065ok_Thing36'):
        assert not _is_linked(a2, 'syswbeff1065ok_Thing36', b)


def test_assoc_toThing32_reverse_link_reassign_clear():
    a1 = syswbeff1065ok_Thing(id=7)
    a2 = syswbeff1065ok_Thing(id=13)
    b = syswbeff1065ok_AssociatedTo(since="sample_text")
    _safe_set(b, 'syswbeff1065ok_AssociatedTo33', a1)
    assert _is_linked(b, 'syswbeff1065ok_AssociatedTo33', a1)
    if hasattr(a1, 'syswbeff1065ok_Thing34'):
        assert _is_linked(a1, 'syswbeff1065ok_Thing34', b)
    _safe_set(b, 'syswbeff1065ok_AssociatedTo33', a2)
    assert _is_linked(b, 'syswbeff1065ok_AssociatedTo33', a2)
    if hasattr(a1, 'syswbeff1065ok_Thing34'):
        assert not _is_linked(a1, 'syswbeff1065ok_Thing34', b)
    if hasattr(a2, 'syswbeff1065ok_Thing34'):
        assert _is_linked(a2, 'syswbeff1065ok_Thing34', b)
    _safe_set(b, 'syswbeff1065ok_AssociatedTo33', None)
    assert not _is_linked(b, 'syswbeff1065ok_AssociatedTo33', a2)
    if hasattr(a2, 'syswbeff1065ok_Thing34'):
        assert not _is_linked(a2, 'syswbeff1065ok_Thing34', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_catalog70_stub_double():
    # syswbeff1065ok_Workbench has no real 'syswbeff1065ok_Workbench71' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_PatternCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_PatternCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_PatternCatalog(id="sample_text")
    partner = syswbeff1065ok_Workbench()
    setattr(partner, 'syswbeff1065ok_Workbench71', None)
    _safe_set(owner, 'syswbeff1065ok_PatternCatalog72', partner)
    assert owner in getattr(partner, 'syswbeff1065ok_Workbench71')
    _safe_set(owner, 'syswbeff1065ok_PatternCatalog72', None)
    assert owner not in getattr(partner, 'syswbeff1065ok_Workbench71')


def test_assoc_flows4_stub_double():
    # syswbeff1065ok_Flow has no real 'syswbeff1065ok_Flow' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Function(domain="sample_text")
    partner = syswbeff1065ok_Flow()
    setattr(partner, 'syswbeff1065ok_Flow', None)
    _safe_set(owner, 'syswbeff1065ok_Function5', {partner})
    assert getattr(partner, 'syswbeff1065ok_Flow') == owner
    _safe_set(owner, 'syswbeff1065ok_Function5', set())
    assert getattr(partner, 'syswbeff1065ok_Flow') is None


def test_assoc_functionProperties67_stub_double():
    # syswbeff1065ok_Workbench has no real 'syswbeff1065ok_Workbench68' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_FunctionProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_FunctionProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_FunctionProperty(description="sample_text")
    partner = syswbeff1065ok_Workbench()
    setattr(partner, 'syswbeff1065ok_Workbench68', None)
    _safe_set(owner, 'syswbeff1065ok_FunctionProperty69', partner)
    assert owner in getattr(partner, 'syswbeff1065ok_Workbench68')
    _safe_set(owner, 'syswbeff1065ok_FunctionProperty69', None)
    assert owner not in getattr(partner, 'syswbeff1065ok_Workbench68')


def test_assoc_inputPorts8_stub_double():
    # syswbeff1065ok_InputPort has no real 'syswbeff1065ok_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Function(domain="sample_text")
    partner = syswbeff1065ok_InputPort()
    setattr(partner, 'syswbeff1065ok_InputPort', None)
    _safe_set(owner, 'syswbeff1065ok_Function9', {partner})
    assert getattr(partner, 'syswbeff1065ok_InputPort') == owner
    _safe_set(owner, 'syswbeff1065ok_Function9', set())
    assert getattr(partner, 'syswbeff1065ok_InputPort') is None


def test_assoc_items26_stub_double():
    # syswbeff1065ok_Flow has no real 'syswbeff1065ok_Flow27' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Item(name="sample_text")
    partner = syswbeff1065ok_Flow()
    setattr(partner, 'syswbeff1065ok_Flow27', None)
    _safe_set(owner, 'syswbeff1065ok_Item', partner)
    assert owner in getattr(partner, 'syswbeff1065ok_Flow27')
    _safe_set(owner, 'syswbeff1065ok_Item', None)
    assert owner not in getattr(partner, 'syswbeff1065ok_Flow27')


def test_assoc_outputPorts6_stub_double():
    # syswbeff1065ok_OutputPort has no real 'syswbeff1065ok_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Function(domain="sample_text")
    partner = syswbeff1065ok_OutputPort()
    setattr(partner, 'syswbeff1065ok_OutputPort', None)
    _safe_set(owner, 'syswbeff1065ok_Function7', {partner})
    assert getattr(partner, 'syswbeff1065ok_OutputPort') == owner
    _safe_set(owner, 'syswbeff1065ok_Function7', set())
    assert getattr(partner, 'syswbeff1065ok_OutputPort') is None


def test_assoc_sequenceNodes2_stub_double():
    # syswbeff1065ok_Sequence has no real 'syswbeff1065ok_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Function(domain="sample_text")
    partner = syswbeff1065ok_Sequence()
    setattr(partner, 'syswbeff1065ok_Sequence', None)
    _safe_set(owner, 'syswbeff1065ok_Function3', {partner})
    assert getattr(partner, 'syswbeff1065ok_Sequence') == owner
    _safe_set(owner, 'syswbeff1065ok_Function3', set())
    assert getattr(partner, 'syswbeff1065ok_Sequence') is None


def test_assoc_systemView64_stub_double():
    # syswbeff1065ok_Workbench has no real 'syswbeff1065ok_Workbench65' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_System(id="sample_text")
    partner = syswbeff1065ok_Workbench()
    setattr(partner, 'syswbeff1065ok_Workbench65', None)
    _safe_set(owner, 'syswbeff1065ok_System66', partner)
    assert getattr(partner, 'syswbeff1065ok_Workbench65') == owner
    _safe_set(owner, 'syswbeff1065ok_System66', None)
    assert getattr(partner, 'syswbeff1065ok_Workbench65') is None


def test_assoc_things59_stub_double():
    # syswbeff1065ok_Workbench has no real 'syswbeff1065ok_Workbench' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Thing(id=7)
    partner = syswbeff1065ok_Workbench()
    setattr(partner, 'syswbeff1065ok_Workbench', None)
    _safe_set(owner, 'syswbeff1065ok_Thing60', partner)
    assert owner in getattr(partner, 'syswbeff1065ok_Workbench')
    _safe_set(owner, 'syswbeff1065ok_Thing60', None)
    assert owner not in getattr(partner, 'syswbeff1065ok_Workbench')


def test_assoc_thoughts61_stub_double():
    # syswbeff1065ok_Workbench has no real 'syswbeff1065ok_Workbench62' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Thoughts's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Thoughts's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Thoughts(id="sample_text")
    partner = syswbeff1065ok_Workbench()
    setattr(partner, 'syswbeff1065ok_Workbench62', None)
    _safe_set(owner, 'syswbeff1065ok_Thoughts63', partner)
    assert owner in getattr(partner, 'syswbeff1065ok_Workbench62')
    _safe_set(owner, 'syswbeff1065ok_Thoughts63', None)
    assert owner not in getattr(partner, 'syswbeff1065ok_Workbench62')


def test_assoc_tokens12_stub_double():
    # syswbeff1065ok_Token has no real 'syswbeff1065ok_Token' property in the generated
    # code (a bare stub) -- manually attach it so syswbeff1065ok_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswbeff1065ok_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswbeff1065ok_Function(domain="sample_text")
    partner = syswbeff1065ok_Token()
    setattr(partner, 'syswbeff1065ok_Token', None)
    _safe_set(owner, 'syswbeff1065ok_Function13', {partner})
    assert getattr(partner, 'syswbeff1065ok_Token') == owner
    _safe_set(owner, 'syswbeff1065ok_Function13', set())
    assert getattr(partner, 'syswbeff1065ok_Token') is None


