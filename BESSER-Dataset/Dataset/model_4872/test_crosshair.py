from python_code import collection_ManualCollection

def test_collection_ManualCollection___init__():
    assert collection_ManualCollection.__init__(collection_ManualCollection()) == None

def test_collection_ManualCollection_addItem():
    assert collection_ManualCollection.addItem(collection_ManualCollection(), '') == None

def test_collection_ManualCollection_removeItem():
    assert collection_ManualCollection.removeItem(collection_ManualCollection(), '') == None


from python_code import collection_RemoteCollection

def test_collection_RemoteCollection___init__():
    assert collection_RemoteCollection.__init__(collection_RemoteCollection(''), '') == None

