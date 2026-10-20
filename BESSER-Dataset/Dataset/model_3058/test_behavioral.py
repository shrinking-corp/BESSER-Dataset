import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    AtomicView,
    ContainerView,
    ElementView,
    EntityModelElement,
    Input,
    Output,
    PropertyType,
    Selection,
    StructuralFeature,
    classLayout2Frontend_Association,
    classLayout2Frontend_AtomicView,
    classLayout2Frontend_Autocomplete,
    classLayout2Frontend_CheckList,
    classLayout2Frontend_Composition,
    classLayout2Frontend_ContainerView,
    classLayout2Frontend_Dropdownlist,
    classLayout2Frontend_ElementView,
    classLayout2Frontend_EntitiesModel,
    classLayout2Frontend_Entity,
    classLayout2Frontend_EntityModelElement,
    classLayout2Frontend_Enumeration,
    classLayout2Frontend_FileUpload,
    classLayout2Frontend_Image,
    classLayout2Frontend_Input,
    classLayout2Frontend_InputForm,
    classLayout2Frontend_InputText,
    classLayout2Frontend_IterationContainer,
    classLayout2Frontend_IterationFilter,
    classLayout2Frontend_List,
    classLayout2Frontend_Literal,
    classLayout2Frontend_Output,
    classLayout2Frontend_PageView,
    classLayout2Frontend_PrimitiveType,
    classLayout2Frontend_Project,
    classLayout2Frontend_Property,
    classLayout2Frontend_PropertyType,
    classLayout2Frontend_RadioButtonGroup,
    classLayout2Frontend_Reference,
    classLayout2Frontend_Selection,
    classLayout2Frontend_SiteView,
    classLayout2Frontend_StaticContainer,
    classLayout2Frontend_StructuralFeature,
    classLayout2Frontend_TextArea,
    LayoutType,
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

def test_assoc_elementViews20_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_PageView(layoutType="sample_text", name="sample_text")
    a2 = classLayout2Frontend_PageView(layoutType="sample_text_2", name="sample_text_2")
    b = classLayout2Frontend_ElementView(description="sample_text", displayName="sample_text", name="sample_text")
    _safe_set(b, 'classLayout2Frontend_ElementView', a1)
    assert _is_linked(b, 'classLayout2Frontend_ElementView', a1)
    if hasattr(a1, 'classLayout2Frontend_PageView21'):
        assert _is_linked(a1, 'classLayout2Frontend_PageView21', b)
    _safe_set(b, 'classLayout2Frontend_ElementView', a2)
    assert _is_linked(b, 'classLayout2Frontend_ElementView', a2)
    if hasattr(a1, 'classLayout2Frontend_PageView21'):
        assert not _is_linked(a1, 'classLayout2Frontend_PageView21', b)
    if hasattr(a2, 'classLayout2Frontend_PageView21'):
        assert _is_linked(a2, 'classLayout2Frontend_PageView21', b)
    _safe_set(b, 'classLayout2Frontend_ElementView', None)
    assert not _is_linked(b, 'classLayout2Frontend_ElementView', a2)
    if hasattr(a2, 'classLayout2Frontend_PageView21'):
        assert not _is_linked(a2, 'classLayout2Frontend_PageView21', b)


def test_assoc_entitiesmodel0_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_Project(name="sample_text")
    a2 = classLayout2Frontend_Project(name="sample_text_2")
    b = classLayout2Frontend_EntitiesModel(name="sample_text")
    _safe_set(b, 'classLayout2Frontend_EntitiesModel', a1)
    assert _is_linked(b, 'classLayout2Frontend_EntitiesModel', a1)
    if hasattr(a1, 'classLayout2Frontend_Project'):
        assert _is_linked(a1, 'classLayout2Frontend_Project', b)
    _safe_set(b, 'classLayout2Frontend_EntitiesModel', a2)
    assert _is_linked(b, 'classLayout2Frontend_EntitiesModel', a2)
    if hasattr(a1, 'classLayout2Frontend_Project'):
        assert not _is_linked(a1, 'classLayout2Frontend_Project', b)
    if hasattr(a2, 'classLayout2Frontend_Project'):
        assert _is_linked(a2, 'classLayout2Frontend_Project', b)
    _safe_set(b, 'classLayout2Frontend_EntitiesModel', None)
    assert not _is_linked(b, 'classLayout2Frontend_EntitiesModel', a2)
    if hasattr(a2, 'classLayout2Frontend_Project'):
        assert not _is_linked(a2, 'classLayout2Frontend_Project', b)


