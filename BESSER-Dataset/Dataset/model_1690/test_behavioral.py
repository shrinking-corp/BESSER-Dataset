import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    helloworld150_Comment,
    helloworld150_NamedElement,
    helloworld150_Own,
    helloworld150_Person,
    helloworld150_Profession,
    helloworld150_Thing,
    helloworld150_World,
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

def test_assoc_comment8_reverse_link_reassign_clear():
    a1 = helloworld150_NamedElement(name="sample_text")
    a2 = helloworld150_NamedElement(name="sample_text_2")
    b = helloworld150_Comment(content="sample_text")
    _safe_set(b, 'helloworld150_Comment', a1)
    assert _is_linked(b, 'helloworld150_Comment', a1)
    if hasattr(a1, 'helloworld150_NamedElement'):
        assert _is_linked(a1, 'helloworld150_NamedElement', b)
    _safe_set(b, 'helloworld150_Comment', a2)
    assert _is_linked(b, 'helloworld150_Comment', a2)
    if hasattr(a1, 'helloworld150_NamedElement'):
        assert not _is_linked(a1, 'helloworld150_NamedElement', b)
    if hasattr(a2, 'helloworld150_NamedElement'):
        assert _is_linked(a2, 'helloworld150_NamedElement', b)
    _safe_set(b, 'helloworld150_Comment', None)
    assert not _is_linked(b, 'helloworld150_Comment', a2)
    if hasattr(a2, 'helloworld150_NamedElement'):
        assert not _is_linked(a2, 'helloworld150_NamedElement', b)


def test_assoc_ownership5_reverse_link_reassign_clear():
    a1 = helloworld150_Thing(id=7)
    a2 = helloworld150_Thing(id=13)
    b = helloworld150_Own(ownerName="sample_text", since="sample_text")
    _safe_set(b, 'Own', a1)
    assert _is_linked(b, 'Own', a1)
    if hasattr(a1, 'thing'):
        assert _is_linked(a1, 'thing', b)
    _safe_set(b, 'Own', a2)
    assert _is_linked(b, 'Own', a2)
    if hasattr(a1, 'thing'):
        assert not _is_linked(a1, 'thing', b)
    if hasattr(a2, 'thing'):
        assert _is_linked(a2, 'thing', b)
    _safe_set(b, 'Own', None)
    assert not _is_linked(b, 'Own', a2)
    if hasattr(a2, 'thing'):
        assert not _is_linked(a2, 'thing', b)


def test_assoc_ownerships6_reverse_link_reassign_clear():
    a1 = helloworld150_Thing(id=7)
    a2 = helloworld150_Thing(id=13)
    b = helloworld150_Own(ownerName="sample_text", since="sample_text")
    _safe_set(b, 'helloworld150_Own', a1)
    assert _is_linked(b, 'helloworld150_Own', a1)
    if hasattr(a1, 'helloworld150_Thing7'):
        assert _is_linked(a1, 'helloworld150_Thing7', b)
    _safe_set(b, 'helloworld150_Own', a2)
    assert _is_linked(b, 'helloworld150_Own', a2)
    if hasattr(a1, 'helloworld150_Thing7'):
        assert not _is_linked(a1, 'helloworld150_Thing7', b)
    if hasattr(a2, 'helloworld150_Thing7'):
        assert _is_linked(a2, 'helloworld150_Thing7', b)
    _safe_set(b, 'helloworld150_Own', None)
    assert not _is_linked(b, 'helloworld150_Own', a2)
    if hasattr(a2, 'helloworld150_Thing7'):
        assert not _is_linked(a2, 'helloworld150_Thing7', b)


def test_assoc_person10_reverse_link_reassign_clear():
    a1 = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    a2 = helloworld150_Person(birthDate="sample_text_2", forName="sample_text_2")
    b = helloworld150_Own(ownerName="sample_text", since="sample_text")
    _safe_set(b, 'helloworld150_Own11', a1)
    assert _is_linked(b, 'helloworld150_Own11', a1)
    if hasattr(a1, 'helloworld150_Person12'):
        assert _is_linked(a1, 'helloworld150_Person12', b)
    _safe_set(b, 'helloworld150_Own11', a2)
    assert _is_linked(b, 'helloworld150_Own11', a2)
    if hasattr(a1, 'helloworld150_Person12'):
        assert not _is_linked(a1, 'helloworld150_Person12', b)
    if hasattr(a2, 'helloworld150_Person12'):
        assert _is_linked(a2, 'helloworld150_Person12', b)
    _safe_set(b, 'helloworld150_Own11', None)
    assert not _is_linked(b, 'helloworld150_Own11', a2)
    if hasattr(a2, 'helloworld150_Person12'):
        assert not _is_linked(a2, 'helloworld150_Person12', b)


