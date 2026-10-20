from python_code import mydsl_MyElement
from python_code import mydsl_MyReference

def test_mydsl_MyElement___init__():
    assert mydsl_MyElement.__init__(mydsl_MyElement('', mydsl_MyElement=mydsl_MyReference()), '', mydsl_MyElement=mydsl_MyReference()) == None


from python_code import mydsl_MyModel

def test_mydsl_MyModel___init__():
    assert mydsl_MyModel.__init__(mydsl_MyModel('', mydsl_MyModel=set()), '', mydsl_MyModel=set()) == None

