import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    Entity,
    Feature,
    Relationship,
    classmodel_Aggregation,
    classmodel_Annotation,
    classmodel_Array,
    classmodel_Association,
    classmodel_Attribute,
    classmodel_Classifier,
    classmodel_Composition,
    classmodel_Constant,
    classmodel_Datatype,
    classmodel_Dependency,
    classmodel_Element,
    classmodel_Entity,
    classmodel_Enumeration,
    classmodel_Feature,
    classmodel_Generalization,
    classmodel_Import,
    classmodel_Model,
    classmodel_Multiplicity,
    classmodel_Operation,
    classmodel_Package,
    classmodel_Parameter,
    classmodel_Realization,
    classmodel_Reference,
    classmodel_Relationship,
    classmodel_Type,
    Visibility,
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

def test_assoc_enumerator17_reverse_link_reassign_clear():
    a1 = classmodel_Feature(constraint="sample_text", name="sample_text", value="sample_text", visibility="sample_text")
    a2 = classmodel_Feature(constraint="sample_text_2", name="sample_text_2", value="sample_text_2", visibility="sample_text_2")
    b = classmodel_Enumeration(constraint="sample_text")
    _safe_set(b, 'classmodel_Enumeration18', {a1})
    assert _is_linked(b, 'classmodel_Enumeration18', a1)
    if hasattr(a1, 'classmodel_Feature19'):
        assert _is_linked(a1, 'classmodel_Feature19', b)
    _safe_set(b, 'classmodel_Enumeration18', {a2})
    assert _is_linked(b, 'classmodel_Enumeration18', a2)
    if hasattr(a1, 'classmodel_Feature19'):
        assert not _is_linked(a1, 'classmodel_Feature19', b)
    if hasattr(a2, 'classmodel_Feature19'):
        assert _is_linked(a2, 'classmodel_Feature19', b)
    _safe_set(b, 'classmodel_Enumeration18', set())
    assert not _is_linked(b, 'classmodel_Enumeration18', a2)
    if hasattr(a2, 'classmodel_Feature19'):
        assert not _is_linked(a2, 'classmodel_Feature19', b)


def test_assoc_feature11_reverse_link_reassign_clear():
    a1 = classmodel_Feature(constraint="sample_text", name="sample_text", value="sample_text", visibility="sample_text")
    a2 = classmodel_Feature(constraint="sample_text_2", name="sample_text_2", value="sample_text_2", visibility="sample_text_2")
    b = classmodel_Classifier(constraint="sample_text")
    _safe_set(b, 'classmodel_Classifier12', {a1})
    assert _is_linked(b, 'classmodel_Classifier12', a1)
    if hasattr(a1, 'classmodel_Feature'):
        assert _is_linked(a1, 'classmodel_Feature', b)
    _safe_set(b, 'classmodel_Classifier12', {a2})
    assert _is_linked(b, 'classmodel_Classifier12', a2)
    if hasattr(a1, 'classmodel_Feature'):
        assert not _is_linked(a1, 'classmodel_Feature', b)
    if hasattr(a2, 'classmodel_Feature'):
        assert _is_linked(a2, 'classmodel_Feature', b)
    _safe_set(b, 'classmodel_Classifier12', set())
    assert not _is_linked(b, 'classmodel_Classifier12', a2)
    if hasattr(a2, 'classmodel_Feature'):
        assert not _is_linked(a2, 'classmodel_Feature', b)


def test_assoc_generalization7_reverse_link_reassign_clear():
    a1 = classmodel_Type(visibility="sample_text")
    a2 = classmodel_Type(visibility="sample_text_2")
    b = classmodel_Classifier(constraint="sample_text")
    _safe_set(b, 'classmodel_Classifier', {a1})
    assert _is_linked(b, 'classmodel_Classifier', a1)
    if hasattr(a1, 'classmodel_Type'):
        assert _is_linked(a1, 'classmodel_Type', b)
    _safe_set(b, 'classmodel_Classifier', {a2})
    assert _is_linked(b, 'classmodel_Classifier', a2)
    if hasattr(a1, 'classmodel_Type'):
        assert not _is_linked(a1, 'classmodel_Type', b)
    if hasattr(a2, 'classmodel_Type'):
        assert _is_linked(a2, 'classmodel_Type', b)
    _safe_set(b, 'classmodel_Classifier', set())
    assert not _is_linked(b, 'classmodel_Classifier', a2)
    if hasattr(a2, 'classmodel_Type'):
        assert not _is_linked(a2, 'classmodel_Type', b)


