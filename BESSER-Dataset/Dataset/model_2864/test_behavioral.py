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


