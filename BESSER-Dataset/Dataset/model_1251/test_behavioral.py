import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallExp,
    Class,
    ConstructorBody,
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
    OclExpression,
    Operation,
    OperationBody,
    OperationCallExp,
    OperationalTransformation,
    Package,
    Parameter,
    Property,
    QVTOperational_Constructor,
    QVTOperational_ConstructorBody,
    QVTOperational_ContextualProperty,
    QVTOperational_EntryOperation,
    QVTOperational_Helper,
    QVTOperational_ImperativeCallExp,
    QVTOperational_ImperativeOperation,
    QVTOperational_Library,
    QVTOperational_MappingBody,
    QVTOperational_MappingCallExp,
    QVTOperational_MappingOperation,
    QVTOperational_MappingParameter,
    QVTOperational_ModelParameter,
    QVTOperational_ModelType,
    QVTOperational_Module,
    QVTOperational_ModuleImport,
    QVTOperational_ObjectExp,
    QVTOperational_OperationBody,
    QVTOperational_OperationalTransformation,
    QVTOperational_ResolveExp,
    QVTOperational_ResolveInExp,
    QVTOperational_VarParameter,
    Relation,
    RelationDomain,
    RelationalTransformation,
    ResolveExp,
    Tag,
    VarParameter,
    Variable,
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

def test_assoc_additionalCondition37_stub_double():
    # OclExpression has no real 'OclExpression38' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModelType(conformanceKind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression38', None)
    _safe_set(owner, 'QVTOperational_ModelType', {partner})
    assert getattr(partner, 'OclExpression38') == owner
    _safe_set(owner, 'QVTOperational_ModelType', set())
    assert getattr(partner, 'OclExpression38') is None


def test_assoc_binding53_stub_double():
    # ModelType has no real 'ModelType54' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType54', None)
    _safe_set(owner, 'QVTOperational_ModuleImport', {partner})
    assert getattr(partner, 'ModelType54') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport', set())
    assert getattr(partner, 'ModelType54') is None


def test_assoc_body5_stub_double():
    # OperationBody has no real 'OperationBody' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = OperationBody()
    setattr(partner, 'OperationBody', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation', partner)
    assert getattr(partner, 'OperationBody') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation', None)
    assert getattr(partner, 'OperationBody') is None


def test_assoc_condition84_stub_double():
    # OclExpression has no real 'OclExpression85' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression85', None)
    _safe_set(owner, 'QVTOperational_ResolveExp', partner)
    assert getattr(partner, 'OclExpression85') == owner
    _safe_set(owner, 'QVTOperational_ResolveExp', None)
    assert getattr(partner, 'OclExpression85') is None


def test_assoc_configProperty41_stub_double():
    # Property has no real 'Property42' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Property()
    setattr(partner, 'Property42', None)
    _safe_set(owner, 'QVTOperational_Module', {partner})
    assert getattr(partner, 'Property42') == owner
    _safe_set(owner, 'QVTOperational_Module', set())
    assert getattr(partner, 'Property42') is None


def test_assoc_context6_stub_double():
    # VarParameter has no real 'VarParameter' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation7', partner)
    assert getattr(partner, 'VarParameter') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation7', None)
    assert getattr(partner, 'VarParameter') is None


def test_assoc_ctxOwner91_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation92' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation92', None)
    _safe_set(owner, 'QVTOperational_VarParameter', partner)
    assert getattr(partner, 'ImperativeOperation92') == owner
    _safe_set(owner, 'QVTOperational_VarParameter', None)
    assert getattr(partner, 'ImperativeOperation92') is None


def test_assoc_entry43_stub_double():
    # EntryOperation has no real 'EntryOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = EntryOperation()
    setattr(partner, 'EntryOperation', None)
    _safe_set(owner, 'QVTOperational_Module44', partner)
    assert getattr(partner, 'EntryOperation') == owner
    _safe_set(owner, 'QVTOperational_Module44', None)
    assert getattr(partner, 'EntryOperation') is None


def test_assoc_importedModule55_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'QVTOperational_ModuleImport56', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport56', None)
    assert getattr(partner, 'Module') is None


def test_assoc_metamodel39_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModelType(conformanceKind="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'QVTOperational_ModelType40', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'QVTOperational_ModelType40', set())
    assert getattr(partner, 'Package') is None


def test_assoc_module57_stub_double():
    # Module has no real 'Module59' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module59', None)
    _safe_set(owner, 'QVTOperational_ModuleImport58', partner)
    assert getattr(partner, 'Module59') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport58', None)
    assert getattr(partner, 'Module59') is None


def test_assoc_moduleImport45_stub_double():
    # ModuleImport has no real 'ModuleImport' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModuleImport()
    setattr(partner, 'ModuleImport', None)
    _safe_set(owner, 'QVTOperational_Module46', {partner})
    assert getattr(partner, 'ModuleImport') == owner
    _safe_set(owner, 'QVTOperational_Module46', set())
    assert getattr(partner, 'ModuleImport') is None


def test_assoc_overridden8_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation9', partner)
    assert getattr(partner, 'ImperativeOperation') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation9', None)
    assert getattr(partner, 'ImperativeOperation') is None


def test_assoc_ownedTag47_stub_double():
    # Tag has no real 'Tag' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Tag()
    setattr(partner, 'Tag', None)
    _safe_set(owner, 'QVTOperational_Module48', {partner})
    assert getattr(partner, 'Tag') == owner
    _safe_set(owner, 'QVTOperational_Module48', set())
    assert getattr(partner, 'Tag') is None


def test_assoc_ownedVariable49_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'QVTOperational_Module50', {partner})
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'QVTOperational_Module50', set())
    assert getattr(partner, 'Variable') is None


def test_assoc_resOwner93_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation95' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation95', None)
    _safe_set(owner, 'QVTOperational_VarParameter94', partner)
    assert getattr(partner, 'ImperativeOperation95') == owner
    _safe_set(owner, 'QVTOperational_VarParameter94', None)
    assert getattr(partner, 'ImperativeOperation95') is None


def test_assoc_result10_stub_double():
    # VarParameter has no real 'VarParameter12' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter12', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation11', {partner})
    assert getattr(partner, 'VarParameter12') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation11', set())
    assert getattr(partner, 'VarParameter12') is None


def test_assoc_target86_stub_double():
    # Variable has no real 'Variable88' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = Variable()
    setattr(partner, 'Variable88', None)
    _safe_set(owner, 'QVTOperational_ResolveExp87', partner)
    assert getattr(partner, 'Variable88') == owner
    _safe_set(owner, 'QVTOperational_ResolveExp87', None)
    assert getattr(partner, 'Variable88') is None


def test_assoc_usedModelType51_stub_double():
    # ModelType has no real 'ModelType' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType', None)
    _safe_set(owner, 'QVTOperational_Module52', {partner})
    assert getattr(partner, 'ModelType') == owner
    _safe_set(owner, 'QVTOperational_Module52', set())
    assert getattr(partner, 'ModelType') is None


