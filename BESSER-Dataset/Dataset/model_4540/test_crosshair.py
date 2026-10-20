from python_code import House2_Boiler

def test_House2_Boiler___init__():
    assert House2_Boiler.__init__(House2_Boiler(True), False) == None


from python_code import House2_BooleanAction

def test_House2_BooleanAction___init__():
    assert House2_BooleanAction.__init__(House2_BooleanAction(True), False) == None


from python_code import House2_EqualCondition

def test_House2_EqualCondition___init__():
    assert House2_EqualCondition.__init__(House2_EqualCondition(False, 0.0), False, 0.0) == None


from python_code import House2_GreaterThanCondition

def test_House2_GreaterThanCondition___init__():
    assert House2_GreaterThanCondition.__init__(House2_GreaterThanCondition(0.0), 0.0) == None


from python_code import House2_Lamp

def test_House2_Lamp___init__():
    assert House2_Lamp.__init__(House2_Lamp(True), False) == None


from python_code import House2_LessThanCondition

def test_House2_LessThanCondition___init__():
    assert House2_LessThanCondition.__init__(House2_LessThanCondition(0.0), 0.0) == None


from python_code import House2_NamedElement

def test_House2_NamedElement___init__():
    assert House2_NamedElement.__init__(House2_NamedElement(''), '') == None


from python_code import House2_RainSensor

def test_House2_RainSensor___init__():
    assert House2_RainSensor.__init__(House2_RainSensor(True), False) == None


from python_code import House2_RollerBlind

def test_House2_RollerBlind___init__():
    assert House2_RollerBlind.__init__(House2_RollerBlind(True), False) == None


from python_code import House2_TemperatureSensor

def test_House2_TemperatureSensor___init__():
    assert House2_TemperatureSensor.__init__(House2_TemperatureSensor(0.0), 0.0) == None


from python_code import House2_TwilightSwitch

def test_House2_TwilightSwitch___init__():
    assert House2_TwilightSwitch.__init__(House2_TwilightSwitch(True), False) == None


from python_code import House2_ValueAction

def test_House2_ValueAction___init__():
    assert House2_ValueAction.__init__(House2_ValueAction(0.0), 0.0) == None

