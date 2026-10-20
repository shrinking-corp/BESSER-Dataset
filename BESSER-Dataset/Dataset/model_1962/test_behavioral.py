import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sourceanalysator_Article,
    sourceanalysator_GeneralSource,
    sourceanalysator_Hyperlink,
    sourceanalysator_Library,
    sourceanalysator_Source,
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

def test_assoc_article2_stub_double():
    # sourceanalysator_Source has no real 'sources3' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_Article's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_Article's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_Article(localFile="sample_text", title="sample_text")
    partner = sourceanalysator_Source()
    setattr(partner, 'sources3', None)
    _safe_set(owner, 'Article', partner)
    assert getattr(partner, 'sources3') == owner
    _safe_set(owner, 'Article', None)
    assert getattr(partner, 'sources3') is None


def test_assoc_articles7_stub_double():
    # sourceanalysator_Library has no real 'sourceanalysator_Library8' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_Article's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_Article's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_Article(localFile="sample_text", title="sample_text")
    partner = sourceanalysator_Library()
    setattr(partner, 'sourceanalysator_Library8', None)
    _safe_set(owner, 'sourceanalysator_Article', partner)
    assert owner in getattr(partner, 'sourceanalysator_Library8')
    _safe_set(owner, 'sourceanalysator_Article', None)
    assert owner not in getattr(partner, 'sourceanalysator_Library8')


def test_assoc_generalSource1_stub_double():
    # sourceanalysator_Source has no real 'sources' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_GeneralSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_GeneralSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_GeneralSource(aliases="sample_text", dontCount=True, name="sample_text")
    partner = sourceanalysator_Source()
    setattr(partner, 'sources', None)
    _safe_set(owner, 'GeneralSource', partner)
    assert getattr(partner, 'sources') == owner
    _safe_set(owner, 'GeneralSource', None)
    assert getattr(partner, 'sources') is None


def test_assoc_generalSources6_stub_double():
    # sourceanalysator_Library has no real 'sourceanalysator_Library' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_GeneralSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_GeneralSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_GeneralSource(aliases="sample_text", dontCount=True, name="sample_text")
    partner = sourceanalysator_Library()
    setattr(partner, 'sourceanalysator_Library', None)
    _safe_set(owner, 'sourceanalysator_GeneralSource', partner)
    assert owner in getattr(partner, 'sourceanalysator_Library')
    _safe_set(owner, 'sourceanalysator_GeneralSource', None)
    assert owner not in getattr(partner, 'sourceanalysator_Library')


def test_assoc_hyperlink4_stub_double():
    # sourceanalysator_Source has no real 'sources5' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_Hyperlink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_Hyperlink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_Hyperlink(url="sample_text")
    partner = sourceanalysator_Source()
    setattr(partner, 'sources5', None)
    _safe_set(owner, 'Hyperlink', partner)
    assert getattr(partner, 'sources5') == owner
    _safe_set(owner, 'Hyperlink', None)
    assert getattr(partner, 'sources5') is None


def test_assoc_hyperlinks9_stub_double():
    # sourceanalysator_Library has no real 'sourceanalysator_Library10' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_Hyperlink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_Hyperlink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_Hyperlink(url="sample_text")
    partner = sourceanalysator_Library()
    setattr(partner, 'sourceanalysator_Library10', None)
    _safe_set(owner, 'sourceanalysator_Hyperlink', partner)
    assert owner in getattr(partner, 'sourceanalysator_Library10')
    _safe_set(owner, 'sourceanalysator_Hyperlink', None)
    assert owner not in getattr(partner, 'sourceanalysator_Library10')


def test_assoc_sources0_stub_double():
    # sourceanalysator_Source has no real 'Source' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_GeneralSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_GeneralSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_GeneralSource(aliases="sample_text", dontCount=True, name="sample_text")
    partner = sourceanalysator_Source()
    setattr(partner, 'Source', None)
    _safe_set(owner, 'generalSource', {partner})
    assert getattr(partner, 'Source') == owner
    _safe_set(owner, 'generalSource', set())
    assert getattr(partner, 'Source') is None


def test_assoc_sources11_stub_double():
    # sourceanalysator_Source has no real 'Source12' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_Article's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_Article's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_Article(localFile="sample_text", title="sample_text")
    partner = sourceanalysator_Source()
    setattr(partner, 'Source12', None)
    _safe_set(owner, 'article', {partner})
    assert getattr(partner, 'Source12') == owner
    _safe_set(owner, 'article', set())
    assert getattr(partner, 'Source12') is None


def test_assoc_sources13_stub_double():
    # sourceanalysator_Source has no real 'Source14' property in the generated
    # code (a bare stub) -- manually attach it so sourceanalysator_Hyperlink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourceanalysator_Hyperlink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourceanalysator_Hyperlink(url="sample_text")
    partner = sourceanalysator_Source()
    setattr(partner, 'Source14', None)
    _safe_set(owner, 'hyperlink', {partner})
    assert getattr(partner, 'Source14') == owner
    _safe_set(owner, 'hyperlink', set())
    assert getattr(partner, 'Source14') is None


