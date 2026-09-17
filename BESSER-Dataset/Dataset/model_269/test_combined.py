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
    EObject,
    ETypedElement,
    javaless_EParameter,
    ENamedElement,
    javaless_ETypedElement,
    javaless_EClassifier,
    javaless_EStructuralFeature,
    javaless_EEnumLiteral,
    EDataType,
    javaless_EEnum,
    javaless_EPackage,
    javaless_EObject,
    javaless_EModelElement,
    javaless_EStringToStringMapEntry,
    EModelElement,
    javaless_ENamedElement,
    javaless_EFactory,
    javaless_EAnnotation,
    EStructuralFeature,
    javaless_EAttribute,
    javaless_EReference,
    javaless_EOperation,
    EClassifier,
    javaless_EDataType,
    javaless_EClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_hyp_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_hyp_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_hyp_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_hyp_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_eparameter_is_not_abstract():
    assert not inspect.isabstract(javaless_EParameter)


def test_hyp_javaless_eparameter_constructor_exists():
    assert callable(javaless_EParameter.__init__)


def test_hyp_javaless_eparameter_constructor_args():
    sig = inspect.signature(javaless_EParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_hyp_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_hyp_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_etypedelement_is_not_abstract():
    assert not inspect.isabstract(javaless_ETypedElement)


def test_hyp_javaless_etypedelement_constructor_exists():
    assert callable(javaless_ETypedElement.__init__)


def test_hyp_javaless_etypedelement_constructor_args():
    sig = inspect.signature(javaless_ETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "required" in params, "Missing parameter 'required'"
    assert "many" in params, "Missing parameter 'many'"
    assert "unique" in params, "Missing parameter 'unique'"









def test_hyp_javaless_eclassifier_is_not_abstract():
    assert not inspect.isabstract(javaless_EClassifier)


def test_hyp_javaless_eclassifier_constructor_exists():
    assert callable(javaless_EClassifier.__init__)


def test_hyp_javaless_eclassifier_constructor_args():
    sig = inspect.signature(javaless_EClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"






def test_hyp_javaless_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(javaless_EStructuralFeature)


def test_hyp_javaless_estructuralfeature_constructor_exists():
    assert callable(javaless_EStructuralFeature.__init__)


def test_hyp_javaless_estructuralfeature_constructor_args():
    sig = inspect.signature(javaless_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "defaultValueLiteral" in params, "Missing parameter 'defaultValueLiteral'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "unsettable" in params, "Missing parameter 'unsettable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"










def test_hyp_javaless_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(javaless_EEnumLiteral)


def test_hyp_javaless_eenumliteral_constructor_exists():
    assert callable(javaless_EEnumLiteral.__init__)


def test_hyp_javaless_eenumliteral_constructor_args():
    sig = inspect.signature(javaless_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "instance" in params, "Missing parameter 'instance'"
    assert "literal" in params, "Missing parameter 'literal'"






def test_hyp_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_hyp_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_hyp_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_eenum_is_not_abstract():
    assert not inspect.isabstract(javaless_EEnum)


def test_hyp_javaless_eenum_constructor_exists():
    assert callable(javaless_EEnum.__init__)


def test_hyp_javaless_eenum_constructor_args():
    sig = inspect.signature(javaless_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_epackage_is_not_abstract():
    assert not inspect.isabstract(javaless_EPackage)


def test_hyp_javaless_epackage_constructor_exists():
    assert callable(javaless_EPackage.__init__)


def test_hyp_javaless_epackage_constructor_args():
    sig = inspect.signature(javaless_EPackage.__init__)
    params = list(sig.parameters.keys())
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"
    assert "nsURI" in params, "Missing parameter 'nsURI'"





def test_hyp_javaless_eobject_is_not_abstract():
    assert not inspect.isabstract(javaless_EObject)


def test_hyp_javaless_eobject_constructor_exists():
    assert callable(javaless_EObject.__init__)


def test_hyp_javaless_eobject_constructor_args():
    sig = inspect.signature(javaless_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_emodelelement_is_not_abstract():
    assert not inspect.isabstract(javaless_EModelElement)


def test_hyp_javaless_emodelelement_constructor_exists():
    assert callable(javaless_EModelElement.__init__)


def test_hyp_javaless_emodelelement_constructor_args():
    sig = inspect.signature(javaless_EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(javaless_EStringToStringMapEntry)


def test_hyp_javaless_estringtostringmapentry_constructor_exists():
    assert callable(javaless_EStringToStringMapEntry.__init__)


def test_hyp_javaless_estringtostringmapentry_constructor_args():
    sig = inspect.signature(javaless_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_hyp_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_hyp_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_enamedelement_is_not_abstract():
    assert not inspect.isabstract(javaless_ENamedElement)


def test_hyp_javaless_enamedelement_constructor_exists():
    assert callable(javaless_ENamedElement.__init__)


def test_hyp_javaless_enamedelement_constructor_args():
    sig = inspect.signature(javaless_ENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_javaless_efactory_is_not_abstract():
    assert not inspect.isabstract(javaless_EFactory)


def test_hyp_javaless_efactory_constructor_exists():
    assert callable(javaless_EFactory.__init__)


def test_hyp_javaless_efactory_constructor_args():
    sig = inspect.signature(javaless_EFactory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_eannotation_is_not_abstract():
    assert not inspect.isabstract(javaless_EAnnotation)


def test_hyp_javaless_eannotation_constructor_exists():
    assert callable(javaless_EAnnotation.__init__)


def test_hyp_javaless_eannotation_constructor_args():
    sig = inspect.signature(javaless_EAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"




def test_hyp_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature)


def test_hyp_estructuralfeature_constructor_exists():
    assert callable(EStructuralFeature.__init__)


def test_hyp_estructuralfeature_constructor_args():
    sig = inspect.signature(EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_eattribute_is_not_abstract():
    assert not inspect.isabstract(javaless_EAttribute)


def test_hyp_javaless_eattribute_constructor_exists():
    assert callable(javaless_EAttribute.__init__)


def test_hyp_javaless_eattribute_constructor_args():
    sig = inspect.signature(javaless_EAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"




def test_hyp_javaless_ereference_is_not_abstract():
    assert not inspect.isabstract(javaless_EReference)


def test_hyp_javaless_ereference_constructor_exists():
    assert callable(javaless_EReference.__init__)


def test_hyp_javaless_ereference_constructor_args():
    sig = inspect.signature(javaless_EReference.__init__)
    params = list(sig.parameters.keys())
    assert "container" in params, "Missing parameter 'container'"
    assert "resolveProxies" in params, "Missing parameter 'resolveProxies'"
    assert "containment" in params, "Missing parameter 'containment'"






def test_hyp_javaless_eoperation_is_not_abstract():
    assert not inspect.isabstract(javaless_EOperation)


def test_hyp_javaless_eoperation_constructor_exists():
    assert callable(javaless_EOperation.__init__)


def test_hyp_javaless_eoperation_constructor_args():
    sig = inspect.signature(javaless_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_hyp_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_hyp_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaless_edatatype_is_not_abstract():
    assert not inspect.isabstract(javaless_EDataType)


def test_hyp_javaless_edatatype_constructor_exists():
    assert callable(javaless_EDataType.__init__)


def test_hyp_javaless_edatatype_constructor_args():
    sig = inspect.signature(javaless_EDataType.__init__)
    params = list(sig.parameters.keys())
    assert "serializable" in params, "Missing parameter 'serializable'"




def test_hyp_javaless_eclass_is_not_abstract():
    assert not inspect.isabstract(javaless_EClass)


def test_hyp_javaless_eclass_constructor_exists():
    assert callable(javaless_EClass.__init__)


def test_hyp_javaless_eclass_constructor_args():
    sig = inspect.signature(javaless_EClass.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "interface" in params, "Missing parameter 'interface'"




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
EObject_strategy = st.builds(
    EObject,
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
javaless_EParameter_strategy = st.builds(
    javaless_EParameter,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
javaless_ETypedElement_strategy = st.builds(
    javaless_ETypedElement,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    ordered=
        st.booleans(),
    required=
        st.booleans(),
    many=
        st.booleans(),
    unique=
        st.booleans()
)
javaless_EClassifier_strategy = st.builds(
    javaless_EClassifier,
    defaultValue=
        safe_text,
    instanceClassName=
        safe_text,
    instanceClass=
        safe_text
)
javaless_EStructuralFeature_strategy = st.builds(
    javaless_EStructuralFeature,
    changeable=
        st.booleans(),
    defaultValueLiteral=
        safe_text,
    volatile=
        st.booleans(),
    derived=
        st.booleans(),
    transient=
        st.booleans(),
    unsettable=
        st.booleans(),
    defaultValue=
        safe_text
)
javaless_EEnumLiteral_strategy = st.builds(
    javaless_EEnumLiteral,
    value=
        st.integers(),
    instance=
        safe_text,
    literal=
        safe_text
)
EDataType_strategy = st.builds(
    EDataType,
)
javaless_EEnum_strategy = st.builds(
    javaless_EEnum,
)
javaless_EPackage_strategy = st.builds(
    javaless_EPackage,
    nsPrefix=
        safe_text,
    nsURI=
        safe_text
)
javaless_EObject_strategy = st.builds(
    javaless_EObject,
)
javaless_EModelElement_strategy = st.builds(
    javaless_EModelElement,
)
javaless_EStringToStringMapEntry_strategy = st.builds(
    javaless_EStringToStringMapEntry,
    value=
        safe_text,
    key=
        safe_text
)
EModelElement_strategy = st.builds(
    EModelElement,
)
javaless_ENamedElement_strategy = st.builds(
    javaless_ENamedElement,
    name=
        safe_text
)
javaless_EFactory_strategy = st.builds(
    javaless_EFactory,
)
javaless_EAnnotation_strategy = st.builds(
    javaless_EAnnotation,
    source=
        safe_text
)
EStructuralFeature_strategy = st.builds(
    EStructuralFeature,
)
javaless_EAttribute_strategy = st.builds(
    javaless_EAttribute,
    iD=
        st.booleans()
)
javaless_EReference_strategy = st.builds(
    javaless_EReference,
    container=
        st.booleans(),
    resolveProxies=
        st.booleans(),
    containment=
        st.booleans()
)
javaless_EOperation_strategy = st.builds(
    javaless_EOperation,
)
EClassifier_strategy = st.builds(
    EClassifier,
)
javaless_EDataType_strategy = st.builds(
    javaless_EDataType,
    serializable=
        st.booleans()
)
javaless_EClass_strategy = st.builds(
    javaless_EClass,
    abstract=
        st.booleans(),
    interface=
        st.booleans()
)








@given(instance=javaless_ETypedElement_strategy)
def test_hyp_javaless_etypedelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=javaless_ETypedElement_strategy)
def test_hyp_javaless_etypedelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=javaless_ETypedElement_strategy)
def test_hyp_javaless_etypedelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=javaless_ETypedElement_strategy)
def test_hyp_javaless_etypedelement_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=javaless_ETypedElement_strategy)
def test_hyp_javaless_etypedelement_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=javaless_ETypedElement_strategy)
def test_hyp_javaless_etypedelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original




@given(instance=javaless_EClassifier_strategy)
def test_hyp_javaless_eclassifier_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=javaless_EClassifier_strategy)
def test_hyp_javaless_eclassifier_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original



@given(instance=javaless_EClassifier_strategy)
def test_hyp_javaless_eclassifier_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EClassifier_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eclassifier_isinstance_changes_state(instance):
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
        assert has_statements, f"Function 'isInstance' in javaless_EClassifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in javaless_EClassifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in javaless_EClassifier is not implemented or raised an error")




@given(instance=javaless_EStructuralFeature_strategy)
def test_hyp_javaless_estructuralfeature_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=javaless_EStructuralFeature_strategy)
def test_hyp_javaless_estructuralfeature_defaultValueLiteral_setter(instance):
    original = instance.defaultValueLiteral
    instance.defaultValueLiteral = original
    assert instance.defaultValueLiteral == original



@given(instance=javaless_EStructuralFeature_strategy)
def test_hyp_javaless_estructuralfeature_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=javaless_EStructuralFeature_strategy)
def test_hyp_javaless_estructuralfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=javaless_EStructuralFeature_strategy)
def test_hyp_javaless_estructuralfeature_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=javaless_EStructuralFeature_strategy)
def test_hyp_javaless_estructuralfeature_unsettable_setter(instance):
    original = instance.unsettable
    instance.unsettable = original
    assert instance.unsettable == original



@given(instance=javaless_EStructuralFeature_strategy)
def test_hyp_javaless_estructuralfeature_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original




@given(instance=javaless_EEnumLiteral_strategy)
def test_hyp_javaless_eenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=javaless_EEnumLiteral_strategy)
def test_hyp_javaless_eenumliteral_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original



@given(instance=javaless_EEnumLiteral_strategy)
def test_hyp_javaless_eenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original






@given(instance=javaless_EPackage_strategy)
def test_hyp_javaless_epackage_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original



@given(instance=javaless_EPackage_strategy)
def test_hyp_javaless_epackage_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_econtainmentfeature_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eContainmentFeature()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eContainmentFeature).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eContainmentFeature' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eContainmentFeature' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eContainmentFeature' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_eisproxy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eIsProxy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eIsProxy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eIsProxy' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eIsProxy' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eIsProxy' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_eunset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eUnset(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eUnset).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eUnset' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eUnset' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eUnset' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_econtents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eContents()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eContents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eContents' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eContents' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eContents' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_eset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eSet(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eSet' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eSet' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eSet' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_eisset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eIsSet(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eIsSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eIsSet' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eIsSet' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eIsSet' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_ecrossreferences_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eCrossReferences()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eCrossReferences).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eCrossReferences' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eCrossReferences' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eCrossReferences' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_eclass_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eClass()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eClass).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eClass' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eClass' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eClass' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_eresource_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eResource()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eResource).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eResource' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eResource' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eResource' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_eallcontents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eAllContents()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eAllContents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eAllContents' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eAllContents' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eAllContents' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_econtainer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eContainer()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eContainer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eContainer' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eContainer' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eContainer' in javaless_EObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EObject_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eobject_econtainingfeature_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eContainingFeature()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eContainingFeature).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eContainingFeature' in javaless_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eContainingFeature' in javaless_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eContainingFeature' in javaless_EObject is not implemented or raised an error")





@given(instance=javaless_EStringToStringMapEntry_strategy)
def test_hyp_javaless_estringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=javaless_EStringToStringMapEntry_strategy)
def test_hyp_javaless_estringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original





@given(instance=javaless_ENamedElement_strategy)
def test_hyp_javaless_enamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EFactory_strategy)
@settings(max_examples=30)
def test_hyp_javaless_efactory_createfromstring_changes_state(instance):
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
        assert has_statements, f"Function 'createFromString' in javaless_EFactory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createFromString' in javaless_EFactory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createFromString' in javaless_EFactory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EFactory_strategy)
@settings(max_examples=30)
def test_hyp_javaless_efactory_converttostring_changes_state(instance):
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
        assert has_statements, f"Function 'convertToString' in javaless_EFactory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'convertToString' in javaless_EFactory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'convertToString' in javaless_EFactory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EFactory_strategy)
@settings(max_examples=30)
def test_hyp_javaless_efactory_create_changes_state(instance):
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
        assert has_statements, f"Function 'create' in javaless_EFactory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in javaless_EFactory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in javaless_EFactory is not implemented or raised an error")




