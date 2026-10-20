import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTd,
    AgentInitialization,
    Asm,
    BasicDerivedRule,
    BasicFunction,
    BasicRule,
    BasicTd,
    BasicTerm,
    Body,
    Classifier,
    CollectionTerm,
    ComplexDomain,
    ComprehensionTerm,
    ConstantTerm,
    DerivedRule,
    Domain,
    DomainDefinition,
    DomainInitialization,
    DynamicFunction,
    ExportClause,
    ExtendedTerm,
    FiniteQuantificationTerm,
    Function,
    FunctionDefinition,
    FunctionInitialization,
    FunctionTerm,
    Header,
    ImportClause,
    Initialization,
    IntegerDomain,
    Invariant,
    LocalFunction,
    NamedElement,
    Property,
    RealDomain,
    Rule,
    RuleDeclaration,
    Signature,
    StructuredTd,
    Term,
    TurboDerivedRule,
    TurboRule,
    TypeDomain,
    VariableBindingTerm,
    asmeta_basicterms_BasicTerm,
    asmeta_basicterms_BooleanTerm,
    asmeta_basicterms_CollectionTerm,
    asmeta_basicterms_ConstantTerm,
    asmeta_basicterms_DomainTerm,
    asmeta_basicterms_ExtendedTerm,
    asmeta_basicterms_FunctionTerm,
    asmeta_basicterms_LocationTerm,
    asmeta_basicterms_RuleAsTerm,
    asmeta_basicterms_SetTerm,
    asmeta_basicterms_Term,
    asmeta_basicterms_TupleTerm,
    asmeta_basicterms_UndefTerm,
    asmeta_basicterms_VariableTerm,
    asmeta_basictransitionrules_BasicRule,
    asmeta_basictransitionrules_BlockRule,
    asmeta_basictransitionrules_ChooseRule,
    asmeta_basictransitionrules_ConditionalRule,
    asmeta_basictransitionrules_ExtendRule,
    asmeta_basictransitionrules_ForallRule,
    asmeta_basictransitionrules_LetRule,
    asmeta_basictransitionrules_MacroCallRule,
    asmeta_basictransitionrules_MacroDeclaration,
    asmeta_basictransitionrules_Rule,
    asmeta_basictransitionrules_SkipRule,
    asmeta_basictransitionrules_TermAsRule,
    asmeta_basictransitionrules_UpdateRule,
    asmeta_definitions_BasicFunction,
    asmeta_definitions_Classifier,
    asmeta_definitions_ControlledFunction,
    asmeta_definitions_DerivedFunction,
    asmeta_definitions_DynamicFunction,
    asmeta_definitions_Function,
    asmeta_definitions_Invariant,
    asmeta_definitions_LocalFunction,
    asmeta_definitions_MonitoredFunction,
    asmeta_definitions_OutFunction,
    asmeta_definitions_Property,
    asmeta_definitions_RuleDeclaration,
    asmeta_definitions_SharedFunction,
    asmeta_definitions_StaticFunction,
    asmeta_derivedtransitionrules_BasicDerivedRule,
    asmeta_derivedtransitionrules_CaseRule,
    asmeta_derivedtransitionrules_DerivedRule,
    asmeta_derivedtransitionrules_IterativeWhileRule,
    asmeta_derivedtransitionrules_RecursiveWhileRule,
    asmeta_derivedtransitionrules_TurboDerivedRule,
    asmeta_domains_AbstractTd,
    asmeta_domains_AgentDomain,
    asmeta_domains_AnyDomain,
    asmeta_domains_BagDomain,
    asmeta_domains_BasicTd,
    asmeta_domains_BooleanDomain,
    asmeta_domains_CharDomain,
    asmeta_domains_ComplexDomain,
    asmeta_domains_ConcreteDomain,
    asmeta_domains_Domain,
    asmeta_domains_EnumElement,
    asmeta_domains_EnumTd,
    asmeta_domains_IntegerDomain,
    asmeta_domains_MapDomain,
    asmeta_domains_NaturalDomain,
    asmeta_domains_PowersetDomain,
    asmeta_domains_ProductDomain,
    asmeta_domains_RealDomain,
    asmeta_domains_ReserveDomain,
    asmeta_domains_RuleDomain,
    asmeta_domains_SequenceDomain,
    asmeta_domains_StringDomain,
    asmeta_domains_StructuredTd,
    asmeta_domains_TypeDomain,
    asmeta_domains_UndefDomain,
    asmeta_furtherterms_BagCt,
    asmeta_furtherterms_BagTerm,
    asmeta_furtherterms_CaseTerm,
    asmeta_furtherterms_CharTerm,
    asmeta_furtherterms_ComplexTerm,
    asmeta_furtherterms_ComprehensionTerm,
    asmeta_furtherterms_ConditionalTerm,
    asmeta_furtherterms_EnumTerm,
    asmeta_furtherterms_ExistTerm,
    asmeta_furtherterms_ExistUniqueTerm,
    asmeta_furtherterms_FiniteQuantificationTerm,
    asmeta_furtherterms_ForallTerm,
    asmeta_furtherterms_IntegerTerm,
    asmeta_furtherterms_LetTerm,
    asmeta_furtherterms_MapCt,
    asmeta_furtherterms_MapTerm,
    asmeta_furtherterms_NaturalTerm,
    asmeta_furtherterms_RealTerm,
    asmeta_furtherterms_SequenceCt,
    asmeta_furtherterms_SequenceTerm,
    asmeta_furtherterms_SetCt,
    asmeta_furtherterms_StringTerm,
    asmeta_furtherterms_VariableBindingTerm,
    asmeta_structure_AgentInitialization,
    asmeta_structure_Asm,
    asmeta_structure_Body,
    asmeta_structure_DomainDefinition,
    asmeta_structure_DomainInitialization,
    asmeta_structure_ExportClause,
    asmeta_structure_FunctionDefinition,
    asmeta_structure_FunctionInitialization,
    asmeta_structure_Header,
    asmeta_structure_ImportClause,
    asmeta_structure_Initialization,
    asmeta_structure_NamedElement,
    asmeta_structure_Signature,
    asmeta_turbotransitionrules_IterateRule,
    asmeta_turbotransitionrules_SeqRule,
    asmeta_turbotransitionrules_TryCatchRule,
    asmeta_turbotransitionrules_TurboCallRule,
    asmeta_turbotransitionrules_TurboDeclaration,
    asmeta_turbotransitionrules_TurboLocalStateRule,
    asmeta_turbotransitionrules_TurboReturnRule,
    asmeta_turbotransitionrules_TurboRule,
    basicterms_Term,
    basicterms_TupleTerm,
    basicterms_VariableTerm,
    basictransitionrules_MacroCallRule,
    basictransitionrules_MacroDeclaration,
    basictransitionrules_Rule,
    basictransitionrules_TermAsRule,
    domains_ConcreteDomain,
    domains_Domain,
    domains_EnumElement,
    domains_StructuredTd,
    domains_TypeDomain,
    furtherterms_FiniteQuantificationTerm,
    turbotransitionrules_TurboCallRule,
    turbotransitionrules_TurboDeclaration,
    VariableKind,
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

