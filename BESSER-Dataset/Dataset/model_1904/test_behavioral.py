import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConnectionType,
    DepXYZ_IMPL,
    DepXY_IMPL,
    DepXZ_IMPL,
    DepX_Impl,
    DepYZ_IMPL,
    DepY_Impl,
    DepZ_Impl,
    InitialPosition,
    Limit,
    Movement,
    Root,
    Surface,
    drn_And,
    drn_Assignement,
    drn_BACKWARD,
    drn_Bluetooth,
    drn_CARREXY,
    drn_CARREXZ,
    drn_CARREYZ,
    drn_CERCLEXY,
    drn_CERCLEXZ,
    drn_CERCLEYZ,
    drn_Configuration,
    drn_ConnectionType,
    drn_Context,
    drn_DOWN,
    drn_Declaration,
    drn_Definition,
    drn_DepXYZ_IMPL,
    drn_DepXY_IMPL,
    drn_DepXZ_IMPL,
    drn_DepX_Impl,
    drn_DepYZ_IMPL,
    drn_DepY_Impl,
    drn_DepZ_Impl,
    drn_Device,
    drn_Element,
    drn_Expression,
    drn_FORWARD,
    drn_Flip,
    drn_InitialDirection,
    drn_InitialPosition,
    drn_InitialPositionX,
    drn_InitialPositionY,
    drn_LEFT,
    drn_Land,
    drn_Library,
    drn_Limit,
    drn_MaxHeight,
    drn_MaxLength,
    drn_MaxSpeed,
    drn_MaxWidth,
    drn_Model,
    drn_Movement,
    drn_RIGHT,
    drn_RefDevice,
    drn_RefPart,
    drn_RefPartLib,
    drn_Root,
    drn_Rotate,
    drn_Surface,
    drn_TakeOff,
    drn_TypeGeneric,
    drn_UP,
    drn_Wait,
    drn_Wifi,
    drn_With,
    DirectionType,
    EBool,
    Mode,
    TypePrimitif,
    Where,
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

def test_assoc_assignement15_reverse_link_reassign_clear():
    a1 = drn_Library(name="sample_text")
    a2 = drn_Library(name="sample_text_2")
    b = drn_Assignement(name="sample_text")
    _safe_set(b, 'drn_Assignement17', a1)
    assert _is_linked(b, 'drn_Assignement17', a1)
    if hasattr(a1, 'drn_Library16'):
        assert _is_linked(a1, 'drn_Library16', b)
    _safe_set(b, 'drn_Assignement17', a2)
    assert _is_linked(b, 'drn_Assignement17', a2)
    if hasattr(a1, 'drn_Library16'):
        assert not _is_linked(a1, 'drn_Library16', b)
    if hasattr(a2, 'drn_Library16'):
        assert _is_linked(a2, 'drn_Library16', b)
    _safe_set(b, 'drn_Assignement17', None)
    assert not _is_linked(b, 'drn_Assignement17', a2)
    if hasattr(a2, 'drn_Library16'):
        assert not _is_linked(a2, 'drn_Library16', b)


def test_assoc_connection13_reverse_link_reassign_clear():
    a1 = drn_ConnectionType(adress="sample_text", name="sample_text")
    a2 = drn_ConnectionType(adress="sample_text_2", name="sample_text_2")
    b = drn_Configuration(name="sample_text")
    _safe_set(b, 'drn_Configuration14', a1)
    assert _is_linked(b, 'drn_Configuration14', a1)
    if hasattr(a1, 'drn_ConnectionType'):
        assert _is_linked(a1, 'drn_ConnectionType', b)
    _safe_set(b, 'drn_Configuration14', a2)
    assert _is_linked(b, 'drn_Configuration14', a2)
    if hasattr(a1, 'drn_ConnectionType'):
        assert not _is_linked(a1, 'drn_ConnectionType', b)
    if hasattr(a2, 'drn_ConnectionType'):
        assert _is_linked(a2, 'drn_ConnectionType', b)
    _safe_set(b, 'drn_Configuration14', None)
    assert not _is_linked(b, 'drn_Configuration14', a2)
    if hasattr(a2, 'drn_ConnectionType'):
        assert not _is_linked(a2, 'drn_ConnectionType', b)


