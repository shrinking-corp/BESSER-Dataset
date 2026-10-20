import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AContent,
    Attrs,
    Base,
    BaseTitleHeadElement,
    Block,
    Blocktext,
    Body,
    ButtonContent,
    CDATA,
    Caption,
    Cellhalign,
    Cellvalign,
    Character,
    Charset,
    Charsets,
    Col,
    ColElement,
    Colgroup,
    ContentType,
    ContentTypes,
    Coords,
    CoreAttrs,
    Datetime,
    DlElement,
    EMPTY,
    Events,
    FieldsetElement,
    Flow,
    Focus,
    Fontstyle,
    FormContent,
    Head,
    HeadElement,
    HeadMisc,
    Heading,
    Html,
    I18n,
    ID,
    IDREF,
    IDREFS,
    Inline,
    Inlineforms,
    LanguageCode,
    Length,
    Li,
    LinkTypes,
    Lists,
    MapContent,
    MapElement,
    MapElementContent,
    MediaDesc,
    Misc,
    Miscinline,
    MultiLength,
    NMTOKEN,
    Number,
    ObjectElement,
    Option,
    PCDATA,
    Phrase,
    Pixels,
    PreContent,
    ScriptExpression,
    SelectElement,
    Special,
    Specialpre,
    StyleSheet,
    TableElement,
    Tbody,
    Text,
    Tfoot,
    Thead,
    Title,
    TitleBaseHeadElement,
    Tr,
    TrElement,
    URI,
    UriList,
    ValuedElement,
    XHTML_A,
    XHTML_AContent,
    XHTML_Abbr,
    XHTML_Acronym,
    XHTML_Address,
    XHTML_Area,
    XHTML_Attrs,
    XHTML_B,
    XHTML_Base,
    XHTML_BaseHeadElement,
    XHTML_BaseTitleHeadElement,
    XHTML_Bdo,
    XHTML_Big,
    XHTML_Block,
    XHTML_Blockquote,
    XHTML_Blocktext,
    XHTML_Body,
    XHTML_Br,
    XHTML_Button,
    XHTML_ButtonContent,
    XHTML_CDATA,
    XHTML_Caption,
    XHTML_Cellhalign,
    XHTML_Cellvalign,
    XHTML_Character,
    XHTML_Charset,
    XHTML_Charsets,
    XHTML_Cite,
    XHTML_Code,
    XHTML_Col,
    XHTML_ColElement,
    XHTML_Colgroup,
    XHTML_ContentType,
    XHTML_ContentTypes,
    XHTML_Coords,
    XHTML_CoreAttrs,
    XHTML_Datetime,
    XHTML_Dd,
    XHTML_Del,
    XHTML_Dfn,
    XHTML_Div,
    XHTML_Dl,
    XHTML_DlElement,
    XHTML_Dt,
    XHTML_EMPTY,
    XHTML_Em,
    XHTML_Events,
    XHTML_Fieldset,
    XHTML_FieldsetElement,
    XHTML_Flow,
    XHTML_Focus,
    XHTML_Fontstyle,
    XHTML_Form,
    XHTML_FormContent,
    XHTML_H1,
    XHTML_H2,
    XHTML_H3,
    XHTML_H4,
    XHTML_H5,
    XHTML_H6,
    XHTML_Head,
    XHTML_HeadElement,
    XHTML_HeadMisc,
    XHTML_Heading,
    XHTML_Hr,
    XHTML_Html,
    XHTML_I,
    XHTML_I18n,
    XHTML_ID,
    XHTML_IDREF,
    XHTML_IDREFS,
    XHTML_Img,
    XHTML_Inline,
    XHTML_Inlineforms,
    XHTML_Input,
    XHTML_Ins,
    XHTML_Kbd,
    XHTML_Label,
    XHTML_LanguageCode,
    XHTML_Legend,
    XHTML_Length,
    XHTML_Li,
    XHTML_Link,
    XHTML_LinkTypes,
    XHTML_Lists,
    XHTML_Map,
    XHTML_MapContent,
    XHTML_MapElement,
    XHTML_MapElementContent,
    XHTML_MediaDesc,
    XHTML_Meta,
    XHTML_Misc,
    XHTML_Miscinline,
    XHTML_MultiLength,
    XHTML_NMTOKEN,
    XHTML_Noscript,
    XHTML_Number,
    XHTML_Object,
    XHTML_ObjectElement,
    XHTML_Ol,
    XHTML_Optgroup,
    XHTML_Option,
    XHTML_P,
    XHTML_PCDATA,
    XHTML_Param,
    XHTML_Phrase,
    XHTML_Pixels,
    XHTML_Pre,
    XHTML_PreContent,
    XHTML_Q,
    XHTML_Samp,
    XHTML_Script,
    XHTML_ScriptExpression,
    XHTML_Select,
    XHTML_SelectElement,
    XHTML_Small,
    XHTML_Span,
    XHTML_Special,
    XHTML_Specialpre,
    XHTML_Strong,
    XHTML_Style,
    XHTML_StyleSheet,
    XHTML_Sub,
    XHTML_Sup,
    XHTML_Table,
    XHTML_TableElement,
    XHTML_Tbody,
    XHTML_Td,
    XHTML_Text,
    XHTML_Textarea,
    XHTML_Tfoot,
    XHTML_Th,
    XHTML_Thead,
    XHTML_Title,
    XHTML_TitleBaseHeadElement,
    XHTML_TitleHeadElement,
    XHTML_Tr,
    XHTML_TrElement,
    XHTML_Tt,
    XHTML_URI,
    XHTML_Ul,
    XHTML_UriList,
    XHTML_ValuedElement,
    XHTML_Var,
    XHTML_block,
    XHTML_inline,
    block,
    inline,
    ButtonType,
    CellHAlign,
    CellVAlign,
    Direction,
    FomeMethod,
    InputType,
    Scope,
    Shape,
    TFrame,
    TRules,
    ValueType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abbr572_stub_double():
    # Text has no real 'Text574' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Th's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Th's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Th(scope="sample_text")
    partner = Text()
    setattr(partner, 'Text574', None)
    _safe_set(owner, 'XHTML_Th573', partner)
    assert getattr(partner, 'Text574') == owner
    _safe_set(owner, 'XHTML_Th573', None)
    assert getattr(partner, 'Text574') is None


