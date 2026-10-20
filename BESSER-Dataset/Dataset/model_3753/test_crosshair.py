from python_code import dbmddandroid_Column
from python_code import dbmddandroid_Table

def test_dbmddandroid_Column___init__():
    assert dbmddandroid_Column.__init__(dbmddandroid_Column('', dbmddandroid_Column=dbmddandroid_Table()), '', dbmddandroid_Column=dbmddandroid_Table()) == None


from python_code import dbmddandroid_NamedElement

def test_dbmddandroid_NamedElement___init__():
    assert dbmddandroid_NamedElement.__init__(dbmddandroid_NamedElement(''), '') == None


from python_code import dbmddandroid_DBScheme
from python_code import dbmddandroid_Relation
from python_code import dbmddandroid_Table

def test_dbmddandroid_Relation___init__():
    assert dbmddandroid_Relation.__init__(dbmddandroid_Relation(0, 0, 0, 0, dbmddandroid_Relation=dbmddandroid_DBScheme(), Relation=dbmddandroid_Table(), Relation7=dbmddandroid_Table(), outRelation=dbmddandroid_Table(), inRelation=dbmddandroid_Table()), 0, 0, 0, 0, dbmddandroid_Relation=dbmddandroid_DBScheme(), Relation=dbmddandroid_Table(), Relation7=dbmddandroid_Table(), outRelation=dbmddandroid_Table(), inRelation=dbmddandroid_Table()) == None

