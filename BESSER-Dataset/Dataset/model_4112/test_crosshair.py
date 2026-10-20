from python_code import wh_Affect

def test_wh_Affect___init__():
    assert wh_Affect.__init__(wh_Affect('', '\x00'), '\x00\x00', '') == None


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


from python_code import wh_Definition
from python_code import wh_Program
from python_code import wh_Wh

def test_wh_Program___init__():
    assert wh_Program.__init__(wh_Program('', wh_Program=wh_Wh(), wh_Program2=wh_Definition()), '', wh_Program=wh_Wh(), wh_Program2=wh_Definition()) == None

