from python_code import Feature
from python_code import FeatureModel
from python_code import spinefm_ActionModel_Action

def test_spinefm_ActionModel_Action___init__():
    assert spinefm_ActionModel_Action.__init__(spinefm_ActionModel_Action('', spinefm_ActionModel_Action=Feature(), spinefm_ActionModel_Action88=FeatureModel()), '', spinefm_ActionModel_Action=Feature(), spinefm_ActionModel_Action88=FeatureModel()) == None

def test_spinefm_ActionModel_Action_isSameObject():
    assert spinefm_ActionModel_Action.isSameObject(spinefm_ActionModel_Action('', spinefm_ActionModel_Action=Feature(), spinefm_ActionModel_Action88=FeatureModel()), 0) == None

def test_spinefm_ActionModel_Action_applyAction():
    assert spinefm_ActionModel_Action.applyAction(spinefm_ActionModel_Action('', spinefm_ActionModel_Action=Feature(), spinefm_ActionModel_Action88=FeatureModel()), 0, '\x00\x00') == None


from python_code import FeatureModel
from python_code import spinefm_ActionModel_ConfigurationState

def test_spinefm_ActionModel_ConfigurationState___init__():
    assert spinefm_ActionModel_ConfigurationState.__init__(spinefm_ActionModel_ConfigurationState('', spinefm_ActionModel_ConfigurationState=set(), spinefm_ActionModel_ConfigurationState75=set(), spinefm_ActionModel_ConfigurationState78=FeatureModel()), '', spinefm_ActionModel_ConfigurationState=set(), spinefm_ActionModel_ConfigurationState75=set(), spinefm_ActionModel_ConfigurationState78=FeatureModel()) == None

def test_spinefm_ActionModel_ConfigurationState_isIncludedIn():
    assert spinefm_ActionModel_ConfigurationState.isIncludedIn(spinefm_ActionModel_ConfigurationState('\x00', spinefm_ActionModel_ConfigurationState=set(), spinefm_ActionModel_ConfigurationState75=set(), spinefm_ActionModel_ConfigurationState78=FeatureModel()), '') == None


from python_code import RestrictionFunction
from python_code import spinefm_ActionModel_RestrictionFunction

def test_spinefm_ActionModel_RestrictionFunction___init__():
    assert spinefm_ActionModel_RestrictionFunction.__init__(spinefm_ActionModel_RestrictionFunction('', spinefm_ActionModel_RestrictionFunction=set(), spinefm_ActionModel_RestrictionFunction70=RestrictionFunction()), '', spinefm_ActionModel_RestrictionFunction=set(), spinefm_ActionModel_RestrictionFunction70=RestrictionFunction()) == None

def test_spinefm_ActionModel_RestrictionFunction_createAndAssociateInverseRestFunc():
    assert spinefm_ActionModel_RestrictionFunction.createAndAssociateInverseRestFunc(spinefm_ActionModel_RestrictionFunction('', spinefm_ActionModel_RestrictionFunction=set(), spinefm_ActionModel_RestrictionFunction70=RestrictionFunction())) == None


from python_code import Action
from python_code import ConfigurationState
from python_code import spinefm_ActionModel_Rule

def test_spinefm_ActionModel_Rule___init__():
    assert spinefm_ActionModel_Rule.__init__(spinefm_ActionModel_Rule('', spinefm_ActionModel_Rule=Action(), spinefm_ActionModel_Rule83=ConfigurationState()), '', spinefm_ActionModel_Rule=Action(), spinefm_ActionModel_Rule83=ConfigurationState()) == None

def test_spinefm_ActionModel_Rule_createInverseRule():
    assert spinefm_ActionModel_Rule.createInverseRule(spinefm_ActionModel_Rule('', spinefm_ActionModel_Rule=Action(), spinefm_ActionModel_Rule83=ConfigurationState())) == None


from python_code import ConfigurationProcessStep
from python_code import ConfigurationState
from python_code import spinefm_ConfigurationModel_Configuration

def test_spinefm_ConfigurationModel_Configuration___init__():
    assert spinefm_ConfigurationModel_Configuration.__init__(spinefm_ConfigurationModel_Configuration('\x00\x00', '', configuration=ConfigurationProcessStep(), spinefm_ConfigurationModel_Configuration=set(), spinefm_ConfigurationModel_Configuration32=ConfigurationState()), '', '', configuration=ConfigurationProcessStep(), spinefm_ConfigurationModel_Configuration=set(), spinefm_ConfigurationModel_Configuration32=ConfigurationState()) == None

