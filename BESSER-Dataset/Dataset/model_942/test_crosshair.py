from python_code import esmodel_ClientVersionInfo

def test_esmodel_ClientVersionInfo___init__():
    assert esmodel_ClientVersionInfo.__init__(esmodel_ClientVersionInfo('', '\x00'), '\x00\x00', '') == None


from python_code import ProjectId
from python_code import esmodel_ProjectHistory

def test_esmodel_ProjectHistory___init__():
    assert esmodel_ProjectHistory.__init__(esmodel_ProjectHistory('\x00\x00', '', esmodel_ProjectHistory=ProjectId(), esmodel_ProjectHistory272=set()), '', '', esmodel_ProjectHistory=ProjectId(), esmodel_ProjectHistory272=set()) == None


from python_code import ProjectId
from python_code import esmodel_ProjectInfo
from python_code import versioning_PrimaryVersionSpec

def test_esmodel_ProjectInfo___init__():
    assert esmodel_ProjectInfo.__init__(esmodel_ProjectInfo('', '\x00', esmodel_ProjectInfo=ProjectId(), esmodel_ProjectInfo276=versioning_PrimaryVersionSpec()), '\x00\x00', '', esmodel_ProjectInfo=ProjectId(), esmodel_ProjectInfo276=versioning_PrimaryVersionSpec()) == None


from python_code import esmodel_VersionInfo

def test_esmodel_VersionInfo___init__():
    assert esmodel_VersionInfo.__init__(esmodel_VersionInfo(''), '') == None


from python_code import esmodel_accesscontrol_ACOrgUnit

def test_esmodel_accesscontrol_ACOrgUnit___init__():
    assert esmodel_accesscontrol_ACOrgUnit.__init__(esmodel_accesscontrol_ACOrgUnit('', '', esmodel_accesscontrol_ACOrgUnit=set(), esmodel_accesscontrol_ACOrgUnit441=set()), '', '', esmodel_accesscontrol_ACOrgUnit=set(), esmodel_accesscontrol_ACOrgUnit441=set()) == None

def test_esmodel_accesscontrol_ACOrgUnit_getId():
    assert esmodel_accesscontrol_ACOrgUnit.getId(esmodel_accesscontrol_ACOrgUnit('', '', esmodel_accesscontrol_ACOrgUnit=set(), esmodel_accesscontrol_ACOrgUnit441=set())) == None


from python_code import esmodel_accesscontrol_ACUser

def test_esmodel_accesscontrol_ACUser___init__():
    assert esmodel_accesscontrol_ACUser.__init__(esmodel_accesscontrol_ACUser('', '\x00'), '\x00\x00', '') == None


from python_code import ProjectId
from python_code import esmodel_accesscontrol_OrgUnitProperty

def test_esmodel_accesscontrol_OrgUnitProperty___init__():
    assert esmodel_accesscontrol_OrgUnitProperty.__init__(esmodel_accesscontrol_OrgUnitProperty('', '\x00', esmodel_accesscontrol_OrgUnitProperty=ProjectId()), '\x00\x00', '', esmodel_accesscontrol_OrgUnitProperty=ProjectId()) == None


from python_code import ModelElementId
from python_code import esmodel_events_DNDEvent

def test_esmodel_events_DNDEvent___init__():
    assert esmodel_events_DNDEvent.__init__(esmodel_events_DNDEvent('', '\x00', esmodel_events_DNDEvent=ModelElementId(), esmodel_events_DNDEvent397=ModelElementId()), '\x00\x00', '', esmodel_events_DNDEvent=ModelElementId(), esmodel_events_DNDEvent397=ModelElementId()) == None


import datetime as _ch_datetime
from python_code import esmodel_events_Event

