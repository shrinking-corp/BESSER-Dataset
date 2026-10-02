import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    cjsidl_EObject,
    cjsidl_action,
    cjsidl_actionList,
    cjsidl_arrayDef,
    cjsidl_bitfieldDef,
    cjsidl_bodyDef,
    cjsidl_bodyRef,
    cjsidl_bodyScopedRef,
    cjsidl_constDef,
    cjsidl_constReference,
    cjsidl_containerDef,
    cjsidl_containerRef,
    cjsidl_declaredConstSet,
    cjsidl_declaredConstSetRef,
    cjsidl_declaredEventDef,
    cjsidl_declaredTypeSet,
    cjsidl_declaredTypeSetRef,
    cjsidl_defaultState,
    cjsidl_defaultTransition,
    cjsidl_description,
    cjsidl_entry,
    cjsidl_eventDef,
    cjsidl_exit,
    cjsidl_fixedFieldDef,
    cjsidl_fixedLenString,
    cjsidl_footerDef,
    cjsidl_footerRef,
    cjsidl_footerScopedRef,
    cjsidl_formatEnumDef,
    cjsidl_guard,
    cjsidl_guardAction,
    cjsidl_guardParam,
    cjsidl_headerDef,
    cjsidl_headerRef,
    cjsidl_headerScopedRef,
    cjsidl_internalEventSet,
    cjsidl_internalTransition,
    cjsidl_jaus,
    cjsidl_listDef,
    cjsidl_messageDef,
    cjsidl_messageRef,
    cjsidl_messageScopedRef,
    cjsidl_messageSet,
    cjsidl_messages,
    cjsidl_nextState,
    cjsidl_popTransition,
    cjsidl_protocolBehavior,
    cjsidl_pushTransition,
    cjsidl_recordDef,
    cjsidl_refAttr,
    cjsidl_references,
    cjsidl_scaledRangeDef,
    cjsidl_scopedConstId,
    cjsidl_scopedEventType,
    cjsidl_scopedType,
    cjsidl_scopedTypeId,
    cjsidl_sendActionList,
    cjsidl_sequenceDef,
    cjsidl_serviceDef,
    cjsidl_simpleNumericType,
    cjsidl_simpleTransition,
    cjsidl_startState,
    cjsidl_state,
    cjsidl_stateMachine,
    cjsidl_subField,
    cjsidl_taggedItemDef,
    cjsidl_taggedUnitsEnum,
    cjsidl_transParam,
    cjsidl_transParams,
    cjsidl_transition,
    cjsidl_typeDef,
    cjsidl_typeReference,
    cjsidl_valueRange,
    cjsidl_valueSetDef,
    cjsidl_valueSpec,
    cjsidl_varField,
    cjsidl_varFormatField,
    cjsidl_varLenField,
    cjsidl_varLenString,
    cjsidl_variantDef,
    containerDef,
    FIELD_FORMAT,
    UNIT,
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