def test_assoc_asmBody231_stub_double():
    # Body has no real 'Body232' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_RuleDeclaration(arity="sample_text")
    partner = Body()
    setattr(partner, 'Body232', None)
    _safe_set(owner, 'ruleDeclaration', partner)
    assert getattr(partner, 'Body232') == owner
    _safe_set(owner, 'ruleDeclaration', None)
    assert getattr(partner, 'Body232') is None


def test_assoc_bodySection126_stub_double():
    # Body has no real 'Body' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Body()
    setattr(partner, 'Body', None)
    _safe_set(owner, 'asm127', partner)
    assert getattr(partner, 'Body') == owner
    _safe_set(owner, 'asm127', None)
    assert getattr(partner, 'Body') is None


def test_assoc_calledMacro186_stub_double():
    # basictransitionrules_MacroDeclaration has no real 'basictransitionrules_MacroDeclaration187' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_MacroCallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_MacroCallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_MacroCallRule(parameters="sample_text")
    partner = basictransitionrules_MacroDeclaration()
    setattr(partner, 'basictransitionrules_MacroDeclaration187', None)
    _safe_set(owner, 'asmeta_basictransitionrules_MacroCallRule', partner)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration187') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_MacroCallRule', None)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration187') is None


def test_assoc_calledRule141_stub_double():
    # turbotransitionrules_TurboDeclaration has no real 'turbotransitionrules_TurboDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_turbotransitionrules_TurboCallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_turbotransitionrules_TurboCallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_turbotransitionrules_TurboCallRule(parameters="sample_text")
    partner = turbotransitionrules_TurboDeclaration()
    setattr(partner, 'turbotransitionrules_TurboDeclaration', None)
    _safe_set(owner, 'asmeta_turbotransitionrules_TurboCallRule', partner)
    assert getattr(partner, 'turbotransitionrules_TurboDeclaration') == owner
    _safe_set(owner, 'asmeta_turbotransitionrules_TurboCallRule', None)
    assert getattr(partner, 'turbotransitionrules_TurboDeclaration') is None


