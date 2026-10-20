from python_code import QuestonOrAnswer
from python_code import User

def test_QuestonOrAnswer___init__():
    assert QuestonOrAnswer.__init__(QuestonOrAnswer('', user17=User()), '', user17=User()) == None

