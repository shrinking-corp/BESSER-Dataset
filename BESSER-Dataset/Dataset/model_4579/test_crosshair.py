from python_code import dsl_AppMetaData
from python_code import dsl_RunTimeModel

def test_dsl_AppMetaData___init__():
    assert dsl_AppMetaData.__init__(dsl_AppMetaData('', dsl_AppMetaData=dsl_RunTimeModel(), dsl_AppMetaData7=set()), '', dsl_AppMetaData=dsl_RunTimeModel(), dsl_AppMetaData7=set()) == None


from python_code import dsl_Boolean_Object

def test_dsl_Boolean_Object___init__():
    assert dsl_Boolean_Object.__init__(dsl_Boolean_Object(True), False) == None


from python_code import dsl_Number_Object

def test_dsl_Number_Object___init__():
    assert dsl_Number_Object.__init__(dsl_Number_Object(''), '') == None


from python_code import dsl_Action
from python_code import dsl_EnvironmentMetaData
from python_code import dsl_Resource
from python_code import dsl_Resource_Object
from python_code import dsl_Trigger

def test_dsl_Resource___init__():
    assert dsl_Resource.__init__(dsl_Resource('\x00', dsl_Resource18=dsl_Trigger(), dsl_Resource=set(), dsl_Resource37=dsl_EnvironmentMetaData(), dsl_Resource40=dsl_Action(), dsl_Resource110=dsl_Resource_Object()), '', dsl_Resource18=dsl_Trigger(), dsl_Resource=set(), dsl_Resource37=dsl_EnvironmentMetaData(), dsl_Resource40=dsl_Action(), dsl_Resource110=dsl_Resource_Object()) == None


from python_code import dsl_RunTimeModel
from python_code import dsl_ServiceMetaData

def test_dsl_ServiceMetaData___init__():
    assert dsl_ServiceMetaData.__init__(dsl_ServiceMetaData('', dsl_ServiceMetaData=dsl_RunTimeModel()), '', dsl_ServiceMetaData=dsl_RunTimeModel()) == None

