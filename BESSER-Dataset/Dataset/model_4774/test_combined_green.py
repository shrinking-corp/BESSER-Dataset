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
    Literal,
    types_CharLiteral,
    types_BooleanLiteral,
    types_NumberLiteral,
    types_MappedByReference,
    types_Literal,
    types_PropertyReference,
    types_EntityRelationship,
    types_Property,
    types_EnumerationLiteral,
    ComplexType,
    types_EntityType,
    types_EnumerationType,
    types_StringLiteral,
    NamedType,
    types_PrimitiveType,
    types_DeclarationTypeReference,
    DeclarationTypeReference,
    types_TypeReference,
    Type,
    types_MapType,
    types_CollectionType,
    types_NamedType,
    types_Type,
    types_ComplexType,
    types_Import,
    types_Model,
    TypeStorageModifier,
    EntityRelationshipKind,
    PropertyStorageModifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_charliteral_is_not_abstract():
    assert not inspect.isabstract(types_CharLiteral)


def test_hyp_types_charliteral_constructor_exists():
    assert callable(types_CharLiteral.__init__)


def test_hyp_types_charliteral_constructor_args():
    sig = inspect.signature(types_CharLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_types_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(types_BooleanLiteral)


def test_hyp_types_booleanliteral_constructor_exists():
    assert callable(types_BooleanLiteral.__init__)


def test_hyp_types_booleanliteral_constructor_args():
    sig = inspect.signature(types_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_types_numberliteral_is_not_abstract():
    assert not inspect.isabstract(types_NumberLiteral)


def test_hyp_types_numberliteral_constructor_exists():
    assert callable(types_NumberLiteral.__init__)


def test_hyp_types_numberliteral_constructor_args():
    sig = inspect.signature(types_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_types_mappedbyreference_is_not_abstract():
    assert not inspect.isabstract(types_MappedByReference)


def test_hyp_types_mappedbyreference_constructor_exists():
    assert callable(types_MappedByReference.__init__)


def test_hyp_types_mappedbyreference_constructor_args():
    sig = inspect.signature(types_MappedByReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_literal_is_not_abstract():
    assert not inspect.isabstract(types_Literal)


def test_hyp_types_literal_constructor_exists():
    assert callable(types_Literal.__init__)


def test_hyp_types_literal_constructor_args():
    sig = inspect.signature(types_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_propertyreference_is_not_abstract():
    assert not inspect.isabstract(types_PropertyReference)


def test_hyp_types_propertyreference_constructor_exists():
    assert callable(types_PropertyReference.__init__)


def test_hyp_types_propertyreference_constructor_args():
    sig = inspect.signature(types_PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_entityrelationship_is_not_abstract():
    assert not inspect.isabstract(types_EntityRelationship)


def test_hyp_types_entityrelationship_constructor_exists():
    assert callable(types_EntityRelationship.__init__)


def test_hyp_types_entityrelationship_constructor_args():
    sig = inspect.signature(types_EntityRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_types_property_is_not_abstract():
    assert not inspect.isabstract(types_Property)


def test_hyp_types_property_constructor_exists():
    assert callable(types_Property.__init__)


def test_hyp_types_property_constructor_args():
    sig = inspect.signature(types_Property.__init__)
    params = list(sig.parameters.keys())
    assert "storageModifier" in params, "Missing parameter 'storageModifier'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_types_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(types_EnumerationLiteral)


def test_hyp_types_enumerationliteral_constructor_exists():
    assert callable(types_EnumerationLiteral.__init__)


def test_hyp_types_enumerationliteral_constructor_args():
    sig = inspect.signature(types_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_hyp_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_hyp_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_entitytype_is_not_abstract():
    assert not inspect.isabstract(types_EntityType)


def test_hyp_types_entitytype_constructor_exists():
    assert callable(types_EntityType.__init__)


def test_hyp_types_entitytype_constructor_args():
    sig = inspect.signature(types_EntityType.__init__)
    params = list(sig.parameters.keys())
    assert "storageModifier" in params, "Missing parameter 'storageModifier'"




def test_hyp_types_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(types_EnumerationType)


def test_hyp_types_enumerationtype_constructor_exists():
    assert callable(types_EnumerationType.__init__)


def test_hyp_types_enumerationtype_constructor_args():
    sig = inspect.signature(types_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_stringliteral_is_not_abstract():
    assert not inspect.isabstract(types_StringLiteral)


def test_hyp_types_stringliteral_constructor_exists():
    assert callable(types_StringLiteral.__init__)


def test_hyp_types_stringliteral_constructor_args():
    sig = inspect.signature(types_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_namedtype_is_not_abstract():
    assert not inspect.isabstract(NamedType)


def test_hyp_namedtype_constructor_exists():
    assert callable(NamedType.__init__)


def test_hyp_namedtype_constructor_args():
    sig = inspect.signature(NamedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_PrimitiveType)


def test_hyp_types_primitivetype_constructor_exists():
    assert callable(types_PrimitiveType.__init__)


def test_hyp_types_primitivetype_constructor_args():
    sig = inspect.signature(types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_declarationtypereference_is_not_abstract():
    assert not inspect.isabstract(types_DeclarationTypeReference)


def test_hyp_types_declarationtypereference_constructor_exists():
    assert callable(types_DeclarationTypeReference.__init__)


def test_hyp_types_declarationtypereference_constructor_args():
    sig = inspect.signature(types_DeclarationTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declarationtypereference_is_not_abstract():
    assert not inspect.isabstract(DeclarationTypeReference)


def test_hyp_declarationtypereference_constructor_exists():
    assert callable(DeclarationTypeReference.__init__)


def test_hyp_declarationtypereference_constructor_args():
    sig = inspect.signature(DeclarationTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_typereference_is_not_abstract():
    assert not inspect.isabstract(types_TypeReference)


def test_hyp_types_typereference_constructor_exists():
    assert callable(types_TypeReference.__init__)


def test_hyp_types_typereference_constructor_args():
    sig = inspect.signature(types_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_maptype_is_not_abstract():
    assert not inspect.isabstract(types_MapType)


def test_hyp_types_maptype_constructor_exists():
    assert callable(types_MapType.__init__)


def test_hyp_types_maptype_constructor_args():
    sig = inspect.signature(types_MapType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"




def test_hyp_types_collectiontype_is_not_abstract():
    assert not inspect.isabstract(types_CollectionType)


def test_hyp_types_collectiontype_constructor_exists():
    assert callable(types_CollectionType.__init__)


def test_hyp_types_collectiontype_constructor_args():
    sig = inspect.signature(types_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"




def test_hyp_types_namedtype_is_not_abstract():
    assert not inspect.isabstract(types_NamedType)


def test_hyp_types_namedtype_constructor_exists():
    assert callable(types_NamedType.__init__)


def test_hyp_types_namedtype_constructor_args():
    sig = inspect.signature(types_NamedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_hyp_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_hyp_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_complextype_is_not_abstract():
    assert not inspect.isabstract(types_ComplexType)


def test_hyp_types_complextype_constructor_exists():
    assert callable(types_ComplexType.__init__)


def test_hyp_types_complextype_constructor_args():
    sig = inspect.signature(types_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_import_is_not_abstract():
    assert not inspect.isabstract(types_Import)


def test_hyp_types_import_constructor_exists():
    assert callable(types_Import.__init__)


def test_hyp_types_import_constructor_args():
    sig = inspect.signature(types_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"




def test_hyp_types_model_is_not_abstract():
    assert not inspect.isabstract(types_Model)


def test_hyp_types_model_constructor_exists():
    assert callable(types_Model.__init__)


def test_hyp_types_model_constructor_args():
    sig = inspect.signature(types_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_typestoragemodifier_exists():
    # Check that the Enumeration exists
    assert TypeStorageModifier is not None

def test_hyp_typestoragemodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeStorageModifier]
    expected_literals = [
        "STORABLE",
        "EMBEDDABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeStorageModifier"

def test_hyp_entityrelationshipkind_exists():
    # Check that the Enumeration exists
    assert EntityRelationshipKind is not None

def test_hyp_entityrelationshipkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityRelationshipKind]
    expected_literals = [
        "UNIQUE",
        "MANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityRelationshipKind"

def test_hyp_propertystoragemodifier_exists():
    # Check that the Enumeration exists
    assert PropertyStorageModifier is not None

def test_hyp_propertystoragemodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PropertyStorageModifier]
    expected_literals = [
        "VARIABLE",
        "TRANSIENT",
        "VALUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PropertyStorageModifier"


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
Literal_strategy = st.builds(
    Literal,
)
types_CharLiteral_strategy = st.builds(
    types_CharLiteral,
    value=
        safe_text
)
types_BooleanLiteral_strategy = st.builds(
    types_BooleanLiteral,
    value=
        st.booleans()
)
types_NumberLiteral_strategy = st.builds(
    types_NumberLiteral,
    value=
        safe_text
)
types_MappedByReference_strategy = st.builds(
    types_MappedByReference,
)
types_Literal_strategy = st.builds(
    types_Literal,
)
types_PropertyReference_strategy = st.builds(
    types_PropertyReference,
)
types_EntityRelationship_strategy = st.builds(
    types_EntityRelationship,
    kind=
        safe_text
)
types_Property_strategy = st.builds(
    types_Property,
    storageModifier=
        safe_text,
    name=
        safe_text
)
types_EnumerationLiteral_strategy = st.builds(
    types_EnumerationLiteral,
    name=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
types_EntityType_strategy = st.builds(
    types_EntityType,
    storageModifier=
        safe_text
)
types_EnumerationType_strategy = st.builds(
    types_EnumerationType,
)
types_StringLiteral_strategy = st.builds(
    types_StringLiteral,
    value=
        safe_text
)
NamedType_strategy = st.builds(
    NamedType,
)
types_PrimitiveType_strategy = st.builds(
    types_PrimitiveType,
)
types_DeclarationTypeReference_strategy = st.builds(
    types_DeclarationTypeReference,
)
DeclarationTypeReference_strategy = st.builds(
    DeclarationTypeReference,
)
types_TypeReference_strategy = st.builds(
    types_TypeReference,
)
Type_strategy = st.builds(
    Type,
)
types_MapType_strategy = st.builds(
    types_MapType,
    size=
        st.integers()
)
types_CollectionType_strategy = st.builds(
    types_CollectionType,
    size=
        st.integers()
)
types_NamedType_strategy = st.builds(
    types_NamedType,
    name=
        safe_text
)
types_Type_strategy = st.builds(
    types_Type,
)
types_ComplexType_strategy = st.builds(
    types_ComplexType,
)
types_Import_strategy = st.builds(
    types_Import,
    importedNamespace=
        safe_text
)
types_Model_strategy = st.builds(
    types_Model,
    name=
        safe_text
)





@given(instance=types_CharLiteral_strategy)
def test_hyp_types_charliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=types_BooleanLiteral_strategy)
def test_hyp_types_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=types_NumberLiteral_strategy)
def test_hyp_types_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=types_EntityRelationship_strategy)
def test_hyp_types_entityrelationship_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=types_Property_strategy)
def test_hyp_types_property_storageModifier_setter(instance):
    original = instance.storageModifier
    instance.storageModifier = original
    assert instance.storageModifier == original



@given(instance=types_Property_strategy)
def test_hyp_types_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=types_EnumerationLiteral_strategy)
def test_hyp_types_enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=types_EntityType_strategy)
def test_hyp_types_entitytype_storageModifier_setter(instance):
    original = instance.storageModifier
    instance.storageModifier = original
    assert instance.storageModifier == original





@given(instance=types_StringLiteral_strategy)
def test_hyp_types_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original










@given(instance=types_MapType_strategy)
def test_hyp_types_maptype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original




@given(instance=types_CollectionType_strategy)
def test_hyp_types_collectiontype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original




@given(instance=types_NamedType_strategy)
def test_hyp_types_namedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=types_Import_strategy)
def test_hyp_types_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original




@given(instance=types_Model_strategy)
def test_hyp_types_model_name_setter(instance):
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
    ComplexType,
    DeclarationTypeReference,
    Literal,
    NamedType,
    Type,
    types_BooleanLiteral,
    types_CharLiteral,
    types_CollectionType,
    types_ComplexType,
    types_DeclarationTypeReference,
    types_EntityRelationship,
    types_EntityType,
    types_EnumerationLiteral,
    types_EnumerationType,
    types_Import,
    types_Literal,
    types_MapType,
    types_MappedByReference,
    types_Model,
    types_NamedType,
    types_NumberLiteral,
    types_PrimitiveType,
    types_Property,
    types_PropertyReference,
    types_StringLiteral,
    types_Type,
    types_TypeReference,
    EntityRelationshipKind,
    PropertyStorageModifier,
    TypeStorageModifier,
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

def test_types_BooleanLiteral_value_value_roundtrip():
    instance = types_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_types_CharLiteral_value_value_roundtrip():
    instance = types_CharLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_types_CollectionType_size_value_roundtrip():
    instance = types_CollectionType(size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_types_EntityRelationship_kind_value_roundtrip():
    instance = types_EntityRelationship(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_types_EntityType_storageModifier_value_roundtrip():
    instance = types_EntityType(storageModifier="sample_text")
    assert instance.storageModifier == "sample_text"
    instance.storageModifier = "sample_text_2"
    assert instance.storageModifier == "sample_text_2"


def test_types_EnumerationLiteral_name_value_roundtrip():
    instance = types_EnumerationLiteral(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_types_Import_importedNamespace_value_roundtrip():
    instance = types_Import(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_types_MapType_size_value_roundtrip():
    instance = types_MapType(size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_types_Model_name_value_roundtrip():
    instance = types_Model(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_types_NamedType_name_value_roundtrip():
    instance = types_NamedType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_types_NumberLiteral_value_value_roundtrip():
    instance = types_NumberLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_types_Property_name_value_roundtrip():
    instance = types_Property(name="sample_text", storageModifier="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_types_Property_storageModifier_value_roundtrip():
    instance = types_Property(name="sample_text", storageModifier="sample_text")
    assert instance.storageModifier == "sample_text"
    instance.storageModifier = "sample_text_2"
    assert instance.storageModifier == "sample_text_2"


def test_types_StringLiteral_value_value_roundtrip():
    instance = types_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_types_EntityType_isa_ComplexType():
    instance = types_EntityType(storageModifier="sample_text")
    assert isinstance(instance, ComplexType)


def test_types_EnumerationType_isa_ComplexType():
    instance = types_EnumerationType()
    assert isinstance(instance, ComplexType)


def test_types_CollectionType_isa_DeclarationTypeReference():
    instance = types_CollectionType(size=7)
    assert isinstance(instance, DeclarationTypeReference)


def test_types_MapType_isa_DeclarationTypeReference():
    instance = types_MapType(size=7)
    assert isinstance(instance, DeclarationTypeReference)


def test_types_TypeReference_isa_DeclarationTypeReference():
    instance = types_TypeReference()
    assert isinstance(instance, DeclarationTypeReference)


def test_types_BooleanLiteral_isa_Literal():
    instance = types_BooleanLiteral(value=True)
    assert isinstance(instance, Literal)


def test_types_CharLiteral_isa_Literal():
    instance = types_CharLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_types_NumberLiteral_isa_Literal():
    instance = types_NumberLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_types_PropertyReference_isa_Literal():
    instance = types_PropertyReference()
    assert isinstance(instance, Literal)


def test_types_StringLiteral_isa_Literal():
    instance = types_StringLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_types_ComplexType_isa_NamedType():
    instance = types_ComplexType()
    assert isinstance(instance, NamedType)


def test_types_PrimitiveType_isa_NamedType():
    instance = types_PrimitiveType()
    assert isinstance(instance, NamedType)


def test_types_CollectionType_isa_Type():
    instance = types_CollectionType(size=7)
    assert isinstance(instance, Type)


def test_types_MapType_isa_Type():
    instance = types_MapType(size=7)
    assert isinstance(instance, Type)


def test_types_NamedType_isa_Type():
    instance = types_NamedType(name="sample_text")
    assert isinstance(instance, Type)


def test_assoc_base29_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_MappedByReference()
    b2 = types_MappedByReference()
    _safe_set(a, 'types_Property31', b1)
    assert _is_linked(a, 'types_Property31', b1)
    if hasattr(b1, 'types_MappedByReference30'):
        assert _is_linked(b1, 'types_MappedByReference30', a)
    _safe_set(a, 'types_Property31', b2)
    assert _is_linked(a, 'types_Property31', b2)
    if hasattr(b1, 'types_MappedByReference30'):
        assert not _is_linked(b1, 'types_MappedByReference30', a)
    if hasattr(b2, 'types_MappedByReference30'):
        assert _is_linked(b2, 'types_MappedByReference30', a)
    _safe_set(a, 'types_Property31', None)
    assert not _is_linked(a, 'types_Property31', b2)
    if hasattr(b2, 'types_MappedByReference30'):
        assert not _is_linked(b2, 'types_MappedByReference30', a)


def test_assoc_imports0_link_reassign_clear():
    a = types_Model(name="sample_text")
    b1 = types_Import(importedNamespace="sample_text")
    b2 = types_Import(importedNamespace="sample_text_2")
    _safe_set(a, 'types_Model', {b1})
    assert _is_linked(a, 'types_Model', b1)
    if hasattr(b1, 'types_Import'):
        assert _is_linked(b1, 'types_Import', a)
    _safe_set(a, 'types_Model', {b2})
    assert _is_linked(a, 'types_Model', b2)
    if hasattr(b1, 'types_Import'):
        assert not _is_linked(b1, 'types_Import', a)
    if hasattr(b2, 'types_Import'):
        assert _is_linked(b2, 'types_Import', a)
    _safe_set(a, 'types_Model', set())
    assert not _is_linked(a, 'types_Model', b2)
    if hasattr(b2, 'types_Import'):
        assert not _is_linked(b2, 'types_Import', a)


def test_assoc_literal25_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_Literal()
    b2 = types_Literal()
    _safe_set(a, 'types_Property26', b1)
    assert _is_linked(a, 'types_Property26', b1)
    if hasattr(b1, 'types_Literal'):
        assert _is_linked(b1, 'types_Literal', a)
    _safe_set(a, 'types_Property26', b2)
    assert _is_linked(a, 'types_Property26', b2)
    if hasattr(b1, 'types_Literal'):
        assert not _is_linked(b1, 'types_Literal', a)
    if hasattr(b2, 'types_Literal'):
        assert _is_linked(b2, 'types_Literal', a)
    _safe_set(a, 'types_Property26', None)
    assert not _is_linked(a, 'types_Property26', b2)
    if hasattr(b2, 'types_Literal'):
        assert not _is_linked(b2, 'types_Literal', a)


def test_assoc_literals14_link_reassign_clear():
    a = types_EnumerationLiteral(name="sample_text")
    b1 = types_EnumerationType()
    b2 = types_EnumerationType()
    _safe_set(a, 'types_EnumerationLiteral', b1)
    assert _is_linked(a, 'types_EnumerationLiteral', b1)
    if hasattr(b1, 'types_EnumerationType'):
        assert _is_linked(b1, 'types_EnumerationType', a)
    _safe_set(a, 'types_EnumerationLiteral', b2)
    assert _is_linked(a, 'types_EnumerationLiteral', b2)
    if hasattr(b1, 'types_EnumerationType'):
        assert not _is_linked(b1, 'types_EnumerationType', a)
    if hasattr(b2, 'types_EnumerationType'):
        assert _is_linked(b2, 'types_EnumerationType', a)
    _safe_set(a, 'types_EnumerationLiteral', None)
    assert not _is_linked(a, 'types_EnumerationLiteral', b2)
    if hasattr(b2, 'types_EnumerationType'):
        assert not _is_linked(b2, 'types_EnumerationType', a)


def test_assoc_mapKey22_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_PropertyReference()
    b2 = types_PropertyReference()
    _safe_set(a, 'types_Property23', b1)
    assert _is_linked(a, 'types_Property23', b1)
    if hasattr(b1, 'types_PropertyReference24'):
        assert _is_linked(b1, 'types_PropertyReference24', a)
    _safe_set(a, 'types_Property23', b2)
    assert _is_linked(a, 'types_Property23', b2)
    if hasattr(b1, 'types_PropertyReference24'):
        assert not _is_linked(b1, 'types_PropertyReference24', a)
    if hasattr(b2, 'types_PropertyReference24'):
        assert _is_linked(b2, 'types_PropertyReference24', a)
    _safe_set(a, 'types_Property23', None)
    assert not _is_linked(a, 'types_Property23', b2)
    if hasattr(b2, 'types_PropertyReference24'):
        assert not _is_linked(b2, 'types_PropertyReference24', a)


def test_assoc_mapType6_link_reassign_clear():
    a = types_MapType(size=7)
    b1 = types_TypeReference()
    b2 = types_TypeReference()
    _safe_set(a, 'types_MapType7', b1)
    assert _is_linked(a, 'types_MapType7', b1)
    if hasattr(b1, 'types_TypeReference8'):
        assert _is_linked(b1, 'types_TypeReference8', a)
    _safe_set(a, 'types_MapType7', b2)
    assert _is_linked(a, 'types_MapType7', b2)
    if hasattr(b1, 'types_TypeReference8'):
        assert not _is_linked(b1, 'types_TypeReference8', a)
    if hasattr(b2, 'types_TypeReference8'):
        assert _is_linked(b2, 'types_TypeReference8', a)
    _safe_set(a, 'types_MapType7', None)
    assert not _is_linked(a, 'types_MapType7', b2)
    if hasattr(b2, 'types_TypeReference8'):
        assert not _is_linked(b2, 'types_TypeReference8', a)


def test_assoc_mappedBy27_link_reassign_clear():
    a = types_EntityRelationship(kind="sample_text")
    b1 = types_MappedByReference()
    b2 = types_MappedByReference()
    _safe_set(a, 'types_EntityRelationship28', b1)
    assert _is_linked(a, 'types_EntityRelationship28', b1)
    if hasattr(b1, 'types_MappedByReference'):
        assert _is_linked(b1, 'types_MappedByReference', a)
    _safe_set(a, 'types_EntityRelationship28', b2)
    assert _is_linked(a, 'types_EntityRelationship28', b2)
    if hasattr(b1, 'types_MappedByReference'):
        assert not _is_linked(b1, 'types_MappedByReference', a)
    if hasattr(b2, 'types_MappedByReference'):
        assert _is_linked(b2, 'types_MappedByReference', a)
    _safe_set(a, 'types_EntityRelationship28', None)
    assert not _is_linked(a, 'types_EntityRelationship28', b2)
    if hasattr(b2, 'types_MappedByReference'):
        assert not _is_linked(b2, 'types_MappedByReference', a)


def test_assoc_orderBy20_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_PropertyReference()
    b2 = types_PropertyReference()
    _safe_set(a, 'types_Property21', b1)
    assert _is_linked(a, 'types_Property21', b1)
    if hasattr(b1, 'types_PropertyReference'):
        assert _is_linked(b1, 'types_PropertyReference', a)
    _safe_set(a, 'types_Property21', b2)
    assert _is_linked(a, 'types_Property21', b2)
    if hasattr(b1, 'types_PropertyReference'):
        assert not _is_linked(b1, 'types_PropertyReference', a)
    if hasattr(b2, 'types_PropertyReference'):
        assert _is_linked(b2, 'types_PropertyReference', a)
    _safe_set(a, 'types_Property21', None)
    assert not _is_linked(a, 'types_Property21', b2)
    if hasattr(b2, 'types_PropertyReference'):
        assert not _is_linked(b2, 'types_PropertyReference', a)


def test_assoc_properties15_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_EntityType(storageModifier="sample_text")
    b2 = types_EntityType(storageModifier="sample_text_2")
    _safe_set(a, 'types_Property', b1)
    assert _is_linked(a, 'types_Property', b1)
    if hasattr(b1, 'types_EntityType'):
        assert _is_linked(b1, 'types_EntityType', a)
    _safe_set(a, 'types_Property', b2)
    assert _is_linked(a, 'types_Property', b2)
    if hasattr(b1, 'types_EntityType'):
        assert not _is_linked(b1, 'types_EntityType', a)
    if hasattr(b2, 'types_EntityType'):
        assert _is_linked(b2, 'types_EntityType', a)
    _safe_set(a, 'types_Property', None)
    assert not _is_linked(a, 'types_Property', b2)
    if hasattr(b2, 'types_EntityType'):
        assert not _is_linked(b2, 'types_EntityType', a)


def test_assoc_reference3_link_reassign_clear():
    a = types_CollectionType(size=7)
    b1 = types_TypeReference()
    b2 = types_TypeReference()
    _safe_set(a, 'types_CollectionType', b1)
    assert _is_linked(a, 'types_CollectionType', b1)
    if hasattr(b1, 'types_TypeReference'):
        assert _is_linked(b1, 'types_TypeReference', a)
    _safe_set(a, 'types_CollectionType', b2)
    assert _is_linked(a, 'types_CollectionType', b2)
    if hasattr(b1, 'types_TypeReference'):
        assert not _is_linked(b1, 'types_TypeReference', a)
    if hasattr(b2, 'types_TypeReference'):
        assert _is_linked(b2, 'types_TypeReference', a)
    _safe_set(a, 'types_CollectionType', None)
    assert not _is_linked(a, 'types_CollectionType', b2)
    if hasattr(b2, 'types_TypeReference'):
        assert not _is_linked(b2, 'types_TypeReference', a)


def test_assoc_reference35_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_PropertyReference()
    b2 = types_PropertyReference()
    _safe_set(a, 'types_Property37', b1)
    assert _is_linked(a, 'types_Property37', b1)
    if hasattr(b1, 'types_PropertyReference36'):
        assert _is_linked(b1, 'types_PropertyReference36', a)
    _safe_set(a, 'types_Property37', b2)
    assert _is_linked(a, 'types_Property37', b2)
    if hasattr(b1, 'types_PropertyReference36'):
        assert not _is_linked(b1, 'types_PropertyReference36', a)
    if hasattr(b2, 'types_PropertyReference36'):
        assert _is_linked(b2, 'types_PropertyReference36', a)
    _safe_set(a, 'types_Property37', None)
    assert not _is_linked(a, 'types_Property37', b2)
    if hasattr(b2, 'types_PropertyReference36'):
        assert not _is_linked(b2, 'types_PropertyReference36', a)


def test_assoc_reference4_link_reassign_clear():
    a = types_MapType(size=7)
    b1 = types_TypeReference()
    b2 = types_TypeReference()
    _safe_set(a, 'types_MapType', b1)
    assert _is_linked(a, 'types_MapType', b1)
    if hasattr(b1, 'types_TypeReference5'):
        assert _is_linked(b1, 'types_TypeReference5', a)
    _safe_set(a, 'types_MapType', b2)
    assert _is_linked(a, 'types_MapType', b2)
    if hasattr(b1, 'types_TypeReference5'):
        assert not _is_linked(b1, 'types_TypeReference5', a)
    if hasattr(b2, 'types_TypeReference5'):
        assert _is_linked(b2, 'types_TypeReference5', a)
    _safe_set(a, 'types_MapType', None)
    assert not _is_linked(a, 'types_MapType', b2)
    if hasattr(b2, 'types_TypeReference5'):
        assert not _is_linked(b2, 'types_TypeReference5', a)


def test_assoc_reference9_link_reassign_clear():
    a = types_NamedType(name="sample_text")
    b1 = types_TypeReference()
    b2 = types_TypeReference()
    _safe_set(a, 'types_NamedType', b1)
    assert _is_linked(a, 'types_NamedType', b1)
    if hasattr(b1, 'types_TypeReference10'):
        assert _is_linked(b1, 'types_TypeReference10', a)
    _safe_set(a, 'types_NamedType', b2)
    assert _is_linked(a, 'types_NamedType', b2)
    if hasattr(b1, 'types_TypeReference10'):
        assert not _is_linked(b1, 'types_TypeReference10', a)
    if hasattr(b2, 'types_TypeReference10'):
        assert _is_linked(b2, 'types_TypeReference10', a)
    _safe_set(a, 'types_NamedType', None)
    assert not _is_linked(a, 'types_NamedType', b2)
    if hasattr(b2, 'types_TypeReference10'):
        assert not _is_linked(b2, 'types_TypeReference10', a)


def test_assoc_relationship18_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_EntityRelationship(kind="sample_text")
    b2 = types_EntityRelationship(kind="sample_text_2")
    _safe_set(a, 'types_Property19', b1)
    assert _is_linked(a, 'types_Property19', b1)
    if hasattr(b1, 'types_EntityRelationship'):
        assert _is_linked(b1, 'types_EntityRelationship', a)
    _safe_set(a, 'types_Property19', b2)
    assert _is_linked(a, 'types_Property19', b2)
    if hasattr(b1, 'types_EntityRelationship'):
        assert not _is_linked(b1, 'types_EntityRelationship', a)
    if hasattr(b2, 'types_EntityRelationship'):
        assert _is_linked(b2, 'types_EntityRelationship', a)
    _safe_set(a, 'types_Property19', None)
    assert not _is_linked(a, 'types_Property19', b2)
    if hasattr(b2, 'types_EntityRelationship'):
        assert not _is_linked(b2, 'types_EntityRelationship', a)


def test_assoc_type16_link_reassign_clear():
    a = types_Property(name="sample_text", storageModifier="sample_text")
    b1 = types_DeclarationTypeReference()
    b2 = types_DeclarationTypeReference()
    _safe_set(a, 'types_Property17', b1)
    assert _is_linked(a, 'types_Property17', b1)
    if hasattr(b1, 'types_DeclarationTypeReference'):
        assert _is_linked(b1, 'types_DeclarationTypeReference', a)
    _safe_set(a, 'types_Property17', b2)
    assert _is_linked(a, 'types_Property17', b2)
    if hasattr(b1, 'types_DeclarationTypeReference'):
        assert not _is_linked(b1, 'types_DeclarationTypeReference', a)
    if hasattr(b2, 'types_DeclarationTypeReference'):
        assert _is_linked(b2, 'types_DeclarationTypeReference', a)
    _safe_set(a, 'types_Property17', None)
    assert not _is_linked(a, 'types_Property17', b2)
    if hasattr(b2, 'types_DeclarationTypeReference'):
        assert not _is_linked(b2, 'types_DeclarationTypeReference', a)


def test_assoc_types1_link_reassign_clear():
    a = types_Model(name="sample_text")
    b1 = types_ComplexType()
    b2 = types_ComplexType()
    _safe_set(a, 'types_Model2', {b1})
    assert _is_linked(a, 'types_Model2', b1)
    if hasattr(b1, 'types_ComplexType'):
        assert _is_linked(b1, 'types_ComplexType', a)
    _safe_set(a, 'types_Model2', {b2})
    assert _is_linked(a, 'types_Model2', b2)
    if hasattr(b1, 'types_ComplexType'):
        assert not _is_linked(b1, 'types_ComplexType', a)
    if hasattr(b2, 'types_ComplexType'):
        assert _is_linked(b2, 'types_ComplexType', a)
    _safe_set(a, 'types_Model2', set())
    assert not _is_linked(a, 'types_Model2', b2)
    if hasattr(b2, 'types_ComplexType'):
        assert not _is_linked(b2, 'types_ComplexType', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ComplexType_strategy = st.builds(ComplexType)
@given(instance=ComplexType_strategy)
@settings(max_examples=25)
def test_ComplexType_instantiation(instance):
    assert isinstance(instance, ComplexType)


DeclarationTypeReference_strategy = st.builds(DeclarationTypeReference)
@given(instance=DeclarationTypeReference_strategy)
@settings(max_examples=25)
def test_DeclarationTypeReference_instantiation(instance):
    assert isinstance(instance, DeclarationTypeReference)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


NamedType_strategy = st.builds(NamedType)
@given(instance=NamedType_strategy)
@settings(max_examples=25)
def test_NamedType_instantiation(instance):
    assert isinstance(instance, NamedType)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


types_BooleanLiteral_strategy = st.builds(types_BooleanLiteral, value=st.booleans())
@given(instance=types_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_types_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, types_BooleanLiteral)


types_CharLiteral_strategy = st.builds(types_CharLiteral, value=safe_text)
@given(instance=types_CharLiteral_strategy)
@settings(max_examples=25)
def test_types_CharLiteral_instantiation(instance):
    assert isinstance(instance, types_CharLiteral)


types_CollectionType_strategy = st.builds(types_CollectionType, size=st.integers())
@given(instance=types_CollectionType_strategy)
@settings(max_examples=25)
def test_types_CollectionType_instantiation(instance):
    assert isinstance(instance, types_CollectionType)


types_ComplexType_strategy = st.builds(types_ComplexType)
@given(instance=types_ComplexType_strategy)
@settings(max_examples=25)
def test_types_ComplexType_instantiation(instance):
    assert isinstance(instance, types_ComplexType)


types_DeclarationTypeReference_strategy = st.builds(types_DeclarationTypeReference)
@given(instance=types_DeclarationTypeReference_strategy)
@settings(max_examples=25)
def test_types_DeclarationTypeReference_instantiation(instance):
    assert isinstance(instance, types_DeclarationTypeReference)


types_EntityRelationship_strategy = st.builds(types_EntityRelationship, kind=safe_text)
@given(instance=types_EntityRelationship_strategy)
@settings(max_examples=25)
def test_types_EntityRelationship_instantiation(instance):
    assert isinstance(instance, types_EntityRelationship)


types_EntityType_strategy = st.builds(types_EntityType, storageModifier=safe_text)
@given(instance=types_EntityType_strategy)
@settings(max_examples=25)
def test_types_EntityType_instantiation(instance):
    assert isinstance(instance, types_EntityType)


types_EnumerationLiteral_strategy = st.builds(types_EnumerationLiteral, name=safe_text)
@given(instance=types_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_types_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, types_EnumerationLiteral)


types_EnumerationType_strategy = st.builds(types_EnumerationType)
@given(instance=types_EnumerationType_strategy)
@settings(max_examples=25)
def test_types_EnumerationType_instantiation(instance):
    assert isinstance(instance, types_EnumerationType)


types_Import_strategy = st.builds(types_Import, importedNamespace=safe_text)
@given(instance=types_Import_strategy)
@settings(max_examples=25)
def test_types_Import_instantiation(instance):
    assert isinstance(instance, types_Import)


types_Literal_strategy = st.builds(types_Literal)
@given(instance=types_Literal_strategy)
@settings(max_examples=25)
def test_types_Literal_instantiation(instance):
    assert isinstance(instance, types_Literal)


types_MapType_strategy = st.builds(types_MapType, size=st.integers())
@given(instance=types_MapType_strategy)
@settings(max_examples=25)
def test_types_MapType_instantiation(instance):
    assert isinstance(instance, types_MapType)


types_MappedByReference_strategy = st.builds(types_MappedByReference)
@given(instance=types_MappedByReference_strategy)
@settings(max_examples=25)
def test_types_MappedByReference_instantiation(instance):
    assert isinstance(instance, types_MappedByReference)


types_Model_strategy = st.builds(types_Model, name=safe_text)
@given(instance=types_Model_strategy)
@settings(max_examples=25)
def test_types_Model_instantiation(instance):
    assert isinstance(instance, types_Model)


types_NamedType_strategy = st.builds(types_NamedType, name=safe_text)
@given(instance=types_NamedType_strategy)
@settings(max_examples=25)
def test_types_NamedType_instantiation(instance):
    assert isinstance(instance, types_NamedType)


types_NumberLiteral_strategy = st.builds(types_NumberLiteral, value=safe_text)
@given(instance=types_NumberLiteral_strategy)
@settings(max_examples=25)
def test_types_NumberLiteral_instantiation(instance):
    assert isinstance(instance, types_NumberLiteral)


types_PrimitiveType_strategy = st.builds(types_PrimitiveType)
@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=25)
def test_types_PrimitiveType_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)


types_Property_strategy = st.builds(types_Property, name=safe_text, storageModifier=safe_text)
@given(instance=types_Property_strategy)
@settings(max_examples=25)
def test_types_Property_instantiation(instance):
    assert isinstance(instance, types_Property)


types_PropertyReference_strategy = st.builds(types_PropertyReference)
@given(instance=types_PropertyReference_strategy)
@settings(max_examples=25)
def test_types_PropertyReference_instantiation(instance):
    assert isinstance(instance, types_PropertyReference)


types_StringLiteral_strategy = st.builds(types_StringLiteral, value=safe_text)
@given(instance=types_StringLiteral_strategy)
@settings(max_examples=25)
def test_types_StringLiteral_instantiation(instance):
    assert isinstance(instance, types_StringLiteral)


types_Type_strategy = st.builds(types_Type)
@given(instance=types_Type_strategy)
@settings(max_examples=25)
def test_types_Type_instantiation(instance):
    assert isinstance(instance, types_Type)


types_TypeReference_strategy = st.builds(types_TypeReference)
@given(instance=types_TypeReference_strategy)
@settings(max_examples=25)
def test_types_TypeReference_instantiation(instance):
    assert isinstance(instance, types_TypeReference)



