from python_code import langc_BuiltInType

def test_langc_BuiltInType___init__():
    assert langc_BuiltInType.__init__(langc_BuiltInType(''), '') == None


from python_code import langc_CharacterLiteral

def test_langc_CharacterLiteral___init__():
    assert langc_CharacterLiteral.__init__(langc_CharacterLiteral(''), '') == None


from python_code import langc_CodeBlock
from python_code import langc_FunctionImplementation

def test_langc_CodeBlock___init__():
    assert langc_CodeBlock.__init__(langc_CodeBlock(False, langc_CodeBlock=set(), langc_CodeBlock136=langc_FunctionImplementation()), False, langc_CodeBlock=set(), langc_CodeBlock136=langc_FunctionImplementation()) == None


from python_code import langc_ExpressionBlob

def test_langc_ExpressionBlob___init__():
    assert langc_ExpressionBlob.__init__(langc_ExpressionBlob(''), '') == None


from python_code import langc_FloatingLiteral

def test_langc_FloatingLiteral___init__():
    assert langc_FloatingLiteral.__init__(langc_FloatingLiteral(0.0), 0.0) == None


from python_code import langc_Enumerator
from python_code import langc_IntegralLiteral

def test_langc_IntegralLiteral___init__():
    assert langc_IntegralLiteral.__init__(langc_IntegralLiteral('', '', False, langc_IntegralLiteral=langc_Enumerator()), '\x00', '', False, langc_IntegralLiteral=langc_Enumerator()) == None


from python_code import langc_LinkableArtifact
from python_code import langc_System

def test_langc_LinkableArtifact___init__():
    assert langc_LinkableArtifact.__init__(langc_LinkableArtifact('', langc_LinkableArtifact=langc_System(), langc_LinkableArtifact149=set(), langc_LinkableArtifact152=set()), '', langc_LinkableArtifact=langc_System(), langc_LinkableArtifact149=set(), langc_LinkableArtifact152=set()) == None


from python_code import langc_Literal

def test_langc_Literal___init__():
    assert langc_Literal.__init__(langc_Literal(''), '') == None


from python_code import langc_StringLiteral

def test_langc_StringLiteral___init__():
    assert langc_StringLiteral.__init__(langc_StringLiteral(''), '') == None


from python_code import langc_SubSystem
from python_code import langc_System

def test_langc_SubSystem___init__():
    assert langc_SubSystem.__init__(langc_SubSystem('', langc_SubSystem=set(), langc_SubSystem74=set(), langc_SubSystem76=set(), langc_SubSystem141=langc_System()), '', langc_SubSystem=set(), langc_SubSystem74=set(), langc_SubSystem76=set(), langc_SubSystem141=langc_System()) == None


from python_code import langc_SwitchClause
from python_code import langc_SwitchStatement

def test_langc_SwitchClause___init__():
    assert langc_SwitchClause.__init__(langc_SwitchClause(True, langc_SwitchClause=langc_SwitchStatement()), False, langc_SwitchClause=langc_SwitchStatement()) == None

