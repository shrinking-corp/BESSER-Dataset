from python_code import cpntools_AuxBox

def test_cpntools_AuxBox___init__():
    assert cpntools_AuxBox.__init__(cpntools_AuxBox(0, 0), 0, 0) == None


from python_code import cpntools_AuxEllipse

def test_cpntools_AuxEllipse___init__():
    assert cpntools_AuxEllipse.__init__(cpntools_AuxEllipse(0, 0), 0, 0) == None


from python_code import cpntools_AuxText

def test_cpntools_AuxText___init__():
    assert cpntools_AuxText.__init__(cpntools_AuxText(''), '') == None


from python_code import cpntools_Block
from python_code import cpntools_Declaration

def test_cpntools_Block___init__():
    assert cpntools_Block.__init__(cpntools_Block('', Block=cpntools_Declaration(), block=set()), '', Block=cpntools_Declaration(), block=set()) == None


from python_code import cpntools_Boolean

def test_cpntools_Boolean___init__():
    assert cpntools_Boolean.__init__(cpntools_Boolean(''), '') == None


from python_code import cpntools_Enumerated

def test_cpntools_Enumerated___init__():
    assert cpntools_Enumerated.__init__(cpntools_Enumerated(''), '') == None


from python_code import cpntools_Cpnet
from python_code import cpntools_Declaration
from python_code import cpntools_Globbox

def test_cpntools_Globbox___init__():
    assert cpntools_Globbox.__init__(cpntools_Globbox('', Globbox34=cpntools_Declaration(), Globbox=cpntools_Cpnet(), globbox=cpntools_Cpnet(), globbox45=set()), '', Globbox34=cpntools_Declaration(), Globbox=cpntools_Cpnet(), globbox=cpntools_Cpnet(), globbox45=set()) == None


from python_code import cpntools_Globref

def test_cpntools_Globref___init__():
    assert cpntools_Globref.__init__(cpntools_Globref(''), '') == None


from python_code import cpntools_Index

def test_cpntools_Index___init__():
    assert cpntools_Index.__init__(cpntools_Index(''), '') == None


from python_code import cpntools_Integer

def test_cpntools_Integer___init__():
    assert cpntools_Integer.__init__(cpntools_Integer(''), '') == None


from python_code import cpntools_LargeInteger

def test_cpntools_LargeInteger___init__():
    assert cpntools_LargeInteger.__init__(cpntools_LargeInteger(''), '') == None


from python_code import cpntools_Ml

def test_cpntools_Ml___init__():
    assert cpntools_Ml.__init__(cpntools_Ml(''), '') == None


from python_code import cpntools_Real

def test_cpntools_Real___init__():
    assert cpntools_Real.__init__(cpntools_Real(''), '') == None


from python_code import cpntools_String

def test_cpntools_String___init__():
    assert cpntools_String.__init__(cpntools_String('', '\x00'), '\x00\x00', '') == None


from python_code import cpntools_Unit

def test_cpntools_Unit___init__():
    assert cpntools_Unit.__init__(cpntools_Unit(''), '') == None

