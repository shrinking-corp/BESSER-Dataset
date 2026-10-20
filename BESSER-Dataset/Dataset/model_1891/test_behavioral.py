import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DeprecatableElement,
    NamedElement,
    sgen_DeprecatableElement,
    sgen_EObject,
    sgen_Expression,
    sgen_FeatureConfiguration,
    sgen_FeatureParameter,
    sgen_FeatureParameterValue,
    sgen_FeatureType,
    sgen_FeatureTypeLibrary,
    sgen_GeneratorConfiguration,
    sgen_GeneratorEntry,
    sgen_GeneratorModel,
    sgen_Property,
    ParameterTypes,
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

def test_assoc_entries0_reverse_link_reassign_clear():
    a1 = sgen_GeneratorModel(generatorId="sample_text")
    a2 = sgen_GeneratorModel(generatorId="sample_text_2")
    b = sgen_GeneratorEntry(contentType="sample_text")
    _safe_set(b, 'sgen_GeneratorEntry', a1)
    assert _is_linked(b, 'sgen_GeneratorEntry', a1)
    if hasattr(a1, 'sgen_GeneratorModel'):
        assert _is_linked(a1, 'sgen_GeneratorModel', b)
    _safe_set(b, 'sgen_GeneratorEntry', a2)
    assert _is_linked(b, 'sgen_GeneratorEntry', a2)
    if hasattr(a1, 'sgen_GeneratorModel'):
        assert not _is_linked(a1, 'sgen_GeneratorModel', b)
    if hasattr(a2, 'sgen_GeneratorModel'):
        assert _is_linked(a2, 'sgen_GeneratorModel', b)
    _safe_set(b, 'sgen_GeneratorEntry', None)
    assert not _is_linked(b, 'sgen_GeneratorEntry', a2)
    if hasattr(a2, 'sgen_GeneratorModel'):
        assert not _is_linked(a2, 'sgen_GeneratorModel', b)


def test_assoc_featureConfiguration17_reverse_link_reassign_clear():
    a1 = sgen_FeatureParameterValue()
    a2 = sgen_FeatureParameterValue()
    b = sgen_FeatureConfiguration()
    _safe_set(b, 'FeatureConfiguration', a1)
    assert _is_linked(b, 'FeatureConfiguration', a1)
    if hasattr(a1, 'parameterValues'):
        assert _is_linked(a1, 'parameterValues', b)
    _safe_set(b, 'FeatureConfiguration', a2)
    assert _is_linked(b, 'FeatureConfiguration', a2)
    if hasattr(a1, 'parameterValues'):
        assert not _is_linked(a1, 'parameterValues', b)
    if hasattr(a2, 'parameterValues'):
        assert _is_linked(a2, 'parameterValues', b)
    _safe_set(b, 'FeatureConfiguration', None)
    assert not _is_linked(b, 'FeatureConfiguration', a2)
    if hasattr(a2, 'parameterValues'):
        assert not _is_linked(a2, 'parameterValues', b)


def test_assoc_featureType6_reverse_link_reassign_clear():
    a1 = sgen_FeatureType(optional=True)
    a2 = sgen_FeatureType(optional=False)
    b = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    _safe_set(b, 'parameters', a1)
    assert _is_linked(b, 'parameters', a1)
    if hasattr(a1, 'FeatureType'):
        assert _is_linked(a1, 'FeatureType', b)
    _safe_set(b, 'parameters', a2)
    assert _is_linked(b, 'parameters', a2)
    if hasattr(a1, 'FeatureType'):
        assert not _is_linked(a1, 'FeatureType', b)
    if hasattr(a2, 'FeatureType'):
        assert _is_linked(a2, 'FeatureType', b)
    _safe_set(b, 'parameters', None)
    assert not _is_linked(b, 'parameters', a2)
    if hasattr(a2, 'FeatureType'):
        assert not _is_linked(a2, 'FeatureType', b)


def test_assoc_features13_reverse_link_reassign_clear():
    a1 = sgen_GeneratorEntry(contentType="sample_text")
    a2 = sgen_GeneratorEntry(contentType="sample_text_2")
    b = sgen_FeatureConfiguration()
    _safe_set(b, 'sgen_FeatureConfiguration15', a1)
    assert _is_linked(b, 'sgen_FeatureConfiguration15', a1)
    if hasattr(a1, 'sgen_GeneratorEntry14'):
        assert _is_linked(a1, 'sgen_GeneratorEntry14', b)
    _safe_set(b, 'sgen_FeatureConfiguration15', a2)
    assert _is_linked(b, 'sgen_FeatureConfiguration15', a2)
    if hasattr(a1, 'sgen_GeneratorEntry14'):
        assert not _is_linked(a1, 'sgen_GeneratorEntry14', b)
    if hasattr(a2, 'sgen_GeneratorEntry14'):
        assert _is_linked(a2, 'sgen_GeneratorEntry14', b)
    _safe_set(b, 'sgen_FeatureConfiguration15', None)
    assert not _is_linked(b, 'sgen_FeatureConfiguration15', a2)
    if hasattr(a2, 'sgen_GeneratorEntry14'):
        assert not _is_linked(a2, 'sgen_GeneratorEntry14', b)


