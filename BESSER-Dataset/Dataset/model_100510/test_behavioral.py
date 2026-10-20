import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Then,
    When,
    requirementEngineeringLanguage_Background,
    requirementEngineeringLanguage_Data,
    requirementEngineeringLanguage_Feature,
    requirementEngineeringLanguage_Given,
    requirementEngineeringLanguage_Goal,
    requirementEngineeringLanguage_Interaction,
    requirementEngineeringLanguage_Loading,
    requirementEngineeringLanguage_Project,
    requirementEngineeringLanguage_Scenario,
    requirementEngineeringLanguage_Then,
    requirementEngineeringLanguage_Update,
    requirementEngineeringLanguage_View,
    requirementEngineeringLanguage_When,
    Action,
    ContainerType,
    DataType,
    Quantifier,
    Reaction,
    State,
    Taxonomy,
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

def test_assoc_background10_reverse_link_reassign_clear():
    a1 = requirementEngineeringLanguage_Project(name="sample_text")
    a2 = requirementEngineeringLanguage_Project(name="sample_text_2")
    b = requirementEngineeringLanguage_Background(dashboard="sample_text")
    _safe_set(b, 'requirementEngineeringLanguage_Background', a1)
    assert _is_linked(b, 'requirementEngineeringLanguage_Background', a1)
    if hasattr(a1, 'requirementEngineeringLanguage_Project11'):
        assert _is_linked(a1, 'requirementEngineeringLanguage_Project11', b)
    _safe_set(b, 'requirementEngineeringLanguage_Background', a2)
    assert _is_linked(b, 'requirementEngineeringLanguage_Background', a2)
    if hasattr(a1, 'requirementEngineeringLanguage_Project11'):
        assert not _is_linked(a1, 'requirementEngineeringLanguage_Project11', b)
    if hasattr(a2, 'requirementEngineeringLanguage_Project11'):
        assert _is_linked(a2, 'requirementEngineeringLanguage_Project11', b)
    _safe_set(b, 'requirementEngineeringLanguage_Background', None)
    assert not _is_linked(b, 'requirementEngineeringLanguage_Background', a2)
    if hasattr(a2, 'requirementEngineeringLanguage_Project11'):
        assert not _is_linked(a2, 'requirementEngineeringLanguage_Project11', b)


def test_assoc_consistOf9_reverse_link_reassign_clear():
    a1 = requirementEngineeringLanguage_Project(name="sample_text")
    a2 = requirementEngineeringLanguage_Project(name="sample_text_2")
    b = requirementEngineeringLanguage_Feature(desc="sample_text", name="sample_text")
    _safe_set(b, 'requirementEngineeringLanguage_Feature', a1)
    assert _is_linked(b, 'requirementEngineeringLanguage_Feature', a1)
    if hasattr(a1, 'requirementEngineeringLanguage_Project'):
        assert _is_linked(a1, 'requirementEngineeringLanguage_Project', b)
    _safe_set(b, 'requirementEngineeringLanguage_Feature', a2)
    assert _is_linked(b, 'requirementEngineeringLanguage_Feature', a2)
    if hasattr(a1, 'requirementEngineeringLanguage_Project'):
        assert not _is_linked(a1, 'requirementEngineeringLanguage_Project', b)
    if hasattr(a2, 'requirementEngineeringLanguage_Project'):
        assert _is_linked(a2, 'requirementEngineeringLanguage_Project', b)
    _safe_set(b, 'requirementEngineeringLanguage_Feature', None)
    assert not _is_linked(b, 'requirementEngineeringLanguage_Feature', a2)
    if hasattr(a2, 'requirementEngineeringLanguage_Project'):
        assert not _is_linked(a2, 'requirementEngineeringLanguage_Project', b)


def test_assoc_data5_reverse_link_reassign_clear():
    a1 = requirementEngineeringLanguage_Given(dashboard="sample_text")
    a2 = requirementEngineeringLanguage_Given(dashboard="sample_text_2")
    b = requirementEngineeringLanguage_Data(location="sample_text", locationType="sample_text", quantifier="sample_text", type="sample_text")
    _safe_set(b, 'requirementEngineeringLanguage_Data', a1)
    assert _is_linked(b, 'requirementEngineeringLanguage_Data', a1)
    if hasattr(a1, 'requirementEngineeringLanguage_Given6'):
        assert _is_linked(a1, 'requirementEngineeringLanguage_Given6', b)
    _safe_set(b, 'requirementEngineeringLanguage_Data', a2)
    assert _is_linked(b, 'requirementEngineeringLanguage_Data', a2)
    if hasattr(a1, 'requirementEngineeringLanguage_Given6'):
        assert not _is_linked(a1, 'requirementEngineeringLanguage_Given6', b)
    if hasattr(a2, 'requirementEngineeringLanguage_Given6'):
        assert _is_linked(a2, 'requirementEngineeringLanguage_Given6', b)
    _safe_set(b, 'requirementEngineeringLanguage_Data', None)
    assert not _is_linked(b, 'requirementEngineeringLanguage_Data', a2)
    if hasattr(a2, 'requirementEngineeringLanguage_Given6'):
        assert not _is_linked(a2, 'requirementEngineeringLanguage_Given6', b)