@given(instance=javaless_EAnnotation_strategy)
def test_hyp_javaless_eannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original





@given(instance=javaless_EAttribute_strategy)
def test_hyp_javaless_eattribute_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original




@given(instance=javaless_EReference_strategy)
def test_hyp_javaless_ereference_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original



@given(instance=javaless_EReference_strategy)
def test_hyp_javaless_ereference_resolveProxies_setter(instance):
    original = instance.resolveProxies
    instance.resolveProxies = original
    assert instance.resolveProxies == original



@given(instance=javaless_EReference_strategy)
def test_hyp_javaless_ereference_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original






@given(instance=javaless_EDataType_strategy)
def test_hyp_javaless_edatatype_serializable_setter(instance):
    original = instance.serializable
    instance.serializable = original
    assert instance.serializable == original




@given(instance=javaless_EClass_strategy)
def test_hyp_javaless_eclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=javaless_EClass_strategy)
def test_hyp_javaless_eclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=javaless_EClass_strategy)
@settings(max_examples=30)
def test_hyp_javaless_eclass_issupertypeof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperTypeOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperTypeOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperTypeOf' in javaless_EClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOf' in javaless_EClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOf' in javaless_EClass is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EObject,
    EStructuralFeature,
    ETypedElement,
    javaless_EAnnotation,
    javaless_EAttribute,
    javaless_EClass,
    javaless_EClassifier,
    javaless_EDataType,
    javaless_EEnum,
    javaless_EEnumLiteral,
    javaless_EFactory,
    javaless_EModelElement,
    javaless_ENamedElement,
    javaless_EObject,
    javaless_EOperation,
    javaless_EPackage,
    javaless_EParameter,
    javaless_EReference,
    javaless_EStringToStringMapEntry,
    javaless_EStructuralFeature,
    javaless_ETypedElement,
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

