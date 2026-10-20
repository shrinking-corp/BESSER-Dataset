from python_code import myDsl_Import

def test_myDsl_Import___init__():
    assert myDsl_Import.__init__(myDsl_Import(''), '') == None


from python_code import myDsl_Namespace

def test_myDsl_Namespace___init__():
    assert myDsl_Namespace.__init__(myDsl_Namespace('', myDsl_Namespace=set()), '', myDsl_Namespace=set()) == None

