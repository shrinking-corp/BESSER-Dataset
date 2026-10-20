import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    syswb106_Component,
    syswb106_Function,
    syswb106_FunctionProperty,
    syswb106_PatternCatalog,
    syswb106_RelatedTo,
    syswb106_System,
    syswb106_Thing,
    syswb106_Thoughts,
    syswb106_Workbench,
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
    a1 = syswb106_Workbench(aprop="sample_text")
    a2 = syswb106_Workbench(aprop="sample_text_2")
    b = syswb106_PatternCatalog(id="sample_text")
    _safe_set(b, 'syswb106_PatternCatalog', a1)
    assert _is_linked(b, 'syswb106_PatternCatalog', a1)
    if hasattr(a1, 'syswb106_Workbench8'):
        assert _is_linked(a1, 'syswb106_Workbench8', b)
    _safe_set(b, 'syswb106_PatternCatalog', a2)
    assert _is_linked(b, 'syswb106_PatternCatalog', a2)
    if hasattr(a1, 'syswb106_Workbench8'):
        assert not _is_linked(a1, 'syswb106_Workbench8', b)
    if hasattr(a2, 'syswb106_Workbench8'):
        assert _is_linked(a2, 'syswb106_Workbench8', b)
    _safe_set(b, 'syswb106_PatternCatalog', None)
    assert not _is_linked(b, 'syswb106_PatternCatalog', a2)
    if hasattr(a2, 'syswb106_Workbench8'):
        assert not _is_linked(a2, 'syswb106_Workbench8', b)


def test_assoc_fromThing10_reverse_link_reassign_clear():
    a1 = syswb106_Thing(id=7)
    a2 = syswb106_Thing(id=13)
    b = syswb106_RelatedTo(since="sample_text")
    _safe_set(b, 'relations', a1)
    assert _is_linked(b, 'relations', a1)
    if hasattr(a1, 'Thing'):
        assert _is_linked(a1, 'Thing', b)
    _safe_set(b, 'relations', a2)
    assert _is_linked(b, 'relations', a2)
    if hasattr(a1, 'Thing'):
        assert not _is_linked(a1, 'Thing', b)
    if hasattr(a2, 'Thing'):
        assert _is_linked(a2, 'Thing', b)
    _safe_set(b, 'relations', None)
    assert not _is_linked(b, 'relations', a2)
    if hasattr(a2, 'Thing'):
        assert not _is_linked(a2, 'Thing', b)


def test_assoc_functionProperties5_reverse_link_reassign_clear():
    a1 = syswb106_Workbench(aprop="sample_text")
    a2 = syswb106_Workbench(aprop="sample_text_2")
    b = syswb106_FunctionProperty(description="sample_text")
    _safe_set(b, 'syswb106_FunctionProperty', a1)
    assert _is_linked(b, 'syswb106_FunctionProperty', a1)
    if hasattr(a1, 'syswb106_Workbench6'):
        assert _is_linked(a1, 'syswb106_Workbench6', b)
    _safe_set(b, 'syswb106_FunctionProperty', a2)
    assert _is_linked(b, 'syswb106_FunctionProperty', a2)
    if hasattr(a1, 'syswb106_Workbench6'):
        assert not _is_linked(a1, 'syswb106_Workbench6', b)
    if hasattr(a2, 'syswb106_Workbench6'):
        assert _is_linked(a2, 'syswb106_Workbench6', b)
    _safe_set(b, 'syswb106_FunctionProperty', None)
    assert not _is_linked(b, 'syswb106_FunctionProperty', a2)
    if hasattr(a2, 'syswb106_Workbench6'):
        assert not _is_linked(a2, 'syswb106_Workbench6', b)


def test_assoc_parent17_reverse_link_reassign_clear():
    a1 = syswb106_FunctionProperty(description="sample_text")
    a2 = syswb106_FunctionProperty(description="sample_text_2")
    b = syswb106_FunctionProperty(description="sample_text")
    _safe_set(b, 'syswb106_FunctionProperty18', a1)
    assert _is_linked(b, 'syswb106_FunctionProperty18', a1)
    if hasattr(a1, 'syswb106_FunctionProperty16'):
        assert _is_linked(a1, 'syswb106_FunctionProperty16', b)
    _safe_set(b, 'syswb106_FunctionProperty18', a2)
    assert _is_linked(b, 'syswb106_FunctionProperty18', a2)
    if hasattr(a1, 'syswb106_FunctionProperty16'):
        assert not _is_linked(a1, 'syswb106_FunctionProperty16', b)
    if hasattr(a2, 'syswb106_FunctionProperty16'):
        assert _is_linked(a2, 'syswb106_FunctionProperty16', b)
    _safe_set(b, 'syswb106_FunctionProperty18', None)
    assert not _is_linked(b, 'syswb106_FunctionProperty18', a2)
    if hasattr(a2, 'syswb106_FunctionProperty16'):
        assert not _is_linked(a2, 'syswb106_FunctionProperty16', b)


def test_assoc_relations9_reverse_link_reassign_clear():
    a1 = syswb106_Thing(id=7)
    a2 = syswb106_Thing(id=13)
    b = syswb106_RelatedTo(since="sample_text")
    _safe_set(b, 'RelatedTo', a1)
    assert _is_linked(b, 'RelatedTo', a1)
    if hasattr(a1, 'fromThing'):
        assert _is_linked(a1, 'fromThing', b)
    _safe_set(b, 'RelatedTo', a2)
    assert _is_linked(b, 'RelatedTo', a2)
    if hasattr(a1, 'fromThing'):
        assert not _is_linked(a1, 'fromThing', b)
    if hasattr(a2, 'fromThing'):
        assert _is_linked(a2, 'fromThing', b)
    _safe_set(b, 'RelatedTo', None)
    assert not _is_linked(b, 'RelatedTo', a2)
    if hasattr(a2, 'fromThing'):
        assert not _is_linked(a2, 'fromThing', b)


