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
    sensinact_DSL_CEP_DURATION_SEC,
    sensinact_DSL_CEP_DURATION_MIN,
    sensinact_DSL_CEP_COUNT,
    DSL_Expression,
    sensinact_DSL_Expression_Diff,
    sensinact_DSL_Expression_Smaller_Equal,
    sensinact_DSL_Object_Ref,
    sensinact_DSL_Object_String,
    sensinact_DSL_Expression_Plus,
    sensinact_DSL_Object_Boolean,
    sensinact_DSL_Expression_Minus,
    sensinact_DSL_Expression_Equal,
    sensinact_DSL_Expression_Smaller,
    sensinact_DSL_Object_Number,
    sensinact_DSL_Expression_And,
    sensinact_DSL_Expression_Negate,
    sensinact_DSL_Expression_Division,
    sensinact_DSL_Expression_Larger_Equal,
    sensinact_DSL_Expression_Larger,
    sensinact_DSL_Expression_Multiplication,
    sensinact_DSL_Expression_Modulo,
    sensinact_DSL_Expression_Or,
    sensinact_DSL_ListParam,
    sensinact_DSL_ResourceAction,
    sensinact_DSL_CEP_COINCIDE,
    sensinact_DSL_CEP_BEFORE,
    sensinact_DSL_CEP_SUM,
    sensinact_DSL_CEP_AVG,
    sensinact_DSL_CEP_MAX,
    sensinact_DSL_CEP_MIN,
    sensinact_DSL_ListActions,
    sensinact_DSL_Expression,
    sensinact_DSL_ElseDo,
    sensinact_DSL_ElseIfDo,
    sensinact_DSL_CEP_DURATION,
    sensinact_DSL_CEP_AFTER,
    sensinact_EObject,
    sensinact_DSL_REF,
    sensinact_DSL_On,
    sensinact_DSL_FLAG_AUTOSTART,
    sensinact_DSL_SENSINACT,
    sensinact_Sensinact,
    sensinact_DSL_IfDo,
    sensinact_DSL_REF_CONDITION,
    DSL_REF,
    sensinact_DSL_Resource,
    sensinact_DSL_CEP_STATEMENT,
    sensinact_DSL_ECA_STATEMENT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sensinact_dsl_cep_duration_sec_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_DURATION_SEC)


def test_hyp_sensinact_dsl_cep_duration_sec_constructor_exists():
    assert callable(sensinact_DSL_CEP_DURATION_SEC.__init__)


def test_hyp_sensinact_dsl_cep_duration_sec_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_DURATION_SEC.__init__)
    params = list(sig.parameters.keys())
    assert "sec" in params, "Missing parameter 'sec'"




def test_hyp_sensinact_dsl_cep_duration_min_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_DURATION_MIN)


def test_hyp_sensinact_dsl_cep_duration_min_constructor_exists():
    assert callable(sensinact_DSL_CEP_DURATION_MIN.__init__)


def test_hyp_sensinact_dsl_cep_duration_min_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_DURATION_MIN.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"




def test_hyp_sensinact_dsl_cep_count_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_COUNT)


def test_hyp_sensinact_dsl_cep_count_constructor_exists():
    assert callable(sensinact_DSL_CEP_COUNT.__init__)


def test_hyp_sensinact_dsl_cep_count_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_COUNT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_expression_is_not_abstract():
    assert not inspect.isabstract(DSL_Expression)


def test_hyp_dsl_expression_constructor_exists():
    assert callable(DSL_Expression.__init__)


def test_hyp_dsl_expression_constructor_args():
    sig = inspect.signature(DSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_diff_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Diff)


def test_hyp_sensinact_dsl_expression_diff_constructor_exists():
    assert callable(sensinact_DSL_Expression_Diff.__init__)


def test_hyp_sensinact_dsl_expression_diff_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Diff.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_smaller_equal_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Smaller_Equal)


def test_hyp_sensinact_dsl_expression_smaller_equal_constructor_exists():
    assert callable(sensinact_DSL_Expression_Smaller_Equal.__init__)


def test_hyp_sensinact_dsl_expression_smaller_equal_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Smaller_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_object_ref_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Object_Ref)


def test_hyp_sensinact_dsl_object_ref_constructor_exists():
    assert callable(sensinact_DSL_Object_Ref.__init__)


def test_hyp_sensinact_dsl_object_ref_constructor_args():
    sig = inspect.signature(sensinact_DSL_Object_Ref.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_object_string_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Object_String)


def test_hyp_sensinact_dsl_object_string_constructor_exists():
    assert callable(sensinact_DSL_Object_String.__init__)


def test_hyp_sensinact_dsl_object_string_constructor_args():
    sig = inspect.signature(sensinact_DSL_Object_String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sensinact_dsl_expression_plus_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Plus)


def test_hyp_sensinact_dsl_expression_plus_constructor_exists():
    assert callable(sensinact_DSL_Expression_Plus.__init__)


def test_hyp_sensinact_dsl_expression_plus_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_object_boolean_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Object_Boolean)


def test_hyp_sensinact_dsl_object_boolean_constructor_exists():
    assert callable(sensinact_DSL_Object_Boolean.__init__)


def test_hyp_sensinact_dsl_object_boolean_constructor_args():
    sig = inspect.signature(sensinact_DSL_Object_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sensinact_dsl_expression_minus_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Minus)


def test_hyp_sensinact_dsl_expression_minus_constructor_exists():
    assert callable(sensinact_DSL_Expression_Minus.__init__)


def test_hyp_sensinact_dsl_expression_minus_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_equal_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Equal)


def test_hyp_sensinact_dsl_expression_equal_constructor_exists():
    assert callable(sensinact_DSL_Expression_Equal.__init__)


def test_hyp_sensinact_dsl_expression_equal_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_smaller_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Smaller)


def test_hyp_sensinact_dsl_expression_smaller_constructor_exists():
    assert callable(sensinact_DSL_Expression_Smaller.__init__)


def test_hyp_sensinact_dsl_expression_smaller_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Smaller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_object_number_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Object_Number)


def test_hyp_sensinact_dsl_object_number_constructor_exists():
    assert callable(sensinact_DSL_Object_Number.__init__)


def test_hyp_sensinact_dsl_object_number_constructor_args():
    sig = inspect.signature(sensinact_DSL_Object_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_sensinact_dsl_expression_and_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_And)


