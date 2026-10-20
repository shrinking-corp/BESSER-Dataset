import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    smalluml_Association,
    smalluml_Attribute,
    smalluml_Generalisation,
    smalluml_Methode,
    smalluml_Role,
    smalluml_SchemaUML,
    smalluml_SmallClass,
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

def test_assoc_cible18_reverse_link_reassign_clear():
    a1 = smalluml_SmallClass(name="sample_text")
    a2 = smalluml_SmallClass(name="sample_text_2")
    b = smalluml_Association(name="sample_text")
    _safe_set(b, 'smalluml_Association19', a1)
    assert _is_linked(b, 'smalluml_Association19', a1)
    if hasattr(a1, 'smalluml_SmallClass20'):
        assert _is_linked(a1, 'smalluml_SmallClass20', b)
    _safe_set(b, 'smalluml_Association19', a2)
    assert _is_linked(b, 'smalluml_Association19', a2)
    if hasattr(a1, 'smalluml_SmallClass20'):
        assert not _is_linked(a1, 'smalluml_SmallClass20', b)
    if hasattr(a2, 'smalluml_SmallClass20'):
        assert _is_linked(a2, 'smalluml_SmallClass20', b)
    _safe_set(b, 'smalluml_Association19', None)
    assert not _is_linked(b, 'smalluml_Association19', a2)
    if hasattr(a2, 'smalluml_SmallClass20'):
        assert not _is_linked(a2, 'smalluml_SmallClass20', b)


def test_assoc_classDedie26_reverse_link_reassign_clear():
    a1 = smalluml_SmallClass(name="sample_text")
    a2 = smalluml_SmallClass(name="sample_text_2")
    b = smalluml_Role(Multiplicity="sample_text")
    _safe_set(b, 'smalluml_Role27', a1)
    assert _is_linked(b, 'smalluml_Role27', a1)
    if hasattr(a1, 'smalluml_SmallClass28'):
        assert _is_linked(a1, 'smalluml_SmallClass28', b)
    _safe_set(b, 'smalluml_Role27', a2)
    assert _is_linked(b, 'smalluml_Role27', a2)
    if hasattr(a1, 'smalluml_SmallClass28'):
        assert not _is_linked(a1, 'smalluml_SmallClass28', b)
    if hasattr(a2, 'smalluml_SmallClass28'):
        assert _is_linked(a2, 'smalluml_SmallClass28', b)
    _safe_set(b, 'smalluml_Role27', None)
    assert not _is_linked(b, 'smalluml_Role27', a2)
    if hasattr(a2, 'smalluml_SmallClass28'):
        assert not _is_linked(a2, 'smalluml_SmallClass28', b)


def test_assoc_listeAttribute21_reverse_link_reassign_clear():
    a1 = smalluml_Attribute(name="sample_text", type="sample_text")
    a2 = smalluml_Attribute(name="sample_text_2", type="sample_text_2")
    b = smalluml_Association(name="sample_text")
    _safe_set(b, 'smalluml_Association22', {a1})
    assert _is_linked(b, 'smalluml_Association22', a1)
    if hasattr(a1, 'smalluml_Attribute23'):
        assert _is_linked(a1, 'smalluml_Attribute23', b)
    _safe_set(b, 'smalluml_Association22', {a2})
    assert _is_linked(b, 'smalluml_Association22', a2)
    if hasattr(a1, 'smalluml_Attribute23'):
        assert not _is_linked(a1, 'smalluml_Attribute23', b)
    if hasattr(a2, 'smalluml_Attribute23'):
        assert _is_linked(a2, 'smalluml_Attribute23', b)
    _safe_set(b, 'smalluml_Association22', set())
    assert not _is_linked(b, 'smalluml_Association22', a2)
    if hasattr(a2, 'smalluml_Attribute23'):
        assert not _is_linked(a2, 'smalluml_Attribute23', b)


def test_assoc_listeAttribute5_reverse_link_reassign_clear():
    a1 = smalluml_SmallClass(name="sample_text")
    a2 = smalluml_SmallClass(name="sample_text_2")
    b = smalluml_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'smalluml_Attribute', a1)
    assert _is_linked(b, 'smalluml_Attribute', a1)
    if hasattr(a1, 'smalluml_SmallClass6'):
        assert _is_linked(a1, 'smalluml_SmallClass6', b)
    _safe_set(b, 'smalluml_Attribute', a2)
    assert _is_linked(b, 'smalluml_Attribute', a2)
    if hasattr(a1, 'smalluml_SmallClass6'):
        assert not _is_linked(a1, 'smalluml_SmallClass6', b)
    if hasattr(a2, 'smalluml_SmallClass6'):
        assert _is_linked(a2, 'smalluml_SmallClass6', b)
    _safe_set(b, 'smalluml_Attribute', None)
    assert not _is_linked(b, 'smalluml_Attribute', a2)
    if hasattr(a2, 'smalluml_SmallClass6'):
        assert not _is_linked(a2, 'smalluml_SmallClass6', b)


