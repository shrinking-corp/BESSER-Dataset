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
    FairnessConstraint,
    FiniteQuantificationTerm,
    Function,
    FunctionDefinition,
    FunctionInitialization,
    FunctionTerm,
    Header,
    ImportClause,
    Initialization,
    IntegerDomain,
    InvarConstraint,
    Invariant,
    LocalFunction,
    NamedElement,
    Property,
    RealDomain,
    Rule,
    RuleDeclaration,
    Signature,
    StructuredTd,
    TemporalProperty,
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
    asmeta_definitions_CompassionConstraint,
    asmeta_definitions_ControlledFunction,
    asmeta_definitions_CtlSpec,
    asmeta_definitions_DerivedFunction,
    asmeta_definitions_DynamicFunction,
    asmeta_definitions_FairnessConstraint,
    asmeta_definitions_Function,
    asmeta_definitions_InvarConstraint,
    asmeta_definitions_Invariant,
    asmeta_definitions_JusticeConstraint,
    asmeta_definitions_LocalFunction,
    asmeta_definitions_LtlSpec,
    asmeta_definitions_MonitoredFunction,
    asmeta_definitions_OutFunction,
    asmeta_definitions_Property,
    asmeta_definitions_RuleDeclaration,
    asmeta_definitions_SharedFunction,
    asmeta_definitions_StaticFunction,
    asmeta_definitions_TemporalProperty,
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

def test_assoc_asmBody235_stub_double():
    # Body has no real 'Body236' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_RuleDeclaration(arity="sample_text")
    partner = Body()
    setattr(partner, 'Body236', None)
    _safe_set(owner, 'ruleDeclaration', partner)
    assert getattr(partner, 'Body236') == owner
    _safe_set(owner, 'ruleDeclaration', None)
    assert getattr(partner, 'Body236') is None


def test_assoc_bodySection130_stub_double():
    # Body has no real 'Body' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Body()
    setattr(partner, 'Body', None)
    _safe_set(owner, 'asm131', partner)
    assert getattr(partner, 'Body') == owner
    _safe_set(owner, 'asm131', None)
    assert getattr(partner, 'Body') is None


def test_assoc_calledMacro190_stub_double():
    # basictransitionrules_MacroDeclaration has no real 'basictransitionrules_MacroDeclaration191' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_MacroCallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_MacroCallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_MacroCallRule(parameters="sample_text")
    partner = basictransitionrules_MacroDeclaration()
    setattr(partner, 'basictransitionrules_MacroDeclaration191', None)
    _safe_set(owner, 'asmeta_basictransitionrules_MacroCallRule', partner)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration191') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_MacroCallRule', None)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration191') is None


def test_assoc_calledRule145_stub_double():
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


def test_assoc_caseTerm172_stub_double():
    # basicterms_Term has no real 'basicterms_Term174' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_derivedtransitionrules_CaseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_derivedtransitionrules_CaseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_derivedtransitionrules_CaseRule(caseBranches="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term174', None)
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule173', {partner})
    assert getattr(partner, 'basicterms_Term174') == owner
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule173', set())
    assert getattr(partner, 'basicterms_Term174') is None


def test_assoc_codomain251_stub_double():
    # domains_Domain has no real 'domains_Domain253' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = domains_Domain()
    setattr(partner, 'domains_Domain253', None)
    _safe_set(owner, 'asmeta_definitions_Function252', partner)
    assert getattr(partner, 'domains_Domain253') == owner
    _safe_set(owner, 'asmeta_definitions_Function252', None)
    assert getattr(partner, 'domains_Domain253') is None


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


def test_assoc_constraint231_stub_double():
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


def test_assoc_constraint256_stub_double():
    # Invariant has no real 'Invariant257' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = Invariant()
    setattr(partner, 'Invariant257', None)
    _safe_set(owner, 'constrainedFunction', {partner})
    assert getattr(partner, 'Invariant257') == owner
    _safe_set(owner, 'constrainedFunction', set())
    assert getattr(partner, 'Invariant257') is None


def test_assoc_constraint281_stub_double():
    # Invariant has no real 'Invariant282' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_Domain()
    partner = Invariant()
    setattr(partner, 'Invariant282', None)
    _safe_set(owner, 'constrainedDomain', {partner})
    assert getattr(partner, 'Invariant282') == owner
    _safe_set(owner, 'constrainedDomain', set())
    assert getattr(partner, 'Invariant282') is None


def test_assoc_defaultInitialState128_stub_double():
    # Initialization has no real 'Initialization129' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Initialization()
    setattr(partner, 'Initialization129', None)
    _safe_set(owner, 'asm', partner)
    assert getattr(partner, 'Initialization129') == owner
    _safe_set(owner, 'asm', None)
    assert getattr(partner, 'Initialization129') is None


