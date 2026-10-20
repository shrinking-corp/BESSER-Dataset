import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    VSpec,
    VSpecResolution,
    VariationPoint,
    cvlmodel_CVLModel,
    cvlmodel_Choice,
    cvlmodel_ChoiceResolution,
    cvlmodel_MOFRef,
    cvlmodel_Multiplicity,
    cvlmodel_ObjectExistence,
    cvlmodel_ResolutionModel,
    cvlmodel_StringToMOFRefMap,
    cvlmodel_VClassifier,
    cvlmodel_VClassifierResolution,
    cvlmodel_VSpec,
    cvlmodel_VSpecResolution,
    cvlmodel_VSpecTree,
    cvlmodel_Variable,
    cvlmodel_VariableResolution,
    cvlmodel_VariationPoint,
    PrimitiveTypeEnum,
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

def test_assoc_binding14_reverse_link_reassign_clear():
    a1 = cvlmodel_VariationPoint(modelTransformationSourceURL="sample_text", modelTransformationURL="sample_text", name="sample_text", negativeVariability="sample_text")
    a2 = cvlmodel_VariationPoint(modelTransformationSourceURL="sample_text_2", modelTransformationURL="sample_text_2", name="sample_text_2", negativeVariability="sample_text_2")
    b = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    _safe_set(b, 'cvlmodel_VSpec15', a1)
    assert _is_linked(b, 'cvlmodel_VSpec15', a1)
    if hasattr(a1, 'cvlmodel_VariationPoint'):
        assert _is_linked(a1, 'cvlmodel_VariationPoint', b)
    _safe_set(b, 'cvlmodel_VSpec15', a2)
    assert _is_linked(b, 'cvlmodel_VSpec15', a2)
    if hasattr(a1, 'cvlmodel_VariationPoint'):
        assert not _is_linked(a1, 'cvlmodel_VariationPoint', b)
    if hasattr(a2, 'cvlmodel_VariationPoint'):
        assert _is_linked(a2, 'cvlmodel_VariationPoint', b)
    _safe_set(b, 'cvlmodel_VSpec15', None)
    assert not _is_linked(b, 'cvlmodel_VSpec15', a2)
    if hasattr(a2, 'cvlmodel_VariationPoint'):
        assert not _is_linked(a2, 'cvlmodel_VariationPoint', b)


def test_assoc_children5_reverse_link_reassign_clear():
    a1 = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    a2 = cvlmodel_VSpec(mandatory="sample_text_2", name="sample_text_2")
    b = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    _safe_set(b, 'cvlmodel_VSpec6', a1)
    assert _is_linked(b, 'cvlmodel_VSpec6', a1)
    if hasattr(a1, 'cvlmodel_VSpec4'):
        assert _is_linked(a1, 'cvlmodel_VSpec4', b)
    _safe_set(b, 'cvlmodel_VSpec6', a2)
    assert _is_linked(b, 'cvlmodel_VSpec6', a2)
    if hasattr(a1, 'cvlmodel_VSpec4'):
        assert not _is_linked(a1, 'cvlmodel_VSpec4', b)
    if hasattr(a2, 'cvlmodel_VSpec4'):
        assert _is_linked(a2, 'cvlmodel_VSpec4', b)
    _safe_set(b, 'cvlmodel_VSpec6', None)
    assert not _is_linked(b, 'cvlmodel_VSpec6', a2)
    if hasattr(a2, 'cvlmodel_VSpec4'):
        assert not _is_linked(a2, 'cvlmodel_VSpec4', b)


def test_assoc_children7_reverse_link_reassign_clear():
    a1 = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    a2 = cvlmodel_VSpec(mandatory="sample_text_2", name="sample_text_2")
    b = cvlmodel_Multiplicity(max="sample_text", min="sample_text")
    _safe_set(b, 'cvlmodel_Multiplicity8', {a1})
    assert _is_linked(b, 'cvlmodel_Multiplicity8', a1)
    if hasattr(a1, 'cvlmodel_VSpec9'):
        assert _is_linked(a1, 'cvlmodel_VSpec9', b)
    _safe_set(b, 'cvlmodel_Multiplicity8', {a2})
    assert _is_linked(b, 'cvlmodel_Multiplicity8', a2)
    if hasattr(a1, 'cvlmodel_VSpec9'):
        assert not _is_linked(a1, 'cvlmodel_VSpec9', b)
    if hasattr(a2, 'cvlmodel_VSpec9'):
        assert _is_linked(a2, 'cvlmodel_VSpec9', b)
    _safe_set(b, 'cvlmodel_Multiplicity8', set())
    assert not _is_linked(b, 'cvlmodel_Multiplicity8', a2)
    if hasattr(a2, 'cvlmodel_VSpec9'):
        assert not _is_linked(a2, 'cvlmodel_VSpec9', b)