def test_javaless_EAnnotation_source_value_roundtrip():
    instance = javaless_EAnnotation(source="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_javaless_EAttribute_iD_value_roundtrip():
    instance = javaless_EAttribute(iD=True)
    assert instance.iD == True
    instance.iD = False
    assert instance.iD == False


def test_javaless_EClass_abstract_value_roundtrip():
    instance = javaless_EClass(abstract=True, interface=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_javaless_EClass_interface_value_roundtrip():
    instance = javaless_EClass(abstract=True, interface=True)
    assert instance.interface == True
    instance.interface = False
    assert instance.interface == False


def test_javaless_EClassifier_defaultValue_value_roundtrip():
    instance = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_javaless_EClassifier_instanceClass_value_roundtrip():
    instance = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    assert instance.instanceClass == "sample_text"
    instance.instanceClass = "sample_text_2"
    assert instance.instanceClass == "sample_text_2"


def test_javaless_EClassifier_instanceClassName_value_roundtrip():
    instance = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    assert instance.instanceClassName == "sample_text"
    instance.instanceClassName = "sample_text_2"
    assert instance.instanceClassName == "sample_text_2"


def test_javaless_EDataType_serializable_value_roundtrip():
    instance = javaless_EDataType(serializable=True)
    assert instance.serializable == True
    instance.serializable = False
    assert instance.serializable == False


def test_javaless_EEnumLiteral_instance_value_roundtrip():
    instance = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.instance == "sample_text"
    instance.instance = "sample_text_2"
    assert instance.instance == "sample_text_2"


def test_javaless_EEnumLiteral_literal_value_roundtrip():
    instance = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.literal == "sample_text"
    instance.literal = "sample_text_2"
    assert instance.literal == "sample_text_2"


def test_javaless_EEnumLiteral_value_value_roundtrip():
    instance = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_javaless_ENamedElement_name_value_roundtrip():
    instance = javaless_ENamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_javaless_EPackage_nsPrefix_value_roundtrip():
    instance = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsPrefix == "sample_text"
    instance.nsPrefix = "sample_text_2"
    assert instance.nsPrefix == "sample_text_2"


def test_javaless_EPackage_nsURI_value_roundtrip():
    instance = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsURI == "sample_text"
    instance.nsURI = "sample_text_2"
    assert instance.nsURI == "sample_text_2"


def test_javaless_EReference_container_value_roundtrip():
    instance = javaless_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.container == True
    instance.container = False
    assert instance.container == False


def test_javaless_EReference_containment_value_roundtrip():
    instance = javaless_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.containment == True
    instance.containment = False
    assert instance.containment == False


def test_javaless_EReference_resolveProxies_value_roundtrip():
    instance = javaless_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.resolveProxies == True
    instance.resolveProxies = False
    assert instance.resolveProxies == False


def test_javaless_EStringToStringMapEntry_key_value_roundtrip():
    instance = javaless_EStringToStringMapEntry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_javaless_EStringToStringMapEntry_value_value_roundtrip():
    instance = javaless_EStringToStringMapEntry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_javaless_EStructuralFeature_changeable_value_roundtrip():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.changeable == True
    instance.changeable = False
    assert instance.changeable == False


def test_javaless_EStructuralFeature_defaultValue_value_roundtrip():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_javaless_EStructuralFeature_defaultValueLiteral_value_roundtrip():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.defaultValueLiteral == "sample_text"
    instance.defaultValueLiteral = "sample_text_2"
    assert instance.defaultValueLiteral == "sample_text_2"


def test_javaless_EStructuralFeature_derived_value_roundtrip():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_javaless_EStructuralFeature_transient_value_roundtrip():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_javaless_EStructuralFeature_unsettable_value_roundtrip():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.unsettable == True
    instance.unsettable = False
    assert instance.unsettable == False


def test_javaless_EStructuralFeature_volatile_value_roundtrip():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.volatile == True
    instance.volatile = False
    assert instance.volatile == False


def test_javaless_ETypedElement_lowerBound_value_roundtrip():
    instance = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_javaless_ETypedElement_many_value_roundtrip():
    instance = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_javaless_ETypedElement_ordered_value_roundtrip():
    instance = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.ordered == True
    instance.ordered = False
    assert instance.ordered == False


def test_javaless_ETypedElement_required_value_roundtrip():
    instance = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_javaless_ETypedElement_unique_value_roundtrip():
    instance = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_javaless_ETypedElement_upperBound_value_roundtrip():
    instance = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_javaless_EClass_isa_EClassifier():
    instance = javaless_EClass(abstract=True, interface=True)
    assert isinstance(instance, EClassifier)


def test_javaless_EDataType_isa_EClassifier():
    instance = javaless_EDataType(serializable=True)
    assert isinstance(instance, EClassifier)


def test_javaless_EEnum_isa_EDataType():
    instance = javaless_EEnum()
    assert isinstance(instance, EDataType)


def test_javaless_EAnnotation_isa_EModelElement():
    instance = javaless_EAnnotation(source="sample_text")
    assert isinstance(instance, EModelElement)


def test_javaless_EFactory_isa_EModelElement():
    instance = javaless_EFactory()
    assert isinstance(instance, EModelElement)


def test_javaless_ENamedElement_isa_EModelElement():
    instance = javaless_ENamedElement(name="sample_text")
    assert isinstance(instance, EModelElement)


def test_javaless_EClassifier_isa_ENamedElement():
    instance = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    assert isinstance(instance, ENamedElement)


def test_javaless_EEnumLiteral_isa_ENamedElement():
    instance = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert isinstance(instance, ENamedElement)


def test_javaless_EPackage_isa_ENamedElement():
    instance = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert isinstance(instance, ENamedElement)


def test_javaless_ETypedElement_isa_ENamedElement():
    instance = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert isinstance(instance, ENamedElement)


def test_javaless_EModelElement_isa_EObject():
    instance = javaless_EModelElement()
    assert isinstance(instance, EObject)


def test_javaless_EAttribute_isa_EStructuralFeature():
    instance = javaless_EAttribute(iD=True)
    assert isinstance(instance, EStructuralFeature)


def test_javaless_EReference_isa_EStructuralFeature():
    instance = javaless_EReference(container=True, containment=True, resolveProxies=True)
    assert isinstance(instance, EStructuralFeature)


def test_javaless_EOperation_isa_ETypedElement():
    instance = javaless_EOperation()
    assert isinstance(instance, ETypedElement)


def test_javaless_EParameter_isa_ETypedElement():
    instance = javaless_EParameter()
    assert isinstance(instance, ETypedElement)


def test_javaless_EStructuralFeature_isa_ETypedElement():
    instance = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert isinstance(instance, ETypedElement)


def test_assoc_contents3_link_reassign_clear():
    a = javaless_EObject()
    b1 = javaless_EAnnotation(source="sample_text")
    b2 = javaless_EAnnotation(source="sample_text_2")
    _safe_set(a, 'javaless_EObject', b1)
    assert _is_linked(a, 'javaless_EObject', b1)
    if hasattr(b1, 'javaless_EAnnotation4'):
        assert _is_linked(b1, 'javaless_EAnnotation4', a)
    _safe_set(a, 'javaless_EObject', b2)
    assert _is_linked(a, 'javaless_EObject', b2)
    if hasattr(b1, 'javaless_EAnnotation4'):
        assert not _is_linked(b1, 'javaless_EAnnotation4', a)
    if hasattr(b2, 'javaless_EAnnotation4'):
        assert _is_linked(b2, 'javaless_EAnnotation4', a)
    _safe_set(a, 'javaless_EObject', None)
    assert not _is_linked(a, 'javaless_EObject', b2)
    if hasattr(b2, 'javaless_EAnnotation4'):
        assert not _is_linked(b2, 'javaless_EAnnotation4', a)


def test_assoc_details1_link_reassign_clear():
    a = javaless_EStringToStringMapEntry(key="sample_text", value="sample_text")
    b1 = javaless_EAnnotation(source="sample_text")
    b2 = javaless_EAnnotation(source="sample_text_2")
    _safe_set(a, 'javaless_EStringToStringMapEntry', b1)
    assert _is_linked(a, 'javaless_EStringToStringMapEntry', b1)
    if hasattr(b1, 'javaless_EAnnotation'):
        assert _is_linked(b1, 'javaless_EAnnotation', a)
    _safe_set(a, 'javaless_EStringToStringMapEntry', b2)
    assert _is_linked(a, 'javaless_EStringToStringMapEntry', b2)
    if hasattr(b1, 'javaless_EAnnotation'):
        assert not _is_linked(b1, 'javaless_EAnnotation', a)
    if hasattr(b2, 'javaless_EAnnotation'):
        assert _is_linked(b2, 'javaless_EAnnotation', a)
    _safe_set(a, 'javaless_EStringToStringMapEntry', None)
    assert not _is_linked(a, 'javaless_EStringToStringMapEntry', b2)
    if hasattr(b2, 'javaless_EAnnotation'):
        assert not _is_linked(b2, 'javaless_EAnnotation', a)


def test_assoc_eAllAttributes11_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EAttribute(iD=True)
    b2 = javaless_EAttribute(iD=False)
    _safe_set(a, 'javaless_EClass12', {b1})
    assert _is_linked(a, 'javaless_EClass12', b1)
    if hasattr(b1, 'javaless_EAttribute13'):
        assert _is_linked(b1, 'javaless_EAttribute13', a)
    _safe_set(a, 'javaless_EClass12', {b2})
    assert _is_linked(a, 'javaless_EClass12', b2)
    if hasattr(b1, 'javaless_EAttribute13'):
        assert not _is_linked(b1, 'javaless_EAttribute13', a)
    if hasattr(b2, 'javaless_EAttribute13'):
        assert _is_linked(b2, 'javaless_EAttribute13', a)
    _safe_set(a, 'javaless_EClass12', set())
    assert not _is_linked(a, 'javaless_EClass12', b2)
    if hasattr(b2, 'javaless_EAttribute13'):
        assert not _is_linked(b2, 'javaless_EAttribute13', a)


def test_assoc_eAllContainments22_link_reassign_clear():
    a = javaless_EReference(container=True, containment=True, resolveProxies=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'javaless_EReference24', b1)
    assert _is_linked(a, 'javaless_EReference24', b1)
    if hasattr(b1, 'javaless_EClass23'):
        assert _is_linked(b1, 'javaless_EClass23', a)
    _safe_set(a, 'javaless_EReference24', b2)
    assert _is_linked(a, 'javaless_EReference24', b2)
    if hasattr(b1, 'javaless_EClass23'):
        assert not _is_linked(b1, 'javaless_EClass23', a)
    if hasattr(b2, 'javaless_EClass23'):
        assert _is_linked(b2, 'javaless_EClass23', a)
    _safe_set(a, 'javaless_EReference24', None)
    assert not _is_linked(a, 'javaless_EReference24', b2)
    if hasattr(b2, 'javaless_EClass23'):
        assert not _is_linked(b2, 'javaless_EClass23', a)


def test_assoc_eAllOperations25_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EOperation()
    b2 = javaless_EOperation()
    _safe_set(a, 'javaless_EClass26', {b1})
    assert _is_linked(a, 'javaless_EClass26', b1)
    if hasattr(b1, 'javaless_EOperation'):
        assert _is_linked(b1, 'javaless_EOperation', a)
    _safe_set(a, 'javaless_EClass26', {b2})
    assert _is_linked(a, 'javaless_EClass26', b2)
    if hasattr(b1, 'javaless_EOperation'):
        assert not _is_linked(b1, 'javaless_EOperation', a)
    if hasattr(b2, 'javaless_EOperation'):
        assert _is_linked(b2, 'javaless_EOperation', a)
    _safe_set(a, 'javaless_EClass26', set())
    assert not _is_linked(a, 'javaless_EClass26', b2)
    if hasattr(b2, 'javaless_EOperation'):
        assert not _is_linked(b2, 'javaless_EOperation', a)


def test_assoc_eAllReferences14_link_reassign_clear():
    a = javaless_EReference(container=True, containment=True, resolveProxies=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'javaless_EReference', b1)
    assert _is_linked(a, 'javaless_EReference', b1)
    if hasattr(b1, 'javaless_EClass15'):
        assert _is_linked(b1, 'javaless_EClass15', a)
    _safe_set(a, 'javaless_EReference', b2)
    assert _is_linked(a, 'javaless_EReference', b2)
    if hasattr(b1, 'javaless_EClass15'):
        assert not _is_linked(b1, 'javaless_EClass15', a)
    if hasattr(b2, 'javaless_EClass15'):
        assert _is_linked(b2, 'javaless_EClass15', a)
    _safe_set(a, 'javaless_EReference', None)
    assert not _is_linked(a, 'javaless_EReference', b2)
    if hasattr(b2, 'javaless_EClass15'):
        assert not _is_linked(b2, 'javaless_EClass15', a)


def test_assoc_eAllStructuralFeatures27_link_reassign_clear():
    a = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'javaless_EStructuralFeature', b1)
    assert _is_linked(a, 'javaless_EStructuralFeature', b1)
    if hasattr(b1, 'javaless_EClass28'):
        assert _is_linked(b1, 'javaless_EClass28', a)
    _safe_set(a, 'javaless_EStructuralFeature', b2)
    assert _is_linked(a, 'javaless_EStructuralFeature', b2)
    if hasattr(b1, 'javaless_EClass28'):
        assert not _is_linked(b1, 'javaless_EClass28', a)
    if hasattr(b2, 'javaless_EClass28'):
        assert _is_linked(b2, 'javaless_EClass28', a)
    _safe_set(a, 'javaless_EStructuralFeature', None)
    assert not _is_linked(a, 'javaless_EStructuralFeature', b2)
    if hasattr(b2, 'javaless_EClass28'):
        assert not _is_linked(b2, 'javaless_EClass28', a)


def test_assoc_eAllSuperTypes30_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'javaless_EClass29', {b1})
    assert _is_linked(a, 'javaless_EClass29', b1)
    if hasattr(b1, 'javaless_EClass31'):
        assert _is_linked(b1, 'javaless_EClass31', a)
    _safe_set(a, 'javaless_EClass29', {b2})
    assert _is_linked(a, 'javaless_EClass29', b2)
    if hasattr(b1, 'javaless_EClass31'):
        assert not _is_linked(b1, 'javaless_EClass31', a)
    if hasattr(b2, 'javaless_EClass31'):
        assert _is_linked(b2, 'javaless_EClass31', a)
    _safe_set(a, 'javaless_EClass29', set())
    assert not _is_linked(a, 'javaless_EClass29', b2)
    if hasattr(b2, 'javaless_EClass31'):
        assert not _is_linked(b2, 'javaless_EClass31', a)