def test_spinefm_ConfigurationModel_Configuration_getFeatureModel():
    assert spinefm_ConfigurationModel_Configuration.getFeatureModel(spinefm_ConfigurationModel_Configuration('', '\x00', configuration=ConfigurationProcessStep(), spinefm_ConfigurationModel_Configuration=set(), spinefm_ConfigurationModel_Configuration32=ConfigurationState())) == None

def test_spinefm_ConfigurationModel_Configuration_canBeLinked():
    assert spinefm_ConfigurationModel_Configuration.canBeLinked(spinefm_ConfigurationModel_Configuration('', '\x00', configuration=ConfigurationProcessStep(), spinefm_ConfigurationModel_Configuration=set(), spinefm_ConfigurationModel_Configuration32=ConfigurationState()), '') == None

def test_spinefm_ConfigurationModel_Configuration_isCompletlyLinked():
    assert spinefm_ConfigurationModel_Configuration.isCompletlyLinked(spinefm_ConfigurationModel_Configuration('', '\x00', configuration=ConfigurationProcessStep(), spinefm_ConfigurationModel_Configuration=set(), spinefm_ConfigurationModel_Configuration32=ConfigurationState())) == None

def test_spinefm_ConfigurationModel_Configuration_getLinkedConfigurationsOfDomainElement():
    assert spinefm_ConfigurationModel_Configuration.getLinkedConfigurationsOfDomainElement(spinefm_ConfigurationModel_Configuration('', '\x00', configuration=ConfigurationProcessStep(), spinefm_ConfigurationModel_Configuration=set(), spinefm_ConfigurationModel_Configuration32=ConfigurationState()), '') == None


from python_code import Configuration
from python_code import DEAssociation
from python_code import spinefm_ConfigurationModel_Link

def test_spinefm_ConfigurationModel_Link___init__():
    assert spinefm_ConfigurationModel_Link.__init__(spinefm_ConfigurationModel_Link('', spinefm_ConfigurationModel_Link=Configuration(), spinefm_ConfigurationModel_Link35=DEAssociation(), spinefm_ConfigurationModel_Link38=Configuration()), '', spinefm_ConfigurationModel_Link=Configuration(), spinefm_ConfigurationModel_Link35=DEAssociation(), spinefm_ConfigurationModel_Link38=Configuration()) == None

def test_spinefm_ConfigurationModel_Link_getAssociatedConfiguration():
    assert spinefm_ConfigurationModel_Link.getAssociatedConfiguration(spinefm_ConfigurationModel_Link('', spinefm_ConfigurationModel_Link=Configuration(), spinefm_ConfigurationModel_Link35=DEAssociation(), spinefm_ConfigurationModel_Link38=Configuration()), 0) == None


from python_code import spinefm_FMModel_Constraint

def test_spinefm_FMModel_Constraint___init__():
    assert spinefm_FMModel_Constraint.__init__(spinefm_FMModel_Constraint(''), '') == None


from python_code import spinefm_FMModel_Feature

def test_spinefm_FMModel_Feature___init__():
    assert spinefm_FMModel_Feature.__init__(spinefm_FMModel_Feature('\x00\x00', '', spinefm_FMModel_Feature=set()), '', '', spinefm_FMModel_Feature=set()) == None

def test_spinefm_FMModel_Feature_getAllChildrenFeatures():
    assert spinefm_FMModel_Feature.getAllChildrenFeatures(spinefm_FMModel_Feature('', '\x00', spinefm_FMModel_Feature=set())) == None


from python_code import Feature
from python_code import spinefm_FMModel_FeatureModel

def test_spinefm_FMModel_FeatureModel___init__():
    assert spinefm_FMModel_FeatureModel.__init__(spinefm_FMModel_FeatureModel('\x00\x00', '', spinefm_FMModel_FeatureModel=Feature(), spinefm_FMModel_FeatureModel2=set()), '', '', spinefm_FMModel_FeatureModel=Feature(), spinefm_FMModel_FeatureModel2=set()) == None

def test_spinefm_FMModel_FeatureModel_addFeature():
    assert spinefm_FMModel_FeatureModel.addFeature(spinefm_FMModel_FeatureModel('', '\x00', spinefm_FMModel_FeatureModel=Feature(), spinefm_FMModel_FeatureModel2=set()), '', '', '') == None

