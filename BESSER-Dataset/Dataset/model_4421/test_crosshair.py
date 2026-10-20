from python_code import robo_Motor
from python_code import robo_Setup

def test_robo_Motor___init__():
    assert robo_Motor.__init__(robo_Motor('', '', 0.0, False, robo_Motor=robo_Setup(), robo_Motor7=robo_Setup()), '', '', 0.0, False, robo_Motor=robo_Setup(), robo_Motor7=robo_Setup()) == None


from python_code import robo_Program
from python_code import robo_Robot

def test_robo_Program___init__():
    assert robo_Program.__init__(robo_Program('', robo_Program11=set(), robo_Program=robo_Robot()), '', robo_Program11=set(), robo_Program=robo_Robot()) == None


from python_code import robo_Sensor
from python_code import robo_Setup

def test_robo_Sensor___init__():
    assert robo_Sensor.__init__(robo_Sensor('\x00\x00', '', '', '', robo_Sensor=robo_Setup()), '', '', '', '', robo_Sensor=robo_Setup()) == None


from python_code import robo_condition_Condition

def test_robo_condition_Condition___init__():
    assert robo_condition_Condition.__init__(robo_condition_Condition()) == None

def test_robo_condition_Condition_evaluate():
    assert robo_condition_Condition.evaluate(robo_condition_Condition()) == None


from python_code import robo_expression_Expr

def test_robo_expression_Expr___init__():
    assert robo_expression_Expr.__init__(robo_expression_Expr()) == None

def test_robo_expression_Expr_evaluate():
    assert robo_expression_Expr.evaluate(robo_expression_Expr()) == None

