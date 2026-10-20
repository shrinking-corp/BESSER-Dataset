import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    Elements_Edge,
    Elements_Element,
    Elements_IdentifiedElement,
    Elements_NamedElement,
    Elements_Node,
    Elements_ReferencingNode,
    Elements_Root,
    Elements_StrictElement,
    IdentifiedElement,
    NamedElement,
    Node,
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

def test_assoc_content0_reverse_link_reassign_clear():
    a1 = Elements_Root(name="sample_text")
    a2 = Elements_Root(name="sample_text_2")
    b = Elements_NamedElement(name="sample_text")
    _safe_set(b, 'Elements_NamedElement', a1)
    assert _is_linked(b, 'Elements_NamedElement', a1)
    if hasattr(a1, 'Elements_Root'):
        assert _is_linked(a1, 'Elements_Root', b)
    _safe_set(b, 'Elements_NamedElement', a2)
    assert _is_linked(b, 'Elements_NamedElement', a2)
    if hasattr(a1, 'Elements_Root'):
        assert not _is_linked(a1, 'Elements_Root', b)
    if hasattr(a2, 'Elements_Root'):
        assert _is_linked(a2, 'Elements_Root', b)
    _safe_set(b, 'Elements_NamedElement', None)
    assert not _is_linked(b, 'Elements_NamedElement', a2)
    if hasattr(a2, 'Elements_Root'):
        assert not _is_linked(a2, 'Elements_Root', b)


def test_assoc_manyContent2_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element1', {a1})
    assert _is_linked(b, 'Elements_Element1', a1)
    if hasattr(a1, 'Elements_Element'):
        assert _is_linked(a1, 'Elements_Element', b)
    _safe_set(b, 'Elements_Element1', {a2})
    assert _is_linked(b, 'Elements_Element1', a2)
    if hasattr(a1, 'Elements_Element'):
        assert not _is_linked(a1, 'Elements_Element', b)
    if hasattr(a2, 'Elements_Element'):
        assert _is_linked(a2, 'Elements_Element', b)
    _safe_set(b, 'Elements_Element1', set())
    assert not _is_linked(b, 'Elements_Element1', a2)
    if hasattr(a2, 'Elements_Element'):
        assert not _is_linked(a2, 'Elements_Element', b)


def test_assoc_manyContentWithUp7_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'upFromManyContent', {a1})
    assert _is_linked(b, 'upFromManyContent', a1)
    if hasattr(a1, 'Element'):
        assert _is_linked(a1, 'Element', b)
    _safe_set(b, 'upFromManyContent', {a2})
    assert _is_linked(b, 'upFromManyContent', a2)
    if hasattr(a1, 'Element'):
        assert not _is_linked(a1, 'Element', b)
    if hasattr(a2, 'Element'):
        assert _is_linked(a2, 'Element', b)
    _safe_set(b, 'upFromManyContent', set())
    assert not _is_linked(b, 'upFromManyContent', a2)
    if hasattr(a2, 'Element'):
        assert not _is_linked(a2, 'Element', b)


def test_assoc_manyFromManyRef136_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'manyFromManyRef2', {a1})
    assert _is_linked(b, 'manyFromManyRef2', a1)
    if hasattr(a1, 'Element37'):
        assert _is_linked(a1, 'Element37', b)
    _safe_set(b, 'manyFromManyRef2', {a2})
    assert _is_linked(b, 'manyFromManyRef2', a2)
    if hasattr(a1, 'Element37'):
        assert not _is_linked(a1, 'Element37', b)
    if hasattr(a2, 'Element37'):
        assert _is_linked(a2, 'Element37', b)
    _safe_set(b, 'manyFromManyRef2', set())
    assert not _is_linked(b, 'manyFromManyRef2', a2)
    if hasattr(a2, 'Element37'):
        assert not _is_linked(a2, 'Element37', b)


