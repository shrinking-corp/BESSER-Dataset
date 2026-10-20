from python_code import model_AssociationNode

def test_model_AssociationNode___init__():
    assert model_AssociationNode.__init__(model_AssociationNode(''), '') == None


from python_code import model_Diagram

def test_model_Diagram___init__():
    assert model_Diagram.__init__(model_Diagram('', model_Diagram=set(), model_Diagram2=set()), '', model_Diagram=set(), model_Diagram2=set()) == None


from python_code import model_TypeNode

def test_model_TypeNode___init__():
    assert model_TypeNode.__init__(model_TypeNode(''), '') == None

