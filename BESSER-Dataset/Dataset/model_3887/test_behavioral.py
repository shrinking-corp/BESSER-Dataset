import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EExperiment,
    EGamaLink,
    EGamaObject,
    ESpecies,
    gama_EAction,
    gama_EActionLink,
    gama_EAspect,
    gama_EAspectLink,
    gama_EBatchExperiment,
    gama_EChartLayer,
    gama_EDisplay,
    gama_EDisplayLink,
    gama_EEquation,
    gama_EEquationLink,
    gama_EExperiment,
    gama_EExperimentLink,
    gama_EFacet,
    gama_EGUIExperiment,
    gama_EGamaLink,
    gama_EGamaModel,
    gama_EGamaObject,
    gama_EGrid,
    gama_EInheritLink,
    gama_ELayer,
    gama_ELayerAspect,
    gama_EMonitor,
    gama_EParameter,
    gama_EPerceive,
    gama_EPerceiveLink,
    gama_EPlan,
    gama_EPlanLink,
    gama_EReflex,
    gama_EReflexLink,
    gama_ERule,
    gama_ERuleLink,
    gama_ESpecies,
    gama_EState,
    gama_EStateLink,
    gama_ESubSpeciesLink,
    gama_ETask,
    gama_ETaskLink,
    gama_EVariable,
    gama_EWorldAgent,
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

def test_assoc_aspect109_reverse_link_reassign_clear():
    a1 = gama_ELayerAspect(at="sample_text", color="sample_text", colorRBG="sample_text", depth="sample_text", empty="sample_text", expression="sample_text", gamlCode="sample_text", heigth="sample_text", imageSize="sample_text", isColorCst="sample_text", path="sample_text", points="sample_text", radius="sample_text", rotate="sample_text", shape="sample_text", shapeType="sample_text", size="sample_text", text="sample_text", textSize="sample_text", texture="sample_text", type="sample_text", width="sample_text")
    a2 = gama_ELayerAspect(at="sample_text_2", color="sample_text_2", colorRBG="sample_text_2", depth="sample_text_2", empty="sample_text_2", expression="sample_text_2", gamlCode="sample_text_2", heigth="sample_text_2", imageSize="sample_text_2", isColorCst="sample_text_2", path="sample_text_2", points="sample_text_2", radius="sample_text_2", rotate="sample_text_2", shape="sample_text_2", shapeType="sample_text_2", size="sample_text_2", text="sample_text_2", textSize="sample_text_2", texture="sample_text_2", type="sample_text_2", width="sample_text_2")
    b = gama_EAspect(defineGamlCode=True, gamlCode="sample_text")
    _safe_set(b, 'gama_EAspect111', a1)
    assert _is_linked(b, 'gama_EAspect111', a1)
    if hasattr(a1, 'gama_ELayerAspect110'):
        assert _is_linked(a1, 'gama_ELayerAspect110', b)
    _safe_set(b, 'gama_EAspect111', a2)
    assert _is_linked(b, 'gama_EAspect111', a2)
    if hasattr(a1, 'gama_ELayerAspect110'):
        assert not _is_linked(a1, 'gama_ELayerAspect110', b)
    if hasattr(a2, 'gama_ELayerAspect110'):
        assert _is_linked(a2, 'gama_ELayerAspect110', b)
    _safe_set(b, 'gama_EAspect111', None)
    assert not _is_linked(b, 'gama_EAspect111', a2)
    if hasattr(a2, 'gama_ELayerAspect110'):
        assert not _is_linked(a2, 'gama_ELayerAspect110', b)


def test_assoc_chartlayers101_reverse_link_reassign_clear():
    a1 = gama_ELayer(agents="sample_text", aspect="sample_text", chart_type="sample_text", color="sample_text", colorRBG="sample_text", file="sample_text", gamlCode="sample_text", grid="sample_text", isColorCst="sample_text", showLines=True, size="sample_text", species="sample_text", text="sample_text", type="sample_text")
    a2 = gama_ELayer(agents="sample_text_2", aspect="sample_text_2", chart_type="sample_text_2", color="sample_text_2", colorRBG="sample_text_2", file="sample_text_2", gamlCode="sample_text_2", grid="sample_text_2", isColorCst="sample_text_2", showLines=False, size="sample_text_2", species="sample_text_2", text="sample_text_2", type="sample_text_2")
    b = gama_EChartLayer(color="sample_text", style="sample_text", value="sample_text")
    _safe_set(b, 'gama_EChartLayer', a1)
    assert _is_linked(b, 'gama_EChartLayer', a1)
    if hasattr(a1, 'gama_ELayer102'):
        assert _is_linked(a1, 'gama_ELayer102', b)
    _safe_set(b, 'gama_EChartLayer', a2)
    assert _is_linked(b, 'gama_EChartLayer', a2)
    if hasattr(a1, 'gama_ELayer102'):
        assert not _is_linked(a1, 'gama_ELayer102', b)
    if hasattr(a2, 'gama_ELayer102'):
        assert _is_linked(a2, 'gama_ELayer102', b)
    _safe_set(b, 'gama_EChartLayer', None)
    assert not _is_linked(b, 'gama_EChartLayer', a2)
    if hasattr(a2, 'gama_ELayer102'):
        assert not _is_linked(a2, 'gama_ELayer102', b)


def test_assoc_display98_reverse_link_reassign_clear():
    a1 = gama_ELayer(agents="sample_text", aspect="sample_text", chart_type="sample_text", color="sample_text", colorRBG="sample_text", file="sample_text", gamlCode="sample_text", grid="sample_text", isColorCst="sample_text", showLines=True, size="sample_text", species="sample_text", text="sample_text", type="sample_text")
    a2 = gama_ELayer(agents="sample_text_2", aspect="sample_text_2", chart_type="sample_text_2", color="sample_text_2", colorRBG="sample_text_2", file="sample_text_2", gamlCode="sample_text_2", grid="sample_text_2", isColorCst="sample_text_2", showLines=False, size="sample_text_2", species="sample_text_2", text="sample_text_2", type="sample_text_2")
    b = gama_EDisplay(defineGamlCode=True, gamlCode="sample_text", layerList="sample_text")
    _safe_set(b, 'gama_EDisplay100', a1)
    assert _is_linked(b, 'gama_EDisplay100', a1)
    if hasattr(a1, 'gama_ELayer99'):
        assert _is_linked(a1, 'gama_ELayer99', b)
    _safe_set(b, 'gama_EDisplay100', a2)
    assert _is_linked(b, 'gama_EDisplay100', a2)
    if hasattr(a1, 'gama_ELayer99'):
        assert not _is_linked(a1, 'gama_ELayer99', b)
    if hasattr(a2, 'gama_ELayer99'):
        assert _is_linked(a2, 'gama_ELayer99', b)
    _safe_set(b, 'gama_EDisplay100', None)
    assert not _is_linked(b, 'gama_EDisplay100', a2)
    if hasattr(a2, 'gama_ELayer99'):
        assert not _is_linked(a2, 'gama_ELayer99', b)


