from python_code import dsl_Greeting
from python_code import dsl_Model

def test_dsl_Greeting___init__():
    assert dsl_Greeting.__init__(dsl_Greeting('', dsl_Greeting=dsl_Model()), '', dsl_Greeting=dsl_Model()) == None