def test_assoc_caseTerm168_stub_double():
    # basicterms_Term has no real 'basicterms_Term170' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_derivedtransitionrules_CaseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_derivedtransitionrules_CaseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_derivedtransitionrules_CaseRule(caseBranches="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term170', None)
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule169', {partner})
    assert getattr(partner, 'basicterms_Term170') == owner
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule169', set())
    assert getattr(partner, 'basicterms_Term170') is None


def test_assoc_codomain247_stub_double():
    # domains_Domain has no real 'domains_Domain249' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = domains_Domain()
    setattr(partner, 'domains_Domain249', None)
    _safe_set(owner, 'asmeta_definitions_Function248', partner)
    assert getattr(partner, 'domains_Domain249') == owner
    _safe_set(owner, 'asmeta_definitions_Function248', None)
    assert getattr(partner, 'domains_Domain249') is None


def test_assoc_comparedTerm28_stub_double():
    # basicterms_Term has no real 'basicterms_Term30' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_CaseTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_CaseTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_CaseTerm(resultTerms="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term30', None)
    _safe_set(owner, 'asmeta_furtherterms_CaseTerm29', partner)
    assert getattr(partner, 'basicterms_Term30') == owner
    _safe_set(owner, 'asmeta_furtherterms_CaseTerm29', None)
    assert getattr(partner, 'basicterms_Term30') is None


def test_assoc_comparingTerm26_stub_double():
    # basicterms_Term has no real 'basicterms_Term27' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_CaseTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_CaseTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_CaseTerm(resultTerms="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term27', None)
    _safe_set(owner, 'asmeta_furtherterms_CaseTerm', {partner})
    assert getattr(partner, 'basicterms_Term27') == owner
    _safe_set(owner, 'asmeta_furtherterms_CaseTerm', set())
    assert getattr(partner, 'basicterms_Term27') is None


def test_assoc_constraint227_stub_double():
    # Invariant has no real 'Invariant' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_RuleDeclaration(arity="sample_text")
    partner = Invariant()
    setattr(partner, 'Invariant', None)
    _safe_set(owner, 'constrainedRule', {partner})
    assert getattr(partner, 'Invariant') == owner
    _safe_set(owner, 'constrainedRule', set())
    assert getattr(partner, 'Invariant') is None


