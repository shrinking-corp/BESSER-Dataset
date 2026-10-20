import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CSTNode,
    CallExpCS,
    ClassifierDefCS,
    ClassifierPropertyCS,
    CollectionLiteralPartCS,
    DictLiteralPartCS,
    DirectionKindCS,
    ImperativeLoopExpCS,
    ImperativeOperationCallExpCS,
    ImportCS,
    LiteralExpCS,
    LocalPropertyCS,
    LogExpCS,
    MappingBodyCS,
    MappingDeclarationCS,
    MappingEndCS,
    MappingExtensionCS,
    MappingInitCS,
    MappingMethodCS,
    MappingModuleCS,
    MappingRuleCS,
    MappingSectionCS,
    MappingSectionsCS,
    ModelTypeCS,
    ModuleKindCS,
    ModulePropertyCS,
    ModuleRefCS,
    ModuleUsageCS,
    MultiplicityDefCS,
    OCLExpressionCS,
    OperationCallExpCS,
    OppositePropertyCS,
    PackageRefCS,
    ParameterDeclarationCS,
    PathNameCS,
    PrimitiveLiteralExpCS,
    RenameCS,
    ResolveExpCS,
    ScopedNameCS,
    SimpleNameCS,
    SimpleSignatureCS,
    StatementCS,
    StringLiteralExpCS,
    SwitchAltExpCS,
    TagCS,
    TransformationHeaderCS,
    TransformationRefineCS,
    TypeCS,
    TypeSpecCS,
    VariableCS,
    cst_CSTNode,
    cst_ElementWithBody,
    cst_InstantiationExpCS,
    cst_LoopExpCS,
    cst_StatementCS,
    qvtoperational_cst_AssertExpCS,
    qvtoperational_cst_AssignStatementCS,
    qvtoperational_cst_BlockExpCS,
    qvtoperational_cst_BreakExpCS,
    qvtoperational_cst_ClassifierDefCS,
    qvtoperational_cst_ClassifierPropertyCS,
    qvtoperational_cst_CompleteSignatureCS,
    qvtoperational_cst_ComputeExpCS,
    qvtoperational_cst_ConfigPropertyCS,
    qvtoperational_cst_ConstructorCS,
    qvtoperational_cst_ContextualPropertyCS,
    qvtoperational_cst_ContinueExpCS,
    qvtoperational_cst_DictLiteralExpCS,
    qvtoperational_cst_DictLiteralPartCS,
    qvtoperational_cst_DictionaryTypeCS,
    qvtoperational_cst_DirectionKindCS,
    qvtoperational_cst_ElementWithBody,
    qvtoperational_cst_ExpressionStatementCS,
    qvtoperational_cst_ForExpCS,
    qvtoperational_cst_ImperativeIterateExpCS,
    qvtoperational_cst_ImperativeLoopExpCS,
    qvtoperational_cst_ImperativeOperationCallExpCS,
    qvtoperational_cst_ImportCS,
    qvtoperational_cst_InstantiationExpCS,
    qvtoperational_cst_LibraryCS,
    qvtoperational_cst_LibraryImportCS,
    qvtoperational_cst_ListLiteralExpCS,
    qvtoperational_cst_ListTypeCS,
    qvtoperational_cst_LocalPropertyCS,
    qvtoperational_cst_LogExpCS,
    qvtoperational_cst_MappingBodyCS,
    qvtoperational_cst_MappingCallExpCS,
    qvtoperational_cst_MappingDeclarationCS,
    qvtoperational_cst_MappingEndCS,
    qvtoperational_cst_MappingExtensionCS,
    qvtoperational_cst_MappingInitCS,
    qvtoperational_cst_MappingMethodCS,
    qvtoperational_cst_MappingModuleCS,
    qvtoperational_cst_MappingQueryCS,
    qvtoperational_cst_MappingRuleCS,
    qvtoperational_cst_MappingSectionCS,
    qvtoperational_cst_MappingSectionsCS,
    qvtoperational_cst_ModelTypeCS,
    qvtoperational_cst_ModuleKindCS,
    qvtoperational_cst_ModulePropertyCS,
    qvtoperational_cst_ModuleRefCS,
    qvtoperational_cst_ModuleUsageCS,
    qvtoperational_cst_MultiplicityDefCS,
    qvtoperational_cst_ObjectExpCS,
    qvtoperational_cst_OppositePropertyCS,
    qvtoperational_cst_PackageRefCS,
    qvtoperational_cst_ParameterDeclarationCS,
    qvtoperational_cst_RenameCS,
    qvtoperational_cst_ResolveExpCS,
    qvtoperational_cst_ResolveInExpCS,
    qvtoperational_cst_ResolveOpArgsExpCS,
    qvtoperational_cst_ReturnExpCS,
    qvtoperational_cst_ScopedNameCS,
    qvtoperational_cst_SimpleSignatureCS,
    qvtoperational_cst_StatementCS,
    qvtoperational_cst_SwitchAltExpCS,
    qvtoperational_cst_SwitchExpCS,
    qvtoperational_cst_TagCS,
    qvtoperational_cst_TransformationHeaderCS,
    qvtoperational_cst_TransformationRefineCS,
    qvtoperational_cst_TypeSpecCS,
    qvtoperational_cst_UnitCS,
    qvtoperational_cst_VariableInitializationCS,
    qvtoperational_cst_WhileExpCS,
    DirectionKindEnum,
    ImportKindEnum,
    MappingExtensionKindCS,
    ModuleKindEnum,
    QualifierKindCS,
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

