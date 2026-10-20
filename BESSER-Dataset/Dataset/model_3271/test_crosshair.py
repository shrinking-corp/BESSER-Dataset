from python_code import smDsl_Event
from python_code import smDsl_EventHandlingDescription
from python_code import smDsl_EventsSection

def test_smDsl_Event___init__():
    assert smDsl_Event.__init__(smDsl_Event('', smDsl_Event=smDsl_EventsSection(), smDsl_Event19=smDsl_EventHandlingDescription()), '', smDsl_Event=smDsl_EventsSection(), smDsl_Event19=smDsl_EventHandlingDescription()) == None


from python_code import smDsl_CommandsSection
from python_code import smDsl_EventsSection
from python_code import smDsl_Model

def test_smDsl_Model___init__():
    assert smDsl_Model.__init__(smDsl_Model('', smDsl_Model4=set(), smDsl_Model=smDsl_EventsSection(), smDsl_Model2=smDsl_CommandsSection()), '', smDsl_Model4=set(), smDsl_Model=smDsl_EventsSection(), smDsl_Model2=smDsl_CommandsSection()) == None

