from python_code import pyrep_AbstractCrossMove
from python_code import pyrep_AbstractMove
from python_code import pyrep_DataMove

def test_pyrep_DataMove___init__():
    assert pyrep_DataMove.__init__(pyrep_DataMove(False, '', '\x00\x00', pyrep_DataMove=pyrep_AbstractMove(), pyrep_DataMove15=pyrep_AbstractCrossMove()), False, '', '', pyrep_DataMove=pyrep_AbstractMove(), pyrep_DataMove15=pyrep_AbstractCrossMove()) == None


from python_code import pyrep_Move

def test_pyrep_Move___init__():
    assert pyrep_Move.__init__(pyrep_Move(''), '') == None

