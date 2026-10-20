from python_code import contentfwk_BusinessArchitecture
from python_code import contentfwk_Contract
from python_code import contentfwk_Service
from python_code import contentfwk_ServiceQuality

def test_contentfwk_Contract___init__():
    assert contentfwk_Contract.__init__(contentfwk_Contract('', '\x00', '', '\x01', '', '', '', '', '', '', '', '', '', '\x00', '\x00', '\x00', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', contentfwk_Contract=contentfwk_BusinessArchitecture(), Contract=contentfwk_ServiceQuality(), isGovernedAndMeasuredByContracts=set(), appliesToContracts=set(), Contract309=contentfwk_Service()), '', '', '', '', '\x00', '', '', '', '\x01', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', contentfwk_Contract=contentfwk_BusinessArchitecture(), Contract=contentfwk_ServiceQuality(), isGovernedAndMeasuredByContracts=set(), appliesToContracts=set(), Contract309=contentfwk_Service()) == None


from python_code import contentfwk_Principle

def test_contentfwk_Principle___init__():
    assert contentfwk_Principle.__init__(contentfwk_Principle('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import contentfwk_Requirement

def test_contentfwk_Requirement___init__():
    assert contentfwk_Requirement.__init__(contentfwk_Requirement('', '', '\x00\x00'), '', '', '') == None


import datetime as _ch_datetime
from python_code import contentfwk_Standard

def test_contentfwk_Standard___init__():
    assert contentfwk_Standard.__init__(contentfwk_Standard('', _ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 3), ''), '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), '') == None

