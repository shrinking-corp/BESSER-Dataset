from python_code import party_Address

def test_party_Address___init__():
    assert party_Address.__init__(party_Address(''), '') == None


from python_code import party_Custom

def test_party_Custom___init__():
    assert party_Custom.__init__(party_Custom(''), '') == None


import datetime as _ch_datetime
from python_code import party_DateEffectiveObject

def test_party_DateEffectiveObject___init__():
    assert party_DateEffectiveObject.__init__(party_DateEffectiveObject(_ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1)), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None

def test_party_DateEffectiveObject_isEffective():
    assert party_DateEffectiveObject.isEffective(party_DateEffectiveObject(_ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1)), '') == None

def test_party_DateEffectiveObject_isEffectiveNow():
    assert party_DateEffectiveObject.isEffectiveNow(party_DateEffectiveObject(_ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1))) == None


from python_code import party_Person

def test_party_Person___init__():
    assert party_Person.__init__(party_Person(''), '') == None


from python_code import party_Phone

def test_party_Phone___init__():
    assert party_Phone.__init__(party_Phone('', 0, '\x00\x00'), '', 0, '') == None


from python_code import party_Tagged

def test_party_Tagged___init__():
    assert party_Tagged.__init__(party_Tagged('', party_Tagged=set()), '', party_Tagged=set()) == None


from python_code import party_URL

def test_party_URL___init__():
    assert party_URL.__init__(party_URL(''), '') == None


from python_code import party_USAddress

def test_party_USAddress___init__():
    assert party_USAddress.__init__(party_USAddress('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

