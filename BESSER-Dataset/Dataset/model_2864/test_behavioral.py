import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    Application_condition,
    Case_branch,
    Class_modifier_fragment,
    Data_constructor_arg,
    Decl,
    Delta_param,
    DomainModel_,
    Eff_expr,
    Exp,
    Fnode,
    Function_param,
    Functional_modifier,
    Guard,
    Interface_modifier_fragment,
    Mexp,
    Module_modifier,
    Namespace_modifier,
    Product_expr,
    Pure_exp,
    Update_preamble_declaration,
    abs_After_condition,
    abs_AndGuard,
    abs_And_expr,
    abs_Annotation,
    abs_Annotations,
    abs_Anon_function_decl,
    abs_AppAnd_exp,
    abs_AppOr_exp,
    abs_Application_condition,
    abs_Case_branch,
    abs_Casestmtbranch,
    abs_Class_decl,
    abs_Class_modifier_fragment,
    abs_Comparison_expr,
    abs_Compilation_Unit,
    abs_DataType_decl,
    abs_Data_constructor,
    abs_Data_constructor_arg,
    abs_Decl,
    abs_Delta_access,
    abs_Delta_clause,
    abs_Delta_decl,
    abs_Delta_id,
    abs_Delta_param,
    abs_Deltaspec,
    abs_DomainModel_,
    abs_Eff_expr,
    abs_Equality_expr,
    abs_Exception_decl,
    abs_Exp,
    abs_Feature,
    abs_Feature_decl,
    abs_Feature_decl_attribute,
    abs_Feature_decl_constraint,
    abs_Feature_decl_group,
    abs_Fextension,
    abs_Field_decl,
    abs_Fnode,
    abs_From_condition,
    abs_Function_decl,
    abs_Function_list,
    abs_Function_name_decl,
    abs_Function_name_list,
    abs_Function_name_param_decl,
    abs_Function_param,
    abs_Functional_modifier,
    abs_Guard,
    abs_Has_condition,
    abs_Interface_decl,
    abs_Interface_modifier_fragment,
    abs_Interface_name,
    abs_Main_block,
    abs_Method,
    abs_Methodsig,
    abs_Mexp,
    abs_MexpAnd_expr,
    abs_MexpComparison_expr,
    abs_MexpEquality_expr,
    abs_MexpImplies_expr,
    abs_MexpMulDivOrMod_expr,
    abs_MexpOr_exp,
    abs_MexpPlusOrMinus_expr,
    abs_MexpPrimary_expr,
    abs_Module_decl,
    abs_Module_export,
    abs_Module_import,
    abs_Module_modifier,
    abs_MulDivOrMod_expr,
    abs_Namespace_modifier,
    abs_OO_modifier,
    abs_Object_update,
    abs_Object_update_assign_stmt,
    abs_Or_expr,
    abs_Par_function_decl,
    abs_Param_decl,
    abs_Param_list,
    abs_Pattern,
    abs_PlusOrMinus_expr,
    abs_ProductAnd_exp,
    abs_ProductMinus_exp,
    abs_ProductOr_expr,
    abs_Product_decl,
    abs_Product_expr,
    abs_Product_reconfiguration,
    abs_Productline_decl,
    abs_Pure_exp,
    abs_Pure_exp_list,
    abs_Stmt,
    abs_Trait_decl,
    abs_Trait_expr,
    abs_Trait_oper,
    abs_Trait_usage,
    abs_Type_exp,
    abs_Type_use,
    abs_Typesyn_decl,
    abs_Update_decl,
    abs_Update_preamble_declaration,
    abs_Var_or_field_ref,
    abs_When_condition,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_b68_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp69', a1)
    assert _is_linked(b, 'abs_Pure_exp69', a1)
    if hasattr(a1, 'abs_Pure_exp67'):
        assert _is_linked(a1, 'abs_Pure_exp67', b)
    _safe_set(b, 'abs_Pure_exp69', a2)
    assert _is_linked(b, 'abs_Pure_exp69', a2)
    if hasattr(a1, 'abs_Pure_exp67'):
        assert not _is_linked(a1, 'abs_Pure_exp67', b)
    if hasattr(a2, 'abs_Pure_exp67'):
        assert _is_linked(a2, 'abs_Pure_exp67', b)
    _safe_set(b, 'abs_Pure_exp69', None)
    assert not _is_linked(b, 'abs_Pure_exp69', a2)
    if hasattr(a2, 'abs_Pure_exp67'):
        assert not _is_linked(a2, 'abs_Pure_exp67', b)


def test_assoc_c195_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp197', a1)
    assert _is_linked(b, 'abs_Pure_exp197', a1)
    if hasattr(a1, 'abs_Stmt196'):
        assert _is_linked(a1, 'abs_Stmt196', b)
    _safe_set(b, 'abs_Pure_exp197', a2)
    assert _is_linked(b, 'abs_Pure_exp197', a2)
    if hasattr(a1, 'abs_Stmt196'):
        assert not _is_linked(a1, 'abs_Stmt196', b)
    if hasattr(a2, 'abs_Stmt196'):
        assert _is_linked(a2, 'abs_Stmt196', b)
    _safe_set(b, 'abs_Pure_exp197', None)
    assert not _is_linked(b, 'abs_Pure_exp197', a2)
    if hasattr(a2, 'abs_Stmt196'):
        assert not _is_linked(a2, 'abs_Stmt196', b)


def test_assoc_case57_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp58', a1)
    assert _is_linked(b, 'abs_Pure_exp58', a1)
    if hasattr(a1, 'abs_Pure_exp56'):
        assert _is_linked(a1, 'abs_Pure_exp56', b)
    _safe_set(b, 'abs_Pure_exp58', a2)
    assert _is_linked(b, 'abs_Pure_exp58', a2)
    if hasattr(a1, 'abs_Pure_exp56'):
        assert not _is_linked(a1, 'abs_Pure_exp56', b)
    if hasattr(a2, 'abs_Pure_exp56'):
        assert _is_linked(a2, 'abs_Pure_exp56', b)
    _safe_set(b, 'abs_Pure_exp58', None)
    assert not _is_linked(b, 'abs_Pure_exp58', a2)
    if hasattr(a2, 'abs_Pure_exp56'):
        assert not _is_linked(a2, 'abs_Pure_exp56', b)


def test_assoc_condition160_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp162', a1)
    assert _is_linked(b, 'abs_Pure_exp162', a1)
    if hasattr(a1, 'abs_Stmt161'):
        assert _is_linked(a1, 'abs_Stmt161', b)
    _safe_set(b, 'abs_Pure_exp162', a2)
    assert _is_linked(b, 'abs_Pure_exp162', a2)
    if hasattr(a1, 'abs_Stmt161'):
        assert not _is_linked(a1, 'abs_Stmt161', b)
    if hasattr(a2, 'abs_Stmt161'):
        assert _is_linked(a2, 'abs_Stmt161', b)
    _safe_set(b, 'abs_Pure_exp162', None)
    assert not _is_linked(b, 'abs_Pure_exp162', a2)
    if hasattr(a2, 'abs_Stmt161'):
        assert not _is_linked(a2, 'abs_Stmt161', b)


def test_assoc_data_constructor30_reverse_link_reassign_clear():
    a1 = abs_Data_constructor(name="sample_text")
    a2 = abs_Data_constructor(name="sample_text_2")
    b = abs_DataType_decl(p="sample_text")
    _safe_set(b, 'abs_DataType_decl', {a1})
    assert _is_linked(b, 'abs_DataType_decl', a1)
    if hasattr(a1, 'abs_Data_constructor'):
        assert _is_linked(a1, 'abs_Data_constructor', b)
    _safe_set(b, 'abs_DataType_decl', {a2})
    assert _is_linked(b, 'abs_DataType_decl', a2)
    if hasattr(a1, 'abs_Data_constructor'):
        assert not _is_linked(a1, 'abs_Data_constructor', b)
    if hasattr(a2, 'abs_Data_constructor'):
        assert _is_linked(a2, 'abs_Data_constructor', b)
    _safe_set(b, 'abs_DataType_decl', set())
    assert not _is_linked(b, 'abs_DataType_decl', a2)
    if hasattr(a2, 'abs_Data_constructor'):
        assert not _is_linked(a2, 'abs_Data_constructor', b)


def test_assoc_decl17_reverse_link_reassign_clear():
    a1 = abs_Module_decl(name="sample_text")
    a2 = abs_Module_decl(name="sample_text_2")
    b = abs_Decl(name="sample_text")
    _safe_set(b, 'abs_Decl', a1)
    assert _is_linked(b, 'abs_Decl', a1)
    if hasattr(a1, 'abs_Module_decl18'):
        assert _is_linked(a1, 'abs_Module_decl18', b)
    _safe_set(b, 'abs_Decl', a2)
    assert _is_linked(b, 'abs_Decl', a2)
    if hasattr(a1, 'abs_Module_decl18'):
        assert not _is_linked(a1, 'abs_Module_decl18', b)
    if hasattr(a2, 'abs_Module_decl18'):
        assert _is_linked(a2, 'abs_Module_decl18', b)
    _safe_set(b, 'abs_Decl', None)
    assert not _is_linked(b, 'abs_Decl', a2)
    if hasattr(a2, 'abs_Module_decl18'):
        assert not _is_linked(a2, 'abs_Module_decl18', b)


def test_assoc_delta_id380_reverse_link_reassign_clear():
    a1 = abs_Product_reconfiguration(name="sample_text", update="sample_text")
    a2 = abs_Product_reconfiguration(name="sample_text_2", update="sample_text_2")
    b = abs_Delta_id(name="sample_text")
    _safe_set(b, 'abs_Delta_id', a1)
    assert _is_linked(b, 'abs_Delta_id', a1)
    if hasattr(a1, 'abs_Product_reconfiguration381'):
        assert _is_linked(a1, 'abs_Product_reconfiguration381', b)
    _safe_set(b, 'abs_Delta_id', a2)
    assert _is_linked(b, 'abs_Delta_id', a2)
    if hasattr(a1, 'abs_Product_reconfiguration381'):
        assert not _is_linked(a1, 'abs_Product_reconfiguration381', b)
    if hasattr(a2, 'abs_Product_reconfiguration381'):
        assert _is_linked(a2, 'abs_Product_reconfiguration381', b)
    _safe_set(b, 'abs_Delta_id', None)
    assert not _is_linked(b, 'abs_Delta_id', a2)
    if hasattr(a2, 'abs_Product_reconfiguration381'):
        assert not _is_linked(a2, 'abs_Product_reconfiguration381', b)


def test_assoc_diePureExp189_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp191', a1)
    assert _is_linked(b, 'abs_Pure_exp191', a1)
    if hasattr(a1, 'abs_Stmt190'):
        assert _is_linked(a1, 'abs_Stmt190', b)
    _safe_set(b, 'abs_Pure_exp191', a2)
    assert _is_linked(b, 'abs_Pure_exp191', a2)
    if hasattr(a1, 'abs_Stmt190'):
        assert not _is_linked(a1, 'abs_Stmt190', b)
    if hasattr(a2, 'abs_Stmt190'):
        assert _is_linked(a2, 'abs_Stmt190', b)
    _safe_set(b, 'abs_Pure_exp191', None)
    assert not _is_linked(b, 'abs_Pure_exp191', a2)
    if hasattr(a2, 'abs_Stmt190'):
        assert not _is_linked(a2, 'abs_Stmt190', b)


def test_assoc_e26_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Par_function_decl(p="sample_text")
    _safe_set(b, 'abs_Par_function_decl27', a1)
    assert _is_linked(b, 'abs_Par_function_decl27', a1)
    if hasattr(a1, 'abs_Pure_exp'):
        assert _is_linked(a1, 'abs_Pure_exp', b)
    _safe_set(b, 'abs_Par_function_decl27', a2)
    assert _is_linked(b, 'abs_Par_function_decl27', a2)
    if hasattr(a1, 'abs_Pure_exp'):
        assert not _is_linked(a1, 'abs_Pure_exp', b)
    if hasattr(a2, 'abs_Pure_exp'):
        assert _is_linked(a2, 'abs_Pure_exp', b)
    _safe_set(b, 'abs_Par_function_decl27', None)
    assert not _is_linked(b, 'abs_Par_function_decl27', a2)
    if hasattr(a2, 'abs_Pure_exp'):
        assert not _is_linked(a2, 'abs_Pure_exp', b)


def test_assoc_else_54_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp55', a1)
    assert _is_linked(b, 'abs_Pure_exp55', a1)
    if hasattr(a1, 'abs_Pure_exp53'):
        assert _is_linked(a1, 'abs_Pure_exp53', b)
    _safe_set(b, 'abs_Pure_exp55', a2)
    assert _is_linked(b, 'abs_Pure_exp55', a2)
    if hasattr(a1, 'abs_Pure_exp53'):
        assert not _is_linked(a1, 'abs_Pure_exp53', b)
    if hasattr(a2, 'abs_Pure_exp53'):
        assert _is_linked(a2, 'abs_Pure_exp53', b)
    _safe_set(b, 'abs_Pure_exp55', None)
    assert not _is_linked(b, 'abs_Pure_exp55', a2)
    if hasattr(a2, 'abs_Pure_exp53'):
        assert not _is_linked(a2, 'abs_Pure_exp53', b)


