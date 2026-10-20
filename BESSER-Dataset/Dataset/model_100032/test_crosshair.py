from python_code import publication102_Counted

def test_publication102_Counted___init__():
    assert publication102_Counted.__init__(publication102_Counted(0), 0) == None


from python_code import publication102_Labelled

def test_publication102_Labelled___init__():
    assert publication102_Labelled.__init__(publication102_Labelled(''), '') == None


from python_code import publication102_Named

def test_publication102_Named___init__():
    assert publication102_Named.__init__(publication102_Named(''), '') == None

