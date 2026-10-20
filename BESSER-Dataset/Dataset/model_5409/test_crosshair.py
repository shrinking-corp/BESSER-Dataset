from python_code import fta_Diagram
from python_code import fta_FTA

def test_fta_Diagram___init__():
    assert fta_Diagram.__init__(fta_Diagram('', '', '\x00\x00', fta_Diagram=fta_FTA()), '', '', '', fta_Diagram=fta_FTA()) == None

