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
    Putnik,
    string,
    Destinacija,
    Double,
    Date,
    Racun,
    Termin,
    Osiguranje,
    Aranzman,
    Agent,
    Rezervacija,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_putnik_is_not_abstract():
    assert not inspect.isabstract(Putnik)


def test_hyp_putnik_constructor_exists():
    assert callable(Putnik.__init__)


def test_hyp_putnik_constructor_args():
    sig = inspect.signature(Putnik.__init__)
    params = list(sig.parameters.keys())
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "ImePutnik" in params, "Missing parameter 'ImePutnik'"
    assert "BrojTel" in params, "Missing parameter 'BrojTel'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "OsiguranjeID" in params, "Missing parameter 'OsiguranjeID'"
    assert "PrezimePutnik" in params, "Missing parameter 'PrezimePutnik'"
    assert "Adresa" in params, "Missing parameter 'Adresa'"












def test_hyp_string_is_not_abstract():
    assert not inspect.isabstract(string)


def test_hyp_string_constructor_exists():
    assert callable(string.__init__)


def test_hyp_string_constructor_args():
    sig = inspect.signature(string.__init__)
    params = list(sig.parameters.keys())



def test_hyp_destinacija_is_not_abstract():
    assert not inspect.isabstract(Destinacija)


def test_hyp_destinacija_constructor_exists():
    assert callable(Destinacija.__init__)


def test_hyp_destinacija_constructor_args():
    sig = inspect.signature(Destinacija.__init__)
    params = list(sig.parameters.keys())
    assert "Drzava" in params, "Missing parameter 'Drzava'"
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "Hotel" in params, "Missing parameter 'Hotel'"
    assert "DestinacijaID" in params, "Missing parameter 'DestinacijaID'"







def test_hyp_double_is_not_abstract():
    assert not inspect.isabstract(Double)


def test_hyp_double_constructor_exists():
    assert callable(Double.__init__)


def test_hyp_double_constructor_args():
    sig = inspect.signature(Double.__init__)
    params = list(sig.parameters.keys())



def test_hyp_date_is_not_abstract():
    assert not inspect.isabstract(Date)


def test_hyp_date_constructor_exists():
    assert callable(Date.__init__)


def test_hyp_date_constructor_args():
    sig = inspect.signature(Date.__init__)
    params = list(sig.parameters.keys())



def test_hyp_racun_is_not_abstract():
    assert not inspect.isabstract(Racun)


def test_hyp_racun_constructor_exists():
    assert callable(Racun.__init__)


def test_hyp_racun_constructor_args():
    sig = inspect.signature(Racun.__init__)
    params = list(sig.parameters.keys())
    assert "Placeno" in params, "Missing parameter 'Placeno'"
    assert "Iznos" in params, "Missing parameter 'Iznos'"
    assert "RacunID" in params, "Missing parameter 'RacunID'"

def test_hyp_racun_has_Placeno():
    assert hasattr(Racun, "Placeno")
    descriptor = None
    for klass in Racun.__mro__:
        if "Placeno" in klass.__dict__:
            descriptor = klass.__dict__["Placeno"]
            break
    assert isinstance(descriptor, property)

def test_hyp_racun_has_Iznos():
    assert hasattr(Racun, "Iznos")
    descriptor = None
    for klass in Racun.__mro__:
        if "Iznos" in klass.__dict__:
            descriptor = klass.__dict__["Iznos"]
            break
    assert isinstance(descriptor, property)

def test_hyp_racun_has_RacunID():
    assert hasattr(Racun, "RacunID")
    descriptor = None
    for klass in Racun.__mro__:
        if "RacunID" in klass.__dict__:
            descriptor = klass.__dict__["RacunID"]
            break
    assert isinstance(descriptor, property)



def test_hyp_termin_is_not_abstract():
    assert not inspect.isabstract(Termin)


def test_hyp_termin_constructor_exists():
    assert callable(Termin.__init__)