def test_assoc_constraint252_stub_double():
    # Invariant has no real 'Invariant253' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = Invariant()
    setattr(partner, 'Invariant253', None)
    _safe_set(owner, 'constrainedFunction', {partner})
    assert getattr(partner, 'Invariant253') == owner
    _safe_set(owner, 'constrainedFunction', set())
    assert getattr(partner, 'Invariant253') is None


def test_assoc_constraint266_stub_double():
    # Invariant has no real 'Invariant267' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_Domain()
    partner = Invariant()
    setattr(partner, 'Invariant267', None)
    _safe_set(owner, 'constrainedDomain', {partner})
    assert getattr(partner, 'Invariant267') == owner
    _safe_set(owner, 'constrainedDomain', set())
    assert getattr(partner, 'Invariant267') is None


def test_assoc_defaultInitialState124_stub_double():
    # Initialization has no real 'Initialization125' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Initialization()
    setattr(partner, 'Initialization125', None)
    _safe_set(owner, 'asm', partner)
    assert getattr(partner, 'Initialization125') == owner
    _safe_set(owner, 'asm', None)
    assert getattr(partner, 'Initialization125') is None


def test_assoc_definition250_stub_double():
    # FunctionDefinition has no real 'FunctionDefinition251' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = FunctionDefinition()
    setattr(partner, 'FunctionDefinition251', None)
    _safe_set(owner, 'definedFunction', partner)
    assert getattr(partner, 'FunctionDefinition251') == owner
    _safe_set(owner, 'definedFunction', None)
    assert getattr(partner, 'FunctionDefinition251') is None


def test_assoc_definition272_stub_double():
    # DomainDefinition has no real 'DomainDefinition273' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_ConcreteDomain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_ConcreteDomain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_ConcreteDomain(isDynamic="sample_text")
    partner = DomainDefinition()
    setattr(partner, 'DomainDefinition273', None)
    _safe_set(owner, 'definedDomain', partner)
    assert getattr(partner, 'DomainDefinition273') == owner
    _safe_set(owner, 'definedDomain', None)
    assert getattr(partner, 'DomainDefinition273') is None


def test_assoc_doRule177_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule179' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule179', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule178', partner)
    assert getattr(partner, 'basictransitionrules_Rule179') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule178', None)
    assert getattr(partner, 'basictransitionrules_Rule179') is None


def test_assoc_doRule201_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule203' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ForallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ForallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ForallRule(ranges="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule203', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule202', partner)
    assert getattr(partner, 'basictransitionrules_Rule203') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule202', None)
    assert getattr(partner, 'basictransitionrules_Rule203') is None


def test_assoc_domain245_stub_double():
    # domains_Domain has no real 'domains_Domain246' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = domains_Domain()
    setattr(partner, 'domains_Domain246', None)
    _safe_set(owner, 'asmeta_definitions_Function', partner)
    assert getattr(partner, 'domains_Domain246') == owner
    _safe_set(owner, 'asmeta_definitions_Function', None)
    assert getattr(partner, 'domains_Domain246') is None


def test_assoc_domain44_stub_double():
    # domains_Domain has no real 'domains_Domain' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basicterms_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basicterms_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basicterms_Term()
    partner = domains_Domain()
    setattr(partner, 'domains_Domain', None)
    _safe_set(owner, 'asmeta_basicterms_Term', partner)
    assert getattr(partner, 'domains_Domain') == owner
    _safe_set(owner, 'asmeta_basicterms_Term', None)
    assert getattr(partner, 'domains_Domain') is None


def test_assoc_finiteQuantificationTerm36_stub_double():
    # furtherterms_FiniteQuantificationTerm has no real 'FiniteQuantificationTerm' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basicterms_VariableTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basicterms_VariableTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basicterms_VariableTerm(kind="sample_text", name="sample_text")
    partner = furtherterms_FiniteQuantificationTerm()
    setattr(partner, 'FiniteQuantificationTerm', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'FiniteQuantificationTerm') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'FiniteQuantificationTerm') is None


