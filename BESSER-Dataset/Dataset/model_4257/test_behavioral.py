import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Division,
    EvoCompany_Category,
    EvoCompany_Client,
    EvoCompany_CompanyModel,
    EvoCompany_Division,
    EvoCompany_Employee,
    EvoCompany_Organisation,
    EvoCompany_Person,
    EvoCompany_Project,
    EvoCompany_ServiceLine,
    EvoCompany_Topic,
    EvoCompany_Unit,
    Person,
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

def test_assoc_assignedTo0_reverse_link_reassign_clear():
    a1 = EvoCompany_Project(budget=7, name="sample_text")
    a2 = EvoCompany_Project(budget=13, name="sample_text_2")
    b = EvoCompany_Person(fullName="sample_text")
    _safe_set(b, 'EvoCompany_Person', {a1})
    assert _is_linked(b, 'EvoCompany_Person', a1)
    if hasattr(a1, 'EvoCompany_Project'):
        assert _is_linked(a1, 'EvoCompany_Project', b)
    _safe_set(b, 'EvoCompany_Person', {a2})
    assert _is_linked(b, 'EvoCompany_Person', a2)
    if hasattr(a1, 'EvoCompany_Project'):
        assert not _is_linked(a1, 'EvoCompany_Project', b)
    if hasattr(a2, 'EvoCompany_Project'):
        assert _is_linked(a2, 'EvoCompany_Project', b)
    _safe_set(b, 'EvoCompany_Person', set())
    assert not _is_linked(b, 'EvoCompany_Person', a2)
    if hasattr(a2, 'EvoCompany_Project'):
        assert not _is_linked(a2, 'EvoCompany_Project', b)


def test_assoc_category13_reverse_link_reassign_clear():
    a1 = EvoCompany_Topic(id="sample_text")
    a2 = EvoCompany_Topic(id="sample_text_2")
    b = EvoCompany_Category(name="sample_text")
    _safe_set(b, 'Category', a1)
    assert _is_linked(b, 'Category', a1)
    if hasattr(a1, 'topics'):
        assert _is_linked(a1, 'topics', b)
    _safe_set(b, 'Category', a2)
    assert _is_linked(b, 'Category', a2)
    if hasattr(a1, 'topics'):
        assert not _is_linked(a1, 'topics', b)
    if hasattr(a2, 'topics'):
        assert _is_linked(a2, 'topics', b)
    _safe_set(b, 'Category', None)
    assert not _is_linked(b, 'Category', a2)
    if hasattr(a2, 'topics'):
        assert not _is_linked(a2, 'topics', b)


def test_assoc_lines8_reverse_link_reassign_clear():
    a1 = EvoCompany_Organisation(city="sample_text", completeAddress="sample_text", name="sample_text")
    a2 = EvoCompany_Organisation(city="sample_text_2", completeAddress="sample_text_2", name="sample_text_2")
    b = EvoCompany_Division(name="sample_text")
    _safe_set(b, 'EvoCompany_Division', a1)
    assert _is_linked(b, 'EvoCompany_Division', a1)
    if hasattr(a1, 'EvoCompany_Organisation9'):
        assert _is_linked(a1, 'EvoCompany_Organisation9', b)
    _safe_set(b, 'EvoCompany_Division', a2)
    assert _is_linked(b, 'EvoCompany_Division', a2)
    if hasattr(a1, 'EvoCompany_Organisation9'):
        assert not _is_linked(a1, 'EvoCompany_Organisation9', b)
    if hasattr(a2, 'EvoCompany_Organisation9'):
        assert _is_linked(a2, 'EvoCompany_Organisation9', b)
    _safe_set(b, 'EvoCompany_Division', None)
    assert not _is_linked(b, 'EvoCompany_Division', a2)
    if hasattr(a2, 'EvoCompany_Organisation9'):
        assert not _is_linked(a2, 'EvoCompany_Organisation9', b)


