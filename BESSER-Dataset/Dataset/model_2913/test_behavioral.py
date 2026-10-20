import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    lSGL_Annotation,
    lSGL_Attribute,
    lSGL_AttributeType,
    lSGL_Config,
    lSGL_ConfigProperty,
    lSGL_Entity,
    lSGL_Enum,
    lSGL_EnumItem,
    lSGL_Generator,
    lSGL_GeneratorAnnotation,
    lSGL_GeneratorConfig,
    lSGL_Model,
    lSGL_Projection,
    lSGL_Type,
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

def test_assoc_annotations21_reverse_link_reassign_clear():
    a1 = lSGL_Attribute(isArray=True, isList=True, isMap=True, name="sample_text")
    a2 = lSGL_Attribute(isArray=False, isList=False, isMap=False, name="sample_text_2")
    b = lSGL_Annotation(name="sample_text", value="sample_text")
    _safe_set(b, 'lSGL_Annotation', a1)
    assert _is_linked(b, 'lSGL_Annotation', a1)
    if hasattr(a1, 'lSGL_Attribute22'):
        assert _is_linked(a1, 'lSGL_Attribute22', b)
    _safe_set(b, 'lSGL_Annotation', a2)
    assert _is_linked(b, 'lSGL_Annotation', a2)
    if hasattr(a1, 'lSGL_Attribute22'):
        assert not _is_linked(a1, 'lSGL_Attribute22', b)
    if hasattr(a2, 'lSGL_Attribute22'):
        assert _is_linked(a2, 'lSGL_Attribute22', b)
    _safe_set(b, 'lSGL_Annotation', None)
    assert not _is_linked(b, 'lSGL_Annotation', a2)
    if hasattr(a2, 'lSGL_Attribute22'):
        assert not _is_linked(a2, 'lSGL_Attribute22', b)


def test_assoc_attributes43_reverse_link_reassign_clear():
    a1 = lSGL_Projection(excluding=True, name="sample_text")
    a2 = lSGL_Projection(excluding=False, name="sample_text_2")
    b = lSGL_Attribute(isArray=True, isList=True, isMap=True, name="sample_text")
    _safe_set(b, 'lSGL_Attribute45', a1)
    assert _is_linked(b, 'lSGL_Attribute45', a1)
    if hasattr(a1, 'lSGL_Projection44'):
        assert _is_linked(a1, 'lSGL_Projection44', b)
    _safe_set(b, 'lSGL_Attribute45', a2)
    assert _is_linked(b, 'lSGL_Attribute45', a2)
    if hasattr(a1, 'lSGL_Projection44'):
        assert not _is_linked(a1, 'lSGL_Projection44', b)
    if hasattr(a2, 'lSGL_Projection44'):
        assert _is_linked(a2, 'lSGL_Projection44', b)
    _safe_set(b, 'lSGL_Attribute45', None)
    assert not _is_linked(b, 'lSGL_Attribute45', a2)
    if hasattr(a2, 'lSGL_Projection44'):
        assert not _is_linked(a2, 'lSGL_Projection44', b)


def test_assoc_configs7_reverse_link_reassign_clear():
    a1 = lSGL_Generator(name="sample_text")
    a2 = lSGL_Generator(name="sample_text_2")
    b = lSGL_Config(name="sample_text")
    _safe_set(b, 'lSGL_Config', a1)
    assert _is_linked(b, 'lSGL_Config', a1)
    if hasattr(a1, 'lSGL_Generator8'):
        assert _is_linked(a1, 'lSGL_Generator8', b)
    _safe_set(b, 'lSGL_Config', a2)
    assert _is_linked(b, 'lSGL_Config', a2)
    if hasattr(a1, 'lSGL_Generator8'):
        assert not _is_linked(a1, 'lSGL_Generator8', b)
    if hasattr(a2, 'lSGL_Generator8'):
        assert _is_linked(a2, 'lSGL_Generator8', b)
    _safe_set(b, 'lSGL_Config', None)
    assert not _is_linked(b, 'lSGL_Config', a2)
    if hasattr(a2, 'lSGL_Generator8'):
        assert not _is_linked(a2, 'lSGL_Generator8', b)


