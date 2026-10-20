from python_code import metamodel_AssociationEntity
from python_code import metamodel_Entity
from python_code import metamodel_Relation

def test_metamodel_Relation___init__():
    assert metamodel_Relation.__init__(metamodel_Relation(False, False, Relation25=metamodel_AssociationEntity(), owns=metamodel_Entity(), ownedBy=metamodel_Entity(), relation=metamodel_AssociationEntity(), Relation=metamodel_Entity(), Relation6=metamodel_Entity()), False, False, Relation25=metamodel_AssociationEntity(), owns=metamodel_Entity(), ownedBy=metamodel_Entity(), relation=metamodel_AssociationEntity(), Relation=metamodel_Entity(), Relation6=metamodel_Entity()) == None


from python_code import metamodel_Entity
from python_code import metamodel_idFeature

def test_metamodel_idFeature___init__():
    assert metamodel_idFeature.__init__(metamodel_idFeature('', metamodel_idFeature=metamodel_Entity()), '', metamodel_idFeature=metamodel_Entity()) == None

