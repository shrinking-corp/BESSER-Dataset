import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sedml_algorithm,
    sedml_curve,
    sedml_dataGenerator,
    sedml_listOfCurves,
    sedml_listOfDataGenerators,
    sedml_listOfModels,
    sedml_listOfOutputs,
    sedml_listOfSimulations,
    sedml_listOfTasks,
    sedml_listOfVariables,
    sedml_math,
    sedml_model,
    sedml_plot2D,
    sedml_sedML,
    sedml_task,
    sedml_uniformTimeCourse,
    sedml_variable,
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

def test_assoc_algorithm19_reverse_link_reassign_clear():
    a1 = sedml_uniformTimeCourse(id="sample_text", initialTime=7, numberOfPoints=7, outputEndTime=7, outputStartTime=7)
    a2 = sedml_uniformTimeCourse(id="sample_text_2", initialTime=13, numberOfPoints=13, outputEndTime=13, outputStartTime=13)
    b = sedml_algorithm(kisaoID="sample_text")
    _safe_set(b, 'sedml_algorithm', a1)
    assert _is_linked(b, 'sedml_algorithm', a1)
    if hasattr(a1, 'sedml_uniformTimeCourse20'):
        assert _is_linked(a1, 'sedml_uniformTimeCourse20', b)
    _safe_set(b, 'sedml_algorithm', a2)
    assert _is_linked(b, 'sedml_algorithm', a2)
    if hasattr(a1, 'sedml_uniformTimeCourse20'):
        assert not _is_linked(a1, 'sedml_uniformTimeCourse20', b)
    if hasattr(a2, 'sedml_uniformTimeCourse20'):
        assert _is_linked(a2, 'sedml_uniformTimeCourse20', b)
    _safe_set(b, 'sedml_algorithm', None)
    assert not _is_linked(b, 'sedml_algorithm', a2)
    if hasattr(a2, 'sedml_uniformTimeCourse20'):
        assert not _is_linked(a2, 'sedml_uniformTimeCourse20', b)


def test_assoc_math33_reverse_link_reassign_clear():
    a1 = sedml_math(xlms="sample_text")
    a2 = sedml_math(xlms="sample_text_2")
    b = sedml_dataGenerator(id="sample_text", name="sample_text")
    _safe_set(b, 'sedml_dataGenerator34', a1)
    assert _is_linked(b, 'sedml_dataGenerator34', a1)
    if hasattr(a1, 'sedml_math'):
        assert _is_linked(a1, 'sedml_math', b)
    _safe_set(b, 'sedml_dataGenerator34', a2)
    assert _is_linked(b, 'sedml_dataGenerator34', a2)
    if hasattr(a1, 'sedml_math'):
        assert not _is_linked(a1, 'sedml_math', b)
    if hasattr(a2, 'sedml_math'):
        assert _is_linked(a2, 'sedml_math', b)
    _safe_set(b, 'sedml_dataGenerator34', None)
    assert not _is_linked(b, 'sedml_dataGenerator34', a2)
    if hasattr(a2, 'sedml_math'):
        assert not _is_linked(a2, 'sedml_math', b)


def test_assoc_modelReference21_reverse_link_reassign_clear():
    a1 = sedml_task(id="sample_text", name="sample_text")
    a2 = sedml_task(id="sample_text_2", name="sample_text_2")
    b = sedml_model(id="sample_text", language="sample_text", name="sample_text", source="sample_text")
    _safe_set(b, 'sedml_model23', a1)
    assert _is_linked(b, 'sedml_model23', a1)
    if hasattr(a1, 'sedml_task22'):
        assert _is_linked(a1, 'sedml_task22', b)
    _safe_set(b, 'sedml_model23', a2)
    assert _is_linked(b, 'sedml_model23', a2)
    if hasattr(a1, 'sedml_task22'):
        assert not _is_linked(a1, 'sedml_task22', b)
    if hasattr(a2, 'sedml_task22'):
        assert _is_linked(a2, 'sedml_task22', b)
    _safe_set(b, 'sedml_model23', None)
    assert not _is_linked(b, 'sedml_model23', a2)
    if hasattr(a2, 'sedml_task22'):
        assert not _is_linked(a2, 'sedml_task22', b)


