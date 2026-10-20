from python_code import tp4_Counted

def test_tp4_Counted___init__():
    assert tp4_Counted.__init__(tp4_Counted(0), 0) == None


from python_code import tp4_Keyword
from python_code import tp4_Paper
from python_code import tp4_PublicationSystem

def test_tp4_Keyword___init__():
    assert tp4_Keyword.__init__(tp4_Keyword('', tp4_Keyword=tp4_Paper(), tp4_Keyword41=tp4_PublicationSystem()), '', tp4_Keyword=tp4_Paper(), tp4_Keyword41=tp4_PublicationSystem()) == None


from python_code import tp4_Labelled

def test_tp4_Labelled___init__():
    assert tp4_Labelled.__init__(tp4_Labelled(''), '') == None


from python_code import tp4_Named

def test_tp4_Named___init__():
    assert tp4_Named.__init__(tp4_Named(''), '') == None

