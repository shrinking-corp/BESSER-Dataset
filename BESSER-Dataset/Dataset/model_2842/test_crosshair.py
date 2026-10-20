from python_code import alf_AcceptBlock
from python_code import alf_AcceptClause
from python_code import alf_AcceptStatement
from python_code import alf_QualifiedNameList

def test_alf_AcceptClause___init__():
    assert alf_AcceptClause.__init__(alf_AcceptClause('', alf_AcceptClause=alf_AcceptStatement(), alf_AcceptClause280=alf_AcceptBlock(), alf_AcceptClause285=alf_QualifiedNameList()), '', alf_AcceptClause=alf_AcceptStatement(), alf_AcceptClause280=alf_AcceptBlock(), alf_AcceptClause285=alf_QualifiedNameList()) == None


from python_code import alf_AnnotatedStatement
from python_code import alf_Annotation

def test_alf_Annotation___init__():
    assert alf_Annotation.__init__(alf_Annotation('', '\x00', alf_Annotation=alf_AnnotatedStatement()), '\x00\x00', '', alf_Annotation=alf_AnnotatedStatement()) == None


from python_code import alf_BOOLEAN_LITERAL

def test_alf_BOOLEAN_LITERAL___init__():
    assert alf_BOOLEAN_LITERAL.__init__(alf_BOOLEAN_LITERAL(''), '') == None


from python_code import alf_CollectOrIterateOperation

def test_alf_CollectOrIterateOperation___init__():
    assert alf_CollectOrIterateOperation.__init__(alf_CollectOrIterateOperation('', '', '', '', ''), '', '', '', '', '') == None


from python_code import alf_DocumentedStatement
from python_code import alf_NonEmptyStatementSequence
from python_code import alf_Statement
from python_code import alf_StatementSequence

def test_alf_DocumentedStatement___init__():
    assert alf_DocumentedStatement.__init__(alf_DocumentedStatement('', alf_DocumentedStatement243=alf_NonEmptyStatementSequence(), alf_DocumentedStatement=alf_StatementSequence(), alf_DocumentedStatement200=alf_Statement()), '', alf_DocumentedStatement243=alf_NonEmptyStatementSequence(), alf_DocumentedStatement=alf_StatementSequence(), alf_DocumentedStatement200=alf_Statement()) == None


from python_code import alf_AndExpression
from python_code import alf_EqualityExpression

def test_alf_EqualityExpression___init__():
    assert alf_EqualityExpression.__init__(alf_EqualityExpression('', alf_EqualityExpression=alf_AndExpression(), alf_EqualityExpression88=set()), '', alf_EqualityExpression=alf_AndExpression(), alf_EqualityExpression88=set()) == None


from python_code import alf_ForAllOrExistsOrOneOperation

def test_alf_ForAllOrExistsOrOneOperation___init__():
    assert alf_ForAllOrExistsOrOneOperation.__init__(alf_ForAllOrExistsOrOneOperation('', '', '', '', ''), '', '', '', '', '') == None


from python_code import alf_FormalParameter
from python_code import alf_FormalParameterList
from python_code import alf_TypePart

def test_alf_FormalParameter___init__():
    assert alf_FormalParameter.__init__(alf_FormalParameter('', '\x00', alf_FormalParameter=alf_FormalParameterList(), alf_FormalParameter16=alf_TypePart()), '\x00\x00', '', alf_FormalParameter=alf_FormalParameterList(), alf_FormalParameter16=alf_TypePart()) == None


from python_code import alf_InlineStatement

def test_alf_InlineStatement___init__():
    assert alf_InlineStatement.__init__(alf_InlineStatement('', '\x00'), '\x00\x00', '') == None


from python_code import alf_Expression
from python_code import alf_IsUniqueOperation

def test_alf_IsUniqueOperation___init__():
    assert alf_IsUniqueOperation.__init__(alf_IsUniqueOperation('', alf_IsUniqueOperation=alf_Expression()), '', alf_IsUniqueOperation=alf_Expression()) == None


from python_code import alf_LinkOperationExpression
from python_code import alf_LinkOperationTuple

def test_alf_LinkOperationExpression___init__():
    assert alf_LinkOperationExpression.__init__(alf_LinkOperationExpression('', alf_LinkOperationExpression=alf_LinkOperationTuple()), '', alf_LinkOperationExpression=alf_LinkOperationTuple()) == None


from python_code import alf_Expression
from python_code import alf_LinkOperationTuple
from python_code import alf_LinkOperationTupleElement
from python_code import alf_ValueSpecification

def test_alf_LinkOperationTupleElement___init__():
    assert alf_LinkOperationTupleElement.__init__(alf_LinkOperationTupleElement('', alf_LinkOperationTupleElement128=alf_Expression(), alf_LinkOperationTupleElement131=alf_ValueSpecification(), alf_LinkOperationTupleElement=alf_LinkOperationTuple()), '', alf_LinkOperationTupleElement128=alf_Expression(), alf_LinkOperationTupleElement131=alf_ValueSpecification(), alf_LinkOperationTupleElement=alf_LinkOperationTuple()) == None


from python_code import alf_Expression
from python_code import alf_ForControl
from python_code import alf_LoopVariableDefinition

