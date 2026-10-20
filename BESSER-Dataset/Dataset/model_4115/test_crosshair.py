from python_code import whileCpp_Definition
from python_code import whileCpp_Function
from python_code import whileCpp_Program

def test_whileCpp_Function___init__():
    assert whileCpp_Function.__init__(whileCpp_Function('', whileCpp_Function=whileCpp_Program(), whileCpp_Function2=whileCpp_Definition()), '', whileCpp_Function=whileCpp_Program(), whileCpp_Function2=whileCpp_Definition()) == None


from python_code import whileCpp_Definition
from python_code import whileCpp_Input

def test_whileCpp_Input___init__():
    assert whileCpp_Input.__init__(whileCpp_Input('', whileCpp_Input=whileCpp_Definition()), '', whileCpp_Input=whileCpp_Definition()) == None


from python_code import whileCpp_Definition
from python_code import whileCpp_Output

def test_whileCpp_Output___init__():
    assert whileCpp_Output.__init__(whileCpp_Output('', whileCpp_Output=whileCpp_Definition()), '', whileCpp_Output=whileCpp_Definition()) == None

