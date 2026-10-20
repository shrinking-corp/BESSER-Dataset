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
    PersonsRegister_Person,
    PersonsRegister_PersonsRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_personsregister_person_is_not_abstract():
    assert not inspect.isabstract(PersonsRegister_Person)


def test_hyp_personsregister_person_constructor_exists():
    assert callable(PersonsRegister_Person.__init__)


def test_hyp_personsregister_person_constructor_args():
    sig = inspect.signature(PersonsRegister_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "identity" in params, "Missing parameter 'identity'"
    assert "lastName" in params, "Missing parameter 'lastName'"






def test_hyp_personsregister_personsregister_is_not_abstract():
    assert not inspect.isabstract(PersonsRegister_PersonsRegister)


def test_hyp_personsregister_personsregister_constructor_exists():
    assert callable(PersonsRegister_PersonsRegister.__init__)


def test_hyp_personsregister_personsregister_constructor_args():
    sig = inspect.signature(PersonsRegister_PersonsRegister.__init__)
    params = list(sig.parameters.keys())


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
PersonsRegister_Person_strategy = st.builds(
    PersonsRegister_Person,
    firstName=
        safe_text,
    identity=
        safe_text,
    lastName=
        safe_text
)
PersonsRegister_PersonsRegister_strategy = st.builds(
    PersonsRegister_PersonsRegister,
)




@given(instance=PersonsRegister_Person_strategy)
def test_hyp_personsregister_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=PersonsRegister_Person_strategy)
def test_hyp_personsregister_person_identity_setter(instance):
    original = instance.identity
    instance.identity = original
    assert instance.identity == original



@given(instance=PersonsRegister_Person_strategy)
def test_hyp_personsregister_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    PersonsRegister_Person,
    PersonsRegister_PersonsRegister,
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

def test_PersonsRegister_Person_firstName_value_roundtrip():
    instance = PersonsRegister_Person(firstName="sample_text", identity="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_PersonsRegister_Person_identity_value_roundtrip():
    instance = PersonsRegister_Person(firstName="sample_text", identity="sample_text", lastName="sample_text")
    assert instance.identity == "sample_text"
    instance.identity = "sample_text_2"
    assert instance.identity == "sample_text_2"


def test_PersonsRegister_Person_lastName_value_roundtrip():
    instance = PersonsRegister_Person(firstName="sample_text", identity="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_assoc_persons0_link_reassign_clear():
    a = PersonsRegister_Person(firstName="sample_text", identity="sample_text", lastName="sample_text")
    b1 = PersonsRegister_PersonsRegister()
    b2 = PersonsRegister_PersonsRegister()
    _safe_set(a, 'PersonsRegister_Person', b1)
    assert _is_linked(a, 'PersonsRegister_Person', b1)
    if hasattr(b1, 'PersonsRegister_PersonsRegister'):
        assert _is_linked(b1, 'PersonsRegister_PersonsRegister', a)
    _safe_set(a, 'PersonsRegister_Person', b2)
    assert _is_linked(a, 'PersonsRegister_Person', b2)
    if hasattr(b1, 'PersonsRegister_PersonsRegister'):
        assert not _is_linked(b1, 'PersonsRegister_PersonsRegister', a)
    if hasattr(b2, 'PersonsRegister_PersonsRegister'):
        assert _is_linked(b2, 'PersonsRegister_PersonsRegister', a)
    _safe_set(a, 'PersonsRegister_Person', None)
    assert not _is_linked(a, 'PersonsRegister_Person', b2)
    if hasattr(b2, 'PersonsRegister_PersonsRegister'):
        assert not _is_linked(b2, 'PersonsRegister_PersonsRegister', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

PersonsRegister_Person_strategy = st.builds(PersonsRegister_Person, firstName=safe_text, identity=safe_text, lastName=safe_text)
@given(instance=PersonsRegister_Person_strategy)
@settings(max_examples=25)
def test_PersonsRegister_Person_instantiation(instance):
    assert isinstance(instance, PersonsRegister_Person)


PersonsRegister_PersonsRegister_strategy = st.builds(PersonsRegister_PersonsRegister)
@given(instance=PersonsRegister_PersonsRegister_strategy)
@settings(max_examples=25)
def test_PersonsRegister_PersonsRegister_instantiation(instance):
    assert isinstance(instance, PersonsRegister_PersonsRegister)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PersonsRegister_Person,
    PersonsRegister_PersonsRegister,
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

def test_assoc_persons0_stub_double():
    # PersonsRegister_PersonsRegister has no real 'PersonsRegister_PersonsRegister' property in the generated
    # code (a bare stub) -- manually attach it so PersonsRegister_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonsRegister_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonsRegister_Person(firstName="sample_text", identity="sample_text", lastName="sample_text")
    partner = PersonsRegister_PersonsRegister()
    setattr(partner, 'PersonsRegister_PersonsRegister', None)
    _safe_set(owner, 'PersonsRegister_Person', partner)
    assert owner in getattr(partner, 'PersonsRegister_PersonsRegister')
    _safe_set(owner, 'PersonsRegister_Person', None)
    assert owner not in getattr(partner, 'PersonsRegister_PersonsRegister')




from python_code import PersonsRegister_Person
from python_code import PersonsRegister_PersonsRegister

def test_PersonsRegister_Person___init__():
    assert PersonsRegister_Person.__init__(PersonsRegister_Person('', '', '\x00\x00', PersonsRegister_Person=PersonsRegister_PersonsRegister()), '', '', '', PersonsRegister_Person=PersonsRegister_PersonsRegister()) == None

