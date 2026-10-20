from python_code import qvtcore_cst_DomainCS

def test_qvtcore_cst_DomainCS___init__():
    assert qvtcore_cst_DomainCS.__init__(qvtcore_cst_DomainCS(False, False), False, False) == None


from python_code import OperationCallExpCS
from python_code import qvtcore_cst_EnforcementOperationCS

def test_qvtcore_cst_EnforcementOperationCS___init__():
    assert qvtcore_cst_EnforcementOperationCS.__init__(qvtcore_cst_EnforcementOperationCS(True, qvtcore_cst_EnforcementOperationCS=OperationCallExpCS()), False, qvtcore_cst_EnforcementOperationCS=OperationCallExpCS()) == None

