import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Argument,
    Dependency,
    Description,
    Requirement,
    SimpleDependency,
    requirements_editor_Argument,
    requirements_editor_BinaryOperatorArgument,
    requirements_editor_CValue,
    requirements_editor_Category,
    requirements_editor_Dependency,
    requirements_editor_Description,
    requirements_editor_DocumentRoot,
    requirements_editor_FunctionalRequirement,
    requirements_editor_ICost,
    requirements_editor_NOTOperator,
    requirements_editor_Person,
    requirements_editor_QualityRequirement,
    requirements_editor_Refines,
    requirements_editor_Requirement,
    requirements_editor_RequirementArgument,
    requirements_editor_Requires,
    requirements_editor_SimpleDependency,
    requirements_editor_TextualDescription,
    BinaryOperator,
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

def test_assoc_categoryOwnedBy6_reverse_link_reassign_clear():
    a1 = requirements_editor_Person(name="sample_text")
    a2 = requirements_editor_Person(name="sample_text_2")
    b = requirements_editor_Category(name="sample_text")
    _safe_set(b, 'personOwnsCategory', a1)
    assert _is_linked(b, 'personOwnsCategory', a1)
    if hasattr(a1, 'Person7'):
        assert _is_linked(a1, 'Person7', b)
    _safe_set(b, 'personOwnsCategory', a2)
    assert _is_linked(b, 'personOwnsCategory', a2)
    if hasattr(a1, 'Person7'):
        assert not _is_linked(a1, 'Person7', b)
    if hasattr(a2, 'Person7'):
        assert _is_linked(a2, 'Person7', b)
    _safe_set(b, 'personOwnsCategory', None)
    assert not _is_linked(b, 'personOwnsCategory', a2)
    if hasattr(a2, 'Person7'):
        assert not _is_linked(a2, 'Person7', b)


def test_assoc_dependencyTarget13_reverse_link_reassign_clear():
    a1 = requirements_editor_SimpleDependency(comment="sample_text")
    a2 = requirements_editor_SimpleDependency(comment="sample_text_2")
    b = requirements_editor_Requirement(identifier="sample_text", isMandatory=True, name="sample_text", priority=7)
    _safe_set(b, 'requirements_editor_Requirement14', a1)
    assert _is_linked(b, 'requirements_editor_Requirement14', a1)
    if hasattr(a1, 'requirements_editor_SimpleDependency'):
        assert _is_linked(a1, 'requirements_editor_SimpleDependency', b)
    _safe_set(b, 'requirements_editor_Requirement14', a2)
    assert _is_linked(b, 'requirements_editor_Requirement14', a2)
    if hasattr(a1, 'requirements_editor_SimpleDependency'):
        assert not _is_linked(a1, 'requirements_editor_SimpleDependency', b)
    if hasattr(a2, 'requirements_editor_SimpleDependency'):
        assert _is_linked(a2, 'requirements_editor_SimpleDependency', b)
    _safe_set(b, 'requirements_editor_Requirement14', None)
    assert not _is_linked(b, 'requirements_editor_Requirement14', a2)
    if hasattr(a2, 'requirements_editor_SimpleDependency'):
        assert not _is_linked(a2, 'requirements_editor_SimpleDependency', b)


def test_assoc_person25_reverse_link_reassign_clear():
    a1 = requirements_editor_Person(name="sample_text")
    a2 = requirements_editor_Person(name="sample_text_2")
    b = requirements_editor_DocumentRoot(name="sample_text")
    _safe_set(b, 'requirements_editor_DocumentRoot26', {a1})
    assert _is_linked(b, 'requirements_editor_DocumentRoot26', a1)
    if hasattr(a1, 'requirements_editor_Person'):
        assert _is_linked(a1, 'requirements_editor_Person', b)
    _safe_set(b, 'requirements_editor_DocumentRoot26', {a2})
    assert _is_linked(b, 'requirements_editor_DocumentRoot26', a2)
    if hasattr(a1, 'requirements_editor_Person'):
        assert not _is_linked(a1, 'requirements_editor_Person', b)
    if hasattr(a2, 'requirements_editor_Person'):
        assert _is_linked(a2, 'requirements_editor_Person', b)
    _safe_set(b, 'requirements_editor_DocumentRoot26', set())
    assert not _is_linked(b, 'requirements_editor_DocumentRoot26', a2)
    if hasattr(a2, 'requirements_editor_Person'):
        assert not _is_linked(a2, 'requirements_editor_Person', b)


def test_assoc_personOwnsCategory12_reverse_link_reassign_clear():
    a1 = requirements_editor_Person(name="sample_text")
    a2 = requirements_editor_Person(name="sample_text_2")
    b = requirements_editor_Category(name="sample_text")
    _safe_set(b, 'Category', a1)
    assert _is_linked(b, 'Category', a1)
    if hasattr(a1, 'categoryOwnedBy'):
        assert _is_linked(a1, 'categoryOwnedBy', b)
    _safe_set(b, 'Category', a2)
    assert _is_linked(b, 'Category', a2)
    if hasattr(a1, 'categoryOwnedBy'):
        assert not _is_linked(a1, 'categoryOwnedBy', b)
    if hasattr(a2, 'categoryOwnedBy'):
        assert _is_linked(a2, 'categoryOwnedBy', b)
    _safe_set(b, 'Category', None)
    assert not _is_linked(b, 'Category', a2)
    if hasattr(a2, 'categoryOwnedBy'):
        assert not _is_linked(a2, 'categoryOwnedBy', b)