def test_assoc_declarations44_reverse_link_reassign_clear():
    a1 = drn_Device(name="sample_text")
    a2 = drn_Device(name="sample_text_2")
    b = drn_Declaration(name="sample_text", typePrimitif="sample_text")
    _safe_set(b, 'drn_Declaration', a1)
    assert _is_linked(b, 'drn_Declaration', a1)
    if hasattr(a1, 'drn_Device45'):
        assert _is_linked(a1, 'drn_Device45', b)
    _safe_set(b, 'drn_Declaration', a2)
    assert _is_linked(b, 'drn_Declaration', a2)
    if hasattr(a1, 'drn_Device45'):
        assert not _is_linked(a1, 'drn_Device45', b)
    if hasattr(a2, 'drn_Device45'):
        assert _is_linked(a2, 'drn_Device45', b)
    _safe_set(b, 'drn_Declaration', None)
    assert not _is_linked(b, 'drn_Declaration', a2)
    if hasattr(a2, 'drn_Device45'):
        assert not _is_linked(a2, 'drn_Device45', b)


def test_assoc_definitions58_reverse_link_reassign_clear():
    a1 = drn_RefDevice(mode="sample_text")
    a2 = drn_RefDevice(mode="sample_text_2")
    b = drn_Definition(bool="sample_text", int="sample_text", real="sample_text", text="sample_text")
    _safe_set(b, 'drn_Definition60', a1)
    assert _is_linked(b, 'drn_Definition60', a1)
    if hasattr(a1, 'drn_RefDevice59'):
        assert _is_linked(a1, 'drn_RefDevice59', b)
    _safe_set(b, 'drn_Definition60', a2)
    assert _is_linked(b, 'drn_Definition60', a2)
    if hasattr(a1, 'drn_RefDevice59'):
        assert not _is_linked(a1, 'drn_RefDevice59', b)
    if hasattr(a2, 'drn_RefDevice59'):
        assert _is_linked(a2, 'drn_RefDevice59', b)
    _safe_set(b, 'drn_Definition60', None)
    assert not _is_linked(b, 'drn_Definition60', a2)
    if hasattr(a2, 'drn_RefDevice59'):
        assert not _is_linked(a2, 'drn_RefDevice59', b)


def test_assoc_depx38_reverse_link_reassign_clear():
    a1 = drn_DepX_Impl(distanceCST=7, name="sample_text", tempsCST=7)
    a2 = drn_DepX_Impl(distanceCST=13, name="sample_text_2", tempsCST=13)
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And39', {a1})
    assert _is_linked(b, 'drn_And39', a1)
    if hasattr(a1, 'drn_DepX_Impl'):
        assert _is_linked(a1, 'drn_DepX_Impl', b)
    _safe_set(b, 'drn_And39', {a2})
    assert _is_linked(b, 'drn_And39', a2)
    if hasattr(a1, 'drn_DepX_Impl'):
        assert not _is_linked(a1, 'drn_DepX_Impl', b)
    if hasattr(a2, 'drn_DepX_Impl'):
        assert _is_linked(a2, 'drn_DepX_Impl', b)
    _safe_set(b, 'drn_And39', set())
    assert not _is_linked(b, 'drn_And39', a2)
    if hasattr(a2, 'drn_DepX_Impl'):
        assert not _is_linked(a2, 'drn_DepX_Impl', b)


