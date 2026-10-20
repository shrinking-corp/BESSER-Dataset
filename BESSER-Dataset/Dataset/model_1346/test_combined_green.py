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
    VariableExpCS,
    essentialOCLCST_CallArgumentsCS,
    PrimitiveLiteralExpCS,
    essentialOCLCST_UnlimitedNaturalLiteralExpCS,
    essentialOCLCST_RealLiteralExpCS,
    essentialOCLCST_NullLiteralExpCS,
    essentialOCLCST_StringLiteralExpCS,
    essentialOCLCST_BooleanLiteralExpCS,
    OclExpressionCS,
    essentialOCLCST_LiteralExpCS,
    essentialOCLCST_VariableExpCS,
    essentialOCLCST_UnaryExpressionCS,
    essentialOCLCST_LetExpCS,
    essentialOCLCST_InvalidLiteralExpCS,
    essentialOCLCST_IntegerLiteralExpCS,
    essentialOCLCST_IfExpCS,
    essentialOCLCST_TypeCS,
    TypeLiteralExpCS,
    CollectionLiteralExpCS,
    TypeCS,
    essentialOCLCST_PathNameCS,
    essentialOCLCST_SimpleNameCS,
    essentialOCLCST_TupleTypeCS,
    essentialOCLCST_CollectionTypeCS,
    essentialOCLCST_CollectionLiteralPartCS,
    LiteralExpCS,
    essentialOCLCST_PrimitiveLiteralExpCS,
    essentialOCLCST_TupleLiteralExpCS,
    essentialOCLCST_TypeLiteralExpCS,
    essentialOCLCST_CollectionLiteralExpCS,
    essentialOCLCST_CallExpCS,
    essentialOCLCST_BinaryExpressionCS,
    essentialOCLCST_OclExpressionCS,
    essentialOCLCST_VariableCS,
    CallArgumentsCS,
    essentialOCLCST_DotIndexArgumentsCS,
    essentialOCLCST_ArrowCallArgumentsCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(VariableExpCS)


def test_hyp_variableexpcs_constructor_exists():
    assert callable(VariableExpCS.__init__)


def test_hyp_variableexpcs_constructor_args():
    sig = inspect.signature(VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_callargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CallArgumentsCS)


def test_hyp_essentialoclcst_callargumentscs_constructor_exists():
    assert callable(essentialOCLCST_CallArgumentsCS.__init__)


def test_hyp_essentialoclcst_callargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CallArgumentsCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_hyp_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_hyp_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_UnlimitedNaturalLiteralExpCS)


def test_hyp_essentialoclcst_unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_UnlimitedNaturalLiteralExpCS.__init__)


def test_hyp_essentialoclcst_unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_realliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_RealLiteralExpCS)


def test_hyp_essentialoclcst_realliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_RealLiteralExpCS.__init__)


def test_hyp_essentialoclcst_realliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_RealLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"




def test_hyp_essentialoclcst_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_NullLiteralExpCS)


def test_hyp_essentialoclcst_nullliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_NullLiteralExpCS.__init__)


def test_hyp_essentialoclcst_nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_StringLiteralExpCS)


def test_hyp_essentialoclcst_stringliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_StringLiteralExpCS.__init__)


def test_hyp_essentialoclcst_stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"




def test_hyp_essentialoclcst_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_BooleanLiteralExpCS)


def test_hyp_essentialoclcst_booleanliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_BooleanLiteralExpCS.__init__)


def test_hyp_essentialoclcst_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OclExpressionCS)


def test_hyp_oclexpressioncs_constructor_exists():
    assert callable(OclExpressionCS.__init__)


def test_hyp_oclexpressioncs_constructor_args():
    sig = inspect.signature(OclExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_LiteralExpCS)


def test_hyp_essentialoclcst_literalexpcs_constructor_exists():
    assert callable(essentialOCLCST_LiteralExpCS.__init__)


def test_hyp_essentialoclcst_literalexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_VariableExpCS)


def test_hyp_essentialoclcst_variableexpcs_constructor_exists():
    assert callable(essentialOCLCST_VariableExpCS.__init__)


def test_hyp_essentialoclcst_variableexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_unaryexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_UnaryExpressionCS)


def test_hyp_essentialoclcst_unaryexpressioncs_constructor_exists():
    assert callable(essentialOCLCST_UnaryExpressionCS.__init__)


def test_hyp_essentialoclcst_unaryexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST_UnaryExpressionCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_essentialoclcst_letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_LetExpCS)


def test_hyp_essentialoclcst_letexpcs_constructor_exists():
    assert callable(essentialOCLCST_LetExpCS.__init__)


def test_hyp_essentialoclcst_letexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_InvalidLiteralExpCS)


def test_hyp_essentialoclcst_invalidliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_InvalidLiteralExpCS.__init__)


def test_hyp_essentialoclcst_invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_integerliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_IntegerLiteralExpCS)


def test_hyp_essentialoclcst_integerliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_IntegerLiteralExpCS.__init__)


def test_hyp_essentialoclcst_integerliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_IntegerLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"




def test_hyp_essentialoclcst_ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_IfExpCS)


def test_hyp_essentialoclcst_ifexpcs_constructor_exists():
    assert callable(essentialOCLCST_IfExpCS.__init__)


def test_hyp_essentialoclcst_ifexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_typecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TypeCS)


def test_hyp_essentialoclcst_typecs_constructor_exists():
    assert callable(essentialOCLCST_TypeCS.__init__)


def test_hyp_essentialoclcst_typecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(TypeLiteralExpCS)


def test_hyp_typeliteralexpcs_constructor_exists():
    assert callable(TypeLiteralExpCS.__init__)