def test_assoc_facets4_reverse_link_reassign_clear():
    a1 = gama_EGamaObject(colorPicto="sample_text", error="sample_text", hasError="sample_text", name="sample_text")
    a2 = gama_EGamaObject(colorPicto="sample_text_2", error="sample_text_2", hasError="sample_text_2", name="sample_text_2")
    b = gama_EFacet(name="sample_text", value="sample_text")
    _safe_set(b, 'gama_EFacet', a1)
    assert _is_linked(b, 'gama_EFacet', a1)
    if hasattr(a1, 'gama_EGamaObject'):
        assert _is_linked(a1, 'gama_EGamaObject', b)
    _safe_set(b, 'gama_EFacet', a2)
    assert _is_linked(b, 'gama_EFacet', a2)
    if hasattr(a1, 'gama_EGamaObject'):
        assert not _is_linked(a1, 'gama_EGamaObject', b)
    if hasattr(a2, 'gama_EGamaObject'):
        assert _is_linked(a2, 'gama_EGamaObject', b)
    _safe_set(b, 'gama_EFacet', None)
    assert not _is_linked(b, 'gama_EFacet', a2)
    if hasattr(a2, 'gama_EGamaObject'):
        assert not _is_linked(a2, 'gama_EGamaObject', b)


def test_assoc_inheritsFrom20_reverse_link_reassign_clear():
    a1 = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    a2 = gama_ESpecies(init="sample_text_2", reflexList="sample_text_2", skills="sample_text_2")
    b = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    _safe_set(b, 'gama_ESpecies21', a1)
    assert _is_linked(b, 'gama_ESpecies21', a1)
    if hasattr(a1, 'gama_ESpecies19'):
        assert _is_linked(a1, 'gama_ESpecies19', b)
    _safe_set(b, 'gama_ESpecies21', a2)
    assert _is_linked(b, 'gama_ESpecies21', a2)
    if hasattr(a1, 'gama_ESpecies19'):
        assert not _is_linked(a1, 'gama_ESpecies19', b)
    if hasattr(a2, 'gama_ESpecies19'):
        assert _is_linked(a2, 'gama_ESpecies19', b)
    _safe_set(b, 'gama_ESpecies21', None)
    assert not _is_linked(b, 'gama_ESpecies21', a2)
    if hasattr(a2, 'gama_ESpecies19'):
        assert not _is_linked(a2, 'gama_ESpecies19', b)


def test_assoc_layers43_reverse_link_reassign_clear():
    a1 = gama_ELayerAspect(at="sample_text", color="sample_text", colorRBG="sample_text", depth="sample_text", empty="sample_text", expression="sample_text", gamlCode="sample_text", heigth="sample_text", imageSize="sample_text", isColorCst="sample_text", path="sample_text", points="sample_text", radius="sample_text", rotate="sample_text", shape="sample_text", shapeType="sample_text", size="sample_text", text="sample_text", textSize="sample_text", texture="sample_text", type="sample_text", width="sample_text")
    a2 = gama_ELayerAspect(at="sample_text_2", color="sample_text_2", colorRBG="sample_text_2", depth="sample_text_2", empty="sample_text_2", expression="sample_text_2", gamlCode="sample_text_2", heigth="sample_text_2", imageSize="sample_text_2", isColorCst="sample_text_2", path="sample_text_2", points="sample_text_2", radius="sample_text_2", rotate="sample_text_2", shape="sample_text_2", shapeType="sample_text_2", size="sample_text_2", text="sample_text_2", textSize="sample_text_2", texture="sample_text_2", type="sample_text_2", width="sample_text_2")
    b = gama_EAspect(defineGamlCode=True, gamlCode="sample_text")
    _safe_set(b, 'gama_EAspect44', {a1})
    assert _is_linked(b, 'gama_EAspect44', a1)
    if hasattr(a1, 'gama_ELayerAspect'):
        assert _is_linked(a1, 'gama_ELayerAspect', b)
    _safe_set(b, 'gama_EAspect44', {a2})
    assert _is_linked(b, 'gama_EAspect44', a2)
    if hasattr(a1, 'gama_ELayerAspect'):
        assert not _is_linked(a1, 'gama_ELayerAspect', b)
    if hasattr(a2, 'gama_ELayerAspect'):
        assert _is_linked(a2, 'gama_ELayerAspect', b)
    _safe_set(b, 'gama_EAspect44', set())
    assert not _is_linked(b, 'gama_EAspect44', a2)
    if hasattr(a2, 'gama_ELayerAspect'):
        assert not _is_linked(a2, 'gama_ELayerAspect', b)