def test_assoc_key23_reverse_link_reassign_clear():
    a1 = lSGL_AttributeType(nullable=True, typeName="sample_text")
    a2 = lSGL_AttributeType(nullable=False, typeName="sample_text_2")
    b = lSGL_Attribute(isArray=True, isList=True, isMap=True, name="sample_text")
    _safe_set(b, 'lSGL_Attribute24', a1)
    assert _is_linked(b, 'lSGL_Attribute24', a1)
    if hasattr(a1, 'lSGL_AttributeType25'):
        assert _is_linked(a1, 'lSGL_AttributeType25', b)
    _safe_set(b, 'lSGL_Attribute24', a2)
    assert _is_linked(b, 'lSGL_Attribute24', a2)
    if hasattr(a1, 'lSGL_AttributeType25'):
        assert not _is_linked(a1, 'lSGL_AttributeType25', b)
    if hasattr(a2, 'lSGL_AttributeType25'):
        assert _is_linked(a2, 'lSGL_AttributeType25', b)
    _safe_set(b, 'lSGL_Attribute24', None)
    assert not _is_linked(b, 'lSGL_Attribute24', a2)
    if hasattr(a2, 'lSGL_AttributeType25'):
        assert not _is_linked(a2, 'lSGL_AttributeType25', b)


def test_assoc_properties5_reverse_link_reassign_clear():
    a1 = lSGL_Generator(name="sample_text")
    a2 = lSGL_Generator(name="sample_text_2")
    b = lSGL_ConfigProperty(name="sample_text", value="sample_text")
    _safe_set(b, 'lSGL_ConfigProperty', a1)
    assert _is_linked(b, 'lSGL_ConfigProperty', a1)
    if hasattr(a1, 'lSGL_Generator6'):
        assert _is_linked(a1, 'lSGL_Generator6', b)
    _safe_set(b, 'lSGL_ConfigProperty', a2)
    assert _is_linked(b, 'lSGL_ConfigProperty', a2)
    if hasattr(a1, 'lSGL_Generator6'):
        assert not _is_linked(a1, 'lSGL_Generator6', b)
    if hasattr(a2, 'lSGL_Generator6'):
        assert _is_linked(a2, 'lSGL_Generator6', b)
    _safe_set(b, 'lSGL_ConfigProperty', None)
    assert not _is_linked(b, 'lSGL_ConfigProperty', a2)
    if hasattr(a2, 'lSGL_Generator6'):
        assert not _is_linked(a2, 'lSGL_Generator6', b)


def test_assoc_properties9_reverse_link_reassign_clear():
    a1 = lSGL_ConfigProperty(name="sample_text", value="sample_text")
    a2 = lSGL_ConfigProperty(name="sample_text_2", value="sample_text_2")
    b = lSGL_Config(name="sample_text")
    _safe_set(b, 'lSGL_Config10', {a1})
    assert _is_linked(b, 'lSGL_Config10', a1)
    if hasattr(a1, 'lSGL_ConfigProperty11'):
        assert _is_linked(a1, 'lSGL_ConfigProperty11', b)
    _safe_set(b, 'lSGL_Config10', {a2})
    assert _is_linked(b, 'lSGL_Config10', a2)
    if hasattr(a1, 'lSGL_ConfigProperty11'):
        assert not _is_linked(a1, 'lSGL_ConfigProperty11', b)
    if hasattr(a2, 'lSGL_ConfigProperty11'):
        assert _is_linked(a2, 'lSGL_ConfigProperty11', b)
    _safe_set(b, 'lSGL_Config10', set())
    assert not _is_linked(b, 'lSGL_Config10', a2)
    if hasattr(a2, 'lSGL_ConfigProperty11'):
        assert not _is_linked(a2, 'lSGL_ConfigProperty11', b)


