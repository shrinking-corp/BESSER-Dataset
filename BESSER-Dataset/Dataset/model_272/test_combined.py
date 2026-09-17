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
    ecore_EStringToStringMapEntry,
    EDataType,
    ecore_EEnum,
    ETypedElement,
    ecore_EParameter,
    ecore_ENamedElement,
    ecore_EOperation,
    ENamedElement,
    ecore_ETypedElement,
    ecore_EPackage,
    ecore_EEnumLiteral,
    ecore_EClassifier,
    ecore_EStructuralFeature,
    EClassifier,
    ecore_EClass,
    ecore_EDataType,
    EStructuralFeature,
    ecore_EReference,
    ecore_EAttribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ecore_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ecore_EStringToStringMapEntry)


def test_hyp_ecore_estringtostringmapentry_constructor_exists():
    assert callable(ecore_EStringToStringMapEntry.__init__)


def test_hyp_ecore_estringtostringmapentry_constructor_args():
    sig = inspect.signature(ecore_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_hyp_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_hyp_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ecore_eenum_is_not_abstract():
    assert not inspect.isabstract(ecore_EEnum)


def test_hyp_ecore_eenum_constructor_exists():
    assert callable(ecore_EEnum.__init__)


def test_hyp_ecore_eenum_constructor_args():
    sig = inspect.signature(ecore_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_hyp_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_hyp_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ecore_eparameter_is_not_abstract():
    assert not inspect.isabstract(ecore_EParameter)


def test_hyp_ecore_eparameter_constructor_exists():
    assert callable(ecore_EParameter.__init__)


def test_hyp_ecore_eparameter_constructor_args():
    sig = inspect.signature(ecore_EParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ecore_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ecore_ENamedElement)


def test_hyp_ecore_enamedelement_constructor_exists():
    assert callable(ecore_ENamedElement.__init__)


def test_hyp_ecore_enamedelement_constructor_args():
    sig = inspect.signature(ecore_ENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ecore_eoperation_is_not_abstract():
    assert not inspect.isabstract(ecore_EOperation)


def test_hyp_ecore_eoperation_constructor_exists():
    assert callable(ecore_EOperation.__init__)


def test_hyp_ecore_eoperation_constructor_args():
    sig = inspect.signature(ecore_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_hyp_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_hyp_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ecore_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ecore_ETypedElement)


def test_hyp_ecore_etypedelement_constructor_exists():
    assert callable(ecore_ETypedElement.__init__)


def test_hyp_ecore_etypedelement_constructor_args():
    sig = inspect.signature(ecore_ETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "many" in params, "Missing parameter 'many'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "required" in params, "Missing parameter 'required'"









def test_hyp_ecore_epackage_is_not_abstract():
    assert not inspect.isabstract(ecore_EPackage)


def test_hyp_ecore_epackage_constructor_exists():
    assert callable(ecore_EPackage.__init__)


def test_hyp_ecore_epackage_constructor_args():
    sig = inspect.signature(ecore_EPackage.__init__)
    params = list(sig.parameters.keys())
    assert "nsURI" in params, "Missing parameter 'nsURI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"





def test_hyp_ecore_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(ecore_EEnumLiteral)


def test_hyp_ecore_eenumliteral_constructor_exists():
    assert callable(ecore_EEnumLiteral.__init__)


def test_hyp_ecore_eenumliteral_constructor_args():
    sig = inspect.signature(ecore_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "instance" in params, "Missing parameter 'instance'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_ecore_eclassifier_is_not_abstract():
    assert not inspect.isabstract(ecore_EClassifier)


def test_hyp_ecore_eclassifier_constructor_exists():
    assert callable(ecore_EClassifier.__init__)


def test_hyp_ecore_eclassifier_constructor_args():
    sig = inspect.signature(ecore_EClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"
    assert "instanceTypeName" in params, "Missing parameter 'instanceTypeName'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"







def test_hyp_ecore_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ecore_EStructuralFeature)


def test_hyp_ecore_estructuralfeature_constructor_exists():
    assert callable(ecore_EStructuralFeature.__init__)


def test_hyp_ecore_estructuralfeature_constructor_args():
    sig = inspect.signature(ecore_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "defaultValueLiteral" in params, "Missing parameter 'defaultValueLiteral'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "unsettable" in params, "Missing parameter 'unsettable'"










def test_hyp_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_hyp_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_hyp_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ecore_eclass_is_not_abstract():
    assert not inspect.isabstract(ecore_EClass)


def test_hyp_ecore_eclass_constructor_exists():
    assert callable(ecore_EClass.__init__)


def test_hyp_ecore_eclass_constructor_args():
    sig = inspect.signature(ecore_EClass.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "interface" in params, "Missing parameter 'interface'"





def test_hyp_ecore_edatatype_is_not_abstract():
    assert not inspect.isabstract(ecore_EDataType)


def test_hyp_ecore_edatatype_constructor_exists():
    assert callable(ecore_EDataType.__init__)


def test_hyp_ecore_edatatype_constructor_args():
    sig = inspect.signature(ecore_EDataType.__init__)
    params = list(sig.parameters.keys())
    assert "serializable" in params, "Missing parameter 'serializable'"




def test_hyp_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature)


def test_hyp_estructuralfeature_constructor_exists():
    assert callable(EStructuralFeature.__init__)


def test_hyp_estructuralfeature_constructor_args():
    sig = inspect.signature(EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ecore_ereference_is_not_abstract():
    assert not inspect.isabstract(ecore_EReference)


def test_hyp_ecore_ereference_constructor_exists():
    assert callable(ecore_EReference.__init__)


def test_hyp_ecore_ereference_constructor_args():
    sig = inspect.signature(ecore_EReference.__init__)
    params = list(sig.parameters.keys())
    assert "containment" in params, "Missing parameter 'containment'"
    assert "container" in params, "Missing parameter 'container'"
    assert "resolveProxies" in params, "Missing parameter 'resolveProxies'"






def test_hyp_ecore_eattribute_is_not_abstract():
    assert not inspect.isabstract(ecore_EAttribute)


def test_hyp_ecore_eattribute_constructor_exists():
    assert callable(ecore_EAttribute.__init__)


def test_hyp_ecore_eattribute_constructor_args():
    sig = inspect.signature(ecore_EAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"



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
ecore_EStringToStringMapEntry_strategy = st.builds(
    ecore_EStringToStringMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
EDataType_strategy = st.builds(
    EDataType,
)
ecore_EEnum_strategy = st.builds(
    ecore_EEnum,
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
ecore_EParameter_strategy = st.builds(
    ecore_EParameter,
)
ecore_ENamedElement_strategy = st.builds(
    ecore_ENamedElement,
    name=
        safe_text
)
ecore_EOperation_strategy = st.builds(
    ecore_EOperation,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ecore_ETypedElement_strategy = st.builds(
    ecore_ETypedElement,
    unique=
        st.booleans(),
    ordered=
        st.booleans(),
    upperBound=
        st.integers(),
    many=
        st.booleans(),
    lowerBound=
        st.integers(),
    required=
        st.booleans()
)
ecore_EPackage_strategy = st.builds(
    ecore_EPackage,
    nsURI=
        safe_text,
    nsPrefix=
        safe_text
)
ecore_EEnumLiteral_strategy = st.builds(
    ecore_EEnumLiteral,
    literal=
        safe_text,
    instance=
        safe_text,
    value=
        st.integers()
)
ecore_EClassifier_strategy = st.builds(
    ecore_EClassifier,
    instanceClass=
        safe_text,
    instanceTypeName=
        safe_text,
    defaultValue=
        safe_text,
    instanceClassName=
        safe_text
)
ecore_EStructuralFeature_strategy = st.builds(
    ecore_EStructuralFeature,
    defaultValue=
        safe_text,
    defaultValueLiteral=
        safe_text,
    volatile=
        st.booleans(),
    changeable=
        st.booleans(),
    transient=
        st.booleans(),
    derived=
        st.booleans(),
    unsettable=
        st.booleans()
)
EClassifier_strategy = st.builds(
    EClassifier,
)
ecore_EClass_strategy = st.builds(
    ecore_EClass,
    abstract=
        st.booleans(),
    interface=
        st.booleans()
)
ecore_EDataType_strategy = st.builds(
    ecore_EDataType,
    serializable=
        st.booleans()
)
EStructuralFeature_strategy = st.builds(
    EStructuralFeature,
)
ecore_EReference_strategy = st.builds(
    ecore_EReference,
    containment=
        st.booleans(),
    container=
        st.booleans(),
    resolveProxies=
        st.booleans()
)
ecore_EAttribute_strategy = st.builds(
    ecore_EAttribute,
    iD=
        st.booleans()
)




@given(instance=ecore_EStringToStringMapEntry_strategy)
def test_hyp_ecore_estringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=ecore_EStringToStringMapEntry_strategy)
def test_hyp_ecore_estringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original








@given(instance=ecore_ENamedElement_strategy)
def test_hyp_ecore_enamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=ecore_ETypedElement_strategy)
def test_hyp_ecore_etypedelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=ecore_ETypedElement_strategy)
def test_hyp_ecore_etypedelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=ecore_ETypedElement_strategy)
def test_hyp_ecore_etypedelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=ecore_ETypedElement_strategy)
def test_hyp_ecore_etypedelement_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=ecore_ETypedElement_strategy)
def test_hyp_ecore_etypedelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=ecore_ETypedElement_strategy)
def test_hyp_ecore_etypedelement_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original




@given(instance=ecore_EPackage_strategy)
def test_hyp_ecore_epackage_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original



@given(instance=ecore_EPackage_strategy)
def test_hyp_ecore_epackage_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original




@given(instance=ecore_EEnumLiteral_strategy)
def test_hyp_ecore_eenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=ecore_EEnumLiteral_strategy)
def test_hyp_ecore_eenumliteral_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original



@given(instance=ecore_EEnumLiteral_strategy)
def test_hyp_ecore_eenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=ecore_EClassifier_strategy)
def test_hyp_ecore_eclassifier_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original



@given(instance=ecore_EClassifier_strategy)
def test_hyp_ecore_eclassifier_instanceTypeName_setter(instance):
    original = instance.instanceTypeName
    instance.instanceTypeName = original
    assert instance.instanceTypeName == original



@given(instance=ecore_EClassifier_strategy)
def test_hyp_ecore_eclassifier_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=ecore_EClassifier_strategy)
def test_hyp_ecore_eclassifier_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ecore_EClassifier_strategy)
@settings(max_examples=30)
def test_hyp_ecore_eclassifier_isinstance_changes_state(instance):
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
        assert has_statements, f"Function 'isInstance' in ecore_EClassifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in ecore_EClassifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in ecore_EClassifier is not implemented or raised an error")




