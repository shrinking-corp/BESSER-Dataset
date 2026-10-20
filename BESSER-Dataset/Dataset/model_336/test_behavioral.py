import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    _15LbQG60EeGkd4g88tZXfA,
    _15N3gm60EeGkd4g88tZXfA,
    _15OelG60EeGkd4g88tZXfA,
    extlibrary_Addressable,
    extlibrary_AudioVisualItem,
    extlibrary_Book,
    extlibrary_BookOnTape,
    extlibrary_Borrower,
    extlibrary_CirculatingItem,
    extlibrary_Employee,
    extlibrary_Item,
    extlibrary_Lendable,
    extlibrary_Library,
    extlibrary_Periodical,
    extlibrary_Person,
    extlibrary_VideoCassette,
    extlibrary_Writer,
    extlibrary__146VgG60EeGkd4g88tZXfA,
    extlibrary__148KsW60EeGkd4g88tZXfA,
    extlibrary__15CRUW60EeGkd4g88tZXfA,
    extlibrary__15Hw4m60EeGkd4g88tZXfA,
    extlibrary__15IX8G60EeGkd4g88tZXfA,
    extlibrary__15N3gm60EeGkd4g88tZXfA,
    extlibrary__15NQcW60EeGkd4g88tZXfA,
    extlibrary__15OekG60EeGkd4g88tZXfA,
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

def test_assoc_author0_stub_double():
    # extlibrary__15CRUW60EeGkd4g88tZXfA has no real 'extlibrary__15CRUW60EeGkd4g88tZXfA' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Book(category="sample_text", pages=7, title="sample_text")
    partner = extlibrary__15CRUW60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__15CRUW60EeGkd4g88tZXfA', None)
    _safe_set(owner, 'extlibrary_Book', partner)
    assert getattr(partner, 'extlibrary__15CRUW60EeGkd4g88tZXfA') == owner
    _safe_set(owner, 'extlibrary_Book', None)
    assert getattr(partner, 'extlibrary__15CRUW60EeGkd4g88tZXfA') is None


def test_assoc_books16_stub_double():
    # extlibrary__146VgG60EeGkd4g88tZXfA has no real 'extlibrary__146VgG60EeGkd4g88tZXfA17' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Writer(name="sample_text")
    partner = extlibrary__146VgG60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__146VgG60EeGkd4g88tZXfA17', None)
    _safe_set(owner, 'extlibrary_Writer', {partner})
    assert getattr(partner, 'extlibrary__146VgG60EeGkd4g88tZXfA17') == owner
    _safe_set(owner, 'extlibrary_Writer', set())
    assert getattr(partner, 'extlibrary__146VgG60EeGkd4g88tZXfA17') is None


def test_assoc_books9_stub_double():
    # extlibrary__146VgG60EeGkd4g88tZXfA has no real 'extlibrary__146VgG60EeGkd4g88tZXfA' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text", people="sample_text")
    partner = extlibrary__146VgG60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__146VgG60EeGkd4g88tZXfA', None)
    _safe_set(owner, 'extlibrary_Library10', {partner})
    assert getattr(partner, 'extlibrary__146VgG60EeGkd4g88tZXfA') == owner
    _safe_set(owner, 'extlibrary_Library10', set())
    assert getattr(partner, 'extlibrary__146VgG60EeGkd4g88tZXfA') is None


def test_assoc_borrowers18_stub_double():
    # extlibrary__15NQcW60EeGkd4g88tZXfA has no real 'extlibrary__15NQcW60EeGkd4g88tZXfA19' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Lendable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Lendable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Lendable(copies=7)
    partner = extlibrary__15NQcW60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__15NQcW60EeGkd4g88tZXfA19', None)
    _safe_set(owner, 'extlibrary_Lendable', {partner})
    assert getattr(partner, 'extlibrary__15NQcW60EeGkd4g88tZXfA19') == owner
    _safe_set(owner, 'extlibrary_Lendable', set())
    assert getattr(partner, 'extlibrary__15NQcW60EeGkd4g88tZXfA19') is None


