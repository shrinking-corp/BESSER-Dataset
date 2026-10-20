from python_code import myDsl_LEFT

def test_myDsl_LEFT___init__():
    assert myDsl_LEFT.__init__(myDsl_LEFT(0), 0) == None


from python_code import myDsl_MOVE

def test_myDsl_MOVE___init__():
    assert myDsl_MOVE.__init__(myDsl_MOVE(0), 0) == None


from python_code import myDsl_PAPER

def test_myDsl_PAPER___init__():
    assert myDsl_PAPER.__init__(myDsl_PAPER(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import myDsl_PENCOLOUR

def test_myDsl_PENCOLOUR___init__():
    assert myDsl_PENCOLOUR.__init__(myDsl_PENCOLOUR(''), '') == None


from python_code import myDsl_PENSTATE

def test_myDsl_PENSTATE___init__():
    assert myDsl_PENSTATE.__init__(myDsl_PENSTATE(''), '') == None


from python_code import myDsl_RIGHT

def test_myDsl_RIGHT___init__():
    assert myDsl_RIGHT.__init__(myDsl_RIGHT(0), 0) == None


from python_code import myDsl_TURTLE

def test_myDsl_TURTLE___init__():
    assert myDsl_TURTLE.__init__(myDsl_TURTLE(0, 0), 0, 0) == None

