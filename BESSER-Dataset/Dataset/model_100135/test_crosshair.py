from python_code import dbca_Attribute

def test_dbca_Attribute___init__():
    assert dbca_Attribute.__init__(dbca_Attribute('', 0), '', 0) == None


from python_code import dbca_CommentedElement

def test_dbca_CommentedElement___init__():
    assert dbca_CommentedElement.__init__(dbca_CommentedElement(''), '') == None


from python_code import dbca_Entity
from python_code import dbca_EntityForm

def test_dbca_EntityForm___init__():
    assert dbca_EntityForm.__init__(dbca_EntityForm('', dbca_EntityForm=dbca_Entity()), '', dbca_EntityForm=dbca_Entity()) == None


from python_code import dbca_Function

def test_dbca_Function___init__():
    assert dbca_Function.__init__(dbca_Function('\x00', dbca_Function=set()), '', dbca_Function=set()) == None


from python_code import dbca_NamedElement

def test_dbca_NamedElement___init__():
    assert dbca_NamedElement.__init__(dbca_NamedElement(''), '') == None


from python_code import dbca_Entity
from python_code import dbca_Relationship

def test_dbca_Relationship___init__():
    assert dbca_Relationship.__init__(dbca_Relationship('', False, '', dbca_Relationship=dbca_Entity(), dbca_Relationship16=dbca_Entity(), dbca_Relationship19=set()), '', False, '', dbca_Relationship=dbca_Entity(), dbca_Relationship16=dbca_Entity(), dbca_Relationship19=set()) == None

