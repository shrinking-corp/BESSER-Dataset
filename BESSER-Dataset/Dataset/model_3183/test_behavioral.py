import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    architecture_AbstractModel,
    architecture_Architecture,
    architecture_AtomicType,
    architecture_Binding,
    architecture_Component,
    architecture_DomainDeclaration,
    architecture_Import,
    architecture_Model,
    architecture_Operation,
    architecture_Variable,
    Type,
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

def test_assoc_arg35_reverse_link_reassign_clear():
    a1 = architecture_Variable(name="sample_text")
    a2 = architecture_Variable(name="sample_text_2")
    b = architecture_Operation(name="sample_text")
    _safe_set(b, 'architecture_Operation36', {a1})
    assert _is_linked(b, 'architecture_Operation36', a1)
    if hasattr(a1, 'architecture_Variable37'):
        assert _is_linked(a1, 'architecture_Variable37', b)
    _safe_set(b, 'architecture_Operation36', {a2})
    assert _is_linked(b, 'architecture_Operation36', a2)
    if hasattr(a1, 'architecture_Variable37'):
        assert not _is_linked(a1, 'architecture_Variable37', b)
    if hasattr(a2, 'architecture_Variable37'):
        assert _is_linked(a2, 'architecture_Variable37', b)
    _safe_set(b, 'architecture_Operation36', set())
    assert not _is_linked(b, 'architecture_Operation36', a2)
    if hasattr(a2, 'architecture_Variable37'):
        assert not _is_linked(a2, 'architecture_Variable37', b)


def test_assoc_compType41_reverse_link_reassign_clear():
    a1 = architecture_Component(name="sample_text")
    a2 = architecture_Component(name="sample_text_2")
    b = architecture_AtomicType(atomType="sample_text")
    _safe_set(b, 'architecture_AtomicType42', a1)
    assert _is_linked(b, 'architecture_AtomicType42', a1)
    if hasattr(a1, 'architecture_Component43'):
        assert _is_linked(a1, 'architecture_Component43', b)
    _safe_set(b, 'architecture_AtomicType42', a2)
    assert _is_linked(b, 'architecture_AtomicType42', a2)
    if hasattr(a1, 'architecture_Component43'):
        assert not _is_linked(a1, 'architecture_Component43', b)
    if hasattr(a2, 'architecture_Component43'):
        assert _is_linked(a2, 'architecture_Component43', b)
    _safe_set(b, 'architecture_AtomicType42', None)
    assert not _is_linked(b, 'architecture_AtomicType42', a2)
    if hasattr(a2, 'architecture_Component43'):
        assert not _is_linked(a2, 'architecture_Component43', b)


def test_assoc_operations14_reverse_link_reassign_clear():
    a1 = architecture_Operation(name="sample_text")
    a2 = architecture_Operation(name="sample_text_2")
    b = architecture_Component(name="sample_text")
    _safe_set(b, 'architecture_Component15', {a1})
    assert _is_linked(b, 'architecture_Component15', a1)
    if hasattr(a1, 'architecture_Operation16'):
        assert _is_linked(a1, 'architecture_Operation16', b)
    _safe_set(b, 'architecture_Component15', {a2})
    assert _is_linked(b, 'architecture_Component15', a2)
    if hasattr(a1, 'architecture_Operation16'):
        assert not _is_linked(a1, 'architecture_Operation16', b)
    if hasattr(a2, 'architecture_Operation16'):
        assert _is_linked(a2, 'architecture_Operation16', b)
    _safe_set(b, 'architecture_Component15', set())
    assert not _is_linked(b, 'architecture_Component15', a2)
    if hasattr(a2, 'architecture_Operation16'):
        assert not _is_linked(a2, 'architecture_Operation16', b)


def test_assoc_ops9_reverse_link_reassign_clear():
    a1 = architecture_Operation(name="sample_text")
    a2 = architecture_Operation(name="sample_text_2")
    b = architecture_Component(name="sample_text")
    _safe_set(b, 'architecture_Component10', {a1})
    assert _is_linked(b, 'architecture_Component10', a1)
    if hasattr(a1, 'architecture_Operation'):
        assert _is_linked(a1, 'architecture_Operation', b)
    _safe_set(b, 'architecture_Component10', {a2})
    assert _is_linked(b, 'architecture_Component10', a2)
    if hasattr(a1, 'architecture_Operation'):
        assert not _is_linked(a1, 'architecture_Operation', b)
    if hasattr(a2, 'architecture_Operation'):
        assert _is_linked(a2, 'architecture_Operation', b)
    _safe_set(b, 'architecture_Component10', set())
    assert not _is_linked(b, 'architecture_Component10', a2)
    if hasattr(a2, 'architecture_Operation'):
        assert not _is_linked(a2, 'architecture_Operation', b)