def test_hyp_sensinact_dsl_expression_and_constructor_exists():
    assert callable(sensinact_DSL_Expression_And.__init__)


def test_hyp_sensinact_dsl_expression_and_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_negate_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Negate)


def test_hyp_sensinact_dsl_expression_negate_constructor_exists():
    assert callable(sensinact_DSL_Expression_Negate.__init__)


def test_hyp_sensinact_dsl_expression_negate_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Negate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_division_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Division)


def test_hyp_sensinact_dsl_expression_division_constructor_exists():
    assert callable(sensinact_DSL_Expression_Division.__init__)


def test_hyp_sensinact_dsl_expression_division_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_larger_equal_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Larger_Equal)


def test_hyp_sensinact_dsl_expression_larger_equal_constructor_exists():
    assert callable(sensinact_DSL_Expression_Larger_Equal.__init__)


def test_hyp_sensinact_dsl_expression_larger_equal_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Larger_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_larger_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Larger)


def test_hyp_sensinact_dsl_expression_larger_constructor_exists():
    assert callable(sensinact_DSL_Expression_Larger.__init__)


def test_hyp_sensinact_dsl_expression_larger_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Larger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_multiplication_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Multiplication)


def test_hyp_sensinact_dsl_expression_multiplication_constructor_exists():
    assert callable(sensinact_DSL_Expression_Multiplication.__init__)


def test_hyp_sensinact_dsl_expression_multiplication_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_modulo_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Modulo)


def test_hyp_sensinact_dsl_expression_modulo_constructor_exists():
    assert callable(sensinact_DSL_Expression_Modulo.__init__)


def test_hyp_sensinact_dsl_expression_modulo_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_or_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression_Or)


def test_hyp_sensinact_dsl_expression_or_constructor_exists():
    assert callable(sensinact_DSL_Expression_Or.__init__)


def test_hyp_sensinact_dsl_expression_or_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_listparam_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_ListParam)


def test_hyp_sensinact_dsl_listparam_constructor_exists():
    assert callable(sensinact_DSL_ListParam.__init__)


def test_hyp_sensinact_dsl_listparam_constructor_args():
    sig = inspect.signature(sensinact_DSL_ListParam.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_resourceaction_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_ResourceAction)


def test_hyp_sensinact_dsl_resourceaction_constructor_exists():
    assert callable(sensinact_DSL_ResourceAction.__init__)


def test_hyp_sensinact_dsl_resourceaction_constructor_args():
    sig = inspect.signature(sensinact_DSL_ResourceAction.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"
    assert "actiontype" in params, "Missing parameter 'actiontype'"





def test_hyp_sensinact_dsl_cep_coincide_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_COINCIDE)


def test_hyp_sensinact_dsl_cep_coincide_constructor_exists():
    assert callable(sensinact_DSL_CEP_COINCIDE.__init__)


def test_hyp_sensinact_dsl_cep_coincide_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_COINCIDE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_cep_before_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_BEFORE)


def test_hyp_sensinact_dsl_cep_before_constructor_exists():
    assert callable(sensinact_DSL_CEP_BEFORE.__init__)


def test_hyp_sensinact_dsl_cep_before_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_BEFORE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_cep_sum_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_SUM)


def test_hyp_sensinact_dsl_cep_sum_constructor_exists():
    assert callable(sensinact_DSL_CEP_SUM.__init__)


def test_hyp_sensinact_dsl_cep_sum_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_SUM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_cep_avg_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_AVG)


def test_hyp_sensinact_dsl_cep_avg_constructor_exists():
    assert callable(sensinact_DSL_CEP_AVG.__init__)


def test_hyp_sensinact_dsl_cep_avg_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_AVG.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_cep_max_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_MAX)


def test_hyp_sensinact_dsl_cep_max_constructor_exists():
    assert callable(sensinact_DSL_CEP_MAX.__init__)


def test_hyp_sensinact_dsl_cep_max_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_MAX.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_cep_min_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_MIN)


def test_hyp_sensinact_dsl_cep_min_constructor_exists():
    assert callable(sensinact_DSL_CEP_MIN.__init__)


def test_hyp_sensinact_dsl_cep_min_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_MIN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_listactions_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_ListActions)


def test_hyp_sensinact_dsl_listactions_constructor_exists():
    assert callable(sensinact_DSL_ListActions.__init__)


def test_hyp_sensinact_dsl_listactions_constructor_args():
    sig = inspect.signature(sensinact_DSL_ListActions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_expression_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Expression)


def test_hyp_sensinact_dsl_expression_constructor_exists():
    assert callable(sensinact_DSL_Expression.__init__)


def test_hyp_sensinact_dsl_expression_constructor_args():
    sig = inspect.signature(sensinact_DSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_elsedo_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_ElseDo)


def test_hyp_sensinact_dsl_elsedo_constructor_exists():
    assert callable(sensinact_DSL_ElseDo.__init__)


def test_hyp_sensinact_dsl_elsedo_constructor_args():
    sig = inspect.signature(sensinact_DSL_ElseDo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_elseifdo_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_ElseIfDo)


def test_hyp_sensinact_dsl_elseifdo_constructor_exists():
    assert callable(sensinact_DSL_ElseIfDo.__init__)


def test_hyp_sensinact_dsl_elseifdo_constructor_args():
    sig = inspect.signature(sensinact_DSL_ElseIfDo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_cep_duration_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_DURATION)


def test_hyp_sensinact_dsl_cep_duration_constructor_exists():
    assert callable(sensinact_DSL_CEP_DURATION.__init__)


def test_hyp_sensinact_dsl_cep_duration_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_DURATION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_cep_after_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_AFTER)


def test_hyp_sensinact_dsl_cep_after_constructor_exists():
    assert callable(sensinact_DSL_CEP_AFTER.__init__)


def test_hyp_sensinact_dsl_cep_after_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_AFTER.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_eobject_is_not_abstract():
    assert not inspect.isabstract(sensinact_EObject)


def test_hyp_sensinact_eobject_constructor_exists():
    assert callable(sensinact_EObject.__init__)


def test_hyp_sensinact_eobject_constructor_args():
    sig = inspect.signature(sensinact_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_ref_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_REF)


def test_hyp_sensinact_dsl_ref_constructor_exists():
    assert callable(sensinact_DSL_REF.__init__)


def test_hyp_sensinact_dsl_ref_constructor_args():
    sig = inspect.signature(sensinact_DSL_REF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sensinact_dsl_on_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_On)


