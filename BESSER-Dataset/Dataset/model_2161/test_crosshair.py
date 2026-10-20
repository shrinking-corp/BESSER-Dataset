from python_code import egt_ColorRegistry
from python_code import egt_GraphModel

def test_egt_ColorRegistry___init__():
    assert egt_ColorRegistry.__init__(egt_ColorRegistry('', egt_ColorRegistry=egt_GraphModel()), '', egt_ColorRegistry=egt_GraphModel()) == None

def test_egt_ColorRegistry_dispose():
    assert egt_ColorRegistry.dispose(egt_ColorRegistry('', egt_ColorRegistry=egt_GraphModel())) == None

def test_egt_ColorRegistry_init():
    assert egt_ColorRegistry.init(egt_ColorRegistry('', egt_ColorRegistry=egt_GraphModel())) == None

