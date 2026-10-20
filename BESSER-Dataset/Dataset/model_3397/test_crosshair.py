from python_code import ramRoot_GenericNode
from python_code import ramRoot_MT__Element

def test_ramRoot_MT__Element___init__():
    assert ramRoot_MT__Element.__init__(ramRoot_MT__Element('', False, ramRoot_MT__Element=ramRoot_GenericNode()), '', False, ramRoot_MT__Element=ramRoot_GenericNode()) == None


from python_code import ramRoot_MTpos__Restaurant
from python_code import ramRoot_MTpos__Waitress

def test_ramRoot_MTpos__Waitress___init__():
    assert ramRoot_MTpos__Waitress.__init__(ramRoot_MTpos__Waitress('', ramRoot_MTpos__Waitress13=ramRoot_MTpos__Restaurant(), ramRoot_MTpos__Waitress=set()), '', ramRoot_MTpos__Waitress13=ramRoot_MTpos__Restaurant(), ramRoot_MTpos__Waitress=set()) == None


from python_code import ramRoot_MTpre__Element

def test_ramRoot_MTpre__Element___init__():
    assert ramRoot_MTpre__Element.__init__(ramRoot_MTpre__Element(True), False) == None


from python_code import ramRoot_MTpre__Restaurant
from python_code import ramRoot_MTpre__Waitress

def test_ramRoot_MTpre__Waitress___init__():
    assert ramRoot_MTpre__Waitress.__init__(ramRoot_MTpre__Waitress('', ramRoot_MTpre__Waitress11=ramRoot_MTpre__Restaurant(), ramRoot_MTpre__Waitress=set()), '', ramRoot_MTpre__Waitress11=ramRoot_MTpre__Restaurant(), ramRoot_MTpre__Waitress=set()) == None

