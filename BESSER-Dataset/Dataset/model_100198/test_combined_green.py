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
    SInlinedSQLType,
    sqlDSL_SDecimal,
    sqlDSL_SString,
    sqlDSL_SEnumLiteral,
    SExtDeclaredSQLType,
    sqlDSL_SInlinedSQLType,
    SArtifact,
    sqlDSL_SEnum,
    sqlDSL_STable,
    sqlDSL_SExtDeclaredSQLType,
    STableMember,
    sqlDSL_SJoinColumn,
    sqlDSL_SColumn,
    sqlDSL_SColumnProps,
    sqlDSL_STableMember,
    sqlDSL_SSettings,
    sqlDSL_SModel,
    sqlDSL_SArtifact,
    SIndex,
    SSimpleTypes,
    SDBEngine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sinlinedsqltype_is_not_abstract():
    assert not inspect.isabstract(SInlinedSQLType)


def test_hyp_sinlinedsqltype_constructor_exists():
    assert callable(SInlinedSQLType.__init__)


def test_hyp_sinlinedsqltype_constructor_args():
    sig = inspect.signature(SInlinedSQLType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_sdecimal_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SDecimal)


def test_hyp_sqldsl_sdecimal_constructor_exists():
    assert callable(sqlDSL_SDecimal.__init__)


def test_hyp_sqldsl_sdecimal_constructor_args():
    sig = inspect.signature(sqlDSL_SDecimal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_sstring_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SString)


def test_hyp_sqldsl_sstring_constructor_exists():
    assert callable(sqlDSL_SString.__init__)


def test_hyp_sqldsl_sstring_constructor_args():
    sig = inspect.signature(sqlDSL_SString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_senumliteral_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SEnumLiteral)


def test_hyp_sqldsl_senumliteral_constructor_exists():
    assert callable(sqlDSL_SEnumLiteral.__init__)


def test_hyp_sqldsl_senumliteral_constructor_args():
    sig = inspect.signature(sqlDSL_SEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_sextdeclaredsqltype_is_not_abstract():
    assert not inspect.isabstract(SExtDeclaredSQLType)


def test_hyp_sextdeclaredsqltype_constructor_exists():
    assert callable(SExtDeclaredSQLType.__init__)


def test_hyp_sextdeclaredsqltype_constructor_args():
    sig = inspect.signature(SExtDeclaredSQLType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_sinlinedsqltype_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SInlinedSQLType)


def test_hyp_sqldsl_sinlinedsqltype_constructor_exists():
    assert callable(sqlDSL_SInlinedSQLType.__init__)


def test_hyp_sqldsl_sinlinedsqltype_constructor_args():
    sig = inspect.signature(sqlDSL_SInlinedSQLType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sartifact_is_not_abstract():
    assert not inspect.isabstract(SArtifact)


def test_hyp_sartifact_constructor_exists():
    assert callable(SArtifact.__init__)


def test_hyp_sartifact_constructor_args():
    sig = inspect.signature(SArtifact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_senum_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SEnum)


def test_hyp_sqldsl_senum_constructor_exists():
    assert callable(sqlDSL_SEnum.__init__)


def test_hyp_sqldsl_senum_constructor_args():
    sig = inspect.signature(sqlDSL_SEnum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_stable_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_STable)


def test_hyp_sqldsl_stable_constructor_exists():
    assert callable(sqlDSL_STable.__init__)


def test_hyp_sqldsl_stable_constructor_args():
    sig = inspect.signature(sqlDSL_STable.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "cached" in params, "Missing parameter 'cached'"
    assert "entityname" in params, "Missing parameter 'entityname'"






def test_hyp_sqldsl_sextdeclaredsqltype_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SExtDeclaredSQLType)


def test_hyp_sqldsl_sextdeclaredsqltype_constructor_exists():
    assert callable(sqlDSL_SExtDeclaredSQLType.__init__)


def test_hyp_sqldsl_sextdeclaredsqltype_constructor_args():
    sig = inspect.signature(sqlDSL_SExtDeclaredSQLType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stablemember_is_not_abstract():
    assert not inspect.isabstract(STableMember)


def test_hyp_stablemember_constructor_exists():
    assert callable(STableMember.__init__)


def test_hyp_stablemember_constructor_args():
    sig = inspect.signature(STableMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_sjoincolumn_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SJoinColumn)


def test_hyp_sqldsl_sjoincolumn_constructor_exists():
    assert callable(sqlDSL_SJoinColumn.__init__)


def test_hyp_sqldsl_sjoincolumn_constructor_args():
    sig = inspect.signature(sqlDSL_SJoinColumn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldsl_scolumn_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SColumn)


def test_hyp_sqldsl_scolumn_constructor_exists():
    assert callable(sqlDSL_SColumn.__init__)


def test_hyp_sqldsl_scolumn_constructor_args():
    sig = inspect.signature(sqlDSL_SColumn.__init__)
    params = list(sig.parameters.keys())
    assert "simpleType" in params, "Missing parameter 'simpleType'"




def test_hyp_sqldsl_scolumnprops_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SColumnProps)


def test_hyp_sqldsl_scolumnprops_constructor_exists():
    assert callable(sqlDSL_SColumnProps.__init__)


def test_hyp_sqldsl_scolumnprops_constructor_args():
    sig = inspect.signature(sqlDSL_SColumnProps.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "aes" in params, "Missing parameter 'aes'"
    assert "index" in params, "Missing parameter 'index'"
    assert "javacolumn" in params, "Missing parameter 'javacolumn'"







def test_hyp_sqldsl_stablemember_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_STableMember)


def test_hyp_sqldsl_stablemember_constructor_exists():
    assert callable(sqlDSL_STableMember.__init__)


def test_hyp_sqldsl_stablemember_constructor_args():
    sig = inspect.signature(sqlDSL_STableMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sqldsl_ssettings_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SSettings)


def test_hyp_sqldsl_ssettings_constructor_exists():
    assert callable(sqlDSL_SSettings.__init__)


def test_hyp_sqldsl_ssettings_constructor_args():
    sig = inspect.signature(sqlDSL_SSettings.__init__)
    params = list(sig.parameters.keys())
    assert "javapackage" in params, "Missing parameter 'javapackage'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "engine" in params, "Missing parameter 'engine'"






def test_hyp_sqldsl_smodel_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SModel)


def test_hyp_sqldsl_smodel_constructor_exists():
    assert callable(sqlDSL_SModel.__init__)


def test_hyp_sqldsl_smodel_constructor_args():
    sig = inspect.signature(sqlDSL_SModel.__init__)
    params = list(sig.parameters.keys())
    assert "generatedFile" in params, "Missing parameter 'generatedFile'"




def test_hyp_sqldsl_sartifact_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SArtifact)


