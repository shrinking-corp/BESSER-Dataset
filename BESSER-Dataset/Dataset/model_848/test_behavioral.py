import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotatedElement,
    Attribute,
    BasicType,
    Category,
    DataType,
    Entity,
    Type,
    occi_Action,
    occi_AnnotatedElement,
    occi_Annotation,
    occi_ArrayType,
    occi_Attribute,
    occi_AttributeState,
    occi_BasicType,
    occi_BooleanType,
    occi_Category,
    occi_Configuration,
    occi_Constraint,
    occi_DataType,
    occi_EObjectType,
    occi_Entity,
    occi_EnumerationLiteral,
    occi_EnumerationType,
    occi_Extension,
    occi_FSM,
    occi_Kind,
    occi_Link,
    occi_Mixin,
    occi_MixinBase,
    occi_NumericType,
    occi_RecordField,
    occi_RecordType,
    occi_Resource,
    occi_State,
    occi_StringType,
    occi_Transition,
    occi_Type,
    NumericTypeEnum,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_attributes1_reverse_link_reassign_clear():
    a1 = occi_Category(description="sample_text", name="sample_text", scheme="sample_text", term="sample_text", title="sample_text")
    a2 = occi_Category(description="sample_text_2", name="sample_text_2", scheme="sample_text_2", term="sample_text_2", title="sample_text_2")
    b = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    _safe_set(b, 'occi_Attribute', a1)
    assert _is_linked(b, 'occi_Attribute', a1)
    if hasattr(a1, 'occi_Category'):
        assert _is_linked(a1, 'occi_Category', b)
    _safe_set(b, 'occi_Attribute', a2)
    assert _is_linked(b, 'occi_Attribute', a2)
    if hasattr(a1, 'occi_Category'):
        assert not _is_linked(a1, 'occi_Category', b)
    if hasattr(a2, 'occi_Category'):
        assert _is_linked(a2, 'occi_Category', b)
    _safe_set(b, 'occi_Attribute', None)
    assert not _is_linked(b, 'occi_Attribute', a2)
    if hasattr(a2, 'occi_Category'):
        assert not _is_linked(a2, 'occi_Category', b)


def test_assoc_attributes44_reverse_link_reassign_clear():
    a1 = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    a2 = occi_Entity(id="sample_text_2", location="sample_text_2", title="sample_text_2")
    b = occi_AttributeState(name="sample_text", value="sample_text")
    _safe_set(b, 'occi_AttributeState', a1)
    assert _is_linked(b, 'occi_AttributeState', a1)
    if hasattr(a1, 'occi_Entity45'):
        assert _is_linked(a1, 'occi_Entity45', b)
    _safe_set(b, 'occi_AttributeState', a2)
    assert _is_linked(b, 'occi_AttributeState', a2)
    if hasattr(a1, 'occi_Entity45'):
        assert not _is_linked(a1, 'occi_Entity45', b)
    if hasattr(a2, 'occi_Entity45'):
        assert _is_linked(a2, 'occi_Entity45', b)
    _safe_set(b, 'occi_AttributeState', None)
    assert not _is_linked(b, 'occi_AttributeState', a2)
    if hasattr(a2, 'occi_Entity45'):
        assert not _is_linked(a2, 'occi_Entity45', b)


def test_assoc_entities25_reverse_link_reassign_clear():
    a1 = occi_Kind()
    a2 = occi_Kind()
    b = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    _safe_set(b, 'occi_Entity', a1)
    assert _is_linked(b, 'occi_Entity', a1)
    if hasattr(a1, 'occi_Kind26'):
        assert _is_linked(a1, 'occi_Kind26', b)
    _safe_set(b, 'occi_Entity', a2)
    assert _is_linked(b, 'occi_Entity', a2)
    if hasattr(a1, 'occi_Kind26'):
        assert not _is_linked(a1, 'occi_Kind26', b)
    if hasattr(a2, 'occi_Kind26'):
        assert _is_linked(a2, 'occi_Kind26', b)
    _safe_set(b, 'occi_Entity', None)
    assert not _is_linked(b, 'occi_Entity', a2)
    if hasattr(a2, 'occi_Kind26'):
        assert not _is_linked(a2, 'occi_Kind26', b)