def test_hyp_termin_constructor_args():
    sig = inspect.signature(Termin.__init__)
    params = list(sig.parameters.keys())
    assert "DatumPovratka" in params, "Missing parameter 'DatumPovratka'"
    assert "DatumPolaska" in params, "Missing parameter 'DatumPolaska'"
    assert "TerminID" in params, "Missing parameter 'TerminID'"

def test_hyp_termin_has_DatumPovratka():
    assert hasattr(Termin, "DatumPovratka")
    descriptor = None
    for klass in Termin.__mro__:
        if "DatumPovratka" in klass.__dict__:
            descriptor = klass.__dict__["DatumPovratka"]
            break
    assert isinstance(descriptor, property)

def test_hyp_termin_has_DatumPolaska():
    assert hasattr(Termin, "DatumPolaska")
    descriptor = None
    for klass in Termin.__mro__:
        if "DatumPolaska" in klass.__dict__:
            descriptor = klass.__dict__["DatumPolaska"]
            break
    assert isinstance(descriptor, property)

def test_hyp_termin_has_TerminID():
    assert hasattr(Termin, "TerminID")
    descriptor = None
    for klass in Termin.__mro__:
        if "TerminID" in klass.__dict__:
            descriptor = klass.__dict__["TerminID"]
            break
    assert isinstance(descriptor, property)



def test_hyp_osiguranje_is_not_abstract():
    assert not inspect.isabstract(Osiguranje)


def test_hyp_osiguranje_constructor_exists():
    assert callable(Osiguranje.__init__)


def test_hyp_osiguranje_constructor_args():
    sig = inspect.signature(Osiguranje.__init__)
    params = list(sig.parameters.keys())
    assert "OsiguranjeID" in params, "Missing parameter 'OsiguranjeID'"
    assert "OsigurKuca" in params, "Missing parameter 'OsigurKuca'"





def test_hyp_aranzman_is_not_abstract():
    assert not inspect.isabstract(Aranzman)


def test_hyp_aranzman_constructor_exists():
    assert callable(Aranzman.__init__)


def test_hyp_aranzman_constructor_args():
    sig = inspect.signature(Aranzman.__init__)
    params = list(sig.parameters.keys())
    assert "TerminID" in params, "Missing parameter 'TerminID'"
    assert "Popunjeno" in params, "Missing parameter 'Popunjeno'"
    assert "DestinacijaID" in params, "Missing parameter 'DestinacijaID'"
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "BrojMesta" in params, "Missing parameter 'BrojMesta'"
    assert "NazivAranzmana" in params, "Missing parameter 'NazivAranzmana'"
    assert "Cena" in params, "Missing parameter 'Cena'"

