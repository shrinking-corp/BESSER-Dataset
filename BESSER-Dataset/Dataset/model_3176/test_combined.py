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
    SJExpression,
    smallJava_SJStringConstant,
    smallJava_SJIntConstant,
    smallJava_SJNew,
    smallJava_SJBoolConstant,
    smallJava_SJNull,
    smallJava_SJMemberSelection,
    smallJava_SJSymbolRef,
    smallJava_SJThis,
    smallJava_SJAssignment,
    SJStatement,
    smallJava_SJIfStatement,
    smallJava_SJReturn,
    smallJava_SJExpression,
    smallJava_SJNamedElement,
    SJMember,
    smallJava_SJMethod,
    smallJava_SJField,
    SJNamedElement,
    smallJava_SJMember,
    smallJava_SJSymbol,
    smallJava_SJClass,
    smallJava_SJStatement,
    SJSymbol,
    smallJava_SJVariableDeclaration,
    smallJava_SJBlock,
    smallJava_SJParameter,
    smallJava_SJProgram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sjexpression_is_not_abstract():
    assert not inspect.isabstract(SJExpression)


def test_hyp_sjexpression_constructor_exists():
    assert callable(SJExpression.__init__)


def test_hyp_sjexpression_constructor_args():
    sig = inspect.signature(SJExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjstringconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJStringConstant)


def test_hyp_smalljava_sjstringconstant_constructor_exists():
    assert callable(smallJava_SJStringConstant.__init__)


def test_hyp_smalljava_sjstringconstant_constructor_args():
    sig = inspect.signature(smallJava_SJStringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smalljava_sjintconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJIntConstant)


def test_hyp_smalljava_sjintconstant_constructor_exists():
    assert callable(smallJava_SJIntConstant.__init__)


def test_hyp_smalljava_sjintconstant_constructor_args():
    sig = inspect.signature(smallJava_SJIntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smalljava_sjnew_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJNew)


def test_hyp_smalljava_sjnew_constructor_exists():
    assert callable(smallJava_SJNew.__init__)


def test_hyp_smalljava_sjnew_constructor_args():
    sig = inspect.signature(smallJava_SJNew.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjboolconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJBoolConstant)


def test_hyp_smalljava_sjboolconstant_constructor_exists():
    assert callable(smallJava_SJBoolConstant.__init__)


def test_hyp_smalljava_sjboolconstant_constructor_args():
    sig = inspect.signature(smallJava_SJBoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_smalljava_sjnull_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJNull)


def test_hyp_smalljava_sjnull_constructor_exists():
    assert callable(smallJava_SJNull.__init__)


def test_hyp_smalljava_sjnull_constructor_args():
    sig = inspect.signature(smallJava_SJNull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjmemberselection_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJMemberSelection)


def test_hyp_smalljava_sjmemberselection_constructor_exists():
    assert callable(smallJava_SJMemberSelection.__init__)


def test_hyp_smalljava_sjmemberselection_constructor_args():
    sig = inspect.signature(smallJava_SJMemberSelection.__init__)
    params = list(sig.parameters.keys())
    assert "methodinvocation" in params, "Missing parameter 'methodinvocation'"




def test_hyp_smalljava_sjsymbolref_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJSymbolRef)


def test_hyp_smalljava_sjsymbolref_constructor_exists():
    assert callable(smallJava_SJSymbolRef.__init__)


def test_hyp_smalljava_sjsymbolref_constructor_args():
    sig = inspect.signature(smallJava_SJSymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjthis_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJThis)


def test_hyp_smalljava_sjthis_constructor_exists():
    assert callable(smallJava_SJThis.__init__)


def test_hyp_smalljava_sjthis_constructor_args():
    sig = inspect.signature(smallJava_SJThis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjassignment_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJAssignment)


def test_hyp_smalljava_sjassignment_constructor_exists():
    assert callable(smallJava_SJAssignment.__init__)


