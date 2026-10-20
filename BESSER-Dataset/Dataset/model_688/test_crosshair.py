from python_code import Janus_JTL_Domain
from python_code import Janus_emof_Comment
from python_code import Model
from python_code import Pattern
from python_code import Relation
from python_code import Variable

def test_Janus_JTL_Domain___init__():
    assert Janus_JTL_Domain.__init__(Janus_JTL_Domain(False, False, domain=Relation(), Janus_JTL_Domain=Pattern(), Janus_JTL_Domain42=Model(), Janus_JTL_Domain45=Variable(), NamedElement=Janus_emof_Comment()), False, False, domain=Relation(), Janus_JTL_Domain=Pattern(), Janus_JTL_Domain42=Model(), Janus_JTL_Domain45=Variable(), NamedElement=Janus_emof_Comment()) == None


from python_code import Janus_JTL_Relation
from python_code import Janus_emof_Comment
from python_code import Pattern
from python_code import Transformation

def test_Janus_JTL_Relation___init__():
    assert Janus_JTL_Relation.__init__(Janus_JTL_Relation(False, relation32=set(), whereOwner=Pattern(), whenOwner=Pattern(), Janus_JTL_Relation=set(), relation=Transformation(), NamedElement=Janus_emof_Comment()), False, relation32=set(), whereOwner=Pattern(), whenOwner=Pattern(), Janus_JTL_Relation=set(), relation=Transformation(), NamedElement=Janus_emof_Comment()) == None


from python_code import Janus_emof_Class
from python_code import Janus_emof_Comment
from python_code import Janus_emof_Operation
from python_code import Janus_emof_Package
from python_code import Janus_emof_TypedElement
from python_code import Janus_essentialocl_CollectionType
from python_code import Janus_essentialocl_TypeExp
from python_code import Janus_imperativeocl_AnonymousTupleType
from python_code import Janus_imperativeocl_DictionaryType
from python_code import Janus_imperativeocl_RaiseExp
from python_code import Janus_imperativeocl_TryExp
from python_code import Janus_imperativeocl_Typedef

def test_Janus_emof_Class___init__():
    assert Janus_emof_Class.__init__(Janus_emof_Class(False, Class=set(), class_=set(), Janus_emof_Class=set(), Type203=Janus_imperativeocl_TryExp(), Type97=Janus_essentialocl_TypeExp(), Type13=Janus_emof_Package('', package=set(), Janus_emof_Package=set(), NamedElement=Janus_emof_Comment()), Type138=Janus_essentialocl_CollectionType(), Type25=Janus_emof_TypedElement(), Type248=Janus_imperativeocl_AnonymousTupleType(), Type208=Janus_imperativeocl_RaiseExp(), Type=Janus_emof_Operation(), Type225=Janus_imperativeocl_DictionaryType(), Type212=Janus_imperativeocl_Typedef()), False, Class=set(), class_=set(), Janus_emof_Class=set(), Type203=Janus_imperativeocl_TryExp(), Type97=Janus_essentialocl_TypeExp(), Type13=Janus_emof_Package('', package=set(), Janus_emof_Package=set(), NamedElement=Janus_emof_Comment()), Type138=Janus_essentialocl_CollectionType(), Type25=Janus_emof_TypedElement(), Type248=Janus_imperativeocl_AnonymousTupleType(), Type208=Janus_imperativeocl_RaiseExp(), Type=Janus_emof_Operation(), Type225=Janus_imperativeocl_DictionaryType(), Type212=Janus_imperativeocl_Typedef()) == None


from python_code import Janus_emof_MultiplicityElement

def test_Janus_emof_MultiplicityElement___init__():
    assert Janus_emof_MultiplicityElement.__init__(Janus_emof_MultiplicityElement('\x00\x00', '', 0, ''), '', '', 0, '') == None


from python_code import Janus_emof_Comment
from python_code import Janus_emof_Package

def test_Janus_emof_Package___init__():
    assert Janus_emof_Package.__init__(Janus_emof_Package('', package=set(), Janus_emof_Package=set(), NamedElement=Janus_emof_Comment()), '', package=set(), Janus_emof_Package=set(), NamedElement=Janus_emof_Comment()) == None


from python_code import Class
from python_code import Janus_emof_Property
from python_code import Property

def test_Janus_emof_Property___init__():
    assert Janus_emof_Property.__init__(Janus_emof_Property(False, False, True, False, '', ownedAttribute=Class(), Janus_emof_Property=Property()), True, False, False, False, '', ownedAttribute=Class(), Janus_emof_Property=Property()) == None


from python_code import Janus_essentialocl_BooleanLiteralExp

def test_Janus_essentialocl_BooleanLiteralExp___init__():
    assert Janus_essentialocl_BooleanLiteralExp.__init__(Janus_essentialocl_BooleanLiteralExp(True), False) == None


from python_code import Janus_essentialocl_CollectionLiteralExp

def test_Janus_essentialocl_CollectionLiteralExp___init__():
    assert Janus_essentialocl_CollectionLiteralExp.__init__(Janus_essentialocl_CollectionLiteralExp('', CollectionLiteralExp=set()), '', CollectionLiteralExp=set()) == None


from python_code import Janus_essentialocl_IntegerLiteralExp

def test_Janus_essentialocl_IntegerLiteralExp___init__():
    assert Janus_essentialocl_IntegerLiteralExp.__init__(Janus_essentialocl_IntegerLiteralExp(0), 0) == None


from python_code import Janus_essentialocl_RealLiteralExp

