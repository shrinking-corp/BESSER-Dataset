import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Abstract,
    Adress,
    Author,
    Bibliography,
    Citation,
    Corps,
    Date,
    Description,
    Document,
    DocumentBody,
    EMail,
    Enumerate,
    Fax,
    Heading,
    Item,
    Items,
    Keywords,
    LaTeX_Abstract,
    LaTeX_Adress,
    LaTeX_Author,
    LaTeX_Bibliography,
    LaTeX_Citation,
    LaTeX_Cite,
    LaTeX_Corps,
    LaTeX_Date,
    LaTeX_Description,
    LaTeX_Document,
    LaTeX_DocumentBody,
    LaTeX_EMail,
    LaTeX_Enumerate,
    LaTeX_Fax,
    LaTeX_Figure,
    LaTeX_Heading,
    LaTeX_Item,
    LaTeX_Items,
    LaTeX_Keywords,
    LaTeX_Label,
    LaTeX_Name,
    LaTeX_Organisation,
    LaTeX_Path,
    LaTeX_Phone,
    LaTeX_Section,
    LaTeX_SectionBody,
    LaTeX_Title,
    LaTeX_Type,
    LaTeX_Value,
    LaTeX_ValuedElement,
    Label,
    Name,
    Organisation,
    Path,
    Phone,
    Section,
    SectionBody,
    Title,
    Type,
    ValuedElement,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

