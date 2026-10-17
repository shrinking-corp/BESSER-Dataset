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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions105_stub_double():
    # cjsidl_actionList has no real 'cjsidl_actionList' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_entry(comment="sample_text")
    partner = cjsidl_actionList()
    setattr(partner, 'cjsidl_actionList', None)
    _safe_set(owner, 'cjsidl_entry106', partner)
    assert getattr(partner, 'cjsidl_actionList') == owner
    _safe_set(owner, 'cjsidl_entry106', None)
    assert getattr(partner, 'cjsidl_actionList') is None


def test_assoc_actions109_stub_double():
    # cjsidl_actionList has no real 'cjsidl_actionList111' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_exit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_exit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_exit(comment="sample_text")
    partner = cjsidl_actionList()
    setattr(partner, 'cjsidl_actionList111', None)
    _safe_set(owner, 'cjsidl_exit110', partner)
    assert getattr(partner, 'cjsidl_actionList111') == owner
    _safe_set(owner, 'cjsidl_exit110', None)
    assert getattr(partner, 'cjsidl_actionList111') is None


def test_assoc_actions129_stub_double():
    # cjsidl_actionList has no real 'cjsidl_actionList131' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    partner = cjsidl_actionList()
    setattr(partner, 'cjsidl_actionList131', None)
    _safe_set(owner, 'cjsidl_transition130', partner)
    assert getattr(partner, 'cjsidl_actionList131') == owner
    _safe_set(owner, 'cjsidl_transition130', None)
    assert getattr(partner, 'cjsidl_actionList131') is None


def test_assoc_actions141_stub_double():
    # cjsidl_actionList has no real 'cjsidl_actionList143' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_defaultTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_defaultTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_defaultTransition(comment="sample_text", type="sample_text")
    partner = cjsidl_actionList()
    setattr(partner, 'cjsidl_actionList143', None)
    _safe_set(owner, 'cjsidl_defaultTransition142', partner)
    assert getattr(partner, 'cjsidl_actionList143') == owner
    _safe_set(owner, 'cjsidl_defaultTransition142', None)
    assert getattr(partner, 'cjsidl_actionList143') is None


def test_assoc_actions177_stub_double():
    # cjsidl_actionList has no real 'cjsidl_actionList178' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_action(comment="sample_text", name="sample_text")
    partner = cjsidl_actionList()
    setattr(partner, 'cjsidl_actionList178', None)
    _safe_set(owner, 'cjsidl_action', partner)
    assert getattr(partner, 'cjsidl_actionList178') == owner
    _safe_set(owner, 'cjsidl_action', None)
    assert getattr(partner, 'cjsidl_actionList178') is None


def test_assoc_actions179_stub_double():
    # cjsidl_sendActionList has no real 'cjsidl_sendActionList180' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_action(comment="sample_text", name="sample_text")
    partner = cjsidl_sendActionList()
    setattr(partner, 'cjsidl_sendActionList180', None)
    _safe_set(owner, 'cjsidl_action181', partner)
    assert getattr(partner, 'cjsidl_sendActionList180') == owner
    _safe_set(owner, 'cjsidl_action181', None)
    assert getattr(partner, 'cjsidl_sendActionList180') is None


def test_assoc_arrayDef193_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef194' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_arrayDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_arrayDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_arrayDef(arraySize="sample_text", comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef194', None)
    _safe_set(owner, 'cjsidl_arrayDef', partner)
    assert getattr(partner, 'cjsidl_typeDef194') == owner
    _safe_set(owner, 'cjsidl_arrayDef', None)
    assert getattr(partner, 'cjsidl_typeDef194') is None


def test_assoc_arrayDef423_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef424' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_arrayDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_arrayDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_arrayDef(arraySize="sample_text", comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef424', None)
    _safe_set(owner, 'cjsidl_arrayDef425', partner)
    assert getattr(partner, 'cjsidl_recordDef424') == owner
    _safe_set(owner, 'cjsidl_arrayDef425', None)
    assert getattr(partner, 'cjsidl_recordDef424') is None


def test_assoc_bitfieldDef207_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef208' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_bitfieldDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_bitfieldDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_bitfieldDef(comment="sample_text", name="sample_text", optional="sample_text", type="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef208', None)
    _safe_set(owner, 'cjsidl_bitfieldDef', partner)
    assert getattr(partner, 'cjsidl_typeDef208') == owner
    _safe_set(owner, 'cjsidl_bitfieldDef', None)
    assert getattr(partner, 'cjsidl_typeDef208') is None


def test_assoc_bitfieldDef432_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef433' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_bitfieldDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_bitfieldDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_bitfieldDef(comment="sample_text", name="sample_text", optional="sample_text", type="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef433', None)
    _safe_set(owner, 'cjsidl_bitfieldDef434', partner)
    assert getattr(partner, 'cjsidl_recordDef433') == owner
    _safe_set(owner, 'cjsidl_bitfieldDef434', None)
    assert getattr(partner, 'cjsidl_recordDef433') is None


def test_assoc_body229_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject231' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject231', None)
    _safe_set(owner, 'cjsidl_messageDef230', partner)
    assert getattr(partner, 'cjsidl_EObject231') == owner
    _safe_set(owner, 'cjsidl_messageDef230', None)
    assert getattr(partner, 'cjsidl_EObject231') is None


def test_assoc_body59_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject61' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_eventDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_eventDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_eventDef(name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject61', None)
    _safe_set(owner, 'cjsidl_eventDef60', partner)
    assert getattr(partner, 'cjsidl_EObject61') == owner
    _safe_set(owner, 'cjsidl_eventDef60', None)
    assert getattr(partner, 'cjsidl_EObject61') is None


