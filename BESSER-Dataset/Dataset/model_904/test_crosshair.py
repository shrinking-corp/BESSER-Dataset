from python_code import spem_Default_TaskDefinitionParameter
from python_code import spem_TaskDefinition
from python_code import spem_WorkProductDefinition

def test_spem_Default_TaskDefinitionParameter___init__():
    assert spem_Default_TaskDefinitionParameter.__init__(spem_Default_TaskDefinitionParameter('', '\x00', spem_Default_TaskDefinitionParameter98=spem_WorkProductDefinition(), spem_Default_TaskDefinitionParameter=spem_TaskDefinition()), '\x00\x00', '', spem_Default_TaskDefinitionParameter98=spem_WorkProductDefinition(), spem_Default_TaskDefinitionParameter=spem_TaskDefinition()) == None


import datetime as _ch_datetime
from python_code import spem_Category
from python_code import spem_DescribableElement

def test_spem_DescribableElement___init__():
    assert spem_DescribableElement.__init__(spem_DescribableElement('', '', '', '', '', '', _ch_datetime.date(1, 1, 2), '', '', spem_DescribableElement=set(), spem_DescribableElement55=set(), categorizedElement=set(), DescribableElement=spem_Category()), '', '', '', '', '', '', _ch_datetime.date(1, 1, 1), '', '', spem_DescribableElement=set(), spem_DescribableElement55=set(), categorizedElement=set(), DescribableElement=spem_Category()) == None


from python_code import spem_MethodContentPackage
from python_code import spem_MethodContentPackageableElement

def test_spem_MethodContentPackageableElement___init__():
    assert spem_MethodContentPackageableElement.__init__(spem_MethodContentPackageableElement('', spem_MethodContentPackageableElement=spem_MethodContentPackage()), '', spem_MethodContentPackageableElement=spem_MethodContentPackage()) == None


from python_code import spem_MethodContentUse

def test_spem_MethodContentUse___init__():
    assert spem_MethodContentUse.__init__(spem_MethodContentUse(True), False) == None


from python_code import spem_MethodContentPackage
from python_code import spem_MethodLibrary

def test_spem_MethodLibrary___init__():
    assert spem_MethodLibrary.__init__(spem_MethodLibrary('', spem_MethodLibrary=set(), spem_MethodLibrary169=set(), spem_MethodLibrary172=spem_MethodContentPackage()), '', spem_MethodLibrary=set(), spem_MethodLibrary169=set(), spem_MethodLibrary172=spem_MethodContentPackage()) == None


from python_code import spem_MethodLibraryPackageableElement

def test_spem_MethodLibraryPackageableElement___init__():
    assert spem_MethodLibraryPackageableElement.__init__(spem_MethodLibraryPackageableElement(''), '') == None


from python_code import spem_ProcessPackage
from python_code import spem_ProcessPackageableElement

def test_spem_ProcessPackageableElement___init__():
    assert spem_ProcessPackageableElement.__init__(spem_ProcessPackageableElement('', spem_ProcessPackageableElement=spem_ProcessPackage()), '', spem_ProcessPackageableElement=spem_ProcessPackage()) == None


from python_code import spem_CompositeRole
from python_code import spem_Default_ResponsibilityAssignment
from python_code import spem_Default_TaskDefinitionPerformer
from python_code import spem_RoleDefinition
from python_code import spem_RoleUse

def test_spem_RoleDefinition___init__():
    assert spem_RoleDefinition.__init__(spem_RoleDefinition('', spem_RoleDefinition=spem_RoleUse(), spem_RoleDefinition80=set(), spem_RoleDefinition91=spem_Default_TaskDefinitionPerformer(), spem_RoleDefinition93=spem_Default_ResponsibilityAssignment(), spem_RoleDefinition118=spem_CompositeRole()), '', spem_RoleDefinition=spem_RoleUse(), spem_RoleDefinition80=set(), spem_RoleDefinition91=spem_Default_TaskDefinitionPerformer(), spem_RoleDefinition93=spem_Default_ResponsibilityAssignment(), spem_RoleDefinition118=spem_CompositeRole()) == None


from python_code import spem_WorkDefinition
from python_code import spem_WorkDefinitionPerformer

def test_spem_WorkDefinition___init__():
    assert spem_WorkDefinition.__init__(spem_WorkDefinition('\x00\x00', '', spem_WorkDefinition=spem_WorkDefinitionPerformer(), spem_WorkDefinition3=set()), '', '', spem_WorkDefinition=spem_WorkDefinitionPerformer(), spem_WorkDefinition3=set()) == None


from python_code import spem_ProcessComponent
from python_code import spem_ProcessComponentUse
from python_code import spem_WorkProductDefinition
from python_code import spem_WorkProductPort
from python_code import spem_WorkProductPortConnector

def test_spem_WorkProductPort___init__():
    assert spem_WorkProductPort.__init__(spem_WorkProductPort(False, '\x00', spem_WorkProductPort175=spem_WorkProductDefinition(), spem_WorkProductPort=spem_ProcessComponent(), spem_WorkProductPort136=spem_ProcessComponentUse(), spem_WorkProductPort178=spem_WorkProductPortConnector()), False, '\x00', spem_WorkProductPort175=spem_WorkProductDefinition(), spem_WorkProductPort=spem_ProcessComponent(), spem_WorkProductPort136=spem_ProcessComponentUse(), spem_WorkProductPort178=spem_WorkProductPortConnector()) == None


from python_code import spem_WorkProductUse
from python_code import spem_WorkProductUseRelationship

def test_spem_WorkProductUseRelationship___init__():
    assert spem_WorkProductUseRelationship.__init__(spem_WorkProductUseRelationship('', spem_WorkProductUseRelationship=spem_WorkProductUse(), spem_WorkProductUseRelationship45=set()), '', spem_WorkProductUseRelationship=spem_WorkProductUse(), spem_WorkProductUseRelationship45=set()) == None


from python_code import spem_uma_Deliverable

def test_spem_uma_Deliverable___init__():
    assert spem_uma_Deliverable.__init__(spem_uma_Deliverable('\x00\x00', '', spem_uma_Deliverable=set()), '', '', spem_uma_Deliverable=set()) == None


from python_code import spem_uma_DeliveryProcess
from python_code import spem_uma_Discipline
from python_code import spem_uma_ProcessPlanningTemplate

def test_spem_uma_DeliveryProcess___init__():
    assert spem_uma_DeliveryProcess.__init__(spem_uma_DeliveryProcess('', '', '\x00', '', '', '', spem_uma_DeliveryProcess186=set(), spem_uma_DeliveryProcess=set(), Process203=spem_uma_ProcessPlanningTemplate(), Process=spem_uma_Discipline()), '', '', '', '', '', '', spem_uma_DeliveryProcess186=set(), spem_uma_DeliveryProcess=set(), Process203=spem_uma_ProcessPlanningTemplate(), Process=spem_uma_Discipline()) == None


from python_code import spem_uma_Practice

def test_spem_uma_Practice___init__():
    assert spem_uma_Practice.__init__(spem_uma_Practice('', '', '', '', '', '', spem_uma_Practice=set(), spem_uma_Practice199=set(), spem_uma_Practice201=set()), '', '', '', '', '\x00', '', spem_uma_Practice=set(), spem_uma_Practice199=set(), spem_uma_Practice201=set()) == None


from python_code import spem_uma_Process

def test_spem_uma_Process___init__():
    assert spem_uma_Process.__init__(spem_uma_Process('', '', spem_uma_Process=set(), spem_uma_Process183=set()), '', '', spem_uma_Process=set(), spem_uma_Process183=set()) == None

