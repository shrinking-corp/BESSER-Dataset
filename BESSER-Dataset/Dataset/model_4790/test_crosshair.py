from python_code import types_JvmArrayType
from python_code import types_JvmComponentType

def test_types_JvmArrayType___init__():
    assert types_JvmArrayType.__init__(types_JvmArrayType(JvmArrayType=types_JvmComponentType(), arrayType=types_JvmComponentType()), JvmArrayType=types_JvmComponentType(), arrayType=types_JvmComponentType()) == None

def test_types_JvmArrayType_getDimensions():
    assert types_JvmArrayType.getDimensions(types_JvmArrayType(JvmArrayType=types_JvmComponentType(), arrayType=types_JvmComponentType())) == None


from python_code import types_JvmBooleanAnnotationValue

def test_types_JvmBooleanAnnotationValue___init__():
    assert types_JvmBooleanAnnotationValue.__init__(types_JvmBooleanAnnotationValue(True), False) == None


from python_code import types_JvmByteAnnotationValue

def test_types_JvmByteAnnotationValue___init__():
    assert types_JvmByteAnnotationValue.__init__(types_JvmByteAnnotationValue(''), '') == None


from python_code import types_JvmCharAnnotationValue

def test_types_JvmCharAnnotationValue___init__():
    assert types_JvmCharAnnotationValue.__init__(types_JvmCharAnnotationValue(''), '') == None


from python_code import types_JvmCustomAnnotationValue

def test_types_JvmCustomAnnotationValue___init__():
    assert types_JvmCustomAnnotationValue.__init__(types_JvmCustomAnnotationValue(''), '') == None


from python_code import types_JvmDoubleAnnotationValue

def test_types_JvmDoubleAnnotationValue___init__():
    assert types_JvmDoubleAnnotationValue.__init__(types_JvmDoubleAnnotationValue(0.0), 0.0) == None


from python_code import types_JvmEnumAnnotationValue
from python_code import types_JvmEnumerationLiteral
from python_code import types_JvmEnumerationType

def test_types_JvmEnumerationLiteral___init__():
    assert types_JvmEnumerationLiteral.__init__(types_JvmEnumerationLiteral(types_JvmEnumerationLiteral47=types_JvmEnumAnnotationValue(), types_JvmEnumerationLiteral=types_JvmEnumerationType()), types_JvmEnumerationLiteral47=types_JvmEnumAnnotationValue(), types_JvmEnumerationLiteral=types_JvmEnumerationType()) == None

def test_types_JvmEnumerationLiteral_getEnumType():
    assert types_JvmEnumerationLiteral.getEnumType(types_JvmEnumerationLiteral(types_JvmEnumerationLiteral47=types_JvmEnumAnnotationValue(), types_JvmEnumerationLiteral=types_JvmEnumerationType())) == None


from python_code import types_JvmFloatAnnotationValue

def test_types_JvmFloatAnnotationValue___init__():
    assert types_JvmFloatAnnotationValue.__init__(types_JvmFloatAnnotationValue(0.0), 0.0) == None


from python_code import types_JvmGenericType

def test_types_JvmGenericType___init__():
    assert types_JvmGenericType.__init__(types_JvmGenericType(True), False) == None

def test_types_JvmGenericType_isInstantiateable():
    assert types_JvmGenericType.isInstantiateable(types_JvmGenericType(False)) == None

def test_types_JvmGenericType_getExtendedClass():
    assert types_JvmGenericType.getExtendedClass(types_JvmGenericType(False)) == None

def test_types_JvmGenericType_getExtendedInterfaces():
    assert types_JvmGenericType.getExtendedInterfaces(types_JvmGenericType(False)) == None

def test_types_JvmGenericType_getDeclaredConstructors():
    assert types_JvmGenericType.getDeclaredConstructors(types_JvmGenericType(False)) == None


from python_code import types_JvmIdentifiableElement

def test_types_JvmIdentifiableElement___init__():
    assert types_JvmIdentifiableElement.__init__(types_JvmIdentifiableElement()) == None

def test_types_JvmIdentifiableElement_getSimpleName():
    assert types_JvmIdentifiableElement.getSimpleName(types_JvmIdentifiableElement()) == None

def test_types_JvmIdentifiableElement_getQualifiedName():
    assert types_JvmIdentifiableElement.getQualifiedName(types_JvmIdentifiableElement(), '') == None

def test_types_JvmIdentifiableElement_getIdentifier():
    assert types_JvmIdentifiableElement.getIdentifier(types_JvmIdentifiableElement()) == None


from python_code import types_JvmIntAnnotationValue

def test_types_JvmIntAnnotationValue___init__():
    assert types_JvmIntAnnotationValue.__init__(types_JvmIntAnnotationValue(0), 0) == None


from python_code import types_JvmLongAnnotationValue

def test_types_JvmLongAnnotationValue___init__():
    assert types_JvmLongAnnotationValue.__init__(types_JvmLongAnnotationValue(''), '') == None


from python_code import types_JvmPrimitiveType

def test_types_JvmPrimitiveType___init__():
    assert types_JvmPrimitiveType.__init__(types_JvmPrimitiveType(''), '') == None


from python_code import types_JvmShortAnnotationValue

def test_types_JvmShortAnnotationValue___init__():
    assert types_JvmShortAnnotationValue.__init__(types_JvmShortAnnotationValue(''), '') == None


from python_code import types_JvmStringAnnotationValue

def test_types_JvmStringAnnotationValue___init__():
    assert types_JvmStringAnnotationValue.__init__(types_JvmStringAnnotationValue(''), '') == None


from python_code import types_JvmTypeParameter
from python_code import types_JvmTypeParameterDeclarator

def test_types_JvmTypeParameter___init__():
    assert types_JvmTypeParameter.__init__(types_JvmTypeParameter('', typeParameters=types_JvmTypeParameterDeclarator(), JvmTypeParameter=types_JvmTypeParameterDeclarator()), '', typeParameters=types_JvmTypeParameterDeclarator(), JvmTypeParameter=types_JvmTypeParameterDeclarator()) == None


from python_code import types_JvmUnknownTypeReference

def test_types_JvmUnknownTypeReference___init__():
    assert types_JvmUnknownTypeReference.__init__(types_JvmUnknownTypeReference(''), '') == None