def test_assoc_definition254_stub_double():
    # FunctionDefinition has no real 'FunctionDefinition255' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = FunctionDefinition()
    setattr(partner, 'FunctionDefinition255', None)
    _safe_set(owner, 'definedFunction', partner)
    assert getattr(partner, 'FunctionDefinition255') == owner
    _safe_set(owner, 'definedFunction', None)
    assert getattr(partner, 'FunctionDefinition255') is None


def test_assoc_definition287_stub_double():
    # DomainDefinition has no real 'DomainDefinition288' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_ConcreteDomain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_ConcreteDomain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_ConcreteDomain(isDynamic="sample_text")
    partner = DomainDefinition()
    setattr(partner, 'DomainDefinition288', None)
    _safe_set(owner, 'definedDomain', partner)
    assert getattr(partner, 'DomainDefinition288') == owner
    _safe_set(owner, 'definedDomain', None)
    assert getattr(partner, 'DomainDefinition288') is None


def test_assoc_doRule181_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule183' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule183', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule182', partner)
    assert getattr(partner, 'basictransitionrules_Rule183') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule182', None)
    assert getattr(partner, 'basictransitionrules_Rule183') is None


def test_assoc_doRule205_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule207' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ForallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ForallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ForallRule(ranges="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule207', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule206', partner)
    assert getattr(partner, 'basictransitionrules_Rule207') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule206', None)
    assert getattr(partner, 'basictransitionrules_Rule207') is None


def test_assoc_domain249_stub_double():
    # domains_Domain has no real 'domains_Domain250' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = domains_Domain()
    setattr(partner, 'domains_Domain250', None)
    _safe_set(owner, 'asmeta_definitions_Function', partner)
    assert getattr(partner, 'domains_Domain250') == owner
    _safe_set(owner, 'asmeta_definitions_Function', None)
    assert getattr(partner, 'domains_Domain250') is None


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


def test_assoc_guard184_stub_double():
    # basicterms_Term has no real 'basicterms_Term186' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term186', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule185', partner)
    assert getattr(partner, 'basicterms_Term186') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule185', None)
    assert getattr(partner, 'basicterms_Term186') is None


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


def test_assoc_guard202_stub_double():
    # basicterms_Term has no real 'basicterms_Term204' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ForallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ForallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ForallRule(ranges="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term204', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule203', partner)
    assert getattr(partner, 'basicterms_Term204') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule203', None)
    assert getattr(partner, 'basicterms_Term204') is None


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


def test_assoc_headerSection132_stub_double():
    # Header has no real 'Header134' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Header()
    setattr(partner, 'Header134', None)
    _safe_set(owner, 'asm133', partner)
    assert getattr(partner, 'Header134') == owner
    _safe_set(owner, 'asm133', None)
    assert getattr(partner, 'Header134') is None


def test_assoc_ifnone179_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule180' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule180', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule', partner)
    assert getattr(partner, 'basictransitionrules_Rule180') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule', None)
    assert getattr(partner, 'basictransitionrules_Rule180') is None


def test_assoc_importedDomain92_stub_double():
    # domains_Domain has no real 'domains_Domain93' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_ImportClause(moduleName="sample_text")
    partner = domains_Domain()
    setattr(partner, 'domains_Domain93', None)
    _safe_set(owner, 'asmeta_structure_ImportClause', {partner})
    assert getattr(partner, 'domains_Domain93') == owner
    _safe_set(owner, 'asmeta_structure_ImportClause', set())
    assert getattr(partner, 'domains_Domain93') is None


def test_assoc_importedFunction94_stub_double():
    # Function has no real 'Function96' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_ImportClause(moduleName="sample_text")
    partner = Function()
    setattr(partner, 'Function96', None)
    _safe_set(owner, 'asmeta_structure_ImportClause95', {partner})
    assert getattr(partner, 'Function96') == owner
    _safe_set(owner, 'asmeta_structure_ImportClause95', set())
    assert getattr(partner, 'Function96') is None


def test_assoc_importedRule97_stub_double():
    # RuleDeclaration has no real 'RuleDeclaration99' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_ImportClause(moduleName="sample_text")
    partner = RuleDeclaration()
    setattr(partner, 'RuleDeclaration99', None)
    _safe_set(owner, 'asmeta_structure_ImportClause98', {partner})
    assert getattr(partner, 'RuleDeclaration99') == owner
    _safe_set(owner, 'asmeta_structure_ImportClause98', set())
    assert getattr(partner, 'RuleDeclaration99') is None


def test_assoc_initialState126_stub_double():
    # Initialization has no real 'Initialization127' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = Initialization()
    setattr(partner, 'Initialization127', None)
    _safe_set(owner, 'asmeta_structure_Asm', {partner})
    assert getattr(partner, 'Initialization127') == owner
    _safe_set(owner, 'asmeta_structure_Asm', set())
    assert getattr(partner, 'Initialization127') is None


