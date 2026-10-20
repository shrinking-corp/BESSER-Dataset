from python_code import newP_Requires
from python_code import newP_Term

def test_newP_Requires___init__():
    assert newP_Requires.__init__(newP_Requires('', newP_Requires=newP_Term()), '', newP_Requires=newP_Term()) == None


from python_code import newP_RequirementTerm
from python_code import newP_SimpleDependency

def test_newP_SimpleDependency___init__():
    assert newP_SimpleDependency.__init__(newP_SimpleDependency('', newP_SimpleDependency=newP_RequirementTerm()), '', newP_SimpleDependency=newP_RequirementTerm()) == None


from python_code import newP_Specification

def test_newP_Specification___init__():
    assert newP_Specification.__init__(newP_Specification('', newP_Specification=set(), newP_Specification11=set()), '', newP_Specification=set(), newP_Specification11=set()) == None


from python_code import newP_TextDescription

def test_newP_TextDescription___init__():
    assert newP_TextDescription.__init__(newP_TextDescription(''), '') == None


from python_code import newP_Term
from python_code import newP_UnaryOperator

def test_newP_UnaryOperator___init__():
    assert newP_UnaryOperator.__init__(newP_UnaryOperator('', newP_UnaryOperator=newP_Term()), '', newP_UnaryOperator=newP_Term()) == None

