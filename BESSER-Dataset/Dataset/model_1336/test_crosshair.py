from python_code import miniOCL_BooleanExpCS

def test_miniOCL_BooleanExpCS___init__():
    assert miniOCL_BooleanExpCS.__init__(miniOCL_BooleanExpCS(True), False) == None


from python_code import miniOCL_IntLiteralExpCS

def test_miniOCL_IntLiteralExpCS___init__():
    assert miniOCL_IntLiteralExpCS.__init__(miniOCL_IntLiteralExpCS(0), 0) == None


from python_code import miniOCL_PathElementCS
from python_code import miniOCL_PathNameCS

def test_miniOCL_PathElementCS___init__():
    assert miniOCL_PathElementCS.__init__(miniOCL_PathElementCS('', miniOCL_PathElementCS=miniOCL_PathNameCS()), '', miniOCL_PathElementCS=miniOCL_PathNameCS()) == None


from python_code import miniOCL_StringLiteralExpCS

def test_miniOCL_StringLiteralExpCS___init__():
    assert miniOCL_StringLiteralExpCS.__init__(miniOCL_StringLiteralExpCS(''), '') == None