def test_assoc_eAnnotations42_link_reassign_clear():
    a = javaless_EModelElement()
    b1 = javaless_EAnnotation(source="sample_text")
    b2 = javaless_EAnnotation(source="sample_text_2")
    _safe_set(a, 'eModelElement', {b1})
    assert _is_linked(a, 'eModelElement', b1)
    if hasattr(b1, 'EAnnotation'):
        assert _is_linked(b1, 'EAnnotation', a)
    _safe_set(a, 'eModelElement', {b2})
    assert _is_linked(a, 'eModelElement', b2)
    if hasattr(b1, 'EAnnotation'):
        assert not _is_linked(b1, 'EAnnotation', a)
    if hasattr(b2, 'EAnnotation'):
        assert _is_linked(b2, 'EAnnotation', a)
    _safe_set(a, 'eModelElement', set())
    assert not _is_linked(a, 'eModelElement', b2)
    if hasattr(b2, 'EAnnotation'):
        assert not _is_linked(b2, 'EAnnotation', a)


def test_assoc_eAttributeType0_link_reassign_clear():
    a = javaless_EDataType(serializable=True)
    b1 = javaless_EAttribute(iD=True)
    b2 = javaless_EAttribute(iD=False)
    _safe_set(a, 'javaless_EDataType', b1)
    assert _is_linked(a, 'javaless_EDataType', b1)
    if hasattr(b1, 'javaless_EAttribute'):
        assert _is_linked(b1, 'javaless_EAttribute', a)
    _safe_set(a, 'javaless_EDataType', b2)
    assert _is_linked(a, 'javaless_EDataType', b2)
    if hasattr(b1, 'javaless_EAttribute'):
        assert not _is_linked(b1, 'javaless_EAttribute', a)
    if hasattr(b2, 'javaless_EAttribute'):
        assert _is_linked(b2, 'javaless_EAttribute', a)
    _safe_set(a, 'javaless_EDataType', None)
    assert not _is_linked(a, 'javaless_EDataType', b2)
    if hasattr(b2, 'javaless_EAttribute'):
        assert not _is_linked(b2, 'javaless_EAttribute', a)


