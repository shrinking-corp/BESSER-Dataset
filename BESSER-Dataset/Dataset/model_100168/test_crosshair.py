from python_code import rdbms_CheckCon
from python_code import rdbms_Table

def test_rdbms_CheckCon___init__():
    assert rdbms_CheckCon.__init__(rdbms_CheckCon('', rdbms_CheckCon=rdbms_Table()), '', rdbms_CheckCon=rdbms_Table()) == None


from python_code import rdbms_Constraints

def test_rdbms_Constraints___init__():
    assert rdbms_Constraints.__init__(rdbms_Constraints('', '\x00'), '\x00\x00', '') == None


from python_code import rdbms_ModelElement

def test_rdbms_ModelElement___init__():
    assert rdbms_ModelElement.__init__(rdbms_ModelElement(''), '') == None

