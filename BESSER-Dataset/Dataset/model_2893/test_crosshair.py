from python_code import webGui_ActionElement

def test_webGui_ActionElement___init__():
    assert webGui_ActionElement.__init__(webGui_ActionElement(''), '') == None


from python_code import webGui_DomainModel
from python_code import webGui_Model
from python_code import webGui_WebModel

def test_webGui_Model___init__():
    assert webGui_Model.__init__(webGui_Model('', webGui_Model=webGui_DomainModel(), webGui_Model2=webGui_WebModel()), '', webGui_Model=webGui_DomainModel(), webGui_Model2=webGui_WebModel()) == None


from python_code import webGui_NumberLiteral

def test_webGui_NumberLiteral___init__():
    assert webGui_NumberLiteral.__init__(webGui_NumberLiteral(0), 0) == None


from python_code import webGui_Entity
from python_code import webGui_Page
from python_code import webGui_WebModel

def test_webGui_Page___init__():
    assert webGui_Page.__init__(webGui_Page('\x00\x00', '', webGui_Page=webGui_WebModel(), webGui_Page14=webGui_Entity(), webGui_Page17=set()), '', '', webGui_Page=webGui_WebModel(), webGui_Page14=webGui_Entity(), webGui_Page17=set()) == None