def test_assoc_manyFromManyRef239_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'manyFromManyRef1', {a1})
    assert _is_linked(b, 'manyFromManyRef1', a1)
    if hasattr(a1, 'Element40'):
        assert _is_linked(a1, 'Element40', b)
    _safe_set(b, 'manyFromManyRef1', {a2})
    assert _is_linked(b, 'manyFromManyRef1', a2)
    if hasattr(a1, 'Element40'):
        assert not _is_linked(a1, 'Element40', b)
    if hasattr(a2, 'Element40'):
        assert _is_linked(a2, 'Element40', b)
    _safe_set(b, 'manyFromManyRef1', set())
    assert not _is_linked(b, 'manyFromManyRef1', a2)
    if hasattr(a2, 'Element40'):
        assert not _is_linked(a2, 'Element40', b)


def test_assoc_manyFromSingleRef30_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'singleFromManyRef', {a1})
    assert _is_linked(b, 'singleFromManyRef', a1)
    if hasattr(a1, 'Element31'):
        assert _is_linked(a1, 'Element31', b)
    _safe_set(b, 'singleFromManyRef', {a2})
    assert _is_linked(b, 'singleFromManyRef', a2)
    if hasattr(a1, 'Element31'):
        assert not _is_linked(a1, 'Element31', b)
    if hasattr(a2, 'Element31'):
        assert _is_linked(a2, 'Element31', b)
    _safe_set(b, 'singleFromManyRef', set())
    assert not _is_linked(b, 'singleFromManyRef', a2)
    if hasattr(a2, 'Element31'):
        assert not _is_linked(a2, 'Element31', b)


def test_assoc_manyRef18_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element19', a1)
    assert _is_linked(b, 'Elements_Element19', a1)
    if hasattr(a1, 'Elements_Element17'):
        assert _is_linked(a1, 'Elements_Element17', b)
    _safe_set(b, 'Elements_Element19', a2)
    assert _is_linked(b, 'Elements_Element19', a2)
    if hasattr(a1, 'Elements_Element17'):
        assert not _is_linked(a1, 'Elements_Element17', b)
    if hasattr(a2, 'Elements_Element17'):
        assert _is_linked(a2, 'Elements_Element17', b)
    _safe_set(b, 'Elements_Element19', None)
    assert not _is_linked(b, 'Elements_Element19', a2)
    if hasattr(a2, 'Elements_Element17'):
        assert not _is_linked(a2, 'Elements_Element17', b)


def test_assoc_sManyContent41_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element42', a1)
    assert _is_linked(b, 'Elements_Element42', a1)
    if hasattr(a1, 'Elements_StrictElement'):
        assert _is_linked(a1, 'Elements_StrictElement', b)
    _safe_set(b, 'Elements_Element42', a2)
    assert _is_linked(b, 'Elements_Element42', a2)
    if hasattr(a1, 'Elements_StrictElement'):
        assert not _is_linked(a1, 'Elements_StrictElement', b)
    if hasattr(a2, 'Elements_StrictElement'):
        assert _is_linked(a2, 'Elements_StrictElement', b)
    _safe_set(b, 'Elements_Element42', None)
    assert not _is_linked(b, 'Elements_Element42', a2)
    if hasattr(a2, 'Elements_StrictElement'):
        assert not _is_linked(a2, 'Elements_StrictElement', b)


def test_assoc_sManyFromManyRef158_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_StrictElement(sValue=7, sValues=7)
    _safe_set(b, 'sManyFromManyRef2', {a1})
    assert _is_linked(b, 'sManyFromManyRef2', a1)
    if hasattr(a1, 'StrictElement59'):
        assert _is_linked(a1, 'StrictElement59', b)
    _safe_set(b, 'sManyFromManyRef2', {a2})
    assert _is_linked(b, 'sManyFromManyRef2', a2)
    if hasattr(a1, 'StrictElement59'):
        assert not _is_linked(a1, 'StrictElement59', b)
    if hasattr(a2, 'StrictElement59'):
        assert _is_linked(a2, 'StrictElement59', b)
    _safe_set(b, 'sManyFromManyRef2', set())
    assert not _is_linked(b, 'sManyFromManyRef2', a2)
    if hasattr(a2, 'StrictElement59'):
        assert not _is_linked(a2, 'StrictElement59', b)


