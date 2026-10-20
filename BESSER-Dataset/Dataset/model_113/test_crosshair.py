from python_code import java_AdditionalField
from python_code import java_Field

def test_java_AdditionalField___init__():
    assert java_AdditionalField.__init__(java_AdditionalField(java_AdditionalField=java_Field()), java_AdditionalField=java_Field()) == None

def test_java_AdditionalField_getArrayDimension():
    assert java_AdditionalField.getArrayDimension(java_AdditionalField(java_AdditionalField=java_Field())) == None


from python_code import java_AdditionalLocalVariable
from python_code import java_LocalVariable

def test_java_AdditionalLocalVariable___init__():
    assert java_AdditionalLocalVariable.__init__(java_AdditionalLocalVariable(java_AdditionalLocalVariable=java_LocalVariable()), java_AdditionalLocalVariable=java_LocalVariable()) == None

def test_java_AdditionalLocalVariable_getArrayDimension():
    assert java_AdditionalLocalVariable.getArrayDimension(java_AdditionalLocalVariable(java_AdditionalLocalVariable=java_LocalVariable())) == None


from python_code import java_Annotation

def test_java_Annotation___init__():
    assert java_Annotation.__init__(java_Annotation()) == None

def test_java_Annotation_getAllSuperClassifiers():
    assert java_Annotation.getAllSuperClassifiers(java_Annotation()) == None


from python_code import java_AnonymousClass
from python_code import java_EnumConstant
from python_code import java_NewConstructorCall

def test_java_AnonymousClass___init__():
    assert java_AnonymousClass.__init__(java_AnonymousClass(java_AnonymousClass114=java_EnumConstant(), java_AnonymousClass=java_NewConstructorCall()), java_AnonymousClass114=java_EnumConstant(), java_AnonymousClass=java_NewConstructorCall()) == None

def test_java_AnonymousClass_getAllMembers():
    assert java_AnonymousClass.getAllMembers(java_AnonymousClass(java_AnonymousClass114=java_EnumConstant(), java_AnonymousClass=java_NewConstructorCall()), '') == None

def test_java_AnonymousClass_getSuperClassifier():
    assert java_AnonymousClass.getSuperClassifier(java_AnonymousClass(java_AnonymousClass114=java_EnumConstant(), java_AnonymousClass=java_NewConstructorCall())) == None

def test_java_AnonymousClass_getAllSuperClassifiers():
    assert java_AnonymousClass.getAllSuperClassifiers(java_AnonymousClass(java_AnonymousClass114=java_EnumConstant(), java_AnonymousClass=java_NewConstructorCall())) == None


from python_code import java_Argumentable

def test_java_Argumentable___init__():
    assert java_Argumentable.__init__(java_Argumentable(java_Argumentable=set()), java_Argumentable=set()) == None

def test_java_Argumentable_getArgumentTypes():
    assert java_Argumentable.getArgumentTypes(java_Argumentable(java_Argumentable=set())) == None


from python_code import java_ArrayTypeable

def test_java_ArrayTypeable___init__():
    assert java_ArrayTypeable.__init__(java_ArrayTypeable(java_ArrayTypeable=set(), java_ArrayTypeable15=set()), java_ArrayTypeable=set(), java_ArrayTypeable15=set()) == None

def test_java_ArrayTypeable_getArrayDimension():
    assert java_ArrayTypeable.getArrayDimension(java_ArrayTypeable(java_ArrayTypeable=set(), java_ArrayTypeable15=set())) == None


from python_code import java_BooleanLiteral

def test_java_BooleanLiteral___init__():
    assert java_BooleanLiteral.__init__(java_BooleanLiteral(True), False) == None


from python_code import java_CharacterLiteral

def test_java_CharacterLiteral___init__():
    assert java_CharacterLiteral.__init__(java_CharacterLiteral(''), '') == None


from python_code import java_AnnotationInstance
from python_code import java_Classifier
from python_code import java_ClassifierReference

def test_java_Classifier___init__():
    assert java_Classifier.__init__(java_Classifier(java_Classifier=java_AnnotationInstance(), java_Classifier172=java_ClassifierReference()), java_Classifier=java_AnnotationInstance(), java_Classifier172=java_ClassifierReference()) == None

def test_java_Classifier_getAllSuperClassifiers():
    assert java_Classifier.getAllSuperClassifiers(java_Classifier(java_Classifier=java_AnnotationInstance(), java_Classifier172=java_ClassifierReference())) == None


from python_code import java_DecimalDoubleLiteral

def test_java_DecimalDoubleLiteral___init__():
    assert java_DecimalDoubleLiteral.__init__(java_DecimalDoubleLiteral(0.0), 0.0) == None


from python_code import java_DecimalFloatLiteral

def test_java_DecimalFloatLiteral___init__():
    assert java_DecimalFloatLiteral.__init__(java_DecimalFloatLiteral(0.0), 0.0) == None


from python_code import java_DecimalIntegerLiteral

def test_java_DecimalIntegerLiteral___init__():
    assert java_DecimalIntegerLiteral.__init__(java_DecimalIntegerLiteral(''), '') == None


from python_code import java_DecimalLongLiteral

def test_java_DecimalLongLiteral___init__():
    assert java_DecimalLongLiteral.__init__(java_DecimalLongLiteral(''), '') == None


from python_code import java_Enumeration

def test_java_Enumeration___init__():
    assert java_Enumeration.__init__(java_Enumeration(java_Enumeration=set()), java_Enumeration=set()) == None

def test_java_Enumeration_getContainedConstant():
    assert java_Enumeration.getContainedConstant(java_Enumeration(java_Enumeration=set()), 0) == None

def test_java_Enumeration_getAllSuperClassifiers():
    assert java_Enumeration.getAllSuperClassifiers(java_Enumeration(java_Enumeration=set())) == None


from python_code import java_HexDoubleLiteral

def test_java_HexDoubleLiteral___init__():
    assert java_HexDoubleLiteral.__init__(java_HexDoubleLiteral(0.0), 0.0) == None


from python_code import java_HexFloatLiteral

def test_java_HexFloatLiteral___init__():
    assert java_HexFloatLiteral.__init__(java_HexFloatLiteral(0.0), 0.0) == None


from python_code import java_HexIntegerLiteral

def test_java_HexIntegerLiteral___init__():
    assert java_HexIntegerLiteral.__init__(java_HexIntegerLiteral(''), '') == None


from python_code import java_HexLongLiteral

def test_java_HexLongLiteral___init__():
    assert java_HexLongLiteral.__init__(java_HexLongLiteral(''), '') == None


from python_code import java_ImportingElement

def test_java_ImportingElement___init__():
    assert java_ImportingElement.__init__(java_ImportingElement(java_ImportingElement=set()), java_ImportingElement=set()) == None

def test_java_ImportingElement_getDefaultImports():
    assert java_ImportingElement.getDefaultImports(java_ImportingElement(java_ImportingElement=set())) == None


from python_code import java_JavaRoot

def test_java_JavaRoot___init__():
    assert java_JavaRoot.__init__(java_JavaRoot()) == None

def test_java_JavaRoot_getClassifiersInSamePackage():
    assert java_JavaRoot.getClassifiersInSamePackage(java_JavaRoot()) == None

