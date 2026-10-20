from python_code import AssistantMVC_Observable

def test_AssistantMVC_Observable___init__():
    assert AssistantMVC_Observable.__init__(AssistantMVC_Observable('', AssistantMVC_Observable=set()), '', AssistantMVC_Observable=set()) == None


from python_code import AssistantMVC_Controller
from python_code import AssistantMVC_Exam
from python_code import AssistantMVC_View

def test_AssistantMVC_View___init__():
    assert AssistantMVC_View.__init__(AssistantMVC_View('', '\x00', AssistantMVC_View=AssistantMVC_Exam(), AssistantMVC_View7=AssistantMVC_Controller()), '\x00\x00', '', AssistantMVC_View=AssistantMVC_Exam(), AssistantMVC_View7=AssistantMVC_Controller()) == None