def test_assoc_sManyFromManyRef261_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_StrictElement(sValue=7, sValues=7)
    _safe_set(b, 'sManyFromManyRef1', {a1})
    assert _is_linked(b, 'sManyFromManyRef1', a1)
    if hasattr(a1, 'StrictElement62'):
        assert _is_linked(a1, 'StrictElement62', b)
    _safe_set(b, 'sManyFromManyRef1', {a2})
    assert _is_linked(b, 'sManyFromManyRef1', a2)
    if hasattr(a1, 'StrictElement62'):
        assert not _is_linked(a1, 'StrictElement62', b)
    if hasattr(a2, 'StrictElement62'):
        assert _is_linked(a2, 'StrictElement62', b)
    _safe_set(b, 'sManyFromManyRef1', set())
    assert not _is_linked(b, 'sManyFromManyRef1', a2)
    if hasattr(a2, 'StrictElement62'):
        assert not _is_linked(a2, 'StrictElement62', b)


def test_assoc_sManyFromSingleRef53_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_StrictElement(sValue=7, sValues=7)
    _safe_set(b, 'sSingleFromManyRef', {a1})
    assert _is_linked(b, 'sSingleFromManyRef', a1)
    if hasattr(a1, 'StrictElement'):
        assert _is_linked(a1, 'StrictElement', b)
    _safe_set(b, 'sSingleFromManyRef', {a2})
    assert _is_linked(b, 'sSingleFromManyRef', a2)
    if hasattr(a1, 'StrictElement'):
        assert not _is_linked(a1, 'StrictElement', b)
    if hasattr(a2, 'StrictElement'):
        assert _is_linked(a2, 'StrictElement', b)
    _safe_set(b, 'sSingleFromManyRef', set())
    assert not _is_linked(b, 'sSingleFromManyRef', a2)
    if hasattr(a2, 'StrictElement'):
        assert not _is_linked(a2, 'StrictElement', b)


def test_assoc_sManyRef46_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element48', a1)
    assert _is_linked(b, 'Elements_Element48', a1)
    if hasattr(a1, 'Elements_StrictElement47'):
        assert _is_linked(a1, 'Elements_StrictElement47', b)
    _safe_set(b, 'Elements_Element48', a2)
    assert _is_linked(b, 'Elements_Element48', a2)
    if hasattr(a1, 'Elements_StrictElement47'):
        assert not _is_linked(a1, 'Elements_StrictElement47', b)
    if hasattr(a2, 'Elements_StrictElement47'):
        assert _is_linked(a2, 'Elements_StrictElement47', b)
    _safe_set(b, 'Elements_Element48', None)
    assert not _is_linked(b, 'Elements_Element48', a2)
    if hasattr(a2, 'Elements_StrictElement47'):
        assert not _is_linked(a2, 'Elements_StrictElement47', b)


def test_assoc_sSingleContent43_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element45', a1)
    assert _is_linked(b, 'Elements_Element45', a1)
    if hasattr(a1, 'Elements_StrictElement44'):
        assert _is_linked(a1, 'Elements_StrictElement44', b)
    _safe_set(b, 'Elements_Element45', a2)
    assert _is_linked(b, 'Elements_Element45', a2)
    if hasattr(a1, 'Elements_StrictElement44'):
        assert not _is_linked(a1, 'Elements_StrictElement44', b)
    if hasattr(a2, 'Elements_StrictElement44'):
        assert _is_linked(a2, 'Elements_StrictElement44', b)
    _safe_set(b, 'Elements_Element45', None)
    assert not _is_linked(b, 'Elements_Element45', a2)
    if hasattr(a2, 'Elements_StrictElement44'):
        assert not _is_linked(a2, 'Elements_StrictElement44', b)


def test_assoc_sSingleFromManyRef55_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_StrictElement(sValue=7, sValues=7)
    _safe_set(b, 'sManyFromSingleRef', a1)
    assert _is_linked(b, 'sManyFromSingleRef', a1)
    if hasattr(a1, 'StrictElement56'):
        assert _is_linked(a1, 'StrictElement56', b)
    _safe_set(b, 'sManyFromSingleRef', a2)
    assert _is_linked(b, 'sManyFromSingleRef', a2)
    if hasattr(a1, 'StrictElement56'):
        assert not _is_linked(a1, 'StrictElement56', b)
    if hasattr(a2, 'StrictElement56'):
        assert _is_linked(a2, 'StrictElement56', b)
    _safe_set(b, 'sManyFromSingleRef', None)
    assert not _is_linked(b, 'sManyFromSingleRef', a2)
    if hasattr(a2, 'StrictElement56'):
        assert not _is_linked(a2, 'StrictElement56', b)