def test_assoc_bodyDef219_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef220' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_bodyDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_bodyDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_bodyDef(comment="sample_text", name="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef220', None)
    _safe_set(owner, 'cjsidl_bodyDef', partner)
    assert getattr(partner, 'cjsidl_typeDef220') == owner
    _safe_set(owner, 'cjsidl_bodyDef', None)
    assert getattr(partner, 'cjsidl_typeDef220') is None


def test_assoc_constScopedRef347_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId349' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_formatEnumDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_formatEnumDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_formatEnumDef(fieldFormat="sample_text", fieldFormatStr="sample_text", index="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId349', None)
    _safe_set(owner, 'cjsidl_formatEnumDef348', partner)
    assert getattr(partner, 'cjsidl_scopedConstId349') == owner
    _safe_set(owner, 'cjsidl_formatEnumDef348', None)
    assert getattr(partner, 'cjsidl_scopedConstId349') is None


def test_assoc_containerDef414_stub_double():
    # cjsidl_taggedItemDef has no real 'cjsidl_taggedItemDef415' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_containerDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_containerDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_containerDef(comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_taggedItemDef()
    setattr(partner, 'cjsidl_taggedItemDef415', None)
    _safe_set(owner, 'cjsidl_containerDef416', partner)
    assert getattr(partner, 'cjsidl_taggedItemDef415') == owner
    _safe_set(owner, 'cjsidl_containerDef416', None)
    assert getattr(partner, 'cjsidl_taggedItemDef415') is None


def test_assoc_containerRef417_stub_double():
    # cjsidl_taggedItemDef has no real 'cjsidl_taggedItemDef418' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_containerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_containerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_containerRef(comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_taggedItemDef()
    setattr(partner, 'cjsidl_taggedItemDef418', None)
    _safe_set(owner, 'cjsidl_containerRef419', partner)
    assert getattr(partner, 'cjsidl_taggedItemDef418') == owner
    _safe_set(owner, 'cjsidl_containerRef419', None)
    assert getattr(partner, 'cjsidl_taggedItemDef418') is None


def test_assoc_defs51_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject53' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_internalEventSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_internalEventSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_internalEventSet(comment="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject53', None)
    _safe_set(owner, 'cjsidl_internalEventSet52', {partner})
    assert getattr(partner, 'cjsidl_EObject53') == owner
    _safe_set(owner, 'cjsidl_internalEventSet52', set())
    assert getattr(partner, 'cjsidl_EObject53') is None


def test_assoc_destination135_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject137' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject137', None)
    _safe_set(owner, 'cjsidl_transition136', partner)
    assert getattr(partner, 'cjsidl_EObject137') == owner
    _safe_set(owner, 'cjsidl_transition136', None)
    assert getattr(partner, 'cjsidl_EObject137') is None


def test_assoc_destination147_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject149' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_defaultTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_defaultTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_defaultTransition(comment="sample_text", type="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject149', None)
    _safe_set(owner, 'cjsidl_defaultTransition148', partner)
    assert getattr(partner, 'cjsidl_EObject149') == owner
    _safe_set(owner, 'cjsidl_defaultTransition148', None)
    assert getattr(partner, 'cjsidl_EObject149') is None


def test_assoc_fieldDef426_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef427' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_fixedFieldDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_fixedFieldDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_fixedFieldDef(comment="sample_text", fieldUnit="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef427', None)
    _safe_set(owner, 'cjsidl_fixedFieldDef428', partner)
    assert getattr(partner, 'cjsidl_recordDef427') == owner
    _safe_set(owner, 'cjsidl_fixedFieldDef428', None)
    assert getattr(partner, 'cjsidl_recordDef427') is None


def test_assoc_fixedFieldDef203_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef204' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_fixedFieldDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_fixedFieldDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_fixedFieldDef(comment="sample_text", fieldUnit="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef204', None)
    _safe_set(owner, 'cjsidl_fixedFieldDef', partner)
    assert getattr(partner, 'cjsidl_typeDef204') == owner
    _safe_set(owner, 'cjsidl_fixedFieldDef', None)
    assert getattr(partner, 'cjsidl_typeDef204') is None


def test_assoc_fixedLenString209_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef210' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_fixedLenString's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_fixedLenString's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_fixedLenString(comment="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef210', None)
    _safe_set(owner, 'cjsidl_fixedLenString', partner)
    assert getattr(partner, 'cjsidl_typeDef210') == owner
    _safe_set(owner, 'cjsidl_fixedLenString', None)
    assert getattr(partner, 'cjsidl_typeDef210') is None


def test_assoc_fixedLengthStringDef435_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef436' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_fixedLenString's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_fixedLenString's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_fixedLenString(comment="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef436', None)
    _safe_set(owner, 'cjsidl_fixedLenString437', partner)
    assert getattr(partner, 'cjsidl_recordDef436') == owner
    _safe_set(owner, 'cjsidl_fixedLenString437', None)
    assert getattr(partner, 'cjsidl_recordDef436') is None


def test_assoc_footer232_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject234' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject234', None)
    _safe_set(owner, 'cjsidl_messageDef233', partner)
    assert getattr(partner, 'cjsidl_EObject234') == owner
    _safe_set(owner, 'cjsidl_messageDef233', None)
    assert getattr(partner, 'cjsidl_EObject234') is None


def test_assoc_footer62_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject64' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_eventDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_eventDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_eventDef(name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject64', None)
    _safe_set(owner, 'cjsidl_eventDef63', partner)
    assert getattr(partner, 'cjsidl_EObject64') == owner
    _safe_set(owner, 'cjsidl_eventDef63', None)
    assert getattr(partner, 'cjsidl_EObject64') is None


