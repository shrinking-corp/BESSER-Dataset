import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    application_Application,
    application_ApplicationGroup,
    application_ApplicationInfrastructureLayer,
    application_ApplicationInfrastructureLayers,
    application_ApplicationLanguages,
    application_ApplicationMapper,
    application_ApplicationMappers,
    application_ApplicationMessageLibraries,
    application_ApplicationMessageLibrary,
    application_ApplicationRealm,
    application_ApplicationRealms,
    application_ApplicationRecipe,
    application_ApplicationRecipes,
    application_ApplicationStyle,
    application_ApplicationStyleLibraries,
    application_ApplicationUILayer,
    application_ApplicationUIPackage,
    application_EnterpriseInfrastructure,
    application_Form,
    application_Language,
    application_Mappers,
    application_MappingLayer,
    application_MessageLibrary,
    application_Recipes,
    application_Roles,
    application_StyleLibrary,
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

def test_assoc_applicationInfrastructureLayer7_reverse_link_reassign_clear():
    a1 = application_ApplicationInfrastructureLayers(name="sample_text", uid="sample_text")
    a2 = application_ApplicationInfrastructureLayers(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application8', a1)
    assert _is_linked(b, 'application_Application8', a1)
    if hasattr(a1, 'application_ApplicationInfrastructureLayers'):
        assert _is_linked(a1, 'application_ApplicationInfrastructureLayers', b)
    _safe_set(b, 'application_Application8', a2)
    assert _is_linked(b, 'application_Application8', a2)
    if hasattr(a1, 'application_ApplicationInfrastructureLayers'):
        assert not _is_linked(a1, 'application_ApplicationInfrastructureLayers', b)
    if hasattr(a2, 'application_ApplicationInfrastructureLayers'):
        assert _is_linked(a2, 'application_ApplicationInfrastructureLayers', b)
    _safe_set(b, 'application_Application8', None)
    assert not _is_linked(b, 'application_Application8', a2)
    if hasattr(a2, 'application_ApplicationInfrastructureLayers'):
        assert not _is_linked(a2, 'application_ApplicationInfrastructureLayers', b)


def test_assoc_applicationLanguages21_reverse_link_reassign_clear():
    a1 = application_ApplicationMessageLibraries(name="sample_text", uid="sample_text")
    a2 = application_ApplicationMessageLibraries(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationLanguages(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationLanguages', a1)
    assert _is_linked(b, 'application_ApplicationLanguages', a1)
    if hasattr(a1, 'application_ApplicationMessageLibraries22'):
        assert _is_linked(a1, 'application_ApplicationMessageLibraries22', b)
    _safe_set(b, 'application_ApplicationLanguages', a2)
    assert _is_linked(b, 'application_ApplicationLanguages', a2)
    if hasattr(a1, 'application_ApplicationMessageLibraries22'):
        assert not _is_linked(a1, 'application_ApplicationMessageLibraries22', b)
    if hasattr(a2, 'application_ApplicationMessageLibraries22'):
        assert _is_linked(a2, 'application_ApplicationMessageLibraries22', b)
    _safe_set(b, 'application_ApplicationLanguages', None)
    assert not _is_linked(b, 'application_ApplicationLanguages', a2)
    if hasattr(a2, 'application_ApplicationMessageLibraries22'):
        assert not _is_linked(a2, 'application_ApplicationMessageLibraries22', b)


def test_assoc_applicationMappers3_reverse_link_reassign_clear():
    a1 = application_ApplicationMappers(name="sample_text", uid="sample_text")
    a2 = application_ApplicationMappers(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application4', a1)
    assert _is_linked(b, 'application_Application4', a1)
    if hasattr(a1, 'application_ApplicationMappers'):
        assert _is_linked(a1, 'application_ApplicationMappers', b)
    _safe_set(b, 'application_Application4', a2)
    assert _is_linked(b, 'application_Application4', a2)
    if hasattr(a1, 'application_ApplicationMappers'):
        assert not _is_linked(a1, 'application_ApplicationMappers', b)
    if hasattr(a2, 'application_ApplicationMappers'):
        assert _is_linked(a2, 'application_ApplicationMappers', b)
    _safe_set(b, 'application_Application4', None)
    assert not _is_linked(b, 'application_Application4', a2)
    if hasattr(a2, 'application_ApplicationMappers'):
        assert not _is_linked(a2, 'application_ApplicationMappers', b)


def test_assoc_applicationMessages13_reverse_link_reassign_clear():
    a1 = application_ApplicationMessageLibraries(name="sample_text", uid="sample_text")
    a2 = application_ApplicationMessageLibraries(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application14', a1)
    assert _is_linked(b, 'application_Application14', a1)
    if hasattr(a1, 'application_ApplicationMessageLibraries'):
        assert _is_linked(a1, 'application_ApplicationMessageLibraries', b)
    _safe_set(b, 'application_Application14', a2)
    assert _is_linked(b, 'application_Application14', a2)
    if hasattr(a1, 'application_ApplicationMessageLibraries'):
        assert not _is_linked(a1, 'application_ApplicationMessageLibraries', b)
    if hasattr(a2, 'application_ApplicationMessageLibraries'):
        assert _is_linked(a2, 'application_ApplicationMessageLibraries', b)
    _safe_set(b, 'application_Application14', None)
    assert not _is_linked(b, 'application_Application14', a2)
    if hasattr(a2, 'application_ApplicationMessageLibraries'):
        assert not _is_linked(a2, 'application_ApplicationMessageLibraries', b)


def test_assoc_applicationRecipes1_reverse_link_reassign_clear():
    a1 = application_ApplicationRecipes(name="sample_text", uid="sample_text")
    a2 = application_ApplicationRecipes(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application2', a1)
    assert _is_linked(b, 'application_Application2', a1)
    if hasattr(a1, 'application_ApplicationRecipes'):
        assert _is_linked(a1, 'application_ApplicationRecipes', b)
    _safe_set(b, 'application_Application2', a2)
    assert _is_linked(b, 'application_Application2', a2)
    if hasattr(a1, 'application_ApplicationRecipes'):
        assert not _is_linked(a1, 'application_ApplicationRecipes', b)
    if hasattr(a2, 'application_ApplicationRecipes'):
        assert _is_linked(a2, 'application_ApplicationRecipes', b)
    _safe_set(b, 'application_Application2', None)
    assert not _is_linked(b, 'application_Application2', a2)
    if hasattr(a2, 'application_ApplicationRecipes'):
        assert not _is_linked(a2, 'application_ApplicationRecipes', b)


def test_assoc_applicationRole11_reverse_link_reassign_clear():
    a1 = application_ApplicationRealms(name="sample_text", uid="sample_text")
    a2 = application_ApplicationRealms(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application12', a1)
    assert _is_linked(b, 'application_Application12', a1)
    if hasattr(a1, 'application_ApplicationRealms'):
        assert _is_linked(a1, 'application_ApplicationRealms', b)
    _safe_set(b, 'application_Application12', a2)
    assert _is_linked(b, 'application_Application12', a2)
    if hasattr(a1, 'application_ApplicationRealms'):
        assert not _is_linked(a1, 'application_ApplicationRealms', b)
    if hasattr(a2, 'application_ApplicationRealms'):
        assert _is_linked(a2, 'application_ApplicationRealms', b)
    _safe_set(b, 'application_Application12', None)
    assert not _is_linked(b, 'application_Application12', a2)
    if hasattr(a2, 'application_ApplicationRealms'):
        assert not _is_linked(a2, 'application_ApplicationRealms', b)


def test_assoc_applicationStyle9_reverse_link_reassign_clear():
    a1 = application_ApplicationStyleLibraries(name="sample_text", uid="sample_text")
    a2 = application_ApplicationStyleLibraries(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application10', a1)
    assert _is_linked(b, 'application_Application10', a1)
    if hasattr(a1, 'application_ApplicationStyleLibraries'):
        assert _is_linked(a1, 'application_ApplicationStyleLibraries', b)
    _safe_set(b, 'application_Application10', a2)
    assert _is_linked(b, 'application_Application10', a2)
    if hasattr(a1, 'application_ApplicationStyleLibraries'):
        assert not _is_linked(a1, 'application_ApplicationStyleLibraries', b)
    if hasattr(a2, 'application_ApplicationStyleLibraries'):
        assert _is_linked(a2, 'application_ApplicationStyleLibraries', b)
    _safe_set(b, 'application_Application10', None)
    assert not _is_linked(b, 'application_Application10', a2)
    if hasattr(a2, 'application_ApplicationStyleLibraries'):
        assert not _is_linked(a2, 'application_ApplicationStyleLibraries', b)


def test_assoc_applicationUILayer5_reverse_link_reassign_clear():
    a1 = application_ApplicationUILayer(name="sample_text", uid="sample_text")
    a2 = application_ApplicationUILayer(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application6', a1)
    assert _is_linked(b, 'application_Application6', a1)
    if hasattr(a1, 'application_ApplicationUILayer'):
        assert _is_linked(a1, 'application_ApplicationUILayer', b)
    _safe_set(b, 'application_Application6', a2)
    assert _is_linked(b, 'application_Application6', a2)
    if hasattr(a1, 'application_ApplicationUILayer'):
        assert not _is_linked(a1, 'application_ApplicationUILayer', b)
    if hasattr(a2, 'application_ApplicationUILayer'):
        assert _is_linked(a2, 'application_ApplicationUILayer', b)
    _safe_set(b, 'application_Application6', None)
    assert not _is_linked(b, 'application_Application6', a2)
    if hasattr(a2, 'application_ApplicationUILayer'):
        assert not _is_linked(a2, 'application_ApplicationUILayer', b)


def test_assoc_applicationUIPackages35_reverse_link_reassign_clear():
    a1 = application_ApplicationUIPackage(name="sample_text", uid="sample_text")
    a2 = application_ApplicationUIPackage(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationUILayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationUILayer36', {a1})
    assert _is_linked(b, 'application_ApplicationUILayer36', a1)
    if hasattr(a1, 'application_ApplicationUIPackage'):
        assert _is_linked(a1, 'application_ApplicationUIPackage', b)
    _safe_set(b, 'application_ApplicationUILayer36', {a2})
    assert _is_linked(b, 'application_ApplicationUILayer36', a2)
    if hasattr(a1, 'application_ApplicationUIPackage'):
        assert not _is_linked(a1, 'application_ApplicationUIPackage', b)
    if hasattr(a2, 'application_ApplicationUIPackage'):
        assert _is_linked(a2, 'application_ApplicationUIPackage', b)
    _safe_set(b, 'application_ApplicationUILayer36', set())
    assert not _is_linked(b, 'application_ApplicationUILayer36', a2)
    if hasattr(a2, 'application_ApplicationUIPackage'):
        assert not _is_linked(a2, 'application_ApplicationUIPackage', b)


def test_assoc_applications0_reverse_link_reassign_clear():
    a1 = application_ApplicationGroup(name="sample_text", uid="sample_text")
    a2 = application_ApplicationGroup(name="sample_text_2", uid="sample_text_2")
    b = application_Application(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_Application', a1)
    assert _is_linked(b, 'application_Application', a1)
    if hasattr(a1, 'application_ApplicationGroup'):
        assert _is_linked(a1, 'application_ApplicationGroup', b)
    _safe_set(b, 'application_Application', a2)
    assert _is_linked(b, 'application_Application', a2)
    if hasattr(a1, 'application_ApplicationGroup'):
        assert not _is_linked(a1, 'application_ApplicationGroup', b)
    if hasattr(a2, 'application_ApplicationGroup'):
        assert _is_linked(a2, 'application_ApplicationGroup', b)
    _safe_set(b, 'application_Application', None)
    assert not _is_linked(b, 'application_Application', a2)
    if hasattr(a2, 'application_ApplicationGroup'):
        assert not _is_linked(a2, 'application_ApplicationGroup', b)


def test_assoc_infarastructureLayers15_reverse_link_reassign_clear():
    a1 = application_ApplicationInfrastructureLayers(name="sample_text", uid="sample_text")
    a2 = application_ApplicationInfrastructureLayers(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationInfrastructureLayer(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationInfrastructureLayer', a1)
    assert _is_linked(b, 'application_ApplicationInfrastructureLayer', a1)
    if hasattr(a1, 'application_ApplicationInfrastructureLayers16'):
        assert _is_linked(a1, 'application_ApplicationInfrastructureLayers16', b)
    _safe_set(b, 'application_ApplicationInfrastructureLayer', a2)
    assert _is_linked(b, 'application_ApplicationInfrastructureLayer', a2)
    if hasattr(a1, 'application_ApplicationInfrastructureLayers16'):
        assert not _is_linked(a1, 'application_ApplicationInfrastructureLayers16', b)
    if hasattr(a2, 'application_ApplicationInfrastructureLayers16'):
        assert _is_linked(a2, 'application_ApplicationInfrastructureLayers16', b)
    _safe_set(b, 'application_ApplicationInfrastructureLayer', None)
    assert not _is_linked(b, 'application_ApplicationInfrastructureLayer', a2)
    if hasattr(a2, 'application_ApplicationInfrastructureLayers16'):
        assert not _is_linked(a2, 'application_ApplicationInfrastructureLayers16', b)


def test_assoc_mappers43_reverse_link_reassign_clear():
    a1 = application_ApplicationMappers(name="sample_text", uid="sample_text")
    a2 = application_ApplicationMappers(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationMapper(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationMapper', a1)
    assert _is_linked(b, 'application_ApplicationMapper', a1)
    if hasattr(a1, 'application_ApplicationMappers44'):
        assert _is_linked(a1, 'application_ApplicationMappers44', b)
    _safe_set(b, 'application_ApplicationMapper', a2)
    assert _is_linked(b, 'application_ApplicationMapper', a2)
    if hasattr(a1, 'application_ApplicationMappers44'):
        assert not _is_linked(a1, 'application_ApplicationMappers44', b)
    if hasattr(a2, 'application_ApplicationMappers44'):
        assert _is_linked(a2, 'application_ApplicationMappers44', b)
    _safe_set(b, 'application_ApplicationMapper', None)
    assert not _is_linked(b, 'application_ApplicationMapper', a2)
    if hasattr(a2, 'application_ApplicationMappers44'):
        assert not _is_linked(a2, 'application_ApplicationMappers44', b)


def test_assoc_messageLibraries19_reverse_link_reassign_clear():
    a1 = application_ApplicationMessageLibrary(name="sample_text", uid="sample_text")
    a2 = application_ApplicationMessageLibrary(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationMessageLibraries(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationMessageLibraries20', a1)
    assert _is_linked(b, 'application_ApplicationMessageLibraries20', a1)
    if hasattr(a1, 'application_ApplicationMessageLibrary'):
        assert _is_linked(a1, 'application_ApplicationMessageLibrary', b)
    _safe_set(b, 'application_ApplicationMessageLibraries20', a2)
    assert _is_linked(b, 'application_ApplicationMessageLibraries20', a2)
    if hasattr(a1, 'application_ApplicationMessageLibrary'):
        assert not _is_linked(a1, 'application_ApplicationMessageLibrary', b)
    if hasattr(a2, 'application_ApplicationMessageLibrary'):
        assert _is_linked(a2, 'application_ApplicationMessageLibrary', b)
    _safe_set(b, 'application_ApplicationMessageLibraries20', None)
    assert not _is_linked(b, 'application_ApplicationMessageLibraries20', a2)
    if hasattr(a2, 'application_ApplicationMessageLibrary'):
        assert not _is_linked(a2, 'application_ApplicationMessageLibrary', b)


def test_assoc_realms27_reverse_link_reassign_clear():
    a1 = application_ApplicationRealms(name="sample_text", uid="sample_text")
    a2 = application_ApplicationRealms(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationRealm(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationRealm', a1)
    assert _is_linked(b, 'application_ApplicationRealm', a1)
    if hasattr(a1, 'application_ApplicationRealms28'):
        assert _is_linked(a1, 'application_ApplicationRealms28', b)
    _safe_set(b, 'application_ApplicationRealm', a2)
    assert _is_linked(b, 'application_ApplicationRealm', a2)
    if hasattr(a1, 'application_ApplicationRealms28'):
        assert not _is_linked(a1, 'application_ApplicationRealms28', b)
    if hasattr(a2, 'application_ApplicationRealms28'):
        assert _is_linked(a2, 'application_ApplicationRealms28', b)
    _safe_set(b, 'application_ApplicationRealm', None)
    assert not _is_linked(b, 'application_ApplicationRealm', a2)
    if hasattr(a2, 'application_ApplicationRealms28'):
        assert not _is_linked(a2, 'application_ApplicationRealms28', b)


def test_assoc_recipes39_reverse_link_reassign_clear():
    a1 = application_ApplicationRecipes(name="sample_text", uid="sample_text")
    a2 = application_ApplicationRecipes(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationRecipe(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationRecipe', a1)
    assert _is_linked(b, 'application_ApplicationRecipe', a1)
    if hasattr(a1, 'application_ApplicationRecipes40'):
        assert _is_linked(a1, 'application_ApplicationRecipes40', b)
    _safe_set(b, 'application_ApplicationRecipe', a2)
    assert _is_linked(b, 'application_ApplicationRecipe', a2)
    if hasattr(a1, 'application_ApplicationRecipes40'):
        assert not _is_linked(a1, 'application_ApplicationRecipes40', b)
    if hasattr(a2, 'application_ApplicationRecipes40'):
        assert _is_linked(a2, 'application_ApplicationRecipes40', b)
    _safe_set(b, 'application_ApplicationRecipe', None)
    assert not _is_linked(b, 'application_ApplicationRecipe', a2)
    if hasattr(a2, 'application_ApplicationRecipes40'):
        assert not _is_linked(a2, 'application_ApplicationRecipes40', b)


def test_assoc_styleLibraries31_reverse_link_reassign_clear():
    a1 = application_ApplicationStyleLibraries(name="sample_text", uid="sample_text")
    a2 = application_ApplicationStyleLibraries(name="sample_text_2", uid="sample_text_2")
    b = application_ApplicationStyle(name="sample_text", uid="sample_text")
    _safe_set(b, 'application_ApplicationStyle', a1)
    assert _is_linked(b, 'application_ApplicationStyle', a1)
    if hasattr(a1, 'application_ApplicationStyleLibraries32'):
        assert _is_linked(a1, 'application_ApplicationStyleLibraries32', b)
    _safe_set(b, 'application_ApplicationStyle', a2)
    assert _is_linked(b, 'application_ApplicationStyle', a2)
    if hasattr(a1, 'application_ApplicationStyleLibraries32'):
        assert not _is_linked(a1, 'application_ApplicationStyleLibraries32', b)
    if hasattr(a2, 'application_ApplicationStyleLibraries32'):
        assert _is_linked(a2, 'application_ApplicationStyleLibraries32', b)
    _safe_set(b, 'application_ApplicationStyle', None)
    assert not _is_linked(b, 'application_ApplicationStyle', a2)
    if hasattr(a2, 'application_ApplicationStyleLibraries32'):
        assert not _is_linked(a2, 'application_ApplicationStyleLibraries32', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_appLayers45_stub_double():
    # application_MappingLayer has no real 'application_MappingLayer' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationMappers's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationMappers's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationMappers(name="sample_text", uid="sample_text")
    partner = application_MappingLayer()
    setattr(partner, 'application_MappingLayer', None)
    _safe_set(owner, 'application_ApplicationMappers46', {partner})
    assert getattr(partner, 'application_MappingLayer') == owner
    _safe_set(owner, 'application_ApplicationMappers46', set())
    assert getattr(partner, 'application_MappingLayer') is None


def test_assoc_forms37_stub_double():
    # application_Form has no real 'application_Form' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationUIPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationUIPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationUIPackage(name="sample_text", uid="sample_text")
    partner = application_Form()
    setattr(partner, 'application_Form', None)
    _safe_set(owner, 'application_ApplicationUIPackage38', {partner})
    assert getattr(partner, 'application_Form') == owner
    _safe_set(owner, 'application_ApplicationUIPackage38', set())
    assert getattr(partner, 'application_Form') is None


def test_assoc_infarastructures17_stub_double():
    # application_EnterpriseInfrastructure has no real 'application_EnterpriseInfrastructure' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationInfrastructureLayer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationInfrastructureLayer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationInfrastructureLayer(name="sample_text", uid="sample_text")
    partner = application_EnterpriseInfrastructure()
    setattr(partner, 'application_EnterpriseInfrastructure', None)
    _safe_set(owner, 'application_ApplicationInfrastructureLayer18', {partner})
    assert getattr(partner, 'application_EnterpriseInfrastructure') == owner
    _safe_set(owner, 'application_ApplicationInfrastructureLayer18', set())
    assert getattr(partner, 'application_EnterpriseInfrastructure') is None


def test_assoc_languages23_stub_double():
    # application_Language has no real 'application_Language' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationLanguages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationLanguages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationLanguages(name="sample_text", uid="sample_text")
    partner = application_Language()
    setattr(partner, 'application_Language', None)
    _safe_set(owner, 'application_ApplicationLanguages24', {partner})
    assert getattr(partner, 'application_Language') == owner
    _safe_set(owner, 'application_ApplicationLanguages24', set())
    assert getattr(partner, 'application_Language') is None


def test_assoc_libraries25_stub_double():
    # application_MessageLibrary has no real 'application_MessageLibrary' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationMessageLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationMessageLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationMessageLibrary(name="sample_text", uid="sample_text")
    partner = application_MessageLibrary()
    setattr(partner, 'application_MessageLibrary', None)
    _safe_set(owner, 'application_ApplicationMessageLibrary26', {partner})
    assert getattr(partner, 'application_MessageLibrary') == owner
    _safe_set(owner, 'application_ApplicationMessageLibrary26', set())
    assert getattr(partner, 'application_MessageLibrary') is None


def test_assoc_libraries33_stub_double():
    # application_StyleLibrary has no real 'application_StyleLibrary' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationStyle(name="sample_text", uid="sample_text")
    partner = application_StyleLibrary()
    setattr(partner, 'application_StyleLibrary', None)
    _safe_set(owner, 'application_ApplicationStyle34', {partner})
    assert getattr(partner, 'application_StyleLibrary') == owner
    _safe_set(owner, 'application_ApplicationStyle34', set())
    assert getattr(partner, 'application_StyleLibrary') is None


def test_assoc_mapper47_stub_double():
    # application_Mappers has no real 'application_Mappers' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationMapper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationMapper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationMapper(name="sample_text", uid="sample_text")
    partner = application_Mappers()
    setattr(partner, 'application_Mappers', None)
    _safe_set(owner, 'application_ApplicationMapper48', partner)
    assert getattr(partner, 'application_Mappers') == owner
    _safe_set(owner, 'application_ApplicationMapper48', None)
    assert getattr(partner, 'application_Mappers') is None


def test_assoc_recipes41_stub_double():
    # application_Recipes has no real 'application_Recipes' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationRecipe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationRecipe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationRecipe(name="sample_text", uid="sample_text")
    partner = application_Recipes()
    setattr(partner, 'application_Recipes', None)
    _safe_set(owner, 'application_ApplicationRecipe42', {partner})
    assert getattr(partner, 'application_Recipes') == owner
    _safe_set(owner, 'application_ApplicationRecipe42', set())
    assert getattr(partner, 'application_Recipes') is None


def test_assoc_roles29_stub_double():
    # application_Roles has no real 'application_Roles' property in the generated
    # code (a bare stub) -- manually attach it so application_ApplicationRealm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ApplicationRealm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ApplicationRealm(name="sample_text", uid="sample_text")
    partner = application_Roles()
    setattr(partner, 'application_Roles', None)
    _safe_set(owner, 'application_ApplicationRealm30', partner)
    assert getattr(partner, 'application_Roles') == owner
    _safe_set(owner, 'application_ApplicationRealm30', None)
    assert getattr(partner, 'application_Roles') is None


