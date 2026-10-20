from python_code import WikiTable_Caption

def test_WikiTable_Caption___init__():
    assert WikiTable_Caption.__init__(WikiTable_Caption(''), '') == None


from python_code import WikiTable_Cell

def test_WikiTable_Cell___init__():
    assert WikiTable_Cell.__init__(WikiTable_Cell('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import WikiTable_LocatedElement

def test_WikiTable_LocatedElement___init__():
    assert WikiTable_LocatedElement.__init__(WikiTable_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import Caption
from python_code import WikiTable_Table

def test_WikiTable_Table___init__():
    assert WikiTable_Table.__init__(WikiTable_Table('', '', '', WikiTable_Table=Caption(), WikiTable_Table2=set()), '', '', '', WikiTable_Table=Caption(), WikiTable_Table2=set()) == None