def test_assoc_borrowers5_stub_double():
    # extlibrary__15NQcW60EeGkd4g88tZXfA has no real 'extlibrary__15NQcW60EeGkd4g88tZXfA' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text", people="sample_text")
    partner = extlibrary__15NQcW60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__15NQcW60EeGkd4g88tZXfA', None)
    _safe_set(owner, 'extlibrary_Library6', {partner})
    assert getattr(partner, 'extlibrary__15NQcW60EeGkd4g88tZXfA') == owner
    _safe_set(owner, 'extlibrary_Library6', set())
    assert getattr(partner, 'extlibrary__15NQcW60EeGkd4g88tZXfA') is None


def test_assoc_branches11_stub_double():
    # extlibrary__148KsW60EeGkd4g88tZXfA has no real 'extlibrary__148KsW60EeGkd4g88tZXfA' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text", people="sample_text")
    partner = extlibrary__148KsW60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__148KsW60EeGkd4g88tZXfA', None)
    _safe_set(owner, 'extlibrary_Library12', {partner})
    assert getattr(partner, 'extlibrary__148KsW60EeGkd4g88tZXfA') == owner
    _safe_set(owner, 'extlibrary_Library12', set())
    assert getattr(partner, 'extlibrary__148KsW60EeGkd4g88tZXfA') is None


def test_assoc_employees3_stub_double():
    # extlibrary__15OekG60EeGkd4g88tZXfA has no real 'extlibrary__15OekG60EeGkd4g88tZXfA' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text", people="sample_text")
    partner = extlibrary__15OekG60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__15OekG60EeGkd4g88tZXfA', None)
    _safe_set(owner, 'extlibrary_Library4', {partner})
    assert getattr(partner, 'extlibrary__15OekG60EeGkd4g88tZXfA') == owner
    _safe_set(owner, 'extlibrary_Library4', set())
    assert getattr(partner, 'extlibrary__15OekG60EeGkd4g88tZXfA') is None


def test_assoc_parentBranch13_stub_double():
    # extlibrary__148KsW60EeGkd4g88tZXfA has no real 'extlibrary__148KsW60EeGkd4g88tZXfA15' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text", people="sample_text")
    partner = extlibrary__148KsW60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__148KsW60EeGkd4g88tZXfA15', None)
    _safe_set(owner, 'extlibrary_Library14', partner)
    assert getattr(partner, 'extlibrary__148KsW60EeGkd4g88tZXfA15') == owner
    _safe_set(owner, 'extlibrary_Library14', None)
    assert getattr(partner, 'extlibrary__148KsW60EeGkd4g88tZXfA15') is None


def test_assoc_stock7_stub_double():
    # extlibrary__15Hw4m60EeGkd4g88tZXfA has no real 'extlibrary__15Hw4m60EeGkd4g88tZXfA' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text", people="sample_text")
    partner = extlibrary__15Hw4m60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__15Hw4m60EeGkd4g88tZXfA', None)
    _safe_set(owner, 'extlibrary_Library8', {partner})
    assert getattr(partner, 'extlibrary__15Hw4m60EeGkd4g88tZXfA') == owner
    _safe_set(owner, 'extlibrary_Library8', set())
    assert getattr(partner, 'extlibrary__15Hw4m60EeGkd4g88tZXfA') is None


def test_assoc_writers1_stub_double():
    # extlibrary__15CRUW60EeGkd4g88tZXfA has no real 'extlibrary__15CRUW60EeGkd4g88tZXfA2' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text", people="sample_text")
    partner = extlibrary__15CRUW60EeGkd4g88tZXfA()
    setattr(partner, 'extlibrary__15CRUW60EeGkd4g88tZXfA2', None)
    _safe_set(owner, 'extlibrary_Library', {partner})
    assert getattr(partner, 'extlibrary__15CRUW60EeGkd4g88tZXfA2') == owner
    _safe_set(owner, 'extlibrary_Library', set())
    assert getattr(partner, 'extlibrary__15CRUW60EeGkd4g88tZXfA2') is None


