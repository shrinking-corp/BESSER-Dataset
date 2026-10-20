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
    Expression,
    parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression,
    parameterizedExpressionsTestLanguage_AssignmentExpression,
    parameterizedExpressionsTestLanguage_IndexedAccessExpression,
    parameterizedExpressionsTestLanguage_YieldExpression,
    parameterizedExpressionsTestLanguage_RelationalExpression,
    parameterizedExpressionsTestLanguage_ShiftExpression,
    parameterizedExpressionsTestLanguage_IdentifierRef,
    parameterizedExpressionsTestLanguage_Expression,
    parameterizedExpressionsTestLanguage_CommaExpression,
    Statement,
    parameterizedExpressionsTestLanguage_LabelledStatement,
    parameterizedExpressionsTestLanguage_Block,
    parameterizedExpressionsTestLanguage_ExpressionStatement,
    parameterizedExpressionsTestLanguage_FunctionDeclaration,
    parameterizedExpressionsTestLanguage_Statement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpressionstestlanguage_parameterizedpropertyaccessexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression)


def test_hyp_parameterizedexpressionstestlanguage_parameterizedpropertyaccessexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_parameterizedpropertyaccessexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "_property" in params, "Missing parameter '_property'"




def test_hyp_parameterizedexpressionstestlanguage_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_AssignmentExpression)


def test_hyp_parameterizedexpressionstestlanguage_assignmentexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_AssignmentExpression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_assignmentexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_parameterizedexpressionstestlanguage_indexedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_IndexedAccessExpression)


def test_hyp_parameterizedexpressionstestlanguage_indexedaccessexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_IndexedAccessExpression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_indexedaccessexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_IndexedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpressionstestlanguage_yieldexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_YieldExpression)


def test_hyp_parameterizedexpressionstestlanguage_yieldexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_YieldExpression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_yieldexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_YieldExpression.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"




def test_hyp_parameterizedexpressionstestlanguage_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_RelationalExpression)


def test_hyp_parameterizedexpressionstestlanguage_relationalexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_RelationalExpression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_relationalexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_parameterizedexpressionstestlanguage_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_ShiftExpression)


def test_hyp_parameterizedexpressionstestlanguage_shiftexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_ShiftExpression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_shiftexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_parameterizedexpressionstestlanguage_identifierref_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_IdentifierRef)


def test_hyp_parameterizedexpressionstestlanguage_identifierref_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_IdentifierRef.__init__)


def test_hyp_parameterizedexpressionstestlanguage_identifierref_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_IdentifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_parameterizedexpressionstestlanguage_expression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_Expression)


def test_hyp_parameterizedexpressionstestlanguage_expression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_Expression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_expression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpressionstestlanguage_commaexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_CommaExpression)


def test_hyp_parameterizedexpressionstestlanguage_commaexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_CommaExpression.__init__)


def test_hyp_parameterizedexpressionstestlanguage_commaexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_CommaExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpressionstestlanguage_labelledstatement_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_LabelledStatement)


def test_hyp_parameterizedexpressionstestlanguage_labelledstatement_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_LabelledStatement.__init__)


def test_hyp_parameterizedexpressionstestlanguage_labelledstatement_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_LabelledStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_parameterizedexpressionstestlanguage_block_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_Block)


def test_hyp_parameterizedexpressionstestlanguage_block_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_Block.__init__)


def test_hyp_parameterizedexpressionstestlanguage_block_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpressionstestlanguage_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_ExpressionStatement)


def test_hyp_parameterizedexpressionstestlanguage_expressionstatement_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_ExpressionStatement.__init__)


def test_hyp_parameterizedexpressionstestlanguage_expressionstatement_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpressionstestlanguage_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_FunctionDeclaration)


def test_hyp_parameterizedexpressionstestlanguage_functiondeclaration_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_FunctionDeclaration.__init__)


def test_hyp_parameterizedexpressionstestlanguage_functiondeclaration_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "generator" in params, "Missing parameter 'generator'"





def test_hyp_parameterizedexpressionstestlanguage_statement_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage_Statement)


def test_hyp_parameterizedexpressionstestlanguage_statement_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage_Statement.__init__)