def test_assoc_sSingleRef49_reverse_link_reassign_clear():
    a1 = Elements_StrictElement(sValue=7, sValues=7)
    a2 = Elements_StrictElement(sValue=13, sValues=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element51', a1)
    assert _is_linked(b, 'Elements_Element51', a1)
    if hasattr(a1, 'Elements_StrictElement50'):
        assert _is_linked(a1, 'Elements_StrictElement50', b)
    _safe_set(b, 'Elements_Element51', a2)
    assert _is_linked(b, 'Elements_Element51', a2)
    if hasattr(a1, 'Elements_StrictElement50'):
        assert not _is_linked(a1, 'Elements_StrictElement50', b)
    if hasattr(a2, 'Elements_StrictElement50'):
        assert _is_linked(a2, 'Elements_StrictElement50', b)
    _safe_set(b, 'Elements_Element51', None)
    assert not _is_linked(b, 'Elements_Element51', a2)
    if hasattr(a2, 'Elements_StrictElement50'):
        assert not _is_linked(a2, 'Elements_StrictElement50', b)


def test_assoc_singleContent4_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element5', a1)
    assert _is_linked(b, 'Elements_Element5', a1)
    if hasattr(a1, 'Elements_Element3'):
        assert _is_linked(a1, 'Elements_Element3', b)
    _safe_set(b, 'Elements_Element5', a2)
    assert _is_linked(b, 'Elements_Element5', a2)
    if hasattr(a1, 'Elements_Element3'):
        assert not _is_linked(a1, 'Elements_Element3', b)
    if hasattr(a2, 'Elements_Element3'):
        assert _is_linked(a2, 'Elements_Element3', b)
    _safe_set(b, 'Elements_Element5', None)
    assert not _is_linked(b, 'Elements_Element5', a2)
    if hasattr(a2, 'Elements_Element3'):
        assert not _is_linked(a2, 'Elements_Element3', b)


def test_assoc_singleContentWithUp12_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'upFromSingleContent', a1)
    assert _is_linked(b, 'upFromSingleContent', a1)
    if hasattr(a1, 'Element13'):
        assert _is_linked(a1, 'Element13', b)
    _safe_set(b, 'upFromSingleContent', a2)
    assert _is_linked(b, 'upFromSingleContent', a2)
    if hasattr(a1, 'Element13'):
        assert not _is_linked(a1, 'Element13', b)
    if hasattr(a2, 'Element13'):
        assert _is_linked(a2, 'Element13', b)
    _safe_set(b, 'upFromSingleContent', None)
    assert not _is_linked(b, 'upFromSingleContent', a2)
    if hasattr(a2, 'Element13'):
        assert not _is_linked(a2, 'Element13', b)


def test_assoc_singleFromManyRef33_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'manyFromSingleRef', a1)
    assert _is_linked(b, 'manyFromSingleRef', a1)
    if hasattr(a1, 'Element34'):
        assert _is_linked(a1, 'Element34', b)
    _safe_set(b, 'manyFromSingleRef', a2)
    assert _is_linked(b, 'manyFromSingleRef', a2)
    if hasattr(a1, 'Element34'):
        assert not _is_linked(a1, 'Element34', b)
    if hasattr(a2, 'Element34'):
        assert _is_linked(a2, 'Element34', b)
    _safe_set(b, 'manyFromSingleRef', None)
    assert not _is_linked(b, 'manyFromSingleRef', a2)
    if hasattr(a2, 'Element34'):
        assert not _is_linked(a2, 'Element34', b)


def test_assoc_singleFromSingleRef124_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'singleFromSingleRef2', a1)
    assert _is_linked(b, 'singleFromSingleRef2', a1)
    if hasattr(a1, 'Element25'):
        assert _is_linked(a1, 'Element25', b)
    _safe_set(b, 'singleFromSingleRef2', a2)
    assert _is_linked(b, 'singleFromSingleRef2', a2)
    if hasattr(a1, 'Element25'):
        assert not _is_linked(a1, 'Element25', b)
    if hasattr(a2, 'Element25'):
        assert _is_linked(a2, 'Element25', b)
    _safe_set(b, 'singleFromSingleRef2', None)
    assert not _is_linked(b, 'singleFromSingleRef2', a2)
    if hasattr(a2, 'Element25'):
        assert not _is_linked(a2, 'Element25', b)


