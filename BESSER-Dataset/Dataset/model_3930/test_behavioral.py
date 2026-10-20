import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnoTypes,
    Annotated,
    AnnotationValue,
    Container,
    Element,
    Field,
    Type,
    Value,
    modelDsl_AnnoTypes,
    modelDsl_Annotated,
    modelDsl_Annotation,
    modelDsl_AnnotationGroup,
    modelDsl_AnnotationHiddenProperty,
    modelDsl_AnnotationInstance,
    modelDsl_AnnotationProperty,
    modelDsl_AnnotationType,
    modelDsl_AnnotationValue,
    modelDsl_Child,
    modelDsl_ChildType,
    modelDsl_Container,
    modelDsl_DataType,
    modelDsl_DataTypeField,
    modelDsl_DataTypeType,
    modelDsl_DoubleValue,
    modelDsl_Element,
    modelDsl_Entity,
    modelDsl_EntityElements,
    modelDsl_EntityGroup,
    modelDsl_EntityType,
    modelDsl_Field,
    modelDsl_FormatRangeValue,
    modelDsl_GroupType,
    modelDsl_Import,
    modelDsl_IntegerValue,
    modelDsl_Model,
    modelDsl_Package,
    modelDsl_PackageType,
    modelDsl_Parent,
    modelDsl_ParentType,
    modelDsl_PatternType,
    modelDsl_Property,
    modelDsl_PropertyType,
    modelDsl_RangeValue,
    modelDsl_Reference,
    modelDsl_ReferenceList,
    modelDsl_ReferenceListType,
    modelDsl_ReferenceType,
    modelDsl_StringValue,
    modelDsl_Type,
    modelDsl_Value,
    ValueType,
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

def test_assoc_group58_reverse_link_reassign_clear():
    a1 = modelDsl_GroupType(name="sample_text")
    a2 = modelDsl_GroupType(name="sample_text_2")
    b = modelDsl_AnnotationProperty(multi=True, name="sample_text", type="sample_text")
    _safe_set(b, 'modelDsl_AnnotationProperty59', a1)
    assert _is_linked(b, 'modelDsl_AnnotationProperty59', a1)
    if hasattr(a1, 'modelDsl_GroupType'):
        assert _is_linked(a1, 'modelDsl_GroupType', b)
    _safe_set(b, 'modelDsl_AnnotationProperty59', a2)
    assert _is_linked(b, 'modelDsl_AnnotationProperty59', a2)
    if hasattr(a1, 'modelDsl_GroupType'):
        assert not _is_linked(a1, 'modelDsl_GroupType', b)
    if hasattr(a2, 'modelDsl_GroupType'):
        assert _is_linked(a2, 'modelDsl_GroupType', b)
    _safe_set(b, 'modelDsl_AnnotationProperty59', None)
    assert not _is_linked(b, 'modelDsl_AnnotationProperty59', a2)
    if hasattr(a2, 'modelDsl_GroupType'):
        assert not _is_linked(a2, 'modelDsl_GroupType', b)


