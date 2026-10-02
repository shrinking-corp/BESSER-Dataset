from enum import Enum
from python_code import AuthenticationFlows
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AuthenticationFlows.PASSWORD, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AuthenticationFlows.PASSWORD, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AuthenticationFlows.PASSWORD, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AuthenticationFlows.IMPLICIT, 0)

def test_Enum___new___2():
    assert Enum.__new__(AuthenticationFlows.PASSWORD, 'PASSWORD') == AuthenticationFlows.PASSWORD

from enum import Enum
from python_code import AuthenticationTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AuthenticationTypes.BASIC, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AuthenticationTypes.BASIC, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AuthenticationTypes.BASIC, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AuthenticationTypes.BASIC, 0)

def test_Enum___new___2():
    assert Enum.__new__(AuthenticationTypes.BASIC, 'BASIC') == AuthenticationTypes.BASIC

from enum import Enum
from python_code import CollectionRealizationEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CollectionRealizationEnum.REFERENCE_LINK_LIST, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CollectionRealizationEnum.REFERENCE_LINK_LIST, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CollectionRealizationEnum.EMBEDDED_OBJECT_LIST, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CollectionRealizationEnum.REFERENCE_LINK_LIST, 0)

def test_Enum___new___2():
    assert Enum.__new__(CollectionRealizationEnum.REFERENCE_LINK_LIST, 'REFERENCE_LINK_LIST') == CollectionRealizationEnum.REFERENCE_LINK_LIST

from enum import Enum
from python_code import CollectionRealizationLevelEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CollectionRealizationLevelEnum.ITEM_LEVEL, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CollectionRealizationLevelEnum.ITEM_LEVEL, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CollectionRealizationLevelEnum.ITEM_LEVEL, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CollectionRealizationLevelEnum.ITEM_LEVEL, 0)

def test_Enum___new___2():
    assert Enum.__new__(CollectionRealizationLevelEnum.ITEM_LEVEL, 'ITEM_LEVEL') == CollectionRealizationLevelEnum.ITEM_LEVEL

