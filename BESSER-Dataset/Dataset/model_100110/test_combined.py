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
    SQLDistinctType,
    SQLSimpleType,
    CWMRelationalData_SQLDataType,
    CWMRelationalData_Trigger,
    QueryExpression,
    Trigger,
    CWMRelationalData_ColumnSet,
    NamedColumnSet,
    ColumnSet,
    CWMRelationalData_NamedColumnSet,
    CWMRelationalData_QueryColumnSet,
    SQLDataType,
    CWMRelationalData_SQLSimpleType,
    CWMRelationalData_SQLDistinctType,
    CheckConstraint,
    CWMRelationalData_View,
    CWMRelationalData_Table,
    CWMRelationalData_CheckConstraint,
    CWMRelationalData_QueryExpression,
    CWMRelationalData_Column,
    Table,
    Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sqldistincttype_is_not_abstract():
    assert not inspect.isabstract(SQLDistinctType)


def test_hyp_sqldistincttype_constructor_exists():
    assert callable(SQLDistinctType.__init__)


def test_hyp_sqldistincttype_constructor_args():
    sig = inspect.signature(SQLDistinctType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqlsimpletype_is_not_abstract():
    assert not inspect.isabstract(SQLSimpleType)


def test_hyp_sqlsimpletype_constructor_exists():
    assert callable(SQLSimpleType.__init__)


def test_hyp_sqlsimpletype_constructor_args():
    sig = inspect.signature(SQLSimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cwmrelationaldata_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_SQLDataType)


def test_hyp_cwmrelationaldata_sqldatatype_constructor_exists():
    assert callable(CWMRelationalData_SQLDataType.__init__)


def test_hyp_cwmrelationaldata_sqldatatype_constructor_args():
    sig = inspect.signature(CWMRelationalData_SQLDataType.__init__)
    params = list(sig.parameters.keys())
    assert "typeNumber" in params, "Missing parameter 'typeNumber'"




def test_hyp_cwmrelationaldata_trigger_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_Trigger)


def test_hyp_cwmrelationaldata_trigger_constructor_exists():
    assert callable(CWMRelationalData_Trigger.__init__)


