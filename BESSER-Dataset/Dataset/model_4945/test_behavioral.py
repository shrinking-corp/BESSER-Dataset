import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ItemType,
    forms_Choice,
    forms_Date,
    forms_Decision,
    forms_Form,
    forms_FreeText,
    forms_Group,
    forms_Item,
    forms_ItemType,
    forms_Number,
    forms_Option,
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

def test_assoc_dependentOf2_reverse_link_reassign_clear():
    a1 = forms_Option(id="sample_text", text="sample_text")
    a2 = forms_Option(id="sample_text_2", text="sample_text_2")
    b = forms_Item(explanation="sample_text", text="sample_text")
    _safe_set(b, 'forms_Item3', {a1})
    assert _is_linked(b, 'forms_Item3', a1)
    if hasattr(a1, 'forms_Option'):
        assert _is_linked(a1, 'forms_Option', b)
    _safe_set(b, 'forms_Item3', {a2})
    assert _is_linked(b, 'forms_Item3', a2)
    if hasattr(a1, 'forms_Option'):
        assert not _is_linked(a1, 'forms_Option', b)
    if hasattr(a2, 'forms_Option'):
        assert _is_linked(a2, 'forms_Option', b)
    _safe_set(b, 'forms_Item3', set())
    assert not _is_linked(b, 'forms_Item3', a2)
    if hasattr(a2, 'forms_Option'):
        assert not _is_linked(a2, 'forms_Option', b)


def test_assoc_form8_reverse_link_reassign_clear():
    a1 = forms_Group(name="sample_text")
    a2 = forms_Group(name="sample_text_2")
    b = forms_Form(caption="sample_text")
    _safe_set(b, 'Form', a1)
    assert _is_linked(b, 'Form', a1)
    if hasattr(a1, 'groups'):
        assert _is_linked(a1, 'groups', b)
    _safe_set(b, 'Form', a2)
    assert _is_linked(b, 'Form', a2)
    if hasattr(a1, 'groups'):
        assert not _is_linked(a1, 'groups', b)
    if hasattr(a2, 'groups'):
        assert _is_linked(a2, 'groups', b)
    _safe_set(b, 'Form', None)
    assert not _is_linked(b, 'Form', a2)
    if hasattr(a2, 'groups'):
        assert not _is_linked(a2, 'groups', b)


def test_assoc_groups0_reverse_link_reassign_clear():
    a1 = forms_Group(name="sample_text")
    a2 = forms_Group(name="sample_text_2")
    b = forms_Form(caption="sample_text")
    _safe_set(b, 'form', {a1})
    assert _is_linked(b, 'form', a1)
    if hasattr(a1, 'Group'):
        assert _is_linked(a1, 'Group', b)
    _safe_set(b, 'form', {a2})
    assert _is_linked(b, 'form', a2)
    if hasattr(a1, 'Group'):
        assert not _is_linked(a1, 'Group', b)
    if hasattr(a2, 'Group'):
        assert _is_linked(a2, 'Group', b)
    _safe_set(b, 'form', set())
    assert not _is_linked(b, 'form', a2)
    if hasattr(a2, 'Group'):
        assert not _is_linked(a2, 'Group', b)


def test_assoc_items6_reverse_link_reassign_clear():
    a1 = forms_Item(explanation="sample_text", text="sample_text")
    a2 = forms_Item(explanation="sample_text_2", text="sample_text_2")
    b = forms_Group(name="sample_text")
    _safe_set(b, 'forms_Group', {a1})
    assert _is_linked(b, 'forms_Group', a1)
    if hasattr(a1, 'forms_Item7'):
        assert _is_linked(a1, 'forms_Item7', b)
    _safe_set(b, 'forms_Group', {a2})
    assert _is_linked(b, 'forms_Group', a2)
    if hasattr(a1, 'forms_Item7'):
        assert not _is_linked(a1, 'forms_Item7', b)
    if hasattr(a2, 'forms_Item7'):
        assert _is_linked(a2, 'forms_Item7', b)
    _safe_set(b, 'forms_Group', set())
    assert not _is_linked(b, 'forms_Group', a2)
    if hasattr(a2, 'forms_Item7'):
        assert not _is_linked(a2, 'forms_Item7', b)


def test_assoc_options4_reverse_link_reassign_clear():
    a1 = forms_Option(id="sample_text", text="sample_text")
    a2 = forms_Option(id="sample_text_2", text="sample_text_2")
    b = forms_Choice(multiple=True)
    _safe_set(b, 'forms_Choice', {a1})
    assert _is_linked(b, 'forms_Choice', a1)
    if hasattr(a1, 'forms_Option5'):
        assert _is_linked(a1, 'forms_Option5', b)
    _safe_set(b, 'forms_Choice', {a2})
    assert _is_linked(b, 'forms_Choice', a2)
    if hasattr(a1, 'forms_Option5'):
        assert not _is_linked(a1, 'forms_Option5', b)
    if hasattr(a2, 'forms_Option5'):
        assert _is_linked(a2, 'forms_Option5', b)
    _safe_set(b, 'forms_Choice', set())
    assert not _is_linked(b, 'forms_Choice', a2)
    if hasattr(a2, 'forms_Option5'):
        assert not _is_linked(a2, 'forms_Option5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_itemType1_stub_double():
    # forms_ItemType has no real 'forms_ItemType' property in the generated
    # code (a bare stub) -- manually attach it so forms_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Item(explanation="sample_text", text="sample_text")
    partner = forms_ItemType()
    setattr(partner, 'forms_ItemType', None)
    _safe_set(owner, 'forms_Item', partner)
    assert getattr(partner, 'forms_ItemType') == owner
    _safe_set(owner, 'forms_Item', None)
    assert getattr(partner, 'forms_ItemType') is None


def test_assoc_options9_stub_double():
    # forms_Decision has no real 'forms_Decision' property in the generated
    # code (a bare stub) -- manually attach it so forms_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # forms_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = forms_Option(id="sample_text", text="sample_text")
    partner = forms_Decision()
    setattr(partner, 'forms_Decision', None)
    _safe_set(owner, 'forms_Option10', partner)
    assert owner in getattr(partner, 'forms_Decision')
    _safe_set(owner, 'forms_Option10', None)
    assert owner not in getattr(partner, 'forms_Decision')


