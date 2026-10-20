from python_code import DatadiagramMLTextFormat_CellType

def test_DatadiagramMLTextFormat_CellType___init__():
    assert DatadiagramMLTextFormat_CellType.__init__(DatadiagramMLTextFormat_CellType('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ColorsTable
from python_code import DatadiagramMLTextFormat_ColorEntry

def test_DatadiagramMLTextFormat_ColorEntry___init__():
    assert DatadiagramMLTextFormat_ColorEntry.__init__(DatadiagramMLTextFormat_ColorEntry('', colorEntries=ColorsTable()), '', colorEntries=ColorsTable()) == None


from python_code import ConnectsCollection
from python_code import DatadiagramMLTextFormat_Connect

def test_DatadiagramMLTextFormat_Connect___init__():
    assert DatadiagramMLTextFormat_Connect.__init__(DatadiagramMLTextFormat_Connect('', '', '', '', '', '', connections=ConnectsCollection()), '', '', '', '', '\x00', '', connections=ConnectsCollection()) == None


from python_code import CustomPropertiesCollection
from python_code import DatadiagramMLTextFormat_CustomProperty

def test_DatadiagramMLTextFormat_CustomProperty___init__():
    assert DatadiagramMLTextFormat_CustomProperty.__init__(DatadiagramMLTextFormat_CustomProperty('', '\x00', cps_customProps=CustomPropertiesCollection()), '\x00\x00', '', cps_customProps=CustomPropertiesCollection()) == None


from python_code import DatadiagramMLTextFormat_DateTimeType

def test_DatadiagramMLTextFormat_DateTimeType___init__():
    assert DatadiagramMLTextFormat_DateTimeType.__init__(DatadiagramMLTextFormat_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import DatadiagramMLTextFormat_DelElt

def test_DatadiagramMLTextFormat_DelElt___init__():
    assert DatadiagramMLTextFormat_DelElt.__init__(DatadiagramMLTextFormat_DelElt(''), '') == None


from python_code import CustomPropertiesCollection
from python_code import DatadiagramMLTextFormat_DocumentPropertiesCollection
from python_code import DateTimeType
from python_code import VisioDocument

def test_DatadiagramMLTextFormat_DocumentPropertiesCollection___init__():
    assert DatadiagramMLTextFormat_DocumentPropertiesCollection.__init__(DatadiagramMLTextFormat_DocumentPropertiesCollection('', '', '', '', '', '', '', '', '\x00', '', '', '', '', docProps=VisioDocument(), cps_docProp=CustomPropertiesCollection(), DatadiagramMLTextFormat_DocumentPropertiesCollection=DateTimeType(), DatadiagramMLTextFormat_DocumentPropertiesCollection21=DateTimeType(), DatadiagramMLTextFormat_DocumentPropertiesCollection24=DateTimeType(), DatadiagramMLTextFormat_DocumentPropertiesCollection27=DateTimeType()), '', '', '', '', '', '', '', '', '', '', '', '\x00', '', docProps=VisioDocument(), cps_docProp=CustomPropertiesCollection(), DatadiagramMLTextFormat_DocumentPropertiesCollection=DateTimeType(), DatadiagramMLTextFormat_DocumentPropertiesCollection21=DateTimeType(), DatadiagramMLTextFormat_DocumentPropertiesCollection24=DateTimeType(), DatadiagramMLTextFormat_DocumentPropertiesCollection27=DateTimeType()) == None


from python_code import DatadiagramMLTextFormat_EmailRoutingData
from python_code import VisioDocument

def test_DatadiagramMLTextFormat_EmailRoutingData___init__():
    assert DatadiagramMLTextFormat_EmailRoutingData.__init__(DatadiagramMLTextFormat_EmailRoutingData('', '\x00', docEmailRoutingData=VisioDocument()), '\x00\x00', '', docEmailRoutingData=VisioDocument()) == None


from python_code import DatadiagramMLTextFormat_FaceName
from python_code import FaceNamesTable

def test_DatadiagramMLTextFormat_FaceName___init__():
    assert DatadiagramMLTextFormat_FaceName.__init__(DatadiagramMLTextFormat_FaceName('', '', '', '', '', faceNameEntries=FaceNamesTable()), '', '', '', '', '', faceNameEntries=FaceNamesTable()) == None


from python_code import DatadiagramMLTextFormat_FontEntry
from python_code import FontsTable

def test_DatadiagramMLTextFormat_FontEntry___init__():
    assert DatadiagramMLTextFormat_FontEntry.__init__(DatadiagramMLTextFormat_FontEntry('', '', '', '', '', '', fontEntries=FontsTable()), '', '', '', '', '\x00', '', fontEntries=FontsTable()) == None


from python_code import DatadiagramMLTextFormat_IXElt

def test_DatadiagramMLTextFormat_IXElt___init__():
    assert DatadiagramMLTextFormat_IXElt.__init__(DatadiagramMLTextFormat_IXElt(''), '') == None


from python_code import DatadiagramMLTextFormat_IXrequiredElt

def test_DatadiagramMLTextFormat_IXrequiredElt___init__():
    assert DatadiagramMLTextFormat_IXrequiredElt.__init__(DatadiagramMLTextFormat_IXrequiredElt(''), '') == None


from python_code import DatadiagramMLTextFormat_Icon
from python_code import DatadiagramMLTextFormat_Master
from python_code import MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLTextFormat_Icon___init__():
    assert DatadiagramMLTextFormat_Icon.__init__(DatadiagramMLTextFormat_Icon('\x00', icons=MasterShortCut(), MasterElt=DatadiagramMLTextFormat_Master('\x00', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())), '', icons=MasterShortCut(), MasterElt=DatadiagramMLTextFormat_Master('', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())) == None


from python_code import DatadiagramMLTextFormat_IdentifiedElt

def test_DatadiagramMLTextFormat_IdentifiedElt___init__():
    assert DatadiagramMLTextFormat_IdentifiedElt.__init__(DatadiagramMLTextFormat_IdentifiedElt(''), '') == None


from python_code import DatadiagramMLTextFormat_Master
from python_code import MastersCollection

def test_DatadiagramMLTextFormat_Master___init__():
    assert DatadiagramMLTextFormat_Master.__init__(DatadiagramMLTextFormat_Master('', '', '\x00', '', '', '', '', '', masters=MastersCollection(), me_master=set()), '', '', '', '', '\x00', '', '', '', masters=MastersCollection(), me_master=set()) == None


from python_code import DatadiagramMLTextFormat_MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLTextFormat_MasterShortCut___init__():
    assert DatadiagramMLTextFormat_MasterShortCut.__init__(DatadiagramMLTextFormat_MasterShortCut('', '', '\x00', '', '', '', masterShortCuts=MastersCollection(), i_masterShortCut=set()), '', '', '', '', '', '', masterShortCuts=MastersCollection(), i_masterShortCut=set()) == None


from python_code import DatadiagramMLTextFormat_NamedElt

def test_DatadiagramMLTextFormat_NamedElt___init__():
    assert DatadiagramMLTextFormat_NamedElt.__init__(DatadiagramMLTextFormat_NamedElt('', '\x00'), '\x00\x00', '') == None


from python_code import DatadiagramMLTextFormat_Page
from python_code import PagesCollection

def test_DatadiagramMLTextFormat_Page___init__():
    assert DatadiagramMLTextFormat_Page.__init__(DatadiagramMLTextFormat_Page('', '', '', '', '\x00', '', '', pages=PagesCollection(), pe_page=set()), '', '', '', '', '', '', '', pages=PagesCollection(), pe_page=set()) == None


from python_code import DatadiagramMLTextFormat_Shape
from python_code import ShapesCollection

def test_DatadiagramMLTextFormat_Shape___init__():
    assert DatadiagramMLTextFormat_Shape.__init__(DatadiagramMLTextFormat_Shape('', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()), '', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()) == None


from python_code import DatadiagramMLTextFormat_StringElt
from python_code import DatadiagramMLTextFormat_Text

def test_DatadiagramMLTextFormat_StringElt___init__():
    assert DatadiagramMLTextFormat_StringElt.__init__(DatadiagramMLTextFormat_StringElt('', TextElt=DatadiagramMLTextFormat_Text()), '', TextElt=DatadiagramMLTextFormat_Text()) == None


from python_code import DatadiagramMLTextFormat_UniqueIdElt

def test_DatadiagramMLTextFormat_UniqueIdElt___init__():
    assert DatadiagramMLTextFormat_UniqueIdElt.__init__(DatadiagramMLTextFormat_UniqueIdElt(''), '') == None


from python_code import DatadiagramMLTextFormat_VBProjectData
from python_code import VisioDocument

def test_DatadiagramMLTextFormat_VBProjectData___init__():
    assert DatadiagramMLTextFormat_VBProjectData.__init__(DatadiagramMLTextFormat_VBProjectData('', docVBProjectData=VisioDocument()), '', docVBProjectData=VisioDocument()) == None


from python_code import ColorsTable
from python_code import DatadiagramMLTextFormat_VisioDocument
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

def test_DatadiagramMLTextFormat_VisioDocument___init__():
    assert DatadiagramMLTextFormat_VisioDocument.__init__(DatadiagramMLTextFormat_VisioDocument('', '', '\x00', '', '', '', dps_visioDocument=DocumentPropertiesCollection(), dss_visioDocument=DocumentSettingsElt(), sss_visioDocument=StyleSheetsCollection(), ds_visioDocument=DocumentSheet(), ms_visioDocument=MastersCollection(), ps_visioDocument10=PagesCollection(), ws_visioDocument=WindowsInfo(), el_visioDocument=EventList(), ef_visioDocument=HeaderFooter(), vpd_visioDocument=VBProjectData(), erd_visioDocument=EmailRoutingData(), sx_visioDocument=set(), cs_visioDocument=ColorsTable(), ps_visioDocument=PrintSetup(), fs_visioDocument=FontsTable(), fns_visioDocument=FaceNamesTable()), '', '', '', '', '', '', dps_visioDocument=DocumentPropertiesCollection(), dss_visioDocument=DocumentSettingsElt(), sss_visioDocument=StyleSheetsCollection(), ds_visioDocument=DocumentSheet(), ms_visioDocument=MastersCollection(), ps_visioDocument10=PagesCollection(), ws_visioDocument=WindowsInfo(), el_visioDocument=EventList(), ef_visioDocument=HeaderFooter(), vpd_visioDocument=VBProjectData(), erd_visioDocument=EmailRoutingData(), sx_visioDocument=set(), cs_visioDocument=ColorsTable(), ps_visioDocument=PrintSetup(), fs_visioDocument=FontsTable(), fns_visioDocument=FaceNamesTable()) == None

