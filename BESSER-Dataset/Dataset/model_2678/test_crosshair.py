from python_code import refinher_A
from python_code import refinher_Named

def test_refinher_Named___init__():
    assert refinher_Named.__init__(refinher_Named('', refinher_Named=refinher_A()), '', refinher_Named=refinher_A()) == None

