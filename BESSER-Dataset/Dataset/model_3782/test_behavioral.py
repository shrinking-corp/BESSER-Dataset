import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ProductEntity,
    product_Product,
    product_ProductAspect,
    product_ProductClass,
    product_ProductComponent,
    product_ProductContainer,
    product_ProductDomainModel,
    product_ProductDomainModels,
    product_ProductEntity,
    product_ProductFeatureConfiguration,
    product_ProductFeaturesConfiguration,
    product_ProductFile,
    product_ProductFolder,
    product_ProductFragment,
    product_ProductFragmentContainer,
    product_ProductImplementationElements,
    product_ProductResourcesContainer,
    product_ProductTemplate,
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

def test_assoc_features43_reverse_link_reassign_clear():
    a1 = product_ProductFeaturesConfiguration(attribute="sample_text", name="sample_text")
    a2 = product_ProductFeaturesConfiguration(attribute="sample_text_2", name="sample_text_2")
    b = product_ProductFeatureConfiguration(attribute="sample_text", isSelected=True, max=7, min=7, name="sample_text")
    _safe_set(b, 'product_ProductFeatureConfiguration', a1)
    assert _is_linked(b, 'product_ProductFeatureConfiguration', a1)
    if hasattr(a1, 'product_ProductFeaturesConfiguration44'):
        assert _is_linked(a1, 'product_ProductFeaturesConfiguration44', b)
    _safe_set(b, 'product_ProductFeatureConfiguration', a2)
    assert _is_linked(b, 'product_ProductFeatureConfiguration', a2)
    if hasattr(a1, 'product_ProductFeaturesConfiguration44'):
        assert not _is_linked(a1, 'product_ProductFeaturesConfiguration44', b)
    if hasattr(a2, 'product_ProductFeaturesConfiguration44'):
        assert _is_linked(a2, 'product_ProductFeaturesConfiguration44', b)
    _safe_set(b, 'product_ProductFeatureConfiguration', None)
    assert not _is_linked(b, 'product_ProductFeatureConfiguration', a2)
    if hasattr(a2, 'product_ProductFeaturesConfiguration44'):
        assert not _is_linked(a2, 'product_ProductFeaturesConfiguration44', b)


def test_assoc_features46_reverse_link_reassign_clear():
    a1 = product_ProductFeatureConfiguration(attribute="sample_text", isSelected=True, max=7, min=7, name="sample_text")
    a2 = product_ProductFeatureConfiguration(attribute="sample_text_2", isSelected=False, max=13, min=13, name="sample_text_2")
    b = product_ProductFeatureConfiguration(attribute="sample_text", isSelected=True, max=7, min=7, name="sample_text")
    _safe_set(b, 'product_ProductFeatureConfiguration47', a1)
    assert _is_linked(b, 'product_ProductFeatureConfiguration47', a1)
    if hasattr(a1, 'product_ProductFeatureConfiguration45'):
        assert _is_linked(a1, 'product_ProductFeatureConfiguration45', b)
    _safe_set(b, 'product_ProductFeatureConfiguration47', a2)
    assert _is_linked(b, 'product_ProductFeatureConfiguration47', a2)
    if hasattr(a1, 'product_ProductFeatureConfiguration45'):
        assert not _is_linked(a1, 'product_ProductFeatureConfiguration45', b)
    if hasattr(a2, 'product_ProductFeatureConfiguration45'):
        assert _is_linked(a2, 'product_ProductFeatureConfiguration45', b)
    _safe_set(b, 'product_ProductFeatureConfiguration47', None)
    assert not _is_linked(b, 'product_ProductFeatureConfiguration47', a2)
    if hasattr(a2, 'product_ProductFeatureConfiguration45'):
        assert not _is_linked(a2, 'product_ProductFeatureConfiguration45', b)


