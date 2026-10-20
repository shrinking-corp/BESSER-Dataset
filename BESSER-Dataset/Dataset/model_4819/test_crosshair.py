from python_code import DiagramEntity
from python_code import FactoryModeloConsulta
from python_code import factoryrules_RulesFactory
from python_code import gestionmodelosconsultas_ModelFactory

def test_gestionmodelosconsultas_ModelFactory___init__():
    assert gestionmodelosconsultas_ModelFactory.__init__(gestionmodelosconsultas_ModelFactory(ModelFactory=factoryrules_RulesFactory(), ModelFactory2=FactoryModeloConsulta(), ModelFactory4=DiagramEntity()), ModelFactory=factoryrules_RulesFactory(), ModelFactory2=FactoryModeloConsulta(), ModelFactory4=DiagramEntity()) == None

def test_gestionmodelosconsultas_ModelFactory_salvar():
    assert gestionmodelosconsultas_ModelFactory.salvar(gestionmodelosconsultas_ModelFactory(ModelFactory=factoryrules_RulesFactory(), ModelFactory2=FactoryModeloConsulta(), ModelFactory4=DiagramEntity())) == None

def test_gestionmodelosconsultas_ModelFactory_cargar():
    assert gestionmodelosconsultas_ModelFactory.cargar(gestionmodelosconsultas_ModelFactory(ModelFactory=factoryrules_RulesFactory(), ModelFactory2=FactoryModeloConsulta(), ModelFactory4=DiagramEntity())) == None


from python_code import Entity
from python_code import gestionmodelosconsultas_entitymodel_Attribute

def test_gestionmodelosconsultas_entitymodel_Attribute___init__():
    assert gestionmodelosconsultas_entitymodel_Attribute.__init__(gestionmodelosconsultas_entitymodel_Attribute('', '', True, '', '', listAttributes=Entity(), valueAttribute=set(), visibleAttribute=set()), '', '', False, '', '', listAttributes=Entity(), valueAttribute=set(), visibleAttribute=set()) == None


from python_code import ModelElementEntity
from python_code import RealizacionDiagramEntity
from python_code import gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity

def test_gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity___init__():
    assert gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity.__init__(gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity('', '', ElementoRealizacionDiagramEntity44=ModelElementEntity(), listElementoRealizacionDiagramEntity=RealizacionDiagramEntity(), ElementoRealizacionDiagramEntity48=set()), '', '', ElementoRealizacionDiagramEntity44=ModelElementEntity(), listElementoRealizacionDiagramEntity=RealizacionDiagramEntity(), ElementoRealizacionDiagramEntity48=set()) == None


from python_code import ElementoRealizacionDiagramEntity
from python_code import gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute

def test_gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute___init__():
    assert gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute.__init__(gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute('', ElementoRealizacionValueAttribute51=set(), listElementoRealizacionAttribute=ElementoRealizacionDiagramEntity(), ElementoRealizacionValueAttribute56=set()), '', ElementoRealizacionValueAttribute51=set(), listElementoRealizacionAttribute=ElementoRealizacionDiagramEntity(), ElementoRealizacionValueAttribute56=set()) == None


from python_code import RealizacionDiagramEntity
from python_code import gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute

def test_gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute___init__():
    assert gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute.__init__(gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute('', realizacionVisibleAttribute=RealizacionDiagramEntity(), ElementoRealizacionVisibleAttribute61=set()), '', realizacionVisibleAttribute=RealizacionDiagramEntity(), ElementoRealizacionVisibleAttribute61=set()) == None


from python_code import DiagramEntity
from python_code import Entity
from python_code import ModelElementEntity
from python_code import RealizacionDiagramEntity
from python_code import gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity
from python_code import gestionmodelosconsultas_entitymodel_EntityRelation

