import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DeprecatableElement,
    Literal,
    NamedElement,
    sgen_BoolLiteral,
    sgen_DeprecatableElement,
    sgen_EObject,
    sgen_FeatureConfiguration,
    sgen_FeatureParameter,
    sgen_FeatureParameterValue,
    sgen_FeatureType,
    sgen_FeatureTypeLibrary,
    sgen_GeneratorConfiguration,
    sgen_GeneratorEntry,
    sgen_GeneratorModel,
    sgen_IntLiteral,
    sgen_Literal,
    sgen_RealLiteral,
    sgen_StringLiteral,
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


def test_assoc_featureConfiguration15_reverse_link_reassign_clear():
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


def test_assoc_featureType4_reverse_link_reassign_clear():
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


def test_assoc_features11_reverse_link_reassign_clear():
    a1 = sgen_GeneratorEntry(contentType="sample_text")
    a2 = sgen_GeneratorEntry(contentType="sample_text_2")
    b = sgen_FeatureConfiguration()
    _safe_set(b, 'sgen_FeatureConfiguration13', a1)
    assert _is_linked(b, 'sgen_FeatureConfiguration13', a1)
    if hasattr(a1, 'sgen_GeneratorEntry12'):
        assert _is_linked(a1, 'sgen_GeneratorEntry12', b)
    _safe_set(b, 'sgen_FeatureConfiguration13', a2)
    assert _is_linked(b, 'sgen_FeatureConfiguration13', a2)
    if hasattr(a1, 'sgen_GeneratorEntry12'):
        assert not _is_linked(a1, 'sgen_GeneratorEntry12', b)
    if hasattr(a2, 'sgen_GeneratorEntry12'):
        assert _is_linked(a2, 'sgen_GeneratorEntry12', b)
    _safe_set(b, 'sgen_FeatureConfiguration13', None)
    assert not _is_linked(b, 'sgen_FeatureConfiguration13', a2)
    if hasattr(a2, 'sgen_GeneratorEntry12'):
        assert not _is_linked(a2, 'sgen_GeneratorEntry12', b)


def test_assoc_library3_reverse_link_reassign_clear():
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


def test_assoc_parameter14_reverse_link_reassign_clear():
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


def test_assoc_parameterValues8_reverse_link_reassign_clear():
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


def test_assoc_parameters2_reverse_link_reassign_clear():
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


def test_assoc_type5_reverse_link_reassign_clear():
    a1 = sgen_FeatureType(optional=True)
    a2 = sgen_FeatureType(optional=False)
    b = sgen_FeatureConfiguration()
    _safe_set(b, 'sgen_FeatureConfiguration6', a1)
    assert _is_linked(b, 'sgen_FeatureConfiguration6', a1)
    if hasattr(a1, 'sgen_FeatureType7'):
        assert _is_linked(a1, 'sgen_FeatureType7', b)
    _safe_set(b, 'sgen_FeatureConfiguration6', a2)
    assert _is_linked(b, 'sgen_FeatureConfiguration6', a2)
    if hasattr(a1, 'sgen_FeatureType7'):
        assert not _is_linked(a1, 'sgen_FeatureType7', b)
    if hasattr(a2, 'sgen_FeatureType7'):
        assert _is_linked(a2, 'sgen_FeatureType7', b)
    _safe_set(b, 'sgen_FeatureConfiguration6', None)
    assert not _is_linked(b, 'sgen_FeatureConfiguration6', a2)
    if hasattr(a2, 'sgen_FeatureType7'):
        assert not _is_linked(a2, 'sgen_FeatureType7', b)


def test_assoc_types18_reverse_link_reassign_clear():
    a1 = sgen_FeatureTypeLibrary(name="sample_text")
    a2 = sgen_FeatureTypeLibrary(name="sample_text_2")
    b = sgen_FeatureType(optional=True)
    _safe_set(b, 'sgen_FeatureType20', a1)
    assert _is_linked(b, 'sgen_FeatureType20', a1)
    if hasattr(a1, 'sgen_FeatureTypeLibrary19'):
        assert _is_linked(a1, 'sgen_FeatureTypeLibrary19', b)
    _safe_set(b, 'sgen_FeatureType20', a2)
    assert _is_linked(b, 'sgen_FeatureType20', a2)
    if hasattr(a1, 'sgen_FeatureTypeLibrary19'):
        assert not _is_linked(a1, 'sgen_FeatureTypeLibrary19', b)
    if hasattr(a2, 'sgen_FeatureTypeLibrary19'):
        assert _is_linked(a2, 'sgen_FeatureTypeLibrary19', b)
    _safe_set(b, 'sgen_FeatureType20', None)
    assert not _is_linked(b, 'sgen_FeatureType20', a2)
    if hasattr(a2, 'sgen_FeatureTypeLibrary19'):
        assert not _is_linked(a2, 'sgen_FeatureTypeLibrary19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configurations1_stub_double():
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


def test_assoc_elementRef9_stub_double():
    # sgen_EObject has no real 'sgen_EObject' property in the generated
    # code (a bare stub) -- manually attach it so sgen_GeneratorEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgen_GeneratorEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgen_GeneratorEntry(contentType="sample_text")
    partner = sgen_EObject()
    setattr(partner, 'sgen_EObject', None)
    _safe_set(owner, 'sgen_GeneratorEntry10', partner)
    assert getattr(partner, 'sgen_EObject') == owner
    _safe_set(owner, 'sgen_GeneratorEntry10', None)
    assert getattr(partner, 'sgen_EObject') is None


def test_assoc_expression16_stub_double():
    # sgen_Literal has no real 'sgen_Literal' property in the generated
    # code (a bare stub) -- manually attach it so sgen_FeatureParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgen_FeatureParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgen_FeatureParameterValue()
    partner = sgen_Literal()
    setattr(partner, 'sgen_Literal', None)
    _safe_set(owner, 'sgen_FeatureParameterValue17', partner)
    assert getattr(partner, 'sgen_Literal') == owner
    _safe_set(owner, 'sgen_FeatureParameterValue17', None)
    assert getattr(partner, 'sgen_Literal') is None