from enum import Enum
from python_code import HTTPMethods
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(HTTPMethods.GET, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(HTTPMethods.GET, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(HTTPMethods.PUT, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(HTTPMethods.GET, 0)

def test_Enum___new___2():
    assert Enum.__new__(HTTPMethods.PUT, 'PUT') == HTTPMethods.PUT

from enum import Enum
from python_code import HttpMessageParameterLocation
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(HttpMessageParameterLocation.NONE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(HttpMessageParameterLocation.NONE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(HttpMessageParameterLocation.NONE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(HttpMessageParameterLocation.NONE, 0)

def test_Enum___new___2():
    assert Enum.__new__(HttpMessageParameterLocation.NONE, 'NONE') == HttpMessageParameterLocation.NONE

from enum import Enum
from python_code import ReferenceRealizationEnum
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ReferenceRealizationEnum.LINK, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ReferenceRealizationEnum.LINK, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ReferenceRealizationEnum.EMBED, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ReferenceRealizationEnum.LINK, 0)

def test_Enum___new___2():
    assert Enum.__new__(ReferenceRealizationEnum.LINK, 'LINK') == ReferenceRealizationEnum.LINK

from python_code import rapidml_CollectionParameter
from python_code import rapidml_CollectionResource

def test_rapidml_CollectionResource___init__():
    assert rapidml_CollectionResource.__init__(rapidml_CollectionResource('', rapidml_CollectionResource=set(), CollectionResource=rapidml_CollectionParameter(), containingResourceDefinition29=set()), '', rapidml_CollectionResource=set(), CollectionResource=rapidml_CollectionParameter(), containingResourceDefinition29=set()) == None

from python_code import rapidml_ConstrainableType

def test_rapidml_ConstrainableType___init__():
    assert rapidml_ConstrainableType.__init__(rapidml_ConstrainableType(rapidml_ConstrainableType=set()), rapidml_ConstrainableType=set()) == None

def test_rapidml_ConstrainableType_getAllConstraints():
    assert rapidml_ConstrainableType.getAllConstraints(rapidml_ConstrainableType(rapidml_ConstrainableType=set())) == None

def test_rapidml_ConstrainableType_getConstrainableParent():
    assert rapidml_ConstrainableType.getConstrainableParent(rapidml_ConstrainableType(rapidml_ConstrainableType=set())) == None

from python_code import rapidml_Documentable
from python_code import rapidml_Documentation

def test_rapidml_Documentation___init__():
    assert rapidml_Documentation.__init__(rapidml_Documentation('', rapidml_Documentation=rapidml_Documentable()), '', rapidml_Documentation=rapidml_Documentable()) == None

from python_code import rapidml_Element

def test_rapidml_Element___init__():
    assert rapidml_Element.__init__(rapidml_Element(''), '') == None

def test_rapidml_Element_getMaxOccurs():
    assert rapidml_Element.getMaxOccurs(rapidml_Element('')) == None

def test_rapidml_Element_getDataType():
    assert rapidml_Element.getDataType(rapidml_Element('')) == None

def test_rapidml_Element_getMinOccurs():
    assert rapidml_Element.getMinOccurs(rapidml_Element('')) == None

def test_rapidml_Element_isMultiValued():
    assert rapidml_Element.isMultiValued(rapidml_Element('')) == None

from python_code import rapidml_Example
from python_code import rapidml_WithExamples

def test_rapidml_Example___init__():
    assert rapidml_Example.__init__(rapidml_Example(rapidml_Example=rapidml_WithExamples()), rapidml_Example=rapidml_WithExamples()) == None

def test_rapidml_Example_getBody():
    assert rapidml_Example.getBody(rapidml_Example(rapidml_Example=rapidml_WithExamples())) == None

from python_code import rapidml_Extensible
from python_code import rapidml_Extension

def test_rapidml_Extension___init__():
    assert rapidml_Extension.__init__(rapidml_Extension('', '\x00', rapidml_Extension=rapidml_Extensible()), '\x00\x00', '', rapidml_Extension=rapidml_Extensible()) == None

from python_code import rapidml_ExternalExample

def test_rapidml_ExternalExample___init__():
    assert rapidml_ExternalExample.__init__(rapidml_ExternalExample(''), '') == None

def test_rapidml_ExternalExample_getBody():
    assert rapidml_ExternalExample.getBody(rapidml_ExternalExample('')) == None

from python_code import rapidml_HasStringValue

def test_rapidml_HasStringValue___init__():
    assert rapidml_HasStringValue.__init__(rapidml_HasStringValue()) == None

def test_rapidml_HasStringValue_toString():
    assert rapidml_HasStringValue.toString(rapidml_HasStringValue()) == None

from python_code import rapidml_HasTitle

def test_rapidml_HasTitle___init__():
    assert rapidml_HasTitle.__init__(rapidml_HasTitle(''), '') == None

from python_code import rapidml_InlineDataExample

def test_rapidml_InlineDataExample___init__():
    assert rapidml_InlineDataExample.__init__(rapidml_InlineDataExample(''), '') == None

from python_code import rapidml_InlineExample

def test_rapidml_InlineExample___init__():
    assert rapidml_InlineExample.__init__(rapidml_InlineExample(''), '') == None

from python_code import rapidml_LengthConstraint

def test_rapidml_LengthConstraint___init__():
    assert rapidml_LengthConstraint.__init__(rapidml_LengthConstraint(0, 0, 0), 0, 0, 0) == None

from python_code import rapidml_ReferenceEmbed

def test_rapidml_ReferenceEmbed___init__():
    assert rapidml_ReferenceEmbed.__init__(rapidml_ReferenceEmbed()) == None

def test_rapidml_ReferenceEmbed_getNestedReferenceTreatments():
    assert rapidml_ReferenceEmbed.getNestedReferenceTreatments(rapidml_ReferenceEmbed()) == None

def test_rapidml_ReferenceEmbed_getAllNestedReferenceTreatments():
    assert rapidml_ReferenceEmbed.getAllNestedReferenceTreatments(rapidml_ReferenceEmbed()) == None

from python_code import rapidml_RegExConstraint

def test_rapidml_RegExConstraint___init__():
    assert rapidml_RegExConstraint.__init__(rapidml_RegExConstraint(''), '') == None

from python_code import rapidml_URI
from python_code import rapidml_URIParameter
from python_code import rapidml_URISegmentWithParameter

def test_rapidml_URIParameter___init__():
    assert rapidml_URIParameter.__init__(rapidml_URIParameter(rapidml_URIParameter=rapidml_URISegmentWithParameter(), uriParameters=rapidml_URI(), URIParameter=rapidml_URI()), rapidml_URIParameter=rapidml_URISegmentWithParameter(), uriParameters=rapidml_URI(), URIParameter=rapidml_URI()) == None

def test_rapidml_URIParameter_getName():
    assert rapidml_URIParameter.getName(rapidml_URIParameter(rapidml_URIParameter=rapidml_URISegmentWithParameter(), uriParameters=rapidml_URI(), URIParameter=rapidml_URI())) == None

from python_code import rapidml_URI
from python_code import rapidml_URISegment

def test_rapidml_URISegment___init__():
    assert rapidml_URISegment.__init__(rapidml_URISegment('', rapidml_URISegment=rapidml_URI()), '', rapidml_URISegment=rapidml_URI()) == None

from python_code import rapidml_SimpleType
from python_code import rapidml_UserDefinedType

def test_rapidml_UserDefinedType___init__():
    assert rapidml_UserDefinedType.__init__(rapidml_UserDefinedType(rapidml_UserDefinedType=rapidml_SimpleType()), rapidml_UserDefinedType=rapidml_SimpleType()) == None

def test_rapidml_UserDefinedType_getPrimitiveType():
    assert rapidml_UserDefinedType.getPrimitiveType(rapidml_UserDefinedType(rapidml_UserDefinedType=rapidml_SimpleType())) == None

from python_code import rapidml_ValueRangeConstraint

def test_rapidml_ValueRangeConstraint___init__():
    assert rapidml_ValueRangeConstraint.__init__(rapidml_ValueRangeConstraint('\x00\x00', False, '', True), '', False, '', False) == None
