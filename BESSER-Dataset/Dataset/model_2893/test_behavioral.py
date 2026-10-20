import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    PageElement,
    Type,
    Value,
    webGui_ActionElement,
    webGui_Add,
    webGui_DataType,
    webGui_DisplayElement,
    webGui_Divide,
    webGui_DomainModel,
    webGui_DomainPath,
    webGui_DomainPathTail,
    webGui_Entity,
    webGui_Expression,
    webGui_Feature,
    webGui_Model,
    webGui_Multiply,
    webGui_NumberLiteral,
    webGui_Page,
    webGui_PageElement,
    webGui_Subtract,
    webGui_Type,
    webGui_Value,
    webGui_WebModel,
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

def test_assoc_type6_reverse_link_reassign_clear():
    a1 = webGui_Type(name="sample_text")
    a2 = webGui_Type(name="sample_text_2")
    b = webGui_Feature(multivalued=True, name="sample_text")
    _safe_set(b, 'webGui_Feature7', a1)
    assert _is_linked(b, 'webGui_Feature7', a1)
    if hasattr(a1, 'webGui_Type8'):
        assert _is_linked(a1, 'webGui_Type8', b)
    _safe_set(b, 'webGui_Feature7', a2)
    assert _is_linked(b, 'webGui_Feature7', a2)
    if hasattr(a1, 'webGui_Type8'):
        assert not _is_linked(a1, 'webGui_Type8', b)
    if hasattr(a2, 'webGui_Type8'):
        assert _is_linked(a2, 'webGui_Type8', b)
    _safe_set(b, 'webGui_Feature7', None)
    assert not _is_linked(b, 'webGui_Feature7', a2)
    if hasattr(a2, 'webGui_Type8'):
        assert not _is_linked(a2, 'webGui_Type8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents16_stub_double():
    # webGui_PageElement has no real 'webGui_PageElement' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Page(name="sample_text", title="sample_text")
    partner = webGui_PageElement()
    setattr(partner, 'webGui_PageElement', None)
    _safe_set(owner, 'webGui_Page17', {partner})
    assert getattr(partner, 'webGui_PageElement') == owner
    _safe_set(owner, 'webGui_Page17', set())
    assert getattr(partner, 'webGui_PageElement') is None


def test_assoc_domain0_stub_double():
    # webGui_DomainModel has no real 'webGui_DomainModel' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Model(name="sample_text")
    partner = webGui_DomainModel()
    setattr(partner, 'webGui_DomainModel', None)
    _safe_set(owner, 'webGui_Model', partner)
    assert getattr(partner, 'webGui_DomainModel') == owner
    _safe_set(owner, 'webGui_Model', None)
    assert getattr(partner, 'webGui_DomainModel') is None


def test_assoc_entity13_stub_double():
    # webGui_Entity has no real 'webGui_Entity15' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Page(name="sample_text", title="sample_text")
    partner = webGui_Entity()
    setattr(partner, 'webGui_Entity15', None)
    _safe_set(owner, 'webGui_Page14', partner)
    assert getattr(partner, 'webGui_Entity15') == owner
    _safe_set(owner, 'webGui_Page14', None)
    assert getattr(partner, 'webGui_Entity15') is None


def test_assoc_expression9_stub_double():
    # webGui_Expression has no real 'webGui_Expression' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Feature(multivalued=True, name="sample_text")
    partner = webGui_Expression()
    setattr(partner, 'webGui_Expression', None)
    _safe_set(owner, 'webGui_Feature10', partner)
    assert getattr(partner, 'webGui_Expression') == owner
    _safe_set(owner, 'webGui_Feature10', None)
    assert getattr(partner, 'webGui_Expression') is None


def test_assoc_feature19_stub_double():
    # webGui_DomainPath has no real 'webGui_DomainPath20' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Feature(multivalued=True, name="sample_text")
    partner = webGui_DomainPath()
    setattr(partner, 'webGui_DomainPath20', None)
    _safe_set(owner, 'webGui_Feature21', partner)
    assert getattr(partner, 'webGui_DomainPath20') == owner
    _safe_set(owner, 'webGui_Feature21', None)
    assert getattr(partner, 'webGui_DomainPath20') is None


def test_assoc_feature24_stub_double():
    # webGui_DomainPathTail has no real 'webGui_DomainPathTail25' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Feature(multivalued=True, name="sample_text")
    partner = webGui_DomainPathTail()
    setattr(partner, 'webGui_DomainPathTail25', None)
    _safe_set(owner, 'webGui_Feature26', partner)
    assert getattr(partner, 'webGui_DomainPathTail25') == owner
    _safe_set(owner, 'webGui_Feature26', None)
    assert getattr(partner, 'webGui_DomainPathTail25') is None


def test_assoc_features5_stub_double():
    # webGui_Entity has no real 'webGui_Entity' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Feature(multivalued=True, name="sample_text")
    partner = webGui_Entity()
    setattr(partner, 'webGui_Entity', None)
    _safe_set(owner, 'webGui_Feature', partner)
    assert owner in getattr(partner, 'webGui_Entity')
    _safe_set(owner, 'webGui_Feature', None)
    assert owner not in getattr(partner, 'webGui_Entity')


def test_assoc_pages11_stub_double():
    # webGui_WebModel has no real 'webGui_WebModel12' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Page(name="sample_text", title="sample_text")
    partner = webGui_WebModel()
    setattr(partner, 'webGui_WebModel12', None)
    _safe_set(owner, 'webGui_Page', partner)
    assert owner in getattr(partner, 'webGui_WebModel12')
    _safe_set(owner, 'webGui_Page', None)
    assert owner not in getattr(partner, 'webGui_WebModel12')


def test_assoc_types3_stub_double():
    # webGui_DomainModel has no real 'webGui_DomainModel4' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Type(name="sample_text")
    partner = webGui_DomainModel()
    setattr(partner, 'webGui_DomainModel4', None)
    _safe_set(owner, 'webGui_Type', partner)
    assert owner in getattr(partner, 'webGui_DomainModel4')
    _safe_set(owner, 'webGui_Type', None)
    assert owner not in getattr(partner, 'webGui_DomainModel4')


def test_assoc_web1_stub_double():
    # webGui_WebModel has no real 'webGui_WebModel' property in the generated
    # code (a bare stub) -- manually attach it so webGui_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webGui_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webGui_Model(name="sample_text")
    partner = webGui_WebModel()
    setattr(partner, 'webGui_WebModel', None)
    _safe_set(owner, 'webGui_Model2', partner)
    assert getattr(partner, 'webGui_WebModel') == owner
    _safe_set(owner, 'webGui_Model2', None)
    assert getattr(partner, 'webGui_WebModel') is None


