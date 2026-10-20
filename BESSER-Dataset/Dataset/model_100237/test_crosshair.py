from python_code import DatadiagramMLBasicDef_CellType

def test_DatadiagramMLBasicDef_CellType___init__():
    assert DatadiagramMLBasicDef_CellType.__init__(DatadiagramMLBasicDef_CellType('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ConnectsCollection
from python_code import DatadiagramMLBasicDef_Connect

def test_DatadiagramMLBasicDef_Connect___init__():
    assert DatadiagramMLBasicDef_Connect.__init__(DatadiagramMLBasicDef_Connect('', '', '', '', '', '', connections=ConnectsCollection()), '', '', '', '', '\x00', '', connections=ConnectsCollection()) == None


from python_code import CustomPropertiesCollection
from python_code import DatadiagramMLBasicDef_CustomProperty

def test_DatadiagramMLBasicDef_CustomProperty___init__():
    assert DatadiagramMLBasicDef_CustomProperty.__init__(DatadiagramMLBasicDef_CustomProperty('', '\x00', cps_customProps=CustomPropertiesCollection()), '\x00\x00', '', cps_customProps=CustomPropertiesCollection()) == None


from python_code import DatadiagramMLBasicDef_DateTimeType

def test_DatadiagramMLBasicDef_DateTimeType___init__():
    assert DatadiagramMLBasicDef_DateTimeType.__init__(DatadiagramMLBasicDef_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import DatadiagramMLBasicDef_DelElt

def test_DatadiagramMLBasicDef_DelElt___init__():
    assert DatadiagramMLBasicDef_DelElt.__init__(DatadiagramMLBasicDef_DelElt(''), '') == None


from python_code import CustomPropertiesCollection
from python_code import DatadiagramMLBasicDef_DocumentPropertiesCollection
from python_code import DateTimeType
from python_code import VisioDocument

def test_DatadiagramMLBasicDef_DocumentPropertiesCollection___init__():
    assert DatadiagramMLBasicDef_DocumentPropertiesCollection.__init__(DatadiagramMLBasicDef_DocumentPropertiesCollection('', '', '', '', '', '', '', '', '\x00', '', '', '', '', cps_docProp=CustomPropertiesCollection(), DatadiagramMLBasicDef_DocumentPropertiesCollection=DateTimeType(), DatadiagramMLBasicDef_DocumentPropertiesCollection21=DateTimeType(), DatadiagramMLBasicDef_DocumentPropertiesCollection24=DateTimeType(), docProps=VisioDocument(), DatadiagramMLBasicDef_DocumentPropertiesCollection27=DateTimeType()), '', '', '', '', '', '', '', '', '', '', '', '\x00', '', cps_docProp=CustomPropertiesCollection(), DatadiagramMLBasicDef_DocumentPropertiesCollection=DateTimeType(), DatadiagramMLBasicDef_DocumentPropertiesCollection21=DateTimeType(), DatadiagramMLBasicDef_DocumentPropertiesCollection24=DateTimeType(), docProps=VisioDocument(), DatadiagramMLBasicDef_DocumentPropertiesCollection27=DateTimeType()) == None


from python_code import DatadiagramMLBasicDef_EmailRoutingData
from python_code import VisioDocument

def test_DatadiagramMLBasicDef_EmailRoutingData___init__():
    assert DatadiagramMLBasicDef_EmailRoutingData.__init__(DatadiagramMLBasicDef_EmailRoutingData('', '\x00', docEmailRoutingData=VisioDocument()), '\x00\x00', '', docEmailRoutingData=VisioDocument()) == None


from python_code import DatadiagramMLBasicDef_IXElt

def test_DatadiagramMLBasicDef_IXElt___init__():
    assert DatadiagramMLBasicDef_IXElt.__init__(DatadiagramMLBasicDef_IXElt(''), '') == None


from python_code import DatadiagramMLBasicDef_Icon
from python_code import DatadiagramMLBasicDef_Master
from python_code import MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLBasicDef_Icon___init__():
    assert DatadiagramMLBasicDef_Icon.__init__(DatadiagramMLBasicDef_Icon('\x00', icons=MasterShortCut(), MasterElt=DatadiagramMLBasicDef_Master('\x00', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())), '', icons=MasterShortCut(), MasterElt=DatadiagramMLBasicDef_Master('', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())) == None


from python_code import DatadiagramMLBasicDef_IdentifiedElt

def test_DatadiagramMLBasicDef_IdentifiedElt___init__():
    assert DatadiagramMLBasicDef_IdentifiedElt.__init__(DatadiagramMLBasicDef_IdentifiedElt(''), '') == None


from python_code import DatadiagramMLBasicDef_Master
from python_code import MastersCollection

def test_DatadiagramMLBasicDef_Master___init__():
    assert DatadiagramMLBasicDef_Master.__init__(DatadiagramMLBasicDef_Master('', '', '\x00', '', '', '', '', '', masters=MastersCollection(), me_master=set()), '', '', '', '', '\x00', '', '', '', masters=MastersCollection(), me_master=set()) == None


from python_code import DatadiagramMLBasicDef_MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLBasicDef_MasterShortCut___init__():
    assert DatadiagramMLBasicDef_MasterShortCut.__init__(DatadiagramMLBasicDef_MasterShortCut('', '', '\x00', '', '', '', masterShortCuts=MastersCollection(), i_masterShortCut=set()), '', '', '', '', '', '', masterShortCuts=MastersCollection(), i_masterShortCut=set()) == None


from python_code import DatadiagramMLBasicDef_NamedElt

def test_DatadiagramMLBasicDef_NamedElt___init__():
    assert DatadiagramMLBasicDef_NamedElt.__init__(DatadiagramMLBasicDef_NamedElt('', '\x00'), '\x00\x00', '') == None


from python_code import DatadiagramMLBasicDef_Page
from python_code import PagesCollection

def test_DatadiagramMLBasicDef_Page___init__():
    assert DatadiagramMLBasicDef_Page.__init__(DatadiagramMLBasicDef_Page('', '', '', '', '\x00', '', '', pe_page=set(), pages=PagesCollection()), '', '', '', '', '', '', '', pe_page=set(), pages=PagesCollection()) == None


from python_code import DatadiagramMLBasicDef_Shape
from python_code import ShapesCollection

def test_DatadiagramMLBasicDef_Shape___init__():
    assert DatadiagramMLBasicDef_Shape.__init__(DatadiagramMLBasicDef_Shape('', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()), '', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()) == None


from python_code import DatadiagramMLBasicDef_StringElt
from python_code import DatadiagramMLBasicDef_Text

def test_DatadiagramMLBasicDef_StringElt___init__():
    assert DatadiagramMLBasicDef_StringElt.__init__(DatadiagramMLBasicDef_StringElt('', TextElt=DatadiagramMLBasicDef_Text()), '', TextElt=DatadiagramMLBasicDef_Text()) == None


from python_code import DatadiagramMLBasicDef_UniqueIdElt

def test_DatadiagramMLBasicDef_UniqueIdElt___init__():
    assert DatadiagramMLBasicDef_UniqueIdElt.__init__(DatadiagramMLBasicDef_UniqueIdElt(''), '') == None


from python_code import DatadiagramMLBasicDef_VBProjectData
from python_code import VisioDocument

def test_DatadiagramMLBasicDef_VBProjectData___init__():
    assert DatadiagramMLBasicDef_VBProjectData.__init__(DatadiagramMLBasicDef_VBProjectData('', docVBProjectData=VisioDocument()), '', docVBProjectData=VisioDocument()) == None


from python_code import ColorsTable
from python_code import DatadiagramMLBasicDef_VisioDocument
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

def test_DatadiagramMLBasicDef_VisioDocument___init__():
    assert DatadiagramMLBasicDef_VisioDocument.__init__(DatadiagramMLBasicDef_VisioDocument('', '', '\x00', '', '', '', ps_visioDocument10=PagesCollection(), el_visioDocument=EventList(), ef_visioDocument=HeaderFooter(), vpd_visioDocument=VBProjectData(), erd_visioDocument=EmailRoutingData(), sx_visioDocument=set(), dps_visioDocument=DocumentPropertiesCollection(), dss_visioDocument=DocumentSettingsElt(), cs_visioDocument=ColorsTable(), ps_visioDocument=PrintSetup(), fs_visioDocument=FontsTable(), fns_visioDocument=FaceNamesTable(), sss_visioDocument=StyleSheetsCollection(), ds_visioDocument=DocumentSheet(), ms_visioDocument=MastersCollection(), ws_visioDocument=WindowsInfo()), '', '', '', '', '', '', ps_visioDocument10=PagesCollection(), el_visioDocument=EventList(), ef_visioDocument=HeaderFooter(), vpd_visioDocument=VBProjectData(), erd_visioDocument=EmailRoutingData(), sx_visioDocument=set(), dps_visioDocument=DocumentPropertiesCollection(), dss_visioDocument=DocumentSettingsElt(), cs_visioDocument=ColorsTable(), ps_visioDocument=PrintSetup(), fs_visioDocument=FontsTable(), fns_visioDocument=FaceNamesTable(), sss_visioDocument=StyleSheetsCollection(), ds_visioDocument=DocumentSheet(), ms_visioDocument=MastersCollection(), ws_visioDocument=WindowsInfo()) == None