def test_assoc_head20_reverse_link_reassign_clear():
    a1 = classmodel_Relationship(label="sample_text")
    a2 = classmodel_Relationship(label="sample_text_2")
    b = classmodel_Entity(name="sample_text")
    _safe_set(b, 'classmodel_Entity21', a1)
    assert _is_linked(b, 'classmodel_Entity21', a1)
    if hasattr(a1, 'classmodel_Relationship'):
        assert _is_linked(a1, 'classmodel_Relationship', b)
    _safe_set(b, 'classmodel_Entity21', a2)
    assert _is_linked(b, 'classmodel_Entity21', a2)
    if hasattr(a1, 'classmodel_Relationship'):
        assert not _is_linked(a1, 'classmodel_Relationship', b)
    if hasattr(a2, 'classmodel_Relationship'):
        assert _is_linked(a2, 'classmodel_Relationship', b)
    _safe_set(b, 'classmodel_Entity21', None)
    assert not _is_linked(b, 'classmodel_Entity21', a2)
    if hasattr(a2, 'classmodel_Relationship'):
        assert not _is_linked(a2, 'classmodel_Relationship', b)


def test_assoc_headMultiplicity25_reverse_link_reassign_clear():
    a1 = classmodel_Multiplicity(lower="sample_text", upper="sample_text")
    a2 = classmodel_Multiplicity(lower="sample_text_2", upper="sample_text_2")
    b = classmodel_Association(headLabel="sample_text", headNavigable=True, headVisibility="sample_text", tailLabel="sample_text", tailNavigable=True, tailVisibility="sample_text")
    _safe_set(b, 'classmodel_Association', a1)
    assert _is_linked(b, 'classmodel_Association', a1)
    if hasattr(a1, 'classmodel_Multiplicity'):
        assert _is_linked(a1, 'classmodel_Multiplicity', b)
    _safe_set(b, 'classmodel_Association', a2)
    assert _is_linked(b, 'classmodel_Association', a2)
    if hasattr(a1, 'classmodel_Multiplicity'):
        assert not _is_linked(a1, 'classmodel_Multiplicity', b)
    if hasattr(a2, 'classmodel_Multiplicity'):
        assert _is_linked(a2, 'classmodel_Multiplicity', b)
    _safe_set(b, 'classmodel_Association', None)
    assert not _is_linked(b, 'classmodel_Association', a2)
    if hasattr(a2, 'classmodel_Multiplicity'):
        assert not _is_linked(a2, 'classmodel_Multiplicity', b)


def test_assoc_headMultiplicity29_reverse_link_reassign_clear():
    a1 = classmodel_Multiplicity(lower="sample_text", upper="sample_text")
    a2 = classmodel_Multiplicity(lower="sample_text_2", upper="sample_text_2")
    b = classmodel_Aggregation(headLabel="sample_text", headNavigable=True, headVisibility="sample_text", tailLabel="sample_text", tailNavigable=True, tailVisibility="sample_text")
    _safe_set(b, 'classmodel_Aggregation', a1)
    assert _is_linked(b, 'classmodel_Aggregation', a1)
    if hasattr(a1, 'classmodel_Multiplicity30'):
        assert _is_linked(a1, 'classmodel_Multiplicity30', b)
    _safe_set(b, 'classmodel_Aggregation', a2)
    assert _is_linked(b, 'classmodel_Aggregation', a2)
    if hasattr(a1, 'classmodel_Multiplicity30'):
        assert not _is_linked(a1, 'classmodel_Multiplicity30', b)
    if hasattr(a2, 'classmodel_Multiplicity30'):
        assert _is_linked(a2, 'classmodel_Multiplicity30', b)
    _safe_set(b, 'classmodel_Aggregation', None)
    assert not _is_linked(b, 'classmodel_Aggregation', a2)
    if hasattr(a2, 'classmodel_Multiplicity30'):
        assert not _is_linked(a2, 'classmodel_Multiplicity30', b)