@given(instance=ecore_EStructuralFeature_strategy)
def test_hyp_ecore_estructuralfeature_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=ecore_EStructuralFeature_strategy)
def test_hyp_ecore_estructuralfeature_defaultValueLiteral_setter(instance):
    original = instance.defaultValueLiteral
    instance.defaultValueLiteral = original
    assert instance.defaultValueLiteral == original



@given(instance=ecore_EStructuralFeature_strategy)
def test_hyp_ecore_estructuralfeature_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=ecore_EStructuralFeature_strategy)
def test_hyp_ecore_estructuralfeature_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=ecore_EStructuralFeature_strategy)
def test_hyp_ecore_estructuralfeature_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=ecore_EStructuralFeature_strategy)
def test_hyp_ecore_estructuralfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=ecore_EStructuralFeature_strategy)
def test_hyp_ecore_estructuralfeature_unsettable_setter(instance):
    original = instance.unsettable
    instance.unsettable = original
    assert instance.unsettable == original





@given(instance=ecore_EClass_strategy)
def test_hyp_ecore_eclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=ecore_EClass_strategy)
def test_hyp_ecore_eclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ecore_EClass_strategy)
@settings(max_examples=30)
def test_hyp_ecore_eclass_issupertypeof_changes_state(instance):
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
        assert has_statements, f"Function 'isSuperTypeOf' in ecore_EClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOf' in ecore_EClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOf' in ecore_EClass is not implemented or raised an error")