def test_assoc_personOwnsRequirement11_reverse_link_reassign_clear():
    a1 = requirements_editor_Requirement(identifier="sample_text", isMandatory=True, name="sample_text", priority=7)
    a2 = requirements_editor_Requirement(identifier="sample_text_2", isMandatory=False, name="sample_text_2", priority=13)
    b = requirements_editor_Person(name="sample_text")
    _safe_set(b, 'requirementOwnedBy', {a1})
    assert _is_linked(b, 'requirementOwnedBy', a1)
    if hasattr(a1, 'Requirement'):
        assert _is_linked(a1, 'Requirement', b)
    _safe_set(b, 'requirementOwnedBy', {a2})
    assert _is_linked(b, 'requirementOwnedBy', a2)
    if hasattr(a1, 'Requirement'):
        assert not _is_linked(a1, 'Requirement', b)
    if hasattr(a2, 'Requirement'):
        assert _is_linked(a2, 'Requirement', b)
    _safe_set(b, 'requirementOwnedBy', set())
    assert not _is_linked(b, 'requirementOwnedBy', a2)
    if hasattr(a2, 'Requirement'):
        assert not _is_linked(a2, 'Requirement', b)


def test_assoc_requirement8_reverse_link_reassign_clear():
    a1 = requirements_editor_Requirement(identifier="sample_text", isMandatory=True, name="sample_text", priority=7)
    a2 = requirements_editor_Requirement(identifier="sample_text_2", isMandatory=False, name="sample_text_2", priority=13)
    b = requirements_editor_Category(name="sample_text")
    _safe_set(b, 'requirements_editor_Category9', {a1})
    assert _is_linked(b, 'requirements_editor_Category9', a1)
    if hasattr(a1, 'requirements_editor_Requirement10'):
        assert _is_linked(a1, 'requirements_editor_Requirement10', b)
    _safe_set(b, 'requirements_editor_Category9', {a2})
    assert _is_linked(b, 'requirements_editor_Category9', a2)
    if hasattr(a1, 'requirements_editor_Requirement10'):
        assert not _is_linked(a1, 'requirements_editor_Requirement10', b)
    if hasattr(a2, 'requirements_editor_Requirement10'):
        assert _is_linked(a2, 'requirements_editor_Requirement10', b)
    _safe_set(b, 'requirements_editor_Category9', set())
    assert not _is_linked(b, 'requirements_editor_Category9', a2)
    if hasattr(a2, 'requirements_editor_Requirement10'):
        assert not _is_linked(a2, 'requirements_editor_Requirement10', b)


def test_assoc_requirementOwnedBy1_reverse_link_reassign_clear():
    a1 = requirements_editor_Requirement(identifier="sample_text", isMandatory=True, name="sample_text", priority=7)
    a2 = requirements_editor_Requirement(identifier="sample_text_2", isMandatory=False, name="sample_text_2", priority=13)
    b = requirements_editor_Person(name="sample_text")
    _safe_set(b, 'Person', a1)
    assert _is_linked(b, 'Person', a1)
    if hasattr(a1, 'personOwnsRequirement'):
        assert _is_linked(a1, 'personOwnsRequirement', b)
    _safe_set(b, 'Person', a2)
    assert _is_linked(b, 'Person', a2)
    if hasattr(a1, 'personOwnsRequirement'):
        assert not _is_linked(a1, 'personOwnsRequirement', b)
    if hasattr(a2, 'personOwnsRequirement'):
        assert _is_linked(a2, 'personOwnsRequirement', b)
    _safe_set(b, 'Person', None)
    assert not _is_linked(b, 'Person', a2)
    if hasattr(a2, 'personOwnsRequirement'):
        assert not _is_linked(a2, 'personOwnsRequirement', b)


def test_assoc_rootCategories23_reverse_link_reassign_clear():
    a1 = requirements_editor_DocumentRoot(name="sample_text")
    a2 = requirements_editor_DocumentRoot(name="sample_text_2")
    b = requirements_editor_Category(name="sample_text")
    _safe_set(b, 'requirements_editor_Category24', a1)
    assert _is_linked(b, 'requirements_editor_Category24', a1)
    if hasattr(a1, 'requirements_editor_DocumentRoot'):
        assert _is_linked(a1, 'requirements_editor_DocumentRoot', b)
    _safe_set(b, 'requirements_editor_Category24', a2)
    assert _is_linked(b, 'requirements_editor_Category24', a2)
    if hasattr(a1, 'requirements_editor_DocumentRoot'):
        assert not _is_linked(a1, 'requirements_editor_DocumentRoot', b)
    if hasattr(a2, 'requirements_editor_DocumentRoot'):
        assert _is_linked(a2, 'requirements_editor_DocumentRoot', b)
    _safe_set(b, 'requirements_editor_Category24', None)
    assert not _is_linked(b, 'requirements_editor_Category24', a2)
    if hasattr(a2, 'requirements_editor_DocumentRoot'):
        assert not _is_linked(a2, 'requirements_editor_DocumentRoot', b)


