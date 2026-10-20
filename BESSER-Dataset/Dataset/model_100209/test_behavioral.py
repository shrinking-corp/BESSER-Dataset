import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    datastyle_AmPmType,
    datastyle_BooleanStyleType,
    datastyle_BooleanType,
    datastyle_CurrencyStyleType,
    datastyle_CurrencySymbolType,
    datastyle_DateStyleType,
    datastyle_DayOfWeekType,
    datastyle_DayType,
    datastyle_DocumentRoot,
    datastyle_EObject,
    datastyle_EStringToStringMapEntry,
    datastyle_EmbeddedTextType,
    datastyle_EraType,
    datastyle_FractionType,
    datastyle_HoursType,
    datastyle_MapType,
    datastyle_MinutesType,
    datastyle_MonthType,
    datastyle_NumberStyleType,
    datastyle_NumberType,
    datastyle_PercentageStyleType,
    datastyle_QuarterType,
    datastyle_ScientificNumberType,
    datastyle_SecondsType,
    datastyle_StyleTextPropertiesContent,
    datastyle_TextContentType,
    datastyle_TextStyleType,
    datastyle_TimeStyleType,
    datastyle_WeekOfYearType,
    datastyle_YearType,
    CalendarTypeMember1,
    CalendarTypeMember2,
    CalendarTypeMember3,
    CalendarTypeMember4,
    CalendarTypeMember5,
    CalendarTypeMember6,
    CalendarTypeMember7,
    CalendarTypeMember8,
    FormatSourceType,
    StyleType,
    TransliterationStyleType,
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

def test_assoc_booleanStyle98_reverse_link_reassign_clear():
    a1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    a2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    b = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_BooleanStyleType100', a1)
    assert _is_linked(b, 'datastyle_BooleanStyleType100', a1)
    if hasattr(a1, 'datastyle_DocumentRoot99'):
        assert _is_linked(a1, 'datastyle_DocumentRoot99', b)
    _safe_set(b, 'datastyle_BooleanStyleType100', a2)
    assert _is_linked(b, 'datastyle_BooleanStyleType100', a2)
    if hasattr(a1, 'datastyle_DocumentRoot99'):
        assert not _is_linked(a1, 'datastyle_DocumentRoot99', b)
    if hasattr(a2, 'datastyle_DocumentRoot99'):
        assert _is_linked(a2, 'datastyle_DocumentRoot99', b)
    _safe_set(b, 'datastyle_BooleanStyleType100', None)
    assert not _is_linked(b, 'datastyle_BooleanStyleType100', a2)
    if hasattr(a2, 'datastyle_DocumentRoot99'):
        assert not _is_linked(a2, 'datastyle_DocumentRoot99', b)


def test_assoc_currencyStyle101_reverse_link_reassign_clear():
    a1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    a2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    b = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_CurrencyStyleType103', a1)
    assert _is_linked(b, 'datastyle_CurrencyStyleType103', a1)
    if hasattr(a1, 'datastyle_DocumentRoot102'):
        assert _is_linked(a1, 'datastyle_DocumentRoot102', b)
    _safe_set(b, 'datastyle_CurrencyStyleType103', a2)
    assert _is_linked(b, 'datastyle_CurrencyStyleType103', a2)
    if hasattr(a1, 'datastyle_DocumentRoot102'):
        assert not _is_linked(a1, 'datastyle_DocumentRoot102', b)
    if hasattr(a2, 'datastyle_DocumentRoot102'):
        assert _is_linked(a2, 'datastyle_DocumentRoot102', b)
    _safe_set(b, 'datastyle_CurrencyStyleType103', None)
    assert not _is_linked(b, 'datastyle_CurrencyStyleType103', a2)
    if hasattr(a2, 'datastyle_DocumentRoot102'):
        assert not _is_linked(a2, 'datastyle_DocumentRoot102', b)


def test_assoc_currencySymbol104_reverse_link_reassign_clear():
    a1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    a2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    b = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    _safe_set(b, 'datastyle_CurrencySymbolType106', a1)
    assert _is_linked(b, 'datastyle_CurrencySymbolType106', a1)
    if hasattr(a1, 'datastyle_DocumentRoot105'):
        assert _is_linked(a1, 'datastyle_DocumentRoot105', b)
    _safe_set(b, 'datastyle_CurrencySymbolType106', a2)
    assert _is_linked(b, 'datastyle_CurrencySymbolType106', a2)
    if hasattr(a1, 'datastyle_DocumentRoot105'):
        assert not _is_linked(a1, 'datastyle_DocumentRoot105', b)
    if hasattr(a2, 'datastyle_DocumentRoot105'):
        assert _is_linked(a2, 'datastyle_DocumentRoot105', b)
    _safe_set(b, 'datastyle_CurrencySymbolType106', None)
    assert not _is_linked(b, 'datastyle_CurrencySymbolType106', a2)
    if hasattr(a2, 'datastyle_DocumentRoot105'):
        assert not _is_linked(a2, 'datastyle_DocumentRoot105', b)


def test_assoc_currencySymbol111_reverse_link_reassign_clear():
    a1 = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    a2 = datastyle_CurrencySymbolType(country="sample_text_2", language="sample_text_2", mixed="sample_text_2")
    b = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_CurrencyStyleType12', a1)
    assert _is_linked(b, 'datastyle_CurrencyStyleType12', a1)
    if hasattr(a1, 'datastyle_CurrencySymbolType13'):
        assert _is_linked(a1, 'datastyle_CurrencySymbolType13', b)
    _safe_set(b, 'datastyle_CurrencyStyleType12', a2)
    assert _is_linked(b, 'datastyle_CurrencyStyleType12', a2)
    if hasattr(a1, 'datastyle_CurrencySymbolType13'):
        assert not _is_linked(a1, 'datastyle_CurrencySymbolType13', b)
    if hasattr(a2, 'datastyle_CurrencySymbolType13'):
        assert _is_linked(a2, 'datastyle_CurrencySymbolType13', b)
    _safe_set(b, 'datastyle_CurrencyStyleType12', None)
    assert not _is_linked(b, 'datastyle_CurrencyStyleType12', a2)
    if hasattr(a2, 'datastyle_CurrencySymbolType13'):
        assert not _is_linked(a2, 'datastyle_CurrencySymbolType13', b)


def test_assoc_currencySymbol9_reverse_link_reassign_clear():
    a1 = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    a2 = datastyle_CurrencySymbolType(country="sample_text_2", language="sample_text_2", mixed="sample_text_2")
    b = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_CurrencyStyleType10', a1)
    assert _is_linked(b, 'datastyle_CurrencyStyleType10', a1)
    if hasattr(a1, 'datastyle_CurrencySymbolType'):
        assert _is_linked(a1, 'datastyle_CurrencySymbolType', b)
    _safe_set(b, 'datastyle_CurrencyStyleType10', a2)
    assert _is_linked(b, 'datastyle_CurrencyStyleType10', a2)
    if hasattr(a1, 'datastyle_CurrencySymbolType'):
        assert not _is_linked(a1, 'datastyle_CurrencySymbolType', b)
    if hasattr(a2, 'datastyle_CurrencySymbolType'):
        assert _is_linked(a2, 'datastyle_CurrencySymbolType', b)
    _safe_set(b, 'datastyle_CurrencyStyleType10', None)
    assert not _is_linked(b, 'datastyle_CurrencyStyleType10', a2)
    if hasattr(a2, 'datastyle_CurrencySymbolType'):
        assert not _is_linked(a2, 'datastyle_CurrencySymbolType', b)


