from python_code import smallJava_BoolConstant

def test_smallJava_BoolConstant___init__():
    assert smallJava_BoolConstant.__init__(smallJava_BoolConstant(''), '') == None


from python_code import smallJava_SJExpression
from python_code import smallJava_SJMember
from python_code import smallJava_SJMemberSelection

def test_smallJava_SJMemberSelection___init__():
    assert smallJava_SJMemberSelection.__init__(smallJava_SJMemberSelection(False, smallJava_SJMemberSelection=smallJava_SJExpression(), smallJava_SJMemberSelection35=smallJava_SJMember(), smallJava_SJMemberSelection38=set()), False, smallJava_SJMemberSelection=smallJava_SJExpression(), smallJava_SJMemberSelection35=smallJava_SJMember(), smallJava_SJMemberSelection38=set()) == None


from python_code import smallJava_SJNamedElement

def test_smallJava_SJNamedElement___init__():
    assert smallJava_SJNamedElement.__init__(smallJava_SJNamedElement(''), '') == None

