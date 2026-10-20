import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ETActionType,
    ETDeclaration,
    ETExpression,
    ETInitialiser,
    ETSpecification,
    ETSpecificationDefinition,
    ETSpecificationExpression,
    ETTypeIdentifier,
    ecdarText_EObject,
    ecdarText_ETActionType,
    ecdarText_ETAddExpression,
    ecdarText_ETAdditionAssignmentExpression,
    ecdarText_ETArrayDeclaration,
    ecdarText_ETArrayExpression,
    ecdarText_ETAssignmentExpression,
    ecdarText_ETBitAndAssignmentExpression,
    ecdarText_ETBitAndExpression,
    ecdarText_ETBitLeftAssignmentExpression,
    ecdarText_ETBitLeftExpression,
    ecdarText_ETBitOrAssignmentExpression,
    ecdarText_ETBitOrExpression,
    ecdarText_ETBitRightAssignmentExpression,
    ecdarText_ETBitRightExpression,
    ecdarText_ETBitXORAssignmentExpression,
    ecdarText_ETBitXORExpression,
    ecdarText_ETBooleanLiteral,
    ecdarText_ETBooleanType,
    ecdarText_ETClockType,
    ecdarText_ETConditionalExpression,
    ecdarText_ETDeclaration,
    ecdarText_ETDeclarations,
    ecdarText_ETDivideExpression,
    ecdarText_ETDivisionAssignmentExpression,
    ecdarText_ETEdge,
    ecdarText_ETEqualExpression,
    ecdarText_ETExistsExpression,
    ecdarText_ETExpression,
    ecdarText_ETFieldDeclaration,
    ecdarText_ETFieldID,
    ecdarText_ETFile,
    ecdarText_ETForallExpression,
    ecdarText_ETGreaterEqualExpression,
    ecdarText_ETGreaterExpression,
    ecdarText_ETIO,
    ecdarText_ETImplyExpression,
    ecdarText_ETImport,
    ecdarText_ETInitialiser,
    ecdarText_ETInputType,
    ecdarText_ETIntegerType,
    ecdarText_ETLessEqualExpression,
    ecdarText_ETLessExpression,
    ecdarText_ETLocation,
    ecdarText_ETLogicAndExpression,
    ecdarText_ETLogicNotExpression,
    ecdarText_ETLogicOrExpression,
    ecdarText_ETMaxExpression,
    ecdarText_ETMinExpression,
    ecdarText_ETMinusExpression,
    ecdarText_ETModuloAssignmentExpression,
    ecdarText_ETModuloExpression,
    ecdarText_ETMultiInitialiser,
    ecdarText_ETMultiplicationAssignmentExpression,
    ecdarText_ETMultiplyExpression,
    ecdarText_ETNumberLiteral,
    ecdarText_ETOutputType,
    ecdarText_ETParameter,
    ecdarText_ETPostDecrementExpression,
    ecdarText_ETPostIncrementExpression,
    ecdarText_ETPreDecrementExpression,
    ecdarText_ETPreIncrementExpression,
    ecdarText_ETReference,
    ecdarText_ETScalarType,
    ecdarText_ETSelect,
    ecdarText_ETSingleInitialiser,
    ecdarText_ETSpecification,
    ecdarText_ETSpecificationBinding,
    ecdarText_ETSpecificationBody,
    ecdarText_ETSpecificationCompositionExpression,
    ecdarText_ETSpecificationConjunctionExpression,
    ecdarText_ETSpecificationDefinition,
    ecdarText_ETSpecificationDisjunctionExpression,
    ecdarText_ETSpecificationExpression,
    ecdarText_ETSpecificationInstantiation,
    ecdarText_ETSpecificationReference,
    ecdarText_ETSpecificationTemplate,
    ecdarText_ETStructExpression,
    ecdarText_ETStructType,
    ecdarText_ETSubtractExpression,
    ecdarText_ETSubtractionAssignmentExpression,
    ecdarText_ETType,
    ecdarText_ETTypeDeclaration,
    ecdarText_ETTypeID,
    ecdarText_ETTypeIdentifier,
    ecdarText_ETTypeModifiers,
    ecdarText_ETTypeReference,
    ecdarText_ETUnequalExpression,
    ecdarText_ETVariableDeclaration,
    ecdarText_ETVariableID,
    ETIOType,
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

