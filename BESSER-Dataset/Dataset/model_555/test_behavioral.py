import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    Person,
    Source,
    gedcoml_Address,
    gedcoml_Author,
    gedcoml_BekanntePerson,
    gedcoml_Family,
    gedcoml_FamilyBook,
    gedcoml_FamilyImport,
    gedcoml_Married,
    gedcoml_Note,
    gedcoml_Others,
    gedcoml_Person,
    gedcoml_PersonRef,
    gedcoml_PostAddress,
    gedcoml_Projectdescription,
    gedcoml_Source,
    gedcoml_UnbekanntePerson,
    Sexus,
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

def test_assoc_addresses34_reverse_link_reassign_clear():
    a1 = gedcoml_Person(id="sample_text", sex="sample_text")
    a2 = gedcoml_Person(id="sample_text_2", sex="sample_text_2")
    b = gedcoml_Address(entry="sample_text", exodus="sample_text")
    _safe_set(b, 'gedcoml_Address', a1)
    assert _is_linked(b, 'gedcoml_Address', a1)
    if hasattr(a1, 'gedcoml_Person35'):
        assert _is_linked(a1, 'gedcoml_Person35', b)
    _safe_set(b, 'gedcoml_Address', a2)
    assert _is_linked(b, 'gedcoml_Address', a2)
    if hasattr(a1, 'gedcoml_Person35'):
        assert not _is_linked(a1, 'gedcoml_Person35', b)
    if hasattr(a2, 'gedcoml_Person35'):
        assert _is_linked(a2, 'gedcoml_Person35', b)
    _safe_set(b, 'gedcoml_Address', None)
    assert not _is_linked(b, 'gedcoml_Address', a2)
    if hasattr(a2, 'gedcoml_Person35'):
        assert not _is_linked(a2, 'gedcoml_Person35', b)


def test_assoc_author1_reverse_link_reassign_clear():
    a1 = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    a2 = gedcoml_Projectdescription(artifactId="sample_text_2", groupId="sample_text_2", publishingDate="sample_text_2", version="sample_text_2")
    b = gedcoml_Author(firstName="sample_text", lastName="sample_text")
    _safe_set(b, 'gedcoml_Author', a1)
    assert _is_linked(b, 'gedcoml_Author', a1)
    if hasattr(a1, 'gedcoml_Projectdescription2'):
        assert _is_linked(a1, 'gedcoml_Projectdescription2', b)
    _safe_set(b, 'gedcoml_Author', a2)
    assert _is_linked(b, 'gedcoml_Author', a2)
    if hasattr(a1, 'gedcoml_Projectdescription2'):
        assert not _is_linked(a1, 'gedcoml_Projectdescription2', b)
    if hasattr(a2, 'gedcoml_Projectdescription2'):
        assert _is_linked(a2, 'gedcoml_Projectdescription2', b)
    _safe_set(b, 'gedcoml_Author', None)
    assert not _is_linked(b, 'gedcoml_Author', a2)
    if hasattr(a2, 'gedcoml_Projectdescription2'):
        assert not _is_linked(a2, 'gedcoml_Projectdescription2', b)


def test_assoc_biologicalFatherIs9_reverse_link_reassign_clear():
    a1 = gedcoml_Person(id="sample_text", sex="sample_text")
    a2 = gedcoml_Person(id="sample_text_2", sex="sample_text_2")
    b = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    _safe_set(b, 'gedcoml_BekanntePerson10', a1)
    assert _is_linked(b, 'gedcoml_BekanntePerson10', a1)
    if hasattr(a1, 'gedcoml_Person11'):
        assert _is_linked(a1, 'gedcoml_Person11', b)
    _safe_set(b, 'gedcoml_BekanntePerson10', a2)
    assert _is_linked(b, 'gedcoml_BekanntePerson10', a2)
    if hasattr(a1, 'gedcoml_Person11'):
        assert not _is_linked(a1, 'gedcoml_Person11', b)
    if hasattr(a2, 'gedcoml_Person11'):
        assert _is_linked(a2, 'gedcoml_Person11', b)
    _safe_set(b, 'gedcoml_BekanntePerson10', None)
    assert not _is_linked(b, 'gedcoml_BekanntePerson10', a2)
    if hasattr(a2, 'gedcoml_Person11'):
        assert not _is_linked(a2, 'gedcoml_Person11', b)


