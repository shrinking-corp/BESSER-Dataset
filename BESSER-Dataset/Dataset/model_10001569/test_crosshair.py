from python_code import author

def test_author___init__():
    assert author.__init__(author('', '', '', '', ''), '', '', '', '', '') == None


from python_code import author
from python_code import journal_article
from python_code import publisher

def test_journal_article___init__():
    assert journal_article.__init__(journal_article('', 0, publisher('', 0, '', ''), '\x00', author('', '', '', '', ''), 0, 0), '', 0, publisher('', 0, '', ''), '', author('', '\x00', '', '', ''), 0, 0) == None


from python_code import publisher

def test_publisher___init__():
    assert publisher.__init__(publisher('\x00\x00', 0, '', ''), '', 0, '', '') == None

