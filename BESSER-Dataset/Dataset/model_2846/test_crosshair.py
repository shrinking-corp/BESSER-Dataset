from python_code import RepresentModel
from python_code import frontend_core_ClassUse

def test_frontend_core_ClassUse___init__():
    assert frontend_core_ClassUse.__init__(frontend_core_ClassUse('', False, frontend_core_ClassUse=RepresentModel()), '', True, frontend_core_ClassUse=RepresentModel()) == None


from python_code import frontend_core_GenericAnnotation

def test_frontend_core_GenericAnnotation___init__():
    assert frontend_core_GenericAnnotation.__init__(frontend_core_GenericAnnotation('', frontend_core_GenericAnnotation=set()), '', frontend_core_GenericAnnotation=set()) == None


from python_code import TypeExpression
from python_code import frontend_core_InlineFeature

def test_frontend_core_InlineFeature___init__():
    assert frontend_core_InlineFeature.__init__(frontend_core_InlineFeature(False, frontend_core_InlineFeature=TypeExpression()), False, frontend_core_InlineFeature=TypeExpression()) == None


from python_code import frontend_core_LocatedElement

def test_frontend_core_LocatedElement___init__():
    assert frontend_core_LocatedElement.__init__(frontend_core_LocatedElement(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import frontend_core_AnnotableElement
from python_code import frontend_core_MetamodelModelAnnotation
from python_code import frontend_core_TransformationDefinition

def test_frontend_core_MetamodelModelAnnotation___init__():
    assert frontend_core_MetamodelModelAnnotation.__init__(frontend_core_MetamodelModelAnnotation('', Annotation=frontend_core_AnnotableElement(), Annotation245=frontend_core_TransformationDefinition()), '', Annotation=frontend_core_AnnotableElement(), Annotation245=frontend_core_TransformationDefinition()) == None


from python_code import frontend_core_NamedElement

def test_frontend_core_NamedElement___init__():
    assert frontend_core_NamedElement.__init__(frontend_core_NamedElement(''), '') == None


from python_code import frontend_core_AnnotableElement
from python_code import frontend_core_OptimizationsAnnotation
from python_code import frontend_core_TransformationDefinition

def test_frontend_core_OptimizationsAnnotation___init__():
    assert frontend_core_OptimizationsAnnotation.__init__(frontend_core_OptimizationsAnnotation(True, Annotation=frontend_core_AnnotableElement(), Annotation245=frontend_core_TransformationDefinition()), False, Annotation=frontend_core_AnnotableElement(), Annotation245=frontend_core_TransformationDefinition()) == None


from python_code import frontend_core_ImplicitlyAnnotableElement
from python_code import frontend_core_PotencyAnnotation

def test_frontend_core_PotencyAnnotation___init__():
    assert frontend_core_PotencyAnnotation.__init__(frontend_core_PotencyAnnotation('', SingleAnnotation=frontend_core_ImplicitlyAnnotableElement()), '', SingleAnnotation=frontend_core_ImplicitlyAnnotableElement()) == None

