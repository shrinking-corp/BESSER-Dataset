from python_code import JTL_JTL_Domain
from python_code import JTL_emof_Comment
from python_code import Model
from python_code import Pattern
from python_code import Relation
from python_code import Variable

def test_JTL_JTL_Domain___init__():
    assert JTL_JTL_Domain.__init__(JTL_JTL_Domain(False, False, domain=Relation(), JTL_JTL_Domain=Pattern(), JTL_JTL_Domain38=Model(), JTL_JTL_Domain41=Variable(), NamedElement=JTL_emof_Comment()), False, False, domain=Relation(), JTL_JTL_Domain=Pattern(), JTL_JTL_Domain38=Model(), JTL_JTL_Domain41=Variable(), NamedElement=JTL_emof_Comment()) == None


from python_code import JTL_JTL_Model
from python_code import JTL_emof_Comment
from python_code import Transformation

def test_JTL_JTL_Model___init__():
    assert JTL_JTL_Model.__init__(JTL_JTL_Model('', modelParameter=Transformation(), JTL_JTL_Model=set(), NamedElement=JTL_emof_Comment()), '', modelParameter=Transformation(), JTL_JTL_Model=set(), NamedElement=JTL_emof_Comment()) == None


from python_code import JTL_JTL_Relation
from python_code import JTL_emof_Comment
from python_code import Transformation
from python_code import When
from python_code import Where

def test_JTL_JTL_Relation___init__():
    assert JTL_JTL_Relation.__init__(JTL_JTL_Relation(False, relation=Transformation(), relation30=set(), whereOwner=Where(), whenOwner=When(), JTL_JTL_Relation=set(), NamedElement=JTL_emof_Comment()), False, relation=Transformation(), relation30=set(), whereOwner=Where(), whenOwner=When(), JTL_JTL_Relation=set(), NamedElement=JTL_emof_Comment()) == None


from python_code import JTL_emof_Class
from python_code import JTL_emof_Comment
from python_code import JTL_emof_Operation
from python_code import JTL_emof_Package
from python_code import JTL_essentialocl_CollectionType
from python_code import JTL_essentialocl_TypeExp
from python_code import JTL_imperativeocl_AnonymousTupleType
from python_code import JTL_imperativeocl_DictionaryType
from python_code import JTL_imperativeocl_RaiseExp
from python_code import JTL_imperativeocl_TryExp
from python_code import JTL_imperativeocl_Typedef

def test_JTL_emof_Class___init__():
    assert JTL_emof_Class.__init__(JTL_emof_Class(False, class_=set(), JTL_emof_Class=set(), Class=set(), Type129=JTL_essentialocl_CollectionType(), Type200=JTL_imperativeocl_RaiseExp(), Type195=JTL_imperativeocl_TryExp(), Type204=JTL_imperativeocl_Typedef(), Type=JTL_emof_Operation(), Type90=JTL_essentialocl_TypeExp(), Type240=JTL_imperativeocl_AnonymousTupleType(), Type217=JTL_imperativeocl_DictionaryType(), Type13=JTL_emof_Package('', package=set(), JTL_emof_Package=set(), NamedElement=JTL_emof_Comment())), False, class_=set(), JTL_emof_Class=set(), Class=set(), Type129=JTL_essentialocl_CollectionType(), Type200=JTL_imperativeocl_RaiseExp(), Type195=JTL_imperativeocl_TryExp(), Type204=JTL_imperativeocl_Typedef(), Type=JTL_emof_Operation(), Type90=JTL_essentialocl_TypeExp(), Type240=JTL_imperativeocl_AnonymousTupleType(), Type217=JTL_imperativeocl_DictionaryType(), Type13=JTL_emof_Package('', package=set(), JTL_emof_Package=set(), NamedElement=JTL_emof_Comment())) == None


from python_code import JTL_emof_MultiplicityElement