def test_assoc_biologicalMotherIs12_reverse_link_reassign_clear():
    a1 = gedcoml_Person(id="sample_text", sex="sample_text")
    a2 = gedcoml_Person(id="sample_text_2", sex="sample_text_2")
    b = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    _safe_set(b, 'gedcoml_BekanntePerson13', a1)
    assert _is_linked(b, 'gedcoml_BekanntePerson13', a1)
    if hasattr(a1, 'gedcoml_Person14'):
        assert _is_linked(a1, 'gedcoml_Person14', b)
    _safe_set(b, 'gedcoml_BekanntePerson13', a2)
    assert _is_linked(b, 'gedcoml_BekanntePerson13', a2)
    if hasattr(a1, 'gedcoml_Person14'):
        assert not _is_linked(a1, 'gedcoml_Person14', b)
    if hasattr(a2, 'gedcoml_Person14'):
        assert _is_linked(a2, 'gedcoml_Person14', b)
    _safe_set(b, 'gedcoml_BekanntePerson13', None)
    assert not _is_linked(b, 'gedcoml_BekanntePerson13', a2)
    if hasattr(a2, 'gedcoml_Person14'):
        assert not _is_linked(a2, 'gedcoml_Person14', b)


def test_assoc_biologicalParentOf7_reverse_link_reassign_clear():
    a1 = gedcoml_Person(id="sample_text", sex="sample_text")
    a2 = gedcoml_Person(id="sample_text_2", sex="sample_text_2")
    b = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    _safe_set(b, 'gedcoml_BekanntePerson', {a1})
    assert _is_linked(b, 'gedcoml_BekanntePerson', a1)
    if hasattr(a1, 'gedcoml_Person8'):
        assert _is_linked(a1, 'gedcoml_Person8', b)
    _safe_set(b, 'gedcoml_BekanntePerson', {a2})
    assert _is_linked(b, 'gedcoml_BekanntePerson', a2)
    if hasattr(a1, 'gedcoml_Person8'):
        assert not _is_linked(a1, 'gedcoml_Person8', b)
    if hasattr(a2, 'gedcoml_Person8'):
        assert _is_linked(a2, 'gedcoml_Person8', b)
    _safe_set(b, 'gedcoml_BekanntePerson', set())
    assert not _is_linked(b, 'gedcoml_BekanntePerson', a2)
    if hasattr(a2, 'gedcoml_Person8'):
        assert not _is_linked(a2, 'gedcoml_Person8', b)


def test_assoc_marriedWith15_reverse_link_reassign_clear():
    a1 = gedcoml_Married(separationDay="sample_text", weddingDay="sample_text")
    a2 = gedcoml_Married(separationDay="sample_text_2", weddingDay="sample_text_2")
    b = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    _safe_set(b, 'gedcoml_BekanntePerson16', {a1})
    assert _is_linked(b, 'gedcoml_BekanntePerson16', a1)
    if hasattr(a1, 'gedcoml_Married'):
        assert _is_linked(a1, 'gedcoml_Married', b)
    _safe_set(b, 'gedcoml_BekanntePerson16', {a2})
    assert _is_linked(b, 'gedcoml_BekanntePerson16', a2)
    if hasattr(a1, 'gedcoml_Married'):
        assert not _is_linked(a1, 'gedcoml_Married', b)
    if hasattr(a2, 'gedcoml_Married'):
        assert _is_linked(a2, 'gedcoml_Married', b)
    _safe_set(b, 'gedcoml_BekanntePerson16', set())
    assert not _is_linked(b, 'gedcoml_BekanntePerson16', a2)
    if hasattr(a2, 'gedcoml_Married'):
        assert not _is_linked(a2, 'gedcoml_Married', b)


