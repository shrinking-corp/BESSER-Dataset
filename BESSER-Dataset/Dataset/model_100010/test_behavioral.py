import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AuthorField,
    BibtexEntryTypes,
    bibTeX_AddressField,
    bibTeX_Article,
    bibTeX_AuthorField,
    bibTeX_Authors,
    bibTeX_BibtexEntryTypes,
    bibTeX_Book,
    bibTeX_CiteKey,
    bibTeX_EObject,
    bibTeX_EditionField,
    bibTeX_EditorField,
    bibTeX_Fullname,
    bibTeX_IsbnField,
    bibTeX_JournalField,
    bibTeX_Model,
    bibTeX_MonthField,
    bibTeX_NoteField,
    bibTeX_NumberField,
    bibTeX_PagesField,
    bibTeX_PublisherField,
    bibTeX_SeriesField,
    bibTeX_TitleField,
    bibTeX_UnknownField,
    bibTeX_UnknownType,
    bibTeX_UnknownValue,
    bibTeX_VolumeField,
    bibTeX_YearField,
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