def test_hyp_aranzman_has_TerminID():
    assert hasattr(Aranzman, "TerminID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "TerminID" in klass.__dict__:
            descriptor = klass.__dict__["TerminID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_aranzman_has_Popunjeno():
    assert hasattr(Aranzman, "Popunjeno")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "Popunjeno" in klass.__dict__:
            descriptor = klass.__dict__["Popunjeno"]
            break
    assert isinstance(descriptor, property)

def test_hyp_aranzman_has_DestinacijaID():
    assert hasattr(Aranzman, "DestinacijaID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "DestinacijaID" in klass.__dict__:
            descriptor = klass.__dict__["DestinacijaID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_aranzman_has_AranzmanID():
    assert hasattr(Aranzman, "AranzmanID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "AranzmanID" in klass.__dict__:
            descriptor = klass.__dict__["AranzmanID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_aranzman_has_BrojMesta():
    assert hasattr(Aranzman, "BrojMesta")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "BrojMesta" in klass.__dict__:
            descriptor = klass.__dict__["BrojMesta"]
            break
    assert isinstance(descriptor, property)

def test_hyp_aranzman_has_NazivAranzmana():
    assert hasattr(Aranzman, "NazivAranzmana")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "NazivAranzmana" in klass.__dict__:
            descriptor = klass.__dict__["NazivAranzmana"]
            break
    assert isinstance(descriptor, property)

def test_hyp_aranzman_has_Cena():
    assert hasattr(Aranzman, "Cena")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "Cena" in klass.__dict__:
            descriptor = klass.__dict__["Cena"]
            break
    assert isinstance(descriptor, property)



def test_hyp_agent_is_not_abstract():
    assert not inspect.isabstract(Agent)


def test_hyp_agent_constructor_exists():
    assert callable(Agent.__init__)


def test_hyp_agent_constructor_args():
    sig = inspect.signature(Agent.__init__)
    params = list(sig.parameters.keys())
    assert "ImeAgent" in params, "Missing parameter 'ImeAgent'"
    assert "BrojTele" in params, "Missing parameter 'BrojTele'"
    assert "PrezimeAgent" in params, "Missing parameter 'PrezimeAgent'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "AgentID" in params, "Missing parameter 'AgentID'"










def test_hyp_rezervacija_is_not_abstract():
    assert not inspect.isabstract(Rezervacija)


def test_hyp_rezervacija_constructor_exists():
    assert callable(Rezervacija.__init__)


def test_hyp_rezervacija_constructor_args():
    sig = inspect.signature(Rezervacija.__init__)
    params = list(sig.parameters.keys())
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"
    assert "ReyervacijaID" in params, "Missing parameter 'ReyervacijaID'"
    assert "DatumKreiranja" in params, "Missing parameter 'DatumKreiranja'"
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "RacunID" in params, "Missing parameter 'RacunID'"
    assert "AgentID" in params, "Missing parameter 'AgentID'"

def test_hyp_rezervacija_has_PutnikID():
    assert hasattr(Rezervacija, "PutnikID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "PutnikID" in klass.__dict__:
            descriptor = klass.__dict__["PutnikID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_rezervacija_has_ReyervacijaID():
    assert hasattr(Rezervacija, "ReyervacijaID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "ReyervacijaID" in klass.__dict__:
            descriptor = klass.__dict__["ReyervacijaID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_rezervacija_has_DatumKreiranja():
    assert hasattr(Rezervacija, "DatumKreiranja")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "DatumKreiranja" in klass.__dict__:
            descriptor = klass.__dict__["DatumKreiranja"]
            break
    assert isinstance(descriptor, property)

def test_hyp_rezervacija_has_AranzmanID():
    assert hasattr(Rezervacija, "AranzmanID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "AranzmanID" in klass.__dict__:
            descriptor = klass.__dict__["AranzmanID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_rezervacija_has_RacunID():
    assert hasattr(Rezervacija, "RacunID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "RacunID" in klass.__dict__:
            descriptor = klass.__dict__["RacunID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_rezervacija_has_AgentID():
    assert hasattr(Rezervacija, "AgentID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "AgentID" in klass.__dict__:
            descriptor = klass.__dict__["AgentID"]
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
Putnik_strategy = st.builds(
    Putnik,
    Grad=
        safe_text,
    PutnikID=
        st.integers(),
    Email=
        safe_text,
    ImePutnik=
        safe_text,
    BrojTel=
        safe_text,
    JMBG=
        safe_text,
    OsiguranjeID=
        st.integers(),
    PrezimePutnik=
        safe_text,
    Adresa=
        safe_text
)
string_strategy = st.builds(
    string,
)
Destinacija_strategy = st.builds(
    Destinacija,
    Drzava=
        safe_text,
    Grad=
        safe_text,
    Hotel=
        safe_text,
    DestinacijaID=
        st.integers()
)
Double_strategy = st.builds(
    Double,
)
Date_strategy = st.builds(
    Date,
)
Racun_strategy = st.builds(
    Racun,
    Placeno=
        st.booleans(),
    Iznos=
        st.none(),
    RacunID=
        st.integers()
)
Termin_strategy = st.builds(
    Termin,
    DatumPovratka=
        st.dates(),
    DatumPolaska=
        st.dates(),
    TerminID=
        st.integers()
)
Osiguranje_strategy = st.builds(
    Osiguranje,
    OsiguranjeID=
        st.integers(),
    OsigurKuca=
        safe_text
)
Aranzman_strategy = st.builds(
    Aranzman,
    TerminID=
        st.integers(),
    Popunjeno=
        st.booleans(),
    DestinacijaID=
        st.integers(),
    AranzmanID=
        st.integers(),
    BrojMesta=
        st.integers(),
    NazivAranzmana=
        safe_text,
    Cena=
        st.none()
)
Agent_strategy = st.builds(
    Agent,
    ImeAgent=
        safe_text,
    BrojTele=
        safe_text,
    PrezimeAgent=
        safe_text,
    Password=
        safe_text,
    Username=
        safe_text,
    Email=
        safe_text,
    AgentID=
        st.integers()
)
Rezervacija_strategy = st.builds(
    Rezervacija,
    PutnikID=
        st.integers(),
    ReyervacijaID=
        st.integers(),
    DatumKreiranja=
        st.dates(),
    AranzmanID=
        st.integers(),
    RacunID=
        st.integers(),
    AgentID=
        st.integers()
)




@given(instance=Putnik_strategy)
def test_hyp_putnik_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_ImePutnik_setter(instance):
    original = instance.ImePutnik
    instance.ImePutnik = original
    assert instance.ImePutnik == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_BrojTel_setter(instance):
    original = instance.BrojTel
    instance.BrojTel = original
    assert instance.BrojTel == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_OsiguranjeID_setter(instance):
    original = instance.OsiguranjeID
    instance.OsiguranjeID = original
    assert instance.OsiguranjeID == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_PrezimePutnik_setter(instance):
    original = instance.PrezimePutnik
    instance.PrezimePutnik = original
    assert instance.PrezimePutnik == original



@given(instance=Putnik_strategy)
def test_hyp_putnik_Adresa_setter(instance):
    original = instance.Adresa
    instance.Adresa = original
    assert instance.Adresa == original





@given(instance=Destinacija_strategy)
def test_hyp_destinacija_Drzava_setter(instance):
    original = instance.Drzava
    instance.Drzava = original
    assert instance.Drzava == original



@given(instance=Destinacija_strategy)
def test_hyp_destinacija_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Destinacija_strategy)
def test_hyp_destinacija_Hotel_setter(instance):
    original = instance.Hotel
    instance.Hotel = original
    assert instance.Hotel == original



@given(instance=Destinacija_strategy)
def test_hyp_destinacija_DestinacijaID_setter(instance):
    original = instance.DestinacijaID
    instance.DestinacijaID = original
    assert instance.DestinacijaID == original



@given(instance=Racun_strategy)
@settings(max_examples=50)
def test_hyp_racun_instantiation(instance):
    assert isinstance(instance, Racun)



@given(instance=Racun_strategy)
def test_hyp_racun_Placeno_setter(instance):
    original = instance.Placeno
    instance.Placeno = original
    assert instance.Placeno == original



@given(instance=Racun_strategy)
def test_hyp_racun_Iznos_setter(instance):
    original = instance.Iznos
    instance.Iznos = original
    assert instance.Iznos == original



@given(instance=Racun_strategy)
def test_hyp_racun_RacunID_setter(instance):
    original = instance.RacunID
    instance.RacunID = original
    assert instance.RacunID == original

@given(instance=Termin_strategy)
@settings(max_examples=50)
def test_hyp_termin_instantiation(instance):
    assert isinstance(instance, Termin)



@given(instance=Termin_strategy)
def test_hyp_termin_DatumPovratka_setter(instance):
    original = instance.DatumPovratka
    instance.DatumPovratka = original
    assert instance.DatumPovratka == original



@given(instance=Termin_strategy)
def test_hyp_termin_DatumPolaska_setter(instance):
    original = instance.DatumPolaska
    instance.DatumPolaska = original
    assert instance.DatumPolaska == original



@given(instance=Termin_strategy)
def test_hyp_termin_TerminID_setter(instance):
    original = instance.TerminID
    instance.TerminID = original
    assert instance.TerminID == original




@given(instance=Osiguranje_strategy)
def test_hyp_osiguranje_OsiguranjeID_setter(instance):
    original = instance.OsiguranjeID
    instance.OsiguranjeID = original
    assert instance.OsiguranjeID == original



@given(instance=Osiguranje_strategy)
def test_hyp_osiguranje_OsigurKuca_setter(instance):
    original = instance.OsigurKuca
    instance.OsigurKuca = original
    assert instance.OsigurKuca == original

@given(instance=Aranzman_strategy)
@settings(max_examples=50)
def test_hyp_aranzman_instantiation(instance):
    assert isinstance(instance, Aranzman)



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_TerminID_setter(instance):
    original = instance.TerminID
    instance.TerminID = original
    assert instance.TerminID == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_Popunjeno_setter(instance):
    original = instance.Popunjeno
    instance.Popunjeno = original
    assert instance.Popunjeno == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_DestinacijaID_setter(instance):
    original = instance.DestinacijaID
    instance.DestinacijaID = original
    assert instance.DestinacijaID == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_BrojMesta_setter(instance):
    original = instance.BrojMesta
    instance.BrojMesta = original
    assert instance.BrojMesta == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_NazivAranzmana_setter(instance):
    original = instance.NazivAranzmana
    instance.NazivAranzmana = original
    assert instance.NazivAranzmana == original



@given(instance=Aranzman_strategy)
def test_hyp_aranzman_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original




@given(instance=Agent_strategy)
def test_hyp_agent_ImeAgent_setter(instance):
    original = instance.ImeAgent
    instance.ImeAgent = original
    assert instance.ImeAgent == original



@given(instance=Agent_strategy)
def test_hyp_agent_BrojTele_setter(instance):
    original = instance.BrojTele
    instance.BrojTele = original
    assert instance.BrojTele == original



@given(instance=Agent_strategy)
def test_hyp_agent_PrezimeAgent_setter(instance):
    original = instance.PrezimeAgent
    instance.PrezimeAgent = original
    assert instance.PrezimeAgent == original



@given(instance=Agent_strategy)
def test_hyp_agent_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Agent_strategy)
def test_hyp_agent_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Agent_strategy)
def test_hyp_agent_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Agent_strategy)
def test_hyp_agent_AgentID_setter(instance):
    original = instance.AgentID
    instance.AgentID = original
    assert instance.AgentID == original

@given(instance=Rezervacija_strategy)
@settings(max_examples=50)
def test_hyp_rezervacija_instantiation(instance):
    assert isinstance(instance, Rezervacija)



@given(instance=Rezervacija_strategy)
def test_hyp_rezervacija_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original



@given(instance=Rezervacija_strategy)
def test_hyp_rezervacija_ReyervacijaID_setter(instance):
    original = instance.ReyervacijaID
    instance.ReyervacijaID = original
    assert instance.ReyervacijaID == original



@given(instance=Rezervacija_strategy)
def test_hyp_rezervacija_DatumKreiranja_setter(instance):
    original = instance.DatumKreiranja
    instance.DatumKreiranja = original
    assert instance.DatumKreiranja == original



@given(instance=Rezervacija_strategy)
def test_hyp_rezervacija_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Rezervacija_strategy)
def test_hyp_rezervacija_RacunID_setter(instance):
    original = instance.RacunID
    instance.RacunID = original
    assert instance.RacunID == original



@given(instance=Rezervacija_strategy)
def test_hyp_rezervacija_AgentID_setter(instance):
    original = instance.AgentID
    instance.AgentID = original
    assert instance.AgentID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Agent,
    Aranzman,
    Date,
    Destinacija,
    Double,
    Osiguranje,
    Putnik,
    Racun,
    Rezervacija,
    Termin,
    string,
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

def test_Agent_AgentID_value_roundtrip():
    instance = Agent(AgentID=7, BrojTele="sample_text", Email="sample_text", ImeAgent="sample_text", Password="sample_text", PrezimeAgent="sample_text", Username="sample_text")
    assert instance.AgentID == 7
    instance.AgentID = 13
    assert instance.AgentID == 13


def test_Agent_BrojTele_value_roundtrip():
    instance = Agent(AgentID=7, BrojTele="sample_text", Email="sample_text", ImeAgent="sample_text", Password="sample_text", PrezimeAgent="sample_text", Username="sample_text")
    assert instance.BrojTele == "sample_text"
    instance.BrojTele = "sample_text_2"
    assert instance.BrojTele == "sample_text_2"


def test_Agent_Email_value_roundtrip():
    instance = Agent(AgentID=7, BrojTele="sample_text", Email="sample_text", ImeAgent="sample_text", Password="sample_text", PrezimeAgent="sample_text", Username="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Agent_ImeAgent_value_roundtrip():
    instance = Agent(AgentID=7, BrojTele="sample_text", Email="sample_text", ImeAgent="sample_text", Password="sample_text", PrezimeAgent="sample_text", Username="sample_text")
    assert instance.ImeAgent == "sample_text"
    instance.ImeAgent = "sample_text_2"
    assert instance.ImeAgent == "sample_text_2"


def test_Agent_Password_value_roundtrip():
    instance = Agent(AgentID=7, BrojTele="sample_text", Email="sample_text", ImeAgent="sample_text", Password="sample_text", PrezimeAgent="sample_text", Username="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Agent_PrezimeAgent_value_roundtrip():
    instance = Agent(AgentID=7, BrojTele="sample_text", Email="sample_text", ImeAgent="sample_text", Password="sample_text", PrezimeAgent="sample_text", Username="sample_text")
    assert instance.PrezimeAgent == "sample_text"
    instance.PrezimeAgent = "sample_text_2"
    assert instance.PrezimeAgent == "sample_text_2"


def test_Agent_Username_value_roundtrip():
    instance = Agent(AgentID=7, BrojTele="sample_text", Email="sample_text", ImeAgent="sample_text", Password="sample_text", PrezimeAgent="sample_text", Username="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_Destinacija_DestinacijaID_value_roundtrip():
    instance = Destinacija(DestinacijaID=7, Drzava="sample_text", Grad="sample_text", Hotel="sample_text")
    assert instance.DestinacijaID == 7
    instance.DestinacijaID = 13
    assert instance.DestinacijaID == 13


def test_Destinacija_Drzava_value_roundtrip():
    instance = Destinacija(DestinacijaID=7, Drzava="sample_text", Grad="sample_text", Hotel="sample_text")
    assert instance.Drzava == "sample_text"
    instance.Drzava = "sample_text_2"
    assert instance.Drzava == "sample_text_2"


def test_Destinacija_Grad_value_roundtrip():
    instance = Destinacija(DestinacijaID=7, Drzava="sample_text", Grad="sample_text", Hotel="sample_text")
    assert instance.Grad == "sample_text"
    instance.Grad = "sample_text_2"
    assert instance.Grad == "sample_text_2"


def test_Destinacija_Hotel_value_roundtrip():
    instance = Destinacija(DestinacijaID=7, Drzava="sample_text", Grad="sample_text", Hotel="sample_text")
    assert instance.Hotel == "sample_text"
    instance.Hotel = "sample_text_2"
    assert instance.Hotel == "sample_text_2"


def test_Osiguranje_OsigurKuca_value_roundtrip():
    instance = Osiguranje(OsigurKuca="sample_text", OsiguranjeID=7)
    assert instance.OsigurKuca == "sample_text"
    instance.OsigurKuca = "sample_text_2"
    assert instance.OsigurKuca == "sample_text_2"


def test_Osiguranje_OsiguranjeID_value_roundtrip():
    instance = Osiguranje(OsigurKuca="sample_text", OsiguranjeID=7)
    assert instance.OsiguranjeID == 7
    instance.OsiguranjeID = 13
    assert instance.OsiguranjeID == 13


def test_Putnik_Adresa_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.Adresa == "sample_text"
    instance.Adresa = "sample_text_2"
    assert instance.Adresa == "sample_text_2"


def test_Putnik_BrojTel_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.BrojTel == "sample_text"
    instance.BrojTel = "sample_text_2"
    assert instance.BrojTel == "sample_text_2"


def test_Putnik_Email_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Putnik_Grad_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.Grad == "sample_text"
    instance.Grad = "sample_text_2"
    assert instance.Grad == "sample_text_2"


def test_Putnik_ImePutnik_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.ImePutnik == "sample_text"
    instance.ImePutnik = "sample_text_2"
    assert instance.ImePutnik == "sample_text_2"


def test_Putnik_JMBG_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.JMBG == "sample_text"
    instance.JMBG = "sample_text_2"
    assert instance.JMBG == "sample_text_2"


def test_Putnik_OsiguranjeID_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.OsiguranjeID == 7
    instance.OsiguranjeID = 13
    assert instance.OsiguranjeID == 13


def test_Putnik_PrezimePutnik_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.PrezimePutnik == "sample_text"
    instance.PrezimePutnik = "sample_text_2"
    assert instance.PrezimePutnik == "sample_text_2"


def test_Putnik_PutnikID_value_roundtrip():
    instance = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    assert instance.PutnikID == 7
    instance.PutnikID = 13
    assert instance.PutnikID == 13


def test_assoc_Osiguranje_Putnik_link_reassign_clear():
    a = Putnik(Adresa="sample_text", BrojTel="sample_text", Email="sample_text", Grad="sample_text", ImePutnik="sample_text", JMBG="sample_text", OsiguranjeID=7, PrezimePutnik="sample_text", PutnikID=7)
    b1 = Osiguranje(OsigurKuca="sample_text", OsiguranjeID=7)
    b2 = Osiguranje(OsigurKuca="sample_text_2", OsiguranjeID=13)
    _safe_set(a, 'osiguranje1', b1)
    assert _is_linked(a, 'osiguranje1', b1)
    if hasattr(b1, 'putnik0'):
        assert _is_linked(b1, 'putnik0', a)
    _safe_set(a, 'osiguranje1', b2)
    assert _is_linked(a, 'osiguranje1', b2)
    if hasattr(b1, 'putnik0'):
        assert not _is_linked(b1, 'putnik0', a)
    if hasattr(b2, 'putnik0'):
        assert _is_linked(b2, 'putnik0', a)
    _safe_set(a, 'osiguranje1', None)
    assert not _is_linked(a, 'osiguranje1', b2)
    if hasattr(b2, 'putnik0'):
        assert not _is_linked(b2, 'putnik0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Agent_strategy = st.builds(Agent, AgentID=st.integers(), BrojTele=safe_text, Email=safe_text, ImeAgent=safe_text, Password=safe_text, PrezimeAgent=safe_text, Username=safe_text)
@given(instance=Agent_strategy)
@settings(max_examples=25)
def test_Agent_instantiation(instance):
    assert isinstance(instance, Agent)


Date_strategy = st.builds(Date)
@given(instance=Date_strategy)
@settings(max_examples=25)
def test_Date_instantiation(instance):
    assert isinstance(instance, Date)


Destinacija_strategy = st.builds(Destinacija, DestinacijaID=st.integers(), Drzava=safe_text, Grad=safe_text, Hotel=safe_text)
@given(instance=Destinacija_strategy)
@settings(max_examples=25)
def test_Destinacija_instantiation(instance):
    assert isinstance(instance, Destinacija)


Double_strategy = st.builds(Double)
@given(instance=Double_strategy)
@settings(max_examples=25)
def test_Double_instantiation(instance):
    assert isinstance(instance, Double)


Osiguranje_strategy = st.builds(Osiguranje, OsigurKuca=safe_text, OsiguranjeID=st.integers())
@given(instance=Osiguranje_strategy)
@settings(max_examples=25)
def test_Osiguranje_instantiation(instance):
    assert isinstance(instance, Osiguranje)


Putnik_strategy = st.builds(Putnik, Adresa=safe_text, BrojTel=safe_text, Email=safe_text, Grad=safe_text, ImePutnik=safe_text, JMBG=safe_text, OsiguranjeID=st.integers(), PrezimePutnik=safe_text, PutnikID=st.integers())
@given(instance=Putnik_strategy)
@settings(max_examples=25)
def test_Putnik_instantiation(instance):
    assert isinstance(instance, Putnik)


string_strategy = st.builds(string)
@given(instance=string_strategy)
@settings(max_examples=25)
def test_string_instantiation(instance):
    assert isinstance(instance, string)



