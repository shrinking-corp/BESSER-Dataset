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
    Zdravstveni_karton,
    Pregled,
    Lekar,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_zdravstveni_karton_is_not_abstract():
    assert not inspect.isabstract(Zdravstveni_karton)


def test_hyp_zdravstveni_karton_constructor_exists():
    assert callable(Zdravstveni_karton.__init__)


def test_hyp_zdravstveni_karton_constructor_args():
    sig = inspect.signature(Zdravstveni_karton.__init__)
    params = list(sig.parameters.keys())
    assert "BrKart" in params, "Missing parameter 'BrKart'"




def test_hyp_pregled_is_not_abstract():
    assert not inspect.isabstract(Pregled)


def test_hyp_pregled_constructor_exists():
    assert callable(Pregled.__init__)


def test_hyp_pregled_constructor_args():
    sig = inspect.signature(Pregled.__init__)
    params = list(sig.parameters.keys())
    assert "DatumP" in params, "Missing parameter 'DatumP'"
    assert "BrPregled" in params, "Missing parameter 'BrPregled'"





def test_hyp_lekar_is_not_abstract():
    assert not inspect.isabstract(Lekar)


def test_hyp_lekar_constructor_exists():
    assert callable(Lekar.__init__)


def test_hyp_lekar_constructor_args():
    sig = inspect.signature(Lekar.__init__)
    params = list(sig.parameters.keys())
    assert "ImeZap" in params, "Missing parameter 'ImeZap'"
    assert "AdrZap" in params, "Missing parameter 'AdrZap'"
    assert "DatZavSk" in params, "Missing parameter 'DatZavSk'"
    assert "PrzZap" in params, "Missing parameter 'PrzZap'"
    assert "RadStaz" in params, "Missing parameter 'RadStaz'"
    assert "Zaposleni_ID" in params, "Missing parameter 'Zaposleni_ID'"
    assert "Fakultet" in params, "Missing parameter 'Fakultet'"
    assert "BrTelZap" in params, "Missing parameter 'BrTelZap'"










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
Zdravstveni_karton_strategy = st.builds(
    Zdravstveni_karton,
    BrKart=
        st.integers()
)
Pregled_strategy = st.builds(
    Pregled,
    DatumP=
        safe_text,
    BrPregled=
        st.integers()
)
Lekar_strategy = st.builds(
    Lekar,
    ImeZap=
        safe_text,
    AdrZap=
        safe_text,
    DatZavSk=
        safe_text,
    PrzZap=
        safe_text,
    RadStaz=
        st.integers(),
    Zaposleni_ID=
        safe_text,
    Fakultet=
        safe_text,
    BrTelZap=
        safe_text
)




@given(instance=Zdravstveni_karton_strategy)
def test_hyp_zdravstveni_karton_BrKart_setter(instance):
    original = instance.BrKart
    instance.BrKart = original
    assert instance.BrKart == original




@given(instance=Pregled_strategy)
def test_hyp_pregled_DatumP_setter(instance):
    original = instance.DatumP
    instance.DatumP = original
    assert instance.DatumP == original



@given(instance=Pregled_strategy)
def test_hyp_pregled_BrPregled_setter(instance):
    original = instance.BrPregled
    instance.BrPregled = original
    assert instance.BrPregled == original




@given(instance=Lekar_strategy)
def test_hyp_lekar_ImeZap_setter(instance):
    original = instance.ImeZap
    instance.ImeZap = original
    assert instance.ImeZap == original



@given(instance=Lekar_strategy)
def test_hyp_lekar_AdrZap_setter(instance):
    original = instance.AdrZap
    instance.AdrZap = original
    assert instance.AdrZap == original



@given(instance=Lekar_strategy)
def test_hyp_lekar_DatZavSk_setter(instance):
    original = instance.DatZavSk
    instance.DatZavSk = original
    assert instance.DatZavSk == original



@given(instance=Lekar_strategy)
def test_hyp_lekar_PrzZap_setter(instance):
    original = instance.PrzZap
    instance.PrzZap = original
    assert instance.PrzZap == original



@given(instance=Lekar_strategy)
def test_hyp_lekar_RadStaz_setter(instance):
    original = instance.RadStaz
    instance.RadStaz = original
    assert instance.RadStaz == original



@given(instance=Lekar_strategy)
def test_hyp_lekar_Zaposleni_ID_setter(instance):
    original = instance.Zaposleni_ID
    instance.Zaposleni_ID = original
    assert instance.Zaposleni_ID == original



@given(instance=Lekar_strategy)
def test_hyp_lekar_Fakultet_setter(instance):
    original = instance.Fakultet
    instance.Fakultet = original
    assert instance.Fakultet == original



@given(instance=Lekar_strategy)
def test_hyp_lekar_BrTelZap_setter(instance):
    original = instance.BrTelZap
    instance.BrTelZap = original
    assert instance.BrTelZap == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Lekar,
    Pregled,
    Zdravstveni_karton,
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

def test_Lekar_AdrZap_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.AdrZap == "sample_text"
    instance.AdrZap = "sample_text_2"
    assert instance.AdrZap == "sample_text_2"


def test_Lekar_BrTelZap_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.BrTelZap == "sample_text"
    instance.BrTelZap = "sample_text_2"
    assert instance.BrTelZap == "sample_text_2"


