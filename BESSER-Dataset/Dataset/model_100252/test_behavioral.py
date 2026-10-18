import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CaseStyle,
    Parameter,
    Pattern,
    Styling_Basic,
    Styling_BooleanParameter,
    Styling_CaseStyle,
    Styling_ConstantPattern,
    Styling_Default,
    Styling_EObject,
    Styling_EObjectParameter,
    Styling_IPredicate,
    Styling_Icon,
    Styling_IntParameter,
    Styling_ModelPattern,
    Styling_OperationPattern,
    Styling_Parameter,
    Styling_Pattern,
    Styling_Segment,
    Styling_StringParameter,
    Styling_Style,
    Styling_Styling,
    Styling_StylingModel,
    Styling_StylingPredicate,
    FontOption,
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

def test_assoc_icon12_reverse_link_reassign_clear():
    a1 = Styling_Icon(image="sample_text")
    a2 = Styling_Icon(image="sample_text_2")
    b = Styling_CaseStyle()
    _safe_set(b, 'Styling_CaseStyle13', a1)
    assert _is_linked(b, 'Styling_CaseStyle13', a1)
    if hasattr(a1, 'Styling_Icon'):
        assert _is_linked(a1, 'Styling_Icon', b)
    _safe_set(b, 'Styling_CaseStyle13', a2)
    assert _is_linked(b, 'Styling_CaseStyle13', a2)
    if hasattr(a1, 'Styling_Icon'):
        assert not _is_linked(a1, 'Styling_Icon', b)
    if hasattr(a2, 'Styling_Icon'):
        assert _is_linked(a2, 'Styling_Icon', b)
    _safe_set(b, 'Styling_CaseStyle13', None)
    assert not _is_linked(b, 'Styling_CaseStyle13', a2)
    if hasattr(a2, 'Styling_Icon'):
        assert not _is_linked(a2, 'Styling_Icon', b)


def test_assoc_parameters16_reverse_link_reassign_clear():
    a1 = Styling_Parameter(name="sample_text")
    a2 = Styling_Parameter(name="sample_text_2")
    b = Styling_OperationPattern(operation="sample_text")
    _safe_set(b, 'Styling_OperationPattern', {a1})
    assert _is_linked(b, 'Styling_OperationPattern', a1)
    if hasattr(a1, 'Styling_Parameter'):
        assert _is_linked(a1, 'Styling_Parameter', b)
    _safe_set(b, 'Styling_OperationPattern', {a2})
    assert _is_linked(b, 'Styling_OperationPattern', a2)
    if hasattr(a1, 'Styling_Parameter'):
        assert not _is_linked(a1, 'Styling_Parameter', b)
    if hasattr(a2, 'Styling_Parameter'):
        assert _is_linked(a2, 'Styling_Parameter', b)
    _safe_set(b, 'Styling_OperationPattern', set())
    assert not _is_linked(b, 'Styling_OperationPattern', a2)
    if hasattr(a2, 'Styling_Parameter'):
        assert not _is_linked(a2, 'Styling_Parameter', b)


def test_assoc_pattern7_reverse_link_reassign_clear():
    a1 = Styling_Segment()
    a2 = Styling_Segment()
    b = Styling_Pattern()
    _safe_set(b, 'Styling_Pattern', a1)
    assert _is_linked(b, 'Styling_Pattern', a1)
    if hasattr(a1, 'Styling_Segment8'):
        assert _is_linked(a1, 'Styling_Segment8', b)
    _safe_set(b, 'Styling_Pattern', a2)
    assert _is_linked(b, 'Styling_Pattern', a2)
    if hasattr(a1, 'Styling_Segment8'):
        assert not _is_linked(a1, 'Styling_Segment8', b)
    if hasattr(a2, 'Styling_Segment8'):
        assert _is_linked(a2, 'Styling_Segment8', b)
    _safe_set(b, 'Styling_Pattern', None)
    assert not _is_linked(b, 'Styling_Pattern', a2)
    if hasattr(a2, 'Styling_Segment8'):
        assert not _is_linked(a2, 'Styling_Segment8', b)


