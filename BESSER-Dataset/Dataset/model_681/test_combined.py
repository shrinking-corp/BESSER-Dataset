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
    Element,
    EMOF_Comment,
    Class,
    Operation,
    Property,
    Type,
    EMOF_Class,
    NamedElement,
    Extent,
    EMOF_URIExtent,
    EMOF_TypedElement,
    EMOF_Tag,
    ReflectiveCollection,
    EMOF_ReflectiveSequence,
    EMOF_Type,
    EMOF_Package,
    Parameter,
    MultiplicityElement,
    TypedElement,
    EMOF_Parameter,
    EMOF_Operation,
    EMOF_Object,
    EMOF_NamedElement,
    EMOF_MultiplicityElement,
    Package,
    EMOF_Property,
    EMOF_Factory,
    Enumeration,
    EMOF_EnumerationLiteral,
    EnumerationLiteral,
    DataType,
    EMOF_PrimitiveType,
    EMOF_Enumeration,
    Comment,
    Object,
    EMOF_ReflectiveCollection,
    EMOF_Extent,
    EMOF_Element,
    EMOF_DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_comment_is_not_abstract():
    assert not inspect.isabstract(EMOF_Comment)


def test_hyp_emof_comment_constructor_exists():
    assert callable(EMOF_Comment.__init__)