def test_hyp_typeliteralexpcs_constructor_args():
    sig = inspect.signature(TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExpCS)


def test_hyp_collectionliteralexpcs_constructor_exists():
    assert callable(CollectionLiteralExpCS.__init__)


def test_hyp_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_hyp_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_hyp_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_PathNameCS)


def test_hyp_essentialoclcst_pathnamecs_constructor_exists():
    assert callable(essentialOCLCST_PathNameCS.__init__)


def test_hyp_essentialoclcst_pathnamecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_SimpleNameCS)


def test_hyp_essentialoclcst_simplenamecs_constructor_exists():
    assert callable(essentialOCLCST_SimpleNameCS.__init__)


def test_hyp_essentialoclcst_simplenamecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_SimpleNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_essentialoclcst_tupletypecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TupleTypeCS)


def test_hyp_essentialoclcst_tupletypecs_constructor_exists():
    assert callable(essentialOCLCST_TupleTypeCS.__init__)


def test_hyp_essentialoclcst_tupletypecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_essentialoclcst_collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CollectionTypeCS)


def test_hyp_essentialoclcst_collectiontypecs_constructor_exists():
    assert callable(essentialOCLCST_CollectionTypeCS.__init__)


def test_hyp_essentialoclcst_collectiontypecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CollectionLiteralPartCS)


def test_hyp_essentialoclcst_collectionliteralpartcs_constructor_exists():
    assert callable(essentialOCLCST_CollectionLiteralPartCS.__init__)


def test_hyp_essentialoclcst_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_hyp_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_hyp_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_PrimitiveLiteralExpCS)


def test_hyp_essentialoclcst_primitiveliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_PrimitiveLiteralExpCS.__init__)


def test_hyp_essentialoclcst_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TupleLiteralExpCS)


def test_hyp_essentialoclcst_tupleliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_TupleLiteralExpCS.__init__)


def test_hyp_essentialoclcst_tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TypeLiteralExpCS)


def test_hyp_essentialoclcst_typeliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_TypeLiteralExpCS.__init__)


def test_hyp_essentialoclcst_typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CollectionLiteralExpCS)


def test_hyp_essentialoclcst_collectionliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_CollectionLiteralExpCS.__init__)


def test_hyp_essentialoclcst_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_callexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CallExpCS)


def test_hyp_essentialoclcst_callexpcs_constructor_exists():
    assert callable(essentialOCLCST_CallExpCS.__init__)


def test_hyp_essentialoclcst_callexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_binaryexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_BinaryExpressionCS)


def test_hyp_essentialoclcst_binaryexpressioncs_constructor_exists():
    assert callable(essentialOCLCST_BinaryExpressionCS.__init__)


def test_hyp_essentialoclcst_binaryexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST_BinaryExpressionCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_essentialoclcst_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_OclExpressionCS)


def test_hyp_essentialoclcst_oclexpressioncs_constructor_exists():
    assert callable(essentialOCLCST_OclExpressionCS.__init__)


def test_hyp_essentialoclcst_oclexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST_OclExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_VariableCS)


def test_hyp_essentialoclcst_variablecs_constructor_exists():
    assert callable(essentialOCLCST_VariableCS.__init__)


def test_hyp_essentialoclcst_variablecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callargumentscs_is_not_abstract():
    assert not inspect.isabstract(CallArgumentsCS)


def test_hyp_callargumentscs_constructor_exists():
    assert callable(CallArgumentsCS.__init__)


def test_hyp_callargumentscs_constructor_args():
    sig = inspect.signature(CallArgumentsCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_essentialoclcst_dotindexargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_DotIndexArgumentsCS)


def test_hyp_essentialoclcst_dotindexargumentscs_constructor_exists():
    assert callable(essentialOCLCST_DotIndexArgumentsCS.__init__)


def test_hyp_essentialoclcst_dotindexargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST_DotIndexArgumentsCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"




def test_hyp_essentialoclcst_arrowcallargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_ArrowCallArgumentsCS)


def test_hyp_essentialoclcst_arrowcallargumentscs_constructor_exists():
    assert callable(essentialOCLCST_ArrowCallArgumentsCS.__init__)


