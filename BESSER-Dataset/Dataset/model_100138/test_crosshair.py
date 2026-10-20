from python_code import dbmap_AbstractDBDataMapTable

def test_dbmap_AbstractDBDataMapTable___init__():
    assert dbmap_AbstractDBDataMapTable.__init__(dbmap_AbstractDBDataMapTable('', False, False, '', dbmap_AbstractDBDataMapTable=set()), '', False, False, '', dbmap_AbstractDBDataMapTable=set()) == None


from python_code import dbmap_FilterEntry
from python_code import dbmap_OutputTable

def test_dbmap_FilterEntry___init__():
    assert dbmap_FilterEntry.__init__(dbmap_FilterEntry('', '\x00', dbmap_FilterEntry=dbmap_OutputTable()), '\x00\x00', '', dbmap_FilterEntry=dbmap_OutputTable()) == None


from python_code import dbmap_DBMapData
from python_code import dbmap_InputTable

def test_dbmap_InputTable___init__():
    assert dbmap_InputTable.__init__(dbmap_InputTable('', '\x00', dbmap_InputTable=dbmap_DBMapData()), '\x00\x00', '', dbmap_InputTable=dbmap_DBMapData()) == None

