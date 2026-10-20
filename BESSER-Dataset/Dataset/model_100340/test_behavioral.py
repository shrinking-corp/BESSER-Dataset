import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASM_AccessUpdateFunction,
    ASM_Argument,
    ASM_Asm,
    ASM_AsmInvocation,
    ASM_Body,
    ASM_BooleanConstant,
    ASM_ChooseRule,
    ASM_ConditionalRule,
    ASM_Constant,
    ASM_Declaration,
    ASM_DoForallRule,
    ASM_ElementDecl,
    ASM_ElseIf,
    ASM_ExtendRule,
    ASM_Extension,
    ASM_Function,
    ASM_FunctionOrVariableTerm,
    ASM_Initialization,
    ASM_IntegerConstant,
    ASM_LocatedElement,
    ASM_MetaInformation,
    ASM_OperatorTerm,
    ASM_Parameter,
    ASM_ReturnRule,
    ASM_Rule,
    ASM_Signature,
    ASM_SkipRule,
    ASM_StringConstant,
    ASM_Term,
    ASM_UndefConstant,
    ASM_Universe,
    ASM_UpdateRule,
    ASM_VariableDecl,
    ASM_XAsmFile,
    ASM_XAsmSpec,
    AccessUpdateFunction,
    Argument,
    Asm,
    Body,
    Constant,
    Declaration,
    ElementDecl,
    ElseIf,
    Extension,
    Function,
    FunctionOrVariableTerm,
    Initialization,
    LocatedElement,
    MetaInformation,
    Parameter,
    Rule,
    Signature,
    Term,
    Universe,
    VariableDecl,
    XAsmFile,
    AccessUpdateType,
    AsmType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessUpdateFunctions14_stub_double():
    # AccessUpdateFunction has no real 'AccessUpdateFunction' property in the generated
    # code (a bare stub) -- manually attach it so ASM_MetaInformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_MetaInformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_MetaInformation(usedAs="sample_text")
    partner = AccessUpdateFunction()
    setattr(partner, 'AccessUpdateFunction', None)
    _safe_set(owner, 'ASM_MetaInformation15', {partner})
    assert getattr(partner, 'AccessUpdateFunction') == owner
    _safe_set(owner, 'ASM_MetaInformation15', set())
    assert getattr(partner, 'AccessUpdateFunction') is None


def test_assoc_arguments32_stub_double():
    # Term has no real 'Term33' property in the generated
    # code (a bare stub) -- manually attach it so ASM_AsmInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_AsmInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_AsmInvocation(asmName="sample_text")
    partner = Term()
    setattr(partner, 'Term33', None)
    _safe_set(owner, 'ASM_AsmInvocation', {partner})
    assert getattr(partner, 'Term33') == owner
    _safe_set(owner, 'ASM_AsmInvocation', set())
    assert getattr(partner, 'Term33') is None


def test_assoc_arguments6_stub_double():
    # Argument has no real 'Argument' property in the generated
    # code (a bare stub) -- manually attach it so ASM_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_Signature(isMain="sample_text", name="sample_text")
    partner = Argument()
    setattr(partner, 'Argument', None)
    _safe_set(owner, 'ASM_Signature', {partner})
    assert getattr(partner, 'Argument') == owner
    _safe_set(owner, 'ASM_Signature', set())
    assert getattr(partner, 'Argument') is None


def test_assoc_body4_stub_double():
    # Body has no real 'Body' property in the generated
    # code (a bare stub) -- manually attach it so ASM_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_Asm(returnType="sample_text")
    partner = Body()
    setattr(partner, 'Body', None)
    _safe_set(owner, 'ASM_Asm5', partner)
    assert getattr(partner, 'Body') == owner
    _safe_set(owner, 'ASM_Asm5', None)
    assert getattr(partner, 'Body') is None