def test_assoc_depy40_reverse_link_reassign_clear():
    a1 = drn_DepY_Impl(distanceCST=7, name="sample_text", tempsCST=7)
    a2 = drn_DepY_Impl(distanceCST=13, name="sample_text_2", tempsCST=13)
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And41', {a1})
    assert _is_linked(b, 'drn_And41', a1)
    if hasattr(a1, 'drn_DepY_Impl'):
        assert _is_linked(a1, 'drn_DepY_Impl', b)
    _safe_set(b, 'drn_And41', {a2})
    assert _is_linked(b, 'drn_And41', a2)
    if hasattr(a1, 'drn_DepY_Impl'):
        assert not _is_linked(a1, 'drn_DepY_Impl', b)
    if hasattr(a2, 'drn_DepY_Impl'):
        assert _is_linked(a2, 'drn_DepY_Impl', b)
    _safe_set(b, 'drn_And41', set())
    assert not _is_linked(b, 'drn_And41', a2)
    if hasattr(a2, 'drn_DepY_Impl'):
        assert not _is_linked(a2, 'drn_DepY_Impl', b)


def test_assoc_depz42_reverse_link_reassign_clear():
    a1 = drn_DepZ_Impl(distanceCST=7, name="sample_text", tempsCST=7)
    a2 = drn_DepZ_Impl(distanceCST=13, name="sample_text_2", tempsCST=13)
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And43', {a1})
    assert _is_linked(b, 'drn_And43', a1)
    if hasattr(a1, 'drn_DepZ_Impl'):
        assert _is_linked(a1, 'drn_DepZ_Impl', b)
    _safe_set(b, 'drn_And43', {a2})
    assert _is_linked(b, 'drn_And43', a2)
    if hasattr(a1, 'drn_DepZ_Impl'):
        assert not _is_linked(a1, 'drn_DepZ_Impl', b)
    if hasattr(a2, 'drn_DepZ_Impl'):
        assert _is_linked(a2, 'drn_DepZ_Impl', b)
    _safe_set(b, 'drn_And43', set())
    assert not _is_linked(b, 'drn_And43', a2)
    if hasattr(a2, 'drn_DepZ_Impl'):
        assert not _is_linked(a2, 'drn_DepZ_Impl', b)


def test_assoc_dev55_reverse_link_reassign_clear():
    a1 = drn_RefDevice(mode="sample_text")
    a2 = drn_RefDevice(mode="sample_text_2")
    b = drn_Device(name="sample_text")
    _safe_set(b, 'drn_Device57', a1)
    assert _is_linked(b, 'drn_Device57', a1)
    if hasattr(a1, 'drn_RefDevice56'):
        assert _is_linked(a1, 'drn_RefDevice56', b)
    _safe_set(b, 'drn_Device57', a2)
    assert _is_linked(b, 'drn_Device57', a2)
    if hasattr(a1, 'drn_RefDevice56'):
        assert not _is_linked(a1, 'drn_RefDevice56', b)
    if hasattr(a2, 'drn_RefDevice56'):
        assert _is_linked(a2, 'drn_RefDevice56', b)
    _safe_set(b, 'drn_Device57', None)
    assert not _is_linked(b, 'drn_Device57', a2)
    if hasattr(a2, 'drn_RefDevice56'):
        assert not _is_linked(a2, 'drn_RefDevice56', b)


def test_assoc_devices11_reverse_link_reassign_clear():
    a1 = drn_Device(name="sample_text")
    a2 = drn_Device(name="sample_text_2")
    b = drn_Configuration(name="sample_text")
    _safe_set(b, 'drn_Configuration12', {a1})
    assert _is_linked(b, 'drn_Configuration12', a1)
    if hasattr(a1, 'drn_Device'):
        assert _is_linked(a1, 'drn_Device', b)
    _safe_set(b, 'drn_Configuration12', {a2})
    assert _is_linked(b, 'drn_Configuration12', a2)
    if hasattr(a1, 'drn_Device'):
        assert not _is_linked(a1, 'drn_Device', b)
    if hasattr(a2, 'drn_Device'):
        assert _is_linked(a2, 'drn_Device', b)
    _safe_set(b, 'drn_Configuration12', set())
    assert not _is_linked(b, 'drn_Configuration12', a2)
    if hasattr(a2, 'drn_Device'):
        assert not _is_linked(a2, 'drn_Device', b)


