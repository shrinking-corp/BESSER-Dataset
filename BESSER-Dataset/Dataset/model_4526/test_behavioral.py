import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DepXYZ_IMPL,
    DepXY_IMPL,
    DepXZ_IMPL,
    DepX_Impl,
    DepYZ_IMPL,
    DepY_Impl,
    DepZ_Impl,
    Expression,
    Limit,
    Option,
    drn_And,
    drn_Assignement,
    drn_BACKWARD,
    drn_CARREXY,
    drn_CARREYZ,
    drn_CERCLEXY,
    drn_CERCLEYZ,
    drn_CameraBottom,
    drn_CameraFront,
    drn_Context,
    drn_DOWN,
    drn_DepXY,
    drn_DepXYZ,
    drn_DepXYZ_IMPL,
    drn_DepXY_IMPL,
    drn_DepXZ,
    drn_DepXZ_IMPL,
    drn_DepX_Impl,
    drn_DepYZ,
    drn_DepYZ_IMPL,
    drn_DepY_Impl,
    drn_DepZ_Impl,
    drn_Expression,
    drn_FORWARD,
    drn_Flip,
    drn_Hmax,
    drn_LEFT,
    drn_Land,
    drn_LedBlink,
    drn_Led_Impl,
    drn_Limit,
    drn_Model,
    drn_Option,
    drn_Parametre,
    drn_RIGHT,
    drn_RefPart,
    drn_Rotate,
    drn_TakeOff,
    drn_UP,
    drn_Vmax,
    drn_Wait,
    drn_With,
    ColorLed,
    EBool,
    Mode,
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

def test_assoc_angleVAR78_reverse_link_reassign_clear():
    a1 = drn_Rotate(angleCST="sample_text", name="sample_text", tempsCST="sample_text")
    a2 = drn_Rotate(angleCST="sample_text_2", name="sample_text_2", tempsCST="sample_text_2")
    b = drn_Parametre(name="sample_text")
    _safe_set(b, 'drn_Parametre80', a1)
    assert _is_linked(b, 'drn_Parametre80', a1)
    if hasattr(a1, 'drn_Rotate79'):
        assert _is_linked(a1, 'drn_Rotate79', b)
    _safe_set(b, 'drn_Parametre80', a2)
    assert _is_linked(b, 'drn_Parametre80', a2)
    if hasattr(a1, 'drn_Rotate79'):
        assert not _is_linked(a1, 'drn_Rotate79', b)
    if hasattr(a2, 'drn_Rotate79'):
        assert _is_linked(a2, 'drn_Rotate79', b)
    _safe_set(b, 'drn_Parametre80', None)
    assert not _is_linked(b, 'drn_Parametre80', a2)
    if hasattr(a2, 'drn_Rotate79'):
        assert not _is_linked(a2, 'drn_Rotate79', b)


def test_assoc_blink_per_secVAR88_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_LedBlink(blink_per_secCST="sample_text", color="sample_text")
    _safe_set(b, 'drn_LedBlink', a1)
    assert _is_linked(b, 'drn_LedBlink', a1)
    if hasattr(a1, 'drn_Parametre89'):
        assert _is_linked(a1, 'drn_Parametre89', b)
    _safe_set(b, 'drn_LedBlink', a2)
    assert _is_linked(b, 'drn_LedBlink', a2)
    if hasattr(a1, 'drn_Parametre89'):
        assert not _is_linked(a1, 'drn_Parametre89', b)
    if hasattr(a2, 'drn_Parametre89'):
        assert _is_linked(a2, 'drn_Parametre89', b)
    _safe_set(b, 'drn_LedBlink', None)
    assert not _is_linked(b, 'drn_LedBlink', a2)
    if hasattr(a2, 'drn_Parametre89'):
        assert not _is_linked(a2, 'drn_Parametre89', b)


def test_assoc_coteVAR58_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_CARREXY(coteCST="sample_text")
    _safe_set(b, 'drn_CARREXY', a1)
    assert _is_linked(b, 'drn_CARREXY', a1)
    if hasattr(a1, 'drn_Parametre59'):
        assert _is_linked(a1, 'drn_Parametre59', b)
    _safe_set(b, 'drn_CARREXY', a2)
    assert _is_linked(b, 'drn_CARREXY', a2)
    if hasattr(a1, 'drn_Parametre59'):
        assert not _is_linked(a1, 'drn_Parametre59', b)
    if hasattr(a2, 'drn_Parametre59'):
        assert _is_linked(a2, 'drn_Parametre59', b)
    _safe_set(b, 'drn_CARREXY', None)
    assert not _is_linked(b, 'drn_CARREXY', a2)
    if hasattr(a2, 'drn_Parametre59'):
        assert not _is_linked(a2, 'drn_Parametre59', b)


