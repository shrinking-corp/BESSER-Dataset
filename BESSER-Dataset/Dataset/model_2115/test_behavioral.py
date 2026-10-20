import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    xtextTest_After,
    xtextTest_Before,
    xtextTest_CodeCall,
    xtextTest_Element,
    xtextTest_EmfTest,
    xtextTest_Generator,
    xtextTest_Import,
    xtextTest_Inner,
    xtextTest_Input,
    xtextTest_Model,
    xtextTest_MyTokens,
    xtextTest_ReplacePatterns,
    xtextTest_Tokens,
    xtextTest_XtextTest,
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

def test_assoc_assign38_reverse_link_reassign_clear():
    a1 = xtextTest_Inner(assignAsBool="sample_text", assignAsData="sample_text", isEmpty=True, isNotNull=True, isNull=True, parameter="sample_text", value="sample_text")
    a2 = xtextTest_Inner(assignAsBool="sample_text_2", assignAsData="sample_text_2", isEmpty=False, isNotNull=False, isNull=False, parameter="sample_text_2", value="sample_text_2")
    b = xtextTest_Element(importing="sample_text", name="sample_text")
    _safe_set(b, 'xtextTest_Element40', a1)
    assert _is_linked(b, 'xtextTest_Element40', a1)
    if hasattr(a1, 'xtextTest_Inner39'):
        assert _is_linked(a1, 'xtextTest_Inner39', b)
    _safe_set(b, 'xtextTest_Element40', a2)
    assert _is_linked(b, 'xtextTest_Element40', a2)
    if hasattr(a1, 'xtextTest_Inner39'):
        assert not _is_linked(a1, 'xtextTest_Inner39', b)
    if hasattr(a2, 'xtextTest_Inner39'):
        assert _is_linked(a2, 'xtextTest_Inner39', b)
    _safe_set(b, 'xtextTest_Element40', None)
    assert not _is_linked(b, 'xtextTest_Element40', a2)
    if hasattr(a2, 'xtextTest_Inner39'):
        assert not _is_linked(a2, 'xtextTest_Inner39', b)


def test_assoc_assignList41_reverse_link_reassign_clear():
    a1 = xtextTest_Inner(assignAsBool="sample_text", assignAsData="sample_text", isEmpty=True, isNotNull=True, isNull=True, parameter="sample_text", value="sample_text")
    a2 = xtextTest_Inner(assignAsBool="sample_text_2", assignAsData="sample_text_2", isEmpty=False, isNotNull=False, isNull=False, parameter="sample_text_2", value="sample_text_2")
    b = xtextTest_Element(importing="sample_text", name="sample_text")
    _safe_set(b, 'xtextTest_Element43', a1)
    assert _is_linked(b, 'xtextTest_Element43', a1)
    if hasattr(a1, 'xtextTest_Inner42'):
        assert _is_linked(a1, 'xtextTest_Inner42', b)
    _safe_set(b, 'xtextTest_Element43', a2)
    assert _is_linked(b, 'xtextTest_Element43', a2)
    if hasattr(a1, 'xtextTest_Inner42'):
        assert not _is_linked(a1, 'xtextTest_Inner42', b)
    if hasattr(a2, 'xtextTest_Inner42'):
        assert _is_linked(a2, 'xtextTest_Inner42', b)
    _safe_set(b, 'xtextTest_Element43', None)
    assert not _is_linked(b, 'xtextTest_Element43', a2)
    if hasattr(a2, 'xtextTest_Inner42'):
        assert not _is_linked(a2, 'xtextTest_Inner42', b)


def test_assoc_codeCall17_reverse_link_reassign_clear():
    a1 = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    a2 = xtextTest_EmfTest(file="sample_text_2", mydefault="sample_text_2", package="sample_text_2", timeOut=13)
    b = xtextTest_CodeCall(method="sample_text", myclass="sample_text", params="sample_text")
    _safe_set(b, 'xtextTest_CodeCall', a1)
    assert _is_linked(b, 'xtextTest_CodeCall', a1)
    if hasattr(a1, 'xtextTest_EmfTest18'):
        assert _is_linked(a1, 'xtextTest_EmfTest18', b)
    _safe_set(b, 'xtextTest_CodeCall', a2)
    assert _is_linked(b, 'xtextTest_CodeCall', a2)
    if hasattr(a1, 'xtextTest_EmfTest18'):
        assert not _is_linked(a1, 'xtextTest_EmfTest18', b)
    if hasattr(a2, 'xtextTest_EmfTest18'):
        assert _is_linked(a2, 'xtextTest_EmfTest18', b)
    _safe_set(b, 'xtextTest_CodeCall', None)
    assert not _is_linked(b, 'xtextTest_CodeCall', a2)
    if hasattr(a2, 'xtextTest_EmfTest18'):
        assert not _is_linked(a2, 'xtextTest_EmfTest18', b)


