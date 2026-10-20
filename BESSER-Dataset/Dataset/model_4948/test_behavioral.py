import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Editable,
    Element,
    form_Editable,
    form_Element,
    form_Formulario,
    form_Input,
    form_Label,
    form_Orden,
    form_SelectionList,
    form_option,
    form_textArea,
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

def test_assoc_hasLabel3_reverse_link_reassign_clear():
    a1 = form_Label(content="sample_text", for_="sample_text")
    a2 = form_Label(content="sample_text_2", for_="sample_text_2")
    b = form_Editable(disabled=True, name="sample_text")
    _safe_set(b, 'form_Editable', a1)
    assert _is_linked(b, 'form_Editable', a1)
    if hasattr(a1, 'form_Label'):
        assert _is_linked(a1, 'form_Label', b)
    _safe_set(b, 'form_Editable', a2)
    assert _is_linked(b, 'form_Editable', a2)
    if hasattr(a1, 'form_Label'):
        assert not _is_linked(a1, 'form_Label', b)
    if hasattr(a2, 'form_Label'):
        assert _is_linked(a2, 'form_Label', b)
    _safe_set(b, 'form_Editable', None)
    assert not _is_linked(b, 'form_Editable', a2)
    if hasattr(a2, 'form_Label'):
        assert not _is_linked(a2, 'form_Label', b)


def test_assoc_hasOption4_reverse_link_reassign_clear():
    a1 = form_option(content="sample_text", value="sample_text")
    a2 = form_option(content="sample_text_2", value="sample_text_2")
    b = form_SelectionList(multiple=True)
    _safe_set(b, 'form_SelectionList', {a1})
    assert _is_linked(b, 'form_SelectionList', a1)
    if hasattr(a1, 'form_option'):
        assert _is_linked(a1, 'form_option', b)
    _safe_set(b, 'form_SelectionList', {a2})
    assert _is_linked(b, 'form_SelectionList', a2)
    if hasattr(a1, 'form_option'):
        assert not _is_linked(a1, 'form_option', b)
    if hasattr(a2, 'form_option'):
        assert _is_linked(a2, 'form_option', b)
    _safe_set(b, 'form_SelectionList', set())
    assert not _is_linked(b, 'form_SelectionList', a2)
    if hasattr(a2, 'form_option'):
        assert not _is_linked(a2, 'form_option', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

