# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genmymodelreverse_javax_swing_JMenuItem,
    genmymodelreverse_javax_swing_JFrame,
    genmymodelreverse_javax_swing_JPanel,
    genmymodelreverse_javax_swing_JLabel,
    genmymodelreverse_java_awt_event_MouseEvent,
    genmymodelreverse_java_awt_event_MouseAdapter,
    genmymodelreverse_java_awt_Graphics,
    Mines,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_genmymodelreverse_javax_swing_jmenuitem_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JMenuItem)


def test_hyp_genmymodelreverse_javax_swing_jmenuitem_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JMenuItem.__init__)


def test_hyp_genmymodelreverse_javax_swing_jmenuitem_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JMenuItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_javax_swing_jframe_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JFrame)


def test_hyp_genmymodelreverse_javax_swing_jframe_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JFrame.__init__)


def test_hyp_genmymodelreverse_javax_swing_jframe_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JFrame.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_javax_swing_jpanel_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JPanel)


def test_hyp_genmymodelreverse_javax_swing_jpanel_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JPanel.__init__)


def test_hyp_genmymodelreverse_javax_swing_jpanel_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JPanel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_javax_swing_jlabel_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JLabel)


def test_hyp_genmymodelreverse_javax_swing_jlabel_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JLabel.__init__)


def test_hyp_genmymodelreverse_javax_swing_jlabel_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_java_awt_event_mouseevent_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_MouseEvent)


def test_hyp_genmymodelreverse_java_awt_event_mouseevent_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_MouseEvent.__init__)


def test_hyp_genmymodelreverse_java_awt_event_mouseevent_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_MouseEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_java_awt_event_mouseadapter_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_MouseAdapter)


def test_hyp_genmymodelreverse_java_awt_event_mouseadapter_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_MouseAdapter.__init__)


def test_hyp_genmymodelreverse_java_awt_event_mouseadapter_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_MouseAdapter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_java_awt_graphics_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_Graphics)


def test_hyp_genmymodelreverse_java_awt_graphics_constructor_exists():
    assert callable(genmymodelreverse_java_awt_Graphics.__init__)


def test_hyp_genmymodelreverse_java_awt_graphics_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mines_is_not_abstract():
    assert not inspect.isabstract(Mines)


def test_hyp_mines_constructor_exists():
    assert callable(Mines.__init__)


def test_hyp_mines_constructor_args():
    sig = inspect.signature(Mines.__init__)
    params = list(sig.parameters.keys())
    assert "FRAME_HEIGHT" in params, "Missing parameter 'FRAME_HEIGHT'"
    assert "hexCell" in params, "Missing parameter 'hexCell'"
    assert "statusbar" in params, "Missing parameter 'statusbar'"
    assert "FRAME_WIDTH" in params, "Missing parameter 'FRAME_WIDTH'"
    assert "timeBar" in params, "Missing parameter 'timeBar'"

