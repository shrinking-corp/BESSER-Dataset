from python_code import research20_Counted

def test_research20_Counted___init__():
    assert research20_Counted.__init__(research20_Counted(0), 0) == None


from python_code import research20_Labelled

def test_research20_Labelled___init__():
    assert research20_Labelled.__init__(research20_Labelled(''), '') == None


from python_code import research20_Named

def test_research20_Named___init__():
    assert research20_Named.__init__(research20_Named(''), '') == None


from python_code import research20_PublicationStatus
from python_code import research20_PublicationStructure

def test_research20_PublicationStatus___init__():
    assert research20_PublicationStatus.__init__(research20_PublicationStatus('', research20_PublicationStatus65=set(), research20_PublicationStatus67=set(), research20_PublicationStatus=research20_PublicationStructure()), '', research20_PublicationStatus65=set(), research20_PublicationStatus67=set(), research20_PublicationStatus=research20_PublicationStructure()) == None


from python_code import research20_StateMachineObject

def test_research20_StateMachineObject___init__():
    assert research20_StateMachineObject.__init__(research20_StateMachineObject(''), '') == None

