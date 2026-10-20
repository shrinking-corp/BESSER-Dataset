from python_code import alf_AcceptBlock
from python_code import alf_AcceptClause
from python_code import alf_AcceptStatement
from python_code import alf_QualifiedNameList

def test_alf_AcceptClause___init__():
    assert alf_AcceptClause.__init__(alf_AcceptClause('', alf_AcceptClause=alf_AcceptStatement(), alf_AcceptClause247=alf_AcceptBlock(), alf_AcceptClause252=alf_QualifiedNameList()), '', alf_AcceptClause=alf_AcceptStatement(), alf_AcceptClause247=alf_AcceptBlock(), alf_AcceptClause252=alf_QualifiedNameList()) == None


from python_code import alf_AnnotatedStatement
from python_code import alf_Annotation

def test_alf_Annotation___init__():
    assert alf_Annotation.__init__(alf_Annotation('', '\x00', alf_Annotation=alf_AnnotatedStatement()), '\x00\x00', '', alf_Annotation=alf_AnnotatedStatement()) == None


from python_code import alf_BOOLEAN_LITERAL

def test_alf_BOOLEAN_LITERAL___init__():
    assert alf_BOOLEAN_LITERAL.__init__(alf_BOOLEAN_LITERAL(''), '') == None


from python_code import alf_CollectOrIterateOperation

def test_alf_CollectOrIterateOperation___init__():
    assert alf_CollectOrIterateOperation.__init__(alf_CollectOrIterateOperation(''), '') == None


from python_code import alf_DocumentedStatement
from python_code import alf_NonEmptyStatementSequence
from python_code import alf_Statement
from python_code import alf_StatementSequence

def test_alf_DocumentedStatement___init__():
    assert alf_DocumentedStatement.__init__(alf_DocumentedStatement('', alf_DocumentedStatement=alf_StatementSequence(), alf_DocumentedStatement157=alf_Statement(), alf_DocumentedStatement204=alf_NonEmptyStatementSequence()), '', alf_DocumentedStatement=alf_StatementSequence(), alf_DocumentedStatement157=alf_Statement(), alf_DocumentedStatement204=alf_NonEmptyStatementSequence()) == None


from python_code import alf_AndExpression
from python_code import alf_EqualityExpression

def test_alf_EqualityExpression___init__():
    assert alf_EqualityExpression.__init__(alf_EqualityExpression('', alf_EqualityExpression=alf_AndExpression(), alf_EqualityExpression51=set()), '', alf_EqualityExpression=alf_AndExpression(), alf_EqualityExpression51=set()) == None


from python_code import alf_ForAllOrExistsOrOneOperation

def test_alf_ForAllOrExistsOrOneOperation___init__():
    assert alf_ForAllOrExistsOrOneOperation.__init__(alf_ForAllOrExistsOrOneOperation(''), '') == None


from python_code import alf_InlineStatement

def test_alf_InlineStatement___init__():
    assert alf_InlineStatement.__init__(alf_InlineStatement('', '\x00'), '\x00\x00', '') == None


from python_code import alf_Expression
from python_code import alf_InstanceCreationTuple
from python_code import alf_InstanceCreationTupleElement

def test_alf_InstanceCreationTupleElement___init__():
    assert alf_InstanceCreationTupleElement.__init__(alf_InstanceCreationTupleElement('', alf_InstanceCreationTupleElement=alf_InstanceCreationTuple(), alf_InstanceCreationTupleElement133=alf_Expression()), '', alf_InstanceCreationTupleElement=alf_InstanceCreationTuple(), alf_InstanceCreationTupleElement133=alf_Expression()) == None


from python_code import alf_LinkOperationExpression
from python_code import alf_LinkOperationTuple

def test_alf_LinkOperationExpression___init__():
    assert alf_LinkOperationExpression.__init__(alf_LinkOperationExpression('', alf_LinkOperationExpression=alf_LinkOperationTuple()), '', alf_LinkOperationExpression=alf_LinkOperationTuple()) == None


from python_code import alf_Expression
from python_code import alf_LinkOperationTuple
from python_code import alf_LinkOperationTupleElement

def test_alf_LinkOperationTupleElement___init__():
    assert alf_LinkOperationTupleElement.__init__(alf_LinkOperationTupleElement('', alf_LinkOperationTupleElement=alf_LinkOperationTuple(), alf_LinkOperationTupleElement86=alf_Expression(), alf_LinkOperationTupleElement89=alf_Expression()), '', alf_LinkOperationTupleElement=alf_LinkOperationTuple(), alf_LinkOperationTupleElement86=alf_Expression(), alf_LinkOperationTupleElement89=alf_Expression()) == None


from python_code import alf_NUMBER_LITERAL

def test_alf_NUMBER_LITERAL___init__():
    assert alf_NUMBER_LITERAL.__init__(alf_NUMBER_LITERAL(''), '') == None


from python_code import alf_OperationCallExpression
from python_code import alf_SuffixExpression
from python_code import alf_Tuple

def test_alf_OperationCallExpression___init__():
    assert alf_OperationCallExpression.__init__(alf_OperationCallExpression('', alf_OperationCallExpression=alf_Tuple(), alf_OperationCallExpression75=alf_SuffixExpression()), '', alf_OperationCallExpression=alf_Tuple(), alf_OperationCallExpression75=alf_SuffixExpression()) == None


from python_code import alf_Expression
from python_code import alf_PropertyCallExpression
from python_code import alf_SuffixExpression

def test_alf_PropertyCallExpression___init__():
    assert alf_PropertyCallExpression.__init__(alf_PropertyCallExpression('', alf_PropertyCallExpression=alf_Expression(), alf_PropertyCallExpression80=alf_SuffixExpression()), '', alf_PropertyCallExpression=alf_Expression(), alf_PropertyCallExpression80=alf_SuffixExpression()) == None


from python_code import alf_STRING_LITERAL

def test_alf_STRING_LITERAL___init__():
    assert alf_STRING_LITERAL.__init__(alf_STRING_LITERAL(''), '') == None


from python_code import alf_SelectOrRejectOperation

def test_alf_SelectOrRejectOperation___init__():
    assert alf_SelectOrRejectOperation.__init__(alf_SelectOrRejectOperation(''), '') == None


from python_code import alf_Expression
from python_code import alf_SequenceExpansionExpression
from python_code import alf_SuffixExpression

def test_alf_SequenceExpansionExpression___init__():
    assert alf_SequenceExpansionExpression.__init__(alf_SequenceExpansionExpression('', alf_SequenceExpansionExpression=alf_Expression(), alf_SequenceExpansionExpression107=alf_SuffixExpression()), '', alf_SequenceExpansionExpression=alf_Expression(), alf_SequenceExpansionExpression107=alf_SuffixExpression()) == None


from python_code import alf_QualifiedNamePath
from python_code import alf_TemplateBinding
from python_code import alf_UnqualifiedName

def test_alf_UnqualifiedName___init__():
    assert alf_UnqualifiedName.__init__(alf_UnqualifiedName('', alf_UnqualifiedName=alf_QualifiedNamePath(), alf_UnqualifiedName17=alf_TemplateBinding()), '', alf_UnqualifiedName=alf_QualifiedNamePath(), alf_UnqualifiedName17=alf_TemplateBinding()) == None

