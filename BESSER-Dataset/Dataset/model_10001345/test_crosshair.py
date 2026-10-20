from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import model2_A
from python_code import model2_R

def test_model2_A___init__():
    assert model2_A.__init__(model2_A('', r6=model2_R(), b9=set()), '', r6=model2_R(), b9=set()) == None


from python_code import model2_Y

def test_model2_Y___init__():
    assert model2_Y.__init__(model2_Y(''), '') == None

