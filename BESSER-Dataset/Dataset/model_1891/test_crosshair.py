from python_code import sgen_DeprecatableElement

def test_sgen_DeprecatableElement___init__():
    assert sgen_DeprecatableElement.__init__(sgen_DeprecatableElement(False, '\x00'), False, '\x00') == None


from python_code import sgen_GeneratorModel

def test_sgen_GeneratorModel___init__():
    assert sgen_GeneratorModel.__init__(sgen_GeneratorModel('', sgen_GeneratorModel=set(), sgen_GeneratorModel2=set()), '', sgen_GeneratorModel=set(), sgen_GeneratorModel2=set()) == None

