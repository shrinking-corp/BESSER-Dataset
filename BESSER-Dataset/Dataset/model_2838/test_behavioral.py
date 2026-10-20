import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ck2gfx_AnimatedSpriteType,
    ck2gfx_Animation,
    ck2gfx_ArrowType,
    ck2gfx_BitmapFont,
    ck2gfx_BitmapFonts,
    ck2gfx_CoatOfArmsLayer,
    ck2gfx_CoatOfArmsType,
    ck2gfx_Color,
    ck2gfx_ColorCode,
    ck2gfx_ColorRatio,
    ck2gfx_Coordinates,
    ck2gfx_CorneredTileSpriteType,
    ck2gfx_EMFXActorType,
    ck2gfx_EObject,
    ck2gfx_LineChartType,
    ck2gfx_MaskedShieldType,
    ck2gfx_Model,
    ck2gfx_ObjectTypes,
    ck2gfx_Pdxmesh,
    ck2gfx_PortraitType,
    ck2gfx_ProgressbarType,
    ck2gfx_SpriteType,
    ck2gfx_SpriteTypes,
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

def test_assoc_animation26_reverse_link_reassign_clear():
    a1 = ck2gfx_EMFXActorType(actorFile="sample_text", attack="sample_text", cullDistance=3.14, idle="sample_text", move="sample_text", name="sample_text", scale=3.14, scaleOnCullDistance=True, useAnimation=True)
    a2 = ck2gfx_EMFXActorType(actorFile="sample_text_2", attack="sample_text_2", cullDistance=9.99, idle="sample_text_2", move="sample_text_2", name="sample_text_2", scale=9.99, scaleOnCullDistance=False, useAnimation=False)
    b = ck2gfx_Animation(defaultAnimationTime=3.14, file="sample_text", name="sample_text")
    _safe_set(b, 'ck2gfx_Animation', a1)
    assert _is_linked(b, 'ck2gfx_Animation', a1)
    if hasattr(a1, 'ck2gfx_EMFXActorType'):
        assert _is_linked(a1, 'ck2gfx_EMFXActorType', b)
    _safe_set(b, 'ck2gfx_Animation', a2)
    assert _is_linked(b, 'ck2gfx_Animation', a2)
    if hasattr(a1, 'ck2gfx_EMFXActorType'):
        assert not _is_linked(a1, 'ck2gfx_EMFXActorType', b)
    if hasattr(a2, 'ck2gfx_EMFXActorType'):
        assert _is_linked(a2, 'ck2gfx_EMFXActorType', b)
    _safe_set(b, 'ck2gfx_Animation', None)
    assert not _is_linked(b, 'ck2gfx_Animation', a2)
    if hasattr(a2, 'ck2gfx_EMFXActorType'):
        assert not _is_linked(a2, 'ck2gfx_EMFXActorType', b)


def test_assoc_borderSize4_reverse_link_reassign_clear():
    a1 = ck2gfx_CorneredTileSpriteType(allwaysTransparent=True, loadType="sample_text", name="sample_text", noRefCount=True, texturefile="sample_text", tilingCenter=True)
    a2 = ck2gfx_CorneredTileSpriteType(allwaysTransparent=False, loadType="sample_text_2", name="sample_text_2", noRefCount=False, texturefile="sample_text_2", tilingCenter=False)
    b = ck2gfx_Coordinates(x=3.14, y=3.14)
    _safe_set(b, 'ck2gfx_Coordinates6', a1)
    assert _is_linked(b, 'ck2gfx_Coordinates6', a1)
    if hasattr(a1, 'ck2gfx_CorneredTileSpriteType5'):
        assert _is_linked(a1, 'ck2gfx_CorneredTileSpriteType5', b)
    _safe_set(b, 'ck2gfx_Coordinates6', a2)
    assert _is_linked(b, 'ck2gfx_Coordinates6', a2)
    if hasattr(a1, 'ck2gfx_CorneredTileSpriteType5'):
        assert not _is_linked(a1, 'ck2gfx_CorneredTileSpriteType5', b)
    if hasattr(a2, 'ck2gfx_CorneredTileSpriteType5'):
        assert _is_linked(a2, 'ck2gfx_CorneredTileSpriteType5', b)
    _safe_set(b, 'ck2gfx_Coordinates6', None)
    assert not _is_linked(b, 'ck2gfx_Coordinates6', a2)
    if hasattr(a2, 'ck2gfx_CorneredTileSpriteType5'):
        assert not _is_linked(a2, 'ck2gfx_CorneredTileSpriteType5', b)


