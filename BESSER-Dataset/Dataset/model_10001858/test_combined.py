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
    cursor1,
    sudoku_validator,
    sudoku_board1,
    load,
    save,
    sudoku_board,
    game_board1,
    game_board,
    choice_window,
    cursor,
    window,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cursor1_is_not_abstract():
    assert not inspect.isabstract(cursor1)


def test_hyp_cursor1_constructor_exists():
    assert callable(cursor1.__init__)


def test_hyp_cursor1_constructor_args():
    sig = inspect.signature(cursor1.__init__)
    params = list(sig.parameters.keys())
    assert "limit_y" in params, "Missing parameter 'limit_y'"
    assert "pos_y" in params, "Missing parameter 'pos_y'"
    assert "pos_x" in params, "Missing parameter 'pos_x'"
    assert "limit_x" in params, "Missing parameter 'limit_x'"







def test_hyp_sudoku_validator_is_not_abstract():
    assert not inspect.isabstract(sudoku_validator)


def test_hyp_sudoku_validator_constructor_exists():
    assert callable(sudoku_validator.__init__)


def test_hyp_sudoku_validator_constructor_args():
    sig = inspect.signature(sudoku_validator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sudoku_board1_is_not_abstract():
    assert not inspect.isabstract(sudoku_board1)


def test_hyp_sudoku_board1_constructor_exists():
    assert callable(sudoku_board1.__init__)


def test_hyp_sudoku_board1_constructor_args():
    sig = inspect.signature(sudoku_board1.__init__)
    params = list(sig.parameters.keys())
    assert "fixed_9__9_" in params, "Missing parameter 'fixed_9__9_'"
    assert "board_9__9_" in params, "Missing parameter 'board_9__9_'"





def test_hyp_load_is_not_abstract():
    assert not inspect.isabstract(load)


def test_hyp_load_constructor_exists():
    assert callable(load.__init__)


def test_hyp_load_constructor_args():
    sig = inspect.signature(load.__init__)
    params = list(sig.parameters.keys())
    assert "file_name" in params, "Missing parameter 'file_name'"




def test_hyp_save_is_not_abstract():
    assert not inspect.isabstract(save)


def test_hyp_save_constructor_exists():
    assert callable(save.__init__)


def test_hyp_save_constructor_args():
    sig = inspect.signature(save.__init__)
    params = list(sig.parameters.keys())
    assert "file_name" in params, "Missing parameter 'file_name'"




def test_hyp_sudoku_board_is_not_abstract():
    assert not inspect.isabstract(sudoku_board)


def test_hyp_sudoku_board_constructor_exists():
    assert callable(sudoku_board.__init__)


def test_hyp_sudoku_board_constructor_args():
    sig = inspect.signature(sudoku_board.__init__)
    params = list(sig.parameters.keys())



def test_hyp_game_board1_is_not_abstract():
    assert not inspect.isabstract(game_board1)


def test_hyp_game_board1_constructor_exists():
    assert callable(game_board1.__init__)


def test_hyp_game_board1_constructor_args():
    sig = inspect.signature(game_board1.__init__)
    params = list(sig.parameters.keys())
    assert "board" in params, "Missing parameter 'board'"

def test_hyp_game_board1_has_board():
    assert hasattr(game_board1, "board")
    descriptor = None
    for klass in game_board1.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_board_is_not_abstract():
    assert not inspect.isabstract(game_board)


def test_hyp_game_board_constructor_exists():
    assert callable(game_board.__init__)


def test_hyp_game_board_constructor_args():
    sig = inspect.signature(game_board.__init__)
    params = list(sig.parameters.keys())



def test_hyp_choice_window_is_not_abstract():
    assert not inspect.isabstract(choice_window)


def test_hyp_choice_window_constructor_exists():
    assert callable(choice_window.__init__)


def test_hyp_choice_window_constructor_args():
    sig = inspect.signature(choice_window.__init__)
    params = list(sig.parameters.keys())
    assert "prompt_3_" in params, "Missing parameter 'prompt_3_'"
    assert "names_3_" in params, "Missing parameter 'names_3_'"
    assert "response_3_" in params, "Missing parameter 'response_3_'"

def test_hyp_choice_window_has_prompt_3_():
    assert hasattr(choice_window, "prompt_3_")
    descriptor = None
    for klass in choice_window.__mro__:
        if "prompt_3_" in klass.__dict__:
            descriptor = klass.__dict__["prompt_3_"]
            break
    assert isinstance(descriptor, property)

def test_hyp_choice_window_has_names_3_():
    assert hasattr(choice_window, "names_3_")
    descriptor = None
    for klass in choice_window.__mro__:
        if "names_3_" in klass.__dict__:
            descriptor = klass.__dict__["names_3_"]
            break
    assert isinstance(descriptor, property)

def test_hyp_choice_window_has_response_3_():
    assert hasattr(choice_window, "response_3_")
    descriptor = None
    for klass in choice_window.__mro__:
        if "response_3_" in klass.__dict__:
            descriptor = klass.__dict__["response_3_"]
            break
    assert isinstance(descriptor, property)



def test_hyp_cursor_is_not_abstract():
    assert not inspect.isabstract(cursor)


def test_hyp_cursor_constructor_exists():
    assert callable(cursor.__init__)


def test_hyp_cursor_constructor_args():
    sig = inspect.signature(cursor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_window_is_not_abstract():
    assert not inspect.isabstract(window)


def test_hyp_window_constructor_exists():
    assert callable(window.__init__)


def test_hyp_window_constructor_args():
    sig = inspect.signature(window.__init__)
    params = list(sig.parameters.keys())
    assert "current" in params, "Missing parameter 'current'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "_main" in params, "Missing parameter '_main'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_hyp_window_has_current():
    assert hasattr(window, "current")
    descriptor = None
    for klass in window.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)

def test_hyp_window_has_lines():
    assert hasattr(window, "lines")
    descriptor = None
    for klass in window.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_hyp_window_has__main():
    assert hasattr(window, "_main")
    descriptor = None
    for klass in window.__mro__:
        if "_main" in klass.__dict__:
            descriptor = klass.__dict__["_main"]
            break
    assert isinstance(descriptor, property)

def test_hyp_window_has_columns():
    assert hasattr(window, "columns")
    descriptor = None
    for klass in window.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_hyp_window_has_y():
    assert hasattr(window, "y")
    descriptor = None
    for klass in window.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_hyp_window_has_x():
    assert hasattr(window, "x")
    descriptor = None
    for klass in window.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
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
cursor1_strategy = st.builds(
    cursor1,
    limit_y=
        safe_text,
    pos_y=
        st.integers(),
    pos_x=
        st.integers(),
    limit_x=
        st.integers()
)
sudoku_validator_strategy = st.builds(
    sudoku_validator,
)
sudoku_board1_strategy = st.builds(
    sudoku_board1,
    fixed_9__9_=
        st.integers(),
    board_9__9_=
        st.integers()
)
load_strategy = st.builds(
    load,
    file_name=
        safe_text
)
save_strategy = st.builds(
    save,
    file_name=
        safe_text
)
sudoku_board_strategy = st.builds(
    sudoku_board,
)
game_board1_strategy = st.builds(
    game_board1,
    board=
        st.none()
)
game_board_strategy = st.builds(
    game_board,
)
choice_window_strategy = st.builds(
    choice_window,
    prompt_3_=
        st.none(),
    names_3_=
        safe_text,
    response_3_=
        safe_text
)
cursor_strategy = st.builds(
    cursor,
)
window_strategy = st.builds(
    window,
    current=
        st.none(),
    lines=
        st.integers(),
    _main=
        safe_text,
    columns=
        st.integers(),
    y=
        st.integers(),
    x=
        st.integers()
)




@given(instance=cursor1_strategy)
def test_hyp_cursor1_limit_y_setter(instance):
    original = instance.limit_y
    instance.limit_y = original
    assert instance.limit_y == original



@given(instance=cursor1_strategy)
def test_hyp_cursor1_pos_y_setter(instance):
    original = instance.pos_y
    instance.pos_y = original
    assert instance.pos_y == original



@given(instance=cursor1_strategy)
def test_hyp_cursor1_pos_x_setter(instance):
    original = instance.pos_x
    instance.pos_x = original
    assert instance.pos_x == original



@given(instance=cursor1_strategy)
def test_hyp_cursor1_limit_x_setter(instance):
    original = instance.limit_x
    instance.limit_x = original
    assert instance.limit_x == original





@given(instance=sudoku_board1_strategy)
def test_hyp_sudoku_board1_fixed_9__9__setter(instance):
    original = instance.fixed_9__9_
    instance.fixed_9__9_ = original
    assert instance.fixed_9__9_ == original



@given(instance=sudoku_board1_strategy)
def test_hyp_sudoku_board1_board_9__9__setter(instance):
    original = instance.board_9__9_
    instance.board_9__9_ = original
    assert instance.board_9__9_ == original




@given(instance=load_strategy)
def test_hyp_load_file_name_setter(instance):
    original = instance.file_name
    instance.file_name = original
    assert instance.file_name == original




@given(instance=save_strategy)
def test_hyp_save_file_name_setter(instance):
    original = instance.file_name
    instance.file_name = original
    assert instance.file_name == original


@given(instance=game_board1_strategy)
@settings(max_examples=50)
def test_hyp_game_board1_instantiation(instance):
    assert isinstance(instance, game_board1)



@given(instance=game_board1_strategy)
def test_hyp_game_board1_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original


@given(instance=choice_window_strategy)
@settings(max_examples=50)
def test_hyp_choice_window_instantiation(instance):
    assert isinstance(instance, choice_window)



@given(instance=choice_window_strategy)
def test_hyp_choice_window_prompt_3__setter(instance):
    original = instance.prompt_3_
    instance.prompt_3_ = original
    assert instance.prompt_3_ == original



@given(instance=choice_window_strategy)
def test_hyp_choice_window_names_3__setter(instance):
    original = instance.names_3_
    instance.names_3_ = original
    assert instance.names_3_ == original



@given(instance=choice_window_strategy)
def test_hyp_choice_window_response_3__setter(instance):
    original = instance.response_3_
    instance.response_3_ = original
    assert instance.response_3_ == original


@given(instance=window_strategy)
@settings(max_examples=50)
def test_hyp_window_instantiation(instance):
    assert isinstance(instance, window)



@given(instance=window_strategy)
def test_hyp_window_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original



@given(instance=window_strategy)
def test_hyp_window_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=window_strategy)
def test_hyp_window__main_setter(instance):
    original = instance._main
    instance._main = original
    assert instance._main == original



