from python_code import core_COREFeatureModel

def test_core_COREFeatureModel___init__():
    assert core_COREFeatureModel.__init__(core_COREFeatureModel()) == None

def test_core_COREFeatureModel_getLocalRoot():
    assert core_COREFeatureModel.getLocalRoot(core_COREFeatureModel()) == None

def test_core_COREFeatureModel_getGlobalRoot():
    assert core_COREFeatureModel.getGlobalRoot(core_COREFeatureModel()) == None


from python_code import core_CORENamedElement

def test_core_CORENamedElement___init__():
    assert core_CORENamedElement.__init__(core_CORENamedElement(''), '') == None

