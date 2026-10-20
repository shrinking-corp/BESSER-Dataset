from python_code import model_Attachment

def test_model_Attachment___init__():
    assert model_Attachment.__init__(model_Attachment('', '', '\x00\x00'), '', '', '') == None


from python_code import model_BasicObject

def test_model_BasicObject___init__():
    assert model_BasicObject.__init__(model_BasicObject('', 0, '\x00\x00'), '', 0, '') == None

def test_model_BasicObject_toString():
    assert model_BasicObject.toString(model_BasicObject('', 0, '\x00')) == None


from python_code import model_Category

def test_model_Category___init__():
    assert model_Category.__init__(model_Category('', '\x00'), '\x00\x00', '') == None


from python_code import model_NotificationDefinition

def test_model_NotificationDefinition___init__():
    assert model_NotificationDefinition.__init__(model_NotificationDefinition('', '', False), '\x00', '', False) == None

def test_model_NotificationDefinition_toString():
    assert model_NotificationDefinition.toString(model_NotificationDefinition('', '', False)) == None

