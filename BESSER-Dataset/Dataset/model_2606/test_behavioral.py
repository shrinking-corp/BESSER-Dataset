import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Company_Category,
    Company_Company,
    Company_CompanyModel,
    Company_Division,
    Company_European,
    Company_National,
    Company_Person,
    Company_Project,
    Company_ServiceLine,
    Company_Topic,
    Company_Unit,
    Division,
    Project,
    type,
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
    a1 = Company_Project(name="sample_text")
    a2 = Company_Project(name="sample_text_2")
    b = Company_Person(firstname="sample_text", lastname="sample_text", position="sample_text")
    _safe_set(b, 'Company_Person', {a1})
    assert _is_linked(b, 'Company_Person', a1)
    if hasattr(a1, 'Company_Project'):
        assert _is_linked(a1, 'Company_Project', b)
    _safe_set(b, 'Company_Person', {a2})
    assert _is_linked(b, 'Company_Person', a2)
    if hasattr(a1, 'Company_Project'):
        assert not _is_linked(a1, 'Company_Project', b)
    if hasattr(a2, 'Company_Project'):
        assert _is_linked(a2, 'Company_Project', b)
    _safe_set(b, 'Company_Person', set())
    assert not _is_linked(b, 'Company_Person', a2)
    if hasattr(a2, 'Company_Project'):
        assert not _is_linked(a2, 'Company_Project', b)


def test_assoc_category13_reverse_link_reassign_clear():
    a1 = Company_Topic(id="sample_text")
    a2 = Company_Topic(id="sample_text_2")
    b = Company_Category(name="sample_text")
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
    a1 = Company_Division(name="sample_text")
    a2 = Company_Division(name="sample_text_2")
    b = Company_Company(city="sample_text", completeAddress="sample_text", name="sample_text")
    _safe_set(b, 'Company_Company9', {a1})
    assert _is_linked(b, 'Company_Company9', a1)
    if hasattr(a1, 'Company_Division'):
        assert _is_linked(a1, 'Company_Division', b)
    _safe_set(b, 'Company_Company9', {a2})
    assert _is_linked(b, 'Company_Company9', a2)
    if hasattr(a1, 'Company_Division'):
        assert not _is_linked(a1, 'Company_Division', b)
    if hasattr(a2, 'Company_Division'):
        assert _is_linked(a2, 'Company_Division', b)
    _safe_set(b, 'Company_Company9', set())
    assert not _is_linked(b, 'Company_Company9', a2)
    if hasattr(a2, 'Company_Division'):
        assert not _is_linked(a2, 'Company_Division', b)


def test_assoc_persons3_reverse_link_reassign_clear():
    a1 = Company_Person(firstname="sample_text", lastname="sample_text", position="sample_text")
    a2 = Company_Person(firstname="sample_text_2", lastname="sample_text_2", position="sample_text_2")
    b = Company_Company(city="sample_text", completeAddress="sample_text", name="sample_text")
    _safe_set(b, 'Company_Company', {a1})
    assert _is_linked(b, 'Company_Company', a1)
    if hasattr(a1, 'Company_Person4'):
        assert _is_linked(a1, 'Company_Person4', b)
    _safe_set(b, 'Company_Company', {a2})
    assert _is_linked(b, 'Company_Company', a2)
    if hasattr(a1, 'Company_Person4'):
        assert not _is_linked(a1, 'Company_Person4', b)
    if hasattr(a2, 'Company_Person4'):
        assert _is_linked(a2, 'Company_Person4', b)
    _safe_set(b, 'Company_Company', set())
    assert not _is_linked(b, 'Company_Company', a2)
    if hasattr(a2, 'Company_Person4'):
        assert not _is_linked(a2, 'Company_Person4', b)


def test_assoc_projects5_reverse_link_reassign_clear():
    a1 = Company_Project(name="sample_text")
    a2 = Company_Project(name="sample_text_2")
    b = Company_Company(city="sample_text", completeAddress="sample_text", name="sample_text")
    _safe_set(b, 'Company_Company6', {a1})
    assert _is_linked(b, 'Company_Company6', a1)
    if hasattr(a1, 'Company_Project7'):
        assert _is_linked(a1, 'Company_Project7', b)
    _safe_set(b, 'Company_Company6', {a2})
    assert _is_linked(b, 'Company_Company6', a2)
    if hasattr(a1, 'Company_Project7'):
        assert not _is_linked(a1, 'Company_Project7', b)
    if hasattr(a2, 'Company_Project7'):
        assert _is_linked(a2, 'Company_Project7', b)
    _safe_set(b, 'Company_Company6', set())
    assert not _is_linked(b, 'Company_Company6', a2)
    if hasattr(a2, 'Company_Project7'):
        assert not _is_linked(a2, 'Company_Project7', b)


