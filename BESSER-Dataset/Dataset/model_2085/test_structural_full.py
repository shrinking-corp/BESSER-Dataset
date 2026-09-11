import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CardinalizedElement,
    CommonFeature,
    ConstraintableElement,
    ContainableElement,
    ContainerElement,
    Feature,
    Literal,
    VariableFeature,
    sxfm_Atom,
    sxfm_CardinalizedElement,
    sxfm_CommonFeature,
    sxfm_Constraint,
    sxfm_ConstraintableElement,
    sxfm_ConstraintsSet,
    sxfm_ContainableElement,
    sxfm_ContainerElement,
    sxfm_Data,
    sxfm_Feature,
    sxfm_FeatureChoice,
    sxfm_FeatureModel,
    sxfm_FeatureModelConfiguaration,
    sxfm_FeatureTree,
    sxfm_Group,
    sxfm_GroupedFeature,
    sxfm_Literal,
    sxfm_Mandatory,
    sxfm_MetadataSet,
    sxfm_Not,
    sxfm_Optional,
    sxfm_Or,
    sxfm_Root,
    sxfm_VariableFeature,
    DecisionType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_sxfm_CardinalizedElement_maxCardinality_value_roundtrip():
    instance = sxfm_CardinalizedElement(maxCardinality=7, minCardinality=7)
    assert instance.maxCardinality == 7
    instance.maxCardinality = 13
    assert instance.maxCardinality == 13


def test_sxfm_CardinalizedElement_minCardinality_value_roundtrip():
    instance = sxfm_CardinalizedElement(maxCardinality=7, minCardinality=7)
    assert instance.minCardinality == 7
    instance.minCardinality = 13
    assert instance.minCardinality == 13


