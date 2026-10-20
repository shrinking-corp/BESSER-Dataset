from python_code import research_Counted

def test_research_Counted___init__():
    assert research_Counted.__init__(research_Counted(0), 0) == None


from python_code import research_Labelled

def test_research_Labelled___init__():
    assert research_Labelled.__init__(research_Labelled(''), '') == None


from python_code import research_Named

def test_research_Named___init__():
    assert research_Named.__init__(research_Named(''), '') == None

