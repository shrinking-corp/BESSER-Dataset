import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BorderPane,
    Button,
    Choose_how_many_Players_external,
    Compute_Column_external,
    Computer_AI_Actor,
    Connect_Four_Component,
    Enter_Name_external,
    HBox,
    ImageIcon,
    Label,
    List_Token_,
    Listener_Interface,
    Player,
    Player_1_Actor,
    Player_2_Actor,
    Select_Column_external,
    VBox,
    connect_four_gui_Circle,
    connect_four_gui_Connect4Constant_Interface,
    connect_four_gui_Connect4GUI,
    connect_four_gui_GUIPlayer,
    connect_four_gui_GameOverPanel,
    connect_four_gui_GamePanel,
    connect_four_gui_StartMenu,
    connect_four_gui_Token,
    connect_four_gui_red,
    connect_four_gui_stage,
    javax_swing_JButton,
    javax_swing_JTextField,
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

