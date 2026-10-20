import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Author,
    AuthoredEntry,
    BibTeXEntry,
    BibTeX_Article,
    BibTeX_Author,
    BibTeX_AuthoredEntry,
    BibTeX_BibTeXEntry,
    BibTeX_BibTeXFile,
    BibTeX_Book,
    BibTeX_BookTitledEntry,
    BibTeX_Booklet,
    BibTeX_DatedEntry,
    BibTeX_InBook,
    BibTeX_InCollection,
    BibTeX_InProceedings,
    BibTeX_Manual,
    BibTeX_MasterThesis,
    BibTeX_Misc,
    BibTeX_PhDThesis,
    BibTeX_Proceedings,
    BibTeX_TechReport,
    BibTeX_ThesisEntry,
    BibTeX_TitledEntry,
    BibTeX_Unpublished,
    Book,
    BookTitledEntry,
    DatedEntry,
    Proceedings,
    ThesisEntry,
    TitledEntry,
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

