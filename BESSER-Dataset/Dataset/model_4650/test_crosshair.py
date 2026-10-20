from python_code import di_DiNode

def test_di_DiNode___init__():
    assert di_DiNode.__init__(di_DiNode('', di_DiNode=set()), '', di_DiNode=set()) == None


from python_code import di_ContainerShape
from python_code import di_Link
from python_code import di_Shape

def test_di_Shape___init__():
    assert di_Shape.__init__(di_Shape(0, 0, 0, 0, Shape6=di_Link(), target=set(), source=set(), di_Shape=di_ContainerShape(), Shape=di_Link()), 0, 0, 0, 0, Shape6=di_Link(), target=set(), source=set(), di_Shape=di_ContainerShape(), Shape=di_Link()) == None