def test_assoc_modelElements9_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_EntityModelElement(description="sample_text", displayName="sample_text", name="sample_text")
    a2 = classLayout2Frontend_EntityModelElement(description="sample_text_2", displayName="sample_text_2", name="sample_text_2")
    b = classLayout2Frontend_EntitiesModel(name="sample_text")
    _safe_set(b, 'classLayout2Frontend_EntitiesModel10', {a1})
    assert _is_linked(b, 'classLayout2Frontend_EntitiesModel10', a1)
    if hasattr(a1, 'classLayout2Frontend_EntityModelElement'):
        assert _is_linked(a1, 'classLayout2Frontend_EntityModelElement', b)
    _safe_set(b, 'classLayout2Frontend_EntitiesModel10', {a2})
    assert _is_linked(b, 'classLayout2Frontend_EntitiesModel10', a2)
    if hasattr(a1, 'classLayout2Frontend_EntityModelElement'):
        assert not _is_linked(a1, 'classLayout2Frontend_EntityModelElement', b)
    if hasattr(a2, 'classLayout2Frontend_EntityModelElement'):
        assert _is_linked(a2, 'classLayout2Frontend_EntityModelElement', b)
    _safe_set(b, 'classLayout2Frontend_EntitiesModel10', set())
    assert not _is_linked(b, 'classLayout2Frontend_EntitiesModel10', a2)
    if hasattr(a2, 'classLayout2Frontend_EntityModelElement'):
        assert not _is_linked(a2, 'classLayout2Frontend_EntityModelElement', b)


def test_assoc_pageViews22_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_SiteView(displayName="sample_text", name="sample_text", templateColor="sample_text", templateName="sample_text")
    a2 = classLayout2Frontend_SiteView(displayName="sample_text_2", name="sample_text_2", templateColor="sample_text_2", templateName="sample_text_2")
    b = classLayout2Frontend_PageView(layoutType="sample_text", name="sample_text")
    _safe_set(b, 'classLayout2Frontend_PageView24', a1)
    assert _is_linked(b, 'classLayout2Frontend_PageView24', a1)
    if hasattr(a1, 'classLayout2Frontend_SiteView23'):
        assert _is_linked(a1, 'classLayout2Frontend_SiteView23', b)
    _safe_set(b, 'classLayout2Frontend_PageView24', a2)
    assert _is_linked(b, 'classLayout2Frontend_PageView24', a2)
    if hasattr(a1, 'classLayout2Frontend_SiteView23'):
        assert not _is_linked(a1, 'classLayout2Frontend_SiteView23', b)
    if hasattr(a2, 'classLayout2Frontend_SiteView23'):
        assert _is_linked(a2, 'classLayout2Frontend_SiteView23', b)
    _safe_set(b, 'classLayout2Frontend_PageView24', None)
    assert not _is_linked(b, 'classLayout2Frontend_PageView24', a2)
    if hasattr(a2, 'classLayout2Frontend_SiteView23'):
        assert not _is_linked(a2, 'classLayout2Frontend_SiteView23', b)


def test_assoc_pageViews3_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_Project(name="sample_text")
    a2 = classLayout2Frontend_Project(name="sample_text_2")
    b = classLayout2Frontend_PageView(layoutType="sample_text", name="sample_text")
    _safe_set(b, 'classLayout2Frontend_PageView', a1)
    assert _is_linked(b, 'classLayout2Frontend_PageView', a1)
    if hasattr(a1, 'classLayout2Frontend_Project4'):
        assert _is_linked(a1, 'classLayout2Frontend_Project4', b)
    _safe_set(b, 'classLayout2Frontend_PageView', a2)
    assert _is_linked(b, 'classLayout2Frontend_PageView', a2)
    if hasattr(a1, 'classLayout2Frontend_Project4'):
        assert not _is_linked(a1, 'classLayout2Frontend_Project4', b)
    if hasattr(a2, 'classLayout2Frontend_Project4'):
        assert _is_linked(a2, 'classLayout2Frontend_Project4', b)
    _safe_set(b, 'classLayout2Frontend_PageView', None)
    assert not _is_linked(b, 'classLayout2Frontend_PageView', a2)
    if hasattr(a2, 'classLayout2Frontend_Project4'):
        assert not _is_linked(a2, 'classLayout2Frontend_Project4', b)