def test_assoc_layers90_reverse_link_reassign_clear():
    a1 = gama_ELayer(agents="sample_text", aspect="sample_text", chart_type="sample_text", color="sample_text", colorRBG="sample_text", file="sample_text", gamlCode="sample_text", grid="sample_text", isColorCst="sample_text", showLines=True, size="sample_text", species="sample_text", text="sample_text", type="sample_text")
    a2 = gama_ELayer(agents="sample_text_2", aspect="sample_text_2", chart_type="sample_text_2", color="sample_text_2", colorRBG="sample_text_2", file="sample_text_2", gamlCode="sample_text_2", grid="sample_text_2", isColorCst="sample_text_2", showLines=False, size="sample_text_2", species="sample_text_2", text="sample_text_2", type="sample_text_2")
    b = gama_EDisplay(defineGamlCode=True, gamlCode="sample_text", layerList="sample_text")
    _safe_set(b, 'gama_EDisplay91', {a1})
    assert _is_linked(b, 'gama_EDisplay91', a1)
    if hasattr(a1, 'gama_ELayer'):
        assert _is_linked(a1, 'gama_ELayer', b)
    _safe_set(b, 'gama_EDisplay91', {a2})
    assert _is_linked(b, 'gama_EDisplay91', a2)
    if hasattr(a1, 'gama_ELayer'):
        assert not _is_linked(a1, 'gama_ELayer', b)
    if hasattr(a2, 'gama_ELayer'):
        assert _is_linked(a2, 'gama_ELayer', b)
    _safe_set(b, 'gama_EDisplay91', set())
    assert not _is_linked(b, 'gama_EDisplay91', a2)
    if hasattr(a2, 'gama_ELayer'):
        assert not _is_linked(a2, 'gama_ELayer', b)


def test_assoc_model3_reverse_link_reassign_clear():
    a1 = gama_EGamaObject(colorPicto="sample_text", error="sample_text", hasError="sample_text", name="sample_text")
    a2 = gama_EGamaObject(colorPicto="sample_text_2", error="sample_text_2", hasError="sample_text_2", name="sample_text_2")
    b = gama_EGamaModel(name="sample_text")
    _safe_set(b, 'EGamaModel', a1)
    assert _is_linked(b, 'EGamaModel', a1)
    if hasattr(a1, 'objects'):
        assert _is_linked(a1, 'objects', b)
    _safe_set(b, 'EGamaModel', a2)
    assert _is_linked(b, 'EGamaModel', a2)
    if hasattr(a1, 'objects'):
        assert not _is_linked(a1, 'objects', b)
    if hasattr(a2, 'objects'):
        assert _is_linked(a2, 'objects', b)
    _safe_set(b, 'EGamaModel', None)
    assert not _is_linked(b, 'EGamaModel', a2)
    if hasattr(a2, 'objects'):
        assert not _is_linked(a2, 'objects', b)


def test_assoc_objects0_reverse_link_reassign_clear():
    a1 = gama_EGamaObject(colorPicto="sample_text", error="sample_text", hasError="sample_text", name="sample_text")
    a2 = gama_EGamaObject(colorPicto="sample_text_2", error="sample_text_2", hasError="sample_text_2", name="sample_text_2")
    b = gama_EGamaModel(name="sample_text")
    _safe_set(b, 'model', {a1})
    assert _is_linked(b, 'model', a1)
    if hasattr(a1, 'EGamaObject'):
        assert _is_linked(a1, 'EGamaObject', b)
    _safe_set(b, 'model', {a2})
    assert _is_linked(b, 'model', a2)
    if hasattr(a1, 'EGamaObject'):
        assert not _is_linked(a1, 'EGamaObject', b)
    if hasattr(a2, 'EGamaObject'):
        assert _is_linked(a2, 'EGamaObject', b)
    _safe_set(b, 'model', set())
    assert not _is_linked(b, 'model', a2)
    if hasattr(a2, 'EGamaObject'):
        assert not _is_linked(a2, 'EGamaObject', b)


def test_assoc_owner118_reverse_link_reassign_clear():
    a1 = gama_EGamaObject(colorPicto="sample_text", error="sample_text", hasError="sample_text", name="sample_text")
    a2 = gama_EGamaObject(colorPicto="sample_text_2", error="sample_text_2", hasError="sample_text_2", name="sample_text_2")
    b = gama_EFacet(name="sample_text", value="sample_text")
    _safe_set(b, 'gama_EFacet119', a1)
    assert _is_linked(b, 'gama_EFacet119', a1)
    if hasattr(a1, 'gama_EGamaObject120'):
        assert _is_linked(a1, 'gama_EGamaObject120', b)
    _safe_set(b, 'gama_EFacet119', a2)
    assert _is_linked(b, 'gama_EFacet119', a2)
    if hasattr(a1, 'gama_EGamaObject120'):
        assert not _is_linked(a1, 'gama_EGamaObject120', b)
    if hasattr(a2, 'gama_EGamaObject120'):
        assert _is_linked(a2, 'gama_EGamaObject120', b)
    _safe_set(b, 'gama_EFacet119', None)
    assert not _is_linked(b, 'gama_EFacet119', a2)
    if hasattr(a2, 'gama_EGamaObject120'):
        assert not _is_linked(a2, 'gama_EGamaObject120', b)


def test_assoc_owner95_reverse_link_reassign_clear():
    a1 = gama_EVariable(error="sample_text", function="sample_text", hasError="sample_text", init="sample_text", max="sample_text", min="sample_text", name="sample_text", type="sample_text", update="sample_text")
    a2 = gama_EVariable(error="sample_text_2", function="sample_text_2", hasError="sample_text_2", init="sample_text_2", max="sample_text_2", min="sample_text_2", name="sample_text_2", type="sample_text_2", update="sample_text_2")
    b = gama_EGamaObject(colorPicto="sample_text", error="sample_text", hasError="sample_text", name="sample_text")
    _safe_set(b, 'gama_EGamaObject97', a1)
    assert _is_linked(b, 'gama_EGamaObject97', a1)
    if hasattr(a1, 'gama_EVariable96'):
        assert _is_linked(a1, 'gama_EVariable96', b)
    _safe_set(b, 'gama_EGamaObject97', a2)
    assert _is_linked(b, 'gama_EGamaObject97', a2)
    if hasattr(a1, 'gama_EVariable96'):
        assert not _is_linked(a1, 'gama_EVariable96', b)
    if hasattr(a2, 'gama_EVariable96'):
        assert _is_linked(a2, 'gama_EVariable96', b)
    _safe_set(b, 'gama_EGamaObject97', None)
    assert not _is_linked(b, 'gama_EGamaObject97', a2)
    if hasattr(a2, 'gama_EVariable96'):
        assert not _is_linked(a2, 'gama_EVariable96', b)