def test_spinefm_FMModel_FeatureModel_getStateFT():
    assert spinefm_FMModel_FeatureModel.getStateFT(spinefm_FMModel_FeatureModel('', '\x00', spinefm_FMModel_FeatureModel=Feature(), spinefm_FMModel_FeatureModel2=set()), '') == None

def test_spinefm_FMModel_FeatureModel_getFeatureFromName():
    assert spinefm_FMModel_FeatureModel.getFeatureFromName(spinefm_FMModel_FeatureModel('', '\x00', spinefm_FMModel_FeatureModel=Feature(), spinefm_FMModel_FeatureModel2=set()), '') == None


from python_code import spinefm_FMModel_Group

def test_spinefm_FMModel_Group___init__():
    assert spinefm_FMModel_Group.__init__(spinefm_FMModel_Group('', spinefm_FMModel_Group=set()), '', spinefm_FMModel_Group=set()) == None

def test_spinefm_FMModel_Group_getAllChildren():
    assert spinefm_FMModel_Group.getAllChildren(spinefm_FMModel_Group('', spinefm_FMModel_Group=set())) == None


from python_code import DEAssociation
from python_code import DEAssociationEnd
from python_code import spinefm_MSPLModel_DEAssociation

def test_spinefm_MSPLModel_DEAssociation___init__():
    assert spinefm_MSPLModel_DEAssociation.__init__(spinefm_MSPLModel_DEAssociation('', spinefm_MSPLModel_DEAssociation16=DEAssociation(), spinefm_MSPLModel_DEAssociation=set(), spinefm_MSPLModel_DEAssociation11=DEAssociationEnd(), spinefm_MSPLModel_DEAssociation13=DEAssociationEnd()), '', spinefm_MSPLModel_DEAssociation16=DEAssociation(), spinefm_MSPLModel_DEAssociation=set(), spinefm_MSPLModel_DEAssociation11=DEAssociationEnd(), spinefm_MSPLModel_DEAssociation13=DEAssociationEnd()) == None

def test_spinefm_MSPLModel_DEAssociation_createAndAssociateInverseAssociation():
    assert spinefm_MSPLModel_DEAssociation.createAndAssociateInverseAssociation(spinefm_MSPLModel_DEAssociation('', spinefm_MSPLModel_DEAssociation16=DEAssociation(), spinefm_MSPLModel_DEAssociation=set(), spinefm_MSPLModel_DEAssociation11=DEAssociationEnd(), spinefm_MSPLModel_DEAssociation13=DEAssociationEnd())) == None

def test_spinefm_MSPLModel_DEAssociation_computeActionsToDo():
    assert spinefm_MSPLModel_DEAssociation.computeActionsToDo(spinefm_MSPLModel_DEAssociation('', spinefm_MSPLModel_DEAssociation16=DEAssociation(), spinefm_MSPLModel_DEAssociation=set(), spinefm_MSPLModel_DEAssociation11=DEAssociationEnd(), spinefm_MSPLModel_DEAssociation13=DEAssociationEnd()), '\x00', '') == None


from python_code import DomainElement
from python_code import MultiplicityElement
from python_code import spinefm_MSPLModel_DEAssociationEnd

def test_spinefm_MSPLModel_DEAssociationEnd___init__():
    assert spinefm_MSPLModel_DEAssociationEnd.__init__(spinefm_MSPLModel_DEAssociationEnd('', spinefm_MSPLModel_DEAssociationEnd=MultiplicityElement(), spinefm_MSPLModel_DEAssociationEnd20=DomainElement()), '', spinefm_MSPLModel_DEAssociationEnd=MultiplicityElement(), spinefm_MSPLModel_DEAssociationEnd20=DomainElement()) == None


from python_code import FeatureModel
from python_code import MultiplicityElement
from python_code import spinefm_MSPLModel_DomainElement

def test_spinefm_MSPLModel_DomainElement___init__():
    assert spinefm_MSPLModel_DomainElement.__init__(spinefm_MSPLModel_DomainElement('', spinefm_MSPLModel_DomainElement=MultiplicityElement(), spinefm_MSPLModel_DomainElement25=FeatureModel(), spinefm_MSPLModel_DomainElement27=set()), '', spinefm_MSPLModel_DomainElement=MultiplicityElement(), spinefm_MSPLModel_DomainElement25=FeatureModel(), spinefm_MSPLModel_DomainElement27=set()) == None