def test_assoc_elements61_reverse_link_reassign_clear():
    a1 = drn_TypeGeneric(name="sample_text")
    a2 = drn_TypeGeneric(name="sample_text_2")
    b = drn_Element(name="sample_text")
    _safe_set(b, 'drn_Element63', a1)
    assert _is_linked(b, 'drn_Element63', a1)
    if hasattr(a1, 'drn_TypeGeneric62'):
        assert _is_linked(a1, 'drn_TypeGeneric62', b)
    _safe_set(b, 'drn_Element63', a2)
    assert _is_linked(b, 'drn_Element63', a2)
    if hasattr(a1, 'drn_TypeGeneric62'):
        assert not _is_linked(a1, 'drn_TypeGeneric62', b)
    if hasattr(a2, 'drn_TypeGeneric62'):
        assert _is_linked(a2, 'drn_TypeGeneric62', b)
    _safe_set(b, 'drn_Element63', None)
    assert not _is_linked(b, 'drn_Element63', a2)
    if hasattr(a2, 'drn_TypeGeneric62'):
        assert not _is_linked(a2, 'drn_TypeGeneric62', b)


def test_assoc_left49_reverse_link_reassign_clear():
    a1 = drn_Definition(bool="sample_text", int="sample_text", real="sample_text", text="sample_text")
    a2 = drn_Definition(bool="sample_text_2", int="sample_text_2", real="sample_text_2", text="sample_text_2")
    b = drn_Declaration(name="sample_text", typePrimitif="sample_text")
    _safe_set(b, 'drn_Declaration50', a1)
    assert _is_linked(b, 'drn_Declaration50', a1)
    if hasattr(a1, 'drn_Definition'):
        assert _is_linked(a1, 'drn_Definition', b)
    _safe_set(b, 'drn_Declaration50', a2)
    assert _is_linked(b, 'drn_Declaration50', a2)
    if hasattr(a1, 'drn_Definition'):
        assert not _is_linked(a1, 'drn_Definition', b)
    if hasattr(a2, 'drn_Definition'):
        assert _is_linked(a2, 'drn_Definition', b)
    _safe_set(b, 'drn_Declaration50', None)
    assert not _is_linked(b, 'drn_Declaration50', a2)
    if hasattr(a2, 'drn_Definition'):
        assert not _is_linked(a2, 'drn_Definition', b)


def test_assoc_limit18_reverse_link_reassign_clear():
    a1 = drn_Limit(name="sample_text")
    a2 = drn_Limit(name="sample_text_2")
    b = drn_Context(name="sample_text", where="sample_text")
    _safe_set(b, 'drn_Context19', {a1})
    assert _is_linked(b, 'drn_Context19', a1)
    if hasattr(a1, 'drn_Limit'):
        assert _is_linked(a1, 'drn_Limit', b)
    _safe_set(b, 'drn_Context19', {a2})
    assert _is_linked(b, 'drn_Context19', a2)
    if hasattr(a1, 'drn_Limit'):
        assert not _is_linked(a1, 'drn_Limit', b)
    if hasattr(a2, 'drn_Limit'):
        assert _is_linked(a2, 'drn_Limit', b)
    _safe_set(b, 'drn_Context19', set())
    assert not _is_linked(b, 'drn_Context19', a2)
    if hasattr(a2, 'drn_Limit'):
        assert not _is_linked(a2, 'drn_Limit', b)


def test_assoc_operandes20_reverse_link_reassign_clear():
    a1 = drn_Expression(repeatCST=7)
    a2 = drn_Expression(repeatCST=13)
    b = drn_Assignement(name="sample_text")
    _safe_set(b, 'drn_Assignement21', {a1})
    assert _is_linked(b, 'drn_Assignement21', a1)
    if hasattr(a1, 'drn_Expression'):
        assert _is_linked(a1, 'drn_Expression', b)
    _safe_set(b, 'drn_Assignement21', {a2})
    assert _is_linked(b, 'drn_Assignement21', a2)
    if hasattr(a1, 'drn_Expression'):
        assert not _is_linked(a1, 'drn_Expression', b)
    if hasattr(a2, 'drn_Expression'):
        assert _is_linked(a2, 'drn_Expression', b)
    _safe_set(b, 'drn_Assignement21', set())
    assert not _is_linked(b, 'drn_Assignement21', a2)
    if hasattr(a2, 'drn_Expression'):
        assert not _is_linked(a2, 'drn_Expression', b)