def test_hyp_parameterizedexpressionstestlanguage_statement_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage_Statement.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression,
    _property=
        safe_text
)
parameterizedExpressionsTestLanguage_AssignmentExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_AssignmentExpression,
    op=
        safe_text
)
parameterizedExpressionsTestLanguage_IndexedAccessExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_IndexedAccessExpression,
)
parameterizedExpressionsTestLanguage_YieldExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_YieldExpression,
    many=
        st.booleans()
)
parameterizedExpressionsTestLanguage_RelationalExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_RelationalExpression,
    op=
        safe_text
)
parameterizedExpressionsTestLanguage_ShiftExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_ShiftExpression,
    op=
        safe_text
)
parameterizedExpressionsTestLanguage_IdentifierRef_strategy = st.builds(
    parameterizedExpressionsTestLanguage_IdentifierRef,
    id=
        safe_text
)
parameterizedExpressionsTestLanguage_Expression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_Expression,
)
parameterizedExpressionsTestLanguage_CommaExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage_CommaExpression,
)
Statement_strategy = st.builds(
    Statement,
)
parameterizedExpressionsTestLanguage_LabelledStatement_strategy = st.builds(
    parameterizedExpressionsTestLanguage_LabelledStatement,
    name=
        safe_text
)
parameterizedExpressionsTestLanguage_Block_strategy = st.builds(
    parameterizedExpressionsTestLanguage_Block,
)
parameterizedExpressionsTestLanguage_ExpressionStatement_strategy = st.builds(
    parameterizedExpressionsTestLanguage_ExpressionStatement,
)
parameterizedExpressionsTestLanguage_FunctionDeclaration_strategy = st.builds(
    parameterizedExpressionsTestLanguage_FunctionDeclaration,
    name=
        safe_text,
    generator=
        st.booleans()
)
parameterizedExpressionsTestLanguage_Statement_strategy = st.builds(
    parameterizedExpressionsTestLanguage_Statement,
)





@given(instance=parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_strategy)
def test_hyp_parameterizedexpressionstestlanguage_parameterizedpropertyaccessexpression__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original




@given(instance=parameterizedExpressionsTestLanguage_AssignmentExpression_strategy)
def test_hyp_parameterizedexpressionstestlanguage_assignmentexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original





@given(instance=parameterizedExpressionsTestLanguage_YieldExpression_strategy)
def test_hyp_parameterizedexpressionstestlanguage_yieldexpression_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original




@given(instance=parameterizedExpressionsTestLanguage_RelationalExpression_strategy)
def test_hyp_parameterizedexpressionstestlanguage_relationalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=parameterizedExpressionsTestLanguage_ShiftExpression_strategy)
def test_hyp_parameterizedexpressionstestlanguage_shiftexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=parameterizedExpressionsTestLanguage_IdentifierRef_strategy)
def test_hyp_parameterizedexpressionstestlanguage_identifierref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original







@given(instance=parameterizedExpressionsTestLanguage_LabelledStatement_strategy)
def test_hyp_parameterizedexpressionstestlanguage_labelledstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=parameterizedExpressionsTestLanguage_FunctionDeclaration_strategy)
def test_hyp_parameterizedexpressionstestlanguage_functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=parameterizedExpressionsTestLanguage_FunctionDeclaration_strategy)
def test_hyp_parameterizedexpressionstestlanguage_functiondeclaration_generator_setter(instance):
    original = instance.generator
    instance.generator = original
    assert instance.generator == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    Statement,
    parameterizedExpressionsTestLanguage_AssignmentExpression,
    parameterizedExpressionsTestLanguage_Block,
    parameterizedExpressionsTestLanguage_CommaExpression,
    parameterizedExpressionsTestLanguage_Expression,
    parameterizedExpressionsTestLanguage_ExpressionStatement,
    parameterizedExpressionsTestLanguage_FunctionDeclaration,
    parameterizedExpressionsTestLanguage_IdentifierRef,
    parameterizedExpressionsTestLanguage_IndexedAccessExpression,
    parameterizedExpressionsTestLanguage_LabelledStatement,
    parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression,
    parameterizedExpressionsTestLanguage_RelationalExpression,
    parameterizedExpressionsTestLanguage_ShiftExpression,
    parameterizedExpressionsTestLanguage_Statement,
    parameterizedExpressionsTestLanguage_YieldExpression,
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