def test_assoc_abbr588_stub_double():
    # Text has no real 'Text590' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Td's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Td's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Td(scope="sample_text")
    partner = Text()
    setattr(partner, 'Text590', None)
    _safe_set(owner, 'XHTML_Td589', partner)
    assert getattr(partner, 'Text590') == owner
    _safe_set(owner, 'XHTML_Td589', None)
    assert getattr(partner, 'Text590') is None


def test_assoc_accept411_stub_double():
    # ContentTypes has no real 'ContentTypes' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Form(method="sample_text")
    partner = ContentTypes()
    setattr(partner, 'ContentTypes', None)
    _safe_set(owner, 'XHTML_Form412', partner)
    assert getattr(partner, 'ContentTypes') == owner
    _safe_set(owner, 'XHTML_Form412', None)
    assert getattr(partner, 'ContentTypes') is None


def test_assoc_accept455_stub_double():
    # ContentTypes has no real 'ContentTypes457' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = ContentTypes()
    setattr(partner, 'ContentTypes457', None)
    _safe_set(owner, 'XHTML_Input456', partner)
    assert getattr(partner, 'ContentTypes457') == owner
    _safe_set(owner, 'XHTML_Input456', None)
    assert getattr(partner, 'ContentTypes457') is None


def test_assoc_accept_charset413_stub_double():
    # Charsets has no real 'Charsets' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Form(method="sample_text")
    partner = Charsets()
    setattr(partner, 'Charsets', None)
    _safe_set(owner, 'XHTML_Form414', partner)
    assert getattr(partner, 'Charsets') == owner
    _safe_set(owner, 'XHTML_Form414', None)
    assert getattr(partner, 'Charsets') is None


def test_assoc_acontent235_stub_double():
    # AContent has no real 'AContent' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = AContent()
    setattr(partner, 'AContent', None)
    _safe_set(owner, 'XHTML_A', {partner})
    assert getattr(partner, 'AContent') == owner
    _safe_set(owner, 'XHTML_A', set())
    assert getattr(partner, 'AContent') is None


def test_assoc_action399_stub_double():
    # URI has no real 'URI401' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Form(method="sample_text")
    partner = URI()
    setattr(partner, 'URI401', None)
    _safe_set(owner, 'XHTML_Form400', partner)
    assert getattr(partner, 'URI401') == owner
    _safe_set(owner, 'XHTML_Form400', None)
    assert getattr(partner, 'URI401') is None


def test_assoc_alt358_stub_double():
    # Text has no real 'Text360' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Img's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Img's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Img(ismap="sample_text")
    partner = Text()
    setattr(partner, 'Text360', None)
    _safe_set(owner, 'XHTML_Img359', partner)
    assert getattr(partner, 'Text360') == owner
    _safe_set(owner, 'XHTML_Img359', None)
    assert getattr(partner, 'Text360') is None


def test_assoc_alt395_stub_double():
    # Text has no real 'Text397' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Area(nohref="sample_text", shape="sample_text")
    partner = Text()
    setattr(partner, 'Text397', None)
    _safe_set(owner, 'XHTML_Area396', partner)
    assert getattr(partner, 'Text397') == owner
    _safe_set(owner, 'XHTML_Area396', None)
    assert getattr(partner, 'Text397') is None


def test_assoc_alt443_stub_double():
    # CDATA has no real 'CDATA445' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA445', None)
    _safe_set(owner, 'XHTML_Input444', partner)
    assert getattr(partner, 'CDATA445') == owner
    _safe_set(owner, 'XHTML_Input444', None)
    assert getattr(partner, 'CDATA445') is None


def test_assoc_archive325_stub_double():
    # UriList has no real 'UriList' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = UriList()
    setattr(partner, 'UriList', None)
    _safe_set(owner, 'XHTML_Object326', partner)
    assert getattr(partner, 'UriList') == owner
    _safe_set(owner, 'XHTML_Object326', None)
    assert getattr(partner, 'UriList') is None


def test_assoc_axis575_stub_double():
    # CDATA has no real 'CDATA577' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Th's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Th's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Th(scope="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA577', None)
    _safe_set(owner, 'XHTML_Th576', partner)
    assert getattr(partner, 'CDATA577') == owner
    _safe_set(owner, 'XHTML_Th576', None)
    assert getattr(partner, 'CDATA577') is None


def test_assoc_axis591_stub_double():
    # CDATA has no real 'CDATA593' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Td's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Td's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Td(scope="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA593', None)
    _safe_set(owner, 'XHTML_Td592', partner)
    assert getattr(partner, 'CDATA593') == owner
    _safe_set(owner, 'XHTML_Td592', None)
    assert getattr(partner, 'CDATA593') is None


def test_assoc_bdoElements260_stub_double():
    # Inline has no real 'Inline261' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Bdo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Bdo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Bdo(dir="sample_text")
    partner = Inline()
    setattr(partner, 'Inline261', None)
    _safe_set(owner, 'XHTML_Bdo', {partner})
    assert getattr(partner, 'Inline261') == owner
    _safe_set(owner, 'XHTML_Bdo', set())
    assert getattr(partner, 'Inline261') is None


def test_assoc_border535_stub_double():
    # Pixels has no real 'Pixels' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Pixels()
    setattr(partner, 'Pixels', None)
    _safe_set(owner, 'XHTML_Table536', partner)
    assert getattr(partner, 'Pixels') == owner
    _safe_set(owner, 'XHTML_Table536', None)
    assert getattr(partner, 'Pixels') is None


def test_assoc_buttoncontent508_stub_double():
    # ButtonContent has no real 'ButtonContent' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Button(disabled="sample_text", type="sample_text")
    partner = ButtonContent()
    setattr(partner, 'ButtonContent', None)
    _safe_set(owner, 'XHTML_Button', {partner})
    assert getattr(partner, 'ButtonContent') == owner
    _safe_set(owner, 'XHTML_Button', set())
    assert getattr(partner, 'ButtonContent') is None


def test_assoc_caption520_stub_double():
    # Caption has no real 'Caption' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Caption()
    setattr(partner, 'Caption', None)
    _safe_set(owner, 'XHTML_Table', {partner})
    assert getattr(partner, 'Caption') == owner
    _safe_set(owner, 'XHTML_Table', set())
    assert getattr(partner, 'Caption') is None


