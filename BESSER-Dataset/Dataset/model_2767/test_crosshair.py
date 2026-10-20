from python_code import my_AType
from python_code import my_BType

def test_my_AType___init__():
    assert my_AType.__init__(my_AType(my_AType=my_BType(), my_AType5=my_BType()), my_AType=my_BType(), my_AType5=my_BType()) == None

def test_my_AType_referenced():
    assert my_AType.referenced(my_AType(my_AType=my_BType(), my_AType5=my_BType())) == None


from python_code import my_Entity

def test_my_Entity___init__():
    assert my_Entity.__init__(my_Entity(''), '') == None