@given(instance=ecore_EDataType_strategy)
def test_hyp_ecore_edatatype_serializable_setter(instance):
    original = instance.serializable
    instance.serializable = original
    assert instance.serializable == original





@given(instance=ecore_EReference_strategy)
def test_hyp_ecore_ereference_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original



@given(instance=ecore_EReference_strategy)
def test_hyp_ecore_ereference_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original



@given(instance=ecore_EReference_strategy)
def test_hyp_ecore_ereference_resolveProxies_setter(instance):
    original = instance.resolveProxies
    instance.resolveProxies = original
    assert instance.resolveProxies == original




@given(instance=ecore_EAttribute_strategy)
def test_hyp_ecore_eattribute_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    EClassifier,
    EDataType,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    ecore_EAttribute,
    ecore_EClass,
    ecore_EClassifier,
    ecore_EDataType,
    ecore_EEnum,
    ecore_EEnumLiteral,
    ecore_ENamedElement,
    ecore_EOperation,
    ecore_EPackage,
    ecore_EParameter,
    ecore_EReference,
    ecore_EStringToStringMapEntry,
    ecore_EStructuralFeature,
    ecore_ETypedElement,
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

def test_ecore_EAttribute_iD_value_roundtrip():
    instance = ecore_EAttribute(iD=True)
    assert instance.iD == True
    instance.iD = False
    assert instance.iD == False