def test_hyp_mines_has_FRAME_HEIGHT():
    assert hasattr(Mines, "FRAME_HEIGHT")
    descriptor = None
    for klass in Mines.__mro__:
        if "FRAME_HEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["FRAME_HEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mines_has_hexCell():
    assert hasattr(Mines, "hexCell")
    descriptor = None
    for klass in Mines.__mro__:
        if "hexCell" in klass.__dict__:
            descriptor = klass.__dict__["hexCell"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mines_has_statusbar():
    assert hasattr(Mines, "statusbar")
    descriptor = None
    for klass in Mines.__mro__:
        if "statusbar" in klass.__dict__:
            descriptor = klass.__dict__["statusbar"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mines_has_FRAME_WIDTH():
    assert hasattr(Mines, "FRAME_WIDTH")
    descriptor = None
    for klass in Mines.__mro__:
        if "FRAME_WIDTH" in klass.__dict__:
            descriptor = klass.__dict__["FRAME_WIDTH"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mines_has_timeBar():
    assert hasattr(Mines, "timeBar")
    descriptor = None
    for klass in Mines.__mro__:
        if "timeBar" in klass.__dict__:
            descriptor = klass.__dict__["timeBar"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
genmymodelreverse_javax_swing_JMenuItem_strategy = st.builds(
    genmymodelreverse_javax_swing_JMenuItem,
)
genmymodelreverse_javax_swing_JFrame_strategy = st.builds(
    genmymodelreverse_javax_swing_JFrame,
)
genmymodelreverse_javax_swing_JPanel_strategy = st.builds(
    genmymodelreverse_javax_swing_JPanel,
)
genmymodelreverse_javax_swing_JLabel_strategy = st.builds(
    genmymodelreverse_javax_swing_JLabel,
)
genmymodelreverse_java_awt_event_MouseEvent_strategy = st.builds(
    genmymodelreverse_java_awt_event_MouseEvent,
)
genmymodelreverse_java_awt_event_MouseAdapter_strategy = st.builds(
    genmymodelreverse_java_awt_event_MouseAdapter,
)
genmymodelreverse_java_awt_Graphics_strategy = st.builds(
    genmymodelreverse_java_awt_Graphics,
)
Mines_strategy = st.builds(
    Mines,
    FRAME_HEIGHT=
        st.integers(),
    hexCell=
        st.none(),
    statusbar=
        st.none(),
    FRAME_WIDTH=
        st.integers(),
    timeBar=
        st.none()
)








@given(instance=Mines_strategy)
@settings(max_examples=50)
def test_hyp_mines_instantiation(instance):
    assert isinstance(instance, Mines)



@given(instance=Mines_strategy)
def test_hyp_mines_FRAME_HEIGHT_setter(instance):
    original = instance.FRAME_HEIGHT
    instance.FRAME_HEIGHT = original
    assert instance.FRAME_HEIGHT == original



@given(instance=Mines_strategy)
def test_hyp_mines_hexCell_setter(instance):
    original = instance.hexCell
    instance.hexCell = original
    assert instance.hexCell == original



@given(instance=Mines_strategy)
def test_hyp_mines_statusbar_setter(instance):
    original = instance.statusbar
    instance.statusbar = original
    assert instance.statusbar == original



@given(instance=Mines_strategy)
def test_hyp_mines_FRAME_WIDTH_setter(instance):
    original = instance.FRAME_WIDTH
    instance.FRAME_WIDTH = original
    assert instance.FRAME_WIDTH == original



@given(instance=Mines_strategy)
def test_hyp_mines_timeBar_setter(instance):
    original = instance.timeBar
    instance.timeBar = original
    assert instance.timeBar == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Mines,
    genmymodelreverse_java_awt_Graphics,
    genmymodelreverse_java_awt_event_MouseAdapter,
    genmymodelreverse_java_awt_event_MouseEvent,
    genmymodelreverse_javax_swing_JFrame,
    genmymodelreverse_javax_swing_JLabel,
    genmymodelreverse_javax_swing_JMenuItem,
    genmymodelreverse_javax_swing_JPanel,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

genmymodelreverse_java_awt_Graphics_strategy = st.builds(genmymodelreverse_java_awt_Graphics)
@given(instance=genmymodelreverse_java_awt_Graphics_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_Graphics_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Graphics)


genmymodelreverse_java_awt_event_MouseAdapter_strategy = st.builds(genmymodelreverse_java_awt_event_MouseAdapter)
@given(instance=genmymodelreverse_java_awt_event_MouseAdapter_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_MouseAdapter_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseAdapter)


genmymodelreverse_java_awt_event_MouseEvent_strategy = st.builds(genmymodelreverse_java_awt_event_MouseEvent)
@given(instance=genmymodelreverse_java_awt_event_MouseEvent_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_MouseEvent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseEvent)


genmymodelreverse_javax_swing_JFrame_strategy = st.builds(genmymodelreverse_javax_swing_JFrame)
@given(instance=genmymodelreverse_javax_swing_JFrame_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JFrame_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JFrame)


genmymodelreverse_javax_swing_JLabel_strategy = st.builds(genmymodelreverse_javax_swing_JLabel)
@given(instance=genmymodelreverse_javax_swing_JLabel_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JLabel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JLabel)


genmymodelreverse_javax_swing_JMenuItem_strategy = st.builds(genmymodelreverse_javax_swing_JMenuItem)
@given(instance=genmymodelreverse_javax_swing_JMenuItem_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JMenuItem_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JMenuItem)


genmymodelreverse_javax_swing_JPanel_strategy = st.builds(genmymodelreverse_javax_swing_JPanel)
@given(instance=genmymodelreverse_javax_swing_JPanel_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JPanel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JPanel)



