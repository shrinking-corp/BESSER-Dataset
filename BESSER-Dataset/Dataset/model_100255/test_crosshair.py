from python_code import wikigen_Article

def test_wikigen_Article___init__():
    assert wikigen_Article.__init__(wikigen_Article(0, False), 0, False) == None


from python_code import wikigen_GenHtmlDocument
from python_code import wikigen_HtmlProfile

def test_wikigen_GenHtmlDocument___init__():
    assert wikigen_GenHtmlDocument.__init__(wikigen_GenHtmlDocument('', wikigen_GenHtmlDocument3=set(), wikigen_GenHtmlDocument=wikigen_HtmlProfile()), '', wikigen_GenHtmlDocument3=set(), wikigen_GenHtmlDocument=wikigen_HtmlProfile()) == None


from python_code import wikigen_GenLatexDocument

def test_wikigen_GenLatexDocument___init__():
    assert wikigen_GenLatexDocument.__init__(wikigen_GenLatexDocument('', '', '', wikigen_GenLatexDocument=set()), '', '', '', wikigen_GenLatexDocument=set()) == None

