from python_code import ClassesProv_ElementImport
from python_code import ClassesProv_Namespace
from python_code import ClassesProv_PackageableElement

def test_ClassesProv_ElementImport___init__():
    assert ClassesProv_ElementImport.__init__(ClassesProv_ElementImport('', ClassesProv_ElementImport=ClassesProv_Namespace(), ClassesProv_ElementImport23=ClassesProv_PackageableElement(), ClassesProv_ElementImport26=ClassesProv_Namespace()), '', ClassesProv_ElementImport=ClassesProv_Namespace(), ClassesProv_ElementImport23=ClassesProv_PackageableElement(), ClassesProv_ElementImport26=ClassesProv_Namespace()) == None

from python_code import ClassesProv_Expression
from python_code import ClassesProv_ValueSpecification

def test_ClassesProv_Expression___init__():
    assert ClassesProv_Expression.__init__(ClassesProv_Expression('', ClassesProv_Expression=ClassesProv_ValueSpecification()), '', ClassesProv_Expression=ClassesProv_ValueSpecification()) == None

from python_code import ClassesProv_MultiplicityElement
from python_code import ClassesProv_ValueSpecification

def test_ClassesProv_MultiplicityElement___init__():
    assert ClassesProv_MultiplicityElement.__init__(ClassesProv_MultiplicityElement(False, False, 0, 0, ClassesProv_MultiplicityElement=ClassesProv_ValueSpecification(), ClassesProv_MultiplicityElement55=ClassesProv_ValueSpecification(), ClassesProv_MultiplicityElement59=ClassesProv_ValueSpecification(), ClassesProv_MultiplicityElement62=ClassesProv_ValueSpecification()), False, False, 0, 0, ClassesProv_MultiplicityElement=ClassesProv_ValueSpecification(), ClassesProv_MultiplicityElement55=ClassesProv_ValueSpecification(), ClassesProv_MultiplicityElement59=ClassesProv_ValueSpecification(), ClassesProv_MultiplicityElement62=ClassesProv_ValueSpecification()) == None

from python_code import ClassesProv_Abstraction
from python_code import ClassesProv_OpaqueExpression

def test_ClassesProv_OpaqueExpression___init__():
    assert ClassesProv_OpaqueExpression.__init__(ClassesProv_OpaqueExpression('', '\x00', ClassesProv_OpaqueExpression=ClassesProv_Abstraction()), '\x00\x00', '', ClassesProv_OpaqueExpression=ClassesProv_Abstraction()) == None

from python_code import ClassesProv_Class
from python_code import ClassesProv_DataType
from python_code import ClassesProv_Interface
from python_code import ClassesProv_Operation
from python_code import ClassesProv_Type

def test_ClassesProv_Operation___init__():
    assert ClassesProv_Operation.__init__(ClassesProv_Operation(False, False, False, 0, 0, ClassesProv_Operation182=set(), ClassesProv_Operation185=set(), ClassesProv_Operation188=set(), ClassesProv_Operation191=ClassesProv_Class(), ClassesProv_Operation194=ClassesProv_DataType(), ClassesProv_Operation197=ClassesProv_Interface(), ClassesProv_Operation=ClassesProv_Type(), ClassesProv_Operation204=ClassesProv_Class(), ClassesProv_Operation260=ClassesProv_Interface(), ClassesProv_Operation225=ClassesProv_DataType()), False, False, False, 0, 0, ClassesProv_Operation182=set(), ClassesProv_Operation185=set(), ClassesProv_Operation188=set(), ClassesProv_Operation191=ClassesProv_Class(), ClassesProv_Operation194=ClassesProv_DataType(), ClassesProv_Operation197=ClassesProv_Interface(), ClassesProv_Operation=ClassesProv_Type(), ClassesProv_Operation204=ClassesProv_Class(), ClassesProv_Operation260=ClassesProv_Interface(), ClassesProv_Operation225=ClassesProv_DataType()) == None

from python_code import ClassesProv_BehavioralFeature
from python_code import ClassesProv_Parameter
from python_code import ClassesProv_ValueSpecification

def test_ClassesProv_Parameter___init__():
    assert ClassesProv_Parameter.__init__(ClassesProv_Parameter('', ClassesProv_Parameter=ClassesProv_BehavioralFeature(), ClassesProv_Parameter174=ClassesProv_BehavioralFeature(), ClassesProv_Parameter177=ClassesProv_ValueSpecification()), '', ClassesProv_Parameter=ClassesProv_BehavioralFeature(), ClassesProv_Parameter174=ClassesProv_BehavioralFeature(), ClassesProv_Parameter177=ClassesProv_ValueSpecification()) == None

from python_code import ClassesProv_Slot
from python_code import ClassesProv_StructuralFeature

def test_ClassesProv_StructuralFeature___init__():
    assert ClassesProv_StructuralFeature.__init__(ClassesProv_StructuralFeature(True, ClassesProv_StructuralFeature=ClassesProv_Slot()), False, ClassesProv_StructuralFeature=ClassesProv_Slot()) == None