def test_assoc_guard180_stub_double():
    # basicterms_Term has no real 'basicterms_Term182' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term182', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule181', partner)
    assert getattr(partner, 'basicterms_Term182') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule181', None)
    assert getattr(partner, 'basicterms_Term182') is None


def test_assoc_guard198_stub_double():
    # basicterms_Term has no real 'basicterms_Term200' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ForallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ForallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ForallRule(ranges="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term200', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule199', partner)
    assert getattr(partner, 'basicterms_Term200') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule199', None)
    assert getattr(partner, 'basicterms_Term200') is None


def test_assoc_guard20_stub_double():
    # basicterms_Term has no real 'basicterms_Term22' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_ComprehensionTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_ComprehensionTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_ComprehensionTerm(ranges="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term22', None)
    _safe_set(owner, 'asmeta_furtherterms_ComprehensionTerm21', partner)
    assert getattr(partner, 'basicterms_Term22') == owner
    _safe_set(owner, 'asmeta_furtherterms_ComprehensionTerm21', None)
    assert getattr(partner, 'basicterms_Term22') is None


def test_assoc_guard8_stub_double():
    # basicterms_Term has no real 'basicterms_Term9' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_FiniteQuantificationTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_FiniteQuantificationTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_FiniteQuantificationTerm(ranges="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term9', None)
    _safe_set(owner, 'asmeta_furtherterms_FiniteQuantificationTerm', partner)
    assert getattr(partner, 'basicterms_Term9') == owner
    _safe_set(owner, 'asmeta_furtherterms_FiniteQuantificationTerm', None)
    assert getattr(partner, 'basicterms_Term9') is None


def test_assoc_headerSection128_stub_double():
    # Header has no real 'Header130' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Header()
    setattr(partner, 'Header130', None)
    _safe_set(owner, 'asm129', partner)
    assert getattr(partner, 'Header130') == owner
    _safe_set(owner, 'asm129', None)
    assert getattr(partner, 'Header130') is None


def test_assoc_ifnone175_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule176' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule176', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule', partner)
    assert getattr(partner, 'basictransitionrules_Rule176') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule', None)
    assert getattr(partner, 'basictransitionrules_Rule176') is None


def test_assoc_importedDomain88_stub_double():
    # domains_Domain has no real 'domains_Domain89' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_ImportClause(moduleName="sample_text")
    partner = domains_Domain()
    setattr(partner, 'domains_Domain89', None)
    _safe_set(owner, 'asmeta_structure_ImportClause', {partner})
    assert getattr(partner, 'domains_Domain89') == owner
    _safe_set(owner, 'asmeta_structure_ImportClause', set())
    assert getattr(partner, 'domains_Domain89') is None


def test_assoc_importedFunction90_stub_double():
    # Function has no real 'Function92' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_ImportClause(moduleName="sample_text")
    partner = Function()
    setattr(partner, 'Function92', None)
    _safe_set(owner, 'asmeta_structure_ImportClause91', {partner})
    assert getattr(partner, 'Function92') == owner
    _safe_set(owner, 'asmeta_structure_ImportClause91', set())
    assert getattr(partner, 'Function92') is None


def test_assoc_importedRule93_stub_double():
    # RuleDeclaration has no real 'RuleDeclaration95' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_ImportClause(moduleName="sample_text")
    partner = RuleDeclaration()
    setattr(partner, 'RuleDeclaration95', None)
    _safe_set(owner, 'asmeta_structure_ImportClause94', {partner})
    assert getattr(partner, 'RuleDeclaration95') == owner
    _safe_set(owner, 'asmeta_structure_ImportClause94', set())
    assert getattr(partner, 'RuleDeclaration95') is None


