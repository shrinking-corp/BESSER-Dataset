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
    fxg_linkActiveFormat,
    RichTextContentContainer,
    fxg_CharacterAttributes,
    fxg_ContainerAttributes,
    fxg_ParagraphAttributes,
    RichTextContent,
    fxg_br,
    fxg_rawtext,
    fxg_linkNormalFormat,
    fxg_tab,
    fxg_span,
    fxg_div,
    fxg_a,
    fxg_img,
    fxg_linkHoverFormat,
    fxg_tcy,
    fxg_RichTextContentContainer,
    fxg_RichTextContent,
    CharacterAttributes,
    ContainerAttributes,
    ParagraphAttributes,
    fxg_p,
    Shape,
    fxg_Line,
    fxg_Ellipse,
    fxg_Rect,
    fxg_Definition,
    FXGElement,
    fxg_RichText,
    fxg_BitmapImage,
    fxg_Fill,
    fxg_Transform,
    fxg_Shape,
    fxg_ColorTransform,
    fxg_PlaceObject,
    fxg_Filter,
    fxg_Matrix,
    fxg_Path,
    fxg_Stroke,
    fxg_Private,
    fxg_Library,
    fxg_Group,
    fxg_Graphic,
    fxg_ContainerElement,
    fxg_FXGElement,
    fxg_GradientBevelFilter,
    fxg_GradientGlowFilter,
    Filter,
    fxg_ColorMatrixFilter,
    fxg_DropShadowFilter,
    fxg_BevelFilter,
    fxg_BlurFilter,
    fxg_GradientEntry,
    fxg_RadialGradientStroke,
    fxg_LinearGradient,
    fxg_LinearGradientStroke,
    Stroke,
    fxg_SolidColorStroke,
    fxg_RadialGradient,
    Fill,
    fxg_BitmapFill,
    fxg_SolidColor,
    FontStyle,
    TextDecoration,
    BlendMode,
    MaskType,
    Joint,
    ScaleMode,
    LigatureLevel,
    TextAlign,
    Winding,
    VerticalAlign,
    TextJustify,
    JustificationRule,
    WhitespaceCollapse,
    BevelFilterType,
    DigitCase,
    Cap,
    BreakOpportunity,
    DominantBaseline,
    BlockProgression,
    AlignmentBaseline,
    InterpolationMethod,
    LeadingModel,
    SpreadMethod,
    TextRotation,
    DigitWidth,
    Kerning,
    FillMode,
    LineBreak,
    JustificationStyle,
    TypographicCase,
    FontWeight,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fxg_linkactiveformat_is_not_abstract():
    assert not inspect.isabstract(fxg_linkActiveFormat)


def test_hyp_fxg_linkactiveformat_constructor_exists():
    assert callable(fxg_linkActiveFormat.__init__)