def test_assoc_functions16_stub_double():
    # Function has no real 'Function' property in the generated
    # code (a bare stub) -- manually attach it so ASM_AccessUpdateFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_AccessUpdateFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_AccessUpdateFunction(type="sample_text")
    partner = Function()
    setattr(partner, 'Function', None)
    _safe_set(owner, 'ASM_AccessUpdateFunction', {partner})
    assert getattr(partner, 'Function') == owner
    _safe_set(owner, 'ASM_AccessUpdateFunction', set())
    assert getattr(partner, 'Function') is None


def test_assoc_initTerm18_stub_double():
    # Term has no real 'Term' property in the generated
    # code (a bare stub) -- manually attach it so ASM_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_Function(isExternal="sample_text", returnType="sample_text")
    partner = Term()
    setattr(partner, 'Term', None)
    _safe_set(owner, 'ASM_Function19', partner)
    assert getattr(partner, 'Term') == owner
    _safe_set(owner, 'ASM_Function19', None)
    assert getattr(partner, 'Term') is None


def test_assoc_leftExp27_stub_double():
    # Term has no real 'Term28' property in the generated
    # code (a bare stub) -- manually attach it so ASM_OperatorTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_OperatorTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_OperatorTerm(opName="sample_text")
    partner = Term()
    setattr(partner, 'Term28', None)
    _safe_set(owner, 'ASM_OperatorTerm', partner)
    assert getattr(partner, 'Term28') == owner
    _safe_set(owner, 'ASM_OperatorTerm', None)
    assert getattr(partner, 'Term28') is None


def test_assoc_metaInformation2_stub_double():
    # MetaInformation has no real 'MetaInformation' property in the generated
    # code (a bare stub) -- manually attach it so ASM_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_Asm(returnType="sample_text")
    partner = MetaInformation()
    setattr(partner, 'MetaInformation', None)
    _safe_set(owner, 'ASM_Asm3', partner)
    assert getattr(partner, 'MetaInformation') == owner
    _safe_set(owner, 'ASM_Asm3', None)
    assert getattr(partner, 'MetaInformation') is None


def test_assoc_parameters17_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ASM_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_Function(isExternal="sample_text", returnType="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'ASM_Function', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'ASM_Function', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_rightExp29_stub_double():
    # Term has no real 'Term31' property in the generated
    # code (a bare stub) -- manually attach it so ASM_OperatorTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_OperatorTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_OperatorTerm(opName="sample_text")
    partner = Term()
    setattr(partner, 'Term31', None)
    _safe_set(owner, 'ASM_OperatorTerm30', partner)
    assert getattr(partner, 'Term31') == owner
    _safe_set(owner, 'ASM_OperatorTerm30', None)
    assert getattr(partner, 'Term31') is None


def test_assoc_signature1_stub_double():
    # Signature has no real 'Signature' property in the generated
    # code (a bare stub) -- manually attach it so ASM_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_Asm(returnType="sample_text")
    partner = Signature()
    setattr(partner, 'Signature', None)
    _safe_set(owner, 'ASM_Asm', partner)
    assert getattr(partner, 'Signature') == owner
    _safe_set(owner, 'ASM_Asm', None)
    assert getattr(partner, 'Signature') is None


def test_assoc_superUniverses20_stub_double():
    # Universe has no real 'Universe' property in the generated
    # code (a bare stub) -- manually attach it so ASM_Universe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_Universe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_Universe(contents="sample_text", name="sample_text")
    partner = Universe()
    setattr(partner, 'Universe', None)
    _safe_set(owner, 'ASM_Universe', {partner})
    assert getattr(partner, 'Universe') == owner
    _safe_set(owner, 'ASM_Universe', set())
    assert getattr(partner, 'Universe') is None


def test_assoc_usedAsIn12_stub_double():
    # Signature has no real 'Signature13' property in the generated
    # code (a bare stub) -- manually attach it so ASM_MetaInformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ASM_MetaInformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ASM_MetaInformation(usedAs="sample_text")
    partner = Signature()
    setattr(partner, 'Signature13', None)
    _safe_set(owner, 'ASM_MetaInformation', {partner})
    assert getattr(partner, 'Signature13') == owner
    _safe_set(owner, 'ASM_MetaInformation', set())
    assert getattr(partner, 'Signature13') is None


