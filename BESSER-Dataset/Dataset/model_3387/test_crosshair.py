from python_code import JPA_Column

def test_JPA_Column___init__():
    assert JPA_Column.__init__(JPA_Column('\x00\x00', '', False, ''), '', '', False, '') == None


from python_code import JPA_Entity
from python_code import JPA_PersistenceUnit

def test_JPA_Entity___init__():
    assert JPA_Entity.__init__(JPA_Entity('', '', JPA_Entity=JPA_PersistenceUnit(), JPA_Entity2=set(), JPA_Entity4=set()), '', '', JPA_Entity=JPA_PersistenceUnit(), JPA_Entity2=set(), JPA_Entity4=set()) == None


from python_code import JPA_EntityPk

def test_JPA_EntityPk___init__():
    assert JPA_EntityPk.__init__(JPA_EntityPk('', JPA_EntityPk=set()), '', JPA_EntityPk=set()) == None


from python_code import JPA_ManyToOne

def test_JPA_ManyToOne___init__():
    assert JPA_ManyToOne.__init__(JPA_ManyToOne('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import JPA_OneToMany

def test_JPA_OneToMany___init__():
    assert JPA_OneToMany.__init__(JPA_OneToMany('', '', '\x00\x00'), '', '', '') == None


from python_code import JPA_OneToOne

def test_JPA_OneToOne___init__():
    assert JPA_OneToOne.__init__(JPA_OneToOne('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import JPA_Table

def test_JPA_Table___init__():
    assert JPA_Table.__init__(JPA_Table(''), '') == None

