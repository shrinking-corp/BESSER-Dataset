from python_code import bibtex_Document
from python_code import bibtex_Model

def test_bibtex_Document___init__():
    assert bibtex_Document.__init__(bibtex_Document('', '', 0, '', '', '', '', '', '', '', '\x00', '', bibtex_Document=bibtex_Model()), '', '', 0, '', '', '', '', '', '', '', '', '', bibtex_Document=bibtex_Model()) == None

