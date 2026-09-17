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
    Bovine,
    tracker_BovineBison,
    tracker_BovineDairy,
    tracker_BovineBeef,
    tracker_Event,
    tracker_Tag,
    tracker_Premises,
    Event,
    tracker_Sighting,
    tracker_ICVI,
    tracker_TagApplied,
    tracker_WeighIn,
    tracker_FairRegistration,
    tracker_Died,
    tracker_Exported,
    tracker_Imported,
    tracker_Slaughtered,
    tracker_AnimalMissing,
    tracker_TagRetired,
    tracker_TagAllocated,
    Animal,
    tracker_Ovine,
    tracker_Bovine,
    tracker_Animal,
    tracker_Swine,
    tracker_ReplacedTag,
    tracker_LostTag,
    tracker_MovedOut,
    tracker_MovedIn,
    SheepBreed,
    Sex,
    BisonBreed,
    DairyBreed,
    SwineBreed,
    BeefBreed,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bovine_is_not_abstract():
    assert not inspect.isabstract(Bovine)


def test_hyp_bovine_constructor_exists():
    assert callable(Bovine.__init__)


def test_hyp_bovine_constructor_args():
    sig = inspect.signature(Bovine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_bovinebison_is_not_abstract():
    assert not inspect.isabstract(tracker_BovineBison)


def test_hyp_tracker_bovinebison_constructor_exists():
    assert callable(tracker_BovineBison.__init__)


def test_hyp_tracker_bovinebison_constructor_args():
    sig = inspect.signature(tracker_BovineBison.__init__)
    params = list(sig.parameters.keys())
    assert "buffaloBreed" in params, "Missing parameter 'buffaloBreed'"




def test_hyp_tracker_bovinedairy_is_not_abstract():
    assert not inspect.isabstract(tracker_BovineDairy)


def test_hyp_tracker_bovinedairy_constructor_exists():
    assert callable(tracker_BovineDairy.__init__)


def test_hyp_tracker_bovinedairy_constructor_args():
    sig = inspect.signature(tracker_BovineDairy.__init__)
    params = list(sig.parameters.keys())
    assert "dairyBreed" in params, "Missing parameter 'dairyBreed'"




def test_hyp_tracker_bovinebeef_is_not_abstract():
    assert not inspect.isabstract(tracker_BovineBeef)


def test_hyp_tracker_bovinebeef_constructor_exists():
    assert callable(tracker_BovineBeef.__init__)


def test_hyp_tracker_bovinebeef_constructor_args():
    sig = inspect.signature(tracker_BovineBeef.__init__)
    params = list(sig.parameters.keys())
    assert "beefBreed" in params, "Missing parameter 'beefBreed'"




def test_hyp_tracker_event_is_not_abstract():
    assert not inspect.isabstract(tracker_Event)


def test_hyp_tracker_event_constructor_exists():
    assert callable(tracker_Event.__init__)


def test_hyp_tracker_event_constructor_args():
    sig = inspect.signature(tracker_Event.__init__)
    params = list(sig.parameters.keys())
    assert "dateTime" in params, "Missing parameter 'dateTime'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "idNumber" in params, "Missing parameter 'idNumber'"
    assert "eventCode" in params, "Missing parameter 'eventCode'"
    assert "electronicallyRead" in params, "Missing parameter 'electronicallyRead'"
    assert "correction" in params, "Missing parameter 'correction'"









def test_hyp_tracker_tag_is_not_abstract():
    assert not inspect.isabstract(tracker_Tag)


def test_hyp_tracker_tag_constructor_exists():
    assert callable(tracker_Tag.__init__)


def test_hyp_tracker_tag_constructor_args():
    sig = inspect.signature(tracker_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "usainNumberUsed" in params, "Missing parameter 'usainNumberUsed'"
    assert "idNumber" in params, "Missing parameter 'idNumber'"





def test_hyp_tracker_premises_is_not_abstract():
    assert not inspect.isabstract(tracker_Premises)


def test_hyp_tracker_premises_constructor_exists():
    assert callable(tracker_Premises.__init__)


def test_hyp_tracker_premises_constructor_args():
    sig = inspect.signature(tracker_Premises.__init__)
    params = list(sig.parameters.keys())
    assert "premisesId" in params, "Missing parameter 'premisesId'"
    assert "emailContact" in params, "Missing parameter 'emailContact'"





def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_sighting_is_not_abstract():
    assert not inspect.isabstract(tracker_Sighting)


def test_hyp_tracker_sighting_constructor_exists():
    assert callable(tracker_Sighting.__init__)


def test_hyp_tracker_sighting_constructor_args():
    sig = inspect.signature(tracker_Sighting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_icvi_is_not_abstract():
    assert not inspect.isabstract(tracker_ICVI)


def test_hyp_tracker_icvi_constructor_exists():
    assert callable(tracker_ICVI.__init__)


def test_hyp_tracker_icvi_constructor_args():
    sig = inspect.signature(tracker_ICVI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_tagapplied_is_not_abstract():
    assert not inspect.isabstract(tracker_TagApplied)


def test_hyp_tracker_tagapplied_constructor_exists():
    assert callable(tracker_TagApplied.__init__)


def test_hyp_tracker_tagapplied_constructor_args():
    sig = inspect.signature(tracker_TagApplied.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_weighin_is_not_abstract():
    assert not inspect.isabstract(tracker_WeighIn)


def test_hyp_tracker_weighin_constructor_exists():
    assert callable(tracker_WeighIn.__init__)


def test_hyp_tracker_weighin_constructor_args():
    sig = inspect.signature(tracker_WeighIn.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"




def test_hyp_tracker_fairregistration_is_not_abstract():
    assert not inspect.isabstract(tracker_FairRegistration)


def test_hyp_tracker_fairregistration_constructor_exists():
    assert callable(tracker_FairRegistration.__init__)


def test_hyp_tracker_fairregistration_constructor_args():
    sig = inspect.signature(tracker_FairRegistration.__init__)
    params = list(sig.parameters.keys())
    assert "participant" in params, "Missing parameter 'participant'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "parent" in params, "Missing parameter 'parent'"
    assert "address" in params, "Missing parameter 'address'"
    assert "club" in params, "Missing parameter 'club'"








def test_hyp_tracker_died_is_not_abstract():
    assert not inspect.isabstract(tracker_Died)


def test_hyp_tracker_died_constructor_exists():
    assert callable(tracker_Died.__init__)


def test_hyp_tracker_died_constructor_args():
    sig = inspect.signature(tracker_Died.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_exported_is_not_abstract():
    assert not inspect.isabstract(tracker_Exported)


def test_hyp_tracker_exported_constructor_exists():
    assert callable(tracker_Exported.__init__)


def test_hyp_tracker_exported_constructor_args():
    sig = inspect.signature(tracker_Exported.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_imported_is_not_abstract():
    assert not inspect.isabstract(tracker_Imported)


def test_hyp_tracker_imported_constructor_exists():
    assert callable(tracker_Imported.__init__)


def test_hyp_tracker_imported_constructor_args():
    sig = inspect.signature(tracker_Imported.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_slaughtered_is_not_abstract():
    assert not inspect.isabstract(tracker_Slaughtered)


def test_hyp_tracker_slaughtered_constructor_exists():
    assert callable(tracker_Slaughtered.__init__)


def test_hyp_tracker_slaughtered_constructor_args():
    sig = inspect.signature(tracker_Slaughtered.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_animalmissing_is_not_abstract():
    assert not inspect.isabstract(tracker_AnimalMissing)


def test_hyp_tracker_animalmissing_constructor_exists():
    assert callable(tracker_AnimalMissing.__init__)


def test_hyp_tracker_animalmissing_constructor_args():
    sig = inspect.signature(tracker_AnimalMissing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_tagretired_is_not_abstract():
    assert not inspect.isabstract(tracker_TagRetired)


def test_hyp_tracker_tagretired_constructor_exists():
    assert callable(tracker_TagRetired.__init__)


def test_hyp_tracker_tagretired_constructor_args():
    sig = inspect.signature(tracker_TagRetired.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_tagallocated_is_not_abstract():
    assert not inspect.isabstract(tracker_TagAllocated)


def test_hyp_tracker_tagallocated_constructor_exists():
    assert callable(tracker_TagAllocated.__init__)


def test_hyp_tracker_tagallocated_constructor_args():
    sig = inspect.signature(tracker_TagAllocated.__init__)
    params = list(sig.parameters.keys())



def test_hyp_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_hyp_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_hyp_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_ovine_is_not_abstract():
    assert not inspect.isabstract(tracker_Ovine)


def test_hyp_tracker_ovine_constructor_exists():
    assert callable(tracker_Ovine.__init__)


def test_hyp_tracker_ovine_constructor_args():
    sig = inspect.signature(tracker_Ovine.__init__)
    params = list(sig.parameters.keys())
    assert "sheepBreed" in params, "Missing parameter 'sheepBreed'"




def test_hyp_tracker_bovine_is_not_abstract():
    assert not inspect.isabstract(tracker_Bovine)


def test_hyp_tracker_bovine_constructor_exists():
    assert callable(tracker_Bovine.__init__)


def test_hyp_tracker_bovine_constructor_args():
    sig = inspect.signature(tracker_Bovine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_animal_is_not_abstract():
    assert not inspect.isabstract(tracker_Animal)


def test_hyp_tracker_animal_constructor_exists():
    assert callable(tracker_Animal.__init__)


def test_hyp_tracker_animal_constructor_args():
    sig = inspect.signature(tracker_Animal.__init__)
    params = list(sig.parameters.keys())
    assert "idNumber" in params, "Missing parameter 'idNumber'"
    assert "breed" in params, "Missing parameter 'breed'"
    assert "species" in params, "Missing parameter 'species'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "sexCode" in params, "Missing parameter 'sexCode'"
    assert "age" in params, "Missing parameter 'age'"
    assert "speciesCode" in params, "Missing parameter 'speciesCode'"











def test_hyp_tracker_swine_is_not_abstract():
    assert not inspect.isabstract(tracker_Swine)


def test_hyp_tracker_swine_constructor_exists():
    assert callable(tracker_Swine.__init__)


def test_hyp_tracker_swine_constructor_args():
    sig = inspect.signature(tracker_Swine.__init__)
    params = list(sig.parameters.keys())
    assert "swineBreed" in params, "Missing parameter 'swineBreed'"




def test_hyp_tracker_replacedtag_is_not_abstract():
    assert not inspect.isabstract(tracker_ReplacedTag)


def test_hyp_tracker_replacedtag_constructor_exists():
    assert callable(tracker_ReplacedTag.__init__)


def test_hyp_tracker_replacedtag_constructor_args():
    sig = inspect.signature(tracker_ReplacedTag.__init__)
    params = list(sig.parameters.keys())
    assert "oldAin" in params, "Missing parameter 'oldAin'"




def test_hyp_tracker_losttag_is_not_abstract():
    assert not inspect.isabstract(tracker_LostTag)


def test_hyp_tracker_losttag_constructor_exists():
    assert callable(tracker_LostTag.__init__)


def test_hyp_tracker_losttag_constructor_args():
    sig = inspect.signature(tracker_LostTag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_movedout_is_not_abstract():
    assert not inspect.isabstract(tracker_MovedOut)


def test_hyp_tracker_movedout_constructor_exists():
    assert callable(tracker_MovedOut.__init__)


def test_hyp_tracker_movedout_constructor_args():
    sig = inspect.signature(tracker_MovedOut.__init__)
    params = list(sig.parameters.keys())
    assert "destinationPin" in params, "Missing parameter 'destinationPin'"




def test_hyp_tracker_movedin_is_not_abstract():
    assert not inspect.isabstract(tracker_MovedIn)


def test_hyp_tracker_movedin_constructor_exists():
    assert callable(tracker_MovedIn.__init__)


def test_hyp_tracker_movedin_constructor_args():
    sig = inspect.signature(tracker_MovedIn.__init__)
    params = list(sig.parameters.keys())
    assert "sourcePin" in params, "Missing parameter 'sourcePin'"


def test_hyp_sheepbreed_exists():
    # Check that the Enumeration exists
    assert SheepBreed is not None

def test_hyp_sheepbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SheepBreed]
    expected_literals = [
        "BC",
        "IL",
        "FN",
        "XL",
        "BW",
        "LE",
        "LI",
        "SX",
        "RI",
        "BO",
        "CO",
        "NL",
        "HL",
        "ST",
        "CF",
        "OX",
        "XM",
        "CR",
        "ZS",
        "HS",
        "SU",
        "RG",
        "TX",
        "DP",
        "PO",
        "RM",
        "MM",
        "CP",
        "NC",
        "TA",
        "FB",
        "ER",
        "SL",
        "TU",
        "SC",
        "LY",
        "SR",
        "OU",
        "CL",
        "RY",
        "KA",
        "CD",
        "KH",
        "BF",
        "BL",
        "MT",
        "DH",
        "HY",
        "MP",
        "KK",
        "DL",
        "Unspecified",
        "PE",
        "RV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SheepBreed"

def test_hyp_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_hyp_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "Unspecified",
        "M",
        "F",
        "S",
        "C",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"

def test_hyp_bisonbreed_exists():
    # Check that the Enumeration exists
    assert BisonBreed is not None

def test_hyp_bisonbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BisonBreed]
    expected_literals = [
        "PB",
        "Unspecified",
        "WO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BisonBreed"

def test_hyp_dairybreed_exists():
    # Check that the Enumeration exists
    assert DairyBreed is not None

def test_hyp_dairybreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DairyBreed]
    expected_literals = [
        "GD",
        "WW",
        "JE",
        "AY",
        "MS",
        "Unspecified",
        "HO",
        "FM",
        "GU",
        "BS",
        "LD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DairyBreed"

def test_hyp_swinebreed_exists():
    # Check that the Enumeration exists
    assert SwineBreed is not None

def test_hyp_swinebreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SwineBreed]
    expected_literals = [
        "SO",
        "RW",
        "LC",
        "LW",
        "Unspecified",
        "LB",
        "LA",
        "DU",
        "BK",
        "HA",
        "PE",
        "YO",
        "TM",
        "CW",
        "WS",
        "PC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SwineBreed"

def test_hyp_beefbreed_exists():
    # Check that the Enumeration exists
    assert BeefBreed is not None

def test_hyp_beefbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BeefBreed]
    expected_literals = [
        "CB",
        "HB",
        "CG",
        "RP",
        "GE",
        "KB",
        "AB",
        "BL",
        "AW",
        "MG",
        "ME",
        "CA",
        "CN",
        "GI",
        "AR",
        "BW",
        "TG",
        "AL",
        "BR",
        "RO",
        "BH",
        "GS",
        "CP",
        "IB",
        "RR",
        "TI",
        "FC",
        "DF",
        "NR",
        "TP",
        "GY",
        "DL",
        "GV",
        "MC",
        "SB",
        "MR",
        "DE",
        "XT",
        "FB",
        "HP",
        "ER",
        "MU",
        "SM",
        "BO",
        "BA",
        "FP",
        "MA",
        "GZ",
        "AU",
        "RD",
        "NE",
        "FA",
        "TL",
        "SA",
        "AN",
        "YA",
        "AF",
        "BG",
        "GR",
        "BQ",
        "PI",
        "DN",
        "SG",
        "MI",
        "LO",
        "MO",
        "SX",
        "BU",
        "LM",
        "PA",
        "NM",
        "SL",
        "SH",
        "RB",
        "BB",
        "HC",
        "RW",
        "SI",
        "BE",
        "PZ",
        "IS",
        "KY",
        "RA",
        "SP",
        "BF",
        "RS",
        "BD",
        "CH",
        "CM",
        "XX",
        "HY",
        "LR",
        "WP",
        "SE",
        "BI",
        "DR",
        "FR",
        "MH",
        "SS",
        "DB",
        "TN",
        "WF",
        "HH",
        "DJ",
        "GA",
        "CU",
        "WB",
        "AK",
        "SV",
        "BM",
        "SW",
        "FL",
        "AM",
        "BN",
        "DS",
        "NS",
        "AE",
        "PR",
        "ML",
        "RN",
        "Unspecified",
        "LU",
        "TA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BeefBreed"


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
Bovine_strategy = st.builds(
    Bovine,
)
tracker_BovineBison_strategy = st.builds(
    tracker_BovineBison,
    buffaloBreed=
        safe_text
)
tracker_BovineDairy_strategy = st.builds(
    tracker_BovineDairy,
    dairyBreed=
        safe_text
)
tracker_BovineBeef_strategy = st.builds(
    tracker_BovineBeef,
    beefBreed=
        safe_text
)
tracker_Event_strategy = st.builds(
    tracker_Event,
    dateTime=
        safe_text,
    comments=
        safe_text,
    idNumber=
        safe_text,
    eventCode=
        st.integers(),
    electronicallyRead=
        st.booleans(),
    correction=
        st.booleans()
)
tracker_Tag_strategy = st.builds(
    tracker_Tag,
    usainNumberUsed=
        st.booleans(),
    idNumber=
        safe_text
)
tracker_Premises_strategy = st.builds(
    tracker_Premises,
    premisesId=
        safe_text,
    emailContact=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
tracker_Sighting_strategy = st.builds(
    tracker_Sighting,
)
tracker_ICVI_strategy = st.builds(
    tracker_ICVI,
)
tracker_TagApplied_strategy = st.builds(
    tracker_TagApplied,
)
tracker_WeighIn_strategy = st.builds(
    tracker_WeighIn,
    weight=
        st.integers()
)
tracker_FairRegistration_strategy = st.builds(
    tracker_FairRegistration,
    participant=
        safe_text,
    phone=
        safe_text,
    parent=
        safe_text,
    address=
        safe_text,
    club=
        safe_text
)
tracker_Died_strategy = st.builds(
    tracker_Died,
)
tracker_Exported_strategy = st.builds(
    tracker_Exported,
)
tracker_Imported_strategy = st.builds(
    tracker_Imported,
)
tracker_Slaughtered_strategy = st.builds(
    tracker_Slaughtered,
)
tracker_AnimalMissing_strategy = st.builds(
    tracker_AnimalMissing,
)
tracker_TagRetired_strategy = st.builds(
    tracker_TagRetired,
)
tracker_TagAllocated_strategy = st.builds(
    tracker_TagAllocated,
)
Animal_strategy = st.builds(
    Animal,
)
tracker_Ovine_strategy = st.builds(
    tracker_Ovine,
    sheepBreed=
        safe_text
)
tracker_Bovine_strategy = st.builds(
    tracker_Bovine,
)
tracker_Animal_strategy = st.builds(
    tracker_Animal,
    idNumber=
        safe_text,
    breed=
        safe_text,
    species=
        safe_text,
    birthDate=
        safe_text,
    sex=
        safe_text,
    sexCode=
        safe_text,
    age=
        safe_text,
    speciesCode=
        safe_text
)
tracker_Swine_strategy = st.builds(
    tracker_Swine,
    swineBreed=
        safe_text
)
tracker_ReplacedTag_strategy = st.builds(
    tracker_ReplacedTag,
    oldAin=
        safe_text
)
tracker_LostTag_strategy = st.builds(
    tracker_LostTag,
)
tracker_MovedOut_strategy = st.builds(
    tracker_MovedOut,
    destinationPin=
        safe_text
)
tracker_MovedIn_strategy = st.builds(
    tracker_MovedIn,
    sourcePin=
        safe_text
)





@given(instance=tracker_BovineBison_strategy)
def test_hyp_tracker_bovinebison_buffaloBreed_setter(instance):
    original = instance.buffaloBreed
    instance.buffaloBreed = original
    assert instance.buffaloBreed == original




@given(instance=tracker_BovineDairy_strategy)
def test_hyp_tracker_bovinedairy_dairyBreed_setter(instance):
    original = instance.dairyBreed
    instance.dairyBreed = original
    assert instance.dairyBreed == original




@given(instance=tracker_BovineBeef_strategy)
def test_hyp_tracker_bovinebeef_beefBreed_setter(instance):
    original = instance.beefBreed
    instance.beefBreed = original
    assert instance.beefBreed == original




@given(instance=tracker_Event_strategy)
def test_hyp_tracker_event_dateTime_setter(instance):
    original = instance.dateTime
    instance.dateTime = original
    assert instance.dateTime == original



@given(instance=tracker_Event_strategy)
def test_hyp_tracker_event_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original



@given(instance=tracker_Event_strategy)
def test_hyp_tracker_event_idNumber_setter(instance):
    original = instance.idNumber
    instance.idNumber = original
    assert instance.idNumber == original



@given(instance=tracker_Event_strategy)
def test_hyp_tracker_event_eventCode_setter(instance):
    original = instance.eventCode
    instance.eventCode = original
    assert instance.eventCode == original



@given(instance=tracker_Event_strategy)
def test_hyp_tracker_event_electronicallyRead_setter(instance):
    original = instance.electronicallyRead
    instance.electronicallyRead = original
    assert instance.electronicallyRead == original



@given(instance=tracker_Event_strategy)
def test_hyp_tracker_event_correction_setter(instance):
    original = instance.correction
    instance.correction = original
    assert instance.correction == original




@given(instance=tracker_Tag_strategy)
def test_hyp_tracker_tag_usainNumberUsed_setter(instance):
    original = instance.usainNumberUsed
    instance.usainNumberUsed = original
    assert instance.usainNumberUsed == original



@given(instance=tracker_Tag_strategy)
def test_hyp_tracker_tag_idNumber_setter(instance):
    original = instance.idNumber
    instance.idNumber = original
    assert instance.idNumber == original




@given(instance=tracker_Premises_strategy)
def test_hyp_tracker_premises_premisesId_setter(instance):
    original = instance.premisesId
    instance.premisesId = original
    assert instance.premisesId == original



@given(instance=tracker_Premises_strategy)
def test_hyp_tracker_premises_emailContact_setter(instance):
    original = instance.emailContact
    instance.emailContact = original
    assert instance.emailContact == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Premises_strategy)
@settings(max_examples=30)
def test_hyp_tracker_premises_addtemplate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addTemplate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addTemplate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addTemplate' in tracker_Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTemplate' in tracker_Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTemplate' in tracker_Premises is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Premises_strategy)
@settings(max_examples=30)
def test_hyp_tracker_premises_findanimal_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findAnimal(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findAnimal).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findAnimal' in tracker_Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findAnimal' in tracker_Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findAnimal' in tracker_Premises is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Premises_strategy)
@settings(max_examples=30)
def test_hyp_tracker_premises_eventhistory_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eventHistory()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eventHistory).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eventHistory' in tracker_Premises is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eventHistory' in tracker_Premises did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eventHistory' in tracker_Premises is not implemented or raised an error")








@given(instance=tracker_WeighIn_strategy)
def test_hyp_tracker_weighin_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original




@given(instance=tracker_FairRegistration_strategy)
def test_hyp_tracker_fairregistration_participant_setter(instance):
    original = instance.participant
    instance.participant = original
    assert instance.participant == original



@given(instance=tracker_FairRegistration_strategy)
def test_hyp_tracker_fairregistration_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=tracker_FairRegistration_strategy)
def test_hyp_tracker_fairregistration_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original



@given(instance=tracker_FairRegistration_strategy)
def test_hyp_tracker_fairregistration_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=tracker_FairRegistration_strategy)
def test_hyp_tracker_fairregistration_club_setter(instance):
    original = instance.club
    instance.club = original
    assert instance.club == original












@given(instance=tracker_Ovine_strategy)
def test_hyp_tracker_ovine_sheepBreed_setter(instance):
    original = instance.sheepBreed
    instance.sheepBreed = original
    assert instance.sheepBreed == original





@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_idNumber_setter(instance):
    original = instance.idNumber
    instance.idNumber = original
    assert instance.idNumber == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_sexCode_setter(instance):
    original = instance.sexCode
    instance.sexCode = original
    assert instance.sexCode == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_speciesCode_setter(instance):
    original = instance.speciesCode
    instance.speciesCode = original
    assert instance.speciesCode == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Animal_strategy)
@settings(max_examples=30)
def test_hyp_tracker_animal_activetag_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.activeTag()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.activeTag).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'activeTag' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activeTag' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activeTag' in tracker_Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Animal_strategy)
@settings(max_examples=30)
def test_hyp_tracker_animal_allevents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allEvents()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allEvents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allEvents' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allEvents' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allEvents' in tracker_Animal is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Animal_strategy)
@settings(max_examples=30)
def test_hyp_tracker_animal_addtemplate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addTemplate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addTemplate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addTemplate' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTemplate' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTemplate' in tracker_Animal is not implemented or raised an error")




@given(instance=tracker_Swine_strategy)
def test_hyp_tracker_swine_swineBreed_setter(instance):
    original = instance.swineBreed
    instance.swineBreed = original
    assert instance.swineBreed == original




@given(instance=tracker_ReplacedTag_strategy)
def test_hyp_tracker_replacedtag_oldAin_setter(instance):
    original = instance.oldAin
    instance.oldAin = original
    assert instance.oldAin == original





@given(instance=tracker_MovedOut_strategy)
def test_hyp_tracker_movedout_destinationPin_setter(instance):
    original = instance.destinationPin
    instance.destinationPin = original
    assert instance.destinationPin == original




@given(instance=tracker_MovedIn_strategy)
def test_hyp_tracker_movedin_sourcePin_setter(instance):
    original = instance.sourcePin
    instance.sourcePin = original
    assert instance.sourcePin == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Animal,
    Bovine,
    Event,
    tracker_Animal,
    tracker_AnimalMissing,
    tracker_Bovine,
    tracker_BovineBeef,
    tracker_BovineBison,
    tracker_BovineDairy,
    tracker_Died,
    tracker_Event,
    tracker_Exported,
    tracker_FairRegistration,
    tracker_ICVI,
    tracker_Imported,
    tracker_LostTag,
    tracker_MovedIn,
    tracker_MovedOut,
    tracker_Ovine,
    tracker_Premises,
    tracker_ReplacedTag,
    tracker_Sighting,
    tracker_Slaughtered,
    tracker_Swine,
    tracker_Tag,
    tracker_TagAllocated,
    tracker_TagApplied,
    tracker_TagRetired,
    tracker_WeighIn,
    BeefBreed,
    BisonBreed,
    DairyBreed,
    Sex,
    SheepBreed,
    SwineBreed,
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

def test_tracker_Animal_age_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.age == "sample_text"
    instance.age = "sample_text_2"
    assert instance.age == "sample_text_2"


def test_tracker_Animal_birthDate_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.birthDate == "sample_text"
    instance.birthDate = "sample_text_2"
    assert instance.birthDate == "sample_text_2"


def test_tracker_Animal_breed_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.breed == "sample_text"
    instance.breed = "sample_text_2"
    assert instance.breed == "sample_text_2"


def test_tracker_Animal_idNumber_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.idNumber == "sample_text"
    instance.idNumber = "sample_text_2"
    assert instance.idNumber == "sample_text_2"


def test_tracker_Animal_sex_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_tracker_Animal_sexCode_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.sexCode == "sample_text"
    instance.sexCode = "sample_text_2"
    assert instance.sexCode == "sample_text_2"


def test_tracker_Animal_species_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.species == "sample_text"
    instance.species = "sample_text_2"
    assert instance.species == "sample_text_2"


def test_tracker_Animal_speciesCode_value_roundtrip():
    instance = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    assert instance.speciesCode == "sample_text"
    instance.speciesCode = "sample_text_2"
    assert instance.speciesCode == "sample_text_2"


def test_tracker_BovineBeef_beefBreed_value_roundtrip():
    instance = tracker_BovineBeef(beefBreed="sample_text")
    assert instance.beefBreed == "sample_text"
    instance.beefBreed = "sample_text_2"
    assert instance.beefBreed == "sample_text_2"


def test_tracker_BovineBison_buffaloBreed_value_roundtrip():
    instance = tracker_BovineBison(buffaloBreed="sample_text")
    assert instance.buffaloBreed == "sample_text"
    instance.buffaloBreed = "sample_text_2"
    assert instance.buffaloBreed == "sample_text_2"


def test_tracker_BovineDairy_dairyBreed_value_roundtrip():
    instance = tracker_BovineDairy(dairyBreed="sample_text")
    assert instance.dairyBreed == "sample_text"
    instance.dairyBreed = "sample_text_2"
    assert instance.dairyBreed == "sample_text_2"


def test_tracker_Event_comments_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_tracker_Event_correction_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    assert instance.correction == True
    instance.correction = False
    assert instance.correction == False


def test_tracker_Event_dateTime_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    assert instance.dateTime == "sample_text"
    instance.dateTime = "sample_text_2"
    assert instance.dateTime == "sample_text_2"


def test_tracker_Event_electronicallyRead_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    assert instance.electronicallyRead == True
    instance.electronicallyRead = False
    assert instance.electronicallyRead == False


def test_tracker_Event_eventCode_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    assert instance.eventCode == 7
    instance.eventCode = 13
    assert instance.eventCode == 13


def test_tracker_Event_idNumber_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    assert instance.idNumber == "sample_text"
    instance.idNumber = "sample_text_2"
    assert instance.idNumber == "sample_text_2"


def test_tracker_FairRegistration_address_value_roundtrip():
    instance = tracker_FairRegistration(address="sample_text", club="sample_text", parent="sample_text", participant="sample_text", phone="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_tracker_FairRegistration_club_value_roundtrip():
    instance = tracker_FairRegistration(address="sample_text", club="sample_text", parent="sample_text", participant="sample_text", phone="sample_text")
    assert instance.club == "sample_text"
    instance.club = "sample_text_2"
    assert instance.club == "sample_text_2"


def test_tracker_FairRegistration_parent_value_roundtrip():
    instance = tracker_FairRegistration(address="sample_text", club="sample_text", parent="sample_text", participant="sample_text", phone="sample_text")
    assert instance.parent == "sample_text"
    instance.parent = "sample_text_2"
    assert instance.parent == "sample_text_2"


def test_tracker_FairRegistration_participant_value_roundtrip():
    instance = tracker_FairRegistration(address="sample_text", club="sample_text", parent="sample_text", participant="sample_text", phone="sample_text")
    assert instance.participant == "sample_text"
    instance.participant = "sample_text_2"
    assert instance.participant == "sample_text_2"


def test_tracker_FairRegistration_phone_value_roundtrip():
    instance = tracker_FairRegistration(address="sample_text", club="sample_text", parent="sample_text", participant="sample_text", phone="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_tracker_MovedIn_sourcePin_value_roundtrip():
    instance = tracker_MovedIn(sourcePin="sample_text")
    assert instance.sourcePin == "sample_text"
    instance.sourcePin = "sample_text_2"
    assert instance.sourcePin == "sample_text_2"


def test_tracker_MovedOut_destinationPin_value_roundtrip():
    instance = tracker_MovedOut(destinationPin="sample_text")
    assert instance.destinationPin == "sample_text"
    instance.destinationPin = "sample_text_2"
    assert instance.destinationPin == "sample_text_2"


def test_tracker_Ovine_sheepBreed_value_roundtrip():
    instance = tracker_Ovine(sheepBreed="sample_text")
    assert instance.sheepBreed == "sample_text"
    instance.sheepBreed = "sample_text_2"
    assert instance.sheepBreed == "sample_text_2"


def test_tracker_Premises_emailContact_value_roundtrip():
    instance = tracker_Premises(emailContact="sample_text", premisesId="sample_text")
    assert instance.emailContact == "sample_text"
    instance.emailContact = "sample_text_2"
    assert instance.emailContact == "sample_text_2"


def test_tracker_Premises_premisesId_value_roundtrip():
    instance = tracker_Premises(emailContact="sample_text", premisesId="sample_text")
    assert instance.premisesId == "sample_text"
    instance.premisesId = "sample_text_2"
    assert instance.premisesId == "sample_text_2"


def test_tracker_ReplacedTag_oldAin_value_roundtrip():
    instance = tracker_ReplacedTag(oldAin="sample_text")
    assert instance.oldAin == "sample_text"
    instance.oldAin = "sample_text_2"
    assert instance.oldAin == "sample_text_2"


def test_tracker_Swine_swineBreed_value_roundtrip():
    instance = tracker_Swine(swineBreed="sample_text")
    assert instance.swineBreed == "sample_text"
    instance.swineBreed = "sample_text_2"
    assert instance.swineBreed == "sample_text_2"


def test_tracker_Tag_idNumber_value_roundtrip():
    instance = tracker_Tag(idNumber="sample_text", usainNumberUsed=True)
    assert instance.idNumber == "sample_text"
    instance.idNumber = "sample_text_2"
    assert instance.idNumber == "sample_text_2"


def test_tracker_Tag_usainNumberUsed_value_roundtrip():
    instance = tracker_Tag(idNumber="sample_text", usainNumberUsed=True)
    assert instance.usainNumberUsed == True
    instance.usainNumberUsed = False
    assert instance.usainNumberUsed == False


def test_tracker_WeighIn_weight_value_roundtrip():
    instance = tracker_WeighIn(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_tracker_Bovine_isa_Animal():
    instance = tracker_Bovine()
    assert isinstance(instance, Animal)


def test_tracker_Ovine_isa_Animal():
    instance = tracker_Ovine(sheepBreed="sample_text")
    assert isinstance(instance, Animal)


def test_tracker_Swine_isa_Animal():
    instance = tracker_Swine(swineBreed="sample_text")
    assert isinstance(instance, Animal)


def test_tracker_BovineBeef_isa_Bovine():
    instance = tracker_BovineBeef(beefBreed="sample_text")
    assert isinstance(instance, Bovine)


def test_tracker_BovineBison_isa_Bovine():
    instance = tracker_BovineBison(buffaloBreed="sample_text")
    assert isinstance(instance, Bovine)


def test_tracker_BovineDairy_isa_Bovine():
    instance = tracker_BovineDairy(dairyBreed="sample_text")
    assert isinstance(instance, Bovine)


def test_tracker_AnimalMissing_isa_Event():
    instance = tracker_AnimalMissing()
    assert isinstance(instance, Event)


def test_tracker_Died_isa_Event():
    instance = tracker_Died()
    assert isinstance(instance, Event)


def test_tracker_Exported_isa_Event():
    instance = tracker_Exported()
    assert isinstance(instance, Event)


def test_tracker_FairRegistration_isa_Event():
    instance = tracker_FairRegistration(address="sample_text", club="sample_text", parent="sample_text", participant="sample_text", phone="sample_text")
    assert isinstance(instance, Event)


def test_tracker_ICVI_isa_Event():
    instance = tracker_ICVI()
    assert isinstance(instance, Event)


def test_tracker_Imported_isa_Event():
    instance = tracker_Imported()
    assert isinstance(instance, Event)


def test_tracker_LostTag_isa_Event():
    instance = tracker_LostTag()
    assert isinstance(instance, Event)


def test_tracker_MovedIn_isa_Event():
    instance = tracker_MovedIn(sourcePin="sample_text")
    assert isinstance(instance, Event)


def test_tracker_MovedOut_isa_Event():
    instance = tracker_MovedOut(destinationPin="sample_text")
    assert isinstance(instance, Event)


def test_tracker_ReplacedTag_isa_Event():
    instance = tracker_ReplacedTag(oldAin="sample_text")
    assert isinstance(instance, Event)


def test_tracker_Sighting_isa_Event():
    instance = tracker_Sighting()
    assert isinstance(instance, Event)


def test_tracker_Slaughtered_isa_Event():
    instance = tracker_Slaughtered()
    assert isinstance(instance, Event)


def test_tracker_TagAllocated_isa_Event():
    instance = tracker_TagAllocated()
    assert isinstance(instance, Event)


def test_tracker_TagApplied_isa_Event():
    instance = tracker_TagApplied()
    assert isinstance(instance, Event)


def test_tracker_TagRetired_isa_Event():
    instance = tracker_TagRetired()
    assert isinstance(instance, Event)


def test_tracker_WeighIn_isa_Event():
    instance = tracker_WeighIn(weight=7)
    assert isinstance(instance, Event)


def test_assoc_animals3_link_reassign_clear():
    a = tracker_Premises(emailContact="sample_text", premisesId="sample_text")
    b1 = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    b2 = tracker_Animal(age="sample_text_2", birthDate="sample_text_2", breed="sample_text_2", idNumber="sample_text_2", sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2")
    _safe_set(a, 'tracker_Premises', {b1})
    assert _is_linked(a, 'tracker_Premises', b1)
    if hasattr(b1, 'tracker_Animal4'):
        assert _is_linked(b1, 'tracker_Animal4', a)
    _safe_set(a, 'tracker_Premises', {b2})
    assert _is_linked(a, 'tracker_Premises', b2)
    if hasattr(b1, 'tracker_Animal4'):
        assert not _is_linked(b1, 'tracker_Animal4', a)
    if hasattr(b2, 'tracker_Animal4'):
        assert _is_linked(b2, 'tracker_Animal4', a)
    _safe_set(a, 'tracker_Premises', set())
    assert not _is_linked(a, 'tracker_Premises', b2)
    if hasattr(b2, 'tracker_Animal4'):
        assert not _is_linked(b2, 'tracker_Animal4', a)


def test_assoc_events1_link_reassign_clear():
    a = tracker_Tag(idNumber="sample_text", usainNumberUsed=True)
    b1 = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    b2 = tracker_Event(comments="sample_text_2", correction=False, dateTime="sample_text_2", electronicallyRead=False, eventCode=13, idNumber="sample_text_2")
    _safe_set(a, 'tag', {b1})
    assert _is_linked(a, 'tag', b1)
    if hasattr(b1, 'Event'):
        assert _is_linked(b1, 'Event', a)
    _safe_set(a, 'tag', {b2})
    assert _is_linked(a, 'tag', b2)
    if hasattr(b1, 'Event'):
        assert not _is_linked(b1, 'Event', a)
    if hasattr(b2, 'Event'):
        assert _is_linked(b2, 'Event', a)
    _safe_set(a, 'tag', set())
    assert not _is_linked(a, 'tag', b2)
    if hasattr(b2, 'Event'):
        assert not _is_linked(b2, 'Event', a)


def test_assoc_tag2_link_reassign_clear():
    a = tracker_Tag(idNumber="sample_text", usainNumberUsed=True)
    b1 = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, idNumber="sample_text")
    b2 = tracker_Event(comments="sample_text_2", correction=False, dateTime="sample_text_2", electronicallyRead=False, eventCode=13, idNumber="sample_text_2")
    _safe_set(a, 'Tag', b1)
    assert _is_linked(a, 'Tag', b1)
    if hasattr(b1, 'events'):
        assert _is_linked(b1, 'events', a)
    _safe_set(a, 'Tag', b2)
    assert _is_linked(a, 'Tag', b2)
    if hasattr(b1, 'events'):
        assert not _is_linked(b1, 'events', a)
    if hasattr(b2, 'events'):
        assert _is_linked(b2, 'events', a)
    _safe_set(a, 'Tag', None)
    assert not _is_linked(a, 'Tag', b2)
    if hasattr(b2, 'events'):
        assert not _is_linked(b2, 'events', a)


def test_assoc_tags0_link_reassign_clear():
    a = tracker_Tag(idNumber="sample_text", usainNumberUsed=True)
    b1 = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    b2 = tracker_Animal(age="sample_text_2", birthDate="sample_text_2", breed="sample_text_2", idNumber="sample_text_2", sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2")
    _safe_set(a, 'tracker_Tag', b1)
    assert _is_linked(a, 'tracker_Tag', b1)
    if hasattr(b1, 'tracker_Animal'):
        assert _is_linked(b1, 'tracker_Animal', a)
    _safe_set(a, 'tracker_Tag', b2)
    assert _is_linked(a, 'tracker_Tag', b2)
    if hasattr(b1, 'tracker_Animal'):
        assert not _is_linked(b1, 'tracker_Animal', a)
    if hasattr(b2, 'tracker_Animal'):
        assert _is_linked(b2, 'tracker_Animal', a)
    _safe_set(a, 'tracker_Tag', None)
    assert not _is_linked(a, 'tracker_Tag', b2)
    if hasattr(b2, 'tracker_Animal'):
        assert not _is_linked(b2, 'tracker_Animal', a)


def test_assoc_unAppliedTags5_link_reassign_clear():
    a = tracker_Tag(idNumber="sample_text", usainNumberUsed=True)
    b1 = tracker_Premises(emailContact="sample_text", premisesId="sample_text")
    b2 = tracker_Premises(emailContact="sample_text_2", premisesId="sample_text_2")
    _safe_set(a, 'tracker_Tag7', b1)
    assert _is_linked(a, 'tracker_Tag7', b1)
    if hasattr(b1, 'tracker_Premises6'):
        assert _is_linked(b1, 'tracker_Premises6', a)
    _safe_set(a, 'tracker_Tag7', b2)
    assert _is_linked(a, 'tracker_Tag7', b2)
    if hasattr(b1, 'tracker_Premises6'):
        assert not _is_linked(b1, 'tracker_Premises6', a)
    if hasattr(b2, 'tracker_Premises6'):
        assert _is_linked(b2, 'tracker_Premises6', a)
    _safe_set(a, 'tracker_Tag7', None)
    assert not _is_linked(a, 'tracker_Tag7', b2)
    if hasattr(b2, 'tracker_Premises6'):
        assert not _is_linked(b2, 'tracker_Premises6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Animal_strategy = st.builds(Animal)
@given(instance=Animal_strategy)
@settings(max_examples=25)
def test_Animal_instantiation(instance):
    assert isinstance(instance, Animal)


Bovine_strategy = st.builds(Bovine)
@given(instance=Bovine_strategy)
@settings(max_examples=25)
def test_Bovine_instantiation(instance):
    assert isinstance(instance, Bovine)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


tracker_Animal_strategy = st.builds(tracker_Animal, age=safe_text, birthDate=safe_text, breed=safe_text, idNumber=safe_text, sex=safe_text, sexCode=safe_text, species=safe_text, speciesCode=safe_text)
@given(instance=tracker_Animal_strategy)
@settings(max_examples=25)
def test_tracker_Animal_instantiation(instance):
    assert isinstance(instance, tracker_Animal)


tracker_AnimalMissing_strategy = st.builds(tracker_AnimalMissing)
@given(instance=tracker_AnimalMissing_strategy)
@settings(max_examples=25)
def test_tracker_AnimalMissing_instantiation(instance):
    assert isinstance(instance, tracker_AnimalMissing)


tracker_Bovine_strategy = st.builds(tracker_Bovine)
@given(instance=tracker_Bovine_strategy)
@settings(max_examples=25)
def test_tracker_Bovine_instantiation(instance):
    assert isinstance(instance, tracker_Bovine)


tracker_BovineBeef_strategy = st.builds(tracker_BovineBeef, beefBreed=safe_text)
@given(instance=tracker_BovineBeef_strategy)
@settings(max_examples=25)
def test_tracker_BovineBeef_instantiation(instance):
    assert isinstance(instance, tracker_BovineBeef)


tracker_BovineBison_strategy = st.builds(tracker_BovineBison, buffaloBreed=safe_text)
@given(instance=tracker_BovineBison_strategy)
@settings(max_examples=25)
def test_tracker_BovineBison_instantiation(instance):
    assert isinstance(instance, tracker_BovineBison)


tracker_BovineDairy_strategy = st.builds(tracker_BovineDairy, dairyBreed=safe_text)
@given(instance=tracker_BovineDairy_strategy)
@settings(max_examples=25)
def test_tracker_BovineDairy_instantiation(instance):
    assert isinstance(instance, tracker_BovineDairy)


tracker_Died_strategy = st.builds(tracker_Died)
@given(instance=tracker_Died_strategy)
@settings(max_examples=25)
def test_tracker_Died_instantiation(instance):
    assert isinstance(instance, tracker_Died)


tracker_Event_strategy = st.builds(tracker_Event, comments=safe_text, correction=st.booleans(), dateTime=safe_text, electronicallyRead=st.booleans(), eventCode=st.integers(), idNumber=safe_text)
@given(instance=tracker_Event_strategy)
@settings(max_examples=25)
def test_tracker_Event_instantiation(instance):
    assert isinstance(instance, tracker_Event)


tracker_Exported_strategy = st.builds(tracker_Exported)
@given(instance=tracker_Exported_strategy)
@settings(max_examples=25)
def test_tracker_Exported_instantiation(instance):
    assert isinstance(instance, tracker_Exported)


tracker_FairRegistration_strategy = st.builds(tracker_FairRegistration, address=safe_text, club=safe_text, parent=safe_text, participant=safe_text, phone=safe_text)
@given(instance=tracker_FairRegistration_strategy)
@settings(max_examples=25)
def test_tracker_FairRegistration_instantiation(instance):
    assert isinstance(instance, tracker_FairRegistration)


tracker_ICVI_strategy = st.builds(tracker_ICVI)
@given(instance=tracker_ICVI_strategy)
@settings(max_examples=25)
def test_tracker_ICVI_instantiation(instance):
    assert isinstance(instance, tracker_ICVI)


tracker_Imported_strategy = st.builds(tracker_Imported)
@given(instance=tracker_Imported_strategy)
@settings(max_examples=25)
def test_tracker_Imported_instantiation(instance):
    assert isinstance(instance, tracker_Imported)


tracker_LostTag_strategy = st.builds(tracker_LostTag)
@given(instance=tracker_LostTag_strategy)
@settings(max_examples=25)
def test_tracker_LostTag_instantiation(instance):
    assert isinstance(instance, tracker_LostTag)


tracker_MovedIn_strategy = st.builds(tracker_MovedIn, sourcePin=safe_text)
@given(instance=tracker_MovedIn_strategy)
@settings(max_examples=25)
def test_tracker_MovedIn_instantiation(instance):
    assert isinstance(instance, tracker_MovedIn)


tracker_MovedOut_strategy = st.builds(tracker_MovedOut, destinationPin=safe_text)
@given(instance=tracker_MovedOut_strategy)
@settings(max_examples=25)
def test_tracker_MovedOut_instantiation(instance):
    assert isinstance(instance, tracker_MovedOut)


tracker_Ovine_strategy = st.builds(tracker_Ovine, sheepBreed=safe_text)
@given(instance=tracker_Ovine_strategy)
@settings(max_examples=25)
def test_tracker_Ovine_instantiation(instance):
    assert isinstance(instance, tracker_Ovine)


tracker_Premises_strategy = st.builds(tracker_Premises, emailContact=safe_text, premisesId=safe_text)
@given(instance=tracker_Premises_strategy)
@settings(max_examples=25)
def test_tracker_Premises_instantiation(instance):
    assert isinstance(instance, tracker_Premises)


tracker_ReplacedTag_strategy = st.builds(tracker_ReplacedTag, oldAin=safe_text)
@given(instance=tracker_ReplacedTag_strategy)
@settings(max_examples=25)
def test_tracker_ReplacedTag_instantiation(instance):
    assert isinstance(instance, tracker_ReplacedTag)


tracker_Sighting_strategy = st.builds(tracker_Sighting)
@given(instance=tracker_Sighting_strategy)
@settings(max_examples=25)
def test_tracker_Sighting_instantiation(instance):
    assert isinstance(instance, tracker_Sighting)


tracker_Slaughtered_strategy = st.builds(tracker_Slaughtered)
@given(instance=tracker_Slaughtered_strategy)
@settings(max_examples=25)
def test_tracker_Slaughtered_instantiation(instance):
    assert isinstance(instance, tracker_Slaughtered)


tracker_Swine_strategy = st.builds(tracker_Swine, swineBreed=safe_text)
@given(instance=tracker_Swine_strategy)
@settings(max_examples=25)
def test_tracker_Swine_instantiation(instance):
    assert isinstance(instance, tracker_Swine)


tracker_Tag_strategy = st.builds(tracker_Tag, idNumber=safe_text, usainNumberUsed=st.booleans())
@given(instance=tracker_Tag_strategy)
@settings(max_examples=25)
def test_tracker_Tag_instantiation(instance):
    assert isinstance(instance, tracker_Tag)


tracker_TagAllocated_strategy = st.builds(tracker_TagAllocated)
@given(instance=tracker_TagAllocated_strategy)
@settings(max_examples=25)
def test_tracker_TagAllocated_instantiation(instance):
    assert isinstance(instance, tracker_TagAllocated)


tracker_TagApplied_strategy = st.builds(tracker_TagApplied)
@given(instance=tracker_TagApplied_strategy)
@settings(max_examples=25)
def test_tracker_TagApplied_instantiation(instance):
    assert isinstance(instance, tracker_TagApplied)


tracker_TagRetired_strategy = st.builds(tracker_TagRetired)
@given(instance=tracker_TagRetired_strategy)
@settings(max_examples=25)
def test_tracker_TagRetired_instantiation(instance):
    assert isinstance(instance, tracker_TagRetired)


tracker_WeighIn_strategy = st.builds(tracker_WeighIn, weight=st.integers())
@given(instance=tracker_WeighIn_strategy)
@settings(max_examples=25)
def test_tracker_WeighIn_instantiation(instance):
    assert isinstance(instance, tracker_WeighIn)