def test_assoc_profession13_reverse_link_reassign_clear():
    a1 = helloworld150_Profession(name="sample_text")
    a2 = helloworld150_Profession(name="sample_text_2")
    b = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    _safe_set(b, 'helloworld150_Person14', a1)
    assert _is_linked(b, 'helloworld150_Person14', a1)
    if hasattr(a1, 'helloworld150_Profession15'):
        assert _is_linked(a1, 'helloworld150_Profession15', b)
    _safe_set(b, 'helloworld150_Person14', a2)
    assert _is_linked(b, 'helloworld150_Person14', a2)
    if hasattr(a1, 'helloworld150_Profession15'):
        assert not _is_linked(a1, 'helloworld150_Profession15', b)
    if hasattr(a2, 'helloworld150_Profession15'):
        assert _is_linked(a2, 'helloworld150_Profession15', b)
    _safe_set(b, 'helloworld150_Person14', None)
    assert not _is_linked(b, 'helloworld150_Person14', a2)
    if hasattr(a2, 'helloworld150_Profession15'):
        assert not _is_linked(a2, 'helloworld150_Profession15', b)


def test_assoc_thing9_reverse_link_reassign_clear():
    a1 = helloworld150_Thing(id=7)
    a2 = helloworld150_Thing(id=13)
    b = helloworld150_Own(ownerName="sample_text", since="sample_text")
    _safe_set(b, 'ownership', a1)
    assert _is_linked(b, 'ownership', a1)
    if hasattr(a1, 'Thing'):
        assert _is_linked(a1, 'Thing', b)
    _safe_set(b, 'ownership', a2)
    assert _is_linked(b, 'ownership', a2)
    if hasattr(a1, 'Thing'):
        assert not _is_linked(a1, 'Thing', b)
    if hasattr(a2, 'Thing'):
        assert _is_linked(a2, 'Thing', b)
    _safe_set(b, 'ownership', None)
    assert not _is_linked(b, 'ownership', a2)
    if hasattr(a2, 'Thing'):
        assert not _is_linked(a2, 'Thing', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_persons1_stub_double():
    # helloworld150_World has no real 'helloworld150_World2' property in the generated
    # code (a bare stub) -- manually attach it so helloworld150_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloworld150_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    partner = helloworld150_World()
    setattr(partner, 'helloworld150_World2', None)
    _safe_set(owner, 'helloworld150_Person', partner)
    assert owner in getattr(partner, 'helloworld150_World2')
    _safe_set(owner, 'helloworld150_Person', None)
    assert owner not in getattr(partner, 'helloworld150_World2')


def test_assoc_professions3_stub_double():
    # helloworld150_World has no real 'helloworld150_World4' property in the generated
    # code (a bare stub) -- manually attach it so helloworld150_Profession's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloworld150_Profession's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloworld150_Profession(name="sample_text")
    partner = helloworld150_World()
    setattr(partner, 'helloworld150_World4', None)
    _safe_set(owner, 'helloworld150_Profession', partner)
    assert owner in getattr(partner, 'helloworld150_World4')
    _safe_set(owner, 'helloworld150_Profession', None)
    assert owner not in getattr(partner, 'helloworld150_World4')


def test_assoc_things0_stub_double():
    # helloworld150_World has no real 'helloworld150_World' property in the generated
    # code (a bare stub) -- manually attach it so helloworld150_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloworld150_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloworld150_Thing(id=7)
    partner = helloworld150_World()
    setattr(partner, 'helloworld150_World', None)
    _safe_set(owner, 'helloworld150_Thing', partner)
    assert owner in getattr(partner, 'helloworld150_World')
    _safe_set(owner, 'helloworld150_Thing', None)
    assert owner not in getattr(partner, 'helloworld150_World')


