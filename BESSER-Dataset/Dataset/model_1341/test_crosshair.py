from python_code import baseCST_AnnotationElementCS
from python_code import baseCST_DetailCS

def test_baseCST_DetailCS___init__():
    assert baseCST_DetailCS.__init__(baseCST_DetailCS('', baseCST_DetailCS=baseCST_AnnotationElementCS()), '', baseCST_DetailCS=baseCST_AnnotationElementCS()) == None


from python_code import baseCST_DocumentationCS

def test_baseCST_DocumentationCS___init__():
    assert baseCST_DocumentationCS.__init__(baseCST_DocumentationCS(''), '') == None


from python_code import baseCST_DataTypeCS
from python_code import baseCST_EnumerationCS
from python_code import baseCST_EnumerationLiteralCS

def test_baseCST_EnumerationLiteralCS___init__():
    assert baseCST_EnumerationLiteralCS.__init__(baseCST_EnumerationLiteralCS(0, baseCST_EnumerationLiteralCS21=baseCST_EnumerationCS(), baseCST_EnumerationLiteralCS=baseCST_DataTypeCS()), 0, baseCST_EnumerationLiteralCS21=baseCST_EnumerationCS(), baseCST_EnumerationLiteralCS=baseCST_DataTypeCS()) == None


from python_code import baseCST_LambdaTypeCS
from python_code import baseCST_TypedRefCS

def test_baseCST_LambdaTypeCS___init__():
    assert baseCST_LambdaTypeCS.__init__(baseCST_LambdaTypeCS('', baseCST_LambdaTypeCS=baseCST_TypedRefCS(), baseCST_LambdaTypeCS28=set(), baseCST_LambdaTypeCS31=baseCST_TypedRefCS()), '', baseCST_LambdaTypeCS=baseCST_TypedRefCS(), baseCST_LambdaTypeCS28=set(), baseCST_LambdaTypeCS31=baseCST_TypedRefCS()) == None


from python_code import baseCST_AnnotationCS
from python_code import baseCST_ModelElementCS

def test_baseCST_ModelElementCS___init__():
    assert baseCST_ModelElementCS.__init__(baseCST_ModelElementCS('\x00\x00', '', baseCST_ModelElementCS36=set(), baseCST_ModelElementCS=baseCST_AnnotationCS()), '', '', baseCST_ModelElementCS36=set(), baseCST_ModelElementCS=baseCST_AnnotationCS()) == None


from python_code import baseCST_MultiplicityBoundsCS

def test_baseCST_MultiplicityBoundsCS___init__():
    assert baseCST_MultiplicityBoundsCS.__init__(baseCST_MultiplicityBoundsCS(0, '\x00'), 0, '\x00') == None


from python_code import baseCST_MultiplicityCS
from python_code import baseCST_TypedRefCS

def test_baseCST_MultiplicityCS___init__():
    assert baseCST_MultiplicityCS.__init__(baseCST_MultiplicityCS(baseCST_MultiplicityCS=baseCST_TypedRefCS()), baseCST_MultiplicityCS=baseCST_TypedRefCS()) == None

def test_baseCST_MultiplicityCS_getUpper():
    assert baseCST_MultiplicityCS.getUpper(baseCST_MultiplicityCS(baseCST_MultiplicityCS=baseCST_TypedRefCS())) == None

def test_baseCST_MultiplicityCS_getLower():
    assert baseCST_MultiplicityCS.getLower(baseCST_MultiplicityCS(baseCST_MultiplicityCS=baseCST_TypedRefCS())) == None


from python_code import baseCST_MultiplicityStringCS

def test_baseCST_MultiplicityStringCS___init__():
    assert baseCST_MultiplicityStringCS.__init__(baseCST_MultiplicityStringCS(''), '') == None


from python_code import baseCST_NamedElementCS

def test_baseCST_NamedElementCS___init__():
    assert baseCST_NamedElementCS.__init__(baseCST_NamedElementCS(''), '') == None


from python_code import baseCST_PathElementWithURICS

def test_baseCST_PathElementWithURICS___init__():
    assert baseCST_PathElementWithURICS.__init__(baseCST_PathElementWithURICS(''), '') == None


from python_code import baseCST_PrimitiveTypeRefCS

def test_baseCST_PrimitiveTypeRefCS___init__():
    assert baseCST_PrimitiveTypeRefCS.__init__(baseCST_PrimitiveTypeRefCS(''), '') == None


from python_code import baseCST_TupleTypeCS

def test_baseCST_TupleTypeCS___init__():
    assert baseCST_TupleTypeCS.__init__(baseCST_TupleTypeCS('', baseCST_TupleTypeCS=set()), '', baseCST_TupleTypeCS=set()) == None


from python_code import baseCST_TypedElementCS
from python_code import baseCST_TypedRefCS

def test_baseCST_TypedElementCS___init__():
    assert baseCST_TypedElementCS.__init__(baseCST_TypedElementCS('', False, baseCST_TypedElementCS=baseCST_TypedRefCS()), '', False, baseCST_TypedElementCS=baseCST_TypedRefCS()) == None