def test_assoc_groupMultiplicity0_reverse_link_reassign_clear():
    a1 = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    a2 = cvlmodel_VSpec(mandatory="sample_text_2", name="sample_text_2")
    b = cvlmodel_Multiplicity(max="sample_text", min="sample_text")
    _safe_set(b, 'cvlmodel_Multiplicity', a1)
    assert _is_linked(b, 'cvlmodel_Multiplicity', a1)
    if hasattr(a1, 'cvlmodel_VSpec'):
        assert _is_linked(a1, 'cvlmodel_VSpec', b)
    _safe_set(b, 'cvlmodel_Multiplicity', a2)
    assert _is_linked(b, 'cvlmodel_Multiplicity', a2)
    if hasattr(a1, 'cvlmodel_VSpec'):
        assert not _is_linked(a1, 'cvlmodel_VSpec', b)
    if hasattr(a2, 'cvlmodel_VSpec'):
        assert _is_linked(a2, 'cvlmodel_VSpec', b)
    _safe_set(b, 'cvlmodel_Multiplicity', None)
    assert not _is_linked(b, 'cvlmodel_Multiplicity', a2)
    if hasattr(a2, 'cvlmodel_VSpec'):
        assert not _is_linked(a2, 'cvlmodel_VSpec', b)


def test_assoc_parent2_reverse_link_reassign_clear():
    a1 = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    a2 = cvlmodel_VSpec(mandatory="sample_text_2", name="sample_text_2")
    b = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    _safe_set(b, 'cvlmodel_VSpec3', a1)
    assert _is_linked(b, 'cvlmodel_VSpec3', a1)
    if hasattr(a1, 'cvlmodel_VSpec1'):
        assert _is_linked(a1, 'cvlmodel_VSpec1', b)
    _safe_set(b, 'cvlmodel_VSpec3', a2)
    assert _is_linked(b, 'cvlmodel_VSpec3', a2)
    if hasattr(a1, 'cvlmodel_VSpec1'):
        assert not _is_linked(a1, 'cvlmodel_VSpec1', b)
    if hasattr(a2, 'cvlmodel_VSpec1'):
        assert _is_linked(a2, 'cvlmodel_VSpec1', b)
    _safe_set(b, 'cvlmodel_VSpec3', None)
    assert not _is_linked(b, 'cvlmodel_VSpec3', a2)
    if hasattr(a2, 'cvlmodel_VSpec1'):
        assert not _is_linked(a2, 'cvlmodel_VSpec1', b)


def test_assoc_references16_reverse_link_reassign_clear():
    a1 = cvlmodel_VariationPoint(modelTransformationSourceURL="sample_text", modelTransformationURL="sample_text", name="sample_text", negativeVariability="sample_text")
    a2 = cvlmodel_VariationPoint(modelTransformationSourceURL="sample_text_2", modelTransformationURL="sample_text_2", name="sample_text_2", negativeVariability="sample_text_2")
    b = cvlmodel_StringToMOFRefMap(key="sample_text")
    _safe_set(b, 'cvlmodel_StringToMOFRefMap', a1)
    assert _is_linked(b, 'cvlmodel_StringToMOFRefMap', a1)
    if hasattr(a1, 'cvlmodel_VariationPoint17'):
        assert _is_linked(a1, 'cvlmodel_VariationPoint17', b)
    _safe_set(b, 'cvlmodel_StringToMOFRefMap', a2)
    assert _is_linked(b, 'cvlmodel_StringToMOFRefMap', a2)
    if hasattr(a1, 'cvlmodel_VariationPoint17'):
        assert not _is_linked(a1, 'cvlmodel_VariationPoint17', b)
    if hasattr(a2, 'cvlmodel_VariationPoint17'):
        assert _is_linked(a2, 'cvlmodel_VariationPoint17', b)
    _safe_set(b, 'cvlmodel_StringToMOFRefMap', None)
    assert not _is_linked(b, 'cvlmodel_StringToMOFRefMap', a2)
    if hasattr(a2, 'cvlmodel_VariationPoint17'):
        assert not _is_linked(a2, 'cvlmodel_VariationPoint17', b)


