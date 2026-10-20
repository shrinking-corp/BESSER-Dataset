from python_code import model6_EmptyStringDefault

def test_model6_EmptyStringDefault___init__():
    assert model6_EmptyStringDefault.__init__(model6_EmptyStringDefault(''), '') == None


from python_code import model6_EmptyStringDefaultUnsettable

def test_model6_EmptyStringDefaultUnsettable___init__():
    assert model6_EmptyStringDefaultUnsettable.__init__(model6_EmptyStringDefaultUnsettable(''), '') == None


from python_code import model6_HasNillableAttribute

def test_model6_HasNillableAttribute___init__():
    assert model6_HasNillableAttribute.__init__(model6_HasNillableAttribute(''), '') == None


from python_code import model6_Holdable
from python_code import model6_Holder

def test_model6_Holdable___init__():
    assert model6_Holdable.__init__(model6_Holdable('', model6_Holdable=model6_Holder(), model6_Holdable50=model6_Holder()), '', model6_Holdable=model6_Holder(), model6_Holdable50=model6_Holder()) == None


from python_code import model6_MyEnumList

def test_model6_MyEnumList___init__():
    assert model6_MyEnumList.__init__(model6_MyEnumList(''), '') == None


from python_code import model6_MyEnumListUnsettable

def test_model6_MyEnumListUnsettable___init__():
    assert model6_MyEnumListUnsettable.__init__(model6_MyEnumListUnsettable(''), '') == None


from python_code import model6_PropertiesMap

def test_model6_PropertiesMap___init__():
    assert model6_PropertiesMap.__init__(model6_PropertiesMap('', model6_PropertiesMap=set(), model6_PropertiesMap27=set()), '', model6_PropertiesMap=set(), model6_PropertiesMap27=set()) == None


import datetime as _ch_datetime
from python_code import model6_UnsettableAttributes

def test_model6_UnsettableAttributes___init__():
    assert model6_UnsettableAttributes.__init__(model6_UnsettableAttributes('', '', '', '\x00', '', '', '', False, '', '', '', '', '', '', _ch_datetime.date(1, 1, 1), 0.0, '', 0.0, '', 0, '', '', ''), '', '', '', '', '', '', '', False, '', '', '\x00', '', '', '', _ch_datetime.date(1, 1, 1), 0.0, '', 0.0, '', 0, '', '', '') == None