def test_gestionmodelosconsultas_entitymodel_EntityRelation___init__():
    assert gestionmodelosconsultas_entitymodel_EntityRelation.__init__(gestionmodelosconsultas_entitymodel_EntityRelation('', '', '', '', listEntityRelation=DiagramEntity(), gestionmodelosconsultas_entitymodel_EntityRelation=Entity(), gestionmodelosconsultas_entitymodel_EntityRelation23=Entity(), ModelElementEntity=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity('', '', ElementoRealizacionDiagramEntity44=ModelElementEntity(), listElementoRealizacionDiagramEntity=RealizacionDiagramEntity(), ElementoRealizacionDiagramEntity48=set())), '', '', '', '', listEntityRelation=DiagramEntity(), gestionmodelosconsultas_entitymodel_EntityRelation=Entity(), gestionmodelosconsultas_entitymodel_EntityRelation23=Entity(), ModelElementEntity=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity('', '', ElementoRealizacionDiagramEntity44=ModelElementEntity(), listElementoRealizacionDiagramEntity=RealizacionDiagramEntity(), ElementoRealizacionDiagramEntity48=set())) == None


from python_code import gestionmodelosconsultas_entitymodel_ModelElementEntity

def test_gestionmodelosconsultas_entitymodel_ModelElementEntity___init__():
    assert gestionmodelosconsultas_entitymodel_ModelElementEntity.__init__(gestionmodelosconsultas_entitymodel_ModelElementEntity('\x00\x00', '', modelElementEntity=set()), '', '', modelElementEntity=set()) == None


from python_code import RealizacionDiagramEntity
from python_code import gestionmodelosconsultas_entitymodel_Value

def test_gestionmodelosconsultas_entitymodel_Value___init__():
    assert gestionmodelosconsultas_entitymodel_Value.__init__(gestionmodelosconsultas_entitymodel_Value('', values=set(), listValues=RealizacionDiagramEntity()), '', values=set(), listValues=RealizacionDiagramEntity()) == None


from python_code import factoryrules_Rule
from python_code import gestionmodelosconsultas_factoryrules_ChildRule

def test_gestionmodelosconsultas_factoryrules_ChildRule___init__():
    assert gestionmodelosconsultas_factoryrules_ChildRule.__init__(gestionmodelosconsultas_factoryrules_ChildRule('', listChildRule=factoryrules_Rule()), '', listChildRule=factoryrules_Rule()) == None


from python_code import factoryrules_RulesFactory
from python_code import gestionmodelosconsultas_factoryrules_Rule

def test_gestionmodelosconsultas_factoryrules_Rule___init__():
    assert gestionmodelosconsultas_factoryrules_Rule.__init__(gestionmodelosconsultas_factoryrules_Rule('', listRuleDiagramEntity=factoryrules_RulesFactory(), Rule12=set()), '', listRuleDiagramEntity=factoryrules_RulesFactory(), Rule12=set()) == None


from python_code import gestionmodelosconsultas_model_Campo
from python_code import model_ElementoConsulta

def test_gestionmodelosconsultas_model_Campo___init__():
    assert gestionmodelosconsultas_model_Campo.__init__(gestionmodelosconsultas_model_Campo('', '', False, listCampos=model_ElementoConsulta()), '\x00', '', False, listCampos=model_ElementoConsulta()) == None


from python_code import ModeloConsulta
from python_code import gestionmodelosconsultas_model_EADiagram

def test_gestionmodelosconsultas_model_EADiagram___init__():
    assert gestionmodelosconsultas_model_EADiagram.__init__(gestionmodelosconsultas_model_EADiagram('', EADiagram93=set(), EADiagram89=set(), listEADiagram=ModeloConsulta()), '', EADiagram93=set(), EADiagram89=set(), listEADiagram=ModeloConsulta()) == None


from python_code import gestionmodelosconsultas_model_ElementoConsulta
from python_code import model_EADiagram

def test_gestionmodelosconsultas_model_ElementoConsulta___init__():
    assert gestionmodelosconsultas_model_ElementoConsulta.__init__(gestionmodelosconsultas_model_ElementoConsulta('', listElementoConsulta=model_EADiagram(), ownedElementoConsulta=set()), '', listElementoConsulta=model_EADiagram(), ownedElementoConsulta=set()) == None


from python_code import gestionmodelosconsultas_model_ElementoModelo

def test_gestionmodelosconsultas_model_ElementoModelo___init__():
    assert gestionmodelosconsultas_model_ElementoModelo.__init__(gestionmodelosconsultas_model_ElementoModelo('', to=set(), from_=set()), '', to=set(), from_=set()) == None


from python_code import gestionmodelosconsultas_model_Relacion
from python_code import model_EADiagram
from python_code import model_ElementoConsulta