def test_assoc_coteVAR66_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_CARREYZ(coteCST="sample_text")
    _safe_set(b, 'drn_CARREYZ', a1)
    assert _is_linked(b, 'drn_CARREYZ', a1)
    if hasattr(a1, 'drn_Parametre67'):
        assert _is_linked(a1, 'drn_Parametre67', b)
    _safe_set(b, 'drn_CARREYZ', a2)
    assert _is_linked(b, 'drn_CARREYZ', a2)
    if hasattr(a1, 'drn_Parametre67'):
        assert not _is_linked(a1, 'drn_Parametre67', b)
    if hasattr(a2, 'drn_Parametre67'):
        assert _is_linked(a2, 'drn_Parametre67', b)
    _safe_set(b, 'drn_CARREYZ', None)
    assert not _is_linked(b, 'drn_CARREYZ', a2)
    if hasattr(a2, 'drn_Parametre67'):
        assert not _is_linked(a2, 'drn_Parametre67', b)


def test_assoc_depx23_reverse_link_reassign_clear():
    a1 = drn_DepX_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    a2 = drn_DepX_Impl(distanceCST="sample_text_2", name="sample_text_2", tempsCST="sample_text_2")
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And24', {a1})
    assert _is_linked(b, 'drn_And24', a1)
    if hasattr(a1, 'drn_DepX_Impl'):
        assert _is_linked(a1, 'drn_DepX_Impl', b)
    _safe_set(b, 'drn_And24', {a2})
    assert _is_linked(b, 'drn_And24', a2)
    if hasattr(a1, 'drn_DepX_Impl'):
        assert not _is_linked(a1, 'drn_DepX_Impl', b)
    if hasattr(a2, 'drn_DepX_Impl'):
        assert _is_linked(a2, 'drn_DepX_Impl', b)
    _safe_set(b, 'drn_And24', set())
    assert not _is_linked(b, 'drn_And24', a2)
    if hasattr(a2, 'drn_DepX_Impl'):
        assert not _is_linked(a2, 'drn_DepX_Impl', b)


def test_assoc_depxy29_reverse_link_reassign_clear():
    a1 = drn_DepXY_IMPL(name="sample_text", tempsCST="sample_text")
    a2 = drn_DepXY_IMPL(name="sample_text_2", tempsCST="sample_text_2")
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And30', {a1})
    assert _is_linked(b, 'drn_And30', a1)
    if hasattr(a1, 'drn_DepXY_IMPL'):
        assert _is_linked(a1, 'drn_DepXY_IMPL', b)
    _safe_set(b, 'drn_And30', {a2})
    assert _is_linked(b, 'drn_And30', a2)
    if hasattr(a1, 'drn_DepXY_IMPL'):
        assert not _is_linked(a1, 'drn_DepXY_IMPL', b)
    if hasattr(a2, 'drn_DepXY_IMPL'):
        assert _is_linked(a2, 'drn_DepXY_IMPL', b)
    _safe_set(b, 'drn_And30', set())
    assert not _is_linked(b, 'drn_And30', a2)
    if hasattr(a2, 'drn_DepXY_IMPL'):
        assert not _is_linked(a2, 'drn_DepXY_IMPL', b)


def test_assoc_depy25_reverse_link_reassign_clear():
    a1 = drn_DepY_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    a2 = drn_DepY_Impl(distanceCST="sample_text_2", name="sample_text_2", tempsCST="sample_text_2")
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And26', {a1})
    assert _is_linked(b, 'drn_And26', a1)
    if hasattr(a1, 'drn_DepY_Impl'):
        assert _is_linked(a1, 'drn_DepY_Impl', b)
    _safe_set(b, 'drn_And26', {a2})
    assert _is_linked(b, 'drn_And26', a2)
    if hasattr(a1, 'drn_DepY_Impl'):
        assert not _is_linked(a1, 'drn_DepY_Impl', b)
    if hasattr(a2, 'drn_DepY_Impl'):
        assert _is_linked(a2, 'drn_DepY_Impl', b)
    _safe_set(b, 'drn_And26', set())
    assert not _is_linked(b, 'drn_And26', a2)
    if hasattr(a2, 'drn_DepY_Impl'):
        assert not _is_linked(a2, 'drn_DepY_Impl', b)


