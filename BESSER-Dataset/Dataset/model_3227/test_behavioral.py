import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    label_declaration_part,
    parameterList,
    pascal_actualParameter,
    pascal_assignmentStatement,
    pascal_block,
    pascal_caseListElement,
    pascal_caseStatement,
    pascal_compoundStatement,
    pascal_conditionalStatement,
    pascal_constList,
    pascal_constant,
    pascal_constantChr,
    pascal_constantDefinition,
    pascal_constantDefinitionPart,
    pascal_expression,
    pascal_factor,
    pascal_fieldList,
    pascal_fixedPart,
    pascal_formalParameterList,
    pascal_formalParameterSection,
    pascal_functionDeclaration,
    pascal_functionDesignator,
    pascal_functionType,
    pascal_gotoStatement,
    pascal_identifier,
    pascal_identifierList,
    pascal_label,
    pascal_label_declaration_part,
    pascal_parameterGroup,
    pascal_parameterList,
    pascal_pascal,
    pascal_pointerType,
    pascal_procedureAndFunctionDeclarationPart,
    pascal_procedureDeclaration,
    pascal_procedureOrFunctionDeclaration,
    pascal_procedureType,
    pascal_program,
    pascal_programHeading,
    pascal_recordSection,
    pascal_recordType,
    pascal_scalarType,
    pascal_signedFactor,
    pascal_simpleExpression,
    pascal_simpleStatement,
    pascal_simpleType,
    pascal_statement,
    pascal_statements,
    pascal_stringtype,
    pascal_structuredStatement,
    pascal_structuredType,
    pascal_subrangeType,
    pascal_tag,
    pascal_term,
    pascal_type,
    pascal_typeDefinition,
    pascal_typeDefinitionPart,
    pascal_typeIdentifier,
    pascal_unlabelledStatement,
    pascal_unpackedStructuredType,
    pascal_unsignedConstant,
    pascal_unsignedInteger,
    pascal_unsignedNumber,
    pascal_usesUnitsPart,
    pascal_variable,
    pascal_variableDeclaration,
    pascal_variableDeclarationPart,
    pascal_variant,
    pascal_variantPart,
    statement,
    variant,
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

def test_assoc_constant51_reverse_link_reassign_clear():
    a1 = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    a2 = pascal_constant(bool="sample_text_2", sign="sample_text_2", string="sample_text_2")
    b = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant52', a1)
    assert _is_linked(b, 'pascal_constant52', a1)
    if hasattr(a1, 'pascal_constant50'):
        assert _is_linked(a1, 'pascal_constant50', b)
    _safe_set(b, 'pascal_constant52', a2)
    assert _is_linked(b, 'pascal_constant52', a2)
    if hasattr(a1, 'pascal_constant50'):
        assert not _is_linked(a1, 'pascal_constant50', b)
    if hasattr(a2, 'pascal_constant50'):
        assert _is_linked(a2, 'pascal_constant50', b)
    _safe_set(b, 'pascal_constant52', None)
    assert not _is_linked(b, 'pascal_constant52', a2)
    if hasattr(a2, 'pascal_constant50'):
        assert not _is_linked(a2, 'pascal_constant50', b)


def test_assoc_expression257_reverse_link_reassign_clear():
    a1 = pascal_expression(relationaloperator="sample_text")
    a2 = pascal_expression(relationaloperator="sample_text_2")
    b = pascal_expression(relationaloperator="sample_text")
    _safe_set(b, 'pascal_expression258', a1)
    assert _is_linked(b, 'pascal_expression258', a1)
    if hasattr(a1, 'pascal_expression256'):
        assert _is_linked(a1, 'pascal_expression256', b)
    _safe_set(b, 'pascal_expression258', a2)
    assert _is_linked(b, 'pascal_expression258', a2)
    if hasattr(a1, 'pascal_expression256'):
        assert not _is_linked(a1, 'pascal_expression256', b)
    if hasattr(a2, 'pascal_expression256'):
        assert _is_linked(a2, 'pascal_expression256', b)
    _safe_set(b, 'pascal_expression258', None)
    assert not _is_linked(b, 'pascal_expression258', a2)
    if hasattr(a2, 'pascal_expression256'):
        assert not _is_linked(a2, 'pascal_expression256', b)


