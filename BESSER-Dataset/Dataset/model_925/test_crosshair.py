from python_code import uma_ActivityDescription

def test_uma_ActivityDescription___init__():
    assert uma_ActivityDescription.__init__(uma_ActivityDescription('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_ApplicableMetaClassInfo
from python_code import uma_Kind

def test_uma_ApplicableMetaClassInfo___init__():
    assert uma_ApplicableMetaClassInfo.__init__(uma_ApplicableMetaClassInfo('', uma_ApplicableMetaClassInfo=uma_Kind()), '', uma_ApplicableMetaClassInfo=uma_Kind()) == None


from python_code import uma_ArtifactDescription

def test_uma_ArtifactDescription___init__():
    assert uma_ArtifactDescription.__init__(uma_ArtifactDescription('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import uma_BreakdownElementDescription

def test_uma_BreakdownElementDescription___init__():
    assert uma_BreakdownElementDescription.__init__(uma_BreakdownElementDescription(''), '') == None


from python_code import uma_Classifier

def test_uma_Classifier___init__():
    assert uma_Classifier.__init__(uma_Classifier(''), '') == None


from python_code import uma_DeliverableDescription

def test_uma_DeliverableDescription___init__():
    assert uma_DeliverableDescription.__init__(uma_DeliverableDescription('', '\x00'), '\x00\x00', '') == None


from python_code import uma_DeliveryProcessDescription

def test_uma_DeliveryProcessDescription___init__():
    assert uma_DeliveryProcessDescription.__init__(uma_DeliveryProcessDescription('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import uma_Descriptor

def test_uma_Descriptor___init__():
    assert uma_Descriptor.__init__(uma_Descriptor(''), '') == None


from python_code import uma_DescriptorDescription

def test_uma_DescriptorDescription___init__():
    assert uma_DescriptorDescription.__init__(uma_DescriptorDescription(''), '') == None


from python_code import uma_Dimension
from python_code import uma_GraphNode

def test_uma_Dimension___init__():
    assert uma_Dimension.__init__(uma_Dimension('', '\x00', uma_Dimension=uma_GraphNode()), '\x00\x00', '', uma_Dimension=uma_GraphNode()) == None


from python_code import uma_GuidanceDescription

def test_uma_GuidanceDescription___init__():
    assert uma_GuidanceDescription.__init__(uma_GuidanceDescription(''), '') == None


from python_code import uma_Image

def test_uma_Image___init__():
    assert uma_Image.__init__(uma_Image('', '\x00'), '\x00\x00', '') == None


from python_code import uma_MethodElement
from python_code import uma_UMASemanticModelBridge

def test_uma_MethodElement___init__():
    assert uma_MethodElement.__init__(uma_MethodElement('\x00', '', '', '', '', uma_MethodElement=set(), uma_MethodElement2=set(), uma_MethodElement4=set(), uma_MethodElement314=uma_UMASemanticModelBridge()), '', '', '', '', '', uma_MethodElement=set(), uma_MethodElement2=set(), uma_MethodElement4=set(), uma_MethodElement314=uma_UMASemanticModelBridge()) == None


from python_code import uma_MethodUnit
from python_code import uma_SupportingMaterial

def test_uma_MethodUnit___init__():
    assert uma_MethodUnit.__init__(uma_MethodUnit('\x00\x00', '', '', '', uma_MethodUnit=uma_SupportingMaterial()), '', '', '', '', uma_MethodUnit=uma_SupportingMaterial()) == None


from python_code import uma_NamedElement

def test_uma_NamedElement___init__():
    assert uma_NamedElement.__init__(uma_NamedElement(''), '') == None


from python_code import uma_PracticeDescription

def test_uma_PracticeDescription___init__():
    assert uma_PracticeDescription.__init__(uma_PracticeDescription('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import uma_ProcessDescription

def test_uma_ProcessDescription___init__():
    assert uma_ProcessDescription.__init__(uma_ProcessDescription('', '\x00'), '\x00\x00', '') == None


from python_code import uma_RoleDescription

def test_uma_RoleDescription___init__():
    assert uma_RoleDescription.__init__(uma_RoleDescription('', '', '\x00\x00'), '', '', '') == None


from python_code import uma_SimpleSemanticModelElement

def test_uma_SimpleSemanticModelElement___init__():
    assert uma_SimpleSemanticModelElement.__init__(uma_SimpleSemanticModelElement(''), '') == None


from python_code import uma_TaskDescription

def test_uma_TaskDescription___init__():
    assert uma_TaskDescription.__init__(uma_TaskDescription('', '\x00'), '\x00\x00', '') == None


from python_code import uma_TextElement

def test_uma_TextElement___init__():
    assert uma_TextElement.__init__(uma_TextElement(''), '') == None


from python_code import uma_WorkProductDescription

def test_uma_WorkProductDescription___init__():
    assert uma_WorkProductDescription.__init__(uma_WorkProductDescription('', '', '\x00\x00'), '', '', '') == None

