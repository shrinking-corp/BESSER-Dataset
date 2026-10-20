from python_code import AssistantMVC_ArrowShape

def test_AssistantMVC_ArrowShape___init__():
    assert AssistantMVC_ArrowShape.__init__(AssistantMVC_ArrowShape('', '\x00'), '\x00\x00', '') == None


from python_code import AssistantMVC_Exam

def test_AssistantMVC_Exam___init__():
    assert AssistantMVC_Exam.__init__(AssistantMVC_Exam('', AssistantMVC_Exam2=set(), AssistantMVC_Exam4=set(), AssistantMVC_Exam=set()), '', AssistantMVC_Exam2=set(), AssistantMVC_Exam4=set(), AssistantMVC_Exam=set()) == None