def test_Janus_essentialocl_RealLiteralExp___init__():
    assert Janus_essentialocl_RealLiteralExp.__init__(Janus_essentialocl_RealLiteralExp(0.0), 0.0) == None


from python_code import Janus_essentialocl_StringLiteralExp

def test_Janus_essentialocl_StringLiteralExp___init__():
    assert Janus_essentialocl_StringLiteralExp.__init__(Janus_essentialocl_StringLiteralExp(''), '') == None


from python_code import Janus_essentialocl_UnlimitedNaturalExp

def test_Janus_essentialocl_UnlimitedNaturalExp___init__():
    assert Janus_essentialocl_UnlimitedNaturalExp.__init__(Janus_essentialocl_UnlimitedNaturalExp(''), '') == None


from python_code import Janus_imperativeocl_AssertExp
from python_code import LogExp
from python_code import OclExpression

def test_Janus_imperativeocl_AssertExp___init__():
    assert Janus_imperativeocl_AssertExp.__init__(Janus_imperativeocl_AssertExp('', Janus_imperativeocl_AssertExp=LogExp(), Janus_imperativeocl_AssertExp239=OclExpression()), '', Janus_imperativeocl_AssertExp=LogExp(), Janus_imperativeocl_AssertExp239=OclExpression()) == None


from python_code import Janus_imperativeocl_AssignExp
from python_code import OclExpression

def test_Janus_imperativeocl_AssignExp___init__():
    assert Janus_imperativeocl_AssignExp.__init__(Janus_imperativeocl_AssignExp(False, Janus_imperativeocl_AssignExp=set(), Janus_imperativeocl_AssignExp166=OclExpression(), Janus_imperativeocl_AssignExp169=OclExpression()), True, Janus_imperativeocl_AssignExp=set(), Janus_imperativeocl_AssignExp166=OclExpression(), Janus_imperativeocl_AssignExp169=OclExpression()) == None


from python_code import Janus_emof_Comment
from python_code import Janus_emof_Operation
from python_code import Janus_emof_Package
from python_code import Janus_emof_TypedElement
from python_code import Janus_essentialocl_CollectionType
from python_code import Janus_essentialocl_TypeExp
from python_code import Janus_imperativeocl_AnonymousTupleType
from python_code import Janus_imperativeocl_DictionaryType
from python_code import Janus_imperativeocl_RaiseExp
from python_code import Janus_imperativeocl_TemplateParameterType
from python_code import Janus_imperativeocl_TryExp
from python_code import Janus_imperativeocl_Typedef

def test_Janus_imperativeocl_TemplateParameterType___init__():
    assert Janus_imperativeocl_TemplateParameterType.__init__(Janus_imperativeocl_TemplateParameterType('', Type203=Janus_imperativeocl_TryExp(), Type97=Janus_essentialocl_TypeExp(), Type13=Janus_emof_Package('', package=set(), Janus_emof_Package=set(), NamedElement=Janus_emof_Comment()), Type138=Janus_essentialocl_CollectionType(), Type25=Janus_emof_TypedElement(), Type248=Janus_imperativeocl_AnonymousTupleType(), Type208=Janus_imperativeocl_RaiseExp(), Type=Janus_emof_Operation(), Type225=Janus_imperativeocl_DictionaryType(), Type212=Janus_imperativeocl_Typedef()), '', Type203=Janus_imperativeocl_TryExp(), Type97=Janus_essentialocl_TypeExp(), Type13=Janus_emof_Package('', package=set(), Janus_emof_Package=set(), NamedElement=Janus_emof_Comment()), Type138=Janus_essentialocl_CollectionType(), Type25=Janus_emof_TypedElement(), Type248=Janus_imperativeocl_AnonymousTupleType(), Type208=Janus_imperativeocl_RaiseExp(), Type=Janus_emof_Operation(), Type225=Janus_imperativeocl_DictionaryType(), Type212=Janus_imperativeocl_Typedef()) == None


from python_code import Janus_imperativeocl_VariableInitExp
from python_code import Variable

def test_Janus_imperativeocl_VariableInitExp___init__():
    assert Janus_imperativeocl_VariableInitExp.__init__(Janus_imperativeocl_VariableInitExp(True, Janus_imperativeocl_VariableInitExp=Variable()), False, Janus_imperativeocl_VariableInitExp=Variable()) == None


from python_code import CollectionType
from python_code import Janus_JTL_Pattern
from python_code import Janus_template_CollectionTemplateExp
from python_code import OclExpression

def test_Janus_template_CollectionTemplateExp___init__():
    assert Janus_template_CollectionTemplateExp.__init__(Janus_template_CollectionTemplateExp('', Janus_template_CollectionTemplateExp=set(), Janus_template_CollectionTemplateExp150=CollectionType(), Janus_template_CollectionTemplateExp152=OclExpression(), TemplateExp=Janus_JTL_Pattern()), '', Janus_template_CollectionTemplateExp=set(), Janus_template_CollectionTemplateExp150=CollectionType(), Janus_template_CollectionTemplateExp152=OclExpression(), TemplateExp=Janus_JTL_Pattern()) == None


from python_code import Janus_JTL_Pattern
from python_code import Janus_template_ObjectTemplateExp

def test_Janus_template_ObjectTemplateExp___init__():
    assert Janus_template_ObjectTemplateExp.__init__(Janus_template_ObjectTemplateExp('', objContainer=set(), TemplateExp=Janus_JTL_Pattern()), '', objContainer=set(), TemplateExp=Janus_JTL_Pattern()) == None

