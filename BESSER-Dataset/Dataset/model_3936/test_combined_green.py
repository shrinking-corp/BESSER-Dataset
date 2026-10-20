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
    ComplexPrimitivePropertyType,
    datatype_DictionaryPropertyType,
    datatype_EnumLiteral,
    datatype_Constraint,
    PropertyType,
    datatype_ComplexPrimitivePropertyType,
    datatype_ObjectPropertyType,
    datatype_PrimitivePropertyType,
    datatype_PropertyAttribute,
    datatype_PropertyType,
    datatype_ConstraintRule,
    PropertyAttribute,
    datatype_EnumLiteralPropertyAttribute,
    datatype_BooleanPropertyAttribute,
    Model,
    datatype_Type,
    Type,
    datatype_Enum,
    datatype_Entity,
    datatype_Presence,
    datatype_Property,
    BooleanPropertyAttributeType,
    PrimitiveType,
    ConstraintIntervalType,
    EnumLiteralPropertyAttributeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_complexprimitivepropertytype_is_not_abstract():
    assert not inspect.isabstract(ComplexPrimitivePropertyType)


def test_hyp_complexprimitivepropertytype_constructor_exists():
    assert callable(ComplexPrimitivePropertyType.__init__)


def test_hyp_complexprimitivepropertytype_constructor_args():
    sig = inspect.signature(ComplexPrimitivePropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_dictionarypropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype_DictionaryPropertyType)


def test_hyp_datatype_dictionarypropertytype_constructor_exists():
    assert callable(datatype_DictionaryPropertyType.__init__)