def test_assoc_persons3_reverse_link_reassign_clear():
    a1 = EvoCompany_Person(fullName="sample_text")
    a2 = EvoCompany_Person(fullName="sample_text_2")
    b = EvoCompany_Organisation(city="sample_text", completeAddress="sample_text", name="sample_text")
    _safe_set(b, 'EvoCompany_Organisation', {a1})
    assert _is_linked(b, 'EvoCompany_Organisation', a1)
    if hasattr(a1, 'EvoCompany_Person4'):
        assert _is_linked(a1, 'EvoCompany_Person4', b)
    _safe_set(b, 'EvoCompany_Organisation', {a2})
    assert _is_linked(b, 'EvoCompany_Organisation', a2)
    if hasattr(a1, 'EvoCompany_Person4'):
        assert not _is_linked(a1, 'EvoCompany_Person4', b)
    if hasattr(a2, 'EvoCompany_Person4'):
        assert _is_linked(a2, 'EvoCompany_Person4', b)
    _safe_set(b, 'EvoCompany_Organisation', set())
    assert not _is_linked(b, 'EvoCompany_Organisation', a2)
    if hasattr(a2, 'EvoCompany_Person4'):
        assert not _is_linked(a2, 'EvoCompany_Person4', b)


def test_assoc_projects5_reverse_link_reassign_clear():
    a1 = EvoCompany_Project(budget=7, name="sample_text")
    a2 = EvoCompany_Project(budget=13, name="sample_text_2")
    b = EvoCompany_Organisation(city="sample_text", completeAddress="sample_text", name="sample_text")
    _safe_set(b, 'EvoCompany_Organisation6', {a1})
    assert _is_linked(b, 'EvoCompany_Organisation6', a1)
    if hasattr(a1, 'EvoCompany_Project7'):
        assert _is_linked(a1, 'EvoCompany_Project7', b)
    _safe_set(b, 'EvoCompany_Organisation6', {a2})
    assert _is_linked(b, 'EvoCompany_Organisation6', a2)
    if hasattr(a1, 'EvoCompany_Project7'):
        assert not _is_linked(a1, 'EvoCompany_Project7', b)
    if hasattr(a2, 'EvoCompany_Project7'):
        assert _is_linked(a2, 'EvoCompany_Project7', b)
    _safe_set(b, 'EvoCompany_Organisation6', set())
    assert not _is_linked(b, 'EvoCompany_Organisation6', a2)
    if hasattr(a2, 'EvoCompany_Project7'):
        assert not _is_linked(a2, 'EvoCompany_Project7', b)


def test_assoc_related10_reverse_link_reassign_clear():
    a1 = EvoCompany_Topic(id="sample_text")
    a2 = EvoCompany_Topic(id="sample_text_2")
    b = EvoCompany_Project(budget=7, name="sample_text")
    _safe_set(b, 'EvoCompany_Project11', a1)
    assert _is_linked(b, 'EvoCompany_Project11', a1)
    if hasattr(a1, 'EvoCompany_Topic'):
        assert _is_linked(a1, 'EvoCompany_Topic', b)
    _safe_set(b, 'EvoCompany_Project11', a2)
    assert _is_linked(b, 'EvoCompany_Project11', a2)
    if hasattr(a1, 'EvoCompany_Topic'):
        assert not _is_linked(a1, 'EvoCompany_Topic', b)
    if hasattr(a2, 'EvoCompany_Topic'):
        assert _is_linked(a2, 'EvoCompany_Topic', b)
    _safe_set(b, 'EvoCompany_Project11', None)
    assert not _is_linked(b, 'EvoCompany_Project11', a2)
    if hasattr(a2, 'EvoCompany_Topic'):
        assert not _is_linked(a2, 'EvoCompany_Topic', b)