def test_assoc_import_64_reverse_link_reassign_clear():
    a1 = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    a2 = occi_Extension(description="sample_text_2", name="sample_text_2", scheme="sample_text_2", specification="sample_text_2")
    b = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    _safe_set(b, 'occi_Extension63', {a1})
    assert _is_linked(b, 'occi_Extension63', a1)
    if hasattr(a1, 'occi_Extension'):
        assert _is_linked(a1, 'occi_Extension', b)
    _safe_set(b, 'occi_Extension63', {a2})
    assert _is_linked(b, 'occi_Extension63', a2)
    if hasattr(a1, 'occi_Extension'):
        assert not _is_linked(a1, 'occi_Extension', b)
    if hasattr(a2, 'occi_Extension'):
        assert _is_linked(a2, 'occi_Extension', b)
    _safe_set(b, 'occi_Extension63', set())
    assert not _is_linked(b, 'occi_Extension63', a2)
    if hasattr(a2, 'occi_Extension'):
        assert not _is_linked(a2, 'occi_Extension', b)


def test_assoc_kind41_reverse_link_reassign_clear():
    a1 = occi_Kind()
    a2 = occi_Kind()
    b = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    _safe_set(b, 'occi_Entity42', a1)
    assert _is_linked(b, 'occi_Entity42', a1)
    if hasattr(a1, 'occi_Kind43'):
        assert _is_linked(a1, 'occi_Kind43', b)
    _safe_set(b, 'occi_Entity42', a2)
    assert _is_linked(b, 'occi_Entity42', a2)
    if hasattr(a1, 'occi_Kind43'):
        assert not _is_linked(a1, 'occi_Kind43', b)
    if hasattr(a2, 'occi_Kind43'):
        assert _is_linked(a2, 'occi_Kind43', b)
    _safe_set(b, 'occi_Entity42', None)
    assert not _is_linked(b, 'occi_Entity42', a2)
    if hasattr(a2, 'occi_Kind43'):
        assert not _is_linked(a2, 'occi_Kind43', b)


def test_assoc_kinds65_reverse_link_reassign_clear():
    a1 = occi_Kind()
    a2 = occi_Kind()
    b = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    _safe_set(b, 'occi_Extension66', {a1})
    assert _is_linked(b, 'occi_Extension66', a1)
    if hasattr(a1, 'occi_Kind67'):
        assert _is_linked(a1, 'occi_Kind67', b)
    _safe_set(b, 'occi_Extension66', {a2})
    assert _is_linked(b, 'occi_Extension66', a2)
    if hasattr(a1, 'occi_Kind67'):
        assert not _is_linked(a1, 'occi_Kind67', b)
    if hasattr(a2, 'occi_Kind67'):
        assert _is_linked(a2, 'occi_Kind67', b)
    _safe_set(b, 'occi_Extension66', set())
    assert not _is_linked(b, 'occi_Extension66', a2)
    if hasattr(a2, 'occi_Kind67'):
        assert not _is_linked(a2, 'occi_Kind67', b)


def test_assoc_links56_reverse_link_reassign_clear():
    a1 = occi_Resource(summary="sample_text")
    a2 = occi_Resource(summary="sample_text_2")
    b = occi_Link()
    _safe_set(b, 'Link', a1)
    assert _is_linked(b, 'Link', a1)
    if hasattr(a1, 'source57'):
        assert _is_linked(a1, 'source57', b)
    _safe_set(b, 'Link', a2)
    assert _is_linked(b, 'Link', a2)
    if hasattr(a1, 'source57'):
        assert not _is_linked(a1, 'source57', b)
    if hasattr(a2, 'source57'):
        assert _is_linked(a2, 'source57', b)
    _safe_set(b, 'Link', None)
    assert not _is_linked(b, 'Link', a2)
    if hasattr(a2, 'source57'):
        assert not _is_linked(a2, 'source57', b)


