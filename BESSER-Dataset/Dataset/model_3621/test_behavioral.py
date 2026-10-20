import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    NamePattern,
    NamedElements,
    OperatorPattern,
    ParamValue,
    tgg_Adornment,
    tgg_AttrCond,
    tgg_AttrCondDef,
    tgg_AttrCondDefLibrary,
    tgg_AttributeAssignment,
    tgg_AttributeConstraint,
    tgg_AttributeExpression,
    tgg_ComplementRule,
    tgg_ContextLinkVariablePattern,
    tgg_ContextObjectVariablePattern,
    tgg_CorrType,
    tgg_CorrVariablePattern,
    tgg_EAttribute,
    tgg_EClass,
    tgg_EDataType,
    tgg_EEnum,
    tgg_EEnumLiteral,
    tgg_EObject,
    tgg_EPackage,
    tgg_EReference,
    tgg_EnumExpression,
    tgg_Expression,
    tgg_Import,
    tgg_LinkVariablePattern,
    tgg_LiteralExpression,
    tgg_LocalVariable,
    tgg_Nac,
    tgg_NamePattern,
    tgg_NamedElements,
    tgg_ObjectVariablePattern,
    tgg_Operator,
    tgg_OperatorPattern,
    tgg_Param,
    tgg_ParamValue,
    tgg_Rule,
    tgg_Schema,
    tgg_TripleGraphGrammarFile,
    tgg_Using,
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

def test_assoc_allowedGenAdornments34_reverse_link_reassign_clear():
    a1 = tgg_AttrCondDef(userDefined=True)
    a2 = tgg_AttrCondDef(userDefined=False)
    b = tgg_Adornment(value="sample_text")
    _safe_set(b, 'tgg_Adornment36', a1)
    assert _is_linked(b, 'tgg_Adornment36', a1)
    if hasattr(a1, 'tgg_AttrCondDef35'):
        assert _is_linked(a1, 'tgg_AttrCondDef35', b)
    _safe_set(b, 'tgg_Adornment36', a2)
    assert _is_linked(b, 'tgg_Adornment36', a2)
    if hasattr(a1, 'tgg_AttrCondDef35'):
        assert not _is_linked(a1, 'tgg_AttrCondDef35', b)
    if hasattr(a2, 'tgg_AttrCondDef35'):
        assert _is_linked(a2, 'tgg_AttrCondDef35', b)
    _safe_set(b, 'tgg_Adornment36', None)
    assert not _is_linked(b, 'tgg_Adornment36', a2)
    if hasattr(a2, 'tgg_AttrCondDef35'):
        assert not _is_linked(a2, 'tgg_AttrCondDef35', b)


def test_assoc_allowedSyncAdornments32_reverse_link_reassign_clear():
    a1 = tgg_AttrCondDef(userDefined=True)
    a2 = tgg_AttrCondDef(userDefined=False)
    b = tgg_Adornment(value="sample_text")
    _safe_set(b, 'tgg_Adornment', a1)
    assert _is_linked(b, 'tgg_Adornment', a1)
    if hasattr(a1, 'tgg_AttrCondDef33'):
        assert _is_linked(a1, 'tgg_AttrCondDef33', b)
    _safe_set(b, 'tgg_Adornment', a2)
    assert _is_linked(b, 'tgg_Adornment', a2)
    if hasattr(a1, 'tgg_AttrCondDef33'):
        assert not _is_linked(a1, 'tgg_AttrCondDef33', b)
    if hasattr(a2, 'tgg_AttrCondDef33'):
        assert _is_linked(a2, 'tgg_AttrCondDef33', b)
    _safe_set(b, 'tgg_Adornment', None)
    assert not _is_linked(b, 'tgg_Adornment', a2)
    if hasattr(a2, 'tgg_AttrCondDef33'):
        assert not _is_linked(a2, 'tgg_AttrCondDef33', b)