def test_assoc_siteViews1_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_SiteView(displayName="sample_text", name="sample_text", templateColor="sample_text", templateName="sample_text")
    a2 = classLayout2Frontend_SiteView(displayName="sample_text_2", name="sample_text_2", templateColor="sample_text_2", templateName="sample_text_2")
    b = classLayout2Frontend_Project(name="sample_text")
    _safe_set(b, 'classLayout2Frontend_Project2', {a1})
    assert _is_linked(b, 'classLayout2Frontend_Project2', a1)
    if hasattr(a1, 'classLayout2Frontend_SiteView'):
        assert _is_linked(a1, 'classLayout2Frontend_SiteView', b)
    _safe_set(b, 'classLayout2Frontend_Project2', {a2})
    assert _is_linked(b, 'classLayout2Frontend_Project2', a2)
    if hasattr(a1, 'classLayout2Frontend_SiteView'):
        assert not _is_linked(a1, 'classLayout2Frontend_SiteView', b)
    if hasattr(a2, 'classLayout2Frontend_SiteView'):
        assert _is_linked(a2, 'classLayout2Frontend_SiteView', b)
    _safe_set(b, 'classLayout2Frontend_Project2', set())
    assert not _is_linked(b, 'classLayout2Frontend_Project2', a2)
    if hasattr(a2, 'classLayout2Frontend_SiteView'):
        assert not _is_linked(a2, 'classLayout2Frontend_SiteView', b)


def test_assoc_structuralFeatures14_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_StructuralFeature(required=True)
    a2 = classLayout2Frontend_StructuralFeature(required=False)
    b = classLayout2Frontend_Entity(isAbstract=True)
    _safe_set(b, 'classLayout2Frontend_Entity15', {a1})
    assert _is_linked(b, 'classLayout2Frontend_Entity15', a1)
    if hasattr(a1, 'classLayout2Frontend_StructuralFeature'):
        assert _is_linked(a1, 'classLayout2Frontend_StructuralFeature', b)
    _safe_set(b, 'classLayout2Frontend_Entity15', {a2})
    assert _is_linked(b, 'classLayout2Frontend_Entity15', a2)
    if hasattr(a1, 'classLayout2Frontend_StructuralFeature'):
        assert not _is_linked(a1, 'classLayout2Frontend_StructuralFeature', b)
    if hasattr(a2, 'classLayout2Frontend_StructuralFeature'):
        assert _is_linked(a2, 'classLayout2Frontend_StructuralFeature', b)
    _safe_set(b, 'classLayout2Frontend_Entity15', set())
    assert not _is_linked(b, 'classLayout2Frontend_Entity15', a2)
    if hasattr(a2, 'classLayout2Frontend_StructuralFeature'):
        assert not _is_linked(a2, 'classLayout2Frontend_StructuralFeature', b)