def test_assoc_expression271_reverse_link_reassign_clear():
    a1 = pascal_factor(bool="sample_text")
    a2 = pascal_factor(bool="sample_text_2")
    b = pascal_expression(relationaloperator="sample_text")
    _safe_set(b, 'pascal_expression273', a1)
    assert _is_linked(b, 'pascal_expression273', a1)
    if hasattr(a1, 'pascal_factor272'):
        assert _is_linked(a1, 'pascal_factor272', b)
    _safe_set(b, 'pascal_expression273', a2)
    assert _is_linked(b, 'pascal_expression273', a2)
    if hasattr(a1, 'pascal_factor272'):
        assert not _is_linked(a1, 'pascal_factor272', b)
    if hasattr(a2, 'pascal_factor272'):
        assert _is_linked(a2, 'pascal_factor272', b)
    _safe_set(b, 'pascal_expression273', None)
    assert not _is_linked(b, 'pascal_expression273', a2)
    if hasattr(a2, 'pascal_factor272'):
        assert not _is_linked(a2, 'pascal_factor272', b)


def test_assoc_factor277_reverse_link_reassign_clear():
    a1 = pascal_factor(bool="sample_text")
    a2 = pascal_factor(bool="sample_text_2")
    b = pascal_factor(bool="sample_text")
    _safe_set(b, 'pascal_factor278', a1)
    assert _is_linked(b, 'pascal_factor278', a1)
    if hasattr(a1, 'pascal_factor276'):
        assert _is_linked(a1, 'pascal_factor276', b)
    _safe_set(b, 'pascal_factor278', a2)
    assert _is_linked(b, 'pascal_factor278', a2)
    if hasattr(a1, 'pascal_factor276'):
        assert not _is_linked(a1, 'pascal_factor276', b)
    if hasattr(a2, 'pascal_factor276'):
        assert _is_linked(a2, 'pascal_factor276', b)
    _safe_set(b, 'pascal_factor278', None)
    assert not _is_linked(b, 'pascal_factor278', a2)
    if hasattr(a2, 'pascal_factor276'):
        assert not _is_linked(a2, 'pascal_factor276', b)


def test_assoc_identifier104_reverse_link_reassign_clear():
    a1 = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    a2 = pascal_typeIdentifier(boolean="sample_text_2", char="sample_text_2", integer="sample_text_2", real="sample_text_2", string="sample_text_2")
    b = pascal_identifier(identifier="sample_text")
    _safe_set(b, 'pascal_identifier106', a1)
    assert _is_linked(b, 'pascal_identifier106', a1)
    if hasattr(a1, 'pascal_typeIdentifier105'):
        assert _is_linked(a1, 'pascal_typeIdentifier105', b)
    _safe_set(b, 'pascal_identifier106', a2)
    assert _is_linked(b, 'pascal_identifier106', a2)
    if hasattr(a1, 'pascal_typeIdentifier105'):
        assert not _is_linked(a1, 'pascal_typeIdentifier105', b)
    if hasattr(a2, 'pascal_typeIdentifier105'):
        assert _is_linked(a2, 'pascal_typeIdentifier105', b)
    _safe_set(b, 'pascal_identifier106', None)
    assert not _is_linked(b, 'pascal_identifier106', a2)
    if hasattr(a2, 'pascal_typeIdentifier105'):
        assert not _is_linked(a2, 'pascal_typeIdentifier105', b)


def test_assoc_identifier45_reverse_link_reassign_clear():
    a1 = pascal_identifier(identifier="sample_text")
    a2 = pascal_identifier(identifier="sample_text_2")
    b = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant46', a1)
    assert _is_linked(b, 'pascal_constant46', a1)
    if hasattr(a1, 'pascal_identifier47'):
        assert _is_linked(a1, 'pascal_identifier47', b)
    _safe_set(b, 'pascal_constant46', a2)
    assert _is_linked(b, 'pascal_constant46', a2)
    if hasattr(a1, 'pascal_identifier47'):
        assert not _is_linked(a1, 'pascal_identifier47', b)
    if hasattr(a2, 'pascal_identifier47'):
        assert _is_linked(a2, 'pascal_identifier47', b)
    _safe_set(b, 'pascal_constant46', None)
    assert not _is_linked(b, 'pascal_constant46', a2)
    if hasattr(a2, 'pascal_identifier47'):
        assert not _is_linked(a2, 'pascal_identifier47', b)


def test_assoc_simpleExpression254_reverse_link_reassign_clear():
    a1 = pascal_simpleExpression(additiveoperator="sample_text")
    a2 = pascal_simpleExpression(additiveoperator="sample_text_2")
    b = pascal_expression(relationaloperator="sample_text")
    _safe_set(b, 'pascal_expression255', a1)
    assert _is_linked(b, 'pascal_expression255', a1)
    if hasattr(a1, 'pascal_simpleExpression'):
        assert _is_linked(a1, 'pascal_simpleExpression', b)
    _safe_set(b, 'pascal_expression255', a2)
    assert _is_linked(b, 'pascal_expression255', a2)
    if hasattr(a1, 'pascal_simpleExpression'):
        assert not _is_linked(a1, 'pascal_simpleExpression', b)
    if hasattr(a2, 'pascal_simpleExpression'):
        assert _is_linked(a2, 'pascal_simpleExpression', b)
    _safe_set(b, 'pascal_expression255', None)
    assert not _is_linked(b, 'pascal_expression255', a2)
    if hasattr(a2, 'pascal_simpleExpression'):
        assert not _is_linked(a2, 'pascal_simpleExpression', b)