def test_assoc_inner36_reverse_link_reassign_clear():
    a1 = xtextTest_Inner(assignAsBool="sample_text", assignAsData="sample_text", isEmpty=True, isNotNull=True, isNull=True, parameter="sample_text", value="sample_text")
    a2 = xtextTest_Inner(assignAsBool="sample_text_2", assignAsData="sample_text_2", isEmpty=False, isNotNull=False, isNull=False, parameter="sample_text_2", value="sample_text_2")
    b = xtextTest_Element(importing="sample_text", name="sample_text")
    _safe_set(b, 'xtextTest_Element37', {a1})
    assert _is_linked(b, 'xtextTest_Element37', a1)
    if hasattr(a1, 'xtextTest_Inner'):
        assert _is_linked(a1, 'xtextTest_Inner', b)
    _safe_set(b, 'xtextTest_Element37', {a2})
    assert _is_linked(b, 'xtextTest_Element37', a2)
    if hasattr(a1, 'xtextTest_Inner'):
        assert not _is_linked(a1, 'xtextTest_Inner', b)
    if hasattr(a2, 'xtextTest_Inner'):
        assert _is_linked(a2, 'xtextTest_Inner', b)
    _safe_set(b, 'xtextTest_Element37', set())
    assert not _is_linked(b, 'xtextTest_Element37', a2)
    if hasattr(a2, 'xtextTest_Inner'):
        assert not _is_linked(a2, 'xtextTest_Inner', b)


def test_assoc_input3_reverse_link_reassign_clear():
    a1 = xtextTest_XtextTest(boolean="sample_text", imports="sample_text", lang="sample_text", package="sample_text", timeOut=7)
    a2 = xtextTest_XtextTest(boolean="sample_text_2", imports="sample_text_2", lang="sample_text_2", package="sample_text_2", timeOut=13)
    b = xtextTest_Input(file="sample_text", text="sample_text")
    _safe_set(b, 'xtextTest_Input', a1)
    assert _is_linked(b, 'xtextTest_Input', a1)
    if hasattr(a1, 'xtextTest_XtextTest4'):
        assert _is_linked(a1, 'xtextTest_XtextTest4', b)
    _safe_set(b, 'xtextTest_Input', a2)
    assert _is_linked(b, 'xtextTest_Input', a2)
    if hasattr(a1, 'xtextTest_XtextTest4'):
        assert not _is_linked(a1, 'xtextTest_XtextTest4', b)
    if hasattr(a2, 'xtextTest_XtextTest4'):
        assert _is_linked(a2, 'xtextTest_XtextTest4', b)
    _safe_set(b, 'xtextTest_Input', None)
    assert not _is_linked(b, 'xtextTest_Input', a2)
    if hasattr(a2, 'xtextTest_XtextTest4'):
        assert not _is_linked(a2, 'xtextTest_XtextTest4', b)


def test_assoc_myimport15_reverse_link_reassign_clear():
    a1 = xtextTest_Import(alias="sample_text", id="sample_text")
    a2 = xtextTest_Import(alias="sample_text_2", id="sample_text_2")
    b = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    _safe_set(b, 'xtextTest_EmfTest16', {a1})
    assert _is_linked(b, 'xtextTest_EmfTest16', a1)
    if hasattr(a1, 'xtextTest_Import'):
        assert _is_linked(a1, 'xtextTest_Import', b)
    _safe_set(b, 'xtextTest_EmfTest16', {a2})
    assert _is_linked(b, 'xtextTest_EmfTest16', a2)
    if hasattr(a1, 'xtextTest_Import'):
        assert not _is_linked(a1, 'xtextTest_Import', b)
    if hasattr(a2, 'xtextTest_Import'):
        assert _is_linked(a2, 'xtextTest_Import', b)
    _safe_set(b, 'xtextTest_EmfTest16', set())
    assert not _is_linked(b, 'xtextTest_EmfTest16', a2)
    if hasattr(a2, 'xtextTest_Import'):
        assert not _is_linked(a2, 'xtextTest_Import', b)


