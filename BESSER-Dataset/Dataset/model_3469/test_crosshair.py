from python_code import featuremodel_AttributeValueBoolean

def test_featuremodel_AttributeValueBoolean___init__():
    assert featuremodel_AttributeValueBoolean.__init__(featuremodel_AttributeValueBoolean(True), False) == None


from python_code import featuremodel_AttributeValueInt

def test_featuremodel_AttributeValueInt___init__():
    assert featuremodel_AttributeValueInt.__init__(featuremodel_AttributeValueInt(0), 0) == None


from python_code import featuremodel_AttributeValueString

def test_featuremodel_AttributeValueString___init__():
    assert featuremodel_AttributeValueString.__init__(featuremodel_AttributeValueString(''), '') == None


from python_code import featuremodel_Rule

def test_featuremodel_Rule___init__():
    assert featuremodel_Rule.__init__(featuremodel_Rule('', '\x00'), '\x00\x00', '') == None

