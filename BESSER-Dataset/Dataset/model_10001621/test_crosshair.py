from python_code import Essay

def test_Essay___init__():
    assert Essay.__init__(Essay('\x00\x00', '', '', True), '', '', '', False) == None


from python_code import MC

def test_MC___init__():
    assert MC.__init__(MC('\x00\x00', '', False, ''), '', '', False, '') == None


from python_code import Matching

def test_Matching___init__():
    assert Matching.__init__(Matching('', '', '', '', False), '', '', '', '', False) == None


from python_code import Ranking

def test_Ranking___init__():
    assert Ranking.__init__(Ranking('\x00\x00', '', '', True), '', '', '', False) == None


from python_code import ShortAnswer

def test_ShortAnswer___init__():
    assert ShortAnswer.__init__(ShortAnswer('\x00\x00', '', '', True), '', '', '', False) == None


from python_code import TF

def test_TF___init__():
    assert TF.__init__(TF('\x00\x00', '', '', True), '', '', '', False) == None