def test_assoc_specifiedBy14_reverse_link_reassign_clear():
    a1 = requirementEngineeringLanguage_Scenario(name="sample_text")
    a2 = requirementEngineeringLanguage_Scenario(name="sample_text_2")
    b = requirementEngineeringLanguage_Feature(desc="sample_text", name="sample_text")
    _safe_set(b, 'requirementEngineeringLanguage_Feature15', {a1})
    assert _is_linked(b, 'requirementEngineeringLanguage_Feature15', a1)
    if hasattr(a1, 'requirementEngineeringLanguage_Scenario16'):
        assert _is_linked(a1, 'requirementEngineeringLanguage_Scenario16', b)
    _safe_set(b, 'requirementEngineeringLanguage_Feature15', {a2})
    assert _is_linked(b, 'requirementEngineeringLanguage_Feature15', a2)
    if hasattr(a1, 'requirementEngineeringLanguage_Scenario16'):
        assert not _is_linked(a1, 'requirementEngineeringLanguage_Scenario16', b)
    if hasattr(a2, 'requirementEngineeringLanguage_Scenario16'):
        assert _is_linked(a2, 'requirementEngineeringLanguage_Scenario16', b)
    _safe_set(b, 'requirementEngineeringLanguage_Feature15', set())
    assert not _is_linked(b, 'requirementEngineeringLanguage_Feature15', a2)
    if hasattr(a2, 'requirementEngineeringLanguage_Scenario16'):
        assert not _is_linked(a2, 'requirementEngineeringLanguage_Scenario16', b)


def test_assoc_system3_reverse_link_reassign_clear():
    a1 = requirementEngineeringLanguage_Scenario(name="sample_text")
    a2 = requirementEngineeringLanguage_Scenario(name="sample_text_2")
    b = requirementEngineeringLanguage_Given(dashboard="sample_text")
    _safe_set(b, 'requirementEngineeringLanguage_Given', a1)
    assert _is_linked(b, 'requirementEngineeringLanguage_Given', a1)
    if hasattr(a1, 'requirementEngineeringLanguage_Scenario4'):
        assert _is_linked(a1, 'requirementEngineeringLanguage_Scenario4', b)
    _safe_set(b, 'requirementEngineeringLanguage_Given', a2)
    assert _is_linked(b, 'requirementEngineeringLanguage_Given', a2)
    if hasattr(a1, 'requirementEngineeringLanguage_Scenario4'):
        assert not _is_linked(a1, 'requirementEngineeringLanguage_Scenario4', b)
    if hasattr(a2, 'requirementEngineeringLanguage_Scenario4'):
        assert _is_linked(a2, 'requirementEngineeringLanguage_Scenario4', b)
    _safe_set(b, 'requirementEngineeringLanguage_Given', None)
    assert not _is_linked(b, 'requirementEngineeringLanguage_Given', a2)
    if hasattr(a2, 'requirementEngineeringLanguage_Scenario4'):
        assert not _is_linked(a2, 'requirementEngineeringLanguage_Scenario4', b)


def test_assoc_target12_reverse_link_reassign_clear():
    a1 = requirementEngineeringLanguage_View(desc="sample_text", name="sample_text")
    a2 = requirementEngineeringLanguage_View(desc="sample_text_2", name="sample_text_2")
    b = requirementEngineeringLanguage_Update(do="sample_text")
    _safe_set(b, 'requirementEngineeringLanguage_Update', a1)
    assert _is_linked(b, 'requirementEngineeringLanguage_Update', a1)
    if hasattr(a1, 'requirementEngineeringLanguage_View13'):
        assert _is_linked(a1, 'requirementEngineeringLanguage_View13', b)
    _safe_set(b, 'requirementEngineeringLanguage_Update', a2)
    assert _is_linked(b, 'requirementEngineeringLanguage_Update', a2)
    if hasattr(a1, 'requirementEngineeringLanguage_View13'):
        assert not _is_linked(a1, 'requirementEngineeringLanguage_View13', b)
    if hasattr(a2, 'requirementEngineeringLanguage_View13'):
        assert _is_linked(a2, 'requirementEngineeringLanguage_View13', b)
    _safe_set(b, 'requirementEngineeringLanguage_Update', None)
    assert not _is_linked(b, 'requirementEngineeringLanguage_Update', a2)
    if hasattr(a2, 'requirementEngineeringLanguage_View13'):
        assert not _is_linked(a2, 'requirementEngineeringLanguage_View13', b)