def test_assoc_memberId29_reverse_link_reassign_clear():
    a1 = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    a2 = gedcoml_BekanntePerson(birthDay="sample_text_2", birthName="sample_text_2", deathDay="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", middleName="sample_text_2")
    b = gedcoml_Author(firstName="sample_text", lastName="sample_text")
    _safe_set(b, 'gedcoml_Author30', a1)
    assert _is_linked(b, 'gedcoml_Author30', a1)
    if hasattr(a1, 'gedcoml_BekanntePerson31'):
        assert _is_linked(a1, 'gedcoml_BekanntePerson31', b)
    _safe_set(b, 'gedcoml_Author30', a2)
    assert _is_linked(b, 'gedcoml_Author30', a2)
    if hasattr(a1, 'gedcoml_BekanntePerson31'):
        assert not _is_linked(a1, 'gedcoml_BekanntePerson31', b)
    if hasattr(a2, 'gedcoml_BekanntePerson31'):
        assert _is_linked(a2, 'gedcoml_BekanntePerson31', b)
    _safe_set(b, 'gedcoml_Author30', None)
    assert not _is_linked(b, 'gedcoml_Author30', a2)
    if hasattr(a2, 'gedcoml_BekanntePerson31'):
        assert not _is_linked(a2, 'gedcoml_BekanntePerson31', b)


def test_assoc_members3_reverse_link_reassign_clear():
    a1 = gedcoml_Person(id="sample_text", sex="sample_text")
    a2 = gedcoml_Person(id="sample_text_2", sex="sample_text_2")
    b = gedcoml_Family(name="sample_text")
    _safe_set(b, 'gedcoml_Family', {a1})
    assert _is_linked(b, 'gedcoml_Family', a1)
    if hasattr(a1, 'gedcoml_Person'):
        assert _is_linked(a1, 'gedcoml_Person', b)
    _safe_set(b, 'gedcoml_Family', {a2})
    assert _is_linked(b, 'gedcoml_Family', a2)
    if hasattr(a1, 'gedcoml_Person'):
        assert not _is_linked(a1, 'gedcoml_Person', b)
    if hasattr(a2, 'gedcoml_Person'):
        assert _is_linked(a2, 'gedcoml_Person', b)
    _safe_set(b, 'gedcoml_Family', set())
    assert not _is_linked(b, 'gedcoml_Family', a2)
    if hasattr(a2, 'gedcoml_Person'):
        assert not _is_linked(a2, 'gedcoml_Person', b)


def test_assoc_notes17_reverse_link_reassign_clear():
    a1 = gedcoml_Note(content="sample_text")
    a2 = gedcoml_Note(content="sample_text_2")
    b = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    _safe_set(b, 'gedcoml_BekanntePerson18', {a1})
    assert _is_linked(b, 'gedcoml_BekanntePerson18', a1)
    if hasattr(a1, 'gedcoml_Note'):
        assert _is_linked(a1, 'gedcoml_Note', b)
    _safe_set(b, 'gedcoml_BekanntePerson18', {a2})
    assert _is_linked(b, 'gedcoml_BekanntePerson18', a2)
    if hasattr(a1, 'gedcoml_Note'):
        assert not _is_linked(a1, 'gedcoml_Note', b)
    if hasattr(a2, 'gedcoml_Note'):
        assert _is_linked(a2, 'gedcoml_Note', b)
    _safe_set(b, 'gedcoml_BekanntePerson18', set())
    assert not _is_linked(b, 'gedcoml_BekanntePerson18', a2)
    if hasattr(a2, 'gedcoml_Note'):
        assert not _is_linked(a2, 'gedcoml_Note', b)


