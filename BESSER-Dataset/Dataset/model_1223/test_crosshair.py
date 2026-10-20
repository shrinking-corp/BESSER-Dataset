from python_code import ActualStructure
from python_code import SizeConstraint
from python_code import VariableType
from python_code import express_algorithms_ActualAGGREGATEType
from python_code import express_algorithms_ActualAggregationType

def test_express_algorithms_ActualAGGREGATEType___init__():
    assert express_algorithms_ActualAGGREGATEType.__init__(express_algorithms_ActualAGGREGATEType('', express_algorithms_ActualAGGREGATEType=SizeConstraint(), express_algorithms_ActualAGGREGATEType433=ActualStructure(), express_algorithms_ActualAGGREGATEType435=VariableType(), express_algorithms_ActualAGGREGATEType438=SizeConstraint(), ActualType=express_algorithms_ActualAggregationType()), '\x00', express_algorithms_ActualAGGREGATEType=SizeConstraint(), express_algorithms_ActualAGGREGATEType433=ActualStructure(), express_algorithms_ActualAGGREGATEType435=VariableType(), express_algorithms_ActualAGGREGATEType438=SizeConstraint(), ActualType=express_algorithms_ActualAggregationType()) == None


from python_code import ArrayBound
from python_code import express_algorithms_ActualARRAYType

def test_express_algorithms_ActualARRAYType___init__():
    assert express_algorithms_ActualARRAYType.__init__(express_algorithms_ActualARRAYType('', express_algorithms_ActualARRAYType=ArrayBound(), express_algorithms_ActualARRAYType428=ArrayBound()), '', express_algorithms_ActualARRAYType=ArrayBound(), express_algorithms_ActualARRAYType428=ArrayBound()) == None


from python_code import ActualDataType
from python_code import express_algorithms_ActualAggregationType
from python_code import express_algorithms_ActualGenericType

def test_express_algorithms_ActualGenericType___init__():
    assert express_algorithms_ActualGenericType.__init__(express_algorithms_ActualGenericType('', '\x00', express_algorithms_ActualGenericType=ActualDataType(), ActualType=express_algorithms_ActualAggregationType()), '\x00\x00', '', express_algorithms_ActualGenericType=ActualDataType(), ActualType=express_algorithms_ActualAggregationType()) == None


from python_code import AGGREGATEType
from python_code import ActualStructure
from python_code import express_algorithms_ActualStructureConstraint

def test_express_algorithms_ActualStructureConstraint___init__():
    assert express_algorithms_ActualStructureConstraint.__init__(express_algorithms_ActualStructureConstraint('', express_algorithms_ActualStructureConstraint=ActualStructure(), constraint449=AGGREGATEType()), '', express_algorithms_ActualStructureConstraint=ActualStructure(), constraint449=AGGREGATEType()) == None


from python_code import ActualDataType
from python_code import GenericType
from python_code import express_algorithms_ActualTypeConstraint

def test_express_algorithms_ActualTypeConstraint___init__():
    assert express_algorithms_ActualTypeConstraint.__init__(express_algorithms_ActualTypeConstraint('', constraint=GenericType(), express_algorithms_ActualTypeConstraint=ActualDataType()), '', constraint=GenericType(), express_algorithms_ActualTypeConstraint=ActualDataType()) == None


from python_code import ParameterType
from python_code import express_algorithms_Parameter
from python_code import express_core_LocalScope

def test_express_algorithms_Parameter___init__():
    assert express_algorithms_Parameter.__init__(express_algorithms_Parameter('', '', express_algorithms_Parameter=set(), express_algorithms_Parameter443=set(), express_algorithms_Parameter446=ParameterType(), LocalElement=express_core_LocalScope()), '', '', express_algorithms_Parameter=set(), express_algorithms_Parameter443=set(), express_algorithms_Parameter446=ParameterType(), LocalElement=express_core_LocalScope()) == None


from python_code import Algorithm
from python_code import RepeatStatement
from python_code import StatementBlock
from python_code import express_algorithms_Statement