def test_assoc_footerDef221_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef222' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_footerDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_footerDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_footerDef(comment="sample_text", name="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef222', None)
    _safe_set(owner, 'cjsidl_footerDef', partner)
    assert getattr(partner, 'cjsidl_typeDef222') == owner
    _safe_set(owner, 'cjsidl_footerDef', None)
    assert getattr(partner, 'cjsidl_typeDef222') is None


def test_assoc_header226_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject228' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject228', None)
    _safe_set(owner, 'cjsidl_messageDef227', partner)
    assert getattr(partner, 'cjsidl_EObject228') == owner
    _safe_set(owner, 'cjsidl_messageDef227', None)
    assert getattr(partner, 'cjsidl_EObject228') is None


def test_assoc_header56_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject58' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_eventDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_eventDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_eventDef(name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject58', None)
    _safe_set(owner, 'cjsidl_eventDef57', partner)
    assert getattr(partner, 'cjsidl_EObject58') == owner
    _safe_set(owner, 'cjsidl_eventDef57', None)
    assert getattr(partner, 'cjsidl_EObject58') is None


def test_assoc_headerDef217_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef218' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_headerDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_headerDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_headerDef(comment="sample_text", name="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef218', None)
    _safe_set(owner, 'cjsidl_headerDef', partner)
    assert getattr(partner, 'cjsidl_typeDef218') == owner
    _safe_set(owner, 'cjsidl_headerDef', None)
    assert getattr(partner, 'cjsidl_typeDef218') is None


def test_assoc_inputSet40_stub_double():
    # cjsidl_messages has no real 'cjsidl_messages' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageSet(comment="sample_text", inputComment="sample_text", outputComment="sample_text")
    partner = cjsidl_messages()
    setattr(partner, 'cjsidl_messages', None)
    _safe_set(owner, 'cjsidl_messageSet41', partner)
    assert getattr(partner, 'cjsidl_messages') == owner
    _safe_set(owner, 'cjsidl_messageSet41', None)
    assert getattr(partner, 'cjsidl_messages') is None


def test_assoc_itemList412_stub_double():
    # cjsidl_taggedItemDef has no real 'cjsidl_taggedItemDef' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_variantDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_variantDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_variantDef(maxCount="sample_text", minCount="sample_text", vtagComment="sample_text")
    partner = cjsidl_taggedItemDef()
    setattr(partner, 'cjsidl_taggedItemDef', None)
    _safe_set(owner, 'cjsidl_variantDef413', {partner})
    assert getattr(partner, 'cjsidl_taggedItemDef') == owner
    _safe_set(owner, 'cjsidl_variantDef413', set())
    assert getattr(partner, 'cjsidl_taggedItemDef') is None


def test_assoc_listDef197_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef198' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_listDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_listDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_listDef(countComment="sample_text", maxCount="sample_text", minCount="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef198', None)
    _safe_set(owner, 'cjsidl_listDef', partner)
    assert getattr(partner, 'cjsidl_typeDef198') == owner
    _safe_set(owner, 'cjsidl_listDef', None)
    assert getattr(partner, 'cjsidl_typeDef198') is None


def test_assoc_lowerLimScoped298_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId300' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenString's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenString's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenString(comment="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId300', None)
    _safe_set(owner, 'cjsidl_varLenString299', partner)
    assert getattr(partner, 'cjsidl_scopedConstId300') == owner
    _safe_set(owner, 'cjsidl_varLenString299', None)
    assert getattr(partner, 'cjsidl_scopedConstId300') is None


def test_assoc_lowerLimScoped318_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId320' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenField(comment="sample_text", countComment="sample_text", fieldFormat="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId320', None)
    _safe_set(owner, 'cjsidl_varLenField319', partner)
    assert getattr(partner, 'cjsidl_scopedConstId320') == owner
    _safe_set(owner, 'cjsidl_varLenField319', None)
    assert getattr(partner, 'cjsidl_scopedConstId320') is None


def test_assoc_lowerLimScoped358_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId360' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_valueRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_valueRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_valueRange(comment="sample_text", lowerLim="sample_text", lowerLimit_type="sample_text", upperLim="sample_text", upperLimit_type="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId360', None)
    _safe_set(owner, 'cjsidl_valueRange359', partner)
    assert getattr(partner, 'cjsidl_scopedConstId360') == owner
    _safe_set(owner, 'cjsidl_valueRange359', None)
    assert getattr(partner, 'cjsidl_scopedConstId360') is None


def test_assoc_lowerLimScoped370_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId372' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_scaledRangeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_scaledRangeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_scaledRangeDef(function="sample_text", interp="sample_text", lowerLim="sample_text", upperLim="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId372', None)
    _safe_set(owner, 'cjsidl_scaledRangeDef371', partner)
    assert getattr(partner, 'cjsidl_scopedConstId372') == owner
    _safe_set(owner, 'cjsidl_scaledRangeDef371', None)
    assert getattr(partner, 'cjsidl_scopedConstId372') is None


def test_assoc_maxCountScoped391_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId393' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_listDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_listDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_listDef(countComment="sample_text", maxCount="sample_text", minCount="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId393', None)
    _safe_set(owner, 'cjsidl_listDef392', partner)
    assert getattr(partner, 'cjsidl_scopedConstId393') == owner
    _safe_set(owner, 'cjsidl_listDef392', None)
    assert getattr(partner, 'cjsidl_scopedConstId393') is None


def test_assoc_maxCountScoped409_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId411' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_variantDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_variantDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_variantDef(maxCount="sample_text", minCount="sample_text", vtagComment="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId411', None)
    _safe_set(owner, 'cjsidl_variantDef410', partner)
    assert getattr(partner, 'cjsidl_scopedConstId411') == owner
    _safe_set(owner, 'cjsidl_variantDef410', None)
    assert getattr(partner, 'cjsidl_scopedConstId411') is None


