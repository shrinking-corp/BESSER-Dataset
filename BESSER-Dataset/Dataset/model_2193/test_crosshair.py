from python_code import article_BodyElement
from python_code import article_BodyElementContainer

def test_article_BodyElement___init__():
    assert article_BodyElement.__init__(article_BodyElement('', BodyElement=article_BodyElementContainer(), elements=article_BodyElementContainer()), '', BodyElement=article_BodyElementContainer(), elements=article_BodyElementContainer()) == None


from python_code import article_ExternalArticle

def test_article_ExternalArticle___init__():
    assert article_ExternalArticle.__init__(article_ExternalArticle(''), '') == None


from python_code import article_ExternalTarget

def test_article_ExternalTarget___init__():
    assert article_ExternalTarget.__init__(article_ExternalTarget(''), '') == None


from python_code import article_HtmlFormatter

def test_article_HtmlFormatter___init__():
    assert article_HtmlFormatter.__init__(article_HtmlFormatter(''), '') == None


from python_code import article_Identifiable

def test_article_Identifiable___init__():
    assert article_Identifiable.__init__(article_Identifiable(''), '') == None


from python_code import article_Image

def test_article_Image___init__():
    assert article_Image.__init__(article_Image(''), '') == None


from python_code import article_ImageFactory

def test_article_ImageFactory___init__():
    assert article_ImageFactory.__init__(article_ImageFactory(''), '') == None


from python_code import article_ImageFormatter

def test_article_ImageFormatter___init__():
    assert article_ImageFormatter.__init__(article_ImageFormatter(''), '') == None


from python_code import article_JavaElement

def test_article_JavaElement___init__():
    assert article_JavaElement.__init__(article_JavaElement(''), '') == None


from python_code import article_Link
from python_code import article_LinkTarget

def test_article_LinkTarget___init__():
    assert article_LinkTarget.__init__(article_LinkTarget('', '\x00', article_LinkTarget=article_Link()), '\x00\x00', '', article_LinkTarget=article_Link()) == None

def test_article_LinkTarget_linkFrom():
    assert article_LinkTarget.linkFrom(article_LinkTarget('', '', article_LinkTarget=article_Link()), '') == None


from python_code import article_Callout
from python_code import article_Description
from python_code import article_Formatter
from python_code import article_Snippet

def test_article_Snippet___init__():
    assert article_Snippet.__init__(article_Snippet('\x00\x00', '', snippet=set(), snippet11=article_Formatter(), snippet13=article_Description(), Snippet=article_Callout(), Snippet37=article_Formatter(), Snippet46=article_Description()), '', '', snippet=set(), snippet11=article_Formatter(), snippet13=article_Description(), Snippet=article_Callout(), Snippet37=article_Formatter(), Snippet46=article_Description()) == None


from python_code import article_Toc

def test_article_Toc___init__():
    assert article_Toc.__init__(article_Toc(0), 0) == None


from python_code import article_TreeFormatter

def test_article_TreeFormatter___init__():
    assert article_TreeFormatter.__init__(article_TreeFormatter('\x00\x00', 0, '', ''), '', 0, '', '') == None


from python_code import article_XmlFormatter

def test_article_XmlFormatter___init__():
    assert article_XmlFormatter.__init__(article_XmlFormatter(''), '') == None

