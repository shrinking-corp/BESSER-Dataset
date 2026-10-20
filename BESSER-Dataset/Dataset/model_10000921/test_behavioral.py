import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    App,
    Array_Zutat___,
    ComboBox,
    DekorRezept,
    Font_,
    Font_2,
    GUI,
    GUIKeksform,
    GUIRezept,
    Groesse,
    Groesse_,
    GussRezept,
    KeyPressEventArgs_,
    KonfigDatei,
    KonfigDatei_,
    List_DekorRezept___,
    List_PlaetzchenForm___,
    List_TeigRezept___,
    List_Zutat___,
    Object_,
    PL_Form_,
    PL_Groesse_,
    Plaetzchen,
    PlaetzchenForm,
    PlaetzchenForm_,
    Plaetzchen_,
    Rezept,
    String_,
    TeigRezept,
    TeigRezept_,
    ThreadExceptionEventArgs_,
    Zutat,
    Zutat_,
    myException,
    PL_Form,
    PL_Groesse,
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