def test_express_algorithms_Statement___init__():
    assert express_algorithms_Statement.__init__(express_algorithms_Statement('', body=RepeatStatement(), body420=Algorithm(), bodyStatements_Statement=StatementBlock(), express_algorithms_Statement=set(), express_algorithms_Statement417=set()), '', body=RepeatStatement(), body420=Algorithm(), bodyStatements_Statement=StatementBlock(), express_algorithms_Statement=set(), express_algorithms_Statement417=set()) == None


from python_code import ArrayBound
from python_code import express_core_ARRAYType

def test_express_core_ARRAYType___init__():
    assert express_core_ARRAYType.__init__(express_core_ARRAYType('', express_core_ARRAYType=ArrayBound(), express_core_ARRAYType403=ArrayBound()), '', express_core_ARRAYType=ArrayBound(), express_core_ARRAYType403=ArrayBound()) == None


from python_code import SizeConstraint
from python_code import express_core_AggregationType

def test_express_core_AggregationType___init__():
    assert express_core_AggregationType.__init__(express_core_AggregationType('', '\x00', express_core_AggregationType372=SizeConstraint(), express_core_AggregationType=SizeConstraint()), '\x00\x00', '', express_core_AggregationType372=SizeConstraint(), express_core_AggregationType=SizeConstraint()) == None


from python_code import AttributeType
from python_code import SingleEntityType
from python_code import express_core_Attribute

def test_express_core_Attribute___init__():
    assert express_core_Attribute.__init__(express_core_Attribute('\x00\x00', '', role=AttributeType(), declaresAttribute=SingleEntityType(), attributes=set()), '', '', role=AttributeType(), declaresAttribute=SingleEntityType(), attributes=set()) == None


from python_code import express_core_DomainRule

def test_express_core_DomainRule___init__():
    assert express_core_DomainRule.__init__(express_core_DomainRule(''), '') == None


from python_code import EnumerationType
from python_code import express_core_EnumerationType

def test_express_core_EnumerationType___init__():
    assert express_core_EnumerationType.__init__(express_core_EnumerationType('', express_core_EnumerationType=set(), declaredIn=set(), base=set(), extension209=EnumerationType()), '', express_core_EnumerationType=set(), declaredIn=set(), base=set(), extension209=EnumerationType()) == None


from python_code import DataType
from python_code import Instance
from python_code import Scope
from python_code import express_core_Expression

def test_express_core_Expression___init__():
    assert express_core_Expression.__init__(express_core_Expression('', express_core_Expression=Instance(), express_core_Expression198=Scope(), express_core_Expression200=DataType()), '', express_core_Expression=Instance(), express_core_Expression198=Scope(), express_core_Expression200=DataType()) == None


from python_code import ArrayBound
from python_code import express_core_GeneralARRAYType

def test_express_core_GeneralARRAYType___init__():
    assert express_core_GeneralARRAYType.__init__(express_core_GeneralARRAYType('', express_core_GeneralARRAYType=ArrayBound(), express_core_GeneralARRAYType351=ArrayBound()), '', express_core_GeneralARRAYType=ArrayBound(), express_core_GeneralARRAYType351=ArrayBound()) == None


from python_code import ActualTypeConstraint
from python_code import express_core_GeneralAggregationType
from python_code import express_core_GenericType
from python_code import express_core_ParameterType

def test_express_core_GenericType___init__():
    assert express_core_GenericType.__init__(express_core_GenericType('', matchingType=ActualTypeConstraint(), GeneralizedType=express_core_GeneralAggregationType(), GeneralizedType379=express_core_ParameterType()), '', matchingType=ActualTypeConstraint(), GeneralizedType=express_core_GeneralAggregationType(), GeneralizedType379=express_core_ParameterType()) == None


from python_code import Schema
from python_code import SchemaElement
from python_code import ScopedId
from python_code import express_core_InterfacedElement

def test_express_core_InterfacedElement___init__():
    assert express_core_InterfacedElement.__init__(express_core_InterfacedElement('', interfaces=Schema(), referencedAs=SchemaElement(), express_core_InterfacedElement=ScopedId()), '\x00', interfaces=Schema(), referencedAs=SchemaElement(), express_core_InterfacedElement=ScopedId()) == None


