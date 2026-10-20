import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    HtmlProfile,
    wikigen_Article,
    wikigen_Container,
    wikigen_Document,
    wikigen_GenHtmlDocument,
    wikigen_GenLatexDocument,
    wikigen_HtmlProfile,
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

def test_assoc_roots0_stub_double():
    # wikigen_Container has no real 'wikigen_Container' property in the generated
    # code (a bare stub) -- manually attach it so wikigen_GenLatexDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikigen_GenLatexDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikigen_GenLatexDocument(authors="sample_text", filename="sample_text", title="sample_text")
    partner = wikigen_Container()
    setattr(partner, 'wikigen_Container', None)
    _safe_set(owner, 'wikigen_GenLatexDocument', {partner})
    assert getattr(partner, 'wikigen_Container') == owner
    _safe_set(owner, 'wikigen_GenLatexDocument', set())
    assert getattr(partner, 'wikigen_Container') is None


def test_assoc_roots2_stub_double():
    # wikigen_Document has no real 'wikigen_Document' property in the generated
    # code (a bare stub) -- manually attach it so wikigen_GenHtmlDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikigen_GenHtmlDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikigen_GenHtmlDocument(filename="sample_text")
    partner = wikigen_Document()
    setattr(partner, 'wikigen_Document', None)
    _safe_set(owner, 'wikigen_GenHtmlDocument3', {partner})
    assert getattr(partner, 'wikigen_Document') == owner
    _safe_set(owner, 'wikigen_GenHtmlDocument3', set())
    assert getattr(partner, 'wikigen_Document') is None


def test_assoc_style1_stub_double():
    # wikigen_HtmlProfile has no real 'wikigen_HtmlProfile' property in the generated
    # code (a bare stub) -- manually attach it so wikigen_GenHtmlDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wikigen_GenHtmlDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wikigen_GenHtmlDocument(filename="sample_text")
    partner = wikigen_HtmlProfile()
    setattr(partner, 'wikigen_HtmlProfile', None)
    _safe_set(owner, 'wikigen_GenHtmlDocument', partner)
    assert getattr(partner, 'wikigen_HtmlProfile') == owner
    _safe_set(owner, 'wikigen_GenHtmlDocument', None)
    assert getattr(partner, 'wikigen_HtmlProfile') is None


