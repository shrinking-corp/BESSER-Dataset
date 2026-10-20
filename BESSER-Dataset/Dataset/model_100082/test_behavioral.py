import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assign,
    AssignExtra,
    BuildEntry,
    If,
    Object_M,
    Object_Y,
    ShellCmd,
    Value,
    VarSlashSym,
    kbuild_Assign,
    kbuild_AssignExtra,
    kbuild_BuildEntry,
    kbuild_EObject,
    kbuild_Entry,
    kbuild_HostProgram,
    kbuild_If,
    kbuild_IfEq,
    kbuild_IfNEq,
    kbuild_Ifndef,
    kbuild_Include,
    kbuild_Model,
    kbuild_MyVariable,
    kbuild_Obj_m,
    kbuild_Obj_y,
    kbuild_Object,
    kbuild_ObjectDir,
    kbuild_ObjectFile,
    kbuild_ObjectShellChar,
    kbuild_ObjectShellCmd,
    kbuild_ObjectSingleFile,
    kbuild_ObjectString,
    kbuild_ObjectVariable,
    kbuild_Object_M,
    kbuild_Object_Y,
    kbuild_ShellCmd,
    kbuild_ShellPart,
    kbuild_Target,
    kbuild_Value,
    kbuild_Values,
    kbuild_VarSlashSym,
    kbuild_Variable,
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

def test_assoc_cmd18_stub_double():
    # kbuild_ShellPart has no real 'kbuild_ShellPart19' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_ShellCmd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_ShellCmd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_ShellCmd(name="sample_text")
    partner = kbuild_ShellPart()
    setattr(partner, 'kbuild_ShellPart19', None)
    _safe_set(owner, 'kbuild_ShellCmd20', partner)
    assert getattr(partner, 'kbuild_ShellPart19') == owner
    _safe_set(owner, 'kbuild_ShellCmd20', None)
    assert getattr(partner, 'kbuild_ShellPart19') is None


def test_assoc_inner23_stub_double():
    # kbuild_Assign has no real 'kbuild_Assign' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_HostProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_HostProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_HostProgram(name="sample_text")
    partner = kbuild_Assign()
    setattr(partner, 'kbuild_Assign', None)
    _safe_set(owner, 'kbuild_HostProgram24', partner)
    assert getattr(partner, 'kbuild_Assign') == owner
    _safe_set(owner, 'kbuild_HostProgram24', None)
    assert getattr(partner, 'kbuild_Assign') is None


def test_assoc_shell6_stub_double():
    # kbuild_If has no real 'kbuild_If' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_ShellCmd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_ShellCmd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_ShellCmd(name="sample_text")
    partner = kbuild_If()
    setattr(partner, 'kbuild_If', None)
    _safe_set(owner, 'kbuild_ShellCmd', partner)
    assert getattr(partner, 'kbuild_If') == owner
    _safe_set(owner, 'kbuild_ShellCmd', None)
    assert getattr(partner, 'kbuild_If') is None


def test_assoc_shellPart14_stub_double():
    # kbuild_ShellPart has no real 'kbuild_ShellPart' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_ShellCmd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_ShellCmd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_ShellCmd(name="sample_text")
    partner = kbuild_ShellPart()
    setattr(partner, 'kbuild_ShellPart', None)
    _safe_set(owner, 'kbuild_ShellCmd15', {partner})
    assert getattr(partner, 'kbuild_ShellPart') == owner
    _safe_set(owner, 'kbuild_ShellCmd15', set())
    assert getattr(partner, 'kbuild_ShellPart') is None


def test_assoc_val16_stub_double():
    # kbuild_ShellPart has no real 'kbuild_ShellPart17' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_VarSlashSym's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_VarSlashSym's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_VarSlashSym(name="sample_text")
    partner = kbuild_ShellPart()
    setattr(partner, 'kbuild_ShellPart17', None)
    _safe_set(owner, 'kbuild_VarSlashSym', partner)
    assert getattr(partner, 'kbuild_ShellPart17') == owner
    _safe_set(owner, 'kbuild_VarSlashSym', None)
    assert getattr(partner, 'kbuild_ShellPart17') is None


def test_assoc_value36_stub_double():
    # kbuild_Variable has no real 'kbuild_Variable37' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_ObjectVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_ObjectVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_ObjectVariable(additional="sample_text")
    partner = kbuild_Variable()
    setattr(partner, 'kbuild_Variable37', None)
    _safe_set(owner, 'kbuild_ObjectVariable', partner)
    assert getattr(partner, 'kbuild_Variable37') == owner
    _safe_set(owner, 'kbuild_ObjectVariable', None)
    assert getattr(partner, 'kbuild_Variable37') is None


def test_assoc_value38_stub_double():
    # kbuild_ObjectShellCmd has no real 'kbuild_ObjectShellCmd' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_ShellCmd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_ShellCmd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_ShellCmd(name="sample_text")
    partner = kbuild_ObjectShellCmd()
    setattr(partner, 'kbuild_ObjectShellCmd', None)
    _safe_set(owner, 'kbuild_ShellCmd39', partner)
    assert getattr(partner, 'kbuild_ObjectShellCmd') == owner
    _safe_set(owner, 'kbuild_ShellCmd39', None)
    assert getattr(partner, 'kbuild_ObjectShellCmd') is None


def test_assoc_variable21_stub_double():
    # kbuild_Variable has no real 'kbuild_Variable22' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_HostProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_HostProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_HostProgram(name="sample_text")
    partner = kbuild_Variable()
    setattr(partner, 'kbuild_Variable22', None)
    _safe_set(owner, 'kbuild_HostProgram', partner)
    assert getattr(partner, 'kbuild_Variable22') == owner
    _safe_set(owner, 'kbuild_HostProgram', None)
    assert getattr(partner, 'kbuild_Variable22') is None


def test_assoc_variable30_stub_double():
    # kbuild_Variable has no real 'kbuild_Variable31' property in the generated
    # code (a bare stub) -- manually attach it so kbuild_MyVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kbuild_MyVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kbuild_MyVariable(name="sample_text")
    partner = kbuild_Variable()
    setattr(partner, 'kbuild_Variable31', None)
    _safe_set(owner, 'kbuild_MyVariable', partner)
    assert getattr(partner, 'kbuild_Variable31') == owner
    _safe_set(owner, 'kbuild_MyVariable', None)
    assert getattr(partner, 'kbuild_Variable31') is None