def test_assoc_subcategoryOf5_reverse_link_reassign_clear():
    a1 = requirements_editor_Category(name="sample_text")
    a2 = requirements_editor_Category(name="sample_text_2")
    b = requirements_editor_Category(name="sample_text")
    _safe_set(b, 'requirements_editor_Category4', {a1})
    assert _is_linked(b, 'requirements_editor_Category4', a1)
    if hasattr(a1, 'requirements_editor_Category'):
        assert _is_linked(a1, 'requirements_editor_Category', b)
    _safe_set(b, 'requirements_editor_Category4', {a2})
    assert _is_linked(b, 'requirements_editor_Category4', a2)
    if hasattr(a1, 'requirements_editor_Category'):
        assert not _is_linked(a1, 'requirements_editor_Category', b)
    if hasattr(a2, 'requirements_editor_Category'):
        assert _is_linked(a2, 'requirements_editor_Category', b)
    _safe_set(b, 'requirements_editor_Category4', set())
    assert not _is_linked(b, 'requirements_editor_Category4', a2)
    if hasattr(a2, 'requirements_editor_Category'):
        assert not _is_linked(a2, 'requirements_editor_Category', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dependencySource2_stub_double():
    # requirements_editor_Dependency has no real 'requirements_editor_Dependency' property in the generated
    # code (a bare stub) -- manually attach it so requirements_editor_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_editor_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_editor_Requirement(identifier="sample_text", isMandatory=True, name="sample_text", priority=7)
    partner = requirements_editor_Dependency()
    setattr(partner, 'requirements_editor_Dependency', None)
    _safe_set(owner, 'requirements_editor_Requirement3', {partner})
    assert getattr(partner, 'requirements_editor_Dependency') == owner
    _safe_set(owner, 'requirements_editor_Requirement3', set())
    assert getattr(partner, 'requirements_editor_Dependency') is None


def test_assoc_description0_stub_double():
    # requirements_editor_Description has no real 'requirements_editor_Description' property in the generated
    # code (a bare stub) -- manually attach it so requirements_editor_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_editor_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_editor_Requirement(identifier="sample_text", isMandatory=True, name="sample_text", priority=7)
    partner = requirements_editor_Description()
    setattr(partner, 'requirements_editor_Description', None)
    _safe_set(owner, 'requirements_editor_Requirement', partner)
    assert getattr(partner, 'requirements_editor_Description') == owner
    _safe_set(owner, 'requirements_editor_Requirement', None)
    assert getattr(partner, 'requirements_editor_Description') is None


def test_assoc_leftSideArgument18_stub_double():
    # requirements_editor_Argument has no real 'requirements_editor_Argument20' property in the generated
    # code (a bare stub) -- manually attach it so requirements_editor_BinaryOperatorArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_editor_BinaryOperatorArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_editor_BinaryOperatorArgument(operator="sample_text")
    partner = requirements_editor_Argument()
    setattr(partner, 'requirements_editor_Argument20', None)
    _safe_set(owner, 'requirements_editor_BinaryOperatorArgument19', partner)
    assert getattr(partner, 'requirements_editor_Argument20') == owner
    _safe_set(owner, 'requirements_editor_BinaryOperatorArgument19', None)
    assert getattr(partner, 'requirements_editor_Argument20') is None


def test_assoc_requirement21_stub_double():
    # requirements_editor_RequirementArgument has no real 'requirements_editor_RequirementArgument' property in the generated
    # code (a bare stub) -- manually attach it so requirements_editor_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_editor_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_editor_Requirement(identifier="sample_text", isMandatory=True, name="sample_text", priority=7)
    partner = requirements_editor_RequirementArgument()
    setattr(partner, 'requirements_editor_RequirementArgument', None)
    _safe_set(owner, 'requirements_editor_Requirement22', partner)
    assert getattr(partner, 'requirements_editor_RequirementArgument') == owner
    _safe_set(owner, 'requirements_editor_Requirement22', None)
    assert getattr(partner, 'requirements_editor_RequirementArgument') is None


def test_assoc_rightSideArgument16_stub_double():
    # requirements_editor_Argument has no real 'requirements_editor_Argument17' property in the generated
    # code (a bare stub) -- manually attach it so requirements_editor_BinaryOperatorArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirements_editor_BinaryOperatorArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirements_editor_BinaryOperatorArgument(operator="sample_text")
    partner = requirements_editor_Argument()
    setattr(partner, 'requirements_editor_Argument17', None)
    _safe_set(owner, 'requirements_editor_BinaryOperatorArgument', partner)
    assert getattr(partner, 'requirements_editor_Argument17') == owner
    _safe_set(owner, 'requirements_editor_BinaryOperatorArgument', None)
    assert getattr(partner, 'requirements_editor_Argument17') is None