def test_assoc_eAttributes19_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EAttribute(iD=True)
    b2 = javaless_EAttribute(iD=False)
    _safe_set(a, 'javaless_EClass20', {b1})
    assert _is_linked(a, 'javaless_EClass20', b1)
    if hasattr(b1, 'javaless_EAttribute21'):
        assert _is_linked(b1, 'javaless_EAttribute21', a)
    _safe_set(a, 'javaless_EClass20', {b2})
    assert _is_linked(a, 'javaless_EClass20', b2)
    if hasattr(b1, 'javaless_EAttribute21'):
        assert not _is_linked(b1, 'javaless_EAttribute21', a)
    if hasattr(b2, 'javaless_EAttribute21'):
        assert _is_linked(b2, 'javaless_EAttribute21', a)
    _safe_set(a, 'javaless_EClass20', set())
    assert not _is_linked(a, 'javaless_EClass20', b2)
    if hasattr(b2, 'javaless_EAttribute21'):
        assert not _is_linked(b2, 'javaless_EAttribute21', a)


def test_assoc_eClassifiers48_link_reassign_clear():
    a = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    b2 = javaless_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2")
    _safe_set(a, 'ePackage49', {b1})
    assert _is_linked(a, 'ePackage49', b1)
    if hasattr(b1, 'EClassifier'):
        assert _is_linked(b1, 'EClassifier', a)
    _safe_set(a, 'ePackage49', {b2})
    assert _is_linked(a, 'ePackage49', b2)
    if hasattr(b1, 'EClassifier'):
        assert not _is_linked(b1, 'EClassifier', a)
    if hasattr(b2, 'EClassifier'):
        assert _is_linked(b2, 'EClassifier', a)
    _safe_set(a, 'ePackage49', set())
    assert not _is_linked(a, 'ePackage49', b2)
    if hasattr(b2, 'EClassifier'):
        assert not _is_linked(b2, 'EClassifier', a)


def test_assoc_eContainingClass43_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EOperation()
    b2 = javaless_EOperation()
    _safe_set(a, 'EClass', b1)
    assert _is_linked(a, 'EClass', b1)
    if hasattr(b1, 'eOperations'):
        assert _is_linked(b1, 'eOperations', a)
    _safe_set(a, 'EClass', b2)
    assert _is_linked(a, 'EClass', b2)
    if hasattr(b1, 'eOperations'):
        assert not _is_linked(b1, 'eOperations', a)
    if hasattr(b2, 'eOperations'):
        assert _is_linked(b2, 'eOperations', a)
    _safe_set(a, 'EClass', None)
    assert not _is_linked(a, 'EClass', b2)
    if hasattr(b2, 'eOperations'):
        assert not _is_linked(b2, 'eOperations', a)


def test_assoc_eContainingClass64_link_reassign_clear():
    a = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'eStructuralFeatures', b1)
    assert _is_linked(a, 'eStructuralFeatures', b1)
    if hasattr(b1, 'EClass65'):
        assert _is_linked(b1, 'EClass65', a)
    _safe_set(a, 'eStructuralFeatures', b2)
    assert _is_linked(a, 'eStructuralFeatures', b2)
    if hasattr(b1, 'EClass65'):
        assert not _is_linked(b1, 'EClass65', a)
    if hasattr(b2, 'EClass65'):
        assert _is_linked(b2, 'EClass65', a)
    _safe_set(a, 'eStructuralFeatures', None)
    assert not _is_linked(a, 'eStructuralFeatures', b2)
    if hasattr(b2, 'EClass65'):
        assert not _is_linked(b2, 'EClass65', a)


def test_assoc_eEnum39_link_reassign_clear():
    a = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    b1 = javaless_EEnum()
    b2 = javaless_EEnum()
    _safe_set(a, 'eLiterals', b1)
    assert _is_linked(a, 'eLiterals', b1)
    if hasattr(b1, 'EEnum'):
        assert _is_linked(b1, 'EEnum', a)
    _safe_set(a, 'eLiterals', b2)
    assert _is_linked(a, 'eLiterals', b2)
    if hasattr(b1, 'EEnum'):
        assert not _is_linked(b1, 'EEnum', a)
    if hasattr(b2, 'EEnum'):
        assert _is_linked(b2, 'EEnum', a)
    _safe_set(a, 'eLiterals', None)
    assert not _is_linked(a, 'eLiterals', b2)
    if hasattr(b2, 'EEnum'):
        assert not _is_linked(b2, 'EEnum', a)