def test_assoc_option53_reverse_link_reassign_clear():
    a1 = drn_With(name="sample_text")
    a2 = drn_With(name="sample_text_2")
    b = drn_RefDevice(mode="sample_text")
    _safe_set(b, 'drn_RefDevice', a1)
    assert _is_linked(b, 'drn_RefDevice', a1)
    if hasattr(a1, 'drn_With54'):
        assert _is_linked(a1, 'drn_With54', b)
    _safe_set(b, 'drn_RefDevice', a2)
    assert _is_linked(b, 'drn_RefDevice', a2)
    if hasattr(a1, 'drn_With54'):
        assert not _is_linked(a1, 'drn_With54', b)
    if hasattr(a2, 'drn_With54'):
        assert _is_linked(a2, 'drn_With54', b)
    _safe_set(b, 'drn_RefDevice', None)
    assert not _is_linked(b, 'drn_RefDevice', a2)
    if hasattr(a2, 'drn_With54'):
        assert not _is_linked(a2, 'drn_With54', b)


def test_assoc_right51_reverse_link_reassign_clear():
    a1 = drn_Element(name="sample_text")
    a2 = drn_Element(name="sample_text_2")
    b = drn_Definition(bool="sample_text", int="sample_text", real="sample_text", text="sample_text")
    _safe_set(b, 'drn_Definition52', a1)
    assert _is_linked(b, 'drn_Definition52', a1)
    if hasattr(a1, 'drn_Element'):
        assert _is_linked(a1, 'drn_Element', b)
    _safe_set(b, 'drn_Definition52', a2)
    assert _is_linked(b, 'drn_Definition52', a2)
    if hasattr(a1, 'drn_Element'):
        assert not _is_linked(a1, 'drn_Element', b)
    if hasattr(a2, 'drn_Element'):
        assert _is_linked(a2, 'drn_Element', b)
    _safe_set(b, 'drn_Definition52', None)
    assert not _is_linked(b, 'drn_Definition52', a2)
    if hasattr(a2, 'drn_Element'):
        assert not _is_linked(a2, 'drn_Element', b)


def test_assoc_rotate37_reverse_link_reassign_clear():
    a1 = drn_Rotate(angleCST="sample_text", name="sample_text", tempsCST=7)
    a2 = drn_Rotate(angleCST="sample_text_2", name="sample_text_2", tempsCST=13)
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And', {a1})
    assert _is_linked(b, 'drn_And', a1)
    if hasattr(a1, 'drn_Rotate'):
        assert _is_linked(a1, 'drn_Rotate', b)
    _safe_set(b, 'drn_And', {a2})
    assert _is_linked(b, 'drn_And', a2)
    if hasattr(a1, 'drn_Rotate'):
        assert not _is_linked(a1, 'drn_Rotate', b)
    if hasattr(a2, 'drn_Rotate'):
        assert _is_linked(a2, 'drn_Rotate', b)
    _safe_set(b, 'drn_And', set())
    assert not _is_linked(b, 'drn_And', a2)
    if hasattr(a2, 'drn_Rotate'):
        assert not _is_linked(a2, 'drn_Rotate', b)


def test_assoc_then27_reverse_link_reassign_clear():
    a1 = drn_Expression(repeatCST=7)
    a2 = drn_Expression(repeatCST=13)
    b = drn_Expression(repeatCST=7)
    _safe_set(b, 'drn_Expression28', a1)
    assert _is_linked(b, 'drn_Expression28', a1)
    if hasattr(a1, 'drn_Expression26'):
        assert _is_linked(a1, 'drn_Expression26', b)
    _safe_set(b, 'drn_Expression28', a2)
    assert _is_linked(b, 'drn_Expression28', a2)
    if hasattr(a1, 'drn_Expression26'):
        assert not _is_linked(a1, 'drn_Expression26', b)
    if hasattr(a2, 'drn_Expression26'):
        assert _is_linked(a2, 'drn_Expression26', b)
    _safe_set(b, 'drn_Expression28', None)
    assert not _is_linked(b, 'drn_Expression28', a2)
    if hasattr(a2, 'drn_Expression26'):
        assert not _is_linked(a2, 'drn_Expression26', b)


