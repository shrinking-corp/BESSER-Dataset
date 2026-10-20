from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import ClassA

def test_ClassA___init__():
    assert ClassA.__init__(ClassA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Basket
from python_code import Client
from python_code import ClientDatabase
from python_code import Order
from python_code import Payment_Interface
from python_code import Wishlist

def test_Client___init__():
    assert Client.__init__(Client('', '', '\x00\x00', clientDatabase30=ClientDatabase(), order36=Order(), payment44=Payment_Interface(), basket46=Basket(), wishlist54=Wishlist()), '', '', '', clientDatabase30=ClientDatabase(), order36=Order(), payment44=Payment_Interface(), basket46=Basket(), wishlist54=Wishlist()) == None


from python_code import ClientRewiev
from python_code import DetailDescription

def test_ClientRewiev___init__():
    assert ClientRewiev.__init__(ClientRewiev(0, '\x00', detailDescription23=DetailDescription()), 0, '\x00', detailDescription23=DetailDescription()) == None


from python_code import DetailDescription
from python_code import OriginalReview

def test_OriginalReview___init__():
    assert OriginalReview.__init__(OriginalReview('', detailDescription25=DetailDescription()), '', detailDescription25=DetailDescription()) == None


from python_code import Basket
from python_code import Catalog
from python_code import DetailDescription
from python_code import Order
from python_code import Review_Interface
from python_code import SearchRequest
from python_code import ShortReview
from python_code import Wishlist
from python_code import book

def test_book___init__():
    assert book.__init__(book('', '', '', '', 0.0, shortReview26=ShortReview(), catalog29=Catalog(), searchRequest39=SearchRequest(), wishlist49=Wishlist(), basket51=Basket(), order53=Order(), review18=Review_Interface(), detailDescription20=DetailDescription()), '', '', '', '', 0.0, shortReview26=ShortReview(), catalog29=Catalog(), searchRequest39=SearchRequest(), wishlist49=Wishlist(), basket51=Basket(), order53=Order(), review18=Review_Interface(), detailDescription20=DetailDescription()) == None

