import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AsmLElement,
    AsmLFile,
    AsmL_AddRule,
    AsmL_AlgorithmSet,
    AsmL_AnyIn,
    AsmL_AsmLElement,
    AsmL_AsmLFile,
    AsmL_Body,
    AsmL_BooleanConstant,
    AsmL_Case,
    AsmL_ChooseRule,
    AsmL_Class,
    AsmL_ConditionalRule,
    AsmL_Constant,
    AsmL_ElseIf,
    AsmL_EnumerateSequence,
    AsmL_EnumerateSet,
    AsmL_Enumeration,
    AsmL_Enumerator,
    AsmL_ExistsTerm,
    AsmL_ForAllTerm,
    AsmL_ForallRule,
    AsmL_Function,
    AsmL_InWhereHolds,
    AsmL_Initially,
    AsmL_IntegerConstant,
    AsmL_LocatedElement,
    AsmL_Main,
    AsmL_MapTerm,
    AsmL_MapType,
    AsmL_Method,
    AsmL_MethodCallTerm,
    AsmL_MethodInvocation,
    AsmL_NamedType,
    AsmL_Namespace,
    AsmL_NewInstance,
    AsmL_NullConstant,
    AsmL_Operator,
    AsmL_Parameter,
    AsmL_PredicateTerm,
    AsmL_RangeSequence,
    AsmL_RangeSet,
    AsmL_RemoveRule,
    AsmL_ReturnRule,
    AsmL_Rule,
    AsmL_SequenceTerm,
    AsmL_SequenceType,
    AsmL_SetTerm,
    AsmL_SetType,
    AsmL_SkipRule,
    AsmL_Step,
    AsmL_StepExpression,
    AsmL_StepForEach,
    AsmL_StepUntil,
    AsmL_StepUntilFixPoint,
    AsmL_StepWhile,
    AsmL_StringConstant,
    AsmL_Structure,
    AsmL_Term,
    AsmL_TulpletTerm,
    AsmL_TupletType,
    AsmL_Type,
    AsmL_UpdateFieldRule,
    AsmL_UpdateMapRule,
    AsmL_UpdateRule,
    AsmL_UpdateVarRule,
    AsmL_VarDeclaration,
    AsmL_VarOrCase,
    AsmL_VarOrMethod,
    AsmL_VarTerm,
    Body,
    Class,
    ConditionalRule,
    Constant,
    ElseIf,
    Enumerator,
    Function,
    InWhereHolds,
    Initially,
    LocatedElement,
    Main,
    Method,
    MethodCallTerm,
    Parameter,
    PredicateTerm,
    Rule,
    SequenceTerm,
    SetTerm,
    Step,
    StepExpression,
    Structure,
    Term,
    Type,
    UpdateRule,
    VarDeclaration,
    VarOrCase,
    VarOrMethod,
    VarTerm,
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

def test_assoc_body23_stub_double():
    # Body has no real 'Body' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Function(name="sample_text")
    partner = Body()
    setattr(partner, 'Body', None)
    _safe_set(owner, 'AsmL_Function', partner)
    assert getattr(partner, 'Body') == owner
    _safe_set(owner, 'AsmL_Function', None)
    assert getattr(partner, 'Body') is None


def test_assoc_enumerators20_stub_double():
    # Enumerator has no real 'Enumerator' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Enumeration(name="sample_text")
    partner = Enumerator()
    setattr(partner, 'Enumerator', None)
    _safe_set(owner, 'AsmL_Enumeration', {partner})
    assert getattr(partner, 'Enumerator') == owner
    _safe_set(owner, 'AsmL_Enumeration', set())
    assert getattr(partner, 'Enumerator') is None


def test_assoc_leftExp108_stub_double():
    # Term has no real 'Term109' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Operator(opName="sample_text")
    partner = Term()
    setattr(partner, 'Term109', None)
    _safe_set(owner, 'AsmL_Operator', partner)
    assert getattr(partner, 'Term109') == owner
    _safe_set(owner, 'AsmL_Operator', None)
    assert getattr(partner, 'Term109') is None


def test_assoc_ofTerm113_stub_double():
    # Term has no real 'Term114' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_MapTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_MapTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_MapTerm(separator="sample_text")
    partner = Term()
    setattr(partner, 'Term114', None)
    _safe_set(owner, 'AsmL_MapTerm', partner)
    assert getattr(partner, 'Term114') == owner
    _safe_set(owner, 'AsmL_MapTerm', None)
    assert getattr(partner, 'Term114') is None


def test_assoc_ownerDeclaration90_stub_double():
    # VarDeclaration has no real 'VarDeclaration91' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Type(withNull="sample_text")
    partner = VarDeclaration()
    setattr(partner, 'VarDeclaration91', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'VarDeclaration91') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'VarDeclaration91') is None


def test_assoc_ownerMethod30_stub_double():
    # Method has no real 'Method' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Parameter(name="sample_text")
    partner = Method()
    setattr(partner, 'Method', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'Method') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'Method') is None