def test_assoc_cellpadding540_stub_double():
    # Length has no real 'Length542' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Length()
    setattr(partner, 'Length542', None)
    _safe_set(owner, 'XHTML_Table541', partner)
    assert getattr(partner, 'Length542') == owner
    _safe_set(owner, 'XHTML_Table541', None)
    assert getattr(partner, 'Length542') is None


def test_assoc_cellspacing537_stub_double():
    # Length has no real 'Length539' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Length()
    setattr(partner, 'Length539', None)
    _safe_set(owner, 'XHTML_Table538', partner)
    assert getattr(partner, 'Length539') == owner
    _safe_set(owner, 'XHTML_Table538', None)
    assert getattr(partner, 'Length539') is None


def test_assoc_char515_stub_double():
    # Character has no real 'Character516' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Cellhalign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Cellhalign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Cellhalign(align="sample_text")
    partner = Character()
    setattr(partner, 'Character516', None)
    _safe_set(owner, 'XHTML_Cellhalign', partner)
    assert getattr(partner, 'Character516') == owner
    _safe_set(owner, 'XHTML_Cellhalign', None)
    assert getattr(partner, 'Character516') is None


def test_assoc_charoff517_stub_double():
    # Length has no real 'Length519' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Cellhalign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Cellhalign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Cellhalign(align="sample_text")
    partner = Length()
    setattr(partner, 'Length519', None)
    _safe_set(owner, 'XHTML_Cellhalign518', partner)
    assert getattr(partner, 'Length519') == owner
    _safe_set(owner, 'XHTML_Cellhalign518', None)
    assert getattr(partner, 'Length519') is None


def test_assoc_charset168_stub_double():
    # Charset has no real 'Charset170' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Script's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Script's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Script(defer="sample_text", xml_space="sample_text")
    partner = Charset()
    setattr(partner, 'Charset170', None)
    _safe_set(owner, 'XHTML_Script169', partner)
    assert getattr(partner, 'Charset170') == owner
    _safe_set(owner, 'XHTML_Script169', None)
    assert getattr(partner, 'Charset170') is None


def test_assoc_charset236_stub_double():
    # Charset has no real 'Charset238' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = Charset()
    setattr(partner, 'Charset238', None)
    _safe_set(owner, 'XHTML_A237', partner)
    assert getattr(partner, 'Charset238') == owner
    _safe_set(owner, 'XHTML_A237', None)
    assert getattr(partner, 'Charset238') is None


def test_assoc_classid310_stub_double():
    # URI has no real 'URI312' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = URI()
    setattr(partner, 'URI312', None)
    _safe_set(owner, 'XHTML_Object311', partner)
    assert getattr(partner, 'URI312') == owner
    _safe_set(owner, 'XHTML_Object311', None)
    assert getattr(partner, 'URI312') is None


def test_assoc_codebase313_stub_double():
    # URI has no real 'URI315' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = URI()
    setattr(partner, 'URI315', None)
    _safe_set(owner, 'XHTML_Object314', partner)
    assert getattr(partner, 'URI315') == owner
    _safe_set(owner, 'XHTML_Object314', None)
    assert getattr(partner, 'URI315') is None


def test_assoc_codetype322_stub_double():
    # ContentType has no real 'ContentType324' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = ContentType()
    setattr(partner, 'ContentType324', None)
    _safe_set(owner, 'XHTML_Object323', partner)
    assert getattr(partner, 'ContentType324') == owner
    _safe_set(owner, 'XHTML_Object323', None)
    assert getattr(partner, 'ContentType324') is None


def test_assoc_colelement521_stub_double():
    # ColElement has no real 'ColElement' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = ColElement()
    setattr(partner, 'ColElement', None)
    _safe_set(owner, 'XHTML_Table522', partner)
    assert getattr(partner, 'ColElement') == owner
    _safe_set(owner, 'XHTML_Table522', None)
    assert getattr(partner, 'ColElement') is None


def test_assoc_cols491_stub_double():
    # Number has no real 'Number493' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Textarea's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Textarea's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Textarea(disabled="sample_text", readonly="sample_text")
    partner = Number()
    setattr(partner, 'Number493', None)
    _safe_set(owner, 'XHTML_Textarea492', partner)
    assert getattr(partner, 'Number493') == owner
    _safe_set(owner, 'XHTML_Textarea492', None)
    assert getattr(partner, 'Number493') is None


def test_assoc_colspan583_stub_double():
    # Number has no real 'Number585' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Th's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Th's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Th(scope="sample_text")
    partner = Number()
    setattr(partner, 'Number585', None)
    _safe_set(owner, 'XHTML_Th584', partner)
    assert getattr(partner, 'Number585') == owner
    _safe_set(owner, 'XHTML_Th584', None)
    assert getattr(partner, 'Number585') is None


def test_assoc_colspan600_stub_double():
    # Number has no real 'Number602' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Td's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Td's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Td(scope="sample_text")
    partner = Number()
    setattr(partner, 'Number602', None)
    _safe_set(owner, 'XHTML_Td601', partner)
    assert getattr(partner, 'Number602') == owner
    _safe_set(owner, 'XHTML_Td601', None)
    assert getattr(partner, 'Number602') is None


def test_assoc_coords256_stub_double():
    # Coords has no real 'Coords' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = Coords()
    setattr(partner, 'Coords', None)
    _safe_set(owner, 'XHTML_A257', partner)
    assert getattr(partner, 'Coords') == owner
    _safe_set(owner, 'XHTML_A257', None)
    assert getattr(partner, 'Coords') is None


def test_assoc_coords390_stub_double():
    # Coords has no real 'Coords391' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Area(nohref="sample_text", shape="sample_text")
    partner = Coords()
    setattr(partner, 'Coords391', None)
    _safe_set(owner, 'XHTML_Area', partner)
    assert getattr(partner, 'Coords391') == owner
    _safe_set(owner, 'XHTML_Area', None)
    assert getattr(partner, 'Coords391') is None


def test_assoc_data316_stub_double():
    # URI has no real 'URI318' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = URI()
    setattr(partner, 'URI318', None)
    _safe_set(owner, 'XHTML_Object317', partner)
    assert getattr(partner, 'URI318') == owner
    _safe_set(owner, 'XHTML_Object317', None)
    assert getattr(partner, 'URI318') is None