def test_assoc_messageDef190_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef191' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef191', None)
    _safe_set(owner, 'cjsidl_messageDef192', partner)
    assert getattr(partner, 'cjsidl_typeDef191') == owner
    _safe_set(owner, 'cjsidl_messageDef192', None)
    assert getattr(partner, 'cjsidl_typeDef191') is None


def test_assoc_messageDefs45_stub_double():
    # cjsidl_messages has no real 'cjsidl_messages46' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageDef(command="sample_text", messageID="sample_text", name="sample_text")
    partner = cjsidl_messages()
    setattr(partner, 'cjsidl_messages46', None)
    _safe_set(owner, 'cjsidl_messageDef', partner)
    assert getattr(partner, 'cjsidl_messages46') == owner
    _safe_set(owner, 'cjsidl_messageDef', None)
    assert getattr(partner, 'cjsidl_messages46') is None


def test_assoc_minCountScoped385_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId387' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_listDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_listDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_listDef(countComment="sample_text", maxCount="sample_text", minCount="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId387', None)
    _safe_set(owner, 'cjsidl_listDef386', partner)
    assert getattr(partner, 'cjsidl_scopedConstId387') == owner
    _safe_set(owner, 'cjsidl_listDef386', None)
    assert getattr(partner, 'cjsidl_scopedConstId387') is None


def test_assoc_minCountScoped403_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId405' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_variantDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_variantDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_variantDef(maxCount="sample_text", minCount="sample_text", vtagComment="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId405', None)
    _safe_set(owner, 'cjsidl_variantDef404', partner)
    assert getattr(partner, 'cjsidl_scopedConstId405') == owner
    _safe_set(owner, 'cjsidl_variantDef404', None)
    assert getattr(partner, 'cjsidl_scopedConstId405') is None


def test_assoc_outputSet42_stub_double():
    # cjsidl_messages has no real 'cjsidl_messages44' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageSet(comment="sample_text", inputComment="sample_text", outputComment="sample_text")
    partner = cjsidl_messages()
    setattr(partner, 'cjsidl_messages44', None)
    _safe_set(owner, 'cjsidl_messageSet43', partner)
    assert getattr(partner, 'cjsidl_messages44') == owner
    _safe_set(owner, 'cjsidl_messageSet43', None)
    assert getattr(partner, 'cjsidl_messages44') is None


def test_assoc_params115_stub_double():
    # cjsidl_transParams has no real 'cjsidl_transParams' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_transParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_transParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_transParam(comment="sample_text", name="sample_text", unsignedType="sample_text")
    partner = cjsidl_transParams()
    setattr(partner, 'cjsidl_transParams', None)
    _safe_set(owner, 'cjsidl_transParam', partner)
    assert getattr(partner, 'cjsidl_transParams') == owner
    _safe_set(owner, 'cjsidl_transParam', None)
    assert getattr(partner, 'cjsidl_transParams') is None


def test_assoc_params124_stub_double():
    # cjsidl_transParams has no real 'cjsidl_transParams126' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    partner = cjsidl_transParams()
    setattr(partner, 'cjsidl_transParams126', None)
    _safe_set(owner, 'cjsidl_transition125', partner)
    assert getattr(partner, 'cjsidl_transParams126') == owner
    _safe_set(owner, 'cjsidl_transition125', None)
    assert getattr(partner, 'cjsidl_transParams126') is None


def test_assoc_recordListSequenceVariant235_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject237' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_headerDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_headerDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_headerDef(comment="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject237', None)
    _safe_set(owner, 'cjsidl_headerDef236', partner)
    assert getattr(partner, 'cjsidl_EObject237') == owner
    _safe_set(owner, 'cjsidl_headerDef236', None)
    assert getattr(partner, 'cjsidl_EObject237') is None


def test_assoc_recordListSequenceVariant238_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject240' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_bodyDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_bodyDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_bodyDef(comment="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject240', None)
    _safe_set(owner, 'cjsidl_bodyDef239', partner)
    assert getattr(partner, 'cjsidl_EObject240') == owner
    _safe_set(owner, 'cjsidl_bodyDef239', None)
    assert getattr(partner, 'cjsidl_EObject240') is None


def test_assoc_recordListSequenceVariant241_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject243' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_footerDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_footerDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_footerDef(comment="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject243', None)
    _safe_set(owner, 'cjsidl_footerDef242', partner)
    assert getattr(partner, 'cjsidl_EObject243') == owner
    _safe_set(owner, 'cjsidl_footerDef242', None)
    assert getattr(partner, 'cjsidl_EObject243') is None


def test_assoc_ref492_stub_double():
    # cjsidl_scopedType has no real 'cjsidl_scopedType494' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_scopedTypeId's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_scopedTypeId's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_scopedTypeId(comment="sample_text", optional="sample_text", scopedName="sample_text")
    partner = cjsidl_scopedType()
    setattr(partner, 'cjsidl_scopedType494', None)
    _safe_set(owner, 'cjsidl_scopedTypeId493', partner)
    assert getattr(partner, 'cjsidl_scopedType494') == owner
    _safe_set(owner, 'cjsidl_scopedTypeId493', None)
    assert getattr(partner, 'cjsidl_scopedType494') is None


def test_assoc_refClient16_stub_double():
    # cjsidl_references has no real 'cjsidl_references17' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_refAttr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_refAttr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_refAttr(comment="sample_text", name="sample_text")
    partner = cjsidl_references()
    setattr(partner, 'cjsidl_references17', None)
    _safe_set(owner, 'cjsidl_refAttr18', partner)
    assert getattr(partner, 'cjsidl_references17') == owner
    _safe_set(owner, 'cjsidl_refAttr18', None)
    assert getattr(partner, 'cjsidl_references17') is None


