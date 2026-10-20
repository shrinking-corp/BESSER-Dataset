from python_code import diastyle_DEdgeStyle

def test_diastyle_DEdgeStyle___init__():
    assert diastyle_DEdgeStyle.__init__(diastyle_DEdgeStyle('', 0, '\x00\x00'), '', 0, '') == None


from python_code import diastyle_DNodeEdgeStyle

def test_diastyle_DNodeEdgeStyle___init__():
    assert diastyle_DNodeEdgeStyle.__init__(diastyle_DNodeEdgeStyle('', 0, '', '', 0, '', '\x00', ''), '', 0, '', '', 0, '', '', '') == None


from python_code import diastyle_DNodeStyle

def test_diastyle_DNodeStyle___init__():
    assert diastyle_DNodeStyle.__init__(diastyle_DNodeStyle('', '', '', 0, 0, '', 0), '', '\x00', '', 0, 0, '', 0) == None

