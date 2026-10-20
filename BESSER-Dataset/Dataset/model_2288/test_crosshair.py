from python_code import gradingsystem_ConcreteTask

def test_gradingsystem_ConcreteTask___init__():
    assert gradingsystem_ConcreteTask.__init__(gradingsystem_ConcreteTask(0), 0) == None


from python_code import gradingsystem_Course
from python_code import gradingsystem_GradingSystem

def test_gradingsystem_Course___init__():
    assert gradingsystem_Course.__init__(gradingsystem_Course('', gradingsystem_Course=gradingsystem_GradingSystem(), gradingsystem_Course2=set()), '', gradingsystem_Course=gradingsystem_GradingSystem(), gradingsystem_Course2=set()) == None


from python_code import gradingsystem_Grade
from python_code import gradingsystem_GradingScheme

def test_gradingsystem_Grade___init__():
    assert gradingsystem_Grade.__init__(gradingsystem_Grade('', 0, gradingsystem_Grade=gradingsystem_GradingScheme(), gradingsystem_Grade9=gradingsystem_GradingScheme()), '', 0, gradingsystem_Grade=gradingsystem_GradingScheme(), gradingsystem_Grade9=gradingsystem_GradingScheme()) == None

