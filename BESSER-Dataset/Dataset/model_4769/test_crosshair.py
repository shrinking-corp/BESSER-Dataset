from python_code import atl_types_EObject
from python_code import atl_types_EnumType

def test_atl_types_EnumType___init__():
    assert atl_types_EnumType.__init__(atl_types_EnumType('', atl_types_EnumType=atl_types_EObject()), '', atl_types_EnumType=atl_types_EObject()) == None


from python_code import atl_types_EClass
from python_code import atl_types_Metaclass

def test_atl_types_Metaclass___init__():
    assert atl_types_Metaclass.__init__(atl_types_Metaclass('', atl_types_Metaclass=atl_types_EClass()), '', atl_types_Metaclass=atl_types_EClass()) == None


from python_code import annotations_atl_types_EObject
from python_code import annotations_atl_types_Type
from python_code import atl_types_annotations_BindingAnnotation

def test_atl_types_annotations_BindingAnnotation___init__():
    assert atl_types_annotations_BindingAnnotation.__init__(atl_types_annotations_BindingAnnotation('', atl_types_annotations_BindingAnnotation=annotations_atl_types_EObject(), atl_types_annotations_BindingAnnotation18=annotations_atl_types_EObject(), atl_types_annotations_BindingAnnotation21=annotations_atl_types_Type(), atl_types_annotations_BindingAnnotation24=annotations_atl_types_Type()), '', atl_types_annotations_BindingAnnotation=annotations_atl_types_EObject(), atl_types_annotations_BindingAnnotation18=annotations_atl_types_EObject(), atl_types_annotations_BindingAnnotation21=annotations_atl_types_Type(), atl_types_annotations_BindingAnnotation24=annotations_atl_types_Type()) == None


from python_code import annotations_atl_types_EObject
from python_code import annotations_atl_types_Type
from python_code import atl_types_annotations_HelperAnnotation

def test_atl_types_annotations_HelperAnnotation___init__():
    assert atl_types_annotations_HelperAnnotation.__init__(atl_types_annotations_HelperAnnotation('', atl_types_annotations_HelperAnnotation=annotations_atl_types_EObject(), atl_types_annotations_HelperAnnotation14=annotations_atl_types_Type()), '', atl_types_annotations_HelperAnnotation=annotations_atl_types_EObject(), atl_types_annotations_HelperAnnotation14=annotations_atl_types_Type()) == None

