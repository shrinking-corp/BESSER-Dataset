from python_code import ulmDsl2_AttributeDecimalType

def test_ulmDsl2_AttributeDecimalType___init__():
    assert ulmDsl2_AttributeDecimalType.__init__(ulmDsl2_AttributeDecimalType('\x00\x00', False, 0, 0), '', False, 0, 0) == None


from python_code import ulmDsl2_AttributeStringType

def test_ulmDsl2_AttributeStringType___init__():
    assert ulmDsl2_AttributeStringType.__init__(ulmDsl2_AttributeStringType('', False, 0), '\x00', False, 0) == None


from python_code import ulmDsl2_AttributeType

def test_ulmDsl2_AttributeType___init__():
    assert ulmDsl2_AttributeType.__init__(ulmDsl2_AttributeType(''), '') == None


from python_code import ulmDsl2_LookupString

def test_ulmDsl2_LookupString___init__():
    assert ulmDsl2_LookupString.__init__(ulmDsl2_LookupString('', ulmDsl2_LookupString=set()), '', ulmDsl2_LookupString=set()) == None

