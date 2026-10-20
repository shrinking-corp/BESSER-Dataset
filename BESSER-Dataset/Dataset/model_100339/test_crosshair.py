from python_code import ardurobotml_AcceleratetAction

def test_ardurobotml_AcceleratetAction___init__():
    assert ardurobotml_AcceleratetAction.__init__(ardurobotml_AcceleratetAction(0, 0), 0, 0) == None


from python_code import ardurobotml_DeceleratetAction

def test_ardurobotml_DeceleratetAction___init__():
    assert ardurobotml_DeceleratetAction.__init__(ardurobotml_DeceleratetAction(0, 0), 0, 0) == None


from python_code import ardurobotml_EmergencyStopAction

def test_ardurobotml_EmergencyStopAction___init__():
    assert ardurobotml_EmergencyStopAction.__init__(ardurobotml_EmergencyStopAction()) == None

def test_ardurobotml_EmergencyStopAction_begin():
    assert ardurobotml_EmergencyStopAction.begin(ardurobotml_EmergencyStopAction()) == None


from python_code import ardurobotml_MoveBackardAction

def test_ardurobotml_MoveBackardAction___init__():
    assert ardurobotml_MoveBackardAction.__init__(ardurobotml_MoveBackardAction(0, 0, 0), 0, 0, 0) == None


from python_code import ardurobotml_MoveBackardAndTurningLeftAction

def test_ardurobotml_MoveBackardAndTurningLeftAction___init__():
    assert ardurobotml_MoveBackardAndTurningLeftAction.__init__(ardurobotml_MoveBackardAndTurningLeftAction(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import ardurobotml_MoveBackardAndTurningRightAction

def test_ardurobotml_MoveBackardAndTurningRightAction___init__():
    assert ardurobotml_MoveBackardAndTurningRightAction.__init__(ardurobotml_MoveBackardAndTurningRightAction(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import ardurobotml_MoveForwardAction

def test_ardurobotml_MoveForwardAction___init__():
    assert ardurobotml_MoveForwardAction.__init__(ardurobotml_MoveForwardAction(0, 0, 0), 0, 0, 0) == None


from python_code import ardurobotml_MoveForwardAndTurningLeftAction

def test_ardurobotml_MoveForwardAndTurningLeftAction___init__():
    assert ardurobotml_MoveForwardAndTurningLeftAction.__init__(ardurobotml_MoveForwardAndTurningLeftAction(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import ardurobotml_MoveForwardAndTurningRightAction

def test_ardurobotml_MoveForwardAndTurningRightAction___init__():
    assert ardurobotml_MoveForwardAndTurningRightAction.__init__(ardurobotml_MoveForwardAndTurningRightAction(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import ardurobotml_NamedElement

def test_ardurobotml_NamedElement___init__():
    assert ardurobotml_NamedElement.__init__(ardurobotml_NamedElement(''), '') == None


from python_code import ardurobotml_SystemPropertyCondition

def test_ardurobotml_SystemPropertyCondition___init__():
    assert ardurobotml_SystemPropertyCondition.__init__(ardurobotml_SystemPropertyCondition(True), False) == None


from python_code import ardurobotml_TurningLeftAction

def test_ardurobotml_TurningLeftAction___init__():
    assert ardurobotml_TurningLeftAction.__init__(ardurobotml_TurningLeftAction(0, 0, 0), 0, 0, 0) == None


from python_code import ardurobotml_TurningRightAction

def test_ardurobotml_TurningRightAction___init__():
    assert ardurobotml_TurningRightAction.__init__(ardurobotml_TurningRightAction(0, 0, 0), 0, 0, 0) == None