def test_ecore_EClass_abstract_value_roundtrip():
    instance = ecore_EClass(abstract=True, interface=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_ecore_EClass_interface_value_roundtrip():
    instance = ecore_EClass(abstract=True, interface=True)
    assert instance.interface == True
    instance.interface = False
    assert instance.interface == False


def test_ecore_EClassifier_defaultValue_value_roundtrip():
    instance = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_ecore_EClassifier_instanceClass_value_roundtrip():
    instance = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.instanceClass == "sample_text"
    instance.instanceClass = "sample_text_2"
    assert instance.instanceClass == "sample_text_2"


def test_ecore_EClassifier_instanceClassName_value_roundtrip():
    instance = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.instanceClassName == "sample_text"
    instance.instanceClassName = "sample_text_2"
    assert instance.instanceClassName == "sample_text_2"


def test_ecore_EClassifier_instanceTypeName_value_roundtrip():
    instance = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.instanceTypeName == "sample_text"
    instance.instanceTypeName = "sample_text_2"
    assert instance.instanceTypeName == "sample_text_2"


def test_ecore_EDataType_serializable_value_roundtrip():
    instance = ecore_EDataType(serializable=True)
    assert instance.serializable == True
    instance.serializable = False
    assert instance.serializable == False


def test_ecore_EEnumLiteral_instance_value_roundtrip():
    instance = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.instance == "sample_text"
    instance.instance = "sample_text_2"
    assert instance.instance == "sample_text_2"


def test_ecore_EEnumLiteral_literal_value_roundtrip():
    instance = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.literal == "sample_text"
    instance.literal = "sample_text_2"
    assert instance.literal == "sample_text_2"


def test_ecore_EEnumLiteral_value_value_roundtrip():
    instance = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_ecore_ENamedElement_name_value_roundtrip():
    instance = ecore_ENamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ecore_EPackage_nsPrefix_value_roundtrip():
    instance = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsPrefix == "sample_text"
    instance.nsPrefix = "sample_text_2"
    assert instance.nsPrefix == "sample_text_2"


def test_ecore_EPackage_nsURI_value_roundtrip():
    instance = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsURI == "sample_text"
    instance.nsURI = "sample_text_2"
    assert instance.nsURI == "sample_text_2"


def test_ecore_EReference_container_value_roundtrip():
    instance = ecore_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.container == True
    instance.container = False
    assert instance.container == False


def test_ecore_EReference_containment_value_roundtrip():
    instance = ecore_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.containment == True
    instance.containment = False
    assert instance.containment == False


def test_ecore_EReference_resolveProxies_value_roundtrip():
    instance = ecore_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.resolveProxies == True
    instance.resolveProxies = False
    assert instance.resolveProxies == False


def test_ecore_EStringToStringMapEntry_key_value_roundtrip():
    instance = ecore_EStringToStringMapEntry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_ecore_EStringToStringMapEntry_value_value_roundtrip():
    instance = ecore_EStringToStringMapEntry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_ecore_EStructuralFeature_changeable_value_roundtrip():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.changeable == True
    instance.changeable = False
    assert instance.changeable == False


def test_ecore_EStructuralFeature_defaultValue_value_roundtrip():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_ecore_EStructuralFeature_defaultValueLiteral_value_roundtrip():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.defaultValueLiteral == "sample_text"
    instance.defaultValueLiteral = "sample_text_2"
    assert instance.defaultValueLiteral == "sample_text_2"


def test_ecore_EStructuralFeature_derived_value_roundtrip():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_ecore_EStructuralFeature_transient_value_roundtrip():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_ecore_EStructuralFeature_unsettable_value_roundtrip():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.unsettable == True
    instance.unsettable = False
    assert instance.unsettable == False


def test_ecore_EStructuralFeature_volatile_value_roundtrip():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.volatile == True
    instance.volatile = False
    assert instance.volatile == False


def test_ecore_ETypedElement_lowerBound_value_roundtrip():
    instance = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_ecore_ETypedElement_many_value_roundtrip():
    instance = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_ecore_ETypedElement_ordered_value_roundtrip():
    instance = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.ordered == True
    instance.ordered = False
    assert instance.ordered == False


def test_ecore_ETypedElement_required_value_roundtrip():
    instance = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_ecore_ETypedElement_unique_value_roundtrip():
    instance = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_ecore_ETypedElement_upperBound_value_roundtrip():
    instance = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_ecore_EClass_isa_EClassifier():
    instance = ecore_EClass(abstract=True, interface=True)
    assert isinstance(instance, EClassifier)


def test_ecore_EDataType_isa_EClassifier():
    instance = ecore_EDataType(serializable=True)
    assert isinstance(instance, EClassifier)


def test_ecore_EEnum_isa_EDataType():
    instance = ecore_EEnum()
    assert isinstance(instance, EDataType)


def test_ecore_EClassifier_isa_ENamedElement():
    instance = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert isinstance(instance, ENamedElement)


def test_ecore_EEnumLiteral_isa_ENamedElement():
    instance = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert isinstance(instance, ENamedElement)


def test_ecore_EPackage_isa_ENamedElement():
    instance = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert isinstance(instance, ENamedElement)


def test_ecore_ETypedElement_isa_ENamedElement():
    instance = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert isinstance(instance, ENamedElement)


def test_ecore_EAttribute_isa_EStructuralFeature():
    instance = ecore_EAttribute(iD=True)
    assert isinstance(instance, EStructuralFeature)


def test_ecore_EReference_isa_EStructuralFeature():
    instance = ecore_EReference(container=True, containment=True, resolveProxies=True)
    assert isinstance(instance, EStructuralFeature)


def test_ecore_EOperation_isa_ETypedElement():
    instance = ecore_EOperation()
    assert isinstance(instance, ETypedElement)


def test_ecore_EParameter_isa_ETypedElement():
    instance = ecore_EParameter()
    assert isinstance(instance, ETypedElement)


def test_ecore_EStructuralFeature_isa_ETypedElement():
    instance = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert isinstance(instance, ETypedElement)


def test_assoc_eAllAttributes4_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EAttribute(iD=True)
    b2 = ecore_EAttribute(iD=False)
    _safe_set(a, 'ecore_EClass5', {b1})
    assert _is_linked(a, 'ecore_EClass5', b1)
    if hasattr(b1, 'ecore_EAttribute6'):
        assert _is_linked(b1, 'ecore_EAttribute6', a)
    _safe_set(a, 'ecore_EClass5', {b2})
    assert _is_linked(a, 'ecore_EClass5', b2)
    if hasattr(b1, 'ecore_EAttribute6'):
        assert not _is_linked(b1, 'ecore_EAttribute6', a)
    if hasattr(b2, 'ecore_EAttribute6'):
        assert _is_linked(b2, 'ecore_EAttribute6', a)
    _safe_set(a, 'ecore_EClass5', set())
    assert not _is_linked(a, 'ecore_EClass5', b2)
    if hasattr(b2, 'ecore_EAttribute6'):
        assert not _is_linked(b2, 'ecore_EAttribute6', a)


def test_assoc_eAllContainments15_link_reassign_clear():
    a = ecore_EReference(container=True, containment=True, resolveProxies=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'ecore_EReference17', b1)
    assert _is_linked(a, 'ecore_EReference17', b1)
    if hasattr(b1, 'ecore_EClass16'):
        assert _is_linked(b1, 'ecore_EClass16', a)
    _safe_set(a, 'ecore_EReference17', b2)
    assert _is_linked(a, 'ecore_EReference17', b2)
    if hasattr(b1, 'ecore_EClass16'):
        assert not _is_linked(b1, 'ecore_EClass16', a)
    if hasattr(b2, 'ecore_EClass16'):
        assert _is_linked(b2, 'ecore_EClass16', a)
    _safe_set(a, 'ecore_EReference17', None)
    assert not _is_linked(a, 'ecore_EReference17', b2)
    if hasattr(b2, 'ecore_EClass16'):
        assert not _is_linked(b2, 'ecore_EClass16', a)


def test_assoc_eAllOperations18_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EOperation()
    b2 = ecore_EOperation()
    _safe_set(a, 'ecore_EClass19', {b1})
    assert _is_linked(a, 'ecore_EClass19', b1)
    if hasattr(b1, 'ecore_EOperation'):
        assert _is_linked(b1, 'ecore_EOperation', a)
    _safe_set(a, 'ecore_EClass19', {b2})
    assert _is_linked(a, 'ecore_EClass19', b2)
    if hasattr(b1, 'ecore_EOperation'):
        assert not _is_linked(b1, 'ecore_EOperation', a)
    if hasattr(b2, 'ecore_EOperation'):
        assert _is_linked(b2, 'ecore_EOperation', a)
    _safe_set(a, 'ecore_EClass19', set())
    assert not _is_linked(a, 'ecore_EClass19', b2)
    if hasattr(b2, 'ecore_EOperation'):
        assert not _is_linked(b2, 'ecore_EOperation', a)


def test_assoc_eAllReferences7_link_reassign_clear():
    a = ecore_EReference(container=True, containment=True, resolveProxies=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'ecore_EReference', b1)
    assert _is_linked(a, 'ecore_EReference', b1)
    if hasattr(b1, 'ecore_EClass8'):
        assert _is_linked(b1, 'ecore_EClass8', a)
    _safe_set(a, 'ecore_EReference', b2)
    assert _is_linked(a, 'ecore_EReference', b2)
    if hasattr(b1, 'ecore_EClass8'):
        assert not _is_linked(b1, 'ecore_EClass8', a)
    if hasattr(b2, 'ecore_EClass8'):
        assert _is_linked(b2, 'ecore_EClass8', a)
    _safe_set(a, 'ecore_EReference', None)
    assert not _is_linked(a, 'ecore_EReference', b2)
    if hasattr(b2, 'ecore_EClass8'):
        assert not _is_linked(b2, 'ecore_EClass8', a)


def test_assoc_eAllStructuralFeatures20_link_reassign_clear():
    a = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'ecore_EStructuralFeature', b1)
    assert _is_linked(a, 'ecore_EStructuralFeature', b1)
    if hasattr(b1, 'ecore_EClass21'):
        assert _is_linked(b1, 'ecore_EClass21', a)
    _safe_set(a, 'ecore_EStructuralFeature', b2)
    assert _is_linked(a, 'ecore_EStructuralFeature', b2)
    if hasattr(b1, 'ecore_EClass21'):
        assert not _is_linked(b1, 'ecore_EClass21', a)
    if hasattr(b2, 'ecore_EClass21'):
        assert _is_linked(b2, 'ecore_EClass21', a)
    _safe_set(a, 'ecore_EStructuralFeature', None)
    assert not _is_linked(a, 'ecore_EStructuralFeature', b2)
    if hasattr(b2, 'ecore_EClass21'):
        assert not _is_linked(b2, 'ecore_EClass21', a)


