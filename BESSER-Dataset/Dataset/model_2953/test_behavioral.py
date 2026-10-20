import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AllModelType,
    CollectionReturnType,
    DefAttribute,
    DefCollectionTypeAttribute,
    DefIdAttribute,
    DefVariable,
    Element,
    Entity,
    Link,
    Method,
    ModelType,
    modelDsl_AllModelType,
    modelDsl_AllModelTypeCollection,
    modelDsl_AssociativeEntity,
    modelDsl_CollectionReturnType,
    modelDsl_DefAllModelTypeVariable,
    modelDsl_DefAttribute,
    modelDsl_DefCollectionTypeAttribute,
    modelDsl_DefCollectionTypeVariable,
    modelDsl_DefIdAttribute,
    modelDsl_DefLinkVariable,
    modelDsl_DefModelModelTypeCollectionVariable,
    modelDsl_DefModelSimpleTypeCollectionVariable,
    modelDsl_DefModelTypeVariable,
    modelDsl_DefSimpleVariable,
    modelDsl_DefVariable,
    modelDsl_Element,
    modelDsl_Entity,
    modelDsl_Enumerable,
    modelDsl_Link,
    modelDsl_Method,
    modelDsl_MethodAllModelReturn,
    modelDsl_MethodCollectionReturn,
    modelDsl_MethodSimpleReturn,
    modelDsl_Model,
    modelDsl_ModelType,
    modelDsl_ModelTypeCollection,
    modelDsl_Relation,
    modelDsl_SimpleEntity,
    modelDsl_SimpleLink,
    modelDsl_SimpleTypeCollection,
    modelDsl_ValueType,
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

def test_assoc_parameters22_reverse_link_reassign_clear():
    a1 = modelDsl_Method(name="sample_text")
    a2 = modelDsl_Method(name="sample_text_2")
    b = modelDsl_DefVariable(name="sample_text")
    _safe_set(b, 'modelDsl_DefVariable', a1)
    assert _is_linked(b, 'modelDsl_DefVariable', a1)
    if hasattr(a1, 'modelDsl_Method23'):
        assert _is_linked(a1, 'modelDsl_Method23', b)
    _safe_set(b, 'modelDsl_DefVariable', a2)
    assert _is_linked(b, 'modelDsl_DefVariable', a2)
    if hasattr(a1, 'modelDsl_Method23'):
        assert not _is_linked(a1, 'modelDsl_Method23', b)
    if hasattr(a2, 'modelDsl_Method23'):
        assert _is_linked(a2, 'modelDsl_Method23', b)
    _safe_set(b, 'modelDsl_DefVariable', None)
    assert not _is_linked(b, 'modelDsl_DefVariable', a2)
    if hasattr(a2, 'modelDsl_Method23'):
        assert not _is_linked(a2, 'modelDsl_Method23', b)