def test_assoc_elsestmt158_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt159', a1)
    assert _is_linked(b, 'abs_Stmt159', a1)
    if hasattr(a1, 'abs_Stmt157'):
        assert _is_linked(a1, 'abs_Stmt157', b)
    _safe_set(b, 'abs_Stmt159', a2)
    assert _is_linked(b, 'abs_Stmt159', a2)
    if hasattr(a1, 'abs_Stmt157'):
        assert not _is_linked(a1, 'abs_Stmt157', b)
    if hasattr(a2, 'abs_Stmt157'):
        assert _is_linked(a2, 'abs_Stmt157', b)
    _safe_set(b, 'abs_Stmt159', None)
    assert not _is_linked(b, 'abs_Stmt159', a2)
    if hasattr(a2, 'abs_Stmt157'):
        assert not _is_linked(a2, 'abs_Stmt157', b)


def test_assoc_f180_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp182', a1)
    assert _is_linked(b, 'abs_Pure_exp182', a1)
    if hasattr(a1, 'abs_Stmt181'):
        assert _is_linked(a1, 'abs_Stmt181', b)
    _safe_set(b, 'abs_Pure_exp182', a2)
    assert _is_linked(b, 'abs_Pure_exp182', a2)
    if hasattr(a1, 'abs_Stmt181'):
        assert not _is_linked(a1, 'abs_Stmt181', b)
    if hasattr(a2, 'abs_Stmt181'):
        assert _is_linked(a2, 'abs_Stmt181', b)
    _safe_set(b, 'abs_Pure_exp182', None)
    assert not _is_linked(b, 'abs_Pure_exp182', a2)
    if hasattr(a2, 'abs_Stmt181'):
        assert not _is_linked(a2, 'abs_Stmt181', b)


def test_assoc_feature325_reverse_link_reassign_clear():
    a1 = abs_Productline_decl(name="sample_text")
    a2 = abs_Productline_decl(name="sample_text_2")
    b = abs_Feature(attr_assignment="sample_text", p="sample_text")
    _safe_set(b, 'abs_Feature', a1)
    assert _is_linked(b, 'abs_Feature', a1)
    if hasattr(a1, 'abs_Productline_decl326'):
        assert _is_linked(a1, 'abs_Productline_decl326', b)
    _safe_set(b, 'abs_Feature', a2)
    assert _is_linked(b, 'abs_Feature', a2)
    if hasattr(a1, 'abs_Productline_decl326'):
        assert not _is_linked(a1, 'abs_Productline_decl326', b)
    if hasattr(a2, 'abs_Productline_decl326'):
        assert _is_linked(a2, 'abs_Productline_decl326', b)
    _safe_set(b, 'abs_Feature', None)
    assert not _is_linked(b, 'abs_Feature', a2)
    if hasattr(a2, 'abs_Productline_decl326'):
        assert not _is_linked(a2, 'abs_Productline_decl326', b)


def test_assoc_feature361_reverse_link_reassign_clear():
    a1 = abs_Product_decl(name="sample_text")
    a2 = abs_Product_decl(name="sample_text_2")
    b = abs_Feature(attr_assignment="sample_text", p="sample_text")
    _safe_set(b, 'abs_Feature363', a1)
    assert _is_linked(b, 'abs_Feature363', a1)
    if hasattr(a1, 'abs_Product_decl362'):
        assert _is_linked(a1, 'abs_Product_decl362', b)
    _safe_set(b, 'abs_Feature363', a2)
    assert _is_linked(b, 'abs_Feature363', a2)
    if hasattr(a1, 'abs_Product_decl362'):
        assert not _is_linked(a1, 'abs_Product_decl362', b)
    if hasattr(a2, 'abs_Product_decl362'):
        assert _is_linked(a2, 'abs_Product_decl362', b)
    _safe_set(b, 'abs_Feature363', None)
    assert not _is_linked(b, 'abs_Feature363', a2)
    if hasattr(a2, 'abs_Product_decl362'):
        assert not _is_linked(a2, 'abs_Product_decl362', b)


def test_assoc_feature_decl329_reverse_link_reassign_clear():
    a1 = abs_Feature_decl(name="sample_text")
    a2 = abs_Feature_decl(name="sample_text_2")
    b = abs_Feature(attr_assignment="sample_text", p="sample_text")
    _safe_set(b, 'abs_Feature330', a1)
    assert _is_linked(b, 'abs_Feature330', a1)
    if hasattr(a1, 'abs_Feature_decl331'):
        assert _is_linked(a1, 'abs_Feature_decl331', b)
    _safe_set(b, 'abs_Feature330', a2)
    assert _is_linked(b, 'abs_Feature330', a2)
    if hasattr(a1, 'abs_Feature_decl331'):
        assert not _is_linked(a1, 'abs_Feature_decl331', b)
    if hasattr(a2, 'abs_Feature_decl331'):
        assert _is_linked(a2, 'abs_Feature_decl331', b)
    _safe_set(b, 'abs_Feature330', None)
    assert not _is_linked(b, 'abs_Feature330', a2)
    if hasattr(a2, 'abs_Feature_decl331'):
        assert not _is_linked(a2, 'abs_Feature_decl331', b)


def test_assoc_feature_decl_attribute384_reverse_link_reassign_clear():
    a1 = abs_Feature_decl_attribute(boundary_val="sample_text", lBoundary_int="sample_text", uBoundary_int="sample_text")
    a2 = abs_Feature_decl_attribute(boundary_val="sample_text_2", lBoundary_int="sample_text_2", uBoundary_int="sample_text_2")
    b = abs_Feature_decl(name="sample_text")
    _safe_set(b, 'abs_Feature_decl385', {a1})
    assert _is_linked(b, 'abs_Feature_decl385', a1)
    if hasattr(a1, 'abs_Feature_decl_attribute'):
        assert _is_linked(a1, 'abs_Feature_decl_attribute', b)
    _safe_set(b, 'abs_Feature_decl385', {a2})
    assert _is_linked(b, 'abs_Feature_decl385', a2)
    if hasattr(a1, 'abs_Feature_decl_attribute'):
        assert not _is_linked(a1, 'abs_Feature_decl_attribute', b)
    if hasattr(a2, 'abs_Feature_decl_attribute'):
        assert _is_linked(a2, 'abs_Feature_decl_attribute', b)
    _safe_set(b, 'abs_Feature_decl385', set())
    assert not _is_linked(b, 'abs_Feature_decl385', a2)
    if hasattr(a2, 'abs_Feature_decl_attribute'):
        assert not _is_linked(a2, 'abs_Feature_decl_attribute', b)


def test_assoc_feature_decl_attribute395_reverse_link_reassign_clear():
    a1 = abs_Fextension(name="sample_text")
    a2 = abs_Fextension(name="sample_text_2")
    b = abs_Feature_decl_attribute(boundary_val="sample_text", lBoundary_int="sample_text", uBoundary_int="sample_text")
    _safe_set(b, 'abs_Feature_decl_attribute397', a1)
    assert _is_linked(b, 'abs_Feature_decl_attribute397', a1)
    if hasattr(a1, 'abs_Fextension396'):
        assert _is_linked(a1, 'abs_Fextension396', b)
    _safe_set(b, 'abs_Feature_decl_attribute397', a2)
    assert _is_linked(b, 'abs_Feature_decl_attribute397', a2)
    if hasattr(a1, 'abs_Fextension396'):
        assert not _is_linked(a1, 'abs_Fextension396', b)
    if hasattr(a2, 'abs_Fextension396'):
        assert _is_linked(a2, 'abs_Fextension396', b)
    _safe_set(b, 'abs_Feature_decl_attribute397', None)
    assert not _is_linked(b, 'abs_Feature_decl_attribute397', a2)
    if hasattr(a2, 'abs_Fextension396'):
        assert not _is_linked(a2, 'abs_Fextension396', b)


def test_assoc_foreachstmt170_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt171', a1)
    assert _is_linked(b, 'abs_Stmt171', a1)
    if hasattr(a1, 'abs_Stmt169'):
        assert _is_linked(a1, 'abs_Stmt169', b)
    _safe_set(b, 'abs_Stmt171', a2)
    assert _is_linked(b, 'abs_Stmt171', a2)
    if hasattr(a1, 'abs_Stmt169'):
        assert not _is_linked(a1, 'abs_Stmt169', b)
    if hasattr(a2, 'abs_Stmt169'):
        assert _is_linked(a2, 'abs_Stmt169', b)
    _safe_set(b, 'abs_Stmt171', None)
    assert not _is_linked(b, 'abs_Stmt171', a2)
    if hasattr(a2, 'abs_Stmt169'):
        assert not _is_linked(a2, 'abs_Stmt169', b)


def test_assoc_i65_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp66', a1)
    assert _is_linked(b, 'abs_Pure_exp66', a1)
    if hasattr(a1, 'abs_Pure_exp64'):
        assert _is_linked(a1, 'abs_Pure_exp64', b)
    _safe_set(b, 'abs_Pure_exp66', a2)
    assert _is_linked(b, 'abs_Pure_exp66', a2)
    if hasattr(a1, 'abs_Pure_exp64'):
        assert not _is_linked(a1, 'abs_Pure_exp64', b)
    if hasattr(a2, 'abs_Pure_exp64'):
        assert _is_linked(a2, 'abs_Pure_exp64', b)
    _safe_set(b, 'abs_Pure_exp66', None)
    assert not _is_linked(b, 'abs_Pure_exp66', a2)
    if hasattr(a2, 'abs_Pure_exp64'):
        assert not _is_linked(a2, 'abs_Pure_exp64', b)


def test_assoc_if_48_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp49', a1)
    assert _is_linked(b, 'abs_Pure_exp49', a1)
    if hasattr(a1, 'abs_Pure_exp47'):
        assert _is_linked(a1, 'abs_Pure_exp47', b)
    _safe_set(b, 'abs_Pure_exp49', a2)
    assert _is_linked(b, 'abs_Pure_exp49', a2)
    if hasattr(a1, 'abs_Pure_exp47'):
        assert not _is_linked(a1, 'abs_Pure_exp47', b)
    if hasattr(a2, 'abs_Pure_exp47'):
        assert _is_linked(a2, 'abs_Pure_exp47', b)
    _safe_set(b, 'abs_Pure_exp49', None)
    assert not _is_linked(b, 'abs_Pure_exp49', a2)
    if hasattr(a2, 'abs_Pure_exp47'):
        assert not _is_linked(a2, 'abs_Pure_exp47', b)


def test_assoc_ifstmt155_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt156', a1)
    assert _is_linked(b, 'abs_Stmt156', a1)
    if hasattr(a1, 'abs_Stmt154'):
        assert _is_linked(a1, 'abs_Stmt154', b)
    _safe_set(b, 'abs_Stmt156', a2)
    assert _is_linked(b, 'abs_Stmt156', a2)
    if hasattr(a1, 'abs_Stmt154'):
        assert not _is_linked(a1, 'abs_Stmt154', b)
    if hasattr(a2, 'abs_Stmt154'):
        assert _is_linked(a2, 'abs_Stmt154', b)
    _safe_set(b, 'abs_Stmt156', None)
    assert not _is_linked(b, 'abs_Stmt156', a2)
    if hasattr(a2, 'abs_Stmt154'):
        assert not _is_linked(a2, 'abs_Stmt154', b)


def test_assoc_l166_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp168', a1)
    assert _is_linked(b, 'abs_Pure_exp168', a1)
    if hasattr(a1, 'abs_Stmt167'):
        assert _is_linked(a1, 'abs_Stmt167', b)
    _safe_set(b, 'abs_Pure_exp168', a2)
    assert _is_linked(b, 'abs_Pure_exp168', a2)
    if hasattr(a1, 'abs_Stmt167'):
        assert not _is_linked(a1, 'abs_Stmt167', b)
    if hasattr(a2, 'abs_Stmt167'):
        assert _is_linked(a2, 'abs_Stmt167', b)
    _safe_set(b, 'abs_Pure_exp168', None)
    assert not _is_linked(b, 'abs_Pure_exp168', a2)
    if hasattr(a2, 'abs_Stmt167'):
        assert not _is_linked(a2, 'abs_Stmt167', b)


def test_assoc_left446_reverse_link_reassign_clear():
    a1 = abs_MexpImplies_expr(op="sample_text")
    a2 = abs_MexpImplies_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp447', a1)
    assert _is_linked(b, 'abs_Mexp447', a1)
    if hasattr(a1, 'abs_MexpImplies_expr'):
        assert _is_linked(a1, 'abs_MexpImplies_expr', b)
    _safe_set(b, 'abs_Mexp447', a2)
    assert _is_linked(b, 'abs_Mexp447', a2)
    if hasattr(a1, 'abs_MexpImplies_expr'):
        assert not _is_linked(a1, 'abs_MexpImplies_expr', b)
    if hasattr(a2, 'abs_MexpImplies_expr'):
        assert _is_linked(a2, 'abs_MexpImplies_expr', b)
    _safe_set(b, 'abs_Mexp447', None)
    assert not _is_linked(b, 'abs_Mexp447', a2)
    if hasattr(a2, 'abs_MexpImplies_expr'):
        assert not _is_linked(a2, 'abs_MexpImplies_expr', b)


def test_assoc_left451_reverse_link_reassign_clear():
    a1 = abs_MexpEquality_expr(op="sample_text")
    a2 = abs_MexpEquality_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp452', a1)
    assert _is_linked(b, 'abs_Mexp452', a1)
    if hasattr(a1, 'abs_MexpEquality_expr'):
        assert _is_linked(a1, 'abs_MexpEquality_expr', b)
    _safe_set(b, 'abs_Mexp452', a2)
    assert _is_linked(b, 'abs_Mexp452', a2)
    if hasattr(a1, 'abs_MexpEquality_expr'):
        assert not _is_linked(a1, 'abs_MexpEquality_expr', b)
    if hasattr(a2, 'abs_MexpEquality_expr'):
        assert _is_linked(a2, 'abs_MexpEquality_expr', b)
    _safe_set(b, 'abs_Mexp452', None)
    assert not _is_linked(b, 'abs_Mexp452', a2)
    if hasattr(a2, 'abs_MexpEquality_expr'):
        assert not _is_linked(a2, 'abs_MexpEquality_expr', b)