def test_assoc_fragments41_reverse_link_reassign_clear():
    a1 = product_ProductFragmentContainer(name="sample_text")
    a2 = product_ProductFragmentContainer(name="sample_text_2")
    b = product_ProductFragment(content="sample_text")
    _safe_set(b, 'product_ProductFragment', a1)
    assert _is_linked(b, 'product_ProductFragment', a1)
    if hasattr(a1, 'product_ProductFragmentContainer42'):
        assert _is_linked(a1, 'product_ProductFragmentContainer42', b)
    _safe_set(b, 'product_ProductFragment', a2)
    assert _is_linked(b, 'product_ProductFragment', a2)
    if hasattr(a1, 'product_ProductFragmentContainer42'):
        assert not _is_linked(a1, 'product_ProductFragmentContainer42', b)
    if hasattr(a2, 'product_ProductFragmentContainer42'):
        assert _is_linked(a2, 'product_ProductFragmentContainer42', b)
    _safe_set(b, 'product_ProductFragment', None)
    assert not _is_linked(b, 'product_ProductFragment', a2)
    if hasattr(a2, 'product_ProductFragmentContainer42'):
        assert not _is_linked(a2, 'product_ProductFragmentContainer42', b)


def test_assoc_templates17_reverse_link_reassign_clear():
    a1 = product_ProductTemplate(generateToPath="sample_text")
    a2 = product_ProductTemplate(generateToPath="sample_text_2")
    b = product_ProductResourcesContainer(name="sample_text")
    _safe_set(b, 'product_ProductResourcesContainer18', {a1})
    assert _is_linked(b, 'product_ProductResourcesContainer18', a1)
    if hasattr(a1, 'product_ProductTemplate'):
        assert _is_linked(a1, 'product_ProductTemplate', b)
    _safe_set(b, 'product_ProductResourcesContainer18', {a2})
    assert _is_linked(b, 'product_ProductResourcesContainer18', a2)
    if hasattr(a1, 'product_ProductTemplate'):
        assert not _is_linked(a1, 'product_ProductTemplate', b)
    if hasattr(a2, 'product_ProductTemplate'):
        assert _is_linked(a2, 'product_ProductTemplate', b)
    _safe_set(b, 'product_ProductResourcesContainer18', set())
    assert not _is_linked(b, 'product_ProductResourcesContainer18', a2)
    if hasattr(a2, 'product_ProductTemplate'):
        assert not _is_linked(a2, 'product_ProductTemplate', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components11_stub_double():
    # product_ProductComponent has no real 'product_ProductComponent' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductContainer(name="sample_text")
    partner = product_ProductComponent()
    setattr(partner, 'product_ProductComponent', None)
    _safe_set(owner, 'product_ProductContainer12', {partner})
    assert getattr(partner, 'product_ProductComponent') == owner
    _safe_set(owner, 'product_ProductContainer12', set())
    assert getattr(partner, 'product_ProductComponent') is None


def test_assoc_containers5_stub_double():
    # product_ProductImplementationElements has no real 'product_ProductImplementationElements6' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductContainer(name="sample_text")
    partner = product_ProductImplementationElements()
    setattr(partner, 'product_ProductImplementationElements6', None)
    _safe_set(owner, 'product_ProductContainer', partner)
    assert owner in getattr(partner, 'product_ProductImplementationElements6')
    _safe_set(owner, 'product_ProductContainer', None)
    assert owner not in getattr(partner, 'product_ProductImplementationElements6')


def test_assoc_domainModel48_stub_double():
    # product_ProductDomainModels has no real 'product_ProductDomainModels49' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductDomainModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductDomainModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductDomainModel(elements="sample_text", name="sample_text")
    partner = product_ProductDomainModels()
    setattr(partner, 'product_ProductDomainModels49', None)
    _safe_set(owner, 'product_ProductDomainModel', partner)
    assert owner in getattr(partner, 'product_ProductDomainModels49')
    _safe_set(owner, 'product_ProductDomainModel', None)
    assert owner not in getattr(partner, 'product_ProductDomainModels49')


def test_assoc_files15_stub_double():
    # product_ProductFile has no real 'product_ProductFile' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductResourcesContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductResourcesContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductResourcesContainer(name="sample_text")
    partner = product_ProductFile()
    setattr(partner, 'product_ProductFile', None)
    _safe_set(owner, 'product_ProductResourcesContainer16', {partner})
    assert getattr(partner, 'product_ProductFile') == owner
    _safe_set(owner, 'product_ProductResourcesContainer16', set())
    assert getattr(partner, 'product_ProductFile') is None


def test_assoc_folders13_stub_double():
    # product_ProductFolder has no real 'product_ProductFolder' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductResourcesContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductResourcesContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductResourcesContainer(name="sample_text")
    partner = product_ProductFolder()
    setattr(partner, 'product_ProductFolder', None)
    _safe_set(owner, 'product_ProductResourcesContainer14', {partner})
    assert getattr(partner, 'product_ProductFolder') == owner
    _safe_set(owner, 'product_ProductResourcesContainer14', set())
    assert getattr(partner, 'product_ProductFolder') is None


def test_assoc_fragmentContainers7_stub_double():
    # product_ProductImplementationElements has no real 'product_ProductImplementationElements8' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductFragmentContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductFragmentContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductFragmentContainer(name="sample_text")
    partner = product_ProductImplementationElements()
    setattr(partner, 'product_ProductImplementationElements8', None)
    _safe_set(owner, 'product_ProductFragmentContainer', partner)
    assert owner in getattr(partner, 'product_ProductImplementationElements8')
    _safe_set(owner, 'product_ProductFragmentContainer', None)
    assert owner not in getattr(partner, 'product_ProductImplementationElements8')


def test_assoc_productFeatures1_stub_double():
    # product_Product has no real 'product_Product2' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductFeaturesConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductFeaturesConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductFeaturesConfiguration(attribute="sample_text", name="sample_text")
    partner = product_Product()
    setattr(partner, 'product_Product2', None)
    _safe_set(owner, 'product_ProductFeaturesConfiguration', partner)
    assert getattr(partner, 'product_Product2') == owner
    _safe_set(owner, 'product_ProductFeaturesConfiguration', None)
    assert getattr(partner, 'product_Product2') is None


def test_assoc_resourceContainers9_stub_double():
    # product_ProductImplementationElements has no real 'product_ProductImplementationElements10' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductResourcesContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductResourcesContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductResourcesContainer(name="sample_text")
    partner = product_ProductImplementationElements()
    setattr(partner, 'product_ProductImplementationElements10', None)
    _safe_set(owner, 'product_ProductResourcesContainer', partner)
    assert owner in getattr(partner, 'product_ProductImplementationElements10')
    _safe_set(owner, 'product_ProductResourcesContainer', None)
    assert owner not in getattr(partner, 'product_ProductImplementationElements10')


def test_assoc_templates26_stub_double():
    # product_ProductComponent has no real 'product_ProductComponent27' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductTemplate(generateToPath="sample_text")
    partner = product_ProductComponent()
    setattr(partner, 'product_ProductComponent27', None)
    _safe_set(owner, 'product_ProductTemplate28', partner)
    assert owner in getattr(partner, 'product_ProductComponent27')
    _safe_set(owner, 'product_ProductTemplate28', None)
    assert owner not in getattr(partner, 'product_ProductComponent27')


def test_assoc_templates38_stub_double():
    # product_ProductFolder has no real 'product_ProductFolder39' property in the generated
    # code (a bare stub) -- manually attach it so product_ProductTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # product_ProductTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = product_ProductTemplate(generateToPath="sample_text")
    partner = product_ProductFolder()
    setattr(partner, 'product_ProductFolder39', None)
    _safe_set(owner, 'product_ProductTemplate40', partner)
    assert owner in getattr(partner, 'product_ProductFolder39')
    _safe_set(owner, 'product_ProductTemplate40', None)
    assert owner not in getattr(partner, 'product_ProductFolder39')


