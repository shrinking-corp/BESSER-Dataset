from python_code import research31_Counted

def test_research31_Counted___init__():
    assert research31_Counted.__init__(research31_Counted(0), 0) == None


from python_code import research31_Labelled

def test_research31_Labelled___init__():
    assert research31_Labelled.__init__(research31_Labelled(''), '') == None


from python_code import research31_Named

def test_research31_Named___init__():
    assert research31_Named.__init__(research31_Named(''), '') == None


from python_code import research31_PublicationStatus
from python_code import research31_PublicationStructure

def test_research31_PublicationStatus___init__():
    assert research31_PublicationStatus.__init__(research31_PublicationStatus('', research31_PublicationStatus=research31_PublicationStructure(), research31_PublicationStatus65=set(), research31_PublicationStatus67=set()), '', research31_PublicationStatus=research31_PublicationStructure(), research31_PublicationStatus65=set(), research31_PublicationStatus67=set()) == None


from python_code import research31_StateMachineObject

def test_research31_StateMachineObject___init__():
    assert research31_StateMachineObject.__init__(research31_StateMachineObject(''), '') == None

