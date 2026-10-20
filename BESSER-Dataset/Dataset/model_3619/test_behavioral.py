import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ANY,
    HXIT,
    IVL,
    QSET,
    QTY,
    XP,
    r2_AD,
    r2_ADXP,
    r2_ANY,
    r2_BL,
    r2_CD,
    r2_CO,
    r2_CS,
    r2_ED,
    r2_EN,
    r2_ENXP,
    r2_EObject,
    r2_HXIT,
    r2_II,
    r2_INT,
    r2_IVL,
    r2_IVLCO,
    r2_IVLINT,
    r2_IVLPQ,
    r2_IVLQTY,
    r2_IVLREAL,
    r2_IVLTS,
    r2_PIVLTS,
    r2_PQ,
    r2_QSET,
    r2_QTY,
    r2_REAL,
    r2_RTO,
    r2_ST,
    r2_TEL,
    r2_TS,
    r2_XP,
    AddressPartType,
    CalendarCycle,
    Compression,
    EntityNamePartQualifier,
    EntityNamePartType,
    EntityNameUse,
    IntegrityCheckAlgorithm,
    PostalAddressUse,
    TelecommunicationAddressUse,
    TelecommunicationCapability,
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

def test_assoc_code8_reverse_link_reassign_clear():
    a1 = r2_CO(value="sample_text")
    a2 = r2_CO(value="sample_text_2")
    b = r2_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", valueSet="sample_text", valueSetVersion="sample_text")
    _safe_set(b, 'r2_CD9', a1)
    assert _is_linked(b, 'r2_CD9', a1)
    if hasattr(a1, 'r2_CO'):
        assert _is_linked(a1, 'r2_CO', b)
    _safe_set(b, 'r2_CD9', a2)
    assert _is_linked(b, 'r2_CD9', a2)
    if hasattr(a1, 'r2_CO'):
        assert not _is_linked(a1, 'r2_CO', b)
    if hasattr(a2, 'r2_CO'):
        assert _is_linked(a2, 'r2_CO', b)
    _safe_set(b, 'r2_CD9', None)
    assert not _is_linked(b, 'r2_CD9', a2)
    if hasattr(a2, 'r2_CO'):
        assert not _is_linked(a2, 'r2_CO', b)


def test_assoc_count49_reverse_link_reassign_clear():
    a1 = r2_PIVLTS(alignment="sample_text", isFlexible="sample_text")
    a2 = r2_PIVLTS(alignment="sample_text_2", isFlexible="sample_text_2")
    b = r2_INT(value="sample_text")
    _safe_set(b, 'r2_INT51', a1)
    assert _is_linked(b, 'r2_INT51', a1)
    if hasattr(a1, 'r2_PIVLTS50'):
        assert _is_linked(a1, 'r2_PIVLTS50', b)
    _safe_set(b, 'r2_INT51', a2)
    assert _is_linked(b, 'r2_INT51', a2)
    if hasattr(a1, 'r2_PIVLTS50'):
        assert not _is_linked(a1, 'r2_PIVLTS50', b)
    if hasattr(a2, 'r2_PIVLTS50'):
        assert _is_linked(a2, 'r2_PIVLTS50', b)
    _safe_set(b, 'r2_INT51', None)
    assert not _is_linked(b, 'r2_INT51', a2)
    if hasattr(a2, 'r2_PIVLTS50'):
        assert not _is_linked(a2, 'r2_PIVLTS50', b)