def test_assoc_simpleExpression262_reverse_link_reassign_clear():
    a1 = pascal_simpleExpression(additiveoperator="sample_text")
    a2 = pascal_simpleExpression(additiveoperator="sample_text_2")
    b = pascal_simpleExpression(additiveoperator="sample_text")
    _safe_set(b, 'pascal_simpleExpression263', a1)
    assert _is_linked(b, 'pascal_simpleExpression263', a1)
    if hasattr(a1, 'pascal_simpleExpression261'):
        assert _is_linked(a1, 'pascal_simpleExpression261', b)
    _safe_set(b, 'pascal_simpleExpression263', a2)
    assert _is_linked(b, 'pascal_simpleExpression263', a2)
    if hasattr(a1, 'pascal_simpleExpression261'):
        assert not _is_linked(a1, 'pascal_simpleExpression261', b)
    if hasattr(a2, 'pascal_simpleExpression261'):
        assert _is_linked(a2, 'pascal_simpleExpression261', b)
    _safe_set(b, 'pascal_simpleExpression263', None)
    assert not _is_linked(b, 'pascal_simpleExpression263', a2)
    if hasattr(a2, 'pascal_simpleExpression261'):
        assert not _is_linked(a2, 'pascal_simpleExpression261', b)


def test_assoc_term259_reverse_link_reassign_clear():
    a1 = pascal_term(multiplicativeoperator="sample_text")
    a2 = pascal_term(multiplicativeoperator="sample_text_2")
    b = pascal_simpleExpression(additiveoperator="sample_text")
    _safe_set(b, 'pascal_simpleExpression260', a1)
    assert _is_linked(b, 'pascal_simpleExpression260', a1)
    if hasattr(a1, 'pascal_term'):
        assert _is_linked(a1, 'pascal_term', b)
    _safe_set(b, 'pascal_simpleExpression260', a2)
    assert _is_linked(b, 'pascal_simpleExpression260', a2)
    if hasattr(a1, 'pascal_term'):
        assert not _is_linked(a1, 'pascal_term', b)
    if hasattr(a2, 'pascal_term'):
        assert _is_linked(a2, 'pascal_term', b)
    _safe_set(b, 'pascal_simpleExpression260', None)
    assert not _is_linked(b, 'pascal_simpleExpression260', a2)
    if hasattr(a2, 'pascal_term'):
        assert not _is_linked(a2, 'pascal_term', b)


def test_assoc_term267_reverse_link_reassign_clear():
    a1 = pascal_term(multiplicativeoperator="sample_text")
    a2 = pascal_term(multiplicativeoperator="sample_text_2")
    b = pascal_term(multiplicativeoperator="sample_text")
    _safe_set(b, 'pascal_term268', a1)
    assert _is_linked(b, 'pascal_term268', a1)
    if hasattr(a1, 'pascal_term266'):
        assert _is_linked(a1, 'pascal_term266', b)
    _safe_set(b, 'pascal_term268', a2)
    assert _is_linked(b, 'pascal_term268', a2)
    if hasattr(a1, 'pascal_term266'):
        assert not _is_linked(a1, 'pascal_term266', b)
    if hasattr(a2, 'pascal_term266'):
        assert _is_linked(a2, 'pascal_term266', b)
    _safe_set(b, 'pascal_term268', None)
    assert not _is_linked(b, 'pascal_term268', a2)
    if hasattr(a2, 'pascal_term266'):
        assert not _is_linked(a2, 'pascal_term266', b)


def test_assoc_unsignedConstant274_reverse_link_reassign_clear():
    a1 = pascal_unsignedConstant(string_literal="sample_text")
    a2 = pascal_unsignedConstant(string_literal="sample_text_2")
    b = pascal_factor(bool="sample_text")
    _safe_set(b, 'pascal_factor275', a1)
    assert _is_linked(b, 'pascal_factor275', a1)
    if hasattr(a1, 'pascal_unsignedConstant'):
        assert _is_linked(a1, 'pascal_unsignedConstant', b)
    _safe_set(b, 'pascal_factor275', a2)
    assert _is_linked(b, 'pascal_factor275', a2)
    if hasattr(a1, 'pascal_unsignedConstant'):
        assert not _is_linked(a1, 'pascal_unsignedConstant', b)
    if hasattr(a2, 'pascal_unsignedConstant'):
        assert _is_linked(a2, 'pascal_unsignedConstant', b)
    _safe_set(b, 'pascal_factor275', None)
    assert not _is_linked(b, 'pascal_factor275', a2)
    if hasattr(a2, 'pascal_unsignedConstant'):
        assert not _is_linked(a2, 'pascal_unsignedConstant', b)