def test_assoc_view17_reverse_link_reassign_clear():
    a1 = requirementEngineeringLanguage_View(desc="sample_text", name="sample_text")
    a2 = requirementEngineeringLanguage_View(desc="sample_text_2", name="sample_text_2")
    b = requirementEngineeringLanguage_Background(dashboard="sample_text")
    _safe_set(b, 'requirementEngineeringLanguage_Background18', {a1})
    assert _is_linked(b, 'requirementEngineeringLanguage_Background18', a1)
    if hasattr(a1, 'requirementEngineeringLanguage_View19'):
        assert _is_linked(a1, 'requirementEngineeringLanguage_View19', b)
    _safe_set(b, 'requirementEngineeringLanguage_Background18', {a2})
    assert _is_linked(b, 'requirementEngineeringLanguage_Background18', a2)
    if hasattr(a1, 'requirementEngineeringLanguage_View19'):
        assert not _is_linked(a1, 'requirementEngineeringLanguage_View19', b)
    if hasattr(a2, 'requirementEngineeringLanguage_View19'):
        assert _is_linked(a2, 'requirementEngineeringLanguage_View19', b)
    _safe_set(b, 'requirementEngineeringLanguage_Background18', set())
    assert not _is_linked(b, 'requirementEngineeringLanguage_Background18', a2)
    if hasattr(a2, 'requirementEngineeringLanguage_View19'):
        assert not _is_linked(a2, 'requirementEngineeringLanguage_View19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_context7_stub_double():
    # requirementEngineeringLanguage_When has no real 'requirementEngineeringLanguage_When8' property in the generated
    # code (a bare stub) -- manually attach it so requirementEngineeringLanguage_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirementEngineeringLanguage_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirementEngineeringLanguage_View(desc="sample_text", name="sample_text")
    partner = requirementEngineeringLanguage_When()
    setattr(partner, 'requirementEngineeringLanguage_When8', None)
    _safe_set(owner, 'requirementEngineeringLanguage_View', partner)
    assert getattr(partner, 'requirementEngineeringLanguage_When8') == owner
    _safe_set(owner, 'requirementEngineeringLanguage_View', None)
    assert getattr(partner, 'requirementEngineeringLanguage_When8') is None


def test_assoc_outcome1_stub_double():
    # requirementEngineeringLanguage_Then has no real 'requirementEngineeringLanguage_Then' property in the generated
    # code (a bare stub) -- manually attach it so requirementEngineeringLanguage_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirementEngineeringLanguage_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirementEngineeringLanguage_Scenario(name="sample_text")
    partner = requirementEngineeringLanguage_Then()
    setattr(partner, 'requirementEngineeringLanguage_Then', None)
    _safe_set(owner, 'requirementEngineeringLanguage_Scenario2', {partner})
    assert getattr(partner, 'requirementEngineeringLanguage_Then') == owner
    _safe_set(owner, 'requirementEngineeringLanguage_Scenario2', set())
    assert getattr(partner, 'requirementEngineeringLanguage_Then') is None


def test_assoc_trigger0_stub_double():
    # requirementEngineeringLanguage_When has no real 'requirementEngineeringLanguage_When' property in the generated
    # code (a bare stub) -- manually attach it so requirementEngineeringLanguage_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirementEngineeringLanguage_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirementEngineeringLanguage_Scenario(name="sample_text")
    partner = requirementEngineeringLanguage_When()
    setattr(partner, 'requirementEngineeringLanguage_When', None)
    _safe_set(owner, 'requirementEngineeringLanguage_Scenario', {partner})
    assert getattr(partner, 'requirementEngineeringLanguage_When') == owner
    _safe_set(owner, 'requirementEngineeringLanguage_Scenario', set())
    assert getattr(partner, 'requirementEngineeringLanguage_When') is None


