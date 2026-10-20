from python_code import mDSL_Greeting
from python_code import mDSL_Model

def test_mDSL_Greeting___init__():
    assert mDSL_Greeting.__init__(mDSL_Greeting('', mDSL_Greeting=mDSL_Model()), '', mDSL_Greeting=mDSL_Model()) == None

