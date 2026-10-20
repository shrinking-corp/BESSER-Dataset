from python_code import smallJava_SJBoolConstant

def test_smallJava_SJBoolConstant___init__():
    assert smallJava_SJBoolConstant.__init__(smallJava_SJBoolConstant(''), '') == None


from python_code import smallJava_SJIntConstant

def test_smallJava_SJIntConstant___init__():
    assert smallJava_SJIntConstant.__init__(smallJava_SJIntConstant(0), 0) == None


from python_code import smallJava_SJExpression
from python_code import smallJava_SJMember
from python_code import smallJava_SJMemberSelection

def test_smallJava_SJMemberSelection___init__():
    assert smallJava_SJMemberSelection.__init__(smallJava_SJMemberSelection(False, smallJava_SJMemberSelection=smallJava_SJExpression(), smallJava_SJMemberSelection35=smallJava_SJMember(), smallJava_SJMemberSelection38=set()), False, smallJava_SJMemberSelection=smallJava_SJExpression(), smallJava_SJMemberSelection35=smallJava_SJMember(), smallJava_SJMemberSelection38=set()) == None


from python_code import smallJava_SJNamedElement

def test_smallJava_SJNamedElement___init__():
    assert smallJava_SJNamedElement.__init__(smallJava_SJNamedElement(''), '') == None


from python_code import smallJava_SJStringConstant

def test_smallJava_SJStringConstant___init__():
    assert smallJava_SJStringConstant.__init__(smallJava_SJStringConstant(''), '') == None

