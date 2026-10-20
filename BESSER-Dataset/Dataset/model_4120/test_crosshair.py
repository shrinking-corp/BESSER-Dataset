from python_code import whileLanguage_Definition
from python_code import whileLanguage_Function
from python_code import whileLanguage_Program

def test_whileLanguage_Function___init__():
    assert whileLanguage_Function.__init__(whileLanguage_Function('', whileLanguage_Function=whileLanguage_Program(), whileLanguage_Function2=whileLanguage_Definition()), '', whileLanguage_Function=whileLanguage_Program(), whileLanguage_Function2=whileLanguage_Definition()) == None


from python_code import whileLanguage_Nop

def test_whileLanguage_Nop___init__():
    assert whileLanguage_Nop.__init__(whileLanguage_Nop(''), '') == None


from python_code import whileLanguage_Definition
from python_code import whileLanguage_Read

def test_whileLanguage_Read___init__():
    assert whileLanguage_Read.__init__(whileLanguage_Read('', whileLanguage_Read=whileLanguage_Definition()), '', whileLanguage_Read=whileLanguage_Definition()) == None


from python_code import whileLanguage_Definition
from python_code import whileLanguage_Write

def test_whileLanguage_Write___init__():
    assert whileLanguage_Write.__init__(whileLanguage_Write('', whileLanguage_Write=whileLanguage_Definition()), '', whileLanguage_Write=whileLanguage_Definition()) == None