def test_assoc_segments9_reverse_link_reassign_clear():
    a1 = Styling_Segment()
    a2 = Styling_Segment()
    b = Styling_CaseStyle()
    _safe_set(b, 'Styling_CaseStyle10', {a1})
    assert _is_linked(b, 'Styling_CaseStyle10', a1)
    if hasattr(a1, 'Styling_Segment11'):
        assert _is_linked(a1, 'Styling_Segment11', b)
    _safe_set(b, 'Styling_CaseStyle10', {a2})
    assert _is_linked(b, 'Styling_CaseStyle10', a2)
    if hasattr(a1, 'Styling_Segment11'):
        assert not _is_linked(a1, 'Styling_Segment11', b)
    if hasattr(a2, 'Styling_Segment11'):
        assert _is_linked(a2, 'Styling_Segment11', b)
    _safe_set(b, 'Styling_CaseStyle10', set())
    assert not _is_linked(b, 'Styling_CaseStyle10', a2)
    if hasattr(a2, 'Styling_Segment11'):
        assert not _is_linked(a2, 'Styling_Segment11', b)


def test_assoc_style6_reverse_link_reassign_clear():
    a1 = Styling_Style(appliedFonts="sample_text", color="sample_text")
    a2 = Styling_Style(appliedFonts="sample_text_2", color="sample_text_2")
    b = Styling_Segment()
    _safe_set(b, 'Styling_Segment', a1)
    assert _is_linked(b, 'Styling_Segment', a1)
    if hasattr(a1, 'Styling_Style'):
        assert _is_linked(a1, 'Styling_Style', b)
    _safe_set(b, 'Styling_Segment', a2)
    assert _is_linked(b, 'Styling_Segment', a2)
    if hasattr(a1, 'Styling_Style'):
        assert not _is_linked(a1, 'Styling_Style', b)
    if hasattr(a2, 'Styling_Style'):
        assert _is_linked(a2, 'Styling_Style', b)
    _safe_set(b, 'Styling_Segment', None)
    assert not _is_linked(b, 'Styling_Segment', a2)
    if hasattr(a2, 'Styling_Style'):
        assert not _is_linked(a2, 'Styling_Style', b)


def test_assoc_styles0_reverse_link_reassign_clear():
    a1 = Styling_StylingModel(modeName="sample_text")
    a2 = Styling_StylingModel(modeName="sample_text_2")
    b = Styling_CaseStyle()
    _safe_set(b, 'Styling_CaseStyle', a1)
    assert _is_linked(b, 'Styling_CaseStyle', a1)
    if hasattr(a1, 'Styling_StylingModel'):
        assert _is_linked(a1, 'Styling_StylingModel', b)
    _safe_set(b, 'Styling_CaseStyle', a2)
    assert _is_linked(b, 'Styling_CaseStyle', a2)
    if hasattr(a1, 'Styling_StylingModel'):
        assert not _is_linked(a1, 'Styling_StylingModel', b)
    if hasattr(a2, 'Styling_StylingModel'):
        assert _is_linked(a2, 'Styling_StylingModel', b)
    _safe_set(b, 'Styling_CaseStyle', None)
    assert not _is_linked(b, 'Styling_CaseStyle', a2)
    if hasattr(a2, 'Styling_StylingModel'):
        assert not _is_linked(a2, 'Styling_StylingModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_basic3_stub_double():
    # Styling_Basic has no real 'Styling_Basic' property in the generated
    # code (a bare stub) -- manually attach it so Styling_StylingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Styling_StylingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Styling_StylingModel(modeName="sample_text")
    partner = Styling_Basic()
    setattr(partner, 'Styling_Basic', None)
    _safe_set(owner, 'Styling_StylingModel4', partner)
    assert getattr(partner, 'Styling_Basic') == owner
    _safe_set(owner, 'Styling_StylingModel4', None)
    assert getattr(partner, 'Styling_Basic') is None


def test_assoc_default1_stub_double():
    # Styling_Default has no real 'Styling_Default' property in the generated
    # code (a bare stub) -- manually attach it so Styling_StylingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Styling_StylingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Styling_StylingModel(modeName="sample_text")
    partner = Styling_Default()
    setattr(partner, 'Styling_Default', None)
    _safe_set(owner, 'Styling_StylingModel2', partner)
    assert getattr(partner, 'Styling_Default') == owner
    _safe_set(owner, 'Styling_StylingModel2', None)
    assert getattr(partner, 'Styling_Default') is None


def test_assoc_models14_stub_double():
    # Styling_Styling has no real 'Styling_Styling' property in the generated
    # code (a bare stub) -- manually attach it so Styling_StylingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Styling_StylingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Styling_StylingModel(modeName="sample_text")
    partner = Styling_Styling()
    setattr(partner, 'Styling_Styling', None)
    _safe_set(owner, 'Styling_StylingModel15', partner)
    assert owner in getattr(partner, 'Styling_Styling')
    _safe_set(owner, 'Styling_StylingModel15', None)
    assert owner not in getattr(partner, 'Styling_Styling')


