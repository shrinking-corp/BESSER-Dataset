from python_code import PHPMVC_coreMVC_Application
from python_code import PackageController
from python_code import PackageModel
from python_code import PackageView

def test_PHPMVC_coreMVC_Application___init__():
    assert PHPMVC_coreMVC_Application.__init__(PHPMVC_coreMVC_Application('\x00\x00', '', '', '', PHPMVC_coreMVC_Application=PackageModel(), PHPMVC_coreMVC_Application2=PackageView(), PHPMVC_coreMVC_Application4=PackageController()), '', '', '', '', PHPMVC_coreMVC_Application=PackageModel(), PHPMVC_coreMVC_Application2=PackageView(), PHPMVC_coreMVC_Application4=PackageController()) == None


from python_code import PHPMVC_coreMVC_Attribute

def test_PHPMVC_coreMVC_Attribute___init__():
    assert PHPMVC_coreMVC_Attribute.__init__(PHPMVC_coreMVC_Attribute(''), '') == None


from python_code import PHPMVC_coreMVC_Event

def test_PHPMVC_coreMVC_Event___init__():
    assert PHPMVC_coreMVC_Event.__init__(PHPMVC_coreMVC_Event('', '\x00'), '\x00\x00', '') == None


from python_code import PHPMVC_coreMVC_Identifier
from python_code import PHPMVC_coreMVC_MVCClass
from python_code import PHPMVC_coreMVC_Method

def test_PHPMVC_coreMVC_Identifier___init__():
    assert PHPMVC_coreMVC_Identifier.__init__(PHPMVC_coreMVC_Identifier(False, Attribute=PHPMVC_coreMVC_MVCClass('', PHPMVC_coreMVC_MVCClass=set()), Attribute19=PHPMVC_coreMVC_Method('\x00', PHPMVC_coreMVC_Method=set(), PHPMVC_coreMVC_Method18=set()), Attribute16=PHPMVC_coreMVC_Method('', PHPMVC_coreMVC_Method=set(), PHPMVC_coreMVC_Method18=set())), False, Attribute=PHPMVC_coreMVC_MVCClass('', PHPMVC_coreMVC_MVCClass=set()), Attribute19=PHPMVC_coreMVC_Method('', PHPMVC_coreMVC_Method=set(), PHPMVC_coreMVC_Method18=set()), Attribute16=PHPMVC_coreMVC_Method('', PHPMVC_coreMVC_Method=set(), PHPMVC_coreMVC_Method18=set())) == None


from python_code import PHPMVC_coreMVC_MVCClass

def test_PHPMVC_coreMVC_MVCClass___init__():
    assert PHPMVC_coreMVC_MVCClass.__init__(PHPMVC_coreMVC_MVCClass('', PHPMVC_coreMVC_MVCClass=set()), '', PHPMVC_coreMVC_MVCClass=set()) == None


from python_code import PHPMVC_coreMVC_Method

def test_PHPMVC_coreMVC_Method___init__():
    assert PHPMVC_coreMVC_Method.__init__(PHPMVC_coreMVC_Method('', PHPMVC_coreMVC_Method=set(), PHPMVC_coreMVC_Method18=set()), '', PHPMVC_coreMVC_Method=set(), PHPMVC_coreMVC_Method18=set()) == None


from python_code import PHPMVC_coreMVC_PackageController

def test_PHPMVC_coreMVC_PackageController___init__():
    assert PHPMVC_coreMVC_PackageController.__init__(PHPMVC_coreMVC_PackageController('', PHPMVC_coreMVC_PackageController=set()), '', PHPMVC_coreMVC_PackageController=set()) == None


from python_code import PHPMVC_coreMVC_PackageModel

def test_PHPMVC_coreMVC_PackageModel___init__():
    assert PHPMVC_coreMVC_PackageModel.__init__(PHPMVC_coreMVC_PackageModel('', PHPMVC_coreMVC_PackageModel=set()), '', PHPMVC_coreMVC_PackageModel=set()) == None


from python_code import PHPMVC_coreMVC_PackageView

def test_PHPMVC_coreMVC_PackageView___init__():
    assert PHPMVC_coreMVC_PackageView.__init__(PHPMVC_coreMVC_PackageView('', PHPMVC_coreMVC_PackageView=set()), '', PHPMVC_coreMVC_PackageView=set()) == None


from python_code import PHPMVC_coreMVC_ViewComponent

def test_PHPMVC_coreMVC_ViewComponent___init__():
    assert PHPMVC_coreMVC_ViewComponent.__init__(PHPMVC_coreMVC_ViewComponent('', PHPMVC_coreMVC_ViewComponent=set()), '', PHPMVC_coreMVC_ViewComponent=set()) == None


from python_code import PHPMVC_coreMVC_View
from python_code import PHPMVC_extPHP_Anchor
from python_code import PHPMVC_extPHP_HTMLElement

def test_PHPMVC_extPHP_Anchor___init__():
    assert PHPMVC_extPHP_Anchor.__init__(PHPMVC_extPHP_Anchor('', '\x00', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', True, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())), '', '', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, True, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())) == None


from python_code import PHPMVC_coreMVC_View
from python_code import PHPMVC_extPHP_Button
from python_code import PHPMVC_extPHP_HTMLElement

def test_PHPMVC_extPHP_Button___init__():
    assert PHPMVC_extPHP_Button.__init__(PHPMVC_extPHP_Button(False, '', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())), False, '', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())) == None


from python_code import PHPMVC_coreMVC_View
from python_code import PHPMVC_extPHP_Form
from python_code import PHPMVC_extPHP_HTMLElement

def test_PHPMVC_extPHP_Form___init__():
    assert PHPMVC_extPHP_Form.__init__(PHPMVC_extPHP_Form('', '', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())), '', '', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())) == None


from python_code import PHPMVC_coreMVC_View
from python_code import PHPMVC_extPHP_HTMLElement

def test_PHPMVC_extPHP_HTMLElement___init__():
    assert PHPMVC_extPHP_HTMLElement.__init__(PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View()), '', False, True, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View()) == None


from python_code import PHPMVC_coreMVC_View
from python_code import PHPMVC_extPHP_HTMLElement
from python_code import PHPMVC_extPHP_Image

def test_PHPMVC_extPHP_Image___init__():
    assert PHPMVC_extPHP_Image.__init__(PHPMVC_extPHP_Image('', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())), '', HTMLElement=PHPMVC_extPHP_HTMLElement('', True, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())) == None


from python_code import PHPMVC_coreMVC_View
from python_code import PHPMVC_extPHP_HTMLElement
from python_code import PHPMVC_extPHP_Input

def test_PHPMVC_extPHP_Input___init__():
    assert PHPMVC_extPHP_Input.__init__(PHPMVC_extPHP_Input('', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())), '', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())) == None


from python_code import PHPMVC_coreMVC_View
from python_code import PHPMVC_extPHP_HTMLElement
from python_code import PHPMVC_extPHP_Text

def test_PHPMVC_extPHP_Text___init__():
    assert PHPMVC_extPHP_Text.__init__(PHPMVC_extPHP_Text('', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())), '', '', HTMLElement=PHPMVC_extPHP_HTMLElement('', False, False, PHPMVC_extPHP_HTMLElement=set(), ViewComponent=PHPMVC_coreMVC_View())) == None