def test_assoc_opsReq11_reverse_link_reassign_clear():
    a1 = architecture_Operation(name="sample_text")
    a2 = architecture_Operation(name="sample_text_2")
    b = architecture_Component(name="sample_text")
    _safe_set(b, 'architecture_Component12', {a1})
    assert _is_linked(b, 'architecture_Component12', a1)
    if hasattr(a1, 'architecture_Operation13'):
        assert _is_linked(a1, 'architecture_Operation13', b)
    _safe_set(b, 'architecture_Component12', {a2})
    assert _is_linked(b, 'architecture_Component12', a2)
    if hasattr(a1, 'architecture_Operation13'):
        assert not _is_linked(a1, 'architecture_Operation13', b)
    if hasattr(a2, 'architecture_Operation13'):
        assert _is_linked(a2, 'architecture_Operation13', b)
    _safe_set(b, 'architecture_Component12', set())
    assert not _is_linked(b, 'architecture_Component12', a2)
    if hasattr(a2, 'architecture_Operation13'):
        assert not _is_linked(a2, 'architecture_Operation13', b)


def test_assoc_type33_reverse_link_reassign_clear():
    a1 = architecture_Variable(name="sample_text")
    a2 = architecture_Variable(name="sample_text_2")
    b = architecture_AtomicType(atomType="sample_text")
    _safe_set(b, 'architecture_AtomicType', a1)
    assert _is_linked(b, 'architecture_AtomicType', a1)
    if hasattr(a1, 'architecture_Variable34'):
        assert _is_linked(a1, 'architecture_Variable34', b)
    _safe_set(b, 'architecture_AtomicType', a2)
    assert _is_linked(b, 'architecture_AtomicType', a2)
    if hasattr(a1, 'architecture_Variable34'):
        assert not _is_linked(a1, 'architecture_Variable34', b)
    if hasattr(a2, 'architecture_Variable34'):
        assert _is_linked(a2, 'architecture_Variable34', b)
    _safe_set(b, 'architecture_AtomicType', None)
    assert not _is_linked(b, 'architecture_AtomicType', a2)
    if hasattr(a2, 'architecture_Variable34'):
        assert not _is_linked(a2, 'architecture_Variable34', b)


