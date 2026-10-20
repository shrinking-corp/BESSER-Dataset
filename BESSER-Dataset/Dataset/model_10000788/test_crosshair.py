from python_code import JArray

def test_JArray___init__():
    assert JArray.__init__(JArray('', value4=set()), '', value4=set()) == None


from python_code import JBool

def test_JBool___init__():
    assert JBool.__init__(JBool(True), False) == None


from python_code import JMember
from python_code import JObject
from python_code import JValue_Interface

def test_JMember___init__():
    assert JMember.__init__(JMember('', JObject_JMember_11=JObject(), jValue2=JValue_Interface()), '', JObject_JMember_11=JObject(), jValue2=JValue_Interface()) == None


from python_code import JNull

def test_JNull___init__():
    assert JNull.__init__(JNull(''), '') == None


from python_code import JNum

def test_JNum___init__():
    assert JNum.__init__(JNum(0), 0) == None


from python_code import JStr

def test_JStr___init__():
    assert JStr.__init__(JStr(''), '') == None