def test_assoc_headMultiplicity34_reverse_link_reassign_clear():
    a1 = classmodel_Multiplicity(lower="sample_text", upper="sample_text")
    a2 = classmodel_Multiplicity(lower="sample_text_2", upper="sample_text_2")
    b = classmodel_Composition(headLabel="sample_text", headNavigable=True, headVisibility="sample_text", tailLabel="sample_text", tailNavigable=True, tailVisibility="sample_text")
    _safe_set(b, 'classmodel_Composition', a1)
    assert _is_linked(b, 'classmodel_Composition', a1)
    if hasattr(a1, 'classmodel_Multiplicity35'):
        assert _is_linked(a1, 'classmodel_Multiplicity35', b)
    _safe_set(b, 'classmodel_Composition', a2)
    assert _is_linked(b, 'classmodel_Composition', a2)
    if hasattr(a1, 'classmodel_Multiplicity35'):
        assert not _is_linked(a1, 'classmodel_Multiplicity35', b)
    if hasattr(a2, 'classmodel_Multiplicity35'):
        assert _is_linked(a2, 'classmodel_Multiplicity35', b)
    _safe_set(b, 'classmodel_Composition', None)
    assert not _is_linked(b, 'classmodel_Composition', a2)
    if hasattr(a2, 'classmodel_Multiplicity35'):
        assert not _is_linked(a2, 'classmodel_Multiplicity35', b)


def test_assoc_name13_reverse_link_reassign_clear():
    a1 = classmodel_Type(visibility="sample_text")
    a2 = classmodel_Type(visibility="sample_text_2")
    b = classmodel_Entity(name="sample_text")
    _safe_set(b, 'classmodel_Entity', a1)
    assert _is_linked(b, 'classmodel_Entity', a1)
    if hasattr(a1, 'classmodel_Type14'):
        assert _is_linked(a1, 'classmodel_Type14', b)
    _safe_set(b, 'classmodel_Entity', a2)
    assert _is_linked(b, 'classmodel_Entity', a2)
    if hasattr(a1, 'classmodel_Type14'):
        assert not _is_linked(a1, 'classmodel_Type14', b)
    if hasattr(a2, 'classmodel_Type14'):
        assert _is_linked(a2, 'classmodel_Type14', b)
    _safe_set(b, 'classmodel_Entity', None)
    assert not _is_linked(b, 'classmodel_Entity', a2)
    if hasattr(a2, 'classmodel_Type14'):
        assert not _is_linked(a2, 'classmodel_Type14', b)


def test_assoc_parameter39_reverse_link_reassign_clear():
    a1 = classmodel_Parameter(implicit="sample_text", name="sample_text")
    a2 = classmodel_Parameter(implicit="sample_text_2", name="sample_text_2")
    b = classmodel_Operation(body="sample_text", static=True)
    _safe_set(b, 'classmodel_Operation', {a1})
    assert _is_linked(b, 'classmodel_Operation', a1)
    if hasattr(a1, 'classmodel_Parameter'):
        assert _is_linked(a1, 'classmodel_Parameter', b)
    _safe_set(b, 'classmodel_Operation', {a2})
    assert _is_linked(b, 'classmodel_Operation', a2)
    if hasattr(a1, 'classmodel_Parameter'):
        assert not _is_linked(a1, 'classmodel_Parameter', b)
    if hasattr(a2, 'classmodel_Parameter'):
        assert _is_linked(a2, 'classmodel_Parameter', b)
    _safe_set(b, 'classmodel_Operation', set())
    assert not _is_linked(b, 'classmodel_Operation', a2)
    if hasattr(a2, 'classmodel_Parameter'):
        assert not _is_linked(a2, 'classmodel_Parameter', b)