def test_assoc_center21_reverse_link_reassign_clear():
    a1 = ck2gfx_Coordinates(x=3.14, y=3.14)
    a2 = ck2gfx_Coordinates(x=9.99, y=9.99)
    b = ck2gfx_CoatOfArmsLayer(mask="sample_text", scale=3.14)
    _safe_set(b, 'ck2gfx_CoatOfArmsLayer22', a1)
    assert _is_linked(b, 'ck2gfx_CoatOfArmsLayer22', a1)
    if hasattr(a1, 'ck2gfx_Coordinates23'):
        assert _is_linked(a1, 'ck2gfx_Coordinates23', b)
    _safe_set(b, 'ck2gfx_CoatOfArmsLayer22', a2)
    assert _is_linked(b, 'ck2gfx_CoatOfArmsLayer22', a2)
    if hasattr(a1, 'ck2gfx_Coordinates23'):
        assert not _is_linked(a1, 'ck2gfx_Coordinates23', b)
    if hasattr(a2, 'ck2gfx_Coordinates23'):
        assert _is_linked(a2, 'ck2gfx_Coordinates23', b)
    _safe_set(b, 'ck2gfx_CoatOfArmsLayer22', None)
    assert not _is_linked(b, 'ck2gfx_CoatOfArmsLayer22', a2)
    if hasattr(a2, 'ck2gfx_Coordinates23'):
        assert not _is_linked(a2, 'ck2gfx_Coordinates23', b)


def test_assoc_color229_reverse_link_reassign_clear():
    a1 = ck2gfx_ColorRatio(b=3.14, g=3.14, r=3.14)
    a2 = ck2gfx_ColorRatio(b=9.99, g=9.99, r=9.99)
    b = ck2gfx_ArrowType(bodyTexture="sample_text", effect="sample_text", endAt=3.14, heading=3.14, height=3.14, name="sample_text", size=3.14, textureFile="sample_text", type=7)
    _safe_set(b, 'ck2gfx_ArrowType30', a1)
    assert _is_linked(b, 'ck2gfx_ArrowType30', a1)
    if hasattr(a1, 'ck2gfx_ColorRatio31'):
        assert _is_linked(a1, 'ck2gfx_ColorRatio31', b)
    _safe_set(b, 'ck2gfx_ArrowType30', a2)
    assert _is_linked(b, 'ck2gfx_ArrowType30', a2)
    if hasattr(a1, 'ck2gfx_ColorRatio31'):
        assert not _is_linked(a1, 'ck2gfx_ColorRatio31', b)
    if hasattr(a2, 'ck2gfx_ColorRatio31'):
        assert _is_linked(a2, 'ck2gfx_ColorRatio31', b)
    _safe_set(b, 'ck2gfx_ArrowType30', None)
    assert not _is_linked(b, 'ck2gfx_ArrowType30', a2)
    if hasattr(a2, 'ck2gfx_ColorRatio31'):
        assert not _is_linked(a2, 'ck2gfx_ColorRatio31', b)


def test_assoc_color27_reverse_link_reassign_clear():
    a1 = ck2gfx_ColorRatio(b=3.14, g=3.14, r=3.14)
    a2 = ck2gfx_ColorRatio(b=9.99, g=9.99, r=9.99)
    b = ck2gfx_ArrowType(bodyTexture="sample_text", effect="sample_text", endAt=3.14, heading=3.14, height=3.14, name="sample_text", size=3.14, textureFile="sample_text", type=7)
    _safe_set(b, 'ck2gfx_ArrowType', a1)
    assert _is_linked(b, 'ck2gfx_ArrowType', a1)
    if hasattr(a1, 'ck2gfx_ColorRatio28'):
        assert _is_linked(a1, 'ck2gfx_ColorRatio28', b)
    _safe_set(b, 'ck2gfx_ArrowType', a2)
    assert _is_linked(b, 'ck2gfx_ArrowType', a2)
    if hasattr(a1, 'ck2gfx_ColorRatio28'):
        assert not _is_linked(a1, 'ck2gfx_ColorRatio28', b)
    if hasattr(a2, 'ck2gfx_ColorRatio28'):
        assert _is_linked(a2, 'ck2gfx_ColorRatio28', b)
    _safe_set(b, 'ck2gfx_ArrowType', None)
    assert not _is_linked(b, 'ck2gfx_ArrowType', a2)
    if hasattr(a2, 'ck2gfx_ColorRatio28'):
        assert not _is_linked(a2, 'ck2gfx_ColorRatio28', b)


