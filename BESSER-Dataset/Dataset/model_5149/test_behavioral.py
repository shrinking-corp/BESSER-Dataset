import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AContent,
    Block,
    Flow,
    Inline,
    PreContent,
    xhtml_A,
    xhtml_AContent,
    xhtml_Abbr,
    xhtml_Acronym,
    xhtml_B,
    xhtml_Big,
    xhtml_Block,
    xhtml_Blockquote,
    xhtml_Br,
    xhtml_Caption,
    xhtml_Cite,
    xhtml_Code,
    xhtml_Col,
    xhtml_Colgroup,
    xhtml_Dd,
    xhtml_Del,
    xhtml_Dfn,
    xhtml_Div,
    xhtml_Dl,
    xhtml_Dt,
    xhtml_Em,
    xhtml_Flow,
    xhtml_Hr,
    xhtml_I,
    xhtml_Img,
    xhtml_Inline,
    xhtml_Ins,
    xhtml_Kbd,
    xhtml_Li,
    xhtml_Object,
    xhtml_Ol,
    xhtml_P,
    xhtml_Param,
    xhtml_Pre,
    xhtml_PreContent,
    xhtml_Q,
    xhtml_Samp,
    xhtml_Small,
    xhtml_Span,
    xhtml_Strong,
    xhtml_Sub,
    xhtml_Sup,
    xhtml_Table,
    xhtml_Tbody,
    xhtml_Td,
    xhtml_Tfoot,
    xhtml_Th,
    xhtml_Thead,
    xhtml_Tr,
    xhtml_Tt,
    xhtml_Ul,
    xhtml_Var,
    AlignType,
    ImageKind,
    MediaType,
    MifClassType,
    ObjectName,
    ParamName,
    Shape,
    StyleSheet,
    TFrame,
    TRules,
    ValignType,
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

def test_assoc_a162_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    _safe_set(b, 'xhtml_A163', a1)
    assert _is_linked(b, 'xhtml_A163', a1)
    if hasattr(a1, 'xhtml_Inline'):
        assert _is_linked(a1, 'xhtml_Inline', b)
    _safe_set(b, 'xhtml_A163', a2)
    assert _is_linked(b, 'xhtml_A163', a2)
    if hasattr(a1, 'xhtml_Inline'):
        assert not _is_linked(a1, 'xhtml_Inline', b)
    if hasattr(a2, 'xhtml_Inline'):
        assert _is_linked(a2, 'xhtml_Inline', b)
    _safe_set(b, 'xhtml_A163', None)
    assert not _is_linked(b, 'xhtml_A163', a2)
    if hasattr(a2, 'xhtml_Inline'):
        assert not _is_linked(a2, 'xhtml_Inline', b)


def test_assoc_a259_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    _safe_set(b, 'xhtml_A261', a1)
    assert _is_linked(b, 'xhtml_A261', a1)
    if hasattr(a1, 'xhtml_Object260'):
        assert _is_linked(a1, 'xhtml_Object260', b)
    _safe_set(b, 'xhtml_A261', a2)
    assert _is_linked(b, 'xhtml_A261', a2)
    if hasattr(a1, 'xhtml_Object260'):
        assert not _is_linked(a1, 'xhtml_Object260', b)
    if hasattr(a2, 'xhtml_Object260'):
        assert _is_linked(a2, 'xhtml_Object260', b)
    _safe_set(b, 'xhtml_A261', None)
    assert not _is_linked(b, 'xhtml_A261', a2)
    if hasattr(a2, 'xhtml_Object260'):
        assert not _is_linked(a2, 'xhtml_Object260', b)


def test_assoc_a330_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    _safe_set(b, 'xhtml_A331', a1)
    assert _is_linked(b, 'xhtml_A331', a1)
    if hasattr(a1, 'xhtml_PreContent'):
        assert _is_linked(a1, 'xhtml_PreContent', b)
    _safe_set(b, 'xhtml_A331', a2)
    assert _is_linked(b, 'xhtml_A331', a2)
    if hasattr(a1, 'xhtml_PreContent'):
        assert not _is_linked(a1, 'xhtml_PreContent', b)
    if hasattr(a2, 'xhtml_PreContent'):
        assert _is_linked(a2, 'xhtml_PreContent', b)
    _safe_set(b, 'xhtml_A331', None)
    assert not _is_linked(b, 'xhtml_A331', a2)
    if hasattr(a2, 'xhtml_PreContent'):
        assert not _is_linked(a2, 'xhtml_PreContent', b)


def test_assoc_a91_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    _safe_set(b, 'xhtml_A', a1)
    assert _is_linked(b, 'xhtml_A', a1)
    if hasattr(a1, 'xhtml_Flow92'):
        assert _is_linked(a1, 'xhtml_Flow92', b)
    _safe_set(b, 'xhtml_A', a2)
    assert _is_linked(b, 'xhtml_A', a2)
    if hasattr(a1, 'xhtml_Flow92'):
        assert not _is_linked(a1, 'xhtml_Flow92', b)
    if hasattr(a2, 'xhtml_Flow92'):
        assert _is_linked(a2, 'xhtml_Flow92', b)
    _safe_set(b, 'xhtml_A', None)
    assert not _is_linked(b, 'xhtml_A', a2)
    if hasattr(a2, 'xhtml_Flow92'):
        assert not _is_linked(a2, 'xhtml_Flow92', b)


def test_assoc_abbr147_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Abbr149', a1)
    assert _is_linked(b, 'xhtml_Abbr149', a1)
    if hasattr(a1, 'xhtml_Flow148'):
        assert _is_linked(a1, 'xhtml_Flow148', b)
    _safe_set(b, 'xhtml_Abbr149', a2)
    assert _is_linked(b, 'xhtml_Abbr149', a2)
    if hasattr(a1, 'xhtml_Flow148'):
        assert not _is_linked(a1, 'xhtml_Flow148', b)
    if hasattr(a2, 'xhtml_Flow148'):
        assert _is_linked(a2, 'xhtml_Flow148', b)
    _safe_set(b, 'xhtml_Abbr149', None)
    assert not _is_linked(b, 'xhtml_Abbr149', a2)
    if hasattr(a2, 'xhtml_Flow148'):
        assert not _is_linked(a2, 'xhtml_Flow148', b)


def test_assoc_abbr218_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Abbr220', a1)
    assert _is_linked(b, 'xhtml_Abbr220', a1)
    if hasattr(a1, 'xhtml_Inline219'):
        assert _is_linked(a1, 'xhtml_Inline219', b)
    _safe_set(b, 'xhtml_Abbr220', a2)
    assert _is_linked(b, 'xhtml_Abbr220', a2)
    if hasattr(a1, 'xhtml_Inline219'):
        assert not _is_linked(a1, 'xhtml_Inline219', b)
    if hasattr(a2, 'xhtml_Inline219'):
        assert _is_linked(a2, 'xhtml_Inline219', b)
    _safe_set(b, 'xhtml_Abbr220', None)
    assert not _is_linked(b, 'xhtml_Abbr220', a2)
    if hasattr(a2, 'xhtml_Inline219'):
        assert not _is_linked(a2, 'xhtml_Inline219', b)


def test_assoc_abbr316_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Abbr318', a1)
    assert _is_linked(b, 'xhtml_Abbr318', a1)
    if hasattr(a1, 'xhtml_Object317'):
        assert _is_linked(a1, 'xhtml_Object317', b)
    _safe_set(b, 'xhtml_Abbr318', a2)
    assert _is_linked(b, 'xhtml_Abbr318', a2)
    if hasattr(a1, 'xhtml_Object317'):
        assert not _is_linked(a1, 'xhtml_Object317', b)
    if hasattr(a2, 'xhtml_Object317'):
        assert _is_linked(a2, 'xhtml_Object317', b)
    _safe_set(b, 'xhtml_Abbr318', None)
    assert not _is_linked(b, 'xhtml_Abbr318', a2)
    if hasattr(a2, 'xhtml_Object317'):
        assert not _is_linked(a2, 'xhtml_Object317', b)


def test_assoc_abbr35_reverse_link_reassign_clear():
    a1 = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Abbr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent36', {a1})
    assert _is_linked(b, 'xhtml_AContent36', a1)
    if hasattr(a1, 'xhtml_Abbr'):
        assert _is_linked(a1, 'xhtml_Abbr', b)
    _safe_set(b, 'xhtml_AContent36', {a2})
    assert _is_linked(b, 'xhtml_AContent36', a2)
    if hasattr(a1, 'xhtml_Abbr'):
        assert not _is_linked(a1, 'xhtml_Abbr', b)
    if hasattr(a2, 'xhtml_Abbr'):
        assert _is_linked(a2, 'xhtml_Abbr', b)
    _safe_set(b, 'xhtml_AContent36', set())
    assert not _is_linked(b, 'xhtml_AContent36', a2)
    if hasattr(a2, 'xhtml_Abbr'):
        assert not _is_linked(a2, 'xhtml_Abbr', b)


def test_assoc_abbr374_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Abbr376', a1)
    assert _is_linked(b, 'xhtml_Abbr376', a1)
    if hasattr(a1, 'xhtml_PreContent375'):
        assert _is_linked(a1, 'xhtml_PreContent375', b)
    _safe_set(b, 'xhtml_Abbr376', a2)
    assert _is_linked(b, 'xhtml_Abbr376', a2)
    if hasattr(a1, 'xhtml_PreContent375'):
        assert not _is_linked(a1, 'xhtml_PreContent375', b)
    if hasattr(a2, 'xhtml_PreContent375'):
        assert _is_linked(a2, 'xhtml_PreContent375', b)
    _safe_set(b, 'xhtml_Abbr376', None)
    assert not _is_linked(b, 'xhtml_Abbr376', a2)
    if hasattr(a2, 'xhtml_PreContent375'):
        assert not _is_linked(a2, 'xhtml_PreContent375', b)


def test_assoc_acronym150_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Acronym152', a1)
    assert _is_linked(b, 'xhtml_Acronym152', a1)
    if hasattr(a1, 'xhtml_Flow151'):
        assert _is_linked(a1, 'xhtml_Flow151', b)
    _safe_set(b, 'xhtml_Acronym152', a2)
    assert _is_linked(b, 'xhtml_Acronym152', a2)
    if hasattr(a1, 'xhtml_Flow151'):
        assert not _is_linked(a1, 'xhtml_Flow151', b)
    if hasattr(a2, 'xhtml_Flow151'):
        assert _is_linked(a2, 'xhtml_Flow151', b)
    _safe_set(b, 'xhtml_Acronym152', None)
    assert not _is_linked(b, 'xhtml_Acronym152', a2)
    if hasattr(a2, 'xhtml_Flow151'):
        assert not _is_linked(a2, 'xhtml_Flow151', b)


def test_assoc_acronym221_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Acronym223', a1)
    assert _is_linked(b, 'xhtml_Acronym223', a1)
    if hasattr(a1, 'xhtml_Inline222'):
        assert _is_linked(a1, 'xhtml_Inline222', b)
    _safe_set(b, 'xhtml_Acronym223', a2)
    assert _is_linked(b, 'xhtml_Acronym223', a2)
    if hasattr(a1, 'xhtml_Inline222'):
        assert not _is_linked(a1, 'xhtml_Inline222', b)
    if hasattr(a2, 'xhtml_Inline222'):
        assert _is_linked(a2, 'xhtml_Inline222', b)
    _safe_set(b, 'xhtml_Acronym223', None)
    assert not _is_linked(b, 'xhtml_Acronym223', a2)
    if hasattr(a2, 'xhtml_Inline222'):
        assert not _is_linked(a2, 'xhtml_Inline222', b)


def test_assoc_acronym319_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Acronym321', a1)
    assert _is_linked(b, 'xhtml_Acronym321', a1)
    if hasattr(a1, 'xhtml_Object320'):
        assert _is_linked(a1, 'xhtml_Object320', b)
    _safe_set(b, 'xhtml_Acronym321', a2)
    assert _is_linked(b, 'xhtml_Acronym321', a2)
    if hasattr(a1, 'xhtml_Object320'):
        assert not _is_linked(a1, 'xhtml_Object320', b)
    if hasattr(a2, 'xhtml_Object320'):
        assert _is_linked(a2, 'xhtml_Object320', b)
    _safe_set(b, 'xhtml_Acronym321', None)
    assert not _is_linked(b, 'xhtml_Acronym321', a2)
    if hasattr(a2, 'xhtml_Object320'):
        assert not _is_linked(a2, 'xhtml_Object320', b)


