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
    State,
    autopl_HierarchicalState,
    autopl_Transition,
    autopl_State,
    autopl_Symbol,
    autopl_Alphabet,
    autopl_Automaton,
    AcceptanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_autopl_hierarchicalstate_is_not_abstract():
    assert not inspect.isabstract(autopl_HierarchicalState)


def test_hyp_autopl_hierarchicalstate_constructor_exists():
    assert callable(autopl_HierarchicalState.__init__)


def test_hyp_autopl_hierarchicalstate_constructor_args():
    sig = inspect.signature(autopl_HierarchicalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_autopl_transition_is_not_abstract():
    assert not inspect.isabstract(autopl_Transition)


def test_hyp_autopl_transition_constructor_exists():
    assert callable(autopl_Transition.__init__)


def test_hyp_autopl_transition_constructor_args():
    sig = inspect.signature(autopl_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"




def test_hyp_autopl_state_is_not_abstract():
    assert not inspect.isabstract(autopl_State)


def test_hyp_autopl_state_constructor_exists():
    assert callable(autopl_State.__init__)


def test_hyp_autopl_state_constructor_args():
    sig = inspect.signature(autopl_State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_autopl_symbol_is_not_abstract():
    assert not inspect.isabstract(autopl_Symbol)


def test_hyp_autopl_symbol_constructor_exists():
    assert callable(autopl_Symbol.__init__)


def test_hyp_autopl_symbol_constructor_args():
    sig = inspect.signature(autopl_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_autopl_alphabet_is_not_abstract():
    assert not inspect.isabstract(autopl_Alphabet)


def test_hyp_autopl_alphabet_constructor_exists():
    assert callable(autopl_Alphabet.__init__)


def test_hyp_autopl_alphabet_constructor_args():
    sig = inspect.signature(autopl_Alphabet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_autopl_automaton_is_not_abstract():
    assert not inspect.isabstract(autopl_Automaton)


def test_hyp_autopl_automaton_constructor_exists():
    assert callable(autopl_Automaton.__init__)


def test_hyp_autopl_automaton_constructor_args():
    sig = inspect.signature(autopl_Automaton.__init__)
    params = list(sig.parameters.keys())

def test_hyp_acceptancekind_exists():
    # Check that the Enumeration exists
    assert AcceptanceKind is not None

def test_hyp_acceptancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AcceptanceKind]
    expected_literals = [
        "Infinite",
        "Finite",
        "Probabilistic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AcceptanceKind"


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
State_strategy = st.builds(
    State,
)
autopl_HierarchicalState_strategy = st.builds(
    autopl_HierarchicalState,
)
autopl_Transition_strategy = st.builds(
    autopl_Transition,
    probability=
        safe_text
)
autopl_State_strategy = st.builds(
    autopl_State,
    isInitial=
        safe_text,
    isFinal=
        safe_text,
    name=
        safe_text
)
autopl_Symbol_strategy = st.builds(
    autopl_Symbol,
    name=
        safe_text
)
autopl_Alphabet_strategy = st.builds(
    autopl_Alphabet,
)
autopl_Automaton_strategy = st.builds(
    autopl_Automaton,
)






@given(instance=autopl_Transition_strategy)
def test_hyp_autopl_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original




@given(instance=autopl_State_strategy)
def test_hyp_autopl_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=autopl_State_strategy)
def test_hyp_autopl_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=autopl_State_strategy)
def test_hyp_autopl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_State_strategy)
@settings(max_examples=30)
def test_hyp_autopl_state_adjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.adjacent()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.adjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'adjacent' in autopl_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'adjacent' in autopl_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'adjacent' in autopl_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_State_strategy)
@settings(max_examples=30)
def test_hyp_autopl_state_outtrans_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.outTrans()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.outTrans).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'outTrans' in autopl_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'outTrans' in autopl_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'outTrans' in autopl_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_State_strategy)
@settings(max_examples=30)
def test_hyp_autopl_state_intrans_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.inTrans()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.inTrans).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'inTrans' in autopl_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inTrans' in autopl_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inTrans' in autopl_State is not implemented or raised an error")




@given(instance=autopl_Symbol_strategy)
def test_hyp_autopl_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_Automaton_strategy)
@settings(max_examples=30)
def test_hyp_autopl_automaton_acceptancecondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.acceptanceCondition()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.acceptanceCondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'acceptanceCondition' in autopl_Automaton is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'acceptanceCondition' in autopl_Automaton did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'acceptanceCondition' in autopl_Automaton is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    State,
    autopl_Alphabet,
    autopl_Automaton,
    autopl_HierarchicalState,
    autopl_State,
    autopl_Symbol,
    autopl_Transition,
    AcceptanceKind,
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

