from python_code import datatype_BooleanPropertyAttribute

def test_datatype_BooleanPropertyAttribute___init__():
    assert datatype_BooleanPropertyAttribute.__init__(datatype_BooleanPropertyAttribute('', False), '', False) == None


from python_code import datatype_Constraint
from python_code import datatype_ConstraintRule

def test_datatype_Constraint___init__():
    assert datatype_Constraint.__init__(datatype_Constraint('', '\x00', datatype_Constraint=datatype_ConstraintRule()), '\x00\x00', '', datatype_Constraint=datatype_ConstraintRule()) == None


from python_code import datatype_PrimitivePropertyType

def test_datatype_PrimitivePropertyType___init__():
    assert datatype_PrimitivePropertyType.__init__(datatype_PrimitivePropertyType(''), '') == None

