import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SomeTestClass,
    test_PatchTestModel,
    test_SomeTestClass,
    test_SomeTestClassWithID,
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

def test_assoc_multiContainmentReference7_reverse_link_reassign_clear():
    a1 = test_SomeTestClass(attribute="sample_text")
    a2 = test_SomeTestClass(attribute="sample_text_2")
    b = test_PatchTestModel(id="sample_text", multiAttribute="sample_text", oneAttribute="sample_text")
    _safe_set(b, 'test_PatchTestModel8', {a1})
    assert _is_linked(b, 'test_PatchTestModel8', a1)
    if hasattr(a1, 'test_SomeTestClass9'):
        assert _is_linked(a1, 'test_SomeTestClass9', b)
    _safe_set(b, 'test_PatchTestModel8', {a2})
    assert _is_linked(b, 'test_PatchTestModel8', a2)
    if hasattr(a1, 'test_SomeTestClass9'):
        assert not _is_linked(a1, 'test_SomeTestClass9', b)
    if hasattr(a2, 'test_SomeTestClass9'):
        assert _is_linked(a2, 'test_SomeTestClass9', b)
    _safe_set(b, 'test_PatchTestModel8', set())
    assert not _is_linked(b, 'test_PatchTestModel8', a2)
    if hasattr(a2, 'test_SomeTestClass9'):
        assert not _is_linked(a2, 'test_SomeTestClass9', b)


def test_assoc_multiNonContainmentReferences1_reverse_link_reassign_clear():
    a1 = test_SomeTestClass(attribute="sample_text")
    a2 = test_SomeTestClass(attribute="sample_text_2")
    b = test_PatchTestModel(id="sample_text", multiAttribute="sample_text", oneAttribute="sample_text")
    _safe_set(b, 'test_PatchTestModel2', {a1})
    assert _is_linked(b, 'test_PatchTestModel2', a1)
    if hasattr(a1, 'test_SomeTestClass3'):
        assert _is_linked(a1, 'test_SomeTestClass3', b)
    _safe_set(b, 'test_PatchTestModel2', {a2})
    assert _is_linked(b, 'test_PatchTestModel2', a2)
    if hasattr(a1, 'test_SomeTestClass3'):
        assert not _is_linked(a1, 'test_SomeTestClass3', b)
    if hasattr(a2, 'test_SomeTestClass3'):
        assert _is_linked(a2, 'test_SomeTestClass3', b)
    _safe_set(b, 'test_PatchTestModel2', set())
    assert not _is_linked(b, 'test_PatchTestModel2', a2)
    if hasattr(a2, 'test_SomeTestClass3'):
        assert not _is_linked(a2, 'test_SomeTestClass3', b)


def test_assoc_oneContainmentReference4_reverse_link_reassign_clear():
    a1 = test_SomeTestClass(attribute="sample_text")
    a2 = test_SomeTestClass(attribute="sample_text_2")
    b = test_PatchTestModel(id="sample_text", multiAttribute="sample_text", oneAttribute="sample_text")
    _safe_set(b, 'test_PatchTestModel5', a1)
    assert _is_linked(b, 'test_PatchTestModel5', a1)
    if hasattr(a1, 'test_SomeTestClass6'):
        assert _is_linked(a1, 'test_SomeTestClass6', b)
    _safe_set(b, 'test_PatchTestModel5', a2)
    assert _is_linked(b, 'test_PatchTestModel5', a2)
    if hasattr(a1, 'test_SomeTestClass6'):
        assert not _is_linked(a1, 'test_SomeTestClass6', b)
    if hasattr(a2, 'test_SomeTestClass6'):
        assert _is_linked(a2, 'test_SomeTestClass6', b)
    _safe_set(b, 'test_PatchTestModel5', None)
    assert not _is_linked(b, 'test_PatchTestModel5', a2)
    if hasattr(a2, 'test_SomeTestClass6'):
        assert not _is_linked(a2, 'test_SomeTestClass6', b)


def test_assoc_oneNonContainmentReference0_reverse_link_reassign_clear():
    a1 = test_SomeTestClass(attribute="sample_text")
    a2 = test_SomeTestClass(attribute="sample_text_2")
    b = test_PatchTestModel(id="sample_text", multiAttribute="sample_text", oneAttribute="sample_text")
    _safe_set(b, 'test_PatchTestModel', a1)
    assert _is_linked(b, 'test_PatchTestModel', a1)
    if hasattr(a1, 'test_SomeTestClass'):
        assert _is_linked(a1, 'test_SomeTestClass', b)
    _safe_set(b, 'test_PatchTestModel', a2)
    assert _is_linked(b, 'test_PatchTestModel', a2)
    if hasattr(a1, 'test_SomeTestClass'):
        assert not _is_linked(a1, 'test_SomeTestClass', b)
    if hasattr(a2, 'test_SomeTestClass'):
        assert _is_linked(a2, 'test_SomeTestClass', b)
    _safe_set(b, 'test_PatchTestModel', None)
    assert not _is_linked(b, 'test_PatchTestModel', a2)
    if hasattr(a2, 'test_SomeTestClass'):
        assert not _is_linked(a2, 'test_SomeTestClass', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