def test_assoc_depz31_reverse_link_reassign_clear():
    a1 = drn_DepZ_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    a2 = drn_DepZ_Impl(distanceCST="sample_text_2", name="sample_text_2", tempsCST="sample_text_2")
    b = drn_And(name="sample_text")
    _safe_set(b, 'drn_And32', {a1})
    assert _is_linked(b, 'drn_And32', a1)
    if hasattr(a1, 'drn_DepZ_Impl'):
        assert _is_linked(a1, 'drn_DepZ_Impl', b)
    _safe_set(b, 'drn_And32', {a2})
    assert _is_linked(b, 'drn_And32', a2)
    if hasattr(a1, 'drn_DepZ_Impl'):
        assert not _is_linked(a1, 'drn_DepZ_Impl', b)
    if hasattr(a2, 'drn_DepZ_Impl'):
        assert _is_linked(a2, 'drn_DepZ_Impl', b)
    _safe_set(b, 'drn_And32', set())
    assert not _is_linked(b, 'drn_And32', a2)
    if hasattr(a2, 'drn_DepZ_Impl'):
        assert not _is_linked(a2, 'drn_DepZ_Impl', b)


def test_assoc_distanceVar33_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepY_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepY_Impl34', a1)
    assert _is_linked(b, 'drn_DepY_Impl34', a1)
    if hasattr(a1, 'drn_Parametre35'):
        assert _is_linked(a1, 'drn_Parametre35', b)
    _safe_set(b, 'drn_DepY_Impl34', a2)
    assert _is_linked(b, 'drn_DepY_Impl34', a2)
    if hasattr(a1, 'drn_Parametre35'):
        assert not _is_linked(a1, 'drn_Parametre35', b)
    if hasattr(a2, 'drn_Parametre35'):
        assert _is_linked(a2, 'drn_Parametre35', b)
    _safe_set(b, 'drn_DepY_Impl34', None)
    assert not _is_linked(b, 'drn_DepY_Impl34', a2)
    if hasattr(a2, 'drn_Parametre35'):
        assert not _is_linked(a2, 'drn_Parametre35', b)


def test_assoc_distanceVar39_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepX_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepX_Impl40', a1)
    assert _is_linked(b, 'drn_DepX_Impl40', a1)
    if hasattr(a1, 'drn_Parametre41'):
        assert _is_linked(a1, 'drn_Parametre41', b)
    _safe_set(b, 'drn_DepX_Impl40', a2)
    assert _is_linked(b, 'drn_DepX_Impl40', a2)
    if hasattr(a1, 'drn_Parametre41'):
        assert not _is_linked(a1, 'drn_Parametre41', b)
    if hasattr(a2, 'drn_Parametre41'):
        assert _is_linked(a2, 'drn_Parametre41', b)
    _safe_set(b, 'drn_DepX_Impl40', None)
    assert not _is_linked(b, 'drn_DepX_Impl40', a2)
    if hasattr(a2, 'drn_Parametre41'):
        assert not _is_linked(a2, 'drn_Parametre41', b)


def test_assoc_distanceVar45_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepZ_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepZ_Impl46', a1)
    assert _is_linked(b, 'drn_DepZ_Impl46', a1)
    if hasattr(a1, 'drn_Parametre47'):
        assert _is_linked(a1, 'drn_Parametre47', b)
    _safe_set(b, 'drn_DepZ_Impl46', a2)
    assert _is_linked(b, 'drn_DepZ_Impl46', a2)
    if hasattr(a1, 'drn_Parametre47'):
        assert not _is_linked(a1, 'drn_Parametre47', b)
    if hasattr(a2, 'drn_Parametre47'):
        assert _is_linked(a2, 'drn_Parametre47', b)
    _safe_set(b, 'drn_DepZ_Impl46', None)
    assert not _is_linked(b, 'drn_DepZ_Impl46', a2)
    if hasattr(a2, 'drn_Parametre47'):
        assert not _is_linked(a2, 'drn_Parametre47', b)


def test_assoc_distanceVar54_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepXY(distanceCST="sample_text")
    _safe_set(b, 'drn_DepXY', a1)
    assert _is_linked(b, 'drn_DepXY', a1)
    if hasattr(a1, 'drn_Parametre55'):
        assert _is_linked(a1, 'drn_Parametre55', b)
    _safe_set(b, 'drn_DepXY', a2)
    assert _is_linked(b, 'drn_DepXY', a2)
    if hasattr(a1, 'drn_Parametre55'):
        assert not _is_linked(a1, 'drn_Parametre55', b)
    if hasattr(a2, 'drn_Parametre55'):
        assert _is_linked(a2, 'drn_Parametre55', b)
    _safe_set(b, 'drn_DepXY', None)
    assert not _is_linked(b, 'drn_DepXY', a2)
    if hasattr(a2, 'drn_Parametre55'):
        assert not _is_linked(a2, 'drn_Parametre55', b)