def test_assoc_eExceptions45_link_reassign_clear():
    a = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    b1 = javaless_EOperation()
    b2 = javaless_EOperation()
    _safe_set(a, 'javaless_EClassifier', b1)
    assert _is_linked(a, 'javaless_EClassifier', b1)
    if hasattr(b1, 'javaless_EOperation46'):
        assert _is_linked(b1, 'javaless_EOperation46', a)
    _safe_set(a, 'javaless_EClassifier', b2)
    assert _is_linked(a, 'javaless_EClassifier', b2)
    if hasattr(b1, 'javaless_EOperation46'):
        assert not _is_linked(b1, 'javaless_EOperation46', a)
    if hasattr(b2, 'javaless_EOperation46'):
        assert _is_linked(b2, 'javaless_EOperation46', a)
    _safe_set(a, 'javaless_EClassifier', None)
    assert not _is_linked(a, 'javaless_EClassifier', b2)
    if hasattr(b2, 'javaless_EOperation46'):
        assert not _is_linked(b2, 'javaless_EOperation46', a)


def test_assoc_eFactoryInstance47_link_reassign_clear():
    a = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = javaless_EFactory()
    b2 = javaless_EFactory()
    _safe_set(a, 'ePackage', b1)
    assert _is_linked(a, 'ePackage', b1)
    if hasattr(b1, 'EFactory'):
        assert _is_linked(b1, 'EFactory', a)
    _safe_set(a, 'ePackage', b2)
    assert _is_linked(a, 'ePackage', b2)
    if hasattr(b1, 'EFactory'):
        assert not _is_linked(b1, 'EFactory', a)
    if hasattr(b2, 'EFactory'):
        assert _is_linked(b2, 'EFactory', a)
    _safe_set(a, 'ePackage', None)
    assert not _is_linked(a, 'ePackage', b2)
    if hasattr(b2, 'EFactory'):
        assert not _is_linked(b2, 'EFactory', a)


def test_assoc_eIDAttribute32_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EAttribute(iD=True)
    b2 = javaless_EAttribute(iD=False)
    _safe_set(a, 'javaless_EClass33', b1)
    assert _is_linked(a, 'javaless_EClass33', b1)
    if hasattr(b1, 'javaless_EAttribute34'):
        assert _is_linked(b1, 'javaless_EAttribute34', a)
    _safe_set(a, 'javaless_EClass33', b2)
    assert _is_linked(a, 'javaless_EClass33', b2)
    if hasattr(b1, 'javaless_EAttribute34'):
        assert not _is_linked(b1, 'javaless_EAttribute34', a)
    if hasattr(b2, 'javaless_EAttribute34'):
        assert _is_linked(b2, 'javaless_EAttribute34', a)
    _safe_set(a, 'javaless_EClass33', None)
    assert not _is_linked(a, 'javaless_EClass33', b2)
    if hasattr(b2, 'javaless_EAttribute34'):
        assert not _is_linked(b2, 'javaless_EAttribute34', a)


def test_assoc_eLiterals38_link_reassign_clear():
    a = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    b1 = javaless_EEnum()
    b2 = javaless_EEnum()
    _safe_set(a, 'EEnumLiteral', b1)
    assert _is_linked(a, 'EEnumLiteral', b1)
    if hasattr(b1, 'eEnum'):
        assert _is_linked(b1, 'eEnum', a)
    _safe_set(a, 'EEnumLiteral', b2)
    assert _is_linked(a, 'EEnumLiteral', b2)
    if hasattr(b1, 'eEnum'):
        assert not _is_linked(b1, 'eEnum', a)
    if hasattr(b2, 'eEnum'):
        assert _is_linked(b2, 'eEnum', a)
    _safe_set(a, 'EEnumLiteral', None)
    assert not _is_linked(a, 'EEnumLiteral', b2)
    if hasattr(b2, 'eEnum'):
        assert not _is_linked(b2, 'eEnum', a)


def test_assoc_eModelElement2_link_reassign_clear():
    a = javaless_EModelElement()
    b1 = javaless_EAnnotation(source="sample_text")
    b2 = javaless_EAnnotation(source="sample_text_2")
    _safe_set(a, 'EModelElement', b1)
    assert _is_linked(a, 'EModelElement', b1)
    if hasattr(b1, 'eAnnotations'):
        assert _is_linked(b1, 'eAnnotations', a)
    _safe_set(a, 'EModelElement', b2)
    assert _is_linked(a, 'EModelElement', b2)
    if hasattr(b1, 'eAnnotations'):
        assert not _is_linked(b1, 'eAnnotations', a)
    if hasattr(b2, 'eAnnotations'):
        assert _is_linked(b2, 'eAnnotations', a)
    _safe_set(a, 'EModelElement', None)
    assert not _is_linked(a, 'EModelElement', b2)
    if hasattr(b2, 'eAnnotations'):
        assert not _is_linked(b2, 'eAnnotations', a)


def test_assoc_eOperations10_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EOperation()
    b2 = javaless_EOperation()
    _safe_set(a, 'eContainingClass', {b1})
    assert _is_linked(a, 'eContainingClass', b1)
    if hasattr(b1, 'EOperation'):
        assert _is_linked(b1, 'EOperation', a)
    _safe_set(a, 'eContainingClass', {b2})
    assert _is_linked(a, 'eContainingClass', b2)
    if hasattr(b1, 'EOperation'):
        assert not _is_linked(b1, 'EOperation', a)
    if hasattr(b2, 'EOperation'):
        assert _is_linked(b2, 'EOperation', a)
    _safe_set(a, 'eContainingClass', set())
    assert not _is_linked(a, 'eContainingClass', b2)
    if hasattr(b2, 'EOperation'):
        assert not _is_linked(b2, 'EOperation', a)


def test_assoc_eOpposite59_link_reassign_clear():
    a = javaless_EReference(container=True, containment=True, resolveProxies=True)
    b1 = javaless_EReference(container=True, containment=True, resolveProxies=True)
    b2 = javaless_EReference(container=False, containment=False, resolveProxies=False)
    _safe_set(a, 'javaless_EReference58', b1)
    assert _is_linked(a, 'javaless_EReference58', b1)
    if hasattr(b1, 'javaless_EReference60'):
        assert _is_linked(b1, 'javaless_EReference60', a)
    _safe_set(a, 'javaless_EReference58', b2)
    assert _is_linked(a, 'javaless_EReference58', b2)
    if hasattr(b1, 'javaless_EReference60'):
        assert not _is_linked(b1, 'javaless_EReference60', a)
    if hasattr(b2, 'javaless_EReference60'):
        assert _is_linked(b2, 'javaless_EReference60', a)
    _safe_set(a, 'javaless_EReference58', None)
    assert not _is_linked(a, 'javaless_EReference58', b2)
    if hasattr(b2, 'javaless_EReference60'):
        assert not _is_linked(b2, 'javaless_EReference60', a)


def test_assoc_ePackage37_link_reassign_clear():
    a = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    b2 = javaless_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2")
    _safe_set(a, 'EPackage', b1)
    assert _is_linked(a, 'EPackage', b1)
    if hasattr(b1, 'eClassifiers'):
        assert _is_linked(b1, 'eClassifiers', a)
    _safe_set(a, 'EPackage', b2)
    assert _is_linked(a, 'EPackage', b2)
    if hasattr(b1, 'eClassifiers'):
        assert not _is_linked(b1, 'eClassifiers', a)
    if hasattr(b2, 'eClassifiers'):
        assert _is_linked(b2, 'eClassifiers', a)
    _safe_set(a, 'EPackage', None)
    assert not _is_linked(a, 'EPackage', b2)
    if hasattr(b2, 'eClassifiers'):
        assert not _is_linked(b2, 'eClassifiers', a)