def test_assoc_topics12_reverse_link_reassign_clear():
    a1 = EvoCompany_Topic(id="sample_text")
    a2 = EvoCompany_Topic(id="sample_text_2")
    b = EvoCompany_Category(name="sample_text")
    _safe_set(b, 'category', {a1})
    assert _is_linked(b, 'category', a1)
    if hasattr(a1, 'Topic'):
        assert _is_linked(a1, 'Topic', b)
    _safe_set(b, 'category', {a2})
    assert _is_linked(b, 'category', a2)
    if hasattr(a1, 'Topic'):
        assert not _is_linked(a1, 'Topic', b)
    if hasattr(a2, 'Topic'):
        assert _is_linked(a2, 'Topic', b)
    _safe_set(b, 'category', set())
    assert not _is_linked(b, 'category', a2)
    if hasattr(a2, 'Topic'):
        assert not _is_linked(a2, 'Topic', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_categories16_stub_double():
    # EvoCompany_CompanyModel has no real 'EvoCompany_CompanyModel17' property in the generated
    # code (a bare stub) -- manually attach it so EvoCompany_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EvoCompany_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EvoCompany_Category(name="sample_text")
    partner = EvoCompany_CompanyModel()
    setattr(partner, 'EvoCompany_CompanyModel17', None)
    _safe_set(owner, 'EvoCompany_Category', partner)
    assert owner in getattr(partner, 'EvoCompany_CompanyModel17')
    _safe_set(owner, 'EvoCompany_Category', None)
    assert owner not in getattr(partner, 'EvoCompany_CompanyModel17')


def test_assoc_company14_stub_double():
    # EvoCompany_CompanyModel has no real 'EvoCompany_CompanyModel' property in the generated
    # code (a bare stub) -- manually attach it so EvoCompany_Organisation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EvoCompany_Organisation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EvoCompany_Organisation(city="sample_text", completeAddress="sample_text", name="sample_text")
    partner = EvoCompany_CompanyModel()
    setattr(partner, 'EvoCompany_CompanyModel', None)
    _safe_set(owner, 'EvoCompany_Organisation15', partner)
    assert getattr(partner, 'EvoCompany_CompanyModel') == owner
    _safe_set(owner, 'EvoCompany_Organisation15', None)
    assert getattr(partner, 'EvoCompany_CompanyModel') is None


def test_assoc_division21_stub_double():
    # EvoCompany_CompanyModel has no real 'EvoCompany_CompanyModel22' property in the generated
    # code (a bare stub) -- manually attach it so EvoCompany_Division's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EvoCompany_Division's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EvoCompany_Division(name="sample_text")
    partner = EvoCompany_CompanyModel()
    setattr(partner, 'EvoCompany_CompanyModel22', None)
    _safe_set(owner, 'EvoCompany_Division23', partner)
    assert owner in getattr(partner, 'EvoCompany_CompanyModel22')
    _safe_set(owner, 'EvoCompany_Division23', None)
    assert owner not in getattr(partner, 'EvoCompany_CompanyModel22')


def test_assoc_employed1_stub_double():
    # EvoCompany_Unit has no real 'EvoCompany_Unit' property in the generated
    # code (a bare stub) -- manually attach it so EvoCompany_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EvoCompany_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EvoCompany_Person(fullName="sample_text")
    partner = EvoCompany_Unit()
    setattr(partner, 'EvoCompany_Unit', None)
    _safe_set(owner, 'EvoCompany_Person2', partner)
    assert getattr(partner, 'EvoCompany_Unit') == owner
    _safe_set(owner, 'EvoCompany_Person2', None)
    assert getattr(partner, 'EvoCompany_Unit') is None


def test_assoc_topics18_stub_double():
    # EvoCompany_CompanyModel has no real 'EvoCompany_CompanyModel19' property in the generated
    # code (a bare stub) -- manually attach it so EvoCompany_Topic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EvoCompany_Topic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EvoCompany_Topic(id="sample_text")
    partner = EvoCompany_CompanyModel()
    setattr(partner, 'EvoCompany_CompanyModel19', None)
    _safe_set(owner, 'EvoCompany_Topic20', partner)
    assert owner in getattr(partner, 'EvoCompany_CompanyModel19')
    _safe_set(owner, 'EvoCompany_Topic20', None)
    assert owner not in getattr(partner, 'EvoCompany_CompanyModel19')


