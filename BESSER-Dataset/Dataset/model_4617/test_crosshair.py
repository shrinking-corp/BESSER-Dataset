from python_code import model_AbstractCardinalityConstraint

def test_model_AbstractCardinalityConstraint___init__():
    assert model_AbstractCardinalityConstraint.__init__(model_AbstractCardinalityConstraint('', '\x00'), '\x00\x00', '') == None


from python_code import model_AbstractRegExpConstraint

def test_model_AbstractRegExpConstraint___init__():
    assert model_AbstractRegExpConstraint.__init__(model_AbstractRegExpConstraint(''), '') == None


from python_code import model_AbstractRegExpTopicType

def test_model_AbstractRegExpTopicType___init__():
    assert model_AbstractRegExpTopicType.__init__(model_AbstractRegExpTopicType(''), '') == None


from python_code import model_AbstractUniqueValueTopicType

def test_model_AbstractUniqueValueTopicType___init__():
    assert model_AbstractUniqueValueTopicType.__init__(model_AbstractUniqueValueTopicType(True), False) == None


from python_code import model_OccurrenceType

def test_model_OccurrenceType___init__():
    assert model_OccurrenceType.__init__(model_OccurrenceType(''), '') == None


from python_code import model_OnoObject

def test_model_OnoObject___init__():
    assert model_OnoObject.__init__(model_OnoObject(0), 0) == None


from python_code import model_TMCLConstruct

def test_model_TMCLConstruct___init__():
    assert model_TMCLConstruct.__init__(model_TMCLConstruct('', '', '', model_TMCLConstruct=set()), '', '', '', model_TMCLConstruct=set()) == None