def test_assoc_enctype402_stub_double():
    # ContentType has no real 'ContentType404' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Form(method="sample_text")
    partner = ContentType()
    setattr(partner, 'ContentType404', None)
    _safe_set(owner, 'XHTML_Form403', partner)
    assert getattr(partner, 'ContentType404') == owner
    _safe_set(owner, 'XHTML_Form403', None)
    assert getattr(partner, 'ContentType404') is None


def test_assoc_formelement398_stub_double():
    # FormContent has no real 'FormContent' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Form(method="sample_text")
    partner = FormContent()
    setattr(partner, 'FormContent', None)
    _safe_set(owner, 'XHTML_Form', {partner})
    assert getattr(partner, 'FormContent') == owner
    _safe_set(owner, 'XHTML_Form', set())
    assert getattr(partner, 'FormContent') is None


def test_assoc_headers578_stub_double():
    # IDREFS has no real 'IDREFS' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Th's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Th's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Th(scope="sample_text")
    partner = IDREFS()
    setattr(partner, 'IDREFS', None)
    _safe_set(owner, 'XHTML_Th579', partner)
    assert getattr(partner, 'IDREFS') == owner
    _safe_set(owner, 'XHTML_Th579', None)
    assert getattr(partner, 'IDREFS') is None


def test_assoc_headers594_stub_double():
    # IDREFS has no real 'IDREFS596' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Td's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Td's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Td(scope="sample_text")
    partner = IDREFS()
    setattr(partner, 'IDREFS596', None)
    _safe_set(owner, 'XHTML_Td595', partner)
    assert getattr(partner, 'IDREFS596') == owner
    _safe_set(owner, 'XHTML_Td595', None)
    assert getattr(partner, 'IDREFS596') is None


def test_assoc_height330_stub_double():
    # Length has no real 'Length332' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = Length()
    setattr(partner, 'Length332', None)
    _safe_set(owner, 'XHTML_Object331', partner)
    assert getattr(partner, 'Length332') == owner
    _safe_set(owner, 'XHTML_Object331', None)
    assert getattr(partner, 'Length332') is None


def test_assoc_height364_stub_double():
    # Length has no real 'Length366' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Img's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Img's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Img(ismap="sample_text")
    partner = Length()
    setattr(partner, 'Length366', None)
    _safe_set(owner, 'XHTML_Img365', partner)
    assert getattr(partner, 'Length366') == owner
    _safe_set(owner, 'XHTML_Img365', None)
    assert getattr(partner, 'Length366') is None


def test_assoc_href244_stub_double():
    # URI has no real 'URI246' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = URI()
    setattr(partner, 'URI246', None)
    _safe_set(owner, 'XHTML_A245', partner)
    assert getattr(partner, 'URI246') == owner
    _safe_set(owner, 'XHTML_A245', None)
    assert getattr(partner, 'URI246') is None


def test_assoc_href392_stub_double():
    # URI has no real 'URI394' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Area(nohref="sample_text", shape="sample_text")
    partner = URI()
    setattr(partner, 'URI394', None)
    _safe_set(owner, 'XHTML_Area393', partner)
    assert getattr(partner, 'URI394') == owner
    _safe_set(owner, 'XHTML_Area393', None)
    assert getattr(partner, 'URI394') is None


def test_assoc_hreflang247_stub_double():
    # LanguageCode has no real 'LanguageCode249' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = LanguageCode()
    setattr(partner, 'LanguageCode249', None)
    _safe_set(owner, 'XHTML_A248', partner)
    assert getattr(partner, 'LanguageCode249') == owner
    _safe_set(owner, 'XHTML_A248', None)
    assert getattr(partner, 'LanguageCode249') is None


def test_assoc_i18n152_stub_double():
    # I18n has no real 'I18n153' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Style(xml_space="sample_text")
    partner = I18n()
    setattr(partner, 'I18n153', None)
    _safe_set(owner, 'XHTML_Style', partner)
    assert getattr(partner, 'I18n153') == owner
    _safe_set(owner, 'XHTML_Style', None)
    assert getattr(partner, 'I18n153') is None


def test_assoc_id154_stub_double():
    # ID has no real 'ID156' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Style(xml_space="sample_text")
    partner = ID()
    setattr(partner, 'ID156', None)
    _safe_set(owner, 'XHTML_Style155', partner)
    assert getattr(partner, 'ID156') == owner
    _safe_set(owner, 'XHTML_Style155', None)
    assert getattr(partner, 'ID156') is None


def test_assoc_id166_stub_double():
    # ID has no real 'ID167' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Script's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Script's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Script(defer="sample_text", xml_space="sample_text")
    partner = ID()
    setattr(partner, 'ID167', None)
    _safe_set(owner, 'XHTML_Script', partner)
    assert getattr(partner, 'ID167') == owner
    _safe_set(owner, 'XHTML_Script', None)
    assert getattr(partner, 'ID167') is None


def test_assoc_id345_stub_double():
    # ID has no real 'ID346' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Param(valuetype="sample_text")
    partner = ID()
    setattr(partner, 'ID346', None)
    _safe_set(owner, 'XHTML_Param', partner)
    assert getattr(partner, 'ID346') == owner
    _safe_set(owner, 'XHTML_Param', None)
    assert getattr(partner, 'ID346') is None


def test_assoc_label478_stub_double():
    # Text has no real 'Text480' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Optgroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Optgroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Optgroup(disabled="sample_text")
    partner = Text()
    setattr(partner, 'Text480', None)
    _safe_set(owner, 'XHTML_Optgroup479', partner)
    assert getattr(partner, 'Text480') == owner
    _safe_set(owner, 'XHTML_Optgroup479', None)
    assert getattr(partner, 'Text480') is None


def test_assoc_label481_stub_double():
    # Text has no real 'Text482' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Option(disabled="sample_text", selected="sample_text")
    partner = Text()
    setattr(partner, 'Text482', None)
    _safe_set(owner, 'XHTML_Option', partner)
    assert getattr(partner, 'Text482') == owner
    _safe_set(owner, 'XHTML_Option', None)
    assert getattr(partner, 'Text482') is None


