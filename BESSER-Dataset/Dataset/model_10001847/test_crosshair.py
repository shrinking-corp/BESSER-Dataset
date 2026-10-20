from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('\x00\x00', '', lineItems10=set()), '', '', lineItems10=set()) == None


from python_code import Redis
from python_code import RedisClient

def test_RedisClient___init__():
    assert RedisClient.__init__(RedisClient('', '', '\x00\x00', account4=Redis()), '', '', '', account4=Redis()) == None

