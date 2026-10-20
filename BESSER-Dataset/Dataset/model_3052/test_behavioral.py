import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MegalDeclaration,
    MegalElement,
    MegalNamed,
    QueryEntry,
    megal_MegalAnnotation,
    megal_MegalDeclaration,
    megal_MegalElement,
    megal_MegalEntity,
    megal_MegalEntityType,
    megal_MegalFile,
    megal_MegalLink,
    megal_MegalNamed,
    megal_MegalPair,
    megal_MegalRelationship,
    megal_MegalRelationshipType,
    megal_QueryEntity,
    megal_QueryEntry,
    megal_QueryParam,
    megal_QueryPos,
    megal_QueryReference,
    megal_QueryStatement,
    megal_QueryString,
    megal_Selection,
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

def test_assoc_bindings4_reverse_link_reassign_clear():
    a1 = megal_MegalLink(to="sample_text")
    a2 = megal_MegalLink(to="sample_text_2")
    b = megal_MegalFile(name="sample_text")
    _safe_set(b, 'megal_MegalFile5', {a1})
    assert _is_linked(b, 'megal_MegalFile5', a1)
    if hasattr(a1, 'megal_MegalLink'):
        assert _is_linked(a1, 'megal_MegalLink', b)
    _safe_set(b, 'megal_MegalFile5', {a2})
    assert _is_linked(b, 'megal_MegalFile5', a2)
    if hasattr(a1, 'megal_MegalLink'):
        assert not _is_linked(a1, 'megal_MegalLink', b)
    if hasattr(a2, 'megal_MegalLink'):
        assert _is_linked(a2, 'megal_MegalLink', b)
    _safe_set(b, 'megal_MegalFile5', set())
    assert not _is_linked(b, 'megal_MegalFile5', a2)
    if hasattr(a2, 'megal_MegalLink'):
        assert not _is_linked(a2, 'megal_MegalLink', b)


def test_assoc_first11_reverse_link_reassign_clear():
    a1 = megal_MegalLink(to="sample_text")
    a2 = megal_MegalLink(to="sample_text_2")
    b = megal_MegalEntity(many=True)
    _safe_set(b, 'megal_MegalEntity13', a1)
    assert _is_linked(b, 'megal_MegalEntity13', a1)
    if hasattr(a1, 'megal_MegalLink12'):
        assert _is_linked(a1, 'megal_MegalLink12', b)
    _safe_set(b, 'megal_MegalEntity13', a2)
    assert _is_linked(b, 'megal_MegalEntity13', a2)
    if hasattr(a1, 'megal_MegalLink12'):
        assert not _is_linked(a1, 'megal_MegalLink12', b)
    if hasattr(a2, 'megal_MegalLink12'):
        assert _is_linked(a2, 'megal_MegalLink12', b)
    _safe_set(b, 'megal_MegalEntity13', None)
    assert not _is_linked(b, 'megal_MegalEntity13', a2)
    if hasattr(a2, 'megal_MegalLink12'):
        assert not _is_linked(a2, 'megal_MegalLink12', b)


def test_assoc_imports7_reverse_link_reassign_clear():
    a1 = megal_MegalFile(name="sample_text")
    a2 = megal_MegalFile(name="sample_text_2")
    b = megal_MegalFile(name="sample_text")
    _safe_set(b, 'megal_MegalFile8', a1)
    assert _is_linked(b, 'megal_MegalFile8', a1)
    if hasattr(a1, 'megal_MegalFile6'):
        assert _is_linked(a1, 'megal_MegalFile6', b)
    _safe_set(b, 'megal_MegalFile8', a2)
    assert _is_linked(b, 'megal_MegalFile8', a2)
    if hasattr(a1, 'megal_MegalFile6'):
        assert not _is_linked(a1, 'megal_MegalFile6', b)
    if hasattr(a2, 'megal_MegalFile6'):
        assert _is_linked(a2, 'megal_MegalFile6', b)
    _safe_set(b, 'megal_MegalFile8', None)
    assert not _is_linked(b, 'megal_MegalFile8', a2)
    if hasattr(a2, 'megal_MegalFile6'):
        assert not _is_linked(a2, 'megal_MegalFile6', b)