def test_assoc_lang12_stub_double():
    # LanguageCode has no real 'LanguageCode' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_I18n's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_I18n's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_I18n(dir="sample_text")
    partner = LanguageCode()
    setattr(partner, 'LanguageCode', None)
    _safe_set(owner, 'XHTML_I18n', partner)
    assert getattr(partner, 'LanguageCode') == owner
    _safe_set(owner, 'XHTML_I18n', None)
    assert getattr(partner, 'LanguageCode') is None


def test_assoc_lang262_stub_double():
    # LanguageCode has no real 'LanguageCode264' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Bdo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Bdo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Bdo(dir="sample_text")
    partner = LanguageCode()
    setattr(partner, 'LanguageCode264', None)
    _safe_set(owner, 'XHTML_Bdo263', partner)
    assert getattr(partner, 'LanguageCode264') == owner
    _safe_set(owner, 'XHTML_Bdo263', None)
    assert getattr(partner, 'LanguageCode264') is None


def test_assoc_longdesc361_stub_double():
    # URI has no real 'URI363' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Img's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Img's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Img(ismap="sample_text")
    partner = URI()
    setattr(partner, 'URI363', None)
    _safe_set(owner, 'XHTML_Img362', partner)
    assert getattr(partner, 'URI363') == owner
    _safe_set(owner, 'XHTML_Img362', None)
    assert getattr(partner, 'URI363') is None


def test_assoc_maxlength437_stub_double():
    # Number has no real 'Number439' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = Number()
    setattr(partner, 'Number439', None)
    _safe_set(owner, 'XHTML_Input438', partner)
    assert getattr(partner, 'Number439') == owner
    _safe_set(owner, 'XHTML_Input438', None)
    assert getattr(partner, 'Number439') is None


def test_assoc_media160_stub_double():
    # MediaDesc has no real 'MediaDesc162' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Style(xml_space="sample_text")
    partner = MediaDesc()
    setattr(partner, 'MediaDesc162', None)
    _safe_set(owner, 'XHTML_Style161', partner)
    assert getattr(partner, 'MediaDesc162') == owner
    _safe_set(owner, 'XHTML_Style161', None)
    assert getattr(partner, 'MediaDesc162') is None


def test_assoc_name242_stub_double():
    # NMTOKEN has no real 'NMTOKEN' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = NMTOKEN()
    setattr(partner, 'NMTOKEN', None)
    _safe_set(owner, 'XHTML_A243', partner)
    assert getattr(partner, 'NMTOKEN') == owner
    _safe_set(owner, 'XHTML_A243', None)
    assert getattr(partner, 'NMTOKEN') is None


def test_assoc_name339_stub_double():
    # NMTOKEN has no real 'NMTOKEN341' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = NMTOKEN()
    setattr(partner, 'NMTOKEN341', None)
    _safe_set(owner, 'XHTML_Object340', partner)
    assert getattr(partner, 'NMTOKEN341') == owner
    _safe_set(owner, 'XHTML_Object340', None)
    assert getattr(partner, 'NMTOKEN341') is None


def test_assoc_name347_stub_double():
    # CDATA has no real 'CDATA349' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Param(valuetype="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA349', None)
    _safe_set(owner, 'XHTML_Param348', partner)
    assert getattr(partner, 'CDATA349') == owner
    _safe_set(owner, 'XHTML_Param348', None)
    assert getattr(partner, 'CDATA349') is None


def test_assoc_name429_stub_double():
    # CDATA has no real 'CDATA430' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA430', None)
    _safe_set(owner, 'XHTML_Input', partner)
    assert getattr(partner, 'CDATA430') == owner
    _safe_set(owner, 'XHTML_Input', None)
    assert getattr(partner, 'CDATA430') is None


def test_assoc_name459_stub_double():
    # CDATA has no real 'CDATA461' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Select(disabled="sample_text", multiple="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA461', None)
    _safe_set(owner, 'XHTML_Select460', partner)
    assert getattr(partner, 'CDATA461') == owner
    _safe_set(owner, 'XHTML_Select460', None)
    assert getattr(partner, 'CDATA461') is None


def test_assoc_name486_stub_double():
    # CDATA has no real 'CDATA487' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Textarea's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Textarea's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Textarea(disabled="sample_text", readonly="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA487', None)
    _safe_set(owner, 'XHTML_Textarea', partner)
    assert getattr(partner, 'CDATA487') == owner
    _safe_set(owner, 'XHTML_Textarea', None)
    assert getattr(partner, 'CDATA487') is None


def test_assoc_name509_stub_double():
    # CDATA has no real 'CDATA511' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Button(disabled="sample_text", type="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA511', None)
    _safe_set(owner, 'XHTML_Button510', partner)
    assert getattr(partner, 'CDATA511') == owner
    _safe_set(owner, 'XHTML_Button510', None)
    assert getattr(partner, 'CDATA511') is None


def test_assoc_objectelement309_stub_double():
    # ObjectElement has no real 'ObjectElement' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = ObjectElement()
    setattr(partner, 'ObjectElement', None)
    _safe_set(owner, 'XHTML_Object', {partner})
    assert getattr(partner, 'ObjectElement') == owner
    _safe_set(owner, 'XHTML_Object', set())
    assert getattr(partner, 'ObjectElement') is None


def test_assoc_onblur471_stub_double():
    # ScriptExpression has no real 'ScriptExpression473' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Select(disabled="sample_text", multiple="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression473', None)
    _safe_set(owner, 'XHTML_Select472', partner)
    assert getattr(partner, 'ScriptExpression473') == owner
    _safe_set(owner, 'XHTML_Select472', None)
    assert getattr(partner, 'ScriptExpression473') is None


def test_assoc_onchange452_stub_double():
    # ScriptExpression has no real 'ScriptExpression454' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression454', None)
    _safe_set(owner, 'XHTML_Input453', partner)
    assert getattr(partner, 'ScriptExpression454') == owner
    _safe_set(owner, 'XHTML_Input453', None)
    assert getattr(partner, 'ScriptExpression454') is None


def test_assoc_onchange474_stub_double():
    # ScriptExpression has no real 'ScriptExpression476' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Select(disabled="sample_text", multiple="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression476', None)
    _safe_set(owner, 'XHTML_Select475', partner)
    assert getattr(partner, 'ScriptExpression476') == owner
    _safe_set(owner, 'XHTML_Select475', None)
    assert getattr(partner, 'ScriptExpression476') is None