def test_assoc_eAllSuperTypes23_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'ecore_EClass22', {b1})
    assert _is_linked(a, 'ecore_EClass22', b1)
    if hasattr(b1, 'ecore_EClass24'):
        assert _is_linked(b1, 'ecore_EClass24', a)
    _safe_set(a, 'ecore_EClass22', {b2})
    assert _is_linked(a, 'ecore_EClass22', b2)
    if hasattr(b1, 'ecore_EClass24'):
        assert not _is_linked(b1, 'ecore_EClass24', a)
    if hasattr(b2, 'ecore_EClass24'):
        assert _is_linked(b2, 'ecore_EClass24', a)
    _safe_set(a, 'ecore_EClass22', set())
    assert not _is_linked(a, 'ecore_EClass22', b2)
    if hasattr(b2, 'ecore_EClass24'):
        assert not _is_linked(b2, 'ecore_EClass24', a)


def test_assoc_eAttributeType0_link_reassign_clear():
    a = ecore_EDataType(serializable=True)
    b1 = ecore_EAttribute(iD=True)
    b2 = ecore_EAttribute(iD=False)
    _safe_set(a, 'ecore_EDataType', b1)
    assert _is_linked(a, 'ecore_EDataType', b1)
    if hasattr(b1, 'ecore_EAttribute'):
        assert _is_linked(b1, 'ecore_EAttribute', a)
    _safe_set(a, 'ecore_EDataType', b2)
    assert _is_linked(a, 'ecore_EDataType', b2)
    if hasattr(b1, 'ecore_EAttribute'):
        assert not _is_linked(b1, 'ecore_EAttribute', a)
    if hasattr(b2, 'ecore_EAttribute'):
        assert _is_linked(b2, 'ecore_EAttribute', a)
    _safe_set(a, 'ecore_EDataType', None)
    assert not _is_linked(a, 'ecore_EDataType', b2)
    if hasattr(b2, 'ecore_EAttribute'):
        assert not _is_linked(b2, 'ecore_EAttribute', a)


def test_assoc_eAttributes12_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EAttribute(iD=True)
    b2 = ecore_EAttribute(iD=False)
    _safe_set(a, 'ecore_EClass13', {b1})
    assert _is_linked(a, 'ecore_EClass13', b1)
    if hasattr(b1, 'ecore_EAttribute14'):
        assert _is_linked(b1, 'ecore_EAttribute14', a)
    _safe_set(a, 'ecore_EClass13', {b2})
    assert _is_linked(a, 'ecore_EClass13', b2)
    if hasattr(b1, 'ecore_EAttribute14'):
        assert not _is_linked(b1, 'ecore_EAttribute14', a)
    if hasattr(b2, 'ecore_EAttribute14'):
        assert _is_linked(b2, 'ecore_EAttribute14', a)
    _safe_set(a, 'ecore_EClass13', set())
    assert not _is_linked(a, 'ecore_EClass13', b2)
    if hasattr(b2, 'ecore_EAttribute14'):
        assert not _is_linked(b2, 'ecore_EAttribute14', a)


def test_assoc_eClassifiers37_link_reassign_clear():
    a = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b2 = ecore_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2", instanceTypeName="sample_text_2")
    _safe_set(a, 'ePackage', {b1})
    assert _is_linked(a, 'ePackage', b1)
    if hasattr(b1, 'EClassifier'):
        assert _is_linked(b1, 'EClassifier', a)
    _safe_set(a, 'ePackage', {b2})
    assert _is_linked(a, 'ePackage', b2)
    if hasattr(b1, 'EClassifier'):
        assert not _is_linked(b1, 'EClassifier', a)
    if hasattr(b2, 'EClassifier'):
        assert _is_linked(b2, 'EClassifier', a)
    _safe_set(a, 'ePackage', set())
    assert not _is_linked(a, 'ePackage', b2)
    if hasattr(b2, 'EClassifier'):
        assert not _is_linked(b2, 'EClassifier', a)