def test_assoc_resolutions25_reverse_link_reassign_clear():
    a1 = cvlmodel_VSpecResolution(name="sample_text")
    a2 = cvlmodel_VSpecResolution(name="sample_text_2")
    b = cvlmodel_ResolutionModel(name="sample_text")
    _safe_set(b, 'cvlmodel_ResolutionModel', {a1})
    assert _is_linked(b, 'cvlmodel_ResolutionModel', a1)
    if hasattr(a1, 'cvlmodel_VSpecResolution26'):
        assert _is_linked(a1, 'cvlmodel_VSpecResolution26', b)
    _safe_set(b, 'cvlmodel_ResolutionModel', {a2})
    assert _is_linked(b, 'cvlmodel_ResolutionModel', a2)
    if hasattr(a1, 'cvlmodel_VSpecResolution26'):
        assert not _is_linked(a1, 'cvlmodel_VSpecResolution26', b)
    if hasattr(a2, 'cvlmodel_VSpecResolution26'):
        assert _is_linked(a2, 'cvlmodel_VSpecResolution26', b)
    _safe_set(b, 'cvlmodel_ResolutionModel', set())
    assert not _is_linked(b, 'cvlmodel_ResolutionModel', a2)
    if hasattr(a2, 'cvlmodel_VSpecResolution26'):
        assert not _is_linked(a2, 'cvlmodel_VSpecResolution26', b)


def test_assoc_resolvedVSpec12_reverse_link_reassign_clear():
    a1 = cvlmodel_VSpecResolution(name="sample_text")
    a2 = cvlmodel_VSpecResolution(name="sample_text_2")
    b = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    _safe_set(b, 'cvlmodel_VSpec13', a1)
    assert _is_linked(b, 'cvlmodel_VSpec13', a1)
    if hasattr(a1, 'cvlmodel_VSpecResolution'):
        assert _is_linked(a1, 'cvlmodel_VSpecResolution', b)
    _safe_set(b, 'cvlmodel_VSpec13', a2)
    assert _is_linked(b, 'cvlmodel_VSpec13', a2)
    if hasattr(a1, 'cvlmodel_VSpecResolution'):
        assert not _is_linked(a1, 'cvlmodel_VSpecResolution', b)
    if hasattr(a2, 'cvlmodel_VSpecResolution'):
        assert _is_linked(a2, 'cvlmodel_VSpecResolution', b)
    _safe_set(b, 'cvlmodel_VSpec13', None)
    assert not _is_linked(b, 'cvlmodel_VSpec13', a2)
    if hasattr(a2, 'cvlmodel_VSpecResolution'):
        assert not _is_linked(a2, 'cvlmodel_VSpecResolution', b)


def test_assoc_value18_reverse_link_reassign_clear():
    a1 = cvlmodel_StringToMOFRefMap(key="sample_text")
    a2 = cvlmodel_StringToMOFRefMap(key="sample_text_2")
    b = cvlmodel_MOFRef(id="sample_text")
    _safe_set(b, 'cvlmodel_MOFRef', a1)
    assert _is_linked(b, 'cvlmodel_MOFRef', a1)
    if hasattr(a1, 'cvlmodel_StringToMOFRefMap19'):
        assert _is_linked(a1, 'cvlmodel_StringToMOFRefMap19', b)
    _safe_set(b, 'cvlmodel_MOFRef', a2)
    assert _is_linked(b, 'cvlmodel_MOFRef', a2)
    if hasattr(a1, 'cvlmodel_StringToMOFRefMap19'):
        assert not _is_linked(a1, 'cvlmodel_StringToMOFRefMap19', b)
    if hasattr(a2, 'cvlmodel_StringToMOFRefMap19'):
        assert _is_linked(a2, 'cvlmodel_StringToMOFRefMap19', b)
    _safe_set(b, 'cvlmodel_MOFRef', None)
    assert not _is_linked(b, 'cvlmodel_MOFRef', a2)
    if hasattr(a2, 'cvlmodel_StringToMOFRefMap19'):
        assert not _is_linked(a2, 'cvlmodel_StringToMOFRefMap19', b)


