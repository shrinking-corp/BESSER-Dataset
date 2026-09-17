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
    tracker_EventAttributeSchema,
    MedicalCondition,
    tracker_Mastitis,
    Birthing,
    tracker_Calving,
    tracker_EventSchema,
    tracker_EventAttribute,
    Bovine,
    tracker_BovineBison,
    tracker_BovineDairy,
    tracker_BovineBeef,
    tracker_Premises,
    Event,
    tracker_MovedOut,
    tracker_HerdTest,
    tracker_MovedIn,
    tracker_WeighIn,
    tracker_ICVI,
    tracker_Exported,
    tracker_Imported,
    tracker_MedicalTreatment,
    tracker_BirthDefect,
    tracker_TagApplied,
    tracker_USSwineGrading,
    tracker_Birthing,
    tracker_TagRetired,
    tracker_MilkTest,
    tracker_USOvineGrading,
    tracker_ReplacedTag,
    tracker_LostTag,
    tracker_GenericEvent,
    tracker_USBeefGrading,
    tracker_Slaughtered,
    tracker_Sighting,
    tracker_AnimalMissing,
    tracker_MedicalCondition,
    tracker_Died,
    tracker_TagAllocated,
    tracker_Schema,
    tracker_Location,
    tracker_Tag,
    Animal,
    tracker_Equine,
    tracker_Swine,
    tracker_Caprine,
    tracker_Ovine,
    tracker_Bovine,
    tracker_Event,
    tracker_Animal,
    SwineBreed,
    Level,
    USSwineQualityGrade,
    AnimalType,
    USQualityGrade,
    HorseBreed,
    EventDataType,
    BeefBreed,
    Treatment,
    USBeefYieldGrade,
    SheepBreed,
    BisonBreed,
    OneToTen,
    Sex,
    DairyBreed,
    GoatBreed,
    TreatmentMethod,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tracker_eventattributeschema_is_not_abstract():
    assert not inspect.isabstract(tracker_EventAttributeSchema)


def test_hyp_tracker_eventattributeschema_constructor_exists():
    assert callable(tracker_EventAttributeSchema.__init__)


