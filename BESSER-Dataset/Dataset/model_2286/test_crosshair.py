from python_code import gsml_ConcreteTask

def test_gsml_ConcreteTask___init__():
    assert gsml_ConcreteTask.__init__(gsml_ConcreteTask(0.0), 0.0) == None


from python_code import gsml_Grade
from python_code import gsml_GradingScheme

def test_gsml_Grade___init__():
    assert gsml_Grade.__init__(gsml_Grade('\x00', 0.0, gsml_Grade=gsml_GradingScheme(), gsml_Grade14=gsml_GradingScheme()), '', 0.0, gsml_Grade=gsml_GradingScheme(), gsml_Grade14=gsml_GradingScheme()) == None