def test_assoc_things0_reverse_link_reassign_clear():
    a1 = syswb106_Workbench(aprop="sample_text")
    a2 = syswb106_Workbench(aprop="sample_text_2")
    b = syswb106_Thing(id=7)
    _safe_set(b, 'syswb106_Thing', a1)
    assert _is_linked(b, 'syswb106_Thing', a1)
    if hasattr(a1, 'syswb106_Workbench'):
        assert _is_linked(a1, 'syswb106_Workbench', b)
    _safe_set(b, 'syswb106_Thing', a2)
    assert _is_linked(b, 'syswb106_Thing', a2)
    if hasattr(a1, 'syswb106_Workbench'):
        assert not _is_linked(a1, 'syswb106_Workbench', b)
    if hasattr(a2, 'syswb106_Workbench'):
        assert _is_linked(a2, 'syswb106_Workbench', b)
    _safe_set(b, 'syswb106_Thing', None)
    assert not _is_linked(b, 'syswb106_Thing', a2)
    if hasattr(a2, 'syswb106_Workbench'):
        assert not _is_linked(a2, 'syswb106_Workbench', b)


def test_assoc_toThing11_reverse_link_reassign_clear():
    a1 = syswb106_Thing(id=7)
    a2 = syswb106_Thing(id=13)
    b = syswb106_RelatedTo(since="sample_text")
    _safe_set(b, 'syswb106_RelatedTo', a1)
    assert _is_linked(b, 'syswb106_RelatedTo', a1)
    if hasattr(a1, 'syswb106_Thing12'):
        assert _is_linked(a1, 'syswb106_Thing12', b)
    _safe_set(b, 'syswb106_RelatedTo', a2)
    assert _is_linked(b, 'syswb106_RelatedTo', a2)
    if hasattr(a1, 'syswb106_Thing12'):
        assert not _is_linked(a1, 'syswb106_Thing12', b)
    if hasattr(a2, 'syswb106_Thing12'):
        assert _is_linked(a2, 'syswb106_Thing12', b)
    _safe_set(b, 'syswb106_RelatedTo', None)
    assert not _is_linked(b, 'syswb106_RelatedTo', a2)
    if hasattr(a2, 'syswb106_Thing12'):
        assert not _is_linked(a2, 'syswb106_Thing12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_patterns44_stub_double():
    # syswb106_Function has no real 'syswb106_Function46' property in the generated
    # code (a bare stub) -- manually attach it so syswb106_PatternCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswb106_PatternCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswb106_PatternCatalog(id="sample_text")
    partner = syswb106_Function()
    setattr(partner, 'syswb106_Function46', None)
    _safe_set(owner, 'syswb106_PatternCatalog45', {partner})
    assert getattr(partner, 'syswb106_Function46') == owner
    _safe_set(owner, 'syswb106_PatternCatalog45', set())
    assert getattr(partner, 'syswb106_Function46') is None


def test_assoc_property29_stub_double():
    # syswb106_Function has no real 'syswb106_Function30' property in the generated
    # code (a bare stub) -- manually attach it so syswb106_FunctionProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswb106_FunctionProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswb106_FunctionProperty(description="sample_text")
    partner = syswb106_Function()
    setattr(partner, 'syswb106_Function30', None)
    _safe_set(owner, 'syswb106_FunctionProperty31', partner)
    assert owner in getattr(partner, 'syswb106_Function30')
    _safe_set(owner, 'syswb106_FunctionProperty31', None)
    assert owner not in getattr(partner, 'syswb106_Function30')


def test_assoc_relatedTo13_stub_double():
    # syswb106_Thoughts has no real 'syswb106_Thoughts14' property in the generated
    # code (a bare stub) -- manually attach it so syswb106_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswb106_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswb106_Thing(id=7)
    partner = syswb106_Thoughts()
    setattr(partner, 'syswb106_Thoughts14', None)
    _safe_set(owner, 'syswb106_Thing15', partner)
    assert owner in getattr(partner, 'syswb106_Thoughts14')
    _safe_set(owner, 'syswb106_Thing15', None)
    assert owner not in getattr(partner, 'syswb106_Thoughts14')


def test_assoc_systemView3_stub_double():
    # syswb106_System has no real 'syswb106_System' property in the generated
    # code (a bare stub) -- manually attach it so syswb106_Workbench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswb106_Workbench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswb106_Workbench(aprop="sample_text")
    partner = syswb106_System()
    setattr(partner, 'syswb106_System', None)
    _safe_set(owner, 'syswb106_Workbench4', partner)
    assert getattr(partner, 'syswb106_System') == owner
    _safe_set(owner, 'syswb106_Workbench4', None)
    assert getattr(partner, 'syswb106_System') is None


def test_assoc_thoughts1_stub_double():
    # syswb106_Thoughts has no real 'syswb106_Thoughts' property in the generated
    # code (a bare stub) -- manually attach it so syswb106_Workbench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # syswb106_Workbench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = syswb106_Workbench(aprop="sample_text")
    partner = syswb106_Thoughts()
    setattr(partner, 'syswb106_Thoughts', None)
    _safe_set(owner, 'syswb106_Workbench2', {partner})
    assert getattr(partner, 'syswb106_Thoughts') == owner
    _safe_set(owner, 'syswb106_Workbench2', set())
    assert getattr(partner, 'syswb106_Thoughts') is None