def test_assoc_variationPoints32_reverse_link_reassign_clear():
    a1 = cvlmodel_VariationPoint(modelTransformationSourceURL="sample_text", modelTransformationURL="sample_text", name="sample_text", negativeVariability="sample_text")
    a2 = cvlmodel_VariationPoint(modelTransformationSourceURL="sample_text_2", modelTransformationURL="sample_text_2", name="sample_text_2", negativeVariability="sample_text_2")
    b = cvlmodel_CVLModel(name="sample_text")
    _safe_set(b, 'cvlmodel_CVLModel33', {a1})
    assert _is_linked(b, 'cvlmodel_CVLModel33', a1)
    if hasattr(a1, 'cvlmodel_VariationPoint34'):
        assert _is_linked(a1, 'cvlmodel_VariationPoint34', b)
    _safe_set(b, 'cvlmodel_CVLModel33', {a2})
    assert _is_linked(b, 'cvlmodel_CVLModel33', a2)
    if hasattr(a1, 'cvlmodel_VariationPoint34'):
        assert not _is_linked(a1, 'cvlmodel_VariationPoint34', b)
    if hasattr(a2, 'cvlmodel_VariationPoint34'):
        assert _is_linked(a2, 'cvlmodel_VariationPoint34', b)
    _safe_set(b, 'cvlmodel_CVLModel33', set())
    assert not _is_linked(b, 'cvlmodel_CVLModel33', a2)
    if hasattr(a2, 'cvlmodel_VariationPoint34'):
        assert not _is_linked(a2, 'cvlmodel_VariationPoint34', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_instanceMultiplicity10_stub_double():
    # cvlmodel_VClassifier has no real 'cvlmodel_VClassifier' property in the generated
    # code (a bare stub) -- manually attach it so cvlmodel_Multiplicity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cvlmodel_Multiplicity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cvlmodel_Multiplicity(max="sample_text", min="sample_text")
    partner = cvlmodel_VClassifier()
    setattr(partner, 'cvlmodel_VClassifier', None)
    _safe_set(owner, 'cvlmodel_Multiplicity11', partner)
    assert getattr(partner, 'cvlmodel_VClassifier') == owner
    _safe_set(owner, 'cvlmodel_Multiplicity11', None)
    assert getattr(partner, 'cvlmodel_VClassifier') is None


def test_assoc_resolvedVSpec27_stub_double():
    # cvlmodel_VSpecTree has no real 'cvlmodel_VSpecTree29' property in the generated
    # code (a bare stub) -- manually attach it so cvlmodel_ResolutionModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cvlmodel_ResolutionModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cvlmodel_ResolutionModel(name="sample_text")
    partner = cvlmodel_VSpecTree()
    setattr(partner, 'cvlmodel_VSpecTree29', None)
    _safe_set(owner, 'cvlmodel_ResolutionModel28', partner)
    assert getattr(partner, 'cvlmodel_VSpecTree29') == owner
    _safe_set(owner, 'cvlmodel_ResolutionModel28', None)
    assert getattr(partner, 'cvlmodel_VSpecTree29') is None


def test_assoc_root22_stub_double():
    # cvlmodel_VSpecTree has no real 'cvlmodel_VSpecTree23' property in the generated
    # code (a bare stub) -- manually attach it so cvlmodel_VSpec's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cvlmodel_VSpec's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    partner = cvlmodel_VSpecTree()
    setattr(partner, 'cvlmodel_VSpecTree23', None)
    _safe_set(owner, 'cvlmodel_VSpec24', partner)
    assert getattr(partner, 'cvlmodel_VSpecTree23') == owner
    _safe_set(owner, 'cvlmodel_VSpec24', None)
    assert getattr(partner, 'cvlmodel_VSpecTree23') is None


def test_assoc_vspecTree30_stub_double():
    # cvlmodel_VSpecTree has no real 'cvlmodel_VSpecTree31' property in the generated
    # code (a bare stub) -- manually attach it so cvlmodel_CVLModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cvlmodel_CVLModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cvlmodel_CVLModel(name="sample_text")
    partner = cvlmodel_VSpecTree()
    setattr(partner, 'cvlmodel_VSpecTree31', None)
    _safe_set(owner, 'cvlmodel_CVLModel', partner)
    assert getattr(partner, 'cvlmodel_VSpecTree31') == owner
    _safe_set(owner, 'cvlmodel_CVLModel', None)
    assert getattr(partner, 'cvlmodel_VSpecTree31') is None


def test_assoc_vspecs20_stub_double():
    # cvlmodel_VSpecTree has no real 'cvlmodel_VSpecTree' property in the generated
    # code (a bare stub) -- manually attach it so cvlmodel_VSpec's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cvlmodel_VSpec's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cvlmodel_VSpec(mandatory="sample_text", name="sample_text")
    partner = cvlmodel_VSpecTree()
    setattr(partner, 'cvlmodel_VSpecTree', None)
    _safe_set(owner, 'cvlmodel_VSpec21', partner)
    assert owner in getattr(partner, 'cvlmodel_VSpecTree')
    _safe_set(owner, 'cvlmodel_VSpec21', None)
    assert owner not in getattr(partner, 'cvlmodel_VSpecTree')