def test_JTL_emof_MultiplicityElement___init__():
    assert JTL_emof_MultiplicityElement.__init__(JTL_emof_MultiplicityElement('\x00\x00', '', '', 0), '', '', '', 0) == None


from python_code import JTL_emof_Comment
from python_code import JTL_emof_Package

def test_JTL_emof_Package___init__():
    assert JTL_emof_Package.__init__(JTL_emof_Package('', package=set(), JTL_emof_Package=set(), NamedElement=JTL_emof_Comment()), '', package=set(), JTL_emof_Package=set(), NamedElement=JTL_emof_Comment()) == None


from python_code import Class
from python_code import JTL_emof_Property
from python_code import Property

def test_JTL_emof_Property___init__():
    assert JTL_emof_Property.__init__(JTL_emof_Property(False, False, True, False, '', ownedAttribute=Class(), JTL_emof_Property=Property()), True, False, False, False, '', ownedAttribute=Class(), JTL_emof_Property=Property()) == None


from python_code import JTL_emof_Comment
from python_code import JTL_emof_TypedElement

def test_JTL_emof_TypedElement___init__():
    assert JTL_emof_TypedElement.__init__(JTL_emof_TypedElement('', NamedElement=JTL_emof_Comment()), '', NamedElement=JTL_emof_Comment()) == None


from python_code import JTL_essentialocl_BooleanLiteralExp

def test_JTL_essentialocl_BooleanLiteralExp___init__():
    assert JTL_essentialocl_BooleanLiteralExp.__init__(JTL_essentialocl_BooleanLiteralExp(True), False) == None


from python_code import JTL_essentialocl_CollectionLiteralExp

def test_JTL_essentialocl_CollectionLiteralExp___init__():
    assert JTL_essentialocl_CollectionLiteralExp.__init__(JTL_essentialocl_CollectionLiteralExp('', CollectionLiteralExp=set()), '', CollectionLiteralExp=set()) == None


from python_code import JTL_essentialocl_IntegerLiteralExp

def test_JTL_essentialocl_IntegerLiteralExp___init__():
    assert JTL_essentialocl_IntegerLiteralExp.__init__(JTL_essentialocl_IntegerLiteralExp(0), 0) == None


from python_code import JTL_essentialocl_RealLiteralExp

def test_JTL_essentialocl_RealLiteralExp___init__():
    assert JTL_essentialocl_RealLiteralExp.__init__(JTL_essentialocl_RealLiteralExp(0.0), 0.0) == None


from python_code import JTL_essentialocl_StringLiteralExp

def test_JTL_essentialocl_StringLiteralExp___init__():
    assert JTL_essentialocl_StringLiteralExp.__init__(JTL_essentialocl_StringLiteralExp(''), '') == None


from python_code import JTL_essentialocl_UnlimitedNaturalExp

def test_JTL_essentialocl_UnlimitedNaturalExp___init__():
    assert JTL_essentialocl_UnlimitedNaturalExp.__init__(JTL_essentialocl_UnlimitedNaturalExp(''), '') == None


from python_code import JTL_imperativeocl_AssertExp
from python_code import LogExp
from python_code import OclExpression

def test_JTL_imperativeocl_AssertExp___init__():
    assert JTL_imperativeocl_AssertExp.__init__(JTL_imperativeocl_AssertExp('', JTL_imperativeocl_AssertExp=LogExp(), JTL_imperativeocl_AssertExp231=OclExpression()), '', JTL_imperativeocl_AssertExp=LogExp(), JTL_imperativeocl_AssertExp231=OclExpression()) == None


from python_code import JTL_imperativeocl_AssignExp
from python_code import OclExpression

def test_JTL_imperativeocl_AssignExp___init__():
    assert JTL_imperativeocl_AssignExp.__init__(JTL_imperativeocl_AssignExp(False, JTL_imperativeocl_AssignExp=set(), JTL_imperativeocl_AssignExp158=OclExpression(), JTL_imperativeocl_AssignExp161=OclExpression()), True, JTL_imperativeocl_AssignExp=set(), JTL_imperativeocl_AssignExp158=OclExpression(), JTL_imperativeocl_AssignExp161=OclExpression()) == None


