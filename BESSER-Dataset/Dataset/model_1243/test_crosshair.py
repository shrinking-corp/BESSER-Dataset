from python_code import ocl_cst_BooleanLiteralExpCS

def test_ocl_cst_BooleanLiteralExpCS___init__():
    assert ocl_cst_BooleanLiteralExpCS.__init__(ocl_cst_BooleanLiteralExpCS(''), '') == None


from python_code import ocl_cst_CSTNode

def test_ocl_cst_CSTNode___init__():
    assert ocl_cst_CSTNode.__init__(ocl_cst_CSTNode(0, 0), 0, 0) == None


from python_code import ocl_cst_CollectionLiteralExpCS

def test_ocl_cst_CollectionLiteralExpCS___init__():
    assert ocl_cst_CollectionLiteralExpCS.__init__(ocl_cst_CollectionLiteralExpCS('', ocl_cst_CollectionLiteralExpCS=set()), '', ocl_cst_CollectionLiteralExpCS=set()) == None


from python_code import ocl_cst_IntegerLiteralExpCS

def test_ocl_cst_IntegerLiteralExpCS___init__():
    assert ocl_cst_IntegerLiteralExpCS.__init__(ocl_cst_IntegerLiteralExpCS(''), '') == None


from python_code import ocl_cst_InvalidLiteralExpCS

def test_ocl_cst_InvalidLiteralExpCS___init__():
    assert ocl_cst_InvalidLiteralExpCS.__init__(ocl_cst_InvalidLiteralExpCS(''), '') == None


from python_code import ocl_cst_IsMarkedPreCS

def test_ocl_cst_IsMarkedPreCS___init__():
    assert ocl_cst_IsMarkedPreCS.__init__(ocl_cst_IsMarkedPreCS(True), False) == None


from python_code import ocl_cst_NullLiteralExpCS

def test_ocl_cst_NullLiteralExpCS___init__():
    assert ocl_cst_NullLiteralExpCS.__init__(ocl_cst_NullLiteralExpCS(''), '') == None


from python_code import ocl_cst_PrimitiveLiteralExpCS

def test_ocl_cst_PrimitiveLiteralExpCS___init__():
    assert ocl_cst_PrimitiveLiteralExpCS.__init__(ocl_cst_PrimitiveLiteralExpCS(''), '') == None


from python_code import ocl_cst_RealLiteralExpCS

def test_ocl_cst_RealLiteralExpCS___init__():
    assert ocl_cst_RealLiteralExpCS.__init__(ocl_cst_RealLiteralExpCS(''), '') == None


from python_code import ocl_cst_StringLiteralExpCS

def test_ocl_cst_StringLiteralExpCS___init__():
    assert ocl_cst_StringLiteralExpCS.__init__(ocl_cst_StringLiteralExpCS(''), '') == None

