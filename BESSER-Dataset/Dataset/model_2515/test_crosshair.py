from python_code import model6_MyEnumList

def test_model6_MyEnumList___init__():
    assert model6_MyEnumList.__init__(model6_MyEnumList(''), '') == None


from python_code import model6_MyEnumListUnsettable

def test_model6_MyEnumListUnsettable___init__():
    assert model6_MyEnumListUnsettable.__init__(model6_MyEnumListUnsettable(''), '') == None


from python_code import model6_PropertiesMap

def test_model6_PropertiesMap___init__():
    assert model6_PropertiesMap.__init__(model6_PropertiesMap('', model6_PropertiesMap27=set(), model6_PropertiesMap=set()), '', model6_PropertiesMap27=set(), model6_PropertiesMap=set()) == None

