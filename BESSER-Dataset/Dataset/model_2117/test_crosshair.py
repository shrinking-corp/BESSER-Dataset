from python_code import avm_CalculatedValue

def test_avm_CalculatedValue___init__():
    assert avm_CalculatedValue.__init__(avm_CalculatedValue('', '\x00'), '\x00\x00', '') == None


from python_code import avm_ComplexFormula

def test_avm_ComplexFormula___init__():
    assert avm_ComplexFormula.__init__(avm_ComplexFormula('', avm_ComplexFormula=set()), '', avm_ComplexFormula=set()) == None


from python_code import avm_ContainerInstanceBase

def test_avm_ContainerInstanceBase___init__():
    assert avm_ContainerInstanceBase.__init__(avm_ContainerInstanceBase('', '', '\x00\x00'), '', '', '') == None


from python_code import avm_DoDDistributionStatement

def test_avm_DoDDistributionStatement___init__():
    assert avm_DoDDistributionStatement.__init__(avm_DoDDistributionStatement(''), '') == None


from python_code import avm_DomainModelParameter

def test_avm_DomainModelParameter___init__():
    assert avm_DomainModelParameter.__init__(avm_DomainModelParameter('', '', '\x00\x00'), '', '', '') == None


from python_code import avm_ExecutionTask

def test_avm_ExecutionTask___init__():
    assert avm_ExecutionTask.__init__(avm_ExecutionTask('', '\x00'), '\x00\x00', '') == None


from python_code import avm_FixedValue
from python_code import avm_ParametricEnumeratedValue

def test_avm_FixedValue___init__():
    assert avm_FixedValue.__init__(avm_FixedValue('', '\x00', avm_FixedValue=avm_ParametricEnumeratedValue()), '\x00\x00', '', avm_FixedValue=avm_ParametricEnumeratedValue()) == None


from python_code import avm_InterpreterTask

def test_avm_InterpreterTask___init__():
    assert avm_InterpreterTask.__init__(avm_InterpreterTask('', '\x00'), '\x00\x00', '') == None


from python_code import avm_Proprietary

def test_avm_Proprietary___init__():
    assert avm_Proprietary.__init__(avm_Proprietary(''), '') == None


from python_code import avm_SecurityClassification

def test_avm_SecurityClassification___init__():
    assert avm_SecurityClassification.__init__(avm_SecurityClassification(''), '') == None


from python_code import avm_SimpleFormula

def test_avm_SimpleFormula___init__():
    assert avm_SimpleFormula.__init__(avm_SimpleFormula('', avm_SimpleFormula=set()), '', avm_SimpleFormula=set()) == None


from python_code import avm_adamsCar_FileReference

def test_avm_adamsCar_FileReference___init__():
    assert avm_adamsCar_FileReference.__init__(avm_adamsCar_FileReference('', '', '', avm_adamsCar_FileReference=set(), avm_adamsCar_FileReference248=set()), '', '', '', avm_adamsCar_FileReference=set(), avm_adamsCar_FileReference248=set()) == None


from python_code import adamsCar_avm_Value
from python_code import avm_adamsCar_Parameter

def test_avm_adamsCar_Parameter___init__():
    assert avm_adamsCar_Parameter.__init__(avm_adamsCar_Parameter('', '\x00', avm_adamsCar_Parameter=adamsCar_avm_Value()), '\x00\x00', '', avm_adamsCar_Parameter=adamsCar_avm_Value()) == None


from python_code import Geometry
from python_code import avm_cad_CustomGeometryInput

def test_avm_cad_CustomGeometryInput___init__():
    assert avm_cad_CustomGeometryInput.__init__(avm_cad_CustomGeometryInput('', avm_cad_CustomGeometryInput=Geometry()), '', avm_cad_CustomGeometryInput=Geometry()) == None


from python_code import avm_cad_Datum

def test_avm_cad_Datum___init__():
    assert avm_cad_Datum.__init__(avm_cad_Datum('', avm_cad_Datum=set()), '', avm_cad_Datum=set()) == None


from python_code import avm_cad_Geometry