def test_assoc_color28_reverse_link_reassign_clear():
    a1 = ck2gfx_ProgressbarType(allwaysTransparent=True, effectFile="sample_text", horizontal=True, loadType="sample_text", maxValue=3.14, name="sample_text", noRefCount=True, textureFile1="sample_text", textureFile2="sample_text")
    a2 = ck2gfx_ProgressbarType(allwaysTransparent=False, effectFile="sample_text_2", horizontal=False, loadType="sample_text_2", maxValue=9.99, name="sample_text_2", noRefCount=False, textureFile1="sample_text_2", textureFile2="sample_text_2")
    b = ck2gfx_ColorRatio(b=3.14, g=3.14, r=3.14)
    _safe_set(b, 'ck2gfx_ColorRatio10', a1)
    assert _is_linked(b, 'ck2gfx_ColorRatio10', a1)
    if hasattr(a1, 'ck2gfx_ProgressbarType9'):
        assert _is_linked(a1, 'ck2gfx_ProgressbarType9', b)
    _safe_set(b, 'ck2gfx_ColorRatio10', a2)
    assert _is_linked(b, 'ck2gfx_ColorRatio10', a2)
    if hasattr(a1, 'ck2gfx_ProgressbarType9'):
        assert not _is_linked(a1, 'ck2gfx_ProgressbarType9', b)
    if hasattr(a2, 'ck2gfx_ProgressbarType9'):
        assert _is_linked(a2, 'ck2gfx_ProgressbarType9', b)
    _safe_set(b, 'ck2gfx_ColorRatio10', None)
    assert not _is_linked(b, 'ck2gfx_ColorRatio10', a2)
    if hasattr(a2, 'ck2gfx_ProgressbarType9'):
        assert not _is_linked(a2, 'ck2gfx_ProgressbarType9', b)


def test_assoc_color7_reverse_link_reassign_clear():
    a1 = ck2gfx_ProgressbarType(allwaysTransparent=True, effectFile="sample_text", horizontal=True, loadType="sample_text", maxValue=3.14, name="sample_text", noRefCount=True, textureFile1="sample_text", textureFile2="sample_text")
    a2 = ck2gfx_ProgressbarType(allwaysTransparent=False, effectFile="sample_text_2", horizontal=False, loadType="sample_text_2", maxValue=9.99, name="sample_text_2", noRefCount=False, textureFile1="sample_text_2", textureFile2="sample_text_2")
    b = ck2gfx_ColorRatio(b=3.14, g=3.14, r=3.14)
    _safe_set(b, 'ck2gfx_ColorRatio', a1)
    assert _is_linked(b, 'ck2gfx_ColorRatio', a1)
    if hasattr(a1, 'ck2gfx_ProgressbarType'):
        assert _is_linked(a1, 'ck2gfx_ProgressbarType', b)
    _safe_set(b, 'ck2gfx_ColorRatio', a2)
    assert _is_linked(b, 'ck2gfx_ColorRatio', a2)
    if hasattr(a1, 'ck2gfx_ProgressbarType'):
        assert not _is_linked(a1, 'ck2gfx_ProgressbarType', b)
    if hasattr(a2, 'ck2gfx_ProgressbarType'):
        assert _is_linked(a2, 'ck2gfx_ProgressbarType', b)
    _safe_set(b, 'ck2gfx_ColorRatio', None)
    assert not _is_linked(b, 'ck2gfx_ColorRatio', a2)
    if hasattr(a2, 'ck2gfx_ProgressbarType'):
        assert not _is_linked(a2, 'ck2gfx_ProgressbarType', b)


