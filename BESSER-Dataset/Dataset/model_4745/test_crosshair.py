from python_code import sWML_ContentLayer
from python_code import sWML_HypertextLayer
from python_code import sWML_WebModel

def test_sWML_WebModel___init__():
    assert sWML_WebModel.__init__(sWML_WebModel('', sWML_WebModel=sWML_HypertextLayer(), sWML_WebModel2=sWML_ContentLayer()), '', sWML_WebModel=sWML_HypertextLayer(), sWML_WebModel2=sWML_ContentLayer()) == None

