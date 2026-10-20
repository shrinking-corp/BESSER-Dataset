from python_code import architecture_DomainDeclaration
from python_code import architecture_Model

def test_architecture_DomainDeclaration___init__():
    assert architecture_DomainDeclaration.__init__(architecture_DomainDeclaration('', architecture_DomainDeclaration=architecture_Model(), architecture_DomainDeclaration2=set()), '', architecture_DomainDeclaration=architecture_Model(), architecture_DomainDeclaration2=set()) == None


from python_code import architecture_AbstractModel
from python_code import architecture_Import

def test_architecture_Import___init__():
    assert architecture_Import.__init__(architecture_Import('', architecture_Import=architecture_AbstractModel()), '', architecture_Import=architecture_AbstractModel()) == None

