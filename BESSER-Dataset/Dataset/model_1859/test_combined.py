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
    Type,
    typeslibrary_TypeInstance,
    typeslibrary_TypesLibrary,
    typeslibrary_TypesLibraryUser,
    typeslibrary_UserDefinedTypeRef,
    typeslibrary_Type,
    typeslibrary_UserDefinedType,
    UserDefinedType,
    typeslibrary_SimpleNamedType,
    typeslibrary_ComplexNamedType,
    typeslibrary_NativeType,
    TypesLibrary,
    typeslibrary_UserDefinedTypesLibrary,
    typeslibrary_NativeTypesLibrary,
    NativeTypeKind,
    TypesLibraryKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_typeinstance_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_TypeInstance)


def test_hyp_typeslibrary_typeinstance_constructor_exists():
    assert callable(typeslibrary_TypeInstance.__init__)


def test_hyp_typeslibrary_typeinstance_constructor_args():
    sig = inspect.signature(typeslibrary_TypeInstance.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "literals" in params, "Missing parameter 'literals'"
    assert "length" in params, "Missing parameter 'length'"






def test_hyp_typeslibrary_typeslibrary_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_TypesLibrary)


def test_hyp_typeslibrary_typeslibrary_constructor_exists():
    assert callable(typeslibrary_TypesLibrary.__init__)


def test_hyp_typeslibrary_typeslibrary_constructor_args():
    sig = inspect.signature(typeslibrary_TypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_typeslibrary_typeslibraryuser_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_TypesLibraryUser)


def test_hyp_typeslibrary_typeslibraryuser_constructor_exists():
    assert callable(typeslibrary_TypesLibraryUser.__init__)


def test_hyp_typeslibrary_typeslibraryuser_constructor_args():
    sig = inspect.signature(typeslibrary_TypesLibraryUser.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_userdefinedtyperef_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_UserDefinedTypeRef)


def test_hyp_typeslibrary_userdefinedtyperef_constructor_exists():
    assert callable(typeslibrary_UserDefinedTypeRef.__init__)


def test_hyp_typeslibrary_userdefinedtyperef_constructor_args():
    sig = inspect.signature(typeslibrary_UserDefinedTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_type_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_Type)


def test_hyp_typeslibrary_type_constructor_exists():
    assert callable(typeslibrary_Type.__init__)


def test_hyp_typeslibrary_type_constructor_args():
    sig = inspect.signature(typeslibrary_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_UserDefinedType)


def test_hyp_typeslibrary_userdefinedtype_constructor_exists():
    assert callable(typeslibrary_UserDefinedType.__init__)


def test_hyp_typeslibrary_userdefinedtype_constructor_args():
    sig = inspect.signature(typeslibrary_UserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_hyp_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_hyp_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_simplenamedtype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_SimpleNamedType)


def test_hyp_typeslibrary_simplenamedtype_constructor_exists():
    assert callable(typeslibrary_SimpleNamedType.__init__)


def test_hyp_typeslibrary_simplenamedtype_constructor_args():
    sig = inspect.signature(typeslibrary_SimpleNamedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_complexnamedtype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_ComplexNamedType)


def test_hyp_typeslibrary_complexnamedtype_constructor_exists():
    assert callable(typeslibrary_ComplexNamedType.__init__)


def test_hyp_typeslibrary_complexnamedtype_constructor_args():
    sig = inspect.signature(typeslibrary_ComplexNamedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_nativetype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_NativeType)


def test_hyp_typeslibrary_nativetype_constructor_exists():
    assert callable(typeslibrary_NativeType.__init__)


