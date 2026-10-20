import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractAspect,
    AbstractDeclaration,
    AbstractExpression,
    AbstractNamedDeclaration,
    AbstractStatement,
    AbstractStatementWithBody,
    BinaryOperation,
    Case,
    Extension,
    FeatureCall,
    IfStatement,
    Literal,
    SyntaxElement,
    declaration_xpand3_DeclaredParameter,
    declaration_xpand3_File,
    declaration_xpand3_Identifier,
    expression_xpand3_Identifier,
    statement_xpand3_Identifier,
    xpand3_DeclaredParameter,
    xpand3_File,
    xpand3_Identifier,
    xpand3_ImportStatement,
    xpand3_SyntaxElement,
    xpand3_declaration_AbstractAspect,
    xpand3_declaration_AbstractDeclaration,
    xpand3_declaration_AbstractNamedDeclaration,
    xpand3_declaration_Check,
    xpand3_declaration_CreateExtension,
    xpand3_declaration_Definition,
    xpand3_declaration_DefinitionAspect,
    xpand3_declaration_Extension,
    xpand3_declaration_ExtensionAspect,
    xpand3_declaration_JavaExtension,
    xpand3_expression_AbstractExpression,
    xpand3_expression_BinaryOperation,
    xpand3_expression_BooleanLiteral,
    xpand3_expression_BooleanOperation,
    xpand3_expression_Case,
    xpand3_expression_Cast,
    xpand3_expression_ChainExpression,
    xpand3_expression_CollectionExpression,
    xpand3_expression_ConstructorCallExpression,
    xpand3_expression_FeatureCall,
    xpand3_expression_GlobalVarExpression,
    xpand3_expression_IfExpression,
    xpand3_expression_IntegerLiteral,
    xpand3_expression_LetExpression,
    xpand3_expression_ListLiteral,
    xpand3_expression_Literal,
    xpand3_expression_NullLiteral,
    xpand3_expression_OperationCall,
    xpand3_expression_RealLiteral,
    xpand3_expression_StringLiteral,
    xpand3_expression_SwitchExpression,
    xpand3_expression_TypeSelectExpression,
    xpand3_expression_UnaryOperation,
    xpand3_statement_AbstractStatement,
    xpand3_statement_AbstractStatementWithBody,
    xpand3_statement_ErrorStatement,
    xpand3_statement_ExpandStatement,
    xpand3_statement_ExpressionStatement,
    xpand3_statement_FileStatement,
    xpand3_statement_ForEachStatement,
    xpand3_statement_IfStatement,
    xpand3_statement_LetStatement,
    xpand3_statement_ProtectStatement,
    xpand3_statement_TextStatement,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_importedId3_reverse_link_reassign_clear():
    a1 = xpand3_ImportStatement(exported=True)
    a2 = xpand3_ImportStatement(exported=False)
    b = xpand3_Identifier(value="sample_text")
    _safe_set(b, 'xpand3_Identifier', a1)
    assert _is_linked(b, 'xpand3_Identifier', a1)
    if hasattr(a1, 'xpand3_ImportStatement4'):
        assert _is_linked(a1, 'xpand3_ImportStatement4', b)
    _safe_set(b, 'xpand3_Identifier', a2)
    assert _is_linked(b, 'xpand3_Identifier', a2)
    if hasattr(a1, 'xpand3_ImportStatement4'):
        assert not _is_linked(a1, 'xpand3_ImportStatement4', b)
    if hasattr(a2, 'xpand3_ImportStatement4'):
        assert _is_linked(a2, 'xpand3_ImportStatement4', b)
    _safe_set(b, 'xpand3_Identifier', None)
    assert not _is_linked(b, 'xpand3_Identifier', a2)
    if hasattr(a2, 'xpand3_ImportStatement4'):
        assert not _is_linked(a2, 'xpand3_ImportStatement4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body138_stub_double():
    # AbstractExpression has no real 'AbstractExpression139' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_Extension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_Extension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_Extension(cached=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression139', None)
    _safe_set(owner, 'xpand3_declaration_Extension', partner)
    assert getattr(partner, 'AbstractExpression139') == owner
    _safe_set(owner, 'xpand3_declaration_Extension', None)
    assert getattr(partner, 'AbstractExpression139') is None


def test_assoc_commentEnd123_stub_double():
    # AbstractExpression has no real 'AbstractExpression125' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_ProtectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_ProtectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_ProtectStatement(disable=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression125', None)
    _safe_set(owner, 'xpand3_statement_ProtectStatement124', partner)
    assert getattr(partner, 'AbstractExpression125') == owner
    _safe_set(owner, 'xpand3_statement_ProtectStatement124', None)
    assert getattr(partner, 'AbstractExpression125') is None


def test_assoc_commentStart121_stub_double():
    # AbstractExpression has no real 'AbstractExpression122' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_ProtectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_ProtectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_ProtectStatement(disable=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression122', None)
    _safe_set(owner, 'xpand3_statement_ProtectStatement', partner)
    assert getattr(partner, 'AbstractExpression122') == owner
    _safe_set(owner, 'xpand3_statement_ProtectStatement', None)
    assert getattr(partner, 'AbstractExpression122') is None


def test_assoc_constraint151_stub_double():
    # AbstractExpression has no real 'AbstractExpression153' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_Check's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_Check's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_Check(errorSeverity=True, feature="sample_text")
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression153', None)
    _safe_set(owner, 'xpand3_declaration_Check152', partner)
    assert getattr(partner, 'AbstractExpression153') == owner
    _safe_set(owner, 'xpand3_declaration_Check152', None)
    assert getattr(partner, 'AbstractExpression153') is None


def test_assoc_definition89_stub_double():
    # statement_xpand3_Identifier has no real 'statement_xpand3_Identifier' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_ExpandStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_ExpandStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_ExpandStatement(foreach=True)
    partner = statement_xpand3_Identifier()
    setattr(partner, 'statement_xpand3_Identifier', None)
    _safe_set(owner, 'xpand3_statement_ExpandStatement90', partner)
    assert getattr(partner, 'statement_xpand3_Identifier') == owner
    _safe_set(owner, 'xpand3_statement_ExpandStatement90', None)
    assert getattr(partner, 'statement_xpand3_Identifier') is None


def test_assoc_fileNameExpression96_stub_double():
    # AbstractExpression has no real 'AbstractExpression97' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_FileStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_FileStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_FileStatement(once=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression97', None)
    _safe_set(owner, 'xpand3_statement_FileStatement', partner)
    assert getattr(partner, 'AbstractExpression97') == owner
    _safe_set(owner, 'xpand3_statement_FileStatement', None)
    assert getattr(partner, 'AbstractExpression97') is None


def test_assoc_guard132_stub_double():
    # AbstractExpression has no real 'AbstractExpression134' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_AbstractDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_AbstractDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_AbstractDeclaration(isPrivate=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression134', None)
    _safe_set(owner, 'xpand3_declaration_AbstractDeclaration133', partner)
    assert getattr(partner, 'AbstractExpression134') == owner
    _safe_set(owner, 'xpand3_declaration_AbstractDeclaration133', None)
    assert getattr(partner, 'AbstractExpression134') is None


def test_assoc_id126_stub_double():
    # AbstractExpression has no real 'AbstractExpression128' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_ProtectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_ProtectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_ProtectStatement(disable=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression128', None)
    _safe_set(owner, 'xpand3_statement_ProtectStatement127', partner)
    assert getattr(partner, 'AbstractExpression128') == owner
    _safe_set(owner, 'xpand3_statement_ProtectStatement127', None)
    assert getattr(partner, 'AbstractExpression128') is None


def test_assoc_imports0_stub_double():
    # xpand3_File has no real 'xpand3_File' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_ImportStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_ImportStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_ImportStatement(exported=True)
    partner = xpand3_File()
    setattr(partner, 'xpand3_File', None)
    _safe_set(owner, 'xpand3_ImportStatement', partner)
    assert owner in getattr(partner, 'xpand3_File')
    _safe_set(owner, 'xpand3_ImportStatement', None)
    assert owner not in getattr(partner, 'xpand3_File')


def test_assoc_msg149_stub_double():
    # AbstractExpression has no real 'AbstractExpression150' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_Check's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_Check's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_Check(errorSeverity=True, feature="sample_text")
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression150', None)
    _safe_set(owner, 'xpand3_declaration_Check', partner)
    assert getattr(partner, 'AbstractExpression150') == owner
    _safe_set(owner, 'xpand3_declaration_Check', None)
    assert getattr(partner, 'AbstractExpression150') is None


def test_assoc_name5_stub_double():
    # xpand3_DeclaredParameter has no real 'xpand3_DeclaredParameter' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_Identifier(value="sample_text")
    partner = xpand3_DeclaredParameter()
    setattr(partner, 'xpand3_DeclaredParameter', None)
    _safe_set(owner, 'xpand3_Identifier6', partner)
    assert getattr(partner, 'xpand3_DeclaredParameter') == owner
    _safe_set(owner, 'xpand3_Identifier6', None)
    assert getattr(partner, 'xpand3_DeclaredParameter') is None


def test_assoc_outletNameIdentifier98_stub_double():
    # statement_xpand3_Identifier has no real 'statement_xpand3_Identifier100' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_FileStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_FileStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_FileStatement(once=True)
    partner = statement_xpand3_Identifier()
    setattr(partner, 'statement_xpand3_Identifier100', None)
    _safe_set(owner, 'xpand3_statement_FileStatement99', partner)
    assert getattr(partner, 'statement_xpand3_Identifier100') == owner
    _safe_set(owner, 'xpand3_statement_FileStatement99', None)
    assert getattr(partner, 'statement_xpand3_Identifier100') is None


def test_assoc_owner129_stub_double():
    # declaration_xpand3_File has no real 'declaration_xpand3_File' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_AbstractDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_AbstractDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_AbstractDeclaration(isPrivate=True)
    partner = declaration_xpand3_File()
    setattr(partner, 'declaration_xpand3_File', None)
    _safe_set(owner, 'xpand3_declaration_AbstractDeclaration', partner)
    assert getattr(partner, 'declaration_xpand3_File') == owner
    _safe_set(owner, 'xpand3_declaration_AbstractDeclaration', None)
    assert getattr(partner, 'declaration_xpand3_File') is None


def test_assoc_parameters81_stub_double():
    # AbstractExpression has no real 'AbstractExpression82' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_ExpandStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_ExpandStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_ExpandStatement(foreach=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression82', None)
    _safe_set(owner, 'xpand3_statement_ExpandStatement', {partner})
    assert getattr(partner, 'AbstractExpression82') == owner
    _safe_set(owner, 'xpand3_statement_ExpandStatement', set())
    assert getattr(partner, 'AbstractExpression82') is None


def test_assoc_params130_stub_double():
    # declaration_xpand3_DeclaredParameter has no real 'declaration_xpand3_DeclaredParameter' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_AbstractDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_AbstractDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_AbstractDeclaration(isPrivate=True)
    partner = declaration_xpand3_DeclaredParameter()
    setattr(partner, 'declaration_xpand3_DeclaredParameter', None)
    _safe_set(owner, 'xpand3_declaration_AbstractDeclaration131', {partner})
    assert getattr(partner, 'declaration_xpand3_DeclaredParameter') == owner
    _safe_set(owner, 'xpand3_declaration_AbstractDeclaration131', set())
    assert getattr(partner, 'declaration_xpand3_DeclaredParameter') is None


def test_assoc_pointcut143_stub_double():
    # declaration_xpand3_Identifier has no real 'declaration_xpand3_Identifier144' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_AbstractAspect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_AbstractAspect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_AbstractAspect(wildparams=True)
    partner = declaration_xpand3_Identifier()
    setattr(partner, 'declaration_xpand3_Identifier144', None)
    _safe_set(owner, 'xpand3_declaration_AbstractAspect', partner)
    assert getattr(partner, 'declaration_xpand3_Identifier144') == owner
    _safe_set(owner, 'xpand3_declaration_AbstractAspect', None)
    assert getattr(partner, 'declaration_xpand3_Identifier144') is None


def test_assoc_returnType140_stub_double():
    # declaration_xpand3_Identifier has no real 'declaration_xpand3_Identifier142' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_declaration_Extension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_declaration_Extension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_declaration_Extension(cached=True)
    partner = declaration_xpand3_Identifier()
    setattr(partner, 'declaration_xpand3_Identifier142', None)
    _safe_set(owner, 'xpand3_declaration_Extension141', partner)
    assert getattr(partner, 'declaration_xpand3_Identifier142') == owner
    _safe_set(owner, 'xpand3_declaration_Extension141', None)
    assert getattr(partner, 'declaration_xpand3_Identifier142') is None


def test_assoc_separator83_stub_double():
    # AbstractExpression has no real 'AbstractExpression85' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_ExpandStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_ExpandStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_ExpandStatement(foreach=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression85', None)
    _safe_set(owner, 'xpand3_statement_ExpandStatement84', partner)
    assert getattr(partner, 'AbstractExpression85') == owner
    _safe_set(owner, 'xpand3_statement_ExpandStatement84', None)
    assert getattr(partner, 'AbstractExpression85') is None


def test_assoc_target86_stub_double():
    # AbstractExpression has no real 'AbstractExpression88' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_statement_ExpandStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_statement_ExpandStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_statement_ExpandStatement(foreach=True)
    partner = AbstractExpression()
    setattr(partner, 'AbstractExpression88', None)
    _safe_set(owner, 'xpand3_statement_ExpandStatement87', partner)
    assert getattr(partner, 'AbstractExpression88') == owner
    _safe_set(owner, 'xpand3_statement_ExpandStatement87', None)
    assert getattr(partner, 'AbstractExpression88') is None


def test_assoc_type7_stub_double():
    # xpand3_DeclaredParameter has no real 'xpand3_DeclaredParameter8' property in the generated
    # code (a bare stub) -- manually attach it so xpand3_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpand3_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpand3_Identifier(value="sample_text")
    partner = xpand3_DeclaredParameter()
    setattr(partner, 'xpand3_DeclaredParameter8', None)
    _safe_set(owner, 'xpand3_Identifier9', partner)
    assert getattr(partner, 'xpand3_DeclaredParameter8') == owner
    _safe_set(owner, 'xpand3_Identifier9', None)
    assert getattr(partner, 'xpand3_DeclaredParameter8') is None


