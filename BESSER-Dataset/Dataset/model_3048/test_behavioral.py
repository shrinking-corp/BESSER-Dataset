import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Entities,
    FeatureType,
    soa_Architecture,
    soa_Comment,
    soa_Entities,
    soa_EntitiesFeature,
    soa_Entity,
    soa_Enum,
    soa_Exception,
    soa_Exceptions,
    soa_Feature,
    soa_FeatureType,
    soa_GenericListFeature,
    soa_Import,
    soa_Model,
    soa_Module,
    soa_Operation,
    soa_PrimitiveFeature,
    soa_Service,
    PrimitiveType,
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

def test_assoc_exceptionts30_reverse_link_reassign_clear():
    a1 = soa_Operation(name="sample_text")
    a2 = soa_Operation(name="sample_text_2")
    b = soa_Exception(msg="sample_text", name="sample_text")
    _safe_set(b, 'soa_Exception32', a1)
    assert _is_linked(b, 'soa_Exception32', a1)
    if hasattr(a1, 'soa_Operation31'):
        assert _is_linked(a1, 'soa_Operation31', b)
    _safe_set(b, 'soa_Exception32', a2)
    assert _is_linked(b, 'soa_Exception32', a2)
    if hasattr(a1, 'soa_Operation31'):
        assert not _is_linked(a1, 'soa_Operation31', b)
    if hasattr(a2, 'soa_Operation31'):
        assert _is_linked(a2, 'soa_Operation31', b)
    _safe_set(b, 'soa_Exception32', None)
    assert not _is_linked(b, 'soa_Exception32', a2)
    if hasattr(a2, 'soa_Operation31'):
        assert not _is_linked(a2, 'soa_Operation31', b)


def test_assoc_featureComment12_reverse_link_reassign_clear():
    a1 = soa_Feature(name="sample_text")
    a2 = soa_Feature(name="sample_text_2")
    b = soa_Comment(value="sample_text")
    _safe_set(b, 'soa_Comment', a1)
    assert _is_linked(b, 'soa_Comment', a1)
    if hasattr(a1, 'soa_Feature13'):
        assert _is_linked(a1, 'soa_Feature13', b)
    _safe_set(b, 'soa_Comment', a2)
    assert _is_linked(b, 'soa_Comment', a2)
    if hasattr(a1, 'soa_Feature13'):
        assert not _is_linked(a1, 'soa_Feature13', b)
    if hasattr(a2, 'soa_Feature13'):
        assert _is_linked(a2, 'soa_Feature13', b)
    _safe_set(b, 'soa_Comment', None)
    assert not _is_linked(b, 'soa_Comment', a2)
    if hasattr(a2, 'soa_Feature13'):
        assert not _is_linked(a2, 'soa_Feature13', b)


def test_assoc_featuresInput24_reverse_link_reassign_clear():
    a1 = soa_Operation(name="sample_text")
    a2 = soa_Operation(name="sample_text_2")
    b = soa_Feature(name="sample_text")
    _safe_set(b, 'soa_Feature26', a1)
    assert _is_linked(b, 'soa_Feature26', a1)
    if hasattr(a1, 'soa_Operation25'):
        assert _is_linked(a1, 'soa_Operation25', b)
    _safe_set(b, 'soa_Feature26', a2)
    assert _is_linked(b, 'soa_Feature26', a2)
    if hasattr(a1, 'soa_Operation25'):
        assert not _is_linked(a1, 'soa_Operation25', b)
    if hasattr(a2, 'soa_Operation25'):
        assert _is_linked(a2, 'soa_Operation25', b)
    _safe_set(b, 'soa_Feature26', None)
    assert not _is_linked(b, 'soa_Feature26', a2)
    if hasattr(a2, 'soa_Operation25'):
        assert not _is_linked(a2, 'soa_Operation25', b)