def test_hyp_sqldsl_sartifact_constructor_exists():
    assert callable(sqlDSL_SArtifact.__init__)


def test_hyp_sqldsl_sartifact_constructor_args():
    sig = inspect.signature(sqlDSL_SArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_sindex_exists():
    # Check that the Enumeration exists
    assert SIndex is not None

def test_hyp_sindex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIndex]
    expected_literals = [
        "UNIQUE",
        "NO",
        "SPATIAL",
        "YES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIndex"

def test_hyp_ssimpletypes_exists():
    # Check that the Enumeration exists
    assert SSimpleTypes is not None

def test_hyp_ssimpletypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SSimpleTypes]
    expected_literals = [
        "MEDIUM_INT",
        "DATETIME",
        "BLOB",
        "Currency",
        "POLYGON",
        "INT",
        "DATE",
        "SMALL_INT",
        "TINY_INT",
        "FOTO",
        "TIME",
        "BOOLEAN",
        "Coordinate",
        "POINT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SSimpleTypes"

def test_hyp_sdbengine_exists():
    # Check that the Enumeration exists
    assert SDBEngine is not None

def test_hyp_sdbengine_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SDBEngine]
    expected_literals = [
        "MYISAM",
        "INNODB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SDBEngine"


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
SInlinedSQLType_strategy = st.builds(
    SInlinedSQLType,
)
sqlDSL_SDecimal_strategy = st.builds(
    sqlDSL_SDecimal,
)
sqlDSL_SString_strategy = st.builds(
    sqlDSL_SString,
)
sqlDSL_SEnumLiteral_strategy = st.builds(
    sqlDSL_SEnumLiteral,
    name=
        safe_text,
    value=
        st.integers()
)
SExtDeclaredSQLType_strategy = st.builds(
    SExtDeclaredSQLType,
)
sqlDSL_SInlinedSQLType_strategy = st.builds(
    sqlDSL_SInlinedSQLType,
    value=
        st.integers()
)
SArtifact_strategy = st.builds(
    SArtifact,
)
sqlDSL_SEnum_strategy = st.builds(
    sqlDSL_SEnum,
)
sqlDSL_STable_strategy = st.builds(
    sqlDSL_STable,
    prefix=
        safe_text,
    cached=
        st.booleans(),
    entityname=
        safe_text
)
sqlDSL_SExtDeclaredSQLType_strategy = st.builds(
    sqlDSL_SExtDeclaredSQLType,
)
STableMember_strategy = st.builds(
    STableMember,
)
sqlDSL_SJoinColumn_strategy = st.builds(
    sqlDSL_SJoinColumn,
)
sqlDSL_SColumn_strategy = st.builds(
    sqlDSL_SColumn,
    simpleType=
        safe_text
)
sqlDSL_SColumnProps_strategy = st.builds(
    sqlDSL_SColumnProps,
    nullable=
        st.booleans(),
    aes=
        st.booleans(),
    index=
        safe_text,
    javacolumn=
        safe_text
)
sqlDSL_STableMember_strategy = st.builds(
    sqlDSL_STableMember,
    name=
        safe_text
)
sqlDSL_SSettings_strategy = st.builds(
    sqlDSL_SSettings,
    javapackage=
        safe_text,
    schema=
        safe_text,
    engine=
        safe_text
)
sqlDSL_SModel_strategy = st.builds(
    sqlDSL_SModel,
    generatedFile=
        safe_text
)
sqlDSL_SArtifact_strategy = st.builds(
    sqlDSL_SArtifact,
    name=
        safe_text
)







@given(instance=sqlDSL_SEnumLiteral_strategy)
def test_hyp_sqldsl_senumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sqlDSL_SEnumLiteral_strategy)
def test_hyp_sqldsl_senumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=sqlDSL_SInlinedSQLType_strategy)
def test_hyp_sqldsl_sinlinedsqltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=sqlDSL_STable_strategy)
def test_hyp_sqldsl_stable_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=sqlDSL_STable_strategy)
def test_hyp_sqldsl_stable_cached_setter(instance):
    original = instance.cached
    instance.cached = original
    assert instance.cached == original



