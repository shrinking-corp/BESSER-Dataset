from python_code import document_Entry
from python_code import document_Table

def test_document_Entry___init__():
    assert document_Entry.__init__(document_Entry(False, False, '\x00\x00', document_Entry=document_Table()), False, False, '', document_Entry=document_Table()) == None