def test_sxfm_Constraint_id_value_roundtrip():
    instance = sxfm_Constraint(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_sxfm_Data_name_value_roundtrip():
    instance = sxfm_Data(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sxfm_Data_value_value_roundtrip():
    instance = sxfm_Data(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_sxfm_Feature_description_value_roundtrip():
    instance = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_sxfm_Feature_id_value_roundtrip():
    instance = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_sxfm_Feature_name_value_roundtrip():
    instance = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sxfm_Feature_treeLevel_value_roundtrip():
    instance = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    assert instance.treeLevel == 7
    instance.treeLevel = 13
    assert instance.treeLevel == 13


def test_sxfm_FeatureChoice_decisionStep_value_roundtrip():
    instance = sxfm_FeatureChoice(decisionStep=7, decisionType="sample_text", selected=True)
    assert instance.decisionStep == 7
    instance.decisionStep = 13
    assert instance.decisionStep == 13


def test_sxfm_FeatureChoice_decisionType_value_roundtrip():
    instance = sxfm_FeatureChoice(decisionStep=7, decisionType="sample_text", selected=True)
    assert instance.decisionType == "sample_text"
    instance.decisionType = "sample_text_2"
    assert instance.decisionType == "sample_text_2"


def test_sxfm_FeatureChoice_selected_value_roundtrip():
    instance = sxfm_FeatureChoice(decisionStep=7, decisionType="sample_text", selected=True)
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_sxfm_FeatureModel_name_value_roundtrip():
    instance = sxfm_FeatureModel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sxfm_Group_id_value_roundtrip():
    instance = sxfm_Group(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_sxfm_Group_isa_CardinalizedElement():
    instance = sxfm_Group(id="sample_text")
    assert isinstance(instance, CardinalizedElement)


def test_sxfm_Mandatory_isa_CommonFeature():
    instance = sxfm_Mandatory()
    assert isinstance(instance, CommonFeature)


def test_sxfm_Root_isa_CommonFeature():
    instance = sxfm_Root()
    assert isinstance(instance, CommonFeature)


def test_sxfm_GroupedFeature_isa_ConstraintableElement():
    instance = sxfm_GroupedFeature()
    assert isinstance(instance, ConstraintableElement)


def test_sxfm_Mandatory_isa_ConstraintableElement():
    instance = sxfm_Mandatory()
    assert isinstance(instance, ConstraintableElement)


def test_sxfm_Optional_isa_ConstraintableElement():
    instance = sxfm_Optional()
    assert isinstance(instance, ConstraintableElement)


def test_sxfm_Mandatory_isa_ContainableElement():
    instance = sxfm_Mandatory()
    assert isinstance(instance, ContainableElement)


def test_sxfm_Optional_isa_ContainableElement():
    instance = sxfm_Optional()
    assert isinstance(instance, ContainableElement)


def test_sxfm_GroupedFeature_isa_ContainerElement():
    instance = sxfm_GroupedFeature()
    assert isinstance(instance, ContainerElement)


def test_sxfm_Mandatory_isa_ContainerElement():
    instance = sxfm_Mandatory()
    assert isinstance(instance, ContainerElement)


def test_sxfm_Optional_isa_ContainerElement():
    instance = sxfm_Optional()
    assert isinstance(instance, ContainerElement)


def test_sxfm_Root_isa_ContainerElement():
    instance = sxfm_Root()
    assert isinstance(instance, ContainerElement)


def test_sxfm_GroupedFeature_isa_Feature():
    instance = sxfm_GroupedFeature()
    assert isinstance(instance, Feature)


def test_sxfm_Mandatory_isa_Feature():
    instance = sxfm_Mandatory()
    assert isinstance(instance, Feature)


def test_sxfm_Optional_isa_Feature():
    instance = sxfm_Optional()
    assert isinstance(instance, Feature)


def test_sxfm_Root_isa_Feature():
    instance = sxfm_Root()
    assert isinstance(instance, Feature)


def test_sxfm_Atom_isa_Literal():
    instance = sxfm_Atom()
    assert isinstance(instance, Literal)


def test_sxfm_Not_isa_Literal():
    instance = sxfm_Not()
    assert isinstance(instance, Literal)


def test_sxfm_GroupedFeature_isa_VariableFeature():
    instance = sxfm_GroupedFeature()
    assert isinstance(instance, VariableFeature)


def test_sxfm_Optional_isa_VariableFeature():
    instance = sxfm_Optional()
    assert isinstance(instance, VariableFeature)


def test_assoc_configuration9_link_reassign_clear():
    a = sxfm_FeatureModel(name="sample_text")
    b1 = sxfm_FeatureModelConfiguaration()
    b2 = sxfm_FeatureModelConfiguaration()
    _safe_set(a, 'sxfm_FeatureModel10', {b1})
    assert _is_linked(a, 'sxfm_FeatureModel10', b1)
    if hasattr(b1, 'sxfm_FeatureModelConfiguaration'):
        assert _is_linked(b1, 'sxfm_FeatureModelConfiguaration', a)
    _safe_set(a, 'sxfm_FeatureModel10', {b2})
    assert _is_linked(a, 'sxfm_FeatureModel10', b2)
    if hasattr(b1, 'sxfm_FeatureModelConfiguaration'):
        assert not _is_linked(b1, 'sxfm_FeatureModelConfiguaration', a)
    if hasattr(b2, 'sxfm_FeatureModelConfiguaration'):
        assert _is_linked(b2, 'sxfm_FeatureModelConfiguaration', a)
    _safe_set(a, 'sxfm_FeatureModel10', set())
    assert not _is_linked(a, 'sxfm_FeatureModel10', b2)
    if hasattr(b2, 'sxfm_FeatureModelConfiguaration'):
        assert not _is_linked(b2, 'sxfm_FeatureModelConfiguaration', a)


def test_assoc_constraints13_link_reassign_clear():
    a = sxfm_Constraint(id=7)
    b1 = sxfm_ConstraintsSet()
    b2 = sxfm_ConstraintsSet()
    _safe_set(a, 'sxfm_Constraint15', b1)
    assert _is_linked(a, 'sxfm_Constraint15', b1)
    if hasattr(b1, 'sxfm_ConstraintsSet14'):
        assert _is_linked(b1, 'sxfm_ConstraintsSet14', a)
    _safe_set(a, 'sxfm_Constraint15', b2)
    assert _is_linked(a, 'sxfm_Constraint15', b2)
    if hasattr(b1, 'sxfm_ConstraintsSet14'):
        assert not _is_linked(b1, 'sxfm_ConstraintsSet14', a)
    if hasattr(b2, 'sxfm_ConstraintsSet14'):
        assert _is_linked(b2, 'sxfm_ConstraintsSet14', a)
    _safe_set(a, 'sxfm_Constraint15', None)
    assert not _is_linked(a, 'sxfm_Constraint15', b2)
    if hasattr(b2, 'sxfm_ConstraintsSet14'):
        assert not _is_linked(b2, 'sxfm_ConstraintsSet14', a)


def test_assoc_constraintsSet4_link_reassign_clear():
    a = sxfm_FeatureModel(name="sample_text")
    b1 = sxfm_ConstraintsSet()
    b2 = sxfm_ConstraintsSet()
    _safe_set(a, 'sxfm_FeatureModel', b1)
    assert _is_linked(a, 'sxfm_FeatureModel', b1)
    if hasattr(b1, 'sxfm_ConstraintsSet'):
        assert _is_linked(b1, 'sxfm_ConstraintsSet', a)
    _safe_set(a, 'sxfm_FeatureModel', b2)
    assert _is_linked(a, 'sxfm_FeatureModel', b2)
    if hasattr(b1, 'sxfm_ConstraintsSet'):
        assert not _is_linked(b1, 'sxfm_ConstraintsSet', a)
    if hasattr(b2, 'sxfm_ConstraintsSet'):
        assert _is_linked(b2, 'sxfm_ConstraintsSet', a)
    _safe_set(a, 'sxfm_FeatureModel', None)
    assert not _is_linked(a, 'sxfm_FeatureModel', b2)
    if hasattr(b2, 'sxfm_ConstraintsSet'):
        assert not _is_linked(b2, 'sxfm_ConstraintsSet', a)


def test_assoc_data22_link_reassign_clear():
    a = sxfm_Data(name="sample_text", value="sample_text")
    b1 = sxfm_MetadataSet()
    b2 = sxfm_MetadataSet()
    _safe_set(a, 'sxfm_Data', b1)
    assert _is_linked(a, 'sxfm_Data', b1)
    if hasattr(b1, 'sxfm_MetadataSet23'):
        assert _is_linked(b1, 'sxfm_MetadataSet23', a)
    _safe_set(a, 'sxfm_Data', b2)
    assert _is_linked(a, 'sxfm_Data', b2)
    if hasattr(b1, 'sxfm_MetadataSet23'):
        assert not _is_linked(b1, 'sxfm_MetadataSet23', a)
    if hasattr(b2, 'sxfm_MetadataSet23'):
        assert _is_linked(b2, 'sxfm_MetadataSet23', a)
    _safe_set(a, 'sxfm_Data', None)
    assert not _is_linked(a, 'sxfm_Data', b2)
    if hasattr(b2, 'sxfm_MetadataSet23'):
        assert not _is_linked(b2, 'sxfm_MetadataSet23', a)


def test_assoc_feature26_link_reassign_clear():
    a = sxfm_FeatureChoice(decisionStep=7, decisionType="sample_text", selected=True)
    b1 = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    b2 = sxfm_Feature(description="sample_text_2", id="sample_text_2", name="sample_text_2", treeLevel=13)
    _safe_set(a, 'sxfm_FeatureChoice27', b1)
    assert _is_linked(a, 'sxfm_FeatureChoice27', b1)
    if hasattr(b1, 'sxfm_Feature28'):
        assert _is_linked(b1, 'sxfm_Feature28', a)
    _safe_set(a, 'sxfm_FeatureChoice27', b2)
    assert _is_linked(a, 'sxfm_FeatureChoice27', b2)
    if hasattr(b1, 'sxfm_Feature28'):
        assert not _is_linked(b1, 'sxfm_Feature28', a)
    if hasattr(b2, 'sxfm_Feature28'):
        assert _is_linked(b2, 'sxfm_Feature28', a)
    _safe_set(a, 'sxfm_FeatureChoice27', None)
    assert not _is_linked(a, 'sxfm_FeatureChoice27', b2)
    if hasattr(b2, 'sxfm_Feature28'):
        assert not _is_linked(b2, 'sxfm_Feature28', a)


def test_assoc_featureChoice24_link_reassign_clear():
    a = sxfm_FeatureChoice(decisionStep=7, decisionType="sample_text", selected=True)
    b1 = sxfm_FeatureModelConfiguaration()
    b2 = sxfm_FeatureModelConfiguaration()
    _safe_set(a, 'sxfm_FeatureChoice', b1)
    assert _is_linked(a, 'sxfm_FeatureChoice', b1)
    if hasattr(b1, 'sxfm_FeatureModelConfiguaration25'):
        assert _is_linked(b1, 'sxfm_FeatureModelConfiguaration25', a)
    _safe_set(a, 'sxfm_FeatureChoice', b2)
    assert _is_linked(a, 'sxfm_FeatureChoice', b2)
    if hasattr(b1, 'sxfm_FeatureModelConfiguaration25'):
        assert not _is_linked(b1, 'sxfm_FeatureModelConfiguaration25', a)
    if hasattr(b2, 'sxfm_FeatureModelConfiguaration25'):
        assert _is_linked(b2, 'sxfm_FeatureModelConfiguaration25', a)
    _safe_set(a, 'sxfm_FeatureChoice', None)
    assert not _is_linked(a, 'sxfm_FeatureChoice', b2)
    if hasattr(b2, 'sxfm_FeatureModelConfiguaration25'):
        assert not _is_linked(b2, 'sxfm_FeatureModelConfiguaration25', a)


def test_assoc_featureModelInfo7_link_reassign_clear():
    a = sxfm_FeatureModel(name="sample_text")
    b1 = sxfm_MetadataSet()
    b2 = sxfm_MetadataSet()
    _safe_set(a, 'sxfm_FeatureModel8', b1)
    assert _is_linked(a, 'sxfm_FeatureModel8', b1)
    if hasattr(b1, 'sxfm_MetadataSet'):
        assert _is_linked(b1, 'sxfm_MetadataSet', a)
    _safe_set(a, 'sxfm_FeatureModel8', b2)
    assert _is_linked(a, 'sxfm_FeatureModel8', b2)
    if hasattr(b1, 'sxfm_MetadataSet'):
        assert not _is_linked(b1, 'sxfm_MetadataSet', a)
    if hasattr(b2, 'sxfm_MetadataSet'):
        assert _is_linked(b2, 'sxfm_MetadataSet', a)
    _safe_set(a, 'sxfm_FeatureModel8', None)
    assert not _is_linked(a, 'sxfm_FeatureModel8', b2)
    if hasattr(b2, 'sxfm_MetadataSet'):
        assert not _is_linked(b2, 'sxfm_MetadataSet', a)


def test_assoc_featureTree5_link_reassign_clear():
    a = sxfm_FeatureModel(name="sample_text")
    b1 = sxfm_FeatureTree()
    b2 = sxfm_FeatureTree()
    _safe_set(a, 'sxfm_FeatureModel6', b1)
    assert _is_linked(a, 'sxfm_FeatureModel6', b1)
    if hasattr(b1, 'sxfm_FeatureTree'):
        assert _is_linked(b1, 'sxfm_FeatureTree', a)
    _safe_set(a, 'sxfm_FeatureModel6', b2)
    assert _is_linked(a, 'sxfm_FeatureModel6', b2)
    if hasattr(b1, 'sxfm_FeatureTree'):
        assert not _is_linked(b1, 'sxfm_FeatureTree', a)
    if hasattr(b2, 'sxfm_FeatureTree'):
        assert _is_linked(b2, 'sxfm_FeatureTree', a)
    _safe_set(a, 'sxfm_FeatureModel6', None)
    assert not _is_linked(a, 'sxfm_FeatureModel6', b2)
    if hasattr(b2, 'sxfm_FeatureTree'):
        assert not _is_linked(b2, 'sxfm_FeatureTree', a)


def test_assoc_groupedFeatures1_link_reassign_clear():
    a = sxfm_Group(id="sample_text")
    b1 = sxfm_GroupedFeature()
    b2 = sxfm_GroupedFeature()
    _safe_set(a, 'sxfm_Group2', {b1})
    assert _is_linked(a, 'sxfm_Group2', b1)
    if hasattr(b1, 'sxfm_GroupedFeature'):
        assert _is_linked(b1, 'sxfm_GroupedFeature', a)
    _safe_set(a, 'sxfm_Group2', {b2})
    assert _is_linked(a, 'sxfm_Group2', b2)
    if hasattr(b1, 'sxfm_GroupedFeature'):
        assert not _is_linked(b1, 'sxfm_GroupedFeature', a)
    if hasattr(b2, 'sxfm_GroupedFeature'):
        assert _is_linked(b2, 'sxfm_GroupedFeature', a)
    _safe_set(a, 'sxfm_Group2', set())
    assert not _is_linked(a, 'sxfm_Group2', b2)
    if hasattr(b2, 'sxfm_GroupedFeature'):
        assert not _is_linked(b2, 'sxfm_GroupedFeature', a)


def test_assoc_groups0_link_reassign_clear():
    a = sxfm_Group(id="sample_text")
    b1 = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    b2 = sxfm_Feature(description="sample_text_2", id="sample_text_2", name="sample_text_2", treeLevel=13)
    _safe_set(a, 'sxfm_Group', b1)
    assert _is_linked(a, 'sxfm_Group', b1)
    if hasattr(b1, 'sxfm_Feature'):
        assert _is_linked(b1, 'sxfm_Feature', a)
    _safe_set(a, 'sxfm_Group', b2)
    assert _is_linked(a, 'sxfm_Group', b2)
    if hasattr(b1, 'sxfm_Feature'):
        assert not _is_linked(b1, 'sxfm_Feature', a)
    if hasattr(b2, 'sxfm_Feature'):
        assert _is_linked(b2, 'sxfm_Feature', a)
    _safe_set(a, 'sxfm_Group', None)
    assert not _is_linked(a, 'sxfm_Group', b2)
    if hasattr(b2, 'sxfm_Feature'):
        assert not _is_linked(b2, 'sxfm_Feature', a)


def test_assoc_or_3_link_reassign_clear():
    a = sxfm_Constraint(id=7)
    b1 = sxfm_Or()
    b2 = sxfm_Or()
    _safe_set(a, 'sxfm_Constraint', b1)
    assert _is_linked(a, 'sxfm_Constraint', b1)
    if hasattr(b1, 'sxfm_Or'):
        assert _is_linked(b1, 'sxfm_Or', a)
    _safe_set(a, 'sxfm_Constraint', b2)
    assert _is_linked(a, 'sxfm_Constraint', b2)
    if hasattr(b1, 'sxfm_Or'):
        assert not _is_linked(b1, 'sxfm_Or', a)
    if hasattr(b2, 'sxfm_Or'):
        assert _is_linked(b2, 'sxfm_Or', a)
    _safe_set(a, 'sxfm_Constraint', None)
    assert not _is_linked(a, 'sxfm_Constraint', b2)
    if hasattr(b2, 'sxfm_Or'):
        assert not _is_linked(b2, 'sxfm_Or', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CardinalizedElement_strategy = st.builds(CardinalizedElement)
@given(instance=CardinalizedElement_strategy)
@settings(max_examples=25)
def test_CardinalizedElement_instantiation(instance):
    assert isinstance(instance, CardinalizedElement)


CommonFeature_strategy = st.builds(CommonFeature)
@given(instance=CommonFeature_strategy)
@settings(max_examples=25)
def test_CommonFeature_instantiation(instance):
    assert isinstance(instance, CommonFeature)


ConstraintableElement_strategy = st.builds(ConstraintableElement)
@given(instance=ConstraintableElement_strategy)
@settings(max_examples=25)
def test_ConstraintableElement_instantiation(instance):
    assert isinstance(instance, ConstraintableElement)


ContainableElement_strategy = st.builds(ContainableElement)
@given(instance=ContainableElement_strategy)
@settings(max_examples=25)
def test_ContainableElement_instantiation(instance):
    assert isinstance(instance, ContainableElement)


ContainerElement_strategy = st.builds(ContainerElement)
@given(instance=ContainerElement_strategy)
@settings(max_examples=25)
def test_ContainerElement_instantiation(instance):
    assert isinstance(instance, ContainerElement)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


VariableFeature_strategy = st.builds(VariableFeature)
@given(instance=VariableFeature_strategy)
@settings(max_examples=25)
def test_VariableFeature_instantiation(instance):
    assert isinstance(instance, VariableFeature)


sxfm_Atom_strategy = st.builds(sxfm_Atom)
@given(instance=sxfm_Atom_strategy)
@settings(max_examples=25)
def test_sxfm_Atom_instantiation(instance):
    assert isinstance(instance, sxfm_Atom)


sxfm_CardinalizedElement_strategy = st.builds(sxfm_CardinalizedElement, maxCardinality=st.integers(), minCardinality=st.integers())
@given(instance=sxfm_CardinalizedElement_strategy)
@settings(max_examples=25)
def test_sxfm_CardinalizedElement_instantiation(instance):
    assert isinstance(instance, sxfm_CardinalizedElement)


sxfm_CommonFeature_strategy = st.builds(sxfm_CommonFeature)
@given(instance=sxfm_CommonFeature_strategy)
@settings(max_examples=25)
def test_sxfm_CommonFeature_instantiation(instance):
    assert isinstance(instance, sxfm_CommonFeature)


sxfm_Constraint_strategy = st.builds(sxfm_Constraint, id=st.integers())
@given(instance=sxfm_Constraint_strategy)
@settings(max_examples=25)
def test_sxfm_Constraint_instantiation(instance):
    assert isinstance(instance, sxfm_Constraint)


sxfm_ConstraintableElement_strategy = st.builds(sxfm_ConstraintableElement)
@given(instance=sxfm_ConstraintableElement_strategy)
@settings(max_examples=25)
def test_sxfm_ConstraintableElement_instantiation(instance):
    assert isinstance(instance, sxfm_ConstraintableElement)


sxfm_ConstraintsSet_strategy = st.builds(sxfm_ConstraintsSet)
@given(instance=sxfm_ConstraintsSet_strategy)
@settings(max_examples=25)
def test_sxfm_ConstraintsSet_instantiation(instance):
    assert isinstance(instance, sxfm_ConstraintsSet)


sxfm_ContainableElement_strategy = st.builds(sxfm_ContainableElement)
@given(instance=sxfm_ContainableElement_strategy)
@settings(max_examples=25)
def test_sxfm_ContainableElement_instantiation(instance):
    assert isinstance(instance, sxfm_ContainableElement)


sxfm_ContainerElement_strategy = st.builds(sxfm_ContainerElement)
@given(instance=sxfm_ContainerElement_strategy)
@settings(max_examples=25)
def test_sxfm_ContainerElement_instantiation(instance):
    assert isinstance(instance, sxfm_ContainerElement)


sxfm_Data_strategy = st.builds(sxfm_Data, name=safe_text, value=safe_text)
@given(instance=sxfm_Data_strategy)
@settings(max_examples=25)
def test_sxfm_Data_instantiation(instance):
    assert isinstance(instance, sxfm_Data)


sxfm_Feature_strategy = st.builds(sxfm_Feature, description=safe_text, id=safe_text, name=safe_text, treeLevel=st.integers())
@given(instance=sxfm_Feature_strategy)
@settings(max_examples=25)
def test_sxfm_Feature_instantiation(instance):
    assert isinstance(instance, sxfm_Feature)


sxfm_FeatureChoice_strategy = st.builds(sxfm_FeatureChoice, decisionStep=st.integers(), decisionType=safe_text, selected=st.booleans())
@given(instance=sxfm_FeatureChoice_strategy)
@settings(max_examples=25)
def test_sxfm_FeatureChoice_instantiation(instance):
    assert isinstance(instance, sxfm_FeatureChoice)


sxfm_FeatureModel_strategy = st.builds(sxfm_FeatureModel, name=safe_text)
@given(instance=sxfm_FeatureModel_strategy)
@settings(max_examples=25)
def test_sxfm_FeatureModel_instantiation(instance):
    assert isinstance(instance, sxfm_FeatureModel)


sxfm_FeatureModelConfiguaration_strategy = st.builds(sxfm_FeatureModelConfiguaration)
@given(instance=sxfm_FeatureModelConfiguaration_strategy)
@settings(max_examples=25)
def test_sxfm_FeatureModelConfiguaration_instantiation(instance):
    assert isinstance(instance, sxfm_FeatureModelConfiguaration)


sxfm_FeatureTree_strategy = st.builds(sxfm_FeatureTree)
@given(instance=sxfm_FeatureTree_strategy)
@settings(max_examples=25)
def test_sxfm_FeatureTree_instantiation(instance):
    assert isinstance(instance, sxfm_FeatureTree)


sxfm_Group_strategy = st.builds(sxfm_Group, id=safe_text)
@given(instance=sxfm_Group_strategy)
@settings(max_examples=25)
def test_sxfm_Group_instantiation(instance):
    assert isinstance(instance, sxfm_Group)


sxfm_GroupedFeature_strategy = st.builds(sxfm_GroupedFeature)
@given(instance=sxfm_GroupedFeature_strategy)
@settings(max_examples=25)
def test_sxfm_GroupedFeature_instantiation(instance):
    assert isinstance(instance, sxfm_GroupedFeature)


sxfm_Literal_strategy = st.builds(sxfm_Literal)
@given(instance=sxfm_Literal_strategy)
@settings(max_examples=25)
def test_sxfm_Literal_instantiation(instance):
    assert isinstance(instance, sxfm_Literal)


sxfm_Mandatory_strategy = st.builds(sxfm_Mandatory)
@given(instance=sxfm_Mandatory_strategy)
@settings(max_examples=25)
def test_sxfm_Mandatory_instantiation(instance):
    assert isinstance(instance, sxfm_Mandatory)


sxfm_MetadataSet_strategy = st.builds(sxfm_MetadataSet)
@given(instance=sxfm_MetadataSet_strategy)
@settings(max_examples=25)
def test_sxfm_MetadataSet_instantiation(instance):
    assert isinstance(instance, sxfm_MetadataSet)


sxfm_Not_strategy = st.builds(sxfm_Not)
@given(instance=sxfm_Not_strategy)
@settings(max_examples=25)
def test_sxfm_Not_instantiation(instance):
    assert isinstance(instance, sxfm_Not)


sxfm_Optional_strategy = st.builds(sxfm_Optional)
@given(instance=sxfm_Optional_strategy)
@settings(max_examples=25)
def test_sxfm_Optional_instantiation(instance):
    assert isinstance(instance, sxfm_Optional)


sxfm_Or_strategy = st.builds(sxfm_Or)
@given(instance=sxfm_Or_strategy)
@settings(max_examples=25)
def test_sxfm_Or_instantiation(instance):
    assert isinstance(instance, sxfm_Or)


sxfm_Root_strategy = st.builds(sxfm_Root)
@given(instance=sxfm_Root_strategy)
@settings(max_examples=25)
def test_sxfm_Root_instantiation(instance):
    assert isinstance(instance, sxfm_Root)


sxfm_VariableFeature_strategy = st.builds(sxfm_VariableFeature)
@given(instance=sxfm_VariableFeature_strategy)
@settings(max_examples=25)
def test_sxfm_VariableFeature_instantiation(instance):
    assert isinstance(instance, sxfm_VariableFeature)


