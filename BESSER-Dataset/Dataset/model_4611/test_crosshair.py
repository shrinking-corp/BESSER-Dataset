from python_code import viewpoint_BasicLabelStyle

def test_viewpoint_BasicLabelStyle___init__():
    assert viewpoint_BasicLabelStyle.__init__(viewpoint_BasicLabelStyle(False, '', '', 0, ''), True, '', '', 0, '') == None


from python_code import viewpoint_Customizable

def test_viewpoint_Customizable___init__():
    assert viewpoint_Customizable.__init__(viewpoint_Customizable(''), '') == None


from python_code import viewpoint_DAnalysisCustomData
from python_code import viewpoint_EObject

def test_viewpoint_DAnalysisCustomData___init__():
    assert viewpoint_DAnalysisCustomData.__init__(viewpoint_DAnalysisCustomData('', viewpoint_DAnalysisCustomData=viewpoint_EObject()), '', viewpoint_DAnalysisCustomData=viewpoint_EObject()) == None


from python_code import viewpoint_DMappingBased

def test_viewpoint_DMappingBased___init__():
    assert viewpoint_DMappingBased.__init__(viewpoint_DMappingBased()) == None

def test_viewpoint_DMappingBased_getMapping():
    assert viewpoint_DMappingBased.getMapping(viewpoint_DMappingBased()) == None


from python_code import viewpoint_DResource
from python_code import viewpoint_DResourceContainer

def test_viewpoint_DResource___init__():
    assert viewpoint_DResource.__init__(viewpoint_DResource('', '\x00', viewpoint_DResource=viewpoint_DResourceContainer()), '\x00\x00', '', viewpoint_DResource=viewpoint_DResourceContainer()) == None


from python_code import viewpoint_DStylizable

def test_viewpoint_DStylizable___init__():
    assert viewpoint_DStylizable.__init__(viewpoint_DStylizable()) == None

def test_viewpoint_DStylizable_getStyle():
    assert viewpoint_DStylizable.getStyle(viewpoint_DStylizable()) == None


from python_code import viewpoint_IdentifiedElement

def test_viewpoint_IdentifiedElement___init__():
    assert viewpoint_IdentifiedElement.__init__(viewpoint_IdentifiedElement(''), '') == None


from python_code import viewpoint_LabelStyle

def test_viewpoint_LabelStyle___init__():
    assert viewpoint_LabelStyle.__init__(viewpoint_LabelStyle(''), '') == None


from python_code import tool_ToolEntry
from python_code import viewpoint_ToolGroupInstance
from python_code import viewpoint_ToolInstance
from python_code import viewpoint_ToolSectionInstance

def test_viewpoint_ToolInstance___init__():
    assert viewpoint_ToolInstance.__init__(viewpoint_ToolInstance('\x00\x00', False, False, True, viewpoint_ToolInstance73=viewpoint_ToolSectionInstance(), viewpoint_ToolInstance=tool_ToolEntry(), viewpoint_ToolInstance67=viewpoint_ToolGroupInstance()), '', False, False, False, viewpoint_ToolInstance73=viewpoint_ToolSectionInstance(), viewpoint_ToolInstance=tool_ToolEntry(), viewpoint_ToolInstance67=viewpoint_ToolGroupInstance()) == None


from python_code import viewpoint_audit_InformationSection

def test_viewpoint_audit_InformationSection___init__():
    assert viewpoint_audit_InformationSection.__init__(viewpoint_audit_InformationSection()) == None

def test_viewpoint_audit_InformationSection_getContent():
    assert viewpoint_audit_InformationSection.getContent(viewpoint_audit_InformationSection(), '') == None


from python_code import viewpoint_audit_TemplateInformationSection

def test_viewpoint_audit_TemplateInformationSection___init__():
    assert viewpoint_audit_TemplateInformationSection.__init__(viewpoint_audit_TemplateInformationSection(''), '') == None


from python_code import viewpoint_description_AbstractMappingImport

def test_viewpoint_description_AbstractMappingImport___init__():
    assert viewpoint_description_AbstractMappingImport.__init__(viewpoint_description_AbstractMappingImport(False, False), False, False) == None


from python_code import viewpoint_description_AbstractVariable

