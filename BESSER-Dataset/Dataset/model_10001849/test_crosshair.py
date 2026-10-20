from python_code import Cluster
from python_code import Redis

def test_Cluster___init__():
    assert Cluster.__init__(Cluster('', redis21=Redis()), '', redis21=Redis()) == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('\x00\x00', '', lineItems10=set()), '', '', lineItems10=set()) == None