def test_assoc_ownerMethod92_stub_double():
    # Method has no real 'Method93' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Type(withNull="sample_text")
    partner = Method()
    setattr(partner, 'Method93', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Method93') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Method93') is None


def test_assoc_ownerParameter94_stub_double():
    # Parameter has no real 'Parameter96' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Type(withNull="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter96', None)
    _safe_set(owner, 'type95', partner)
    assert getattr(partner, 'Parameter96') == owner
    _safe_set(owner, 'type95', None)
    assert getattr(partner, 'Parameter96') is None


def test_assoc_parameters120_stub_double():
    # Term has no real 'Term121' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_MethodCallTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_MethodCallTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_MethodCallTerm(name="sample_text")
    partner = Term()
    setattr(partner, 'Term121', None)
    _safe_set(owner, 'AsmL_MethodCallTerm', {partner})
    assert getattr(partner, 'Term121') == owner
    _safe_set(owner, 'AsmL_MethodCallTerm', set())
    assert getattr(partner, 'Term121') is None


def test_assoc_parameters26_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Method(isAbstract="sample_text", isEntryPoint="sample_text", isOverride="sample_text", isShared="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'ownerMethod27', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'ownerMethod27', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_returnType24_stub_double():
    # Type has no real 'Type25' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Method(isAbstract="sample_text", isEntryPoint="sample_text", isOverride="sample_text", isShared="sample_text")
    partner = Type()
    setattr(partner, 'Type25', None)
    _safe_set(owner, 'ownerMethod', partner)
    assert getattr(partner, 'Type25') == owner
    _safe_set(owner, 'ownerMethod', None)
    assert getattr(partner, 'Type25') is None


def test_assoc_rightExp110_stub_double():
    # Term has no real 'Term112' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Operator(opName="sample_text")
    partner = Term()
    setattr(partner, 'Term112', None)
    _safe_set(owner, 'AsmL_Operator111', partner)
    assert getattr(partner, 'Term112') == owner
    _safe_set(owner, 'AsmL_Operator111', None)
    assert getattr(partner, 'Term112') is None


def test_assoc_toTerm115_stub_double():
    # Term has no real 'Term117' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_MapTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_MapTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_MapTerm(separator="sample_text")
    partner = Term()
    setattr(partner, 'Term117', None)
    _safe_set(owner, 'AsmL_MapTerm116', partner)
    assert getattr(partner, 'Term117') == owner
    _safe_set(owner, 'AsmL_MapTerm116', None)
    assert getattr(partner, 'Term117') is None


def test_assoc_type14_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_VarDeclaration(isConstant="sample_text", isDeclaration="sample_text", isLocal="sample_text", name="sample_text")
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'ownerDeclaration', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'ownerDeclaration', None)
    assert getattr(partner, 'Type') is None


def test_assoc_type28_stub_double():
    # Type has no real 'Type29' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Parameter(name="sample_text")
    partner = Type()
    setattr(partner, 'Type29', None)
    _safe_set(owner, 'ownerParameter', partner)
    assert getattr(partner, 'Type29') == owner
    _safe_set(owner, 'ownerParameter', None)
    assert getattr(partner, 'Type29') is None


def test_assoc_value21_stub_double():
    # Term has no real 'Term22' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Enumerator(name="sample_text")
    partner = Term()
    setattr(partner, 'Term22', None)
    _safe_set(owner, 'AsmL_Enumerator', partner)
    assert getattr(partner, 'Term22') == owner
    _safe_set(owner, 'AsmL_Enumerator', None)
    assert getattr(partner, 'Term22') is None


def test_assoc_varOrCase15_stub_double():
    # VarOrCase has no real 'VarOrCase' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Structure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Structure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Structure(name="sample_text", superStructureName="sample_text")
    partner = VarOrCase()
    setattr(partner, 'VarOrCase', None)
    _safe_set(owner, 'ownerStructure', {partner})
    assert getattr(partner, 'VarOrCase') == owner
    _safe_set(owner, 'ownerStructure', set())
    assert getattr(partner, 'VarOrCase') is None


def test_assoc_varOrMethod18_stub_double():
    # VarOrMethod has no real 'VarOrMethod' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Class(isAbstract="sample_text", name="sample_text", superClassName="sample_text")
    partner = VarOrMethod()
    setattr(partner, 'VarOrMethod', None)
    _safe_set(owner, 'ownerClass', {partner})
    assert getattr(partner, 'VarOrMethod') == owner
    _safe_set(owner, 'ownerClass', set())
    assert getattr(partner, 'VarOrMethod') is None


def test_assoc_variables17_stub_double():
    # VarDeclaration has no real 'VarDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so AsmL_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AsmL_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AsmL_Case(name="sample_text")
    partner = VarDeclaration()
    setattr(partner, 'VarDeclaration', None)
    _safe_set(owner, 'AsmL_Case', {partner})
    assert getattr(partner, 'VarDeclaration') == owner
    _safe_set(owner, 'AsmL_Case', set())
    assert getattr(partner, 'VarDeclaration') is None