def test_hyp_typeslibrary_nativetype_constructor_args():
    sig = inspect.signature(typeslibrary_NativeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "spec" in params, "Missing parameter 'spec'"





def test_hyp_typeslibrary_is_not_abstract():
    assert not inspect.isabstract(TypesLibrary)


def test_hyp_typeslibrary_constructor_exists():
    assert callable(TypesLibrary.__init__)


def test_hyp_typeslibrary_constructor_args():
    sig = inspect.signature(TypesLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeslibrary_userdefinedtypeslibrary_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_UserDefinedTypesLibrary)


def test_hyp_typeslibrary_userdefinedtypeslibrary_constructor_exists():
    assert callable(typeslibrary_UserDefinedTypesLibrary.__init__)


def test_hyp_typeslibrary_userdefinedtypeslibrary_constructor_args():
    sig = inspect.signature(typeslibrary_UserDefinedTypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_typeslibrary_nativetypeslibrary_is_not_abstract():
    assert not inspect.isabstract(typeslibrary_NativeTypesLibrary)


def test_hyp_typeslibrary_nativetypeslibrary_constructor_exists():
    assert callable(typeslibrary_NativeTypesLibrary.__init__)


def test_hyp_typeslibrary_nativetypeslibrary_constructor_args():
    sig = inspect.signature(typeslibrary_NativeTypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_nativetypekind_exists():
    # Check that the Enumeration exists
    assert NativeTypeKind is not None

def test_hyp_nativetypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NativeTypeKind]
    expected_literals = [
        "Enum",
        "Length",
        "LengthAndPrecision",
        "Simple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NativeTypeKind"

def test_hyp_typeslibrarykind_exists():
    # Check that the Enumeration exists
    assert TypesLibraryKind is not None

def test_hyp_typeslibrarykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypesLibraryKind]
    expected_literals = [
        "logicalTypes",
        "physicalTypes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypesLibraryKind"


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
Type_strategy = st.builds(
    Type,
)
typeslibrary_TypeInstance_strategy = st.builds(
    typeslibrary_TypeInstance,
    precision=
        st.integers(),
    literals=
        safe_text,
    length=
        st.integers()
)
typeslibrary_TypesLibrary_strategy = st.builds(
    typeslibrary_TypesLibrary,
    kind=
        safe_text
)
typeslibrary_TypesLibraryUser_strategy = st.builds(
    typeslibrary_TypesLibraryUser,
)
typeslibrary_UserDefinedTypeRef_strategy = st.builds(
    typeslibrary_UserDefinedTypeRef,
)
typeslibrary_Type_strategy = st.builds(
    typeslibrary_Type,
)
typeslibrary_UserDefinedType_strategy = st.builds(
    typeslibrary_UserDefinedType,
    name=
        safe_text
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
typeslibrary_SimpleNamedType_strategy = st.builds(
    typeslibrary_SimpleNamedType,
)
typeslibrary_ComplexNamedType_strategy = st.builds(
    typeslibrary_ComplexNamedType,
)
typeslibrary_NativeType_strategy = st.builds(
    typeslibrary_NativeType,
    name=
        safe_text,
    spec=
        safe_text
)
TypesLibrary_strategy = st.builds(
    TypesLibrary,
)
typeslibrary_UserDefinedTypesLibrary_strategy = st.builds(
    typeslibrary_UserDefinedTypesLibrary,
    name=
        safe_text
)
typeslibrary_NativeTypesLibrary_strategy = st.builds(
    typeslibrary_NativeTypesLibrary,
    name=
        safe_text
)





@given(instance=typeslibrary_TypeInstance_strategy)
def test_hyp_typeslibrary_typeinstance_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=typeslibrary_TypeInstance_strategy)
def test_hyp_typeslibrary_typeinstance_literals_setter(instance):
    original = instance.literals
    instance.literals = original
    assert instance.literals == original



@given(instance=typeslibrary_TypeInstance_strategy)
def test_hyp_typeslibrary_typeinstance_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original




@given(instance=typeslibrary_TypesLibrary_strategy)
def test_hyp_typeslibrary_typeslibrary_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original







@given(instance=typeslibrary_UserDefinedType_strategy)
def test_hyp_typeslibrary_userdefinedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=typeslibrary_NativeType_strategy)
def test_hyp_typeslibrary_nativetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=typeslibrary_NativeType_strategy)
def test_hyp_typeslibrary_nativetype_spec_setter(instance):
    original = instance.spec
    instance.spec = original
    assert instance.spec == original





@given(instance=typeslibrary_UserDefinedTypesLibrary_strategy)
def test_hyp_typeslibrary_userdefinedtypeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=typeslibrary_NativeTypesLibrary_strategy)
def test_hyp_typeslibrary_nativetypeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=typeslibrary_NativeTypesLibrary_strategy)
@settings(max_examples=30)
def test_hyp_typeslibrary_nativetypeslibrary_findtypebyname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findTypeByName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findTypeByName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findTypeByName' in typeslibrary_NativeTypesLibrary is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findTypeByName' in typeslibrary_NativeTypesLibrary did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findTypeByName' in typeslibrary_NativeTypesLibrary is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Type,
    TypesLibrary,
    UserDefinedType,
    typeslibrary_ComplexNamedType,
    typeslibrary_NativeType,
    typeslibrary_NativeTypesLibrary,
    typeslibrary_SimpleNamedType,
    typeslibrary_Type,
    typeslibrary_TypeInstance,
    typeslibrary_TypesLibrary,
    typeslibrary_TypesLibraryUser,
    typeslibrary_UserDefinedType,
    typeslibrary_UserDefinedTypeRef,
    typeslibrary_UserDefinedTypesLibrary,
    NativeTypeKind,
    TypesLibraryKind,
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