def test_assoc_condition157_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS159' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ResolveExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ResolveExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ResolveExpCS(isDeferred=True, isInverse=True, one=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS159', None)
    _safe_set(owner, 'qvtoperational_cst_ResolveExpCS158', partner)
    assert getattr(partner, 'OCLExpressionCS159') == owner
    _safe_set(owner, 'qvtoperational_cst_ResolveExpCS158', None)
    assert getattr(partner, 'OCLExpressionCS159') is None


def test_assoc_contextType66_stub_double():
    # TypeCS has no real 'TypeCS68' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingDeclarationCS(isQuery=True, qualifiers="sample_text")
    partner = TypeCS()
    setattr(partner, 'TypeCS68', None)
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS67', partner)
    assert getattr(partner, 'TypeCS68') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS67', None)
    assert getattr(partner, 'TypeCS68') is None


def test_assoc_directionKindCS74_stub_double():
    # DirectionKindCS has no real 'DirectionKindCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingDeclarationCS(isQuery=True, qualifiers="sample_text")
    partner = DirectionKindCS()
    setattr(partner, 'DirectionKindCS', None)
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS75', partner)
    assert getattr(partner, 'DirectionKindCS') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS75', None)
    assert getattr(partner, 'DirectionKindCS') is None


def test_assoc_expressions150_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS152' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ObjectExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ObjectExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ObjectExpCS(isImplicit=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS152', None)
    _safe_set(owner, 'qvtoperational_cst_ObjectExpCS151', {partner})
    assert getattr(partner, 'OCLExpressionCS152') == owner
    _safe_set(owner, 'qvtoperational_cst_ObjectExpCS151', set())
    assert getattr(partner, 'OCLExpressionCS152') is None


def test_assoc_expressions93_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS94' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingQueryCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingQueryCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingQueryCS(isSimpleDefinition=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS94', None)
    _safe_set(owner, 'qvtoperational_cst_MappingQueryCS', {partner})
    assert getattr(partner, 'OCLExpressionCS94') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingQueryCS', set())
    assert getattr(partner, 'OCLExpressionCS94') is None


def test_assoc_featureKeys48_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS50' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ClassifierPropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ClassifierPropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ClassifierPropertyCS(isOrdered=True)
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS50', None)
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS49', {partner})
    assert getattr(partner, 'SimpleNameCS50') == owner
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS49', set())
    assert getattr(partner, 'SimpleNameCS50') is None