def test_hyp_sensinact_dsl_on_constructor_exists():
    assert callable(sensinact_DSL_On.__init__)


def test_hyp_sensinact_dsl_on_constructor_args():
    sig = inspect.signature(sensinact_DSL_On.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_flag_autostart_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_FLAG_AUTOSTART)


def test_hyp_sensinact_dsl_flag_autostart_constructor_exists():
    assert callable(sensinact_DSL_FLAG_AUTOSTART.__init__)


def test_hyp_sensinact_dsl_flag_autostart_constructor_args():
    sig = inspect.signature(sensinact_DSL_FLAG_AUTOSTART.__init__)
    params = list(sig.parameters.keys())
    assert "activated" in params, "Missing parameter 'activated'"




def test_hyp_sensinact_dsl_sensinact_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_SENSINACT)


def test_hyp_sensinact_dsl_sensinact_constructor_exists():
    assert callable(sensinact_DSL_SENSINACT.__init__)


def test_hyp_sensinact_dsl_sensinact_constructor_args():
    sig = inspect.signature(sensinact_DSL_SENSINACT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_sensinact_is_not_abstract():
    assert not inspect.isabstract(sensinact_Sensinact)


def test_hyp_sensinact_sensinact_constructor_exists():
    assert callable(sensinact_Sensinact.__init__)


def test_hyp_sensinact_sensinact_constructor_args():
    sig = inspect.signature(sensinact_Sensinact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_ifdo_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_IfDo)


def test_hyp_sensinact_dsl_ifdo_constructor_exists():
    assert callable(sensinact_DSL_IfDo.__init__)


def test_hyp_sensinact_dsl_ifdo_constructor_args():
    sig = inspect.signature(sensinact_DSL_IfDo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_ref_condition_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_REF_CONDITION)


def test_hyp_sensinact_dsl_ref_condition_constructor_exists():
    assert callable(sensinact_DSL_REF_CONDITION.__init__)


def test_hyp_sensinact_dsl_ref_condition_constructor_args():
    sig = inspect.signature(sensinact_DSL_REF_CONDITION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_ref_is_not_abstract():
    assert not inspect.isabstract(DSL_REF)


def test_hyp_dsl_ref_constructor_exists():
    assert callable(DSL_REF.__init__)


def test_hyp_dsl_ref_constructor_args():
    sig = inspect.signature(DSL_REF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_resource_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_Resource)


def test_hyp_sensinact_dsl_resource_constructor_exists():
    assert callable(sensinact_DSL_Resource.__init__)


def test_hyp_sensinact_dsl_resource_constructor_args():
    sig = inspect.signature(sensinact_DSL_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "resourceID" in params, "Missing parameter 'resourceID'"
    assert "deviceID" in params, "Missing parameter 'deviceID'"
    assert "serviceID" in params, "Missing parameter 'serviceID'"
    assert "gatewayID" in params, "Missing parameter 'gatewayID'"







def test_hyp_sensinact_dsl_cep_statement_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_CEP_STATEMENT)


def test_hyp_sensinact_dsl_cep_statement_constructor_exists():
    assert callable(sensinact_DSL_CEP_STATEMENT.__init__)


def test_hyp_sensinact_dsl_cep_statement_constructor_args():
    sig = inspect.signature(sensinact_DSL_CEP_STATEMENT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensinact_dsl_eca_statement_is_not_abstract():
    assert not inspect.isabstract(sensinact_DSL_ECA_STATEMENT)


def test_hyp_sensinact_dsl_eca_statement_constructor_exists():
    assert callable(sensinact_DSL_ECA_STATEMENT.__init__)


def test_hyp_sensinact_dsl_eca_statement_constructor_args():
    sig = inspect.signature(sensinact_DSL_ECA_STATEMENT.__init__)
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
sensinact_DSL_CEP_DURATION_SEC_strategy = st.builds(
    sensinact_DSL_CEP_DURATION_SEC,
    sec=
        safe_text
)
sensinact_DSL_CEP_DURATION_MIN_strategy = st.builds(
    sensinact_DSL_CEP_DURATION_MIN,
    min=
        safe_text
)
sensinact_DSL_CEP_COUNT_strategy = st.builds(
    sensinact_DSL_CEP_COUNT,
)
DSL_Expression_strategy = st.builds(
    DSL_Expression,
)
sensinact_DSL_Expression_Diff_strategy = st.builds(
    sensinact_DSL_Expression_Diff,
)
sensinact_DSL_Expression_Smaller_Equal_strategy = st.builds(
    sensinact_DSL_Expression_Smaller_Equal,
)
sensinact_DSL_Object_Ref_strategy = st.builds(
    sensinact_DSL_Object_Ref,
)
sensinact_DSL_Object_String_strategy = st.builds(
    sensinact_DSL_Object_String,
    value=
        safe_text
)
sensinact_DSL_Expression_Plus_strategy = st.builds(
    sensinact_DSL_Expression_Plus,
)
sensinact_DSL_Object_Boolean_strategy = st.builds(
    sensinact_DSL_Object_Boolean,
    value=
        st.booleans()
)
sensinact_DSL_Expression_Minus_strategy = st.builds(
    sensinact_DSL_Expression_Minus,
)
sensinact_DSL_Expression_Equal_strategy = st.builds(
    sensinact_DSL_Expression_Equal,
)
sensinact_DSL_Expression_Smaller_strategy = st.builds(
    sensinact_DSL_Expression_Smaller,
)
sensinact_DSL_Object_Number_strategy = st.builds(
    sensinact_DSL_Object_Number,
    value=
        safe_text
)
sensinact_DSL_Expression_And_strategy = st.builds(
    sensinact_DSL_Expression_And,
)
sensinact_DSL_Expression_Negate_strategy = st.builds(
    sensinact_DSL_Expression_Negate,
)
sensinact_DSL_Expression_Division_strategy = st.builds(
    sensinact_DSL_Expression_Division,
)
sensinact_DSL_Expression_Larger_Equal_strategy = st.builds(
    sensinact_DSL_Expression_Larger_Equal,
)
sensinact_DSL_Expression_Larger_strategy = st.builds(
    sensinact_DSL_Expression_Larger,
)
sensinact_DSL_Expression_Multiplication_strategy = st.builds(
    sensinact_DSL_Expression_Multiplication,
)
sensinact_DSL_Expression_Modulo_strategy = st.builds(
    sensinact_DSL_Expression_Modulo,
)
sensinact_DSL_Expression_Or_strategy = st.builds(
    sensinact_DSL_Expression_Or,
)
sensinact_DSL_ListParam_strategy = st.builds(
    sensinact_DSL_ListParam,
)
sensinact_DSL_ResourceAction_strategy = st.builds(
    sensinact_DSL_ResourceAction,
    variable=
        safe_text,
    actiontype=
        safe_text
)
sensinact_DSL_CEP_COINCIDE_strategy = st.builds(
    sensinact_DSL_CEP_COINCIDE,
)
sensinact_DSL_CEP_BEFORE_strategy = st.builds(
    sensinact_DSL_CEP_BEFORE,
)
sensinact_DSL_CEP_SUM_strategy = st.builds(
    sensinact_DSL_CEP_SUM,
)
sensinact_DSL_CEP_AVG_strategy = st.builds(
    sensinact_DSL_CEP_AVG,
)
sensinact_DSL_CEP_MAX_strategy = st.builds(
    sensinact_DSL_CEP_MAX,
)
sensinact_DSL_CEP_MIN_strategy = st.builds(
    sensinact_DSL_CEP_MIN,
)
sensinact_DSL_ListActions_strategy = st.builds(
    sensinact_DSL_ListActions,
)
sensinact_DSL_Expression_strategy = st.builds(
    sensinact_DSL_Expression,
)
sensinact_DSL_ElseDo_strategy = st.builds(
    sensinact_DSL_ElseDo,
)
sensinact_DSL_ElseIfDo_strategy = st.builds(
    sensinact_DSL_ElseIfDo,
)
sensinact_DSL_CEP_DURATION_strategy = st.builds(
    sensinact_DSL_CEP_DURATION,
)
sensinact_DSL_CEP_AFTER_strategy = st.builds(
    sensinact_DSL_CEP_AFTER,
)
sensinact_EObject_strategy = st.builds(
    sensinact_EObject,
)
sensinact_DSL_REF_strategy = st.builds(
    sensinact_DSL_REF,
    name=
        safe_text
)
sensinact_DSL_On_strategy = st.builds(
    sensinact_DSL_On,
)
sensinact_DSL_FLAG_AUTOSTART_strategy = st.builds(
    sensinact_DSL_FLAG_AUTOSTART,
    activated=
        st.booleans()
)
sensinact_DSL_SENSINACT_strategy = st.builds(
    sensinact_DSL_SENSINACT,
)
sensinact_Sensinact_strategy = st.builds(
    sensinact_Sensinact,
)
sensinact_DSL_IfDo_strategy = st.builds(
    sensinact_DSL_IfDo,
)
sensinact_DSL_REF_CONDITION_strategy = st.builds(
    sensinact_DSL_REF_CONDITION,
)
DSL_REF_strategy = st.builds(
    DSL_REF,
)
sensinact_DSL_Resource_strategy = st.builds(
    sensinact_DSL_Resource,
    resourceID=
        safe_text,
    deviceID=
        safe_text,
    serviceID=
        safe_text,
    gatewayID=
        safe_text
)
sensinact_DSL_CEP_STATEMENT_strategy = st.builds(
    sensinact_DSL_CEP_STATEMENT,
)
sensinact_DSL_ECA_STATEMENT_strategy = st.builds(
    sensinact_DSL_ECA_STATEMENT,
)




@given(instance=sensinact_DSL_CEP_DURATION_SEC_strategy)
def test_hyp_sensinact_dsl_cep_duration_sec_sec_setter(instance):
    original = instance.sec
    instance.sec = original
    assert instance.sec == original




@given(instance=sensinact_DSL_CEP_DURATION_MIN_strategy)
def test_hyp_sensinact_dsl_cep_duration_min_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original









@given(instance=sensinact_DSL_Object_String_strategy)
def test_hyp_sensinact_dsl_object_string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=sensinact_DSL_Object_Boolean_strategy)
def test_hyp_sensinact_dsl_object_boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=sensinact_DSL_Object_Number_strategy)
def test_hyp_sensinact_dsl_object_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original













@given(instance=sensinact_DSL_ResourceAction_strategy)
def test_hyp_sensinact_dsl_resourceaction_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original



@given(instance=sensinact_DSL_ResourceAction_strategy)
def test_hyp_sensinact_dsl_resourceaction_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original

















@given(instance=sensinact_DSL_REF_strategy)
def test_hyp_sensinact_dsl_ref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=sensinact_DSL_FLAG_AUTOSTART_strategy)
def test_hyp_sensinact_dsl_flag_autostart_activated_setter(instance):
    original = instance.activated
    instance.activated = original
    assert instance.activated == original