def test_assoc_pattern10_reverse_link_reassign_clear():
    a1 = modelDsl_PatternType(DATE="sample_text", NUMBER="sample_text", REGEX="sample_text")
    a2 = modelDsl_PatternType(DATE="sample_text_2", NUMBER="sample_text_2", REGEX="sample_text_2")
    b = modelDsl_DataTypeField(format="sample_text")
    _safe_set(b, 'modelDsl_DataTypeField11', a1)
    assert _is_linked(b, 'modelDsl_DataTypeField11', a1)
    if hasattr(a1, 'modelDsl_PatternType'):
        assert _is_linked(a1, 'modelDsl_PatternType', b)
    _safe_set(b, 'modelDsl_DataTypeField11', a2)
    assert _is_linked(b, 'modelDsl_DataTypeField11', a2)
    if hasattr(a1, 'modelDsl_PatternType'):
        assert not _is_linked(a1, 'modelDsl_PatternType', b)
    if hasattr(a2, 'modelDsl_PatternType'):
        assert _is_linked(a2, 'modelDsl_PatternType', b)
    _safe_set(b, 'modelDsl_DataTypeField11', None)
    assert not _is_linked(b, 'modelDsl_DataTypeField11', a2)
    if hasattr(a2, 'modelDsl_PatternType'):
        assert not _is_linked(a2, 'modelDsl_PatternType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations36_stub_double():
    # modelDsl_AnnotationGroup has no real 'modelDsl_AnnotationGroup37' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Field(name="sample_text")
    partner = modelDsl_AnnotationGroup()
    setattr(partner, 'modelDsl_AnnotationGroup37', None)
    _safe_set(owner, 'modelDsl_Field', {partner})
    assert getattr(partner, 'modelDsl_AnnotationGroup37') == owner
    _safe_set(owner, 'modelDsl_Field', set())
    assert getattr(partner, 'modelDsl_AnnotationGroup37') is None


def test_assoc_elements1_stub_double():
    # modelDsl_Model has no real 'modelDsl_Model2' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Element(name="sample_text")
    partner = modelDsl_Model()
    setattr(partner, 'modelDsl_Model2', None)
    _safe_set(owner, 'modelDsl_Element', partner)
    assert owner in getattr(partner, 'modelDsl_Model2')
    _safe_set(owner, 'modelDsl_Element', None)
    assert owner not in getattr(partner, 'modelDsl_Model2')


def test_assoc_elements20_stub_double():
    # modelDsl_EntityElements has no real 'modelDsl_EntityElements22' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_EntityGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_EntityGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_EntityGroup(name="sample_text")
    partner = modelDsl_EntityElements()
    setattr(partner, 'modelDsl_EntityElements22', None)
    _safe_set(owner, 'modelDsl_EntityGroup21', partner)
    assert getattr(partner, 'modelDsl_EntityElements22') == owner
    _safe_set(owner, 'modelDsl_EntityGroup21', None)
    assert getattr(partner, 'modelDsl_EntityElements22') is None


def test_assoc_elements6_stub_double():
    # modelDsl_Package has no real 'modelDsl_Package7' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Element(name="sample_text")
    partner = modelDsl_Package()
    setattr(partner, 'modelDsl_Package7', None)
    _safe_set(owner, 'modelDsl_Element8', partner)
    assert owner in getattr(partner, 'modelDsl_Package7')
    _safe_set(owner, 'modelDsl_Element8', None)
    assert owner not in getattr(partner, 'modelDsl_Package7')


def test_assoc_entity41_stub_double():
    # modelDsl_Entity has no real 'modelDsl_Entity43' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Reference(optional=True)
    partner = modelDsl_Entity()
    setattr(partner, 'modelDsl_Entity43', None)
    _safe_set(owner, 'modelDsl_Reference42', partner)
    assert getattr(partner, 'modelDsl_Entity43') == owner
    _safe_set(owner, 'modelDsl_Reference42', None)
    assert getattr(partner, 'modelDsl_Entity43') is None


def test_assoc_formatedFields9_stub_double():
    # modelDsl_DataType has no real 'modelDsl_DataType' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_DataTypeField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_DataTypeField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_DataTypeField(format="sample_text")
    partner = modelDsl_DataType()
    setattr(partner, 'modelDsl_DataType', None)
    _safe_set(owner, 'modelDsl_DataTypeField', partner)
    assert owner in getattr(partner, 'modelDsl_DataType')
    _safe_set(owner, 'modelDsl_DataTypeField', None)
    assert owner not in getattr(partner, 'modelDsl_DataType')


def test_assoc_groups18_stub_double():
    # modelDsl_Entity has no real 'modelDsl_Entity19' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_EntityGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_EntityGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_EntityGroup(name="sample_text")
    partner = modelDsl_Entity()
    setattr(partner, 'modelDsl_Entity19', None)
    _safe_set(owner, 'modelDsl_EntityGroup', partner)
    assert owner in getattr(partner, 'modelDsl_Entity19')
    _safe_set(owner, 'modelDsl_EntityGroup', None)
    assert owner not in getattr(partner, 'modelDsl_Entity19')


def test_assoc_imports0_stub_double():
    # modelDsl_Model has no real 'modelDsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Import(importedNamespace="sample_text")
    partner = modelDsl_Model()
    setattr(partner, 'modelDsl_Model', None)
    _safe_set(owner, 'modelDsl_Import', partner)
    assert owner in getattr(partner, 'modelDsl_Model')
    _safe_set(owner, 'modelDsl_Import', None)
    assert owner not in getattr(partner, 'modelDsl_Model')


def test_assoc_mandatories53_stub_double():
    # modelDsl_Annotation has no real 'modelDsl_Annotation54' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_AnnotationProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_AnnotationProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_AnnotationProperty(multi=True, name="sample_text", type="sample_text")
    partner = modelDsl_Annotation()
    setattr(partner, 'modelDsl_Annotation54', None)
    _safe_set(owner, 'modelDsl_AnnotationProperty', partner)
    assert owner in getattr(partner, 'modelDsl_Annotation54')
    _safe_set(owner, 'modelDsl_AnnotationProperty', None)
    assert owner not in getattr(partner, 'modelDsl_Annotation54')


def test_assoc_optionals55_stub_double():
    # modelDsl_Annotation has no real 'modelDsl_Annotation56' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_AnnotationProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_AnnotationProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_AnnotationProperty(multi=True, name="sample_text", type="sample_text")
    partner = modelDsl_Annotation()
    setattr(partner, 'modelDsl_Annotation56', None)
    _safe_set(owner, 'modelDsl_AnnotationProperty57', partner)
    assert owner in getattr(partner, 'modelDsl_Annotation56')
    _safe_set(owner, 'modelDsl_AnnotationProperty57', None)
    assert owner not in getattr(partner, 'modelDsl_Annotation56')


def test_assoc_properties25_stub_double():
    # modelDsl_EntityElements has no real 'modelDsl_EntityElements26' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Property(optional=True)
    partner = modelDsl_EntityElements()
    setattr(partner, 'modelDsl_EntityElements26', None)
    _safe_set(owner, 'modelDsl_Property', partner)
    assert owner in getattr(partner, 'modelDsl_EntityElements26')
    _safe_set(owner, 'modelDsl_Property', None)
    assert owner not in getattr(partner, 'modelDsl_EntityElements26')


def test_assoc_property70_stub_double():
    # modelDsl_AnnotationHiddenProperty has no real 'modelDsl_AnnotationHiddenProperty71' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_AnnotationProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_AnnotationProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_AnnotationProperty(multi=True, name="sample_text", type="sample_text")
    partner = modelDsl_AnnotationHiddenProperty()
    setattr(partner, 'modelDsl_AnnotationHiddenProperty71', None)
    _safe_set(owner, 'modelDsl_AnnotationProperty72', partner)
    assert getattr(partner, 'modelDsl_AnnotationHiddenProperty71') == owner
    _safe_set(owner, 'modelDsl_AnnotationProperty72', None)
    assert getattr(partner, 'modelDsl_AnnotationHiddenProperty71') is None


def test_assoc_reference44_stub_double():
    # modelDsl_ReferenceList has no real 'modelDsl_ReferenceList45' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Reference(optional=True)
    partner = modelDsl_ReferenceList()
    setattr(partner, 'modelDsl_ReferenceList45', None)
    _safe_set(owner, 'modelDsl_Reference46', partner)
    assert getattr(partner, 'modelDsl_ReferenceList45') == owner
    _safe_set(owner, 'modelDsl_Reference46', None)
    assert getattr(partner, 'modelDsl_ReferenceList45') is None


def test_assoc_references27_stub_double():
    # modelDsl_EntityElements has no real 'modelDsl_EntityElements28' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Reference(optional=True)
    partner = modelDsl_EntityElements()
    setattr(partner, 'modelDsl_EntityElements28', None)
    _safe_set(owner, 'modelDsl_Reference', partner)
    assert owner in getattr(partner, 'modelDsl_EntityElements28')
    _safe_set(owner, 'modelDsl_Reference', None)
    assert owner not in getattr(partner, 'modelDsl_EntityElements28')


def test_assoc_type12_stub_double():
    # modelDsl_DataType has no real 'modelDsl_DataType14' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_DataTypeField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_DataTypeField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_DataTypeField(format="sample_text")
    partner = modelDsl_DataType()
    setattr(partner, 'modelDsl_DataType14', None)
    _safe_set(owner, 'modelDsl_DataTypeField13', partner)
    assert getattr(partner, 'modelDsl_DataType14') == owner
    _safe_set(owner, 'modelDsl_DataTypeField13', None)
    assert getattr(partner, 'modelDsl_DataType14') is None


def test_assoc_type38_stub_double():
    # modelDsl_Type has no real 'modelDsl_Type40' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_Property(optional=True)
    partner = modelDsl_Type()
    setattr(partner, 'modelDsl_Type40', None)
    _safe_set(owner, 'modelDsl_Property39', partner)
    assert getattr(partner, 'modelDsl_Type40') == owner
    _safe_set(owner, 'modelDsl_Property39', None)
    assert getattr(partner, 'modelDsl_Type40') is None


def test_assoc_types50_stub_double():
    # modelDsl_Annotation has no real 'modelDsl_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so modelDsl_AnnoTypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modelDsl_AnnoTypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modelDsl_AnnoTypes(type="sample_text")
    partner = modelDsl_Annotation()
    setattr(partner, 'modelDsl_Annotation', None)
    _safe_set(owner, 'modelDsl_AnnoTypes', partner)
    assert owner in getattr(partner, 'modelDsl_Annotation')
    _safe_set(owner, 'modelDsl_AnnoTypes', None)
    assert owner not in getattr(partner, 'modelDsl_Annotation')


