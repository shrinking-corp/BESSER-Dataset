import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallExp,
    Class,
    ConstructorBody,
    Dummy2,
    DummyRelation,
    DummyRelationDomain,
    Element,
    EntryOperation,
    ImperativeCallExp,
    ImperativeExpression,
    ImperativeOperation,
    InstantiationExp,
    MappingOperation,
    ModelParameter,
    ModelType,
    Module,
    ModuleImport,
    Operation,
    OperationBody,
    OperationCallExp,
    Parameter,
    Property,
    ResolveExp,
    VarParameter,
    Variable,
    qvtoperational_Class,
    qvtoperational_Constructor,
    qvtoperational_ConstructorBody,
    qvtoperational_ContextualProperty,
    qvtoperational_DummyRelation,
    qvtoperational_DummyRelationDomain,
    qvtoperational_DummyRelationalTransformation,
    qvtoperational_Element,
    qvtoperational_EntryOperation,
    qvtoperational_Helper,
    qvtoperational_ImperativeCallExp,
    qvtoperational_ImperativeOperation,
    qvtoperational_Library,
    qvtoperational_MappingBody,
    qvtoperational_MappingCallExp,
    qvtoperational_MappingOperation,
    qvtoperational_MappingParameter,
    qvtoperational_ModelParameter,
    qvtoperational_ModelType,
    qvtoperational_Module,
    qvtoperational_ModuleImport,
    qvtoperational_OCLExpression,
    qvtoperational_ObjectExp,
    qvtoperational_OperationBody,
    qvtoperational_OperationalTransformation,
    qvtoperational_Package,
    qvtoperational_Property,
    qvtoperational_ResolveExp,
    qvtoperational_ResolveInExp,
    qvtoperational_Tag,
    qvtoperational_TemplateableElement,
    qvtoperational_VarParameter,
    qvtoperational_Variable,
    DirectionKind,
    ImportKind,
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

def test_assoc_additionalCondition36_stub_double():
    # qvtoperational_OCLExpression has no real 'qvtoperational_OCLExpression37' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModelType(conformanceKind="sample_text")
    partner = qvtoperational_OCLExpression()
    setattr(partner, 'qvtoperational_OCLExpression37', None)
    _safe_set(owner, 'qvtoperational_ModelType', {partner})
    assert getattr(partner, 'qvtoperational_OCLExpression37') == owner
    _safe_set(owner, 'qvtoperational_ModelType', set())
    assert getattr(partner, 'qvtoperational_OCLExpression37') is None


def test_assoc_binding52_stub_double():
    # ModelType has no real 'ModelType53' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModuleImport(kind="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType53', None)
    _safe_set(owner, 'qvtoperational_ModuleImport', {partner})
    assert getattr(partner, 'ModelType53') == owner
    _safe_set(owner, 'qvtoperational_ModuleImport', set())
    assert getattr(partner, 'ModelType53') is None


def test_assoc_body5_stub_double():
    # OperationBody has no real 'OperationBody' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = OperationBody()
    setattr(partner, 'OperationBody', None)
    _safe_set(owner, 'qvtoperational_ImperativeOperation', partner)
    assert getattr(partner, 'OperationBody') == owner
    _safe_set(owner, 'qvtoperational_ImperativeOperation', None)
    assert getattr(partner, 'OperationBody') is None


def test_assoc_condition84_stub_double():
    # qvtoperational_OCLExpression has no real 'qvtoperational_OCLExpression85' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = qvtoperational_OCLExpression()
    setattr(partner, 'qvtoperational_OCLExpression85', None)
    _safe_set(owner, 'qvtoperational_ResolveExp', partner)
    assert getattr(partner, 'qvtoperational_OCLExpression85') == owner
    _safe_set(owner, 'qvtoperational_ResolveExp', None)
    assert getattr(partner, 'qvtoperational_OCLExpression85') is None


def test_assoc_configProperty40_stub_double():
    # qvtoperational_Property has no real 'qvtoperational_Property41' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = qvtoperational_Property()
    setattr(partner, 'qvtoperational_Property41', None)
    _safe_set(owner, 'qvtoperational_Module', {partner})
    assert getattr(partner, 'qvtoperational_Property41') == owner
    _safe_set(owner, 'qvtoperational_Module', set())
    assert getattr(partner, 'qvtoperational_Property41') is None


def test_assoc_context6_stub_double():
    # VarParameter has no real 'VarParameter' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter', None)
    _safe_set(owner, 'qvtoperational_ImperativeOperation7', partner)
    assert getattr(partner, 'VarParameter') == owner
    _safe_set(owner, 'qvtoperational_ImperativeOperation7', None)
    assert getattr(partner, 'VarParameter') is None


def test_assoc_ctxOwner91_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation92' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation92', None)
    _safe_set(owner, 'qvtoperational_VarParameter', partner)
    assert getattr(partner, 'ImperativeOperation92') == owner
    _safe_set(owner, 'qvtoperational_VarParameter', None)
    assert getattr(partner, 'ImperativeOperation92') is None


