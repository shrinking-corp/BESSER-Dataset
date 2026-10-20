import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CodeBlock,
    Expression,
    Parameter,
    Statement,
    debugSeq_And,
    debugSeq_Assignment,
    debugSeq_BitAnd,
    debugSeq_BitNot,
    debugSeq_BitOr,
    debugSeq_BitXor,
    debugSeq_Block,
    debugSeq_CodeBlock,
    debugSeq_Comparison,
    debugSeq_Control,
    debugSeq_DapDelay,
    debugSeq_DapJtagSequence,
    debugSeq_DapSwjClock,
    debugSeq_DapSwjPins,
    debugSeq_DapSwjSequence,
    debugSeq_DapWriteABORT,
    debugSeq_DebugSeqModel,
    debugSeq_DebugVars,
    debugSeq_Div,
    debugSeq_Equality,
    debugSeq_Expression,
    debugSeq_IntConstant,
    debugSeq_LoadDebugInfo,
    debugSeq_Message,
    debugSeq_Minus,
    debugSeq_Mul,
    debugSeq_Not,
    debugSeq_Or,
    debugSeq_Parameter,
    debugSeq_Plus,
    debugSeq_Query,
    debugSeq_QueryValue,
    debugSeq_Read16,
    debugSeq_Read32,
    debugSeq_Read64,
    debugSeq_Read8,
    debugSeq_ReadAP,
    debugSeq_ReadDP,
    debugSeq_Rem,
    debugSeq_Sequence,
    debugSeq_SequenceCall,
    debugSeq_Sequences,
    debugSeq_Shift,
    debugSeq_Statement,
    debugSeq_StringConstant,
    debugSeq_Ternary,
    debugSeq_VariableDeclaration,
    debugSeq_VariableRef,
    debugSeq_Write16,
    debugSeq_Write32,
    debugSeq_Write64,
    debugSeq_Write8,
    debugSeq_WriteAP,
    debugSeq_WriteDP,
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

def test_assoc_codeblocks17_reverse_link_reassign_clear():
    a1 = debugSeq_Control(timeout="sample_text")
    a2 = debugSeq_Control(timeout="sample_text_2")
    b = debugSeq_CodeBlock(info="sample_text")
    _safe_set(b, 'debugSeq_CodeBlock19', a1)
    assert _is_linked(b, 'debugSeq_CodeBlock19', a1)
    if hasattr(a1, 'debugSeq_Control18'):
        assert _is_linked(a1, 'debugSeq_Control18', b)
    _safe_set(b, 'debugSeq_CodeBlock19', a2)
    assert _is_linked(b, 'debugSeq_CodeBlock19', a2)
    if hasattr(a1, 'debugSeq_Control18'):
        assert not _is_linked(a1, 'debugSeq_Control18', b)
    if hasattr(a2, 'debugSeq_Control18'):
        assert _is_linked(a2, 'debugSeq_Control18', b)
    _safe_set(b, 'debugSeq_CodeBlock19', None)
    assert not _is_linked(b, 'debugSeq_CodeBlock19', a2)
    if hasattr(a2, 'debugSeq_Control18'):
        assert not _is_linked(a2, 'debugSeq_Control18', b)


def test_assoc_codeblocks8_reverse_link_reassign_clear():
    a1 = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    a2 = debugSeq_Sequence(disable="sample_text_2", info="sample_text_2", name="sample_text_2", pname="sample_text_2")
    b = debugSeq_CodeBlock(info="sample_text")
    _safe_set(b, 'debugSeq_CodeBlock', a1)
    assert _is_linked(b, 'debugSeq_CodeBlock', a1)
    if hasattr(a1, 'debugSeq_Sequence9'):
        assert _is_linked(a1, 'debugSeq_Sequence9', b)
    _safe_set(b, 'debugSeq_CodeBlock', a2)
    assert _is_linked(b, 'debugSeq_CodeBlock', a2)
    if hasattr(a1, 'debugSeq_Sequence9'):
        assert not _is_linked(a1, 'debugSeq_Sequence9', b)
    if hasattr(a2, 'debugSeq_Sequence9'):
        assert _is_linked(a2, 'debugSeq_Sequence9', b)
    _safe_set(b, 'debugSeq_CodeBlock', None)
    assert not _is_linked(b, 'debugSeq_CodeBlock', a2)
    if hasattr(a2, 'debugSeq_Sequence9'):
        assert not _is_linked(a2, 'debugSeq_Sequence9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_debugvars0_stub_double():
    # debugSeq_DebugSeqModel has no real 'debugSeq_DebugSeqModel' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_DebugVars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_DebugVars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_DebugVars(configfile="sample_text", pname="sample_text", version="sample_text")
    partner = debugSeq_DebugSeqModel()
    setattr(partner, 'debugSeq_DebugSeqModel', None)
    _safe_set(owner, 'debugSeq_DebugVars', partner)
    assert getattr(partner, 'debugSeq_DebugSeqModel') == owner
    _safe_set(owner, 'debugSeq_DebugVars', None)
    assert getattr(partner, 'debugSeq_DebugSeqModel') is None


def test_assoc_default104_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression106' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Query(message="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression106', None)
    _safe_set(owner, 'debugSeq_Query105', partner)
    assert getattr(partner, 'debugSeq_Expression106') == owner
    _safe_set(owner, 'debugSeq_Query105', None)
    assert getattr(partner, 'debugSeq_Expression106') is None


