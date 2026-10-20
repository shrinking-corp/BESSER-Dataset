from python_code import crom_l1_composed_ComplexConstraint

def test_crom_l1_composed_ComplexConstraint___init__():
    assert crom_l1_composed_ComplexConstraint.__init__(crom_l1_composed_ComplexConstraint('', crom_l1_composed_ComplexConstraint=set()), '', crom_l1_composed_ComplexConstraint=set()) == None


from python_code import crom_l1_composed_NamedElement

def test_crom_l1_composed_NamedElement___init__():
    assert crom_l1_composed_NamedElement.__init__(crom_l1_composed_NamedElement(''), '') == None


from python_code import crom_l1_composed_Operation
from python_code import crom_l1_composed_Type

def test_crom_l1_composed_Operation___init__():
    assert crom_l1_composed_Operation.__init__(crom_l1_composed_Operation('', crom_l1_composed_Operation=set(), operations=crom_l1_composed_Type(), Operation=crom_l1_composed_Type()), '', crom_l1_composed_Operation=set(), operations=crom_l1_composed_Type(), Operation=crom_l1_composed_Type()) == None


from python_code import crom_l1_composed_AbstractRole
from python_code import crom_l1_composed_CompartmentType
from python_code import crom_l1_composed_Part

def test_crom_l1_composed_Part___init__():
    assert crom_l1_composed_Part.__init__(crom_l1_composed_Part(0, 0, parts=crom_l1_composed_CompartmentType(), crom_l1_composed_Part=crom_l1_composed_AbstractRole(), Part=crom_l1_composed_CompartmentType()), 0, 0, parts=crom_l1_composed_CompartmentType(), crom_l1_composed_Part=crom_l1_composed_AbstractRole(), Part=crom_l1_composed_CompartmentType()) == None


from python_code import crom_l1_composed_ParthoodConstraint

def test_crom_l1_composed_ParthoodConstraint___init__():
    assert crom_l1_composed_ParthoodConstraint.__init__(crom_l1_composed_ParthoodConstraint(''), '') == None


from python_code import crom_l1_composed_Model
from python_code import crom_l1_composed_Relation
from python_code import crom_l1_composed_RelationTarget

def test_crom_l1_composed_Relation___init__():
    assert crom_l1_composed_Relation.__init__(crom_l1_composed_Relation(crom_l1_composed_Relation=crom_l1_composed_Model(), crom_l1_composed_Relation78=crom_l1_composed_RelationTarget(), crom_l1_composed_Relation81=crom_l1_composed_RelationTarget()), crom_l1_composed_Relation=crom_l1_composed_Model(), crom_l1_composed_Relation78=crom_l1_composed_RelationTarget(), crom_l1_composed_Relation81=crom_l1_composed_RelationTarget()) == None

def test_crom_l1_composed_Relation_getTarget():
    assert crom_l1_composed_Relation.getTarget(crom_l1_composed_Relation(crom_l1_composed_Relation=crom_l1_composed_Model(), crom_l1_composed_Relation78=crom_l1_composed_RelationTarget(), crom_l1_composed_Relation81=crom_l1_composed_RelationTarget())) == None

def test_crom_l1_composed_Relation_getSource():
    assert crom_l1_composed_Relation.getSource(crom_l1_composed_Relation(crom_l1_composed_Relation=crom_l1_composed_Model(), crom_l1_composed_Relation78=crom_l1_composed_RelationTarget(), crom_l1_composed_Relation81=crom_l1_composed_RelationTarget())) == None


from python_code import crom_l1_composed_RoleGroup

def test_crom_l1_composed_RoleGroup___init__():
    assert crom_l1_composed_RoleGroup.__init__(crom_l1_composed_RoleGroup(0, 0, crom_l1_composed_RoleGroup=set()), 0, 0, crom_l1_composed_RoleGroup=set()) == None