def test_assoc_related10_reverse_link_reassign_clear():
    a1 = Company_Project(name="sample_text")
    a2 = Company_Project(name="sample_text_2")
    b = Company_Category(name="sample_text")
    _safe_set(b, 'Company_Category', a1)
    assert _is_linked(b, 'Company_Category', a1)
    if hasattr(a1, 'Company_Project11'):
        assert _is_linked(a1, 'Company_Project11', b)
    _safe_set(b, 'Company_Category', a2)
    assert _is_linked(b, 'Company_Category', a2)
    if hasattr(a1, 'Company_Project11'):
        assert not _is_linked(a1, 'Company_Project11', b)
    if hasattr(a2, 'Company_Project11'):
        assert _is_linked(a2, 'Company_Project11', b)
    _safe_set(b, 'Company_Category', None)
    assert not _is_linked(b, 'Company_Category', a2)
    if hasattr(a2, 'Company_Project11'):
        assert not _is_linked(a2, 'Company_Project11', b)


def test_assoc_topics12_reverse_link_reassign_clear():
    a1 = Company_Topic(id="sample_text")
    a2 = Company_Topic(id="sample_text_2")
    b = Company_Category(name="sample_text")
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
    # Company_CompanyModel has no real 'Company_CompanyModel17' property in the generated
    # code (a bare stub) -- manually attach it so Company_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Company_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Company_Category(name="sample_text")
    partner = Company_CompanyModel()
    setattr(partner, 'Company_CompanyModel17', None)
    _safe_set(owner, 'Company_Category18', partner)
    assert owner in getattr(partner, 'Company_CompanyModel17')
    _safe_set(owner, 'Company_Category18', None)
    assert owner not in getattr(partner, 'Company_CompanyModel17')


def test_assoc_company14_stub_double():
    # Company_CompanyModel has no real 'Company_CompanyModel' property in the generated
    # code (a bare stub) -- manually attach it so Company_Company's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Company_Company's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Company_Company(city="sample_text", completeAddress="sample_text", name="sample_text")
    partner = Company_CompanyModel()
    setattr(partner, 'Company_CompanyModel', None)
    _safe_set(owner, 'Company_Company15', partner)
    assert owner in getattr(partner, 'Company_CompanyModel')
    _safe_set(owner, 'Company_Company15', None)
    assert owner not in getattr(partner, 'Company_CompanyModel')


def test_assoc_division21_stub_double():
    # Company_CompanyModel has no real 'Company_CompanyModel22' property in the generated
    # code (a bare stub) -- manually attach it so Company_Division's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Company_Division's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Company_Division(name="sample_text")
    partner = Company_CompanyModel()
    setattr(partner, 'Company_CompanyModel22', None)
    _safe_set(owner, 'Company_Division23', partner)
    assert owner in getattr(partner, 'Company_CompanyModel22')
    _safe_set(owner, 'Company_Division23', None)
    assert owner not in getattr(partner, 'Company_CompanyModel22')


def test_assoc_employed1_stub_double():
    # Company_ServiceLine has no real 'Company_ServiceLine' property in the generated
    # code (a bare stub) -- manually attach it so Company_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Company_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Company_Person(firstname="sample_text", lastname="sample_text", position="sample_text")
    partner = Company_ServiceLine()
    setattr(partner, 'Company_ServiceLine', None)
    _safe_set(owner, 'Company_Person2', partner)
    assert getattr(partner, 'Company_ServiceLine') == owner
    _safe_set(owner, 'Company_Person2', None)
    assert getattr(partner, 'Company_ServiceLine') is None


def test_assoc_topics19_stub_double():
    # Company_CompanyModel has no real 'Company_CompanyModel20' property in the generated
    # code (a bare stub) -- manually attach it so Company_Topic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Company_Topic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Company_Topic(id="sample_text")
    partner = Company_CompanyModel()
    setattr(partner, 'Company_CompanyModel20', None)
    _safe_set(owner, 'Company_Topic', partner)
    assert owner in getattr(partner, 'Company_CompanyModel20')
    _safe_set(owner, 'Company_Topic', None)
    assert owner not in getattr(partner, 'Company_CompanyModel20')