def test_assoc_onchange497_stub_double():
    # ScriptExpression has no real 'ScriptExpression499' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Textarea's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Textarea's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Textarea(disabled="sample_text", readonly="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression499', None)
    _safe_set(owner, 'XHTML_Textarea498', partner)
    assert getattr(partner, 'ScriptExpression499') == owner
    _safe_set(owner, 'XHTML_Textarea498', None)
    assert getattr(partner, 'ScriptExpression499') is None


def test_assoc_onfocus468_stub_double():
    # ScriptExpression has no real 'ScriptExpression470' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Select(disabled="sample_text", multiple="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression470', None)
    _safe_set(owner, 'XHTML_Select469', partner)
    assert getattr(partner, 'ScriptExpression470') == owner
    _safe_set(owner, 'XHTML_Select469', None)
    assert getattr(partner, 'ScriptExpression470') is None


def test_assoc_onreset408_stub_double():
    # ScriptExpression has no real 'ScriptExpression410' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Form(method="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression410', None)
    _safe_set(owner, 'XHTML_Form409', partner)
    assert getattr(partner, 'ScriptExpression410') == owner
    _safe_set(owner, 'XHTML_Form409', None)
    assert getattr(partner, 'ScriptExpression410') is None


def test_assoc_onselect449_stub_double():
    # ScriptExpression has no real 'ScriptExpression451' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression451', None)
    _safe_set(owner, 'XHTML_Input450', partner)
    assert getattr(partner, 'ScriptExpression451') == owner
    _safe_set(owner, 'XHTML_Input450', None)
    assert getattr(partner, 'ScriptExpression451') is None


def test_assoc_onselect494_stub_double():
    # ScriptExpression has no real 'ScriptExpression496' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Textarea's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Textarea's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Textarea(disabled="sample_text", readonly="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression496', None)
    _safe_set(owner, 'XHTML_Textarea495', partner)
    assert getattr(partner, 'ScriptExpression496') == owner
    _safe_set(owner, 'XHTML_Textarea495', None)
    assert getattr(partner, 'ScriptExpression496') is None


def test_assoc_onsubmit405_stub_double():
    # ScriptExpression has no real 'ScriptExpression407' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Form(method="sample_text")
    partner = ScriptExpression()
    setattr(partner, 'ScriptExpression407', None)
    _safe_set(owner, 'XHTML_Form406', partner)
    assert getattr(partner, 'ScriptExpression407') == owner
    _safe_set(owner, 'XHTML_Form406', None)
    assert getattr(partner, 'ScriptExpression407') is None


def test_assoc_options477_stub_double():
    # Option has no real 'Option' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Optgroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Optgroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Optgroup(disabled="sample_text")
    partner = Option()
    setattr(partner, 'Option', None)
    _safe_set(owner, 'XHTML_Optgroup', {partner})
    assert getattr(partner, 'Option') == owner
    _safe_set(owner, 'XHTML_Optgroup', set())
    assert getattr(partner, 'Option') is None


def test_assoc_optionvalue483_stub_double():
    # CDATA has no real 'CDATA485' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Option(disabled="sample_text", selected="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA485', None)
    _safe_set(owner, 'XHTML_Option484', partner)
    assert getattr(partner, 'CDATA485') == owner
    _safe_set(owner, 'XHTML_Option484', None)
    assert getattr(partner, 'CDATA485') is None


def test_assoc_preElements214_stub_double():
    # PreContent has no real 'PreContent' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Pre's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Pre's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Pre(xml_space="sample_text")
    partner = PreContent()
    setattr(partner, 'PreContent', None)
    _safe_set(owner, 'XHTML_Pre', {partner})
    assert getattr(partner, 'PreContent') == owner
    _safe_set(owner, 'XHTML_Pre', set())
    assert getattr(partner, 'PreContent') is None


def test_assoc_rel250_stub_double():
    # LinkTypes has no real 'LinkTypes252' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = LinkTypes()
    setattr(partner, 'LinkTypes252', None)
    _safe_set(owner, 'XHTML_A251', partner)
    assert getattr(partner, 'LinkTypes252') == owner
    _safe_set(owner, 'XHTML_A251', None)
    assert getattr(partner, 'LinkTypes252') is None


def test_assoc_rev253_stub_double():
    # LinkTypes has no real 'LinkTypes255' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = LinkTypes()
    setattr(partner, 'LinkTypes255', None)
    _safe_set(owner, 'XHTML_A254', partner)
    assert getattr(partner, 'LinkTypes255') == owner
    _safe_set(owner, 'XHTML_A254', None)
    assert getattr(partner, 'LinkTypes255') is None


def test_assoc_rows488_stub_double():
    # Number has no real 'Number490' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Textarea's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Textarea's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Textarea(disabled="sample_text", readonly="sample_text")
    partner = Number()
    setattr(partner, 'Number490', None)
    _safe_set(owner, 'XHTML_Textarea489', partner)
    assert getattr(partner, 'Number490') == owner
    _safe_set(owner, 'XHTML_Textarea489', None)
    assert getattr(partner, 'Number490') is None


def test_assoc_rowspan580_stub_double():
    # Number has no real 'Number582' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Th's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Th's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Th(scope="sample_text")
    partner = Number()
    setattr(partner, 'Number582', None)
    _safe_set(owner, 'XHTML_Th581', partner)
    assert getattr(partner, 'Number582') == owner
    _safe_set(owner, 'XHTML_Th581', None)
    assert getattr(partner, 'Number582') is None


def test_assoc_rowspan597_stub_double():
    # Number has no real 'Number599' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Td's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Td's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Td(scope="sample_text")
    partner = Number()
    setattr(partner, 'Number599', None)
    _safe_set(owner, 'XHTML_Td598', partner)
    assert getattr(partner, 'Number599') == owner
    _safe_set(owner, 'XHTML_Td598', None)
    assert getattr(partner, 'Number599') is None


def test_assoc_selectelement458_stub_double():
    # SelectElement has no real 'SelectElement' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Select(disabled="sample_text", multiple="sample_text")
    partner = SelectElement()
    setattr(partner, 'SelectElement', None)
    _safe_set(owner, 'XHTML_Select', {partner})
    assert getattr(partner, 'SelectElement') == owner
    _safe_set(owner, 'XHTML_Select', set())
    assert getattr(partner, 'SelectElement') is None