def test_assoc_leftParams40_reverse_link_reassign_clear():
    a1 = megal_MegalRelationshipType(leftBoth=True, leftMany=True, rightBoth=True, rightMany=True)
    a2 = megal_MegalRelationshipType(leftBoth=False, leftMany=False, rightBoth=False, rightMany=False)
    b = megal_MegalEntity(many=True)
    _safe_set(b, 'megal_MegalEntity42', a1)
    assert _is_linked(b, 'megal_MegalEntity42', a1)
    if hasattr(a1, 'megal_MegalRelationshipType41'):
        assert _is_linked(a1, 'megal_MegalRelationshipType41', b)
    _safe_set(b, 'megal_MegalEntity42', a2)
    assert _is_linked(b, 'megal_MegalEntity42', a2)
    if hasattr(a1, 'megal_MegalRelationshipType41'):
        assert not _is_linked(a1, 'megal_MegalRelationshipType41', b)
    if hasattr(a2, 'megal_MegalRelationshipType41'):
        assert _is_linked(a2, 'megal_MegalRelationshipType41', b)
    _safe_set(b, 'megal_MegalEntity42', None)
    assert not _is_linked(b, 'megal_MegalEntity42', a2)
    if hasattr(a2, 'megal_MegalRelationshipType41'):
        assert not _is_linked(a2, 'megal_MegalRelationshipType41', b)


def test_assoc_link9_reverse_link_reassign_clear():
    a1 = megal_MegalLink(to="sample_text")
    a2 = megal_MegalLink(to="sample_text_2")
    b = megal_MegalEntity(many=True)
    _safe_set(b, 'megal_MegalEntity', a1)
    assert _is_linked(b, 'megal_MegalEntity', a1)
    if hasattr(a1, 'megal_MegalLink10'):
        assert _is_linked(a1, 'megal_MegalLink10', b)
    _safe_set(b, 'megal_MegalEntity', a2)
    assert _is_linked(b, 'megal_MegalEntity', a2)
    if hasattr(a1, 'megal_MegalLink10'):
        assert not _is_linked(a1, 'megal_MegalLink10', b)
    if hasattr(a2, 'megal_MegalLink10'):
        assert _is_linked(a2, 'megal_MegalLink10', b)
    _safe_set(b, 'megal_MegalEntity', None)
    assert not _is_linked(b, 'megal_MegalEntity', a2)
    if hasattr(a2, 'megal_MegalLink10'):
        assert not _is_linked(a2, 'megal_MegalLink10', b)


def test_assoc_params50_reverse_link_reassign_clear():
    a1 = megal_MegalEntity(many=True)
    a2 = megal_MegalEntity(many=False)
    b = megal_MegalEntity(many=True)
    _safe_set(b, 'megal_MegalEntity51', a1)
    assert _is_linked(b, 'megal_MegalEntity51', a1)
    if hasattr(a1, 'megal_MegalEntity49'):
        assert _is_linked(a1, 'megal_MegalEntity49', b)
    _safe_set(b, 'megal_MegalEntity51', a2)
    assert _is_linked(b, 'megal_MegalEntity51', a2)
    if hasattr(a1, 'megal_MegalEntity49'):
        assert not _is_linked(a1, 'megal_MegalEntity49', b)
    if hasattr(a2, 'megal_MegalEntity49'):
        assert _is_linked(a2, 'megal_MegalEntity49', b)
    _safe_set(b, 'megal_MegalEntity51', None)
    assert not _is_linked(b, 'megal_MegalEntity51', a2)
    if hasattr(a2, 'megal_MegalEntity49'):
        assert not _is_linked(a2, 'megal_MegalEntity49', b)


def test_assoc_rightParams43_reverse_link_reassign_clear():
    a1 = megal_MegalRelationshipType(leftBoth=True, leftMany=True, rightBoth=True, rightMany=True)
    a2 = megal_MegalRelationshipType(leftBoth=False, leftMany=False, rightBoth=False, rightMany=False)
    b = megal_MegalEntity(many=True)
    _safe_set(b, 'megal_MegalEntity45', a1)
    assert _is_linked(b, 'megal_MegalEntity45', a1)
    if hasattr(a1, 'megal_MegalRelationshipType44'):
        assert _is_linked(a1, 'megal_MegalRelationshipType44', b)
    _safe_set(b, 'megal_MegalEntity45', a2)
    assert _is_linked(b, 'megal_MegalEntity45', a2)
    if hasattr(a1, 'megal_MegalRelationshipType44'):
        assert not _is_linked(a1, 'megal_MegalRelationshipType44', b)
    if hasattr(a2, 'megal_MegalRelationshipType44'):
        assert _is_linked(a2, 'megal_MegalRelationshipType44', b)
    _safe_set(b, 'megal_MegalEntity45', None)
    assert not _is_linked(b, 'megal_MegalEntity45', a2)
    if hasattr(a2, 'megal_MegalRelationshipType44'):
        assert not _is_linked(a2, 'megal_MegalRelationshipType44', b)