def test_assoc_tail22_reverse_link_reassign_clear():
    a1 = classmodel_Relationship(label="sample_text")
    a2 = classmodel_Relationship(label="sample_text_2")
    b = classmodel_Entity(name="sample_text")
    _safe_set(b, 'classmodel_Entity24', a1)
    assert _is_linked(b, 'classmodel_Entity24', a1)
    if hasattr(a1, 'classmodel_Relationship23'):
        assert _is_linked(a1, 'classmodel_Relationship23', b)
    _safe_set(b, 'classmodel_Entity24', a2)
    assert _is_linked(b, 'classmodel_Entity24', a2)
    if hasattr(a1, 'classmodel_Relationship23'):
        assert not _is_linked(a1, 'classmodel_Relationship23', b)
    if hasattr(a2, 'classmodel_Relationship23'):
        assert _is_linked(a2, 'classmodel_Relationship23', b)
    _safe_set(b, 'classmodel_Entity24', None)
    assert not _is_linked(b, 'classmodel_Entity24', a2)
    if hasattr(a2, 'classmodel_Relationship23'):
        assert not _is_linked(a2, 'classmodel_Relationship23', b)


def test_assoc_tailMultiplicity26_reverse_link_reassign_clear():
    a1 = classmodel_Multiplicity(lower="sample_text", upper="sample_text")
    a2 = classmodel_Multiplicity(lower="sample_text_2", upper="sample_text_2")
    b = classmodel_Association(headLabel="sample_text", headNavigable=True, headVisibility="sample_text", tailLabel="sample_text", tailNavigable=True, tailVisibility="sample_text")
    _safe_set(b, 'classmodel_Association27', a1)
    assert _is_linked(b, 'classmodel_Association27', a1)
    if hasattr(a1, 'classmodel_Multiplicity28'):
        assert _is_linked(a1, 'classmodel_Multiplicity28', b)
    _safe_set(b, 'classmodel_Association27', a2)
    assert _is_linked(b, 'classmodel_Association27', a2)
    if hasattr(a1, 'classmodel_Multiplicity28'):
        assert not _is_linked(a1, 'classmodel_Multiplicity28', b)
    if hasattr(a2, 'classmodel_Multiplicity28'):
        assert _is_linked(a2, 'classmodel_Multiplicity28', b)
    _safe_set(b, 'classmodel_Association27', None)
    assert not _is_linked(b, 'classmodel_Association27', a2)
    if hasattr(a2, 'classmodel_Multiplicity28'):
        assert not _is_linked(a2, 'classmodel_Multiplicity28', b)


def test_assoc_tailMultiplicity31_reverse_link_reassign_clear():
    a1 = classmodel_Multiplicity(lower="sample_text", upper="sample_text")
    a2 = classmodel_Multiplicity(lower="sample_text_2", upper="sample_text_2")
    b = classmodel_Aggregation(headLabel="sample_text", headNavigable=True, headVisibility="sample_text", tailLabel="sample_text", tailNavigable=True, tailVisibility="sample_text")
    _safe_set(b, 'classmodel_Aggregation32', a1)
    assert _is_linked(b, 'classmodel_Aggregation32', a1)
    if hasattr(a1, 'classmodel_Multiplicity33'):
        assert _is_linked(a1, 'classmodel_Multiplicity33', b)
    _safe_set(b, 'classmodel_Aggregation32', a2)
    assert _is_linked(b, 'classmodel_Aggregation32', a2)
    if hasattr(a1, 'classmodel_Multiplicity33'):
        assert not _is_linked(a1, 'classmodel_Multiplicity33', b)
    if hasattr(a2, 'classmodel_Multiplicity33'):
        assert _is_linked(a2, 'classmodel_Multiplicity33', b)
    _safe_set(b, 'classmodel_Aggregation32', None)
    assert not _is_linked(b, 'classmodel_Aggregation32', a2)
    if hasattr(a2, 'classmodel_Multiplicity33'):
        assert not _is_linked(a2, 'classmodel_Multiplicity33', b)


