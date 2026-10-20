from python_code import ocl_cst_BooleanLiteralExpCS

def test_ocl_cst_BooleanLiteralExpCS___init__():
    assert ocl_cst_BooleanLiteralExpCS.__init__(ocl_cst_BooleanLiteralExpCS(''), '') == None


from python_code import ocl_cst_CSTNode

def test_ocl_cst_CSTNode___init__():
    assert ocl_cst_CSTNode.__init__(ocl_cst_CSTNode(0, 0, '', '', ''), 0, 0, '', '', '') == None


from python_code import ocl_cst_CollectionLiteralExpCS

def test_ocl_cst_CollectionLiteralExpCS___init__():
    assert ocl_cst_CollectionLiteralExpCS.__init__(ocl_cst_CollectionLiteralExpCS('', ocl_cst_CollectionLiteralExpCS=set()), '', ocl_cst_CollectionLiteralExpCS=set()) == None


from python_code import TypeCS
from python_code import ocl_cst_CollectionTypeCS

def test_ocl_cst_CollectionTypeCS___init__():
    assert ocl_cst_CollectionTypeCS.__init__(ocl_cst_CollectionTypeCS('', ocl_cst_CollectionTypeCS=TypeCS()), '\x00', ocl_cst_CollectionTypeCS=TypeCS()) == None


from python_code import DefExpressionCS
from python_code import ocl_cst_ClassifierContextDeclCS
from python_code import ocl_cst_DefCS

def test_ocl_cst_DefCS___init__():
    assert ocl_cst_DefCS.__init__(ocl_cst_DefCS(True, ocl_cst_DefCS=DefExpressionCS(), InvOrDefCS=ocl_cst_ClassifierContextDeclCS()), False, ocl_cst_DefCS=DefExpressionCS(), InvOrDefCS=ocl_cst_ClassifierContextDeclCS()) == None


from python_code import ocl_cst_IntegerLiteralExpCS

def test_ocl_cst_IntegerLiteralExpCS___init__():
    assert ocl_cst_IntegerLiteralExpCS.__init__(ocl_cst_IntegerLiteralExpCS('', '', '\x00\x00'), '', '', '') == None


from python_code import ocl_cst_OperationCallExpCS

def test_ocl_cst_OperationCallExpCS___init__():
    assert ocl_cst_OperationCallExpCS.__init__(ocl_cst_OperationCallExpCS(''), '') == None


from python_code import ocl_cst_PrimitiveLiteralExpCS

def test_ocl_cst_PrimitiveLiteralExpCS___init__():
    assert ocl_cst_PrimitiveLiteralExpCS.__init__(ocl_cst_PrimitiveLiteralExpCS(''), '') == None


from python_code import ocl_cst_RealLiteralExpCS

def test_ocl_cst_RealLiteralExpCS___init__():
    assert ocl_cst_RealLiteralExpCS.__init__(ocl_cst_RealLiteralExpCS(''), '') == None


from python_code import ocl_cst_StringLiteralExpCS

def test_ocl_cst_StringLiteralExpCS___init__():
    assert ocl_cst_StringLiteralExpCS.__init__(ocl_cst_StringLiteralExpCS('', '\x00'), '\x00\x00', '') == None


from python_code import ocl_cst_UnlimitedNaturalLiteralExpCS

def test_ocl_cst_UnlimitedNaturalLiteralExpCS___init__():
    assert ocl_cst_UnlimitedNaturalLiteralExpCS.__init__(ocl_cst_UnlimitedNaturalLiteralExpCS('', '', '\x00\x00'), '', '', '') == None