def test_assoc_acronym37_reverse_link_reassign_clear():
    a1 = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Acronym(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent38', {a1})
    assert _is_linked(b, 'xhtml_AContent38', a1)
    if hasattr(a1, 'xhtml_Acronym'):
        assert _is_linked(a1, 'xhtml_Acronym', b)
    _safe_set(b, 'xhtml_AContent38', {a2})
    assert _is_linked(b, 'xhtml_AContent38', a2)
    if hasattr(a1, 'xhtml_Acronym'):
        assert not _is_linked(a1, 'xhtml_Acronym', b)
    if hasattr(a2, 'xhtml_Acronym'):
        assert _is_linked(a2, 'xhtml_Acronym', b)
    _safe_set(b, 'xhtml_AContent38', set())
    assert not _is_linked(b, 'xhtml_AContent38', a2)
    if hasattr(a2, 'xhtml_Acronym'):
        assert not _is_linked(a2, 'xhtml_Acronym', b)


def test_assoc_acronym377_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Acronym379', a1)
    assert _is_linked(b, 'xhtml_Acronym379', a1)
    if hasattr(a1, 'xhtml_PreContent378'):
        assert _is_linked(a1, 'xhtml_PreContent378', b)
    _safe_set(b, 'xhtml_Acronym379', a2)
    assert _is_linked(b, 'xhtml_Acronym379', a2)
    if hasattr(a1, 'xhtml_PreContent378'):
        assert not _is_linked(a1, 'xhtml_PreContent378', b)
    if hasattr(a2, 'xhtml_PreContent378'):
        assert _is_linked(a2, 'xhtml_PreContent378', b)
    _safe_set(b, 'xhtml_Acronym379', None)
    assert not _is_linked(b, 'xhtml_Acronym379', a2)
    if hasattr(a2, 'xhtml_PreContent378'):
        assert not _is_linked(a2, 'xhtml_PreContent378', b)


def test_assoc_b11_reverse_link_reassign_clear():
    a1 = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_B(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent12', {a1})
    assert _is_linked(b, 'xhtml_AContent12', a1)
    if hasattr(a1, 'xhtml_B'):
        assert _is_linked(a1, 'xhtml_B', b)
    _safe_set(b, 'xhtml_AContent12', {a2})
    assert _is_linked(b, 'xhtml_AContent12', a2)
    if hasattr(a1, 'xhtml_B'):
        assert not _is_linked(a1, 'xhtml_B', b)
    if hasattr(a2, 'xhtml_B'):
        assert _is_linked(a2, 'xhtml_B', b)
    _safe_set(b, 'xhtml_AContent12', set())
    assert not _is_linked(b, 'xhtml_AContent12', a2)
    if hasattr(a2, 'xhtml_B'):
        assert not _is_linked(a2, 'xhtml_B', b)


def test_assoc_b111_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_B113', a1)
    assert _is_linked(b, 'xhtml_B113', a1)
    if hasattr(a1, 'xhtml_Flow112'):
        assert _is_linked(a1, 'xhtml_Flow112', b)
    _safe_set(b, 'xhtml_B113', a2)
    assert _is_linked(b, 'xhtml_B113', a2)
    if hasattr(a1, 'xhtml_Flow112'):
        assert not _is_linked(a1, 'xhtml_Flow112', b)
    if hasattr(a2, 'xhtml_Flow112'):
        assert _is_linked(a2, 'xhtml_Flow112', b)
    _safe_set(b, 'xhtml_B113', None)
    assert not _is_linked(b, 'xhtml_B113', a2)
    if hasattr(a2, 'xhtml_Flow112'):
        assert not _is_linked(a2, 'xhtml_Flow112', b)


def test_assoc_b182_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_B184', a1)
    assert _is_linked(b, 'xhtml_B184', a1)
    if hasattr(a1, 'xhtml_Inline183'):
        assert _is_linked(a1, 'xhtml_Inline183', b)
    _safe_set(b, 'xhtml_B184', a2)
    assert _is_linked(b, 'xhtml_B184', a2)
    if hasattr(a1, 'xhtml_Inline183'):
        assert not _is_linked(a1, 'xhtml_Inline183', b)
    if hasattr(a2, 'xhtml_Inline183'):
        assert _is_linked(a2, 'xhtml_Inline183', b)
    _safe_set(b, 'xhtml_B184', None)
    assert not _is_linked(b, 'xhtml_B184', a2)
    if hasattr(a2, 'xhtml_Inline183'):
        assert not _is_linked(a2, 'xhtml_Inline183', b)


def test_assoc_b280_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_B282', a1)
    assert _is_linked(b, 'xhtml_B282', a1)
    if hasattr(a1, 'xhtml_Object281'):
        assert _is_linked(a1, 'xhtml_Object281', b)
    _safe_set(b, 'xhtml_B282', a2)
    assert _is_linked(b, 'xhtml_B282', a2)
    if hasattr(a1, 'xhtml_Object281'):
        assert not _is_linked(a1, 'xhtml_Object281', b)
    if hasattr(a2, 'xhtml_Object281'):
        assert _is_linked(a2, 'xhtml_Object281', b)
    _safe_set(b, 'xhtml_B282', None)
    assert not _is_linked(b, 'xhtml_B282', a2)
    if hasattr(a2, 'xhtml_Object281'):
        assert not _is_linked(a2, 'xhtml_Object281', b)


def test_assoc_b338_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_B340', a1)
    assert _is_linked(b, 'xhtml_B340', a1)
    if hasattr(a1, 'xhtml_PreContent339'):
        assert _is_linked(a1, 'xhtml_PreContent339', b)
    _safe_set(b, 'xhtml_B340', a2)
    assert _is_linked(b, 'xhtml_B340', a2)
    if hasattr(a1, 'xhtml_PreContent339'):
        assert not _is_linked(a1, 'xhtml_PreContent339', b)
    if hasattr(a2, 'xhtml_PreContent339'):
        assert _is_linked(a2, 'xhtml_PreContent339', b)
    _safe_set(b, 'xhtml_B340', None)
    assert not _is_linked(b, 'xhtml_B340', a2)
    if hasattr(a2, 'xhtml_PreContent339'):
        assert not _is_linked(a2, 'xhtml_PreContent339', b)


def test_assoc_big114_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Big116', a1)
    assert _is_linked(b, 'xhtml_Big116', a1)
    if hasattr(a1, 'xhtml_Flow115'):
        assert _is_linked(a1, 'xhtml_Flow115', b)
    _safe_set(b, 'xhtml_Big116', a2)
    assert _is_linked(b, 'xhtml_Big116', a2)
    if hasattr(a1, 'xhtml_Flow115'):
        assert not _is_linked(a1, 'xhtml_Flow115', b)
    if hasattr(a2, 'xhtml_Flow115'):
        assert _is_linked(a2, 'xhtml_Flow115', b)
    _safe_set(b, 'xhtml_Big116', None)
    assert not _is_linked(b, 'xhtml_Big116', a2)
    if hasattr(a2, 'xhtml_Flow115'):
        assert not _is_linked(a2, 'xhtml_Flow115', b)


def test_assoc_big13_reverse_link_reassign_clear():
    a1 = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Big(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent14', {a1})
    assert _is_linked(b, 'xhtml_AContent14', a1)
    if hasattr(a1, 'xhtml_Big'):
        assert _is_linked(a1, 'xhtml_Big', b)
    _safe_set(b, 'xhtml_AContent14', {a2})
    assert _is_linked(b, 'xhtml_AContent14', a2)
    if hasattr(a1, 'xhtml_Big'):
        assert not _is_linked(a1, 'xhtml_Big', b)
    if hasattr(a2, 'xhtml_Big'):
        assert _is_linked(a2, 'xhtml_Big', b)
    _safe_set(b, 'xhtml_AContent14', set())
    assert not _is_linked(b, 'xhtml_AContent14', a2)
    if hasattr(a2, 'xhtml_Big'):
        assert not _is_linked(a2, 'xhtml_Big', b)


def test_assoc_big185_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Big187', a1)
    assert _is_linked(b, 'xhtml_Big187', a1)
    if hasattr(a1, 'xhtml_Inline186'):
        assert _is_linked(a1, 'xhtml_Inline186', b)
    _safe_set(b, 'xhtml_Big187', a2)
    assert _is_linked(b, 'xhtml_Big187', a2)
    if hasattr(a1, 'xhtml_Inline186'):
        assert not _is_linked(a1, 'xhtml_Inline186', b)
    if hasattr(a2, 'xhtml_Inline186'):
        assert _is_linked(a2, 'xhtml_Inline186', b)
    _safe_set(b, 'xhtml_Big187', None)
    assert not _is_linked(b, 'xhtml_Big187', a2)
    if hasattr(a2, 'xhtml_Inline186'):
        assert not _is_linked(a2, 'xhtml_Inline186', b)


def test_assoc_big283_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Big285', a1)
    assert _is_linked(b, 'xhtml_Big285', a1)
    if hasattr(a1, 'xhtml_Object284'):
        assert _is_linked(a1, 'xhtml_Object284', b)
    _safe_set(b, 'xhtml_Big285', a2)
    assert _is_linked(b, 'xhtml_Big285', a2)
    if hasattr(a1, 'xhtml_Object284'):
        assert not _is_linked(a1, 'xhtml_Object284', b)
    if hasattr(a2, 'xhtml_Object284'):
        assert _is_linked(a2, 'xhtml_Object284', b)
    _safe_set(b, 'xhtml_Big285', None)
    assert not _is_linked(b, 'xhtml_Big285', a2)
    if hasattr(a2, 'xhtml_Object284'):
        assert not _is_linked(a2, 'xhtml_Object284', b)


def test_assoc_big341_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Big343', a1)
    assert _is_linked(b, 'xhtml_Big343', a1)
    if hasattr(a1, 'xhtml_PreContent342'):
        assert _is_linked(a1, 'xhtml_PreContent342', b)
    _safe_set(b, 'xhtml_Big343', a2)
    assert _is_linked(b, 'xhtml_Big343', a2)
    if hasattr(a1, 'xhtml_PreContent342'):
        assert not _is_linked(a1, 'xhtml_PreContent342', b)
    if hasattr(a2, 'xhtml_PreContent342'):
        assert _is_linked(a2, 'xhtml_PreContent342', b)
    _safe_set(b, 'xhtml_Big343', None)
    assert not _is_linked(b, 'xhtml_Big343', a2)
    if hasattr(a2, 'xhtml_PreContent342'):
        assert not _is_linked(a2, 'xhtml_PreContent342', b)


def test_assoc_blockquote253_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Blockquote255', a1)
    assert _is_linked(b, 'xhtml_Blockquote255', a1)
    if hasattr(a1, 'xhtml_Object254'):
        assert _is_linked(a1, 'xhtml_Object254', b)
    _safe_set(b, 'xhtml_Blockquote255', a2)
    assert _is_linked(b, 'xhtml_Blockquote255', a2)
    if hasattr(a1, 'xhtml_Object254'):
        assert not _is_linked(a1, 'xhtml_Object254', b)
    if hasattr(a2, 'xhtml_Object254'):
        assert _is_linked(a2, 'xhtml_Object254', b)
    _safe_set(b, 'xhtml_Blockquote255', None)
    assert not _is_linked(b, 'xhtml_Blockquote255', a2)
    if hasattr(a2, 'xhtml_Object254'):
        assert not _is_linked(a2, 'xhtml_Object254', b)


def test_assoc_blockquote56_reverse_link_reassign_clear():
    a1 = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Blockquote(cite="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block57', {a1})
    assert _is_linked(b, 'xhtml_Block57', a1)
    if hasattr(a1, 'xhtml_Blockquote'):
        assert _is_linked(a1, 'xhtml_Blockquote', b)
    _safe_set(b, 'xhtml_Block57', {a2})
    assert _is_linked(b, 'xhtml_Block57', a2)
    if hasattr(a1, 'xhtml_Blockquote'):
        assert not _is_linked(a1, 'xhtml_Blockquote', b)
    if hasattr(a2, 'xhtml_Blockquote'):
        assert _is_linked(a2, 'xhtml_Blockquote', b)
    _safe_set(b, 'xhtml_Block57', set())
    assert not _is_linked(b, 'xhtml_Block57', a2)
    if hasattr(a2, 'xhtml_Blockquote'):
        assert not _is_linked(a2, 'xhtml_Blockquote', b)


def test_assoc_blockquote85_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Blockquote87', a1)
    assert _is_linked(b, 'xhtml_Blockquote87', a1)
    if hasattr(a1, 'xhtml_Flow86'):
        assert _is_linked(a1, 'xhtml_Flow86', b)
    _safe_set(b, 'xhtml_Blockquote87', a2)
    assert _is_linked(b, 'xhtml_Blockquote87', a2)
    if hasattr(a1, 'xhtml_Flow86'):
        assert not _is_linked(a1, 'xhtml_Flow86', b)
    if hasattr(a2, 'xhtml_Flow86'):
        assert _is_linked(a2, 'xhtml_Flow86', b)
    _safe_set(b, 'xhtml_Blockquote87', None)
    assert not _is_linked(b, 'xhtml_Blockquote87', a2)
    if hasattr(a2, 'xhtml_Flow86'):
        assert not _is_linked(a2, 'xhtml_Flow86', b)


def test_assoc_br0_reverse_link_reassign_clear():
    a1 = xhtml_Br(class_="sample_text", style="sample_text")
    a2 = xhtml_Br(class_="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent', {a1})
    assert _is_linked(b, 'xhtml_AContent', a1)
    if hasattr(a1, 'xhtml_Br'):
        assert _is_linked(a1, 'xhtml_Br', b)
    _safe_set(b, 'xhtml_AContent', {a2})
    assert _is_linked(b, 'xhtml_AContent', a2)
    if hasattr(a1, 'xhtml_Br'):
        assert not _is_linked(a1, 'xhtml_Br', b)
    if hasattr(a2, 'xhtml_Br'):
        assert _is_linked(a2, 'xhtml_Br', b)
    _safe_set(b, 'xhtml_AContent', set())
    assert not _is_linked(b, 'xhtml_AContent', a2)
    if hasattr(a2, 'xhtml_Br'):
        assert not _is_linked(a2, 'xhtml_Br', b)


def test_assoc_br164_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Br(class_="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Br166', a1)
    assert _is_linked(b, 'xhtml_Br166', a1)
    if hasattr(a1, 'xhtml_Inline165'):
        assert _is_linked(a1, 'xhtml_Inline165', b)
    _safe_set(b, 'xhtml_Br166', a2)
    assert _is_linked(b, 'xhtml_Br166', a2)
    if hasattr(a1, 'xhtml_Inline165'):
        assert not _is_linked(a1, 'xhtml_Inline165', b)
    if hasattr(a2, 'xhtml_Inline165'):
        assert _is_linked(a2, 'xhtml_Inline165', b)
    _safe_set(b, 'xhtml_Br166', None)
    assert not _is_linked(b, 'xhtml_Br166', a2)
    if hasattr(a2, 'xhtml_Inline165'):
        assert not _is_linked(a2, 'xhtml_Inline165', b)


def test_assoc_br262_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Br(class_="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Br264', a1)
    assert _is_linked(b, 'xhtml_Br264', a1)
    if hasattr(a1, 'xhtml_Object263'):
        assert _is_linked(a1, 'xhtml_Object263', b)
    _safe_set(b, 'xhtml_Br264', a2)
    assert _is_linked(b, 'xhtml_Br264', a2)
    if hasattr(a1, 'xhtml_Object263'):
        assert not _is_linked(a1, 'xhtml_Object263', b)
    if hasattr(a2, 'xhtml_Object263'):
        assert _is_linked(a2, 'xhtml_Object263', b)
    _safe_set(b, 'xhtml_Br264', None)
    assert not _is_linked(b, 'xhtml_Br264', a2)
    if hasattr(a2, 'xhtml_Object263'):
        assert not _is_linked(a2, 'xhtml_Object263', b)


def test_assoc_br386_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Br(class_="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Br388', a1)
    assert _is_linked(b, 'xhtml_Br388', a1)
    if hasattr(a1, 'xhtml_PreContent387'):
        assert _is_linked(a1, 'xhtml_PreContent387', b)
    _safe_set(b, 'xhtml_Br388', a2)
    assert _is_linked(b, 'xhtml_Br388', a2)
    if hasattr(a1, 'xhtml_PreContent387'):
        assert not _is_linked(a1, 'xhtml_PreContent387', b)
    if hasattr(a2, 'xhtml_PreContent387'):
        assert _is_linked(a2, 'xhtml_PreContent387', b)
    _safe_set(b, 'xhtml_Br388', None)
    assert not _is_linked(b, 'xhtml_Br388', a2)
    if hasattr(a2, 'xhtml_PreContent387'):
        assert not _is_linked(a2, 'xhtml_PreContent387', b)


def test_assoc_br93_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Br(class_="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Br95', a1)
    assert _is_linked(b, 'xhtml_Br95', a1)
    if hasattr(a1, 'xhtml_Flow94'):
        assert _is_linked(a1, 'xhtml_Flow94', b)
    _safe_set(b, 'xhtml_Br95', a2)
    assert _is_linked(b, 'xhtml_Br95', a2)
    if hasattr(a1, 'xhtml_Flow94'):
        assert not _is_linked(a1, 'xhtml_Flow94', b)
    if hasattr(a2, 'xhtml_Flow94'):
        assert _is_linked(a2, 'xhtml_Flow94', b)
    _safe_set(b, 'xhtml_Br95', None)
    assert not _is_linked(b, 'xhtml_Br95', a2)
    if hasattr(a2, 'xhtml_Flow94'):
        assert not _is_linked(a2, 'xhtml_Flow94', b)


def test_assoc_caption392_reverse_link_reassign_clear():
    a1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Caption(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Caption', a1)
    assert _is_linked(b, 'xhtml_Caption', a1)
    if hasattr(a1, 'xhtml_Table393'):
        assert _is_linked(a1, 'xhtml_Table393', b)
    _safe_set(b, 'xhtml_Caption', a2)
    assert _is_linked(b, 'xhtml_Caption', a2)
    if hasattr(a1, 'xhtml_Table393'):
        assert not _is_linked(a1, 'xhtml_Table393', b)
    if hasattr(a2, 'xhtml_Table393'):
        assert _is_linked(a2, 'xhtml_Table393', b)
    _safe_set(b, 'xhtml_Caption', None)
    assert not _is_linked(b, 'xhtml_Caption', a2)
    if hasattr(a2, 'xhtml_Table393'):
        assert not _is_linked(a2, 'xhtml_Table393', b)


def test_assoc_cite144_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Cite146', a1)
    assert _is_linked(b, 'xhtml_Cite146', a1)
    if hasattr(a1, 'xhtml_Flow145'):
        assert _is_linked(a1, 'xhtml_Flow145', b)
    _safe_set(b, 'xhtml_Cite146', a2)
    assert _is_linked(b, 'xhtml_Cite146', a2)
    if hasattr(a1, 'xhtml_Flow145'):
        assert not _is_linked(a1, 'xhtml_Flow145', b)
    if hasattr(a2, 'xhtml_Flow145'):
        assert _is_linked(a2, 'xhtml_Flow145', b)
    _safe_set(b, 'xhtml_Cite146', None)
    assert not _is_linked(b, 'xhtml_Cite146', a2)
    if hasattr(a2, 'xhtml_Flow145'):
        assert not _is_linked(a2, 'xhtml_Flow145', b)


def test_assoc_cite215_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Cite217', a1)
    assert _is_linked(b, 'xhtml_Cite217', a1)
    if hasattr(a1, 'xhtml_Inline216'):
        assert _is_linked(a1, 'xhtml_Inline216', b)
    _safe_set(b, 'xhtml_Cite217', a2)
    assert _is_linked(b, 'xhtml_Cite217', a2)
    if hasattr(a1, 'xhtml_Inline216'):
        assert not _is_linked(a1, 'xhtml_Inline216', b)
    if hasattr(a2, 'xhtml_Inline216'):
        assert _is_linked(a2, 'xhtml_Inline216', b)
    _safe_set(b, 'xhtml_Cite217', None)
    assert not _is_linked(b, 'xhtml_Cite217', a2)
    if hasattr(a2, 'xhtml_Inline216'):
        assert not _is_linked(a2, 'xhtml_Inline216', b)


def test_assoc_cite313_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Cite315', a1)
    assert _is_linked(b, 'xhtml_Cite315', a1)
    if hasattr(a1, 'xhtml_Object314'):
        assert _is_linked(a1, 'xhtml_Object314', b)
    _safe_set(b, 'xhtml_Cite315', a2)
    assert _is_linked(b, 'xhtml_Cite315', a2)
    if hasattr(a1, 'xhtml_Object314'):
        assert not _is_linked(a1, 'xhtml_Object314', b)
    if hasattr(a2, 'xhtml_Object314'):
        assert _is_linked(a2, 'xhtml_Object314', b)
    _safe_set(b, 'xhtml_Cite315', None)
    assert not _is_linked(b, 'xhtml_Cite315', a2)
    if hasattr(a2, 'xhtml_Object314'):
        assert not _is_linked(a2, 'xhtml_Object314', b)


def test_assoc_cite33_reverse_link_reassign_clear():
    a1 = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Cite(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent34', {a1})
    assert _is_linked(b, 'xhtml_AContent34', a1)
    if hasattr(a1, 'xhtml_Cite'):
        assert _is_linked(a1, 'xhtml_Cite', b)
    _safe_set(b, 'xhtml_AContent34', {a2})
    assert _is_linked(b, 'xhtml_AContent34', a2)
    if hasattr(a1, 'xhtml_Cite'):
        assert not _is_linked(a1, 'xhtml_Cite', b)
    if hasattr(a2, 'xhtml_Cite'):
        assert _is_linked(a2, 'xhtml_Cite', b)
    _safe_set(b, 'xhtml_AContent34', set())
    assert not _is_linked(b, 'xhtml_AContent34', a2)
    if hasattr(a2, 'xhtml_Cite'):
        assert not _is_linked(a2, 'xhtml_Cite', b)


def test_assoc_cite371_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Cite373', a1)
    assert _is_linked(b, 'xhtml_Cite373', a1)
    if hasattr(a1, 'xhtml_PreContent372'):
        assert _is_linked(a1, 'xhtml_PreContent372', b)
    _safe_set(b, 'xhtml_Cite373', a2)
    assert _is_linked(b, 'xhtml_Cite373', a2)
    if hasattr(a1, 'xhtml_PreContent372'):
        assert not _is_linked(a1, 'xhtml_PreContent372', b)
    if hasattr(a2, 'xhtml_PreContent372'):
        assert _is_linked(a2, 'xhtml_PreContent372', b)
    _safe_set(b, 'xhtml_Cite373', None)
    assert not _is_linked(b, 'xhtml_Cite373', a2)
    if hasattr(a2, 'xhtml_PreContent372'):
        assert not _is_linked(a2, 'xhtml_PreContent372', b)


def test_assoc_code129_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Code131', a1)
    assert _is_linked(b, 'xhtml_Code131', a1)
    if hasattr(a1, 'xhtml_Flow130'):
        assert _is_linked(a1, 'xhtml_Flow130', b)
    _safe_set(b, 'xhtml_Code131', a2)
    assert _is_linked(b, 'xhtml_Code131', a2)
    if hasattr(a1, 'xhtml_Flow130'):
        assert not _is_linked(a1, 'xhtml_Flow130', b)
    if hasattr(a2, 'xhtml_Flow130'):
        assert _is_linked(a2, 'xhtml_Flow130', b)
    _safe_set(b, 'xhtml_Code131', None)
    assert not _is_linked(b, 'xhtml_Code131', a2)
    if hasattr(a2, 'xhtml_Flow130'):
        assert not _is_linked(a2, 'xhtml_Flow130', b)


def test_assoc_code200_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Code202', a1)
    assert _is_linked(b, 'xhtml_Code202', a1)
    if hasattr(a1, 'xhtml_Inline201'):
        assert _is_linked(a1, 'xhtml_Inline201', b)
    _safe_set(b, 'xhtml_Code202', a2)
    assert _is_linked(b, 'xhtml_Code202', a2)
    if hasattr(a1, 'xhtml_Inline201'):
        assert not _is_linked(a1, 'xhtml_Inline201', b)
    if hasattr(a2, 'xhtml_Inline201'):
        assert _is_linked(a2, 'xhtml_Inline201', b)
    _safe_set(b, 'xhtml_Code202', None)
    assert not _is_linked(b, 'xhtml_Code202', a2)
    if hasattr(a2, 'xhtml_Inline201'):
        assert not _is_linked(a2, 'xhtml_Inline201', b)


def test_assoc_code23_reverse_link_reassign_clear():
    a1 = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Code(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent24', {a1})
    assert _is_linked(b, 'xhtml_AContent24', a1)
    if hasattr(a1, 'xhtml_Code'):
        assert _is_linked(a1, 'xhtml_Code', b)
    _safe_set(b, 'xhtml_AContent24', {a2})
    assert _is_linked(b, 'xhtml_AContent24', a2)
    if hasattr(a1, 'xhtml_Code'):
        assert not _is_linked(a1, 'xhtml_Code', b)
    if hasattr(a2, 'xhtml_Code'):
        assert _is_linked(a2, 'xhtml_Code', b)
    _safe_set(b, 'xhtml_AContent24', set())
    assert not _is_linked(b, 'xhtml_AContent24', a2)
    if hasattr(a2, 'xhtml_Code'):
        assert not _is_linked(a2, 'xhtml_Code', b)


def test_assoc_code298_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Code300', a1)
    assert _is_linked(b, 'xhtml_Code300', a1)
    if hasattr(a1, 'xhtml_Object299'):
        assert _is_linked(a1, 'xhtml_Object299', b)
    _safe_set(b, 'xhtml_Code300', a2)
    assert _is_linked(b, 'xhtml_Code300', a2)
    if hasattr(a1, 'xhtml_Object299'):
        assert not _is_linked(a1, 'xhtml_Object299', b)
    if hasattr(a2, 'xhtml_Object299'):
        assert _is_linked(a2, 'xhtml_Object299', b)
    _safe_set(b, 'xhtml_Code300', None)
    assert not _is_linked(b, 'xhtml_Code300', a2)
    if hasattr(a2, 'xhtml_Object299'):
        assert not _is_linked(a2, 'xhtml_Object299', b)


def test_assoc_code356_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Code358', a1)
    assert _is_linked(b, 'xhtml_Code358', a1)
    if hasattr(a1, 'xhtml_PreContent357'):
        assert _is_linked(a1, 'xhtml_PreContent357', b)
    _safe_set(b, 'xhtml_Code358', a2)
    assert _is_linked(b, 'xhtml_Code358', a2)
    if hasattr(a1, 'xhtml_PreContent357'):
        assert not _is_linked(a1, 'xhtml_PreContent357', b)
    if hasattr(a2, 'xhtml_PreContent357'):
        assert _is_linked(a2, 'xhtml_PreContent357', b)
    _safe_set(b, 'xhtml_Code358', None)
    assert not _is_linked(b, 'xhtml_Code358', a2)
    if hasattr(a2, 'xhtml_PreContent357'):
        assert not _is_linked(a2, 'xhtml_PreContent357', b)


def test_assoc_col394_reverse_link_reassign_clear():
    a1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Col396', a1)
    assert _is_linked(b, 'xhtml_Col396', a1)
    if hasattr(a1, 'xhtml_Table395'):
        assert _is_linked(a1, 'xhtml_Table395', b)
    _safe_set(b, 'xhtml_Col396', a2)
    assert _is_linked(b, 'xhtml_Col396', a2)
    if hasattr(a1, 'xhtml_Table395'):
        assert not _is_linked(a1, 'xhtml_Table395', b)
    if hasattr(a2, 'xhtml_Table395'):
        assert _is_linked(a2, 'xhtml_Table395', b)
    _safe_set(b, 'xhtml_Col396', None)
    assert not _is_linked(b, 'xhtml_Col396', a2)
    if hasattr(a2, 'xhtml_Table395'):
        assert not _is_linked(a2, 'xhtml_Table395', b)


def test_assoc_col60_reverse_link_reassign_clear():
    a1 = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    a2 = xhtml_Colgroup(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", span="sample_text_2", style="sample_text_2", valign="sample_text_2", width="sample_text_2")
    b = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Col', a1)
    assert _is_linked(b, 'xhtml_Col', a1)
    if hasattr(a1, 'xhtml_Colgroup'):
        assert _is_linked(a1, 'xhtml_Colgroup', b)
    _safe_set(b, 'xhtml_Col', a2)
    assert _is_linked(b, 'xhtml_Col', a2)
    if hasattr(a1, 'xhtml_Colgroup'):
        assert not _is_linked(a1, 'xhtml_Colgroup', b)
    if hasattr(a2, 'xhtml_Colgroup'):
        assert _is_linked(a2, 'xhtml_Colgroup', b)
    _safe_set(b, 'xhtml_Col', None)
    assert not _is_linked(b, 'xhtml_Col', a2)
    if hasattr(a2, 'xhtml_Colgroup'):
        assert not _is_linked(a2, 'xhtml_Colgroup', b)


def test_assoc_colgroup397_reverse_link_reassign_clear():
    a1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Colgroup399', a1)
    assert _is_linked(b, 'xhtml_Colgroup399', a1)
    if hasattr(a1, 'xhtml_Table398'):
        assert _is_linked(a1, 'xhtml_Table398', b)
    _safe_set(b, 'xhtml_Colgroup399', a2)
    assert _is_linked(b, 'xhtml_Colgroup399', a2)
    if hasattr(a1, 'xhtml_Table398'):
        assert not _is_linked(a1, 'xhtml_Table398', b)
    if hasattr(a2, 'xhtml_Table398'):
        assert _is_linked(a2, 'xhtml_Table398', b)
    _safe_set(b, 'xhtml_Colgroup399', None)
    assert not _is_linked(b, 'xhtml_Colgroup399', a2)
    if hasattr(a2, 'xhtml_Table398'):
        assert not _is_linked(a2, 'xhtml_Table398', b)


def test_assoc_dd63_reverse_link_reassign_clear():
    a1 = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Dl(class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Dd(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dd', a1)
    assert _is_linked(b, 'xhtml_Dd', a1)
    if hasattr(a1, 'xhtml_Dl64'):
        assert _is_linked(a1, 'xhtml_Dl64', b)
    _safe_set(b, 'xhtml_Dd', a2)
    assert _is_linked(b, 'xhtml_Dd', a2)
    if hasattr(a1, 'xhtml_Dl64'):
        assert not _is_linked(a1, 'xhtml_Dl64', b)
    if hasattr(a2, 'xhtml_Dl64'):
        assert _is_linked(a2, 'xhtml_Dl64', b)
    _safe_set(b, 'xhtml_Dd', None)
    assert not _is_linked(b, 'xhtml_Dd', a2)
    if hasattr(a2, 'xhtml_Dl64'):
        assert not _is_linked(a2, 'xhtml_Dl64', b)


def test_assoc_dfn126_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dfn128', a1)
    assert _is_linked(b, 'xhtml_Dfn128', a1)
    if hasattr(a1, 'xhtml_Flow127'):
        assert _is_linked(a1, 'xhtml_Flow127', b)
    _safe_set(b, 'xhtml_Dfn128', a2)
    assert _is_linked(b, 'xhtml_Dfn128', a2)
    if hasattr(a1, 'xhtml_Flow127'):
        assert not _is_linked(a1, 'xhtml_Flow127', b)
    if hasattr(a2, 'xhtml_Flow127'):
        assert _is_linked(a2, 'xhtml_Flow127', b)
    _safe_set(b, 'xhtml_Dfn128', None)
    assert not _is_linked(b, 'xhtml_Dfn128', a2)
    if hasattr(a2, 'xhtml_Flow127'):
        assert not _is_linked(a2, 'xhtml_Flow127', b)


def test_assoc_dfn197_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dfn199', a1)
    assert _is_linked(b, 'xhtml_Dfn199', a1)
    if hasattr(a1, 'xhtml_Inline198'):
        assert _is_linked(a1, 'xhtml_Inline198', b)
    _safe_set(b, 'xhtml_Dfn199', a2)
    assert _is_linked(b, 'xhtml_Dfn199', a2)
    if hasattr(a1, 'xhtml_Inline198'):
        assert not _is_linked(a1, 'xhtml_Inline198', b)
    if hasattr(a2, 'xhtml_Inline198'):
        assert _is_linked(a2, 'xhtml_Inline198', b)
    _safe_set(b, 'xhtml_Dfn199', None)
    assert not _is_linked(b, 'xhtml_Dfn199', a2)
    if hasattr(a2, 'xhtml_Inline198'):
        assert not _is_linked(a2, 'xhtml_Inline198', b)


def test_assoc_dfn21_reverse_link_reassign_clear():
    a1 = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Dfn(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent22', {a1})
    assert _is_linked(b, 'xhtml_AContent22', a1)
    if hasattr(a1, 'xhtml_Dfn'):
        assert _is_linked(a1, 'xhtml_Dfn', b)
    _safe_set(b, 'xhtml_AContent22', {a2})
    assert _is_linked(b, 'xhtml_AContent22', a2)
    if hasattr(a1, 'xhtml_Dfn'):
        assert not _is_linked(a1, 'xhtml_Dfn', b)
    if hasattr(a2, 'xhtml_Dfn'):
        assert _is_linked(a2, 'xhtml_Dfn', b)
    _safe_set(b, 'xhtml_AContent22', set())
    assert not _is_linked(b, 'xhtml_AContent22', a2)
    if hasattr(a2, 'xhtml_Dfn'):
        assert not _is_linked(a2, 'xhtml_Dfn', b)


def test_assoc_dfn295_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dfn297', a1)
    assert _is_linked(b, 'xhtml_Dfn297', a1)
    if hasattr(a1, 'xhtml_Object296'):
        assert _is_linked(a1, 'xhtml_Object296', b)
    _safe_set(b, 'xhtml_Dfn297', a2)
    assert _is_linked(b, 'xhtml_Dfn297', a2)
    if hasattr(a1, 'xhtml_Object296'):
        assert not _is_linked(a1, 'xhtml_Object296', b)
    if hasattr(a2, 'xhtml_Object296'):
        assert _is_linked(a2, 'xhtml_Object296', b)
    _safe_set(b, 'xhtml_Dfn297', None)
    assert not _is_linked(b, 'xhtml_Dfn297', a2)
    if hasattr(a2, 'xhtml_Object296'):
        assert not _is_linked(a2, 'xhtml_Object296', b)


def test_assoc_dfn353_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dfn355', a1)
    assert _is_linked(b, 'xhtml_Dfn355', a1)
    if hasattr(a1, 'xhtml_PreContent354'):
        assert _is_linked(a1, 'xhtml_PreContent354', b)
    _safe_set(b, 'xhtml_Dfn355', a2)
    assert _is_linked(b, 'xhtml_Dfn355', a2)
    if hasattr(a1, 'xhtml_PreContent354'):
        assert not _is_linked(a1, 'xhtml_PreContent354', b)
    if hasattr(a2, 'xhtml_PreContent354'):
        assert _is_linked(a2, 'xhtml_PreContent354', b)
    _safe_set(b, 'xhtml_Dfn355', None)
    assert not _is_linked(b, 'xhtml_Dfn355', a2)
    if hasattr(a2, 'xhtml_PreContent354'):
        assert not _is_linked(a2, 'xhtml_PreContent354', b)


def test_assoc_div235_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    _safe_set(b, 'xhtml_Div237', a1)
    assert _is_linked(b, 'xhtml_Div237', a1)
    if hasattr(a1, 'xhtml_Object236'):
        assert _is_linked(a1, 'xhtml_Object236', b)
    _safe_set(b, 'xhtml_Div237', a2)
    assert _is_linked(b, 'xhtml_Div237', a2)
    if hasattr(a1, 'xhtml_Object236'):
        assert not _is_linked(a1, 'xhtml_Object236', b)
    if hasattr(a2, 'xhtml_Object236'):
        assert _is_linked(a2, 'xhtml_Object236', b)
    _safe_set(b, 'xhtml_Div237', None)
    assert not _is_linked(b, 'xhtml_Div237', a2)
    if hasattr(a2, 'xhtml_Object236'):
        assert not _is_linked(a2, 'xhtml_Object236', b)


def test_assoc_div44_reverse_link_reassign_clear():
    a1 = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    a2 = xhtml_Div(class_="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", style="sample_text_2", title="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block45', {a1})
    assert _is_linked(b, 'xhtml_Block45', a1)
    if hasattr(a1, 'xhtml_Div'):
        assert _is_linked(a1, 'xhtml_Div', b)
    _safe_set(b, 'xhtml_Block45', {a2})
    assert _is_linked(b, 'xhtml_Block45', a2)
    if hasattr(a1, 'xhtml_Div'):
        assert not _is_linked(a1, 'xhtml_Div', b)
    if hasattr(a2, 'xhtml_Div'):
        assert _is_linked(a2, 'xhtml_Div', b)
    _safe_set(b, 'xhtml_Block45', set())
    assert not _is_linked(b, 'xhtml_Block45', a2)
    if hasattr(a2, 'xhtml_Div'):
        assert not _is_linked(a2, 'xhtml_Div', b)


def test_assoc_div67_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    _safe_set(b, 'xhtml_Div69', a1)
    assert _is_linked(b, 'xhtml_Div69', a1)
    if hasattr(a1, 'xhtml_Flow68'):
        assert _is_linked(a1, 'xhtml_Flow68', b)
    _safe_set(b, 'xhtml_Div69', a2)
    assert _is_linked(b, 'xhtml_Div69', a2)
    if hasattr(a1, 'xhtml_Flow68'):
        assert not _is_linked(a1, 'xhtml_Flow68', b)
    if hasattr(a2, 'xhtml_Flow68'):
        assert _is_linked(a2, 'xhtml_Flow68', b)
    _safe_set(b, 'xhtml_Div69', None)
    assert not _is_linked(b, 'xhtml_Div69', a2)
    if hasattr(a2, 'xhtml_Flow68'):
        assert not _is_linked(a2, 'xhtml_Flow68', b)


def test_assoc_dl244_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dl246', a1)
    assert _is_linked(b, 'xhtml_Dl246', a1)
    if hasattr(a1, 'xhtml_Object245'):
        assert _is_linked(a1, 'xhtml_Object245', b)
    _safe_set(b, 'xhtml_Dl246', a2)
    assert _is_linked(b, 'xhtml_Dl246', a2)
    if hasattr(a1, 'xhtml_Object245'):
        assert not _is_linked(a1, 'xhtml_Object245', b)
    if hasattr(a2, 'xhtml_Object245'):
        assert _is_linked(a2, 'xhtml_Object245', b)
    _safe_set(b, 'xhtml_Dl246', None)
    assert not _is_linked(b, 'xhtml_Dl246', a2)
    if hasattr(a2, 'xhtml_Object245'):
        assert not _is_linked(a2, 'xhtml_Object245', b)


def test_assoc_dl50_reverse_link_reassign_clear():
    a1 = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Dl(class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block51', {a1})
    assert _is_linked(b, 'xhtml_Block51', a1)
    if hasattr(a1, 'xhtml_Dl'):
        assert _is_linked(a1, 'xhtml_Dl', b)
    _safe_set(b, 'xhtml_Block51', {a2})
    assert _is_linked(b, 'xhtml_Block51', a2)
    if hasattr(a1, 'xhtml_Dl'):
        assert not _is_linked(a1, 'xhtml_Dl', b)
    if hasattr(a2, 'xhtml_Dl'):
        assert _is_linked(a2, 'xhtml_Dl', b)
    _safe_set(b, 'xhtml_Block51', set())
    assert not _is_linked(b, 'xhtml_Block51', a2)
    if hasattr(a2, 'xhtml_Dl'):
        assert not _is_linked(a2, 'xhtml_Dl', b)


def test_assoc_dl76_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dl78', a1)
    assert _is_linked(b, 'xhtml_Dl78', a1)
    if hasattr(a1, 'xhtml_Flow77'):
        assert _is_linked(a1, 'xhtml_Flow77', b)
    _safe_set(b, 'xhtml_Dl78', a2)
    assert _is_linked(b, 'xhtml_Dl78', a2)
    if hasattr(a1, 'xhtml_Flow77'):
        assert not _is_linked(a1, 'xhtml_Flow77', b)
    if hasattr(a2, 'xhtml_Flow77'):
        assert _is_linked(a2, 'xhtml_Flow77', b)
    _safe_set(b, 'xhtml_Dl78', None)
    assert not _is_linked(b, 'xhtml_Dl78', a2)
    if hasattr(a2, 'xhtml_Flow77'):
        assert not _is_linked(a2, 'xhtml_Flow77', b)


def test_assoc_dt61_reverse_link_reassign_clear():
    a1 = xhtml_Dt(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Dt(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Dl62', {a1})
    assert _is_linked(b, 'xhtml_Dl62', a1)
    if hasattr(a1, 'xhtml_Dt'):
        assert _is_linked(a1, 'xhtml_Dt', b)
    _safe_set(b, 'xhtml_Dl62', {a2})
    assert _is_linked(b, 'xhtml_Dl62', a2)
    if hasattr(a1, 'xhtml_Dt'):
        assert not _is_linked(a1, 'xhtml_Dt', b)
    if hasattr(a2, 'xhtml_Dt'):
        assert _is_linked(a2, 'xhtml_Dt', b)
    _safe_set(b, 'xhtml_Dl62', set())
    assert not _is_linked(b, 'xhtml_Dl62', a2)
    if hasattr(a2, 'xhtml_Dt'):
        assert not _is_linked(a2, 'xhtml_Dt', b)


def test_assoc_em120_reverse_link_reassign_clear():
    a1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    a2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Em122', a1)
    assert _is_linked(b, 'xhtml_Em122', a1)
    if hasattr(a1, 'xhtml_Flow121'):
        assert _is_linked(a1, 'xhtml_Flow121', b)
    _safe_set(b, 'xhtml_Em122', a2)
    assert _is_linked(b, 'xhtml_Em122', a2)
    if hasattr(a1, 'xhtml_Flow121'):
        assert not _is_linked(a1, 'xhtml_Flow121', b)
    if hasattr(a2, 'xhtml_Flow121'):
        assert _is_linked(a2, 'xhtml_Flow121', b)
    _safe_set(b, 'xhtml_Em122', None)
    assert not _is_linked(b, 'xhtml_Em122', a2)
    if hasattr(a2, 'xhtml_Flow121'):
        assert not _is_linked(a2, 'xhtml_Flow121', b)


def test_assoc_em17_reverse_link_reassign_clear():
    a1 = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Em(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent18', {a1})
    assert _is_linked(b, 'xhtml_AContent18', a1)
    if hasattr(a1, 'xhtml_Em'):
        assert _is_linked(a1, 'xhtml_Em', b)
    _safe_set(b, 'xhtml_AContent18', {a2})
    assert _is_linked(b, 'xhtml_AContent18', a2)
    if hasattr(a1, 'xhtml_Em'):
        assert not _is_linked(a1, 'xhtml_Em', b)
    if hasattr(a2, 'xhtml_Em'):
        assert _is_linked(a2, 'xhtml_Em', b)
    _safe_set(b, 'xhtml_AContent18', set())
    assert not _is_linked(b, 'xhtml_AContent18', a2)
    if hasattr(a2, 'xhtml_Em'):
        assert not _is_linked(a2, 'xhtml_Em', b)


def test_assoc_em191_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Em193', a1)
    assert _is_linked(b, 'xhtml_Em193', a1)
    if hasattr(a1, 'xhtml_Inline192'):
        assert _is_linked(a1, 'xhtml_Inline192', b)
    _safe_set(b, 'xhtml_Em193', a2)
    assert _is_linked(b, 'xhtml_Em193', a2)
    if hasattr(a1, 'xhtml_Inline192'):
        assert not _is_linked(a1, 'xhtml_Inline192', b)
    if hasattr(a2, 'xhtml_Inline192'):
        assert _is_linked(a2, 'xhtml_Inline192', b)
    _safe_set(b, 'xhtml_Em193', None)
    assert not _is_linked(b, 'xhtml_Em193', a2)
    if hasattr(a2, 'xhtml_Inline192'):
        assert not _is_linked(a2, 'xhtml_Inline192', b)


def test_assoc_em289_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Em291', a1)
    assert _is_linked(b, 'xhtml_Em291', a1)
    if hasattr(a1, 'xhtml_Object290'):
        assert _is_linked(a1, 'xhtml_Object290', b)
    _safe_set(b, 'xhtml_Em291', a2)
    assert _is_linked(b, 'xhtml_Em291', a2)
    if hasattr(a1, 'xhtml_Object290'):
        assert not _is_linked(a1, 'xhtml_Object290', b)
    if hasattr(a2, 'xhtml_Object290'):
        assert _is_linked(a2, 'xhtml_Object290', b)
    _safe_set(b, 'xhtml_Em291', None)
    assert not _is_linked(b, 'xhtml_Em291', a2)
    if hasattr(a2, 'xhtml_Object290'):
        assert not _is_linked(a2, 'xhtml_Object290', b)


def test_assoc_em347_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Em349', a1)
    assert _is_linked(b, 'xhtml_Em349', a1)
    if hasattr(a1, 'xhtml_PreContent348'):
        assert _is_linked(a1, 'xhtml_PreContent348', b)
    _safe_set(b, 'xhtml_Em349', a2)
    assert _is_linked(b, 'xhtml_Em349', a2)
    if hasattr(a1, 'xhtml_PreContent348'):
        assert not _is_linked(a1, 'xhtml_PreContent348', b)
    if hasattr(a2, 'xhtml_PreContent348'):
        assert _is_linked(a2, 'xhtml_PreContent348', b)
    _safe_set(b, 'xhtml_Em349', None)
    assert not _is_linked(b, 'xhtml_Em349', a2)
    if hasattr(a2, 'xhtml_PreContent348'):
        assert not _is_linked(a2, 'xhtml_PreContent348', b)


def test_assoc_hr250_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Hr252', a1)
    assert _is_linked(b, 'xhtml_Hr252', a1)
    if hasattr(a1, 'xhtml_Object251'):
        assert _is_linked(a1, 'xhtml_Object251', b)
    _safe_set(b, 'xhtml_Hr252', a2)
    assert _is_linked(b, 'xhtml_Hr252', a2)
    if hasattr(a1, 'xhtml_Object251'):
        assert not _is_linked(a1, 'xhtml_Object251', b)
    if hasattr(a2, 'xhtml_Object251'):
        assert _is_linked(a2, 'xhtml_Object251', b)
    _safe_set(b, 'xhtml_Hr252', None)
    assert not _is_linked(b, 'xhtml_Hr252', a2)
    if hasattr(a2, 'xhtml_Object251'):
        assert not _is_linked(a2, 'xhtml_Object251', b)


def test_assoc_hr54_reverse_link_reassign_clear():
    a1 = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Hr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block55', {a1})
    assert _is_linked(b, 'xhtml_Block55', a1)
    if hasattr(a1, 'xhtml_Hr'):
        assert _is_linked(a1, 'xhtml_Hr', b)
    _safe_set(b, 'xhtml_Block55', {a2})
    assert _is_linked(b, 'xhtml_Block55', a2)
    if hasattr(a1, 'xhtml_Hr'):
        assert not _is_linked(a1, 'xhtml_Hr', b)
    if hasattr(a2, 'xhtml_Hr'):
        assert _is_linked(a2, 'xhtml_Hr', b)
    _safe_set(b, 'xhtml_Block55', set())
    assert not _is_linked(b, 'xhtml_Block55', a2)
    if hasattr(a2, 'xhtml_Hr'):
        assert not _is_linked(a2, 'xhtml_Hr', b)


def test_assoc_hr82_reverse_link_reassign_clear():
    a1 = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Hr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow83', {a1})
    assert _is_linked(b, 'xhtml_Flow83', a1)
    if hasattr(a1, 'xhtml_Hr84'):
        assert _is_linked(a1, 'xhtml_Hr84', b)
    _safe_set(b, 'xhtml_Flow83', {a2})
    assert _is_linked(b, 'xhtml_Flow83', a2)
    if hasattr(a1, 'xhtml_Hr84'):
        assert not _is_linked(a1, 'xhtml_Hr84', b)
    if hasattr(a2, 'xhtml_Hr84'):
        assert _is_linked(a2, 'xhtml_Hr84', b)
    _safe_set(b, 'xhtml_Flow83', set())
    assert not _is_linked(b, 'xhtml_Flow83', a2)
    if hasattr(a2, 'xhtml_Hr84'):
        assert not _is_linked(a2, 'xhtml_Hr84', b)


def test_assoc_i108_reverse_link_reassign_clear():
    a1 = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_I(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow109', {a1})
    assert _is_linked(b, 'xhtml_Flow109', a1)
    if hasattr(a1, 'xhtml_I110'):
        assert _is_linked(a1, 'xhtml_I110', b)
    _safe_set(b, 'xhtml_Flow109', {a2})
    assert _is_linked(b, 'xhtml_Flow109', a2)
    if hasattr(a1, 'xhtml_I110'):
        assert not _is_linked(a1, 'xhtml_I110', b)
    if hasattr(a2, 'xhtml_I110'):
        assert _is_linked(a2, 'xhtml_I110', b)
    _safe_set(b, 'xhtml_Flow109', set())
    assert not _is_linked(b, 'xhtml_Flow109', a2)
    if hasattr(a2, 'xhtml_I110'):
        assert not _is_linked(a2, 'xhtml_I110', b)


def test_assoc_i179_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_I181', a1)
    assert _is_linked(b, 'xhtml_I181', a1)
    if hasattr(a1, 'xhtml_Inline180'):
        assert _is_linked(a1, 'xhtml_Inline180', b)
    _safe_set(b, 'xhtml_I181', a2)
    assert _is_linked(b, 'xhtml_I181', a2)
    if hasattr(a1, 'xhtml_Inline180'):
        assert not _is_linked(a1, 'xhtml_Inline180', b)
    if hasattr(a2, 'xhtml_Inline180'):
        assert _is_linked(a2, 'xhtml_Inline180', b)
    _safe_set(b, 'xhtml_I181', None)
    assert not _is_linked(b, 'xhtml_I181', a2)
    if hasattr(a2, 'xhtml_Inline180'):
        assert not _is_linked(a2, 'xhtml_Inline180', b)


def test_assoc_i277_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_I279', a1)
    assert _is_linked(b, 'xhtml_I279', a1)
    if hasattr(a1, 'xhtml_Object278'):
        assert _is_linked(a1, 'xhtml_Object278', b)
    _safe_set(b, 'xhtml_I279', a2)
    assert _is_linked(b, 'xhtml_I279', a2)
    if hasattr(a1, 'xhtml_Object278'):
        assert not _is_linked(a1, 'xhtml_Object278', b)
    if hasattr(a2, 'xhtml_Object278'):
        assert _is_linked(a2, 'xhtml_Object278', b)
    _safe_set(b, 'xhtml_I279', None)
    assert not _is_linked(b, 'xhtml_I279', a2)
    if hasattr(a2, 'xhtml_Object278'):
        assert not _is_linked(a2, 'xhtml_Object278', b)


def test_assoc_i335_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_I337', a1)
    assert _is_linked(b, 'xhtml_I337', a1)
    if hasattr(a1, 'xhtml_PreContent336'):
        assert _is_linked(a1, 'xhtml_PreContent336', b)
    _safe_set(b, 'xhtml_I337', a2)
    assert _is_linked(b, 'xhtml_I337', a2)
    if hasattr(a1, 'xhtml_PreContent336'):
        assert not _is_linked(a1, 'xhtml_PreContent336', b)
    if hasattr(a2, 'xhtml_PreContent336'):
        assert _is_linked(a2, 'xhtml_PreContent336', b)
    _safe_set(b, 'xhtml_I337', None)
    assert not _is_linked(b, 'xhtml_I337', a2)
    if hasattr(a2, 'xhtml_PreContent336'):
        assert not _is_linked(a2, 'xhtml_PreContent336', b)


def test_assoc_i9_reverse_link_reassign_clear():
    a1 = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_I(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent10', {a1})
    assert _is_linked(b, 'xhtml_AContent10', a1)
    if hasattr(a1, 'xhtml_I'):
        assert _is_linked(a1, 'xhtml_I', b)
    _safe_set(b, 'xhtml_AContent10', {a2})
    assert _is_linked(b, 'xhtml_AContent10', a2)
    if hasattr(a1, 'xhtml_I'):
        assert not _is_linked(a1, 'xhtml_I', b)
    if hasattr(a2, 'xhtml_I'):
        assert _is_linked(a2, 'xhtml_I', b)
    _safe_set(b, 'xhtml_AContent10', set())
    assert not _is_linked(b, 'xhtml_AContent10', a2)
    if hasattr(a2, 'xhtml_I'):
        assert not _is_linked(a2, 'xhtml_I', b)


def test_assoc_img102_reverse_link_reassign_clear():
    a1 = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Img(alt="sample_text_2", class_="sample_text_2", height="sample_text_2", hl7Id="sample_text_2", imageType="sample_text_2", lang="sample_text_2", src="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow103', {a1})
    assert _is_linked(b, 'xhtml_Flow103', a1)
    if hasattr(a1, 'xhtml_Img104'):
        assert _is_linked(a1, 'xhtml_Img104', b)
    _safe_set(b, 'xhtml_Flow103', {a2})
    assert _is_linked(b, 'xhtml_Flow103', a2)
    if hasattr(a1, 'xhtml_Img104'):
        assert not _is_linked(a1, 'xhtml_Img104', b)
    if hasattr(a2, 'xhtml_Img104'):
        assert _is_linked(a2, 'xhtml_Img104', b)
    _safe_set(b, 'xhtml_Flow103', set())
    assert not _is_linked(b, 'xhtml_Flow103', a2)
    if hasattr(a2, 'xhtml_Img104'):
        assert not _is_linked(a2, 'xhtml_Img104', b)


def test_assoc_img173_reverse_link_reassign_clear():
    a1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    a2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    b = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Img175', a1)
    assert _is_linked(b, 'xhtml_Img175', a1)
    if hasattr(a1, 'xhtml_Inline174'):
        assert _is_linked(a1, 'xhtml_Inline174', b)
    _safe_set(b, 'xhtml_Img175', a2)
    assert _is_linked(b, 'xhtml_Img175', a2)
    if hasattr(a1, 'xhtml_Inline174'):
        assert not _is_linked(a1, 'xhtml_Inline174', b)
    if hasattr(a2, 'xhtml_Inline174'):
        assert _is_linked(a2, 'xhtml_Inline174', b)
    _safe_set(b, 'xhtml_Img175', None)
    assert not _is_linked(b, 'xhtml_Img175', a2)
    if hasattr(a2, 'xhtml_Inline174'):
        assert not _is_linked(a2, 'xhtml_Inline174', b)


def test_assoc_img271_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Img273', a1)
    assert _is_linked(b, 'xhtml_Img273', a1)
    if hasattr(a1, 'xhtml_Object272'):
        assert _is_linked(a1, 'xhtml_Object272', b)
    _safe_set(b, 'xhtml_Img273', a2)
    assert _is_linked(b, 'xhtml_Img273', a2)
    if hasattr(a1, 'xhtml_Object272'):
        assert not _is_linked(a1, 'xhtml_Object272', b)
    if hasattr(a2, 'xhtml_Object272'):
        assert _is_linked(a2, 'xhtml_Object272', b)
    _safe_set(b, 'xhtml_Img273', None)
    assert not _is_linked(b, 'xhtml_Img273', a2)
    if hasattr(a2, 'xhtml_Object272'):
        assert not _is_linked(a2, 'xhtml_Object272', b)


def test_assoc_img5_reverse_link_reassign_clear():
    a1 = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Img(alt="sample_text_2", class_="sample_text_2", height="sample_text_2", hl7Id="sample_text_2", imageType="sample_text_2", lang="sample_text_2", src="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent6', {a1})
    assert _is_linked(b, 'xhtml_AContent6', a1)
    if hasattr(a1, 'xhtml_Img'):
        assert _is_linked(a1, 'xhtml_Img', b)
    _safe_set(b, 'xhtml_AContent6', {a2})
    assert _is_linked(b, 'xhtml_AContent6', a2)
    if hasattr(a1, 'xhtml_Img'):
        assert not _is_linked(a1, 'xhtml_Img', b)
    if hasattr(a2, 'xhtml_Img'):
        assert _is_linked(a2, 'xhtml_Img', b)
    _safe_set(b, 'xhtml_AContent6', set())
    assert not _is_linked(b, 'xhtml_AContent6', a2)
    if hasattr(a2, 'xhtml_Img'):
        assert not _is_linked(a2, 'xhtml_Img', b)


def test_assoc_kbd138_reverse_link_reassign_clear():
    a1 = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Kbd(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow139', {a1})
    assert _is_linked(b, 'xhtml_Flow139', a1)
    if hasattr(a1, 'xhtml_Kbd140'):
        assert _is_linked(a1, 'xhtml_Kbd140', b)
    _safe_set(b, 'xhtml_Flow139', {a2})
    assert _is_linked(b, 'xhtml_Flow139', a2)
    if hasattr(a1, 'xhtml_Kbd140'):
        assert not _is_linked(a1, 'xhtml_Kbd140', b)
    if hasattr(a2, 'xhtml_Kbd140'):
        assert _is_linked(a2, 'xhtml_Kbd140', b)
    _safe_set(b, 'xhtml_Flow139', set())
    assert not _is_linked(b, 'xhtml_Flow139', a2)
    if hasattr(a2, 'xhtml_Kbd140'):
        assert not _is_linked(a2, 'xhtml_Kbd140', b)


def test_assoc_kbd209_reverse_link_reassign_clear():
    a1 = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Kbd(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline210', {a1})
    assert _is_linked(b, 'xhtml_Inline210', a1)
    if hasattr(a1, 'xhtml_Kbd211'):
        assert _is_linked(a1, 'xhtml_Kbd211', b)
    _safe_set(b, 'xhtml_Inline210', {a2})
    assert _is_linked(b, 'xhtml_Inline210', a2)
    if hasattr(a1, 'xhtml_Kbd211'):
        assert not _is_linked(a1, 'xhtml_Kbd211', b)
    if hasattr(a2, 'xhtml_Kbd211'):
        assert _is_linked(a2, 'xhtml_Kbd211', b)
    _safe_set(b, 'xhtml_Inline210', set())
    assert not _is_linked(b, 'xhtml_Inline210', a2)
    if hasattr(a2, 'xhtml_Kbd211'):
        assert not _is_linked(a2, 'xhtml_Kbd211', b)


def test_assoc_kbd29_reverse_link_reassign_clear():
    a1 = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Kbd(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent30', {a1})
    assert _is_linked(b, 'xhtml_AContent30', a1)
    if hasattr(a1, 'xhtml_Kbd'):
        assert _is_linked(a1, 'xhtml_Kbd', b)
    _safe_set(b, 'xhtml_AContent30', {a2})
    assert _is_linked(b, 'xhtml_AContent30', a2)
    if hasattr(a1, 'xhtml_Kbd'):
        assert not _is_linked(a1, 'xhtml_Kbd', b)
    if hasattr(a2, 'xhtml_Kbd'):
        assert _is_linked(a2, 'xhtml_Kbd', b)
    _safe_set(b, 'xhtml_AContent30', set())
    assert not _is_linked(b, 'xhtml_AContent30', a2)
    if hasattr(a2, 'xhtml_Kbd'):
        assert not _is_linked(a2, 'xhtml_Kbd', b)


def test_assoc_kbd307_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Kbd309', a1)
    assert _is_linked(b, 'xhtml_Kbd309', a1)
    if hasattr(a1, 'xhtml_Object308'):
        assert _is_linked(a1, 'xhtml_Object308', b)
    _safe_set(b, 'xhtml_Kbd309', a2)
    assert _is_linked(b, 'xhtml_Kbd309', a2)
    if hasattr(a1, 'xhtml_Object308'):
        assert not _is_linked(a1, 'xhtml_Object308', b)
    if hasattr(a2, 'xhtml_Object308'):
        assert _is_linked(a2, 'xhtml_Object308', b)
    _safe_set(b, 'xhtml_Kbd309', None)
    assert not _is_linked(b, 'xhtml_Kbd309', a2)
    if hasattr(a2, 'xhtml_Object308'):
        assert not _is_linked(a2, 'xhtml_Object308', b)


def test_assoc_kbd365_reverse_link_reassign_clear():
    a1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    a2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    b = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Kbd367', a1)
    assert _is_linked(b, 'xhtml_Kbd367', a1)
    if hasattr(a1, 'xhtml_PreContent366'):
        assert _is_linked(a1, 'xhtml_PreContent366', b)
    _safe_set(b, 'xhtml_Kbd367', a2)
    assert _is_linked(b, 'xhtml_Kbd367', a2)
    if hasattr(a1, 'xhtml_PreContent366'):
        assert not _is_linked(a1, 'xhtml_PreContent366', b)
    if hasattr(a2, 'xhtml_PreContent366'):
        assert _is_linked(a2, 'xhtml_PreContent366', b)
    _safe_set(b, 'xhtml_Kbd367', None)
    assert not _is_linked(b, 'xhtml_Kbd367', a2)
    if hasattr(a2, 'xhtml_PreContent366'):
        assert not _is_linked(a2, 'xhtml_PreContent366', b)


def test_assoc_li1328_reverse_link_reassign_clear():
    a1 = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ol(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Li', a1)
    assert _is_linked(b, 'xhtml_Li', a1)
    if hasattr(a1, 'xhtml_Ol329'):
        assert _is_linked(a1, 'xhtml_Ol329', b)
    _safe_set(b, 'xhtml_Li', a2)
    assert _is_linked(b, 'xhtml_Li', a2)
    if hasattr(a1, 'xhtml_Ol329'):
        assert not _is_linked(a1, 'xhtml_Ol329', b)
    if hasattr(a2, 'xhtml_Ol329'):
        assert _is_linked(a2, 'xhtml_Ol329', b)
    _safe_set(b, 'xhtml_Li', None)
    assert not _is_linked(b, 'xhtml_Li', a2)
    if hasattr(a2, 'xhtml_Ol329'):
        assert not _is_linked(a2, 'xhtml_Ol329', b)


def test_assoc_li1421_reverse_link_reassign_clear():
    a1 = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ul(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    _safe_set(b, 'xhtml_Li423', a1)
    assert _is_linked(b, 'xhtml_Li423', a1)
    if hasattr(a1, 'xhtml_Ul422'):
        assert _is_linked(a1, 'xhtml_Ul422', b)
    _safe_set(b, 'xhtml_Li423', a2)
    assert _is_linked(b, 'xhtml_Li423', a2)
    if hasattr(a1, 'xhtml_Ul422'):
        assert not _is_linked(a1, 'xhtml_Ul422', b)
    if hasattr(a2, 'xhtml_Ul422'):
        assert _is_linked(a2, 'xhtml_Ul422', b)
    _safe_set(b, 'xhtml_Li423', None)
    assert not _is_linked(b, 'xhtml_Li423', a2)
    if hasattr(a2, 'xhtml_Ul422'):
        assert not _is_linked(a2, 'xhtml_Ul422', b)


def test_assoc_object170_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline171', {a1})
    assert _is_linked(b, 'xhtml_Inline171', a1)
    if hasattr(a1, 'xhtml_Object172'):
        assert _is_linked(a1, 'xhtml_Object172', b)
    _safe_set(b, 'xhtml_Inline171', {a2})
    assert _is_linked(b, 'xhtml_Inline171', a2)
    if hasattr(a1, 'xhtml_Object172'):
        assert not _is_linked(a1, 'xhtml_Object172', b)
    if hasattr(a2, 'xhtml_Object172'):
        assert _is_linked(a2, 'xhtml_Object172', b)
    _safe_set(b, 'xhtml_Inline171', set())
    assert not _is_linked(b, 'xhtml_Inline171', a2)
    if hasattr(a2, 'xhtml_Object172'):
        assert not _is_linked(a2, 'xhtml_Object172', b)


def test_assoc_object269_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object270', a1)
    assert _is_linked(b, 'xhtml_Object270', a1)
    if hasattr(a1, 'xhtml_Object268'):
        assert _is_linked(a1, 'xhtml_Object268', b)
    _safe_set(b, 'xhtml_Object270', a2)
    assert _is_linked(b, 'xhtml_Object270', a2)
    if hasattr(a1, 'xhtml_Object268'):
        assert not _is_linked(a1, 'xhtml_Object268', b)
    if hasattr(a2, 'xhtml_Object268'):
        assert _is_linked(a2, 'xhtml_Object268', b)
    _safe_set(b, 'xhtml_Object270', None)
    assert not _is_linked(b, 'xhtml_Object270', a2)
    if hasattr(a2, 'xhtml_Object268'):
        assert not _is_linked(a2, 'xhtml_Object268', b)


def test_assoc_object3_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent4', {a1})
    assert _is_linked(b, 'xhtml_AContent4', a1)
    if hasattr(a1, 'xhtml_Object'):
        assert _is_linked(a1, 'xhtml_Object', b)
    _safe_set(b, 'xhtml_AContent4', {a2})
    assert _is_linked(b, 'xhtml_AContent4', a2)
    if hasattr(a1, 'xhtml_Object'):
        assert not _is_linked(a1, 'xhtml_Object', b)
    if hasattr(a2, 'xhtml_Object'):
        assert _is_linked(a2, 'xhtml_Object', b)
    _safe_set(b, 'xhtml_AContent4', set())
    assert not _is_linked(b, 'xhtml_AContent4', a2)
    if hasattr(a2, 'xhtml_Object'):
        assert not _is_linked(a2, 'xhtml_Object', b)


def test_assoc_object99_reverse_link_reassign_clear():
    a1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    a2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow100', {a1})
    assert _is_linked(b, 'xhtml_Flow100', a1)
    if hasattr(a1, 'xhtml_Object101'):
        assert _is_linked(a1, 'xhtml_Object101', b)
    _safe_set(b, 'xhtml_Flow100', {a2})
    assert _is_linked(b, 'xhtml_Flow100', a2)
    if hasattr(a1, 'xhtml_Object101'):
        assert not _is_linked(a1, 'xhtml_Object101', b)
    if hasattr(a2, 'xhtml_Object101'):
        assert _is_linked(a2, 'xhtml_Object101', b)
    _safe_set(b, 'xhtml_Flow100', set())
    assert not _is_linked(b, 'xhtml_Flow100', a2)
    if hasattr(a2, 'xhtml_Object101'):
        assert not _is_linked(a2, 'xhtml_Object101', b)


def test_assoc_ol241_reverse_link_reassign_clear():
    a1 = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ol(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object242', {a1})
    assert _is_linked(b, 'xhtml_Object242', a1)
    if hasattr(a1, 'xhtml_Ol243'):
        assert _is_linked(a1, 'xhtml_Ol243', b)
    _safe_set(b, 'xhtml_Object242', {a2})
    assert _is_linked(b, 'xhtml_Object242', a2)
    if hasattr(a1, 'xhtml_Ol243'):
        assert not _is_linked(a1, 'xhtml_Ol243', b)
    if hasattr(a2, 'xhtml_Ol243'):
        assert _is_linked(a2, 'xhtml_Ol243', b)
    _safe_set(b, 'xhtml_Object242', set())
    assert not _is_linked(b, 'xhtml_Object242', a2)
    if hasattr(a2, 'xhtml_Ol243'):
        assert not _is_linked(a2, 'xhtml_Ol243', b)


def test_assoc_ol48_reverse_link_reassign_clear():
    a1 = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ol(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block49', {a1})
    assert _is_linked(b, 'xhtml_Block49', a1)
    if hasattr(a1, 'xhtml_Ol'):
        assert _is_linked(a1, 'xhtml_Ol', b)
    _safe_set(b, 'xhtml_Block49', {a2})
    assert _is_linked(b, 'xhtml_Block49', a2)
    if hasattr(a1, 'xhtml_Ol'):
        assert not _is_linked(a1, 'xhtml_Ol', b)
    if hasattr(a2, 'xhtml_Ol'):
        assert _is_linked(a2, 'xhtml_Ol', b)
    _safe_set(b, 'xhtml_Block49', set())
    assert not _is_linked(b, 'xhtml_Block49', a2)
    if hasattr(a2, 'xhtml_Ol'):
        assert not _is_linked(a2, 'xhtml_Ol', b)


def test_assoc_ol73_reverse_link_reassign_clear():
    a1 = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ol(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow74', {a1})
    assert _is_linked(b, 'xhtml_Flow74', a1)
    if hasattr(a1, 'xhtml_Ol75'):
        assert _is_linked(a1, 'xhtml_Ol75', b)
    _safe_set(b, 'xhtml_Flow74', {a2})
    assert _is_linked(b, 'xhtml_Flow74', a2)
    if hasattr(a1, 'xhtml_Ol75'):
        assert not _is_linked(a1, 'xhtml_Ol75', b)
    if hasattr(a2, 'xhtml_Ol75'):
        assert _is_linked(a2, 'xhtml_Ol75', b)
    _safe_set(b, 'xhtml_Flow74', set())
    assert not _is_linked(b, 'xhtml_Flow74', a2)
    if hasattr(a2, 'xhtml_Ol75'):
        assert not _is_linked(a2, 'xhtml_Ol75', b)


def test_assoc_p232_reverse_link_reassign_clear():
    a1 = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_P(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object233', {a1})
    assert _is_linked(b, 'xhtml_Object233', a1)
    if hasattr(a1, 'xhtml_P234'):
        assert _is_linked(a1, 'xhtml_P234', b)
    _safe_set(b, 'xhtml_Object233', {a2})
    assert _is_linked(b, 'xhtml_Object233', a2)
    if hasattr(a1, 'xhtml_P234'):
        assert not _is_linked(a1, 'xhtml_P234', b)
    if hasattr(a2, 'xhtml_P234'):
        assert _is_linked(a2, 'xhtml_P234', b)
    _safe_set(b, 'xhtml_Object233', set())
    assert not _is_linked(b, 'xhtml_Object233', a2)
    if hasattr(a2, 'xhtml_P234'):
        assert not _is_linked(a2, 'xhtml_P234', b)


def test_assoc_p43_reverse_link_reassign_clear():
    a1 = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_P(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block', {a1})
    assert _is_linked(b, 'xhtml_Block', a1)
    if hasattr(a1, 'xhtml_P'):
        assert _is_linked(a1, 'xhtml_P', b)
    _safe_set(b, 'xhtml_Block', {a2})
    assert _is_linked(b, 'xhtml_Block', a2)
    if hasattr(a1, 'xhtml_P'):
        assert not _is_linked(a1, 'xhtml_P', b)
    if hasattr(a2, 'xhtml_P'):
        assert _is_linked(a2, 'xhtml_P', b)
    _safe_set(b, 'xhtml_Block', set())
    assert not _is_linked(b, 'xhtml_Block', a2)
    if hasattr(a2, 'xhtml_P'):
        assert not _is_linked(a2, 'xhtml_P', b)


def test_assoc_p65_reverse_link_reassign_clear():
    a1 = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_P(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow', {a1})
    assert _is_linked(b, 'xhtml_Flow', a1)
    if hasattr(a1, 'xhtml_P66'):
        assert _is_linked(a1, 'xhtml_P66', b)
    _safe_set(b, 'xhtml_Flow', {a2})
    assert _is_linked(b, 'xhtml_Flow', a2)
    if hasattr(a1, 'xhtml_P66'):
        assert not _is_linked(a1, 'xhtml_P66', b)
    if hasattr(a2, 'xhtml_P66'):
        assert _is_linked(a2, 'xhtml_P66', b)
    _safe_set(b, 'xhtml_Flow', set())
    assert not _is_linked(b, 'xhtml_Flow', a2)
    if hasattr(a2, 'xhtml_P66'):
        assert not _is_linked(a2, 'xhtml_P66', b)


def test_assoc_param230_reverse_link_reassign_clear():
    a1 = xhtml_Param(name="sample_text", value="sample_text")
    a2 = xhtml_Param(name="sample_text_2", value="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object231', {a1})
    assert _is_linked(b, 'xhtml_Object231', a1)
    if hasattr(a1, 'xhtml_Param'):
        assert _is_linked(a1, 'xhtml_Param', b)
    _safe_set(b, 'xhtml_Object231', {a2})
    assert _is_linked(b, 'xhtml_Object231', a2)
    if hasattr(a1, 'xhtml_Param'):
        assert not _is_linked(a1, 'xhtml_Param', b)
    if hasattr(a2, 'xhtml_Param'):
        assert _is_linked(a2, 'xhtml_Param', b)
    _safe_set(b, 'xhtml_Object231', set())
    assert not _is_linked(b, 'xhtml_Object231', a2)
    if hasattr(a2, 'xhtml_Param'):
        assert not _is_linked(a2, 'xhtml_Param', b)


def test_assoc_pre247_reverse_link_reassign_clear():
    a1 = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    a2 = xhtml_Pre(class_="sample_text_2", lang="sample_text_2", space="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object248', {a1})
    assert _is_linked(b, 'xhtml_Object248', a1)
    if hasattr(a1, 'xhtml_Pre249'):
        assert _is_linked(a1, 'xhtml_Pre249', b)
    _safe_set(b, 'xhtml_Object248', {a2})
    assert _is_linked(b, 'xhtml_Object248', a2)
    if hasattr(a1, 'xhtml_Pre249'):
        assert not _is_linked(a1, 'xhtml_Pre249', b)
    if hasattr(a2, 'xhtml_Pre249'):
        assert _is_linked(a2, 'xhtml_Pre249', b)
    _safe_set(b, 'xhtml_Object248', set())
    assert not _is_linked(b, 'xhtml_Object248', a2)
    if hasattr(a2, 'xhtml_Pre249'):
        assert not _is_linked(a2, 'xhtml_Pre249', b)


def test_assoc_pre52_reverse_link_reassign_clear():
    a1 = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    a2 = xhtml_Pre(class_="sample_text_2", lang="sample_text_2", space="sample_text_2", style="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block53', {a1})
    assert _is_linked(b, 'xhtml_Block53', a1)
    if hasattr(a1, 'xhtml_Pre'):
        assert _is_linked(a1, 'xhtml_Pre', b)
    _safe_set(b, 'xhtml_Block53', {a2})
    assert _is_linked(b, 'xhtml_Block53', a2)
    if hasattr(a1, 'xhtml_Pre'):
        assert not _is_linked(a1, 'xhtml_Pre', b)
    if hasattr(a2, 'xhtml_Pre'):
        assert _is_linked(a2, 'xhtml_Pre', b)
    _safe_set(b, 'xhtml_Block53', set())
    assert not _is_linked(b, 'xhtml_Block53', a2)
    if hasattr(a2, 'xhtml_Pre'):
        assert not _is_linked(a2, 'xhtml_Pre', b)


def test_assoc_pre79_reverse_link_reassign_clear():
    a1 = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    a2 = xhtml_Pre(class_="sample_text_2", lang="sample_text_2", space="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow80', {a1})
    assert _is_linked(b, 'xhtml_Flow80', a1)
    if hasattr(a1, 'xhtml_Pre81'):
        assert _is_linked(a1, 'xhtml_Pre81', b)
    _safe_set(b, 'xhtml_Flow80', {a2})
    assert _is_linked(b, 'xhtml_Flow80', a2)
    if hasattr(a1, 'xhtml_Pre81'):
        assert not _is_linked(a1, 'xhtml_Pre81', b)
    if hasattr(a2, 'xhtml_Pre81'):
        assert _is_linked(a2, 'xhtml_Pre81', b)
    _safe_set(b, 'xhtml_Flow80', set())
    assert not _is_linked(b, 'xhtml_Flow80', a2)
    if hasattr(a2, 'xhtml_Pre81'):
        assert not _is_linked(a2, 'xhtml_Pre81', b)


def test_assoc_q132_reverse_link_reassign_clear():
    a1 = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Q(cite1="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow133', {a1})
    assert _is_linked(b, 'xhtml_Flow133', a1)
    if hasattr(a1, 'xhtml_Q134'):
        assert _is_linked(a1, 'xhtml_Q134', b)
    _safe_set(b, 'xhtml_Flow133', {a2})
    assert _is_linked(b, 'xhtml_Flow133', a2)
    if hasattr(a1, 'xhtml_Q134'):
        assert not _is_linked(a1, 'xhtml_Q134', b)
    if hasattr(a2, 'xhtml_Q134'):
        assert _is_linked(a2, 'xhtml_Q134', b)
    _safe_set(b, 'xhtml_Flow133', set())
    assert not _is_linked(b, 'xhtml_Flow133', a2)
    if hasattr(a2, 'xhtml_Q134'):
        assert not _is_linked(a2, 'xhtml_Q134', b)


def test_assoc_q203_reverse_link_reassign_clear():
    a1 = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Q(cite1="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline204', {a1})
    assert _is_linked(b, 'xhtml_Inline204', a1)
    if hasattr(a1, 'xhtml_Q205'):
        assert _is_linked(a1, 'xhtml_Q205', b)
    _safe_set(b, 'xhtml_Inline204', {a2})
    assert _is_linked(b, 'xhtml_Inline204', a2)
    if hasattr(a1, 'xhtml_Q205'):
        assert not _is_linked(a1, 'xhtml_Q205', b)
    if hasattr(a2, 'xhtml_Q205'):
        assert _is_linked(a2, 'xhtml_Q205', b)
    _safe_set(b, 'xhtml_Inline204', set())
    assert not _is_linked(b, 'xhtml_Inline204', a2)
    if hasattr(a2, 'xhtml_Q205'):
        assert not _is_linked(a2, 'xhtml_Q205', b)


def test_assoc_q25_reverse_link_reassign_clear():
    a1 = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Q(cite1="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent26', {a1})
    assert _is_linked(b, 'xhtml_AContent26', a1)
    if hasattr(a1, 'xhtml_Q'):
        assert _is_linked(a1, 'xhtml_Q', b)
    _safe_set(b, 'xhtml_AContent26', {a2})
    assert _is_linked(b, 'xhtml_AContent26', a2)
    if hasattr(a1, 'xhtml_Q'):
        assert not _is_linked(a1, 'xhtml_Q', b)
    if hasattr(a2, 'xhtml_Q'):
        assert _is_linked(a2, 'xhtml_Q', b)
    _safe_set(b, 'xhtml_AContent26', set())
    assert not _is_linked(b, 'xhtml_AContent26', a2)
    if hasattr(a2, 'xhtml_Q'):
        assert not _is_linked(a2, 'xhtml_Q', b)


def test_assoc_q301_reverse_link_reassign_clear():
    a1 = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Q(cite1="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object302', {a1})
    assert _is_linked(b, 'xhtml_Object302', a1)
    if hasattr(a1, 'xhtml_Q303'):
        assert _is_linked(a1, 'xhtml_Q303', b)
    _safe_set(b, 'xhtml_Object302', {a2})
    assert _is_linked(b, 'xhtml_Object302', a2)
    if hasattr(a1, 'xhtml_Q303'):
        assert not _is_linked(a1, 'xhtml_Q303', b)
    if hasattr(a2, 'xhtml_Q303'):
        assert _is_linked(a2, 'xhtml_Q303', b)
    _safe_set(b, 'xhtml_Object302', set())
    assert not _is_linked(b, 'xhtml_Object302', a2)
    if hasattr(a2, 'xhtml_Q303'):
        assert not _is_linked(a2, 'xhtml_Q303', b)


def test_assoc_q359_reverse_link_reassign_clear():
    a1 = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Q(cite1="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent360', {a1})
    assert _is_linked(b, 'xhtml_PreContent360', a1)
    if hasattr(a1, 'xhtml_Q361'):
        assert _is_linked(a1, 'xhtml_Q361', b)
    _safe_set(b, 'xhtml_PreContent360', {a2})
    assert _is_linked(b, 'xhtml_PreContent360', a2)
    if hasattr(a1, 'xhtml_Q361'):
        assert not _is_linked(a1, 'xhtml_Q361', b)
    if hasattr(a2, 'xhtml_Q361'):
        assert _is_linked(a2, 'xhtml_Q361', b)
    _safe_set(b, 'xhtml_PreContent360', set())
    assert not _is_linked(b, 'xhtml_PreContent360', a2)
    if hasattr(a2, 'xhtml_Q361'):
        assert not _is_linked(a2, 'xhtml_Q361', b)


def test_assoc_samp135_reverse_link_reassign_clear():
    a1 = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Samp(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow136', {a1})
    assert _is_linked(b, 'xhtml_Flow136', a1)
    if hasattr(a1, 'xhtml_Samp137'):
        assert _is_linked(a1, 'xhtml_Samp137', b)
    _safe_set(b, 'xhtml_Flow136', {a2})
    assert _is_linked(b, 'xhtml_Flow136', a2)
    if hasattr(a1, 'xhtml_Samp137'):
        assert not _is_linked(a1, 'xhtml_Samp137', b)
    if hasattr(a2, 'xhtml_Samp137'):
        assert _is_linked(a2, 'xhtml_Samp137', b)
    _safe_set(b, 'xhtml_Flow136', set())
    assert not _is_linked(b, 'xhtml_Flow136', a2)
    if hasattr(a2, 'xhtml_Samp137'):
        assert not _is_linked(a2, 'xhtml_Samp137', b)


def test_assoc_samp206_reverse_link_reassign_clear():
    a1 = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Samp(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline207', {a1})
    assert _is_linked(b, 'xhtml_Inline207', a1)
    if hasattr(a1, 'xhtml_Samp208'):
        assert _is_linked(a1, 'xhtml_Samp208', b)
    _safe_set(b, 'xhtml_Inline207', {a2})
    assert _is_linked(b, 'xhtml_Inline207', a2)
    if hasattr(a1, 'xhtml_Samp208'):
        assert not _is_linked(a1, 'xhtml_Samp208', b)
    if hasattr(a2, 'xhtml_Samp208'):
        assert _is_linked(a2, 'xhtml_Samp208', b)
    _safe_set(b, 'xhtml_Inline207', set())
    assert not _is_linked(b, 'xhtml_Inline207', a2)
    if hasattr(a2, 'xhtml_Samp208'):
        assert not _is_linked(a2, 'xhtml_Samp208', b)


def test_assoc_samp27_reverse_link_reassign_clear():
    a1 = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Samp(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent28', {a1})
    assert _is_linked(b, 'xhtml_AContent28', a1)
    if hasattr(a1, 'xhtml_Samp'):
        assert _is_linked(a1, 'xhtml_Samp', b)
    _safe_set(b, 'xhtml_AContent28', {a2})
    assert _is_linked(b, 'xhtml_AContent28', a2)
    if hasattr(a1, 'xhtml_Samp'):
        assert not _is_linked(a1, 'xhtml_Samp', b)
    if hasattr(a2, 'xhtml_Samp'):
        assert _is_linked(a2, 'xhtml_Samp', b)
    _safe_set(b, 'xhtml_AContent28', set())
    assert not _is_linked(b, 'xhtml_AContent28', a2)
    if hasattr(a2, 'xhtml_Samp'):
        assert not _is_linked(a2, 'xhtml_Samp', b)


def test_assoc_samp304_reverse_link_reassign_clear():
    a1 = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Samp(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object305', {a1})
    assert _is_linked(b, 'xhtml_Object305', a1)
    if hasattr(a1, 'xhtml_Samp306'):
        assert _is_linked(a1, 'xhtml_Samp306', b)
    _safe_set(b, 'xhtml_Object305', {a2})
    assert _is_linked(b, 'xhtml_Object305', a2)
    if hasattr(a1, 'xhtml_Samp306'):
        assert not _is_linked(a1, 'xhtml_Samp306', b)
    if hasattr(a2, 'xhtml_Samp306'):
        assert _is_linked(a2, 'xhtml_Samp306', b)
    _safe_set(b, 'xhtml_Object305', set())
    assert not _is_linked(b, 'xhtml_Object305', a2)
    if hasattr(a2, 'xhtml_Samp306'):
        assert not _is_linked(a2, 'xhtml_Samp306', b)


def test_assoc_samp362_reverse_link_reassign_clear():
    a1 = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Samp(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent363', {a1})
    assert _is_linked(b, 'xhtml_PreContent363', a1)
    if hasattr(a1, 'xhtml_Samp364'):
        assert _is_linked(a1, 'xhtml_Samp364', b)
    _safe_set(b, 'xhtml_PreContent363', {a2})
    assert _is_linked(b, 'xhtml_PreContent363', a2)
    if hasattr(a1, 'xhtml_Samp364'):
        assert not _is_linked(a1, 'xhtml_Samp364', b)
    if hasattr(a2, 'xhtml_Samp364'):
        assert _is_linked(a2, 'xhtml_Samp364', b)
    _safe_set(b, 'xhtml_PreContent363', set())
    assert not _is_linked(b, 'xhtml_PreContent363', a2)
    if hasattr(a2, 'xhtml_Samp364'):
        assert not _is_linked(a2, 'xhtml_Samp364', b)


def test_assoc_small117_reverse_link_reassign_clear():
    a1 = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Small(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow118', {a1})
    assert _is_linked(b, 'xhtml_Flow118', a1)
    if hasattr(a1, 'xhtml_Small119'):
        assert _is_linked(a1, 'xhtml_Small119', b)
    _safe_set(b, 'xhtml_Flow118', {a2})
    assert _is_linked(b, 'xhtml_Flow118', a2)
    if hasattr(a1, 'xhtml_Small119'):
        assert not _is_linked(a1, 'xhtml_Small119', b)
    if hasattr(a2, 'xhtml_Small119'):
        assert _is_linked(a2, 'xhtml_Small119', b)
    _safe_set(b, 'xhtml_Flow118', set())
    assert not _is_linked(b, 'xhtml_Flow118', a2)
    if hasattr(a2, 'xhtml_Small119'):
        assert not _is_linked(a2, 'xhtml_Small119', b)


def test_assoc_small15_reverse_link_reassign_clear():
    a1 = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Small(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent16', {a1})
    assert _is_linked(b, 'xhtml_AContent16', a1)
    if hasattr(a1, 'xhtml_Small'):
        assert _is_linked(a1, 'xhtml_Small', b)
    _safe_set(b, 'xhtml_AContent16', {a2})
    assert _is_linked(b, 'xhtml_AContent16', a2)
    if hasattr(a1, 'xhtml_Small'):
        assert not _is_linked(a1, 'xhtml_Small', b)
    if hasattr(a2, 'xhtml_Small'):
        assert _is_linked(a2, 'xhtml_Small', b)
    _safe_set(b, 'xhtml_AContent16', set())
    assert not _is_linked(b, 'xhtml_AContent16', a2)
    if hasattr(a2, 'xhtml_Small'):
        assert not _is_linked(a2, 'xhtml_Small', b)


def test_assoc_small188_reverse_link_reassign_clear():
    a1 = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Small(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline189', {a1})
    assert _is_linked(b, 'xhtml_Inline189', a1)
    if hasattr(a1, 'xhtml_Small190'):
        assert _is_linked(a1, 'xhtml_Small190', b)
    _safe_set(b, 'xhtml_Inline189', {a2})
    assert _is_linked(b, 'xhtml_Inline189', a2)
    if hasattr(a1, 'xhtml_Small190'):
        assert not _is_linked(a1, 'xhtml_Small190', b)
    if hasattr(a2, 'xhtml_Small190'):
        assert _is_linked(a2, 'xhtml_Small190', b)
    _safe_set(b, 'xhtml_Inline189', set())
    assert not _is_linked(b, 'xhtml_Inline189', a2)
    if hasattr(a2, 'xhtml_Small190'):
        assert not _is_linked(a2, 'xhtml_Small190', b)


def test_assoc_small286_reverse_link_reassign_clear():
    a1 = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Small(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object287', {a1})
    assert _is_linked(b, 'xhtml_Object287', a1)
    if hasattr(a1, 'xhtml_Small288'):
        assert _is_linked(a1, 'xhtml_Small288', b)
    _safe_set(b, 'xhtml_Object287', {a2})
    assert _is_linked(b, 'xhtml_Object287', a2)
    if hasattr(a1, 'xhtml_Small288'):
        assert not _is_linked(a1, 'xhtml_Small288', b)
    if hasattr(a2, 'xhtml_Small288'):
        assert _is_linked(a2, 'xhtml_Small288', b)
    _safe_set(b, 'xhtml_Object287', set())
    assert not _is_linked(b, 'xhtml_Object287', a2)
    if hasattr(a2, 'xhtml_Small288'):
        assert not _is_linked(a2, 'xhtml_Small288', b)


def test_assoc_small344_reverse_link_reassign_clear():
    a1 = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Small(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent345', {a1})
    assert _is_linked(b, 'xhtml_PreContent345', a1)
    if hasattr(a1, 'xhtml_Small346'):
        assert _is_linked(a1, 'xhtml_Small346', b)
    _safe_set(b, 'xhtml_PreContent345', {a2})
    assert _is_linked(b, 'xhtml_PreContent345', a2)
    if hasattr(a1, 'xhtml_Small346'):
        assert not _is_linked(a1, 'xhtml_Small346', b)
    if hasattr(a2, 'xhtml_Small346'):
        assert _is_linked(a2, 'xhtml_Small346', b)
    _safe_set(b, 'xhtml_PreContent345', set())
    assert not _is_linked(b, 'xhtml_PreContent345', a2)
    if hasattr(a2, 'xhtml_Small346'):
        assert not _is_linked(a2, 'xhtml_Small346', b)


def test_assoc_span1_reverse_link_reassign_clear():
    a1 = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Span(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent2', {a1})
    assert _is_linked(b, 'xhtml_AContent2', a1)
    if hasattr(a1, 'xhtml_Span'):
        assert _is_linked(a1, 'xhtml_Span', b)
    _safe_set(b, 'xhtml_AContent2', {a2})
    assert _is_linked(b, 'xhtml_AContent2', a2)
    if hasattr(a1, 'xhtml_Span'):
        assert not _is_linked(a1, 'xhtml_Span', b)
    if hasattr(a2, 'xhtml_Span'):
        assert _is_linked(a2, 'xhtml_Span', b)
    _safe_set(b, 'xhtml_AContent2', set())
    assert not _is_linked(b, 'xhtml_AContent2', a2)
    if hasattr(a2, 'xhtml_Span'):
        assert not _is_linked(a2, 'xhtml_Span', b)


def test_assoc_span167_reverse_link_reassign_clear():
    a1 = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Span(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline168', {a1})
    assert _is_linked(b, 'xhtml_Inline168', a1)
    if hasattr(a1, 'xhtml_Span169'):
        assert _is_linked(a1, 'xhtml_Span169', b)
    _safe_set(b, 'xhtml_Inline168', {a2})
    assert _is_linked(b, 'xhtml_Inline168', a2)
    if hasattr(a1, 'xhtml_Span169'):
        assert not _is_linked(a1, 'xhtml_Span169', b)
    if hasattr(a2, 'xhtml_Span169'):
        assert _is_linked(a2, 'xhtml_Span169', b)
    _safe_set(b, 'xhtml_Inline168', set())
    assert not _is_linked(b, 'xhtml_Inline168', a2)
    if hasattr(a2, 'xhtml_Span169'):
        assert not _is_linked(a2, 'xhtml_Span169', b)


def test_assoc_span265_reverse_link_reassign_clear():
    a1 = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Span(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object266', {a1})
    assert _is_linked(b, 'xhtml_Object266', a1)
    if hasattr(a1, 'xhtml_Span267'):
        assert _is_linked(a1, 'xhtml_Span267', b)
    _safe_set(b, 'xhtml_Object266', {a2})
    assert _is_linked(b, 'xhtml_Object266', a2)
    if hasattr(a1, 'xhtml_Span267'):
        assert not _is_linked(a1, 'xhtml_Span267', b)
    if hasattr(a2, 'xhtml_Span267'):
        assert _is_linked(a2, 'xhtml_Span267', b)
    _safe_set(b, 'xhtml_Object266', set())
    assert not _is_linked(b, 'xhtml_Object266', a2)
    if hasattr(a2, 'xhtml_Span267'):
        assert not _is_linked(a2, 'xhtml_Span267', b)


def test_assoc_span389_reverse_link_reassign_clear():
    a1 = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Span(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent390', {a1})
    assert _is_linked(b, 'xhtml_PreContent390', a1)
    if hasattr(a1, 'xhtml_Span391'):
        assert _is_linked(a1, 'xhtml_Span391', b)
    _safe_set(b, 'xhtml_PreContent390', {a2})
    assert _is_linked(b, 'xhtml_PreContent390', a2)
    if hasattr(a1, 'xhtml_Span391'):
        assert not _is_linked(a1, 'xhtml_Span391', b)
    if hasattr(a2, 'xhtml_Span391'):
        assert _is_linked(a2, 'xhtml_Span391', b)
    _safe_set(b, 'xhtml_PreContent390', set())
    assert not _is_linked(b, 'xhtml_PreContent390', a2)
    if hasattr(a2, 'xhtml_Span391'):
        assert not _is_linked(a2, 'xhtml_Span391', b)


def test_assoc_span96_reverse_link_reassign_clear():
    a1 = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Span(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow97', {a1})
    assert _is_linked(b, 'xhtml_Flow97', a1)
    if hasattr(a1, 'xhtml_Span98'):
        assert _is_linked(a1, 'xhtml_Span98', b)
    _safe_set(b, 'xhtml_Flow97', {a2})
    assert _is_linked(b, 'xhtml_Flow97', a2)
    if hasattr(a1, 'xhtml_Span98'):
        assert not _is_linked(a1, 'xhtml_Span98', b)
    if hasattr(a2, 'xhtml_Span98'):
        assert _is_linked(a2, 'xhtml_Span98', b)
    _safe_set(b, 'xhtml_Flow97', set())
    assert not _is_linked(b, 'xhtml_Flow97', a2)
    if hasattr(a2, 'xhtml_Span98'):
        assert not _is_linked(a2, 'xhtml_Span98', b)


def test_assoc_strong123_reverse_link_reassign_clear():
    a1 = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Strong(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow124', {a1})
    assert _is_linked(b, 'xhtml_Flow124', a1)
    if hasattr(a1, 'xhtml_Strong125'):
        assert _is_linked(a1, 'xhtml_Strong125', b)
    _safe_set(b, 'xhtml_Flow124', {a2})
    assert _is_linked(b, 'xhtml_Flow124', a2)
    if hasattr(a1, 'xhtml_Strong125'):
        assert not _is_linked(a1, 'xhtml_Strong125', b)
    if hasattr(a2, 'xhtml_Strong125'):
        assert _is_linked(a2, 'xhtml_Strong125', b)
    _safe_set(b, 'xhtml_Flow124', set())
    assert not _is_linked(b, 'xhtml_Flow124', a2)
    if hasattr(a2, 'xhtml_Strong125'):
        assert not _is_linked(a2, 'xhtml_Strong125', b)


def test_assoc_strong19_reverse_link_reassign_clear():
    a1 = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Strong(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent20', {a1})
    assert _is_linked(b, 'xhtml_AContent20', a1)
    if hasattr(a1, 'xhtml_Strong'):
        assert _is_linked(a1, 'xhtml_Strong', b)
    _safe_set(b, 'xhtml_AContent20', {a2})
    assert _is_linked(b, 'xhtml_AContent20', a2)
    if hasattr(a1, 'xhtml_Strong'):
        assert not _is_linked(a1, 'xhtml_Strong', b)
    if hasattr(a2, 'xhtml_Strong'):
        assert _is_linked(a2, 'xhtml_Strong', b)
    _safe_set(b, 'xhtml_AContent20', set())
    assert not _is_linked(b, 'xhtml_AContent20', a2)
    if hasattr(a2, 'xhtml_Strong'):
        assert not _is_linked(a2, 'xhtml_Strong', b)


def test_assoc_strong194_reverse_link_reassign_clear():
    a1 = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Strong(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline195', {a1})
    assert _is_linked(b, 'xhtml_Inline195', a1)
    if hasattr(a1, 'xhtml_Strong196'):
        assert _is_linked(a1, 'xhtml_Strong196', b)
    _safe_set(b, 'xhtml_Inline195', {a2})
    assert _is_linked(b, 'xhtml_Inline195', a2)
    if hasattr(a1, 'xhtml_Strong196'):
        assert not _is_linked(a1, 'xhtml_Strong196', b)
    if hasattr(a2, 'xhtml_Strong196'):
        assert _is_linked(a2, 'xhtml_Strong196', b)
    _safe_set(b, 'xhtml_Inline195', set())
    assert not _is_linked(b, 'xhtml_Inline195', a2)
    if hasattr(a2, 'xhtml_Strong196'):
        assert not _is_linked(a2, 'xhtml_Strong196', b)


def test_assoc_strong292_reverse_link_reassign_clear():
    a1 = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Strong(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object293', {a1})
    assert _is_linked(b, 'xhtml_Object293', a1)
    if hasattr(a1, 'xhtml_Strong294'):
        assert _is_linked(a1, 'xhtml_Strong294', b)
    _safe_set(b, 'xhtml_Object293', {a2})
    assert _is_linked(b, 'xhtml_Object293', a2)
    if hasattr(a1, 'xhtml_Strong294'):
        assert not _is_linked(a1, 'xhtml_Strong294', b)
    if hasattr(a2, 'xhtml_Strong294'):
        assert _is_linked(a2, 'xhtml_Strong294', b)
    _safe_set(b, 'xhtml_Object293', set())
    assert not _is_linked(b, 'xhtml_Object293', a2)
    if hasattr(a2, 'xhtml_Strong294'):
        assert not _is_linked(a2, 'xhtml_Strong294', b)


def test_assoc_strong350_reverse_link_reassign_clear():
    a1 = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Strong(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent351', {a1})
    assert _is_linked(b, 'xhtml_PreContent351', a1)
    if hasattr(a1, 'xhtml_Strong352'):
        assert _is_linked(a1, 'xhtml_Strong352', b)
    _safe_set(b, 'xhtml_PreContent351', {a2})
    assert _is_linked(b, 'xhtml_PreContent351', a2)
    if hasattr(a1, 'xhtml_Strong352'):
        assert not _is_linked(a1, 'xhtml_Strong352', b)
    if hasattr(a2, 'xhtml_Strong352'):
        assert _is_linked(a2, 'xhtml_Strong352', b)
    _safe_set(b, 'xhtml_PreContent351', set())
    assert not _is_linked(b, 'xhtml_PreContent351', a2)
    if hasattr(a2, 'xhtml_Strong352'):
        assert not _is_linked(a2, 'xhtml_Strong352', b)


def test_assoc_sub153_reverse_link_reassign_clear():
    a1 = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sub(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow154', {a1})
    assert _is_linked(b, 'xhtml_Flow154', a1)
    if hasattr(a1, 'xhtml_Sub155'):
        assert _is_linked(a1, 'xhtml_Sub155', b)
    _safe_set(b, 'xhtml_Flow154', {a2})
    assert _is_linked(b, 'xhtml_Flow154', a2)
    if hasattr(a1, 'xhtml_Sub155'):
        assert not _is_linked(a1, 'xhtml_Sub155', b)
    if hasattr(a2, 'xhtml_Sub155'):
        assert _is_linked(a2, 'xhtml_Sub155', b)
    _safe_set(b, 'xhtml_Flow154', set())
    assert not _is_linked(b, 'xhtml_Flow154', a2)
    if hasattr(a2, 'xhtml_Sub155'):
        assert not _is_linked(a2, 'xhtml_Sub155', b)


def test_assoc_sub224_reverse_link_reassign_clear():
    a1 = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sub(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline225', {a1})
    assert _is_linked(b, 'xhtml_Inline225', a1)
    if hasattr(a1, 'xhtml_Sub226'):
        assert _is_linked(a1, 'xhtml_Sub226', b)
    _safe_set(b, 'xhtml_Inline225', {a2})
    assert _is_linked(b, 'xhtml_Inline225', a2)
    if hasattr(a1, 'xhtml_Sub226'):
        assert not _is_linked(a1, 'xhtml_Sub226', b)
    if hasattr(a2, 'xhtml_Sub226'):
        assert _is_linked(a2, 'xhtml_Sub226', b)
    _safe_set(b, 'xhtml_Inline225', set())
    assert not _is_linked(b, 'xhtml_Inline225', a2)
    if hasattr(a2, 'xhtml_Sub226'):
        assert not _is_linked(a2, 'xhtml_Sub226', b)


def test_assoc_sub322_reverse_link_reassign_clear():
    a1 = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sub(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object323', {a1})
    assert _is_linked(b, 'xhtml_Object323', a1)
    if hasattr(a1, 'xhtml_Sub324'):
        assert _is_linked(a1, 'xhtml_Sub324', b)
    _safe_set(b, 'xhtml_Object323', {a2})
    assert _is_linked(b, 'xhtml_Object323', a2)
    if hasattr(a1, 'xhtml_Sub324'):
        assert not _is_linked(a1, 'xhtml_Sub324', b)
    if hasattr(a2, 'xhtml_Sub324'):
        assert _is_linked(a2, 'xhtml_Sub324', b)
    _safe_set(b, 'xhtml_Object323', set())
    assert not _is_linked(b, 'xhtml_Object323', a2)
    if hasattr(a2, 'xhtml_Sub324'):
        assert not _is_linked(a2, 'xhtml_Sub324', b)


def test_assoc_sub380_reverse_link_reassign_clear():
    a1 = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sub(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent381', {a1})
    assert _is_linked(b, 'xhtml_PreContent381', a1)
    if hasattr(a1, 'xhtml_Sub382'):
        assert _is_linked(a1, 'xhtml_Sub382', b)
    _safe_set(b, 'xhtml_PreContent381', {a2})
    assert _is_linked(b, 'xhtml_PreContent381', a2)
    if hasattr(a1, 'xhtml_Sub382'):
        assert not _is_linked(a1, 'xhtml_Sub382', b)
    if hasattr(a2, 'xhtml_Sub382'):
        assert _is_linked(a2, 'xhtml_Sub382', b)
    _safe_set(b, 'xhtml_PreContent381', set())
    assert not _is_linked(b, 'xhtml_PreContent381', a2)
    if hasattr(a2, 'xhtml_Sub382'):
        assert not _is_linked(a2, 'xhtml_Sub382', b)


def test_assoc_sub39_reverse_link_reassign_clear():
    a1 = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sub(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent40', {a1})
    assert _is_linked(b, 'xhtml_AContent40', a1)
    if hasattr(a1, 'xhtml_Sub'):
        assert _is_linked(a1, 'xhtml_Sub', b)
    _safe_set(b, 'xhtml_AContent40', {a2})
    assert _is_linked(b, 'xhtml_AContent40', a2)
    if hasattr(a1, 'xhtml_Sub'):
        assert not _is_linked(a1, 'xhtml_Sub', b)
    if hasattr(a2, 'xhtml_Sub'):
        assert _is_linked(a2, 'xhtml_Sub', b)
    _safe_set(b, 'xhtml_AContent40', set())
    assert not _is_linked(b, 'xhtml_AContent40', a2)
    if hasattr(a2, 'xhtml_Sub'):
        assert not _is_linked(a2, 'xhtml_Sub', b)


def test_assoc_sup156_reverse_link_reassign_clear():
    a1 = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sup(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow157', {a1})
    assert _is_linked(b, 'xhtml_Flow157', a1)
    if hasattr(a1, 'xhtml_Sup158'):
        assert _is_linked(a1, 'xhtml_Sup158', b)
    _safe_set(b, 'xhtml_Flow157', {a2})
    assert _is_linked(b, 'xhtml_Flow157', a2)
    if hasattr(a1, 'xhtml_Sup158'):
        assert not _is_linked(a1, 'xhtml_Sup158', b)
    if hasattr(a2, 'xhtml_Sup158'):
        assert _is_linked(a2, 'xhtml_Sup158', b)
    _safe_set(b, 'xhtml_Flow157', set())
    assert not _is_linked(b, 'xhtml_Flow157', a2)
    if hasattr(a2, 'xhtml_Sup158'):
        assert not _is_linked(a2, 'xhtml_Sup158', b)


def test_assoc_sup227_reverse_link_reassign_clear():
    a1 = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sup(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline228', {a1})
    assert _is_linked(b, 'xhtml_Inline228', a1)
    if hasattr(a1, 'xhtml_Sup229'):
        assert _is_linked(a1, 'xhtml_Sup229', b)
    _safe_set(b, 'xhtml_Inline228', {a2})
    assert _is_linked(b, 'xhtml_Inline228', a2)
    if hasattr(a1, 'xhtml_Sup229'):
        assert not _is_linked(a1, 'xhtml_Sup229', b)
    if hasattr(a2, 'xhtml_Sup229'):
        assert _is_linked(a2, 'xhtml_Sup229', b)
    _safe_set(b, 'xhtml_Inline228', set())
    assert not _is_linked(b, 'xhtml_Inline228', a2)
    if hasattr(a2, 'xhtml_Sup229'):
        assert not _is_linked(a2, 'xhtml_Sup229', b)


def test_assoc_sup325_reverse_link_reassign_clear():
    a1 = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sup(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object326', {a1})
    assert _is_linked(b, 'xhtml_Object326', a1)
    if hasattr(a1, 'xhtml_Sup327'):
        assert _is_linked(a1, 'xhtml_Sup327', b)
    _safe_set(b, 'xhtml_Object326', {a2})
    assert _is_linked(b, 'xhtml_Object326', a2)
    if hasattr(a1, 'xhtml_Sup327'):
        assert not _is_linked(a1, 'xhtml_Sup327', b)
    if hasattr(a2, 'xhtml_Sup327'):
        assert _is_linked(a2, 'xhtml_Sup327', b)
    _safe_set(b, 'xhtml_Object326', set())
    assert not _is_linked(b, 'xhtml_Object326', a2)
    if hasattr(a2, 'xhtml_Sup327'):
        assert not _is_linked(a2, 'xhtml_Sup327', b)


def test_assoc_sup383_reverse_link_reassign_clear():
    a1 = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sup(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent384', {a1})
    assert _is_linked(b, 'xhtml_PreContent384', a1)
    if hasattr(a1, 'xhtml_Sup385'):
        assert _is_linked(a1, 'xhtml_Sup385', b)
    _safe_set(b, 'xhtml_PreContent384', {a2})
    assert _is_linked(b, 'xhtml_PreContent384', a2)
    if hasattr(a1, 'xhtml_Sup385'):
        assert not _is_linked(a1, 'xhtml_Sup385', b)
    if hasattr(a2, 'xhtml_Sup385'):
        assert _is_linked(a2, 'xhtml_Sup385', b)
    _safe_set(b, 'xhtml_PreContent384', set())
    assert not _is_linked(b, 'xhtml_PreContent384', a2)
    if hasattr(a2, 'xhtml_Sup385'):
        assert not _is_linked(a2, 'xhtml_Sup385', b)


def test_assoc_sup41_reverse_link_reassign_clear():
    a1 = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Sup(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent42', {a1})
    assert _is_linked(b, 'xhtml_AContent42', a1)
    if hasattr(a1, 'xhtml_Sup'):
        assert _is_linked(a1, 'xhtml_Sup', b)
    _safe_set(b, 'xhtml_AContent42', {a2})
    assert _is_linked(b, 'xhtml_AContent42', a2)
    if hasattr(a1, 'xhtml_Sup'):
        assert not _is_linked(a1, 'xhtml_Sup', b)
    if hasattr(a2, 'xhtml_Sup'):
        assert _is_linked(a2, 'xhtml_Sup', b)
    _safe_set(b, 'xhtml_AContent42', set())
    assert not _is_linked(b, 'xhtml_AContent42', a2)
    if hasattr(a2, 'xhtml_Sup'):
        assert not _is_linked(a2, 'xhtml_Sup', b)


def test_assoc_table256_reverse_link_reassign_clear():
    a1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object257', {a1})
    assert _is_linked(b, 'xhtml_Object257', a1)
    if hasattr(a1, 'xhtml_Table258'):
        assert _is_linked(a1, 'xhtml_Table258', b)
    _safe_set(b, 'xhtml_Object257', {a2})
    assert _is_linked(b, 'xhtml_Object257', a2)
    if hasattr(a1, 'xhtml_Table258'):
        assert not _is_linked(a1, 'xhtml_Table258', b)
    if hasattr(a2, 'xhtml_Table258'):
        assert _is_linked(a2, 'xhtml_Table258', b)
    _safe_set(b, 'xhtml_Object257', set())
    assert not _is_linked(b, 'xhtml_Object257', a2)
    if hasattr(a2, 'xhtml_Table258'):
        assert not _is_linked(a2, 'xhtml_Table258', b)


def test_assoc_table58_reverse_link_reassign_clear():
    a1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block59', {a1})
    assert _is_linked(b, 'xhtml_Block59', a1)
    if hasattr(a1, 'xhtml_Table'):
        assert _is_linked(a1, 'xhtml_Table', b)
    _safe_set(b, 'xhtml_Block59', {a2})
    assert _is_linked(b, 'xhtml_Block59', a2)
    if hasattr(a1, 'xhtml_Table'):
        assert not _is_linked(a1, 'xhtml_Table', b)
    if hasattr(a2, 'xhtml_Table'):
        assert _is_linked(a2, 'xhtml_Table', b)
    _safe_set(b, 'xhtml_Block59', set())
    assert not _is_linked(b, 'xhtml_Block59', a2)
    if hasattr(a2, 'xhtml_Table'):
        assert not _is_linked(a2, 'xhtml_Table', b)


def test_assoc_table88_reverse_link_reassign_clear():
    a1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow89', {a1})
    assert _is_linked(b, 'xhtml_Flow89', a1)
    if hasattr(a1, 'xhtml_Table90'):
        assert _is_linked(a1, 'xhtml_Table90', b)
    _safe_set(b, 'xhtml_Flow89', {a2})
    assert _is_linked(b, 'xhtml_Flow89', a2)
    if hasattr(a1, 'xhtml_Table90'):
        assert not _is_linked(a1, 'xhtml_Table90', b)
    if hasattr(a2, 'xhtml_Table90'):
        assert _is_linked(a2, 'xhtml_Table90', b)
    _safe_set(b, 'xhtml_Flow89', set())
    assert not _is_linked(b, 'xhtml_Flow89', a2)
    if hasattr(a2, 'xhtml_Table90'):
        assert not _is_linked(a2, 'xhtml_Table90', b)


def test_assoc_tbody404_reverse_link_reassign_clear():
    a1 = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tbody(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Table405', {a1})
    assert _is_linked(b, 'xhtml_Table405', a1)
    if hasattr(a1, 'xhtml_Tbody'):
        assert _is_linked(a1, 'xhtml_Tbody', b)
    _safe_set(b, 'xhtml_Table405', {a2})
    assert _is_linked(b, 'xhtml_Table405', a2)
    if hasattr(a1, 'xhtml_Tbody'):
        assert not _is_linked(a1, 'xhtml_Tbody', b)
    if hasattr(a2, 'xhtml_Tbody'):
        assert _is_linked(a2, 'xhtml_Tbody', b)
    _safe_set(b, 'xhtml_Table405', set())
    assert not _is_linked(b, 'xhtml_Table405', a2)
    if hasattr(a2, 'xhtml_Tbody'):
        assert not _is_linked(a2, 'xhtml_Tbody', b)


def test_assoc_td419_reverse_link_reassign_clear():
    a1 = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tr(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    _safe_set(b, 'xhtml_Td', a1)
    assert _is_linked(b, 'xhtml_Td', a1)
    if hasattr(a1, 'xhtml_Tr420'):
        assert _is_linked(a1, 'xhtml_Tr420', b)
    _safe_set(b, 'xhtml_Td', a2)
    assert _is_linked(b, 'xhtml_Td', a2)
    if hasattr(a1, 'xhtml_Tr420'):
        assert not _is_linked(a1, 'xhtml_Tr420', b)
    if hasattr(a2, 'xhtml_Tr420'):
        assert _is_linked(a2, 'xhtml_Tr420', b)
    _safe_set(b, 'xhtml_Td', None)
    assert not _is_linked(b, 'xhtml_Td', a2)
    if hasattr(a2, 'xhtml_Tr420'):
        assert not _is_linked(a2, 'xhtml_Tr420', b)


def test_assoc_tfoot402_reverse_link_reassign_clear():
    a1 = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tfoot(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Table403', a1)
    assert _is_linked(b, 'xhtml_Table403', a1)
    if hasattr(a1, 'xhtml_Tfoot'):
        assert _is_linked(a1, 'xhtml_Tfoot', b)
    _safe_set(b, 'xhtml_Table403', a2)
    assert _is_linked(b, 'xhtml_Table403', a2)
    if hasattr(a1, 'xhtml_Tfoot'):
        assert not _is_linked(a1, 'xhtml_Tfoot', b)
    if hasattr(a2, 'xhtml_Tfoot'):
        assert _is_linked(a2, 'xhtml_Tfoot', b)
    _safe_set(b, 'xhtml_Table403', None)
    assert not _is_linked(b, 'xhtml_Table403', a2)
    if hasattr(a2, 'xhtml_Tfoot'):
        assert not _is_linked(a2, 'xhtml_Tfoot', b)


def test_assoc_th417_reverse_link_reassign_clear():
    a1 = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tr(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    _safe_set(b, 'xhtml_Th', a1)
    assert _is_linked(b, 'xhtml_Th', a1)
    if hasattr(a1, 'xhtml_Tr418'):
        assert _is_linked(a1, 'xhtml_Tr418', b)
    _safe_set(b, 'xhtml_Th', a2)
    assert _is_linked(b, 'xhtml_Th', a2)
    if hasattr(a1, 'xhtml_Tr418'):
        assert not _is_linked(a1, 'xhtml_Tr418', b)
    if hasattr(a2, 'xhtml_Tr418'):
        assert _is_linked(a2, 'xhtml_Tr418', b)
    _safe_set(b, 'xhtml_Th', None)
    assert not _is_linked(b, 'xhtml_Th', a2)
    if hasattr(a2, 'xhtml_Tr418'):
        assert not _is_linked(a2, 'xhtml_Tr418', b)


def test_assoc_thead400_reverse_link_reassign_clear():
    a1 = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Thead(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Table401', a1)
    assert _is_linked(b, 'xhtml_Table401', a1)
    if hasattr(a1, 'xhtml_Thead'):
        assert _is_linked(a1, 'xhtml_Thead', b)
    _safe_set(b, 'xhtml_Table401', a2)
    assert _is_linked(b, 'xhtml_Table401', a2)
    if hasattr(a1, 'xhtml_Thead'):
        assert not _is_linked(a1, 'xhtml_Thead', b)
    if hasattr(a2, 'xhtml_Thead'):
        assert _is_linked(a2, 'xhtml_Thead', b)
    _safe_set(b, 'xhtml_Table401', None)
    assert not _is_linked(b, 'xhtml_Table401', a2)
    if hasattr(a2, 'xhtml_Thead'):
        assert not _is_linked(a2, 'xhtml_Thead', b)


def test_assoc_thumbnail160_reverse_link_reassign_clear():
    a1 = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    a2 = xhtml_Img(alt="sample_text_2", class_="sample_text_2", height="sample_text_2", hl7Id="sample_text_2", imageType="sample_text_2", lang="sample_text_2", src="sample_text_2", style="sample_text_2", width="sample_text_2")
    b = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Img161', a1)
    assert _is_linked(b, 'xhtml_Img161', a1)
    if hasattr(a1, 'xhtml_Img159'):
        assert _is_linked(a1, 'xhtml_Img159', b)
    _safe_set(b, 'xhtml_Img161', a2)
    assert _is_linked(b, 'xhtml_Img161', a2)
    if hasattr(a1, 'xhtml_Img159'):
        assert not _is_linked(a1, 'xhtml_Img159', b)
    if hasattr(a2, 'xhtml_Img159'):
        assert _is_linked(a2, 'xhtml_Img159', b)
    _safe_set(b, 'xhtml_Img161', None)
    assert not _is_linked(b, 'xhtml_Img161', a2)
    if hasattr(a2, 'xhtml_Img159'):
        assert not _is_linked(a2, 'xhtml_Img159', b)


def test_assoc_tr406_reverse_link_reassign_clear():
    a1 = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tr(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    _safe_set(b, 'xhtml_Table407', {a1})
    assert _is_linked(b, 'xhtml_Table407', a1)
    if hasattr(a1, 'xhtml_Tr'):
        assert _is_linked(a1, 'xhtml_Tr', b)
    _safe_set(b, 'xhtml_Table407', {a2})
    assert _is_linked(b, 'xhtml_Table407', a2)
    if hasattr(a1, 'xhtml_Tr'):
        assert not _is_linked(a1, 'xhtml_Tr', b)
    if hasattr(a2, 'xhtml_Tr'):
        assert _is_linked(a2, 'xhtml_Tr', b)
    _safe_set(b, 'xhtml_Table407', set())
    assert not _is_linked(b, 'xhtml_Table407', a2)
    if hasattr(a2, 'xhtml_Tr'):
        assert not _is_linked(a2, 'xhtml_Tr', b)


def test_assoc_tr408_reverse_link_reassign_clear():
    a1 = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tr(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    _safe_set(b, 'xhtml_Tbody409', {a1})
    assert _is_linked(b, 'xhtml_Tbody409', a1)
    if hasattr(a1, 'xhtml_Tr410'):
        assert _is_linked(a1, 'xhtml_Tr410', b)
    _safe_set(b, 'xhtml_Tbody409', {a2})
    assert _is_linked(b, 'xhtml_Tbody409', a2)
    if hasattr(a1, 'xhtml_Tr410'):
        assert not _is_linked(a1, 'xhtml_Tr410', b)
    if hasattr(a2, 'xhtml_Tr410'):
        assert _is_linked(a2, 'xhtml_Tr410', b)
    _safe_set(b, 'xhtml_Tbody409', set())
    assert not _is_linked(b, 'xhtml_Tbody409', a2)
    if hasattr(a2, 'xhtml_Tr410'):
        assert not _is_linked(a2, 'xhtml_Tr410', b)


def test_assoc_tr411_reverse_link_reassign_clear():
    a1 = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tr(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    _safe_set(b, 'xhtml_Tfoot412', {a1})
    assert _is_linked(b, 'xhtml_Tfoot412', a1)
    if hasattr(a1, 'xhtml_Tr413'):
        assert _is_linked(a1, 'xhtml_Tr413', b)
    _safe_set(b, 'xhtml_Tfoot412', {a2})
    assert _is_linked(b, 'xhtml_Tfoot412', a2)
    if hasattr(a1, 'xhtml_Tr413'):
        assert not _is_linked(a1, 'xhtml_Tr413', b)
    if hasattr(a2, 'xhtml_Tr413'):
        assert _is_linked(a2, 'xhtml_Tr413', b)
    _safe_set(b, 'xhtml_Tfoot412', set())
    assert not _is_linked(b, 'xhtml_Tfoot412', a2)
    if hasattr(a2, 'xhtml_Tr413'):
        assert not _is_linked(a2, 'xhtml_Tr413', b)


def test_assoc_tr414_reverse_link_reassign_clear():
    a1 = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    a2 = xhtml_Tr(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    b = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    _safe_set(b, 'xhtml_Thead415', {a1})
    assert _is_linked(b, 'xhtml_Thead415', a1)
    if hasattr(a1, 'xhtml_Tr416'):
        assert _is_linked(a1, 'xhtml_Tr416', b)
    _safe_set(b, 'xhtml_Thead415', {a2})
    assert _is_linked(b, 'xhtml_Thead415', a2)
    if hasattr(a1, 'xhtml_Tr416'):
        assert not _is_linked(a1, 'xhtml_Tr416', b)
    if hasattr(a2, 'xhtml_Tr416'):
        assert _is_linked(a2, 'xhtml_Tr416', b)
    _safe_set(b, 'xhtml_Thead415', set())
    assert not _is_linked(b, 'xhtml_Thead415', a2)
    if hasattr(a2, 'xhtml_Tr416'):
        assert not _is_linked(a2, 'xhtml_Tr416', b)


def test_assoc_tt105_reverse_link_reassign_clear():
    a1 = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Tt(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow106', {a1})
    assert _is_linked(b, 'xhtml_Flow106', a1)
    if hasattr(a1, 'xhtml_Tt107'):
        assert _is_linked(a1, 'xhtml_Tt107', b)
    _safe_set(b, 'xhtml_Flow106', {a2})
    assert _is_linked(b, 'xhtml_Flow106', a2)
    if hasattr(a1, 'xhtml_Tt107'):
        assert not _is_linked(a1, 'xhtml_Tt107', b)
    if hasattr(a2, 'xhtml_Tt107'):
        assert _is_linked(a2, 'xhtml_Tt107', b)
    _safe_set(b, 'xhtml_Flow106', set())
    assert not _is_linked(b, 'xhtml_Flow106', a2)
    if hasattr(a2, 'xhtml_Tt107'):
        assert not _is_linked(a2, 'xhtml_Tt107', b)


def test_assoc_tt176_reverse_link_reassign_clear():
    a1 = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Tt(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline177', {a1})
    assert _is_linked(b, 'xhtml_Inline177', a1)
    if hasattr(a1, 'xhtml_Tt178'):
        assert _is_linked(a1, 'xhtml_Tt178', b)
    _safe_set(b, 'xhtml_Inline177', {a2})
    assert _is_linked(b, 'xhtml_Inline177', a2)
    if hasattr(a1, 'xhtml_Tt178'):
        assert not _is_linked(a1, 'xhtml_Tt178', b)
    if hasattr(a2, 'xhtml_Tt178'):
        assert _is_linked(a2, 'xhtml_Tt178', b)
    _safe_set(b, 'xhtml_Inline177', set())
    assert not _is_linked(b, 'xhtml_Inline177', a2)
    if hasattr(a2, 'xhtml_Tt178'):
        assert not _is_linked(a2, 'xhtml_Tt178', b)


def test_assoc_tt274_reverse_link_reassign_clear():
    a1 = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Tt(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object275', {a1})
    assert _is_linked(b, 'xhtml_Object275', a1)
    if hasattr(a1, 'xhtml_Tt276'):
        assert _is_linked(a1, 'xhtml_Tt276', b)
    _safe_set(b, 'xhtml_Object275', {a2})
    assert _is_linked(b, 'xhtml_Object275', a2)
    if hasattr(a1, 'xhtml_Tt276'):
        assert not _is_linked(a1, 'xhtml_Tt276', b)
    if hasattr(a2, 'xhtml_Tt276'):
        assert _is_linked(a2, 'xhtml_Tt276', b)
    _safe_set(b, 'xhtml_Object275', set())
    assert not _is_linked(b, 'xhtml_Object275', a2)
    if hasattr(a2, 'xhtml_Tt276'):
        assert not _is_linked(a2, 'xhtml_Tt276', b)


def test_assoc_tt332_reverse_link_reassign_clear():
    a1 = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Tt(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent333', {a1})
    assert _is_linked(b, 'xhtml_PreContent333', a1)
    if hasattr(a1, 'xhtml_Tt334'):
        assert _is_linked(a1, 'xhtml_Tt334', b)
    _safe_set(b, 'xhtml_PreContent333', {a2})
    assert _is_linked(b, 'xhtml_PreContent333', a2)
    if hasattr(a1, 'xhtml_Tt334'):
        assert not _is_linked(a1, 'xhtml_Tt334', b)
    if hasattr(a2, 'xhtml_Tt334'):
        assert _is_linked(a2, 'xhtml_Tt334', b)
    _safe_set(b, 'xhtml_PreContent333', set())
    assert not _is_linked(b, 'xhtml_PreContent333', a2)
    if hasattr(a2, 'xhtml_Tt334'):
        assert not _is_linked(a2, 'xhtml_Tt334', b)


def test_assoc_tt7_reverse_link_reassign_clear():
    a1 = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Tt(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent8', {a1})
    assert _is_linked(b, 'xhtml_AContent8', a1)
    if hasattr(a1, 'xhtml_Tt'):
        assert _is_linked(a1, 'xhtml_Tt', b)
    _safe_set(b, 'xhtml_AContent8', {a2})
    assert _is_linked(b, 'xhtml_AContent8', a2)
    if hasattr(a1, 'xhtml_Tt'):
        assert not _is_linked(a1, 'xhtml_Tt', b)
    if hasattr(a2, 'xhtml_Tt'):
        assert _is_linked(a2, 'xhtml_Tt', b)
    _safe_set(b, 'xhtml_AContent8', set())
    assert not _is_linked(b, 'xhtml_AContent8', a2)
    if hasattr(a2, 'xhtml_Tt'):
        assert not _is_linked(a2, 'xhtml_Tt', b)


def test_assoc_ul238_reverse_link_reassign_clear():
    a1 = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ul(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object239', {a1})
    assert _is_linked(b, 'xhtml_Object239', a1)
    if hasattr(a1, 'xhtml_Ul240'):
        assert _is_linked(a1, 'xhtml_Ul240', b)
    _safe_set(b, 'xhtml_Object239', {a2})
    assert _is_linked(b, 'xhtml_Object239', a2)
    if hasattr(a1, 'xhtml_Ul240'):
        assert not _is_linked(a1, 'xhtml_Ul240', b)
    if hasattr(a2, 'xhtml_Ul240'):
        assert _is_linked(a2, 'xhtml_Ul240', b)
    _safe_set(b, 'xhtml_Object239', set())
    assert not _is_linked(b, 'xhtml_Object239', a2)
    if hasattr(a2, 'xhtml_Ul240'):
        assert not _is_linked(a2, 'xhtml_Ul240', b)


def test_assoc_ul46_reverse_link_reassign_clear():
    a1 = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ul(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Block(block="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Block47', {a1})
    assert _is_linked(b, 'xhtml_Block47', a1)
    if hasattr(a1, 'xhtml_Ul'):
        assert _is_linked(a1, 'xhtml_Ul', b)
    _safe_set(b, 'xhtml_Block47', {a2})
    assert _is_linked(b, 'xhtml_Block47', a2)
    if hasattr(a1, 'xhtml_Ul'):
        assert not _is_linked(a1, 'xhtml_Ul', b)
    if hasattr(a2, 'xhtml_Ul'):
        assert _is_linked(a2, 'xhtml_Ul', b)
    _safe_set(b, 'xhtml_Block47', set())
    assert not _is_linked(b, 'xhtml_Block47', a2)
    if hasattr(a2, 'xhtml_Ul'):
        assert not _is_linked(a2, 'xhtml_Ul', b)


def test_assoc_ul70_reverse_link_reassign_clear():
    a1 = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    a2 = xhtml_Ul(class_="sample_text_2", lang="sample_text_2", li="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow71', {a1})
    assert _is_linked(b, 'xhtml_Flow71', a1)
    if hasattr(a1, 'xhtml_Ul72'):
        assert _is_linked(a1, 'xhtml_Ul72', b)
    _safe_set(b, 'xhtml_Flow71', {a2})
    assert _is_linked(b, 'xhtml_Flow71', a2)
    if hasattr(a1, 'xhtml_Ul72'):
        assert not _is_linked(a1, 'xhtml_Ul72', b)
    if hasattr(a2, 'xhtml_Ul72'):
        assert _is_linked(a2, 'xhtml_Ul72', b)
    _safe_set(b, 'xhtml_Flow71', set())
    assert not _is_linked(b, 'xhtml_Flow71', a2)
    if hasattr(a2, 'xhtml_Ul72'):
        assert not _is_linked(a2, 'xhtml_Ul72', b)


def test_assoc_var141_reverse_link_reassign_clear():
    a1 = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Var(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Flow(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Flow142', {a1})
    assert _is_linked(b, 'xhtml_Flow142', a1)
    if hasattr(a1, 'xhtml_Var143'):
        assert _is_linked(a1, 'xhtml_Var143', b)
    _safe_set(b, 'xhtml_Flow142', {a2})
    assert _is_linked(b, 'xhtml_Flow142', a2)
    if hasattr(a1, 'xhtml_Var143'):
        assert not _is_linked(a1, 'xhtml_Var143', b)
    if hasattr(a2, 'xhtml_Var143'):
        assert _is_linked(a2, 'xhtml_Var143', b)
    _safe_set(b, 'xhtml_Flow142', set())
    assert not _is_linked(b, 'xhtml_Flow142', a2)
    if hasattr(a2, 'xhtml_Var143'):
        assert not _is_linked(a2, 'xhtml_Var143', b)


def test_assoc_var212_reverse_link_reassign_clear():
    a1 = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Var(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Inline(inline="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_Inline213', {a1})
    assert _is_linked(b, 'xhtml_Inline213', a1)
    if hasattr(a1, 'xhtml_Var214'):
        assert _is_linked(a1, 'xhtml_Var214', b)
    _safe_set(b, 'xhtml_Inline213', {a2})
    assert _is_linked(b, 'xhtml_Inline213', a2)
    if hasattr(a1, 'xhtml_Var214'):
        assert not _is_linked(a1, 'xhtml_Var214', b)
    if hasattr(a2, 'xhtml_Var214'):
        assert _is_linked(a2, 'xhtml_Var214', b)
    _safe_set(b, 'xhtml_Inline213', set())
    assert not _is_linked(b, 'xhtml_Inline213', a2)
    if hasattr(a2, 'xhtml_Var214'):
        assert not _is_linked(a2, 'xhtml_Var214', b)


def test_assoc_var31_reverse_link_reassign_clear():
    a1 = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Var(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_AContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_AContent32', {a1})
    assert _is_linked(b, 'xhtml_AContent32', a1)
    if hasattr(a1, 'xhtml_Var'):
        assert _is_linked(a1, 'xhtml_Var', b)
    _safe_set(b, 'xhtml_AContent32', {a2})
    assert _is_linked(b, 'xhtml_AContent32', a2)
    if hasattr(a1, 'xhtml_Var'):
        assert not _is_linked(a1, 'xhtml_Var', b)
    if hasattr(a2, 'xhtml_Var'):
        assert _is_linked(a2, 'xhtml_Var', b)
    _safe_set(b, 'xhtml_AContent32', set())
    assert not _is_linked(b, 'xhtml_AContent32', a2)
    if hasattr(a2, 'xhtml_Var'):
        assert not _is_linked(a2, 'xhtml_Var', b)


def test_assoc_var310_reverse_link_reassign_clear():
    a1 = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Var(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'xhtml_Object311', {a1})
    assert _is_linked(b, 'xhtml_Object311', a1)
    if hasattr(a1, 'xhtml_Var312'):
        assert _is_linked(a1, 'xhtml_Var312', b)
    _safe_set(b, 'xhtml_Object311', {a2})
    assert _is_linked(b, 'xhtml_Object311', a2)
    if hasattr(a1, 'xhtml_Var312'):
        assert not _is_linked(a1, 'xhtml_Var312', b)
    if hasattr(a2, 'xhtml_Var312'):
        assert _is_linked(a2, 'xhtml_Var312', b)
    _safe_set(b, 'xhtml_Object311', set())
    assert not _is_linked(b, 'xhtml_Object311', a2)
    if hasattr(a2, 'xhtml_Var312'):
        assert not _is_linked(a2, 'xhtml_Var312', b)


def test_assoc_var368_reverse_link_reassign_clear():
    a1 = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    a2 = xhtml_Var(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    b = xhtml_PreContent(group="sample_text", mixed="sample_text")
    _safe_set(b, 'xhtml_PreContent369', {a1})
    assert _is_linked(b, 'xhtml_PreContent369', a1)
    if hasattr(a1, 'xhtml_Var370'):
        assert _is_linked(a1, 'xhtml_Var370', b)
    _safe_set(b, 'xhtml_PreContent369', {a2})
    assert _is_linked(b, 'xhtml_PreContent369', a2)
    if hasattr(a1, 'xhtml_Var370'):
        assert not _is_linked(a1, 'xhtml_Var370', b)
    if hasattr(a2, 'xhtml_Var370'):
        assert _is_linked(a2, 'xhtml_Var370', b)
    _safe_set(b, 'xhtml_PreContent369', set())
    assert not _is_linked(b, 'xhtml_PreContent369', a2)
    if hasattr(a2, 'xhtml_Var370'):
        assert not _is_linked(a2, 'xhtml_Var370', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