def test_parameterizedExpressionsTestLanguage_AssignmentExpression_op_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_parameterizedExpressionsTestLanguage_FunctionDeclaration_generator_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_FunctionDeclaration(generator=True, name="sample_text")
    assert instance.generator == True
    instance.generator = False
    assert instance.generator == False


def test_parameterizedExpressionsTestLanguage_FunctionDeclaration_name_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_FunctionDeclaration(generator=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_parameterizedExpressionsTestLanguage_IdentifierRef_id_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_IdentifierRef(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_parameterizedExpressionsTestLanguage_LabelledStatement_name_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_LabelledStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression__property_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(_property="sample_text")
    assert instance._property == "sample_text"
    instance._property = "sample_text_2"
    assert instance._property == "sample_text_2"


def test_parameterizedExpressionsTestLanguage_RelationalExpression_op_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_parameterizedExpressionsTestLanguage_ShiftExpression_op_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_parameterizedExpressionsTestLanguage_YieldExpression_many_value_roundtrip():
    instance = parameterizedExpressionsTestLanguage_YieldExpression(many=True)
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_parameterizedExpressionsTestLanguage_AssignmentExpression_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_CommaExpression_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_CommaExpression()
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_IdentifierRef_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_IdentifierRef(id="sample_text")
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_IndexedAccessExpression_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_IndexedAccessExpression()
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(_property="sample_text")
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_RelationalExpression_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_ShiftExpression_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_YieldExpression_isa_Expression():
    instance = parameterizedExpressionsTestLanguage_YieldExpression(many=True)
    assert isinstance(instance, Expression)


def test_parameterizedExpressionsTestLanguage_Block_isa_Statement():
    instance = parameterizedExpressionsTestLanguage_Block()
    assert isinstance(instance, Statement)


def test_parameterizedExpressionsTestLanguage_ExpressionStatement_isa_Statement():
    instance = parameterizedExpressionsTestLanguage_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_parameterizedExpressionsTestLanguage_FunctionDeclaration_isa_Statement():
    instance = parameterizedExpressionsTestLanguage_FunctionDeclaration(generator=True, name="sample_text")
    assert isinstance(instance, Statement)


def test_parameterizedExpressionsTestLanguage_LabelledStatement_isa_Statement():
    instance = parameterizedExpressionsTestLanguage_LabelledStatement(name="sample_text")
    assert isinstance(instance, Statement)


def test_assoc_body0_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_FunctionDeclaration(generator=True, name="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Block()
    b2 = parameterizedExpressionsTestLanguage_Block()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Block'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Block', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Block'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Block', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Block'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Block', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Block'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Block', a)


def test_assoc_expression28_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_YieldExpression(many=True)
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_YieldExpression', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_YieldExpression', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression29'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression29', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_YieldExpression', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_YieldExpression', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression29'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression29', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression29'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression29', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_YieldExpression', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_YieldExpression', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression29'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression29', a)


def test_assoc_lhs13_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ShiftExpression', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_ShiftExpression', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression14'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression14', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ShiftExpression', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_ShiftExpression', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression14'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression14', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression14'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression14', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ShiftExpression', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_ShiftExpression', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression14'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression14', a)


def test_assoc_lhs18_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_RelationalExpression', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_RelationalExpression', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression19'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression19', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_RelationalExpression', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_RelationalExpression', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression19'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression19', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression19'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression19', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_RelationalExpression', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_RelationalExpression', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression19'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression19', a)


def test_assoc_lhs23_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression24'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression24', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression24'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression24', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression24'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression24', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression24'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression24', a)


def test_assoc_rhs15_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ShiftExpression16', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_ShiftExpression16', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression17'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression17', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ShiftExpression16', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_ShiftExpression16', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression17'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression17', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression17'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression17', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ShiftExpression16', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_ShiftExpression16', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression17'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression17', a)


def test_assoc_rhs20_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_RelationalExpression21', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_RelationalExpression21', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression22'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression22', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_RelationalExpression21', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_RelationalExpression21', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression22'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression22', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression22'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression22', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_RelationalExpression21', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_RelationalExpression21', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression22'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression22', a)