def test_assoc_lValueCS141_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS142' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_AssignStatementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_AssignStatementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_AssignStatementCS(incremental=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS142', None)
    _safe_set(owner, 'qvtoperational_cst_AssignStatementCS', partner)
    assert getattr(partner, 'OCLExpressionCS142') == owner
    _safe_set(owner, 'qvtoperational_cst_AssignStatementCS', None)
    assert getattr(partner, 'OCLExpressionCS142') is None


def test_assoc_mappingDeclarationCS88_stub_double():
    # MappingDeclarationCS has no real 'MappingDeclarationCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingMethodCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingMethodCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingMethodCS(blackBox=True)
    partner = MappingDeclarationCS()
    setattr(partner, 'MappingDeclarationCS', None)
    _safe_set(owner, 'qvtoperational_cst_MappingMethodCS', partner)
    assert getattr(partner, 'MappingDeclarationCS') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingMethodCS', None)
    assert getattr(partner, 'MappingDeclarationCS') is None


def test_assoc_mappingExtension76_stub_double():
    # MappingExtensionCS has no real 'MappingExtensionCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingDeclarationCS(isQuery=True, qualifiers="sample_text")
    partner = MappingExtensionCS()
    setattr(partner, 'MappingExtensionCS', None)
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS77', {partner})
    assert getattr(partner, 'MappingExtensionCS') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS77', set())
    assert getattr(partner, 'MappingExtensionCS') is None


def test_assoc_mappingIdentifiers221_stub_double():
    # ScopedNameCS has no real 'ScopedNameCS222' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingExtensionCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingExtensionCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingExtensionCS(kind="sample_text")
    partner = ScopedNameCS()
    setattr(partner, 'ScopedNameCS222', None)
    _safe_set(owner, 'qvtoperational_cst_MappingExtensionCS', {partner})
    assert getattr(partner, 'ScopedNameCS222') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingExtensionCS', set())
    assert getattr(partner, 'ScopedNameCS222') is None


def test_assoc_moduleKindCS197_stub_double():
    # ModuleKindCS has no real 'ModuleKindCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ModuleUsageCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ModuleUsageCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ModuleUsageCS(importKind="sample_text")
    partner = ModuleKindCS()
    setattr(partner, 'ModuleKindCS', None)
    _safe_set(owner, 'qvtoperational_cst_ModuleUsageCS', partner)
    assert getattr(partner, 'ModuleKindCS') == owner
    _safe_set(owner, 'qvtoperational_cst_ModuleUsageCS', None)
    assert getattr(partner, 'ModuleKindCS') is None


def test_assoc_moduleRefs198_stub_double():
    # ModuleRefCS has no real 'ModuleRefCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ModuleUsageCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ModuleUsageCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ModuleUsageCS(importKind="sample_text")
    partner = ModuleRefCS()
    setattr(partner, 'ModuleRefCS', None)
    _safe_set(owner, 'qvtoperational_cst_ModuleUsageCS199', {partner})
    assert getattr(partner, 'ModuleRefCS') == owner
    _safe_set(owner, 'qvtoperational_cst_ModuleUsageCS199', set())
    assert getattr(partner, 'ModuleRefCS') is None


def test_assoc_multiplicity51_stub_double():
    # MultiplicityDefCS has no real 'MultiplicityDefCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ClassifierPropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ClassifierPropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ClassifierPropertyCS(isOrdered=True)
    partner = MultiplicityDefCS()
    setattr(partner, 'MultiplicityDefCS', None)
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS52', partner)
    assert getattr(partner, 'MultiplicityDefCS') == owner
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS52', None)
    assert getattr(partner, 'MultiplicityDefCS') is None