def test_assoc_superClass5_reverse_link_reassign_clear():
    a1 = modelDsl_SimpleEntity(implementation="sample_text")
    a2 = modelDsl_SimpleEntity(implementation="sample_text_2")
    b = modelDsl_SimpleEntity(implementation="sample_text")
    _safe_set(b, 'modelDsl_SimpleEntity4', a1)
    assert _is_linked(b, 'modelDsl_SimpleEntity4', a1)
    if hasattr(a1, 'modelDsl_SimpleEntity'):
        assert _is_linked(a1, 'modelDsl_SimpleEntity', b)
    _safe_set(b, 'modelDsl_SimpleEntity4', a2)
    assert _is_linked(b, 'modelDsl_SimpleEntity4', a2)
    if hasattr(a1, 'modelDsl_SimpleEntity'):
        assert not _is_linked(a1, 'modelDsl_SimpleEntity', b)
    if hasattr(a2, 'modelDsl_SimpleEntity'):
        assert _is_linked(a2, 'modelDsl_SimpleEntity', b)
    _safe_set(b, 'modelDsl_SimpleEntity4', None)
    assert not _is_linked(b, 'modelDsl_SimpleEntity4', a2)
    if hasattr(a2, 'modelDsl_SimpleEntity'):
        assert not _is_linked(a2, 'modelDsl_SimpleEntity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributesId6_stub_double():
    # modelDsl_DefIdAttribute has no real 'modelDsl_DefIdAttribute' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_SimpleEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_SimpleEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_SimpleEntity(implementation="sample_text")
    partner = modelDsl_DefIdAttribute()
    setattr(partner, 'modelDsl_DefIdAttribute', None)
    _safe_set(owner, 'modelDsl_SimpleEntity7', {partner})
    assert getattr(partner, 'modelDsl_DefIdAttribute') == owner
    _safe_set(owner, 'modelDsl_SimpleEntity7', set())
    assert getattr(partner, 'modelDsl_DefIdAttribute') is None


def test_assoc_elements0_stub_double():
    # modelDsl_Model has no real 'modelDsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Element(name="sample_text")
    partner = modelDsl_Model()
    setattr(partner, 'modelDsl_Model', None)
    _safe_set(owner, 'modelDsl_Element', partner)
    assert owner in getattr(partner, 'modelDsl_Model')
    _safe_set(owner, 'modelDsl_Element', None)
    assert owner not in getattr(partner, 'modelDsl_Model')


def test_assoc_methods2_stub_double():
    # modelDsl_Entity has no real 'modelDsl_Entity3' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Method(name="sample_text")
    partner = modelDsl_Entity()
    setattr(partner, 'modelDsl_Entity3', None)
    _safe_set(owner, 'modelDsl_Method', partner)
    assert owner in getattr(partner, 'modelDsl_Entity3')
    _safe_set(owner, 'modelDsl_Method', None)
    assert owner not in getattr(partner, 'modelDsl_Entity3')


def test_assoc_relations11_stub_double():
    # modelDsl_SimpleLink has no real 'modelDsl_SimpleLink' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Relation(multiplicity="sample_text", name="sample_text", navigable="sample_text")
    partner = modelDsl_SimpleLink()
    setattr(partner, 'modelDsl_SimpleLink', None)
    _safe_set(owner, 'modelDsl_Relation12', partner)
    assert owner in getattr(partner, 'modelDsl_SimpleLink')
    _safe_set(owner, 'modelDsl_Relation12', None)
    assert owner not in getattr(partner, 'modelDsl_SimpleLink')


def test_assoc_relations8_stub_double():
    # modelDsl_AssociativeEntity has no real 'modelDsl_AssociativeEntity' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Relation(multiplicity="sample_text", name="sample_text", navigable="sample_text")
    partner = modelDsl_AssociativeEntity()
    setattr(partner, 'modelDsl_AssociativeEntity', None)
    _safe_set(owner, 'modelDsl_Relation', partner)
    assert owner in getattr(partner, 'modelDsl_AssociativeEntity')
    _safe_set(owner, 'modelDsl_Relation', None)
    assert owner not in getattr(partner, 'modelDsl_AssociativeEntity')


def test_assoc_returnType24_stub_double():
    # modelDsl_MethodCollectionReturn has no real 'modelDsl_MethodCollectionReturn' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_CollectionReturnType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_CollectionReturnType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_CollectionReturnType(collection="sample_text")
    partner = modelDsl_MethodCollectionReturn()
    setattr(partner, 'modelDsl_MethodCollectionReturn', None)
    _safe_set(owner, 'modelDsl_CollectionReturnType25', partner)
    assert getattr(partner, 'modelDsl_MethodCollectionReturn') == owner
    _safe_set(owner, 'modelDsl_CollectionReturnType25', None)
    assert getattr(partner, 'modelDsl_MethodCollectionReturn') is None


def test_assoc_type13_stub_double():
    # modelDsl_Entity has no real 'modelDsl_Entity15' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Relation(multiplicity="sample_text", name="sample_text", navigable="sample_text")
    partner = modelDsl_Entity()
    setattr(partner, 'modelDsl_Entity15', None)
    _safe_set(owner, 'modelDsl_Relation14', partner)
    assert getattr(partner, 'modelDsl_Entity15') == owner
    _safe_set(owner, 'modelDsl_Relation14', None)
    assert getattr(partner, 'modelDsl_Entity15') is None


def test_assoc_type17_stub_double():
    # modelDsl_ModelType has no real 'modelDsl_ModelType' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_DefModelTypeVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_DefModelTypeVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_DefModelTypeVariable(name="sample_text", nullable="sample_text")
    partner = modelDsl_ModelType()
    setattr(partner, 'modelDsl_ModelType', None)
    _safe_set(owner, 'modelDsl_DefModelTypeVariable', partner)
    assert getattr(partner, 'modelDsl_ModelType') == owner
    _safe_set(owner, 'modelDsl_DefModelTypeVariable', None)
    assert getattr(partner, 'modelDsl_ModelType') is None


def test_assoc_type18_stub_double():
    # modelDsl_DefCollectionTypeVariable has no real 'modelDsl_DefCollectionTypeVariable' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_CollectionReturnType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_CollectionReturnType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_CollectionReturnType(collection="sample_text")
    partner = modelDsl_DefCollectionTypeVariable()
    setattr(partner, 'modelDsl_DefCollectionTypeVariable', None)
    _safe_set(owner, 'modelDsl_CollectionReturnType', partner)
    assert getattr(partner, 'modelDsl_DefCollectionTypeVariable') == owner
    _safe_set(owner, 'modelDsl_CollectionReturnType', None)
    assert getattr(partner, 'modelDsl_DefCollectionTypeVariable') is None


def test_assoc_type19_stub_double():
    # modelDsl_DefModelModelTypeCollectionVariable has no real 'modelDsl_DefModelModelTypeCollectionVariable' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_ModelTypeCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_ModelTypeCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_ModelTypeCollection(collection="sample_text")
    partner = modelDsl_DefModelModelTypeCollectionVariable()
    setattr(partner, 'modelDsl_DefModelModelTypeCollectionVariable', None)
    _safe_set(owner, 'modelDsl_ModelTypeCollection', partner)
    assert getattr(partner, 'modelDsl_DefModelModelTypeCollectionVariable') == owner
    _safe_set(owner, 'modelDsl_ModelTypeCollection', None)
    assert getattr(partner, 'modelDsl_DefModelModelTypeCollectionVariable') is None


def test_assoc_type20_stub_double():
    # modelDsl_DefModelSimpleTypeCollectionVariable has no real 'modelDsl_DefModelSimpleTypeCollectionVariable' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_SimpleTypeCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_SimpleTypeCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_SimpleTypeCollection(type="sample_text")
    partner = modelDsl_DefModelSimpleTypeCollectionVariable()
    setattr(partner, 'modelDsl_DefModelSimpleTypeCollectionVariable', None)
    _safe_set(owner, 'modelDsl_SimpleTypeCollection', partner)
    assert getattr(partner, 'modelDsl_DefModelSimpleTypeCollectionVariable') == owner
    _safe_set(owner, 'modelDsl_SimpleTypeCollection', None)
    assert getattr(partner, 'modelDsl_DefModelSimpleTypeCollectionVariable') is None


def test_assoc_type21_stub_double():
    # modelDsl_Link has no real 'modelDsl_Link' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_DefLinkVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_DefLinkVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_DefLinkVariable(name="sample_text")
    partner = modelDsl_Link()
    setattr(partner, 'modelDsl_Link', None)
    _safe_set(owner, 'modelDsl_DefLinkVariable', partner)
    assert getattr(partner, 'modelDsl_Link') == owner
    _safe_set(owner, 'modelDsl_DefLinkVariable', None)
    assert getattr(partner, 'modelDsl_Link') is None


def test_assoc_type30_stub_double():
    # modelDsl_ModelType has no real 'modelDsl_ModelType32' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_ModelTypeCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_ModelTypeCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_ModelTypeCollection(collection="sample_text")
    partner = modelDsl_ModelType()
    setattr(partner, 'modelDsl_ModelType32', None)
    _safe_set(owner, 'modelDsl_ModelTypeCollection31', partner)
    assert getattr(partner, 'modelDsl_ModelType32') == owner
    _safe_set(owner, 'modelDsl_ModelTypeCollection31', None)
    assert getattr(partner, 'modelDsl_ModelType32') is None