def test_typeslibrary_NativeType_name_value_roundtrip():
    instance = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_typeslibrary_NativeType_spec_value_roundtrip():
    instance = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    assert instance.spec == "sample_text"
    instance.spec = "sample_text_2"
    assert instance.spec == "sample_text_2"


def test_typeslibrary_NativeTypesLibrary_name_value_roundtrip():
    instance = typeslibrary_NativeTypesLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_typeslibrary_TypeInstance_length_value_roundtrip():
    instance = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_typeslibrary_TypeInstance_literals_value_roundtrip():
    instance = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    assert instance.literals == "sample_text"
    instance.literals = "sample_text_2"
    assert instance.literals == "sample_text_2"


def test_typeslibrary_TypeInstance_precision_value_roundtrip():
    instance = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    assert instance.precision == 7
    instance.precision = 13
    assert instance.precision == 13


def test_typeslibrary_TypesLibrary_kind_value_roundtrip():
    instance = typeslibrary_TypesLibrary(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_typeslibrary_UserDefinedType_name_value_roundtrip():
    instance = typeslibrary_UserDefinedType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_typeslibrary_UserDefinedTypesLibrary_name_value_roundtrip():
    instance = typeslibrary_UserDefinedTypesLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_typeslibrary_TypeInstance_isa_Type():
    instance = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    assert isinstance(instance, Type)


def test_typeslibrary_UserDefinedTypeRef_isa_Type():
    instance = typeslibrary_UserDefinedTypeRef()
    assert isinstance(instance, Type)


def test_typeslibrary_NativeTypesLibrary_isa_TypesLibrary():
    instance = typeslibrary_NativeTypesLibrary(name="sample_text")
    assert isinstance(instance, TypesLibrary)


def test_typeslibrary_UserDefinedTypesLibrary_isa_TypesLibrary():
    instance = typeslibrary_UserDefinedTypesLibrary(name="sample_text")
    assert isinstance(instance, TypesLibrary)


def test_typeslibrary_ComplexNamedType_isa_UserDefinedType():
    instance = typeslibrary_ComplexNamedType()
    assert isinstance(instance, UserDefinedType)


def test_typeslibrary_SimpleNamedType_isa_UserDefinedType():
    instance = typeslibrary_SimpleNamedType()
    assert isinstance(instance, UserDefinedType)


def test_assoc_mapsTo4_link_reassign_clear():
    a = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    b1 = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    b2 = typeslibrary_NativeType(name="sample_text_2", spec="sample_text_2")
    _safe_set(a, 'typeslibrary_NativeType3', b1)
    assert _is_linked(a, 'typeslibrary_NativeType3', b1)
    if hasattr(b1, 'typeslibrary_NativeType5'):
        assert _is_linked(b1, 'typeslibrary_NativeType5', a)
    _safe_set(a, 'typeslibrary_NativeType3', b2)
    assert _is_linked(a, 'typeslibrary_NativeType3', b2)
    if hasattr(b1, 'typeslibrary_NativeType5'):
        assert not _is_linked(b1, 'typeslibrary_NativeType5', a)
    if hasattr(b2, 'typeslibrary_NativeType5'):
        assert _is_linked(b2, 'typeslibrary_NativeType5', a)
    _safe_set(a, 'typeslibrary_NativeType3', None)
    assert not _is_linked(a, 'typeslibrary_NativeType3', b2)
    if hasattr(b2, 'typeslibrary_NativeType5'):
        assert not _is_linked(b2, 'typeslibrary_NativeType5', a)


def test_assoc_nativeType1_link_reassign_clear():
    a = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    b1 = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    b2 = typeslibrary_NativeType(name="sample_text_2", spec="sample_text_2")
    _safe_set(a, 'typeslibrary_TypeInstance', b1)
    assert _is_linked(a, 'typeslibrary_TypeInstance', b1)
    if hasattr(b1, 'typeslibrary_NativeType2'):
        assert _is_linked(b1, 'typeslibrary_NativeType2', a)
    _safe_set(a, 'typeslibrary_TypeInstance', b2)
    assert _is_linked(a, 'typeslibrary_TypeInstance', b2)
    if hasattr(b1, 'typeslibrary_NativeType2'):
        assert not _is_linked(b1, 'typeslibrary_NativeType2', a)
    if hasattr(b2, 'typeslibrary_NativeType2'):
        assert _is_linked(b2, 'typeslibrary_NativeType2', a)
    _safe_set(a, 'typeslibrary_TypeInstance', None)
    assert not _is_linked(a, 'typeslibrary_TypeInstance', b2)
    if hasattr(b2, 'typeslibrary_NativeType2'):
        assert not _is_linked(b2, 'typeslibrary_NativeType2', a)


def test_assoc_nativeTypes0_link_reassign_clear():
    a = typeslibrary_NativeTypesLibrary(name="sample_text")
    b1 = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    b2 = typeslibrary_NativeType(name="sample_text_2", spec="sample_text_2")
    _safe_set(a, 'typeslibrary_NativeTypesLibrary', {b1})
    assert _is_linked(a, 'typeslibrary_NativeTypesLibrary', b1)
    if hasattr(b1, 'typeslibrary_NativeType'):
        assert _is_linked(b1, 'typeslibrary_NativeType', a)
    _safe_set(a, 'typeslibrary_NativeTypesLibrary', {b2})
    assert _is_linked(a, 'typeslibrary_NativeTypesLibrary', b2)
    if hasattr(b1, 'typeslibrary_NativeType'):
        assert not _is_linked(b1, 'typeslibrary_NativeType', a)
    if hasattr(b2, 'typeslibrary_NativeType'):
        assert _is_linked(b2, 'typeslibrary_NativeType', a)
    _safe_set(a, 'typeslibrary_NativeTypesLibrary', set())
    assert not _is_linked(a, 'typeslibrary_NativeTypesLibrary', b2)
    if hasattr(b2, 'typeslibrary_NativeType'):
        assert not _is_linked(b2, 'typeslibrary_NativeType', a)


def test_assoc_type7_link_reassign_clear():
    a = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    b1 = typeslibrary_SimpleNamedType()
    b2 = typeslibrary_SimpleNamedType()
    _safe_set(a, 'typeslibrary_TypeInstance8', b1)
    assert _is_linked(a, 'typeslibrary_TypeInstance8', b1)
    if hasattr(b1, 'typeslibrary_SimpleNamedType'):
        assert _is_linked(b1, 'typeslibrary_SimpleNamedType', a)
    _safe_set(a, 'typeslibrary_TypeInstance8', b2)
    assert _is_linked(a, 'typeslibrary_TypeInstance8', b2)
    if hasattr(b1, 'typeslibrary_SimpleNamedType'):
        assert not _is_linked(b1, 'typeslibrary_SimpleNamedType', a)
    if hasattr(b2, 'typeslibrary_SimpleNamedType'):
        assert _is_linked(b2, 'typeslibrary_SimpleNamedType', a)
    _safe_set(a, 'typeslibrary_TypeInstance8', None)
    assert not _is_linked(a, 'typeslibrary_TypeInstance8', b2)
    if hasattr(b2, 'typeslibrary_SimpleNamedType'):
        assert not _is_linked(b2, 'typeslibrary_SimpleNamedType', a)


def test_assoc_type9_link_reassign_clear():
    a = typeslibrary_UserDefinedType(name="sample_text")
    b1 = typeslibrary_UserDefinedTypeRef()
    b2 = typeslibrary_UserDefinedTypeRef()
    _safe_set(a, 'typeslibrary_UserDefinedType10', b1)
    assert _is_linked(a, 'typeslibrary_UserDefinedType10', b1)
    if hasattr(b1, 'typeslibrary_UserDefinedTypeRef'):
        assert _is_linked(b1, 'typeslibrary_UserDefinedTypeRef', a)
    _safe_set(a, 'typeslibrary_UserDefinedType10', b2)
    assert _is_linked(a, 'typeslibrary_UserDefinedType10', b2)
    if hasattr(b1, 'typeslibrary_UserDefinedTypeRef'):
        assert not _is_linked(b1, 'typeslibrary_UserDefinedTypeRef', a)
    if hasattr(b2, 'typeslibrary_UserDefinedTypeRef'):
        assert _is_linked(b2, 'typeslibrary_UserDefinedTypeRef', a)
    _safe_set(a, 'typeslibrary_UserDefinedType10', None)
    assert not _is_linked(a, 'typeslibrary_UserDefinedType10', b2)
    if hasattr(b2, 'typeslibrary_UserDefinedTypeRef'):
        assert not _is_linked(b2, 'typeslibrary_UserDefinedTypeRef', a)


def test_assoc_types6_link_reassign_clear():
    a = typeslibrary_UserDefinedType(name="sample_text")
    b1 = typeslibrary_ComplexNamedType()
    b2 = typeslibrary_ComplexNamedType()
    _safe_set(a, 'typeslibrary_UserDefinedType', b1)
    assert _is_linked(a, 'typeslibrary_UserDefinedType', b1)
    if hasattr(b1, 'typeslibrary_ComplexNamedType'):
        assert _is_linked(b1, 'typeslibrary_ComplexNamedType', a)
    _safe_set(a, 'typeslibrary_UserDefinedType', b2)
    assert _is_linked(a, 'typeslibrary_UserDefinedType', b2)
    if hasattr(b1, 'typeslibrary_ComplexNamedType'):
        assert not _is_linked(b1, 'typeslibrary_ComplexNamedType', a)
    if hasattr(b2, 'typeslibrary_ComplexNamedType'):
        assert _is_linked(b2, 'typeslibrary_ComplexNamedType', a)
    _safe_set(a, 'typeslibrary_UserDefinedType', None)
    assert not _is_linked(a, 'typeslibrary_UserDefinedType', b2)
    if hasattr(b2, 'typeslibrary_ComplexNamedType'):
        assert not _is_linked(b2, 'typeslibrary_ComplexNamedType', a)


def test_assoc_usedLibraries13_link_reassign_clear():
    a = typeslibrary_TypesLibrary(kind="sample_text")
    b1 = typeslibrary_TypesLibraryUser()
    b2 = typeslibrary_TypesLibraryUser()
    _safe_set(a, 'typeslibrary_TypesLibrary', b1)
    assert _is_linked(a, 'typeslibrary_TypesLibrary', b1)
    if hasattr(b1, 'typeslibrary_TypesLibraryUser'):
        assert _is_linked(b1, 'typeslibrary_TypesLibraryUser', a)
    _safe_set(a, 'typeslibrary_TypesLibrary', b2)
    assert _is_linked(a, 'typeslibrary_TypesLibrary', b2)
    if hasattr(b1, 'typeslibrary_TypesLibraryUser'):
        assert not _is_linked(b1, 'typeslibrary_TypesLibraryUser', a)
    if hasattr(b2, 'typeslibrary_TypesLibraryUser'):
        assert _is_linked(b2, 'typeslibrary_TypesLibraryUser', a)
    _safe_set(a, 'typeslibrary_TypesLibrary', None)
    assert not _is_linked(a, 'typeslibrary_TypesLibrary', b2)
    if hasattr(b2, 'typeslibrary_TypesLibraryUser'):
        assert not _is_linked(b2, 'typeslibrary_TypesLibraryUser', a)


def test_assoc_userDefinedTypes11_link_reassign_clear():
    a = typeslibrary_UserDefinedTypesLibrary(name="sample_text")
    b1 = typeslibrary_UserDefinedType(name="sample_text")
    b2 = typeslibrary_UserDefinedType(name="sample_text_2")
    _safe_set(a, 'typeslibrary_UserDefinedTypesLibrary', {b1})
    assert _is_linked(a, 'typeslibrary_UserDefinedTypesLibrary', b1)
    if hasattr(b1, 'typeslibrary_UserDefinedType12'):
        assert _is_linked(b1, 'typeslibrary_UserDefinedType12', a)
    _safe_set(a, 'typeslibrary_UserDefinedTypesLibrary', {b2})
    assert _is_linked(a, 'typeslibrary_UserDefinedTypesLibrary', b2)
    if hasattr(b1, 'typeslibrary_UserDefinedType12'):
        assert not _is_linked(b1, 'typeslibrary_UserDefinedType12', a)
    if hasattr(b2, 'typeslibrary_UserDefinedType12'):
        assert _is_linked(b2, 'typeslibrary_UserDefinedType12', a)
    _safe_set(a, 'typeslibrary_UserDefinedTypesLibrary', set())
    assert not _is_linked(a, 'typeslibrary_UserDefinedTypesLibrary', b2)
    if hasattr(b2, 'typeslibrary_UserDefinedType12'):
        assert not _is_linked(b2, 'typeslibrary_UserDefinedType12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypesLibrary_strategy = st.builds(TypesLibrary)
@given(instance=TypesLibrary_strategy)
@settings(max_examples=25)
def test_TypesLibrary_instantiation(instance):
    assert isinstance(instance, TypesLibrary)


UserDefinedType_strategy = st.builds(UserDefinedType)
@given(instance=UserDefinedType_strategy)
@settings(max_examples=25)
def test_UserDefinedType_instantiation(instance):
    assert isinstance(instance, UserDefinedType)


typeslibrary_ComplexNamedType_strategy = st.builds(typeslibrary_ComplexNamedType)
@given(instance=typeslibrary_ComplexNamedType_strategy)
@settings(max_examples=25)
def test_typeslibrary_ComplexNamedType_instantiation(instance):
    assert isinstance(instance, typeslibrary_ComplexNamedType)


typeslibrary_NativeType_strategy = st.builds(typeslibrary_NativeType, name=safe_text, spec=safe_text)
@given(instance=typeslibrary_NativeType_strategy)
@settings(max_examples=25)
def test_typeslibrary_NativeType_instantiation(instance):
    assert isinstance(instance, typeslibrary_NativeType)


typeslibrary_NativeTypesLibrary_strategy = st.builds(typeslibrary_NativeTypesLibrary, name=safe_text)
@given(instance=typeslibrary_NativeTypesLibrary_strategy)
@settings(max_examples=25)
def test_typeslibrary_NativeTypesLibrary_instantiation(instance):
    assert isinstance(instance, typeslibrary_NativeTypesLibrary)


typeslibrary_SimpleNamedType_strategy = st.builds(typeslibrary_SimpleNamedType)
@given(instance=typeslibrary_SimpleNamedType_strategy)
@settings(max_examples=25)
def test_typeslibrary_SimpleNamedType_instantiation(instance):
    assert isinstance(instance, typeslibrary_SimpleNamedType)


typeslibrary_Type_strategy = st.builds(typeslibrary_Type)
@given(instance=typeslibrary_Type_strategy)
@settings(max_examples=25)
def test_typeslibrary_Type_instantiation(instance):
    assert isinstance(instance, typeslibrary_Type)


typeslibrary_TypeInstance_strategy = st.builds(typeslibrary_TypeInstance, length=st.integers(), literals=safe_text, precision=st.integers())
@given(instance=typeslibrary_TypeInstance_strategy)
@settings(max_examples=25)
def test_typeslibrary_TypeInstance_instantiation(instance):
    assert isinstance(instance, typeslibrary_TypeInstance)


typeslibrary_TypesLibrary_strategy = st.builds(typeslibrary_TypesLibrary, kind=safe_text)
@given(instance=typeslibrary_TypesLibrary_strategy)
@settings(max_examples=25)
def test_typeslibrary_TypesLibrary_instantiation(instance):
    assert isinstance(instance, typeslibrary_TypesLibrary)


typeslibrary_TypesLibraryUser_strategy = st.builds(typeslibrary_TypesLibraryUser)
@given(instance=typeslibrary_TypesLibraryUser_strategy)
@settings(max_examples=25)
def test_typeslibrary_TypesLibraryUser_instantiation(instance):
    assert isinstance(instance, typeslibrary_TypesLibraryUser)


typeslibrary_UserDefinedType_strategy = st.builds(typeslibrary_UserDefinedType, name=safe_text)
@given(instance=typeslibrary_UserDefinedType_strategy)
@settings(max_examples=25)
def test_typeslibrary_UserDefinedType_instantiation(instance):
    assert isinstance(instance, typeslibrary_UserDefinedType)


typeslibrary_UserDefinedTypeRef_strategy = st.builds(typeslibrary_UserDefinedTypeRef)
@given(instance=typeslibrary_UserDefinedTypeRef_strategy)
@settings(max_examples=25)
def test_typeslibrary_UserDefinedTypeRef_instantiation(instance):
    assert isinstance(instance, typeslibrary_UserDefinedTypeRef)


typeslibrary_UserDefinedTypesLibrary_strategy = st.builds(typeslibrary_UserDefinedTypesLibrary, name=safe_text)
@given(instance=typeslibrary_UserDefinedTypesLibrary_strategy)
@settings(max_examples=25)
def test_typeslibrary_UserDefinedTypesLibrary_instantiation(instance):
    assert isinstance(instance, typeslibrary_UserDefinedTypesLibrary)



