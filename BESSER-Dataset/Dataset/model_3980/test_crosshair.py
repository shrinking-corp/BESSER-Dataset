from python_code import dtmc_NamedEntity

def test_dtmc_NamedEntity___init__():
    assert dtmc_NamedEntity.__init__(dtmc_NamedEntity('', '\x00'), '\x00\x00', '') == None

