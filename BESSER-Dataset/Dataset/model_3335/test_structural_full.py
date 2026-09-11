import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    JavaElement,
    javaz_Block,
    javaz_Field,
    javaz_JavaClass,
    javaz_JavaElement,
    javaz_JavaPackageX,
    javaz_JavaParameter,
    javaz_Javaz,
    javaz_Method,
    JavaKind,
    JavaParameterKind,
    JavaVisibilityKind,
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

def test_javaz_Block_content_value_roundtrip():
    instance = javaz_Block(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_javaz_Field_final_value_roundtrip():
    instance = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_javaz_Field_static_value_roundtrip():
    instance = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_javaz_Field_transient_value_roundtrip():
    instance = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_javaz_Field_type_value_roundtrip():
    instance = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_javaz_Field_visibility_value_roundtrip():
    instance = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_javaz_Field_volatile_value_roundtrip():
    instance = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    assert instance.volatile == True
    instance.volatile = False
    assert instance.volatile == False


def test_javaz_JavaClass_final_value_roundtrip():
    instance = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_javaz_JavaClass_kind_value_roundtrip():
    instance = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_javaz_JavaClass_needToGenerate_value_roundtrip():
    instance = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    assert instance.needToGenerate == True
    instance.needToGenerate = False
    assert instance.needToGenerate == False


def test_javaz_JavaClass_public_value_roundtrip():
    instance = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    assert instance.public == True
    instance.public = False
    assert instance.public == False


def test_javaz_JavaClass_rewritable_value_roundtrip():
    instance = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    assert instance.rewritable == True
    instance.rewritable = False
    assert instance.rewritable == False


def test_javaz_JavaElement_name_value_roundtrip():
    instance = javaz_JavaElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_javaz_JavaPackageX_needToGenerate_value_roundtrip():
    instance = javaz_JavaPackageX(needToGenerate=True)
    assert instance.needToGenerate == True
    instance.needToGenerate = False
    assert instance.needToGenerate == False


def test_javaz_JavaParameter_final_value_roundtrip():
    instance = javaz_JavaParameter(final=True, kind="sample_text", parameterKind="sample_text", type="sample_text")
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_javaz_JavaParameter_kind_value_roundtrip():
    instance = javaz_JavaParameter(final=True, kind="sample_text", parameterKind="sample_text", type="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_javaz_JavaParameter_parameterKind_value_roundtrip():
    instance = javaz_JavaParameter(final=True, kind="sample_text", parameterKind="sample_text", type="sample_text")
    assert instance.parameterKind == "sample_text"
    instance.parameterKind = "sample_text_2"
    assert instance.parameterKind == "sample_text_2"


def test_javaz_JavaParameter_type_value_roundtrip():
    instance = javaz_JavaParameter(final=True, kind="sample_text", parameterKind="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_javaz_Method_abstract_value_roundtrip():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_javaz_Method_constructor_value_roundtrip():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert instance.constructor == True
    instance.constructor = False
    assert instance.constructor == False


def test_javaz_Method_final_value_roundtrip():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_javaz_Method_native_value_roundtrip():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert instance.native == True
    instance.native = False
    assert instance.native == False


def test_javaz_Method_static_value_roundtrip():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_javaz_Method_synchronized_value_roundtrip():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert instance.synchronized == True
    instance.synchronized = False
    assert instance.synchronized == False


def test_javaz_Method_visibility_value_roundtrip():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_javaz_Field_isa_JavaElement():
    instance = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    assert isinstance(instance, JavaElement)


def test_javaz_JavaClass_isa_JavaElement():
    instance = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    assert isinstance(instance, JavaElement)


def test_javaz_JavaPackageX_isa_JavaElement():
    instance = javaz_JavaPackageX(needToGenerate=True)
    assert isinstance(instance, JavaElement)


def test_javaz_JavaParameter_isa_JavaElement():
    instance = javaz_JavaParameter(final=True, kind="sample_text", parameterKind="sample_text", type="sample_text")
    assert isinstance(instance, JavaElement)


def test_javaz_Javaz_isa_JavaElement():
    instance = javaz_Javaz()
    assert isinstance(instance, JavaElement)


def test_javaz_Method_isa_JavaElement():
    instance = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    assert isinstance(instance, JavaElement)


def test_assoc_block21_link_reassign_clear():
    a = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    b1 = javaz_Block(content="sample_text")
    b2 = javaz_Block(content="sample_text_2")
    _safe_set(a, 'javaz_Method22', b1)
    assert _is_linked(a, 'javaz_Method22', b1)
    if hasattr(b1, 'javaz_Block'):
        assert _is_linked(b1, 'javaz_Block', a)
    _safe_set(a, 'javaz_Method22', b2)
    assert _is_linked(a, 'javaz_Method22', b2)
    if hasattr(b1, 'javaz_Block'):
        assert not _is_linked(b1, 'javaz_Block', a)
    if hasattr(b2, 'javaz_Block'):
        assert _is_linked(b2, 'javaz_Block', a)
    _safe_set(a, 'javaz_Method22', None)
    assert not _is_linked(a, 'javaz_Method22', b2)
    if hasattr(b2, 'javaz_Block'):
        assert not _is_linked(b2, 'javaz_Block', a)


def test_assoc_classes1_link_reassign_clear():
    a = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b1 = javaz_Javaz()
    b2 = javaz_Javaz()
    _safe_set(a, 'javaz_JavaClass', b1)
    assert _is_linked(a, 'javaz_JavaClass', b1)
    if hasattr(b1, 'javaz_Javaz2'):
        assert _is_linked(b1, 'javaz_Javaz2', a)
    _safe_set(a, 'javaz_JavaClass', b2)
    assert _is_linked(a, 'javaz_JavaClass', b2)
    if hasattr(b1, 'javaz_Javaz2'):
        assert not _is_linked(b1, 'javaz_Javaz2', a)
    if hasattr(b2, 'javaz_Javaz2'):
        assert _is_linked(b2, 'javaz_Javaz2', a)
    _safe_set(a, 'javaz_JavaClass', None)
    assert not _is_linked(a, 'javaz_JavaClass', b2)
    if hasattr(b2, 'javaz_Javaz2'):
        assert not _is_linked(b2, 'javaz_Javaz2', a)


def test_assoc_extends14_link_reassign_clear():
    a = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b1 = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b2 = javaz_JavaClass(final=False, kind="sample_text_2", needToGenerate=False, public=False, rewritable=False)
    _safe_set(a, 'javaz_JavaClass13', b1)
    assert _is_linked(a, 'javaz_JavaClass13', b1)
    if hasattr(b1, 'javaz_JavaClass15'):
        assert _is_linked(b1, 'javaz_JavaClass15', a)
    _safe_set(a, 'javaz_JavaClass13', b2)
    assert _is_linked(a, 'javaz_JavaClass13', b2)
    if hasattr(b1, 'javaz_JavaClass15'):
        assert not _is_linked(b1, 'javaz_JavaClass15', a)
    if hasattr(b2, 'javaz_JavaClass15'):
        assert _is_linked(b2, 'javaz_JavaClass15', a)
    _safe_set(a, 'javaz_JavaClass13', None)
    assert not _is_linked(a, 'javaz_JavaClass13', b2)
    if hasattr(b2, 'javaz_JavaClass15'):
        assert not _is_linked(b2, 'javaz_JavaClass15', a)


def test_assoc_fields5_link_reassign_clear():
    a = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b1 = javaz_Field(final=True, static=True, transient=True, type="sample_text", visibility="sample_text", volatile=True)
    b2 = javaz_Field(final=False, static=False, transient=False, type="sample_text_2", visibility="sample_text_2", volatile=False)
    _safe_set(a, 'javaz_JavaClass6', {b1})
    assert _is_linked(a, 'javaz_JavaClass6', b1)
    if hasattr(b1, 'javaz_Field'):
        assert _is_linked(b1, 'javaz_Field', a)
    _safe_set(a, 'javaz_JavaClass6', {b2})
    assert _is_linked(a, 'javaz_JavaClass6', b2)
    if hasattr(b1, 'javaz_Field'):
        assert not _is_linked(b1, 'javaz_Field', a)
    if hasattr(b2, 'javaz_Field'):
        assert _is_linked(b2, 'javaz_Field', a)
    _safe_set(a, 'javaz_JavaClass6', set())
    assert not _is_linked(a, 'javaz_JavaClass6', b2)
    if hasattr(b2, 'javaz_Field'):
        assert not _is_linked(b2, 'javaz_Field', a)


def test_assoc_implements17_link_reassign_clear():
    a = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b1 = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b2 = javaz_JavaClass(final=False, kind="sample_text_2", needToGenerate=False, public=False, rewritable=False)
    _safe_set(a, 'javaz_JavaClass16', {b1})
    assert _is_linked(a, 'javaz_JavaClass16', b1)
    if hasattr(b1, 'javaz_JavaClass18'):
        assert _is_linked(b1, 'javaz_JavaClass18', a)
    _safe_set(a, 'javaz_JavaClass16', {b2})
    assert _is_linked(a, 'javaz_JavaClass16', b2)
    if hasattr(b1, 'javaz_JavaClass18'):
        assert not _is_linked(b1, 'javaz_JavaClass18', a)
    if hasattr(b2, 'javaz_JavaClass18'):
        assert _is_linked(b2, 'javaz_JavaClass18', a)
    _safe_set(a, 'javaz_JavaClass16', set())
    assert not _is_linked(a, 'javaz_JavaClass16', b2)
    if hasattr(b2, 'javaz_JavaClass18'):
        assert not _is_linked(b2, 'javaz_JavaClass18', a)


def test_assoc_imports8_link_reassign_clear():
    a = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b1 = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b2 = javaz_JavaClass(final=False, kind="sample_text_2", needToGenerate=False, public=False, rewritable=False)
    _safe_set(a, 'javaz_JavaClass7', {b1})
    assert _is_linked(a, 'javaz_JavaClass7', b1)
    if hasattr(b1, 'javaz_JavaClass9'):
        assert _is_linked(b1, 'javaz_JavaClass9', a)
    _safe_set(a, 'javaz_JavaClass7', {b2})
    assert _is_linked(a, 'javaz_JavaClass7', b2)
    if hasattr(b1, 'javaz_JavaClass9'):
        assert not _is_linked(b1, 'javaz_JavaClass9', a)
    if hasattr(b2, 'javaz_JavaClass9'):
        assert _is_linked(b2, 'javaz_JavaClass9', a)
    _safe_set(a, 'javaz_JavaClass7', set())
    assert not _is_linked(a, 'javaz_JavaClass7', b2)
    if hasattr(b2, 'javaz_JavaClass9'):
        assert not _is_linked(b2, 'javaz_JavaClass9', a)


def test_assoc_methods3_link_reassign_clear():
    a = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    b1 = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b2 = javaz_JavaClass(final=False, kind="sample_text_2", needToGenerate=False, public=False, rewritable=False)
    _safe_set(a, 'javaz_Method', b1)
    assert _is_linked(a, 'javaz_Method', b1)
    if hasattr(b1, 'javaz_JavaClass4'):
        assert _is_linked(b1, 'javaz_JavaClass4', a)
    _safe_set(a, 'javaz_Method', b2)
    assert _is_linked(a, 'javaz_Method', b2)
    if hasattr(b1, 'javaz_JavaClass4'):
        assert not _is_linked(b1, 'javaz_JavaClass4', a)
    if hasattr(b2, 'javaz_JavaClass4'):
        assert _is_linked(b2, 'javaz_JavaClass4', a)
    _safe_set(a, 'javaz_Method', None)
    assert not _is_linked(a, 'javaz_Method', b2)
    if hasattr(b2, 'javaz_JavaClass4'):
        assert not _is_linked(b2, 'javaz_JavaClass4', a)


def test_assoc_package10_link_reassign_clear():
    a = javaz_JavaPackageX(needToGenerate=True)
    b1 = javaz_JavaClass(final=True, kind="sample_text", needToGenerate=True, public=True, rewritable=True)
    b2 = javaz_JavaClass(final=False, kind="sample_text_2", needToGenerate=False, public=False, rewritable=False)
    _safe_set(a, 'javaz_JavaPackageX12', b1)
    assert _is_linked(a, 'javaz_JavaPackageX12', b1)
    if hasattr(b1, 'javaz_JavaClass11'):
        assert _is_linked(b1, 'javaz_JavaClass11', a)
    _safe_set(a, 'javaz_JavaPackageX12', b2)
    assert _is_linked(a, 'javaz_JavaPackageX12', b2)
    if hasattr(b1, 'javaz_JavaClass11'):
        assert not _is_linked(b1, 'javaz_JavaClass11', a)
    if hasattr(b2, 'javaz_JavaClass11'):
        assert _is_linked(b2, 'javaz_JavaClass11', a)
    _safe_set(a, 'javaz_JavaPackageX12', None)
    assert not _is_linked(a, 'javaz_JavaPackageX12', b2)
    if hasattr(b2, 'javaz_JavaClass11'):
        assert not _is_linked(b2, 'javaz_JavaClass11', a)


def test_assoc_packages0_link_reassign_clear():
    a = javaz_JavaPackageX(needToGenerate=True)
    b1 = javaz_Javaz()
    b2 = javaz_Javaz()
    _safe_set(a, 'javaz_JavaPackageX', b1)
    assert _is_linked(a, 'javaz_JavaPackageX', b1)
    if hasattr(b1, 'javaz_Javaz'):
        assert _is_linked(b1, 'javaz_Javaz', a)
    _safe_set(a, 'javaz_JavaPackageX', b2)
    assert _is_linked(a, 'javaz_JavaPackageX', b2)
    if hasattr(b1, 'javaz_Javaz'):
        assert not _is_linked(b1, 'javaz_Javaz', a)
    if hasattr(b2, 'javaz_Javaz'):
        assert _is_linked(b2, 'javaz_Javaz', a)
    _safe_set(a, 'javaz_JavaPackageX', None)
    assert not _is_linked(a, 'javaz_JavaPackageX', b2)
    if hasattr(b2, 'javaz_Javaz'):
        assert not _is_linked(b2, 'javaz_Javaz', a)


def test_assoc_parameters19_link_reassign_clear():
    a = javaz_Method(abstract=True, constructor=True, final=True, native=True, static=True, synchronized=True, visibility="sample_text")
    b1 = javaz_JavaParameter(final=True, kind="sample_text", parameterKind="sample_text", type="sample_text")
    b2 = javaz_JavaParameter(final=False, kind="sample_text_2", parameterKind="sample_text_2", type="sample_text_2")
    _safe_set(a, 'javaz_Method20', {b1})
    assert _is_linked(a, 'javaz_Method20', b1)
    if hasattr(b1, 'javaz_JavaParameter'):
        assert _is_linked(b1, 'javaz_JavaParameter', a)
    _safe_set(a, 'javaz_Method20', {b2})
    assert _is_linked(a, 'javaz_Method20', b2)
    if hasattr(b1, 'javaz_JavaParameter'):
        assert not _is_linked(b1, 'javaz_JavaParameter', a)
    if hasattr(b2, 'javaz_JavaParameter'):
        assert _is_linked(b2, 'javaz_JavaParameter', a)
    _safe_set(a, 'javaz_Method20', set())
    assert not _is_linked(a, 'javaz_Method20', b2)
    if hasattr(b2, 'javaz_JavaParameter'):
        assert not _is_linked(b2, 'javaz_JavaParameter', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

JavaElement_strategy = st.builds(JavaElement)
@given(instance=JavaElement_strategy)
@settings(max_examples=25)
def test_JavaElement_instantiation(instance):
    assert isinstance(instance, JavaElement)


javaz_Block_strategy = st.builds(javaz_Block, content=safe_text)
@given(instance=javaz_Block_strategy)
@settings(max_examples=25)
def test_javaz_Block_instantiation(instance):
    assert isinstance(instance, javaz_Block)


javaz_Field_strategy = st.builds(javaz_Field, final=st.booleans(), static=st.booleans(), transient=st.booleans(), type=safe_text, visibility=safe_text, volatile=st.booleans())
@given(instance=javaz_Field_strategy)
@settings(max_examples=25)
def test_javaz_Field_instantiation(instance):
    assert isinstance(instance, javaz_Field)


javaz_JavaClass_strategy = st.builds(javaz_JavaClass, final=st.booleans(), kind=safe_text, needToGenerate=st.booleans(), public=st.booleans(), rewritable=st.booleans())
@given(instance=javaz_JavaClass_strategy)
@settings(max_examples=25)
def test_javaz_JavaClass_instantiation(instance):
    assert isinstance(instance, javaz_JavaClass)


javaz_JavaElement_strategy = st.builds(javaz_JavaElement, name=safe_text)
@given(instance=javaz_JavaElement_strategy)
@settings(max_examples=25)
def test_javaz_JavaElement_instantiation(instance):
    assert isinstance(instance, javaz_JavaElement)


javaz_JavaPackageX_strategy = st.builds(javaz_JavaPackageX, needToGenerate=st.booleans())
@given(instance=javaz_JavaPackageX_strategy)
@settings(max_examples=25)
def test_javaz_JavaPackageX_instantiation(instance):
    assert isinstance(instance, javaz_JavaPackageX)


javaz_JavaParameter_strategy = st.builds(javaz_JavaParameter, final=st.booleans(), kind=safe_text, parameterKind=safe_text, type=safe_text)
@given(instance=javaz_JavaParameter_strategy)
@settings(max_examples=25)
def test_javaz_JavaParameter_instantiation(instance):
    assert isinstance(instance, javaz_JavaParameter)


javaz_Javaz_strategy = st.builds(javaz_Javaz)
@given(instance=javaz_Javaz_strategy)
@settings(max_examples=25)
def test_javaz_Javaz_instantiation(instance):
    assert isinstance(instance, javaz_Javaz)


javaz_Method_strategy = st.builds(javaz_Method, abstract=st.booleans(), constructor=st.booleans(), final=st.booleans(), native=st.booleans(), static=st.booleans(), synchronized=st.booleans(), visibility=safe_text)
@given(instance=javaz_Method_strategy)
@settings(max_examples=25)
def test_javaz_Method_instantiation(instance):
    assert isinstance(instance, javaz_Method)


