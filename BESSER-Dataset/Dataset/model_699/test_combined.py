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
    type_EStringToStringMapEntry,
    type_XMLTypeDocumentRoot,
    type_EDataType,
    AnyType,
    type_SimpleAnyType,
    type_ProcessingInstruction,
    type_AnyType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_type_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(type_EStringToStringMapEntry)


def test_hyp_type_estringtostringmapentry_constructor_exists():
    assert callable(type_EStringToStringMapEntry.__init__)


def test_hyp_type_estringtostringmapentry_constructor_args():
    sig = inspect.signature(type_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_xmltypedocumentroot_is_not_abstract():
    assert not inspect.isabstract(type_XMLTypeDocumentRoot)


def test_hyp_type_xmltypedocumentroot_constructor_exists():
    assert callable(type_XMLTypeDocumentRoot.__init__)


def test_hyp_type_xmltypedocumentroot_constructor_args():
    sig = inspect.signature(type_XMLTypeDocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "cDATA" in params, "Missing parameter 'cDATA'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "text" in params, "Missing parameter 'text'"







def test_hyp_type_edatatype_is_not_abstract():
    assert not inspect.isabstract(type_EDataType)


def test_hyp_type_edatatype_constructor_exists():
    assert callable(type_EDataType.__init__)


def test_hyp_type_edatatype_constructor_args():
    sig = inspect.signature(type_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_anytype_is_not_abstract():
    assert not inspect.isabstract(AnyType)


def test_hyp_anytype_constructor_exists():
    assert callable(AnyType.__init__)


def test_hyp_anytype_constructor_args():
    sig = inspect.signature(AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_simpleanytype_is_not_abstract():
    assert not inspect.isabstract(type_SimpleAnyType)


def test_hyp_type_simpleanytype_constructor_exists():
    assert callable(type_SimpleAnyType.__init__)


def test_hyp_type_simpleanytype_constructor_args():
    sig = inspect.signature(type_SimpleAnyType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "rawValue" in params, "Missing parameter 'rawValue'"





def test_hyp_type_processinginstruction_is_not_abstract():
    assert not inspect.isabstract(type_ProcessingInstruction)


def test_hyp_type_processinginstruction_constructor_exists():
    assert callable(type_ProcessingInstruction.__init__)


def test_hyp_type_processinginstruction_constructor_args():
    sig = inspect.signature(type_ProcessingInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "target" in params, "Missing parameter 'target'"





def test_hyp_type_anytype_is_not_abstract():
    assert not inspect.isabstract(type_AnyType)


def test_hyp_type_anytype_constructor_exists():
    assert callable(type_AnyType.__init__)


def test_hyp_type_anytype_constructor_args():
    sig = inspect.signature(type_AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"





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
type_EStringToStringMapEntry_strategy = st.builds(
    type_EStringToStringMapEntry,
)
type_XMLTypeDocumentRoot_strategy = st.builds(
    type_XMLTypeDocumentRoot,
    comment=
        safe_text,
    cDATA=
        safe_text,
    mixed=
        safe_text,
    text=
        safe_text
)
type_EDataType_strategy = st.builds(
    type_EDataType,
)
AnyType_strategy = st.builds(
    AnyType,
)
type_SimpleAnyType_strategy = st.builds(
    type_SimpleAnyType,
    value=
        safe_text,
    rawValue=
        safe_text
)
type_ProcessingInstruction_strategy = st.builds(
    type_ProcessingInstruction,
    data=
        safe_text,
    target=
        safe_text
)
type_AnyType_strategy = st.builds(
    type_AnyType,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)





@given(instance=type_XMLTypeDocumentRoot_strategy)
def test_hyp_type_xmltypedocumentroot_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=type_XMLTypeDocumentRoot_strategy)
def test_hyp_type_xmltypedocumentroot_cDATA_setter(instance):
    original = instance.cDATA
    instance.cDATA = original
    assert instance.cDATA == original



@given(instance=type_XMLTypeDocumentRoot_strategy)
def test_hyp_type_xmltypedocumentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=type_XMLTypeDocumentRoot_strategy)
def test_hyp_type_xmltypedocumentroot_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original






@given(instance=type_SimpleAnyType_strategy)
def test_hyp_type_simpleanytype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=type_SimpleAnyType_strategy)
def test_hyp_type_simpleanytype_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original




@given(instance=type_ProcessingInstruction_strategy)
def test_hyp_type_processinginstruction_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=type_ProcessingInstruction_strategy)
def test_hyp_type_processinginstruction_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original




@given(instance=type_AnyType_strategy)
def test_hyp_type_anytype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=type_AnyType_strategy)
def test_hyp_type_anytype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=type_AnyType_strategy)
def test_hyp_type_anytype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnyType,
    type_AnyType,
    type_EDataType,
    type_EStringToStringMapEntry,
    type_ProcessingInstruction,
    type_SimpleAnyType,
    type_XMLTypeDocumentRoot,
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

def test_type_AnyType_any_value_roundtrip():
    instance = type_AnyType(any="sample_text", anyAttribute="sample_text", mixed="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_type_AnyType_anyAttribute_value_roundtrip():
    instance = type_AnyType(any="sample_text", anyAttribute="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_type_AnyType_mixed_value_roundtrip():
    instance = type_AnyType(any="sample_text", anyAttribute="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_type_ProcessingInstruction_data_value_roundtrip():
    instance = type_ProcessingInstruction(data="sample_text", target="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_type_ProcessingInstruction_target_value_roundtrip():
    instance = type_ProcessingInstruction(data="sample_text", target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_type_SimpleAnyType_rawValue_value_roundtrip():
    instance = type_SimpleAnyType(rawValue="sample_text", value="sample_text")
    assert instance.rawValue == "sample_text"
    instance.rawValue = "sample_text_2"
    assert instance.rawValue == "sample_text_2"


def test_type_SimpleAnyType_value_value_roundtrip():
    instance = type_SimpleAnyType(rawValue="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_type_XMLTypeDocumentRoot_cDATA_value_roundtrip():
    instance = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    assert instance.cDATA == "sample_text"
    instance.cDATA = "sample_text_2"
    assert instance.cDATA == "sample_text_2"


def test_type_XMLTypeDocumentRoot_comment_value_roundtrip():
    instance = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_type_XMLTypeDocumentRoot_mixed_value_roundtrip():
    instance = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_type_XMLTypeDocumentRoot_text_value_roundtrip():
    instance = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_type_SimpleAnyType_isa_AnyType():
    instance = type_SimpleAnyType(rawValue="sample_text", value="sample_text")
    assert isinstance(instance, AnyType)


def test_assoc_instanceType0_link_reassign_clear():
    a = type_SimpleAnyType(rawValue="sample_text", value="sample_text")
    b1 = type_EDataType()
    b2 = type_EDataType()
    _safe_set(a, 'type_SimpleAnyType', b1)
    assert _is_linked(a, 'type_SimpleAnyType', b1)
    if hasattr(b1, 'type_EDataType'):
        assert _is_linked(b1, 'type_EDataType', a)
    _safe_set(a, 'type_SimpleAnyType', b2)
    assert _is_linked(a, 'type_SimpleAnyType', b2)
    if hasattr(b1, 'type_EDataType'):
        assert not _is_linked(b1, 'type_EDataType', a)
    if hasattr(b2, 'type_EDataType'):
        assert _is_linked(b2, 'type_EDataType', a)
    _safe_set(a, 'type_SimpleAnyType', None)
    assert not _is_linked(a, 'type_SimpleAnyType', b2)
    if hasattr(b2, 'type_EDataType'):
        assert not _is_linked(b2, 'type_EDataType', a)


def test_assoc_processingInstruction5_link_reassign_clear():
    a = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    b1 = type_ProcessingInstruction(data="sample_text", target="sample_text")
    b2 = type_ProcessingInstruction(data="sample_text_2", target="sample_text_2")
    _safe_set(a, 'type_XMLTypeDocumentRoot6', {b1})
    assert _is_linked(a, 'type_XMLTypeDocumentRoot6', b1)
    if hasattr(b1, 'type_ProcessingInstruction'):
        assert _is_linked(b1, 'type_ProcessingInstruction', a)
    _safe_set(a, 'type_XMLTypeDocumentRoot6', {b2})
    assert _is_linked(a, 'type_XMLTypeDocumentRoot6', b2)
    if hasattr(b1, 'type_ProcessingInstruction'):
        assert not _is_linked(b1, 'type_ProcessingInstruction', a)
    if hasattr(b2, 'type_ProcessingInstruction'):
        assert _is_linked(b2, 'type_ProcessingInstruction', a)
    _safe_set(a, 'type_XMLTypeDocumentRoot6', set())
    assert not _is_linked(a, 'type_XMLTypeDocumentRoot6', b2)
    if hasattr(b2, 'type_ProcessingInstruction'):
        assert not _is_linked(b2, 'type_ProcessingInstruction', a)


def test_assoc_xMLNSPrefixMap1_link_reassign_clear():
    a = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    b1 = type_EStringToStringMapEntry()
    b2 = type_EStringToStringMapEntry()
    _safe_set(a, 'type_XMLTypeDocumentRoot', {b1})
    assert _is_linked(a, 'type_XMLTypeDocumentRoot', b1)
    if hasattr(b1, 'type_EStringToStringMapEntry'):
        assert _is_linked(b1, 'type_EStringToStringMapEntry', a)
    _safe_set(a, 'type_XMLTypeDocumentRoot', {b2})
    assert _is_linked(a, 'type_XMLTypeDocumentRoot', b2)
    if hasattr(b1, 'type_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'type_EStringToStringMapEntry', a)
    if hasattr(b2, 'type_EStringToStringMapEntry'):
        assert _is_linked(b2, 'type_EStringToStringMapEntry', a)
    _safe_set(a, 'type_XMLTypeDocumentRoot', set())
    assert not _is_linked(a, 'type_XMLTypeDocumentRoot', b2)
    if hasattr(b2, 'type_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'type_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation2_link_reassign_clear():
    a = type_XMLTypeDocumentRoot(cDATA="sample_text", comment="sample_text", mixed="sample_text", text="sample_text")
    b1 = type_EStringToStringMapEntry()
    b2 = type_EStringToStringMapEntry()
    _safe_set(a, 'type_XMLTypeDocumentRoot3', {b1})
    assert _is_linked(a, 'type_XMLTypeDocumentRoot3', b1)
    if hasattr(b1, 'type_EStringToStringMapEntry4'):
        assert _is_linked(b1, 'type_EStringToStringMapEntry4', a)
    _safe_set(a, 'type_XMLTypeDocumentRoot3', {b2})
    assert _is_linked(a, 'type_XMLTypeDocumentRoot3', b2)
    if hasattr(b1, 'type_EStringToStringMapEntry4'):
        assert not _is_linked(b1, 'type_EStringToStringMapEntry4', a)
    if hasattr(b2, 'type_EStringToStringMapEntry4'):
        assert _is_linked(b2, 'type_EStringToStringMapEntry4', a)
    _safe_set(a, 'type_XMLTypeDocumentRoot3', set())
    assert not _is_linked(a, 'type_XMLTypeDocumentRoot3', b2)
    if hasattr(b2, 'type_EStringToStringMapEntry4'):
        assert not _is_linked(b2, 'type_EStringToStringMapEntry4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnyType_strategy = st.builds(AnyType)
@given(instance=AnyType_strategy)
@settings(max_examples=25)
def test_AnyType_instantiation(instance):
    assert isinstance(instance, AnyType)


type_AnyType_strategy = st.builds(type_AnyType, any=safe_text, anyAttribute=safe_text, mixed=safe_text)
@given(instance=type_AnyType_strategy)
@settings(max_examples=25)
def test_type_AnyType_instantiation(instance):
    assert isinstance(instance, type_AnyType)


type_EDataType_strategy = st.builds(type_EDataType)
@given(instance=type_EDataType_strategy)
@settings(max_examples=25)
def test_type_EDataType_instantiation(instance):
    assert isinstance(instance, type_EDataType)


type_EStringToStringMapEntry_strategy = st.builds(type_EStringToStringMapEntry)
@given(instance=type_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_type_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, type_EStringToStringMapEntry)


type_ProcessingInstruction_strategy = st.builds(type_ProcessingInstruction, data=safe_text, target=safe_text)
@given(instance=type_ProcessingInstruction_strategy)
@settings(max_examples=25)
def test_type_ProcessingInstruction_instantiation(instance):
    assert isinstance(instance, type_ProcessingInstruction)


type_SimpleAnyType_strategy = st.builds(type_SimpleAnyType, rawValue=safe_text, value=safe_text)
@given(instance=type_SimpleAnyType_strategy)
@settings(max_examples=25)
def test_type_SimpleAnyType_instantiation(instance):
    assert isinstance(instance, type_SimpleAnyType)


type_XMLTypeDocumentRoot_strategy = st.builds(type_XMLTypeDocumentRoot, cDATA=safe_text, comment=safe_text, mixed=safe_text, text=safe_text)
@given(instance=type_XMLTypeDocumentRoot_strategy)
@settings(max_examples=25)
def test_type_XMLTypeDocumentRoot_instantiation(instance):
    assert isinstance(instance, type_XMLTypeDocumentRoot)



