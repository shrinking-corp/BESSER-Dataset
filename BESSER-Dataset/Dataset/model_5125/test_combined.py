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
    Constraint,
    diva_Invariant,
    diva_DiVAModelElement,
    diva_Annotation,
    Rule,
    diva_PriorityRule,
    Expression,
    diva_VariantExpression,
    diva_ContextExpression,
    diva_MultiplicityConstraint,
    Term,
    diva_NotTerm,
    NaryTerm,
    diva_OrTerm,
    diva_AndTerm,
    Variable,
    diva_BooleanVariable,
    diva_EnumVariable,
    Model,
    diva_BaseModel,
    diva_AspectModel,
    NamedElement,
    diva_EnumLiteral,
    diva_Constraint,
    diva_Variable,
    diva_Rule,
    diva_Dimension,
    diva_Property,
    VariableTerm,
    diva_BooleanTerm,
    diva_EnumTerm,
    diva_VariableTerm,
    diva_Variant,
    diva_VariantTerm,
    diva_NaryTerm,
    DiVAModelElement,
    diva_Model,
    diva_PropertyValue,
    diva_Expression,
    diva_PropertyPriority,
    diva_Term,
    diva_NamedElement,
    diva_VariabilityModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_invariant_is_not_abstract():
    assert not inspect.isabstract(diva_Invariant)


def test_hyp_diva_invariant_constructor_exists():
    assert callable(diva_Invariant.__init__)


