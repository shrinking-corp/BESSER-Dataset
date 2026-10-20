from python_code import wh_Definition
from python_code import wh_Function
from python_code import wh_Program

def test_wh_Function___init__():
    assert wh_Function.__init__(wh_Function('', wh_Function=wh_Program(), wh_Function4=wh_Definition()), '', wh_Function=wh_Program(), wh_Function4=wh_Definition()) == None


from python_code import wh_Definition
from python_code import wh_Input

def test_wh_Input___init__():
    assert wh_Input.__init__(wh_Input('', wh_Input=wh_Definition()), '', wh_Input=wh_Definition()) == None


from python_code import wh_Nop

def test_wh_Nop___init__():
    assert wh_Nop.__init__(wh_Nop(''), '') == None


from python_code import wh_Definition
from python_code import wh_Output

def test_wh_Output___init__():
    assert wh_Output.__init__(wh_Output('', wh_Output=wh_Definition()), '', wh_Output=wh_Definition()) == None


from python_code import wh_Assign
from python_code import wh_Vars

def test_wh_Vars___init__():
    assert wh_Vars.__init__(wh_Vars('', wh_Vars=wh_Assign()), '', wh_Vars=wh_Assign()) == None