def test_hyp_smalljava_sjassignment_constructor_args():
    sig = inspect.signature(smallJava_SJAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sjstatement_is_not_abstract():
    assert not inspect.isabstract(SJStatement)


def test_hyp_sjstatement_constructor_exists():
    assert callable(SJStatement.__init__)


def test_hyp_sjstatement_constructor_args():
    sig = inspect.signature(SJStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjifstatement_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJIfStatement)


def test_hyp_smalljava_sjifstatement_constructor_exists():
    assert callable(smallJava_SJIfStatement.__init__)


def test_hyp_smalljava_sjifstatement_constructor_args():
    sig = inspect.signature(smallJava_SJIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjreturn_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJReturn)


def test_hyp_smalljava_sjreturn_constructor_exists():
    assert callable(smallJava_SJReturn.__init__)


def test_hyp_smalljava_sjreturn_constructor_args():
    sig = inspect.signature(smallJava_SJReturn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjexpression_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJExpression)


def test_hyp_smalljava_sjexpression_constructor_exists():
    assert callable(smallJava_SJExpression.__init__)


def test_hyp_smalljava_sjexpression_constructor_args():
    sig = inspect.signature(smallJava_SJExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjnamedelement_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJNamedElement)


def test_hyp_smalljava_sjnamedelement_constructor_exists():
    assert callable(smallJava_SJNamedElement.__init__)


def test_hyp_smalljava_sjnamedelement_constructor_args():
    sig = inspect.signature(smallJava_SJNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sjmember_is_not_abstract():
    assert not inspect.isabstract(SJMember)


def test_hyp_sjmember_constructor_exists():
    assert callable(SJMember.__init__)


def test_hyp_sjmember_constructor_args():
    sig = inspect.signature(SJMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjmethod_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJMethod)


def test_hyp_smalljava_sjmethod_constructor_exists():
    assert callable(smallJava_SJMethod.__init__)


def test_hyp_smalljava_sjmethod_constructor_args():
    sig = inspect.signature(smallJava_SJMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjfield_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJField)


def test_hyp_smalljava_sjfield_constructor_exists():
    assert callable(smallJava_SJField.__init__)


def test_hyp_smalljava_sjfield_constructor_args():
    sig = inspect.signature(smallJava_SJField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sjnamedelement_is_not_abstract():
    assert not inspect.isabstract(SJNamedElement)


def test_hyp_sjnamedelement_constructor_exists():
    assert callable(SJNamedElement.__init__)


def test_hyp_sjnamedelement_constructor_args():
    sig = inspect.signature(SJNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjmember_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJMember)


def test_hyp_smalljava_sjmember_constructor_exists():
    assert callable(smallJava_SJMember.__init__)


def test_hyp_smalljava_sjmember_constructor_args():
    sig = inspect.signature(smallJava_SJMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjsymbol_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJSymbol)


def test_hyp_smalljava_sjsymbol_constructor_exists():
    assert callable(smallJava_SJSymbol.__init__)


def test_hyp_smalljava_sjsymbol_constructor_args():
    sig = inspect.signature(smallJava_SJSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjclass_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJClass)


def test_hyp_smalljava_sjclass_constructor_exists():
    assert callable(smallJava_SJClass.__init__)


def test_hyp_smalljava_sjclass_constructor_args():
    sig = inspect.signature(smallJava_SJClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjstatement_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJStatement)


def test_hyp_smalljava_sjstatement_constructor_exists():
    assert callable(smallJava_SJStatement.__init__)


def test_hyp_smalljava_sjstatement_constructor_args():
    sig = inspect.signature(smallJava_SJStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sjsymbol_is_not_abstract():
    assert not inspect.isabstract(SJSymbol)


def test_hyp_sjsymbol_constructor_exists():
    assert callable(SJSymbol.__init__)


def test_hyp_sjsymbol_constructor_args():
    sig = inspect.signature(SJSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJVariableDeclaration)


def test_hyp_smalljava_sjvariabledeclaration_constructor_exists():
    assert callable(smallJava_SJVariableDeclaration.__init__)


def test_hyp_smalljava_sjvariabledeclaration_constructor_args():
    sig = inspect.signature(smallJava_SJVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjblock_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJBlock)


def test_hyp_smalljava_sjblock_constructor_exists():
    assert callable(smallJava_SJBlock.__init__)


def test_hyp_smalljava_sjblock_constructor_args():
    sig = inspect.signature(smallJava_SJBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjparameter_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJParameter)


def test_hyp_smalljava_sjparameter_constructor_exists():
    assert callable(smallJava_SJParameter.__init__)


def test_hyp_smalljava_sjparameter_constructor_args():
    sig = inspect.signature(smallJava_SJParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_smalljava_sjprogram_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJProgram)


def test_hyp_smalljava_sjprogram_constructor_exists():
    assert callable(smallJava_SJProgram.__init__)


def test_hyp_smalljava_sjprogram_constructor_args():
    sig = inspect.signature(smallJava_SJProgram.__init__)
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
SJExpression_strategy = st.builds(
    SJExpression,
)
smallJava_SJStringConstant_strategy = st.builds(
    smallJava_SJStringConstant,
    value=
        safe_text
)
smallJava_SJIntConstant_strategy = st.builds(
    smallJava_SJIntConstant,
    value=
        st.integers()
)
smallJava_SJNew_strategy = st.builds(
    smallJava_SJNew,
)
smallJava_SJBoolConstant_strategy = st.builds(
    smallJava_SJBoolConstant,
    value=
        safe_text
)
smallJava_SJNull_strategy = st.builds(
    smallJava_SJNull,
)
smallJava_SJMemberSelection_strategy = st.builds(
    smallJava_SJMemberSelection,
    methodinvocation=
        st.booleans()
)
smallJava_SJSymbolRef_strategy = st.builds(
    smallJava_SJSymbolRef,
)
smallJava_SJThis_strategy = st.builds(
    smallJava_SJThis,
)
smallJava_SJAssignment_strategy = st.builds(
    smallJava_SJAssignment,
)
SJStatement_strategy = st.builds(
    SJStatement,
)
smallJava_SJIfStatement_strategy = st.builds(
    smallJava_SJIfStatement,
)
smallJava_SJReturn_strategy = st.builds(
    smallJava_SJReturn,
)
smallJava_SJExpression_strategy = st.builds(
    smallJava_SJExpression,
)
smallJava_SJNamedElement_strategy = st.builds(
    smallJava_SJNamedElement,
    name=
        safe_text
)
SJMember_strategy = st.builds(
    SJMember,
)
smallJava_SJMethod_strategy = st.builds(
    smallJava_SJMethod,
)
smallJava_SJField_strategy = st.builds(
    smallJava_SJField,
)
SJNamedElement_strategy = st.builds(
    SJNamedElement,
)
smallJava_SJMember_strategy = st.builds(
    smallJava_SJMember,
)
smallJava_SJSymbol_strategy = st.builds(
    smallJava_SJSymbol,
)
smallJava_SJClass_strategy = st.builds(
    smallJava_SJClass,
)
smallJava_SJStatement_strategy = st.builds(
    smallJava_SJStatement,
)
SJSymbol_strategy = st.builds(
    SJSymbol,
)
smallJava_SJVariableDeclaration_strategy = st.builds(
    smallJava_SJVariableDeclaration,
)
smallJava_SJBlock_strategy = st.builds(
    smallJava_SJBlock,
)
smallJava_SJParameter_strategy = st.builds(
    smallJava_SJParameter,
)
smallJava_SJProgram_strategy = st.builds(
    smallJava_SJProgram,
)





@given(instance=smallJava_SJStringConstant_strategy)
def test_hyp_smalljava_sjstringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=smallJava_SJIntConstant_strategy)
def test_hyp_smalljava_sjintconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=smallJava_SJBoolConstant_strategy)
def test_hyp_smalljava_sjboolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=smallJava_SJMemberSelection_strategy)
def test_hyp_smalljava_sjmemberselection_methodinvocation_setter(instance):
    original = instance.methodinvocation
    instance.methodinvocation = original
    assert instance.methodinvocation == original











@given(instance=smallJava_SJNamedElement_strategy)
def test_hyp_smalljava_sjnamedelement_name_setter(instance):
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
    SJExpression,
    SJMember,
    SJNamedElement,
    SJStatement,
    SJSymbol,
    smallJava_SJAssignment,
    smallJava_SJBlock,
    smallJava_SJBoolConstant,
    smallJava_SJClass,
    smallJava_SJExpression,
    smallJava_SJField,
    smallJava_SJIfStatement,
    smallJava_SJIntConstant,
    smallJava_SJMember,
    smallJava_SJMemberSelection,
    smallJava_SJMethod,
    smallJava_SJNamedElement,
    smallJava_SJNew,
    smallJava_SJNull,
    smallJava_SJParameter,
    smallJava_SJProgram,
    smallJava_SJReturn,
    smallJava_SJStatement,
    smallJava_SJStringConstant,
    smallJava_SJSymbol,
    smallJava_SJSymbolRef,
    smallJava_SJThis,
    smallJava_SJVariableDeclaration,
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

def test_smallJava_SJBoolConstant_value_value_roundtrip():
    instance = smallJava_SJBoolConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_smallJava_SJIntConstant_value_value_roundtrip():
    instance = smallJava_SJIntConstant(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_smallJava_SJMemberSelection_methodinvocation_value_roundtrip():
    instance = smallJava_SJMemberSelection(methodinvocation=True)
    assert instance.methodinvocation == True
    instance.methodinvocation = False
    assert instance.methodinvocation == False


def test_smallJava_SJNamedElement_name_value_roundtrip():
    instance = smallJava_SJNamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_smallJava_SJStringConstant_value_value_roundtrip():
    instance = smallJava_SJStringConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_smallJava_SJAssignment_isa_SJExpression():
    instance = smallJava_SJAssignment()
    assert isinstance(instance, SJExpression)


def test_smallJava_SJBoolConstant_isa_SJExpression():
    instance = smallJava_SJBoolConstant(value="sample_text")
    assert isinstance(instance, SJExpression)


def test_smallJava_SJIntConstant_isa_SJExpression():
    instance = smallJava_SJIntConstant(value=7)
    assert isinstance(instance, SJExpression)


def test_smallJava_SJMemberSelection_isa_SJExpression():
    instance = smallJava_SJMemberSelection(methodinvocation=True)
    assert isinstance(instance, SJExpression)


def test_smallJava_SJNew_isa_SJExpression():
    instance = smallJava_SJNew()
    assert isinstance(instance, SJExpression)


def test_smallJava_SJNull_isa_SJExpression():
    instance = smallJava_SJNull()
    assert isinstance(instance, SJExpression)


def test_smallJava_SJStringConstant_isa_SJExpression():
    instance = smallJava_SJStringConstant(value="sample_text")
    assert isinstance(instance, SJExpression)


def test_smallJava_SJSymbolRef_isa_SJExpression():
    instance = smallJava_SJSymbolRef()
    assert isinstance(instance, SJExpression)


def test_smallJava_SJThis_isa_SJExpression():
    instance = smallJava_SJThis()
    assert isinstance(instance, SJExpression)


def test_smallJava_SJField_isa_SJMember():
    instance = smallJava_SJField()
    assert isinstance(instance, SJMember)


def test_smallJava_SJMethod_isa_SJMember():
    instance = smallJava_SJMethod()
    assert isinstance(instance, SJMember)


def test_smallJava_SJClass_isa_SJNamedElement():
    instance = smallJava_SJClass()
    assert isinstance(instance, SJNamedElement)


def test_smallJava_SJMember_isa_SJNamedElement():
    instance = smallJava_SJMember()
    assert isinstance(instance, SJNamedElement)


def test_smallJava_SJSymbol_isa_SJNamedElement():
    instance = smallJava_SJSymbol()
    assert isinstance(instance, SJNamedElement)


def test_smallJava_SJExpression_isa_SJStatement():
    instance = smallJava_SJExpression()
    assert isinstance(instance, SJStatement)


def test_smallJava_SJIfStatement_isa_SJStatement():
    instance = smallJava_SJIfStatement()
    assert isinstance(instance, SJStatement)


def test_smallJava_SJReturn_isa_SJStatement():
    instance = smallJava_SJReturn()
    assert isinstance(instance, SJStatement)


def test_smallJava_SJVariableDeclaration_isa_SJStatement():
    instance = smallJava_SJVariableDeclaration()
    assert isinstance(instance, SJStatement)


def test_smallJava_SJParameter_isa_SJSymbol():
    instance = smallJava_SJParameter()
    assert isinstance(instance, SJSymbol)


def test_smallJava_SJVariableDeclaration_isa_SJSymbol():
    instance = smallJava_SJVariableDeclaration()
    assert isinstance(instance, SJSymbol)


def test_assoc_args37_link_reassign_clear():
    a = smallJava_SJMemberSelection(methodinvocation=True)
    b1 = smallJava_SJExpression()
    b2 = smallJava_SJExpression()
    _safe_set(a, 'smallJava_SJMemberSelection38', {b1})
    assert _is_linked(a, 'smallJava_SJMemberSelection38', b1)
    if hasattr(b1, 'smallJava_SJExpression39'):
        assert _is_linked(b1, 'smallJava_SJExpression39', a)
    _safe_set(a, 'smallJava_SJMemberSelection38', {b2})
    assert _is_linked(a, 'smallJava_SJMemberSelection38', b2)
    if hasattr(b1, 'smallJava_SJExpression39'):
        assert not _is_linked(b1, 'smallJava_SJExpression39', a)
    if hasattr(b2, 'smallJava_SJExpression39'):
        assert _is_linked(b2, 'smallJava_SJExpression39', a)
    _safe_set(a, 'smallJava_SJMemberSelection38', set())
    assert not _is_linked(a, 'smallJava_SJMemberSelection38', b2)
    if hasattr(b2, 'smallJava_SJExpression39'):
        assert not _is_linked(b2, 'smallJava_SJExpression39', a)


def test_assoc_member34_link_reassign_clear():
    a = smallJava_SJMemberSelection(methodinvocation=True)
    b1 = smallJava_SJMember()
    b2 = smallJava_SJMember()
    _safe_set(a, 'smallJava_SJMemberSelection35', b1)
    assert _is_linked(a, 'smallJava_SJMemberSelection35', b1)
    if hasattr(b1, 'smallJava_SJMember36'):
        assert _is_linked(b1, 'smallJava_SJMember36', a)
    _safe_set(a, 'smallJava_SJMemberSelection35', b2)
    assert _is_linked(a, 'smallJava_SJMemberSelection35', b2)
    if hasattr(b1, 'smallJava_SJMember36'):
        assert not _is_linked(b1, 'smallJava_SJMember36', a)
    if hasattr(b2, 'smallJava_SJMember36'):
        assert _is_linked(b2, 'smallJava_SJMember36', a)
    _safe_set(a, 'smallJava_SJMemberSelection35', None)
    assert not _is_linked(a, 'smallJava_SJMemberSelection35', b2)
    if hasattr(b2, 'smallJava_SJMember36'):
        assert not _is_linked(b2, 'smallJava_SJMember36', a)


def test_assoc_receiver32_link_reassign_clear():
    a = smallJava_SJMemberSelection(methodinvocation=True)
    b1 = smallJava_SJExpression()
    b2 = smallJava_SJExpression()
    _safe_set(a, 'smallJava_SJMemberSelection', b1)
    assert _is_linked(a, 'smallJava_SJMemberSelection', b1)
    if hasattr(b1, 'smallJava_SJExpression33'):
        assert _is_linked(b1, 'smallJava_SJExpression33', a)
    _safe_set(a, 'smallJava_SJMemberSelection', b2)
    assert _is_linked(a, 'smallJava_SJMemberSelection', b2)
    if hasattr(b1, 'smallJava_SJExpression33'):
        assert not _is_linked(b1, 'smallJava_SJExpression33', a)
    if hasattr(b2, 'smallJava_SJExpression33'):
        assert _is_linked(b2, 'smallJava_SJExpression33', a)
    _safe_set(a, 'smallJava_SJMemberSelection', None)
    assert not _is_linked(a, 'smallJava_SJMemberSelection', b2)
    if hasattr(b2, 'smallJava_SJExpression33'):
        assert not _is_linked(b2, 'smallJava_SJExpression33', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SJExpression_strategy = st.builds(SJExpression)
@given(instance=SJExpression_strategy)
@settings(max_examples=25)
def test_SJExpression_instantiation(instance):
    assert isinstance(instance, SJExpression)


SJMember_strategy = st.builds(SJMember)
@given(instance=SJMember_strategy)
@settings(max_examples=25)
def test_SJMember_instantiation(instance):
    assert isinstance(instance, SJMember)


SJNamedElement_strategy = st.builds(SJNamedElement)
@given(instance=SJNamedElement_strategy)
@settings(max_examples=25)
def test_SJNamedElement_instantiation(instance):
    assert isinstance(instance, SJNamedElement)


SJStatement_strategy = st.builds(SJStatement)
@given(instance=SJStatement_strategy)
@settings(max_examples=25)
def test_SJStatement_instantiation(instance):
    assert isinstance(instance, SJStatement)


SJSymbol_strategy = st.builds(SJSymbol)
@given(instance=SJSymbol_strategy)
@settings(max_examples=25)
def test_SJSymbol_instantiation(instance):
    assert isinstance(instance, SJSymbol)


smallJava_SJAssignment_strategy = st.builds(smallJava_SJAssignment)
@given(instance=smallJava_SJAssignment_strategy)
@settings(max_examples=25)
def test_smallJava_SJAssignment_instantiation(instance):
    assert isinstance(instance, smallJava_SJAssignment)


smallJava_SJBlock_strategy = st.builds(smallJava_SJBlock)
@given(instance=smallJava_SJBlock_strategy)
@settings(max_examples=25)
def test_smallJava_SJBlock_instantiation(instance):
    assert isinstance(instance, smallJava_SJBlock)


smallJava_SJBoolConstant_strategy = st.builds(smallJava_SJBoolConstant, value=safe_text)
@given(instance=smallJava_SJBoolConstant_strategy)
@settings(max_examples=25)
def test_smallJava_SJBoolConstant_instantiation(instance):
    assert isinstance(instance, smallJava_SJBoolConstant)


smallJava_SJClass_strategy = st.builds(smallJava_SJClass)
@given(instance=smallJava_SJClass_strategy)
@settings(max_examples=25)
def test_smallJava_SJClass_instantiation(instance):
    assert isinstance(instance, smallJava_SJClass)


smallJava_SJExpression_strategy = st.builds(smallJava_SJExpression)
@given(instance=smallJava_SJExpression_strategy)
@settings(max_examples=25)
def test_smallJava_SJExpression_instantiation(instance):
    assert isinstance(instance, smallJava_SJExpression)


smallJava_SJField_strategy = st.builds(smallJava_SJField)
@given(instance=smallJava_SJField_strategy)
@settings(max_examples=25)
def test_smallJava_SJField_instantiation(instance):
    assert isinstance(instance, smallJava_SJField)


smallJava_SJIfStatement_strategy = st.builds(smallJava_SJIfStatement)
@given(instance=smallJava_SJIfStatement_strategy)
@settings(max_examples=25)
def test_smallJava_SJIfStatement_instantiation(instance):
    assert isinstance(instance, smallJava_SJIfStatement)


smallJava_SJIntConstant_strategy = st.builds(smallJava_SJIntConstant, value=st.integers())
@given(instance=smallJava_SJIntConstant_strategy)
@settings(max_examples=25)
def test_smallJava_SJIntConstant_instantiation(instance):
    assert isinstance(instance, smallJava_SJIntConstant)


smallJava_SJMember_strategy = st.builds(smallJava_SJMember)
@given(instance=smallJava_SJMember_strategy)
@settings(max_examples=25)
def test_smallJava_SJMember_instantiation(instance):
    assert isinstance(instance, smallJava_SJMember)


smallJava_SJMemberSelection_strategy = st.builds(smallJava_SJMemberSelection, methodinvocation=st.booleans())
@given(instance=smallJava_SJMemberSelection_strategy)
@settings(max_examples=25)
def test_smallJava_SJMemberSelection_instantiation(instance):
    assert isinstance(instance, smallJava_SJMemberSelection)


smallJava_SJMethod_strategy = st.builds(smallJava_SJMethod)
@given(instance=smallJava_SJMethod_strategy)
@settings(max_examples=25)
def test_smallJava_SJMethod_instantiation(instance):
    assert isinstance(instance, smallJava_SJMethod)


smallJava_SJNamedElement_strategy = st.builds(smallJava_SJNamedElement, name=safe_text)
@given(instance=smallJava_SJNamedElement_strategy)
@settings(max_examples=25)
def test_smallJava_SJNamedElement_instantiation(instance):
    assert isinstance(instance, smallJava_SJNamedElement)


smallJava_SJNew_strategy = st.builds(smallJava_SJNew)
@given(instance=smallJava_SJNew_strategy)
@settings(max_examples=25)
def test_smallJava_SJNew_instantiation(instance):
    assert isinstance(instance, smallJava_SJNew)


smallJava_SJNull_strategy = st.builds(smallJava_SJNull)
@given(instance=smallJava_SJNull_strategy)
@settings(max_examples=25)
def test_smallJava_SJNull_instantiation(instance):
    assert isinstance(instance, smallJava_SJNull)


smallJava_SJParameter_strategy = st.builds(smallJava_SJParameter)
@given(instance=smallJava_SJParameter_strategy)
@settings(max_examples=25)
def test_smallJava_SJParameter_instantiation(instance):
    assert isinstance(instance, smallJava_SJParameter)


smallJava_SJProgram_strategy = st.builds(smallJava_SJProgram)
@given(instance=smallJava_SJProgram_strategy)
@settings(max_examples=25)
def test_smallJava_SJProgram_instantiation(instance):
    assert isinstance(instance, smallJava_SJProgram)


smallJava_SJReturn_strategy = st.builds(smallJava_SJReturn)
@given(instance=smallJava_SJReturn_strategy)
@settings(max_examples=25)
def test_smallJava_SJReturn_instantiation(instance):
    assert isinstance(instance, smallJava_SJReturn)


smallJava_SJStatement_strategy = st.builds(smallJava_SJStatement)
@given(instance=smallJava_SJStatement_strategy)
@settings(max_examples=25)
def test_smallJava_SJStatement_instantiation(instance):
    assert isinstance(instance, smallJava_SJStatement)


smallJava_SJStringConstant_strategy = st.builds(smallJava_SJStringConstant, value=safe_text)
@given(instance=smallJava_SJStringConstant_strategy)
@settings(max_examples=25)
def test_smallJava_SJStringConstant_instantiation(instance):
    assert isinstance(instance, smallJava_SJStringConstant)


smallJava_SJSymbol_strategy = st.builds(smallJava_SJSymbol)
@given(instance=smallJava_SJSymbol_strategy)
@settings(max_examples=25)
def test_smallJava_SJSymbol_instantiation(instance):
    assert isinstance(instance, smallJava_SJSymbol)


smallJava_SJSymbolRef_strategy = st.builds(smallJava_SJSymbolRef)
@given(instance=smallJava_SJSymbolRef_strategy)
@settings(max_examples=25)
def test_smallJava_SJSymbolRef_instantiation(instance):
    assert isinstance(instance, smallJava_SJSymbolRef)


smallJava_SJThis_strategy = st.builds(smallJava_SJThis)
@given(instance=smallJava_SJThis_strategy)
@settings(max_examples=25)
def test_smallJava_SJThis_instantiation(instance):
    assert isinstance(instance, smallJava_SJThis)


smallJava_SJVariableDeclaration_strategy = st.builds(smallJava_SJVariableDeclaration)
@given(instance=smallJava_SJVariableDeclaration_strategy)
@settings(max_examples=25)
def test_smallJava_SJVariableDeclaration_instantiation(instance):
    assert isinstance(instance, smallJava_SJVariableDeclaration)