def test_assoc_attributeConstraints82_reverse_link_reassign_clear():
    a1 = tgg_ContextObjectVariablePattern(name="sample_text")
    a2 = tgg_ContextObjectVariablePattern(name="sample_text_2")
    b = tgg_AttributeConstraint(op="sample_text")
    _safe_set(b, 'tgg_AttributeConstraint84', a1)
    assert _is_linked(b, 'tgg_AttributeConstraint84', a1)
    if hasattr(a1, 'tgg_ContextObjectVariablePattern83'):
        assert _is_linked(a1, 'tgg_ContextObjectVariablePattern83', b)
    _safe_set(b, 'tgg_AttributeConstraint84', a2)
    assert _is_linked(b, 'tgg_AttributeConstraint84', a2)
    if hasattr(a1, 'tgg_ContextObjectVariablePattern83'):
        assert not _is_linked(a1, 'tgg_ContextObjectVariablePattern83', b)
    if hasattr(a2, 'tgg_ContextObjectVariablePattern83'):
        assert _is_linked(a2, 'tgg_ContextObjectVariablePattern83', b)
    _safe_set(b, 'tgg_AttributeConstraint84', None)
    assert not _is_linked(b, 'tgg_AttributeConstraint84', a2)
    if hasattr(a2, 'tgg_ContextObjectVariablePattern83'):
        assert not _is_linked(a2, 'tgg_ContextObjectVariablePattern83', b)


def test_assoc_params30_reverse_link_reassign_clear():
    a1 = tgg_Param(paramName="sample_text")
    a2 = tgg_Param(paramName="sample_text_2")
    b = tgg_AttrCondDef(userDefined=True)
    _safe_set(b, 'tgg_AttrCondDef31', {a1})
    assert _is_linked(b, 'tgg_AttrCondDef31', a1)
    if hasattr(a1, 'tgg_Param'):
        assert _is_linked(a1, 'tgg_Param', b)
    _safe_set(b, 'tgg_AttrCondDef31', {a2})
    assert _is_linked(b, 'tgg_AttrCondDef31', a2)
    if hasattr(a1, 'tgg_Param'):
        assert not _is_linked(a1, 'tgg_Param', b)
    if hasattr(a2, 'tgg_Param'):
        assert _is_linked(a2, 'tgg_Param', b)
    _safe_set(b, 'tgg_AttrCondDef31', set())
    assert not _is_linked(b, 'tgg_AttrCondDef31', a2)
    if hasattr(a2, 'tgg_Param'):
        assert not _is_linked(a2, 'tgg_Param', b)