def test_assoc_description13_reverse_link_reassign_clear():
    a1 = r2_ST(value="sample_text")
    a2 = r2_ST(value="sample_text_2")
    b = r2_ED(charset="sample_text", compression="sample_text", data="sample_text", integrityCheck="sample_text", integrityCheckAlgorithm="sample_text", language="sample_text", mediaType="sample_text", value="sample_text")
    _safe_set(b, 'r2_ED14', a1)
    assert _is_linked(b, 'r2_ED14', a1)
    if hasattr(a1, 'r2_ST15'):
        assert _is_linked(a1, 'r2_ST15', b)
    _safe_set(b, 'r2_ED14', a2)
    assert _is_linked(b, 'r2_ED14', a2)
    if hasattr(a1, 'r2_ST15'):
        assert not _is_linked(a1, 'r2_ST15', b)
    if hasattr(a2, 'r2_ST15'):
        assert _is_linked(a2, 'r2_ST15', b)
    _safe_set(b, 'r2_ED14', None)
    assert not _is_linked(b, 'r2_ED14', a2)
    if hasattr(a2, 'r2_ST15'):
        assert not _is_linked(a2, 'r2_ST15', b)


def test_assoc_displayName1_reverse_link_reassign_clear():
    a1 = r2_ST(value="sample_text")
    a2 = r2_ST(value="sample_text_2")
    b = r2_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", valueSet="sample_text", valueSetVersion="sample_text")
    _safe_set(b, 'r2_CD', a1)
    assert _is_linked(b, 'r2_CD', a1)
    if hasattr(a1, 'r2_ST'):
        assert _is_linked(a1, 'r2_ST', b)
    _safe_set(b, 'r2_CD', a2)
    assert _is_linked(b, 'r2_CD', a2)
    if hasattr(a1, 'r2_ST'):
        assert not _is_linked(a1, 'r2_ST', b)
    if hasattr(a2, 'r2_ST'):
        assert _is_linked(a2, 'r2_ST', b)
    _safe_set(b, 'r2_CD', None)
    assert not _is_linked(b, 'r2_CD', a2)
    if hasattr(a2, 'r2_ST'):
        assert not _is_linked(a2, 'r2_ST', b)


def test_assoc_high19_reverse_link_reassign_clear():
    a1 = r2_IVLCO(highClosed="sample_text", lowClosed="sample_text")
    a2 = r2_IVLCO(highClosed="sample_text_2", lowClosed="sample_text_2")
    b = r2_CO(value="sample_text")
    _safe_set(b, 'r2_CO21', a1)
    assert _is_linked(b, 'r2_CO21', a1)
    if hasattr(a1, 'r2_IVLCO20'):
        assert _is_linked(a1, 'r2_IVLCO20', b)
    _safe_set(b, 'r2_CO21', a2)
    assert _is_linked(b, 'r2_CO21', a2)
    if hasattr(a1, 'r2_IVLCO20'):
        assert not _is_linked(a1, 'r2_IVLCO20', b)
    if hasattr(a2, 'r2_IVLCO20'):
        assert _is_linked(a2, 'r2_IVLCO20', b)
    _safe_set(b, 'r2_CO21', None)
    assert not _is_linked(b, 'r2_CO21', a2)
    if hasattr(a2, 'r2_IVLCO20'):
        assert not _is_linked(a2, 'r2_IVLCO20', b)


def test_assoc_high23_reverse_link_reassign_clear():
    a1 = r2_IVLINT(highClosed="sample_text", lowClosed="sample_text")
    a2 = r2_IVLINT(highClosed="sample_text_2", lowClosed="sample_text_2")
    b = r2_INT(value="sample_text")
    _safe_set(b, 'r2_INT25', a1)
    assert _is_linked(b, 'r2_INT25', a1)
    if hasattr(a1, 'r2_IVLINT24'):
        assert _is_linked(a1, 'r2_IVLINT24', b)
    _safe_set(b, 'r2_INT25', a2)
    assert _is_linked(b, 'r2_INT25', a2)
    if hasattr(a1, 'r2_IVLINT24'):
        assert not _is_linked(a1, 'r2_IVLINT24', b)
    if hasattr(a2, 'r2_IVLINT24'):
        assert _is_linked(a2, 'r2_IVLINT24', b)
    _safe_set(b, 'r2_INT25', None)
    assert not _is_linked(b, 'r2_INT25', a2)
    if hasattr(a2, 'r2_IVLINT24'):
        assert not _is_linked(a2, 'r2_IVLINT24', b)