def test_gestionmodelosconsultas_model_Relacion___init__():
    assert gestionmodelosconsultas_model_Relacion.__init__(gestionmodelosconsultas_model_Relacion('', '\x00', listRelacion=model_EADiagram(), gestionmodelosconsultas_model_Relacion=model_ElementoConsulta(), gestionmodelosconsultas_model_Relacion85=model_ElementoConsulta()), '\x00\x00', '', listRelacion=model_EADiagram(), gestionmodelosconsultas_model_Relacion=model_ElementoConsulta(), gestionmodelosconsultas_model_Relacion85=model_ElementoConsulta()) == None


from python_code import FactoryModeloConsulta
from python_code import RealizacionDiagramEntity
from python_code import gestionmodelosconsultas_modeloconsultas_ModeloConsulta

def test_gestionmodelosconsultas_modeloconsultas_ModeloConsulta___init__():
    assert gestionmodelosconsultas_modeloconsultas_ModeloConsulta.__init__(gestionmodelosconsultas_modeloconsultas_ModeloConsulta('', ModeloConsulta68=RealizacionDiagramEntity(), listModeloConsulta=FactoryModeloConsulta(), ModeloConsulta73=set(), ModeloConsulta75=set()), '', ModeloConsulta68=RealizacionDiagramEntity(), listModeloConsulta=FactoryModeloConsulta(), ModeloConsulta73=set(), ModeloConsulta75=set()) == None


from python_code import gestionmodelosconsultas_resultcotracir_Consolidado

def test_gestionmodelosconsultas_resultcotracir_Consolidado___init__():
    assert gestionmodelosconsultas_resultcotracir_Consolidado.__init__(gestionmodelosconsultas_resultcotracir_Consolidado('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import gestionmodelosconsultas_resultcotracir_Detallado

def test_gestionmodelosconsultas_resultcotracir_Detallado___init__():
    assert gestionmodelosconsultas_resultcotracir_Detallado.__init__(gestionmodelosconsultas_resultcotracir_Detallado('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import gestionmodelosconsultas_resultcotracir_Planilla

def test_gestionmodelosconsultas_resultcotracir_Planilla___init__():
    assert gestionmodelosconsultas_resultcotracir_Planilla.__init__(gestionmodelosconsultas_resultcotracir_Planilla('', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', ''), '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import gestionmodelosconsultas_resultcotracir_Propietario

def test_gestionmodelosconsultas_resultcotracir_Propietario___init__():
    assert gestionmodelosconsultas_resultcotracir_Propietario.__init__(gestionmodelosconsultas_resultcotracir_Propietario('', '', '\x00\x00'), '', '', '') == None


from python_code import gestionmodelosconsultas_resultcotracir_Trama

def test_gestionmodelosconsultas_resultcotracir_Trama___init__():
    assert gestionmodelosconsultas_resultcotracir_Trama.__init__(gestionmodelosconsultas_resultcotracir_Trama('', '\x00'), '\x00\x00', '') == None


from python_code import gestionmodelosconsultas_resultcotracir_Transaccion

def test_gestionmodelosconsultas_resultcotracir_Transaccion___init__():
    assert gestionmodelosconsultas_resultcotracir_Transaccion.__init__(gestionmodelosconsultas_resultcotracir_Transaccion('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import gestionmodelosconsultas_resultset_ElementoModeloResultado
from python_code import resultset_ElementoModeloResultado

def test_gestionmodelosconsultas_resultset_ElementoModeloResultado___init__():
    assert gestionmodelosconsultas_resultset_ElementoModeloResultado.__init__(gestionmodelosconsultas_resultset_ElementoModeloResultado('', ElementoModeloResultado=set(), listElementoModeloResultado=resultset_ElementoModeloResultado()), '', ElementoModeloResultado=set(), listElementoModeloResultado=resultset_ElementoModeloResultado()) == None


from python_code import ModeloConsulta
from python_code import gestionmodelosconsultas_resultset_Resultado

def test_gestionmodelosconsultas_resultset_Resultado___init__():
    assert gestionmodelosconsultas_resultset_Resultado.__init__(gestionmodelosconsultas_resultset_Resultado('', listResultado=ModeloConsulta(), Resultado104=set()), '', listResultado=ModeloConsulta(), Resultado104=set()) == None

