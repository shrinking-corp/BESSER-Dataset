from python_code import researchvc_Counted

def test_researchvc_Counted___init__():
    assert researchvc_Counted.__init__(researchvc_Counted(0), 0) == None


from python_code import researchvc_Labelled

def test_researchvc_Labelled___init__():
    assert researchvc_Labelled.__init__(researchvc_Labelled(''), '') == None


from python_code import researchvc_Named

def test_researchvc_Named___init__():
    assert researchvc_Named.__init__(researchvc_Named(''), '') == None


from python_code import researchvc_Paper
from python_code import researchvc_PublicationStructure
from python_code import researchvc_Researcher

def test_researchvc_Researcher___init__():
    assert researchvc_Researcher.__init__(researchvc_Researcher('', '', researchvc_Researcher=set(), researchvc_Researcher2=set(), authors=set(), Researcher=researchvc_Paper(), researchvc_Researcher22=researchvc_PublicationStructure(), researchvc_Researcher5=set()), '\x00', '', researchvc_Researcher=set(), researchvc_Researcher2=set(), authors=set(), Researcher=researchvc_Paper(), researchvc_Researcher22=researchvc_PublicationStructure(), researchvc_Researcher5=set()) == None