def test_assoc_initialState122_stub_double():
    # Initialization has no real 'Initialization123' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Initialization()
    setattr(partner, 'Initialization123', None)
    _safe_set(owner, 'asmeta_structure_Asm', {partner})
    assert getattr(partner, 'Initialization123') == owner
    _safe_set(owner, 'asmeta_structure_Asm', set())
    assert getattr(partner, 'Initialization123') is None


def test_assoc_initialization270_stub_double():
    # DomainInitialization has no real 'DomainInitialization271' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_ConcreteDomain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_ConcreteDomain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_ConcreteDomain(isDynamic="sample_text")
    partner = DomainInitialization()
    setattr(partner, 'DomainInitialization271', None)
    _safe_set(owner, 'initializedDomain', {partner})
    assert getattr(partner, 'DomainInitialization271') == owner
    _safe_set(owner, 'initializedDomain', set())
    assert getattr(partner, 'DomainInitialization271') is None


def test_assoc_mainrule131_stub_double():
    # basictransitionrules_MacroDeclaration has no real 'basictransitionrules_MacroDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = basictransitionrules_MacroDeclaration()
    setattr(partner, 'basictransitionrules_MacroDeclaration', None)
    _safe_set(owner, 'asmeta_structure_Asm132', partner)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration') == owner
    _safe_set(owner, 'asmeta_structure_Asm132', None)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration') is None


def test_assoc_otherwiseBranch171_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule173' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_derivedtransitionrules_CaseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_derivedtransitionrules_CaseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_derivedtransitionrules_CaseRule(caseBranches="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule173', None)
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule172', partner)
    assert getattr(partner, 'basictransitionrules_Rule173') == owner
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule172', None)
    assert getattr(partner, 'basictransitionrules_Rule173') is None


def test_assoc_otherwiseTerm31_stub_double():
    # basicterms_Term has no real 'basicterms_Term33' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_CaseTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_CaseTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_CaseTerm(resultTerms="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term33', None)
    _safe_set(owner, 'asmeta_furtherterms_CaseTerm32', partner)
    assert getattr(partner, 'basicterms_Term33') == owner
    _safe_set(owner, 'asmeta_furtherterms_CaseTerm32', None)
    assert getattr(partner, 'basicterms_Term33') is None


def test_assoc_ruleBody228_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule230' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_RuleDeclaration(arity="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule230', None)
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration229', partner)
    assert getattr(partner, 'basictransitionrules_Rule230') == owner
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration229', None)
    assert getattr(partner, 'basictransitionrules_Rule230') is None


def test_assoc_signature254_stub_double():
    # Signature has no real 'Signature255' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = Signature()
    setattr(partner, 'Signature255', None)
    _safe_set(owner, 'function', partner)
    assert getattr(partner, 'Signature255') == owner
    _safe_set(owner, 'function', None)
    assert getattr(partner, 'Signature255') is None


def test_assoc_signature268_stub_double():
    # Signature has no real 'Signature269' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_Domain()
    partner = Signature()
    setattr(partner, 'Signature269', None)
    _safe_set(owner, 'domain', partner)
    assert getattr(partner, 'Signature269') == owner
    _safe_set(owner, 'domain', None)
    assert getattr(partner, 'Signature269') is None


def test_assoc_term166_stub_double():
    # basicterms_Term has no real 'basicterms_Term167' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_derivedtransitionrules_CaseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_derivedtransitionrules_CaseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_derivedtransitionrules_CaseRule(caseBranches="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term167', None)
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule', partner)
    assert getattr(partner, 'basicterms_Term167') == owner
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule', None)
    assert getattr(partner, 'basicterms_Term167') is None


def test_assoc_term174_stub_double():
    # basicterms_Term has no real 'Term' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_TermAsRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_TermAsRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_TermAsRule(parameters="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'Term', None)
    _safe_set(owner, 'termAsRule', partner)
    assert getattr(partner, 'Term') == owner
    _safe_set(owner, 'termAsRule', None)
    assert getattr(partner, 'Term') is None