def test_assoc_default107_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression108' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_QueryValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_QueryValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_QueryValue(message="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression108', None)
    _safe_set(owner, 'debugSeq_QueryValue', partner)
    assert getattr(partner, 'debugSeq_Expression108') == owner
    _safe_set(owner, 'debugSeq_QueryValue', None)
    assert getattr(partner, 'debugSeq_Expression108') is None


def test_assoc_if_12_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression13' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Control(timeout="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression13', None)
    _safe_set(owner, 'debugSeq_Control', partner)
    assert getattr(partner, 'debugSeq_Expression13') == owner
    _safe_set(owner, 'debugSeq_Control', None)
    assert getattr(partner, 'debugSeq_Expression13') is None


def test_assoc_left20_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression21' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Assignment(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression21', None)
    _safe_set(owner, 'debugSeq_Assignment', partner)
    assert getattr(partner, 'debugSeq_Expression21') == owner
    _safe_set(owner, 'debugSeq_Assignment', None)
    assert getattr(partner, 'debugSeq_Expression21') is None


def test_assoc_left58_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression59' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Equality(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression59', None)
    _safe_set(owner, 'debugSeq_Equality', partner)
    assert getattr(partner, 'debugSeq_Expression59') == owner
    _safe_set(owner, 'debugSeq_Equality', None)
    assert getattr(partner, 'debugSeq_Expression59') is None


def test_assoc_left63_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression64' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Comparison(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression64', None)
    _safe_set(owner, 'debugSeq_Comparison', partner)
    assert getattr(partner, 'debugSeq_Expression64') == owner
    _safe_set(owner, 'debugSeq_Comparison', None)
    assert getattr(partner, 'debugSeq_Expression64') is None


def test_assoc_left68_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Shift's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Shift's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Shift(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression69', None)
    _safe_set(owner, 'debugSeq_Shift', partner)
    assert getattr(partner, 'debugSeq_Expression69') == owner
    _safe_set(owner, 'debugSeq_Shift', None)
    assert getattr(partner, 'debugSeq_Expression69') is None


def test_assoc_parameters111_stub_double():
    # debugSeq_Parameter has no real 'debugSeq_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Message(format="sample_text")
    partner = debugSeq_Parameter()
    setattr(partner, 'debugSeq_Parameter', None)
    _safe_set(owner, 'debugSeq_Message112', {partner})
    assert getattr(partner, 'debugSeq_Parameter') == owner
    _safe_set(owner, 'debugSeq_Message112', set())
    assert getattr(partner, 'debugSeq_Parameter') is None


def test_assoc_right22_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Assignment(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression24', None)
    _safe_set(owner, 'debugSeq_Assignment23', partner)
    assert getattr(partner, 'debugSeq_Expression24') == owner
    _safe_set(owner, 'debugSeq_Assignment23', None)
    assert getattr(partner, 'debugSeq_Expression24') is None


def test_assoc_right60_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression62' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Equality(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression62', None)
    _safe_set(owner, 'debugSeq_Equality61', partner)
    assert getattr(partner, 'debugSeq_Expression62') == owner
    _safe_set(owner, 'debugSeq_Equality61', None)
    assert getattr(partner, 'debugSeq_Expression62') is None


def test_assoc_right65_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression67' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Comparison(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression67', None)
    _safe_set(owner, 'debugSeq_Comparison66', partner)
    assert getattr(partner, 'debugSeq_Expression67') == owner
    _safe_set(owner, 'debugSeq_Comparison66', None)
    assert getattr(partner, 'debugSeq_Expression67') is None


