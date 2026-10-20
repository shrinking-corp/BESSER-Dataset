from python_code import yuml_ClassMember

def test_yuml_ClassMember___init__():
    assert yuml_ClassMember.__init__(yuml_ClassMember('', '\x00'), '\x00\x00', '') == None


from python_code import yuml_Note
from python_code import yuml_NoteAssociation

def test_yuml_Note___init__():
    assert yuml_Note.__init__(yuml_Note('', yuml_Note=yuml_NoteAssociation()), '', yuml_Note=yuml_NoteAssociation()) == None

