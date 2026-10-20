from python_code import Styling_BooleanParameter

def test_Styling_BooleanParameter___init__():
    assert Styling_BooleanParameter.__init__(Styling_BooleanParameter(True), False) == None


from python_code import Styling_ConstantPattern

def test_Styling_ConstantPattern___init__():
    assert Styling_ConstantPattern.__init__(Styling_ConstantPattern(''), '') == None


from python_code import Styling_IntParameter

def test_Styling_IntParameter___init__():
    assert Styling_IntParameter.__init__(Styling_IntParameter(0), 0) == None


from python_code import Styling_ModelPattern

def test_Styling_ModelPattern___init__():
    assert Styling_ModelPattern.__init__(Styling_ModelPattern(''), '') == None


from python_code import Styling_OperationPattern

def test_Styling_OperationPattern___init__():
    assert Styling_OperationPattern.__init__(Styling_OperationPattern('\x00', Styling_OperationPattern=set()), '', Styling_OperationPattern=set()) == None


from python_code import Styling_StringParameter

def test_Styling_StringParameter___init__():
    assert Styling_StringParameter.__init__(Styling_StringParameter(''), '') == None


from python_code import Styling_Default
from python_code import Styling_Styling
from python_code import Styling_StylingModel

def test_Styling_StylingModel___init__():
    assert Styling_StylingModel.__init__(Styling_StylingModel('', Styling_StylingModel=set(), Styling_StylingModel2=Styling_Default(), Styling_StylingModel13=Styling_Styling()), '', Styling_StylingModel=set(), Styling_StylingModel2=Styling_Default(), Styling_StylingModel13=Styling_Styling()) == None