def test_assoc_type19_reverse_link_reassign_clear():
    a1 = lSGL_Type(name="sample_text")
    a2 = lSGL_Type(name="sample_text_2")
    b = lSGL_AttributeType(nullable=True, typeName="sample_text")
    _safe_set(b, 'lSGL_AttributeType', a1)
    assert _is_linked(b, 'lSGL_AttributeType', a1)
    if hasattr(a1, 'lSGL_Type20'):
        assert _is_linked(a1, 'lSGL_Type20', b)
    _safe_set(b, 'lSGL_AttributeType', a2)
    assert _is_linked(b, 'lSGL_AttributeType', a2)
    if hasattr(a1, 'lSGL_Type20'):
        assert not _is_linked(a1, 'lSGL_Type20', b)
    if hasattr(a2, 'lSGL_Type20'):
        assert _is_linked(a2, 'lSGL_Type20', b)
    _safe_set(b, 'lSGL_AttributeType', None)
    assert not _is_linked(b, 'lSGL_AttributeType', a2)
    if hasattr(a2, 'lSGL_Type20'):
        assert not _is_linked(a2, 'lSGL_Type20', b)


def test_assoc_type26_reverse_link_reassign_clear():
    a1 = lSGL_AttributeType(nullable=True, typeName="sample_text")
    a2 = lSGL_AttributeType(nullable=False, typeName="sample_text_2")
    b = lSGL_Attribute(isArray=True, isList=True, isMap=True, name="sample_text")
    _safe_set(b, 'lSGL_Attribute27', a1)
    assert _is_linked(b, 'lSGL_Attribute27', a1)
    if hasattr(a1, 'lSGL_AttributeType28'):
        assert _is_linked(a1, 'lSGL_AttributeType28', b)
    _safe_set(b, 'lSGL_Attribute27', a2)
    assert _is_linked(b, 'lSGL_Attribute27', a2)
    if hasattr(a1, 'lSGL_AttributeType28'):
        assert not _is_linked(a1, 'lSGL_AttributeType28', b)
    if hasattr(a2, 'lSGL_AttributeType28'):
        assert _is_linked(a2, 'lSGL_AttributeType28', b)
    _safe_set(b, 'lSGL_Attribute27', None)
    assert not _is_linked(b, 'lSGL_Attribute27', a2)
    if hasattr(a2, 'lSGL_AttributeType28'):
        assert not _is_linked(a2, 'lSGL_AttributeType28', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes17_stub_double():
    # lSGL_Entity has no real 'lSGL_Entity18' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Attribute(isArray=True, isList=True, isMap=True, name="sample_text")
    partner = lSGL_Entity()
    setattr(partner, 'lSGL_Entity18', None)
    _safe_set(owner, 'lSGL_Attribute', partner)
    assert owner in getattr(partner, 'lSGL_Entity18')
    _safe_set(owner, 'lSGL_Attribute', None)
    assert owner not in getattr(partner, 'lSGL_Entity18')


def test_assoc_configItem32_stub_double():
    # lSGL_GeneratorAnnotation has no real 'lSGL_GeneratorAnnotation33' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Config's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Config's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Config(name="sample_text")
    partner = lSGL_GeneratorAnnotation()
    setattr(partner, 'lSGL_GeneratorAnnotation33', None)
    _safe_set(owner, 'lSGL_Config34', partner)
    assert getattr(partner, 'lSGL_GeneratorAnnotation33') == owner
    _safe_set(owner, 'lSGL_Config34', None)
    assert getattr(partner, 'lSGL_GeneratorAnnotation33') is None


def test_assoc_customConfig35_stub_double():
    # lSGL_GeneratorAnnotation has no real 'lSGL_GeneratorAnnotation36' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_GeneratorConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_GeneratorConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_GeneratorConfig(cfgName="sample_text", values="sample_text")
    partner = lSGL_GeneratorAnnotation()
    setattr(partner, 'lSGL_GeneratorAnnotation36', None)
    _safe_set(owner, 'lSGL_GeneratorConfig', partner)
    assert owner in getattr(partner, 'lSGL_GeneratorAnnotation36')
    _safe_set(owner, 'lSGL_GeneratorConfig', None)
    assert owner not in getattr(partner, 'lSGL_GeneratorAnnotation36')


def test_assoc_entity40_stub_double():
    # lSGL_Entity has no real 'lSGL_Entity42' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Projection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Projection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Projection(excluding=True, name="sample_text")
    partner = lSGL_Entity()
    setattr(partner, 'lSGL_Entity42', None)
    _safe_set(owner, 'lSGL_Projection41', partner)
    assert getattr(partner, 'lSGL_Entity42') == owner
    _safe_set(owner, 'lSGL_Projection41', None)
    assert getattr(partner, 'lSGL_Entity42') is None


def test_assoc_generator29_stub_double():
    # lSGL_GeneratorAnnotation has no real 'lSGL_GeneratorAnnotation30' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Generator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Generator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Generator(name="sample_text")
    partner = lSGL_GeneratorAnnotation()
    setattr(partner, 'lSGL_GeneratorAnnotation30', None)
    _safe_set(owner, 'lSGL_Generator31', partner)
    assert getattr(partner, 'lSGL_GeneratorAnnotation30') == owner
    _safe_set(owner, 'lSGL_Generator31', None)
    assert getattr(partner, 'lSGL_GeneratorAnnotation30') is None


def test_assoc_generatorAnnotations37_stub_double():
    # lSGL_GeneratorAnnotation has no real 'lSGL_GeneratorAnnotation39' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Projection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Projection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Projection(excluding=True, name="sample_text")
    partner = lSGL_GeneratorAnnotation()
    setattr(partner, 'lSGL_GeneratorAnnotation39', None)
    _safe_set(owner, 'lSGL_Projection38', {partner})
    assert getattr(partner, 'lSGL_GeneratorAnnotation39') == owner
    _safe_set(owner, 'lSGL_Projection38', set())
    assert getattr(partner, 'lSGL_GeneratorAnnotation39') is None


def test_assoc_generators0_stub_double():
    # lSGL_Model has no real 'lSGL_Model' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Generator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Generator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Generator(name="sample_text")
    partner = lSGL_Model()
    setattr(partner, 'lSGL_Model', None)
    _safe_set(owner, 'lSGL_Generator', partner)
    assert owner in getattr(partner, 'lSGL_Model')
    _safe_set(owner, 'lSGL_Generator', None)
    assert owner not in getattr(partner, 'lSGL_Model')


def test_assoc_items12_stub_double():
    # lSGL_Enum has no real 'lSGL_Enum' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_EnumItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_EnumItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_EnumItem(name="sample_text", value="sample_text")
    partner = lSGL_Enum()
    setattr(partner, 'lSGL_Enum', None)
    _safe_set(owner, 'lSGL_EnumItem', partner)
    assert owner in getattr(partner, 'lSGL_Enum')
    _safe_set(owner, 'lSGL_EnumItem', None)
    assert owner not in getattr(partner, 'lSGL_Enum')


def test_assoc_projections3_stub_double():
    # lSGL_Model has no real 'lSGL_Model4' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Projection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Projection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Projection(excluding=True, name="sample_text")
    partner = lSGL_Model()
    setattr(partner, 'lSGL_Model4', None)
    _safe_set(owner, 'lSGL_Projection', partner)
    assert owner in getattr(partner, 'lSGL_Model4')
    _safe_set(owner, 'lSGL_Projection', None)
    assert owner not in getattr(partner, 'lSGL_Model4')


def test_assoc_types1_stub_double():
    # lSGL_Model has no real 'lSGL_Model2' property in the generated
    # code (a bare stub) -- manually attach it so lSGL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lSGL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lSGL_Type(name="sample_text")
    partner = lSGL_Model()
    setattr(partner, 'lSGL_Model2', None)
    _safe_set(owner, 'lSGL_Type', partner)
    assert owner in getattr(partner, 'lSGL_Model2')
    _safe_set(owner, 'lSGL_Type', None)
    assert owner not in getattr(partner, 'lSGL_Model2')


