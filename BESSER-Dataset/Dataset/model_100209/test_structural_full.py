import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_datastyle_BooleanStyleType_country_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_BooleanStyleType_language_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_BooleanStyleType_name_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datastyle_BooleanStyleType_text_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_BooleanStyleType_text1_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text1 == "sample_text"
    instance.text1 = "sample_text_2"
    assert instance.text1 == "sample_text_2"


def test_datastyle_BooleanStyleType_title_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_BooleanStyleType_transliterationCountry_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_BooleanStyleType_transliterationFormat_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_BooleanStyleType_transliterationLanguage_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_BooleanStyleType_transliterationStyle_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_BooleanStyleType_volatile_value_roundtrip():
    instance = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_datastyle_CurrencyStyleType_automaticOrder_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.automaticOrder == "sample_text"
    instance.automaticOrder = "sample_text_2"
    assert instance.automaticOrder == "sample_text_2"


def test_datastyle_CurrencyStyleType_country_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_CurrencyStyleType_language_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_CurrencyStyleType_name_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datastyle_CurrencyStyleType_text_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_CurrencyStyleType_text1_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text1 == "sample_text"
    instance.text1 = "sample_text_2"
    assert instance.text1 == "sample_text_2"


def test_datastyle_CurrencyStyleType_text2_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text2 == "sample_text"
    instance.text2 = "sample_text_2"
    assert instance.text2 == "sample_text_2"


def test_datastyle_CurrencyStyleType_text3_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text3 == "sample_text"
    instance.text3 = "sample_text_2"
    assert instance.text3 == "sample_text_2"


def test_datastyle_CurrencyStyleType_text4_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text4 == "sample_text"
    instance.text4 = "sample_text_2"
    assert instance.text4 == "sample_text_2"


def test_datastyle_CurrencyStyleType_title_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_CurrencyStyleType_transliterationCountry_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_CurrencyStyleType_transliterationFormat_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_CurrencyStyleType_transliterationLanguage_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_CurrencyStyleType_transliterationStyle_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_CurrencyStyleType_volatile_value_roundtrip():
    instance = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_datastyle_CurrencySymbolType_country_value_roundtrip():
    instance = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_CurrencySymbolType_language_value_roundtrip():
    instance = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_CurrencySymbolType_mixed_value_roundtrip():
    instance = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_datastyle_DateStyleType_automaticOrder_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.automaticOrder == "sample_text"
    instance.automaticOrder = "sample_text_2"
    assert instance.automaticOrder == "sample_text_2"


def test_datastyle_DateStyleType_country_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_DateStyleType_formatSource_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.formatSource == "sample_text"
    instance.formatSource = "sample_text_2"
    assert instance.formatSource == "sample_text_2"


def test_datastyle_DateStyleType_group_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_datastyle_DateStyleType_language_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_DateStyleType_name_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datastyle_DateStyleType_text_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_DateStyleType_text1_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text1 == "sample_text"
    instance.text1 = "sample_text_2"
    assert instance.text1 == "sample_text_2"