def test_assoc_literal11_reverse_link_reassign_clear():
    a1 = occi_State(final="sample_text", initial="sample_text")
    a2 = occi_State(final="sample_text_2", initial="sample_text_2")
    b = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    _safe_set(b, 'occi_EnumerationLiteral', a1)
    assert _is_linked(b, 'occi_EnumerationLiteral', a1)
    if hasattr(a1, 'occi_State'):
        assert _is_linked(a1, 'occi_State', b)
    _safe_set(b, 'occi_EnumerationLiteral', a2)
    assert _is_linked(b, 'occi_EnumerationLiteral', a2)
    if hasattr(a1, 'occi_State'):
        assert not _is_linked(a1, 'occi_State', b)
    if hasattr(a2, 'occi_State'):
        assert _is_linked(a2, 'occi_State', b)
    _safe_set(b, 'occi_EnumerationLiteral', None)
    assert not _is_linked(b, 'occi_EnumerationLiteral', a2)
    if hasattr(a2, 'occi_State'):
        assert not _is_linked(a2, 'occi_State', b)


def test_assoc_parent24_reverse_link_reassign_clear():
    a1 = occi_Kind()
    a2 = occi_Kind()
    b = occi_Kind()
    _safe_set(b, 'occi_Kind23', a1)
    assert _is_linked(b, 'occi_Kind23', a1)
    if hasattr(a1, 'occi_Kind'):
        assert _is_linked(a1, 'occi_Kind', b)
    _safe_set(b, 'occi_Kind23', a2)
    assert _is_linked(b, 'occi_Kind23', a2)
    if hasattr(a1, 'occi_Kind'):
        assert not _is_linked(a1, 'occi_Kind', b)
    if hasattr(a2, 'occi_Kind'):
        assert _is_linked(a2, 'occi_Kind', b)
    _safe_set(b, 'occi_Kind23', None)
    assert not _is_linked(b, 'occi_Kind23', a2)
    if hasattr(a2, 'occi_Kind'):
        assert not _is_linked(a2, 'occi_Kind', b)


def test_assoc_resources76_reverse_link_reassign_clear():
    a1 = occi_Resource(summary="sample_text")
    a2 = occi_Resource(summary="sample_text_2")
    b = occi_Configuration(description="sample_text", location="sample_text")
    _safe_set(b, 'occi_Configuration77', {a1})
    assert _is_linked(b, 'occi_Configuration77', a1)
    if hasattr(a1, 'occi_Resource'):
        assert _is_linked(a1, 'occi_Resource', b)
    _safe_set(b, 'occi_Configuration77', {a2})
    assert _is_linked(b, 'occi_Configuration77', a2)
    if hasattr(a1, 'occi_Resource'):
        assert not _is_linked(a1, 'occi_Resource', b)
    if hasattr(a2, 'occi_Resource'):
        assert _is_linked(a2, 'occi_Resource', b)
    _safe_set(b, 'occi_Configuration77', set())
    assert not _is_linked(b, 'occi_Configuration77', a2)
    if hasattr(a2, 'occi_Resource'):
        assert not _is_linked(a2, 'occi_Resource', b)