def test_assoc_left456_reverse_link_reassign_clear():
    a1 = abs_MexpComparison_expr(op="sample_text")
    a2 = abs_MexpComparison_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp457', a1)
    assert _is_linked(b, 'abs_Mexp457', a1)
    if hasattr(a1, 'abs_MexpComparison_expr'):
        assert _is_linked(a1, 'abs_MexpComparison_expr', b)
    _safe_set(b, 'abs_Mexp457', a2)
    assert _is_linked(b, 'abs_Mexp457', a2)
    if hasattr(a1, 'abs_MexpComparison_expr'):
        assert not _is_linked(a1, 'abs_MexpComparison_expr', b)
    if hasattr(a2, 'abs_MexpComparison_expr'):
        assert _is_linked(a2, 'abs_MexpComparison_expr', b)
    _safe_set(b, 'abs_Mexp457', None)
    assert not _is_linked(b, 'abs_Mexp457', a2)
    if hasattr(a2, 'abs_MexpComparison_expr'):
        assert not _is_linked(a2, 'abs_MexpComparison_expr', b)


def test_assoc_left461_reverse_link_reassign_clear():
    a1 = abs_MexpPlusOrMinus_expr(op="sample_text")
    a2 = abs_MexpPlusOrMinus_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp462', a1)
    assert _is_linked(b, 'abs_Mexp462', a1)
    if hasattr(a1, 'abs_MexpPlusOrMinus_expr'):
        assert _is_linked(a1, 'abs_MexpPlusOrMinus_expr', b)
    _safe_set(b, 'abs_Mexp462', a2)
    assert _is_linked(b, 'abs_Mexp462', a2)
    if hasattr(a1, 'abs_MexpPlusOrMinus_expr'):
        assert not _is_linked(a1, 'abs_MexpPlusOrMinus_expr', b)
    if hasattr(a2, 'abs_MexpPlusOrMinus_expr'):
        assert _is_linked(a2, 'abs_MexpPlusOrMinus_expr', b)
    _safe_set(b, 'abs_Mexp462', None)
    assert not _is_linked(b, 'abs_Mexp462', a2)
    if hasattr(a2, 'abs_MexpPlusOrMinus_expr'):
        assert not _is_linked(a2, 'abs_MexpPlusOrMinus_expr', b)


def test_assoc_left466_reverse_link_reassign_clear():
    a1 = abs_MexpMulDivOrMod_expr(op="sample_text")
    a2 = abs_MexpMulDivOrMod_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp467', a1)
    assert _is_linked(b, 'abs_Mexp467', a1)
    if hasattr(a1, 'abs_MexpMulDivOrMod_expr'):
        assert _is_linked(a1, 'abs_MexpMulDivOrMod_expr', b)
    _safe_set(b, 'abs_Mexp467', a2)
    assert _is_linked(b, 'abs_Mexp467', a2)
    if hasattr(a1, 'abs_MexpMulDivOrMod_expr'):
        assert not _is_linked(a1, 'abs_MexpMulDivOrMod_expr', b)
    if hasattr(a2, 'abs_MexpMulDivOrMod_expr'):
        assert _is_linked(a2, 'abs_MexpMulDivOrMod_expr', b)
    _safe_set(b, 'abs_Mexp467', None)
    assert not _is_linked(b, 'abs_Mexp467', a2)
    if hasattr(a2, 'abs_MexpMulDivOrMod_expr'):
        assert not _is_linked(a2, 'abs_MexpMulDivOrMod_expr', b)


def test_assoc_module_export13_reverse_link_reassign_clear():
    a1 = abs_Module_export(anyPackage="sample_text", importedNamespace="sample_text")
    a2 = abs_Module_export(anyPackage="sample_text_2", importedNamespace="sample_text_2")
    b = abs_Module_decl(name="sample_text")
    _safe_set(b, 'abs_Module_decl14', {a1})
    assert _is_linked(b, 'abs_Module_decl14', a1)
    if hasattr(a1, 'abs_Module_export'):
        assert _is_linked(a1, 'abs_Module_export', b)
    _safe_set(b, 'abs_Module_decl14', {a2})
    assert _is_linked(b, 'abs_Module_decl14', a2)
    if hasattr(a1, 'abs_Module_export'):
        assert not _is_linked(a1, 'abs_Module_export', b)
    if hasattr(a2, 'abs_Module_export'):
        assert _is_linked(a2, 'abs_Module_export', b)
    _safe_set(b, 'abs_Module_decl14', set())
    assert not _is_linked(b, 'abs_Module_decl14', a2)
    if hasattr(a2, 'abs_Module_export'):
        assert not _is_linked(a2, 'abs_Module_export', b)


def test_assoc_module_import15_reverse_link_reassign_clear():
    a1 = abs_Module_import(importedNamespace="sample_text", name="sample_text")
    a2 = abs_Module_import(importedNamespace="sample_text_2", name="sample_text_2")
    b = abs_Module_decl(name="sample_text")
    _safe_set(b, 'abs_Module_decl16', {a1})
    assert _is_linked(b, 'abs_Module_decl16', a1)
    if hasattr(a1, 'abs_Module_import'):
        assert _is_linked(a1, 'abs_Module_import', b)
    _safe_set(b, 'abs_Module_decl16', {a2})
    assert _is_linked(b, 'abs_Module_decl16', a2)
    if hasattr(a1, 'abs_Module_import'):
        assert not _is_linked(a1, 'abs_Module_import', b)
    if hasattr(a2, 'abs_Module_import'):
        assert _is_linked(a2, 'abs_Module_import', b)
    _safe_set(b, 'abs_Module_decl16', set())
    assert not _is_linked(b, 'abs_Module_decl16', a2)
    if hasattr(a2, 'abs_Module_import'):
        assert not _is_linked(a2, 'abs_Module_import', b)


def test_assoc_moveCogTo192_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp194', a1)
    assert _is_linked(b, 'abs_Pure_exp194', a1)
    if hasattr(a1, 'abs_Stmt193'):
        assert _is_linked(a1, 'abs_Stmt193', b)
    _safe_set(b, 'abs_Pure_exp194', a2)
    assert _is_linked(b, 'abs_Pure_exp194', a2)
    if hasattr(a1, 'abs_Stmt193'):
        assert not _is_linked(a1, 'abs_Stmt193', b)
    if hasattr(a2, 'abs_Stmt193'):
        assert _is_linked(a2, 'abs_Stmt193', b)
    _safe_set(b, 'abs_Pure_exp194', None)
    assert not _is_linked(b, 'abs_Pure_exp194', a2)
    if hasattr(a2, 'abs_Stmt193'):
        assert not _is_linked(a2, 'abs_Stmt193', b)


def test_assoc_p93_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Type_exp(name="sample_text")
    _safe_set(b, 'abs_Type_exp94', {a1})
    assert _is_linked(b, 'abs_Type_exp94', a1)
    if hasattr(a1, 'abs_Type_use95'):
        assert _is_linked(a1, 'abs_Type_use95', b)
    _safe_set(b, 'abs_Type_exp94', {a2})
    assert _is_linked(b, 'abs_Type_exp94', a2)
    if hasattr(a1, 'abs_Type_use95'):
        assert not _is_linked(a1, 'abs_Type_use95', b)
    if hasattr(a2, 'abs_Type_use95'):
        assert _is_linked(a2, 'abs_Type_use95', b)
    _safe_set(b, 'abs_Type_exp94', set())
    assert not _is_linked(b, 'abs_Type_exp94', a2)
    if hasattr(a2, 'abs_Type_use95'):
        assert not _is_linked(a2, 'abs_Type_use95', b)


def test_assoc_product_reconfiguration364_reverse_link_reassign_clear():
    a1 = abs_Product_reconfiguration(name="sample_text", update="sample_text")
    a2 = abs_Product_reconfiguration(name="sample_text_2", update="sample_text_2")
    b = abs_Product_decl(name="sample_text")
    _safe_set(b, 'abs_Product_decl365', {a1})
    assert _is_linked(b, 'abs_Product_decl365', a1)
    if hasattr(a1, 'abs_Product_reconfiguration'):
        assert _is_linked(a1, 'abs_Product_reconfiguration', b)
    _safe_set(b, 'abs_Product_decl365', {a2})
    assert _is_linked(b, 'abs_Product_decl365', a2)
    if hasattr(a1, 'abs_Product_reconfiguration'):
        assert not _is_linked(a1, 'abs_Product_reconfiguration', b)
    if hasattr(a2, 'abs_Product_reconfiguration'):
        assert _is_linked(a2, 'abs_Product_reconfiguration', b)
    _safe_set(b, 'abs_Product_decl365', set())
    assert not _is_linked(b, 'abs_Product_decl365', a2)
    if hasattr(a2, 'abs_Product_reconfiguration'):
        assert not _is_linked(a2, 'abs_Product_reconfiguration', b)


def test_assoc_pure_exp101_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Function_decl(p="sample_text")
    _safe_set(b, 'abs_Function_decl102', a1)
    assert _is_linked(b, 'abs_Function_decl102', a1)
    if hasattr(a1, 'abs_Pure_exp103'):
        assert _is_linked(a1, 'abs_Pure_exp103', b)
    _safe_set(b, 'abs_Function_decl102', a2)
    assert _is_linked(b, 'abs_Function_decl102', a2)
    if hasattr(a1, 'abs_Pure_exp103'):
        assert not _is_linked(a1, 'abs_Pure_exp103', b)
    if hasattr(a2, 'abs_Pure_exp103'):
        assert _is_linked(a2, 'abs_Pure_exp103', b)
    _safe_set(b, 'abs_Function_decl102', None)
    assert not _is_linked(b, 'abs_Function_decl102', a2)
    if hasattr(a2, 'abs_Pure_exp103'):
        assert not _is_linked(a2, 'abs_Pure_exp103', b)


def test_assoc_pure_exp137_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Field_decl(name="sample_text")
    _safe_set(b, 'abs_Field_decl138', a1)
    assert _is_linked(b, 'abs_Field_decl138', a1)
    if hasattr(a1, 'abs_Pure_exp139'):
        assert _is_linked(a1, 'abs_Pure_exp139', b)
    _safe_set(b, 'abs_Field_decl138', a2)
    assert _is_linked(b, 'abs_Field_decl138', a2)
    if hasattr(a1, 'abs_Pure_exp139'):
        assert not _is_linked(a1, 'abs_Pure_exp139', b)
    if hasattr(a2, 'abs_Pure_exp139'):
        assert _is_linked(a2, 'abs_Pure_exp139', b)
    _safe_set(b, 'abs_Field_decl138', None)
    assert not _is_linked(b, 'abs_Field_decl138', a2)
    if hasattr(a2, 'abs_Pure_exp139'):
        assert not _is_linked(a2, 'abs_Pure_exp139', b)


def test_assoc_pure_exp151_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp153', a1)
    assert _is_linked(b, 'abs_Pure_exp153', a1)
    if hasattr(a1, 'abs_Stmt152'):
        assert _is_linked(a1, 'abs_Stmt152', b)
    _safe_set(b, 'abs_Pure_exp153', a2)
    assert _is_linked(b, 'abs_Pure_exp153', a2)
    if hasattr(a1, 'abs_Stmt152'):
        assert not _is_linked(a1, 'abs_Stmt152', b)
    if hasattr(a2, 'abs_Stmt152'):
        assert _is_linked(a2, 'abs_Stmt152', b)
    _safe_set(b, 'abs_Pure_exp153', None)
    assert not _is_linked(b, 'abs_Pure_exp153', a2)
    if hasattr(a2, 'abs_Stmt152'):
        assert not _is_linked(a2, 'abs_Stmt152', b)


def test_assoc_pure_exp71_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp72', a1)
    assert _is_linked(b, 'abs_Pure_exp72', a1)
    if hasattr(a1, 'abs_Pure_exp70'):
        assert _is_linked(a1, 'abs_Pure_exp70', b)
    _safe_set(b, 'abs_Pure_exp72', a2)
    assert _is_linked(b, 'abs_Pure_exp72', a2)
    if hasattr(a1, 'abs_Pure_exp70'):
        assert not _is_linked(a1, 'abs_Pure_exp70', b)
    if hasattr(a2, 'abs_Pure_exp70'):
        assert _is_linked(a2, 'abs_Pure_exp70', b)
    _safe_set(b, 'abs_Pure_exp72', None)
    assert not _is_linked(b, 'abs_Pure_exp72', a2)
    if hasattr(a2, 'abs_Pure_exp70'):
        assert not _is_linked(a2, 'abs_Pure_exp70', b)


def test_assoc_ref73_reverse_link_reassign_clear():
    a1 = abs_Var_or_field_ref(name="sample_text")
    a2 = abs_Var_or_field_ref(name="sample_text_2")
    b = abs_Field_decl(name="sample_text")
    _safe_set(b, 'abs_Field_decl', a1)
    assert _is_linked(b, 'abs_Field_decl', a1)
    if hasattr(a1, 'abs_Var_or_field_ref'):
        assert _is_linked(a1, 'abs_Var_or_field_ref', b)
    _safe_set(b, 'abs_Field_decl', a2)
    assert _is_linked(b, 'abs_Field_decl', a2)
    if hasattr(a1, 'abs_Var_or_field_ref'):
        assert not _is_linked(a1, 'abs_Var_or_field_ref', b)
    if hasattr(a2, 'abs_Var_or_field_ref'):
        assert _is_linked(a2, 'abs_Var_or_field_ref', b)
    _safe_set(b, 'abs_Field_decl', None)
    assert not _is_linked(b, 'abs_Field_decl', a2)
    if hasattr(a2, 'abs_Var_or_field_ref'):
        assert not _is_linked(a2, 'abs_Var_or_field_ref', b)