def test_esmodel_events_Event___init__():
    assert esmodel_events_Event.__init__(esmodel_events_Event(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import esmodel_events_ExceptionEvent

def test_esmodel_events_ExceptionEvent___init__():
    assert esmodel_events_ExceptionEvent.__init__(esmodel_events_ExceptionEvent('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ModelElementId
from python_code import esmodel_events_LinkEvent

def test_esmodel_events_LinkEvent___init__():
    assert esmodel_events_LinkEvent.__init__(esmodel_events_LinkEvent('', False, esmodel_events_LinkEvent=ModelElementId(), esmodel_events_LinkEvent402=ModelElementId()), '', False, esmodel_events_LinkEvent=ModelElementId(), esmodel_events_LinkEvent402=ModelElementId()) == None


from python_code import ModelElementId
from python_code import esmodel_events_MergeChoiceEvent

def test_esmodel_events_MergeChoiceEvent___init__():
    assert esmodel_events_MergeChoiceEvent.__init__(esmodel_events_MergeChoiceEvent('', '', '', esmodel_events_MergeChoiceEvent=set(), esmodel_events_MergeChoiceEvent430=set(), esmodel_events_MergeChoiceEvent433=ModelElementId()), '', '', '', esmodel_events_MergeChoiceEvent=set(), esmodel_events_MergeChoiceEvent430=set(), esmodel_events_MergeChoiceEvent433=ModelElementId()) == None


from python_code import esmodel_events_MergeEvent
from python_code import versioning_PrimaryVersionSpec

def test_esmodel_events_MergeEvent___init__():
    assert esmodel_events_MergeEvent.__init__(esmodel_events_MergeEvent(0, 0, esmodel_events_MergeEvent=versioning_PrimaryVersionSpec(), esmodel_events_MergeEvent369=versioning_PrimaryVersionSpec(), esmodel_events_MergeEvent372=set()), 0, 0, esmodel_events_MergeEvent=versioning_PrimaryVersionSpec(), esmodel_events_MergeEvent369=versioning_PrimaryVersionSpec(), esmodel_events_MergeEvent372=set()) == None


from python_code import esmodel_events_MergeGlobalChoiceEvent

def test_esmodel_events_MergeGlobalChoiceEvent___init__():
    assert esmodel_events_MergeGlobalChoiceEvent.__init__(esmodel_events_MergeGlobalChoiceEvent(''), '') == None


from python_code import ModelElementId
from python_code import esmodel_events_NavigatorCreateEvent

def test_esmodel_events_NavigatorCreateEvent___init__():
    assert esmodel_events_NavigatorCreateEvent.__init__(esmodel_events_NavigatorCreateEvent(True, esmodel_events_NavigatorCreateEvent=ModelElementId(), esmodel_events_NavigatorCreateEvent412=ModelElementId()), False, esmodel_events_NavigatorCreateEvent=ModelElementId(), esmodel_events_NavigatorCreateEvent412=ModelElementId()) == None


from python_code import esmodel_events_NotificationIgnoreEvent

def test_esmodel_events_NotificationIgnoreEvent___init__():
    assert esmodel_events_NotificationIgnoreEvent.__init__(esmodel_events_NotificationIgnoreEvent(''), '') == None


from python_code import esmodel_events_NotificationReadEvent

def test_esmodel_events_NotificationReadEvent___init__():
    assert esmodel_events_NotificationReadEvent.__init__(esmodel_events_NotificationReadEvent(''), '') == None


import datetime as _ch_datetime
from python_code import esmodel_events_PluginFocusEvent

def test_esmodel_events_PluginFocusEvent___init__():
    assert esmodel_events_PluginFocusEvent.__init__(esmodel_events_PluginFocusEvent('', _ch_datetime.date(1, 1, 1)), '', _ch_datetime.date(1, 1, 2)) == None


from python_code import esmodel_events_PluginStartEvent

def test_esmodel_events_PluginStartEvent___init__():
    assert esmodel_events_PluginStartEvent.__init__(esmodel_events_PluginStartEvent(''), '') == None


from python_code import esmodel_events_PresentationSwitchEvent

def test_esmodel_events_PresentationSwitchEvent___init__():
    assert esmodel_events_PresentationSwitchEvent.__init__(esmodel_events_PresentationSwitchEvent('', '\x00'), '\x00\x00', '') == None


from python_code import ModelElementId
from python_code import esmodel_events_ReadEvent

def test_esmodel_events_ReadEvent___init__():
    assert esmodel_events_ReadEvent.__init__(esmodel_events_ReadEvent('', '\x00', esmodel_events_ReadEvent=ModelElementId()), '\x00\x00', '', esmodel_events_ReadEvent=ModelElementId()) == None


from python_code import esmodel_events_RevertEvent

def test_esmodel_events_RevertEvent___init__():
    assert esmodel_events_RevertEvent.__init__(esmodel_events_RevertEvent(0), 0) == None


from python_code import ModelElementId
from python_code import esmodel_events_TraceEvent

def test_esmodel_events_TraceEvent___init__():
    assert esmodel_events_TraceEvent.__init__(esmodel_events_TraceEvent('', esmodel_events_TraceEvent=ModelElementId(), esmodel_events_TraceEvent407=ModelElementId()), '', esmodel_events_TraceEvent=ModelElementId(), esmodel_events_TraceEvent407=ModelElementId()) == None


from python_code import ModelElementId
from python_code import esmodel_events_URLEvent

def test_esmodel_events_URLEvent___init__():
    assert esmodel_events_URLEvent.__init__(esmodel_events_URLEvent('', esmodel_events_URLEvent=ModelElementId(), esmodel_events_URLEvent426=ModelElementId()), '', esmodel_events_URLEvent=ModelElementId(), esmodel_events_URLEvent426=ModelElementId()) == None


import datetime as _ch_datetime
from python_code import ProjectId
from python_code import esmodel_notification_ESNotification

def test_esmodel_notification_ESNotification___init__():
    assert esmodel_notification_ESNotification.__init__(esmodel_notification_ESNotification('\x00', '', '', False, _ch_datetime.date(1, 1, 1), '', '', '', esmodel_notification_ESNotification=ProjectId(), esmodel_notification_ESNotification450=set(), esmodel_notification_ESNotification453=set()), '', '', '\x00', False, _ch_datetime.date(1, 1, 1), '', '', '', esmodel_notification_ESNotification=ProjectId(), esmodel_notification_ESNotification450=set(), esmodel_notification_ESNotification453=set()) == None


import datetime as _ch_datetime
from python_code import ModelElementId
from python_code import esmodel_operations_AbstractOperation

def test_esmodel_operations_AbstractOperation___init__():
    assert esmodel_operations_AbstractOperation.__init__(esmodel_operations_AbstractOperation('', '', False, _ch_datetime.date(1, 1, 2), esmodel_operations_AbstractOperation=ModelElementId()), '', '', False, _ch_datetime.date(1, 1, 1), esmodel_operations_AbstractOperation=ModelElementId()) == None


from python_code import esmodel_operations_AttributeOperation

def test_esmodel_operations_AttributeOperation___init__():
    assert esmodel_operations_AttributeOperation.__init__(esmodel_operations_AttributeOperation('', '\x00'), '\x00\x00', '') == None


from python_code import esmodel_operations_CompositeOperation
from python_code import operations_AbstractOperation

def test_esmodel_operations_CompositeOperation___init__():
    assert esmodel_operations_CompositeOperation.__init__(esmodel_operations_CompositeOperation('', '', False, esmodel_operations_CompositeOperation=set(), esmodel_operations_CompositeOperation334=operations_AbstractOperation()), '', '', True, esmodel_operations_CompositeOperation=set(), esmodel_operations_CompositeOperation334=operations_AbstractOperation()) == None


from python_code import esmodel_operations_CreateDeleteOperation
from python_code import operations_esmodel_EObject

def test_esmodel_operations_CreateDeleteOperation___init__():
    assert esmodel_operations_CreateDeleteOperation.__init__(esmodel_operations_CreateDeleteOperation(False, esmodel_operations_CreateDeleteOperation=operations_esmodel_EObject(), esmodel_operations_CreateDeleteOperation338=set(), esmodel_operations_CreateDeleteOperation340=set()), False, esmodel_operations_CreateDeleteOperation=operations_esmodel_EObject(), esmodel_operations_CreateDeleteOperation338=set(), esmodel_operations_CreateDeleteOperation340=set()) == None


from python_code import esmodel_operations_FeatureOperation

def test_esmodel_operations_FeatureOperation___init__():
    assert esmodel_operations_FeatureOperation.__init__(esmodel_operations_FeatureOperation(''), '') == None


from python_code import esmodel_operations_ModelElementGroup

def test_esmodel_operations_ModelElementGroup___init__():
    assert esmodel_operations_ModelElementGroup.__init__(esmodel_operations_ModelElementGroup('', esmodel_operations_ModelElementGroup=set()), '', esmodel_operations_ModelElementGroup=set()) == None


from python_code import esmodel_operations_MultiAttributeMoveOperation

def test_esmodel_operations_MultiAttributeMoveOperation___init__():
    assert esmodel_operations_MultiAttributeMoveOperation.__init__(esmodel_operations_MultiAttributeMoveOperation(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import esmodel_operations_MultiAttributeOperation

def test_esmodel_operations_MultiAttributeOperation___init__():
    assert esmodel_operations_MultiAttributeOperation.__init__(esmodel_operations_MultiAttributeOperation(False, 0, '\x00\x00'), False, 0, '') == None


from python_code import esmodel_operations_MultiAttributeSetOperation

def test_esmodel_operations_MultiAttributeSetOperation___init__():
    assert esmodel_operations_MultiAttributeSetOperation.__init__(esmodel_operations_MultiAttributeSetOperation(0, '', '\x00\x00'), 0, '', '') == None


from python_code import ModelElementId
from python_code import esmodel_operations_MultiReferenceMoveOperation

def test_esmodel_operations_MultiReferenceMoveOperation___init__():
    assert esmodel_operations_MultiReferenceMoveOperation.__init__(esmodel_operations_MultiReferenceMoveOperation(0, 0, esmodel_operations_MultiReferenceMoveOperation=ModelElementId()), 0, 0, esmodel_operations_MultiReferenceMoveOperation=ModelElementId()) == None


from python_code import esmodel_operations_MultiReferenceOperation

def test_esmodel_operations_MultiReferenceOperation___init__():
    assert esmodel_operations_MultiReferenceOperation.__init__(esmodel_operations_MultiReferenceOperation(False, 0, esmodel_operations_MultiReferenceOperation=set()), False, 0, esmodel_operations_MultiReferenceOperation=set()) == None


from python_code import ModelElementId
from python_code import esmodel_operations_MultiReferenceSetOperation

def test_esmodel_operations_MultiReferenceSetOperation___init__():
    assert esmodel_operations_MultiReferenceSetOperation.__init__(esmodel_operations_MultiReferenceSetOperation(0, esmodel_operations_MultiReferenceSetOperation349=ModelElementId(), esmodel_operations_MultiReferenceSetOperation=ModelElementId()), 0, esmodel_operations_MultiReferenceSetOperation349=ModelElementId(), esmodel_operations_MultiReferenceSetOperation=ModelElementId()) == None


from python_code import esmodel_operations_OperationGroup

def test_esmodel_operations_OperationGroup___init__():
    assert esmodel_operations_OperationGroup.__init__(esmodel_operations_OperationGroup('', esmodel_operations_OperationGroup=set()), '', esmodel_operations_OperationGroup=set()) == None


from python_code import esmodel_operations_ReferenceOperation

def test_esmodel_operations_ReferenceOperation___init__():
    assert esmodel_operations_ReferenceOperation.__init__(esmodel_operations_ReferenceOperation(False, '', '\x00\x00'), False, '', '') == None


from python_code import ModelElementId
from python_code import esmodel_url_ModelElementUrlFragment

def test_esmodel_url_ModelElementUrlFragment___init__():
    assert esmodel_url_ModelElementUrlFragment.__init__(esmodel_url_ModelElementUrlFragment('', esmodel_url_ModelElementUrlFragment=ModelElementId()), '', esmodel_url_ModelElementUrlFragment=ModelElementId()) == None


from python_code import ProjectId
from python_code import esmodel_url_ProjectUrlFragment

def test_esmodel_url_ProjectUrlFragment___init__():
    assert esmodel_url_ProjectUrlFragment.__init__(esmodel_url_ProjectUrlFragment('', esmodel_url_ProjectUrlFragment=ProjectId()), '', esmodel_url_ProjectUrlFragment=ProjectId()) == None


from python_code import esmodel_url_ServerUrl

def test_esmodel_url_ServerUrl___init__():
    assert esmodel_url_ServerUrl.__init__(esmodel_url_ServerUrl('', 0), '', 0) == None


import datetime as _ch_datetime
from python_code import esmodel_versioning_DateVersionSpec

def test_esmodel_versioning_DateVersionSpec___init__():
    assert esmodel_versioning_DateVersionSpec.__init__(esmodel_versioning_DateVersionSpec(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import esmodel_versioning_HistoryQuery
from python_code import versioning_PrimaryVersionSpec

def test_esmodel_versioning_HistoryQuery___init__():
    assert esmodel_versioning_HistoryQuery.__init__(esmodel_versioning_HistoryQuery(False, esmodel_versioning_HistoryQuery=versioning_PrimaryVersionSpec(), esmodel_versioning_HistoryQuery308=versioning_PrimaryVersionSpec(), esmodel_versioning_HistoryQuery311=set()), False, esmodel_versioning_HistoryQuery=versioning_PrimaryVersionSpec(), esmodel_versioning_HistoryQuery308=versioning_PrimaryVersionSpec(), esmodel_versioning_HistoryQuery311=set()) == None


import datetime as _ch_datetime
from python_code import esmodel_versioning_LogMessage

def test_esmodel_versioning_LogMessage___init__():
    assert esmodel_versioning_LogMessage.__init__(esmodel_versioning_LogMessage('', '\x00', _ch_datetime.date(1, 1, 3), _ch_datetime.date(1, 1, 1)), '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None


from python_code import esmodel_versioning_PrimaryVersionSpec

def test_esmodel_versioning_PrimaryVersionSpec___init__():
    assert esmodel_versioning_PrimaryVersionSpec.__init__(esmodel_versioning_PrimaryVersionSpec(0), 0) == None


from python_code import esmodel_versioning_TagVersionSpec

def test_esmodel_versioning_TagVersionSpec___init__():
    assert esmodel_versioning_TagVersionSpec.__init__(esmodel_versioning_TagVersionSpec(''), '') == None


from python_code import esmodel_versioning_VersionProperty

def test_esmodel_versioning_VersionProperty___init__():
    assert esmodel_versioning_VersionProperty.__init__(esmodel_versioning_VersionProperty('', '\x00'), '\x00\x00', '') == None


from python_code import metamodel_IdentifiableElement

def test_metamodel_IdentifiableElement___init__():
    assert metamodel_IdentifiableElement.__init__(metamodel_IdentifiableElement(''), '') == None


import datetime as _ch_datetime
from python_code import metamodel_ModelElement

def test_metamodel_ModelElement___init__():
    assert metamodel_ModelElement.__init__(metamodel_ModelElement('', _ch_datetime.date(1, 1, 1)), '', _ch_datetime.date(1, 1, 2)) == None


from python_code import metamodel_ModelVersion

def test_metamodel_ModelVersion___init__():
    assert metamodel_ModelVersion.__init__(metamodel_ModelVersion(0), 0) == None


from python_code import metamodel_UniqueIdentifier

def test_metamodel_UniqueIdentifier___init__():
    assert metamodel_UniqueIdentifier.__init__(metamodel_UniqueIdentifier(''), '') == None


from python_code import document_LeafSection
from python_code import metamodel_Project
from python_code import model_UnicaseModelElement

def test_model_UnicaseModelElement___init__():
    assert model_UnicaseModelElement.__init__(model_UnicaseModelElement('', '', '', annotatedModelElements=set(), referringModelElements=set(), modelElements=document_LeafSection(), referencedModelElements=set(), commentedElement=set(), modelElement=set(), ModelElement3=metamodel_Project(), ModelElement=metamodel_Project()), '', '', '', annotatedModelElements=set(), referringModelElements=set(), modelElements=document_LeafSection(), referencedModelElements=set(), commentedElement=set(), modelElement=set(), ModelElement3=metamodel_Project(), ModelElement=metamodel_Project()) == None