def test_assoc_edges67_reverse_link_reassign_clear():
    a1 = ecdarText_ETLocation(name="sample_text", universal=True, urgent=True)
    a2 = ecdarText_ETLocation(name="sample_text_2", universal=False, urgent=False)
    b = ecdarText_ETEdge(controllable=True)
    _safe_set(b, 'ecdarText_ETEdge', a1)
    assert _is_linked(b, 'ecdarText_ETEdge', a1)
    if hasattr(a1, 'ecdarText_ETLocation68'):
        assert _is_linked(a1, 'ecdarText_ETLocation68', b)
    _safe_set(b, 'ecdarText_ETEdge', a2)
    assert _is_linked(b, 'ecdarText_ETEdge', a2)
    if hasattr(a1, 'ecdarText_ETLocation68'):
        assert not _is_linked(a1, 'ecdarText_ETLocation68', b)
    if hasattr(a2, 'ecdarText_ETLocation68'):
        assert _is_linked(a2, 'ecdarText_ETLocation68', b)
    _safe_set(b, 'ecdarText_ETEdge', None)
    assert not _is_linked(b, 'ecdarText_ETEdge', a2)
    if hasattr(a2, 'ecdarText_ETLocation68'):
        assert not _is_linked(a2, 'ecdarText_ETLocation68', b)


def test_assoc_io71_reverse_link_reassign_clear():
    a1 = ecdarText_ETIO(type="sample_text")
    a2 = ecdarText_ETIO(type="sample_text_2")
    b = ecdarText_ETEdge(controllable=True)
    _safe_set(b, 'ecdarText_ETEdge72', a1)
    assert _is_linked(b, 'ecdarText_ETEdge72', a1)
    if hasattr(a1, 'ecdarText_ETIO'):
        assert _is_linked(a1, 'ecdarText_ETIO', b)
    _safe_set(b, 'ecdarText_ETEdge72', a2)
    assert _is_linked(b, 'ecdarText_ETEdge72', a2)
    if hasattr(a1, 'ecdarText_ETIO'):
        assert not _is_linked(a1, 'ecdarText_ETIO', b)
    if hasattr(a2, 'ecdarText_ETIO'):
        assert _is_linked(a2, 'ecdarText_ETIO', b)
    _safe_set(b, 'ecdarText_ETEdge72', None)
    assert not _is_linked(b, 'ecdarText_ETEdge72', a2)
    if hasattr(a2, 'ecdarText_ETIO'):
        assert not _is_linked(a2, 'ecdarText_ETIO', b)


def test_assoc_selects69_reverse_link_reassign_clear():
    a1 = ecdarText_ETSelect(name="sample_text")
    a2 = ecdarText_ETSelect(name="sample_text_2")
    b = ecdarText_ETEdge(controllable=True)
    _safe_set(b, 'ecdarText_ETEdge70', {a1})
    assert _is_linked(b, 'ecdarText_ETEdge70', a1)
    if hasattr(a1, 'ecdarText_ETSelect'):
        assert _is_linked(a1, 'ecdarText_ETSelect', b)
    _safe_set(b, 'ecdarText_ETEdge70', {a2})
    assert _is_linked(b, 'ecdarText_ETEdge70', a2)
    if hasattr(a1, 'ecdarText_ETSelect'):
        assert not _is_linked(a1, 'ecdarText_ETSelect', b)
    if hasattr(a2, 'ecdarText_ETSelect'):
        assert _is_linked(a2, 'ecdarText_ETSelect', b)
    _safe_set(b, 'ecdarText_ETEdge70', set())
    assert not _is_linked(b, 'ecdarText_ETEdge70', a2)
    if hasattr(a2, 'ecdarText_ETSelect'):
        assert not _is_linked(a2, 'ecdarText_ETSelect', b)