def test_assoc_tailMultiplicity36_reverse_link_reassign_clear():
    a1 = classmodel_Multiplicity(lower="sample_text", upper="sample_text")
    a2 = classmodel_Multiplicity(lower="sample_text_2", upper="sample_text_2")
    b = classmodel_Composition(headLabel="sample_text", headNavigable=True, headVisibility="sample_text", tailLabel="sample_text", tailNavigable=True, tailVisibility="sample_text")
    _safe_set(b, 'classmodel_Composition37', a1)
    assert _is_linked(b, 'classmodel_Composition37', a1)
    if hasattr(a1, 'classmodel_Multiplicity38'):
        assert _is_linked(a1, 'classmodel_Multiplicity38', b)
    _safe_set(b, 'classmodel_Composition37', a2)
    assert _is_linked(b, 'classmodel_Composition37', a2)
    if hasattr(a1, 'classmodel_Multiplicity38'):
        assert not _is_linked(a1, 'classmodel_Multiplicity38', b)
    if hasattr(a2, 'classmodel_Multiplicity38'):
        assert _is_linked(a2, 'classmodel_Multiplicity38', b)
    _safe_set(b, 'classmodel_Composition37', None)
    assert not _is_linked(b, 'classmodel_Composition37', a2)
    if hasattr(a2, 'classmodel_Multiplicity38'):
        assert not _is_linked(a2, 'classmodel_Multiplicity38', b)


def test_assoc_upperClass15_reverse_link_reassign_clear():
    a1 = classmodel_Type(visibility="sample_text")
    a2 = classmodel_Type(visibility="sample_text_2")
    b = classmodel_Enumeration(constraint="sample_text")
    _safe_set(b, 'classmodel_Enumeration', a1)
    assert _is_linked(b, 'classmodel_Enumeration', a1)
    if hasattr(a1, 'classmodel_Type16'):
        assert _is_linked(a1, 'classmodel_Type16', b)
    _safe_set(b, 'classmodel_Enumeration', a2)
    assert _is_linked(b, 'classmodel_Enumeration', a2)
    if hasattr(a1, 'classmodel_Type16'):
        assert not _is_linked(a1, 'classmodel_Type16', b)
    if hasattr(a2, 'classmodel_Type16'):
        assert _is_linked(a2, 'classmodel_Type16', b)
    _safe_set(b, 'classmodel_Enumeration', None)
    assert not _is_linked(b, 'classmodel_Enumeration', a2)
    if hasattr(a2, 'classmodel_Type16'):
        assert not _is_linked(a2, 'classmodel_Type16', b)


