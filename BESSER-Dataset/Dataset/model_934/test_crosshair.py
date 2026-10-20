from python_code import uma_Activity

def test_uma_Activity___init__():
    assert uma_Activity.__init__(uma_Activity('', '', '', '', '\x00', '', '', uma_Activity=set()), '', '', '', '', '', '', '', uma_Activity=set()) == None


from python_code import uma_ActivityDescription

def test_uma_ActivityDescription___init__():
    assert uma_ActivityDescription.__init__(uma_ActivityDescription('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_ApplicableMetaClassInfo

def test_uma_ApplicableMetaClassInfo___init__():
    assert uma_ApplicableMetaClassInfo.__init__(uma_ApplicableMetaClassInfo(''), '') == None


from python_code import uma_ArtifactDescription

def test_uma_ArtifactDescription___init__():
    assert uma_ArtifactDescription.__init__(uma_ArtifactDescription('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import uma_BreakdownElementDescription

def test_uma_BreakdownElementDescription___init__():
    assert uma_BreakdownElementDescription.__init__(uma_BreakdownElementDescription(''), '') == None


from python_code import uma_CompositeRole

def test_uma_CompositeRole___init__():
    assert uma_CompositeRole.__init__(uma_CompositeRole('', uma_CompositeRole=set()), '', uma_CompositeRole=set()) == None


from python_code import uma_ContentCategoryPackage

def test_uma_ContentCategoryPackage___init__():
    assert uma_ContentCategoryPackage.__init__(uma_ContentCategoryPackage('', uma_ContentCategoryPackage=set()), '', uma_ContentCategoryPackage=set()) == None


from python_code import uma_ContentPackage

def test_uma_ContentPackage___init__():
    assert uma_ContentPackage.__init__(uma_ContentPackage('', uma_ContentPackage=set()), '', uma_ContentPackage=set()) == None


from python_code import uma_CustomCategory

def test_uma_CustomCategory___init__():
    assert uma_CustomCategory.__init__(uma_CustomCategory('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_Deliverable

def test_uma_Deliverable___init__():
    assert uma_Deliverable.__init__(uma_Deliverable('', '\x00'), '\x00\x00', '') == None


from python_code import uma_DeliverableDescription

def test_uma_DeliverableDescription___init__():
    assert uma_DeliverableDescription.__init__(uma_DeliverableDescription('', '\x00'), '\x00\x00', '') == None


from python_code import uma_DeliveryProcess

def test_uma_DeliveryProcess___init__():
    assert uma_DeliveryProcess.__init__(uma_DeliveryProcess('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_DeliveryProcessDescription

def test_uma_DeliveryProcessDescription___init__():
    assert uma_DeliveryProcessDescription.__init__(uma_DeliveryProcessDescription('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import uma_Descriptor

def test_uma_Descriptor___init__():
    assert uma_Descriptor.__init__(uma_Descriptor(''), '') == None


from python_code import uma_DescriptorDescription

def test_uma_DescriptorDescription___init__():
    assert uma_DescriptorDescription.__init__(uma_DescriptorDescription(''), '') == None


from python_code import uma_DisciplineGrouping

def test_uma_DisciplineGrouping___init__():
    assert uma_DisciplineGrouping.__init__(uma_DisciplineGrouping('', '\x00'), '\x00\x00', '') == None


from python_code import uma_Estimate

def test_uma_Estimate___init__():
    assert uma_Estimate.__init__(uma_Estimate('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_GuidanceDescription

def test_uma_GuidanceDescription___init__():
    assert uma_GuidanceDescription.__init__(uma_GuidanceDescription(''), '') == None


from python_code import uma_Kind

def test_uma_Kind___init__():
    assert uma_Kind.__init__(uma_Kind(''), '') == None


from python_code import uma_MethodElement

def test_uma_MethodElement___init__():
    assert uma_MethodElement.__init__(uma_MethodElement('', '', '\x00', '', '', '', uma_MethodElement=set(), uma_MethodElement25=set()), '', '', '', '', '', '', uma_MethodElement=set(), uma_MethodElement25=set()) == None


from python_code import uma_MethodUnit

def test_uma_MethodUnit___init__():
    assert uma_MethodUnit.__init__(uma_MethodUnit('', '', '', '', ''), '', '', '', '', '') == None


from python_code import uma_Milestone

def test_uma_Milestone___init__():
    assert uma_Milestone.__init__(uma_Milestone(''), '') == None


from python_code import uma_NamedElement

def test_uma_NamedElement___init__():
    assert uma_NamedElement.__init__(uma_NamedElement(''), '') == None


from python_code import uma_PlanningData

def test_uma_PlanningData___init__():
    assert uma_PlanningData.__init__(uma_PlanningData('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_PracticeDescription

def test_uma_PracticeDescription___init__():
    assert uma_PracticeDescription.__init__(uma_PracticeDescription('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import uma_ProcessDescription

def test_uma_ProcessDescription___init__():
    assert uma_ProcessDescription.__init__(uma_ProcessDescription('', '\x00'), '\x00\x00', '') == None


from python_code import uma_ProcessPackage

def test_uma_ProcessPackage___init__():
    assert uma_ProcessPackage.__init__(uma_ProcessPackage('', uma_ProcessPackage=set()), '', uma_ProcessPackage=set()) == None


from python_code import uma_ProcessPlanningTemplate

def test_uma_ProcessPlanningTemplate___init__():
    assert uma_ProcessPlanningTemplate.__init__(uma_ProcessPlanningTemplate('', '\x00'), '\x00\x00', '') == None


from python_code import uma_RoleDescription

def test_uma_RoleDescription___init__():
    assert uma_RoleDescription.__init__(uma_RoleDescription('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_RoleDescriptor

def test_uma_RoleDescriptor___init__():
    assert uma_RoleDescriptor.__init__(uma_RoleDescriptor('', '\x00'), '\x00\x00', '') == None


from python_code import uma_RoleSet

def test_uma_RoleSet___init__():
    assert uma_RoleSet.__init__(uma_RoleSet('', '\x00'), '\x00\x00', '') == None


from python_code import uma_RoleSetGrouping

def test_uma_RoleSetGrouping___init__():
    assert uma_RoleSetGrouping.__init__(uma_RoleSetGrouping('', '\x00'), '\x00\x00', '') == None


from python_code import uma_Task

def test_uma_Task___init__():
    assert uma_Task.__init__(uma_Task('\x00', '', '', '', '', '', '', '', '', '', '\x00'), '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import uma_TaskDescription

def test_uma_TaskDescription___init__():
    assert uma_TaskDescription.__init__(uma_TaskDescription('', '\x00'), '\x00\x00', '') == None


from python_code import uma_TeamProfile

def test_uma_TeamProfile___init__():
    assert uma_TeamProfile.__init__(uma_TeamProfile('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import uma_Tool

def test_uma_Tool___init__():
    assert uma_Tool.__init__(uma_Tool('', '\x00'), '\x00\x00', '') == None


from python_code import uma_WorkBreakdownElement

def test_uma_WorkBreakdownElement___init__():
    assert uma_WorkBreakdownElement.__init__(uma_WorkBreakdownElement('', '', '', '', uma_WorkBreakdownElement=set()), '', '', '', '', uma_WorkBreakdownElement=set()) == None


from python_code import uma_WorkDefinition

def test_uma_WorkDefinition___init__():
    assert uma_WorkDefinition.__init__(uma_WorkDefinition('', '\x00'), '\x00\x00', '') == None


from python_code import uma_WorkProduct

def test_uma_WorkProduct___init__():
    assert uma_WorkProduct.__init__(uma_WorkProduct('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import uma_WorkProductDescription

def test_uma_WorkProductDescription___init__():
    assert uma_WorkProductDescription.__init__(uma_WorkProductDescription('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_WorkProductType

def test_uma_WorkProductType___init__():
    assert uma_WorkProductType.__init__(uma_WorkProductType('', '\x00'), '\x00\x00', '') == None

