from python_code import gDSL_CONS
from python_code import gDSL_ConDecl

def test_gDSL_CONS___init__():
    assert gDSL_CONS.__init__(gDSL_CONS('', gDSL_CONS=gDSL_ConDecl()), '', gDSL_CONS=gDSL_ConDecl()) == None


from python_code import gDSL_SelectExp

def test_gDSL_SelectExp___init__():
    assert gDSL_SelectExp.__init__(gDSL_SelectExp('', gDSL_SelectExp=set()), '', gDSL_SelectExp=set()) == None

