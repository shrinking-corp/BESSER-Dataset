from python_code import statespace_Storage

def test_statespace_Storage___init__():
    assert statespace_Storage.__init__(statespace_Storage(''), '') == None

def test_statespace_Storage_setData():
    assert statespace_Storage.setData(statespace_Storage(''), 0, '\x00\x00', '') == None

def test_statespace_Storage_getData():
    assert statespace_Storage.getData(statespace_Storage(''), 0, '\x00\x00') == None

