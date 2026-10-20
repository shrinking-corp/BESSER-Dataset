from python_code import cSharpArchId_AbstractTypeDeclaration
from python_code import cSharpArchId_BodyDeclaration
from python_code import cSharpArchId_Modifier

def test_cSharpArchId_Modifier___init__():
    assert cSharpArchId_Modifier.__init__(cSharpArchId_Modifier('', '', False, cSharpArchId_Modifier=cSharpArchId_AbstractTypeDeclaration(), modifier=cSharpArchId_BodyDeclaration(), cSharpArchId_Modifier41=set()), '', '', True, cSharpArchId_Modifier=cSharpArchId_AbstractTypeDeclaration(), modifier=cSharpArchId_BodyDeclaration(), cSharpArchId_Modifier41=set()) == None


from python_code import cSharpArchId_PrimitiveType

def test_cSharpArchId_PrimitiveType___init__():
    assert cSharpArchId_PrimitiveType.__init__(cSharpArchId_PrimitiveType(''), '') == None


from python_code import cSharpArchId_ReturnType

def test_cSharpArchId_ReturnType___init__():
    assert cSharpArchId_ReturnType.__init__(cSharpArchId_ReturnType(''), '') == None