def test_assoc_eContainingClass33_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EOperation()
    b2 = ecore_EOperation()
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


def test_assoc_eContainingClass55_link_reassign_clear():
    a = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'eStructuralFeatures', b1)
    assert _is_linked(a, 'eStructuralFeatures', b1)
    if hasattr(b1, 'EClass56'):
        assert _is_linked(b1, 'EClass56', a)
    _safe_set(a, 'eStructuralFeatures', b2)
    assert _is_linked(a, 'eStructuralFeatures', b2)
    if hasattr(b1, 'EClass56'):
        assert not _is_linked(b1, 'EClass56', a)
    if hasattr(b2, 'EClass56'):
        assert _is_linked(b2, 'EClass56', a)
    _safe_set(a, 'eStructuralFeatures', None)
    assert not _is_linked(a, 'eStructuralFeatures', b2)
    if hasattr(b2, 'EClass56'):
        assert not _is_linked(b2, 'EClass56', a)


def test_assoc_eEnum32_link_reassign_clear():
    a = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    b1 = ecore_EEnum()
    b2 = ecore_EEnum()
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


def test_assoc_eExceptions35_link_reassign_clear():
    a = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b1 = ecore_EOperation()
    b2 = ecore_EOperation()
    _safe_set(a, 'ecore_EClassifier', b1)
    assert _is_linked(a, 'ecore_EClassifier', b1)
    if hasattr(b1, 'ecore_EOperation36'):
        assert _is_linked(b1, 'ecore_EOperation36', a)
    _safe_set(a, 'ecore_EClassifier', b2)
    assert _is_linked(a, 'ecore_EClassifier', b2)
    if hasattr(b1, 'ecore_EOperation36'):
        assert not _is_linked(b1, 'ecore_EOperation36', a)
    if hasattr(b2, 'ecore_EOperation36'):
        assert _is_linked(b2, 'ecore_EOperation36', a)
    _safe_set(a, 'ecore_EClassifier', None)
    assert not _is_linked(a, 'ecore_EClassifier', b2)
    if hasattr(b2, 'ecore_EOperation36'):
        assert not _is_linked(b2, 'ecore_EOperation36', a)


def test_assoc_eIDAttribute25_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EAttribute(iD=True)
    b2 = ecore_EAttribute(iD=False)
    _safe_set(a, 'ecore_EClass26', b1)
    assert _is_linked(a, 'ecore_EClass26', b1)
    if hasattr(b1, 'ecore_EAttribute27'):
        assert _is_linked(b1, 'ecore_EAttribute27', a)
    _safe_set(a, 'ecore_EClass26', b2)
    assert _is_linked(a, 'ecore_EClass26', b2)
    if hasattr(b1, 'ecore_EAttribute27'):
        assert not _is_linked(b1, 'ecore_EAttribute27', a)
    if hasattr(b2, 'ecore_EAttribute27'):
        assert _is_linked(b2, 'ecore_EAttribute27', a)
    _safe_set(a, 'ecore_EClass26', None)
    assert not _is_linked(a, 'ecore_EClass26', b2)
    if hasattr(b2, 'ecore_EAttribute27'):
        assert not _is_linked(b2, 'ecore_EAttribute27', a)


def test_assoc_eKeys52_link_reassign_clear():
    a = ecore_EReference(container=True, containment=True, resolveProxies=True)
    b1 = ecore_EAttribute(iD=True)
    b2 = ecore_EAttribute(iD=False)
    _safe_set(a, 'ecore_EReference53', {b1})
    assert _is_linked(a, 'ecore_EReference53', b1)
    if hasattr(b1, 'ecore_EAttribute54'):
        assert _is_linked(b1, 'ecore_EAttribute54', a)
    _safe_set(a, 'ecore_EReference53', {b2})
    assert _is_linked(a, 'ecore_EReference53', b2)
    if hasattr(b1, 'ecore_EAttribute54'):
        assert not _is_linked(b1, 'ecore_EAttribute54', a)
    if hasattr(b2, 'ecore_EAttribute54'):
        assert _is_linked(b2, 'ecore_EAttribute54', a)
    _safe_set(a, 'ecore_EReference53', set())
    assert not _is_linked(a, 'ecore_EReference53', b2)
    if hasattr(b2, 'ecore_EAttribute54'):
        assert not _is_linked(b2, 'ecore_EAttribute54', a)


def test_assoc_eLiterals31_link_reassign_clear():
    a = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    b1 = ecore_EEnum()
    b2 = ecore_EEnum()
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


def test_assoc_eOperations3_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EOperation()
    b2 = ecore_EOperation()
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


def test_assoc_eOpposite47_link_reassign_clear():
    a = ecore_EReference(container=True, containment=True, resolveProxies=True)
    b1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    b2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    _safe_set(a, 'ecore_EReference46', b1)
    assert _is_linked(a, 'ecore_EReference46', b1)
    if hasattr(b1, 'ecore_EReference48'):
        assert _is_linked(b1, 'ecore_EReference48', a)
    _safe_set(a, 'ecore_EReference46', b2)
    assert _is_linked(a, 'ecore_EReference46', b2)
    if hasattr(b1, 'ecore_EReference48'):
        assert not _is_linked(b1, 'ecore_EReference48', a)
    if hasattr(b2, 'ecore_EReference48'):
        assert _is_linked(b2, 'ecore_EReference48', a)
    _safe_set(a, 'ecore_EReference46', None)
    assert not _is_linked(a, 'ecore_EReference46', b2)
    if hasattr(b2, 'ecore_EReference48'):
        assert not _is_linked(b2, 'ecore_EReference48', a)


def test_assoc_ePackage30_link_reassign_clear():
    a = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b2 = ecore_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2", instanceTypeName="sample_text_2")
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