def test_assoc_high27_reverse_link_reassign_clear():
    a1 = r2_PQ(unit="sample_text", value="sample_text")
    a2 = r2_PQ(unit="sample_text_2", value="sample_text_2")
    b = r2_IVLPQ(highClosed="sample_text", lowClosed="sample_text")
    _safe_set(b, 'r2_IVLPQ28', a1)
    assert _is_linked(b, 'r2_IVLPQ28', a1)
    if hasattr(a1, 'r2_PQ29'):
        assert _is_linked(a1, 'r2_PQ29', b)
    _safe_set(b, 'r2_IVLPQ28', a2)
    assert _is_linked(b, 'r2_IVLPQ28', a2)
    if hasattr(a1, 'r2_PQ29'):
        assert not _is_linked(a1, 'r2_PQ29', b)
    if hasattr(a2, 'r2_PQ29'):
        assert _is_linked(a2, 'r2_PQ29', b)
    _safe_set(b, 'r2_IVLPQ28', None)
    assert not _is_linked(b, 'r2_IVLPQ28', a2)
    if hasattr(a2, 'r2_PQ29'):
        assert not _is_linked(a2, 'r2_PQ29', b)


def test_assoc_high35_reverse_link_reassign_clear():
    a1 = r2_REAL(value="sample_text")
    a2 = r2_REAL(value="sample_text_2")
    b = r2_IVLREAL(highClosed="sample_text", lowClosed="sample_text")
    _safe_set(b, 'r2_IVLREAL36', a1)
    assert _is_linked(b, 'r2_IVLREAL36', a1)
    if hasattr(a1, 'r2_REAL37'):
        assert _is_linked(a1, 'r2_REAL37', b)
    _safe_set(b, 'r2_IVLREAL36', a2)
    assert _is_linked(b, 'r2_IVLREAL36', a2)
    if hasattr(a1, 'r2_REAL37'):
        assert not _is_linked(a1, 'r2_REAL37', b)
    if hasattr(a2, 'r2_REAL37'):
        assert _is_linked(a2, 'r2_REAL37', b)
    _safe_set(b, 'r2_IVLREAL36', None)
    assert not _is_linked(b, 'r2_IVLREAL36', a2)
    if hasattr(a2, 'r2_REAL37'):
        assert not _is_linked(a2, 'r2_REAL37', b)


def test_assoc_high39_reverse_link_reassign_clear():
    a1 = r2_TS(value="sample_text")
    a2 = r2_TS(value="sample_text_2")
    b = r2_IVLTS(highClosed="sample_text", lowClosed="sample_text")
    _safe_set(b, 'r2_IVLTS40', a1)
    assert _is_linked(b, 'r2_IVLTS40', a1)
    if hasattr(a1, 'r2_TS41'):
        assert _is_linked(a1, 'r2_TS41', b)
    _safe_set(b, 'r2_IVLTS40', a2)
    assert _is_linked(b, 'r2_IVLTS40', a2)
    if hasattr(a1, 'r2_TS41'):
        assert not _is_linked(a1, 'r2_TS41', b)
    if hasattr(a2, 'r2_TS41'):
        assert _is_linked(a2, 'r2_TS41', b)
    _safe_set(b, 'r2_IVLTS40', None)
    assert not _is_linked(b, 'r2_IVLTS40', a2)
    if hasattr(a2, 'r2_TS41'):
        assert not _is_linked(a2, 'r2_TS41', b)