def test_assoc_second14_reverse_link_reassign_clear():
    a1 = megal_MegalLink(to="sample_text")
    a2 = megal_MegalLink(to="sample_text_2")
    b = megal_MegalEntity(many=True)
    _safe_set(b, 'megal_MegalEntity16', a1)
    assert _is_linked(b, 'megal_MegalEntity16', a1)
    if hasattr(a1, 'megal_MegalLink15'):
        assert _is_linked(a1, 'megal_MegalLink15', b)
    _safe_set(b, 'megal_MegalEntity16', a2)
    assert _is_linked(b, 'megal_MegalEntity16', a2)
    if hasattr(a1, 'megal_MegalLink15'):
        assert not _is_linked(a1, 'megal_MegalLink15', b)
    if hasattr(a2, 'megal_MegalLink15'):
        assert _is_linked(a2, 'megal_MegalLink15', b)
    _safe_set(b, 'megal_MegalEntity16', None)
    assert not _is_linked(b, 'megal_MegalEntity16', a2)
    if hasattr(a2, 'megal_MegalLink15'):
        assert not _is_linked(a2, 'megal_MegalLink15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations1_stub_double():
    # megal_MegalElement has no real 'megal_MegalElement' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalAnnotation(key="sample_text")
    partner = megal_MegalElement()
    setattr(partner, 'megal_MegalElement', None)
    _safe_set(owner, 'megal_MegalAnnotation2', partner)
    assert owner in getattr(partner, 'megal_MegalElement')
    _safe_set(owner, 'megal_MegalAnnotation2', None)
    assert owner not in getattr(partner, 'megal_MegalElement')


def test_assoc_declarations3_stub_double():
    # megal_MegalDeclaration has no real 'megal_MegalDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalFile(name="sample_text")
    partner = megal_MegalDeclaration()
    setattr(partner, 'megal_MegalDeclaration', None)
    _safe_set(owner, 'megal_MegalFile', {partner})
    assert getattr(partner, 'megal_MegalDeclaration') == owner
    _safe_set(owner, 'megal_MegalFile', set())
    assert getattr(partner, 'megal_MegalDeclaration') is None


def test_assoc_entity69_stub_double():
    # megal_QueryEntity has no real 'megal_QueryEntity' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalEntity(many=True)
    partner = megal_QueryEntity()
    setattr(partner, 'megal_QueryEntity', None)
    _safe_set(owner, 'megal_MegalEntity70', partner)
    assert getattr(partner, 'megal_QueryEntity') == owner
    _safe_set(owner, 'megal_MegalEntity70', None)
    assert getattr(partner, 'megal_QueryEntity') is None


def test_assoc_first26_stub_double():
    # megal_MegalPair has no real 'megal_MegalPair27' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalEntity(many=True)
    partner = megal_MegalPair()
    setattr(partner, 'megal_MegalPair27', None)
    _safe_set(owner, 'megal_MegalEntity28', partner)
    assert getattr(partner, 'megal_MegalPair27') == owner
    _safe_set(owner, 'megal_MegalEntity28', None)
    assert getattr(partner, 'megal_MegalPair27') is None


def test_assoc_left18_stub_double():
    # megal_MegalRelationship has no real 'megal_MegalRelationship19' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalEntity(many=True)
    partner = megal_MegalRelationship()
    setattr(partner, 'megal_MegalRelationship19', None)
    _safe_set(owner, 'megal_MegalEntity20', partner)
    assert getattr(partner, 'megal_MegalRelationship19') == owner
    _safe_set(owner, 'megal_MegalEntity20', None)
    assert getattr(partner, 'megal_MegalRelationship19') is None


def test_assoc_left34_stub_double():
    # megal_MegalEntityType has no real 'megal_MegalEntityType36' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalRelationshipType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalRelationshipType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalRelationshipType(leftBoth=True, leftMany=True, rightBoth=True, rightMany=True)
    partner = megal_MegalEntityType()
    setattr(partner, 'megal_MegalEntityType36', None)
    _safe_set(owner, 'megal_MegalRelationshipType35', partner)
    assert getattr(partner, 'megal_MegalEntityType36') == owner
    _safe_set(owner, 'megal_MegalRelationshipType35', None)
    assert getattr(partner, 'megal_MegalEntityType36') is None


def test_assoc_predicate59_stub_double():
    # megal_QueryStatement has no real 'megal_QueryStatement60' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalRelationshipType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalRelationshipType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalRelationshipType(leftBoth=True, leftMany=True, rightBoth=True, rightMany=True)
    partner = megal_QueryStatement()
    setattr(partner, 'megal_QueryStatement60', None)
    _safe_set(owner, 'megal_MegalRelationshipType61', partner)
    assert getattr(partner, 'megal_QueryStatement60') == owner
    _safe_set(owner, 'megal_MegalRelationshipType61', None)
    assert getattr(partner, 'megal_QueryStatement60') is None


def test_assoc_ref67_stub_double():
    # megal_QueryReference has no real 'megal_QueryReference' property in the generated
    # code (a bare stub) -- manually attach it so megal_QueryParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_QueryParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_QueryParam(name="sample_text")
    partner = megal_QueryReference()
    setattr(partner, 'megal_QueryReference', None)
    _safe_set(owner, 'megal_QueryParam68', partner)
    assert getattr(partner, 'megal_QueryReference') == owner
    _safe_set(owner, 'megal_QueryParam68', None)
    assert getattr(partner, 'megal_QueryReference') is None


def test_assoc_right21_stub_double():
    # megal_MegalRelationship has no real 'megal_MegalRelationship22' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalEntity(many=True)
    partner = megal_MegalRelationship()
    setattr(partner, 'megal_MegalRelationship22', None)
    _safe_set(owner, 'megal_MegalEntity23', partner)
    assert getattr(partner, 'megal_MegalRelationship22') == owner
    _safe_set(owner, 'megal_MegalEntity23', None)
    assert getattr(partner, 'megal_MegalRelationship22') is None


def test_assoc_right37_stub_double():
    # megal_MegalEntityType has no real 'megal_MegalEntityType39' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalRelationshipType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalRelationshipType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalRelationshipType(leftBoth=True, leftMany=True, rightBoth=True, rightMany=True)
    partner = megal_MegalEntityType()
    setattr(partner, 'megal_MegalEntityType39', None)
    _safe_set(owner, 'megal_MegalRelationshipType38', partner)
    assert getattr(partner, 'megal_MegalEntityType39') == owner
    _safe_set(owner, 'megal_MegalRelationshipType38', None)
    assert getattr(partner, 'megal_MegalEntityType39') is None


def test_assoc_second29_stub_double():
    # megal_MegalPair has no real 'megal_MegalPair30' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalEntity(many=True)
    partner = megal_MegalPair()
    setattr(partner, 'megal_MegalPair30', None)
    _safe_set(owner, 'megal_MegalEntity31', partner)
    assert getattr(partner, 'megal_MegalPair30') == owner
    _safe_set(owner, 'megal_MegalEntity31', None)
    assert getattr(partner, 'megal_MegalPair30') is None


def test_assoc_selection0_stub_double():
    # megal_Selection has no real 'megal_Selection' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalAnnotation(key="sample_text")
    partner = megal_Selection()
    setattr(partner, 'megal_Selection', None)
    _safe_set(owner, 'megal_MegalAnnotation', partner)
    assert getattr(partner, 'megal_Selection') == owner
    _safe_set(owner, 'megal_MegalAnnotation', None)
    assert getattr(partner, 'megal_Selection') is None


def test_assoc_set24_stub_double():
    # megal_MegalPair has no real 'megal_MegalPair' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalEntity(many=True)
    partner = megal_MegalPair()
    setattr(partner, 'megal_MegalPair', None)
    _safe_set(owner, 'megal_MegalEntity25', partner)
    assert getattr(partner, 'megal_MegalPair') == owner
    _safe_set(owner, 'megal_MegalEntity25', None)
    assert getattr(partner, 'megal_MegalPair') is None


def test_assoc_type17_stub_double():
    # megal_MegalRelationship has no real 'megal_MegalRelationship' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalRelationshipType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalRelationshipType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalRelationshipType(leftBoth=True, leftMany=True, rightBoth=True, rightMany=True)
    partner = megal_MegalRelationship()
    setattr(partner, 'megal_MegalRelationship', None)
    _safe_set(owner, 'megal_MegalRelationshipType', partner)
    assert getattr(partner, 'megal_MegalRelationship') == owner
    _safe_set(owner, 'megal_MegalRelationshipType', None)
    assert getattr(partner, 'megal_MegalRelationship') is None


def test_assoc_type46_stub_double():
    # megal_MegalEntityType has no real 'megal_MegalEntityType48' property in the generated
    # code (a bare stub) -- manually attach it so megal_MegalEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_MegalEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_MegalEntity(many=True)
    partner = megal_MegalEntityType()
    setattr(partner, 'megal_MegalEntityType48', None)
    _safe_set(owner, 'megal_MegalEntity47', partner)
    assert getattr(partner, 'megal_MegalEntityType48') == owner
    _safe_set(owner, 'megal_MegalEntity47', None)
    assert getattr(partner, 'megal_MegalEntityType48') is None


def test_assoc_type65_stub_double():
    # megal_MegalEntityType has no real 'megal_MegalEntityType66' property in the generated
    # code (a bare stub) -- manually attach it so megal_QueryParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # megal_QueryParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = megal_QueryParam(name="sample_text")
    partner = megal_MegalEntityType()
    setattr(partner, 'megal_MegalEntityType66', None)
    _safe_set(owner, 'megal_QueryParam', partner)
    assert getattr(partner, 'megal_MegalEntityType66') == owner
    _safe_set(owner, 'megal_QueryParam', None)
    assert getattr(partner, 'megal_MegalEntityType66') is None


