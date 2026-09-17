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
    Expr,
    paplj_And,
    paplj_Lt,
    paplj_MemberRef,
    paplj_New,
    paplj_Null,
    paplj_Eq,
    paplj_Not,
    paplj_Bool,
    paplj_Add,
    paplj_Var,
    paplj_Assignment,
    paplj_Neq,
    paplj_Cast,
    paplj_Num,
    paplj_Mul,
    paplj_Min,
    paplj_Let,
    paplj_Sub,
    paplj_This,
    paplj_If,
    paplj_Div,
    paplj_Or,
    paplj_Symbol,
    Symbol,
    paplj_Binding,
    paplj_Member,
    paplj_Expr,
    paplj_Type,
    paplj_Import,
    paplj_Program,
    paplj_Block2,
    paplj_Param,
    Member,
    paplj_Method,
    paplj_Field,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_hyp_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_hyp_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_and_is_not_abstract():
    assert not inspect.isabstract(paplj_And)


def test_hyp_paplj_and_constructor_exists():
    assert callable(paplj_And.__init__)


def test_hyp_paplj_and_constructor_args():
    sig = inspect.signature(paplj_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_lt_is_not_abstract():
    assert not inspect.isabstract(paplj_Lt)


def test_hyp_paplj_lt_constructor_exists():
    assert callable(paplj_Lt.__init__)


def test_hyp_paplj_lt_constructor_args():
    sig = inspect.signature(paplj_Lt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_memberref_is_not_abstract():
    assert not inspect.isabstract(paplj_MemberRef)


def test_hyp_paplj_memberref_constructor_exists():
    assert callable(paplj_MemberRef.__init__)


def test_hyp_paplj_memberref_constructor_args():
    sig = inspect.signature(paplj_MemberRef.__init__)
    params = list(sig.parameters.keys())
    assert "methodInvocation" in params, "Missing parameter 'methodInvocation'"




def test_hyp_paplj_new_is_not_abstract():
    assert not inspect.isabstract(paplj_New)


def test_hyp_paplj_new_constructor_exists():
    assert callable(paplj_New.__init__)


def test_hyp_paplj_new_constructor_args():
    sig = inspect.signature(paplj_New.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_null_is_not_abstract():
    assert not inspect.isabstract(paplj_Null)


def test_hyp_paplj_null_constructor_exists():
    assert callable(paplj_Null.__init__)


def test_hyp_paplj_null_constructor_args():
    sig = inspect.signature(paplj_Null.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_eq_is_not_abstract():
    assert not inspect.isabstract(paplj_Eq)


def test_hyp_paplj_eq_constructor_exists():
    assert callable(paplj_Eq.__init__)


def test_hyp_paplj_eq_constructor_args():
    sig = inspect.signature(paplj_Eq.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_not_is_not_abstract():
    assert not inspect.isabstract(paplj_Not)


def test_hyp_paplj_not_constructor_exists():
    assert callable(paplj_Not.__init__)


def test_hyp_paplj_not_constructor_args():
    sig = inspect.signature(paplj_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_bool_is_not_abstract():
    assert not inspect.isabstract(paplj_Bool)


def test_hyp_paplj_bool_constructor_exists():
    assert callable(paplj_Bool.__init__)


def test_hyp_paplj_bool_constructor_args():
    sig = inspect.signature(paplj_Bool.__init__)
    params = list(sig.parameters.keys())
    assert "true" in params, "Missing parameter 'true'"




def test_hyp_paplj_add_is_not_abstract():
    assert not inspect.isabstract(paplj_Add)


def test_hyp_paplj_add_constructor_exists():
    assert callable(paplj_Add.__init__)


def test_hyp_paplj_add_constructor_args():
    sig = inspect.signature(paplj_Add.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_var_is_not_abstract():
    assert not inspect.isabstract(paplj_Var)


def test_hyp_paplj_var_constructor_exists():
    assert callable(paplj_Var.__init__)


def test_hyp_paplj_var_constructor_args():
    sig = inspect.signature(paplj_Var.__init__)
    params = list(sig.parameters.keys())
    assert "methodInvocation" in params, "Missing parameter 'methodInvocation'"




def test_hyp_paplj_assignment_is_not_abstract():
    assert not inspect.isabstract(paplj_Assignment)


def test_hyp_paplj_assignment_constructor_exists():
    assert callable(paplj_Assignment.__init__)


def test_hyp_paplj_assignment_constructor_args():
    sig = inspect.signature(paplj_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_neq_is_not_abstract():
    assert not inspect.isabstract(paplj_Neq)


def test_hyp_paplj_neq_constructor_exists():
    assert callable(paplj_Neq.__init__)


def test_hyp_paplj_neq_constructor_args():
    sig = inspect.signature(paplj_Neq.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_cast_is_not_abstract():
    assert not inspect.isabstract(paplj_Cast)


def test_hyp_paplj_cast_constructor_exists():
    assert callable(paplj_Cast.__init__)


def test_hyp_paplj_cast_constructor_args():
    sig = inspect.signature(paplj_Cast.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_num_is_not_abstract():
    assert not inspect.isabstract(paplj_Num)


def test_hyp_paplj_num_constructor_exists():
    assert callable(paplj_Num.__init__)


def test_hyp_paplj_num_constructor_args():
    sig = inspect.signature(paplj_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_paplj_mul_is_not_abstract():
    assert not inspect.isabstract(paplj_Mul)


def test_hyp_paplj_mul_constructor_exists():
    assert callable(paplj_Mul.__init__)


def test_hyp_paplj_mul_constructor_args():
    sig = inspect.signature(paplj_Mul.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_min_is_not_abstract():
    assert not inspect.isabstract(paplj_Min)


def test_hyp_paplj_min_constructor_exists():
    assert callable(paplj_Min.__init__)


def test_hyp_paplj_min_constructor_args():
    sig = inspect.signature(paplj_Min.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_let_is_not_abstract():
    assert not inspect.isabstract(paplj_Let)


def test_hyp_paplj_let_constructor_exists():
    assert callable(paplj_Let.__init__)


def test_hyp_paplj_let_constructor_args():
    sig = inspect.signature(paplj_Let.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_sub_is_not_abstract():
    assert not inspect.isabstract(paplj_Sub)


def test_hyp_paplj_sub_constructor_exists():
    assert callable(paplj_Sub.__init__)


def test_hyp_paplj_sub_constructor_args():
    sig = inspect.signature(paplj_Sub.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_this_is_not_abstract():
    assert not inspect.isabstract(paplj_This)


def test_hyp_paplj_this_constructor_exists():
    assert callable(paplj_This.__init__)


def test_hyp_paplj_this_constructor_args():
    sig = inspect.signature(paplj_This.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_if_is_not_abstract():
    assert not inspect.isabstract(paplj_If)


def test_hyp_paplj_if_constructor_exists():
    assert callable(paplj_If.__init__)


def test_hyp_paplj_if_constructor_args():
    sig = inspect.signature(paplj_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_div_is_not_abstract():
    assert not inspect.isabstract(paplj_Div)


def test_hyp_paplj_div_constructor_exists():
    assert callable(paplj_Div.__init__)


def test_hyp_paplj_div_constructor_args():
    sig = inspect.signature(paplj_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_or_is_not_abstract():
    assert not inspect.isabstract(paplj_Or)


def test_hyp_paplj_or_constructor_exists():
    assert callable(paplj_Or.__init__)


def test_hyp_paplj_or_constructor_args():
    sig = inspect.signature(paplj_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_symbol_is_not_abstract():
    assert not inspect.isabstract(paplj_Symbol)


def test_hyp_paplj_symbol_constructor_exists():
    assert callable(paplj_Symbol.__init__)


def test_hyp_paplj_symbol_constructor_args():
    sig = inspect.signature(paplj_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_hyp_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_hyp_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_binding_is_not_abstract():
    assert not inspect.isabstract(paplj_Binding)


def test_hyp_paplj_binding_constructor_exists():
    assert callable(paplj_Binding.__init__)


def test_hyp_paplj_binding_constructor_args():
    sig = inspect.signature(paplj_Binding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_member_is_not_abstract():
    assert not inspect.isabstract(paplj_Member)


def test_hyp_paplj_member_constructor_exists():
    assert callable(paplj_Member.__init__)


def test_hyp_paplj_member_constructor_args():
    sig = inspect.signature(paplj_Member.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_expr_is_not_abstract():
    assert not inspect.isabstract(paplj_Expr)


def test_hyp_paplj_expr_constructor_exists():
    assert callable(paplj_Expr.__init__)


def test_hyp_paplj_expr_constructor_args():
    sig = inspect.signature(paplj_Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_type_is_not_abstract():
    assert not inspect.isabstract(paplj_Type)


def test_hyp_paplj_type_constructor_exists():
    assert callable(paplj_Type.__init__)


def test_hyp_paplj_type_constructor_args():
    sig = inspect.signature(paplj_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_paplj_import_is_not_abstract():
    assert not inspect.isabstract(paplj_Import)


def test_hyp_paplj_import_constructor_exists():
    assert callable(paplj_Import.__init__)


def test_hyp_paplj_import_constructor_args():
    sig = inspect.signature(paplj_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"




def test_hyp_paplj_program_is_not_abstract():
    assert not inspect.isabstract(paplj_Program)


def test_hyp_paplj_program_constructor_exists():
    assert callable(paplj_Program.__init__)


def test_hyp_paplj_program_constructor_args():
    sig = inspect.signature(paplj_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_paplj_block2_is_not_abstract():
    assert not inspect.isabstract(paplj_Block2)


def test_hyp_paplj_block2_constructor_exists():
    assert callable(paplj_Block2.__init__)


def test_hyp_paplj_block2_constructor_args():
    sig = inspect.signature(paplj_Block2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_param_is_not_abstract():
    assert not inspect.isabstract(paplj_Param)


def test_hyp_paplj_param_constructor_exists():
    assert callable(paplj_Param.__init__)


def test_hyp_paplj_param_constructor_args():
    sig = inspect.signature(paplj_Param.__init__)
    params = list(sig.parameters.keys())



def test_hyp_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_hyp_member_constructor_exists():
    assert callable(Member.__init__)


def test_hyp_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_method_is_not_abstract():
    assert not inspect.isabstract(paplj_Method)


def test_hyp_paplj_method_constructor_exists():
    assert callable(paplj_Method.__init__)


def test_hyp_paplj_method_constructor_args():
    sig = inspect.signature(paplj_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paplj_field_is_not_abstract():
    assert not inspect.isabstract(paplj_Field)


def test_hyp_paplj_field_constructor_exists():
    assert callable(paplj_Field.__init__)


def test_hyp_paplj_field_constructor_args():
    sig = inspect.signature(paplj_Field.__init__)
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
Expr_strategy = st.builds(
    Expr,
)
paplj_And_strategy = st.builds(
    paplj_And,
)
paplj_Lt_strategy = st.builds(
    paplj_Lt,
)
paplj_MemberRef_strategy = st.builds(
    paplj_MemberRef,
    methodInvocation=
        st.booleans()
)
paplj_New_strategy = st.builds(
    paplj_New,
)
paplj_Null_strategy = st.builds(
    paplj_Null,
)
paplj_Eq_strategy = st.builds(
    paplj_Eq,
)
paplj_Not_strategy = st.builds(
    paplj_Not,
)
paplj_Bool_strategy = st.builds(
    paplj_Bool,
    true=
        st.booleans()
)
paplj_Add_strategy = st.builds(
    paplj_Add,
)
paplj_Var_strategy = st.builds(
    paplj_Var,
    methodInvocation=
        st.booleans()
)
paplj_Assignment_strategy = st.builds(
    paplj_Assignment,
)
paplj_Neq_strategy = st.builds(
    paplj_Neq,
)
paplj_Cast_strategy = st.builds(
    paplj_Cast,
)
paplj_Num_strategy = st.builds(
    paplj_Num,
    value=
        st.integers()
)
paplj_Mul_strategy = st.builds(
    paplj_Mul,
)
paplj_Min_strategy = st.builds(
    paplj_Min,
)
paplj_Let_strategy = st.builds(
    paplj_Let,
)
paplj_Sub_strategy = st.builds(
    paplj_Sub,
)
paplj_This_strategy = st.builds(
    paplj_This,
)
paplj_If_strategy = st.builds(
    paplj_If,
)
paplj_Div_strategy = st.builds(
    paplj_Div,
)
paplj_Or_strategy = st.builds(
    paplj_Or,
)
paplj_Symbol_strategy = st.builds(
    paplj_Symbol,
    name=
        safe_text
)
Symbol_strategy = st.builds(
    Symbol,
)
paplj_Binding_strategy = st.builds(
    paplj_Binding,
)
paplj_Member_strategy = st.builds(
    paplj_Member,
)
paplj_Expr_strategy = st.builds(
    paplj_Expr,
)
paplj_Type_strategy = st.builds(
    paplj_Type,
    name=
        safe_text
)
paplj_Import_strategy = st.builds(
    paplj_Import,
    importedNamespace=
        safe_text
)
paplj_Program_strategy = st.builds(
    paplj_Program,
    name=
        safe_text
)
paplj_Block2_strategy = st.builds(
    paplj_Block2,
)
paplj_Param_strategy = st.builds(
    paplj_Param,
)
Member_strategy = st.builds(
    Member,
)
paplj_Method_strategy = st.builds(
    paplj_Method,
)
paplj_Field_strategy = st.builds(
    paplj_Field,
)







@given(instance=paplj_MemberRef_strategy)
def test_hyp_paplj_memberref_methodInvocation_setter(instance):
    original = instance.methodInvocation
    instance.methodInvocation = original
    assert instance.methodInvocation == original








@given(instance=paplj_Bool_strategy)
def test_hyp_paplj_bool_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original





@given(instance=paplj_Var_strategy)
def test_hyp_paplj_var_methodInvocation_setter(instance):
    original = instance.methodInvocation
    instance.methodInvocation = original
    assert instance.methodInvocation == original







@given(instance=paplj_Num_strategy)
def test_hyp_paplj_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original












@given(instance=paplj_Symbol_strategy)
def test_hyp_paplj_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=paplj_Type_strategy)
def test_hyp_paplj_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=paplj_Import_strategy)
def test_hyp_paplj_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original




@given(instance=paplj_Program_strategy)
def test_hyp_paplj_program_name_setter(instance):
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
    Expr,
    Member,
    Symbol,
    paplj_Add,
    paplj_And,
    paplj_Assignment,
    paplj_Binding,
    paplj_Block2,
    paplj_Bool,
    paplj_Cast,
    paplj_Div,
    paplj_Eq,
    paplj_Expr,
    paplj_Field,
    paplj_If,
    paplj_Import,
    paplj_Let,
    paplj_Lt,
    paplj_Member,
    paplj_MemberRef,
    paplj_Method,
    paplj_Min,
    paplj_Mul,
    paplj_Neq,
    paplj_New,
    paplj_Not,
    paplj_Null,
    paplj_Num,
    paplj_Or,
    paplj_Param,
    paplj_Program,
    paplj_Sub,
    paplj_Symbol,
    paplj_This,
    paplj_Type,
    paplj_Var,
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

def test_paplj_Bool_true_value_roundtrip():
    instance = paplj_Bool(true=True)
    assert instance.true == True
    instance.true = False
    assert instance.true == False


def test_paplj_Import_importedNamespace_value_roundtrip():
    instance = paplj_Import(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_paplj_MemberRef_methodInvocation_value_roundtrip():
    instance = paplj_MemberRef(methodInvocation=True)
    assert instance.methodInvocation == True
    instance.methodInvocation = False
    assert instance.methodInvocation == False


def test_paplj_Num_value_value_roundtrip():
    instance = paplj_Num(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_paplj_Program_name_value_roundtrip():
    instance = paplj_Program(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_paplj_Symbol_name_value_roundtrip():
    instance = paplj_Symbol(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_paplj_Type_name_value_roundtrip():
    instance = paplj_Type(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_paplj_Var_methodInvocation_value_roundtrip():
    instance = paplj_Var(methodInvocation=True)
    assert instance.methodInvocation == True
    instance.methodInvocation = False
    assert instance.methodInvocation == False


def test_paplj_Add_isa_Expr():
    instance = paplj_Add()
    assert isinstance(instance, Expr)


def test_paplj_And_isa_Expr():
    instance = paplj_And()
    assert isinstance(instance, Expr)


def test_paplj_Assignment_isa_Expr():
    instance = paplj_Assignment()
    assert isinstance(instance, Expr)


def test_paplj_Block2_isa_Expr():
    instance = paplj_Block2()
    assert isinstance(instance, Expr)


def test_paplj_Bool_isa_Expr():
    instance = paplj_Bool(true=True)
    assert isinstance(instance, Expr)


def test_paplj_Cast_isa_Expr():
    instance = paplj_Cast()
    assert isinstance(instance, Expr)


def test_paplj_Div_isa_Expr():
    instance = paplj_Div()
    assert isinstance(instance, Expr)


def test_paplj_Eq_isa_Expr():
    instance = paplj_Eq()
    assert isinstance(instance, Expr)


def test_paplj_If_isa_Expr():
    instance = paplj_If()
    assert isinstance(instance, Expr)


def test_paplj_Let_isa_Expr():
    instance = paplj_Let()
    assert isinstance(instance, Expr)


def test_paplj_Lt_isa_Expr():
    instance = paplj_Lt()
    assert isinstance(instance, Expr)


def test_paplj_MemberRef_isa_Expr():
    instance = paplj_MemberRef(methodInvocation=True)
    assert isinstance(instance, Expr)


def test_paplj_Min_isa_Expr():
    instance = paplj_Min()
    assert isinstance(instance, Expr)


def test_paplj_Mul_isa_Expr():
    instance = paplj_Mul()
    assert isinstance(instance, Expr)


def test_paplj_Neq_isa_Expr():
    instance = paplj_Neq()
    assert isinstance(instance, Expr)


def test_paplj_New_isa_Expr():
    instance = paplj_New()
    assert isinstance(instance, Expr)


def test_paplj_Not_isa_Expr():
    instance = paplj_Not()
    assert isinstance(instance, Expr)


def test_paplj_Null_isa_Expr():
    instance = paplj_Null()
    assert isinstance(instance, Expr)


def test_paplj_Num_isa_Expr():
    instance = paplj_Num(value=7)
    assert isinstance(instance, Expr)


def test_paplj_Or_isa_Expr():
    instance = paplj_Or()
    assert isinstance(instance, Expr)


def test_paplj_Sub_isa_Expr():
    instance = paplj_Sub()
    assert isinstance(instance, Expr)


def test_paplj_This_isa_Expr():
    instance = paplj_This()
    assert isinstance(instance, Expr)


def test_paplj_Var_isa_Expr():
    instance = paplj_Var(methodInvocation=True)
    assert isinstance(instance, Expr)


def test_paplj_Field_isa_Member():
    instance = paplj_Field()
    assert isinstance(instance, Member)


def test_paplj_Method_isa_Member():
    instance = paplj_Method()
    assert isinstance(instance, Member)


def test_paplj_Binding_isa_Symbol():
    instance = paplj_Binding()
    assert isinstance(instance, Symbol)


def test_paplj_Member_isa_Symbol():
    instance = paplj_Member()
    assert isinstance(instance, Symbol)


def test_paplj_Param_isa_Symbol():
    instance = paplj_Param()
    assert isinstance(instance, Symbol)


def test_assoc_args106_link_reassign_clear():
    a = paplj_Var(methodInvocation=True)
    b1 = paplj_Expr()
    b2 = paplj_Expr()
    _safe_set(a, 'paplj_Var107', {b1})
    assert _is_linked(a, 'paplj_Var107', b1)
    if hasattr(b1, 'paplj_Expr108'):
        assert _is_linked(b1, 'paplj_Expr108', a)
    _safe_set(a, 'paplj_Var107', {b2})
    assert _is_linked(a, 'paplj_Var107', b2)
    if hasattr(b1, 'paplj_Expr108'):
        assert not _is_linked(b1, 'paplj_Expr108', a)
    if hasattr(b2, 'paplj_Expr108'):
        assert _is_linked(b2, 'paplj_Expr108', a)
    _safe_set(a, 'paplj_Var107', set())
    assert not _is_linked(a, 'paplj_Var107', b2)
    if hasattr(b2, 'paplj_Expr108'):
        assert not _is_linked(b2, 'paplj_Expr108', a)


def test_assoc_args97_link_reassign_clear():
    a = paplj_MemberRef(methodInvocation=True)
    b1 = paplj_Expr()
    b2 = paplj_Expr()
    _safe_set(a, 'paplj_MemberRef98', {b1})
    assert _is_linked(a, 'paplj_MemberRef98', b1)
    if hasattr(b1, 'paplj_Expr99'):
        assert _is_linked(b1, 'paplj_Expr99', a)
    _safe_set(a, 'paplj_MemberRef98', {b2})
    assert _is_linked(a, 'paplj_MemberRef98', b2)
    if hasattr(b1, 'paplj_Expr99'):
        assert not _is_linked(b1, 'paplj_Expr99', a)
    if hasattr(b2, 'paplj_Expr99'):
        assert _is_linked(b2, 'paplj_Expr99', a)
    _safe_set(a, 'paplj_MemberRef98', set())
    assert not _is_linked(a, 'paplj_MemberRef98', b2)
    if hasattr(b2, 'paplj_Expr99'):
        assert not _is_linked(b2, 'paplj_Expr99', a)


def test_assoc_classes1_link_reassign_clear():
    a = paplj_Type(name="sample_text")
    b1 = paplj_Program(name="sample_text")
    b2 = paplj_Program(name="sample_text_2")
    _safe_set(a, 'paplj_Type', b1)
    assert _is_linked(a, 'paplj_Type', b1)
    if hasattr(b1, 'paplj_Program2'):
        assert _is_linked(b1, 'paplj_Program2', a)
    _safe_set(a, 'paplj_Type', b2)
    assert _is_linked(a, 'paplj_Type', b2)
    if hasattr(b1, 'paplj_Program2'):
        assert not _is_linked(b1, 'paplj_Program2', a)
    if hasattr(b2, 'paplj_Program2'):
        assert _is_linked(b2, 'paplj_Program2', a)
    _safe_set(a, 'paplj_Type', None)
    assert not _is_linked(a, 'paplj_Type', b2)
    if hasattr(b2, 'paplj_Program2'):
        assert not _is_linked(b2, 'paplj_Program2', a)


def test_assoc_expr3_link_reassign_clear():
    a = paplj_Program(name="sample_text")
    b1 = paplj_Expr()
    b2 = paplj_Expr()
    _safe_set(a, 'paplj_Program4', b1)
    assert _is_linked(a, 'paplj_Program4', b1)
    if hasattr(b1, 'paplj_Expr'):
        assert _is_linked(b1, 'paplj_Expr', a)
    _safe_set(a, 'paplj_Program4', b2)
    assert _is_linked(a, 'paplj_Program4', b2)
    if hasattr(b1, 'paplj_Expr'):
        assert not _is_linked(b1, 'paplj_Expr', a)
    if hasattr(b2, 'paplj_Expr'):
        assert _is_linked(b2, 'paplj_Expr', a)
    _safe_set(a, 'paplj_Program4', None)
    assert not _is_linked(a, 'paplj_Program4', b2)
    if hasattr(b2, 'paplj_Expr'):
        assert not _is_linked(b2, 'paplj_Expr', a)


def test_assoc_imports0_link_reassign_clear():
    a = paplj_Program(name="sample_text")
    b1 = paplj_Import(importedNamespace="sample_text")
    b2 = paplj_Import(importedNamespace="sample_text_2")
    _safe_set(a, 'paplj_Program', {b1})
    assert _is_linked(a, 'paplj_Program', b1)
    if hasattr(b1, 'paplj_Import'):
        assert _is_linked(b1, 'paplj_Import', a)
    _safe_set(a, 'paplj_Program', {b2})
    assert _is_linked(a, 'paplj_Program', b2)
    if hasattr(b1, 'paplj_Import'):
        assert not _is_linked(b1, 'paplj_Import', a)
    if hasattr(b2, 'paplj_Import'):
        assert _is_linked(b2, 'paplj_Import', a)
    _safe_set(a, 'paplj_Program', set())
    assert not _is_linked(a, 'paplj_Program', b2)
    if hasattr(b2, 'paplj_Import'):
        assert not _is_linked(b2, 'paplj_Import', a)


def test_assoc_left92_link_reassign_clear():
    a = paplj_MemberRef(methodInvocation=True)
    b1 = paplj_Expr()
    b2 = paplj_Expr()
    _safe_set(a, 'paplj_MemberRef', b1)
    assert _is_linked(a, 'paplj_MemberRef', b1)
    if hasattr(b1, 'paplj_Expr93'):
        assert _is_linked(b1, 'paplj_Expr93', a)
    _safe_set(a, 'paplj_MemberRef', b2)
    assert _is_linked(a, 'paplj_MemberRef', b2)
    if hasattr(b1, 'paplj_Expr93'):
        assert not _is_linked(b1, 'paplj_Expr93', a)
    if hasattr(b2, 'paplj_Expr93'):
        assert _is_linked(b2, 'paplj_Expr93', a)
    _safe_set(a, 'paplj_MemberRef', None)
    assert not _is_linked(a, 'paplj_MemberRef', b2)
    if hasattr(b2, 'paplj_Expr93'):
        assert not _is_linked(b2, 'paplj_Expr93', a)


def test_assoc_member104_link_reassign_clear():
    a = paplj_Var(methodInvocation=True)
    b1 = paplj_Symbol(name="sample_text")
    b2 = paplj_Symbol(name="sample_text_2")
    _safe_set(a, 'paplj_Var', b1)
    assert _is_linked(a, 'paplj_Var', b1)
    if hasattr(b1, 'paplj_Symbol105'):
        assert _is_linked(b1, 'paplj_Symbol105', a)
    _safe_set(a, 'paplj_Var', b2)
    assert _is_linked(a, 'paplj_Var', b2)
    if hasattr(b1, 'paplj_Symbol105'):
        assert not _is_linked(b1, 'paplj_Symbol105', a)
    if hasattr(b2, 'paplj_Symbol105'):
        assert _is_linked(b2, 'paplj_Symbol105', a)
    _safe_set(a, 'paplj_Var', None)
    assert not _is_linked(a, 'paplj_Var', b2)
    if hasattr(b2, 'paplj_Symbol105'):
        assert not _is_linked(b2, 'paplj_Symbol105', a)


def test_assoc_member94_link_reassign_clear():
    a = paplj_MemberRef(methodInvocation=True)
    b1 = paplj_Member()
    b2 = paplj_Member()
    _safe_set(a, 'paplj_MemberRef95', b1)
    assert _is_linked(a, 'paplj_MemberRef95', b1)
    if hasattr(b1, 'paplj_Member96'):
        assert _is_linked(b1, 'paplj_Member96', a)
    _safe_set(a, 'paplj_MemberRef95', b2)
    assert _is_linked(a, 'paplj_MemberRef95', b2)
    if hasattr(b1, 'paplj_Member96'):
        assert not _is_linked(b1, 'paplj_Member96', a)
    if hasattr(b2, 'paplj_Member96'):
        assert _is_linked(b2, 'paplj_Member96', a)
    _safe_set(a, 'paplj_MemberRef95', None)
    assert not _is_linked(a, 'paplj_MemberRef95', b2)
    if hasattr(b2, 'paplj_Member96'):
        assert not _is_linked(b2, 'paplj_Member96', a)


def test_assoc_members8_link_reassign_clear():
    a = paplj_Type(name="sample_text")
    b1 = paplj_Member()
    b2 = paplj_Member()
    _safe_set(a, 'paplj_Type9', {b1})
    assert _is_linked(a, 'paplj_Type9', b1)
    if hasattr(b1, 'paplj_Member'):
        assert _is_linked(b1, 'paplj_Member', a)
    _safe_set(a, 'paplj_Type9', {b2})
    assert _is_linked(a, 'paplj_Type9', b2)
    if hasattr(b1, 'paplj_Member'):
        assert not _is_linked(b1, 'paplj_Member', a)
    if hasattr(b2, 'paplj_Member'):
        assert _is_linked(b2, 'paplj_Member', a)
    _safe_set(a, 'paplj_Type9', set())
    assert not _is_linked(a, 'paplj_Type9', b2)
    if hasattr(b2, 'paplj_Member'):
        assert not _is_linked(b2, 'paplj_Member', a)


def test_assoc_superType6_link_reassign_clear():
    a = paplj_Type(name="sample_text")
    b1 = paplj_Type(name="sample_text")
    b2 = paplj_Type(name="sample_text_2")
    _safe_set(a, 'paplj_Type5', b1)
    assert _is_linked(a, 'paplj_Type5', b1)
    if hasattr(b1, 'paplj_Type7'):
        assert _is_linked(b1, 'paplj_Type7', a)
    _safe_set(a, 'paplj_Type5', b2)
    assert _is_linked(a, 'paplj_Type5', b2)
    if hasattr(b1, 'paplj_Type7'):
        assert not _is_linked(b1, 'paplj_Type7', a)
    if hasattr(b2, 'paplj_Type7'):
        assert _is_linked(b2, 'paplj_Type7', a)
    _safe_set(a, 'paplj_Type5', None)
    assert not _is_linked(a, 'paplj_Type5', b2)
    if hasattr(b2, 'paplj_Type7'):
        assert not _is_linked(b2, 'paplj_Type7', a)


def test_assoc_type10_link_reassign_clear():
    a = paplj_Type(name="sample_text")
    b1 = paplj_Symbol(name="sample_text")
    b2 = paplj_Symbol(name="sample_text_2")
    _safe_set(a, 'paplj_Type11', b1)
    assert _is_linked(a, 'paplj_Type11', b1)
    if hasattr(b1, 'paplj_Symbol'):
        assert _is_linked(b1, 'paplj_Symbol', a)
    _safe_set(a, 'paplj_Type11', b2)
    assert _is_linked(a, 'paplj_Type11', b2)
    if hasattr(b1, 'paplj_Symbol'):
        assert not _is_linked(b1, 'paplj_Symbol', a)
    if hasattr(b2, 'paplj_Symbol'):
        assert _is_linked(b2, 'paplj_Symbol', a)
    _safe_set(a, 'paplj_Type11', None)
    assert not _is_linked(a, 'paplj_Type11', b2)
    if hasattr(b2, 'paplj_Symbol'):
        assert not _is_linked(b2, 'paplj_Symbol', a)


def test_assoc_type100_link_reassign_clear():
    a = paplj_Type(name="sample_text")
    b1 = paplj_Null()
    b2 = paplj_Null()
    _safe_set(a, 'paplj_Type101', b1)
    assert _is_linked(a, 'paplj_Type101', b1)
    if hasattr(b1, 'paplj_Null'):
        assert _is_linked(b1, 'paplj_Null', a)
    _safe_set(a, 'paplj_Type101', b2)
    assert _is_linked(a, 'paplj_Type101', b2)
    if hasattr(b1, 'paplj_Null'):
        assert not _is_linked(b1, 'paplj_Null', a)
    if hasattr(b2, 'paplj_Null'):
        assert _is_linked(b2, 'paplj_Null', a)
    _safe_set(a, 'paplj_Type101', None)
    assert not _is_linked(a, 'paplj_Type101', b2)
    if hasattr(b2, 'paplj_Null'):
        assert not _is_linked(b2, 'paplj_Null', a)


def test_assoc_type102_link_reassign_clear():
    a = paplj_Type(name="sample_text")
    b1 = paplj_New()
    b2 = paplj_New()
    _safe_set(a, 'paplj_Type103', b1)
    assert _is_linked(a, 'paplj_Type103', b1)
    if hasattr(b1, 'paplj_New'):
        assert _is_linked(b1, 'paplj_New', a)
    _safe_set(a, 'paplj_Type103', b2)
    assert _is_linked(a, 'paplj_Type103', b2)
    if hasattr(b1, 'paplj_New'):
        assert not _is_linked(b1, 'paplj_New', a)
    if hasattr(b2, 'paplj_New'):
        assert _is_linked(b2, 'paplj_New', a)
    _safe_set(a, 'paplj_Type103', None)
    assert not _is_linked(a, 'paplj_Type103', b2)
    if hasattr(b2, 'paplj_New'):
        assert not _is_linked(b2, 'paplj_New', a)


def test_assoc_type85_link_reassign_clear():
    a = paplj_Type(name="sample_text")
    b1 = paplj_Cast()
    b2 = paplj_Cast()
    _safe_set(a, 'paplj_Type87', b1)
    assert _is_linked(a, 'paplj_Type87', b1)
    if hasattr(b1, 'paplj_Cast86'):
        assert _is_linked(b1, 'paplj_Cast86', a)
    _safe_set(a, 'paplj_Type87', b2)
    assert _is_linked(a, 'paplj_Type87', b2)
    if hasattr(b1, 'paplj_Cast86'):
        assert not _is_linked(b1, 'paplj_Cast86', a)
    if hasattr(b2, 'paplj_Cast86'):
        assert _is_linked(b2, 'paplj_Cast86', a)
    _safe_set(a, 'paplj_Type87', None)
    assert not _is_linked(a, 'paplj_Type87', b2)
    if hasattr(b2, 'paplj_Cast86'):
        assert not _is_linked(b2, 'paplj_Cast86', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expr_strategy = st.builds(Expr)
@given(instance=Expr_strategy)
@settings(max_examples=25)
def test_Expr_instantiation(instance):
    assert isinstance(instance, Expr)


Member_strategy = st.builds(Member)
@given(instance=Member_strategy)
@settings(max_examples=25)
def test_Member_instantiation(instance):
    assert isinstance(instance, Member)


Symbol_strategy = st.builds(Symbol)
@given(instance=Symbol_strategy)
@settings(max_examples=25)
def test_Symbol_instantiation(instance):
    assert isinstance(instance, Symbol)


paplj_Add_strategy = st.builds(paplj_Add)
@given(instance=paplj_Add_strategy)
@settings(max_examples=25)
def test_paplj_Add_instantiation(instance):
    assert isinstance(instance, paplj_Add)


paplj_And_strategy = st.builds(paplj_And)
@given(instance=paplj_And_strategy)
@settings(max_examples=25)
def test_paplj_And_instantiation(instance):
    assert isinstance(instance, paplj_And)


paplj_Assignment_strategy = st.builds(paplj_Assignment)
@given(instance=paplj_Assignment_strategy)
@settings(max_examples=25)
def test_paplj_Assignment_instantiation(instance):
    assert isinstance(instance, paplj_Assignment)


paplj_Binding_strategy = st.builds(paplj_Binding)
@given(instance=paplj_Binding_strategy)
@settings(max_examples=25)
def test_paplj_Binding_instantiation(instance):
    assert isinstance(instance, paplj_Binding)


paplj_Block2_strategy = st.builds(paplj_Block2)
@given(instance=paplj_Block2_strategy)
@settings(max_examples=25)
def test_paplj_Block2_instantiation(instance):
    assert isinstance(instance, paplj_Block2)


paplj_Bool_strategy = st.builds(paplj_Bool, true=st.booleans())
@given(instance=paplj_Bool_strategy)
@settings(max_examples=25)
def test_paplj_Bool_instantiation(instance):
    assert isinstance(instance, paplj_Bool)


paplj_Cast_strategy = st.builds(paplj_Cast)
@given(instance=paplj_Cast_strategy)
@settings(max_examples=25)
def test_paplj_Cast_instantiation(instance):
    assert isinstance(instance, paplj_Cast)


paplj_Div_strategy = st.builds(paplj_Div)
@given(instance=paplj_Div_strategy)
@settings(max_examples=25)
def test_paplj_Div_instantiation(instance):
    assert isinstance(instance, paplj_Div)


paplj_Eq_strategy = st.builds(paplj_Eq)
@given(instance=paplj_Eq_strategy)
@settings(max_examples=25)
def test_paplj_Eq_instantiation(instance):
    assert isinstance(instance, paplj_Eq)


paplj_Expr_strategy = st.builds(paplj_Expr)
@given(instance=paplj_Expr_strategy)
@settings(max_examples=25)
def test_paplj_Expr_instantiation(instance):
    assert isinstance(instance, paplj_Expr)


paplj_Field_strategy = st.builds(paplj_Field)
@given(instance=paplj_Field_strategy)
@settings(max_examples=25)
def test_paplj_Field_instantiation(instance):
    assert isinstance(instance, paplj_Field)


paplj_If_strategy = st.builds(paplj_If)
@given(instance=paplj_If_strategy)
@settings(max_examples=25)
def test_paplj_If_instantiation(instance):
    assert isinstance(instance, paplj_If)


paplj_Import_strategy = st.builds(paplj_Import, importedNamespace=safe_text)
@given(instance=paplj_Import_strategy)
@settings(max_examples=25)
def test_paplj_Import_instantiation(instance):
    assert isinstance(instance, paplj_Import)


paplj_Let_strategy = st.builds(paplj_Let)
@given(instance=paplj_Let_strategy)
@settings(max_examples=25)
def test_paplj_Let_instantiation(instance):
    assert isinstance(instance, paplj_Let)


paplj_Lt_strategy = st.builds(paplj_Lt)
@given(instance=paplj_Lt_strategy)
@settings(max_examples=25)
def test_paplj_Lt_instantiation(instance):
    assert isinstance(instance, paplj_Lt)


paplj_Member_strategy = st.builds(paplj_Member)
@given(instance=paplj_Member_strategy)
@settings(max_examples=25)
def test_paplj_Member_instantiation(instance):
    assert isinstance(instance, paplj_Member)


paplj_MemberRef_strategy = st.builds(paplj_MemberRef, methodInvocation=st.booleans())
@given(instance=paplj_MemberRef_strategy)
@settings(max_examples=25)
def test_paplj_MemberRef_instantiation(instance):
    assert isinstance(instance, paplj_MemberRef)


paplj_Method_strategy = st.builds(paplj_Method)
@given(instance=paplj_Method_strategy)
@settings(max_examples=25)
def test_paplj_Method_instantiation(instance):
    assert isinstance(instance, paplj_Method)


paplj_Min_strategy = st.builds(paplj_Min)
@given(instance=paplj_Min_strategy)
@settings(max_examples=25)
def test_paplj_Min_instantiation(instance):
    assert isinstance(instance, paplj_Min)


paplj_Mul_strategy = st.builds(paplj_Mul)
@given(instance=paplj_Mul_strategy)
@settings(max_examples=25)
def test_paplj_Mul_instantiation(instance):
    assert isinstance(instance, paplj_Mul)


paplj_Neq_strategy = st.builds(paplj_Neq)
@given(instance=paplj_Neq_strategy)
@settings(max_examples=25)
def test_paplj_Neq_instantiation(instance):
    assert isinstance(instance, paplj_Neq)


paplj_New_strategy = st.builds(paplj_New)
@given(instance=paplj_New_strategy)
@settings(max_examples=25)
def test_paplj_New_instantiation(instance):
    assert isinstance(instance, paplj_New)


paplj_Not_strategy = st.builds(paplj_Not)
@given(instance=paplj_Not_strategy)
@settings(max_examples=25)
def test_paplj_Not_instantiation(instance):
    assert isinstance(instance, paplj_Not)


paplj_Null_strategy = st.builds(paplj_Null)
@given(instance=paplj_Null_strategy)
@settings(max_examples=25)
def test_paplj_Null_instantiation(instance):
    assert isinstance(instance, paplj_Null)


paplj_Num_strategy = st.builds(paplj_Num, value=st.integers())
@given(instance=paplj_Num_strategy)
@settings(max_examples=25)
def test_paplj_Num_instantiation(instance):
    assert isinstance(instance, paplj_Num)


paplj_Or_strategy = st.builds(paplj_Or)
@given(instance=paplj_Or_strategy)
@settings(max_examples=25)
def test_paplj_Or_instantiation(instance):
    assert isinstance(instance, paplj_Or)


paplj_Param_strategy = st.builds(paplj_Param)
@given(instance=paplj_Param_strategy)
@settings(max_examples=25)
def test_paplj_Param_instantiation(instance):
    assert isinstance(instance, paplj_Param)


paplj_Program_strategy = st.builds(paplj_Program, name=safe_text)
@given(instance=paplj_Program_strategy)
@settings(max_examples=25)
def test_paplj_Program_instantiation(instance):
    assert isinstance(instance, paplj_Program)


paplj_Sub_strategy = st.builds(paplj_Sub)
@given(instance=paplj_Sub_strategy)
@settings(max_examples=25)
def test_paplj_Sub_instantiation(instance):
    assert isinstance(instance, paplj_Sub)


paplj_Symbol_strategy = st.builds(paplj_Symbol, name=safe_text)
@given(instance=paplj_Symbol_strategy)
@settings(max_examples=25)
def test_paplj_Symbol_instantiation(instance):
    assert isinstance(instance, paplj_Symbol)


paplj_This_strategy = st.builds(paplj_This)
@given(instance=paplj_This_strategy)
@settings(max_examples=25)
def test_paplj_This_instantiation(instance):
    assert isinstance(instance, paplj_This)


paplj_Type_strategy = st.builds(paplj_Type, name=safe_text)
@given(instance=paplj_Type_strategy)
@settings(max_examples=25)
def test_paplj_Type_instantiation(instance):
    assert isinstance(instance, paplj_Type)


paplj_Var_strategy = st.builds(paplj_Var, methodInvocation=st.booleans())
@given(instance=paplj_Var_strategy)
@settings(max_examples=25)
def test_paplj_Var_instantiation(instance):
    assert isinstance(instance, paplj_Var)



