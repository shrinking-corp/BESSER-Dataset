from python_code import bibtex_Article

def test_bibtex_Article___init__():
    assert bibtex_Article.__init__(bibtex_Article('', 0, 0, 0, ''), '', 0, 0, 0, '') == None


from python_code import bibtex_Author

def test_bibtex_Author___init__():
    assert bibtex_Author.__init__(bibtex_Author('\x00\x00', '', bibtex_Author=set()), '', '', bibtex_Author=set()) == None


from python_code import bibtex_Book

def test_bibtex_Book___init__():
    assert bibtex_Book.__init__(bibtex_Book('', 0, 0, '', 0), '', 0, 0, '', 0) == None


from python_code import bibtex_DatedEntry

def test_bibtex_DatedEntry___init__():
    assert bibtex_DatedEntry.__init__(bibtex_DatedEntry(0), 0) == None


from python_code import bibtex_MonthEntry

def test_bibtex_MonthEntry___init__():
    assert bibtex_MonthEntry.__init__(bibtex_MonthEntry(''), '') == None

