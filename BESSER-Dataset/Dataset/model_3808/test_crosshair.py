from python_code import exercises_NamableElement

def test_exercises_NamableElement___init__():
    assert exercises_NamableElement.__init__(exercises_NamableElement(''), '') == None


from python_code import exercises_DFA
from python_code import exercises_State

def test_exercises_State___init__():
    assert exercises_State.__init__(exercises_State('', True, False, exercises_State=exercises_DFA(), exercises_State4=set(), exercises_State7=set()), '', False, False, exercises_State=exercises_DFA(), exercises_State4=set(), exercises_State7=set()) == None