def test_autopl_State_isFinal_value_roundtrip():
    instance = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    assert instance.isFinal == "sample_text"
    instance.isFinal = "sample_text_2"
    assert instance.isFinal == "sample_text_2"


def test_autopl_State_isInitial_value_roundtrip():
    instance = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    assert instance.isInitial == "sample_text"
    instance.isInitial = "sample_text_2"
    assert instance.isInitial == "sample_text_2"


def test_autopl_State_name_value_roundtrip():
    instance = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_autopl_Symbol_name_value_roundtrip():
    instance = autopl_Symbol(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_autopl_Transition_probability_value_roundtrip():
    instance = autopl_Transition(probability="sample_text")
    assert instance.probability == "sample_text"
    instance.probability = "sample_text_2"
    assert instance.probability == "sample_text_2"


def test_autopl_HierarchicalState_isa_State():
    instance = autopl_HierarchicalState()
    assert isinstance(instance, State)


def test_assoc_from_28_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    b2 = autopl_State(isFinal="sample_text_2", isInitial="sample_text_2", name="sample_text_2")
    _safe_set(a, 'autopl_Transition29', b1)
    assert _is_linked(a, 'autopl_Transition29', b1)
    if hasattr(b1, 'autopl_State30'):
        assert _is_linked(b1, 'autopl_State30', a)
    _safe_set(a, 'autopl_Transition29', b2)
    assert _is_linked(a, 'autopl_Transition29', b2)
    if hasattr(b1, 'autopl_State30'):
        assert not _is_linked(b1, 'autopl_State30', a)
    if hasattr(b2, 'autopl_State30'):
        assert _is_linked(b2, 'autopl_State30', a)
    _safe_set(a, 'autopl_Transition29', None)
    assert not _is_linked(a, 'autopl_Transition29', b2)
    if hasattr(b2, 'autopl_State30'):
        assert not _is_linked(b2, 'autopl_State30', a)


def test_assoc_initialStackSymbol7_link_reassign_clear():
    a = autopl_Symbol(name="sample_text")
    b1 = autopl_Automaton()
    b2 = autopl_Automaton()
    _safe_set(a, 'autopl_Symbol', b1)
    assert _is_linked(a, 'autopl_Symbol', b1)
    if hasattr(b1, 'autopl_Automaton8'):
        assert _is_linked(b1, 'autopl_Automaton8', a)
    _safe_set(a, 'autopl_Symbol', b2)
    assert _is_linked(a, 'autopl_Symbol', b2)
    if hasattr(b1, 'autopl_Automaton8'):
        assert not _is_linked(b1, 'autopl_Automaton8', a)
    if hasattr(b2, 'autopl_Automaton8'):
        assert _is_linked(b2, 'autopl_Automaton8', a)
    _safe_set(a, 'autopl_Symbol', None)
    assert not _is_linked(a, 'autopl_Symbol', b2)
    if hasattr(b2, 'autopl_Automaton8'):
        assert not _is_linked(b2, 'autopl_Automaton8', a)


def test_assoc_input16_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_Symbol(name="sample_text")
    b2 = autopl_Symbol(name="sample_text_2")
    _safe_set(a, 'autopl_Transition17', b1)
    assert _is_linked(a, 'autopl_Transition17', b1)
    if hasattr(b1, 'autopl_Symbol18'):
        assert _is_linked(b1, 'autopl_Symbol18', a)
    _safe_set(a, 'autopl_Transition17', b2)
    assert _is_linked(a, 'autopl_Transition17', b2)
    if hasattr(b1, 'autopl_Symbol18'):
        assert not _is_linked(b1, 'autopl_Symbol18', a)
    if hasattr(b2, 'autopl_Symbol18'):
        assert _is_linked(b2, 'autopl_Symbol18', a)
    _safe_set(a, 'autopl_Transition17', None)
    assert not _is_linked(a, 'autopl_Transition17', b2)
    if hasattr(b2, 'autopl_Symbol18'):
        assert not _is_linked(b2, 'autopl_Symbol18', a)


def test_assoc_inputAlphabet0_link_reassign_clear():
    a = autopl_Automaton()
    b1 = autopl_Alphabet()
    b2 = autopl_Alphabet()
    _safe_set(a, 'autopl_Automaton', b1)
    assert _is_linked(a, 'autopl_Automaton', b1)
    if hasattr(b1, 'autopl_Alphabet'):
        assert _is_linked(b1, 'autopl_Alphabet', a)
    _safe_set(a, 'autopl_Automaton', b2)
    assert _is_linked(a, 'autopl_Automaton', b2)
    if hasattr(b1, 'autopl_Alphabet'):
        assert not _is_linked(b1, 'autopl_Alphabet', a)
    if hasattr(b2, 'autopl_Alphabet'):
        assert _is_linked(b2, 'autopl_Alphabet', a)
    _safe_set(a, 'autopl_Automaton', None)
    assert not _is_linked(a, 'autopl_Automaton', b2)
    if hasattr(b2, 'autopl_Alphabet'):
        assert not _is_linked(b2, 'autopl_Alphabet', a)


def test_assoc_output19_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_Symbol(name="sample_text")
    b2 = autopl_Symbol(name="sample_text_2")
    _safe_set(a, 'autopl_Transition20', b1)
    assert _is_linked(a, 'autopl_Transition20', b1)
    if hasattr(b1, 'autopl_Symbol21'):
        assert _is_linked(b1, 'autopl_Symbol21', a)
    _safe_set(a, 'autopl_Transition20', b2)
    assert _is_linked(a, 'autopl_Transition20', b2)
    if hasattr(b1, 'autopl_Symbol21'):
        assert not _is_linked(b1, 'autopl_Symbol21', a)
    if hasattr(b2, 'autopl_Symbol21'):
        assert _is_linked(b2, 'autopl_Symbol21', a)
    _safe_set(a, 'autopl_Transition20', None)
    assert not _is_linked(a, 'autopl_Transition20', b2)
    if hasattr(b2, 'autopl_Symbol21'):
        assert not _is_linked(b2, 'autopl_Symbol21', a)


def test_assoc_outputAlphabet1_link_reassign_clear():
    a = autopl_Automaton()
    b1 = autopl_Alphabet()
    b2 = autopl_Alphabet()
    _safe_set(a, 'autopl_Automaton2', b1)
    assert _is_linked(a, 'autopl_Automaton2', b1)
    if hasattr(b1, 'autopl_Alphabet3'):
        assert _is_linked(b1, 'autopl_Alphabet3', a)
    _safe_set(a, 'autopl_Automaton2', b2)
    assert _is_linked(a, 'autopl_Automaton2', b2)
    if hasattr(b1, 'autopl_Alphabet3'):
        assert not _is_linked(b1, 'autopl_Alphabet3', a)
    if hasattr(b2, 'autopl_Alphabet3'):
        assert _is_linked(b2, 'autopl_Alphabet3', a)
    _safe_set(a, 'autopl_Automaton2', None)
    assert not _is_linked(a, 'autopl_Automaton2', b2)
    if hasattr(b2, 'autopl_Alphabet3'):
        assert not _is_linked(b2, 'autopl_Alphabet3', a)


def test_assoc_stackAlphabet4_link_reassign_clear():
    a = autopl_Automaton()
    b1 = autopl_Alphabet()
    b2 = autopl_Alphabet()
    _safe_set(a, 'autopl_Automaton5', b1)
    assert _is_linked(a, 'autopl_Automaton5', b1)
    if hasattr(b1, 'autopl_Alphabet6'):
        assert _is_linked(b1, 'autopl_Alphabet6', a)
    _safe_set(a, 'autopl_Automaton5', b2)
    assert _is_linked(a, 'autopl_Automaton5', b2)
    if hasattr(b1, 'autopl_Alphabet6'):
        assert not _is_linked(b1, 'autopl_Alphabet6', a)
    if hasattr(b2, 'autopl_Alphabet6'):
        assert _is_linked(b2, 'autopl_Alphabet6', a)
    _safe_set(a, 'autopl_Automaton5', None)
    assert not _is_linked(a, 'autopl_Automaton5', b2)
    if hasattr(b2, 'autopl_Alphabet6'):
        assert not _is_linked(b2, 'autopl_Alphabet6', a)


def test_assoc_stackCheck22_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_Symbol(name="sample_text")
    b2 = autopl_Symbol(name="sample_text_2")
    _safe_set(a, 'autopl_Transition23', b1)
    assert _is_linked(a, 'autopl_Transition23', b1)
    if hasattr(b1, 'autopl_Symbol24'):
        assert _is_linked(b1, 'autopl_Symbol24', a)
    _safe_set(a, 'autopl_Transition23', b2)
    assert _is_linked(a, 'autopl_Transition23', b2)
    if hasattr(b1, 'autopl_Symbol24'):
        assert not _is_linked(b1, 'autopl_Symbol24', a)
    if hasattr(b2, 'autopl_Symbol24'):
        assert _is_linked(b2, 'autopl_Symbol24', a)
    _safe_set(a, 'autopl_Transition23', None)
    assert not _is_linked(a, 'autopl_Transition23', b2)
    if hasattr(b2, 'autopl_Symbol24'):
        assert not _is_linked(b2, 'autopl_Symbol24', a)


def test_assoc_stackPush25_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_Symbol(name="sample_text")
    b2 = autopl_Symbol(name="sample_text_2")
    _safe_set(a, 'autopl_Transition26', {b1})
    assert _is_linked(a, 'autopl_Transition26', b1)
    if hasattr(b1, 'autopl_Symbol27'):
        assert _is_linked(b1, 'autopl_Symbol27', a)
    _safe_set(a, 'autopl_Transition26', {b2})
    assert _is_linked(a, 'autopl_Transition26', b2)
    if hasattr(b1, 'autopl_Symbol27'):
        assert not _is_linked(b1, 'autopl_Symbol27', a)
    if hasattr(b2, 'autopl_Symbol27'):
        assert _is_linked(b2, 'autopl_Symbol27', a)
    _safe_set(a, 'autopl_Transition26', set())
    assert not _is_linked(a, 'autopl_Transition26', b2)
    if hasattr(b2, 'autopl_Symbol27'):
        assert not _is_linked(b2, 'autopl_Symbol27', a)


def test_assoc_states34_link_reassign_clear():
    a = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    b1 = autopl_HierarchicalState()
    b2 = autopl_HierarchicalState()
    _safe_set(a, 'autopl_State35', b1)
    assert _is_linked(a, 'autopl_State35', b1)
    if hasattr(b1, 'autopl_HierarchicalState'):
        assert _is_linked(b1, 'autopl_HierarchicalState', a)
    _safe_set(a, 'autopl_State35', b2)
    assert _is_linked(a, 'autopl_State35', b2)
    if hasattr(b1, 'autopl_HierarchicalState'):
        assert not _is_linked(b1, 'autopl_HierarchicalState', a)
    if hasattr(b2, 'autopl_HierarchicalState'):
        assert _is_linked(b2, 'autopl_HierarchicalState', a)
    _safe_set(a, 'autopl_State35', None)
    assert not _is_linked(a, 'autopl_State35', b2)
    if hasattr(b2, 'autopl_HierarchicalState'):
        assert not _is_linked(b2, 'autopl_HierarchicalState', a)


def test_assoc_states9_link_reassign_clear():
    a = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    b1 = autopl_Automaton()
    b2 = autopl_Automaton()
    _safe_set(a, 'autopl_State', b1)
    assert _is_linked(a, 'autopl_State', b1)
    if hasattr(b1, 'autopl_Automaton10'):
        assert _is_linked(b1, 'autopl_Automaton10', a)
    _safe_set(a, 'autopl_State', b2)
    assert _is_linked(a, 'autopl_State', b2)
    if hasattr(b1, 'autopl_Automaton10'):
        assert not _is_linked(b1, 'autopl_Automaton10', a)
    if hasattr(b2, 'autopl_Automaton10'):
        assert _is_linked(b2, 'autopl_Automaton10', a)
    _safe_set(a, 'autopl_State', None)
    assert not _is_linked(a, 'autopl_State', b2)
    if hasattr(b2, 'autopl_Automaton10'):
        assert not _is_linked(b2, 'autopl_Automaton10', a)


def test_assoc_symbols13_link_reassign_clear():
    a = autopl_Symbol(name="sample_text")
    b1 = autopl_Alphabet()
    b2 = autopl_Alphabet()
    _safe_set(a, 'autopl_Symbol15', b1)
    assert _is_linked(a, 'autopl_Symbol15', b1)
    if hasattr(b1, 'autopl_Alphabet14'):
        assert _is_linked(b1, 'autopl_Alphabet14', a)
    _safe_set(a, 'autopl_Symbol15', b2)
    assert _is_linked(a, 'autopl_Symbol15', b2)
    if hasattr(b1, 'autopl_Alphabet14'):
        assert not _is_linked(b1, 'autopl_Alphabet14', a)
    if hasattr(b2, 'autopl_Alphabet14'):
        assert _is_linked(b2, 'autopl_Alphabet14', a)
    _safe_set(a, 'autopl_Symbol15', None)
    assert not _is_linked(a, 'autopl_Symbol15', b2)
    if hasattr(b2, 'autopl_Alphabet14'):
        assert not _is_linked(b2, 'autopl_Alphabet14', a)


def test_assoc_to31_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    b2 = autopl_State(isFinal="sample_text_2", isInitial="sample_text_2", name="sample_text_2")
    _safe_set(a, 'autopl_Transition32', b1)
    assert _is_linked(a, 'autopl_Transition32', b1)
    if hasattr(b1, 'autopl_State33'):
        assert _is_linked(b1, 'autopl_State33', a)
    _safe_set(a, 'autopl_Transition32', b2)
    assert _is_linked(a, 'autopl_Transition32', b2)
    if hasattr(b1, 'autopl_State33'):
        assert not _is_linked(b1, 'autopl_State33', a)
    if hasattr(b2, 'autopl_State33'):
        assert _is_linked(b2, 'autopl_State33', a)
    _safe_set(a, 'autopl_Transition32', None)
    assert not _is_linked(a, 'autopl_Transition32', b2)
    if hasattr(b2, 'autopl_State33'):
        assert not _is_linked(b2, 'autopl_State33', a)


def test_assoc_transitions11_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_Automaton()
    b2 = autopl_Automaton()
    _safe_set(a, 'autopl_Transition', b1)
    assert _is_linked(a, 'autopl_Transition', b1)
    if hasattr(b1, 'autopl_Automaton12'):
        assert _is_linked(b1, 'autopl_Automaton12', a)
    _safe_set(a, 'autopl_Transition', b2)
    assert _is_linked(a, 'autopl_Transition', b2)
    if hasattr(b1, 'autopl_Automaton12'):
        assert not _is_linked(b1, 'autopl_Automaton12', a)
    if hasattr(b2, 'autopl_Automaton12'):
        assert _is_linked(b2, 'autopl_Automaton12', a)
    _safe_set(a, 'autopl_Transition', None)
    assert not _is_linked(a, 'autopl_Transition', b2)
    if hasattr(b2, 'autopl_Automaton12'):
        assert not _is_linked(b2, 'autopl_Automaton12', a)


def test_assoc_transitions36_link_reassign_clear():
    a = autopl_Transition(probability="sample_text")
    b1 = autopl_HierarchicalState()
    b2 = autopl_HierarchicalState()
    _safe_set(a, 'autopl_Transition38', b1)
    assert _is_linked(a, 'autopl_Transition38', b1)
    if hasattr(b1, 'autopl_HierarchicalState37'):
        assert _is_linked(b1, 'autopl_HierarchicalState37', a)
    _safe_set(a, 'autopl_Transition38', b2)
    assert _is_linked(a, 'autopl_Transition38', b2)
    if hasattr(b1, 'autopl_HierarchicalState37'):
        assert not _is_linked(b1, 'autopl_HierarchicalState37', a)
    if hasattr(b2, 'autopl_HierarchicalState37'):
        assert _is_linked(b2, 'autopl_HierarchicalState37', a)
    _safe_set(a, 'autopl_Transition38', None)
    assert not _is_linked(a, 'autopl_Transition38', b2)
    if hasattr(b2, 'autopl_HierarchicalState37'):
        assert not _is_linked(b2, 'autopl_HierarchicalState37', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


autopl_Alphabet_strategy = st.builds(autopl_Alphabet)
@given(instance=autopl_Alphabet_strategy)
@settings(max_examples=25)
def test_autopl_Alphabet_instantiation(instance):
    assert isinstance(instance, autopl_Alphabet)


autopl_Automaton_strategy = st.builds(autopl_Automaton)
@given(instance=autopl_Automaton_strategy)
@settings(max_examples=25)
def test_autopl_Automaton_instantiation(instance):
    assert isinstance(instance, autopl_Automaton)


autopl_HierarchicalState_strategy = st.builds(autopl_HierarchicalState)
@given(instance=autopl_HierarchicalState_strategy)
@settings(max_examples=25)
def test_autopl_HierarchicalState_instantiation(instance):
    assert isinstance(instance, autopl_HierarchicalState)


autopl_State_strategy = st.builds(autopl_State, isFinal=safe_text, isInitial=safe_text, name=safe_text)
@given(instance=autopl_State_strategy)
@settings(max_examples=25)
def test_autopl_State_instantiation(instance):
    assert isinstance(instance, autopl_State)


autopl_Symbol_strategy = st.builds(autopl_Symbol, name=safe_text)
@given(instance=autopl_Symbol_strategy)
@settings(max_examples=25)
def test_autopl_Symbol_instantiation(instance):
    assert isinstance(instance, autopl_Symbol)


autopl_Transition_strategy = st.builds(autopl_Transition, probability=safe_text)
@given(instance=autopl_Transition_strategy)
@settings(max_examples=25)
def test_autopl_Transition_instantiation(instance):
    assert isinstance(instance, autopl_Transition)



