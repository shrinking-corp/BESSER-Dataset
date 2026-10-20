from python_code import DatadiagramMLSimplified_CellType

def test_DatadiagramMLSimplified_CellType___init__():
    assert DatadiagramMLSimplified_CellType.__init__(DatadiagramMLSimplified_CellType('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ConnectsCollection
from python_code import DatadiagramMLSimplified_Connect

def test_DatadiagramMLSimplified_Connect___init__():
    assert DatadiagramMLSimplified_Connect.__init__(DatadiagramMLSimplified_Connect('', '', '', '', '', '', connections=ConnectsCollection()), '', '', '', '', '\x00', '', connections=ConnectsCollection()) == None


from python_code import DatadiagramMLSimplified_DelElt

def test_DatadiagramMLSimplified_DelElt___init__():
    assert DatadiagramMLSimplified_DelElt.__init__(DatadiagramMLSimplified_DelElt(''), '') == None


from python_code import DatadiagramMLSimplified_IXElt

def test_DatadiagramMLSimplified_IXElt___init__():
    assert DatadiagramMLSimplified_IXElt.__init__(DatadiagramMLSimplified_IXElt(''), '') == None


from python_code import DatadiagramMLSimplified_Icon
from python_code import DatadiagramMLSimplified_Master
from python_code import MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLSimplified_Icon___init__():
    assert DatadiagramMLSimplified_Icon.__init__(DatadiagramMLSimplified_Icon('\x00', icons=MasterShortCut(), MasterElt=DatadiagramMLSimplified_Master('\x00', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())), '', icons=MasterShortCut(), MasterElt=DatadiagramMLSimplified_Master('', '', '', '', '', '', '', '', masters=MastersCollection(), me_master=set())) == None


from python_code import DatadiagramMLSimplified_IdentifiedElt

def test_DatadiagramMLSimplified_IdentifiedElt___init__():
    assert DatadiagramMLSimplified_IdentifiedElt.__init__(DatadiagramMLSimplified_IdentifiedElt(''), '') == None


from python_code import DatadiagramMLSimplified_Master
from python_code import MastersCollection

def test_DatadiagramMLSimplified_Master___init__():
    assert DatadiagramMLSimplified_Master.__init__(DatadiagramMLSimplified_Master('', '', '\x00', '', '', '', '', '', masters=MastersCollection(), me_master=set()), '', '', '', '', '\x00', '', '', '', masters=MastersCollection(), me_master=set()) == None


from python_code import DatadiagramMLSimplified_MasterShortCut
from python_code import MastersCollection

def test_DatadiagramMLSimplified_MasterShortCut___init__():
    assert DatadiagramMLSimplified_MasterShortCut.__init__(DatadiagramMLSimplified_MasterShortCut('', '', '\x00', '', '', '', i_masterShortCut=set(), masterShortCuts=MastersCollection()), '', '', '', '', '', '', i_masterShortCut=set(), masterShortCuts=MastersCollection()) == None


from python_code import DatadiagramMLSimplified_NamedElt

def test_DatadiagramMLSimplified_NamedElt___init__():
    assert DatadiagramMLSimplified_NamedElt.__init__(DatadiagramMLSimplified_NamedElt('', '\x00'), '\x00\x00', '') == None


from python_code import DatadiagramMLSimplified_Page
from python_code import PagesCollection

def test_DatadiagramMLSimplified_Page___init__():
    assert DatadiagramMLSimplified_Page.__init__(DatadiagramMLSimplified_Page('', '', '', '', '\x00', '', '', pages=PagesCollection(), pe_page=set()), '', '', '', '', '', '', '', pages=PagesCollection(), pe_page=set()) == None


from python_code import DatadiagramMLSimplified_Shape
from python_code import ShapesCollection

def test_DatadiagramMLSimplified_Shape___init__():
    assert DatadiagramMLSimplified_Shape.__init__(DatadiagramMLSimplified_Shape('', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()), '', '', '', shapes=ShapesCollection(), sse_shapeSheet=set()) == None


from python_code import DatadiagramMLSimplified_StringElt
from python_code import DatadiagramMLSimplified_Text

def test_DatadiagramMLSimplified_StringElt___init__():
    assert DatadiagramMLSimplified_StringElt.__init__(DatadiagramMLSimplified_StringElt('', TextElt=DatadiagramMLSimplified_Text()), '', TextElt=DatadiagramMLSimplified_Text()) == None


from python_code import DatadiagramMLSimplified_UniqueIdElt

def test_DatadiagramMLSimplified_UniqueIdElt___init__():
    assert DatadiagramMLSimplified_UniqueIdElt.__init__(DatadiagramMLSimplified_UniqueIdElt(''), '') == None

