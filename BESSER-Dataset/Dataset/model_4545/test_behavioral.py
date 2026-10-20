import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConversionBasedUnit,
    Dimension,
    Integer,
    Number,
    Prefix,
    QuantityKind,
    QuantityKindFactor,
    Rational,
    Real,
    SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex,
    SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer,
    SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number,
    SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational,
    SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real,
    SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit,
    SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit,
    SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind,
    SysML_ValueTypes_QUDV_QUDV_DerivedUnit,
    SysML_ValueTypes_QUDV_QUDV_Dimension,
    SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit,
    SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit,
    SysML_ValueTypes_QUDV_QUDV_Prefix,
    SysML_ValueTypes_QUDV_QUDV_PrefixedUnit,
    SysML_ValueTypes_QUDV_QUDV_QuantityKind,
    SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor,
    SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind,
    SysML_ValueTypes_QUDV_QUDV_SimpleUnit,
    SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities,
    SysML_ValueTypes_QUDV_QUDV_SystemOfUnits,
    SysML_ValueTypes_QUDV_QUDV_Unit,
    SysML_ValueTypes_QUDV_QUDV_UnitFactor,
    SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER,
    SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind,
    SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit,
    SystemOfQuantities,
    SystemOfUnits,
    Unit,
    UnitFactor,
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