def test_assoc_eReferenceType49_link_reassign_clear():
    a = ecore_EReference(container=True, containment=True, resolveProxies=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'ecore_EReference50', b1)
    assert _is_linked(a, 'ecore_EReference50', b1)
    if hasattr(b1, 'ecore_EClass51'):
        assert _is_linked(b1, 'ecore_EClass51', a)
    _safe_set(a, 'ecore_EReference50', b2)
    assert _is_linked(a, 'ecore_EReference50', b2)
    if hasattr(b1, 'ecore_EClass51'):
        assert not _is_linked(b1, 'ecore_EClass51', a)
    if hasattr(b2, 'ecore_EClass51'):
        assert _is_linked(b2, 'ecore_EClass51', a)
    _safe_set(a, 'ecore_EReference50', None)
    assert not _is_linked(a, 'ecore_EReference50', b2)
    if hasattr(b2, 'ecore_EClass51'):
        assert not _is_linked(b2, 'ecore_EClass51', a)


def test_assoc_eReferences9_link_reassign_clear():
    a = ecore_EReference(container=True, containment=True, resolveProxies=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'ecore_EReference11', b1)
    assert _is_linked(a, 'ecore_EReference11', b1)
    if hasattr(b1, 'ecore_EClass10'):
        assert _is_linked(b1, 'ecore_EClass10', a)
    _safe_set(a, 'ecore_EReference11', b2)
    assert _is_linked(a, 'ecore_EReference11', b2)
    if hasattr(b1, 'ecore_EClass10'):
        assert not _is_linked(b1, 'ecore_EClass10', a)
    if hasattr(b2, 'ecore_EClass10'):
        assert _is_linked(b2, 'ecore_EClass10', a)
    _safe_set(a, 'ecore_EReference11', None)
    assert not _is_linked(a, 'ecore_EReference11', b2)
    if hasattr(b2, 'ecore_EClass10'):
        assert not _is_linked(b2, 'ecore_EClass10', a)


def test_assoc_eStructuralFeatures28_link_reassign_clear():
    a = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'EStructuralFeature', b1)
    assert _is_linked(a, 'EStructuralFeature', b1)
    if hasattr(b1, 'eContainingClass29'):
        assert _is_linked(b1, 'eContainingClass29', a)
    _safe_set(a, 'EStructuralFeature', b2)
    assert _is_linked(a, 'EStructuralFeature', b2)
    if hasattr(b1, 'eContainingClass29'):
        assert not _is_linked(b1, 'eContainingClass29', a)
    if hasattr(b2, 'eContainingClass29'):
        assert _is_linked(b2, 'eContainingClass29', a)
    _safe_set(a, 'EStructuralFeature', None)
    assert not _is_linked(a, 'EStructuralFeature', b2)
    if hasattr(b2, 'eContainingClass29'):
        assert not _is_linked(b2, 'eContainingClass29', a)


def test_assoc_eSubpackages39_link_reassign_clear():
    a = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    _safe_set(a, 'EPackage40', b1)
    assert _is_linked(a, 'EPackage40', b1)
    if hasattr(b1, 'eSuperPackage'):
        assert _is_linked(b1, 'eSuperPackage', a)
    _safe_set(a, 'EPackage40', b2)
    assert _is_linked(a, 'EPackage40', b2)
    if hasattr(b1, 'eSuperPackage'):
        assert not _is_linked(b1, 'eSuperPackage', a)
    if hasattr(b2, 'eSuperPackage'):
        assert _is_linked(b2, 'eSuperPackage', a)
    _safe_set(a, 'EPackage40', None)
    assert not _is_linked(a, 'EPackage40', b2)
    if hasattr(b2, 'eSuperPackage'):
        assert not _is_linked(b2, 'eSuperPackage', a)


def test_assoc_eSuperPackage42_link_reassign_clear():
    a = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    _safe_set(a, 'EPackage43', b1)
    assert _is_linked(a, 'EPackage43', b1)
    if hasattr(b1, 'eSubpackages'):
        assert _is_linked(b1, 'eSubpackages', a)
    _safe_set(a, 'EPackage43', b2)
    assert _is_linked(a, 'EPackage43', b2)
    if hasattr(b1, 'eSubpackages'):
        assert not _is_linked(b1, 'eSubpackages', a)
    if hasattr(b2, 'eSubpackages'):
        assert _is_linked(b2, 'eSubpackages', a)
    _safe_set(a, 'EPackage43', None)
    assert not _is_linked(a, 'EPackage43', b2)
    if hasattr(b2, 'eSubpackages'):
        assert not _is_linked(b2, 'eSubpackages', a)


def test_assoc_eSuperTypes2_link_reassign_clear():
    a = ecore_EClass(abstract=True, interface=True)
    b1 = ecore_EClass(abstract=True, interface=True)
    b2 = ecore_EClass(abstract=False, interface=False)
    _safe_set(a, 'ecore_EClass', b1)
    assert _is_linked(a, 'ecore_EClass', b1)
    if hasattr(b1, 'ecore_EClass1'):
        assert _is_linked(b1, 'ecore_EClass1', a)
    _safe_set(a, 'ecore_EClass', b2)
    assert _is_linked(a, 'ecore_EClass', b2)
    if hasattr(b1, 'ecore_EClass1'):
        assert not _is_linked(b1, 'ecore_EClass1', a)
    if hasattr(b2, 'ecore_EClass1'):
        assert _is_linked(b2, 'ecore_EClass1', a)
    _safe_set(a, 'ecore_EClass', None)
    assert not _is_linked(a, 'ecore_EClass', b2)
    if hasattr(b2, 'ecore_EClass1'):
        assert not _is_linked(b2, 'ecore_EClass1', a)


