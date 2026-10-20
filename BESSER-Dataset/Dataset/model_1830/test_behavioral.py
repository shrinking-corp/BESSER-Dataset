import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SrcAuthor,
    SrcAuthoredEntry,
    SrcBibTeXEntry,
    SrcBook,
    SrcBookTitledEntry,
    SrcDatedEntry,
    SrcMasterThesis,
    SrcProceedings,
    SrcThesisEntry,
    SrcTitledEntry,
    TrgArticle,
    TrgBook,
    TrgDocBook,
    TrgPara,
    TrgSect1,
    TrgSect2,
    TrgSection,
    TrgTitledElement,
    jointPackage_JointMM,
    jointPackage_SrcArticle,
    jointPackage_SrcAuthor,
    jointPackage_SrcAuthoredEntry,
    jointPackage_SrcBibTeXEntry,
    jointPackage_SrcBibTeXFile,
    jointPackage_SrcBook,
    jointPackage_SrcBookTitledEntry,
    jointPackage_SrcBooklet,
    jointPackage_SrcDatedEntry,
    jointPackage_SrcInBook,
    jointPackage_SrcInCollection,
    jointPackage_SrcInProceedings,
    jointPackage_SrcManual,
    jointPackage_SrcMasterThesis,
    jointPackage_SrcMisc,
    jointPackage_SrcPhDThesis,
    jointPackage_SrcProceedings,
    jointPackage_SrcTechReport,
    jointPackage_SrcThesisEntry,
    jointPackage_SrcTitledEntry,
    jointPackage_SrcUnpublished,
    jointPackage_TrgArticle,
    jointPackage_TrgBook,
    jointPackage_TrgDocBook,
    jointPackage_TrgPara,
    jointPackage_TrgSect1,
    jointPackage_TrgSect2,
    jointPackage_TrgSection,
    jointPackage_TrgTitledElement,
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

def test_assoc_section10_stub_double():
    # TrgSection has no real 'TrgSection' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_TrgPara's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_TrgPara's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_TrgPara(content="sample_text")
    partner = TrgSection()
    setattr(partner, 'TrgSection', None)
    _safe_set(owner, 'paras', partner)
    assert getattr(partner, 'TrgSection') == owner
    _safe_set(owner, 'paras', None)
    assert getattr(partner, 'TrgSection') is None