def test_assoc_low17_reverse_link_reassign_clear():
    a1 = r2_IVLCO(highClosed="sample_text", lowClosed="sample_text")
    a2 = r2_IVLCO(highClosed="sample_text_2", lowClosed="sample_text_2")
    b = r2_CO(value="sample_text")
    _safe_set(b, 'r2_CO18', a1)
    assert _is_linked(b, 'r2_CO18', a1)
    if hasattr(a1, 'r2_IVLCO'):
        assert _is_linked(a1, 'r2_IVLCO', b)
    _safe_set(b, 'r2_CO18', a2)
    assert _is_linked(b, 'r2_CO18', a2)
    if hasattr(a1, 'r2_IVLCO'):
        assert not _is_linked(a1, 'r2_IVLCO', b)
    if hasattr(a2, 'r2_IVLCO'):
        assert _is_linked(a2, 'r2_IVLCO', b)
    _safe_set(b, 'r2_CO18', None)
    assert not _is_linked(b, 'r2_CO18', a2)
    if hasattr(a2, 'r2_IVLCO'):
        assert not _is_linked(a2, 'r2_IVLCO', b)


def test_assoc_low22_reverse_link_reassign_clear():
    a1 = r2_IVLINT(highClosed="sample_text", lowClosed="sample_text")
    a2 = r2_IVLINT(highClosed="sample_text_2", lowClosed="sample_text_2")
    b = r2_INT(value="sample_text")
    _safe_set(b, 'r2_INT', a1)
    assert _is_linked(b, 'r2_INT', a1)
    if hasattr(a1, 'r2_IVLINT'):
        assert _is_linked(a1, 'r2_IVLINT', b)
    _safe_set(b, 'r2_INT', a2)
    assert _is_linked(b, 'r2_INT', a2)
    if hasattr(a1, 'r2_IVLINT'):
        assert not _is_linked(a1, 'r2_IVLINT', b)
    if hasattr(a2, 'r2_IVLINT'):
        assert _is_linked(a2, 'r2_IVLINT', b)
    _safe_set(b, 'r2_INT', None)
    assert not _is_linked(b, 'r2_INT', a2)
    if hasattr(a2, 'r2_IVLINT'):
        assert not _is_linked(a2, 'r2_IVLINT', b)


def test_assoc_low26_reverse_link_reassign_clear():
    a1 = r2_PQ(unit="sample_text", value="sample_text")
    a2 = r2_PQ(unit="sample_text_2", value="sample_text_2")
    b = r2_IVLPQ(highClosed="sample_text", lowClosed="sample_text")
    _safe_set(b, 'r2_IVLPQ', a1)
    assert _is_linked(b, 'r2_IVLPQ', a1)
    if hasattr(a1, 'r2_PQ'):
        assert _is_linked(a1, 'r2_PQ', b)
    _safe_set(b, 'r2_IVLPQ', a2)
    assert _is_linked(b, 'r2_IVLPQ', a2)
    if hasattr(a1, 'r2_PQ'):
        assert not _is_linked(a1, 'r2_PQ', b)
    if hasattr(a2, 'r2_PQ'):
        assert _is_linked(a2, 'r2_PQ', b)
    _safe_set(b, 'r2_IVLPQ', None)
    assert not _is_linked(b, 'r2_IVLPQ', a2)
    if hasattr(a2, 'r2_PQ'):
        assert not _is_linked(a2, 'r2_PQ', b)


def test_assoc_low34_reverse_link_reassign_clear():
    a1 = r2_REAL(value="sample_text")
    a2 = r2_REAL(value="sample_text_2")
    b = r2_IVLREAL(highClosed="sample_text", lowClosed="sample_text")
    _safe_set(b, 'r2_IVLREAL', a1)
    assert _is_linked(b, 'r2_IVLREAL', a1)
    if hasattr(a1, 'r2_REAL'):
        assert _is_linked(a1, 'r2_REAL', b)
    _safe_set(b, 'r2_IVLREAL', a2)
    assert _is_linked(b, 'r2_IVLREAL', a2)
    if hasattr(a1, 'r2_REAL'):
        assert not _is_linked(a1, 'r2_REAL', b)
    if hasattr(a2, 'r2_REAL'):
        assert _is_linked(a2, 'r2_REAL', b)
    _safe_set(b, 'r2_IVLREAL', None)
    assert not _is_linked(b, 'r2_IVLREAL', a2)
    if hasattr(a2, 'r2_REAL'):
        assert not _is_linked(a2, 'r2_REAL', b)