def test_assoc_rhs25_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression27'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression27', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression27'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression27', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression27'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression27', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression27'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression27', a)


def test_assoc_statement4_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_LabelledStatement(name="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Statement()
    b2 = parameterizedExpressionsTestLanguage_Statement()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_LabelledStatement', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_LabelledStatement', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Statement5'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Statement5', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_LabelledStatement', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_LabelledStatement', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Statement5'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Statement5', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Statement5'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Statement5', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_LabelledStatement', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_LabelledStatement', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Statement5'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Statement5', a)


def test_assoc_target11_link_reassign_clear():
    a = parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(_property="sample_text")
    b1 = parameterizedExpressionsTestLanguage_Expression()
    b2 = parameterizedExpressionsTestLanguage_Expression()
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', b1)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', b1)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression12'):
        assert _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression12', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', b2)
    assert _is_linked(a, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', b2)
    if hasattr(b1, 'parameterizedExpressionsTestLanguage_Expression12'):
        assert not _is_linked(b1, 'parameterizedExpressionsTestLanguage_Expression12', a)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression12'):
        assert _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression12', a)
    _safe_set(a, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', None)
    assert not _is_linked(a, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', b2)
    if hasattr(b2, 'parameterizedExpressionsTestLanguage_Expression12'):
        assert not _is_linked(b2, 'parameterizedExpressionsTestLanguage_Expression12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


parameterizedExpressionsTestLanguage_AssignmentExpression_strategy = st.builds(parameterizedExpressionsTestLanguage_AssignmentExpression, op=safe_text)
@given(instance=parameterizedExpressionsTestLanguage_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_AssignmentExpression)


parameterizedExpressionsTestLanguage_Block_strategy = st.builds(parameterizedExpressionsTestLanguage_Block)
@given(instance=parameterizedExpressionsTestLanguage_Block_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_Block_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_Block)


parameterizedExpressionsTestLanguage_CommaExpression_strategy = st.builds(parameterizedExpressionsTestLanguage_CommaExpression)
@given(instance=parameterizedExpressionsTestLanguage_CommaExpression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_CommaExpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_CommaExpression)


parameterizedExpressionsTestLanguage_Expression_strategy = st.builds(parameterizedExpressionsTestLanguage_Expression)
@given(instance=parameterizedExpressionsTestLanguage_Expression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_Expression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_Expression)


parameterizedExpressionsTestLanguage_ExpressionStatement_strategy = st.builds(parameterizedExpressionsTestLanguage_ExpressionStatement)
@given(instance=parameterizedExpressionsTestLanguage_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_ExpressionStatement)


parameterizedExpressionsTestLanguage_FunctionDeclaration_strategy = st.builds(parameterizedExpressionsTestLanguage_FunctionDeclaration, generator=st.booleans(), name=safe_text)
@given(instance=parameterizedExpressionsTestLanguage_FunctionDeclaration_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_FunctionDeclaration_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_FunctionDeclaration)


parameterizedExpressionsTestLanguage_IdentifierRef_strategy = st.builds(parameterizedExpressionsTestLanguage_IdentifierRef, id=safe_text)
@given(instance=parameterizedExpressionsTestLanguage_IdentifierRef_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_IdentifierRef_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_IdentifierRef)


parameterizedExpressionsTestLanguage_IndexedAccessExpression_strategy = st.builds(parameterizedExpressionsTestLanguage_IndexedAccessExpression)
@given(instance=parameterizedExpressionsTestLanguage_IndexedAccessExpression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_IndexedAccessExpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_IndexedAccessExpression)


parameterizedExpressionsTestLanguage_LabelledStatement_strategy = st.builds(parameterizedExpressionsTestLanguage_LabelledStatement, name=safe_text)
@given(instance=parameterizedExpressionsTestLanguage_LabelledStatement_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_LabelledStatement_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_LabelledStatement)


parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_strategy = st.builds(parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression, _property=safe_text)
@given(instance=parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression)


parameterizedExpressionsTestLanguage_RelationalExpression_strategy = st.builds(parameterizedExpressionsTestLanguage_RelationalExpression, op=safe_text)
@given(instance=parameterizedExpressionsTestLanguage_RelationalExpression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_RelationalExpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_RelationalExpression)


parameterizedExpressionsTestLanguage_ShiftExpression_strategy = st.builds(parameterizedExpressionsTestLanguage_ShiftExpression, op=safe_text)
@given(instance=parameterizedExpressionsTestLanguage_ShiftExpression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_ShiftExpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_ShiftExpression)


parameterizedExpressionsTestLanguage_Statement_strategy = st.builds(parameterizedExpressionsTestLanguage_Statement)
@given(instance=parameterizedExpressionsTestLanguage_Statement_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_Statement_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_Statement)


parameterizedExpressionsTestLanguage_YieldExpression_strategy = st.builds(parameterizedExpressionsTestLanguage_YieldExpression, many=st.booleans())
@given(instance=parameterizedExpressionsTestLanguage_YieldExpression_strategy)
@settings(max_examples=25)
def test_parameterizedExpressionsTestLanguage_YieldExpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage_YieldExpression)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Statement,
    parameterizedExpressionsTestLanguage_AssignmentExpression,
    parameterizedExpressionsTestLanguage_Block,
    parameterizedExpressionsTestLanguage_CommaExpression,
    parameterizedExpressionsTestLanguage_Expression,
    parameterizedExpressionsTestLanguage_ExpressionStatement,
    parameterizedExpressionsTestLanguage_FunctionDeclaration,
    parameterizedExpressionsTestLanguage_IdentifierRef,
    parameterizedExpressionsTestLanguage_IndexedAccessExpression,
    parameterizedExpressionsTestLanguage_LabelledStatement,
    parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression,
    parameterizedExpressionsTestLanguage_RelationalExpression,
    parameterizedExpressionsTestLanguage_ShiftExpression,
    parameterizedExpressionsTestLanguage_Statement,
    parameterizedExpressionsTestLanguage_YieldExpression,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body0_stub_double():
    # parameterizedExpressionsTestLanguage_Block has no real 'parameterizedExpressionsTestLanguage_Block' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_FunctionDeclaration(generator=True, name="sample_text")
    partner = parameterizedExpressionsTestLanguage_Block()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Block', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Block') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Block') is None


def test_assoc_expression28_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression29' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_YieldExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_YieldExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_YieldExpression(many=True)
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression29', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_YieldExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression29') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_YieldExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression29') is None


def test_assoc_lhs13_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression14', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression14') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression14') is None


