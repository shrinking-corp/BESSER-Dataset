from python_code import common_DoubleValueList
from python_code import common_DoubleValueMatrix

def test_common_DoubleValueList___init__():
    assert common_DoubleValueList.__init__(common_DoubleValueList('', common_DoubleValueList=set(), common_DoubleValueList3=common_DoubleValueMatrix()), '', common_DoubleValueList=set(), common_DoubleValueList3=common_DoubleValueMatrix()) == None


from python_code import common_StringValue
from python_code import common_StringValueList

def test_common_StringValue___init__():
    assert common_StringValue.__init__(common_StringValue('', common_StringValue=common_StringValueList()), '', common_StringValue=common_StringValueList()) == None

