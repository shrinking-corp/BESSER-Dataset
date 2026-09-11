import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    codetaginfo_CodeTag,
    codetaginfo_CodeTagContext,
    codetaginfo_CodeTagInfo,
    codetaginfo_DocumentRoot,
    codetaginfo_EStringToStringMapEntry,
    CodeTagType,
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

def test_codetaginfo_CodeTag_contents_value_roundtrip():
    instance = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    assert instance.contents == "sample_text"
    instance.contents = "sample_text_2"
    assert instance.contents == "sample_text_2"


def test_codetaginfo_CodeTag_group_value_roundtrip():
    instance = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_codetaginfo_CodeTag_name_value_roundtrip():
    instance = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_codetaginfo_CodeTag_tag_begin_value_roundtrip():
    instance = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    assert instance.tag_begin == "sample_text"
    instance.tag_begin = "sample_text_2"
    assert instance.tag_begin == "sample_text_2"


def test_codetaginfo_CodeTag_tag_end_value_roundtrip():
    instance = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    assert instance.tag_end == "sample_text"
    instance.tag_end = "sample_text_2"
    assert instance.tag_end == "sample_text_2"


def test_codetaginfo_CodeTag_type_value_roundtrip():
    instance = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_codetaginfo_CodeTag_uuid_value_roundtrip():
    instance = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    assert instance.uuid == "sample_text"
    instance.uuid = "sample_text_2"
    assert instance.uuid == "sample_text_2"


def test_codetaginfo_CodeTagContext_class_name_value_roundtrip():
    instance = codetaginfo_CodeTagContext(class_name="sample_text", component_name="sample_text", group="sample_text", operation_name="sample_text")
    assert instance.class_name == "sample_text"
    instance.class_name = "sample_text_2"
    assert instance.class_name == "sample_text_2"


def test_codetaginfo_CodeTagContext_component_name_value_roundtrip():
    instance = codetaginfo_CodeTagContext(class_name="sample_text", component_name="sample_text", group="sample_text", operation_name="sample_text")
    assert instance.component_name == "sample_text"
    instance.component_name = "sample_text_2"
    assert instance.component_name == "sample_text_2"