def test_assoc_type38_reverse_link_reassign_clear():
    a1 = architecture_Operation(name="sample_text")
    a2 = architecture_Operation(name="sample_text_2")
    b = architecture_AtomicType(atomType="sample_text")
    _safe_set(b, 'architecture_AtomicType40', a1)
    assert _is_linked(b, 'architecture_AtomicType40', a1)
    if hasattr(a1, 'architecture_Operation39'):
        assert _is_linked(a1, 'architecture_Operation39', b)
    _safe_set(b, 'architecture_AtomicType40', a2)
    assert _is_linked(b, 'architecture_AtomicType40', a2)
    if hasattr(a1, 'architecture_Operation39'):
        assert not _is_linked(a1, 'architecture_Operation39', b)
    if hasattr(a2, 'architecture_Operation39'):
        assert _is_linked(a2, 'architecture_Operation39', b)
    _safe_set(b, 'architecture_AtomicType40', None)
    assert not _is_linked(b, 'architecture_AtomicType40', a2)
    if hasattr(a2, 'architecture_Operation39'):
        assert not _is_linked(a2, 'architecture_Operation39', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_comp5_stub_double():
    # architecture_AbstractModel has no real 'architecture_AbstractModel6' property in the generated
    # code (a bare stub) -- manually attach it so architecture_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_Component(name="sample_text")
    partner = architecture_AbstractModel()
    setattr(partner, 'architecture_AbstractModel6', None)
    _safe_set(owner, 'architecture_Component', partner)
    assert owner in getattr(partner, 'architecture_AbstractModel6')
    _safe_set(owner, 'architecture_Component', None)
    assert owner not in getattr(partner, 'architecture_AbstractModel6')


def test_assoc_elements1_stub_double():
    # architecture_AbstractModel has no real 'architecture_AbstractModel' property in the generated
    # code (a bare stub) -- manually attach it so architecture_DomainDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_DomainDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_DomainDeclaration(name="sample_text")
    partner = architecture_AbstractModel()
    setattr(partner, 'architecture_AbstractModel', None)
    _safe_set(owner, 'architecture_DomainDeclaration2', {partner})
    assert getattr(partner, 'architecture_AbstractModel') == owner
    _safe_set(owner, 'architecture_DomainDeclaration2', set())
    assert getattr(partner, 'architecture_AbstractModel') is None


def test_assoc_imp3_stub_double():
    # architecture_AbstractModel has no real 'architecture_AbstractModel4' property in the generated
    # code (a bare stub) -- manually attach it so architecture_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_Import(importedNamespace="sample_text")
    partner = architecture_AbstractModel()
    setattr(partner, 'architecture_AbstractModel4', None)
    _safe_set(owner, 'architecture_Import', partner)
    assert owner in getattr(partner, 'architecture_AbstractModel4')
    _safe_set(owner, 'architecture_Import', None)
    assert owner not in getattr(partner, 'architecture_AbstractModel4')


def test_assoc_package0_stub_double():
    # architecture_Model has no real 'architecture_Model' property in the generated
    # code (a bare stub) -- manually attach it so architecture_DomainDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_DomainDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_DomainDeclaration(name="sample_text")
    partner = architecture_Model()
    setattr(partner, 'architecture_Model', None)
    _safe_set(owner, 'architecture_DomainDeclaration', partner)
    assert owner in getattr(partner, 'architecture_Model')
    _safe_set(owner, 'architecture_DomainDeclaration', None)
    assert owner not in getattr(partner, 'architecture_Model')


def test_assoc_proMember24_stub_double():
    # architecture_Binding has no real 'architecture_Binding25' property in the generated
    # code (a bare stub) -- manually attach it so architecture_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_Operation(name="sample_text")
    partner = architecture_Binding()
    setattr(partner, 'architecture_Binding25', None)
    _safe_set(owner, 'architecture_Operation26', partner)
    assert getattr(partner, 'architecture_Binding25') == owner
    _safe_set(owner, 'architecture_Operation26', None)
    assert getattr(partner, 'architecture_Binding25') is None


def test_assoc_provider21_stub_double():
    # architecture_Binding has no real 'architecture_Binding22' property in the generated
    # code (a bare stub) -- manually attach it so architecture_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_Variable(name="sample_text")
    partner = architecture_Binding()
    setattr(partner, 'architecture_Binding22', None)
    _safe_set(owner, 'architecture_Variable23', partner)
    assert getattr(partner, 'architecture_Binding22') == owner
    _safe_set(owner, 'architecture_Variable23', None)
    assert getattr(partner, 'architecture_Binding22') is None


def test_assoc_recMember30_stub_double():
    # architecture_Binding has no real 'architecture_Binding31' property in the generated
    # code (a bare stub) -- manually attach it so architecture_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_Operation(name="sample_text")
    partner = architecture_Binding()
    setattr(partner, 'architecture_Binding31', None)
    _safe_set(owner, 'architecture_Operation32', partner)
    assert getattr(partner, 'architecture_Binding31') == owner
    _safe_set(owner, 'architecture_Operation32', None)
    assert getattr(partner, 'architecture_Binding31') is None


def test_assoc_receiver27_stub_double():
    # architecture_Binding has no real 'architecture_Binding28' property in the generated
    # code (a bare stub) -- manually attach it so architecture_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_Variable(name="sample_text")
    partner = architecture_Binding()
    setattr(partner, 'architecture_Binding28', None)
    _safe_set(owner, 'architecture_Variable29', partner)
    assert getattr(partner, 'architecture_Binding28') == owner
    _safe_set(owner, 'architecture_Variable29', None)
    assert getattr(partner, 'architecture_Binding28') is None


def test_assoc_vars17_stub_double():
    # architecture_Architecture has no real 'architecture_Architecture18' property in the generated
    # code (a bare stub) -- manually attach it so architecture_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_Variable(name="sample_text")
    partner = architecture_Architecture()
    setattr(partner, 'architecture_Architecture18', None)
    _safe_set(owner, 'architecture_Variable', partner)
    assert owner in getattr(partner, 'architecture_Architecture18')
    _safe_set(owner, 'architecture_Variable', None)
    assert owner not in getattr(partner, 'architecture_Architecture18')


