from python_code import publication101_Counted

def test_publication101_Counted___init__():
    assert publication101_Counted.__init__(publication101_Counted(0), 0) == None


from python_code import publication101_Labelled

def test_publication101_Labelled___init__():
    assert publication101_Labelled.__init__(publication101_Labelled(''), '') == None


from python_code import publication101_Named

def test_publication101_Named___init__():
    assert publication101_Named.__init__(publication101_Named(''), '') == None

