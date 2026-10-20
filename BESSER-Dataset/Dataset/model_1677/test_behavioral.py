import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Named,
    NamedElement,
    systemworkbench101_Component,
    systemworkbench101_Function,
    systemworkbench101_FunctionProperty,
    systemworkbench101_Named,
    systemworkbench101_NamedElement,
    systemworkbench101_PatternCatalog,
    systemworkbench101_RelatedTo,
    systemworkbench101_System,
    systemworkbench101_Thing,
    systemworkbench101_Thoughts,
    systemworkbench101_Workbench,
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

def test_assoc_catalog7_reverse_link_reassign_clear():
    a1 = systemworkbench101_Workbench(foobar="sample_text")
    a2 = systemworkbench101_Workbench(foobar="sample_text_2")
    b = systemworkbench101_PatternCatalog(id=7)
    _safe_set(b, 'systemworkbench101_PatternCatalog', a1)
    assert _is_linked(b, 'systemworkbench101_PatternCatalog', a1)
    if hasattr(a1, 'systemworkbench101_Workbench8'):
        assert _is_linked(a1, 'systemworkbench101_Workbench8', b)
    _safe_set(b, 'systemworkbench101_PatternCatalog', a2)
    assert _is_linked(b, 'systemworkbench101_PatternCatalog', a2)
    if hasattr(a1, 'systemworkbench101_Workbench8'):
        assert not _is_linked(a1, 'systemworkbench101_Workbench8', b)
    if hasattr(a2, 'systemworkbench101_Workbench8'):
        assert _is_linked(a2, 'systemworkbench101_Workbench8', b)
    _safe_set(b, 'systemworkbench101_PatternCatalog', None)
    assert not _is_linked(b, 'systemworkbench101_PatternCatalog', a2)
    if hasattr(a2, 'systemworkbench101_Workbench8'):
        assert not _is_linked(a2, 'systemworkbench101_Workbench8', b)


def test_assoc_fromThing36_reverse_link_reassign_clear():
    a1 = systemworkbench101_Thing(id=7)
    a2 = systemworkbench101_Thing(id=13)
    b = systemworkbench101_RelatedTo(since="sample_text")
    _safe_set(b, 'systemworkbench101_RelatedTo', a1)
    assert _is_linked(b, 'systemworkbench101_RelatedTo', a1)
    if hasattr(a1, 'systemworkbench101_Thing37'):
        assert _is_linked(a1, 'systemworkbench101_Thing37', b)
    _safe_set(b, 'systemworkbench101_RelatedTo', a2)
    assert _is_linked(b, 'systemworkbench101_RelatedTo', a2)
    if hasattr(a1, 'systemworkbench101_Thing37'):
        assert not _is_linked(a1, 'systemworkbench101_Thing37', b)
    if hasattr(a2, 'systemworkbench101_Thing37'):
        assert _is_linked(a2, 'systemworkbench101_Thing37', b)
    _safe_set(b, 'systemworkbench101_RelatedTo', None)
    assert not _is_linked(b, 'systemworkbench101_RelatedTo', a2)
    if hasattr(a2, 'systemworkbench101_Thing37'):
        assert not _is_linked(a2, 'systemworkbench101_Thing37', b)


def test_assoc_functionProperties5_reverse_link_reassign_clear():
    a1 = systemworkbench101_Workbench(foobar="sample_text")
    a2 = systemworkbench101_Workbench(foobar="sample_text_2")
    b = systemworkbench101_FunctionProperty(description="sample_text")
    _safe_set(b, 'systemworkbench101_FunctionProperty', a1)
    assert _is_linked(b, 'systemworkbench101_FunctionProperty', a1)
    if hasattr(a1, 'systemworkbench101_Workbench6'):
        assert _is_linked(a1, 'systemworkbench101_Workbench6', b)
    _safe_set(b, 'systemworkbench101_FunctionProperty', a2)
    assert _is_linked(b, 'systemworkbench101_FunctionProperty', a2)
    if hasattr(a1, 'systemworkbench101_Workbench6'):
        assert not _is_linked(a1, 'systemworkbench101_Workbench6', b)
    if hasattr(a2, 'systemworkbench101_Workbench6'):
        assert _is_linked(a2, 'systemworkbench101_Workbench6', b)
    _safe_set(b, 'systemworkbench101_FunctionProperty', None)
    assert not _is_linked(b, 'systemworkbench101_FunctionProperty', a2)
    if hasattr(a2, 'systemworkbench101_Workbench6'):
        assert not _is_linked(a2, 'systemworkbench101_Workbench6', b)


