from python_code import qualitymodel_CompositeAttribute

def test_qualitymodel_CompositeAttribute___init__():
    assert qualitymodel_CompositeAttribute.__init__(qualitymodel_CompositeAttribute('', qualitymodel_CompositeAttribute=set()), '', qualitymodel_CompositeAttribute=set()) == None

def test_qualitymodel_CompositeAttribute_calculateSimultaneity():
    assert qualitymodel_CompositeAttribute.calculateSimultaneity(qualitymodel_CompositeAttribute('', qualitymodel_CompositeAttribute=set()), 0) == None

def test_qualitymodel_CompositeAttribute_calculateReplaceability():
    assert qualitymodel_CompositeAttribute.calculateReplaceability(qualitymodel_CompositeAttribute('', qualitymodel_CompositeAttribute=set()), 0) == None

def test_qualitymodel_CompositeAttribute_calculateNeutrality():
    assert qualitymodel_CompositeAttribute.calculateNeutrality(qualitymodel_CompositeAttribute('', qualitymodel_CompositeAttribute=set()), 0) == None


from python_code import qualitymodel_ConfigurationProfile

def test_qualitymodel_ConfigurationProfile___init__():
    assert qualitymodel_ConfigurationProfile.__init__(qualitymodel_ConfigurationProfile(0, qualitymodel_ConfigurationProfile=set(), qualitymodel_ConfigurationProfile9=set()), 0, qualitymodel_ConfigurationProfile=set(), qualitymodel_ConfigurationProfile9=set()) == None

