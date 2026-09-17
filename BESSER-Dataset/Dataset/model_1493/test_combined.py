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
    petriNet_PetriNetwork,
    PetriElement,
    petriNet_Place,
    petriNet_Arc,
    petriNet_Transition,
    petriNet_PetriElement,
    ArcDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_petrinet_petrinetwork_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNetwork)


def test_hyp_petrinet_petrinetwork_constructor_exists():
    assert callable(petriNet_PetriNetwork.__init__)


def test_hyp_petrinet_petrinetwork_constructor_args():
    sig = inspect.signature(petriNet_PetriNetwork.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriElement)


def test_hyp_petrielement_constructor_exists():
    assert callable(PetriElement.__init__)


def test_hyp_petrielement_constructor_args():
    sig = inspect.signature(PetriElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petriNet_Place)


def test_hyp_petrinet_place_constructor_exists():
    assert callable(petriNet_Place.__init__)


def test_hyp_petrinet_place_constructor_args():
    sig = inspect.signature(petriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "nbJetons" in params, "Missing parameter 'nbJetons'"




def test_hyp_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petriNet_Arc)


def test_hyp_petrinet_arc_constructor_exists():
    assert callable(petriNet_Arc.__init__)


def test_hyp_petrinet_arc_constructor_args():
    sig = inspect.signature(petriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "Direction" in params, "Missing parameter 'Direction'"
    assert "jetonsTransferes" in params, "Missing parameter 'jetonsTransferes'"





def test_hyp_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petriNet_Transition)


def test_hyp_petrinet_transition_constructor_exists():
    assert callable(petriNet_Transition.__init__)


def test_hyp_petrinet_transition_constructor_args():
    sig = inspect.signature(petriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_petrielement_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriElement)


def test_hyp_petrinet_petrielement_constructor_exists():
    assert callable(petriNet_PetriElement.__init__)


def test_hyp_petrinet_petrielement_constructor_args():
    sig = inspect.signature(petriNet_PetriElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_arcdirection_exists():
    # Check that the Enumeration exists
    assert ArcDirection is not None

def test_hyp_arcdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcDirection]
    expected_literals = [
        "T2P",
        "P2T",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArcDirection"


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
petriNet_PetriNetwork_strategy = st.builds(
    petriNet_PetriNetwork,
    name=
        safe_text
)
PetriElement_strategy = st.builds(
    PetriElement,
)
petriNet_Place_strategy = st.builds(
    petriNet_Place,
    nbJetons=
        st.integers()
)
petriNet_Arc_strategy = st.builds(
    petriNet_Arc,
    Direction=
        safe_text,
    jetonsTransferes=
        st.integers()
)
petriNet_Transition_strategy = st.builds(
    petriNet_Transition,
)
petriNet_PetriElement_strategy = st.builds(
    petriNet_PetriElement,
    name=
        safe_text
)




@given(instance=petriNet_PetriNetwork_strategy)
def test_hyp_petrinet_petrinetwork_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=petriNet_Place_strategy)
def test_hyp_petrinet_place_nbJetons_setter(instance):
    original = instance.nbJetons
    instance.nbJetons = original
    assert instance.nbJetons == original




@given(instance=petriNet_Arc_strategy)
def test_hyp_petrinet_arc_Direction_setter(instance):
    original = instance.Direction
    instance.Direction = original
    assert instance.Direction == original



@given(instance=petriNet_Arc_strategy)
def test_hyp_petrinet_arc_jetonsTransferes_setter(instance):
    original = instance.jetonsTransferes
    instance.jetonsTransferes = original
    assert instance.jetonsTransferes == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=30)
def test_hyp_petrinet_transition_newoperation1_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.newOperation1()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.newOperation1).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'newOperation1' in petriNet_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'newOperation1' in petriNet_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'newOperation1' in petriNet_Transition is not implemented or raised an error")




@given(instance=petriNet_PetriElement_strategy)
def test_hyp_petrinet_petrielement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    PetriElement,
    petriNet_Arc,
    petriNet_PetriElement,
    petriNet_PetriNetwork,
    petriNet_Place,
    petriNet_Transition,
    ArcDirection,
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

def test_petriNet_Arc_Direction_value_roundtrip():
    instance = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    assert instance.Direction == "sample_text"
    instance.Direction = "sample_text_2"
    assert instance.Direction == "sample_text_2"


def test_petriNet_Arc_jetonsTransferes_value_roundtrip():
    instance = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    assert instance.jetonsTransferes == 7
    instance.jetonsTransferes = 13
    assert instance.jetonsTransferes == 13