from python_code import express_core_AttributeType
from python_code import express_core_LengthConstraint

def test_express_core_LengthConstraint___init__():
    assert express_core_LengthConstraint.__init__(express_core_LengthConstraint('', '\x00', DomainConstraint=express_core_AttributeType()), '\x00\x00', '', DomainConstraint=express_core_AttributeType()) == None


from python_code import express_core_RealType

def test_express_core_RealType___init__():
    assert express_core_RealType.__init__(express_core_RealType(''), '') == None


from python_code import Attribute
from python_code import AttributeType
from python_code import EntityType
from python_code import Expression
from python_code import Redeclaration
from python_code import Role
from python_code import ScopedId
from python_code import SizeConstraint
from python_code import express_core_Redeclaration

def test_express_core_Redeclaration___init__():
    assert express_core_Redeclaration.__init__(express_core_Redeclaration('', '', express_core_Redeclaration223=SizeConstraint(), redeclarations=EntityType(), express_core_Redeclaration228=Attribute(), express_core_Redeclaration231=Role(), express_core_Redeclaration233=ScopedId(), express_core_Redeclaration=Expression(), express_core_Redeclaration216=AttributeType(), express_core_Redeclaration218=Redeclaration(), express_core_Redeclaration220=SizeConstraint()), '', '', express_core_Redeclaration223=SizeConstraint(), redeclarations=EntityType(), express_core_Redeclaration228=Attribute(), express_core_Redeclaration231=Role(), express_core_Redeclaration233=ScopedId(), express_core_Redeclaration=Expression(), express_core_Redeclaration216=AttributeType(), express_core_Redeclaration218=Redeclaration(), express_core_Redeclaration220=SizeConstraint()) == None


from python_code import Scope
from python_code import express_core_Remark

def test_express_core_Remark___init__():
    assert express_core_Remark.__init__(express_core_Remark('', '', '', documentation=set(), includesRemarks=Scope(), documentation338=set()), '', '', '\x00', documentation=set(), includesRemarks=Scope(), documentation338=set()) == None


from python_code import Scope
from python_code import express_core_ScopedId

def test_express_core_ScopedId___init__():
    assert express_core_ScopedId.__init__(express_core_ScopedId('', express_core_ScopedId=Scope()), '\x00', express_core_ScopedId=Scope()) == None


from python_code import SelectType
from python_code import express_core_SelectType

def test_express_core_SelectType___init__():
    assert express_core_SelectType.__init__(express_core_SelectType('', '', instantiates=set(), base383=set(), extension386=SelectType(), express_core_SelectType=set()), '', '', instantiates=set(), base383=set(), extension386=SelectType(), express_core_SelectType=set()) == None


from python_code import express_core_AnonymousType
from python_code import express_core_SimpleType

def test_express_core_SimpleType___init__():
    assert express_core_SimpleType.__init__(express_core_SimpleType('', AnonymousType=express_core_AnonymousType()), '', AnonymousType=express_core_AnonymousType()) == None


from python_code import express_core_AttributeType
from python_code import express_core_SizeConstraint

def test_express_core_SizeConstraint___init__():
    assert express_core_SizeConstraint.__init__(express_core_SizeConstraint('', DomainConstraint=express_core_AttributeType()), '', DomainConstraint=express_core_AttributeType()) == None


from python_code import EntityType
from python_code import express_core_UniqueRule

def test_express_core_UniqueRule___init__():
    assert express_core_UniqueRule.__init__(express_core_UniqueRule('', uniqueRules=EntityType(), express_core_UniqueRule=set()), '', uniqueRules=EntityType(), express_core_UniqueRule=set()) == None


from python_code import Attribute
from python_code import express_expressions_AttributeRef

def test_express_expressions_AttributeRef___init__():
    assert express_expressions_AttributeRef.__init__(express_expressions_AttributeRef('', express_expressions_AttributeRef=Attribute()), '', express_expressions_AttributeRef=Attribute()) == None

