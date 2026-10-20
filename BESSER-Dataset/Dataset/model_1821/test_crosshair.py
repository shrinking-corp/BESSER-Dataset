from python_code import Documentation_Book

def test_Documentation_Book___init__():
    assert Documentation_Book.__init__(Documentation_Book('', Documentation_Book=set()), '', Documentation_Book=set()) == None


from python_code import Documentation_EmphasisValue

def test_Documentation_EmphasisValue___init__():
    assert Documentation_EmphasisValue.__init__(Documentation_EmphasisValue(''), '') == None


from python_code import Documentation_InformalTableValue

def test_Documentation_InformalTableValue___init__():
    assert Documentation_InformalTableValue.__init__(Documentation_InformalTableValue(0, Documentation_InformalTableValue=set(), Documentation_InformalTableValue13=set()), 0, Documentation_InformalTableValue=set(), Documentation_InformalTableValue13=set()) == None


from python_code import Documentation_InformalTableValueRow
from python_code import Documentation_TextualValue

def test_Documentation_TextualValue___init__():
    assert Documentation_TextualValue.__init__(Documentation_TextualValue('', Documentation_TextualValue=Documentation_InformalTableValueRow()), '', Documentation_TextualValue=Documentation_InformalTableValueRow()) == None

