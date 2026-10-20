from python_code import avm_CalculatedValue

def test_avm_CalculatedValue___init__():
    assert avm_CalculatedValue.__init__(avm_CalculatedValue('', '\x00'), '\x00\x00', '') == None


from python_code import avm_ComplexFormula

def test_avm_ComplexFormula___init__():
    assert avm_ComplexFormula.__init__(avm_ComplexFormula('', avm_ComplexFormula=set()), '', avm_ComplexFormula=set()) == None