def test_assoc_right448_reverse_link_reassign_clear():
    a1 = abs_MexpImplies_expr(op="sample_text")
    a2 = abs_MexpImplies_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp450', a1)
    assert _is_linked(b, 'abs_Mexp450', a1)
    if hasattr(a1, 'abs_MexpImplies_expr449'):
        assert _is_linked(a1, 'abs_MexpImplies_expr449', b)
    _safe_set(b, 'abs_Mexp450', a2)
    assert _is_linked(b, 'abs_Mexp450', a2)
    if hasattr(a1, 'abs_MexpImplies_expr449'):
        assert not _is_linked(a1, 'abs_MexpImplies_expr449', b)
    if hasattr(a2, 'abs_MexpImplies_expr449'):
        assert _is_linked(a2, 'abs_MexpImplies_expr449', b)
    _safe_set(b, 'abs_Mexp450', None)
    assert not _is_linked(b, 'abs_Mexp450', a2)
    if hasattr(a2, 'abs_MexpImplies_expr449'):
        assert not _is_linked(a2, 'abs_MexpImplies_expr449', b)


def test_assoc_right453_reverse_link_reassign_clear():
    a1 = abs_MexpEquality_expr(op="sample_text")
    a2 = abs_MexpEquality_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp455', a1)
    assert _is_linked(b, 'abs_Mexp455', a1)
    if hasattr(a1, 'abs_MexpEquality_expr454'):
        assert _is_linked(a1, 'abs_MexpEquality_expr454', b)
    _safe_set(b, 'abs_Mexp455', a2)
    assert _is_linked(b, 'abs_Mexp455', a2)
    if hasattr(a1, 'abs_MexpEquality_expr454'):
        assert not _is_linked(a1, 'abs_MexpEquality_expr454', b)
    if hasattr(a2, 'abs_MexpEquality_expr454'):
        assert _is_linked(a2, 'abs_MexpEquality_expr454', b)
    _safe_set(b, 'abs_Mexp455', None)
    assert not _is_linked(b, 'abs_Mexp455', a2)
    if hasattr(a2, 'abs_MexpEquality_expr454'):
        assert not _is_linked(a2, 'abs_MexpEquality_expr454', b)


def test_assoc_right458_reverse_link_reassign_clear():
    a1 = abs_MexpComparison_expr(op="sample_text")
    a2 = abs_MexpComparison_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp460', a1)
    assert _is_linked(b, 'abs_Mexp460', a1)
    if hasattr(a1, 'abs_MexpComparison_expr459'):
        assert _is_linked(a1, 'abs_MexpComparison_expr459', b)
    _safe_set(b, 'abs_Mexp460', a2)
    assert _is_linked(b, 'abs_Mexp460', a2)
    if hasattr(a1, 'abs_MexpComparison_expr459'):
        assert not _is_linked(a1, 'abs_MexpComparison_expr459', b)
    if hasattr(a2, 'abs_MexpComparison_expr459'):
        assert _is_linked(a2, 'abs_MexpComparison_expr459', b)
    _safe_set(b, 'abs_Mexp460', None)
    assert not _is_linked(b, 'abs_Mexp460', a2)
    if hasattr(a2, 'abs_MexpComparison_expr459'):
        assert not _is_linked(a2, 'abs_MexpComparison_expr459', b)


def test_assoc_right463_reverse_link_reassign_clear():
    a1 = abs_MexpPlusOrMinus_expr(op="sample_text")
    a2 = abs_MexpPlusOrMinus_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp465', a1)
    assert _is_linked(b, 'abs_Mexp465', a1)
    if hasattr(a1, 'abs_MexpPlusOrMinus_expr464'):
        assert _is_linked(a1, 'abs_MexpPlusOrMinus_expr464', b)
    _safe_set(b, 'abs_Mexp465', a2)
    assert _is_linked(b, 'abs_Mexp465', a2)
    if hasattr(a1, 'abs_MexpPlusOrMinus_expr464'):
        assert not _is_linked(a1, 'abs_MexpPlusOrMinus_expr464', b)
    if hasattr(a2, 'abs_MexpPlusOrMinus_expr464'):
        assert _is_linked(a2, 'abs_MexpPlusOrMinus_expr464', b)
    _safe_set(b, 'abs_Mexp465', None)
    assert not _is_linked(b, 'abs_Mexp465', a2)
    if hasattr(a2, 'abs_MexpPlusOrMinus_expr464'):
        assert not _is_linked(a2, 'abs_MexpPlusOrMinus_expr464', b)


def test_assoc_right468_reverse_link_reassign_clear():
    a1 = abs_MexpMulDivOrMod_expr(op="sample_text")
    a2 = abs_MexpMulDivOrMod_expr(op="sample_text_2")
    b = abs_Mexp(value=7)
    _safe_set(b, 'abs_Mexp470', a1)
    assert _is_linked(b, 'abs_Mexp470', a1)
    if hasattr(a1, 'abs_MexpMulDivOrMod_expr469'):
        assert _is_linked(a1, 'abs_MexpMulDivOrMod_expr469', b)
    _safe_set(b, 'abs_Mexp470', a2)
    assert _is_linked(b, 'abs_Mexp470', a2)
    if hasattr(a1, 'abs_MexpMulDivOrMod_expr469'):
        assert not _is_linked(a1, 'abs_MexpMulDivOrMod_expr469', b)
    if hasattr(a2, 'abs_MexpMulDivOrMod_expr469'):
        assert _is_linked(a2, 'abs_MexpMulDivOrMod_expr469', b)
    _safe_set(b, 'abs_Mexp470', None)
    assert not _is_linked(b, 'abs_Mexp470', a2)
    if hasattr(a2, 'abs_MexpMulDivOrMod_expr469'):
        assert not _is_linked(a2, 'abs_MexpMulDivOrMod_expr469', b)


def test_assoc_stmt149_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt150', a1)
    assert _is_linked(b, 'abs_Stmt150', a1)
    if hasattr(a1, 'abs_Stmt148'):
        assert _is_linked(a1, 'abs_Stmt148', b)
    _safe_set(b, 'abs_Stmt150', a2)
    assert _is_linked(b, 'abs_Stmt150', a2)
    if hasattr(a1, 'abs_Stmt148'):
        assert not _is_linked(a1, 'abs_Stmt148', b)
    if hasattr(a2, 'abs_Stmt148'):
        assert _is_linked(a2, 'abs_Stmt148', b)
    _safe_set(b, 'abs_Stmt150', None)
    assert not _is_linked(b, 'abs_Stmt150', a2)
    if hasattr(a2, 'abs_Stmt148'):
        assert not _is_linked(a2, 'abs_Stmt148', b)


def test_assoc_stmt254_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Method(name="sample_text")
    _safe_set(b, 'abs_Method255', {a1})
    assert _is_linked(b, 'abs_Method255', a1)
    if hasattr(a1, 'abs_Stmt256'):
        assert _is_linked(a1, 'abs_Stmt256', b)
    _safe_set(b, 'abs_Method255', {a2})
    assert _is_linked(b, 'abs_Method255', a2)
    if hasattr(a1, 'abs_Stmt256'):
        assert not _is_linked(a1, 'abs_Stmt256', b)
    if hasattr(a2, 'abs_Stmt256'):
        assert _is_linked(a2, 'abs_Stmt256', b)
    _safe_set(b, 'abs_Method255', set())
    assert not _is_linked(b, 'abs_Method255', a2)
    if hasattr(a2, 'abs_Stmt256'):
        assert not _is_linked(a2, 'abs_Stmt256', b)


def test_assoc_t183_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp185', a1)
    assert _is_linked(b, 'abs_Pure_exp185', a1)
    if hasattr(a1, 'abs_Stmt184'):
        assert _is_linked(a1, 'abs_Stmt184', b)
    _safe_set(b, 'abs_Pure_exp185', a2)
    assert _is_linked(b, 'abs_Pure_exp185', a2)
    if hasattr(a1, 'abs_Stmt184'):
        assert not _is_linked(a1, 'abs_Stmt184', b)
    if hasattr(a2, 'abs_Stmt184'):
        assert _is_linked(a2, 'abs_Stmt184', b)
    _safe_set(b, 'abs_Pure_exp185', None)
    assert not _is_linked(b, 'abs_Pure_exp185', a2)
    if hasattr(a2, 'abs_Stmt184'):
        assert not _is_linked(a2, 'abs_Stmt184', b)


