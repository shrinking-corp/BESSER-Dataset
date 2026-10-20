from python_code import PyDslRep_AbstractCrossMove
from python_code import PyDslRep_AbstractMove
from python_code import PyDslRep_DataMove

def test_PyDslRep_DataMove___init__():
    assert PyDslRep_DataMove.__init__(PyDslRep_DataMove(False, '', '\x00\x00', PyDslRep_DataMove=PyDslRep_AbstractMove(), PyDslRep_DataMove15=PyDslRep_AbstractCrossMove()), False, '', '', PyDslRep_DataMove=PyDslRep_AbstractMove(), PyDslRep_DataMove15=PyDslRep_AbstractCrossMove()) == None


from python_code import PyDslRep_Move

def test_PyDslRep_Move___init__():
    assert PyDslRep_Move.__init__(PyDslRep_Move(''), '') == None

