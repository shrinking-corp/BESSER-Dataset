from python_code import emof_Class
from python_code import emof_Comment
from python_code import emof_Operation
from python_code import emof_Package
from python_code import emof_TypedElement
from python_code import essentialocl_CollectionType
from python_code import essentialocl_TypeExp
from python_code import imperativeocl_AnonymousTupleType
from python_code import imperativeocl_DictionaryType
from python_code import imperativeocl_RaiseExp
from python_code import imperativeocl_TryExp
from python_code import imperativeocl_Typedef

def test_emof_Class___init__():
    assert emof_Class.__init__(emof_Class('', emof_Class=set(), class_=set(), emof_Class110=set(), Type389=essentialocl_CollectionType(), Type=imperativeocl_TryExp(), Type63=imperativeocl_RaiseExp(), Type141=emof_TypedElement(), Type347=essentialocl_TypeExp(), Type102=imperativeocl_AnonymousTupleType(), Type126=emof_Package('', package=set(), emof_Package=set(), NamedElement=emof_Comment()), Type124=emof_Operation(), Type80=imperativeocl_DictionaryType(), Type67=imperativeocl_Typedef()), '', emof_Class=set(), class_=set(), emof_Class110=set(), Type389=essentialocl_CollectionType(), Type=imperativeocl_TryExp(), Type63=imperativeocl_RaiseExp(), Type141=emof_TypedElement(), Type347=essentialocl_TypeExp(), Type102=imperativeocl_AnonymousTupleType(), Type126=emof_Package('', package=set(), emof_Package=set(), NamedElement=emof_Comment()), Type124=emof_Operation(), Type80=imperativeocl_DictionaryType(), Type67=imperativeocl_Typedef()) == None


from python_code import emof_MultiplicityElement