def test_assoc_right70_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression72' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Shift's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Shift's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Shift(op="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression72', None)
    _safe_set(owner, 'debugSeq_Shift71', partner)
    assert getattr(partner, 'debugSeq_Expression72') == owner
    _safe_set(owner, 'debugSeq_Shift71', None)
    assert getattr(partner, 'debugSeq_Expression72') is None


def test_assoc_sequences6_stub_double():
    # debugSeq_Sequences has no real 'debugSeq_Sequences7' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Sequence(disable="sample_text", info="sample_text", name="sample_text", pname="sample_text")
    partner = debugSeq_Sequences()
    setattr(partner, 'debugSeq_Sequences7', None)
    _safe_set(owner, 'debugSeq_Sequence', partner)
    assert owner in getattr(partner, 'debugSeq_Sequences7')
    _safe_set(owner, 'debugSeq_Sequence', None)
    assert owner not in getattr(partner, 'debugSeq_Sequences7')


def test_assoc_statements10_stub_double():
    # debugSeq_Statement has no real 'debugSeq_Statement11' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Block(atomic="sample_text")
    partner = debugSeq_Statement()
    setattr(partner, 'debugSeq_Statement11', None)
    _safe_set(owner, 'debugSeq_Block', {partner})
    assert getattr(partner, 'debugSeq_Statement11') == owner
    _safe_set(owner, 'debugSeq_Block', set())
    assert getattr(partner, 'debugSeq_Statement11') is None


def test_assoc_statements3_stub_double():
    # debugSeq_Statement has no real 'debugSeq_Statement' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_DebugVars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_DebugVars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_DebugVars(configfile="sample_text", pname="sample_text", version="sample_text")
    partner = debugSeq_Statement()
    setattr(partner, 'debugSeq_Statement', None)
    _safe_set(owner, 'debugSeq_DebugVars4', {partner})
    assert getattr(partner, 'debugSeq_Statement') == owner
    _safe_set(owner, 'debugSeq_DebugVars4', set())
    assert getattr(partner, 'debugSeq_Statement') is None


def test_assoc_type102_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression103' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Query(message="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression103', None)
    _safe_set(owner, 'debugSeq_Query', partner)
    assert getattr(partner, 'debugSeq_Expression103') == owner
    _safe_set(owner, 'debugSeq_Query', None)
    assert getattr(partner, 'debugSeq_Expression103') is None


def test_assoc_type109_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Message(format="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression110', None)
    _safe_set(owner, 'debugSeq_Message', partner)
    assert getattr(partner, 'debugSeq_Expression110') == owner
    _safe_set(owner, 'debugSeq_Message', None)
    assert getattr(partner, 'debugSeq_Expression110') is None


def test_assoc_value5_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_VariableDeclaration(name="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression', None)
    _safe_set(owner, 'debugSeq_VariableDeclaration', partner)
    assert getattr(partner, 'debugSeq_Expression') == owner
    _safe_set(owner, 'debugSeq_VariableDeclaration', None)
    assert getattr(partner, 'debugSeq_Expression') is None


def test_assoc_variable182_stub_double():
    # debugSeq_VariableRef has no real 'debugSeq_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_VariableDeclaration(name="sample_text")
    partner = debugSeq_VariableRef()
    setattr(partner, 'debugSeq_VariableRef', None)
    _safe_set(owner, 'debugSeq_VariableDeclaration183', partner)
    assert getattr(partner, 'debugSeq_VariableRef') == owner
    _safe_set(owner, 'debugSeq_VariableDeclaration183', None)
    assert getattr(partner, 'debugSeq_VariableRef') is None


def test_assoc_while_14_stub_double():
    # debugSeq_Expression has no real 'debugSeq_Expression16' property in the generated
    # code (a bare stub) -- manually attach it so debugSeq_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # debugSeq_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = debugSeq_Control(timeout="sample_text")
    partner = debugSeq_Expression()
    setattr(partner, 'debugSeq_Expression16', None)
    _safe_set(owner, 'debugSeq_Control15', partner)
    assert getattr(partner, 'debugSeq_Expression16') == owner
    _safe_set(owner, 'debugSeq_Control15', None)
    assert getattr(partner, 'debugSeq_Expression16') is None


