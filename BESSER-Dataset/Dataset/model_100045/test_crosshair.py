from python_code import research16_Counted

def test_research16_Counted___init__():
    assert research16_Counted.__init__(research16_Counted(0), 0) == None


from python_code import research16_Labelled

def test_research16_Labelled___init__():
    assert research16_Labelled.__init__(research16_Labelled(''), '') == None


from python_code import research16_Named

def test_research16_Named___init__():
    assert research16_Named.__init__(research16_Named(''), '') == None


from python_code import research16_PublicationStatus
from python_code import research16_PublicationSystem

def test_research16_PublicationStatus___init__():
    assert research16_PublicationStatus.__init__(research16_PublicationStatus('', research16_PublicationStatus=research16_PublicationSystem(), research16_PublicationStatus65=set(), research16_PublicationStatus67=set()), '', research16_PublicationStatus=research16_PublicationSystem(), research16_PublicationStatus65=set(), research16_PublicationStatus67=set()) == None


from python_code import research16_StateMachineObject

def test_research16_StateMachineObject___init__():
    assert research16_StateMachineObject.__init__(research16_StateMachineObject(''), '') == None