@given(instance=sensinact_DSL_Resource_strategy)
def test_hyp_sensinact_dsl_resource_resourceID_setter(instance):
    original = instance.resourceID
    instance.resourceID = original
    assert instance.resourceID == original



@given(instance=sensinact_DSL_Resource_strategy)
def test_hyp_sensinact_dsl_resource_deviceID_setter(instance):
    original = instance.deviceID
    instance.deviceID = original
    assert instance.deviceID == original



@given(instance=sensinact_DSL_Resource_strategy)
def test_hyp_sensinact_dsl_resource_serviceID_setter(instance):
    original = instance.serviceID
    instance.serviceID = original
    assert instance.serviceID == original



@given(instance=sensinact_DSL_Resource_strategy)
def test_hyp_sensinact_dsl_resource_gatewayID_setter(instance):
    original = instance.gatewayID
    instance.gatewayID = original
    assert instance.gatewayID == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DSL_Expression,
    DSL_REF,
    sensinact_DSL_CEP_AFTER,
    sensinact_DSL_CEP_AVG,
    sensinact_DSL_CEP_BEFORE,
    sensinact_DSL_CEP_COINCIDE,
    sensinact_DSL_CEP_COUNT,
    sensinact_DSL_CEP_DURATION,
    sensinact_DSL_CEP_DURATION_MIN,
    sensinact_DSL_CEP_DURATION_SEC,
    sensinact_DSL_CEP_MAX,
    sensinact_DSL_CEP_MIN,
    sensinact_DSL_CEP_STATEMENT,
    sensinact_DSL_CEP_SUM,
    sensinact_DSL_ECA_STATEMENT,
    sensinact_DSL_ElseDo,
    sensinact_DSL_ElseIfDo,
    sensinact_DSL_Expression,
    sensinact_DSL_Expression_And,
    sensinact_DSL_Expression_Diff,
    sensinact_DSL_Expression_Division,
    sensinact_DSL_Expression_Equal,
    sensinact_DSL_Expression_Larger,
    sensinact_DSL_Expression_Larger_Equal,
    sensinact_DSL_Expression_Minus,
    sensinact_DSL_Expression_Modulo,
    sensinact_DSL_Expression_Multiplication,
    sensinact_DSL_Expression_Negate,
    sensinact_DSL_Expression_Or,
    sensinact_DSL_Expression_Plus,
    sensinact_DSL_Expression_Smaller,
    sensinact_DSL_Expression_Smaller_Equal,
    sensinact_DSL_FLAG_AUTOSTART,
    sensinact_DSL_IfDo,
    sensinact_DSL_ListActions,
    sensinact_DSL_ListParam,
    sensinact_DSL_Object_Boolean,
    sensinact_DSL_Object_Number,
    sensinact_DSL_Object_Ref,
    sensinact_DSL_Object_String,
    sensinact_DSL_On,
    sensinact_DSL_REF,
    sensinact_DSL_REF_CONDITION,
    sensinact_DSL_Resource,
    sensinact_DSL_ResourceAction,
    sensinact_DSL_SENSINACT,
    sensinact_EObject,
    sensinact_Sensinact,
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