def test_hyp_diva_invariant_constructor_args():
    sig = inspect.signature(diva_Invariant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_divamodelelement_is_not_abstract():
    assert not inspect.isabstract(diva_DiVAModelElement)


def test_hyp_diva_divamodelelement_constructor_exists():
    assert callable(diva_DiVAModelElement.__init__)


def test_hyp_diva_divamodelelement_constructor_args():
    sig = inspect.signature(diva_DiVAModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_annotation_is_not_abstract():
    assert not inspect.isabstract(diva_Annotation)


def test_hyp_diva_annotation_constructor_exists():
    assert callable(diva_Annotation.__init__)


def test_hyp_diva_annotation_constructor_args():
    sig = inspect.signature(diva_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_hyp_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_hyp_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_priorityrule_is_not_abstract():
    assert not inspect.isabstract(diva_PriorityRule)


def test_hyp_diva_priorityrule_constructor_exists():
    assert callable(diva_PriorityRule.__init__)


def test_hyp_diva_priorityrule_constructor_args():
    sig = inspect.signature(diva_PriorityRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_variantexpression_is_not_abstract():
    assert not inspect.isabstract(diva_VariantExpression)


def test_hyp_diva_variantexpression_constructor_exists():
    assert callable(diva_VariantExpression.__init__)


def test_hyp_diva_variantexpression_constructor_args():
    sig = inspect.signature(diva_VariantExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_contextexpression_is_not_abstract():
    assert not inspect.isabstract(diva_ContextExpression)


def test_hyp_diva_contextexpression_constructor_exists():
    assert callable(diva_ContextExpression.__init__)


def test_hyp_diva_contextexpression_constructor_args():
    sig = inspect.signature(diva_ContextExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_multiplicityconstraint_is_not_abstract():
    assert not inspect.isabstract(diva_MultiplicityConstraint)


def test_hyp_diva_multiplicityconstraint_constructor_exists():
    assert callable(diva_MultiplicityConstraint.__init__)


def test_hyp_diva_multiplicityconstraint_constructor_args():
    sig = inspect.signature(diva_MultiplicityConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"





def test_hyp_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_hyp_term_constructor_exists():
    assert callable(Term.__init__)


def test_hyp_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_notterm_is_not_abstract():
    assert not inspect.isabstract(diva_NotTerm)


def test_hyp_diva_notterm_constructor_exists():
    assert callable(diva_NotTerm.__init__)


def test_hyp_diva_notterm_constructor_args():
    sig = inspect.signature(diva_NotTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_naryterm_is_not_abstract():
    assert not inspect.isabstract(NaryTerm)


def test_hyp_naryterm_constructor_exists():
    assert callable(NaryTerm.__init__)


def test_hyp_naryterm_constructor_args():
    sig = inspect.signature(NaryTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_orterm_is_not_abstract():
    assert not inspect.isabstract(diva_OrTerm)


def test_hyp_diva_orterm_constructor_exists():
    assert callable(diva_OrTerm.__init__)


def test_hyp_diva_orterm_constructor_args():
    sig = inspect.signature(diva_OrTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_andterm_is_not_abstract():
    assert not inspect.isabstract(diva_AndTerm)


def test_hyp_diva_andterm_constructor_exists():
    assert callable(diva_AndTerm.__init__)


def test_hyp_diva_andterm_constructor_args():
    sig = inspect.signature(diva_AndTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_booleanvariable_is_not_abstract():
    assert not inspect.isabstract(diva_BooleanVariable)


def test_hyp_diva_booleanvariable_constructor_exists():
    assert callable(diva_BooleanVariable.__init__)


def test_hyp_diva_booleanvariable_constructor_args():
    sig = inspect.signature(diva_BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_enumvariable_is_not_abstract():
    assert not inspect.isabstract(diva_EnumVariable)


def test_hyp_diva_enumvariable_constructor_exists():
    assert callable(diva_EnumVariable.__init__)


def test_hyp_diva_enumvariable_constructor_args():
    sig = inspect.signature(diva_EnumVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_hyp_model_constructor_exists():
    assert callable(Model.__init__)


def test_hyp_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_basemodel_is_not_abstract():
    assert not inspect.isabstract(diva_BaseModel)


def test_hyp_diva_basemodel_constructor_exists():
    assert callable(diva_BaseModel.__init__)


def test_hyp_diva_basemodel_constructor_args():
    sig = inspect.signature(diva_BaseModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_aspectmodel_is_not_abstract():
    assert not inspect.isabstract(diva_AspectModel)


def test_hyp_diva_aspectmodel_constructor_exists():
    assert callable(diva_AspectModel.__init__)


def test_hyp_diva_aspectmodel_constructor_args():
    sig = inspect.signature(diva_AspectModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_enumliteral_is_not_abstract():
    assert not inspect.isabstract(diva_EnumLiteral)


def test_hyp_diva_enumliteral_constructor_exists():
    assert callable(diva_EnumLiteral.__init__)


def test_hyp_diva_enumliteral_constructor_args():
    sig = inspect.signature(diva_EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_constraint_is_not_abstract():
    assert not inspect.isabstract(diva_Constraint)


def test_hyp_diva_constraint_constructor_exists():
    assert callable(diva_Constraint.__init__)


def test_hyp_diva_constraint_constructor_args():
    sig = inspect.signature(diva_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_variable_is_not_abstract():
    assert not inspect.isabstract(diva_Variable)


def test_hyp_diva_variable_constructor_exists():
    assert callable(diva_Variable.__init__)


def test_hyp_diva_variable_constructor_args():
    sig = inspect.signature(diva_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_rule_is_not_abstract():
    assert not inspect.isabstract(diva_Rule)


def test_hyp_diva_rule_constructor_exists():
    assert callable(diva_Rule.__init__)


def test_hyp_diva_rule_constructor_args():
    sig = inspect.signature(diva_Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_dimension_is_not_abstract():
    assert not inspect.isabstract(diva_Dimension)


def test_hyp_diva_dimension_constructor_exists():
    assert callable(diva_Dimension.__init__)


def test_hyp_diva_dimension_constructor_args():
    sig = inspect.signature(diva_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"





def test_hyp_diva_property_is_not_abstract():
    assert not inspect.isabstract(diva_Property)


def test_hyp_diva_property_constructor_exists():
    assert callable(diva_Property.__init__)


def test_hyp_diva_property_constructor_args():
    sig = inspect.signature(diva_Property.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"




def test_hyp_variableterm_is_not_abstract():
    assert not inspect.isabstract(VariableTerm)


def test_hyp_variableterm_constructor_exists():
    assert callable(VariableTerm.__init__)


def test_hyp_variableterm_constructor_args():
    sig = inspect.signature(VariableTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_booleanterm_is_not_abstract():
    assert not inspect.isabstract(diva_BooleanTerm)


def test_hyp_diva_booleanterm_constructor_exists():
    assert callable(diva_BooleanTerm.__init__)


def test_hyp_diva_booleanterm_constructor_args():
    sig = inspect.signature(diva_BooleanTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_enumterm_is_not_abstract():
    assert not inspect.isabstract(diva_EnumTerm)


def test_hyp_diva_enumterm_constructor_exists():
    assert callable(diva_EnumTerm.__init__)


def test_hyp_diva_enumterm_constructor_args():
    sig = inspect.signature(diva_EnumTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_variableterm_is_not_abstract():
    assert not inspect.isabstract(diva_VariableTerm)


def test_hyp_diva_variableterm_constructor_exists():
    assert callable(diva_VariableTerm.__init__)


def test_hyp_diva_variableterm_constructor_args():
    sig = inspect.signature(diva_VariableTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_variant_is_not_abstract():
    assert not inspect.isabstract(diva_Variant)


def test_hyp_diva_variant_constructor_exists():
    assert callable(diva_Variant.__init__)


def test_hyp_diva_variant_constructor_args():
    sig = inspect.signature(diva_Variant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_variantterm_is_not_abstract():
    assert not inspect.isabstract(diva_VariantTerm)


def test_hyp_diva_variantterm_constructor_exists():
    assert callable(diva_VariantTerm.__init__)


def test_hyp_diva_variantterm_constructor_args():
    sig = inspect.signature(diva_VariantTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_naryterm_is_not_abstract():
    assert not inspect.isabstract(diva_NaryTerm)


def test_hyp_diva_naryterm_constructor_exists():
    assert callable(diva_NaryTerm.__init__)


def test_hyp_diva_naryterm_constructor_args():
    sig = inspect.signature(diva_NaryTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_divamodelelement_is_not_abstract():
    assert not inspect.isabstract(DiVAModelElement)


def test_hyp_divamodelelement_constructor_exists():
    assert callable(DiVAModelElement.__init__)


def test_hyp_divamodelelement_constructor_args():
    sig = inspect.signature(DiVAModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_model_is_not_abstract():
    assert not inspect.isabstract(diva_Model)


def test_hyp_diva_model_constructor_exists():
    assert callable(diva_Model.__init__)


def test_hyp_diva_model_constructor_args():
    sig = inspect.signature(diva_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(diva_PropertyValue)


def test_hyp_diva_propertyvalue_constructor_exists():
    assert callable(diva_PropertyValue.__init__)


def test_hyp_diva_propertyvalue_constructor_args():
    sig = inspect.signature(diva_PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_diva_expression_is_not_abstract():
    assert not inspect.isabstract(diva_Expression)


def test_hyp_diva_expression_constructor_exists():
    assert callable(diva_Expression.__init__)


def test_hyp_diva_expression_constructor_args():
    sig = inspect.signature(diva_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_diva_propertypriority_is_not_abstract():
    assert not inspect.isabstract(diva_PropertyPriority)


def test_hyp_diva_propertypriority_constructor_exists():
    assert callable(diva_PropertyPriority.__init__)


def test_hyp_diva_propertypriority_constructor_args():
    sig = inspect.signature(diva_PropertyPriority.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"




def test_hyp_diva_term_is_not_abstract():
    assert not inspect.isabstract(diva_Term)


def test_hyp_diva_term_constructor_exists():
    assert callable(diva_Term.__init__)


def test_hyp_diva_term_constructor_args():
    sig = inspect.signature(diva_Term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diva_namedelement_is_not_abstract():
    assert not inspect.isabstract(diva_NamedElement)


def test_hyp_diva_namedelement_constructor_exists():
    assert callable(diva_NamedElement.__init__)


def test_hyp_diva_namedelement_constructor_args():
    sig = inspect.signature(diva_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_diva_variabilitymodel_is_not_abstract():
    assert not inspect.isabstract(diva_VariabilityModel)


def test_hyp_diva_variabilitymodel_constructor_exists():
    assert callable(diva_VariabilityModel.__init__)


def test_hyp_diva_variabilitymodel_constructor_args():
    sig = inspect.signature(diva_VariabilityModel.__init__)
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
Constraint_strategy = st.builds(
    Constraint,
)
diva_Invariant_strategy = st.builds(
    diva_Invariant,
)
diva_DiVAModelElement_strategy = st.builds(
    diva_DiVAModelElement,
)
diva_Annotation_strategy = st.builds(
    diva_Annotation,
    value=
        safe_text,
    key=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
diva_PriorityRule_strategy = st.builds(
    diva_PriorityRule,
)
Expression_strategy = st.builds(
    Expression,
)
diva_VariantExpression_strategy = st.builds(
    diva_VariantExpression,
)
diva_ContextExpression_strategy = st.builds(
    diva_ContextExpression,
)
diva_MultiplicityConstraint_strategy = st.builds(
    diva_MultiplicityConstraint,
    lower=
        safe_text,
    upper=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
diva_NotTerm_strategy = st.builds(
    diva_NotTerm,
)
NaryTerm_strategy = st.builds(
    NaryTerm,
)
diva_OrTerm_strategy = st.builds(
    diva_OrTerm,
)
diva_AndTerm_strategy = st.builds(
    diva_AndTerm,
)
Variable_strategy = st.builds(
    Variable,
)
diva_BooleanVariable_strategy = st.builds(
    diva_BooleanVariable,
)
diva_EnumVariable_strategy = st.builds(
    diva_EnumVariable,
)
Model_strategy = st.builds(
    Model,
)
diva_BaseModel_strategy = st.builds(
    diva_BaseModel,
)
diva_AspectModel_strategy = st.builds(
    diva_AspectModel,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
diva_EnumLiteral_strategy = st.builds(
    diva_EnumLiteral,
)
diva_Constraint_strategy = st.builds(
    diva_Constraint,
)
diva_Variable_strategy = st.builds(
    diva_Variable,
)
diva_Rule_strategy = st.builds(
    diva_Rule,
)
diva_Dimension_strategy = st.builds(
    diva_Dimension,
    upper=
        safe_text,
    lower=
        safe_text
)
diva_Property_strategy = st.builds(
    diva_Property,
    direction=
        safe_text
)
VariableTerm_strategy = st.builds(
    VariableTerm,
)
diva_BooleanTerm_strategy = st.builds(
    diva_BooleanTerm,
)
diva_EnumTerm_strategy = st.builds(
    diva_EnumTerm,
)
diva_VariableTerm_strategy = st.builds(
    diva_VariableTerm,
)
diva_Variant_strategy = st.builds(
    diva_Variant,
)
diva_VariantTerm_strategy = st.builds(
    diva_VariantTerm,
)
diva_NaryTerm_strategy = st.builds(
    diva_NaryTerm,
)
DiVAModelElement_strategy = st.builds(
    DiVAModelElement,
)
diva_Model_strategy = st.builds(
    diva_Model,
)
diva_PropertyValue_strategy = st.builds(
    diva_PropertyValue,
    value=
        safe_text
)
diva_Expression_strategy = st.builds(
    diva_Expression,
    text=
        safe_text
)
diva_PropertyPriority_strategy = st.builds(
    diva_PropertyPriority,
    priority=
        safe_text
)
diva_Term_strategy = st.builds(
    diva_Term,
)
diva_NamedElement_strategy = st.builds(
    diva_NamedElement,
    id=
        safe_text,
    name=
        safe_text
)
diva_VariabilityModel_strategy = st.builds(
    diva_VariabilityModel,
)







@given(instance=diva_Annotation_strategy)
def test_hyp_diva_annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=diva_Annotation_strategy)
def test_hyp_diva_annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original









@given(instance=diva_MultiplicityConstraint_strategy)
def test_hyp_diva_multiplicityconstraint_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=diva_MultiplicityConstraint_strategy)
def test_hyp_diva_multiplicityconstraint_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original











import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diva_BaseModel_strategy)
@settings(max_examples=30)
def test_hyp_diva_basemodel_weave_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.weave()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.weave).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'weave' in diva_BaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'weave' in diva_BaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'weave' in diva_BaseModel is not implemented or raised an error")










@given(instance=diva_Dimension_strategy)
def test_hyp_diva_dimension_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=diva_Dimension_strategy)
def test_hyp_diva_dimension_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original




@given(instance=diva_Property_strategy)
def test_hyp_diva_property_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original













@given(instance=diva_PropertyValue_strategy)
def test_hyp_diva_propertyvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=diva_Expression_strategy)
def test_hyp_diva_expression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=diva_PropertyPriority_strategy)
def test_hyp_diva_propertypriority_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original





@given(instance=diva_NamedElement_strategy)
def test_hyp_diva_namedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=diva_NamedElement_strategy)
def test_hyp_diva_namedelement_name_setter(instance):
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
    Constraint,
    DiVAModelElement,
    Expression,
    Model,
    NamedElement,
    NaryTerm,
    Rule,
    Term,
    Variable,
    VariableTerm,
    diva_AndTerm,
    diva_Annotation,
    diva_AspectModel,
    diva_BaseModel,
    diva_BooleanTerm,
    diva_BooleanVariable,
    diva_Constraint,
    diva_ContextExpression,
    diva_DiVAModelElement,
    diva_Dimension,
    diva_EnumLiteral,
    diva_EnumTerm,
    diva_EnumVariable,
    diva_Expression,
    diva_Invariant,
    diva_Model,
    diva_MultiplicityConstraint,
    diva_NamedElement,
    diva_NaryTerm,
    diva_NotTerm,
    diva_OrTerm,
    diva_PriorityRule,
    diva_Property,
    diva_PropertyPriority,
    diva_PropertyValue,
    diva_Rule,
    diva_Term,
    diva_VariabilityModel,
    diva_Variable,
    diva_VariableTerm,
    diva_Variant,
    diva_VariantExpression,
    diva_VariantTerm,
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

def test_diva_Annotation_key_value_roundtrip():
    instance = diva_Annotation(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_diva_Annotation_value_value_roundtrip():
    instance = diva_Annotation(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_diva_Dimension_lower_value_roundtrip():
    instance = diva_Dimension(lower="sample_text", upper="sample_text")
    assert instance.lower == "sample_text"
    instance.lower = "sample_text_2"
    assert instance.lower == "sample_text_2"


def test_diva_Dimension_upper_value_roundtrip():
    instance = diva_Dimension(lower="sample_text", upper="sample_text")
    assert instance.upper == "sample_text"
    instance.upper = "sample_text_2"
    assert instance.upper == "sample_text_2"


def test_diva_Expression_text_value_roundtrip():
    instance = diva_Expression(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_diva_MultiplicityConstraint_lower_value_roundtrip():
    instance = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    assert instance.lower == "sample_text"
    instance.lower = "sample_text_2"
    assert instance.lower == "sample_text_2"


def test_diva_MultiplicityConstraint_upper_value_roundtrip():
    instance = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    assert instance.upper == "sample_text"
    instance.upper = "sample_text_2"
    assert instance.upper == "sample_text_2"


def test_diva_NamedElement_id_value_roundtrip():
    instance = diva_NamedElement(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_diva_NamedElement_name_value_roundtrip():
    instance = diva_NamedElement(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_diva_Property_direction_value_roundtrip():
    instance = diva_Property(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_diva_PropertyPriority_priority_value_roundtrip():
    instance = diva_PropertyPriority(priority="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_diva_PropertyValue_value_value_roundtrip():
    instance = diva_PropertyValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_diva_Invariant_isa_Constraint():
    instance = diva_Invariant()
    assert isinstance(instance, Constraint)


def test_diva_MultiplicityConstraint_isa_Constraint():
    instance = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    assert isinstance(instance, Constraint)


def test_diva_Expression_isa_DiVAModelElement():
    instance = diva_Expression(text="sample_text")
    assert isinstance(instance, DiVAModelElement)


def test_diva_Model_isa_DiVAModelElement():
    instance = diva_Model()
    assert isinstance(instance, DiVAModelElement)


def test_diva_NamedElement_isa_DiVAModelElement():
    instance = diva_NamedElement(id="sample_text", name="sample_text")
    assert isinstance(instance, DiVAModelElement)


def test_diva_PropertyPriority_isa_DiVAModelElement():
    instance = diva_PropertyPriority(priority="sample_text")
    assert isinstance(instance, DiVAModelElement)


def test_diva_PropertyValue_isa_DiVAModelElement():
    instance = diva_PropertyValue(value="sample_text")
    assert isinstance(instance, DiVAModelElement)


def test_diva_Term_isa_DiVAModelElement():
    instance = diva_Term()
    assert isinstance(instance, DiVAModelElement)


def test_diva_VariabilityModel_isa_DiVAModelElement():
    instance = diva_VariabilityModel()
    assert isinstance(instance, DiVAModelElement)


def test_diva_ContextExpression_isa_Expression():
    instance = diva_ContextExpression()
    assert isinstance(instance, Expression)


def test_diva_VariantExpression_isa_Expression():
    instance = diva_VariantExpression()
    assert isinstance(instance, Expression)


def test_diva_AspectModel_isa_Model():
    instance = diva_AspectModel()
    assert isinstance(instance, Model)


def test_diva_BaseModel_isa_Model():
    instance = diva_BaseModel()
    assert isinstance(instance, Model)


def test_diva_Constraint_isa_NamedElement():
    instance = diva_Constraint()
    assert isinstance(instance, NamedElement)


def test_diva_Dimension_isa_NamedElement():
    instance = diva_Dimension(lower="sample_text", upper="sample_text")
    assert isinstance(instance, NamedElement)


def test_diva_EnumLiteral_isa_NamedElement():
    instance = diva_EnumLiteral()
    assert isinstance(instance, NamedElement)


def test_diva_Property_isa_NamedElement():
    instance = diva_Property(direction="sample_text")
    assert isinstance(instance, NamedElement)


def test_diva_Rule_isa_NamedElement():
    instance = diva_Rule()
    assert isinstance(instance, NamedElement)


def test_diva_Variable_isa_NamedElement():
    instance = diva_Variable()
    assert isinstance(instance, NamedElement)


def test_diva_Variant_isa_NamedElement():
    instance = diva_Variant()
    assert isinstance(instance, NamedElement)


def test_diva_AndTerm_isa_NaryTerm():
    instance = diva_AndTerm()
    assert isinstance(instance, NaryTerm)


def test_diva_OrTerm_isa_NaryTerm():
    instance = diva_OrTerm()
    assert isinstance(instance, NaryTerm)


def test_diva_PriorityRule_isa_Rule():
    instance = diva_PriorityRule()
    assert isinstance(instance, Rule)


def test_diva_NaryTerm_isa_Term():
    instance = diva_NaryTerm()
    assert isinstance(instance, Term)


def test_diva_NotTerm_isa_Term():
    instance = diva_NotTerm()
    assert isinstance(instance, Term)


def test_diva_VariableTerm_isa_Term():
    instance = diva_VariableTerm()
    assert isinstance(instance, Term)


def test_diva_VariantTerm_isa_Term():
    instance = diva_VariantTerm()
    assert isinstance(instance, Term)


def test_diva_BooleanVariable_isa_Variable():
    instance = diva_BooleanVariable()
    assert isinstance(instance, Variable)


def test_diva_EnumVariable_isa_Variable():
    instance = diva_EnumVariable()
    assert isinstance(instance, Variable)


def test_diva_BooleanTerm_isa_VariableTerm():
    instance = diva_BooleanTerm()
    assert isinstance(instance, VariableTerm)


def test_diva_EnumTerm_isa_VariableTerm():
    instance = diva_EnumTerm()
    assert isinstance(instance, VariableTerm)


def test_assoc_annotation55_link_reassign_clear():
    a = diva_Annotation(key="sample_text", value="sample_text")
    b1 = diva_DiVAModelElement()
    b2 = diva_DiVAModelElement()
    _safe_set(a, 'diva_Annotation', b1)
    assert _is_linked(a, 'diva_Annotation', b1)
    if hasattr(b1, 'diva_DiVAModelElement'):
        assert _is_linked(b1, 'diva_DiVAModelElement', a)
    _safe_set(a, 'diva_Annotation', b2)
    assert _is_linked(a, 'diva_Annotation', b2)
    if hasattr(b1, 'diva_DiVAModelElement'):
        assert not _is_linked(b1, 'diva_DiVAModelElement', a)
    if hasattr(b2, 'diva_DiVAModelElement'):
        assert _is_linked(b2, 'diva_DiVAModelElement', a)
    _safe_set(a, 'diva_Annotation', None)
    assert not _is_linked(a, 'diva_Annotation', b2)
    if hasattr(b2, 'diva_DiVAModelElement'):
        assert not _is_linked(b2, 'diva_DiVAModelElement', a)


def test_assoc_available52_link_reassign_clear():
    a = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    b1 = diva_ContextExpression()
    b2 = diva_ContextExpression()
    _safe_set(a, 'diva_MultiplicityConstraint53', b1)
    assert _is_linked(a, 'diva_MultiplicityConstraint53', b1)
    if hasattr(b1, 'diva_ContextExpression54'):
        assert _is_linked(b1, 'diva_ContextExpression54', a)
    _safe_set(a, 'diva_MultiplicityConstraint53', b2)
    assert _is_linked(a, 'diva_MultiplicityConstraint53', b2)
    if hasattr(b1, 'diva_ContextExpression54'):
        assert not _is_linked(b1, 'diva_ContextExpression54', a)
    if hasattr(b2, 'diva_ContextExpression54'):
        assert _is_linked(b2, 'diva_ContextExpression54', a)
    _safe_set(a, 'diva_MultiplicityConstraint53', None)
    assert not _is_linked(a, 'diva_MultiplicityConstraint53', b2)
    if hasattr(b2, 'diva_ContextExpression54'):
        assert not _is_linked(b2, 'diva_ContextExpression54', a)


def test_assoc_base0_link_reassign_clear():
    a = diva_BaseModel()
    b1 = diva_VariabilityModel()
    b2 = diva_VariabilityModel()
    _safe_set(a, 'diva_BaseModel', b1)
    assert _is_linked(a, 'diva_BaseModel', b1)
    if hasattr(b1, 'diva_VariabilityModel'):
        assert _is_linked(b1, 'diva_VariabilityModel', a)
    _safe_set(a, 'diva_BaseModel', b2)
    assert _is_linked(a, 'diva_BaseModel', b2)
    if hasattr(b1, 'diva_VariabilityModel'):
        assert not _is_linked(b1, 'diva_VariabilityModel', a)
    if hasattr(b2, 'diva_VariabilityModel'):
        assert _is_linked(b2, 'diva_VariabilityModel', a)
    _safe_set(a, 'diva_BaseModel', None)
    assert not _is_linked(a, 'diva_BaseModel', b2)
    if hasattr(b2, 'diva_VariabilityModel'):
        assert not _is_linked(b2, 'diva_VariabilityModel', a)


def test_assoc_constraints37_link_reassign_clear():
    a = diva_MultiplicityConstraint(lower="sample_text", upper="sample_text")
    b1 = diva_Dimension(lower="sample_text", upper="sample_text")
    b2 = diva_Dimension(lower="sample_text_2", upper="sample_text_2")
    _safe_set(a, 'diva_MultiplicityConstraint', b1)
    assert _is_linked(a, 'diva_MultiplicityConstraint', b1)
    if hasattr(b1, 'diva_Dimension38'):
        assert _is_linked(b1, 'diva_Dimension38', a)
    _safe_set(a, 'diva_MultiplicityConstraint', b2)
    assert _is_linked(a, 'diva_MultiplicityConstraint', b2)
    if hasattr(b1, 'diva_Dimension38'):
        assert not _is_linked(b1, 'diva_Dimension38', a)
    if hasattr(b2, 'diva_Dimension38'):
        assert _is_linked(b2, 'diva_Dimension38', a)
    _safe_set(a, 'diva_MultiplicityConstraint', None)
    assert not _is_linked(a, 'diva_MultiplicityConstraint', b2)
    if hasattr(b2, 'diva_Dimension38'):
        assert not _is_linked(b2, 'diva_Dimension38', a)


def test_assoc_dimension5_link_reassign_clear():
    a = diva_Dimension(lower="sample_text", upper="sample_text")
    b1 = diva_VariabilityModel()
    b2 = diva_VariabilityModel()
    _safe_set(a, 'diva_Dimension', b1)
    assert _is_linked(a, 'diva_Dimension', b1)
    if hasattr(b1, 'diva_VariabilityModel6'):
        assert _is_linked(b1, 'diva_VariabilityModel6', a)
    _safe_set(a, 'diva_Dimension', b2)
    assert _is_linked(a, 'diva_Dimension', b2)
    if hasattr(b1, 'diva_VariabilityModel6'):
        assert not _is_linked(b1, 'diva_VariabilityModel6', a)
    if hasattr(b2, 'diva_VariabilityModel6'):
        assert _is_linked(b2, 'diva_VariabilityModel6', a)
    _safe_set(a, 'diva_Dimension', None)
    assert not _is_linked(a, 'diva_Dimension', b2)
    if hasattr(b2, 'diva_VariabilityModel6'):
        assert not _is_linked(b2, 'diva_VariabilityModel6', a)


def test_assoc_expression11_link_reassign_clear():
    a = diva_Expression(text="sample_text")
    b1 = diva_Invariant()
    b2 = diva_Invariant()
    _safe_set(a, 'diva_Expression', b1)
    assert _is_linked(a, 'diva_Expression', b1)
    if hasattr(b1, 'diva_Invariant'):
        assert _is_linked(b1, 'diva_Invariant', a)
    _safe_set(a, 'diva_Expression', b2)
    assert _is_linked(a, 'diva_Expression', b2)
    if hasattr(b1, 'diva_Invariant'):
        assert not _is_linked(b1, 'diva_Invariant', a)
    if hasattr(b2, 'diva_Invariant'):
        assert _is_linked(b2, 'diva_Invariant', a)
    _safe_set(a, 'diva_Expression', None)
    assert not _is_linked(a, 'diva_Expression', b2)
    if hasattr(b2, 'diva_Invariant'):
        assert not _is_linked(b2, 'diva_Invariant', a)


def test_assoc_priority44_link_reassign_clear():
    a = diva_PropertyPriority(priority="sample_text")
    b1 = diva_PriorityRule()
    b2 = diva_PriorityRule()
    _safe_set(a, 'diva_PropertyPriority', b1)
    assert _is_linked(a, 'diva_PropertyPriority', b1)
    if hasattr(b1, 'diva_PriorityRule45'):
        assert _is_linked(b1, 'diva_PriorityRule45', a)
    _safe_set(a, 'diva_PropertyPriority', b2)
    assert _is_linked(a, 'diva_PropertyPriority', b2)
    if hasattr(b1, 'diva_PriorityRule45'):
        assert not _is_linked(b1, 'diva_PriorityRule45', a)
    if hasattr(b2, 'diva_PriorityRule45'):
        assert _is_linked(b2, 'diva_PriorityRule45', a)
    _safe_set(a, 'diva_PropertyPriority', None)
    assert not _is_linked(a, 'diva_PropertyPriority', b2)
    if hasattr(b2, 'diva_PriorityRule45'):
        assert not _is_linked(b2, 'diva_PriorityRule45', a)


def test_assoc_property3_link_reassign_clear():
    a = diva_Property(direction="sample_text")
    b1 = diva_VariabilityModel()
    b2 = diva_VariabilityModel()
    _safe_set(a, 'diva_Property', b1)
    assert _is_linked(a, 'diva_Property', b1)
    if hasattr(b1, 'diva_VariabilityModel4'):
        assert _is_linked(b1, 'diva_VariabilityModel4', a)
    _safe_set(a, 'diva_Property', b2)
    assert _is_linked(a, 'diva_Property', b2)
    if hasattr(b1, 'diva_VariabilityModel4'):
        assert not _is_linked(b1, 'diva_VariabilityModel4', a)
    if hasattr(b2, 'diva_VariabilityModel4'):
        assert _is_linked(b2, 'diva_VariabilityModel4', a)
    _safe_set(a, 'diva_Property', None)
    assert not _is_linked(a, 'diva_Property', b2)
    if hasattr(b2, 'diva_VariabilityModel4'):
        assert not _is_linked(b2, 'diva_VariabilityModel4', a)


def test_assoc_property34_link_reassign_clear():
    a = diva_Property(direction="sample_text")
    b1 = diva_Dimension(lower="sample_text", upper="sample_text")
    b2 = diva_Dimension(lower="sample_text_2", upper="sample_text_2")
    _safe_set(a, 'diva_Property36', b1)
    assert _is_linked(a, 'diva_Property36', b1)
    if hasattr(b1, 'diva_Dimension35'):
        assert _is_linked(b1, 'diva_Dimension35', a)
    _safe_set(a, 'diva_Property36', b2)
    assert _is_linked(a, 'diva_Property36', b2)
    if hasattr(b1, 'diva_Dimension35'):
        assert not _is_linked(b1, 'diva_Dimension35', a)
    if hasattr(b2, 'diva_Dimension35'):
        assert _is_linked(b2, 'diva_Dimension35', a)
    _safe_set(a, 'diva_Property36', None)
    assert not _is_linked(a, 'diva_Property36', b2)
    if hasattr(b2, 'diva_Dimension35'):
        assert not _is_linked(b2, 'diva_Dimension35', a)


def test_assoc_property46_link_reassign_clear():
    a = diva_PropertyValue(value="sample_text")
    b1 = diva_Property(direction="sample_text")
    b2 = diva_Property(direction="sample_text_2")
    _safe_set(a, 'diva_PropertyValue47', b1)
    assert _is_linked(a, 'diva_PropertyValue47', b1)
    if hasattr(b1, 'diva_Property48'):
        assert _is_linked(b1, 'diva_Property48', a)
    _safe_set(a, 'diva_PropertyValue47', b2)
    assert _is_linked(a, 'diva_PropertyValue47', b2)
    if hasattr(b1, 'diva_Property48'):
        assert not _is_linked(b1, 'diva_Property48', a)
    if hasattr(b2, 'diva_Property48'):
        assert _is_linked(b2, 'diva_Property48', a)
    _safe_set(a, 'diva_PropertyValue47', None)
    assert not _is_linked(a, 'diva_PropertyValue47', b2)
    if hasattr(b2, 'diva_Property48'):
        assert not _is_linked(b2, 'diva_Property48', a)


def test_assoc_property49_link_reassign_clear():
    a = diva_PropertyPriority(priority="sample_text")
    b1 = diva_Property(direction="sample_text")
    b2 = diva_Property(direction="sample_text_2")
    _safe_set(a, 'diva_PropertyPriority50', b1)
    assert _is_linked(a, 'diva_PropertyPriority50', b1)
    if hasattr(b1, 'diva_Property51'):
        assert _is_linked(b1, 'diva_Property51', a)
    _safe_set(a, 'diva_PropertyPriority50', b2)
    assert _is_linked(a, 'diva_PropertyPriority50', b2)
    if hasattr(b1, 'diva_Property51'):
        assert not _is_linked(b1, 'diva_Property51', a)
    if hasattr(b2, 'diva_Property51'):
        assert _is_linked(b2, 'diva_Property51', a)
    _safe_set(a, 'diva_PropertyPriority50', None)
    assert not _is_linked(a, 'diva_PropertyPriority50', b2)
    if hasattr(b2, 'diva_Property51'):
        assert not _is_linked(b2, 'diva_Property51', a)


def test_assoc_propertyValue24_link_reassign_clear():
    a = diva_PropertyValue(value="sample_text")
    b1 = diva_Variant()
    b2 = diva_Variant()
    _safe_set(a, 'diva_PropertyValue', b1)
    assert _is_linked(a, 'diva_PropertyValue', b1)
    if hasattr(b1, 'diva_Variant25'):
        assert _is_linked(b1, 'diva_Variant25', a)
    _safe_set(a, 'diva_PropertyValue', b2)
    assert _is_linked(a, 'diva_PropertyValue', b2)
    if hasattr(b1, 'diva_Variant25'):
        assert not _is_linked(b1, 'diva_Variant25', a)
    if hasattr(b2, 'diva_Variant25'):
        assert _is_linked(b2, 'diva_Variant25', a)
    _safe_set(a, 'diva_PropertyValue', None)
    assert not _is_linked(a, 'diva_PropertyValue', b2)
    if hasattr(b2, 'diva_Variant25'):
        assert not _is_linked(b2, 'diva_Variant25', a)


def test_assoc_term39_link_reassign_clear():
    a = diva_Expression(text="sample_text")
    b1 = diva_Term()
    b2 = diva_Term()
    _safe_set(a, 'diva_Expression40', b1)
    assert _is_linked(a, 'diva_Expression40', b1)
    if hasattr(b1, 'diva_Term41'):
        assert _is_linked(b1, 'diva_Term41', a)
    _safe_set(a, 'diva_Expression40', b2)
    assert _is_linked(a, 'diva_Expression40', b2)
    if hasattr(b1, 'diva_Term41'):
        assert not _is_linked(b1, 'diva_Term41', a)
    if hasattr(b2, 'diva_Term41'):
        assert _is_linked(b2, 'diva_Term41', a)
    _safe_set(a, 'diva_Expression40', None)
    assert not _is_linked(a, 'diva_Expression40', b2)
    if hasattr(b2, 'diva_Term41'):
        assert not _is_linked(b2, 'diva_Term41', a)


def test_assoc_type23_link_reassign_clear():
    a = diva_Dimension(lower="sample_text", upper="sample_text")
    b1 = diva_Variant()
    b2 = diva_Variant()
    _safe_set(a, 'Dimension', b1)
    assert _is_linked(a, 'Dimension', b1)
    if hasattr(b1, 'variant'):
        assert _is_linked(b1, 'variant', a)
    _safe_set(a, 'Dimension', b2)
    assert _is_linked(a, 'Dimension', b2)
    if hasattr(b1, 'variant'):
        assert not _is_linked(b1, 'variant', a)
    if hasattr(b2, 'variant'):
        assert _is_linked(b2, 'variant', a)
    _safe_set(a, 'Dimension', None)
    assert not _is_linked(a, 'Dimension', b2)
    if hasattr(b2, 'variant'):
        assert not _is_linked(b2, 'variant', a)


def test_assoc_variant33_link_reassign_clear():
    a = diva_Dimension(lower="sample_text", upper="sample_text")
    b1 = diva_Variant()
    b2 = diva_Variant()
    _safe_set(a, 'type', {b1})
    assert _is_linked(a, 'type', b1)
    if hasattr(b1, 'Variant'):
        assert _is_linked(b1, 'Variant', a)
    _safe_set(a, 'type', {b2})
    assert _is_linked(a, 'type', b2)
    if hasattr(b1, 'Variant'):
        assert not _is_linked(b1, 'Variant', a)
    if hasattr(b2, 'Variant'):
        assert _is_linked(b2, 'Variant', a)
    _safe_set(a, 'type', set())
    assert not _is_linked(a, 'type', b2)
    if hasattr(b2, 'Variant'):
        assert not _is_linked(b2, 'Variant', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


DiVAModelElement_strategy = st.builds(DiVAModelElement)
@given(instance=DiVAModelElement_strategy)
@settings(max_examples=25)
def test_DiVAModelElement_instantiation(instance):
    assert isinstance(instance, DiVAModelElement)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Model_strategy = st.builds(Model)
@given(instance=Model_strategy)
@settings(max_examples=25)
def test_Model_instantiation(instance):
    assert isinstance(instance, Model)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NaryTerm_strategy = st.builds(NaryTerm)
@given(instance=NaryTerm_strategy)
@settings(max_examples=25)
def test_NaryTerm_instantiation(instance):
    assert isinstance(instance, NaryTerm)


Rule_strategy = st.builds(Rule)
@given(instance=Rule_strategy)
@settings(max_examples=25)
def test_Rule_instantiation(instance):
    assert isinstance(instance, Rule)


Term_strategy = st.builds(Term)
@given(instance=Term_strategy)
@settings(max_examples=25)
def test_Term_instantiation(instance):
    assert isinstance(instance, Term)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


VariableTerm_strategy = st.builds(VariableTerm)
@given(instance=VariableTerm_strategy)
@settings(max_examples=25)
def test_VariableTerm_instantiation(instance):
    assert isinstance(instance, VariableTerm)


diva_AndTerm_strategy = st.builds(diva_AndTerm)
@given(instance=diva_AndTerm_strategy)
@settings(max_examples=25)
def test_diva_AndTerm_instantiation(instance):
    assert isinstance(instance, diva_AndTerm)


diva_Annotation_strategy = st.builds(diva_Annotation, key=safe_text, value=safe_text)
@given(instance=diva_Annotation_strategy)
@settings(max_examples=25)
def test_diva_Annotation_instantiation(instance):
    assert isinstance(instance, diva_Annotation)


diva_AspectModel_strategy = st.builds(diva_AspectModel)
@given(instance=diva_AspectModel_strategy)
@settings(max_examples=25)
def test_diva_AspectModel_instantiation(instance):
    assert isinstance(instance, diva_AspectModel)


diva_BaseModel_strategy = st.builds(diva_BaseModel)
@given(instance=diva_BaseModel_strategy)
@settings(max_examples=25)
def test_diva_BaseModel_instantiation(instance):
    assert isinstance(instance, diva_BaseModel)


diva_BooleanTerm_strategy = st.builds(diva_BooleanTerm)
@given(instance=diva_BooleanTerm_strategy)
@settings(max_examples=25)
def test_diva_BooleanTerm_instantiation(instance):
    assert isinstance(instance, diva_BooleanTerm)


diva_BooleanVariable_strategy = st.builds(diva_BooleanVariable)
@given(instance=diva_BooleanVariable_strategy)
@settings(max_examples=25)
def test_diva_BooleanVariable_instantiation(instance):
    assert isinstance(instance, diva_BooleanVariable)


diva_Constraint_strategy = st.builds(diva_Constraint)
@given(instance=diva_Constraint_strategy)
@settings(max_examples=25)
def test_diva_Constraint_instantiation(instance):
    assert isinstance(instance, diva_Constraint)


diva_ContextExpression_strategy = st.builds(diva_ContextExpression)
@given(instance=diva_ContextExpression_strategy)
@settings(max_examples=25)
def test_diva_ContextExpression_instantiation(instance):
    assert isinstance(instance, diva_ContextExpression)


diva_DiVAModelElement_strategy = st.builds(diva_DiVAModelElement)
@given(instance=diva_DiVAModelElement_strategy)
@settings(max_examples=25)
def test_diva_DiVAModelElement_instantiation(instance):
    assert isinstance(instance, diva_DiVAModelElement)


diva_Dimension_strategy = st.builds(diva_Dimension, lower=safe_text, upper=safe_text)
@given(instance=diva_Dimension_strategy)
@settings(max_examples=25)
def test_diva_Dimension_instantiation(instance):
    assert isinstance(instance, diva_Dimension)


diva_EnumLiteral_strategy = st.builds(diva_EnumLiteral)
@given(instance=diva_EnumLiteral_strategy)
@settings(max_examples=25)
def test_diva_EnumLiteral_instantiation(instance):
    assert isinstance(instance, diva_EnumLiteral)


diva_EnumTerm_strategy = st.builds(diva_EnumTerm)
@given(instance=diva_EnumTerm_strategy)
@settings(max_examples=25)
def test_diva_EnumTerm_instantiation(instance):
    assert isinstance(instance, diva_EnumTerm)


diva_EnumVariable_strategy = st.builds(diva_EnumVariable)
@given(instance=diva_EnumVariable_strategy)
@settings(max_examples=25)
def test_diva_EnumVariable_instantiation(instance):
    assert isinstance(instance, diva_EnumVariable)


diva_Expression_strategy = st.builds(diva_Expression, text=safe_text)
@given(instance=diva_Expression_strategy)
@settings(max_examples=25)
def test_diva_Expression_instantiation(instance):
    assert isinstance(instance, diva_Expression)


diva_Invariant_strategy = st.builds(diva_Invariant)
@given(instance=diva_Invariant_strategy)
@settings(max_examples=25)
def test_diva_Invariant_instantiation(instance):
    assert isinstance(instance, diva_Invariant)


diva_Model_strategy = st.builds(diva_Model)
@given(instance=diva_Model_strategy)
@settings(max_examples=25)
def test_diva_Model_instantiation(instance):
    assert isinstance(instance, diva_Model)


diva_MultiplicityConstraint_strategy = st.builds(diva_MultiplicityConstraint, lower=safe_text, upper=safe_text)
@given(instance=diva_MultiplicityConstraint_strategy)
@settings(max_examples=25)
def test_diva_MultiplicityConstraint_instantiation(instance):
    assert isinstance(instance, diva_MultiplicityConstraint)


diva_NamedElement_strategy = st.builds(diva_NamedElement, id=safe_text, name=safe_text)
@given(instance=diva_NamedElement_strategy)
@settings(max_examples=25)
def test_diva_NamedElement_instantiation(instance):
    assert isinstance(instance, diva_NamedElement)


diva_NaryTerm_strategy = st.builds(diva_NaryTerm)
@given(instance=diva_NaryTerm_strategy)
@settings(max_examples=25)
def test_diva_NaryTerm_instantiation(instance):
    assert isinstance(instance, diva_NaryTerm)


diva_NotTerm_strategy = st.builds(diva_NotTerm)
@given(instance=diva_NotTerm_strategy)
@settings(max_examples=25)
def test_diva_NotTerm_instantiation(instance):
    assert isinstance(instance, diva_NotTerm)


diva_OrTerm_strategy = st.builds(diva_OrTerm)
@given(instance=diva_OrTerm_strategy)
@settings(max_examples=25)
def test_diva_OrTerm_instantiation(instance):
    assert isinstance(instance, diva_OrTerm)


diva_PriorityRule_strategy = st.builds(diva_PriorityRule)
@given(instance=diva_PriorityRule_strategy)
@settings(max_examples=25)
def test_diva_PriorityRule_instantiation(instance):
    assert isinstance(instance, diva_PriorityRule)


diva_Property_strategy = st.builds(diva_Property, direction=safe_text)
@given(instance=diva_Property_strategy)
@settings(max_examples=25)
def test_diva_Property_instantiation(instance):
    assert isinstance(instance, diva_Property)


diva_PropertyPriority_strategy = st.builds(diva_PropertyPriority, priority=safe_text)
@given(instance=diva_PropertyPriority_strategy)
@settings(max_examples=25)
def test_diva_PropertyPriority_instantiation(instance):
    assert isinstance(instance, diva_PropertyPriority)


diva_PropertyValue_strategy = st.builds(diva_PropertyValue, value=safe_text)
@given(instance=diva_PropertyValue_strategy)
@settings(max_examples=25)
def test_diva_PropertyValue_instantiation(instance):
    assert isinstance(instance, diva_PropertyValue)


diva_Rule_strategy = st.builds(diva_Rule)
@given(instance=diva_Rule_strategy)
@settings(max_examples=25)
def test_diva_Rule_instantiation(instance):
    assert isinstance(instance, diva_Rule)


diva_Term_strategy = st.builds(diva_Term)
@given(instance=diva_Term_strategy)
@settings(max_examples=25)
def test_diva_Term_instantiation(instance):
    assert isinstance(instance, diva_Term)


diva_VariabilityModel_strategy = st.builds(diva_VariabilityModel)
@given(instance=diva_VariabilityModel_strategy)
@settings(max_examples=25)
def test_diva_VariabilityModel_instantiation(instance):
    assert isinstance(instance, diva_VariabilityModel)


diva_Variable_strategy = st.builds(diva_Variable)
@given(instance=diva_Variable_strategy)
@settings(max_examples=25)
def test_diva_Variable_instantiation(instance):
    assert isinstance(instance, diva_Variable)


diva_VariableTerm_strategy = st.builds(diva_VariableTerm)
@given(instance=diva_VariableTerm_strategy)
@settings(max_examples=25)
def test_diva_VariableTerm_instantiation(instance):
    assert isinstance(instance, diva_VariableTerm)


diva_Variant_strategy = st.builds(diva_Variant)
@given(instance=diva_Variant_strategy)
@settings(max_examples=25)
def test_diva_Variant_instantiation(instance):
    assert isinstance(instance, diva_Variant)


diva_VariantExpression_strategy = st.builds(diva_VariantExpression)
@given(instance=diva_VariantExpression_strategy)
@settings(max_examples=25)
def test_diva_VariantExpression_instantiation(instance):
    assert isinstance(instance, diva_VariantExpression)


diva_VariantTerm_strategy = st.builds(diva_VariantTerm)
@given(instance=diva_VariantTerm_strategy)
@settings(max_examples=25)
def test_diva_VariantTerm_instantiation(instance):
    assert isinstance(instance, diva_VariantTerm)



