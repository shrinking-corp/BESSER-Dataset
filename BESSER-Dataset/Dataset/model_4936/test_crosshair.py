from python_code import webapp_Attribute
from python_code import webapp_DataStructure

def test_webapp_Attribute___init__():
    assert webapp_Attribute.__init__(webapp_Attribute('', Attribute=webapp_DataStructure(), Attribute13=webapp_DataStructure(), parentOf=webapp_DataStructure(), linkedTo=set()), '', Attribute=webapp_DataStructure(), Attribute13=webapp_DataStructure(), parentOf=webapp_DataStructure(), linkedTo=set()) == None


from python_code import webapp_Named

def test_webapp_Named___init__():
    assert webapp_Named.__init__(webapp_Named(''), '') == None


from python_code import webapp_ClientPage
from python_code import webapp_DataSourceManager
from python_code import webapp_DataStructure
from python_code import webapp_ServerPage
from python_code import webapp_WebApp

def test_webapp_ServerPage___init__():
    assert webapp_ServerPage.__init__(webapp_ServerPage(webapp_ServerPage=webapp_WebApp(), ServerPage23=webapp_ClientPage(), connectsTo=webapp_ClientPage(), providesContent=set(), managedBy=set(), ServerPage=webapp_DataStructure(), ServerPage15=webapp_DataSourceManager()), webapp_ServerPage=webapp_WebApp(), ServerPage23=webapp_ClientPage(), connectsTo=webapp_ClientPage(), providesContent=set(), managedBy=set(), ServerPage=webapp_DataStructure(), ServerPage15=webapp_DataSourceManager()) == None

def test_webapp_ServerPage_request():
    assert webapp_ServerPage.request(webapp_ServerPage(webapp_ServerPage=webapp_WebApp(), ServerPage23=webapp_ClientPage(), connectsTo=webapp_ClientPage(), providesContent=set(), managedBy=set(), ServerPage=webapp_DataStructure(), ServerPage15=webapp_DataSourceManager())) == None

def test_webapp_ServerPage_response():
    assert webapp_ServerPage.response(webapp_ServerPage(webapp_ServerPage=webapp_WebApp(), ServerPage23=webapp_ClientPage(), connectsTo=webapp_ClientPage(), providesContent=set(), managedBy=set(), ServerPage=webapp_DataStructure(), ServerPage15=webapp_DataSourceManager())) == None


from python_code import webapp_ClientPage
from python_code import webapp_DataStructure
from python_code import webapp_UIElement

def test_webapp_UIElement___init__():
    assert webapp_UIElement.__init__(webapp_UIElement('', webapp_UIElement25=webapp_DataStructure(), webapp_UIElement=webapp_ClientPage()), '', webapp_UIElement25=webapp_DataStructure(), webapp_UIElement=webapp_ClientPage()) == None