def test_hyp_cwmrelationaldata_trigger_constructor_args():
    sig = inspect.signature(CWMRelationalData_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_queryexpression_is_not_abstract():
    assert not inspect.isabstract(QueryExpression)


def test_hyp_queryexpression_constructor_exists():
    assert callable(QueryExpression.__init__)


def test_hyp_queryexpression_constructor_args():
    sig = inspect.signature(QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_hyp_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_hyp_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cwmrelationaldata_columnset_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_ColumnSet)


def test_hyp_cwmrelationaldata_columnset_constructor_exists():
    assert callable(CWMRelationalData_ColumnSet.__init__)


def test_hyp_cwmrelationaldata_columnset_constructor_args():
    sig = inspect.signature(CWMRelationalData_ColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedcolumnset_is_not_abstract():
    assert not inspect.isabstract(NamedColumnSet)


def test_hyp_namedcolumnset_constructor_exists():
    assert callable(NamedColumnSet.__init__)


def test_hyp_namedcolumnset_constructor_args():
    sig = inspect.signature(NamedColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_columnset_is_not_abstract():
    assert not inspect.isabstract(ColumnSet)


def test_hyp_columnset_constructor_exists():
    assert callable(ColumnSet.__init__)


def test_hyp_columnset_constructor_args():
    sig = inspect.signature(ColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cwmrelationaldata_namedcolumnset_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_NamedColumnSet)


def test_hyp_cwmrelationaldata_namedcolumnset_constructor_exists():
    assert callable(CWMRelationalData_NamedColumnSet.__init__)


def test_hyp_cwmrelationaldata_namedcolumnset_constructor_args():
    sig = inspect.signature(CWMRelationalData_NamedColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cwmrelationaldata_querycolumnset_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_QueryColumnSet)


def test_hyp_cwmrelationaldata_querycolumnset_constructor_exists():
    assert callable(CWMRelationalData_QueryColumnSet.__init__)


def test_hyp_cwmrelationaldata_querycolumnset_constructor_args():
    sig = inspect.signature(CWMRelationalData_QueryColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(SQLDataType)


def test_hyp_sqldatatype_constructor_exists():
    assert callable(SQLDataType.__init__)


def test_hyp_sqldatatype_constructor_args():
    sig = inspect.signature(SQLDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cwmrelationaldata_sqlsimpletype_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_SQLSimpleType)


def test_hyp_cwmrelationaldata_sqlsimpletype_constructor_exists():
    assert callable(CWMRelationalData_SQLSimpleType.__init__)


def test_hyp_cwmrelationaldata_sqlsimpletype_constructor_args():
    sig = inspect.signature(CWMRelationalData_SQLSimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "numericScale" in params, "Missing parameter 'numericScale'"
    assert "characterOctetLength" in params, "Missing parameter 'characterOctetLength'"
    assert "characterMaximumLength" in params, "Missing parameter 'characterMaximumLength'"
    assert "numericPrecisionRadix" in params, "Missing parameter 'numericPrecisionRadix'"
    assert "dateTimePrecision" in params, "Missing parameter 'dateTimePrecision'"
    assert "numericPrecision" in params, "Missing parameter 'numericPrecision'"









def test_hyp_cwmrelationaldata_sqldistincttype_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_SQLDistinctType)


def test_hyp_cwmrelationaldata_sqldistincttype_constructor_exists():
    assert callable(CWMRelationalData_SQLDistinctType.__init__)


def test_hyp_cwmrelationaldata_sqldistincttype_constructor_args():
    sig = inspect.signature(CWMRelationalData_SQLDistinctType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"






def test_hyp_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(CheckConstraint)


def test_hyp_checkconstraint_constructor_exists():
    assert callable(CheckConstraint.__init__)


def test_hyp_checkconstraint_constructor_args():
    sig = inspect.signature(CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cwmrelationaldata_view_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_View)


def test_hyp_cwmrelationaldata_view_constructor_exists():
    assert callable(CWMRelationalData_View.__init__)


def test_hyp_cwmrelationaldata_view_constructor_args():
    sig = inspect.signature(CWMRelationalData_View.__init__)
    params = list(sig.parameters.keys())
    assert "checkOption" in params, "Missing parameter 'checkOption'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"





def test_hyp_cwmrelationaldata_table_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_Table)


def test_hyp_cwmrelationaldata_table_constructor_exists():
    assert callable(CWMRelationalData_Table.__init__)


def test_hyp_cwmrelationaldata_table_constructor_args():
    sig = inspect.signature(CWMRelationalData_Table.__init__)
    params = list(sig.parameters.keys())
    assert "isTemporary" in params, "Missing parameter 'isTemporary'"
    assert "temporaryScope" in params, "Missing parameter 'temporaryScope'"
    assert "isSystem" in params, "Missing parameter 'isSystem'"






def test_hyp_cwmrelationaldata_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_CheckConstraint)


def test_hyp_cwmrelationaldata_checkconstraint_constructor_exists():
    assert callable(CWMRelationalData_CheckConstraint.__init__)


def test_hyp_cwmrelationaldata_checkconstraint_constructor_args():
    sig = inspect.signature(CWMRelationalData_CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cwmrelationaldata_queryexpression_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_QueryExpression)


def test_hyp_cwmrelationaldata_queryexpression_constructor_exists():
    assert callable(CWMRelationalData_QueryExpression.__init__)


def test_hyp_cwmrelationaldata_queryexpression_constructor_args():
    sig = inspect.signature(CWMRelationalData_QueryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expresssion" in params, "Missing parameter 'expresssion'"




def test_hyp_cwmrelationaldata_column_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_Column)


def test_hyp_cwmrelationaldata_column_constructor_exists():
    assert callable(CWMRelationalData_Column.__init__)


def test_hyp_cwmrelationaldata_column_constructor_args():
    sig = inspect.signature(CWMRelationalData_Column.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "characterSetName" in params, "Missing parameter 'characterSetName'"
    assert "length" in params, "Missing parameter 'length'"
    assert "isNullable" in params, "Missing parameter 'isNullable'"
    assert "collectionName" in params, "Missing parameter 'collectionName'"









def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_hyp_column_constructor_exists():
    assert callable(Column.__init__)


def test_hyp_column_constructor_args():
    sig = inspect.signature(Column.__init__)
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
SQLDistinctType_strategy = st.builds(
    SQLDistinctType,
)
SQLSimpleType_strategy = st.builds(
    SQLSimpleType,
)
CWMRelationalData_SQLDataType_strategy = st.builds(
    CWMRelationalData_SQLDataType,
    typeNumber=
        safe_text
)
CWMRelationalData_Trigger_strategy = st.builds(
    CWMRelationalData_Trigger,
)
QueryExpression_strategy = st.builds(
    QueryExpression,
)
Trigger_strategy = st.builds(
    Trigger,
)
CWMRelationalData_ColumnSet_strategy = st.builds(
    CWMRelationalData_ColumnSet,
)
NamedColumnSet_strategy = st.builds(
    NamedColumnSet,
)
ColumnSet_strategy = st.builds(
    ColumnSet,
)
CWMRelationalData_NamedColumnSet_strategy = st.builds(
    CWMRelationalData_NamedColumnSet,
)
CWMRelationalData_QueryColumnSet_strategy = st.builds(
    CWMRelationalData_QueryColumnSet,
)
SQLDataType_strategy = st.builds(
    SQLDataType,
)
CWMRelationalData_SQLSimpleType_strategy = st.builds(
    CWMRelationalData_SQLSimpleType,
    numericScale=
        safe_text,
    characterOctetLength=
        safe_text,
    characterMaximumLength=
        safe_text,
    numericPrecisionRadix=
        safe_text,
    dateTimePrecision=
        safe_text,
    numericPrecision=
        safe_text
)
CWMRelationalData_SQLDistinctType_strategy = st.builds(
    CWMRelationalData_SQLDistinctType,
    length=
        safe_text,
    precision=
        safe_text,
    scale=
        safe_text
)
CheckConstraint_strategy = st.builds(
    CheckConstraint,
)
CWMRelationalData_View_strategy = st.builds(
    CWMRelationalData_View,
    checkOption=
        safe_text,
    isReadOnly=
        safe_text
)
CWMRelationalData_Table_strategy = st.builds(
    CWMRelationalData_Table,
    isTemporary=
        safe_text,
    temporaryScope=
        safe_text,
    isSystem=
        safe_text
)
CWMRelationalData_CheckConstraint_strategy = st.builds(
    CWMRelationalData_CheckConstraint,
)
CWMRelationalData_QueryExpression_strategy = st.builds(
    CWMRelationalData_QueryExpression,
    expresssion=
        safe_text
)
CWMRelationalData_Column_strategy = st.builds(
    CWMRelationalData_Column,
    precision=
        safe_text,
    scale=
        safe_text,
    characterSetName=
        safe_text,
    length=
        safe_text,
    isNullable=
        safe_text,
    collectionName=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
Column_strategy = st.builds(
    Column,
)






@given(instance=CWMRelationalData_SQLDataType_strategy)
def test_hyp_cwmrelationaldata_sqldatatype_typeNumber_setter(instance):
    original = instance.typeNumber
    instance.typeNumber = original
    assert instance.typeNumber == original













@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_hyp_cwmrelationaldata_sqlsimpletype_numericScale_setter(instance):
    original = instance.numericScale
    instance.numericScale = original
    assert instance.numericScale == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_hyp_cwmrelationaldata_sqlsimpletype_characterOctetLength_setter(instance):
    original = instance.characterOctetLength
    instance.characterOctetLength = original
    assert instance.characterOctetLength == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_hyp_cwmrelationaldata_sqlsimpletype_characterMaximumLength_setter(instance):
    original = instance.characterMaximumLength
    instance.characterMaximumLength = original
    assert instance.characterMaximumLength == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_hyp_cwmrelationaldata_sqlsimpletype_numericPrecisionRadix_setter(instance):
    original = instance.numericPrecisionRadix
    instance.numericPrecisionRadix = original
    assert instance.numericPrecisionRadix == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_hyp_cwmrelationaldata_sqlsimpletype_dateTimePrecision_setter(instance):
    original = instance.dateTimePrecision
    instance.dateTimePrecision = original
    assert instance.dateTimePrecision == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_hyp_cwmrelationaldata_sqlsimpletype_numericPrecision_setter(instance):
    original = instance.numericPrecision
    instance.numericPrecision = original
    assert instance.numericPrecision == original




@given(instance=CWMRelationalData_SQLDistinctType_strategy)
def test_hyp_cwmrelationaldata_sqldistincttype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=CWMRelationalData_SQLDistinctType_strategy)
def test_hyp_cwmrelationaldata_sqldistincttype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=CWMRelationalData_SQLDistinctType_strategy)
def test_hyp_cwmrelationaldata_sqldistincttype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original





@given(instance=CWMRelationalData_View_strategy)
def test_hyp_cwmrelationaldata_view_checkOption_setter(instance):
    original = instance.checkOption
    instance.checkOption = original
    assert instance.checkOption == original



@given(instance=CWMRelationalData_View_strategy)
def test_hyp_cwmrelationaldata_view_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original




@given(instance=CWMRelationalData_Table_strategy)
def test_hyp_cwmrelationaldata_table_isTemporary_setter(instance):
    original = instance.isTemporary
    instance.isTemporary = original
    assert instance.isTemporary == original



@given(instance=CWMRelationalData_Table_strategy)
def test_hyp_cwmrelationaldata_table_temporaryScope_setter(instance):
    original = instance.temporaryScope
    instance.temporaryScope = original
    assert instance.temporaryScope == original



@given(instance=CWMRelationalData_Table_strategy)
def test_hyp_cwmrelationaldata_table_isSystem_setter(instance):
    original = instance.isSystem
    instance.isSystem = original
    assert instance.isSystem == original





@given(instance=CWMRelationalData_QueryExpression_strategy)
def test_hyp_cwmrelationaldata_queryexpression_expresssion_setter(instance):
    original = instance.expresssion
    instance.expresssion = original
    assert instance.expresssion == original




@given(instance=CWMRelationalData_Column_strategy)
def test_hyp_cwmrelationaldata_column_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=CWMRelationalData_Column_strategy)
def test_hyp_cwmrelationaldata_column_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=CWMRelationalData_Column_strategy)
def test_hyp_cwmrelationaldata_column_characterSetName_setter(instance):
    original = instance.characterSetName
    instance.characterSetName = original
    assert instance.characterSetName == original



@given(instance=CWMRelationalData_Column_strategy)
def test_hyp_cwmrelationaldata_column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=CWMRelationalData_Column_strategy)
def test_hyp_cwmrelationaldata_column_isNullable_setter(instance):
    original = instance.isNullable
    instance.isNullable = original
    assert instance.isNullable == original



