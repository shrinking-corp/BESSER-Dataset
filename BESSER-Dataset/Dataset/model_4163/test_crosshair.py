from python_code import resource_Greeting
from python_code import resource_Model

def test_resource_Greeting___init__():
    assert resource_Greeting.__init__(resource_Greeting('', resource_Greeting=resource_Model()), '', resource_Greeting=resource_Model()) == None

