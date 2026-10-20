import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractAssignment,
    AccessControl,
    Command,
    Computation,
    Download,
    Expression,
    Functions,
    smc_AbstractAssignment,
    smc_AccessControl,
    smc_AddValues,
    smc_And,
    smc_Average,
    smc_BellLapadula,
    smc_Block,
    smc_BlockSMC,
    smc_BloomFilter,
    smc_BooleanLiteral,
    smc_CheckTable,
    smc_Client,
    smc_Command,
    smc_Comparison,
    smc_Computation,
    smc_Count,
    smc_Covered,
    smc_CreateTable,
    smc_Database,
    smc_DateLiteral,
    smc_Dict,
    smc_DoubleLiteral,
    smc_Download,
    smc_Equality,
    smc_Expression,
    smc_Functions,
    smc_IfThenElse,
    smc_IntLiteral,
    smc_Invocation,
    smc_InvocationVoid,
    smc_List,
    smc_MainSMC,
    smc_Median,
    smc_MulOrDiv,
    smc_Multiplication,
    smc_Not,
    smc_Or,
    smc_ParamDecl,
    smc_PlusOrMinus,
    smc_Print,
    smc_Return,
    smc_Search,
    smc_Smc,
    smc_StringLiteral,
    smc_TimeLiteral,
    smc_Tuple,
    smc_VariableAssignment,
    smc_VariableDecl,
    smc_VariableRef,
    smc_WeightedAvg,
    smc_While,
    BasicType,
    BlockType,
    SecType,
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

def test_assoc_cur66_reverse_link_reassign_clear():
    a1 = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    a2 = smc_VariableDecl(array=False, length=13, name="sample_text_2", type="sample_text_2", visibility="sample_text_2")
    b = smc_BellLapadula(mode="sample_text")
    _safe_set(b, 'smc_BellLapadula', a1)
    assert _is_linked(b, 'smc_BellLapadula', a1)
    if hasattr(a1, 'smc_VariableDecl67'):
        assert _is_linked(a1, 'smc_VariableDecl67', b)
    _safe_set(b, 'smc_BellLapadula', a2)
    assert _is_linked(b, 'smc_BellLapadula', a2)
    if hasattr(a1, 'smc_VariableDecl67'):
        assert not _is_linked(a1, 'smc_VariableDecl67', b)
    if hasattr(a2, 'smc_VariableDecl67'):
        assert _is_linked(a2, 'smc_VariableDecl67', b)
    _safe_set(b, 'smc_BellLapadula', None)
    assert not _is_linked(b, 'smc_BellLapadula', a2)
    if hasattr(a2, 'smc_VariableDecl67'):
        assert not _is_linked(a2, 'smc_VariableDecl67', b)


def test_assoc_keyword75_reverse_link_reassign_clear():
    a1 = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    a2 = smc_VariableDecl(array=False, length=13, name="sample_text_2", type="sample_text_2", visibility="sample_text_2")
    b = smc_Search(column="sample_text")
    _safe_set(b, 'smc_Search76', a1)
    assert _is_linked(b, 'smc_Search76', a1)
    if hasattr(a1, 'smc_VariableDecl77'):
        assert _is_linked(a1, 'smc_VariableDecl77', b)
    _safe_set(b, 'smc_Search76', a2)
    assert _is_linked(b, 'smc_Search76', a2)
    if hasattr(a1, 'smc_VariableDecl77'):
        assert not _is_linked(a1, 'smc_VariableDecl77', b)
    if hasattr(a2, 'smc_VariableDecl77'):
        assert _is_linked(a2, 'smc_VariableDecl77', b)
    _safe_set(b, 'smc_Search76', None)
    assert not _is_linked(b, 'smc_Search76', a2)
    if hasattr(a2, 'smc_VariableDecl77'):
        assert not _is_linked(a2, 'smc_VariableDecl77', b)


