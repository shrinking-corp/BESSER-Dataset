from python_code import PagosPim_Add
from python_code import PagosPim_Expression

def test_PagosPim_Add___init__():
    assert PagosPim_Add.__init__(PagosPim_Add('', PagosPim_Add90=PagosPim_Expression(), PagosPim_Add=PagosPim_Expression()), '', PagosPim_Add90=PagosPim_Expression(), PagosPim_Add=PagosPim_Expression()) == None


from python_code import PagosPim_Application

def test_PagosPim_Application___init__():
    assert PagosPim_Application.__init__(PagosPim_Application('\x00', PagosPim_Application=set(), PagosPim_Application2=set(), PagosPim_Application4=set(), PagosPim_Application6=set(), PagosPim_Application8=set()), '', PagosPim_Application=set(), PagosPim_Application2=set(), PagosPim_Application4=set(), PagosPim_Application6=set(), PagosPim_Application8=set()) == None


from python_code import PagosPim_AttributeDefinition
from python_code import PagosPim_EObject

def test_PagosPim_AttributeDefinition___init__():
    assert PagosPim_AttributeDefinition.__init__(PagosPim_AttributeDefinition('', '\x00', PagosPim_AttributeDefinition=PagosPim_EObject()), '\x00\x00', '', PagosPim_AttributeDefinition=PagosPim_EObject()) == None


from python_code import PagosPim_Expression
from python_code import PagosPim_Mult

def test_PagosPim_Mult___init__():
    assert PagosPim_Mult.__init__(PagosPim_Mult('', PagosPim_Mult=PagosPim_Expression(), PagosPim_Mult95=PagosPim_Expression()), '', PagosPim_Mult=PagosPim_Expression(), PagosPim_Mult95=PagosPim_Expression()) == None


from python_code import PagosPim_Body
from python_code import PagosPim_ElseSegment
from python_code import PagosPim_IfCondition
from python_code import PagosPim_Return

def test_PagosPim_Return___init__():
    assert PagosPim_Return.__init__(PagosPim_Return('', PagosPim_Return69=PagosPim_ElseSegment(), PagosPim_Return=set(), PagosPim_Return49=PagosPim_Body(), PagosPim_Return60=PagosPim_IfCondition()), '', PagosPim_Return69=PagosPim_ElseSegment(), PagosPim_Return=set(), PagosPim_Return49=PagosPim_Body(), PagosPim_Return60=PagosPim_IfCondition()) == None

