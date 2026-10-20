from python_code import sooml_Attribute

def test_sooml_Attribute___init__():
    assert sooml_Attribute.__init__(sooml_Attribute(''), '') == None


from python_code import sooml_NamedElement

def test_sooml_NamedElement___init__():
    assert sooml_NamedElement.__init__(sooml_NamedElement(''), '') == None


from python_code import sooml_CallParameterOperationAction
from python_code import sooml_Class
from python_code import sooml_Operation
from python_code import sooml_Parameter
from python_code import sooml_ParameterBinding
from python_code import sooml_ParameterIsInStateCondition
from python_code import sooml_ReferenceAssignmentAction

def test_sooml_Parameter___init__():
    assert sooml_Parameter.__init__(sooml_Parameter('', sooml_Parameter=sooml_Operation(), sooml_Parameter40=sooml_Class(), sooml_Parameter51=sooml_ParameterBinding(), sooml_Parameter60=sooml_ParameterIsInStateCondition(), sooml_Parameter64=sooml_CallParameterOperationAction(), sooml_Parameter66=sooml_ReferenceAssignmentAction()), '', sooml_Parameter=sooml_Operation(), sooml_Parameter40=sooml_Class(), sooml_Parameter51=sooml_ParameterBinding(), sooml_Parameter60=sooml_ParameterIsInStateCondition(), sooml_Parameter64=sooml_CallParameterOperationAction(), sooml_Parameter66=sooml_ReferenceAssignmentAction()) == None


from python_code import sooml_Class
from python_code import sooml_ParameterBinding
from python_code import sooml_StructuralFeature

def test_sooml_StructuralFeature___init__():
    assert sooml_StructuralFeature.__init__(sooml_StructuralFeature(0, 0, sooml_StructuralFeature=sooml_Class(), sooml_StructuralFeature48=sooml_ParameterBinding()), 0, 0, sooml_StructuralFeature=sooml_Class(), sooml_StructuralFeature48=sooml_ParameterBinding()) == None

