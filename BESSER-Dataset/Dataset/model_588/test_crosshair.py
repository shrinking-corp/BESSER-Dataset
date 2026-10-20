from python_code import AssistantMVC_Exam
from python_code import AssistantMVC_ExamItem

def test_AssistantMVC_ExamItem___init__():
    assert AssistantMVC_ExamItem.__init__(AssistantMVC_ExamItem('', AssistantMVC_ExamItem=AssistantMVC_Exam()), '', AssistantMVC_ExamItem=AssistantMVC_Exam()) == None


from python_code import AssistantMVC_Exam
from python_code import AssistantMVC_ExamController
from python_code import AssistantMVC_ExamItemController
from python_code import AssistantMVC_View

def test_AssistantMVC_View___init__():
    assert AssistantMVC_View.__init__(AssistantMVC_View('', '\x00', AssistantMVC_View=AssistantMVC_Exam(), AssistantMVC_View7=AssistantMVC_ExamController(), AssistantMVC_View9=AssistantMVC_ExamItemController()), '\x00\x00', '', AssistantMVC_View=AssistantMVC_Exam(), AssistantMVC_View7=AssistantMVC_ExamController(), AssistantMVC_View9=AssistantMVC_ExamItemController()) == None