def test_viewpoint_description_AbstractVariable___init__():
    assert viewpoint_description_AbstractVariable.__init__(viewpoint_description_AbstractVariable(''), '') == None


from python_code import description_viewpoint_EObject
from python_code import viewpoint_description_AnnotationEntry

def test_viewpoint_description_AnnotationEntry___init__():
    assert viewpoint_description_AnnotationEntry.__init__(viewpoint_description_AnnotationEntry('', viewpoint_description_AnnotationEntry=description_viewpoint_EObject()), '', viewpoint_description_AnnotationEntry=description_viewpoint_EObject()) == None


from python_code import FixedColor
from python_code import viewpoint_description_ColorStep

def test_viewpoint_description_ColorStep___init__():
    assert viewpoint_description_ColorStep.__init__(viewpoint_description_ColorStep('', viewpoint_description_ColorStep=FixedColor()), '\x00', viewpoint_description_ColorStep=FixedColor()) == None


from python_code import viewpoint_description_ComputedColor

def test_viewpoint_description_ComputedColor___init__():
    assert viewpoint_description_ComputedColor.__init__(viewpoint_description_ComputedColor('', '', '\x00\x00'), '', '', '') == None


from python_code import viewpoint_description_ConditionalStyleDescription

def test_viewpoint_description_ConditionalStyleDescription___init__():
    assert viewpoint_description_ConditionalStyleDescription.__init__(viewpoint_description_ConditionalStyleDescription(''), '') == None

def test_viewpoint_description_ConditionalStyleDescription_checkPredicate():
    assert viewpoint_description_ConditionalStyleDescription.checkPredicate(viewpoint_description_ConditionalStyleDescription(''), 0, '\x00\x00', '') == None


from python_code import viewpoint_description_DAnnotation

def test_viewpoint_description_DAnnotation___init__():
    assert viewpoint_description_DAnnotation.__init__(viewpoint_description_DAnnotation('', viewpoint_description_DAnnotation=set(), viewpoint_description_DAnnotation115=set()), '', viewpoint_description_DAnnotation=set(), viewpoint_description_DAnnotation115=set()) == None


from python_code import viewpoint_description_DAnnotationEntry

def test_viewpoint_description_DAnnotationEntry___init__():
    assert viewpoint_description_DAnnotationEntry.__init__(viewpoint_description_DAnnotationEntry('', '\x00'), '\x00\x00', '') == None


from python_code import viewpoint_description_DModelElement

def test_viewpoint_description_DModelElement___init__():
    assert viewpoint_description_DModelElement.__init__(viewpoint_description_DModelElement(viewpoint_description_DModelElement=set()), viewpoint_description_DModelElement=set()) == None

def test_viewpoint_description_DModelElement_getDAnnotation():
    assert viewpoint_description_DModelElement.getDAnnotation(viewpoint_description_DModelElement(viewpoint_description_DModelElement=set()), 0) == None


from python_code import viewpoint_description_DecorationDescription