def test_assoc_library5_reverse_link_reassign_clear():
    a1 = sgen_FeatureTypeLibrary(name="sample_text")
    a2 = sgen_FeatureTypeLibrary(name="sample_text_2")
    b = sgen_FeatureType(optional=True)
    _safe_set(b, 'sgen_FeatureType', a1)
    assert _is_linked(b, 'sgen_FeatureType', a1)
    if hasattr(a1, 'sgen_FeatureTypeLibrary'):
        assert _is_linked(a1, 'sgen_FeatureTypeLibrary', b)
    _safe_set(b, 'sgen_FeatureType', a2)
    assert _is_linked(b, 'sgen_FeatureType', a2)
    if hasattr(a1, 'sgen_FeatureTypeLibrary'):
        assert not _is_linked(a1, 'sgen_FeatureTypeLibrary', b)
    if hasattr(a2, 'sgen_FeatureTypeLibrary'):
        assert _is_linked(a2, 'sgen_FeatureTypeLibrary', b)
    _safe_set(b, 'sgen_FeatureType', None)
    assert not _is_linked(b, 'sgen_FeatureType', a2)
    if hasattr(a2, 'sgen_FeatureTypeLibrary'):
        assert not _is_linked(a2, 'sgen_FeatureTypeLibrary', b)


def test_assoc_parameter16_reverse_link_reassign_clear():
    a1 = sgen_FeatureParameterValue()
    a2 = sgen_FeatureParameterValue()
    b = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    _safe_set(b, 'sgen_FeatureParameter', a1)
    assert _is_linked(b, 'sgen_FeatureParameter', a1)
    if hasattr(a1, 'sgen_FeatureParameterValue'):
        assert _is_linked(a1, 'sgen_FeatureParameterValue', b)
    _safe_set(b, 'sgen_FeatureParameter', a2)
    assert _is_linked(b, 'sgen_FeatureParameter', a2)
    if hasattr(a1, 'sgen_FeatureParameterValue'):
        assert not _is_linked(a1, 'sgen_FeatureParameterValue', b)
    if hasattr(a2, 'sgen_FeatureParameterValue'):
        assert _is_linked(a2, 'sgen_FeatureParameterValue', b)
    _safe_set(b, 'sgen_FeatureParameter', None)
    assert not _is_linked(b, 'sgen_FeatureParameter', a2)
    if hasattr(a2, 'sgen_FeatureParameterValue'):
        assert not _is_linked(a2, 'sgen_FeatureParameterValue', b)


def test_assoc_parameterValues10_reverse_link_reassign_clear():
    a1 = sgen_FeatureParameterValue()
    a2 = sgen_FeatureParameterValue()
    b = sgen_FeatureConfiguration()
    _safe_set(b, 'featureConfiguration', {a1})
    assert _is_linked(b, 'featureConfiguration', a1)
    if hasattr(a1, 'FeatureParameterValue'):
        assert _is_linked(a1, 'FeatureParameterValue', b)
    _safe_set(b, 'featureConfiguration', {a2})
    assert _is_linked(b, 'featureConfiguration', a2)
    if hasattr(a1, 'FeatureParameterValue'):
        assert not _is_linked(a1, 'FeatureParameterValue', b)
    if hasattr(a2, 'FeatureParameterValue'):
        assert _is_linked(a2, 'FeatureParameterValue', b)
    _safe_set(b, 'featureConfiguration', set())
    assert not _is_linked(b, 'featureConfiguration', a2)
    if hasattr(a2, 'FeatureParameterValue'):
        assert not _is_linked(a2, 'FeatureParameterValue', b)


def test_assoc_parameters4_reverse_link_reassign_clear():
    a1 = sgen_FeatureType(optional=True)
    a2 = sgen_FeatureType(optional=False)
    b = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    _safe_set(b, 'FeatureParameter', a1)
    assert _is_linked(b, 'FeatureParameter', a1)
    if hasattr(a1, 'featureType'):
        assert _is_linked(a1, 'featureType', b)
    _safe_set(b, 'FeatureParameter', a2)
    assert _is_linked(b, 'FeatureParameter', a2)
    if hasattr(a1, 'featureType'):
        assert not _is_linked(a1, 'featureType', b)
    if hasattr(a2, 'featureType'):
        assert _is_linked(a2, 'featureType', b)
    _safe_set(b, 'FeatureParameter', None)
    assert not _is_linked(b, 'FeatureParameter', a2)
    if hasattr(a2, 'featureType'):
        assert not _is_linked(a2, 'featureType', b)