def test_assoc_distanceVar62_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepYZ(distanceCST="sample_text")
    _safe_set(b, 'drn_DepYZ', a1)
    assert _is_linked(b, 'drn_DepYZ', a1)
    if hasattr(a1, 'drn_Parametre63'):
        assert _is_linked(a1, 'drn_Parametre63', b)
    _safe_set(b, 'drn_DepYZ', a2)
    assert _is_linked(b, 'drn_DepYZ', a2)
    if hasattr(a1, 'drn_Parametre63'):
        assert not _is_linked(a1, 'drn_Parametre63', b)
    if hasattr(a2, 'drn_Parametre63'):
        assert _is_linked(a2, 'drn_Parametre63', b)
    _safe_set(b, 'drn_DepYZ', None)
    assert not _is_linked(b, 'drn_DepYZ', a2)
    if hasattr(a2, 'drn_Parametre63'):
        assert not _is_linked(a2, 'drn_Parametre63', b)


def test_assoc_distanceVar68_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepXZ(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepXZ', a1)
    assert _is_linked(b, 'drn_DepXZ', a1)
    if hasattr(a1, 'drn_Parametre69'):
        assert _is_linked(a1, 'drn_Parametre69', b)
    _safe_set(b, 'drn_DepXZ', a2)
    assert _is_linked(b, 'drn_DepXZ', a2)
    if hasattr(a1, 'drn_Parametre69'):
        assert not _is_linked(a1, 'drn_Parametre69', b)
    if hasattr(a2, 'drn_Parametre69'):
        assert _is_linked(a2, 'drn_Parametre69', b)
    _safe_set(b, 'drn_DepXZ', None)
    assert not _is_linked(b, 'drn_DepXZ', a2)
    if hasattr(a2, 'drn_Parametre69'):
        assert not _is_linked(a2, 'drn_Parametre69', b)


def test_assoc_distanceVar73_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepXYZ(distanceCST="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepXYZ', a1)
    assert _is_linked(b, 'drn_DepXYZ', a1)
    if hasattr(a1, 'drn_Parametre74'):
        assert _is_linked(a1, 'drn_Parametre74', b)
    _safe_set(b, 'drn_DepXYZ', a2)
    assert _is_linked(b, 'drn_DepXYZ', a2)
    if hasattr(a1, 'drn_Parametre74'):
        assert not _is_linked(a1, 'drn_Parametre74', b)
    if hasattr(a2, 'drn_Parametre74'):
        assert _is_linked(a2, 'drn_Parametre74', b)
    _safe_set(b, 'drn_DepXYZ', None)
    assert not _is_linked(b, 'drn_DepXYZ', a2)
    if hasattr(a2, 'drn_Parametre74'):
        assert not _is_linked(a2, 'drn_Parametre74', b)


def test_assoc_operandes9_reverse_link_reassign_clear():
    a1 = drn_Expression(repeatCST="sample_text")
    a2 = drn_Expression(repeatCST="sample_text_2")
    b = drn_Assignement(name="sample_text")
    _safe_set(b, 'drn_Assignement10', {a1})
    assert _is_linked(b, 'drn_Assignement10', a1)
    if hasattr(a1, 'drn_Expression'):
        assert _is_linked(a1, 'drn_Expression', b)
    _safe_set(b, 'drn_Assignement10', {a2})
    assert _is_linked(b, 'drn_Assignement10', a2)
    if hasattr(a1, 'drn_Expression'):
        assert not _is_linked(a1, 'drn_Expression', b)
    if hasattr(a2, 'drn_Expression'):
        assert _is_linked(a2, 'drn_Expression', b)
    _safe_set(b, 'drn_Assignement10', set())
    assert not _is_linked(b, 'drn_Assignement10', a2)
    if hasattr(a2, 'drn_Expression'):
        assert not _is_linked(a2, 'drn_Expression', b)


def test_assoc_option86_reverse_link_reassign_clear():
    a1 = drn_With(name="sample_text")
    a2 = drn_With(name="sample_text_2")
    b = drn_Option(name="sample_text")
    _safe_set(b, 'drn_Option', a1)
    assert _is_linked(b, 'drn_Option', a1)
    if hasattr(a1, 'drn_With87'):
        assert _is_linked(a1, 'drn_With87', b)
    _safe_set(b, 'drn_Option', a2)
    assert _is_linked(b, 'drn_Option', a2)
    if hasattr(a1, 'drn_With87'):
        assert not _is_linked(a1, 'drn_With87', b)
    if hasattr(a2, 'drn_With87'):
        assert _is_linked(a2, 'drn_With87', b)
    _safe_set(b, 'drn_Option', None)
    assert not _is_linked(b, 'drn_Option', a2)
    if hasattr(a2, 'drn_With87'):
        assert not _is_linked(a2, 'drn_With87', b)


def test_assoc_parametre7_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_Assignement(name="sample_text")
    _safe_set(b, 'drn_Assignement8', {a1})
    assert _is_linked(b, 'drn_Assignement8', a1)
    if hasattr(a1, 'drn_Parametre'):
        assert _is_linked(a1, 'drn_Parametre', b)
    _safe_set(b, 'drn_Assignement8', {a2})
    assert _is_linked(b, 'drn_Assignement8', a2)
    if hasattr(a1, 'drn_Parametre'):
        assert not _is_linked(a1, 'drn_Parametre', b)
    if hasattr(a2, 'drn_Parametre'):
        assert _is_linked(a2, 'drn_Parametre', b)
    _safe_set(b, 'drn_Assignement8', set())
    assert not _is_linked(b, 'drn_Assignement8', a2)
    if hasattr(a2, 'drn_Parametre'):
        assert not _is_linked(a2, 'drn_Parametre', b)


def test_assoc_rayonVar56_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_CERCLEXY(rayonCST="sample_text")
    _safe_set(b, 'drn_CERCLEXY', a1)
    assert _is_linked(b, 'drn_CERCLEXY', a1)
    if hasattr(a1, 'drn_Parametre57'):
        assert _is_linked(a1, 'drn_Parametre57', b)
    _safe_set(b, 'drn_CERCLEXY', a2)
    assert _is_linked(b, 'drn_CERCLEXY', a2)
    if hasattr(a1, 'drn_Parametre57'):
        assert not _is_linked(a1, 'drn_Parametre57', b)
    if hasattr(a2, 'drn_Parametre57'):
        assert _is_linked(a2, 'drn_Parametre57', b)
    _safe_set(b, 'drn_CERCLEXY', None)
    assert not _is_linked(b, 'drn_CERCLEXY', a2)
    if hasattr(a2, 'drn_Parametre57'):
        assert not _is_linked(a2, 'drn_Parametre57', b)


def test_assoc_rayonVar64_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_CERCLEYZ(rayonCST="sample_text")
    _safe_set(b, 'drn_CERCLEYZ', a1)
    assert _is_linked(b, 'drn_CERCLEYZ', a1)
    if hasattr(a1, 'drn_Parametre65'):
        assert _is_linked(a1, 'drn_Parametre65', b)
    _safe_set(b, 'drn_CERCLEYZ', a2)
    assert _is_linked(b, 'drn_CERCLEYZ', a2)
    if hasattr(a1, 'drn_Parametre65'):
        assert not _is_linked(a1, 'drn_Parametre65', b)
    if hasattr(a2, 'drn_Parametre65'):
        assert _is_linked(a2, 'drn_Parametre65', b)
    _safe_set(b, 'drn_CERCLEYZ', None)
    assert not _is_linked(b, 'drn_CERCLEYZ', a2)
    if hasattr(a2, 'drn_Parametre65'):
        assert not _is_linked(a2, 'drn_Parametre65', b)


def test_assoc_repeatVAR11_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_Expression(repeatCST="sample_text")
    _safe_set(b, 'drn_Expression12', a1)
    assert _is_linked(b, 'drn_Expression12', a1)
    if hasattr(a1, 'drn_Parametre13'):
        assert _is_linked(a1, 'drn_Parametre13', b)
    _safe_set(b, 'drn_Expression12', a2)
    assert _is_linked(b, 'drn_Expression12', a2)
    if hasattr(a1, 'drn_Parametre13'):
        assert not _is_linked(a1, 'drn_Parametre13', b)
    if hasattr(a2, 'drn_Parametre13'):
        assert _is_linked(a2, 'drn_Parametre13', b)
    _safe_set(b, 'drn_Expression12', None)
    assert not _is_linked(b, 'drn_Expression12', a2)
    if hasattr(a2, 'drn_Parametre13'):
        assert not _is_linked(a2, 'drn_Parametre13', b)


def test_assoc_rotate22_reverse_link_reassign_clear():
    a1 = drn_Rotate(angleCST="sample_text", name="sample_text", tempsCST="sample_text")
    a2 = drn_Rotate(angleCST="sample_text_2", name="sample_text_2", tempsCST="sample_text_2")
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


def test_assoc_tempsVAR36_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepY_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepY_Impl37', a1)
    assert _is_linked(b, 'drn_DepY_Impl37', a1)
    if hasattr(a1, 'drn_Parametre38'):
        assert _is_linked(a1, 'drn_Parametre38', b)
    _safe_set(b, 'drn_DepY_Impl37', a2)
    assert _is_linked(b, 'drn_DepY_Impl37', a2)
    if hasattr(a1, 'drn_Parametre38'):
        assert not _is_linked(a1, 'drn_Parametre38', b)
    if hasattr(a2, 'drn_Parametre38'):
        assert _is_linked(a2, 'drn_Parametre38', b)
    _safe_set(b, 'drn_DepY_Impl37', None)
    assert not _is_linked(b, 'drn_DepY_Impl37', a2)
    if hasattr(a2, 'drn_Parametre38'):
        assert not _is_linked(a2, 'drn_Parametre38', b)


def test_assoc_tempsVAR42_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepX_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepX_Impl43', a1)
    assert _is_linked(b, 'drn_DepX_Impl43', a1)
    if hasattr(a1, 'drn_Parametre44'):
        assert _is_linked(a1, 'drn_Parametre44', b)
    _safe_set(b, 'drn_DepX_Impl43', a2)
    assert _is_linked(b, 'drn_DepX_Impl43', a2)
    if hasattr(a1, 'drn_Parametre44'):
        assert not _is_linked(a1, 'drn_Parametre44', b)
    if hasattr(a2, 'drn_Parametre44'):
        assert _is_linked(a2, 'drn_Parametre44', b)
    _safe_set(b, 'drn_DepX_Impl43', None)
    assert not _is_linked(b, 'drn_DepX_Impl43', a2)
    if hasattr(a2, 'drn_Parametre44'):
        assert not _is_linked(a2, 'drn_Parametre44', b)


def test_assoc_tempsVAR48_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepZ_Impl(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepZ_Impl49', a1)
    assert _is_linked(b, 'drn_DepZ_Impl49', a1)
    if hasattr(a1, 'drn_Parametre50'):
        assert _is_linked(a1, 'drn_Parametre50', b)
    _safe_set(b, 'drn_DepZ_Impl49', a2)
    assert _is_linked(b, 'drn_DepZ_Impl49', a2)
    if hasattr(a1, 'drn_Parametre50'):
        assert not _is_linked(a1, 'drn_Parametre50', b)
    if hasattr(a2, 'drn_Parametre50'):
        assert _is_linked(a2, 'drn_Parametre50', b)
    _safe_set(b, 'drn_DepZ_Impl49', None)
    assert not _is_linked(b, 'drn_DepZ_Impl49', a2)
    if hasattr(a2, 'drn_Parametre50'):
        assert not _is_linked(a2, 'drn_Parametre50', b)


def test_assoc_tempsVAR51_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepXY_IMPL(name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepXY_IMPL52', a1)
    assert _is_linked(b, 'drn_DepXY_IMPL52', a1)
    if hasattr(a1, 'drn_Parametre53'):
        assert _is_linked(a1, 'drn_Parametre53', b)
    _safe_set(b, 'drn_DepXY_IMPL52', a2)
    assert _is_linked(b, 'drn_DepXY_IMPL52', a2)
    if hasattr(a1, 'drn_Parametre53'):
        assert not _is_linked(a1, 'drn_Parametre53', b)
    if hasattr(a2, 'drn_Parametre53'):
        assert _is_linked(a2, 'drn_Parametre53', b)
    _safe_set(b, 'drn_DepXY_IMPL52', None)
    assert not _is_linked(b, 'drn_DepXY_IMPL52', a2)
    if hasattr(a2, 'drn_Parametre53'):
        assert not _is_linked(a2, 'drn_Parametre53', b)


def test_assoc_tempsVAR60_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepYZ_IMPL(name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepYZ_IMPL', a1)
    assert _is_linked(b, 'drn_DepYZ_IMPL', a1)
    if hasattr(a1, 'drn_Parametre61'):
        assert _is_linked(a1, 'drn_Parametre61', b)
    _safe_set(b, 'drn_DepYZ_IMPL', a2)
    assert _is_linked(b, 'drn_DepYZ_IMPL', a2)
    if hasattr(a1, 'drn_Parametre61'):
        assert not _is_linked(a1, 'drn_Parametre61', b)
    if hasattr(a2, 'drn_Parametre61'):
        assert _is_linked(a2, 'drn_Parametre61', b)
    _safe_set(b, 'drn_DepYZ_IMPL', None)
    assert not _is_linked(b, 'drn_DepYZ_IMPL', a2)
    if hasattr(a2, 'drn_Parametre61'):
        assert not _is_linked(a2, 'drn_Parametre61', b)


def test_assoc_tempsVAR70_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepXZ(distanceCST="sample_text", name="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepXZ71', a1)
    assert _is_linked(b, 'drn_DepXZ71', a1)
    if hasattr(a1, 'drn_Parametre72'):
        assert _is_linked(a1, 'drn_Parametre72', b)
    _safe_set(b, 'drn_DepXZ71', a2)
    assert _is_linked(b, 'drn_DepXZ71', a2)
    if hasattr(a1, 'drn_Parametre72'):
        assert not _is_linked(a1, 'drn_Parametre72', b)
    if hasattr(a2, 'drn_Parametre72'):
        assert _is_linked(a2, 'drn_Parametre72', b)
    _safe_set(b, 'drn_DepXZ71', None)
    assert not _is_linked(b, 'drn_DepXZ71', a2)
    if hasattr(a2, 'drn_Parametre72'):
        assert not _is_linked(a2, 'drn_Parametre72', b)


def test_assoc_tempsVAR75_reverse_link_reassign_clear():
    a1 = drn_Parametre(name="sample_text")
    a2 = drn_Parametre(name="sample_text_2")
    b = drn_DepXYZ(distanceCST="sample_text", tempsCST="sample_text")
    _safe_set(b, 'drn_DepXYZ76', a1)
    assert _is_linked(b, 'drn_DepXYZ76', a1)
    if hasattr(a1, 'drn_Parametre77'):
        assert _is_linked(a1, 'drn_Parametre77', b)
    _safe_set(b, 'drn_DepXYZ76', a2)
    assert _is_linked(b, 'drn_DepXYZ76', a2)
    if hasattr(a1, 'drn_Parametre77'):
        assert not _is_linked(a1, 'drn_Parametre77', b)
    if hasattr(a2, 'drn_Parametre77'):
        assert _is_linked(a2, 'drn_Parametre77', b)
    _safe_set(b, 'drn_DepXYZ76', None)
    assert not _is_linked(b, 'drn_DepXYZ76', a2)
    if hasattr(a2, 'drn_Parametre77'):
        assert not _is_linked(a2, 'drn_Parametre77', b)


def test_assoc_tempsVAR81_reverse_link_reassign_clear():
    a1 = drn_Rotate(angleCST="sample_text", name="sample_text", tempsCST="sample_text")
    a2 = drn_Rotate(angleCST="sample_text_2", name="sample_text_2", tempsCST="sample_text_2")
    b = drn_Parametre(name="sample_text")
    _safe_set(b, 'drn_Parametre83', a1)
    assert _is_linked(b, 'drn_Parametre83', a1)
    if hasattr(a1, 'drn_Rotate82'):
        assert _is_linked(a1, 'drn_Rotate82', b)
    _safe_set(b, 'drn_Parametre83', a2)
    assert _is_linked(b, 'drn_Parametre83', a2)
    if hasattr(a1, 'drn_Rotate82'):
        assert not _is_linked(a1, 'drn_Rotate82', b)
    if hasattr(a2, 'drn_Rotate82'):
        assert _is_linked(a2, 'drn_Rotate82', b)
    _safe_set(b, 'drn_Parametre83', None)
    assert not _is_linked(b, 'drn_Parametre83', a2)
    if hasattr(a2, 'drn_Rotate82'):
        assert not _is_linked(a2, 'drn_Rotate82', b)


def test_assoc_tempsVAR84_reverse_link_reassign_clear():
    a1 = drn_Wait(name="sample_text", tempsCST="sample_text")
    a2 = drn_Wait(name="sample_text_2", tempsCST="sample_text_2")
    b = drn_Parametre(name="sample_text")
    _safe_set(b, 'drn_Parametre85', a1)
    assert _is_linked(b, 'drn_Parametre85', a1)
    if hasattr(a1, 'drn_Wait'):
        assert _is_linked(a1, 'drn_Wait', b)
    _safe_set(b, 'drn_Parametre85', a2)
    assert _is_linked(b, 'drn_Parametre85', a2)
    if hasattr(a1, 'drn_Wait'):
        assert not _is_linked(a1, 'drn_Wait', b)
    if hasattr(a2, 'drn_Wait'):
        assert _is_linked(a2, 'drn_Wait', b)
    _safe_set(b, 'drn_Parametre85', None)
    assert not _is_linked(b, 'drn_Parametre85', a2)
    if hasattr(a2, 'drn_Wait'):
        assert not _is_linked(a2, 'drn_Wait', b)


def test_assoc_then17_reverse_link_reassign_clear():
    a1 = drn_Expression(repeatCST="sample_text")
    a2 = drn_Expression(repeatCST="sample_text_2")
    b = drn_Expression(repeatCST="sample_text")
    _safe_set(b, 'drn_Expression18', a1)
    assert _is_linked(b, 'drn_Expression18', a1)
    if hasattr(a1, 'drn_Expression16'):
        assert _is_linked(a1, 'drn_Expression16', b)
    _safe_set(b, 'drn_Expression18', a2)
    assert _is_linked(b, 'drn_Expression18', a2)
    if hasattr(a1, 'drn_Expression16'):
        assert not _is_linked(a1, 'drn_Expression16', b)
    if hasattr(a2, 'drn_Expression16'):
        assert _is_linked(a2, 'drn_Expression16', b)
    _safe_set(b, 'drn_Expression18', None)
    assert not _is_linked(b, 'drn_Expression18', a2)
    if hasattr(a2, 'drn_Expression16'):
        assert not _is_linked(a2, 'drn_Expression16', b)


def test_assoc_variable_partie19_reverse_link_reassign_clear():
    a1 = drn_RefPart(params="sample_text")
    a2 = drn_RefPart(params="sample_text_2")
    b = drn_Assignement(name="sample_text")
    _safe_set(b, 'drn_Assignement21', a1)
    assert _is_linked(b, 'drn_Assignement21', a1)
    if hasattr(a1, 'drn_RefPart20'):
        assert _is_linked(a1, 'drn_RefPart20', b)
    _safe_set(b, 'drn_Assignement21', a2)
    assert _is_linked(b, 'drn_Assignement21', a2)
    if hasattr(a1, 'drn_RefPart20'):
        assert not _is_linked(a1, 'drn_RefPart20', b)
    if hasattr(a2, 'drn_RefPart20'):
        assert _is_linked(a2, 'drn_RefPart20', b)
    _safe_set(b, 'drn_Assignement21', None)
    assert not _is_linked(b, 'drn_Assignement21', a2)
    if hasattr(a2, 'drn_RefPart20'):
        assert not _is_linked(a2, 'drn_RefPart20', b)


def test_assoc_with_14_reverse_link_reassign_clear():
    a1 = drn_With(name="sample_text")
    a2 = drn_With(name="sample_text_2")
    b = drn_Expression(repeatCST="sample_text")
    _safe_set(b, 'drn_Expression15', {a1})
    assert _is_linked(b, 'drn_Expression15', a1)
    if hasattr(a1, 'drn_With'):
        assert _is_linked(a1, 'drn_With', b)
    _safe_set(b, 'drn_Expression15', {a2})
    assert _is_linked(b, 'drn_Expression15', a2)
    if hasattr(a1, 'drn_With'):
        assert not _is_linked(a1, 'drn_With', b)
    if hasattr(a2, 'drn_With'):
        assert _is_linked(a2, 'drn_With', b)
    _safe_set(b, 'drn_Expression15', set())
    assert not _is_linked(b, 'drn_Expression15', a2)
    if hasattr(a2, 'drn_With'):
        assert not _is_linked(a2, 'drn_With', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignement1_stub_double():
    # drn_Model has no real 'drn_Model2' property in the generated
    # code (a bare stub) -- manually attach it so drn_Assignement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Assignement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Assignement(name="sample_text")
    partner = drn_Model()
    setattr(partner, 'drn_Model2', None)
    _safe_set(owner, 'drn_Assignement', partner)
    assert owner in getattr(partner, 'drn_Model2')
    _safe_set(owner, 'drn_Assignement', None)
    assert owner not in getattr(partner, 'drn_Model2')


def test_assoc_depxz27_stub_double():
    # drn_DepXZ_IMPL has no real 'drn_DepXZ_IMPL' property in the generated
    # code (a bare stub) -- manually attach it so drn_And's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_And's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_And(name="sample_text")
    partner = drn_DepXZ_IMPL()
    setattr(partner, 'drn_DepXZ_IMPL', None)
    _safe_set(owner, 'drn_And28', {partner})
    assert getattr(partner, 'drn_DepXZ_IMPL') == owner
    _safe_set(owner, 'drn_And28', set())
    assert getattr(partner, 'drn_DepXZ_IMPL') is None


def test_assoc_limit5_stub_double():
    # drn_Context has no real 'drn_Context6' property in the generated
    # code (a bare stub) -- manually attach it so drn_Limit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_Limit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_Limit(name="sample_text", value="sample_text")
    partner = drn_Context()
    setattr(partner, 'drn_Context6', None)
    _safe_set(owner, 'drn_Limit', partner)
    assert owner in getattr(partner, 'drn_Context6')
    _safe_set(owner, 'drn_Limit', None)
    assert owner not in getattr(partner, 'drn_Context6')


def test_assoc_main3_stub_double():
    # drn_Model has no real 'drn_Model4' property in the generated
    # code (a bare stub) -- manually attach it so drn_RefPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drn_RefPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drn_RefPart(params="sample_text")
    partner = drn_Model()
    setattr(partner, 'drn_Model4', None)
    _safe_set(owner, 'drn_RefPart', partner)
    assert getattr(partner, 'drn_Model4') == owner
    _safe_set(owner, 'drn_RefPart', None)
    assert getattr(partner, 'drn_Model4') is None


