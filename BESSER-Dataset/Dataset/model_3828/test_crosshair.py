import datetime as _ch_datetime
from python_code import TestPackage_SubPackage_SubTestClass

def test_TestPackage_SubPackage_SubTestClass___init__():
    assert TestPackage_SubPackage_SubTestClass.__init__(TestPackage_SubPackage_SubTestClass(0, '\x00', '', False, _ch_datetime.date(1, 1, 1)), 0, '', '', False, _ch_datetime.date(1, 1, 1)) == None


import datetime as _ch_datetime
from python_code import TestPackage_TestClass

def test_TestPackage_TestClass___init__():
    assert TestPackage_TestClass.__init__(TestPackage_TestClass(_ch_datetime.date(1, 1, 1), '', '', False, 0, 0, 0, 0, 0, 0, '', 0, 0, 0), _ch_datetime.date(1, 1, 1), '', '', True, 0, 0, 0, 0, 0, 0, '', 0, 0, 0) == None

