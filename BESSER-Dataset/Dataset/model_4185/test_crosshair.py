from python_code import kobold_Greeting
from python_code import kobold_Model

def test_kobold_Greeting___init__():
    assert kobold_Greeting.__init__(kobold_Greeting('', kobold_Greeting=kobold_Model()), '', kobold_Greeting=kobold_Model()) == None

