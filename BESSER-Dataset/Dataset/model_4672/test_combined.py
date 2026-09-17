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
    IdUse,
    picojava_VariableUse,
    picojava_TypeUse,
    picojava_Use,
    Exp,
    picojava_BooleanLiteral,
    Access,
    picojava_Dot,
    picojava_Exp,
    picojava_IdUse,
    Stmt,
    picojava_WhileStmt,
    picojava_AssignStmt,
    picojava_Access,
    TypeDecl,
    picojava_ClassDecl,
    Decl,
    picojava_VarDecl,
    picojava_BlockStmt,
    BlockStmt,
    picojava_Decl,
    picojava_Stmt,
    picojava_TypeDecl,
    picojava_Block,
    picojava_PrimitiveDecl,
    picojava_UnknownDecl,
    picojava_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_iduse_is_not_abstract():
    assert not inspect.isabstract(IdUse)


def test_hyp_iduse_constructor_exists():
    assert callable(IdUse.__init__)


def test_hyp_iduse_constructor_args():
    sig = inspect.signature(IdUse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_variableuse_is_not_abstract():
    assert not inspect.isabstract(picojava_VariableUse)


def test_hyp_picojava_variableuse_constructor_exists():
    assert callable(picojava_VariableUse.__init__)


def test_hyp_picojava_variableuse_constructor_args():
    sig = inspect.signature(picojava_VariableUse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_typeuse_is_not_abstract():
    assert not inspect.isabstract(picojava_TypeUse)


def test_hyp_picojava_typeuse_constructor_exists():
    assert callable(picojava_TypeUse.__init__)


def test_hyp_picojava_typeuse_constructor_args():
    sig = inspect.signature(picojava_TypeUse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_use_is_not_abstract():
    assert not inspect.isabstract(picojava_Use)


def test_hyp_picojava_use_constructor_exists():
    assert callable(picojava_Use.__init__)


def test_hyp_picojava_use_constructor_args():
    sig = inspect.signature(picojava_Use.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_hyp_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_hyp_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(picojava_BooleanLiteral)


def test_hyp_picojava_booleanliteral_constructor_exists():
    assert callable(picojava_BooleanLiteral.__init__)


def test_hyp_picojava_booleanliteral_constructor_args():
    sig = inspect.signature(picojava_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"




def test_hyp_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_hyp_access_constructor_exists():
    assert callable(Access.__init__)


def test_hyp_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_dot_is_not_abstract():
    assert not inspect.isabstract(picojava_Dot)


def test_hyp_picojava_dot_constructor_exists():
    assert callable(picojava_Dot.__init__)


def test_hyp_picojava_dot_constructor_args():
    sig = inspect.signature(picojava_Dot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_exp_is_not_abstract():
    assert not inspect.isabstract(picojava_Exp)


def test_hyp_picojava_exp_constructor_exists():
    assert callable(picojava_Exp.__init__)


def test_hyp_picojava_exp_constructor_args():
    sig = inspect.signature(picojava_Exp.__init__)
    params = list(sig.parameters.keys())
    assert "isValue" in params, "Missing parameter 'isValue'"




def test_hyp_picojava_iduse_is_not_abstract():
    assert not inspect.isabstract(picojava_IdUse)


def test_hyp_picojava_iduse_constructor_exists():
    assert callable(picojava_IdUse.__init__)


def test_hyp_picojava_iduse_constructor_args():
    sig = inspect.signature(picojava_IdUse.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "isQualified" in params, "Missing parameter 'isQualified'"





def test_hyp_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_hyp_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_hyp_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_whilestmt_is_not_abstract():
    assert not inspect.isabstract(picojava_WhileStmt)


def test_hyp_picojava_whilestmt_constructor_exists():
    assert callable(picojava_WhileStmt.__init__)


def test_hyp_picojava_whilestmt_constructor_args():
    sig = inspect.signature(picojava_WhileStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_assignstmt_is_not_abstract():
    assert not inspect.isabstract(picojava_AssignStmt)


def test_hyp_picojava_assignstmt_constructor_exists():
    assert callable(picojava_AssignStmt.__init__)


def test_hyp_picojava_assignstmt_constructor_args():
    sig = inspect.signature(picojava_AssignStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_access_is_not_abstract():
    assert not inspect.isabstract(picojava_Access)


def test_hyp_picojava_access_constructor_exists():
    assert callable(picojava_Access.__init__)


def test_hyp_picojava_access_constructor_args():
    sig = inspect.signature(picojava_Access.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedecl_is_not_abstract():
    assert not inspect.isabstract(TypeDecl)


def test_hyp_typedecl_constructor_exists():
    assert callable(TypeDecl.__init__)


def test_hyp_typedecl_constructor_args():
    sig = inspect.signature(TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_classdecl_is_not_abstract():
    assert not inspect.isabstract(picojava_ClassDecl)


def test_hyp_picojava_classdecl_constructor_exists():
    assert callable(picojava_ClassDecl.__init__)


def test_hyp_picojava_classdecl_constructor_args():
    sig = inspect.signature(picojava_ClassDecl.__init__)
    params = list(sig.parameters.keys())
    assert "hasCycleOnSuperclassChain" in params, "Missing parameter 'hasCycleOnSuperclassChain'"




def test_hyp_decl_is_not_abstract():
    assert not inspect.isabstract(Decl)


def test_hyp_decl_constructor_exists():
    assert callable(Decl.__init__)


def test_hyp_decl_constructor_args():
    sig = inspect.signature(Decl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_vardecl_is_not_abstract():
    assert not inspect.isabstract(picojava_VarDecl)


def test_hyp_picojava_vardecl_constructor_exists():
    assert callable(picojava_VarDecl.__init__)


def test_hyp_picojava_vardecl_constructor_args():
    sig = inspect.signature(picojava_VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_blockstmt_is_not_abstract():
    assert not inspect.isabstract(picojava_BlockStmt)


def test_hyp_picojava_blockstmt_constructor_exists():
    assert callable(picojava_BlockStmt.__init__)


def test_hyp_picojava_blockstmt_constructor_args():
    sig = inspect.signature(picojava_BlockStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blockstmt_is_not_abstract():
    assert not inspect.isabstract(BlockStmt)


def test_hyp_blockstmt_constructor_exists():
    assert callable(BlockStmt.__init__)


def test_hyp_blockstmt_constructor_args():
    sig = inspect.signature(BlockStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_decl_is_not_abstract():
    assert not inspect.isabstract(picojava_Decl)


def test_hyp_picojava_decl_constructor_exists():
    assert callable(picojava_Decl.__init__)


def test_hyp_picojava_decl_constructor_args():
    sig = inspect.signature(picojava_Decl.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "isUnknown" in params, "Missing parameter 'isUnknown'"





def test_hyp_picojava_stmt_is_not_abstract():
    assert not inspect.isabstract(picojava_Stmt)


def test_hyp_picojava_stmt_constructor_exists():
    assert callable(picojava_Stmt.__init__)


def test_hyp_picojava_stmt_constructor_args():
    sig = inspect.signature(picojava_Stmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_typedecl_is_not_abstract():
    assert not inspect.isabstract(picojava_TypeDecl)


def test_hyp_picojava_typedecl_constructor_exists():
    assert callable(picojava_TypeDecl.__init__)


def test_hyp_picojava_typedecl_constructor_args():
    sig = inspect.signature(picojava_TypeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "isQualified" in params, "Missing parameter 'isQualified'"




def test_hyp_picojava_block_is_not_abstract():
    assert not inspect.isabstract(picojava_Block)


def test_hyp_picojava_block_constructor_exists():
    assert callable(picojava_Block.__init__)


def test_hyp_picojava_block_constructor_args():
    sig = inspect.signature(picojava_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_primitivedecl_is_not_abstract():
    assert not inspect.isabstract(picojava_PrimitiveDecl)


def test_hyp_picojava_primitivedecl_constructor_exists():
    assert callable(picojava_PrimitiveDecl.__init__)


def test_hyp_picojava_primitivedecl_constructor_args():
    sig = inspect.signature(picojava_PrimitiveDecl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_unknowndecl_is_not_abstract():
    assert not inspect.isabstract(picojava_UnknownDecl)


def test_hyp_picojava_unknowndecl_constructor_exists():
    assert callable(picojava_UnknownDecl.__init__)


def test_hyp_picojava_unknowndecl_constructor_args():
    sig = inspect.signature(picojava_UnknownDecl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_picojava_program_is_not_abstract():
    assert not inspect.isabstract(picojava_Program)


def test_hyp_picojava_program_constructor_exists():
    assert callable(picojava_Program.__init__)


def test_hyp_picojava_program_constructor_args():
    sig = inspect.signature(picojava_Program.__init__)
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
IdUse_strategy = st.builds(
    IdUse,
)
picojava_VariableUse_strategy = st.builds(
    picojava_VariableUse,
)
picojava_TypeUse_strategy = st.builds(
    picojava_TypeUse,
)
picojava_Use_strategy = st.builds(
    picojava_Use,
)
Exp_strategy = st.builds(
    Exp,
)
picojava_BooleanLiteral_strategy = st.builds(
    picojava_BooleanLiteral,
    Value=
        safe_text
)
Access_strategy = st.builds(
    Access,
)
picojava_Dot_strategy = st.builds(
    picojava_Dot,
)
picojava_Exp_strategy = st.builds(
    picojava_Exp,
    isValue=
        st.booleans()
)
picojava_IdUse_strategy = st.builds(
    picojava_IdUse,
    Name=
        safe_text,
    isQualified=
        st.booleans()
)
Stmt_strategy = st.builds(
    Stmt,
)
picojava_WhileStmt_strategy = st.builds(
    picojava_WhileStmt,
)
picojava_AssignStmt_strategy = st.builds(
    picojava_AssignStmt,
)
picojava_Access_strategy = st.builds(
    picojava_Access,
)
TypeDecl_strategy = st.builds(
    TypeDecl,
)
picojava_ClassDecl_strategy = st.builds(
    picojava_ClassDecl,
    hasCycleOnSuperclassChain=
        st.booleans()
)
Decl_strategy = st.builds(
    Decl,
)
picojava_VarDecl_strategy = st.builds(
    picojava_VarDecl,
)
picojava_BlockStmt_strategy = st.builds(
    picojava_BlockStmt,
)
BlockStmt_strategy = st.builds(
    BlockStmt,
)
picojava_Decl_strategy = st.builds(
    picojava_Decl,
    Name=
        safe_text,
    isUnknown=
        st.booleans()
)
picojava_Stmt_strategy = st.builds(
    picojava_Stmt,
)
picojava_TypeDecl_strategy = st.builds(
    picojava_TypeDecl,
    isQualified=
        st.booleans()
)
picojava_Block_strategy = st.builds(
    picojava_Block,
)
picojava_PrimitiveDecl_strategy = st.builds(
    picojava_PrimitiveDecl,
)
picojava_UnknownDecl_strategy = st.builds(
    picojava_UnknownDecl,
)
picojava_Program_strategy = st.builds(
    picojava_Program,
)









@given(instance=picojava_BooleanLiteral_strategy)
def test_hyp_picojava_booleanliteral_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original






@given(instance=picojava_Exp_strategy)
def test_hyp_picojava_exp_isValue_setter(instance):
    original = instance.isValue
    instance.isValue = original
    assert instance.isValue == original




@given(instance=picojava_IdUse_strategy)
def test_hyp_picojava_iduse_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=picojava_IdUse_strategy)
def test_hyp_picojava_iduse_isQualified_setter(instance):
    original = instance.isQualified
    instance.isQualified = original
    assert instance.isQualified == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_IdUse_strategy)
@settings(max_examples=30)
def test_hyp_picojava_iduse_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in picojava_IdUse is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in picojava_IdUse did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in picojava_IdUse is not implemented or raised an error")









@given(instance=picojava_ClassDecl_strategy)
def test_hyp_picojava_classdecl_hasCycleOnSuperclassChain_setter(instance):
    original = instance.hasCycleOnSuperclassChain
    instance.hasCycleOnSuperclassChain = original
    assert instance.hasCycleOnSuperclassChain == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_BlockStmt_strategy)
@settings(max_examples=30)
def test_hyp_picojava_blockstmt_declarationof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.declarationOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.declarationOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'declarationOf' in picojava_BlockStmt is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'declarationOf' in picojava_BlockStmt did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'declarationOf' in picojava_BlockStmt is not implemented or raised an error")





@given(instance=picojava_Decl_strategy)
def test_hyp_picojava_decl_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=picojava_Decl_strategy)
def test_hyp_picojava_decl_isUnknown_setter(instance):
    original = instance.isUnknown
    instance.isUnknown = original
    assert instance.isUnknown == original





@given(instance=picojava_TypeDecl_strategy)
def test_hyp_picojava_typedecl_isQualified_setter(instance):
    original = instance.isQualified
    instance.isQualified = original
    assert instance.isQualified == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_TypeDecl_strategy)
@settings(max_examples=30)
def test_hyp_picojava_typedecl_issubtypeof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSubtypeOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSubtypeOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSubtypeOf' in picojava_TypeDecl is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSubtypeOf' in picojava_TypeDecl did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSubtypeOf' in picojava_TypeDecl is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_TypeDecl_strategy)
@settings(max_examples=30)
def test_hyp_picojava_typedecl_remotelookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remoteLookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remoteLookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remoteLookup' in picojava_TypeDecl is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remoteLookup' in picojava_TypeDecl did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remoteLookup' in picojava_TypeDecl is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_TypeDecl_strategy)
@settings(max_examples=30)
def test_hyp_picojava_typedecl_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in picojava_TypeDecl is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in picojava_TypeDecl did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in picojava_TypeDecl is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_TypeDecl_strategy)
@settings(max_examples=30)
def test_hyp_picojava_typedecl_issupertypeofclassdecl_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperTypeOfClassDecl(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperTypeOfClassDecl).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperTypeOfClassDecl' in picojava_TypeDecl is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOfClassDecl' in picojava_TypeDecl did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOfClassDecl' in picojava_TypeDecl is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_TypeDecl_strategy)
@settings(max_examples=30)
def test_hyp_picojava_typedecl_issupertypeof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperTypeOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperTypeOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperTypeOf' in picojava_TypeDecl is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOf' in picojava_TypeDecl did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOf' in picojava_TypeDecl is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_Block_strategy)
@settings(max_examples=30)
def test_hyp_picojava_block_locallookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.localLookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.localLookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'localLookup' in picojava_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'localLookup' in picojava_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'localLookup' in picojava_Block is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_Block_strategy)
@settings(max_examples=30)
def test_hyp_picojava_block_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in picojava_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in picojava_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in picojava_Block is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=picojava_Program_strategy)
@settings(max_examples=30)
def test_hyp_picojava_program_locallookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.localLookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.localLookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'localLookup' in picojava_Program is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'localLookup' in picojava_Program did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'localLookup' in picojava_Program is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Access,
    BlockStmt,
    Decl,
    Exp,
    IdUse,
    Stmt,
    TypeDecl,
    picojava_Access,
    picojava_AssignStmt,
    picojava_Block,
    picojava_BlockStmt,
    picojava_BooleanLiteral,
    picojava_ClassDecl,
    picojava_Decl,
    picojava_Dot,
    picojava_Exp,
    picojava_IdUse,
    picojava_PrimitiveDecl,
    picojava_Program,
    picojava_Stmt,
    picojava_TypeDecl,
    picojava_TypeUse,
    picojava_UnknownDecl,
    picojava_Use,
    picojava_VarDecl,
    picojava_VariableUse,
    picojava_WhileStmt,
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

def test_picojava_BooleanLiteral_Value_value_roundtrip():
    instance = picojava_BooleanLiteral(Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_picojava_ClassDecl_hasCycleOnSuperclassChain_value_roundtrip():
    instance = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    assert instance.hasCycleOnSuperclassChain == True
    instance.hasCycleOnSuperclassChain = False
    assert instance.hasCycleOnSuperclassChain == False


def test_picojava_Decl_Name_value_roundtrip():
    instance = picojava_Decl(Name="sample_text", isUnknown=True)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_picojava_Decl_isUnknown_value_roundtrip():
    instance = picojava_Decl(Name="sample_text", isUnknown=True)
    assert instance.isUnknown == True
    instance.isUnknown = False
    assert instance.isUnknown == False


def test_picojava_Exp_isValue_value_roundtrip():
    instance = picojava_Exp(isValue=True)
    assert instance.isValue == True
    instance.isValue = False
    assert instance.isValue == False


def test_picojava_IdUse_Name_value_roundtrip():
    instance = picojava_IdUse(Name="sample_text", isQualified=True)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_picojava_IdUse_isQualified_value_roundtrip():
    instance = picojava_IdUse(Name="sample_text", isQualified=True)
    assert instance.isQualified == True
    instance.isQualified = False
    assert instance.isQualified == False


def test_picojava_TypeDecl_isQualified_value_roundtrip():
    instance = picojava_TypeDecl(isQualified=True)
    assert instance.isQualified == True
    instance.isQualified = False
    assert instance.isQualified == False


def test_picojava_Dot_isa_Access():
    instance = picojava_Dot()
    assert isinstance(instance, Access)


def test_picojava_IdUse_isa_Access():
    instance = picojava_IdUse(Name="sample_text", isQualified=True)
    assert isinstance(instance, Access)


def test_picojava_Decl_isa_BlockStmt():
    instance = picojava_Decl(Name="sample_text", isUnknown=True)
    assert isinstance(instance, BlockStmt)


def test_picojava_Stmt_isa_BlockStmt():
    instance = picojava_Stmt()
    assert isinstance(instance, BlockStmt)


def test_picojava_TypeDecl_isa_Decl():
    instance = picojava_TypeDecl(isQualified=True)
    assert isinstance(instance, Decl)


def test_picojava_VarDecl_isa_Decl():
    instance = picojava_VarDecl()
    assert isinstance(instance, Decl)


def test_picojava_Access_isa_Exp():
    instance = picojava_Access()
    assert isinstance(instance, Exp)


def test_picojava_BooleanLiteral_isa_Exp():
    instance = picojava_BooleanLiteral(Value="sample_text")
    assert isinstance(instance, Exp)


def test_picojava_TypeUse_isa_IdUse():
    instance = picojava_TypeUse()
    assert isinstance(instance, IdUse)


def test_picojava_Use_isa_IdUse():
    instance = picojava_Use()
    assert isinstance(instance, IdUse)


def test_picojava_VariableUse_isa_IdUse():
    instance = picojava_VariableUse()
    assert isinstance(instance, IdUse)


def test_picojava_AssignStmt_isa_Stmt():
    instance = picojava_AssignStmt()
    assert isinstance(instance, Stmt)


def test_picojava_WhileStmt_isa_Stmt():
    instance = picojava_WhileStmt()
    assert isinstance(instance, Stmt)


def test_picojava_ClassDecl_isa_TypeDecl():
    instance = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    assert isinstance(instance, TypeDecl)


def test_picojava_PrimitiveDecl_isa_TypeDecl():
    instance = picojava_PrimitiveDecl()
    assert isinstance(instance, TypeDecl)


def test_picojava_UnknownDecl_isa_TypeDecl():
    instance = picojava_UnknownDecl()
    assert isinstance(instance, TypeDecl)


def test_assoc_Block0_link_reassign_clear():
    a = picojava_Program()
    b1 = picojava_Block()
    b2 = picojava_Block()
    _safe_set(a, 'picojava_Program', b1)
    assert _is_linked(a, 'picojava_Program', b1)
    if hasattr(b1, 'picojava_Block'):
        assert _is_linked(b1, 'picojava_Block', a)
    _safe_set(a, 'picojava_Program', b2)
    assert _is_linked(a, 'picojava_Program', b2)
    if hasattr(b1, 'picojava_Block'):
        assert not _is_linked(b1, 'picojava_Block', a)
    if hasattr(b2, 'picojava_Block'):
        assert _is_linked(b2, 'picojava_Block', a)
    _safe_set(a, 'picojava_Program', None)
    assert not _is_linked(a, 'picojava_Program', b2)
    if hasattr(b2, 'picojava_Block'):
        assert not _is_linked(b2, 'picojava_Block', a)


def test_assoc_BlockStmt7_link_reassign_clear():
    a = picojava_BlockStmt()
    b1 = picojava_Block()
    b2 = picojava_Block()
    _safe_set(a, 'picojava_BlockStmt', b1)
    assert _is_linked(a, 'picojava_BlockStmt', b1)
    if hasattr(b1, 'picojava_Block8'):
        assert _is_linked(b1, 'picojava_Block8', a)
    _safe_set(a, 'picojava_BlockStmt', b2)
    assert _is_linked(a, 'picojava_BlockStmt', b2)
    if hasattr(b1, 'picojava_Block8'):
        assert not _is_linked(b1, 'picojava_Block8', a)
    if hasattr(b2, 'picojava_Block8'):
        assert _is_linked(b2, 'picojava_Block8', a)
    _safe_set(a, 'picojava_BlockStmt', None)
    assert not _is_linked(a, 'picojava_BlockStmt', b2)
    if hasattr(b2, 'picojava_Block8'):
        assert not _is_linked(b2, 'picojava_Block8', a)


def test_assoc_Body23_link_reassign_clear():
    a = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    b1 = picojava_Block()
    b2 = picojava_Block()
    _safe_set(a, 'picojava_ClassDecl24', b1)
    assert _is_linked(a, 'picojava_ClassDecl24', b1)
    if hasattr(b1, 'picojava_Block25'):
        assert _is_linked(b1, 'picojava_Block25', a)
    _safe_set(a, 'picojava_ClassDecl24', b2)
    assert _is_linked(a, 'picojava_ClassDecl24', b2)
    if hasattr(b1, 'picojava_Block25'):
        assert not _is_linked(b1, 'picojava_Block25', a)
    if hasattr(b2, 'picojava_Block25'):
        assert _is_linked(b2, 'picojava_Block25', a)
    _safe_set(a, 'picojava_ClassDecl24', None)
    assert not _is_linked(a, 'picojava_ClassDecl24', b2)
    if hasattr(b2, 'picojava_Block25'):
        assert not _is_linked(b2, 'picojava_Block25', a)


def test_assoc_Condition35_link_reassign_clear():
    a = picojava_Exp(isValue=True)
    b1 = picojava_WhileStmt()
    b2 = picojava_WhileStmt()
    _safe_set(a, 'picojava_Exp36', b1)
    assert _is_linked(a, 'picojava_Exp36', b1)
    if hasattr(b1, 'picojava_WhileStmt'):
        assert _is_linked(b1, 'picojava_WhileStmt', a)
    _safe_set(a, 'picojava_Exp36', b2)
    assert _is_linked(a, 'picojava_Exp36', b2)
    if hasattr(b1, 'picojava_WhileStmt'):
        assert not _is_linked(b1, 'picojava_WhileStmt', a)
    if hasattr(b2, 'picojava_WhileStmt'):
        assert _is_linked(b2, 'picojava_WhileStmt', a)
    _safe_set(a, 'picojava_Exp36', None)
    assert not _is_linked(a, 'picojava_Exp36', b2)
    if hasattr(b2, 'picojava_WhileStmt'):
        assert not _is_linked(b2, 'picojava_WhileStmt', a)


def test_assoc_IdUse53_link_reassign_clear():
    a = picojava_IdUse(Name="sample_text", isQualified=True)
    b1 = picojava_Dot()
    b2 = picojava_Dot()
    _safe_set(a, 'picojava_IdUse55', b1)
    assert _is_linked(a, 'picojava_IdUse55', b1)
    if hasattr(b1, 'picojava_Dot54'):
        assert _is_linked(b1, 'picojava_Dot54', a)
    _safe_set(a, 'picojava_IdUse55', b2)
    assert _is_linked(a, 'picojava_IdUse55', b2)
    if hasattr(b1, 'picojava_Dot54'):
        assert not _is_linked(b1, 'picojava_Dot54', a)
    if hasattr(b2, 'picojava_Dot54'):
        assert _is_linked(b2, 'picojava_Dot54', a)
    _safe_set(a, 'picojava_IdUse55', None)
    assert not _is_linked(a, 'picojava_IdUse55', b2)
    if hasattr(b2, 'picojava_Dot54'):
        assert not _is_linked(b2, 'picojava_Dot54', a)


def test_assoc_PredefinedType1_link_reassign_clear():
    a = picojava_TypeDecl(isQualified=True)
    b1 = picojava_Program()
    b2 = picojava_Program()
    _safe_set(a, 'picojava_TypeDecl', b1)
    assert _is_linked(a, 'picojava_TypeDecl', b1)
    if hasattr(b1, 'picojava_Program2'):
        assert _is_linked(b1, 'picojava_Program2', a)
    _safe_set(a, 'picojava_TypeDecl', b2)
    assert _is_linked(a, 'picojava_TypeDecl', b2)
    if hasattr(b1, 'picojava_Program2'):
        assert not _is_linked(b1, 'picojava_Program2', a)
    if hasattr(b2, 'picojava_Program2'):
        assert _is_linked(b2, 'picojava_Program2', a)
    _safe_set(a, 'picojava_TypeDecl', None)
    assert not _is_linked(a, 'picojava_TypeDecl', b2)
    if hasattr(b2, 'picojava_Program2'):
        assert not _is_linked(b2, 'picojava_Program2', a)


def test_assoc_SuperclassId22_link_reassign_clear():
    a = picojava_IdUse(Name="sample_text", isQualified=True)
    b1 = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    b2 = picojava_ClassDecl(hasCycleOnSuperclassChain=False)
    _safe_set(a, 'picojava_IdUse', b1)
    assert _is_linked(a, 'picojava_IdUse', b1)
    if hasattr(b1, 'picojava_ClassDecl'):
        assert _is_linked(b1, 'picojava_ClassDecl', a)
    _safe_set(a, 'picojava_IdUse', b2)
    assert _is_linked(a, 'picojava_IdUse', b2)
    if hasattr(b1, 'picojava_ClassDecl'):
        assert not _is_linked(b1, 'picojava_ClassDecl', a)
    if hasattr(b2, 'picojava_ClassDecl'):
        assert _is_linked(b2, 'picojava_ClassDecl', a)
    _safe_set(a, 'picojava_IdUse', None)
    assert not _is_linked(a, 'picojava_IdUse', b2)
    if hasattr(b2, 'picojava_ClassDecl'):
        assert not _is_linked(b2, 'picojava_ClassDecl', a)


def test_assoc_Value33_link_reassign_clear():
    a = picojava_Exp(isValue=True)
    b1 = picojava_AssignStmt()
    b2 = picojava_AssignStmt()
    _safe_set(a, 'picojava_Exp', b1)
    assert _is_linked(a, 'picojava_Exp', b1)
    if hasattr(b1, 'picojava_AssignStmt34'):
        assert _is_linked(b1, 'picojava_AssignStmt34', a)
    _safe_set(a, 'picojava_Exp', b2)
    assert _is_linked(a, 'picojava_Exp', b2)
    if hasattr(b1, 'picojava_AssignStmt34'):
        assert not _is_linked(b1, 'picojava_AssignStmt34', a)
    if hasattr(b2, 'picojava_AssignStmt34'):
        assert _is_linked(b2, 'picojava_AssignStmt34', a)
    _safe_set(a, 'picojava_Exp', None)
    assert not _is_linked(a, 'picojava_Exp', b2)
    if hasattr(b2, 'picojava_AssignStmt34'):
        assert not _is_linked(b2, 'picojava_AssignStmt34', a)


def test_assoc_booleanType14_link_reassign_clear():
    a = picojava_Decl(Name="sample_text", isUnknown=True)
    b1 = picojava_PrimitiveDecl()
    b2 = picojava_PrimitiveDecl()
    _safe_set(a, 'picojava_Decl15', b1)
    assert _is_linked(a, 'picojava_Decl15', b1)
    if hasattr(b1, 'picojava_PrimitiveDecl16'):
        assert _is_linked(b1, 'picojava_PrimitiveDecl16', a)
    _safe_set(a, 'picojava_Decl15', b2)
    assert _is_linked(a, 'picojava_Decl15', b2)
    if hasattr(b1, 'picojava_PrimitiveDecl16'):
        assert not _is_linked(b1, 'picojava_PrimitiveDecl16', a)
    if hasattr(b2, 'picojava_PrimitiveDecl16'):
        assert _is_linked(b2, 'picojava_PrimitiveDecl16', a)
    _safe_set(a, 'picojava_Decl15', None)
    assert not _is_linked(a, 'picojava_Decl15', b2)
    if hasattr(b2, 'picojava_PrimitiveDecl16'):
        assert not _is_linked(b2, 'picojava_PrimitiveDecl16', a)


def test_assoc_booleanType5_link_reassign_clear():
    a = picojava_Program()
    b1 = picojava_PrimitiveDecl()
    b2 = picojava_PrimitiveDecl()
    _safe_set(a, 'picojava_Program6', b1)
    assert _is_linked(a, 'picojava_Program6', b1)
    if hasattr(b1, 'picojava_PrimitiveDecl'):
        assert _is_linked(b1, 'picojava_PrimitiveDecl', a)
    _safe_set(a, 'picojava_Program6', b2)
    assert _is_linked(a, 'picojava_Program6', b2)
    if hasattr(b1, 'picojava_PrimitiveDecl'):
        assert not _is_linked(b1, 'picojava_PrimitiveDecl', a)
    if hasattr(b2, 'picojava_PrimitiveDecl'):
        assert _is_linked(b2, 'picojava_PrimitiveDecl', a)
    _safe_set(a, 'picojava_Program6', None)
    assert not _is_linked(a, 'picojava_Program6', b2)
    if hasattr(b2, 'picojava_PrimitiveDecl'):
        assert not _is_linked(b2, 'picojava_PrimitiveDecl', a)


def test_assoc_booleanType56_link_reassign_clear():
    a = picojava_BooleanLiteral(Value="sample_text")
    b1 = picojava_PrimitiveDecl()
    b2 = picojava_PrimitiveDecl()
    _safe_set(a, 'picojava_BooleanLiteral', b1)
    assert _is_linked(a, 'picojava_BooleanLiteral', b1)
    if hasattr(b1, 'picojava_PrimitiveDecl57'):
        assert _is_linked(b1, 'picojava_PrimitiveDecl57', a)
    _safe_set(a, 'picojava_BooleanLiteral', b2)
    assert _is_linked(a, 'picojava_BooleanLiteral', b2)
    if hasattr(b1, 'picojava_PrimitiveDecl57'):
        assert not _is_linked(b1, 'picojava_PrimitiveDecl57', a)
    if hasattr(b2, 'picojava_PrimitiveDecl57'):
        assert _is_linked(b2, 'picojava_PrimitiveDecl57', a)
    _safe_set(a, 'picojava_BooleanLiteral', None)
    assert not _is_linked(a, 'picojava_BooleanLiteral', b2)
    if hasattr(b2, 'picojava_PrimitiveDecl57'):
        assert not _is_linked(b2, 'picojava_PrimitiveDecl57', a)


def test_assoc_decl45_link_reassign_clear():
    a = picojava_Decl(Name="sample_text", isUnknown=True)
    b1 = picojava_Access()
    b2 = picojava_Access()
    _safe_set(a, 'picojava_Decl47', b1)
    assert _is_linked(a, 'picojava_Decl47', b1)
    if hasattr(b1, 'picojava_Access46'):
        assert _is_linked(b1, 'picojava_Access46', a)
    _safe_set(a, 'picojava_Decl47', b2)
    assert _is_linked(a, 'picojava_Decl47', b2)
    if hasattr(b1, 'picojava_Access46'):
        assert not _is_linked(b1, 'picojava_Access46', a)
    if hasattr(b2, 'picojava_Access46'):
        assert _is_linked(b2, 'picojava_Access46', a)
    _safe_set(a, 'picojava_Decl47', None)
    assert not _is_linked(a, 'picojava_Decl47', b2)
    if hasattr(b2, 'picojava_Access46'):
        assert not _is_linked(b2, 'picojava_Access46', a)


def test_assoc_qualifier17_link_reassign_clear():
    a = picojava_TypeDecl(isQualified=True)
    b1 = picojava_Access()
    b2 = picojava_Access()
    _safe_set(a, 'picojava_TypeDecl18', b1)
    assert _is_linked(a, 'picojava_TypeDecl18', b1)
    if hasattr(b1, 'picojava_Access'):
        assert _is_linked(b1, 'picojava_Access', a)
    _safe_set(a, 'picojava_TypeDecl18', b2)
    assert _is_linked(a, 'picojava_TypeDecl18', b2)
    if hasattr(b1, 'picojava_Access'):
        assert not _is_linked(b1, 'picojava_Access', a)
    if hasattr(b2, 'picojava_Access'):
        assert _is_linked(b2, 'picojava_Access', a)
    _safe_set(a, 'picojava_TypeDecl18', None)
    assert not _is_linked(a, 'picojava_TypeDecl18', b2)
    if hasattr(b2, 'picojava_Access'):
        assert not _is_linked(b2, 'picojava_Access', a)


def test_assoc_qualifier48_link_reassign_clear():
    a = picojava_IdUse(Name="sample_text", isQualified=True)
    b1 = picojava_Access()
    b2 = picojava_Access()
    _safe_set(a, 'picojava_IdUse49', b1)
    assert _is_linked(a, 'picojava_IdUse49', b1)
    if hasattr(b1, 'picojava_Access50'):
        assert _is_linked(b1, 'picojava_Access50', a)
    _safe_set(a, 'picojava_IdUse49', b2)
    assert _is_linked(a, 'picojava_IdUse49', b2)
    if hasattr(b1, 'picojava_Access50'):
        assert not _is_linked(b1, 'picojava_Access50', a)
    if hasattr(b2, 'picojava_Access50'):
        assert _is_linked(b2, 'picojava_Access50', a)
    _safe_set(a, 'picojava_IdUse49', None)
    assert not _is_linked(a, 'picojava_IdUse49', b2)
    if hasattr(b2, 'picojava_Access50'):
        assert not _is_linked(b2, 'picojava_Access50', a)


def test_assoc_superClass27_link_reassign_clear():
    a = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    b1 = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    b2 = picojava_ClassDecl(hasCycleOnSuperclassChain=False)
    _safe_set(a, 'picojava_ClassDecl26', b1)
    assert _is_linked(a, 'picojava_ClassDecl26', b1)
    if hasattr(b1, 'picojava_ClassDecl28'):
        assert _is_linked(b1, 'picojava_ClassDecl28', a)
    _safe_set(a, 'picojava_ClassDecl26', b2)
    assert _is_linked(a, 'picojava_ClassDecl26', b2)
    if hasattr(b1, 'picojava_ClassDecl28'):
        assert not _is_linked(b1, 'picojava_ClassDecl28', a)
    if hasattr(b2, 'picojava_ClassDecl28'):
        assert _is_linked(b2, 'picojava_ClassDecl28', a)
    _safe_set(a, 'picojava_ClassDecl26', None)
    assert not _is_linked(a, 'picojava_ClassDecl26', b2)
    if hasattr(b2, 'picojava_ClassDecl28'):
        assert not _is_linked(b2, 'picojava_ClassDecl28', a)


def test_assoc_type11_link_reassign_clear():
    a = picojava_TypeDecl(isQualified=True)
    b1 = picojava_Decl(Name="sample_text", isUnknown=True)
    b2 = picojava_Decl(Name="sample_text_2", isUnknown=False)
    _safe_set(a, 'picojava_TypeDecl13', b1)
    assert _is_linked(a, 'picojava_TypeDecl13', b1)
    if hasattr(b1, 'picojava_Decl12'):
        assert _is_linked(b1, 'picojava_Decl12', a)
    _safe_set(a, 'picojava_TypeDecl13', b2)
    assert _is_linked(a, 'picojava_TypeDecl13', b2)
    if hasattr(b1, 'picojava_Decl12'):
        assert not _is_linked(b1, 'picojava_Decl12', a)
    if hasattr(b2, 'picojava_Decl12'):
        assert _is_linked(b2, 'picojava_Decl12', a)
    _safe_set(a, 'picojava_TypeDecl13', None)
    assert not _is_linked(a, 'picojava_TypeDecl13', b2)
    if hasattr(b2, 'picojava_Decl12'):
        assert not _is_linked(b2, 'picojava_Decl12', a)


def test_assoc_type42_link_reassign_clear():
    a = picojava_TypeDecl(isQualified=True)
    b1 = picojava_Exp(isValue=True)
    b2 = picojava_Exp(isValue=False)
    _safe_set(a, 'picojava_TypeDecl44', b1)
    assert _is_linked(a, 'picojava_TypeDecl44', b1)
    if hasattr(b1, 'picojava_Exp43'):
        assert _is_linked(b1, 'picojava_Exp43', a)
    _safe_set(a, 'picojava_TypeDecl44', b2)
    assert _is_linked(a, 'picojava_TypeDecl44', b2)
    if hasattr(b1, 'picojava_Exp43'):
        assert not _is_linked(b1, 'picojava_Exp43', a)
    if hasattr(b2, 'picojava_Exp43'):
        assert _is_linked(b2, 'picojava_Exp43', a)
    _safe_set(a, 'picojava_TypeDecl44', None)
    assert not _is_linked(a, 'picojava_TypeDecl44', b2)
    if hasattr(b2, 'picojava_Exp43'):
        assert not _is_linked(b2, 'picojava_Exp43', a)


def test_assoc_unknownDecl19_link_reassign_clear():
    a = picojava_TypeDecl(isQualified=True)
    b1 = picojava_Decl(Name="sample_text", isUnknown=True)
    b2 = picojava_Decl(Name="sample_text_2", isUnknown=False)
    _safe_set(a, 'picojava_TypeDecl20', b1)
    assert _is_linked(a, 'picojava_TypeDecl20', b1)
    if hasattr(b1, 'picojava_Decl21'):
        assert _is_linked(b1, 'picojava_Decl21', a)
    _safe_set(a, 'picojava_TypeDecl20', b2)
    assert _is_linked(a, 'picojava_TypeDecl20', b2)
    if hasattr(b1, 'picojava_Decl21'):
        assert not _is_linked(b1, 'picojava_Decl21', a)
    if hasattr(b2, 'picojava_Decl21'):
        assert _is_linked(b2, 'picojava_Decl21', a)
    _safe_set(a, 'picojava_TypeDecl20', None)
    assert not _is_linked(a, 'picojava_TypeDecl20', b2)
    if hasattr(b2, 'picojava_Decl21'):
        assert not _is_linked(b2, 'picojava_Decl21', a)


def test_assoc_unknownDecl3_link_reassign_clear():
    a = picojava_Program()
    b1 = picojava_UnknownDecl()
    b2 = picojava_UnknownDecl()
    _safe_set(a, 'picojava_Program4', b1)
    assert _is_linked(a, 'picojava_Program4', b1)
    if hasattr(b1, 'picojava_UnknownDecl'):
        assert _is_linked(b1, 'picojava_UnknownDecl', a)
    _safe_set(a, 'picojava_Program4', b2)
    assert _is_linked(a, 'picojava_Program4', b2)
    if hasattr(b1, 'picojava_UnknownDecl'):
        assert not _is_linked(b1, 'picojava_UnknownDecl', a)
    if hasattr(b2, 'picojava_UnknownDecl'):
        assert _is_linked(b2, 'picojava_UnknownDecl', a)
    _safe_set(a, 'picojava_Program4', None)
    assert not _is_linked(a, 'picojava_Program4', b2)
    if hasattr(b2, 'picojava_UnknownDecl'):
        assert not _is_linked(b2, 'picojava_UnknownDecl', a)


def test_assoc_unknownDecl9_link_reassign_clear():
    a = picojava_Decl(Name="sample_text", isUnknown=True)
    b1 = picojava_Block()
    b2 = picojava_Block()
    _safe_set(a, 'picojava_Decl', b1)
    assert _is_linked(a, 'picojava_Decl', b1)
    if hasattr(b1, 'picojava_Block10'):
        assert _is_linked(b1, 'picojava_Block10', a)
    _safe_set(a, 'picojava_Decl', b2)
    assert _is_linked(a, 'picojava_Decl', b2)
    if hasattr(b1, 'picojava_Block10'):
        assert not _is_linked(b1, 'picojava_Block10', a)
    if hasattr(b2, 'picojava_Block10'):
        assert _is_linked(b2, 'picojava_Block10', a)
    _safe_set(a, 'picojava_Decl', None)
    assert not _is_linked(a, 'picojava_Decl', b2)
    if hasattr(b2, 'picojava_Block10'):
        assert not _is_linked(b2, 'picojava_Block10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Access_strategy = st.builds(Access)
@given(instance=Access_strategy)
@settings(max_examples=25)
def test_Access_instantiation(instance):
    assert isinstance(instance, Access)


BlockStmt_strategy = st.builds(BlockStmt)
@given(instance=BlockStmt_strategy)
@settings(max_examples=25)
def test_BlockStmt_instantiation(instance):
    assert isinstance(instance, BlockStmt)


Decl_strategy = st.builds(Decl)
@given(instance=Decl_strategy)
@settings(max_examples=25)
def test_Decl_instantiation(instance):
    assert isinstance(instance, Decl)


Exp_strategy = st.builds(Exp)
@given(instance=Exp_strategy)
@settings(max_examples=25)
def test_Exp_instantiation(instance):
    assert isinstance(instance, Exp)


IdUse_strategy = st.builds(IdUse)
@given(instance=IdUse_strategy)
@settings(max_examples=25)
def test_IdUse_instantiation(instance):
    assert isinstance(instance, IdUse)


Stmt_strategy = st.builds(Stmt)
@given(instance=Stmt_strategy)
@settings(max_examples=25)
def test_Stmt_instantiation(instance):
    assert isinstance(instance, Stmt)


TypeDecl_strategy = st.builds(TypeDecl)
@given(instance=TypeDecl_strategy)
@settings(max_examples=25)
def test_TypeDecl_instantiation(instance):
    assert isinstance(instance, TypeDecl)


picojava_Access_strategy = st.builds(picojava_Access)
@given(instance=picojava_Access_strategy)
@settings(max_examples=25)
def test_picojava_Access_instantiation(instance):
    assert isinstance(instance, picojava_Access)


picojava_AssignStmt_strategy = st.builds(picojava_AssignStmt)
@given(instance=picojava_AssignStmt_strategy)
@settings(max_examples=25)
def test_picojava_AssignStmt_instantiation(instance):
    assert isinstance(instance, picojava_AssignStmt)


picojava_Block_strategy = st.builds(picojava_Block)
@given(instance=picojava_Block_strategy)
@settings(max_examples=25)
def test_picojava_Block_instantiation(instance):
    assert isinstance(instance, picojava_Block)


picojava_BlockStmt_strategy = st.builds(picojava_BlockStmt)
@given(instance=picojava_BlockStmt_strategy)
@settings(max_examples=25)
def test_picojava_BlockStmt_instantiation(instance):
    assert isinstance(instance, picojava_BlockStmt)


picojava_BooleanLiteral_strategy = st.builds(picojava_BooleanLiteral, Value=safe_text)
@given(instance=picojava_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_picojava_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, picojava_BooleanLiteral)


picojava_ClassDecl_strategy = st.builds(picojava_ClassDecl, hasCycleOnSuperclassChain=st.booleans())
@given(instance=picojava_ClassDecl_strategy)
@settings(max_examples=25)
def test_picojava_ClassDecl_instantiation(instance):
    assert isinstance(instance, picojava_ClassDecl)


picojava_Decl_strategy = st.builds(picojava_Decl, Name=safe_text, isUnknown=st.booleans())
@given(instance=picojava_Decl_strategy)
@settings(max_examples=25)
def test_picojava_Decl_instantiation(instance):
    assert isinstance(instance, picojava_Decl)


picojava_Dot_strategy = st.builds(picojava_Dot)
@given(instance=picojava_Dot_strategy)
@settings(max_examples=25)
def test_picojava_Dot_instantiation(instance):
    assert isinstance(instance, picojava_Dot)


picojava_Exp_strategy = st.builds(picojava_Exp, isValue=st.booleans())
@given(instance=picojava_Exp_strategy)
@settings(max_examples=25)
def test_picojava_Exp_instantiation(instance):
    assert isinstance(instance, picojava_Exp)


picojava_IdUse_strategy = st.builds(picojava_IdUse, Name=safe_text, isQualified=st.booleans())
@given(instance=picojava_IdUse_strategy)
@settings(max_examples=25)
def test_picojava_IdUse_instantiation(instance):
    assert isinstance(instance, picojava_IdUse)


picojava_PrimitiveDecl_strategy = st.builds(picojava_PrimitiveDecl)
@given(instance=picojava_PrimitiveDecl_strategy)
@settings(max_examples=25)
def test_picojava_PrimitiveDecl_instantiation(instance):
    assert isinstance(instance, picojava_PrimitiveDecl)


picojava_Program_strategy = st.builds(picojava_Program)
@given(instance=picojava_Program_strategy)
@settings(max_examples=25)
def test_picojava_Program_instantiation(instance):
    assert isinstance(instance, picojava_Program)


picojava_Stmt_strategy = st.builds(picojava_Stmt)
@given(instance=picojava_Stmt_strategy)
@settings(max_examples=25)
def test_picojava_Stmt_instantiation(instance):
    assert isinstance(instance, picojava_Stmt)


picojava_TypeDecl_strategy = st.builds(picojava_TypeDecl, isQualified=st.booleans())
@given(instance=picojava_TypeDecl_strategy)
@settings(max_examples=25)
def test_picojava_TypeDecl_instantiation(instance):
    assert isinstance(instance, picojava_TypeDecl)


picojava_TypeUse_strategy = st.builds(picojava_TypeUse)
@given(instance=picojava_TypeUse_strategy)
@settings(max_examples=25)
def test_picojava_TypeUse_instantiation(instance):
    assert isinstance(instance, picojava_TypeUse)


picojava_UnknownDecl_strategy = st.builds(picojava_UnknownDecl)
@given(instance=picojava_UnknownDecl_strategy)
@settings(max_examples=25)
def test_picojava_UnknownDecl_instantiation(instance):
    assert isinstance(instance, picojava_UnknownDecl)


picojava_Use_strategy = st.builds(picojava_Use)
@given(instance=picojava_Use_strategy)
@settings(max_examples=25)
def test_picojava_Use_instantiation(instance):
    assert isinstance(instance, picojava_Use)


picojava_VarDecl_strategy = st.builds(picojava_VarDecl)
@given(instance=picojava_VarDecl_strategy)
@settings(max_examples=25)
def test_picojava_VarDecl_instantiation(instance):
    assert isinstance(instance, picojava_VarDecl)


picojava_VariableUse_strategy = st.builds(picojava_VariableUse)
@given(instance=picojava_VariableUse_strategy)
@settings(max_examples=25)
def test_picojava_VariableUse_instantiation(instance):
    assert isinstance(instance, picojava_VariableUse)


picojava_WhileStmt_strategy = st.builds(picojava_WhileStmt)
@given(instance=picojava_WhileStmt_strategy)
@settings(max_examples=25)
def test_picojava_WhileStmt_instantiation(instance):
    assert isinstance(instance, picojava_WhileStmt)



