from python_code import qvt_cst_ErrorNode

def test_qvt_cst_ErrorNode___init__():
    assert qvt_cst_ErrorNode.__init__(qvt_cst_ErrorNode(''), '') == None


from python_code import cst_qvt_EObject
from python_code import qvt_cst_IdentifierCS

def test_qvt_cst_IdentifierCS___init__():
    assert qvt_cst_IdentifierCS.__init__(qvt_cst_IdentifierCS('', qvt_cst_IdentifierCS=cst_qvt_EObject()), '', qvt_cst_IdentifierCS=cst_qvt_EObject()) == None