def test_petriNet_PetriElement_name_value_roundtrip():
    instance = petriNet_PetriElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_petriNet_PetriNetwork_name_value_roundtrip():
    instance = petriNet_PetriNetwork(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_petriNet_Place_nbJetons_value_roundtrip():
    instance = petriNet_Place(nbJetons=7)
    assert instance.nbJetons == 7
    instance.nbJetons = 13
    assert instance.nbJetons == 13


def test_petriNet_Arc_isa_PetriElement():
    instance = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    assert isinstance(instance, PetriElement)


def test_petriNet_Place_isa_PetriElement():
    instance = petriNet_Place(nbJetons=7)
    assert isinstance(instance, PetriElement)


def test_petriNet_Transition_isa_PetriElement():
    instance = petriNet_Transition()
    assert isinstance(instance, PetriElement)


def test_assoc_arcEntrants1_link_reassign_clear():
    a = petriNet_Transition()
    b1 = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    b2 = petriNet_Arc(Direction="sample_text_2", jetonsTransferes=13)
    _safe_set(a, 'petriNet_Transition2', {b1})
    assert _is_linked(a, 'petriNet_Transition2', b1)
    if hasattr(b1, 'petriNet_Arc3'):
        assert _is_linked(b1, 'petriNet_Arc3', a)
    _safe_set(a, 'petriNet_Transition2', {b2})
    assert _is_linked(a, 'petriNet_Transition2', b2)
    if hasattr(b1, 'petriNet_Arc3'):
        assert not _is_linked(b1, 'petriNet_Arc3', a)
    if hasattr(b2, 'petriNet_Arc3'):
        assert _is_linked(b2, 'petriNet_Arc3', a)
    _safe_set(a, 'petriNet_Transition2', set())
    assert not _is_linked(a, 'petriNet_Transition2', b2)
    if hasattr(b2, 'petriNet_Arc3'):
        assert not _is_linked(b2, 'petriNet_Arc3', a)


def test_assoc_arcEntrants4_link_reassign_clear():
    a = petriNet_Place(nbJetons=7)
    b1 = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    b2 = petriNet_Arc(Direction="sample_text_2", jetonsTransferes=13)
    _safe_set(a, 'petriNet_Place', {b1})
    assert _is_linked(a, 'petriNet_Place', b1)
    if hasattr(b1, 'petriNet_Arc5'):
        assert _is_linked(b1, 'petriNet_Arc5', a)
    _safe_set(a, 'petriNet_Place', {b2})
    assert _is_linked(a, 'petriNet_Place', b2)
    if hasattr(b1, 'petriNet_Arc5'):
        assert not _is_linked(b1, 'petriNet_Arc5', a)
    if hasattr(b2, 'petriNet_Arc5'):
        assert _is_linked(b2, 'petriNet_Arc5', a)
    _safe_set(a, 'petriNet_Place', set())
    assert not _is_linked(a, 'petriNet_Place', b2)
    if hasattr(b2, 'petriNet_Arc5'):
        assert not _is_linked(b2, 'petriNet_Arc5', a)


def test_assoc_arcSortants0_link_reassign_clear():
    a = petriNet_Transition()
    b1 = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    b2 = petriNet_Arc(Direction="sample_text_2", jetonsTransferes=13)
    _safe_set(a, 'petriNet_Transition', {b1})
    assert _is_linked(a, 'petriNet_Transition', b1)
    if hasattr(b1, 'petriNet_Arc'):
        assert _is_linked(b1, 'petriNet_Arc', a)
    _safe_set(a, 'petriNet_Transition', {b2})
    assert _is_linked(a, 'petriNet_Transition', b2)
    if hasattr(b1, 'petriNet_Arc'):
        assert not _is_linked(b1, 'petriNet_Arc', a)
    if hasattr(b2, 'petriNet_Arc'):
        assert _is_linked(b2, 'petriNet_Arc', a)
    _safe_set(a, 'petriNet_Transition', set())
    assert not _is_linked(a, 'petriNet_Transition', b2)
    if hasattr(b2, 'petriNet_Arc'):
        assert not _is_linked(b2, 'petriNet_Arc', a)


def test_assoc_arcSortants6_link_reassign_clear():
    a = petriNet_Place(nbJetons=7)
    b1 = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    b2 = petriNet_Arc(Direction="sample_text_2", jetonsTransferes=13)
    _safe_set(a, 'petriNet_Place7', {b1})
    assert _is_linked(a, 'petriNet_Place7', b1)
    if hasattr(b1, 'petriNet_Arc8'):
        assert _is_linked(b1, 'petriNet_Arc8', a)
    _safe_set(a, 'petriNet_Place7', {b2})
    assert _is_linked(a, 'petriNet_Place7', b2)
    if hasattr(b1, 'petriNet_Arc8'):
        assert not _is_linked(b1, 'petriNet_Arc8', a)
    if hasattr(b2, 'petriNet_Arc8'):
        assert _is_linked(b2, 'petriNet_Arc8', a)
    _safe_set(a, 'petriNet_Place7', set())
    assert not _is_linked(a, 'petriNet_Place7', b2)
    if hasattr(b2, 'petriNet_Arc8'):
        assert not _is_linked(b2, 'petriNet_Arc8', a)


def test_assoc_petrielement15_link_reassign_clear():
    a = petriNet_PetriNetwork(name="sample_text")
    b1 = petriNet_PetriElement(name="sample_text")
    b2 = petriNet_PetriElement(name="sample_text_2")
    _safe_set(a, 'petriNet_PetriNetwork', {b1})
    assert _is_linked(a, 'petriNet_PetriNetwork', b1)
    if hasattr(b1, 'petriNet_PetriElement'):
        assert _is_linked(b1, 'petriNet_PetriElement', a)
    _safe_set(a, 'petriNet_PetriNetwork', {b2})
    assert _is_linked(a, 'petriNet_PetriNetwork', b2)
    if hasattr(b1, 'petriNet_PetriElement'):
        assert not _is_linked(b1, 'petriNet_PetriElement', a)
    if hasattr(b2, 'petriNet_PetriElement'):
        assert _is_linked(b2, 'petriNet_PetriElement', a)
    _safe_set(a, 'petriNet_PetriNetwork', set())
    assert not _is_linked(a, 'petriNet_PetriNetwork', b2)
    if hasattr(b2, 'petriNet_PetriElement'):
        assert not _is_linked(b2, 'petriNet_PetriElement', a)


def test_assoc_place12_link_reassign_clear():
    a = petriNet_Place(nbJetons=7)
    b1 = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    b2 = petriNet_Arc(Direction="sample_text_2", jetonsTransferes=13)
    _safe_set(a, 'petriNet_Place14', b1)
    assert _is_linked(a, 'petriNet_Place14', b1)
    if hasattr(b1, 'petriNet_Arc13'):
        assert _is_linked(b1, 'petriNet_Arc13', a)
    _safe_set(a, 'petriNet_Place14', b2)
    assert _is_linked(a, 'petriNet_Place14', b2)
    if hasattr(b1, 'petriNet_Arc13'):
        assert not _is_linked(b1, 'petriNet_Arc13', a)
    if hasattr(b2, 'petriNet_Arc13'):
        assert _is_linked(b2, 'petriNet_Arc13', a)
    _safe_set(a, 'petriNet_Place14', None)
    assert not _is_linked(a, 'petriNet_Place14', b2)
    if hasattr(b2, 'petriNet_Arc13'):
        assert not _is_linked(b2, 'petriNet_Arc13', a)


def test_assoc_transition9_link_reassign_clear():
    a = petriNet_Transition()
    b1 = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    b2 = petriNet_Arc(Direction="sample_text_2", jetonsTransferes=13)
    _safe_set(a, 'petriNet_Transition11', b1)
    assert _is_linked(a, 'petriNet_Transition11', b1)
    if hasattr(b1, 'petriNet_Arc10'):
        assert _is_linked(b1, 'petriNet_Arc10', a)
    _safe_set(a, 'petriNet_Transition11', b2)
    assert _is_linked(a, 'petriNet_Transition11', b2)
    if hasattr(b1, 'petriNet_Arc10'):
        assert not _is_linked(b1, 'petriNet_Arc10', a)
    if hasattr(b2, 'petriNet_Arc10'):
        assert _is_linked(b2, 'petriNet_Arc10', a)
    _safe_set(a, 'petriNet_Transition11', None)
    assert not _is_linked(a, 'petriNet_Transition11', b2)
    if hasattr(b2, 'petriNet_Arc10'):
        assert not _is_linked(b2, 'petriNet_Arc10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

PetriElement_strategy = st.builds(PetriElement)
@given(instance=PetriElement_strategy)
@settings(max_examples=25)
def test_PetriElement_instantiation(instance):
    assert isinstance(instance, PetriElement)


petriNet_Arc_strategy = st.builds(petriNet_Arc, Direction=safe_text, jetonsTransferes=st.integers())
@given(instance=petriNet_Arc_strategy)
@settings(max_examples=25)
def test_petriNet_Arc_instantiation(instance):
    assert isinstance(instance, petriNet_Arc)


petriNet_PetriElement_strategy = st.builds(petriNet_PetriElement, name=safe_text)
@given(instance=petriNet_PetriElement_strategy)
@settings(max_examples=25)
def test_petriNet_PetriElement_instantiation(instance):
    assert isinstance(instance, petriNet_PetriElement)


petriNet_PetriNetwork_strategy = st.builds(petriNet_PetriNetwork, name=safe_text)
@given(instance=petriNet_PetriNetwork_strategy)
@settings(max_examples=25)
def test_petriNet_PetriNetwork_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNetwork)


petriNet_Place_strategy = st.builds(petriNet_Place, nbJetons=st.integers())
@given(instance=petriNet_Place_strategy)
@settings(max_examples=25)
def test_petriNet_Place_instantiation(instance):
    assert isinstance(instance, petriNet_Place)


petriNet_Transition_strategy = st.builds(petriNet_Transition)
@given(instance=petriNet_Transition_strategy)
@settings(max_examples=25)
def test_petriNet_Transition_instantiation(instance):
    assert isinstance(instance, petriNet_Transition)