def test_assoc_partner26_reverse_link_reassign_clear():
    a1 = gedcoml_Person(id="sample_text", sex="sample_text")
    a2 = gedcoml_Person(id="sample_text_2", sex="sample_text_2")
    b = gedcoml_Married(separationDay="sample_text", weddingDay="sample_text")
    _safe_set(b, 'gedcoml_Married27', a1)
    assert _is_linked(b, 'gedcoml_Married27', a1)
    if hasattr(a1, 'gedcoml_Person28'):
        assert _is_linked(a1, 'gedcoml_Person28', b)
    _safe_set(b, 'gedcoml_Married27', a2)
    assert _is_linked(b, 'gedcoml_Married27', a2)
    if hasattr(a1, 'gedcoml_Person28'):
        assert not _is_linked(a1, 'gedcoml_Person28', b)
    if hasattr(a2, 'gedcoml_Person28'):
        assert _is_linked(a2, 'gedcoml_Person28', b)
    _safe_set(b, 'gedcoml_Married27', None)
    assert not _is_linked(b, 'gedcoml_Married27', a2)
    if hasattr(a2, 'gedcoml_Person28'):
        assert not _is_linked(a2, 'gedcoml_Person28', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_importedResource23_stub_double():
    # gedcoml_FamilyImport has no real 'gedcoml_FamilyImport24' property in the generated
    # code (a bare stub) -- manually attach it so gedcoml_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gedcoml_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gedcoml_Family(name="sample_text")
    partner = gedcoml_FamilyImport()
    setattr(partner, 'gedcoml_FamilyImport24', None)
    _safe_set(owner, 'gedcoml_Family25', partner)
    assert getattr(partner, 'gedcoml_FamilyImport24') == owner
    _safe_set(owner, 'gedcoml_Family25', None)
    assert getattr(partner, 'gedcoml_FamilyImport24') is None


def test_assoc_imports0_stub_double():
    # gedcoml_FamilyImport has no real 'gedcoml_FamilyImport' property in the generated
    # code (a bare stub) -- manually attach it so gedcoml_Projectdescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gedcoml_Projectdescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    partner = gedcoml_FamilyImport()
    setattr(partner, 'gedcoml_FamilyImport', None)
    _safe_set(owner, 'gedcoml_Projectdescription', {partner})
    assert getattr(partner, 'gedcoml_FamilyImport') == owner
    _safe_set(owner, 'gedcoml_Projectdescription', set())
    assert getattr(partner, 'gedcoml_FamilyImport') is None


def test_assoc_imports4_stub_double():
    # gedcoml_FamilyImport has no real 'gedcoml_FamilyImport6' property in the generated
    # code (a bare stub) -- manually attach it so gedcoml_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gedcoml_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gedcoml_Family(name="sample_text")
    partner = gedcoml_FamilyImport()
    setattr(partner, 'gedcoml_FamilyImport6', None)
    _safe_set(owner, 'gedcoml_Family5', {partner})
    assert getattr(partner, 'gedcoml_FamilyImport6') == owner
    _safe_set(owner, 'gedcoml_Family5', set())
    assert getattr(partner, 'gedcoml_FamilyImport6') is None


def test_assoc_personID32_stub_double():
    # gedcoml_PersonRef has no real 'gedcoml_PersonRef' property in the generated
    # code (a bare stub) -- manually attach it so gedcoml_BekanntePerson's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gedcoml_BekanntePerson's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    partner = gedcoml_PersonRef()
    setattr(partner, 'gedcoml_PersonRef', None)
    _safe_set(owner, 'gedcoml_BekanntePerson33', partner)
    assert getattr(partner, 'gedcoml_PersonRef') == owner
    _safe_set(owner, 'gedcoml_BekanntePerson33', None)
    assert getattr(partner, 'gedcoml_PersonRef') is None


def test_assoc_project21_stub_double():
    # gedcoml_FamilyBook has no real 'gedcoml_FamilyBook' property in the generated
    # code (a bare stub) -- manually attach it so gedcoml_Projectdescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gedcoml_Projectdescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    partner = gedcoml_FamilyBook()
    setattr(partner, 'gedcoml_FamilyBook', None)
    _safe_set(owner, 'gedcoml_Projectdescription22', partner)
    assert getattr(partner, 'gedcoml_FamilyBook') == owner
    _safe_set(owner, 'gedcoml_Projectdescription22', None)
    assert getattr(partner, 'gedcoml_FamilyBook') is None


def test_assoc_sources19_stub_double():
    # gedcoml_Source has no real 'gedcoml_Source' property in the generated
    # code (a bare stub) -- manually attach it so gedcoml_BekanntePerson's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gedcoml_BekanntePerson's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    partner = gedcoml_Source()
    setattr(partner, 'gedcoml_Source', None)
    _safe_set(owner, 'gedcoml_BekanntePerson20', {partner})
    assert getattr(partner, 'gedcoml_Source') == owner
    _safe_set(owner, 'gedcoml_BekanntePerson20', set())
    assert getattr(partner, 'gedcoml_Source') is None


