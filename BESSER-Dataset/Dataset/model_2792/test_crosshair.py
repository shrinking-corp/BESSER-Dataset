from python_code import kreq205_SObject

def test_kreq205_SObject___init__():
    assert kreq205_SObject.__init__(kreq205_SObject('', '\x00'), '\x00\x00', '') == None

