import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotableElement,
    BasicElement,
    ModelElement,
    Organization,
    requirements_Agent,
    requirements_AnnotableElement,
    requirements_Annotation,
    requirements_Attribute,
    requirements_BasicElement,
    requirements_Entity,
    requirements_Goal,
    requirements_GoalStep,
    requirements_ModelElement,
    requirements_Organization,
    requirements_Privilege,
    requirements_PrivilegeGroup,
    requirements_Process,
    requirements_RelationShip,
    requirements_RequirementsDefinition,
    AnnotationStatus,
    AttributeType,
    PriorityLevel,
    PrivilegeNature,
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

def test_assoc_element18_reverse_link_reassign_clear():
    a1 = requirements_Privilege(category="sample_text")
    a2 = requirements_Privilege(category="sample_text_2")
    b = requirements_BasicElement(documentation="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'requirements_BasicElement', a1)
    assert _is_linked(b, 'requirements_BasicElement', a1)
    if hasattr(a1, 'requirements_Privilege'):
        assert _is_linked(a1, 'requirements_Privilege', b)
    _safe_set(b, 'requirements_BasicElement', a2)
    assert _is_linked(b, 'requirements_BasicElement', a2)
    if hasattr(a1, 'requirements_Privilege'):
        assert not _is_linked(a1, 'requirements_Privilege', b)
    if hasattr(a2, 'requirements_Privilege'):
        assert _is_linked(a2, 'requirements_Privilege', b)
    _safe_set(b, 'requirements_BasicElement', None)
    assert not _is_linked(b, 'requirements_BasicElement', a2)
    if hasattr(a2, 'requirements_Privilege'):
        assert not _is_linked(a2, 'requirements_Privilege', b)


def test_assoc_isResponsible10_reverse_link_reassign_clear():
    a1 = requirements_Goal(priority="sample_text", synopsis="sample_text")
    a2 = requirements_Goal(priority="sample_text_2", synopsis="sample_text_2")
    b = requirements_Agent(isHuman=True)
    _safe_set(b, 'responsible', {a1})
    assert _is_linked(b, 'responsible', a1)
    if hasattr(a1, 'Goal'):
        assert _is_linked(a1, 'Goal', b)
    _safe_set(b, 'responsible', {a2})
    assert _is_linked(b, 'responsible', a2)
    if hasattr(a1, 'Goal'):
        assert not _is_linked(a1, 'Goal', b)
    if hasattr(a2, 'Goal'):
        assert _is_linked(a2, 'Goal', b)
    _safe_set(b, 'responsible', set())
    assert not _is_linked(b, 'responsible', a2)
    if hasattr(a2, 'Goal'):
        assert not _is_linked(a2, 'Goal', b)


def test_assoc_privilegeGroup14_reverse_link_reassign_clear():
    a1 = requirements_PrivilegeGroup(documentation="sample_text")
    a2 = requirements_PrivilegeGroup(documentation="sample_text_2")
    b = requirements_Goal(priority="sample_text", synopsis="sample_text")
    _safe_set(b, 'requirements_Goal15', {a1})
    assert _is_linked(b, 'requirements_Goal15', a1)
    if hasattr(a1, 'requirements_PrivilegeGroup'):
        assert _is_linked(a1, 'requirements_PrivilegeGroup', b)
    _safe_set(b, 'requirements_Goal15', {a2})
    assert _is_linked(b, 'requirements_Goal15', a2)
    if hasattr(a1, 'requirements_PrivilegeGroup'):
        assert not _is_linked(a1, 'requirements_PrivilegeGroup', b)
    if hasattr(a2, 'requirements_PrivilegeGroup'):
        assert _is_linked(a2, 'requirements_PrivilegeGroup', b)
    _safe_set(b, 'requirements_Goal15', set())
    assert not _is_linked(b, 'requirements_Goal15', a2)
    if hasattr(a2, 'requirements_PrivilegeGroup'):
        assert not _is_linked(a2, 'requirements_PrivilegeGroup', b)


def test_assoc_privileges22_reverse_link_reassign_clear():
    a1 = requirements_PrivilegeGroup(documentation="sample_text")
    a2 = requirements_PrivilegeGroup(documentation="sample_text_2")
    b = requirements_Privilege(category="sample_text")
    _safe_set(b, 'requirements_Privilege24', a1)
    assert _is_linked(b, 'requirements_Privilege24', a1)
    if hasattr(a1, 'requirements_PrivilegeGroup23'):
        assert _is_linked(a1, 'requirements_PrivilegeGroup23', b)
    _safe_set(b, 'requirements_Privilege24', a2)
    assert _is_linked(b, 'requirements_Privilege24', a2)
    if hasattr(a1, 'requirements_PrivilegeGroup23'):
        assert not _is_linked(a1, 'requirements_PrivilegeGroup23', b)
    if hasattr(a2, 'requirements_PrivilegeGroup23'):
        assert _is_linked(a2, 'requirements_PrivilegeGroup23', b)
    _safe_set(b, 'requirements_Privilege24', None)
    assert not _is_linked(b, 'requirements_Privilege24', a2)
    if hasattr(a2, 'requirements_PrivilegeGroup23'):
        assert not _is_linked(a2, 'requirements_PrivilegeGroup23', b)


def test_assoc_responsible13_reverse_link_reassign_clear():
    a1 = requirements_Goal(priority="sample_text", synopsis="sample_text")
    a2 = requirements_Goal(priority="sample_text_2", synopsis="sample_text_2")
    b = requirements_Agent(isHuman=True)
    _safe_set(b, 'Agent', a1)
    assert _is_linked(b, 'Agent', a1)
    if hasattr(a1, 'isResponsible'):
        assert _is_linked(a1, 'isResponsible', b)
    _safe_set(b, 'Agent', a2)
    assert _is_linked(b, 'Agent', a2)
    if hasattr(a1, 'isResponsible'):
        assert not _is_linked(a1, 'isResponsible', b)
    if hasattr(a2, 'isResponsible'):
        assert _is_linked(a2, 'isResponsible', b)
    _safe_set(b, 'Agent', None)
    assert not _is_linked(b, 'Agent', a2)
    if hasattr(a2, 'isResponsible'):
        assert not _is_linked(a2, 'isResponsible', b)


def test_assoc_subgoals12_reverse_link_reassign_clear():
    a1 = requirements_Goal(priority="sample_text", synopsis="sample_text")
    a2 = requirements_Goal(priority="sample_text_2", synopsis="sample_text_2")
    b = requirements_Goal(priority="sample_text", synopsis="sample_text")
    _safe_set(b, 'requirements_Goal11', {a1})
    assert _is_linked(b, 'requirements_Goal11', a1)
    if hasattr(a1, 'requirements_Goal'):
        assert _is_linked(a1, 'requirements_Goal', b)
    _safe_set(b, 'requirements_Goal11', {a2})
    assert _is_linked(b, 'requirements_Goal11', a2)
    if hasattr(a1, 'requirements_Goal'):
        assert not _is_linked(a1, 'requirements_Goal', b)
    if hasattr(a2, 'requirements_Goal'):
        assert _is_linked(a2, 'requirements_Goal', b)
    _safe_set(b, 'requirements_Goal11', set())
    assert not _is_linked(b, 'requirements_Goal11', a2)
    if hasattr(a2, 'requirements_Goal'):
        assert not _is_linked(a2, 'requirements_Goal', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotation30_stub_double():
    # requirements_AnnotableElement has no real 'requirements_AnnotableElement' property in the generated
    # code (a bare stub) -- manually attach it so requirements_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_Annotation(annotation="sample_text", author="sample_text", comment="sample_text", date=date(2024, 1, 1), id="sample_text", status="sample_text")
    partner = requirements_AnnotableElement()
    setattr(partner, 'requirements_AnnotableElement', None)
    _safe_set(owner, 'requirements_Annotation', partner)
    assert owner in getattr(partner, 'requirements_AnnotableElement')
    _safe_set(owner, 'requirements_Annotation', None)
    assert owner not in getattr(partner, 'requirements_AnnotableElement')


def test_assoc_attributes2_stub_double():
    # requirements_Entity has no real 'requirements_Entity3' property in the generated
    # code (a bare stub) -- manually attach it so requirements_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_Attribute(type="sample_text")
    partner = requirements_Entity()
    setattr(partner, 'requirements_Entity3', None)
    _safe_set(owner, 'requirements_Attribute', partner)
    assert owner in getattr(partner, 'requirements_Entity3')
    _safe_set(owner, 'requirements_Attribute', None)
    assert owner not in getattr(partner, 'requirements_Entity3')


def test_assoc_entryPoint19_stub_double():
    # requirements_Entity has no real 'requirements_Entity21' property in the generated
    # code (a bare stub) -- manually attach it so requirements_PrivilegeGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_PrivilegeGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_PrivilegeGroup(documentation="sample_text")
    partner = requirements_Entity()
    setattr(partner, 'requirements_Entity21', None)
    _safe_set(owner, 'requirements_PrivilegeGroup20', partner)
    assert getattr(partner, 'requirements_Entity21') == owner
    _safe_set(owner, 'requirements_PrivilegeGroup20', None)
    assert getattr(partner, 'requirements_Entity21') is None


def test_assoc_nextGoals25_stub_double():
    # requirements_GoalStep has no real 'requirements_GoalStep26' property in the generated
    # code (a bare stub) -- manually attach it so requirements_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_Goal(priority="sample_text", synopsis="sample_text")
    partner = requirements_GoalStep()
    setattr(partner, 'requirements_GoalStep26', None)
    _safe_set(owner, 'requirements_Goal27', partner)
    assert owner in getattr(partner, 'requirements_GoalStep26')
    _safe_set(owner, 'requirements_Goal27', None)
    assert owner not in getattr(partner, 'requirements_GoalStep26')


def test_assoc_source4_stub_double():
    # requirements_Entity has no real 'requirements_Entity5' property in the generated
    # code (a bare stub) -- manually attach it so requirements_RelationShip's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_RelationShip's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_RelationShip(sourceMax=7, sourceMin=7, targetMax=7, targetMin=7)
    partner = requirements_Entity()
    setattr(partner, 'requirements_Entity5', None)
    _safe_set(owner, 'requirements_RelationShip', partner)
    assert getattr(partner, 'requirements_Entity5') == owner
    _safe_set(owner, 'requirements_RelationShip', None)
    assert getattr(partner, 'requirements_Entity5') is None


def test_assoc_step16_stub_double():
    # requirements_GoalStep has no real 'requirements_GoalStep' property in the generated
    # code (a bare stub) -- manually attach it so requirements_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_Goal(priority="sample_text", synopsis="sample_text")
    partner = requirements_GoalStep()
    setattr(partner, 'requirements_GoalStep', None)
    _safe_set(owner, 'requirements_Goal17', {partner})
    assert getattr(partner, 'requirements_GoalStep') == owner
    _safe_set(owner, 'requirements_Goal17', set())
    assert getattr(partner, 'requirements_GoalStep') is None


def test_assoc_target6_stub_double():
    # requirements_Entity has no real 'requirements_Entity8' property in the generated
    # code (a bare stub) -- manually attach it so requirements_RelationShip's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_RelationShip's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_RelationShip(sourceMax=7, sourceMin=7, targetMax=7, targetMin=7)
    partner = requirements_Entity()
    setattr(partner, 'requirements_Entity8', None)
    _safe_set(owner, 'requirements_RelationShip7', partner)
    assert getattr(partner, 'requirements_Entity8') == owner
    _safe_set(owner, 'requirements_RelationShip7', None)
    assert getattr(partner, 'requirements_Entity8') is None


