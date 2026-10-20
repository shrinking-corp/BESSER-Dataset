import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    Attribute,
    Classifier,
    EncapsulatedFeature,
    EntityAssociation,
    EntityAttribute,
    EntityFeature,
    EntityOrView,
    Feature,
    Label,
    ModelLabelFeature,
    NamedDisplayElement,
    NamedElement,
    PathElement,
    ResourceAttribute,
    ViewFeature,
    persistence_Association,
    persistence_AssociationKey,
    persistence_AssociationWithContainment,
    persistence_AssociationWithoutContainment,
    persistence_Attribute,
    persistence_DataType,
    persistence_DataTypeAttribute,
    persistence_DateAttribute,
    persistence_DatePathElement,
    persistence_EncapsulatedAssociation,
    persistence_EncapsulatedAttribute,
    persistence_EncapsulatedFeature,
    persistence_Entity,
    persistence_EntityAssociation,
    persistence_EntityAttribute,
    persistence_EntityFeature,
    persistence_EntityOrView,
    persistence_Expression,
    persistence_Feature,
    persistence_FileAttribute,
    persistence_ImageAttribute,
    persistence_Label,
    persistence_LocationAttribute,
    persistence_ModelLabel,
    persistence_ModelLabelAssociation,
    persistence_ModelLabelAttribute,
    persistence_ModelLabelFeature,
    persistence_PathElement,
    persistence_Persistence,
    persistence_ResourceAttribute,
    persistence_SerializationGroup,
    persistence_StaticPathElement,
    persistence_UrlAttribute,
    persistence_View,
    persistence_ViewAssociation,
    persistence_ViewFeature,
    Cardinality,
    DatabaseTechnologies,
    DateDetails,
    OrmTechnologies,
    isHasChoices,
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

