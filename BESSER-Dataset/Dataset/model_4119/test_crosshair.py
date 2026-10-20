from python_code import whileComp_Affectation

def test_whileComp_Affectation___init__():
    assert whileComp_Affectation.__init__(whileComp_Affectation('', whileComp_Affectation=set()), '', whileComp_Affectation=set()) == None


from python_code import whileComp_Cons

def test_whileComp_Cons___init__():
    assert whileComp_Cons.__init__(whileComp_Cons(''), '') == None


from python_code import whileComp_Definition
from python_code import whileComp_Function
from python_code import whileComp_Program

def test_whileComp_Function___init__():
    assert whileComp_Function.__init__(whileComp_Function('', whileComp_Function=whileComp_Program(), whileComp_Function2=whileComp_Definition()), '', whileComp_Function=whileComp_Program(), whileComp_Function2=whileComp_Definition()) == None


from python_code import whileComp_Hd

def test_whileComp_Hd___init__():
    assert whileComp_Hd.__init__(whileComp_Hd(''), '') == None


from python_code import whileComp_List

def test_whileComp_List___init__():
    assert whileComp_List.__init__(whileComp_List(''), '') == None


from python_code import whileComp_Nil2

def test_whileComp_Nil2___init__():
    assert whileComp_Nil2.__init__(whileComp_Nil2(''), '') == None


from python_code import whileComp_Nop

def test_whileComp_Nop___init__():
    assert whileComp_Nop.__init__(whileComp_Nop(''), '') == None


from python_code import whileComp_Definition
from python_code import whileComp_Read

def test_whileComp_Read___init__():
    assert whileComp_Read.__init__(whileComp_Read('', whileComp_Read=whileComp_Definition()), '', whileComp_Read=whileComp_Definition()) == None


from python_code import whileComp_Tl

def test_whileComp_Tl___init__():
    assert whileComp_Tl.__init__(whileComp_Tl(''), '') == None


from python_code import whileComp_Definition
from python_code import whileComp_Write

def test_whileComp_Write___init__():
    assert whileComp_Write.__init__(whileComp_Write('', whileComp_Write=whileComp_Definition()), '', whileComp_Write=whileComp_Definition()) == None

