from python_code import gyro_Bumpers

def test_gyro_Bumpers___init__():
    assert gyro_Bumpers.__init__(gyro_Bumpers(''), '') == None


from python_code import gyro_Distance

def test_gyro_Distance___init__():
    assert gyro_Distance.__init__(gyro_Distance(0, '\x00'), 0, '\x00') == None


from python_code import gyro_GyroSpecification

def test_gyro_GyroSpecification___init__():
    assert gyro_GyroSpecification.__init__(gyro_GyroSpecification('', gyro_GyroSpecification=set(), gyro_GyroSpecification2=set(), gyro_GyroSpecification4=set()), '', gyro_GyroSpecification=set(), gyro_GyroSpecification2=set(), gyro_GyroSpecification4=set()) == None


from python_code import gyro_LED

def test_gyro_LED___init__():
    assert gyro_LED.__init__(gyro_LED(''), '') == None


from python_code import gyro_Motor

def test_gyro_Motor___init__():
    assert gyro_Motor.__init__(gyro_Motor(0, 0), 0, 0) == None


from python_code import gyro_Servo

def test_gyro_Servo___init__():
    assert gyro_Servo.__init__(gyro_Servo(0, 0, 0), 0, 0, 0) == None


from python_code import gyro_StatusChange

def test_gyro_StatusChange___init__():
    assert gyro_StatusChange.__init__(gyro_StatusChange('', '', '\x00\x00'), '', '', '') == None


from python_code import gyro_Waiting

def test_gyro_Waiting___init__():
    assert gyro_Waiting.__init__(gyro_Waiting(0), 0) == None