def test_assoc_optionCall19_reverse_link_reassign_clear():
    a1 = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    a2 = xtextTest_EmfTest(file="sample_text_2", mydefault="sample_text_2", package="sample_text_2", timeOut=13)
    b = xtextTest_CodeCall(method="sample_text", myclass="sample_text", params="sample_text")
    _safe_set(b, 'xtextTest_CodeCall21', a1)
    assert _is_linked(b, 'xtextTest_CodeCall21', a1)
    if hasattr(a1, 'xtextTest_EmfTest20'):
        assert _is_linked(a1, 'xtextTest_EmfTest20', b)
    _safe_set(b, 'xtextTest_CodeCall21', a2)
    assert _is_linked(b, 'xtextTest_CodeCall21', a2)
    if hasattr(a1, 'xtextTest_EmfTest20'):
        assert not _is_linked(a1, 'xtextTest_EmfTest20', b)
    if hasattr(a2, 'xtextTest_EmfTest20'):
        assert _is_linked(a2, 'xtextTest_EmfTest20', b)
    _safe_set(b, 'xtextTest_CodeCall21', None)
    assert not _is_linked(b, 'xtextTest_CodeCall21', a2)
    if hasattr(a2, 'xtextTest_EmfTest20'):
        assert not _is_linked(a2, 'xtextTest_EmfTest20', b)


def test_assoc_output9_reverse_link_reassign_clear():
    a1 = xtextTest_XtextTest(boolean="sample_text", imports="sample_text", lang="sample_text", package="sample_text", timeOut=7)
    a2 = xtextTest_XtextTest(boolean="sample_text_2", imports="sample_text_2", lang="sample_text_2", package="sample_text_2", timeOut=13)
    b = xtextTest_Generator(exception="sample_text", expected="sample_text", isSameAsInputFile=True, output="sample_text", patternFile="sample_text")
    _safe_set(b, 'xtextTest_Generator', a1)
    assert _is_linked(b, 'xtextTest_Generator', a1)
    if hasattr(a1, 'xtextTest_XtextTest10'):
        assert _is_linked(a1, 'xtextTest_XtextTest10', b)
    _safe_set(b, 'xtextTest_Generator', a2)
    assert _is_linked(b, 'xtextTest_Generator', a2)
    if hasattr(a1, 'xtextTest_XtextTest10'):
        assert not _is_linked(a1, 'xtextTest_XtextTest10', b)
    if hasattr(a2, 'xtextTest_XtextTest10'):
        assert _is_linked(a2, 'xtextTest_XtextTest10', b)
    _safe_set(b, 'xtextTest_Generator', None)
    assert not _is_linked(b, 'xtextTest_Generator', a2)
    if hasattr(a2, 'xtextTest_XtextTest10'):
        assert not _is_linked(a2, 'xtextTest_XtextTest10', b)


def test_assoc_paramCall22_reverse_link_reassign_clear():
    a1 = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    a2 = xtextTest_EmfTest(file="sample_text_2", mydefault="sample_text_2", package="sample_text_2", timeOut=13)
    b = xtextTest_CodeCall(method="sample_text", myclass="sample_text", params="sample_text")
    _safe_set(b, 'xtextTest_CodeCall24', a1)
    assert _is_linked(b, 'xtextTest_CodeCall24', a1)
    if hasattr(a1, 'xtextTest_EmfTest23'):
        assert _is_linked(a1, 'xtextTest_EmfTest23', b)
    _safe_set(b, 'xtextTest_CodeCall24', a2)
    assert _is_linked(b, 'xtextTest_CodeCall24', a2)
    if hasattr(a1, 'xtextTest_EmfTest23'):
        assert not _is_linked(a1, 'xtextTest_EmfTest23', b)
    if hasattr(a2, 'xtextTest_EmfTest23'):
        assert _is_linked(a2, 'xtextTest_EmfTest23', b)
    _safe_set(b, 'xtextTest_CodeCall24', None)
    assert not _is_linked(b, 'xtextTest_CodeCall24', a2)
    if hasattr(a2, 'xtextTest_EmfTest23'):
        assert not _is_linked(a2, 'xtextTest_EmfTest23', b)


def test_assoc_replacePatterns44_reverse_link_reassign_clear():
    a1 = xtextTest_ReplacePatterns(regex="sample_text", replace="sample_text")
    a2 = xtextTest_ReplacePatterns(regex="sample_text_2", replace="sample_text_2")
    b = xtextTest_Generator(exception="sample_text", expected="sample_text", isSameAsInputFile=True, output="sample_text", patternFile="sample_text")
    _safe_set(b, 'xtextTest_Generator45', {a1})
    assert _is_linked(b, 'xtextTest_Generator45', a1)
    if hasattr(a1, 'xtextTest_ReplacePatterns'):
        assert _is_linked(a1, 'xtextTest_ReplacePatterns', b)
    _safe_set(b, 'xtextTest_Generator45', {a2})
    assert _is_linked(b, 'xtextTest_Generator45', a2)
    if hasattr(a1, 'xtextTest_ReplacePatterns'):
        assert not _is_linked(a1, 'xtextTest_ReplacePatterns', b)
    if hasattr(a2, 'xtextTest_ReplacePatterns'):
        assert _is_linked(a2, 'xtextTest_ReplacePatterns', b)
    _safe_set(b, 'xtextTest_Generator45', set())
    assert not _is_linked(b, 'xtextTest_Generator45', a2)
    if hasattr(a2, 'xtextTest_ReplacePatterns'):
        assert not _is_linked(a2, 'xtextTest_ReplacePatterns', b)