def test_spinefm_MSPLModel_DomainElement_getSourcedAssociations():
    assert spinefm_MSPLModel_DomainElement.getSourcedAssociations(spinefm_MSPLModel_DomainElement('', spinefm_MSPLModel_DomainElement=MultiplicityElement(), spinefm_MSPLModel_DomainElement25=FeatureModel(), spinefm_MSPLModel_DomainElement27=set())) == None


from python_code import spinefm_MSPLModel_MultipleSoftwareProductLine

def test_spinefm_MSPLModel_MultipleSoftwareProductLine___init__():
    assert spinefm_MSPLModel_MultipleSoftwareProductLine.__init__(spinefm_MSPLModel_MultipleSoftwareProductLine(spinefm_MSPLModel_MultipleSoftwareProductLine=set(), spinefm_MSPLModel_MultipleSoftwareProductLine8=set()), spinefm_MSPLModel_MultipleSoftwareProductLine=set(), spinefm_MSPLModel_MultipleSoftwareProductLine8=set()) == None

def test_spinefm_MSPLModel_MultipleSoftwareProductLine_getDomainElementByName():
    assert spinefm_MSPLModel_MultipleSoftwareProductLine.getDomainElementByName(spinefm_MSPLModel_MultipleSoftwareProductLine(spinefm_MSPLModel_MultipleSoftwareProductLine=set(), spinefm_MSPLModel_MultipleSoftwareProductLine8=set()), 0) == None

def test_spinefm_MSPLModel_MultipleSoftwareProductLine_getValidAssociationsForSourceAndTarget():
    assert spinefm_MSPLModel_MultipleSoftwareProductLine.getValidAssociationsForSourceAndTarget(spinefm_MSPLModel_MultipleSoftwareProductLine(spinefm_MSPLModel_MultipleSoftwareProductLine=set(), spinefm_MSPLModel_MultipleSoftwareProductLine8=set()), '\x00', '') == None


from python_code import spinefm_MSPLModel_MultiplicityElement

def test_spinefm_MSPLModel_MultiplicityElement___init__():
    assert spinefm_MSPLModel_MultiplicityElement.__init__(spinefm_MSPLModel_MultiplicityElement(0, 0, '\x00\x00'), 0, 0, '') == None

def test_spinefm_MSPLModel_MultiplicityElement_respectBoundaries():
    assert spinefm_MSPLModel_MultiplicityElement.respectBoundaries(spinefm_MSPLModel_MultiplicityElement(0, 0, '\x00'), '') == None

def test_spinefm_MSPLModel_MultiplicityElement_isLowerThanUpperBound():
    assert spinefm_MSPLModel_MultiplicityElement.isLowerThanUpperBound(spinefm_MSPLModel_MultiplicityElement(0, 0, '\x00'), '') == None

def test_spinefm_MSPLModel_MultiplicityElement_isExactlyOne():
    assert spinefm_MSPLModel_MultiplicityElement.isExactlyOne(spinefm_MSPLModel_MultiplicityElement(0, 0, '\x00')) == None


from python_code import spinefm_ProcessModel_Context

def test_spinefm_ProcessModel_Context___init__():
    assert spinefm_ProcessModel_Context.__init__(spinefm_ProcessModel_Context('', spinefm_ProcessModel_Context=set()), '', spinefm_ProcessModel_Context=set()) == None

def test_spinefm_ProcessModel_Context_mergeExternalCPS():
    assert spinefm_ProcessModel_Context.mergeExternalCPS(spinefm_ProcessModel_Context('', spinefm_ProcessModel_Context=set()), '') == None

def test_spinefm_ProcessModel_Context_addCPS():
    assert spinefm_ProcessModel_Context.addCPS(spinefm_ProcessModel_Context('', spinefm_ProcessModel_Context=set()), '') == None

def test_spinefm_ProcessModel_Context_getCPSOfDE():
    assert spinefm_ProcessModel_Context.getCPSOfDE(spinefm_ProcessModel_Context('', spinefm_ProcessModel_Context=set()), '') == None


from python_code import Context
from python_code import spinefm_ProcessModel_DeletedContextInformations

def test_spinefm_ProcessModel_DeletedContextInformations___init__():
    assert spinefm_ProcessModel_DeletedContextInformations.__init__(spinefm_ProcessModel_DeletedContextInformations('', spinefm_ProcessModel_DeletedContextInformations=Context()), '\x00', spinefm_ProcessModel_DeletedContextInformations=Context()) == None

