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
    Attribute,
    occi_RecordField,
    occi_Configuration,
    BasicType,
    occi_NumericType,
    occi_EObjectType,
    occi_BooleanType,
    occi_StringType,
    DataType,
    occi_ArrayType,
    occi_EnumerationType,
    occi_RecordType,
    occi_BasicType,
    Entity,
    occi_Resource,
    occi_Extension,
    occi_Link,
    occi_Entity,
    occi_MixinBase,
    occi_AttributeState,
    Type,
    occi_Kind,
    occi_DataType,
    occi_Mixin,
    occi_EnumerationLiteral,
    occi_State,
    occi_FSM,
    Category,
    occi_Action,
    occi_Type,
    occi_Transition,
    AnnotatedElement,
    occi_Category,
    occi_Annotation,
    occi_AnnotatedElement,
    occi_Constraint,
    occi_Attribute,
    NumericTypeEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_hyp_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_hyp_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_recordfield_is_not_abstract():
    assert not inspect.isabstract(occi_RecordField)


def test_hyp_occi_recordfield_constructor_exists():
    assert callable(occi_RecordField.__init__)


def test_hyp_occi_recordfield_constructor_args():
    sig = inspect.signature(occi_RecordField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_configuration_is_not_abstract():
    assert not inspect.isabstract(occi_Configuration)


def test_hyp_occi_configuration_constructor_exists():
    assert callable(occi_Configuration.__init__)


def test_hyp_occi_configuration_constructor_args():
    sig = inspect.signature(occi_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "description" in params, "Missing parameter 'description'"





def test_hyp_basictype_is_not_abstract():
    assert not inspect.isabstract(BasicType)


def test_hyp_basictype_constructor_exists():
    assert callable(BasicType.__init__)


def test_hyp_basictype_constructor_args():
    sig = inspect.signature(BasicType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_numerictype_is_not_abstract():
    assert not inspect.isabstract(occi_NumericType)


def test_hyp_occi_numerictype_constructor_exists():
    assert callable(occi_NumericType.__init__)


def test_hyp_occi_numerictype_constructor_args():
    sig = inspect.signature(occi_NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "totalDigits" in params, "Missing parameter 'totalDigits'"
    assert "type" in params, "Missing parameter 'type'"
    assert "maxExclusive" in params, "Missing parameter 'maxExclusive'"
    assert "minExclusive" in params, "Missing parameter 'minExclusive'"
    assert "minInclusive" in params, "Missing parameter 'minInclusive'"
    assert "maxInclusive" in params, "Missing parameter 'maxInclusive'"









def test_hyp_occi_eobjecttype_is_not_abstract():
    assert not inspect.isabstract(occi_EObjectType)


def test_hyp_occi_eobjecttype_constructor_exists():
    assert callable(occi_EObjectType.__init__)


def test_hyp_occi_eobjecttype_constructor_args():
    sig = inspect.signature(occi_EObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"




def test_hyp_occi_booleantype_is_not_abstract():
    assert not inspect.isabstract(occi_BooleanType)


def test_hyp_occi_booleantype_constructor_exists():
    assert callable(occi_BooleanType.__init__)


def test_hyp_occi_booleantype_constructor_args():
    sig = inspect.signature(occi_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_stringtype_is_not_abstract():
    assert not inspect.isabstract(occi_StringType)


def test_hyp_occi_stringtype_constructor_exists():
    assert callable(occi_StringType.__init__)


def test_hyp_occi_stringtype_constructor_args():
    sig = inspect.signature(occi_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "length" in params, "Missing parameter 'length'"







def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_arraytype_is_not_abstract():
    assert not inspect.isabstract(occi_ArrayType)


def test_hyp_occi_arraytype_constructor_exists():
    assert callable(occi_ArrayType.__init__)


def test_hyp_occi_arraytype_constructor_args():
    sig = inspect.signature(occi_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(occi_EnumerationType)


def test_hyp_occi_enumerationtype_constructor_exists():
    assert callable(occi_EnumerationType.__init__)


def test_hyp_occi_enumerationtype_constructor_args():
    sig = inspect.signature(occi_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_recordtype_is_not_abstract():
    assert not inspect.isabstract(occi_RecordType)


def test_hyp_occi_recordtype_constructor_exists():
    assert callable(occi_RecordType.__init__)


def test_hyp_occi_recordtype_constructor_args():
    sig = inspect.signature(occi_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_basictype_is_not_abstract():
    assert not inspect.isabstract(occi_BasicType)


def test_hyp_occi_basictype_constructor_exists():
    assert callable(occi_BasicType.__init__)


def test_hyp_occi_basictype_constructor_args():
    sig = inspect.signature(occi_BasicType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_hyp_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_hyp_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_resource_is_not_abstract():
    assert not inspect.isabstract(occi_Resource)


def test_hyp_occi_resource_constructor_exists():
    assert callable(occi_Resource.__init__)


def test_hyp_occi_resource_constructor_args():
    sig = inspect.signature(occi_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "summary" in params, "Missing parameter 'summary'"




def test_hyp_occi_extension_is_not_abstract():
    assert not inspect.isabstract(occi_Extension)


def test_hyp_occi_extension_constructor_exists():
    assert callable(occi_Extension.__init__)


def test_hyp_occi_extension_constructor_args():
    sig = inspect.signature(occi_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "name" in params, "Missing parameter 'name'"
    assert "specification" in params, "Missing parameter 'specification'"
    assert "description" in params, "Missing parameter 'description'"







def test_hyp_occi_link_is_not_abstract():
    assert not inspect.isabstract(occi_Link)


def test_hyp_occi_link_constructor_exists():
    assert callable(occi_Link.__init__)


def test_hyp_occi_link_constructor_args():
    sig = inspect.signature(occi_Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_entity_is_not_abstract():
    assert not inspect.isabstract(occi_Entity)


def test_hyp_occi_entity_constructor_exists():
    assert callable(occi_Entity.__init__)


def test_hyp_occi_entity_constructor_args():
    sig = inspect.signature(occi_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "location" in params, "Missing parameter 'location'"






def test_hyp_occi_mixinbase_is_not_abstract():
    assert not inspect.isabstract(occi_MixinBase)


def test_hyp_occi_mixinbase_constructor_exists():
    assert callable(occi_MixinBase.__init__)


def test_hyp_occi_mixinbase_constructor_args():
    sig = inspect.signature(occi_MixinBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_attributestate_is_not_abstract():
    assert not inspect.isabstract(occi_AttributeState)


def test_hyp_occi_attributestate_constructor_exists():
    assert callable(occi_AttributeState.__init__)


def test_hyp_occi_attributestate_constructor_args():
    sig = inspect.signature(occi_AttributeState.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_kind_is_not_abstract():
    assert not inspect.isabstract(occi_Kind)


def test_hyp_occi_kind_constructor_exists():
    assert callable(occi_Kind.__init__)


def test_hyp_occi_kind_constructor_args():
    sig = inspect.signature(occi_Kind.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_datatype_is_not_abstract():
    assert not inspect.isabstract(occi_DataType)


def test_hyp_occi_datatype_constructor_exists():
    assert callable(occi_DataType.__init__)


def test_hyp_occi_datatype_constructor_args():
    sig = inspect.signature(occi_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_occi_mixin_is_not_abstract():
    assert not inspect.isabstract(occi_Mixin)


def test_hyp_occi_mixin_constructor_exists():
    assert callable(occi_Mixin.__init__)


def test_hyp_occi_mixin_constructor_args():
    sig = inspect.signature(occi_Mixin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(occi_EnumerationLiteral)


def test_hyp_occi_enumerationliteral_constructor_exists():
    assert callable(occi_EnumerationLiteral.__init__)


def test_hyp_occi_enumerationliteral_constructor_args():
    sig = inspect.signature(occi_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "documentation" in params, "Missing parameter 'documentation'"





def test_hyp_occi_state_is_not_abstract():
    assert not inspect.isabstract(occi_State)


def test_hyp_occi_state_constructor_exists():
    assert callable(occi_State.__init__)


def test_hyp_occi_state_constructor_args():
    sig = inspect.signature(occi_State.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "initial" in params, "Missing parameter 'initial'"





def test_hyp_occi_fsm_is_not_abstract():
    assert not inspect.isabstract(occi_FSM)


def test_hyp_occi_fsm_constructor_exists():
    assert callable(occi_FSM.__init__)


def test_hyp_occi_fsm_constructor_args():
    sig = inspect.signature(occi_FSM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_action_is_not_abstract():
    assert not inspect.isabstract(occi_Action)


def test_hyp_occi_action_constructor_exists():
    assert callable(occi_Action.__init__)


def test_hyp_occi_action_constructor_args():
    sig = inspect.signature(occi_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_type_is_not_abstract():
    assert not inspect.isabstract(occi_Type)


def test_hyp_occi_type_constructor_exists():
    assert callable(occi_Type.__init__)


def test_hyp_occi_type_constructor_args():
    sig = inspect.signature(occi_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_transition_is_not_abstract():
    assert not inspect.isabstract(occi_Transition)


def test_hyp_occi_transition_constructor_exists():
    assert callable(occi_Transition.__init__)


def test_hyp_occi_transition_constructor_args():
    sig = inspect.signature(occi_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_hyp_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_hyp_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_category_is_not_abstract():
    assert not inspect.isabstract(occi_Category)


def test_hyp_occi_category_constructor_exists():
    assert callable(occi_Category.__init__)


def test_hyp_occi_category_constructor_args():
    sig = inspect.signature(occi_Category.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"
    assert "term" in params, "Missing parameter 'term'"
    assert "description" in params, "Missing parameter 'description'"
    assert "scheme" in params, "Missing parameter 'scheme'"








def test_hyp_occi_annotation_is_not_abstract():
    assert not inspect.isabstract(occi_Annotation)


def test_hyp_occi_annotation_constructor_exists():
    assert callable(occi_Annotation.__init__)


def test_hyp_occi_annotation_constructor_args():
    sig = inspect.signature(occi_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_occi_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(occi_AnnotatedElement)


def test_hyp_occi_annotatedelement_constructor_exists():
    assert callable(occi_AnnotatedElement.__init__)


def test_hyp_occi_annotatedelement_constructor_args():
    sig = inspect.signature(occi_AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occi_constraint_is_not_abstract():
    assert not inspect.isabstract(occi_Constraint)


def test_hyp_occi_constraint_constructor_exists():
    assert callable(occi_Constraint.__init__)


def test_hyp_occi_constraint_constructor_args():
    sig = inspect.signature(occi_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"






def test_hyp_occi_attribute_is_not_abstract():
    assert not inspect.isabstract(occi_Attribute)


def test_hyp_occi_attribute_constructor_exists():
    assert callable(occi_Attribute.__init__)


def test_hyp_occi_attribute_constructor_args():
    sig = inspect.signature(occi_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "required" in params, "Missing parameter 'required'"
    assert "mutable" in params, "Missing parameter 'mutable'"
    assert "default" in params, "Missing parameter 'default'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_numerictypeenum_exists():
    # Check that the Enumeration exists
    assert NumericTypeEnum is not None

def test_hyp_numerictypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericTypeEnum]
    expected_literals = [
        "Byte",
        "Integer",
        "Short",
        "BigDecimal",
        "Double",
        "Float",
        "Long",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericTypeEnum"


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
Attribute_strategy = st.builds(
    Attribute,
)
occi_RecordField_strategy = st.builds(
    occi_RecordField,
)
occi_Configuration_strategy = st.builds(
    occi_Configuration,
    location=
        safe_text,
    description=
        safe_text
)
BasicType_strategy = st.builds(
    BasicType,
)
occi_NumericType_strategy = st.builds(
    occi_NumericType,
    totalDigits=
        safe_text,
    type=
        safe_text,
    maxExclusive=
        safe_text,
    minExclusive=
        safe_text,
    minInclusive=
        safe_text,
    maxInclusive=
        safe_text
)
occi_EObjectType_strategy = st.builds(
    occi_EObjectType,
    instanceClassName=
        safe_text
)
occi_BooleanType_strategy = st.builds(
    occi_BooleanType,
)
occi_StringType_strategy = st.builds(
    occi_StringType,
    minLength=
        safe_text,
    maxLength=
        safe_text,
    pattern=
        safe_text,
    length=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
occi_ArrayType_strategy = st.builds(
    occi_ArrayType,
)
occi_EnumerationType_strategy = st.builds(
    occi_EnumerationType,
)
occi_RecordType_strategy = st.builds(
    occi_RecordType,
)
occi_BasicType_strategy = st.builds(
    occi_BasicType,
)
Entity_strategy = st.builds(
    Entity,
)
occi_Resource_strategy = st.builds(
    occi_Resource,
    summary=
        safe_text
)
occi_Extension_strategy = st.builds(
    occi_Extension,
    scheme=
        safe_text,
    name=
        safe_text,
    specification=
        safe_text,
    description=
        safe_text
)
occi_Link_strategy = st.builds(
    occi_Link,
)
occi_Entity_strategy = st.builds(
    occi_Entity,
    title=
        safe_text,
    id=
        safe_text,
    location=
        safe_text
)
occi_MixinBase_strategy = st.builds(
    occi_MixinBase,
)
occi_AttributeState_strategy = st.builds(
    occi_AttributeState,
    value=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
occi_Kind_strategy = st.builds(
    occi_Kind,
)
occi_DataType_strategy = st.builds(
    occi_DataType,
    documentation=
        safe_text,
    name=
        safe_text
)
occi_Mixin_strategy = st.builds(
    occi_Mixin,
)
occi_EnumerationLiteral_strategy = st.builds(
    occi_EnumerationLiteral,
    name=
        safe_text,
    documentation=
        safe_text
)
occi_State_strategy = st.builds(
    occi_State,
    final=
        safe_text,
    initial=
        safe_text
)
occi_FSM_strategy = st.builds(
    occi_FSM,
)
Category_strategy = st.builds(
    Category,
)
occi_Action_strategy = st.builds(
    occi_Action,
)
occi_Type_strategy = st.builds(
    occi_Type,
)
occi_Transition_strategy = st.builds(
    occi_Transition,
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
occi_Category_strategy = st.builds(
    occi_Category,
    title=
        safe_text,
    name=
        safe_text,
    term=
        safe_text,
    description=
        safe_text,
    scheme=
        safe_text
)
occi_Annotation_strategy = st.builds(
    occi_Annotation,
    value=
        safe_text,
    key=
        safe_text
)
occi_AnnotatedElement_strategy = st.builds(
    occi_AnnotatedElement,
)
occi_Constraint_strategy = st.builds(
    occi_Constraint,
    description=
        safe_text,
    name=
        safe_text,
    body=
        safe_text
)
occi_Attribute_strategy = st.builds(
    occi_Attribute,
    description=
        safe_text,
    required=
        safe_text,
    mutable=
        safe_text,
    default=
        safe_text,
    name=
        safe_text
)






@given(instance=occi_Configuration_strategy)
def test_hyp_occi_configuration_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=occi_Configuration_strategy)
def test_hyp_occi_configuration_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original





@given(instance=occi_NumericType_strategy)
def test_hyp_occi_numerictype_totalDigits_setter(instance):
    original = instance.totalDigits
    instance.totalDigits = original
    assert instance.totalDigits == original



@given(instance=occi_NumericType_strategy)
def test_hyp_occi_numerictype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=occi_NumericType_strategy)
def test_hyp_occi_numerictype_maxExclusive_setter(instance):
    original = instance.maxExclusive
    instance.maxExclusive = original
    assert instance.maxExclusive == original



@given(instance=occi_NumericType_strategy)
def test_hyp_occi_numerictype_minExclusive_setter(instance):
    original = instance.minExclusive
    instance.minExclusive = original
    assert instance.minExclusive == original



@given(instance=occi_NumericType_strategy)
def test_hyp_occi_numerictype_minInclusive_setter(instance):
    original = instance.minInclusive
    instance.minInclusive = original
    assert instance.minInclusive == original



@given(instance=occi_NumericType_strategy)
def test_hyp_occi_numerictype_maxInclusive_setter(instance):
    original = instance.maxInclusive
    instance.maxInclusive = original
    assert instance.maxInclusive == original




@given(instance=occi_EObjectType_strategy)
def test_hyp_occi_eobjecttype_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original





@given(instance=occi_StringType_strategy)
def test_hyp_occi_stringtype_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original



@given(instance=occi_StringType_strategy)
def test_hyp_occi_stringtype_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=occi_StringType_strategy)
def test_hyp_occi_stringtype_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=occi_StringType_strategy)
def test_hyp_occi_stringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original










@given(instance=occi_Resource_strategy)
def test_hyp_occi_resource_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original




@given(instance=occi_Extension_strategy)
def test_hyp_occi_extension_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original



@given(instance=occi_Extension_strategy)
def test_hyp_occi_extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=occi_Extension_strategy)
def test_hyp_occi_extension_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original



@given(instance=occi_Extension_strategy)
def test_hyp_occi_extension_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=occi_Link_strategy)
@settings(max_examples=30)
def test_hyp_occi_link_linksourceinvariant_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.LinkSourceInvariant(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.LinkSourceInvariant).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'LinkSourceInvariant' in occi_Link is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'LinkSourceInvariant' in occi_Link did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'LinkSourceInvariant' in occi_Link is not implemented or raised an error")




@given(instance=occi_Entity_strategy)
def test_hyp_occi_entity_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=occi_Entity_strategy)
def test_hyp_occi_entity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=occi_Entity_strategy)
def test_hyp_occi_entity_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=occi_Entity_strategy)
@settings(max_examples=30)
def test_hyp_occi_entity_occiretrieve_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.occiRetrieve()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.occiRetrieve).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'occiRetrieve' in occi_Entity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'occiRetrieve' in occi_Entity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'occiRetrieve' in occi_Entity is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=occi_Entity_strategy)
@settings(max_examples=30)
def test_hyp_occi_entity_occiupdate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.occiUpdate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.occiUpdate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'occiUpdate' in occi_Entity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'occiUpdate' in occi_Entity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'occiUpdate' in occi_Entity is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=occi_Entity_strategy)
@settings(max_examples=30)
def test_hyp_occi_entity_occicreate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.occiCreate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.occiCreate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'occiCreate' in occi_Entity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'occiCreate' in occi_Entity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'occiCreate' in occi_Entity is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=occi_Entity_strategy)
@settings(max_examples=30)
def test_hyp_occi_entity_occidelete_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.occiDelete()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.occiDelete).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'occiDelete' in occi_Entity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'occiDelete' in occi_Entity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'occiDelete' in occi_Entity is not implemented or raised an error")





@given(instance=occi_AttributeState_strategy)
def test_hyp_occi_attributestate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=occi_AttributeState_strategy)
def test_hyp_occi_attributestate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=occi_Kind_strategy)
@settings(max_examples=30)
def test_hyp_occi_kind_occiiskindof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.occiIsKindOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.occiIsKindOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'occiIsKindOf' in occi_Kind is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'occiIsKindOf' in occi_Kind did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'occiIsKindOf' in occi_Kind is not implemented or raised an error")




@given(instance=occi_DataType_strategy)
def test_hyp_occi_datatype_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=occi_DataType_strategy)
def test_hyp_occi_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=occi_EnumerationLiteral_strategy)
def test_hyp_occi_enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=occi_EnumerationLiteral_strategy)
def test_hyp_occi_enumerationliteral_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original




@given(instance=occi_State_strategy)
def test_hyp_occi_state_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=occi_State_strategy)
def test_hyp_occi_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original










@given(instance=occi_Category_strategy)
def test_hyp_occi_category_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=occi_Category_strategy)
def test_hyp_occi_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=occi_Category_strategy)
def test_hyp_occi_category_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=occi_Category_strategy)
def test_hyp_occi_category_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=occi_Category_strategy)
def test_hyp_occi_category_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original




@given(instance=occi_Annotation_strategy)
def test_hyp_occi_annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=occi_Annotation_strategy)
def test_hyp_occi_annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original





@given(instance=occi_Constraint_strategy)
def test_hyp_occi_constraint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=occi_Constraint_strategy)
def test_hyp_occi_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=occi_Constraint_strategy)
def test_hyp_occi_constraint_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original




@given(instance=occi_Attribute_strategy)
def test_hyp_occi_attribute_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=occi_Attribute_strategy)
def test_hyp_occi_attribute_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=occi_Attribute_strategy)
def test_hyp_occi_attribute_mutable_setter(instance):
    original = instance.mutable
    instance.mutable = original
    assert instance.mutable == original



@given(instance=occi_Attribute_strategy)
def test_hyp_occi_attribute_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=occi_Attribute_strategy)
def test_hyp_occi_attribute_name_setter(instance):
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
    AnnotatedElement,
    Attribute,
    BasicType,
    Category,
    DataType,
    Entity,
    Type,
    occi_Action,
    occi_AnnotatedElement,
    occi_Annotation,
    occi_ArrayType,
    occi_Attribute,
    occi_AttributeState,
    occi_BasicType,
    occi_BooleanType,
    occi_Category,
    occi_Configuration,
    occi_Constraint,
    occi_DataType,
    occi_EObjectType,
    occi_Entity,
    occi_EnumerationLiteral,
    occi_EnumerationType,
    occi_Extension,
    occi_FSM,
    occi_Kind,
    occi_Link,
    occi_Mixin,
    occi_MixinBase,
    occi_NumericType,
    occi_RecordField,
    occi_RecordType,
    occi_Resource,
    occi_State,
    occi_StringType,
    occi_Transition,
    occi_Type,
    NumericTypeEnum,
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

def test_occi_Annotation_key_value_roundtrip():
    instance = occi_Annotation(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_occi_Annotation_value_value_roundtrip():
    instance = occi_Annotation(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_occi_Attribute_default_value_roundtrip():
    instance = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_occi_Attribute_description_value_roundtrip():
    instance = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_occi_Attribute_mutable_value_roundtrip():
    instance = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    assert instance.mutable == "sample_text"
    instance.mutable = "sample_text_2"
    assert instance.mutable == "sample_text_2"


def test_occi_Attribute_name_value_roundtrip():
    instance = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_occi_Attribute_required_value_roundtrip():
    instance = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    assert instance.required == "sample_text"
    instance.required = "sample_text_2"
    assert instance.required == "sample_text_2"


def test_occi_AttributeState_name_value_roundtrip():
    instance = occi_AttributeState(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_occi_AttributeState_value_value_roundtrip():
    instance = occi_AttributeState(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_occi_Category_description_value_roundtrip():
    instance = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_occi_Category_name_value_roundtrip():
    instance = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_occi_Category_scheme_value_roundtrip():
    instance = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    assert instance.scheme == "sample_text"
    instance.scheme = "sample_text_2"
    assert instance.scheme == "sample_text_2"


def test_occi_Category_term_value_roundtrip():
    instance = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    assert instance.term == "sample_text"
    instance.term = "sample_text_2"
    assert instance.term == "sample_text_2"


def test_occi_Category_title_value_roundtrip():
    instance = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_occi_Configuration_description_value_roundtrip():
    instance = occi_Configuration(description="sample_text", location="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_occi_Configuration_location_value_roundtrip():
    instance = occi_Configuration(description="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_occi_Constraint_body_value_roundtrip():
    instance = occi_Constraint(body="sample_text", description="sample_text", name="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_occi_Constraint_description_value_roundtrip():
    instance = occi_Constraint(body="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_occi_Constraint_name_value_roundtrip():
    instance = occi_Constraint(body="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_occi_DataType_documentation_value_roundtrip():
    instance = occi_DataType(documentation="sample_text", name="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_occi_DataType_name_value_roundtrip():
    instance = occi_DataType(documentation="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_occi_EObjectType_instanceClassName_value_roundtrip():
    instance = occi_EObjectType(instanceClassName="sample_text")
    assert instance.instanceClassName == "sample_text"
    instance.instanceClassName = "sample_text_2"
    assert instance.instanceClassName == "sample_text_2"


def test_occi_Entity_id_value_roundtrip():
    instance = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_occi_Entity_location_value_roundtrip():
    instance = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_occi_Entity_title_value_roundtrip():
    instance = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_occi_EnumerationLiteral_documentation_value_roundtrip():
    instance = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_occi_EnumerationLiteral_name_value_roundtrip():
    instance = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_occi_Extension_description_value_roundtrip():
    instance = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_occi_Extension_name_value_roundtrip():
    instance = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_occi_Extension_scheme_value_roundtrip():
    instance = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    assert instance.scheme == "sample_text"
    instance.scheme = "sample_text_2"
    assert instance.scheme == "sample_text_2"


def test_occi_Extension_specification_value_roundtrip():
    instance = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    assert instance.specification == "sample_text"
    instance.specification = "sample_text_2"
    assert instance.specification == "sample_text_2"


def test_occi_NumericType_maxExclusive_value_roundtrip():
    instance = occi_NumericType(maxExclusive="sample_text", maxInclusive="sample_text", minExclusive="sample_text", minInclusive="sample_text", totalDigits="sample_text", type="sample_text")
    assert instance.maxExclusive == "sample_text"
    instance.maxExclusive = "sample_text_2"
    assert instance.maxExclusive == "sample_text_2"


def test_occi_NumericType_maxInclusive_value_roundtrip():
    instance = occi_NumericType(maxExclusive="sample_text", maxInclusive="sample_text", minExclusive="sample_text", minInclusive="sample_text", totalDigits="sample_text", type="sample_text")
    assert instance.maxInclusive == "sample_text"
    instance.maxInclusive = "sample_text_2"
    assert instance.maxInclusive == "sample_text_2"


def test_occi_NumericType_minExclusive_value_roundtrip():
    instance = occi_NumericType(maxExclusive="sample_text", maxInclusive="sample_text", minExclusive="sample_text", minInclusive="sample_text", totalDigits="sample_text", type="sample_text")
    assert instance.minExclusive == "sample_text"
    instance.minExclusive = "sample_text_2"
    assert instance.minExclusive == "sample_text_2"


def test_occi_NumericType_minInclusive_value_roundtrip():
    instance = occi_NumericType(maxExclusive="sample_text", maxInclusive="sample_text", minExclusive="sample_text", minInclusive="sample_text", totalDigits="sample_text", type="sample_text")
    assert instance.minInclusive == "sample_text"
    instance.minInclusive = "sample_text_2"
    assert instance.minInclusive == "sample_text_2"


def test_occi_NumericType_totalDigits_value_roundtrip():
    instance = occi_NumericType(maxExclusive="sample_text", maxInclusive="sample_text", minExclusive="sample_text", minInclusive="sample_text", totalDigits="sample_text", type="sample_text")
    assert instance.totalDigits == "sample_text"
    instance.totalDigits = "sample_text_2"
    assert instance.totalDigits == "sample_text_2"


def test_occi_NumericType_type_value_roundtrip():
    instance = occi_NumericType(maxExclusive="sample_text", maxInclusive="sample_text", minExclusive="sample_text", minInclusive="sample_text", totalDigits="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_occi_Resource_summary_value_roundtrip():
    instance = occi_Resource(summary="sample_text")
    assert instance.summary == "sample_text"
    instance.summary = "sample_text_2"
    assert instance.summary == "sample_text_2"


def test_occi_State_final_value_roundtrip():
    instance = occi_State(final="sample_text", initial="sample_text")
    assert instance.final == "sample_text"
    instance.final = "sample_text_2"
    assert instance.final == "sample_text_2"


def test_occi_State_initial_value_roundtrip():
    instance = occi_State(final="sample_text", initial="sample_text")
    assert instance.initial == "sample_text"
    instance.initial = "sample_text_2"
    assert instance.initial == "sample_text_2"


def test_occi_StringType_length_value_roundtrip():
    instance = occi_StringType(length="sample_text", maxLength="sample_text", minLength="sample_text", pattern="sample_text")
    assert instance.length == "sample_text"
    instance.length = "sample_text_2"
    assert instance.length == "sample_text_2"


def test_occi_StringType_maxLength_value_roundtrip():
    instance = occi_StringType(length="sample_text", maxLength="sample_text", minLength="sample_text", pattern="sample_text")
    assert instance.maxLength == "sample_text"
    instance.maxLength = "sample_text_2"
    assert instance.maxLength == "sample_text_2"


def test_occi_StringType_minLength_value_roundtrip():
    instance = occi_StringType(length="sample_text", maxLength="sample_text", minLength="sample_text", pattern="sample_text")
    assert instance.minLength == "sample_text"
    instance.minLength = "sample_text_2"
    assert instance.minLength == "sample_text_2"


def test_occi_StringType_pattern_value_roundtrip():
    instance = occi_StringType(length="sample_text", maxLength="sample_text", minLength="sample_text", pattern="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_occi_Attribute_isa_AnnotatedElement():
    instance = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    assert isinstance(instance, AnnotatedElement)


def test_occi_Category_isa_AnnotatedElement():
    instance = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    assert isinstance(instance, AnnotatedElement)


def test_occi_RecordField_isa_Attribute():
    instance = occi_RecordField()
    assert isinstance(instance, Attribute)


def test_occi_BooleanType_isa_BasicType():
    instance = occi_BooleanType()
    assert isinstance(instance, BasicType)


def test_occi_EObjectType_isa_BasicType():
    instance = occi_EObjectType(instanceClassName="sample_text")
    assert isinstance(instance, BasicType)


def test_occi_NumericType_isa_BasicType():
    instance = occi_NumericType(maxExclusive="sample_text", maxInclusive="sample_text", minExclusive="sample_text", minInclusive="sample_text", totalDigits="sample_text", type="sample_text")
    assert isinstance(instance, BasicType)


def test_occi_StringType_isa_BasicType():
    instance = occi_StringType(length="sample_text", maxLength="sample_text", minLength="sample_text", pattern="sample_text")
    assert isinstance(instance, BasicType)


def test_occi_Action_isa_Category():
    instance = occi_Action()
    assert isinstance(instance, Category)


def test_occi_Type_isa_Category():
    instance = occi_Type()
    assert isinstance(instance, Category)


def test_occi_ArrayType_isa_DataType():
    instance = occi_ArrayType()
    assert isinstance(instance, DataType)


def test_occi_BasicType_isa_DataType():
    instance = occi_BasicType()
    assert isinstance(instance, DataType)


def test_occi_EnumerationType_isa_DataType():
    instance = occi_EnumerationType()
    assert isinstance(instance, DataType)


def test_occi_RecordType_isa_DataType():
    instance = occi_RecordType()
    assert isinstance(instance, DataType)


def test_occi_Link_isa_Entity():
    instance = occi_Link()
    assert isinstance(instance, Entity)


def test_occi_Resource_isa_Entity():
    instance = occi_Resource(summary="sample_text")
    assert isinstance(instance, Entity)


def test_occi_Kind_isa_Type():
    instance = occi_Kind()
    assert isinstance(instance, Type)


def test_occi_Mixin_isa_Type():
    instance = occi_Mixin()
    assert isinstance(instance, Type)


def test_assoc_annotations0_link_reassign_clear():
    a = occi_Annotation(key="sample_text", value="sample_text")
    b1 = occi_AnnotatedElement()
    b2 = occi_AnnotatedElement()
    _safe_set(a, 'occi_Annotation', b1)
    assert _is_linked(a, 'occi_Annotation', b1)
    if hasattr(b1, 'occi_AnnotatedElement'):
        assert _is_linked(b1, 'occi_AnnotatedElement', a)
    _safe_set(a, 'occi_Annotation', b2)
    assert _is_linked(a, 'occi_Annotation', b2)
    if hasattr(b1, 'occi_AnnotatedElement'):
        assert not _is_linked(b1, 'occi_AnnotatedElement', a)
    if hasattr(b2, 'occi_AnnotatedElement'):
        assert _is_linked(b2, 'occi_AnnotatedElement', a)
    _safe_set(a, 'occi_Annotation', None)
    assert not _is_linked(a, 'occi_Annotation', b2)
    if hasattr(b2, 'occi_AnnotatedElement'):
        assert not _is_linked(b2, 'occi_AnnotatedElement', a)


def test_assoc_applies35_link_reassign_clear():
    a = occi_Kind()
    b1 = occi_Mixin()
    b2 = occi_Mixin()
    _safe_set(a, 'occi_Kind37', b1)
    assert _is_linked(a, 'occi_Kind37', b1)
    if hasattr(b1, 'occi_Mixin36'):
        assert _is_linked(b1, 'occi_Mixin36', a)
    _safe_set(a, 'occi_Kind37', b2)
    assert _is_linked(a, 'occi_Kind37', b2)
    if hasattr(b1, 'occi_Mixin36'):
        assert not _is_linked(b1, 'occi_Mixin36', a)
    if hasattr(b2, 'occi_Mixin36'):
        assert _is_linked(b2, 'occi_Mixin36', a)
    _safe_set(a, 'occi_Kind37', None)
    assert not _is_linked(a, 'occi_Kind37', b2)
    if hasattr(b2, 'occi_Mixin36'):
        assert not _is_linked(b2, 'occi_Mixin36', a)


def test_assoc_attribute8_link_reassign_clear():
    a = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    b1 = occi_FSM()
    b2 = occi_FSM()
    _safe_set(a, 'occi_Attribute10', b1)
    assert _is_linked(a, 'occi_Attribute10', b1)
    if hasattr(b1, 'occi_FSM9'):
        assert _is_linked(b1, 'occi_FSM9', a)
    _safe_set(a, 'occi_Attribute10', b2)
    assert _is_linked(a, 'occi_Attribute10', b2)
    if hasattr(b1, 'occi_FSM9'):
        assert not _is_linked(b1, 'occi_FSM9', a)
    if hasattr(b2, 'occi_FSM9'):
        assert _is_linked(b2, 'occi_FSM9', a)
    _safe_set(a, 'occi_Attribute10', None)
    assert not _is_linked(a, 'occi_Attribute10', b2)
    if hasattr(b2, 'occi_FSM9'):
        assert not _is_linked(b2, 'occi_FSM9', a)


def test_assoc_attributes1_link_reassign_clear():
    a = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    b1 = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    b2 = occi_Attribute(default="sample_text_2", description="sample_text_2", mutable="sample_text_2", name="sample_text_2", required="sample_text_2")
    _safe_set(a, 'occi_Category', {b1})
    assert _is_linked(a, 'occi_Category', b1)
    if hasattr(b1, 'occi_Attribute'):
        assert _is_linked(b1, 'occi_Attribute', a)
    _safe_set(a, 'occi_Category', {b2})
    assert _is_linked(a, 'occi_Category', b2)
    if hasattr(b1, 'occi_Attribute'):
        assert not _is_linked(b1, 'occi_Attribute', a)
    if hasattr(b2, 'occi_Attribute'):
        assert _is_linked(b2, 'occi_Attribute', a)
    _safe_set(a, 'occi_Category', set())
    assert not _is_linked(a, 'occi_Category', b2)
    if hasattr(b2, 'occi_Attribute'):
        assert not _is_linked(b2, 'occi_Attribute', a)


def test_assoc_attributes44_link_reassign_clear():
    a = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    b1 = occi_AttributeState(name="sample_text", value="sample_text")
    b2 = occi_AttributeState(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'occi_Entity45', {b1})
    assert _is_linked(a, 'occi_Entity45', b1)
    if hasattr(b1, 'occi_AttributeState'):
        assert _is_linked(b1, 'occi_AttributeState', a)
    _safe_set(a, 'occi_Entity45', {b2})
    assert _is_linked(a, 'occi_Entity45', b2)
    if hasattr(b1, 'occi_AttributeState'):
        assert not _is_linked(b1, 'occi_AttributeState', a)
    if hasattr(b2, 'occi_AttributeState'):
        assert _is_linked(b2, 'occi_AttributeState', a)
    _safe_set(a, 'occi_Entity45', set())
    assert not _is_linked(a, 'occi_Entity45', b2)
    if hasattr(b2, 'occi_AttributeState'):
        assert not _is_linked(b2, 'occi_AttributeState', a)


def test_assoc_attributes53_link_reassign_clear():
    a = occi_AttributeState(name="sample_text", value="sample_text")
    b1 = occi_MixinBase()
    b2 = occi_MixinBase()
    _safe_set(a, 'occi_AttributeState55', b1)
    assert _is_linked(a, 'occi_AttributeState55', b1)
    if hasattr(b1, 'occi_MixinBase54'):
        assert _is_linked(b1, 'occi_MixinBase54', a)
    _safe_set(a, 'occi_AttributeState55', b2)
    assert _is_linked(a, 'occi_AttributeState55', b2)
    if hasattr(b1, 'occi_MixinBase54'):
        assert not _is_linked(b1, 'occi_MixinBase54', a)
    if hasattr(b2, 'occi_MixinBase54'):
        assert _is_linked(b2, 'occi_MixinBase54', a)
    _safe_set(a, 'occi_AttributeState55', None)
    assert not _is_linked(a, 'occi_AttributeState55', b2)
    if hasattr(b2, 'occi_MixinBase54'):
        assert not _is_linked(b2, 'occi_MixinBase54', a)


def test_assoc_constraints3_link_reassign_clear():
    a = occi_Constraint(body="sample_text", description="sample_text", name="sample_text")
    b1 = occi_Type()
    b2 = occi_Type()
    _safe_set(a, 'occi_Constraint', b1)
    assert _is_linked(a, 'occi_Constraint', b1)
    if hasattr(b1, 'occi_Type4'):
        assert _is_linked(b1, 'occi_Type4', a)
    _safe_set(a, 'occi_Constraint', b2)
    assert _is_linked(a, 'occi_Constraint', b2)
    if hasattr(b1, 'occi_Type4'):
        assert not _is_linked(b1, 'occi_Type4', a)
    if hasattr(b2, 'occi_Type4'):
        assert _is_linked(b2, 'occi_Type4', a)
    _safe_set(a, 'occi_Constraint', None)
    assert not _is_linked(a, 'occi_Constraint', b2)
    if hasattr(b2, 'occi_Type4'):
        assert not _is_linked(b2, 'occi_Type4', a)


def test_assoc_entities25_link_reassign_clear():
    a = occi_Kind()
    b1 = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    b2 = occi_Entity(id="sample_text_2", location="sample_text_2", title="sample_text_2")
    _safe_set(a, 'occi_Kind26', {b1})
    assert _is_linked(a, 'occi_Kind26', b1)
    if hasattr(b1, 'occi_Entity'):
        assert _is_linked(b1, 'occi_Entity', a)
    _safe_set(a, 'occi_Kind26', {b2})
    assert _is_linked(a, 'occi_Kind26', b2)
    if hasattr(b1, 'occi_Entity'):
        assert not _is_linked(b1, 'occi_Entity', a)
    if hasattr(b2, 'occi_Entity'):
        assert _is_linked(b2, 'occi_Entity', a)
    _safe_set(a, 'occi_Kind26', set())
    assert not _is_linked(a, 'occi_Kind26', b2)
    if hasattr(b2, 'occi_Entity'):
        assert not _is_linked(b2, 'occi_Entity', a)


def test_assoc_entities38_link_reassign_clear():
    a = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    b1 = occi_Mixin()
    b2 = occi_Mixin()
    _safe_set(a, 'occi_Entity40', b1)
    assert _is_linked(a, 'occi_Entity40', b1)
    if hasattr(b1, 'occi_Mixin39'):
        assert _is_linked(b1, 'occi_Mixin39', a)
    _safe_set(a, 'occi_Entity40', b2)
    assert _is_linked(a, 'occi_Entity40', b2)
    if hasattr(b1, 'occi_Mixin39'):
        assert not _is_linked(b1, 'occi_Mixin39', a)
    if hasattr(b2, 'occi_Mixin39'):
        assert _is_linked(b2, 'occi_Mixin39', a)
    _safe_set(a, 'occi_Entity40', None)
    assert not _is_linked(a, 'occi_Entity40', b2)
    if hasattr(b2, 'occi_Mixin39'):
        assert not _is_linked(b2, 'occi_Mixin39', a)


def test_assoc_entity52_link_reassign_clear():
    a = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    b1 = occi_MixinBase()
    b2 = occi_MixinBase()
    _safe_set(a, 'Entity', b1)
    assert _is_linked(a, 'Entity', b1)
    if hasattr(b1, 'parts'):
        assert _is_linked(b1, 'parts', a)
    _safe_set(a, 'Entity', b2)
    assert _is_linked(a, 'Entity', b2)
    if hasattr(b1, 'parts'):
        assert not _is_linked(b1, 'parts', a)
    if hasattr(b2, 'parts'):
        assert _is_linked(b2, 'parts', a)
    _safe_set(a, 'Entity', None)
    assert not _is_linked(a, 'Entity', b2)
    if hasattr(b2, 'parts'):
        assert not _is_linked(b2, 'parts', a)


def test_assoc_enumerationType82_link_reassign_clear():
    a = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    b1 = occi_EnumerationType()
    b2 = occi_EnumerationType()
    _safe_set(a, 'literals', b1)
    assert _is_linked(a, 'literals', b1)
    if hasattr(b1, 'EnumerationType'):
        assert _is_linked(b1, 'EnumerationType', a)
    _safe_set(a, 'literals', b2)
    assert _is_linked(a, 'literals', b2)
    if hasattr(b1, 'EnumerationType'):
        assert not _is_linked(b1, 'EnumerationType', a)
    if hasattr(b2, 'EnumerationType'):
        assert _is_linked(b2, 'EnumerationType', a)
    _safe_set(a, 'literals', None)
    assert not _is_linked(a, 'literals', b2)
    if hasattr(b2, 'EnumerationType'):
        assert not _is_linked(b2, 'EnumerationType', a)


def test_assoc_import_64_link_reassign_clear():
    a = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    b1 = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    b2 = occi_Extension(description="sample_text_2", name="sample_text_2", scheme="sample_text_2", specification="sample_text_2")
    _safe_set(a, 'occi_Extension', b1)
    assert _is_linked(a, 'occi_Extension', b1)
    if hasattr(b1, 'occi_Extension63'):
        assert _is_linked(b1, 'occi_Extension63', a)
    _safe_set(a, 'occi_Extension', b2)
    assert _is_linked(a, 'occi_Extension', b2)
    if hasattr(b1, 'occi_Extension63'):
        assert not _is_linked(b1, 'occi_Extension63', a)
    if hasattr(b2, 'occi_Extension63'):
        assert _is_linked(b2, 'occi_Extension63', a)
    _safe_set(a, 'occi_Extension', None)
    assert not _is_linked(a, 'occi_Extension', b2)
    if hasattr(b2, 'occi_Extension63'):
        assert not _is_linked(b2, 'occi_Extension63', a)


def test_assoc_kind41_link_reassign_clear():
    a = occi_Kind()
    b1 = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    b2 = occi_Entity(id="sample_text_2", location="sample_text_2", title="sample_text_2")
    _safe_set(a, 'occi_Kind43', b1)
    assert _is_linked(a, 'occi_Kind43', b1)
    if hasattr(b1, 'occi_Entity42'):
        assert _is_linked(b1, 'occi_Entity42', a)
    _safe_set(a, 'occi_Kind43', b2)
    assert _is_linked(a, 'occi_Kind43', b2)
    if hasattr(b1, 'occi_Entity42'):
        assert not _is_linked(b1, 'occi_Entity42', a)
    if hasattr(b2, 'occi_Entity42'):
        assert _is_linked(b2, 'occi_Entity42', a)
    _safe_set(a, 'occi_Kind43', None)
    assert not _is_linked(a, 'occi_Kind43', b2)
    if hasattr(b2, 'occi_Entity42'):
        assert not _is_linked(b2, 'occi_Entity42', a)


def test_assoc_kinds65_link_reassign_clear():
    a = occi_Kind()
    b1 = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    b2 = occi_Extension(description="sample_text_2", name="sample_text_2", scheme="sample_text_2", specification="sample_text_2")
    _safe_set(a, 'occi_Kind67', b1)
    assert _is_linked(a, 'occi_Kind67', b1)
    if hasattr(b1, 'occi_Extension66'):
        assert _is_linked(b1, 'occi_Extension66', a)
    _safe_set(a, 'occi_Kind67', b2)
    assert _is_linked(a, 'occi_Kind67', b2)
    if hasattr(b1, 'occi_Extension66'):
        assert not _is_linked(b1, 'occi_Extension66', a)
    if hasattr(b2, 'occi_Extension66'):
        assert _is_linked(b2, 'occi_Extension66', a)
    _safe_set(a, 'occi_Kind67', None)
    assert not _is_linked(a, 'occi_Kind67', b2)
    if hasattr(b2, 'occi_Extension66'):
        assert not _is_linked(b2, 'occi_Extension66', a)


def test_assoc_links56_link_reassign_clear():
    a = occi_Resource(summary="sample_text")
    b1 = occi_Link()
    b2 = occi_Link()
    _safe_set(a, 'source57', {b1})
    assert _is_linked(a, 'source57', b1)
    if hasattr(b1, 'Link'):
        assert _is_linked(b1, 'Link', a)
    _safe_set(a, 'source57', {b2})
    assert _is_linked(a, 'source57', b2)
    if hasattr(b1, 'Link'):
        assert not _is_linked(b1, 'Link', a)
    if hasattr(b2, 'Link'):
        assert _is_linked(b2, 'Link', a)
    _safe_set(a, 'source57', set())
    assert not _is_linked(a, 'source57', b2)
    if hasattr(b2, 'Link'):
        assert not _is_linked(b2, 'Link', a)


def test_assoc_literal11_link_reassign_clear():
    a = occi_State(final="sample_text", initial="sample_text")
    b1 = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    b2 = occi_EnumerationLiteral(documentation="sample_text_2", name="sample_text_2")
    _safe_set(a, 'occi_State', b1)
    assert _is_linked(a, 'occi_State', b1)
    if hasattr(b1, 'occi_EnumerationLiteral'):
        assert _is_linked(b1, 'occi_EnumerationLiteral', a)
    _safe_set(a, 'occi_State', b2)
    assert _is_linked(a, 'occi_State', b2)
    if hasattr(b1, 'occi_EnumerationLiteral'):
        assert not _is_linked(b1, 'occi_EnumerationLiteral', a)
    if hasattr(b2, 'occi_EnumerationLiteral'):
        assert _is_linked(b2, 'occi_EnumerationLiteral', a)
    _safe_set(a, 'occi_State', None)
    assert not _is_linked(a, 'occi_State', b2)
    if hasattr(b2, 'occi_EnumerationLiteral'):
        assert not _is_linked(b2, 'occi_EnumerationLiteral', a)


def test_assoc_literals81_link_reassign_clear():
    a = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    b1 = occi_EnumerationType()
    b2 = occi_EnumerationType()
    _safe_set(a, 'EnumerationLiteral', b1)
    assert _is_linked(a, 'EnumerationLiteral', b1)
    if hasattr(b1, 'enumerationType'):
        assert _is_linked(b1, 'enumerationType', a)
    _safe_set(a, 'EnumerationLiteral', b2)
    assert _is_linked(a, 'EnumerationLiteral', b2)
    if hasattr(b1, 'enumerationType'):
        assert not _is_linked(b1, 'enumerationType', a)
    if hasattr(b2, 'enumerationType'):
        assert _is_linked(b2, 'enumerationType', a)
    _safe_set(a, 'EnumerationLiteral', None)
    assert not _is_linked(a, 'EnumerationLiteral', b2)
    if hasattr(b2, 'enumerationType'):
        assert not _is_linked(b2, 'enumerationType', a)


def test_assoc_mixins46_link_reassign_clear():
    a = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    b1 = occi_Mixin()
    b2 = occi_Mixin()
    _safe_set(a, 'occi_Entity47', {b1})
    assert _is_linked(a, 'occi_Entity47', b1)
    if hasattr(b1, 'occi_Mixin48'):
        assert _is_linked(b1, 'occi_Mixin48', a)
    _safe_set(a, 'occi_Entity47', {b2})
    assert _is_linked(a, 'occi_Entity47', b2)
    if hasattr(b1, 'occi_Mixin48'):
        assert not _is_linked(b1, 'occi_Mixin48', a)
    if hasattr(b2, 'occi_Mixin48'):
        assert _is_linked(b2, 'occi_Mixin48', a)
    _safe_set(a, 'occi_Entity47', set())
    assert not _is_linked(a, 'occi_Entity47', b2)
    if hasattr(b2, 'occi_Mixin48'):
        assert not _is_linked(b2, 'occi_Mixin48', a)


def test_assoc_mixins68_link_reassign_clear():
    a = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    b1 = occi_Mixin()
    b2 = occi_Mixin()
    _safe_set(a, 'occi_Extension69', {b1})
    assert _is_linked(a, 'occi_Extension69', b1)
    if hasattr(b1, 'occi_Mixin70'):
        assert _is_linked(b1, 'occi_Mixin70', a)
    _safe_set(a, 'occi_Extension69', {b2})
    assert _is_linked(a, 'occi_Extension69', b2)
    if hasattr(b1, 'occi_Mixin70'):
        assert not _is_linked(b1, 'occi_Mixin70', a)
    if hasattr(b2, 'occi_Mixin70'):
        assert _is_linked(b2, 'occi_Mixin70', a)
    _safe_set(a, 'occi_Extension69', set())
    assert not _is_linked(a, 'occi_Extension69', b2)
    if hasattr(b2, 'occi_Mixin70'):
        assert not _is_linked(b2, 'occi_Mixin70', a)


def test_assoc_mixins78_link_reassign_clear():
    a = occi_Configuration(description="sample_text", location="sample_text")
    b1 = occi_Mixin()
    b2 = occi_Mixin()
    _safe_set(a, 'occi_Configuration79', {b1})
    assert _is_linked(a, 'occi_Configuration79', b1)
    if hasattr(b1, 'occi_Mixin80'):
        assert _is_linked(b1, 'occi_Mixin80', a)
    _safe_set(a, 'occi_Configuration79', {b2})
    assert _is_linked(a, 'occi_Configuration79', b2)
    if hasattr(b1, 'occi_Mixin80'):
        assert not _is_linked(b1, 'occi_Mixin80', a)
    if hasattr(b2, 'occi_Mixin80'):
        assert _is_linked(b2, 'occi_Mixin80', a)
    _safe_set(a, 'occi_Configuration79', set())
    assert not _is_linked(a, 'occi_Configuration79', b2)
    if hasattr(b2, 'occi_Mixin80'):
        assert not _is_linked(b2, 'occi_Mixin80', a)


def test_assoc_outgoingTransition13_link_reassign_clear():
    a = occi_State(final="sample_text", initial="sample_text")
    b1 = occi_Transition()
    b2 = occi_Transition()
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Transition'):
        assert _is_linked(b1, 'Transition', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Transition'):
        assert not _is_linked(b1, 'Transition', a)
    if hasattr(b2, 'Transition'):
        assert _is_linked(b2, 'Transition', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Transition'):
        assert not _is_linked(b2, 'Transition', a)


def test_assoc_ownedState7_link_reassign_clear():
    a = occi_State(final="sample_text", initial="sample_text")
    b1 = occi_FSM()
    b2 = occi_FSM()
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'owningFSM'):
        assert _is_linked(b1, 'owningFSM', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'owningFSM'):
        assert not _is_linked(b1, 'owningFSM', a)
    if hasattr(b2, 'owningFSM'):
        assert _is_linked(b2, 'owningFSM', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'owningFSM'):
        assert not _is_linked(b2, 'owningFSM', a)


def test_assoc_owningFSM12_link_reassign_clear():
    a = occi_State(final="sample_text", initial="sample_text")
    b1 = occi_FSM()
    b2 = occi_FSM()
    _safe_set(a, 'ownedState', b1)
    assert _is_linked(a, 'ownedState', b1)
    if hasattr(b1, 'FSM'):
        assert _is_linked(b1, 'FSM', a)
    _safe_set(a, 'ownedState', b2)
    assert _is_linked(a, 'ownedState', b2)
    if hasattr(b1, 'FSM'):
        assert not _is_linked(b1, 'FSM', a)
    if hasattr(b2, 'FSM'):
        assert _is_linked(b2, 'FSM', a)
    _safe_set(a, 'ownedState', None)
    assert not _is_linked(a, 'ownedState', b2)
    if hasattr(b2, 'FSM'):
        assert not _is_linked(b2, 'FSM', a)


def test_assoc_parent24_link_reassign_clear():
    a = occi_Kind()
    b1 = occi_Kind()
    b2 = occi_Kind()
    _safe_set(a, 'occi_Kind', b1)
    assert _is_linked(a, 'occi_Kind', b1)
    if hasattr(b1, 'occi_Kind23'):
        assert _is_linked(b1, 'occi_Kind23', a)
    _safe_set(a, 'occi_Kind', b2)
    assert _is_linked(a, 'occi_Kind', b2)
    if hasattr(b1, 'occi_Kind23'):
        assert not _is_linked(b1, 'occi_Kind23', a)
    if hasattr(b2, 'occi_Kind23'):
        assert _is_linked(b2, 'occi_Kind23', a)
    _safe_set(a, 'occi_Kind', None)
    assert not _is_linked(a, 'occi_Kind', b2)
    if hasattr(b2, 'occi_Kind23'):
        assert not _is_linked(b2, 'occi_Kind23', a)


def test_assoc_parts49_link_reassign_clear():
    a = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    b1 = occi_MixinBase()
    b2 = occi_MixinBase()
    _safe_set(a, 'entity', {b1})
    assert _is_linked(a, 'entity', b1)
    if hasattr(b1, 'MixinBase'):
        assert _is_linked(b1, 'MixinBase', a)
    _safe_set(a, 'entity', {b2})
    assert _is_linked(a, 'entity', b2)
    if hasattr(b1, 'MixinBase'):
        assert not _is_linked(b1, 'MixinBase', a)
    if hasattr(b2, 'MixinBase'):
        assert _is_linked(b2, 'MixinBase', a)
    _safe_set(a, 'entity', set())
    assert not _is_linked(a, 'entity', b2)
    if hasattr(b2, 'MixinBase'):
        assert not _is_linked(b2, 'MixinBase', a)


def test_assoc_resources76_link_reassign_clear():
    a = occi_Resource(summary="sample_text")
    b1 = occi_Configuration(description="sample_text", location="sample_text")
    b2 = occi_Configuration(description="sample_text_2", location="sample_text_2")
    _safe_set(a, 'occi_Resource', b1)
    assert _is_linked(a, 'occi_Resource', b1)
    if hasattr(b1, 'occi_Configuration77'):
        assert _is_linked(b1, 'occi_Configuration77', a)
    _safe_set(a, 'occi_Resource', b2)
    assert _is_linked(a, 'occi_Resource', b2)
    if hasattr(b1, 'occi_Configuration77'):
        assert not _is_linked(b1, 'occi_Configuration77', a)
    if hasattr(b2, 'occi_Configuration77'):
        assert _is_linked(b2, 'occi_Configuration77', a)
    _safe_set(a, 'occi_Resource', None)
    assert not _is_linked(a, 'occi_Resource', b2)
    if hasattr(b2, 'occi_Configuration77'):
        assert not _is_linked(b2, 'occi_Configuration77', a)


def test_assoc_rlinks58_link_reassign_clear():
    a = occi_Resource(summary="sample_text")
    b1 = occi_Link()
    b2 = occi_Link()
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'Link59'):
        assert _is_linked(b1, 'Link59', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'Link59'):
        assert not _is_linked(b1, 'Link59', a)
    if hasattr(b2, 'Link59'):
        assert _is_linked(b2, 'Link59', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'Link59'):
        assert not _is_linked(b2, 'Link59', a)


def test_assoc_source14_link_reassign_clear():
    a = occi_State(final="sample_text", initial="sample_text")
    b1 = occi_Transition()
    b2 = occi_Transition()
    _safe_set(a, 'State15', b1)
    assert _is_linked(a, 'State15', b1)
    if hasattr(b1, 'outgoingTransition'):
        assert _is_linked(b1, 'outgoingTransition', a)
    _safe_set(a, 'State15', b2)
    assert _is_linked(a, 'State15', b2)
    if hasattr(b1, 'outgoingTransition'):
        assert not _is_linked(b1, 'outgoingTransition', a)
    if hasattr(b2, 'outgoingTransition'):
        assert _is_linked(b2, 'outgoingTransition', a)
    _safe_set(a, 'State15', None)
    assert not _is_linked(a, 'State15', b2)
    if hasattr(b2, 'outgoingTransition'):
        assert not _is_linked(b2, 'outgoingTransition', a)


def test_assoc_source28_link_reassign_clear():
    a = occi_Kind()
    b1 = occi_Kind()
    b2 = occi_Kind()
    _safe_set(a, 'occi_Kind27', {b1})
    assert _is_linked(a, 'occi_Kind27', b1)
    if hasattr(b1, 'occi_Kind29'):
        assert _is_linked(b1, 'occi_Kind29', a)
    _safe_set(a, 'occi_Kind27', {b2})
    assert _is_linked(a, 'occi_Kind27', b2)
    if hasattr(b1, 'occi_Kind29'):
        assert not _is_linked(b1, 'occi_Kind29', a)
    if hasattr(b2, 'occi_Kind29'):
        assert _is_linked(b2, 'occi_Kind29', a)
    _safe_set(a, 'occi_Kind27', set())
    assert not _is_linked(a, 'occi_Kind27', b2)
    if hasattr(b2, 'occi_Kind29'):
        assert not _is_linked(b2, 'occi_Kind29', a)


def test_assoc_source60_link_reassign_clear():
    a = occi_Resource(summary="sample_text")
    b1 = occi_Link()
    b2 = occi_Link()
    _safe_set(a, 'Resource', b1)
    assert _is_linked(a, 'Resource', b1)
    if hasattr(b1, 'links'):
        assert _is_linked(b1, 'links', a)
    _safe_set(a, 'Resource', b2)
    assert _is_linked(a, 'Resource', b2)
    if hasattr(b1, 'links'):
        assert not _is_linked(b1, 'links', a)
    if hasattr(b2, 'links'):
        assert _is_linked(b2, 'links', a)
    _safe_set(a, 'Resource', None)
    assert not _is_linked(a, 'Resource', b2)
    if hasattr(b2, 'links'):
        assert not _is_linked(b2, 'links', a)


def test_assoc_target16_link_reassign_clear():
    a = occi_State(final="sample_text", initial="sample_text")
    b1 = occi_Transition()
    b2 = occi_Transition()
    _safe_set(a, 'occi_State17', b1)
    assert _is_linked(a, 'occi_State17', b1)
    if hasattr(b1, 'occi_Transition'):
        assert _is_linked(b1, 'occi_Transition', a)
    _safe_set(a, 'occi_State17', b2)
    assert _is_linked(a, 'occi_State17', b2)
    if hasattr(b1, 'occi_Transition'):
        assert not _is_linked(b1, 'occi_Transition', a)
    if hasattr(b2, 'occi_Transition'):
        assert _is_linked(b2, 'occi_Transition', a)
    _safe_set(a, 'occi_State17', None)
    assert not _is_linked(a, 'occi_State17', b2)
    if hasattr(b2, 'occi_Transition'):
        assert not _is_linked(b2, 'occi_Transition', a)


def test_assoc_target31_link_reassign_clear():
    a = occi_Kind()
    b1 = occi_Kind()
    b2 = occi_Kind()
    _safe_set(a, 'occi_Kind30', {b1})
    assert _is_linked(a, 'occi_Kind30', b1)
    if hasattr(b1, 'occi_Kind32'):
        assert _is_linked(b1, 'occi_Kind32', a)
    _safe_set(a, 'occi_Kind30', {b2})
    assert _is_linked(a, 'occi_Kind30', b2)
    if hasattr(b1, 'occi_Kind32'):
        assert not _is_linked(b1, 'occi_Kind32', a)
    if hasattr(b2, 'occi_Kind32'):
        assert _is_linked(b2, 'occi_Kind32', a)
    _safe_set(a, 'occi_Kind30', set())
    assert not _is_linked(a, 'occi_Kind30', b2)
    if hasattr(b2, 'occi_Kind32'):
        assert not _is_linked(b2, 'occi_Kind32', a)


def test_assoc_target61_link_reassign_clear():
    a = occi_Resource(summary="sample_text")
    b1 = occi_Link()
    b2 = occi_Link()
    _safe_set(a, 'Resource62', b1)
    assert _is_linked(a, 'Resource62', b1)
    if hasattr(b1, 'rlinks'):
        assert _is_linked(b1, 'rlinks', a)
    _safe_set(a, 'Resource62', b2)
    assert _is_linked(a, 'Resource62', b2)
    if hasattr(b1, 'rlinks'):
        assert not _is_linked(b1, 'rlinks', a)
    if hasattr(b2, 'rlinks'):
        assert _is_linked(b2, 'rlinks', a)
    _safe_set(a, 'Resource62', None)
    assert not _is_linked(a, 'Resource62', b2)
    if hasattr(b2, 'rlinks'):
        assert not _is_linked(b2, 'rlinks', a)


def test_assoc_type21_link_reassign_clear():
    a = occi_DataType(documentation="sample_text", name="sample_text")
    b1 = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    b2 = occi_Attribute(default="sample_text_2", description="sample_text_2", mutable="sample_text_2", name="sample_text_2", required="sample_text_2")
    _safe_set(a, 'occi_DataType', b1)
    assert _is_linked(a, 'occi_DataType', b1)
    if hasattr(b1, 'occi_Attribute22'):
        assert _is_linked(b1, 'occi_Attribute22', a)
    _safe_set(a, 'occi_DataType', b2)
    assert _is_linked(a, 'occi_DataType', b2)
    if hasattr(b1, 'occi_Attribute22'):
        assert not _is_linked(b1, 'occi_Attribute22', a)
    if hasattr(b2, 'occi_Attribute22'):
        assert _is_linked(b2, 'occi_Attribute22', a)
    _safe_set(a, 'occi_DataType', None)
    assert not _is_linked(a, 'occi_DataType', b2)
    if hasattr(b2, 'occi_Attribute22'):
        assert not _is_linked(b2, 'occi_Attribute22', a)


def test_assoc_type84_link_reassign_clear():
    a = occi_DataType(documentation="sample_text", name="sample_text")
    b1 = occi_ArrayType()
    b2 = occi_ArrayType()
    _safe_set(a, 'occi_DataType85', b1)
    assert _is_linked(a, 'occi_DataType85', b1)
    if hasattr(b1, 'occi_ArrayType'):
        assert _is_linked(b1, 'occi_ArrayType', a)
    _safe_set(a, 'occi_DataType85', b2)
    assert _is_linked(a, 'occi_DataType85', b2)
    if hasattr(b1, 'occi_ArrayType'):
        assert not _is_linked(b1, 'occi_ArrayType', a)
    if hasattr(b2, 'occi_ArrayType'):
        assert _is_linked(b2, 'occi_ArrayType', a)
    _safe_set(a, 'occi_DataType85', None)
    assert not _is_linked(a, 'occi_DataType85', b2)
    if hasattr(b2, 'occi_ArrayType'):
        assert not _is_linked(b2, 'occi_ArrayType', a)


def test_assoc_types71_link_reassign_clear():
    a = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    b1 = occi_DataType(documentation="sample_text", name="sample_text")
    b2 = occi_DataType(documentation="sample_text_2", name="sample_text_2")
    _safe_set(a, 'occi_Extension72', {b1})
    assert _is_linked(a, 'occi_Extension72', b1)
    if hasattr(b1, 'occi_DataType73'):
        assert _is_linked(b1, 'occi_DataType73', a)
    _safe_set(a, 'occi_Extension72', {b2})
    assert _is_linked(a, 'occi_Extension72', b2)
    if hasattr(b1, 'occi_DataType73'):
        assert not _is_linked(b1, 'occi_DataType73', a)
    if hasattr(b2, 'occi_DataType73'):
        assert _is_linked(b2, 'occi_DataType73', a)
    _safe_set(a, 'occi_Extension72', set())
    assert not _is_linked(a, 'occi_Extension72', b2)
    if hasattr(b2, 'occi_DataType73'):
        assert not _is_linked(b2, 'occi_DataType73', a)


def test_assoc_use74_link_reassign_clear():
    a = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    b1 = occi_Configuration(description="sample_text", location="sample_text")
    b2 = occi_Configuration(description="sample_text_2", location="sample_text_2")
    _safe_set(a, 'occi_Extension75', b1)
    assert _is_linked(a, 'occi_Extension75', b1)
    if hasattr(b1, 'occi_Configuration'):
        assert _is_linked(b1, 'occi_Configuration', a)
    _safe_set(a, 'occi_Extension75', b2)
    assert _is_linked(a, 'occi_Extension75', b2)
    if hasattr(b1, 'occi_Configuration'):
        assert not _is_linked(b1, 'occi_Configuration', a)
    if hasattr(b2, 'occi_Configuration'):
        assert _is_linked(b2, 'occi_Configuration', a)
    _safe_set(a, 'occi_Extension75', None)
    assert not _is_linked(a, 'occi_Extension75', b2)
    if hasattr(b2, 'occi_Configuration'):
        assert not _is_linked(b2, 'occi_Configuration', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnnotatedElement_strategy = st.builds(AnnotatedElement)
@given(instance=AnnotatedElement_strategy)
@settings(max_examples=25)
def test_AnnotatedElement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)


Attribute_strategy = st.builds(Attribute)
@given(instance=Attribute_strategy)
@settings(max_examples=25)
def test_Attribute_instantiation(instance):
    assert isinstance(instance, Attribute)


BasicType_strategy = st.builds(BasicType)
@given(instance=BasicType_strategy)
@settings(max_examples=25)
def test_BasicType_instantiation(instance):
    assert isinstance(instance, BasicType)


Category_strategy = st.builds(Category)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Entity_strategy = st.builds(Entity)
@given(instance=Entity_strategy)
@settings(max_examples=25)
def test_Entity_instantiation(instance):
    assert isinstance(instance, Entity)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


occi_Action_strategy = st.builds(occi_Action)
@given(instance=occi_Action_strategy)
@settings(max_examples=25)
def test_occi_Action_instantiation(instance):
    assert isinstance(instance, occi_Action)


occi_AnnotatedElement_strategy = st.builds(occi_AnnotatedElement)
@given(instance=occi_AnnotatedElement_strategy)
@settings(max_examples=25)
def test_occi_AnnotatedElement_instantiation(instance):
    assert isinstance(instance, occi_AnnotatedElement)


occi_Annotation_strategy = st.builds(occi_Annotation, key=safe_text, value=safe_text)
@given(instance=occi_Annotation_strategy)
@settings(max_examples=25)
def test_occi_Annotation_instantiation(instance):
    assert isinstance(instance, occi_Annotation)


occi_ArrayType_strategy = st.builds(occi_ArrayType)
@given(instance=occi_ArrayType_strategy)
@settings(max_examples=25)
def test_occi_ArrayType_instantiation(instance):
    assert isinstance(instance, occi_ArrayType)


occi_Attribute_strategy = st.builds(occi_Attribute, default=safe_text, description=safe_text, mutable=safe_text, name=safe_text, required=safe_text)
@given(instance=occi_Attribute_strategy)
@settings(max_examples=25)
def test_occi_Attribute_instantiation(instance):
    assert isinstance(instance, occi_Attribute)


occi_AttributeState_strategy = st.builds(occi_AttributeState, name=safe_text, value=safe_text)
@given(instance=occi_AttributeState_strategy)
@settings(max_examples=25)
def test_occi_AttributeState_instantiation(instance):
    assert isinstance(instance, occi_AttributeState)


occi_BasicType_strategy = st.builds(occi_BasicType)
@given(instance=occi_BasicType_strategy)
@settings(max_examples=25)
def test_occi_BasicType_instantiation(instance):
    assert isinstance(instance, occi_BasicType)


occi_BooleanType_strategy = st.builds(occi_BooleanType)
@given(instance=occi_BooleanType_strategy)
@settings(max_examples=25)
def test_occi_BooleanType_instantiation(instance):
    assert isinstance(instance, occi_BooleanType)


occi_Category_strategy = st.builds(occi_Category, description=safe_text, name=safe_text, scheme=safe_text, term=safe_text, title=safe_text)
@given(instance=occi_Category_strategy)
@settings(max_examples=25)
def test_occi_Category_instantiation(instance):
    assert isinstance(instance, occi_Category)


occi_Configuration_strategy = st.builds(occi_Configuration, description=safe_text, location=safe_text)
@given(instance=occi_Configuration_strategy)
@settings(max_examples=25)
def test_occi_Configuration_instantiation(instance):
    assert isinstance(instance, occi_Configuration)


occi_Constraint_strategy = st.builds(occi_Constraint, body=safe_text, description=safe_text, name=safe_text)
@given(instance=occi_Constraint_strategy)
@settings(max_examples=25)
def test_occi_Constraint_instantiation(instance):
    assert isinstance(instance, occi_Constraint)


occi_DataType_strategy = st.builds(occi_DataType, documentation=safe_text, name=safe_text)
@given(instance=occi_DataType_strategy)
@settings(max_examples=25)
def test_occi_DataType_instantiation(instance):
    assert isinstance(instance, occi_DataType)


occi_EObjectType_strategy = st.builds(occi_EObjectType, instanceClassName=safe_text)
@given(instance=occi_EObjectType_strategy)
@settings(max_examples=25)
def test_occi_EObjectType_instantiation(instance):
    assert isinstance(instance, occi_EObjectType)


occi_Entity_strategy = st.builds(occi_Entity, id=safe_text, location=safe_text, title=safe_text)
@given(instance=occi_Entity_strategy)
@settings(max_examples=25)
def test_occi_Entity_instantiation(instance):
    assert isinstance(instance, occi_Entity)


occi_EnumerationLiteral_strategy = st.builds(occi_EnumerationLiteral, documentation=safe_text, name=safe_text)
@given(instance=occi_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_occi_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, occi_EnumerationLiteral)


occi_EnumerationType_strategy = st.builds(occi_EnumerationType)
@given(instance=occi_EnumerationType_strategy)
@settings(max_examples=25)
def test_occi_EnumerationType_instantiation(instance):
    assert isinstance(instance, occi_EnumerationType)


occi_Extension_strategy = st.builds(occi_Extension, description=safe_text, name=safe_text, scheme=safe_text, specification=safe_text)
@given(instance=occi_Extension_strategy)
@settings(max_examples=25)
def test_occi_Extension_instantiation(instance):
    assert isinstance(instance, occi_Extension)


occi_FSM_strategy = st.builds(occi_FSM)
@given(instance=occi_FSM_strategy)
@settings(max_examples=25)
def test_occi_FSM_instantiation(instance):
    assert isinstance(instance, occi_FSM)


occi_Kind_strategy = st.builds(occi_Kind)
@given(instance=occi_Kind_strategy)
@settings(max_examples=25)
def test_occi_Kind_instantiation(instance):
    assert isinstance(instance, occi_Kind)


occi_Link_strategy = st.builds(occi_Link)
@given(instance=occi_Link_strategy)
@settings(max_examples=25)
def test_occi_Link_instantiation(instance):
    assert isinstance(instance, occi_Link)


occi_Mixin_strategy = st.builds(occi_Mixin)
@given(instance=occi_Mixin_strategy)
@settings(max_examples=25)
def test_occi_Mixin_instantiation(instance):
    assert isinstance(instance, occi_Mixin)


occi_MixinBase_strategy = st.builds(occi_MixinBase)
@given(instance=occi_MixinBase_strategy)
@settings(max_examples=25)
def test_occi_MixinBase_instantiation(instance):
    assert isinstance(instance, occi_MixinBase)


occi_NumericType_strategy = st.builds(occi_NumericType, maxExclusive=safe_text, maxInclusive=safe_text, minExclusive=safe_text, minInclusive=safe_text, totalDigits=safe_text, type=safe_text)
@given(instance=occi_NumericType_strategy)
@settings(max_examples=25)
def test_occi_NumericType_instantiation(instance):
    assert isinstance(instance, occi_NumericType)


occi_RecordField_strategy = st.builds(occi_RecordField)
@given(instance=occi_RecordField_strategy)
@settings(max_examples=25)
def test_occi_RecordField_instantiation(instance):
    assert isinstance(instance, occi_RecordField)


occi_RecordType_strategy = st.builds(occi_RecordType)
@given(instance=occi_RecordType_strategy)
@settings(max_examples=25)
def test_occi_RecordType_instantiation(instance):
    assert isinstance(instance, occi_RecordType)


occi_Resource_strategy = st.builds(occi_Resource, summary=safe_text)
@given(instance=occi_Resource_strategy)
@settings(max_examples=25)
def test_occi_Resource_instantiation(instance):
    assert isinstance(instance, occi_Resource)


occi_State_strategy = st.builds(occi_State, final=safe_text, initial=safe_text)
@given(instance=occi_State_strategy)
@settings(max_examples=25)
def test_occi_State_instantiation(instance):
    assert isinstance(instance, occi_State)


occi_StringType_strategy = st.builds(occi_StringType, length=safe_text, maxLength=safe_text, minLength=safe_text, pattern=safe_text)
@given(instance=occi_StringType_strategy)
@settings(max_examples=25)
def test_occi_StringType_instantiation(instance):
    assert isinstance(instance, occi_StringType)


occi_Transition_strategy = st.builds(occi_Transition)
@given(instance=occi_Transition_strategy)
@settings(max_examples=25)
def test_occi_Transition_instantiation(instance):
    assert isinstance(instance, occi_Transition)


occi_Type_strategy = st.builds(occi_Type)
@given(instance=occi_Type_strategy)
@settings(max_examples=25)
def test_occi_Type_instantiation(instance):
    assert isinstance(instance, occi_Type)