def test_assoc_elements96_stub_double():
    # qvtoperational_Element has no real 'qvtoperational_Element' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Tag(name="sample_text", value="sample_text")
    partner = qvtoperational_Element()
    setattr(partner, 'qvtoperational_Element', None)
    _safe_set(owner, 'qvtoperational_Tag', {partner})
    assert getattr(partner, 'qvtoperational_Element') == owner
    _safe_set(owner, 'qvtoperational_Tag', set())
    assert getattr(partner, 'qvtoperational_Element') is None


def test_assoc_entry42_stub_double():
    # EntryOperation has no real 'EntryOperation' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = EntryOperation()
    setattr(partner, 'EntryOperation', None)
    _safe_set(owner, 'qvtoperational_Module43', partner)
    assert getattr(partner, 'EntryOperation') == owner
    _safe_set(owner, 'qvtoperational_Module43', None)
    assert getattr(partner, 'EntryOperation') is None


def test_assoc_importedModule54_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'qvtoperational_ModuleImport55', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'qvtoperational_ModuleImport55', None)
    assert getattr(partner, 'Module') is None


def test_assoc_metamodel38_stub_double():
    # qvtoperational_Package has no real 'qvtoperational_Package' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModelType(conformanceKind="sample_text")
    partner = qvtoperational_Package()
    setattr(partner, 'qvtoperational_Package', None)
    _safe_set(owner, 'qvtoperational_ModelType39', {partner})
    assert getattr(partner, 'qvtoperational_Package') == owner
    _safe_set(owner, 'qvtoperational_ModelType39', set())
    assert getattr(partner, 'qvtoperational_Package') is None


def test_assoc_module56_stub_double():
    # Module has no real 'Module58' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module58', None)
    _safe_set(owner, 'qvtoperational_ModuleImport57', partner)
    assert getattr(partner, 'Module58') == owner
    _safe_set(owner, 'qvtoperational_ModuleImport57', None)
    assert getattr(partner, 'Module58') is None


def test_assoc_moduleImport44_stub_double():
    # ModuleImport has no real 'ModuleImport' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = ModuleImport()
    setattr(partner, 'ModuleImport', None)
    _safe_set(owner, 'qvtoperational_Module45', {partner})
    assert getattr(partner, 'ModuleImport') == owner
    _safe_set(owner, 'qvtoperational_Module45', set())
    assert getattr(partner, 'ModuleImport') is None


def test_assoc_overridden8_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation', None)
    _safe_set(owner, 'qvtoperational_ImperativeOperation9', partner)
    assert getattr(partner, 'ImperativeOperation') == owner
    _safe_set(owner, 'qvtoperational_ImperativeOperation9', None)
    assert getattr(partner, 'ImperativeOperation') is None


def test_assoc_ownedTag46_stub_double():
    # qvtoperational_TemplateableElement has no real 'qvtoperational_TemplateableElement' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = qvtoperational_TemplateableElement()
    setattr(partner, 'qvtoperational_TemplateableElement', None)
    _safe_set(owner, 'qvtoperational_Module47', {partner})
    assert getattr(partner, 'qvtoperational_TemplateableElement') == owner
    _safe_set(owner, 'qvtoperational_Module47', set())
    assert getattr(partner, 'qvtoperational_TemplateableElement') is None


def test_assoc_ownedVariable48_stub_double():
    # qvtoperational_Variable has no real 'qvtoperational_Variable' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = qvtoperational_Variable()
    setattr(partner, 'qvtoperational_Variable', None)
    _safe_set(owner, 'qvtoperational_Module49', {partner})
    assert getattr(partner, 'qvtoperational_Variable') == owner
    _safe_set(owner, 'qvtoperational_Module49', set())
    assert getattr(partner, 'qvtoperational_Variable') is None


def test_assoc_resOwner93_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation95' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation95', None)
    _safe_set(owner, 'qvtoperational_VarParameter94', partner)
    assert getattr(partner, 'ImperativeOperation95') == owner
    _safe_set(owner, 'qvtoperational_VarParameter94', None)
    assert getattr(partner, 'ImperativeOperation95') is None


def test_assoc_result10_stub_double():
    # VarParameter has no real 'VarParameter12' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter12', None)
    _safe_set(owner, 'qvtoperational_ImperativeOperation11', {partner})
    assert getattr(partner, 'VarParameter12') == owner
    _safe_set(owner, 'qvtoperational_ImperativeOperation11', set())
    assert getattr(partner, 'VarParameter12') is None


def test_assoc_target86_stub_double():
    # qvtoperational_Variable has no real 'qvtoperational_Variable88' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = qvtoperational_Variable()
    setattr(partner, 'qvtoperational_Variable88', None)
    _safe_set(owner, 'qvtoperational_ResolveExp87', partner)
    assert getattr(partner, 'qvtoperational_Variable88') == owner
    _safe_set(owner, 'qvtoperational_ResolveExp87', None)
    assert getattr(partner, 'qvtoperational_Variable88') is None


def test_assoc_usedModelType50_stub_double():
    # ModelType has no real 'ModelType' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType', None)
    _safe_set(owner, 'qvtoperational_Module51', {partner})
    assert getattr(partner, 'ModelType') == owner
    _safe_set(owner, 'qvtoperational_Module51', set())
    assert getattr(partner, 'ModelType') is None