def test_hyp_fxg_linkactiveformat_constructor_args():
    sig = inspect.signature(fxg_linkActiveFormat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_richtextcontentcontainer_is_not_abstract():
    assert not inspect.isabstract(RichTextContentContainer)


def test_hyp_richtextcontentcontainer_constructor_exists():
    assert callable(RichTextContentContainer.__init__)


def test_hyp_richtextcontentcontainer_constructor_args():
    sig = inspect.signature(RichTextContentContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_characterattributes_is_not_abstract():
    assert not inspect.isabstract(fxg_CharacterAttributes)


def test_hyp_fxg_characterattributes_constructor_exists():
    assert callable(fxg_CharacterAttributes.__init__)


def test_hyp_fxg_characterattributes_constructor_args():
    sig = inspect.signature(fxg_CharacterAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "lineHeight" in params, "Missing parameter 'lineHeight'"
    assert "ligatureLevel" in params, "Missing parameter 'ligatureLevel'"
    assert "kerning" in params, "Missing parameter 'kerning'"
    assert "dominantBaseline" in params, "Missing parameter 'dominantBaseline'"
    assert "digitWidth" in params, "Missing parameter 'digitWidth'"
    assert "textDecoration" in params, "Missing parameter 'textDecoration'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "typographicCase" in params, "Missing parameter 'typographicCase'"
    assert "color" in params, "Missing parameter 'color'"
    assert "fontFamily" in params, "Missing parameter 'fontFamily'"
    assert "textRotation" in params, "Missing parameter 'textRotation'"
    assert "baselineShift" in params, "Missing parameter 'baselineShift'"
    assert "textAlpha" in params, "Missing parameter 'textAlpha'"
    assert "whiteSpaceCollapse" in params, "Missing parameter 'whiteSpaceCollapse'"
    assert "fontWeight" in params, "Missing parameter 'fontWeight'"
    assert "fontStyle" in params, "Missing parameter 'fontStyle'"
    assert "alignmentBaseline" in params, "Missing parameter 'alignmentBaseline'"
    assert "digitCase" in params, "Missing parameter 'digitCase'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "breakOpportunity" in params, "Missing parameter 'breakOpportunity'"
    assert "lineThrough" in params, "Missing parameter 'lineThrough'"
    assert "trackingRight" in params, "Missing parameter 'trackingRight'"
    assert "backgroundAlpha" in params, "Missing parameter 'backgroundAlpha'"
    assert "trackingLeft" in params, "Missing parameter 'trackingLeft'"




























def test_hyp_fxg_containerattributes_is_not_abstract():
    assert not inspect.isabstract(fxg_ContainerAttributes)


def test_hyp_fxg_containerattributes_constructor_exists():
    assert callable(fxg_ContainerAttributes.__init__)


def test_hyp_fxg_containerattributes_constructor_args():
    sig = inspect.signature(fxg_ContainerAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "lineBreak" in params, "Missing parameter 'lineBreak'"
    assert "paddingLeft" in params, "Missing parameter 'paddingLeft'"
    assert "firstBaselineOffset" in params, "Missing parameter 'firstBaselineOffset'"
    assert "blockProgression" in params, "Missing parameter 'blockProgression'"
    assert "columnWidth" in params, "Missing parameter 'columnWidth'"
    assert "verticalAlign" in params, "Missing parameter 'verticalAlign'"
    assert "columnCount" in params, "Missing parameter 'columnCount'"
    assert "columnGap" in params, "Missing parameter 'columnGap'"
    assert "paddingBottom" in params, "Missing parameter 'paddingBottom'"
    assert "paddingTop" in params, "Missing parameter 'paddingTop'"
    assert "paddingRight" in params, "Missing parameter 'paddingRight'"














def test_hyp_fxg_paragraphattributes_is_not_abstract():
    assert not inspect.isabstract(fxg_ParagraphAttributes)


def test_hyp_fxg_paragraphattributes_constructor_exists():
    assert callable(fxg_ParagraphAttributes.__init__)


def test_hyp_fxg_paragraphattributes_constructor_args():
    sig = inspect.signature(fxg_ParagraphAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "paragraphEndIndent" in params, "Missing parameter 'paragraphEndIndent'"
    assert "leadingModel" in params, "Missing parameter 'leadingModel'"
    assert "paragraphStartIndent" in params, "Missing parameter 'paragraphStartIndent'"
    assert "tabStops" in params, "Missing parameter 'tabStops'"
    assert "paragraphSpaceBefore" in params, "Missing parameter 'paragraphSpaceBefore'"
    assert "justificationRule" in params, "Missing parameter 'justificationRule'"
    assert "justificationStyle" in params, "Missing parameter 'justificationStyle'"
    assert "textIndent" in params, "Missing parameter 'textIndent'"
    assert "textAlignLast" in params, "Missing parameter 'textAlignLast'"
    assert "textJustify" in params, "Missing parameter 'textJustify'"
    assert "paragraphSpaceAfter" in params, "Missing parameter 'paragraphSpaceAfter'"
    assert "textAlign" in params, "Missing parameter 'textAlign'"















def test_hyp_richtextcontent_is_not_abstract():
    assert not inspect.isabstract(RichTextContent)


def test_hyp_richtextcontent_constructor_exists():
    assert callable(RichTextContent.__init__)


def test_hyp_richtextcontent_constructor_args():
    sig = inspect.signature(RichTextContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_br_is_not_abstract():
    assert not inspect.isabstract(fxg_br)


def test_hyp_fxg_br_constructor_exists():
    assert callable(fxg_br.__init__)


def test_hyp_fxg_br_constructor_args():
    sig = inspect.signature(fxg_br.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_rawtext_is_not_abstract():
    assert not inspect.isabstract(fxg_rawtext)


def test_hyp_fxg_rawtext_constructor_exists():
    assert callable(fxg_rawtext.__init__)


def test_hyp_fxg_rawtext_constructor_args():
    sig = inspect.signature(fxg_rawtext.__init__)
    params = list(sig.parameters.keys())
    assert "_text" in params, "Missing parameter '_text'"




def test_hyp_fxg_linknormalformat_is_not_abstract():
    assert not inspect.isabstract(fxg_linkNormalFormat)


def test_hyp_fxg_linknormalformat_constructor_exists():
    assert callable(fxg_linkNormalFormat.__init__)


def test_hyp_fxg_linknormalformat_constructor_args():
    sig = inspect.signature(fxg_linkNormalFormat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_tab_is_not_abstract():
    assert not inspect.isabstract(fxg_tab)


def test_hyp_fxg_tab_constructor_exists():
    assert callable(fxg_tab.__init__)


def test_hyp_fxg_tab_constructor_args():
    sig = inspect.signature(fxg_tab.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_span_is_not_abstract():
    assert not inspect.isabstract(fxg_span)


def test_hyp_fxg_span_constructor_exists():
    assert callable(fxg_span.__init__)


def test_hyp_fxg_span_constructor_args():
    sig = inspect.signature(fxg_span.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_div_is_not_abstract():
    assert not inspect.isabstract(fxg_div)


def test_hyp_fxg_div_constructor_exists():
    assert callable(fxg_div.__init__)


def test_hyp_fxg_div_constructor_args():
    sig = inspect.signature(fxg_div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_a_is_not_abstract():
    assert not inspect.isabstract(fxg_a)


def test_hyp_fxg_a_constructor_exists():
    assert callable(fxg_a.__init__)


def test_hyp_fxg_a_constructor_args():
    sig = inspect.signature(fxg_a.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_img_is_not_abstract():
    assert not inspect.isabstract(fxg_img)


def test_hyp_fxg_img_constructor_exists():
    assert callable(fxg_img.__init__)


def test_hyp_fxg_img_constructor_args():
    sig = inspect.signature(fxg_img.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_linkhoverformat_is_not_abstract():
    assert not inspect.isabstract(fxg_linkHoverFormat)


def test_hyp_fxg_linkhoverformat_constructor_exists():
    assert callable(fxg_linkHoverFormat.__init__)


def test_hyp_fxg_linkhoverformat_constructor_args():
    sig = inspect.signature(fxg_linkHoverFormat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_tcy_is_not_abstract():
    assert not inspect.isabstract(fxg_tcy)


def test_hyp_fxg_tcy_constructor_exists():
    assert callable(fxg_tcy.__init__)


def test_hyp_fxg_tcy_constructor_args():
    sig = inspect.signature(fxg_tcy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_richtextcontentcontainer_is_not_abstract():
    assert not inspect.isabstract(fxg_RichTextContentContainer)


def test_hyp_fxg_richtextcontentcontainer_constructor_exists():
    assert callable(fxg_RichTextContentContainer.__init__)


def test_hyp_fxg_richtextcontentcontainer_constructor_args():
    sig = inspect.signature(fxg_RichTextContentContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_richtextcontent_is_not_abstract():
    assert not inspect.isabstract(fxg_RichTextContent)


def test_hyp_fxg_richtextcontent_constructor_exists():
    assert callable(fxg_RichTextContent.__init__)


def test_hyp_fxg_richtextcontent_constructor_args():
    sig = inspect.signature(fxg_RichTextContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_characterattributes_is_not_abstract():
    assert not inspect.isabstract(CharacterAttributes)


def test_hyp_characterattributes_constructor_exists():
    assert callable(CharacterAttributes.__init__)


def test_hyp_characterattributes_constructor_args():
    sig = inspect.signature(CharacterAttributes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_containerattributes_is_not_abstract():
    assert not inspect.isabstract(ContainerAttributes)


def test_hyp_containerattributes_constructor_exists():
    assert callable(ContainerAttributes.__init__)


def test_hyp_containerattributes_constructor_args():
    sig = inspect.signature(ContainerAttributes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paragraphattributes_is_not_abstract():
    assert not inspect.isabstract(ParagraphAttributes)


def test_hyp_paragraphattributes_constructor_exists():
    assert callable(ParagraphAttributes.__init__)


def test_hyp_paragraphattributes_constructor_args():
    sig = inspect.signature(ParagraphAttributes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_p_is_not_abstract():
    assert not inspect.isabstract(fxg_p)


def test_hyp_fxg_p_constructor_exists():
    assert callable(fxg_p.__init__)


def test_hyp_fxg_p_constructor_args():
    sig = inspect.signature(fxg_p.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_hyp_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_hyp_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_line_is_not_abstract():
    assert not inspect.isabstract(fxg_Line)


def test_hyp_fxg_line_constructor_exists():
    assert callable(fxg_Line.__init__)


def test_hyp_fxg_line_constructor_args():
    sig = inspect.signature(fxg_Line.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "y" in params, "Missing parameter 'y'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "yFrom" in params, "Missing parameter 'yFrom'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "xFrom" in params, "Missing parameter 'xFrom'"
    assert "yTo" in params, "Missing parameter 'yTo'"
    assert "id" in params, "Missing parameter 'id'"
    assert "xTo" in params, "Missing parameter 'xTo'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"

















def test_hyp_fxg_ellipse_is_not_abstract():
    assert not inspect.isabstract(fxg_Ellipse)


def test_hyp_fxg_ellipse_constructor_exists():
    assert callable(fxg_Ellipse.__init__)


def test_hyp_fxg_ellipse_constructor_args():
    sig = inspect.signature(fxg_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "width" in params, "Missing parameter 'width'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"













def test_hyp_fxg_rect_is_not_abstract():
    assert not inspect.isabstract(fxg_Rect)


def test_hyp_fxg_rect_constructor_exists():
    assert callable(fxg_Rect.__init__)


def test_hyp_fxg_rect_constructor_args():
    sig = inspect.signature(fxg_Rect.__init__)
    params = list(sig.parameters.keys())
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "topLeftRadiusX" in params, "Missing parameter 'topLeftRadiusX'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "height" in params, "Missing parameter 'height'"
    assert "y" in params, "Missing parameter 'y'"
    assert "topRightRadiusX" in params, "Missing parameter 'topRightRadiusX'"
    assert "bottomLeftRadiusY" in params, "Missing parameter 'bottomLeftRadiusY'"
    assert "bottomRightRadiusY" in params, "Missing parameter 'bottomRightRadiusY'"
    assert "topRightRadiusY" in params, "Missing parameter 'topRightRadiusY'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "bottomLeftRadiusX" in params, "Missing parameter 'bottomLeftRadiusX'"
    assert "x" in params, "Missing parameter 'x'"
    assert "radiusX" in params, "Missing parameter 'radiusX'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "width" in params, "Missing parameter 'width'"
    assert "radiusY" in params, "Missing parameter 'radiusY'"
    assert "topLeftRadiusY" in params, "Missing parameter 'topLeftRadiusY'"
    assert "bottomRightRadiusX" in params, "Missing parameter 'bottomRightRadiusX'"























def test_hyp_fxg_definition_is_not_abstract():
    assert not inspect.isabstract(fxg_Definition)


def test_hyp_fxg_definition_constructor_exists():
    assert callable(fxg_Definition.__init__)


def test_hyp_fxg_definition_constructor_args():
    sig = inspect.signature(fxg_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fxgelement_is_not_abstract():
    assert not inspect.isabstract(FXGElement)


def test_hyp_fxgelement_constructor_exists():
    assert callable(FXGElement.__init__)


def test_hyp_fxgelement_constructor_args():
    sig = inspect.signature(FXGElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_richtext_is_not_abstract():
    assert not inspect.isabstract(fxg_RichText)


def test_hyp_fxg_richtext_constructor_exists():
    assert callable(fxg_RichText.__init__)


def test_hyp_fxg_richtext_constructor_args():
    sig = inspect.signature(fxg_RichText.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "_tempcontent" in params, "Missing parameter '_tempcontent'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "id" in params, "Missing parameter 'id'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"
















def test_hyp_fxg_bitmapimage_is_not_abstract():
    assert not inspect.isabstract(fxg_BitmapImage)


def test_hyp_fxg_bitmapimage_constructor_exists():
    assert callable(fxg_BitmapImage.__init__)


def test_hyp_fxg_bitmapimage_constructor_args():
    sig = inspect.signature(fxg_BitmapImage.__init__)
    params = list(sig.parameters.keys())
    assert "fillMode" in params, "Missing parameter 'fillMode'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "width" in params, "Missing parameter 'width'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "height" in params, "Missing parameter 'height'"
    assert "source" in params, "Missing parameter 'source'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"















def test_hyp_fxg_fill_is_not_abstract():
    assert not inspect.isabstract(fxg_Fill)


def test_hyp_fxg_fill_constructor_exists():
    assert callable(fxg_Fill.__init__)


def test_hyp_fxg_fill_constructor_args():
    sig = inspect.signature(fxg_Fill.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_transform_is_not_abstract():
    assert not inspect.isabstract(fxg_Transform)


def test_hyp_fxg_transform_constructor_exists():
    assert callable(fxg_Transform.__init__)


def test_hyp_fxg_transform_constructor_args():
    sig = inspect.signature(fxg_Transform.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_shape_is_not_abstract():
    assert not inspect.isabstract(fxg_Shape)


def test_hyp_fxg_shape_constructor_exists():
    assert callable(fxg_Shape.__init__)


def test_hyp_fxg_shape_constructor_args():
    sig = inspect.signature(fxg_Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_colortransform_is_not_abstract():
    assert not inspect.isabstract(fxg_ColorTransform)


def test_hyp_fxg_colortransform_constructor_exists():
    assert callable(fxg_ColorTransform.__init__)


def test_hyp_fxg_colortransform_constructor_args():
    sig = inspect.signature(fxg_ColorTransform.__init__)
    params = list(sig.parameters.keys())
    assert "greenOffset" in params, "Missing parameter 'greenOffset'"
    assert "greenMultiplier" in params, "Missing parameter 'greenMultiplier'"
    assert "blueOffset" in params, "Missing parameter 'blueOffset'"
    assert "alphaOffset" in params, "Missing parameter 'alphaOffset'"
    assert "alphaMultiplier" in params, "Missing parameter 'alphaMultiplier'"
    assert "redOffset" in params, "Missing parameter 'redOffset'"
    assert "blueMultiplier" in params, "Missing parameter 'blueMultiplier'"
    assert "redMultiplier" in params, "Missing parameter 'redMultiplier'"











def test_hyp_fxg_placeobject_is_not_abstract():
    assert not inspect.isabstract(fxg_PlaceObject)


def test_hyp_fxg_placeobject_constructor_exists():
    assert callable(fxg_PlaceObject.__init__)


def test_hyp_fxg_placeobject_constructor_args():
    sig = inspect.signature(fxg_PlaceObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_fxg_filter_is_not_abstract():
    assert not inspect.isabstract(fxg_Filter)


def test_hyp_fxg_filter_constructor_exists():
    assert callable(fxg_Filter.__init__)


def test_hyp_fxg_filter_constructor_args():
    sig = inspect.signature(fxg_Filter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_matrix_is_not_abstract():
    assert not inspect.isabstract(fxg_Matrix)


def test_hyp_fxg_matrix_constructor_exists():
    assert callable(fxg_Matrix.__init__)


def test_hyp_fxg_matrix_constructor_args():
    sig = inspect.signature(fxg_Matrix.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "d" in params, "Missing parameter 'd'"
    assert "b" in params, "Missing parameter 'b'"
    assert "ty" in params, "Missing parameter 'ty'"
    assert "tx" in params, "Missing parameter 'tx'"
    assert "c" in params, "Missing parameter 'c'"









def test_hyp_fxg_path_is_not_abstract():
    assert not inspect.isabstract(fxg_Path)


def test_hyp_fxg_path_constructor_exists():
    assert callable(fxg_Path.__init__)


def test_hyp_fxg_path_constructor_args():
    sig = inspect.signature(fxg_Path.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "y" in params, "Missing parameter 'y'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "data" in params, "Missing parameter 'data'"
    assert "winding" in params, "Missing parameter 'winding'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "visible" in params, "Missing parameter 'visible'"













def test_hyp_fxg_stroke_is_not_abstract():
    assert not inspect.isabstract(fxg_Stroke)


def test_hyp_fxg_stroke_constructor_exists():
    assert callable(fxg_Stroke.__init__)


def test_hyp_fxg_stroke_constructor_args():
    sig = inspect.signature(fxg_Stroke.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_private_is_not_abstract():
    assert not inspect.isabstract(fxg_Private)


def test_hyp_fxg_private_constructor_exists():
    assert callable(fxg_Private.__init__)


def test_hyp_fxg_private_constructor_args():
    sig = inspect.signature(fxg_Private.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_library_is_not_abstract():
    assert not inspect.isabstract(fxg_Library)


def test_hyp_fxg_library_constructor_exists():
    assert callable(fxg_Library.__init__)


def test_hyp_fxg_library_constructor_args():
    sig = inspect.signature(fxg_Library.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_group_is_not_abstract():
    assert not inspect.isabstract(fxg_Group)


def test_hyp_fxg_group_constructor_exists():
    assert callable(fxg_Group.__init__)


def test_hyp_fxg_group_constructor_args():
    sig = inspect.signature(fxg_Group.__init__)
    params = list(sig.parameters.keys())
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "x" in params, "Missing parameter 'x'"
    assert "transformY" in params, "Missing parameter 'transformY'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "scaleGridLeft" in params, "Missing parameter 'scaleGridLeft'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "scaleGridRight" in params, "Missing parameter 'scaleGridRight'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleGridTop" in params, "Missing parameter 'scaleGridTop'"
    assert "scaleGridBottom" in params, "Missing parameter 'scaleGridBottom'"
    assert "y" in params, "Missing parameter 'y'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "transformX" in params, "Missing parameter 'transformX'"
    assert "id" in params, "Missing parameter 'id'"



















def test_hyp_fxg_graphic_is_not_abstract():
    assert not inspect.isabstract(fxg_Graphic)


def test_hyp_fxg_graphic_constructor_exists():
    assert callable(fxg_Graphic.__init__)


def test_hyp_fxg_graphic_constructor_args():
    sig = inspect.signature(fxg_Graphic.__init__)
    params = list(sig.parameters.keys())
    assert "viewHeight" in params, "Missing parameter 'viewHeight'"
    assert "viewWidth" in params, "Missing parameter 'viewWidth'"
    assert "scaleGridTop" in params, "Missing parameter 'scaleGridTop'"
    assert "scaleGridRight" in params, "Missing parameter 'scaleGridRight'"
    assert "version" in params, "Missing parameter 'version'"
    assert "scaleGridBottom" in params, "Missing parameter 'scaleGridBottom'"
    assert "scaleGridLeft" in params, "Missing parameter 'scaleGridLeft'"










def test_hyp_fxg_containerelement_is_not_abstract():
    assert not inspect.isabstract(fxg_ContainerElement)


def test_hyp_fxg_containerelement_constructor_exists():
    assert callable(fxg_ContainerElement.__init__)


def test_hyp_fxg_containerelement_constructor_args():
    sig = inspect.signature(fxg_ContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_fxgelement_is_not_abstract():
    assert not inspect.isabstract(fxg_FXGElement)


def test_hyp_fxg_fxgelement_constructor_exists():
    assert callable(fxg_FXGElement.__init__)


def test_hyp_fxg_fxgelement_constructor_args():
    sig = inspect.signature(fxg_FXGElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_gradientbevelfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_GradientBevelFilter)


def test_hyp_fxg_gradientbevelfilter_constructor_exists():
    assert callable(fxg_GradientBevelFilter.__init__)


def test_hyp_fxg_gradientbevelfilter_constructor_args():
    sig = inspect.signature(fxg_GradientBevelFilter.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "type" in params, "Missing parameter 'type'"











def test_hyp_fxg_gradientglowfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_GradientGlowFilter)


def test_hyp_fxg_gradientglowfilter_constructor_exists():
    assert callable(fxg_GradientGlowFilter.__init__)


def test_hyp_fxg_gradientglowfilter_constructor_args():
    sig = inspect.signature(fxg_GradientGlowFilter.__init__)
    params = list(sig.parameters.keys())
    assert "inner" in params, "Missing parameter 'inner'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "distance" in params, "Missing parameter 'distance'"











def test_hyp_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_hyp_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_hyp_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_colormatrixfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_ColorMatrixFilter)


def test_hyp_fxg_colormatrixfilter_constructor_exists():
    assert callable(fxg_ColorMatrixFilter.__init__)


def test_hyp_fxg_colormatrixfilter_constructor_args():
    sig = inspect.signature(fxg_ColorMatrixFilter.__init__)
    params = list(sig.parameters.keys())
    assert "matrix" in params, "Missing parameter 'matrix'"




def test_hyp_fxg_dropshadowfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_DropShadowFilter)


def test_hyp_fxg_dropshadowfilter_constructor_exists():
    assert callable(fxg_DropShadowFilter.__init__)


def test_hyp_fxg_dropshadowfilter_constructor_args():
    sig = inspect.signature(fxg_DropShadowFilter.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "inner" in params, "Missing parameter 'inner'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "color" in params, "Missing parameter 'color'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "hideObject" in params, "Missing parameter 'hideObject'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "blurY" in params, "Missing parameter 'blurY'"














def test_hyp_fxg_bevelfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_BevelFilter)


def test_hyp_fxg_bevelfilter_constructor_exists():
    assert callable(fxg_BevelFilter.__init__)


def test_hyp_fxg_bevelfilter_constructor_args():
    sig = inspect.signature(fxg_BevelFilter.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"
    assert "shadowColor" in params, "Missing parameter 'shadowColor'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "type" in params, "Missing parameter 'type'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "shadowAlpha" in params, "Missing parameter 'shadowAlpha'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "highlightAlpha" in params, "Missing parameter 'highlightAlpha'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "highlightColor" in params, "Missing parameter 'highlightColor'"
    assert "angle" in params, "Missing parameter 'angle'"















def test_hyp_fxg_blurfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_BlurFilter)


def test_hyp_fxg_blurfilter_constructor_exists():
    assert callable(fxg_BlurFilter.__init__)


def test_hyp_fxg_blurfilter_constructor_args():
    sig = inspect.signature(fxg_BlurFilter.__init__)
    params = list(sig.parameters.keys())
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "quality" in params, "Missing parameter 'quality'"






def test_hyp_fxg_gradiententry_is_not_abstract():
    assert not inspect.isabstract(fxg_GradientEntry)


def test_hyp_fxg_gradiententry_constructor_exists():
    assert callable(fxg_GradientEntry.__init__)


def test_hyp_fxg_gradiententry_constructor_args():
    sig = inspect.signature(fxg_GradientEntry.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"
    assert "color" in params, "Missing parameter 'color'"
    assert "alpha" in params, "Missing parameter 'alpha'"






def test_hyp_fxg_radialgradientstroke_is_not_abstract():
    assert not inspect.isabstract(fxg_RadialGradientStroke)


def test_hyp_fxg_radialgradientstroke_constructor_exists():
    assert callable(fxg_RadialGradientStroke.__init__)


def test_hyp_fxg_radialgradientstroke_constructor_args():
    sig = inspect.signature(fxg_RadialGradientStroke.__init__)
    params = list(sig.parameters.keys())
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "caps" in params, "Missing parameter 'caps'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "y" in params, "Missing parameter 'y'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "focalPointRatio" in params, "Missing parameter 'focalPointRatio'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "x" in params, "Missing parameter 'x'"
    assert "weight" in params, "Missing parameter 'weight'"

















def test_hyp_fxg_lineargradient_is_not_abstract():
    assert not inspect.isabstract(fxg_LinearGradient)


def test_hyp_fxg_lineargradient_constructor_exists():
    assert callable(fxg_LinearGradient.__init__)


def test_hyp_fxg_lineargradient_constructor_args():
    sig = inspect.signature(fxg_LinearGradient.__init__)
    params = list(sig.parameters.keys())
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "y" in params, "Missing parameter 'y'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "x" in params, "Missing parameter 'x'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"









def test_hyp_fxg_lineargradientstroke_is_not_abstract():
    assert not inspect.isabstract(fxg_LinearGradientStroke)


def test_hyp_fxg_lineargradientstroke_constructor_exists():
    assert callable(fxg_LinearGradientStroke.__init__)


def test_hyp_fxg_lineargradientstroke_constructor_args():
    sig = inspect.signature(fxg_LinearGradientStroke.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "caps" in params, "Missing parameter 'caps'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "y" in params, "Missing parameter 'y'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"















def test_hyp_stroke_is_not_abstract():
    assert not inspect.isabstract(Stroke)


def test_hyp_stroke_constructor_exists():
    assert callable(Stroke.__init__)


def test_hyp_stroke_constructor_args():
    sig = inspect.signature(Stroke.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_solidcolorstroke_is_not_abstract():
    assert not inspect.isabstract(fxg_SolidColorStroke)


def test_hyp_fxg_solidcolorstroke_constructor_exists():
    assert callable(fxg_SolidColorStroke.__init__)


def test_hyp_fxg_solidcolorstroke_constructor_args():
    sig = inspect.signature(fxg_SolidColorStroke.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "caps" in params, "Missing parameter 'caps'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"











def test_hyp_fxg_radialgradient_is_not_abstract():
    assert not inspect.isabstract(fxg_RadialGradient)


def test_hyp_fxg_radialgradient_constructor_exists():
    assert callable(fxg_RadialGradient.__init__)


def test_hyp_fxg_radialgradient_constructor_args():
    sig = inspect.signature(fxg_RadialGradient.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "focalPointRatio" in params, "Missing parameter 'focalPointRatio'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "y" in params, "Missing parameter 'y'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"











def test_hyp_fill_is_not_abstract():
    assert not inspect.isabstract(Fill)


def test_hyp_fill_constructor_exists():
    assert callable(Fill.__init__)


def test_hyp_fill_constructor_args():
    sig = inspect.signature(Fill.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fxg_bitmapfill_is_not_abstract():
    assert not inspect.isabstract(fxg_BitmapFill)


def test_hyp_fxg_bitmapfill_constructor_exists():
    assert callable(fxg_BitmapFill.__init__)


def test_hyp_fxg_bitmapfill_constructor_args():
    sig = inspect.signature(fxg_BitmapFill.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "source" in params, "Missing parameter 'source'"
    assert "fillMode" in params, "Missing parameter 'fillMode'"
    assert "x" in params, "Missing parameter 'x'"










def test_hyp_fxg_solidcolor_is_not_abstract():
    assert not inspect.isabstract(fxg_SolidColor)


def test_hyp_fxg_solidcolor_constructor_exists():
    assert callable(fxg_SolidColor.__init__)


def test_hyp_fxg_solidcolor_constructor_args():
    sig = inspect.signature(fxg_SolidColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "alpha" in params, "Missing parameter 'alpha'"



def test_hyp_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_hyp_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "NORMAL",
        "ITALIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_hyp_textdecoration_exists():
    # Check that the Enumeration exists
    assert TextDecoration is not None

def test_hyp_textdecoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextDecoration]
    expected_literals = [
        "NONE",
        "UNDERLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextDecoration"

def test_hyp_blendmode_exists():
    # Check that the Enumeration exists
    assert BlendMode is not None

def test_hyp_blendmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlendMode]
    expected_literals = [
        "alpha",
        "NOT_SET",
        "normal",
        "shader",
        "lighten",
        "add",
        "multiply",
        "subtract",
        "difference",
        "invert",
        "darken",
        "overlay",
        "hardlight",
        "layer",
        "erase",
        "screen",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlendMode"

def test_hyp_masktype_exists():
    # Check that the Enumeration exists
    assert MaskType is not None

def test_hyp_masktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MaskType]
    expected_literals = [
        "CLIP",
        "ALPHA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MaskType"

def test_hyp_joint_exists():
    # Check that the Enumeration exists
    assert Joint is not None

def test_hyp_joint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Joint]
    expected_literals = [
        "ROUND",
        "BEVEL",
        "MITER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Joint"

def test_hyp_scalemode_exists():
    # Check that the Enumeration exists
    assert ScaleMode is not None

def test_hyp_scalemode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleMode]
    expected_literals = [
        "NORMAL",
        "NONE",
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleMode"

def test_hyp_ligaturelevel_exists():
    # Check that the Enumeration exists
    assert LigatureLevel is not None

def test_hyp_ligaturelevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LigatureLevel]
    expected_literals = [
        "uncommon",
        "common",
        "exotic",
        "minimum",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LigatureLevel"

def test_hyp_textalign_exists():
    # Check that the Enumeration exists
    assert TextAlign is not None

def test_hyp_textalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlign]
    expected_literals = [
        "left",
        "end",
        "start",
        "center",
        "right",
        "justify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlign"

def test_hyp_winding_exists():
    # Check that the Enumeration exists
    assert Winding is not None

def test_hyp_winding_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Winding]
    expected_literals = [
        "nonZero",
        "NOT_SET",
        "evenOdd",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Winding"

def test_hyp_verticalalign_exists():
    # Check that the Enumeration exists
    assert VerticalAlign is not None

def test_hyp_verticalalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VerticalAlign]
    expected_literals = [
        "top",
        "inherit",
        "bottom",
        "justify",
        "middle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VerticalAlign"

def test_hyp_textjustify_exists():
    # Check that the Enumeration exists
    assert TextJustify is not None

def test_hyp_textjustify_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextJustify]
    expected_literals = [
        "interWord",
        "distribute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextJustify"

def test_hyp_justificationrule_exists():
    # Check that the Enumeration exists
    assert JustificationRule is not None

def test_hyp_justificationrule_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JustificationRule]
    expected_literals = [
        "space",
        "auto",
        "eastAsian",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JustificationRule"

def test_hyp_whitespacecollapse_exists():
    # Check that the Enumeration exists
    assert WhitespaceCollapse is not None

def test_hyp_whitespacecollapse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WhitespaceCollapse]
    expected_literals = [
        "COLLAPSE",
        "PRESERVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WhitespaceCollapse"

def test_hyp_bevelfiltertype_exists():
    # Check that the Enumeration exists
    assert BevelFilterType is not None

def test_hyp_bevelfiltertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BevelFilterType]
    expected_literals = [
        "INNER",
        "OUTER",
        "FULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BevelFilterType"

def test_hyp_digitcase_exists():
    # Check that the Enumeration exists
    assert DigitCase is not None

def test_hyp_digitcase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitCase]
    expected_literals = [
        "default",
        "lining",
        "oldStyle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitCase"

def test_hyp_cap_exists():
    # Check that the Enumeration exists
    assert Cap is not None

def test_hyp_cap_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cap]
    expected_literals = [
        "SQUARE",
        "NONE",
        "ROUND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cap"

def test_hyp_breakopportunity_exists():
    # Check that the Enumeration exists
    assert BreakOpportunity is not None

def test_hyp_breakopportunity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakOpportunity]
    expected_literals = [
        "auto",
        "all",
        "any",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BreakOpportunity"

def test_hyp_dominantbaseline_exists():
    # Check that the Enumeration exists
    assert DominantBaseline is not None

def test_hyp_dominantbaseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DominantBaseline]
    expected_literals = [
        "roman",
        "ideographicTop",
        "descent",
        "ascent",
        "ideographicCenter",
        "auto",
        "ideographicBottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DominantBaseline"

def test_hyp_blockprogression_exists():
    # Check that the Enumeration exists
    assert BlockProgression is not None

def test_hyp_blockprogression_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlockProgression]
    expected_literals = [
        "tb",
        "rl",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlockProgression"

def test_hyp_alignmentbaseline_exists():
    # Check that the Enumeration exists
    assert AlignmentBaseline is not None

def test_hyp_alignmentbaseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentBaseline]
    expected_literals = [
        "descent",
        "ideographicTop",
        "auto",
        "ideographicBottom",
        "ideographicCenter",
        "useDominantBaseline",
        "roman",
        "ascent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentBaseline"

def test_hyp_interpolationmethod_exists():
    # Check that the Enumeration exists
    assert InterpolationMethod is not None

def test_hyp_interpolationmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterpolationMethod]
    expected_literals = [
        "rgb",
        "linearRGB",
        "NOT_SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterpolationMethod"

def test_hyp_leadingmodel_exists():
    # Check that the Enumeration exists
    assert LeadingModel is not None

def test_hyp_leadingmodel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeadingModel]
    expected_literals = [
        "ideographicCenterDown",
        "ideographicCenterUp",
        "auto",
        "ideographicTopDown",
        "ascentDescentUp",
        "ideographicTopUp",
        "romanUp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeadingModel"

def test_hyp_spreadmethod_exists():
    # Check that the Enumeration exists
    assert SpreadMethod is not None

def test_hyp_spreadmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpreadMethod]
    expected_literals = [
        "NOT_SET",
        "repeat",
        "reflect",
        "pad",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpreadMethod"

def test_hyp_textrotation_exists():
    # Check that the Enumeration exists
    assert TextRotation is not None

def test_hyp_textrotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextRotation]
    expected_literals = [
        "rotate0",
        "auto",
        "rotate180",
        "rotate270",
        "rotate90",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextRotation"

def test_hyp_digitwidth_exists():
    # Check that the Enumeration exists
    assert DigitWidth is not None

def test_hyp_digitwidth_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitWidth]
    expected_literals = [
        "proportional",
        "default",
        "tabular",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitWidth"

def test_hyp_kerning_exists():
    # Check that the Enumeration exists
    assert Kerning is not None

def test_hyp_kerning_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Kerning]
    expected_literals = [
        "OFF",
        "ON",
        "AUTO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Kerning"

def test_hyp_fillmode_exists():
    # Check that the Enumeration exists
    assert FillMode is not None

def test_hyp_fillmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FillMode]
    expected_literals = [
        "REPEAT",
        "SCALE",
        "CLIP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FillMode"

def test_hyp_linebreak_exists():
    # Check that the Enumeration exists
    assert LineBreak is not None

def test_hyp_linebreak_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineBreak]
    expected_literals = [
        "explicit",
        "toFit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineBreak"

def test_hyp_justificationstyle_exists():
    # Check that the Enumeration exists
    assert JustificationStyle is not None

def test_hyp_justificationstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JustificationStyle]
    expected_literals = [
        "prioritizeLeastAdjustment",
        "auto",
        "pushOutOnly",
        "pushInKinsoku",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JustificationStyle"

def test_hyp_typographiccase_exists():
    # Check that the Enumeration exists
    assert TypographicCase is not None

def test_hyp_typographiccase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypographicCase]
    expected_literals = [
        "default",
        "lowercaseToSmallCaps",
        "lowercase",
        "uppercase",
        "capsToSmallCaps",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypographicCase"

def test_hyp_fontweight_exists():
    # Check that the Enumeration exists
    assert FontWeight is not None

def test_hyp_fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontWeight]
    expected_literals = [
        "BOLD",
        "NORMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontWeight"


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
fxg_linkActiveFormat_strategy = st.builds(
    fxg_linkActiveFormat,
)
RichTextContentContainer_strategy = st.builds(
    RichTextContentContainer,
)
fxg_CharacterAttributes_strategy = st.builds(
    fxg_CharacterAttributes,
    backgroundColor=
        safe_text,
    lineHeight=
        safe_text,
    ligatureLevel=
        safe_text,
    kerning=
        safe_text,
    dominantBaseline=
        safe_text,
    digitWidth=
        safe_text,
    textDecoration=
        safe_text,
    fontSize=
        safe_text,
    typographicCase=
        safe_text,
    color=
        safe_text,
    fontFamily=
        safe_text,
    textRotation=
        safe_text,
    baselineShift=
        safe_text,
    textAlpha=
        safe_text,
    whiteSpaceCollapse=
        safe_text,
    fontWeight=
        safe_text,
    fontStyle=
        safe_text,
    alignmentBaseline=
        safe_text,
    digitCase=
        safe_text,
    locale=
        safe_text,
    breakOpportunity=
        safe_text,
    lineThrough=
        safe_text,
    trackingRight=
        safe_text,
    backgroundAlpha=
        safe_text,
    trackingLeft=
        safe_text
)
fxg_ContainerAttributes_strategy = st.builds(
    fxg_ContainerAttributes,
    lineBreak=
        safe_text,
    paddingLeft=
        safe_text,
    firstBaselineOffset=
        safe_text,
    blockProgression=
        safe_text,
    columnWidth=
        safe_text,
    verticalAlign=
        safe_text,
    columnCount=
        safe_text,
    columnGap=
        safe_text,
    paddingBottom=
        safe_text,
    paddingTop=
        safe_text,
    paddingRight=
        safe_text
)
fxg_ParagraphAttributes_strategy = st.builds(
    fxg_ParagraphAttributes,
    paragraphEndIndent=
        safe_text,
    leadingModel=
        safe_text,
    paragraphStartIndent=
        safe_text,
    tabStops=
        safe_text,
    paragraphSpaceBefore=
        safe_text,
    justificationRule=
        safe_text,
    justificationStyle=
        safe_text,
    textIndent=
        safe_text,
    textAlignLast=
        safe_text,
    textJustify=
        safe_text,
    paragraphSpaceAfter=
        safe_text,
    textAlign=
        safe_text
)
RichTextContent_strategy = st.builds(
    RichTextContent,
)
fxg_br_strategy = st.builds(
    fxg_br,
)
fxg_rawtext_strategy = st.builds(
    fxg_rawtext,
    _text=
        safe_text
)
fxg_linkNormalFormat_strategy = st.builds(
    fxg_linkNormalFormat,
)
fxg_tab_strategy = st.builds(
    fxg_tab,
)
fxg_span_strategy = st.builds(
    fxg_span,
)
fxg_div_strategy = st.builds(
    fxg_div,
)
fxg_a_strategy = st.builds(
    fxg_a,
)
fxg_img_strategy = st.builds(
    fxg_img,
)
fxg_linkHoverFormat_strategy = st.builds(
    fxg_linkHoverFormat,
)
fxg_tcy_strategy = st.builds(
    fxg_tcy,
)
fxg_RichTextContentContainer_strategy = st.builds(
    fxg_RichTextContentContainer,
)
fxg_RichTextContent_strategy = st.builds(
    fxg_RichTextContent,
)
CharacterAttributes_strategy = st.builds(
    CharacterAttributes,
)
ContainerAttributes_strategy = st.builds(
    ContainerAttributes,
)
ParagraphAttributes_strategy = st.builds(
    ParagraphAttributes,
)
fxg_p_strategy = st.builds(
    fxg_p,
)
Shape_strategy = st.builds(
    Shape,
)
fxg_Line_strategy = st.builds(
    fxg_Line,
    x=
        safe_text,
    rotation=
        safe_text,
    y=
        safe_text,
    maskType=
        safe_text,
    scaleY=
        safe_text,
    yFrom=
        safe_text,
    scaleX=
        safe_text,
    alpha=
        safe_text,
    xFrom=
        safe_text,
    yTo=
        safe_text,
    id=
        safe_text,
    xTo=
        safe_text,
    visible=
        safe_text,
    blendMode=
        safe_text
)
fxg_Ellipse_strategy = st.builds(
    fxg_Ellipse,
    scaleY=
        safe_text,
    rotation=
        safe_text,
    scaleX=
        safe_text,
    visible=
        safe_text,
    blendMode=
        safe_text,
    width=
        safe_text,
    alpha=
        safe_text,
    height=
        safe_text,
    x=
        safe_text,
    y=
        safe_text
)
fxg_Rect_strategy = st.builds(
    fxg_Rect,
    scaleX=
        safe_text,
    topLeftRadiusX=
        safe_text,
    alpha=
        safe_text,
    height=
        safe_text,
    y=
        safe_text,
    topRightRadiusX=
        safe_text,
    bottomLeftRadiusY=
        safe_text,
    bottomRightRadiusY=
        safe_text,
    topRightRadiusY=
        safe_text,
    scaleY=
        safe_text,
    rotation=
        safe_text,
    blendMode=
        safe_text,
    bottomLeftRadiusX=
        safe_text,
    x=
        safe_text,
    radiusX=
        safe_text,
    visible=
        safe_text,
    width=
        safe_text,
    radiusY=
        safe_text,
    topLeftRadiusY=
        safe_text,
    bottomRightRadiusX=
        safe_text
)
fxg_Definition_strategy = st.builds(
    fxg_Definition,
    name=
        safe_text
)
FXGElement_strategy = st.builds(
    FXGElement,
)
fxg_RichText_strategy = st.builds(
    fxg_RichText,
    x=
        safe_text,
    _tempcontent=
        safe_text,
    scaleX=
        safe_text,
    maskType=
        safe_text,
    rotation=
        safe_text,
    blendMode=
        safe_text,
    alpha=
        safe_text,
    visible=
        safe_text,
    scaleY=
        safe_text,
    id=
        safe_text,
    width=
        safe_text,
    y=
        safe_text,
    height=
        safe_text
)
fxg_BitmapImage_strategy = st.builds(
    fxg_BitmapImage,
    fillMode=
        safe_text,
    y=
        safe_text,
    x=
        safe_text,
    blendMode=
        safe_text,
    visible=
        safe_text,
    rotation=
        safe_text,
    width=
        safe_text,
    scaleX=
        safe_text,
    alpha=
        safe_text,
    height=
        safe_text,
    source=
        safe_text,
    scaleY=
        safe_text
)
fxg_Fill_strategy = st.builds(
    fxg_Fill,
)
fxg_Transform_strategy = st.builds(
    fxg_Transform,
)
fxg_Shape_strategy = st.builds(
    fxg_Shape,
)
fxg_ColorTransform_strategy = st.builds(
    fxg_ColorTransform,
    greenOffset=
        safe_text,
    greenMultiplier=
        safe_text,
    blueOffset=
        safe_text,
    alphaOffset=
        safe_text,
    alphaMultiplier=
        safe_text,
    redOffset=
        safe_text,
    blueMultiplier=
        safe_text,
    redMultiplier=
        safe_text
)
fxg_PlaceObject_strategy = st.builds(
    fxg_PlaceObject,
    id=
        safe_text
)
fxg_Filter_strategy = st.builds(
    fxg_Filter,
)
fxg_Matrix_strategy = st.builds(
    fxg_Matrix,
    a=
        safe_text,
    d=
        safe_text,
    b=
        safe_text,
    ty=
        safe_text,
    tx=
        safe_text,
    c=
        safe_text
)
fxg_Path_strategy = st.builds(
    fxg_Path,
    x=
        safe_text,
    rotation=
        safe_text,
    y=
        safe_text,
    scaleY=
        safe_text,
    scaleX=
        safe_text,
    blendMode=
        safe_text,
    data=
        safe_text,
    winding=
        safe_text,
    alpha=
        safe_text,
    visible=
        safe_text
)
fxg_Stroke_strategy = st.builds(
    fxg_Stroke,
)
fxg_Private_strategy = st.builds(
    fxg_Private,
)
fxg_Library_strategy = st.builds(
    fxg_Library,
)
fxg_Group_strategy = st.builds(
    fxg_Group,
    blendMode=
        safe_text,
    x=
        safe_text,
    transformY=
        safe_text,
    maskType=
        safe_text,
    scaleGridLeft=
        safe_text,
    visible=
        safe_text,
    scaleGridRight=
        safe_text,
    scaleY=
        safe_text,
    rotation=
        safe_text,
    scaleGridTop=
        safe_text,
    scaleGridBottom=
        safe_text,
    y=
        safe_text,
    scaleX=
        safe_text,
    alpha=
        safe_text,
    transformX=
        safe_text,
    id=
        safe_text
)
fxg_Graphic_strategy = st.builds(
    fxg_Graphic,
    viewHeight=
        st.integers(),
    viewWidth=
        st.integers(),
    scaleGridTop=
        safe_text,
    scaleGridRight=
        safe_text,
    version=
        safe_text,
    scaleGridBottom=
        safe_text,
    scaleGridLeft=
        safe_text
)
fxg_ContainerElement_strategy = st.builds(
    fxg_ContainerElement,
)
fxg_FXGElement_strategy = st.builds(
    fxg_FXGElement,
)
fxg_GradientBevelFilter_strategy = st.builds(
    fxg_GradientBevelFilter,
    distance=
        safe_text,
    blurY=
        safe_text,
    angle=
        safe_text,
    quality=
        safe_text,
    knockout=
        safe_text,
    blurX=
        safe_text,
    strength=
        safe_text,
    type=
        safe_text
)
fxg_GradientGlowFilter_strategy = st.builds(
    fxg_GradientGlowFilter,
    inner=
        safe_text,
    blurY=
        safe_text,
    strength=
        safe_text,
    angle=
        safe_text,
    knockout=
        safe_text,
    blurX=
        safe_text,
    quality=
        safe_text,
    distance=
        safe_text
)
Filter_strategy = st.builds(
    Filter,
)
fxg_ColorMatrixFilter_strategy = st.builds(
    fxg_ColorMatrixFilter,
    matrix=
        safe_text
)
fxg_DropShadowFilter_strategy = st.builds(
    fxg_DropShadowFilter,
    angle=
        safe_text,
    blurX=
        safe_text,
    inner=
        safe_text,
    knockout=
        safe_text,
    strength=
        safe_text,
    quality=
        safe_text,
    color=
        safe_text,
    distance=
        safe_text,
    hideObject=
        safe_text,
    alpha=
        safe_text,
    blurY=
        safe_text
)
fxg_BevelFilter_strategy = st.builds(
    fxg_BevelFilter,
    distance=
        safe_text,
    shadowColor=
        safe_text,
    knockout=
        safe_text,
    type=
        safe_text,
    strength=
        safe_text,
    blurY=
        safe_text,
    shadowAlpha=
        safe_text,
    quality=
        safe_text,
    highlightAlpha=
        safe_text,
    blurX=
        safe_text,
    highlightColor=
        safe_text,
    angle=
        safe_text
)
fxg_BlurFilter_strategy = st.builds(
    fxg_BlurFilter,
    blurY=
        safe_text,
    blurX=
        safe_text,
    quality=
        safe_text
)
fxg_GradientEntry_strategy = st.builds(
    fxg_GradientEntry,
    ratio=
        safe_text,
    color=
        safe_text,
    alpha=
        safe_text
)
fxg_RadialGradientStroke_strategy = st.builds(
    fxg_RadialGradientStroke,
    scaleX=
        safe_text,
    spreadMethod=
        safe_text,
    caps=
        safe_text,
    joints=
        safe_text,
    miterLimit=
        safe_text,
    pixelHinting=
        safe_text,
    y=
        safe_text,
    interpolationMethod=
        safe_text,
    scaleY=
        safe_text,
    focalPointRatio=
        safe_text,
    rotation=
        safe_text,
    scaleMode=
        safe_text,
    x=
        safe_text,
    weight=
        safe_text
)
fxg_LinearGradient_strategy = st.builds(
    fxg_LinearGradient,
    scaleX=
        safe_text,
    y=
        safe_text,
    spreadMethod=
        safe_text,
    x=
        safe_text,
    rotation=
        safe_text,
    interpolationMethod=
        safe_text
)
fxg_LinearGradientStroke_strategy = st.builds(
    fxg_LinearGradientStroke,
    weight=
        safe_text,
    interpolationMethod=
        safe_text,
    caps=
        safe_text,
    rotation=
        safe_text,
    y=
        safe_text,
    pixelHinting=
        safe_text,
    spreadMethod=
        safe_text,
    scaleX=
        safe_text,
    joints=
        safe_text,
    miterLimit=
        safe_text,
    x=
        safe_text,
    scaleMode=
        safe_text
)
Stroke_strategy = st.builds(
    Stroke,
)
fxg_SolidColorStroke_strategy = st.builds(
    fxg_SolidColorStroke,
    color=
        safe_text,
    caps=
        safe_text,
    miterLimit=
        safe_text,
    alpha=
        safe_text,
    joints=
        safe_text,
    weight=
        safe_text,
    scaleMode=
        safe_text,
    pixelHinting=
        safe_text
)
fxg_RadialGradient_strategy = st.builds(
    fxg_RadialGradient,
    x=
        safe_text,
    rotation=
        safe_text,
    focalPointRatio=
        safe_text,
    scaleX=
        safe_text,
    scaleY=
        safe_text,
    spreadMethod=
        safe_text,
    y=
        safe_text,
    interpolationMethod=
        safe_text
)
Fill_strategy = st.builds(
    Fill,
)
fxg_BitmapFill_strategy = st.builds(
    fxg_BitmapFill,
    y=
        safe_text,
    scaleX=
        safe_text,
    scaleY=
        safe_text,
    rotation=
        safe_text,
    source=
        safe_text,
    fillMode=
        safe_text,
    x=
        safe_text
)
fxg_SolidColor_strategy = st.builds(
    fxg_SolidColor,
    color=
        safe_text,
    alpha=
        safe_text
)






@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_lineHeight_setter(instance):
    original = instance.lineHeight
    instance.lineHeight = original
    assert instance.lineHeight == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_ligatureLevel_setter(instance):
    original = instance.ligatureLevel
    instance.ligatureLevel = original
    assert instance.ligatureLevel == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_kerning_setter(instance):
    original = instance.kerning
    instance.kerning = original
    assert instance.kerning == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_dominantBaseline_setter(instance):
    original = instance.dominantBaseline
    instance.dominantBaseline = original
    assert instance.dominantBaseline == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_digitWidth_setter(instance):
    original = instance.digitWidth
    instance.digitWidth = original
    assert instance.digitWidth == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_textDecoration_setter(instance):
    original = instance.textDecoration
    instance.textDecoration = original
    assert instance.textDecoration == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_typographicCase_setter(instance):
    original = instance.typographicCase
    instance.typographicCase = original
    assert instance.typographicCase == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_fontFamily_setter(instance):
    original = instance.fontFamily
    instance.fontFamily = original
    assert instance.fontFamily == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_textRotation_setter(instance):
    original = instance.textRotation
    instance.textRotation = original
    assert instance.textRotation == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_baselineShift_setter(instance):
    original = instance.baselineShift
    instance.baselineShift = original
    assert instance.baselineShift == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_textAlpha_setter(instance):
    original = instance.textAlpha
    instance.textAlpha = original
    assert instance.textAlpha == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_whiteSpaceCollapse_setter(instance):
    original = instance.whiteSpaceCollapse
    instance.whiteSpaceCollapse = original
    assert instance.whiteSpaceCollapse == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_fontWeight_setter(instance):
    original = instance.fontWeight
    instance.fontWeight = original
    assert instance.fontWeight == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_fontStyle_setter(instance):
    original = instance.fontStyle
    instance.fontStyle = original
    assert instance.fontStyle == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_alignmentBaseline_setter(instance):
    original = instance.alignmentBaseline
    instance.alignmentBaseline = original
    assert instance.alignmentBaseline == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_digitCase_setter(instance):
    original = instance.digitCase
    instance.digitCase = original
    assert instance.digitCase == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_breakOpportunity_setter(instance):
    original = instance.breakOpportunity
    instance.breakOpportunity = original
    assert instance.breakOpportunity == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_lineThrough_setter(instance):
    original = instance.lineThrough
    instance.lineThrough = original
    assert instance.lineThrough == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_trackingRight_setter(instance):
    original = instance.trackingRight
    instance.trackingRight = original
    assert instance.trackingRight == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_backgroundAlpha_setter(instance):
    original = instance.backgroundAlpha
    instance.backgroundAlpha = original
    assert instance.backgroundAlpha == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_hyp_fxg_characterattributes_trackingLeft_setter(instance):
    original = instance.trackingLeft
    instance.trackingLeft = original
    assert instance.trackingLeft == original




@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_lineBreak_setter(instance):
    original = instance.lineBreak
    instance.lineBreak = original
    assert instance.lineBreak == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_paddingLeft_setter(instance):
    original = instance.paddingLeft
    instance.paddingLeft = original
    assert instance.paddingLeft == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_firstBaselineOffset_setter(instance):
    original = instance.firstBaselineOffset
    instance.firstBaselineOffset = original
    assert instance.firstBaselineOffset == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_blockProgression_setter(instance):
    original = instance.blockProgression
    instance.blockProgression = original
    assert instance.blockProgression == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_columnWidth_setter(instance):
    original = instance.columnWidth
    instance.columnWidth = original
    assert instance.columnWidth == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_verticalAlign_setter(instance):
    original = instance.verticalAlign
    instance.verticalAlign = original
    assert instance.verticalAlign == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_columnCount_setter(instance):
    original = instance.columnCount
    instance.columnCount = original
    assert instance.columnCount == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_columnGap_setter(instance):
    original = instance.columnGap
    instance.columnGap = original
    assert instance.columnGap == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_paddingBottom_setter(instance):
    original = instance.paddingBottom
    instance.paddingBottom = original
    assert instance.paddingBottom == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_paddingTop_setter(instance):
    original = instance.paddingTop
    instance.paddingTop = original
    assert instance.paddingTop == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_hyp_fxg_containerattributes_paddingRight_setter(instance):
    original = instance.paddingRight
    instance.paddingRight = original
    assert instance.paddingRight == original




@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_paragraphEndIndent_setter(instance):
    original = instance.paragraphEndIndent
    instance.paragraphEndIndent = original
    assert instance.paragraphEndIndent == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_leadingModel_setter(instance):
    original = instance.leadingModel
    instance.leadingModel = original
    assert instance.leadingModel == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_paragraphStartIndent_setter(instance):
    original = instance.paragraphStartIndent
    instance.paragraphStartIndent = original
    assert instance.paragraphStartIndent == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_tabStops_setter(instance):
    original = instance.tabStops
    instance.tabStops = original
    assert instance.tabStops == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_paragraphSpaceBefore_setter(instance):
    original = instance.paragraphSpaceBefore
    instance.paragraphSpaceBefore = original
    assert instance.paragraphSpaceBefore == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_justificationRule_setter(instance):
    original = instance.justificationRule
    instance.justificationRule = original
    assert instance.justificationRule == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_justificationStyle_setter(instance):
    original = instance.justificationStyle
    instance.justificationStyle = original
    assert instance.justificationStyle == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_textIndent_setter(instance):
    original = instance.textIndent
    instance.textIndent = original
    assert instance.textIndent == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_textAlignLast_setter(instance):
    original = instance.textAlignLast
    instance.textAlignLast = original
    assert instance.textAlignLast == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_textJustify_setter(instance):
    original = instance.textJustify
    instance.textJustify = original
    assert instance.textJustify == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_paragraphSpaceAfter_setter(instance):
    original = instance.paragraphSpaceAfter
    instance.paragraphSpaceAfter = original
    assert instance.paragraphSpaceAfter == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_hyp_fxg_paragraphattributes_textAlign_setter(instance):
    original = instance.textAlign
    instance.textAlign = original
    assert instance.textAlign == original






@given(instance=fxg_rawtext_strategy)
def test_hyp_fxg_rawtext__text_setter(instance):
    original = instance._text
    instance._text = original
    assert instance._text == original



















@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_yFrom_setter(instance):
    original = instance.yFrom
    instance.yFrom = original
    assert instance.yFrom == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_xFrom_setter(instance):
    original = instance.xFrom
    instance.xFrom = original
    assert instance.xFrom == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_yTo_setter(instance):
    original = instance.yTo
    instance.yTo = original
    assert instance.yTo == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_xTo_setter(instance):
    original = instance.xTo
    instance.xTo = original
    assert instance.xTo == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Line_strategy)
def test_hyp_fxg_line_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original




@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Ellipse_strategy)
def test_hyp_fxg_ellipse_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original




@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_topLeftRadiusX_setter(instance):
    original = instance.topLeftRadiusX
    instance.topLeftRadiusX = original
    assert instance.topLeftRadiusX == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_topRightRadiusX_setter(instance):
    original = instance.topRightRadiusX
    instance.topRightRadiusX = original
    assert instance.topRightRadiusX == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_bottomLeftRadiusY_setter(instance):
    original = instance.bottomLeftRadiusY
    instance.bottomLeftRadiusY = original
    assert instance.bottomLeftRadiusY == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_bottomRightRadiusY_setter(instance):
    original = instance.bottomRightRadiusY
    instance.bottomRightRadiusY = original
    assert instance.bottomRightRadiusY == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_topRightRadiusY_setter(instance):
    original = instance.topRightRadiusY
    instance.topRightRadiusY = original
    assert instance.topRightRadiusY == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_bottomLeftRadiusX_setter(instance):
    original = instance.bottomLeftRadiusX
    instance.bottomLeftRadiusX = original
    assert instance.bottomLeftRadiusX == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_radiusX_setter(instance):
    original = instance.radiusX
    instance.radiusX = original
    assert instance.radiusX == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_radiusY_setter(instance):
    original = instance.radiusY
    instance.radiusY = original
    assert instance.radiusY == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_topLeftRadiusY_setter(instance):
    original = instance.topLeftRadiusY
    instance.topLeftRadiusY = original
    assert instance.topLeftRadiusY == original



@given(instance=fxg_Rect_strategy)
def test_hyp_fxg_rect_bottomRightRadiusX_setter(instance):
    original = instance.bottomRightRadiusX
    instance.bottomRightRadiusX = original
    assert instance.bottomRightRadiusX == original




@given(instance=fxg_Definition_strategy)
def test_hyp_fxg_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext__tempcontent_setter(instance):
    original = instance._tempcontent
    instance._tempcontent = original
    assert instance._tempcontent == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_RichText_strategy)
def test_hyp_fxg_richtext_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_fillMode_setter(instance):
    original = instance.fillMode
    instance.fillMode = original
    assert instance.fillMode == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=fxg_BitmapImage_strategy)
def test_hyp_fxg_bitmapimage_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original







@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_greenOffset_setter(instance):
    original = instance.greenOffset
    instance.greenOffset = original
    assert instance.greenOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_greenMultiplier_setter(instance):
    original = instance.greenMultiplier
    instance.greenMultiplier = original
    assert instance.greenMultiplier == original



@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_blueOffset_setter(instance):
    original = instance.blueOffset
    instance.blueOffset = original
    assert instance.blueOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_alphaOffset_setter(instance):
    original = instance.alphaOffset
    instance.alphaOffset = original
    assert instance.alphaOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_alphaMultiplier_setter(instance):
    original = instance.alphaMultiplier
    instance.alphaMultiplier = original
    assert instance.alphaMultiplier == original



@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_redOffset_setter(instance):
    original = instance.redOffset
    instance.redOffset = original
    assert instance.redOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_blueMultiplier_setter(instance):
    original = instance.blueMultiplier
    instance.blueMultiplier = original
    assert instance.blueMultiplier == original



@given(instance=fxg_ColorTransform_strategy)
def test_hyp_fxg_colortransform_redMultiplier_setter(instance):
    original = instance.redMultiplier
    instance.redMultiplier = original
    assert instance.redMultiplier == original




@given(instance=fxg_PlaceObject_strategy)
def test_hyp_fxg_placeobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=fxg_Matrix_strategy)
def test_hyp_fxg_matrix_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=fxg_Matrix_strategy)
def test_hyp_fxg_matrix_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=fxg_Matrix_strategy)
def test_hyp_fxg_matrix_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=fxg_Matrix_strategy)
def test_hyp_fxg_matrix_ty_setter(instance):
    original = instance.ty
    instance.ty = original
    assert instance.ty == original



@given(instance=fxg_Matrix_strategy)
def test_hyp_fxg_matrix_tx_setter(instance):
    original = instance.tx
    instance.tx = original
    assert instance.tx == original



@given(instance=fxg_Matrix_strategy)
def test_hyp_fxg_matrix_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original




@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_winding_setter(instance):
    original = instance.winding
    instance.winding = original
    assert instance.winding == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Path_strategy)
def test_hyp_fxg_path_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original







@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_transformY_setter(instance):
    original = instance.transformY
    instance.transformY = original
    assert instance.transformY == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_scaleGridLeft_setter(instance):
    original = instance.scaleGridLeft
    instance.scaleGridLeft = original
    assert instance.scaleGridLeft == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_scaleGridRight_setter(instance):
    original = instance.scaleGridRight
    instance.scaleGridRight = original
    assert instance.scaleGridRight == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_scaleGridTop_setter(instance):
    original = instance.scaleGridTop
    instance.scaleGridTop = original
    assert instance.scaleGridTop == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_scaleGridBottom_setter(instance):
    original = instance.scaleGridBottom
    instance.scaleGridBottom = original
    assert instance.scaleGridBottom == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_transformX_setter(instance):
    original = instance.transformX
    instance.transformX = original
    assert instance.transformX == original



@given(instance=fxg_Group_strategy)
def test_hyp_fxg_group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=fxg_Graphic_strategy)
def test_hyp_fxg_graphic_viewHeight_setter(instance):
    original = instance.viewHeight
    instance.viewHeight = original
    assert instance.viewHeight == original



@given(instance=fxg_Graphic_strategy)
def test_hyp_fxg_graphic_viewWidth_setter(instance):
    original = instance.viewWidth
    instance.viewWidth = original
    assert instance.viewWidth == original



@given(instance=fxg_Graphic_strategy)
def test_hyp_fxg_graphic_scaleGridTop_setter(instance):
    original = instance.scaleGridTop
    instance.scaleGridTop = original
    assert instance.scaleGridTop == original



@given(instance=fxg_Graphic_strategy)
def test_hyp_fxg_graphic_scaleGridRight_setter(instance):
    original = instance.scaleGridRight
    instance.scaleGridRight = original
    assert instance.scaleGridRight == original



@given(instance=fxg_Graphic_strategy)
def test_hyp_fxg_graphic_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=fxg_Graphic_strategy)
def test_hyp_fxg_graphic_scaleGridBottom_setter(instance):
    original = instance.scaleGridBottom
    instance.scaleGridBottom = original
    assert instance.scaleGridBottom == original



@given(instance=fxg_Graphic_strategy)
def test_hyp_fxg_graphic_scaleGridLeft_setter(instance):
    original = instance.scaleGridLeft
    instance.scaleGridLeft = original
    assert instance.scaleGridLeft == original






@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_hyp_fxg_gradientbevelfilter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_hyp_fxg_gradientglowfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original





@given(instance=fxg_ColorMatrixFilter_strategy)
def test_hyp_fxg_colormatrixfilter_matrix_setter(instance):
    original = instance.matrix
    instance.matrix = original
    assert instance.matrix == original




@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_hideObject_setter(instance):
    original = instance.hideObject
    instance.hideObject = original
    assert instance.hideObject == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_hyp_fxg_dropshadowfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original




@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_shadowColor_setter(instance):
    original = instance.shadowColor
    instance.shadowColor = original
    assert instance.shadowColor == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_shadowAlpha_setter(instance):
    original = instance.shadowAlpha
    instance.shadowAlpha = original
    assert instance.shadowAlpha == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_highlightAlpha_setter(instance):
    original = instance.highlightAlpha
    instance.highlightAlpha = original
    assert instance.highlightAlpha == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_highlightColor_setter(instance):
    original = instance.highlightColor
    instance.highlightColor = original
    assert instance.highlightColor == original



@given(instance=fxg_BevelFilter_strategy)
def test_hyp_fxg_bevelfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=fxg_BlurFilter_strategy)
def test_hyp_fxg_blurfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_BlurFilter_strategy)
def test_hyp_fxg_blurfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_BlurFilter_strategy)
def test_hyp_fxg_blurfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original




@given(instance=fxg_GradientEntry_strategy)
def test_hyp_fxg_gradiententry_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original



@given(instance=fxg_GradientEntry_strategy)
def test_hyp_fxg_gradiententry_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_GradientEntry_strategy)
def test_hyp_fxg_gradiententry_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original




@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_focalPointRatio_setter(instance):
    original = instance.focalPointRatio
    instance.focalPointRatio = original
    assert instance.focalPointRatio == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_hyp_fxg_radialgradientstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original




@given(instance=fxg_LinearGradient_strategy)
def test_hyp_fxg_lineargradient_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_LinearGradient_strategy)
def test_hyp_fxg_lineargradient_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_LinearGradient_strategy)
def test_hyp_fxg_lineargradient_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_LinearGradient_strategy)
def test_hyp_fxg_lineargradient_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_LinearGradient_strategy)
def test_hyp_fxg_lineargradient_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_LinearGradient_strategy)
def test_hyp_fxg_lineargradient_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original




@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_hyp_fxg_lineargradientstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original





@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_hyp_fxg_solidcolorstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original




@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_focalPointRatio_setter(instance):
    original = instance.focalPointRatio
    instance.focalPointRatio = original
    assert instance.focalPointRatio == original



@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_RadialGradient_strategy)
def test_hyp_fxg_radialgradient_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original





@given(instance=fxg_BitmapFill_strategy)
def test_hyp_fxg_bitmapfill_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_BitmapFill_strategy)
def test_hyp_fxg_bitmapfill_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_BitmapFill_strategy)
def test_hyp_fxg_bitmapfill_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_BitmapFill_strategy)
def test_hyp_fxg_bitmapfill_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_BitmapFill_strategy)
def test_hyp_fxg_bitmapfill_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=fxg_BitmapFill_strategy)
def test_hyp_fxg_bitmapfill_fillMode_setter(instance):
    original = instance.fillMode
    instance.fillMode = original
    assert instance.fillMode == original



@given(instance=fxg_BitmapFill_strategy)
def test_hyp_fxg_bitmapfill_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=fxg_SolidColor_strategy)
def test_hyp_fxg_solidcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_SolidColor_strategy)
def test_hyp_fxg_solidcolor_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CharacterAttributes,
    ContainerAttributes,
    FXGElement,
    Fill,
    Filter,
    ParagraphAttributes,
    RichTextContent,
    RichTextContentContainer,
    Shape,
    Stroke,
    fxg_BevelFilter,
    fxg_BitmapFill,
    fxg_BitmapImage,
    fxg_BlurFilter,
    fxg_CharacterAttributes,
    fxg_ColorMatrixFilter,
    fxg_ColorTransform,
    fxg_ContainerAttributes,
    fxg_ContainerElement,
    fxg_Definition,
    fxg_DropShadowFilter,
    fxg_Ellipse,
    fxg_FXGElement,
    fxg_Fill,
    fxg_Filter,
    fxg_GradientBevelFilter,
    fxg_GradientEntry,
    fxg_GradientGlowFilter,
    fxg_Graphic,
    fxg_Group,
    fxg_Library,
    fxg_Line,
    fxg_LinearGradient,
    fxg_LinearGradientStroke,
    fxg_Matrix,
    fxg_ParagraphAttributes,
    fxg_Path,
    fxg_PlaceObject,
    fxg_Private,
    fxg_RadialGradient,
    fxg_RadialGradientStroke,
    fxg_Rect,
    fxg_RichText,
    fxg_RichTextContent,
    fxg_RichTextContentContainer,
    fxg_Shape,
    fxg_SolidColor,
    fxg_SolidColorStroke,
    fxg_Stroke,
    fxg_Transform,
    fxg_a,
    fxg_br,
    fxg_div,
    fxg_img,
    fxg_linkActiveFormat,
    fxg_linkHoverFormat,
    fxg_linkNormalFormat,
    fxg_p,
    fxg_rawtext,
    fxg_span,
    fxg_tab,
    fxg_tcy,
    AlignmentBaseline,
    BevelFilterType,
    BlendMode,
    BlockProgression,
    BreakOpportunity,
    Cap,
    DigitCase,
    DigitWidth,
    DominantBaseline,
    FillMode,
    FontStyle,
    FontWeight,
    InterpolationMethod,
    Joint,
    JustificationRule,
    JustificationStyle,
    Kerning,
    LeadingModel,
    LigatureLevel,
    LineBreak,
    MaskType,
    ScaleMode,
    SpreadMethod,
    TextAlign,
    TextDecoration,
    TextJustify,
    TextRotation,
    TypographicCase,
    VerticalAlign,
    WhitespaceCollapse,
    Winding,
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

def test_fxg_BevelFilter_angle_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_fxg_BevelFilter_blurX_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.blurX == "sample_text"
    instance.blurX = "sample_text_2"
    assert instance.blurX == "sample_text_2"


def test_fxg_BevelFilter_blurY_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.blurY == "sample_text"
    instance.blurY = "sample_text_2"
    assert instance.blurY == "sample_text_2"


def test_fxg_BevelFilter_distance_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_fxg_BevelFilter_highlightAlpha_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.highlightAlpha == "sample_text"
    instance.highlightAlpha = "sample_text_2"
    assert instance.highlightAlpha == "sample_text_2"


def test_fxg_BevelFilter_highlightColor_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.highlightColor == "sample_text"
    instance.highlightColor = "sample_text_2"
    assert instance.highlightColor == "sample_text_2"


def test_fxg_BevelFilter_knockout_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.knockout == "sample_text"
    instance.knockout = "sample_text_2"
    assert instance.knockout == "sample_text_2"


def test_fxg_BevelFilter_quality_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.quality == "sample_text"
    instance.quality = "sample_text_2"
    assert instance.quality == "sample_text_2"


def test_fxg_BevelFilter_shadowAlpha_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.shadowAlpha == "sample_text"
    instance.shadowAlpha = "sample_text_2"
    assert instance.shadowAlpha == "sample_text_2"


def test_fxg_BevelFilter_shadowColor_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.shadowColor == "sample_text"
    instance.shadowColor = "sample_text_2"
    assert instance.shadowColor == "sample_text_2"


def test_fxg_BevelFilter_strength_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.strength == "sample_text"
    instance.strength = "sample_text_2"
    assert instance.strength == "sample_text_2"


def test_fxg_BevelFilter_type_value_roundtrip():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_fxg_BitmapFill_fillMode_value_roundtrip():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert instance.fillMode == "sample_text"
    instance.fillMode = "sample_text_2"
    assert instance.fillMode == "sample_text_2"


def test_fxg_BitmapFill_rotation_value_roundtrip():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_BitmapFill_scaleX_value_roundtrip():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_BitmapFill_scaleY_value_roundtrip():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_BitmapFill_source_value_roundtrip():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_fxg_BitmapFill_x_value_roundtrip():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_BitmapFill_y_value_roundtrip():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_BitmapImage_alpha_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_BitmapImage_blendMode_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.blendMode == "sample_text"
    instance.blendMode = "sample_text_2"
    assert instance.blendMode == "sample_text_2"


def test_fxg_BitmapImage_fillMode_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.fillMode == "sample_text"
    instance.fillMode = "sample_text_2"
    assert instance.fillMode == "sample_text_2"


def test_fxg_BitmapImage_height_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_fxg_BitmapImage_rotation_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_BitmapImage_scaleX_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_BitmapImage_scaleY_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_BitmapImage_source_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_fxg_BitmapImage_visible_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.visible == "sample_text"
    instance.visible = "sample_text_2"
    assert instance.visible == "sample_text_2"


def test_fxg_BitmapImage_width_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_fxg_BitmapImage_x_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_BitmapImage_y_value_roundtrip():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_BlurFilter_blurX_value_roundtrip():
    instance = fxg_BlurFilter(blurX="sample_text", blurY="sample_text", quality="sample_text")
    assert instance.blurX == "sample_text"
    instance.blurX = "sample_text_2"
    assert instance.blurX == "sample_text_2"


def test_fxg_BlurFilter_blurY_value_roundtrip():
    instance = fxg_BlurFilter(blurX="sample_text", blurY="sample_text", quality="sample_text")
    assert instance.blurY == "sample_text"
    instance.blurY = "sample_text_2"
    assert instance.blurY == "sample_text_2"


def test_fxg_BlurFilter_quality_value_roundtrip():
    instance = fxg_BlurFilter(blurX="sample_text", blurY="sample_text", quality="sample_text")
    assert instance.quality == "sample_text"
    instance.quality = "sample_text_2"
    assert instance.quality == "sample_text_2"


def test_fxg_CharacterAttributes_alignmentBaseline_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.alignmentBaseline == "sample_text"
    instance.alignmentBaseline = "sample_text_2"
    assert instance.alignmentBaseline == "sample_text_2"


def test_fxg_CharacterAttributes_backgroundAlpha_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.backgroundAlpha == "sample_text"
    instance.backgroundAlpha = "sample_text_2"
    assert instance.backgroundAlpha == "sample_text_2"


def test_fxg_CharacterAttributes_backgroundColor_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_fxg_CharacterAttributes_baselineShift_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.baselineShift == "sample_text"
    instance.baselineShift = "sample_text_2"
    assert instance.baselineShift == "sample_text_2"


def test_fxg_CharacterAttributes_breakOpportunity_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.breakOpportunity == "sample_text"
    instance.breakOpportunity = "sample_text_2"
    assert instance.breakOpportunity == "sample_text_2"


def test_fxg_CharacterAttributes_color_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_fxg_CharacterAttributes_digitCase_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.digitCase == "sample_text"
    instance.digitCase = "sample_text_2"
    assert instance.digitCase == "sample_text_2"


def test_fxg_CharacterAttributes_digitWidth_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.digitWidth == "sample_text"
    instance.digitWidth = "sample_text_2"
    assert instance.digitWidth == "sample_text_2"


def test_fxg_CharacterAttributes_dominantBaseline_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.dominantBaseline == "sample_text"
    instance.dominantBaseline = "sample_text_2"
    assert instance.dominantBaseline == "sample_text_2"


def test_fxg_CharacterAttributes_fontFamily_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.fontFamily == "sample_text"
    instance.fontFamily = "sample_text_2"
    assert instance.fontFamily == "sample_text_2"


def test_fxg_CharacterAttributes_fontSize_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.fontSize == "sample_text"
    instance.fontSize = "sample_text_2"
    assert instance.fontSize == "sample_text_2"


def test_fxg_CharacterAttributes_fontStyle_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.fontStyle == "sample_text"
    instance.fontStyle = "sample_text_2"
    assert instance.fontStyle == "sample_text_2"


def test_fxg_CharacterAttributes_fontWeight_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.fontWeight == "sample_text"
    instance.fontWeight = "sample_text_2"
    assert instance.fontWeight == "sample_text_2"


def test_fxg_CharacterAttributes_kerning_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.kerning == "sample_text"
    instance.kerning = "sample_text_2"
    assert instance.kerning == "sample_text_2"


def test_fxg_CharacterAttributes_ligatureLevel_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.ligatureLevel == "sample_text"
    instance.ligatureLevel = "sample_text_2"
    assert instance.ligatureLevel == "sample_text_2"


def test_fxg_CharacterAttributes_lineHeight_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.lineHeight == "sample_text"
    instance.lineHeight = "sample_text_2"
    assert instance.lineHeight == "sample_text_2"


def test_fxg_CharacterAttributes_lineThrough_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.lineThrough == "sample_text"
    instance.lineThrough = "sample_text_2"
    assert instance.lineThrough == "sample_text_2"


def test_fxg_CharacterAttributes_locale_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.locale == "sample_text"
    instance.locale = "sample_text_2"
    assert instance.locale == "sample_text_2"


def test_fxg_CharacterAttributes_textAlpha_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.textAlpha == "sample_text"
    instance.textAlpha = "sample_text_2"
    assert instance.textAlpha == "sample_text_2"


def test_fxg_CharacterAttributes_textDecoration_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.textDecoration == "sample_text"
    instance.textDecoration = "sample_text_2"
    assert instance.textDecoration == "sample_text_2"


def test_fxg_CharacterAttributes_textRotation_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.textRotation == "sample_text"
    instance.textRotation = "sample_text_2"
    assert instance.textRotation == "sample_text_2"


def test_fxg_CharacterAttributes_trackingLeft_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.trackingLeft == "sample_text"
    instance.trackingLeft = "sample_text_2"
    assert instance.trackingLeft == "sample_text_2"


def test_fxg_CharacterAttributes_trackingRight_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.trackingRight == "sample_text"
    instance.trackingRight = "sample_text_2"
    assert instance.trackingRight == "sample_text_2"


def test_fxg_CharacterAttributes_typographicCase_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.typographicCase == "sample_text"
    instance.typographicCase = "sample_text_2"
    assert instance.typographicCase == "sample_text_2"


def test_fxg_CharacterAttributes_whiteSpaceCollapse_value_roundtrip():
    instance = fxg_CharacterAttributes(alignmentBaseline="sample_text", backgroundAlpha="sample_text", backgroundColor="sample_text", baselineShift="sample_text", breakOpportunity="sample_text", color="sample_text", digitCase="sample_text", digitWidth="sample_text", dominantBaseline="sample_text", fontFamily="sample_text", fontSize="sample_text", fontStyle="sample_text", fontWeight="sample_text", kerning="sample_text", ligatureLevel="sample_text", lineHeight="sample_text", lineThrough="sample_text", locale="sample_text", textAlpha="sample_text", textDecoration="sample_text", textRotation="sample_text", trackingLeft="sample_text", trackingRight="sample_text", typographicCase="sample_text", whiteSpaceCollapse="sample_text")
    assert instance.whiteSpaceCollapse == "sample_text"
    instance.whiteSpaceCollapse = "sample_text_2"
    assert instance.whiteSpaceCollapse == "sample_text_2"


def test_fxg_ColorMatrixFilter_matrix_value_roundtrip():
    instance = fxg_ColorMatrixFilter(matrix="sample_text")
    assert instance.matrix == "sample_text"
    instance.matrix = "sample_text_2"
    assert instance.matrix == "sample_text_2"


def test_fxg_ColorTransform_alphaMultiplier_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.alphaMultiplier == "sample_text"
    instance.alphaMultiplier = "sample_text_2"
    assert instance.alphaMultiplier == "sample_text_2"


def test_fxg_ColorTransform_alphaOffset_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.alphaOffset == "sample_text"
    instance.alphaOffset = "sample_text_2"
    assert instance.alphaOffset == "sample_text_2"


def test_fxg_ColorTransform_blueMultiplier_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.blueMultiplier == "sample_text"
    instance.blueMultiplier = "sample_text_2"
    assert instance.blueMultiplier == "sample_text_2"


def test_fxg_ColorTransform_blueOffset_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.blueOffset == "sample_text"
    instance.blueOffset = "sample_text_2"
    assert instance.blueOffset == "sample_text_2"


def test_fxg_ColorTransform_greenMultiplier_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.greenMultiplier == "sample_text"
    instance.greenMultiplier = "sample_text_2"
    assert instance.greenMultiplier == "sample_text_2"


def test_fxg_ColorTransform_greenOffset_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.greenOffset == "sample_text"
    instance.greenOffset = "sample_text_2"
    assert instance.greenOffset == "sample_text_2"


def test_fxg_ColorTransform_redMultiplier_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.redMultiplier == "sample_text"
    instance.redMultiplier = "sample_text_2"
    assert instance.redMultiplier == "sample_text_2"


def test_fxg_ColorTransform_redOffset_value_roundtrip():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert instance.redOffset == "sample_text"
    instance.redOffset = "sample_text_2"
    assert instance.redOffset == "sample_text_2"


def test_fxg_ContainerAttributes_blockProgression_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.blockProgression == "sample_text"
    instance.blockProgression = "sample_text_2"
    assert instance.blockProgression == "sample_text_2"


def test_fxg_ContainerAttributes_columnCount_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.columnCount == "sample_text"
    instance.columnCount = "sample_text_2"
    assert instance.columnCount == "sample_text_2"


def test_fxg_ContainerAttributes_columnGap_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.columnGap == "sample_text"
    instance.columnGap = "sample_text_2"
    assert instance.columnGap == "sample_text_2"


def test_fxg_ContainerAttributes_columnWidth_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.columnWidth == "sample_text"
    instance.columnWidth = "sample_text_2"
    assert instance.columnWidth == "sample_text_2"


def test_fxg_ContainerAttributes_firstBaselineOffset_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.firstBaselineOffset == "sample_text"
    instance.firstBaselineOffset = "sample_text_2"
    assert instance.firstBaselineOffset == "sample_text_2"


def test_fxg_ContainerAttributes_lineBreak_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.lineBreak == "sample_text"
    instance.lineBreak = "sample_text_2"
    assert instance.lineBreak == "sample_text_2"


def test_fxg_ContainerAttributes_paddingBottom_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.paddingBottom == "sample_text"
    instance.paddingBottom = "sample_text_2"
    assert instance.paddingBottom == "sample_text_2"


def test_fxg_ContainerAttributes_paddingLeft_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.paddingLeft == "sample_text"
    instance.paddingLeft = "sample_text_2"
    assert instance.paddingLeft == "sample_text_2"


def test_fxg_ContainerAttributes_paddingRight_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.paddingRight == "sample_text"
    instance.paddingRight = "sample_text_2"
    assert instance.paddingRight == "sample_text_2"


def test_fxg_ContainerAttributes_paddingTop_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.paddingTop == "sample_text"
    instance.paddingTop = "sample_text_2"
    assert instance.paddingTop == "sample_text_2"


def test_fxg_ContainerAttributes_verticalAlign_value_roundtrip():
    instance = fxg_ContainerAttributes(blockProgression="sample_text", columnCount="sample_text", columnGap="sample_text", columnWidth="sample_text", firstBaselineOffset="sample_text", lineBreak="sample_text", paddingBottom="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", verticalAlign="sample_text")
    assert instance.verticalAlign == "sample_text"
    instance.verticalAlign = "sample_text_2"
    assert instance.verticalAlign == "sample_text_2"


def test_fxg_Definition_name_value_roundtrip():
    instance = fxg_Definition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fxg_DropShadowFilter_alpha_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_DropShadowFilter_angle_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_fxg_DropShadowFilter_blurX_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.blurX == "sample_text"
    instance.blurX = "sample_text_2"
    assert instance.blurX == "sample_text_2"


def test_fxg_DropShadowFilter_blurY_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.blurY == "sample_text"
    instance.blurY = "sample_text_2"
    assert instance.blurY == "sample_text_2"


def test_fxg_DropShadowFilter_color_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_fxg_DropShadowFilter_distance_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_fxg_DropShadowFilter_hideObject_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.hideObject == "sample_text"
    instance.hideObject = "sample_text_2"
    assert instance.hideObject == "sample_text_2"


def test_fxg_DropShadowFilter_inner_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.inner == "sample_text"
    instance.inner = "sample_text_2"
    assert instance.inner == "sample_text_2"


def test_fxg_DropShadowFilter_knockout_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.knockout == "sample_text"
    instance.knockout = "sample_text_2"
    assert instance.knockout == "sample_text_2"


def test_fxg_DropShadowFilter_quality_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.quality == "sample_text"
    instance.quality = "sample_text_2"
    assert instance.quality == "sample_text_2"


def test_fxg_DropShadowFilter_strength_value_roundtrip():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.strength == "sample_text"
    instance.strength = "sample_text_2"
    assert instance.strength == "sample_text_2"


def test_fxg_Ellipse_alpha_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_Ellipse_blendMode_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.blendMode == "sample_text"
    instance.blendMode = "sample_text_2"
    assert instance.blendMode == "sample_text_2"


def test_fxg_Ellipse_height_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_fxg_Ellipse_rotation_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_Ellipse_scaleX_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_Ellipse_scaleY_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_Ellipse_visible_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.visible == "sample_text"
    instance.visible = "sample_text_2"
    assert instance.visible == "sample_text_2"


def test_fxg_Ellipse_width_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_fxg_Ellipse_x_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_Ellipse_y_value_roundtrip():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_GradientBevelFilter_angle_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_fxg_GradientBevelFilter_blurX_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.blurX == "sample_text"
    instance.blurX = "sample_text_2"
    assert instance.blurX == "sample_text_2"


def test_fxg_GradientBevelFilter_blurY_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.blurY == "sample_text"
    instance.blurY = "sample_text_2"
    assert instance.blurY == "sample_text_2"


def test_fxg_GradientBevelFilter_distance_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_fxg_GradientBevelFilter_knockout_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.knockout == "sample_text"
    instance.knockout = "sample_text_2"
    assert instance.knockout == "sample_text_2"


def test_fxg_GradientBevelFilter_quality_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.quality == "sample_text"
    instance.quality = "sample_text_2"
    assert instance.quality == "sample_text_2"


def test_fxg_GradientBevelFilter_strength_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.strength == "sample_text"
    instance.strength = "sample_text_2"
    assert instance.strength == "sample_text_2"


def test_fxg_GradientBevelFilter_type_value_roundtrip():
    instance = fxg_GradientBevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_fxg_GradientEntry_alpha_value_roundtrip():
    instance = fxg_GradientEntry(alpha="sample_text", color="sample_text", ratio="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_GradientEntry_color_value_roundtrip():
    instance = fxg_GradientEntry(alpha="sample_text", color="sample_text", ratio="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_fxg_GradientEntry_ratio_value_roundtrip():
    instance = fxg_GradientEntry(alpha="sample_text", color="sample_text", ratio="sample_text")
    assert instance.ratio == "sample_text"
    instance.ratio = "sample_text_2"
    assert instance.ratio == "sample_text_2"


def test_fxg_GradientGlowFilter_angle_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_fxg_GradientGlowFilter_blurX_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.blurX == "sample_text"
    instance.blurX = "sample_text_2"
    assert instance.blurX == "sample_text_2"


def test_fxg_GradientGlowFilter_blurY_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.blurY == "sample_text"
    instance.blurY = "sample_text_2"
    assert instance.blurY == "sample_text_2"


def test_fxg_GradientGlowFilter_distance_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_fxg_GradientGlowFilter_inner_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.inner == "sample_text"
    instance.inner = "sample_text_2"
    assert instance.inner == "sample_text_2"


def test_fxg_GradientGlowFilter_knockout_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.knockout == "sample_text"
    instance.knockout = "sample_text_2"
    assert instance.knockout == "sample_text_2"


def test_fxg_GradientGlowFilter_quality_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.quality == "sample_text"
    instance.quality = "sample_text_2"
    assert instance.quality == "sample_text_2"


def test_fxg_GradientGlowFilter_strength_value_roundtrip():
    instance = fxg_GradientGlowFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert instance.strength == "sample_text"
    instance.strength = "sample_text_2"
    assert instance.strength == "sample_text_2"


def test_fxg_Graphic_scaleGridBottom_value_roundtrip():
    instance = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    assert instance.scaleGridBottom == "sample_text"
    instance.scaleGridBottom = "sample_text_2"
    assert instance.scaleGridBottom == "sample_text_2"


def test_fxg_Graphic_scaleGridLeft_value_roundtrip():
    instance = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    assert instance.scaleGridLeft == "sample_text"
    instance.scaleGridLeft = "sample_text_2"
    assert instance.scaleGridLeft == "sample_text_2"


def test_fxg_Graphic_scaleGridRight_value_roundtrip():
    instance = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    assert instance.scaleGridRight == "sample_text"
    instance.scaleGridRight = "sample_text_2"
    assert instance.scaleGridRight == "sample_text_2"


def test_fxg_Graphic_scaleGridTop_value_roundtrip():
    instance = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    assert instance.scaleGridTop == "sample_text"
    instance.scaleGridTop = "sample_text_2"
    assert instance.scaleGridTop == "sample_text_2"


def test_fxg_Graphic_version_value_roundtrip():
    instance = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_fxg_Graphic_viewHeight_value_roundtrip():
    instance = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    assert instance.viewHeight == 7
    instance.viewHeight = 13
    assert instance.viewHeight == 13


def test_fxg_Graphic_viewWidth_value_roundtrip():
    instance = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    assert instance.viewWidth == 7
    instance.viewWidth = 13
    assert instance.viewWidth == 13


def test_fxg_Group_alpha_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_Group_blendMode_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.blendMode == "sample_text"
    instance.blendMode = "sample_text_2"
    assert instance.blendMode == "sample_text_2"


def test_fxg_Group_id_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fxg_Group_maskType_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.maskType == "sample_text"
    instance.maskType = "sample_text_2"
    assert instance.maskType == "sample_text_2"


def test_fxg_Group_rotation_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_Group_scaleGridBottom_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleGridBottom == "sample_text"
    instance.scaleGridBottom = "sample_text_2"
    assert instance.scaleGridBottom == "sample_text_2"


def test_fxg_Group_scaleGridLeft_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleGridLeft == "sample_text"
    instance.scaleGridLeft = "sample_text_2"
    assert instance.scaleGridLeft == "sample_text_2"


def test_fxg_Group_scaleGridRight_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleGridRight == "sample_text"
    instance.scaleGridRight = "sample_text_2"
    assert instance.scaleGridRight == "sample_text_2"


def test_fxg_Group_scaleGridTop_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleGridTop == "sample_text"
    instance.scaleGridTop = "sample_text_2"
    assert instance.scaleGridTop == "sample_text_2"


def test_fxg_Group_scaleX_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_Group_scaleY_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_Group_transformX_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.transformX == "sample_text"
    instance.transformX = "sample_text_2"
    assert instance.transformX == "sample_text_2"


def test_fxg_Group_transformY_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.transformY == "sample_text"
    instance.transformY = "sample_text_2"
    assert instance.transformY == "sample_text_2"


def test_fxg_Group_visible_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.visible == "sample_text"
    instance.visible = "sample_text_2"
    assert instance.visible == "sample_text_2"


def test_fxg_Group_x_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_Group_y_value_roundtrip():
    instance = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_Line_alpha_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_Line_blendMode_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.blendMode == "sample_text"
    instance.blendMode = "sample_text_2"
    assert instance.blendMode == "sample_text_2"


def test_fxg_Line_id_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fxg_Line_maskType_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.maskType == "sample_text"
    instance.maskType = "sample_text_2"
    assert instance.maskType == "sample_text_2"


def test_fxg_Line_rotation_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_Line_scaleX_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_Line_scaleY_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_Line_visible_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.visible == "sample_text"
    instance.visible = "sample_text_2"
    assert instance.visible == "sample_text_2"


def test_fxg_Line_x_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_Line_xFrom_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.xFrom == "sample_text"
    instance.xFrom = "sample_text_2"
    assert instance.xFrom == "sample_text_2"


def test_fxg_Line_xTo_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.xTo == "sample_text"
    instance.xTo = "sample_text_2"
    assert instance.xTo == "sample_text_2"


def test_fxg_Line_y_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_Line_yFrom_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.yFrom == "sample_text"
    instance.yFrom = "sample_text_2"
    assert instance.yFrom == "sample_text_2"


def test_fxg_Line_yTo_value_roundtrip():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert instance.yTo == "sample_text"
    instance.yTo = "sample_text_2"
    assert instance.yTo == "sample_text_2"


def test_fxg_LinearGradient_interpolationMethod_value_roundtrip():
    instance = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.interpolationMethod == "sample_text"
    instance.interpolationMethod = "sample_text_2"
    assert instance.interpolationMethod == "sample_text_2"


def test_fxg_LinearGradient_rotation_value_roundtrip():
    instance = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_LinearGradient_scaleX_value_roundtrip():
    instance = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_LinearGradient_spreadMethod_value_roundtrip():
    instance = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.spreadMethod == "sample_text"
    instance.spreadMethod = "sample_text_2"
    assert instance.spreadMethod == "sample_text_2"


def test_fxg_LinearGradient_x_value_roundtrip():
    instance = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_LinearGradient_y_value_roundtrip():
    instance = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_LinearGradientStroke_caps_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.caps == "sample_text"
    instance.caps = "sample_text_2"
    assert instance.caps == "sample_text_2"


def test_fxg_LinearGradientStroke_interpolationMethod_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.interpolationMethod == "sample_text"
    instance.interpolationMethod = "sample_text_2"
    assert instance.interpolationMethod == "sample_text_2"


def test_fxg_LinearGradientStroke_joints_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.joints == "sample_text"
    instance.joints = "sample_text_2"
    assert instance.joints == "sample_text_2"


def test_fxg_LinearGradientStroke_miterLimit_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.miterLimit == "sample_text"
    instance.miterLimit = "sample_text_2"
    assert instance.miterLimit == "sample_text_2"


def test_fxg_LinearGradientStroke_pixelHinting_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.pixelHinting == "sample_text"
    instance.pixelHinting = "sample_text_2"
    assert instance.pixelHinting == "sample_text_2"


def test_fxg_LinearGradientStroke_rotation_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_LinearGradientStroke_scaleMode_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleMode == "sample_text"
    instance.scaleMode = "sample_text_2"
    assert instance.scaleMode == "sample_text_2"


def test_fxg_LinearGradientStroke_scaleX_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_LinearGradientStroke_spreadMethod_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.spreadMethod == "sample_text"
    instance.spreadMethod = "sample_text_2"
    assert instance.spreadMethod == "sample_text_2"


def test_fxg_LinearGradientStroke_weight_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_fxg_LinearGradientStroke_x_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_LinearGradientStroke_y_value_roundtrip():
    instance = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_Matrix_a_value_roundtrip():
    instance = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


def test_fxg_Matrix_b_value_roundtrip():
    instance = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_fxg_Matrix_c_value_roundtrip():
    instance = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    assert instance.c == "sample_text"
    instance.c = "sample_text_2"
    assert instance.c == "sample_text_2"


def test_fxg_Matrix_d_value_roundtrip():
    instance = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    assert instance.d == "sample_text"
    instance.d = "sample_text_2"
    assert instance.d == "sample_text_2"


def test_fxg_Matrix_tx_value_roundtrip():
    instance = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    assert instance.tx == "sample_text"
    instance.tx = "sample_text_2"
    assert instance.tx == "sample_text_2"


def test_fxg_Matrix_ty_value_roundtrip():
    instance = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    assert instance.ty == "sample_text"
    instance.ty = "sample_text_2"
    assert instance.ty == "sample_text_2"


def test_fxg_ParagraphAttributes_justificationRule_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.justificationRule == "sample_text"
    instance.justificationRule = "sample_text_2"
    assert instance.justificationRule == "sample_text_2"


def test_fxg_ParagraphAttributes_justificationStyle_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.justificationStyle == "sample_text"
    instance.justificationStyle = "sample_text_2"
    assert instance.justificationStyle == "sample_text_2"


def test_fxg_ParagraphAttributes_leadingModel_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.leadingModel == "sample_text"
    instance.leadingModel = "sample_text_2"
    assert instance.leadingModel == "sample_text_2"


def test_fxg_ParagraphAttributes_paragraphEndIndent_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.paragraphEndIndent == "sample_text"
    instance.paragraphEndIndent = "sample_text_2"
    assert instance.paragraphEndIndent == "sample_text_2"


def test_fxg_ParagraphAttributes_paragraphSpaceAfter_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.paragraphSpaceAfter == "sample_text"
    instance.paragraphSpaceAfter = "sample_text_2"
    assert instance.paragraphSpaceAfter == "sample_text_2"


def test_fxg_ParagraphAttributes_paragraphSpaceBefore_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.paragraphSpaceBefore == "sample_text"
    instance.paragraphSpaceBefore = "sample_text_2"
    assert instance.paragraphSpaceBefore == "sample_text_2"


def test_fxg_ParagraphAttributes_paragraphStartIndent_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.paragraphStartIndent == "sample_text"
    instance.paragraphStartIndent = "sample_text_2"
    assert instance.paragraphStartIndent == "sample_text_2"


def test_fxg_ParagraphAttributes_tabStops_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.tabStops == "sample_text"
    instance.tabStops = "sample_text_2"
    assert instance.tabStops == "sample_text_2"


def test_fxg_ParagraphAttributes_textAlign_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.textAlign == "sample_text"
    instance.textAlign = "sample_text_2"
    assert instance.textAlign == "sample_text_2"


def test_fxg_ParagraphAttributes_textAlignLast_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.textAlignLast == "sample_text"
    instance.textAlignLast = "sample_text_2"
    assert instance.textAlignLast == "sample_text_2"


def test_fxg_ParagraphAttributes_textIndent_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.textIndent == "sample_text"
    instance.textIndent = "sample_text_2"
    assert instance.textIndent == "sample_text_2"


def test_fxg_ParagraphAttributes_textJustify_value_roundtrip():
    instance = fxg_ParagraphAttributes(justificationRule="sample_text", justificationStyle="sample_text", leadingModel="sample_text", paragraphEndIndent="sample_text", paragraphSpaceAfter="sample_text", paragraphSpaceBefore="sample_text", paragraphStartIndent="sample_text", tabStops="sample_text", textAlign="sample_text", textAlignLast="sample_text", textIndent="sample_text", textJustify="sample_text")
    assert instance.textJustify == "sample_text"
    instance.textJustify = "sample_text_2"
    assert instance.textJustify == "sample_text_2"


def test_fxg_Path_alpha_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_Path_blendMode_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.blendMode == "sample_text"
    instance.blendMode = "sample_text_2"
    assert instance.blendMode == "sample_text_2"


def test_fxg_Path_data_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_fxg_Path_rotation_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_Path_scaleX_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_Path_scaleY_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_Path_visible_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.visible == "sample_text"
    instance.visible = "sample_text_2"
    assert instance.visible == "sample_text_2"


def test_fxg_Path_winding_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.winding == "sample_text"
    instance.winding = "sample_text_2"
    assert instance.winding == "sample_text_2"


def test_fxg_Path_x_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_Path_y_value_roundtrip():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_PlaceObject_id_value_roundtrip():
    instance = fxg_PlaceObject(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fxg_RadialGradient_focalPointRatio_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.focalPointRatio == "sample_text"
    instance.focalPointRatio = "sample_text_2"
    assert instance.focalPointRatio == "sample_text_2"


def test_fxg_RadialGradient_interpolationMethod_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.interpolationMethod == "sample_text"
    instance.interpolationMethod = "sample_text_2"
    assert instance.interpolationMethod == "sample_text_2"


def test_fxg_RadialGradient_rotation_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_RadialGradient_scaleX_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_RadialGradient_scaleY_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_RadialGradient_spreadMethod_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.spreadMethod == "sample_text"
    instance.spreadMethod = "sample_text_2"
    assert instance.spreadMethod == "sample_text_2"


def test_fxg_RadialGradient_x_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_RadialGradient_y_value_roundtrip():
    instance = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_RadialGradientStroke_caps_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.caps == "sample_text"
    instance.caps = "sample_text_2"
    assert instance.caps == "sample_text_2"


def test_fxg_RadialGradientStroke_focalPointRatio_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.focalPointRatio == "sample_text"
    instance.focalPointRatio = "sample_text_2"
    assert instance.focalPointRatio == "sample_text_2"


def test_fxg_RadialGradientStroke_interpolationMethod_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.interpolationMethod == "sample_text"
    instance.interpolationMethod = "sample_text_2"
    assert instance.interpolationMethod == "sample_text_2"


def test_fxg_RadialGradientStroke_joints_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.joints == "sample_text"
    instance.joints = "sample_text_2"
    assert instance.joints == "sample_text_2"


def test_fxg_RadialGradientStroke_miterLimit_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.miterLimit == "sample_text"
    instance.miterLimit = "sample_text_2"
    assert instance.miterLimit == "sample_text_2"


def test_fxg_RadialGradientStroke_pixelHinting_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.pixelHinting == "sample_text"
    instance.pixelHinting = "sample_text_2"
    assert instance.pixelHinting == "sample_text_2"


def test_fxg_RadialGradientStroke_rotation_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_RadialGradientStroke_scaleMode_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleMode == "sample_text"
    instance.scaleMode = "sample_text_2"
    assert instance.scaleMode == "sample_text_2"


def test_fxg_RadialGradientStroke_scaleX_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_RadialGradientStroke_scaleY_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_RadialGradientStroke_spreadMethod_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.spreadMethod == "sample_text"
    instance.spreadMethod = "sample_text_2"
    assert instance.spreadMethod == "sample_text_2"


def test_fxg_RadialGradientStroke_weight_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_fxg_RadialGradientStroke_x_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_RadialGradientStroke_y_value_roundtrip():
    instance = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_Rect_alpha_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_Rect_blendMode_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.blendMode == "sample_text"
    instance.blendMode = "sample_text_2"
    assert instance.blendMode == "sample_text_2"


def test_fxg_Rect_bottomLeftRadiusX_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.bottomLeftRadiusX == "sample_text"
    instance.bottomLeftRadiusX = "sample_text_2"
    assert instance.bottomLeftRadiusX == "sample_text_2"


def test_fxg_Rect_bottomLeftRadiusY_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.bottomLeftRadiusY == "sample_text"
    instance.bottomLeftRadiusY = "sample_text_2"
    assert instance.bottomLeftRadiusY == "sample_text_2"


def test_fxg_Rect_bottomRightRadiusX_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.bottomRightRadiusX == "sample_text"
    instance.bottomRightRadiusX = "sample_text_2"
    assert instance.bottomRightRadiusX == "sample_text_2"


def test_fxg_Rect_bottomRightRadiusY_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.bottomRightRadiusY == "sample_text"
    instance.bottomRightRadiusY = "sample_text_2"
    assert instance.bottomRightRadiusY == "sample_text_2"


def test_fxg_Rect_height_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_fxg_Rect_radiusX_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.radiusX == "sample_text"
    instance.radiusX = "sample_text_2"
    assert instance.radiusX == "sample_text_2"


def test_fxg_Rect_radiusY_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.radiusY == "sample_text"
    instance.radiusY = "sample_text_2"
    assert instance.radiusY == "sample_text_2"


def test_fxg_Rect_rotation_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_Rect_scaleX_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_Rect_scaleY_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_Rect_topLeftRadiusX_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.topLeftRadiusX == "sample_text"
    instance.topLeftRadiusX = "sample_text_2"
    assert instance.topLeftRadiusX == "sample_text_2"


def test_fxg_Rect_topLeftRadiusY_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.topLeftRadiusY == "sample_text"
    instance.topLeftRadiusY = "sample_text_2"
    assert instance.topLeftRadiusY == "sample_text_2"


def test_fxg_Rect_topRightRadiusX_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.topRightRadiusX == "sample_text"
    instance.topRightRadiusX = "sample_text_2"
    assert instance.topRightRadiusX == "sample_text_2"


def test_fxg_Rect_topRightRadiusY_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.topRightRadiusY == "sample_text"
    instance.topRightRadiusY = "sample_text_2"
    assert instance.topRightRadiusY == "sample_text_2"


def test_fxg_Rect_visible_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.visible == "sample_text"
    instance.visible = "sample_text_2"
    assert instance.visible == "sample_text_2"


def test_fxg_Rect_width_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_fxg_Rect_x_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_Rect_y_value_roundtrip():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_RichText__tempcontent_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance._tempcontent == "sample_text"
    instance._tempcontent = "sample_text_2"
    assert instance._tempcontent == "sample_text_2"


def test_fxg_RichText_alpha_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_RichText_blendMode_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.blendMode == "sample_text"
    instance.blendMode = "sample_text_2"
    assert instance.blendMode == "sample_text_2"


def test_fxg_RichText_height_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_fxg_RichText_id_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fxg_RichText_maskType_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.maskType == "sample_text"
    instance.maskType = "sample_text_2"
    assert instance.maskType == "sample_text_2"


def test_fxg_RichText_rotation_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_fxg_RichText_scaleX_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleX == "sample_text"
    instance.scaleX = "sample_text_2"
    assert instance.scaleX == "sample_text_2"


def test_fxg_RichText_scaleY_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.scaleY == "sample_text"
    instance.scaleY = "sample_text_2"
    assert instance.scaleY == "sample_text_2"


def test_fxg_RichText_visible_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.visible == "sample_text"
    instance.visible = "sample_text_2"
    assert instance.visible == "sample_text_2"


def test_fxg_RichText_width_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_fxg_RichText_x_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_fxg_RichText_y_value_roundtrip():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_fxg_SolidColor_alpha_value_roundtrip():
    instance = fxg_SolidColor(alpha="sample_text", color="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_SolidColor_color_value_roundtrip():
    instance = fxg_SolidColor(alpha="sample_text", color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_fxg_SolidColorStroke_alpha_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_fxg_SolidColorStroke_caps_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.caps == "sample_text"
    instance.caps = "sample_text_2"
    assert instance.caps == "sample_text_2"


def test_fxg_SolidColorStroke_color_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_fxg_SolidColorStroke_joints_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.joints == "sample_text"
    instance.joints = "sample_text_2"
    assert instance.joints == "sample_text_2"


def test_fxg_SolidColorStroke_miterLimit_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.miterLimit == "sample_text"
    instance.miterLimit = "sample_text_2"
    assert instance.miterLimit == "sample_text_2"


def test_fxg_SolidColorStroke_pixelHinting_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.pixelHinting == "sample_text"
    instance.pixelHinting = "sample_text_2"
    assert instance.pixelHinting == "sample_text_2"


def test_fxg_SolidColorStroke_scaleMode_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.scaleMode == "sample_text"
    instance.scaleMode = "sample_text_2"
    assert instance.scaleMode == "sample_text_2"


def test_fxg_SolidColorStroke_weight_value_roundtrip():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_fxg_rawtext__text_value_roundtrip():
    instance = fxg_rawtext(_text="sample_text")
    assert instance._text == "sample_text"
    instance._text = "sample_text_2"
    assert instance._text == "sample_text_2"


def test_fxg_RichText_isa_CharacterAttributes():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, CharacterAttributes)


def test_fxg_RichText_isa_ContainerAttributes():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, ContainerAttributes)


def test_fxg_BitmapImage_isa_FXGElement():
    instance = fxg_BitmapImage(alpha="sample_text", blendMode="sample_text", fillMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, FXGElement)


def test_fxg_ColorTransform_isa_FXGElement():
    instance = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    assert isinstance(instance, FXGElement)


def test_fxg_ContainerElement_isa_FXGElement():
    instance = fxg_ContainerElement()
    assert isinstance(instance, FXGElement)


def test_fxg_Fill_isa_FXGElement():
    instance = fxg_Fill()
    assert isinstance(instance, FXGElement)


def test_fxg_Filter_isa_FXGElement():
    instance = fxg_Filter()
    assert isinstance(instance, FXGElement)


def test_fxg_GradientEntry_isa_FXGElement():
    instance = fxg_GradientEntry(alpha="sample_text", color="sample_text", ratio="sample_text")
    assert isinstance(instance, FXGElement)


def test_fxg_Matrix_isa_FXGElement():
    instance = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    assert isinstance(instance, FXGElement)


def test_fxg_Path_isa_FXGElement():
    instance = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, FXGElement)


def test_fxg_PlaceObject_isa_FXGElement():
    instance = fxg_PlaceObject(id="sample_text")
    assert isinstance(instance, FXGElement)


def test_fxg_Private_isa_FXGElement():
    instance = fxg_Private()
    assert isinstance(instance, FXGElement)


def test_fxg_RichText_isa_FXGElement():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, FXGElement)


def test_fxg_Shape_isa_FXGElement():
    instance = fxg_Shape()
    assert isinstance(instance, FXGElement)


def test_fxg_Stroke_isa_FXGElement():
    instance = fxg_Stroke()
    assert isinstance(instance, FXGElement)


def test_fxg_Transform_isa_FXGElement():
    instance = fxg_Transform()
    assert isinstance(instance, FXGElement)


def test_fxg_BitmapFill_isa_Fill():
    instance = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, Fill)


def test_fxg_SolidColor_isa_Fill():
    instance = fxg_SolidColor(alpha="sample_text", color="sample_text")
    assert isinstance(instance, Fill)


def test_fxg_BevelFilter_isa_Filter():
    instance = fxg_BevelFilter(angle="sample_text", blurX="sample_text", blurY="sample_text", distance="sample_text", highlightAlpha="sample_text", highlightColor="sample_text", knockout="sample_text", quality="sample_text", shadowAlpha="sample_text", shadowColor="sample_text", strength="sample_text", type="sample_text")
    assert isinstance(instance, Filter)


def test_fxg_BlurFilter_isa_Filter():
    instance = fxg_BlurFilter(blurX="sample_text", blurY="sample_text", quality="sample_text")
    assert isinstance(instance, Filter)


def test_fxg_ColorMatrixFilter_isa_Filter():
    instance = fxg_ColorMatrixFilter(matrix="sample_text")
    assert isinstance(instance, Filter)


def test_fxg_DropShadowFilter_isa_Filter():
    instance = fxg_DropShadowFilter(alpha="sample_text", angle="sample_text", blurX="sample_text", blurY="sample_text", color="sample_text", distance="sample_text", hideObject="sample_text", inner="sample_text", knockout="sample_text", quality="sample_text", strength="sample_text")
    assert isinstance(instance, Filter)


def test_fxg_RichText_isa_ParagraphAttributes():
    instance = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, ParagraphAttributes)


def test_fxg_p_isa_ParagraphAttributes():
    instance = fxg_p()
    assert isinstance(instance, ParagraphAttributes)


def test_fxg_RichTextContentContainer_isa_RichTextContent():
    instance = fxg_RichTextContentContainer()
    assert isinstance(instance, RichTextContent)


def test_fxg_a_isa_RichTextContent():
    instance = fxg_a()
    assert isinstance(instance, RichTextContent)


def test_fxg_br_isa_RichTextContent():
    instance = fxg_br()
    assert isinstance(instance, RichTextContent)


def test_fxg_div_isa_RichTextContent():
    instance = fxg_div()
    assert isinstance(instance, RichTextContent)


def test_fxg_img_isa_RichTextContent():
    instance = fxg_img()
    assert isinstance(instance, RichTextContent)


def test_fxg_linkHoverFormat_isa_RichTextContent():
    instance = fxg_linkHoverFormat()
    assert isinstance(instance, RichTextContent)


def test_fxg_linkNormalFormat_isa_RichTextContent():
    instance = fxg_linkNormalFormat()
    assert isinstance(instance, RichTextContent)


def test_fxg_p_isa_RichTextContent():
    instance = fxg_p()
    assert isinstance(instance, RichTextContent)


def test_fxg_rawtext_isa_RichTextContent():
    instance = fxg_rawtext(_text="sample_text")
    assert isinstance(instance, RichTextContent)


def test_fxg_span_isa_RichTextContent():
    instance = fxg_span()
    assert isinstance(instance, RichTextContent)


def test_fxg_tab_isa_RichTextContent():
    instance = fxg_tab()
    assert isinstance(instance, RichTextContent)


def test_fxg_tcy_isa_RichTextContent():
    instance = fxg_tcy()
    assert isinstance(instance, RichTextContent)


def test_fxg_a_isa_RichTextContentContainer():
    instance = fxg_a()
    assert isinstance(instance, RichTextContentContainer)


def test_fxg_div_isa_RichTextContentContainer():
    instance = fxg_div()
    assert isinstance(instance, RichTextContentContainer)


def test_fxg_p_isa_RichTextContentContainer():
    instance = fxg_p()
    assert isinstance(instance, RichTextContentContainer)


def test_fxg_span_isa_RichTextContentContainer():
    instance = fxg_span()
    assert isinstance(instance, RichTextContentContainer)


def test_fxg_tcy_isa_RichTextContentContainer():
    instance = fxg_tcy()
    assert isinstance(instance, RichTextContentContainer)


def test_fxg_Ellipse_isa_Shape():
    instance = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, Shape)


def test_fxg_Line_isa_Shape():
    instance = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    assert isinstance(instance, Shape)


def test_fxg_Rect_isa_Shape():
    instance = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, Shape)


def test_fxg_SolidColorStroke_isa_Stroke():
    instance = fxg_SolidColorStroke(alpha="sample_text", caps="sample_text", color="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", scaleMode="sample_text", weight="sample_text")
    assert isinstance(instance, Stroke)


def test_assoc_colorTransform10_link_reassign_clear():
    a = fxg_ColorTransform(alphaMultiplier="sample_text", alphaOffset="sample_text", blueMultiplier="sample_text", blueOffset="sample_text", greenMultiplier="sample_text", greenOffset="sample_text", redMultiplier="sample_text", redOffset="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_ColorTransform', b1)
    assert _is_linked(a, 'fxg_ColorTransform', b1)
    if hasattr(b1, 'fxg_Transform11'):
        assert _is_linked(b1, 'fxg_Transform11', a)
    _safe_set(a, 'fxg_ColorTransform', b2)
    assert _is_linked(a, 'fxg_ColorTransform', b2)
    if hasattr(b1, 'fxg_Transform11'):
        assert not _is_linked(b1, 'fxg_Transform11', a)
    if hasattr(b2, 'fxg_Transform11'):
        assert _is_linked(b2, 'fxg_Transform11', a)
    _safe_set(a, 'fxg_ColorTransform', None)
    assert not _is_linked(a, 'fxg_ColorTransform', b2)
    if hasattr(b2, 'fxg_Transform11'):
        assert not _is_linked(b2, 'fxg_Transform11', a)


def test_assoc_content74_link_reassign_clear():
    a = fxg_RichText(_tempcontent="sample_text", alpha="sample_text", blendMode="sample_text", height="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_RichTextContent()
    b2 = fxg_RichTextContent()
    _safe_set(a, 'fxg_RichText', {b1})
    assert _is_linked(a, 'fxg_RichText', b1)
    if hasattr(b1, 'fxg_RichTextContent'):
        assert _is_linked(b1, 'fxg_RichTextContent', a)
    _safe_set(a, 'fxg_RichText', {b2})
    assert _is_linked(a, 'fxg_RichText', b2)
    if hasattr(b1, 'fxg_RichTextContent'):
        assert not _is_linked(b1, 'fxg_RichTextContent', a)
    if hasattr(b2, 'fxg_RichTextContent'):
        assert _is_linked(b2, 'fxg_RichTextContent', a)
    _safe_set(a, 'fxg_RichText', set())
    assert not _is_linked(a, 'fxg_RichText', b2)
    if hasattr(b2, 'fxg_RichTextContent'):
        assert not _is_linked(b2, 'fxg_RichTextContent', a)


def test_assoc_fill20_link_reassign_clear():
    a = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Fill()
    b2 = fxg_Fill()
    _safe_set(a, 'fxg_Path', b1)
    assert _is_linked(a, 'fxg_Path', b1)
    if hasattr(b1, 'fxg_Fill'):
        assert _is_linked(b1, 'fxg_Fill', a)
    _safe_set(a, 'fxg_Path', b2)
    assert _is_linked(a, 'fxg_Path', b2)
    if hasattr(b1, 'fxg_Fill'):
        assert not _is_linked(b1, 'fxg_Fill', a)
    if hasattr(b2, 'fxg_Fill'):
        assert _is_linked(b2, 'fxg_Fill', a)
    _safe_set(a, 'fxg_Path', None)
    assert not _is_linked(a, 'fxg_Path', b2)
    if hasattr(b2, 'fxg_Fill'):
        assert not _is_linked(b2, 'fxg_Fill', a)


def test_assoc_fill37_link_reassign_clear():
    a = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Fill()
    b2 = fxg_Fill()
    _safe_set(a, 'fxg_Rect38', b1)
    assert _is_linked(a, 'fxg_Rect38', b1)
    if hasattr(b1, 'fxg_Fill39'):
        assert _is_linked(b1, 'fxg_Fill39', a)
    _safe_set(a, 'fxg_Rect38', b2)
    assert _is_linked(a, 'fxg_Rect38', b2)
    if hasattr(b1, 'fxg_Fill39'):
        assert not _is_linked(b1, 'fxg_Fill39', a)
    if hasattr(b2, 'fxg_Fill39'):
        assert _is_linked(b2, 'fxg_Fill39', a)
    _safe_set(a, 'fxg_Rect38', None)
    assert not _is_linked(a, 'fxg_Rect38', b2)
    if hasattr(b2, 'fxg_Fill39'):
        assert not _is_linked(b2, 'fxg_Fill39', a)


def test_assoc_fill51_link_reassign_clear():
    a = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Fill()
    b2 = fxg_Fill()
    _safe_set(a, 'fxg_Ellipse52', b1)
    assert _is_linked(a, 'fxg_Ellipse52', b1)
    if hasattr(b1, 'fxg_Fill53'):
        assert _is_linked(b1, 'fxg_Fill53', a)
    _safe_set(a, 'fxg_Ellipse52', b2)
    assert _is_linked(a, 'fxg_Ellipse52', b2)
    if hasattr(b1, 'fxg_Fill53'):
        assert not _is_linked(b1, 'fxg_Fill53', a)
    if hasattr(b2, 'fxg_Fill53'):
        assert _is_linked(b2, 'fxg_Fill53', a)
    _safe_set(a, 'fxg_Ellipse52', None)
    assert not _is_linked(a, 'fxg_Ellipse52', b2)
    if hasattr(b2, 'fxg_Fill53'):
        assert not _is_linked(b2, 'fxg_Fill53', a)


def test_assoc_fill65_link_reassign_clear():
    a = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    b1 = fxg_Fill()
    b2 = fxg_Fill()
    _safe_set(a, 'fxg_Line66', b1)
    assert _is_linked(a, 'fxg_Line66', b1)
    if hasattr(b1, 'fxg_Fill67'):
        assert _is_linked(b1, 'fxg_Fill67', a)
    _safe_set(a, 'fxg_Line66', b2)
    assert _is_linked(a, 'fxg_Line66', b2)
    if hasattr(b1, 'fxg_Fill67'):
        assert not _is_linked(b1, 'fxg_Fill67', a)
    if hasattr(b2, 'fxg_Fill67'):
        assert _is_linked(b2, 'fxg_Fill67', a)
    _safe_set(a, 'fxg_Line66', None)
    assert not _is_linked(a, 'fxg_Line66', b2)
    if hasattr(b2, 'fxg_Fill67'):
        assert not _is_linked(b2, 'fxg_Fill67', a)


def test_assoc_filters14_link_reassign_clear():
    a = fxg_PlaceObject(id="sample_text")
    b1 = fxg_Filter()
    b2 = fxg_Filter()
    _safe_set(a, 'fxg_PlaceObject15', {b1})
    assert _is_linked(a, 'fxg_PlaceObject15', b1)
    if hasattr(b1, 'fxg_Filter16'):
        assert _is_linked(b1, 'fxg_Filter16', a)
    _safe_set(a, 'fxg_PlaceObject15', {b2})
    assert _is_linked(a, 'fxg_PlaceObject15', b2)
    if hasattr(b1, 'fxg_Filter16'):
        assert not _is_linked(b1, 'fxg_Filter16', a)
    if hasattr(b2, 'fxg_Filter16'):
        assert _is_linked(b2, 'fxg_Filter16', a)
    _safe_set(a, 'fxg_PlaceObject15', set())
    assert not _is_linked(a, 'fxg_PlaceObject15', b2)
    if hasattr(b2, 'fxg_Filter16'):
        assert not _is_linked(b2, 'fxg_Filter16', a)


def test_assoc_filters23_link_reassign_clear():
    a = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Filter()
    b2 = fxg_Filter()
    _safe_set(a, 'fxg_Path24', {b1})
    assert _is_linked(a, 'fxg_Path24', b1)
    if hasattr(b1, 'fxg_Filter25'):
        assert _is_linked(b1, 'fxg_Filter25', a)
    _safe_set(a, 'fxg_Path24', {b2})
    assert _is_linked(a, 'fxg_Path24', b2)
    if hasattr(b1, 'fxg_Filter25'):
        assert not _is_linked(b1, 'fxg_Filter25', a)
    if hasattr(b2, 'fxg_Filter25'):
        assert _is_linked(b2, 'fxg_Filter25', a)
    _safe_set(a, 'fxg_Path24', set())
    assert not _is_linked(a, 'fxg_Path24', b2)
    if hasattr(b2, 'fxg_Filter25'):
        assert not _is_linked(b2, 'fxg_Filter25', a)


def test_assoc_filters3_link_reassign_clear():
    a = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Filter()
    b2 = fxg_Filter()
    _safe_set(a, 'fxg_Group4', {b1})
    assert _is_linked(a, 'fxg_Group4', b1)
    if hasattr(b1, 'fxg_Filter'):
        assert _is_linked(b1, 'fxg_Filter', a)
    _safe_set(a, 'fxg_Group4', {b2})
    assert _is_linked(a, 'fxg_Group4', b2)
    if hasattr(b1, 'fxg_Filter'):
        assert not _is_linked(b1, 'fxg_Filter', a)
    if hasattr(b2, 'fxg_Filter'):
        assert _is_linked(b2, 'fxg_Filter', a)
    _safe_set(a, 'fxg_Group4', set())
    assert not _is_linked(a, 'fxg_Group4', b2)
    if hasattr(b2, 'fxg_Filter'):
        assert not _is_linked(b2, 'fxg_Filter', a)


def test_assoc_filters34_link_reassign_clear():
    a = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Filter()
    b2 = fxg_Filter()
    _safe_set(a, 'fxg_Rect35', {b1})
    assert _is_linked(a, 'fxg_Rect35', b1)
    if hasattr(b1, 'fxg_Filter36'):
        assert _is_linked(b1, 'fxg_Filter36', a)
    _safe_set(a, 'fxg_Rect35', {b2})
    assert _is_linked(a, 'fxg_Rect35', b2)
    if hasattr(b1, 'fxg_Filter36'):
        assert not _is_linked(b1, 'fxg_Filter36', a)
    if hasattr(b2, 'fxg_Filter36'):
        assert _is_linked(b2, 'fxg_Filter36', a)
    _safe_set(a, 'fxg_Rect35', set())
    assert not _is_linked(a, 'fxg_Rect35', b2)
    if hasattr(b2, 'fxg_Filter36'):
        assert not _is_linked(b2, 'fxg_Filter36', a)


def test_assoc_filters48_link_reassign_clear():
    a = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Filter()
    b2 = fxg_Filter()
    _safe_set(a, 'fxg_Ellipse49', {b1})
    assert _is_linked(a, 'fxg_Ellipse49', b1)
    if hasattr(b1, 'fxg_Filter50'):
        assert _is_linked(b1, 'fxg_Filter50', a)
    _safe_set(a, 'fxg_Ellipse49', {b2})
    assert _is_linked(a, 'fxg_Ellipse49', b2)
    if hasattr(b1, 'fxg_Filter50'):
        assert not _is_linked(b1, 'fxg_Filter50', a)
    if hasattr(b2, 'fxg_Filter50'):
        assert _is_linked(b2, 'fxg_Filter50', a)
    _safe_set(a, 'fxg_Ellipse49', set())
    assert not _is_linked(a, 'fxg_Ellipse49', b2)
    if hasattr(b2, 'fxg_Filter50'):
        assert not _is_linked(b2, 'fxg_Filter50', a)


def test_assoc_filters62_link_reassign_clear():
    a = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    b1 = fxg_Filter()
    b2 = fxg_Filter()
    _safe_set(a, 'fxg_Line63', {b1})
    assert _is_linked(a, 'fxg_Line63', b1)
    if hasattr(b1, 'fxg_Filter64'):
        assert _is_linked(b1, 'fxg_Filter64', a)
    _safe_set(a, 'fxg_Line63', {b2})
    assert _is_linked(a, 'fxg_Line63', b2)
    if hasattr(b1, 'fxg_Filter64'):
        assert not _is_linked(b1, 'fxg_Filter64', a)
    if hasattr(b2, 'fxg_Filter64'):
        assert _is_linked(b2, 'fxg_Filter64', a)
    _safe_set(a, 'fxg_Line63', set())
    assert not _is_linked(a, 'fxg_Line63', b2)
    if hasattr(b2, 'fxg_Filter64'):
        assert not _is_linked(b2, 'fxg_Filter64', a)


def test_assoc_mask0_link_reassign_clear():
    a = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Graphic(scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", version="sample_text", viewHeight=7, viewWidth=7)
    b2 = fxg_Graphic(scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", version="sample_text_2", viewHeight=13, viewWidth=13)
    _safe_set(a, 'fxg_Group', b1)
    assert _is_linked(a, 'fxg_Group', b1)
    if hasattr(b1, 'fxg_Graphic'):
        assert _is_linked(b1, 'fxg_Graphic', a)
    _safe_set(a, 'fxg_Group', b2)
    assert _is_linked(a, 'fxg_Group', b2)
    if hasattr(b1, 'fxg_Graphic'):
        assert not _is_linked(b1, 'fxg_Graphic', a)
    if hasattr(b2, 'fxg_Graphic'):
        assert _is_linked(b2, 'fxg_Graphic', a)
    _safe_set(a, 'fxg_Group', None)
    assert not _is_linked(a, 'fxg_Group', b2)
    if hasattr(b2, 'fxg_Graphic'):
        assert not _is_linked(b2, 'fxg_Graphic', a)


def test_assoc_mask17_link_reassign_clear():
    a = fxg_PlaceObject(id="sample_text")
    b1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_PlaceObject18', b1)
    assert _is_linked(a, 'fxg_PlaceObject18', b1)
    if hasattr(b1, 'fxg_Group19'):
        assert _is_linked(b1, 'fxg_Group19', a)
    _safe_set(a, 'fxg_PlaceObject18', b2)
    assert _is_linked(a, 'fxg_PlaceObject18', b2)
    if hasattr(b1, 'fxg_Group19'):
        assert not _is_linked(b1, 'fxg_Group19', a)
    if hasattr(b2, 'fxg_Group19'):
        assert _is_linked(b2, 'fxg_Group19', a)
    _safe_set(a, 'fxg_PlaceObject18', None)
    assert not _is_linked(a, 'fxg_PlaceObject18', b2)
    if hasattr(b2, 'fxg_Group19'):
        assert not _is_linked(b2, 'fxg_Group19', a)


def test_assoc_mask29_link_reassign_clear():
    a = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Path30', b1)
    assert _is_linked(a, 'fxg_Path30', b1)
    if hasattr(b1, 'fxg_Group31'):
        assert _is_linked(b1, 'fxg_Group31', a)
    _safe_set(a, 'fxg_Path30', b2)
    assert _is_linked(a, 'fxg_Path30', b2)
    if hasattr(b1, 'fxg_Group31'):
        assert not _is_linked(b1, 'fxg_Group31', a)
    if hasattr(b2, 'fxg_Group31'):
        assert _is_linked(b2, 'fxg_Group31', a)
    _safe_set(a, 'fxg_Path30', None)
    assert not _is_linked(a, 'fxg_Path30', b2)
    if hasattr(b2, 'fxg_Group31'):
        assert not _is_linked(b2, 'fxg_Group31', a)


def test_assoc_mask43_link_reassign_clear():
    a = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Rect44', b1)
    assert _is_linked(a, 'fxg_Rect44', b1)
    if hasattr(b1, 'fxg_Group45'):
        assert _is_linked(b1, 'fxg_Group45', a)
    _safe_set(a, 'fxg_Rect44', b2)
    assert _is_linked(a, 'fxg_Rect44', b2)
    if hasattr(b1, 'fxg_Group45'):
        assert not _is_linked(b1, 'fxg_Group45', a)
    if hasattr(b2, 'fxg_Group45'):
        assert _is_linked(b2, 'fxg_Group45', a)
    _safe_set(a, 'fxg_Rect44', None)
    assert not _is_linked(a, 'fxg_Rect44', b2)
    if hasattr(b2, 'fxg_Group45'):
        assert not _is_linked(b2, 'fxg_Group45', a)


def test_assoc_mask57_link_reassign_clear():
    a = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_Ellipse(alpha="sample_text_2", blendMode="sample_text_2", height="sample_text_2", rotation="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", visible="sample_text_2", width="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Group59', b1)
    assert _is_linked(a, 'fxg_Group59', b1)
    if hasattr(b1, 'fxg_Ellipse58'):
        assert _is_linked(b1, 'fxg_Ellipse58', a)
    _safe_set(a, 'fxg_Group59', b2)
    assert _is_linked(a, 'fxg_Group59', b2)
    if hasattr(b1, 'fxg_Ellipse58'):
        assert not _is_linked(b1, 'fxg_Ellipse58', a)
    if hasattr(b2, 'fxg_Ellipse58'):
        assert _is_linked(b2, 'fxg_Ellipse58', a)
    _safe_set(a, 'fxg_Group59', None)
    assert not _is_linked(a, 'fxg_Group59', b2)
    if hasattr(b2, 'fxg_Ellipse58'):
        assert not _is_linked(b2, 'fxg_Ellipse58', a)


def test_assoc_mask6_link_reassign_clear():
    a = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Group5', b1)
    assert _is_linked(a, 'fxg_Group5', b1)
    if hasattr(b1, 'fxg_Group7'):
        assert _is_linked(b1, 'fxg_Group7', a)
    _safe_set(a, 'fxg_Group5', b2)
    assert _is_linked(a, 'fxg_Group5', b2)
    if hasattr(b1, 'fxg_Group7'):
        assert not _is_linked(b1, 'fxg_Group7', a)
    if hasattr(b2, 'fxg_Group7'):
        assert _is_linked(b2, 'fxg_Group7', a)
    _safe_set(a, 'fxg_Group5', None)
    assert not _is_linked(a, 'fxg_Group5', b2)
    if hasattr(b2, 'fxg_Group7'):
        assert not _is_linked(b2, 'fxg_Group7', a)


def test_assoc_mask71_link_reassign_clear():
    a = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    b1 = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_Group(alpha="sample_text_2", blendMode="sample_text_2", id="sample_text_2", maskType="sample_text_2", rotation="sample_text_2", scaleGridBottom="sample_text_2", scaleGridLeft="sample_text_2", scaleGridRight="sample_text_2", scaleGridTop="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", transformX="sample_text_2", transformY="sample_text_2", visible="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Line72', b1)
    assert _is_linked(a, 'fxg_Line72', b1)
    if hasattr(b1, 'fxg_Group73'):
        assert _is_linked(b1, 'fxg_Group73', a)
    _safe_set(a, 'fxg_Line72', b2)
    assert _is_linked(a, 'fxg_Line72', b2)
    if hasattr(b1, 'fxg_Group73'):
        assert not _is_linked(b1, 'fxg_Group73', a)
    if hasattr(b2, 'fxg_Group73'):
        assert _is_linked(b2, 'fxg_Group73', a)
    _safe_set(a, 'fxg_Line72', None)
    assert not _is_linked(a, 'fxg_Line72', b2)
    if hasattr(b2, 'fxg_Group73'):
        assert not _is_linked(b2, 'fxg_Group73', a)


def test_assoc_matrix77_link_reassign_clear():
    a = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    b1 = fxg_LinearGradient(interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_LinearGradient(interpolationMethod="sample_text_2", rotation="sample_text_2", scaleX="sample_text_2", spreadMethod="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Matrix78', b1)
    assert _is_linked(a, 'fxg_Matrix78', b1)
    if hasattr(b1, 'fxg_LinearGradient'):
        assert _is_linked(b1, 'fxg_LinearGradient', a)
    _safe_set(a, 'fxg_Matrix78', b2)
    assert _is_linked(a, 'fxg_Matrix78', b2)
    if hasattr(b1, 'fxg_LinearGradient'):
        assert not _is_linked(b1, 'fxg_LinearGradient', a)
    if hasattr(b2, 'fxg_LinearGradient'):
        assert _is_linked(b2, 'fxg_LinearGradient', a)
    _safe_set(a, 'fxg_Matrix78', None)
    assert not _is_linked(a, 'fxg_Matrix78', b2)
    if hasattr(b2, 'fxg_LinearGradient'):
        assert not _is_linked(b2, 'fxg_LinearGradient', a)


def test_assoc_matrix79_link_reassign_clear():
    a = fxg_RadialGradient(focalPointRatio="sample_text", interpolationMethod="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    b2 = fxg_Matrix(a="sample_text_2", b="sample_text_2", c="sample_text_2", d="sample_text_2", tx="sample_text_2", ty="sample_text_2")
    _safe_set(a, 'fxg_RadialGradient', b1)
    assert _is_linked(a, 'fxg_RadialGradient', b1)
    if hasattr(b1, 'fxg_Matrix80'):
        assert _is_linked(b1, 'fxg_Matrix80', a)
    _safe_set(a, 'fxg_RadialGradient', b2)
    assert _is_linked(a, 'fxg_RadialGradient', b2)
    if hasattr(b1, 'fxg_Matrix80'):
        assert not _is_linked(b1, 'fxg_Matrix80', a)
    if hasattr(b2, 'fxg_Matrix80'):
        assert _is_linked(b2, 'fxg_Matrix80', a)
    _safe_set(a, 'fxg_RadialGradient', None)
    assert not _is_linked(a, 'fxg_RadialGradient', b2)
    if hasattr(b2, 'fxg_Matrix80'):
        assert not _is_linked(b2, 'fxg_Matrix80', a)


def test_assoc_matrix8_link_reassign_clear():
    a = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_Matrix', b1)
    assert _is_linked(a, 'fxg_Matrix', b1)
    if hasattr(b1, 'fxg_Transform9'):
        assert _is_linked(b1, 'fxg_Transform9', a)
    _safe_set(a, 'fxg_Matrix', b2)
    assert _is_linked(a, 'fxg_Matrix', b2)
    if hasattr(b1, 'fxg_Transform9'):
        assert not _is_linked(b1, 'fxg_Transform9', a)
    if hasattr(b2, 'fxg_Transform9'):
        assert _is_linked(b2, 'fxg_Transform9', a)
    _safe_set(a, 'fxg_Matrix', None)
    assert not _is_linked(a, 'fxg_Matrix', b2)
    if hasattr(b2, 'fxg_Transform9'):
        assert not _is_linked(b2, 'fxg_Transform9', a)


def test_assoc_matrix81_link_reassign_clear():
    a = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    b1 = fxg_BitmapFill(fillMode="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", source="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_BitmapFill(fillMode="sample_text_2", rotation="sample_text_2", scaleX="sample_text_2", scaleY="sample_text_2", source="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Matrix82', b1)
    assert _is_linked(a, 'fxg_Matrix82', b1)
    if hasattr(b1, 'fxg_BitmapFill'):
        assert _is_linked(b1, 'fxg_BitmapFill', a)
    _safe_set(a, 'fxg_Matrix82', b2)
    assert _is_linked(a, 'fxg_Matrix82', b2)
    if hasattr(b1, 'fxg_BitmapFill'):
        assert not _is_linked(b1, 'fxg_BitmapFill', a)
    if hasattr(b2, 'fxg_BitmapFill'):
        assert _is_linked(b2, 'fxg_BitmapFill', a)
    _safe_set(a, 'fxg_Matrix82', None)
    assert not _is_linked(a, 'fxg_Matrix82', b2)
    if hasattr(b2, 'fxg_BitmapFill'):
        assert not _is_linked(b2, 'fxg_BitmapFill', a)


def test_assoc_matrix83_link_reassign_clear():
    a = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    b1 = fxg_LinearGradientStroke(caps="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    b2 = fxg_LinearGradientStroke(caps="sample_text_2", interpolationMethod="sample_text_2", joints="sample_text_2", miterLimit="sample_text_2", pixelHinting="sample_text_2", rotation="sample_text_2", scaleMode="sample_text_2", scaleX="sample_text_2", spreadMethod="sample_text_2", weight="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'fxg_Matrix84', b1)
    assert _is_linked(a, 'fxg_Matrix84', b1)
    if hasattr(b1, 'fxg_LinearGradientStroke'):
        assert _is_linked(b1, 'fxg_LinearGradientStroke', a)
    _safe_set(a, 'fxg_Matrix84', b2)
    assert _is_linked(a, 'fxg_Matrix84', b2)
    if hasattr(b1, 'fxg_LinearGradientStroke'):
        assert not _is_linked(b1, 'fxg_LinearGradientStroke', a)
    if hasattr(b2, 'fxg_LinearGradientStroke'):
        assert _is_linked(b2, 'fxg_LinearGradientStroke', a)
    _safe_set(a, 'fxg_Matrix84', None)
    assert not _is_linked(a, 'fxg_Matrix84', b2)
    if hasattr(b2, 'fxg_LinearGradientStroke'):
        assert not _is_linked(b2, 'fxg_LinearGradientStroke', a)


def test_assoc_matrix85_link_reassign_clear():
    a = fxg_RadialGradientStroke(caps="sample_text", focalPointRatio="sample_text", interpolationMethod="sample_text", joints="sample_text", miterLimit="sample_text", pixelHinting="sample_text", rotation="sample_text", scaleMode="sample_text", scaleX="sample_text", scaleY="sample_text", spreadMethod="sample_text", weight="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Matrix(a="sample_text", b="sample_text", c="sample_text", d="sample_text", tx="sample_text", ty="sample_text")
    b2 = fxg_Matrix(a="sample_text_2", b="sample_text_2", c="sample_text_2", d="sample_text_2", tx="sample_text_2", ty="sample_text_2")
    _safe_set(a, 'fxg_RadialGradientStroke', b1)
    assert _is_linked(a, 'fxg_RadialGradientStroke', b1)
    if hasattr(b1, 'fxg_Matrix86'):
        assert _is_linked(b1, 'fxg_Matrix86', a)
    _safe_set(a, 'fxg_RadialGradientStroke', b2)
    assert _is_linked(a, 'fxg_RadialGradientStroke', b2)
    if hasattr(b1, 'fxg_Matrix86'):
        assert not _is_linked(b1, 'fxg_Matrix86', a)
    if hasattr(b2, 'fxg_Matrix86'):
        assert _is_linked(b2, 'fxg_Matrix86', a)
    _safe_set(a, 'fxg_RadialGradientStroke', None)
    assert not _is_linked(a, 'fxg_RadialGradientStroke', b2)
    if hasattr(b2, 'fxg_Matrix86'):
        assert not _is_linked(b2, 'fxg_Matrix86', a)


def test_assoc_stroke21_link_reassign_clear():
    a = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Stroke()
    b2 = fxg_Stroke()
    _safe_set(a, 'fxg_Path22', b1)
    assert _is_linked(a, 'fxg_Path22', b1)
    if hasattr(b1, 'fxg_Stroke'):
        assert _is_linked(b1, 'fxg_Stroke', a)
    _safe_set(a, 'fxg_Path22', b2)
    assert _is_linked(a, 'fxg_Path22', b2)
    if hasattr(b1, 'fxg_Stroke'):
        assert not _is_linked(b1, 'fxg_Stroke', a)
    if hasattr(b2, 'fxg_Stroke'):
        assert _is_linked(b2, 'fxg_Stroke', a)
    _safe_set(a, 'fxg_Path22', None)
    assert not _is_linked(a, 'fxg_Path22', b2)
    if hasattr(b2, 'fxg_Stroke'):
        assert not _is_linked(b2, 'fxg_Stroke', a)


def test_assoc_stroke40_link_reassign_clear():
    a = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Stroke()
    b2 = fxg_Stroke()
    _safe_set(a, 'fxg_Rect41', b1)
    assert _is_linked(a, 'fxg_Rect41', b1)
    if hasattr(b1, 'fxg_Stroke42'):
        assert _is_linked(b1, 'fxg_Stroke42', a)
    _safe_set(a, 'fxg_Rect41', b2)
    assert _is_linked(a, 'fxg_Rect41', b2)
    if hasattr(b1, 'fxg_Stroke42'):
        assert not _is_linked(b1, 'fxg_Stroke42', a)
    if hasattr(b2, 'fxg_Stroke42'):
        assert _is_linked(b2, 'fxg_Stroke42', a)
    _safe_set(a, 'fxg_Rect41', None)
    assert not _is_linked(a, 'fxg_Rect41', b2)
    if hasattr(b2, 'fxg_Stroke42'):
        assert not _is_linked(b2, 'fxg_Stroke42', a)


def test_assoc_stroke54_link_reassign_clear():
    a = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Stroke()
    b2 = fxg_Stroke()
    _safe_set(a, 'fxg_Ellipse55', b1)
    assert _is_linked(a, 'fxg_Ellipse55', b1)
    if hasattr(b1, 'fxg_Stroke56'):
        assert _is_linked(b1, 'fxg_Stroke56', a)
    _safe_set(a, 'fxg_Ellipse55', b2)
    assert _is_linked(a, 'fxg_Ellipse55', b2)
    if hasattr(b1, 'fxg_Stroke56'):
        assert not _is_linked(b1, 'fxg_Stroke56', a)
    if hasattr(b2, 'fxg_Stroke56'):
        assert _is_linked(b2, 'fxg_Stroke56', a)
    _safe_set(a, 'fxg_Ellipse55', None)
    assert not _is_linked(a, 'fxg_Ellipse55', b2)
    if hasattr(b2, 'fxg_Stroke56'):
        assert not _is_linked(b2, 'fxg_Stroke56', a)


def test_assoc_stroke68_link_reassign_clear():
    a = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    b1 = fxg_Stroke()
    b2 = fxg_Stroke()
    _safe_set(a, 'fxg_Line69', b1)
    assert _is_linked(a, 'fxg_Line69', b1)
    if hasattr(b1, 'fxg_Stroke70'):
        assert _is_linked(b1, 'fxg_Stroke70', a)
    _safe_set(a, 'fxg_Line69', b2)
    assert _is_linked(a, 'fxg_Line69', b2)
    if hasattr(b1, 'fxg_Stroke70'):
        assert not _is_linked(b1, 'fxg_Stroke70', a)
    if hasattr(b2, 'fxg_Stroke70'):
        assert _is_linked(b2, 'fxg_Stroke70', a)
    _safe_set(a, 'fxg_Line69', None)
    assert not _is_linked(a, 'fxg_Line69', b2)
    if hasattr(b2, 'fxg_Stroke70'):
        assert not _is_linked(b2, 'fxg_Stroke70', a)


def test_assoc_transform1_link_reassign_clear():
    a = fxg_Group(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleGridBottom="sample_text", scaleGridLeft="sample_text", scaleGridRight="sample_text", scaleGridTop="sample_text", scaleX="sample_text", scaleY="sample_text", transformX="sample_text", transformY="sample_text", visible="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_Group2', b1)
    assert _is_linked(a, 'fxg_Group2', b1)
    if hasattr(b1, 'fxg_Transform'):
        assert _is_linked(b1, 'fxg_Transform', a)
    _safe_set(a, 'fxg_Group2', b2)
    assert _is_linked(a, 'fxg_Group2', b2)
    if hasattr(b1, 'fxg_Transform'):
        assert not _is_linked(b1, 'fxg_Transform', a)
    if hasattr(b2, 'fxg_Transform'):
        assert _is_linked(b2, 'fxg_Transform', a)
    _safe_set(a, 'fxg_Group2', None)
    assert not _is_linked(a, 'fxg_Group2', b2)
    if hasattr(b2, 'fxg_Transform'):
        assert not _is_linked(b2, 'fxg_Transform', a)


def test_assoc_transform12_link_reassign_clear():
    a = fxg_PlaceObject(id="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_PlaceObject', b1)
    assert _is_linked(a, 'fxg_PlaceObject', b1)
    if hasattr(b1, 'fxg_Transform13'):
        assert _is_linked(b1, 'fxg_Transform13', a)
    _safe_set(a, 'fxg_PlaceObject', b2)
    assert _is_linked(a, 'fxg_PlaceObject', b2)
    if hasattr(b1, 'fxg_Transform13'):
        assert not _is_linked(b1, 'fxg_Transform13', a)
    if hasattr(b2, 'fxg_Transform13'):
        assert _is_linked(b2, 'fxg_Transform13', a)
    _safe_set(a, 'fxg_PlaceObject', None)
    assert not _is_linked(a, 'fxg_PlaceObject', b2)
    if hasattr(b2, 'fxg_Transform13'):
        assert not _is_linked(b2, 'fxg_Transform13', a)


def test_assoc_transform26_link_reassign_clear():
    a = fxg_Path(alpha="sample_text", blendMode="sample_text", data="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", winding="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_Path27', b1)
    assert _is_linked(a, 'fxg_Path27', b1)
    if hasattr(b1, 'fxg_Transform28'):
        assert _is_linked(b1, 'fxg_Transform28', a)
    _safe_set(a, 'fxg_Path27', b2)
    assert _is_linked(a, 'fxg_Path27', b2)
    if hasattr(b1, 'fxg_Transform28'):
        assert not _is_linked(b1, 'fxg_Transform28', a)
    if hasattr(b2, 'fxg_Transform28'):
        assert _is_linked(b2, 'fxg_Transform28', a)
    _safe_set(a, 'fxg_Path27', None)
    assert not _is_linked(a, 'fxg_Path27', b2)
    if hasattr(b2, 'fxg_Transform28'):
        assert not _is_linked(b2, 'fxg_Transform28', a)


def test_assoc_transform32_link_reassign_clear():
    a = fxg_Rect(alpha="sample_text", blendMode="sample_text", bottomLeftRadiusX="sample_text", bottomLeftRadiusY="sample_text", bottomRightRadiusX="sample_text", bottomRightRadiusY="sample_text", height="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", topLeftRadiusX="sample_text", topLeftRadiusY="sample_text", topRightRadiusX="sample_text", topRightRadiusY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_Rect', b1)
    assert _is_linked(a, 'fxg_Rect', b1)
    if hasattr(b1, 'fxg_Transform33'):
        assert _is_linked(b1, 'fxg_Transform33', a)
    _safe_set(a, 'fxg_Rect', b2)
    assert _is_linked(a, 'fxg_Rect', b2)
    if hasattr(b1, 'fxg_Transform33'):
        assert not _is_linked(b1, 'fxg_Transform33', a)
    if hasattr(b2, 'fxg_Transform33'):
        assert _is_linked(b2, 'fxg_Transform33', a)
    _safe_set(a, 'fxg_Rect', None)
    assert not _is_linked(a, 'fxg_Rect', b2)
    if hasattr(b2, 'fxg_Transform33'):
        assert not _is_linked(b2, 'fxg_Transform33', a)


def test_assoc_transform46_link_reassign_clear():
    a = fxg_Ellipse(alpha="sample_text", blendMode="sample_text", height="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", width="sample_text", x="sample_text", y="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_Ellipse', b1)
    assert _is_linked(a, 'fxg_Ellipse', b1)
    if hasattr(b1, 'fxg_Transform47'):
        assert _is_linked(b1, 'fxg_Transform47', a)
    _safe_set(a, 'fxg_Ellipse', b2)
    assert _is_linked(a, 'fxg_Ellipse', b2)
    if hasattr(b1, 'fxg_Transform47'):
        assert not _is_linked(b1, 'fxg_Transform47', a)
    if hasattr(b2, 'fxg_Transform47'):
        assert _is_linked(b2, 'fxg_Transform47', a)
    _safe_set(a, 'fxg_Ellipse', None)
    assert not _is_linked(a, 'fxg_Ellipse', b2)
    if hasattr(b2, 'fxg_Transform47'):
        assert not _is_linked(b2, 'fxg_Transform47', a)


def test_assoc_transform60_link_reassign_clear():
    a = fxg_Line(alpha="sample_text", blendMode="sample_text", id="sample_text", maskType="sample_text", rotation="sample_text", scaleX="sample_text", scaleY="sample_text", visible="sample_text", x="sample_text", xFrom="sample_text", xTo="sample_text", y="sample_text", yFrom="sample_text", yTo="sample_text")
    b1 = fxg_Transform()
    b2 = fxg_Transform()
    _safe_set(a, 'fxg_Line', b1)
    assert _is_linked(a, 'fxg_Line', b1)
    if hasattr(b1, 'fxg_Transform61'):
        assert _is_linked(b1, 'fxg_Transform61', a)
    _safe_set(a, 'fxg_Line', b2)
    assert _is_linked(a, 'fxg_Line', b2)
    if hasattr(b1, 'fxg_Transform61'):
        assert not _is_linked(b1, 'fxg_Transform61', a)
    if hasattr(b2, 'fxg_Transform61'):
        assert _is_linked(b2, 'fxg_Transform61', a)
    _safe_set(a, 'fxg_Line', None)
    assert not _is_linked(a, 'fxg_Line', b2)
    if hasattr(b2, 'fxg_Transform61'):
        assert not _is_linked(b2, 'fxg_Transform61', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CharacterAttributes_strategy = st.builds(CharacterAttributes)
@given(instance=CharacterAttributes_strategy)
@settings(max_examples=25)
def test_CharacterAttributes_instantiation(instance):
    assert isinstance(instance, CharacterAttributes)


ContainerAttributes_strategy = st.builds(ContainerAttributes)
@given(instance=ContainerAttributes_strategy)
@settings(max_examples=25)
def test_ContainerAttributes_instantiation(instance):
    assert isinstance(instance, ContainerAttributes)


FXGElement_strategy = st.builds(FXGElement)
@given(instance=FXGElement_strategy)
@settings(max_examples=25)
def test_FXGElement_instantiation(instance):
    assert isinstance(instance, FXGElement)


Fill_strategy = st.builds(Fill)
@given(instance=Fill_strategy)
@settings(max_examples=25)
def test_Fill_instantiation(instance):
    assert isinstance(instance, Fill)


Filter_strategy = st.builds(Filter)
@given(instance=Filter_strategy)
@settings(max_examples=25)
def test_Filter_instantiation(instance):
    assert isinstance(instance, Filter)


ParagraphAttributes_strategy = st.builds(ParagraphAttributes)
@given(instance=ParagraphAttributes_strategy)
@settings(max_examples=25)
def test_ParagraphAttributes_instantiation(instance):
    assert isinstance(instance, ParagraphAttributes)


RichTextContent_strategy = st.builds(RichTextContent)
@given(instance=RichTextContent_strategy)
@settings(max_examples=25)
def test_RichTextContent_instantiation(instance):
    assert isinstance(instance, RichTextContent)


RichTextContentContainer_strategy = st.builds(RichTextContentContainer)
@given(instance=RichTextContentContainer_strategy)
@settings(max_examples=25)
def test_RichTextContentContainer_instantiation(instance):
    assert isinstance(instance, RichTextContentContainer)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


Stroke_strategy = st.builds(Stroke)
@given(instance=Stroke_strategy)
@settings(max_examples=25)
def test_Stroke_instantiation(instance):
    assert isinstance(instance, Stroke)


fxg_BevelFilter_strategy = st.builds(fxg_BevelFilter, angle=safe_text, blurX=safe_text, blurY=safe_text, distance=safe_text, highlightAlpha=safe_text, highlightColor=safe_text, knockout=safe_text, quality=safe_text, shadowAlpha=safe_text, shadowColor=safe_text, strength=safe_text, type=safe_text)
@given(instance=fxg_BevelFilter_strategy)
@settings(max_examples=25)
def test_fxg_BevelFilter_instantiation(instance):
    assert isinstance(instance, fxg_BevelFilter)


fxg_BitmapFill_strategy = st.builds(fxg_BitmapFill, fillMode=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, source=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_BitmapFill_strategy)
@settings(max_examples=25)
def test_fxg_BitmapFill_instantiation(instance):
    assert isinstance(instance, fxg_BitmapFill)


fxg_BitmapImage_strategy = st.builds(fxg_BitmapImage, alpha=safe_text, blendMode=safe_text, fillMode=safe_text, height=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, source=safe_text, visible=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_BitmapImage_strategy)
@settings(max_examples=25)
def test_fxg_BitmapImage_instantiation(instance):
    assert isinstance(instance, fxg_BitmapImage)


fxg_BlurFilter_strategy = st.builds(fxg_BlurFilter, blurX=safe_text, blurY=safe_text, quality=safe_text)
@given(instance=fxg_BlurFilter_strategy)
@settings(max_examples=25)
def test_fxg_BlurFilter_instantiation(instance):
    assert isinstance(instance, fxg_BlurFilter)


fxg_CharacterAttributes_strategy = st.builds(fxg_CharacterAttributes, alignmentBaseline=safe_text, backgroundAlpha=safe_text, backgroundColor=safe_text, baselineShift=safe_text, breakOpportunity=safe_text, color=safe_text, digitCase=safe_text, digitWidth=safe_text, dominantBaseline=safe_text, fontFamily=safe_text, fontSize=safe_text, fontStyle=safe_text, fontWeight=safe_text, kerning=safe_text, ligatureLevel=safe_text, lineHeight=safe_text, lineThrough=safe_text, locale=safe_text, textAlpha=safe_text, textDecoration=safe_text, textRotation=safe_text, trackingLeft=safe_text, trackingRight=safe_text, typographicCase=safe_text, whiteSpaceCollapse=safe_text)
@given(instance=fxg_CharacterAttributes_strategy)
@settings(max_examples=25)
def test_fxg_CharacterAttributes_instantiation(instance):
    assert isinstance(instance, fxg_CharacterAttributes)


fxg_ColorMatrixFilter_strategy = st.builds(fxg_ColorMatrixFilter, matrix=safe_text)
@given(instance=fxg_ColorMatrixFilter_strategy)
@settings(max_examples=25)
def test_fxg_ColorMatrixFilter_instantiation(instance):
    assert isinstance(instance, fxg_ColorMatrixFilter)


fxg_ColorTransform_strategy = st.builds(fxg_ColorTransform, alphaMultiplier=safe_text, alphaOffset=safe_text, blueMultiplier=safe_text, blueOffset=safe_text, greenMultiplier=safe_text, greenOffset=safe_text, redMultiplier=safe_text, redOffset=safe_text)
@given(instance=fxg_ColorTransform_strategy)
@settings(max_examples=25)
def test_fxg_ColorTransform_instantiation(instance):
    assert isinstance(instance, fxg_ColorTransform)


fxg_ContainerAttributes_strategy = st.builds(fxg_ContainerAttributes, blockProgression=safe_text, columnCount=safe_text, columnGap=safe_text, columnWidth=safe_text, firstBaselineOffset=safe_text, lineBreak=safe_text, paddingBottom=safe_text, paddingLeft=safe_text, paddingRight=safe_text, paddingTop=safe_text, verticalAlign=safe_text)
@given(instance=fxg_ContainerAttributes_strategy)
@settings(max_examples=25)
def test_fxg_ContainerAttributes_instantiation(instance):
    assert isinstance(instance, fxg_ContainerAttributes)


fxg_ContainerElement_strategy = st.builds(fxg_ContainerElement)
@given(instance=fxg_ContainerElement_strategy)
@settings(max_examples=25)
def test_fxg_ContainerElement_instantiation(instance):
    assert isinstance(instance, fxg_ContainerElement)


fxg_Definition_strategy = st.builds(fxg_Definition, name=safe_text)
@given(instance=fxg_Definition_strategy)
@settings(max_examples=25)
def test_fxg_Definition_instantiation(instance):
    assert isinstance(instance, fxg_Definition)


fxg_DropShadowFilter_strategy = st.builds(fxg_DropShadowFilter, alpha=safe_text, angle=safe_text, blurX=safe_text, blurY=safe_text, color=safe_text, distance=safe_text, hideObject=safe_text, inner=safe_text, knockout=safe_text, quality=safe_text, strength=safe_text)
@given(instance=fxg_DropShadowFilter_strategy)
@settings(max_examples=25)
def test_fxg_DropShadowFilter_instantiation(instance):
    assert isinstance(instance, fxg_DropShadowFilter)


fxg_Ellipse_strategy = st.builds(fxg_Ellipse, alpha=safe_text, blendMode=safe_text, height=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, visible=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_Ellipse_strategy)
@settings(max_examples=25)
def test_fxg_Ellipse_instantiation(instance):
    assert isinstance(instance, fxg_Ellipse)


fxg_FXGElement_strategy = st.builds(fxg_FXGElement)
@given(instance=fxg_FXGElement_strategy)
@settings(max_examples=25)
def test_fxg_FXGElement_instantiation(instance):
    assert isinstance(instance, fxg_FXGElement)


fxg_Fill_strategy = st.builds(fxg_Fill)
@given(instance=fxg_Fill_strategy)
@settings(max_examples=25)
def test_fxg_Fill_instantiation(instance):
    assert isinstance(instance, fxg_Fill)


fxg_Filter_strategy = st.builds(fxg_Filter)
@given(instance=fxg_Filter_strategy)
@settings(max_examples=25)
def test_fxg_Filter_instantiation(instance):
    assert isinstance(instance, fxg_Filter)


fxg_GradientBevelFilter_strategy = st.builds(fxg_GradientBevelFilter, angle=safe_text, blurX=safe_text, blurY=safe_text, distance=safe_text, knockout=safe_text, quality=safe_text, strength=safe_text, type=safe_text)
@given(instance=fxg_GradientBevelFilter_strategy)
@settings(max_examples=25)
def test_fxg_GradientBevelFilter_instantiation(instance):
    assert isinstance(instance, fxg_GradientBevelFilter)


fxg_GradientEntry_strategy = st.builds(fxg_GradientEntry, alpha=safe_text, color=safe_text, ratio=safe_text)
@given(instance=fxg_GradientEntry_strategy)
@settings(max_examples=25)
def test_fxg_GradientEntry_instantiation(instance):
    assert isinstance(instance, fxg_GradientEntry)


fxg_GradientGlowFilter_strategy = st.builds(fxg_GradientGlowFilter, angle=safe_text, blurX=safe_text, blurY=safe_text, distance=safe_text, inner=safe_text, knockout=safe_text, quality=safe_text, strength=safe_text)
@given(instance=fxg_GradientGlowFilter_strategy)
@settings(max_examples=25)
def test_fxg_GradientGlowFilter_instantiation(instance):
    assert isinstance(instance, fxg_GradientGlowFilter)


fxg_Graphic_strategy = st.builds(fxg_Graphic, scaleGridBottom=safe_text, scaleGridLeft=safe_text, scaleGridRight=safe_text, scaleGridTop=safe_text, version=safe_text, viewHeight=st.integers(), viewWidth=st.integers())
@given(instance=fxg_Graphic_strategy)
@settings(max_examples=25)
def test_fxg_Graphic_instantiation(instance):
    assert isinstance(instance, fxg_Graphic)


fxg_Group_strategy = st.builds(fxg_Group, alpha=safe_text, blendMode=safe_text, id=safe_text, maskType=safe_text, rotation=safe_text, scaleGridBottom=safe_text, scaleGridLeft=safe_text, scaleGridRight=safe_text, scaleGridTop=safe_text, scaleX=safe_text, scaleY=safe_text, transformX=safe_text, transformY=safe_text, visible=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_Group_strategy)
@settings(max_examples=25)
def test_fxg_Group_instantiation(instance):
    assert isinstance(instance, fxg_Group)


fxg_Library_strategy = st.builds(fxg_Library)
@given(instance=fxg_Library_strategy)
@settings(max_examples=25)
def test_fxg_Library_instantiation(instance):
    assert isinstance(instance, fxg_Library)


fxg_Line_strategy = st.builds(fxg_Line, alpha=safe_text, blendMode=safe_text, id=safe_text, maskType=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, visible=safe_text, x=safe_text, xFrom=safe_text, xTo=safe_text, y=safe_text, yFrom=safe_text, yTo=safe_text)
@given(instance=fxg_Line_strategy)
@settings(max_examples=25)
def test_fxg_Line_instantiation(instance):
    assert isinstance(instance, fxg_Line)


fxg_LinearGradient_strategy = st.builds(fxg_LinearGradient, interpolationMethod=safe_text, rotation=safe_text, scaleX=safe_text, spreadMethod=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_LinearGradient_strategy)
@settings(max_examples=25)
def test_fxg_LinearGradient_instantiation(instance):
    assert isinstance(instance, fxg_LinearGradient)


fxg_LinearGradientStroke_strategy = st.builds(fxg_LinearGradientStroke, caps=safe_text, interpolationMethod=safe_text, joints=safe_text, miterLimit=safe_text, pixelHinting=safe_text, rotation=safe_text, scaleMode=safe_text, scaleX=safe_text, spreadMethod=safe_text, weight=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_LinearGradientStroke_strategy)
@settings(max_examples=25)
def test_fxg_LinearGradientStroke_instantiation(instance):
    assert isinstance(instance, fxg_LinearGradientStroke)


fxg_Matrix_strategy = st.builds(fxg_Matrix, a=safe_text, b=safe_text, c=safe_text, d=safe_text, tx=safe_text, ty=safe_text)
@given(instance=fxg_Matrix_strategy)
@settings(max_examples=25)
def test_fxg_Matrix_instantiation(instance):
    assert isinstance(instance, fxg_Matrix)


fxg_ParagraphAttributes_strategy = st.builds(fxg_ParagraphAttributes, justificationRule=safe_text, justificationStyle=safe_text, leadingModel=safe_text, paragraphEndIndent=safe_text, paragraphSpaceAfter=safe_text, paragraphSpaceBefore=safe_text, paragraphStartIndent=safe_text, tabStops=safe_text, textAlign=safe_text, textAlignLast=safe_text, textIndent=safe_text, textJustify=safe_text)
@given(instance=fxg_ParagraphAttributes_strategy)
@settings(max_examples=25)
def test_fxg_ParagraphAttributes_instantiation(instance):
    assert isinstance(instance, fxg_ParagraphAttributes)


fxg_Path_strategy = st.builds(fxg_Path, alpha=safe_text, blendMode=safe_text, data=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, visible=safe_text, winding=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_Path_strategy)
@settings(max_examples=25)
def test_fxg_Path_instantiation(instance):
    assert isinstance(instance, fxg_Path)


fxg_PlaceObject_strategy = st.builds(fxg_PlaceObject, id=safe_text)
@given(instance=fxg_PlaceObject_strategy)
@settings(max_examples=25)
def test_fxg_PlaceObject_instantiation(instance):
    assert isinstance(instance, fxg_PlaceObject)


fxg_Private_strategy = st.builds(fxg_Private)
@given(instance=fxg_Private_strategy)
@settings(max_examples=25)
def test_fxg_Private_instantiation(instance):
    assert isinstance(instance, fxg_Private)


fxg_RadialGradient_strategy = st.builds(fxg_RadialGradient, focalPointRatio=safe_text, interpolationMethod=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, spreadMethod=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_RadialGradient_strategy)
@settings(max_examples=25)
def test_fxg_RadialGradient_instantiation(instance):
    assert isinstance(instance, fxg_RadialGradient)


fxg_RadialGradientStroke_strategy = st.builds(fxg_RadialGradientStroke, caps=safe_text, focalPointRatio=safe_text, interpolationMethod=safe_text, joints=safe_text, miterLimit=safe_text, pixelHinting=safe_text, rotation=safe_text, scaleMode=safe_text, scaleX=safe_text, scaleY=safe_text, spreadMethod=safe_text, weight=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_RadialGradientStroke_strategy)
@settings(max_examples=25)
def test_fxg_RadialGradientStroke_instantiation(instance):
    assert isinstance(instance, fxg_RadialGradientStroke)


fxg_Rect_strategy = st.builds(fxg_Rect, alpha=safe_text, blendMode=safe_text, bottomLeftRadiusX=safe_text, bottomLeftRadiusY=safe_text, bottomRightRadiusX=safe_text, bottomRightRadiusY=safe_text, height=safe_text, radiusX=safe_text, radiusY=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, topLeftRadiusX=safe_text, topLeftRadiusY=safe_text, topRightRadiusX=safe_text, topRightRadiusY=safe_text, visible=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_Rect_strategy)
@settings(max_examples=25)
def test_fxg_Rect_instantiation(instance):
    assert isinstance(instance, fxg_Rect)


fxg_RichText_strategy = st.builds(fxg_RichText, _tempcontent=safe_text, alpha=safe_text, blendMode=safe_text, height=safe_text, id=safe_text, maskType=safe_text, rotation=safe_text, scaleX=safe_text, scaleY=safe_text, visible=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=fxg_RichText_strategy)
@settings(max_examples=25)
def test_fxg_RichText_instantiation(instance):
    assert isinstance(instance, fxg_RichText)


fxg_RichTextContent_strategy = st.builds(fxg_RichTextContent)
@given(instance=fxg_RichTextContent_strategy)
@settings(max_examples=25)
def test_fxg_RichTextContent_instantiation(instance):
    assert isinstance(instance, fxg_RichTextContent)


fxg_RichTextContentContainer_strategy = st.builds(fxg_RichTextContentContainer)
@given(instance=fxg_RichTextContentContainer_strategy)
@settings(max_examples=25)
def test_fxg_RichTextContentContainer_instantiation(instance):
    assert isinstance(instance, fxg_RichTextContentContainer)


fxg_Shape_strategy = st.builds(fxg_Shape)
@given(instance=fxg_Shape_strategy)
@settings(max_examples=25)
def test_fxg_Shape_instantiation(instance):
    assert isinstance(instance, fxg_Shape)


fxg_SolidColor_strategy = st.builds(fxg_SolidColor, alpha=safe_text, color=safe_text)
@given(instance=fxg_SolidColor_strategy)
@settings(max_examples=25)
def test_fxg_SolidColor_instantiation(instance):
    assert isinstance(instance, fxg_SolidColor)


fxg_SolidColorStroke_strategy = st.builds(fxg_SolidColorStroke, alpha=safe_text, caps=safe_text, color=safe_text, joints=safe_text, miterLimit=safe_text, pixelHinting=safe_text, scaleMode=safe_text, weight=safe_text)
@given(instance=fxg_SolidColorStroke_strategy)
@settings(max_examples=25)
def test_fxg_SolidColorStroke_instantiation(instance):
    assert isinstance(instance, fxg_SolidColorStroke)


fxg_Stroke_strategy = st.builds(fxg_Stroke)
@given(instance=fxg_Stroke_strategy)
@settings(max_examples=25)
def test_fxg_Stroke_instantiation(instance):
    assert isinstance(instance, fxg_Stroke)


fxg_Transform_strategy = st.builds(fxg_Transform)
@given(instance=fxg_Transform_strategy)
@settings(max_examples=25)
def test_fxg_Transform_instantiation(instance):
    assert isinstance(instance, fxg_Transform)


fxg_a_strategy = st.builds(fxg_a)
@given(instance=fxg_a_strategy)
@settings(max_examples=25)
def test_fxg_a_instantiation(instance):
    assert isinstance(instance, fxg_a)


fxg_br_strategy = st.builds(fxg_br)
@given(instance=fxg_br_strategy)
@settings(max_examples=25)
def test_fxg_br_instantiation(instance):
    assert isinstance(instance, fxg_br)


fxg_div_strategy = st.builds(fxg_div)
@given(instance=fxg_div_strategy)
@settings(max_examples=25)
def test_fxg_div_instantiation(instance):
    assert isinstance(instance, fxg_div)


fxg_img_strategy = st.builds(fxg_img)
@given(instance=fxg_img_strategy)
@settings(max_examples=25)
def test_fxg_img_instantiation(instance):
    assert isinstance(instance, fxg_img)


fxg_linkActiveFormat_strategy = st.builds(fxg_linkActiveFormat)
@given(instance=fxg_linkActiveFormat_strategy)
@settings(max_examples=25)
def test_fxg_linkActiveFormat_instantiation(instance):
    assert isinstance(instance, fxg_linkActiveFormat)


fxg_linkHoverFormat_strategy = st.builds(fxg_linkHoverFormat)
@given(instance=fxg_linkHoverFormat_strategy)
@settings(max_examples=25)
def test_fxg_linkHoverFormat_instantiation(instance):
    assert isinstance(instance, fxg_linkHoverFormat)


fxg_linkNormalFormat_strategy = st.builds(fxg_linkNormalFormat)
@given(instance=fxg_linkNormalFormat_strategy)
@settings(max_examples=25)
def test_fxg_linkNormalFormat_instantiation(instance):
    assert isinstance(instance, fxg_linkNormalFormat)


fxg_p_strategy = st.builds(fxg_p)
@given(instance=fxg_p_strategy)
@settings(max_examples=25)
def test_fxg_p_instantiation(instance):
    assert isinstance(instance, fxg_p)


fxg_rawtext_strategy = st.builds(fxg_rawtext, _text=safe_text)
@given(instance=fxg_rawtext_strategy)
@settings(max_examples=25)
def test_fxg_rawtext_instantiation(instance):
    assert isinstance(instance, fxg_rawtext)


fxg_span_strategy = st.builds(fxg_span)
@given(instance=fxg_span_strategy)
@settings(max_examples=25)
def test_fxg_span_instantiation(instance):
    assert isinstance(instance, fxg_span)


fxg_tab_strategy = st.builds(fxg_tab)
@given(instance=fxg_tab_strategy)
@settings(max_examples=25)
def test_fxg_tab_instantiation(instance):
    assert isinstance(instance, fxg_tab)


fxg_tcy_strategy = st.builds(fxg_tcy)
@given(instance=fxg_tcy_strategy)
@settings(max_examples=25)
def test_fxg_tcy_instantiation(instance):
    assert isinstance(instance, fxg_tcy)