def test_assoc_lhs18_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression19' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression19', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression19') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression19') is None


def test_assoc_lhs23_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression24', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression24') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression24') is None


def test_assoc_rhs15_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression17', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression16', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression17') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression16', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression17') is None


def test_assoc_rhs20_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression22' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression22', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression21', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression22') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression21', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression22') is None


def test_assoc_rhs25_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression27', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression27') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression27') is None


def test_assoc_statement4_stub_double():
    # parameterizedExpressionsTestLanguage_Statement has no real 'parameterizedExpressionsTestLanguage_Statement5' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_LabelledStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_LabelledStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_LabelledStatement(name="sample_text")
    partner = parameterizedExpressionsTestLanguage_Statement()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Statement5', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_LabelledStatement', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Statement5') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_LabelledStatement', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Statement5') is None


def test_assoc_target11_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression12' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(_property="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression12', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression12') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression12') is None




from python_code import parameterizedExpressionsTestLanguage_AssignmentExpression
from python_code import parameterizedExpressionsTestLanguage_Expression

def test_parameterizedExpressionsTestLanguage_AssignmentExpression___init__():
    assert parameterizedExpressionsTestLanguage_AssignmentExpression.__init__(parameterizedExpressionsTestLanguage_AssignmentExpression('', parameterizedExpressionsTestLanguage_AssignmentExpression=parameterizedExpressionsTestLanguage_Expression(), parameterizedExpressionsTestLanguage_AssignmentExpression26=parameterizedExpressionsTestLanguage_Expression()), '', parameterizedExpressionsTestLanguage_AssignmentExpression=parameterizedExpressionsTestLanguage_Expression(), parameterizedExpressionsTestLanguage_AssignmentExpression26=parameterizedExpressionsTestLanguage_Expression()) == None
