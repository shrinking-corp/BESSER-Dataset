from python_code import archDSL_AltCall

def test_archDSL_AltCall___init__():
    assert archDSL_AltCall.__init__(archDSL_AltCall(False, archDSL_AltCall=set()), False, archDSL_AltCall=set()) == None


from python_code import archDSL_Connector
from python_code import archDSL_Model

def test_archDSL_Connector___init__():
    assert archDSL_Connector.__init__(archDSL_Connector('', archDSL_Connector=archDSL_Model(), archDSL_Connector19=set()), '', archDSL_Connector=archDSL_Model(), archDSL_Connector19=set()) == None