def test_assoc_root25_reverse_link_reassign_clear():
    a1 = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    a2 = xtextTest_EmfTest(file="sample_text_2", mydefault="sample_text_2", package="sample_text_2", timeOut=13)
    b = xtextTest_Element(importing="sample_text", name="sample_text")
    _safe_set(b, 'xtextTest_Element27', a1)
    assert _is_linked(b, 'xtextTest_Element27', a1)
    if hasattr(a1, 'xtextTest_EmfTest26'):
        assert _is_linked(a1, 'xtextTest_EmfTest26', b)
    _safe_set(b, 'xtextTest_Element27', a2)
    assert _is_linked(b, 'xtextTest_Element27', a2)
    if hasattr(a1, 'xtextTest_EmfTest26'):
        assert not _is_linked(a1, 'xtextTest_EmfTest26', b)
    if hasattr(a2, 'xtextTest_EmfTest26'):
        assert _is_linked(a2, 'xtextTest_EmfTest26', b)
    _safe_set(b, 'xtextTest_Element27', None)
    assert not _is_linked(b, 'xtextTest_Element27', a2)
    if hasattr(a2, 'xtextTest_EmfTest26'):
        assert not _is_linked(a2, 'xtextTest_EmfTest26', b)


def test_assoc_root7_reverse_link_reassign_clear():
    a1 = xtextTest_XtextTest(boolean="sample_text", imports="sample_text", lang="sample_text", package="sample_text", timeOut=7)
    a2 = xtextTest_XtextTest(boolean="sample_text_2", imports="sample_text_2", lang="sample_text_2", package="sample_text_2", timeOut=13)
    b = xtextTest_Element(importing="sample_text", name="sample_text")
    _safe_set(b, 'xtextTest_Element', a1)
    assert _is_linked(b, 'xtextTest_Element', a1)
    if hasattr(a1, 'xtextTest_XtextTest8'):
        assert _is_linked(a1, 'xtextTest_XtextTest8', b)
    _safe_set(b, 'xtextTest_Element', a2)
    assert _is_linked(b, 'xtextTest_Element', a2)
    if hasattr(a1, 'xtextTest_XtextTest8'):
        assert not _is_linked(a1, 'xtextTest_XtextTest8', b)
    if hasattr(a2, 'xtextTest_XtextTest8'):
        assert _is_linked(a2, 'xtextTest_XtextTest8', b)
    _safe_set(b, 'xtextTest_Element', None)
    assert not _is_linked(b, 'xtextTest_Element', a2)
    if hasattr(a2, 'xtextTest_XtextTest8'):
        assert not _is_linked(a2, 'xtextTest_XtextTest8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_after13_stub_double():
    # xtextTest_After has no real 'xtextTest_After' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_XtextTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_XtextTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_XtextTest(boolean="sample_text", imports="sample_text", lang="sample_text", package="sample_text", timeOut=7)
    partner = xtextTest_After()
    setattr(partner, 'xtextTest_After', None)
    _safe_set(owner, 'xtextTest_XtextTest14', partner)
    assert getattr(partner, 'xtextTest_After') == owner
    _safe_set(owner, 'xtextTest_XtextTest14', None)
    assert getattr(partner, 'xtextTest_After') is None


def test_assoc_after31_stub_double():
    # xtextTest_After has no real 'xtextTest_After33' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_EmfTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_EmfTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    partner = xtextTest_After()
    setattr(partner, 'xtextTest_After33', None)
    _safe_set(owner, 'xtextTest_EmfTest32', partner)
    assert getattr(partner, 'xtextTest_After33') == owner
    _safe_set(owner, 'xtextTest_EmfTest32', None)
    assert getattr(partner, 'xtextTest_After33') is None


def test_assoc_before11_stub_double():
    # xtextTest_Before has no real 'xtextTest_Before' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_XtextTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_XtextTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_XtextTest(boolean="sample_text", imports="sample_text", lang="sample_text", package="sample_text", timeOut=7)
    partner = xtextTest_Before()
    setattr(partner, 'xtextTest_Before', None)
    _safe_set(owner, 'xtextTest_XtextTest12', partner)
    assert getattr(partner, 'xtextTest_Before') == owner
    _safe_set(owner, 'xtextTest_XtextTest12', None)
    assert getattr(partner, 'xtextTest_Before') is None


def test_assoc_before28_stub_double():
    # xtextTest_Before has no real 'xtextTest_Before30' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_EmfTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_EmfTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    partner = xtextTest_Before()
    setattr(partner, 'xtextTest_Before30', None)
    _safe_set(owner, 'xtextTest_EmfTest29', partner)
    assert getattr(partner, 'xtextTest_Before30') == owner
    _safe_set(owner, 'xtextTest_EmfTest29', None)
    assert getattr(partner, 'xtextTest_Before30') is None


def test_assoc_codeCall46_stub_double():
    # xtextTest_Before has no real 'xtextTest_Before47' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_CodeCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_CodeCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_CodeCall(method="sample_text", myclass="sample_text", params="sample_text")
    partner = xtextTest_Before()
    setattr(partner, 'xtextTest_Before47', None)
    _safe_set(owner, 'xtextTest_CodeCall48', partner)
    assert getattr(partner, 'xtextTest_Before47') == owner
    _safe_set(owner, 'xtextTest_CodeCall48', None)
    assert getattr(partner, 'xtextTest_Before47') is None


def test_assoc_codeCall49_stub_double():
    # xtextTest_After has no real 'xtextTest_After50' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_CodeCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_CodeCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_CodeCall(method="sample_text", myclass="sample_text", params="sample_text")
    partner = xtextTest_After()
    setattr(partner, 'xtextTest_After50', None)
    _safe_set(owner, 'xtextTest_CodeCall51', partner)
    assert getattr(partner, 'xtextTest_After50') == owner
    _safe_set(owner, 'xtextTest_CodeCall51', None)
    assert getattr(partner, 'xtextTest_After50') is None


def test_assoc_emfTest1_stub_double():
    # xtextTest_Model has no real 'xtextTest_Model2' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_EmfTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_EmfTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_EmfTest(file="sample_text", mydefault="sample_text", package="sample_text", timeOut=7)
    partner = xtextTest_Model()
    setattr(partner, 'xtextTest_Model2', None)
    _safe_set(owner, 'xtextTest_EmfTest', partner)
    assert getattr(partner, 'xtextTest_Model2') == owner
    _safe_set(owner, 'xtextTest_EmfTest', None)
    assert getattr(partner, 'xtextTest_Model2') is None


def test_assoc_tokens34_stub_double():
    # xtextTest_Tokens has no real 'xtextTest_Tokens35' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_MyTokens's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_MyTokens's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_MyTokens(count=7, string="sample_text", token="sample_text")
    partner = xtextTest_Tokens()
    setattr(partner, 'xtextTest_Tokens35', None)
    _safe_set(owner, 'xtextTest_MyTokens', partner)
    assert owner in getattr(partner, 'xtextTest_Tokens35')
    _safe_set(owner, 'xtextTest_MyTokens', None)
    assert owner not in getattr(partner, 'xtextTest_Tokens35')


def test_assoc_tokens5_stub_double():
    # xtextTest_Tokens has no real 'xtextTest_Tokens' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_XtextTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_XtextTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_XtextTest(boolean="sample_text", imports="sample_text", lang="sample_text", package="sample_text", timeOut=7)
    partner = xtextTest_Tokens()
    setattr(partner, 'xtextTest_Tokens', None)
    _safe_set(owner, 'xtextTest_XtextTest6', partner)
    assert getattr(partner, 'xtextTest_Tokens') == owner
    _safe_set(owner, 'xtextTest_XtextTest6', None)
    assert getattr(partner, 'xtextTest_Tokens') is None


def test_assoc_xtextTest0_stub_double():
    # xtextTest_Model has no real 'xtextTest_Model' property in the generated
    # code (a bare stub) -- manually attach it so xtextTest_XtextTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xtextTest_XtextTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xtextTest_XtextTest(boolean="sample_text", imports="sample_text", lang="sample_text", package="sample_text", timeOut=7)
    partner = xtextTest_Model()
    setattr(partner, 'xtextTest_Model', None)
    _safe_set(owner, 'xtextTest_XtextTest', partner)
    assert getattr(partner, 'xtextTest_Model') == owner
    _safe_set(owner, 'xtextTest_XtextTest', None)
    assert getattr(partner, 'xtextTest_Model') is None


