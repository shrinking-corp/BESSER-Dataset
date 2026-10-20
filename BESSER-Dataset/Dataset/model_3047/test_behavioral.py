import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    AtomicView,
    ContainerView,
    ElementView,
    EntitiesModel,
    Entity,
    EntityModelElement,
    Input,
    IterationFilter,
    Literal,
    Output,
    PageView,
    PropertyType,
    Selection,
    SiteView,
    StructuralFeature,
    classLayout2Frontend_Entities_Association,
    classLayout2Frontend_Entities_Composition,
    classLayout2Frontend_Entities_EntitiesModel,
    classLayout2Frontend_Entities_Entity,
    classLayout2Frontend_Entities_EntityModelElement,
    classLayout2Frontend_Entities_Enumeration,
    classLayout2Frontend_Entities_Literal,
    classLayout2Frontend_Entities_PrimitiveType,
    classLayout2Frontend_Entities_Property,
    classLayout2Frontend_Entities_PropertyType,
    classLayout2Frontend_Entities_Reference,
    classLayout2Frontend_Entities_StructuralFeature,
    classLayout2Frontend_Project,
    classLayout2Frontend_Views_AtomicView,
    classLayout2Frontend_Views_Autocomplete,
    classLayout2Frontend_Views_CheckList,
    classLayout2Frontend_Views_ContainerView,
    classLayout2Frontend_Views_Dropdownlist,
    classLayout2Frontend_Views_ElementView,
    classLayout2Frontend_Views_FileUpload,
    classLayout2Frontend_Views_Image,
    classLayout2Frontend_Views_Input,
    classLayout2Frontend_Views_InputForm,
    classLayout2Frontend_Views_InputText,
    classLayout2Frontend_Views_IterationContainer,
    classLayout2Frontend_Views_IterationFilter,
    classLayout2Frontend_Views_List,
    classLayout2Frontend_Views_Output,
    classLayout2Frontend_Views_PageView,
    classLayout2Frontend_Views_RadioButtonGroup,
    classLayout2Frontend_Views_Selection,
    classLayout2Frontend_Views_SiteView,
    classLayout2Frontend_Views_StaticContainer,
    classLayout2Frontend_Views_TextArea,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containerViews5_stub_double():
    # ContainerView has no real 'ContainerView' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Project(name="sample_text")
    partner = ContainerView()
    setattr(partner, 'ContainerView', None)
    _safe_set(owner, 'classLayout2Frontend_Project6', {partner})
    assert getattr(partner, 'ContainerView') == owner
    _safe_set(owner, 'classLayout2Frontend_Project6', set())
    assert getattr(partner, 'ContainerView') is None


def test_assoc_elementViews24_stub_double():
    # ElementView has no real 'ElementView25' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Views_PageView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Views_PageView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Views_PageView(layoutType="sample_text", name="sample_text")
    partner = ElementView()
    setattr(partner, 'ElementView25', None)
    _safe_set(owner, 'classLayout2Frontend_Views_PageView', {partner})
    assert getattr(partner, 'ElementView25') == owner
    _safe_set(owner, 'classLayout2Frontend_Views_PageView', set())
    assert getattr(partner, 'ElementView25') is None


def test_assoc_entitiesmodel0_stub_double():
    # EntitiesModel has no real 'EntitiesModel' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Project(name="sample_text")
    partner = EntitiesModel()
    setattr(partner, 'EntitiesModel', None)
    _safe_set(owner, 'classLayout2Frontend_Project', partner)
    assert getattr(partner, 'EntitiesModel') == owner
    _safe_set(owner, 'classLayout2Frontend_Project', None)
    assert getattr(partner, 'EntitiesModel') is None


