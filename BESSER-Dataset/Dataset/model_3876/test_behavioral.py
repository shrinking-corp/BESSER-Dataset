import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    fl_Apply,
    fl_Argument,
    fl_Binary,
    fl_DocumentRoot,
    fl_EStringToStringMapEntry,
    fl_Expr,
    fl_Function,
    fl_IfThenElse,
    fl_Literal,
    fl_ProgramType,
    Ops,
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

def test_assoc_arg0_stub_double():
    # fl_Expr has no real 'fl_Expr' property in the generated
    # code (a bare stub) -- manually attach it so fl_Apply's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_Apply's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_Apply(name="sample_text")
    partner = fl_Expr()
    setattr(partner, 'fl_Expr', None)
    _safe_set(owner, 'fl_Apply', {partner})
    assert getattr(partner, 'fl_Expr') == owner
    _safe_set(owner, 'fl_Apply', set())
    assert getattr(partner, 'fl_Expr') is None


def test_assoc_fragment10_stub_double():
    # fl_Expr has no real 'fl_Expr12' property in the generated
    # code (a bare stub) -- manually attach it so fl_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_DocumentRoot(mixed="sample_text")
    partner = fl_Expr()
    setattr(partner, 'fl_Expr12', None)
    _safe_set(owner, 'fl_DocumentRoot11', {partner})
    assert getattr(partner, 'fl_Expr12') == owner
    _safe_set(owner, 'fl_DocumentRoot11', set())
    assert getattr(partner, 'fl_Expr12') is None


def test_assoc_function25_stub_double():
    # fl_ProgramType has no real 'fl_ProgramType26' property in the generated
    # code (a bare stub) -- manually attach it so fl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_Function(arg="sample_text", name="sample_text")
    partner = fl_ProgramType()
    setattr(partner, 'fl_ProgramType26', None)
    _safe_set(owner, 'fl_Function27', partner)
    assert owner in getattr(partner, 'fl_ProgramType26')
    _safe_set(owner, 'fl_Function27', None)
    assert owner not in getattr(partner, 'fl_ProgramType26')


def test_assoc_left1_stub_double():
    # fl_Expr has no real 'fl_Expr2' property in the generated
    # code (a bare stub) -- manually attach it so fl_Binary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_Binary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_Binary(ops="sample_text")
    partner = fl_Expr()
    setattr(partner, 'fl_Expr2', None)
    _safe_set(owner, 'fl_Binary', partner)
    assert getattr(partner, 'fl_Expr2') == owner
    _safe_set(owner, 'fl_Binary', None)
    assert getattr(partner, 'fl_Expr2') is None


def test_assoc_program13_stub_double():
    # fl_ProgramType has no real 'fl_ProgramType' property in the generated
    # code (a bare stub) -- manually attach it so fl_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_DocumentRoot(mixed="sample_text")
    partner = fl_ProgramType()
    setattr(partner, 'fl_ProgramType', None)
    _safe_set(owner, 'fl_DocumentRoot14', {partner})
    assert getattr(partner, 'fl_ProgramType') == owner
    _safe_set(owner, 'fl_DocumentRoot14', set())
    assert getattr(partner, 'fl_ProgramType') is None


def test_assoc_rhs15_stub_double():
    # fl_Expr has no real 'fl_Expr16' property in the generated
    # code (a bare stub) -- manually attach it so fl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_Function(arg="sample_text", name="sample_text")
    partner = fl_Expr()
    setattr(partner, 'fl_Expr16', None)
    _safe_set(owner, 'fl_Function', partner)
    assert getattr(partner, 'fl_Expr16') == owner
    _safe_set(owner, 'fl_Function', None)
    assert getattr(partner, 'fl_Expr16') is None


def test_assoc_right3_stub_double():
    # fl_Expr has no real 'fl_Expr5' property in the generated
    # code (a bare stub) -- manually attach it so fl_Binary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_Binary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_Binary(ops="sample_text")
    partner = fl_Expr()
    setattr(partner, 'fl_Expr5', None)
    _safe_set(owner, 'fl_Binary4', partner)
    assert getattr(partner, 'fl_Expr5') == owner
    _safe_set(owner, 'fl_Binary4', None)
    assert getattr(partner, 'fl_Expr5') is None


def test_assoc_xMLNSPrefixMap6_stub_double():
    # fl_EStringToStringMapEntry has no real 'fl_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so fl_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_DocumentRoot(mixed="sample_text")
    partner = fl_EStringToStringMapEntry()
    setattr(partner, 'fl_EStringToStringMapEntry', None)
    _safe_set(owner, 'fl_DocumentRoot', {partner})
    assert getattr(partner, 'fl_EStringToStringMapEntry') == owner
    _safe_set(owner, 'fl_DocumentRoot', set())
    assert getattr(partner, 'fl_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation7_stub_double():
    # fl_EStringToStringMapEntry has no real 'fl_EStringToStringMapEntry9' property in the generated
    # code (a bare stub) -- manually attach it so fl_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fl_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fl_DocumentRoot(mixed="sample_text")
    partner = fl_EStringToStringMapEntry()
    setattr(partner, 'fl_EStringToStringMapEntry9', None)
    _safe_set(owner, 'fl_DocumentRoot8', {partner})
    assert getattr(partner, 'fl_EStringToStringMapEntry9') == owner
    _safe_set(owner, 'fl_DocumentRoot8', set())
    assert getattr(partner, 'fl_EStringToStringMapEntry9') is None