def test_avm_cad_Geometry___init__():
    assert avm_cad_Geometry.__init__(avm_cad_Geometry('', '\x00'), '\x00\x00', '') == None


from python_code import avm_cad_Metric

def test_avm_cad_Metric___init__():
    assert avm_cad_Metric.__init__(avm_cad_Metric(''), '') == None


from python_code import avm_cad_Parameter
from python_code import cad_avm_Value

def test_avm_cad_Parameter___init__():
    assert avm_cad_Parameter.__init__(avm_cad_Parameter('', avm_cad_Parameter=cad_avm_Value()), '', avm_cad_Parameter=cad_avm_Value()) == None


from python_code import avm_cyber_CyberModel

def test_avm_cyber_CyberModel___init__():
    assert avm_cyber_CyberModel.__init__(avm_cyber_CyberModel('', '', '', avm_cyber_CyberModel=set(), avm_cyber_CyberModel238=set()), '', '', '', avm_cyber_CyberModel=set(), avm_cyber_CyberModel238=set()) == None


from python_code import avm_manufacturing_Metric

def test_avm_manufacturing_Metric___init__():
    assert avm_manufacturing_Metric.__init__(avm_manufacturing_Metric(''), '') == None


from python_code import avm_manufacturing_Parameter
from python_code import manufacturing_avm_Value

def test_avm_manufacturing_Parameter___init__():
    assert avm_manufacturing_Parameter.__init__(avm_manufacturing_Parameter('', '\x00', avm_manufacturing_Parameter=manufacturing_avm_Value()), '\x00\x00', '', avm_manufacturing_Parameter=manufacturing_avm_Value()) == None


from python_code import avm_modelica_Connector

def test_avm_modelica_Connector___init__():
    assert avm_modelica_Connector.__init__(avm_modelica_Connector('', '', avm_modelica_Connector=set(), avm_modelica_Connector149=set()), '', '', avm_modelica_Connector=set(), avm_modelica_Connector149=set()) == None


from python_code import avm_modelica_Limit
from python_code import modelica_avm_Value

def test_avm_modelica_Limit___init__():
    assert avm_modelica_Limit.__init__(avm_modelica_Limit('', '', '', '', '', avm_modelica_Limit=modelica_avm_Value()), '', '', '', '', '', avm_modelica_Limit=modelica_avm_Value()) == None


from python_code import avm_modelica_Metric

def test_avm_modelica_Metric___init__():
    assert avm_modelica_Metric.__init__(avm_modelica_Metric(''), '') == None


from python_code import avm_modelica_ModelicaModel

def test_avm_modelica_ModelicaModel___init__():
    assert avm_modelica_ModelicaModel.__init__(avm_modelica_ModelicaModel('\x00', avm_modelica_ModelicaModel145=set(), avm_modelica_ModelicaModel=set(), avm_modelica_ModelicaModel139=set(), avm_modelica_ModelicaModel141=set(), avm_modelica_ModelicaModel143=set()), '', avm_modelica_ModelicaModel145=set(), avm_modelica_ModelicaModel=set(), avm_modelica_ModelicaModel139=set(), avm_modelica_ModelicaModel141=set(), avm_modelica_ModelicaModel143=set()) == None


from python_code import avm_modelica_Parameter
from python_code import modelica_avm_Value

def test_avm_modelica_Parameter___init__():
    assert avm_modelica_Parameter.__init__(avm_modelica_Parameter('', avm_modelica_Parameter=modelica_avm_Value()), '', avm_modelica_Parameter=modelica_avm_Value()) == None


from python_code import avm_modelica_Redeclare
from python_code import modelica_avm_Value

def test_avm_modelica_Redeclare___init__():
    assert avm_modelica_Redeclare.__init__(avm_modelica_Redeclare('', '\x00', avm_modelica_Redeclare=modelica_avm_Value()), '\x00\x00', '', avm_modelica_Redeclare=modelica_avm_Value()) == None


from python_code import avm_modelica_SolverSettings

def test_avm_modelica_SolverSettings___init__():
    assert avm_modelica_SolverSettings.__init__(avm_modelica_SolverSettings('', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '\x00', '', '', '') == None