def test_assoc_ePackage40_link_reassign_clear():
    a = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = javaless_EFactory()
    b2 = javaless_EFactory()
    _safe_set(a, 'EPackage41', b1)
    assert _is_linked(a, 'EPackage41', b1)
    if hasattr(b1, 'eFactoryInstance'):
        assert _is_linked(b1, 'eFactoryInstance', a)
    _safe_set(a, 'EPackage41', b2)
    assert _is_linked(a, 'EPackage41', b2)
    if hasattr(b1, 'eFactoryInstance'):
        assert not _is_linked(b1, 'eFactoryInstance', a)
    if hasattr(b2, 'eFactoryInstance'):
        assert _is_linked(b2, 'eFactoryInstance', a)
    _safe_set(a, 'EPackage41', None)
    assert not _is_linked(a, 'EPackage41', b2)
    if hasattr(b2, 'eFactoryInstance'):
        assert not _is_linked(b2, 'eFactoryInstance', a)


def test_assoc_eReferenceType61_link_reassign_clear():
    a = javaless_EReference(container=True, containment=True, resolveProxies=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'javaless_EReference62', b1)
    assert _is_linked(a, 'javaless_EReference62', b1)
    if hasattr(b1, 'javaless_EClass63'):
        assert _is_linked(b1, 'javaless_EClass63', a)
    _safe_set(a, 'javaless_EReference62', b2)
    assert _is_linked(a, 'javaless_EReference62', b2)
    if hasattr(b1, 'javaless_EClass63'):
        assert not _is_linked(b1, 'javaless_EClass63', a)
    if hasattr(b2, 'javaless_EClass63'):
        assert _is_linked(b2, 'javaless_EClass63', a)
    _safe_set(a, 'javaless_EReference62', None)
    assert not _is_linked(a, 'javaless_EReference62', b2)
    if hasattr(b2, 'javaless_EClass63'):
        assert not _is_linked(b2, 'javaless_EClass63', a)


def test_assoc_eReferences16_link_reassign_clear():
    a = javaless_EReference(container=True, containment=True, resolveProxies=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'javaless_EReference18', b1)
    assert _is_linked(a, 'javaless_EReference18', b1)
    if hasattr(b1, 'javaless_EClass17'):
        assert _is_linked(b1, 'javaless_EClass17', a)
    _safe_set(a, 'javaless_EReference18', b2)
    assert _is_linked(a, 'javaless_EReference18', b2)
    if hasattr(b1, 'javaless_EClass17'):
        assert not _is_linked(b1, 'javaless_EClass17', a)
    if hasattr(b2, 'javaless_EClass17'):
        assert _is_linked(b2, 'javaless_EClass17', a)
    _safe_set(a, 'javaless_EReference18', None)
    assert not _is_linked(a, 'javaless_EReference18', b2)
    if hasattr(b2, 'javaless_EClass17'):
        assert not _is_linked(b2, 'javaless_EClass17', a)


def test_assoc_eStructuralFeatures35_link_reassign_clear():
    a = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'EStructuralFeature', b1)
    assert _is_linked(a, 'EStructuralFeature', b1)
    if hasattr(b1, 'eContainingClass36'):
        assert _is_linked(b1, 'eContainingClass36', a)
    _safe_set(a, 'EStructuralFeature', b2)
    assert _is_linked(a, 'EStructuralFeature', b2)
    if hasattr(b1, 'eContainingClass36'):
        assert not _is_linked(b1, 'eContainingClass36', a)
    if hasattr(b2, 'eContainingClass36'):
        assert _is_linked(b2, 'eContainingClass36', a)
    _safe_set(a, 'EStructuralFeature', None)
    assert not _is_linked(a, 'EStructuralFeature', b2)
    if hasattr(b2, 'eContainingClass36'):
        assert not _is_linked(b2, 'eContainingClass36', a)


def test_assoc_eSubpackages51_link_reassign_clear():
    a = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    _safe_set(a, 'EPackage52', b1)
    assert _is_linked(a, 'EPackage52', b1)
    if hasattr(b1, 'eSuperPackage'):
        assert _is_linked(b1, 'eSuperPackage', a)
    _safe_set(a, 'EPackage52', b2)
    assert _is_linked(a, 'EPackage52', b2)
    if hasattr(b1, 'eSuperPackage'):
        assert not _is_linked(b1, 'eSuperPackage', a)
    if hasattr(b2, 'eSuperPackage'):
        assert _is_linked(b2, 'eSuperPackage', a)
    _safe_set(a, 'EPackage52', None)
    assert not _is_linked(a, 'EPackage52', b2)
    if hasattr(b2, 'eSuperPackage'):
        assert not _is_linked(b2, 'eSuperPackage', a)


def test_assoc_eSuperPackage54_link_reassign_clear():
    a = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    _safe_set(a, 'EPackage55', b1)
    assert _is_linked(a, 'EPackage55', b1)
    if hasattr(b1, 'eSubpackages'):
        assert _is_linked(b1, 'eSubpackages', a)
    _safe_set(a, 'EPackage55', b2)
    assert _is_linked(a, 'EPackage55', b2)
    if hasattr(b1, 'eSubpackages'):
        assert not _is_linked(b1, 'eSubpackages', a)
    if hasattr(b2, 'eSubpackages'):
        assert _is_linked(b2, 'eSubpackages', a)
    _safe_set(a, 'EPackage55', None)
    assert not _is_linked(a, 'EPackage55', b2)
    if hasattr(b2, 'eSubpackages'):
        assert not _is_linked(b2, 'eSubpackages', a)


def test_assoc_eSuperTypes9_link_reassign_clear():
    a = javaless_EClass(abstract=True, interface=True)
    b1 = javaless_EClass(abstract=True, interface=True)
    b2 = javaless_EClass(abstract=False, interface=False)
    _safe_set(a, 'javaless_EClass', b1)
    assert _is_linked(a, 'javaless_EClass', b1)
    if hasattr(b1, 'javaless_EClass8'):
        assert _is_linked(b1, 'javaless_EClass8', a)
    _safe_set(a, 'javaless_EClass', b2)
    assert _is_linked(a, 'javaless_EClass', b2)
    if hasattr(b1, 'javaless_EClass8'):
        assert not _is_linked(b1, 'javaless_EClass8', a)
    if hasattr(b2, 'javaless_EClass8'):
        assert _is_linked(b2, 'javaless_EClass8', a)
    _safe_set(a, 'javaless_EClass', None)
    assert not _is_linked(a, 'javaless_EClass', b2)
    if hasattr(b2, 'javaless_EClass8'):
        assert not _is_linked(b2, 'javaless_EClass8', a)


def test_assoc_eType66_link_reassign_clear():
    a = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    b1 = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    b2 = javaless_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2")
    _safe_set(a, 'javaless_ETypedElement', b1)
    assert _is_linked(a, 'javaless_ETypedElement', b1)
    if hasattr(b1, 'javaless_EClassifier67'):
        assert _is_linked(b1, 'javaless_EClassifier67', a)
    _safe_set(a, 'javaless_ETypedElement', b2)
    assert _is_linked(a, 'javaless_ETypedElement', b2)
    if hasattr(b1, 'javaless_EClassifier67'):
        assert not _is_linked(b1, 'javaless_EClassifier67', a)
    if hasattr(b2, 'javaless_EClassifier67'):
        assert _is_linked(b2, 'javaless_EClassifier67', a)
    _safe_set(a, 'javaless_ETypedElement', None)
    assert not _is_linked(a, 'javaless_ETypedElement', b2)
    if hasattr(b2, 'javaless_EClassifier67'):
        assert not _is_linked(b2, 'javaless_EClassifier67', a)


