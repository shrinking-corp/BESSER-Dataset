from python_code import classescs_NamedElementCS

def test_classescs_NamedElementCS___init__():
    assert classescs_NamedElementCS.__init__(classescs_NamedElementCS(''), '') == None


from python_code import classescs_ClassCS
from python_code import classescs_OperationCS
from python_code import classescs_PathNameCS

def test_classescs_OperationCS___init__():
    assert classescs_OperationCS.__init__(classescs_OperationCS('', classescs_OperationCS=classescs_ClassCS(), classescs_OperationCS19=set(), classescs_OperationCS21=classescs_PathNameCS()), '', classescs_OperationCS=classescs_ClassCS(), classescs_OperationCS19=set(), classescs_OperationCS21=classescs_PathNameCS()) == None

