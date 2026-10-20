from python_code import AssistantMVC_Exam
from python_code import AssistantMVC_ExamItem

def test_AssistantMVC_ExamItem___init__():
    assert AssistantMVC_ExamItem.__init__(AssistantMVC_ExamItem('', AssistantMVC_ExamItem=AssistantMVC_Exam()), '', AssistantMVC_ExamItem=AssistantMVC_Exam()) == None


from python_code import AssistantMVC_MultipleChoice

def test_AssistantMVC_MultipleChoice___init__():
    assert AssistantMVC_MultipleChoice.__init__(AssistantMVC_MultipleChoice(0, '', False), 0, '', False) == None


from python_code import AssistantMVC_MultipleChoiceController

def test_AssistantMVC_MultipleChoiceController___init__():
    assert AssistantMVC_MultipleChoiceController.__init__(AssistantMVC_MultipleChoiceController(0, '\x00'), 0, '\x00') == None


from python_code import AssistantMVC_MultipleChoiceView

def test_AssistantMVC_MultipleChoiceView___init__():
    assert AssistantMVC_MultipleChoiceView.__init__(AssistantMVC_MultipleChoiceView(0, '\x00'), 0, '\x00') == None


from python_code import AssistantMVC_Controller
from python_code import AssistantMVC_Exam
from python_code import AssistantMVC_View

def test_AssistantMVC_View___init__():
    assert AssistantMVC_View.__init__(AssistantMVC_View('', '\x00', AssistantMVC_View=AssistantMVC_Exam(), AssistantMVC_View7=AssistantMVC_Controller()), '\x00\x00', '', AssistantMVC_View=AssistantMVC_Exam(), AssistantMVC_View7=AssistantMVC_Controller()) == None