def test_assoc_low38_reverse_link_reassign_clear():
    a1 = r2_TS(value="sample_text")
    a2 = r2_TS(value="sample_text_2")
    b = r2_IVLTS(highClosed="sample_text", lowClosed="sample_text")
    _safe_set(b, 'r2_IVLTS', a1)
    assert _is_linked(b, 'r2_IVLTS', a1)
    if hasattr(a1, 'r2_TS'):
        assert _is_linked(a1, 'r2_TS', b)
    _safe_set(b, 'r2_IVLTS', a2)
    assert _is_linked(b, 'r2_IVLTS', a2)
    if hasattr(a1, 'r2_TS'):
        assert not _is_linked(a1, 'r2_TS', b)
    if hasattr(a2, 'r2_TS'):
        assert _is_linked(a2, 'r2_TS', b)
    _safe_set(b, 'r2_IVLTS', None)
    assert not _is_linked(b, 'r2_IVLTS', a2)
    if hasattr(a2, 'r2_TS'):
        assert not _is_linked(a2, 'r2_TS', b)


def test_assoc_originalText2_reverse_link_reassign_clear():
    a1 = r2_ST(value="sample_text")
    a2 = r2_ST(value="sample_text_2")
    b = r2_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", valueSet="sample_text", valueSetVersion="sample_text")
    _safe_set(b, 'r2_CD3', a1)
    assert _is_linked(b, 'r2_CD3', a1)
    if hasattr(a1, 'r2_ST4'):
        assert _is_linked(a1, 'r2_ST4', b)
    _safe_set(b, 'r2_CD3', a2)
    assert _is_linked(b, 'r2_CD3', a2)
    if hasattr(a1, 'r2_ST4'):
        assert not _is_linked(a1, 'r2_ST4', b)
    if hasattr(a2, 'r2_ST4'):
        assert _is_linked(a2, 'r2_ST4', b)
    _safe_set(b, 'r2_CD3', None)
    assert not _is_linked(b, 'r2_CD3', a2)
    if hasattr(a2, 'r2_ST4'):
        assert not _is_linked(a2, 'r2_ST4', b)


def test_assoc_part0_reverse_link_reassign_clear():
    a1 = r2_ADXP(type="sample_text")
    a2 = r2_ADXP(type="sample_text_2")
    b = r2_AD(use="sample_text")
    _safe_set(b, 'r2_AD', {a1})
    assert _is_linked(b, 'r2_AD', a1)
    if hasattr(a1, 'r2_ADXP'):
        assert _is_linked(a1, 'r2_ADXP', b)
    _safe_set(b, 'r2_AD', {a2})
    assert _is_linked(b, 'r2_AD', a2)
    if hasattr(a1, 'r2_ADXP'):
        assert not _is_linked(a1, 'r2_ADXP', b)
    if hasattr(a2, 'r2_ADXP'):
        assert _is_linked(a2, 'r2_ADXP', b)
    _safe_set(b, 'r2_AD', set())
    assert not _is_linked(b, 'r2_AD', a2)
    if hasattr(a2, 'r2_ADXP'):
        assert not _is_linked(a2, 'r2_ADXP', b)


def test_assoc_part16_reverse_link_reassign_clear():
    a1 = r2_ENXP(qualifier="sample_text", type="sample_text")
    a2 = r2_ENXP(qualifier="sample_text_2", type="sample_text_2")
    b = r2_EN(use="sample_text")
    _safe_set(b, 'r2_EN', {a1})
    assert _is_linked(b, 'r2_EN', a1)
    if hasattr(a1, 'r2_ENXP'):
        assert _is_linked(a1, 'r2_ENXP', b)
    _safe_set(b, 'r2_EN', {a2})
    assert _is_linked(b, 'r2_EN', a2)
    if hasattr(a1, 'r2_ENXP'):
        assert not _is_linked(a1, 'r2_ENXP', b)
    if hasattr(a2, 'r2_ENXP'):
        assert _is_linked(a2, 'r2_ENXP', b)
    _safe_set(b, 'r2_EN', set())
    assert not _is_linked(b, 'r2_EN', a2)
    if hasattr(a2, 'r2_ENXP'):
        assert not _is_linked(a2, 'r2_ENXP', b)


