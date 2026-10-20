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
    assert dsl_Resource.__init__(dsl_Resource('\x00', dsl_Resource=set(), dsl_Resource16=dsl_Trigger(), dsl_Resource35=dsl_EnvironmentMetaData(), dsl_Resource38=dsl_Action(), dsl_Resource108=dsl_Resource_Object()), '', dsl_Resource=set(), dsl_Resource16=dsl_Trigger(), dsl_Resource35=dsl_EnvironmentMetaData(), dsl_Resource38=dsl_Action(), dsl_Resource108=dsl_Resource_Object()) == None

