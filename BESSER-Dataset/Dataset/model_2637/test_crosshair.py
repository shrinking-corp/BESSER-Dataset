from python_code import model3_ClassWithIDAttribute

def test_model3_ClassWithIDAttribute___init__():
    assert model3_ClassWithIDAttribute.__init__(model3_ClassWithIDAttribute(''), '') == None


from python_code import model3_File

def test_model3_File___init__():
    assert model3_File.__init__(model3_File('', '\x00'), '\x00\x00', '') == None


from python_code import model3_Image

def test_model3_Image___init__():
    assert model3_Image.__init__(model3_Image(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import model3_Polygon

def test_model3_Polygon___init__():
    assert model3_Polygon.__init__(model3_Polygon(''), '') == None


from python_code import model3_PolygonWithDuplicates

def test_model3_PolygonWithDuplicates___init__():
    assert model3_PolygonWithDuplicates.__init__(model3_PolygonWithDuplicates(''), '') == None