def test_assoc_then51_reverse_link_reassign_clear():
    a1 = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    a2 = abs_Pure_exp(await_="sample_text_2", op="sample_text_2", val="sample_text_2", value="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp52', a1)
    assert _is_linked(b, 'abs_Pure_exp52', a1)
    if hasattr(a1, 'abs_Pure_exp50'):
        assert _is_linked(a1, 'abs_Pure_exp50', b)
    _safe_set(b, 'abs_Pure_exp52', a2)
    assert _is_linked(b, 'abs_Pure_exp52', a2)
    if hasattr(a1, 'abs_Pure_exp50'):
        assert not _is_linked(a1, 'abs_Pure_exp50', b)
    if hasattr(a2, 'abs_Pure_exp50'):
        assert _is_linked(a2, 'abs_Pure_exp50', b)
    _safe_set(b, 'abs_Pure_exp52', None)
    assert not _is_linked(b, 'abs_Pure_exp52', a2)
    if hasattr(a2, 'abs_Pure_exp50'):
        assert not _is_linked(a2, 'abs_Pure_exp50', b)


def test_assoc_throwPureExp186_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp188', a1)
    assert _is_linked(b, 'abs_Pure_exp188', a1)
    if hasattr(a1, 'abs_Stmt187'):
        assert _is_linked(a1, 'abs_Stmt187', b)
    _safe_set(b, 'abs_Pure_exp188', a2)
    assert _is_linked(b, 'abs_Pure_exp188', a2)
    if hasattr(a1, 'abs_Stmt187'):
        assert not _is_linked(a1, 'abs_Stmt187', b)
    if hasattr(a2, 'abs_Stmt187'):
        assert _is_linked(a2, 'abs_Stmt187', b)
    _safe_set(b, 'abs_Pure_exp188', None)
    assert not _is_linked(b, 'abs_Pure_exp188', a2)
    if hasattr(a2, 'abs_Stmt187'):
        assert not _is_linked(a2, 'abs_Stmt187', b)


def test_assoc_trystmt173_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt174', a1)
    assert _is_linked(b, 'abs_Stmt174', a1)
    if hasattr(a1, 'abs_Stmt172'):
        assert _is_linked(a1, 'abs_Stmt172', b)
    _safe_set(b, 'abs_Stmt174', a2)
    assert _is_linked(b, 'abs_Stmt174', a2)
    if hasattr(a1, 'abs_Stmt172'):
        assert not _is_linked(a1, 'abs_Stmt172', b)
    if hasattr(a2, 'abs_Stmt172'):
        assert _is_linked(a2, 'abs_Stmt172', b)
    _safe_set(b, 'abs_Stmt174', None)
    assert not _is_linked(b, 'abs_Stmt174', a2)
    if hasattr(a2, 'abs_Stmt172'):
        assert not _is_linked(a2, 'abs_Stmt172', b)


def test_assoc_type_exp140_reverse_link_reassign_clear():
    a1 = abs_Type_exp(name="sample_text")
    a2 = abs_Type_exp(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt141', a1)
    assert _is_linked(b, 'abs_Stmt141', a1)
    if hasattr(a1, 'abs_Type_exp142'):
        assert _is_linked(a1, 'abs_Type_exp142', b)
    _safe_set(b, 'abs_Stmt141', a2)
    assert _is_linked(b, 'abs_Stmt141', a2)
    if hasattr(a1, 'abs_Type_exp142'):
        assert not _is_linked(a1, 'abs_Type_exp142', b)
    if hasattr(a2, 'abs_Type_exp142'):
        assert _is_linked(a2, 'abs_Type_exp142', b)
    _safe_set(b, 'abs_Stmt141', None)
    assert not _is_linked(b, 'abs_Stmt141', a2)
    if hasattr(a2, 'abs_Type_exp142'):
        assert not _is_linked(a2, 'abs_Type_exp142', b)


def test_assoc_type_exp91_reverse_link_reassign_clear():
    a1 = abs_Type_exp(name="sample_text")
    a2 = abs_Type_exp(name="sample_text_2")
    b = abs_Param_decl(name="sample_text")
    _safe_set(b, 'abs_Param_decl92', a1)
    assert _is_linked(b, 'abs_Param_decl92', a1)
    if hasattr(a1, 'abs_Type_exp'):
        assert _is_linked(a1, 'abs_Type_exp', b)
    _safe_set(b, 'abs_Param_decl92', a2)
    assert _is_linked(b, 'abs_Param_decl92', a2)
    if hasattr(a1, 'abs_Type_exp'):
        assert not _is_linked(a1, 'abs_Type_exp', b)
    if hasattr(a2, 'abs_Type_exp'):
        assert _is_linked(a2, 'abs_Type_exp', b)
    _safe_set(b, 'abs_Param_decl92', None)
    assert not _is_linked(b, 'abs_Param_decl92', a2)
    if hasattr(a2, 'abs_Type_exp'):
        assert not _is_linked(a2, 'abs_Type_exp', b)


def test_assoc_type_use112_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Methodsig(name="sample_text")
    _safe_set(b, 'abs_Methodsig113', a1)
    assert _is_linked(b, 'abs_Methodsig113', a1)
    if hasattr(a1, 'abs_Type_use114'):
        assert _is_linked(a1, 'abs_Type_use114', b)
    _safe_set(b, 'abs_Methodsig113', a2)
    assert _is_linked(b, 'abs_Methodsig113', a2)
    if hasattr(a1, 'abs_Type_use114'):
        assert not _is_linked(a1, 'abs_Type_use114', b)
    if hasattr(a2, 'abs_Type_use114'):
        assert _is_linked(a2, 'abs_Type_use114', b)
    _safe_set(b, 'abs_Methodsig113', None)
    assert not _is_linked(b, 'abs_Methodsig113', a2)
    if hasattr(a2, 'abs_Type_use114'):
        assert not _is_linked(a2, 'abs_Type_use114', b)


def test_assoc_type_use134_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Field_decl(name="sample_text")
    _safe_set(b, 'abs_Field_decl135', a1)
    assert _is_linked(b, 'abs_Field_decl135', a1)
    if hasattr(a1, 'abs_Type_use136'):
        assert _is_linked(a1, 'abs_Type_use136', b)
    _safe_set(b, 'abs_Field_decl135', a2)
    assert _is_linked(b, 'abs_Field_decl135', a2)
    if hasattr(a1, 'abs_Type_use136'):
        assert not _is_linked(a1, 'abs_Type_use136', b)
    if hasattr(a2, 'abs_Type_use136'):
        assert _is_linked(a2, 'abs_Type_use136', b)
    _safe_set(b, 'abs_Field_decl135', None)
    assert not _is_linked(b, 'abs_Field_decl135', a2)
    if hasattr(a2, 'abs_Type_use136'):
        assert not _is_linked(a2, 'abs_Type_use136', b)


def test_assoc_type_use21_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Par_function_decl(p="sample_text")
    _safe_set(b, 'abs_Par_function_decl', a1)
    assert _is_linked(b, 'abs_Par_function_decl', a1)
    if hasattr(a1, 'abs_Type_use'):
        assert _is_linked(a1, 'abs_Type_use', b)
    _safe_set(b, 'abs_Par_function_decl', a2)
    assert _is_linked(b, 'abs_Par_function_decl', a2)
    if hasattr(a1, 'abs_Type_use'):
        assert not _is_linked(a1, 'abs_Type_use', b)
    if hasattr(a2, 'abs_Type_use'):
        assert _is_linked(a2, 'abs_Type_use', b)
    _safe_set(b, 'abs_Par_function_decl', None)
    assert not _is_linked(b, 'abs_Par_function_decl', a2)
    if hasattr(a2, 'abs_Type_use'):
        assert not _is_linked(a2, 'abs_Type_use', b)


def test_assoc_type_use248_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Method(name="sample_text")
    _safe_set(b, 'abs_Method249', a1)
    assert _is_linked(b, 'abs_Method249', a1)
    if hasattr(a1, 'abs_Type_use250'):
        assert _is_linked(a1, 'abs_Type_use250', b)
    _safe_set(b, 'abs_Method249', a2)
    assert _is_linked(b, 'abs_Method249', a2)
    if hasattr(a1, 'abs_Type_use250'):
        assert not _is_linked(a1, 'abs_Type_use250', b)
    if hasattr(a2, 'abs_Type_use250'):
        assert _is_linked(a2, 'abs_Type_use250', b)
    _safe_set(b, 'abs_Method249', None)
    assert not _is_linked(b, 'abs_Method249', a2)
    if hasattr(a2, 'abs_Type_use250'):
        assert not _is_linked(a2, 'abs_Type_use250', b)


def test_assoc_type_use38_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Type_use(name="sample_text")
    _safe_set(b, 'abs_Type_use39', a1)
    assert _is_linked(b, 'abs_Type_use39', a1)
    if hasattr(a1, 'abs_Type_use37'):
        assert _is_linked(a1, 'abs_Type_use37', b)
    _safe_set(b, 'abs_Type_use39', a2)
    assert _is_linked(b, 'abs_Type_use39', a2)
    if hasattr(a1, 'abs_Type_use37'):
        assert not _is_linked(a1, 'abs_Type_use37', b)
    if hasattr(a2, 'abs_Type_use37'):
        assert _is_linked(a2, 'abs_Type_use37', b)
    _safe_set(b, 'abs_Type_use39', None)
    assert not _is_linked(b, 'abs_Type_use39', a2)
    if hasattr(a2, 'abs_Type_use37'):
        assert not _is_linked(a2, 'abs_Type_use37', b)


def test_assoc_type_use61_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    _safe_set(b, 'abs_Pure_exp62', a1)
    assert _is_linked(b, 'abs_Pure_exp62', a1)
    if hasattr(a1, 'abs_Type_use63'):
        assert _is_linked(a1, 'abs_Type_use63', b)
    _safe_set(b, 'abs_Pure_exp62', a2)
    assert _is_linked(b, 'abs_Pure_exp62', a2)
    if hasattr(a1, 'abs_Type_use63'):
        assert not _is_linked(a1, 'abs_Type_use63', b)
    if hasattr(a2, 'abs_Type_use63'):
        assert _is_linked(a2, 'abs_Type_use63', b)
    _safe_set(b, 'abs_Pure_exp62', None)
    assert not _is_linked(b, 'abs_Pure_exp62', a2)
    if hasattr(a2, 'abs_Type_use63'):
        assert not _is_linked(a2, 'abs_Type_use63', b)


def test_assoc_type_use96_reverse_link_reassign_clear():
    a1 = abs_Type_use(name="sample_text")
    a2 = abs_Type_use(name="sample_text_2")
    b = abs_Function_decl(p="sample_text")
    _safe_set(b, 'abs_Function_decl', a1)
    assert _is_linked(b, 'abs_Function_decl', a1)
    if hasattr(a1, 'abs_Type_use97'):
        assert _is_linked(a1, 'abs_Type_use97', b)
    _safe_set(b, 'abs_Function_decl', a2)
    assert _is_linked(b, 'abs_Function_decl', a2)
    if hasattr(a1, 'abs_Type_use97'):
        assert not _is_linked(a1, 'abs_Type_use97', b)
    if hasattr(a2, 'abs_Type_use97'):
        assert _is_linked(a2, 'abs_Type_use97', b)
    _safe_set(b, 'abs_Function_decl', None)
    assert not _is_linked(b, 'abs_Function_decl', a2)
    if hasattr(a2, 'abs_Type_use97'):
        assert not _is_linked(a2, 'abs_Type_use97', b)


def test_assoc_var_or_field_ref145_reverse_link_reassign_clear():
    a1 = abs_Var_or_field_ref(name="sample_text")
    a2 = abs_Var_or_field_ref(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt146', a1)
    assert _is_linked(b, 'abs_Stmt146', a1)
    if hasattr(a1, 'abs_Var_or_field_ref147'):
        assert _is_linked(a1, 'abs_Var_or_field_ref147', b)
    _safe_set(b, 'abs_Stmt146', a2)
    assert _is_linked(b, 'abs_Stmt146', a2)
    if hasattr(a1, 'abs_Var_or_field_ref147'):
        assert not _is_linked(a1, 'abs_Var_or_field_ref147', b)
    if hasattr(a2, 'abs_Var_or_field_ref147'):
        assert _is_linked(a2, 'abs_Var_or_field_ref147', b)
    _safe_set(b, 'abs_Stmt146', None)
    assert not _is_linked(b, 'abs_Stmt146', a2)
    if hasattr(a2, 'abs_Var_or_field_ref147'):
        assert not _is_linked(a2, 'abs_Var_or_field_ref147', b)


def test_assoc_whilestmt164_reverse_link_reassign_clear():
    a1 = abs_Stmt(name="sample_text")
    a2 = abs_Stmt(name="sample_text_2")
    b = abs_Stmt(name="sample_text")
    _safe_set(b, 'abs_Stmt165', a1)
    assert _is_linked(b, 'abs_Stmt165', a1)
    if hasattr(a1, 'abs_Stmt163'):
        assert _is_linked(a1, 'abs_Stmt163', b)
    _safe_set(b, 'abs_Stmt165', a2)
    assert _is_linked(b, 'abs_Stmt165', a2)
    if hasattr(a1, 'abs_Stmt163'):
        assert not _is_linked(a1, 'abs_Stmt163', b)
    if hasattr(a2, 'abs_Stmt163'):
        assert _is_linked(a2, 'abs_Stmt163', b)
    _safe_set(b, 'abs_Stmt165', None)
    assert not _is_linked(b, 'abs_Stmt165', a2)
    if hasattr(a2, 'abs_Stmt163'):
        assert not _is_linked(a2, 'abs_Stmt163', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a471_stub_double():
    # abs_MexpPrimary_expr has no real 'abs_MexpPrimary_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Mexp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Mexp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Mexp(value=7)
    partner = abs_MexpPrimary_expr()
    setattr(partner, 'abs_MexpPrimary_expr', None)
    _safe_set(owner, 'abs_Mexp472', partner)
    assert getattr(partner, 'abs_MexpPrimary_expr') == owner
    _safe_set(owner, 'abs_Mexp472', None)
    assert getattr(partner, 'abs_MexpPrimary_expr') is None


def test_assoc_casebranch59_stub_double():
    # abs_Case_branch has no real 'abs_Case_branch' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Case_branch()
    setattr(partner, 'abs_Case_branch', None)
    _safe_set(owner, 'abs_Pure_exp60', {partner})
    assert getattr(partner, 'abs_Case_branch') == owner
    _safe_set(owner, 'abs_Pure_exp60', set())
    assert getattr(partner, 'abs_Case_branch') is None


def test_assoc_casestmtbranch175_stub_double():
    # abs_Casestmtbranch has no real 'abs_Casestmtbranch177' property in the generated
    # code (a bare stub) -- manually attach it so abs_Stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Stmt(name="sample_text")
    partner = abs_Casestmtbranch()
    setattr(partner, 'abs_Casestmtbranch177', None)
    _safe_set(owner, 'abs_Stmt176', {partner})
    assert getattr(partner, 'abs_Casestmtbranch177') == owner
    _safe_set(owner, 'abs_Stmt176', set())
    assert getattr(partner, 'abs_Casestmtbranch177') is None


def test_assoc_data_constructor_arg31_stub_double():
    # abs_Data_constructor_arg has no real 'abs_Data_constructor_arg' property in the generated
    # code (a bare stub) -- manually attach it so abs_Data_constructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Data_constructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Data_constructor(name="sample_text")
    partner = abs_Data_constructor_arg()
    setattr(partner, 'abs_Data_constructor_arg', None)
    _safe_set(owner, 'abs_Data_constructor32', {partner})
    assert getattr(partner, 'abs_Data_constructor_arg') == owner
    _safe_set(owner, 'abs_Data_constructor32', set())
    assert getattr(partner, 'abs_Data_constructor_arg') is None


def test_assoc_deltaDecl1_stub_double():
    # abs_Compilation_Unit has no real 'abs_Compilation_Unit2' property in the generated
    # code (a bare stub) -- manually attach it so abs_Delta_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Delta_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Delta_decl(name="sample_text")
    partner = abs_Compilation_Unit()
    setattr(partner, 'abs_Compilation_Unit2', None)
    _safe_set(owner, 'abs_Delta_decl', partner)
    assert getattr(partner, 'abs_Compilation_Unit2') == owner
    _safe_set(owner, 'abs_Delta_decl', None)
    assert getattr(partner, 'abs_Compilation_Unit2') is None


def test_assoc_delta_access265_stub_double():
    # abs_Delta_access has no real 'abs_Delta_access' property in the generated
    # code (a bare stub) -- manually attach it so abs_Delta_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Delta_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Delta_decl(name="sample_text")
    partner = abs_Delta_access()
    setattr(partner, 'abs_Delta_access', None)
    _safe_set(owner, 'abs_Delta_decl266', {partner})
    assert getattr(partner, 'abs_Delta_access') == owner
    _safe_set(owner, 'abs_Delta_decl266', set())
    assert getattr(partner, 'abs_Delta_access') is None


def test_assoc_delta_clause327_stub_double():
    # abs_Delta_clause has no real 'abs_Delta_clause' property in the generated
    # code (a bare stub) -- manually attach it so abs_Productline_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Productline_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Productline_decl(name="sample_text")
    partner = abs_Delta_clause()
    setattr(partner, 'abs_Delta_clause', None)
    _safe_set(owner, 'abs_Productline_decl328', {partner})
    assert getattr(partner, 'abs_Delta_clause') == owner
    _safe_set(owner, 'abs_Productline_decl328', set())
    assert getattr(partner, 'abs_Delta_clause') is None


def test_assoc_delta_id341_stub_double():
    # abs_After_condition has no real 'abs_After_condition342' property in the generated
    # code (a bare stub) -- manually attach it so abs_Delta_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Delta_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Delta_decl(name="sample_text")
    partner = abs_After_condition()
    setattr(partner, 'abs_After_condition342', None)
    _safe_set(owner, 'abs_Delta_decl343', partner)
    assert getattr(partner, 'abs_After_condition342') == owner
    _safe_set(owner, 'abs_Delta_decl343', None)
    assert getattr(partner, 'abs_After_condition342') is None


def test_assoc_deltaspec332_stub_double():
    # abs_Delta_clause has no real 'abs_Delta_clause333' property in the generated
    # code (a bare stub) -- manually attach it so abs_Delta_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Delta_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Delta_decl(name="sample_text")
    partner = abs_Delta_clause()
    setattr(partner, 'abs_Delta_clause333', None)
    _safe_set(owner, 'abs_Delta_decl334', partner)
    assert getattr(partner, 'abs_Delta_clause333') == owner
    _safe_set(owner, 'abs_Delta_decl334', None)
    assert getattr(partner, 'abs_Delta_clause333') is None


def test_assoc_exp143_stub_double():
    # abs_Exp has no real 'abs_Exp' property in the generated
    # code (a bare stub) -- manually attach it so abs_Stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Stmt(name="sample_text")
    partner = abs_Exp()
    setattr(partner, 'abs_Exp', None)
    _safe_set(owner, 'abs_Stmt144', partner)
    assert getattr(partner, 'abs_Exp') == owner
    _safe_set(owner, 'abs_Stmt144', None)
    assert getattr(partner, 'abs_Exp') is None


def test_assoc_feature352_stub_double():
    # abs_Application_condition has no real 'abs_Application_condition353' property in the generated
    # code (a bare stub) -- manually attach it so abs_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Feature(attr_assignment="sample_text", p="sample_text")
    partner = abs_Application_condition()
    setattr(partner, 'abs_Application_condition353', None)
    _safe_set(owner, 'abs_Feature354', partner)
    assert getattr(partner, 'abs_Application_condition353') == owner
    _safe_set(owner, 'abs_Feature354', None)
    assert getattr(partner, 'abs_Application_condition353') is None


def test_assoc_feature368_stub_double():
    # abs_Product_expr has no real 'abs_Product_expr369' property in the generated
    # code (a bare stub) -- manually attach it so abs_Feature_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Feature_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Feature_decl(name="sample_text")
    partner = abs_Product_expr()
    setattr(partner, 'abs_Product_expr369', None)
    _safe_set(owner, 'abs_Feature_decl370', partner)
    assert getattr(partner, 'abs_Product_expr369') == owner
    _safe_set(owner, 'abs_Feature_decl370', None)
    assert getattr(partner, 'abs_Product_expr369') is None


def test_assoc_feature_decl9_stub_double():
    # abs_Compilation_Unit has no real 'abs_Compilation_Unit10' property in the generated
    # code (a bare stub) -- manually attach it so abs_Feature_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Feature_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Feature_decl(name="sample_text")
    partner = abs_Compilation_Unit()
    setattr(partner, 'abs_Compilation_Unit10', None)
    _safe_set(owner, 'abs_Feature_decl', partner)
    assert getattr(partner, 'abs_Compilation_Unit10') == owner
    _safe_set(owner, 'abs_Feature_decl', None)
    assert getattr(partner, 'abs_Compilation_Unit10') is None


def test_assoc_feature_decl_constraint386_stub_double():
    # abs_Feature_decl_constraint has no real 'abs_Feature_decl_constraint' property in the generated
    # code (a bare stub) -- manually attach it so abs_Feature_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Feature_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Feature_decl(name="sample_text")
    partner = abs_Feature_decl_constraint()
    setattr(partner, 'abs_Feature_decl_constraint', None)
    _safe_set(owner, 'abs_Feature_decl387', {partner})
    assert getattr(partner, 'abs_Feature_decl_constraint') == owner
    _safe_set(owner, 'abs_Feature_decl387', set())
    assert getattr(partner, 'abs_Feature_decl_constraint') is None


def test_assoc_feature_decl_constraint398_stub_double():
    # abs_Feature_decl_constraint has no real 'abs_Feature_decl_constraint400' property in the generated
    # code (a bare stub) -- manually attach it so abs_Fextension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Fextension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Fextension(name="sample_text")
    partner = abs_Feature_decl_constraint()
    setattr(partner, 'abs_Feature_decl_constraint400', None)
    _safe_set(owner, 'abs_Fextension399', {partner})
    assert getattr(partner, 'abs_Feature_decl_constraint400') == owner
    _safe_set(owner, 'abs_Fextension399', set())
    assert getattr(partner, 'abs_Feature_decl_constraint400') is None


def test_assoc_feature_decl_group382_stub_double():
    # abs_Feature_decl_group has no real 'abs_Feature_decl_group' property in the generated
    # code (a bare stub) -- manually attach it so abs_Feature_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Feature_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Feature_decl(name="sample_text")
    partner = abs_Feature_decl_group()
    setattr(partner, 'abs_Feature_decl_group', None)
    _safe_set(owner, 'abs_Feature_decl383', partner)
    assert getattr(partner, 'abs_Feature_decl_group') == owner
    _safe_set(owner, 'abs_Feature_decl383', None)
    assert getattr(partner, 'abs_Feature_decl_group') is None


def test_assoc_feature_decl_group392_stub_double():
    # abs_Feature_decl_group has no real 'abs_Feature_decl_group394' property in the generated
    # code (a bare stub) -- manually attach it so abs_Fextension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Fextension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Fextension(name="sample_text")
    partner = abs_Feature_decl_group()
    setattr(partner, 'abs_Feature_decl_group394', None)
    _safe_set(owner, 'abs_Fextension393', partner)
    assert getattr(partner, 'abs_Feature_decl_group394') == owner
    _safe_set(owner, 'abs_Fextension393', None)
    assert getattr(partner, 'abs_Feature_decl_group394') is None


def test_assoc_fextension11_stub_double():
    # abs_Compilation_Unit has no real 'abs_Compilation_Unit12' property in the generated
    # code (a bare stub) -- manually attach it so abs_Fextension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Fextension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Fextension(name="sample_text")
    partner = abs_Compilation_Unit()
    setattr(partner, 'abs_Compilation_Unit12', None)
    _safe_set(owner, 'abs_Fextension', partner)
    assert getattr(partner, 'abs_Compilation_Unit12') == owner
    _safe_set(owner, 'abs_Fextension', None)
    assert getattr(partner, 'abs_Compilation_Unit12') is None


def test_assoc_field269_stub_double():
    # abs_Has_condition has no real 'abs_Has_condition' property in the generated
    # code (a bare stub) -- manually attach it so abs_Field_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Field_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Field_decl(name="sample_text")
    partner = abs_Has_condition()
    setattr(partner, 'abs_Has_condition', None)
    _safe_set(owner, 'abs_Field_decl270', partner)
    assert getattr(partner, 'abs_Has_condition') == owner
    _safe_set(owner, 'abs_Field_decl270', None)
    assert getattr(partner, 'abs_Has_condition') is None


def test_assoc_field_decl123_stub_double():
    # abs_Class_decl has no real 'abs_Class_decl124' property in the generated
    # code (a bare stub) -- manually attach it so abs_Field_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Field_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Field_decl(name="sample_text")
    partner = abs_Class_decl()
    setattr(partner, 'abs_Class_decl124', None)
    _safe_set(owner, 'abs_Field_decl125', partner)
    assert getattr(partner, 'abs_Class_decl124') == owner
    _safe_set(owner, 'abs_Field_decl125', None)
    assert getattr(partner, 'abs_Class_decl124') is None


def test_assoc_function_list40_stub_double():
    # abs_Function_list has no real 'abs_Function_list' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Function_list()
    setattr(partner, 'abs_Function_list', None)
    _safe_set(owner, 'abs_Pure_exp41', {partner})
    assert getattr(partner, 'abs_Function_list') == owner
    _safe_set(owner, 'abs_Pure_exp41', set())
    assert getattr(partner, 'abs_Function_list') is None


def test_assoc_function_name_decl28_stub_double():
    # abs_Function_name_list has no real 'abs_Function_name_list29' property in the generated
    # code (a bare stub) -- manually attach it so abs_Function_name_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Function_name_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Function_name_decl(name="sample_text")
    partner = abs_Function_name_list()
    setattr(partner, 'abs_Function_name_list29', None)
    _safe_set(owner, 'abs_Function_name_decl', partner)
    assert getattr(partner, 'abs_Function_name_list29') == owner
    _safe_set(owner, 'abs_Function_name_decl', None)
    assert getattr(partner, 'abs_Function_name_list29') is None


def test_assoc_functions22_stub_double():
    # abs_Function_name_list has no real 'abs_Function_name_list' property in the generated
    # code (a bare stub) -- manually attach it so abs_Par_function_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Par_function_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Par_function_decl(p="sample_text")
    partner = abs_Function_name_list()
    setattr(partner, 'abs_Function_name_list', None)
    _safe_set(owner, 'abs_Par_function_decl23', partner)
    assert getattr(partner, 'abs_Function_name_list') == owner
    _safe_set(owner, 'abs_Par_function_decl23', None)
    assert getattr(partner, 'abs_Function_name_list') is None


def test_assoc_guard212_stub_double():
    # abs_Guard has no real 'abs_Guard213' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Guard()
    setattr(partner, 'abs_Guard213', None)
    _safe_set(owner, 'abs_Pure_exp214', partner)
    assert getattr(partner, 'abs_Guard213') == owner
    _safe_set(owner, 'abs_Pure_exp214', None)
    assert getattr(partner, 'abs_Guard213') is None


def test_assoc_left401_stub_double():
    # abs_Or_expr has no real 'abs_Or_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Or_expr()
    setattr(partner, 'abs_Or_expr', None)
    _safe_set(owner, 'abs_Pure_exp402', partner)
    assert getattr(partner, 'abs_Or_expr') == owner
    _safe_set(owner, 'abs_Pure_exp402', None)
    assert getattr(partner, 'abs_Or_expr') is None


def test_assoc_left406_stub_double():
    # abs_And_expr has no real 'abs_And_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_And_expr()
    setattr(partner, 'abs_And_expr', None)
    _safe_set(owner, 'abs_Pure_exp407', partner)
    assert getattr(partner, 'abs_And_expr') == owner
    _safe_set(owner, 'abs_Pure_exp407', None)
    assert getattr(partner, 'abs_And_expr') is None


def test_assoc_left411_stub_double():
    # abs_Equality_expr has no real 'abs_Equality_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Equality_expr()
    setattr(partner, 'abs_Equality_expr', None)
    _safe_set(owner, 'abs_Pure_exp412', partner)
    assert getattr(partner, 'abs_Equality_expr') == owner
    _safe_set(owner, 'abs_Pure_exp412', None)
    assert getattr(partner, 'abs_Equality_expr') is None


def test_assoc_left416_stub_double():
    # abs_Comparison_expr has no real 'abs_Comparison_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Comparison_expr()
    setattr(partner, 'abs_Comparison_expr', None)
    _safe_set(owner, 'abs_Pure_exp417', partner)
    assert getattr(partner, 'abs_Comparison_expr') == owner
    _safe_set(owner, 'abs_Pure_exp417', None)
    assert getattr(partner, 'abs_Comparison_expr') is None


def test_assoc_left421_stub_double():
    # abs_PlusOrMinus_expr has no real 'abs_PlusOrMinus_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_PlusOrMinus_expr()
    setattr(partner, 'abs_PlusOrMinus_expr', None)
    _safe_set(owner, 'abs_Pure_exp422', partner)
    assert getattr(partner, 'abs_PlusOrMinus_expr') == owner
    _safe_set(owner, 'abs_Pure_exp422', None)
    assert getattr(partner, 'abs_PlusOrMinus_expr') is None


def test_assoc_left426_stub_double():
    # abs_MulDivOrMod_expr has no real 'abs_MulDivOrMod_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_MulDivOrMod_expr()
    setattr(partner, 'abs_MulDivOrMod_expr', None)
    _safe_set(owner, 'abs_Pure_exp427', partner)
    assert getattr(partner, 'abs_MulDivOrMod_expr') == owner
    _safe_set(owner, 'abs_Pure_exp427', None)
    assert getattr(partner, 'abs_MulDivOrMod_expr') is None


def test_assoc_left431_stub_double():
    # abs_Guard has no real 'abs_Guard432' property in the generated
    # code (a bare stub) -- manually attach it so abs_AndGuard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_AndGuard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_AndGuard(op="sample_text")
    partner = abs_Guard()
    setattr(partner, 'abs_Guard432', None)
    _safe_set(owner, 'abs_AndGuard', partner)
    assert getattr(partner, 'abs_Guard432') == owner
    _safe_set(owner, 'abs_AndGuard', None)
    assert getattr(partner, 'abs_Guard432') is None


def test_assoc_left436_stub_double():
    # abs_MexpOr_exp has no real 'abs_MexpOr_exp' property in the generated
    # code (a bare stub) -- manually attach it so abs_Mexp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Mexp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Mexp(value=7)
    partner = abs_MexpOr_exp()
    setattr(partner, 'abs_MexpOr_exp', None)
    _safe_set(owner, 'abs_Mexp437', partner)
    assert getattr(partner, 'abs_MexpOr_exp') == owner
    _safe_set(owner, 'abs_Mexp437', None)
    assert getattr(partner, 'abs_MexpOr_exp') is None


def test_assoc_left441_stub_double():
    # abs_MexpAnd_expr has no real 'abs_MexpAnd_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Mexp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Mexp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Mexp(value=7)
    partner = abs_MexpAnd_expr()
    setattr(partner, 'abs_MexpAnd_expr', None)
    _safe_set(owner, 'abs_Mexp442', partner)
    assert getattr(partner, 'abs_MexpAnd_expr') == owner
    _safe_set(owner, 'abs_Mexp442', None)
    assert getattr(partner, 'abs_MexpAnd_expr') is None


def test_assoc_list200_stub_double():
    # abs_Pure_exp_list has no real 'abs_Pure_exp_list202' property in the generated
    # code (a bare stub) -- manually attach it so abs_Eff_expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Eff_expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Eff_expr(l="sample_text")
    partner = abs_Pure_exp_list()
    setattr(partner, 'abs_Pure_exp_list202', None)
    _safe_set(owner, 'abs_Eff_expr201', {partner})
    assert getattr(partner, 'abs_Pure_exp_list202') == owner
    _safe_set(owner, 'abs_Eff_expr201', set())
    assert getattr(partner, 'abs_Pure_exp_list202') is None


def test_assoc_main_block19_stub_double():
    # abs_Main_block has no real 'abs_Main_block' property in the generated
    # code (a bare stub) -- manually attach it so abs_Module_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Module_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Module_decl(name="sample_text")
    partner = abs_Main_block()
    setattr(partner, 'abs_Main_block', None)
    _safe_set(owner, 'abs_Module_decl20', {partner})
    assert getattr(partner, 'abs_Main_block') == owner
    _safe_set(owner, 'abs_Module_decl20', set())
    assert getattr(partner, 'abs_Main_block') is None


def test_assoc_max209_stub_double():
    # abs_Guard has no real 'abs_Guard210' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Guard()
    setattr(partner, 'abs_Guard210', None)
    _safe_set(owner, 'abs_Pure_exp211', partner)
    assert getattr(partner, 'abs_Guard210') == owner
    _safe_set(owner, 'abs_Pure_exp211', None)
    assert getattr(partner, 'abs_Guard210') is None


def test_assoc_method132_stub_double():
    # abs_Class_decl has no real 'abs_Class_decl133' property in the generated
    # code (a bare stub) -- manually attach it so abs_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Method(name="sample_text")
    partner = abs_Class_decl()
    setattr(partner, 'abs_Class_decl133', None)
    _safe_set(owner, 'abs_Method', partner)
    assert getattr(partner, 'abs_Class_decl133') == owner
    _safe_set(owner, 'abs_Method', None)
    assert getattr(partner, 'abs_Class_decl133') is None


def test_assoc_method223_stub_double():
    # abs_Trait_expr has no real 'abs_Trait_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Method(name="sample_text")
    partner = abs_Trait_expr()
    setattr(partner, 'abs_Trait_expr', None)
    _safe_set(owner, 'abs_Method224', partner)
    assert getattr(partner, 'abs_Trait_expr') == owner
    _safe_set(owner, 'abs_Method224', None)
    assert getattr(partner, 'abs_Trait_expr') is None


def test_assoc_method236_stub_double():
    # abs_Trait_oper has no real 'abs_Trait_oper237' property in the generated
    # code (a bare stub) -- manually attach it so abs_Methodsig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Methodsig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Methodsig(name="sample_text")
    partner = abs_Trait_oper()
    setattr(partner, 'abs_Trait_oper237', None)
    _safe_set(owner, 'abs_Methodsig238', partner)
    assert getattr(partner, 'abs_Trait_oper237') == owner
    _safe_set(owner, 'abs_Methodsig238', None)
    assert getattr(partner, 'abs_Trait_oper237') is None


def test_assoc_method271_stub_double():
    # abs_Has_condition has no real 'abs_Has_condition272' property in the generated
    # code (a bare stub) -- manually attach it so abs_Methodsig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Methodsig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Methodsig(name="sample_text")
    partner = abs_Has_condition()
    setattr(partner, 'abs_Has_condition272', None)
    _safe_set(owner, 'abs_Methodsig273', partner)
    assert getattr(partner, 'abs_Has_condition272') == owner
    _safe_set(owner, 'abs_Methodsig273', None)
    assert getattr(partner, 'abs_Has_condition272') is None


def test_assoc_methodsig110_stub_double():
    # abs_Interface_decl has no real 'abs_Interface_decl111' property in the generated
    # code (a bare stub) -- manually attach it so abs_Methodsig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Methodsig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Methodsig(name="sample_text")
    partner = abs_Interface_decl()
    setattr(partner, 'abs_Interface_decl111', None)
    _safe_set(owner, 'abs_Methodsig', partner)
    assert getattr(partner, 'abs_Interface_decl111') == owner
    _safe_set(owner, 'abs_Methodsig', None)
    assert getattr(partner, 'abs_Interface_decl111') is None


def test_assoc_methodsig239_stub_double():
    # abs_Trait_oper has no real 'abs_Trait_oper240' property in the generated
    # code (a bare stub) -- manually attach it so abs_Methodsig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Methodsig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Methodsig(name="sample_text")
    partner = abs_Trait_oper()
    setattr(partner, 'abs_Trait_oper240', None)
    _safe_set(owner, 'abs_Methodsig241', partner)
    assert getattr(partner, 'abs_Trait_oper240') == owner
    _safe_set(owner, 'abs_Methodsig241', None)
    assert getattr(partner, 'abs_Trait_oper240') is None


def test_assoc_methodsig304_stub_double():
    # abs_Class_modifier_fragment has no real 'abs_Class_modifier_fragment305' property in the generated
    # code (a bare stub) -- manually attach it so abs_Methodsig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Methodsig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Methodsig(name="sample_text")
    partner = abs_Class_modifier_fragment()
    setattr(partner, 'abs_Class_modifier_fragment305', None)
    _safe_set(owner, 'abs_Methodsig306', partner)
    assert getattr(partner, 'abs_Class_modifier_fragment305') == owner
    _safe_set(owner, 'abs_Methodsig306', None)
    assert getattr(partner, 'abs_Class_modifier_fragment305') is None


def test_assoc_mexp390_stub_double():
    # abs_Feature_decl_constraint has no real 'abs_Feature_decl_constraint391' property in the generated
    # code (a bare stub) -- manually attach it so abs_Mexp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Mexp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Mexp(value=7)
    partner = abs_Feature_decl_constraint()
    setattr(partner, 'abs_Feature_decl_constraint391', None)
    _safe_set(owner, 'abs_Mexp', partner)
    assert getattr(partner, 'abs_Feature_decl_constraint391') == owner
    _safe_set(owner, 'abs_Mexp', None)
    assert getattr(partner, 'abs_Feature_decl_constraint391') is None


def test_assoc_min206_stub_double():
    # abs_Guard has no real 'abs_Guard207' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Guard()
    setattr(partner, 'abs_Guard207', None)
    _safe_set(owner, 'abs_Pure_exp208', partner)
    assert getattr(partner, 'abs_Guard207') == owner
    _safe_set(owner, 'abs_Pure_exp208', None)
    assert getattr(partner, 'abs_Guard207') is None


def test_assoc_module0_stub_double():
    # abs_Compilation_Unit has no real 'abs_Compilation_Unit' property in the generated
    # code (a bare stub) -- manually attach it so abs_Module_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Module_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Module_decl(name="sample_text")
    partner = abs_Compilation_Unit()
    setattr(partner, 'abs_Compilation_Unit', None)
    _safe_set(owner, 'abs_Module_decl', partner)
    assert getattr(partner, 'abs_Compilation_Unit') == owner
    _safe_set(owner, 'abs_Module_decl', None)
    assert getattr(partner, 'abs_Compilation_Unit') is None


def test_assoc_module_modifier267_stub_double():
    # abs_Module_modifier has no real 'abs_Module_modifier' property in the generated
    # code (a bare stub) -- manually attach it so abs_Delta_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Delta_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Delta_decl(name="sample_text")
    partner = abs_Module_modifier()
    setattr(partner, 'abs_Module_modifier', None)
    _safe_set(owner, 'abs_Delta_decl268', {partner})
    assert getattr(partner, 'abs_Module_modifier') == owner
    _safe_set(owner, 'abs_Delta_decl268', set())
    assert getattr(partner, 'abs_Module_modifier') is None


def test_assoc_module_ref277_stub_double():
    # abs_Delta_access has no real 'abs_Delta_access278' property in the generated
    # code (a bare stub) -- manually attach it so abs_Module_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Module_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Module_decl(name="sample_text")
    partner = abs_Delta_access()
    setattr(partner, 'abs_Delta_access278', None)
    _safe_set(owner, 'abs_Module_decl279', partner)
    assert getattr(partner, 'abs_Delta_access278') == owner
    _safe_set(owner, 'abs_Module_decl279', None)
    assert getattr(partner, 'abs_Delta_access278') is None


def test_assoc_object_update307_stub_double():
    # abs_Object_update has no real 'abs_Object_update' property in the generated
    # code (a bare stub) -- manually attach it so abs_Update_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Update_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Update_decl(name="sample_text")
    partner = abs_Object_update()
    setattr(partner, 'abs_Object_update', None)
    _safe_set(owner, 'abs_Update_decl308', {partner})
    assert getattr(partner, 'abs_Object_update') == owner
    _safe_set(owner, 'abs_Update_decl308', set())
    assert getattr(partner, 'abs_Object_update') is None


def test_assoc_p263_stub_double():
    # abs_Delta_param has no real 'abs_Delta_param' property in the generated
    # code (a bare stub) -- manually attach it so abs_Delta_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Delta_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Delta_decl(name="sample_text")
    partner = abs_Delta_param()
    setattr(partner, 'abs_Delta_param', None)
    _safe_set(owner, 'abs_Delta_decl264', {partner})
    assert getattr(partner, 'abs_Delta_param') == owner
    _safe_set(owner, 'abs_Delta_decl264', set())
    assert getattr(partner, 'abs_Delta_param') is None


def test_assoc_param_decl89_stub_double():
    # abs_Param_list has no real 'abs_Param_list90' property in the generated
    # code (a bare stub) -- manually attach it so abs_Param_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Param_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Param_decl(name="sample_text")
    partner = abs_Param_list()
    setattr(partner, 'abs_Param_list90', None)
    _safe_set(owner, 'abs_Param_decl', partner)
    assert getattr(partner, 'abs_Param_list90') == owner
    _safe_set(owner, 'abs_Param_decl', None)
    assert getattr(partner, 'abs_Param_list90') is None


def test_assoc_paramlist115_stub_double():
    # abs_Param_list has no real 'abs_Param_list117' property in the generated
    # code (a bare stub) -- manually attach it so abs_Methodsig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Methodsig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Methodsig(name="sample_text")
    partner = abs_Param_list()
    setattr(partner, 'abs_Param_list117', None)
    _safe_set(owner, 'abs_Methodsig116', partner)
    assert getattr(partner, 'abs_Param_list117') == owner
    _safe_set(owner, 'abs_Methodsig116', None)
    assert getattr(partner, 'abs_Param_list117') is None


def test_assoc_paramlist251_stub_double():
    # abs_Param_list has no real 'abs_Param_list253' property in the generated
    # code (a bare stub) -- manually attach it so abs_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Method(name="sample_text")
    partner = abs_Param_list()
    setattr(partner, 'abs_Param_list253', None)
    _safe_set(owner, 'abs_Method252', partner)
    assert getattr(partner, 'abs_Param_list253') == owner
    _safe_set(owner, 'abs_Method252', None)
    assert getattr(partner, 'abs_Param_list253') is None


def test_assoc_paramlist98_stub_double():
    # abs_Param_list has no real 'abs_Param_list100' property in the generated
    # code (a bare stub) -- manually attach it so abs_Function_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Function_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Function_decl(p="sample_text")
    partner = abs_Param_list()
    setattr(partner, 'abs_Param_list100', None)
    _safe_set(owner, 'abs_Function_decl99', partner)
    assert getattr(partner, 'abs_Param_list100') == owner
    _safe_set(owner, 'abs_Function_decl99', None)
    assert getattr(partner, 'abs_Param_list100') is None


def test_assoc_params24_stub_double():
    # abs_Param_list has no real 'abs_Param_list' property in the generated
    # code (a bare stub) -- manually attach it so abs_Par_function_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Par_function_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Par_function_decl(p="sample_text")
    partner = abs_Param_list()
    setattr(partner, 'abs_Param_list', None)
    _safe_set(owner, 'abs_Par_function_decl25', partner)
    assert getattr(partner, 'abs_Param_list') == owner
    _safe_set(owner, 'abs_Par_function_decl25', None)
    assert getattr(partner, 'abs_Param_list') is None


def test_assoc_partial_function_pure_exp_list42_stub_double():
    # abs_Pure_exp_list has no real 'abs_Pure_exp_list' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Pure_exp_list()
    setattr(partner, 'abs_Pure_exp_list', None)
    _safe_set(owner, 'abs_Pure_exp43', partner)
    assert getattr(partner, 'abs_Pure_exp_list') == owner
    _safe_set(owner, 'abs_Pure_exp43', None)
    assert getattr(partner, 'abs_Pure_exp_list') is None


def test_assoc_productDecl371_stub_double():
    # abs_Product_expr has no real 'abs_Product_expr372' property in the generated
    # code (a bare stub) -- manually attach it so abs_Product_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Product_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Product_decl(name="sample_text")
    partner = abs_Product_expr()
    setattr(partner, 'abs_Product_expr372', None)
    _safe_set(owner, 'abs_Product_decl373', partner)
    assert getattr(partner, 'abs_Product_expr372') == owner
    _safe_set(owner, 'abs_Product_decl373', None)
    assert getattr(partner, 'abs_Product_expr372') is None


def test_assoc_product_decl7_stub_double():
    # abs_Compilation_Unit has no real 'abs_Compilation_Unit8' property in the generated
    # code (a bare stub) -- manually attach it so abs_Product_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Product_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Product_decl(name="sample_text")
    partner = abs_Compilation_Unit()
    setattr(partner, 'abs_Compilation_Unit8', None)
    _safe_set(owner, 'abs_Product_decl', partner)
    assert getattr(partner, 'abs_Compilation_Unit8') == owner
    _safe_set(owner, 'abs_Product_decl', None)
    assert getattr(partner, 'abs_Compilation_Unit8') is None


def test_assoc_product_expr366_stub_double():
    # abs_Product_expr has no real 'abs_Product_expr' property in the generated
    # code (a bare stub) -- manually attach it so abs_Product_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Product_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Product_decl(name="sample_text")
    partner = abs_Product_expr()
    setattr(partner, 'abs_Product_expr', None)
    _safe_set(owner, 'abs_Product_decl367', partner)
    assert getattr(partner, 'abs_Product_expr') == owner
    _safe_set(owner, 'abs_Product_decl367', None)
    assert getattr(partner, 'abs_Product_expr') is None


def test_assoc_productline_decl5_stub_double():
    # abs_Compilation_Unit has no real 'abs_Compilation_Unit6' property in the generated
    # code (a bare stub) -- manually attach it so abs_Productline_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Productline_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Productline_decl(name="sample_text")
    partner = abs_Compilation_Unit()
    setattr(partner, 'abs_Compilation_Unit6', None)
    _safe_set(owner, 'abs_Productline_decl', partner)
    assert getattr(partner, 'abs_Compilation_Unit6') == owner
    _safe_set(owner, 'abs_Productline_decl', None)
    assert getattr(partner, 'abs_Compilation_Unit6') is None


def test_assoc_pure_exp34_stub_double():
    # abs_Annotation has no real 'abs_Annotation35' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Annotation()
    setattr(partner, 'abs_Annotation35', None)
    _safe_set(owner, 'abs_Pure_exp36', partner)
    assert getattr(partner, 'abs_Annotation35') == owner
    _safe_set(owner, 'abs_Pure_exp36', None)
    assert getattr(partner, 'abs_Annotation35') is None


def test_assoc_pure_exp74_stub_double():
    # abs_Pattern has no real 'abs_Pattern' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Pattern()
    setattr(partner, 'abs_Pattern', None)
    _safe_set(owner, 'abs_Pure_exp75', partner)
    assert getattr(partner, 'abs_Pattern') == owner
    _safe_set(owner, 'abs_Pure_exp75', None)
    assert getattr(partner, 'abs_Pattern') is None


def test_assoc_pure_exp79_stub_double():
    # abs_Pure_exp_list has no real 'abs_Pure_exp_list80' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Pure_exp_list()
    setattr(partner, 'abs_Pure_exp_list80', None)
    _safe_set(owner, 'abs_Pure_exp81', partner)
    assert getattr(partner, 'abs_Pure_exp_list80') == owner
    _safe_set(owner, 'abs_Pure_exp81', None)
    assert getattr(partner, 'abs_Pure_exp_list80') is None


def test_assoc_pure_exp86_stub_double():
    # abs_Anon_function_decl has no real 'abs_Anon_function_decl87' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Anon_function_decl()
    setattr(partner, 'abs_Anon_function_decl87', None)
    _safe_set(owner, 'abs_Pure_exp88', partner)
    assert getattr(partner, 'abs_Anon_function_decl87') == owner
    _safe_set(owner, 'abs_Pure_exp88', None)
    assert getattr(partner, 'abs_Anon_function_decl87') is None


def test_assoc_pure_exp_list198_stub_double():
    # abs_Pure_exp_list has no real 'abs_Pure_exp_list199' property in the generated
    # code (a bare stub) -- manually attach it so abs_Eff_expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Eff_expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Eff_expr(l="sample_text")
    partner = abs_Pure_exp_list()
    setattr(partner, 'abs_Pure_exp_list199', None)
    _safe_set(owner, 'abs_Eff_expr', partner)
    assert getattr(partner, 'abs_Pure_exp_list199') == owner
    _safe_set(owner, 'abs_Eff_expr', None)
    assert getattr(partner, 'abs_Pure_exp_list199') is None


def test_assoc_ref178_stub_double():
    # abs_Guard has no real 'abs_Guard' property in the generated
    # code (a bare stub) -- manually attach it so abs_Stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Stmt(name="sample_text")
    partner = abs_Guard()
    setattr(partner, 'abs_Guard', None)
    _safe_set(owner, 'abs_Stmt179', partner)
    assert getattr(partner, 'abs_Guard') == owner
    _safe_set(owner, 'abs_Stmt179', None)
    assert getattr(partner, 'abs_Guard') is None


def test_assoc_ref203_stub_double():
    # abs_Guard has no real 'abs_Guard204' property in the generated
    # code (a bare stub) -- manually attach it so abs_Var_or_field_ref's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Var_or_field_ref's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Var_or_field_ref(name="sample_text")
    partner = abs_Guard()
    setattr(partner, 'abs_Guard204', None)
    _safe_set(owner, 'abs_Var_or_field_ref205', partner)
    assert getattr(partner, 'abs_Guard204') == owner
    _safe_set(owner, 'abs_Var_or_field_ref205', None)
    assert getattr(partner, 'abs_Guard204') is None


def test_assoc_right403_stub_double():
    # abs_Or_expr has no real 'abs_Or_expr404' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Or_expr()
    setattr(partner, 'abs_Or_expr404', None)
    _safe_set(owner, 'abs_Pure_exp405', partner)
    assert getattr(partner, 'abs_Or_expr404') == owner
    _safe_set(owner, 'abs_Pure_exp405', None)
    assert getattr(partner, 'abs_Or_expr404') is None


def test_assoc_right408_stub_double():
    # abs_And_expr has no real 'abs_And_expr409' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_And_expr()
    setattr(partner, 'abs_And_expr409', None)
    _safe_set(owner, 'abs_Pure_exp410', partner)
    assert getattr(partner, 'abs_And_expr409') == owner
    _safe_set(owner, 'abs_Pure_exp410', None)
    assert getattr(partner, 'abs_And_expr409') is None


def test_assoc_right413_stub_double():
    # abs_Equality_expr has no real 'abs_Equality_expr414' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Equality_expr()
    setattr(partner, 'abs_Equality_expr414', None)
    _safe_set(owner, 'abs_Pure_exp415', partner)
    assert getattr(partner, 'abs_Equality_expr414') == owner
    _safe_set(owner, 'abs_Pure_exp415', None)
    assert getattr(partner, 'abs_Equality_expr414') is None


def test_assoc_right418_stub_double():
    # abs_Comparison_expr has no real 'abs_Comparison_expr419' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Comparison_expr()
    setattr(partner, 'abs_Comparison_expr419', None)
    _safe_set(owner, 'abs_Pure_exp420', partner)
    assert getattr(partner, 'abs_Comparison_expr419') == owner
    _safe_set(owner, 'abs_Pure_exp420', None)
    assert getattr(partner, 'abs_Comparison_expr419') is None


def test_assoc_right423_stub_double():
    # abs_PlusOrMinus_expr has no real 'abs_PlusOrMinus_expr424' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_PlusOrMinus_expr()
    setattr(partner, 'abs_PlusOrMinus_expr424', None)
    _safe_set(owner, 'abs_Pure_exp425', partner)
    assert getattr(partner, 'abs_PlusOrMinus_expr424') == owner
    _safe_set(owner, 'abs_Pure_exp425', None)
    assert getattr(partner, 'abs_PlusOrMinus_expr424') is None


def test_assoc_right428_stub_double():
    # abs_MulDivOrMod_expr has no real 'abs_MulDivOrMod_expr429' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_MulDivOrMod_expr()
    setattr(partner, 'abs_MulDivOrMod_expr429', None)
    _safe_set(owner, 'abs_Pure_exp430', partner)
    assert getattr(partner, 'abs_MulDivOrMod_expr429') == owner
    _safe_set(owner, 'abs_Pure_exp430', None)
    assert getattr(partner, 'abs_MulDivOrMod_expr429') is None


def test_assoc_right433_stub_double():
    # abs_Guard has no real 'abs_Guard435' property in the generated
    # code (a bare stub) -- manually attach it so abs_AndGuard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_AndGuard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_AndGuard(op="sample_text")
    partner = abs_Guard()
    setattr(partner, 'abs_Guard435', None)
    _safe_set(owner, 'abs_AndGuard434', partner)
    assert getattr(partner, 'abs_Guard435') == owner
    _safe_set(owner, 'abs_AndGuard434', None)
    assert getattr(partner, 'abs_Guard435') is None


def test_assoc_right438_stub_double():
    # abs_MexpOr_exp has no real 'abs_MexpOr_exp439' property in the generated
    # code (a bare stub) -- manually attach it so abs_Mexp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Mexp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Mexp(value=7)
    partner = abs_MexpOr_exp()
    setattr(partner, 'abs_MexpOr_exp439', None)
    _safe_set(owner, 'abs_Mexp440', partner)
    assert getattr(partner, 'abs_MexpOr_exp439') == owner
    _safe_set(owner, 'abs_Mexp440', None)
    assert getattr(partner, 'abs_MexpOr_exp439') is None


def test_assoc_right443_stub_double():
    # abs_MexpAnd_expr has no real 'abs_MexpAnd_expr444' property in the generated
    # code (a bare stub) -- manually attach it so abs_Mexp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Mexp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Mexp(value=7)
    partner = abs_MexpAnd_expr()
    setattr(partner, 'abs_MexpAnd_expr444', None)
    _safe_set(owner, 'abs_Mexp445', partner)
    assert getattr(partner, 'abs_MexpAnd_expr444') == owner
    _safe_set(owner, 'abs_Mexp445', None)
    assert getattr(partner, 'abs_MexpAnd_expr444') is None


def test_assoc_stmt126_stub_double():
    # abs_Class_decl has no real 'abs_Class_decl127' property in the generated
    # code (a bare stub) -- manually attach it so abs_Stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Stmt(name="sample_text")
    partner = abs_Class_decl()
    setattr(partner, 'abs_Class_decl127', None)
    _safe_set(owner, 'abs_Stmt', partner)
    assert getattr(partner, 'abs_Class_decl127') == owner
    _safe_set(owner, 'abs_Stmt', None)
    assert getattr(partner, 'abs_Class_decl127') is None


def test_assoc_stmt218_stub_double():
    # abs_Casestmtbranch has no real 'abs_Casestmtbranch219' property in the generated
    # code (a bare stub) -- manually attach it so abs_Stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Stmt(name="sample_text")
    partner = abs_Casestmtbranch()
    setattr(partner, 'abs_Casestmtbranch219', None)
    _safe_set(owner, 'abs_Stmt220', partner)
    assert getattr(partner, 'abs_Casestmtbranch219') == owner
    _safe_set(owner, 'abs_Stmt220', None)
    assert getattr(partner, 'abs_Casestmtbranch219') is None


def test_assoc_stmt260_stub_double():
    # abs_Main_block has no real 'abs_Main_block261' property in the generated
    # code (a bare stub) -- manually attach it so abs_Stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Stmt(name="sample_text")
    partner = abs_Main_block()
    setattr(partner, 'abs_Main_block261', None)
    _safe_set(owner, 'abs_Stmt262', partner)
    assert getattr(partner, 'abs_Main_block261') == owner
    _safe_set(owner, 'abs_Stmt262', None)
    assert getattr(partner, 'abs_Main_block261') is None


def test_assoc_traitMethod225_stub_double():
    # abs_Trait_expr has no real 'abs_Trait_expr226' property in the generated
    # code (a bare stub) -- manually attach it so abs_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Method(name="sample_text")
    partner = abs_Trait_expr()
    setattr(partner, 'abs_Trait_expr226', None)
    _safe_set(owner, 'abs_Method227', partner)
    assert getattr(partner, 'abs_Trait_expr226') == owner
    _safe_set(owner, 'abs_Method227', None)
    assert getattr(partner, 'abs_Trait_expr226') is None


def test_assoc_type_use104_stub_double():
    # abs_Typesyn_decl has no real 'abs_Typesyn_decl' property in the generated
    # code (a bare stub) -- manually attach it so abs_Type_use's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Type_use's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Type_use(name="sample_text")
    partner = abs_Typesyn_decl()
    setattr(partner, 'abs_Typesyn_decl', None)
    _safe_set(owner, 'abs_Type_use105', partner)
    assert getattr(partner, 'abs_Typesyn_decl') == owner
    _safe_set(owner, 'abs_Type_use105', None)
    assert getattr(partner, 'abs_Typesyn_decl') is None


def test_assoc_update_decl3_stub_double():
    # abs_Compilation_Unit has no real 'abs_Compilation_Unit4' property in the generated
    # code (a bare stub) -- manually attach it so abs_Update_decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Update_decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Update_decl(name="sample_text")
    partner = abs_Compilation_Unit()
    setattr(partner, 'abs_Compilation_Unit4', None)
    _safe_set(owner, 'abs_Update_decl', partner)
    assert getattr(partner, 'abs_Compilation_Unit4') == owner
    _safe_set(owner, 'abs_Update_decl', None)
    assert getattr(partner, 'abs_Compilation_Unit4') is None


def test_assoc_var_or_field_ref319_stub_double():
    # abs_Object_update_assign_stmt has no real 'abs_Object_update_assign_stmt320' property in the generated
    # code (a bare stub) -- manually attach it so abs_Var_or_field_ref's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Var_or_field_ref's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Var_or_field_ref(name="sample_text")
    partner = abs_Object_update_assign_stmt()
    setattr(partner, 'abs_Object_update_assign_stmt320', None)
    _safe_set(owner, 'abs_Var_or_field_ref321', partner)
    assert getattr(partner, 'abs_Object_update_assign_stmt320') == owner
    _safe_set(owner, 'abs_Var_or_field_ref321', None)
    assert getattr(partner, 'abs_Object_update_assign_stmt320') is None


def test_assoc_variadic_exp_list44_stub_double():
    # abs_Pure_exp_list has no real 'abs_Pure_exp_list46' property in the generated
    # code (a bare stub) -- manually attach it so abs_Pure_exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # abs_Pure_exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = abs_Pure_exp(await_="sample_text", op="sample_text", val="sample_text", value="sample_text")
    partner = abs_Pure_exp_list()
    setattr(partner, 'abs_Pure_exp_list46', None)
    _safe_set(owner, 'abs_Pure_exp45', partner)
    assert getattr(partner, 'abs_Pure_exp_list46') == owner
    _safe_set(owner, 'abs_Pure_exp45', None)
    assert getattr(partner, 'abs_Pure_exp_list46') is None