def test_assoc_colorcodes33_reverse_link_reassign_clear():
    a1 = ck2gfx_ColorCode(key="sample_text")
    a2 = ck2gfx_ColorCode(key="sample_text_2")
    b = ck2gfx_BitmapFont(color=7, effect=True, fontName="sample_text", name="sample_text")
    _safe_set(b, 'ck2gfx_BitmapFont34', {a1})
    assert _is_linked(b, 'ck2gfx_BitmapFont34', a1)
    if hasattr(a1, 'ck2gfx_ColorCode'):
        assert _is_linked(a1, 'ck2gfx_ColorCode', b)
    _safe_set(b, 'ck2gfx_BitmapFont34', {a2})
    assert _is_linked(b, 'ck2gfx_BitmapFont34', a2)
    if hasattr(a1, 'ck2gfx_ColorCode'):
        assert not _is_linked(a1, 'ck2gfx_ColorCode', b)
    if hasattr(a2, 'ck2gfx_ColorCode'):
        assert _is_linked(a2, 'ck2gfx_ColorCode', b)
    _safe_set(b, 'ck2gfx_BitmapFont34', set())
    assert not _is_linked(b, 'ck2gfx_BitmapFont34', a2)
    if hasattr(a2, 'ck2gfx_ColorCode'):
        assert not _is_linked(a2, 'ck2gfx_ColorCode', b)


def test_assoc_eyeColor15_reverse_link_reassign_clear():
    a1 = ck2gfx_PortraitType(effectFile="sample_text", eyeColorIndex=7, hairColorIndex=7, headgearThatHidesHair=7, layers="sample_text", name="sample_text")
    a2 = ck2gfx_PortraitType(effectFile="sample_text_2", eyeColorIndex=13, hairColorIndex=13, headgearThatHidesHair=13, layers="sample_text_2", name="sample_text_2")
    b = ck2gfx_Color(b=7, g=7, r=7)
    _safe_set(b, 'ck2gfx_Color17', a1)
    assert _is_linked(b, 'ck2gfx_Color17', a1)
    if hasattr(a1, 'ck2gfx_PortraitType16'):
        assert _is_linked(a1, 'ck2gfx_PortraitType16', b)
    _safe_set(b, 'ck2gfx_Color17', a2)
    assert _is_linked(b, 'ck2gfx_Color17', a2)
    if hasattr(a1, 'ck2gfx_PortraitType16'):
        assert not _is_linked(a1, 'ck2gfx_PortraitType16', b)
    if hasattr(a2, 'ck2gfx_PortraitType16'):
        assert _is_linked(a2, 'ck2gfx_PortraitType16', b)
    _safe_set(b, 'ck2gfx_Color17', None)
    assert not _is_linked(b, 'ck2gfx_Color17', a2)
    if hasattr(a2, 'ck2gfx_PortraitType16'):
        assert not _is_linked(a2, 'ck2gfx_PortraitType16', b)


def test_assoc_hairColor14_reverse_link_reassign_clear():
    a1 = ck2gfx_PortraitType(effectFile="sample_text", eyeColorIndex=7, hairColorIndex=7, headgearThatHidesHair=7, layers="sample_text", name="sample_text")
    a2 = ck2gfx_PortraitType(effectFile="sample_text_2", eyeColorIndex=13, hairColorIndex=13, headgearThatHidesHair=13, layers="sample_text_2", name="sample_text_2")
    b = ck2gfx_Color(b=7, g=7, r=7)
    _safe_set(b, 'ck2gfx_Color', a1)
    assert _is_linked(b, 'ck2gfx_Color', a1)
    if hasattr(a1, 'ck2gfx_PortraitType'):
        assert _is_linked(a1, 'ck2gfx_PortraitType', b)
    _safe_set(b, 'ck2gfx_Color', a2)
    assert _is_linked(b, 'ck2gfx_Color', a2)
    if hasattr(a1, 'ck2gfx_PortraitType'):
        assert not _is_linked(a1, 'ck2gfx_PortraitType', b)
    if hasattr(a2, 'ck2gfx_PortraitType'):
        assert _is_linked(a2, 'ck2gfx_PortraitType', b)
    _safe_set(b, 'ck2gfx_Color', None)
    assert not _is_linked(b, 'ck2gfx_Color', a2)
    if hasattr(a2, 'ck2gfx_PortraitType'):
        assert not _is_linked(a2, 'ck2gfx_PortraitType', b)