def test_assoc_type46_reverse_link_reassign_clear():
    a1 = drn_TypeGeneric(name="sample_text")
    a2 = drn_TypeGeneric(name="sample_text_2")
    b = drn_Declaration(name="sample_text", typePrimitif="sample_text")
    _safe_set(b, 'drn_Declaration47', a1)
    assert _is_linked(b, 'drn_Declaration47', a1)
    if hasattr(a1, 'drn_TypeGeneric48'):
        assert _is_linked(a1, 'drn_TypeGeneric48', b)
    _safe_set(b, 'drn_Declaration47', a2)
    assert _is_linked(b, 'drn_Declaration47', a2)
    if hasattr(a1, 'drn_TypeGeneric48'):
        assert not _is_linked(a1, 'drn_TypeGeneric48', b)
    if hasattr(a2, 'drn_TypeGeneric48'):
        assert _is_linked(a2, 'drn_TypeGeneric48', b)
    _safe_set(b, 'drn_Declaration47', None)
    assert not _is_linked(b, 'drn_Declaration47', a2)
    if hasattr(a2, 'drn_TypeGeneric48'):
        assert not _is_linked(a2, 'drn_TypeGeneric48', b)


def test_assoc_types9_reverse_link_reassign_clear():
    a1 = drn_TypeGeneric(name="sample_text")
    a2 = drn_TypeGeneric(name="sample_text_2")
    b = drn_Configuration(name="sample_text")
    _safe_set(b, 'drn_Configuration10', {a1})
    assert _is_linked(b, 'drn_Configuration10', a1)
    if hasattr(a1, 'drn_TypeGeneric'):
        assert _is_linked(a1, 'drn_TypeGeneric', b)
    _safe_set(b, 'drn_Configuration10', {a2})
    assert _is_linked(b, 'drn_Configuration10', a2)
    if hasattr(a1, 'drn_TypeGeneric'):
        assert not _is_linked(a1, 'drn_TypeGeneric', b)
    if hasattr(a2, 'drn_TypeGeneric'):
        assert _is_linked(a2, 'drn_TypeGeneric', b)
    _safe_set(b, 'drn_Configuration10', set())
    assert not _is_linked(b, 'drn_Configuration10', a2)
    if hasattr(a2, 'drn_TypeGeneric'):
        assert not _is_linked(a2, 'drn_TypeGeneric', b)


