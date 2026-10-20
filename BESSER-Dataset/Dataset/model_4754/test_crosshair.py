from python_code import myffbd_Flow
from python_code import myffbd_Item

def test_myffbd_Item___init__():
    assert myffbd_Item.__init__(myffbd_Item('', myffbd_Item=myffbd_Flow()), '', myffbd_Item=myffbd_Flow()) == None

