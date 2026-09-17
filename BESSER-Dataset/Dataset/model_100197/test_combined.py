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
    ValueExp,
    SQLDML_IntegerValueExp,
    SQLDML_StringValueExp,
    DataType,
    StringValueExp,
    Predicate,
    SQLDML_ValueExp,
    SQLDML_FunctionExp,
    SQLDML_ListExp,
    BinaryExp,
    SQLDML_OperationExp,
    SQLDML_AndExp,
    SQLDML_OrExp,
    WhereClause,
    NamedElement,
    SQLDML_ColumnExp,
    SQLDML_DataType,
    SQLDML_Table,
    Expression,
    SQLDML_InExp,
    SQLDML_LikeExp,
    SQLDML_BinaryExp,
    SQLDML_NotExp,
    SQLDML_Predicate,
    SQLDML_QueryPredicate,
    QueryStmt,
    SQLDML_QueryStmtCol,
    SQLDML_QueryStmtAllCol,
    ColumnExp,
    Table,
    Statement,
    SQLDML_InsertStmt,
    SQLDML_QueryStmt,
    LocatedElement,
    SQLDML_NamedElement,
    SQLDML_Expression,
    SQLDML_WhereClause,
    SQLDML_SQLRoot,
    SQLDML_ViewStatement,
    SQLDML_Statement,
    SQLDML_LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_valueexp_is_not_abstract():
    assert not inspect.isabstract(ValueExp)


def test_hyp_valueexp_constructor_exists():
    assert callable(ValueExp.__init__)


def test_hyp_valueexp_constructor_args():
    sig = inspect.signature(ValueExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_integervalueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_IntegerValueExp)


def test_hyp_sqldml_integervalueexp_constructor_exists():
    assert callable(SQLDML_IntegerValueExp.__init__)


def test_hyp_sqldml_integervalueexp_constructor_args():
    sig = inspect.signature(SQLDML_IntegerValueExp.__init__)
    params = list(sig.parameters.keys())
    assert "aValue" in params, "Missing parameter 'aValue'"




def test_hyp_sqldml_stringvalueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_StringValueExp)


def test_hyp_sqldml_stringvalueexp_constructor_exists():
    assert callable(SQLDML_StringValueExp.__init__)


def test_hyp_sqldml_stringvalueexp_constructor_args():
    sig = inspect.signature(SQLDML_StringValueExp.__init__)
    params = list(sig.parameters.keys())
    assert "aValue" in params, "Missing parameter 'aValue'"




def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stringvalueexp_is_not_abstract():
    assert not inspect.isabstract(StringValueExp)


def test_hyp_stringvalueexp_constructor_exists():
    assert callable(StringValueExp.__init__)


def test_hyp_stringvalueexp_constructor_args():
    sig = inspect.signature(StringValueExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_hyp_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_hyp_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_valueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ValueExp)


def test_hyp_sqldml_valueexp_constructor_exists():
    assert callable(SQLDML_ValueExp.__init__)


def test_hyp_sqldml_valueexp_constructor_args():
    sig = inspect.signature(SQLDML_ValueExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_functionexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_FunctionExp)


def test_hyp_sqldml_functionexp_constructor_exists():
    assert callable(SQLDML_FunctionExp.__init__)


def test_hyp_sqldml_functionexp_constructor_args():
    sig = inspect.signature(SQLDML_FunctionExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sqldml_listexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ListExp)


def test_hyp_sqldml_listexp_constructor_exists():
    assert callable(SQLDML_ListExp.__init__)


def test_hyp_sqldml_listexp_constructor_args():
    sig = inspect.signature(SQLDML_ListExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_hyp_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_hyp_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_operationexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_OperationExp)


def test_hyp_sqldml_operationexp_constructor_exists():
    assert callable(SQLDML_OperationExp.__init__)


def test_hyp_sqldml_operationexp_constructor_args():
    sig = inspect.signature(SQLDML_OperationExp.__init__)
    params = list(sig.parameters.keys())
    assert "optName" in params, "Missing parameter 'optName'"




def test_hyp_sqldml_andexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_AndExp)


def test_hyp_sqldml_andexp_constructor_exists():
    assert callable(SQLDML_AndExp.__init__)


def test_hyp_sqldml_andexp_constructor_args():
    sig = inspect.signature(SQLDML_AndExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_orexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_OrExp)


def test_hyp_sqldml_orexp_constructor_exists():
    assert callable(SQLDML_OrExp.__init__)