def test_viewpoint_description_DecorationDescription___init__():
    assert viewpoint_description_DecorationDescription.__init__(viewpoint_description_DecorationDescription('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import viewpoint_description_DocumentedElement

def test_viewpoint_description_DocumentedElement___init__():
    assert viewpoint_description_DocumentedElement.__init__(viewpoint_description_DocumentedElement(''), '') == None


from python_code import viewpoint_description_Customization
from python_code import viewpoint_description_EAttributeCustomization
from python_code import viewpoint_description_VSMElementCustomization
from python_code import viewpoint_description_VSMElementCustomizationReuse

def test_viewpoint_description_EAttributeCustomization___init__():
    assert viewpoint_description_EAttributeCustomization.__init__(viewpoint_description_EAttributeCustomization('', '', EStructuralFeatureCustomization123=viewpoint_description_VSMElementCustomizationReuse(), EStructuralFeatureCustomization=viewpoint_description_VSMElementCustomization('', viewpoint_description_VSMElementCustomization=set(), IVSMElementCustomization=viewpoint_description_Customization())), '', '', EStructuralFeatureCustomization123=viewpoint_description_VSMElementCustomizationReuse(), EStructuralFeatureCustomization=viewpoint_description_VSMElementCustomization('', viewpoint_description_VSMElementCustomization=set(), IVSMElementCustomization=viewpoint_description_Customization())) == None


from python_code import description_viewpoint_EObject
from python_code import viewpoint_description_Customization
from python_code import viewpoint_description_EReferenceCustomization
from python_code import viewpoint_description_VSMElementCustomization
from python_code import viewpoint_description_VSMElementCustomizationReuse

def test_viewpoint_description_EReferenceCustomization___init__():
    assert viewpoint_description_EReferenceCustomization.__init__(viewpoint_description_EReferenceCustomization('\x00\x00', viewpoint_description_EReferenceCustomization=description_viewpoint_EObject(), EStructuralFeatureCustomization123=viewpoint_description_VSMElementCustomizationReuse(), EStructuralFeatureCustomization=viewpoint_description_VSMElementCustomization('', viewpoint_description_VSMElementCustomization=set(), IVSMElementCustomization=viewpoint_description_Customization())), '', viewpoint_description_EReferenceCustomization=description_viewpoint_EObject(), EStructuralFeatureCustomization123=viewpoint_description_VSMElementCustomizationReuse(), EStructuralFeatureCustomization=viewpoint_description_VSMElementCustomization('', viewpoint_description_VSMElementCustomization=set(), IVSMElementCustomization=viewpoint_description_Customization())) == None


from python_code import viewpoint_description_EStructuralFeatureCustomization

def test_viewpoint_description_EStructuralFeatureCustomization___init__():
    assert viewpoint_description_EStructuralFeatureCustomization.__init__(viewpoint_description_EStructuralFeatureCustomization(False, viewpoint_description_EStructuralFeatureCustomization=set()), False, viewpoint_description_EStructuralFeatureCustomization=set()) == None


from python_code import viewpoint_description_EndUserDocumentedElement

def test_viewpoint_description_EndUserDocumentedElement___init__():
    assert viewpoint_description_EndUserDocumentedElement.__init__(viewpoint_description_EndUserDocumentedElement(''), '') == None


from python_code import ColorDescription
from python_code import viewpoint_description_FixedColor
from python_code import viewpoint_style_BasicLabelStyleDescription

def test_viewpoint_description_FixedColor___init__():
    assert viewpoint_description_FixedColor.__init__(viewpoint_description_FixedColor(0, 0, 0, ColorDescription=viewpoint_style_BasicLabelStyleDescription(0, '', False, '', '', viewpoint_style_BasicLabelStyleDescription=ColorDescription())), 0, 0, 0, ColorDescription=viewpoint_style_BasicLabelStyleDescription(0, '', False, '', '\x00', viewpoint_style_BasicLabelStyleDescription=ColorDescription())) == None


from python_code import SytemColorsPalette
from python_code import viewpoint_description_Group

def test_viewpoint_description_Group___init__():
    assert viewpoint_description_Group.__init__(viewpoint_description_Group('', '', viewpoint_description_Group=set(), viewpoint_description_Group83=SytemColorsPalette(), viewpoint_description_Group85=set(), viewpoint_description_Group87=set()), '', '', viewpoint_description_Group=set(), viewpoint_description_Group83=SytemColorsPalette(), viewpoint_description_Group85=set(), viewpoint_description_Group87=set()) == None


from python_code import viewpoint_description_IdentifiedElement

def test_viewpoint_description_IdentifiedElement___init__():
    assert viewpoint_description_IdentifiedElement.__init__(viewpoint_description_IdentifiedElement('', '\x00'), '\x00\x00', '') == None


from python_code import viewpoint_description_InteractiveVariableDescription

def test_viewpoint_description_InteractiveVariableDescription___init__():
    assert viewpoint_description_InteractiveVariableDescription.__init__(viewpoint_description_InteractiveVariableDescription(''), '') == None


from python_code import viewpoint_description_InterpolatedColor

def test_viewpoint_description_InterpolatedColor___init__():
    assert viewpoint_description_InterpolatedColor.__init__(viewpoint_description_InterpolatedColor('', '', '', viewpoint_description_InterpolatedColor=set()), '', '', '', viewpoint_description_InterpolatedColor=set()) == None


from python_code import viewpoint_description_JavaExtension

def test_viewpoint_description_JavaExtension___init__():
    assert viewpoint_description_JavaExtension.__init__(viewpoint_description_JavaExtension(''), '') == None


from python_code import viewpoint_description_RepresentationDescription

def test_viewpoint_description_RepresentationDescription___init__():
    assert viewpoint_description_RepresentationDescription.__init__(viewpoint_description_RepresentationDescription('', False, False, viewpoint_description_RepresentationDescription=set()), '', False, True, viewpoint_description_RepresentationDescription=set()) == None


from python_code import viewpoint_description_RepresentationExtensionDescription

def test_viewpoint_description_RepresentationExtensionDescription___init__():
    assert viewpoint_description_RepresentationExtensionDescription.__init__(viewpoint_description_RepresentationExtensionDescription('', '', '', viewpoint_description_RepresentationExtensionDescription=set()), '', '', '', viewpoint_description_RepresentationExtensionDescription=set()) == None


from python_code import viewpoint_description_RepresentationTemplate

def test_viewpoint_description_RepresentationTemplate___init__():
    assert viewpoint_description_RepresentationTemplate.__init__(viewpoint_description_RepresentationTemplate('', viewpoint_description_RepresentationTemplate=set()), '', viewpoint_description_RepresentationTemplate=set()) == None


from python_code import viewpoint_description_SelectionDescription

def test_viewpoint_description_SelectionDescription___init__():
    assert viewpoint_description_SelectionDescription.__init__(viewpoint_description_SelectionDescription('', False, False, '', '', ''), '', False, False, '', '\x00', '') == None


from python_code import viewpoint_Decoration
from python_code import viewpoint_description_DecorationDescriptionsSet
from python_code import viewpoint_description_SemanticBasedDecoration

def test_viewpoint_description_SemanticBasedDecoration___init__():
    assert viewpoint_description_SemanticBasedDecoration.__init__(viewpoint_description_SemanticBasedDecoration('', DecorationDescription119=viewpoint_description_DecorationDescriptionsSet(), DecorationDescription=viewpoint_Decoration()), '', DecorationDescription119=viewpoint_description_DecorationDescriptionsSet(), DecorationDescription=viewpoint_Decoration()) == None


from python_code import FixedColor
from python_code import viewpoint_description_ColorStep
from python_code import viewpoint_description_SystemColor

def test_viewpoint_description_SystemColor___init__():
    assert viewpoint_description_SystemColor.__init__(viewpoint_description_SystemColor('', FixedColor=viewpoint_description_ColorStep('', viewpoint_description_ColorStep=FixedColor())), '', FixedColor=viewpoint_description_ColorStep('', viewpoint_description_ColorStep=FixedColor())) == None


from python_code import description_viewpoint_EDataType
from python_code import viewpoint_description_TypedVariable

def test_viewpoint_description_TypedVariable___init__():
    assert viewpoint_description_TypedVariable.__init__(viewpoint_description_TypedVariable('', viewpoint_description_TypedVariable=description_viewpoint_EDataType()), '', viewpoint_description_TypedVariable=description_viewpoint_EDataType()) == None


from python_code import viewpoint_description_UserColor

def test_viewpoint_description_UserColor___init__():
    assert viewpoint_description_UserColor.__init__(viewpoint_description_UserColor(''), '') == None


from python_code import viewpoint_description_UserColorsPalette

def test_viewpoint_description_UserColorsPalette___init__():
    assert viewpoint_description_UserColorsPalette.__init__(viewpoint_description_UserColorsPalette('', viewpoint_description_UserColorsPalette=set()), '', viewpoint_description_UserColorsPalette=set()) == None


from python_code import viewpoint_description_Customization
from python_code import viewpoint_description_VSMElementCustomization

def test_viewpoint_description_VSMElementCustomization___init__():
    assert viewpoint_description_VSMElementCustomization.__init__(viewpoint_description_VSMElementCustomization('', viewpoint_description_VSMElementCustomization=set(), IVSMElementCustomization=viewpoint_description_Customization()), '', viewpoint_description_VSMElementCustomization=set(), IVSMElementCustomization=viewpoint_description_Customization()) == None