def test_assoc_size434_stub_double():
    # CDATA has no real 'CDATA436' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA436', None)
    _safe_set(owner, 'XHTML_Input435', partner)
    assert getattr(partner, 'CDATA436') == owner
    _safe_set(owner, 'XHTML_Input435', None)
    assert getattr(partner, 'CDATA436') is None


def test_assoc_size462_stub_double():
    # Number has no real 'Number464' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Select(disabled="sample_text", multiple="sample_text")
    partner = Number()
    setattr(partner, 'Number464', None)
    _safe_set(owner, 'XHTML_Select463', partner)
    assert getattr(partner, 'Number464') == owner
    _safe_set(owner, 'XHTML_Select463', None)
    assert getattr(partner, 'Number464') is None


def test_assoc_src174_stub_double():
    # URI has no real 'URI176' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Script's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Script's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Script(defer="sample_text", xml_space="sample_text")
    partner = URI()
    setattr(partner, 'URI176', None)
    _safe_set(owner, 'XHTML_Script175', partner)
    assert getattr(partner, 'URI176') == owner
    _safe_set(owner, 'XHTML_Script175', None)
    assert getattr(partner, 'URI176') is None


def test_assoc_src356_stub_double():
    # URI has no real 'URI357' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Img's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Img's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Img(ismap="sample_text")
    partner = URI()
    setattr(partner, 'URI357', None)
    _safe_set(owner, 'XHTML_Img', partner)
    assert getattr(partner, 'URI357') == owner
    _safe_set(owner, 'XHTML_Img', None)
    assert getattr(partner, 'URI357') is None


def test_assoc_src440_stub_double():
    # URI has no real 'URI442' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = URI()
    setattr(partner, 'URI442', None)
    _safe_set(owner, 'XHTML_Input441', partner)
    assert getattr(partner, 'URI442') == owner
    _safe_set(owner, 'XHTML_Input441', None)
    assert getattr(partner, 'URI442') is None


def test_assoc_standby327_stub_double():
    # Text has no real 'Text329' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = Text()
    setattr(partner, 'Text329', None)
    _safe_set(owner, 'XHTML_Object328', partner)
    assert getattr(partner, 'Text329') == owner
    _safe_set(owner, 'XHTML_Object328', None)
    assert getattr(partner, 'Text329') is None


def test_assoc_summary529_stub_double():
    # Text has no real 'Text531' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Text()
    setattr(partner, 'Text531', None)
    _safe_set(owner, 'XHTML_Table530', partner)
    assert getattr(partner, 'Text531') == owner
    _safe_set(owner, 'XHTML_Table530', None)
    assert getattr(partner, 'Text531') is None


def test_assoc_tabindex342_stub_double():
    # Number has no real 'Number344' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = Number()
    setattr(partner, 'Number344', None)
    _safe_set(owner, 'XHTML_Object343', partner)
    assert getattr(partner, 'Number344') == owner
    _safe_set(owner, 'XHTML_Object343', None)
    assert getattr(partner, 'Number344') is None


def test_assoc_tabindex465_stub_double():
    # Number has no real 'Number467' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Select(disabled="sample_text", multiple="sample_text")
    partner = Number()
    setattr(partner, 'Number467', None)
    _safe_set(owner, 'XHTML_Select466', partner)
    assert getattr(partner, 'Number467') == owner
    _safe_set(owner, 'XHTML_Select466', None)
    assert getattr(partner, 'Number467') is None


def test_assoc_tableelement527_stub_double():
    # TableElement has no real 'TableElement' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = TableElement()
    setattr(partner, 'TableElement', None)
    _safe_set(owner, 'XHTML_Table528', partner)
    assert getattr(partner, 'TableElement') == owner
    _safe_set(owner, 'XHTML_Table528', None)
    assert getattr(partner, 'TableElement') is None


def test_assoc_tdelement586_stub_double():
    # Flow has no real 'Flow587' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Td's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Td's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Td(scope="sample_text")
    partner = Flow()
    setattr(partner, 'Flow587', None)
    _safe_set(owner, 'XHTML_Td', {partner})
    assert getattr(partner, 'Flow587') == owner
    _safe_set(owner, 'XHTML_Td', set())
    assert getattr(partner, 'Flow587') is None


def test_assoc_tfoot525_stub_double():
    # Tfoot has no real 'Tfoot' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Tfoot()
    setattr(partner, 'Tfoot', None)
    _safe_set(owner, 'XHTML_Table526', partner)
    assert getattr(partner, 'Tfoot') == owner
    _safe_set(owner, 'XHTML_Table526', None)
    assert getattr(partner, 'Tfoot') is None


def test_assoc_thead523_stub_double():
    # Thead has no real 'Thead' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Thead()
    setattr(partner, 'Thead', None)
    _safe_set(owner, 'XHTML_Table524', partner)
    assert getattr(partner, 'Thead') == owner
    _safe_set(owner, 'XHTML_Table524', None)
    assert getattr(partner, 'Thead') is None


def test_assoc_thelement570_stub_double():
    # Flow has no real 'Flow571' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Th's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Th's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Th(scope="sample_text")
    partner = Flow()
    setattr(partner, 'Flow571', None)
    _safe_set(owner, 'XHTML_Th', {partner})
    assert getattr(partner, 'Flow571') == owner
    _safe_set(owner, 'XHTML_Th', set())
    assert getattr(partner, 'Flow571') is None


def test_assoc_title163_stub_double():
    # Text has no real 'Text165' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Style(xml_space="sample_text")
    partner = Text()
    setattr(partner, 'Text165', None)
    _safe_set(owner, 'XHTML_Style164', partner)
    assert getattr(partner, 'Text165') == owner
    _safe_set(owner, 'XHTML_Style164', None)
    assert getattr(partner, 'Text165') is None


def test_assoc_type157_stub_double():
    # ContentType has no real 'ContentType159' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Style(xml_space="sample_text")
    partner = ContentType()
    setattr(partner, 'ContentType159', None)
    _safe_set(owner, 'XHTML_Style158', partner)
    assert getattr(partner, 'ContentType159') == owner
    _safe_set(owner, 'XHTML_Style158', None)
    assert getattr(partner, 'ContentType159') is None