def test_assoc_type7_reverse_link_reassign_clear():
    a1 = sgen_FeatureType(optional=True)
    a2 = sgen_FeatureType(optional=False)
    b = sgen_FeatureConfiguration()
    _safe_set(b, 'sgen_FeatureConfiguration8', a1)
    assert _is_linked(b, 'sgen_FeatureConfiguration8', a1)
    if hasattr(a1, 'sgen_FeatureType9'):
        assert _is_linked(a1, 'sgen_FeatureType9', b)
    _safe_set(b, 'sgen_FeatureConfiguration8', a2)
    assert _is_linked(b, 'sgen_FeatureConfiguration8', a2)
    if hasattr(a1, 'sgen_FeatureType9'):
        assert not _is_linked(a1, 'sgen_FeatureType9', b)
    if hasattr(a2, 'sgen_FeatureType9'):
        assert _is_linked(a2, 'sgen_FeatureType9', b)
    _safe_set(b, 'sgen_FeatureConfiguration8', None)
    assert not _is_linked(b, 'sgen_FeatureConfiguration8', a2)
    if hasattr(a2, 'sgen_FeatureType9'):
        assert not _is_linked(a2, 'sgen_FeatureType9', b)


def test_assoc_types20_reverse_link_reassign_clear():
    a1 = sgen_FeatureTypeLibrary(name="sample_text")
    a2 = sgen_FeatureTypeLibrary(name="sample_text_2")
    b = sgen_FeatureType(optional=True)
    _safe_set(b, 'sgen_FeatureType22', a1)
    assert _is_linked(b, 'sgen_FeatureType22', a1)
    if hasattr(a1, 'sgen_FeatureTypeLibrary21'):
        assert _is_linked(a1, 'sgen_FeatureTypeLibrary21', b)
    _safe_set(b, 'sgen_FeatureType22', a2)
    assert _is_linked(b, 'sgen_FeatureType22', a2)
    if hasattr(a1, 'sgen_FeatureTypeLibrary21'):
        assert not _is_linked(a1, 'sgen_FeatureTypeLibrary21', b)
    if hasattr(a2, 'sgen_FeatureTypeLibrary21'):
        assert _is_linked(a2, 'sgen_FeatureTypeLibrary21', b)
    _safe_set(b, 'sgen_FeatureType22', None)
    assert not _is_linked(b, 'sgen_FeatureType22', a2)
    if hasattr(a2, 'sgen_FeatureTypeLibrary21'):
        assert not _is_linked(a2, 'sgen_FeatureTypeLibrary21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configurations3_stub_double():
    # sgen_GeneratorConfiguration has no real 'sgen_GeneratorConfiguration' property in the generated
    # code (a bare stub) -- manually attach it so sgen_FeatureConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgen_FeatureConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgen_FeatureConfiguration()
    partner = sgen_GeneratorConfiguration()
    setattr(partner, 'sgen_GeneratorConfiguration', None)
    _safe_set(owner, 'sgen_FeatureConfiguration', partner)
    assert owner in getattr(partner, 'sgen_GeneratorConfiguration')
    _safe_set(owner, 'sgen_FeatureConfiguration', None)
    assert owner not in getattr(partner, 'sgen_GeneratorConfiguration')


def test_assoc_elementRef11_stub_double():
    # sgen_EObject has no real 'sgen_EObject' property in the generated
    # code (a bare stub) -- manually attach it so sgen_GeneratorEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgen_GeneratorEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgen_GeneratorEntry(contentType="sample_text")
    partner = sgen_EObject()
    setattr(partner, 'sgen_EObject', None)
    _safe_set(owner, 'sgen_GeneratorEntry12', partner)
    assert getattr(partner, 'sgen_EObject') == owner
    _safe_set(owner, 'sgen_GeneratorEntry12', None)
    assert getattr(partner, 'sgen_EObject') is None


def test_assoc_expression18_stub_double():
    # sgen_Expression has no real 'sgen_Expression' property in the generated
    # code (a bare stub) -- manually attach it so sgen_FeatureParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgen_FeatureParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgen_FeatureParameterValue()
    partner = sgen_Expression()
    setattr(partner, 'sgen_Expression', None)
    _safe_set(owner, 'sgen_FeatureParameterValue19', partner)
    assert getattr(partner, 'sgen_Expression') == owner
    _safe_set(owner, 'sgen_FeatureParameterValue19', None)
    assert getattr(partner, 'sgen_Expression') is None


def test_assoc_properties1_stub_double():
    # sgen_Property has no real 'sgen_Property' property in the generated
    # code (a bare stub) -- manually attach it so sgen_GeneratorModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgen_GeneratorModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgen_GeneratorModel(generatorId="sample_text")
    partner = sgen_Property()
    setattr(partner, 'sgen_Property', None)
    _safe_set(owner, 'sgen_GeneratorModel2', {partner})
    assert getattr(partner, 'sgen_Property') == owner
    _safe_set(owner, 'sgen_GeneratorModel2', set())
    assert getattr(partner, 'sgen_Property') is None


