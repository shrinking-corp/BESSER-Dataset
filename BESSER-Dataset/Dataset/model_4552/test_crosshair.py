from python_code import polybot_Move

def test_polybot_Move___init__():
    assert polybot_Move.__init__(polybot_Move(0, 0), 0, 0) == None


from python_code import polybot_Bot
from python_code import polybot_Point

def test_polybot_Point___init__():
    assert polybot_Point.__init__(polybot_Point(0, 0, polybot_Point=polybot_Bot()), 0, 0, polybot_Point=polybot_Bot()) == None


from python_code import polybot_While

def test_polybot_While___init__():
    assert polybot_While.__init__(polybot_While(0, polybot_While=set()), 0, polybot_While=set()) == None

