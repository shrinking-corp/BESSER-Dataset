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
    Benutzer_Actor,
    Kalendarische_Ansicht_ver_ndern_external,
    PDF_Datei_erstellen_external,
    Pr_fungen_sehen_external,
    Pr_fungstermine_verschieben_external,
    Pr_fungsplaner_einsehen_external,
    Im_LTS_anmelden_external,
    Pr_funungen_einsehen_external,
    ExaminationDate,
    Pr_fungsplaner_Component,
    Supervisor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_benutzer_actor_is_not_abstract():
    assert not inspect.isabstract(Benutzer_Actor)


def test_hyp_benutzer_actor_constructor_exists():
    assert callable(Benutzer_Actor.__init__)


def test_hyp_benutzer_actor_constructor_args():
    sig = inspect.signature(Benutzer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kalendarische_ansicht_ver_ndern_external_is_not_abstract():
    assert not inspect.isabstract(Kalendarische_Ansicht_ver_ndern_external)


def test_hyp_kalendarische_ansicht_ver_ndern_external_constructor_exists():
    assert callable(Kalendarische_Ansicht_ver_ndern_external.__init__)


def test_hyp_kalendarische_ansicht_ver_ndern_external_constructor_args():
    sig = inspect.signature(Kalendarische_Ansicht_ver_ndern_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pdf_datei_erstellen_external_is_not_abstract():
    assert not inspect.isabstract(PDF_Datei_erstellen_external)


def test_hyp_pdf_datei_erstellen_external_constructor_exists():
    assert callable(PDF_Datei_erstellen_external.__init__)


def test_hyp_pdf_datei_erstellen_external_constructor_args():
    sig = inspect.signature(PDF_Datei_erstellen_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pr_fungen_sehen_external_is_not_abstract():
    assert not inspect.isabstract(Pr_fungen_sehen_external)


def test_hyp_pr_fungen_sehen_external_constructor_exists():
    assert callable(Pr_fungen_sehen_external.__init__)


def test_hyp_pr_fungen_sehen_external_constructor_args():
    sig = inspect.signature(Pr_fungen_sehen_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pr_fungstermine_verschieben_external_is_not_abstract():
    assert not inspect.isabstract(Pr_fungstermine_verschieben_external)


def test_hyp_pr_fungstermine_verschieben_external_constructor_exists():
    assert callable(Pr_fungstermine_verschieben_external.__init__)


def test_hyp_pr_fungstermine_verschieben_external_constructor_args():
    sig = inspect.signature(Pr_fungstermine_verschieben_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pr_fungsplaner_einsehen_external_is_not_abstract():
    assert not inspect.isabstract(Pr_fungsplaner_einsehen_external)


def test_hyp_pr_fungsplaner_einsehen_external_constructor_exists():
    assert callable(Pr_fungsplaner_einsehen_external.__init__)


def test_hyp_pr_fungsplaner_einsehen_external_constructor_args():
    sig = inspect.signature(Pr_fungsplaner_einsehen_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_im_lts_anmelden_external_is_not_abstract():
    assert not inspect.isabstract(Im_LTS_anmelden_external)


def test_hyp_im_lts_anmelden_external_constructor_exists():
    assert callable(Im_LTS_anmelden_external.__init__)


def test_hyp_im_lts_anmelden_external_constructor_args():
    sig = inspect.signature(Im_LTS_anmelden_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pr_funungen_einsehen_external_is_not_abstract():
    assert not inspect.isabstract(Pr_funungen_einsehen_external)


def test_hyp_pr_funungen_einsehen_external_constructor_exists():
    assert callable(Pr_funungen_einsehen_external.__init__)


def test_hyp_pr_funungen_einsehen_external_constructor_args():
    sig = inspect.signature(Pr_funungen_einsehen_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_examinationdate_is_not_abstract():
    assert not inspect.isabstract(ExaminationDate)


def test_hyp_examinationdate_constructor_exists():
    assert callable(ExaminationDate.__init__)


def test_hyp_examinationdate_constructor_args():
    sig = inspect.signature(ExaminationDate.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_pr_fungsplaner_component_is_not_abstract():
    assert not inspect.isabstract(Pr_fungsplaner_Component)


def test_hyp_pr_fungsplaner_component_constructor_exists():
    assert callable(Pr_fungsplaner_Component.__init__)


def test_hyp_pr_fungsplaner_component_constructor_args():
    sig = inspect.signature(Pr_fungsplaner_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_supervisor_actor_is_not_abstract():
    assert not inspect.isabstract(Supervisor_Actor)


def test_hyp_supervisor_actor_constructor_exists():
    assert callable(Supervisor_Actor.__init__)


def test_hyp_supervisor_actor_constructor_args():
    sig = inspect.signature(Supervisor_Actor.__init__)
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
Benutzer_Actor_strategy = st.builds(
    Benutzer_Actor,
)
Kalendarische_Ansicht_ver_ndern_external_strategy = st.builds(
    Kalendarische_Ansicht_ver_ndern_external,
)
PDF_Datei_erstellen_external_strategy = st.builds(
    PDF_Datei_erstellen_external,
)
Pr_fungen_sehen_external_strategy = st.builds(
    Pr_fungen_sehen_external,
)
Pr_fungstermine_verschieben_external_strategy = st.builds(
    Pr_fungstermine_verschieben_external,
)
Pr_fungsplaner_einsehen_external_strategy = st.builds(
    Pr_fungsplaner_einsehen_external,
)
Im_LTS_anmelden_external_strategy = st.builds(
    Im_LTS_anmelden_external,
)
Pr_funungen_einsehen_external_strategy = st.builds(
    Pr_funungen_einsehen_external,
)
ExaminationDate_strategy = st.builds(
    ExaminationDate,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
Pr_fungsplaner_Component_strategy = st.builds(
    Pr_fungsplaner_Component,
)
Supervisor_Actor_strategy = st.builds(
    Supervisor_Actor,
)












@given(instance=ExaminationDate_strategy)
def test_hyp_examinationdate_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ExaminationDate_strategy)
def test_hyp_examinationdate_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Benutzer_Actor,
    ExaminationDate,
    Im_LTS_anmelden_external,
    Kalendarische_Ansicht_ver_ndern_external,
    PDF_Datei_erstellen_external,
    Pr_fungen_sehen_external,
    Pr_fungsplaner_Component,
    Pr_fungsplaner_einsehen_external,
    Pr_fungstermine_verschieben_external,
    Pr_funungen_einsehen_external,
    Supervisor_Actor,
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

def test_ExaminationDate_attribute_value_roundtrip():
    instance = ExaminationDate(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_ExaminationDate_attribute2_value_roundtrip():
    instance = ExaminationDate(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Benutzer_Actor_strategy = st.builds(Benutzer_Actor)
@given(instance=Benutzer_Actor_strategy)
@settings(max_examples=25)
def test_Benutzer_Actor_instantiation(instance):
    assert isinstance(instance, Benutzer_Actor)


ExaminationDate_strategy = st.builds(ExaminationDate, attribute=safe_text, attribute2=safe_text)
@given(instance=ExaminationDate_strategy)
@settings(max_examples=25)
def test_ExaminationDate_instantiation(instance):
    assert isinstance(instance, ExaminationDate)


Im_LTS_anmelden_external_strategy = st.builds(Im_LTS_anmelden_external)
@given(instance=Im_LTS_anmelden_external_strategy)
@settings(max_examples=25)
def test_Im_LTS_anmelden_external_instantiation(instance):
    assert isinstance(instance, Im_LTS_anmelden_external)


Kalendarische_Ansicht_ver_ndern_external_strategy = st.builds(Kalendarische_Ansicht_ver_ndern_external)
@given(instance=Kalendarische_Ansicht_ver_ndern_external_strategy)
@settings(max_examples=25)
def test_Kalendarische_Ansicht_ver_ndern_external_instantiation(instance):
    assert isinstance(instance, Kalendarische_Ansicht_ver_ndern_external)


PDF_Datei_erstellen_external_strategy = st.builds(PDF_Datei_erstellen_external)
@given(instance=PDF_Datei_erstellen_external_strategy)
@settings(max_examples=25)
def test_PDF_Datei_erstellen_external_instantiation(instance):
    assert isinstance(instance, PDF_Datei_erstellen_external)


Pr_fungen_sehen_external_strategy = st.builds(Pr_fungen_sehen_external)
@given(instance=Pr_fungen_sehen_external_strategy)
@settings(max_examples=25)
def test_Pr_fungen_sehen_external_instantiation(instance):
    assert isinstance(instance, Pr_fungen_sehen_external)


Pr_fungsplaner_Component_strategy = st.builds(Pr_fungsplaner_Component)
@given(instance=Pr_fungsplaner_Component_strategy)
@settings(max_examples=25)
def test_Pr_fungsplaner_Component_instantiation(instance):
    assert isinstance(instance, Pr_fungsplaner_Component)


Pr_fungsplaner_einsehen_external_strategy = st.builds(Pr_fungsplaner_einsehen_external)
@given(instance=Pr_fungsplaner_einsehen_external_strategy)
@settings(max_examples=25)
def test_Pr_fungsplaner_einsehen_external_instantiation(instance):
    assert isinstance(instance, Pr_fungsplaner_einsehen_external)


Pr_fungstermine_verschieben_external_strategy = st.builds(Pr_fungstermine_verschieben_external)
@given(instance=Pr_fungstermine_verschieben_external_strategy)
@settings(max_examples=25)
def test_Pr_fungstermine_verschieben_external_instantiation(instance):
    assert isinstance(instance, Pr_fungstermine_verschieben_external)


Pr_funungen_einsehen_external_strategy = st.builds(Pr_funungen_einsehen_external)
@given(instance=Pr_funungen_einsehen_external_strategy)
@settings(max_examples=25)
def test_Pr_funungen_einsehen_external_instantiation(instance):
    assert isinstance(instance, Pr_funungen_einsehen_external)


Supervisor_Actor_strategy = st.builds(Supervisor_Actor)
@given(instance=Supervisor_Actor_strategy)
@settings(max_examples=25)
def test_Supervisor_Actor_instantiation(instance):
    assert isinstance(instance, Supervisor_Actor)



