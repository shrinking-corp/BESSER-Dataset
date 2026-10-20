from python_code import DbMddAndroid_Column
from python_code import DbMddAndroid_Table

def test_DbMddAndroid_Column___init__():
    assert DbMddAndroid_Column.__init__(DbMddAndroid_Column('', DbMddAndroid_Column=DbMddAndroid_Table(), DbMddAndroid_Column7=DbMddAndroid_Table()), '', DbMddAndroid_Column=DbMddAndroid_Table(), DbMddAndroid_Column7=DbMddAndroid_Table()) == None


from python_code import DbMddAndroid_NamedElement

def test_DbMddAndroid_NamedElement___init__():
    assert DbMddAndroid_NamedElement.__init__(DbMddAndroid_NamedElement(''), '') == None


from python_code import DbMddAndroid_DBScheme
from python_code import DbMddAndroid_Relation
from python_code import DbMddAndroid_Table

def test_DbMddAndroid_Relation___init__():
    assert DbMddAndroid_Relation.__init__(DbMddAndroid_Relation(0, 0, 0, 0, Relation=DbMddAndroid_Table(), Relation10=DbMddAndroid_Table(), DbMddAndroid_Relation=DbMddAndroid_DBScheme(), outRelation=DbMddAndroid_Table(), inRelation=DbMddAndroid_Table()), 0, 0, 0, 0, Relation=DbMddAndroid_Table(), Relation10=DbMddAndroid_Table(), DbMddAndroid_Relation=DbMddAndroid_DBScheme(), outRelation=DbMddAndroid_Table(), inRelation=DbMddAndroid_Table()) == None