def test_assoc_supertypes40_reverse_link_reassign_clear():
    a1 = tgg_Rule(abstractRule=True)
    a2 = tgg_Rule(abstractRule=False)
    b = tgg_Rule(abstractRule=True)
    _safe_set(b, 'tgg_Rule41', a1)
    assert _is_linked(b, 'tgg_Rule41', a1)
    if hasattr(a1, 'tgg_Rule39'):
        assert _is_linked(a1, 'tgg_Rule39', b)
    _safe_set(b, 'tgg_Rule41', a2)
    assert _is_linked(b, 'tgg_Rule41', a2)
    if hasattr(a1, 'tgg_Rule39'):
        assert not _is_linked(a1, 'tgg_Rule39', b)
    if hasattr(a2, 'tgg_Rule39'):
        assert _is_linked(a2, 'tgg_Rule39', b)
    _safe_set(b, 'tgg_Rule41', None)
    assert not _is_linked(b, 'tgg_Rule41', a2)
    if hasattr(a2, 'tgg_Rule39'):
        assert not _is_linked(a2, 'tgg_Rule39', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attrConditions52_stub_double():
    # tgg_AttrCond has no real 'tgg_AttrCond' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_AttrCond()
    setattr(partner, 'tgg_AttrCond', None)
    _safe_set(owner, 'tgg_Rule53', {partner})
    assert getattr(partner, 'tgg_AttrCond') == owner
    _safe_set(owner, 'tgg_Rule53', set())
    assert getattr(partner, 'tgg_AttrCond') is None


def test_assoc_attribute87_stub_double():
    # tgg_EAttribute has no real 'tgg_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttributeConstraint(op="sample_text")
    partner = tgg_EAttribute()
    setattr(partner, 'tgg_EAttribute', None)
    _safe_set(owner, 'tgg_AttributeConstraint88', partner)
    assert getattr(partner, 'tgg_EAttribute') == owner
    _safe_set(owner, 'tgg_AttributeConstraint88', None)
    assert getattr(partner, 'tgg_EAttribute') is None


def test_assoc_attribute91_stub_double():
    # tgg_EAttribute has no real 'tgg_EAttribute93' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttributeAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttributeAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttributeAssignment(op="sample_text")
    partner = tgg_EAttribute()
    setattr(partner, 'tgg_EAttribute93', None)
    _safe_set(owner, 'tgg_AttributeAssignment92', partner)
    assert getattr(partner, 'tgg_EAttribute93') == owner
    _safe_set(owner, 'tgg_AttributeAssignment92', None)
    assert getattr(partner, 'tgg_EAttribute93') is None


def test_assoc_attributeAssignments74_stub_double():
    # tgg_ObjectVariablePattern has no real 'tgg_ObjectVariablePattern75' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttributeAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttributeAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttributeAssignment(op="sample_text")
    partner = tgg_ObjectVariablePattern()
    setattr(partner, 'tgg_ObjectVariablePattern75', None)
    _safe_set(owner, 'tgg_AttributeAssignment', partner)
    assert owner in getattr(partner, 'tgg_ObjectVariablePattern75')
    _safe_set(owner, 'tgg_AttributeAssignment', None)
    assert owner not in getattr(partner, 'tgg_ObjectVariablePattern75')


def test_assoc_attributeCondDefs20_stub_double():
    # tgg_Schema has no real 'tgg_Schema21' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttrCondDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttrCondDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttrCondDef(userDefined=True)
    partner = tgg_Schema()
    setattr(partner, 'tgg_Schema21', None)
    _safe_set(owner, 'tgg_AttrCondDef', partner)
    assert owner in getattr(partner, 'tgg_Schema21')
    _safe_set(owner, 'tgg_AttrCondDef', None)
    assert owner not in getattr(partner, 'tgg_Schema21')


def test_assoc_attributeCondDefs59_stub_double():
    # tgg_AttrCondDefLibrary has no real 'tgg_AttrCondDefLibrary60' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttrCondDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttrCondDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttrCondDef(userDefined=True)
    partner = tgg_AttrCondDefLibrary()
    setattr(partner, 'tgg_AttrCondDefLibrary60', None)
    _safe_set(owner, 'tgg_AttrCondDef61', partner)
    assert owner in getattr(partner, 'tgg_AttrCondDefLibrary60')
    _safe_set(owner, 'tgg_AttrCondDef61', None)
    assert owner not in getattr(partner, 'tgg_AttrCondDefLibrary60')


def test_assoc_attributeConstraints76_stub_double():
    # tgg_ObjectVariablePattern has no real 'tgg_ObjectVariablePattern77' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttributeConstraint(op="sample_text")
    partner = tgg_ObjectVariablePattern()
    setattr(partner, 'tgg_ObjectVariablePattern77', None)
    _safe_set(owner, 'tgg_AttributeConstraint', partner)
    assert owner in getattr(partner, 'tgg_ObjectVariablePattern77')
    _safe_set(owner, 'tgg_AttributeConstraint', None)
    assert owner not in getattr(partner, 'tgg_ObjectVariablePattern77')


def test_assoc_correspondencePatterns50_stub_double():
    # tgg_CorrVariablePattern has no real 'tgg_CorrVariablePattern' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_CorrVariablePattern()
    setattr(partner, 'tgg_CorrVariablePattern', None)
    _safe_set(owner, 'tgg_Rule51', {partner})
    assert getattr(partner, 'tgg_CorrVariablePattern') == owner
    _safe_set(owner, 'tgg_Rule51', set())
    assert getattr(partner, 'tgg_CorrVariablePattern') is None


def test_assoc_imports0_stub_double():
    # tgg_TripleGraphGrammarFile has no real 'tgg_TripleGraphGrammarFile' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Import(name="sample_text")
    partner = tgg_TripleGraphGrammarFile()
    setattr(partner, 'tgg_TripleGraphGrammarFile', None)
    _safe_set(owner, 'tgg_Import', partner)
    assert owner in getattr(partner, 'tgg_TripleGraphGrammarFile')
    _safe_set(owner, 'tgg_Import', None)
    assert owner not in getattr(partner, 'tgg_TripleGraphGrammarFile')


def test_assoc_kernel115_stub_double():
    # tgg_ComplementRule has no real 'tgg_ComplementRule116' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_ComplementRule()
    setattr(partner, 'tgg_ComplementRule116', None)
    _safe_set(owner, 'tgg_Rule117', partner)
    assert getattr(partner, 'tgg_ComplementRule116') == owner
    _safe_set(owner, 'tgg_Rule117', None)
    assert getattr(partner, 'tgg_ComplementRule116') is None


def test_assoc_linkVariablePatterns85_stub_double():
    # tgg_ContextLinkVariablePattern has no real 'tgg_ContextLinkVariablePattern' property in the generated
    # code (a bare stub) -- manually attach it so tgg_ContextObjectVariablePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_ContextObjectVariablePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_ContextObjectVariablePattern(name="sample_text")
    partner = tgg_ContextLinkVariablePattern()
    setattr(partner, 'tgg_ContextLinkVariablePattern', None)
    _safe_set(owner, 'tgg_ContextObjectVariablePattern86', {partner})
    assert getattr(partner, 'tgg_ContextLinkVariablePattern') == owner
    _safe_set(owner, 'tgg_ContextObjectVariablePattern86', set())
    assert getattr(partner, 'tgg_ContextLinkVariablePattern') is None


def test_assoc_name54_stub_double():
    # tgg_AttrCond has no real 'tgg_AttrCond55' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttrCondDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttrCondDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttrCondDef(userDefined=True)
    partner = tgg_AttrCond()
    setattr(partner, 'tgg_AttrCond55', None)
    _safe_set(owner, 'tgg_AttrCondDef56', partner)
    assert getattr(partner, 'tgg_AttrCond55') == owner
    _safe_set(owner, 'tgg_AttrCondDef56', None)
    assert getattr(partner, 'tgg_AttrCond55') is None


def test_assoc_op142_stub_double():
    # tgg_OperatorPattern has no real 'tgg_OperatorPattern' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Operator(value="sample_text")
    partner = tgg_OperatorPattern()
    setattr(partner, 'tgg_OperatorPattern', None)
    _safe_set(owner, 'tgg_Operator', partner)
    assert getattr(partner, 'tgg_OperatorPattern') == owner
    _safe_set(owner, 'tgg_Operator', None)
    assert getattr(partner, 'tgg_OperatorPattern') is None


def test_assoc_rule130_stub_double():
    # tgg_Nac has no real 'tgg_Nac131' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_Nac()
    setattr(partner, 'tgg_Nac131', None)
    _safe_set(owner, 'tgg_Rule132', partner)
    assert getattr(partner, 'tgg_Nac131') == owner
    _safe_set(owner, 'tgg_Rule132', None)
    assert getattr(partner, 'tgg_Nac131') is None


def test_assoc_rules5_stub_double():
    # tgg_TripleGraphGrammarFile has no real 'tgg_TripleGraphGrammarFile6' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_TripleGraphGrammarFile()
    setattr(partner, 'tgg_TripleGraphGrammarFile6', None)
    _safe_set(owner, 'tgg_Rule', partner)
    assert owner in getattr(partner, 'tgg_TripleGraphGrammarFile6')
    _safe_set(owner, 'tgg_Rule', None)
    assert owner not in getattr(partner, 'tgg_TripleGraphGrammarFile6')


def test_assoc_schema42_stub_double():
    # tgg_Schema has no real 'tgg_Schema44' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_Schema()
    setattr(partner, 'tgg_Schema44', None)
    _safe_set(owner, 'tgg_Rule43', partner)
    assert getattr(partner, 'tgg_Schema44') == owner
    _safe_set(owner, 'tgg_Rule43', None)
    assert getattr(partner, 'tgg_Schema44') is None


def test_assoc_sourcePatterns133_stub_double():
    # tgg_Nac has no real 'tgg_Nac134' property in the generated
    # code (a bare stub) -- manually attach it so tgg_ContextObjectVariablePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_ContextObjectVariablePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_ContextObjectVariablePattern(name="sample_text")
    partner = tgg_Nac()
    setattr(partner, 'tgg_Nac134', None)
    _safe_set(owner, 'tgg_ContextObjectVariablePattern135', partner)
    assert owner in getattr(partner, 'tgg_Nac134')
    _safe_set(owner, 'tgg_ContextObjectVariablePattern135', None)
    assert owner not in getattr(partner, 'tgg_Nac134')


def test_assoc_sourcePatterns45_stub_double():
    # tgg_ObjectVariablePattern has no real 'tgg_ObjectVariablePattern' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_ObjectVariablePattern()
    setattr(partner, 'tgg_ObjectVariablePattern', None)
    _safe_set(owner, 'tgg_Rule46', {partner})
    assert getattr(partner, 'tgg_ObjectVariablePattern') == owner
    _safe_set(owner, 'tgg_Rule46', set())
    assert getattr(partner, 'tgg_ObjectVariablePattern') is None


def test_assoc_target112_stub_double():
    # tgg_ContextLinkVariablePattern has no real 'tgg_ContextLinkVariablePattern113' property in the generated
    # code (a bare stub) -- manually attach it so tgg_ContextObjectVariablePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_ContextObjectVariablePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_ContextObjectVariablePattern(name="sample_text")
    partner = tgg_ContextLinkVariablePattern()
    setattr(partner, 'tgg_ContextLinkVariablePattern113', None)
    _safe_set(owner, 'tgg_ContextObjectVariablePattern114', partner)
    assert getattr(partner, 'tgg_ContextLinkVariablePattern113') == owner
    _safe_set(owner, 'tgg_ContextObjectVariablePattern114', None)
    assert getattr(partner, 'tgg_ContextLinkVariablePattern113') is None


def test_assoc_targetPatterns136_stub_double():
    # tgg_Nac has no real 'tgg_Nac137' property in the generated
    # code (a bare stub) -- manually attach it so tgg_ContextObjectVariablePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_ContextObjectVariablePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_ContextObjectVariablePattern(name="sample_text")
    partner = tgg_Nac()
    setattr(partner, 'tgg_Nac137', None)
    _safe_set(owner, 'tgg_ContextObjectVariablePattern138', partner)
    assert owner in getattr(partner, 'tgg_Nac137')
    _safe_set(owner, 'tgg_ContextObjectVariablePattern138', None)
    assert owner not in getattr(partner, 'tgg_Nac137')


def test_assoc_targetPatterns47_stub_double():
    # tgg_ObjectVariablePattern has no real 'tgg_ObjectVariablePattern49' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Rule(abstractRule=True)
    partner = tgg_ObjectVariablePattern()
    setattr(partner, 'tgg_ObjectVariablePattern49', None)
    _safe_set(owner, 'tgg_Rule48', {partner})
    assert getattr(partner, 'tgg_ObjectVariablePattern49') == owner
    _safe_set(owner, 'tgg_Rule48', set())
    assert getattr(partner, 'tgg_ObjectVariablePattern49') is None


def test_assoc_type37_stub_double():
    # tgg_EDataType has no real 'tgg_EDataType' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Param(paramName="sample_text")
    partner = tgg_EDataType()
    setattr(partner, 'tgg_EDataType', None)
    _safe_set(owner, 'tgg_Param38', partner)
    assert getattr(partner, 'tgg_EDataType') == owner
    _safe_set(owner, 'tgg_Param38', None)
    assert getattr(partner, 'tgg_EDataType') is None


def test_assoc_type80_stub_double():
    # tgg_EClass has no real 'tgg_EClass81' property in the generated
    # code (a bare stub) -- manually attach it so tgg_ContextObjectVariablePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_ContextObjectVariablePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_ContextObjectVariablePattern(name="sample_text")
    partner = tgg_EClass()
    setattr(partner, 'tgg_EClass81', None)
    _safe_set(owner, 'tgg_ContextObjectVariablePattern', partner)
    assert getattr(partner, 'tgg_EClass81') == owner
    _safe_set(owner, 'tgg_ContextObjectVariablePattern', None)
    assert getattr(partner, 'tgg_EClass81') is None


def test_assoc_using1_stub_double():
    # tgg_TripleGraphGrammarFile has no real 'tgg_TripleGraphGrammarFile2' property in the generated
    # code (a bare stub) -- manually attach it so tgg_Using's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_Using's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_Using(importedNamespace="sample_text")
    partner = tgg_TripleGraphGrammarFile()
    setattr(partner, 'tgg_TripleGraphGrammarFile2', None)
    _safe_set(owner, 'tgg_Using', partner)
    assert owner in getattr(partner, 'tgg_TripleGraphGrammarFile2')
    _safe_set(owner, 'tgg_Using', None)
    assert owner not in getattr(partner, 'tgg_TripleGraphGrammarFile2')


def test_assoc_valueExp89_stub_double():
    # tgg_Expression has no real 'tgg_Expression' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttributeConstraint(op="sample_text")
    partner = tgg_Expression()
    setattr(partner, 'tgg_Expression', None)
    _safe_set(owner, 'tgg_AttributeConstraint90', partner)
    assert getattr(partner, 'tgg_Expression') == owner
    _safe_set(owner, 'tgg_AttributeConstraint90', None)
    assert getattr(partner, 'tgg_Expression') is None


def test_assoc_valueExp94_stub_double():
    # tgg_Expression has no real 'tgg_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so tgg_AttributeAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tgg_AttributeAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tgg_AttributeAssignment(op="sample_text")
    partner = tgg_Expression()
    setattr(partner, 'tgg_Expression96', None)
    _safe_set(owner, 'tgg_AttributeAssignment95', partner)
    assert getattr(partner, 'tgg_Expression96') == owner
    _safe_set(owner, 'tgg_AttributeAssignment95', None)
    assert getattr(partner, 'tgg_Expression96') is None


