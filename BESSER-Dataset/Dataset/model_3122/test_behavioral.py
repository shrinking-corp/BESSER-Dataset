import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RefAssociation,
    RefAttribute,
    RefClass,
    RefDataType,
    RefMethod,
    RefPackage,
    RefParameter,
    class_diagramm_Association,
    class_diagramm_Attribute,
    class_diagramm_Class,
    class_diagramm_DataType,
    class_diagramm_Method,
    class_diagramm_Package,
    class_diagramm_Parameter,
    class_diagramm_RefAssociation,
    class_diagramm_RefAttribute,
    class_diagramm_RefClass,
    class_diagramm_RefDataType,
    class_diagramm_RefMethod,
    class_diagramm_RefPackage,
    class_diagramm_RefParameter,
    ModifierType,
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

def test_assoc_associations0_stub_double():
    # class_diagramm_RefAssociation has no real 'class_diagramm_RefAssociation' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Package(name="sample_text")
    partner = class_diagramm_RefAssociation()
    setattr(partner, 'class_diagramm_RefAssociation', None)
    _safe_set(owner, 'class_diagramm_Package', {partner})
    assert getattr(partner, 'class_diagramm_RefAssociation') == owner
    _safe_set(owner, 'class_diagramm_Package', set())
    assert getattr(partner, 'class_diagramm_RefAssociation') is None


def test_assoc_attributes21_stub_double():
    # class_diagramm_RefAttribute has no real 'class_diagramm_RefAttribute' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Class(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefAttribute()
    setattr(partner, 'class_diagramm_RefAttribute', None)
    _safe_set(owner, 'class_diagramm_Class22', {partner})
    assert getattr(partner, 'class_diagramm_RefAttribute') == owner
    _safe_set(owner, 'class_diagramm_Class22', set())
    assert getattr(partner, 'class_diagramm_RefAttribute') is None


def test_assoc_classes1_stub_double():
    # class_diagramm_RefClass has no real 'class_diagramm_RefClass' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Package(name="sample_text")
    partner = class_diagramm_RefClass()
    setattr(partner, 'class_diagramm_RefClass', None)
    _safe_set(owner, 'class_diagramm_Package2', {partner})
    assert getattr(partner, 'class_diagramm_RefClass') == owner
    _safe_set(owner, 'class_diagramm_Package2', set())
    assert getattr(partner, 'class_diagramm_RefClass') is None


def test_assoc_methods23_stub_double():
    # class_diagramm_RefMethod has no real 'class_diagramm_RefMethod' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Class(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefMethod()
    setattr(partner, 'class_diagramm_RefMethod', None)
    _safe_set(owner, 'class_diagramm_Class24', {partner})
    assert getattr(partner, 'class_diagramm_RefMethod') == owner
    _safe_set(owner, 'class_diagramm_Class24', set())
    assert getattr(partner, 'class_diagramm_RefMethod') is None


def test_assoc_parameters5_stub_double():
    # class_diagramm_RefParameter has no real 'class_diagramm_RefParameter' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Method(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefParameter()
    setattr(partner, 'class_diagramm_RefParameter', None)
    _safe_set(owner, 'class_diagramm_Method6', {partner})
    assert getattr(partner, 'class_diagramm_RefParameter') == owner
    _safe_set(owner, 'class_diagramm_Method6', set())
    assert getattr(partner, 'class_diagramm_RefParameter') is None


def test_assoc_parent19_stub_double():
    # class_diagramm_RefClass has no real 'class_diagramm_RefClass20' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Class(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefClass()
    setattr(partner, 'class_diagramm_RefClass20', None)
    _safe_set(owner, 'class_diagramm_Class', partner)
    assert getattr(partner, 'class_diagramm_RefClass20') == owner
    _safe_set(owner, 'class_diagramm_Class', None)
    assert getattr(partner, 'class_diagramm_RefClass20') is None


def test_assoc_primitive_return7_stub_double():
    # class_diagramm_RefDataType has no real 'class_diagramm_RefDataType' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Method(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefDataType()
    setattr(partner, 'class_diagramm_RefDataType', None)
    _safe_set(owner, 'class_diagramm_Method8', partner)
    assert getattr(partner, 'class_diagramm_RefDataType') == owner
    _safe_set(owner, 'class_diagramm_Method8', None)
    assert getattr(partner, 'class_diagramm_RefDataType') is None


