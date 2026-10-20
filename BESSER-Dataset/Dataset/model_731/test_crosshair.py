from python_code import dc_Bounds

def test_dc_Bounds___init__():
    assert dc_Bounds.__init__(dc_Bounds('\x00\x00', '', '', ''), '', '', '', '') == None

def test_dc_Bounds_nonNegativeWidth():
    assert dc_Bounds.nonNegativeWidth(dc_Bounds('', '\x00', '\x00\x00', ''), '', 0) == None

def test_dc_Bounds_nonNegativeHeight():
    assert dc_Bounds.nonNegativeHeight(dc_Bounds('', '\x00', '\x00\x00', ''), '', 0) == None


from python_code import dc_Dimension

def test_dc_Dimension___init__():
    assert dc_Dimension.__init__(dc_Dimension('', '\x00'), '\x00\x00', '') == None

def test_dc_Dimension_nonNegativeWidth():
    assert dc_Dimension.nonNegativeWidth(dc_Dimension('', ''), '', '') == None

def test_dc_Dimension_nonNegativeHeight():
    assert dc_Dimension.nonNegativeHeight(dc_Dimension('', ''), '', '') == None


from python_code import dc_Point

def test_dc_Point___init__():
    assert dc_Point.__init__(dc_Point('', '\x00'), '\x00\x00', '') == None

