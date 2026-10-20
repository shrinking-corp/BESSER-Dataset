from python_code import Charset
from python_code import ContentType
from python_code import Coords
from python_code import LanguageCode
from python_code import LinkTypes
from python_code import NMTOKEN
from python_code import URI
from python_code import XHTML_A
from python_code import XHTML_Pre

def test_XHTML_A___init__():
    assert XHTML_A.__init__(XHTML_A('', XHTML_A=set(), XHTML_A237=Charset(), XHTML_A240=ContentType(), XHTML_A243=NMTOKEN(), XHTML_A245=URI(), XHTML_A248=LanguageCode(), XHTML_A251=LinkTypes(), XHTML_A254=LinkTypes(), XHTML_A257=Coords(), PreContent=XHTML_Pre('', XHTML_Pre=set())), '\x00', XHTML_A=set(), XHTML_A237=Charset(), XHTML_A240=ContentType(), XHTML_A243=NMTOKEN(), XHTML_A245=URI(), XHTML_A248=LanguageCode(), XHTML_A251=LinkTypes(), XHTML_A254=LinkTypes(), XHTML_A257=Coords(), PreContent=XHTML_Pre('', XHTML_Pre=set())) == None


from python_code import Coords
from python_code import Text
from python_code import URI
from python_code import XHTML_Area
from python_code import XHTML_MapContent

def test_XHTML_Area___init__():
    assert XHTML_Area.__init__(XHTML_Area('', '\x00', XHTML_Area=Coords(), XHTML_Area393=URI(), XHTML_Area396=Text(), MapElement=XHTML_MapContent()), '\x00\x00', '', XHTML_Area=Coords(), XHTML_Area393=URI(), XHTML_Area396=Text(), MapElement=XHTML_MapContent()) == None


from python_code import LanguageCode
from python_code import XHTML_Bdo

def test_XHTML_Bdo___init__():
    assert XHTML_Bdo.__init__(XHTML_Bdo('', XHTML_Bdo=set(), XHTML_Bdo263=LanguageCode(), XHTML_Bdo266=LanguageCode()), '', XHTML_Bdo=set(), XHTML_Bdo263=LanguageCode(), XHTML_Bdo266=LanguageCode()) == None


from python_code import CDATA
from python_code import XHTML_Button
from python_code import XHTML_URI

def test_XHTML_Button___init__():
    assert XHTML_Button.__init__(XHTML_Button('', '', XHTML_Button=set(), XHTML_Button510=CDATA(), XHTML_Button513=XHTML_URI()), '', '', XHTML_Button=set(), XHTML_Button510=CDATA(), XHTML_Button513=CDATA()) == None


from python_code import Character
from python_code import Length
from python_code import XHTML_Cellhalign

def test_XHTML_Cellhalign___init__():
    assert XHTML_Cellhalign.__init__(XHTML_Cellhalign('', XHTML_Cellhalign=Character(), XHTML_Cellhalign518=Length()), '', XHTML_Cellhalign=Character(), XHTML_Cellhalign518=Length()) == None


from python_code import XHTML_Cellvalign

def test_XHTML_Cellvalign___init__():
    assert XHTML_Cellvalign.__init__(XHTML_Cellvalign(''), '') == None


from python_code import Charsets
from python_code import ContentType
from python_code import ContentTypes
from python_code import Length
from python_code import NMTOKEN
from python_code import Number
from python_code import ScriptExpression
from python_code import Text
from python_code import URI
from python_code import UriList
from python_code import XHTML_BaseHeadElement
from python_code import XHTML_BaseTitleHeadElement
from python_code import XHTML_Blockquote
from python_code import XHTML_Body
from python_code import XHTML_Fieldset
from python_code import XHTML_Form
from python_code import XHTML_Head
from python_code import XHTML_Noscript
from python_code import XHTML_Object
from python_code import XHTML_TitleBaseHeadElement
from python_code import XHTML_TitleHeadElement

