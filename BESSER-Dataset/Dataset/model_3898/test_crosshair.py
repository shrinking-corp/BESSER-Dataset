from python_code import behaviour_BinaryArithmeticFunction

def test_behaviour_BinaryArithmeticFunction___init__():
    assert behaviour_BinaryArithmeticFunction.__init__(behaviour_BinaryArithmeticFunction(''), '') == None


from python_code import behaviour_BooleanPrimitive

def test_behaviour_BooleanPrimitive___init__():
    assert behaviour_BooleanPrimitive.__init__(behaviour_BooleanPrimitive(''), '') == None


from python_code import behaviour_ComparisonBooleanFunction

def test_behaviour_ComparisonBooleanFunction___init__():
    assert behaviour_ComparisonBooleanFunction.__init__(behaviour_ComparisonBooleanFunction(''), '') == None


from python_code import behaviour_CoordinateLocationExpression

def test_behaviour_CoordinateLocationExpression___init__():
    assert behaviour_CoordinateLocationExpression.__init__(behaviour_CoordinateLocationExpression(0.0, 0.0), 0.0, 0.0) == None


from python_code import behaviour_EntityClass

def test_behaviour_EntityClass___init__():
    assert behaviour_EntityClass.__init__(behaviour_EntityClass('', behaviour_EntityClass=set(), behaviour_EntityClass13=set()), '', behaviour_EntityClass=set(), behaviour_EntityClass13=set()) == None


from python_code import behaviour_EntityPrimive

def test_behaviour_EntityPrimive___init__():
    assert behaviour_EntityPrimive.__init__(behaviour_EntityPrimive(''), '') == None


from python_code import behaviour_EntitySetPrimitive

def test_behaviour_EntitySetPrimitive___init__():
    assert behaviour_EntitySetPrimitive.__init__(behaviour_EntitySetPrimitive(''), '') == None


from python_code import behaviour_FloatConstantExpression

def test_behaviour_FloatConstantExpression___init__():
    assert behaviour_FloatConstantExpression.__init__(behaviour_FloatConstantExpression(0.0), 0.0) == None


from python_code import behaviour_IntConstantExpression

def test_behaviour_IntConstantExpression___init__():
    assert behaviour_IntConstantExpression.__init__(behaviour_IntConstantExpression(0), 0) == None


from python_code import behaviour_LocationPrimitive

def test_behaviour_LocationPrimitive___init__():
    assert behaviour_LocationPrimitive.__init__(behaviour_LocationPrimitive(''), '') == None


from python_code import behaviour_LocationSetPrimitive

def test_behaviour_LocationSetPrimitive___init__():
    assert behaviour_LocationSetPrimitive.__init__(behaviour_LocationSetPrimitive(''), '') == None


from python_code import behaviour_LogicBooleanFunction

def test_behaviour_LogicBooleanFunction___init__():
    assert behaviour_LogicBooleanFunction.__init__(behaviour_LogicBooleanFunction(''), '') == None


from python_code import behaviour_MonthDuration

def test_behaviour_MonthDuration___init__():
    assert behaviour_MonthDuration.__init__(behaviour_MonthDuration(''), '') == None


from python_code import behaviour_NameLocationExpression

def test_behaviour_NameLocationExpression___init__():
    assert behaviour_NameLocationExpression.__init__(behaviour_NameLocationExpression(''), '') == None


from python_code import behaviour_OccupationBooleanFunction

def test_behaviour_OccupationBooleanFunction___init__():
    assert behaviour_OccupationBooleanFunction.__init__(behaviour_OccupationBooleanFunction(''), '') == None


from python_code import behaviour_StringConstantExpression

def test_behaviour_StringConstantExpression___init__():
    assert behaviour_StringConstantExpression.__init__(behaviour_StringConstantExpression(''), '') == None


from python_code import behaviour_UnaryEntityFunction

def test_behaviour_UnaryEntityFunction___init__():
    assert behaviour_UnaryEntityFunction.__init__(behaviour_UnaryEntityFunction(''), '') == None


from python_code import behaviour_UnaryLocationFunction

def test_behaviour_UnaryLocationFunction___init__():
    assert behaviour_UnaryLocationFunction.__init__(behaviour_UnaryLocationFunction(''), '') == None


from python_code import behaviour_UnaryNumericFunction

def test_behaviour_UnaryNumericFunction___init__():
    assert behaviour_UnaryNumericFunction.__init__(behaviour_UnaryNumericFunction(''), '') == None


from python_code import behaviour_UnaryStringFunction

def test_behaviour_UnaryStringFunction___init__():
    assert behaviour_UnaryStringFunction.__init__(behaviour_UnaryStringFunction(''), '') == None