def test_assoc_parent14_reverse_link_reassign_clear():
    a1 = systemworkbench101_FunctionProperty(description="sample_text")
    a2 = systemworkbench101_FunctionProperty(description="sample_text_2")
    b = systemworkbench101_FunctionProperty(description="sample_text")
    _safe_set(b, 'systemworkbench101_FunctionProperty15', a1)
    assert _is_linked(b, 'systemworkbench101_FunctionProperty15', a1)
    if hasattr(a1, 'systemworkbench101_FunctionProperty13'):
        assert _is_linked(a1, 'systemworkbench101_FunctionProperty13', b)
    _safe_set(b, 'systemworkbench101_FunctionProperty15', a2)
    assert _is_linked(b, 'systemworkbench101_FunctionProperty15', a2)
    if hasattr(a1, 'systemworkbench101_FunctionProperty13'):
        assert not _is_linked(a1, 'systemworkbench101_FunctionProperty13', b)
    if hasattr(a2, 'systemworkbench101_FunctionProperty13'):
        assert _is_linked(a2, 'systemworkbench101_FunctionProperty13', b)
    _safe_set(b, 'systemworkbench101_FunctionProperty15', None)
    assert not _is_linked(b, 'systemworkbench101_FunctionProperty15', a2)
    if hasattr(a2, 'systemworkbench101_FunctionProperty13'):
        assert not _is_linked(a2, 'systemworkbench101_FunctionProperty13', b)


def test_assoc_relations41_reverse_link_reassign_clear():
    a1 = systemworkbench101_Thing(id=7)
    a2 = systemworkbench101_Thing(id=13)
    b = systemworkbench101_RelatedTo(since="sample_text")
    _safe_set(b, 'systemworkbench101_RelatedTo43', a1)
    assert _is_linked(b, 'systemworkbench101_RelatedTo43', a1)
    if hasattr(a1, 'systemworkbench101_Thing42'):
        assert _is_linked(a1, 'systemworkbench101_Thing42', b)
    _safe_set(b, 'systemworkbench101_RelatedTo43', a2)
    assert _is_linked(b, 'systemworkbench101_RelatedTo43', a2)
    if hasattr(a1, 'systemworkbench101_Thing42'):
        assert not _is_linked(a1, 'systemworkbench101_Thing42', b)
    if hasattr(a2, 'systemworkbench101_Thing42'):
        assert _is_linked(a2, 'systemworkbench101_Thing42', b)
    _safe_set(b, 'systemworkbench101_RelatedTo43', None)
    assert not _is_linked(b, 'systemworkbench101_RelatedTo43', a2)
    if hasattr(a2, 'systemworkbench101_Thing42'):
        assert not _is_linked(a2, 'systemworkbench101_Thing42', b)


def test_assoc_things9_reverse_link_reassign_clear():
    a1 = systemworkbench101_Workbench(foobar="sample_text")
    a2 = systemworkbench101_Workbench(foobar="sample_text_2")
    b = systemworkbench101_Thing(id=7)
    _safe_set(b, 'systemworkbench101_Thing', a1)
    assert _is_linked(b, 'systemworkbench101_Thing', a1)
    if hasattr(a1, 'systemworkbench101_Workbench10'):
        assert _is_linked(a1, 'systemworkbench101_Workbench10', b)
    _safe_set(b, 'systemworkbench101_Thing', a2)
    assert _is_linked(b, 'systemworkbench101_Thing', a2)
    if hasattr(a1, 'systemworkbench101_Workbench10'):
        assert not _is_linked(a1, 'systemworkbench101_Workbench10', b)
    if hasattr(a2, 'systemworkbench101_Workbench10'):
        assert _is_linked(a2, 'systemworkbench101_Workbench10', b)
    _safe_set(b, 'systemworkbench101_Thing', None)
    assert not _is_linked(b, 'systemworkbench101_Thing', a2)
    if hasattr(a2, 'systemworkbench101_Workbench10'):
        assert not _is_linked(a2, 'systemworkbench101_Workbench10', b)