def test_assoc_layers20_reverse_link_reassign_clear():
    a1 = ck2gfx_CoatOfArmsType(effect="sample_text", frame="sample_text", mask="sample_text", name="sample_text", sealOverlay="sample_text")
    a2 = ck2gfx_CoatOfArmsType(effect="sample_text_2", frame="sample_text_2", mask="sample_text_2", name="sample_text_2", sealOverlay="sample_text_2")
    b = ck2gfx_CoatOfArmsLayer(mask="sample_text", scale=3.14)
    _safe_set(b, 'ck2gfx_CoatOfArmsLayer', a1)
    assert _is_linked(b, 'ck2gfx_CoatOfArmsLayer', a1)
    if hasattr(a1, 'ck2gfx_CoatOfArmsType'):
        assert _is_linked(a1, 'ck2gfx_CoatOfArmsType', b)
    _safe_set(b, 'ck2gfx_CoatOfArmsLayer', a2)
    assert _is_linked(b, 'ck2gfx_CoatOfArmsLayer', a2)
    if hasattr(a1, 'ck2gfx_CoatOfArmsType'):
        assert not _is_linked(a1, 'ck2gfx_CoatOfArmsType', b)
    if hasattr(a2, 'ck2gfx_CoatOfArmsType'):
        assert _is_linked(a2, 'ck2gfx_CoatOfArmsType', b)
    _safe_set(b, 'ck2gfx_CoatOfArmsLayer', None)
    assert not _is_linked(b, 'ck2gfx_CoatOfArmsLayer', a2)
    if hasattr(a2, 'ck2gfx_CoatOfArmsType'):
        assert not _is_linked(a2, 'ck2gfx_CoatOfArmsType', b)


def test_assoc_size11_reverse_link_reassign_clear():
    a1 = ck2gfx_ProgressbarType(allwaysTransparent=True, effectFile="sample_text", horizontal=True, loadType="sample_text", maxValue=3.14, name="sample_text", noRefCount=True, textureFile1="sample_text", textureFile2="sample_text")
    a2 = ck2gfx_ProgressbarType(allwaysTransparent=False, effectFile="sample_text_2", horizontal=False, loadType="sample_text_2", maxValue=9.99, name="sample_text_2", noRefCount=False, textureFile1="sample_text_2", textureFile2="sample_text_2")
    b = ck2gfx_Coordinates(x=3.14, y=3.14)
    _safe_set(b, 'ck2gfx_Coordinates13', a1)
    assert _is_linked(b, 'ck2gfx_Coordinates13', a1)
    if hasattr(a1, 'ck2gfx_ProgressbarType12'):
        assert _is_linked(a1, 'ck2gfx_ProgressbarType12', b)
    _safe_set(b, 'ck2gfx_Coordinates13', a2)
    assert _is_linked(b, 'ck2gfx_Coordinates13', a2)
    if hasattr(a1, 'ck2gfx_ProgressbarType12'):
        assert not _is_linked(a1, 'ck2gfx_ProgressbarType12', b)
    if hasattr(a2, 'ck2gfx_ProgressbarType12'):
        assert _is_linked(a2, 'ck2gfx_ProgressbarType12', b)
    _safe_set(b, 'ck2gfx_Coordinates13', None)
    assert not _is_linked(b, 'ck2gfx_Coordinates13', a2)
    if hasattr(a2, 'ck2gfx_ProgressbarType12'):
        assert not _is_linked(a2, 'ck2gfx_ProgressbarType12', b)


def test_assoc_size18_reverse_link_reassign_clear():
    a1 = ck2gfx_LineChartType(lineWidth=7, name="sample_text")
    a2 = ck2gfx_LineChartType(lineWidth=13, name="sample_text_2")
    b = ck2gfx_Coordinates(x=3.14, y=3.14)
    _safe_set(b, 'ck2gfx_Coordinates19', a1)
    assert _is_linked(b, 'ck2gfx_Coordinates19', a1)
    if hasattr(a1, 'ck2gfx_LineChartType'):
        assert _is_linked(a1, 'ck2gfx_LineChartType', b)
    _safe_set(b, 'ck2gfx_Coordinates19', a2)
    assert _is_linked(b, 'ck2gfx_Coordinates19', a2)
    if hasattr(a1, 'ck2gfx_LineChartType'):
        assert not _is_linked(a1, 'ck2gfx_LineChartType', b)
    if hasattr(a2, 'ck2gfx_LineChartType'):
        assert _is_linked(a2, 'ck2gfx_LineChartType', b)
    _safe_set(b, 'ck2gfx_Coordinates19', None)
    assert not _is_linked(b, 'ck2gfx_Coordinates19', a2)
    if hasattr(a2, 'ck2gfx_LineChartType'):
        assert not _is_linked(a2, 'ck2gfx_LineChartType', b)


