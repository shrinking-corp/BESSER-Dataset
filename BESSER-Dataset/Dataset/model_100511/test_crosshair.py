import datetime as _ch_datetime
from python_code import requirements_AnnotableElement
from python_code import requirements_Annotation

def test_requirements_Annotation___init__():
    assert requirements_Annotation.__init__(requirements_Annotation('', '', _ch_datetime.date(1, 1, 1), '', '', '', requirements_Annotation=requirements_AnnotableElement()), '', '', _ch_datetime.date(1, 1, 1), '', '', '', requirements_Annotation=requirements_AnnotableElement()) == None


from python_code import requirements_Attribute
from python_code import requirements_Entity

def test_requirements_Attribute___init__():
    assert requirements_Attribute.__init__(requirements_Attribute('', requirements_Attribute=requirements_Entity()), '', requirements_Attribute=requirements_Entity()) == None


from python_code import requirements_Entity
from python_code import requirements_RelationShip

def test_requirements_RelationShip___init__():
    assert requirements_RelationShip.__init__(requirements_RelationShip(0, 0, 0, 0, requirements_RelationShip=requirements_Entity(), requirements_RelationShip7=requirements_Entity()), 0, 0, 0, 0, requirements_RelationShip=requirements_Entity(), requirements_RelationShip7=requirements_Entity()) == None


import datetime as _ch_datetime
from python_code import requirements_RequirementsDefinition

def test_requirements_RequirementsDefinition___init__():
    assert requirements_RequirementsDefinition.__init__(requirements_RequirementsDefinition('', _ch_datetime.date(1, 1, 1)), '', _ch_datetime.date(1, 1, 2)) == None