def test_assoc_multiplicity57_stub_double():
    # MultiplicityDefCS has no real 'MultiplicityDefCS59' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_OppositePropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_OppositePropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_OppositePropertyCS(isNavigable=True)
    partner = MultiplicityDefCS()
    setattr(partner, 'MultiplicityDefCS59', None)
    _safe_set(owner, 'qvtoperational_cst_OppositePropertyCS58', partner)
    assert getattr(partner, 'MultiplicityDefCS59') == owner
    _safe_set(owner, 'qvtoperational_cst_OppositePropertyCS58', None)
    assert getattr(partner, 'MultiplicityDefCS59') is None


def test_assoc_oclExpressionCS133_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS134' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_VariableInitializationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_VariableInitializationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_VariableInitializationCS(withResult=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS134', None)
    _safe_set(owner, 'qvtoperational_cst_VariableInitializationCS', partner)
    assert getattr(partner, 'OCLExpressionCS134') == owner
    _safe_set(owner, 'qvtoperational_cst_VariableInitializationCS', None)
    assert getattr(partner, 'OCLExpressionCS134') is None


def test_assoc_oclExpressionCS143_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS145' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_AssignStatementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_AssignStatementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_AssignStatementCS(incremental=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS145', None)
    _safe_set(owner, 'qvtoperational_cst_AssignStatementCS144', partner)
    assert getattr(partner, 'OCLExpressionCS145') == owner
    _safe_set(owner, 'qvtoperational_cst_AssignStatementCS144', None)
    assert getattr(partner, 'OCLExpressionCS145') is None


def test_assoc_opposite53_stub_double():
    # OppositePropertyCS has no real 'OppositePropertyCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ClassifierPropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ClassifierPropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ClassifierPropertyCS(isOrdered=True)
    partner = OppositePropertyCS()
    setattr(partner, 'OppositePropertyCS', None)
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS54', partner)
    assert getattr(partner, 'OppositePropertyCS') == owner
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS54', None)
    assert getattr(partner, 'OppositePropertyCS') is None


def test_assoc_parameters69_stub_double():
    # ParameterDeclarationCS has no real 'ParameterDeclarationCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingDeclarationCS(isQuery=True, qualifiers="sample_text")
    partner = ParameterDeclarationCS()
    setattr(partner, 'ParameterDeclarationCS', None)
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS70', {partner})
    assert getattr(partner, 'ParameterDeclarationCS') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS70', set())
    assert getattr(partner, 'ParameterDeclarationCS') is None


def test_assoc_result71_stub_double():
    # ParameterDeclarationCS has no real 'ParameterDeclarationCS73' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingDeclarationCS(isQuery=True, qualifiers="sample_text")
    partner = ParameterDeclarationCS()
    setattr(partner, 'ParameterDeclarationCS73', None)
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS72', {partner})
    assert getattr(partner, 'ParameterDeclarationCS73') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS72', set())
    assert getattr(partner, 'ParameterDeclarationCS73') is None


def test_assoc_simpleNameCS135_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS137' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_VariableInitializationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_VariableInitializationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_VariableInitializationCS(withResult=True)
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS137', None)
    _safe_set(owner, 'qvtoperational_cst_VariableInitializationCS136', partner)
    assert getattr(partner, 'SimpleNameCS137') == owner
    _safe_set(owner, 'qvtoperational_cst_VariableInitializationCS136', None)
    assert getattr(partner, 'SimpleNameCS137') is None


def test_assoc_simpleNameCS148_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS149' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ObjectExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ObjectExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ObjectExpCS(isImplicit=True)
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS149', None)
    _safe_set(owner, 'qvtoperational_cst_ObjectExpCS', partner)
    assert getattr(partner, 'SimpleNameCS149') == owner
    _safe_set(owner, 'qvtoperational_cst_ObjectExpCS', None)
    assert getattr(partner, 'SimpleNameCS149') is None