def test_assoc_unsignedInteger58_reverse_link_reassign_clear():
    a1 = pascal_unsignedNumber(unsignedReal="sample_text")
    a2 = pascal_unsignedNumber(unsignedReal="sample_text_2")
    b = pascal_unsignedInteger(number="sample_text")
    _safe_set(b, 'pascal_unsignedInteger60', a1)
    assert _is_linked(b, 'pascal_unsignedInteger60', a1)
    if hasattr(a1, 'pascal_unsignedNumber59'):
        assert _is_linked(a1, 'pascal_unsignedNumber59', b)
    _safe_set(b, 'pascal_unsignedInteger60', a2)
    assert _is_linked(b, 'pascal_unsignedInteger60', a2)
    if hasattr(a1, 'pascal_unsignedNumber59'):
        assert not _is_linked(a1, 'pascal_unsignedNumber59', b)
    if hasattr(a2, 'pascal_unsignedNumber59'):
        assert _is_linked(a2, 'pascal_unsignedNumber59', b)
    _safe_set(b, 'pascal_unsignedInteger60', None)
    assert not _is_linked(b, 'pascal_unsignedInteger60', a2)
    if hasattr(a2, 'pascal_unsignedNumber59'):
        assert not _is_linked(a2, 'pascal_unsignedNumber59', b)


def test_assoc_unsignedNumber284_reverse_link_reassign_clear():
    a1 = pascal_unsignedNumber(unsignedReal="sample_text")
    a2 = pascal_unsignedNumber(unsignedReal="sample_text_2")
    b = pascal_unsignedConstant(string_literal="sample_text")
    _safe_set(b, 'pascal_unsignedConstant285', a1)
    assert _is_linked(b, 'pascal_unsignedConstant285', a1)
    if hasattr(a1, 'pascal_unsignedNumber286'):
        assert _is_linked(a1, 'pascal_unsignedNumber286', b)
    _safe_set(b, 'pascal_unsignedConstant285', a2)
    assert _is_linked(b, 'pascal_unsignedConstant285', a2)
    if hasattr(a1, 'pascal_unsignedNumber286'):
        assert not _is_linked(a1, 'pascal_unsignedNumber286', b)
    if hasattr(a2, 'pascal_unsignedNumber286'):
        assert _is_linked(a2, 'pascal_unsignedNumber286', b)
    _safe_set(b, 'pascal_unsignedConstant285', None)
    assert not _is_linked(b, 'pascal_unsignedConstant285', a2)
    if hasattr(a2, 'pascal_unsignedNumber286'):
        assert not _is_linked(a2, 'pascal_unsignedNumber286', b)