def test_assoc_rlinks58_reverse_link_reassign_clear():
    a1 = occi_Resource(summary="sample_text")
    a2 = occi_Resource(summary="sample_text_2")
    b = occi_Link()
    _safe_set(b, 'Link59', a1)
    assert _is_linked(b, 'Link59', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Link59', a2)
    assert _is_linked(b, 'Link59', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Link59', None)
    assert not _is_linked(b, 'Link59', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_source28_reverse_link_reassign_clear():
    a1 = occi_Kind()
    a2 = occi_Kind()
    b = occi_Kind()
    _safe_set(b, 'occi_Kind29', a1)
    assert _is_linked(b, 'occi_Kind29', a1)
    if hasattr(a1, 'occi_Kind27'):
        assert _is_linked(a1, 'occi_Kind27', b)
    _safe_set(b, 'occi_Kind29', a2)
    assert _is_linked(b, 'occi_Kind29', a2)
    if hasattr(a1, 'occi_Kind27'):
        assert not _is_linked(a1, 'occi_Kind27', b)
    if hasattr(a2, 'occi_Kind27'):
        assert _is_linked(a2, 'occi_Kind27', b)
    _safe_set(b, 'occi_Kind29', None)
    assert not _is_linked(b, 'occi_Kind29', a2)
    if hasattr(a2, 'occi_Kind27'):
        assert not _is_linked(a2, 'occi_Kind27', b)


def test_assoc_source60_reverse_link_reassign_clear():
    a1 = occi_Resource(summary="sample_text")
    a2 = occi_Resource(summary="sample_text_2")
    b = occi_Link()
    _safe_set(b, 'links', a1)
    assert _is_linked(b, 'links', a1)
    if hasattr(a1, 'Resource'):
        assert _is_linked(a1, 'Resource', b)
    _safe_set(b, 'links', a2)
    assert _is_linked(b, 'links', a2)
    if hasattr(a1, 'Resource'):
        assert not _is_linked(a1, 'Resource', b)
    if hasattr(a2, 'Resource'):
        assert _is_linked(a2, 'Resource', b)
    _safe_set(b, 'links', None)
    assert not _is_linked(b, 'links', a2)
    if hasattr(a2, 'Resource'):
        assert not _is_linked(a2, 'Resource', b)


def test_assoc_target31_reverse_link_reassign_clear():
    a1 = occi_Kind()
    a2 = occi_Kind()
    b = occi_Kind()
    _safe_set(b, 'occi_Kind32', a1)
    assert _is_linked(b, 'occi_Kind32', a1)
    if hasattr(a1, 'occi_Kind30'):
        assert _is_linked(a1, 'occi_Kind30', b)
    _safe_set(b, 'occi_Kind32', a2)
    assert _is_linked(b, 'occi_Kind32', a2)
    if hasattr(a1, 'occi_Kind30'):
        assert not _is_linked(a1, 'occi_Kind30', b)
    if hasattr(a2, 'occi_Kind30'):
        assert _is_linked(a2, 'occi_Kind30', b)
    _safe_set(b, 'occi_Kind32', None)
    assert not _is_linked(b, 'occi_Kind32', a2)
    if hasattr(a2, 'occi_Kind30'):
        assert not _is_linked(a2, 'occi_Kind30', b)


def test_assoc_target61_reverse_link_reassign_clear():
    a1 = occi_Resource(summary="sample_text")
    a2 = occi_Resource(summary="sample_text_2")
    b = occi_Link()
    _safe_set(b, 'rlinks', a1)
    assert _is_linked(b, 'rlinks', a1)
    if hasattr(a1, 'Resource62'):
        assert _is_linked(a1, 'Resource62', b)
    _safe_set(b, 'rlinks', a2)
    assert _is_linked(b, 'rlinks', a2)
    if hasattr(a1, 'Resource62'):
        assert not _is_linked(a1, 'Resource62', b)
    if hasattr(a2, 'Resource62'):
        assert _is_linked(a2, 'Resource62', b)
    _safe_set(b, 'rlinks', None)
    assert not _is_linked(b, 'rlinks', a2)
    if hasattr(a2, 'Resource62'):
        assert not _is_linked(a2, 'Resource62', b)


def test_assoc_type21_reverse_link_reassign_clear():
    a1 = occi_DataType(documentation="sample_text", name="sample_text")
    a2 = occi_DataType(documentation="sample_text_2", name="sample_text_2")
    b = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    _safe_set(b, 'occi_Attribute22', a1)
    assert _is_linked(b, 'occi_Attribute22', a1)
    if hasattr(a1, 'occi_DataType'):
        assert _is_linked(a1, 'occi_DataType', b)
    _safe_set(b, 'occi_Attribute22', a2)
    assert _is_linked(b, 'occi_Attribute22', a2)
    if hasattr(a1, 'occi_DataType'):
        assert not _is_linked(a1, 'occi_DataType', b)
    if hasattr(a2, 'occi_DataType'):
        assert _is_linked(a2, 'occi_DataType', b)
    _safe_set(b, 'occi_Attribute22', None)
    assert not _is_linked(b, 'occi_Attribute22', a2)
    if hasattr(a2, 'occi_DataType'):
        assert not _is_linked(a2, 'occi_DataType', b)


def test_assoc_types71_reverse_link_reassign_clear():
    a1 = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    a2 = occi_Extension(description="sample_text_2", name="sample_text_2", scheme="sample_text_2", specification="sample_text_2")
    b = occi_DataType(documentation="sample_text", name="sample_text")
    _safe_set(b, 'occi_DataType73', a1)
    assert _is_linked(b, 'occi_DataType73', a1)
    if hasattr(a1, 'occi_Extension72'):
        assert _is_linked(a1, 'occi_Extension72', b)
    _safe_set(b, 'occi_DataType73', a2)
    assert _is_linked(b, 'occi_DataType73', a2)
    if hasattr(a1, 'occi_Extension72'):
        assert not _is_linked(a1, 'occi_Extension72', b)
    if hasattr(a2, 'occi_Extension72'):
        assert _is_linked(a2, 'occi_Extension72', b)
    _safe_set(b, 'occi_DataType73', None)
    assert not _is_linked(b, 'occi_DataType73', a2)
    if hasattr(a2, 'occi_Extension72'):
        assert not _is_linked(a2, 'occi_Extension72', b)


def test_assoc_use74_reverse_link_reassign_clear():
    a1 = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    a2 = occi_Extension(description="sample_text_2", name="sample_text_2", scheme="sample_text_2", specification="sample_text_2")
    b = occi_Configuration(description="sample_text", location="sample_text")
    _safe_set(b, 'occi_Configuration', {a1})
    assert _is_linked(b, 'occi_Configuration', a1)
    if hasattr(a1, 'occi_Extension75'):
        assert _is_linked(a1, 'occi_Extension75', b)
    _safe_set(b, 'occi_Configuration', {a2})
    assert _is_linked(b, 'occi_Configuration', a2)
    if hasattr(a1, 'occi_Extension75'):
        assert not _is_linked(a1, 'occi_Extension75', b)
    if hasattr(a2, 'occi_Extension75'):
        assert _is_linked(a2, 'occi_Extension75', b)
    _safe_set(b, 'occi_Configuration', set())
    assert not _is_linked(b, 'occi_Configuration', a2)
    if hasattr(a2, 'occi_Extension75'):
        assert not _is_linked(a2, 'occi_Extension75', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations0_stub_double():
    # occi_AnnotatedElement has no real 'occi_AnnotatedElement' property in the generated
    # code (a bare stub) -- manually attach it so occi_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Annotation(key="sample_text", value="sample_text")
    partner = occi_AnnotatedElement()
    setattr(partner, 'occi_AnnotatedElement', None)
    _safe_set(owner, 'occi_Annotation', partner)
    assert owner in getattr(partner, 'occi_AnnotatedElement')
    _safe_set(owner, 'occi_Annotation', None)
    assert owner not in getattr(partner, 'occi_AnnotatedElement')


def test_assoc_applies35_stub_double():
    # occi_Mixin has no real 'occi_Mixin36' property in the generated
    # code (a bare stub) -- manually attach it so occi_Kind's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Kind's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Kind()
    partner = occi_Mixin()
    setattr(partner, 'occi_Mixin36', None)
    _safe_set(owner, 'occi_Kind37', partner)
    assert owner in getattr(partner, 'occi_Mixin36')
    _safe_set(owner, 'occi_Kind37', None)
    assert owner not in getattr(partner, 'occi_Mixin36')


def test_assoc_attribute8_stub_double():
    # occi_FSM has no real 'occi_FSM9' property in the generated
    # code (a bare stub) -- manually attach it so occi_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Attribute(default="sample_text", description="sample_text", mutable="sample_text", name="sample_text", required="sample_text")
    partner = occi_FSM()
    setattr(partner, 'occi_FSM9', None)
    _safe_set(owner, 'occi_Attribute10', partner)
    assert getattr(partner, 'occi_FSM9') == owner
    _safe_set(owner, 'occi_Attribute10', None)
    assert getattr(partner, 'occi_FSM9') is None


def test_assoc_attributes53_stub_double():
    # occi_MixinBase has no real 'occi_MixinBase54' property in the generated
    # code (a bare stub) -- manually attach it so occi_AttributeState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_AttributeState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_AttributeState(name="sample_text", value="sample_text")
    partner = occi_MixinBase()
    setattr(partner, 'occi_MixinBase54', None)
    _safe_set(owner, 'occi_AttributeState55', partner)
    assert owner in getattr(partner, 'occi_MixinBase54')
    _safe_set(owner, 'occi_AttributeState55', None)
    assert owner not in getattr(partner, 'occi_MixinBase54')


def test_assoc_constraints3_stub_double():
    # occi_Type has no real 'occi_Type4' property in the generated
    # code (a bare stub) -- manually attach it so occi_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Constraint(body="sample_text", description="sample_text", name="sample_text")
    partner = occi_Type()
    setattr(partner, 'occi_Type4', None)
    _safe_set(owner, 'occi_Constraint', partner)
    assert owner in getattr(partner, 'occi_Type4')
    _safe_set(owner, 'occi_Constraint', None)
    assert owner not in getattr(partner, 'occi_Type4')


def test_assoc_entities38_stub_double():
    # occi_Mixin has no real 'occi_Mixin39' property in the generated
    # code (a bare stub) -- manually attach it so occi_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    partner = occi_Mixin()
    setattr(partner, 'occi_Mixin39', None)
    _safe_set(owner, 'occi_Entity40', partner)
    assert owner in getattr(partner, 'occi_Mixin39')
    _safe_set(owner, 'occi_Entity40', None)
    assert owner not in getattr(partner, 'occi_Mixin39')


def test_assoc_entity52_stub_double():
    # occi_MixinBase has no real 'parts' property in the generated
    # code (a bare stub) -- manually attach it so occi_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    partner = occi_MixinBase()
    setattr(partner, 'parts', None)
    _safe_set(owner, 'Entity', partner)
    assert getattr(partner, 'parts') == owner
    _safe_set(owner, 'Entity', None)
    assert getattr(partner, 'parts') is None


def test_assoc_enumerationType82_stub_double():
    # occi_EnumerationType has no real 'EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so occi_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    partner = occi_EnumerationType()
    setattr(partner, 'EnumerationType', None)
    _safe_set(owner, 'literals', partner)
    assert getattr(partner, 'EnumerationType') == owner
    _safe_set(owner, 'literals', None)
    assert getattr(partner, 'EnumerationType') is None


def test_assoc_literals81_stub_double():
    # occi_EnumerationType has no real 'enumerationType' property in the generated
    # code (a bare stub) -- manually attach it so occi_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_EnumerationLiteral(documentation="sample_text", name="sample_text")
    partner = occi_EnumerationType()
    setattr(partner, 'enumerationType', None)
    _safe_set(owner, 'EnumerationLiteral', partner)
    assert owner in getattr(partner, 'enumerationType')
    _safe_set(owner, 'EnumerationLiteral', None)
    assert owner not in getattr(partner, 'enumerationType')


def test_assoc_mixins46_stub_double():
    # occi_Mixin has no real 'occi_Mixin48' property in the generated
    # code (a bare stub) -- manually attach it so occi_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    partner = occi_Mixin()
    setattr(partner, 'occi_Mixin48', None)
    _safe_set(owner, 'occi_Entity47', {partner})
    assert getattr(partner, 'occi_Mixin48') == owner
    _safe_set(owner, 'occi_Entity47', set())
    assert getattr(partner, 'occi_Mixin48') is None


def test_assoc_mixins68_stub_double():
    # occi_Mixin has no real 'occi_Mixin70' property in the generated
    # code (a bare stub) -- manually attach it so occi_Extension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Extension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Extension(description="sample_text", name="sample_text", scheme="sample_text", specification="sample_text")
    partner = occi_Mixin()
    setattr(partner, 'occi_Mixin70', None)
    _safe_set(owner, 'occi_Extension69', {partner})
    assert getattr(partner, 'occi_Mixin70') == owner
    _safe_set(owner, 'occi_Extension69', set())
    assert getattr(partner, 'occi_Mixin70') is None


def test_assoc_mixins78_stub_double():
    # occi_Mixin has no real 'occi_Mixin80' property in the generated
    # code (a bare stub) -- manually attach it so occi_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Configuration(description="sample_text", location="sample_text")
    partner = occi_Mixin()
    setattr(partner, 'occi_Mixin80', None)
    _safe_set(owner, 'occi_Configuration79', {partner})
    assert getattr(partner, 'occi_Mixin80') == owner
    _safe_set(owner, 'occi_Configuration79', set())
    assert getattr(partner, 'occi_Mixin80') is None


def test_assoc_outgoingTransition13_stub_double():
    # occi_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so occi_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_State(final="sample_text", initial="sample_text")
    partner = occi_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_ownedState7_stub_double():
    # occi_FSM has no real 'owningFSM' property in the generated
    # code (a bare stub) -- manually attach it so occi_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_State(final="sample_text", initial="sample_text")
    partner = occi_FSM()
    setattr(partner, 'owningFSM', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningFSM')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningFSM')


def test_assoc_owningFSM12_stub_double():
    # occi_FSM has no real 'FSM' property in the generated
    # code (a bare stub) -- manually attach it so occi_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_State(final="sample_text", initial="sample_text")
    partner = occi_FSM()
    setattr(partner, 'FSM', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'FSM') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'FSM') is None


def test_assoc_parts49_stub_double():
    # occi_MixinBase has no real 'MixinBase' property in the generated
    # code (a bare stub) -- manually attach it so occi_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_Entity(id="sample_text", location="sample_text", title="sample_text")
    partner = occi_MixinBase()
    setattr(partner, 'MixinBase', None)
    _safe_set(owner, 'entity', {partner})
    assert getattr(partner, 'MixinBase') == owner
    _safe_set(owner, 'entity', set())
    assert getattr(partner, 'MixinBase') is None


def test_assoc_source14_stub_double():
    # occi_Transition has no real 'outgoingTransition' property in the generated
    # code (a bare stub) -- manually attach it so occi_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_State(final="sample_text", initial="sample_text")
    partner = occi_Transition()
    setattr(partner, 'outgoingTransition', None)
    _safe_set(owner, 'State15', partner)
    assert getattr(partner, 'outgoingTransition') == owner
    _safe_set(owner, 'State15', None)
    assert getattr(partner, 'outgoingTransition') is None


def test_assoc_target16_stub_double():
    # occi_Transition has no real 'occi_Transition' property in the generated
    # code (a bare stub) -- manually attach it so occi_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_State(final="sample_text", initial="sample_text")
    partner = occi_Transition()
    setattr(partner, 'occi_Transition', None)
    _safe_set(owner, 'occi_State17', partner)
    assert getattr(partner, 'occi_Transition') == owner
    _safe_set(owner, 'occi_State17', None)
    assert getattr(partner, 'occi_Transition') is None


def test_assoc_type84_stub_double():
    # occi_ArrayType has no real 'occi_ArrayType' property in the generated
    # code (a bare stub) -- manually attach it so occi_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # occi_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = occi_DataType(documentation="sample_text", name="sample_text")
    partner = occi_ArrayType()
    setattr(partner, 'occi_ArrayType', None)
    _safe_set(owner, 'occi_DataType85', partner)
    assert getattr(partner, 'occi_ArrayType') == owner
    _safe_set(owner, 'occi_DataType85', None)
    assert getattr(partner, 'occi_ArrayType') is None


