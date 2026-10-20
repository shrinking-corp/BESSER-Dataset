from python_code import decorators_TestEdgeDecorator1

def test_decorators_TestEdgeDecorator1___init__():
    assert decorators_TestEdgeDecorator1.__init__(decorators_TestEdgeDecorator1('', '', '\x00\x00'), '', '', '') == None


from python_code import decorators_STEMTime
from python_code import decorators_TestScenarioGraphDecorator1

def test_decorators_TestScenarioGraphDecorator1___init__():
    assert decorators_TestScenarioGraphDecorator1.__init__(decorators_TestScenarioGraphDecorator1(0.0, 0, '', False, decorators_TestScenarioGraphDecorator1=decorators_STEMTime()), 0.0, 0, '', False, decorators_TestScenarioGraphDecorator1=decorators_STEMTime()) == None