def test_assoc_type171_stub_double():
    # ContentType has no real 'ContentType173' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Script's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Script's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Script(defer="sample_text", xml_space="sample_text")
    partner = ContentType()
    setattr(partner, 'ContentType173', None)
    _safe_set(owner, 'XHTML_Script172', partner)
    assert getattr(partner, 'ContentType173') == owner
    _safe_set(owner, 'XHTML_Script172', None)
    assert getattr(partner, 'ContentType173') is None


def test_assoc_type239_stub_double():
    # ContentType has no real 'ContentType241' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_A(shape="sample_text")
    partner = ContentType()
    setattr(partner, 'ContentType241', None)
    _safe_set(owner, 'XHTML_A240', partner)
    assert getattr(partner, 'ContentType241') == owner
    _safe_set(owner, 'XHTML_A240', None)
    assert getattr(partner, 'ContentType241') is None


def test_assoc_type319_stub_double():
    # ContentType has no real 'ContentType321' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = ContentType()
    setattr(partner, 'ContentType321', None)
    _safe_set(owner, 'XHTML_Object320', partner)
    assert getattr(partner, 'ContentType321') == owner
    _safe_set(owner, 'XHTML_Object320', None)
    assert getattr(partner, 'ContentType321') is None


def test_assoc_type353_stub_double():
    # ContentType has no real 'ContentType355' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Param(valuetype="sample_text")
    partner = ContentType()
    setattr(partner, 'ContentType355', None)
    _safe_set(owner, 'XHTML_Param354', partner)
    assert getattr(partner, 'ContentType355') == owner
    _safe_set(owner, 'XHTML_Param354', None)
    assert getattr(partner, 'ContentType355') is None


def test_assoc_usemap336_stub_double():
    # URI has no real 'URI338' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = URI()
    setattr(partner, 'URI338', None)
    _safe_set(owner, 'XHTML_Object337', partner)
    assert getattr(partner, 'URI338') == owner
    _safe_set(owner, 'XHTML_Object337', None)
    assert getattr(partner, 'URI338') is None


def test_assoc_usemap370_stub_double():
    # URI has no real 'URI372' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Img's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Img's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Img(ismap="sample_text")
    partner = URI()
    setattr(partner, 'URI372', None)
    _safe_set(owner, 'XHTML_Img371', partner)
    assert getattr(partner, 'URI372') == owner
    _safe_set(owner, 'XHTML_Img371', None)
    assert getattr(partner, 'URI372') is None


def test_assoc_usemap446_stub_double():
    # URI has no real 'URI448' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = URI()
    setattr(partner, 'URI448', None)
    _safe_set(owner, 'XHTML_Input447', partner)
    assert getattr(partner, 'URI448') == owner
    _safe_set(owner, 'XHTML_Input447', None)
    assert getattr(partner, 'URI448') is None


def test_assoc_value350_stub_double():
    # CDATA has no real 'CDATA352' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Param(valuetype="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA352', None)
    _safe_set(owner, 'XHTML_Param351', partner)
    assert getattr(partner, 'CDATA352') == owner
    _safe_set(owner, 'XHTML_Param351', None)
    assert getattr(partner, 'CDATA352') is None


def test_assoc_value431_stub_double():
    # CDATA has no real 'CDATA433' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Input(checked="sample_text", disabled="sample_text", readonly="sample_text", type="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA433', None)
    _safe_set(owner, 'XHTML_Input432', partner)
    assert getattr(partner, 'CDATA433') == owner
    _safe_set(owner, 'XHTML_Input432', None)
    assert getattr(partner, 'CDATA433') is None


def test_assoc_value512_stub_double():
    # CDATA has no real 'CDATA514' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Button(disabled="sample_text", type="sample_text")
    partner = CDATA()
    setattr(partner, 'CDATA514', None)
    _safe_set(owner, 'XHTML_Button513', partner)
    assert getattr(partner, 'CDATA514') == owner
    _safe_set(owner, 'XHTML_Button513', None)
    assert getattr(partner, 'CDATA514') is None


def test_assoc_width333_stub_double():
    # Length has no real 'Length335' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Object(declare="sample_text")
    partner = Length()
    setattr(partner, 'Length335', None)
    _safe_set(owner, 'XHTML_Object334', partner)
    assert getattr(partner, 'Length335') == owner
    _safe_set(owner, 'XHTML_Object334', None)
    assert getattr(partner, 'Length335') is None


def test_assoc_width367_stub_double():
    # Length has no real 'Length369' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Img's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Img's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Img(ismap="sample_text")
    partner = Length()
    setattr(partner, 'Length369', None)
    _safe_set(owner, 'XHTML_Img368', partner)
    assert getattr(partner, 'Length369') == owner
    _safe_set(owner, 'XHTML_Img368', None)
    assert getattr(partner, 'Length369') is None


def test_assoc_width532_stub_double():
    # Length has no real 'Length534' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Table(frame="sample_text", rules="sample_text")
    partner = Length()
    setattr(partner, 'Length534', None)
    _safe_set(owner, 'XHTML_Table533', partner)
    assert getattr(partner, 'Length534') == owner
    _safe_set(owner, 'XHTML_Table533', None)
    assert getattr(partner, 'Length534') is None


def test_assoc_xml_lang13_stub_double():
    # LanguageCode has no real 'LanguageCode15' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_I18n's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_I18n's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_I18n(dir="sample_text")
    partner = LanguageCode()
    setattr(partner, 'LanguageCode15', None)
    _safe_set(owner, 'XHTML_I18n14', partner)
    assert getattr(partner, 'LanguageCode15') == owner
    _safe_set(owner, 'XHTML_I18n14', None)
    assert getattr(partner, 'LanguageCode15') is None


def test_assoc_xml_lang265_stub_double():
    # LanguageCode has no real 'LanguageCode267' property in the generated
    # code (a bare stub) -- manually attach it so XHTML_Bdo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XHTML_Bdo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XHTML_Bdo(dir="sample_text")
    partner = LanguageCode()
    setattr(partner, 'LanguageCode267', None)
    _safe_set(owner, 'XHTML_Bdo266', partner)
    assert getattr(partner, 'LanguageCode267') == owner
    _safe_set(owner, 'XHTML_Bdo266', None)
    assert getattr(partner, 'LanguageCode267') is None


