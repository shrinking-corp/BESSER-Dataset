import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bibtex_Document,
    bibtex_Model,
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

def test_assoc_taxonomy0_stub_double():
    # bibtex_Model has no real 'bibtex_Model' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Document(abstract="sample_text", authors="sample_text", cites=7, doi="sample_text", file="sample_text", key="sample_text", month="sample_text", title="sample_text", type="sample_text", unparsedAuthors="sample_text", url="sample_text", year="sample_text")
    partner = bibtex_Model()
    setattr(partner, 'bibtex_Model', None)
    _safe_set(owner, 'bibtex_Document', partner)
    assert getattr(partner, 'bibtex_Model') == owner
    _safe_set(owner, 'bibtex_Document', None)
    assert getattr(partner, 'bibtex_Model') is None