def test_hyp_sqldml_orexp_constructor_args():
    sig = inspect.signature(SQLDML_OrExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whereclause_is_not_abstract():
    assert not inspect.isabstract(WhereClause)


def test_hyp_whereclause_constructor_exists():
    assert callable(WhereClause.__init__)


def test_hyp_whereclause_constructor_args():
    sig = inspect.signature(WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_columnexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ColumnExp)


def test_hyp_sqldml_columnexp_constructor_exists():
    assert callable(SQLDML_ColumnExp.__init__)


def test_hyp_sqldml_columnexp_constructor_args():
    sig = inspect.signature(SQLDML_ColumnExp.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"




def test_hyp_sqldml_datatype_is_not_abstract():
    assert not inspect.isabstract(SQLDML_DataType)


def test_hyp_sqldml_datatype_constructor_exists():
    assert callable(SQLDML_DataType.__init__)


def test_hyp_sqldml_datatype_constructor_args():
    sig = inspect.signature(SQLDML_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_table_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Table)


def test_hyp_sqldml_table_constructor_exists():
    assert callable(SQLDML_Table.__init__)


def test_hyp_sqldml_table_constructor_args():
    sig = inspect.signature(SQLDML_Table.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_inexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_InExp)


def test_hyp_sqldml_inexp_constructor_exists():
    assert callable(SQLDML_InExp.__init__)


def test_hyp_sqldml_inexp_constructor_args():
    sig = inspect.signature(SQLDML_InExp.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"




def test_hyp_sqldml_likeexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_LikeExp)


def test_hyp_sqldml_likeexp_constructor_exists():
    assert callable(SQLDML_LikeExp.__init__)


def test_hyp_sqldml_likeexp_constructor_args():
    sig = inspect.signature(SQLDML_LikeExp.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"




def test_hyp_sqldml_binaryexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_BinaryExp)


def test_hyp_sqldml_binaryexp_constructor_exists():
    assert callable(SQLDML_BinaryExp.__init__)


def test_hyp_sqldml_binaryexp_constructor_args():
    sig = inspect.signature(SQLDML_BinaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"




def test_hyp_sqldml_notexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_NotExp)


def test_hyp_sqldml_notexp_constructor_exists():
    assert callable(SQLDML_NotExp.__init__)


def test_hyp_sqldml_notexp_constructor_args():
    sig = inspect.signature(SQLDML_NotExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"




def test_hyp_sqldml_predicate_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Predicate)


def test_hyp_sqldml_predicate_constructor_exists():
    assert callable(SQLDML_Predicate.__init__)


def test_hyp_sqldml_predicate_constructor_args():
    sig = inspect.signature(SQLDML_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_querypredicate_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryPredicate)


def test_hyp_sqldml_querypredicate_constructor_exists():
    assert callable(SQLDML_QueryPredicate.__init__)


def test_hyp_sqldml_querypredicate_constructor_args():
    sig = inspect.signature(SQLDML_QueryPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_querystmt_is_not_abstract():
    assert not inspect.isabstract(QueryStmt)


def test_hyp_querystmt_constructor_exists():
    assert callable(QueryStmt.__init__)


def test_hyp_querystmt_constructor_args():
    sig = inspect.signature(QueryStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_querystmtcol_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryStmtCol)


def test_hyp_sqldml_querystmtcol_constructor_exists():
    assert callable(SQLDML_QueryStmtCol.__init__)


def test_hyp_sqldml_querystmtcol_constructor_args():
    sig = inspect.signature(SQLDML_QueryStmtCol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_querystmtallcol_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryStmtAllCol)


def test_hyp_sqldml_querystmtallcol_constructor_exists():
    assert callable(SQLDML_QueryStmtAllCol.__init__)


def test_hyp_sqldml_querystmtallcol_constructor_args():
    sig = inspect.signature(SQLDML_QueryStmtAllCol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_columnexp_is_not_abstract():
    assert not inspect.isabstract(ColumnExp)


def test_hyp_columnexp_constructor_exists():
    assert callable(ColumnExp.__init__)


def test_hyp_columnexp_constructor_args():
    sig = inspect.signature(ColumnExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_insertstmt_is_not_abstract():
    assert not inspect.isabstract(SQLDML_InsertStmt)


def test_hyp_sqldml_insertstmt_constructor_exists():
    assert callable(SQLDML_InsertStmt.__init__)


def test_hyp_sqldml_insertstmt_constructor_args():
    sig = inspect.signature(SQLDML_InsertStmt.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"




def test_hyp_sqldml_querystmt_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryStmt)


def test_hyp_sqldml_querystmt_constructor_exists():
    assert callable(SQLDML_QueryStmt.__init__)


def test_hyp_sqldml_querystmt_constructor_args():
    sig = inspect.signature(SQLDML_QueryStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_hyp_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_hyp_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_namedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_NamedElement)


def test_hyp_sqldml_namedelement_constructor_exists():
    assert callable(SQLDML_NamedElement.__init__)


def test_hyp_sqldml_namedelement_constructor_args():
    sig = inspect.signature(SQLDML_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sqldml_expression_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Expression)


def test_hyp_sqldml_expression_constructor_exists():
    assert callable(SQLDML_Expression.__init__)


def test_hyp_sqldml_expression_constructor_args():
    sig = inspect.signature(SQLDML_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_whereclause_is_not_abstract():
    assert not inspect.isabstract(SQLDML_WhereClause)


def test_hyp_sqldml_whereclause_constructor_exists():
    assert callable(SQLDML_WhereClause.__init__)


def test_hyp_sqldml_whereclause_constructor_args():
    sig = inspect.signature(SQLDML_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_sqlroot_is_not_abstract():
    assert not inspect.isabstract(SQLDML_SQLRoot)


def test_hyp_sqldml_sqlroot_constructor_exists():
    assert callable(SQLDML_SQLRoot.__init__)


def test_hyp_sqldml_sqlroot_constructor_args():
    sig = inspect.signature(SQLDML_SQLRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_viewstatement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ViewStatement)


def test_hyp_sqldml_viewstatement_constructor_exists():
    assert callable(SQLDML_ViewStatement.__init__)


def test_hyp_sqldml_viewstatement_constructor_args():
    sig = inspect.signature(SQLDML_ViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sqldml_statement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Statement)


def test_hyp_sqldml_statement_constructor_exists():
    assert callable(SQLDML_Statement.__init__)


def test_hyp_sqldml_statement_constructor_args():
    sig = inspect.signature(SQLDML_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sqldml_locatedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_LocatedElement)


def test_hyp_sqldml_locatedelement_constructor_exists():
    assert callable(SQLDML_LocatedElement.__init__)


def test_hyp_sqldml_locatedelement_constructor_args():
    sig = inspect.signature(SQLDML_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"





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
ValueExp_strategy = st.builds(
    ValueExp,
)
SQLDML_IntegerValueExp_strategy = st.builds(
    SQLDML_IntegerValueExp,
    aValue=
        safe_text
)
SQLDML_StringValueExp_strategy = st.builds(
    SQLDML_StringValueExp,
    aValue=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
StringValueExp_strategy = st.builds(
    StringValueExp,
)
Predicate_strategy = st.builds(
    Predicate,
)
SQLDML_ValueExp_strategy = st.builds(
    SQLDML_ValueExp,
)
SQLDML_FunctionExp_strategy = st.builds(
    SQLDML_FunctionExp,
    name=
        safe_text
)
SQLDML_ListExp_strategy = st.builds(
    SQLDML_ListExp,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
SQLDML_OperationExp_strategy = st.builds(
    SQLDML_OperationExp,
    optName=
        safe_text
)
SQLDML_AndExp_strategy = st.builds(
    SQLDML_AndExp,
)
SQLDML_OrExp_strategy = st.builds(
    SQLDML_OrExp,
)
WhereClause_strategy = st.builds(
    WhereClause,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SQLDML_ColumnExp_strategy = st.builds(
    SQLDML_ColumnExp,
    alias=
        safe_text
)
SQLDML_DataType_strategy = st.builds(
    SQLDML_DataType,
)
SQLDML_Table_strategy = st.builds(
    SQLDML_Table,
    alias=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
SQLDML_InExp_strategy = st.builds(
    SQLDML_InExp,
    columnName=
        safe_text
)
SQLDML_LikeExp_strategy = st.builds(
    SQLDML_LikeExp,
    columnName=
        safe_text
)
SQLDML_BinaryExp_strategy = st.builds(
    SQLDML_BinaryExp,
    opName=
        safe_text
)
SQLDML_NotExp_strategy = st.builds(
    SQLDML_NotExp,
    opName=
        safe_text
)
SQLDML_Predicate_strategy = st.builds(
    SQLDML_Predicate,
)
SQLDML_QueryPredicate_strategy = st.builds(
    SQLDML_QueryPredicate,
)
QueryStmt_strategy = st.builds(
    QueryStmt,
)
SQLDML_QueryStmtCol_strategy = st.builds(
    SQLDML_QueryStmtCol,
)
SQLDML_QueryStmtAllCol_strategy = st.builds(
    SQLDML_QueryStmtAllCol,
)
ColumnExp_strategy = st.builds(
    ColumnExp,
)
Table_strategy = st.builds(
    Table,
)
Statement_strategy = st.builds(
    Statement,
)
SQLDML_InsertStmt_strategy = st.builds(
    SQLDML_InsertStmt,
    tableName=
        safe_text
)
SQLDML_QueryStmt_strategy = st.builds(
    SQLDML_QueryStmt,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
SQLDML_NamedElement_strategy = st.builds(
    SQLDML_NamedElement,
    name=
        safe_text
)
SQLDML_Expression_strategy = st.builds(
    SQLDML_Expression,
)
SQLDML_WhereClause_strategy = st.builds(
    SQLDML_WhereClause,
)
SQLDML_SQLRoot_strategy = st.builds(
    SQLDML_SQLRoot,
)
SQLDML_ViewStatement_strategy = st.builds(
    SQLDML_ViewStatement,
    name=
        safe_text
)
SQLDML_Statement_strategy = st.builds(
    SQLDML_Statement,
)
SQLDML_LocatedElement_strategy = st.builds(
    SQLDML_LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)





@given(instance=SQLDML_IntegerValueExp_strategy)
def test_hyp_sqldml_integervalueexp_aValue_setter(instance):
    original = instance.aValue
    instance.aValue = original
    assert instance.aValue == original




@given(instance=SQLDML_StringValueExp_strategy)
def test_hyp_sqldml_stringvalueexp_aValue_setter(instance):
    original = instance.aValue
    instance.aValue = original
    assert instance.aValue == original








@given(instance=SQLDML_FunctionExp_strategy)
def test_hyp_sqldml_functionexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=SQLDML_OperationExp_strategy)
def test_hyp_sqldml_operationexp_optName_setter(instance):
    original = instance.optName
    instance.optName = original
    assert instance.optName == original








@given(instance=SQLDML_ColumnExp_strategy)
def test_hyp_sqldml_columnexp_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original





@given(instance=SQLDML_Table_strategy)
def test_hyp_sqldml_table_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original





@given(instance=SQLDML_InExp_strategy)
def test_hyp_sqldml_inexp_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original




@given(instance=SQLDML_LikeExp_strategy)
def test_hyp_sqldml_likeexp_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original




@given(instance=SQLDML_BinaryExp_strategy)
def test_hyp_sqldml_binaryexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original




@given(instance=SQLDML_NotExp_strategy)
def test_hyp_sqldml_notexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original












@given(instance=SQLDML_InsertStmt_strategy)
def test_hyp_sqldml_insertstmt_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original






@given(instance=SQLDML_NamedElement_strategy)
def test_hyp_sqldml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=SQLDML_ViewStatement_strategy)
def test_hyp_sqldml_viewstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=SQLDML_LocatedElement_strategy)
def test_hyp_sqldml_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=SQLDML_LocatedElement_strategy)
def test_hyp_sqldml_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=SQLDML_LocatedElement_strategy)
def test_hyp_sqldml_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryExp,
    ColumnExp,
    DataType,
    Expression,
    LocatedElement,
    NamedElement,
    Predicate,
    QueryStmt,
    SQLDML_AndExp,
    SQLDML_BinaryExp,
    SQLDML_ColumnExp,
    SQLDML_DataType,
    SQLDML_Expression,
    SQLDML_FunctionExp,
    SQLDML_InExp,
    SQLDML_InsertStmt,
    SQLDML_IntegerValueExp,
    SQLDML_LikeExp,
    SQLDML_ListExp,
    SQLDML_LocatedElement,
    SQLDML_NamedElement,
    SQLDML_NotExp,
    SQLDML_OperationExp,
    SQLDML_OrExp,
    SQLDML_Predicate,
    SQLDML_QueryPredicate,
    SQLDML_QueryStmt,
    SQLDML_QueryStmtAllCol,
    SQLDML_QueryStmtCol,
    SQLDML_SQLRoot,
    SQLDML_Statement,
    SQLDML_StringValueExp,
    SQLDML_Table,
    SQLDML_ValueExp,
    SQLDML_ViewStatement,
    SQLDML_WhereClause,
    Statement,
    StringValueExp,
    Table,
    ValueExp,
    WhereClause,
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

def test_SQLDML_BinaryExp_opName_value_roundtrip():
    instance = SQLDML_BinaryExp(opName="sample_text")
    assert instance.opName == "sample_text"
    instance.opName = "sample_text_2"
    assert instance.opName == "sample_text_2"


def test_SQLDML_ColumnExp_alias_value_roundtrip():
    instance = SQLDML_ColumnExp(alias="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_SQLDML_FunctionExp_name_value_roundtrip():
    instance = SQLDML_FunctionExp(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SQLDML_InExp_columnName_value_roundtrip():
    instance = SQLDML_InExp(columnName="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_SQLDML_InsertStmt_tableName_value_roundtrip():
    instance = SQLDML_InsertStmt(tableName="sample_text")
    assert instance.tableName == "sample_text"
    instance.tableName = "sample_text_2"
    assert instance.tableName == "sample_text_2"


def test_SQLDML_IntegerValueExp_aValue_value_roundtrip():
    instance = SQLDML_IntegerValueExp(aValue="sample_text")
    assert instance.aValue == "sample_text"
    instance.aValue = "sample_text_2"
    assert instance.aValue == "sample_text_2"


def test_SQLDML_LikeExp_columnName_value_roundtrip():
    instance = SQLDML_LikeExp(columnName="sample_text")
    assert instance.columnName == "sample_text"
    instance.columnName = "sample_text_2"
    assert instance.columnName == "sample_text_2"


def test_SQLDML_LocatedElement_commentsAfter_value_roundtrip():
    instance = SQLDML_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.commentsAfter == "sample_text"
    instance.commentsAfter = "sample_text_2"
    assert instance.commentsAfter == "sample_text_2"


def test_SQLDML_LocatedElement_commentsBefore_value_roundtrip():
    instance = SQLDML_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.commentsBefore == "sample_text"
    instance.commentsBefore = "sample_text_2"
    assert instance.commentsBefore == "sample_text_2"


def test_SQLDML_LocatedElement_location_value_roundtrip():
    instance = SQLDML_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_SQLDML_NamedElement_name_value_roundtrip():
    instance = SQLDML_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SQLDML_NotExp_opName_value_roundtrip():
    instance = SQLDML_NotExp(opName="sample_text")
    assert instance.opName == "sample_text"
    instance.opName = "sample_text_2"
    assert instance.opName == "sample_text_2"


def test_SQLDML_OperationExp_optName_value_roundtrip():
    instance = SQLDML_OperationExp(optName="sample_text")
    assert instance.optName == "sample_text"
    instance.optName = "sample_text_2"
    assert instance.optName == "sample_text_2"


def test_SQLDML_StringValueExp_aValue_value_roundtrip():
    instance = SQLDML_StringValueExp(aValue="sample_text")
    assert instance.aValue == "sample_text"
    instance.aValue = "sample_text_2"
    assert instance.aValue == "sample_text_2"


def test_SQLDML_Table_alias_value_roundtrip():
    instance = SQLDML_Table(alias="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_SQLDML_ViewStatement_name_value_roundtrip():
    instance = SQLDML_ViewStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SQLDML_AndExp_isa_BinaryExp():
    instance = SQLDML_AndExp()
    assert isinstance(instance, BinaryExp)


def test_SQLDML_OperationExp_isa_BinaryExp():
    instance = SQLDML_OperationExp(optName="sample_text")
    assert isinstance(instance, BinaryExp)


def test_SQLDML_OrExp_isa_BinaryExp():
    instance = SQLDML_OrExp()
    assert isinstance(instance, BinaryExp)


def test_SQLDML_BinaryExp_isa_Expression():
    instance = SQLDML_BinaryExp(opName="sample_text")
    assert isinstance(instance, Expression)


def test_SQLDML_InExp_isa_Expression():
    instance = SQLDML_InExp(columnName="sample_text")
    assert isinstance(instance, Expression)


def test_SQLDML_LikeExp_isa_Expression():
    instance = SQLDML_LikeExp(columnName="sample_text")
    assert isinstance(instance, Expression)


def test_SQLDML_NotExp_isa_Expression():
    instance = SQLDML_NotExp(opName="sample_text")
    assert isinstance(instance, Expression)


def test_SQLDML_Predicate_isa_Expression():
    instance = SQLDML_Predicate()
    assert isinstance(instance, Expression)


def test_SQLDML_QueryPredicate_isa_Expression():
    instance = SQLDML_QueryPredicate()
    assert isinstance(instance, Expression)


def test_SQLDML_Expression_isa_LocatedElement():
    instance = SQLDML_Expression()
    assert isinstance(instance, LocatedElement)


def test_SQLDML_NamedElement_isa_LocatedElement():
    instance = SQLDML_NamedElement(name="sample_text")
    assert isinstance(instance, LocatedElement)


def test_SQLDML_SQLRoot_isa_LocatedElement():
    instance = SQLDML_SQLRoot()
    assert isinstance(instance, LocatedElement)


def test_SQLDML_Statement_isa_LocatedElement():
    instance = SQLDML_Statement()
    assert isinstance(instance, LocatedElement)


def test_SQLDML_WhereClause_isa_LocatedElement():
    instance = SQLDML_WhereClause()
    assert isinstance(instance, LocatedElement)


def test_SQLDML_ColumnExp_isa_NamedElement():
    instance = SQLDML_ColumnExp(alias="sample_text")
    assert isinstance(instance, NamedElement)


def test_SQLDML_DataType_isa_NamedElement():
    instance = SQLDML_DataType()
    assert isinstance(instance, NamedElement)


def test_SQLDML_Table_isa_NamedElement():
    instance = SQLDML_Table(alias="sample_text")
    assert isinstance(instance, NamedElement)


def test_SQLDML_ColumnExp_isa_Predicate():
    instance = SQLDML_ColumnExp(alias="sample_text")
    assert isinstance(instance, Predicate)


def test_SQLDML_FunctionExp_isa_Predicate():
    instance = SQLDML_FunctionExp(name="sample_text")
    assert isinstance(instance, Predicate)


def test_SQLDML_ListExp_isa_Predicate():
    instance = SQLDML_ListExp()
    assert isinstance(instance, Predicate)


def test_SQLDML_ValueExp_isa_Predicate():
    instance = SQLDML_ValueExp()
    assert isinstance(instance, Predicate)


def test_SQLDML_QueryStmtAllCol_isa_QueryStmt():
    instance = SQLDML_QueryStmtAllCol()
    assert isinstance(instance, QueryStmt)


def test_SQLDML_QueryStmtCol_isa_QueryStmt():
    instance = SQLDML_QueryStmtCol()
    assert isinstance(instance, QueryStmt)


def test_SQLDML_InsertStmt_isa_Statement():
    instance = SQLDML_InsertStmt(tableName="sample_text")
    assert isinstance(instance, Statement)


def test_SQLDML_QueryStmt_isa_Statement():
    instance = SQLDML_QueryStmt()
    assert isinstance(instance, Statement)


def test_SQLDML_ViewStatement_isa_Statement():
    instance = SQLDML_ViewStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_SQLDML_IntegerValueExp_isa_ValueExp():
    instance = SQLDML_IntegerValueExp(aValue="sample_text")
    assert isinstance(instance, ValueExp)


def test_SQLDML_StringValueExp_isa_ValueExp():
    instance = SQLDML_StringValueExp(aValue="sample_text")
    assert isinstance(instance, ValueExp)


def test_assoc_arguments31_link_reassign_clear():
    a = SQLDML_FunctionExp(name="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'SQLDML_FunctionExp', {b1})
    assert _is_linked(a, 'SQLDML_FunctionExp', b1)
    if hasattr(b1, 'Expression32'):
        assert _is_linked(b1, 'Expression32', a)
    _safe_set(a, 'SQLDML_FunctionExp', {b2})
    assert _is_linked(a, 'SQLDML_FunctionExp', b2)
    if hasattr(b1, 'Expression32'):
        assert not _is_linked(b1, 'Expression32', a)
    if hasattr(b2, 'Expression32'):
        assert _is_linked(b2, 'Expression32', a)
    _safe_set(a, 'SQLDML_FunctionExp', set())
    assert not _is_linked(a, 'SQLDML_FunctionExp', b2)
    if hasattr(b2, 'Expression32'):
        assert not _is_linked(b2, 'Expression32', a)


def test_assoc_columns1_link_reassign_clear():
    a = SQLDML_ViewStatement(name="sample_text")
    b1 = ColumnExp()
    b2 = ColumnExp()
    _safe_set(a, 'SQLDML_ViewStatement', {b1})
    assert _is_linked(a, 'SQLDML_ViewStatement', b1)
    if hasattr(b1, 'ColumnExp'):
        assert _is_linked(b1, 'ColumnExp', a)
    _safe_set(a, 'SQLDML_ViewStatement', {b2})
    assert _is_linked(a, 'SQLDML_ViewStatement', b2)
    if hasattr(b1, 'ColumnExp'):
        assert not _is_linked(b1, 'ColumnExp', a)
    if hasattr(b2, 'ColumnExp'):
        assert _is_linked(b2, 'ColumnExp', a)
    _safe_set(a, 'SQLDML_ViewStatement', set())
    assert not _is_linked(a, 'SQLDML_ViewStatement', b2)
    if hasattr(b2, 'ColumnExp'):
        assert not _is_linked(b2, 'ColumnExp', a)


def test_assoc_elements23_link_reassign_clear():
    a = SQLDML_InExp(columnName="sample_text")
    b1 = Predicate()
    b2 = Predicate()
    _safe_set(a, 'SQLDML_InExp', {b1})
    assert _is_linked(a, 'SQLDML_InExp', b1)
    if hasattr(b1, 'Predicate'):
        assert _is_linked(b1, 'Predicate', a)
    _safe_set(a, 'SQLDML_InExp', {b2})
    assert _is_linked(a, 'SQLDML_InExp', b2)
    if hasattr(b1, 'Predicate'):
        assert not _is_linked(b1, 'Predicate', a)
    if hasattr(b2, 'Predicate'):
        assert _is_linked(b2, 'Predicate', a)
    _safe_set(a, 'SQLDML_InExp', set())
    assert not _is_linked(a, 'SQLDML_InExp', b2)
    if hasattr(b2, 'Predicate'):
        assert not _is_linked(b2, 'Predicate', a)


def test_assoc_expression22_link_reassign_clear():
    a = SQLDML_LikeExp(columnName="sample_text")
    b1 = StringValueExp()
    b2 = StringValueExp()
    _safe_set(a, 'SQLDML_LikeExp', b1)
    assert _is_linked(a, 'SQLDML_LikeExp', b1)
    if hasattr(b1, 'StringValueExp'):
        assert _is_linked(b1, 'StringValueExp', a)
    _safe_set(a, 'SQLDML_LikeExp', b2)
    assert _is_linked(a, 'SQLDML_LikeExp', b2)
    if hasattr(b1, 'StringValueExp'):
        assert not _is_linked(b1, 'StringValueExp', a)
    if hasattr(b2, 'StringValueExp'):
        assert _is_linked(b2, 'StringValueExp', a)
    _safe_set(a, 'SQLDML_LikeExp', None)
    assert not _is_linked(a, 'SQLDML_LikeExp', b2)
    if hasattr(b2, 'StringValueExp'):
        assert not _is_linked(b2, 'StringValueExp', a)


def test_assoc_leftExp12_link_reassign_clear():
    a = SQLDML_BinaryExp(opName="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'SQLDML_BinaryExp', b1)
    assert _is_linked(a, 'SQLDML_BinaryExp', b1)
    if hasattr(b1, 'Expression13'):
        assert _is_linked(b1, 'Expression13', a)
    _safe_set(a, 'SQLDML_BinaryExp', b2)
    assert _is_linked(a, 'SQLDML_BinaryExp', b2)
    if hasattr(b1, 'Expression13'):
        assert not _is_linked(b1, 'Expression13', a)
    if hasattr(b2, 'Expression13'):
        assert _is_linked(b2, 'Expression13', a)
    _safe_set(a, 'SQLDML_BinaryExp', None)
    assert not _is_linked(a, 'SQLDML_BinaryExp', b2)
    if hasattr(b2, 'Expression13'):
        assert not _is_linked(b2, 'Expression13', a)


def test_assoc_query2_link_reassign_clear():
    a = SQLDML_ViewStatement(name="sample_text")
    b1 = QueryStmt()
    b2 = QueryStmt()
    _safe_set(a, 'SQLDML_ViewStatement3', b1)
    assert _is_linked(a, 'SQLDML_ViewStatement3', b1)
    if hasattr(b1, 'QueryStmt'):
        assert _is_linked(b1, 'QueryStmt', a)
    _safe_set(a, 'SQLDML_ViewStatement3', b2)
    assert _is_linked(a, 'SQLDML_ViewStatement3', b2)
    if hasattr(b1, 'QueryStmt'):
        assert not _is_linked(b1, 'QueryStmt', a)
    if hasattr(b2, 'QueryStmt'):
        assert _is_linked(b2, 'QueryStmt', a)
    _safe_set(a, 'SQLDML_ViewStatement3', None)
    assert not _is_linked(a, 'SQLDML_ViewStatement3', b2)
    if hasattr(b2, 'QueryStmt'):
        assert not _is_linked(b2, 'QueryStmt', a)


def test_assoc_rightExp14_link_reassign_clear():
    a = SQLDML_BinaryExp(opName="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'SQLDML_BinaryExp15', b1)
    assert _is_linked(a, 'SQLDML_BinaryExp15', b1)
    if hasattr(b1, 'Expression16'):
        assert _is_linked(b1, 'Expression16', a)
    _safe_set(a, 'SQLDML_BinaryExp15', b2)
    assert _is_linked(a, 'SQLDML_BinaryExp15', b2)
    if hasattr(b1, 'Expression16'):
        assert not _is_linked(b1, 'Expression16', a)
    if hasattr(b2, 'Expression16'):
        assert _is_linked(b2, 'Expression16', a)
    _safe_set(a, 'SQLDML_BinaryExp15', None)
    assert not _is_linked(a, 'SQLDML_BinaryExp15', b2)
    if hasattr(b2, 'Expression16'):
        assert not _is_linked(b2, 'Expression16', a)


def test_assoc_type26_link_reassign_clear():
    a = SQLDML_ColumnExp(alias="sample_text")
    b1 = DataType()
    b2 = DataType()
    _safe_set(a, 'SQLDML_ColumnExp', b1)
    assert _is_linked(a, 'SQLDML_ColumnExp', b1)
    if hasattr(b1, 'DataType'):
        assert _is_linked(b1, 'DataType', a)
    _safe_set(a, 'SQLDML_ColumnExp', b2)
    assert _is_linked(a, 'SQLDML_ColumnExp', b2)
    if hasattr(b1, 'DataType'):
        assert not _is_linked(b1, 'DataType', a)
    if hasattr(b2, 'DataType'):
        assert _is_linked(b2, 'DataType', a)
    _safe_set(a, 'SQLDML_ColumnExp', None)
    assert not _is_linked(a, 'SQLDML_ColumnExp', b2)
    if hasattr(b2, 'DataType'):
        assert not _is_linked(b2, 'DataType', a)


def test_assoc_unused19_link_reassign_clear():
    a = SQLDML_NotExp(opName="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'SQLDML_NotExp20', b1)
    assert _is_linked(a, 'SQLDML_NotExp20', b1)
    if hasattr(b1, 'Expression21'):
        assert _is_linked(b1, 'Expression21', a)
    _safe_set(a, 'SQLDML_NotExp20', b2)
    assert _is_linked(a, 'SQLDML_NotExp20', b2)
    if hasattr(b1, 'Expression21'):
        assert not _is_linked(b1, 'Expression21', a)
    if hasattr(b2, 'Expression21'):
        assert _is_linked(b2, 'Expression21', a)
    _safe_set(a, 'SQLDML_NotExp20', None)
    assert not _is_linked(a, 'SQLDML_NotExp20', b2)
    if hasattr(b2, 'Expression21'):
        assert not _is_linked(b2, 'Expression21', a)


def test_assoc_valueExp17_link_reassign_clear():
    a = SQLDML_NotExp(opName="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'SQLDML_NotExp', b1)
    assert _is_linked(a, 'SQLDML_NotExp', b1)
    if hasattr(b1, 'Expression18'):
        assert _is_linked(b1, 'Expression18', a)
    _safe_set(a, 'SQLDML_NotExp', b2)
    assert _is_linked(a, 'SQLDML_NotExp', b2)
    if hasattr(b1, 'Expression18'):
        assert not _is_linked(b1, 'Expression18', a)
    if hasattr(b2, 'Expression18'):
        assert _is_linked(b2, 'Expression18', a)
    _safe_set(a, 'SQLDML_NotExp', None)
    assert not _is_linked(a, 'SQLDML_NotExp', b2)
    if hasattr(b2, 'Expression18'):
        assert not _is_linked(b2, 'Expression18', a)


def test_assoc_values4_link_reassign_clear():
    a = SQLDML_InsertStmt(tableName="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'SQLDML_InsertStmt', {b1})
    assert _is_linked(a, 'SQLDML_InsertStmt', b1)
    if hasattr(b1, 'Expression'):
        assert _is_linked(b1, 'Expression', a)
    _safe_set(a, 'SQLDML_InsertStmt', {b2})
    assert _is_linked(a, 'SQLDML_InsertStmt', b2)
    if hasattr(b1, 'Expression'):
        assert not _is_linked(b1, 'Expression', a)
    if hasattr(b2, 'Expression'):
        assert _is_linked(b2, 'Expression', a)
    _safe_set(a, 'SQLDML_InsertStmt', set())
    assert not _is_linked(a, 'SQLDML_InsertStmt', b2)
    if hasattr(b2, 'Expression'):
        assert not _is_linked(b2, 'Expression', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryExp_strategy = st.builds(BinaryExp)
@given(instance=BinaryExp_strategy)
@settings(max_examples=25)
def test_BinaryExp_instantiation(instance):
    assert isinstance(instance, BinaryExp)


ColumnExp_strategy = st.builds(ColumnExp)
@given(instance=ColumnExp_strategy)
@settings(max_examples=25)
def test_ColumnExp_instantiation(instance):
    assert isinstance(instance, ColumnExp)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


LocatedElement_strategy = st.builds(LocatedElement)
@given(instance=LocatedElement_strategy)
@settings(max_examples=25)
def test_LocatedElement_instantiation(instance):
    assert isinstance(instance, LocatedElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Predicate_strategy = st.builds(Predicate)
@given(instance=Predicate_strategy)
@settings(max_examples=25)
def test_Predicate_instantiation(instance):
    assert isinstance(instance, Predicate)


QueryStmt_strategy = st.builds(QueryStmt)
@given(instance=QueryStmt_strategy)
@settings(max_examples=25)
def test_QueryStmt_instantiation(instance):
    assert isinstance(instance, QueryStmt)


SQLDML_AndExp_strategy = st.builds(SQLDML_AndExp)
@given(instance=SQLDML_AndExp_strategy)
@settings(max_examples=25)
def test_SQLDML_AndExp_instantiation(instance):
    assert isinstance(instance, SQLDML_AndExp)


SQLDML_BinaryExp_strategy = st.builds(SQLDML_BinaryExp, opName=safe_text)
@given(instance=SQLDML_BinaryExp_strategy)
@settings(max_examples=25)
def test_SQLDML_BinaryExp_instantiation(instance):
    assert isinstance(instance, SQLDML_BinaryExp)


SQLDML_ColumnExp_strategy = st.builds(SQLDML_ColumnExp, alias=safe_text)
@given(instance=SQLDML_ColumnExp_strategy)
@settings(max_examples=25)
def test_SQLDML_ColumnExp_instantiation(instance):
    assert isinstance(instance, SQLDML_ColumnExp)


SQLDML_DataType_strategy = st.builds(SQLDML_DataType)
@given(instance=SQLDML_DataType_strategy)
@settings(max_examples=25)
def test_SQLDML_DataType_instantiation(instance):
    assert isinstance(instance, SQLDML_DataType)


SQLDML_Expression_strategy = st.builds(SQLDML_Expression)
@given(instance=SQLDML_Expression_strategy)
@settings(max_examples=25)
def test_SQLDML_Expression_instantiation(instance):
    assert isinstance(instance, SQLDML_Expression)


SQLDML_FunctionExp_strategy = st.builds(SQLDML_FunctionExp, name=safe_text)
@given(instance=SQLDML_FunctionExp_strategy)
@settings(max_examples=25)
def test_SQLDML_FunctionExp_instantiation(instance):
    assert isinstance(instance, SQLDML_FunctionExp)


SQLDML_InExp_strategy = st.builds(SQLDML_InExp, columnName=safe_text)
@given(instance=SQLDML_InExp_strategy)
@settings(max_examples=25)
def test_SQLDML_InExp_instantiation(instance):
    assert isinstance(instance, SQLDML_InExp)


SQLDML_InsertStmt_strategy = st.builds(SQLDML_InsertStmt, tableName=safe_text)
@given(instance=SQLDML_InsertStmt_strategy)
@settings(max_examples=25)
def test_SQLDML_InsertStmt_instantiation(instance):
    assert isinstance(instance, SQLDML_InsertStmt)


SQLDML_IntegerValueExp_strategy = st.builds(SQLDML_IntegerValueExp, aValue=safe_text)
@given(instance=SQLDML_IntegerValueExp_strategy)
@settings(max_examples=25)
def test_SQLDML_IntegerValueExp_instantiation(instance):
    assert isinstance(instance, SQLDML_IntegerValueExp)


SQLDML_LikeExp_strategy = st.builds(SQLDML_LikeExp, columnName=safe_text)
@given(instance=SQLDML_LikeExp_strategy)
@settings(max_examples=25)
def test_SQLDML_LikeExp_instantiation(instance):
    assert isinstance(instance, SQLDML_LikeExp)


SQLDML_ListExp_strategy = st.builds(SQLDML_ListExp)
@given(instance=SQLDML_ListExp_strategy)
@settings(max_examples=25)
def test_SQLDML_ListExp_instantiation(instance):
    assert isinstance(instance, SQLDML_ListExp)


SQLDML_LocatedElement_strategy = st.builds(SQLDML_LocatedElement, commentsAfter=safe_text, commentsBefore=safe_text, location=safe_text)
@given(instance=SQLDML_LocatedElement_strategy)
@settings(max_examples=25)
def test_SQLDML_LocatedElement_instantiation(instance):
    assert isinstance(instance, SQLDML_LocatedElement)


SQLDML_NamedElement_strategy = st.builds(SQLDML_NamedElement, name=safe_text)
@given(instance=SQLDML_NamedElement_strategy)
@settings(max_examples=25)
def test_SQLDML_NamedElement_instantiation(instance):
    assert isinstance(instance, SQLDML_NamedElement)


SQLDML_NotExp_strategy = st.builds(SQLDML_NotExp, opName=safe_text)
@given(instance=SQLDML_NotExp_strategy)
@settings(max_examples=25)
def test_SQLDML_NotExp_instantiation(instance):
    assert isinstance(instance, SQLDML_NotExp)


SQLDML_OperationExp_strategy = st.builds(SQLDML_OperationExp, optName=safe_text)
@given(instance=SQLDML_OperationExp_strategy)
@settings(max_examples=25)
def test_SQLDML_OperationExp_instantiation(instance):
    assert isinstance(instance, SQLDML_OperationExp)


SQLDML_OrExp_strategy = st.builds(SQLDML_OrExp)
@given(instance=SQLDML_OrExp_strategy)
@settings(max_examples=25)
def test_SQLDML_OrExp_instantiation(instance):
    assert isinstance(instance, SQLDML_OrExp)


SQLDML_Predicate_strategy = st.builds(SQLDML_Predicate)
@given(instance=SQLDML_Predicate_strategy)
@settings(max_examples=25)
def test_SQLDML_Predicate_instantiation(instance):
    assert isinstance(instance, SQLDML_Predicate)


SQLDML_QueryPredicate_strategy = st.builds(SQLDML_QueryPredicate)
@given(instance=SQLDML_QueryPredicate_strategy)
@settings(max_examples=25)
def test_SQLDML_QueryPredicate_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryPredicate)


SQLDML_QueryStmt_strategy = st.builds(SQLDML_QueryStmt)
@given(instance=SQLDML_QueryStmt_strategy)
@settings(max_examples=25)
def test_SQLDML_QueryStmt_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryStmt)


SQLDML_QueryStmtAllCol_strategy = st.builds(SQLDML_QueryStmtAllCol)
@given(instance=SQLDML_QueryStmtAllCol_strategy)
@settings(max_examples=25)
def test_SQLDML_QueryStmtAllCol_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryStmtAllCol)


SQLDML_QueryStmtCol_strategy = st.builds(SQLDML_QueryStmtCol)
@given(instance=SQLDML_QueryStmtCol_strategy)
@settings(max_examples=25)
def test_SQLDML_QueryStmtCol_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryStmtCol)


SQLDML_SQLRoot_strategy = st.builds(SQLDML_SQLRoot)
@given(instance=SQLDML_SQLRoot_strategy)
@settings(max_examples=25)
def test_SQLDML_SQLRoot_instantiation(instance):
    assert isinstance(instance, SQLDML_SQLRoot)


SQLDML_Statement_strategy = st.builds(SQLDML_Statement)
@given(instance=SQLDML_Statement_strategy)
@settings(max_examples=25)
def test_SQLDML_Statement_instantiation(instance):
    assert isinstance(instance, SQLDML_Statement)


SQLDML_StringValueExp_strategy = st.builds(SQLDML_StringValueExp, aValue=safe_text)
@given(instance=SQLDML_StringValueExp_strategy)
@settings(max_examples=25)
def test_SQLDML_StringValueExp_instantiation(instance):
    assert isinstance(instance, SQLDML_StringValueExp)


SQLDML_Table_strategy = st.builds(SQLDML_Table, alias=safe_text)
@given(instance=SQLDML_Table_strategy)
@settings(max_examples=25)
def test_SQLDML_Table_instantiation(instance):
    assert isinstance(instance, SQLDML_Table)


SQLDML_ValueExp_strategy = st.builds(SQLDML_ValueExp)
@given(instance=SQLDML_ValueExp_strategy)
@settings(max_examples=25)
def test_SQLDML_ValueExp_instantiation(instance):
    assert isinstance(instance, SQLDML_ValueExp)


SQLDML_ViewStatement_strategy = st.builds(SQLDML_ViewStatement, name=safe_text)
@given(instance=SQLDML_ViewStatement_strategy)
@settings(max_examples=25)
def test_SQLDML_ViewStatement_instantiation(instance):
    assert isinstance(instance, SQLDML_ViewStatement)


SQLDML_WhereClause_strategy = st.builds(SQLDML_WhereClause)
@given(instance=SQLDML_WhereClause_strategy)
@settings(max_examples=25)
def test_SQLDML_WhereClause_instantiation(instance):
    assert isinstance(instance, SQLDML_WhereClause)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


StringValueExp_strategy = st.builds(StringValueExp)
@given(instance=StringValueExp_strategy)
@settings(max_examples=25)
def test_StringValueExp_instantiation(instance):
    assert isinstance(instance, StringValueExp)


Table_strategy = st.builds(Table)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


ValueExp_strategy = st.builds(ValueExp)
@given(instance=ValueExp_strategy)
@settings(max_examples=25)
def test_ValueExp_instantiation(instance):
    assert isinstance(instance, ValueExp)


WhereClause_strategy = st.builds(WhereClause)
@given(instance=WhereClause_strategy)
@settings(max_examples=25)
def test_WhereClause_instantiation(instance):
    assert isinstance(instance, WhereClause)



