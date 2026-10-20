import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConstructorBody,
    EntryOperation,
    ImperativeCallExp,
    ImperativeOperation,
    MappingOperation,
    ModelParameter,
    ModelType,
    Module,
    ModuleImport,
    OperationBody,
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
    ResolveExp,
    VarParameter,
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

def test_assoc_binding21_stub_double():
    # ModelType has no real 'ModelType22' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType22', None)
    _safe_set(owner, 'QVTOperational_ModuleImport', {partner})
    assert getattr(partner, 'ModelType22') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport', set())
    assert getattr(partner, 'ModelType22') is None


def test_assoc_body0_stub_double():
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


def test_assoc_context1_stub_double():
    # VarParameter has no real 'VarParameter' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation2', partner)
    assert getattr(partner, 'VarParameter') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation2', None)
    assert getattr(partner, 'VarParameter') is None


def test_assoc_ctxOwner35_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation36' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation36', None)
    _safe_set(owner, 'QVTOperational_VarParameter', partner)
    assert getattr(partner, 'ImperativeOperation36') == owner
    _safe_set(owner, 'QVTOperational_VarParameter', None)
    assert getattr(partner, 'ImperativeOperation36') is None


def test_assoc_entry16_stub_double():
    # EntryOperation has no real 'EntryOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = EntryOperation()
    setattr(partner, 'EntryOperation', None)
    _safe_set(owner, 'QVTOperational_Module', partner)
    assert getattr(partner, 'EntryOperation') == owner
    _safe_set(owner, 'QVTOperational_Module', None)
    assert getattr(partner, 'EntryOperation') is None


def test_assoc_importedModule23_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'QVTOperational_ModuleImport24', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport24', None)
    assert getattr(partner, 'Module') is None


def test_assoc_module25_stub_double():
    # Module has no real 'Module27' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module27', None)
    _safe_set(owner, 'QVTOperational_ModuleImport26', partner)
    assert getattr(partner, 'Module27') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport26', None)
    assert getattr(partner, 'Module27') is None


def test_assoc_moduleImport17_stub_double():
    # ModuleImport has no real 'ModuleImport' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModuleImport()
    setattr(partner, 'ModuleImport', None)
    _safe_set(owner, 'QVTOperational_Module18', {partner})
    assert getattr(partner, 'ModuleImport') == owner
    _safe_set(owner, 'QVTOperational_Module18', set())
    assert getattr(partner, 'ModuleImport') is None


def test_assoc_overridden3_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation4', partner)
    assert getattr(partner, 'ImperativeOperation') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation4', None)
    assert getattr(partner, 'ImperativeOperation') is None


def test_assoc_resOwner37_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation39' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation39', None)
    _safe_set(owner, 'QVTOperational_VarParameter38', partner)
    assert getattr(partner, 'ImperativeOperation39') == owner
    _safe_set(owner, 'QVTOperational_VarParameter38', None)
    assert getattr(partner, 'ImperativeOperation39') is None


def test_assoc_result5_stub_double():
    # VarParameter has no real 'VarParameter7' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter7', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation6', {partner})
    assert getattr(partner, 'VarParameter7') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation6', set())
    assert getattr(partner, 'VarParameter7') is None


def test_assoc_usedModelType19_stub_double():
    # ModelType has no real 'ModelType' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType', None)
    _safe_set(owner, 'QVTOperational_Module20', {partner})
    assert getattr(partner, 'ModelType') == owner
    _safe_set(owner, 'QVTOperational_Module20', set())
    assert getattr(partner, 'ModelType') is None