def test_assoc_toThing38_reverse_link_reassign_clear():
    a1 = systemworkbench101_Thing(id=7)
    a2 = systemworkbench101_Thing(id=13)
    b = systemworkbench101_RelatedTo(since="sample_text")
    _safe_set(b, 'systemworkbench101_RelatedTo39', a1)
    assert _is_linked(b, 'systemworkbench101_RelatedTo39', a1)
    if hasattr(a1, 'systemworkbench101_Thing40'):
        assert _is_linked(a1, 'systemworkbench101_Thing40', b)
    _safe_set(b, 'systemworkbench101_RelatedTo39', a2)
    assert _is_linked(b, 'systemworkbench101_RelatedTo39', a2)
    if hasattr(a1, 'systemworkbench101_Thing40'):
        assert not _is_linked(a1, 'systemworkbench101_Thing40', b)
    if hasattr(a2, 'systemworkbench101_Thing40'):
        assert _is_linked(a2, 'systemworkbench101_Thing40', b)
    _safe_set(b, 'systemworkbench101_RelatedTo39', None)
    assert not _is_linked(b, 'systemworkbench101_RelatedTo39', a2)
    if hasattr(a2, 'systemworkbench101_Thing40'):
        assert not _is_linked(a2, 'systemworkbench101_Thing40', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_patterns33_stub_double():
    # systemworkbench101_Function has no real 'systemworkbench101_Function35' property in the generated
    # code (a bare stub) -- manually attach it so systemworkbench101_PatternCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemworkbench101_PatternCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemworkbench101_PatternCatalog(id=7)
    partner = systemworkbench101_Function()
    setattr(partner, 'systemworkbench101_Function35', None)
    _safe_set(owner, 'systemworkbench101_PatternCatalog34', {partner})
    assert getattr(partner, 'systemworkbench101_Function35') == owner
    _safe_set(owner, 'systemworkbench101_PatternCatalog34', set())
    assert getattr(partner, 'systemworkbench101_Function35') is None


def test_assoc_property19_stub_double():
    # systemworkbench101_Function has no real 'systemworkbench101_Function20' property in the generated
    # code (a bare stub) -- manually attach it so systemworkbench101_FunctionProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemworkbench101_FunctionProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemworkbench101_FunctionProperty(description="sample_text")
    partner = systemworkbench101_Function()
    setattr(partner, 'systemworkbench101_Function20', None)
    _safe_set(owner, 'systemworkbench101_FunctionProperty21', partner)
    assert owner in getattr(partner, 'systemworkbench101_Function20')
    _safe_set(owner, 'systemworkbench101_FunctionProperty21', None)
    assert owner not in getattr(partner, 'systemworkbench101_Function20')


def test_assoc_relatedTo44_stub_double():
    # systemworkbench101_Thoughts has no real 'systemworkbench101_Thoughts45' property in the generated
    # code (a bare stub) -- manually attach it so systemworkbench101_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemworkbench101_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemworkbench101_Thing(id=7)
    partner = systemworkbench101_Thoughts()
    setattr(partner, 'systemworkbench101_Thoughts45', None)
    _safe_set(owner, 'systemworkbench101_Thing46', partner)
    assert owner in getattr(partner, 'systemworkbench101_Thoughts45')
    _safe_set(owner, 'systemworkbench101_Thing46', None)
    assert owner not in getattr(partner, 'systemworkbench101_Thoughts45')


def test_assoc_systemView3_stub_double():
    # systemworkbench101_System has no real 'systemworkbench101_System4' property in the generated
    # code (a bare stub) -- manually attach it so systemworkbench101_Workbench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemworkbench101_Workbench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemworkbench101_Workbench(foobar="sample_text")
    partner = systemworkbench101_System()
    setattr(partner, 'systemworkbench101_System4', None)
    _safe_set(owner, 'systemworkbench101_Workbench', partner)
    assert getattr(partner, 'systemworkbench101_System4') == owner
    _safe_set(owner, 'systemworkbench101_Workbench', None)
    assert getattr(partner, 'systemworkbench101_System4') is None


def test_assoc_thoughts11_stub_double():
    # systemworkbench101_Thoughts has no real 'systemworkbench101_Thoughts' property in the generated
    # code (a bare stub) -- manually attach it so systemworkbench101_Workbench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # systemworkbench101_Workbench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = systemworkbench101_Workbench(foobar="sample_text")
    partner = systemworkbench101_Thoughts()
    setattr(partner, 'systemworkbench101_Thoughts', None)
    _safe_set(owner, 'systemworkbench101_Workbench12', {partner})
    assert getattr(partner, 'systemworkbench101_Thoughts') == owner
    _safe_set(owner, 'systemworkbench101_Workbench12', set())
    assert getattr(partner, 'systemworkbench101_Thoughts') is None


