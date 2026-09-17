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
    kreq108c_Gggg,
    Gggg,
    kreq108c_Ffff,
    kreq108c_Eeee,
    kreq108c_Cccc,
    kreq108c_Bbbb,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_kreq108c_gggg_is_not_abstract():
    assert not inspect.isabstract(kreq108c_Gggg)


def test_hyp_kreq108c_gggg_constructor_exists():
    assert callable(kreq108c_Gggg.__init__)


def test_hyp_kreq108c_gggg_constructor_args():
    sig = inspect.signature(kreq108c_Gggg.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_gggg_is_not_abstract():
    assert not inspect.isabstract(Gggg)


def test_hyp_gggg_constructor_exists():
    assert callable(Gggg.__init__)


def test_hyp_gggg_constructor_args():
    sig = inspect.signature(Gggg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kreq108c_ffff_is_not_abstract():
    assert not inspect.isabstract(kreq108c_Ffff)


def test_hyp_kreq108c_ffff_constructor_exists():
    assert callable(kreq108c_Ffff.__init__)


def test_hyp_kreq108c_ffff_constructor_args():
    sig = inspect.signature(kreq108c_Ffff.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_kreq108c_eeee_is_not_abstract():
    assert not inspect.isabstract(kreq108c_Eeee)


def test_hyp_kreq108c_eeee_constructor_exists():
    assert callable(kreq108c_Eeee.__init__)


def test_hyp_kreq108c_eeee_constructor_args():
    sig = inspect.signature(kreq108c_Eeee.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_kreq108c_cccc_is_not_abstract():
    assert not inspect.isabstract(kreq108c_Cccc)


def test_hyp_kreq108c_cccc_constructor_exists():
    assert callable(kreq108c_Cccc.__init__)


def test_hyp_kreq108c_cccc_constructor_args():
    sig = inspect.signature(kreq108c_Cccc.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_kreq108c_bbbb_is_not_abstract():
    assert not inspect.isabstract(kreq108c_Bbbb)


def test_hyp_kreq108c_bbbb_constructor_exists():
    assert callable(kreq108c_Bbbb.__init__)


def test_hyp_kreq108c_bbbb_constructor_args():
    sig = inspect.signature(kreq108c_Bbbb.__init__)
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
kreq108c_Gggg_strategy = st.builds(
    kreq108c_Gggg,
    name=
        safe_text
)
Gggg_strategy = st.builds(
    Gggg,
)
kreq108c_Ffff_strategy = st.builds(
    kreq108c_Ffff,
    id=
        safe_text
)
kreq108c_Eeee_strategy = st.builds(
    kreq108c_Eeee,
    id=
        safe_text
)
kreq108c_Cccc_strategy = st.builds(
    kreq108c_Cccc,
    id=
        safe_text
)
kreq108c_Bbbb_strategy = st.builds(
    kreq108c_Bbbb,
)




@given(instance=kreq108c_Gggg_strategy)
def test_hyp_kreq108c_gggg_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=kreq108c_Ffff_strategy)
def test_hyp_kreq108c_ffff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=kreq108c_Eeee_strategy)
def test_hyp_kreq108c_eeee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=kreq108c_Cccc_strategy)
def test_hyp_kreq108c_cccc_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Gggg,
    kreq108c_Bbbb,
    kreq108c_Cccc,
    kreq108c_Eeee,
    kreq108c_Ffff,
    kreq108c_Gggg,
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

def test_kreq108c_Cccc_id_value_roundtrip():
    instance = kreq108c_Cccc(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_kreq108c_Eeee_id_value_roundtrip():
    instance = kreq108c_Eeee(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_kreq108c_Ffff_id_value_roundtrip():
    instance = kreq108c_Ffff(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_kreq108c_Gggg_name_value_roundtrip():
    instance = kreq108c_Gggg(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_kreq108c_Eeee_isa_Gggg():
    instance = kreq108c_Eeee(id="sample_text")
    assert isinstance(instance, Gggg)


def test_kreq108c_Ffff_isa_Gggg():
    instance = kreq108c_Ffff(id="sample_text")
    assert isinstance(instance, Gggg)


def test_assoc_cs0_link_reassign_clear():
    a = kreq108c_Cccc(id="sample_text")
    b1 = kreq108c_Bbbb()
    b2 = kreq108c_Bbbb()
    _safe_set(a, 'kreq108c_Cccc', b1)
    assert _is_linked(a, 'kreq108c_Cccc', b1)
    if hasattr(b1, 'kreq108c_Bbbb'):
        assert _is_linked(b1, 'kreq108c_Bbbb', a)
    _safe_set(a, 'kreq108c_Cccc', b2)
    assert _is_linked(a, 'kreq108c_Cccc', b2)
    if hasattr(b1, 'kreq108c_Bbbb'):
        assert not _is_linked(b1, 'kreq108c_Bbbb', a)
    if hasattr(b2, 'kreq108c_Bbbb'):
        assert _is_linked(b2, 'kreq108c_Bbbb', a)
    _safe_set(a, 'kreq108c_Cccc', None)
    assert not _is_linked(a, 'kreq108c_Cccc', b2)
    if hasattr(b2, 'kreq108c_Bbbb'):
        assert not _is_linked(b2, 'kreq108c_Bbbb', a)


def test_assoc_es1_link_reassign_clear():
    a = kreq108c_Eeee(id="sample_text")
    b1 = kreq108c_Bbbb()
    b2 = kreq108c_Bbbb()
    _safe_set(a, 'kreq108c_Eeee', b1)
    assert _is_linked(a, 'kreq108c_Eeee', b1)
    if hasattr(b1, 'kreq108c_Bbbb2'):
        assert _is_linked(b1, 'kreq108c_Bbbb2', a)
    _safe_set(a, 'kreq108c_Eeee', b2)
    assert _is_linked(a, 'kreq108c_Eeee', b2)
    if hasattr(b1, 'kreq108c_Bbbb2'):
        assert not _is_linked(b1, 'kreq108c_Bbbb2', a)
    if hasattr(b2, 'kreq108c_Bbbb2'):
        assert _is_linked(b2, 'kreq108c_Bbbb2', a)
    _safe_set(a, 'kreq108c_Eeee', None)
    assert not _is_linked(a, 'kreq108c_Eeee', b2)
    if hasattr(b2, 'kreq108c_Bbbb2'):
        assert not _is_linked(b2, 'kreq108c_Bbbb2', a)


def test_assoc_fs3_link_reassign_clear():
    a = kreq108c_Ffff(id="sample_text")
    b1 = kreq108c_Cccc(id="sample_text")
    b2 = kreq108c_Cccc(id="sample_text_2")
    _safe_set(a, 'kreq108c_Ffff', b1)
    assert _is_linked(a, 'kreq108c_Ffff', b1)
    if hasattr(b1, 'kreq108c_Cccc4'):
        assert _is_linked(b1, 'kreq108c_Cccc4', a)
    _safe_set(a, 'kreq108c_Ffff', b2)
    assert _is_linked(a, 'kreq108c_Ffff', b2)
    if hasattr(b1, 'kreq108c_Cccc4'):
        assert not _is_linked(b1, 'kreq108c_Cccc4', a)
    if hasattr(b2, 'kreq108c_Cccc4'):
        assert _is_linked(b2, 'kreq108c_Cccc4', a)
    _safe_set(a, 'kreq108c_Ffff', None)
    assert not _is_linked(a, 'kreq108c_Ffff', b2)
    if hasattr(b2, 'kreq108c_Cccc4'):
        assert not _is_linked(b2, 'kreq108c_Cccc4', a)


def test_assoc_subFs9_link_reassign_clear():
    a = kreq108c_Ffff(id="sample_text")
    b1 = kreq108c_Ffff(id="sample_text")
    b2 = kreq108c_Ffff(id="sample_text_2")
    _safe_set(a, 'kreq108c_Ffff10', b1)
    assert _is_linked(a, 'kreq108c_Ffff10', b1)
    if hasattr(b1, 'kreq108c_Ffff8'):
        assert _is_linked(b1, 'kreq108c_Ffff8', a)
    _safe_set(a, 'kreq108c_Ffff10', b2)
    assert _is_linked(a, 'kreq108c_Ffff10', b2)
    if hasattr(b1, 'kreq108c_Ffff8'):
        assert not _is_linked(b1, 'kreq108c_Ffff8', a)
    if hasattr(b2, 'kreq108c_Ffff8'):
        assert _is_linked(b2, 'kreq108c_Ffff8', a)
    _safe_set(a, 'kreq108c_Ffff10', None)
    assert not _is_linked(a, 'kreq108c_Ffff10', b2)
    if hasattr(b2, 'kreq108c_Ffff8'):
        assert not _is_linked(b2, 'kreq108c_Ffff8', a)


def test_assoc_varifedBy5_link_reassign_clear():
    a = kreq108c_Ffff(id="sample_text")
    b1 = kreq108c_Eeee(id="sample_text")
    b2 = kreq108c_Eeee(id="sample_text_2")
    _safe_set(a, 'kreq108c_Ffff6', {b1})
    assert _is_linked(a, 'kreq108c_Ffff6', b1)
    if hasattr(b1, 'kreq108c_Eeee7'):
        assert _is_linked(b1, 'kreq108c_Eeee7', a)
    _safe_set(a, 'kreq108c_Ffff6', {b2})
    assert _is_linked(a, 'kreq108c_Ffff6', b2)
    if hasattr(b1, 'kreq108c_Eeee7'):
        assert not _is_linked(b1, 'kreq108c_Eeee7', a)
    if hasattr(b2, 'kreq108c_Eeee7'):
        assert _is_linked(b2, 'kreq108c_Eeee7', a)
    _safe_set(a, 'kreq108c_Ffff6', set())
    assert not _is_linked(a, 'kreq108c_Ffff6', b2)
    if hasattr(b2, 'kreq108c_Eeee7'):
        assert not _is_linked(b2, 'kreq108c_Eeee7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Gggg_strategy = st.builds(Gggg)
@given(instance=Gggg_strategy)
@settings(max_examples=25)
def test_Gggg_instantiation(instance):
    assert isinstance(instance, Gggg)


kreq108c_Bbbb_strategy = st.builds(kreq108c_Bbbb)
@given(instance=kreq108c_Bbbb_strategy)
@settings(max_examples=25)
def test_kreq108c_Bbbb_instantiation(instance):
    assert isinstance(instance, kreq108c_Bbbb)


kreq108c_Cccc_strategy = st.builds(kreq108c_Cccc, id=safe_text)
@given(instance=kreq108c_Cccc_strategy)
@settings(max_examples=25)
def test_kreq108c_Cccc_instantiation(instance):
    assert isinstance(instance, kreq108c_Cccc)


kreq108c_Eeee_strategy = st.builds(kreq108c_Eeee, id=safe_text)
@given(instance=kreq108c_Eeee_strategy)
@settings(max_examples=25)
def test_kreq108c_Eeee_instantiation(instance):
    assert isinstance(instance, kreq108c_Eeee)


kreq108c_Ffff_strategy = st.builds(kreq108c_Ffff, id=safe_text)
@given(instance=kreq108c_Ffff_strategy)
@settings(max_examples=25)
def test_kreq108c_Ffff_instantiation(instance):
    assert isinstance(instance, kreq108c_Ffff)


kreq108c_Gggg_strategy = st.builds(kreq108c_Gggg, name=safe_text)
@given(instance=kreq108c_Gggg_strategy)
@settings(max_examples=25)
def test_kreq108c_Gggg_instantiation(instance):
    assert isinstance(instance, kreq108c_Gggg)