def test_alf_LoopVariableDefinition___init__():
    assert alf_LoopVariableDefinition.__init__(alf_LoopVariableDefinition('', alf_LoopVariableDefinition=alf_ForControl(), alf_LoopVariableDefinition261=alf_Expression(), alf_LoopVariableDefinition264=alf_Expression()), '', alf_LoopVariableDefinition=alf_ForControl(), alf_LoopVariableDefinition261=alf_Expression(), alf_LoopVariableDefinition264=alf_Expression()) == None


from python_code import alf_Multiplicity
from python_code import alf_MultiplicityRange
from python_code import alf_TypePart

def test_alf_Multiplicity___init__():
    assert alf_Multiplicity.__init__(alf_Multiplicity(False, False, False, alf_Multiplicity=alf_TypePart(), alf_Multiplicity23=alf_MultiplicityRange()), False, False, False, alf_Multiplicity=alf_TypePart(), alf_Multiplicity23=alf_MultiplicityRange()) == None


from python_code import alf_NUMBER_LITERAL

def test_alf_NUMBER_LITERAL___init__():
    assert alf_NUMBER_LITERAL.__init__(alf_NUMBER_LITERAL(''), '') == None


from python_code import alf_MultiplicityRange
from python_code import alf_NUMBER_LITERAL_WITHOUT_SUFFIX

def test_alf_NUMBER_LITERAL_WITHOUT_SUFFIX___init__():
    assert alf_NUMBER_LITERAL_WITHOUT_SUFFIX.__init__(alf_NUMBER_LITERAL_WITHOUT_SUFFIX('', alf_NUMBER_LITERAL_WITHOUT_SUFFIX=alf_MultiplicityRange(), alf_NUMBER_LITERAL_WITHOUT_SUFFIX28=alf_MultiplicityRange()), '', alf_NUMBER_LITERAL_WITHOUT_SUFFIX=alf_MultiplicityRange(), alf_NUMBER_LITERAL_WITHOUT_SUFFIX28=alf_MultiplicityRange()) == None


from python_code import alf_FormalParameters
from python_code import alf_OperationDeclaration
from python_code import alf_OperationDefinitionOrStub
from python_code import alf_RedefinitionClause
from python_code import alf_TypePart

def test_alf_OperationDeclaration___init__():
    assert alf_OperationDeclaration.__init__(alf_OperationDeclaration('', alf_OperationDeclaration=alf_OperationDefinitionOrStub(), alf_OperationDeclaration6=alf_FormalParameters(), alf_OperationDeclaration8=alf_TypePart(), alf_OperationDeclaration10=alf_RedefinitionClause()), '', alf_OperationDeclaration=alf_OperationDefinitionOrStub(), alf_OperationDeclaration6=alf_FormalParameters(), alf_OperationDeclaration8=alf_TypePart(), alf_OperationDeclaration10=alf_RedefinitionClause()) == None


from python_code import alf_Operations

def test_alf_Operations___init__():
    assert alf_Operations.__init__(alf_Operations('', alf_Operations=set()), '', alf_Operations=set()) == None


from python_code import alf_Expression
from python_code import alf_PropertyCallExpression
from python_code import alf_SuffixExpression

def test_alf_PropertyCallExpression___init__():
    assert alf_PropertyCallExpression.__init__(alf_PropertyCallExpression('', alf_PropertyCallExpression=alf_Expression(), alf_PropertyCallExpression122=alf_SuffixExpression()), '', alf_PropertyCallExpression=alf_Expression(), alf_PropertyCallExpression122=alf_SuffixExpression()) == None


from python_code import alf_STRING_LITERAL

def test_alf_STRING_LITERAL___init__():
    assert alf_STRING_LITERAL.__init__(alf_STRING_LITERAL(''), '') == None


from python_code import alf_SelectOrRejectOperation

def test_alf_SelectOrRejectOperation___init__():
    assert alf_SelectOrRejectOperation.__init__(alf_SelectOrRejectOperation('', '', '', '', ''), '', '', '', '', '') == None


from python_code import alf_InstanceCreationExpression
from python_code import alf_SequenceConstructionCompletion
from python_code import alf_SequenceConstructionExpression

def test_alf_SequenceConstructionCompletion___init__():
    assert alf_SequenceConstructionCompletion.__init__(alf_SequenceConstructionCompletion(True, alf_SequenceConstructionCompletion=alf_InstanceCreationExpression(), alf_SequenceConstructionCompletion184=alf_SequenceConstructionExpression()), False, alf_SequenceConstructionCompletion=alf_InstanceCreationExpression(), alf_SequenceConstructionCompletion184=alf_SequenceConstructionExpression()) == None


from python_code import alf_SequenceOperationExpression
from python_code import alf_SuffixExpression
from python_code import alf_Tuple

def test_alf_SequenceOperationExpression___init__():
    assert alf_SequenceOperationExpression.__init__(alf_SequenceOperationExpression('', alf_SequenceOperationExpression=alf_Tuple(), alf_SequenceOperationExpression136=alf_SuffixExpression()), '', alf_SequenceOperationExpression=alf_Tuple(), alf_SequenceOperationExpression136=alf_SuffixExpression()) == None


from python_code import alf_QualifiedNamePath
from python_code import alf_TemplateBinding
from python_code import alf_UnqualifiedName

def test_alf_UnqualifiedName___init__():
    assert alf_UnqualifiedName.__init__(alf_UnqualifiedName('', alf_UnqualifiedName=alf_QualifiedNamePath(), alf_UnqualifiedName53=alf_TemplateBinding()), '', alf_UnqualifiedName=alf_QualifiedNamePath(), alf_UnqualifiedName53=alf_TemplateBinding()) == None

