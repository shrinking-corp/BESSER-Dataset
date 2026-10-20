from python_code import helloWorldDsl_Greeting
from python_code import helloWorldDsl_Model

def test_helloWorldDsl_Greeting___init__():
    assert helloWorldDsl_Greeting.__init__(helloWorldDsl_Greeting('', helloWorldDsl_Greeting=helloWorldDsl_Model()), '', helloWorldDsl_Greeting=helloWorldDsl_Model()) == None