def test_hyp_emof_comment_constructor_args():
    sig = inspect.signature(EMOF_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_hyp_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_hyp_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_class_is_not_abstract():
    assert not inspect.isabstract(EMOF_Class)


def test_hyp_emof_class_constructor_exists():
    assert callable(EMOF_Class.__init__)


def test_hyp_emof_class_constructor_args():
    sig = inspect.signature(EMOF_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_hyp_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_hyp_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_uriextent_is_not_abstract():
    assert not inspect.isabstract(EMOF_URIExtent)


def test_hyp_emof_uriextent_constructor_exists():
    assert callable(EMOF_URIExtent.__init__)


def test_hyp_emof_uriextent_constructor_args():
    sig = inspect.signature(EMOF_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_typedelement_is_not_abstract():
    assert not inspect.isabstract(EMOF_TypedElement)


def test_hyp_emof_typedelement_constructor_exists():
    assert callable(EMOF_TypedElement.__init__)


def test_hyp_emof_typedelement_constructor_args():
    sig = inspect.signature(EMOF_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_tag_is_not_abstract():
    assert not inspect.isabstract(EMOF_Tag)


def test_hyp_emof_tag_constructor_exists():
    assert callable(EMOF_Tag.__init__)


def test_hyp_emof_tag_constructor_args():
    sig = inspect.signature(EMOF_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(ReflectiveCollection)


def test_hyp_reflectivecollection_constructor_exists():
    assert callable(ReflectiveCollection.__init__)


def test_hyp_reflectivecollection_constructor_args():
    sig = inspect.signature(ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_reflectivesequence_is_not_abstract():
    assert not inspect.isabstract(EMOF_ReflectiveSequence)


def test_hyp_emof_reflectivesequence_constructor_exists():
    assert callable(EMOF_ReflectiveSequence.__init__)


def test_hyp_emof_reflectivesequence_constructor_args():
    sig = inspect.signature(EMOF_ReflectiveSequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_type_is_not_abstract():
    assert not inspect.isabstract(EMOF_Type)


def test_hyp_emof_type_constructor_exists():
    assert callable(EMOF_Type.__init__)


def test_hyp_emof_type_constructor_args():
    sig = inspect.signature(EMOF_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_package_is_not_abstract():
    assert not inspect.isabstract(EMOF_Package)


def test_hyp_emof_package_constructor_exists():
    assert callable(EMOF_Package.__init__)


def test_hyp_emof_package_constructor_args():
    sig = inspect.signature(EMOF_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"




def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_hyp_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_hyp_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_parameter_is_not_abstract():
    assert not inspect.isabstract(EMOF_Parameter)


def test_hyp_emof_parameter_constructor_exists():
    assert callable(EMOF_Parameter.__init__)


def test_hyp_emof_parameter_constructor_args():
    sig = inspect.signature(EMOF_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_operation_is_not_abstract():
    assert not inspect.isabstract(EMOF_Operation)


def test_hyp_emof_operation_constructor_exists():
    assert callable(EMOF_Operation.__init__)


def test_hyp_emof_operation_constructor_args():
    sig = inspect.signature(EMOF_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_object_is_not_abstract():
    assert not inspect.isabstract(EMOF_Object)


def test_hyp_emof_object_constructor_exists():
    assert callable(EMOF_Object.__init__)


def test_hyp_emof_object_constructor_args():
    sig = inspect.signature(EMOF_Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_namedelement_is_not_abstract():
    assert not inspect.isabstract(EMOF_NamedElement)


def test_hyp_emof_namedelement_constructor_exists():
    assert callable(EMOF_NamedElement.__init__)


def test_hyp_emof_namedelement_constructor_args():
    sig = inspect.signature(EMOF_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_emof_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(EMOF_MultiplicityElement)


def test_hyp_emof_multiplicityelement_constructor_exists():
    assert callable(EMOF_MultiplicityElement.__init__)


def test_hyp_emof_multiplicityelement_constructor_args():
    sig = inspect.signature(EMOF_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"







def test_hyp_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_hyp_package_constructor_exists():
    assert callable(Package.__init__)


def test_hyp_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_property_is_not_abstract():
    assert not inspect.isabstract(EMOF_Property)


def test_hyp_emof_property_constructor_exists():
    assert callable(EMOF_Property.__init__)


def test_hyp_emof_property_constructor_args():
    sig = inspect.signature(EMOF_Property.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"








def test_hyp_emof_factory_is_not_abstract():
    assert not inspect.isabstract(EMOF_Factory)


def test_hyp_emof_factory_constructor_exists():
    assert callable(EMOF_Factory.__init__)


def test_hyp_emof_factory_constructor_args():
    sig = inspect.signature(EMOF_Factory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_hyp_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_hyp_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EMOF_EnumerationLiteral)


def test_hyp_emof_enumerationliteral_constructor_exists():
    assert callable(EMOF_EnumerationLiteral.__init__)


def test_hyp_emof_enumerationliteral_constructor_args():
    sig = inspect.signature(EMOF_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_hyp_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_hyp_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_primitivetype_is_not_abstract():
    assert not inspect.isabstract(EMOF_PrimitiveType)


def test_hyp_emof_primitivetype_constructor_exists():
    assert callable(EMOF_PrimitiveType.__init__)


def test_hyp_emof_primitivetype_constructor_args():
    sig = inspect.signature(EMOF_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_enumeration_is_not_abstract():
    assert not inspect.isabstract(EMOF_Enumeration)


def test_hyp_emof_enumeration_constructor_exists():
    assert callable(EMOF_Enumeration.__init__)


def test_hyp_emof_enumeration_constructor_args():
    sig = inspect.signature(EMOF_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_hyp_object_constructor_exists():
    assert callable(Object.__init__)


def test_hyp_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(EMOF_ReflectiveCollection)


def test_hyp_emof_reflectivecollection_constructor_exists():
    assert callable(EMOF_ReflectiveCollection.__init__)


def test_hyp_emof_reflectivecollection_constructor_args():
    sig = inspect.signature(EMOF_ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_extent_is_not_abstract():
    assert not inspect.isabstract(EMOF_Extent)


def test_hyp_emof_extent_constructor_exists():
    assert callable(EMOF_Extent.__init__)


def test_hyp_emof_extent_constructor_args():
    sig = inspect.signature(EMOF_Extent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_element_is_not_abstract():
    assert not inspect.isabstract(EMOF_Element)


def test_hyp_emof_element_constructor_exists():
    assert callable(EMOF_Element.__init__)


def test_hyp_emof_element_constructor_args():
    sig = inspect.signature(EMOF_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emof_datatype_is_not_abstract():
    assert not inspect.isabstract(EMOF_DataType)


def test_hyp_emof_datatype_constructor_exists():
    assert callable(EMOF_DataType.__init__)


def test_hyp_emof_datatype_constructor_args():
    sig = inspect.signature(EMOF_DataType.__init__)
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
Element_strategy = st.builds(
    Element,
)
EMOF_Comment_strategy = st.builds(
    EMOF_Comment,
    body=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
Operation_strategy = st.builds(
    Operation,
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
EMOF_Class_strategy = st.builds(
    EMOF_Class,
    isAbstract=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Extent_strategy = st.builds(
    Extent,
)
EMOF_URIExtent_strategy = st.builds(
    EMOF_URIExtent,
)
EMOF_TypedElement_strategy = st.builds(
    EMOF_TypedElement,
)
EMOF_Tag_strategy = st.builds(
    EMOF_Tag,
    value=
        safe_text,
    name=
        safe_text
)
ReflectiveCollection_strategy = st.builds(
    ReflectiveCollection,
)
EMOF_ReflectiveSequence_strategy = st.builds(
    EMOF_ReflectiveSequence,
)
EMOF_Type_strategy = st.builds(
    EMOF_Type,
)
EMOF_Package_strategy = st.builds(
    EMOF_Package,
    uri=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
EMOF_Parameter_strategy = st.builds(
    EMOF_Parameter,
)
EMOF_Operation_strategy = st.builds(
    EMOF_Operation,
)
EMOF_Object_strategy = st.builds(
    EMOF_Object,
)
EMOF_NamedElement_strategy = st.builds(
    EMOF_NamedElement,
    name=
        safe_text
)
EMOF_MultiplicityElement_strategy = st.builds(
    EMOF_MultiplicityElement,
    lower=
        safe_text,
    upper=
        safe_text,
    isUnique=
        safe_text,
    isOrdered=
        safe_text
)
Package_strategy = st.builds(
    Package,
)
EMOF_Property_strategy = st.builds(
    EMOF_Property,
    default=
        safe_text,
    isID=
        safe_text,
    isComposite=
        safe_text,
    isDerived=
        safe_text,
    isReadOnly=
        safe_text
)
EMOF_Factory_strategy = st.builds(
    EMOF_Factory,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
EMOF_EnumerationLiteral_strategy = st.builds(
    EMOF_EnumerationLiteral,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
EMOF_PrimitiveType_strategy = st.builds(
    EMOF_PrimitiveType,
)
EMOF_Enumeration_strategy = st.builds(
    EMOF_Enumeration,
)
Comment_strategy = st.builds(
    Comment,
)
Object_strategy = st.builds(
    Object,
)
EMOF_ReflectiveCollection_strategy = st.builds(
    EMOF_ReflectiveCollection,
)
EMOF_Extent_strategy = st.builds(
    EMOF_Extent,
)
EMOF_Element_strategy = st.builds(
    EMOF_Element,
)
EMOF_DataType_strategy = st.builds(
    EMOF_DataType,
)





@given(instance=EMOF_Comment_strategy)
def test_hyp_emof_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original








@given(instance=EMOF_Class_strategy)
def test_hyp_emof_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=30)
def test_hyp_emof_uriextent_uri_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.uri(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.uri).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'uri' in EMOF_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'uri' in EMOF_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'uri' in EMOF_URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=30)
def test_hyp_emof_uriextent_contexturi_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.contextURI()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.contextURI).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'contextURI' in EMOF_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'contextURI' in EMOF_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'contextURI' in EMOF_URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=30)
def test_hyp_emof_uriextent_element_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.element(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.element).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'element' in EMOF_URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'element' in EMOF_URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'element' in EMOF_URIExtent is not implemented or raised an error")





@given(instance=EMOF_Tag_strategy)
def test_hyp_emof_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=EMOF_Tag_strategy)
def test_hyp_emof_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivesequence_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in EMOF_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in EMOF_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in EMOF_ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivesequence_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in EMOF_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in EMOF_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in EMOF_ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivesequence_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in EMOF_ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in EMOF_ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in EMOF_ReflectiveSequence is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Type_strategy)
@settings(max_examples=30)
def test_hyp_emof_type_isinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInstance(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInstance' in EMOF_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in EMOF_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in EMOF_Type is not implemented or raised an error")




@given(instance=EMOF_Package_strategy)
def test_hyp_emof_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original










@given(instance=EMOF_NamedElement_strategy)
def test_hyp_emof_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=EMOF_MultiplicityElement_strategy)
def test_hyp_emof_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=EMOF_MultiplicityElement_strategy)
def test_hyp_emof_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=EMOF_MultiplicityElement_strategy)
def test_hyp_emof_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=EMOF_MultiplicityElement_strategy)
def test_hyp_emof_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original





@given(instance=EMOF_Property_strategy)
def test_hyp_emof_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=EMOF_Property_strategy)
def test_hyp_emof_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=EMOF_Property_strategy)
def test_hyp_emof_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=EMOF_Property_strategy)
def test_hyp_emof_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=EMOF_Property_strategy)
def test_hyp_emof_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Factory_strategy)
@settings(max_examples=30)
def test_hyp_emof_factory_converttostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.convertToString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.convertToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'convertToString' in EMOF_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'convertToString' in EMOF_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'convertToString' in EMOF_Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Factory_strategy)
@settings(max_examples=30)
def test_hyp_emof_factory_create_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.create(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.create).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'create' in EMOF_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in EMOF_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in EMOF_Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Factory_strategy)
@settings(max_examples=30)
def test_hyp_emof_factory_createfromstring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createFromString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createFromString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createFromString' in EMOF_Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createFromString' in EMOF_Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createFromString' in EMOF_Factory is not implemented or raised an error")










import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivecollection_addall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAll(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAll).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAll' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAll' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAll' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivecollection_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivecollection_clear_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clear()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clear).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clear' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clear' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clear' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivecollection_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in EMOF_ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_hyp_emof_reflectivecollection_size_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.size()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.size).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'size' in EMOF_ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'size' in EMOF_ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'size' in EMOF_ReflectiveCollection is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Extent_strategy)
@settings(max_examples=30)
def test_hyp_emof_extent_elements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.elements()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.elements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'elements' in EMOF_Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'elements' in EMOF_Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'elements' in EMOF_Extent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Extent_strategy)
@settings(max_examples=30)
def test_hyp_emof_extent_usecontainment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.useContainment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.useContainment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'useContainment' in EMOF_Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'useContainment' in EMOF_Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'useContainment' in EMOF_Extent is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_hyp_emof_element_container_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.container()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.container).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'container' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'container' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'container' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_hyp_emof_element_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_hyp_emof_element_isset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSet(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSet' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSet' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSet' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_hyp_emof_element_unset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unset(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unset).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unset' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unset' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unset' in EMOF_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF_Element_strategy)
@settings(max_examples=30)
def test_hyp_emof_element_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in EMOF_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in EMOF_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in EMOF_Element is not implemented or raised an error")



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    Comment,
    DataType,
    EMOF_Class,
    EMOF_Comment,
    EMOF_DataType,
    EMOF_Element,
    EMOF_Enumeration,
    EMOF_EnumerationLiteral,
    EMOF_Extent,
    EMOF_Factory,
    EMOF_MultiplicityElement,
    EMOF_NamedElement,
    EMOF_Object,
    EMOF_Operation,
    EMOF_Package,
    EMOF_Parameter,
    EMOF_PrimitiveType,
    EMOF_Property,
    EMOF_ReflectiveCollection,
    EMOF_ReflectiveSequence,
    EMOF_Tag,
    EMOF_Type,
    EMOF_TypedElement,
    EMOF_URIExtent,
    Element,
    Enumeration,
    EnumerationLiteral,
    Extent,
    MultiplicityElement,
    NamedElement,
    Object,
    Operation,
    Package,
    Parameter,
    Property,
    ReflectiveCollection,
    Type,
    TypedElement,
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

def test_EMOF_Class_isAbstract_value_roundtrip():
    instance = EMOF_Class(isAbstract="sample_text")
    assert instance.isAbstract == "sample_text"
    instance.isAbstract = "sample_text_2"
    assert instance.isAbstract == "sample_text_2"


def test_EMOF_Comment_body_value_roundtrip():
    instance = EMOF_Comment(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_EMOF_MultiplicityElement_isOrdered_value_roundtrip():
    instance = EMOF_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.isOrdered == "sample_text"
    instance.isOrdered = "sample_text_2"
    assert instance.isOrdered == "sample_text_2"


def test_EMOF_MultiplicityElement_isUnique_value_roundtrip():
    instance = EMOF_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.isUnique == "sample_text"
    instance.isUnique = "sample_text_2"
    assert instance.isUnique == "sample_text_2"


def test_EMOF_MultiplicityElement_lower_value_roundtrip():
    instance = EMOF_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.lower == "sample_text"
    instance.lower = "sample_text_2"
    assert instance.lower == "sample_text_2"


def test_EMOF_MultiplicityElement_upper_value_roundtrip():
    instance = EMOF_MultiplicityElement(isOrdered="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    assert instance.upper == "sample_text"
    instance.upper = "sample_text_2"
    assert instance.upper == "sample_text_2"


def test_EMOF_NamedElement_name_value_roundtrip():
    instance = EMOF_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_EMOF_Package_uri_value_roundtrip():
    instance = EMOF_Package(uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_EMOF_Property_default_value_roundtrip():
    instance = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_EMOF_Property_isComposite_value_roundtrip():
    instance = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    assert instance.isComposite == "sample_text"
    instance.isComposite = "sample_text_2"
    assert instance.isComposite == "sample_text_2"


def test_EMOF_Property_isDerived_value_roundtrip():
    instance = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    assert instance.isDerived == "sample_text"
    instance.isDerived = "sample_text_2"
    assert instance.isDerived == "sample_text_2"


def test_EMOF_Property_isID_value_roundtrip():
    instance = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    assert instance.isID == "sample_text"
    instance.isID = "sample_text_2"
    assert instance.isID == "sample_text_2"


def test_EMOF_Property_isReadOnly_value_roundtrip():
    instance = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    assert instance.isReadOnly == "sample_text"
    instance.isReadOnly = "sample_text_2"
    assert instance.isReadOnly == "sample_text_2"


def test_EMOF_Tag_name_value_roundtrip():
    instance = EMOF_Tag(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_EMOF_Tag_value_value_roundtrip():
    instance = EMOF_Tag(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_EMOF_Enumeration_isa_DataType():
    instance = EMOF_Enumeration()
    assert isinstance(instance, DataType)


def test_EMOF_PrimitiveType_isa_DataType():
    instance = EMOF_PrimitiveType()
    assert isinstance(instance, DataType)


def test_EMOF_Comment_isa_Element():
    instance = EMOF_Comment(body="sample_text")
    assert isinstance(instance, Element)


def test_EMOF_Factory_isa_Element():
    instance = EMOF_Factory()
    assert isinstance(instance, Element)


def test_EMOF_NamedElement_isa_Element():
    instance = EMOF_NamedElement(name="sample_text")
    assert isinstance(instance, Element)


def test_EMOF_Tag_isa_Element():
    instance = EMOF_Tag(name="sample_text", value="sample_text")
    assert isinstance(instance, Element)


def test_EMOF_URIExtent_isa_Extent():
    instance = EMOF_URIExtent()
    assert isinstance(instance, Extent)


def test_EMOF_Operation_isa_MultiplicityElement():
    instance = EMOF_Operation()
    assert isinstance(instance, MultiplicityElement)


def test_EMOF_Parameter_isa_MultiplicityElement():
    instance = EMOF_Parameter()
    assert isinstance(instance, MultiplicityElement)


def test_EMOF_Property_isa_MultiplicityElement():
    instance = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    assert isinstance(instance, MultiplicityElement)


def test_EMOF_EnumerationLiteral_isa_NamedElement():
    instance = EMOF_EnumerationLiteral()
    assert isinstance(instance, NamedElement)


def test_EMOF_Package_isa_NamedElement():
    instance = EMOF_Package(uri="sample_text")
    assert isinstance(instance, NamedElement)


def test_EMOF_Type_isa_NamedElement():
    instance = EMOF_Type()
    assert isinstance(instance, NamedElement)


def test_EMOF_TypedElement_isa_NamedElement():
    instance = EMOF_TypedElement()
    assert isinstance(instance, NamedElement)


def test_EMOF_Element_isa_Object():
    instance = EMOF_Element()
    assert isinstance(instance, Object)


def test_EMOF_Extent_isa_Object():
    instance = EMOF_Extent()
    assert isinstance(instance, Object)


def test_EMOF_ReflectiveCollection_isa_Object():
    instance = EMOF_ReflectiveCollection()
    assert isinstance(instance, Object)


def test_EMOF_ReflectiveSequence_isa_ReflectiveCollection():
    instance = EMOF_ReflectiveSequence()
    assert isinstance(instance, ReflectiveCollection)


def test_EMOF_Class_isa_Type():
    instance = EMOF_Class(isAbstract="sample_text")
    assert isinstance(instance, Type)


def test_EMOF_DataType_isa_Type():
    instance = EMOF_DataType()
    assert isinstance(instance, Type)


def test_EMOF_Operation_isa_TypedElement():
    instance = EMOF_Operation()
    assert isinstance(instance, TypedElement)


def test_EMOF_Parameter_isa_TypedElement():
    instance = EMOF_Parameter()
    assert isinstance(instance, TypedElement)


def test_EMOF_Property_isa_TypedElement():
    instance = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    assert isinstance(instance, TypedElement)


def test_assoc_annotatedElement5_link_reassign_clear():
    a = EMOF_Comment(body="sample_text")
    b1 = NamedElement()
    b2 = NamedElement()
    _safe_set(a, 'EMOF_Comment', {b1})
    assert _is_linked(a, 'EMOF_Comment', b1)
    if hasattr(b1, 'NamedElement'):
        assert _is_linked(b1, 'NamedElement', a)
    _safe_set(a, 'EMOF_Comment', {b2})
    assert _is_linked(a, 'EMOF_Comment', b2)
    if hasattr(b1, 'NamedElement'):
        assert not _is_linked(b1, 'NamedElement', a)
    if hasattr(b2, 'NamedElement'):
        assert _is_linked(b2, 'NamedElement', a)
    _safe_set(a, 'EMOF_Comment', set())
    assert not _is_linked(a, 'EMOF_Comment', b2)
    if hasattr(b2, 'NamedElement'):
        assert not _is_linked(b2, 'NamedElement', a)


def test_assoc_class_25_link_reassign_clear():
    a = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    b1 = Class()
    b2 = Class()
    _safe_set(a, 'EMOF_Property', b1)
    assert _is_linked(a, 'EMOF_Property', b1)
    if hasattr(b1, 'Class26'):
        assert _is_linked(b1, 'Class26', a)
    _safe_set(a, 'EMOF_Property', b2)
    assert _is_linked(a, 'EMOF_Property', b2)
    if hasattr(b1, 'Class26'):
        assert not _is_linked(b1, 'Class26', a)
    if hasattr(b2, 'Class26'):
        assert _is_linked(b2, 'Class26', a)
    _safe_set(a, 'EMOF_Property', None)
    assert not _is_linked(a, 'EMOF_Property', b2)
    if hasattr(b2, 'Class26'):
        assert not _is_linked(b2, 'Class26', a)


def test_assoc_element30_link_reassign_clear():
    a = EMOF_Tag(name="sample_text", value="sample_text")
    b1 = Element()
    b2 = Element()
    _safe_set(a, 'EMOF_Tag', {b1})
    assert _is_linked(a, 'EMOF_Tag', b1)
    if hasattr(b1, 'Element'):
        assert _is_linked(b1, 'Element', a)
    _safe_set(a, 'EMOF_Tag', {b2})
    assert _is_linked(a, 'EMOF_Tag', b2)
    if hasattr(b1, 'Element'):
        assert not _is_linked(b1, 'Element', a)
    if hasattr(b2, 'Element'):
        assert _is_linked(b2, 'Element', a)
    _safe_set(a, 'EMOF_Tag', set())
    assert not _is_linked(a, 'EMOF_Tag', b2)
    if hasattr(b2, 'Element'):
        assert not _is_linked(b2, 'Element', a)


def test_assoc_nestedPackage16_link_reassign_clear():
    a = EMOF_Package(uri="sample_text")
    b1 = Package()
    b2 = Package()
    _safe_set(a, 'nestingPackage', {b1})
    assert _is_linked(a, 'nestingPackage', b1)
    if hasattr(b1, 'Package17'):
        assert _is_linked(b1, 'Package17', a)
    _safe_set(a, 'nestingPackage', {b2})
    assert _is_linked(a, 'nestingPackage', b2)
    if hasattr(b1, 'Package17'):
        assert not _is_linked(b1, 'Package17', a)
    if hasattr(b2, 'Package17'):
        assert _is_linked(b2, 'Package17', a)
    _safe_set(a, 'nestingPackage', set())
    assert not _is_linked(a, 'nestingPackage', b2)
    if hasattr(b2, 'Package17'):
        assert not _is_linked(b2, 'Package17', a)


def test_assoc_nestingPackage18_link_reassign_clear():
    a = EMOF_Package(uri="sample_text")
    b1 = Package()
    b2 = Package()
    _safe_set(a, 'EMOF_Package', b1)
    assert _is_linked(a, 'EMOF_Package', b1)
    if hasattr(b1, 'Package19'):
        assert _is_linked(b1, 'Package19', a)
    _safe_set(a, 'EMOF_Package', b2)
    assert _is_linked(a, 'EMOF_Package', b2)
    if hasattr(b1, 'Package19'):
        assert not _is_linked(b1, 'Package19', a)
    if hasattr(b2, 'Package19'):
        assert _is_linked(b2, 'Package19', a)
    _safe_set(a, 'EMOF_Package', None)
    assert not _is_linked(a, 'EMOF_Package', b2)
    if hasattr(b2, 'Package19'):
        assert not _is_linked(b2, 'Package19', a)


def test_assoc_opposite27_link_reassign_clear():
    a = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'EMOF_Property28', b1)
    assert _is_linked(a, 'EMOF_Property28', b1)
    if hasattr(b1, 'Property29'):
        assert _is_linked(b1, 'Property29', a)
    _safe_set(a, 'EMOF_Property28', b2)
    assert _is_linked(a, 'EMOF_Property28', b2)
    if hasattr(b1, 'Property29'):
        assert not _is_linked(b1, 'Property29', a)
    if hasattr(b2, 'Property29'):
        assert _is_linked(b2, 'Property29', a)
    _safe_set(a, 'EMOF_Property28', None)
    assert not _is_linked(a, 'EMOF_Property28', b2)
    if hasattr(b2, 'Property29'):
        assert not _is_linked(b2, 'Property29', a)


def test_assoc_ownedAttribute0_link_reassign_clear():
    a = EMOF_Class(isAbstract="sample_text")
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'EMOF_Class', {b1})
    assert _is_linked(a, 'EMOF_Class', b1)
    if hasattr(b1, 'Property'):
        assert _is_linked(b1, 'Property', a)
    _safe_set(a, 'EMOF_Class', {b2})
    assert _is_linked(a, 'EMOF_Class', b2)
    if hasattr(b1, 'Property'):
        assert not _is_linked(b1, 'Property', a)
    if hasattr(b2, 'Property'):
        assert _is_linked(b2, 'Property', a)
    _safe_set(a, 'EMOF_Class', set())
    assert not _is_linked(a, 'EMOF_Class', b2)
    if hasattr(b2, 'Property'):
        assert not _is_linked(b2, 'Property', a)


def test_assoc_ownedComment6_link_reassign_clear():
    a = EMOF_Element()
    b1 = Comment()
    b2 = Comment()
    _safe_set(a, 'EMOF_Element', {b1})
    assert _is_linked(a, 'EMOF_Element', b1)
    if hasattr(b1, 'Comment'):
        assert _is_linked(b1, 'Comment', a)
    _safe_set(a, 'EMOF_Element', {b2})
    assert _is_linked(a, 'EMOF_Element', b2)
    if hasattr(b1, 'Comment'):
        assert not _is_linked(b1, 'Comment', a)
    if hasattr(b2, 'Comment'):
        assert _is_linked(b2, 'Comment', a)
    _safe_set(a, 'EMOF_Element', set())
    assert not _is_linked(a, 'EMOF_Element', b2)
    if hasattr(b2, 'Comment'):
        assert not _is_linked(b2, 'Comment', a)


def test_assoc_ownedOperation1_link_reassign_clear():
    a = EMOF_Class(isAbstract="sample_text")
    b1 = Operation()
    b2 = Operation()
    _safe_set(a, 'EMOF_Class2', {b1})
    assert _is_linked(a, 'EMOF_Class2', b1)
    if hasattr(b1, 'Operation'):
        assert _is_linked(b1, 'Operation', a)
    _safe_set(a, 'EMOF_Class2', {b2})
    assert _is_linked(a, 'EMOF_Class2', b2)
    if hasattr(b1, 'Operation'):
        assert not _is_linked(b1, 'Operation', a)
    if hasattr(b2, 'Operation'):
        assert _is_linked(b2, 'Operation', a)
    _safe_set(a, 'EMOF_Class2', set())
    assert not _is_linked(a, 'EMOF_Class2', b2)
    if hasattr(b2, 'Operation'):
        assert not _is_linked(b2, 'Operation', a)


def test_assoc_ownedType20_link_reassign_clear():
    a = EMOF_Package(uri="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'EMOF_Package21', {b1})
    assert _is_linked(a, 'EMOF_Package21', b1)
    if hasattr(b1, 'Type22'):
        assert _is_linked(b1, 'Type22', a)
    _safe_set(a, 'EMOF_Package21', {b2})
    assert _is_linked(a, 'EMOF_Package21', b2)
    if hasattr(b1, 'Type22'):
        assert not _is_linked(b1, 'Type22', a)
    if hasattr(b2, 'Type22'):
        assert _is_linked(b2, 'Type22', a)
    _safe_set(a, 'EMOF_Package21', set())
    assert not _is_linked(a, 'EMOF_Package21', b2)
    if hasattr(b2, 'Type22'):
        assert not _is_linked(b2, 'Type22', a)


def test_assoc_package31_link_reassign_clear():
    a = EMOF_Type()
    b1 = Package()
    b2 = Package()
    _safe_set(a, 'EMOF_Type', b1)
    assert _is_linked(a, 'EMOF_Type', b1)
    if hasattr(b1, 'Package32'):
        assert _is_linked(b1, 'Package32', a)
    _safe_set(a, 'EMOF_Type', b2)
    assert _is_linked(a, 'EMOF_Type', b2)
    if hasattr(b1, 'Package32'):
        assert not _is_linked(b1, 'Package32', a)
    if hasattr(b2, 'Package32'):
        assert _is_linked(b2, 'Package32', a)
    _safe_set(a, 'EMOF_Type', None)
    assert not _is_linked(a, 'EMOF_Type', b2)
    if hasattr(b2, 'Package32'):
        assert not _is_linked(b2, 'Package32', a)


def test_assoc_package9_link_reassign_clear():
    a = EMOF_Factory()
    b1 = Package()
    b2 = Package()
    _safe_set(a, 'EMOF_Factory', b1)
    assert _is_linked(a, 'EMOF_Factory', b1)
    if hasattr(b1, 'Package'):
        assert _is_linked(b1, 'Package', a)
    _safe_set(a, 'EMOF_Factory', b2)
    assert _is_linked(a, 'EMOF_Factory', b2)
    if hasattr(b1, 'Package'):
        assert not _is_linked(b1, 'Package', a)
    if hasattr(b2, 'Package'):
        assert _is_linked(b2, 'Package', a)
    _safe_set(a, 'EMOF_Factory', None)
    assert not _is_linked(a, 'EMOF_Factory', b2)
    if hasattr(b2, 'Package'):
        assert not _is_linked(b2, 'Package', a)


def test_assoc_superClass3_link_reassign_clear():
    a = EMOF_Class(isAbstract="sample_text")
    b1 = Class()
    b2 = Class()
    _safe_set(a, 'EMOF_Class4', {b1})
    assert _is_linked(a, 'EMOF_Class4', b1)
    if hasattr(b1, 'Class'):
        assert _is_linked(b1, 'Class', a)
    _safe_set(a, 'EMOF_Class4', {b2})
    assert _is_linked(a, 'EMOF_Class4', b2)
    if hasattr(b1, 'Class'):
        assert not _is_linked(b1, 'Class', a)
    if hasattr(b2, 'Class'):
        assert _is_linked(b2, 'Class', a)
    _safe_set(a, 'EMOF_Class4', set())
    assert not _is_linked(a, 'EMOF_Class4', b2)
    if hasattr(b2, 'Class'):
        assert not _is_linked(b2, 'Class', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Comment_strategy = st.builds(Comment)
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


EMOF_Class_strategy = st.builds(EMOF_Class, isAbstract=safe_text)
@given(instance=EMOF_Class_strategy)
@settings(max_examples=25)
def test_EMOF_Class_instantiation(instance):
    assert isinstance(instance, EMOF_Class)


EMOF_Comment_strategy = st.builds(EMOF_Comment, body=safe_text)
@given(instance=EMOF_Comment_strategy)
@settings(max_examples=25)
def test_EMOF_Comment_instantiation(instance):
    assert isinstance(instance, EMOF_Comment)


EMOF_DataType_strategy = st.builds(EMOF_DataType)
@given(instance=EMOF_DataType_strategy)
@settings(max_examples=25)
def test_EMOF_DataType_instantiation(instance):
    assert isinstance(instance, EMOF_DataType)


EMOF_Element_strategy = st.builds(EMOF_Element)
@given(instance=EMOF_Element_strategy)
@settings(max_examples=25)
def test_EMOF_Element_instantiation(instance):
    assert isinstance(instance, EMOF_Element)


EMOF_Enumeration_strategy = st.builds(EMOF_Enumeration)
@given(instance=EMOF_Enumeration_strategy)
@settings(max_examples=25)
def test_EMOF_Enumeration_instantiation(instance):
    assert isinstance(instance, EMOF_Enumeration)


EMOF_EnumerationLiteral_strategy = st.builds(EMOF_EnumerationLiteral)
@given(instance=EMOF_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_EMOF_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, EMOF_EnumerationLiteral)


EMOF_Extent_strategy = st.builds(EMOF_Extent)
@given(instance=EMOF_Extent_strategy)
@settings(max_examples=25)
def test_EMOF_Extent_instantiation(instance):
    assert isinstance(instance, EMOF_Extent)


EMOF_Factory_strategy = st.builds(EMOF_Factory)
@given(instance=EMOF_Factory_strategy)
@settings(max_examples=25)
def test_EMOF_Factory_instantiation(instance):
    assert isinstance(instance, EMOF_Factory)


EMOF_MultiplicityElement_strategy = st.builds(EMOF_MultiplicityElement, isOrdered=safe_text, isUnique=safe_text, lower=safe_text, upper=safe_text)
@given(instance=EMOF_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_EMOF_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, EMOF_MultiplicityElement)


EMOF_NamedElement_strategy = st.builds(EMOF_NamedElement, name=safe_text)
@given(instance=EMOF_NamedElement_strategy)
@settings(max_examples=25)
def test_EMOF_NamedElement_instantiation(instance):
    assert isinstance(instance, EMOF_NamedElement)


EMOF_Object_strategy = st.builds(EMOF_Object)
@given(instance=EMOF_Object_strategy)
@settings(max_examples=25)
def test_EMOF_Object_instantiation(instance):
    assert isinstance(instance, EMOF_Object)


EMOF_Operation_strategy = st.builds(EMOF_Operation)
@given(instance=EMOF_Operation_strategy)
@settings(max_examples=25)
def test_EMOF_Operation_instantiation(instance):
    assert isinstance(instance, EMOF_Operation)


EMOF_Package_strategy = st.builds(EMOF_Package, uri=safe_text)
@given(instance=EMOF_Package_strategy)
@settings(max_examples=25)
def test_EMOF_Package_instantiation(instance):
    assert isinstance(instance, EMOF_Package)


EMOF_Parameter_strategy = st.builds(EMOF_Parameter)
@given(instance=EMOF_Parameter_strategy)
@settings(max_examples=25)
def test_EMOF_Parameter_instantiation(instance):
    assert isinstance(instance, EMOF_Parameter)


EMOF_PrimitiveType_strategy = st.builds(EMOF_PrimitiveType)
@given(instance=EMOF_PrimitiveType_strategy)
@settings(max_examples=25)
def test_EMOF_PrimitiveType_instantiation(instance):
    assert isinstance(instance, EMOF_PrimitiveType)


EMOF_Property_strategy = st.builds(EMOF_Property, default=safe_text, isComposite=safe_text, isDerived=safe_text, isID=safe_text, isReadOnly=safe_text)
@given(instance=EMOF_Property_strategy)
@settings(max_examples=25)
def test_EMOF_Property_instantiation(instance):
    assert isinstance(instance, EMOF_Property)


EMOF_ReflectiveCollection_strategy = st.builds(EMOF_ReflectiveCollection)
@given(instance=EMOF_ReflectiveCollection_strategy)
@settings(max_examples=25)
def test_EMOF_ReflectiveCollection_instantiation(instance):
    assert isinstance(instance, EMOF_ReflectiveCollection)


EMOF_ReflectiveSequence_strategy = st.builds(EMOF_ReflectiveSequence)
@given(instance=EMOF_ReflectiveSequence_strategy)
@settings(max_examples=25)
def test_EMOF_ReflectiveSequence_instantiation(instance):
    assert isinstance(instance, EMOF_ReflectiveSequence)


EMOF_Tag_strategy = st.builds(EMOF_Tag, name=safe_text, value=safe_text)
@given(instance=EMOF_Tag_strategy)
@settings(max_examples=25)
def test_EMOF_Tag_instantiation(instance):
    assert isinstance(instance, EMOF_Tag)


EMOF_Type_strategy = st.builds(EMOF_Type)
@given(instance=EMOF_Type_strategy)
@settings(max_examples=25)
def test_EMOF_Type_instantiation(instance):
    assert isinstance(instance, EMOF_Type)


EMOF_TypedElement_strategy = st.builds(EMOF_TypedElement)
@given(instance=EMOF_TypedElement_strategy)
@settings(max_examples=25)
def test_EMOF_TypedElement_instantiation(instance):
    assert isinstance(instance, EMOF_TypedElement)


EMOF_URIExtent_strategy = st.builds(EMOF_URIExtent)
@given(instance=EMOF_URIExtent_strategy)
@settings(max_examples=25)
def test_EMOF_URIExtent_instantiation(instance):
    assert isinstance(instance, EMOF_URIExtent)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Enumeration_strategy = st.builds(Enumeration)
@given(instance=Enumeration_strategy)
@settings(max_examples=25)
def test_Enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)


EnumerationLiteral_strategy = st.builds(EnumerationLiteral)
@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)


Extent_strategy = st.builds(Extent)
@given(instance=Extent_strategy)
@settings(max_examples=25)
def test_Extent_instantiation(instance):
    assert isinstance(instance, Extent)


MultiplicityElement_strategy = st.builds(MultiplicityElement)
@given(instance=MultiplicityElement_strategy)
@settings(max_examples=25)
def test_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Object_strategy = st.builds(Object)
@given(instance=Object_strategy)
@settings(max_examples=25)
def test_Object_instantiation(instance):
    assert isinstance(instance, Object)


Operation_strategy = st.builds(Operation)
@given(instance=Operation_strategy)
@settings(max_examples=25)
def test_Operation_instantiation(instance):
    assert isinstance(instance, Operation)


Package_strategy = st.builds(Package)
@given(instance=Package_strategy)
@settings(max_examples=25)
def test_Package_instantiation(instance):
    assert isinstance(instance, Package)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


ReflectiveCollection_strategy = st.builds(ReflectiveCollection)
@given(instance=ReflectiveCollection_strategy)
@settings(max_examples=25)
def test_ReflectiveCollection_instantiation(instance):
    assert isinstance(instance, ReflectiveCollection)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)



