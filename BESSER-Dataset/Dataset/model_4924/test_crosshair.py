from python_code import web_HtmlContent

def test_web_HtmlContent___init__():
    assert web_HtmlContent.__init__(web_HtmlContent(''), '') == None


from python_code import web_SocialBar
from python_code import web_SocialInformation

def test_web_SocialInformation___init__():
    assert web_SocialInformation.__init__(web_SocialInformation('\x00\x00', '', '', '', web_SocialInformation=web_SocialBar()), '', '', '', '', web_SocialInformation=web_SocialBar()) == None

