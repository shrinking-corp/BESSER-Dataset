from python_code import errors_CheckError
from python_code import errors_Ck
from python_code import errors_Table

def test_errors_CheckError___init__():
    assert errors_CheckError.__init__(errors_CheckError('', errors_CheckError=errors_Ck(), errors_CheckError13=errors_Table(), errors_CheckError16=set()), '', errors_CheckError=errors_Ck(), errors_CheckError13=errors_Table(), errors_CheckError16=set()) == None


from python_code import errors_Error
from python_code import errors_Errores

def test_errors_Error___init__():
    assert errors_Error.__init__(errors_Error('', '\x00', errors_Error=errors_Errores()), '\x00\x00', '', errors_Error=errors_Errores()) == None


from python_code import errors_Fk
from python_code import errors_ForeignError
from python_code import errors_Table

def test_errors_ForeignError___init__():
    assert errors_ForeignError.__init__(errors_ForeignError('', errors_ForeignError6=set(), errors_ForeignError8=errors_Fk(), errors_ForeignError10=set(), errors_ForeignError=errors_Table(), errors_ForeignError3=errors_Table()), '', errors_ForeignError6=set(), errors_ForeignError8=errors_Fk(), errors_ForeignError10=set(), errors_ForeignError=errors_Table(), errors_ForeignError3=errors_Table()) == None