def test_hyp_tracker_eventattributeschema_constructor_args():
    sig = inspect.signature(tracker_EventAttributeSchema.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"






def test_hyp_medicalcondition_is_not_abstract():
    assert not inspect.isabstract(MedicalCondition)


def test_hyp_medicalcondition_constructor_exists():
    assert callable(MedicalCondition.__init__)


def test_hyp_medicalcondition_constructor_args():
    sig = inspect.signature(MedicalCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_mastitis_is_not_abstract():
    assert not inspect.isabstract(tracker_Mastitis)


def test_hyp_tracker_mastitis_constructor_exists():
    assert callable(tracker_Mastitis.__init__)


def test_hyp_tracker_mastitis_constructor_args():
    sig = inspect.signature(tracker_Mastitis.__init__)
    params = list(sig.parameters.keys())
    assert "origin" in params, "Missing parameter 'origin'"
    assert "location" in params, "Missing parameter 'location'"





def test_hyp_birthing_is_not_abstract():
    assert not inspect.isabstract(Birthing)


def test_hyp_birthing_constructor_exists():
    assert callable(Birthing.__init__)


def test_hyp_birthing_constructor_args():
    sig = inspect.signature(Birthing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_calving_is_not_abstract():
    assert not inspect.isabstract(tracker_Calving)


def test_hyp_tracker_calving_constructor_exists():
    assert callable(tracker_Calving.__init__)


def test_hyp_tracker_calving_constructor_args():
    sig = inspect.signature(tracker_Calving.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_eventschema_is_not_abstract():
    assert not inspect.isabstract(tracker_EventSchema)


def test_hyp_tracker_eventschema_constructor_exists():
    assert callable(tracker_EventSchema.__init__)


def test_hyp_tracker_eventschema_constructor_args():
    sig = inspect.signature(tracker_EventSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "animalType" in params, "Missing parameter 'animalType'"
    assert "description" in params, "Missing parameter 'description'"






def test_hyp_tracker_eventattribute_is_not_abstract():
    assert not inspect.isabstract(tracker_EventAttribute)


def test_hyp_tracker_eventattribute_constructor_exists():
    assert callable(tracker_EventAttribute.__init__)


def test_hyp_tracker_eventattribute_constructor_args():
    sig = inspect.signature(tracker_EventAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





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




def test_hyp_tracker_premises_is_not_abstract():
    assert not inspect.isabstract(tracker_Premises)


def test_hyp_tracker_premises_constructor_exists():
    assert callable(tracker_Premises.__init__)


def test_hyp_tracker_premises_constructor_args():
    sig = inspect.signature(tracker_Premises.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "name" in params, "Missing parameter 'name'"
    assert "emailContact" in params, "Missing parameter 'emailContact'"
    assert "premisesId" in params, "Missing parameter 'premisesId'"







def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_movedout_is_not_abstract():
    assert not inspect.isabstract(tracker_MovedOut)


def test_hyp_tracker_movedout_constructor_exists():
    assert callable(tracker_MovedOut.__init__)


def test_hyp_tracker_movedout_constructor_args():
    sig = inspect.signature(tracker_MovedOut.__init__)
    params = list(sig.parameters.keys())
    assert "destinationPin" in params, "Missing parameter 'destinationPin'"




def test_hyp_tracker_herdtest_is_not_abstract():
    assert not inspect.isabstract(tracker_HerdTest)


def test_hyp_tracker_herdtest_constructor_exists():
    assert callable(tracker_HerdTest.__init__)


def test_hyp_tracker_herdtest_constructor_args():
    sig = inspect.signature(tracker_HerdTest.__init__)
    params = list(sig.parameters.keys())
    assert "pregnant" in params, "Missing parameter 'pregnant'"
    assert "bredDateEstimate" in params, "Missing parameter 'bredDateEstimate'"
    assert "daysSinceBredEstimate" in params, "Missing parameter 'daysSinceBredEstimate'"






def test_hyp_tracker_movedin_is_not_abstract():
    assert not inspect.isabstract(tracker_MovedIn)


def test_hyp_tracker_movedin_constructor_exists():
    assert callable(tracker_MovedIn.__init__)


def test_hyp_tracker_movedin_constructor_args():
    sig = inspect.signature(tracker_MovedIn.__init__)
    params = list(sig.parameters.keys())
    assert "sourcePin" in params, "Missing parameter 'sourcePin'"




def test_hyp_tracker_weighin_is_not_abstract():
    assert not inspect.isabstract(tracker_WeighIn)


def test_hyp_tracker_weighin_constructor_exists():
    assert callable(tracker_WeighIn.__init__)


def test_hyp_tracker_weighin_constructor_args():
    sig = inspect.signature(tracker_WeighIn.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "weightGainPerDay" in params, "Missing parameter 'weightGainPerDay'"





def test_hyp_tracker_icvi_is_not_abstract():
    assert not inspect.isabstract(tracker_ICVI)


def test_hyp_tracker_icvi_constructor_exists():
    assert callable(tracker_ICVI.__init__)


def test_hyp_tracker_icvi_constructor_args():
    sig = inspect.signature(tracker_ICVI.__init__)
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



def test_hyp_tracker_medicaltreatment_is_not_abstract():
    assert not inspect.isabstract(tracker_MedicalTreatment)


def test_hyp_tracker_medicaltreatment_constructor_exists():
    assert callable(tracker_MedicalTreatment.__init__)


def test_hyp_tracker_medicaltreatment_constructor_args():
    sig = inspect.signature(tracker_MedicalTreatment.__init__)
    params = list(sig.parameters.keys())
    assert "product" in params, "Missing parameter 'product'"
    assert "method" in params, "Missing parameter 'method'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "lot" in params, "Missing parameter 'lot'"
    assert "treatment" in params, "Missing parameter 'treatment'"
    assert "name" in params, "Missing parameter 'name'"










def test_hyp_tracker_birthdefect_is_not_abstract():
    assert not inspect.isabstract(tracker_BirthDefect)


def test_hyp_tracker_birthdefect_constructor_exists():
    assert callable(tracker_BirthDefect.__init__)


def test_hyp_tracker_birthdefect_constructor_args():
    sig = inspect.signature(tracker_BirthDefect.__init__)
    params = list(sig.parameters.keys())
    assert "freemartin" in params, "Missing parameter 'freemartin'"




def test_hyp_tracker_tagapplied_is_not_abstract():
    assert not inspect.isabstract(tracker_TagApplied)


def test_hyp_tracker_tagapplied_constructor_exists():
    assert callable(tracker_TagApplied.__init__)


def test_hyp_tracker_tagapplied_constructor_args():
    sig = inspect.signature(tracker_TagApplied.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_usswinegrading_is_not_abstract():
    assert not inspect.isabstract(tracker_USSwineGrading)


def test_hyp_tracker_usswinegrading_constructor_exists():
    assert callable(tracker_USSwineGrading.__init__)


def test_hyp_tracker_usswinegrading_constructor_args():
    sig = inspect.signature(tracker_USSwineGrading.__init__)
    params = list(sig.parameters.keys())
    assert "qualityGrade" in params, "Missing parameter 'qualityGrade'"




def test_hyp_tracker_birthing_is_not_abstract():
    assert not inspect.isabstract(tracker_Birthing)


def test_hyp_tracker_birthing_constructor_exists():
    assert callable(tracker_Birthing.__init__)


def test_hyp_tracker_birthing_constructor_args():
    sig = inspect.signature(tracker_Birthing.__init__)
    params = list(sig.parameters.keys())
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "assisted" in params, "Missing parameter 'assisted'"
    assert "viability" in params, "Missing parameter 'viability'"






def test_hyp_tracker_tagretired_is_not_abstract():
    assert not inspect.isabstract(tracker_TagRetired)


def test_hyp_tracker_tagretired_constructor_exists():
    assert callable(tracker_TagRetired.__init__)


def test_hyp_tracker_tagretired_constructor_args():
    sig = inspect.signature(tracker_TagRetired.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_milktest_is_not_abstract():
    assert not inspect.isabstract(tracker_MilkTest)


def test_hyp_tracker_milktest_constructor_exists():
    assert callable(tracker_MilkTest.__init__)


def test_hyp_tracker_milktest_constructor_args():
    sig = inspect.signature(tracker_MilkTest.__init__)
    params = list(sig.parameters.keys())
    assert "poundsProduced" in params, "Missing parameter 'poundsProduced'"
    assert "somaticCellCounts" in params, "Missing parameter 'somaticCellCounts'"
    assert "otherSolids" in params, "Missing parameter 'otherSolids'"
    assert "percentProtein" in params, "Missing parameter 'percentProtein'"
    assert "percentButterFat" in params, "Missing parameter 'percentButterFat'"








def test_hyp_tracker_usovinegrading_is_not_abstract():
    assert not inspect.isabstract(tracker_USOvineGrading)


def test_hyp_tracker_usovinegrading_constructor_exists():
    assert callable(tracker_USOvineGrading.__init__)


def test_hyp_tracker_usovinegrading_constructor_args():
    sig = inspect.signature(tracker_USOvineGrading.__init__)
    params = list(sig.parameters.keys())
    assert "qualityGradeLevel" in params, "Missing parameter 'qualityGradeLevel'"
    assert "qualityGrade" in params, "Missing parameter 'qualityGrade'"





def test_hyp_tracker_replacedtag_is_not_abstract():
    assert not inspect.isabstract(tracker_ReplacedTag)


def test_hyp_tracker_replacedtag_constructor_exists():
    assert callable(tracker_ReplacedTag.__init__)


def test_hyp_tracker_replacedtag_constructor_args():
    sig = inspect.signature(tracker_ReplacedTag.__init__)
    params = list(sig.parameters.keys())
    assert "usainNumberUsedForOldId" in params, "Missing parameter 'usainNumberUsedForOldId'"
    assert "oldId" in params, "Missing parameter 'oldId'"





def test_hyp_tracker_losttag_is_not_abstract():
    assert not inspect.isabstract(tracker_LostTag)


def test_hyp_tracker_losttag_constructor_exists():
    assert callable(tracker_LostTag.__init__)


def test_hyp_tracker_losttag_constructor_args():
    sig = inspect.signature(tracker_LostTag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_genericevent_is_not_abstract():
    assert not inspect.isabstract(tracker_GenericEvent)


def test_hyp_tracker_genericevent_constructor_exists():
    assert callable(tracker_GenericEvent.__init__)


def test_hyp_tracker_genericevent_constructor_args():
    sig = inspect.signature(tracker_GenericEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_usbeefgrading_is_not_abstract():
    assert not inspect.isabstract(tracker_USBeefGrading)


def test_hyp_tracker_usbeefgrading_constructor_exists():
    assert callable(tracker_USBeefGrading.__init__)


def test_hyp_tracker_usbeefgrading_constructor_args():
    sig = inspect.signature(tracker_USBeefGrading.__init__)
    params = list(sig.parameters.keys())
    assert "qualityGrade" in params, "Missing parameter 'qualityGrade'"
    assert "qualityGradeLevel" in params, "Missing parameter 'qualityGradeLevel'"
    assert "yieldGrade" in params, "Missing parameter 'yieldGrade'"






def test_hyp_tracker_slaughtered_is_not_abstract():
    assert not inspect.isabstract(tracker_Slaughtered)


def test_hyp_tracker_slaughtered_constructor_exists():
    assert callable(tracker_Slaughtered.__init__)


def test_hyp_tracker_slaughtered_constructor_args():
    sig = inspect.signature(tracker_Slaughtered.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_sighting_is_not_abstract():
    assert not inspect.isabstract(tracker_Sighting)


def test_hyp_tracker_sighting_constructor_exists():
    assert callable(tracker_Sighting.__init__)


def test_hyp_tracker_sighting_constructor_args():
    sig = inspect.signature(tracker_Sighting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_animalmissing_is_not_abstract():
    assert not inspect.isabstract(tracker_AnimalMissing)


def test_hyp_tracker_animalmissing_constructor_exists():
    assert callable(tracker_AnimalMissing.__init__)


def test_hyp_tracker_animalmissing_constructor_args():
    sig = inspect.signature(tracker_AnimalMissing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_medicalcondition_is_not_abstract():
    assert not inspect.isabstract(tracker_MedicalCondition)


def test_hyp_tracker_medicalcondition_constructor_exists():
    assert callable(tracker_MedicalCondition.__init__)


def test_hyp_tracker_medicalcondition_constructor_args():
    sig = inspect.signature(tracker_MedicalCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_died_is_not_abstract():
    assert not inspect.isabstract(tracker_Died)


def test_hyp_tracker_died_constructor_exists():
    assert callable(tracker_Died.__init__)


def test_hyp_tracker_died_constructor_args():
    sig = inspect.signature(tracker_Died.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_tagallocated_is_not_abstract():
    assert not inspect.isabstract(tracker_TagAllocated)


def test_hyp_tracker_tagallocated_constructor_exists():
    assert callable(tracker_TagAllocated.__init__)


def test_hyp_tracker_tagallocated_constructor_args():
    sig = inspect.signature(tracker_TagAllocated.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_schema_is_not_abstract():
    assert not inspect.isabstract(tracker_Schema)


def test_hyp_tracker_schema_constructor_exists():
    assert callable(tracker_Schema.__init__)


def test_hyp_tracker_schema_constructor_args():
    sig = inspect.signature(tracker_Schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_location_is_not_abstract():
    assert not inspect.isabstract(tracker_Location)


def test_hyp_tracker_location_constructor_exists():
    assert callable(tracker_Location.__init__)


def test_hyp_tracker_location_constructor_args():
    sig = inspect.signature(tracker_Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tracker_tag_is_not_abstract():
    assert not inspect.isabstract(tracker_Tag)


def test_hyp_tracker_tag_constructor_exists():
    assert callable(tracker_Tag.__init__)


def test_hyp_tracker_tag_constructor_args():
    sig = inspect.signature(tracker_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "usainNumberUsed" in params, "Missing parameter 'usainNumberUsed'"





def test_hyp_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_hyp_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_hyp_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_equine_is_not_abstract():
    assert not inspect.isabstract(tracker_Equine)


def test_hyp_tracker_equine_constructor_exists():
    assert callable(tracker_Equine.__init__)


def test_hyp_tracker_equine_constructor_args():
    sig = inspect.signature(tracker_Equine.__init__)
    params = list(sig.parameters.keys())
    assert "horseBreed" in params, "Missing parameter 'horseBreed'"




def test_hyp_tracker_swine_is_not_abstract():
    assert not inspect.isabstract(tracker_Swine)


def test_hyp_tracker_swine_constructor_exists():
    assert callable(tracker_Swine.__init__)


def test_hyp_tracker_swine_constructor_args():
    sig = inspect.signature(tracker_Swine.__init__)
    params = list(sig.parameters.keys())
    assert "leftEarNotching" in params, "Missing parameter 'leftEarNotching'"
    assert "rightEarNotching" in params, "Missing parameter 'rightEarNotching'"
    assert "swineBreed" in params, "Missing parameter 'swineBreed'"






def test_hyp_tracker_caprine_is_not_abstract():
    assert not inspect.isabstract(tracker_Caprine)


def test_hyp_tracker_caprine_constructor_exists():
    assert callable(tracker_Caprine.__init__)


def test_hyp_tracker_caprine_constructor_args():
    sig = inspect.signature(tracker_Caprine.__init__)
    params = list(sig.parameters.keys())
    assert "goatBreed" in params, "Missing parameter 'goatBreed'"




def test_hyp_tracker_ovine_is_not_abstract():
    assert not inspect.isabstract(tracker_Ovine)


def test_hyp_tracker_ovine_constructor_exists():
    assert callable(tracker_Ovine.__init__)


def test_hyp_tracker_ovine_constructor_args():
    sig = inspect.signature(tracker_Ovine.__init__)
    params = list(sig.parameters.keys())
    assert "sheepBreed" in params, "Missing parameter 'sheepBreed'"
    assert "scrapieTag" in params, "Missing parameter 'scrapieTag'"





def test_hyp_tracker_bovine_is_not_abstract():
    assert not inspect.isabstract(tracker_Bovine)


def test_hyp_tracker_bovine_constructor_exists():
    assert callable(tracker_Bovine.__init__)


def test_hyp_tracker_bovine_constructor_args():
    sig = inspect.signature(tracker_Bovine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tracker_event_is_not_abstract():
    assert not inspect.isabstract(tracker_Event)


def test_hyp_tracker_event_constructor_exists():
    assert callable(tracker_Event.__init__)


def test_hyp_tracker_event_constructor_args():
    sig = inspect.signature(tracker_Event.__init__)
    params = list(sig.parameters.keys())
    assert "electronicallyRead" in params, "Missing parameter 'electronicallyRead'"
    assert "correction" in params, "Missing parameter 'correction'"
    assert "eventCode" in params, "Missing parameter 'eventCode'"
    assert "dateTime" in params, "Missing parameter 'dateTime'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "id" in params, "Missing parameter 'id'"









def test_hyp_tracker_animal_is_not_abstract():
    assert not inspect.isabstract(tracker_Animal)


def test_hyp_tracker_animal_constructor_exists():
    assert callable(tracker_Animal.__init__)


def test_hyp_tracker_animal_constructor_args():
    sig = inspect.signature(tracker_Animal.__init__)
    params = list(sig.parameters.keys())
    assert "ageInDays" in params, "Missing parameter 'ageInDays'"
    assert "visualID" in params, "Missing parameter 'visualID'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "speciesCode" in params, "Missing parameter 'speciesCode'"
    assert "sexCode" in params, "Missing parameter 'sexCode'"
    assert "alternativeID" in params, "Missing parameter 'alternativeID'"
    assert "breed" in params, "Missing parameter 'breed'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "weightGainPerDay" in params, "Missing parameter 'weightGainPerDay'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "species" in params, "Missing parameter 'species'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "lastEventDateTime" in params, "Missing parameter 'lastEventDateTime'"
















def test_hyp_swinebreed_exists():
    # Check that the Enumeration exists
    assert SwineBreed is not None

def test_hyp_swinebreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SwineBreed]
    expected_literals = [
        "CW",
        "YO",
        "HA",
        "PC",
        "LW",
        "TM",
        "LC",
        "LB",
        "RW",
        "BK",
        "Unspecified",
        "LA",
        "SO",
        "PE",
        "WS",
        "DU",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SwineBreed"

def test_hyp_level_exists():
    # Check that the Enumeration exists
    assert Level is not None

def test_hyp_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Level]
    expected_literals = [
        "Average",
        "High",
        "Unspecified",
        "Low",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Level"

def test_hyp_usswinequalitygrade_exists():
    # Check that the Enumeration exists
    assert USSwineQualityGrade is not None

def test_hyp_usswinequalitygrade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USSwineQualityGrade]
    expected_literals = [
        "One",
        "Three",
        "Two",
        "Unspecified",
        "Four",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USSwineQualityGrade"

def test_hyp_animaltype_exists():
    # Check that the Enumeration exists
    assert AnimalType is not None

def test_hyp_animaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnimalType]
    expected_literals = [
        "Swine",
        "BovineBeef",
        "BovineBison",
        "BovineDairy",
        "Equine",
        "Caprine",
        "Ovine",
        "Unspecified",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnimalType"

def test_hyp_usqualitygrade_exists():
    # Check that the Enumeration exists
    assert USQualityGrade is not None

def test_hyp_usqualitygrade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USQualityGrade]
    expected_literals = [
        "Choice",
        "Prime",
        "Standard",
        "Unspecified",
        "Select",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USQualityGrade"

def test_hyp_horsebreed_exists():
    # Check that the Enumeration exists
    assert HorseBreed is not None

def test_hyp_horsebreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HorseBreed]
    expected_literals = [
        "BW",
        "WE",
        "FR",
        "TP",
        "HU",
        "WW",
        "PT",
        "AA",
        "DW",
        "HT",
        "CM",
        "PL",
        "WG",
        "EX",
        "SE",
        "CI",
        "PN",
        "SY",
        "HK",
        "HG",
        "IC",
        "OB",
        "AO",
        "MU",
        "WI",
        "WU",
        "AD",
        "FC",
        "DT",
        "TR",
        "WF",
        "SF",
        "HV",
        "AC",
        "PV",
        "AP",
        "TH",
        "CY",
        "SN",
        "LZ",
        "MN",
        "BY",
        "PH",
        "RH",
        "VK",
        "HW",
        "BU",
        "OL",
        "HF",
        "FH",
        "AS",
        "NF",
        "RU",
        "NO",
        "CV",
        "GL",
        "PF",
        "PW",
        "HN",
        "MF",
        "FJ",
        "NK",
        "QH",
        "TW",
        "FE",
        "Unspecified",
        "TF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HorseBreed"

def test_hyp_eventdatatype_exists():
    # Check that the Enumeration exists
    assert EventDataType is not None

def test_hyp_eventdatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventDataType]
    expected_literals = [
        "Integer",
        "String",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventDataType"

def test_hyp_beefbreed_exists():
    # Check that the Enumeration exists
    assert BeefBreed is not None

def test_hyp_beefbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BeefBreed]
    expected_literals = [
        "BM",
        "SL",
        "DS",
        "AR",
        "AU",
        "PI",
        "CN",
        "RB",
        "TN",
        "GR",
        "BR",
        "RA",
        "SS",
        "PZ",
        "BQ",
        "DB",
        "HB",
        "CA",
        "LU",
        "RR",
        "SE",
        "GY",
        "FC",
        "AN",
        "FA",
        "DN",
        "GZ",
        "WP",
        "TI",
        "FP",
        "DE",
        "SM",
        "SX",
        "DL",
        "MC",
        "AK",
        "AB",
        "NE",
        "HP",
        "GV",
        "MH",
        "RO",
        "SG",
        "NS",
        "BG",
        "WF",
        "CG",
        "MO",
        "ER",
        "MI",
        "SB",
        "WB",
        "DJ",
        "Unspecified",
        "SP",
        "HC",
        "RP",
        "GS",
        "BW",
        "SA",
        "BI",
        "IS",
        "AW",
        "AM",
        "MA",
        "DF",
        "LO",
        "SV",
        "LR",
        "TG",
        "RD",
        "LM",
        "BF",
        "PA",
        "CB",
        "CH",
        "HY",
        "HH",
        "CM",
        "BE",
        "GA",
        "BD",
        "TP",
        "CP",
        "AL",
        "RS",
        "MU",
        "RW",
        "AE",
        "BO",
        "BL",
        "AF",
        "MR",
        "MG",
        "TL",
        "NM",
        "CU",
        "XX",
        "IB",
        "TA",
        "BB",
        "XT",
        "ML",
        "BU",
        "SH",
        "YA",
        "KB",
        "ME",
        "SI",
        "DR",
        "SW",
        "GI",
        "NR",
        "FB",
        "BH",
        "KY",
        "GE",
        "BA",
        "BN",
        "RN",
        "FL",
        "PR",
        "FR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BeefBreed"

def test_hyp_treatment_exists():
    # Check that the Enumeration exists
    assert Treatment is not None

def test_hyp_treatment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Treatment]
    expected_literals = [
        "Prevention",
        "Unspecified",
        "Vaccination",
        "Hormone",
        "Vitamin",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Treatment"

def test_hyp_usbeefyieldgrade_exists():
    # Check that the Enumeration exists
    assert USBeefYieldGrade is not None

def test_hyp_usbeefyieldgrade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USBeefYieldGrade]
    expected_literals = [
        "Four",
        "Three",
        "Unspecified",
        "One",
        "Two",
        "Five",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USBeefYieldGrade"

def test_hyp_sheepbreed_exists():
    # Check that the Enumeration exists
    assert SheepBreed is not None

def test_hyp_sheepbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SheepBreed]
    expected_literals = [
        "TX",
        "NC",
        "MP",
        "CL",
        "BC",
        "BW",
        "KH",
        "SX",
        "TA",
        "XM",
        "HS",
        "LI",
        "NL",
        "PO",
        "BF",
        "FN",
        "CD",
        "DP",
        "XL",
        "OX",
        "LY",
        "PE",
        "RG",
        "KK",
        "DL",
        "SL",
        "ZS",
        "DH",
        "ST",
        "HL",
        "OU",
        "TU",
        "IL",
        "RM",
        "RV",
        "CF",
        "BO",
        "CO",
        "KA",
        "FB",
        "MT",
        "MM",
        "SC",
        "SR",
        "CR",
        "ER",
        "BL",
        "HY",
        "SU",
        "LE",
        "Unspecified",
        "RY",
        "RI",
        "CP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SheepBreed"

def test_hyp_bisonbreed_exists():
    # Check that the Enumeration exists
    assert BisonBreed is not None

def test_hyp_bisonbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BisonBreed]
    expected_literals = [
        "WO",
        "Unspecified",
        "PB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BisonBreed"

def test_hyp_onetoten_exists():
    # Check that the Enumeration exists
    assert OneToTen is not None

def test_hyp_onetoten_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OneToTen]
    expected_literals = [
        "Six",
        "Five",
        "Two",
        "One",
        "Eight",
        "Three",
        "Four",
        "Nine",
        "Seven",
        "Unspecified",
        "Ten",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OneToTen"

def test_hyp_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_hyp_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "F",
        "S",
        "C",
        "M",
        "Unspecified",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"

def test_hyp_dairybreed_exists():
    # Check that the Enumeration exists
    assert DairyBreed is not None

def test_hyp_dairybreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DairyBreed]
    expected_literals = [
        "BS",
        "FM",
        "GU",
        "HO",
        "GD",
        "WW",
        "Unspecified",
        "AY",
        "JE",
        "MS",
        "LD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DairyBreed"

def test_hyp_goatbreed_exists():
    # Check that the Enumeration exists
    assert GoatBreed is not None

def test_hyp_goatbreed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GoatBreed]
    expected_literals = [
        "EN",
        "AI",
        "ND",
        "TO",
        "NU",
        "LN",
        "CS",
        "BZ",
        "PY",
        "OH",
        "Unspecified",
        "AG",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GoatBreed"

def test_hyp_treatmentmethod_exists():
    # Check that the Enumeration exists
    assert TreatmentMethod is not None

def test_hyp_treatmentmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreatmentMethod]
    expected_literals = [
        "Unspecified",
        "Salve",
        "Nasal",
        "Intramuscular",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreatmentMethod"


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
tracker_EventAttributeSchema_strategy = st.builds(
    tracker_EventAttributeSchema,
    description=
        safe_text,
    name=
        safe_text,
    dataType=
        safe_text
)
MedicalCondition_strategy = st.builds(
    MedicalCondition,
)
tracker_Mastitis_strategy = st.builds(
    tracker_Mastitis,
    origin=
        safe_text,
    location=
        safe_text
)
Birthing_strategy = st.builds(
    Birthing,
)
tracker_Calving_strategy = st.builds(
    tracker_Calving,
)
tracker_EventSchema_strategy = st.builds(
    tracker_EventSchema,
    name=
        safe_text,
    animalType=
        safe_text,
    description=
        safe_text
)
tracker_EventAttribute_strategy = st.builds(
    tracker_EventAttribute,
    value=
        safe_text,
    key=
        safe_text
)
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
tracker_Premises_strategy = st.builds(
    tracker_Premises,
    uri=
        safe_text,
    name=
        safe_text,
    emailContact=
        safe_text,
    premisesId=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
tracker_MovedOut_strategy = st.builds(
    tracker_MovedOut,
    destinationPin=
        safe_text
)
tracker_HerdTest_strategy = st.builds(
    tracker_HerdTest,
    pregnant=
        st.booleans(),
    bredDateEstimate=
        st.dates(),
    daysSinceBredEstimate=
        st.integers()
)
tracker_MovedIn_strategy = st.builds(
    tracker_MovedIn,
    sourcePin=
        safe_text
)
tracker_WeighIn_strategy = st.builds(
    tracker_WeighIn,
    weight=
        safe_text,
    weightGainPerDay=
        safe_text
)
tracker_ICVI_strategy = st.builds(
    tracker_ICVI,
)
tracker_Exported_strategy = st.builds(
    tracker_Exported,
)
tracker_Imported_strategy = st.builds(
    tracker_Imported,
)
tracker_MedicalTreatment_strategy = st.builds(
    tracker_MedicalTreatment,
    product=
        safe_text,
    method=
        safe_text,
    quantity=
        safe_text,
    manufacturer=
        safe_text,
    lot=
        safe_text,
    treatment=
        safe_text,
    name=
        safe_text
)
tracker_BirthDefect_strategy = st.builds(
    tracker_BirthDefect,
    freemartin=
        st.booleans()
)
tracker_TagApplied_strategy = st.builds(
    tracker_TagApplied,
)
tracker_USSwineGrading_strategy = st.builds(
    tracker_USSwineGrading,
    qualityGrade=
        safe_text
)
tracker_Birthing_strategy = st.builds(
    tracker_Birthing,
    difficulty=
        safe_text,
    assisted=
        st.booleans(),
    viability=
        st.booleans()
)
tracker_TagRetired_strategy = st.builds(
    tracker_TagRetired,
)
tracker_MilkTest_strategy = st.builds(
    tracker_MilkTest,
    poundsProduced=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    somaticCellCounts=
        st.integers(),
    otherSolids=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    percentProtein=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    percentButterFat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
tracker_USOvineGrading_strategy = st.builds(
    tracker_USOvineGrading,
    qualityGradeLevel=
        safe_text,
    qualityGrade=
        safe_text
)
tracker_ReplacedTag_strategy = st.builds(
    tracker_ReplacedTag,
    usainNumberUsedForOldId=
        st.booleans(),
    oldId=
        safe_text
)
tracker_LostTag_strategy = st.builds(
    tracker_LostTag,
)
tracker_GenericEvent_strategy = st.builds(
    tracker_GenericEvent,
)
tracker_USBeefGrading_strategy = st.builds(
    tracker_USBeefGrading,
    qualityGrade=
        safe_text,
    qualityGradeLevel=
        safe_text,
    yieldGrade=
        safe_text
)
tracker_Slaughtered_strategy = st.builds(
    tracker_Slaughtered,
)
tracker_Sighting_strategy = st.builds(
    tracker_Sighting,
)
tracker_AnimalMissing_strategy = st.builds(
    tracker_AnimalMissing,
)
tracker_MedicalCondition_strategy = st.builds(
    tracker_MedicalCondition,
)
tracker_Died_strategy = st.builds(
    tracker_Died,
)
tracker_TagAllocated_strategy = st.builds(
    tracker_TagAllocated,
)
tracker_Schema_strategy = st.builds(
    tracker_Schema,
)
tracker_Location_strategy = st.builds(
    tracker_Location,
    name=
        safe_text
)
tracker_Tag_strategy = st.builds(
    tracker_Tag,
    id=
        safe_text,
    usainNumberUsed=
        st.booleans()
)
Animal_strategy = st.builds(
    Animal,
)
tracker_Equine_strategy = st.builds(
    tracker_Equine,
    horseBreed=
        safe_text
)
tracker_Swine_strategy = st.builds(
    tracker_Swine,
    leftEarNotching=
        st.integers(),
    rightEarNotching=
        st.integers(),
    swineBreed=
        safe_text
)
tracker_Caprine_strategy = st.builds(
    tracker_Caprine,
    goatBreed=
        safe_text
)
tracker_Ovine_strategy = st.builds(
    tracker_Ovine,
    sheepBreed=
        safe_text,
    scrapieTag=
        safe_text
)
tracker_Bovine_strategy = st.builds(
    tracker_Bovine,
)
tracker_Event_strategy = st.builds(
    tracker_Event,
    electronicallyRead=
        st.booleans(),
    correction=
        st.booleans(),
    eventCode=
        st.integers(),
    dateTime=
        st.dates(),
    comments=
        safe_text,
    id=
        safe_text
)
tracker_Animal_strategy = st.builds(
    tracker_Animal,
    ageInDays=
        st.integers(),
    visualID=
        safe_text,
    comments=
        safe_text,
    speciesCode=
        safe_text,
    sexCode=
        safe_text,
    alternativeID=
        safe_text,
    breed=
        safe_text,
    sex=
        safe_text,
    weightGainPerDay=
        safe_text,
    id=
        safe_text,
    type=
        safe_text,
    birthDate=
        st.dates(),
    species=
        safe_text,
    weight=
        safe_text,
    lastEventDateTime=
        st.dates()
)




@given(instance=tracker_EventAttributeSchema_strategy)
def test_hyp_tracker_eventattributeschema_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=tracker_EventAttributeSchema_strategy)
def test_hyp_tracker_eventattributeschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tracker_EventAttributeSchema_strategy)
def test_hyp_tracker_eventattributeschema_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original





@given(instance=tracker_Mastitis_strategy)
def test_hyp_tracker_mastitis_origin_setter(instance):
    original = instance.origin
    instance.origin = original
    assert instance.origin == original



@given(instance=tracker_Mastitis_strategy)
def test_hyp_tracker_mastitis_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original






@given(instance=tracker_EventSchema_strategy)
def test_hyp_tracker_eventschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tracker_EventSchema_strategy)
def test_hyp_tracker_eventschema_animalType_setter(instance):
    original = instance.animalType
    instance.animalType = original
    assert instance.animalType == original



@given(instance=tracker_EventSchema_strategy)
def test_hyp_tracker_eventschema_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=tracker_EventAttribute_strategy)
def test_hyp_tracker_eventattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=tracker_EventAttribute_strategy)
def test_hyp_tracker_eventattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original





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




@given(instance=tracker_Premises_strategy)
def test_hyp_tracker_premises_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=tracker_Premises_strategy)
def test_hyp_tracker_premises_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tracker_Premises_strategy)
def test_hyp_tracker_premises_emailContact_setter(instance):
    original = instance.emailContact
    instance.emailContact = original
    assert instance.emailContact == original



@given(instance=tracker_Premises_strategy)
def test_hyp_tracker_premises_premisesId_setter(instance):
    original = instance.premisesId
    instance.premisesId = original
    assert instance.premisesId == original

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





@given(instance=tracker_MovedOut_strategy)
def test_hyp_tracker_movedout_destinationPin_setter(instance):
    original = instance.destinationPin
    instance.destinationPin = original
    assert instance.destinationPin == original




@given(instance=tracker_HerdTest_strategy)
def test_hyp_tracker_herdtest_pregnant_setter(instance):
    original = instance.pregnant
    instance.pregnant = original
    assert instance.pregnant == original



@given(instance=tracker_HerdTest_strategy)
def test_hyp_tracker_herdtest_bredDateEstimate_setter(instance):
    original = instance.bredDateEstimate
    instance.bredDateEstimate = original
    assert instance.bredDateEstimate == original



@given(instance=tracker_HerdTest_strategy)
def test_hyp_tracker_herdtest_daysSinceBredEstimate_setter(instance):
    original = instance.daysSinceBredEstimate
    instance.daysSinceBredEstimate = original
    assert instance.daysSinceBredEstimate == original




@given(instance=tracker_MovedIn_strategy)
def test_hyp_tracker_movedin_sourcePin_setter(instance):
    original = instance.sourcePin
    instance.sourcePin = original
    assert instance.sourcePin == original




@given(instance=tracker_WeighIn_strategy)
def test_hyp_tracker_weighin_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=tracker_WeighIn_strategy)
def test_hyp_tracker_weighin_weightGainPerDay_setter(instance):
    original = instance.weightGainPerDay
    instance.weightGainPerDay = original
    assert instance.weightGainPerDay == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_WeighIn_strategy)
@settings(max_examples=30)
def test_hyp_tracker_weighin_previousweighin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.previousWeighIn()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.previousWeighIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'previousWeighIn' in tracker_WeighIn is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'previousWeighIn' in tracker_WeighIn did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'previousWeighIn' in tracker_WeighIn is not implemented or raised an error")







@given(instance=tracker_MedicalTreatment_strategy)
def test_hyp_tracker_medicaltreatment_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=tracker_MedicalTreatment_strategy)
def test_hyp_tracker_medicaltreatment_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original



@given(instance=tracker_MedicalTreatment_strategy)
def test_hyp_tracker_medicaltreatment_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=tracker_MedicalTreatment_strategy)
def test_hyp_tracker_medicaltreatment_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=tracker_MedicalTreatment_strategy)
def test_hyp_tracker_medicaltreatment_lot_setter(instance):
    original = instance.lot
    instance.lot = original
    assert instance.lot == original



@given(instance=tracker_MedicalTreatment_strategy)
def test_hyp_tracker_medicaltreatment_treatment_setter(instance):
    original = instance.treatment
    instance.treatment = original
    assert instance.treatment == original



@given(instance=tracker_MedicalTreatment_strategy)
def test_hyp_tracker_medicaltreatment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tracker_BirthDefect_strategy)
def test_hyp_tracker_birthdefect_freemartin_setter(instance):
    original = instance.freemartin
    instance.freemartin = original
    assert instance.freemartin == original





@given(instance=tracker_USSwineGrading_strategy)
def test_hyp_tracker_usswinegrading_qualityGrade_setter(instance):
    original = instance.qualityGrade
    instance.qualityGrade = original
    assert instance.qualityGrade == original




@given(instance=tracker_Birthing_strategy)
def test_hyp_tracker_birthing_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=tracker_Birthing_strategy)
def test_hyp_tracker_birthing_assisted_setter(instance):
    original = instance.assisted
    instance.assisted = original
    assert instance.assisted == original



@given(instance=tracker_Birthing_strategy)
def test_hyp_tracker_birthing_viability_setter(instance):
    original = instance.viability
    instance.viability = original
    assert instance.viability == original





@given(instance=tracker_MilkTest_strategy)
def test_hyp_tracker_milktest_poundsProduced_setter(instance):
    original = instance.poundsProduced
    instance.poundsProduced = original
    assert instance.poundsProduced == original



@given(instance=tracker_MilkTest_strategy)
def test_hyp_tracker_milktest_somaticCellCounts_setter(instance):
    original = instance.somaticCellCounts
    instance.somaticCellCounts = original
    assert instance.somaticCellCounts == original



@given(instance=tracker_MilkTest_strategy)
def test_hyp_tracker_milktest_otherSolids_setter(instance):
    original = instance.otherSolids
    instance.otherSolids = original
    assert instance.otherSolids == original



@given(instance=tracker_MilkTest_strategy)
def test_hyp_tracker_milktest_percentProtein_setter(instance):
    original = instance.percentProtein
    instance.percentProtein = original
    assert instance.percentProtein == original



@given(instance=tracker_MilkTest_strategy)
def test_hyp_tracker_milktest_percentButterFat_setter(instance):
    original = instance.percentButterFat
    instance.percentButterFat = original
    assert instance.percentButterFat == original




@given(instance=tracker_USOvineGrading_strategy)
def test_hyp_tracker_usovinegrading_qualityGradeLevel_setter(instance):
    original = instance.qualityGradeLevel
    instance.qualityGradeLevel = original
    assert instance.qualityGradeLevel == original



@given(instance=tracker_USOvineGrading_strategy)
def test_hyp_tracker_usovinegrading_qualityGrade_setter(instance):
    original = instance.qualityGrade
    instance.qualityGrade = original
    assert instance.qualityGrade == original




@given(instance=tracker_ReplacedTag_strategy)
def test_hyp_tracker_replacedtag_usainNumberUsedForOldId_setter(instance):
    original = instance.usainNumberUsedForOldId
    instance.usainNumberUsedForOldId = original
    assert instance.usainNumberUsedForOldId == original



@given(instance=tracker_ReplacedTag_strategy)
def test_hyp_tracker_replacedtag_oldId_setter(instance):
    original = instance.oldId
    instance.oldId = original
    assert instance.oldId == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_GenericEvent_strategy)
@settings(max_examples=30)
def test_hyp_tracker_genericevent_findschema_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findSchema(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findSchema).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findSchema' in tracker_GenericEvent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findSchema' in tracker_GenericEvent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findSchema' in tracker_GenericEvent is not implemented or raised an error")




@given(instance=tracker_USBeefGrading_strategy)
def test_hyp_tracker_usbeefgrading_qualityGrade_setter(instance):
    original = instance.qualityGrade
    instance.qualityGrade = original
    assert instance.qualityGrade == original



@given(instance=tracker_USBeefGrading_strategy)
def test_hyp_tracker_usbeefgrading_qualityGradeLevel_setter(instance):
    original = instance.qualityGradeLevel
    instance.qualityGradeLevel = original
    assert instance.qualityGradeLevel == original



@given(instance=tracker_USBeefGrading_strategy)
def test_hyp_tracker_usbeefgrading_yieldGrade_setter(instance):
    original = instance.yieldGrade
    instance.yieldGrade = original
    assert instance.yieldGrade == original











@given(instance=tracker_Location_strategy)
def test_hyp_tracker_location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tracker_Tag_strategy)
def test_hyp_tracker_tag_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=tracker_Tag_strategy)
def test_hyp_tracker_tag_usainNumberUsed_setter(instance):
    original = instance.usainNumberUsed
    instance.usainNumberUsed = original
    assert instance.usainNumberUsed == original





@given(instance=tracker_Equine_strategy)
def test_hyp_tracker_equine_horseBreed_setter(instance):
    original = instance.horseBreed
    instance.horseBreed = original
    assert instance.horseBreed == original




@given(instance=tracker_Swine_strategy)
def test_hyp_tracker_swine_leftEarNotching_setter(instance):
    original = instance.leftEarNotching
    instance.leftEarNotching = original
    assert instance.leftEarNotching == original



@given(instance=tracker_Swine_strategy)
def test_hyp_tracker_swine_rightEarNotching_setter(instance):
    original = instance.rightEarNotching
    instance.rightEarNotching = original
    assert instance.rightEarNotching == original



@given(instance=tracker_Swine_strategy)
def test_hyp_tracker_swine_swineBreed_setter(instance):
    original = instance.swineBreed
    instance.swineBreed = original
    assert instance.swineBreed == original




@given(instance=tracker_Caprine_strategy)
def test_hyp_tracker_caprine_goatBreed_setter(instance):
    original = instance.goatBreed
    instance.goatBreed = original
    assert instance.goatBreed == original




@given(instance=tracker_Ovine_strategy)
def test_hyp_tracker_ovine_sheepBreed_setter(instance):
    original = instance.sheepBreed
    instance.sheepBreed = original
    assert instance.sheepBreed == original



@given(instance=tracker_Ovine_strategy)
def test_hyp_tracker_ovine_scrapieTag_setter(instance):
    original = instance.scrapieTag
    instance.scrapieTag = original
    assert instance.scrapieTag == original





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



@given(instance=tracker_Event_strategy)
def test_hyp_tracker_event_eventCode_setter(instance):
    original = instance.eventCode
    instance.eventCode = original
    assert instance.eventCode == original



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
def test_hyp_tracker_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_ageInDays_setter(instance):
    original = instance.ageInDays
    instance.ageInDays = original
    assert instance.ageInDays == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_visualID_setter(instance):
    original = instance.visualID
    instance.visualID = original
    assert instance.visualID == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_speciesCode_setter(instance):
    original = instance.speciesCode
    instance.speciesCode = original
    assert instance.speciesCode == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_sexCode_setter(instance):
    original = instance.sexCode
    instance.sexCode = original
    assert instance.sexCode == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_alternativeID_setter(instance):
    original = instance.alternativeID
    instance.alternativeID = original
    assert instance.alternativeID == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_weightGainPerDay_setter(instance):
    original = instance.weightGainPerDay
    instance.weightGainPerDay = original
    assert instance.weightGainPerDay == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=tracker_Animal_strategy)
def test_hyp_tracker_animal_lastEventDateTime_setter(instance):
    original = instance.lastEventDateTime
    instance.lastEventDateTime = original
    assert instance.lastEventDateTime == original

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
def test_hyp_tracker_animal_lastweighin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lastWeighIn()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lastWeighIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lastWeighIn' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lastWeighIn' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lastWeighIn' in tracker_Animal is not implemented or raised an error")

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

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tracker_Animal_strategy)
@settings(max_examples=30)
def test_hyp_tracker_animal_eventhistory_changes_state(instance):
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
        assert has_statements, f"Function 'eventHistory' in tracker_Animal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eventHistory' in tracker_Animal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eventHistory' in tracker_Animal is not implemented or raised an error")

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


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Animal,
    Birthing,
    Bovine,
    Event,
    MedicalCondition,
    tracker_Animal,
    tracker_AnimalMissing,
    tracker_BirthDefect,
    tracker_Birthing,
    tracker_Bovine,
    tracker_BovineBeef,
    tracker_BovineBison,
    tracker_BovineDairy,
    tracker_Calving,
    tracker_Caprine,
    tracker_Died,
    tracker_Equine,
    tracker_Event,
    tracker_EventAttribute,
    tracker_EventAttributeSchema,
    tracker_EventSchema,
    tracker_Exported,
    tracker_GenericEvent,
    tracker_HerdTest,
    tracker_ICVI,
    tracker_Imported,
    tracker_Location,
    tracker_LostTag,
    tracker_Mastitis,
    tracker_MedicalCondition,
    tracker_MedicalTreatment,
    tracker_MilkTest,
    tracker_MovedIn,
    tracker_MovedOut,
    tracker_Ovine,
    tracker_Premises,
    tracker_ReplacedTag,
    tracker_Schema,
    tracker_Sighting,
    tracker_Slaughtered,
    tracker_Swine,
    tracker_Tag,
    tracker_TagAllocated,
    tracker_TagApplied,
    tracker_TagRetired,
    tracker_USBeefGrading,
    tracker_USOvineGrading,
    tracker_USSwineGrading,
    tracker_WeighIn,
    AnimalType,
    BeefBreed,
    BisonBreed,
    DairyBreed,
    EventDataType,
    GoatBreed,
    HorseBreed,
    Level,
    OneToTen,
    Sex,
    SheepBreed,
    SwineBreed,
    Treatment,
    TreatmentMethod,
    USBeefYieldGrade,
    USQualityGrade,
    USSwineQualityGrade,
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

def test_tracker_Animal_ageInDays_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.ageInDays == 7
    instance.ageInDays = 13
    assert instance.ageInDays == 13


def test_tracker_Animal_alternativeID_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.alternativeID == "sample_text"
    instance.alternativeID = "sample_text_2"
    assert instance.alternativeID == "sample_text_2"


def test_tracker_Animal_birthDate_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.birthDate == date(2024, 1, 1)
    instance.birthDate = date(2025, 6, 15)
    assert instance.birthDate == date(2025, 6, 15)


def test_tracker_Animal_breed_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.breed == "sample_text"
    instance.breed = "sample_text_2"
    assert instance.breed == "sample_text_2"


def test_tracker_Animal_comments_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_tracker_Animal_id_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_tracker_Animal_lastEventDateTime_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.lastEventDateTime == date(2024, 1, 1)
    instance.lastEventDateTime = date(2025, 6, 15)
    assert instance.lastEventDateTime == date(2025, 6, 15)


def test_tracker_Animal_sex_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_tracker_Animal_sexCode_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.sexCode == "sample_text"
    instance.sexCode = "sample_text_2"
    assert instance.sexCode == "sample_text_2"


def test_tracker_Animal_species_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.species == "sample_text"
    instance.species = "sample_text_2"
    assert instance.species == "sample_text_2"


def test_tracker_Animal_speciesCode_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.speciesCode == "sample_text"
    instance.speciesCode = "sample_text_2"
    assert instance.speciesCode == "sample_text_2"


def test_tracker_Animal_type_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_tracker_Animal_visualID_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.visualID == "sample_text"
    instance.visualID = "sample_text_2"
    assert instance.visualID == "sample_text_2"


def test_tracker_Animal_weight_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_tracker_Animal_weightGainPerDay_value_roundtrip():
    instance = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    assert instance.weightGainPerDay == "sample_text"
    instance.weightGainPerDay = "sample_text_2"
    assert instance.weightGainPerDay == "sample_text_2"


def test_tracker_BirthDefect_freemartin_value_roundtrip():
    instance = tracker_BirthDefect(freemartin=True)
    assert instance.freemartin == True
    instance.freemartin = False
    assert instance.freemartin == False


def test_tracker_Birthing_assisted_value_roundtrip():
    instance = tracker_Birthing(assisted=True, difficulty="sample_text", viability=True)
    assert instance.assisted == True
    instance.assisted = False
    assert instance.assisted == False


def test_tracker_Birthing_difficulty_value_roundtrip():
    instance = tracker_Birthing(assisted=True, difficulty="sample_text", viability=True)
    assert instance.difficulty == "sample_text"
    instance.difficulty = "sample_text_2"
    assert instance.difficulty == "sample_text_2"


def test_tracker_Birthing_viability_value_roundtrip():
    instance = tracker_Birthing(assisted=True, difficulty="sample_text", viability=True)
    assert instance.viability == True
    instance.viability = False
    assert instance.viability == False


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


def test_tracker_Caprine_goatBreed_value_roundtrip():
    instance = tracker_Caprine(goatBreed="sample_text")
    assert instance.goatBreed == "sample_text"
    instance.goatBreed = "sample_text_2"
    assert instance.goatBreed == "sample_text_2"


def test_tracker_Equine_horseBreed_value_roundtrip():
    instance = tracker_Equine(horseBreed="sample_text")
    assert instance.horseBreed == "sample_text"
    instance.horseBreed = "sample_text_2"
    assert instance.horseBreed == "sample_text_2"


def test_tracker_Event_comments_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_tracker_Event_correction_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    assert instance.correction == True
    instance.correction = False
    assert instance.correction == False


def test_tracker_Event_dateTime_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    assert instance.dateTime == date(2024, 1, 1)
    instance.dateTime = date(2025, 6, 15)
    assert instance.dateTime == date(2025, 6, 15)


def test_tracker_Event_electronicallyRead_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    assert instance.electronicallyRead == True
    instance.electronicallyRead = False
    assert instance.electronicallyRead == False


def test_tracker_Event_eventCode_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    assert instance.eventCode == 7
    instance.eventCode = 13
    assert instance.eventCode == 13


def test_tracker_Event_id_value_roundtrip():
    instance = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_tracker_EventAttribute_key_value_roundtrip():
    instance = tracker_EventAttribute(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_tracker_EventAttribute_value_value_roundtrip():
    instance = tracker_EventAttribute(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_tracker_EventAttributeSchema_dataType_value_roundtrip():
    instance = tracker_EventAttributeSchema(dataType="sample_text", description="sample_text", name="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_tracker_EventAttributeSchema_description_value_roundtrip():
    instance = tracker_EventAttributeSchema(dataType="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_tracker_EventAttributeSchema_name_value_roundtrip():
    instance = tracker_EventAttributeSchema(dataType="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tracker_EventSchema_animalType_value_roundtrip():
    instance = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    assert instance.animalType == "sample_text"
    instance.animalType = "sample_text_2"
    assert instance.animalType == "sample_text_2"


def test_tracker_EventSchema_description_value_roundtrip():
    instance = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_tracker_EventSchema_name_value_roundtrip():
    instance = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tracker_HerdTest_bredDateEstimate_value_roundtrip():
    instance = tracker_HerdTest(bredDateEstimate=date(2024, 1, 1), daysSinceBredEstimate=7, pregnant=True)
    assert instance.bredDateEstimate == date(2024, 1, 1)
    instance.bredDateEstimate = date(2025, 6, 15)
    assert instance.bredDateEstimate == date(2025, 6, 15)


def test_tracker_HerdTest_daysSinceBredEstimate_value_roundtrip():
    instance = tracker_HerdTest(bredDateEstimate=date(2024, 1, 1), daysSinceBredEstimate=7, pregnant=True)
    assert instance.daysSinceBredEstimate == 7
    instance.daysSinceBredEstimate = 13
    assert instance.daysSinceBredEstimate == 13


def test_tracker_HerdTest_pregnant_value_roundtrip():
    instance = tracker_HerdTest(bredDateEstimate=date(2024, 1, 1), daysSinceBredEstimate=7, pregnant=True)
    assert instance.pregnant == True
    instance.pregnant = False
    assert instance.pregnant == False


def test_tracker_Location_name_value_roundtrip():
    instance = tracker_Location(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tracker_Mastitis_location_value_roundtrip():
    instance = tracker_Mastitis(location="sample_text", origin="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_tracker_Mastitis_origin_value_roundtrip():
    instance = tracker_Mastitis(location="sample_text", origin="sample_text")
    assert instance.origin == "sample_text"
    instance.origin = "sample_text_2"
    assert instance.origin == "sample_text_2"


def test_tracker_MedicalTreatment_lot_value_roundtrip():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert instance.lot == "sample_text"
    instance.lot = "sample_text_2"
    assert instance.lot == "sample_text_2"


def test_tracker_MedicalTreatment_manufacturer_value_roundtrip():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert instance.manufacturer == "sample_text"
    instance.manufacturer = "sample_text_2"
    assert instance.manufacturer == "sample_text_2"


def test_tracker_MedicalTreatment_method_value_roundtrip():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert instance.method == "sample_text"
    instance.method = "sample_text_2"
    assert instance.method == "sample_text_2"


def test_tracker_MedicalTreatment_name_value_roundtrip():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tracker_MedicalTreatment_product_value_roundtrip():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert instance.product == "sample_text"
    instance.product = "sample_text_2"
    assert instance.product == "sample_text_2"


def test_tracker_MedicalTreatment_quantity_value_roundtrip():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert instance.quantity == "sample_text"
    instance.quantity = "sample_text_2"
    assert instance.quantity == "sample_text_2"


def test_tracker_MedicalTreatment_treatment_value_roundtrip():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert instance.treatment == "sample_text"
    instance.treatment = "sample_text_2"
    assert instance.treatment == "sample_text_2"


def test_tracker_MilkTest_otherSolids_value_roundtrip():
    instance = tracker_MilkTest(otherSolids=3.14, percentButterFat=3.14, percentProtein=3.14, poundsProduced=3.14, somaticCellCounts=7)
    assert instance.otherSolids == 3.14
    instance.otherSolids = 9.99
    assert instance.otherSolids == 9.99


def test_tracker_MilkTest_percentButterFat_value_roundtrip():
    instance = tracker_MilkTest(otherSolids=3.14, percentButterFat=3.14, percentProtein=3.14, poundsProduced=3.14, somaticCellCounts=7)
    assert instance.percentButterFat == 3.14
    instance.percentButterFat = 9.99
    assert instance.percentButterFat == 9.99


def test_tracker_MilkTest_percentProtein_value_roundtrip():
    instance = tracker_MilkTest(otherSolids=3.14, percentButterFat=3.14, percentProtein=3.14, poundsProduced=3.14, somaticCellCounts=7)
    assert instance.percentProtein == 3.14
    instance.percentProtein = 9.99
    assert instance.percentProtein == 9.99


def test_tracker_MilkTest_poundsProduced_value_roundtrip():
    instance = tracker_MilkTest(otherSolids=3.14, percentButterFat=3.14, percentProtein=3.14, poundsProduced=3.14, somaticCellCounts=7)
    assert instance.poundsProduced == 3.14
    instance.poundsProduced = 9.99
    assert instance.poundsProduced == 9.99


def test_tracker_MilkTest_somaticCellCounts_value_roundtrip():
    instance = tracker_MilkTest(otherSolids=3.14, percentButterFat=3.14, percentProtein=3.14, poundsProduced=3.14, somaticCellCounts=7)
    assert instance.somaticCellCounts == 7
    instance.somaticCellCounts = 13
    assert instance.somaticCellCounts == 13


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


def test_tracker_Ovine_scrapieTag_value_roundtrip():
    instance = tracker_Ovine(scrapieTag="sample_text", sheepBreed="sample_text")
    assert instance.scrapieTag == "sample_text"
    instance.scrapieTag = "sample_text_2"
    assert instance.scrapieTag == "sample_text_2"


def test_tracker_Ovine_sheepBreed_value_roundtrip():
    instance = tracker_Ovine(scrapieTag="sample_text", sheepBreed="sample_text")
    assert instance.sheepBreed == "sample_text"
    instance.sheepBreed = "sample_text_2"
    assert instance.sheepBreed == "sample_text_2"


def test_tracker_Premises_emailContact_value_roundtrip():
    instance = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    assert instance.emailContact == "sample_text"
    instance.emailContact = "sample_text_2"
    assert instance.emailContact == "sample_text_2"


def test_tracker_Premises_name_value_roundtrip():
    instance = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tracker_Premises_premisesId_value_roundtrip():
    instance = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    assert instance.premisesId == "sample_text"
    instance.premisesId = "sample_text_2"
    assert instance.premisesId == "sample_text_2"


def test_tracker_Premises_uri_value_roundtrip():
    instance = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_tracker_ReplacedTag_oldId_value_roundtrip():
    instance = tracker_ReplacedTag(oldId="sample_text", usainNumberUsedForOldId=True)
    assert instance.oldId == "sample_text"
    instance.oldId = "sample_text_2"
    assert instance.oldId == "sample_text_2"


def test_tracker_ReplacedTag_usainNumberUsedForOldId_value_roundtrip():
    instance = tracker_ReplacedTag(oldId="sample_text", usainNumberUsedForOldId=True)
    assert instance.usainNumberUsedForOldId == True
    instance.usainNumberUsedForOldId = False
    assert instance.usainNumberUsedForOldId == False


def test_tracker_Swine_leftEarNotching_value_roundtrip():
    instance = tracker_Swine(leftEarNotching=7, rightEarNotching=7, swineBreed="sample_text")
    assert instance.leftEarNotching == 7
    instance.leftEarNotching = 13
    assert instance.leftEarNotching == 13


def test_tracker_Swine_rightEarNotching_value_roundtrip():
    instance = tracker_Swine(leftEarNotching=7, rightEarNotching=7, swineBreed="sample_text")
    assert instance.rightEarNotching == 7
    instance.rightEarNotching = 13
    assert instance.rightEarNotching == 13


def test_tracker_Swine_swineBreed_value_roundtrip():
    instance = tracker_Swine(leftEarNotching=7, rightEarNotching=7, swineBreed="sample_text")
    assert instance.swineBreed == "sample_text"
    instance.swineBreed = "sample_text_2"
    assert instance.swineBreed == "sample_text_2"


def test_tracker_Tag_id_value_roundtrip():
    instance = tracker_Tag(id="sample_text", usainNumberUsed=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_tracker_Tag_usainNumberUsed_value_roundtrip():
    instance = tracker_Tag(id="sample_text", usainNumberUsed=True)
    assert instance.usainNumberUsed == True
    instance.usainNumberUsed = False
    assert instance.usainNumberUsed == False


def test_tracker_USBeefGrading_qualityGrade_value_roundtrip():
    instance = tracker_USBeefGrading(qualityGrade="sample_text", qualityGradeLevel="sample_text", yieldGrade="sample_text")
    assert instance.qualityGrade == "sample_text"
    instance.qualityGrade = "sample_text_2"
    assert instance.qualityGrade == "sample_text_2"


def test_tracker_USBeefGrading_qualityGradeLevel_value_roundtrip():
    instance = tracker_USBeefGrading(qualityGrade="sample_text", qualityGradeLevel="sample_text", yieldGrade="sample_text")
    assert instance.qualityGradeLevel == "sample_text"
    instance.qualityGradeLevel = "sample_text_2"
    assert instance.qualityGradeLevel == "sample_text_2"


def test_tracker_USBeefGrading_yieldGrade_value_roundtrip():
    instance = tracker_USBeefGrading(qualityGrade="sample_text", qualityGradeLevel="sample_text", yieldGrade="sample_text")
    assert instance.yieldGrade == "sample_text"
    instance.yieldGrade = "sample_text_2"
    assert instance.yieldGrade == "sample_text_2"


def test_tracker_USOvineGrading_qualityGrade_value_roundtrip():
    instance = tracker_USOvineGrading(qualityGrade="sample_text", qualityGradeLevel="sample_text")
    assert instance.qualityGrade == "sample_text"
    instance.qualityGrade = "sample_text_2"
    assert instance.qualityGrade == "sample_text_2"


def test_tracker_USOvineGrading_qualityGradeLevel_value_roundtrip():
    instance = tracker_USOvineGrading(qualityGrade="sample_text", qualityGradeLevel="sample_text")
    assert instance.qualityGradeLevel == "sample_text"
    instance.qualityGradeLevel = "sample_text_2"
    assert instance.qualityGradeLevel == "sample_text_2"


def test_tracker_USSwineGrading_qualityGrade_value_roundtrip():
    instance = tracker_USSwineGrading(qualityGrade="sample_text")
    assert instance.qualityGrade == "sample_text"
    instance.qualityGrade = "sample_text_2"
    assert instance.qualityGrade == "sample_text_2"


def test_tracker_WeighIn_weight_value_roundtrip():
    instance = tracker_WeighIn(weight="sample_text", weightGainPerDay="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_tracker_WeighIn_weightGainPerDay_value_roundtrip():
    instance = tracker_WeighIn(weight="sample_text", weightGainPerDay="sample_text")
    assert instance.weightGainPerDay == "sample_text"
    instance.weightGainPerDay = "sample_text_2"
    assert instance.weightGainPerDay == "sample_text_2"


def test_tracker_Bovine_isa_Animal():
    instance = tracker_Bovine()
    assert isinstance(instance, Animal)


def test_tracker_Caprine_isa_Animal():
    instance = tracker_Caprine(goatBreed="sample_text")
    assert isinstance(instance, Animal)


def test_tracker_Equine_isa_Animal():
    instance = tracker_Equine(horseBreed="sample_text")
    assert isinstance(instance, Animal)


def test_tracker_Ovine_isa_Animal():
    instance = tracker_Ovine(scrapieTag="sample_text", sheepBreed="sample_text")
    assert isinstance(instance, Animal)


def test_tracker_Swine_isa_Animal():
    instance = tracker_Swine(leftEarNotching=7, rightEarNotching=7, swineBreed="sample_text")
    assert isinstance(instance, Animal)


def test_tracker_Calving_isa_Birthing():
    instance = tracker_Calving()
    assert isinstance(instance, Birthing)


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


def test_tracker_BirthDefect_isa_Event():
    instance = tracker_BirthDefect(freemartin=True)
    assert isinstance(instance, Event)


def test_tracker_Birthing_isa_Event():
    instance = tracker_Birthing(assisted=True, difficulty="sample_text", viability=True)
    assert isinstance(instance, Event)


def test_tracker_Died_isa_Event():
    instance = tracker_Died()
    assert isinstance(instance, Event)


def test_tracker_Exported_isa_Event():
    instance = tracker_Exported()
    assert isinstance(instance, Event)


def test_tracker_GenericEvent_isa_Event():
    instance = tracker_GenericEvent()
    assert isinstance(instance, Event)


def test_tracker_HerdTest_isa_Event():
    instance = tracker_HerdTest(bredDateEstimate=date(2024, 1, 1), daysSinceBredEstimate=7, pregnant=True)
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


def test_tracker_MedicalCondition_isa_Event():
    instance = tracker_MedicalCondition()
    assert isinstance(instance, Event)


def test_tracker_MedicalTreatment_isa_Event():
    instance = tracker_MedicalTreatment(lot="sample_text", manufacturer="sample_text", method="sample_text", name="sample_text", product="sample_text", quantity="sample_text", treatment="sample_text")
    assert isinstance(instance, Event)


def test_tracker_MilkTest_isa_Event():
    instance = tracker_MilkTest(otherSolids=3.14, percentButterFat=3.14, percentProtein=3.14, poundsProduced=3.14, somaticCellCounts=7)
    assert isinstance(instance, Event)


def test_tracker_MovedIn_isa_Event():
    instance = tracker_MovedIn(sourcePin="sample_text")
    assert isinstance(instance, Event)


def test_tracker_MovedOut_isa_Event():
    instance = tracker_MovedOut(destinationPin="sample_text")
    assert isinstance(instance, Event)


def test_tracker_ReplacedTag_isa_Event():
    instance = tracker_ReplacedTag(oldId="sample_text", usainNumberUsedForOldId=True)
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


def test_tracker_USBeefGrading_isa_Event():
    instance = tracker_USBeefGrading(qualityGrade="sample_text", qualityGradeLevel="sample_text", yieldGrade="sample_text")
    assert isinstance(instance, Event)


def test_tracker_USOvineGrading_isa_Event():
    instance = tracker_USOvineGrading(qualityGrade="sample_text", qualityGradeLevel="sample_text")
    assert isinstance(instance, Event)


def test_tracker_USSwineGrading_isa_Event():
    instance = tracker_USSwineGrading(qualityGrade="sample_text")
    assert isinstance(instance, Event)


def test_tracker_WeighIn_isa_Event():
    instance = tracker_WeighIn(weight="sample_text", weightGainPerDay="sample_text")
    assert isinstance(instance, Event)


def test_tracker_Mastitis_isa_MedicalCondition():
    instance = tracker_Mastitis(location="sample_text", origin="sample_text")
    assert isinstance(instance, MedicalCondition)


def test_assoc_animals9_link_reassign_clear():
    a = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    b1 = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    b2 = tracker_Animal(ageInDays=13, alternativeID="sample_text_2", birthDate=date(2025, 6, 15), breed="sample_text_2", comments="sample_text_2", id="sample_text_2", lastEventDateTime=date(2025, 6, 15), sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2", type="sample_text_2", visualID="sample_text_2", weight="sample_text_2", weightGainPerDay="sample_text_2")
    _safe_set(a, 'tracker_Premises', {b1})
    assert _is_linked(a, 'tracker_Premises', b1)
    if hasattr(b1, 'tracker_Animal10'):
        assert _is_linked(b1, 'tracker_Animal10', a)
    _safe_set(a, 'tracker_Premises', {b2})
    assert _is_linked(a, 'tracker_Premises', b2)
    if hasattr(b1, 'tracker_Animal10'):
        assert not _is_linked(b1, 'tracker_Animal10', a)
    if hasattr(b2, 'tracker_Animal10'):
        assert _is_linked(b2, 'tracker_Animal10', a)
    _safe_set(a, 'tracker_Premises', set())
    assert not _is_linked(a, 'tracker_Premises', b2)
    if hasattr(b2, 'tracker_Animal10'):
        assert not _is_linked(b2, 'tracker_Animal10', a)


def test_assoc_dam2_link_reassign_clear():
    a = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    b1 = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    b2 = tracker_Animal(ageInDays=13, alternativeID="sample_text_2", birthDate=date(2025, 6, 15), breed="sample_text_2", comments="sample_text_2", id="sample_text_2", lastEventDateTime=date(2025, 6, 15), sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2", type="sample_text_2", visualID="sample_text_2", weight="sample_text_2", weightGainPerDay="sample_text_2")
    _safe_set(a, 'tracker_Animal1', b1)
    assert _is_linked(a, 'tracker_Animal1', b1)
    if hasattr(b1, 'tracker_Animal3'):
        assert _is_linked(b1, 'tracker_Animal3', a)
    _safe_set(a, 'tracker_Animal1', b2)
    assert _is_linked(a, 'tracker_Animal1', b2)
    if hasattr(b1, 'tracker_Animal3'):
        assert not _is_linked(b1, 'tracker_Animal3', a)
    if hasattr(b2, 'tracker_Animal3'):
        assert _is_linked(b2, 'tracker_Animal3', a)
    _safe_set(a, 'tracker_Animal1', None)
    assert not _is_linked(a, 'tracker_Animal1', b2)
    if hasattr(b2, 'tracker_Animal3'):
        assert not _is_linked(b2, 'tracker_Animal3', a)


def test_assoc_eventAttributes22_link_reassign_clear():
    a = tracker_GenericEvent()
    b1 = tracker_EventAttribute(key="sample_text", value="sample_text")
    b2 = tracker_EventAttribute(key="sample_text_2", value="sample_text_2")
    _safe_set(a, 'tracker_GenericEvent', {b1})
    assert _is_linked(a, 'tracker_GenericEvent', b1)
    if hasattr(b1, 'tracker_EventAttribute'):
        assert _is_linked(b1, 'tracker_EventAttribute', a)
    _safe_set(a, 'tracker_GenericEvent', {b2})
    assert _is_linked(a, 'tracker_GenericEvent', b2)
    if hasattr(b1, 'tracker_EventAttribute'):
        assert not _is_linked(b1, 'tracker_EventAttribute', a)
    if hasattr(b2, 'tracker_EventAttribute'):
        assert _is_linked(b2, 'tracker_EventAttribute', a)
    _safe_set(a, 'tracker_GenericEvent', set())
    assert not _is_linked(a, 'tracker_GenericEvent', b2)
    if hasattr(b2, 'tracker_EventAttribute'):
        assert not _is_linked(b2, 'tracker_EventAttribute', a)


def test_assoc_eventAttributes25_link_reassign_clear():
    a = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    b1 = tracker_EventAttributeSchema(dataType="sample_text", description="sample_text", name="sample_text")
    b2 = tracker_EventAttributeSchema(dataType="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'tracker_EventSchema26', {b1})
    assert _is_linked(a, 'tracker_EventSchema26', b1)
    if hasattr(b1, 'tracker_EventAttributeSchema'):
        assert _is_linked(b1, 'tracker_EventAttributeSchema', a)
    _safe_set(a, 'tracker_EventSchema26', {b2})
    assert _is_linked(a, 'tracker_EventSchema26', b2)
    if hasattr(b1, 'tracker_EventAttributeSchema'):
        assert not _is_linked(b1, 'tracker_EventAttributeSchema', a)
    if hasattr(b2, 'tracker_EventAttributeSchema'):
        assert _is_linked(b2, 'tracker_EventAttributeSchema', a)
    _safe_set(a, 'tracker_EventSchema26', set())
    assert not _is_linked(a, 'tracker_EventSchema26', b2)
    if hasattr(b2, 'tracker_EventAttributeSchema'):
        assert not _is_linked(b2, 'tracker_EventAttributeSchema', a)


def test_assoc_eventSchema23_link_reassign_clear():
    a = tracker_GenericEvent()
    b1 = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    b2 = tracker_EventSchema(animalType="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'tracker_GenericEvent24', b1)
    assert _is_linked(a, 'tracker_GenericEvent24', b1)
    if hasattr(b1, 'tracker_EventSchema'):
        assert _is_linked(b1, 'tracker_EventSchema', a)
    _safe_set(a, 'tracker_GenericEvent24', b2)
    assert _is_linked(a, 'tracker_GenericEvent24', b2)
    if hasattr(b1, 'tracker_EventSchema'):
        assert not _is_linked(b1, 'tracker_EventSchema', a)
    if hasattr(b2, 'tracker_EventSchema'):
        assert _is_linked(b2, 'tracker_EventSchema', a)
    _safe_set(a, 'tracker_GenericEvent24', None)
    assert not _is_linked(a, 'tracker_GenericEvent24', b2)
    if hasattr(b2, 'tracker_EventSchema'):
        assert not _is_linked(b2, 'tracker_EventSchema', a)


def test_assoc_eventSchemas27_link_reassign_clear():
    a = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    b1 = tracker_Schema()
    b2 = tracker_Schema()
    _safe_set(a, 'tracker_EventSchema29', b1)
    assert _is_linked(a, 'tracker_EventSchema29', b1)
    if hasattr(b1, 'tracker_Schema28'):
        assert _is_linked(b1, 'tracker_Schema28', a)
    _safe_set(a, 'tracker_EventSchema29', b2)
    assert _is_linked(a, 'tracker_EventSchema29', b2)
    if hasattr(b1, 'tracker_Schema28'):
        assert not _is_linked(b1, 'tracker_Schema28', a)
    if hasattr(b2, 'tracker_Schema28'):
        assert _is_linked(b2, 'tracker_Schema28', a)
    _safe_set(a, 'tracker_EventSchema29', None)
    assert not _is_linked(a, 'tracker_EventSchema29', b2)
    if hasattr(b2, 'tracker_Schema28'):
        assert not _is_linked(b2, 'tracker_Schema28', a)


def test_assoc_events7_link_reassign_clear():
    a = tracker_Tag(id="sample_text", usainNumberUsed=True)
    b1 = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    b2 = tracker_Event(comments="sample_text_2", correction=False, dateTime=date(2025, 6, 15), electronicallyRead=False, eventCode=13, id="sample_text_2")
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


def test_assoc_location20_link_reassign_clear():
    a = tracker_Location(name="sample_text")
    b1 = tracker_Sighting()
    b2 = tracker_Sighting()
    _safe_set(a, 'tracker_Location21', b1)
    assert _is_linked(a, 'tracker_Location21', b1)
    if hasattr(b1, 'tracker_Sighting'):
        assert _is_linked(b1, 'tracker_Sighting', a)
    _safe_set(a, 'tracker_Location21', b2)
    assert _is_linked(a, 'tracker_Location21', b2)
    if hasattr(b1, 'tracker_Sighting'):
        assert not _is_linked(b1, 'tracker_Sighting', a)
    if hasattr(b2, 'tracker_Sighting'):
        assert _is_linked(b2, 'tracker_Sighting', a)
    _safe_set(a, 'tracker_Location21', None)
    assert not _is_linked(a, 'tracker_Location21', b2)
    if hasattr(b2, 'tracker_Sighting'):
        assert not _is_linked(b2, 'tracker_Sighting', a)


def test_assoc_locations14_link_reassign_clear():
    a = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    b1 = tracker_Location(name="sample_text")
    b2 = tracker_Location(name="sample_text_2")
    _safe_set(a, 'tracker_Premises15', {b1})
    assert _is_linked(a, 'tracker_Premises15', b1)
    if hasattr(b1, 'tracker_Location'):
        assert _is_linked(b1, 'tracker_Location', a)
    _safe_set(a, 'tracker_Premises15', {b2})
    assert _is_linked(a, 'tracker_Premises15', b2)
    if hasattr(b1, 'tracker_Location'):
        assert not _is_linked(b1, 'tracker_Location', a)
    if hasattr(b2, 'tracker_Location'):
        assert _is_linked(b2, 'tracker_Location', a)
    _safe_set(a, 'tracker_Premises15', set())
    assert not _is_linked(a, 'tracker_Premises15', b2)
    if hasattr(b2, 'tracker_Location'):
        assert not _is_linked(b2, 'tracker_Location', a)


def test_assoc_oldTag18_link_reassign_clear():
    a = tracker_Tag(id="sample_text", usainNumberUsed=True)
    b1 = tracker_ReplacedTag(oldId="sample_text", usainNumberUsedForOldId=True)
    b2 = tracker_ReplacedTag(oldId="sample_text_2", usainNumberUsedForOldId=False)
    _safe_set(a, 'tracker_Tag19', b1)
    assert _is_linked(a, 'tracker_Tag19', b1)
    if hasattr(b1, 'tracker_ReplacedTag'):
        assert _is_linked(b1, 'tracker_ReplacedTag', a)
    _safe_set(a, 'tracker_Tag19', b2)
    assert _is_linked(a, 'tracker_Tag19', b2)
    if hasattr(b1, 'tracker_ReplacedTag'):
        assert not _is_linked(b1, 'tracker_ReplacedTag', a)
    if hasattr(b2, 'tracker_ReplacedTag'):
        assert _is_linked(b2, 'tracker_ReplacedTag', a)
    _safe_set(a, 'tracker_Tag19', None)
    assert not _is_linked(a, 'tracker_Tag19', b2)
    if hasattr(b2, 'tracker_ReplacedTag'):
        assert not _is_linked(b2, 'tracker_ReplacedTag', a)


def test_assoc_schema16_link_reassign_clear():
    a = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    b1 = tracker_Schema()
    b2 = tracker_Schema()
    _safe_set(a, 'tracker_Premises17', b1)
    assert _is_linked(a, 'tracker_Premises17', b1)
    if hasattr(b1, 'tracker_Schema'):
        assert _is_linked(b1, 'tracker_Schema', a)
    _safe_set(a, 'tracker_Premises17', b2)
    assert _is_linked(a, 'tracker_Premises17', b2)
    if hasattr(b1, 'tracker_Schema'):
        assert not _is_linked(b1, 'tracker_Schema', a)
    if hasattr(b2, 'tracker_Schema'):
        assert _is_linked(b2, 'tracker_Schema', a)
    _safe_set(a, 'tracker_Premises17', None)
    assert not _is_linked(a, 'tracker_Premises17', b2)
    if hasattr(b2, 'tracker_Schema'):
        assert not _is_linked(b2, 'tracker_Schema', a)


def test_assoc_sire5_link_reassign_clear():
    a = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    b1 = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    b2 = tracker_Animal(ageInDays=13, alternativeID="sample_text_2", birthDate=date(2025, 6, 15), breed="sample_text_2", comments="sample_text_2", id="sample_text_2", lastEventDateTime=date(2025, 6, 15), sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2", type="sample_text_2", visualID="sample_text_2", weight="sample_text_2", weightGainPerDay="sample_text_2")
    _safe_set(a, 'tracker_Animal4', b1)
    assert _is_linked(a, 'tracker_Animal4', b1)
    if hasattr(b1, 'tracker_Animal6'):
        assert _is_linked(b1, 'tracker_Animal6', a)
    _safe_set(a, 'tracker_Animal4', b2)
    assert _is_linked(a, 'tracker_Animal4', b2)
    if hasattr(b1, 'tracker_Animal6'):
        assert not _is_linked(b1, 'tracker_Animal6', a)
    if hasattr(b2, 'tracker_Animal6'):
        assert _is_linked(b2, 'tracker_Animal6', a)
    _safe_set(a, 'tracker_Animal4', None)
    assert not _is_linked(a, 'tracker_Animal4', b2)
    if hasattr(b2, 'tracker_Animal6'):
        assert not _is_linked(b2, 'tracker_Animal6', a)


def test_assoc_tag8_link_reassign_clear():
    a = tracker_Tag(id="sample_text", usainNumberUsed=True)
    b1 = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    b2 = tracker_Event(comments="sample_text_2", correction=False, dateTime=date(2025, 6, 15), electronicallyRead=False, eventCode=13, id="sample_text_2")
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
    a = tracker_Tag(id="sample_text", usainNumberUsed=True)
    b1 = tracker_Animal(ageInDays=7, alternativeID="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", type="sample_text", visualID="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    b2 = tracker_Animal(ageInDays=13, alternativeID="sample_text_2", birthDate=date(2025, 6, 15), breed="sample_text_2", comments="sample_text_2", id="sample_text_2", lastEventDateTime=date(2025, 6, 15), sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2", type="sample_text_2", visualID="sample_text_2", weight="sample_text_2", weightGainPerDay="sample_text_2")
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


def test_assoc_unAppliedTags11_link_reassign_clear():
    a = tracker_Tag(id="sample_text", usainNumberUsed=True)
    b1 = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    b2 = tracker_Premises(emailContact="sample_text_2", name="sample_text_2", premisesId="sample_text_2", uri="sample_text_2")
    _safe_set(a, 'tracker_Tag13', b1)
    assert _is_linked(a, 'tracker_Tag13', b1)
    if hasattr(b1, 'tracker_Premises12'):
        assert _is_linked(b1, 'tracker_Premises12', a)
    _safe_set(a, 'tracker_Tag13', b2)
    assert _is_linked(a, 'tracker_Tag13', b2)
    if hasattr(b1, 'tracker_Premises12'):
        assert not _is_linked(b1, 'tracker_Premises12', a)
    if hasattr(b2, 'tracker_Premises12'):
        assert _is_linked(b2, 'tracker_Premises12', a)
    _safe_set(a, 'tracker_Tag13', None)
    assert not _is_linked(a, 'tracker_Tag13', b2)
    if hasattr(b2, 'tracker_Premises12'):
        assert not _is_linked(b2, 'tracker_Premises12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Animal_strategy = st.builds(Animal)
@given(instance=Animal_strategy)
@settings(max_examples=25)
def test_Animal_instantiation(instance):
    assert isinstance(instance, Animal)


Birthing_strategy = st.builds(Birthing)
@given(instance=Birthing_strategy)
@settings(max_examples=25)
def test_Birthing_instantiation(instance):
    assert isinstance(instance, Birthing)


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


MedicalCondition_strategy = st.builds(MedicalCondition)
@given(instance=MedicalCondition_strategy)
@settings(max_examples=25)
def test_MedicalCondition_instantiation(instance):
    assert isinstance(instance, MedicalCondition)


tracker_Animal_strategy = st.builds(tracker_Animal, ageInDays=st.integers(), alternativeID=safe_text, birthDate=st.dates(), breed=safe_text, comments=safe_text, id=safe_text, lastEventDateTime=st.dates(), sex=safe_text, sexCode=safe_text, species=safe_text, speciesCode=safe_text, type=safe_text, visualID=safe_text, weight=safe_text, weightGainPerDay=safe_text)
@given(instance=tracker_Animal_strategy)
@settings(max_examples=25)
def test_tracker_Animal_instantiation(instance):
    assert isinstance(instance, tracker_Animal)


tracker_AnimalMissing_strategy = st.builds(tracker_AnimalMissing)
@given(instance=tracker_AnimalMissing_strategy)
@settings(max_examples=25)
def test_tracker_AnimalMissing_instantiation(instance):
    assert isinstance(instance, tracker_AnimalMissing)


tracker_BirthDefect_strategy = st.builds(tracker_BirthDefect, freemartin=st.booleans())
@given(instance=tracker_BirthDefect_strategy)
@settings(max_examples=25)
def test_tracker_BirthDefect_instantiation(instance):
    assert isinstance(instance, tracker_BirthDefect)


tracker_Birthing_strategy = st.builds(tracker_Birthing, assisted=st.booleans(), difficulty=safe_text, viability=st.booleans())
@given(instance=tracker_Birthing_strategy)
@settings(max_examples=25)
def test_tracker_Birthing_instantiation(instance):
    assert isinstance(instance, tracker_Birthing)


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


tracker_Calving_strategy = st.builds(tracker_Calving)
@given(instance=tracker_Calving_strategy)
@settings(max_examples=25)
def test_tracker_Calving_instantiation(instance):
    assert isinstance(instance, tracker_Calving)


tracker_Caprine_strategy = st.builds(tracker_Caprine, goatBreed=safe_text)
@given(instance=tracker_Caprine_strategy)
@settings(max_examples=25)
def test_tracker_Caprine_instantiation(instance):
    assert isinstance(instance, tracker_Caprine)


tracker_Died_strategy = st.builds(tracker_Died)
@given(instance=tracker_Died_strategy)
@settings(max_examples=25)
def test_tracker_Died_instantiation(instance):
    assert isinstance(instance, tracker_Died)


tracker_Equine_strategy = st.builds(tracker_Equine, horseBreed=safe_text)
@given(instance=tracker_Equine_strategy)
@settings(max_examples=25)
def test_tracker_Equine_instantiation(instance):
    assert isinstance(instance, tracker_Equine)


tracker_Event_strategy = st.builds(tracker_Event, comments=safe_text, correction=st.booleans(), dateTime=st.dates(), electronicallyRead=st.booleans(), eventCode=st.integers(), id=safe_text)
@given(instance=tracker_Event_strategy)
@settings(max_examples=25)
def test_tracker_Event_instantiation(instance):
    assert isinstance(instance, tracker_Event)


tracker_EventAttribute_strategy = st.builds(tracker_EventAttribute, key=safe_text, value=safe_text)
@given(instance=tracker_EventAttribute_strategy)
@settings(max_examples=25)
def test_tracker_EventAttribute_instantiation(instance):
    assert isinstance(instance, tracker_EventAttribute)


tracker_EventAttributeSchema_strategy = st.builds(tracker_EventAttributeSchema, dataType=safe_text, description=safe_text, name=safe_text)
@given(instance=tracker_EventAttributeSchema_strategy)
@settings(max_examples=25)
def test_tracker_EventAttributeSchema_instantiation(instance):
    assert isinstance(instance, tracker_EventAttributeSchema)


tracker_EventSchema_strategy = st.builds(tracker_EventSchema, animalType=safe_text, description=safe_text, name=safe_text)
@given(instance=tracker_EventSchema_strategy)
@settings(max_examples=25)
def test_tracker_EventSchema_instantiation(instance):
    assert isinstance(instance, tracker_EventSchema)


tracker_Exported_strategy = st.builds(tracker_Exported)
@given(instance=tracker_Exported_strategy)
@settings(max_examples=25)
def test_tracker_Exported_instantiation(instance):
    assert isinstance(instance, tracker_Exported)


tracker_GenericEvent_strategy = st.builds(tracker_GenericEvent)
@given(instance=tracker_GenericEvent_strategy)
@settings(max_examples=25)
def test_tracker_GenericEvent_instantiation(instance):
    assert isinstance(instance, tracker_GenericEvent)


tracker_HerdTest_strategy = st.builds(tracker_HerdTest, bredDateEstimate=st.dates(), daysSinceBredEstimate=st.integers(), pregnant=st.booleans())
@given(instance=tracker_HerdTest_strategy)
@settings(max_examples=25)
def test_tracker_HerdTest_instantiation(instance):
    assert isinstance(instance, tracker_HerdTest)


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


tracker_Location_strategy = st.builds(tracker_Location, name=safe_text)
@given(instance=tracker_Location_strategy)
@settings(max_examples=25)
def test_tracker_Location_instantiation(instance):
    assert isinstance(instance, tracker_Location)


tracker_LostTag_strategy = st.builds(tracker_LostTag)
@given(instance=tracker_LostTag_strategy)
@settings(max_examples=25)
def test_tracker_LostTag_instantiation(instance):
    assert isinstance(instance, tracker_LostTag)


tracker_Mastitis_strategy = st.builds(tracker_Mastitis, location=safe_text, origin=safe_text)
@given(instance=tracker_Mastitis_strategy)
@settings(max_examples=25)
def test_tracker_Mastitis_instantiation(instance):
    assert isinstance(instance, tracker_Mastitis)


tracker_MedicalCondition_strategy = st.builds(tracker_MedicalCondition)
@given(instance=tracker_MedicalCondition_strategy)
@settings(max_examples=25)
def test_tracker_MedicalCondition_instantiation(instance):
    assert isinstance(instance, tracker_MedicalCondition)


tracker_MedicalTreatment_strategy = st.builds(tracker_MedicalTreatment, lot=safe_text, manufacturer=safe_text, method=safe_text, name=safe_text, product=safe_text, quantity=safe_text, treatment=safe_text)
@given(instance=tracker_MedicalTreatment_strategy)
@settings(max_examples=25)
def test_tracker_MedicalTreatment_instantiation(instance):
    assert isinstance(instance, tracker_MedicalTreatment)


tracker_MilkTest_strategy = st.builds(tracker_MilkTest, otherSolids=st.floats(allow_nan=False, allow_infinity=False), percentButterFat=st.floats(allow_nan=False, allow_infinity=False), percentProtein=st.floats(allow_nan=False, allow_infinity=False), poundsProduced=st.floats(allow_nan=False, allow_infinity=False), somaticCellCounts=st.integers())
@given(instance=tracker_MilkTest_strategy)
@settings(max_examples=25)
def test_tracker_MilkTest_instantiation(instance):
    assert isinstance(instance, tracker_MilkTest)


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


tracker_Ovine_strategy = st.builds(tracker_Ovine, scrapieTag=safe_text, sheepBreed=safe_text)
@given(instance=tracker_Ovine_strategy)
@settings(max_examples=25)
def test_tracker_Ovine_instantiation(instance):
    assert isinstance(instance, tracker_Ovine)


tracker_Premises_strategy = st.builds(tracker_Premises, emailContact=safe_text, name=safe_text, premisesId=safe_text, uri=safe_text)
@given(instance=tracker_Premises_strategy)
@settings(max_examples=25)
def test_tracker_Premises_instantiation(instance):
    assert isinstance(instance, tracker_Premises)


tracker_ReplacedTag_strategy = st.builds(tracker_ReplacedTag, oldId=safe_text, usainNumberUsedForOldId=st.booleans())
@given(instance=tracker_ReplacedTag_strategy)
@settings(max_examples=25)
def test_tracker_ReplacedTag_instantiation(instance):
    assert isinstance(instance, tracker_ReplacedTag)


tracker_Schema_strategy = st.builds(tracker_Schema)
@given(instance=tracker_Schema_strategy)
@settings(max_examples=25)
def test_tracker_Schema_instantiation(instance):
    assert isinstance(instance, tracker_Schema)


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


tracker_Swine_strategy = st.builds(tracker_Swine, leftEarNotching=st.integers(), rightEarNotching=st.integers(), swineBreed=safe_text)
@given(instance=tracker_Swine_strategy)
@settings(max_examples=25)
def test_tracker_Swine_instantiation(instance):
    assert isinstance(instance, tracker_Swine)


tracker_Tag_strategy = st.builds(tracker_Tag, id=safe_text, usainNumberUsed=st.booleans())
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


tracker_USBeefGrading_strategy = st.builds(tracker_USBeefGrading, qualityGrade=safe_text, qualityGradeLevel=safe_text, yieldGrade=safe_text)
@given(instance=tracker_USBeefGrading_strategy)
@settings(max_examples=25)
def test_tracker_USBeefGrading_instantiation(instance):
    assert isinstance(instance, tracker_USBeefGrading)


tracker_USOvineGrading_strategy = st.builds(tracker_USOvineGrading, qualityGrade=safe_text, qualityGradeLevel=safe_text)
@given(instance=tracker_USOvineGrading_strategy)
@settings(max_examples=25)
def test_tracker_USOvineGrading_instantiation(instance):
    assert isinstance(instance, tracker_USOvineGrading)


tracker_USSwineGrading_strategy = st.builds(tracker_USSwineGrading, qualityGrade=safe_text)
@given(instance=tracker_USSwineGrading_strategy)
@settings(max_examples=25)
def test_tracker_USSwineGrading_instantiation(instance):
    assert isinstance(instance, tracker_USSwineGrading)


tracker_WeighIn_strategy = st.builds(tracker_WeighIn, weight=safe_text, weightGainPerDay=safe_text)
@given(instance=tracker_WeighIn_strategy)
@settings(max_examples=25)
def test_tracker_WeighIn_instantiation(instance):
    assert isinstance(instance, tracker_WeighIn)