from python_code import JTL_emof_Comment
from python_code import JTL_emof_Operation
from python_code import JTL_emof_Package
from python_code import JTL_essentialocl_CollectionType
from python_code import JTL_essentialocl_TypeExp
from python_code import JTL_imperativeocl_AnonymousTupleType
from python_code import JTL_imperativeocl_DictionaryType
from python_code import JTL_imperativeocl_RaiseExp
from python_code import JTL_imperativeocl_TemplateParameterType
from python_code import JTL_imperativeocl_TryExp
from python_code import JTL_imperativeocl_Typedef

def test_JTL_imperativeocl_TemplateParameterType___init__():
    assert JTL_imperativeocl_TemplateParameterType.__init__(JTL_imperativeocl_TemplateParameterType('', Type129=JTL_essentialocl_CollectionType(), Type200=JTL_imperativeocl_RaiseExp(), Type195=JTL_imperativeocl_TryExp(), Type204=JTL_imperativeocl_Typedef(), Type=JTL_emof_Operation(), Type90=JTL_essentialocl_TypeExp(), Type240=JTL_imperativeocl_AnonymousTupleType(), Type217=JTL_imperativeocl_DictionaryType(), Type13=JTL_emof_Package('', package=set(), JTL_emof_Package=set(), NamedElement=JTL_emof_Comment())), '', Type129=JTL_essentialocl_CollectionType(), Type200=JTL_imperativeocl_RaiseExp(), Type195=JTL_imperativeocl_TryExp(), Type204=JTL_imperativeocl_Typedef(), Type=JTL_emof_Operation(), Type90=JTL_essentialocl_TypeExp(), Type240=JTL_imperativeocl_AnonymousTupleType(), Type217=JTL_imperativeocl_DictionaryType(), Type13=JTL_emof_Package('', package=set(), JTL_emof_Package=set(), NamedElement=JTL_emof_Comment())) == None


from python_code import JTL_imperativeocl_VariableInitExp
from python_code import Variable

def test_JTL_imperativeocl_VariableInitExp___init__():
    assert JTL_imperativeocl_VariableInitExp.__init__(JTL_imperativeocl_VariableInitExp(True, JTL_imperativeocl_VariableInitExp=Variable()), False, JTL_imperativeocl_VariableInitExp=Variable()) == None


from python_code import CollectionType
from python_code import JTL_JTL_Pattern
from python_code import JTL_template_CollectionTemplateExp
from python_code import OclExpression

def test_JTL_template_CollectionTemplateExp___init__():
    assert JTL_template_CollectionTemplateExp.__init__(JTL_template_CollectionTemplateExp('', JTL_template_CollectionTemplateExp142=CollectionType(), JTL_template_CollectionTemplateExp144=OclExpression(), JTL_template_CollectionTemplateExp=set(), TemplateExp=JTL_JTL_Pattern()), '', JTL_template_CollectionTemplateExp142=CollectionType(), JTL_template_CollectionTemplateExp144=OclExpression(), JTL_template_CollectionTemplateExp=set(), TemplateExp=JTL_JTL_Pattern()) == None


from python_code import JTL_JTL_Pattern
from python_code import JTL_template_ObjectTemplateExp

def test_JTL_template_ObjectTemplateExp___init__():
    assert JTL_template_ObjectTemplateExp.__init__(JTL_template_ObjectTemplateExp('', objContainer=set(), JTL_template_ObjectTemplateExp=set(), TemplateExp=JTL_JTL_Pattern()), '', objContainer=set(), JTL_template_ObjectTemplateExp=set(), TemplateExp=JTL_JTL_Pattern()) == None