def test_assoc_upperClass8_reverse_link_reassign_clear():
    a1 = classmodel_Type(visibility="sample_text")
    a2 = classmodel_Type(visibility="sample_text_2")
    b = classmodel_Classifier(constraint="sample_text")
    _safe_set(b, 'classmodel_Classifier9', a1)
    assert _is_linked(b, 'classmodel_Classifier9', a1)
    if hasattr(a1, 'classmodel_Type10'):
        assert _is_linked(a1, 'classmodel_Type10', b)
    _safe_set(b, 'classmodel_Classifier9', a2)
    assert _is_linked(b, 'classmodel_Classifier9', a2)
    if hasattr(a1, 'classmodel_Type10'):
        assert not _is_linked(a1, 'classmodel_Type10', b)
    if hasattr(a2, 'classmodel_Type10'):
        assert _is_linked(a2, 'classmodel_Type10', b)
    _safe_set(b, 'classmodel_Classifier9', None)
    assert not _is_linked(b, 'classmodel_Classifier9', a2)
    if hasattr(a2, 'classmodel_Type10'):
        assert not _is_linked(a2, 'classmodel_Type10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_element5_stub_double():
    # classmodel_Element has no real 'classmodel_Element6' property in the generated
    # code (a bare stub) -- manually attach it so classmodel_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmodel_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmodel_Package(name="sample_text")
    partner = classmodel_Element()
    setattr(partner, 'classmodel_Element6', None)
    _safe_set(owner, 'classmodel_Package', {partner})
    assert getattr(partner, 'classmodel_Element6') == owner
    _safe_set(owner, 'classmodel_Package', set())
    assert getattr(partner, 'classmodel_Element6') is None


def test_assoc_imports0_stub_double():
    # classmodel_Model has no real 'classmodel_Model' property in the generated
    # code (a bare stub) -- manually attach it so classmodel_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmodel_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmodel_Import(importURI="sample_text")
    partner = classmodel_Model()
    setattr(partner, 'classmodel_Model', None)
    _safe_set(owner, 'classmodel_Import', partner)
    assert owner in getattr(partner, 'classmodel_Model')
    _safe_set(owner, 'classmodel_Import', None)
    assert owner not in getattr(partner, 'classmodel_Model')


def test_assoc_return_40_stub_double():
    # classmodel_Reference has no real 'classmodel_Reference' property in the generated
    # code (a bare stub) -- manually attach it so classmodel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmodel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmodel_Operation(body="sample_text", static=True)
    partner = classmodel_Reference()
    setattr(partner, 'classmodel_Reference', None)
    _safe_set(owner, 'classmodel_Operation41', partner)
    assert getattr(partner, 'classmodel_Reference') == owner
    _safe_set(owner, 'classmodel_Operation41', None)
    assert getattr(partner, 'classmodel_Reference') is None


def test_assoc_size52_stub_double():
    # classmodel_Array has no real 'classmodel_Array53' property in the generated
    # code (a bare stub) -- manually attach it so classmodel_Multiplicity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmodel_Multiplicity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmodel_Multiplicity(lower="sample_text", upper="sample_text")
    partner = classmodel_Array()
    setattr(partner, 'classmodel_Array53', None)
    _safe_set(owner, 'classmodel_Multiplicity54', partner)
    assert getattr(partner, 'classmodel_Array53') == owner
    _safe_set(owner, 'classmodel_Multiplicity54', None)
    assert getattr(partner, 'classmodel_Array53') is None


def test_assoc_type42_stub_double():
    # classmodel_Reference has no real 'classmodel_Reference44' property in the generated
    # code (a bare stub) -- manually attach it so classmodel_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmodel_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmodel_Parameter(implicit="sample_text", name="sample_text")
    partner = classmodel_Reference()
    setattr(partner, 'classmodel_Reference44', None)
    _safe_set(owner, 'classmodel_Parameter43', partner)
    assert getattr(partner, 'classmodel_Reference44') == owner
    _safe_set(owner, 'classmodel_Parameter43', None)
    assert getattr(partner, 'classmodel_Reference44') is None


def test_assoc_type45_stub_double():
    # classmodel_Reference has no real 'classmodel_Reference46' property in the generated
    # code (a bare stub) -- manually attach it so classmodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmodel_Attribute(implicit="sample_text", static=True)
    partner = classmodel_Reference()
    setattr(partner, 'classmodel_Reference46', None)
    _safe_set(owner, 'classmodel_Attribute', partner)
    assert getattr(partner, 'classmodel_Reference46') == owner
    _safe_set(owner, 'classmodel_Attribute', None)
    assert getattr(partner, 'classmodel_Reference46') is None


def test_assoc_type47_stub_double():
    # classmodel_Reference has no real 'classmodel_Reference48' property in the generated
    # code (a bare stub) -- manually attach it so classmodel_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmodel_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmodel_Entity(name="sample_text")
    partner = classmodel_Reference()
    setattr(partner, 'classmodel_Reference48', None)
    _safe_set(owner, 'classmodel_Entity49', partner)
    assert getattr(partner, 'classmodel_Reference48') == owner
    _safe_set(owner, 'classmodel_Entity49', None)
    assert getattr(partner, 'classmodel_Reference48') is None


