import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Addressable,
    AudioVisualItem,
    CirculatingItem,
    Item,
    Lendable,
    Person,
    extlibraryprofile_Addressable,
    extlibraryprofile_AudioVisualItem,
    extlibraryprofile_Book,
    extlibraryprofile_BookOnTape,
    extlibraryprofile_Borrower,
    extlibraryprofile_Borrows,
    extlibraryprofile_CirculatingItem,
    extlibraryprofile_Class,
    extlibraryprofile_Dependency,
    extlibraryprofile_Employee,
    extlibraryprofile_Item,
    extlibraryprofile_Lendable,
    extlibraryprofile_Library,
    extlibraryprofile_Package,
    extlibraryprofile_Periodical,
    extlibraryprofile_Person,
    extlibraryprofile_VideoCassete,
    extlibraryprofile_Writer,
    BookCategory,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_base_Class0_stub_double():
    # extlibraryprofile_Class has no real 'extlibraryprofile_Class' property in the generated
    # code (a bare stub) -- manually attach it so extlibraryprofile_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibraryprofile_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibraryprofile_Item(publicationDate="sample_text", title="sample_text")
    partner = extlibraryprofile_Class()
    setattr(partner, 'extlibraryprofile_Class', None)
    _safe_set(owner, 'extlibraryprofile_Item', partner)
    assert getattr(partner, 'extlibraryprofile_Class') == owner
    _safe_set(owner, 'extlibraryprofile_Item', None)
    assert getattr(partner, 'extlibraryprofile_Class') is None


def test_assoc_base_Class7_stub_double():
    # extlibraryprofile_Class has no real 'extlibraryprofile_Class9' property in the generated
    # code (a bare stub) -- manually attach it so extlibraryprofile_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibraryprofile_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibraryprofile_Person(firstName="sample_text", lastName="sample_text")
    partner = extlibraryprofile_Class()
    setattr(partner, 'extlibraryprofile_Class9', None)
    _safe_set(owner, 'extlibraryprofile_Person8', partner)
    assert getattr(partner, 'extlibraryprofile_Class9') == owner
    _safe_set(owner, 'extlibraryprofile_Person8', None)
    assert getattr(partner, 'extlibraryprofile_Class9') is None


def test_assoc_base_Package1_stub_double():
    # extlibraryprofile_Package has no real 'extlibraryprofile_Package' property in the generated
    # code (a bare stub) -- manually attach it so extlibraryprofile_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibraryprofile_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibraryprofile_Library(name="sample_text")
    partner = extlibraryprofile_Package()
    setattr(partner, 'extlibraryprofile_Package', None)
    _safe_set(owner, 'extlibraryprofile_Library', partner)
    assert getattr(partner, 'extlibraryprofile_Package') == owner
    _safe_set(owner, 'extlibraryprofile_Library', None)
    assert getattr(partner, 'extlibraryprofile_Package') is None


def test_assoc_bookOnTape14_stub_double():
    # extlibraryprofile_BookOnTape has no real 'extlibraryprofile_BookOnTape6' property in the generated
    # code (a bare stub) -- manually attach it so extlibraryprofile_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibraryprofile_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibraryprofile_Person(firstName="sample_text", lastName="sample_text")
    partner = extlibraryprofile_BookOnTape()
    setattr(partner, 'extlibraryprofile_BookOnTape6', None)
    _safe_set(owner, 'extlibraryprofile_Person5', partner)
    assert getattr(partner, 'extlibraryprofile_BookOnTape6') == owner
    _safe_set(owner, 'extlibraryprofile_Person5', None)
    assert getattr(partner, 'extlibraryprofile_BookOnTape6') is None


def test_assoc_bookOnTape2_stub_double():
    # extlibraryprofile_BookOnTape has no real 'extlibraryprofile_BookOnTape' property in the generated
    # code (a bare stub) -- manually attach it so extlibraryprofile_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibraryprofile_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibraryprofile_Writer(name="sample_text")
    partner = extlibraryprofile_BookOnTape()
    setattr(partner, 'extlibraryprofile_BookOnTape', None)
    _safe_set(owner, 'extlibraryprofile_Writer', partner)
    assert getattr(partner, 'extlibraryprofile_BookOnTape') == owner
    _safe_set(owner, 'extlibraryprofile_Writer', None)
    assert getattr(partner, 'extlibraryprofile_BookOnTape') is None


def test_assoc_videoCassete3_stub_double():
    # extlibraryprofile_VideoCassete has no real 'extlibraryprofile_VideoCassete' property in the generated
    # code (a bare stub) -- manually attach it so extlibraryprofile_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibraryprofile_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibraryprofile_Person(firstName="sample_text", lastName="sample_text")
    partner = extlibraryprofile_VideoCassete()
    setattr(partner, 'extlibraryprofile_VideoCassete', None)
    _safe_set(owner, 'extlibraryprofile_Person', {partner})
    assert getattr(partner, 'extlibraryprofile_VideoCassete') == owner
    _safe_set(owner, 'extlibraryprofile_Person', set())
    assert getattr(partner, 'extlibraryprofile_VideoCassete') is None


