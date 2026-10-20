from python_code import ryz_Button

def test_ryz_Button___init__():
    assert ryz_Button.__init__(ryz_Button(''), '') == None


from python_code import ryz_Header
from python_code import ryz_Table

def test_ryz_Header___init__():
    assert ryz_Header.__init__(ryz_Header('', '\x00', ryz_Header=ryz_Table()), '\x00\x00', '', ryz_Header=ryz_Table()) == None


from python_code import ryz_AbstractView
from python_code import ryz_FormElementToPropertyKeyRelation
from python_code import ryz_HelperForSendingRequest
from python_code import ryz_PresentationElement
from python_code import ryz_UseCase
from python_code import ryz_ViewToControllerRelation

def test_ryz_HelperForSendingRequest___init__():
    assert ryz_HelperForSendingRequest.__init__(ryz_HelperForSendingRequest('', '', '', helperforsendingrequest56=set(), HelperForSendingRequest=ryz_UseCase(), helperforsendingrequest=set(), HelperForSendingRequest83=ryz_PresentationElement(), ryz_HelperForSendingRequest88=ryz_FormElementToPropertyKeyRelation(), ryz_HelperForSendingRequest=ryz_AbstractView(), ryz_HelperForSendingRequest35=ryz_ViewToControllerRelation()), '', '', '', helperforsendingrequest56=set(), HelperForSendingRequest=ryz_UseCase(), helperforsendingrequest=set(), HelperForSendingRequest83=ryz_PresentationElement(), ryz_HelperForSendingRequest88=ryz_FormElementToPropertyKeyRelation(), ryz_HelperForSendingRequest=ryz_AbstractView(), ryz_HelperForSendingRequest35=ryz_ViewToControllerRelation()) == None


from python_code import ryz_Input

def test_ryz_Input___init__():
    assert ryz_Input.__init__(ryz_Input('', False, False), '\x00', False, False) == None


from python_code import ryz_Link

def test_ryz_Link___init__():
    assert ryz_Link.__init__(ryz_Link(''), '') == None


from python_code import ryz_MultipleChoice

def test_ryz_MultipleChoice___init__():
    assert ryz_MultipleChoice.__init__(ryz_MultipleChoice('\x00\x00', False, ryz_MultipleChoice=set()), '', True, ryz_MultipleChoice=set()) == None


from python_code import ryz_NamedElement

def test_ryz_NamedElement___init__():
    assert ryz_NamedElement.__init__(ryz_NamedElement(''), '') == None


from python_code import ryz_PresentationForm
from python_code import ryz_PresentationFormElement
from python_code import ryz_PresentationFormElementToPropertyKey

def test_ryz_PresentationFormElement___init__():
    assert ryz_PresentationFormElement.__init__(ryz_PresentationFormElement('', ryz_PresentationFormElement=ryz_PresentationForm(), ryz_PresentationFormElement96=ryz_PresentationFormElementToPropertyKey()), '', ryz_PresentationFormElement=ryz_PresentationForm(), ryz_PresentationFormElement96=ryz_PresentationFormElementToPropertyKey()) == None