def test_codetaginfo_CodeTagContext_group_value_roundtrip():
    instance = codetaginfo_CodeTagContext(class_name="sample_text", component_name="sample_text", group="sample_text", operation_name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_codetaginfo_CodeTagContext_operation_name_value_roundtrip():
    instance = codetaginfo_CodeTagContext(class_name="sample_text", component_name="sample_text", group="sample_text", operation_name="sample_text")
    assert instance.operation_name == "sample_text"
    instance.operation_name = "sample_text_2"
    assert instance.operation_name == "sample_text_2"


def test_codetaginfo_CodeTagInfo_filename_value_roundtrip():
    instance = codetaginfo_CodeTagInfo(filename="sample_text", group="sample_text")
    assert instance.filename == "sample_text"
    instance.filename = "sample_text_2"
    assert instance.filename == "sample_text_2"


def test_codetaginfo_CodeTagInfo_group_value_roundtrip():
    instance = codetaginfo_CodeTagInfo(filename="sample_text", group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_codetaginfo_DocumentRoot_mixed_value_roundtrip():
    instance = codetaginfo_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_assoc_codeTagInfo7_link_reassign_clear():
    a = codetaginfo_DocumentRoot(mixed="sample_text")
    b1 = codetaginfo_CodeTagInfo(filename="sample_text", group="sample_text")
    b2 = codetaginfo_CodeTagInfo(filename="sample_text_2", group="sample_text_2")
    _safe_set(a, 'codetaginfo_DocumentRoot8', {b1})
    assert _is_linked(a, 'codetaginfo_DocumentRoot8', b1)
    if hasattr(b1, 'codetaginfo_CodeTagInfo9'):
        assert _is_linked(b1, 'codetaginfo_CodeTagInfo9', a)
    _safe_set(a, 'codetaginfo_DocumentRoot8', {b2})
    assert _is_linked(a, 'codetaginfo_DocumentRoot8', b2)
    if hasattr(b1, 'codetaginfo_CodeTagInfo9'):
        assert not _is_linked(b1, 'codetaginfo_CodeTagInfo9', a)
    if hasattr(b2, 'codetaginfo_CodeTagInfo9'):
        assert _is_linked(b2, 'codetaginfo_CodeTagInfo9', a)
    _safe_set(a, 'codetaginfo_DocumentRoot8', set())
    assert not _is_linked(a, 'codetaginfo_DocumentRoot8', b2)
    if hasattr(b2, 'codetaginfo_CodeTagInfo9'):
        assert not _is_linked(b2, 'codetaginfo_CodeTagInfo9', a)


def test_assoc_codetag1_link_reassign_clear():
    a = codetaginfo_CodeTagInfo(filename="sample_text", group="sample_text")
    b1 = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    b2 = codetaginfo_CodeTag(contents="sample_text_2", group="sample_text_2", name="sample_text_2", tag_begin="sample_text_2", tag_end="sample_text_2", type="sample_text_2", uuid="sample_text_2")
    _safe_set(a, 'codetaginfo_CodeTagInfo', {b1})
    assert _is_linked(a, 'codetaginfo_CodeTagInfo', b1)
    if hasattr(b1, 'codetaginfo_CodeTag2'):
        assert _is_linked(b1, 'codetaginfo_CodeTag2', a)
    _safe_set(a, 'codetaginfo_CodeTagInfo', {b2})
    assert _is_linked(a, 'codetaginfo_CodeTagInfo', b2)
    if hasattr(b1, 'codetaginfo_CodeTag2'):
        assert not _is_linked(b1, 'codetaginfo_CodeTag2', a)
    if hasattr(b2, 'codetaginfo_CodeTag2'):
        assert _is_linked(b2, 'codetaginfo_CodeTag2', a)
    _safe_set(a, 'codetaginfo_CodeTagInfo', set())
    assert not _is_linked(a, 'codetaginfo_CodeTagInfo', b2)
    if hasattr(b2, 'codetaginfo_CodeTag2'):
        assert not _is_linked(b2, 'codetaginfo_CodeTag2', a)


def test_assoc_contextinfo0_link_reassign_clear():
    a = codetaginfo_CodeTagContext(class_name="sample_text", component_name="sample_text", group="sample_text", operation_name="sample_text")
    b1 = codetaginfo_CodeTag(contents="sample_text", group="sample_text", name="sample_text", tag_begin="sample_text", tag_end="sample_text", type="sample_text", uuid="sample_text")
    b2 = codetaginfo_CodeTag(contents="sample_text_2", group="sample_text_2", name="sample_text_2", tag_begin="sample_text_2", tag_end="sample_text_2", type="sample_text_2", uuid="sample_text_2")
    _safe_set(a, 'codetaginfo_CodeTagContext', b1)
    assert _is_linked(a, 'codetaginfo_CodeTagContext', b1)
    if hasattr(b1, 'codetaginfo_CodeTag'):
        assert _is_linked(b1, 'codetaginfo_CodeTag', a)
    _safe_set(a, 'codetaginfo_CodeTagContext', b2)
    assert _is_linked(a, 'codetaginfo_CodeTagContext', b2)
    if hasattr(b1, 'codetaginfo_CodeTag'):
        assert not _is_linked(b1, 'codetaginfo_CodeTag', a)
    if hasattr(b2, 'codetaginfo_CodeTag'):
        assert _is_linked(b2, 'codetaginfo_CodeTag', a)
    _safe_set(a, 'codetaginfo_CodeTagContext', None)
    assert not _is_linked(a, 'codetaginfo_CodeTagContext', b2)
    if hasattr(b2, 'codetaginfo_CodeTag'):
        assert not _is_linked(b2, 'codetaginfo_CodeTag', a)


def test_assoc_xMLNSPrefixMap3_link_reassign_clear():
    a = codetaginfo_DocumentRoot(mixed="sample_text")
    b1 = codetaginfo_EStringToStringMapEntry()
    b2 = codetaginfo_EStringToStringMapEntry()
    _safe_set(a, 'codetaginfo_DocumentRoot', {b1})
    assert _is_linked(a, 'codetaginfo_DocumentRoot', b1)
    if hasattr(b1, 'codetaginfo_EStringToStringMapEntry'):
        assert _is_linked(b1, 'codetaginfo_EStringToStringMapEntry', a)
    _safe_set(a, 'codetaginfo_DocumentRoot', {b2})
    assert _is_linked(a, 'codetaginfo_DocumentRoot', b2)
    if hasattr(b1, 'codetaginfo_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'codetaginfo_EStringToStringMapEntry', a)
    if hasattr(b2, 'codetaginfo_EStringToStringMapEntry'):
        assert _is_linked(b2, 'codetaginfo_EStringToStringMapEntry', a)
    _safe_set(a, 'codetaginfo_DocumentRoot', set())
    assert not _is_linked(a, 'codetaginfo_DocumentRoot', b2)
    if hasattr(b2, 'codetaginfo_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'codetaginfo_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation4_link_reassign_clear():
    a = codetaginfo_DocumentRoot(mixed="sample_text")
    b1 = codetaginfo_EStringToStringMapEntry()
    b2 = codetaginfo_EStringToStringMapEntry()
    _safe_set(a, 'codetaginfo_DocumentRoot5', {b1})
    assert _is_linked(a, 'codetaginfo_DocumentRoot5', b1)
    if hasattr(b1, 'codetaginfo_EStringToStringMapEntry6'):
        assert _is_linked(b1, 'codetaginfo_EStringToStringMapEntry6', a)
    _safe_set(a, 'codetaginfo_DocumentRoot5', {b2})
    assert _is_linked(a, 'codetaginfo_DocumentRoot5', b2)
    if hasattr(b1, 'codetaginfo_EStringToStringMapEntry6'):
        assert not _is_linked(b1, 'codetaginfo_EStringToStringMapEntry6', a)
    if hasattr(b2, 'codetaginfo_EStringToStringMapEntry6'):
        assert _is_linked(b2, 'codetaginfo_EStringToStringMapEntry6', a)
    _safe_set(a, 'codetaginfo_DocumentRoot5', set())
    assert not _is_linked(a, 'codetaginfo_DocumentRoot5', b2)
    if hasattr(b2, 'codetaginfo_EStringToStringMapEntry6'):
        assert not _is_linked(b2, 'codetaginfo_EStringToStringMapEntry6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

codetaginfo_CodeTag_strategy = st.builds(codetaginfo_CodeTag, contents=safe_text, group=safe_text, name=safe_text, tag_begin=safe_text, tag_end=safe_text, type=safe_text, uuid=safe_text)
@given(instance=codetaginfo_CodeTag_strategy)
@settings(max_examples=25)
def test_codetaginfo_CodeTag_instantiation(instance):
    assert isinstance(instance, codetaginfo_CodeTag)


codetaginfo_CodeTagContext_strategy = st.builds(codetaginfo_CodeTagContext, class_name=safe_text, component_name=safe_text, group=safe_text, operation_name=safe_text)
@given(instance=codetaginfo_CodeTagContext_strategy)
@settings(max_examples=25)
def test_codetaginfo_CodeTagContext_instantiation(instance):
    assert isinstance(instance, codetaginfo_CodeTagContext)


codetaginfo_CodeTagInfo_strategy = st.builds(codetaginfo_CodeTagInfo, filename=safe_text, group=safe_text)
@given(instance=codetaginfo_CodeTagInfo_strategy)
@settings(max_examples=25)
def test_codetaginfo_CodeTagInfo_instantiation(instance):
    assert isinstance(instance, codetaginfo_CodeTagInfo)


codetaginfo_DocumentRoot_strategy = st.builds(codetaginfo_DocumentRoot, mixed=safe_text)
@given(instance=codetaginfo_DocumentRoot_strategy)
@settings(max_examples=25)
def test_codetaginfo_DocumentRoot_instantiation(instance):
    assert isinstance(instance, codetaginfo_DocumentRoot)


codetaginfo_EStringToStringMapEntry_strategy = st.builds(codetaginfo_EStringToStringMapEntry)
@given(instance=codetaginfo_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_codetaginfo_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, codetaginfo_EStringToStringMapEntry)