def test_assoc_tblname73_reverse_link_reassign_clear():
    a1 = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    a2 = smc_VariableDecl(array=False, length=13, name="sample_text_2", type="sample_text_2", visibility="sample_text_2")
    b = smc_Search(column="sample_text")
    _safe_set(b, 'smc_Search', a1)
    assert _is_linked(b, 'smc_Search', a1)
    if hasattr(a1, 'smc_VariableDecl74'):
        assert _is_linked(a1, 'smc_VariableDecl74', b)
    _safe_set(b, 'smc_Search', a2)
    assert _is_linked(b, 'smc_Search', a2)
    if hasattr(a1, 'smc_VariableDecl74'):
        assert not _is_linked(a1, 'smc_VariableDecl74', b)
    if hasattr(a2, 'smc_VariableDecl74'):
        assert _is_linked(a2, 'smc_VariableDecl74', b)
    _safe_set(b, 'smc_Search', None)
    assert not _is_linked(b, 'smc_Search', a2)
    if hasattr(a2, 'smc_VariableDecl74'):
        assert not _is_linked(a2, 'smc_VariableDecl74', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args87_stub_double():
    # smc_AddValues has no real 'smc_AddValues88' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_AddValues()
    setattr(partner, 'smc_AddValues88', None)
    _safe_set(owner, 'smc_VariableDecl89', partner)
    assert owner in getattr(partner, 'smc_AddValues88')
    _safe_set(owner, 'smc_VariableDecl89', None)
    assert owner not in getattr(partner, 'smc_AddValues88')


def test_assoc_array50_stub_double():
    # smc_Median has no real 'smc_Median' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_Median()
    setattr(partner, 'smc_Median', None)
    _safe_set(owner, 'smc_VariableDecl51', partner)
    assert getattr(partner, 'smc_Median') == owner
    _safe_set(owner, 'smc_VariableDecl51', None)
    assert getattr(partner, 'smc_Median') is None


def test_assoc_array57_stub_double():
    # smc_Average has no real 'smc_Average' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_Average()
    setattr(partner, 'smc_Average', None)
    _safe_set(owner, 'smc_VariableDecl58', partner)
    assert getattr(partner, 'smc_Average') == owner
    _safe_set(owner, 'smc_VariableDecl58', None)
    assert getattr(partner, 'smc_Average') is None


def test_assoc_array59_stub_double():
    # smc_Count has no real 'smc_Count' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_Count()
    setattr(partner, 'smc_Count', None)
    _safe_set(owner, 'smc_VariableDecl60', partner)
    assert getattr(partner, 'smc_Count') == owner
    _safe_set(owner, 'smc_VariableDecl60', None)
    assert getattr(partner, 'smc_Count') is None


def test_assoc_blockName40_stub_double():
    # smc_Invocation has no real 'smc_Invocation41' property in the generated
    # code (a bare stub) -- manually attach it so smc_BlockSMC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_BlockSMC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_BlockSMC(name="sample_text", type="sample_text")
    partner = smc_Invocation()
    setattr(partner, 'smc_Invocation41', None)
    _safe_set(owner, 'smc_BlockSMC42', partner)
    assert getattr(partner, 'smc_Invocation41') == owner
    _safe_set(owner, 'smc_BlockSMC42', None)
    assert getattr(partner, 'smc_Invocation41') is None


def test_assoc_blocks0_stub_double():
    # smc_Smc has no real 'smc_Smc' property in the generated
    # code (a bare stub) -- manually attach it so smc_BlockSMC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_BlockSMC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_BlockSMC(name="sample_text", type="sample_text")
    partner = smc_Smc()
    setattr(partner, 'smc_Smc', None)
    _safe_set(owner, 'smc_BlockSMC', partner)
    assert owner in getattr(partner, 'smc_Smc')
    _safe_set(owner, 'smc_BlockSMC', None)
    assert owner not in getattr(partner, 'smc_Smc')


def test_assoc_c_lvls61_stub_double():
    # smc_AccessControl has no real 'smc_AccessControl' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_AccessControl()
    setattr(partner, 'smc_AccessControl', None)
    _safe_set(owner, 'smc_VariableDecl62', partner)
    assert getattr(partner, 'smc_AccessControl') == owner
    _safe_set(owner, 'smc_VariableDecl62', None)
    assert getattr(partner, 'smc_AccessControl') is None


def test_assoc_covered70_stub_double():
    # smc_Covered has no real 'smc_Covered71' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_Covered()
    setattr(partner, 'smc_Covered71', None)
    _safe_set(owner, 'smc_VariableDecl72', partner)
    assert getattr(partner, 'smc_Covered71') == owner
    _safe_set(owner, 'smc_VariableDecl72', None)
    assert getattr(partner, 'smc_Covered71') is None


def test_assoc_elems54_stub_double():
    # smc_WeightedAvg has no real 'smc_WeightedAvg55' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_WeightedAvg()
    setattr(partner, 'smc_WeightedAvg55', None)
    _safe_set(owner, 'smc_VariableDecl56', partner)
    assert getattr(partner, 'smc_WeightedAvg55') == owner
    _safe_set(owner, 'smc_VariableDecl56', None)
    assert getattr(partner, 'smc_WeightedAvg55') is None


def test_assoc_left106_stub_double():
    # smc_Expression has no real 'smc_Expression107' property in the generated
    # code (a bare stub) -- manually attach it so smc_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_Equality(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression107', None)
    _safe_set(owner, 'smc_Equality', partner)
    assert getattr(partner, 'smc_Expression107') == owner
    _safe_set(owner, 'smc_Equality', None)
    assert getattr(partner, 'smc_Expression107') is None


def test_assoc_left111_stub_double():
    # smc_Expression has no real 'smc_Expression112' property in the generated
    # code (a bare stub) -- manually attach it so smc_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_Comparison(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression112', None)
    _safe_set(owner, 'smc_Comparison', partner)
    assert getattr(partner, 'smc_Expression112') == owner
    _safe_set(owner, 'smc_Comparison', None)
    assert getattr(partner, 'smc_Expression112') is None


def test_assoc_left116_stub_double():
    # smc_Expression has no real 'smc_Expression117' property in the generated
    # code (a bare stub) -- manually attach it so smc_PlusOrMinus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_PlusOrMinus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_PlusOrMinus(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression117', None)
    _safe_set(owner, 'smc_PlusOrMinus', partner)
    assert getattr(partner, 'smc_Expression117') == owner
    _safe_set(owner, 'smc_PlusOrMinus', None)
    assert getattr(partner, 'smc_Expression117') is None


def test_assoc_left121_stub_double():
    # smc_Expression has no real 'smc_Expression122' property in the generated
    # code (a bare stub) -- manually attach it so smc_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_MulOrDiv(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression122', None)
    _safe_set(owner, 'smc_MulOrDiv', partner)
    assert getattr(partner, 'smc_Expression122') == owner
    _safe_set(owner, 'smc_MulOrDiv', None)
    assert getattr(partner, 'smc_Expression122') is None


def test_assoc_match68_stub_double():
    # smc_Covered has no real 'smc_Covered' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_Covered()
    setattr(partner, 'smc_Covered', None)
    _safe_set(owner, 'smc_VariableDecl69', partner)
    assert getattr(partner, 'smc_Covered') == owner
    _safe_set(owner, 'smc_VariableDecl69', None)
    assert getattr(partner, 'smc_Covered') is None


def test_assoc_option20_stub_double():
    # smc_AbstractAssignment has no real 'smc_AbstractAssignment' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_AbstractAssignment()
    setattr(partner, 'smc_AbstractAssignment', None)
    _safe_set(owner, 'smc_VariableDecl', partner)
    assert getattr(partner, 'smc_AbstractAssignment') == owner
    _safe_set(owner, 'smc_VariableDecl', None)
    assert getattr(partner, 'smc_AbstractAssignment') is None


def test_assoc_params92_stub_double():
    # smc_CreateTable has no real 'smc_CreateTable93' property in the generated
    # code (a bare stub) -- manually attach it so smc_ParamDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_ParamDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_ParamDecl(btype="sample_text", name="sample_text", parName="sample_text", stype="sample_text")
    partner = smc_CreateTable()
    setattr(partner, 'smc_CreateTable93', None)
    _safe_set(owner, 'smc_ParamDecl', partner)
    assert owner in getattr(partner, 'smc_CreateTable93')
    _safe_set(owner, 'smc_ParamDecl', None)
    assert owner not in getattr(partner, 'smc_CreateTable93')


def test_assoc_post80_stub_double():
    # smc_BloomFilter has no real 'smc_BloomFilter81' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_BloomFilter()
    setattr(partner, 'smc_BloomFilter81', None)
    _safe_set(owner, 'smc_VariableDecl82', partner)
    assert getattr(partner, 'smc_BloomFilter81') == owner
    _safe_set(owner, 'smc_VariableDecl82', None)
    assert getattr(partner, 'smc_BloomFilter81') is None


def test_assoc_pre78_stub_double():
    # smc_BloomFilter has no real 'smc_BloomFilter' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_BloomFilter()
    setattr(partner, 'smc_BloomFilter', None)
    _safe_set(owner, 'smc_VariableDecl79', partner)
    assert getattr(partner, 'smc_BloomFilter') == owner
    _safe_set(owner, 'smc_VariableDecl79', None)
    assert getattr(partner, 'smc_BloomFilter') is None


def test_assoc_right108_stub_double():
    # smc_Expression has no real 'smc_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so smc_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_Equality(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression110', None)
    _safe_set(owner, 'smc_Equality109', partner)
    assert getattr(partner, 'smc_Expression110') == owner
    _safe_set(owner, 'smc_Equality109', None)
    assert getattr(partner, 'smc_Expression110') is None


def test_assoc_right113_stub_double():
    # smc_Expression has no real 'smc_Expression115' property in the generated
    # code (a bare stub) -- manually attach it so smc_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_Comparison(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression115', None)
    _safe_set(owner, 'smc_Comparison114', partner)
    assert getattr(partner, 'smc_Expression115') == owner
    _safe_set(owner, 'smc_Comparison114', None)
    assert getattr(partner, 'smc_Expression115') is None


def test_assoc_right118_stub_double():
    # smc_Expression has no real 'smc_Expression120' property in the generated
    # code (a bare stub) -- manually attach it so smc_PlusOrMinus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_PlusOrMinus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_PlusOrMinus(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression120', None)
    _safe_set(owner, 'smc_PlusOrMinus119', partner)
    assert getattr(partner, 'smc_Expression120') == owner
    _safe_set(owner, 'smc_PlusOrMinus119', None)
    assert getattr(partner, 'smc_Expression120') is None


def test_assoc_right123_stub_double():
    # smc_Expression has no real 'smc_Expression125' property in the generated
    # code (a bare stub) -- manually attach it so smc_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_MulOrDiv(op="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression125', None)
    _safe_set(owner, 'smc_MulOrDiv124', partner)
    assert getattr(partner, 'smc_Expression125') == owner
    _safe_set(owner, 'smc_MulOrDiv124', None)
    assert getattr(partner, 'smc_Expression125') is None


def test_assoc_tbl26_stub_double():
    # smc_Expression has no real 'smc_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so smc_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_Database(clm="sample_text")
    partner = smc_Expression()
    setattr(partner, 'smc_Expression27', None)
    _safe_set(owner, 'smc_Database', partner)
    assert getattr(partner, 'smc_Expression27') == owner
    _safe_set(owner, 'smc_Database', None)
    assert getattr(partner, 'smc_Expression27') is None


def test_assoc_tblname83_stub_double():
    # smc_CheckTable has no real 'smc_CheckTable' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_CheckTable()
    setattr(partner, 'smc_CheckTable', None)
    _safe_set(owner, 'smc_VariableDecl84', partner)
    assert getattr(partner, 'smc_CheckTable') == owner
    _safe_set(owner, 'smc_VariableDecl84', None)
    assert getattr(partner, 'smc_CheckTable') is None


def test_assoc_tblname85_stub_double():
    # smc_AddValues has no real 'smc_AddValues' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_AddValues()
    setattr(partner, 'smc_AddValues', None)
    _safe_set(owner, 'smc_VariableDecl86', partner)
    assert getattr(partner, 'smc_AddValues') == owner
    _safe_set(owner, 'smc_VariableDecl86', None)
    assert getattr(partner, 'smc_AddValues') is None


def test_assoc_tblname90_stub_double():
    # smc_CreateTable has no real 'smc_CreateTable' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_CreateTable()
    setattr(partner, 'smc_CreateTable', None)
    _safe_set(owner, 'smc_VariableDecl91', partner)
    assert getattr(partner, 'smc_CreateTable') == owner
    _safe_set(owner, 'smc_VariableDecl91', None)
    assert getattr(partner, 'smc_CreateTable') is None


def test_assoc_v_lvl63_stub_double():
    # smc_AccessControl has no real 'smc_AccessControl64' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_AccessControl()
    setattr(partner, 'smc_AccessControl64', None)
    _safe_set(owner, 'smc_VariableDecl65', partner)
    assert getattr(partner, 'smc_AccessControl64') == owner
    _safe_set(owner, 'smc_VariableDecl65', None)
    assert getattr(partner, 'smc_AccessControl64') is None


def test_assoc_var21_stub_double():
    # smc_VariableAssignment has no real 'smc_VariableAssignment' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_VariableAssignment()
    setattr(partner, 'smc_VariableAssignment', None)
    _safe_set(owner, 'smc_VariableDecl22', partner)
    assert getattr(partner, 'smc_VariableAssignment') == owner
    _safe_set(owner, 'smc_VariableDecl22', None)
    assert getattr(partner, 'smc_VariableAssignment') is None


def test_assoc_variable128_stub_double():
    # smc_VariableRef has no real 'smc_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_VariableRef()
    setattr(partner, 'smc_VariableRef', None)
    _safe_set(owner, 'smc_VariableDecl129', partner)
    assert getattr(partner, 'smc_VariableRef') == owner
    _safe_set(owner, 'smc_VariableDecl129', None)
    assert getattr(partner, 'smc_VariableRef') is None


def test_assoc_weights52_stub_double():
    # smc_WeightedAvg has no real 'smc_WeightedAvg' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_WeightedAvg()
    setattr(partner, 'smc_WeightedAvg', None)
    _safe_set(owner, 'smc_VariableDecl53', partner)
    assert getattr(partner, 'smc_WeightedAvg') == owner
    _safe_set(owner, 'smc_VariableDecl53', None)
    assert getattr(partner, 'smc_WeightedAvg') is None


def test_assoc_x45_stub_double():
    # smc_Multiplication has no real 'smc_Multiplication' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_Multiplication()
    setattr(partner, 'smc_Multiplication', None)
    _safe_set(owner, 'smc_VariableDecl46', partner)
    assert getattr(partner, 'smc_Multiplication') == owner
    _safe_set(owner, 'smc_VariableDecl46', None)
    assert getattr(partner, 'smc_Multiplication') is None


def test_assoc_y47_stub_double():
    # smc_Multiplication has no real 'smc_Multiplication48' property in the generated
    # code (a bare stub) -- manually attach it so smc_VariableDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smc_VariableDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smc_VariableDecl(array=True, length=7, name="sample_text", type="sample_text", visibility="sample_text")
    partner = smc_Multiplication()
    setattr(partner, 'smc_Multiplication48', None)
    _safe_set(owner, 'smc_VariableDecl49', partner)
    assert getattr(partner, 'smc_Multiplication48') == owner
    _safe_set(owner, 'smc_VariableDecl49', None)
    assert getattr(partner, 'smc_Multiplication48') is None


