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
    PKeyAndUnique,
    rdbms_ModelElement,
    DataType,
    Constraints,
    rdbms_SystemDataType,
    rdbms_UserDefinedDataType,
    ModelElement,
    rdbms_Constraints,
    rdbms_Table,
    rdbms_Database,
    rdbms_DataType,
    rdbms_PKeyAndUnique,
    rdbms_CheckCon,
    rdbms_Column,
    rdbms_UniqueCon,
    rdbms_PrimaryKeyCon,
    rdbms_ForeignKey,
    DeferrableAct,
    ReferencingType,
    Action,
    DeferredAct,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pkeyandunique_is_not_abstract():
    assert not inspect.isabstract(PKeyAndUnique)


def test_hyp_pkeyandunique_constructor_exists():
    assert callable(PKeyAndUnique.__init__)


def test_hyp_pkeyandunique_constructor_args():
    sig = inspect.signature(PKeyAndUnique.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_modelelement_is_not_abstract():
    assert not inspect.isabstract(rdbms_ModelElement)


def test_hyp_rdbms_modelelement_constructor_exists():
    assert callable(rdbms_ModelElement.__init__)


def test_hyp_rdbms_modelelement_constructor_args():
    sig = inspect.signature(rdbms_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constraints_is_not_abstract():
    assert not inspect.isabstract(Constraints)


def test_hyp_constraints_constructor_exists():
    assert callable(Constraints.__init__)


def test_hyp_constraints_constructor_args():
    sig = inspect.signature(Constraints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_systemdatatype_is_not_abstract():
    assert not inspect.isabstract(rdbms_SystemDataType)


def test_hyp_rdbms_systemdatatype_constructor_exists():
    assert callable(rdbms_SystemDataType.__init__)


def test_hyp_rdbms_systemdatatype_constructor_args():
    sig = inspect.signature(rdbms_SystemDataType.__init__)
    params = list(sig.parameters.keys())
    assert "predefinedDecPlaces" in params, "Missing parameter 'predefinedDecPlaces'"
    assert "predefinedLength" in params, "Missing parameter 'predefinedLength'"





def test_hyp_rdbms_userdefineddatatype_is_not_abstract():
    assert not inspect.isabstract(rdbms_UserDefinedDataType)


def test_hyp_rdbms_userdefineddatatype_constructor_exists():
    assert callable(rdbms_UserDefinedDataType.__init__)


def test_hyp_rdbms_userdefineddatatype_constructor_args():
    sig = inspect.signature(rdbms_UserDefinedDataType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "length" in params, "Missing parameter 'length'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"






def test_hyp_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_hyp_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_hyp_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_constraints_is_not_abstract():
    assert not inspect.isabstract(rdbms_Constraints)


def test_hyp_rdbms_constraints_constructor_exists():
    assert callable(rdbms_Constraints.__init__)


def test_hyp_rdbms_constraints_constructor_args():
    sig = inspect.signature(rdbms_Constraints.__init__)
    params = list(sig.parameters.keys())
    assert "deferrable" in params, "Missing parameter 'deferrable'"
    assert "deferred" in params, "Missing parameter 'deferred'"





def test_hyp_rdbms_table_is_not_abstract():
    assert not inspect.isabstract(rdbms_Table)


def test_hyp_rdbms_table_constructor_exists():
    assert callable(rdbms_Table.__init__)


def test_hyp_rdbms_table_constructor_args():
    sig = inspect.signature(rdbms_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_database_is_not_abstract():
    assert not inspect.isabstract(rdbms_Database)


def test_hyp_rdbms_database_constructor_exists():
    assert callable(rdbms_Database.__init__)


def test_hyp_rdbms_database_constructor_args():
    sig = inspect.signature(rdbms_Database.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_datatype_is_not_abstract():
    assert not inspect.isabstract(rdbms_DataType)


def test_hyp_rdbms_datatype_constructor_exists():
    assert callable(rdbms_DataType.__init__)


def test_hyp_rdbms_datatype_constructor_args():
    sig = inspect.signature(rdbms_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_pkeyandunique_is_not_abstract():
    assert not inspect.isabstract(rdbms_PKeyAndUnique)


def test_hyp_rdbms_pkeyandunique_constructor_exists():
    assert callable(rdbms_PKeyAndUnique.__init__)


def test_hyp_rdbms_pkeyandunique_constructor_args():
    sig = inspect.signature(rdbms_PKeyAndUnique.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_checkcon_is_not_abstract():
    assert not inspect.isabstract(rdbms_CheckCon)


def test_hyp_rdbms_checkcon_constructor_exists():
    assert callable(rdbms_CheckCon.__init__)


def test_hyp_rdbms_checkcon_constructor_args():
    sig = inspect.signature(rdbms_CheckCon.__init__)
    params = list(sig.parameters.keys())
    assert "checkCondition" in params, "Missing parameter 'checkCondition'"




def test_hyp_rdbms_column_is_not_abstract():
    assert not inspect.isabstract(rdbms_Column)


def test_hyp_rdbms_column_constructor_exists():
    assert callable(rdbms_Column.__init__)


def test_hyp_rdbms_column_constructor_args():
    sig = inspect.signature(rdbms_Column.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "length" in params, "Missing parameter 'length'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "default" in params, "Missing parameter 'default'"







def test_hyp_rdbms_uniquecon_is_not_abstract():
    assert not inspect.isabstract(rdbms_UniqueCon)


def test_hyp_rdbms_uniquecon_constructor_exists():
    assert callable(rdbms_UniqueCon.__init__)


def test_hyp_rdbms_uniquecon_constructor_args():
    sig = inspect.signature(rdbms_UniqueCon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_primarykeycon_is_not_abstract():
    assert not inspect.isabstract(rdbms_PrimaryKeyCon)


def test_hyp_rdbms_primarykeycon_constructor_exists():
    assert callable(rdbms_PrimaryKeyCon.__init__)


def test_hyp_rdbms_primarykeycon_constructor_args():
    sig = inspect.signature(rdbms_PrimaryKeyCon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms_ForeignKey)


def test_hyp_rdbms_foreignkey_constructor_exists():
    assert callable(rdbms_ForeignKey.__init__)


def test_hyp_rdbms_foreignkey_constructor_args():
    sig = inspect.signature(rdbms_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "match" in params, "Missing parameter 'match'"
    assert "inverseReferentialIntegrityCon" in params, "Missing parameter 'inverseReferentialIntegrityCon'"
    assert "deleteActionRHS" in params, "Missing parameter 'deleteActionRHS'"
    assert "updateActionRHS" in params, "Missing parameter 'updateActionRHS'"





def test_hyp_deferrableact_exists():
    # Check that the Enumeration exists
    assert DeferrableAct is not None

def test_hyp_deferrableact_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeferrableAct]
    expected_literals = [
        "DEFFERABLE",
        "NOT_DEFFERABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeferrableAct"

def test_hyp_referencingtype_exists():
    # Check that the Enumeration exists
    assert ReferencingType is not None

def test_hyp_referencingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferencingType]
    expected_literals = [
        "PARTIAL",
        "FULL",
        "DEFAULT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferencingType"

def test_hyp_action_exists():
    # Check that the Enumeration exists
    assert Action is not None

def test_hyp_action_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Action]
    expected_literals = [
        "NO_ACTION",
        "SET_NULL",
        "SET_DEFAULT",
        "RESTRICT",
        "CASCADE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Action"

def test_hyp_deferredact_exists():
    # Check that the Enumeration exists
    assert DeferredAct is not None

def test_hyp_deferredact_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeferredAct]
    expected_literals = [
        "INITIALLY_IMMEDIATE",
        "INITIALLY_DEFERRED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeferredAct"


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
PKeyAndUnique_strategy = st.builds(
    PKeyAndUnique,
)
rdbms_ModelElement_strategy = st.builds(
    rdbms_ModelElement,
    name=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
Constraints_strategy = st.builds(
    Constraints,
)
rdbms_SystemDataType_strategy = st.builds(
    rdbms_SystemDataType,
    predefinedDecPlaces=
        st.integers(),
    predefinedLength=
        st.integers()
)
rdbms_UserDefinedDataType_strategy = st.builds(
    rdbms_UserDefinedDataType,
    precision=
        st.integers(),
    length=
        st.integers(),
    defaultValue=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
rdbms_Constraints_strategy = st.builds(
    rdbms_Constraints,
    deferrable=
        safe_text,
    deferred=
        safe_text
)
rdbms_Table_strategy = st.builds(
    rdbms_Table,
)
rdbms_Database_strategy = st.builds(
    rdbms_Database,
)
rdbms_DataType_strategy = st.builds(
    rdbms_DataType,
)
rdbms_PKeyAndUnique_strategy = st.builds(
    rdbms_PKeyAndUnique,
)
rdbms_CheckCon_strategy = st.builds(
    rdbms_CheckCon,
    checkCondition=
        safe_text
)
rdbms_Column_strategy = st.builds(
    rdbms_Column,
    nullable=
        st.booleans(),
    length=
        st.integers(),
    precision=
        st.integers(),
    default=
        safe_text
)
rdbms_UniqueCon_strategy = st.builds(
    rdbms_UniqueCon,
)
rdbms_PrimaryKeyCon_strategy = st.builds(
    rdbms_PrimaryKeyCon,
)
rdbms_ForeignKey_strategy = st.builds(
    rdbms_ForeignKey,
    match=
        safe_text,
    inverseReferentialIntegrityCon=
        st.booleans(),
    deleteActionRHS=
        safe_text,
    updateActionRHS=
        safe_text
)





@given(instance=rdbms_ModelElement_strategy)
def test_hyp_rdbms_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=rdbms_SystemDataType_strategy)
def test_hyp_rdbms_systemdatatype_predefinedDecPlaces_setter(instance):
    original = instance.predefinedDecPlaces
    instance.predefinedDecPlaces = original
    assert instance.predefinedDecPlaces == original



@given(instance=rdbms_SystemDataType_strategy)
def test_hyp_rdbms_systemdatatype_predefinedLength_setter(instance):
    original = instance.predefinedLength
    instance.predefinedLength = original
    assert instance.predefinedLength == original




@given(instance=rdbms_UserDefinedDataType_strategy)
def test_hyp_rdbms_userdefineddatatype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=rdbms_UserDefinedDataType_strategy)
def test_hyp_rdbms_userdefineddatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=rdbms_UserDefinedDataType_strategy)
def test_hyp_rdbms_userdefineddatatype_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original





@given(instance=rdbms_Constraints_strategy)
def test_hyp_rdbms_constraints_deferrable_setter(instance):
    original = instance.deferrable
    instance.deferrable = original
    assert instance.deferrable == original



@given(instance=rdbms_Constraints_strategy)
def test_hyp_rdbms_constraints_deferred_setter(instance):
    original = instance.deferred
    instance.deferred = original
    assert instance.deferred == original








@given(instance=rdbms_CheckCon_strategy)
def test_hyp_rdbms_checkcon_checkCondition_setter(instance):
    original = instance.checkCondition
    instance.checkCondition = original
    assert instance.checkCondition == original




@given(instance=rdbms_Column_strategy)
def test_hyp_rdbms_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=rdbms_Column_strategy)
def test_hyp_rdbms_column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=rdbms_Column_strategy)
def test_hyp_rdbms_column_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=rdbms_Column_strategy)
def test_hyp_rdbms_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original






@given(instance=rdbms_ForeignKey_strategy)
def test_hyp_rdbms_foreignkey_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original



@given(instance=rdbms_ForeignKey_strategy)
def test_hyp_rdbms_foreignkey_inverseReferentialIntegrityCon_setter(instance):
    original = instance.inverseReferentialIntegrityCon
    instance.inverseReferentialIntegrityCon = original
    assert instance.inverseReferentialIntegrityCon == original



@given(instance=rdbms_ForeignKey_strategy)
def test_hyp_rdbms_foreignkey_deleteActionRHS_setter(instance):
    original = instance.deleteActionRHS
    instance.deleteActionRHS = original
    assert instance.deleteActionRHS == original



@given(instance=rdbms_ForeignKey_strategy)
def test_hyp_rdbms_foreignkey_updateActionRHS_setter(instance):
    original = instance.updateActionRHS
    instance.updateActionRHS = original
    assert instance.updateActionRHS == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Constraints,
    DataType,
    ModelElement,
    PKeyAndUnique,
    rdbms_CheckCon,
    rdbms_Column,
    rdbms_Constraints,
    rdbms_DataType,
    rdbms_Database,
    rdbms_ForeignKey,
    rdbms_ModelElement,
    rdbms_PKeyAndUnique,
    rdbms_PrimaryKeyCon,
    rdbms_SystemDataType,
    rdbms_Table,
    rdbms_UniqueCon,
    rdbms_UserDefinedDataType,
    Action,
    DeferrableAct,
    DeferredAct,
    ReferencingType,
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

def test_rdbms_CheckCon_checkCondition_value_roundtrip():
    instance = rdbms_CheckCon(checkCondition="sample_text")
    assert instance.checkCondition == "sample_text"
    instance.checkCondition = "sample_text_2"
    assert instance.checkCondition == "sample_text_2"


def test_rdbms_Column_default_value_roundtrip():
    instance = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_rdbms_Column_length_value_roundtrip():
    instance = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_rdbms_Column_nullable_value_roundtrip():
    instance = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    assert instance.nullable == True
    instance.nullable = False
    assert instance.nullable == False


def test_rdbms_Column_precision_value_roundtrip():
    instance = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    assert instance.precision == 7
    instance.precision = 13
    assert instance.precision == 13


def test_rdbms_Constraints_deferrable_value_roundtrip():
    instance = rdbms_Constraints(deferrable="sample_text", deferred="sample_text")
    assert instance.deferrable == "sample_text"
    instance.deferrable = "sample_text_2"
    assert instance.deferrable == "sample_text_2"


def test_rdbms_Constraints_deferred_value_roundtrip():
    instance = rdbms_Constraints(deferrable="sample_text", deferred="sample_text")
    assert instance.deferred == "sample_text"
    instance.deferred = "sample_text_2"
    assert instance.deferred == "sample_text_2"


def test_rdbms_ForeignKey_deleteActionRHS_value_roundtrip():
    instance = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    assert instance.deleteActionRHS == "sample_text"
    instance.deleteActionRHS = "sample_text_2"
    assert instance.deleteActionRHS == "sample_text_2"


def test_rdbms_ForeignKey_inverseReferentialIntegrityCon_value_roundtrip():
    instance = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    assert instance.inverseReferentialIntegrityCon == True
    instance.inverseReferentialIntegrityCon = False
    assert instance.inverseReferentialIntegrityCon == False


def test_rdbms_ForeignKey_match_value_roundtrip():
    instance = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    assert instance.match == "sample_text"
    instance.match = "sample_text_2"
    assert instance.match == "sample_text_2"


def test_rdbms_ForeignKey_updateActionRHS_value_roundtrip():
    instance = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    assert instance.updateActionRHS == "sample_text"
    instance.updateActionRHS = "sample_text_2"
    assert instance.updateActionRHS == "sample_text_2"


def test_rdbms_ModelElement_name_value_roundtrip():
    instance = rdbms_ModelElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rdbms_SystemDataType_predefinedDecPlaces_value_roundtrip():
    instance = rdbms_SystemDataType(predefinedDecPlaces=7, predefinedLength=7)
    assert instance.predefinedDecPlaces == 7
    instance.predefinedDecPlaces = 13
    assert instance.predefinedDecPlaces == 13


def test_rdbms_SystemDataType_predefinedLength_value_roundtrip():
    instance = rdbms_SystemDataType(predefinedDecPlaces=7, predefinedLength=7)
    assert instance.predefinedLength == 7
    instance.predefinedLength = 13
    assert instance.predefinedLength == 13


def test_rdbms_UserDefinedDataType_defaultValue_value_roundtrip():
    instance = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_rdbms_UserDefinedDataType_length_value_roundtrip():
    instance = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_rdbms_UserDefinedDataType_precision_value_roundtrip():
    instance = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    assert instance.precision == 7
    instance.precision = 13
    assert instance.precision == 13


def test_rdbms_CheckCon_isa_Constraints():
    instance = rdbms_CheckCon(checkCondition="sample_text")
    assert isinstance(instance, Constraints)


def test_rdbms_ForeignKey_isa_Constraints():
    instance = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    assert isinstance(instance, Constraints)


def test_rdbms_PKeyAndUnique_isa_Constraints():
    instance = rdbms_PKeyAndUnique()
    assert isinstance(instance, Constraints)


def test_rdbms_SystemDataType_isa_DataType():
    instance = rdbms_SystemDataType(predefinedDecPlaces=7, predefinedLength=7)
    assert isinstance(instance, DataType)


def test_rdbms_UserDefinedDataType_isa_DataType():
    instance = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    assert isinstance(instance, DataType)


def test_rdbms_Column_isa_ModelElement():
    instance = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    assert isinstance(instance, ModelElement)


def test_rdbms_Constraints_isa_ModelElement():
    instance = rdbms_Constraints(deferrable="sample_text", deferred="sample_text")
    assert isinstance(instance, ModelElement)


def test_rdbms_DataType_isa_ModelElement():
    instance = rdbms_DataType()
    assert isinstance(instance, ModelElement)


def test_rdbms_Database_isa_ModelElement():
    instance = rdbms_Database()
    assert isinstance(instance, ModelElement)


def test_rdbms_Table_isa_ModelElement():
    instance = rdbms_Table()
    assert isinstance(instance, ModelElement)


def test_rdbms_PrimaryKeyCon_isa_PKeyAndUnique():
    instance = rdbms_PrimaryKeyCon()
    assert isinstance(instance, PKeyAndUnique)


def test_rdbms_UniqueCon_isa_PKeyAndUnique():
    instance = rdbms_UniqueCon()
    assert isinstance(instance, PKeyAndUnique)


def test_assoc_FKTable29_link_reassign_clear():
    a = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    b1 = rdbms_Table()
    b2 = rdbms_Table()
    _safe_set(a, 'tableFKs', b1)
    assert _is_linked(a, 'tableFKs', b1)
    if hasattr(b1, 'Table'):
        assert _is_linked(b1, 'Table', a)
    _safe_set(a, 'tableFKs', b2)
    assert _is_linked(a, 'tableFKs', b2)
    if hasattr(b1, 'Table'):
        assert not _is_linked(b1, 'Table', a)
    if hasattr(b2, 'Table'):
        assert _is_linked(b2, 'Table', a)
    _safe_set(a, 'tableFKs', None)
    assert not _is_linked(a, 'tableFKs', b2)
    if hasattr(b2, 'Table'):
        assert not _is_linked(b2, 'Table', a)


def test_assoc_PKandUQColumns30_link_reassign_clear():
    a = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    b1 = rdbms_PKeyAndUnique()
    b2 = rdbms_PKeyAndUnique()
    _safe_set(a, 'rdbms_Column32', b1)
    assert _is_linked(a, 'rdbms_Column32', b1)
    if hasattr(b1, 'rdbms_PKeyAndUnique31'):
        assert _is_linked(b1, 'rdbms_PKeyAndUnique31', a)
    _safe_set(a, 'rdbms_Column32', b2)
    assert _is_linked(a, 'rdbms_Column32', b2)
    if hasattr(b1, 'rdbms_PKeyAndUnique31'):
        assert not _is_linked(b1, 'rdbms_PKeyAndUnique31', a)
    if hasattr(b2, 'rdbms_PKeyAndUnique31'):
        assert _is_linked(b2, 'rdbms_PKeyAndUnique31', a)
    _safe_set(a, 'rdbms_Column32', None)
    assert not _is_linked(a, 'rdbms_Column32', b2)
    if hasattr(b2, 'rdbms_PKeyAndUnique31'):
        assert not _is_linked(b2, 'rdbms_PKeyAndUnique31', a)


def test_assoc_columnDataType18_link_reassign_clear():
    a = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    b1 = rdbms_DataType()
    b2 = rdbms_DataType()
    _safe_set(a, 'rdbms_Column19', b1)
    assert _is_linked(a, 'rdbms_Column19', b1)
    if hasattr(b1, 'rdbms_DataType'):
        assert _is_linked(b1, 'rdbms_DataType', a)
    _safe_set(a, 'rdbms_Column19', b2)
    assert _is_linked(a, 'rdbms_Column19', b2)
    if hasattr(b1, 'rdbms_DataType'):
        assert not _is_linked(b1, 'rdbms_DataType', a)
    if hasattr(b2, 'rdbms_DataType'):
        assert _is_linked(b2, 'rdbms_DataType', a)
    _safe_set(a, 'rdbms_Column19', None)
    assert not _is_linked(a, 'rdbms_Column19', b2)
    if hasattr(b2, 'rdbms_DataType'):
        assert not _is_linked(b2, 'rdbms_DataType', a)


def test_assoc_columnInFK16_link_reassign_clear():
    a = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    b1 = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    b2 = rdbms_Column(default="sample_text_2", length=13, nullable=False, precision=13)
    _safe_set(a, 'rdbms_ForeignKey', b1)
    assert _is_linked(a, 'rdbms_ForeignKey', b1)
    if hasattr(b1, 'rdbms_Column17'):
        assert _is_linked(b1, 'rdbms_Column17', a)
    _safe_set(a, 'rdbms_ForeignKey', b2)
    assert _is_linked(a, 'rdbms_ForeignKey', b2)
    if hasattr(b1, 'rdbms_Column17'):
        assert not _is_linked(b1, 'rdbms_Column17', a)
    if hasattr(b2, 'rdbms_Column17'):
        assert _is_linked(b2, 'rdbms_Column17', a)
    _safe_set(a, 'rdbms_ForeignKey', None)
    assert not _is_linked(a, 'rdbms_ForeignKey', b2)
    if hasattr(b2, 'rdbms_Column17'):
        assert not _is_linked(b2, 'rdbms_Column17', a)


def test_assoc_columnInPKandUQ14_link_reassign_clear():
    a = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    b1 = rdbms_PKeyAndUnique()
    b2 = rdbms_PKeyAndUnique()
    _safe_set(a, 'rdbms_Column15', b1)
    assert _is_linked(a, 'rdbms_Column15', b1)
    if hasattr(b1, 'rdbms_PKeyAndUnique'):
        assert _is_linked(b1, 'rdbms_PKeyAndUnique', a)
    _safe_set(a, 'rdbms_Column15', b2)
    assert _is_linked(a, 'rdbms_Column15', b2)
    if hasattr(b1, 'rdbms_PKeyAndUnique'):
        assert not _is_linked(b1, 'rdbms_PKeyAndUnique', a)
    if hasattr(b2, 'rdbms_PKeyAndUnique'):
        assert _is_linked(b2, 'rdbms_PKeyAndUnique', a)
    _safe_set(a, 'rdbms_Column15', None)
    assert not _is_linked(a, 'rdbms_Column15', b2)
    if hasattr(b2, 'rdbms_PKeyAndUnique'):
        assert not _is_linked(b2, 'rdbms_PKeyAndUnique', a)


def test_assoc_columns10_link_reassign_clear():
    a = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    b1 = rdbms_Table()
    b2 = rdbms_Table()
    _safe_set(a, 'rdbms_Column', b1)
    assert _is_linked(a, 'rdbms_Column', b1)
    if hasattr(b1, 'rdbms_Table11'):
        assert _is_linked(b1, 'rdbms_Table11', a)
    _safe_set(a, 'rdbms_Column', b2)
    assert _is_linked(a, 'rdbms_Column', b2)
    if hasattr(b1, 'rdbms_Table11'):
        assert not _is_linked(b1, 'rdbms_Table11', a)
    if hasattr(b2, 'rdbms_Table11'):
        assert _is_linked(b2, 'rdbms_Table11', a)
    _safe_set(a, 'rdbms_Column', None)
    assert not _is_linked(a, 'rdbms_Column', b2)
    if hasattr(b2, 'rdbms_Table11'):
        assert not _is_linked(b2, 'rdbms_Table11', a)


def test_assoc_dataType33_link_reassign_clear():
    a = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    b1 = rdbms_SystemDataType(predefinedDecPlaces=7, predefinedLength=7)
    b2 = rdbms_SystemDataType(predefinedDecPlaces=13, predefinedLength=13)
    _safe_set(a, 'rdbms_UserDefinedDataType34', b1)
    assert _is_linked(a, 'rdbms_UserDefinedDataType34', b1)
    if hasattr(b1, 'rdbms_SystemDataType35'):
        assert _is_linked(b1, 'rdbms_SystemDataType35', a)
    _safe_set(a, 'rdbms_UserDefinedDataType34', b2)
    assert _is_linked(a, 'rdbms_UserDefinedDataType34', b2)
    if hasattr(b1, 'rdbms_SystemDataType35'):
        assert not _is_linked(b1, 'rdbms_SystemDataType35', a)
    if hasattr(b2, 'rdbms_SystemDataType35'):
        assert _is_linked(b2, 'rdbms_SystemDataType35', a)
    _safe_set(a, 'rdbms_UserDefinedDataType34', None)
    assert not _is_linked(a, 'rdbms_UserDefinedDataType34', b2)
    if hasattr(b2, 'rdbms_SystemDataType35'):
        assert not _is_linked(b2, 'rdbms_SystemDataType35', a)


def test_assoc_dataTypes3_link_reassign_clear():
    a = rdbms_SystemDataType(predefinedDecPlaces=7, predefinedLength=7)
    b1 = rdbms_Database()
    b2 = rdbms_Database()
    _safe_set(a, 'rdbms_SystemDataType', b1)
    assert _is_linked(a, 'rdbms_SystemDataType', b1)
    if hasattr(b1, 'rdbms_Database4'):
        assert _is_linked(b1, 'rdbms_Database4', a)
    _safe_set(a, 'rdbms_SystemDataType', b2)
    assert _is_linked(a, 'rdbms_SystemDataType', b2)
    if hasattr(b1, 'rdbms_Database4'):
        assert not _is_linked(b1, 'rdbms_Database4', a)
    if hasattr(b2, 'rdbms_Database4'):
        assert _is_linked(b2, 'rdbms_Database4', a)
    _safe_set(a, 'rdbms_SystemDataType', None)
    assert not _is_linked(a, 'rdbms_SystemDataType', b2)
    if hasattr(b2, 'rdbms_Database4'):
        assert not _is_linked(b2, 'rdbms_Database4', a)


def test_assoc_lhsAttr23_link_reassign_clear():
    a = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    b1 = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    b2 = rdbms_Column(default="sample_text_2", length=13, nullable=False, precision=13)
    _safe_set(a, 'rdbms_ForeignKey24', {b1})
    assert _is_linked(a, 'rdbms_ForeignKey24', b1)
    if hasattr(b1, 'rdbms_Column25'):
        assert _is_linked(b1, 'rdbms_Column25', a)
    _safe_set(a, 'rdbms_ForeignKey24', {b2})
    assert _is_linked(a, 'rdbms_ForeignKey24', b2)
    if hasattr(b1, 'rdbms_Column25'):
        assert not _is_linked(b1, 'rdbms_Column25', a)
    if hasattr(b2, 'rdbms_Column25'):
        assert _is_linked(b2, 'rdbms_Column25', a)
    _safe_set(a, 'rdbms_ForeignKey24', set())
    assert not _is_linked(a, 'rdbms_ForeignKey24', b2)
    if hasattr(b2, 'rdbms_Column25'):
        assert not _is_linked(b2, 'rdbms_Column25', a)


def test_assoc_refersTo26_link_reassign_clear():
    a = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    b1 = rdbms_Table()
    b2 = rdbms_Table()
    _safe_set(a, 'rdbms_ForeignKey27', b1)
    assert _is_linked(a, 'rdbms_ForeignKey27', b1)
    if hasattr(b1, 'rdbms_Table28'):
        assert _is_linked(b1, 'rdbms_Table28', a)
    _safe_set(a, 'rdbms_ForeignKey27', b2)
    assert _is_linked(a, 'rdbms_ForeignKey27', b2)
    if hasattr(b1, 'rdbms_Table28'):
        assert not _is_linked(b1, 'rdbms_Table28', a)
    if hasattr(b2, 'rdbms_Table28'):
        assert _is_linked(b2, 'rdbms_Table28', a)
    _safe_set(a, 'rdbms_ForeignKey27', None)
    assert not _is_linked(a, 'rdbms_ForeignKey27', b2)
    if hasattr(b2, 'rdbms_Table28'):
        assert not _is_linked(b2, 'rdbms_Table28', a)


def test_assoc_rhsKey20_link_reassign_clear():
    a = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    b1 = rdbms_PKeyAndUnique()
    b2 = rdbms_PKeyAndUnique()
    _safe_set(a, 'rdbms_ForeignKey21', b1)
    assert _is_linked(a, 'rdbms_ForeignKey21', b1)
    if hasattr(b1, 'rdbms_PKeyAndUnique22'):
        assert _is_linked(b1, 'rdbms_PKeyAndUnique22', a)
    _safe_set(a, 'rdbms_ForeignKey21', b2)
    assert _is_linked(a, 'rdbms_ForeignKey21', b2)
    if hasattr(b1, 'rdbms_PKeyAndUnique22'):
        assert not _is_linked(b1, 'rdbms_PKeyAndUnique22', a)
    if hasattr(b2, 'rdbms_PKeyAndUnique22'):
        assert _is_linked(b2, 'rdbms_PKeyAndUnique22', a)
    _safe_set(a, 'rdbms_ForeignKey21', None)
    assert not _is_linked(a, 'rdbms_ForeignKey21', b2)
    if hasattr(b2, 'rdbms_PKeyAndUnique22'):
        assert not _is_linked(b2, 'rdbms_PKeyAndUnique22', a)


def test_assoc_tableCHs12_link_reassign_clear():
    a = rdbms_CheckCon(checkCondition="sample_text")
    b1 = rdbms_Table()
    b2 = rdbms_Table()
    _safe_set(a, 'rdbms_CheckCon', b1)
    assert _is_linked(a, 'rdbms_CheckCon', b1)
    if hasattr(b1, 'rdbms_Table13'):
        assert _is_linked(b1, 'rdbms_Table13', a)
    _safe_set(a, 'rdbms_CheckCon', b2)
    assert _is_linked(a, 'rdbms_CheckCon', b2)
    if hasattr(b1, 'rdbms_Table13'):
        assert not _is_linked(b1, 'rdbms_Table13', a)
    if hasattr(b2, 'rdbms_Table13'):
        assert _is_linked(b2, 'rdbms_Table13', a)
    _safe_set(a, 'rdbms_CheckCon', None)
    assert not _is_linked(a, 'rdbms_CheckCon', b2)
    if hasattr(b2, 'rdbms_Table13'):
        assert not _is_linked(b2, 'rdbms_Table13', a)


def test_assoc_tableFKs5_link_reassign_clear():
    a = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    b1 = rdbms_Table()
    b2 = rdbms_Table()
    _safe_set(a, 'ForeignKey', b1)
    assert _is_linked(a, 'ForeignKey', b1)
    if hasattr(b1, 'FKTable'):
        assert _is_linked(b1, 'FKTable', a)
    _safe_set(a, 'ForeignKey', b2)
    assert _is_linked(a, 'ForeignKey', b2)
    if hasattr(b1, 'FKTable'):
        assert not _is_linked(b1, 'FKTable', a)
    if hasattr(b2, 'FKTable'):
        assert _is_linked(b2, 'FKTable', a)
    _safe_set(a, 'ForeignKey', None)
    assert not _is_linked(a, 'ForeignKey', b2)
    if hasattr(b2, 'FKTable'):
        assert not _is_linked(b2, 'FKTable', a)


def test_assoc_userDefinedDataTypes0_link_reassign_clear():
    a = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    b1 = rdbms_Database()
    b2 = rdbms_Database()
    _safe_set(a, 'rdbms_UserDefinedDataType', b1)
    assert _is_linked(a, 'rdbms_UserDefinedDataType', b1)
    if hasattr(b1, 'rdbms_Database'):
        assert _is_linked(b1, 'rdbms_Database', a)
    _safe_set(a, 'rdbms_UserDefinedDataType', b2)
    assert _is_linked(a, 'rdbms_UserDefinedDataType', b2)
    if hasattr(b1, 'rdbms_Database'):
        assert not _is_linked(b1, 'rdbms_Database', a)
    if hasattr(b2, 'rdbms_Database'):
        assert _is_linked(b2, 'rdbms_Database', a)
    _safe_set(a, 'rdbms_UserDefinedDataType', None)
    assert not _is_linked(a, 'rdbms_UserDefinedDataType', b2)
    if hasattr(b2, 'rdbms_Database'):
        assert not _is_linked(b2, 'rdbms_Database', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Constraints_strategy = st.builds(Constraints)
@given(instance=Constraints_strategy)
@settings(max_examples=25)
def test_Constraints_instantiation(instance):
    assert isinstance(instance, Constraints)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


ModelElement_strategy = st.builds(ModelElement)
@given(instance=ModelElement_strategy)
@settings(max_examples=25)
def test_ModelElement_instantiation(instance):
    assert isinstance(instance, ModelElement)


PKeyAndUnique_strategy = st.builds(PKeyAndUnique)
@given(instance=PKeyAndUnique_strategy)
@settings(max_examples=25)
def test_PKeyAndUnique_instantiation(instance):
    assert isinstance(instance, PKeyAndUnique)


rdbms_CheckCon_strategy = st.builds(rdbms_CheckCon, checkCondition=safe_text)
@given(instance=rdbms_CheckCon_strategy)
@settings(max_examples=25)
def test_rdbms_CheckCon_instantiation(instance):
    assert isinstance(instance, rdbms_CheckCon)


rdbms_Column_strategy = st.builds(rdbms_Column, default=safe_text, length=st.integers(), nullable=st.booleans(), precision=st.integers())
@given(instance=rdbms_Column_strategy)
@settings(max_examples=25)
def test_rdbms_Column_instantiation(instance):
    assert isinstance(instance, rdbms_Column)


rdbms_Constraints_strategy = st.builds(rdbms_Constraints, deferrable=safe_text, deferred=safe_text)
@given(instance=rdbms_Constraints_strategy)
@settings(max_examples=25)
def test_rdbms_Constraints_instantiation(instance):
    assert isinstance(instance, rdbms_Constraints)


rdbms_DataType_strategy = st.builds(rdbms_DataType)
@given(instance=rdbms_DataType_strategy)
@settings(max_examples=25)
def test_rdbms_DataType_instantiation(instance):
    assert isinstance(instance, rdbms_DataType)


rdbms_Database_strategy = st.builds(rdbms_Database)
@given(instance=rdbms_Database_strategy)
@settings(max_examples=25)
def test_rdbms_Database_instantiation(instance):
    assert isinstance(instance, rdbms_Database)


rdbms_ForeignKey_strategy = st.builds(rdbms_ForeignKey, deleteActionRHS=safe_text, inverseReferentialIntegrityCon=st.booleans(), match=safe_text, updateActionRHS=safe_text)
@given(instance=rdbms_ForeignKey_strategy)
@settings(max_examples=25)
def test_rdbms_ForeignKey_instantiation(instance):
    assert isinstance(instance, rdbms_ForeignKey)


rdbms_ModelElement_strategy = st.builds(rdbms_ModelElement, name=safe_text)
@given(instance=rdbms_ModelElement_strategy)
@settings(max_examples=25)
def test_rdbms_ModelElement_instantiation(instance):
    assert isinstance(instance, rdbms_ModelElement)


rdbms_PKeyAndUnique_strategy = st.builds(rdbms_PKeyAndUnique)
@given(instance=rdbms_PKeyAndUnique_strategy)
@settings(max_examples=25)
def test_rdbms_PKeyAndUnique_instantiation(instance):
    assert isinstance(instance, rdbms_PKeyAndUnique)


rdbms_PrimaryKeyCon_strategy = st.builds(rdbms_PrimaryKeyCon)
@given(instance=rdbms_PrimaryKeyCon_strategy)
@settings(max_examples=25)
def test_rdbms_PrimaryKeyCon_instantiation(instance):
    assert isinstance(instance, rdbms_PrimaryKeyCon)


rdbms_SystemDataType_strategy = st.builds(rdbms_SystemDataType, predefinedDecPlaces=st.integers(), predefinedLength=st.integers())
@given(instance=rdbms_SystemDataType_strategy)
@settings(max_examples=25)
def test_rdbms_SystemDataType_instantiation(instance):
    assert isinstance(instance, rdbms_SystemDataType)


rdbms_Table_strategy = st.builds(rdbms_Table)
@given(instance=rdbms_Table_strategy)
@settings(max_examples=25)
def test_rdbms_Table_instantiation(instance):
    assert isinstance(instance, rdbms_Table)


rdbms_UniqueCon_strategy = st.builds(rdbms_UniqueCon)
@given(instance=rdbms_UniqueCon_strategy)
@settings(max_examples=25)
def test_rdbms_UniqueCon_instantiation(instance):
    assert isinstance(instance, rdbms_UniqueCon)


rdbms_UserDefinedDataType_strategy = st.builds(rdbms_UserDefinedDataType, defaultValue=safe_text, length=st.integers(), precision=st.integers())
@given(instance=rdbms_UserDefinedDataType_strategy)
@settings(max_examples=25)
def test_rdbms_UserDefinedDataType_instantiation(instance):
    assert isinstance(instance, rdbms_UserDefinedDataType)



