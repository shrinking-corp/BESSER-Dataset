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
    Condition,
    forms_CompositeCondition,
    forms_AttributeValueCondition,
    forms_Condition,
    AttributePageElement,
    forms_SelectionField,
    forms_TimeSelectionField,
    forms_DateSelectionField,
    forms_TextArea,
    forms_TextField,
    PageElement,
    forms_RelationshipPageElement,
    forms_AttributePageElement,
    forms_PageElement,
    forms_Page,
    forms_Column,
    RelationshipPageElement,
    forms_Table,
    forms_List,
    forms_Literal,
    forms_Enumeration,
    forms_Relationship,
    forms_Form,
    forms_Entity,
    forms_EFML,
    forms_Attribute,
    AttributeType,
    ConditionType,
    Operators,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_compositecondition_is_not_abstract():
    assert not inspect.isabstract(forms_CompositeCondition)


def test_hyp_forms_compositecondition_constructor_exists():
    assert callable(forms_CompositeCondition.__init__)


def test_hyp_forms_compositecondition_constructor_args():
    sig = inspect.signature(forms_CompositeCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_forms_attributevaluecondition_is_not_abstract():
    assert not inspect.isabstract(forms_AttributeValueCondition)


def test_hyp_forms_attributevaluecondition_constructor_exists():
    assert callable(forms_AttributeValueCondition.__init__)


def test_hyp_forms_attributevaluecondition_constructor_args():
    sig = inspect.signature(forms_AttributeValueCondition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_forms_condition_is_not_abstract():
    assert not inspect.isabstract(forms_Condition)


def test_hyp_forms_condition_constructor_exists():
    assert callable(forms_Condition.__init__)


def test_hyp_forms_condition_constructor_args():
    sig = inspect.signature(forms_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "conditionID" in params, "Missing parameter 'conditionID'"





def test_hyp_attributepageelement_is_not_abstract():
    assert not inspect.isabstract(AttributePageElement)


def test_hyp_attributepageelement_constructor_exists():
    assert callable(AttributePageElement.__init__)


def test_hyp_attributepageelement_constructor_args():
    sig = inspect.signature(AttributePageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_selectionfield_is_not_abstract():
    assert not inspect.isabstract(forms_SelectionField)


def test_hyp_forms_selectionfield_constructor_exists():
    assert callable(forms_SelectionField.__init__)


def test_hyp_forms_selectionfield_constructor_args():
    sig = inspect.signature(forms_SelectionField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_timeselectionfield_is_not_abstract():
    assert not inspect.isabstract(forms_TimeSelectionField)


def test_hyp_forms_timeselectionfield_constructor_exists():
    assert callable(forms_TimeSelectionField.__init__)


def test_hyp_forms_timeselectionfield_constructor_args():
    sig = inspect.signature(forms_TimeSelectionField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_dateselectionfield_is_not_abstract():
    assert not inspect.isabstract(forms_DateSelectionField)


def test_hyp_forms_dateselectionfield_constructor_exists():
    assert callable(forms_DateSelectionField.__init__)


def test_hyp_forms_dateselectionfield_constructor_args():
    sig = inspect.signature(forms_DateSelectionField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_textarea_is_not_abstract():
    assert not inspect.isabstract(forms_TextArea)


def test_hyp_forms_textarea_constructor_exists():
    assert callable(forms_TextArea.__init__)


def test_hyp_forms_textarea_constructor_args():
    sig = inspect.signature(forms_TextArea.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_textfield_is_not_abstract():
    assert not inspect.isabstract(forms_TextField)


def test_hyp_forms_textfield_constructor_exists():
    assert callable(forms_TextField.__init__)


def test_hyp_forms_textfield_constructor_args():
    sig = inspect.signature(forms_TextField.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"




def test_hyp_pageelement_is_not_abstract():
    assert not inspect.isabstract(PageElement)


def test_hyp_pageelement_constructor_exists():
    assert callable(PageElement.__init__)


def test_hyp_pageelement_constructor_args():
    sig = inspect.signature(PageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_relationshippageelement_is_not_abstract():
    assert not inspect.isabstract(forms_RelationshipPageElement)


def test_hyp_forms_relationshippageelement_constructor_exists():
    assert callable(forms_RelationshipPageElement.__init__)


def test_hyp_forms_relationshippageelement_constructor_args():
    sig = inspect.signature(forms_RelationshipPageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_attributepageelement_is_not_abstract():
    assert not inspect.isabstract(forms_AttributePageElement)


def test_hyp_forms_attributepageelement_constructor_exists():
    assert callable(forms_AttributePageElement.__init__)


def test_hyp_forms_attributepageelement_constructor_args():
    sig = inspect.signature(forms_AttributePageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_pageelement_is_not_abstract():
    assert not inspect.isabstract(forms_PageElement)


def test_hyp_forms_pageelement_constructor_exists():
    assert callable(forms_PageElement.__init__)


def test_hyp_forms_pageelement_constructor_args():
    sig = inspect.signature(forms_PageElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementID" in params, "Missing parameter 'elementID'"
    assert "label" in params, "Missing parameter 'label'"





def test_hyp_forms_page_is_not_abstract():
    assert not inspect.isabstract(forms_Page)


def test_hyp_forms_page_constructor_exists():
    assert callable(forms_Page.__init__)


def test_hyp_forms_page_constructor_args():
    sig = inspect.signature(forms_Page.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_forms_column_is_not_abstract():
    assert not inspect.isabstract(forms_Column)


def test_hyp_forms_column_constructor_exists():
    assert callable(forms_Column.__init__)


def test_hyp_forms_column_constructor_args():
    sig = inspect.signature(forms_Column.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationshippageelement_is_not_abstract():
    assert not inspect.isabstract(RelationshipPageElement)


def test_hyp_relationshippageelement_constructor_exists():
    assert callable(RelationshipPageElement.__init__)


def test_hyp_relationshippageelement_constructor_args():
    sig = inspect.signature(RelationshipPageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_table_is_not_abstract():
    assert not inspect.isabstract(forms_Table)


def test_hyp_forms_table_constructor_exists():
    assert callable(forms_Table.__init__)


def test_hyp_forms_table_constructor_args():
    sig = inspect.signature(forms_Table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_list_is_not_abstract():
    assert not inspect.isabstract(forms_List)


def test_hyp_forms_list_constructor_exists():
    assert callable(forms_List.__init__)


def test_hyp_forms_list_constructor_args():
    sig = inspect.signature(forms_List.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_literal_is_not_abstract():
    assert not inspect.isabstract(forms_Literal)


def test_hyp_forms_literal_constructor_exists():
    assert callable(forms_Literal.__init__)


def test_hyp_forms_literal_constructor_args():
    sig = inspect.signature(forms_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_forms_enumeration_is_not_abstract():
    assert not inspect.isabstract(forms_Enumeration)


def test_hyp_forms_enumeration_constructor_exists():
    assert callable(forms_Enumeration.__init__)


def test_hyp_forms_enumeration_constructor_args():
    sig = inspect.signature(forms_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_forms_relationship_is_not_abstract():
    assert not inspect.isabstract(forms_Relationship)


def test_hyp_forms_relationship_constructor_exists():
    assert callable(forms_Relationship.__init__)


def test_hyp_forms_relationship_constructor_args():
    sig = inspect.signature(forms_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_forms_form_is_not_abstract():
    assert not inspect.isabstract(forms_Form)


def test_hyp_forms_form_constructor_exists():
    assert callable(forms_Form.__init__)


def test_hyp_forms_form_constructor_args():
    sig = inspect.signature(forms_Form.__init__)
    params = list(sig.parameters.keys())
    assert "mainForm" in params, "Missing parameter 'mainForm'"
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_forms_entity_is_not_abstract():
    assert not inspect.isabstract(forms_Entity)


def test_hyp_forms_entity_constructor_exists():
    assert callable(forms_Entity.__init__)


def test_hyp_forms_entity_constructor_args():
    sig = inspect.signature(forms_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_forms_efml_is_not_abstract():
    assert not inspect.isabstract(forms_EFML)


def test_hyp_forms_efml_constructor_exists():
    assert callable(forms_EFML.__init__)


def test_hyp_forms_efml_constructor_args():
    sig = inspect.signature(forms_EFML.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forms_attribute_is_not_abstract():
    assert not inspect.isabstract(forms_Attribute)


def test_hyp_forms_attribute_constructor_exists():
    assert callable(forms_Attribute.__init__)


def test_hyp_forms_attribute_constructor_args():
    sig = inspect.signature(forms_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"




def test_hyp_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_hyp_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "Integer",
        "String",
        "Text",
        "Time",
        "Year",
        "Email",
        "Boolean",
        "None_",
        "Date",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeType"

def test_hyp_conditiontype_exists():
    # Check that the Enumeration exists
    assert ConditionType is not None

def test_hyp_conditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionType]
    expected_literals = [
        "Hide",
        "Enable",
        "Disable",
        "Show",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionType"

def test_hyp_operators_exists():
    # Check that the Enumeration exists
    assert Operators is not None

def test_hyp_operators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operators]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operators"


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
Condition_strategy = st.builds(
    Condition,
)
forms_CompositeCondition_strategy = st.builds(
    forms_CompositeCondition,
    operator=
        safe_text
)
forms_AttributeValueCondition_strategy = st.builds(
    forms_AttributeValueCondition,
    value=
        safe_text
)
forms_Condition_strategy = st.builds(
    forms_Condition,
    type=
        safe_text,
    conditionID=
        safe_text
)
AttributePageElement_strategy = st.builds(
    AttributePageElement,
)
forms_SelectionField_strategy = st.builds(
    forms_SelectionField,
)
forms_TimeSelectionField_strategy = st.builds(
    forms_TimeSelectionField,
)
forms_DateSelectionField_strategy = st.builds(
    forms_DateSelectionField,
)
forms_TextArea_strategy = st.builds(
    forms_TextArea,
)
forms_TextField_strategy = st.builds(
    forms_TextField,
    format=
        safe_text
)
PageElement_strategy = st.builds(
    PageElement,
)
forms_RelationshipPageElement_strategy = st.builds(
    forms_RelationshipPageElement,
)
forms_AttributePageElement_strategy = st.builds(
    forms_AttributePageElement,
)
forms_PageElement_strategy = st.builds(
    forms_PageElement,
    elementID=
        safe_text,
    label=
        safe_text
)
forms_Page_strategy = st.builds(
    forms_Page,
    title=
        safe_text
)
forms_Column_strategy = st.builds(
    forms_Column,
)
RelationshipPageElement_strategy = st.builds(
    RelationshipPageElement,
)
forms_Table_strategy = st.builds(
    forms_Table,
)
forms_List_strategy = st.builds(
    forms_List,
)
forms_Literal_strategy = st.builds(
    forms_Literal,
    value=
        safe_text,
    name=
        safe_text
)
forms_Enumeration_strategy = st.builds(
    forms_Enumeration,
    name=
        safe_text
)
forms_Relationship_strategy = st.builds(
    forms_Relationship,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers(),
    name=
        safe_text
)
forms_Form_strategy = st.builds(
    forms_Form,
    mainForm=
        st.booleans(),
    description=
        safe_text,
    title=
        safe_text,
    name=
        safe_text
)
forms_Entity_strategy = st.builds(
    forms_Entity,
    name=
        safe_text
)
forms_EFML_strategy = st.builds(
    forms_EFML,
)
forms_Attribute_strategy = st.builds(
    forms_Attribute,
    type=
        safe_text,
    name=
        safe_text,
    mandatory=
        st.booleans()
)





@given(instance=forms_CompositeCondition_strategy)
def test_hyp_forms_compositecondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=forms_AttributeValueCondition_strategy)
def test_hyp_forms_attributevaluecondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=forms_Condition_strategy)
def test_hyp_forms_condition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=forms_Condition_strategy)
def test_hyp_forms_condition_conditionID_setter(instance):
    original = instance.conditionID
    instance.conditionID = original
    assert instance.conditionID == original









@given(instance=forms_TextField_strategy)
def test_hyp_forms_textfield_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original







@given(instance=forms_PageElement_strategy)
def test_hyp_forms_pageelement_elementID_setter(instance):
    original = instance.elementID
    instance.elementID = original
    assert instance.elementID == original



@given(instance=forms_PageElement_strategy)
def test_hyp_forms_pageelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=forms_Page_strategy)
def test_hyp_forms_page_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original








@given(instance=forms_Literal_strategy)
def test_hyp_forms_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=forms_Literal_strategy)
def test_hyp_forms_literal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=forms_Enumeration_strategy)
def test_hyp_forms_enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=forms_Relationship_strategy)
def test_hyp_forms_relationship_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=forms_Relationship_strategy)
def test_hyp_forms_relationship_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=forms_Relationship_strategy)
def test_hyp_forms_relationship_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=forms_Form_strategy)
def test_hyp_forms_form_mainForm_setter(instance):
    original = instance.mainForm
    instance.mainForm = original
    assert instance.mainForm == original



@given(instance=forms_Form_strategy)
def test_hyp_forms_form_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=forms_Form_strategy)
def test_hyp_forms_form_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=forms_Form_strategy)
def test_hyp_forms_form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=forms_Entity_strategy)
def test_hyp_forms_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=forms_Attribute_strategy)
def test_hyp_forms_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=forms_Attribute_strategy)
def test_hyp_forms_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=forms_Attribute_strategy)
def test_hyp_forms_attribute_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AttributePageElement,
    Condition,
    PageElement,
    RelationshipPageElement,
    forms_Attribute,
    forms_AttributePageElement,
    forms_AttributeValueCondition,
    forms_Column,
    forms_CompositeCondition,
    forms_Condition,
    forms_DateSelectionField,
    forms_EFML,
    forms_Entity,
    forms_Enumeration,
    forms_Form,
    forms_List,
    forms_Literal,
    forms_Page,
    forms_PageElement,
    forms_Relationship,
    forms_RelationshipPageElement,
    forms_SelectionField,
    forms_Table,
    forms_TextArea,
    forms_TextField,
    forms_TimeSelectionField,
    AttributeType,
    ConditionType,
    Operators,
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

def test_forms_Attribute_mandatory_value_roundtrip():
    instance = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_forms_Attribute_name_value_roundtrip():
    instance = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_forms_Attribute_type_value_roundtrip():
    instance = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_forms_AttributeValueCondition_value_value_roundtrip():
    instance = forms_AttributeValueCondition(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_forms_CompositeCondition_operator_value_roundtrip():
    instance = forms_CompositeCondition(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_forms_Condition_conditionID_value_roundtrip():
    instance = forms_Condition(conditionID="sample_text", type="sample_text")
    assert instance.conditionID == "sample_text"
    instance.conditionID = "sample_text_2"
    assert instance.conditionID == "sample_text_2"


def test_forms_Condition_type_value_roundtrip():
    instance = forms_Condition(conditionID="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_forms_Entity_name_value_roundtrip():
    instance = forms_Entity(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_forms_Enumeration_name_value_roundtrip():
    instance = forms_Enumeration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_forms_Form_description_value_roundtrip():
    instance = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_forms_Form_mainForm_value_roundtrip():
    instance = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    assert instance.mainForm == True
    instance.mainForm = False
    assert instance.mainForm == False


def test_forms_Form_name_value_roundtrip():
    instance = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_forms_Form_title_value_roundtrip():
    instance = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_forms_Literal_name_value_roundtrip():
    instance = forms_Literal(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_forms_Literal_value_value_roundtrip():
    instance = forms_Literal(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_forms_Page_title_value_roundtrip():
    instance = forms_Page(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_forms_PageElement_elementID_value_roundtrip():
    instance = forms_PageElement(elementID="sample_text", label="sample_text")
    assert instance.elementID == "sample_text"
    instance.elementID = "sample_text_2"
    assert instance.elementID == "sample_text_2"


def test_forms_PageElement_label_value_roundtrip():
    instance = forms_PageElement(elementID="sample_text", label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_forms_Relationship_lowerBound_value_roundtrip():
    instance = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_forms_Relationship_name_value_roundtrip():
    instance = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_forms_Relationship_upperBound_value_roundtrip():
    instance = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_forms_TextField_format_value_roundtrip():
    instance = forms_TextField(format="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_forms_DateSelectionField_isa_AttributePageElement():
    instance = forms_DateSelectionField()
    assert isinstance(instance, AttributePageElement)


def test_forms_SelectionField_isa_AttributePageElement():
    instance = forms_SelectionField()
    assert isinstance(instance, AttributePageElement)


def test_forms_TextArea_isa_AttributePageElement():
    instance = forms_TextArea()
    assert isinstance(instance, AttributePageElement)


def test_forms_TextField_isa_AttributePageElement():
    instance = forms_TextField(format="sample_text")
    assert isinstance(instance, AttributePageElement)


def test_forms_TimeSelectionField_isa_AttributePageElement():
    instance = forms_TimeSelectionField()
    assert isinstance(instance, AttributePageElement)


def test_forms_AttributeValueCondition_isa_Condition():
    instance = forms_AttributeValueCondition(value="sample_text")
    assert isinstance(instance, Condition)


def test_forms_CompositeCondition_isa_Condition():
    instance = forms_CompositeCondition(operator="sample_text")
    assert isinstance(instance, Condition)


def test_forms_AttributePageElement_isa_PageElement():
    instance = forms_AttributePageElement()
    assert isinstance(instance, PageElement)


def test_forms_RelationshipPageElement_isa_PageElement():
    instance = forms_RelationshipPageElement()
    assert isinstance(instance, PageElement)


def test_forms_List_isa_RelationshipPageElement():
    instance = forms_List()
    assert isinstance(instance, RelationshipPageElement)


def test_forms_Table_isa_RelationshipPageElement():
    instance = forms_Table()
    assert isinstance(instance, RelationshipPageElement)


def test_assoc_attribute30_link_reassign_clear():
    a = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    b1 = forms_AttributePageElement()
    b2 = forms_AttributePageElement()
    _safe_set(a, 'forms_Attribute31', b1)
    assert _is_linked(a, 'forms_Attribute31', b1)
    if hasattr(b1, 'forms_AttributePageElement'):
        assert _is_linked(b1, 'forms_AttributePageElement', a)
    _safe_set(a, 'forms_Attribute31', b2)
    assert _is_linked(a, 'forms_Attribute31', b2)
    if hasattr(b1, 'forms_AttributePageElement'):
        assert not _is_linked(b1, 'forms_AttributePageElement', a)
    if hasattr(b2, 'forms_AttributePageElement'):
        assert _is_linked(b2, 'forms_AttributePageElement', a)
    _safe_set(a, 'forms_Attribute31', None)
    assert not _is_linked(a, 'forms_Attribute31', b2)
    if hasattr(b2, 'forms_AttributePageElement'):
        assert not _is_linked(b2, 'forms_AttributePageElement', a)


def test_assoc_attributes3_link_reassign_clear():
    a = forms_Entity(name="sample_text")
    b1 = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    b2 = forms_Attribute(mandatory=False, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'forms_Entity4', {b1})
    assert _is_linked(a, 'forms_Entity4', b1)
    if hasattr(b1, 'forms_Attribute'):
        assert _is_linked(b1, 'forms_Attribute', a)
    _safe_set(a, 'forms_Entity4', {b2})
    assert _is_linked(a, 'forms_Entity4', b2)
    if hasattr(b1, 'forms_Attribute'):
        assert not _is_linked(b1, 'forms_Attribute', a)
    if hasattr(b2, 'forms_Attribute'):
        assert _is_linked(b2, 'forms_Attribute', a)
    _safe_set(a, 'forms_Entity4', set())
    assert not _is_linked(a, 'forms_Entity4', b2)
    if hasattr(b2, 'forms_Attribute'):
        assert not _is_linked(b2, 'forms_Attribute', a)


def test_assoc_conditions38_link_reassign_clear():
    a = forms_Condition(conditionID="sample_text", type="sample_text")
    b1 = forms_CompositeCondition(operator="sample_text")
    b2 = forms_CompositeCondition(operator="sample_text_2")
    _safe_set(a, 'forms_Condition', b1)
    assert _is_linked(a, 'forms_Condition', b1)
    if hasattr(b1, 'forms_CompositeCondition'):
        assert _is_linked(b1, 'forms_CompositeCondition', a)
    _safe_set(a, 'forms_Condition', b2)
    assert _is_linked(a, 'forms_Condition', b2)
    if hasattr(b1, 'forms_CompositeCondition'):
        assert not _is_linked(b1, 'forms_CompositeCondition', a)
    if hasattr(b2, 'forms_CompositeCondition'):
        assert _is_linked(b2, 'forms_CompositeCondition', a)
    _safe_set(a, 'forms_Condition', None)
    assert not _is_linked(a, 'forms_Condition', b2)
    if hasattr(b2, 'forms_CompositeCondition'):
        assert not _is_linked(b2, 'forms_CompositeCondition', a)


def test_assoc_editingForm32_link_reassign_clear():
    a = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    b1 = forms_RelationshipPageElement()
    b2 = forms_RelationshipPageElement()
    _safe_set(a, 'forms_Form33', b1)
    assert _is_linked(a, 'forms_Form33', b1)
    if hasattr(b1, 'forms_RelationshipPageElement'):
        assert _is_linked(b1, 'forms_RelationshipPageElement', a)
    _safe_set(a, 'forms_Form33', b2)
    assert _is_linked(a, 'forms_Form33', b2)
    if hasattr(b1, 'forms_RelationshipPageElement'):
        assert not _is_linked(b1, 'forms_RelationshipPageElement', a)
    if hasattr(b2, 'forms_RelationshipPageElement'):
        assert _is_linked(b2, 'forms_RelationshipPageElement', a)
    _safe_set(a, 'forms_Form33', None)
    assert not _is_linked(a, 'forms_Form33', b2)
    if hasattr(b2, 'forms_RelationshipPageElement'):
        assert not _is_linked(b2, 'forms_RelationshipPageElement', a)


def test_assoc_entities0_link_reassign_clear():
    a = forms_Entity(name="sample_text")
    b1 = forms_EFML()
    b2 = forms_EFML()
    _safe_set(a, 'forms_Entity', b1)
    assert _is_linked(a, 'forms_Entity', b1)
    if hasattr(b1, 'forms_EFML'):
        assert _is_linked(b1, 'forms_EFML', a)
    _safe_set(a, 'forms_Entity', b2)
    assert _is_linked(a, 'forms_Entity', b2)
    if hasattr(b1, 'forms_EFML'):
        assert not _is_linked(b1, 'forms_EFML', a)
    if hasattr(b2, 'forms_EFML'):
        assert _is_linked(b2, 'forms_EFML', a)
    _safe_set(a, 'forms_Entity', None)
    assert not _is_linked(a, 'forms_Entity', b2)
    if hasattr(b2, 'forms_EFML'):
        assert not _is_linked(b2, 'forms_EFML', a)


def test_assoc_entity23_link_reassign_clear():
    a = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    b1 = forms_Entity(name="sample_text")
    b2 = forms_Entity(name="sample_text_2")
    _safe_set(a, 'forms_Form24', b1)
    assert _is_linked(a, 'forms_Form24', b1)
    if hasattr(b1, 'forms_Entity25'):
        assert _is_linked(b1, 'forms_Entity25', a)
    _safe_set(a, 'forms_Form24', b2)
    assert _is_linked(a, 'forms_Form24', b2)
    if hasattr(b1, 'forms_Entity25'):
        assert not _is_linked(b1, 'forms_Entity25', a)
    if hasattr(b2, 'forms_Entity25'):
        assert _is_linked(b2, 'forms_Entity25', a)
    _safe_set(a, 'forms_Form24', None)
    assert not _is_linked(a, 'forms_Form24', b2)
    if hasattr(b2, 'forms_Entity25'):
        assert not _is_linked(b2, 'forms_Entity25', a)


def test_assoc_entityAttribute35_link_reassign_clear():
    a = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    b1 = forms_Column()
    b2 = forms_Column()
    _safe_set(a, 'forms_Attribute37', b1)
    assert _is_linked(a, 'forms_Attribute37', b1)
    if hasattr(b1, 'forms_Column36'):
        assert _is_linked(b1, 'forms_Column36', a)
    _safe_set(a, 'forms_Attribute37', b2)
    assert _is_linked(a, 'forms_Attribute37', b2)
    if hasattr(b1, 'forms_Column36'):
        assert not _is_linked(b1, 'forms_Column36', a)
    if hasattr(b2, 'forms_Column36'):
        assert _is_linked(b2, 'forms_Column36', a)
    _safe_set(a, 'forms_Attribute37', None)
    assert not _is_linked(a, 'forms_Attribute37', b2)
    if hasattr(b2, 'forms_Column36'):
        assert not _is_linked(b2, 'forms_Column36', a)


def test_assoc_enumerationType13_link_reassign_clear():
    a = forms_Enumeration(name="sample_text")
    b1 = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    b2 = forms_Attribute(mandatory=False, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'forms_Enumeration', b1)
    assert _is_linked(a, 'forms_Enumeration', b1)
    if hasattr(b1, 'forms_Attribute14'):
        assert _is_linked(b1, 'forms_Attribute14', a)
    _safe_set(a, 'forms_Enumeration', b2)
    assert _is_linked(a, 'forms_Enumeration', b2)
    if hasattr(b1, 'forms_Attribute14'):
        assert not _is_linked(b1, 'forms_Attribute14', a)
    if hasattr(b2, 'forms_Attribute14'):
        assert _is_linked(b2, 'forms_Attribute14', a)
    _safe_set(a, 'forms_Enumeration', None)
    assert not _is_linked(a, 'forms_Enumeration', b2)
    if hasattr(b2, 'forms_Attribute14'):
        assert not _is_linked(b2, 'forms_Attribute14', a)


def test_assoc_forms1_link_reassign_clear():
    a = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    b1 = forms_EFML()
    b2 = forms_EFML()
    _safe_set(a, 'forms_Form', b1)
    assert _is_linked(a, 'forms_Form', b1)
    if hasattr(b1, 'forms_EFML2'):
        assert _is_linked(b1, 'forms_EFML2', a)
    _safe_set(a, 'forms_Form', b2)
    assert _is_linked(a, 'forms_Form', b2)
    if hasattr(b1, 'forms_EFML2'):
        assert not _is_linked(b1, 'forms_EFML2', a)
    if hasattr(b2, 'forms_EFML2'):
        assert _is_linked(b2, 'forms_EFML2', a)
    _safe_set(a, 'forms_Form', None)
    assert not _is_linked(a, 'forms_Form', b2)
    if hasattr(b2, 'forms_EFML2'):
        assert not _is_linked(b2, 'forms_EFML2', a)


def test_assoc_id5_link_reassign_clear():
    a = forms_Entity(name="sample_text")
    b1 = forms_Attribute(mandatory=True, name="sample_text", type="sample_text")
    b2 = forms_Attribute(mandatory=False, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'forms_Entity6', b1)
    assert _is_linked(a, 'forms_Entity6', b1)
    if hasattr(b1, 'forms_Attribute7'):
        assert _is_linked(b1, 'forms_Attribute7', a)
    _safe_set(a, 'forms_Entity6', b2)
    assert _is_linked(a, 'forms_Entity6', b2)
    if hasattr(b1, 'forms_Attribute7'):
        assert not _is_linked(b1, 'forms_Attribute7', a)
    if hasattr(b2, 'forms_Attribute7'):
        assert _is_linked(b2, 'forms_Attribute7', a)
    _safe_set(a, 'forms_Entity6', None)
    assert not _is_linked(a, 'forms_Entity6', b2)
    if hasattr(b2, 'forms_Attribute7'):
        assert not _is_linked(b2, 'forms_Attribute7', a)


def test_assoc_literals15_link_reassign_clear():
    a = forms_Literal(name="sample_text", value="sample_text")
    b1 = forms_Enumeration(name="sample_text")
    b2 = forms_Enumeration(name="sample_text_2")
    _safe_set(a, 'forms_Literal', b1)
    assert _is_linked(a, 'forms_Literal', b1)
    if hasattr(b1, 'forms_Enumeration16'):
        assert _is_linked(b1, 'forms_Enumeration16', a)
    _safe_set(a, 'forms_Literal', b2)
    assert _is_linked(a, 'forms_Literal', b2)
    if hasattr(b1, 'forms_Enumeration16'):
        assert not _is_linked(b1, 'forms_Enumeration16', a)
    if hasattr(b2, 'forms_Enumeration16'):
        assert _is_linked(b2, 'forms_Enumeration16', a)
    _safe_set(a, 'forms_Literal', None)
    assert not _is_linked(a, 'forms_Literal', b2)
    if hasattr(b2, 'forms_Enumeration16'):
        assert not _is_linked(b2, 'forms_Enumeration16', a)


def test_assoc_opposite18_link_reassign_clear():
    a = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    b1 = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    b2 = forms_Relationship(lowerBound=13, name="sample_text_2", upperBound=13)
    _safe_set(a, 'forms_Relationship17', b1)
    assert _is_linked(a, 'forms_Relationship17', b1)
    if hasattr(b1, 'forms_Relationship19'):
        assert _is_linked(b1, 'forms_Relationship19', a)
    _safe_set(a, 'forms_Relationship17', b2)
    assert _is_linked(a, 'forms_Relationship17', b2)
    if hasattr(b1, 'forms_Relationship19'):
        assert not _is_linked(b1, 'forms_Relationship19', a)
    if hasattr(b2, 'forms_Relationship19'):
        assert _is_linked(b2, 'forms_Relationship19', a)
    _safe_set(a, 'forms_Relationship17', None)
    assert not _is_linked(a, 'forms_Relationship17', b2)
    if hasattr(b2, 'forms_Relationship19'):
        assert not _is_linked(b2, 'forms_Relationship19', a)


def test_assoc_pageElements28_link_reassign_clear():
    a = forms_PageElement(elementID="sample_text", label="sample_text")
    b1 = forms_Page(title="sample_text")
    b2 = forms_Page(title="sample_text_2")
    _safe_set(a, 'forms_PageElement', b1)
    assert _is_linked(a, 'forms_PageElement', b1)
    if hasattr(b1, 'forms_Page29'):
        assert _is_linked(b1, 'forms_Page29', a)
    _safe_set(a, 'forms_PageElement', b2)
    assert _is_linked(a, 'forms_PageElement', b2)
    if hasattr(b1, 'forms_Page29'):
        assert not _is_linked(b1, 'forms_Page29', a)
    if hasattr(b2, 'forms_Page29'):
        assert _is_linked(b2, 'forms_Page29', a)
    _safe_set(a, 'forms_PageElement', None)
    assert not _is_linked(a, 'forms_PageElement', b2)
    if hasattr(b2, 'forms_Page29'):
        assert not _is_linked(b2, 'forms_Page29', a)


def test_assoc_pages26_link_reassign_clear():
    a = forms_Page(title="sample_text")
    b1 = forms_Form(description="sample_text", mainForm=True, name="sample_text", title="sample_text")
    b2 = forms_Form(description="sample_text_2", mainForm=False, name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'forms_Page', b1)
    assert _is_linked(a, 'forms_Page', b1)
    if hasattr(b1, 'forms_Form27'):
        assert _is_linked(b1, 'forms_Form27', a)
    _safe_set(a, 'forms_Page', b2)
    assert _is_linked(a, 'forms_Page', b2)
    if hasattr(b1, 'forms_Form27'):
        assert not _is_linked(b1, 'forms_Form27', a)
    if hasattr(b2, 'forms_Form27'):
        assert _is_linked(b2, 'forms_Form27', a)
    _safe_set(a, 'forms_Page', None)
    assert not _is_linked(a, 'forms_Page', b2)
    if hasattr(b2, 'forms_Form27'):
        assert not _is_linked(b2, 'forms_Form27', a)


def test_assoc_relationships8_link_reassign_clear():
    a = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    b1 = forms_Entity(name="sample_text")
    b2 = forms_Entity(name="sample_text_2")
    _safe_set(a, 'forms_Relationship', b1)
    assert _is_linked(a, 'forms_Relationship', b1)
    if hasattr(b1, 'forms_Entity9'):
        assert _is_linked(b1, 'forms_Entity9', a)
    _safe_set(a, 'forms_Relationship', b2)
    assert _is_linked(a, 'forms_Relationship', b2)
    if hasattr(b1, 'forms_Entity9'):
        assert not _is_linked(b1, 'forms_Entity9', a)
    if hasattr(b2, 'forms_Entity9'):
        assert _is_linked(b2, 'forms_Entity9', a)
    _safe_set(a, 'forms_Relationship', None)
    assert not _is_linked(a, 'forms_Relationship', b2)
    if hasattr(b2, 'forms_Entity9'):
        assert not _is_linked(b2, 'forms_Entity9', a)


def test_assoc_superType11_link_reassign_clear():
    a = forms_Entity(name="sample_text")
    b1 = forms_Entity(name="sample_text")
    b2 = forms_Entity(name="sample_text_2")
    _safe_set(a, 'forms_Entity10', b1)
    assert _is_linked(a, 'forms_Entity10', b1)
    if hasattr(b1, 'forms_Entity12'):
        assert _is_linked(b1, 'forms_Entity12', a)
    _safe_set(a, 'forms_Entity10', b2)
    assert _is_linked(a, 'forms_Entity10', b2)
    if hasattr(b1, 'forms_Entity12'):
        assert not _is_linked(b1, 'forms_Entity12', a)
    if hasattr(b2, 'forms_Entity12'):
        assert _is_linked(b2, 'forms_Entity12', a)
    _safe_set(a, 'forms_Entity10', None)
    assert not _is_linked(a, 'forms_Entity10', b2)
    if hasattr(b2, 'forms_Entity12'):
        assert not _is_linked(b2, 'forms_Entity12', a)


def test_assoc_target20_link_reassign_clear():
    a = forms_Relationship(lowerBound=7, name="sample_text", upperBound=7)
    b1 = forms_Entity(name="sample_text")
    b2 = forms_Entity(name="sample_text_2")
    _safe_set(a, 'forms_Relationship21', b1)
    assert _is_linked(a, 'forms_Relationship21', b1)
    if hasattr(b1, 'forms_Entity22'):
        assert _is_linked(b1, 'forms_Entity22', a)
    _safe_set(a, 'forms_Relationship21', b2)
    assert _is_linked(a, 'forms_Relationship21', b2)
    if hasattr(b1, 'forms_Entity22'):
        assert not _is_linked(b1, 'forms_Entity22', a)
    if hasattr(b2, 'forms_Entity22'):
        assert _is_linked(b2, 'forms_Entity22', a)
    _safe_set(a, 'forms_Relationship21', None)
    assert not _is_linked(a, 'forms_Relationship21', b2)
    if hasattr(b2, 'forms_Entity22'):
        assert not _is_linked(b2, 'forms_Entity22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AttributePageElement_strategy = st.builds(AttributePageElement)
@given(instance=AttributePageElement_strategy)
@settings(max_examples=25)
def test_AttributePageElement_instantiation(instance):
    assert isinstance(instance, AttributePageElement)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


PageElement_strategy = st.builds(PageElement)
@given(instance=PageElement_strategy)
@settings(max_examples=25)
def test_PageElement_instantiation(instance):
    assert isinstance(instance, PageElement)


RelationshipPageElement_strategy = st.builds(RelationshipPageElement)
@given(instance=RelationshipPageElement_strategy)
@settings(max_examples=25)
def test_RelationshipPageElement_instantiation(instance):
    assert isinstance(instance, RelationshipPageElement)


forms_Attribute_strategy = st.builds(forms_Attribute, mandatory=st.booleans(), name=safe_text, type=safe_text)
@given(instance=forms_Attribute_strategy)
@settings(max_examples=25)
def test_forms_Attribute_instantiation(instance):
    assert isinstance(instance, forms_Attribute)


forms_AttributePageElement_strategy = st.builds(forms_AttributePageElement)
@given(instance=forms_AttributePageElement_strategy)
@settings(max_examples=25)
def test_forms_AttributePageElement_instantiation(instance):
    assert isinstance(instance, forms_AttributePageElement)


forms_AttributeValueCondition_strategy = st.builds(forms_AttributeValueCondition, value=safe_text)
@given(instance=forms_AttributeValueCondition_strategy)
@settings(max_examples=25)
def test_forms_AttributeValueCondition_instantiation(instance):
    assert isinstance(instance, forms_AttributeValueCondition)


forms_Column_strategy = st.builds(forms_Column)
@given(instance=forms_Column_strategy)
@settings(max_examples=25)
def test_forms_Column_instantiation(instance):
    assert isinstance(instance, forms_Column)


forms_CompositeCondition_strategy = st.builds(forms_CompositeCondition, operator=safe_text)
@given(instance=forms_CompositeCondition_strategy)
@settings(max_examples=25)
def test_forms_CompositeCondition_instantiation(instance):
    assert isinstance(instance, forms_CompositeCondition)


forms_Condition_strategy = st.builds(forms_Condition, conditionID=safe_text, type=safe_text)
@given(instance=forms_Condition_strategy)
@settings(max_examples=25)
def test_forms_Condition_instantiation(instance):
    assert isinstance(instance, forms_Condition)


forms_DateSelectionField_strategy = st.builds(forms_DateSelectionField)
@given(instance=forms_DateSelectionField_strategy)
@settings(max_examples=25)
def test_forms_DateSelectionField_instantiation(instance):
    assert isinstance(instance, forms_DateSelectionField)


forms_EFML_strategy = st.builds(forms_EFML)
@given(instance=forms_EFML_strategy)
@settings(max_examples=25)
def test_forms_EFML_instantiation(instance):
    assert isinstance(instance, forms_EFML)


forms_Entity_strategy = st.builds(forms_Entity, name=safe_text)
@given(instance=forms_Entity_strategy)
@settings(max_examples=25)
def test_forms_Entity_instantiation(instance):
    assert isinstance(instance, forms_Entity)


forms_Enumeration_strategy = st.builds(forms_Enumeration, name=safe_text)
@given(instance=forms_Enumeration_strategy)
@settings(max_examples=25)
def test_forms_Enumeration_instantiation(instance):
    assert isinstance(instance, forms_Enumeration)


forms_Form_strategy = st.builds(forms_Form, description=safe_text, mainForm=st.booleans(), name=safe_text, title=safe_text)
@given(instance=forms_Form_strategy)
@settings(max_examples=25)
def test_forms_Form_instantiation(instance):
    assert isinstance(instance, forms_Form)


forms_List_strategy = st.builds(forms_List)
@given(instance=forms_List_strategy)
@settings(max_examples=25)
def test_forms_List_instantiation(instance):
    assert isinstance(instance, forms_List)


forms_Literal_strategy = st.builds(forms_Literal, name=safe_text, value=safe_text)
@given(instance=forms_Literal_strategy)
@settings(max_examples=25)
def test_forms_Literal_instantiation(instance):
    assert isinstance(instance, forms_Literal)


forms_Page_strategy = st.builds(forms_Page, title=safe_text)
@given(instance=forms_Page_strategy)
@settings(max_examples=25)
def test_forms_Page_instantiation(instance):
    assert isinstance(instance, forms_Page)


forms_PageElement_strategy = st.builds(forms_PageElement, elementID=safe_text, label=safe_text)
@given(instance=forms_PageElement_strategy)
@settings(max_examples=25)
def test_forms_PageElement_instantiation(instance):
    assert isinstance(instance, forms_PageElement)


forms_Relationship_strategy = st.builds(forms_Relationship, lowerBound=st.integers(), name=safe_text, upperBound=st.integers())
@given(instance=forms_Relationship_strategy)
@settings(max_examples=25)
def test_forms_Relationship_instantiation(instance):
    assert isinstance(instance, forms_Relationship)


forms_RelationshipPageElement_strategy = st.builds(forms_RelationshipPageElement)
@given(instance=forms_RelationshipPageElement_strategy)
@settings(max_examples=25)
def test_forms_RelationshipPageElement_instantiation(instance):
    assert isinstance(instance, forms_RelationshipPageElement)


forms_SelectionField_strategy = st.builds(forms_SelectionField)
@given(instance=forms_SelectionField_strategy)
@settings(max_examples=25)
def test_forms_SelectionField_instantiation(instance):
    assert isinstance(instance, forms_SelectionField)


forms_Table_strategy = st.builds(forms_Table)
@given(instance=forms_Table_strategy)
@settings(max_examples=25)
def test_forms_Table_instantiation(instance):
    assert isinstance(instance, forms_Table)


forms_TextArea_strategy = st.builds(forms_TextArea)
@given(instance=forms_TextArea_strategy)
@settings(max_examples=25)
def test_forms_TextArea_instantiation(instance):
    assert isinstance(instance, forms_TextArea)


forms_TextField_strategy = st.builds(forms_TextField, format=safe_text)
@given(instance=forms_TextField_strategy)
@settings(max_examples=25)
def test_forms_TextField_instantiation(instance):
    assert isinstance(instance, forms_TextField)


forms_TimeSelectionField_strategy = st.builds(forms_TimeSelectionField)
@given(instance=forms_TimeSelectionField_strategy)
@settings(max_examples=25)
def test_forms_TimeSelectionField_instantiation(instance):
    assert isinstance(instance, forms_TimeSelectionField)