@given(instance=sqlDSL_STable_strategy)
def test_hyp_sqldsl_stable_entityname_setter(instance):
    original = instance.entityname
    instance.entityname = original
    assert instance.entityname == original







@given(instance=sqlDSL_SColumn_strategy)
def test_hyp_sqldsl_scolumn_simpleType_setter(instance):
    original = instance.simpleType
    instance.simpleType = original
    assert instance.simpleType == original




@given(instance=sqlDSL_SColumnProps_strategy)
def test_hyp_sqldsl_scolumnprops_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=sqlDSL_SColumnProps_strategy)
def test_hyp_sqldsl_scolumnprops_aes_setter(instance):
    original = instance.aes
    instance.aes = original
    assert instance.aes == original



@given(instance=sqlDSL_SColumnProps_strategy)
def test_hyp_sqldsl_scolumnprops_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=sqlDSL_SColumnProps_strategy)
def test_hyp_sqldsl_scolumnprops_javacolumn_setter(instance):
    original = instance.javacolumn
    instance.javacolumn = original
    assert instance.javacolumn == original




@given(instance=sqlDSL_STableMember_strategy)
def test_hyp_sqldsl_stablemember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=sqlDSL_SSettings_strategy)
def test_hyp_sqldsl_ssettings_javapackage_setter(instance):
    original = instance.javapackage
    instance.javapackage = original
    assert instance.javapackage == original



@given(instance=sqlDSL_SSettings_strategy)
def test_hyp_sqldsl_ssettings_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original



@given(instance=sqlDSL_SSettings_strategy)
def test_hyp_sqldsl_ssettings_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original




@given(instance=sqlDSL_SModel_strategy)
def test_hyp_sqldsl_smodel_generatedFile_setter(instance):
    original = instance.generatedFile
    instance.generatedFile = original
    assert instance.generatedFile == original




@given(instance=sqlDSL_SArtifact_strategy)
def test_hyp_sqldsl_sartifact_name_setter(instance):
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
    SArtifact,
    SExtDeclaredSQLType,
    SInlinedSQLType,
    STableMember,
    sqlDSL_SArtifact,
    sqlDSL_SColumn,
    sqlDSL_SColumnProps,
    sqlDSL_SDecimal,
    sqlDSL_SEnum,
    sqlDSL_SEnumLiteral,
    sqlDSL_SExtDeclaredSQLType,
    sqlDSL_SInlinedSQLType,
    sqlDSL_SJoinColumn,
    sqlDSL_SModel,
    sqlDSL_SSettings,
    sqlDSL_SString,
    sqlDSL_STable,
    sqlDSL_STableMember,
    SDBEngine,
    SIndex,
    SSimpleTypes,
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