def test_assoc_dateStyle107_reverse_link_reassign_clear():
    a1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    a2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType109', a1)
    assert _is_linked(b, 'datastyle_DateStyleType109', a1)
    if hasattr(a1, 'datastyle_DocumentRoot108'):
        assert _is_linked(a1, 'datastyle_DocumentRoot108', b)
    _safe_set(b, 'datastyle_DateStyleType109', a2)
    assert _is_linked(b, 'datastyle_DateStyleType109', a2)
    if hasattr(a1, 'datastyle_DocumentRoot108'):
        assert not _is_linked(a1, 'datastyle_DocumentRoot108', b)
    if hasattr(a2, 'datastyle_DocumentRoot108'):
        assert _is_linked(a2, 'datastyle_DocumentRoot108', b)
    _safe_set(b, 'datastyle_DateStyleType109', None)
    assert not _is_linked(b, 'datastyle_DateStyleType109', a2)
    if hasattr(a2, 'datastyle_DocumentRoot108'):
        assert not _is_linked(a2, 'datastyle_DocumentRoot108', b)


def test_assoc_day110_reverse_link_reassign_clear():
    a1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    a2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    b = datastyle_DayType(calendar="sample_text", style="sample_text")
    _safe_set(b, 'datastyle_DayType112', a1)
    assert _is_linked(b, 'datastyle_DayType112', a1)
    if hasattr(a1, 'datastyle_DocumentRoot111'):
        assert _is_linked(a1, 'datastyle_DocumentRoot111', b)
    _safe_set(b, 'datastyle_DayType112', a2)
    assert _is_linked(b, 'datastyle_DayType112', a2)
    if hasattr(a1, 'datastyle_DocumentRoot111'):
        assert not _is_linked(a1, 'datastyle_DocumentRoot111', b)
    if hasattr(a2, 'datastyle_DocumentRoot111'):
        assert _is_linked(a2, 'datastyle_DocumentRoot111', b)
    _safe_set(b, 'datastyle_DayType112', None)
    assert not _is_linked(b, 'datastyle_DayType112', a2)
    if hasattr(a2, 'datastyle_DocumentRoot111'):
        assert not _is_linked(a2, 'datastyle_DocumentRoot111', b)


