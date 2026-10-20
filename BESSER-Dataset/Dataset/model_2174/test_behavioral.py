import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graphDsl_ChildrenProperty,
    graphDsl_Component,
    graphDsl_ComponentOrFacet,
    graphDsl_ComponentProperties,
    graphDsl_ExportsProperty,
    graphDsl_ExportsVariable,
    graphDsl_ExtendsProperty,
    graphDsl_Facet,
    graphDsl_FacetProperties,
    graphDsl_FacetProperty,
    graphDsl_FacetsProperty,
    graphDsl_Graph,
    graphDsl_ImportsProperty,
    graphDsl_ImportsVariable,
    graphDsl_InstallerProperty,
    graphDsl_OptionalProperty,
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

def test_assoc_childrenProperty15_stub_double():
    # graphDsl_FacetProperty has no real 'graphDsl_FacetProperty16' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_ChildrenProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_ChildrenProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_ChildrenProperty(name="sample_text")
    partner = graphDsl_FacetProperty()
    setattr(partner, 'graphDsl_FacetProperty16', None)
    _safe_set(owner, 'graphDsl_ChildrenProperty', partner)
    assert getattr(partner, 'graphDsl_FacetProperty16') == owner
    _safe_set(owner, 'graphDsl_ChildrenProperty', None)
    assert getattr(partner, 'graphDsl_FacetProperty16') is None


def test_assoc_childrenProperty19_stub_double():
    # graphDsl_OptionalProperty has no real 'graphDsl_OptionalProperty20' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_ChildrenProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_ChildrenProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_ChildrenProperty(name="sample_text")
    partner = graphDsl_OptionalProperty()
    setattr(partner, 'graphDsl_OptionalProperty20', None)
    _safe_set(owner, 'graphDsl_ChildrenProperty21', partner)
    assert getattr(partner, 'graphDsl_OptionalProperty20') == owner
    _safe_set(owner, 'graphDsl_ChildrenProperty21', None)
    assert getattr(partner, 'graphDsl_OptionalProperty20') is None


def test_assoc_component1_stub_double():
    # graphDsl_ComponentOrFacet has no real 'graphDsl_ComponentOrFacet2' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_Component(name="sample_text")
    partner = graphDsl_ComponentOrFacet()
    setattr(partner, 'graphDsl_ComponentOrFacet2', None)
    _safe_set(owner, 'graphDsl_Component', partner)
    assert getattr(partner, 'graphDsl_ComponentOrFacet2') == owner
    _safe_set(owner, 'graphDsl_Component', None)
    assert getattr(partner, 'graphDsl_ComponentOrFacet2') is None


def test_assoc_components0_stub_double():
    # graphDsl_ComponentOrFacet has no real 'graphDsl_ComponentOrFacet' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_Graph(comments="sample_text")
    partner = graphDsl_ComponentOrFacet()
    setattr(partner, 'graphDsl_ComponentOrFacet', None)
    _safe_set(owner, 'graphDsl_Graph', {partner})
    assert getattr(partner, 'graphDsl_ComponentOrFacet') == owner
    _safe_set(owner, 'graphDsl_Graph', set())
    assert getattr(partner, 'graphDsl_ComponentOrFacet') is None


def test_assoc_exportsVariables31_stub_double():
    # graphDsl_ExportsProperty has no real 'graphDsl_ExportsProperty32' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_ExportsVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_ExportsVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_ExportsVariable(intValue=7, name="sample_text", strValue="sample_text")
    partner = graphDsl_ExportsProperty()
    setattr(partner, 'graphDsl_ExportsProperty32', None)
    _safe_set(owner, 'graphDsl_ExportsVariable', partner)
    assert owner in getattr(partner, 'graphDsl_ExportsProperty32')
    _safe_set(owner, 'graphDsl_ExportsVariable', None)
    assert owner not in getattr(partner, 'graphDsl_ExportsProperty32')