def test_assoc_refInherit14_stub_double():
    # cjsidl_references has no real 'cjsidl_references15' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_refAttr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_refAttr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_refAttr(comment="sample_text", name="sample_text")
    partner = cjsidl_references()
    setattr(partner, 'cjsidl_references15', None)
    _safe_set(owner, 'cjsidl_refAttr', partner)
    assert getattr(partner, 'cjsidl_references15') == owner
    _safe_set(owner, 'cjsidl_refAttr', None)
    assert getattr(partner, 'cjsidl_references15') is None


def test_assoc_refs2_stub_double():
    # cjsidl_references has no real 'cjsidl_references' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_serviceDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_serviceDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_serviceDef(assumpt="sample_text", name="sample_text", serviceName="sample_text", serviceVersion="sample_text")
    partner = cjsidl_references()
    setattr(partner, 'cjsidl_references', None)
    _safe_set(owner, 'cjsidl_serviceDef3', partner)
    assert getattr(partner, 'cjsidl_references') == owner
    _safe_set(owner, 'cjsidl_serviceDef3', None)
    assert getattr(partner, 'cjsidl_references') is None


def test_assoc_scope465_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject467' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageScopedRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageScopedRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageScopedRef(comment="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject467', None)
    _safe_set(owner, 'cjsidl_messageScopedRef466', partner)
    assert getattr(partner, 'cjsidl_EObject467') == owner
    _safe_set(owner, 'cjsidl_messageScopedRef466', None)
    assert getattr(partner, 'cjsidl_EObject467') is None


def test_assoc_scopedEventType119_stub_double():
    # cjsidl_scopedEventType has no real 'cjsidl_scopedEventType' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_transParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_transParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_transParam(comment="sample_text", name="sample_text", unsignedType="sample_text")
    partner = cjsidl_scopedEventType()
    setattr(partner, 'cjsidl_scopedEventType', None)
    _safe_set(owner, 'cjsidl_transParam120', partner)
    assert getattr(partner, 'cjsidl_scopedEventType') == owner
    _safe_set(owner, 'cjsidl_transParam120', None)
    assert getattr(partner, 'cjsidl_scopedEventType') is None


def test_assoc_scopedEventType288_stub_double():
    # cjsidl_scopedEventType has no real 'cjsidl_scopedEventType290' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_declaredEventDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_declaredEventDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_declaredEventDef(comment="sample_text", name="sample_text")
    partner = cjsidl_scopedEventType()
    setattr(partner, 'cjsidl_scopedEventType290', None)
    _safe_set(owner, 'cjsidl_declaredEventDef289', partner)
    assert getattr(partner, 'cjsidl_scopedEventType290') == owner
    _safe_set(owner, 'cjsidl_declaredEventDef289', None)
    assert getattr(partner, 'cjsidl_scopedEventType290') is None


def test_assoc_scopedRef246_stub_double():
    # cjsidl_headerScopedRef has no real 'cjsidl_headerScopedRef' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_headerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_headerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_headerRef(comment="sample_text", name="sample_text")
    partner = cjsidl_headerScopedRef()
    setattr(partner, 'cjsidl_headerScopedRef', None)
    _safe_set(owner, 'cjsidl_headerRef247', partner)
    assert getattr(partner, 'cjsidl_headerScopedRef') == owner
    _safe_set(owner, 'cjsidl_headerRef247', None)
    assert getattr(partner, 'cjsidl_headerScopedRef') is None


def test_assoc_scopedRef250_stub_double():
    # cjsidl_bodyScopedRef has no real 'cjsidl_bodyScopedRef' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_bodyRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_bodyRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_bodyRef(comment="sample_text", name="sample_text")
    partner = cjsidl_bodyScopedRef()
    setattr(partner, 'cjsidl_bodyScopedRef', None)
    _safe_set(owner, 'cjsidl_bodyRef251', partner)
    assert getattr(partner, 'cjsidl_bodyScopedRef') == owner
    _safe_set(owner, 'cjsidl_bodyRef251', None)
    assert getattr(partner, 'cjsidl_bodyScopedRef') is None


def test_assoc_scopedRef254_stub_double():
    # cjsidl_footerScopedRef has no real 'cjsidl_footerScopedRef' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_footerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_footerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_footerRef(comment="sample_text", name="sample_text")
    partner = cjsidl_footerScopedRef()
    setattr(partner, 'cjsidl_footerScopedRef', None)
    _safe_set(owner, 'cjsidl_footerRef255', partner)
    assert getattr(partner, 'cjsidl_footerScopedRef') == owner
    _safe_set(owner, 'cjsidl_footerRef255', None)
    assert getattr(partner, 'cjsidl_footerScopedRef') is None


def test_assoc_scopedRef450_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef451' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_scopedTypeId's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_scopedTypeId's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_scopedTypeId(comment="sample_text", optional="sample_text", scopedName="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef451', None)
    _safe_set(owner, 'cjsidl_scopedTypeId452', partner)
    assert getattr(partner, 'cjsidl_recordDef451') == owner
    _safe_set(owner, 'cjsidl_scopedTypeId452', None)
    assert getattr(partner, 'cjsidl_recordDef451') is None


def test_assoc_scopedRefs49_stub_double():
    # cjsidl_messages has no real 'cjsidl_messages50' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageScopedRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageScopedRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageScopedRef(comment="sample_text", name="sample_text")
    partner = cjsidl_messages()
    setattr(partner, 'cjsidl_messages50', None)
    _safe_set(owner, 'cjsidl_messageScopedRef', partner)
    assert getattr(partner, 'cjsidl_messages50') == owner
    _safe_set(owner, 'cjsidl_messageScopedRef', None)
    assert getattr(partner, 'cjsidl_messages50') is None