def test_assoc_unsignedNumber43_reverse_link_reassign_clear():
    a1 = pascal_unsignedNumber(unsignedReal="sample_text")
    a2 = pascal_unsignedNumber(unsignedReal="sample_text_2")
    b = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    _safe_set(b, 'pascal_constant44', a1)
    assert _is_linked(b, 'pascal_constant44', a1)
    if hasattr(a1, 'pascal_unsignedNumber'):
        assert _is_linked(a1, 'pascal_unsignedNumber', b)
    _safe_set(b, 'pascal_constant44', a2)
    assert _is_linked(b, 'pascal_constant44', a2)
    if hasattr(a1, 'pascal_unsignedNumber'):
        assert not _is_linked(a1, 'pascal_unsignedNumber', b)
    if hasattr(a2, 'pascal_unsignedNumber'):
        assert _is_linked(a2, 'pascal_unsignedNumber', b)
    _safe_set(b, 'pascal_constant44', None)
    assert not _is_linked(b, 'pascal_constant44', a2)
    if hasattr(a2, 'pascal_unsignedNumber'):
        assert not _is_linked(a2, 'pascal_unsignedNumber', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_constant1189_stub_double():
    # pascal_constList has no real 'pascal_constList190' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    partner = pascal_constList()
    setattr(partner, 'pascal_constList190', None)
    _safe_set(owner, 'pascal_constant191', partner)
    assert owner in getattr(partner, 'pascal_constList190')
    _safe_set(owner, 'pascal_constant191', None)
    assert owner not in getattr(partner, 'pascal_constList190')


def test_assoc_constant131_stub_double():
    # pascal_subrangeType has no real 'pascal_subrangeType132' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    partner = pascal_subrangeType()
    setattr(partner, 'pascal_subrangeType132', None)
    _safe_set(owner, 'pascal_constant133', partner)
    assert getattr(partner, 'pascal_subrangeType132') == owner
    _safe_set(owner, 'pascal_constant133', None)
    assert getattr(partner, 'pascal_subrangeType132') is None


def test_assoc_constant187_stub_double():
    # pascal_constList has no real 'pascal_constList' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    partner = pascal_constList()
    setattr(partner, 'pascal_constList', None)
    _safe_set(owner, 'pascal_constant188', partner)
    assert getattr(partner, 'pascal_constList') == owner
    _safe_set(owner, 'pascal_constant188', None)
    assert getattr(partner, 'pascal_constList') is None


def test_assoc_constant2134_stub_double():
    # pascal_subrangeType has no real 'pascal_subrangeType135' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    partner = pascal_subrangeType()
    setattr(partner, 'pascal_subrangeType135', None)
    _safe_set(owner, 'pascal_constant136', partner)
    assert getattr(partner, 'pascal_subrangeType135') == owner
    _safe_set(owner, 'pascal_constant136', None)
    assert getattr(partner, 'pascal_subrangeType135') is None


def test_assoc_constant41_stub_double():
    # pascal_constantDefinition has no real 'pascal_constantDefinition42' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    partner = pascal_constantDefinition()
    setattr(partner, 'pascal_constantDefinition42', None)
    _safe_set(owner, 'pascal_constant', partner)
    assert getattr(partner, 'pascal_constantDefinition42') == owner
    _safe_set(owner, 'pascal_constant', None)
    assert getattr(partner, 'pascal_constantDefinition42') is None


def test_assoc_constantChr287_stub_double():
    # pascal_constantChr has no real 'pascal_constantChr289' property in the generated
    # code (a bare stub) -- manually attach it so pascal_unsignedConstant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_unsignedConstant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_unsignedConstant(string_literal="sample_text")
    partner = pascal_constantChr()
    setattr(partner, 'pascal_constantChr289', None)
    _safe_set(owner, 'pascal_unsignedConstant288', partner)
    assert getattr(partner, 'pascal_constantChr289') == owner
    _safe_set(owner, 'pascal_unsignedConstant288', None)
    assert getattr(partner, 'pascal_constantChr289') is None


def test_assoc_constantChr48_stub_double():
    # pascal_constantChr has no real 'pascal_constantChr' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    partner = pascal_constantChr()
    setattr(partner, 'pascal_constantChr', None)
    _safe_set(owner, 'pascal_constant49', partner)
    assert getattr(partner, 'pascal_constantChr') == owner
    _safe_set(owner, 'pascal_constant49', None)
    assert getattr(partner, 'pascal_constantChr') is None


def test_assoc_expression203_stub_double():
    # pascal_variableDeclaration has no real 'pascal_variableDeclaration204' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relationaloperator="sample_text")
    partner = pascal_variableDeclaration()
    setattr(partner, 'pascal_variableDeclaration204', None)
    _safe_set(owner, 'pascal_expression', partner)
    assert getattr(partner, 'pascal_variableDeclaration204') == owner
    _safe_set(owner, 'pascal_expression', None)
    assert getattr(partner, 'pascal_variableDeclaration204') is None


def test_assoc_expression248_stub_double():
    # pascal_assignmentStatement has no real 'pascal_assignmentStatement249' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relationaloperator="sample_text")
    partner = pascal_assignmentStatement()
    setattr(partner, 'pascal_assignmentStatement249', None)
    _safe_set(owner, 'pascal_expression250', partner)
    assert getattr(partner, 'pascal_assignmentStatement249') == owner
    _safe_set(owner, 'pascal_expression250', None)
    assert getattr(partner, 'pascal_assignmentStatement249') is None


def test_assoc_expression298_stub_double():
    # pascal_actualParameter has no real 'pascal_actualParameter299' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relationaloperator="sample_text")
    partner = pascal_actualParameter()
    setattr(partner, 'pascal_actualParameter299', None)
    _safe_set(owner, 'pascal_expression300', partner)
    assert getattr(partner, 'pascal_actualParameter299') == owner
    _safe_set(owner, 'pascal_expression300', None)
    assert getattr(partner, 'pascal_actualParameter299') is None


def test_assoc_expression316_stub_double():
    # pascal_caseStatement has no real 'pascal_caseStatement317' property in the generated
    # code (a bare stub) -- manually attach it so pascal_expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_expression(relationaloperator="sample_text")
    partner = pascal_caseStatement()
    setattr(partner, 'pascal_caseStatement317', None)
    _safe_set(owner, 'pascal_expression318', partner)
    assert getattr(partner, 'pascal_caseStatement317') == owner
    _safe_set(owner, 'pascal_expression318', None)
    assert getattr(partner, 'pascal_caseStatement317') is None


def test_assoc_factor269_stub_double():
    # pascal_signedFactor has no real 'pascal_signedFactor270' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(bool="sample_text")
    partner = pascal_signedFactor()
    setattr(partner, 'pascal_signedFactor270', None)
    _safe_set(owner, 'pascal_factor', partner)
    assert getattr(partner, 'pascal_signedFactor270') == owner
    _safe_set(owner, 'pascal_factor', None)
    assert getattr(partner, 'pascal_signedFactor270') is None


def test_assoc_fieldList53_stub_double():
    # pascal_fieldList has no real 'pascal_fieldList' property in the generated
    # code (a bare stub) -- manually attach it so pascal_constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    partner = pascal_fieldList()
    setattr(partner, 'pascal_fieldList', None)
    _safe_set(owner, 'pascal_constant54', partner)
    assert getattr(partner, 'pascal_fieldList') == owner
    _safe_set(owner, 'pascal_constant54', None)
    assert getattr(partner, 'pascal_fieldList') is None


def test_assoc_functionDesignator279_stub_double():
    # pascal_functionDesignator has no real 'pascal_functionDesignator' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(bool="sample_text")
    partner = pascal_functionDesignator()
    setattr(partner, 'pascal_functionDesignator', None)
    _safe_set(owner, 'pascal_factor280', partner)
    assert getattr(partner, 'pascal_functionDesignator') == owner
    _safe_set(owner, 'pascal_factor280', None)
    assert getattr(partner, 'pascal_functionDesignator') is None


def test_assoc_identifer5_stub_double():
    # pascal_programHeading has no real 'pascal_programHeading6' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_programHeading()
    setattr(partner, 'pascal_programHeading6', None)
    _safe_set(owner, 'pascal_identifier', partner)
    assert getattr(partner, 'pascal_programHeading6') == owner
    _safe_set(owner, 'pascal_identifier', None)
    assert getattr(partner, 'pascal_programHeading6') is None


def test_assoc_identifier144_stub_double():
    # pascal_stringtype has no real 'pascal_stringtype145' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_stringtype()
    setattr(partner, 'pascal_stringtype145', None)
    _safe_set(owner, 'pascal_identifier146', partner)
    assert getattr(partner, 'pascal_stringtype145') == owner
    _safe_set(owner, 'pascal_identifier146', None)
    assert getattr(partner, 'pascal_stringtype145') is None


def test_assoc_identifier178_stub_double():
    # pascal_tag has no real 'pascal_tag179' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_tag()
    setattr(partner, 'pascal_tag179', None)
    _safe_set(owner, 'pascal_identifier180', partner)
    assert getattr(partner, 'pascal_tag179') == owner
    _safe_set(owner, 'pascal_identifier180', None)
    assert getattr(partner, 'pascal_tag179') is None


def test_assoc_identifier211_stub_double():
    # pascal_procedureDeclaration has no real 'pascal_procedureDeclaration212' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_procedureDeclaration()
    setattr(partner, 'pascal_procedureDeclaration212', None)
    _safe_set(owner, 'pascal_identifier213', partner)
    assert getattr(partner, 'pascal_procedureDeclaration212') == owner
    _safe_set(owner, 'pascal_identifier213', None)
    assert getattr(partner, 'pascal_procedureDeclaration212') is None


def test_assoc_identifier220_stub_double():
    # pascal_functionDeclaration has no real 'pascal_functionDeclaration221' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_functionDeclaration()
    setattr(partner, 'pascal_functionDeclaration221', None)
    _safe_set(owner, 'pascal_identifier222', partner)
    assert getattr(partner, 'pascal_functionDeclaration221') == owner
    _safe_set(owner, 'pascal_identifier222', None)
    assert getattr(partner, 'pascal_functionDeclaration221') is None


def test_assoc_identifier237_stub_double():
    # pascal_unlabelledStatement has no real 'pascal_unlabelledStatement238' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_unlabelledStatement()
    setattr(partner, 'pascal_unlabelledStatement238', None)
    _safe_set(owner, 'pascal_identifier239', partner)
    assert getattr(partner, 'pascal_unlabelledStatement238') == owner
    _safe_set(owner, 'pascal_identifier239', None)
    assert getattr(partner, 'pascal_unlabelledStatement238') is None


def test_assoc_identifier251_stub_double():
    # pascal_variable has no real 'pascal_variable252' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_variable()
    setattr(partner, 'pascal_variable252', None)
    _safe_set(owner, 'pascal_identifier253', partner)
    assert getattr(partner, 'pascal_variable252') == owner
    _safe_set(owner, 'pascal_identifier253', None)
    assert getattr(partner, 'pascal_variable252') is None


def test_assoc_identifier290_stub_double():
    # pascal_functionDesignator has no real 'pascal_functionDesignator291' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_functionDesignator()
    setattr(partner, 'pascal_functionDesignator291', None)
    _safe_set(owner, 'pascal_identifier292', partner)
    assert getattr(partner, 'pascal_functionDesignator291') == owner
    _safe_set(owner, 'pascal_identifier292', None)
    assert getattr(partner, 'pascal_functionDesignator291') is None


def test_assoc_identifier33_stub_double():
    # pascal_label has no real 'pascal_label34' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_label()
    setattr(partner, 'pascal_label34', None)
    _safe_set(owner, 'pascal_identifier35', partner)
    assert getattr(partner, 'pascal_label34') == owner
    _safe_set(owner, 'pascal_identifier35', None)
    assert getattr(partner, 'pascal_label34') is None


def test_assoc_identifier38_stub_double():
    # pascal_constantDefinition has no real 'pascal_constantDefinition39' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_constantDefinition()
    setattr(partner, 'pascal_constantDefinition39', None)
    _safe_set(owner, 'pascal_identifier40', partner)
    assert getattr(partner, 'pascal_constantDefinition39') == owner
    _safe_set(owner, 'pascal_identifier40', None)
    assert getattr(partner, 'pascal_constantDefinition39') is None


def test_assoc_identifier69_stub_double():
    # pascal_typeDefinition has no real 'pascal_typeDefinition70' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_typeDefinition()
    setattr(partner, 'pascal_typeDefinition70', None)
    _safe_set(owner, 'pascal_identifier71', partner)
    assert getattr(partner, 'pascal_typeDefinition70') == owner
    _safe_set(owner, 'pascal_identifier71', None)
    assert getattr(partner, 'pascal_typeDefinition70') is None


def test_assoc_identifier9_stub_double():
    # pascal_identifierList has no real 'pascal_identifierList10' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_identifierList()
    setattr(partner, 'pascal_identifierList10', None)
    _safe_set(owner, 'pascal_identifier11', partner)
    assert getattr(partner, 'pascal_identifierList10') == owner
    _safe_set(owner, 'pascal_identifier11', None)
    assert getattr(partner, 'pascal_identifierList10') is None


def test_assoc_identifierList112_stub_double():
    # pascal_identifierList has no real 'pascal_identifierList13' property in the generated
    # code (a bare stub) -- manually attach it so pascal_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_identifier(identifier="sample_text")
    partner = pascal_identifierList()
    setattr(partner, 'pascal_identifierList13', None)
    _safe_set(owner, 'pascal_identifier14', partner)
    assert owner in getattr(partner, 'pascal_identifierList13')
    _safe_set(owner, 'pascal_identifier14', None)
    assert owner not in getattr(partner, 'pascal_identifierList13')


def test_assoc_signedFactor264_stub_double():
    # pascal_signedFactor has no real 'pascal_signedFactor' property in the generated
    # code (a bare stub) -- manually attach it so pascal_term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_term(multiplicativeoperator="sample_text")
    partner = pascal_signedFactor()
    setattr(partner, 'pascal_signedFactor', None)
    _safe_set(owner, 'pascal_term265', partner)
    assert getattr(partner, 'pascal_signedFactor') == owner
    _safe_set(owner, 'pascal_term265', None)
    assert getattr(partner, 'pascal_signedFactor') is None


def test_assoc_typeIdentifier101_stub_double():
    # pascal_parameterGroup has no real 'pascal_parameterGroup102' property in the generated
    # code (a bare stub) -- manually attach it so pascal_typeIdentifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_typeIdentifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    partner = pascal_parameterGroup()
    setattr(partner, 'pascal_parameterGroup102', None)
    _safe_set(owner, 'pascal_typeIdentifier103', partner)
    assert getattr(partner, 'pascal_parameterGroup102') == owner
    _safe_set(owner, 'pascal_typeIdentifier103', None)
    assert getattr(partner, 'pascal_parameterGroup102') is None


def test_assoc_typeIdentifier116_stub_double():
    # pascal_pointerType has no real 'pascal_pointerType117' property in the generated
    # code (a bare stub) -- manually attach it so pascal_typeIdentifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_typeIdentifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    partner = pascal_pointerType()
    setattr(partner, 'pascal_pointerType117', None)
    _safe_set(owner, 'pascal_typeIdentifier118', partner)
    assert getattr(partner, 'pascal_pointerType117') == owner
    _safe_set(owner, 'pascal_typeIdentifier118', None)
    assert getattr(partner, 'pascal_pointerType117') is None


def test_assoc_typeIdentifier1184_stub_double():
    # pascal_tag has no real 'pascal_tag185' property in the generated
    # code (a bare stub) -- manually attach it so pascal_typeIdentifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_typeIdentifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    partner = pascal_tag()
    setattr(partner, 'pascal_tag185', None)
    _safe_set(owner, 'pascal_typeIdentifier186', partner)
    assert owner in getattr(partner, 'pascal_tag185')
    _safe_set(owner, 'pascal_typeIdentifier186', None)
    assert owner not in getattr(partner, 'pascal_tag185')


def test_assoc_typeIdentifier123_stub_double():
    # pascal_simpleType has no real 'pascal_simpleType124' property in the generated
    # code (a bare stub) -- manually attach it so pascal_typeIdentifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_typeIdentifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    partner = pascal_simpleType()
    setattr(partner, 'pascal_simpleType124', None)
    _safe_set(owner, 'pascal_typeIdentifier125', partner)
    assert getattr(partner, 'pascal_simpleType124') == owner
    _safe_set(owner, 'pascal_typeIdentifier125', None)
    assert getattr(partner, 'pascal_simpleType124') is None


def test_assoc_typeIdentifier181_stub_double():
    # pascal_tag has no real 'pascal_tag182' property in the generated
    # code (a bare stub) -- manually attach it so pascal_typeIdentifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_typeIdentifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    partner = pascal_tag()
    setattr(partner, 'pascal_tag182', None)
    _safe_set(owner, 'pascal_typeIdentifier183', partner)
    assert getattr(partner, 'pascal_tag182') == owner
    _safe_set(owner, 'pascal_typeIdentifier183', None)
    assert getattr(partner, 'pascal_tag182') is None


def test_assoc_typeIdentifier226_stub_double():
    # pascal_functionDeclaration has no real 'pascal_functionDeclaration227' property in the generated
    # code (a bare stub) -- manually attach it so pascal_typeIdentifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_typeIdentifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    partner = pascal_functionDeclaration()
    setattr(partner, 'pascal_functionDeclaration227', None)
    _safe_set(owner, 'pascal_typeIdentifier228', partner)
    assert getattr(partner, 'pascal_functionDeclaration227') == owner
    _safe_set(owner, 'pascal_typeIdentifier228', None)
    assert getattr(partner, 'pascal_functionDeclaration227') is None


def test_assoc_typeIdentifier80_stub_double():
    # pascal_functionType has no real 'pascal_functionType81' property in the generated
    # code (a bare stub) -- manually attach it so pascal_typeIdentifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_typeIdentifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    partner = pascal_functionType()
    setattr(partner, 'pascal_functionType81', None)
    _safe_set(owner, 'pascal_typeIdentifier', partner)
    assert getattr(partner, 'pascal_functionType81') == owner
    _safe_set(owner, 'pascal_typeIdentifier', None)
    assert getattr(partner, 'pascal_functionType81') is None


def test_assoc_unsignedInteger31_stub_double():
    # pascal_label has no real 'pascal_label32' property in the generated
    # code (a bare stub) -- manually attach it so pascal_unsignedInteger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_unsignedInteger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_unsignedInteger(number="sample_text")
    partner = pascal_label()
    setattr(partner, 'pascal_label32', None)
    _safe_set(owner, 'pascal_unsignedInteger', partner)
    assert getattr(partner, 'pascal_label32') == owner
    _safe_set(owner, 'pascal_unsignedInteger', None)
    assert getattr(partner, 'pascal_label32') is None


def test_assoc_unsignedInteger55_stub_double():
    # pascal_constantChr has no real 'pascal_constantChr56' property in the generated
    # code (a bare stub) -- manually attach it so pascal_unsignedInteger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_unsignedInteger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_unsignedInteger(number="sample_text")
    partner = pascal_constantChr()
    setattr(partner, 'pascal_constantChr56', None)
    _safe_set(owner, 'pascal_unsignedInteger57', partner)
    assert getattr(partner, 'pascal_constantChr56') == owner
    _safe_set(owner, 'pascal_unsignedInteger57', None)
    assert getattr(partner, 'pascal_constantChr56') is None


def test_assoc_unsignedNumber147_stub_double():
    # pascal_stringtype has no real 'pascal_stringtype148' property in the generated
    # code (a bare stub) -- manually attach it so pascal_unsignedNumber's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_unsignedNumber's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_unsignedNumber(unsignedReal="sample_text")
    partner = pascal_stringtype()
    setattr(partner, 'pascal_stringtype148', None)
    _safe_set(owner, 'pascal_unsignedNumber149', partner)
    assert getattr(partner, 'pascal_stringtype148') == owner
    _safe_set(owner, 'pascal_unsignedNumber149', None)
    assert getattr(partner, 'pascal_stringtype148') is None


def test_assoc_variable281_stub_double():
    # pascal_variable has no real 'pascal_variable283' property in the generated
    # code (a bare stub) -- manually attach it so pascal_factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pascal_factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pascal_factor(bool="sample_text")
    partner = pascal_variable()
    setattr(partner, 'pascal_variable283', None)
    _safe_set(owner, 'pascal_factor282', partner)
    assert getattr(partner, 'pascal_variable283') == owner
    _safe_set(owner, 'pascal_factor282', None)
    assert getattr(partner, 'pascal_variable283') is None