def test_emof_MultiplicityElement___init__():
    assert emof_MultiplicityElement.__init__(emof_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import emof_Comment
from python_code import emof_Package

def test_emof_Package___init__():
    assert emof_Package.__init__(emof_Package('', package=set(), emof_Package=set(), NamedElement=emof_Comment()), '', package=set(), emof_Package=set(), NamedElement=emof_Comment()) == None


from python_code import Class
from python_code import Module
from python_code import Property
from python_code import emof_Property

def test_emof_Property___init__():
    assert emof_Property.__init__(emof_Property('', '', '\x00', '', '', emof_Property=Class(), emof_Property136=Property(), configProperty=Module()), '', '', '', '', '', emof_Property=Class(), emof_Property136=Property(), configProperty=Module()) == None


from python_code import essentialocl_BooleanLiteralExp

def test_essentialocl_BooleanLiteralExp___init__():
    assert essentialocl_BooleanLiteralExp.__init__(essentialocl_BooleanLiteralExp(''), '') == None


from python_code import essentialocl_CollectionLiteralExp

def test_essentialocl_CollectionLiteralExp___init__():
    assert essentialocl_CollectionLiteralExp.__init__(essentialocl_CollectionLiteralExp('', CollectionLiteralExp=set()), '', CollectionLiteralExp=set()) == None


from python_code import essentialocl_IntegerLiteralExp

def test_essentialocl_IntegerLiteralExp___init__():
    assert essentialocl_IntegerLiteralExp.__init__(essentialocl_IntegerLiteralExp(''), '') == None


from python_code import essentialocl_RealLiteralExp

def test_essentialocl_RealLiteralExp___init__():
    assert essentialocl_RealLiteralExp.__init__(essentialocl_RealLiteralExp(''), '') == None


from python_code import essentialocl_StringLiteralExp

def test_essentialocl_StringLiteralExp___init__():
    assert essentialocl_StringLiteralExp.__init__(essentialocl_StringLiteralExp(''), '') == None


from python_code import essentialocl_UnlimitedNaturalExp

def test_essentialocl_UnlimitedNaturalExp___init__():
    assert essentialocl_UnlimitedNaturalExp.__init__(essentialocl_UnlimitedNaturalExp(''), '') == None


from python_code import LogExp
from python_code import OclExpression
from python_code import imperativeocl_AssertExp

def test_imperativeocl_AssertExp___init__():
    assert imperativeocl_AssertExp.__init__(imperativeocl_AssertExp('', imperativeocl_AssertExp=LogExp(), imperativeocl_AssertExp93=OclExpression()), '', imperativeocl_AssertExp=LogExp(), imperativeocl_AssertExp93=OclExpression()) == None


from python_code import OclExpression
from python_code import imperativeocl_AssignExp

def test_imperativeocl_AssignExp___init__():
    assert imperativeocl_AssignExp.__init__(imperativeocl_AssignExp('', imperativeocl_AssignExp=set(), imperativeocl_AssignExp22=OclExpression(), imperativeocl_AssignExp25=OclExpression()), '', imperativeocl_AssignExp=set(), imperativeocl_AssignExp22=OclExpression(), imperativeocl_AssignExp25=OclExpression()) == None


from python_code import emof_Comment
from python_code import emof_Operation
from python_code import emof_Package
from python_code import emof_TypedElement
from python_code import essentialocl_CollectionType
from python_code import essentialocl_TypeExp
from python_code import imperativeocl_AnonymousTupleType
from python_code import imperativeocl_DictionaryType
from python_code import imperativeocl_RaiseExp
from python_code import imperativeocl_TemplateParameterType
from python_code import imperativeocl_TryExp
from python_code import imperativeocl_Typedef

def test_imperativeocl_TemplateParameterType___init__():
    assert imperativeocl_TemplateParameterType.__init__(imperativeocl_TemplateParameterType('', Type389=essentialocl_CollectionType(), Type=imperativeocl_TryExp(), Type63=imperativeocl_RaiseExp(), Type141=emof_TypedElement(), Type347=essentialocl_TypeExp(), Type102=imperativeocl_AnonymousTupleType(), Type126=emof_Package('', package=set(), emof_Package=set(), NamedElement=emof_Comment()), Type124=emof_Operation(), Type80=imperativeocl_DictionaryType(), Type67=imperativeocl_Typedef()), '', Type389=essentialocl_CollectionType(), Type=imperativeocl_TryExp(), Type63=imperativeocl_RaiseExp(), Type141=emof_TypedElement(), Type347=essentialocl_TypeExp(), Type102=imperativeocl_AnonymousTupleType(), Type126=emof_Package('', package=set(), emof_Package=set(), NamedElement=emof_Comment()), Type124=emof_Operation(), Type80=imperativeocl_DictionaryType(), Type67=imperativeocl_Typedef()) == None


from python_code import Variable
from python_code import imperativeocl_VariableInitExp

def test_imperativeocl_VariableInitExp___init__():
    assert imperativeocl_VariableInitExp.__init__(imperativeocl_VariableInitExp('', imperativeocl_VariableInitExp=Variable()), '', imperativeocl_VariableInitExp=Variable()) == None


from python_code import Rule
from python_code import TypedModel
from python_code import emof_Comment
from python_code import qvtbase_Domain

def test_qvtbase_Domain___init__():
    assert qvtbase_Domain.__init__(qvtbase_Domain('\x00', '', domain=Rule(), qvtbase_Domain=TypedModel(), NamedElement=emof_Comment()), '', '', domain=Rule(), qvtbase_Domain=TypedModel(), NamedElement=emof_Comment()) == None


from python_code import BottomPattern
from python_code import OclExpression
from python_code import Property
from python_code import qvtcore_Assignment

def test_qvtcore_Assignment___init__():
    assert qvtcore_Assignment.__init__(qvtcore_Assignment('', qvtcore_Assignment233=OclExpression(), qvtcore_Assignment236=Property(), assignment=BottomPattern(), qvtcore_Assignment=OclExpression()), '', qvtcore_Assignment233=OclExpression(), qvtcore_Assignment236=Property(), assignment=BottomPattern(), qvtcore_Assignment=OclExpression()) == None


from python_code import BottomPattern
from python_code import OperationCallExp
from python_code import qvtcore_EnforcementOperation

def test_qvtcore_EnforcementOperation___init__():
    assert qvtcore_EnforcementOperation.__init__(qvtcore_EnforcementOperation('', enforcementOperation=BottomPattern(), qvtcore_EnforcementOperation=OperationCallExp()), '\x00', enforcementOperation=BottomPattern(), qvtcore_EnforcementOperation=OperationCallExp()) == None

