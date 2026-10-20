from python_code import modelDsl_AnnoTypes
from python_code import modelDsl_Annotation

def test_modelDsl_AnnoTypes___init__():
    assert modelDsl_AnnoTypes.__init__(modelDsl_AnnoTypes('', modelDsl_AnnoTypes=modelDsl_Annotation()), '', modelDsl_AnnoTypes=modelDsl_Annotation()) == None


from python_code import modelDsl_DoubleValue

def test_modelDsl_DoubleValue___init__():
    assert modelDsl_DoubleValue.__init__(modelDsl_DoubleValue(0.0), 0.0) == None


from python_code import modelDsl_Element
from python_code import modelDsl_Model
from python_code import modelDsl_Package

def test_modelDsl_Element___init__():
    assert modelDsl_Element.__init__(modelDsl_Element('', modelDsl_Element=modelDsl_Model(), modelDsl_Element8=modelDsl_Package()), '', modelDsl_Element=modelDsl_Model(), modelDsl_Element8=modelDsl_Package()) == None


from python_code import modelDsl_Entity
from python_code import modelDsl_EntityElements
from python_code import modelDsl_EntityGroup

def test_modelDsl_EntityGroup___init__():
    assert modelDsl_EntityGroup.__init__(modelDsl_EntityGroup('', modelDsl_EntityGroup=modelDsl_Entity(), modelDsl_EntityGroup21=modelDsl_EntityElements()), '', modelDsl_EntityGroup=modelDsl_Entity(), modelDsl_EntityGroup21=modelDsl_EntityElements()) == None


from python_code import modelDsl_Field

def test_modelDsl_Field___init__():
    assert modelDsl_Field.__init__(modelDsl_Field('', modelDsl_Field=set()), '', modelDsl_Field=set()) == None


from python_code import modelDsl_FormatRangeValue

def test_modelDsl_FormatRangeValue___init__():
    assert modelDsl_FormatRangeValue.__init__(modelDsl_FormatRangeValue('', '\x00'), '\x00\x00', '') == None


from python_code import modelDsl_Import
from python_code import modelDsl_Model

def test_modelDsl_Import___init__():
    assert modelDsl_Import.__init__(modelDsl_Import('', modelDsl_Import=modelDsl_Model()), '', modelDsl_Import=modelDsl_Model()) == None


from python_code import modelDsl_IntegerValue

def test_modelDsl_IntegerValue___init__():
    assert modelDsl_IntegerValue.__init__(modelDsl_IntegerValue(0), 0) == None


from python_code import modelDsl_EntityElements
from python_code import modelDsl_Property
from python_code import modelDsl_Type

def test_modelDsl_Property___init__():
    assert modelDsl_Property.__init__(modelDsl_Property(True, modelDsl_Property39=modelDsl_Type(), modelDsl_Property=modelDsl_EntityElements()), False, modelDsl_Property39=modelDsl_Type(), modelDsl_Property=modelDsl_EntityElements()) == None


from python_code import modelDsl_RangeValue

def test_modelDsl_RangeValue___init__():
    assert modelDsl_RangeValue.__init__(modelDsl_RangeValue(0, False, 0, False), 0, False, 0, True) == None


from python_code import modelDsl_Entity
from python_code import modelDsl_EntityElements
from python_code import modelDsl_Reference
from python_code import modelDsl_ReferenceList

def test_modelDsl_Reference___init__():
    assert modelDsl_Reference.__init__(modelDsl_Reference(True, modelDsl_Reference42=modelDsl_Entity(), modelDsl_Reference46=modelDsl_ReferenceList(), modelDsl_Reference=modelDsl_EntityElements()), False, modelDsl_Reference42=modelDsl_Entity(), modelDsl_Reference46=modelDsl_ReferenceList(), modelDsl_Reference=modelDsl_EntityElements()) == None


from python_code import modelDsl_StringValue

def test_modelDsl_StringValue___init__():
    assert modelDsl_StringValue.__init__(modelDsl_StringValue(''), '') == None

