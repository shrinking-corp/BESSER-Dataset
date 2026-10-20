from python_code import javaMetaModel_JAttribute

def test_javaMetaModel_JAttribute___init__():
    assert javaMetaModel_JAttribute.__init__(javaMetaModel_JAttribute(''), '') == None


from python_code import javaMetaModel_JElement

def test_javaMetaModel_JElement___init__():
    assert javaMetaModel_JElement.__init__(javaMetaModel_JElement(''), '') == None


from python_code import javaMetaModel_JMethod
from python_code import javaMetaModel_JParameter

def test_javaMetaModel_JParameter___init__():
    assert javaMetaModel_JParameter.__init__(javaMetaModel_JParameter('', JParameter=javaMetaModel_JMethod(), jparameter=javaMetaModel_JMethod()), '', JParameter=javaMetaModel_JMethod(), jparameter=javaMetaModel_JMethod()) == None


from python_code import javaMetaModel_JPrimitiveTypePar

def test_javaMetaModel_JPrimitiveTypePar___init__():
    assert javaMetaModel_JPrimitiveTypePar.__init__(javaMetaModel_JPrimitiveTypePar(''), '') == None


from python_code import javaMetaModel_JReference

def test_javaMetaModel_JReference___init__():
    assert javaMetaModel_JReference.__init__(javaMetaModel_JReference(''), '') == None


from python_code import javaMetaModel_JReferenceTypePar

def test_javaMetaModel_JReferenceTypePar___init__():
    assert javaMetaModel_JReferenceTypePar.__init__(javaMetaModel_JReferenceTypePar(''), '') == None

