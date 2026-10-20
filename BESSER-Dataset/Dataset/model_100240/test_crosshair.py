from python_code import DatadiagramMLXForm_CellType

def test_DatadiagramMLXForm_CellType___init__():
    assert DatadiagramMLXForm_CellType.__init__(DatadiagramMLXForm_CellType('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ColorsTable
from python_code import DatadiagramMLXForm_ColorEntry

def test_DatadiagramMLXForm_ColorEntry___init__():
    assert DatadiagramMLXForm_ColorEntry.__init__(DatadiagramMLXForm_ColorEntry('', colorEntries=ColorsTable()), '', colorEntries=ColorsTable()) == None


from python_code import ConnectsCollection
from python_code import DatadiagramMLXForm_Connect

def test_DatadiagramMLXForm_Connect___init__():
    assert DatadiagramMLXForm_Connect.__init__(DatadiagramMLXForm_Connect('', '', '', '', '', '', connections=ConnectsCollection()), '', '', '', '', '\x00', '', connections=ConnectsCollection()) == None


from python_code import CustomPropertiesCollection
from python_code import DatadiagramMLXForm_CustomProperty

def test_DatadiagramMLXForm_CustomProperty___init__():
    assert DatadiagramMLXForm_CustomProperty.__init__(DatadiagramMLXForm_CustomProperty('', '\x00', cps_customProps=CustomPropertiesCollection()), '\x00\x00', '', cps_customProps=CustomPropertiesCollection()) == None


from python_code import DatadiagramMLXForm_DateTimeType

def test_DatadiagramMLXForm_DateTimeType___init__():
    assert DatadiagramMLXForm_DateTimeType.__init__(DatadiagramMLXForm_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import DatadiagramMLXForm_DelElt

def test_DatadiagramMLXForm_DelElt___init__():
    assert DatadiagramMLXForm_DelElt.__init__(DatadiagramMLXForm_DelElt(''), '') == None


from python_code import CustomPropertiesCollection
from python_code import DatadiagramMLXForm_DocumentPropertiesCollection
from python_code import DateTimeType
from python_code import VisioDocument

def test_DatadiagramMLXForm_DocumentPropertiesCollection___init__():
    assert DatadiagramMLXForm_DocumentPropertiesCollection.__init__(DatadiagramMLXForm_DocumentPropertiesCollection('', '', '', '', '', '', '', '', '\x00', '', '', '', '', docProps=VisioDocument(), DatadiagramMLXForm_DocumentPropertiesCollection27=DateTimeType(), cps_docProp=CustomPropertiesCollection(), DatadiagramMLXForm_DocumentPropertiesCollection=DateTimeType(), DatadiagramMLXForm_DocumentPropertiesCollection21=DateTimeType(), DatadiagramMLXForm_DocumentPropertiesCollection24=DateTimeType()), '', '', '', '', '', '', '', '', '', '', '', '\x00', '', docProps=VisioDocument(), DatadiagramMLXForm_DocumentPropertiesCollection27=DateTimeType(), cps_docProp=CustomPropertiesCollection(), DatadiagramMLXForm_DocumentPropertiesCollection=DateTimeType(), DatadiagramMLXForm_DocumentPropertiesCollection21=DateTimeType(), DatadiagramMLXForm_DocumentPropertiesCollection24=DateTimeType()) == None


from python_code import DatadiagramMLXForm_DocumentSettingsElt
from python_code import Page
from python_code import SnapAnglesCollection
from python_code import StyleSheet
from python_code import VisioDocument

def test_DatadiagramMLXForm_DocumentSettingsElt___init__():
    assert DatadiagramMLXForm_DocumentSettingsElt.__init__(DatadiagramMLXForm_DocumentSettingsElt('\x00', '', '', '', '', '', '', '', '', '', '\x00', DatadiagramMLXForm_DocumentSettingsElt40=StyleSheet(), DatadiagramMLXForm_DocumentSettingsElt43=StyleSheet(), DatadiagramMLXForm_DocumentSettingsElt46=StyleSheet(), sa_docSettings=SnapAnglesCollection(), docSettings=VisioDocument(), DatadiagramMLXForm_DocumentSettingsElt=Page(), DatadiagramMLXForm_DocumentSettingsElt38=StyleSheet()), '', '', '', '', '', '', '', '', '', '', '', DatadiagramMLXForm_DocumentSettingsElt40=StyleSheet(), DatadiagramMLXForm_DocumentSettingsElt43=StyleSheet(), DatadiagramMLXForm_DocumentSettingsElt46=StyleSheet(), sa_docSettings=SnapAnglesCollection(), docSettings=VisioDocument(), DatadiagramMLXForm_DocumentSettingsElt=Page(), DatadiagramMLXForm_DocumentSettingsElt38=StyleSheet()) == None


from python_code import DatadiagramMLXForm_EmailRoutingData
from python_code import VisioDocument

def test_DatadiagramMLXForm_EmailRoutingData___init__():
    assert DatadiagramMLXForm_EmailRoutingData.__init__(DatadiagramMLXForm_EmailRoutingData('', '\x00', docEmailRoutingData=VisioDocument()), '\x00\x00', '', docEmailRoutingData=VisioDocument()) == None


from python_code import DatadiagramMLXForm_FaceName
from python_code import FaceNamesTable

def test_DatadiagramMLXForm_FaceName___init__():
    assert DatadiagramMLXForm_FaceName.__init__(DatadiagramMLXForm_FaceName('', '', '', '', '', faceNameEntries=FaceNamesTable()), '', '', '', '', '', faceNameEntries=FaceNamesTable()) == None


from python_code import DatadiagramMLXForm_FontEntry
from python_code import FontsTable

def test_DatadiagramMLXForm_FontEntry___init__():
    assert DatadiagramMLXForm_FontEntry.__init__(DatadiagramMLXForm_FontEntry('', '', '', '', '', '', fontEntries=FontsTable()), '', '', '', '', '\x00', '', fontEntries=FontsTable()) == None


from python_code import DatadiagramMLXForm_IXElt

def test_DatadiagramMLXForm_IXElt___init__():
    assert DatadiagramMLXForm_IXElt.__init__(DatadiagramMLXForm_IXElt(''), '') == None


from python_code import DatadiagramMLXForm_IXrequiredElt

def test_DatadiagramMLXForm_IXrequiredElt___init__():
    assert DatadiagramMLXForm_IXrequiredElt.__init__(DatadiagramMLXForm_IXrequiredElt(''), '') == None


from python_code import DatadiagramMLXForm_Icon
from python_code import DatadiagramMLXForm_Master
from python_code import MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLXForm_Icon___init__():
    assert DatadiagramMLXForm_Icon.__init__(DatadiagramMLXForm_Icon('\x00', icons=MasterShortCut(), MasterElt=DatadiagramMLXForm_Master('\x00', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())), '', icons=MasterShortCut(), MasterElt=DatadiagramMLXForm_Master('', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())) == None


from python_code import DatadiagramMLXForm_IdentifiedElt

def test_DatadiagramMLXForm_IdentifiedElt___init__():
    assert DatadiagramMLXForm_IdentifiedElt.__init__(DatadiagramMLXForm_IdentifiedElt(''), '') == None


from python_code import DatadiagramMLXForm_Master
from python_code import MastersCollection

def test_DatadiagramMLXForm_Master___init__():
    assert DatadiagramMLXForm_Master.__init__(DatadiagramMLXForm_Master('', '', '\x00', '', '', '', '', '', masters=MastersCollection(), me_master=set()), '', '', '', '', '\x00', '', '', '', masters=MastersCollection(), me_master=set()) == None


from python_code import DatadiagramMLXForm_MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLXForm_MasterShortCut___init__():
    assert DatadiagramMLXForm_MasterShortCut.__init__(DatadiagramMLXForm_MasterShortCut('', '', '\x00', '', '', '', i_masterShortCut=set(), masterShortCuts=MastersCollection()), '', '', '', '', '', '', i_masterShortCut=set(), masterShortCuts=MastersCollection()) == None


from python_code import DatadiagramMLXForm_NamedElt

def test_DatadiagramMLXForm_NamedElt___init__():
    assert DatadiagramMLXForm_NamedElt.__init__(DatadiagramMLXForm_NamedElt('', '\x00'), '\x00\x00', '') == None


from python_code import DatadiagramMLXForm_Page
from python_code import PagesCollection

def test_DatadiagramMLXForm_Page___init__():
    assert DatadiagramMLXForm_Page.__init__(DatadiagramMLXForm_Page('', '', '', '', '\x00', '', '', pages=PagesCollection(), pe_page=set()), '', '', '', '', '', '', '', pages=PagesCollection(), pe_page=set()) == None


from python_code import DatadiagramMLXForm_Shape
from python_code import ShapesCollection

def test_DatadiagramMLXForm_Shape___init__():
    assert DatadiagramMLXForm_Shape.__init__(DatadiagramMLXForm_Shape('', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()), '', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()) == None


from python_code import DatadiagramMLXForm_SnapAngle
from python_code import SnapAnglesCollection

def test_DatadiagramMLXForm_SnapAngle___init__():
    assert DatadiagramMLXForm_SnapAngle.__init__(DatadiagramMLXForm_SnapAngle('', snapAngles=SnapAnglesCollection()), '', snapAngles=SnapAnglesCollection()) == None


from python_code import DatadiagramMLXForm_StringElt
from python_code import DatadiagramMLXForm_Text

def test_DatadiagramMLXForm_StringElt___init__():
    assert DatadiagramMLXForm_StringElt.__init__(DatadiagramMLXForm_StringElt('', TextElt=DatadiagramMLXForm_Text()), '', TextElt=DatadiagramMLXForm_Text()) == None


from python_code import DatadiagramMLXForm_UniqueIdElt

def test_DatadiagramMLXForm_UniqueIdElt___init__():
    assert DatadiagramMLXForm_UniqueIdElt.__init__(DatadiagramMLXForm_UniqueIdElt(''), '') == None


from python_code import DatadiagramMLXForm_VBProjectData
from python_code import VisioDocument

def test_DatadiagramMLXForm_VBProjectData___init__():
    assert DatadiagramMLXForm_VBProjectData.__init__(DatadiagramMLXForm_VBProjectData('', docVBProjectData=VisioDocument()), '', docVBProjectData=VisioDocument()) == None


from python_code import ColorsTable
from python_code import DatadiagramMLXForm_VisioDocument
from python_code import DocumentPropertiesCollection
from python_code import DocumentSettingsElt
from python_code import DocumentSheet
from python_code import EmailRoutingData
from python_code import EventList
from python_code import FaceNamesTable
from python_code import FontsTable
from python_code import HeaderFooter
from python_code import MastersCollection
from python_code import PagesCollection
from python_code import PrintSetup
from python_code import StyleSheetsCollection
from python_code import VBProjectData
from python_code import WindowsInfo

def test_DatadiagramMLXForm_VisioDocument___init__():
    assert DatadiagramMLXForm_VisioDocument.__init__(DatadiagramMLXForm_VisioDocument('', '', '\x00', '', '', '', dss_visioDocument=DocumentSettingsElt(), cs_visioDocument=ColorsTable(), ps_visioDocument=PrintSetup(), fs_visioDocument=FontsTable(), fns_visioDocument=FaceNamesTable(), dps_visioDocument=DocumentPropertiesCollection(), erd_visioDocument=EmailRoutingData(), sx_visioDocument=set(), sss_visioDocument=StyleSheetsCollection(), ds_visioDocument=DocumentSheet(), ms_visioDocument=MastersCollection(), ps_visioDocument10=PagesCollection(), ws_visioDocument=WindowsInfo(), el_visioDocument=EventList(), ef_visioDocument=HeaderFooter(), vpd_visioDocument=VBProjectData()), '', '', '', '', '', '', dss_visioDocument=DocumentSettingsElt(), cs_visioDocument=ColorsTable(), ps_visioDocument=PrintSetup(), fs_visioDocument=FontsTable(), fns_visioDocument=FaceNamesTable(), dps_visioDocument=DocumentPropertiesCollection(), erd_visioDocument=EmailRoutingData(), sx_visioDocument=set(), sss_visioDocument=StyleSheetsCollection(), ds_visioDocument=DocumentSheet(), ms_visioDocument=MastersCollection(), ps_visioDocument10=PagesCollection(), ws_visioDocument=WindowsInfo(), el_visioDocument=EventList(), ef_visioDocument=HeaderFooter(), vpd_visioDocument=VBProjectData()) == None