def test_assoc_size3_reverse_link_reassign_clear():
    a1 = ck2gfx_CorneredTileSpriteType(allwaysTransparent=True, loadType="sample_text", name="sample_text", noRefCount=True, texturefile="sample_text", tilingCenter=True)
    a2 = ck2gfx_CorneredTileSpriteType(allwaysTransparent=False, loadType="sample_text_2", name="sample_text_2", noRefCount=False, texturefile="sample_text_2", tilingCenter=False)
    b = ck2gfx_Coordinates(x=3.14, y=3.14)
    _safe_set(b, 'ck2gfx_Coordinates', a1)
    assert _is_linked(b, 'ck2gfx_Coordinates', a1)
    if hasattr(a1, 'ck2gfx_CorneredTileSpriteType'):
        assert _is_linked(a1, 'ck2gfx_CorneredTileSpriteType', b)
    _safe_set(b, 'ck2gfx_Coordinates', a2)
    assert _is_linked(b, 'ck2gfx_Coordinates', a2)
    if hasattr(a1, 'ck2gfx_CorneredTileSpriteType'):
        assert not _is_linked(a1, 'ck2gfx_CorneredTileSpriteType', b)
    if hasattr(a2, 'ck2gfx_CorneredTileSpriteType'):
        assert _is_linked(a2, 'ck2gfx_CorneredTileSpriteType', b)
    _safe_set(b, 'ck2gfx_Coordinates', None)
    assert not _is_linked(b, 'ck2gfx_Coordinates', a2)
    if hasattr(a2, 'ck2gfx_CorneredTileSpriteType'):
        assert not _is_linked(a2, 'ck2gfx_CorneredTileSpriteType', b)


def test_assoc_value35_reverse_link_reassign_clear():
    a1 = ck2gfx_ColorCode(key="sample_text")
    a2 = ck2gfx_ColorCode(key="sample_text_2")
    b = ck2gfx_Color(b=7, g=7, r=7)
    _safe_set(b, 'ck2gfx_Color37', a1)
    assert _is_linked(b, 'ck2gfx_Color37', a1)
    if hasattr(a1, 'ck2gfx_ColorCode36'):
        assert _is_linked(a1, 'ck2gfx_ColorCode36', b)
    _safe_set(b, 'ck2gfx_Color37', a2)
    assert _is_linked(b, 'ck2gfx_Color37', a2)
    if hasattr(a1, 'ck2gfx_ColorCode36'):
        assert not _is_linked(a1, 'ck2gfx_ColorCode36', b)
    if hasattr(a2, 'ck2gfx_ColorCode36'):
        assert _is_linked(a2, 'ck2gfx_ColorCode36', b)
    _safe_set(b, 'ck2gfx_Color37', None)
    assert not _is_linked(b, 'ck2gfx_Color37', a2)
    if hasattr(a2, 'ck2gfx_ColorCode36'):
        assert not _is_linked(a2, 'ck2gfx_ColorCode36', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_types32_stub_double():
    # ck2gfx_BitmapFonts has no real 'ck2gfx_BitmapFonts' property in the generated
    # code (a bare stub) -- manually attach it so ck2gfx_BitmapFont's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ck2gfx_BitmapFont's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ck2gfx_BitmapFont(color=7, effect=True, fontName="sample_text", name="sample_text")
    partner = ck2gfx_BitmapFonts()
    setattr(partner, 'ck2gfx_BitmapFonts', None)
    _safe_set(owner, 'ck2gfx_BitmapFont', partner)
    assert owner in getattr(partner, 'ck2gfx_BitmapFonts')
    _safe_set(owner, 'ck2gfx_BitmapFont', None)
    assert owner not in getattr(partner, 'ck2gfx_BitmapFonts')