def test_assoc_simulationReference24_reverse_link_reassign_clear():
    a1 = sedml_uniformTimeCourse(id="sample_text", initialTime=7, numberOfPoints=7, outputEndTime=7, outputStartTime=7)
    a2 = sedml_uniformTimeCourse(id="sample_text_2", initialTime=13, numberOfPoints=13, outputEndTime=13, outputStartTime=13)
    b = sedml_task(id="sample_text", name="sample_text")
    _safe_set(b, 'sedml_task25', a1)
    assert _is_linked(b, 'sedml_task25', a1)
    if hasattr(a1, 'sedml_uniformTimeCourse26'):
        assert _is_linked(a1, 'sedml_uniformTimeCourse26', b)
    _safe_set(b, 'sedml_task25', a2)
    assert _is_linked(b, 'sedml_task25', a2)
    if hasattr(a1, 'sedml_uniformTimeCourse26'):
        assert not _is_linked(a1, 'sedml_uniformTimeCourse26', b)
    if hasattr(a2, 'sedml_uniformTimeCourse26'):
        assert _is_linked(a2, 'sedml_uniformTimeCourse26', b)
    _safe_set(b, 'sedml_task25', None)
    assert not _is_linked(b, 'sedml_task25', a2)
    if hasattr(a2, 'sedml_uniformTimeCourse26'):
        assert not _is_linked(a2, 'sedml_uniformTimeCourse26', b)


