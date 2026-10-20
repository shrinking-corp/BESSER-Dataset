from python_code import vM_CardinalityBased

def test_vM_CardinalityBased___init__():
    assert vM_CardinalityBased.__init__(vM_CardinalityBased('', '', False), '\x00', '', False) == None


from python_code import vM_ComplexExpression
from python_code import vM_Constraint
from python_code import vM_Constraints

def test_vM_Constraint___init__():
    assert vM_Constraint.__init__(vM_Constraint('', False, vM_Constraint=vM_Constraints(), vM_Constraint66=vM_ComplexExpression()), '', False, vM_Constraint=vM_Constraints(), vM_Constraint66=vM_ComplexExpression()) == None


from python_code import vM_ImportDeclaration

def test_vM_ImportDeclaration___init__():
    assert vM_ImportDeclaration.__init__(vM_ImportDeclaration(''), '') == None


from python_code import vM_IntegerAttrDefUnbounded

def test_vM_IntegerAttrDefUnbounded___init__():
    assert vM_IntegerAttrDefUnbounded.__init__(vM_IntegerAttrDefUnbounded(''), '') == None


from python_code import vM_EnumIntegerDef
from python_code import vM_IntegerAttrDef
from python_code import vM_IntegerDefaultDef

def test_vM_IntegerDefaultDef___init__():
    assert vM_IntegerDefaultDef.__init__(vM_IntegerDefaultDef(0, vM_IntegerDefaultDef=vM_IntegerAttrDef(), vM_IntegerDefaultDef48=vM_EnumIntegerDef()), 0, vM_IntegerDefaultDef=vM_IntegerAttrDef(), vM_IntegerDefaultDef48=vM_EnumIntegerDef()) == None


from python_code import vM_PackageDeclaration

def test_vM_PackageDeclaration___init__():
    assert vM_PackageDeclaration.__init__(vM_PackageDeclaration('', vM_PackageDeclaration=set()), '', vM_PackageDeclaration=set()) == None


from python_code import vM_RealAttrDefUnbounded

def test_vM_RealAttrDefUnbounded___init__():
    assert vM_RealAttrDefUnbounded.__init__(vM_RealAttrDefUnbounded(''), '') == None


from python_code import vM_EnumRealDef
from python_code import vM_RealAttrDef
from python_code import vM_RealDefaultDef

def test_vM_RealDefaultDef___init__():
    assert vM_RealDefaultDef.__init__(vM_RealDefaultDef('', vM_RealDefaultDef=vM_RealAttrDef(), vM_RealDefaultDef52=vM_EnumRealDef()), '', vM_RealDefaultDef=vM_RealAttrDef(), vM_RealDefaultDef52=vM_EnumRealDef()) == None


from python_code import vM_StringExpression

def test_vM_StringExpression___init__():
    assert vM_StringExpression.__init__(vM_StringExpression(''), '') == None