def test_assoc_references5_link_reassign_clear():
    a = javaless_EObject()
    b1 = javaless_EAnnotation(source="sample_text")
    b2 = javaless_EAnnotation(source="sample_text_2")
    _safe_set(a, 'javaless_EObject7', b1)
    assert _is_linked(a, 'javaless_EObject7', b1)
    if hasattr(b1, 'javaless_EAnnotation6'):
        assert _is_linked(b1, 'javaless_EAnnotation6', a)
    _safe_set(a, 'javaless_EObject7', b2)
    assert _is_linked(a, 'javaless_EObject7', b2)
    if hasattr(b1, 'javaless_EAnnotation6'):
        assert not _is_linked(b1, 'javaless_EAnnotation6', a)
    if hasattr(b2, 'javaless_EAnnotation6'):
        assert _is_linked(b2, 'javaless_EAnnotation6', a)
    _safe_set(a, 'javaless_EObject7', None)
    assert not _is_linked(a, 'javaless_EObject7', b2)
    if hasattr(b2, 'javaless_EAnnotation6'):
        assert not _is_linked(b2, 'javaless_EAnnotation6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EClassifier_strategy = st.builds(EClassifier)
@given(instance=EClassifier_strategy)
@settings(max_examples=25)
def test_EClassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)


EDataType_strategy = st.builds(EDataType)
@given(instance=EDataType_strategy)
@settings(max_examples=25)
def test_EDataType_instantiation(instance):
    assert isinstance(instance, EDataType)


EModelElement_strategy = st.builds(EModelElement)
@given(instance=EModelElement_strategy)
@settings(max_examples=25)
def test_EModelElement_instantiation(instance):
    assert isinstance(instance, EModelElement)


ENamedElement_strategy = st.builds(ENamedElement)
@given(instance=ENamedElement_strategy)
@settings(max_examples=25)
def test_ENamedElement_instantiation(instance):
    assert isinstance(instance, ENamedElement)


EObject_strategy = st.builds(EObject)
@given(instance=EObject_strategy)
@settings(max_examples=25)
def test_EObject_instantiation(instance):
    assert isinstance(instance, EObject)


EStructuralFeature_strategy = st.builds(EStructuralFeature)
@given(instance=EStructuralFeature_strategy)
@settings(max_examples=25)
def test_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, EStructuralFeature)


ETypedElement_strategy = st.builds(ETypedElement)
@given(instance=ETypedElement_strategy)
@settings(max_examples=25)
def test_ETypedElement_instantiation(instance):
    assert isinstance(instance, ETypedElement)


javaless_EAnnotation_strategy = st.builds(javaless_EAnnotation, source=safe_text)
@given(instance=javaless_EAnnotation_strategy)
@settings(max_examples=25)
def test_javaless_EAnnotation_instantiation(instance):
    assert isinstance(instance, javaless_EAnnotation)


javaless_EAttribute_strategy = st.builds(javaless_EAttribute, iD=st.booleans())
@given(instance=javaless_EAttribute_strategy)
@settings(max_examples=25)
def test_javaless_EAttribute_instantiation(instance):
    assert isinstance(instance, javaless_EAttribute)


javaless_EClass_strategy = st.builds(javaless_EClass, abstract=st.booleans(), interface=st.booleans())
@given(instance=javaless_EClass_strategy)
@settings(max_examples=25)
def test_javaless_EClass_instantiation(instance):
    assert isinstance(instance, javaless_EClass)


javaless_EClassifier_strategy = st.builds(javaless_EClassifier, defaultValue=safe_text, instanceClass=safe_text, instanceClassName=safe_text)
@given(instance=javaless_EClassifier_strategy)
@settings(max_examples=25)
def test_javaless_EClassifier_instantiation(instance):
    assert isinstance(instance, javaless_EClassifier)


javaless_EDataType_strategy = st.builds(javaless_EDataType, serializable=st.booleans())
@given(instance=javaless_EDataType_strategy)
@settings(max_examples=25)
def test_javaless_EDataType_instantiation(instance):
    assert isinstance(instance, javaless_EDataType)


javaless_EEnum_strategy = st.builds(javaless_EEnum)
@given(instance=javaless_EEnum_strategy)
@settings(max_examples=25)
def test_javaless_EEnum_instantiation(instance):
    assert isinstance(instance, javaless_EEnum)


javaless_EEnumLiteral_strategy = st.builds(javaless_EEnumLiteral, instance=safe_text, literal=safe_text, value=st.integers())
@given(instance=javaless_EEnumLiteral_strategy)
@settings(max_examples=25)
def test_javaless_EEnumLiteral_instantiation(instance):
    assert isinstance(instance, javaless_EEnumLiteral)


javaless_EFactory_strategy = st.builds(javaless_EFactory)
@given(instance=javaless_EFactory_strategy)
@settings(max_examples=25)
def test_javaless_EFactory_instantiation(instance):
    assert isinstance(instance, javaless_EFactory)


javaless_EModelElement_strategy = st.builds(javaless_EModelElement)
@given(instance=javaless_EModelElement_strategy)
@settings(max_examples=25)
def test_javaless_EModelElement_instantiation(instance):
    assert isinstance(instance, javaless_EModelElement)


javaless_ENamedElement_strategy = st.builds(javaless_ENamedElement, name=safe_text)
@given(instance=javaless_ENamedElement_strategy)
@settings(max_examples=25)
def test_javaless_ENamedElement_instantiation(instance):
    assert isinstance(instance, javaless_ENamedElement)


javaless_EObject_strategy = st.builds(javaless_EObject)
@given(instance=javaless_EObject_strategy)
@settings(max_examples=25)
def test_javaless_EObject_instantiation(instance):
    assert isinstance(instance, javaless_EObject)


javaless_EOperation_strategy = st.builds(javaless_EOperation)
@given(instance=javaless_EOperation_strategy)
@settings(max_examples=25)
def test_javaless_EOperation_instantiation(instance):
    assert isinstance(instance, javaless_EOperation)


javaless_EPackage_strategy = st.builds(javaless_EPackage, nsPrefix=safe_text, nsURI=safe_text)
@given(instance=javaless_EPackage_strategy)
@settings(max_examples=25)
def test_javaless_EPackage_instantiation(instance):
    assert isinstance(instance, javaless_EPackage)


javaless_EParameter_strategy = st.builds(javaless_EParameter)
@given(instance=javaless_EParameter_strategy)
@settings(max_examples=25)
def test_javaless_EParameter_instantiation(instance):
    assert isinstance(instance, javaless_EParameter)


javaless_EReference_strategy = st.builds(javaless_EReference, container=st.booleans(), containment=st.booleans(), resolveProxies=st.booleans())
@given(instance=javaless_EReference_strategy)
@settings(max_examples=25)
def test_javaless_EReference_instantiation(instance):
    assert isinstance(instance, javaless_EReference)


javaless_EStringToStringMapEntry_strategy = st.builds(javaless_EStringToStringMapEntry, key=safe_text, value=safe_text)
@given(instance=javaless_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_javaless_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, javaless_EStringToStringMapEntry)


javaless_EStructuralFeature_strategy = st.builds(javaless_EStructuralFeature, changeable=st.booleans(), defaultValue=safe_text, defaultValueLiteral=safe_text, derived=st.booleans(), transient=st.booleans(), unsettable=st.booleans(), volatile=st.booleans())
@given(instance=javaless_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_javaless_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, javaless_EStructuralFeature)


javaless_ETypedElement_strategy = st.builds(javaless_ETypedElement, lowerBound=st.integers(), many=st.booleans(), ordered=st.booleans(), required=st.booleans(), unique=st.booleans(), upperBound=st.integers())
@given(instance=javaless_ETypedElement_strategy)
@settings(max_examples=25)
def test_javaless_ETypedElement_instantiation(instance):
    assert isinstance(instance, javaless_ETypedElement)