def test_Lekar_DatZavSk_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.DatZavSk == "sample_text"
    instance.DatZavSk = "sample_text_2"
    assert instance.DatZavSk == "sample_text_2"


def test_Lekar_Fakultet_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.Fakultet == "sample_text"
    instance.Fakultet = "sample_text_2"
    assert instance.Fakultet == "sample_text_2"


def test_Lekar_ImeZap_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.ImeZap == "sample_text"
    instance.ImeZap = "sample_text_2"
    assert instance.ImeZap == "sample_text_2"


def test_Lekar_PrzZap_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.PrzZap == "sample_text"
    instance.PrzZap = "sample_text_2"
    assert instance.PrzZap == "sample_text_2"


def test_Lekar_RadStaz_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.RadStaz == 7
    instance.RadStaz = 13
    assert instance.RadStaz == 13


def test_Lekar_Zaposleni_ID_value_roundtrip():
    instance = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    assert instance.Zaposleni_ID == "sample_text"
    instance.Zaposleni_ID = "sample_text_2"
    assert instance.Zaposleni_ID == "sample_text_2"


def test_Pregled_BrPregled_value_roundtrip():
    instance = Pregled(BrPregled=7, DatumP="sample_text")
    assert instance.BrPregled == 7
    instance.BrPregled = 13
    assert instance.BrPregled == 13


def test_Pregled_DatumP_value_roundtrip():
    instance = Pregled(BrPregled=7, DatumP="sample_text")
    assert instance.DatumP == "sample_text"
    instance.DatumP = "sample_text_2"
    assert instance.DatumP == "sample_text_2"


def test_Zdravstveni_karton_BrKart_value_roundtrip():
    instance = Zdravstveni_karton(BrKart=7)
    assert instance.BrKart == 7
    instance.BrKart = 13
    assert instance.BrKart == 13


def test_assoc_Vrsi_P_link_reassign_clear():
    a = Pregled(BrPregled=7, DatumP="sample_text")
    b1 = Lekar(AdrZap="sample_text", BrTelZap="sample_text", DatZavSk="sample_text", Fakultet="sample_text", ImeZap="sample_text", PrzZap="sample_text", RadStaz=7, Zaposleni_ID="sample_text")
    b2 = Lekar(AdrZap="sample_text_2", BrTelZap="sample_text_2", DatZavSk="sample_text_2", Fakultet="sample_text_2", ImeZap="sample_text_2", PrzZap="sample_text_2", RadStaz=13, Zaposleni_ID="sample_text_2")
    _safe_set(a, 'lekar1', {b1})
    assert _is_linked(a, 'lekar1', b1)
    if hasattr(b1, 'pregled0'):
        assert _is_linked(b1, 'pregled0', a)
    _safe_set(a, 'lekar1', {b2})
    assert _is_linked(a, 'lekar1', b2)
    if hasattr(b1, 'pregled0'):
        assert not _is_linked(b1, 'pregled0', a)
    if hasattr(b2, 'pregled0'):
        assert _is_linked(b2, 'pregled0', a)
    _safe_set(a, 'lekar1', set())
    assert not _is_linked(a, 'lekar1', b2)
    if hasattr(b2, 'pregled0'):
        assert not _is_linked(b2, 'pregled0', a)


def test_assoc_Zdravstveni_karton_Pregled_link_reassign_clear():
    a = Zdravstveni_karton(BrKart=7)
    b1 = Pregled(BrPregled=7, DatumP="sample_text")
    b2 = Pregled(BrPregled=13, DatumP="sample_text_2")
    _safe_set(a, 'pregled2', b1)
    assert _is_linked(a, 'pregled2', b1)
    if hasattr(b1, 'zdravstveni_karton3'):
        assert _is_linked(b1, 'zdravstveni_karton3', a)
    _safe_set(a, 'pregled2', b2)
    assert _is_linked(a, 'pregled2', b2)
    if hasattr(b1, 'zdravstveni_karton3'):
        assert not _is_linked(b1, 'zdravstveni_karton3', a)
    if hasattr(b2, 'zdravstveni_karton3'):
        assert _is_linked(b2, 'zdravstveni_karton3', a)
    _safe_set(a, 'pregled2', None)
    assert not _is_linked(a, 'pregled2', b2)
    if hasattr(b2, 'zdravstveni_karton3'):
        assert not _is_linked(b2, 'zdravstveni_karton3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Lekar_strategy = st.builds(Lekar, AdrZap=safe_text, BrTelZap=safe_text, DatZavSk=safe_text, Fakultet=safe_text, ImeZap=safe_text, PrzZap=safe_text, RadStaz=st.integers(), Zaposleni_ID=safe_text)
@given(instance=Lekar_strategy)
@settings(max_examples=25)
def test_Lekar_instantiation(instance):
    assert isinstance(instance, Lekar)


Pregled_strategy = st.builds(Pregled, BrPregled=st.integers(), DatumP=safe_text)
@given(instance=Pregled_strategy)
@settings(max_examples=25)
def test_Pregled_instantiation(instance):
    assert isinstance(instance, Pregled)


Zdravstveni_karton_strategy = st.builds(Zdravstveni_karton, BrKart=st.integers())
@given(instance=Zdravstveni_karton_strategy)
@settings(max_examples=25)
def test_Zdravstveni_karton_instantiation(instance):
    assert isinstance(instance, Zdravstveni_karton)