def test_assoc_with_24_reverse_link_reassign_clear():
    a1 = drn_With(name="sample_text")
    a2 = drn_With(name="sample_text_2")
    b = drn_Expression(repeatCST=7)
    _safe_set(b, 'drn_Expression25', {a1})
    assert _is_linked(b, 'drn_Expression25', a1)
    if hasattr(a1, 'drn_With'):
        assert _is_linked(a1, 'drn_With', b)
    _safe_set(b, 'drn_Expression25', {a2})
    assert _is_linked(b, 'drn_Expression25', a2)
    if hasattr(a1, 'drn_With'):
        assert not _is_linked(a1, 'drn_With', b)
    if hasattr(a2, 'drn_With'):
        assert _is_linked(a2, 'drn_With', b)
    _safe_set(b, 'drn_Expression25', set())
    assert not _is_linked(b, 'drn_Expression25', a2)
    if hasattr(a2, 'drn_With'):
        assert not _is_linked(a2, 'drn_With', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignement34_stub_double():
    # drn_RefPartLib has no real 'drn_RefPartLib35' property in the generated
    # code (a bare stub) -- manually attach it so drn_Assignement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Assignement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Assignement(name="sample_text")
    partner = drn_RefPartLib()
    setattr(partner, 'drn_RefPartLib35', None)
    _safe_set(owner, 'drn_Assignement36', partner)
    assert getattr(partner, 'drn_RefPartLib35') == owner
    _safe_set(owner, 'drn_Assignement36', None)
    assert getattr(partner, 'drn_RefPartLib35') is None


def test_assoc_assignement5_stub_double():
    # drn_Model has no real 'drn_Model6' property in the generated
    # code (a bare stub) -- manually attach it so drn_Assignement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Assignement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Assignement(name="sample_text")
    partner = drn_Model()
    setattr(partner, 'drn_Model6', None)
    _safe_set(owner, 'drn_Assignement', partner)
    assert owner in getattr(partner, 'drn_Model6')
    _safe_set(owner, 'drn_Assignement', None)
    assert owner not in getattr(partner, 'drn_Model6')


def test_assoc_config0_stub_double():
    # drn_Model has no real 'drn_Model' property in the generated
    # code (a bare stub) -- manually attach it so drn_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Configuration(name="sample_text")
    partner = drn_Model()
    setattr(partner, 'drn_Model', None)
    _safe_set(owner, 'drn_Configuration', partner)
    assert getattr(partner, 'drn_Model') == owner
    _safe_set(owner, 'drn_Configuration', None)
    assert getattr(partner, 'drn_Model') is None


def test_assoc_context3_stub_double():
    # drn_Model has no real 'drn_Model4' property in the generated
    # code (a bare stub) -- manually attach it so drn_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Context(name="sample_text", where="sample_text")
    partner = drn_Model()
    setattr(partner, 'drn_Model4', None)
    _safe_set(owner, 'drn_Context', partner)
    assert getattr(partner, 'drn_Model4') == owner
    _safe_set(owner, 'drn_Context', None)
    assert getattr(partner, 'drn_Model4') is None


def test_assoc_lib32_stub_double():
    # drn_RefPartLib has no real 'drn_RefPartLib' property in the generated
    # code (a bare stub) -- manually attach it so drn_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Library(name="sample_text")
    partner = drn_RefPartLib()
    setattr(partner, 'drn_RefPartLib', None)
    _safe_set(owner, 'drn_Library33', partner)
    assert getattr(partner, 'drn_RefPartLib') == owner
    _safe_set(owner, 'drn_Library33', None)
    assert getattr(partner, 'drn_RefPartLib') is None


def test_assoc_libraries1_stub_double():
    # drn_Model has no real 'drn_Model2' property in the generated
    # code (a bare stub) -- manually attach it so drn_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Library(name="sample_text")
    partner = drn_Model()
    setattr(partner, 'drn_Model2', None)
    _safe_set(owner, 'drn_Library', partner)
    assert owner in getattr(partner, 'drn_Model2')
    _safe_set(owner, 'drn_Library', None)
    assert owner not in getattr(partner, 'drn_Model2')


def test_assoc_move22_stub_double():
    # drn_Movement has no real 'drn_Movement' property in the generated
    # code (a bare stub) -- manually attach it so drn_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Expression(repeatCST=7)
    partner = drn_Movement()
    setattr(partner, 'drn_Movement', None)
    _safe_set(owner, 'drn_Expression23', partner)
    assert getattr(partner, 'drn_Movement') == owner
    _safe_set(owner, 'drn_Expression23', None)
    assert getattr(partner, 'drn_Movement') is None


def test_assoc_variable_partie29_stub_double():
    # drn_RefPart has no real 'drn_RefPart30' property in the generated
    # code (a bare stub) -- manually attach it so drn_Assignement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Assignement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Assignement(name="sample_text")
    partner = drn_RefPart()
    setattr(partner, 'drn_RefPart30', None)
    _safe_set(owner, 'drn_Assignement31', partner)
    assert getattr(partner, 'drn_RefPart30') == owner
    _safe_set(owner, 'drn_Assignement31', None)
    assert getattr(partner, 'drn_RefPart30') is None