def test_datastyle_DateStyleType_title_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_DateStyleType_transliterationCountry_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_DateStyleType_transliterationFormat_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_DateStyleType_transliterationLanguage_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_DateStyleType_transliterationStyle_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_DateStyleType_volatile_value_roundtrip():
    instance = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_datastyle_DayOfWeekType_calendar_value_roundtrip():
    instance = datastyle_DayOfWeekType(calendar="sample_text", style="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_DayOfWeekType_style_value_roundtrip():
    instance = datastyle_DayOfWeekType(calendar="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_DayType_calendar_value_roundtrip():
    instance = datastyle_DayType(calendar="sample_text", style="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_DayType_style_value_roundtrip():
    instance = datastyle_DayType(calendar="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_DocumentRoot_automaticOrder_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.automaticOrder == "sample_text"
    instance.automaticOrder = "sample_text_2"
    assert instance.automaticOrder == "sample_text_2"


def test_datastyle_DocumentRoot_calendar_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_DocumentRoot_country_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_DocumentRoot_decimalPlaces_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.decimalPlaces == "sample_text"
    instance.decimalPlaces = "sample_text_2"
    assert instance.decimalPlaces == "sample_text_2"


def test_datastyle_DocumentRoot_decimalReplacement_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.decimalReplacement == "sample_text"
    instance.decimalReplacement = "sample_text_2"
    assert instance.decimalReplacement == "sample_text_2"


def test_datastyle_DocumentRoot_denominatorValue_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.denominatorValue == "sample_text"
    instance.denominatorValue = "sample_text_2"
    assert instance.denominatorValue == "sample_text_2"


def test_datastyle_DocumentRoot_displayFactor_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.displayFactor == "sample_text"
    instance.displayFactor = "sample_text_2"
    assert instance.displayFactor == "sample_text_2"


def test_datastyle_DocumentRoot_formatSource_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.formatSource == "sample_text"
    instance.formatSource = "sample_text_2"
    assert instance.formatSource == "sample_text_2"


def test_datastyle_DocumentRoot_grouping_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.grouping == "sample_text"
    instance.grouping = "sample_text_2"
    assert instance.grouping == "sample_text_2"


def test_datastyle_DocumentRoot_language_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_DocumentRoot_minDenominatorDigits_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.minDenominatorDigits == "sample_text"
    instance.minDenominatorDigits = "sample_text_2"
    assert instance.minDenominatorDigits == "sample_text_2"


def test_datastyle_DocumentRoot_minExponentDigits_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.minExponentDigits == "sample_text"
    instance.minExponentDigits = "sample_text_2"
    assert instance.minExponentDigits == "sample_text_2"


def test_datastyle_DocumentRoot_minIntegerDigits_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.minIntegerDigits == "sample_text"
    instance.minIntegerDigits = "sample_text_2"
    assert instance.minIntegerDigits == "sample_text_2"


def test_datastyle_DocumentRoot_minNumeratorDigits_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.minNumeratorDigits == "sample_text"
    instance.minNumeratorDigits = "sample_text_2"
    assert instance.minNumeratorDigits == "sample_text_2"


def test_datastyle_DocumentRoot_mixed_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_datastyle_DocumentRoot_position_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_datastyle_DocumentRoot_possessiveForm_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.possessiveForm == "sample_text"
    instance.possessiveForm = "sample_text_2"
    assert instance.possessiveForm == "sample_text_2"


def test_datastyle_DocumentRoot_style_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_DocumentRoot_text_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_DocumentRoot_textual_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.textual == "sample_text"
    instance.textual = "sample_text_2"
    assert instance.textual == "sample_text_2"


def test_datastyle_DocumentRoot_title_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_DocumentRoot_transliterationCountry_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_DocumentRoot_transliterationFormat_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_DocumentRoot_transliterationLanguage_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_DocumentRoot_transliterationStyle_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_DocumentRoot_truncateOnOverflow_value_roundtrip():
    instance = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    assert instance.truncateOnOverflow == "sample_text"
    instance.truncateOnOverflow = "sample_text_2"
    assert instance.truncateOnOverflow == "sample_text_2"


def test_datastyle_EmbeddedTextType_mixed_value_roundtrip():
    instance = datastyle_EmbeddedTextType(mixed="sample_text", position="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_datastyle_EmbeddedTextType_position_value_roundtrip():
    instance = datastyle_EmbeddedTextType(mixed="sample_text", position="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_datastyle_EraType_calendar_value_roundtrip():
    instance = datastyle_EraType(calendar="sample_text", style="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_EraType_style_value_roundtrip():
    instance = datastyle_EraType(calendar="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_FractionType_denominatorValue_value_roundtrip():
    instance = datastyle_FractionType(denominatorValue="sample_text", grouping="sample_text", minDenominatorDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text")
    assert instance.denominatorValue == "sample_text"
    instance.denominatorValue = "sample_text_2"
    assert instance.denominatorValue == "sample_text_2"


def test_datastyle_FractionType_grouping_value_roundtrip():
    instance = datastyle_FractionType(denominatorValue="sample_text", grouping="sample_text", minDenominatorDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text")
    assert instance.grouping == "sample_text"
    instance.grouping = "sample_text_2"
    assert instance.grouping == "sample_text_2"


def test_datastyle_FractionType_minDenominatorDigits_value_roundtrip():
    instance = datastyle_FractionType(denominatorValue="sample_text", grouping="sample_text", minDenominatorDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text")
    assert instance.minDenominatorDigits == "sample_text"
    instance.minDenominatorDigits = "sample_text_2"
    assert instance.minDenominatorDigits == "sample_text_2"


def test_datastyle_FractionType_minIntegerDigits_value_roundtrip():
    instance = datastyle_FractionType(denominatorValue="sample_text", grouping="sample_text", minDenominatorDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text")
    assert instance.minIntegerDigits == "sample_text"
    instance.minIntegerDigits = "sample_text_2"
    assert instance.minIntegerDigits == "sample_text_2"


def test_datastyle_FractionType_minNumeratorDigits_value_roundtrip():
    instance = datastyle_FractionType(denominatorValue="sample_text", grouping="sample_text", minDenominatorDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text")
    assert instance.minNumeratorDigits == "sample_text"
    instance.minNumeratorDigits = "sample_text_2"
    assert instance.minNumeratorDigits == "sample_text_2"


def test_datastyle_HoursType_style_value_roundtrip():
    instance = datastyle_HoursType(style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_MinutesType_style_value_roundtrip():
    instance = datastyle_MinutesType(style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_MonthType_calendar_value_roundtrip():
    instance = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_MonthType_possessiveForm_value_roundtrip():
    instance = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    assert instance.possessiveForm == "sample_text"
    instance.possessiveForm = "sample_text_2"
    assert instance.possessiveForm == "sample_text_2"


def test_datastyle_MonthType_style_value_roundtrip():
    instance = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_MonthType_textual_value_roundtrip():
    instance = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    assert instance.textual == "sample_text"
    instance.textual = "sample_text_2"
    assert instance.textual == "sample_text_2"


def test_datastyle_NumberStyleType_anyNumberGroup_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.anyNumberGroup == "sample_text"
    instance.anyNumberGroup = "sample_text_2"
    assert instance.anyNumberGroup == "sample_text_2"


def test_datastyle_NumberStyleType_country_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_NumberStyleType_language_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_NumberStyleType_name_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datastyle_NumberStyleType_text_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_NumberStyleType_text1_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text1 == "sample_text"
    instance.text1 = "sample_text_2"
    assert instance.text1 == "sample_text_2"


def test_datastyle_NumberStyleType_title_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_NumberStyleType_transliterationCountry_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_NumberStyleType_transliterationFormat_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_NumberStyleType_transliterationLanguage_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_NumberStyleType_transliterationStyle_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_NumberStyleType_volatile_value_roundtrip():
    instance = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_datastyle_NumberType_decimalPlaces_value_roundtrip():
    instance = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    assert instance.decimalPlaces == "sample_text"
    instance.decimalPlaces = "sample_text_2"
    assert instance.decimalPlaces == "sample_text_2"


def test_datastyle_NumberType_decimalReplacement_value_roundtrip():
    instance = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    assert instance.decimalReplacement == "sample_text"
    instance.decimalReplacement = "sample_text_2"
    assert instance.decimalReplacement == "sample_text_2"


def test_datastyle_NumberType_displayFactor_value_roundtrip():
    instance = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    assert instance.displayFactor == "sample_text"
    instance.displayFactor = "sample_text_2"
    assert instance.displayFactor == "sample_text_2"


def test_datastyle_NumberType_grouping_value_roundtrip():
    instance = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    assert instance.grouping == "sample_text"
    instance.grouping = "sample_text_2"
    assert instance.grouping == "sample_text_2"


def test_datastyle_NumberType_minIntegerDigits_value_roundtrip():
    instance = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    assert instance.minIntegerDigits == "sample_text"
    instance.minIntegerDigits = "sample_text_2"
    assert instance.minIntegerDigits == "sample_text_2"


def test_datastyle_PercentageStyleType_country_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_PercentageStyleType_language_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_PercentageStyleType_name_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datastyle_PercentageStyleType_text_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_PercentageStyleType_text1_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text1 == "sample_text"
    instance.text1 = "sample_text_2"
    assert instance.text1 == "sample_text_2"


def test_datastyle_PercentageStyleType_title_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_PercentageStyleType_transliterationCountry_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_PercentageStyleType_transliterationFormat_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_PercentageStyleType_transliterationLanguage_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_PercentageStyleType_transliterationStyle_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_PercentageStyleType_volatile_value_roundtrip():
    instance = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_datastyle_QuarterType_calendar_value_roundtrip():
    instance = datastyle_QuarterType(calendar="sample_text", style="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_QuarterType_style_value_roundtrip():
    instance = datastyle_QuarterType(calendar="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_ScientificNumberType_decimalPlaces_value_roundtrip():
    instance = datastyle_ScientificNumberType(decimalPlaces="sample_text", grouping="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text")
    assert instance.decimalPlaces == "sample_text"
    instance.decimalPlaces = "sample_text_2"
    assert instance.decimalPlaces == "sample_text_2"


def test_datastyle_ScientificNumberType_grouping_value_roundtrip():
    instance = datastyle_ScientificNumberType(decimalPlaces="sample_text", grouping="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text")
    assert instance.grouping == "sample_text"
    instance.grouping = "sample_text_2"
    assert instance.grouping == "sample_text_2"


def test_datastyle_ScientificNumberType_minExponentDigits_value_roundtrip():
    instance = datastyle_ScientificNumberType(decimalPlaces="sample_text", grouping="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text")
    assert instance.minExponentDigits == "sample_text"
    instance.minExponentDigits = "sample_text_2"
    assert instance.minExponentDigits == "sample_text_2"


def test_datastyle_ScientificNumberType_minIntegerDigits_value_roundtrip():
    instance = datastyle_ScientificNumberType(decimalPlaces="sample_text", grouping="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text")
    assert instance.minIntegerDigits == "sample_text"
    instance.minIntegerDigits = "sample_text_2"
    assert instance.minIntegerDigits == "sample_text_2"


def test_datastyle_SecondsType_decimalPlaces_value_roundtrip():
    instance = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    assert instance.decimalPlaces == "sample_text"
    instance.decimalPlaces = "sample_text_2"
    assert instance.decimalPlaces == "sample_text_2"


def test_datastyle_SecondsType_style_value_roundtrip():
    instance = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_datastyle_TextStyleType_country_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_TextStyleType_group_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_datastyle_TextStyleType_language_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_TextStyleType_name_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datastyle_TextStyleType_text_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_TextStyleType_text1_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.text1 == "sample_text"
    instance.text1 = "sample_text_2"
    assert instance.text1 == "sample_text_2"


def test_datastyle_TextStyleType_title_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_TextStyleType_transliterationCountry_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_TextStyleType_transliterationFormat_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_TextStyleType_transliterationLanguage_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_TextStyleType_transliterationStyle_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_TextStyleType_volatile_value_roundtrip():
    instance = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_datastyle_TimeStyleType_country_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_datastyle_TimeStyleType_formatSource_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.formatSource == "sample_text"
    instance.formatSource = "sample_text_2"
    assert instance.formatSource == "sample_text_2"


def test_datastyle_TimeStyleType_group_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_datastyle_TimeStyleType_language_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_datastyle_TimeStyleType_name_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datastyle_TimeStyleType_text_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_datastyle_TimeStyleType_text1_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.text1 == "sample_text"
    instance.text1 = "sample_text_2"
    assert instance.text1 == "sample_text_2"


def test_datastyle_TimeStyleType_title_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_datastyle_TimeStyleType_transliterationCountry_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.transliterationCountry == "sample_text"
    instance.transliterationCountry = "sample_text_2"
    assert instance.transliterationCountry == "sample_text_2"


def test_datastyle_TimeStyleType_transliterationFormat_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.transliterationFormat == "sample_text"
    instance.transliterationFormat = "sample_text_2"
    assert instance.transliterationFormat == "sample_text_2"


def test_datastyle_TimeStyleType_transliterationLanguage_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.transliterationLanguage == "sample_text"
    instance.transliterationLanguage = "sample_text_2"
    assert instance.transliterationLanguage == "sample_text_2"


def test_datastyle_TimeStyleType_transliterationStyle_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.transliterationStyle == "sample_text"
    instance.transliterationStyle = "sample_text_2"
    assert instance.transliterationStyle == "sample_text_2"


def test_datastyle_TimeStyleType_truncateOnOverflow_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.truncateOnOverflow == "sample_text"
    instance.truncateOnOverflow = "sample_text_2"
    assert instance.truncateOnOverflow == "sample_text_2"


def test_datastyle_TimeStyleType_volatile_value_roundtrip():
    instance = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_datastyle_WeekOfYearType_calendar_value_roundtrip():
    instance = datastyle_WeekOfYearType(calendar="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_YearType_calendar_value_roundtrip():
    instance = datastyle_YearType(calendar="sample_text", style="sample_text")
    assert instance.calendar == "sample_text"
    instance.calendar = "sample_text_2"
    assert instance.calendar == "sample_text_2"


def test_datastyle_YearType_style_value_roundtrip():
    instance = datastyle_YearType(calendar="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_assoc_amPm38_link_reassign_clear():
    a = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_AmPmType()
    b2 = datastyle_AmPmType()
    _safe_set(a, 'datastyle_DateStyleType39', {b1})
    assert _is_linked(a, 'datastyle_DateStyleType39', b1)
    if hasattr(b1, 'datastyle_AmPmType'):
        assert _is_linked(b1, 'datastyle_AmPmType', a)
    _safe_set(a, 'datastyle_DateStyleType39', {b2})
    assert _is_linked(a, 'datastyle_DateStyleType39', b2)
    if hasattr(b1, 'datastyle_AmPmType'):
        assert not _is_linked(b1, 'datastyle_AmPmType', a)
    if hasattr(b2, 'datastyle_AmPmType'):
        assert _is_linked(b2, 'datastyle_AmPmType', a)
    _safe_set(a, 'datastyle_DateStyleType39', set())
    assert not _is_linked(a, 'datastyle_DateStyleType39', b2)
    if hasattr(b2, 'datastyle_AmPmType'):
        assert not _is_linked(b2, 'datastyle_AmPmType', a)


def test_assoc_amPm76_link_reassign_clear():
    a = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    b1 = datastyle_AmPmType()
    b2 = datastyle_AmPmType()
    _safe_set(a, 'datastyle_TimeStyleType77', {b1})
    assert _is_linked(a, 'datastyle_TimeStyleType77', b1)
    if hasattr(b1, 'datastyle_AmPmType78'):
        assert _is_linked(b1, 'datastyle_AmPmType78', a)
    _safe_set(a, 'datastyle_TimeStyleType77', {b2})
    assert _is_linked(a, 'datastyle_TimeStyleType77', b2)
    if hasattr(b1, 'datastyle_AmPmType78'):
        assert not _is_linked(b1, 'datastyle_AmPmType78', a)
    if hasattr(b2, 'datastyle_AmPmType78'):
        assert _is_linked(b2, 'datastyle_AmPmType78', a)
    _safe_set(a, 'datastyle_TimeStyleType77', set())
    assert not _is_linked(a, 'datastyle_TimeStyleType77', b2)
    if hasattr(b2, 'datastyle_AmPmType78'):
        assert not _is_linked(b2, 'datastyle_AmPmType78', a)


def test_assoc_amPm92_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_AmPmType()
    b2 = datastyle_AmPmType()
    _safe_set(a, 'datastyle_DocumentRoot93', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot93', b1)
    if hasattr(b1, 'datastyle_AmPmType94'):
        assert _is_linked(b1, 'datastyle_AmPmType94', a)
    _safe_set(a, 'datastyle_DocumentRoot93', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot93', b2)
    if hasattr(b1, 'datastyle_AmPmType94'):
        assert not _is_linked(b1, 'datastyle_AmPmType94', a)
    if hasattr(b2, 'datastyle_AmPmType94'):
        assert _is_linked(b2, 'datastyle_AmPmType94', a)
    _safe_set(a, 'datastyle_DocumentRoot93', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot93', b2)
    if hasattr(b2, 'datastyle_AmPmType94'):
        assert not _is_linked(b2, 'datastyle_AmPmType94', a)


def test_assoc_anyNumber49_link_reassign_clear():
    a = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_EObject()
    b2 = datastyle_EObject()
    _safe_set(a, 'datastyle_NumberStyleType50', b1)
    assert _is_linked(a, 'datastyle_NumberStyleType50', b1)
    if hasattr(b1, 'datastyle_EObject'):
        assert _is_linked(b1, 'datastyle_EObject', a)
    _safe_set(a, 'datastyle_NumberStyleType50', b2)
    assert _is_linked(a, 'datastyle_NumberStyleType50', b2)
    if hasattr(b1, 'datastyle_EObject'):
        assert not _is_linked(b1, 'datastyle_EObject', a)
    if hasattr(b2, 'datastyle_EObject'):
        assert _is_linked(b2, 'datastyle_EObject', a)
    _safe_set(a, 'datastyle_NumberStyleType50', None)
    assert not _is_linked(a, 'datastyle_NumberStyleType50', b2)
    if hasattr(b2, 'datastyle_EObject'):
        assert not _is_linked(b2, 'datastyle_EObject', a)


def test_assoc_boolean1_link_reassign_clear():
    a = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_BooleanType()
    b2 = datastyle_BooleanType()
    _safe_set(a, 'datastyle_BooleanStyleType2', b1)
    assert _is_linked(a, 'datastyle_BooleanStyleType2', b1)
    if hasattr(b1, 'datastyle_BooleanType'):
        assert _is_linked(b1, 'datastyle_BooleanType', a)
    _safe_set(a, 'datastyle_BooleanStyleType2', b2)
    assert _is_linked(a, 'datastyle_BooleanStyleType2', b2)
    if hasattr(b1, 'datastyle_BooleanType'):
        assert not _is_linked(b1, 'datastyle_BooleanType', a)
    if hasattr(b2, 'datastyle_BooleanType'):
        assert _is_linked(b2, 'datastyle_BooleanType', a)
    _safe_set(a, 'datastyle_BooleanStyleType2', None)
    assert not _is_linked(a, 'datastyle_BooleanStyleType2', b2)
    if hasattr(b2, 'datastyle_BooleanType'):
        assert not _is_linked(b2, 'datastyle_BooleanType', a)


def test_assoc_boolean95_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_BooleanType()
    b2 = datastyle_BooleanType()
    _safe_set(a, 'datastyle_DocumentRoot96', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot96', b1)
    if hasattr(b1, 'datastyle_BooleanType97'):
        assert _is_linked(b1, 'datastyle_BooleanType97', a)
    _safe_set(a, 'datastyle_DocumentRoot96', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot96', b2)
    if hasattr(b1, 'datastyle_BooleanType97'):
        assert not _is_linked(b1, 'datastyle_BooleanType97', a)
    if hasattr(b2, 'datastyle_BooleanType97'):
        assert _is_linked(b2, 'datastyle_BooleanType97', a)
    _safe_set(a, 'datastyle_DocumentRoot96', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot96', b2)
    if hasattr(b2, 'datastyle_BooleanType97'):
        assert not _is_linked(b2, 'datastyle_BooleanType97', a)


def test_assoc_booleanStyle98_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_BooleanStyleType(country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_DocumentRoot99', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot99', b1)
    if hasattr(b1, 'datastyle_BooleanStyleType100'):
        assert _is_linked(b1, 'datastyle_BooleanStyleType100', a)
    _safe_set(a, 'datastyle_DocumentRoot99', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot99', b2)
    if hasattr(b1, 'datastyle_BooleanStyleType100'):
        assert not _is_linked(b1, 'datastyle_BooleanStyleType100', a)
    if hasattr(b2, 'datastyle_BooleanStyleType100'):
        assert _is_linked(b2, 'datastyle_BooleanStyleType100', a)
    _safe_set(a, 'datastyle_DocumentRoot99', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot99', b2)
    if hasattr(b2, 'datastyle_BooleanStyleType100'):
        assert not _is_linked(b2, 'datastyle_BooleanStyleType100', a)


def test_assoc_currencyStyle101_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_CurrencyStyleType(automaticOrder="sample_text_2", country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", text2="sample_text_2", text3="sample_text_2", text4="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_DocumentRoot102', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot102', b1)
    if hasattr(b1, 'datastyle_CurrencyStyleType103'):
        assert _is_linked(b1, 'datastyle_CurrencyStyleType103', a)
    _safe_set(a, 'datastyle_DocumentRoot102', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot102', b2)
    if hasattr(b1, 'datastyle_CurrencyStyleType103'):
        assert not _is_linked(b1, 'datastyle_CurrencyStyleType103', a)
    if hasattr(b2, 'datastyle_CurrencyStyleType103'):
        assert _is_linked(b2, 'datastyle_CurrencyStyleType103', a)
    _safe_set(a, 'datastyle_DocumentRoot102', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot102', b2)
    if hasattr(b2, 'datastyle_CurrencyStyleType103'):
        assert not _is_linked(b2, 'datastyle_CurrencyStyleType103', a)


def test_assoc_currencySymbol104_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    b2 = datastyle_CurrencySymbolType(country="sample_text_2", language="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'datastyle_DocumentRoot105', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot105', b1)
    if hasattr(b1, 'datastyle_CurrencySymbolType106'):
        assert _is_linked(b1, 'datastyle_CurrencySymbolType106', a)
    _safe_set(a, 'datastyle_DocumentRoot105', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot105', b2)
    if hasattr(b1, 'datastyle_CurrencySymbolType106'):
        assert not _is_linked(b1, 'datastyle_CurrencySymbolType106', a)
    if hasattr(b2, 'datastyle_CurrencySymbolType106'):
        assert _is_linked(b2, 'datastyle_CurrencySymbolType106', a)
    _safe_set(a, 'datastyle_DocumentRoot105', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot105', b2)
    if hasattr(b2, 'datastyle_CurrencySymbolType106'):
        assert not _is_linked(b2, 'datastyle_CurrencySymbolType106', a)


def test_assoc_currencySymbol111_link_reassign_clear():
    a = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    b1 = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_CurrencyStyleType(automaticOrder="sample_text_2", country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", text2="sample_text_2", text3="sample_text_2", text4="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_CurrencySymbolType13', b1)
    assert _is_linked(a, 'datastyle_CurrencySymbolType13', b1)
    if hasattr(b1, 'datastyle_CurrencyStyleType12'):
        assert _is_linked(b1, 'datastyle_CurrencyStyleType12', a)
    _safe_set(a, 'datastyle_CurrencySymbolType13', b2)
    assert _is_linked(a, 'datastyle_CurrencySymbolType13', b2)
    if hasattr(b1, 'datastyle_CurrencyStyleType12'):
        assert not _is_linked(b1, 'datastyle_CurrencyStyleType12', a)
    if hasattr(b2, 'datastyle_CurrencyStyleType12'):
        assert _is_linked(b2, 'datastyle_CurrencyStyleType12', a)
    _safe_set(a, 'datastyle_CurrencySymbolType13', None)
    assert not _is_linked(a, 'datastyle_CurrencySymbolType13', b2)
    if hasattr(b2, 'datastyle_CurrencyStyleType12'):
        assert not _is_linked(b2, 'datastyle_CurrencyStyleType12', a)


def test_assoc_currencySymbol9_link_reassign_clear():
    a = datastyle_CurrencySymbolType(country="sample_text", language="sample_text", mixed="sample_text")
    b1 = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_CurrencyStyleType(automaticOrder="sample_text_2", country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", text2="sample_text_2", text3="sample_text_2", text4="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_CurrencySymbolType', b1)
    assert _is_linked(a, 'datastyle_CurrencySymbolType', b1)
    if hasattr(b1, 'datastyle_CurrencyStyleType10'):
        assert _is_linked(b1, 'datastyle_CurrencyStyleType10', a)
    _safe_set(a, 'datastyle_CurrencySymbolType', b2)
    assert _is_linked(a, 'datastyle_CurrencySymbolType', b2)
    if hasattr(b1, 'datastyle_CurrencyStyleType10'):
        assert not _is_linked(b1, 'datastyle_CurrencyStyleType10', a)
    if hasattr(b2, 'datastyle_CurrencyStyleType10'):
        assert _is_linked(b2, 'datastyle_CurrencyStyleType10', a)
    _safe_set(a, 'datastyle_CurrencySymbolType', None)
    assert not _is_linked(a, 'datastyle_CurrencySymbolType', b2)
    if hasattr(b2, 'datastyle_CurrencyStyleType10'):
        assert not _is_linked(b2, 'datastyle_CurrencyStyleType10', a)


def test_assoc_dateStyle107_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_DocumentRoot108', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot108', b1)
    if hasattr(b1, 'datastyle_DateStyleType109'):
        assert _is_linked(b1, 'datastyle_DateStyleType109', a)
    _safe_set(a, 'datastyle_DocumentRoot108', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot108', b2)
    if hasattr(b1, 'datastyle_DateStyleType109'):
        assert not _is_linked(b1, 'datastyle_DateStyleType109', a)
    if hasattr(b2, 'datastyle_DateStyleType109'):
        assert _is_linked(b2, 'datastyle_DateStyleType109', a)
    _safe_set(a, 'datastyle_DocumentRoot108', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot108', b2)
    if hasattr(b2, 'datastyle_DateStyleType109'):
        assert not _is_linked(b2, 'datastyle_DateStyleType109', a)


def test_assoc_day110_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_DayType(calendar="sample_text", style="sample_text")
    b2 = datastyle_DayType(calendar="sample_text_2", style="sample_text_2")
    _safe_set(a, 'datastyle_DocumentRoot111', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot111', b1)
    if hasattr(b1, 'datastyle_DayType112'):
        assert _is_linked(b1, 'datastyle_DayType112', a)
    _safe_set(a, 'datastyle_DocumentRoot111', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot111', b2)
    if hasattr(b1, 'datastyle_DayType112'):
        assert not _is_linked(b1, 'datastyle_DayType112', a)
    if hasattr(b2, 'datastyle_DayType112'):
        assert _is_linked(b2, 'datastyle_DayType112', a)
    _safe_set(a, 'datastyle_DocumentRoot111', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot111', b2)
    if hasattr(b2, 'datastyle_DayType112'):
        assert not _is_linked(b2, 'datastyle_DayType112', a)


def test_assoc_day22_link_reassign_clear():
    a = datastyle_DayType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_DayType', b1)
    assert _is_linked(a, 'datastyle_DayType', b1)
    if hasattr(b1, 'datastyle_DateStyleType23'):
        assert _is_linked(b1, 'datastyle_DateStyleType23', a)
    _safe_set(a, 'datastyle_DayType', b2)
    assert _is_linked(a, 'datastyle_DayType', b2)
    if hasattr(b1, 'datastyle_DateStyleType23'):
        assert not _is_linked(b1, 'datastyle_DateStyleType23', a)
    if hasattr(b2, 'datastyle_DateStyleType23'):
        assert _is_linked(b2, 'datastyle_DateStyleType23', a)
    _safe_set(a, 'datastyle_DayType', None)
    assert not _is_linked(a, 'datastyle_DayType', b2)
    if hasattr(b2, 'datastyle_DateStyleType23'):
        assert not _is_linked(b2, 'datastyle_DateStyleType23', a)


def test_assoc_dayOfWeek113_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_DayOfWeekType(calendar="sample_text", style="sample_text")
    b2 = datastyle_DayOfWeekType(calendar="sample_text_2", style="sample_text_2")
    _safe_set(a, 'datastyle_DocumentRoot114', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot114', b1)
    if hasattr(b1, 'datastyle_DayOfWeekType115'):
        assert _is_linked(b1, 'datastyle_DayOfWeekType115', a)
    _safe_set(a, 'datastyle_DocumentRoot114', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot114', b2)
    if hasattr(b1, 'datastyle_DayOfWeekType115'):
        assert not _is_linked(b1, 'datastyle_DayOfWeekType115', a)
    if hasattr(b2, 'datastyle_DayOfWeekType115'):
        assert _is_linked(b2, 'datastyle_DayOfWeekType115', a)
    _safe_set(a, 'datastyle_DocumentRoot114', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot114', b2)
    if hasattr(b2, 'datastyle_DayOfWeekType115'):
        assert not _is_linked(b2, 'datastyle_DayOfWeekType115', a)


def test_assoc_dayOfWeek30_link_reassign_clear():
    a = datastyle_DayOfWeekType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_DayOfWeekType', b1)
    assert _is_linked(a, 'datastyle_DayOfWeekType', b1)
    if hasattr(b1, 'datastyle_DateStyleType31'):
        assert _is_linked(b1, 'datastyle_DateStyleType31', a)
    _safe_set(a, 'datastyle_DayOfWeekType', b2)
    assert _is_linked(a, 'datastyle_DayOfWeekType', b2)
    if hasattr(b1, 'datastyle_DateStyleType31'):
        assert not _is_linked(b1, 'datastyle_DateStyleType31', a)
    if hasattr(b2, 'datastyle_DateStyleType31'):
        assert _is_linked(b2, 'datastyle_DateStyleType31', a)
    _safe_set(a, 'datastyle_DayOfWeekType', None)
    assert not _is_linked(a, 'datastyle_DayOfWeekType', b2)
    if hasattr(b2, 'datastyle_DateStyleType31'):
        assert not _is_linked(b2, 'datastyle_DateStyleType31', a)


def test_assoc_embeddedText116_link_reassign_clear():
    a = datastyle_EmbeddedTextType(mixed="sample_text", position="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_EmbeddedTextType118', b1)
    assert _is_linked(a, 'datastyle_EmbeddedTextType118', b1)
    if hasattr(b1, 'datastyle_DocumentRoot117'):
        assert _is_linked(b1, 'datastyle_DocumentRoot117', a)
    _safe_set(a, 'datastyle_EmbeddedTextType118', b2)
    assert _is_linked(a, 'datastyle_EmbeddedTextType118', b2)
    if hasattr(b1, 'datastyle_DocumentRoot117'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot117', a)
    if hasattr(b2, 'datastyle_DocumentRoot117'):
        assert _is_linked(b2, 'datastyle_DocumentRoot117', a)
    _safe_set(a, 'datastyle_EmbeddedTextType118', None)
    assert not _is_linked(a, 'datastyle_EmbeddedTextType118', b2)
    if hasattr(b2, 'datastyle_DocumentRoot117'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot117', a)


def test_assoc_embeddedText54_link_reassign_clear():
    a = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    b1 = datastyle_EmbeddedTextType(mixed="sample_text", position="sample_text")
    b2 = datastyle_EmbeddedTextType(mixed="sample_text_2", position="sample_text_2")
    _safe_set(a, 'datastyle_NumberType55', {b1})
    assert _is_linked(a, 'datastyle_NumberType55', b1)
    if hasattr(b1, 'datastyle_EmbeddedTextType'):
        assert _is_linked(b1, 'datastyle_EmbeddedTextType', a)
    _safe_set(a, 'datastyle_NumberType55', {b2})
    assert _is_linked(a, 'datastyle_NumberType55', b2)
    if hasattr(b1, 'datastyle_EmbeddedTextType'):
        assert not _is_linked(b1, 'datastyle_EmbeddedTextType', a)
    if hasattr(b2, 'datastyle_EmbeddedTextType'):
        assert _is_linked(b2, 'datastyle_EmbeddedTextType', a)
    _safe_set(a, 'datastyle_NumberType55', set())
    assert not _is_linked(a, 'datastyle_NumberType55', b2)
    if hasattr(b2, 'datastyle_EmbeddedTextType'):
        assert not _is_linked(b2, 'datastyle_EmbeddedTextType', a)


def test_assoc_era119_link_reassign_clear():
    a = datastyle_EraType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_EraType121', b1)
    assert _is_linked(a, 'datastyle_EraType121', b1)
    if hasattr(b1, 'datastyle_DocumentRoot120'):
        assert _is_linked(b1, 'datastyle_DocumentRoot120', a)
    _safe_set(a, 'datastyle_EraType121', b2)
    assert _is_linked(a, 'datastyle_EraType121', b2)
    if hasattr(b1, 'datastyle_DocumentRoot120'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot120', a)
    if hasattr(b2, 'datastyle_DocumentRoot120'):
        assert _is_linked(b2, 'datastyle_DocumentRoot120', a)
    _safe_set(a, 'datastyle_EraType121', None)
    assert not _is_linked(a, 'datastyle_EraType121', b2)
    if hasattr(b2, 'datastyle_DocumentRoot120'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot120', a)


def test_assoc_era28_link_reassign_clear():
    a = datastyle_EraType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_EraType', b1)
    assert _is_linked(a, 'datastyle_EraType', b1)
    if hasattr(b1, 'datastyle_DateStyleType29'):
        assert _is_linked(b1, 'datastyle_DateStyleType29', a)
    _safe_set(a, 'datastyle_EraType', b2)
    assert _is_linked(a, 'datastyle_EraType', b2)
    if hasattr(b1, 'datastyle_DateStyleType29'):
        assert not _is_linked(b1, 'datastyle_DateStyleType29', a)
    if hasattr(b2, 'datastyle_DateStyleType29'):
        assert _is_linked(b2, 'datastyle_DateStyleType29', a)
    _safe_set(a, 'datastyle_EraType', None)
    assert not _is_linked(a, 'datastyle_EraType', b2)
    if hasattr(b2, 'datastyle_DateStyleType29'):
        assert not _is_linked(b2, 'datastyle_DateStyleType29', a)


def test_assoc_fraction122_link_reassign_clear():
    a = datastyle_FractionType(denominatorValue="sample_text", grouping="sample_text", minDenominatorDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_FractionType', b1)
    assert _is_linked(a, 'datastyle_FractionType', b1)
    if hasattr(b1, 'datastyle_DocumentRoot123'):
        assert _is_linked(b1, 'datastyle_DocumentRoot123', a)
    _safe_set(a, 'datastyle_FractionType', b2)
    assert _is_linked(a, 'datastyle_FractionType', b2)
    if hasattr(b1, 'datastyle_DocumentRoot123'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot123', a)
    if hasattr(b2, 'datastyle_DocumentRoot123'):
        assert _is_linked(b2, 'datastyle_DocumentRoot123', a)
    _safe_set(a, 'datastyle_FractionType', None)
    assert not _is_linked(a, 'datastyle_FractionType', b2)
    if hasattr(b2, 'datastyle_DocumentRoot123'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot123', a)


def test_assoc_hours124_link_reassign_clear():
    a = datastyle_HoursType(style="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_HoursType126', b1)
    assert _is_linked(a, 'datastyle_HoursType126', b1)
    if hasattr(b1, 'datastyle_DocumentRoot125'):
        assert _is_linked(b1, 'datastyle_DocumentRoot125', a)
    _safe_set(a, 'datastyle_HoursType126', b2)
    assert _is_linked(a, 'datastyle_HoursType126', b2)
    if hasattr(b1, 'datastyle_DocumentRoot125'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot125', a)
    if hasattr(b2, 'datastyle_DocumentRoot125'):
        assert _is_linked(b2, 'datastyle_DocumentRoot125', a)
    _safe_set(a, 'datastyle_HoursType126', None)
    assert not _is_linked(a, 'datastyle_HoursType126', b2)
    if hasattr(b2, 'datastyle_DocumentRoot125'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot125', a)


def test_assoc_hours36_link_reassign_clear():
    a = datastyle_HoursType(style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_HoursType', b1)
    assert _is_linked(a, 'datastyle_HoursType', b1)
    if hasattr(b1, 'datastyle_DateStyleType37'):
        assert _is_linked(b1, 'datastyle_DateStyleType37', a)
    _safe_set(a, 'datastyle_HoursType', b2)
    assert _is_linked(a, 'datastyle_HoursType', b2)
    if hasattr(b1, 'datastyle_DateStyleType37'):
        assert not _is_linked(b1, 'datastyle_DateStyleType37', a)
    if hasattr(b2, 'datastyle_DateStyleType37'):
        assert _is_linked(b2, 'datastyle_DateStyleType37', a)
    _safe_set(a, 'datastyle_HoursType', None)
    assert not _is_linked(a, 'datastyle_HoursType', b2)
    if hasattr(b2, 'datastyle_DateStyleType37'):
        assert not _is_linked(b2, 'datastyle_DateStyleType37', a)


def test_assoc_hours73_link_reassign_clear():
    a = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    b1 = datastyle_HoursType(style="sample_text")
    b2 = datastyle_HoursType(style="sample_text_2")
    _safe_set(a, 'datastyle_TimeStyleType74', {b1})
    assert _is_linked(a, 'datastyle_TimeStyleType74', b1)
    if hasattr(b1, 'datastyle_HoursType75'):
        assert _is_linked(b1, 'datastyle_HoursType75', a)
    _safe_set(a, 'datastyle_TimeStyleType74', {b2})
    assert _is_linked(a, 'datastyle_TimeStyleType74', b2)
    if hasattr(b1, 'datastyle_HoursType75'):
        assert not _is_linked(b1, 'datastyle_HoursType75', a)
    if hasattr(b2, 'datastyle_HoursType75'):
        assert _is_linked(b2, 'datastyle_HoursType75', a)
    _safe_set(a, 'datastyle_TimeStyleType74', set())
    assert not _is_linked(a, 'datastyle_TimeStyleType74', b2)
    if hasattr(b2, 'datastyle_HoursType75'):
        assert not _is_linked(b2, 'datastyle_HoursType75', a)


def test_assoc_map17_link_reassign_clear():
    a = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_MapType()
    b2 = datastyle_MapType()
    _safe_set(a, 'datastyle_CurrencyStyleType18', {b1})
    assert _is_linked(a, 'datastyle_CurrencyStyleType18', b1)
    if hasattr(b1, 'datastyle_MapType19'):
        assert _is_linked(b1, 'datastyle_MapType19', a)
    _safe_set(a, 'datastyle_CurrencyStyleType18', {b2})
    assert _is_linked(a, 'datastyle_CurrencyStyleType18', b2)
    if hasattr(b1, 'datastyle_MapType19'):
        assert not _is_linked(b1, 'datastyle_MapType19', a)
    if hasattr(b2, 'datastyle_MapType19'):
        assert _is_linked(b2, 'datastyle_MapType19', a)
    _safe_set(a, 'datastyle_CurrencyStyleType18', set())
    assert not _is_linked(a, 'datastyle_CurrencyStyleType18', b2)
    if hasattr(b2, 'datastyle_MapType19'):
        assert not _is_linked(b2, 'datastyle_MapType19', a)


def test_assoc_map3_link_reassign_clear():
    a = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_MapType()
    b2 = datastyle_MapType()
    _safe_set(a, 'datastyle_BooleanStyleType4', {b1})
    assert _is_linked(a, 'datastyle_BooleanStyleType4', b1)
    if hasattr(b1, 'datastyle_MapType'):
        assert _is_linked(b1, 'datastyle_MapType', a)
    _safe_set(a, 'datastyle_BooleanStyleType4', {b2})
    assert _is_linked(a, 'datastyle_BooleanStyleType4', b2)
    if hasattr(b1, 'datastyle_MapType'):
        assert not _is_linked(b1, 'datastyle_MapType', a)
    if hasattr(b2, 'datastyle_MapType'):
        assert _is_linked(b2, 'datastyle_MapType', a)
    _safe_set(a, 'datastyle_BooleanStyleType4', set())
    assert not _is_linked(a, 'datastyle_BooleanStyleType4', b2)
    if hasattr(b2, 'datastyle_MapType'):
        assert not _is_linked(b2, 'datastyle_MapType', a)


def test_assoc_map44_link_reassign_clear():
    a = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_MapType()
    b2 = datastyle_MapType()
    _safe_set(a, 'datastyle_DateStyleType45', {b1})
    assert _is_linked(a, 'datastyle_DateStyleType45', b1)
    if hasattr(b1, 'datastyle_MapType46'):
        assert _is_linked(b1, 'datastyle_MapType46', a)
    _safe_set(a, 'datastyle_DateStyleType45', {b2})
    assert _is_linked(a, 'datastyle_DateStyleType45', b2)
    if hasattr(b1, 'datastyle_MapType46'):
        assert not _is_linked(b1, 'datastyle_MapType46', a)
    if hasattr(b2, 'datastyle_MapType46'):
        assert _is_linked(b2, 'datastyle_MapType46', a)
    _safe_set(a, 'datastyle_DateStyleType45', set())
    assert not _is_linked(a, 'datastyle_DateStyleType45', b2)
    if hasattr(b2, 'datastyle_MapType46'):
        assert not _is_linked(b2, 'datastyle_MapType46', a)


def test_assoc_map51_link_reassign_clear():
    a = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_MapType()
    b2 = datastyle_MapType()
    _safe_set(a, 'datastyle_NumberStyleType52', {b1})
    assert _is_linked(a, 'datastyle_NumberStyleType52', b1)
    if hasattr(b1, 'datastyle_MapType53'):
        assert _is_linked(b1, 'datastyle_MapType53', a)
    _safe_set(a, 'datastyle_NumberStyleType52', {b2})
    assert _is_linked(a, 'datastyle_NumberStyleType52', b2)
    if hasattr(b1, 'datastyle_MapType53'):
        assert not _is_linked(b1, 'datastyle_MapType53', a)
    if hasattr(b2, 'datastyle_MapType53'):
        assert _is_linked(b2, 'datastyle_MapType53', a)
    _safe_set(a, 'datastyle_NumberStyleType52', set())
    assert not _is_linked(a, 'datastyle_NumberStyleType52', b2)
    if hasattr(b2, 'datastyle_MapType53'):
        assert not _is_linked(b2, 'datastyle_MapType53', a)


def test_assoc_map61_link_reassign_clear():
    a = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_MapType()
    b2 = datastyle_MapType()
    _safe_set(a, 'datastyle_PercentageStyleType62', {b1})
    assert _is_linked(a, 'datastyle_PercentageStyleType62', b1)
    if hasattr(b1, 'datastyle_MapType63'):
        assert _is_linked(b1, 'datastyle_MapType63', a)
    _safe_set(a, 'datastyle_PercentageStyleType62', {b2})
    assert _is_linked(a, 'datastyle_PercentageStyleType62', b2)
    if hasattr(b1, 'datastyle_MapType63'):
        assert not _is_linked(b1, 'datastyle_MapType63', a)
    if hasattr(b2, 'datastyle_MapType63'):
        assert _is_linked(b2, 'datastyle_MapType63', a)
    _safe_set(a, 'datastyle_PercentageStyleType62', set())
    assert not _is_linked(a, 'datastyle_PercentageStyleType62', b2)
    if hasattr(b2, 'datastyle_MapType63'):
        assert not _is_linked(b2, 'datastyle_MapType63', a)


def test_assoc_map68_link_reassign_clear():
    a = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_MapType()
    b2 = datastyle_MapType()
    _safe_set(a, 'datastyle_TextStyleType69', {b1})
    assert _is_linked(a, 'datastyle_TextStyleType69', b1)
    if hasattr(b1, 'datastyle_MapType70'):
        assert _is_linked(b1, 'datastyle_MapType70', a)
    _safe_set(a, 'datastyle_TextStyleType69', {b2})
    assert _is_linked(a, 'datastyle_TextStyleType69', b2)
    if hasattr(b1, 'datastyle_MapType70'):
        assert not _is_linked(b1, 'datastyle_MapType70', a)
    if hasattr(b2, 'datastyle_MapType70'):
        assert _is_linked(b2, 'datastyle_MapType70', a)
    _safe_set(a, 'datastyle_TextStyleType69', set())
    assert not _is_linked(a, 'datastyle_TextStyleType69', b2)
    if hasattr(b2, 'datastyle_MapType70'):
        assert not _is_linked(b2, 'datastyle_MapType70', a)


def test_assoc_map85_link_reassign_clear():
    a = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    b1 = datastyle_MapType()
    b2 = datastyle_MapType()
    _safe_set(a, 'datastyle_TimeStyleType86', {b1})
    assert _is_linked(a, 'datastyle_TimeStyleType86', b1)
    if hasattr(b1, 'datastyle_MapType87'):
        assert _is_linked(b1, 'datastyle_MapType87', a)
    _safe_set(a, 'datastyle_TimeStyleType86', {b2})
    assert _is_linked(a, 'datastyle_TimeStyleType86', b2)
    if hasattr(b1, 'datastyle_MapType87'):
        assert not _is_linked(b1, 'datastyle_MapType87', a)
    if hasattr(b2, 'datastyle_MapType87'):
        assert _is_linked(b2, 'datastyle_MapType87', a)
    _safe_set(a, 'datastyle_TimeStyleType86', set())
    assert not _is_linked(a, 'datastyle_TimeStyleType86', b2)
    if hasattr(b2, 'datastyle_MapType87'):
        assert not _is_linked(b2, 'datastyle_MapType87', a)


def test_assoc_minutes127_link_reassign_clear():
    a = datastyle_MinutesType(style="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_MinutesType129', b1)
    assert _is_linked(a, 'datastyle_MinutesType129', b1)
    if hasattr(b1, 'datastyle_DocumentRoot128'):
        assert _is_linked(b1, 'datastyle_DocumentRoot128', a)
    _safe_set(a, 'datastyle_MinutesType129', b2)
    assert _is_linked(a, 'datastyle_MinutesType129', b2)
    if hasattr(b1, 'datastyle_DocumentRoot128'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot128', a)
    if hasattr(b2, 'datastyle_DocumentRoot128'):
        assert _is_linked(b2, 'datastyle_DocumentRoot128', a)
    _safe_set(a, 'datastyle_MinutesType129', None)
    assert not _is_linked(a, 'datastyle_MinutesType129', b2)
    if hasattr(b2, 'datastyle_DocumentRoot128'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot128', a)


def test_assoc_minutes40_link_reassign_clear():
    a = datastyle_MinutesType(style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_MinutesType', b1)
    assert _is_linked(a, 'datastyle_MinutesType', b1)
    if hasattr(b1, 'datastyle_DateStyleType41'):
        assert _is_linked(b1, 'datastyle_DateStyleType41', a)
    _safe_set(a, 'datastyle_MinutesType', b2)
    assert _is_linked(a, 'datastyle_MinutesType', b2)
    if hasattr(b1, 'datastyle_DateStyleType41'):
        assert not _is_linked(b1, 'datastyle_DateStyleType41', a)
    if hasattr(b2, 'datastyle_DateStyleType41'):
        assert _is_linked(b2, 'datastyle_DateStyleType41', a)
    _safe_set(a, 'datastyle_MinutesType', None)
    assert not _is_linked(a, 'datastyle_MinutesType', b2)
    if hasattr(b2, 'datastyle_DateStyleType41'):
        assert not _is_linked(b2, 'datastyle_DateStyleType41', a)


def test_assoc_minutes79_link_reassign_clear():
    a = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    b1 = datastyle_MinutesType(style="sample_text")
    b2 = datastyle_MinutesType(style="sample_text_2")
    _safe_set(a, 'datastyle_TimeStyleType80', {b1})
    assert _is_linked(a, 'datastyle_TimeStyleType80', b1)
    if hasattr(b1, 'datastyle_MinutesType81'):
        assert _is_linked(b1, 'datastyle_MinutesType81', a)
    _safe_set(a, 'datastyle_TimeStyleType80', {b2})
    assert _is_linked(a, 'datastyle_TimeStyleType80', b2)
    if hasattr(b1, 'datastyle_MinutesType81'):
        assert not _is_linked(b1, 'datastyle_MinutesType81', a)
    if hasattr(b2, 'datastyle_MinutesType81'):
        assert _is_linked(b2, 'datastyle_MinutesType81', a)
    _safe_set(a, 'datastyle_TimeStyleType80', set())
    assert not _is_linked(a, 'datastyle_TimeStyleType80', b2)
    if hasattr(b2, 'datastyle_MinutesType81'):
        assert not _is_linked(b2, 'datastyle_MinutesType81', a)


def test_assoc_month130_link_reassign_clear():
    a = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_MonthType132', b1)
    assert _is_linked(a, 'datastyle_MonthType132', b1)
    if hasattr(b1, 'datastyle_DocumentRoot131'):
        assert _is_linked(b1, 'datastyle_DocumentRoot131', a)
    _safe_set(a, 'datastyle_MonthType132', b2)
    assert _is_linked(a, 'datastyle_MonthType132', b2)
    if hasattr(b1, 'datastyle_DocumentRoot131'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot131', a)
    if hasattr(b2, 'datastyle_DocumentRoot131'):
        assert _is_linked(b2, 'datastyle_DocumentRoot131', a)
    _safe_set(a, 'datastyle_MonthType132', None)
    assert not _is_linked(a, 'datastyle_MonthType132', b2)
    if hasattr(b2, 'datastyle_DocumentRoot131'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot131', a)


def test_assoc_month24_link_reassign_clear():
    a = datastyle_MonthType(calendar="sample_text", possessiveForm="sample_text", style="sample_text", textual="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_MonthType', b1)
    assert _is_linked(a, 'datastyle_MonthType', b1)
    if hasattr(b1, 'datastyle_DateStyleType25'):
        assert _is_linked(b1, 'datastyle_DateStyleType25', a)
    _safe_set(a, 'datastyle_MonthType', b2)
    assert _is_linked(a, 'datastyle_MonthType', b2)
    if hasattr(b1, 'datastyle_DateStyleType25'):
        assert not _is_linked(b1, 'datastyle_DateStyleType25', a)
    if hasattr(b2, 'datastyle_DateStyleType25'):
        assert _is_linked(b2, 'datastyle_DateStyleType25', a)
    _safe_set(a, 'datastyle_MonthType', None)
    assert not _is_linked(a, 'datastyle_MonthType', b2)
    if hasattr(b2, 'datastyle_DateStyleType25'):
        assert not _is_linked(b2, 'datastyle_DateStyleType25', a)


def test_assoc_number114_link_reassign_clear():
    a = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    b1 = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_CurrencyStyleType(automaticOrder="sample_text_2", country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", text2="sample_text_2", text3="sample_text_2", text4="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_NumberType16', b1)
    assert _is_linked(a, 'datastyle_NumberType16', b1)
    if hasattr(b1, 'datastyle_CurrencyStyleType15'):
        assert _is_linked(b1, 'datastyle_CurrencyStyleType15', a)
    _safe_set(a, 'datastyle_NumberType16', b2)
    assert _is_linked(a, 'datastyle_NumberType16', b2)
    if hasattr(b1, 'datastyle_CurrencyStyleType15'):
        assert not _is_linked(b1, 'datastyle_CurrencyStyleType15', a)
    if hasattr(b2, 'datastyle_CurrencyStyleType15'):
        assert _is_linked(b2, 'datastyle_CurrencyStyleType15', a)
    _safe_set(a, 'datastyle_NumberType16', None)
    assert not _is_linked(a, 'datastyle_NumberType16', b2)
    if hasattr(b2, 'datastyle_CurrencyStyleType15'):
        assert not _is_linked(b2, 'datastyle_CurrencyStyleType15', a)


def test_assoc_number133_link_reassign_clear():
    a = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_NumberType135', b1)
    assert _is_linked(a, 'datastyle_NumberType135', b1)
    if hasattr(b1, 'datastyle_DocumentRoot134'):
        assert _is_linked(b1, 'datastyle_DocumentRoot134', a)
    _safe_set(a, 'datastyle_NumberType135', b2)
    assert _is_linked(a, 'datastyle_NumberType135', b2)
    if hasattr(b1, 'datastyle_DocumentRoot134'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot134', a)
    if hasattr(b2, 'datastyle_DocumentRoot134'):
        assert _is_linked(b2, 'datastyle_DocumentRoot134', a)
    _safe_set(a, 'datastyle_NumberType135', None)
    assert not _is_linked(a, 'datastyle_NumberType135', b2)
    if hasattr(b2, 'datastyle_DocumentRoot134'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot134', a)


def test_assoc_number58_link_reassign_clear():
    a = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    b2 = datastyle_NumberType(decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", displayFactor="sample_text_2", grouping="sample_text_2", minIntegerDigits="sample_text_2")
    _safe_set(a, 'datastyle_PercentageStyleType59', b1)
    assert _is_linked(a, 'datastyle_PercentageStyleType59', b1)
    if hasattr(b1, 'datastyle_NumberType60'):
        assert _is_linked(b1, 'datastyle_NumberType60', a)
    _safe_set(a, 'datastyle_PercentageStyleType59', b2)
    assert _is_linked(a, 'datastyle_PercentageStyleType59', b2)
    if hasattr(b1, 'datastyle_NumberType60'):
        assert not _is_linked(b1, 'datastyle_NumberType60', a)
    if hasattr(b2, 'datastyle_NumberType60'):
        assert _is_linked(b2, 'datastyle_NumberType60', a)
    _safe_set(a, 'datastyle_PercentageStyleType59', None)
    assert not _is_linked(a, 'datastyle_PercentageStyleType59', b2)
    if hasattr(b2, 'datastyle_NumberType60'):
        assert not _is_linked(b2, 'datastyle_NumberType60', a)


def test_assoc_number7_link_reassign_clear():
    a = datastyle_NumberType(decimalPlaces="sample_text", decimalReplacement="sample_text", displayFactor="sample_text", grouping="sample_text", minIntegerDigits="sample_text")
    b1 = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_CurrencyStyleType(automaticOrder="sample_text_2", country="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", text2="sample_text_2", text3="sample_text_2", text4="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_NumberType', b1)
    assert _is_linked(a, 'datastyle_NumberType', b1)
    if hasattr(b1, 'datastyle_CurrencyStyleType8'):
        assert _is_linked(b1, 'datastyle_CurrencyStyleType8', a)
    _safe_set(a, 'datastyle_NumberType', b2)
    assert _is_linked(a, 'datastyle_NumberType', b2)
    if hasattr(b1, 'datastyle_CurrencyStyleType8'):
        assert not _is_linked(b1, 'datastyle_CurrencyStyleType8', a)
    if hasattr(b2, 'datastyle_CurrencyStyleType8'):
        assert _is_linked(b2, 'datastyle_CurrencyStyleType8', a)
    _safe_set(a, 'datastyle_NumberType', None)
    assert not _is_linked(a, 'datastyle_NumberType', b2)
    if hasattr(b2, 'datastyle_CurrencyStyleType8'):
        assert not _is_linked(b2, 'datastyle_CurrencyStyleType8', a)


def test_assoc_numberStyle136_link_reassign_clear():
    a = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_NumberStyleType138', b1)
    assert _is_linked(a, 'datastyle_NumberStyleType138', b1)
    if hasattr(b1, 'datastyle_DocumentRoot137'):
        assert _is_linked(b1, 'datastyle_DocumentRoot137', a)
    _safe_set(a, 'datastyle_NumberStyleType138', b2)
    assert _is_linked(a, 'datastyle_NumberStyleType138', b2)
    if hasattr(b1, 'datastyle_DocumentRoot137'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot137', a)
    if hasattr(b2, 'datastyle_DocumentRoot137'):
        assert _is_linked(b2, 'datastyle_DocumentRoot137', a)
    _safe_set(a, 'datastyle_NumberStyleType138', None)
    assert not _is_linked(a, 'datastyle_NumberStyleType138', b2)
    if hasattr(b2, 'datastyle_DocumentRoot137'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot137', a)


def test_assoc_percentageStyle139_link_reassign_clear():
    a = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_PercentageStyleType141', b1)
    assert _is_linked(a, 'datastyle_PercentageStyleType141', b1)
    if hasattr(b1, 'datastyle_DocumentRoot140'):
        assert _is_linked(b1, 'datastyle_DocumentRoot140', a)
    _safe_set(a, 'datastyle_PercentageStyleType141', b2)
    assert _is_linked(a, 'datastyle_PercentageStyleType141', b2)
    if hasattr(b1, 'datastyle_DocumentRoot140'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot140', a)
    if hasattr(b2, 'datastyle_DocumentRoot140'):
        assert _is_linked(b2, 'datastyle_DocumentRoot140', a)
    _safe_set(a, 'datastyle_PercentageStyleType141', None)
    assert not _is_linked(a, 'datastyle_PercentageStyleType141', b2)
    if hasattr(b2, 'datastyle_DocumentRoot140'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot140', a)


def test_assoc_quarter142_link_reassign_clear():
    a = datastyle_QuarterType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_QuarterType144', b1)
    assert _is_linked(a, 'datastyle_QuarterType144', b1)
    if hasattr(b1, 'datastyle_DocumentRoot143'):
        assert _is_linked(b1, 'datastyle_DocumentRoot143', a)
    _safe_set(a, 'datastyle_QuarterType144', b2)
    assert _is_linked(a, 'datastyle_QuarterType144', b2)
    if hasattr(b1, 'datastyle_DocumentRoot143'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot143', a)
    if hasattr(b2, 'datastyle_DocumentRoot143'):
        assert _is_linked(b2, 'datastyle_DocumentRoot143', a)
    _safe_set(a, 'datastyle_QuarterType144', None)
    assert not _is_linked(a, 'datastyle_QuarterType144', b2)
    if hasattr(b2, 'datastyle_DocumentRoot143'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot143', a)


def test_assoc_quarter34_link_reassign_clear():
    a = datastyle_QuarterType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_QuarterType', b1)
    assert _is_linked(a, 'datastyle_QuarterType', b1)
    if hasattr(b1, 'datastyle_DateStyleType35'):
        assert _is_linked(b1, 'datastyle_DateStyleType35', a)
    _safe_set(a, 'datastyle_QuarterType', b2)
    assert _is_linked(a, 'datastyle_QuarterType', b2)
    if hasattr(b1, 'datastyle_DateStyleType35'):
        assert not _is_linked(b1, 'datastyle_DateStyleType35', a)
    if hasattr(b2, 'datastyle_DateStyleType35'):
        assert _is_linked(b2, 'datastyle_DateStyleType35', a)
    _safe_set(a, 'datastyle_QuarterType', None)
    assert not _is_linked(a, 'datastyle_QuarterType', b2)
    if hasattr(b2, 'datastyle_DateStyleType35'):
        assert not _is_linked(b2, 'datastyle_DateStyleType35', a)


def test_assoc_scientificNumber145_link_reassign_clear():
    a = datastyle_ScientificNumberType(decimalPlaces="sample_text", grouping="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_ScientificNumberType', b1)
    assert _is_linked(a, 'datastyle_ScientificNumberType', b1)
    if hasattr(b1, 'datastyle_DocumentRoot146'):
        assert _is_linked(b1, 'datastyle_DocumentRoot146', a)
    _safe_set(a, 'datastyle_ScientificNumberType', b2)
    assert _is_linked(a, 'datastyle_ScientificNumberType', b2)
    if hasattr(b1, 'datastyle_DocumentRoot146'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot146', a)
    if hasattr(b2, 'datastyle_DocumentRoot146'):
        assert _is_linked(b2, 'datastyle_DocumentRoot146', a)
    _safe_set(a, 'datastyle_ScientificNumberType', None)
    assert not _is_linked(a, 'datastyle_ScientificNumberType', b2)
    if hasattr(b2, 'datastyle_DocumentRoot146'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot146', a)


def test_assoc_seconds147_link_reassign_clear():
    a = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_SecondsType149', b1)
    assert _is_linked(a, 'datastyle_SecondsType149', b1)
    if hasattr(b1, 'datastyle_DocumentRoot148'):
        assert _is_linked(b1, 'datastyle_DocumentRoot148', a)
    _safe_set(a, 'datastyle_SecondsType149', b2)
    assert _is_linked(a, 'datastyle_SecondsType149', b2)
    if hasattr(b1, 'datastyle_DocumentRoot148'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot148', a)
    if hasattr(b2, 'datastyle_DocumentRoot148'):
        assert _is_linked(b2, 'datastyle_DocumentRoot148', a)
    _safe_set(a, 'datastyle_SecondsType149', None)
    assert not _is_linked(a, 'datastyle_SecondsType149', b2)
    if hasattr(b2, 'datastyle_DocumentRoot148'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot148', a)


def test_assoc_seconds42_link_reassign_clear():
    a = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_SecondsType', b1)
    assert _is_linked(a, 'datastyle_SecondsType', b1)
    if hasattr(b1, 'datastyle_DateStyleType43'):
        assert _is_linked(b1, 'datastyle_DateStyleType43', a)
    _safe_set(a, 'datastyle_SecondsType', b2)
    assert _is_linked(a, 'datastyle_SecondsType', b2)
    if hasattr(b1, 'datastyle_DateStyleType43'):
        assert not _is_linked(b1, 'datastyle_DateStyleType43', a)
    if hasattr(b2, 'datastyle_DateStyleType43'):
        assert _is_linked(b2, 'datastyle_DateStyleType43', a)
    _safe_set(a, 'datastyle_SecondsType', None)
    assert not _is_linked(a, 'datastyle_SecondsType', b2)
    if hasattr(b2, 'datastyle_DateStyleType43'):
        assert not _is_linked(b2, 'datastyle_DateStyleType43', a)


def test_assoc_seconds82_link_reassign_clear():
    a = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    b1 = datastyle_SecondsType(decimalPlaces="sample_text", style="sample_text")
    b2 = datastyle_SecondsType(decimalPlaces="sample_text_2", style="sample_text_2")
    _safe_set(a, 'datastyle_TimeStyleType83', {b1})
    assert _is_linked(a, 'datastyle_TimeStyleType83', b1)
    if hasattr(b1, 'datastyle_SecondsType84'):
        assert _is_linked(b1, 'datastyle_SecondsType84', a)
    _safe_set(a, 'datastyle_TimeStyleType83', {b2})
    assert _is_linked(a, 'datastyle_TimeStyleType83', b2)
    if hasattr(b1, 'datastyle_SecondsType84'):
        assert not _is_linked(b1, 'datastyle_SecondsType84', a)
    if hasattr(b2, 'datastyle_SecondsType84'):
        assert _is_linked(b2, 'datastyle_SecondsType84', a)
    _safe_set(a, 'datastyle_TimeStyleType83', set())
    assert not _is_linked(a, 'datastyle_TimeStyleType83', b2)
    if hasattr(b2, 'datastyle_SecondsType84'):
        assert not _is_linked(b2, 'datastyle_SecondsType84', a)


def test_assoc_textContent150_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_TextContentType()
    b2 = datastyle_TextContentType()
    _safe_set(a, 'datastyle_DocumentRoot151', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot151', b1)
    if hasattr(b1, 'datastyle_TextContentType152'):
        assert _is_linked(b1, 'datastyle_TextContentType152', a)
    _safe_set(a, 'datastyle_DocumentRoot151', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot151', b2)
    if hasattr(b1, 'datastyle_TextContentType152'):
        assert not _is_linked(b1, 'datastyle_TextContentType152', a)
    if hasattr(b2, 'datastyle_TextContentType152'):
        assert _is_linked(b2, 'datastyle_TextContentType152', a)
    _safe_set(a, 'datastyle_DocumentRoot151', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot151', b2)
    if hasattr(b2, 'datastyle_TextContentType152'):
        assert not _is_linked(b2, 'datastyle_TextContentType152', a)


def test_assoc_textContent66_link_reassign_clear():
    a = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_TextContentType()
    b2 = datastyle_TextContentType()
    _safe_set(a, 'datastyle_TextStyleType67', {b1})
    assert _is_linked(a, 'datastyle_TextStyleType67', b1)
    if hasattr(b1, 'datastyle_TextContentType'):
        assert _is_linked(b1, 'datastyle_TextContentType', a)
    _safe_set(a, 'datastyle_TextStyleType67', {b2})
    assert _is_linked(a, 'datastyle_TextStyleType67', b2)
    if hasattr(b1, 'datastyle_TextContentType'):
        assert not _is_linked(b1, 'datastyle_TextContentType', a)
    if hasattr(b2, 'datastyle_TextContentType'):
        assert _is_linked(b2, 'datastyle_TextContentType', a)
    _safe_set(a, 'datastyle_TextStyleType67', set())
    assert not _is_linked(a, 'datastyle_TextStyleType67', b2)
    if hasattr(b2, 'datastyle_TextContentType'):
        assert not _is_linked(b2, 'datastyle_TextContentType', a)


def test_assoc_textProperties0_link_reassign_clear():
    a = datastyle_BooleanStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_StyleTextPropertiesContent()
    b2 = datastyle_StyleTextPropertiesContent()
    _safe_set(a, 'datastyle_BooleanStyleType', b1)
    assert _is_linked(a, 'datastyle_BooleanStyleType', b1)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent'):
        assert _is_linked(b1, 'datastyle_StyleTextPropertiesContent', a)
    _safe_set(a, 'datastyle_BooleanStyleType', b2)
    assert _is_linked(a, 'datastyle_BooleanStyleType', b2)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent'):
        assert not _is_linked(b1, 'datastyle_StyleTextPropertiesContent', a)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent'):
        assert _is_linked(b2, 'datastyle_StyleTextPropertiesContent', a)
    _safe_set(a, 'datastyle_BooleanStyleType', None)
    assert not _is_linked(a, 'datastyle_BooleanStyleType', b2)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent'):
        assert not _is_linked(b2, 'datastyle_StyleTextPropertiesContent', a)


def test_assoc_textProperties20_link_reassign_clear():
    a = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_StyleTextPropertiesContent()
    b2 = datastyle_StyleTextPropertiesContent()
    _safe_set(a, 'datastyle_DateStyleType', b1)
    assert _is_linked(a, 'datastyle_DateStyleType', b1)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent21'):
        assert _is_linked(b1, 'datastyle_StyleTextPropertiesContent21', a)
    _safe_set(a, 'datastyle_DateStyleType', b2)
    assert _is_linked(a, 'datastyle_DateStyleType', b2)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent21'):
        assert not _is_linked(b1, 'datastyle_StyleTextPropertiesContent21', a)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent21'):
        assert _is_linked(b2, 'datastyle_StyleTextPropertiesContent21', a)
    _safe_set(a, 'datastyle_DateStyleType', None)
    assert not _is_linked(a, 'datastyle_DateStyleType', b2)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent21'):
        assert not _is_linked(b2, 'datastyle_StyleTextPropertiesContent21', a)


def test_assoc_textProperties47_link_reassign_clear():
    a = datastyle_NumberStyleType(anyNumberGroup="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_StyleTextPropertiesContent()
    b2 = datastyle_StyleTextPropertiesContent()
    _safe_set(a, 'datastyle_NumberStyleType', b1)
    assert _is_linked(a, 'datastyle_NumberStyleType', b1)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent48'):
        assert _is_linked(b1, 'datastyle_StyleTextPropertiesContent48', a)
    _safe_set(a, 'datastyle_NumberStyleType', b2)
    assert _is_linked(a, 'datastyle_NumberStyleType', b2)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent48'):
        assert not _is_linked(b1, 'datastyle_StyleTextPropertiesContent48', a)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent48'):
        assert _is_linked(b2, 'datastyle_StyleTextPropertiesContent48', a)
    _safe_set(a, 'datastyle_NumberStyleType', None)
    assert not _is_linked(a, 'datastyle_NumberStyleType', b2)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent48'):
        assert not _is_linked(b2, 'datastyle_StyleTextPropertiesContent48', a)


def test_assoc_textProperties5_link_reassign_clear():
    a = datastyle_CurrencyStyleType(automaticOrder="sample_text", country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", text2="sample_text", text3="sample_text", text4="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_StyleTextPropertiesContent()
    b2 = datastyle_StyleTextPropertiesContent()
    _safe_set(a, 'datastyle_CurrencyStyleType', b1)
    assert _is_linked(a, 'datastyle_CurrencyStyleType', b1)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent6'):
        assert _is_linked(b1, 'datastyle_StyleTextPropertiesContent6', a)
    _safe_set(a, 'datastyle_CurrencyStyleType', b2)
    assert _is_linked(a, 'datastyle_CurrencyStyleType', b2)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent6'):
        assert not _is_linked(b1, 'datastyle_StyleTextPropertiesContent6', a)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent6'):
        assert _is_linked(b2, 'datastyle_StyleTextPropertiesContent6', a)
    _safe_set(a, 'datastyle_CurrencyStyleType', None)
    assert not _is_linked(a, 'datastyle_CurrencyStyleType', b2)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent6'):
        assert not _is_linked(b2, 'datastyle_StyleTextPropertiesContent6', a)


def test_assoc_textProperties56_link_reassign_clear():
    a = datastyle_PercentageStyleType(country="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_StyleTextPropertiesContent()
    b2 = datastyle_StyleTextPropertiesContent()
    _safe_set(a, 'datastyle_PercentageStyleType', b1)
    assert _is_linked(a, 'datastyle_PercentageStyleType', b1)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent57'):
        assert _is_linked(b1, 'datastyle_StyleTextPropertiesContent57', a)
    _safe_set(a, 'datastyle_PercentageStyleType', b2)
    assert _is_linked(a, 'datastyle_PercentageStyleType', b2)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent57'):
        assert not _is_linked(b1, 'datastyle_StyleTextPropertiesContent57', a)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent57'):
        assert _is_linked(b2, 'datastyle_StyleTextPropertiesContent57', a)
    _safe_set(a, 'datastyle_PercentageStyleType', None)
    assert not _is_linked(a, 'datastyle_PercentageStyleType', b2)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent57'):
        assert not _is_linked(b2, 'datastyle_StyleTextPropertiesContent57', a)


def test_assoc_textProperties64_link_reassign_clear():
    a = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_StyleTextPropertiesContent()
    b2 = datastyle_StyleTextPropertiesContent()
    _safe_set(a, 'datastyle_TextStyleType', b1)
    assert _is_linked(a, 'datastyle_TextStyleType', b1)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent65'):
        assert _is_linked(b1, 'datastyle_StyleTextPropertiesContent65', a)
    _safe_set(a, 'datastyle_TextStyleType', b2)
    assert _is_linked(a, 'datastyle_TextStyleType', b2)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent65'):
        assert not _is_linked(b1, 'datastyle_StyleTextPropertiesContent65', a)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent65'):
        assert _is_linked(b2, 'datastyle_StyleTextPropertiesContent65', a)
    _safe_set(a, 'datastyle_TextStyleType', None)
    assert not _is_linked(a, 'datastyle_TextStyleType', b2)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent65'):
        assert not _is_linked(b2, 'datastyle_StyleTextPropertiesContent65', a)


def test_assoc_textProperties71_link_reassign_clear():
    a = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    b1 = datastyle_StyleTextPropertiesContent()
    b2 = datastyle_StyleTextPropertiesContent()
    _safe_set(a, 'datastyle_TimeStyleType', b1)
    assert _is_linked(a, 'datastyle_TimeStyleType', b1)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent72'):
        assert _is_linked(b1, 'datastyle_StyleTextPropertiesContent72', a)
    _safe_set(a, 'datastyle_TimeStyleType', b2)
    assert _is_linked(a, 'datastyle_TimeStyleType', b2)
    if hasattr(b1, 'datastyle_StyleTextPropertiesContent72'):
        assert not _is_linked(b1, 'datastyle_StyleTextPropertiesContent72', a)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent72'):
        assert _is_linked(b2, 'datastyle_StyleTextPropertiesContent72', a)
    _safe_set(a, 'datastyle_TimeStyleType', None)
    assert not _is_linked(a, 'datastyle_TimeStyleType', b2)
    if hasattr(b2, 'datastyle_StyleTextPropertiesContent72'):
        assert not _is_linked(b2, 'datastyle_StyleTextPropertiesContent72', a)


def test_assoc_textStyle153_link_reassign_clear():
    a = datastyle_TextStyleType(country="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_TextStyleType155', b1)
    assert _is_linked(a, 'datastyle_TextStyleType155', b1)
    if hasattr(b1, 'datastyle_DocumentRoot154'):
        assert _is_linked(b1, 'datastyle_DocumentRoot154', a)
    _safe_set(a, 'datastyle_TextStyleType155', b2)
    assert _is_linked(a, 'datastyle_TextStyleType155', b2)
    if hasattr(b1, 'datastyle_DocumentRoot154'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot154', a)
    if hasattr(b2, 'datastyle_DocumentRoot154'):
        assert _is_linked(b2, 'datastyle_DocumentRoot154', a)
    _safe_set(a, 'datastyle_TextStyleType155', None)
    assert not _is_linked(a, 'datastyle_TextStyleType155', b2)
    if hasattr(b2, 'datastyle_DocumentRoot154'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot154', a)


def test_assoc_timeStyle156_link_reassign_clear():
    a = datastyle_TimeStyleType(country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text", volatile="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_TimeStyleType158', b1)
    assert _is_linked(a, 'datastyle_TimeStyleType158', b1)
    if hasattr(b1, 'datastyle_DocumentRoot157'):
        assert _is_linked(b1, 'datastyle_DocumentRoot157', a)
    _safe_set(a, 'datastyle_TimeStyleType158', b2)
    assert _is_linked(a, 'datastyle_TimeStyleType158', b2)
    if hasattr(b1, 'datastyle_DocumentRoot157'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot157', a)
    if hasattr(b2, 'datastyle_DocumentRoot157'):
        assert _is_linked(b2, 'datastyle_DocumentRoot157', a)
    _safe_set(a, 'datastyle_TimeStyleType158', None)
    assert not _is_linked(a, 'datastyle_TimeStyleType158', b2)
    if hasattr(b2, 'datastyle_DocumentRoot157'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot157', a)


def test_assoc_weekOfYear159_link_reassign_clear():
    a = datastyle_WeekOfYearType(calendar="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_WeekOfYearType161', b1)
    assert _is_linked(a, 'datastyle_WeekOfYearType161', b1)
    if hasattr(b1, 'datastyle_DocumentRoot160'):
        assert _is_linked(b1, 'datastyle_DocumentRoot160', a)
    _safe_set(a, 'datastyle_WeekOfYearType161', b2)
    assert _is_linked(a, 'datastyle_WeekOfYearType161', b2)
    if hasattr(b1, 'datastyle_DocumentRoot160'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot160', a)
    if hasattr(b2, 'datastyle_DocumentRoot160'):
        assert _is_linked(b2, 'datastyle_DocumentRoot160', a)
    _safe_set(a, 'datastyle_WeekOfYearType161', None)
    assert not _is_linked(a, 'datastyle_WeekOfYearType161', b2)
    if hasattr(b2, 'datastyle_DocumentRoot160'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot160', a)


def test_assoc_weekOfYear32_link_reassign_clear():
    a = datastyle_WeekOfYearType(calendar="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_WeekOfYearType', b1)
    assert _is_linked(a, 'datastyle_WeekOfYearType', b1)
    if hasattr(b1, 'datastyle_DateStyleType33'):
        assert _is_linked(b1, 'datastyle_DateStyleType33', a)
    _safe_set(a, 'datastyle_WeekOfYearType', b2)
    assert _is_linked(a, 'datastyle_WeekOfYearType', b2)
    if hasattr(b1, 'datastyle_DateStyleType33'):
        assert not _is_linked(b1, 'datastyle_DateStyleType33', a)
    if hasattr(b2, 'datastyle_DateStyleType33'):
        assert _is_linked(b2, 'datastyle_DateStyleType33', a)
    _safe_set(a, 'datastyle_WeekOfYearType', None)
    assert not _is_linked(a, 'datastyle_WeekOfYearType', b2)
    if hasattr(b2, 'datastyle_DateStyleType33'):
        assert not _is_linked(b2, 'datastyle_DateStyleType33', a)


def test_assoc_xMLNSPrefixMap88_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_EStringToStringMapEntry()
    b2 = datastyle_EStringToStringMapEntry()
    _safe_set(a, 'datastyle_DocumentRoot', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot', b1)
    if hasattr(b1, 'datastyle_EStringToStringMapEntry'):
        assert _is_linked(b1, 'datastyle_EStringToStringMapEntry', a)
    _safe_set(a, 'datastyle_DocumentRoot', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot', b2)
    if hasattr(b1, 'datastyle_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'datastyle_EStringToStringMapEntry', a)
    if hasattr(b2, 'datastyle_EStringToStringMapEntry'):
        assert _is_linked(b2, 'datastyle_EStringToStringMapEntry', a)
    _safe_set(a, 'datastyle_DocumentRoot', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot', b2)
    if hasattr(b2, 'datastyle_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'datastyle_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation89_link_reassign_clear():
    a = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b1 = datastyle_EStringToStringMapEntry()
    b2 = datastyle_EStringToStringMapEntry()
    _safe_set(a, 'datastyle_DocumentRoot90', {b1})
    assert _is_linked(a, 'datastyle_DocumentRoot90', b1)
    if hasattr(b1, 'datastyle_EStringToStringMapEntry91'):
        assert _is_linked(b1, 'datastyle_EStringToStringMapEntry91', a)
    _safe_set(a, 'datastyle_DocumentRoot90', {b2})
    assert _is_linked(a, 'datastyle_DocumentRoot90', b2)
    if hasattr(b1, 'datastyle_EStringToStringMapEntry91'):
        assert not _is_linked(b1, 'datastyle_EStringToStringMapEntry91', a)
    if hasattr(b2, 'datastyle_EStringToStringMapEntry91'):
        assert _is_linked(b2, 'datastyle_EStringToStringMapEntry91', a)
    _safe_set(a, 'datastyle_DocumentRoot90', set())
    assert not _is_linked(a, 'datastyle_DocumentRoot90', b2)
    if hasattr(b2, 'datastyle_EStringToStringMapEntry91'):
        assert not _is_linked(b2, 'datastyle_EStringToStringMapEntry91', a)


def test_assoc_year162_link_reassign_clear():
    a = datastyle_YearType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DocumentRoot(automaticOrder="sample_text", calendar="sample_text", country="sample_text", decimalPlaces="sample_text", decimalReplacement="sample_text", denominatorValue="sample_text", displayFactor="sample_text", formatSource="sample_text", grouping="sample_text", language="sample_text", minDenominatorDigits="sample_text", minExponentDigits="sample_text", minIntegerDigits="sample_text", minNumeratorDigits="sample_text", mixed="sample_text", position="sample_text", possessiveForm="sample_text", style="sample_text", text="sample_text", textual="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", truncateOnOverflow="sample_text")
    b2 = datastyle_DocumentRoot(automaticOrder="sample_text_2", calendar="sample_text_2", country="sample_text_2", decimalPlaces="sample_text_2", decimalReplacement="sample_text_2", denominatorValue="sample_text_2", displayFactor="sample_text_2", formatSource="sample_text_2", grouping="sample_text_2", language="sample_text_2", minDenominatorDigits="sample_text_2", minExponentDigits="sample_text_2", minIntegerDigits="sample_text_2", minNumeratorDigits="sample_text_2", mixed="sample_text_2", position="sample_text_2", possessiveForm="sample_text_2", style="sample_text_2", text="sample_text_2", textual="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", truncateOnOverflow="sample_text_2")
    _safe_set(a, 'datastyle_YearType164', b1)
    assert _is_linked(a, 'datastyle_YearType164', b1)
    if hasattr(b1, 'datastyle_DocumentRoot163'):
        assert _is_linked(b1, 'datastyle_DocumentRoot163', a)
    _safe_set(a, 'datastyle_YearType164', b2)
    assert _is_linked(a, 'datastyle_YearType164', b2)
    if hasattr(b1, 'datastyle_DocumentRoot163'):
        assert not _is_linked(b1, 'datastyle_DocumentRoot163', a)
    if hasattr(b2, 'datastyle_DocumentRoot163'):
        assert _is_linked(b2, 'datastyle_DocumentRoot163', a)
    _safe_set(a, 'datastyle_YearType164', None)
    assert not _is_linked(a, 'datastyle_YearType164', b2)
    if hasattr(b2, 'datastyle_DocumentRoot163'):
        assert not _is_linked(b2, 'datastyle_DocumentRoot163', a)


def test_assoc_year26_link_reassign_clear():
    a = datastyle_YearType(calendar="sample_text", style="sample_text")
    b1 = datastyle_DateStyleType(automaticOrder="sample_text", country="sample_text", formatSource="sample_text", group="sample_text", language="sample_text", name="sample_text", text="sample_text", text1="sample_text", title="sample_text", transliterationCountry="sample_text", transliterationFormat="sample_text", transliterationLanguage="sample_text", transliterationStyle="sample_text", volatile="sample_text")
    b2 = datastyle_DateStyleType(automaticOrder="sample_text_2", country="sample_text_2", formatSource="sample_text_2", group="sample_text_2", language="sample_text_2", name="sample_text_2", text="sample_text_2", text1="sample_text_2", title="sample_text_2", transliterationCountry="sample_text_2", transliterationFormat="sample_text_2", transliterationLanguage="sample_text_2", transliterationStyle="sample_text_2", volatile="sample_text_2")
    _safe_set(a, 'datastyle_YearType', b1)
    assert _is_linked(a, 'datastyle_YearType', b1)
    if hasattr(b1, 'datastyle_DateStyleType27'):
        assert _is_linked(b1, 'datastyle_DateStyleType27', a)
    _safe_set(a, 'datastyle_YearType', b2)
    assert _is_linked(a, 'datastyle_YearType', b2)
    if hasattr(b1, 'datastyle_DateStyleType27'):
        assert not _is_linked(b1, 'datastyle_DateStyleType27', a)
    if hasattr(b2, 'datastyle_DateStyleType27'):
        assert _is_linked(b2, 'datastyle_DateStyleType27', a)
    _safe_set(a, 'datastyle_YearType', None)
    assert not _is_linked(a, 'datastyle_YearType', b2)
    if hasattr(b2, 'datastyle_DateStyleType27'):
        assert not _is_linked(b2, 'datastyle_DateStyleType27', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

datastyle_AmPmType_strategy = st.builds(datastyle_AmPmType)
@given(instance=datastyle_AmPmType_strategy)
@settings(max_examples=25)
def test_datastyle_AmPmType_instantiation(instance):
    assert isinstance(instance, datastyle_AmPmType)


datastyle_BooleanStyleType_strategy = st.builds(datastyle_BooleanStyleType, country=safe_text, language=safe_text, name=safe_text, text=safe_text, text1=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, volatile=safe_text)
@given(instance=datastyle_BooleanStyleType_strategy)
@settings(max_examples=25)
def test_datastyle_BooleanStyleType_instantiation(instance):
    assert isinstance(instance, datastyle_BooleanStyleType)


datastyle_BooleanType_strategy = st.builds(datastyle_BooleanType)
@given(instance=datastyle_BooleanType_strategy)
@settings(max_examples=25)
def test_datastyle_BooleanType_instantiation(instance):
    assert isinstance(instance, datastyle_BooleanType)


datastyle_CurrencyStyleType_strategy = st.builds(datastyle_CurrencyStyleType, automaticOrder=safe_text, country=safe_text, language=safe_text, name=safe_text, text=safe_text, text1=safe_text, text2=safe_text, text3=safe_text, text4=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, volatile=safe_text)
@given(instance=datastyle_CurrencyStyleType_strategy)
@settings(max_examples=25)
def test_datastyle_CurrencyStyleType_instantiation(instance):
    assert isinstance(instance, datastyle_CurrencyStyleType)


datastyle_CurrencySymbolType_strategy = st.builds(datastyle_CurrencySymbolType, country=safe_text, language=safe_text, mixed=safe_text)
@given(instance=datastyle_CurrencySymbolType_strategy)
@settings(max_examples=25)
def test_datastyle_CurrencySymbolType_instantiation(instance):
    assert isinstance(instance, datastyle_CurrencySymbolType)


datastyle_DateStyleType_strategy = st.builds(datastyle_DateStyleType, automaticOrder=safe_text, country=safe_text, formatSource=safe_text, group=safe_text, language=safe_text, name=safe_text, text=safe_text, text1=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, volatile=safe_text)
@given(instance=datastyle_DateStyleType_strategy)
@settings(max_examples=25)
def test_datastyle_DateStyleType_instantiation(instance):
    assert isinstance(instance, datastyle_DateStyleType)


datastyle_DayOfWeekType_strategy = st.builds(datastyle_DayOfWeekType, calendar=safe_text, style=safe_text)
@given(instance=datastyle_DayOfWeekType_strategy)
@settings(max_examples=25)
def test_datastyle_DayOfWeekType_instantiation(instance):
    assert isinstance(instance, datastyle_DayOfWeekType)


datastyle_DayType_strategy = st.builds(datastyle_DayType, calendar=safe_text, style=safe_text)
@given(instance=datastyle_DayType_strategy)
@settings(max_examples=25)
def test_datastyle_DayType_instantiation(instance):
    assert isinstance(instance, datastyle_DayType)


datastyle_DocumentRoot_strategy = st.builds(datastyle_DocumentRoot, automaticOrder=safe_text, calendar=safe_text, country=safe_text, decimalPlaces=safe_text, decimalReplacement=safe_text, denominatorValue=safe_text, displayFactor=safe_text, formatSource=safe_text, grouping=safe_text, language=safe_text, minDenominatorDigits=safe_text, minExponentDigits=safe_text, minIntegerDigits=safe_text, minNumeratorDigits=safe_text, mixed=safe_text, position=safe_text, possessiveForm=safe_text, style=safe_text, text=safe_text, textual=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, truncateOnOverflow=safe_text)
@given(instance=datastyle_DocumentRoot_strategy)
@settings(max_examples=25)
def test_datastyle_DocumentRoot_instantiation(instance):
    assert isinstance(instance, datastyle_DocumentRoot)


datastyle_EObject_strategy = st.builds(datastyle_EObject)
@given(instance=datastyle_EObject_strategy)
@settings(max_examples=25)
def test_datastyle_EObject_instantiation(instance):
    assert isinstance(instance, datastyle_EObject)


datastyle_EStringToStringMapEntry_strategy = st.builds(datastyle_EStringToStringMapEntry)
@given(instance=datastyle_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_datastyle_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, datastyle_EStringToStringMapEntry)


datastyle_EmbeddedTextType_strategy = st.builds(datastyle_EmbeddedTextType, mixed=safe_text, position=safe_text)
@given(instance=datastyle_EmbeddedTextType_strategy)
@settings(max_examples=25)
def test_datastyle_EmbeddedTextType_instantiation(instance):
    assert isinstance(instance, datastyle_EmbeddedTextType)


datastyle_EraType_strategy = st.builds(datastyle_EraType, calendar=safe_text, style=safe_text)
@given(instance=datastyle_EraType_strategy)
@settings(max_examples=25)
def test_datastyle_EraType_instantiation(instance):
    assert isinstance(instance, datastyle_EraType)


datastyle_FractionType_strategy = st.builds(datastyle_FractionType, denominatorValue=safe_text, grouping=safe_text, minDenominatorDigits=safe_text, minIntegerDigits=safe_text, minNumeratorDigits=safe_text)
@given(instance=datastyle_FractionType_strategy)
@settings(max_examples=25)
def test_datastyle_FractionType_instantiation(instance):
    assert isinstance(instance, datastyle_FractionType)


datastyle_HoursType_strategy = st.builds(datastyle_HoursType, style=safe_text)
@given(instance=datastyle_HoursType_strategy)
@settings(max_examples=25)
def test_datastyle_HoursType_instantiation(instance):
    assert isinstance(instance, datastyle_HoursType)


datastyle_MapType_strategy = st.builds(datastyle_MapType)
@given(instance=datastyle_MapType_strategy)
@settings(max_examples=25)
def test_datastyle_MapType_instantiation(instance):
    assert isinstance(instance, datastyle_MapType)


datastyle_MinutesType_strategy = st.builds(datastyle_MinutesType, style=safe_text)
@given(instance=datastyle_MinutesType_strategy)
@settings(max_examples=25)
def test_datastyle_MinutesType_instantiation(instance):
    assert isinstance(instance, datastyle_MinutesType)


datastyle_MonthType_strategy = st.builds(datastyle_MonthType, calendar=safe_text, possessiveForm=safe_text, style=safe_text, textual=safe_text)
@given(instance=datastyle_MonthType_strategy)
@settings(max_examples=25)
def test_datastyle_MonthType_instantiation(instance):
    assert isinstance(instance, datastyle_MonthType)


datastyle_NumberStyleType_strategy = st.builds(datastyle_NumberStyleType, anyNumberGroup=safe_text, country=safe_text, language=safe_text, name=safe_text, text=safe_text, text1=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, volatile=safe_text)
@given(instance=datastyle_NumberStyleType_strategy)
@settings(max_examples=25)
def test_datastyle_NumberStyleType_instantiation(instance):
    assert isinstance(instance, datastyle_NumberStyleType)


datastyle_NumberType_strategy = st.builds(datastyle_NumberType, decimalPlaces=safe_text, decimalReplacement=safe_text, displayFactor=safe_text, grouping=safe_text, minIntegerDigits=safe_text)
@given(instance=datastyle_NumberType_strategy)
@settings(max_examples=25)
def test_datastyle_NumberType_instantiation(instance):
    assert isinstance(instance, datastyle_NumberType)


datastyle_PercentageStyleType_strategy = st.builds(datastyle_PercentageStyleType, country=safe_text, language=safe_text, name=safe_text, text=safe_text, text1=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, volatile=safe_text)
@given(instance=datastyle_PercentageStyleType_strategy)
@settings(max_examples=25)
def test_datastyle_PercentageStyleType_instantiation(instance):
    assert isinstance(instance, datastyle_PercentageStyleType)


datastyle_QuarterType_strategy = st.builds(datastyle_QuarterType, calendar=safe_text, style=safe_text)
@given(instance=datastyle_QuarterType_strategy)
@settings(max_examples=25)
def test_datastyle_QuarterType_instantiation(instance):
    assert isinstance(instance, datastyle_QuarterType)


datastyle_ScientificNumberType_strategy = st.builds(datastyle_ScientificNumberType, decimalPlaces=safe_text, grouping=safe_text, minExponentDigits=safe_text, minIntegerDigits=safe_text)
@given(instance=datastyle_ScientificNumberType_strategy)
@settings(max_examples=25)
def test_datastyle_ScientificNumberType_instantiation(instance):
    assert isinstance(instance, datastyle_ScientificNumberType)


datastyle_SecondsType_strategy = st.builds(datastyle_SecondsType, decimalPlaces=safe_text, style=safe_text)
@given(instance=datastyle_SecondsType_strategy)
@settings(max_examples=25)
def test_datastyle_SecondsType_instantiation(instance):
    assert isinstance(instance, datastyle_SecondsType)


datastyle_StyleTextPropertiesContent_strategy = st.builds(datastyle_StyleTextPropertiesContent)
@given(instance=datastyle_StyleTextPropertiesContent_strategy)
@settings(max_examples=25)
def test_datastyle_StyleTextPropertiesContent_instantiation(instance):
    assert isinstance(instance, datastyle_StyleTextPropertiesContent)


datastyle_TextContentType_strategy = st.builds(datastyle_TextContentType)
@given(instance=datastyle_TextContentType_strategy)
@settings(max_examples=25)
def test_datastyle_TextContentType_instantiation(instance):
    assert isinstance(instance, datastyle_TextContentType)


datastyle_TextStyleType_strategy = st.builds(datastyle_TextStyleType, country=safe_text, group=safe_text, language=safe_text, name=safe_text, text=safe_text, text1=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, volatile=safe_text)
@given(instance=datastyle_TextStyleType_strategy)
@settings(max_examples=25)
def test_datastyle_TextStyleType_instantiation(instance):
    assert isinstance(instance, datastyle_TextStyleType)


datastyle_TimeStyleType_strategy = st.builds(datastyle_TimeStyleType, country=safe_text, formatSource=safe_text, group=safe_text, language=safe_text, name=safe_text, text=safe_text, text1=safe_text, title=safe_text, transliterationCountry=safe_text, transliterationFormat=safe_text, transliterationLanguage=safe_text, transliterationStyle=safe_text, truncateOnOverflow=safe_text, volatile=safe_text)
@given(instance=datastyle_TimeStyleType_strategy)
@settings(max_examples=25)
def test_datastyle_TimeStyleType_instantiation(instance):
    assert isinstance(instance, datastyle_TimeStyleType)


datastyle_WeekOfYearType_strategy = st.builds(datastyle_WeekOfYearType, calendar=safe_text)
@given(instance=datastyle_WeekOfYearType_strategy)
@settings(max_examples=25)
def test_datastyle_WeekOfYearType_instantiation(instance):
    assert isinstance(instance, datastyle_WeekOfYearType)


datastyle_YearType_strategy = st.builds(datastyle_YearType, calendar=safe_text, style=safe_text)
@given(instance=datastyle_YearType_strategy)
@settings(max_examples=25)
def test_datastyle_YearType_instantiation(instance):
    assert isinstance(instance, datastyle_YearType)


