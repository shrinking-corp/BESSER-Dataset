from python_code import kmLogo_VM_Point

def test_kmLogo_VM_Point___init__():
    assert kmLogo_VM_Point.__init__(kmLogo_VM_Point('', '\x00'), '\x00\x00', '') == None


from python_code import Point
from python_code import kmLogo_VM_Turtle

def test_kmLogo_VM_Turtle___init__():
    assert kmLogo_VM_Turtle.__init__(kmLogo_VM_Turtle('', '', kmLogo_VM_Turtle=Point(), kmLogo_VM_Turtle2=set(), kmLogo_VM_Turtle4=set()), '', '', kmLogo_VM_Turtle=Point(), kmLogo_VM_Turtle2=set(), kmLogo_VM_Turtle4=set()) == None