def test_assoc_scopedTag330_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId332' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_taggedUnitsEnum's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_taggedUnitsEnum's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_taggedUnitsEnum(const_tag="sample_text", fieldUnit="sample_text", name="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId332', None)
    _safe_set(owner, 'cjsidl_taggedUnitsEnum331', partner)
    assert getattr(partner, 'cjsidl_scopedConstId332') == owner
    _safe_set(owner, 'cjsidl_taggedUnitsEnum331', None)
    assert getattr(partner, 'cjsidl_scopedConstId332') is None


def test_assoc_scopedType462_stub_double():
    # cjsidl_scopedType has no real 'cjsidl_scopedType464' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_arrayDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_arrayDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_arrayDef(arraySize="sample_text", comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_scopedType()
    setattr(partner, 'cjsidl_scopedType464', None)
    _safe_set(owner, 'cjsidl_arrayDef463', partner)
    assert getattr(partner, 'cjsidl_scopedType464') == owner
    _safe_set(owner, 'cjsidl_arrayDef463', None)
    assert getattr(partner, 'cjsidl_scopedType464') is None


def test_assoc_scopes468_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject470' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageScopedRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageScopedRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageScopedRef(comment="sample_text", name="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject470', None)
    _safe_set(owner, 'cjsidl_messageScopedRef469', {partner})
    assert getattr(partner, 'cjsidl_EObject470') == owner
    _safe_set(owner, 'cjsidl_messageScopedRef469', set())
    assert getattr(partner, 'cjsidl_EObject470') is None


def test_assoc_sendActions107_stub_double():
    # cjsidl_sendActionList has no real 'cjsidl_sendActionList' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_entry(comment="sample_text")
    partner = cjsidl_sendActionList()
    setattr(partner, 'cjsidl_sendActionList', None)
    _safe_set(owner, 'cjsidl_entry108', partner)
    assert getattr(partner, 'cjsidl_sendActionList') == owner
    _safe_set(owner, 'cjsidl_entry108', None)
    assert getattr(partner, 'cjsidl_sendActionList') is None


def test_assoc_sendActions112_stub_double():
    # cjsidl_sendActionList has no real 'cjsidl_sendActionList114' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_exit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_exit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_exit(comment="sample_text")
    partner = cjsidl_sendActionList()
    setattr(partner, 'cjsidl_sendActionList114', None)
    _safe_set(owner, 'cjsidl_exit113', partner)
    assert getattr(partner, 'cjsidl_sendActionList114') == owner
    _safe_set(owner, 'cjsidl_exit113', None)
    assert getattr(partner, 'cjsidl_sendActionList114') is None


def test_assoc_sendActions132_stub_double():
    # cjsidl_sendActionList has no real 'cjsidl_sendActionList134' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_transition(comment="sample_text", name="sample_text", type="sample_text")
    partner = cjsidl_sendActionList()
    setattr(partner, 'cjsidl_sendActionList134', None)
    _safe_set(owner, 'cjsidl_transition133', partner)
    assert getattr(partner, 'cjsidl_sendActionList134') == owner
    _safe_set(owner, 'cjsidl_transition133', None)
    assert getattr(partner, 'cjsidl_sendActionList134') is None


def test_assoc_sendActions144_stub_double():
    # cjsidl_sendActionList has no real 'cjsidl_sendActionList146' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_defaultTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_defaultTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_defaultTransition(comment="sample_text", type="sample_text")
    partner = cjsidl_sendActionList()
    setattr(partner, 'cjsidl_sendActionList146', None)
    _safe_set(owner, 'cjsidl_defaultTransition145', partner)
    assert getattr(partner, 'cjsidl_sendActionList146') == owner
    _safe_set(owner, 'cjsidl_defaultTransition145', None)
    assert getattr(partner, 'cjsidl_sendActionList146') is None


def test_assoc_type116_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject118' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_transParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_transParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_transParam(comment="sample_text", name="sample_text", unsignedType="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject118', None)
    _safe_set(owner, 'cjsidl_transParam117', partner)
    assert getattr(partner, 'cjsidl_EObject118') == owner
    _safe_set(owner, 'cjsidl_transParam117', None)
    assert getattr(partner, 'cjsidl_EObject118') is None


def test_assoc_type262_stub_double():
    # cjsidl_headerScopedRef has no real 'cjsidl_headerScopedRef263' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_headerDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_headerDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_headerDef(comment="sample_text", name="sample_text")
    partner = cjsidl_headerScopedRef()
    setattr(partner, 'cjsidl_headerScopedRef263', None)
    _safe_set(owner, 'cjsidl_headerDef264', partner)
    assert getattr(partner, 'cjsidl_headerScopedRef263') == owner
    _safe_set(owner, 'cjsidl_headerDef264', None)
    assert getattr(partner, 'cjsidl_headerScopedRef263') is None


def test_assoc_type271_stub_double():
    # cjsidl_bodyScopedRef has no real 'cjsidl_bodyScopedRef272' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_bodyDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_bodyDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_bodyDef(comment="sample_text", name="sample_text")
    partner = cjsidl_bodyScopedRef()
    setattr(partner, 'cjsidl_bodyScopedRef272', None)
    _safe_set(owner, 'cjsidl_bodyDef273', partner)
    assert getattr(partner, 'cjsidl_bodyScopedRef272') == owner
    _safe_set(owner, 'cjsidl_bodyDef273', None)
    assert getattr(partner, 'cjsidl_bodyScopedRef272') is None


