from python_code import uml_Behavior

def test_uml_Behavior___init__():
    assert uml_Behavior.__init__(uml_Behavior(''), '') == None


from python_code import uml_Class

def test_uml_Class___init__():
    assert uml_Class.__init__(uml_Class(''), '') == None


from python_code import uml_Classifier

def test_uml_Classifier___init__():
    assert uml_Classifier.__init__(uml_Classifier(''), '') == None


from python_code import uml_JoinNode

def test_uml_JoinNode___init__():
    assert uml_JoinNode.__init__(uml_JoinNode(''), '') == None


from python_code import uml_NamedElement

def test_uml_NamedElement___init__():
    assert uml_NamedElement.__init__(uml_NamedElement(''), '') == None


from python_code import uml_ObjectFlow

def test_uml_ObjectFlow___init__():
    assert uml_ObjectFlow.__init__(uml_ObjectFlow('', '\x00'), '\x00\x00', '') == None


from python_code import uml_ObjectNode

def test_uml_ObjectNode___init__():
    assert uml_ObjectNode.__init__(uml_ObjectNode('', '\x00'), '\x00\x00', '') == None


from python_code import uml_OpaqueExpression

def test_uml_OpaqueExpression___init__():
    assert uml_OpaqueExpression.__init__(uml_OpaqueExpression(''), '') == None


from python_code import uml_RedefinableElement

def test_uml_RedefinableElement___init__():
    assert uml_RedefinableElement.__init__(uml_RedefinableElement(''), '') == None