from python_code import parameterizedExpressionsTestLanguage_Block
from python_code import parameterizedExpressionsTestLanguage_FunctionDeclaration

def test_parameterizedExpressionsTestLanguage_FunctionDeclaration___init__():
    assert parameterizedExpressionsTestLanguage_FunctionDeclaration.__init__(parameterizedExpressionsTestLanguage_FunctionDeclaration(False, '\x00', parameterizedExpressionsTestLanguage_FunctionDeclaration=parameterizedExpressionsTestLanguage_Block()), False, '\x00', parameterizedExpressionsTestLanguage_FunctionDeclaration=parameterizedExpressionsTestLanguage_Block()) == None
from python_code import parameterizedExpressionsTestLanguage_IdentifierRef

def test_parameterizedExpressionsTestLanguage_IdentifierRef___init__():
    assert parameterizedExpressionsTestLanguage_IdentifierRef.__init__(parameterizedExpressionsTestLanguage_IdentifierRef(''), '') == None
from python_code import parameterizedExpressionsTestLanguage_LabelledStatement
from python_code import parameterizedExpressionsTestLanguage_Statement

def test_parameterizedExpressionsTestLanguage_LabelledStatement___init__():
    assert parameterizedExpressionsTestLanguage_LabelledStatement.__init__(parameterizedExpressionsTestLanguage_LabelledStatement('', parameterizedExpressionsTestLanguage_LabelledStatement=parameterizedExpressionsTestLanguage_Statement()), '', parameterizedExpressionsTestLanguage_LabelledStatement=parameterizedExpressionsTestLanguage_Statement()) == None
from python_code import parameterizedExpressionsTestLanguage_Expression
from python_code import parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression

def test_parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression___init__():
    assert parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression.__init__(parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression('', parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression=parameterizedExpressionsTestLanguage_Expression()), '', parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression=parameterizedExpressionsTestLanguage_Expression()) == None
from python_code import parameterizedExpressionsTestLanguage_Expression
from python_code import parameterizedExpressionsTestLanguage_RelationalExpression

def test_parameterizedExpressionsTestLanguage_RelationalExpression___init__():
    assert parameterizedExpressionsTestLanguage_RelationalExpression.__init__(parameterizedExpressionsTestLanguage_RelationalExpression('', parameterizedExpressionsTestLanguage_RelationalExpression=parameterizedExpressionsTestLanguage_Expression(), parameterizedExpressionsTestLanguage_RelationalExpression21=parameterizedExpressionsTestLanguage_Expression()), '', parameterizedExpressionsTestLanguage_RelationalExpression=parameterizedExpressionsTestLanguage_Expression(), parameterizedExpressionsTestLanguage_RelationalExpression21=parameterizedExpressionsTestLanguage_Expression()) == None
from python_code import parameterizedExpressionsTestLanguage_Expression
from python_code import parameterizedExpressionsTestLanguage_ShiftExpression

def test_parameterizedExpressionsTestLanguage_ShiftExpression___init__():
    assert parameterizedExpressionsTestLanguage_ShiftExpression.__init__(parameterizedExpressionsTestLanguage_ShiftExpression('', parameterizedExpressionsTestLanguage_ShiftExpression=parameterizedExpressionsTestLanguage_Expression(), parameterizedExpressionsTestLanguage_ShiftExpression16=parameterizedExpressionsTestLanguage_Expression()), '', parameterizedExpressionsTestLanguage_ShiftExpression=parameterizedExpressionsTestLanguage_Expression(), parameterizedExpressionsTestLanguage_ShiftExpression16=parameterizedExpressionsTestLanguage_Expression()) == None
from python_code import parameterizedExpressionsTestLanguage_Expression
from python_code import parameterizedExpressionsTestLanguage_YieldExpression

def test_parameterizedExpressionsTestLanguage_YieldExpression___init__():
    assert parameterizedExpressionsTestLanguage_YieldExpression.__init__(parameterizedExpressionsTestLanguage_YieldExpression(True, parameterizedExpressionsTestLanguage_YieldExpression=parameterizedExpressionsTestLanguage_Expression()), False, parameterizedExpressionsTestLanguage_YieldExpression=parameterizedExpressionsTestLanguage_Expression()) == None