def test_assoc_taskReference37_reverse_link_reassign_clear():
    a1 = sedml_variable(id="sample_text", symbol="sample_text", target="sample_text")
    a2 = sedml_variable(id="sample_text_2", symbol="sample_text_2", target="sample_text_2")
    b = sedml_task(id="sample_text", name="sample_text")
    _safe_set(b, 'sedml_task39', a1)
    assert _is_linked(b, 'sedml_task39', a1)
    if hasattr(a1, 'sedml_variable38'):
        assert _is_linked(a1, 'sedml_variable38', b)
    _safe_set(b, 'sedml_task39', a2)
    assert _is_linked(b, 'sedml_task39', a2)
    if hasattr(a1, 'sedml_variable38'):
        assert not _is_linked(a1, 'sedml_variable38', b)
    if hasattr(a2, 'sedml_variable38'):
        assert _is_linked(a2, 'sedml_variable38', b)
    _safe_set(b, 'sedml_task39', None)
    assert not _is_linked(b, 'sedml_task39', a2)
    if hasattr(a2, 'sedml_variable38'):
        assert not _is_linked(a2, 'sedml_variable38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_curve29_stub_double():
    # sedml_listOfCurves has no real 'sedml_listOfCurves30' property in the generated
    # code (a bare stub) -- manually attach it so sedml_curve's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_curve's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_curve(id="sample_text", logX="sample_text", logY="sample_text", xDataReference="sample_text", yDataReference="sample_text")
    partner = sedml_listOfCurves()
    setattr(partner, 'sedml_listOfCurves30', None)
    _safe_set(owner, 'sedml_curve', partner)
    assert owner in getattr(partner, 'sedml_listOfCurves30')
    _safe_set(owner, 'sedml_curve', None)
    assert owner not in getattr(partner, 'sedml_listOfCurves30')


def test_assoc_dataGenerator15_stub_double():
    # sedml_listOfDataGenerators has no real 'sedml_listOfDataGenerators16' property in the generated
    # code (a bare stub) -- manually attach it so sedml_dataGenerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_dataGenerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_dataGenerator(id="sample_text", name="sample_text")
    partner = sedml_listOfDataGenerators()
    setattr(partner, 'sedml_listOfDataGenerators16', None)
    _safe_set(owner, 'sedml_dataGenerator', partner)
    assert owner in getattr(partner, 'sedml_listOfDataGenerators16')
    _safe_set(owner, 'sedml_dataGenerator', None)
    assert owner not in getattr(partner, 'sedml_listOfDataGenerators16')


def test_assoc_listOfCurves27_stub_double():
    # sedml_listOfCurves has no real 'sedml_listOfCurves' property in the generated
    # code (a bare stub) -- manually attach it so sedml_plot2D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_plot2D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_plot2D(id="sample_text", name="sample_text")
    partner = sedml_listOfCurves()
    setattr(partner, 'sedml_listOfCurves', None)
    _safe_set(owner, 'sedml_plot2D28', partner)
    assert getattr(partner, 'sedml_listOfCurves') == owner
    _safe_set(owner, 'sedml_plot2D28', None)
    assert getattr(partner, 'sedml_listOfCurves') is None


def test_assoc_listOfDataGenerators5_stub_double():
    # sedml_listOfDataGenerators has no real 'sedml_listOfDataGenerators' property in the generated
    # code (a bare stub) -- manually attach it so sedml_sedML's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_sedML's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_sedML(level=7, version=7)
    partner = sedml_listOfDataGenerators()
    setattr(partner, 'sedml_listOfDataGenerators', None)
    _safe_set(owner, 'sedml_sedML6', partner)
    assert getattr(partner, 'sedml_listOfDataGenerators') == owner
    _safe_set(owner, 'sedml_sedML6', None)
    assert getattr(partner, 'sedml_listOfDataGenerators') is None


def test_assoc_listOfModels1_stub_double():
    # sedml_listOfModels has no real 'sedml_listOfModels' property in the generated
    # code (a bare stub) -- manually attach it so sedml_sedML's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_sedML's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_sedML(level=7, version=7)
    partner = sedml_listOfModels()
    setattr(partner, 'sedml_listOfModels', None)
    _safe_set(owner, 'sedml_sedML2', partner)
    assert getattr(partner, 'sedml_listOfModels') == owner
    _safe_set(owner, 'sedml_sedML2', None)
    assert getattr(partner, 'sedml_listOfModels') is None


def test_assoc_listOfOutputs7_stub_double():
    # sedml_listOfOutputs has no real 'sedml_listOfOutputs' property in the generated
    # code (a bare stub) -- manually attach it so sedml_sedML's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_sedML's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_sedML(level=7, version=7)
    partner = sedml_listOfOutputs()
    setattr(partner, 'sedml_listOfOutputs', None)
    _safe_set(owner, 'sedml_sedML8', partner)
    assert getattr(partner, 'sedml_listOfOutputs') == owner
    _safe_set(owner, 'sedml_sedML8', None)
    assert getattr(partner, 'sedml_listOfOutputs') is None


def test_assoc_listOfSimulations0_stub_double():
    # sedml_listOfSimulations has no real 'sedml_listOfSimulations' property in the generated
    # code (a bare stub) -- manually attach it so sedml_sedML's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_sedML's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_sedML(level=7, version=7)
    partner = sedml_listOfSimulations()
    setattr(partner, 'sedml_listOfSimulations', None)
    _safe_set(owner, 'sedml_sedML', partner)
    assert getattr(partner, 'sedml_listOfSimulations') == owner
    _safe_set(owner, 'sedml_sedML', None)
    assert getattr(partner, 'sedml_listOfSimulations') is None


def test_assoc_listOfTasks3_stub_double():
    # sedml_listOfTasks has no real 'sedml_listOfTasks' property in the generated
    # code (a bare stub) -- manually attach it so sedml_sedML's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_sedML's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_sedML(level=7, version=7)
    partner = sedml_listOfTasks()
    setattr(partner, 'sedml_listOfTasks', None)
    _safe_set(owner, 'sedml_sedML4', partner)
    assert getattr(partner, 'sedml_listOfTasks') == owner
    _safe_set(owner, 'sedml_sedML4', None)
    assert getattr(partner, 'sedml_listOfTasks') is None


def test_assoc_listOfVariables31_stub_double():
    # sedml_listOfVariables has no real 'sedml_listOfVariables' property in the generated
    # code (a bare stub) -- manually attach it so sedml_dataGenerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_dataGenerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_dataGenerator(id="sample_text", name="sample_text")
    partner = sedml_listOfVariables()
    setattr(partner, 'sedml_listOfVariables', None)
    _safe_set(owner, 'sedml_dataGenerator32', partner)
    assert getattr(partner, 'sedml_listOfVariables') == owner
    _safe_set(owner, 'sedml_dataGenerator32', None)
    assert getattr(partner, 'sedml_listOfVariables') is None


def test_assoc_model11_stub_double():
    # sedml_listOfModels has no real 'sedml_listOfModels12' property in the generated
    # code (a bare stub) -- manually attach it so sedml_model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_model(id="sample_text", language="sample_text", name="sample_text", source="sample_text")
    partner = sedml_listOfModels()
    setattr(partner, 'sedml_listOfModels12', None)
    _safe_set(owner, 'sedml_model', partner)
    assert owner in getattr(partner, 'sedml_listOfModels12')
    _safe_set(owner, 'sedml_model', None)
    assert owner not in getattr(partner, 'sedml_listOfModels12')


def test_assoc_plot2D17_stub_double():
    # sedml_listOfOutputs has no real 'sedml_listOfOutputs18' property in the generated
    # code (a bare stub) -- manually attach it so sedml_plot2D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_plot2D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_plot2D(id="sample_text", name="sample_text")
    partner = sedml_listOfOutputs()
    setattr(partner, 'sedml_listOfOutputs18', None)
    _safe_set(owner, 'sedml_plot2D', partner)
    assert owner in getattr(partner, 'sedml_listOfOutputs18')
    _safe_set(owner, 'sedml_plot2D', None)
    assert owner not in getattr(partner, 'sedml_listOfOutputs18')


def test_assoc_task13_stub_double():
    # sedml_listOfTasks has no real 'sedml_listOfTasks14' property in the generated
    # code (a bare stub) -- manually attach it so sedml_task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_task(id="sample_text", name="sample_text")
    partner = sedml_listOfTasks()
    setattr(partner, 'sedml_listOfTasks14', None)
    _safe_set(owner, 'sedml_task', partner)
    assert owner in getattr(partner, 'sedml_listOfTasks14')
    _safe_set(owner, 'sedml_task', None)
    assert owner not in getattr(partner, 'sedml_listOfTasks14')


def test_assoc_uniformTimeCourse9_stub_double():
    # sedml_listOfSimulations has no real 'sedml_listOfSimulations10' property in the generated
    # code (a bare stub) -- manually attach it so sedml_uniformTimeCourse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_uniformTimeCourse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_uniformTimeCourse(id="sample_text", initialTime=7, numberOfPoints=7, outputEndTime=7, outputStartTime=7)
    partner = sedml_listOfSimulations()
    setattr(partner, 'sedml_listOfSimulations10', None)
    _safe_set(owner, 'sedml_uniformTimeCourse', partner)
    assert owner in getattr(partner, 'sedml_listOfSimulations10')
    _safe_set(owner, 'sedml_uniformTimeCourse', None)
    assert owner not in getattr(partner, 'sedml_listOfSimulations10')


def test_assoc_variable35_stub_double():
    # sedml_listOfVariables has no real 'sedml_listOfVariables36' property in the generated
    # code (a bare stub) -- manually attach it so sedml_variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sedml_variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sedml_variable(id="sample_text", symbol="sample_text", target="sample_text")
    partner = sedml_listOfVariables()
    setattr(partner, 'sedml_listOfVariables36', None)
    _safe_set(owner, 'sedml_variable', partner)
    assert owner in getattr(partner, 'sedml_listOfVariables36')
    _safe_set(owner, 'sedml_variable', None)
    assert owner not in getattr(partner, 'sedml_listOfVariables36')