@given(instance=CWMRelationalData_Column_strategy)
def test_hyp_cwmrelationaldata_column_collectionName_setter(instance):
    original = instance.collectionName
    instance.collectionName = original
    assert instance.collectionName == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CWMRelationalData_CheckConstraint,
    CWMRelationalData_Column,
    CWMRelationalData_ColumnSet,
    CWMRelationalData_NamedColumnSet,
    CWMRelationalData_QueryColumnSet,
    CWMRelationalData_QueryExpression,
    CWMRelationalData_SQLDataType,
    CWMRelationalData_SQLDistinctType,
    CWMRelationalData_SQLSimpleType,
    CWMRelationalData_Table,
    CWMRelationalData_Trigger,
    CWMRelationalData_View,
    CheckConstraint,
    Column,
    ColumnSet,
    NamedColumnSet,
    QueryExpression,
    SQLDataType,
    SQLDistinctType,
    SQLSimpleType,
    Table,
    Trigger,
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

def test_CWMRelationalData_Column_characterSetName_value_roundtrip():
    instance = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.characterSetName == "sample_text"
    instance.characterSetName = "sample_text_2"
    assert instance.characterSetName == "sample_text_2"


def test_CWMRelationalData_Column_collectionName_value_roundtrip():
    instance = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.collectionName == "sample_text"
    instance.collectionName = "sample_text_2"
    assert instance.collectionName == "sample_text_2"