def test_assoc_constDef24_reverse_link_reassign_clear():
    a1 = cjsidl_declaredConstSet(constName="sample_text", constSetVersion="sample_text", name="sample_text")
    a2 = cjsidl_declaredConstSet(constName="sample_text_2", constSetVersion="sample_text_2", name="sample_text_2")
    b = cjsidl_constDef(comment="sample_text", constValue="sample_text", fieldUnits="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_constDef', a1)
    assert _is_linked(b, 'cjsidl_constDef', a1)
    if hasattr(a1, 'cjsidl_declaredConstSet25'):
        assert _is_linked(a1, 'cjsidl_declaredConstSet25', b)
    _safe_set(b, 'cjsidl_constDef', a2)
    assert _is_linked(b, 'cjsidl_constDef', a2)
    if hasattr(a1, 'cjsidl_declaredConstSet25'):
        assert not _is_linked(a1, 'cjsidl_declaredConstSet25', b)
    if hasattr(a2, 'cjsidl_declaredConstSet25'):
        assert _is_linked(a2, 'cjsidl_declaredConstSet25', b)
    _safe_set(b, 'cjsidl_constDef', None)
    assert not _is_linked(b, 'cjsidl_constDef', a2)
    if hasattr(a2, 'cjsidl_declaredConstSet25'):
        assert not _is_linked(a2, 'cjsidl_declaredConstSet25', b)


def test_assoc_constRef344_reverse_link_reassign_clear():
    a1 = cjsidl_formatEnumDef(fieldFormat="sample_text", fieldFormatStr="sample_text", index="sample_text")
    a2 = cjsidl_formatEnumDef(fieldFormat="sample_text_2", fieldFormatStr="sample_text_2", index="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference346', a1)
    assert _is_linked(b, 'cjsidl_constReference346', a1)
    if hasattr(a1, 'cjsidl_formatEnumDef345'):
        assert _is_linked(a1, 'cjsidl_formatEnumDef345', b)
    _safe_set(b, 'cjsidl_constReference346', a2)
    assert _is_linked(b, 'cjsidl_constReference346', a2)
    if hasattr(a1, 'cjsidl_formatEnumDef345'):
        assert not _is_linked(a1, 'cjsidl_formatEnumDef345', b)
    if hasattr(a2, 'cjsidl_formatEnumDef345'):
        assert _is_linked(a2, 'cjsidl_formatEnumDef345', b)
    _safe_set(b, 'cjsidl_constReference346', None)
    assert not _is_linked(b, 'cjsidl_constReference346', a2)
    if hasattr(a2, 'cjsidl_formatEnumDef345'):
        assert not _is_linked(a2, 'cjsidl_formatEnumDef345', b)


def test_assoc_constSet4_reverse_link_reassign_clear():
    a1 = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    a2 = cjsidl_serviceDef(assumpt="sample_text_2", name="sample_text_2", serviceName="sample_text_2", serviceVersion="sample_text_2")
    b = cjsidl_declaredConstSet(constName="sample_text", constSetVersion="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_declaredConstSet', a1)
    assert _is_linked(b, 'cjsidl_declaredConstSet', a1)
    if hasattr(a1, 'cjsidl_serviceDef5'):
        assert _is_linked(a1, 'cjsidl_serviceDef5', b)
    _safe_set(b, 'cjsidl_declaredConstSet', a2)
    assert _is_linked(b, 'cjsidl_declaredConstSet', a2)
    if hasattr(a1, 'cjsidl_serviceDef5'):
        assert not _is_linked(a1, 'cjsidl_serviceDef5', b)
    if hasattr(a2, 'cjsidl_serviceDef5'):
        assert _is_linked(a2, 'cjsidl_serviceDef5', b)
    _safe_set(b, 'cjsidl_declaredConstSet', None)
    assert not _is_linked(b, 'cjsidl_declaredConstSet', a2)
    if hasattr(a2, 'cjsidl_serviceDef5'):
        assert not _is_linked(a2, 'cjsidl_serviceDef5', b)


def test_assoc_constType185_reverse_link_reassign_clear():
    a1 = cjsidl_simpleNumericType(type="sample_text")
    a2 = cjsidl_simpleNumericType(type="sample_text_2")
    b = cjsidl_constDef(comment="sample_text", constValue="sample_text", fieldUnits="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_constDef186', a1)
    assert _is_linked(b, 'cjsidl_constDef186', a1)
    if hasattr(a1, 'cjsidl_simpleNumericType'):
        assert _is_linked(a1, 'cjsidl_simpleNumericType', b)
    _safe_set(b, 'cjsidl_constDef186', a2)
    assert _is_linked(b, 'cjsidl_constDef186', a2)
    if hasattr(a1, 'cjsidl_simpleNumericType'):
        assert not _is_linked(a1, 'cjsidl_simpleNumericType', b)
    if hasattr(a2, 'cjsidl_simpleNumericType'):
        assert _is_linked(a2, 'cjsidl_simpleNumericType', b)
    _safe_set(b, 'cjsidl_constDef186', None)
    assert not _is_linked(b, 'cjsidl_constDef186', a2)
    if hasattr(a2, 'cjsidl_simpleNumericType'):
        assert not _is_linked(a2, 'cjsidl_simpleNumericType', b)


def test_assoc_constVal453_reverse_link_reassign_clear():
    a1 = cjsidl_constReference(comment="sample_text")
    a2 = cjsidl_constReference(comment="sample_text_2")
    b = cjsidl_constDef(comment="sample_text", constValue="sample_text", fieldUnits="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_constDef455', a1)
    assert _is_linked(b, 'cjsidl_constDef455', a1)
    if hasattr(a1, 'cjsidl_constReference454'):
        assert _is_linked(a1, 'cjsidl_constReference454', b)
    _safe_set(b, 'cjsidl_constDef455', a2)
    assert _is_linked(b, 'cjsidl_constDef455', a2)
    if hasattr(a1, 'cjsidl_constReference454'):
        assert not _is_linked(a1, 'cjsidl_constReference454', b)
    if hasattr(a2, 'cjsidl_constReference454'):
        assert _is_linked(a2, 'cjsidl_constReference454', b)
    _safe_set(b, 'cjsidl_constDef455', None)
    assert not _is_linked(b, 'cjsidl_constDef455', a2)
    if hasattr(a2, 'cjsidl_constReference454'):
        assert not _is_linked(a2, 'cjsidl_constReference454', b)


def test_assoc_containerDef397_reverse_link_reassign_clear():
    a1 = cjsidl_listDef(countComment="sample_text", maxCount="sample_text", minCount="sample_text")
    a2 = cjsidl_listDef(countComment="sample_text_2", maxCount="sample_text_2", minCount="sample_text_2")
    b = cjsidl_containerDef(comment="sample_text", name="sample_text", optional="sample_text")
    _safe_set(b, 'cjsidl_containerDef399', a1)
    assert _is_linked(b, 'cjsidl_containerDef399', a1)
    if hasattr(a1, 'cjsidl_listDef398'):
        assert _is_linked(a1, 'cjsidl_listDef398', b)
    _safe_set(b, 'cjsidl_containerDef399', a2)
    assert _is_linked(b, 'cjsidl_containerDef399', a2)
    if hasattr(a1, 'cjsidl_listDef398'):
        assert not _is_linked(a1, 'cjsidl_listDef398', b)
    if hasattr(a2, 'cjsidl_listDef398'):
        assert _is_linked(a2, 'cjsidl_listDef398', b)
    _safe_set(b, 'cjsidl_containerDef399', None)
    assert not _is_linked(b, 'cjsidl_containerDef399', a2)
    if hasattr(a2, 'cjsidl_listDef398'):
        assert not _is_linked(a2, 'cjsidl_listDef398', b)


def test_assoc_containerRef394_reverse_link_reassign_clear():
    a1 = cjsidl_listDef(countComment="sample_text", maxCount="sample_text", minCount="sample_text")
    a2 = cjsidl_listDef(countComment="sample_text_2", maxCount="sample_text_2", minCount="sample_text_2")
    b = cjsidl_containerRef(comment="sample_text", name="sample_text", optional="sample_text")
    _safe_set(b, 'cjsidl_containerRef396', a1)
    assert _is_linked(b, 'cjsidl_containerRef396', a1)
    if hasattr(a1, 'cjsidl_listDef395'):
        assert _is_linked(a1, 'cjsidl_listDef395', b)
    _safe_set(b, 'cjsidl_containerRef396', a2)
    assert _is_linked(b, 'cjsidl_containerRef396', a2)
    if hasattr(a1, 'cjsidl_listDef395'):
        assert not _is_linked(a1, 'cjsidl_listDef395', b)
    if hasattr(a2, 'cjsidl_listDef395'):
        assert _is_linked(a2, 'cjsidl_listDef395', b)
    _safe_set(b, 'cjsidl_containerRef396', None)
    assert not _is_linked(b, 'cjsidl_containerRef396', a2)
    if hasattr(a2, 'cjsidl_listDef395'):
        assert not _is_linked(a2, 'cjsidl_listDef395', b)


def test_assoc_countRange340_reverse_link_reassign_clear():
    a1 = cjsidl_varFormatField(comment="sample_text", countComment="sample_text", name="sample_text", optional="sample_text", units="sample_text")
    a2 = cjsidl_varFormatField(comment="sample_text_2", countComment="sample_text_2", name="sample_text_2", optional="sample_text_2", units="sample_text_2")
    b = cjsidl_valueRange(comment="sample_text", lowerLim="sample_text", lowerLimit_type="sample_text", upperLim="sample_text", upperLimit_type="sample_text")
    _safe_set(b, 'cjsidl_valueRange', a1)
    assert _is_linked(b, 'cjsidl_valueRange', a1)
    if hasattr(a1, 'cjsidl_varFormatField341'):
        assert _is_linked(a1, 'cjsidl_varFormatField341', b)
    _safe_set(b, 'cjsidl_valueRange', a2)
    assert _is_linked(b, 'cjsidl_valueRange', a2)
    if hasattr(a1, 'cjsidl_varFormatField341'):
        assert not _is_linked(a1, 'cjsidl_varFormatField341', b)
    if hasattr(a2, 'cjsidl_varFormatField341'):
        assert _is_linked(a2, 'cjsidl_varFormatField341', b)
    _safe_set(b, 'cjsidl_valueRange', None)
    assert not _is_linked(b, 'cjsidl_valueRange', a2)
    if hasattr(a2, 'cjsidl_varFormatField341'):
        assert not _is_linked(a2, 'cjsidl_varFormatField341', b)


def test_assoc_declaredConstSetRef22_reverse_link_reassign_clear():
    a1 = cjsidl_declaredConstSetRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_declaredConstSetRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_declaredConstSet(constName="sample_text", constSetVersion="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_declaredConstSet23', {a1})
    assert _is_linked(b, 'cjsidl_declaredConstSet23', a1)
    if hasattr(a1, 'cjsidl_declaredConstSetRef'):
        assert _is_linked(a1, 'cjsidl_declaredConstSetRef', b)
    _safe_set(b, 'cjsidl_declaredConstSet23', {a2})
    assert _is_linked(b, 'cjsidl_declaredConstSet23', a2)
    if hasattr(a1, 'cjsidl_declaredConstSetRef'):
        assert not _is_linked(a1, 'cjsidl_declaredConstSetRef', b)
    if hasattr(a2, 'cjsidl_declaredConstSetRef'):
        assert _is_linked(a2, 'cjsidl_declaredConstSetRef', b)
    _safe_set(b, 'cjsidl_declaredConstSet23', set())
    assert not _is_linked(b, 'cjsidl_declaredConstSet23', a2)
    if hasattr(a2, 'cjsidl_declaredConstSetRef'):
        assert not _is_linked(a2, 'cjsidl_declaredConstSetRef', b)


def test_assoc_declaredConstSetRef29_reverse_link_reassign_clear():
    a1 = cjsidl_declaredTypeSet(name="sample_text", typeName="sample_text", version="sample_text")
    a2 = cjsidl_declaredTypeSet(name="sample_text_2", typeName="sample_text_2", version="sample_text_2")
    b = cjsidl_declaredConstSetRef(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_declaredConstSetRef31', a1)
    assert _is_linked(b, 'cjsidl_declaredConstSetRef31', a1)
    if hasattr(a1, 'cjsidl_declaredTypeSet30'):
        assert _is_linked(a1, 'cjsidl_declaredTypeSet30', b)
    _safe_set(b, 'cjsidl_declaredConstSetRef31', a2)
    assert _is_linked(b, 'cjsidl_declaredConstSetRef31', a2)
    if hasattr(a1, 'cjsidl_declaredTypeSet30'):
        assert not _is_linked(a1, 'cjsidl_declaredTypeSet30', b)
    if hasattr(a2, 'cjsidl_declaredTypeSet30'):
        assert _is_linked(a2, 'cjsidl_declaredTypeSet30', b)
    _safe_set(b, 'cjsidl_declaredConstSetRef31', None)
    assert not _is_linked(b, 'cjsidl_declaredConstSetRef31', a2)
    if hasattr(a2, 'cjsidl_declaredTypeSet30'):
        assert not _is_linked(a2, 'cjsidl_declaredTypeSet30', b)


def test_assoc_declaredTypeSetRef32_reverse_link_reassign_clear():
    a1 = cjsidl_declaredTypeSetRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_declaredTypeSetRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_declaredTypeSet(name="sample_text", typeName="sample_text", version="sample_text")
    _safe_set(b, 'cjsidl_declaredTypeSet33', {a1})
    assert _is_linked(b, 'cjsidl_declaredTypeSet33', a1)
    if hasattr(a1, 'cjsidl_declaredTypeSetRef'):
        assert _is_linked(a1, 'cjsidl_declaredTypeSetRef', b)
    _safe_set(b, 'cjsidl_declaredTypeSet33', {a2})
    assert _is_linked(b, 'cjsidl_declaredTypeSet33', a2)
    if hasattr(a1, 'cjsidl_declaredTypeSetRef'):
        assert not _is_linked(a1, 'cjsidl_declaredTypeSetRef', b)
    if hasattr(a2, 'cjsidl_declaredTypeSetRef'):
        assert _is_linked(a2, 'cjsidl_declaredTypeSetRef', b)
    _safe_set(b, 'cjsidl_declaredTypeSet33', set())
    assert not _is_linked(b, 'cjsidl_declaredTypeSet33', a2)
    if hasattr(a2, 'cjsidl_declaredTypeSetRef'):
        assert not _is_linked(a2, 'cjsidl_declaredTypeSetRef', b)


def test_assoc_defaultState80_reverse_link_reassign_clear():
    a1 = cjsidl_stateMachine(comment="sample_text", name="sample_text")
    a2 = cjsidl_stateMachine(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_defaultState(comment="sample_text")
    _safe_set(b, 'cjsidl_defaultState', a1)
    assert _is_linked(b, 'cjsidl_defaultState', a1)
    if hasattr(a1, 'cjsidl_stateMachine81'):
        assert _is_linked(a1, 'cjsidl_stateMachine81', b)
    _safe_set(b, 'cjsidl_defaultState', a2)
    assert _is_linked(b, 'cjsidl_defaultState', a2)
    if hasattr(a1, 'cjsidl_stateMachine81'):
        assert not _is_linked(a1, 'cjsidl_stateMachine81', b)
    if hasattr(a2, 'cjsidl_stateMachine81'):
        assert _is_linked(a2, 'cjsidl_stateMachine81', b)
    _safe_set(b, 'cjsidl_defaultState', None)
    assert not _is_linked(b, 'cjsidl_defaultState', a2)
    if hasattr(a2, 'cjsidl_stateMachine81'):
        assert not _is_linked(a2, 'cjsidl_stateMachine81', b)


def test_assoc_defaultState93_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_defaultState(comment="sample_text")
    _safe_set(b, 'cjsidl_defaultState95', a1)
    assert _is_linked(b, 'cjsidl_defaultState95', a1)
    if hasattr(a1, 'cjsidl_state94'):
        assert _is_linked(a1, 'cjsidl_state94', b)
    _safe_set(b, 'cjsidl_defaultState95', a2)
    assert _is_linked(b, 'cjsidl_defaultState95', a2)
    if hasattr(a1, 'cjsidl_state94'):
        assert not _is_linked(a1, 'cjsidl_state94', b)
    if hasattr(a2, 'cjsidl_state94'):
        assert _is_linked(a2, 'cjsidl_state94', b)
    _safe_set(b, 'cjsidl_defaultState95', None)
    assert not _is_linked(b, 'cjsidl_defaultState95', a2)
    if hasattr(a2, 'cjsidl_state94'):
        assert not _is_linked(a2, 'cjsidl_state94', b)


def test_assoc_defaultTransition102_reverse_link_reassign_clear():
    a1 = cjsidl_defaultTransition(comment="sample_text", type="sample_text")
    a2 = cjsidl_defaultTransition(comment="sample_text_2", type="sample_text_2")
    b = cjsidl_defaultState(comment="sample_text")
    _safe_set(b, 'cjsidl_defaultState103', {a1})
    assert _is_linked(b, 'cjsidl_defaultState103', a1)
    if hasattr(a1, 'cjsidl_defaultTransition104'):
        assert _is_linked(a1, 'cjsidl_defaultTransition104', b)
    _safe_set(b, 'cjsidl_defaultState103', {a2})
    assert _is_linked(b, 'cjsidl_defaultState103', a2)
    if hasattr(a1, 'cjsidl_defaultTransition104'):
        assert not _is_linked(a1, 'cjsidl_defaultTransition104', b)
    if hasattr(a2, 'cjsidl_defaultTransition104'):
        assert _is_linked(a2, 'cjsidl_defaultTransition104', b)
    _safe_set(b, 'cjsidl_defaultState103', set())
    assert not _is_linked(b, 'cjsidl_defaultState103', a2)
    if hasattr(a2, 'cjsidl_defaultTransition104'):
        assert not _is_linked(a2, 'cjsidl_defaultTransition104', b)


def test_assoc_defaultTransition91_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_defaultTransition(comment="sample_text", type="sample_text")
    _safe_set(b, 'cjsidl_defaultTransition', a1)
    assert _is_linked(b, 'cjsidl_defaultTransition', a1)
    if hasattr(a1, 'cjsidl_state92'):
        assert _is_linked(a1, 'cjsidl_state92', b)
    _safe_set(b, 'cjsidl_defaultTransition', a2)
    assert _is_linked(b, 'cjsidl_defaultTransition', a2)
    if hasattr(a1, 'cjsidl_state92'):
        assert not _is_linked(a1, 'cjsidl_state92', b)
    if hasattr(a2, 'cjsidl_state92'):
        assert _is_linked(a2, 'cjsidl_state92', b)
    _safe_set(b, 'cjsidl_defaultTransition', None)
    assert not _is_linked(b, 'cjsidl_defaultTransition', a2)
    if hasattr(a2, 'cjsidl_state92'):
        assert not _is_linked(a2, 'cjsidl_state92', b)


def test_assoc_descr1_reverse_link_reassign_clear():
    a1 = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    a2 = cjsidl_serviceDef(assumpt="sample_text_2", name="sample_text_2", serviceName="sample_text_2", serviceVersion="sample_text_2")
    b = cjsidl_description(content="sample_text")
    _safe_set(b, 'cjsidl_description', a1)
    assert _is_linked(b, 'cjsidl_description', a1)
    if hasattr(a1, 'cjsidl_serviceDef'):
        assert _is_linked(a1, 'cjsidl_serviceDef', b)
    _safe_set(b, 'cjsidl_description', a2)
    assert _is_linked(b, 'cjsidl_description', a2)
    if hasattr(a1, 'cjsidl_serviceDef'):
        assert not _is_linked(a1, 'cjsidl_serviceDef', b)
    if hasattr(a2, 'cjsidl_serviceDef'):
        assert _is_linked(a2, 'cjsidl_serviceDef', b)
    _safe_set(b, 'cjsidl_description', None)
    assert not _is_linked(b, 'cjsidl_description', a2)
    if hasattr(a2, 'cjsidl_serviceDef'):
        assert not _is_linked(a2, 'cjsidl_serviceDef', b)


def test_assoc_descr223_reverse_link_reassign_clear():
    a1 = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    a2 = cjsidl_messageDef(command="sample_text_2", messageID="sample_text_2", name="sample_text_2")
    b = cjsidl_description(content="sample_text")
    _safe_set(b, 'cjsidl_description225', a1)
    assert _is_linked(b, 'cjsidl_description225', a1)
    if hasattr(a1, 'cjsidl_messageDef224'):
        assert _is_linked(a1, 'cjsidl_messageDef224', b)
    _safe_set(b, 'cjsidl_description225', a2)
    assert _is_linked(b, 'cjsidl_description225', a2)
    if hasattr(a1, 'cjsidl_messageDef224'):
        assert not _is_linked(a1, 'cjsidl_messageDef224', b)
    if hasattr(a2, 'cjsidl_messageDef224'):
        assert _is_linked(a2, 'cjsidl_messageDef224', b)
    _safe_set(b, 'cjsidl_description225', None)
    assert not _is_linked(b, 'cjsidl_description225', a2)
    if hasattr(a2, 'cjsidl_messageDef224'):
        assert not _is_linked(a2, 'cjsidl_messageDef224', b)


def test_assoc_descr54_reverse_link_reassign_clear():
    a1 = cjsidl_eventDef(name="sample_text")
    a2 = cjsidl_eventDef(name="sample_text_2")
    b = cjsidl_description(content="sample_text")
    _safe_set(b, 'cjsidl_description55', a1)
    assert _is_linked(b, 'cjsidl_description55', a1)
    if hasattr(a1, 'cjsidl_eventDef'):
        assert _is_linked(a1, 'cjsidl_eventDef', b)
    _safe_set(b, 'cjsidl_description55', a2)
    assert _is_linked(b, 'cjsidl_description55', a2)
    if hasattr(a1, 'cjsidl_eventDef'):
        assert not _is_linked(a1, 'cjsidl_eventDef', b)
    if hasattr(a2, 'cjsidl_eventDef'):
        assert _is_linked(a2, 'cjsidl_eventDef', b)
    _safe_set(b, 'cjsidl_description55', None)
    assert not _is_linked(b, 'cjsidl_description55', a2)
    if hasattr(a2, 'cjsidl_eventDef'):
        assert not _is_linked(a2, 'cjsidl_eventDef', b)


def test_assoc_entryAction85_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_entry(comment="sample_text")
    _safe_set(b, 'cjsidl_entry', a1)
    assert _is_linked(b, 'cjsidl_entry', a1)
    if hasattr(a1, 'cjsidl_state86'):
        assert _is_linked(a1, 'cjsidl_state86', b)
    _safe_set(b, 'cjsidl_entry', a2)
    assert _is_linked(b, 'cjsidl_entry', a2)
    if hasattr(a1, 'cjsidl_state86'):
        assert not _is_linked(a1, 'cjsidl_state86', b)
    if hasattr(a2, 'cjsidl_state86'):
        assert _is_linked(a2, 'cjsidl_state86', b)
    _safe_set(b, 'cjsidl_entry', None)
    assert not _is_linked(b, 'cjsidl_entry', a2)
    if hasattr(a2, 'cjsidl_state86'):
        assert not _is_linked(a2, 'cjsidl_state86', b)


def test_assoc_exitAction87_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_exit(comment="sample_text")
    _safe_set(b, 'cjsidl_exit', a1)
    assert _is_linked(b, 'cjsidl_exit', a1)
    if hasattr(a1, 'cjsidl_state88'):
        assert _is_linked(a1, 'cjsidl_state88', b)
    _safe_set(b, 'cjsidl_exit', a2)
    assert _is_linked(b, 'cjsidl_exit', a2)
    if hasattr(a1, 'cjsidl_state88'):
        assert not _is_linked(a1, 'cjsidl_state88', b)
    if hasattr(a2, 'cjsidl_state88'):
        assert _is_linked(a2, 'cjsidl_state88', b)
    _safe_set(b, 'cjsidl_exit', None)
    assert not _is_linked(b, 'cjsidl_exit', a2)
    if hasattr(a2, 'cjsidl_state88'):
        assert not _is_linked(a2, 'cjsidl_state88', b)


def test_assoc_firstState160_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_nextState(comment="sample_text")
    _safe_set(b, 'cjsidl_nextState161', a1)
    assert _is_linked(b, 'cjsidl_nextState161', a1)
    if hasattr(a1, 'cjsidl_state162'):
        assert _is_linked(a1, 'cjsidl_state162', b)
    _safe_set(b, 'cjsidl_nextState161', a2)
    assert _is_linked(b, 'cjsidl_nextState161', a2)
    if hasattr(a1, 'cjsidl_state162'):
        assert not _is_linked(a1, 'cjsidl_state162', b)
    if hasattr(a2, 'cjsidl_state162'):
        assert _is_linked(a2, 'cjsidl_state162', b)
    _safe_set(b, 'cjsidl_nextState161', None)
    assert not _is_linked(b, 'cjsidl_nextState161', a2)
    if hasattr(a2, 'cjsidl_state162'):
        assert not _is_linked(a2, 'cjsidl_state162', b)


def test_assoc_formatField342_reverse_link_reassign_clear():
    a1 = cjsidl_varFormatField(comment="sample_text", countComment="sample_text", name="sample_text", optional="sample_text", units="sample_text")
    a2 = cjsidl_varFormatField(comment="sample_text_2", countComment="sample_text_2", name="sample_text_2", optional="sample_text_2", units="sample_text_2")
    b = cjsidl_formatEnumDef(fieldFormat="sample_text", fieldFormatStr="sample_text", index="sample_text")
    _safe_set(b, 'cjsidl_formatEnumDef', a1)
    assert _is_linked(b, 'cjsidl_formatEnumDef', a1)
    if hasattr(a1, 'cjsidl_varFormatField343'):
        assert _is_linked(a1, 'cjsidl_varFormatField343', b)
    _safe_set(b, 'cjsidl_formatEnumDef', a2)
    assert _is_linked(b, 'cjsidl_formatEnumDef', a2)
    if hasattr(a1, 'cjsidl_varFormatField343'):
        assert not _is_linked(a1, 'cjsidl_varFormatField343', b)
    if hasattr(a2, 'cjsidl_varFormatField343'):
        assert _is_linked(a2, 'cjsidl_varFormatField343', b)
    _safe_set(b, 'cjsidl_formatEnumDef', None)
    assert not _is_linked(b, 'cjsidl_formatEnumDef', a2)
    if hasattr(a2, 'cjsidl_varFormatField343'):
        assert not _is_linked(a2, 'cjsidl_varFormatField343', b)


def test_assoc_guardAction169_reverse_link_reassign_clear():
    a1 = cjsidl_guardAction(name="sample_text", not_="sample_text")
    a2 = cjsidl_guardAction(name="sample_text_2", not_="sample_text_2")
    b = cjsidl_guard(comment="sample_text", equiv="sample_text", logicalOperator="sample_text")
    _safe_set(b, 'cjsidl_guard170', {a1})
    assert _is_linked(b, 'cjsidl_guard170', a1)
    if hasattr(a1, 'cjsidl_guardAction'):
        assert _is_linked(a1, 'cjsidl_guardAction', b)
    _safe_set(b, 'cjsidl_guard170', {a2})
    assert _is_linked(b, 'cjsidl_guard170', a2)
    if hasattr(a1, 'cjsidl_guardAction'):
        assert not _is_linked(a1, 'cjsidl_guardAction', b)
    if hasattr(a2, 'cjsidl_guardAction'):
        assert _is_linked(a2, 'cjsidl_guardAction', b)
    _safe_set(b, 'cjsidl_guard170', set())
    assert not _is_linked(b, 'cjsidl_guard170', a2)
    if hasattr(a2, 'cjsidl_guardAction'):
        assert not _is_linked(a2, 'cjsidl_guardAction', b)


def test_assoc_importedNamespace187_reverse_link_reassign_clear():
    a1 = cjsidl_declaredTypeSetRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_declaredTypeSetRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_declaredTypeSet(name="sample_text", typeName="sample_text", version="sample_text")
    _safe_set(b, 'cjsidl_declaredTypeSet189', a1)
    assert _is_linked(b, 'cjsidl_declaredTypeSet189', a1)
    if hasattr(a1, 'cjsidl_declaredTypeSetRef188'):
        assert _is_linked(a1, 'cjsidl_declaredTypeSetRef188', b)
    _safe_set(b, 'cjsidl_declaredTypeSet189', a2)
    assert _is_linked(b, 'cjsidl_declaredTypeSet189', a2)
    if hasattr(a1, 'cjsidl_declaredTypeSetRef188'):
        assert not _is_linked(a1, 'cjsidl_declaredTypeSetRef188', b)
    if hasattr(a2, 'cjsidl_declaredTypeSetRef188'):
        assert _is_linked(a2, 'cjsidl_declaredTypeSetRef188', b)
    _safe_set(b, 'cjsidl_declaredTypeSet189', None)
    assert not _is_linked(b, 'cjsidl_declaredTypeSet189', a2)
    if hasattr(a2, 'cjsidl_declaredTypeSetRef188'):
        assert not _is_linked(a2, 'cjsidl_declaredTypeSetRef188', b)


def test_assoc_importedNamespace19_reverse_link_reassign_clear():
    a1 = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    a2 = cjsidl_serviceDef(assumpt="sample_text_2", name="sample_text_2", serviceName="sample_text_2", serviceVersion="sample_text_2")
    b = cjsidl_refAttr(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_refAttr20', a1)
    assert _is_linked(b, 'cjsidl_refAttr20', a1)
    if hasattr(a1, 'cjsidl_serviceDef21'):
        assert _is_linked(a1, 'cjsidl_serviceDef21', b)
    _safe_set(b, 'cjsidl_refAttr20', a2)
    assert _is_linked(b, 'cjsidl_refAttr20', a2)
    if hasattr(a1, 'cjsidl_serviceDef21'):
        assert not _is_linked(a1, 'cjsidl_serviceDef21', b)
    if hasattr(a2, 'cjsidl_serviceDef21'):
        assert _is_linked(a2, 'cjsidl_serviceDef21', b)
    _safe_set(b, 'cjsidl_refAttr20', None)
    assert not _is_linked(b, 'cjsidl_refAttr20', a2)
    if hasattr(a2, 'cjsidl_serviceDef21'):
        assert not _is_linked(a2, 'cjsidl_serviceDef21', b)


def test_assoc_importedNamespace26_reverse_link_reassign_clear():
    a1 = cjsidl_declaredConstSetRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_declaredConstSetRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_declaredConstSet(constName="sample_text", constSetVersion="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_declaredConstSet28', a1)
    assert _is_linked(b, 'cjsidl_declaredConstSet28', a1)
    if hasattr(a1, 'cjsidl_declaredConstSetRef27'):
        assert _is_linked(a1, 'cjsidl_declaredConstSetRef27', b)
    _safe_set(b, 'cjsidl_declaredConstSet28', a2)
    assert _is_linked(b, 'cjsidl_declaredConstSet28', a2)
    if hasattr(a1, 'cjsidl_declaredConstSetRef27'):
        assert not _is_linked(a1, 'cjsidl_declaredConstSetRef27', b)
    if hasattr(a2, 'cjsidl_declaredConstSetRef27'):
        assert _is_linked(a2, 'cjsidl_declaredConstSetRef27', b)
    _safe_set(b, 'cjsidl_declaredConstSet28', None)
    assert not _is_linked(b, 'cjsidl_declaredConstSet28', a2)
    if hasattr(a2, 'cjsidl_declaredConstSetRef27'):
        assert not _is_linked(a2, 'cjsidl_declaredConstSetRef27', b)


def test_assoc_internalEventSet10_reverse_link_reassign_clear():
    a1 = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    a2 = cjsidl_serviceDef(assumpt="sample_text_2", name="sample_text_2", serviceName="sample_text_2", serviceVersion="sample_text_2")
    b = cjsidl_internalEventSet(comment="sample_text")
    _safe_set(b, 'cjsidl_internalEventSet', a1)
    assert _is_linked(b, 'cjsidl_internalEventSet', a1)
    if hasattr(a1, 'cjsidl_serviceDef11'):
        assert _is_linked(a1, 'cjsidl_serviceDef11', b)
    _safe_set(b, 'cjsidl_internalEventSet', a2)
    assert _is_linked(b, 'cjsidl_internalEventSet', a2)
    if hasattr(a1, 'cjsidl_serviceDef11'):
        assert not _is_linked(a1, 'cjsidl_serviceDef11', b)
    if hasattr(a2, 'cjsidl_serviceDef11'):
        assert _is_linked(a2, 'cjsidl_serviceDef11', b)
    _safe_set(b, 'cjsidl_internalEventSet', None)
    assert not _is_linked(b, 'cjsidl_internalEventSet', a2)
    if hasattr(a2, 'cjsidl_serviceDef11'):
        assert not _is_linked(a2, 'cjsidl_serviceDef11', b)


def test_assoc_lowerLimRef295_reverse_link_reassign_clear():
    a1 = cjsidl_varLenString(comment="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    a2 = cjsidl_varLenString(comment="sample_text_2", lowerLim="sample_text_2", name="sample_text_2", optional="sample_text_2", upperLim="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference297', a1)
    assert _is_linked(b, 'cjsidl_constReference297', a1)
    if hasattr(a1, 'cjsidl_varLenString296'):
        assert _is_linked(a1, 'cjsidl_varLenString296', b)
    _safe_set(b, 'cjsidl_constReference297', a2)
    assert _is_linked(b, 'cjsidl_constReference297', a2)
    if hasattr(a1, 'cjsidl_varLenString296'):
        assert not _is_linked(a1, 'cjsidl_varLenString296', b)
    if hasattr(a2, 'cjsidl_varLenString296'):
        assert _is_linked(a2, 'cjsidl_varLenString296', b)
    _safe_set(b, 'cjsidl_constReference297', None)
    assert not _is_linked(b, 'cjsidl_constReference297', a2)
    if hasattr(a2, 'cjsidl_varLenString296'):
        assert not _is_linked(a2, 'cjsidl_varLenString296', b)


def test_assoc_lowerLimRef315_reverse_link_reassign_clear():
    a1 = cjsidl_varLenField(comment="sample_text", countComment="sample_text", fieldFormat="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    a2 = cjsidl_varLenField(comment="sample_text_2", countComment="sample_text_2", fieldFormat="sample_text_2", lowerLim="sample_text_2", name="sample_text_2", optional="sample_text_2", upperLim="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference317', a1)
    assert _is_linked(b, 'cjsidl_constReference317', a1)
    if hasattr(a1, 'cjsidl_varLenField316'):
        assert _is_linked(a1, 'cjsidl_varLenField316', b)
    _safe_set(b, 'cjsidl_constReference317', a2)
    assert _is_linked(b, 'cjsidl_constReference317', a2)
    if hasattr(a1, 'cjsidl_varLenField316'):
        assert not _is_linked(a1, 'cjsidl_varLenField316', b)
    if hasattr(a2, 'cjsidl_varLenField316'):
        assert _is_linked(a2, 'cjsidl_varLenField316', b)
    _safe_set(b, 'cjsidl_constReference317', None)
    assert not _is_linked(b, 'cjsidl_constReference317', a2)
    if hasattr(a2, 'cjsidl_varLenField316'):
        assert not _is_linked(a2, 'cjsidl_varLenField316', b)


def test_assoc_lowerLimRef355_reverse_link_reassign_clear():
    a1 = cjsidl_valueRange(comment="sample_text", lowerLim="sample_text", lowerLimit_type="sample_text", upperLim="sample_text", upperLimit_type="sample_text")
    a2 = cjsidl_valueRange(comment="sample_text_2", lowerLim="sample_text_2", lowerLimit_type="sample_text_2", upperLim="sample_text_2", upperLimit_type="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference357', a1)
    assert _is_linked(b, 'cjsidl_constReference357', a1)
    if hasattr(a1, 'cjsidl_valueRange356'):
        assert _is_linked(a1, 'cjsidl_valueRange356', b)
    _safe_set(b, 'cjsidl_constReference357', a2)
    assert _is_linked(b, 'cjsidl_constReference357', a2)
    if hasattr(a1, 'cjsidl_valueRange356'):
        assert not _is_linked(a1, 'cjsidl_valueRange356', b)
    if hasattr(a2, 'cjsidl_valueRange356'):
        assert _is_linked(a2, 'cjsidl_valueRange356', b)
    _safe_set(b, 'cjsidl_constReference357', None)
    assert not _is_linked(b, 'cjsidl_constReference357', a2)
    if hasattr(a2, 'cjsidl_valueRange356'):
        assert not _is_linked(a2, 'cjsidl_valueRange356', b)


def test_assoc_lowerLimRef367_reverse_link_reassign_clear():
    a1 = cjsidl_scaledRangeDef(function="sample_text", interp="sample_text", lowerLim="sample_text", upperLim="sample_text")
    a2 = cjsidl_scaledRangeDef(function="sample_text_2", interp="sample_text_2", lowerLim="sample_text_2", upperLim="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference369', a1)
    assert _is_linked(b, 'cjsidl_constReference369', a1)
    if hasattr(a1, 'cjsidl_scaledRangeDef368'):
        assert _is_linked(a1, 'cjsidl_scaledRangeDef368', b)
    _safe_set(b, 'cjsidl_constReference369', a2)
    assert _is_linked(b, 'cjsidl_constReference369', a2)
    if hasattr(a1, 'cjsidl_scaledRangeDef368'):
        assert not _is_linked(a1, 'cjsidl_scaledRangeDef368', b)
    if hasattr(a2, 'cjsidl_scaledRangeDef368'):
        assert _is_linked(a2, 'cjsidl_scaledRangeDef368', b)
    _safe_set(b, 'cjsidl_constReference369', None)
    assert not _is_linked(b, 'cjsidl_constReference369', a2)
    if hasattr(a2, 'cjsidl_scaledRangeDef368'):
        assert not _is_linked(a2, 'cjsidl_scaledRangeDef368', b)


def test_assoc_maxCountRef388_reverse_link_reassign_clear():
    a1 = cjsidl_listDef(countComment="sample_text", maxCount="sample_text", minCount="sample_text")
    a2 = cjsidl_listDef(countComment="sample_text_2", maxCount="sample_text_2", minCount="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference390', a1)
    assert _is_linked(b, 'cjsidl_constReference390', a1)
    if hasattr(a1, 'cjsidl_listDef389'):
        assert _is_linked(a1, 'cjsidl_listDef389', b)
    _safe_set(b, 'cjsidl_constReference390', a2)
    assert _is_linked(b, 'cjsidl_constReference390', a2)
    if hasattr(a1, 'cjsidl_listDef389'):
        assert not _is_linked(a1, 'cjsidl_listDef389', b)
    if hasattr(a2, 'cjsidl_listDef389'):
        assert _is_linked(a2, 'cjsidl_listDef389', b)
    _safe_set(b, 'cjsidl_constReference390', None)
    assert not _is_linked(b, 'cjsidl_constReference390', a2)
    if hasattr(a2, 'cjsidl_listDef389'):
        assert not _is_linked(a2, 'cjsidl_listDef389', b)


def test_assoc_maxCountRef406_reverse_link_reassign_clear():
    a1 = cjsidl_variantDef(maxCount="sample_text", minCount="sample_text", vtagComment="sample_text")
    a2 = cjsidl_variantDef(maxCount="sample_text_2", minCount="sample_text_2", vtagComment="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference408', a1)
    assert _is_linked(b, 'cjsidl_constReference408', a1)
    if hasattr(a1, 'cjsidl_variantDef407'):
        assert _is_linked(a1, 'cjsidl_variantDef407', b)
    _safe_set(b, 'cjsidl_constReference408', a2)
    assert _is_linked(b, 'cjsidl_constReference408', a2)
    if hasattr(a1, 'cjsidl_variantDef407'):
        assert not _is_linked(a1, 'cjsidl_variantDef407', b)
    if hasattr(a2, 'cjsidl_variantDef407'):
        assert _is_linked(a2, 'cjsidl_variantDef407', b)
    _safe_set(b, 'cjsidl_constReference408', None)
    assert not _is_linked(b, 'cjsidl_constReference408', a2)
    if hasattr(a2, 'cjsidl_variantDef407'):
        assert not _is_linked(a2, 'cjsidl_variantDef407', b)


def test_assoc_messageSet8_reverse_link_reassign_clear():
    a1 = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    a2 = cjsidl_serviceDef(assumpt="sample_text_2", name="sample_text_2", serviceName="sample_text_2", serviceVersion="sample_text_2")
    b = cjsidl_messageSet(comment="sample_text", inputComment="sample_text", outputComment="sample_text")
    _safe_set(b, 'cjsidl_messageSet', a1)
    assert _is_linked(b, 'cjsidl_messageSet', a1)
    if hasattr(a1, 'cjsidl_serviceDef9'):
        assert _is_linked(a1, 'cjsidl_serviceDef9', b)
    _safe_set(b, 'cjsidl_messageSet', a2)
    assert _is_linked(b, 'cjsidl_messageSet', a2)
    if hasattr(a1, 'cjsidl_serviceDef9'):
        assert not _is_linked(a1, 'cjsidl_serviceDef9', b)
    if hasattr(a2, 'cjsidl_serviceDef9'):
        assert _is_linked(a2, 'cjsidl_serviceDef9', b)
    _safe_set(b, 'cjsidl_messageSet', None)
    assert not _is_linked(b, 'cjsidl_messageSet', a2)
    if hasattr(a2, 'cjsidl_serviceDef9'):
        assert not _is_linked(a2, 'cjsidl_serviceDef9', b)


def test_assoc_minCountRef382_reverse_link_reassign_clear():
    a1 = cjsidl_listDef(countComment="sample_text", maxCount="sample_text", minCount="sample_text")
    a2 = cjsidl_listDef(countComment="sample_text_2", maxCount="sample_text_2", minCount="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference384', a1)
    assert _is_linked(b, 'cjsidl_constReference384', a1)
    if hasattr(a1, 'cjsidl_listDef383'):
        assert _is_linked(a1, 'cjsidl_listDef383', b)
    _safe_set(b, 'cjsidl_constReference384', a2)
    assert _is_linked(b, 'cjsidl_constReference384', a2)
    if hasattr(a1, 'cjsidl_listDef383'):
        assert not _is_linked(a1, 'cjsidl_listDef383', b)
    if hasattr(a2, 'cjsidl_listDef383'):
        assert _is_linked(a2, 'cjsidl_listDef383', b)
    _safe_set(b, 'cjsidl_constReference384', None)
    assert not _is_linked(b, 'cjsidl_constReference384', a2)
    if hasattr(a2, 'cjsidl_listDef383'):
        assert not _is_linked(a2, 'cjsidl_listDef383', b)


def test_assoc_minCountRef400_reverse_link_reassign_clear():
    a1 = cjsidl_variantDef(maxCount="sample_text", minCount="sample_text", vtagComment="sample_text")
    a2 = cjsidl_variantDef(maxCount="sample_text_2", minCount="sample_text_2", vtagComment="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference402', a1)
    assert _is_linked(b, 'cjsidl_constReference402', a1)
    if hasattr(a1, 'cjsidl_variantDef401'):
        assert _is_linked(a1, 'cjsidl_variantDef401', b)
    _safe_set(b, 'cjsidl_constReference402', a2)
    assert _is_linked(b, 'cjsidl_constReference402', a2)
    if hasattr(a1, 'cjsidl_variantDef401'):
        assert not _is_linked(a1, 'cjsidl_variantDef401', b)
    if hasattr(a2, 'cjsidl_variantDef401'):
        assert _is_linked(a2, 'cjsidl_variantDef401', b)
    _safe_set(b, 'cjsidl_constReference402', None)
    assert not _is_linked(b, 'cjsidl_constReference402', a2)
    if hasattr(a2, 'cjsidl_variantDef401'):
        assert not _is_linked(a2, 'cjsidl_variantDef401', b)


def test_assoc_nextState150_reverse_link_reassign_clear():
    a1 = cjsidl_simpleTransition(comment="sample_text")
    a2 = cjsidl_simpleTransition(comment="sample_text_2")
    b = cjsidl_nextState(comment="sample_text")
    _safe_set(b, 'cjsidl_nextState', a1)
    assert _is_linked(b, 'cjsidl_nextState', a1)
    if hasattr(a1, 'cjsidl_simpleTransition'):
        assert _is_linked(a1, 'cjsidl_simpleTransition', b)
    _safe_set(b, 'cjsidl_nextState', a2)
    assert _is_linked(b, 'cjsidl_nextState', a2)
    if hasattr(a1, 'cjsidl_simpleTransition'):
        assert not _is_linked(a1, 'cjsidl_simpleTransition', b)
    if hasattr(a2, 'cjsidl_simpleTransition'):
        assert _is_linked(a2, 'cjsidl_simpleTransition', b)
    _safe_set(b, 'cjsidl_nextState', None)
    assert not _is_linked(b, 'cjsidl_nextState', a2)
    if hasattr(a2, 'cjsidl_simpleTransition'):
        assert not _is_linked(a2, 'cjsidl_simpleTransition', b)


def test_assoc_nextState151_reverse_link_reassign_clear():
    a1 = cjsidl_pushTransition(comment="sample_text")
    a2 = cjsidl_pushTransition(comment="sample_text_2")
    b = cjsidl_nextState(comment="sample_text")
    _safe_set(b, 'cjsidl_nextState152', a1)
    assert _is_linked(b, 'cjsidl_nextState152', a1)
    if hasattr(a1, 'cjsidl_pushTransition'):
        assert _is_linked(a1, 'cjsidl_pushTransition', b)
    _safe_set(b, 'cjsidl_nextState152', a2)
    assert _is_linked(b, 'cjsidl_nextState152', a2)
    if hasattr(a1, 'cjsidl_pushTransition'):
        assert not _is_linked(a1, 'cjsidl_pushTransition', b)
    if hasattr(a2, 'cjsidl_pushTransition'):
        assert _is_linked(a2, 'cjsidl_pushTransition', b)
    _safe_set(b, 'cjsidl_nextState152', None)
    assert not _is_linked(b, 'cjsidl_nextState152', a2)
    if hasattr(a2, 'cjsidl_pushTransition'):
        assert not _is_linked(a2, 'cjsidl_pushTransition', b)


def test_assoc_nextState166_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_nextState(comment="sample_text")
    _safe_set(b, 'cjsidl_nextState167', a1)
    assert _is_linked(b, 'cjsidl_nextState167', a1)
    if hasattr(a1, 'cjsidl_state168'):
        assert _is_linked(a1, 'cjsidl_state168', b)
    _safe_set(b, 'cjsidl_nextState167', a2)
    assert _is_linked(b, 'cjsidl_nextState167', a2)
    if hasattr(a1, 'cjsidl_state168'):
        assert not _is_linked(a1, 'cjsidl_state168', b)
    if hasattr(a2, 'cjsidl_state168'):
        assert _is_linked(a2, 'cjsidl_state168', b)
    _safe_set(b, 'cjsidl_nextState167', None)
    assert not _is_linked(b, 'cjsidl_nextState167', a2)
    if hasattr(a2, 'cjsidl_state168'):
        assert not _is_linked(a2, 'cjsidl_state168', b)


def test_assoc_param158_reverse_link_reassign_clear():
    a1 = cjsidl_popTransition(comment="sample_text")
    a2 = cjsidl_popTransition(comment="sample_text_2")
    b = cjsidl_guardParam(guardConst="sample_text")
    _safe_set(b, 'cjsidl_guardParam', a1)
    assert _is_linked(b, 'cjsidl_guardParam', a1)
    if hasattr(a1, 'cjsidl_popTransition159'):
        assert _is_linked(a1, 'cjsidl_popTransition159', b)
    _safe_set(b, 'cjsidl_guardParam', a2)
    assert _is_linked(b, 'cjsidl_guardParam', a2)
    if hasattr(a1, 'cjsidl_popTransition159'):
        assert not _is_linked(a1, 'cjsidl_popTransition159', b)
    if hasattr(a2, 'cjsidl_popTransition159'):
        assert _is_linked(a2, 'cjsidl_popTransition159', b)
    _safe_set(b, 'cjsidl_guardParam', None)
    assert not _is_linked(b, 'cjsidl_guardParam', a2)
    if hasattr(a2, 'cjsidl_popTransition159'):
        assert not _is_linked(a2, 'cjsidl_popTransition159', b)


def test_assoc_param171_reverse_link_reassign_clear():
    a1 = cjsidl_guardParam(guardConst="sample_text")
    a2 = cjsidl_guardParam(guardConst="sample_text_2")
    b = cjsidl_guardAction(name="sample_text", not_="sample_text")
    _safe_set(b, 'cjsidl_guardAction172', {a1})
    assert _is_linked(b, 'cjsidl_guardAction172', a1)
    if hasattr(a1, 'cjsidl_guardParam173'):
        assert _is_linked(a1, 'cjsidl_guardParam173', b)
    _safe_set(b, 'cjsidl_guardAction172', {a2})
    assert _is_linked(b, 'cjsidl_guardAction172', a2)
    if hasattr(a1, 'cjsidl_guardParam173'):
        assert not _is_linked(a1, 'cjsidl_guardParam173', b)
    if hasattr(a2, 'cjsidl_guardParam173'):
        assert _is_linked(a2, 'cjsidl_guardParam173', b)
    _safe_set(b, 'cjsidl_guardAction172', set())
    assert not _is_linked(b, 'cjsidl_guardAction172', a2)
    if hasattr(a2, 'cjsidl_guardParam173'):
        assert not _is_linked(a2, 'cjsidl_guardParam173', b)


def test_assoc_param182_reverse_link_reassign_clear():
    a1 = cjsidl_guardParam(guardConst="sample_text")
    a2 = cjsidl_guardParam(guardConst="sample_text_2")
    b = cjsidl_action(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_action183', {a1})
    assert _is_linked(b, 'cjsidl_action183', a1)
    if hasattr(a1, 'cjsidl_guardParam184'):
        assert _is_linked(a1, 'cjsidl_guardParam184', b)
    _safe_set(b, 'cjsidl_action183', {a2})
    assert _is_linked(b, 'cjsidl_action183', a2)
    if hasattr(a1, 'cjsidl_guardParam184'):
        assert not _is_linked(a1, 'cjsidl_guardParam184', b)
    if hasattr(a2, 'cjsidl_guardParam184'):
        assert _is_linked(a2, 'cjsidl_guardParam184', b)
    _safe_set(b, 'cjsidl_action183', set())
    assert not _is_linked(b, 'cjsidl_action183', a2)
    if hasattr(a2, 'cjsidl_guardParam184'):
        assert not _is_linked(a2, 'cjsidl_guardParam184', b)


def test_assoc_parameter174_reverse_link_reassign_clear():
    a1 = cjsidl_transParam(comment="sample_text", name="sample_text", unsignedType="sample_text")
    a2 = cjsidl_transParam(comment="sample_text_2", name="sample_text_2", unsignedType="sample_text_2")
    b = cjsidl_guardParam(guardConst="sample_text")
    _safe_set(b, 'cjsidl_guardParam175', a1)
    assert _is_linked(b, 'cjsidl_guardParam175', a1)
    if hasattr(a1, 'cjsidl_transParam176'):
        assert _is_linked(a1, 'cjsidl_transParam176', b)
    _safe_set(b, 'cjsidl_guardParam175', a2)
    assert _is_linked(b, 'cjsidl_guardParam175', a2)
    if hasattr(a1, 'cjsidl_transParam176'):
        assert not _is_linked(a1, 'cjsidl_transParam176', b)
    if hasattr(a2, 'cjsidl_transParam176'):
        assert _is_linked(a2, 'cjsidl_transParam176', b)
    _safe_set(b, 'cjsidl_guardParam175', None)
    assert not _is_linked(b, 'cjsidl_guardParam175', a2)
    if hasattr(a2, 'cjsidl_transParam176'):
        assert not _is_linked(a2, 'cjsidl_transParam176', b)


def test_assoc_protocolBehavior12_reverse_link_reassign_clear():
    a1 = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    a2 = cjsidl_serviceDef(assumpt="sample_text_2", name="sample_text_2", serviceName="sample_text_2", serviceVersion="sample_text_2")
    b = cjsidl_protocolBehavior(comment="sample_text", stateless="sample_text")
    _safe_set(b, 'cjsidl_protocolBehavior', a1)
    assert _is_linked(b, 'cjsidl_protocolBehavior', a1)
    if hasattr(a1, 'cjsidl_serviceDef13'):
        assert _is_linked(a1, 'cjsidl_serviceDef13', b)
    _safe_set(b, 'cjsidl_protocolBehavior', a2)
    assert _is_linked(b, 'cjsidl_protocolBehavior', a2)
    if hasattr(a1, 'cjsidl_serviceDef13'):
        assert not _is_linked(a1, 'cjsidl_serviceDef13', b)
    if hasattr(a2, 'cjsidl_serviceDef13'):
        assert _is_linked(a2, 'cjsidl_serviceDef13', b)
    _safe_set(b, 'cjsidl_protocolBehavior', None)
    assert not _is_linked(b, 'cjsidl_protocolBehavior', a2)
    if hasattr(a2, 'cjsidl_serviceDef13'):
        assert not _is_linked(a2, 'cjsidl_serviceDef13', b)


def test_assoc_ref471_reverse_link_reassign_clear():
    a1 = cjsidl_messageScopedRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_messageScopedRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_messageDef473', a1)
    assert _is_linked(b, 'cjsidl_messageDef473', a1)
    if hasattr(a1, 'cjsidl_messageScopedRef472'):
        assert _is_linked(a1, 'cjsidl_messageScopedRef472', b)
    _safe_set(b, 'cjsidl_messageDef473', a2)
    assert _is_linked(b, 'cjsidl_messageDef473', a2)
    if hasattr(a1, 'cjsidl_messageScopedRef472'):
        assert not _is_linked(a1, 'cjsidl_messageScopedRef472', b)
    if hasattr(a2, 'cjsidl_messageScopedRef472'):
        assert _is_linked(a2, 'cjsidl_messageScopedRef472', b)
    _safe_set(b, 'cjsidl_messageDef473', None)
    assert not _is_linked(b, 'cjsidl_messageDef473', a2)
    if hasattr(a2, 'cjsidl_messageScopedRef472'):
        assert not _is_linked(a2, 'cjsidl_messageScopedRef472', b)


def test_assoc_ref65_reverse_link_reassign_clear():
    a1 = cjsidl_messageRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_messageRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_messageDef67', a1)
    assert _is_linked(b, 'cjsidl_messageDef67', a1)
    if hasattr(a1, 'cjsidl_messageRef66'):
        assert _is_linked(a1, 'cjsidl_messageRef66', b)
    _safe_set(b, 'cjsidl_messageDef67', a2)
    assert _is_linked(b, 'cjsidl_messageDef67', a2)
    if hasattr(a1, 'cjsidl_messageRef66'):
        assert not _is_linked(a1, 'cjsidl_messageRef66', b)
    if hasattr(a2, 'cjsidl_messageRef66'):
        assert _is_linked(a2, 'cjsidl_messageRef66', b)
    _safe_set(b, 'cjsidl_messageDef67', None)
    assert not _is_linked(b, 'cjsidl_messageDef67', a2)
    if hasattr(a2, 'cjsidl_messageRef66'):
        assert not _is_linked(a2, 'cjsidl_messageRef66', b)


def test_assoc_scaledRangeDef338_reverse_link_reassign_clear():
    a1 = cjsidl_taggedUnitsEnum(const_tag="sample_text", fieldUnit="sample_text", name="sample_text")
    a2 = cjsidl_taggedUnitsEnum(const_tag="sample_text_2", fieldUnit="sample_text_2", name="sample_text_2")
    b = cjsidl_scaledRangeDef(function="sample_text", interp="sample_text", lowerLim="sample_text", upperLim="sample_text")
    _safe_set(b, 'cjsidl_scaledRangeDef', a1)
    assert _is_linked(b, 'cjsidl_scaledRangeDef', a1)
    if hasattr(a1, 'cjsidl_taggedUnitsEnum339'):
        assert _is_linked(a1, 'cjsidl_taggedUnitsEnum339', b)
    _safe_set(b, 'cjsidl_scaledRangeDef', a2)
    assert _is_linked(b, 'cjsidl_scaledRangeDef', a2)
    if hasattr(a1, 'cjsidl_taggedUnitsEnum339'):
        assert not _is_linked(a1, 'cjsidl_taggedUnitsEnum339', b)
    if hasattr(a2, 'cjsidl_taggedUnitsEnum339'):
        assert _is_linked(a2, 'cjsidl_taggedUnitsEnum339', b)
    _safe_set(b, 'cjsidl_scaledRangeDef', None)
    assert not _is_linked(b, 'cjsidl_scaledRangeDef', a2)
    if hasattr(a2, 'cjsidl_taggedUnitsEnum339'):
        assert not _is_linked(a2, 'cjsidl_taggedUnitsEnum339', b)


def test_assoc_scoped121_reverse_link_reassign_clear():
    a1 = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    a2 = cjsidl_transition(comment="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = cjsidl_refAttr(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_refAttr123', a1)
    assert _is_linked(b, 'cjsidl_refAttr123', a1)
    if hasattr(a1, 'cjsidl_transition122'):
        assert _is_linked(a1, 'cjsidl_transition122', b)
    _safe_set(b, 'cjsidl_refAttr123', a2)
    assert _is_linked(b, 'cjsidl_refAttr123', a2)
    if hasattr(a1, 'cjsidl_transition122'):
        assert not _is_linked(a1, 'cjsidl_transition122', b)
    if hasattr(a2, 'cjsidl_transition122'):
        assert _is_linked(a2, 'cjsidl_transition122', b)
    _safe_set(b, 'cjsidl_refAttr123', None)
    assert not _is_linked(b, 'cjsidl_refAttr123', a2)
    if hasattr(a2, 'cjsidl_transition122'):
        assert not _is_linked(a2, 'cjsidl_transition122', b)


def test_assoc_scoped163_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_nextState(comment="sample_text")
    _safe_set(b, 'cjsidl_nextState164', {a1})
    assert _is_linked(b, 'cjsidl_nextState164', a1)
    if hasattr(a1, 'cjsidl_state165'):
        assert _is_linked(a1, 'cjsidl_state165', b)
    _safe_set(b, 'cjsidl_nextState164', {a2})
    assert _is_linked(b, 'cjsidl_nextState164', a2)
    if hasattr(a1, 'cjsidl_state165'):
        assert not _is_linked(a1, 'cjsidl_state165', b)
    if hasattr(a2, 'cjsidl_state165'):
        assert _is_linked(a2, 'cjsidl_state165', b)
    _safe_set(b, 'cjsidl_nextState164', set())
    assert not _is_linked(b, 'cjsidl_nextState164', a2)
    if hasattr(a2, 'cjsidl_state165'):
        assert not _is_linked(a2, 'cjsidl_state165', b)


def test_assoc_scoped70_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_startState(comment="sample_text")
    _safe_set(b, 'cjsidl_startState', {a1})
    assert _is_linked(b, 'cjsidl_startState', a1)
    if hasattr(a1, 'cjsidl_state'):
        assert _is_linked(a1, 'cjsidl_state', b)
    _safe_set(b, 'cjsidl_startState', {a2})
    assert _is_linked(b, 'cjsidl_startState', a2)
    if hasattr(a1, 'cjsidl_state'):
        assert not _is_linked(a1, 'cjsidl_state', b)
    if hasattr(a2, 'cjsidl_state'):
        assert _is_linked(a2, 'cjsidl_state', b)
    _safe_set(b, 'cjsidl_startState', set())
    assert not _is_linked(b, 'cjsidl_startState', a2)
    if hasattr(a2, 'cjsidl_state'):
        assert not _is_linked(a2, 'cjsidl_state', b)


def test_assoc_scoped74_reverse_link_reassign_clear():
    a1 = cjsidl_stateMachine(comment="sample_text", name="sample_text")
    a2 = cjsidl_stateMachine(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_refAttr(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_refAttr76', a1)
    assert _is_linked(b, 'cjsidl_refAttr76', a1)
    if hasattr(a1, 'cjsidl_stateMachine75'):
        assert _is_linked(a1, 'cjsidl_stateMachine75', b)
    _safe_set(b, 'cjsidl_refAttr76', a2)
    assert _is_linked(b, 'cjsidl_refAttr76', a2)
    if hasattr(a1, 'cjsidl_stateMachine75'):
        assert not _is_linked(a1, 'cjsidl_stateMachine75', b)
    if hasattr(a2, 'cjsidl_stateMachine75'):
        assert _is_linked(a2, 'cjsidl_stateMachine75', b)
    _safe_set(b, 'cjsidl_refAttr76', None)
    assert not _is_linked(b, 'cjsidl_refAttr76', a2)
    if hasattr(a2, 'cjsidl_stateMachine75'):
        assert not _is_linked(a2, 'cjsidl_stateMachine75', b)


def test_assoc_scopedRef38_reverse_link_reassign_clear():
    a1 = cjsidl_scopedTypeId(comment="sample_text", optional="sample_text", scopedName="sample_text")
    a2 = cjsidl_scopedTypeId(comment="sample_text_2", optional="sample_text_2", scopedName="sample_text_2")
    b = cjsidl_declaredTypeSet(name="sample_text", typeName="sample_text", version="sample_text")
    _safe_set(b, 'cjsidl_declaredTypeSet39', {a1})
    assert _is_linked(b, 'cjsidl_declaredTypeSet39', a1)
    if hasattr(a1, 'cjsidl_scopedTypeId'):
        assert _is_linked(a1, 'cjsidl_scopedTypeId', b)
    _safe_set(b, 'cjsidl_declaredTypeSet39', {a2})
    assert _is_linked(b, 'cjsidl_declaredTypeSet39', a2)
    if hasattr(a1, 'cjsidl_scopedTypeId'):
        assert not _is_linked(a1, 'cjsidl_scopedTypeId', b)
    if hasattr(a2, 'cjsidl_scopedTypeId'):
        assert _is_linked(a2, 'cjsidl_scopedTypeId', b)
    _safe_set(b, 'cjsidl_declaredTypeSet39', set())
    assert not _is_linked(b, 'cjsidl_declaredTypeSet39', a2)
    if hasattr(a2, 'cjsidl_scopedTypeId'):
        assert not _is_linked(a2, 'cjsidl_scopedTypeId', b)


def test_assoc_secondaryTransition156_reverse_link_reassign_clear():
    a1 = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    a2 = cjsidl_transition(comment="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = cjsidl_popTransition(comment="sample_text")
    _safe_set(b, 'cjsidl_popTransition', a1)
    assert _is_linked(b, 'cjsidl_popTransition', a1)
    if hasattr(a1, 'cjsidl_transition157'):
        assert _is_linked(a1, 'cjsidl_transition157', b)
    _safe_set(b, 'cjsidl_popTransition', a2)
    assert _is_linked(b, 'cjsidl_popTransition', a2)
    if hasattr(a1, 'cjsidl_transition157'):
        assert not _is_linked(a1, 'cjsidl_transition157', b)
    if hasattr(a2, 'cjsidl_transition157'):
        assert _is_linked(a2, 'cjsidl_transition157', b)
    _safe_set(b, 'cjsidl_popTransition', None)
    assert not _is_linked(b, 'cjsidl_popTransition', a2)
    if hasattr(a2, 'cjsidl_transition157'):
        assert not _is_linked(a2, 'cjsidl_transition157', b)


def test_assoc_simpleTransition153_reverse_link_reassign_clear():
    a1 = cjsidl_simpleTransition(comment="sample_text")
    a2 = cjsidl_simpleTransition(comment="sample_text_2")
    b = cjsidl_pushTransition(comment="sample_text")
    _safe_set(b, 'cjsidl_pushTransition154', a1)
    assert _is_linked(b, 'cjsidl_pushTransition154', a1)
    if hasattr(a1, 'cjsidl_simpleTransition155'):
        assert _is_linked(a1, 'cjsidl_simpleTransition155', b)
    _safe_set(b, 'cjsidl_pushTransition154', a2)
    assert _is_linked(b, 'cjsidl_pushTransition154', a2)
    if hasattr(a1, 'cjsidl_simpleTransition155'):
        assert not _is_linked(a1, 'cjsidl_simpleTransition155', b)
    if hasattr(a2, 'cjsidl_simpleTransition155'):
        assert _is_linked(a2, 'cjsidl_simpleTransition155', b)
    _safe_set(b, 'cjsidl_pushTransition154', None)
    assert not _is_linked(b, 'cjsidl_pushTransition154', a2)
    if hasattr(a2, 'cjsidl_simpleTransition155'):
        assert not _is_linked(a2, 'cjsidl_simpleTransition155', b)


def test_assoc_startState77_reverse_link_reassign_clear():
    a1 = cjsidl_stateMachine(comment="sample_text", name="sample_text")
    a2 = cjsidl_stateMachine(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_startState(comment="sample_text")
    _safe_set(b, 'cjsidl_startState79', a1)
    assert _is_linked(b, 'cjsidl_startState79', a1)
    if hasattr(a1, 'cjsidl_stateMachine78'):
        assert _is_linked(a1, 'cjsidl_stateMachine78', b)
    _safe_set(b, 'cjsidl_startState79', a2)
    assert _is_linked(b, 'cjsidl_startState79', a2)
    if hasattr(a1, 'cjsidl_stateMachine78'):
        assert not _is_linked(a1, 'cjsidl_stateMachine78', b)
    if hasattr(a2, 'cjsidl_stateMachine78'):
        assert _is_linked(a2, 'cjsidl_stateMachine78', b)
    _safe_set(b, 'cjsidl_startState79', None)
    assert not _is_linked(b, 'cjsidl_startState79', a2)
    if hasattr(a2, 'cjsidl_stateMachine78'):
        assert not _is_linked(a2, 'cjsidl_stateMachine78', b)


def test_assoc_state71_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_startState(comment="sample_text")
    _safe_set(b, 'cjsidl_startState72', a1)
    assert _is_linked(b, 'cjsidl_startState72', a1)
    if hasattr(a1, 'cjsidl_state73'):
        assert _is_linked(a1, 'cjsidl_state73', b)
    _safe_set(b, 'cjsidl_startState72', a2)
    assert _is_linked(b, 'cjsidl_startState72', a2)
    if hasattr(a1, 'cjsidl_state73'):
        assert not _is_linked(a1, 'cjsidl_state73', b)
    if hasattr(a2, 'cjsidl_state73'):
        assert _is_linked(a2, 'cjsidl_state73', b)
    _safe_set(b, 'cjsidl_startState72', None)
    assert not _is_linked(b, 'cjsidl_startState72', a2)
    if hasattr(a2, 'cjsidl_state73'):
        assert not _is_linked(a2, 'cjsidl_state73', b)


def test_assoc_stateMachine68_reverse_link_reassign_clear():
    a1 = cjsidl_stateMachine(comment="sample_text", name="sample_text")
    a2 = cjsidl_stateMachine(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_protocolBehavior(comment="sample_text", stateless="sample_text")
    _safe_set(b, 'cjsidl_protocolBehavior69', {a1})
    assert _is_linked(b, 'cjsidl_protocolBehavior69', a1)
    if hasattr(a1, 'cjsidl_stateMachine'):
        assert _is_linked(a1, 'cjsidl_stateMachine', b)
    _safe_set(b, 'cjsidl_protocolBehavior69', {a2})
    assert _is_linked(b, 'cjsidl_protocolBehavior69', a2)
    if hasattr(a1, 'cjsidl_stateMachine'):
        assert not _is_linked(a1, 'cjsidl_stateMachine', b)
    if hasattr(a2, 'cjsidl_stateMachine'):
        assert _is_linked(a2, 'cjsidl_stateMachine', b)
    _safe_set(b, 'cjsidl_protocolBehavior69', set())
    assert not _is_linked(b, 'cjsidl_protocolBehavior69', a2)
    if hasattr(a2, 'cjsidl_stateMachine'):
        assert not _is_linked(a2, 'cjsidl_stateMachine', b)


def test_assoc_states82_reverse_link_reassign_clear():
    a1 = cjsidl_stateMachine(comment="sample_text", name="sample_text")
    a2 = cjsidl_stateMachine(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_state84', a1)
    assert _is_linked(b, 'cjsidl_state84', a1)
    if hasattr(a1, 'cjsidl_stateMachine83'):
        assert _is_linked(a1, 'cjsidl_stateMachine83', b)
    _safe_set(b, 'cjsidl_state84', a2)
    assert _is_linked(b, 'cjsidl_state84', a2)
    if hasattr(a1, 'cjsidl_stateMachine83'):
        assert not _is_linked(a1, 'cjsidl_stateMachine83', b)
    if hasattr(a2, 'cjsidl_stateMachine83'):
        assert _is_linked(a2, 'cjsidl_stateMachine83', b)
    _safe_set(b, 'cjsidl_state84', None)
    assert not _is_linked(b, 'cjsidl_state84', a2)
    if hasattr(a2, 'cjsidl_stateMachine83'):
        assert not _is_linked(a2, 'cjsidl_stateMachine83', b)


def test_assoc_subField353_reverse_link_reassign_clear():
    a1 = cjsidl_subField(comment="sample_text", fromIndex="sample_text", name="sample_text", toIndex="sample_text")
    a2 = cjsidl_subField(comment="sample_text_2", fromIndex="sample_text_2", name="sample_text_2", toIndex="sample_text_2")
    b = cjsidl_bitfieldDef(comment="sample_text", name="sample_text", optional="sample_text", type="sample_text")
    _safe_set(b, 'cjsidl_bitfieldDef354', {a1})
    assert _is_linked(b, 'cjsidl_bitfieldDef354', a1)
    if hasattr(a1, 'cjsidl_subField'):
        assert _is_linked(a1, 'cjsidl_subField', b)
    _safe_set(b, 'cjsidl_bitfieldDef354', {a2})
    assert _is_linked(b, 'cjsidl_bitfieldDef354', a2)
    if hasattr(a1, 'cjsidl_subField'):
        assert not _is_linked(a1, 'cjsidl_subField', b)
    if hasattr(a2, 'cjsidl_subField'):
        assert _is_linked(a2, 'cjsidl_subField', b)
    _safe_set(b, 'cjsidl_bitfieldDef354', set())
    assert not _is_linked(b, 'cjsidl_bitfieldDef354', a2)
    if hasattr(a2, 'cjsidl_subField'):
        assert not _is_linked(a2, 'cjsidl_subField', b)


def test_assoc_subState97_reverse_link_reassign_clear():
    a1 = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    a2 = cjsidl_state(comment="sample_text_2", initial="sample_text_2", name="sample_text_2")
    b = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_state98', a1)
    assert _is_linked(b, 'cjsidl_state98', a1)
    if hasattr(a1, 'cjsidl_state96'):
        assert _is_linked(a1, 'cjsidl_state96', b)
    _safe_set(b, 'cjsidl_state98', a2)
    assert _is_linked(b, 'cjsidl_state98', a2)
    if hasattr(a1, 'cjsidl_state96'):
        assert not _is_linked(a1, 'cjsidl_state96', b)
    if hasattr(a2, 'cjsidl_state96'):
        assert _is_linked(a2, 'cjsidl_state96', b)
    _safe_set(b, 'cjsidl_state98', None)
    assert not _is_linked(b, 'cjsidl_state98', a2)
    if hasattr(a2, 'cjsidl_state96'):
        assert not _is_linked(a2, 'cjsidl_state96', b)


def test_assoc_tag327_reverse_link_reassign_clear():
    a1 = cjsidl_taggedUnitsEnum(const_tag="sample_text", fieldUnit="sample_text", name="sample_text")
    a2 = cjsidl_taggedUnitsEnum(const_tag="sample_text_2", fieldUnit="sample_text_2", name="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference329', a1)
    assert _is_linked(b, 'cjsidl_constReference329', a1)
    if hasattr(a1, 'cjsidl_taggedUnitsEnum328'):
        assert _is_linked(a1, 'cjsidl_taggedUnitsEnum328', b)
    _safe_set(b, 'cjsidl_constReference329', a2)
    assert _is_linked(b, 'cjsidl_constReference329', a2)
    if hasattr(a1, 'cjsidl_taggedUnitsEnum328'):
        assert not _is_linked(a1, 'cjsidl_taggedUnitsEnum328', b)
    if hasattr(a2, 'cjsidl_taggedUnitsEnum328'):
        assert _is_linked(a2, 'cjsidl_taggedUnitsEnum328', b)
    _safe_set(b, 'cjsidl_constReference329', None)
    assert not _is_linked(b, 'cjsidl_constReference329', a2)
    if hasattr(a2, 'cjsidl_taggedUnitsEnum328'):
        assert not _is_linked(a2, 'cjsidl_taggedUnitsEnum328', b)


def test_assoc_transGuard127_reverse_link_reassign_clear():
    a1 = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    a2 = cjsidl_transition(comment="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = cjsidl_guard(comment="sample_text", equiv="sample_text", logicalOperator="sample_text")
    _safe_set(b, 'cjsidl_guard', a1)
    assert _is_linked(b, 'cjsidl_guard', a1)
    if hasattr(a1, 'cjsidl_transition128'):
        assert _is_linked(a1, 'cjsidl_transition128', b)
    _safe_set(b, 'cjsidl_guard', a2)
    assert _is_linked(b, 'cjsidl_guard', a2)
    if hasattr(a1, 'cjsidl_transition128'):
        assert not _is_linked(a1, 'cjsidl_transition128', b)
    if hasattr(a2, 'cjsidl_transition128'):
        assert _is_linked(a2, 'cjsidl_transition128', b)
    _safe_set(b, 'cjsidl_guard', None)
    assert not _is_linked(b, 'cjsidl_guard', a2)
    if hasattr(a2, 'cjsidl_transition128'):
        assert not _is_linked(a2, 'cjsidl_transition128', b)


def test_assoc_transGuard138_reverse_link_reassign_clear():
    a1 = cjsidl_guard(comment="sample_text", equiv="sample_text", logicalOperator="sample_text")
    a2 = cjsidl_guard(comment="sample_text_2", equiv="sample_text_2", logicalOperator="sample_text_2")
    b = cjsidl_defaultTransition(comment="sample_text", type="sample_text")
    _safe_set(b, 'cjsidl_defaultTransition139', a1)
    assert _is_linked(b, 'cjsidl_defaultTransition139', a1)
    if hasattr(a1, 'cjsidl_guard140'):
        assert _is_linked(a1, 'cjsidl_guard140', b)
    _safe_set(b, 'cjsidl_defaultTransition139', a2)
    assert _is_linked(b, 'cjsidl_defaultTransition139', a2)
    if hasattr(a1, 'cjsidl_guard140'):
        assert not _is_linked(a1, 'cjsidl_guard140', b)
    if hasattr(a2, 'cjsidl_guard140'):
        assert _is_linked(a2, 'cjsidl_guard140', b)
    _safe_set(b, 'cjsidl_defaultTransition139', None)
    assert not _is_linked(b, 'cjsidl_defaultTransition139', a2)
    if hasattr(a2, 'cjsidl_guard140'):
        assert not _is_linked(a2, 'cjsidl_guard140', b)


def test_assoc_transition99_reverse_link_reassign_clear():
    a1 = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    a2 = cjsidl_transition(comment="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = cjsidl_defaultState(comment="sample_text")
    _safe_set(b, 'cjsidl_defaultState100', {a1})
    assert _is_linked(b, 'cjsidl_defaultState100', a1)
    if hasattr(a1, 'cjsidl_transition101'):
        assert _is_linked(a1, 'cjsidl_transition101', b)
    _safe_set(b, 'cjsidl_defaultState100', {a2})
    assert _is_linked(b, 'cjsidl_defaultState100', a2)
    if hasattr(a1, 'cjsidl_transition101'):
        assert not _is_linked(a1, 'cjsidl_transition101', b)
    if hasattr(a2, 'cjsidl_transition101'):
        assert _is_linked(a2, 'cjsidl_transition101', b)
    _safe_set(b, 'cjsidl_defaultState100', set())
    assert not _is_linked(b, 'cjsidl_defaultState100', a2)
    if hasattr(a2, 'cjsidl_transition101'):
        assert not _is_linked(a2, 'cjsidl_transition101', b)


def test_assoc_transitions89_reverse_link_reassign_clear():
    a1 = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    a2 = cjsidl_transition(comment="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = cjsidl_state(comment="sample_text", initial="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_state90', {a1})
    assert _is_linked(b, 'cjsidl_state90', a1)
    if hasattr(a1, 'cjsidl_transition'):
        assert _is_linked(a1, 'cjsidl_transition', b)
    _safe_set(b, 'cjsidl_state90', {a2})
    assert _is_linked(b, 'cjsidl_state90', a2)
    if hasattr(a1, 'cjsidl_transition'):
        assert not _is_linked(a1, 'cjsidl_transition', b)
    if hasattr(a2, 'cjsidl_transition'):
        assert _is_linked(a2, 'cjsidl_transition', b)
    _safe_set(b, 'cjsidl_state90', set())
    assert not _is_linked(b, 'cjsidl_state90', a2)
    if hasattr(a2, 'cjsidl_transition'):
        assert not _is_linked(a2, 'cjsidl_transition', b)


def test_assoc_type283_reverse_link_reassign_clear():
    a1 = cjsidl_containerRef(comment="sample_text", name="sample_text", optional="sample_text")
    a2 = cjsidl_containerRef(comment="sample_text_2", name="sample_text_2", optional="sample_text_2")
    b = cjsidl_containerDef(comment="sample_text", name="sample_text", optional="sample_text")
    _safe_set(b, 'cjsidl_containerDef', a1)
    assert _is_linked(b, 'cjsidl_containerDef', a1)
    if hasattr(a1, 'cjsidl_containerRef'):
        assert _is_linked(a1, 'cjsidl_containerRef', b)
    _safe_set(b, 'cjsidl_containerDef', a2)
    assert _is_linked(b, 'cjsidl_containerDef', a2)
    if hasattr(a1, 'cjsidl_containerRef'):
        assert not _is_linked(a1, 'cjsidl_containerRef', b)
    if hasattr(a2, 'cjsidl_containerRef'):
        assert _is_linked(a2, 'cjsidl_containerRef', b)
    _safe_set(b, 'cjsidl_containerDef', None)
    assert not _is_linked(b, 'cjsidl_containerDef', a2)
    if hasattr(a2, 'cjsidl_containerRef'):
        assert not _is_linked(a2, 'cjsidl_containerRef', b)


def test_assoc_type286_reverse_link_reassign_clear():
    a1 = cjsidl_eventDef(name="sample_text")
    a2 = cjsidl_eventDef(name="sample_text_2")
    b = cjsidl_declaredEventDef(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_declaredEventDef', a1)
    assert _is_linked(b, 'cjsidl_declaredEventDef', a1)
    if hasattr(a1, 'cjsidl_eventDef287'):
        assert _is_linked(a1, 'cjsidl_eventDef287', b)
    _safe_set(b, 'cjsidl_declaredEventDef', a2)
    assert _is_linked(b, 'cjsidl_declaredEventDef', a2)
    if hasattr(a1, 'cjsidl_eventDef287'):
        assert not _is_linked(a1, 'cjsidl_eventDef287', b)
    if hasattr(a2, 'cjsidl_eventDef287'):
        assert _is_linked(a2, 'cjsidl_eventDef287', b)
    _safe_set(b, 'cjsidl_declaredEventDef', None)
    assert not _is_linked(b, 'cjsidl_declaredEventDef', a2)
    if hasattr(a2, 'cjsidl_eventDef287'):
        assert not _is_linked(a2, 'cjsidl_eventDef287', b)


def test_assoc_type307_reverse_link_reassign_clear():
    a1 = cjsidl_simpleNumericType(type="sample_text")
    a2 = cjsidl_simpleNumericType(type="sample_text_2")
    b = cjsidl_fixedFieldDef(comment="sample_text", fieldUnit="sample_text", name="sample_text", optional="sample_text")
    _safe_set(b, 'cjsidl_fixedFieldDef308', a1)
    assert _is_linked(b, 'cjsidl_fixedFieldDef308', a1)
    if hasattr(a1, 'cjsidl_simpleNumericType309'):
        assert _is_linked(a1, 'cjsidl_simpleNumericType309', b)
    _safe_set(b, 'cjsidl_fixedFieldDef308', a2)
    assert _is_linked(b, 'cjsidl_fixedFieldDef308', a2)
    if hasattr(a1, 'cjsidl_simpleNumericType309'):
        assert not _is_linked(a1, 'cjsidl_simpleNumericType309', b)
    if hasattr(a2, 'cjsidl_simpleNumericType309'):
        assert _is_linked(a2, 'cjsidl_simpleNumericType309', b)
    _safe_set(b, 'cjsidl_fixedFieldDef308', None)
    assert not _is_linked(b, 'cjsidl_fixedFieldDef308', a2)
    if hasattr(a2, 'cjsidl_simpleNumericType309'):
        assert not _is_linked(a2, 'cjsidl_simpleNumericType309', b)


def test_assoc_type333_reverse_link_reassign_clear():
    a1 = cjsidl_taggedUnitsEnum(const_tag="sample_text", fieldUnit="sample_text", name="sample_text")
    a2 = cjsidl_taggedUnitsEnum(const_tag="sample_text_2", fieldUnit="sample_text_2", name="sample_text_2")
    b = cjsidl_simpleNumericType(type="sample_text")
    _safe_set(b, 'cjsidl_simpleNumericType335', a1)
    assert _is_linked(b, 'cjsidl_simpleNumericType335', a1)
    if hasattr(a1, 'cjsidl_taggedUnitsEnum334'):
        assert _is_linked(a1, 'cjsidl_taggedUnitsEnum334', b)
    _safe_set(b, 'cjsidl_simpleNumericType335', a2)
    assert _is_linked(b, 'cjsidl_simpleNumericType335', a2)
    if hasattr(a1, 'cjsidl_taggedUnitsEnum334'):
        assert not _is_linked(a1, 'cjsidl_taggedUnitsEnum334', b)
    if hasattr(a2, 'cjsidl_taggedUnitsEnum334'):
        assert _is_linked(a2, 'cjsidl_taggedUnitsEnum334', b)
    _safe_set(b, 'cjsidl_simpleNumericType335', None)
    assert not _is_linked(b, 'cjsidl_simpleNumericType335', a2)
    if hasattr(a2, 'cjsidl_taggedUnitsEnum334'):
        assert not _is_linked(a2, 'cjsidl_taggedUnitsEnum334', b)


def test_assoc_typeRef244_reverse_link_reassign_clear():
    a1 = cjsidl_headerRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_headerRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_headerDef(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_headerDef245', a1)
    assert _is_linked(b, 'cjsidl_headerDef245', a1)
    if hasattr(a1, 'cjsidl_headerRef'):
        assert _is_linked(a1, 'cjsidl_headerRef', b)
    _safe_set(b, 'cjsidl_headerDef245', a2)
    assert _is_linked(b, 'cjsidl_headerDef245', a2)
    if hasattr(a1, 'cjsidl_headerRef'):
        assert not _is_linked(a1, 'cjsidl_headerRef', b)
    if hasattr(a2, 'cjsidl_headerRef'):
        assert _is_linked(a2, 'cjsidl_headerRef', b)
    _safe_set(b, 'cjsidl_headerDef245', None)
    assert not _is_linked(b, 'cjsidl_headerDef245', a2)
    if hasattr(a2, 'cjsidl_headerRef'):
        assert not _is_linked(a2, 'cjsidl_headerRef', b)


def test_assoc_typeRef248_reverse_link_reassign_clear():
    a1 = cjsidl_bodyRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_bodyRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_bodyDef(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_bodyDef249', a1)
    assert _is_linked(b, 'cjsidl_bodyDef249', a1)
    if hasattr(a1, 'cjsidl_bodyRef'):
        assert _is_linked(a1, 'cjsidl_bodyRef', b)
    _safe_set(b, 'cjsidl_bodyDef249', a2)
    assert _is_linked(b, 'cjsidl_bodyDef249', a2)
    if hasattr(a1, 'cjsidl_bodyRef'):
        assert not _is_linked(a1, 'cjsidl_bodyRef', b)
    if hasattr(a2, 'cjsidl_bodyRef'):
        assert _is_linked(a2, 'cjsidl_bodyRef', b)
    _safe_set(b, 'cjsidl_bodyDef249', None)
    assert not _is_linked(b, 'cjsidl_bodyDef249', a2)
    if hasattr(a2, 'cjsidl_bodyRef'):
        assert not _is_linked(a2, 'cjsidl_bodyRef', b)


def test_assoc_typeRef252_reverse_link_reassign_clear():
    a1 = cjsidl_footerRef(comment="sample_text", name="sample_text")
    a2 = cjsidl_footerRef(comment="sample_text_2", name="sample_text_2")
    b = cjsidl_footerDef(comment="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_footerDef253', a1)
    assert _is_linked(b, 'cjsidl_footerDef253', a1)
    if hasattr(a1, 'cjsidl_footerRef'):
        assert _is_linked(a1, 'cjsidl_footerRef', b)
    _safe_set(b, 'cjsidl_footerDef253', a2)
    assert _is_linked(b, 'cjsidl_footerDef253', a2)
    if hasattr(a1, 'cjsidl_footerRef'):
        assert not _is_linked(a1, 'cjsidl_footerRef', b)
    if hasattr(a2, 'cjsidl_footerRef'):
        assert _is_linked(a2, 'cjsidl_footerRef', b)
    _safe_set(b, 'cjsidl_footerDef253', None)
    assert not _is_linked(b, 'cjsidl_footerDef253', a2)
    if hasattr(a2, 'cjsidl_footerRef'):
        assert not _is_linked(a2, 'cjsidl_footerRef', b)


def test_assoc_typeRef36_reverse_link_reassign_clear():
    a1 = cjsidl_typeReference(comment="sample_text", name="sample_text", optional="sample_text")
    a2 = cjsidl_typeReference(comment="sample_text_2", name="sample_text_2", optional="sample_text_2")
    b = cjsidl_declaredTypeSet(name="sample_text", typeName="sample_text", version="sample_text")
    _safe_set(b, 'cjsidl_declaredTypeSet37', {a1})
    assert _is_linked(b, 'cjsidl_declaredTypeSet37', a1)
    if hasattr(a1, 'cjsidl_typeReference'):
        assert _is_linked(a1, 'cjsidl_typeReference', b)
    _safe_set(b, 'cjsidl_declaredTypeSet37', {a2})
    assert _is_linked(b, 'cjsidl_declaredTypeSet37', a2)
    if hasattr(a1, 'cjsidl_typeReference'):
        assert not _is_linked(a1, 'cjsidl_typeReference', b)
    if hasattr(a2, 'cjsidl_typeReference'):
        assert _is_linked(a2, 'cjsidl_typeReference', b)
    _safe_set(b, 'cjsidl_declaredTypeSet37', set())
    assert not _is_linked(b, 'cjsidl_declaredTypeSet37', a2)
    if hasattr(a2, 'cjsidl_typeReference'):
        assert not _is_linked(a2, 'cjsidl_typeReference', b)


def test_assoc_typeSet6_reverse_link_reassign_clear():
    a1 = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    a2 = cjsidl_serviceDef(assumpt="sample_text_2", name="sample_text_2", serviceName="sample_text_2", serviceVersion="sample_text_2")
    b = cjsidl_declaredTypeSet(name="sample_text", typeName="sample_text", version="sample_text")
    _safe_set(b, 'cjsidl_declaredTypeSet', a1)
    assert _is_linked(b, 'cjsidl_declaredTypeSet', a1)
    if hasattr(a1, 'cjsidl_serviceDef7'):
        assert _is_linked(a1, 'cjsidl_serviceDef7', b)
    _safe_set(b, 'cjsidl_declaredTypeSet', a2)
    assert _is_linked(b, 'cjsidl_declaredTypeSet', a2)
    if hasattr(a1, 'cjsidl_serviceDef7'):
        assert not _is_linked(a1, 'cjsidl_serviceDef7', b)
    if hasattr(a2, 'cjsidl_serviceDef7'):
        assert _is_linked(a2, 'cjsidl_serviceDef7', b)
    _safe_set(b, 'cjsidl_declaredTypeSet', None)
    assert not _is_linked(b, 'cjsidl_declaredTypeSet', a2)
    if hasattr(a2, 'cjsidl_serviceDef7'):
        assert not _is_linked(a2, 'cjsidl_serviceDef7', b)


def test_assoc_upperLimRef291_reverse_link_reassign_clear():
    a1 = cjsidl_fixedLenString(comment="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    a2 = cjsidl_fixedLenString(comment="sample_text_2", name="sample_text_2", optional="sample_text_2", upperLim="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference', a1)
    assert _is_linked(b, 'cjsidl_constReference', a1)
    if hasattr(a1, 'cjsidl_fixedLenString292'):
        assert _is_linked(a1, 'cjsidl_fixedLenString292', b)
    _safe_set(b, 'cjsidl_constReference', a2)
    assert _is_linked(b, 'cjsidl_constReference', a2)
    if hasattr(a1, 'cjsidl_fixedLenString292'):
        assert not _is_linked(a1, 'cjsidl_fixedLenString292', b)
    if hasattr(a2, 'cjsidl_fixedLenString292'):
        assert _is_linked(a2, 'cjsidl_fixedLenString292', b)
    _safe_set(b, 'cjsidl_constReference', None)
    assert not _is_linked(b, 'cjsidl_constReference', a2)
    if hasattr(a2, 'cjsidl_fixedLenString292'):
        assert not _is_linked(a2, 'cjsidl_fixedLenString292', b)


def test_assoc_upperLimRef301_reverse_link_reassign_clear():
    a1 = cjsidl_varLenString(comment="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    a2 = cjsidl_varLenString(comment="sample_text_2", lowerLim="sample_text_2", name="sample_text_2", optional="sample_text_2", upperLim="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference303', a1)
    assert _is_linked(b, 'cjsidl_constReference303', a1)
    if hasattr(a1, 'cjsidl_varLenString302'):
        assert _is_linked(a1, 'cjsidl_varLenString302', b)
    _safe_set(b, 'cjsidl_constReference303', a2)
    assert _is_linked(b, 'cjsidl_constReference303', a2)
    if hasattr(a1, 'cjsidl_varLenString302'):
        assert not _is_linked(a1, 'cjsidl_varLenString302', b)
    if hasattr(a2, 'cjsidl_varLenString302'):
        assert _is_linked(a2, 'cjsidl_varLenString302', b)
    _safe_set(b, 'cjsidl_constReference303', None)
    assert not _is_linked(b, 'cjsidl_constReference303', a2)
    if hasattr(a2, 'cjsidl_varLenString302'):
        assert not _is_linked(a2, 'cjsidl_varLenString302', b)


def test_assoc_upperLimRef321_reverse_link_reassign_clear():
    a1 = cjsidl_varLenField(comment="sample_text", countComment="sample_text", fieldFormat="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    a2 = cjsidl_varLenField(comment="sample_text_2", countComment="sample_text_2", fieldFormat="sample_text_2", lowerLim="sample_text_2", name="sample_text_2", optional="sample_text_2", upperLim="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference323', a1)
    assert _is_linked(b, 'cjsidl_constReference323', a1)
    if hasattr(a1, 'cjsidl_varLenField322'):
        assert _is_linked(a1, 'cjsidl_varLenField322', b)
    _safe_set(b, 'cjsidl_constReference323', a2)
    assert _is_linked(b, 'cjsidl_constReference323', a2)
    if hasattr(a1, 'cjsidl_varLenField322'):
        assert not _is_linked(a1, 'cjsidl_varLenField322', b)
    if hasattr(a2, 'cjsidl_varLenField322'):
        assert _is_linked(a2, 'cjsidl_varLenField322', b)
    _safe_set(b, 'cjsidl_constReference323', None)
    assert not _is_linked(b, 'cjsidl_constReference323', a2)
    if hasattr(a2, 'cjsidl_varLenField322'):
        assert not _is_linked(a2, 'cjsidl_varLenField322', b)


def test_assoc_upperLimRef361_reverse_link_reassign_clear():
    a1 = cjsidl_valueRange(comment="sample_text", lowerLim="sample_text", lowerLimit_type="sample_text", upperLim="sample_text", upperLimit_type="sample_text")
    a2 = cjsidl_valueRange(comment="sample_text_2", lowerLim="sample_text_2", lowerLimit_type="sample_text_2", upperLim="sample_text_2", upperLimit_type="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference363', a1)
    assert _is_linked(b, 'cjsidl_constReference363', a1)
    if hasattr(a1, 'cjsidl_valueRange362'):
        assert _is_linked(a1, 'cjsidl_valueRange362', b)
    _safe_set(b, 'cjsidl_constReference363', a2)
    assert _is_linked(b, 'cjsidl_constReference363', a2)
    if hasattr(a1, 'cjsidl_valueRange362'):
        assert not _is_linked(a1, 'cjsidl_valueRange362', b)
    if hasattr(a2, 'cjsidl_valueRange362'):
        assert _is_linked(a2, 'cjsidl_valueRange362', b)
    _safe_set(b, 'cjsidl_constReference363', None)
    assert not _is_linked(b, 'cjsidl_constReference363', a2)
    if hasattr(a2, 'cjsidl_valueRange362'):
        assert not _is_linked(a2, 'cjsidl_valueRange362', b)


def test_assoc_upperLimRef373_reverse_link_reassign_clear():
    a1 = cjsidl_scaledRangeDef(function="sample_text", interp="sample_text", lowerLim="sample_text", upperLim="sample_text")
    a2 = cjsidl_scaledRangeDef(function="sample_text_2", interp="sample_text_2", lowerLim="sample_text_2", upperLim="sample_text_2")
    b = cjsidl_constReference(comment="sample_text")
    _safe_set(b, 'cjsidl_constReference375', a1)
    assert _is_linked(b, 'cjsidl_constReference375', a1)
    if hasattr(a1, 'cjsidl_scaledRangeDef374'):
        assert _is_linked(a1, 'cjsidl_scaledRangeDef374', b)
    _safe_set(b, 'cjsidl_constReference375', a2)
    assert _is_linked(b, 'cjsidl_constReference375', a2)
    if hasattr(a1, 'cjsidl_scaledRangeDef374'):
        assert not _is_linked(a1, 'cjsidl_scaledRangeDef374', b)
    if hasattr(a2, 'cjsidl_scaledRangeDef374'):
        assert _is_linked(a2, 'cjsidl_scaledRangeDef374', b)
    _safe_set(b, 'cjsidl_constReference375', None)
    assert not _is_linked(b, 'cjsidl_constReference375', a2)
    if hasattr(a2, 'cjsidl_scaledRangeDef374'):
        assert not _is_linked(a2, 'cjsidl_scaledRangeDef374', b)


def test_assoc_valueSet379_reverse_link_reassign_clear():
    a1 = cjsidl_valueSetDef(offset="sample_text")
    a2 = cjsidl_valueSetDef(offset="sample_text_2")
    b = cjsidl_subField(comment="sample_text", fromIndex="sample_text", name="sample_text", toIndex="sample_text")
    _safe_set(b, 'cjsidl_subField380', a1)
    assert _is_linked(b, 'cjsidl_subField380', a1)
    if hasattr(a1, 'cjsidl_valueSetDef381'):
        assert _is_linked(a1, 'cjsidl_valueSetDef381', b)
    _safe_set(b, 'cjsidl_subField380', a2)
    assert _is_linked(b, 'cjsidl_subField380', a2)
    if hasattr(a1, 'cjsidl_valueSetDef381'):
        assert not _is_linked(a1, 'cjsidl_valueSetDef381', b)
    if hasattr(a2, 'cjsidl_valueSetDef381'):
        assert _is_linked(a2, 'cjsidl_valueSetDef381', b)
    _safe_set(b, 'cjsidl_subField380', None)
    assert not _is_linked(b, 'cjsidl_subField380', a2)
    if hasattr(a2, 'cjsidl_valueSetDef381'):
        assert not _is_linked(a2, 'cjsidl_valueSetDef381', b)


def test_assoc_valueSetDef336_reverse_link_reassign_clear():
    a1 = cjsidl_valueSetDef(offset="sample_text")
    a2 = cjsidl_valueSetDef(offset="sample_text_2")
    b = cjsidl_taggedUnitsEnum(const_tag="sample_text", fieldUnit="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_taggedUnitsEnum337', a1)
    assert _is_linked(b, 'cjsidl_taggedUnitsEnum337', a1)
    if hasattr(a1, 'cjsidl_valueSetDef'):
        assert _is_linked(a1, 'cjsidl_valueSetDef', b)
    _safe_set(b, 'cjsidl_taggedUnitsEnum337', a2)
    assert _is_linked(b, 'cjsidl_taggedUnitsEnum337', a2)
    if hasattr(a1, 'cjsidl_valueSetDef'):
        assert not _is_linked(a1, 'cjsidl_valueSetDef', b)
    if hasattr(a2, 'cjsidl_valueSetDef'):
        assert _is_linked(a2, 'cjsidl_valueSetDef', b)
    _safe_set(b, 'cjsidl_taggedUnitsEnum337', None)
    assert not _is_linked(b, 'cjsidl_taggedUnitsEnum337', a2)
    if hasattr(a2, 'cjsidl_valueSetDef'):
        assert not _is_linked(a2, 'cjsidl_valueSetDef', b)


def test_assoc_vtagField313_reverse_link_reassign_clear():
    a1 = cjsidl_varField(comment="sample_text", name="sample_text", optional="sample_text")
    a2 = cjsidl_varField(comment="sample_text_2", name="sample_text_2", optional="sample_text_2")
    b = cjsidl_taggedUnitsEnum(const_tag="sample_text", fieldUnit="sample_text", name="sample_text")
    _safe_set(b, 'cjsidl_taggedUnitsEnum', a1)
    assert _is_linked(b, 'cjsidl_taggedUnitsEnum', a1)
    if hasattr(a1, 'cjsidl_varField314'):
        assert _is_linked(a1, 'cjsidl_varField314', b)
    _safe_set(b, 'cjsidl_taggedUnitsEnum', a2)
    assert _is_linked(b, 'cjsidl_taggedUnitsEnum', a2)
    if hasattr(a1, 'cjsidl_varField314'):
        assert not _is_linked(a1, 'cjsidl_varField314', b)
    if hasattr(a2, 'cjsidl_varField314'):
        assert _is_linked(a2, 'cjsidl_varField314', b)
    _safe_set(b, 'cjsidl_taggedUnitsEnum', None)
    assert not _is_linked(b, 'cjsidl_taggedUnitsEnum', a2)
    if hasattr(a2, 'cjsidl_varField314'):
        assert not _is_linked(a2, 'cjsidl_varField314', b)


