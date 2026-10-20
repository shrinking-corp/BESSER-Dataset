from python_code import miniOCL_AccVarCS
from python_code import miniOCL_ExistsExpCS
from python_code import miniOCL_ExpCS
from python_code import miniOCL_ForAllExpCS
from python_code import miniOCL_IterateExpCS
from python_code import miniOCL_PathNameCS

def test_miniOCL_AccVarCS___init__():
    assert miniOCL_AccVarCS.__init__(miniOCL_AccVarCS('', miniOCL_AccVarCS=miniOCL_IterateExpCS(), miniOCL_AccVarCS60=miniOCL_PathNameCS(), miniOCL_AccVarCS63=miniOCL_ExpCS(), miniOCL_AccVarCS72=miniOCL_ExistsExpCS(), miniOCL_AccVarCS85=miniOCL_ForAllExpCS()), '', miniOCL_AccVarCS=miniOCL_IterateExpCS(), miniOCL_AccVarCS60=miniOCL_PathNameCS(), miniOCL_AccVarCS63=miniOCL_ExpCS(), miniOCL_AccVarCS72=miniOCL_ExistsExpCS(), miniOCL_AccVarCS85=miniOCL_ForAllExpCS()) == None


from python_code import miniOCL_BooleanExpCS

def test_miniOCL_BooleanExpCS___init__():
    assert miniOCL_BooleanExpCS.__init__(miniOCL_BooleanExpCS(True), False) == None


from python_code import miniOCL_IntLiteralExpCS

def test_miniOCL_IntLiteralExpCS___init__():
    assert miniOCL_IntLiteralExpCS.__init__(miniOCL_IntLiteralExpCS(0), 0) == None


from python_code import miniOCL_NavigationPathVariableCS

def test_miniOCL_NavigationPathVariableCS___init__():
    assert miniOCL_NavigationPathVariableCS.__init__(miniOCL_NavigationPathVariableCS(''), '') == None


from python_code import miniOCL_PathVariableCS

def test_miniOCL_PathVariableCS___init__():
    assert miniOCL_PathVariableCS.__init__(miniOCL_PathVariableCS(''), '') == None


from python_code import miniOCL_StringLiteralExpCS

def test_miniOCL_StringLiteralExpCS___init__():
    assert miniOCL_StringLiteralExpCS.__init__(miniOCL_StringLiteralExpCS(''), '') == None