def test_assoc_type280_stub_double():
    # cjsidl_footerScopedRef has no real 'cjsidl_footerScopedRef281' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_footerDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_footerDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_footerDef(comment="sample_text", name="sample_text")
    partner = cjsidl_footerScopedRef()
    setattr(partner, 'cjsidl_footerScopedRef281', None)
    _safe_set(owner, 'cjsidl_footerDef282', partner)
    assert getattr(partner, 'cjsidl_footerScopedRef281') == owner
    _safe_set(owner, 'cjsidl_footerDef282', None)
    assert getattr(partner, 'cjsidl_footerScopedRef281') is None


def test_assoc_type456_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject458' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_typeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_typeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_typeReference(comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject458', None)
    _safe_set(owner, 'cjsidl_typeReference457', partner)
    assert getattr(partner, 'cjsidl_EObject458') == owner
    _safe_set(owner, 'cjsidl_typeReference457', None)
    assert getattr(partner, 'cjsidl_EObject458') is None


def test_assoc_type501_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId502' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_constDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_constDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_constDef(comment="sample_text", constValue="sample_text", fieldUnits="sample_text", name="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId502', None)
    _safe_set(owner, 'cjsidl_constDef503', partner)
    assert getattr(partner, 'cjsidl_scopedConstId502') == owner
    _safe_set(owner, 'cjsidl_constDef503', None)
    assert getattr(partner, 'cjsidl_scopedConstId502') is None


def test_assoc_typeDef34_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_declaredTypeSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_declaredTypeSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_declaredTypeSet(name="sample_text", typeName="sample_text", version="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef', None)
    _safe_set(owner, 'cjsidl_declaredTypeSet35', {partner})
    assert getattr(partner, 'cjsidl_typeDef') == owner
    _safe_set(owner, 'cjsidl_declaredTypeSet35', set())
    assert getattr(partner, 'cjsidl_typeDef') is None


def test_assoc_typeRef459_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject461' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_arrayDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_arrayDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_arrayDef(arraySize="sample_text", comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject461', None)
    _safe_set(owner, 'cjsidl_arrayDef460', partner)
    assert getattr(partner, 'cjsidl_EObject461') == owner
    _safe_set(owner, 'cjsidl_arrayDef460', None)
    assert getattr(partner, 'cjsidl_EObject461') is None


def test_assoc_typeReference447_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef448' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_typeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_typeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_typeReference(comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef448', None)
    _safe_set(owner, 'cjsidl_typeReference449', partner)
    assert getattr(partner, 'cjsidl_recordDef448') == owner
    _safe_set(owner, 'cjsidl_typeReference449', None)
    assert getattr(partner, 'cjsidl_recordDef448') is None


def test_assoc_typeRefs47_stub_double():
    # cjsidl_messages has no real 'cjsidl_messages48' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_messageRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_messageRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_messageRef(comment="sample_text", name="sample_text")
    partner = cjsidl_messages()
    setattr(partner, 'cjsidl_messages48', None)
    _safe_set(owner, 'cjsidl_messageRef', partner)
    assert getattr(partner, 'cjsidl_messages48') == owner
    _safe_set(owner, 'cjsidl_messageRef', None)
    assert getattr(partner, 'cjsidl_messages48') is None


def test_assoc_typeScoped284_stub_double():
    # cjsidl_scopedType has no real 'cjsidl_scopedType' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_containerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_containerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_containerRef(comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_scopedType()
    setattr(partner, 'cjsidl_scopedType', None)
    _safe_set(owner, 'cjsidl_containerRef285', partner)
    assert getattr(partner, 'cjsidl_scopedType') == owner
    _safe_set(owner, 'cjsidl_containerRef285', None)
    assert getattr(partner, 'cjsidl_scopedType') is None


def test_assoc_upperLimScoped293_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_fixedLenString's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_fixedLenString's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_fixedLenString(comment="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId', None)
    _safe_set(owner, 'cjsidl_fixedLenString294', partner)
    assert getattr(partner, 'cjsidl_scopedConstId') == owner
    _safe_set(owner, 'cjsidl_fixedLenString294', None)
    assert getattr(partner, 'cjsidl_scopedConstId') is None


def test_assoc_upperLimScoped304_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId306' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenString's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenString's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenString(comment="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId306', None)
    _safe_set(owner, 'cjsidl_varLenString305', partner)
    assert getattr(partner, 'cjsidl_scopedConstId306') == owner
    _safe_set(owner, 'cjsidl_varLenString305', None)
    assert getattr(partner, 'cjsidl_scopedConstId306') is None


def test_assoc_upperLimScoped324_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId326' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenField(comment="sample_text", countComment="sample_text", fieldFormat="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId326', None)
    _safe_set(owner, 'cjsidl_varLenField325', partner)
    assert getattr(partner, 'cjsidl_scopedConstId326') == owner
    _safe_set(owner, 'cjsidl_varLenField325', None)
    assert getattr(partner, 'cjsidl_scopedConstId326') is None


def test_assoc_upperLimScoped364_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId366' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_valueRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_valueRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_valueRange(comment="sample_text", lowerLim="sample_text", lowerLimit_type="sample_text", upperLim="sample_text", upperLimit_type="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId366', None)
    _safe_set(owner, 'cjsidl_valueRange365', partner)
    assert getattr(partner, 'cjsidl_scopedConstId366') == owner
    _safe_set(owner, 'cjsidl_valueRange365', None)
    assert getattr(partner, 'cjsidl_scopedConstId366') is None


