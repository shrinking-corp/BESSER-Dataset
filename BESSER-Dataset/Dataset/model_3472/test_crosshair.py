from python_code import servicefeaturemodel_MandatoryServiceFeature

def test_servicefeaturemodel_MandatoryServiceFeature___init__():
    assert servicefeaturemodel_MandatoryServiceFeature.__init__(servicefeaturemodel_MandatoryServiceFeature(''), '') == None


from python_code import servicefeaturemodel_OR

def test_servicefeaturemodel_OR___init__():
    assert servicefeaturemodel_OR.__init__(servicefeaturemodel_OR(0, 0), 0, 0) == None


from python_code import servicefeaturemodel_GroupRelationship
from python_code import servicefeaturemodel_OptionalServiceFeature

def test_servicefeaturemodel_OptionalServiceFeature___init__():
    assert servicefeaturemodel_OptionalServiceFeature.__init__(servicefeaturemodel_OptionalServiceFeature('', servicefeaturemodel_OptionalServiceFeature=servicefeaturemodel_GroupRelationship()), '', servicefeaturemodel_OptionalServiceFeature=servicefeaturemodel_GroupRelationship()) == None

