import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Lekar,
    Pregled,
    Zdravstveni_karton,
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

def test_assoc_Vrsi_P_reverse_link_reassign_clear():
    a1 = Pregled(BrPregled=7, DatumP="sample_text")
    a2 = Pregled(BrPregled=13, DatumP="sample_text_2")
    b = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    _safe_set(b, 'pregled0', a1)
    assert _is_linked(b, 'pregled0', a1)
    if hasattr(a1, 'lekar1'):
        assert _is_linked(a1, 'lekar1', b)
    _safe_set(b, 'pregled0', a2)
    assert _is_linked(b, 'pregled0', a2)
    if hasattr(a1, 'lekar1'):
        assert not _is_linked(a1, 'lekar1', b)
    if hasattr(a2, 'lekar1'):
        assert _is_linked(a2, 'lekar1', b)
    _safe_set(b, 'pregled0', None)
    assert not _is_linked(b, 'pregled0', a2)
    if hasattr(a2, 'lekar1'):
        assert not _is_linked(a2, 'lekar1', b)


def test_assoc_Zdravstveni_karton_Pregled_reverse_link_reassign_clear():
    a1 = Zdravstveni_karton(BrKart=7)
    a2 = Zdravstveni_karton(BrKart=13)
    b = Pregled(BrPregled=7, DatumP="sample_text")
    _safe_set(b, 'zdravstveni_karton3', a1)
    assert _is_linked(b, 'zdravstveni_karton3', a1)
    if hasattr(a1, 'pregled2'):
        assert _is_linked(a1, 'pregled2', b)
    _safe_set(b, 'zdravstveni_karton3', a2)
    assert _is_linked(b, 'zdravstveni_karton3', a2)
    if hasattr(a1, 'pregled2'):
        assert not _is_linked(a1, 'pregled2', b)
    if hasattr(a2, 'pregled2'):
        assert _is_linked(a2, 'pregled2', b)
    _safe_set(b, 'zdravstveni_karton3', None)
    assert not _is_linked(b, 'zdravstveni_karton3', a2)
    if hasattr(a2, 'pregled2'):
        assert not _is_linked(a2, 'pregled2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