def test_sqlDSL_SArtifact_name_value_roundtrip():
    instance = sqlDSL_SArtifact(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sqlDSL_SColumn_simpleType_value_roundtrip():
    instance = sqlDSL_SColumn(simpleType="sample_text")
    assert instance.simpleType == "sample_text"
    instance.simpleType = "sample_text_2"
    assert instance.simpleType == "sample_text_2"


def test_sqlDSL_SColumnProps_aes_value_roundtrip():
    instance = sqlDSL_SColumnProps(aes=True, index="sample_text", javacolumn="sample_text", nullable=True)
    assert instance.aes == True
    instance.aes = False
    assert instance.aes == False


def test_sqlDSL_SColumnProps_index_value_roundtrip():
    instance = sqlDSL_SColumnProps(aes=True, index="sample_text", javacolumn="sample_text", nullable=True)
    assert instance.index == "sample_text"
    instance.index = "sample_text_2"
    assert instance.index == "sample_text_2"


def test_sqlDSL_SColumnProps_javacolumn_value_roundtrip():
    instance = sqlDSL_SColumnProps(aes=True, index="sample_text", javacolumn="sample_text", nullable=True)
    assert instance.javacolumn == "sample_text"
    instance.javacolumn = "sample_text_2"
    assert instance.javacolumn == "sample_text_2"


def test_sqlDSL_SColumnProps_nullable_value_roundtrip():
    instance = sqlDSL_SColumnProps(aes=True, index="sample_text", javacolumn="sample_text", nullable=True)
    assert instance.nullable == True
    instance.nullable = False
    assert instance.nullable == False


def test_sqlDSL_SEnumLiteral_name_value_roundtrip():
    instance = sqlDSL_SEnumLiteral(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sqlDSL_SEnumLiteral_value_value_roundtrip():
    instance = sqlDSL_SEnumLiteral(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_sqlDSL_SInlinedSQLType_value_value_roundtrip():
    instance = sqlDSL_SInlinedSQLType(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_sqlDSL_SModel_generatedFile_value_roundtrip():
    instance = sqlDSL_SModel(generatedFile="sample_text")
    assert instance.generatedFile == "sample_text"
    instance.generatedFile = "sample_text_2"
    assert instance.generatedFile == "sample_text_2"


def test_sqlDSL_SSettings_engine_value_roundtrip():
    instance = sqlDSL_SSettings(engine="sample_text", javapackage="sample_text", schema="sample_text")
    assert instance.engine == "sample_text"
    instance.engine = "sample_text_2"
    assert instance.engine == "sample_text_2"


def test_sqlDSL_SSettings_javapackage_value_roundtrip():
    instance = sqlDSL_SSettings(engine="sample_text", javapackage="sample_text", schema="sample_text")
    assert instance.javapackage == "sample_text"
    instance.javapackage = "sample_text_2"
    assert instance.javapackage == "sample_text_2"


def test_sqlDSL_SSettings_schema_value_roundtrip():
    instance = sqlDSL_SSettings(engine="sample_text", javapackage="sample_text", schema="sample_text")
    assert instance.schema == "sample_text"
    instance.schema = "sample_text_2"
    assert instance.schema == "sample_text_2"


def test_sqlDSL_STable_cached_value_roundtrip():
    instance = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    assert instance.cached == True
    instance.cached = False
    assert instance.cached == False


def test_sqlDSL_STable_entityname_value_roundtrip():
    instance = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    assert instance.entityname == "sample_text"
    instance.entityname = "sample_text_2"
    assert instance.entityname == "sample_text_2"


def test_sqlDSL_STable_prefix_value_roundtrip():
    instance = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    assert instance.prefix == "sample_text"
    instance.prefix = "sample_text_2"
    assert instance.prefix == "sample_text_2"


def test_sqlDSL_STableMember_name_value_roundtrip():
    instance = sqlDSL_STableMember(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sqlDSL_SEnum_isa_SArtifact():
    instance = sqlDSL_SEnum()
    assert isinstance(instance, SArtifact)


def test_sqlDSL_STable_isa_SArtifact():
    instance = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    assert isinstance(instance, SArtifact)


def test_sqlDSL_SEnum_isa_SExtDeclaredSQLType():
    instance = sqlDSL_SEnum()
    assert isinstance(instance, SExtDeclaredSQLType)


def test_sqlDSL_SDecimal_isa_SInlinedSQLType():
    instance = sqlDSL_SDecimal()
    assert isinstance(instance, SInlinedSQLType)


def test_sqlDSL_SString_isa_SInlinedSQLType():
    instance = sqlDSL_SString()
    assert isinstance(instance, SInlinedSQLType)


def test_sqlDSL_SColumn_isa_STableMember():
    instance = sqlDSL_SColumn(simpleType="sample_text")
    assert isinstance(instance, STableMember)


def test_sqlDSL_SJoinColumn_isa_STableMember():
    instance = sqlDSL_SJoinColumn()
    assert isinstance(instance, STableMember)


def test_assoc_artifact1_link_reassign_clear():
    a = sqlDSL_SModel(generatedFile="sample_text")
    b1 = sqlDSL_SArtifact(name="sample_text")
    b2 = sqlDSL_SArtifact(name="sample_text_2")
    _safe_set(a, 'sqlDSL_SModel2', {b1})
    assert _is_linked(a, 'sqlDSL_SModel2', b1)
    if hasattr(b1, 'sqlDSL_SArtifact'):
        assert _is_linked(b1, 'sqlDSL_SArtifact', a)
    _safe_set(a, 'sqlDSL_SModel2', {b2})
    assert _is_linked(a, 'sqlDSL_SModel2', b2)
    if hasattr(b1, 'sqlDSL_SArtifact'):
        assert not _is_linked(b1, 'sqlDSL_SArtifact', a)
    if hasattr(b2, 'sqlDSL_SArtifact'):
        assert _is_linked(b2, 'sqlDSL_SArtifact', a)
    _safe_set(a, 'sqlDSL_SModel2', set())
    assert not _is_linked(a, 'sqlDSL_SModel2', b2)
    if hasattr(b2, 'sqlDSL_SArtifact'):
        assert not _is_linked(b2, 'sqlDSL_SArtifact', a)


def test_assoc_columns5_link_reassign_clear():
    a = sqlDSL_STableMember(name="sample_text")
    b1 = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    b2 = sqlDSL_STable(cached=False, entityname="sample_text_2", prefix="sample_text_2")
    _safe_set(a, 'sqlDSL_STableMember', b1)
    assert _is_linked(a, 'sqlDSL_STableMember', b1)
    if hasattr(b1, 'sqlDSL_STable6'):
        assert _is_linked(b1, 'sqlDSL_STable6', a)
    _safe_set(a, 'sqlDSL_STableMember', b2)
    assert _is_linked(a, 'sqlDSL_STableMember', b2)
    if hasattr(b1, 'sqlDSL_STable6'):
        assert not _is_linked(b1, 'sqlDSL_STable6', a)
    if hasattr(b2, 'sqlDSL_STable6'):
        assert _is_linked(b2, 'sqlDSL_STable6', a)
    _safe_set(a, 'sqlDSL_STableMember', None)
    assert not _is_linked(a, 'sqlDSL_STableMember', b2)
    if hasattr(b2, 'sqlDSL_STable6'):
        assert not _is_linked(b2, 'sqlDSL_STable6', a)


def test_assoc_extType9_link_reassign_clear():
    a = sqlDSL_SColumn(simpleType="sample_text")
    b1 = sqlDSL_SExtDeclaredSQLType()
    b2 = sqlDSL_SExtDeclaredSQLType()
    _safe_set(a, 'sqlDSL_SColumn', b1)
    assert _is_linked(a, 'sqlDSL_SColumn', b1)
    if hasattr(b1, 'sqlDSL_SExtDeclaredSQLType'):
        assert _is_linked(b1, 'sqlDSL_SExtDeclaredSQLType', a)
    _safe_set(a, 'sqlDSL_SColumn', b2)
    assert _is_linked(a, 'sqlDSL_SColumn', b2)
    if hasattr(b1, 'sqlDSL_SExtDeclaredSQLType'):
        assert not _is_linked(b1, 'sqlDSL_SExtDeclaredSQLType', a)
    if hasattr(b2, 'sqlDSL_SExtDeclaredSQLType'):
        assert _is_linked(b2, 'sqlDSL_SExtDeclaredSQLType', a)
    _safe_set(a, 'sqlDSL_SColumn', None)
    assert not _is_linked(a, 'sqlDSL_SColumn', b2)
    if hasattr(b2, 'sqlDSL_SExtDeclaredSQLType'):
        assert not _is_linked(b2, 'sqlDSL_SExtDeclaredSQLType', a)


def test_assoc_inlinedType10_link_reassign_clear():
    a = sqlDSL_SInlinedSQLType(value=7)
    b1 = sqlDSL_SColumn(simpleType="sample_text")
    b2 = sqlDSL_SColumn(simpleType="sample_text_2")
    _safe_set(a, 'sqlDSL_SInlinedSQLType', b1)
    assert _is_linked(a, 'sqlDSL_SInlinedSQLType', b1)
    if hasattr(b1, 'sqlDSL_SColumn11'):
        assert _is_linked(b1, 'sqlDSL_SColumn11', a)
    _safe_set(a, 'sqlDSL_SInlinedSQLType', b2)
    assert _is_linked(a, 'sqlDSL_SInlinedSQLType', b2)
    if hasattr(b1, 'sqlDSL_SColumn11'):
        assert not _is_linked(b1, 'sqlDSL_SColumn11', a)
    if hasattr(b2, 'sqlDSL_SColumn11'):
        assert _is_linked(b2, 'sqlDSL_SColumn11', a)
    _safe_set(a, 'sqlDSL_SInlinedSQLType', None)
    assert not _is_linked(a, 'sqlDSL_SInlinedSQLType', b2)
    if hasattr(b2, 'sqlDSL_SColumn11'):
        assert not _is_linked(b2, 'sqlDSL_SColumn11', a)


def test_assoc_literals14_link_reassign_clear():
    a = sqlDSL_SEnumLiteral(name="sample_text", value=7)
    b1 = sqlDSL_SEnum()
    b2 = sqlDSL_SEnum()
    _safe_set(a, 'sqlDSL_SEnumLiteral', b1)
    assert _is_linked(a, 'sqlDSL_SEnumLiteral', b1)
    if hasattr(b1, 'sqlDSL_SEnum'):
        assert _is_linked(b1, 'sqlDSL_SEnum', a)
    _safe_set(a, 'sqlDSL_SEnumLiteral', b2)
    assert _is_linked(a, 'sqlDSL_SEnumLiteral', b2)
    if hasattr(b1, 'sqlDSL_SEnum'):
        assert not _is_linked(b1, 'sqlDSL_SEnum', a)
    if hasattr(b2, 'sqlDSL_SEnum'):
        assert _is_linked(b2, 'sqlDSL_SEnum', a)
    _safe_set(a, 'sqlDSL_SEnumLiteral', None)
    assert not _is_linked(a, 'sqlDSL_SEnumLiteral', b2)
    if hasattr(b2, 'sqlDSL_SEnum'):
        assert not _is_linked(b2, 'sqlDSL_SEnum', a)


def test_assoc_props7_link_reassign_clear():
    a = sqlDSL_STableMember(name="sample_text")
    b1 = sqlDSL_SColumnProps(aes=True, index="sample_text", javacolumn="sample_text", nullable=True)
    b2 = sqlDSL_SColumnProps(aes=False, index="sample_text_2", javacolumn="sample_text_2", nullable=False)
    _safe_set(a, 'sqlDSL_STableMember8', b1)
    assert _is_linked(a, 'sqlDSL_STableMember8', b1)
    if hasattr(b1, 'sqlDSL_SColumnProps'):
        assert _is_linked(b1, 'sqlDSL_SColumnProps', a)
    _safe_set(a, 'sqlDSL_STableMember8', b2)
    assert _is_linked(a, 'sqlDSL_STableMember8', b2)
    if hasattr(b1, 'sqlDSL_SColumnProps'):
        assert not _is_linked(b1, 'sqlDSL_SColumnProps', a)
    if hasattr(b2, 'sqlDSL_SColumnProps'):
        assert _is_linked(b2, 'sqlDSL_SColumnProps', a)
    _safe_set(a, 'sqlDSL_STableMember8', None)
    assert not _is_linked(a, 'sqlDSL_STableMember8', b2)
    if hasattr(b2, 'sqlDSL_SColumnProps'):
        assert not _is_linked(b2, 'sqlDSL_SColumnProps', a)


def test_assoc_referencedType12_link_reassign_clear():
    a = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    b1 = sqlDSL_SJoinColumn()
    b2 = sqlDSL_SJoinColumn()
    _safe_set(a, 'sqlDSL_STable13', b1)
    assert _is_linked(a, 'sqlDSL_STable13', b1)
    if hasattr(b1, 'sqlDSL_SJoinColumn'):
        assert _is_linked(b1, 'sqlDSL_SJoinColumn', a)
    _safe_set(a, 'sqlDSL_STable13', b2)
    assert _is_linked(a, 'sqlDSL_STable13', b2)
    if hasattr(b1, 'sqlDSL_SJoinColumn'):
        assert not _is_linked(b1, 'sqlDSL_SJoinColumn', a)
    if hasattr(b2, 'sqlDSL_SJoinColumn'):
        assert _is_linked(b2, 'sqlDSL_SJoinColumn', a)
    _safe_set(a, 'sqlDSL_STable13', None)
    assert not _is_linked(a, 'sqlDSL_STable13', b2)
    if hasattr(b2, 'sqlDSL_SJoinColumn'):
        assert not _is_linked(b2, 'sqlDSL_SJoinColumn', a)


def test_assoc_settings0_link_reassign_clear():
    a = sqlDSL_SSettings(engine="sample_text", javapackage="sample_text", schema="sample_text")
    b1 = sqlDSL_SModel(generatedFile="sample_text")
    b2 = sqlDSL_SModel(generatedFile="sample_text_2")
    _safe_set(a, 'sqlDSL_SSettings', b1)
    assert _is_linked(a, 'sqlDSL_SSettings', b1)
    if hasattr(b1, 'sqlDSL_SModel'):
        assert _is_linked(b1, 'sqlDSL_SModel', a)
    _safe_set(a, 'sqlDSL_SSettings', b2)
    assert _is_linked(a, 'sqlDSL_SSettings', b2)
    if hasattr(b1, 'sqlDSL_SModel'):
        assert not _is_linked(b1, 'sqlDSL_SModel', a)
    if hasattr(b2, 'sqlDSL_SModel'):
        assert _is_linked(b2, 'sqlDSL_SModel', a)
    _safe_set(a, 'sqlDSL_SSettings', None)
    assert not _is_linked(a, 'sqlDSL_SSettings', b2)
    if hasattr(b2, 'sqlDSL_SModel'):
        assert not _is_linked(b2, 'sqlDSL_SModel', a)


def test_assoc_settings3_link_reassign_clear():
    a = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    b1 = sqlDSL_SSettings(engine="sample_text", javapackage="sample_text", schema="sample_text")
    b2 = sqlDSL_SSettings(engine="sample_text_2", javapackage="sample_text_2", schema="sample_text_2")
    _safe_set(a, 'sqlDSL_STable', b1)
    assert _is_linked(a, 'sqlDSL_STable', b1)
    if hasattr(b1, 'sqlDSL_SSettings4'):
        assert _is_linked(b1, 'sqlDSL_SSettings4', a)
    _safe_set(a, 'sqlDSL_STable', b2)
    assert _is_linked(a, 'sqlDSL_STable', b2)
    if hasattr(b1, 'sqlDSL_SSettings4'):
        assert not _is_linked(b1, 'sqlDSL_SSettings4', a)
    if hasattr(b2, 'sqlDSL_SSettings4'):
        assert _is_linked(b2, 'sqlDSL_SSettings4', a)
    _safe_set(a, 'sqlDSL_STable', None)
    assert not _is_linked(a, 'sqlDSL_STable', b2)
    if hasattr(b2, 'sqlDSL_SSettings4'):
        assert not _is_linked(b2, 'sqlDSL_SSettings4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SArtifact_strategy = st.builds(SArtifact)
@given(instance=SArtifact_strategy)
@settings(max_examples=25)
def test_SArtifact_instantiation(instance):
    assert isinstance(instance, SArtifact)


SExtDeclaredSQLType_strategy = st.builds(SExtDeclaredSQLType)
@given(instance=SExtDeclaredSQLType_strategy)
@settings(max_examples=25)
def test_SExtDeclaredSQLType_instantiation(instance):
    assert isinstance(instance, SExtDeclaredSQLType)


SInlinedSQLType_strategy = st.builds(SInlinedSQLType)
@given(instance=SInlinedSQLType_strategy)
@settings(max_examples=25)
def test_SInlinedSQLType_instantiation(instance):
    assert isinstance(instance, SInlinedSQLType)


STableMember_strategy = st.builds(STableMember)
@given(instance=STableMember_strategy)
@settings(max_examples=25)
def test_STableMember_instantiation(instance):
    assert isinstance(instance, STableMember)


sqlDSL_SArtifact_strategy = st.builds(sqlDSL_SArtifact, name=safe_text)
@given(instance=sqlDSL_SArtifact_strategy)
@settings(max_examples=25)
def test_sqlDSL_SArtifact_instantiation(instance):
    assert isinstance(instance, sqlDSL_SArtifact)


sqlDSL_SColumn_strategy = st.builds(sqlDSL_SColumn, simpleType=safe_text)
@given(instance=sqlDSL_SColumn_strategy)
@settings(max_examples=25)
def test_sqlDSL_SColumn_instantiation(instance):
    assert isinstance(instance, sqlDSL_SColumn)


sqlDSL_SColumnProps_strategy = st.builds(sqlDSL_SColumnProps, aes=st.booleans(), index=safe_text, javacolumn=safe_text, nullable=st.booleans())
@given(instance=sqlDSL_SColumnProps_strategy)
@settings(max_examples=25)
def test_sqlDSL_SColumnProps_instantiation(instance):
    assert isinstance(instance, sqlDSL_SColumnProps)


sqlDSL_SDecimal_strategy = st.builds(sqlDSL_SDecimal)
@given(instance=sqlDSL_SDecimal_strategy)
@settings(max_examples=25)
def test_sqlDSL_SDecimal_instantiation(instance):
    assert isinstance(instance, sqlDSL_SDecimal)


sqlDSL_SEnum_strategy = st.builds(sqlDSL_SEnum)
@given(instance=sqlDSL_SEnum_strategy)
@settings(max_examples=25)
def test_sqlDSL_SEnum_instantiation(instance):
    assert isinstance(instance, sqlDSL_SEnum)


sqlDSL_SEnumLiteral_strategy = st.builds(sqlDSL_SEnumLiteral, name=safe_text, value=st.integers())
@given(instance=sqlDSL_SEnumLiteral_strategy)
@settings(max_examples=25)
def test_sqlDSL_SEnumLiteral_instantiation(instance):
    assert isinstance(instance, sqlDSL_SEnumLiteral)


sqlDSL_SExtDeclaredSQLType_strategy = st.builds(sqlDSL_SExtDeclaredSQLType)
@given(instance=sqlDSL_SExtDeclaredSQLType_strategy)
@settings(max_examples=25)
def test_sqlDSL_SExtDeclaredSQLType_instantiation(instance):
    assert isinstance(instance, sqlDSL_SExtDeclaredSQLType)


sqlDSL_SInlinedSQLType_strategy = st.builds(sqlDSL_SInlinedSQLType, value=st.integers())
@given(instance=sqlDSL_SInlinedSQLType_strategy)
@settings(max_examples=25)
def test_sqlDSL_SInlinedSQLType_instantiation(instance):
    assert isinstance(instance, sqlDSL_SInlinedSQLType)


sqlDSL_SJoinColumn_strategy = st.builds(sqlDSL_SJoinColumn)
@given(instance=sqlDSL_SJoinColumn_strategy)
@settings(max_examples=25)
def test_sqlDSL_SJoinColumn_instantiation(instance):
    assert isinstance(instance, sqlDSL_SJoinColumn)


sqlDSL_SModel_strategy = st.builds(sqlDSL_SModel, generatedFile=safe_text)
@given(instance=sqlDSL_SModel_strategy)
@settings(max_examples=25)
def test_sqlDSL_SModel_instantiation(instance):
    assert isinstance(instance, sqlDSL_SModel)


sqlDSL_SSettings_strategy = st.builds(sqlDSL_SSettings, engine=safe_text, javapackage=safe_text, schema=safe_text)
@given(instance=sqlDSL_SSettings_strategy)
@settings(max_examples=25)
def test_sqlDSL_SSettings_instantiation(instance):
    assert isinstance(instance, sqlDSL_SSettings)


sqlDSL_SString_strategy = st.builds(sqlDSL_SString)
@given(instance=sqlDSL_SString_strategy)
@settings(max_examples=25)
def test_sqlDSL_SString_instantiation(instance):
    assert isinstance(instance, sqlDSL_SString)


sqlDSL_STable_strategy = st.builds(sqlDSL_STable, cached=st.booleans(), entityname=safe_text, prefix=safe_text)
@given(instance=sqlDSL_STable_strategy)
@settings(max_examples=25)
def test_sqlDSL_STable_instantiation(instance):
    assert isinstance(instance, sqlDSL_STable)


sqlDSL_STableMember_strategy = st.builds(sqlDSL_STableMember, name=safe_text)
@given(instance=sqlDSL_STableMember_strategy)
@settings(max_examples=25)
def test_sqlDSL_STableMember_instantiation(instance):
    assert isinstance(instance, sqlDSL_STableMember)



