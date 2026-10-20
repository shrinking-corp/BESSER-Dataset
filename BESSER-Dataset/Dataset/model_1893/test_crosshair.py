from python_code import sgen_BoolLiteral

def test_sgen_BoolLiteral___init__():
    assert sgen_BoolLiteral.__init__(sgen_BoolLiteral(True), False) == None


from python_code import sgen_DeprecatableElement

def test_sgen_DeprecatableElement___init__():
    assert sgen_DeprecatableElement.__init__(sgen_DeprecatableElement(False, '\x00'), False, '\x00') == None


from python_code import sgen_GeneratorModel

def test_sgen_GeneratorModel___init__():
    assert sgen_GeneratorModel.__init__(sgen_GeneratorModel('', sgen_GeneratorModel=set()), '', sgen_GeneratorModel=set()) == None


from python_code import sgen_IntLiteral

def test_sgen_IntLiteral___init__():
    assert sgen_IntLiteral.__init__(sgen_IntLiteral(0), 0) == None


from python_code import sgen_RealLiteral

def test_sgen_RealLiteral___init__():
    assert sgen_RealLiteral.__init__(sgen_RealLiteral(0.0), 0.0) == None


from python_code import sgen_StringLiteral

def test_sgen_StringLiteral___init__():
    assert sgen_StringLiteral.__init__(sgen_StringLiteral(''), '') == None