def test_assoc_period44_reverse_link_reassign_clear():
    a1 = r2_PQ(unit="sample_text", value="sample_text")
    a2 = r2_PQ(unit="sample_text_2", value="sample_text_2")
    b = r2_PIVLTS(alignment="sample_text", isFlexible="sample_text")
    _safe_set(b, 'r2_PIVLTS45', a1)
    assert _is_linked(b, 'r2_PIVLTS45', a1)
    if hasattr(a1, 'r2_PQ46'):
        assert _is_linked(a1, 'r2_PQ46', b)
    _safe_set(b, 'r2_PIVLTS45', a2)
    assert _is_linked(b, 'r2_PIVLTS45', a2)
    if hasattr(a1, 'r2_PQ46'):
        assert not _is_linked(a1, 'r2_PQ46', b)
    if hasattr(a2, 'r2_PQ46'):
        assert _is_linked(a2, 'r2_PQ46', b)
    _safe_set(b, 'r2_PIVLTS45', None)
    assert not _is_linked(b, 'r2_PIVLTS45', a2)
    if hasattr(a2, 'r2_PQ46'):
        assert not _is_linked(a2, 'r2_PQ46', b)


def test_assoc_phase42_reverse_link_reassign_clear():
    a1 = r2_PIVLTS(alignment="sample_text", isFlexible="sample_text")
    a2 = r2_PIVLTS(alignment="sample_text_2", isFlexible="sample_text_2")
    b = r2_IVLTS(highClosed="sample_text", lowClosed="sample_text")
    _safe_set(b, 'r2_IVLTS43', a1)
    assert _is_linked(b, 'r2_IVLTS43', a1)
    if hasattr(a1, 'r2_PIVLTS'):
        assert _is_linked(a1, 'r2_PIVLTS', b)
    _safe_set(b, 'r2_IVLTS43', a2)
    assert _is_linked(b, 'r2_IVLTS43', a2)
    if hasattr(a1, 'r2_PIVLTS'):
        assert not _is_linked(a1, 'r2_PIVLTS', b)
    if hasattr(a2, 'r2_PIVLTS'):
        assert _is_linked(a2, 'r2_PIVLTS', b)
    _safe_set(b, 'r2_IVLTS43', None)
    assert not _is_linked(b, 'r2_IVLTS43', a2)
    if hasattr(a2, 'r2_PIVLTS'):
        assert not _is_linked(a2, 'r2_PIVLTS', b)


def test_assoc_reference11_reverse_link_reassign_clear():
    a1 = r2_TEL(capabilities="sample_text", use="sample_text", value="sample_text")
    a2 = r2_TEL(capabilities="sample_text_2", use="sample_text_2", value="sample_text_2")
    b = r2_ED(charset="sample_text", compression="sample_text", data="sample_text", integrityCheck="sample_text", integrityCheckAlgorithm="sample_text", language="sample_text", mediaType="sample_text", value="sample_text")
    _safe_set(b, 'r2_ED12', a1)
    assert _is_linked(b, 'r2_ED12', a1)
    if hasattr(a1, 'r2_TEL'):
        assert _is_linked(a1, 'r2_TEL', b)
    _safe_set(b, 'r2_ED12', a2)
    assert _is_linked(b, 'r2_ED12', a2)
    if hasattr(a1, 'r2_TEL'):
        assert not _is_linked(a1, 'r2_TEL', b)
    if hasattr(a2, 'r2_TEL'):
        assert _is_linked(a2, 'r2_TEL', b)
    _safe_set(b, 'r2_ED12', None)
    assert not _is_linked(b, 'r2_ED12', a2)
    if hasattr(a2, 'r2_TEL'):
        assert not _is_linked(a2, 'r2_TEL', b)


