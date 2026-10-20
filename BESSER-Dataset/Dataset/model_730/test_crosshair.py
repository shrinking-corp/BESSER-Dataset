from python_code import dc_Bounds

def test_dc_Bounds___init__():
    assert dc_Bounds.__init__(dc_Bounds('\x00\x00', '', '', ''), '', '', '', '') == None

def test_dc_Bounds_nonNegativeSize():
    assert dc_Bounds.nonNegativeSize(dc_Bounds('', '\x00', '\x00\x00', ''), '', 0) == None


from python_code import dc_Dimension

def test_dc_Dimension___init__():
    assert dc_Dimension.__init__(dc_Dimension('', '\x00'), '\x00\x00', '') == None

def test_dc_Dimension_nonNegativeDimension():
    assert dc_Dimension.nonNegativeDimension(dc_Dimension('', ''), '', '') == None


from python_code import dc_Point

def test_dc_Point___init__():
    assert dc_Point.__init__(dc_Point('', '\x00'), '\x00\x00', '') == None

