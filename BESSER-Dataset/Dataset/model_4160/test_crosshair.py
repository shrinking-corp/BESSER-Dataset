from python_code import font_Greeting
from python_code import font_Model

def test_font_Greeting___init__():
    assert font_Greeting.__init__(font_Greeting('', font_Greeting=font_Model()), '', font_Greeting=font_Model()) == None