def test_XHTML_Form___init__():
    assert XHTML_Form.__init__(XHTML_Form('', XHTML_Form400=URI(), XHTML_Form403=ContentType(), XHTML_Form406=ScriptExpression(), XHTML_Form409=ScriptExpression(), XHTML_Form412=ContentTypes(), XHTML_Form414=Charsets(), XHTML_Form=set(), Block=XHTML_Noscript(), Block216=XHTML_Blockquote(), Block179=XHTML_Body(), ObjectElement=XHTML_Object('', XHTML_Object311=URI(), XHTML_Object314=URI(), XHTML_Object317=URI(), XHTML_Object320=ContentType(), XHTML_Object323=ContentType(), XHTML_Object326=UriList(), XHTML_Object328=Text(), XHTML_Object334=Length(), XHTML_Object337=URI(), XHTML_Object340=NMTOKEN(), XHTML_Object343=Number(), XHTML_Object331=Length(), XHTML_Object=set(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()), FieldsetElement=XHTML_Fieldset()), '', XHTML_Form400=URI(), XHTML_Form403=ContentType(), XHTML_Form406=ScriptExpression(), XHTML_Form409=ScriptExpression(), XHTML_Form412=ContentTypes(), XHTML_Form414=Charsets(), XHTML_Form=set(), Block=XHTML_Noscript(), Block216=XHTML_Blockquote(), Block179=XHTML_Body(), ObjectElement=XHTML_Object('', XHTML_Object311=URI(), XHTML_Object314=URI(), XHTML_Object317=URI(), XHTML_Object320=ContentType(), XHTML_Object323=ContentType(), XHTML_Object326=UriList(), XHTML_Object328=Text(), XHTML_Object334=Length(), XHTML_Object337=URI(), XHTML_Object340=NMTOKEN(), XHTML_Object343=Number(), XHTML_Object331=Length(), XHTML_Object=set(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()), FieldsetElement=XHTML_Fieldset()) == None


from python_code import LanguageCode
from python_code import XHTML_I18n

def test_XHTML_I18n___init__():
    assert XHTML_I18n.__init__(XHTML_I18n('', XHTML_I18n=LanguageCode(), XHTML_I18n14=LanguageCode()), '', XHTML_I18n=LanguageCode(), XHTML_I18n14=LanguageCode()) == None


from python_code import Length
from python_code import Text
from python_code import URI
from python_code import XHTML_Img

def test_XHTML_Img___init__():
    assert XHTML_Img.__init__(XHTML_Img('', XHTML_Img=URI(), XHTML_Img359=Text(), XHTML_Img362=URI(), XHTML_Img365=Length(), XHTML_Img368=Length(), XHTML_Img371=URI()), '', XHTML_Img=URI(), XHTML_Img359=Text(), XHTML_Img362=URI(), XHTML_Img365=Length(), XHTML_Img368=Length(), XHTML_Img371=URI()) == None


from python_code import CDATA
from python_code import ContentTypes
from python_code import Number
from python_code import ScriptExpression
from python_code import URI
from python_code import XHTML_Input
from python_code import XHTML_URI

def test_XHTML_Input___init__():
    assert XHTML_Input.__init__(XHTML_Input('', '', '', '', XHTML_Input453=ScriptExpression(), XHTML_Input456=ContentTypes(), XHTML_Input435=XHTML_URI(), XHTML_Input438=Number(), XHTML_Input441=URI(), XHTML_Input444=CDATA(), XHTML_Input=CDATA(), XHTML_Input432=CDATA(), XHTML_Input447=URI(), XHTML_Input450=ScriptExpression()), '', '', '', '', XHTML_Input453=ScriptExpression(), XHTML_Input456=ContentTypes(), XHTML_Input435=CDATA(), XHTML_Input438=Number(), XHTML_Input441=URI(), XHTML_Input444=CDATA(), XHTML_Input=CDATA(), XHTML_Input432=CDATA(), XHTML_Input447=URI(), XHTML_Input450=ScriptExpression()) == None


from python_code import ContentType
from python_code import Length
from python_code import NMTOKEN
from python_code import Number
from python_code import Text
from python_code import URI
from python_code import UriList
from python_code import XHTML_BaseHeadElement
from python_code import XHTML_BaseTitleHeadElement
from python_code import XHTML_Head
from python_code import XHTML_Object
from python_code import XHTML_TitleBaseHeadElement
from python_code import XHTML_TitleHeadElement

def test_XHTML_Object___init__():
    assert XHTML_Object.__init__(XHTML_Object('', XHTML_Object311=URI(), XHTML_Object314=URI(), XHTML_Object317=URI(), XHTML_Object320=ContentType(), XHTML_Object323=ContentType(), XHTML_Object326=UriList(), XHTML_Object328=Text(), XHTML_Object334=Length(), XHTML_Object337=URI(), XHTML_Object340=NMTOKEN(), XHTML_Object343=Number(), XHTML_Object331=Length(), XHTML_Object=set(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()), '', XHTML_Object311=URI(), XHTML_Object314=URI(), XHTML_Object317=URI(), XHTML_Object320=ContentType(), XHTML_Object323=ContentType(), XHTML_Object326=UriList(), XHTML_Object328=Text(), XHTML_Object334=Length(), XHTML_Object337=URI(), XHTML_Object340=NMTOKEN(), XHTML_Object343=Number(), XHTML_Object331=Length(), XHTML_Object=set(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()) == None


from python_code import CDATA
from python_code import Number
from python_code import ScriptExpression
from python_code import Text
from python_code import XHTML_Optgroup
from python_code import XHTML_Select

def test_XHTML_Optgroup___init__():
    assert XHTML_Optgroup.__init__(XHTML_Optgroup('', XHTML_Optgroup=set(), XHTML_Optgroup479=Text(), SelectElement=XHTML_Select('', '', XHTML_Select=set(), XHTML_Select460=CDATA(), XHTML_Select463=Number(), XHTML_Select466=Number(), XHTML_Select469=ScriptExpression(), XHTML_Select472=ScriptExpression(), XHTML_Select475=ScriptExpression())), '\x00', XHTML_Optgroup=set(), XHTML_Optgroup479=Text(), SelectElement=XHTML_Select('', '', XHTML_Select=set(), XHTML_Select460=CDATA(), XHTML_Select463=Number(), XHTML_Select466=Number(), XHTML_Select469=ScriptExpression(), XHTML_Select472=ScriptExpression(), XHTML_Select475=ScriptExpression())) == None


from python_code import CDATA
from python_code import Number
from python_code import ScriptExpression
from python_code import Text
from python_code import XHTML_AContent
from python_code import XHTML_ButtonContent
from python_code import XHTML_FieldsetElement
from python_code import XHTML_Flow
from python_code import XHTML_Inline
from python_code import XHTML_ObjectElement
from python_code import XHTML_Option
from python_code import XHTML_PreContent
from python_code import XHTML_Select

def test_XHTML_Option___init__():
    assert XHTML_Option.__init__(XHTML_Option('', '', XHTML_Option=Text(), XHTML_Option484=CDATA(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement(), SelectElement=XHTML_Select('', '', XHTML_Select=set(), XHTML_Select460=CDATA(), XHTML_Select463=Number(), XHTML_Select466=Number(), XHTML_Select469=ScriptExpression(), XHTML_Select472=ScriptExpression(), XHTML_Select475=ScriptExpression())), '', '', XHTML_Option=Text(), XHTML_Option484=CDATA(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement(), SelectElement=XHTML_Select('', '', XHTML_Select=set(), XHTML_Select460=CDATA(), XHTML_Select463=Number(), XHTML_Select466=Number(), XHTML_Select469=ScriptExpression(), XHTML_Select472=ScriptExpression(), XHTML_Select475=ScriptExpression())) == None


from python_code import CDATA
from python_code import ContentType
from python_code import ID
from python_code import Length
from python_code import NMTOKEN
from python_code import Number
from python_code import Text
from python_code import URI
from python_code import UriList
from python_code import XHTML_BaseHeadElement
from python_code import XHTML_BaseTitleHeadElement
from python_code import XHTML_Head
from python_code import XHTML_Object
from python_code import XHTML_Param
from python_code import XHTML_TitleBaseHeadElement
from python_code import XHTML_TitleHeadElement

def test_XHTML_Param___init__():
    assert XHTML_Param.__init__(XHTML_Param('', XHTML_Param=ID(), XHTML_Param348=CDATA(), XHTML_Param351=CDATA(), XHTML_Param354=ContentType(), ObjectElement=XHTML_Object('', XHTML_Object311=URI(), XHTML_Object314=URI(), XHTML_Object317=URI(), XHTML_Object320=ContentType(), XHTML_Object323=ContentType(), XHTML_Object326=UriList(), XHTML_Object328=Text(), XHTML_Object334=Length(), XHTML_Object337=URI(), XHTML_Object340=NMTOKEN(), XHTML_Object343=Number(), XHTML_Object331=Length(), XHTML_Object=set(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement())), '', XHTML_Param=ID(), XHTML_Param348=CDATA(), XHTML_Param351=CDATA(), XHTML_Param354=ContentType(), ObjectElement=XHTML_Object('', XHTML_Object311=URI(), XHTML_Object314=URI(), XHTML_Object317=URI(), XHTML_Object320=ContentType(), XHTML_Object323=ContentType(), XHTML_Object326=UriList(), XHTML_Object328=Text(), XHTML_Object334=Length(), XHTML_Object337=URI(), XHTML_Object340=NMTOKEN(), XHTML_Object343=Number(), XHTML_Object331=Length(), XHTML_Object=set(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement())) == None


from python_code import XHTML_Pre

def test_XHTML_Pre___init__():
    assert XHTML_Pre.__init__(XHTML_Pre('', XHTML_Pre=set()), '', XHTML_Pre=set()) == None


from python_code import Charset
from python_code import ContentType
from python_code import ID
from python_code import URI
from python_code import XHTML_AContent
from python_code import XHTML_BaseHeadElement
from python_code import XHTML_BaseTitleHeadElement
from python_code import XHTML_ButtonContent
from python_code import XHTML_FieldsetElement
from python_code import XHTML_Flow
from python_code import XHTML_Head
from python_code import XHTML_Inline
from python_code import XHTML_ObjectElement
from python_code import XHTML_PreContent
from python_code import XHTML_Script
from python_code import XHTML_TitleBaseHeadElement
from python_code import XHTML_TitleHeadElement

def test_XHTML_Script___init__():
    assert XHTML_Script.__init__(XHTML_Script('', '\x00', XHTML_Script175=URI(), XHTML_Script=ID(), XHTML_Script169=Charset(), XHTML_Script172=ContentType(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()), '\x00\x00', '', XHTML_Script175=URI(), XHTML_Script=ID(), XHTML_Script169=Charset(), XHTML_Script172=ContentType(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()) == None


from python_code import CDATA
from python_code import Number
from python_code import ScriptExpression
from python_code import XHTML_Select

def test_XHTML_Select___init__():
    assert XHTML_Select.__init__(XHTML_Select('', '', XHTML_Select=set(), XHTML_Select460=CDATA(), XHTML_Select463=Number(), XHTML_Select466=Number(), XHTML_Select469=ScriptExpression(), XHTML_Select472=ScriptExpression(), XHTML_Select475=ScriptExpression()), '', '', XHTML_Select=set(), XHTML_Select460=CDATA(), XHTML_Select463=Number(), XHTML_Select466=Number(), XHTML_Select469=ScriptExpression(), XHTML_Select472=ScriptExpression(), XHTML_Select475=ScriptExpression()) == None


from python_code import ContentType
from python_code import I18n
from python_code import ID
from python_code import MediaDesc
from python_code import Text
from python_code import XHTML_AContent
from python_code import XHTML_BaseHeadElement
from python_code import XHTML_BaseTitleHeadElement
from python_code import XHTML_ButtonContent
from python_code import XHTML_FieldsetElement
from python_code import XHTML_Flow
from python_code import XHTML_Head
from python_code import XHTML_Inline
from python_code import XHTML_ObjectElement
from python_code import XHTML_PreContent
from python_code import XHTML_Style
from python_code import XHTML_TitleBaseHeadElement
from python_code import XHTML_TitleHeadElement

def test_XHTML_Style___init__():
    assert XHTML_Style.__init__(XHTML_Style('', XHTML_Style=I18n(), XHTML_Style155=ID(), XHTML_Style158=ContentType(), XHTML_Style161=MediaDesc(), XHTML_Style164=Text(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()), '\x00', XHTML_Style=I18n(), XHTML_Style155=ID(), XHTML_Style158=ContentType(), XHTML_Style161=MediaDesc(), XHTML_Style164=Text(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement(), HeadMisc99=XHTML_BaseHeadElement(), HeadMisc=XHTML_Head(), HeadMisc106=XHTML_TitleBaseHeadElement(), HeadMisc94=XHTML_BaseTitleHeadElement(), HeadMisc88=XHTML_TitleHeadElement()) == None


from python_code import CDATA
from python_code import ColElement
from python_code import Length
from python_code import Pixels
from python_code import TableElement
from python_code import Text
from python_code import Tfoot
from python_code import Thead
from python_code import XHTML_Button
from python_code import XHTML_Table

def test_XHTML_Table___init__():
    assert XHTML_Table.__init__(XHTML_Table('', '', XHTML_Table=set(), XHTML_Table522=ColElement(), XHTML_Table524=Thead(), XHTML_Table526=Tfoot(), XHTML_Table528=TableElement(), XHTML_Table530=Text(), XHTML_Table538=Length(), XHTML_Table541=Length(), XHTML_Table533=Length(), XHTML_Table536=Pixels(), ButtonContent=XHTML_Button('', '', XHTML_Button=set(), XHTML_Button510=CDATA(), XHTML_Button513=CDATA())), '', '', XHTML_Table=set(), XHTML_Table522=ColElement(), XHTML_Table524=Thead(), XHTML_Table526=Tfoot(), XHTML_Table528=TableElement(), XHTML_Table530=Text(), XHTML_Table538=Length(), XHTML_Table541=Length(), XHTML_Table533=Length(), XHTML_Table536=Pixels(), ButtonContent=XHTML_Button('', '', XHTML_Button=set(), XHTML_Button510=CDATA(), XHTML_Button513=CDATA())) == None


from python_code import CDATA
from python_code import IDREFS
from python_code import Number
from python_code import Text
from python_code import XHTML_Td
from python_code import XHTML_Tr

def test_XHTML_Td___init__():
    assert XHTML_Td.__init__(XHTML_Td('', XHTML_Td592=CDATA(), XHTML_Td=set(), XHTML_Td589=Text(), XHTML_Td595=IDREFS(), XHTML_Td598=Number(), XHTML_Td601=Number(), TrElement=XHTML_Tr()), '', XHTML_Td592=CDATA(), XHTML_Td=set(), XHTML_Td589=Text(), XHTML_Td595=IDREFS(), XHTML_Td598=Number(), XHTML_Td601=Number(), TrElement=XHTML_Tr()) == None


from python_code import CDATA
from python_code import Number
from python_code import ScriptExpression
from python_code import XHTML_AContent
from python_code import XHTML_ButtonContent
from python_code import XHTML_FieldsetElement
from python_code import XHTML_Flow
from python_code import XHTML_Inline
from python_code import XHTML_ObjectElement
from python_code import XHTML_PreContent
from python_code import XHTML_Textarea
from python_code import XHTML_URI

def test_XHTML_Textarea___init__():
    assert XHTML_Textarea.__init__(XHTML_Textarea('', '', XHTML_Textarea=XHTML_URI(), XHTML_Textarea489=Number(), XHTML_Textarea492=Number(), XHTML_Textarea495=ScriptExpression(), XHTML_Textarea498=ScriptExpression(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement()), '', '', XHTML_Textarea=CDATA(), XHTML_Textarea489=Number(), XHTML_Textarea492=Number(), XHTML_Textarea495=ScriptExpression(), XHTML_Textarea498=ScriptExpression(), PCDATA55=XHTML_Flow(), PCDATA=XHTML_Inline(), PCDATA308=XHTML_ObjectElement(), PCDATA61=XHTML_ButtonContent(), PCDATA57=XHTML_AContent(), PCDATA59=XHTML_PreContent(), PCDATA501=XHTML_FieldsetElement()) == None


from python_code import CDATA
from python_code import IDREFS
from python_code import Number
from python_code import Text
from python_code import XHTML_Th
from python_code import XHTML_Tr

def test_XHTML_Th___init__():
    assert XHTML_Th.__init__(XHTML_Th('', XHTML_Th=set(), XHTML_Th573=Text(), XHTML_Th576=CDATA(), XHTML_Th579=IDREFS(), XHTML_Th581=Number(), XHTML_Th584=Number(), TrElement=XHTML_Tr()), '', XHTML_Th=set(), XHTML_Th573=Text(), XHTML_Th576=CDATA(), XHTML_Th579=IDREFS(), XHTML_Th581=Number(), XHTML_Th584=Number(), TrElement=XHTML_Tr()) == None


from python_code import XHTML_ValuedElement

def test_XHTML_ValuedElement___init__():
    assert XHTML_ValuedElement.__init__(XHTML_ValuedElement(''), '') == None

