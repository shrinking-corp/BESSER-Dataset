from python_code import xwiki_HistorySummary
from python_code import xwiki_HistoryType

def test_xwiki_HistorySummary___init__():
    assert xwiki_HistorySummary.__init__(xwiki_HistorySummary('', '', '', '', '', '', '', '', '', '', '\x00', '', xwiki_HistorySummary=xwiki_HistoryType()), '', '', '', '', '', '', '', '', '', '', '', '', xwiki_HistorySummary=xwiki_HistoryType()) == None


from python_code import xwiki_Link
from python_code import xwiki_LinkCollection

def test_xwiki_Link___init__():
    assert xwiki_Link.__init__(xwiki_Link('\x00\x00', '', '', '', xwiki_Link=xwiki_LinkCollection()), '', '', '', '', xwiki_Link=xwiki_LinkCollection()) == None