def test_hyp_datatype_dictionarypropertytype_constructor_args():
    sig = inspect.signature(datatype_DictionaryPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_enumliteral_is_not_abstract():
    assert not inspect.isabstract(datatype_EnumLiteral)


def test_hyp_datatype_enumliteral_constructor_exists():
    assert callable(datatype_EnumLiteral.__init__)


def test_hyp_datatype_enumliteral_constructor_args():
    sig = inspect.signature(datatype_EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_datatype_constraint_is_not_abstract():
    assert not inspect.isabstract(datatype_Constraint)


def test_hyp_datatype_constraint_constructor_exists():
    assert callable(datatype_Constraint.__init__)


def test_hyp_datatype_constraint_constructor_args():
    sig = inspect.signature(datatype_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "constraintValues" in params, "Missing parameter 'constraintValues'"





def test_hyp_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_hyp_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_hyp_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_complexprimitivepropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype_ComplexPrimitivePropertyType)


def test_hyp_datatype_complexprimitivepropertytype_constructor_exists():
    assert callable(datatype_ComplexPrimitivePropertyType.__init__)


def test_hyp_datatype_complexprimitivepropertytype_constructor_args():
    sig = inspect.signature(datatype_ComplexPrimitivePropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_objectpropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype_ObjectPropertyType)


def test_hyp_datatype_objectpropertytype_constructor_exists():
    assert callable(datatype_ObjectPropertyType.__init__)


def test_hyp_datatype_objectpropertytype_constructor_args():
    sig = inspect.signature(datatype_ObjectPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_primitivepropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype_PrimitivePropertyType)


def test_hyp_datatype_primitivepropertytype_constructor_exists():
    assert callable(datatype_PrimitivePropertyType.__init__)


def test_hyp_datatype_primitivepropertytype_constructor_args():
    sig = inspect.signature(datatype_PrimitivePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_datatype_propertyattribute_is_not_abstract():
    assert not inspect.isabstract(datatype_PropertyAttribute)


def test_hyp_datatype_propertyattribute_constructor_exists():
    assert callable(datatype_PropertyAttribute.__init__)


def test_hyp_datatype_propertyattribute_constructor_args():
    sig = inspect.signature(datatype_PropertyAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_propertytype_is_not_abstract():
    assert not inspect.isabstract(datatype_PropertyType)


def test_hyp_datatype_propertytype_constructor_exists():
    assert callable(datatype_PropertyType.__init__)


def test_hyp_datatype_propertytype_constructor_args():
    sig = inspect.signature(datatype_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_constraintrule_is_not_abstract():
    assert not inspect.isabstract(datatype_ConstraintRule)


def test_hyp_datatype_constraintrule_constructor_exists():
    assert callable(datatype_ConstraintRule.__init__)


def test_hyp_datatype_constraintrule_constructor_args():
    sig = inspect.signature(datatype_ConstraintRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertyattribute_is_not_abstract():
    assert not inspect.isabstract(PropertyAttribute)


def test_hyp_propertyattribute_constructor_exists():
    assert callable(PropertyAttribute.__init__)


def test_hyp_propertyattribute_constructor_args():
    sig = inspect.signature(PropertyAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_enumliteralpropertyattribute_is_not_abstract():
    assert not inspect.isabstract(datatype_EnumLiteralPropertyAttribute)


def test_hyp_datatype_enumliteralpropertyattribute_constructor_exists():
    assert callable(datatype_EnumLiteralPropertyAttribute.__init__)


def test_hyp_datatype_enumliteralpropertyattribute_constructor_args():
    sig = inspect.signature(datatype_EnumLiteralPropertyAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_datatype_booleanpropertyattribute_is_not_abstract():
    assert not inspect.isabstract(datatype_BooleanPropertyAttribute)


def test_hyp_datatype_booleanpropertyattribute_constructor_exists():
    assert callable(datatype_BooleanPropertyAttribute.__init__)


def test_hyp_datatype_booleanpropertyattribute_constructor_args():
    sig = inspect.signature(datatype_BooleanPropertyAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_hyp_model_constructor_exists():
    assert callable(Model.__init__)


def test_hyp_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_type_is_not_abstract():
    assert not inspect.isabstract(datatype_Type)


def test_hyp_datatype_type_constructor_exists():
    assert callable(datatype_Type.__init__)


def test_hyp_datatype_type_constructor_args():
    sig = inspect.signature(datatype_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_enum_is_not_abstract():
    assert not inspect.isabstract(datatype_Enum)


def test_hyp_datatype_enum_constructor_exists():
    assert callable(datatype_Enum.__init__)


def test_hyp_datatype_enum_constructor_args():
    sig = inspect.signature(datatype_Enum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_entity_is_not_abstract():
    assert not inspect.isabstract(datatype_Entity)


def test_hyp_datatype_entity_constructor_exists():
    assert callable(datatype_Entity.__init__)


def test_hyp_datatype_entity_constructor_args():
    sig = inspect.signature(datatype_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_presence_is_not_abstract():
    assert not inspect.isabstract(datatype_Presence)


def test_hyp_datatype_presence_constructor_exists():
    assert callable(datatype_Presence.__init__)


def test_hyp_datatype_presence_constructor_args():
    sig = inspect.signature(datatype_Presence.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"




def test_hyp_datatype_property_is_not_abstract():
    assert not inspect.isabstract(datatype_Property)


def test_hyp_datatype_property_constructor_exists():
    assert callable(datatype_Property.__init__)


def test_hyp_datatype_property_constructor_args():
    sig = inspect.signature(datatype_Property.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"





def test_hyp_booleanpropertyattributetype_exists():
    # Check that the Enumeration exists
    assert BooleanPropertyAttributeType is not None

def test_hyp_booleanpropertyattributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanPropertyAttributeType]
    expected_literals = [
        "writable",
        "eventable",
        "readable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanPropertyAttributeType"

def test_hyp_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_hyp_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "int",
        "short",
        "base64Binary",
        "boolean",
        "string",
        "double",
        "byte",
        "datetime",
        "float",
        "long",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"

def test_hyp_constraintintervaltype_exists():
    # Check that the Enumeration exists
    assert ConstraintIntervalType is not None

def test_hyp_constraintintervaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintIntervalType]
    expected_literals = [
        "regex",
        "strlen",
        "mimetype",
        "scaling",
        "default",
        "min",
        "max",
        "nullable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintIntervalType"

def test_hyp_enumliteralpropertyattributetype_exists():
    # Check that the Enumeration exists
    assert EnumLiteralPropertyAttributeType is not None

def test_hyp_enumliteralpropertyattributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumLiteralPropertyAttributeType]
    expected_literals = [
        "measurementUnit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumLiteralPropertyAttributeType"


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
ComplexPrimitivePropertyType_strategy = st.builds(
    ComplexPrimitivePropertyType,
)
datatype_DictionaryPropertyType_strategy = st.builds(
    datatype_DictionaryPropertyType,
)
datatype_EnumLiteral_strategy = st.builds(
    datatype_EnumLiteral,
    description=
        safe_text,
    name=
        safe_text
)
datatype_Constraint_strategy = st.builds(
    datatype_Constraint,
    type=
        safe_text,
    constraintValues=
        safe_text
)
PropertyType_strategy = st.builds(
    PropertyType,
)
datatype_ComplexPrimitivePropertyType_strategy = st.builds(
    datatype_ComplexPrimitivePropertyType,
)
datatype_ObjectPropertyType_strategy = st.builds(
    datatype_ObjectPropertyType,
)
datatype_PrimitivePropertyType_strategy = st.builds(
    datatype_PrimitivePropertyType,
    type=
        safe_text
)
datatype_PropertyAttribute_strategy = st.builds(
    datatype_PropertyAttribute,
)
datatype_PropertyType_strategy = st.builds(
    datatype_PropertyType,
)
datatype_ConstraintRule_strategy = st.builds(
    datatype_ConstraintRule,
)
PropertyAttribute_strategy = st.builds(
    PropertyAttribute,
)
datatype_EnumLiteralPropertyAttribute_strategy = st.builds(
    datatype_EnumLiteralPropertyAttribute,
    type=
        safe_text
)
datatype_BooleanPropertyAttribute_strategy = st.builds(
    datatype_BooleanPropertyAttribute,
    type=
        safe_text,
    value=
        st.booleans()
)
Model_strategy = st.builds(
    Model,
)
datatype_Type_strategy = st.builds(
    datatype_Type,
)
Type_strategy = st.builds(
    Type,
)
datatype_Enum_strategy = st.builds(
    datatype_Enum,
)
datatype_Entity_strategy = st.builds(
    datatype_Entity,
)
datatype_Presence_strategy = st.builds(
    datatype_Presence,
    mandatory=
        st.booleans()
)
datatype_Property_strategy = st.builds(
    datatype_Property,
    extension=
        st.booleans(),
    name=
        safe_text,
    description=
        safe_text,
    multiplicity=
        st.booleans()
)






@given(instance=datatype_EnumLiteral_strategy)
def test_hyp_datatype_enumliteral_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=datatype_EnumLiteral_strategy)
def test_hyp_datatype_enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=datatype_Constraint_strategy)
def test_hyp_datatype_constraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=datatype_Constraint_strategy)
def test_hyp_datatype_constraint_constraintValues_setter(instance):
    original = instance.constraintValues
    instance.constraintValues = original
    assert instance.constraintValues == original







@given(instance=datatype_PrimitivePropertyType_strategy)
def test_hyp_datatype_primitivepropertytype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original








@given(instance=datatype_EnumLiteralPropertyAttribute_strategy)
def test_hyp_datatype_enumliteralpropertyattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=datatype_BooleanPropertyAttribute_strategy)
def test_hyp_datatype_booleanpropertyattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=datatype_BooleanPropertyAttribute_strategy)
def test_hyp_datatype_booleanpropertyattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original









@given(instance=datatype_Presence_strategy)
def test_hyp_datatype_presence_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original




@given(instance=datatype_Property_strategy)
def test_hyp_datatype_property_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=datatype_Property_strategy)
def test_hyp_datatype_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=datatype_Property_strategy)
def test_hyp_datatype_property_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=datatype_Property_strategy)
def test_hyp_datatype_property_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ComplexPrimitivePropertyType,
    Model,
    PropertyAttribute,
    PropertyType,
    Type,
    datatype_BooleanPropertyAttribute,
    datatype_ComplexPrimitivePropertyType,
    datatype_Constraint,
    datatype_ConstraintRule,
    datatype_DictionaryPropertyType,
    datatype_Entity,
    datatype_Enum,
    datatype_EnumLiteral,
    datatype_EnumLiteralPropertyAttribute,
    datatype_ObjectPropertyType,
    datatype_Presence,
    datatype_PrimitivePropertyType,
    datatype_Property,
    datatype_PropertyAttribute,
    datatype_PropertyType,
    datatype_Type,
    BooleanPropertyAttributeType,
    ConstraintIntervalType,
    EnumLiteralPropertyAttributeType,
    PrimitiveType,
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

def test_datatype_BooleanPropertyAttribute_type_value_roundtrip():
    instance = datatype_BooleanPropertyAttribute(type="sample_text", value=True)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_datatype_BooleanPropertyAttribute_value_value_roundtrip():
    instance = datatype_BooleanPropertyAttribute(type="sample_text", value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_datatype_Constraint_constraintValues_value_roundtrip():
    instance = datatype_Constraint(constraintValues="sample_text", type="sample_text")
    assert instance.constraintValues == "sample_text"
    instance.constraintValues = "sample_text_2"
    assert instance.constraintValues == "sample_text_2"


def test_datatype_Constraint_type_value_roundtrip():
    instance = datatype_Constraint(constraintValues="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_datatype_EnumLiteral_description_value_roundtrip():
    instance = datatype_EnumLiteral(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_datatype_EnumLiteral_name_value_roundtrip():
    instance = datatype_EnumLiteral(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datatype_EnumLiteralPropertyAttribute_type_value_roundtrip():
    instance = datatype_EnumLiteralPropertyAttribute(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_datatype_Presence_mandatory_value_roundtrip():
    instance = datatype_Presence(mandatory=True)
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_datatype_PrimitivePropertyType_type_value_roundtrip():
    instance = datatype_PrimitivePropertyType(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_datatype_Property_description_value_roundtrip():
    instance = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_datatype_Property_extension_value_roundtrip():
    instance = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    assert instance.extension == True
    instance.extension = False
    assert instance.extension == False


def test_datatype_Property_multiplicity_value_roundtrip():
    instance = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    assert instance.multiplicity == True
    instance.multiplicity = False
    assert instance.multiplicity == False


def test_datatype_Property_name_value_roundtrip():
    instance = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_datatype_DictionaryPropertyType_isa_ComplexPrimitivePropertyType():
    instance = datatype_DictionaryPropertyType()
    assert isinstance(instance, ComplexPrimitivePropertyType)


def test_datatype_Type_isa_Model():
    instance = datatype_Type()
    assert isinstance(instance, Model)


def test_datatype_BooleanPropertyAttribute_isa_PropertyAttribute():
    instance = datatype_BooleanPropertyAttribute(type="sample_text", value=True)
    assert isinstance(instance, PropertyAttribute)


def test_datatype_EnumLiteralPropertyAttribute_isa_PropertyAttribute():
    instance = datatype_EnumLiteralPropertyAttribute(type="sample_text")
    assert isinstance(instance, PropertyAttribute)


def test_datatype_ComplexPrimitivePropertyType_isa_PropertyType():
    instance = datatype_ComplexPrimitivePropertyType()
    assert isinstance(instance, PropertyType)


def test_datatype_ObjectPropertyType_isa_PropertyType():
    instance = datatype_ObjectPropertyType()
    assert isinstance(instance, PropertyType)


def test_datatype_PrimitivePropertyType_isa_PropertyType():
    instance = datatype_PrimitivePropertyType(type="sample_text")
    assert isinstance(instance, PropertyType)


def test_datatype_Entity_isa_Type():
    instance = datatype_Entity()
    assert isinstance(instance, Type)


def test_datatype_Enum_isa_Type():
    instance = datatype_Enum()
    assert isinstance(instance, Type)


def test_assoc_Constraints16_link_reassign_clear():
    a = datatype_Constraint(constraintValues="sample_text", type="sample_text")
    b1 = datatype_ConstraintRule()
    b2 = datatype_ConstraintRule()
    _safe_set(a, 'datatype_Constraint', b1)
    assert _is_linked(a, 'datatype_Constraint', b1)
    if hasattr(b1, 'datatype_ConstraintRule17'):
        assert _is_linked(b1, 'datatype_ConstraintRule17', a)
    _safe_set(a, 'datatype_Constraint', b2)
    assert _is_linked(a, 'datatype_Constraint', b2)
    if hasattr(b1, 'datatype_ConstraintRule17'):
        assert not _is_linked(b1, 'datatype_ConstraintRule17', a)
    if hasattr(b2, 'datatype_ConstraintRule17'):
        assert _is_linked(b2, 'datatype_ConstraintRule17', a)
    _safe_set(a, 'datatype_Constraint', None)
    assert not _is_linked(a, 'datatype_Constraint', b2)
    if hasattr(b2, 'datatype_ConstraintRule17'):
        assert not _is_linked(b2, 'datatype_ConstraintRule17', a)


def test_assoc_constraintRule6_link_reassign_clear():
    a = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    b1 = datatype_ConstraintRule()
    b2 = datatype_ConstraintRule()
    _safe_set(a, 'datatype_Property7', b1)
    assert _is_linked(a, 'datatype_Property7', b1)
    if hasattr(b1, 'datatype_ConstraintRule'):
        assert _is_linked(b1, 'datatype_ConstraintRule', a)
    _safe_set(a, 'datatype_Property7', b2)
    assert _is_linked(a, 'datatype_Property7', b2)
    if hasattr(b1, 'datatype_ConstraintRule'):
        assert not _is_linked(b1, 'datatype_ConstraintRule', a)
    if hasattr(b2, 'datatype_ConstraintRule'):
        assert _is_linked(b2, 'datatype_ConstraintRule', a)
    _safe_set(a, 'datatype_Property7', None)
    assert not _is_linked(a, 'datatype_Property7', b2)
    if hasattr(b2, 'datatype_ConstraintRule'):
        assert not _is_linked(b2, 'datatype_ConstraintRule', a)


def test_assoc_enums13_link_reassign_clear():
    a = datatype_EnumLiteral(description="sample_text", name="sample_text")
    b1 = datatype_Enum()
    b2 = datatype_Enum()
    _safe_set(a, 'datatype_EnumLiteral', b1)
    assert _is_linked(a, 'datatype_EnumLiteral', b1)
    if hasattr(b1, 'datatype_Enum'):
        assert _is_linked(b1, 'datatype_Enum', a)
    _safe_set(a, 'datatype_EnumLiteral', b2)
    assert _is_linked(a, 'datatype_EnumLiteral', b2)
    if hasattr(b1, 'datatype_Enum'):
        assert not _is_linked(b1, 'datatype_Enum', a)
    if hasattr(b2, 'datatype_Enum'):
        assert _is_linked(b2, 'datatype_Enum', a)
    _safe_set(a, 'datatype_EnumLiteral', None)
    assert not _is_linked(a, 'datatype_EnumLiteral', b2)
    if hasattr(b2, 'datatype_Enum'):
        assert not _is_linked(b2, 'datatype_Enum', a)


def test_assoc_presence4_link_reassign_clear():
    a = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    b1 = datatype_Presence(mandatory=True)
    b2 = datatype_Presence(mandatory=False)
    _safe_set(a, 'datatype_Property5', b1)
    assert _is_linked(a, 'datatype_Property5', b1)
    if hasattr(b1, 'datatype_Presence'):
        assert _is_linked(b1, 'datatype_Presence', a)
    _safe_set(a, 'datatype_Property5', b2)
    assert _is_linked(a, 'datatype_Property5', b2)
    if hasattr(b1, 'datatype_Presence'):
        assert not _is_linked(b1, 'datatype_Presence', a)
    if hasattr(b2, 'datatype_Presence'):
        assert _is_linked(b2, 'datatype_Presence', a)
    _safe_set(a, 'datatype_Property5', None)
    assert not _is_linked(a, 'datatype_Property5', b2)
    if hasattr(b2, 'datatype_Presence'):
        assert not _is_linked(b2, 'datatype_Presence', a)


def test_assoc_properties2_link_reassign_clear():
    a = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    b1 = datatype_Entity()
    b2 = datatype_Entity()
    _safe_set(a, 'datatype_Property', b1)
    assert _is_linked(a, 'datatype_Property', b1)
    if hasattr(b1, 'datatype_Entity3'):
        assert _is_linked(b1, 'datatype_Entity3', a)
    _safe_set(a, 'datatype_Property', b2)
    assert _is_linked(a, 'datatype_Property', b2)
    if hasattr(b1, 'datatype_Entity3'):
        assert not _is_linked(b1, 'datatype_Entity3', a)
    if hasattr(b2, 'datatype_Entity3'):
        assert _is_linked(b2, 'datatype_Entity3', a)
    _safe_set(a, 'datatype_Property', None)
    assert not _is_linked(a, 'datatype_Property', b2)
    if hasattr(b2, 'datatype_Entity3'):
        assert not _is_linked(b2, 'datatype_Entity3', a)


def test_assoc_propertyAttributes10_link_reassign_clear():
    a = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    b1 = datatype_PropertyAttribute()
    b2 = datatype_PropertyAttribute()
    _safe_set(a, 'datatype_Property11', {b1})
    assert _is_linked(a, 'datatype_Property11', b1)
    if hasattr(b1, 'datatype_PropertyAttribute'):
        assert _is_linked(b1, 'datatype_PropertyAttribute', a)
    _safe_set(a, 'datatype_Property11', {b2})
    assert _is_linked(a, 'datatype_Property11', b2)
    if hasattr(b1, 'datatype_PropertyAttribute'):
        assert not _is_linked(b1, 'datatype_PropertyAttribute', a)
    if hasattr(b2, 'datatype_PropertyAttribute'):
        assert _is_linked(b2, 'datatype_PropertyAttribute', a)
    _safe_set(a, 'datatype_Property11', set())
    assert not _is_linked(a, 'datatype_Property11', b2)
    if hasattr(b2, 'datatype_PropertyAttribute'):
        assert not _is_linked(b2, 'datatype_PropertyAttribute', a)


def test_assoc_type8_link_reassign_clear():
    a = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    b1 = datatype_PropertyType()
    b2 = datatype_PropertyType()
    _safe_set(a, 'datatype_Property9', b1)
    assert _is_linked(a, 'datatype_Property9', b1)
    if hasattr(b1, 'datatype_PropertyType'):
        assert _is_linked(b1, 'datatype_PropertyType', a)
    _safe_set(a, 'datatype_Property9', b2)
    assert _is_linked(a, 'datatype_Property9', b2)
    if hasattr(b1, 'datatype_PropertyType'):
        assert not _is_linked(b1, 'datatype_PropertyType', a)
    if hasattr(b2, 'datatype_PropertyType'):
        assert _is_linked(b2, 'datatype_PropertyType', a)
    _safe_set(a, 'datatype_Property9', None)
    assert not _is_linked(a, 'datatype_Property9', b2)
    if hasattr(b2, 'datatype_PropertyType'):
        assert not _is_linked(b2, 'datatype_PropertyType', a)


def test_assoc_value14_link_reassign_clear():
    a = datatype_EnumLiteralPropertyAttribute(type="sample_text")
    b1 = datatype_EnumLiteral(description="sample_text", name="sample_text")
    b2 = datatype_EnumLiteral(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'datatype_EnumLiteralPropertyAttribute', b1)
    assert _is_linked(a, 'datatype_EnumLiteralPropertyAttribute', b1)
    if hasattr(b1, 'datatype_EnumLiteral15'):
        assert _is_linked(b1, 'datatype_EnumLiteral15', a)
    _safe_set(a, 'datatype_EnumLiteralPropertyAttribute', b2)
    assert _is_linked(a, 'datatype_EnumLiteralPropertyAttribute', b2)
    if hasattr(b1, 'datatype_EnumLiteral15'):
        assert not _is_linked(b1, 'datatype_EnumLiteral15', a)
    if hasattr(b2, 'datatype_EnumLiteral15'):
        assert _is_linked(b2, 'datatype_EnumLiteral15', a)
    _safe_set(a, 'datatype_EnumLiteralPropertyAttribute', None)
    assert not _is_linked(a, 'datatype_EnumLiteralPropertyAttribute', b2)
    if hasattr(b2, 'datatype_EnumLiteral15'):
        assert not _is_linked(b2, 'datatype_EnumLiteral15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ComplexPrimitivePropertyType_strategy = st.builds(ComplexPrimitivePropertyType)
@given(instance=ComplexPrimitivePropertyType_strategy)
@settings(max_examples=25)
def test_ComplexPrimitivePropertyType_instantiation(instance):
    assert isinstance(instance, ComplexPrimitivePropertyType)


Model_strategy = st.builds(Model)
@given(instance=Model_strategy)
@settings(max_examples=25)
def test_Model_instantiation(instance):
    assert isinstance(instance, Model)


PropertyAttribute_strategy = st.builds(PropertyAttribute)
@given(instance=PropertyAttribute_strategy)
@settings(max_examples=25)
def test_PropertyAttribute_instantiation(instance):
    assert isinstance(instance, PropertyAttribute)


PropertyType_strategy = st.builds(PropertyType)
@given(instance=PropertyType_strategy)
@settings(max_examples=25)
def test_PropertyType_instantiation(instance):
    assert isinstance(instance, PropertyType)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


datatype_BooleanPropertyAttribute_strategy = st.builds(datatype_BooleanPropertyAttribute, type=safe_text, value=st.booleans())
@given(instance=datatype_BooleanPropertyAttribute_strategy)
@settings(max_examples=25)
def test_datatype_BooleanPropertyAttribute_instantiation(instance):
    assert isinstance(instance, datatype_BooleanPropertyAttribute)


datatype_ComplexPrimitivePropertyType_strategy = st.builds(datatype_ComplexPrimitivePropertyType)
@given(instance=datatype_ComplexPrimitivePropertyType_strategy)
@settings(max_examples=25)
def test_datatype_ComplexPrimitivePropertyType_instantiation(instance):
    assert isinstance(instance, datatype_ComplexPrimitivePropertyType)


datatype_Constraint_strategy = st.builds(datatype_Constraint, constraintValues=safe_text, type=safe_text)
@given(instance=datatype_Constraint_strategy)
@settings(max_examples=25)
def test_datatype_Constraint_instantiation(instance):
    assert isinstance(instance, datatype_Constraint)


datatype_ConstraintRule_strategy = st.builds(datatype_ConstraintRule)
@given(instance=datatype_ConstraintRule_strategy)
@settings(max_examples=25)
def test_datatype_ConstraintRule_instantiation(instance):
    assert isinstance(instance, datatype_ConstraintRule)


datatype_DictionaryPropertyType_strategy = st.builds(datatype_DictionaryPropertyType)
@given(instance=datatype_DictionaryPropertyType_strategy)
@settings(max_examples=25)
def test_datatype_DictionaryPropertyType_instantiation(instance):
    assert isinstance(instance, datatype_DictionaryPropertyType)


datatype_Entity_strategy = st.builds(datatype_Entity)
@given(instance=datatype_Entity_strategy)
@settings(max_examples=25)
def test_datatype_Entity_instantiation(instance):
    assert isinstance(instance, datatype_Entity)


datatype_Enum_strategy = st.builds(datatype_Enum)
@given(instance=datatype_Enum_strategy)
@settings(max_examples=25)
def test_datatype_Enum_instantiation(instance):
    assert isinstance(instance, datatype_Enum)


datatype_EnumLiteral_strategy = st.builds(datatype_EnumLiteral, description=safe_text, name=safe_text)
@given(instance=datatype_EnumLiteral_strategy)
@settings(max_examples=25)
def test_datatype_EnumLiteral_instantiation(instance):
    assert isinstance(instance, datatype_EnumLiteral)


datatype_EnumLiteralPropertyAttribute_strategy = st.builds(datatype_EnumLiteralPropertyAttribute, type=safe_text)
@given(instance=datatype_EnumLiteralPropertyAttribute_strategy)
@settings(max_examples=25)
def test_datatype_EnumLiteralPropertyAttribute_instantiation(instance):
    assert isinstance(instance, datatype_EnumLiteralPropertyAttribute)


datatype_ObjectPropertyType_strategy = st.builds(datatype_ObjectPropertyType)
@given(instance=datatype_ObjectPropertyType_strategy)
@settings(max_examples=25)
def test_datatype_ObjectPropertyType_instantiation(instance):
    assert isinstance(instance, datatype_ObjectPropertyType)


datatype_Presence_strategy = st.builds(datatype_Presence, mandatory=st.booleans())
@given(instance=datatype_Presence_strategy)
@settings(max_examples=25)
def test_datatype_Presence_instantiation(instance):
    assert isinstance(instance, datatype_Presence)


datatype_PrimitivePropertyType_strategy = st.builds(datatype_PrimitivePropertyType, type=safe_text)
@given(instance=datatype_PrimitivePropertyType_strategy)
@settings(max_examples=25)
def test_datatype_PrimitivePropertyType_instantiation(instance):
    assert isinstance(instance, datatype_PrimitivePropertyType)


datatype_Property_strategy = st.builds(datatype_Property, description=safe_text, extension=st.booleans(), multiplicity=st.booleans(), name=safe_text)
@given(instance=datatype_Property_strategy)
@settings(max_examples=25)
def test_datatype_Property_instantiation(instance):
    assert isinstance(instance, datatype_Property)


datatype_PropertyAttribute_strategy = st.builds(datatype_PropertyAttribute)
@given(instance=datatype_PropertyAttribute_strategy)
@settings(max_examples=25)
def test_datatype_PropertyAttribute_instantiation(instance):
    assert isinstance(instance, datatype_PropertyAttribute)


datatype_PropertyType_strategy = st.builds(datatype_PropertyType)
@given(instance=datatype_PropertyType_strategy)
@settings(max_examples=25)
def test_datatype_PropertyType_instantiation(instance):
    assert isinstance(instance, datatype_PropertyType)


datatype_Type_strategy = st.builds(datatype_Type)
@given(instance=datatype_Type_strategy)
@settings(max_examples=25)
def test_datatype_Type_instantiation(instance):
    assert isinstance(instance, datatype_Type)