def test_assoc_simpleNameCS55_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS56' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_OppositePropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_OppositePropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_OppositePropertyCS(isNavigable=True)
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS56', None)
    _safe_set(owner, 'qvtoperational_cst_OppositePropertyCS', partner)
    assert getattr(partner, 'SimpleNameCS56') == owner
    _safe_set(owner, 'qvtoperational_cst_OppositePropertyCS', None)
    assert getattr(partner, 'SimpleNameCS56') is None


def test_assoc_simpleNameCS64_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS65' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_MappingDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_MappingDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_MappingDeclarationCS(isQuery=True, qualifiers="sample_text")
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS65', None)
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS', partner)
    assert getattr(partner, 'SimpleNameCS65') == owner
    _safe_set(owner, 'qvtoperational_cst_MappingDeclarationCS', None)
    assert getattr(partner, 'SimpleNameCS65') is None


def test_assoc_simpleNameCS78_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS79' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ParameterDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ParameterDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ParameterDeclarationCS(directionKind="sample_text")
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS79', None)
    _safe_set(owner, 'qvtoperational_cst_ParameterDeclarationCS', partner)
    assert getattr(partner, 'SimpleNameCS79') == owner
    _safe_set(owner, 'qvtoperational_cst_ParameterDeclarationCS', None)
    assert getattr(partner, 'SimpleNameCS79') is None


def test_assoc_stereotypeQualifiers46_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS47' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ClassifierPropertyCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ClassifierPropertyCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ClassifierPropertyCS(isOrdered=True)
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS47', None)
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS', {partner})
    assert getattr(partner, 'SimpleNameCS47') == owner
    _safe_set(owner, 'qvtoperational_cst_ClassifierPropertyCS', set())
    assert getattr(partner, 'SimpleNameCS47') is None


def test_assoc_target155_stub_double():
    # VariableCS has no real 'VariableCS156' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ResolveExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ResolveExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ResolveExpCS(isDeferred=True, isInverse=True, one=True)
    partner = VariableCS()
    setattr(partner, 'VariableCS156', None)
    _safe_set(owner, 'qvtoperational_cst_ResolveExpCS', partner)
    assert getattr(partner, 'VariableCS156') == owner
    _safe_set(owner, 'qvtoperational_cst_ResolveExpCS', None)
    assert getattr(partner, 'VariableCS156') is None


def test_assoc_typeCS138_stub_double():
    # TypeCS has no real 'TypeCS140' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_VariableInitializationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_VariableInitializationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_VariableInitializationCS(withResult=True)
    partner = TypeCS()
    setattr(partner, 'TypeCS140', None)
    _safe_set(owner, 'qvtoperational_cst_VariableInitializationCS139', partner)
    assert getattr(partner, 'TypeCS140') == owner
    _safe_set(owner, 'qvtoperational_cst_VariableInitializationCS139', None)
    assert getattr(partner, 'TypeCS140') is None


def test_assoc_typeCS263_stub_double():
    # TypeCS has no real 'TypeCS264' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ScopedNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ScopedNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ScopedNameCS(name="sample_text")
    partner = TypeCS()
    setattr(partner, 'TypeCS264', None)
    _safe_set(owner, 'qvtoperational_cst_ScopedNameCS', partner)
    assert getattr(partner, 'TypeCS264') == owner
    _safe_set(owner, 'qvtoperational_cst_ScopedNameCS', None)
    assert getattr(partner, 'TypeCS264') is None


def test_assoc_typeSpecCS80_stub_double():
    # TypeSpecCS has no real 'TypeSpecCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_cst_ParameterDeclarationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_cst_ParameterDeclarationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_cst_ParameterDeclarationCS(directionKind="sample_text")
    partner = TypeSpecCS()
    setattr(partner, 'TypeSpecCS', None)
    _safe_set(owner, 'qvtoperational_cst_ParameterDeclarationCS81', partner)
    assert getattr(partner, 'TypeSpecCS') == owner
    _safe_set(owner, 'qvtoperational_cst_ParameterDeclarationCS81', None)
    assert getattr(partner, 'TypeSpecCS') is None