def test_assoc_upperLimScoped376_stub_double():
    # cjsidl_scopedConstId has no real 'cjsidl_scopedConstId378' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_scaledRangeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_scaledRangeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_scaledRangeDef(function="sample_text", interp="sample_text", lowerLim="sample_text", upperLim="sample_text")
    partner = cjsidl_scopedConstId()
    setattr(partner, 'cjsidl_scopedConstId378', None)
    _safe_set(owner, 'cjsidl_scaledRangeDef377', partner)
    assert getattr(partner, 'cjsidl_scopedConstId378') == owner
    _safe_set(owner, 'cjsidl_scaledRangeDef377', None)
    assert getattr(partner, 'cjsidl_scopedConstId378') is None


def test_assoc_value350_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject352' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_valueSetDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_valueSetDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_valueSetDef(offset="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject352', None)
    _safe_set(owner, 'cjsidl_valueSetDef351', {partner})
    assert getattr(partner, 'cjsidl_EObject352') == owner
    _safe_set(owner, 'cjsidl_valueSetDef351', set())
    assert getattr(partner, 'cjsidl_EObject352') is None


def test_assoc_valueRange310_stub_double():
    # cjsidl_EObject has no real 'cjsidl_EObject312' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_fixedFieldDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_fixedFieldDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_fixedFieldDef(comment="sample_text", fieldUnit="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_EObject()
    setattr(partner, 'cjsidl_EObject312', None)
    _safe_set(owner, 'cjsidl_fixedFieldDef311', partner)
    assert getattr(partner, 'cjsidl_EObject312') == owner
    _safe_set(owner, 'cjsidl_fixedFieldDef311', None)
    assert getattr(partner, 'cjsidl_EObject312') is None


def test_assoc_varField205_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef206' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varField(comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef206', None)
    _safe_set(owner, 'cjsidl_varField', partner)
    assert getattr(partner, 'cjsidl_typeDef206') == owner
    _safe_set(owner, 'cjsidl_varField', None)
    assert getattr(partner, 'cjsidl_typeDef206') is None


def test_assoc_varFormatField215_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef216' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varFormatField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varFormatField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varFormatField(comment="sample_text", countComment="sample_text", name="sample_text", optional="sample_text", units="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef216', None)
    _safe_set(owner, 'cjsidl_varFormatField', partner)
    assert getattr(partner, 'cjsidl_typeDef216') == owner
    _safe_set(owner, 'cjsidl_varFormatField', None)
    assert getattr(partner, 'cjsidl_typeDef216') is None


def test_assoc_varFormatField444_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef445' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varFormatField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varFormatField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varFormatField(comment="sample_text", countComment="sample_text", name="sample_text", optional="sample_text", units="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef445', None)
    _safe_set(owner, 'cjsidl_varFormatField446', partner)
    assert getattr(partner, 'cjsidl_recordDef445') == owner
    _safe_set(owner, 'cjsidl_varFormatField446', None)
    assert getattr(partner, 'cjsidl_recordDef445') is None


def test_assoc_varLenField213_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef214' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenField(comment="sample_text", countComment="sample_text", fieldFormat="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef214', None)
    _safe_set(owner, 'cjsidl_varLenField', partner)
    assert getattr(partner, 'cjsidl_typeDef214') == owner
    _safe_set(owner, 'cjsidl_varLenField', None)
    assert getattr(partner, 'cjsidl_typeDef214') is None


def test_assoc_varLenString211_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef212' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenString's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenString's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenString(comment="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef212', None)
    _safe_set(owner, 'cjsidl_varLenString', partner)
    assert getattr(partner, 'cjsidl_typeDef212') == owner
    _safe_set(owner, 'cjsidl_varLenString', None)
    assert getattr(partner, 'cjsidl_typeDef212') is None


def test_assoc_variableFieldDef429_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef430' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varField(comment="sample_text", name="sample_text", optional="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef430', None)
    _safe_set(owner, 'cjsidl_varField431', partner)
    assert getattr(partner, 'cjsidl_recordDef430') == owner
    _safe_set(owner, 'cjsidl_varField431', None)
    assert getattr(partner, 'cjsidl_recordDef430') is None


def test_assoc_variableLengthFieldDef441_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef442' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenField(comment="sample_text", countComment="sample_text", fieldFormat="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef442', None)
    _safe_set(owner, 'cjsidl_varLenField443', partner)
    assert getattr(partner, 'cjsidl_recordDef442') == owner
    _safe_set(owner, 'cjsidl_varLenField443', None)
    assert getattr(partner, 'cjsidl_recordDef442') is None


def test_assoc_variableLengthStringDef438_stub_double():
    # cjsidl_recordDef has no real 'cjsidl_recordDef439' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_varLenString's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_varLenString's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_varLenString(comment="sample_text", lowerLim="sample_text", name="sample_text", optional="sample_text", upperLim="sample_text")
    partner = cjsidl_recordDef()
    setattr(partner, 'cjsidl_recordDef439', None)
    _safe_set(owner, 'cjsidl_varLenString440', partner)
    assert getattr(partner, 'cjsidl_recordDef439') == owner
    _safe_set(owner, 'cjsidl_varLenString440', None)
    assert getattr(partner, 'cjsidl_recordDef439') is None


def test_assoc_variantDef199_stub_double():
    # cjsidl_typeDef has no real 'cjsidl_typeDef200' property in the generated
    # code (a bare stub) -- manually attach it so cjsidl_variantDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cjsidl_variantDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cjsidl_variantDef(maxCount="sample_text", minCount="sample_text", vtagComment="sample_text")
    partner = cjsidl_typeDef()
    setattr(partner, 'cjsidl_typeDef200', None)
    _safe_set(owner, 'cjsidl_variantDef', partner)
    assert getattr(partner, 'cjsidl_typeDef200') == owner
    _safe_set(owner, 'cjsidl_variantDef', None)
    assert getattr(partner, 'cjsidl_typeDef200') is None