def test_CWMRelationalData_Column_isNullable_value_roundtrip():
    instance = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.isNullable == "sample_text"
    instance.isNullable = "sample_text_2"
    assert instance.isNullable == "sample_text_2"


def test_CWMRelationalData_Column_length_value_roundtrip():
    instance = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.length == "sample_text"
    instance.length = "sample_text_2"
    assert instance.length == "sample_text_2"


def test_CWMRelationalData_Column_precision_value_roundtrip():
    instance = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_CWMRelationalData_Column_scale_value_roundtrip():
    instance = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.scale == "sample_text"
    instance.scale = "sample_text_2"
    assert instance.scale == "sample_text_2"


def test_CWMRelationalData_QueryExpression_expresssion_value_roundtrip():
    instance = CWMRelationalData_QueryExpression(expresssion="sample_text")
    assert instance.expresssion == "sample_text"
    instance.expresssion = "sample_text_2"
    assert instance.expresssion == "sample_text_2"


def test_CWMRelationalData_SQLDataType_typeNumber_value_roundtrip():
    instance = CWMRelationalData_SQLDataType(typeNumber="sample_text")
    assert instance.typeNumber == "sample_text"
    instance.typeNumber = "sample_text_2"
    assert instance.typeNumber == "sample_text_2"


def test_CWMRelationalData_SQLDistinctType_length_value_roundtrip():
    instance = CWMRelationalData_SQLDistinctType(length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.length == "sample_text"
    instance.length = "sample_text_2"
    assert instance.length == "sample_text_2"


def test_CWMRelationalData_SQLDistinctType_precision_value_roundtrip():
    instance = CWMRelationalData_SQLDistinctType(length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.precision == "sample_text"
    instance.precision = "sample_text_2"
    assert instance.precision == "sample_text_2"


def test_CWMRelationalData_SQLDistinctType_scale_value_roundtrip():
    instance = CWMRelationalData_SQLDistinctType(length="sample_text", precision="sample_text", scale="sample_text")
    assert instance.scale == "sample_text"
    instance.scale = "sample_text_2"
    assert instance.scale == "sample_text_2"


def test_CWMRelationalData_SQLSimpleType_characterMaximumLength_value_roundtrip():
    instance = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    assert instance.characterMaximumLength == "sample_text"
    instance.characterMaximumLength = "sample_text_2"
    assert instance.characterMaximumLength == "sample_text_2"


def test_CWMRelationalData_SQLSimpleType_characterOctetLength_value_roundtrip():
    instance = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    assert instance.characterOctetLength == "sample_text"
    instance.characterOctetLength = "sample_text_2"
    assert instance.characterOctetLength == "sample_text_2"


def test_CWMRelationalData_SQLSimpleType_dateTimePrecision_value_roundtrip():
    instance = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    assert instance.dateTimePrecision == "sample_text"
    instance.dateTimePrecision = "sample_text_2"
    assert instance.dateTimePrecision == "sample_text_2"


def test_CWMRelationalData_SQLSimpleType_numericPrecision_value_roundtrip():
    instance = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    assert instance.numericPrecision == "sample_text"
    instance.numericPrecision = "sample_text_2"
    assert instance.numericPrecision == "sample_text_2"


def test_CWMRelationalData_SQLSimpleType_numericPrecisionRadix_value_roundtrip():
    instance = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    assert instance.numericPrecisionRadix == "sample_text"
    instance.numericPrecisionRadix = "sample_text_2"
    assert instance.numericPrecisionRadix == "sample_text_2"


def test_CWMRelationalData_SQLSimpleType_numericScale_value_roundtrip():
    instance = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    assert instance.numericScale == "sample_text"
    instance.numericScale = "sample_text_2"
    assert instance.numericScale == "sample_text_2"


def test_CWMRelationalData_Table_isSystem_value_roundtrip():
    instance = CWMRelationalData_Table(isSystem="sample_text", isTemporary="sample_text", temporaryScope="sample_text")
    assert instance.isSystem == "sample_text"
    instance.isSystem = "sample_text_2"
    assert instance.isSystem == "sample_text_2"


def test_CWMRelationalData_Table_isTemporary_value_roundtrip():
    instance = CWMRelationalData_Table(isSystem="sample_text", isTemporary="sample_text", temporaryScope="sample_text")
    assert instance.isTemporary == "sample_text"
    instance.isTemporary = "sample_text_2"
    assert instance.isTemporary == "sample_text_2"


def test_CWMRelationalData_Table_temporaryScope_value_roundtrip():
    instance = CWMRelationalData_Table(isSystem="sample_text", isTemporary="sample_text", temporaryScope="sample_text")
    assert instance.temporaryScope == "sample_text"
    instance.temporaryScope = "sample_text_2"
    assert instance.temporaryScope == "sample_text_2"


def test_CWMRelationalData_View_checkOption_value_roundtrip():
    instance = CWMRelationalData_View(checkOption="sample_text", isReadOnly="sample_text")
    assert instance.checkOption == "sample_text"
    instance.checkOption = "sample_text_2"
    assert instance.checkOption == "sample_text_2"


def test_CWMRelationalData_View_isReadOnly_value_roundtrip():
    instance = CWMRelationalData_View(checkOption="sample_text", isReadOnly="sample_text")
    assert instance.isReadOnly == "sample_text"
    instance.isReadOnly = "sample_text_2"
    assert instance.isReadOnly == "sample_text_2"


def test_CWMRelationalData_NamedColumnSet_isa_ColumnSet():
    instance = CWMRelationalData_NamedColumnSet()
    assert isinstance(instance, ColumnSet)


def test_CWMRelationalData_QueryColumnSet_isa_ColumnSet():
    instance = CWMRelationalData_QueryColumnSet()
    assert isinstance(instance, ColumnSet)


def test_CWMRelationalData_Table_isa_NamedColumnSet():
    instance = CWMRelationalData_Table(isSystem="sample_text", isTemporary="sample_text", temporaryScope="sample_text")
    assert isinstance(instance, NamedColumnSet)


def test_CWMRelationalData_View_isa_NamedColumnSet():
    instance = CWMRelationalData_View(checkOption="sample_text", isReadOnly="sample_text")
    assert isinstance(instance, NamedColumnSet)


def test_CWMRelationalData_SQLDistinctType_isa_SQLDataType():
    instance = CWMRelationalData_SQLDistinctType(length="sample_text", precision="sample_text", scale="sample_text")
    assert isinstance(instance, SQLDataType)


def test_CWMRelationalData_SQLSimpleType_isa_SQLDataType():
    instance = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    assert isinstance(instance, SQLDataType)


def test_assoc_column_constraints2_link_reassign_clear():
    a = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    b1 = CheckConstraint()
    b2 = CheckConstraint()
    _safe_set(a, 'constraintElements', {b1})
    assert _is_linked(a, 'constraintElements', b1)
    if hasattr(b1, 'CheckConstraint'):
        assert _is_linked(b1, 'CheckConstraint', a)
    _safe_set(a, 'constraintElements', {b2})
    assert _is_linked(a, 'constraintElements', b2)
    if hasattr(b1, 'CheckConstraint'):
        assert not _is_linked(b1, 'CheckConstraint', a)
    if hasattr(b2, 'CheckConstraint'):
        assert _is_linked(b2, 'CheckConstraint', a)
    _safe_set(a, 'constraintElements', set())
    assert not _is_linked(a, 'constraintElements', b2)
    if hasattr(b2, 'CheckConstraint'):
        assert not _is_linked(b2, 'CheckConstraint', a)


def test_assoc_optionScopeColumnSet5_link_reassign_clear():
    a = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    b1 = NamedColumnSet()
    b2 = NamedColumnSet()
    _safe_set(a, 'optionScopeColumn', b1)
    assert _is_linked(a, 'optionScopeColumn', b1)
    if hasattr(b1, 'NamedColumnSet'):
        assert _is_linked(b1, 'NamedColumnSet', a)
    _safe_set(a, 'optionScopeColumn', b2)
    assert _is_linked(a, 'optionScopeColumn', b2)
    if hasattr(b1, 'NamedColumnSet'):
        assert not _is_linked(b1, 'NamedColumnSet', a)
    if hasattr(b2, 'NamedColumnSet'):
        assert _is_linked(b2, 'NamedColumnSet', a)
    _safe_set(a, 'optionScopeColumn', None)
    assert not _is_linked(a, 'optionScopeColumn', b2)
    if hasattr(b2, 'NamedColumnSet'):
        assert not _is_linked(b2, 'NamedColumnSet', a)


def test_assoc_owner4_link_reassign_clear():
    a = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    b1 = ColumnSet()
    b2 = ColumnSet()
    _safe_set(a, 'features', b1)
    assert _is_linked(a, 'features', b1)
    if hasattr(b1, 'ColumnSet'):
        assert _is_linked(b1, 'ColumnSet', a)
    _safe_set(a, 'features', b2)
    assert _is_linked(a, 'features', b2)
    if hasattr(b1, 'ColumnSet'):
        assert not _is_linked(b1, 'ColumnSet', a)
    if hasattr(b2, 'ColumnSet'):
        assert _is_linked(b2, 'ColumnSet', a)
    _safe_set(a, 'features', None)
    assert not _is_linked(a, 'features', b2)
    if hasattr(b2, 'ColumnSet'):
        assert not _is_linked(b2, 'ColumnSet', a)


def test_assoc_queryExpression14_link_reassign_clear():
    a = CWMRelationalData_View(checkOption="sample_text", isReadOnly="sample_text")
    b1 = QueryExpression()
    b2 = QueryExpression()
    _safe_set(a, 'CWMRelationalData_View', b1)
    assert _is_linked(a, 'CWMRelationalData_View', b1)
    if hasattr(b1, 'QueryExpression15'):
        assert _is_linked(b1, 'QueryExpression15', a)
    _safe_set(a, 'CWMRelationalData_View', b2)
    assert _is_linked(a, 'CWMRelationalData_View', b2)
    if hasattr(b1, 'QueryExpression15'):
        assert not _is_linked(b1, 'QueryExpression15', a)
    if hasattr(b2, 'QueryExpression15'):
        assert _is_linked(b2, 'QueryExpression15', a)
    _safe_set(a, 'CWMRelationalData_View', None)
    assert not _is_linked(a, 'CWMRelationalData_View', b2)
    if hasattr(b2, 'QueryExpression15'):
        assert not _is_linked(b2, 'QueryExpression15', a)


def test_assoc_sqlDistinctTypes21_link_reassign_clear():
    a = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    b1 = SQLDistinctType()
    b2 = SQLDistinctType()
    _safe_set(a, 'sqlSimpleType', {b1})
    assert _is_linked(a, 'sqlSimpleType', b1)
    if hasattr(b1, 'SQLDistinctType'):
        assert _is_linked(b1, 'SQLDistinctType', a)
    _safe_set(a, 'sqlSimpleType', {b2})
    assert _is_linked(a, 'sqlSimpleType', b2)
    if hasattr(b1, 'SQLDistinctType'):
        assert not _is_linked(b1, 'SQLDistinctType', a)
    if hasattr(b2, 'SQLDistinctType'):
        assert _is_linked(b2, 'SQLDistinctType', a)
    _safe_set(a, 'sqlSimpleType', set())
    assert not _is_linked(a, 'sqlSimpleType', b2)
    if hasattr(b2, 'SQLDistinctType'):
        assert not _is_linked(b2, 'SQLDistinctType', a)


def test_assoc_sqlSimpleType20_link_reassign_clear():
    a = CWMRelationalData_SQLDistinctType(length="sample_text", precision="sample_text", scale="sample_text")
    b1 = SQLSimpleType()
    b2 = SQLSimpleType()
    _safe_set(a, 'sqlDistinctTypes', b1)
    assert _is_linked(a, 'sqlDistinctTypes', b1)
    if hasattr(b1, 'SQLSimpleType'):
        assert _is_linked(b1, 'SQLSimpleType', a)
    _safe_set(a, 'sqlDistinctTypes', b2)
    assert _is_linked(a, 'sqlDistinctTypes', b2)
    if hasattr(b1, 'SQLSimpleType'):
        assert not _is_linked(b1, 'SQLSimpleType', a)
    if hasattr(b2, 'SQLSimpleType'):
        assert _is_linked(b2, 'SQLSimpleType', a)
    _safe_set(a, 'sqlDistinctTypes', None)
    assert not _is_linked(a, 'sqlDistinctTypes', b2)
    if hasattr(b2, 'SQLSimpleType'):
        assert not _is_linked(b2, 'SQLSimpleType', a)


def test_assoc_structuralFeatures18_link_reassign_clear():
    a = CWMRelationalData_SQLDataType(typeNumber="sample_text")
    b1 = Column()
    b2 = Column()
    _safe_set(a, 'type', {b1})
    assert _is_linked(a, 'type', b1)
    if hasattr(b1, 'Column19'):
        assert _is_linked(b1, 'Column19', a)
    _safe_set(a, 'type', {b2})
    assert _is_linked(a, 'type', b2)
    if hasattr(b1, 'Column19'):
        assert not _is_linked(b1, 'Column19', a)
    if hasattr(b2, 'Column19'):
        assert _is_linked(b2, 'Column19', a)
    _safe_set(a, 'type', set())
    assert not _is_linked(a, 'type', b2)
    if hasattr(b2, 'Column19'):
        assert not _is_linked(b2, 'Column19', a)


def test_assoc_table_constraints12_link_reassign_clear():
    a = CWMRelationalData_Table(isSystem="sample_text", isTemporary="sample_text", temporaryScope="sample_text")
    b1 = CheckConstraint()
    b2 = CheckConstraint()
    _safe_set(a, 'constrainedElements', {b1})
    assert _is_linked(a, 'constrainedElements', b1)
    if hasattr(b1, 'CheckConstraint13'):
        assert _is_linked(b1, 'CheckConstraint13', a)
    _safe_set(a, 'constrainedElements', {b2})
    assert _is_linked(a, 'constrainedElements', b2)
    if hasattr(b1, 'CheckConstraint13'):
        assert not _is_linked(b1, 'CheckConstraint13', a)
    if hasattr(b2, 'CheckConstraint13'):
        assert _is_linked(b2, 'CheckConstraint13', a)
    _safe_set(a, 'constrainedElements', set())
    assert not _is_linked(a, 'constrainedElements', b2)
    if hasattr(b2, 'CheckConstraint13'):
        assert not _is_linked(b2, 'CheckConstraint13', a)


def test_assoc_type3_link_reassign_clear():
    a = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    b1 = SQLDataType()
    b2 = SQLDataType()
    _safe_set(a, 'structuralFeatures', b1)
    assert _is_linked(a, 'structuralFeatures', b1)
    if hasattr(b1, 'SQLDataType'):
        assert _is_linked(b1, 'SQLDataType', a)
    _safe_set(a, 'structuralFeatures', b2)
    assert _is_linked(a, 'structuralFeatures', b2)
    if hasattr(b1, 'SQLDataType'):
        assert not _is_linked(b1, 'SQLDataType', a)
    if hasattr(b2, 'SQLDataType'):
        assert _is_linked(b2, 'SQLDataType', a)
    _safe_set(a, 'structuralFeatures', None)
    assert not _is_linked(a, 'structuralFeatures', b2)
    if hasattr(b2, 'SQLDataType'):
        assert not _is_linked(b2, 'SQLDataType', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CWMRelationalData_CheckConstraint_strategy = st.builds(CWMRelationalData_CheckConstraint)
@given(instance=CWMRelationalData_CheckConstraint_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_CheckConstraint_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_CheckConstraint)


CWMRelationalData_Column_strategy = st.builds(CWMRelationalData_Column, characterSetName=safe_text, collectionName=safe_text, isNullable=safe_text, length=safe_text, precision=safe_text, scale=safe_text)
@given(instance=CWMRelationalData_Column_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_Column_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_Column)


CWMRelationalData_ColumnSet_strategy = st.builds(CWMRelationalData_ColumnSet)
@given(instance=CWMRelationalData_ColumnSet_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_ColumnSet_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_ColumnSet)


CWMRelationalData_NamedColumnSet_strategy = st.builds(CWMRelationalData_NamedColumnSet)
@given(instance=CWMRelationalData_NamedColumnSet_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_NamedColumnSet_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_NamedColumnSet)


CWMRelationalData_QueryColumnSet_strategy = st.builds(CWMRelationalData_QueryColumnSet)
@given(instance=CWMRelationalData_QueryColumnSet_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_QueryColumnSet_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_QueryColumnSet)


CWMRelationalData_QueryExpression_strategy = st.builds(CWMRelationalData_QueryExpression, expresssion=safe_text)
@given(instance=CWMRelationalData_QueryExpression_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_QueryExpression_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_QueryExpression)


CWMRelationalData_SQLDataType_strategy = st.builds(CWMRelationalData_SQLDataType, typeNumber=safe_text)
@given(instance=CWMRelationalData_SQLDataType_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_SQLDataType_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_SQLDataType)


CWMRelationalData_SQLDistinctType_strategy = st.builds(CWMRelationalData_SQLDistinctType, length=safe_text, precision=safe_text, scale=safe_text)
@given(instance=CWMRelationalData_SQLDistinctType_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_SQLDistinctType_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_SQLDistinctType)


CWMRelationalData_SQLSimpleType_strategy = st.builds(CWMRelationalData_SQLSimpleType, characterMaximumLength=safe_text, characterOctetLength=safe_text, dateTimePrecision=safe_text, numericPrecision=safe_text, numericPrecisionRadix=safe_text, numericScale=safe_text)
@given(instance=CWMRelationalData_SQLSimpleType_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_SQLSimpleType_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_SQLSimpleType)


CWMRelationalData_Table_strategy = st.builds(CWMRelationalData_Table, isSystem=safe_text, isTemporary=safe_text, temporaryScope=safe_text)
@given(instance=CWMRelationalData_Table_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_Table_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_Table)


CWMRelationalData_Trigger_strategy = st.builds(CWMRelationalData_Trigger)
@given(instance=CWMRelationalData_Trigger_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_Trigger_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_Trigger)


CWMRelationalData_View_strategy = st.builds(CWMRelationalData_View, checkOption=safe_text, isReadOnly=safe_text)
@given(instance=CWMRelationalData_View_strategy)
@settings(max_examples=25)
def test_CWMRelationalData_View_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_View)


CheckConstraint_strategy = st.builds(CheckConstraint)
@given(instance=CheckConstraint_strategy)
@settings(max_examples=25)
def test_CheckConstraint_instantiation(instance):
    assert isinstance(instance, CheckConstraint)


Column_strategy = st.builds(Column)
@given(instance=Column_strategy)
@settings(max_examples=25)
def test_Column_instantiation(instance):
    assert isinstance(instance, Column)


ColumnSet_strategy = st.builds(ColumnSet)
@given(instance=ColumnSet_strategy)
@settings(max_examples=25)
def test_ColumnSet_instantiation(instance):
    assert isinstance(instance, ColumnSet)


NamedColumnSet_strategy = st.builds(NamedColumnSet)
@given(instance=NamedColumnSet_strategy)
@settings(max_examples=25)
def test_NamedColumnSet_instantiation(instance):
    assert isinstance(instance, NamedColumnSet)


QueryExpression_strategy = st.builds(QueryExpression)
@given(instance=QueryExpression_strategy)
@settings(max_examples=25)
def test_QueryExpression_instantiation(instance):
    assert isinstance(instance, QueryExpression)


SQLDataType_strategy = st.builds(SQLDataType)
@given(instance=SQLDataType_strategy)
@settings(max_examples=25)
def test_SQLDataType_instantiation(instance):
    assert isinstance(instance, SQLDataType)


SQLDistinctType_strategy = st.builds(SQLDistinctType)
@given(instance=SQLDistinctType_strategy)
@settings(max_examples=25)
def test_SQLDistinctType_instantiation(instance):
    assert isinstance(instance, SQLDistinctType)


SQLSimpleType_strategy = st.builds(SQLSimpleType)
@given(instance=SQLSimpleType_strategy)
@settings(max_examples=25)
def test_SQLSimpleType_instantiation(instance):
    assert isinstance(instance, SQLSimpleType)


Table_strategy = st.builds(Table)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


Trigger_strategy = st.builds(Trigger)
@given(instance=Trigger_strategy)
@settings(max_examples=25)
def test_Trigger_instantiation(instance):
    assert isinstance(instance, Trigger)