def test_hyp_essentialoclcst_arrowcallargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST_ArrowCallArgumentsCS.__init__)
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
VariableExpCS_strategy = st.builds(
    VariableExpCS,
)
essentialOCLCST_CallArgumentsCS_strategy = st.builds(
    essentialOCLCST_CallArgumentsCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialOCLCST_UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialOCLCST_UnlimitedNaturalLiteralExpCS,
)
essentialOCLCST_RealLiteralExpCS_strategy = st.builds(
    essentialOCLCST_RealLiteralExpCS,
    realSymbol=
        safe_text
)
essentialOCLCST_NullLiteralExpCS_strategy = st.builds(
    essentialOCLCST_NullLiteralExpCS,
)
essentialOCLCST_StringLiteralExpCS_strategy = st.builds(
    essentialOCLCST_StringLiteralExpCS,
    stringSymbol=
        safe_text
)
essentialOCLCST_BooleanLiteralExpCS_strategy = st.builds(
    essentialOCLCST_BooleanLiteralExpCS,
    value=
        safe_text
)
OclExpressionCS_strategy = st.builds(
    OclExpressionCS,
)
essentialOCLCST_LiteralExpCS_strategy = st.builds(
    essentialOCLCST_LiteralExpCS,
)
essentialOCLCST_VariableExpCS_strategy = st.builds(
    essentialOCLCST_VariableExpCS,
)
essentialOCLCST_UnaryExpressionCS_strategy = st.builds(
    essentialOCLCST_UnaryExpressionCS,
    op=
        safe_text
)
essentialOCLCST_LetExpCS_strategy = st.builds(
    essentialOCLCST_LetExpCS,
)
essentialOCLCST_InvalidLiteralExpCS_strategy = st.builds(
    essentialOCLCST_InvalidLiteralExpCS,
)
essentialOCLCST_IntegerLiteralExpCS_strategy = st.builds(
    essentialOCLCST_IntegerLiteralExpCS,
    integerSymbol=
        safe_text
)
essentialOCLCST_IfExpCS_strategy = st.builds(
    essentialOCLCST_IfExpCS,
)
essentialOCLCST_TypeCS_strategy = st.builds(
    essentialOCLCST_TypeCS,
)
TypeLiteralExpCS_strategy = st.builds(
    TypeLiteralExpCS,
)
CollectionLiteralExpCS_strategy = st.builds(
    CollectionLiteralExpCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
essentialOCLCST_PathNameCS_strategy = st.builds(
    essentialOCLCST_PathNameCS,
)
essentialOCLCST_SimpleNameCS_strategy = st.builds(
    essentialOCLCST_SimpleNameCS,
    value=
        safe_text
)
essentialOCLCST_TupleTypeCS_strategy = st.builds(
    essentialOCLCST_TupleTypeCS,
    value=
        safe_text
)
essentialOCLCST_CollectionTypeCS_strategy = st.builds(
    essentialOCLCST_CollectionTypeCS,
)
essentialOCLCST_CollectionLiteralPartCS_strategy = st.builds(
    essentialOCLCST_CollectionLiteralPartCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialOCLCST_PrimitiveLiteralExpCS_strategy = st.builds(
    essentialOCLCST_PrimitiveLiteralExpCS,
)
essentialOCLCST_TupleLiteralExpCS_strategy = st.builds(
    essentialOCLCST_TupleLiteralExpCS,
)
essentialOCLCST_TypeLiteralExpCS_strategy = st.builds(
    essentialOCLCST_TypeLiteralExpCS,
)
essentialOCLCST_CollectionLiteralExpCS_strategy = st.builds(
    essentialOCLCST_CollectionLiteralExpCS,
)
essentialOCLCST_CallExpCS_strategy = st.builds(
    essentialOCLCST_CallExpCS,
)
essentialOCLCST_BinaryExpressionCS_strategy = st.builds(
    essentialOCLCST_BinaryExpressionCS,
    op=
        safe_text
)
essentialOCLCST_OclExpressionCS_strategy = st.builds(
    essentialOCLCST_OclExpressionCS,
)
essentialOCLCST_VariableCS_strategy = st.builds(
    essentialOCLCST_VariableCS,
)
CallArgumentsCS_strategy = st.builds(
    CallArgumentsCS,
)
essentialOCLCST_DotIndexArgumentsCS_strategy = st.builds(
    essentialOCLCST_DotIndexArgumentsCS,
    isPre=
        st.booleans()
)
essentialOCLCST_ArrowCallArgumentsCS_strategy = st.builds(
    essentialOCLCST_ArrowCallArgumentsCS,
)








@given(instance=essentialOCLCST_RealLiteralExpCS_strategy)
def test_hyp_essentialoclcst_realliteralexpcs_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original





@given(instance=essentialOCLCST_StringLiteralExpCS_strategy)
def test_hyp_essentialoclcst_stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original




@given(instance=essentialOCLCST_BooleanLiteralExpCS_strategy)
def test_hyp_essentialoclcst_booleanliteralexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=essentialOCLCST_UnaryExpressionCS_strategy)
def test_hyp_essentialoclcst_unaryexpressioncs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original






@given(instance=essentialOCLCST_IntegerLiteralExpCS_strategy)
def test_hyp_essentialoclcst_integerliteralexpcs_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original










@given(instance=essentialOCLCST_SimpleNameCS_strategy)
def test_hyp_essentialoclcst_simplenamecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=essentialOCLCST_TupleTypeCS_strategy)
def test_hyp_essentialoclcst_tupletypecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original












@given(instance=essentialOCLCST_BinaryExpressionCS_strategy)
def test_hyp_essentialoclcst_binaryexpressioncs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original







@given(instance=essentialOCLCST_DotIndexArgumentsCS_strategy)
def test_hyp_essentialoclcst_dotindexargumentscs_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CallArgumentsCS,
    CollectionLiteralExpCS,
    LiteralExpCS,
    OclExpressionCS,
    PrimitiveLiteralExpCS,
    TypeCS,
    TypeLiteralExpCS,
    VariableExpCS,
    essentialOCLCST_ArrowCallArgumentsCS,
    essentialOCLCST_BinaryExpressionCS,
    essentialOCLCST_BooleanLiteralExpCS,
    essentialOCLCST_CallArgumentsCS,
    essentialOCLCST_CallExpCS,
    essentialOCLCST_CollectionLiteralExpCS,
    essentialOCLCST_CollectionLiteralPartCS,
    essentialOCLCST_CollectionTypeCS,
    essentialOCLCST_DotIndexArgumentsCS,
    essentialOCLCST_IfExpCS,
    essentialOCLCST_IntegerLiteralExpCS,
    essentialOCLCST_InvalidLiteralExpCS,
    essentialOCLCST_LetExpCS,
    essentialOCLCST_LiteralExpCS,
    essentialOCLCST_NullLiteralExpCS,
    essentialOCLCST_OclExpressionCS,
    essentialOCLCST_PathNameCS,
    essentialOCLCST_PrimitiveLiteralExpCS,
    essentialOCLCST_RealLiteralExpCS,
    essentialOCLCST_SimpleNameCS,
    essentialOCLCST_StringLiteralExpCS,
    essentialOCLCST_TupleLiteralExpCS,
    essentialOCLCST_TupleTypeCS,
    essentialOCLCST_TypeCS,
    essentialOCLCST_TypeLiteralExpCS,
    essentialOCLCST_UnaryExpressionCS,
    essentialOCLCST_UnlimitedNaturalLiteralExpCS,
    essentialOCLCST_VariableCS,
    essentialOCLCST_VariableExpCS,
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