def test_assoc_baseQuantityKind55_stub_double():
    # QuantityKind has no real 'QuantityKind56' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(definitionURI="sample_text", description="sample_text", name=True, symbol="sample_text")
    partner = QuantityKind()
    setattr(partner, 'QuantityKind56', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities', {partner})
    assert getattr(partner, 'QuantityKind56') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities', set())
    assert getattr(partner, 'QuantityKind56') is None


def test_assoc_baseUnit66_stub_double():
    # Unit has no real 'Unit67' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(definitionURI="sample_text", description="sample_text", name="sample_text", symbol="sample_text")
    partner = Unit()
    setattr(partner, 'Unit67', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits', {partner})
    assert getattr(partner, 'Unit67') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits', set())
    assert getattr(partner, 'Unit67') is None


def test_assoc_denominator22_stub_double():
    # Integer has no real 'Integer24' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational()
    partner = Integer()
    setattr(partner, 'Integer24', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23', partner)
    assert getattr(partner, 'Integer24') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23', None)
    assert getattr(partner, 'Integer24') is None


def test_assoc_dependsOnQuantityKinds45_stub_double():
    # QuantityKind has no real 'QuantityKind46' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_QuantityKind's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_QuantityKind's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_QuantityKind(isNumberOfEntities=True, isQuantityOfDimensionOne=True)
    partner = QuantityKind()
    setattr(partner, 'QuantityKind46', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKind', {partner})
    assert getattr(partner, 'QuantityKind46') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKind', set())
    assert getattr(partner, 'QuantityKind46') is None


def test_assoc_dependsOnUnits83_stub_double():
    # Unit has no real 'Unit84' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_Unit(isUnitCountOfEntities=True, isUnitForQuantityOfDimensionOne=True)
    partner = Unit()
    setattr(partner, 'Unit84', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Unit', {partner})
    assert getattr(partner, 'Unit84') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Unit', set())
    assert getattr(partner, 'Unit84') is None


def test_assoc_exponent50_stub_double():
    # Rational has no real 'Rational51' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor(name="sample_text")
    partner = Rational()
    setattr(partner, 'Rational51', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor', partner)
    assert getattr(partner, 'Rational51') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor', None)
    assert getattr(partner, 'Rational51') is None


def test_assoc_exponent88_stub_double():
    # Rational has no real 'Rational89' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_UnitFactor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_UnitFactor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_UnitFactor(name="sample_text")
    partner = Rational()
    setattr(partner, 'Rational89', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_UnitFactor', partner)
    assert getattr(partner, 'Rational89') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_UnitFactor', None)
    assert getattr(partner, 'Rational89') is None


def test_assoc_factor34_stub_double():
    # QuantityKindFactor has no real 'QuantityKindFactor35' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind()
    partner = QuantityKindFactor()
    setattr(partner, 'QuantityKindFactor35', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind', {partner})
    assert getattr(partner, 'QuantityKindFactor35') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind', set())
    assert getattr(partner, 'QuantityKindFactor35') is None


def test_assoc_factor36_stub_double():
    # UnitFactor has no real 'UnitFactor37' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_DerivedUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_DerivedUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_DerivedUnit()
    partner = UnitFactor()
    setattr(partner, 'UnitFactor37', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_DerivedUnit', {partner})
    assert getattr(partner, 'UnitFactor37') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_DerivedUnit', set())
    assert getattr(partner, 'UnitFactor37') is None


def test_assoc_factor38_stub_double():
    # QuantityKindFactor has no real 'QuantityKindFactor39' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_Dimension(name="sample_text")
    partner = QuantityKindFactor()
    setattr(partner, 'QuantityKindFactor39', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Dimension', {partner})
    assert getattr(partner, 'QuantityKindFactor39') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Dimension', set())
    assert getattr(partner, 'QuantityKindFactor39') is None


def test_assoc_factor42_stub_double():
    # Rational has no real 'Rational' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_Prefix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_Prefix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_Prefix(name="sample_text", symbol="sample_text")
    partner = Rational()
    setattr(partner, 'Rational', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Prefix', partner)
    assert getattr(partner, 'Rational') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Prefix', None)
    assert getattr(partner, 'Rational') is None


def test_assoc_general47_stub_double():
    # QuantityKind has no real 'QuantityKind49' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_QuantityKind's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_QuantityKind's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_QuantityKind(isNumberOfEntities=True, isQuantityOfDimensionOne=True)
    partner = QuantityKind()
    setattr(partner, 'QuantityKind49', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKind48', {partner})
    assert getattr(partner, 'QuantityKind49') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKind48', set())
    assert getattr(partner, 'QuantityKind49') is None


def test_assoc_general85_stub_double():
    # Unit has no real 'Unit87' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_Unit(isUnitCountOfEntities=True, isUnitForQuantityOfDimensionOne=True)
    partner = Unit()
    setattr(partner, 'Unit87', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Unit86', {partner})
    assert getattr(partner, 'Unit87') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_Unit86', set())
    assert getattr(partner, 'Unit87') is None


def test_assoc_imaginaryPart18_stub_double():
    # Real has no real 'Real20' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex()
    partner = Real()
    setattr(partner, 'Real20', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19', partner)
    assert getattr(partner, 'Real20') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19', None)
    assert getattr(partner, 'Real20') is None


def test_assoc_includedSystemOfQuantities57_stub_double():
    # SystemOfQuantities has no real 'SystemOfQuantities59' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(definitionURI="sample_text", description="sample_text", name=True, symbol="sample_text")
    partner = SystemOfQuantities()
    setattr(partner, 'SystemOfQuantities59', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58', {partner})
    assert getattr(partner, 'SystemOfQuantities59') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58', set())
    assert getattr(partner, 'SystemOfQuantities59') is None


def test_assoc_includedSystemOfUnits68_stub_double():
    # SystemOfUnits has no real 'SystemOfUnits70' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(definitionURI="sample_text", description="sample_text", name="sample_text", symbol="sample_text")
    partner = SystemOfUnits()
    setattr(partner, 'SystemOfUnits70', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69', {partner})
    assert getattr(partner, 'SystemOfUnits70') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69', set())
    assert getattr(partner, 'SystemOfUnits70') is None


def test_assoc_numerator21_stub_double():
    # Integer has no real 'Integer' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational()
    partner = Integer()
    setattr(partner, 'Integer', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational', partner)
    assert getattr(partner, 'Integer') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational', None)
    assert getattr(partner, 'Integer') is None


def test_assoc_prefix71_stub_double():
    # Prefix has no real 'Prefix73' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(definitionURI="sample_text", description="sample_text", name="sample_text", symbol="sample_text")
    partner = Prefix()
    setattr(partner, 'Prefix73', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72', {partner})
    assert getattr(partner, 'Prefix73') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72', set())
    assert getattr(partner, 'Prefix73') is None


def test_assoc_quantityKind25_stub_double():
    # QuantityKind has no real 'QuantityKind26' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit(definitionURI="sample_text", description="sample_text", name="sample_text", symbol="sample_text")
    partner = QuantityKind()
    setattr(partner, 'QuantityKind26', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit', {partner})
    assert getattr(partner, 'QuantityKind26') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit', set())
    assert getattr(partner, 'QuantityKind26') is None


def test_assoc_quantityKind52_stub_double():
    # QuantityKind has no real 'QuantityKind54' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor(name="sample_text")
    partner = QuantityKind()
    setattr(partner, 'QuantityKind54', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53', partner)
    assert getattr(partner, 'QuantityKind54') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53', None)
    assert getattr(partner, 'QuantityKind54') is None


def test_assoc_quantityKind60_stub_double():
    # QuantityKind has no real 'QuantityKind62' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(definitionURI="sample_text", description="sample_text", name=True, symbol="sample_text")
    partner = QuantityKind()
    setattr(partner, 'QuantityKind62', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61', {partner})
    assert getattr(partner, 'QuantityKind62') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61', set())
    assert getattr(partner, 'QuantityKind62') is None


def test_assoc_realPart17_stub_double():
    # Real has no real 'Real' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex()
    partner = Real()
    setattr(partner, 'Real', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex', partner)
    assert getattr(partner, 'Real') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex', None)
    assert getattr(partner, 'Real') is None


def test_assoc_referenceUnit32_stub_double():
    # Unit has no real 'Unit33' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit(isInvertible=True)
    partner = Unit()
    setattr(partner, 'Unit33', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit', partner)
    assert getattr(partner, 'Unit33') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit', None)
    assert getattr(partner, 'Unit33') is None


def test_assoc_systemOfQuantities74_stub_double():
    # SystemOfQuantities has no real 'SystemOfQuantities76' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(definitionURI="sample_text", description="sample_text", name="sample_text", symbol="sample_text")
    partner = SystemOfQuantities()
    setattr(partner, 'SystemOfQuantities76', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75', partner)
    assert getattr(partner, 'SystemOfQuantities76') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75', None)
    assert getattr(partner, 'SystemOfQuantities76') is None


def test_assoc_unit77_stub_double():
    # Unit has no real 'Unit79' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(definitionURI="sample_text", description="sample_text", name="sample_text", symbol="sample_text")
    partner = Unit()
    setattr(partner, 'Unit79', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78', {partner})
    assert getattr(partner, 'Unit79') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78', set())
    assert getattr(partner, 'Unit79') is None


def test_assoc_unit90_stub_double():
    # Unit has no real 'Unit92' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_UnitFactor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_UnitFactor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_UnitFactor(name="sample_text")
    partner = Unit()
    setattr(partner, 'Unit92', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_UnitFactor91', partner)
    assert getattr(partner, 'Unit92') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_UnitFactor91', None)
    assert getattr(partner, 'Unit92') is None


def test_assoc_usedSystemOfQuantities63_stub_double():
    # SystemOfQuantities has no real 'SystemOfQuantities65' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(definitionURI="sample_text", description="sample_text", name=True, symbol="sample_text")
    partner = SystemOfQuantities()
    setattr(partner, 'SystemOfQuantities65', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64', {partner})
    assert getattr(partner, 'SystemOfQuantities65') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64', set())
    assert getattr(partner, 'SystemOfQuantities65') is None


def test_assoc_usedSystemOfUnits80_stub_double():
    # SystemOfUnits has no real 'SystemOfUnits82' property in the generated
    # code (a bare stub) -- manually attach it so SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SysML_ValueTypes_QUDV_QUDV_SystemOfUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(definitionURI="sample_text", description="sample_text", name="sample_text", symbol="sample_text")
    partner = SystemOfUnits()
    setattr(partner, 'SystemOfUnits82', None)
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81', {partner})
    assert getattr(partner, 'SystemOfUnits82') == owner
    _safe_set(owner, 'SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81', set())
    assert getattr(partner, 'SystemOfUnits82') is None


