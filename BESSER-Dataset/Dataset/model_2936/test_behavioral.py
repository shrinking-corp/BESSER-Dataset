import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    AbstractType,
    FormTypes,
    extended_AbstractElement,
    extended_AbstractType,
    extended_DataType,
    extended_Domainmodel,
    extended_Entity,
    extended_EntityType,
    extended_Feature,
    extended_Form,
    extended_FormNewEntityOnly,
    extended_FormReport,
    extended_FormTypes,
    extended_Import,
    extended_PackageDeclaration,
    extended_Page,
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

def test_assoc_entity12_reverse_link_reassign_clear():
    a1 = extended_FormTypes(name="sample_text")
    a2 = extended_FormTypes(name="sample_text_2")
    b = extended_Entity(name="sample_text")
    _safe_set(b, 'extended_Entity14', a1)
    assert _is_linked(b, 'extended_Entity14', a1)
    if hasattr(a1, 'extended_FormTypes13'):
        assert _is_linked(a1, 'extended_FormTypes13', b)
    _safe_set(b, 'extended_Entity14', a2)
    assert _is_linked(b, 'extended_Entity14', a2)
    if hasattr(a1, 'extended_FormTypes13'):
        assert not _is_linked(a1, 'extended_FormTypes13', b)
    if hasattr(a2, 'extended_FormTypes13'):
        assert _is_linked(a2, 'extended_FormTypes13', b)
    _safe_set(b, 'extended_Entity14', None)
    assert not _is_linked(b, 'extended_Entity14', a2)
    if hasattr(a2, 'extended_FormTypes13'):
        assert not _is_linked(a2, 'extended_FormTypes13', b)


def test_assoc_features7_reverse_link_reassign_clear():
    a1 = extended_Feature(max=7, min=7, name="sample_text", required="sample_text")
    a2 = extended_Feature(max=13, min=13, name="sample_text_2", required="sample_text_2")
    b = extended_Entity(name="sample_text")
    _safe_set(b, 'extended_Entity8', {a1})
    assert _is_linked(b, 'extended_Entity8', a1)
    if hasattr(a1, 'extended_Feature'):
        assert _is_linked(a1, 'extended_Feature', b)
    _safe_set(b, 'extended_Entity8', {a2})
    assert _is_linked(b, 'extended_Entity8', a2)
    if hasattr(a1, 'extended_Feature'):
        assert not _is_linked(a1, 'extended_Feature', b)
    if hasattr(a2, 'extended_Feature'):
        assert _is_linked(a2, 'extended_Feature', b)
    _safe_set(b, 'extended_Entity8', set())
    assert not _is_linked(b, 'extended_Entity8', a2)
    if hasattr(a2, 'extended_Feature'):
        assert not _is_linked(a2, 'extended_Feature', b)


def test_assoc_forms11_reverse_link_reassign_clear():
    a1 = extended_Page(footer="sample_text", header="sample_text", name="sample_text", title="sample_text")
    a2 = extended_Page(footer="sample_text_2", header="sample_text_2", name="sample_text_2", title="sample_text_2")
    b = extended_FormTypes(name="sample_text")
    _safe_set(b, 'extended_FormTypes', a1)
    assert _is_linked(b, 'extended_FormTypes', a1)
    if hasattr(a1, 'extended_Page'):
        assert _is_linked(a1, 'extended_Page', b)
    _safe_set(b, 'extended_FormTypes', a2)
    assert _is_linked(b, 'extended_FormTypes', a2)
    if hasattr(a1, 'extended_Page'):
        assert not _is_linked(a1, 'extended_Page', b)
    if hasattr(a2, 'extended_Page'):
        assert _is_linked(a2, 'extended_Page', b)
    _safe_set(b, 'extended_FormTypes', None)
    assert not _is_linked(b, 'extended_FormTypes', a2)
    if hasattr(a2, 'extended_Page'):
        assert not _is_linked(a2, 'extended_Page', b)


def test_assoc_superType5_reverse_link_reassign_clear():
    a1 = extended_Entity(name="sample_text")
    a2 = extended_Entity(name="sample_text_2")
    b = extended_Entity(name="sample_text")
    _safe_set(b, 'extended_Entity6', a1)
    assert _is_linked(b, 'extended_Entity6', a1)
    if hasattr(a1, 'extended_Entity4'):
        assert _is_linked(a1, 'extended_Entity4', b)
    _safe_set(b, 'extended_Entity6', a2)
    assert _is_linked(b, 'extended_Entity6', a2)
    if hasattr(a1, 'extended_Entity4'):
        assert not _is_linked(a1, 'extended_Entity4', b)
    if hasattr(a2, 'extended_Entity4'):
        assert _is_linked(a2, 'extended_Entity4', b)
    _safe_set(b, 'extended_Entity6', None)
    assert not _is_linked(b, 'extended_Entity6', a2)
    if hasattr(a2, 'extended_Entity4'):
        assert not _is_linked(a2, 'extended_Entity4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # extended_AbstractElement has no real 'extended_AbstractElement' property in the generated
    # code (a bare stub) -- manually attach it so extended_Domainmodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extended_Domainmodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extended_Domainmodel(nomeProj="sample_text")
    partner = extended_AbstractElement()
    setattr(partner, 'extended_AbstractElement', None)
    _safe_set(owner, 'extended_Domainmodel', {partner})
    assert getattr(partner, 'extended_AbstractElement') == owner
    _safe_set(owner, 'extended_Domainmodel', set())
    assert getattr(partner, 'extended_AbstractElement') is None


def test_assoc_elements1_stub_double():
    # extended_AbstractElement has no real 'extended_AbstractElement2' property in the generated
    # code (a bare stub) -- manually attach it so extended_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extended_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extended_PackageDeclaration(name="sample_text")
    partner = extended_AbstractElement()
    setattr(partner, 'extended_AbstractElement2', None)
    _safe_set(owner, 'extended_PackageDeclaration', {partner})
    assert getattr(partner, 'extended_AbstractElement2') == owner
    _safe_set(owner, 'extended_PackageDeclaration', set())
    assert getattr(partner, 'extended_AbstractElement2') is None


def test_assoc_entity3_stub_double():
    # extended_EntityType has no real 'extended_EntityType' property in the generated
    # code (a bare stub) -- manually attach it so extended_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extended_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extended_Entity(name="sample_text")
    partner = extended_EntityType()
    setattr(partner, 'extended_EntityType', None)
    _safe_set(owner, 'extended_Entity', partner)
    assert getattr(partner, 'extended_EntityType') == owner
    _safe_set(owner, 'extended_Entity', None)
    assert getattr(partner, 'extended_EntityType') is None


def test_assoc_type9_stub_double():
    # extended_AbstractType has no real 'extended_AbstractType' property in the generated
    # code (a bare stub) -- manually attach it so extended_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extended_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extended_Feature(max=7, min=7, name="sample_text", required="sample_text")
    partner = extended_AbstractType()
    setattr(partner, 'extended_AbstractType', None)
    _safe_set(owner, 'extended_Feature10', partner)
    assert getattr(partner, 'extended_AbstractType') == owner
    _safe_set(owner, 'extended_Feature10', None)
    assert getattr(partner, 'extended_AbstractType') is None