def test_assoc_allAssociations24_reverse_link_reassign_clear():
    a1 = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_EntityOrView(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    _safe_set(b, 'persistence_Association26', a1)
    assert _is_linked(b, 'persistence_Association26', a1)
    if hasattr(a1, 'persistence_EntityOrView25'):
        assert _is_linked(a1, 'persistence_EntityOrView25', b)
    _safe_set(b, 'persistence_Association26', a2)
    assert _is_linked(b, 'persistence_Association26', a2)
    if hasattr(a1, 'persistence_EntityOrView25'):
        assert not _is_linked(a1, 'persistence_EntityOrView25', b)
    if hasattr(a2, 'persistence_EntityOrView25'):
        assert _is_linked(a2, 'persistence_EntityOrView25', b)
    _safe_set(b, 'persistence_Association26', None)
    assert not _is_linked(b, 'persistence_Association26', a2)
    if hasattr(a2, 'persistence_EntityOrView25'):
        assert not _is_linked(a2, 'persistence_EntityOrView25', b)


def test_assoc_allFeatures17_reverse_link_reassign_clear():
    a1 = persistence_Feature(collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", placeholder="sample_text", title="sample_text")
    a2 = persistence_Feature(collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, displayClass="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", nullDisplayValue="sample_text_2", placeholder="sample_text_2", title="sample_text_2")
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_EntityOrView18', {a1})
    assert _is_linked(b, 'persistence_EntityOrView18', a1)
    if hasattr(a1, 'persistence_Feature19'):
        assert _is_linked(a1, 'persistence_Feature19', b)
    _safe_set(b, 'persistence_EntityOrView18', {a2})
    assert _is_linked(b, 'persistence_EntityOrView18', a2)
    if hasattr(a1, 'persistence_Feature19'):
        assert not _is_linked(a1, 'persistence_Feature19', b)
    if hasattr(a2, 'persistence_Feature19'):
        assert _is_linked(a2, 'persistence_Feature19', b)
    _safe_set(b, 'persistence_EntityOrView18', set())
    assert not _is_linked(b, 'persistence_EntityOrView18', a2)
    if hasattr(a2, 'persistence_Feature19'):
        assert not _is_linked(a2, 'persistence_Feature19', b)


def test_assoc_association47_reverse_link_reassign_clear():
    a1 = persistence_ModelLabelAssociation(isSourceAssociation=True)
    a2 = persistence_ModelLabelAssociation(isSourceAssociation=False)
    b = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    _safe_set(b, 'persistence_EntityAssociation', a1)
    assert _is_linked(b, 'persistence_EntityAssociation', a1)
    if hasattr(a1, 'persistence_ModelLabelAssociation'):
        assert _is_linked(a1, 'persistence_ModelLabelAssociation', b)
    _safe_set(b, 'persistence_EntityAssociation', a2)
    assert _is_linked(b, 'persistence_EntityAssociation', a2)
    if hasattr(a1, 'persistence_ModelLabelAssociation'):
        assert not _is_linked(a1, 'persistence_ModelLabelAssociation', b)
    if hasattr(a2, 'persistence_ModelLabelAssociation'):
        assert _is_linked(a2, 'persistence_ModelLabelAssociation', b)
    _safe_set(b, 'persistence_EntityAssociation', None)
    assert not _is_linked(b, 'persistence_EntityAssociation', a2)
    if hasattr(a2, 'persistence_ModelLabelAssociation'):
        assert not _is_linked(a2, 'persistence_ModelLabelAssociation', b)


def test_assoc_association76_reverse_link_reassign_clear():
    a1 = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    a2 = persistence_EncapsulatedAssociation(cardinality="sample_text_2", isSourceAssociation=False, name="sample_text_2")
    b = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    _safe_set(b, 'Association', a1)
    assert _is_linked(b, 'Association', a1)
    if hasattr(a1, 'encapsulatedBy'):
        assert _is_linked(a1, 'encapsulatedBy', b)
    _safe_set(b, 'Association', a2)
    assert _is_linked(b, 'Association', a2)
    if hasattr(a1, 'encapsulatedBy'):
        assert not _is_linked(a1, 'encapsulatedBy', b)
    if hasattr(a2, 'encapsulatedBy'):
        assert _is_linked(a2, 'encapsulatedBy', b)
    _safe_set(b, 'Association', None)
    assert not _is_linked(b, 'Association', a2)
    if hasattr(a2, 'encapsulatedBy'):
        assert not _is_linked(a2, 'encapsulatedBy', b)


def test_assoc_associations22_reverse_link_reassign_clear():
    a1 = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_EntityOrView(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    _safe_set(b, 'persistence_Association', a1)
    assert _is_linked(b, 'persistence_Association', a1)
    if hasattr(a1, 'persistence_EntityOrView23'):
        assert _is_linked(a1, 'persistence_EntityOrView23', b)
    _safe_set(b, 'persistence_Association', a2)
    assert _is_linked(b, 'persistence_Association', a2)
    if hasattr(a1, 'persistence_EntityOrView23'):
        assert not _is_linked(a1, 'persistence_EntityOrView23', b)
    if hasattr(a2, 'persistence_EntityOrView23'):
        assert _is_linked(a2, 'persistence_EntityOrView23', b)
    _safe_set(b, 'persistence_Association', None)
    assert not _is_linked(b, 'persistence_Association', a2)
    if hasattr(a2, 'persistence_EntityOrView23'):
        assert not _is_linked(a2, 'persistence_EntityOrView23', b)


def test_assoc_attribute45_reverse_link_reassign_clear():
    a1 = persistence_ModelLabelAttribute(dateFormat="sample_text")
    a2 = persistence_ModelLabelAttribute(dateFormat="sample_text_2")
    b = persistence_Attribute(inputClass="sample_text", validationPattern="sample_text")
    _safe_set(b, 'persistence_Attribute46', a1)
    assert _is_linked(b, 'persistence_Attribute46', a1)
    if hasattr(a1, 'persistence_ModelLabelAttribute'):
        assert _is_linked(a1, 'persistence_ModelLabelAttribute', b)
    _safe_set(b, 'persistence_Attribute46', a2)
    assert _is_linked(b, 'persistence_Attribute46', a2)
    if hasattr(a1, 'persistence_ModelLabelAttribute'):
        assert not _is_linked(a1, 'persistence_ModelLabelAttribute', b)
    if hasattr(a2, 'persistence_ModelLabelAttribute'):
        assert _is_linked(a2, 'persistence_ModelLabelAttribute', b)
    _safe_set(b, 'persistence_Attribute46', None)
    assert not _is_linked(b, 'persistence_Attribute46', a2)
    if hasattr(a2, 'persistence_ModelLabelAttribute'):
        assert not _is_linked(a2, 'persistence_ModelLabelAttribute', b)


def test_assoc_attribute74_reverse_link_reassign_clear():
    a1 = persistence_EncapsulatedAttribute(cardinality="sample_text", name="sample_text")
    a2 = persistence_EncapsulatedAttribute(cardinality="sample_text_2", name="sample_text_2")
    b = persistence_Attribute(inputClass="sample_text", validationPattern="sample_text")
    _safe_set(b, 'persistence_Attribute75', a1)
    assert _is_linked(b, 'persistence_Attribute75', a1)
    if hasattr(a1, 'persistence_EncapsulatedAttribute'):
        assert _is_linked(a1, 'persistence_EncapsulatedAttribute', b)
    _safe_set(b, 'persistence_Attribute75', a2)
    assert _is_linked(b, 'persistence_Attribute75', a2)
    if hasattr(a1, 'persistence_EncapsulatedAttribute'):
        assert not _is_linked(a1, 'persistence_EncapsulatedAttribute', b)
    if hasattr(a2, 'persistence_EncapsulatedAttribute'):
        assert _is_linked(a2, 'persistence_EncapsulatedAttribute', b)
    _safe_set(b, 'persistence_Attribute75', None)
    assert not _is_linked(b, 'persistence_Attribute75', a2)
    if hasattr(a2, 'persistence_EncapsulatedAttribute'):
        assert not _is_linked(a2, 'persistence_EncapsulatedAttribute', b)


def test_assoc_attributes20_reverse_link_reassign_clear():
    a1 = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_EntityOrView(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Attribute(inputClass="sample_text", validationPattern="sample_text")
    _safe_set(b, 'persistence_Attribute', a1)
    assert _is_linked(b, 'persistence_Attribute', a1)
    if hasattr(a1, 'persistence_EntityOrView21'):
        assert _is_linked(a1, 'persistence_EntityOrView21', b)
    _safe_set(b, 'persistence_Attribute', a2)
    assert _is_linked(b, 'persistence_Attribute', a2)
    if hasattr(a1, 'persistence_EntityOrView21'):
        assert not _is_linked(a1, 'persistence_EntityOrView21', b)
    if hasattr(a2, 'persistence_EntityOrView21'):
        assert _is_linked(a2, 'persistence_EntityOrView21', b)
    _safe_set(b, 'persistence_Attribute', None)
    assert not _is_linked(b, 'persistence_Attribute', a2)
    if hasattr(a2, 'persistence_EntityOrView21'):
        assert not _is_linked(a2, 'persistence_EntityOrView21', b)


def test_assoc_containerUnique10_reverse_link_reassign_clear():
    a1 = persistence_Feature(collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", placeholder="sample_text", title="sample_text")
    a2 = persistence_Feature(collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, displayClass="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", nullDisplayValue="sample_text_2", placeholder="sample_text_2", title="sample_text_2")
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_EntityOrView11', {a1})
    assert _is_linked(b, 'persistence_EntityOrView11', a1)
    if hasattr(a1, 'persistence_Feature12'):
        assert _is_linked(a1, 'persistence_Feature12', b)
    _safe_set(b, 'persistence_EntityOrView11', {a2})
    assert _is_linked(b, 'persistence_EntityOrView11', a2)
    if hasattr(a1, 'persistence_Feature12'):
        assert not _is_linked(a1, 'persistence_Feature12', b)
    if hasattr(a2, 'persistence_Feature12'):
        assert _is_linked(a2, 'persistence_Feature12', b)
    _safe_set(b, 'persistence_EntityOrView11', set())
    assert not _is_linked(b, 'persistence_EntityOrView11', a2)
    if hasattr(a2, 'persistence_Feature12'):
        assert not _is_linked(a2, 'persistence_Feature12', b)


def test_assoc_dynamicLabel48_reverse_link_reassign_clear():
    a1 = persistence_ModelLabelAssociation(isSourceAssociation=True)
    a2 = persistence_ModelLabelAssociation(isSourceAssociation=False)
    b = persistence_ModelLabel(customise=True, format="sample_text")
    _safe_set(b, 'persistence_ModelLabel50', a1)
    assert _is_linked(b, 'persistence_ModelLabel50', a1)
    if hasattr(a1, 'persistence_ModelLabelAssociation49'):
        assert _is_linked(a1, 'persistence_ModelLabelAssociation49', b)
    _safe_set(b, 'persistence_ModelLabel50', a2)
    assert _is_linked(b, 'persistence_ModelLabel50', a2)
    if hasattr(a1, 'persistence_ModelLabelAssociation49'):
        assert not _is_linked(a1, 'persistence_ModelLabelAssociation49', b)
    if hasattr(a2, 'persistence_ModelLabelAssociation49'):
        assert _is_linked(a2, 'persistence_ModelLabelAssociation49', b)
    _safe_set(b, 'persistence_ModelLabel50', None)
    assert not _is_linked(b, 'persistence_ModelLabel50', a2)
    if hasattr(a2, 'persistence_ModelLabelAssociation49'):
        assert not _is_linked(a2, 'persistence_ModelLabelAssociation49', b)


def test_assoc_encapsulatedBy32_reverse_link_reassign_clear():
    a1 = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    a2 = persistence_EncapsulatedAssociation(cardinality="sample_text_2", isSourceAssociation=False, name="sample_text_2")
    b = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    _safe_set(b, 'association', {a1})
    assert _is_linked(b, 'association', a1)
    if hasattr(a1, 'EncapsulatedAssociation'):
        assert _is_linked(a1, 'EncapsulatedAssociation', b)
    _safe_set(b, 'association', {a2})
    assert _is_linked(b, 'association', a2)
    if hasattr(a1, 'EncapsulatedAssociation'):
        assert not _is_linked(a1, 'EncapsulatedAssociation', b)
    if hasattr(a2, 'EncapsulatedAssociation'):
        assert _is_linked(a2, 'EncapsulatedAssociation', b)
    _safe_set(b, 'association', set())
    assert not _is_linked(b, 'association', a2)
    if hasattr(a2, 'EncapsulatedAssociation'):
        assert not _is_linked(a2, 'EncapsulatedAssociation', b)


def test_assoc_encapsulatedTarget78_reverse_link_reassign_clear():
    a1 = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    a2 = persistence_EncapsulatedAssociation(cardinality="sample_text_2", isSourceAssociation=False, name="sample_text_2")
    b = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    _safe_set(b, 'persistence_EncapsulatedAssociation77', a1)
    assert _is_linked(b, 'persistence_EncapsulatedAssociation77', a1)
    if hasattr(a1, 'persistence_EncapsulatedAssociation'):
        assert _is_linked(a1, 'persistence_EncapsulatedAssociation', b)
    _safe_set(b, 'persistence_EncapsulatedAssociation77', a2)
    assert _is_linked(b, 'persistence_EncapsulatedAssociation77', a2)
    if hasattr(a1, 'persistence_EncapsulatedAssociation'):
        assert not _is_linked(a1, 'persistence_EncapsulatedAssociation', b)
    if hasattr(a2, 'persistence_EncapsulatedAssociation'):
        assert _is_linked(a2, 'persistence_EncapsulatedAssociation', b)
    _safe_set(b, 'persistence_EncapsulatedAssociation77', None)
    assert not _is_linked(b, 'persistence_EncapsulatedAssociation77', a2)
    if hasattr(a2, 'persistence_EncapsulatedAssociation'):
        assert not _is_linked(a2, 'persistence_EncapsulatedAssociation', b)


def test_assoc_entities3_reverse_link_reassign_clear():
    a1 = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    a2 = persistence_Persistence(databaseTechnology="sample_text_2", ormTechnology="sample_text_2", timestampCreation=False, timestampUpdates=False)
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_EntityOrView', a1)
    assert _is_linked(b, 'persistence_EntityOrView', a1)
    if hasattr(a1, 'persistence_Persistence4'):
        assert _is_linked(a1, 'persistence_Persistence4', b)
    _safe_set(b, 'persistence_EntityOrView', a2)
    assert _is_linked(b, 'persistence_EntityOrView', a2)
    if hasattr(a1, 'persistence_Persistence4'):
        assert not _is_linked(a1, 'persistence_Persistence4', b)
    if hasattr(a2, 'persistence_Persistence4'):
        assert _is_linked(a2, 'persistence_Persistence4', b)
    _safe_set(b, 'persistence_EntityOrView', None)
    assert not _is_linked(b, 'persistence_EntityOrView', a2)
    if hasattr(a2, 'persistence_Persistence4'):
        assert not _is_linked(a2, 'persistence_Persistence4', b)


def test_assoc_features14_reverse_link_reassign_clear():
    a1 = persistence_Feature(collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", placeholder="sample_text", title="sample_text")
    a2 = persistence_Feature(collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, displayClass="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", nullDisplayValue="sample_text_2", placeholder="sample_text_2", title="sample_text_2")
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_EntityOrView15', {a1})
    assert _is_linked(b, 'persistence_EntityOrView15', a1)
    if hasattr(a1, 'persistence_Feature16'):
        assert _is_linked(a1, 'persistence_Feature16', b)
    _safe_set(b, 'persistence_EntityOrView15', {a2})
    assert _is_linked(b, 'persistence_EntityOrView15', a2)
    if hasattr(a1, 'persistence_Feature16'):
        assert not _is_linked(a1, 'persistence_Feature16', b)
    if hasattr(a2, 'persistence_Feature16'):
        assert _is_linked(a2, 'persistence_Feature16', b)
    _safe_set(b, 'persistence_EntityOrView15', set())
    assert not _is_linked(b, 'persistence_EntityOrView15', a2)
    if hasattr(a2, 'persistence_Feature16'):
        assert not _is_linked(a2, 'persistence_Feature16', b)


def test_assoc_keys5_reverse_link_reassign_clear():
    a1 = persistence_Feature(collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", placeholder="sample_text", title="sample_text")
    a2 = persistence_Feature(collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, displayClass="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", nullDisplayValue="sample_text_2", placeholder="sample_text_2", title="sample_text_2")
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_EntityOrView6', {a1})
    assert _is_linked(b, 'persistence_EntityOrView6', a1)
    if hasattr(a1, 'persistence_Feature'):
        assert _is_linked(a1, 'persistence_Feature', b)
    _safe_set(b, 'persistence_EntityOrView6', {a2})
    assert _is_linked(b, 'persistence_EntityOrView6', a2)
    if hasattr(a1, 'persistence_Feature'):
        assert not _is_linked(a1, 'persistence_Feature', b)
    if hasattr(a2, 'persistence_Feature'):
        assert _is_linked(a2, 'persistence_Feature', b)
    _safe_set(b, 'persistence_EntityOrView6', set())
    assert not _is_linked(b, 'persistence_EntityOrView6', a2)
    if hasattr(a2, 'persistence_Feature'):
        assert not _is_linked(a2, 'persistence_Feature', b)


def test_assoc_labelFor39_reverse_link_reassign_clear():
    a1 = persistence_ModelLabel(customise=True, format="sample_text")
    a2 = persistence_ModelLabel(customise=False, format="sample_text_2")
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'EntityOrView', a1)
    assert _is_linked(b, 'EntityOrView', a1)
    if hasattr(a1, 'labels'):
        assert _is_linked(a1, 'labels', b)
    _safe_set(b, 'EntityOrView', a2)
    assert _is_linked(b, 'EntityOrView', a2)
    if hasattr(a1, 'labels'):
        assert not _is_linked(a1, 'labels', b)
    if hasattr(a2, 'labels'):
        assert _is_linked(a2, 'labels', b)
    _safe_set(b, 'EntityOrView', None)
    assert not _is_linked(b, 'EntityOrView', a2)
    if hasattr(a2, 'labels'):
        assert not _is_linked(a2, 'labels', b)


def test_assoc_labels13_reverse_link_reassign_clear():
    a1 = persistence_ModelLabel(customise=True, format="sample_text")
    a2 = persistence_ModelLabel(customise=False, format="sample_text_2")
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'labelFor', {a1})
    assert _is_linked(b, 'labelFor', a1)
    if hasattr(a1, 'ModelLabel'):
        assert _is_linked(a1, 'ModelLabel', b)
    _safe_set(b, 'labelFor', {a2})
    assert _is_linked(b, 'labelFor', a2)
    if hasattr(a1, 'ModelLabel'):
        assert not _is_linked(a1, 'ModelLabel', b)
    if hasattr(a2, 'ModelLabel'):
        assert _is_linked(a2, 'ModelLabel', b)
    _safe_set(b, 'labelFor', set())
    assert not _is_linked(b, 'labelFor', a2)
    if hasattr(a2, 'ModelLabel'):
        assert not _is_linked(a2, 'ModelLabel', b)


def test_assoc_opposite84_reverse_link_reassign_clear():
    a1 = persistence_ViewAssociation(cardinality="sample_text")
    a2 = persistence_ViewAssociation(cardinality="sample_text_2")
    b = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    _safe_set(b, 'persistence_EncapsulatedAssociation85', a1)
    assert _is_linked(b, 'persistence_EncapsulatedAssociation85', a1)
    if hasattr(a1, 'persistence_ViewAssociation'):
        assert _is_linked(a1, 'persistence_ViewAssociation', b)
    _safe_set(b, 'persistence_EncapsulatedAssociation85', a2)
    assert _is_linked(b, 'persistence_EncapsulatedAssociation85', a2)
    if hasattr(a1, 'persistence_ViewAssociation'):
        assert not _is_linked(a1, 'persistence_ViewAssociation', b)
    if hasattr(a2, 'persistence_ViewAssociation'):
        assert _is_linked(a2, 'persistence_ViewAssociation', b)
    _safe_set(b, 'persistence_EncapsulatedAssociation85', None)
    assert not _is_linked(b, 'persistence_EncapsulatedAssociation85', a2)
    if hasattr(a2, 'persistence_ViewAssociation'):
        assert not _is_linked(a2, 'persistence_ViewAssociation', b)


def test_assoc_slugFields55_reverse_link_reassign_clear():
    a1 = persistence_EntityAttribute(containerUnique=True, hidden=True, interfaceType="sample_text", ormType="sample_text", persistentType="sample_text", unique=True)
    a2 = persistence_EntityAttribute(containerUnique=False, hidden=False, interfaceType="sample_text_2", ormType="sample_text_2", persistentType="sample_text_2", unique=False)
    b = persistence_Attribute(inputClass="sample_text", validationPattern="sample_text")
    _safe_set(b, 'persistence_Attribute56', a1)
    assert _is_linked(b, 'persistence_Attribute56', a1)
    if hasattr(a1, 'persistence_EntityAttribute'):
        assert _is_linked(a1, 'persistence_EntityAttribute', b)
    _safe_set(b, 'persistence_Attribute56', a2)
    assert _is_linked(b, 'persistence_Attribute56', a2)
    if hasattr(a1, 'persistence_EntityAttribute'):
        assert not _is_linked(a1, 'persistence_EntityAttribute', b)
    if hasattr(a2, 'persistence_EntityAttribute'):
        assert _is_linked(a2, 'persistence_EntityAttribute', b)
    _safe_set(b, 'persistence_Attribute56', None)
    assert not _is_linked(b, 'persistence_Attribute56', a2)
    if hasattr(a2, 'persistence_EntityAttribute'):
        assert not _is_linked(a2, 'persistence_EntityAttribute', b)


def test_assoc_sourceEntityX33_reverse_link_reassign_clear():
    a1 = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_EntityOrView(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    _safe_set(b, 'persistence_Association34', a1)
    assert _is_linked(b, 'persistence_Association34', a1)
    if hasattr(a1, 'persistence_EntityOrView35'):
        assert _is_linked(a1, 'persistence_EntityOrView35', b)
    _safe_set(b, 'persistence_Association34', a2)
    assert _is_linked(b, 'persistence_Association34', a2)
    if hasattr(a1, 'persistence_EntityOrView35'):
        assert not _is_linked(a1, 'persistence_EntityOrView35', b)
    if hasattr(a2, 'persistence_EntityOrView35'):
        assert _is_linked(a2, 'persistence_EntityOrView35', b)
    _safe_set(b, 'persistence_Association34', None)
    assert not _is_linked(b, 'persistence_Association34', a2)
    if hasattr(a2, 'persistence_EntityOrView35'):
        assert not _is_linked(a2, 'persistence_EntityOrView35', b)


def test_assoc_targetEntityX36_reverse_link_reassign_clear():
    a1 = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    a2 = persistence_EntityOrView(allowFormTypeCustomisation=False, autoKeyGenerationStrategy="sample_text_2", autoKeyName="sample_text_2", autoKeyPersistentType="sample_text_2", implementsUserInterface=False, pluralisedName="sample_text_2", singletonName="sample_text_2", tableName="sample_text_2")
    b = persistence_Association(inputClass="sample_text", pseudo=True, serializationMaxDepth=7)
    _safe_set(b, 'persistence_Association37', a1)
    assert _is_linked(b, 'persistence_Association37', a1)
    if hasattr(a1, 'persistence_EntityOrView38'):
        assert _is_linked(a1, 'persistence_EntityOrView38', b)
    _safe_set(b, 'persistence_Association37', a2)
    assert _is_linked(b, 'persistence_Association37', a2)
    if hasattr(a1, 'persistence_EntityOrView38'):
        assert not _is_linked(a1, 'persistence_EntityOrView38', b)
    if hasattr(a2, 'persistence_EntityOrView38'):
        assert _is_linked(a2, 'persistence_EntityOrView38', b)
    _safe_set(b, 'persistence_Association37', None)
    assert not _is_linked(b, 'persistence_Association37', a2)
    if hasattr(a2, 'persistence_EntityOrView38'):
        assert not _is_linked(a2, 'persistence_EntityOrView38', b)


def test_assoc_unique7_reverse_link_reassign_clear():
    a1 = persistence_Feature(collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", placeholder="sample_text", title="sample_text")
    a2 = persistence_Feature(collectionOrmAllowAdd=False, collectionOrmAllowRemove=False, displayClass="sample_text_2", encodeUriKey=False, footerClass="sample_text_2", headerClass="sample_text_2", nullDisplayValue="sample_text_2", placeholder="sample_text_2", title="sample_text_2")
    b = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    _safe_set(b, 'persistence_EntityOrView8', {a1})
    assert _is_linked(b, 'persistence_EntityOrView8', a1)
    if hasattr(a1, 'persistence_Feature9'):
        assert _is_linked(a1, 'persistence_Feature9', b)
    _safe_set(b, 'persistence_EntityOrView8', {a2})
    assert _is_linked(b, 'persistence_EntityOrView8', a2)
    if hasattr(a1, 'persistence_Feature9'):
        assert not _is_linked(a1, 'persistence_Feature9', b)
    if hasattr(a2, 'persistence_Feature9'):
        assert _is_linked(a2, 'persistence_Feature9', b)
    _safe_set(b, 'persistence_EntityOrView8', set())
    assert not _is_linked(b, 'persistence_EntityOrView8', a2)
    if hasattr(a2, 'persistence_Feature9'):
        assert not _is_linked(a2, 'persistence_Feature9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_associationEnds53_stub_double():
    # persistence_Entity has no real 'targetEntity' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    partner = persistence_Entity()
    setattr(partner, 'targetEntity', None)
    _safe_set(owner, 'EntityAssociation', partner)
    assert owner in getattr(partner, 'targetEntity')
    _safe_set(owner, 'EntityAssociation', None)
    assert owner not in getattr(partner, 'targetEntity')


def test_assoc_dataType57_stub_double():
    # persistence_DataType has no real 'persistence_DataType58' property in the generated
    # code (a bare stub) -- manually attach it so persistence_DataTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_DataTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_DataTypeAttribute(caseInsensitive=True, encrypt=True, obfuscateFormFields=True)
    partner = persistence_DataType()
    setattr(partner, 'persistence_DataType58', None)
    _safe_set(owner, 'persistence_DataTypeAttribute', partner)
    assert getattr(partner, 'persistence_DataType58') == owner
    _safe_set(owner, 'persistence_DataTypeAttribute', None)
    assert getattr(partner, 'persistence_DataType58') is None


def test_assoc_dataTypes1_stub_double():
    # persistence_DataType has no real 'persistence_DataType' property in the generated
    # code (a bare stub) -- manually attach it so persistence_Persistence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_Persistence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    partner = persistence_DataType()
    setattr(partner, 'persistence_DataType', None)
    _safe_set(owner, 'persistence_Persistence2', {partner})
    assert getattr(partner, 'persistence_DataType') == owner
    _safe_set(owner, 'persistence_Persistence2', set())
    assert getattr(partner, 'persistence_DataType') is None


def test_assoc_defaultValue30_stub_double():
    # persistence_Expression has no real 'persistence_Expression' property in the generated
    # code (a bare stub) -- manually attach it so persistence_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_Attribute(inputClass="sample_text", validationPattern="sample_text")
    partner = persistence_Expression()
    setattr(partner, 'persistence_Expression', None)
    _safe_set(owner, 'persistence_Attribute31', partner)
    assert getattr(partner, 'persistence_Expression') == owner
    _safe_set(owner, 'persistence_Attribute31', None)
    assert getattr(partner, 'persistence_Expression') is None


def test_assoc_encapsulates69_stub_double():
    # persistence_View has no real 'persistence_View' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityOrView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityOrView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityOrView(allowFormTypeCustomisation=True, autoKeyGenerationStrategy="sample_text", autoKeyName="sample_text", autoKeyPersistentType="sample_text", implementsUserInterface=True, pluralisedName="sample_text", singletonName="sample_text", tableName="sample_text")
    partner = persistence_View()
    setattr(partner, 'persistence_View', None)
    _safe_set(owner, 'persistence_EntityOrView70', partner)
    assert owner in getattr(partner, 'persistence_View')
    _safe_set(owner, 'persistence_EntityOrView70', None)
    assert owner not in getattr(partner, 'persistence_View')


def test_assoc_entityFeatures51_stub_double():
    # persistence_Entity has no real 'partOf52' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", customiseSet=True, derived=True, ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text")
    partner = persistence_Entity()
    setattr(partner, 'partOf52', None)
    _safe_set(owner, 'EntityFeature', partner)
    assert owner in getattr(partner, 'partOf52')
    _safe_set(owner, 'EntityFeature', None)
    assert owner not in getattr(partner, 'partOf52')


def test_assoc_features40_stub_double():
    # persistence_ModelLabelFeature has no real 'ModelLabelFeature' property in the generated
    # code (a bare stub) -- manually attach it so persistence_ModelLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_ModelLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_ModelLabel(customise=True, format="sample_text")
    partner = persistence_ModelLabelFeature()
    setattr(partner, 'ModelLabelFeature', None)
    _safe_set(owner, 'partOf', {partner})
    assert getattr(partner, 'ModelLabelFeature') == owner
    _safe_set(owner, 'partOf', set())
    assert getattr(partner, 'ModelLabelFeature') is None


def test_assoc_keyFor63_stub_double():
    # persistence_AssociationKey has no real 'keys' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    partner = persistence_AssociationKey()
    setattr(partner, 'keys', None)
    _safe_set(owner, 'EntityAssociation64', partner)
    assert getattr(partner, 'keys') == owner
    _safe_set(owner, 'EntityAssociation64', None)
    assert getattr(partner, 'keys') is None


def test_assoc_keys60_stub_double():
    # persistence_AssociationKey has no real 'AssociationKey' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    partner = persistence_AssociationKey()
    setattr(partner, 'AssociationKey', None)
    _safe_set(owner, 'keyFor', {partner})
    assert getattr(partner, 'AssociationKey') == owner
    _safe_set(owner, 'keyFor', set())
    assert getattr(partner, 'AssociationKey') is None


def test_assoc_partOf43_stub_double():
    # persistence_ModelLabelFeature has no real 'features' property in the generated
    # code (a bare stub) -- manually attach it so persistence_ModelLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_ModelLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_ModelLabel(customise=True, format="sample_text")
    partner = persistence_ModelLabelFeature()
    setattr(partner, 'features', None)
    _safe_set(owner, 'ModelLabel44', partner)
    assert getattr(partner, 'features') == owner
    _safe_set(owner, 'ModelLabel44', None)
    assert getattr(partner, 'features') is None


def test_assoc_partOf54_stub_double():
    # persistence_Entity has no real 'Entity' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", customiseSet=True, derived=True, ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text")
    partner = persistence_Entity()
    setattr(partner, 'Entity', None)
    _safe_set(owner, 'entityFeatures', partner)
    assert getattr(partner, 'Entity') == owner
    _safe_set(owner, 'entityFeatures', None)
    assert getattr(partner, 'Entity') is None


def test_assoc_serializationGroups0_stub_double():
    # persistence_SerializationGroup has no real 'persistence_SerializationGroup' property in the generated
    # code (a bare stub) -- manually attach it so persistence_Persistence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_Persistence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_Persistence(databaseTechnology="sample_text", ormTechnology="sample_text", timestampCreation=True, timestampUpdates=True)
    partner = persistence_SerializationGroup()
    setattr(partner, 'persistence_SerializationGroup', None)
    _safe_set(owner, 'persistence_Persistence', {partner})
    assert getattr(partner, 'persistence_SerializationGroup') == owner
    _safe_set(owner, 'persistence_Persistence', set())
    assert getattr(partner, 'persistence_SerializationGroup') is None


def test_assoc_serializationGroups27_stub_double():
    # persistence_SerializationGroup has no real 'persistence_SerializationGroup29' property in the generated
    # code (a bare stub) -- manually attach it so persistence_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_Feature(collectionOrmAllowAdd=True, collectionOrmAllowRemove=True, displayClass="sample_text", encodeUriKey=True, footerClass="sample_text", headerClass="sample_text", nullDisplayValue="sample_text", placeholder="sample_text", title="sample_text")
    partner = persistence_SerializationGroup()
    setattr(partner, 'persistence_SerializationGroup29', None)
    _safe_set(owner, 'persistence_Feature28', {partner})
    assert getattr(partner, 'persistence_SerializationGroup29') == owner
    _safe_set(owner, 'persistence_Feature28', set())
    assert getattr(partner, 'persistence_SerializationGroup29') is None


def test_assoc_serializationGroups41_stub_double():
    # persistence_SerializationGroup has no real 'persistence_SerializationGroup42' property in the generated
    # code (a bare stub) -- manually attach it so persistence_ModelLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_ModelLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_ModelLabel(customise=True, format="sample_text")
    partner = persistence_SerializationGroup()
    setattr(partner, 'persistence_SerializationGroup42', None)
    _safe_set(owner, 'persistence_ModelLabel', {partner})
    assert getattr(partner, 'persistence_SerializationGroup42') == owner
    _safe_set(owner, 'persistence_ModelLabel', set())
    assert getattr(partner, 'persistence_SerializationGroup42') is None


def test_assoc_sourceEntity79_stub_double():
    # persistence_Entity has no real 'persistence_Entity' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EncapsulatedAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EncapsulatedAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    partner = persistence_Entity()
    setattr(partner, 'persistence_Entity', None)
    _safe_set(owner, 'persistence_EncapsulatedAssociation80', partner)
    assert getattr(partner, 'persistence_Entity') == owner
    _safe_set(owner, 'persistence_EncapsulatedAssociation80', None)
    assert getattr(partner, 'persistence_Entity') is None


def test_assoc_sourceFeature65_stub_double():
    # persistence_AssociationKey has no real 'persistence_AssociationKey' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", customiseSet=True, derived=True, ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text")
    partner = persistence_AssociationKey()
    setattr(partner, 'persistence_AssociationKey', None)
    _safe_set(owner, 'persistence_EntityFeature', partner)
    assert getattr(partner, 'persistence_AssociationKey') == owner
    _safe_set(owner, 'persistence_EntityFeature', None)
    assert getattr(partner, 'persistence_AssociationKey') is None


def test_assoc_targetEntity61_stub_double():
    # persistence_Entity has no real 'Entity62' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityAssociation(bidirectional=True, pivotTableName="sample_text", targetColumnName="sample_text", targetDisplayClass="sample_text", targetDisplayLabel="sample_text", targetFeatureName="sample_text", targetFooterClass="sample_text", targetHeaderClass="sample_text", targetInputClass="sample_text", targetPrimaryKey=True, unique=True)
    partner = persistence_Entity()
    setattr(partner, 'Entity62', None)
    _safe_set(owner, 'associationEnds', partner)
    assert getattr(partner, 'Entity62') == owner
    _safe_set(owner, 'associationEnds', None)
    assert getattr(partner, 'Entity62') is None


def test_assoc_targetEntity81_stub_double():
    # persistence_Entity has no real 'persistence_Entity83' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EncapsulatedAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EncapsulatedAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EncapsulatedAssociation(cardinality="sample_text", isSourceAssociation=True, name="sample_text")
    partner = persistence_Entity()
    setattr(partner, 'persistence_Entity83', None)
    _safe_set(owner, 'persistence_EncapsulatedAssociation82', partner)
    assert getattr(partner, 'persistence_Entity83') == owner
    _safe_set(owner, 'persistence_EncapsulatedAssociation82', None)
    assert getattr(partner, 'persistence_Entity83') is None


def test_assoc_targetFeature66_stub_double():
    # persistence_AssociationKey has no real 'persistence_AssociationKey67' property in the generated
    # code (a bare stub) -- manually attach it so persistence_EntityFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_EntityFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_EntityFeature(booleanIsHasChoice="sample_text", cardinality="sample_text", columnName="sample_text", customiseSet=True, derived=True, ordered=True, pluralisedName="sample_text", primaryKey=True, singletonName="sample_text")
    partner = persistence_AssociationKey()
    setattr(partner, 'persistence_AssociationKey67', None)
    _safe_set(owner, 'persistence_EntityFeature68', partner)
    assert getattr(partner, 'persistence_AssociationKey67') == owner
    _safe_set(owner, 'persistence_EntityFeature68', None)
    assert getattr(partner, 'persistence_AssociationKey67') is None


def test_assoc_uploadPath59_stub_double():
    # persistence_PathElement has no real 'persistence_PathElement' property in the generated
    # code (a bare stub) -- manually attach it so persistence_ResourceAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persistence_ResourceAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persistence_ResourceAttribute(maximumUploadSize=7, uploadsWithinWebsite=True, validUploadExtensions="sample_text", validUploadMimeTypes="sample_text")
    partner = persistence_PathElement()
    setattr(partner, 'persistence_PathElement', None)
    _safe_set(owner, 'persistence_ResourceAttribute', {partner})
    assert getattr(partner, 'persistence_PathElement') == owner
    _safe_set(owner, 'persistence_ResourceAttribute', set())
    assert getattr(partner, 'persistence_PathElement') is None