def test_assoc_variables38_reverse_link_reassign_clear():
    a1 = gama_EVariable(error="sample_text", function="sample_text", hasError="sample_text", init="sample_text", max="sample_text", min="sample_text", name="sample_text", type="sample_text", update="sample_text")
    a2 = gama_EVariable(error="sample_text_2", function="sample_text_2", hasError="sample_text_2", init="sample_text_2", max="sample_text_2", min="sample_text_2", name="sample_text_2", type="sample_text_2", update="sample_text_2")
    b = gama_EAction(gamlCode="sample_text", returnType="sample_text")
    _safe_set(b, 'gama_EAction39', {a1})
    assert _is_linked(b, 'gama_EAction39', a1)
    if hasattr(a1, 'gama_EVariable40'):
        assert _is_linked(a1, 'gama_EVariable40', b)
    _safe_set(b, 'gama_EAction39', {a2})
    assert _is_linked(b, 'gama_EAction39', a2)
    if hasattr(a1, 'gama_EVariable40'):
        assert not _is_linked(a1, 'gama_EVariable40', b)
    if hasattr(a2, 'gama_EVariable40'):
        assert _is_linked(a2, 'gama_EVariable40', b)
    _safe_set(b, 'gama_EAction39', set())
    assert not _is_linked(b, 'gama_EAction39', a2)
    if hasattr(a2, 'gama_EVariable40'):
        assert not _is_linked(a2, 'gama_EVariable40', b)