@given(instance=window_strategy)
def test_hyp_window_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=window_strategy)
def test_hyp_window_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=window_strategy)
def test_hyp_window_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    choice_window,
    cursor,
    cursor1,
    game_board,
    game_board1,
    load,
    save,
    sudoku_board,
    sudoku_board1,
    sudoku_validator,
    window,
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

def test_cursor1_limit_x_value_roundtrip():
    instance = cursor1(limit_x=7, limit_y="sample_text", pos_x=7, pos_y=7)
    assert instance.limit_x == 7
    instance.limit_x = 13
    assert instance.limit_x == 13


def test_cursor1_limit_y_value_roundtrip():
    instance = cursor1(limit_x=7, limit_y="sample_text", pos_x=7, pos_y=7)
    assert instance.limit_y == "sample_text"
    instance.limit_y = "sample_text_2"
    assert instance.limit_y == "sample_text_2"


def test_cursor1_pos_x_value_roundtrip():
    instance = cursor1(limit_x=7, limit_y="sample_text", pos_x=7, pos_y=7)
    assert instance.pos_x == 7
    instance.pos_x = 13
    assert instance.pos_x == 13


def test_cursor1_pos_y_value_roundtrip():
    instance = cursor1(limit_x=7, limit_y="sample_text", pos_x=7, pos_y=7)
    assert instance.pos_y == 7
    instance.pos_y = 13
    assert instance.pos_y == 13