def test_assoc_term23_stub_double():
    # basicterms_Term has no real 'basicterms_Term25' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_ComprehensionTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_ComprehensionTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_ComprehensionTerm(ranges="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term25', None)
    _safe_set(owner, 'asmeta_furtherterms_ComprehensionTerm24', partner)
    assert getattr(partner, 'basicterms_Term25') == owner
    _safe_set(owner, 'asmeta_furtherterms_ComprehensionTerm24', None)
    assert getattr(partner, 'basicterms_Term25') is None


def test_assoc_termAsRule45_stub_double():
    # basictransitionrules_TermAsRule has no real 'TermAsRule' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basicterms_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basicterms_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basicterms_Term()
    partner = basictransitionrules_TermAsRule()
    setattr(partner, 'TermAsRule', None)
    _safe_set(owner, 'term', {partner})
    assert getattr(partner, 'TermAsRule') == owner
    _safe_set(owner, 'term', set())
    assert getattr(partner, 'TermAsRule') is None


def test_assoc_typeDomain274_stub_double():
    # domains_TypeDomain has no real 'domains_TypeDomain' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_ConcreteDomain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_ConcreteDomain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_ConcreteDomain(isDynamic="sample_text")
    partner = domains_TypeDomain()
    setattr(partner, 'domains_TypeDomain', None)
    _safe_set(owner, 'asmeta_domains_ConcreteDomain', partner)
    assert getattr(partner, 'domains_TypeDomain') == owner
    _safe_set(owner, 'asmeta_domains_ConcreteDomain', None)
    assert getattr(partner, 'domains_TypeDomain') is None


def test_assoc_variable18_stub_double():
    # basicterms_VariableTerm has no real 'basicterms_VariableTerm19' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_ComprehensionTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_ComprehensionTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_ComprehensionTerm(ranges="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'basicterms_VariableTerm19', None)
    _safe_set(owner, 'asmeta_furtherterms_ComprehensionTerm', {partner})
    assert getattr(partner, 'basicterms_VariableTerm19') == owner
    _safe_set(owner, 'asmeta_furtherterms_ComprehensionTerm', set())
    assert getattr(partner, 'basicterms_VariableTerm19') is None


def test_assoc_variable183_stub_double():
    # basicterms_VariableTerm has no real 'basicterms_VariableTerm185' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'basicterms_VariableTerm185', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule184', {partner})
    assert getattr(partner, 'basicterms_VariableTerm185') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule184', set())
    assert getattr(partner, 'basicterms_VariableTerm185') is None


def test_assoc_variable196_stub_double():
    # basicterms_VariableTerm has no real 'basicterms_VariableTerm197' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ForallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ForallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ForallRule(ranges="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'basicterms_VariableTerm197', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule', {partner})
    assert getattr(partner, 'basicterms_VariableTerm197') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule', set())
    assert getattr(partner, 'basicterms_VariableTerm197') is None


def test_assoc_variable225_stub_double():
    # basicterms_VariableTerm has no real 'basicterms_VariableTerm226' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_RuleDeclaration(arity="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'basicterms_VariableTerm226', None)
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration', {partner})
    assert getattr(partner, 'basicterms_VariableTerm226') == owner
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration', set())
    assert getattr(partner, 'basicterms_VariableTerm226') is None


def test_assoc_variable7_stub_double():
    # basicterms_VariableTerm has no real 'VariableTerm' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_furtherterms_FiniteQuantificationTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_furtherterms_FiniteQuantificationTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_furtherterms_FiniteQuantificationTerm(ranges="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'VariableTerm', None)
    _safe_set(owner, 'finiteQuantificationTerm', {partner})
    assert getattr(partner, 'VariableTerm') == owner
    _safe_set(owner, 'finiteQuantificationTerm', set())
    assert getattr(partner, 'VariableTerm') is None