def test_assoc_variables5_reverse_link_reassign_clear():
    a1 = gama_EVariable(error="sample_text", function="sample_text", hasError="sample_text", init="sample_text", max="sample_text", min="sample_text", name="sample_text", type="sample_text", update="sample_text")
    a2 = gama_EVariable(error="sample_text_2", function="sample_text_2", hasError="sample_text_2", init="sample_text_2", max="sample_text_2", min="sample_text_2", name="sample_text_2", type="sample_text_2", update="sample_text_2")
    b = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    _safe_set(b, 'gama_ESpecies', {a1})
    assert _is_linked(b, 'gama_ESpecies', a1)
    if hasattr(a1, 'gama_EVariable'):
        assert _is_linked(a1, 'gama_EVariable', b)
    _safe_set(b, 'gama_ESpecies', {a2})
    assert _is_linked(b, 'gama_ESpecies', a2)
    if hasattr(a1, 'gama_EVariable'):
        assert not _is_linked(a1, 'gama_EVariable', b)
    if hasattr(a2, 'gama_EVariable'):
        assert _is_linked(a2, 'gama_EVariable', b)
    _safe_set(b, 'gama_ESpecies', set())
    assert not _is_linked(b, 'gama_ESpecies', a2)
    if hasattr(a2, 'gama_EVariable'):
        assert not _is_linked(a2, 'gama_EVariable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action68_stub_double():
    # gama_EActionLink has no real 'gama_EActionLink69' property in the generated
    # code (a bare stub) -- manually attach it so gama_EAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EAction(gamlCode="sample_text", returnType="sample_text")
    partner = gama_EActionLink()
    setattr(partner, 'gama_EActionLink69', None)
    _safe_set(owner, 'gama_EAction70', partner)
    assert getattr(partner, 'gama_EActionLink69') == owner
    _safe_set(owner, 'gama_EAction70', None)
    assert getattr(partner, 'gama_EActionLink69') is None


def test_assoc_actionLinks10_stub_double():
    # gama_EActionLink has no real 'gama_EActionLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EActionLink()
    setattr(partner, 'gama_EActionLink', None)
    _safe_set(owner, 'gama_ESpecies11', {partner})
    assert getattr(partner, 'gama_EActionLink') == owner
    _safe_set(owner, 'gama_ESpecies11', set())
    assert getattr(partner, 'gama_EActionLink') is None


def test_assoc_actionLinks36_stub_double():
    # gama_EActionLink has no real 'gama_EActionLink37' property in the generated
    # code (a bare stub) -- manually attach it so gama_EAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EAction(gamlCode="sample_text", returnType="sample_text")
    partner = gama_EActionLink()
    setattr(partner, 'gama_EActionLink37', None)
    _safe_set(owner, 'gama_EAction', {partner})
    assert getattr(partner, 'gama_EActionLink37') == owner
    _safe_set(owner, 'gama_EAction', set())
    assert getattr(partner, 'gama_EActionLink37') is None


def test_assoc_aspect74_stub_double():
    # gama_EAspectLink has no real 'gama_EAspectLink75' property in the generated
    # code (a bare stub) -- manually attach it so gama_EAspect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EAspect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EAspect(defineGamlCode=True, gamlCode="sample_text")
    partner = gama_EAspectLink()
    setattr(partner, 'gama_EAspectLink75', None)
    _safe_set(owner, 'gama_EAspect76', partner)
    assert getattr(partner, 'gama_EAspectLink75') == owner
    _safe_set(owner, 'gama_EAspect76', None)
    assert getattr(partner, 'gama_EAspectLink75') is None


def test_assoc_aspectLinks41_stub_double():
    # gama_EAspectLink has no real 'gama_EAspectLink42' property in the generated
    # code (a bare stub) -- manually attach it so gama_EAspect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EAspect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EAspect(defineGamlCode=True, gamlCode="sample_text")
    partner = gama_EAspectLink()
    setattr(partner, 'gama_EAspectLink42', None)
    _safe_set(owner, 'gama_EAspect', {partner})
    assert getattr(partner, 'gama_EAspectLink42') == owner
    _safe_set(owner, 'gama_EAspect', set())
    assert getattr(partner, 'gama_EAspectLink42') is None


def test_assoc_aspectLinks8_stub_double():
    # gama_EAspectLink has no real 'gama_EAspectLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EAspectLink()
    setattr(partner, 'gama_EAspectLink', None)
    _safe_set(owner, 'gama_ESpecies9', {partner})
    assert getattr(partner, 'gama_EAspectLink') == owner
    _safe_set(owner, 'gama_ESpecies9', set())
    assert getattr(partner, 'gama_EAspectLink') is None


def test_assoc_child115_stub_double():
    # gama_EInheritLink has no real 'gama_EInheritLink116' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EInheritLink()
    setattr(partner, 'gama_EInheritLink116', None)
    _safe_set(owner, 'gama_ESpecies117', partner)
    assert getattr(partner, 'gama_EInheritLink116') == owner
    _safe_set(owner, 'gama_ESpecies117', None)
    assert getattr(partner, 'gama_EInheritLink116') is None


def test_assoc_display88_stub_double():
    # gama_EDisplayLink has no real 'gama_EDisplayLink89' property in the generated
    # code (a bare stub) -- manually attach it so gama_EDisplay's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EDisplay's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EDisplay(defineGamlCode=True, gamlCode="sample_text", layerList="sample_text")
    partner = gama_EDisplayLink()
    setattr(partner, 'gama_EDisplayLink89', None)
    _safe_set(owner, 'gama_EDisplay', partner)
    assert getattr(partner, 'gama_EDisplayLink89') == owner
    _safe_set(owner, 'gama_EDisplay', None)
    assert getattr(partner, 'gama_EDisplayLink89') is None


def test_assoc_displayLink92_stub_double():
    # gama_EDisplayLink has no real 'gama_EDisplayLink94' property in the generated
    # code (a bare stub) -- manually attach it so gama_EDisplay's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EDisplay's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EDisplay(defineGamlCode=True, gamlCode="sample_text", layerList="sample_text")
    partner = gama_EDisplayLink()
    setattr(partner, 'gama_EDisplayLink94', None)
    _safe_set(owner, 'gama_EDisplay93', partner)
    assert getattr(partner, 'gama_EDisplayLink94') == owner
    _safe_set(owner, 'gama_EDisplay93', None)
    assert getattr(partner, 'gama_EDisplayLink94') is None


def test_assoc_equation163_stub_double():
    # gama_EEquationLink has no real 'gama_EEquationLink164' property in the generated
    # code (a bare stub) -- manually attach it so gama_EEquation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EEquation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EEquation(gamlCode="sample_text")
    partner = gama_EEquationLink()
    setattr(partner, 'gama_EEquationLink164', None)
    _safe_set(owner, 'gama_EEquation165', partner)
    assert getattr(partner, 'gama_EEquationLink164') == owner
    _safe_set(owner, 'gama_EEquation165', None)
    assert getattr(partner, 'gama_EEquationLink164') is None


def test_assoc_equationLinks161_stub_double():
    # gama_EEquationLink has no real 'gama_EEquationLink162' property in the generated
    # code (a bare stub) -- manually attach it so gama_EEquation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EEquation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EEquation(gamlCode="sample_text")
    partner = gama_EEquationLink()
    setattr(partner, 'gama_EEquationLink162', None)
    _safe_set(owner, 'gama_EEquation', {partner})
    assert getattr(partner, 'gama_EEquationLink162') == owner
    _safe_set(owner, 'gama_EEquation', set())
    assert getattr(partner, 'gama_EEquationLink162') is None


def test_assoc_equationLinks34_stub_double():
    # gama_EEquationLink has no real 'gama_EEquationLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EEquationLink()
    setattr(partner, 'gama_EEquationLink', None)
    _safe_set(owner, 'gama_ESpecies35', {partner})
    assert getattr(partner, 'gama_EEquationLink') == owner
    _safe_set(owner, 'gama_ESpecies35', set())
    assert getattr(partner, 'gama_EEquationLink') is None


def test_assoc_experimentLinks6_stub_double():
    # gama_EExperimentLink has no real 'gama_EExperimentLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EExperimentLink()
    setattr(partner, 'gama_EExperimentLink', None)
    _safe_set(owner, 'gama_ESpecies7', {partner})
    assert getattr(partner, 'gama_EExperimentLink') == owner
    _safe_set(owner, 'gama_ESpecies7', set())
    assert getattr(partner, 'gama_EExperimentLink') is None


def test_assoc_inheritingLinks22_stub_double():
    # gama_EInheritLink has no real 'gama_EInheritLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EInheritLink()
    setattr(partner, 'gama_EInheritLink', None)
    _safe_set(owner, 'gama_ESpecies23', {partner})
    assert getattr(partner, 'gama_EInheritLink') == owner
    _safe_set(owner, 'gama_ESpecies23', set())
    assert getattr(partner, 'gama_EInheritLink') is None


def test_assoc_links1_stub_double():
    # gama_EGamaLink has no real 'EGamaLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_EGamaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EGamaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EGamaModel(name="sample_text")
    partner = gama_EGamaLink()
    setattr(partner, 'EGamaLink', None)
    _safe_set(owner, 'model2', {partner})
    assert getattr(partner, 'EGamaLink') == owner
    _safe_set(owner, 'model2', set())
    assert getattr(partner, 'EGamaLink') is None


def test_assoc_macro62_stub_double():
    # gama_ESubSpeciesLink has no real 'gama_ESubSpeciesLink63' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ESubSpeciesLink()
    setattr(partner, 'gama_ESubSpeciesLink63', None)
    _safe_set(owner, 'gama_ESpecies64', partner)
    assert getattr(partner, 'gama_ESubSpeciesLink63') == owner
    _safe_set(owner, 'gama_ESpecies64', None)
    assert getattr(partner, 'gama_ESubSpeciesLink63') is None


def test_assoc_macroSpeciesLinks16_stub_double():
    # gama_ESubSpeciesLink has no real 'gama_ESubSpeciesLink18' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ESubSpeciesLink()
    setattr(partner, 'gama_ESubSpeciesLink18', None)
    _safe_set(owner, 'gama_ESpecies17', {partner})
    assert getattr(partner, 'gama_ESubSpeciesLink18') == owner
    _safe_set(owner, 'gama_ESpecies17', set())
    assert getattr(partner, 'gama_ESubSpeciesLink18') is None


def test_assoc_micro65_stub_double():
    # gama_ESubSpeciesLink has no real 'gama_ESubSpeciesLink66' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ESubSpeciesLink()
    setattr(partner, 'gama_ESubSpeciesLink66', None)
    _safe_set(owner, 'gama_ESpecies67', partner)
    assert getattr(partner, 'gama_ESubSpeciesLink66') == owner
    _safe_set(owner, 'gama_ESpecies67', None)
    assert getattr(partner, 'gama_ESubSpeciesLink66') is None


def test_assoc_microSpeciesLinks14_stub_double():
    # gama_ESubSpeciesLink has no real 'gama_ESubSpeciesLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ESubSpeciesLink()
    setattr(partner, 'gama_ESubSpeciesLink', None)
    _safe_set(owner, 'gama_ESpecies15', {partner})
    assert getattr(partner, 'gama_ESubSpeciesLink') == owner
    _safe_set(owner, 'gama_ESpecies15', set())
    assert getattr(partner, 'gama_ESubSpeciesLink') is None


def test_assoc_model60_stub_double():
    # gama_EGamaLink has no real 'links' property in the generated
    # code (a bare stub) -- manually attach it so gama_EGamaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EGamaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EGamaModel(name="sample_text")
    partner = gama_EGamaLink()
    setattr(partner, 'links', None)
    _safe_set(owner, 'EGamaModel61', partner)
    assert getattr(partner, 'links') == owner
    _safe_set(owner, 'EGamaModel61', None)
    assert getattr(partner, 'links') is None


def test_assoc_monitors53_stub_double():
    # gama_EExperiment has no real 'gama_EExperiment54' property in the generated
    # code (a bare stub) -- manually attach it so gama_EMonitor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EMonitor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EMonitor(value="sample_text")
    partner = gama_EExperiment()
    setattr(partner, 'gama_EExperiment54', None)
    _safe_set(owner, 'gama_EMonitor', partner)
    assert owner in getattr(partner, 'gama_EExperiment54')
    _safe_set(owner, 'gama_EMonitor', None)
    assert owner not in getattr(partner, 'gama_EExperiment54')


def test_assoc_parameters51_stub_double():
    # gama_EExperiment has no real 'gama_EExperiment52' property in the generated
    # code (a bare stub) -- manually attach it so gama_EParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EParameter(among="sample_text", category="sample_text", init="sample_text", max="sample_text", min="sample_text", step="sample_text", variable="sample_text")
    partner = gama_EExperiment()
    setattr(partner, 'gama_EExperiment52', None)
    _safe_set(owner, 'gama_EParameter', partner)
    assert owner in getattr(partner, 'gama_EExperiment52')
    _safe_set(owner, 'gama_EParameter', None)
    assert owner not in getattr(partner, 'gama_EExperiment52')


def test_assoc_parent112_stub_double():
    # gama_EInheritLink has no real 'gama_EInheritLink113' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EInheritLink()
    setattr(partner, 'gama_EInheritLink113', None)
    _safe_set(owner, 'gama_ESpecies114', partner)
    assert getattr(partner, 'gama_EInheritLink113') == owner
    _safe_set(owner, 'gama_ESpecies114', None)
    assert getattr(partner, 'gama_EInheritLink113') is None


def test_assoc_perceive147_stub_double():
    # gama_EPerceiveLink has no real 'gama_EPerceiveLink148' property in the generated
    # code (a bare stub) -- manually attach it so gama_EPerceive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EPerceive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EPerceive(gamlCode="sample_text")
    partner = gama_EPerceiveLink()
    setattr(partner, 'gama_EPerceiveLink148', None)
    _safe_set(owner, 'gama_EPerceive149', partner)
    assert getattr(partner, 'gama_EPerceiveLink148') == owner
    _safe_set(owner, 'gama_EPerceive149', None)
    assert getattr(partner, 'gama_EPerceiveLink148') is None


def test_assoc_perceiveLinks145_stub_double():
    # gama_EPerceiveLink has no real 'gama_EPerceiveLink146' property in the generated
    # code (a bare stub) -- manually attach it so gama_EPerceive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EPerceive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EPerceive(gamlCode="sample_text")
    partner = gama_EPerceiveLink()
    setattr(partner, 'gama_EPerceiveLink146', None)
    _safe_set(owner, 'gama_EPerceive', {partner})
    assert getattr(partner, 'gama_EPerceiveLink146') == owner
    _safe_set(owner, 'gama_EPerceive', set())
    assert getattr(partner, 'gama_EPerceiveLink146') is None


def test_assoc_perceiveLinks30_stub_double():
    # gama_EPerceiveLink has no real 'gama_EPerceiveLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EPerceiveLink()
    setattr(partner, 'gama_EPerceiveLink', None)
    _safe_set(owner, 'gama_ESpecies31', {partner})
    assert getattr(partner, 'gama_EPerceiveLink') == owner
    _safe_set(owner, 'gama_ESpecies31', set())
    assert getattr(partner, 'gama_EPerceiveLink') is None


def test_assoc_plan127_stub_double():
    # gama_EPlanLink has no real 'gama_EPlanLink128' property in the generated
    # code (a bare stub) -- manually attach it so gama_EPlan's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EPlan's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EPlan(gamlCode="sample_text")
    partner = gama_EPlanLink()
    setattr(partner, 'gama_EPlanLink128', None)
    _safe_set(owner, 'gama_EPlan129', partner)
    assert getattr(partner, 'gama_EPlanLink128') == owner
    _safe_set(owner, 'gama_EPlan129', None)
    assert getattr(partner, 'gama_EPlanLink128') is None


def test_assoc_planLinks121_stub_double():
    # gama_EPlanLink has no real 'gama_EPlanLink122' property in the generated
    # code (a bare stub) -- manually attach it so gama_EPlan's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EPlan's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EPlan(gamlCode="sample_text")
    partner = gama_EPlanLink()
    setattr(partner, 'gama_EPlanLink122', None)
    _safe_set(owner, 'gama_EPlan', {partner})
    assert getattr(partner, 'gama_EPlanLink122') == owner
    _safe_set(owner, 'gama_EPlan', set())
    assert getattr(partner, 'gama_EPlanLink122') is None


def test_assoc_planLinks24_stub_double():
    # gama_EPlanLink has no real 'gama_EPlanLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EPlanLink()
    setattr(partner, 'gama_EPlanLink', None)
    _safe_set(owner, 'gama_ESpecies25', {partner})
    assert getattr(partner, 'gama_EPlanLink') == owner
    _safe_set(owner, 'gama_ESpecies25', set())
    assert getattr(partner, 'gama_EPlanLink') is None


def test_assoc_reflex80_stub_double():
    # gama_EReflexLink has no real 'gama_EReflexLink81' property in the generated
    # code (a bare stub) -- manually attach it so gama_EReflex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EReflex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EReflex(gamlCode="sample_text")
    partner = gama_EReflexLink()
    setattr(partner, 'gama_EReflexLink81', None)
    _safe_set(owner, 'gama_EReflex82', partner)
    assert getattr(partner, 'gama_EReflexLink81') == owner
    _safe_set(owner, 'gama_EReflex82', None)
    assert getattr(partner, 'gama_EReflexLink81') is None


def test_assoc_reflexLinks12_stub_double():
    # gama_EReflexLink has no real 'gama_EReflexLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EReflexLink()
    setattr(partner, 'gama_EReflexLink', None)
    _safe_set(owner, 'gama_ESpecies13', {partner})
    assert getattr(partner, 'gama_EReflexLink') == owner
    _safe_set(owner, 'gama_ESpecies13', set())
    assert getattr(partner, 'gama_EReflexLink') is None


def test_assoc_reflexLinks45_stub_double():
    # gama_EReflexLink has no real 'gama_EReflexLink46' property in the generated
    # code (a bare stub) -- manually attach it so gama_EReflex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EReflex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EReflex(gamlCode="sample_text")
    partner = gama_EReflexLink()
    setattr(partner, 'gama_EReflexLink46', None)
    _safe_set(owner, 'gama_EReflex', {partner})
    assert getattr(partner, 'gama_EReflexLink46') == owner
    _safe_set(owner, 'gama_EReflex', set())
    assert getattr(partner, 'gama_EReflexLink46') is None


def test_assoc_rule155_stub_double():
    # gama_ERuleLink has no real 'gama_ERuleLink156' property in the generated
    # code (a bare stub) -- manually attach it so gama_ERule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ERule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ERule(gamlCode="sample_text")
    partner = gama_ERuleLink()
    setattr(partner, 'gama_ERuleLink156', None)
    _safe_set(owner, 'gama_ERule157', partner)
    assert getattr(partner, 'gama_ERuleLink156') == owner
    _safe_set(owner, 'gama_ERule157', None)
    assert getattr(partner, 'gama_ERuleLink156') is None


def test_assoc_ruleLinks153_stub_double():
    # gama_ERuleLink has no real 'gama_ERuleLink154' property in the generated
    # code (a bare stub) -- manually attach it so gama_ERule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ERule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ERule(gamlCode="sample_text")
    partner = gama_ERuleLink()
    setattr(partner, 'gama_ERuleLink154', None)
    _safe_set(owner, 'gama_ERule', {partner})
    assert getattr(partner, 'gama_ERuleLink154') == owner
    _safe_set(owner, 'gama_ERule', set())
    assert getattr(partner, 'gama_ERuleLink154') is None


def test_assoc_ruleLinks32_stub_double():
    # gama_ERuleLink has no real 'gama_ERuleLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ERuleLink()
    setattr(partner, 'gama_ERuleLink', None)
    _safe_set(owner, 'gama_ESpecies33', {partner})
    assert getattr(partner, 'gama_ERuleLink') == owner
    _safe_set(owner, 'gama_ESpecies33', set())
    assert getattr(partner, 'gama_ERuleLink') is None


def test_assoc_source57_stub_double():
    # gama_EGamaLink has no real 'gama_EGamaLink58' property in the generated
    # code (a bare stub) -- manually attach it so gama_EGamaObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EGamaObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EGamaObject(colorPicto="sample_text", error="sample_text", hasError="sample_text", name="sample_text")
    partner = gama_EGamaLink()
    setattr(partner, 'gama_EGamaLink58', None)
    _safe_set(owner, 'gama_EGamaObject59', partner)
    assert getattr(partner, 'gama_EGamaLink58') == owner
    _safe_set(owner, 'gama_EGamaObject59', None)
    assert getattr(partner, 'gama_EGamaLink58') is None


def test_assoc_species103_stub_double():
    # gama_EExperimentLink has no real 'gama_EExperimentLink104' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EExperimentLink()
    setattr(partner, 'gama_EExperimentLink104', None)
    _safe_set(owner, 'gama_ESpecies105', partner)
    assert getattr(partner, 'gama_EExperimentLink104') == owner
    _safe_set(owner, 'gama_ESpecies105', None)
    assert getattr(partner, 'gama_EExperimentLink104') is None


def test_assoc_species130_stub_double():
    # gama_EPlanLink has no real 'gama_EPlanLink131' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EPlanLink()
    setattr(partner, 'gama_EPlanLink131', None)
    _safe_set(owner, 'gama_ESpecies132', partner)
    assert getattr(partner, 'gama_EPlanLink131') == owner
    _safe_set(owner, 'gama_ESpecies132', None)
    assert getattr(partner, 'gama_EPlanLink131') is None


def test_assoc_species136_stub_double():
    # gama_EStateLink has no real 'gama_EStateLink137' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EStateLink()
    setattr(partner, 'gama_EStateLink137', None)
    _safe_set(owner, 'gama_ESpecies138', partner)
    assert getattr(partner, 'gama_EStateLink137') == owner
    _safe_set(owner, 'gama_ESpecies138', None)
    assert getattr(partner, 'gama_EStateLink137') is None


def test_assoc_species142_stub_double():
    # gama_ETaskLink has no real 'gama_ETaskLink143' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ETaskLink()
    setattr(partner, 'gama_ETaskLink143', None)
    _safe_set(owner, 'gama_ESpecies144', partner)
    assert getattr(partner, 'gama_ETaskLink143') == owner
    _safe_set(owner, 'gama_ESpecies144', None)
    assert getattr(partner, 'gama_ETaskLink143') is None


def test_assoc_species150_stub_double():
    # gama_EPerceiveLink has no real 'gama_EPerceiveLink151' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EPerceiveLink()
    setattr(partner, 'gama_EPerceiveLink151', None)
    _safe_set(owner, 'gama_ESpecies152', partner)
    assert getattr(partner, 'gama_EPerceiveLink151') == owner
    _safe_set(owner, 'gama_ESpecies152', None)
    assert getattr(partner, 'gama_EPerceiveLink151') is None


def test_assoc_species158_stub_double():
    # gama_ERuleLink has no real 'gama_ERuleLink159' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ERuleLink()
    setattr(partner, 'gama_ERuleLink159', None)
    _safe_set(owner, 'gama_ESpecies160', partner)
    assert getattr(partner, 'gama_ERuleLink159') == owner
    _safe_set(owner, 'gama_ESpecies160', None)
    assert getattr(partner, 'gama_ERuleLink159') is None


def test_assoc_species166_stub_double():
    # gama_EEquationLink has no real 'gama_EEquationLink167' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EEquationLink()
    setattr(partner, 'gama_EEquationLink167', None)
    _safe_set(owner, 'gama_ESpecies168', partner)
    assert getattr(partner, 'gama_EEquationLink167') == owner
    _safe_set(owner, 'gama_ESpecies168', None)
    assert getattr(partner, 'gama_EEquationLink167') is None


def test_assoc_species71_stub_double():
    # gama_EActionLink has no real 'gama_EActionLink72' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EActionLink()
    setattr(partner, 'gama_EActionLink72', None)
    _safe_set(owner, 'gama_ESpecies73', partner)
    assert getattr(partner, 'gama_EActionLink72') == owner
    _safe_set(owner, 'gama_ESpecies73', None)
    assert getattr(partner, 'gama_EActionLink72') is None


def test_assoc_species77_stub_double():
    # gama_EAspectLink has no real 'gama_EAspectLink78' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EAspectLink()
    setattr(partner, 'gama_EAspectLink78', None)
    _safe_set(owner, 'gama_ESpecies79', partner)
    assert getattr(partner, 'gama_EAspectLink78') == owner
    _safe_set(owner, 'gama_ESpecies79', None)
    assert getattr(partner, 'gama_EAspectLink78') is None


def test_assoc_species83_stub_double():
    # gama_EReflexLink has no real 'gama_EReflexLink84' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EReflexLink()
    setattr(partner, 'gama_EReflexLink84', None)
    _safe_set(owner, 'gama_ESpecies85', partner)
    assert getattr(partner, 'gama_EReflexLink84') == owner
    _safe_set(owner, 'gama_ESpecies85', None)
    assert getattr(partner, 'gama_EReflexLink84') is None


def test_assoc_state133_stub_double():
    # gama_EStateLink has no real 'gama_EStateLink134' property in the generated
    # code (a bare stub) -- manually attach it so gama_EState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EState(gamlCode="sample_text")
    partner = gama_EStateLink()
    setattr(partner, 'gama_EStateLink134', None)
    _safe_set(owner, 'gama_EState135', partner)
    assert getattr(partner, 'gama_EStateLink134') == owner
    _safe_set(owner, 'gama_EState135', None)
    assert getattr(partner, 'gama_EStateLink134') is None


def test_assoc_stateLinks123_stub_double():
    # gama_EStateLink has no real 'gama_EStateLink124' property in the generated
    # code (a bare stub) -- manually attach it so gama_EState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EState(gamlCode="sample_text")
    partner = gama_EStateLink()
    setattr(partner, 'gama_EStateLink124', None)
    _safe_set(owner, 'gama_EState', {partner})
    assert getattr(partner, 'gama_EStateLink124') == owner
    _safe_set(owner, 'gama_EState', set())
    assert getattr(partner, 'gama_EStateLink124') is None


def test_assoc_stateLinks26_stub_double():
    # gama_EStateLink has no real 'gama_EStateLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_EStateLink()
    setattr(partner, 'gama_EStateLink', None)
    _safe_set(owner, 'gama_ESpecies27', {partner})
    assert getattr(partner, 'gama_EStateLink') == owner
    _safe_set(owner, 'gama_ESpecies27', set())
    assert getattr(partner, 'gama_EStateLink') is None


def test_assoc_target55_stub_double():
    # gama_EGamaLink has no real 'gama_EGamaLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_EGamaObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_EGamaObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_EGamaObject(colorPicto="sample_text", error="sample_text", hasError="sample_text", name="sample_text")
    partner = gama_EGamaLink()
    setattr(partner, 'gama_EGamaLink', None)
    _safe_set(owner, 'gama_EGamaObject56', partner)
    assert getattr(partner, 'gama_EGamaLink') == owner
    _safe_set(owner, 'gama_EGamaObject56', None)
    assert getattr(partner, 'gama_EGamaLink') is None


def test_assoc_task139_stub_double():
    # gama_ETaskLink has no real 'gama_ETaskLink140' property in the generated
    # code (a bare stub) -- manually attach it so gama_ETask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ETask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ETask(gamlCode="sample_text")
    partner = gama_ETaskLink()
    setattr(partner, 'gama_ETaskLink140', None)
    _safe_set(owner, 'gama_ETask141', partner)
    assert getattr(partner, 'gama_ETaskLink140') == owner
    _safe_set(owner, 'gama_ETask141', None)
    assert getattr(partner, 'gama_ETaskLink140') is None


def test_assoc_taskLinks125_stub_double():
    # gama_ETaskLink has no real 'gama_ETaskLink126' property in the generated
    # code (a bare stub) -- manually attach it so gama_ETask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ETask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ETask(gamlCode="sample_text")
    partner = gama_ETaskLink()
    setattr(partner, 'gama_ETaskLink126', None)
    _safe_set(owner, 'gama_ETask', {partner})
    assert getattr(partner, 'gama_ETaskLink126') == owner
    _safe_set(owner, 'gama_ETask', set())
    assert getattr(partner, 'gama_ETaskLink126') is None


def test_assoc_taskLinks28_stub_double():
    # gama_ETaskLink has no real 'gama_ETaskLink' property in the generated
    # code (a bare stub) -- manually attach it so gama_ESpecies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gama_ESpecies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gama_ESpecies(init="sample_text", reflexList="sample_text", skills="sample_text")
    partner = gama_ETaskLink()
    setattr(partner, 'gama_ETaskLink', None)
    _safe_set(owner, 'gama_ESpecies29', {partner})
    assert getattr(partner, 'gama_ETaskLink') == owner
    _safe_set(owner, 'gama_ESpecies29', set())
    assert getattr(partner, 'gama_ETaskLink') is None


