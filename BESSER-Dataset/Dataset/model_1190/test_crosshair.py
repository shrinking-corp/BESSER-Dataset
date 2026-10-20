from python_code import EssentialOCL_BooleanLiteralExp

def test_EssentialOCL_BooleanLiteralExp___init__():
    assert EssentialOCL_BooleanLiteralExp.__init__(EssentialOCL_BooleanLiteralExp(''), '') == None


from python_code import EssentialOCL_CollectionLiteralExp

def test_EssentialOCL_CollectionLiteralExp___init__():
    assert EssentialOCL_CollectionLiteralExp.__init__(EssentialOCL_CollectionLiteralExp('', EssentialOCL_CollectionLiteralExp=set()), '', EssentialOCL_CollectionLiteralExp=set()) == None


from python_code import EssentialOCL_IntegerLiteralExp

def test_EssentialOCL_IntegerLiteralExp___init__():
    assert EssentialOCL_IntegerLiteralExp.__init__(EssentialOCL_IntegerLiteralExp(''), '') == None


from python_code import EssentialOCL_RealLiteralExp

def test_EssentialOCL_RealLiteralExp___init__():
    assert EssentialOCL_RealLiteralExp.__init__(EssentialOCL_RealLiteralExp(''), '') == None


from python_code import EssentialOCL_StringLiteralExp

def test_EssentialOCL_StringLiteralExp___init__():
    assert EssentialOCL_StringLiteralExp.__init__(EssentialOCL_StringLiteralExp(''), '') == None


from python_code import EssentialOCL_UnlimitedNaturalExp

def test_EssentialOCL_UnlimitedNaturalExp___init__():
    assert EssentialOCL_UnlimitedNaturalExp.__init__(EssentialOCL_UnlimitedNaturalExp(''), '') == None