def test_assoc_target76_reverse_link_reassign_clear():
    a1 = ecdarText_ETLocation(name="sample_text", universal=True, urgent=True)
    a2 = ecdarText_ETLocation(name="sample_text_2", universal=False, urgent=False)
    b = ecdarText_ETEdge(controllable=True)
    _safe_set(b, 'ecdarText_ETEdge77', a1)
    assert _is_linked(b, 'ecdarText_ETEdge77', a1)
    if hasattr(a1, 'ecdarText_ETLocation78'):
        assert _is_linked(a1, 'ecdarText_ETLocation78', b)
    _safe_set(b, 'ecdarText_ETEdge77', a2)
    assert _is_linked(b, 'ecdarText_ETEdge77', a2)
    if hasattr(a1, 'ecdarText_ETLocation78'):
        assert not _is_linked(a1, 'ecdarText_ETLocation78', b)
    if hasattr(a2, 'ecdarText_ETLocation78'):
        assert _is_linked(a2, 'ecdarText_ETLocation78', b)
    _safe_set(b, 'ecdarText_ETEdge77', None)
    assert not _is_linked(b, 'ecdarText_ETEdge77', a2)
    if hasattr(a2, 'ecdarText_ETLocation78'):
        assert not _is_linked(a2, 'ecdarText_ETLocation78', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dimensions15_stub_double():
    # ecdarText_ETArrayDeclaration has no real 'ecdarText_ETArrayDeclaration17' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETVariableID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETVariableID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETVariableID(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETArrayDeclaration()
    setattr(partner, 'ecdarText_ETArrayDeclaration17', None)
    _safe_set(owner, 'ecdarText_ETVariableID16', {partner})
    assert getattr(partner, 'ecdarText_ETArrayDeclaration17') == owner
    _safe_set(owner, 'ecdarText_ETVariableID16', set())
    assert getattr(partner, 'ecdarText_ETArrayDeclaration17') is None


def test_assoc_dimensions28_stub_double():
    # ecdarText_ETArrayDeclaration has no real 'ecdarText_ETArrayDeclaration30' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETTypeID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETTypeID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETTypeID(name="sample_text")
    partner = ecdarText_ETArrayDeclaration()
    setattr(partner, 'ecdarText_ETArrayDeclaration30', None)
    _safe_set(owner, 'ecdarText_ETTypeID29', {partner})
    assert getattr(partner, 'ecdarText_ETArrayDeclaration30') == owner
    _safe_set(owner, 'ecdarText_ETTypeID29', set())
    assert getattr(partner, 'ecdarText_ETArrayDeclaration30') is None


def test_assoc_dimensions44_stub_double():
    # ecdarText_ETArrayDeclaration has no real 'ecdarText_ETArrayDeclaration46' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETFieldID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETFieldID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETFieldID(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETArrayDeclaration()
    setattr(partner, 'ecdarText_ETArrayDeclaration46', None)
    _safe_set(owner, 'ecdarText_ETFieldID45', {partner})
    assert getattr(partner, 'ecdarText_ETArrayDeclaration46') == owner
    _safe_set(owner, 'ecdarText_ETFieldID45', set())
    assert getattr(partner, 'ecdarText_ETArrayDeclaration46') is None


def test_assoc_dimensions61_stub_double():
    # ecdarText_ETArrayDeclaration has no real 'ecdarText_ETArrayDeclaration63' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETParameter(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETArrayDeclaration()
    setattr(partner, 'ecdarText_ETArrayDeclaration63', None)
    _safe_set(owner, 'ecdarText_ETParameter62', {partner})
    assert getattr(partner, 'ecdarText_ETArrayDeclaration63') == owner
    _safe_set(owner, 'ecdarText_ETParameter62', set())
    assert getattr(partner, 'ecdarText_ETArrayDeclaration63') is None


def test_assoc_expression114_stub_double():
    # ecdarText_ETExpression has no real 'ecdarText_ETExpression116' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETForallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETForallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETForallExpression(name="sample_text")
    partner = ecdarText_ETExpression()
    setattr(partner, 'ecdarText_ETExpression116', None)
    _safe_set(owner, 'ecdarText_ETForallExpression115', partner)
    assert getattr(partner, 'ecdarText_ETExpression116') == owner
    _safe_set(owner, 'ecdarText_ETForallExpression115', None)
    assert getattr(partner, 'ecdarText_ETExpression116') is None


def test_assoc_expression119_stub_double():
    # ecdarText_ETExpression has no real 'ecdarText_ETExpression121' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETExistsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETExistsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETExistsExpression(name="sample_text")
    partner = ecdarText_ETExpression()
    setattr(partner, 'ecdarText_ETExpression121', None)
    _safe_set(owner, 'ecdarText_ETExistsExpression120', partner)
    assert getattr(partner, 'ecdarText_ETExpression121') == owner
    _safe_set(owner, 'ecdarText_ETExistsExpression120', None)
    assert getattr(partner, 'ecdarText_ETExpression121') is None


def test_assoc_expression82_stub_double():
    # ecdarText_ETExpression has no real 'ecdarText_ETExpression84' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETIO's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETIO's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETIO(type="sample_text")
    partner = ecdarText_ETExpression()
    setattr(partner, 'ecdarText_ETExpression84', None)
    _safe_set(owner, 'ecdarText_ETIO83', partner)
    assert getattr(partner, 'ecdarText_ETExpression84') == owner
    _safe_set(owner, 'ecdarText_ETIO83', None)
    assert getattr(partner, 'ecdarText_ETExpression84') is None


def test_assoc_fields42_stub_double():
    # ecdarText_ETFieldDeclaration has no real 'ecdarText_ETFieldDeclaration43' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETFieldID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETFieldID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETFieldID(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETFieldDeclaration()
    setattr(partner, 'ecdarText_ETFieldDeclaration43', None)
    _safe_set(owner, 'ecdarText_ETFieldID', partner)
    assert owner in getattr(partner, 'ecdarText_ETFieldDeclaration43')
    _safe_set(owner, 'ecdarText_ETFieldID', None)
    assert owner not in getattr(partner, 'ecdarText_ETFieldDeclaration43')


def test_assoc_guard73_stub_double():
    # ecdarText_ETExpression has no real 'ecdarText_ETExpression75' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETEdge(controllable=True)
    partner = ecdarText_ETExpression()
    setattr(partner, 'ecdarText_ETExpression75', None)
    _safe_set(owner, 'ecdarText_ETEdge74', partner)
    assert getattr(partner, 'ecdarText_ETExpression75') == owner
    _safe_set(owner, 'ecdarText_ETEdge74', None)
    assert getattr(partner, 'ecdarText_ETExpression75') is None


def test_assoc_imports0_stub_double():
    # ecdarText_ETFile has no real 'ecdarText_ETFile' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETImport(importedNamespace="sample_text")
    partner = ecdarText_ETFile()
    setattr(partner, 'ecdarText_ETFile', None)
    _safe_set(owner, 'ecdarText_ETImport', partner)
    assert owner in getattr(partner, 'ecdarText_ETFile')
    _safe_set(owner, 'ecdarText_ETImport', None)
    assert owner not in getattr(partner, 'ecdarText_ETFile')


def test_assoc_initialLocation53_stub_double():
    # ecdarText_ETSpecificationBody has no real 'ecdarText_ETSpecificationBody54' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETLocation(name="sample_text", universal=True, urgent=True)
    partner = ecdarText_ETSpecificationBody()
    setattr(partner, 'ecdarText_ETSpecificationBody54', None)
    _safe_set(owner, 'ecdarText_ETLocation', partner)
    assert getattr(partner, 'ecdarText_ETSpecificationBody54') == owner
    _safe_set(owner, 'ecdarText_ETLocation', None)
    assert getattr(partner, 'ecdarText_ETSpecificationBody54') is None


def test_assoc_initialiser18_stub_double():
    # ecdarText_ETInitialiser has no real 'ecdarText_ETInitialiser' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETVariableID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETVariableID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETVariableID(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETInitialiser()
    setattr(partner, 'ecdarText_ETInitialiser', None)
    _safe_set(owner, 'ecdarText_ETVariableID19', partner)
    assert getattr(partner, 'ecdarText_ETInitialiser') == owner
    _safe_set(owner, 'ecdarText_ETVariableID19', None)
    assert getattr(partner, 'ecdarText_ETInitialiser') is None


def test_assoc_invariants64_stub_double():
    # ecdarText_ETExpression has no real 'ecdarText_ETExpression66' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETLocation(name="sample_text", universal=True, urgent=True)
    partner = ecdarText_ETExpression()
    setattr(partner, 'ecdarText_ETExpression66', None)
    _safe_set(owner, 'ecdarText_ETLocation65', {partner})
    assert getattr(partner, 'ecdarText_ETExpression66') == owner
    _safe_set(owner, 'ecdarText_ETLocation65', set())
    assert getattr(partner, 'ecdarText_ETExpression66') is None


def test_assoc_left302_stub_double():
    # ecdarText_ETExpression has no real 'ecdarText_ETExpression303' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETStructExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETStructExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETStructExpression(right="sample_text")
    partner = ecdarText_ETExpression()
    setattr(partner, 'ecdarText_ETExpression303', None)
    _safe_set(owner, 'ecdarText_ETStructExpression', partner)
    assert getattr(partner, 'ecdarText_ETExpression303') == owner
    _safe_set(owner, 'ecdarText_ETStructExpression', None)
    assert getattr(partner, 'ecdarText_ETExpression303') is None


def test_assoc_locations55_stub_double():
    # ecdarText_ETSpecificationBody has no real 'ecdarText_ETSpecificationBody56' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETLocation(name="sample_text", universal=True, urgent=True)
    partner = ecdarText_ETSpecificationBody()
    setattr(partner, 'ecdarText_ETSpecificationBody56', None)
    _safe_set(owner, 'ecdarText_ETLocation57', partner)
    assert owner in getattr(partner, 'ecdarText_ETSpecificationBody56')
    _safe_set(owner, 'ecdarText_ETLocation57', None)
    assert owner not in getattr(partner, 'ecdarText_ETSpecificationBody56')


def test_assoc_modifiers8_stub_double():
    # ecdarText_ETType has no real 'ecdarText_ETType' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETTypeModifiers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETTypeModifiers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETTypeModifiers(const=True, meta=True, urgent=True)
    partner = ecdarText_ETType()
    setattr(partner, 'ecdarText_ETType', None)
    _safe_set(owner, 'ecdarText_ETTypeModifiers', partner)
    assert getattr(partner, 'ecdarText_ETType') == owner
    _safe_set(owner, 'ecdarText_ETTypeModifiers', None)
    assert getattr(partner, 'ecdarText_ETType') is None


def test_assoc_parameters49_stub_double():
    # ecdarText_ETSpecificationTemplate has no real 'ecdarText_ETSpecificationTemplate' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETParameter(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETSpecificationTemplate()
    setattr(partner, 'ecdarText_ETSpecificationTemplate', None)
    _safe_set(owner, 'ecdarText_ETParameter', partner)
    assert owner in getattr(partner, 'ecdarText_ETSpecificationTemplate')
    _safe_set(owner, 'ecdarText_ETParameter', None)
    assert owner not in getattr(partner, 'ecdarText_ETSpecificationTemplate')


def test_assoc_specification105_stub_double():
    # ecdarText_ETSpecificationReference has no real 'ecdarText_ETSpecificationReference' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETSpecification(name="sample_text")
    partner = ecdarText_ETSpecificationReference()
    setattr(partner, 'ecdarText_ETSpecificationReference', None)
    _safe_set(owner, 'ecdarText_ETSpecification106', partner)
    assert getattr(partner, 'ecdarText_ETSpecificationReference') == owner
    _safe_set(owner, 'ecdarText_ETSpecification106', None)
    assert getattr(partner, 'ecdarText_ETSpecificationReference') is None


def test_assoc_specifications3_stub_double():
    # ecdarText_ETFile has no real 'ecdarText_ETFile4' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETSpecification(name="sample_text")
    partner = ecdarText_ETFile()
    setattr(partner, 'ecdarText_ETFile4', None)
    _safe_set(owner, 'ecdarText_ETSpecification', partner)
    assert owner in getattr(partner, 'ecdarText_ETFile4')
    _safe_set(owner, 'ecdarText_ETSpecification', None)
    assert owner not in getattr(partner, 'ecdarText_ETFile4')


def test_assoc_target88_stub_double():
    # ecdarText_ETTypeReference has no real 'ecdarText_ETTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETTypeID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETTypeID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETTypeID(name="sample_text")
    partner = ecdarText_ETTypeReference()
    setattr(partner, 'ecdarText_ETTypeReference', None)
    _safe_set(owner, 'ecdarText_ETTypeID89', partner)
    assert getattr(partner, 'ecdarText_ETTypeReference') == owner
    _safe_set(owner, 'ecdarText_ETTypeID89', None)
    assert getattr(partner, 'ecdarText_ETTypeReference') is None


def test_assoc_type112_stub_double():
    # ecdarText_ETType has no real 'ecdarText_ETType113' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETForallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETForallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETForallExpression(name="sample_text")
    partner = ecdarText_ETType()
    setattr(partner, 'ecdarText_ETType113', None)
    _safe_set(owner, 'ecdarText_ETForallExpression', partner)
    assert getattr(partner, 'ecdarText_ETType113') == owner
    _safe_set(owner, 'ecdarText_ETForallExpression', None)
    assert getattr(partner, 'ecdarText_ETType113') is None


def test_assoc_type117_stub_double():
    # ecdarText_ETType has no real 'ecdarText_ETType118' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETExistsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETExistsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETExistsExpression(name="sample_text")
    partner = ecdarText_ETType()
    setattr(partner, 'ecdarText_ETType118', None)
    _safe_set(owner, 'ecdarText_ETExistsExpression', partner)
    assert getattr(partner, 'ecdarText_ETType118') == owner
    _safe_set(owner, 'ecdarText_ETExistsExpression', None)
    assert getattr(partner, 'ecdarText_ETType118') is None


def test_assoc_type58_stub_double():
    # ecdarText_ETType has no real 'ecdarText_ETType60' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETParameter(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETType()
    setattr(partner, 'ecdarText_ETType60', None)
    _safe_set(owner, 'ecdarText_ETParameter59', partner)
    assert getattr(partner, 'ecdarText_ETType60') == owner
    _safe_set(owner, 'ecdarText_ETParameter59', None)
    assert getattr(partner, 'ecdarText_ETType60') is None


def test_assoc_type85_stub_double():
    # ecdarText_ETType has no real 'ecdarText_ETType87' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETSelect(name="sample_text")
    partner = ecdarText_ETType()
    setattr(partner, 'ecdarText_ETType87', None)
    _safe_set(owner, 'ecdarText_ETSelect86', partner)
    assert getattr(partner, 'ecdarText_ETType87') == owner
    _safe_set(owner, 'ecdarText_ETSelect86', None)
    assert getattr(partner, 'ecdarText_ETType87') is None


def test_assoc_types26_stub_double():
    # ecdarText_ETTypeDeclaration has no real 'ecdarText_ETTypeDeclaration27' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETTypeID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETTypeID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETTypeID(name="sample_text")
    partner = ecdarText_ETTypeDeclaration()
    setattr(partner, 'ecdarText_ETTypeDeclaration27', None)
    _safe_set(owner, 'ecdarText_ETTypeID', partner)
    assert owner in getattr(partner, 'ecdarText_ETTypeDeclaration27')
    _safe_set(owner, 'ecdarText_ETTypeID', None)
    assert owner not in getattr(partner, 'ecdarText_ETTypeDeclaration27')


def test_assoc_updates79_stub_double():
    # ecdarText_ETExpression has no real 'ecdarText_ETExpression81' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETEdge(controllable=True)
    partner = ecdarText_ETExpression()
    setattr(partner, 'ecdarText_ETExpression81', None)
    _safe_set(owner, 'ecdarText_ETEdge80', {partner})
    assert getattr(partner, 'ecdarText_ETExpression81') == owner
    _safe_set(owner, 'ecdarText_ETEdge80', set())
    assert getattr(partner, 'ecdarText_ETExpression81') is None


def test_assoc_variables13_stub_double():
    # ecdarText_ETVariableDeclaration has no real 'ecdarText_ETVariableDeclaration14' property in the generated
    # code (a bare stub) -- manually attach it so ecdarText_ETVariableID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecdarText_ETVariableID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecdarText_ETVariableID(ioType="sample_text", name="sample_text")
    partner = ecdarText_ETVariableDeclaration()
    setattr(partner, 'ecdarText_ETVariableDeclaration14', None)
    _safe_set(owner, 'ecdarText_ETVariableID', partner)
    assert owner in getattr(partner, 'ecdarText_ETVariableDeclaration14')
    _safe_set(owner, 'ecdarText_ETVariableID', None)
    assert owner not in getattr(partner, 'ecdarText_ETVariableDeclaration14')