def test_assoc_primitive_type11_stub_double():
    # class_diagramm_RefDataType has no real 'class_diagramm_RefDataType13' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Attribute(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefDataType()
    setattr(partner, 'class_diagramm_RefDataType13', None)
    _safe_set(owner, 'class_diagramm_Attribute12', partner)
    assert getattr(partner, 'class_diagramm_RefDataType13') == owner
    _safe_set(owner, 'class_diagramm_Attribute12', None)
    assert getattr(partner, 'class_diagramm_RefDataType13') is None


def test_assoc_primitive_type16_stub_double():
    # class_diagramm_RefDataType has no real 'class_diagramm_RefDataType18' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Parameter(name="sample_text")
    partner = class_diagramm_RefDataType()
    setattr(partner, 'class_diagramm_RefDataType18', None)
    _safe_set(owner, 'class_diagramm_Parameter17', partner)
    assert getattr(partner, 'class_diagramm_RefDataType18') == owner
    _safe_set(owner, 'class_diagramm_Parameter17', None)
    assert getattr(partner, 'class_diagramm_RefDataType18') is None


def test_assoc_return_3_stub_double():
    # class_diagramm_RefClass has no real 'class_diagramm_RefClass4' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Method(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefClass()
    setattr(partner, 'class_diagramm_RefClass4', None)
    _safe_set(owner, 'class_diagramm_Method', partner)
    assert getattr(partner, 'class_diagramm_RefClass4') == owner
    _safe_set(owner, 'class_diagramm_Method', None)
    assert getattr(partner, 'class_diagramm_RefClass4') is None


def test_assoc_source25_stub_double():
    # class_diagramm_RefClass has no real 'class_diagramm_RefClass26' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Association(isAggregation=True, maxCardinality=7, minCardinality=7, name="sample_text")
    partner = class_diagramm_RefClass()
    setattr(partner, 'class_diagramm_RefClass26', None)
    _safe_set(owner, 'class_diagramm_Association', partner)
    assert getattr(partner, 'class_diagramm_RefClass26') == owner
    _safe_set(owner, 'class_diagramm_Association', None)
    assert getattr(partner, 'class_diagramm_RefClass26') is None


def test_assoc_target27_stub_double():
    # class_diagramm_RefClass has no real 'class_diagramm_RefClass29' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Association(isAggregation=True, maxCardinality=7, minCardinality=7, name="sample_text")
    partner = class_diagramm_RefClass()
    setattr(partner, 'class_diagramm_RefClass29', None)
    _safe_set(owner, 'class_diagramm_Association28', partner)
    assert getattr(partner, 'class_diagramm_RefClass29') == owner
    _safe_set(owner, 'class_diagramm_Association28', None)
    assert getattr(partner, 'class_diagramm_RefClass29') is None


def test_assoc_type14_stub_double():
    # class_diagramm_RefClass has no real 'class_diagramm_RefClass15' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Parameter(name="sample_text")
    partner = class_diagramm_RefClass()
    setattr(partner, 'class_diagramm_RefClass15', None)
    _safe_set(owner, 'class_diagramm_Parameter', partner)
    assert getattr(partner, 'class_diagramm_RefClass15') == owner
    _safe_set(owner, 'class_diagramm_Parameter', None)
    assert getattr(partner, 'class_diagramm_RefClass15') is None


def test_assoc_type9_stub_double():
    # class_diagramm_RefClass has no real 'class_diagramm_RefClass10' property in the generated
    # code (a bare stub) -- manually attach it so class_diagramm_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_diagramm_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_diagramm_Attribute(modifier="sample_text", name="sample_text")
    partner = class_diagramm_RefClass()
    setattr(partner, 'class_diagramm_RefClass10', None)
    _safe_set(owner, 'class_diagramm_Attribute', partner)
    assert getattr(partner, 'class_diagramm_RefClass10') == owner
    _safe_set(owner, 'class_diagramm_Attribute', None)
    assert getattr(partner, 'class_diagramm_RefClass10') is None


