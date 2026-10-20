from python_code import Documentation_Book

def test_Documentation_Book___init__():
    assert Documentation_Book.__init__(Documentation_Book('', Documentation_Book=set()), '', Documentation_Book=set()) == None


from python_code import Documentation_EmphasisValue

def test_Documentation_EmphasisValue___init__():
    assert Documentation_EmphasisValue.__init__(Documentation_EmphasisValue('', '\x00'), '\x00\x00', '') == None


from python_code import Documentation_InformalTableValueEntry
from python_code import Documentation_InformalTableValueRow

def test_Documentation_InformalTableValueEntry___init__():
    assert Documentation_InformalTableValueEntry.__init__(Documentation_InformalTableValueEntry('', Documentation_InformalTableValueEntry=Documentation_InformalTableValueRow()), '', Documentation_InformalTableValueEntry=Documentation_InformalTableValueRow()) == None


from python_code import Documentation_InformalTableValue
from python_code import Documentation_InformalTableValueBody
from python_code import Documentation_InformalTableValueGroup
from python_code import Documentation_InformalTableValueHead

def test_Documentation_InformalTableValueGroup___init__():
    assert Documentation_InformalTableValueGroup.__init__(Documentation_InformalTableValueGroup(0, Documentation_InformalTableValueGroup=Documentation_InformalTableValue(), Documentation_InformalTableValueGroup13=Documentation_InformalTableValueHead(), Documentation_InformalTableValueGroup15=Documentation_InformalTableValueBody()), 0, Documentation_InformalTableValueGroup=Documentation_InformalTableValue(), Documentation_InformalTableValueGroup13=Documentation_InformalTableValueHead(), Documentation_InformalTableValueGroup15=Documentation_InformalTableValueBody()) == None


from python_code import Documentation_TextualValue

def test_Documentation_TextualValue___init__():
    assert Documentation_TextualValue.__init__(Documentation_TextualValue(''), '') == None

