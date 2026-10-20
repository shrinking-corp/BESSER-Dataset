from python_code import model_DoorsFolder

def test_model_DoorsFolder___init__():
    assert model_DoorsFolder.__init__(model_DoorsFolder(True), False) == None


from python_code import model_DoorsModule

def test_model_DoorsModule___init__():
    assert model_DoorsModule.__init__(model_DoorsModule()) == None

def test_model_DoorsModule_getObjectAttributes():
    assert model_DoorsModule.getObjectAttributes(model_DoorsModule()) == None

def test_model_DoorsModule_getView():
    assert model_DoorsModule.getView(model_DoorsModule()) == None

def test_model_DoorsModule_setObjectAttributes():
    assert model_DoorsModule.setObjectAttributes(model_DoorsModule(), '') == None