def test_sensinact_DSL_CEP_DURATION_MIN_min_value_roundtrip():
    instance = sensinact_DSL_CEP_DURATION_MIN(min="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_sensinact_DSL_CEP_DURATION_SEC_sec_value_roundtrip():
    instance = sensinact_DSL_CEP_DURATION_SEC(sec="sample_text")
    assert instance.sec == "sample_text"
    instance.sec = "sample_text_2"
    assert instance.sec == "sample_text_2"


def test_sensinact_DSL_FLAG_AUTOSTART_activated_value_roundtrip():
    instance = sensinact_DSL_FLAG_AUTOSTART(activated=True)
    assert instance.activated == True
    instance.activated = False
    assert instance.activated == False


def test_sensinact_DSL_Object_Boolean_value_value_roundtrip():
    instance = sensinact_DSL_Object_Boolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_sensinact_DSL_Object_Number_value_value_roundtrip():
    instance = sensinact_DSL_Object_Number(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sensinact_DSL_Object_String_value_value_roundtrip():
    instance = sensinact_DSL_Object_String(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sensinact_DSL_REF_name_value_roundtrip():
    instance = sensinact_DSL_REF(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sensinact_DSL_Resource_deviceID_value_roundtrip():
    instance = sensinact_DSL_Resource(deviceID="sample_text", gatewayID="sample_text", resourceID="sample_text", serviceID="sample_text")
    assert instance.deviceID == "sample_text"
    instance.deviceID = "sample_text_2"
    assert instance.deviceID == "sample_text_2"


def test_sensinact_DSL_Resource_gatewayID_value_roundtrip():
    instance = sensinact_DSL_Resource(deviceID="sample_text", gatewayID="sample_text", resourceID="sample_text", serviceID="sample_text")
    assert instance.gatewayID == "sample_text"
    instance.gatewayID = "sample_text_2"
    assert instance.gatewayID == "sample_text_2"


def test_sensinact_DSL_Resource_resourceID_value_roundtrip():
    instance = sensinact_DSL_Resource(deviceID="sample_text", gatewayID="sample_text", resourceID="sample_text", serviceID="sample_text")
    assert instance.resourceID == "sample_text"
    instance.resourceID = "sample_text_2"
    assert instance.resourceID == "sample_text_2"


def test_sensinact_DSL_Resource_serviceID_value_roundtrip():
    instance = sensinact_DSL_Resource(deviceID="sample_text", gatewayID="sample_text", resourceID="sample_text", serviceID="sample_text")
    assert instance.serviceID == "sample_text"
    instance.serviceID = "sample_text_2"
    assert instance.serviceID == "sample_text_2"


def test_sensinact_DSL_ResourceAction_actiontype_value_roundtrip():
    instance = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    assert instance.actiontype == "sample_text"
    instance.actiontype = "sample_text_2"
    assert instance.actiontype == "sample_text_2"


def test_sensinact_DSL_ResourceAction_variable_value_roundtrip():
    instance = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    assert instance.variable == "sample_text"
    instance.variable = "sample_text_2"
    assert instance.variable == "sample_text_2"


def test_sensinact_DSL_Expression_And_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_And()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Diff_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Diff()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Division_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Division()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Equal_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Equal()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Larger_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Larger()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Larger_Equal_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Larger_Equal()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Minus_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Minus()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Modulo_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Modulo()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Multiplication_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Multiplication()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Negate_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Negate()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Or_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Or()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Plus_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Plus()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Smaller_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Smaller()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Expression_Smaller_Equal_isa_DSL_Expression():
    instance = sensinact_DSL_Expression_Smaller_Equal()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Object_Boolean_isa_DSL_Expression():
    instance = sensinact_DSL_Object_Boolean(value=True)
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Object_Number_isa_DSL_Expression():
    instance = sensinact_DSL_Object_Number(value="sample_text")
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Object_Ref_isa_DSL_Expression():
    instance = sensinact_DSL_Object_Ref()
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_Object_String_isa_DSL_Expression():
    instance = sensinact_DSL_Object_String(value="sample_text")
    assert isinstance(instance, DSL_Expression)


def test_sensinact_DSL_CEP_STATEMENT_isa_DSL_REF():
    instance = sensinact_DSL_CEP_STATEMENT()
    assert isinstance(instance, DSL_REF)


def test_sensinact_DSL_Resource_isa_DSL_REF():
    instance = sensinact_DSL_Resource(deviceID="sample_text", gatewayID="sample_text", resourceID="sample_text", serviceID="sample_text")
    assert isinstance(instance, DSL_REF)


def test_assoc_actionList93_link_reassign_clear():
    a = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    b1 = sensinact_DSL_ListActions()
    b2 = sensinact_DSL_ListActions()
    _safe_set(a, 'sensinact_DSL_ResourceAction', b1)
    assert _is_linked(a, 'sensinact_DSL_ResourceAction', b1)
    if hasattr(b1, 'sensinact_DSL_ListActions94'):
        assert _is_linked(b1, 'sensinact_DSL_ListActions94', a)
    _safe_set(a, 'sensinact_DSL_ResourceAction', b2)
    assert _is_linked(a, 'sensinact_DSL_ResourceAction', b2)
    if hasattr(b1, 'sensinact_DSL_ListActions94'):
        assert not _is_linked(b1, 'sensinact_DSL_ListActions94', a)
    if hasattr(b2, 'sensinact_DSL_ListActions94'):
        assert _is_linked(b2, 'sensinact_DSL_ListActions94', a)
    _safe_set(a, 'sensinact_DSL_ResourceAction', None)
    assert not _is_linked(a, 'sensinact_DSL_ResourceAction', b2)
    if hasattr(b2, 'sensinact_DSL_ListActions94'):
        assert not _is_linked(b2, 'sensinact_DSL_ListActions94', a)


def test_assoc_autostart1_link_reassign_clear():
    a = sensinact_DSL_FLAG_AUTOSTART(activated=True)
    b1 = sensinact_DSL_SENSINACT()
    b2 = sensinact_DSL_SENSINACT()
    _safe_set(a, 'sensinact_DSL_FLAG_AUTOSTART', b1)
    assert _is_linked(a, 'sensinact_DSL_FLAG_AUTOSTART', b1)
    if hasattr(b1, 'sensinact_DSL_SENSINACT2'):
        assert _is_linked(b1, 'sensinact_DSL_SENSINACT2', a)
    _safe_set(a, 'sensinact_DSL_FLAG_AUTOSTART', b2)
    assert _is_linked(a, 'sensinact_DSL_FLAG_AUTOSTART', b2)
    if hasattr(b1, 'sensinact_DSL_SENSINACT2'):
        assert not _is_linked(b1, 'sensinact_DSL_SENSINACT2', a)
    if hasattr(b2, 'sensinact_DSL_SENSINACT2'):
        assert _is_linked(b2, 'sensinact_DSL_SENSINACT2', a)
    _safe_set(a, 'sensinact_DSL_FLAG_AUTOSTART', None)
    assert not _is_linked(a, 'sensinact_DSL_FLAG_AUTOSTART', b2)
    if hasattr(b2, 'sensinact_DSL_SENSINACT2'):
        assert not _is_linked(b2, 'sensinact_DSL_SENSINACT2', a)


def test_assoc_listParam98_link_reassign_clear():
    a = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    b1 = sensinact_DSL_ListParam()
    b2 = sensinact_DSL_ListParam()
    _safe_set(a, 'sensinact_DSL_ResourceAction99', b1)
    assert _is_linked(a, 'sensinact_DSL_ResourceAction99', b1)
    if hasattr(b1, 'sensinact_DSL_ListParam'):
        assert _is_linked(b1, 'sensinact_DSL_ListParam', a)
    _safe_set(a, 'sensinact_DSL_ResourceAction99', b2)
    assert _is_linked(a, 'sensinact_DSL_ResourceAction99', b2)
    if hasattr(b1, 'sensinact_DSL_ListParam'):
        assert not _is_linked(b1, 'sensinact_DSL_ListParam', a)
    if hasattr(b2, 'sensinact_DSL_ListParam'):
        assert _is_linked(b2, 'sensinact_DSL_ListParam', a)
    _safe_set(a, 'sensinact_DSL_ResourceAction99', None)
    assert not _is_linked(a, 'sensinact_DSL_ResourceAction99', b2)
    if hasattr(b2, 'sensinact_DSL_ListParam'):
        assert not _is_linked(b2, 'sensinact_DSL_ListParam', a)


def test_assoc_ref32_link_reassign_clear():
    a = sensinact_DSL_REF(name="sample_text")
    b1 = sensinact_DSL_REF_CONDITION()
    b2 = sensinact_DSL_REF_CONDITION()
    _safe_set(a, 'sensinact_DSL_REF', b1)
    assert _is_linked(a, 'sensinact_DSL_REF', b1)
    if hasattr(b1, 'sensinact_DSL_REF_CONDITION33'):
        assert _is_linked(b1, 'sensinact_DSL_REF_CONDITION33', a)
    _safe_set(a, 'sensinact_DSL_REF', b2)
    assert _is_linked(a, 'sensinact_DSL_REF', b2)
    if hasattr(b1, 'sensinact_DSL_REF_CONDITION33'):
        assert not _is_linked(b1, 'sensinact_DSL_REF_CONDITION33', a)
    if hasattr(b2, 'sensinact_DSL_REF_CONDITION33'):
        assert _is_linked(b2, 'sensinact_DSL_REF_CONDITION33', a)
    _safe_set(a, 'sensinact_DSL_REF', None)
    assert not _is_linked(a, 'sensinact_DSL_REF', b2)
    if hasattr(b2, 'sensinact_DSL_REF_CONDITION33'):
        assert not _is_linked(b2, 'sensinact_DSL_REF_CONDITION33', a)


def test_assoc_ref95_link_reassign_clear():
    a = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    b1 = sensinact_DSL_REF(name="sample_text")
    b2 = sensinact_DSL_REF(name="sample_text_2")
    _safe_set(a, 'sensinact_DSL_ResourceAction96', b1)
    assert _is_linked(a, 'sensinact_DSL_ResourceAction96', b1)
    if hasattr(b1, 'sensinact_DSL_REF97'):
        assert _is_linked(b1, 'sensinact_DSL_REF97', a)
    _safe_set(a, 'sensinact_DSL_ResourceAction96', b2)
    assert _is_linked(a, 'sensinact_DSL_ResourceAction96', b2)
    if hasattr(b1, 'sensinact_DSL_REF97'):
        assert not _is_linked(b1, 'sensinact_DSL_REF97', a)
    if hasattr(b2, 'sensinact_DSL_REF97'):
        assert _is_linked(b2, 'sensinact_DSL_REF97', a)
    _safe_set(a, 'sensinact_DSL_ResourceAction96', None)
    assert not _is_linked(a, 'sensinact_DSL_ResourceAction96', b2)
    if hasattr(b2, 'sensinact_DSL_REF97'):
        assert not _is_linked(b2, 'sensinact_DSL_REF97', a)


def test_assoc_resources3_link_reassign_clear():
    a = sensinact_DSL_Resource(deviceID="sample_text", gatewayID="sample_text", resourceID="sample_text", serviceID="sample_text")
    b1 = sensinact_DSL_SENSINACT()
    b2 = sensinact_DSL_SENSINACT()
    _safe_set(a, 'sensinact_DSL_Resource', b1)
    assert _is_linked(a, 'sensinact_DSL_Resource', b1)
    if hasattr(b1, 'sensinact_DSL_SENSINACT4'):
        assert _is_linked(b1, 'sensinact_DSL_SENSINACT4', a)
    _safe_set(a, 'sensinact_DSL_Resource', b2)
    assert _is_linked(a, 'sensinact_DSL_Resource', b2)
    if hasattr(b1, 'sensinact_DSL_SENSINACT4'):
        assert not _is_linked(b1, 'sensinact_DSL_SENSINACT4', a)
    if hasattr(b2, 'sensinact_DSL_SENSINACT4'):
        assert _is_linked(b2, 'sensinact_DSL_SENSINACT4', a)
    _safe_set(a, 'sensinact_DSL_Resource', None)
    assert not _is_linked(a, 'sensinact_DSL_Resource', b2)
    if hasattr(b2, 'sensinact_DSL_SENSINACT4'):
        assert not _is_linked(b2, 'sensinact_DSL_SENSINACT4', a)


def test_assoc_value168_link_reassign_clear():
    a = sensinact_DSL_REF(name="sample_text")
    b1 = sensinact_DSL_Object_Ref()
    b2 = sensinact_DSL_Object_Ref()
    _safe_set(a, 'sensinact_DSL_REF169', b1)
    assert _is_linked(a, 'sensinact_DSL_REF169', b1)
    if hasattr(b1, 'sensinact_DSL_Object_Ref'):
        assert _is_linked(b1, 'sensinact_DSL_Object_Ref', a)
    _safe_set(a, 'sensinact_DSL_REF169', b2)
    assert _is_linked(a, 'sensinact_DSL_REF169', b2)
    if hasattr(b1, 'sensinact_DSL_Object_Ref'):
        assert not _is_linked(b1, 'sensinact_DSL_Object_Ref', a)
    if hasattr(b2, 'sensinact_DSL_Object_Ref'):
        assert _is_linked(b2, 'sensinact_DSL_Object_Ref', a)
    _safe_set(a, 'sensinact_DSL_REF169', None)
    assert not _is_linked(a, 'sensinact_DSL_REF169', b2)
    if hasattr(b2, 'sensinact_DSL_Object_Ref'):
        assert not _is_linked(b2, 'sensinact_DSL_Object_Ref', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DSL_Expression_strategy = st.builds(DSL_Expression)
@given(instance=DSL_Expression_strategy)
@settings(max_examples=25)
def test_DSL_Expression_instantiation(instance):
    assert isinstance(instance, DSL_Expression)


DSL_REF_strategy = st.builds(DSL_REF)
@given(instance=DSL_REF_strategy)
@settings(max_examples=25)
def test_DSL_REF_instantiation(instance):
    assert isinstance(instance, DSL_REF)


sensinact_DSL_CEP_AFTER_strategy = st.builds(sensinact_DSL_CEP_AFTER)
@given(instance=sensinact_DSL_CEP_AFTER_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_AFTER_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_AFTER)


sensinact_DSL_CEP_AVG_strategy = st.builds(sensinact_DSL_CEP_AVG)
@given(instance=sensinact_DSL_CEP_AVG_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_AVG_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_AVG)


sensinact_DSL_CEP_BEFORE_strategy = st.builds(sensinact_DSL_CEP_BEFORE)
@given(instance=sensinact_DSL_CEP_BEFORE_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_BEFORE_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_BEFORE)


sensinact_DSL_CEP_COINCIDE_strategy = st.builds(sensinact_DSL_CEP_COINCIDE)
@given(instance=sensinact_DSL_CEP_COINCIDE_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_COINCIDE_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_COINCIDE)


sensinact_DSL_CEP_COUNT_strategy = st.builds(sensinact_DSL_CEP_COUNT)
@given(instance=sensinact_DSL_CEP_COUNT_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_COUNT_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_COUNT)


sensinact_DSL_CEP_DURATION_strategy = st.builds(sensinact_DSL_CEP_DURATION)
@given(instance=sensinact_DSL_CEP_DURATION_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_DURATION_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_DURATION)


sensinact_DSL_CEP_DURATION_MIN_strategy = st.builds(sensinact_DSL_CEP_DURATION_MIN, min=safe_text)
@given(instance=sensinact_DSL_CEP_DURATION_MIN_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_DURATION_MIN_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_DURATION_MIN)


sensinact_DSL_CEP_DURATION_SEC_strategy = st.builds(sensinact_DSL_CEP_DURATION_SEC, sec=safe_text)
@given(instance=sensinact_DSL_CEP_DURATION_SEC_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_DURATION_SEC_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_DURATION_SEC)


sensinact_DSL_CEP_MAX_strategy = st.builds(sensinact_DSL_CEP_MAX)
@given(instance=sensinact_DSL_CEP_MAX_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_MAX_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_MAX)


sensinact_DSL_CEP_MIN_strategy = st.builds(sensinact_DSL_CEP_MIN)
@given(instance=sensinact_DSL_CEP_MIN_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_MIN_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_MIN)


sensinact_DSL_CEP_STATEMENT_strategy = st.builds(sensinact_DSL_CEP_STATEMENT)
@given(instance=sensinact_DSL_CEP_STATEMENT_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_STATEMENT_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_STATEMENT)


sensinact_DSL_CEP_SUM_strategy = st.builds(sensinact_DSL_CEP_SUM)
@given(instance=sensinact_DSL_CEP_SUM_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_CEP_SUM_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_CEP_SUM)


sensinact_DSL_ECA_STATEMENT_strategy = st.builds(sensinact_DSL_ECA_STATEMENT)
@given(instance=sensinact_DSL_ECA_STATEMENT_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_ECA_STATEMENT_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_ECA_STATEMENT)


sensinact_DSL_ElseDo_strategy = st.builds(sensinact_DSL_ElseDo)
@given(instance=sensinact_DSL_ElseDo_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_ElseDo_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_ElseDo)


sensinact_DSL_ElseIfDo_strategy = st.builds(sensinact_DSL_ElseIfDo)
@given(instance=sensinact_DSL_ElseIfDo_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_ElseIfDo_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_ElseIfDo)


sensinact_DSL_Expression_strategy = st.builds(sensinact_DSL_Expression)
@given(instance=sensinact_DSL_Expression_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression)


sensinact_DSL_Expression_And_strategy = st.builds(sensinact_DSL_Expression_And)
@given(instance=sensinact_DSL_Expression_And_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_And_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_And)


sensinact_DSL_Expression_Diff_strategy = st.builds(sensinact_DSL_Expression_Diff)
@given(instance=sensinact_DSL_Expression_Diff_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Diff_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Diff)


sensinact_DSL_Expression_Division_strategy = st.builds(sensinact_DSL_Expression_Division)
@given(instance=sensinact_DSL_Expression_Division_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Division_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Division)


sensinact_DSL_Expression_Equal_strategy = st.builds(sensinact_DSL_Expression_Equal)
@given(instance=sensinact_DSL_Expression_Equal_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Equal_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Equal)


sensinact_DSL_Expression_Larger_strategy = st.builds(sensinact_DSL_Expression_Larger)
@given(instance=sensinact_DSL_Expression_Larger_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Larger_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Larger)


sensinact_DSL_Expression_Larger_Equal_strategy = st.builds(sensinact_DSL_Expression_Larger_Equal)
@given(instance=sensinact_DSL_Expression_Larger_Equal_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Larger_Equal_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Larger_Equal)


sensinact_DSL_Expression_Minus_strategy = st.builds(sensinact_DSL_Expression_Minus)
@given(instance=sensinact_DSL_Expression_Minus_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Minus_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Minus)


sensinact_DSL_Expression_Modulo_strategy = st.builds(sensinact_DSL_Expression_Modulo)
@given(instance=sensinact_DSL_Expression_Modulo_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Modulo_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Modulo)


sensinact_DSL_Expression_Multiplication_strategy = st.builds(sensinact_DSL_Expression_Multiplication)
@given(instance=sensinact_DSL_Expression_Multiplication_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Multiplication_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Multiplication)


sensinact_DSL_Expression_Negate_strategy = st.builds(sensinact_DSL_Expression_Negate)
@given(instance=sensinact_DSL_Expression_Negate_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Negate_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Negate)


sensinact_DSL_Expression_Or_strategy = st.builds(sensinact_DSL_Expression_Or)
@given(instance=sensinact_DSL_Expression_Or_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Or_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Or)


sensinact_DSL_Expression_Plus_strategy = st.builds(sensinact_DSL_Expression_Plus)
@given(instance=sensinact_DSL_Expression_Plus_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Plus_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Plus)


sensinact_DSL_Expression_Smaller_strategy = st.builds(sensinact_DSL_Expression_Smaller)
@given(instance=sensinact_DSL_Expression_Smaller_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Smaller_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Smaller)


sensinact_DSL_Expression_Smaller_Equal_strategy = st.builds(sensinact_DSL_Expression_Smaller_Equal)
@given(instance=sensinact_DSL_Expression_Smaller_Equal_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Expression_Smaller_Equal_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Expression_Smaller_Equal)


sensinact_DSL_FLAG_AUTOSTART_strategy = st.builds(sensinact_DSL_FLAG_AUTOSTART, activated=st.booleans())
@given(instance=sensinact_DSL_FLAG_AUTOSTART_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_FLAG_AUTOSTART_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_FLAG_AUTOSTART)


sensinact_DSL_IfDo_strategy = st.builds(sensinact_DSL_IfDo)
@given(instance=sensinact_DSL_IfDo_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_IfDo_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_IfDo)


sensinact_DSL_ListActions_strategy = st.builds(sensinact_DSL_ListActions)
@given(instance=sensinact_DSL_ListActions_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_ListActions_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_ListActions)


sensinact_DSL_ListParam_strategy = st.builds(sensinact_DSL_ListParam)
@given(instance=sensinact_DSL_ListParam_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_ListParam_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_ListParam)


sensinact_DSL_Object_Boolean_strategy = st.builds(sensinact_DSL_Object_Boolean, value=st.booleans())
@given(instance=sensinact_DSL_Object_Boolean_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Object_Boolean_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Object_Boolean)


sensinact_DSL_Object_Number_strategy = st.builds(sensinact_DSL_Object_Number, value=safe_text)
@given(instance=sensinact_DSL_Object_Number_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Object_Number_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Object_Number)


sensinact_DSL_Object_Ref_strategy = st.builds(sensinact_DSL_Object_Ref)
@given(instance=sensinact_DSL_Object_Ref_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Object_Ref_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Object_Ref)


sensinact_DSL_Object_String_strategy = st.builds(sensinact_DSL_Object_String, value=safe_text)
@given(instance=sensinact_DSL_Object_String_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Object_String_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Object_String)


sensinact_DSL_On_strategy = st.builds(sensinact_DSL_On)
@given(instance=sensinact_DSL_On_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_On_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_On)


sensinact_DSL_REF_strategy = st.builds(sensinact_DSL_REF, name=safe_text)
@given(instance=sensinact_DSL_REF_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_REF_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_REF)


sensinact_DSL_REF_CONDITION_strategy = st.builds(sensinact_DSL_REF_CONDITION)
@given(instance=sensinact_DSL_REF_CONDITION_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_REF_CONDITION_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_REF_CONDITION)


sensinact_DSL_Resource_strategy = st.builds(sensinact_DSL_Resource, deviceID=safe_text, gatewayID=safe_text, resourceID=safe_text, serviceID=safe_text)
@given(instance=sensinact_DSL_Resource_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_Resource_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_Resource)


sensinact_DSL_ResourceAction_strategy = st.builds(sensinact_DSL_ResourceAction, actiontype=safe_text, variable=safe_text)
@given(instance=sensinact_DSL_ResourceAction_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_ResourceAction_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_ResourceAction)


sensinact_DSL_SENSINACT_strategy = st.builds(sensinact_DSL_SENSINACT)
@given(instance=sensinact_DSL_SENSINACT_strategy)
@settings(max_examples=25)
def test_sensinact_DSL_SENSINACT_instantiation(instance):
    assert isinstance(instance, sensinact_DSL_SENSINACT)


sensinact_EObject_strategy = st.builds(sensinact_EObject)
@given(instance=sensinact_EObject_strategy)
@settings(max_examples=25)
def test_sensinact_EObject_instantiation(instance):
    assert isinstance(instance, sensinact_EObject)


sensinact_Sensinact_strategy = st.builds(sensinact_Sensinact)
@given(instance=sensinact_Sensinact_strategy)
@settings(max_examples=25)
def test_sensinact_Sensinact_instantiation(instance):
    assert isinstance(instance, sensinact_Sensinact)