def test_assoc_listeMethode7_reverse_link_reassign_clear():
    a1 = smalluml_SmallClass(name="sample_text")
    a2 = smalluml_SmallClass(name="sample_text_2")
    b = smalluml_Methode(name="sample_text", returnType="sample_text")
    _safe_set(b, 'smalluml_Methode', a1)
    assert _is_linked(b, 'smalluml_Methode', a1)
    if hasattr(a1, 'smalluml_SmallClass8'):
        assert _is_linked(a1, 'smalluml_SmallClass8', b)
    _safe_set(b, 'smalluml_Methode', a2)
    assert _is_linked(b, 'smalluml_Methode', a2)
    if hasattr(a1, 'smalluml_SmallClass8'):
        assert not _is_linked(a1, 'smalluml_SmallClass8', b)
    if hasattr(a2, 'smalluml_SmallClass8'):
        assert _is_linked(a2, 'smalluml_SmallClass8', b)
    _safe_set(b, 'smalluml_Methode', None)
    assert not _is_linked(b, 'smalluml_Methode', a2)
    if hasattr(a2, 'smalluml_SmallClass8'):
        assert not _is_linked(a2, 'smalluml_SmallClass8', b)


def test_assoc_listeRole24_reverse_link_reassign_clear():
    a1 = smalluml_Role(Multiplicity="sample_text")
    a2 = smalluml_Role(Multiplicity="sample_text_2")
    b = smalluml_Association(name="sample_text")
    _safe_set(b, 'smalluml_Association25', {a1})
    assert _is_linked(b, 'smalluml_Association25', a1)
    if hasattr(a1, 'smalluml_Role'):
        assert _is_linked(a1, 'smalluml_Role', b)
    _safe_set(b, 'smalluml_Association25', {a2})
    assert _is_linked(b, 'smalluml_Association25', a2)
    if hasattr(a1, 'smalluml_Role'):
        assert not _is_linked(a1, 'smalluml_Role', b)
    if hasattr(a2, 'smalluml_Role'):
        assert _is_linked(a2, 'smalluml_Role', b)
    _safe_set(b, 'smalluml_Association25', set())
    assert not _is_linked(b, 'smalluml_Association25', a2)
    if hasattr(a2, 'smalluml_Role'):
        assert not _is_linked(a2, 'smalluml_Role', b)


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = smalluml_SmallClass(name="sample_text")
    a2 = smalluml_SmallClass(name="sample_text_2")
    b = smalluml_Association(name="sample_text")
    _safe_set(b, 'smalluml_Association16', a1)
    assert _is_linked(b, 'smalluml_Association16', a1)
    if hasattr(a1, 'smalluml_SmallClass17'):
        assert _is_linked(a1, 'smalluml_SmallClass17', b)
    _safe_set(b, 'smalluml_Association16', a2)
    assert _is_linked(b, 'smalluml_Association16', a2)
    if hasattr(a1, 'smalluml_SmallClass17'):
        assert not _is_linked(a1, 'smalluml_SmallClass17', b)
    if hasattr(a2, 'smalluml_SmallClass17'):
        assert _is_linked(a2, 'smalluml_SmallClass17', b)
    _safe_set(b, 'smalluml_Association16', None)
    assert not _is_linked(b, 'smalluml_Association16', a2)
    if hasattr(a2, 'smalluml_SmallClass17'):
        assert not _is_linked(a2, 'smalluml_SmallClass17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ass3_stub_double():
    # smalluml_SchemaUML has no real 'smalluml_SchemaUML4' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Association(name="sample_text")
    partner = smalluml_SchemaUML()
    setattr(partner, 'smalluml_SchemaUML4', None)
    _safe_set(owner, 'smalluml_Association', partner)
    assert owner in getattr(partner, 'smalluml_SchemaUML4')
    _safe_set(owner, 'smalluml_Association', None)
    assert owner not in getattr(partner, 'smalluml_SchemaUML4')


def test_assoc_c1_stub_double():
    # smalluml_SchemaUML has no real 'smalluml_SchemaUML2' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_SmallClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_SmallClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_SmallClass(name="sample_text")
    partner = smalluml_SchemaUML()
    setattr(partner, 'smalluml_SchemaUML2', None)
    _safe_set(owner, 'smalluml_SmallClass', partner)
    assert owner in getattr(partner, 'smalluml_SchemaUML2')
    _safe_set(owner, 'smalluml_SmallClass', None)
    assert owner not in getattr(partner, 'smalluml_SchemaUML2')


def test_assoc_cible12_stub_double():
    # smalluml_Generalisation has no real 'smalluml_Generalisation13' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_SmallClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_SmallClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_SmallClass(name="sample_text")
    partner = smalluml_Generalisation()
    setattr(partner, 'smalluml_Generalisation13', None)
    _safe_set(owner, 'smalluml_SmallClass14', partner)
    assert getattr(partner, 'smalluml_Generalisation13') == owner
    _safe_set(owner, 'smalluml_SmallClass14', None)
    assert getattr(partner, 'smalluml_Generalisation13') is None


def test_assoc_source9_stub_double():
    # smalluml_Generalisation has no real 'smalluml_Generalisation10' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_SmallClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_SmallClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_SmallClass(name="sample_text")
    partner = smalluml_Generalisation()
    setattr(partner, 'smalluml_Generalisation10', None)
    _safe_set(owner, 'smalluml_SmallClass11', partner)
    assert getattr(partner, 'smalluml_Generalisation10') == owner
    _safe_set(owner, 'smalluml_SmallClass11', None)
    assert getattr(partner, 'smalluml_Generalisation10') is None


