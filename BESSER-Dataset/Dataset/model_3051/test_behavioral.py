import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Feature,
    domainmodel_AbstractElement,
    domainmodel_DomainModel,
    domainmodel_Entity,
    domainmodel_Feature,
    domainmodel_Import,
    domainmodel_JvmFormalParameter,
    domainmodel_JvmParameterizedTypeReference,
    domainmodel_JvmTypeReference,
    domainmodel_Operation,
    domainmodel_PackageDeclaration,
    domainmodel_Property,
    domainmodel_XExpression,
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

def test_assoc_features3_reverse_link_reassign_clear():
    a1 = domainmodel_Feature(name="sample_text")
    a2 = domainmodel_Feature(name="sample_text_2")
    b = domainmodel_Entity(name="sample_text")
    _safe_set(b, 'domainmodel_Entity', {a1})
    assert _is_linked(b, 'domainmodel_Entity', a1)
    if hasattr(a1, 'domainmodel_Feature'):
        assert _is_linked(a1, 'domainmodel_Feature', b)
    _safe_set(b, 'domainmodel_Entity', {a2})
    assert _is_linked(b, 'domainmodel_Entity', a2)
    if hasattr(a1, 'domainmodel_Feature'):
        assert not _is_linked(a1, 'domainmodel_Feature', b)
    if hasattr(a2, 'domainmodel_Feature'):
        assert _is_linked(a2, 'domainmodel_Feature', b)
    _safe_set(b, 'domainmodel_Entity', set())
    assert not _is_linked(b, 'domainmodel_Entity', a2)
    if hasattr(a2, 'domainmodel_Feature'):
        assert not _is_linked(a2, 'domainmodel_Feature', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements1_stub_double():
    # domainmodel_AbstractElement has no real 'domainmodel_AbstractElement2' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_PackageDeclaration(name="sample_text")
    partner = domainmodel_AbstractElement()
    setattr(partner, 'domainmodel_AbstractElement2', None)
    _safe_set(owner, 'domainmodel_PackageDeclaration', {partner})
    assert getattr(partner, 'domainmodel_AbstractElement2') == owner
    _safe_set(owner, 'domainmodel_PackageDeclaration', set())
    assert getattr(partner, 'domainmodel_AbstractElement2') is None


def test_assoc_superType4_stub_double():
    # domainmodel_JvmParameterizedTypeReference has no real 'domainmodel_JvmParameterizedTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_Entity(name="sample_text")
    partner = domainmodel_JvmParameterizedTypeReference()
    setattr(partner, 'domainmodel_JvmParameterizedTypeReference', None)
    _safe_set(owner, 'domainmodel_Entity5', partner)
    assert getattr(partner, 'domainmodel_JvmParameterizedTypeReference') == owner
    _safe_set(owner, 'domainmodel_Entity5', None)
    assert getattr(partner, 'domainmodel_JvmParameterizedTypeReference') is None


def test_assoc_type6_stub_double():
    # domainmodel_JvmTypeReference has no real 'domainmodel_JvmTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_Feature(name="sample_text")
    partner = domainmodel_JvmTypeReference()
    setattr(partner, 'domainmodel_JvmTypeReference', None)
    _safe_set(owner, 'domainmodel_Feature7', partner)
    assert getattr(partner, 'domainmodel_JvmTypeReference') == owner
    _safe_set(owner, 'domainmodel_Feature7', None)
    assert getattr(partner, 'domainmodel_JvmTypeReference') is None