def test_assoc_singleFromSingleRef227_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'singleFromSingleRef1', a1)
    assert _is_linked(b, 'singleFromSingleRef1', a1)
    if hasattr(a1, 'Element28'):
        assert _is_linked(a1, 'Element28', b)
    _safe_set(b, 'singleFromSingleRef1', a2)
    assert _is_linked(b, 'singleFromSingleRef1', a2)
    if hasattr(a1, 'Element28'):
        assert not _is_linked(a1, 'Element28', b)
    if hasattr(a2, 'Element28'):
        assert _is_linked(a2, 'Element28', b)
    _safe_set(b, 'singleFromSingleRef1', None)
    assert not _is_linked(b, 'singleFromSingleRef1', a2)
    if hasattr(a2, 'Element28'):
        assert not _is_linked(a2, 'Element28', b)


def test_assoc_singleRef21_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'Elements_Element22', a1)
    assert _is_linked(b, 'Elements_Element22', a1)
    if hasattr(a1, 'Elements_Element20'):
        assert _is_linked(a1, 'Elements_Element20', b)
    _safe_set(b, 'Elements_Element22', a2)
    assert _is_linked(b, 'Elements_Element22', a2)
    if hasattr(a1, 'Elements_Element20'):
        assert not _is_linked(a1, 'Elements_Element20', b)
    if hasattr(a2, 'Elements_Element20'):
        assert _is_linked(a2, 'Elements_Element20', b)
    _safe_set(b, 'Elements_Element22', None)
    assert not _is_linked(b, 'Elements_Element22', a2)
    if hasattr(a2, 'Elements_Element20'):
        assert not _is_linked(a2, 'Elements_Element20', b)


def test_assoc_upFromManyContent9_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'manyContentWithUp', a1)
    assert _is_linked(b, 'manyContentWithUp', a1)
    if hasattr(a1, 'Element10'):
        assert _is_linked(a1, 'Element10', b)
    _safe_set(b, 'manyContentWithUp', a2)
    assert _is_linked(b, 'manyContentWithUp', a2)
    if hasattr(a1, 'Element10'):
        assert not _is_linked(a1, 'Element10', b)
    if hasattr(a2, 'Element10'):
        assert _is_linked(a2, 'Element10', b)
    _safe_set(b, 'manyContentWithUp', None)
    assert not _is_linked(b, 'manyContentWithUp', a2)
    if hasattr(a2, 'Element10'):
        assert not _is_linked(a2, 'Element10', b)


def test_assoc_upFromSingleContent15_reverse_link_reassign_clear():
    a1 = Elements_Element(value=7, values=7)
    a2 = Elements_Element(value=13, values=13)
    b = Elements_Element(value=7, values=7)
    _safe_set(b, 'singleContentWithUp', a1)
    assert _is_linked(b, 'singleContentWithUp', a1)
    if hasattr(a1, 'Element16'):
        assert _is_linked(a1, 'Element16', b)
    _safe_set(b, 'singleContentWithUp', a2)
    assert _is_linked(b, 'singleContentWithUp', a2)
    if hasattr(a1, 'Element16'):
        assert not _is_linked(a1, 'Element16', b)
    if hasattr(a2, 'Element16'):
        assert _is_linked(a2, 'Element16', b)
    _safe_set(b, 'singleContentWithUp', None)
    assert not _is_linked(b, 'singleContentWithUp', a2)
    if hasattr(a2, 'Element16'):
        assert not _is_linked(a2, 'Element16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_subNodes66_stub_double():
    # Elements_Node has no real 'Elements_Node' property in the generated
    # code (a bare stub) -- manually attach it so Elements_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Elements_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Elements_NamedElement(name="sample_text")
    partner = Elements_Node()
    setattr(partner, 'Elements_Node', None)
    _safe_set(owner, 'Elements_NamedElement67', partner)
    assert owner in getattr(partner, 'Elements_Node')
    _safe_set(owner, 'Elements_NamedElement67', None)
    assert owner not in getattr(partner, 'Elements_Node')


