from python_code import research2_Counted

def test_research2_Counted___init__():
    assert research2_Counted.__init__(research2_Counted(0), 0) == None


from python_code import research2_Keyword
from python_code import research2_KnowledgeManager
from python_code import research2_Paper

def test_research2_Keyword___init__():
    assert research2_Keyword.__init__(research2_Keyword('', keywords=set(), research2_Keyword=research2_KnowledgeManager(), Keyword=research2_Paper()), '', keywords=set(), research2_Keyword=research2_KnowledgeManager(), Keyword=research2_Paper()) == None


from python_code import research2_Labelled

def test_research2_Labelled___init__():
    assert research2_Labelled.__init__(research2_Labelled(''), '') == None


from python_code import research2_Named

def test_research2_Named___init__():
    assert research2_Named.__init__(research2_Named(''), '') == None