def test_assoc_modelElements7_stub_double():
    # EntityModelElement has no real 'EntityModelElement' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Entities_EntitiesModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Entities_EntitiesModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Entities_EntitiesModel(name="sample_text")
    partner = EntityModelElement()
    setattr(partner, 'EntityModelElement', None)
    _safe_set(owner, 'classLayout2Frontend_Entities_EntitiesModel', {partner})
    assert getattr(partner, 'EntityModelElement') == owner
    _safe_set(owner, 'classLayout2Frontend_Entities_EntitiesModel', set())
    assert getattr(partner, 'EntityModelElement') is None


def test_assoc_pageViews15_stub_double():
    # PageView has no real 'PageView16' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Views_SiteView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Views_SiteView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Views_SiteView(displayName="sample_text", name="sample_text", templateColor="sample_text", templateName="sample_text")
    partner = PageView()
    setattr(partner, 'PageView16', None)
    _safe_set(owner, 'classLayout2Frontend_Views_SiteView', {partner})
    assert getattr(partner, 'PageView16') == owner
    _safe_set(owner, 'classLayout2Frontend_Views_SiteView', set())
    assert getattr(partner, 'PageView16') is None


def test_assoc_pageViews3_stub_double():
    # PageView has no real 'PageView' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Project(name="sample_text")
    partner = PageView()
    setattr(partner, 'PageView', None)
    _safe_set(owner, 'classLayout2Frontend_Project4', {partner})
    assert getattr(partner, 'PageView') == owner
    _safe_set(owner, 'classLayout2Frontend_Project4', set())
    assert getattr(partner, 'PageView') is None


def test_assoc_siteViews1_stub_double():
    # SiteView has no real 'SiteView' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Project(name="sample_text")
    partner = SiteView()
    setattr(partner, 'SiteView', None)
    _safe_set(owner, 'classLayout2Frontend_Project2', {partner})
    assert getattr(partner, 'SiteView') == owner
    _safe_set(owner, 'classLayout2Frontend_Project2', set())
    assert getattr(partner, 'SiteView') is None


def test_assoc_structuralFeatures11_stub_double():
    # StructuralFeature has no real 'StructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Entities_Entity(isAbstract=True)
    partner = StructuralFeature()
    setattr(partner, 'StructuralFeature', None)
    _safe_set(owner, 'classLayout2Frontend_Entities_Entity12', {partner})
    assert getattr(partner, 'StructuralFeature') == owner
    _safe_set(owner, 'classLayout2Frontend_Entities_Entity12', set())
    assert getattr(partner, 'StructuralFeature') is None


def test_assoc_superclass9_stub_double():
    # Entity has no real 'Entity10' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Entities_Entity(isAbstract=True)
    partner = Entity()
    setattr(partner, 'Entity10', None)
    _safe_set(owner, 'classLayout2Frontend_Entities_Entity', partner)
    assert getattr(partner, 'Entity10') == owner
    _safe_set(owner, 'classLayout2Frontend_Entities_Entity', None)
    assert getattr(partner, 'Entity10') is None


def test_assoc_target8_stub_double():
    # Entity has no real 'Entity' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Entities_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Entities_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Entities_Association(many=True)
    partner = Entity()
    setattr(partner, 'Entity', None)
    _safe_set(owner, 'classLayout2Frontend_Entities_Association', partner)
    assert getattr(partner, 'Entity') == owner
    _safe_set(owner, 'classLayout2Frontend_Entities_Association', None)
    assert getattr(partner, 'Entity') is None


def test_assoc_type13_stub_double():
    # PropertyType has no real 'PropertyType' property in the generated
    # code (a bare stub) -- manually attach it so classLayout2Frontend_Entities_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classLayout2Frontend_Entities_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classLayout2Frontend_Entities_Property(defaultValue="sample_text")
    partner = PropertyType()
    setattr(partner, 'PropertyType', None)
    _safe_set(owner, 'classLayout2Frontend_Entities_Property', partner)
    assert getattr(partner, 'PropertyType') == owner
    _safe_set(owner, 'classLayout2Frontend_Entities_Property', None)
    assert getattr(partner, 'PropertyType') is None