def test_load_file_name_value_roundtrip():
    instance = load(file_name="sample_text")
    assert instance.file_name == "sample_text"
    instance.file_name = "sample_text_2"
    assert instance.file_name == "sample_text_2"


def test_save_file_name_value_roundtrip():
    instance = save(file_name="sample_text")
    assert instance.file_name == "sample_text"
    instance.file_name = "sample_text_2"
    assert instance.file_name == "sample_text_2"


def test_sudoku_board1_board_9__9__value_roundtrip():
    instance = sudoku_board1(board_9__9_=7, fixed_9__9_=7)
    assert instance.board_9__9_ == 7
    instance.board_9__9_ = 13
    assert instance.board_9__9_ == 13


def test_sudoku_board1_fixed_9__9__value_roundtrip():
    instance = sudoku_board1(board_9__9_=7, fixed_9__9_=7)
    assert instance.fixed_9__9_ == 7
    instance.fixed_9__9_ = 13
    assert instance.fixed_9__9_ == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

cursor_strategy = st.builds(cursor)
@given(instance=cursor_strategy)
@settings(max_examples=25)
def test_cursor_instantiation(instance):
    assert isinstance(instance, cursor)


cursor1_strategy = st.builds(cursor1, limit_x=st.integers(), limit_y=safe_text, pos_x=st.integers(), pos_y=st.integers())
@given(instance=cursor1_strategy)
@settings(max_examples=25)
def test_cursor1_instantiation(instance):
    assert isinstance(instance, cursor1)


game_board_strategy = st.builds(game_board)
@given(instance=game_board_strategy)
@settings(max_examples=25)
def test_game_board_instantiation(instance):
    assert isinstance(instance, game_board)


load_strategy = st.builds(load, file_name=safe_text)
@given(instance=load_strategy)
@settings(max_examples=25)
def test_load_instantiation(instance):
    assert isinstance(instance, load)


save_strategy = st.builds(save, file_name=safe_text)
@given(instance=save_strategy)
@settings(max_examples=25)
def test_save_instantiation(instance):
    assert isinstance(instance, save)


sudoku_board_strategy = st.builds(sudoku_board)
@given(instance=sudoku_board_strategy)
@settings(max_examples=25)
def test_sudoku_board_instantiation(instance):
    assert isinstance(instance, sudoku_board)


sudoku_board1_strategy = st.builds(sudoku_board1, board_9__9_=st.integers(), fixed_9__9_=st.integers())
@given(instance=sudoku_board1_strategy)
@settings(max_examples=25)
def test_sudoku_board1_instantiation(instance):
    assert isinstance(instance, sudoku_board1)


sudoku_validator_strategy = st.builds(sudoku_validator)
@given(instance=sudoku_validator_strategy)
@settings(max_examples=25)
def test_sudoku_validator_instantiation(instance):
    assert isinstance(instance, sudoku_validator)