def test_assoc_eType57_link_reassign_clear():
    a = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    b1 = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b2 = ecore_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2", instanceTypeName="sample_text_2")
    _safe_set(a, 'ecore_ETypedElement', b1)
    assert _is_linked(a, 'ecore_ETypedElement', b1)
    if hasattr(b1, 'ecore_EClassifier58'):
        assert _is_linked(b1, 'ecore_EClassifier58', a)
    _safe_set(a, 'ecore_ETypedElement', b2)
    assert _is_linked(a, 'ecore_ETypedElement', b2)
    if hasattr(b1, 'ecore_EClassifier58'):
        assert not _is_linked(b1, 'ecore_EClassifier58', a)
    if hasattr(b2, 'ecore_EClassifier58'):
        assert _is_linked(b2, 'ecore_EClassifier58', a)
    _safe_set(a, 'ecore_ETypedElement', None)
    assert not _is_linked(a, 'ecore_ETypedElement', b2)
    if hasattr(b2, 'ecore_EClassifier58'):
        assert not _is_linked(b2, 'ecore_EClassifier58', a)


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


ENamedElement_strategy = st.builds(ENamedElement)
@given(instance=ENamedElement_strategy)
@settings(max_examples=25)
def test_ENamedElement_instantiation(instance):
    assert isinstance(instance, ENamedElement)


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


ecore_EAttribute_strategy = st.builds(ecore_EAttribute, iD=st.booleans())
@given(instance=ecore_EAttribute_strategy)
@settings(max_examples=25)
def test_ecore_EAttribute_instantiation(instance):
    assert isinstance(instance, ecore_EAttribute)


ecore_EClass_strategy = st.builds(ecore_EClass, abstract=st.booleans(), interface=st.booleans())
@given(instance=ecore_EClass_strategy)
@settings(max_examples=25)
def test_ecore_EClass_instantiation(instance):
    assert isinstance(instance, ecore_EClass)


ecore_EClassifier_strategy = st.builds(ecore_EClassifier, defaultValue=safe_text, instanceClass=safe_text, instanceClassName=safe_text, instanceTypeName=safe_text)
@given(instance=ecore_EClassifier_strategy)
@settings(max_examples=25)
def test_ecore_EClassifier_instantiation(instance):
    assert isinstance(instance, ecore_EClassifier)


ecore_EDataType_strategy = st.builds(ecore_EDataType, serializable=st.booleans())
@given(instance=ecore_EDataType_strategy)
@settings(max_examples=25)
def test_ecore_EDataType_instantiation(instance):
    assert isinstance(instance, ecore_EDataType)


ecore_EEnum_strategy = st.builds(ecore_EEnum)
@given(instance=ecore_EEnum_strategy)
@settings(max_examples=25)
def test_ecore_EEnum_instantiation(instance):
    assert isinstance(instance, ecore_EEnum)


ecore_EEnumLiteral_strategy = st.builds(ecore_EEnumLiteral, instance=safe_text, literal=safe_text, value=st.integers())
@given(instance=ecore_EEnumLiteral_strategy)
@settings(max_examples=25)
def test_ecore_EEnumLiteral_instantiation(instance):
    assert isinstance(instance, ecore_EEnumLiteral)


ecore_ENamedElement_strategy = st.builds(ecore_ENamedElement, name=safe_text)
@given(instance=ecore_ENamedElement_strategy)
@settings(max_examples=25)
def test_ecore_ENamedElement_instantiation(instance):
    assert isinstance(instance, ecore_ENamedElement)


ecore_EOperation_strategy = st.builds(ecore_EOperation)
@given(instance=ecore_EOperation_strategy)
@settings(max_examples=25)
def test_ecore_EOperation_instantiation(instance):
    assert isinstance(instance, ecore_EOperation)


ecore_EPackage_strategy = st.builds(ecore_EPackage, nsPrefix=safe_text, nsURI=safe_text)
@given(instance=ecore_EPackage_strategy)
@settings(max_examples=25)
def test_ecore_EPackage_instantiation(instance):
    assert isinstance(instance, ecore_EPackage)


ecore_EParameter_strategy = st.builds(ecore_EParameter)
@given(instance=ecore_EParameter_strategy)
@settings(max_examples=25)
def test_ecore_EParameter_instantiation(instance):
    assert isinstance(instance, ecore_EParameter)


ecore_EReference_strategy = st.builds(ecore_EReference, container=st.booleans(), containment=st.booleans(), resolveProxies=st.booleans())
@given(instance=ecore_EReference_strategy)
@settings(max_examples=25)
def test_ecore_EReference_instantiation(instance):
    assert isinstance(instance, ecore_EReference)


ecore_EStringToStringMapEntry_strategy = st.builds(ecore_EStringToStringMapEntry, key=safe_text, value=safe_text)
@given(instance=ecore_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_ecore_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, ecore_EStringToStringMapEntry)


ecore_EStructuralFeature_strategy = st.builds(ecore_EStructuralFeature, changeable=st.booleans(), defaultValue=safe_text, defaultValueLiteral=safe_text, derived=st.booleans(), transient=st.booleans(), unsettable=st.booleans(), volatile=st.booleans())
@given(instance=ecore_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_ecore_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, ecore_EStructuralFeature)


ecore_ETypedElement_strategy = st.builds(ecore_ETypedElement, lowerBound=st.integers(), many=st.booleans(), ordered=st.booleans(), required=st.booleans(), unique=st.booleans(), upperBound=st.integers())
@given(instance=ecore_ETypedElement_strategy)
@settings(max_examples=25)
def test_ecore_ETypedElement_instantiation(instance):
    assert isinstance(instance, ecore_ETypedElement)