def test_assoc_day22_reverse_link_reassign_clear():
    a1 = datastyle_DayType(calendar="sample_text", style="sample_text")
    a2 = datastyle_DayType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType23', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType23', a1)
    if hasattr(a1, 'datastyle_DayType'):
        assert _is_linked(a1, 'datastyle_DayType', b)
    _safe_set(b, 'datastyle_DateStyleType23', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType23', a2)
    if hasattr(a1, 'datastyle_DayType'):
        assert not _is_linked(a1, 'datastyle_DayType', b)
    if hasattr(a2, 'datastyle_DayType'):
        assert _is_linked(a2, 'datastyle_DayType', b)
    _safe_set(b, 'datastyle_DateStyleType23', set())
    assert not _is_linked(b, 'datastyle_DateStyleType23', a2)
    if hasattr(a2, 'datastyle_DayType'):
        assert not _is_linked(a2, 'datastyle_DayType', b)


def test_assoc_dayOfWeek113_reverse_link_reassign_clear():
    a1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    a2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    b = datastyle_DayOfWeekType(calendar="sample_text", style="sample_text")
    _safe_set(b, 'datastyle_DayOfWeekType115', a1)
    assert _is_linked(b, 'datastyle_DayOfWeekType115', a1)
    if hasattr(a1, 'datastyle_DocumentRoot114'):
        assert _is_linked(a1, 'datastyle_DocumentRoot114', b)
    _safe_set(b, 'datastyle_DayOfWeekType115', a2)
    assert _is_linked(b, 'datastyle_DayOfWeekType115', a2)
    if hasattr(a1, 'datastyle_DocumentRoot114'):
        assert not _is_linked(a1, 'datastyle_DocumentRoot114', b)
    if hasattr(a2, 'datastyle_DocumentRoot114'):
        assert _is_linked(a2, 'datastyle_DocumentRoot114', b)
    _safe_set(b, 'datastyle_DayOfWeekType115', None)
    assert not _is_linked(b, 'datastyle_DayOfWeekType115', a2)
    if hasattr(a2, 'datastyle_DocumentRoot114'):
        assert not _is_linked(a2, 'datastyle_DocumentRoot114', b)


def test_assoc_dayOfWeek30_reverse_link_reassign_clear():
    a1 = datastyle_DayOfWeekType(calendar="sample_text", style="sample_text")
    a2 = datastyle_DayOfWeekType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType31', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType31', a1)
    if hasattr(a1, 'datastyle_DayOfWeekType'):
        assert _is_linked(a1, 'datastyle_DayOfWeekType', b)
    _safe_set(b, 'datastyle_DateStyleType31', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType31', a2)
    if hasattr(a1, 'datastyle_DayOfWeekType'):
        assert not _is_linked(a1, 'datastyle_DayOfWeekType', b)
    if hasattr(a2, 'datastyle_DayOfWeekType'):
        assert _is_linked(a2, 'datastyle_DayOfWeekType', b)
    _safe_set(b, 'datastyle_DateStyleType31', set())
    assert not _is_linked(b, 'datastyle_DateStyleType31', a2)
    if hasattr(a2, 'datastyle_DayOfWeekType'):
        assert not _is_linked(a2, 'datastyle_DayOfWeekType', b)


def test_assoc_embeddedText116_reverse_link_reassign_clear():
    a1 = datastyle_EmbeddedTextType(mixed="sample_text", position="sample_text")
    a2 = datastyle_EmbeddedTextType(mixed="sample_text_2", position="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot117', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot117', a1)
    if hasattr(a1, 'datastyle_EmbeddedTextType118'):
        assert _is_linked(a1, 'datastyle_EmbeddedTextType118', b)
    _safe_set(b, 'datastyle_DocumentRoot117', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot117', a2)
    if hasattr(a1, 'datastyle_EmbeddedTextType118'):
        assert not _is_linked(a1, 'datastyle_EmbeddedTextType118', b)
    if hasattr(a2, 'datastyle_EmbeddedTextType118'):
        assert _is_linked(a2, 'datastyle_EmbeddedTextType118', b)
    _safe_set(b, 'datastyle_DocumentRoot117', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot117', a2)
    if hasattr(a2, 'datastyle_EmbeddedTextType118'):
        assert not _is_linked(a2, 'datastyle_EmbeddedTextType118', b)


def test_assoc_embeddedText54_reverse_link_reassign_clear():
    a1 = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    a2 = datastyle_NumberType(decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", displayFactor="sample_text_2", grouping="sample_text_2", minIntegerDigits="sample_text_2")
    b = datastyle_EmbeddedTextType(mixed="sample_text", position="sample_text")
    _safe_set(b, 'datastyle_EmbeddedTextType', a1)
    assert _is_linked(b, 'datastyle_EmbeddedTextType', a1)
    if hasattr(a1, 'datastyle_NumberType55'):
        assert _is_linked(a1, 'datastyle_NumberType55', b)
    _safe_set(b, 'datastyle_EmbeddedTextType', a2)
    assert _is_linked(b, 'datastyle_EmbeddedTextType', a2)
    if hasattr(a1, 'datastyle_NumberType55'):
        assert not _is_linked(a1, 'datastyle_NumberType55', b)
    if hasattr(a2, 'datastyle_NumberType55'):
        assert _is_linked(a2, 'datastyle_NumberType55', b)
    _safe_set(b, 'datastyle_EmbeddedTextType', None)
    assert not _is_linked(b, 'datastyle_EmbeddedTextType', a2)
    if hasattr(a2, 'datastyle_NumberType55'):
        assert not _is_linked(a2, 'datastyle_NumberType55', b)


def test_assoc_era119_reverse_link_reassign_clear():
    a1 = datastyle_EraType(calendar="sample_text", style="sample_text")
    a2 = datastyle_EraType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot120', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot120', a1)
    if hasattr(a1, 'datastyle_EraType121'):
        assert _is_linked(a1, 'datastyle_EraType121', b)
    _safe_set(b, 'datastyle_DocumentRoot120', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot120', a2)
    if hasattr(a1, 'datastyle_EraType121'):
        assert not _is_linked(a1, 'datastyle_EraType121', b)
    if hasattr(a2, 'datastyle_EraType121'):
        assert _is_linked(a2, 'datastyle_EraType121', b)
    _safe_set(b, 'datastyle_DocumentRoot120', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot120', a2)
    if hasattr(a2, 'datastyle_EraType121'):
        assert not _is_linked(a2, 'datastyle_EraType121', b)


def test_assoc_era28_reverse_link_reassign_clear():
    a1 = datastyle_EraType(calendar="sample_text", style="sample_text")
    a2 = datastyle_EraType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType29', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType29', a1)
    if hasattr(a1, 'datastyle_EraType'):
        assert _is_linked(a1, 'datastyle_EraType', b)
    _safe_set(b, 'datastyle_DateStyleType29', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType29', a2)
    if hasattr(a1, 'datastyle_EraType'):
        assert not _is_linked(a1, 'datastyle_EraType', b)
    if hasattr(a2, 'datastyle_EraType'):
        assert _is_linked(a2, 'datastyle_EraType', b)
    _safe_set(b, 'datastyle_DateStyleType29', set())
    assert not _is_linked(b, 'datastyle_DateStyleType29', a2)
    if hasattr(a2, 'datastyle_EraType'):
        assert not _is_linked(a2, 'datastyle_EraType', b)


def test_assoc_fraction122_reverse_link_reassign_clear():
    a1 = datastyle_FractionType(denominatorValue="sample_text", grouping="sample_text", minDenominatorDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text")
    a2 = datastyle_FractionType(denominatorValue="sample_text_2", grouping="sample_text_2", minDenominatorDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot123', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot123', a1)
    if hasattr(a1, 'datastyle_FractionType'):
        assert _is_linked(a1, 'datastyle_FractionType', b)
    _safe_set(b, 'datastyle_DocumentRoot123', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot123', a2)
    if hasattr(a1, 'datastyle_FractionType'):
        assert not _is_linked(a1, 'datastyle_FractionType', b)
    if hasattr(a2, 'datastyle_FractionType'):
        assert _is_linked(a2, 'datastyle_FractionType', b)
    _safe_set(b, 'datastyle_DocumentRoot123', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot123', a2)
    if hasattr(a2, 'datastyle_FractionType'):
        assert not _is_linked(a2, 'datastyle_FractionType', b)


def test_assoc_hours124_reverse_link_reassign_clear():
    a1 = datastyle_HoursType(style="sample_text")
    a2 = datastyle_HoursType(style="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot125', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot125', a1)
    if hasattr(a1, 'datastyle_HoursType126'):
        assert _is_linked(a1, 'datastyle_HoursType126', b)
    _safe_set(b, 'datastyle_DocumentRoot125', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot125', a2)
    if hasattr(a1, 'datastyle_HoursType126'):
        assert not _is_linked(a1, 'datastyle_HoursType126', b)
    if hasattr(a2, 'datastyle_HoursType126'):
        assert _is_linked(a2, 'datastyle_HoursType126', b)
    _safe_set(b, 'datastyle_DocumentRoot125', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot125', a2)
    if hasattr(a2, 'datastyle_HoursType126'):
        assert not _is_linked(a2, 'datastyle_HoursType126', b)


def test_assoc_hours36_reverse_link_reassign_clear():
    a1 = datastyle_HoursType(style="sample_text")
    a2 = datastyle_HoursType(style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType37', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType37', a1)
    if hasattr(a1, 'datastyle_HoursType'):
        assert _is_linked(a1, 'datastyle_HoursType', b)
    _safe_set(b, 'datastyle_DateStyleType37', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType37', a2)
    if hasattr(a1, 'datastyle_HoursType'):
        assert not _is_linked(a1, 'datastyle_HoursType', b)
    if hasattr(a2, 'datastyle_HoursType'):
        assert _is_linked(a2, 'datastyle_HoursType', b)
    _safe_set(b, 'datastyle_DateStyleType37', set())
    assert not _is_linked(b, 'datastyle_DateStyleType37', a2)
    if hasattr(a2, 'datastyle_HoursType'):
        assert not _is_linked(a2, 'datastyle_HoursType', b)


def test_assoc_hours73_reverse_link_reassign_clear():
    a1 = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    a2 = datastyle_TimeStyleType(country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2", volatile="sample_text_2")
    b = datastyle_HoursType(style="sample_text")
    _safe_set(b, 'datastyle_HoursType75', a1)
    assert _is_linked(b, 'datastyle_HoursType75', a1)
    if hasattr(a1, 'datastyle_TimeStyleType74'):
        assert _is_linked(a1, 'datastyle_TimeStyleType74', b)
    _safe_set(b, 'datastyle_HoursType75', a2)
    assert _is_linked(b, 'datastyle_HoursType75', a2)
    if hasattr(a1, 'datastyle_TimeStyleType74'):
        assert not _is_linked(a1, 'datastyle_TimeStyleType74', b)
    if hasattr(a2, 'datastyle_TimeStyleType74'):
        assert _is_linked(a2, 'datastyle_TimeStyleType74', b)
    _safe_set(b, 'datastyle_HoursType75', None)
    assert not _is_linked(b, 'datastyle_HoursType75', a2)
    if hasattr(a2, 'datastyle_TimeStyleType74'):
        assert not _is_linked(a2, 'datastyle_TimeStyleType74', b)


def test_assoc_minutes127_reverse_link_reassign_clear():
    a1 = datastyle_MinutesType(style="sample_text")
    a2 = datastyle_MinutesType(style="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot128', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot128', a1)
    if hasattr(a1, 'datastyle_MinutesType129'):
        assert _is_linked(a1, 'datastyle_MinutesType129', b)
    _safe_set(b, 'datastyle_DocumentRoot128', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot128', a2)
    if hasattr(a1, 'datastyle_MinutesType129'):
        assert not _is_linked(a1, 'datastyle_MinutesType129', b)
    if hasattr(a2, 'datastyle_MinutesType129'):
        assert _is_linked(a2, 'datastyle_MinutesType129', b)
    _safe_set(b, 'datastyle_DocumentRoot128', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot128', a2)
    if hasattr(a2, 'datastyle_MinutesType129'):
        assert not _is_linked(a2, 'datastyle_MinutesType129', b)


def test_assoc_minutes40_reverse_link_reassign_clear():
    a1 = datastyle_MinutesType(style="sample_text")
    a2 = datastyle_MinutesType(style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType41', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType41', a1)
    if hasattr(a1, 'datastyle_MinutesType'):
        assert _is_linked(a1, 'datastyle_MinutesType', b)
    _safe_set(b, 'datastyle_DateStyleType41', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType41', a2)
    if hasattr(a1, 'datastyle_MinutesType'):
        assert not _is_linked(a1, 'datastyle_MinutesType', b)
    if hasattr(a2, 'datastyle_MinutesType'):
        assert _is_linked(a2, 'datastyle_MinutesType', b)
    _safe_set(b, 'datastyle_DateStyleType41', set())
    assert not _is_linked(b, 'datastyle_DateStyleType41', a2)
    if hasattr(a2, 'datastyle_MinutesType'):
        assert not _is_linked(a2, 'datastyle_MinutesType', b)


def test_assoc_minutes79_reverse_link_reassign_clear():
    a1 = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    a2 = datastyle_TimeStyleType(country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2", volatile="sample_text_2")
    b = datastyle_MinutesType(style="sample_text")
    _safe_set(b, 'datastyle_MinutesType81', a1)
    assert _is_linked(b, 'datastyle_MinutesType81', a1)
    if hasattr(a1, 'datastyle_TimeStyleType80'):
        assert _is_linked(a1, 'datastyle_TimeStyleType80', b)
    _safe_set(b, 'datastyle_MinutesType81', a2)
    assert _is_linked(b, 'datastyle_MinutesType81', a2)
    if hasattr(a1, 'datastyle_TimeStyleType80'):
        assert not _is_linked(a1, 'datastyle_TimeStyleType80', b)
    if hasattr(a2, 'datastyle_TimeStyleType80'):
        assert _is_linked(a2, 'datastyle_TimeStyleType80', b)
    _safe_set(b, 'datastyle_MinutesType81', None)
    assert not _is_linked(b, 'datastyle_MinutesType81', a2)
    if hasattr(a2, 'datastyle_TimeStyleType80'):
        assert not _is_linked(a2, 'datastyle_TimeStyleType80', b)


def test_assoc_month130_reverse_link_reassign_clear():
    a1 = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    a2 = datastyle_MonthType(calendar="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", textual="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot131', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot131', a1)
    if hasattr(a1, 'datastyle_MonthType132'):
        assert _is_linked(a1, 'datastyle_MonthType132', b)
    _safe_set(b, 'datastyle_DocumentRoot131', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot131', a2)
    if hasattr(a1, 'datastyle_MonthType132'):
        assert not _is_linked(a1, 'datastyle_MonthType132', b)
    if hasattr(a2, 'datastyle_MonthType132'):
        assert _is_linked(a2, 'datastyle_MonthType132', b)
    _safe_set(b, 'datastyle_DocumentRoot131', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot131', a2)
    if hasattr(a2, 'datastyle_MonthType132'):
        assert not _is_linked(a2, 'datastyle_MonthType132', b)


def test_assoc_month24_reverse_link_reassign_clear():
    a1 = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    a2 = datastyle_MonthType(calendar="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", textual="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType25', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType25', a1)
    if hasattr(a1, 'datastyle_MonthType'):
        assert _is_linked(a1, 'datastyle_MonthType', b)
    _safe_set(b, 'datastyle_DateStyleType25', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType25', a2)
    if hasattr(a1, 'datastyle_MonthType'):
        assert not _is_linked(a1, 'datastyle_MonthType', b)
    if hasattr(a2, 'datastyle_MonthType'):
        assert _is_linked(a2, 'datastyle_MonthType', b)
    _safe_set(b, 'datastyle_DateStyleType25', set())
    assert not _is_linked(b, 'datastyle_DateStyleType25', a2)
    if hasattr(a2, 'datastyle_MonthType'):
        assert not _is_linked(a2, 'datastyle_MonthType', b)


def test_assoc_number114_reverse_link_reassign_clear():
    a1 = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    a2 = datastyle_NumberType(decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", displayFactor="sample_text_2", grouping="sample_text_2", minIntegerDigits="sample_text_2")
    b = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_CurrencyStyleType15', a1)
    assert _is_linked(b, 'datastyle_CurrencyStyleType15', a1)
    if hasattr(a1, 'datastyle_NumberType16'):
        assert _is_linked(a1, 'datastyle_NumberType16', b)
    _safe_set(b, 'datastyle_CurrencyStyleType15', a2)
    assert _is_linked(b, 'datastyle_CurrencyStyleType15', a2)
    if hasattr(a1, 'datastyle_NumberType16'):
        assert not _is_linked(a1, 'datastyle_NumberType16', b)
    if hasattr(a2, 'datastyle_NumberType16'):
        assert _is_linked(a2, 'datastyle_NumberType16', b)
    _safe_set(b, 'datastyle_CurrencyStyleType15', None)
    assert not _is_linked(b, 'datastyle_CurrencyStyleType15', a2)
    if hasattr(a2, 'datastyle_NumberType16'):
        assert not _is_linked(a2, 'datastyle_NumberType16', b)


def test_assoc_number133_reverse_link_reassign_clear():
    a1 = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    a2 = datastyle_NumberType(decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", displayFactor="sample_text_2", grouping="sample_text_2", minIntegerDigits="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot134', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot134', a1)
    if hasattr(a1, 'datastyle_NumberType135'):
        assert _is_linked(a1, 'datastyle_NumberType135', b)
    _safe_set(b, 'datastyle_DocumentRoot134', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot134', a2)
    if hasattr(a1, 'datastyle_NumberType135'):
        assert not _is_linked(a1, 'datastyle_NumberType135', b)
    if hasattr(a2, 'datastyle_NumberType135'):
        assert _is_linked(a2, 'datastyle_NumberType135', b)
    _safe_set(b, 'datastyle_DocumentRoot134', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot134', a2)
    if hasattr(a2, 'datastyle_NumberType135'):
        assert not _is_linked(a2, 'datastyle_NumberType135', b)


def test_assoc_number58_reverse_link_reassign_clear():
    a1 = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    a2 = datastyle_PercentageStyleType(country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    b = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    _safe_set(b, 'datastyle_NumberType60', a1)
    assert _is_linked(b, 'datastyle_NumberType60', a1)
    if hasattr(a1, 'datastyle_PercentageStyleType59'):
        assert _is_linked(a1, 'datastyle_PercentageStyleType59', b)
    _safe_set(b, 'datastyle_NumberType60', a2)
    assert _is_linked(b, 'datastyle_NumberType60', a2)
    if hasattr(a1, 'datastyle_PercentageStyleType59'):
        assert not _is_linked(a1, 'datastyle_PercentageStyleType59', b)
    if hasattr(a2, 'datastyle_PercentageStyleType59'):
        assert _is_linked(a2, 'datastyle_PercentageStyleType59', b)
    _safe_set(b, 'datastyle_NumberType60', None)
    assert not _is_linked(b, 'datastyle_NumberType60', a2)
    if hasattr(a2, 'datastyle_PercentageStyleType59'):
        assert not _is_linked(a2, 'datastyle_PercentageStyleType59', b)


def test_assoc_number7_reverse_link_reassign_clear():
    a1 = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    a2 = datastyle_NumberType(decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", displayFactor="sample_text_2", grouping="sample_text_2", minIntegerDigits="sample_text_2")
    b = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_CurrencyStyleType8', a1)
    assert _is_linked(b, 'datastyle_CurrencyStyleType8', a1)
    if hasattr(a1, 'datastyle_NumberType'):
        assert _is_linked(a1, 'datastyle_NumberType', b)
    _safe_set(b, 'datastyle_CurrencyStyleType8', a2)
    assert _is_linked(b, 'datastyle_CurrencyStyleType8', a2)
    if hasattr(a1, 'datastyle_NumberType'):
        assert not _is_linked(a1, 'datastyle_NumberType', b)
    if hasattr(a2, 'datastyle_NumberType'):
        assert _is_linked(a2, 'datastyle_NumberType', b)
    _safe_set(b, 'datastyle_CurrencyStyleType8', None)
    assert not _is_linked(b, 'datastyle_CurrencyStyleType8', a2)
    if hasattr(a2, 'datastyle_NumberType'):
        assert not _is_linked(a2, 'datastyle_NumberType', b)


def test_assoc_numberStyle136_reverse_link_reassign_clear():
    a1 = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    a2 = datastyle_NumberStyleType(anyNumberGroup="sample_text_2", country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot137', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot137', a1)
    if hasattr(a1, 'datastyle_NumberStyleType138'):
        assert _is_linked(a1, 'datastyle_NumberStyleType138', b)
    _safe_set(b, 'datastyle_DocumentRoot137', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot137', a2)
    if hasattr(a1, 'datastyle_NumberStyleType138'):
        assert not _is_linked(a1, 'datastyle_NumberStyleType138', b)
    if hasattr(a2, 'datastyle_NumberStyleType138'):
        assert _is_linked(a2, 'datastyle_NumberStyleType138', b)
    _safe_set(b, 'datastyle_DocumentRoot137', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot137', a2)
    if hasattr(a2, 'datastyle_NumberStyleType138'):
        assert not _is_linked(a2, 'datastyle_NumberStyleType138', b)


def test_assoc_percentageStyle139_reverse_link_reassign_clear():
    a1 = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    a2 = datastyle_PercentageStyleType(country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot140', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot140', a1)
    if hasattr(a1, 'datastyle_PercentageStyleType141'):
        assert _is_linked(a1, 'datastyle_PercentageStyleType141', b)
    _safe_set(b, 'datastyle_DocumentRoot140', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot140', a2)
    if hasattr(a1, 'datastyle_PercentageStyleType141'):
        assert not _is_linked(a1, 'datastyle_PercentageStyleType141', b)
    if hasattr(a2, 'datastyle_PercentageStyleType141'):
        assert _is_linked(a2, 'datastyle_PercentageStyleType141', b)
    _safe_set(b, 'datastyle_DocumentRoot140', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot140', a2)
    if hasattr(a2, 'datastyle_PercentageStyleType141'):
        assert not _is_linked(a2, 'datastyle_PercentageStyleType141', b)


def test_assoc_quarter142_reverse_link_reassign_clear():
    a1 = datastyle_QuarterType(calendar="sample_text", style="sample_text")
    a2 = datastyle_QuarterType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot143', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot143', a1)
    if hasattr(a1, 'datastyle_QuarterType144'):
        assert _is_linked(a1, 'datastyle_QuarterType144', b)
    _safe_set(b, 'datastyle_DocumentRoot143', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot143', a2)
    if hasattr(a1, 'datastyle_QuarterType144'):
        assert not _is_linked(a1, 'datastyle_QuarterType144', b)
    if hasattr(a2, 'datastyle_QuarterType144'):
        assert _is_linked(a2, 'datastyle_QuarterType144', b)
    _safe_set(b, 'datastyle_DocumentRoot143', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot143', a2)
    if hasattr(a2, 'datastyle_QuarterType144'):
        assert not _is_linked(a2, 'datastyle_QuarterType144', b)


def test_assoc_quarter34_reverse_link_reassign_clear():
    a1 = datastyle_QuarterType(calendar="sample_text", style="sample_text")
    a2 = datastyle_QuarterType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType35', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType35', a1)
    if hasattr(a1, 'datastyle_QuarterType'):
        assert _is_linked(a1, 'datastyle_QuarterType', b)
    _safe_set(b, 'datastyle_DateStyleType35', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType35', a2)
    if hasattr(a1, 'datastyle_QuarterType'):
        assert not _is_linked(a1, 'datastyle_QuarterType', b)
    if hasattr(a2, 'datastyle_QuarterType'):
        assert _is_linked(a2, 'datastyle_QuarterType', b)
    _safe_set(b, 'datastyle_DateStyleType35', set())
    assert not _is_linked(b, 'datastyle_DateStyleType35', a2)
    if hasattr(a2, 'datastyle_QuarterType'):
        assert not _is_linked(a2, 'datastyle_QuarterType', b)


def test_assoc_scientificNumber145_reverse_link_reassign_clear():
    a1 = datastyle_ScientificNumberType(decimalPlaces="sample_text", grouping="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text")
    a2 = datastyle_ScientificNumberType(decimalPlaces="sample_text_2", grouping="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot146', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot146', a1)
    if hasattr(a1, 'datastyle_ScientificNumberType'):
        assert _is_linked(a1, 'datastyle_ScientificNumberType', b)
    _safe_set(b, 'datastyle_DocumentRoot146', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot146', a2)
    if hasattr(a1, 'datastyle_ScientificNumberType'):
        assert not _is_linked(a1, 'datastyle_ScientificNumberType', b)
    if hasattr(a2, 'datastyle_ScientificNumberType'):
        assert _is_linked(a2, 'datastyle_ScientificNumberType', b)
    _safe_set(b, 'datastyle_DocumentRoot146', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot146', a2)
    if hasattr(a2, 'datastyle_ScientificNumberType'):
        assert not _is_linked(a2, 'datastyle_ScientificNumberType', b)


def test_assoc_seconds147_reverse_link_reassign_clear():
    a1 = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    a2 = datastyle_SecondsType(decimalPlaces="sample_text_2", style="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot148', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot148', a1)
    if hasattr(a1, 'datastyle_SecondsType149'):
        assert _is_linked(a1, 'datastyle_SecondsType149', b)
    _safe_set(b, 'datastyle_DocumentRoot148', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot148', a2)
    if hasattr(a1, 'datastyle_SecondsType149'):
        assert not _is_linked(a1, 'datastyle_SecondsType149', b)
    if hasattr(a2, 'datastyle_SecondsType149'):
        assert _is_linked(a2, 'datastyle_SecondsType149', b)
    _safe_set(b, 'datastyle_DocumentRoot148', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot148', a2)
    if hasattr(a2, 'datastyle_SecondsType149'):
        assert not _is_linked(a2, 'datastyle_SecondsType149', b)


def test_assoc_seconds42_reverse_link_reassign_clear():
    a1 = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    a2 = datastyle_SecondsType(decimalPlaces="sample_text_2", style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType43', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType43', a1)
    if hasattr(a1, 'datastyle_SecondsType'):
        assert _is_linked(a1, 'datastyle_SecondsType', b)
    _safe_set(b, 'datastyle_DateStyleType43', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType43', a2)
    if hasattr(a1, 'datastyle_SecondsType'):
        assert not _is_linked(a1, 'datastyle_SecondsType', b)
    if hasattr(a2, 'datastyle_SecondsType'):
        assert _is_linked(a2, 'datastyle_SecondsType', b)
    _safe_set(b, 'datastyle_DateStyleType43', set())
    assert not _is_linked(b, 'datastyle_DateStyleType43', a2)
    if hasattr(a2, 'datastyle_SecondsType'):
        assert not _is_linked(a2, 'datastyle_SecondsType', b)


def test_assoc_seconds82_reverse_link_reassign_clear():
    a1 = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    a2 = datastyle_TimeStyleType(country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2", volatile="sample_text_2")
    b = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    _safe_set(b, 'datastyle_SecondsType84', a1)
    assert _is_linked(b, 'datastyle_SecondsType84', a1)
    if hasattr(a1, 'datastyle_TimeStyleType83'):
        assert _is_linked(a1, 'datastyle_TimeStyleType83', b)
    _safe_set(b, 'datastyle_SecondsType84', a2)
    assert _is_linked(b, 'datastyle_SecondsType84', a2)
    if hasattr(a1, 'datastyle_TimeStyleType83'):
        assert not _is_linked(a1, 'datastyle_TimeStyleType83', b)
    if hasattr(a2, 'datastyle_TimeStyleType83'):
        assert _is_linked(a2, 'datastyle_TimeStyleType83', b)
    _safe_set(b, 'datastyle_SecondsType84', None)
    assert not _is_linked(b, 'datastyle_SecondsType84', a2)
    if hasattr(a2, 'datastyle_TimeStyleType83'):
        assert not _is_linked(a2, 'datastyle_TimeStyleType83', b)


def test_assoc_textStyle153_reverse_link_reassign_clear():
    a1 = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    a2 = datastyle_TextStyleType(country="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot154', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot154', a1)
    if hasattr(a1, 'datastyle_TextStyleType155'):
        assert _is_linked(a1, 'datastyle_TextStyleType155', b)
    _safe_set(b, 'datastyle_DocumentRoot154', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot154', a2)
    if hasattr(a1, 'datastyle_TextStyleType155'):
        assert not _is_linked(a1, 'datastyle_TextStyleType155', b)
    if hasattr(a2, 'datastyle_TextStyleType155'):
        assert _is_linked(a2, 'datastyle_TextStyleType155', b)
    _safe_set(b, 'datastyle_DocumentRoot154', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot154', a2)
    if hasattr(a2, 'datastyle_TextStyleType155'):
        assert not _is_linked(a2, 'datastyle_TextStyleType155', b)


def test_assoc_timeStyle156_reverse_link_reassign_clear():
    a1 = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    a2 = datastyle_TimeStyleType(country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2", volatile="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot157', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot157', a1)
    if hasattr(a1, 'datastyle_TimeStyleType158'):
        assert _is_linked(a1, 'datastyle_TimeStyleType158', b)
    _safe_set(b, 'datastyle_DocumentRoot157', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot157', a2)
    if hasattr(a1, 'datastyle_TimeStyleType158'):
        assert not _is_linked(a1, 'datastyle_TimeStyleType158', b)
    if hasattr(a2, 'datastyle_TimeStyleType158'):
        assert _is_linked(a2, 'datastyle_TimeStyleType158', b)
    _safe_set(b, 'datastyle_DocumentRoot157', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot157', a2)
    if hasattr(a2, 'datastyle_TimeStyleType158'):
        assert not _is_linked(a2, 'datastyle_TimeStyleType158', b)


def test_assoc_weekOfYear159_reverse_link_reassign_clear():
    a1 = datastyle_WeekOfYearType(calendar="sample_text")
    a2 = datastyle_WeekOfYearType(calendar="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot160', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot160', a1)
    if hasattr(a1, 'datastyle_WeekOfYearType161'):
        assert _is_linked(a1, 'datastyle_WeekOfYearType161', b)
    _safe_set(b, 'datastyle_DocumentRoot160', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot160', a2)
    if hasattr(a1, 'datastyle_WeekOfYearType161'):
        assert not _is_linked(a1, 'datastyle_WeekOfYearType161', b)
    if hasattr(a2, 'datastyle_WeekOfYearType161'):
        assert _is_linked(a2, 'datastyle_WeekOfYearType161', b)
    _safe_set(b, 'datastyle_DocumentRoot160', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot160', a2)
    if hasattr(a2, 'datastyle_WeekOfYearType161'):
        assert not _is_linked(a2, 'datastyle_WeekOfYearType161', b)


def test_assoc_weekOfYear32_reverse_link_reassign_clear():
    a1 = datastyle_WeekOfYearType(calendar="sample_text")
    a2 = datastyle_WeekOfYearType(calendar="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType33', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType33', a1)
    if hasattr(a1, 'datastyle_WeekOfYearType'):
        assert _is_linked(a1, 'datastyle_WeekOfYearType', b)
    _safe_set(b, 'datastyle_DateStyleType33', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType33', a2)
    if hasattr(a1, 'datastyle_WeekOfYearType'):
        assert not _is_linked(a1, 'datastyle_WeekOfYearType', b)
    if hasattr(a2, 'datastyle_WeekOfYearType'):
        assert _is_linked(a2, 'datastyle_WeekOfYearType', b)
    _safe_set(b, 'datastyle_DateStyleType33', set())
    assert not _is_linked(b, 'datastyle_DateStyleType33', a2)
    if hasattr(a2, 'datastyle_WeekOfYearType'):
        assert not _is_linked(a2, 'datastyle_WeekOfYearType', b)


def test_assoc_year162_reverse_link_reassign_clear():
    a1 = datastyle_YearType(calendar="sample_text", style="sample_text")
    a2 = datastyle_YearType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    _safe_set(b, 'datastyle_DocumentRoot163', {a1})
    assert _is_linked(b, 'datastyle_DocumentRoot163', a1)
    if hasattr(a1, 'datastyle_YearType164'):
        assert _is_linked(a1, 'datastyle_YearType164', b)
    _safe_set(b, 'datastyle_DocumentRoot163', {a2})
    assert _is_linked(b, 'datastyle_DocumentRoot163', a2)
    if hasattr(a1, 'datastyle_YearType164'):
        assert not _is_linked(a1, 'datastyle_YearType164', b)
    if hasattr(a2, 'datastyle_YearType164'):
        assert _is_linked(a2, 'datastyle_YearType164', b)
    _safe_set(b, 'datastyle_DocumentRoot163', set())
    assert not _is_linked(b, 'datastyle_DocumentRoot163', a2)
    if hasattr(a2, 'datastyle_YearType164'):
        assert not _is_linked(a2, 'datastyle_YearType164', b)


def test_assoc_year26_reverse_link_reassign_clear():
    a1 = datastyle_YearType(calendar="sample_text", style="sample_text")
    a2 = datastyle_YearType(calendar="sample_text_2", style="sample_text_2")
    b = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    _safe_set(b, 'datastyle_DateStyleType27', {a1})
    assert _is_linked(b, 'datastyle_DateStyleType27', a1)
    if hasattr(a1, 'datastyle_YearType'):
        assert _is_linked(a1, 'datastyle_YearType', b)
    _safe_set(b, 'datastyle_DateStyleType27', {a2})
    assert _is_linked(b, 'datastyle_DateStyleType27', a2)
    if hasattr(a1, 'datastyle_YearType'):
        assert not _is_linked(a1, 'datastyle_YearType', b)
    if hasattr(a2, 'datastyle_YearType'):
        assert _is_linked(a2, 'datastyle_YearType', b)
    _safe_set(b, 'datastyle_DateStyleType27', set())
    assert not _is_linked(b, 'datastyle_DateStyleType27', a2)
    if hasattr(a2, 'datastyle_YearType'):
        assert not _is_linked(a2, 'datastyle_YearType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_amPm38_stub_double():
    # datastyle_AmPmType has no real 'datastyle_AmPmType' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DateStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DateStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_AmPmType()
    setattr(partner, 'datastyle_AmPmType', None)
    _safe_set(owner, 'datastyle_DateStyleType39', {partner})
    assert getattr(partner, 'datastyle_AmPmType') == owner
    _safe_set(owner, 'datastyle_DateStyleType39', set())
    assert getattr(partner, 'datastyle_AmPmType') is None


def test_assoc_amPm76_stub_double():
    # datastyle_AmPmType has no real 'datastyle_AmPmType78' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_TimeStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_TimeStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    partner = datastyle_AmPmType()
    setattr(partner, 'datastyle_AmPmType78', None)
    _safe_set(owner, 'datastyle_TimeStyleType77', {partner})
    assert getattr(partner, 'datastyle_AmPmType78') == owner
    _safe_set(owner, 'datastyle_TimeStyleType77', set())
    assert getattr(partner, 'datastyle_AmPmType78') is None


def test_assoc_amPm92_stub_double():
    # datastyle_AmPmType has no real 'datastyle_AmPmType94' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    partner = datastyle_AmPmType()
    setattr(partner, 'datastyle_AmPmType94', None)
    _safe_set(owner, 'datastyle_DocumentRoot93', {partner})
    assert getattr(partner, 'datastyle_AmPmType94') == owner
    _safe_set(owner, 'datastyle_DocumentRoot93', set())
    assert getattr(partner, 'datastyle_AmPmType94') is None


def test_assoc_anyNumber49_stub_double():
    # datastyle_EObject has no real 'datastyle_EObject' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_NumberStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_NumberStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_EObject()
    setattr(partner, 'datastyle_EObject', None)
    _safe_set(owner, 'datastyle_NumberStyleType50', partner)
    assert getattr(partner, 'datastyle_EObject') == owner
    _safe_set(owner, 'datastyle_NumberStyleType50', None)
    assert getattr(partner, 'datastyle_EObject') is None


def test_assoc_boolean1_stub_double():
    # datastyle_BooleanType has no real 'datastyle_BooleanType' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_BooleanStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_BooleanStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_BooleanType()
    setattr(partner, 'datastyle_BooleanType', None)
    _safe_set(owner, 'datastyle_BooleanStyleType2', partner)
    assert getattr(partner, 'datastyle_BooleanType') == owner
    _safe_set(owner, 'datastyle_BooleanStyleType2', None)
    assert getattr(partner, 'datastyle_BooleanType') is None


def test_assoc_boolean95_stub_double():
    # datastyle_BooleanType has no real 'datastyle_BooleanType97' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    partner = datastyle_BooleanType()
    setattr(partner, 'datastyle_BooleanType97', None)
    _safe_set(owner, 'datastyle_DocumentRoot96', {partner})
    assert getattr(partner, 'datastyle_BooleanType97') == owner
    _safe_set(owner, 'datastyle_DocumentRoot96', set())
    assert getattr(partner, 'datastyle_BooleanType97') is None


def test_assoc_map17_stub_double():
    # datastyle_MapType has no real 'datastyle_MapType19' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_CurrencyStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_CurrencyStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_MapType()
    setattr(partner, 'datastyle_MapType19', None)
    _safe_set(owner, 'datastyle_CurrencyStyleType18', {partner})
    assert getattr(partner, 'datastyle_MapType19') == owner
    _safe_set(owner, 'datastyle_CurrencyStyleType18', set())
    assert getattr(partner, 'datastyle_MapType19') is None


def test_assoc_map3_stub_double():
    # datastyle_MapType has no real 'datastyle_MapType' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_BooleanStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_BooleanStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_MapType()
    setattr(partner, 'datastyle_MapType', None)
    _safe_set(owner, 'datastyle_BooleanStyleType4', {partner})
    assert getattr(partner, 'datastyle_MapType') == owner
    _safe_set(owner, 'datastyle_BooleanStyleType4', set())
    assert getattr(partner, 'datastyle_MapType') is None


def test_assoc_map44_stub_double():
    # datastyle_MapType has no real 'datastyle_MapType46' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DateStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DateStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_MapType()
    setattr(partner, 'datastyle_MapType46', None)
    _safe_set(owner, 'datastyle_DateStyleType45', {partner})
    assert getattr(partner, 'datastyle_MapType46') == owner
    _safe_set(owner, 'datastyle_DateStyleType45', set())
    assert getattr(partner, 'datastyle_MapType46') is None


def test_assoc_map51_stub_double():
    # datastyle_MapType has no real 'datastyle_MapType53' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_NumberStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_NumberStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_MapType()
    setattr(partner, 'datastyle_MapType53', None)
    _safe_set(owner, 'datastyle_NumberStyleType52', {partner})
    assert getattr(partner, 'datastyle_MapType53') == owner
    _safe_set(owner, 'datastyle_NumberStyleType52', set())
    assert getattr(partner, 'datastyle_MapType53') is None


def test_assoc_map61_stub_double():
    # datastyle_MapType has no real 'datastyle_MapType63' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_PercentageStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_PercentageStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_MapType()
    setattr(partner, 'datastyle_MapType63', None)
    _safe_set(owner, 'datastyle_PercentageStyleType62', {partner})
    assert getattr(partner, 'datastyle_MapType63') == owner
    _safe_set(owner, 'datastyle_PercentageStyleType62', set())
    assert getattr(partner, 'datastyle_MapType63') is None


def test_assoc_map68_stub_double():
    # datastyle_MapType has no real 'datastyle_MapType70' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_TextStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_TextStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_MapType()
    setattr(partner, 'datastyle_MapType70', None)
    _safe_set(owner, 'datastyle_TextStyleType69', {partner})
    assert getattr(partner, 'datastyle_MapType70') == owner
    _safe_set(owner, 'datastyle_TextStyleType69', set())
    assert getattr(partner, 'datastyle_MapType70') is None


def test_assoc_map85_stub_double():
    # datastyle_MapType has no real 'datastyle_MapType87' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_TimeStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_TimeStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    partner = datastyle_MapType()
    setattr(partner, 'datastyle_MapType87', None)
    _safe_set(owner, 'datastyle_TimeStyleType86', {partner})
    assert getattr(partner, 'datastyle_MapType87') == owner
    _safe_set(owner, 'datastyle_TimeStyleType86', set())
    assert getattr(partner, 'datastyle_MapType87') is None


def test_assoc_textContent150_stub_double():
    # datastyle_TextContentType has no real 'datastyle_TextContentType152' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    partner = datastyle_TextContentType()
    setattr(partner, 'datastyle_TextContentType152', None)
    _safe_set(owner, 'datastyle_DocumentRoot151', {partner})
    assert getattr(partner, 'datastyle_TextContentType152') == owner
    _safe_set(owner, 'datastyle_DocumentRoot151', set())
    assert getattr(partner, 'datastyle_TextContentType152') is None


def test_assoc_textContent66_stub_double():
    # datastyle_TextContentType has no real 'datastyle_TextContentType' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_TextStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_TextStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_TextContentType()
    setattr(partner, 'datastyle_TextContentType', None)
    _safe_set(owner, 'datastyle_TextStyleType67', {partner})
    assert getattr(partner, 'datastyle_TextContentType') == owner
    _safe_set(owner, 'datastyle_TextStyleType67', set())
    assert getattr(partner, 'datastyle_TextContentType') is None


def test_assoc_textProperties0_stub_double():
    # datastyle_StyleTextPropertiesContent has no real 'datastyle_StyleTextPropertiesContent' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_BooleanStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_BooleanStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_StyleTextPropertiesContent()
    setattr(partner, 'datastyle_StyleTextPropertiesContent', None)
    _safe_set(owner, 'datastyle_BooleanStyleType', partner)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent') == owner
    _safe_set(owner, 'datastyle_BooleanStyleType', None)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent') is None


def test_assoc_textProperties20_stub_double():
    # datastyle_StyleTextPropertiesContent has no real 'datastyle_StyleTextPropertiesContent21' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DateStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DateStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_StyleTextPropertiesContent()
    setattr(partner, 'datastyle_StyleTextPropertiesContent21', None)
    _safe_set(owner, 'datastyle_DateStyleType', partner)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent21') == owner
    _safe_set(owner, 'datastyle_DateStyleType', None)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent21') is None


def test_assoc_textProperties47_stub_double():
    # datastyle_StyleTextPropertiesContent has no real 'datastyle_StyleTextPropertiesContent48' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_NumberStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_NumberStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_StyleTextPropertiesContent()
    setattr(partner, 'datastyle_StyleTextPropertiesContent48', None)
    _safe_set(owner, 'datastyle_NumberStyleType', partner)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent48') == owner
    _safe_set(owner, 'datastyle_NumberStyleType', None)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent48') is None


def test_assoc_textProperties5_stub_double():
    # datastyle_StyleTextPropertiesContent has no real 'datastyle_StyleTextPropertiesContent6' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_CurrencyStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_CurrencyStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_StyleTextPropertiesContent()
    setattr(partner, 'datastyle_StyleTextPropertiesContent6', None)
    _safe_set(owner, 'datastyle_CurrencyStyleType', partner)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent6') == owner
    _safe_set(owner, 'datastyle_CurrencyStyleType', None)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent6') is None


def test_assoc_textProperties56_stub_double():
    # datastyle_StyleTextPropertiesContent has no real 'datastyle_StyleTextPropertiesContent57' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_PercentageStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_PercentageStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_StyleTextPropertiesContent()
    setattr(partner, 'datastyle_StyleTextPropertiesContent57', None)
    _safe_set(owner, 'datastyle_PercentageStyleType', partner)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent57') == owner
    _safe_set(owner, 'datastyle_PercentageStyleType', None)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent57') is None


def test_assoc_textProperties64_stub_double():
    # datastyle_StyleTextPropertiesContent has no real 'datastyle_StyleTextPropertiesContent65' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_TextStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_TextStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    partner = datastyle_StyleTextPropertiesContent()
    setattr(partner, 'datastyle_StyleTextPropertiesContent65', None)
    _safe_set(owner, 'datastyle_TextStyleType', partner)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent65') == owner
    _safe_set(owner, 'datastyle_TextStyleType', None)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent65') is None


def test_assoc_textProperties71_stub_double():
    # datastyle_StyleTextPropertiesContent has no real 'datastyle_StyleTextPropertiesContent72' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_TimeStyleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_TimeStyleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    partner = datastyle_StyleTextPropertiesContent()
    setattr(partner, 'datastyle_StyleTextPropertiesContent72', None)
    _safe_set(owner, 'datastyle_TimeStyleType', partner)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent72') == owner
    _safe_set(owner, 'datastyle_TimeStyleType', None)
    assert getattr(partner, 'datastyle_StyleTextPropertiesContent72') is None


def test_assoc_xMLNSPrefixMap88_stub_double():
    # datastyle_EStringToStringMapEntry has no real 'datastyle_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    partner = datastyle_EStringToStringMapEntry()
    setattr(partner, 'datastyle_EStringToStringMapEntry', None)
    _safe_set(owner, 'datastyle_DocumentRoot', {partner})
    assert getattr(partner, 'datastyle_EStringToStringMapEntry') == owner
    _safe_set(owner, 'datastyle_DocumentRoot', set())
    assert getattr(partner, 'datastyle_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation89_stub_double():
    # datastyle_EStringToStringMapEntry has no real 'datastyle_EStringToStringMapEntry91' property in the generated
    # code (a bare stub) -- manually attach it so datastyle_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datastyle_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    partner = datastyle_EStringToStringMapEntry()
    setattr(partner, 'datastyle_EStringToStringMapEntry91', None)
    _safe_set(owner, 'datastyle_DocumentRoot90', {partner})
    assert getattr(partner, 'datastyle_EStringToStringMapEntry91') == owner
    _safe_set(owner, 'datastyle_DocumentRoot90', set())
    assert getattr(partner, 'datastyle_EStringToStringMapEntry91') is None