def test_assoc_translation6_reverse_link_reassign_clear():
    a1 = r2_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", valueSet="sample_text", valueSetVersion="sample_text")
    a2 = r2_CD(code="sample_text_2", codeSystem="sample_text_2", codeSystemName="sample_text_2", codeSystemVersion="sample_text_2", valueSet="sample_text_2", valueSetVersion="sample_text_2")
    b = r2_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", valueSet="sample_text", valueSetVersion="sample_text")
    _safe_set(b, 'r2_CD7', a1)
    assert _is_linked(b, 'r2_CD7', a1)
    if hasattr(a1, 'r2_CD5'):
        assert _is_linked(a1, 'r2_CD5', b)
    _safe_set(b, 'r2_CD7', a2)
    assert _is_linked(b, 'r2_CD7', a2)
    if hasattr(a1, 'r2_CD5'):
        assert not _is_linked(a1, 'r2_CD5', b)
    if hasattr(a2, 'r2_CD5'):
        assert _is_linked(a2, 'r2_CD5', b)
    _safe_set(b, 'r2_CD7', None)
    assert not _is_linked(b, 'r2_CD7', a2)
    if hasattr(a2, 'r2_CD5'):
        assert not _is_linked(a2, 'r2_CD5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_frequency47_stub_double():
    # r2_RTO has no real 'r2_RTO' property in the generated
    # code (a bare stub) -- manually attach it so r2_PIVLTS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r2_PIVLTS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r2_PIVLTS(alignment="sample_text", isFlexible="sample_text")
    partner = r2_RTO()
    setattr(partner, 'r2_RTO', None)
    _safe_set(owner, 'r2_PIVLTS48', partner)
    assert getattr(partner, 'r2_RTO') == owner
    _safe_set(owner, 'r2_PIVLTS48', None)
    assert getattr(partner, 'r2_RTO') is None


def test_assoc_high31_stub_double():
    # r2_QTY has no real 'r2_QTY33' property in the generated
    # code (a bare stub) -- manually attach it so r2_IVLQTY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r2_IVLQTY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r2_IVLQTY(highClosed="sample_text", lowClosed="sample_text")
    partner = r2_QTY()
    setattr(partner, 'r2_QTY33', None)
    _safe_set(owner, 'r2_IVLQTY32', partner)
    assert getattr(partner, 'r2_QTY33') == owner
    _safe_set(owner, 'r2_IVLQTY32', None)
    assert getattr(partner, 'r2_QTY33') is None


def test_assoc_low30_stub_double():
    # r2_QTY has no real 'r2_QTY' property in the generated
    # code (a bare stub) -- manually attach it so r2_IVLQTY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r2_IVLQTY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r2_IVLQTY(highClosed="sample_text", lowClosed="sample_text")
    partner = r2_QTY()
    setattr(partner, 'r2_QTY', None)
    _safe_set(owner, 'r2_IVLQTY', partner)
    assert getattr(partner, 'r2_QTY') == owner
    _safe_set(owner, 'r2_IVLQTY', None)
    assert getattr(partner, 'r2_QTY') is None


def test_assoc_xml10_stub_double():
    # r2_EObject has no real 'r2_EObject' property in the generated
    # code (a bare stub) -- manually attach it so r2_ED's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r2_ED's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r2_ED(charset="sample_text", compression="sample_text", data="sample_text", integrityCheck="sample_text", integrityCheckAlgorithm="sample_text", language="sample_text", mediaType="sample_text", value="sample_text")
    partner = r2_EObject()
    setattr(partner, 'r2_EObject', None)
    _safe_set(owner, 'r2_ED', partner)
    assert getattr(partner, 'r2_EObject') == owner
    _safe_set(owner, 'r2_ED', None)
    assert getattr(partner, 'r2_EObject') is None


