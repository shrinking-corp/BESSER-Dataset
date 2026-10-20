from python_code import myDsl_Compilation_unit
from python_code import myDsl_Import_statement

def test_myDsl_Import_statement___init__():
    assert myDsl_Import_statement.__init__(myDsl_Import_statement('', '\x00', myDsl_Import_statement=myDsl_Compilation_unit()), '\x00\x00', '', myDsl_Import_statement=myDsl_Compilation_unit()) == None


from python_code import myDsl_Compilation_unit
from python_code import myDsl_Package_statement

def test_myDsl_Package_statement___init__():
    assert myDsl_Package_statement.__init__(myDsl_Package_statement('', myDsl_Package_statement=myDsl_Compilation_unit()), '', myDsl_Package_statement=myDsl_Compilation_unit()) == None