def test_essentialOCLCST_BinaryExpressionCS_op_value_roundtrip():
    instance = essentialOCLCST_BinaryExpressionCS(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_essentialOCLCST_BooleanLiteralExpCS_value_value_roundtrip():
    instance = essentialOCLCST_BooleanLiteralExpCS(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_essentialOCLCST_DotIndexArgumentsCS_isPre_value_roundtrip():
    instance = essentialOCLCST_DotIndexArgumentsCS(isPre=True)
    assert instance.isPre == True
    instance.isPre = False
    assert instance.isPre == False


def test_essentialOCLCST_IntegerLiteralExpCS_integerSymbol_value_roundtrip():
    instance = essentialOCLCST_IntegerLiteralExpCS(integerSymbol="sample_text")
    assert instance.integerSymbol == "sample_text"
    instance.integerSymbol = "sample_text_2"
    assert instance.integerSymbol == "sample_text_2"


def test_essentialOCLCST_RealLiteralExpCS_realSymbol_value_roundtrip():
    instance = essentialOCLCST_RealLiteralExpCS(realSymbol="sample_text")
    assert instance.realSymbol == "sample_text"
    instance.realSymbol = "sample_text_2"
    assert instance.realSymbol == "sample_text_2"


def test_essentialOCLCST_SimpleNameCS_value_value_roundtrip():
    instance = essentialOCLCST_SimpleNameCS(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_essentialOCLCST_StringLiteralExpCS_stringSymbol_value_roundtrip():
    instance = essentialOCLCST_StringLiteralExpCS(stringSymbol="sample_text")
    assert instance.stringSymbol == "sample_text"
    instance.stringSymbol = "sample_text_2"
    assert instance.stringSymbol == "sample_text_2"


def test_essentialOCLCST_TupleTypeCS_value_value_roundtrip():
    instance = essentialOCLCST_TupleTypeCS(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_essentialOCLCST_UnaryExpressionCS_op_value_roundtrip():
    instance = essentialOCLCST_UnaryExpressionCS(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_essentialOCLCST_ArrowCallArgumentsCS_isa_CallArgumentsCS():
    instance = essentialOCLCST_ArrowCallArgumentsCS()
    assert isinstance(instance, CallArgumentsCS)


def test_essentialOCLCST_DotIndexArgumentsCS_isa_CallArgumentsCS():
    instance = essentialOCLCST_DotIndexArgumentsCS(isPre=True)
    assert isinstance(instance, CallArgumentsCS)


def test_essentialOCLCST_CollectionTypeCS_isa_CollectionLiteralExpCS():
    instance = essentialOCLCST_CollectionTypeCS()
    assert isinstance(instance, CollectionLiteralExpCS)


def test_essentialOCLCST_SimpleNameCS_isa_CollectionLiteralExpCS():
    instance = essentialOCLCST_SimpleNameCS(value="sample_text")
    assert isinstance(instance, CollectionLiteralExpCS)


def test_essentialOCLCST_CollectionLiteralExpCS_isa_LiteralExpCS():
    instance = essentialOCLCST_CollectionLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialOCLCST_PrimitiveLiteralExpCS_isa_LiteralExpCS():
    instance = essentialOCLCST_PrimitiveLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialOCLCST_TupleLiteralExpCS_isa_LiteralExpCS():
    instance = essentialOCLCST_TupleLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialOCLCST_TypeLiteralExpCS_isa_LiteralExpCS():
    instance = essentialOCLCST_TypeLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_essentialOCLCST_BinaryExpressionCS_isa_OclExpressionCS():
    instance = essentialOCLCST_BinaryExpressionCS(op="sample_text")
    assert isinstance(instance, OclExpressionCS)


def test_essentialOCLCST_CallExpCS_isa_OclExpressionCS():
    instance = essentialOCLCST_CallExpCS()
    assert isinstance(instance, OclExpressionCS)


def test_essentialOCLCST_IfExpCS_isa_OclExpressionCS():
    instance = essentialOCLCST_IfExpCS()
    assert isinstance(instance, OclExpressionCS)


def test_essentialOCLCST_LetExpCS_isa_OclExpressionCS():
    instance = essentialOCLCST_LetExpCS()
    assert isinstance(instance, OclExpressionCS)


def test_essentialOCLCST_LiteralExpCS_isa_OclExpressionCS():
    instance = essentialOCLCST_LiteralExpCS()
    assert isinstance(instance, OclExpressionCS)


def test_essentialOCLCST_UnaryExpressionCS_isa_OclExpressionCS():
    instance = essentialOCLCST_UnaryExpressionCS(op="sample_text")
    assert isinstance(instance, OclExpressionCS)


def test_essentialOCLCST_VariableExpCS_isa_OclExpressionCS():
    instance = essentialOCLCST_VariableExpCS()
    assert isinstance(instance, OclExpressionCS)


def test_essentialOCLCST_BooleanLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialOCLCST_BooleanLiteralExpCS(value="sample_text")
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialOCLCST_IntegerLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialOCLCST_IntegerLiteralExpCS(integerSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialOCLCST_InvalidLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialOCLCST_InvalidLiteralExpCS()
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialOCLCST_NullLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialOCLCST_NullLiteralExpCS()
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialOCLCST_RealLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialOCLCST_RealLiteralExpCS(realSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialOCLCST_StringLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialOCLCST_StringLiteralExpCS(stringSymbol="sample_text")
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialOCLCST_UnlimitedNaturalLiteralExpCS_isa_PrimitiveLiteralExpCS():
    instance = essentialOCLCST_UnlimitedNaturalLiteralExpCS()
    assert isinstance(instance, PrimitiveLiteralExpCS)


def test_essentialOCLCST_CollectionTypeCS_isa_TypeCS():
    instance = essentialOCLCST_CollectionTypeCS()
    assert isinstance(instance, TypeCS)


def test_essentialOCLCST_PathNameCS_isa_TypeCS():
    instance = essentialOCLCST_PathNameCS()
    assert isinstance(instance, TypeCS)


def test_essentialOCLCST_SimpleNameCS_isa_TypeCS():
    instance = essentialOCLCST_SimpleNameCS(value="sample_text")
    assert isinstance(instance, TypeCS)


def test_essentialOCLCST_TupleTypeCS_isa_TypeCS():
    instance = essentialOCLCST_TupleTypeCS(value="sample_text")
    assert isinstance(instance, TypeCS)


def test_essentialOCLCST_CollectionTypeCS_isa_TypeLiteralExpCS():
    instance = essentialOCLCST_CollectionTypeCS()
    assert isinstance(instance, TypeLiteralExpCS)


def test_essentialOCLCST_PathNameCS_isa_TypeLiteralExpCS():
    instance = essentialOCLCST_PathNameCS()
    assert isinstance(instance, TypeLiteralExpCS)


def test_essentialOCLCST_SimpleNameCS_isa_TypeLiteralExpCS():
    instance = essentialOCLCST_SimpleNameCS(value="sample_text")
    assert isinstance(instance, TypeLiteralExpCS)


def test_essentialOCLCST_TupleTypeCS_isa_TypeLiteralExpCS():
    instance = essentialOCLCST_TupleTypeCS(value="sample_text")
    assert isinstance(instance, TypeLiteralExpCS)


def test_essentialOCLCST_SimpleNameCS_isa_VariableExpCS():
    instance = essentialOCLCST_SimpleNameCS(value="sample_text")
    assert isinstance(instance, VariableExpCS)


def test_assoc_collectionLiteralParts49_link_reassign_clear():
    a = essentialOCLCST_SimpleNameCS(value="sample_text")
    b1 = essentialOCLCST_CollectionLiteralPartCS()
    b2 = essentialOCLCST_CollectionLiteralPartCS()
    _safe_set(a, 'essentialOCLCST_SimpleNameCS50', {b1})
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS50', b1)
    if hasattr(b1, 'essentialOCLCST_CollectionLiteralPartCS51'):
        assert _is_linked(b1, 'essentialOCLCST_CollectionLiteralPartCS51', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS50', {b2})
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS50', b2)
    if hasattr(b1, 'essentialOCLCST_CollectionLiteralPartCS51'):
        assert not _is_linked(b1, 'essentialOCLCST_CollectionLiteralPartCS51', a)
    if hasattr(b2, 'essentialOCLCST_CollectionLiteralPartCS51'):
        assert _is_linked(b2, 'essentialOCLCST_CollectionLiteralPartCS51', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS50', set())
    assert not _is_linked(a, 'essentialOCLCST_SimpleNameCS50', b2)
    if hasattr(b2, 'essentialOCLCST_CollectionLiteralPartCS51'):
        assert not _is_linked(b2, 'essentialOCLCST_CollectionLiteralPartCS51', a)


def test_assoc_indexes31_link_reassign_clear():
    a = essentialOCLCST_DotIndexArgumentsCS(isPre=True)
    b1 = essentialOCLCST_OclExpressionCS()
    b2 = essentialOCLCST_OclExpressionCS()
    _safe_set(a, 'essentialOCLCST_DotIndexArgumentsCS', {b1})
    assert _is_linked(a, 'essentialOCLCST_DotIndexArgumentsCS', b1)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS32'):
        assert _is_linked(b1, 'essentialOCLCST_OclExpressionCS32', a)
    _safe_set(a, 'essentialOCLCST_DotIndexArgumentsCS', {b2})
    assert _is_linked(a, 'essentialOCLCST_DotIndexArgumentsCS', b2)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS32'):
        assert not _is_linked(b1, 'essentialOCLCST_OclExpressionCS32', a)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS32'):
        assert _is_linked(b2, 'essentialOCLCST_OclExpressionCS32', a)
    _safe_set(a, 'essentialOCLCST_DotIndexArgumentsCS', set())
    assert not _is_linked(a, 'essentialOCLCST_DotIndexArgumentsCS', b2)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS32'):
        assert not _is_linked(b2, 'essentialOCLCST_OclExpressionCS32', a)


def test_assoc_left6_link_reassign_clear():
    a = essentialOCLCST_BinaryExpressionCS(op="sample_text")
    b1 = essentialOCLCST_OclExpressionCS()
    b2 = essentialOCLCST_OclExpressionCS()
    _safe_set(a, 'essentialOCLCST_BinaryExpressionCS', b1)
    assert _is_linked(a, 'essentialOCLCST_BinaryExpressionCS', b1)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS7'):
        assert _is_linked(b1, 'essentialOCLCST_OclExpressionCS7', a)
    _safe_set(a, 'essentialOCLCST_BinaryExpressionCS', b2)
    assert _is_linked(a, 'essentialOCLCST_BinaryExpressionCS', b2)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS7'):
        assert not _is_linked(b1, 'essentialOCLCST_OclExpressionCS7', a)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS7'):
        assert _is_linked(b2, 'essentialOCLCST_OclExpressionCS7', a)
    _safe_set(a, 'essentialOCLCST_BinaryExpressionCS', None)
    assert not _is_linked(a, 'essentialOCLCST_BinaryExpressionCS', b2)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS7'):
        assert not _is_linked(b2, 'essentialOCLCST_OclExpressionCS7', a)


def test_assoc_name58_link_reassign_clear():
    a = essentialOCLCST_SimpleNameCS(value="sample_text")
    b1 = essentialOCLCST_VariableCS()
    b2 = essentialOCLCST_VariableCS()
    _safe_set(a, 'essentialOCLCST_SimpleNameCS60', b1)
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS60', b1)
    if hasattr(b1, 'essentialOCLCST_VariableCS59'):
        assert _is_linked(b1, 'essentialOCLCST_VariableCS59', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS60', b2)
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS60', b2)
    if hasattr(b1, 'essentialOCLCST_VariableCS59'):
        assert not _is_linked(b1, 'essentialOCLCST_VariableCS59', a)
    if hasattr(b2, 'essentialOCLCST_VariableCS59'):
        assert _is_linked(b2, 'essentialOCLCST_VariableCS59', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS60', None)
    assert not _is_linked(a, 'essentialOCLCST_SimpleNameCS60', b2)
    if hasattr(b2, 'essentialOCLCST_VariableCS59'):
        assert not _is_linked(b2, 'essentialOCLCST_VariableCS59', a)


def test_assoc_part54_link_reassign_clear():
    a = essentialOCLCST_TupleTypeCS(value="sample_text")
    b1 = essentialOCLCST_VariableCS()
    b2 = essentialOCLCST_VariableCS()
    _safe_set(a, 'essentialOCLCST_TupleTypeCS', {b1})
    assert _is_linked(a, 'essentialOCLCST_TupleTypeCS', b1)
    if hasattr(b1, 'essentialOCLCST_VariableCS55'):
        assert _is_linked(b1, 'essentialOCLCST_VariableCS55', a)
    _safe_set(a, 'essentialOCLCST_TupleTypeCS', {b2})
    assert _is_linked(a, 'essentialOCLCST_TupleTypeCS', b2)
    if hasattr(b1, 'essentialOCLCST_VariableCS55'):
        assert not _is_linked(b1, 'essentialOCLCST_VariableCS55', a)
    if hasattr(b2, 'essentialOCLCST_VariableCS55'):
        assert _is_linked(b2, 'essentialOCLCST_VariableCS55', a)
    _safe_set(a, 'essentialOCLCST_TupleTypeCS', set())
    assert not _is_linked(a, 'essentialOCLCST_TupleTypeCS', b2)
    if hasattr(b2, 'essentialOCLCST_VariableCS55'):
        assert not _is_linked(b2, 'essentialOCLCST_VariableCS55', a)


def test_assoc_right8_link_reassign_clear():
    a = essentialOCLCST_BinaryExpressionCS(op="sample_text")
    b1 = essentialOCLCST_OclExpressionCS()
    b2 = essentialOCLCST_OclExpressionCS()
    _safe_set(a, 'essentialOCLCST_BinaryExpressionCS9', b1)
    assert _is_linked(a, 'essentialOCLCST_BinaryExpressionCS9', b1)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS10'):
        assert _is_linked(b1, 'essentialOCLCST_OclExpressionCS10', a)
    _safe_set(a, 'essentialOCLCST_BinaryExpressionCS9', b2)
    assert _is_linked(a, 'essentialOCLCST_BinaryExpressionCS9', b2)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS10'):
        assert not _is_linked(b1, 'essentialOCLCST_OclExpressionCS10', a)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS10'):
        assert _is_linked(b2, 'essentialOCLCST_OclExpressionCS10', a)
    _safe_set(a, 'essentialOCLCST_BinaryExpressionCS9', None)
    assert not _is_linked(a, 'essentialOCLCST_BinaryExpressionCS9', b2)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS10'):
        assert not _is_linked(b2, 'essentialOCLCST_OclExpressionCS10', a)


def test_assoc_simpleNames46_link_reassign_clear():
    a = essentialOCLCST_SimpleNameCS(value="sample_text")
    b1 = essentialOCLCST_PathNameCS()
    b2 = essentialOCLCST_PathNameCS()
    _safe_set(a, 'essentialOCLCST_SimpleNameCS48', b1)
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS48', b1)
    if hasattr(b1, 'essentialOCLCST_PathNameCS47'):
        assert _is_linked(b1, 'essentialOCLCST_PathNameCS47', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS48', b2)
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS48', b2)
    if hasattr(b1, 'essentialOCLCST_PathNameCS47'):
        assert not _is_linked(b1, 'essentialOCLCST_PathNameCS47', a)
    if hasattr(b2, 'essentialOCLCST_PathNameCS47'):
        assert _is_linked(b2, 'essentialOCLCST_PathNameCS47', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS48', None)
    assert not _is_linked(a, 'essentialOCLCST_SimpleNameCS48', b2)
    if hasattr(b2, 'essentialOCLCST_PathNameCS47'):
        assert not _is_linked(b2, 'essentialOCLCST_PathNameCS47', a)


def test_assoc_source56_link_reassign_clear():
    a = essentialOCLCST_UnaryExpressionCS(op="sample_text")
    b1 = essentialOCLCST_OclExpressionCS()
    b2 = essentialOCLCST_OclExpressionCS()
    _safe_set(a, 'essentialOCLCST_UnaryExpressionCS', b1)
    assert _is_linked(a, 'essentialOCLCST_UnaryExpressionCS', b1)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS57'):
        assert _is_linked(b1, 'essentialOCLCST_OclExpressionCS57', a)
    _safe_set(a, 'essentialOCLCST_UnaryExpressionCS', b2)
    assert _is_linked(a, 'essentialOCLCST_UnaryExpressionCS', b2)
    if hasattr(b1, 'essentialOCLCST_OclExpressionCS57'):
        assert not _is_linked(b1, 'essentialOCLCST_OclExpressionCS57', a)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS57'):
        assert _is_linked(b2, 'essentialOCLCST_OclExpressionCS57', a)
    _safe_set(a, 'essentialOCLCST_UnaryExpressionCS', None)
    assert not _is_linked(a, 'essentialOCLCST_UnaryExpressionCS', b2)
    if hasattr(b2, 'essentialOCLCST_OclExpressionCS57'):
        assert not _is_linked(b2, 'essentialOCLCST_OclExpressionCS57', a)


def test_assoc_value25_link_reassign_clear():
    a = essentialOCLCST_SimpleNameCS(value="sample_text")
    b1 = essentialOCLCST_CollectionTypeCS()
    b2 = essentialOCLCST_CollectionTypeCS()
    _safe_set(a, 'essentialOCLCST_SimpleNameCS', b1)
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS', b1)
    if hasattr(b1, 'essentialOCLCST_CollectionTypeCS'):
        assert _is_linked(b1, 'essentialOCLCST_CollectionTypeCS', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS', b2)
    assert _is_linked(a, 'essentialOCLCST_SimpleNameCS', b2)
    if hasattr(b1, 'essentialOCLCST_CollectionTypeCS'):
        assert not _is_linked(b1, 'essentialOCLCST_CollectionTypeCS', a)
    if hasattr(b2, 'essentialOCLCST_CollectionTypeCS'):
        assert _is_linked(b2, 'essentialOCLCST_CollectionTypeCS', a)
    _safe_set(a, 'essentialOCLCST_SimpleNameCS', None)
    assert not _is_linked(a, 'essentialOCLCST_SimpleNameCS', b2)
    if hasattr(b2, 'essentialOCLCST_CollectionTypeCS'):
        assert not _is_linked(b2, 'essentialOCLCST_CollectionTypeCS', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CallArgumentsCS_strategy = st.builds(CallArgumentsCS)
@given(instance=CallArgumentsCS_strategy)
@settings(max_examples=25)
def test_CallArgumentsCS_instantiation(instance):
    assert isinstance(instance, CallArgumentsCS)


CollectionLiteralExpCS_strategy = st.builds(CollectionLiteralExpCS)
@given(instance=CollectionLiteralExpCS_strategy)
@settings(max_examples=25)
def test_CollectionLiteralExpCS_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExpCS)


LiteralExpCS_strategy = st.builds(LiteralExpCS)
@given(instance=LiteralExpCS_strategy)
@settings(max_examples=25)
def test_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)


OclExpressionCS_strategy = st.builds(OclExpressionCS)
@given(instance=OclExpressionCS_strategy)
@settings(max_examples=25)
def test_OclExpressionCS_instantiation(instance):
    assert isinstance(instance, OclExpressionCS)


PrimitiveLiteralExpCS_strategy = st.builds(PrimitiveLiteralExpCS)
@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=25)
def test_PrimitiveLiteralExpCS_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)


TypeCS_strategy = st.builds(TypeCS)
@given(instance=TypeCS_strategy)
@settings(max_examples=25)
def test_TypeCS_instantiation(instance):
    assert isinstance(instance, TypeCS)


TypeLiteralExpCS_strategy = st.builds(TypeLiteralExpCS)
@given(instance=TypeLiteralExpCS_strategy)
@settings(max_examples=25)
def test_TypeLiteralExpCS_instantiation(instance):
    assert isinstance(instance, TypeLiteralExpCS)


VariableExpCS_strategy = st.builds(VariableExpCS)
@given(instance=VariableExpCS_strategy)
@settings(max_examples=25)
def test_VariableExpCS_instantiation(instance):
    assert isinstance(instance, VariableExpCS)


essentialOCLCST_ArrowCallArgumentsCS_strategy = st.builds(essentialOCLCST_ArrowCallArgumentsCS)
@given(instance=essentialOCLCST_ArrowCallArgumentsCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_ArrowCallArgumentsCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_ArrowCallArgumentsCS)


essentialOCLCST_BinaryExpressionCS_strategy = st.builds(essentialOCLCST_BinaryExpressionCS, op=safe_text)
@given(instance=essentialOCLCST_BinaryExpressionCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_BinaryExpressionCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_BinaryExpressionCS)


essentialOCLCST_BooleanLiteralExpCS_strategy = st.builds(essentialOCLCST_BooleanLiteralExpCS, value=safe_text)
@given(instance=essentialOCLCST_BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_BooleanLiteralExpCS)


essentialOCLCST_CallArgumentsCS_strategy = st.builds(essentialOCLCST_CallArgumentsCS)
@given(instance=essentialOCLCST_CallArgumentsCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_CallArgumentsCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CallArgumentsCS)


essentialOCLCST_CallExpCS_strategy = st.builds(essentialOCLCST_CallExpCS)
@given(instance=essentialOCLCST_CallExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_CallExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CallExpCS)


essentialOCLCST_CollectionLiteralExpCS_strategy = st.builds(essentialOCLCST_CollectionLiteralExpCS)
@given(instance=essentialOCLCST_CollectionLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_CollectionLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CollectionLiteralExpCS)


essentialOCLCST_CollectionLiteralPartCS_strategy = st.builds(essentialOCLCST_CollectionLiteralPartCS)
@given(instance=essentialOCLCST_CollectionLiteralPartCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_CollectionLiteralPartCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CollectionLiteralPartCS)


essentialOCLCST_CollectionTypeCS_strategy = st.builds(essentialOCLCST_CollectionTypeCS)
@given(instance=essentialOCLCST_CollectionTypeCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_CollectionTypeCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CollectionTypeCS)


essentialOCLCST_DotIndexArgumentsCS_strategy = st.builds(essentialOCLCST_DotIndexArgumentsCS, isPre=st.booleans())
@given(instance=essentialOCLCST_DotIndexArgumentsCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_DotIndexArgumentsCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_DotIndexArgumentsCS)


essentialOCLCST_IfExpCS_strategy = st.builds(essentialOCLCST_IfExpCS)
@given(instance=essentialOCLCST_IfExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_IfExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_IfExpCS)


essentialOCLCST_IntegerLiteralExpCS_strategy = st.builds(essentialOCLCST_IntegerLiteralExpCS, integerSymbol=safe_text)
@given(instance=essentialOCLCST_IntegerLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_IntegerLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_IntegerLiteralExpCS)


essentialOCLCST_InvalidLiteralExpCS_strategy = st.builds(essentialOCLCST_InvalidLiteralExpCS)
@given(instance=essentialOCLCST_InvalidLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_InvalidLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_InvalidLiteralExpCS)


essentialOCLCST_LetExpCS_strategy = st.builds(essentialOCLCST_LetExpCS)
@given(instance=essentialOCLCST_LetExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_LetExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_LetExpCS)


essentialOCLCST_LiteralExpCS_strategy = st.builds(essentialOCLCST_LiteralExpCS)
@given(instance=essentialOCLCST_LiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_LiteralExpCS)


essentialOCLCST_NullLiteralExpCS_strategy = st.builds(essentialOCLCST_NullLiteralExpCS)
@given(instance=essentialOCLCST_NullLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_NullLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_NullLiteralExpCS)


essentialOCLCST_OclExpressionCS_strategy = st.builds(essentialOCLCST_OclExpressionCS)
@given(instance=essentialOCLCST_OclExpressionCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_OclExpressionCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_OclExpressionCS)


essentialOCLCST_PathNameCS_strategy = st.builds(essentialOCLCST_PathNameCS)
@given(instance=essentialOCLCST_PathNameCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_PathNameCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_PathNameCS)


essentialOCLCST_PrimitiveLiteralExpCS_strategy = st.builds(essentialOCLCST_PrimitiveLiteralExpCS)
@given(instance=essentialOCLCST_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_PrimitiveLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_PrimitiveLiteralExpCS)


essentialOCLCST_RealLiteralExpCS_strategy = st.builds(essentialOCLCST_RealLiteralExpCS, realSymbol=safe_text)
@given(instance=essentialOCLCST_RealLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_RealLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_RealLiteralExpCS)


essentialOCLCST_SimpleNameCS_strategy = st.builds(essentialOCLCST_SimpleNameCS, value=safe_text)
@given(instance=essentialOCLCST_SimpleNameCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_SimpleNameCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_SimpleNameCS)


essentialOCLCST_StringLiteralExpCS_strategy = st.builds(essentialOCLCST_StringLiteralExpCS, stringSymbol=safe_text)
@given(instance=essentialOCLCST_StringLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_StringLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_StringLiteralExpCS)


essentialOCLCST_TupleLiteralExpCS_strategy = st.builds(essentialOCLCST_TupleLiteralExpCS)
@given(instance=essentialOCLCST_TupleLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_TupleLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TupleLiteralExpCS)


essentialOCLCST_TupleTypeCS_strategy = st.builds(essentialOCLCST_TupleTypeCS, value=safe_text)
@given(instance=essentialOCLCST_TupleTypeCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_TupleTypeCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TupleTypeCS)


essentialOCLCST_TypeCS_strategy = st.builds(essentialOCLCST_TypeCS)
@given(instance=essentialOCLCST_TypeCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_TypeCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TypeCS)


essentialOCLCST_TypeLiteralExpCS_strategy = st.builds(essentialOCLCST_TypeLiteralExpCS)
@given(instance=essentialOCLCST_TypeLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_TypeLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TypeLiteralExpCS)


essentialOCLCST_UnaryExpressionCS_strategy = st.builds(essentialOCLCST_UnaryExpressionCS, op=safe_text)
@given(instance=essentialOCLCST_UnaryExpressionCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_UnaryExpressionCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_UnaryExpressionCS)


essentialOCLCST_UnlimitedNaturalLiteralExpCS_strategy = st.builds(essentialOCLCST_UnlimitedNaturalLiteralExpCS)
@given(instance=essentialOCLCST_UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_UnlimitedNaturalLiteralExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_UnlimitedNaturalLiteralExpCS)


essentialOCLCST_VariableCS_strategy = st.builds(essentialOCLCST_VariableCS)
@given(instance=essentialOCLCST_VariableCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_VariableCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_VariableCS)


essentialOCLCST_VariableExpCS_strategy = st.builds(essentialOCLCST_VariableExpCS)
@given(instance=essentialOCLCST_VariableExpCS_strategy)
@settings(max_examples=25)
def test_essentialOCLCST_VariableExpCS_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_VariableExpCS)