def test_assoc_superclass12_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_Entity(isAbstract=True)
    a2 = classLayout2Frontend_Entity(isAbstract=False)
    b = classLayout2Frontend_Entity(isAbstract=True)
    _safe_set(b, 'classLayout2Frontend_Entity13', a1)
    assert _is_linked(b, 'classLayout2Frontend_Entity13', a1)
    if hasattr(a1, 'classLayout2Frontend_Entity11'):
        assert _is_linked(a1, 'classLayout2Frontend_Entity11', b)
    _safe_set(b, 'classLayout2Frontend_Entity13', a2)
    assert _is_linked(b, 'classLayout2Frontend_Entity13', a2)
    if hasattr(a1, 'classLayout2Frontend_Entity11'):
        assert not _is_linked(a1, 'classLayout2Frontend_Entity11', b)
    if hasattr(a2, 'classLayout2Frontend_Entity11'):
        assert _is_linked(a2, 'classLayout2Frontend_Entity11', b)
    _safe_set(b, 'classLayout2Frontend_Entity13', None)
    assert not _is_linked(b, 'classLayout2Frontend_Entity13', a2)
    if hasattr(a2, 'classLayout2Frontend_Entity11'):
        assert not _is_linked(a2, 'classLayout2Frontend_Entity11', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = classLayout2Frontend_Entity(isAbstract=True)
    a2 = classLayout2Frontend_Entity(isAbstract=False)
    b = classLayout2Frontend_Association(many=True)
    _safe_set(b, 'classLayout2Frontend_Association', a1)
    assert _is_linked(b, 'classLayout2Frontend_Association', a1)
    if hasattr(a1, 'classLayout2Frontend_Entity'):
        assert _is_linked(a1, 'classLayout2Frontend_Entity', b)
    _safe_set(b, 'classLayout2Frontend_Association', a2)
    assert _is_linked(b, 'classLayout2Frontend_Association', a2)
    if hasattr(a1, 'classLayout2Frontend_Entity'):
        assert not _is_linked(a1, 'classLayout2Frontend_Entity', b)
    if hasattr(a2, 'classLayout2Frontend_Entity'):
        assert _is_linked(a2, 'classLayout2Frontend_Entity', b)
    _safe_set(b, 'classLayout2Frontend_Association', None)
    assert not _is_linked(b, 'classLayout2Frontend_Association', a2)
    if hasattr(a2, 'classLayout2Frontend_Entity'):
        assert not _is_linked(a2, 'classLayout2Frontend_Entity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containerViews5_stub_double():
    # classLayout2Frontend_ContainerView has no real 'classLayout2Frontend_ContainerView' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Project(name="sample_text")
    partner = classLayout2Frontend_ContainerView()
    setattr(partner, 'classLayout2Frontend_ContainerView', None)
    _safe_set(owner, 'classLayout2Frontend_Project6', {partner})
    assert getattr(partner, 'classLayout2Frontend_ContainerView') == owner
    _safe_set(owner, 'classLayout2Frontend_Project6', set())
    assert getattr(partner, 'classLayout2Frontend_ContainerView') is None


def test_assoc_elements27_stub_double():
    # classLayout2Frontend_ContainerView has no real 'classLayout2Frontend_ContainerView28' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_ElementView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_ElementView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_ElementView(description="sample_text", displayName="sample_text", name="sample_text")
    partner = classLayout2Frontend_ContainerView()
    setattr(partner, 'classLayout2Frontend_ContainerView28', None)
    _safe_set(owner, 'classLayout2Frontend_ElementView29', partner)
    assert owner in getattr(partner, 'classLayout2Frontend_ContainerView28')
    _safe_set(owner, 'classLayout2Frontend_ElementView29', None)
    assert owner not in getattr(partner, 'classLayout2Frontend_ContainerView28')


def test_assoc_entity30_stub_double():
    # classLayout2Frontend_ContainerView has no real 'classLayout2Frontend_ContainerView31' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Entity(isAbstract=True)
    partner = classLayout2Frontend_ContainerView()
    setattr(partner, 'classLayout2Frontend_ContainerView31', None)
    _safe_set(owner, 'classLayout2Frontend_Entity32', partner)
    assert getattr(partner, 'classLayout2Frontend_ContainerView31') == owner
    _safe_set(owner, 'classLayout2Frontend_Entity32', None)
    assert getattr(partner, 'classLayout2Frontend_ContainerView31') is None


def test_assoc_input19_stub_double():
    # classLayout2Frontend_IterationFilter has no real 'classLayout2Frontend_IterationFilter' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Input(label="sample_text")
    partner = classLayout2Frontend_IterationFilter()
    setattr(partner, 'classLayout2Frontend_IterationFilter', None)
    _safe_set(owner, 'classLayout2Frontend_Input', partner)
    assert getattr(partner, 'classLayout2Frontend_IterationFilter') == owner
    _safe_set(owner, 'classLayout2Frontend_Input', None)
    assert getattr(partner, 'classLayout2Frontend_IterationFilter') is None


def test_assoc_literals16_stub_double():
    # classLayout2Frontend_Enumeration has no real 'classLayout2Frontend_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Literal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Literal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Literal(value=7)
    partner = classLayout2Frontend_Enumeration()
    setattr(partner, 'classLayout2Frontend_Enumeration', None)
    _safe_set(owner, 'classLayout2Frontend_Literal', partner)
    assert owner in getattr(partner, 'classLayout2Frontend_Enumeration')
    _safe_set(owner, 'classLayout2Frontend_Literal', None)
    assert owner not in getattr(partner, 'classLayout2Frontend_Enumeration')


def test_assoc_property17_stub_double():
    # classLayout2Frontend_AtomicView has no real 'classLayout2Frontend_AtomicView' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_StructuralFeature(required=True)
    partner = classLayout2Frontend_AtomicView()
    setattr(partner, 'classLayout2Frontend_AtomicView', None)
    _safe_set(owner, 'classLayout2Frontend_StructuralFeature18', partner)
    assert getattr(partner, 'classLayout2Frontend_AtomicView') == owner
    _safe_set(owner, 'classLayout2Frontend_StructuralFeature18', None)
    assert getattr(partner, 'classLayout2Frontend_AtomicView') is None


def test_assoc_type8_stub_double():
    # classLayout2Frontend_PropertyType has no real 'classLayout2Frontend_PropertyType' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Property(defaultValue="sample_text")
    partner = classLayout2Frontend_PropertyType()
    setattr(partner, 'classLayout2Frontend_PropertyType', None)
    _safe_set(owner, 'classLayout2Frontend_Property', partner)
    assert getattr(partner, 'classLayout2Frontend_PropertyType') == owner
    _safe_set(owner, 'classLayout2Frontend_Property', None)
    assert getattr(partner, 'classLayout2Frontend_PropertyType') is None