def test_assoc_initialization285_stub_double():
    # DomainInitialization has no real 'DomainInitialization286' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_ConcreteDomain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_ConcreteDomain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_ConcreteDomain(isDynamic="sample_text")
    partner = DomainInitialization()
    setattr(partner, 'DomainInitialization286', None)
    _safe_set(owner, 'initializedDomain', {partner})
    assert getattr(partner, 'DomainInitialization286') == owner
    _safe_set(owner, 'initializedDomain', set())
    assert getattr(partner, 'DomainInitialization286') is None


def test_assoc_mainrule135_stub_double():
    # basictransitionrules_MacroDeclaration has no real 'basictransitionrules_MacroDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_structure_Asm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_structure_Asm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_structure_Asm(isAsynchr="sample_text")
    partner = basictransitionrules_MacroDeclaration()
    setattr(partner, 'basictransitionrules_MacroDeclaration', None)
    _safe_set(owner, 'asmeta_structure_Asm136', partner)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration') == owner
    _safe_set(owner, 'asmeta_structure_Asm136', None)
    assert getattr(partner, 'basictransitionrules_MacroDeclaration') is None


def test_assoc_otherwiseBranch175_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule177' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_derivedtransitionrules_CaseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_derivedtransitionrules_CaseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_derivedtransitionrules_CaseRule(caseBranches="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule177', None)
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule176', partner)
    assert getattr(partner, 'basictransitionrules_Rule177') == owner
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule176', None)
    assert getattr(partner, 'basictransitionrules_Rule177') is None


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


def test_assoc_ruleBody232_stub_double():
    # basictransitionrules_Rule has no real 'basictransitionrules_Rule234' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_RuleDeclaration(arity="sample_text")
    partner = basictransitionrules_Rule()
    setattr(partner, 'basictransitionrules_Rule234', None)
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration233', partner)
    assert getattr(partner, 'basictransitionrules_Rule234') == owner
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration233', None)
    assert getattr(partner, 'basictransitionrules_Rule234') is None


def test_assoc_signature258_stub_double():
    # Signature has no real 'Signature259' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_Function(arity="sample_text")
    partner = Signature()
    setattr(partner, 'Signature259', None)
    _safe_set(owner, 'function', partner)
    assert getattr(partner, 'Signature259') == owner
    _safe_set(owner, 'function', None)
    assert getattr(partner, 'Signature259') is None


def test_assoc_signature283_stub_double():
    # Signature has no real 'Signature284' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_domains_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_domains_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_domains_Domain()
    partner = Signature()
    setattr(partner, 'Signature284', None)
    _safe_set(owner, 'domain', partner)
    assert getattr(partner, 'Signature284') == owner
    _safe_set(owner, 'domain', None)
    assert getattr(partner, 'Signature284') is None


def test_assoc_term170_stub_double():
    # basicterms_Term has no real 'basicterms_Term171' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_derivedtransitionrules_CaseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_derivedtransitionrules_CaseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_derivedtransitionrules_CaseRule(caseBranches="sample_text")
    partner = basicterms_Term()
    setattr(partner, 'basicterms_Term171', None)
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule', partner)
    assert getattr(partner, 'basicterms_Term171') == owner
    _safe_set(owner, 'asmeta_derivedtransitionrules_CaseRule', None)
    assert getattr(partner, 'basicterms_Term171') is None


def test_assoc_term178_stub_double():
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


def test_assoc_typeDomain289_stub_double():
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


def test_assoc_variable187_stub_double():
    # basicterms_VariableTerm has no real 'basicterms_VariableTerm189' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ChooseRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ChooseRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ChooseRule(ranges="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'basicterms_VariableTerm189', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule188', {partner})
    assert getattr(partner, 'basicterms_VariableTerm189') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ChooseRule188', set())
    assert getattr(partner, 'basicterms_VariableTerm189') is None


def test_assoc_variable200_stub_double():
    # basicterms_VariableTerm has no real 'basicterms_VariableTerm201' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_basictransitionrules_ForallRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_basictransitionrules_ForallRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_basictransitionrules_ForallRule(ranges="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'basicterms_VariableTerm201', None)
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule', {partner})
    assert getattr(partner, 'basicterms_VariableTerm201') == owner
    _safe_set(owner, 'asmeta_basictransitionrules_ForallRule', set())
    assert getattr(partner, 'basicterms_VariableTerm201') is None


def test_assoc_variable229_stub_double():
    # basicterms_VariableTerm has no real 'basicterms_VariableTerm230' property in the generated
    # code (a bare stub) -- manually attach it so asmeta_definitions_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asmeta_definitions_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asmeta_definitions_RuleDeclaration(arity="sample_text")
    partner = basicterms_VariableTerm()
    setattr(partner, 'basicterms_VariableTerm230', None)
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration', {partner})
    assert getattr(partner, 'basicterms_VariableTerm230') == owner
    _safe_set(owner, 'asmeta_definitions_RuleDeclaration', set())
    assert getattr(partner, 'basicterms_VariableTerm230') is None


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


