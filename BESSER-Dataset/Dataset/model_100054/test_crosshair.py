from python_code import researchva_Counted

def test_researchva_Counted___init__():
    assert researchva_Counted.__init__(researchva_Counted(0), 0) == None


from python_code import researchva_Keyword
from python_code import researchva_PublicationStructure

def test_researchva_Keyword___init__():
    assert researchva_Keyword.__init__(researchva_Keyword('', researchva_Keyword=researchva_PublicationStructure()), '', researchva_Keyword=researchva_PublicationStructure()) == None


from python_code import researchva_Labelled

def test_researchva_Labelled___init__():
    assert researchva_Labelled.__init__(researchva_Labelled(''), '') == None


from python_code import researchva_Named

def test_researchva_Named___init__():
    assert researchva_Named.__init__(researchva_Named(''), '') == None

