from python_code import jsonldConverter_Enum
from python_code import jsonldConverter_EnumItem

def test_jsonldConverter_EnumItem___init__():
    assert jsonldConverter_EnumItem.__init__(jsonldConverter_EnumItem('', '\x00', jsonldConverter_EnumItem=jsonldConverter_Enum()), '\x00\x00', '', jsonldConverter_EnumItem=jsonldConverter_Enum()) == None

