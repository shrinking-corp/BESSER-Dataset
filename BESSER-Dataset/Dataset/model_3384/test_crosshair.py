from python_code import errors_CheckError

def test_errors_CheckError___init__():
    assert errors_CheckError.__init__(errors_CheckError('', '', '', errors_CheckError=set()), '', '', '', errors_CheckError=set()) == None