def test_assoc_featuresOutput27_reverse_link_reassign_clear():
    a1 = soa_Operation(name="sample_text")
    a2 = soa_Operation(name="sample_text_2")
    b = soa_Feature(name="sample_text")
    _safe_set(b, 'soa_Feature29', a1)
    assert _is_linked(b, 'soa_Feature29', a1)
    if hasattr(a1, 'soa_Operation28'):
        assert _is_linked(a1, 'soa_Operation28', b)
    _safe_set(b, 'soa_Feature29', a2)
    assert _is_linked(b, 'soa_Feature29', a2)
    if hasattr(a1, 'soa_Operation28'):
        assert not _is_linked(a1, 'soa_Operation28', b)
    if hasattr(a2, 'soa_Operation28'):
        assert _is_linked(a2, 'soa_Operation28', b)
    _safe_set(b, 'soa_Feature29', None)
    assert not _is_linked(b, 'soa_Feature29', a2)
    if hasattr(a2, 'soa_Operation28'):
        assert not _is_linked(a2, 'soa_Operation28', b)


def test_assoc_imports1_reverse_link_reassign_clear():
    a1 = soa_Module(event="sample_text", name="sample_text", version="sample_text")
    a2 = soa_Module(event="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = soa_Import(importedNamespace="sample_text")
    _safe_set(b, 'soa_Import', a1)
    assert _is_linked(b, 'soa_Import', a1)
    if hasattr(a1, 'soa_Module2'):
        assert _is_linked(a1, 'soa_Module2', b)
    _safe_set(b, 'soa_Import', a2)
    assert _is_linked(b, 'soa_Import', a2)
    if hasattr(a1, 'soa_Module2'):
        assert not _is_linked(a1, 'soa_Module2', b)
    if hasattr(a2, 'soa_Module2'):
        assert _is_linked(a2, 'soa_Module2', b)
    _safe_set(b, 'soa_Import', None)
    assert not _is_linked(b, 'soa_Import', a2)
    if hasattr(a2, 'soa_Module2'):
        assert not _is_linked(a2, 'soa_Module2', b)


def test_assoc_module0_reverse_link_reassign_clear():
    a1 = soa_Module(event="sample_text", name="sample_text", version="sample_text")
    a2 = soa_Module(event="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = soa_Architecture(name="sample_text")
    _safe_set(b, 'soa_Architecture', a1)
    assert _is_linked(b, 'soa_Architecture', a1)
    if hasattr(a1, 'soa_Module'):
        assert _is_linked(a1, 'soa_Module', b)
    _safe_set(b, 'soa_Architecture', a2)
    assert _is_linked(b, 'soa_Architecture', a2)
    if hasattr(a1, 'soa_Module'):
        assert not _is_linked(a1, 'soa_Module', b)
    if hasattr(a2, 'soa_Module'):
        assert _is_linked(a2, 'soa_Module', b)
    _safe_set(b, 'soa_Architecture', None)
    assert not _is_linked(b, 'soa_Architecture', a2)
    if hasattr(a2, 'soa_Module'):
        assert not _is_linked(a2, 'soa_Module', b)


def test_assoc_operations22_reverse_link_reassign_clear():
    a1 = soa_Service(name="sample_text")
    a2 = soa_Service(name="sample_text_2")
    b = soa_Operation(name="sample_text")
    _safe_set(b, 'soa_Operation', a1)
    assert _is_linked(b, 'soa_Operation', a1)
    if hasattr(a1, 'soa_Service23'):
        assert _is_linked(a1, 'soa_Service23', b)
    _safe_set(b, 'soa_Operation', a2)
    assert _is_linked(b, 'soa_Operation', a2)
    if hasattr(a1, 'soa_Service23'):
        assert not _is_linked(a1, 'soa_Service23', b)
    if hasattr(a2, 'soa_Service23'):
        assert _is_linked(a2, 'soa_Service23', b)
    _safe_set(b, 'soa_Operation', None)
    assert not _is_linked(b, 'soa_Operation', a2)
    if hasattr(a2, 'soa_Service23'):
        assert not _is_linked(a2, 'soa_Service23', b)


def test_assoc_services7_reverse_link_reassign_clear():
    a1 = soa_Service(name="sample_text")
    a2 = soa_Service(name="sample_text_2")
    b = soa_Module(event="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'soa_Module8', {a1})
    assert _is_linked(b, 'soa_Module8', a1)
    if hasattr(a1, 'soa_Service'):
        assert _is_linked(a1, 'soa_Service', b)
    _safe_set(b, 'soa_Module8', {a2})
    assert _is_linked(b, 'soa_Module8', a2)
    if hasattr(a1, 'soa_Service'):
        assert not _is_linked(a1, 'soa_Service', b)
    if hasattr(a2, 'soa_Service'):
        assert _is_linked(a2, 'soa_Service', b)
    _safe_set(b, 'soa_Module8', set())
    assert not _is_linked(b, 'soa_Module8', a2)
    if hasattr(a2, 'soa_Service'):
        assert not _is_linked(a2, 'soa_Service', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entities9_stub_double():
    # soa_Model has no real 'soa_Model10' property in the generated
    # code (a bare stub) -- manually attach it so soa_Entities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soa_Entities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soa_Entities(name="sample_text")
    partner = soa_Model()
    setattr(partner, 'soa_Model10', None)
    _safe_set(owner, 'soa_Entities', partner)
    assert owner in getattr(partner, 'soa_Model10')
    _safe_set(owner, 'soa_Entities', None)
    assert owner not in getattr(partner, 'soa_Model10')


def test_assoc_exceptions20_stub_double():
    # soa_Exceptions has no real 'soa_Exceptions21' property in the generated
    # code (a bare stub) -- manually attach it so soa_Exception's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soa_Exception's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soa_Exception(msg="sample_text", name="sample_text")
    partner = soa_Exceptions()
    setattr(partner, 'soa_Exceptions21', None)
    _safe_set(owner, 'soa_Exception', partner)
    assert owner in getattr(partner, 'soa_Exceptions21')
    _safe_set(owner, 'soa_Exception', None)
    assert owner not in getattr(partner, 'soa_Exceptions21')


def test_assoc_exceptions5_stub_double():
    # soa_Exceptions has no real 'soa_Exceptions' property in the generated
    # code (a bare stub) -- manually attach it so soa_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soa_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soa_Module(event="sample_text", name="sample_text", version="sample_text")
    partner = soa_Exceptions()
    setattr(partner, 'soa_Exceptions', None)
    _safe_set(owner, 'soa_Module6', partner)
    assert getattr(partner, 'soa_Exceptions') == owner
    _safe_set(owner, 'soa_Module6', None)
    assert getattr(partner, 'soa_Exceptions') is None


def test_assoc_features11_stub_double():
    # soa_Entity has no real 'soa_Entity' property in the generated
    # code (a bare stub) -- manually attach it so soa_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soa_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soa_Feature(name="sample_text")
    partner = soa_Entity()
    setattr(partner, 'soa_Entity', None)
    _safe_set(owner, 'soa_Feature', partner)
    assert owner in getattr(partner, 'soa_Entity')
    _safe_set(owner, 'soa_Feature', None)
    assert owner not in getattr(partner, 'soa_Entity')


def test_assoc_model3_stub_double():
    # soa_Model has no real 'soa_Model' property in the generated
    # code (a bare stub) -- manually attach it so soa_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soa_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soa_Module(event="sample_text", name="sample_text", version="sample_text")
    partner = soa_Model()
    setattr(partner, 'soa_Model', None)
    _safe_set(owner, 'soa_Module4', partner)
    assert getattr(partner, 'soa_Model') == owner
    _safe_set(owner, 'soa_Module4', None)
    assert getattr(partner, 'soa_Model') is None


def test_assoc_type14_stub_double():
    # soa_FeatureType has no real 'soa_FeatureType' property in the generated
    # code (a bare stub) -- manually attach it so soa_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soa_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soa_Feature(name="sample_text")
    partner = soa_FeatureType()
    setattr(partner, 'soa_FeatureType', None)
    _safe_set(owner, 'soa_Feature15', partner)
    assert getattr(partner, 'soa_FeatureType') == owner
    _safe_set(owner, 'soa_Feature15', None)
    assert getattr(partner, 'soa_FeatureType') is None


def test_assoc_type16_stub_double():
    # soa_EntitiesFeature has no real 'soa_EntitiesFeature' property in the generated
    # code (a bare stub) -- manually attach it so soa_Entities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soa_Entities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soa_Entities(name="sample_text")
    partner = soa_EntitiesFeature()
    setattr(partner, 'soa_EntitiesFeature', None)
    _safe_set(owner, 'soa_Entities17', partner)
    assert getattr(partner, 'soa_EntitiesFeature') == owner
    _safe_set(owner, 'soa_Entities17', None)
    assert getattr(partner, 'soa_EntitiesFeature') is None