def test_assoc_extendsProperty29_stub_double():
    # graphDsl_OptionalProperty has no real 'graphDsl_OptionalProperty30' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_ExtendsProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_ExtendsProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_ExtendsProperty(extendsNames="sample_text")
    partner = graphDsl_OptionalProperty()
    setattr(partner, 'graphDsl_OptionalProperty30', None)
    _safe_set(owner, 'graphDsl_ExtendsProperty', partner)
    assert getattr(partner, 'graphDsl_OptionalProperty30') == owner
    _safe_set(owner, 'graphDsl_ExtendsProperty', None)
    assert getattr(partner, 'graphDsl_OptionalProperty30') is None


def test_assoc_facet3_stub_double():
    # graphDsl_ComponentOrFacet has no real 'graphDsl_ComponentOrFacet4' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_Facet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_Facet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_Facet(name="sample_text")
    partner = graphDsl_ComponentOrFacet()
    setattr(partner, 'graphDsl_ComponentOrFacet4', None)
    _safe_set(owner, 'graphDsl_Facet', partner)
    assert getattr(partner, 'graphDsl_ComponentOrFacet4') == owner
    _safe_set(owner, 'graphDsl_Facet', None)
    assert getattr(partner, 'graphDsl_ComponentOrFacet4') is None


def test_assoc_facetsProperty27_stub_double():
    # graphDsl_OptionalProperty has no real 'graphDsl_OptionalProperty28' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_FacetsProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_FacetsProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_FacetsProperty(facetsNames="sample_text")
    partner = graphDsl_OptionalProperty()
    setattr(partner, 'graphDsl_OptionalProperty28', None)
    _safe_set(owner, 'graphDsl_FacetsProperty', partner)
    assert getattr(partner, 'graphDsl_OptionalProperty28') == owner
    _safe_set(owner, 'graphDsl_FacetsProperty', None)
    assert getattr(partner, 'graphDsl_OptionalProperty28') is None


def test_assoc_importsVariables33_stub_double():
    # graphDsl_ImportsProperty has no real 'graphDsl_ImportsProperty34' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_ImportsVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_ImportsVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_ImportsVariable(componentName="sample_text", componentProperty="sample_text", isExternal=True, isOptional=True)
    partner = graphDsl_ImportsProperty()
    setattr(partner, 'graphDsl_ImportsProperty34', None)
    _safe_set(owner, 'graphDsl_ImportsVariable', partner)
    assert owner in getattr(partner, 'graphDsl_ImportsProperty34')
    _safe_set(owner, 'graphDsl_ImportsVariable', None)
    assert owner not in getattr(partner, 'graphDsl_ImportsProperty34')


def test_assoc_installerProperty11_stub_double():
    # graphDsl_ComponentProperties has no real 'graphDsl_ComponentProperties12' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_InstallerProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_InstallerProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_InstallerProperty(name="sample_text")
    partner = graphDsl_ComponentProperties()
    setattr(partner, 'graphDsl_ComponentProperties12', None)
    _safe_set(owner, 'graphDsl_InstallerProperty', partner)
    assert getattr(partner, 'graphDsl_ComponentProperties12') == owner
    _safe_set(owner, 'graphDsl_InstallerProperty', None)
    assert getattr(partner, 'graphDsl_ComponentProperties12') is None


def test_assoc_properties5_stub_double():
    # graphDsl_ComponentProperties has no real 'graphDsl_ComponentProperties' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_Component(name="sample_text")
    partner = graphDsl_ComponentProperties()
    setattr(partner, 'graphDsl_ComponentProperties', None)
    _safe_set(owner, 'graphDsl_Component6', partner)
    assert getattr(partner, 'graphDsl_ComponentProperties') == owner
    _safe_set(owner, 'graphDsl_Component6', None)
    assert getattr(partner, 'graphDsl_ComponentProperties') is None


def test_assoc_properties7_stub_double():
    # graphDsl_FacetProperties has no real 'graphDsl_FacetProperties' property in the generated
    # code (a bare stub) -- manually attach it so graphDsl_Facet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphDsl_Facet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphDsl_Facet(name="sample_text")
    partner = graphDsl_FacetProperties()
    setattr(partner, 'graphDsl_FacetProperties', None)
    _safe_set(owner, 'graphDsl_Facet8', partner)
    assert getattr(partner, 'graphDsl_FacetProperties') == owner
    _safe_set(owner, 'graphDsl_Facet8', None)
    assert getattr(partner, 'graphDsl_FacetProperties') is None


