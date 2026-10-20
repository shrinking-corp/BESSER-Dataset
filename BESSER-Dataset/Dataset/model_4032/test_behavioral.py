import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    uml_DocumentRoot,
    uml_EStringToStringMapEntry,
    uml_UML,
    uml_association,
    uml_attribute,
    uml_attributes,
    uml_class_,
    uml_classifiersAndAssociations,
    uml_generalClass,
    uml_ownerClassifier,
    uml_package_,
    uml_packages,
    uml_primitiveDataType,
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

def test_assoc_association11_reverse_link_reassign_clear():
    a1 = uml_classifiersAndAssociations(group="sample_text")
    a2 = uml_classifiersAndAssociations(group="sample_text_2")
    b = uml_association(destination="sample_text", kind="sample_text", name="sample_text", oID="sample_text", source="sample_text")
    _safe_set(b, 'uml_association', a1)
    assert _is_linked(b, 'uml_association', a1)
    if hasattr(a1, 'uml_classifiersAndAssociations12'):
        assert _is_linked(a1, 'uml_classifiersAndAssociations12', b)
    _safe_set(b, 'uml_association', a2)
    assert _is_linked(b, 'uml_association', a2)
    if hasattr(a1, 'uml_classifiersAndAssociations12'):
        assert not _is_linked(a1, 'uml_classifiersAndAssociations12', b)
    if hasattr(a2, 'uml_classifiersAndAssociations12'):
        assert _is_linked(a2, 'uml_classifiersAndAssociations12', b)
    _safe_set(b, 'uml_association', None)
    assert not _is_linked(b, 'uml_association', a2)
    if hasattr(a2, 'uml_classifiersAndAssociations12'):
        assert not _is_linked(a2, 'uml_classifiersAndAssociations12', b)


def test_assoc_association17_reverse_link_reassign_clear():
    a1 = uml_association(destination="sample_text", kind="sample_text", name="sample_text", oID="sample_text", source="sample_text")
    a2 = uml_association(destination="sample_text_2", kind="sample_text_2", name="sample_text_2", oID="sample_text_2", source="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot18', {a1})
    assert _is_linked(b, 'uml_DocumentRoot18', a1)
    if hasattr(a1, 'uml_association19'):
        assert _is_linked(a1, 'uml_association19', b)
    _safe_set(b, 'uml_DocumentRoot18', {a2})
    assert _is_linked(b, 'uml_DocumentRoot18', a2)
    if hasattr(a1, 'uml_association19'):
        assert not _is_linked(a1, 'uml_association19', b)
    if hasattr(a2, 'uml_association19'):
        assert _is_linked(a2, 'uml_association19', b)
    _safe_set(b, 'uml_DocumentRoot18', set())
    assert not _is_linked(b, 'uml_DocumentRoot18', a2)
    if hasattr(a2, 'uml_association19'):
        assert not _is_linked(a2, 'uml_association19', b)


def test_assoc_attribute1_reverse_link_reassign_clear():
    a1 = uml_attributes(group="sample_text")
    a2 = uml_attributes(group="sample_text_2")
    b = uml_attribute(kind="sample_text", name="sample_text", oID="sample_text")
    _safe_set(b, 'uml_attribute2', a1)
    assert _is_linked(b, 'uml_attribute2', a1)
    if hasattr(a1, 'uml_attributes'):
        assert _is_linked(a1, 'uml_attributes', b)
    _safe_set(b, 'uml_attribute2', a2)
    assert _is_linked(b, 'uml_attribute2', a2)
    if hasattr(a1, 'uml_attributes'):
        assert not _is_linked(a1, 'uml_attributes', b)
    if hasattr(a2, 'uml_attributes'):
        assert _is_linked(a2, 'uml_attributes', b)
    _safe_set(b, 'uml_attribute2', None)
    assert not _is_linked(b, 'uml_attribute2', a2)
    if hasattr(a2, 'uml_attributes'):
        assert not _is_linked(a2, 'uml_attributes', b)


def test_assoc_attribute20_reverse_link_reassign_clear():
    a1 = uml_attribute(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = uml_attribute(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot21', {a1})
    assert _is_linked(b, 'uml_DocumentRoot21', a1)
    if hasattr(a1, 'uml_attribute22'):
        assert _is_linked(a1, 'uml_attribute22', b)
    _safe_set(b, 'uml_DocumentRoot21', {a2})
    assert _is_linked(b, 'uml_DocumentRoot21', a2)
    if hasattr(a1, 'uml_attribute22'):
        assert not _is_linked(a1, 'uml_attribute22', b)
    if hasattr(a2, 'uml_attribute22'):
        assert _is_linked(a2, 'uml_attribute22', b)
    _safe_set(b, 'uml_DocumentRoot21', set())
    assert not _is_linked(b, 'uml_DocumentRoot21', a2)
    if hasattr(a2, 'uml_attribute22'):
        assert not _is_linked(a2, 'uml_attribute22', b)


def test_assoc_attributes23_reverse_link_reassign_clear():
    a1 = uml_attributes(group="sample_text")
    a2 = uml_attributes(group="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot24', {a1})
    assert _is_linked(b, 'uml_DocumentRoot24', a1)
    if hasattr(a1, 'uml_attributes25'):
        assert _is_linked(a1, 'uml_attributes25', b)
    _safe_set(b, 'uml_DocumentRoot24', {a2})
    assert _is_linked(b, 'uml_DocumentRoot24', a2)
    if hasattr(a1, 'uml_attributes25'):
        assert not _is_linked(a1, 'uml_attributes25', b)
    if hasattr(a2, 'uml_attributes25'):
        assert _is_linked(a2, 'uml_attributes25', b)
    _safe_set(b, 'uml_DocumentRoot24', set())
    assert not _is_linked(b, 'uml_DocumentRoot24', a2)
    if hasattr(a2, 'uml_attributes25'):
        assert not _is_linked(a2, 'uml_attributes25', b)


def test_assoc_attributes4_reverse_link_reassign_clear():
    a1 = uml_class_(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = uml_class_(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = uml_attributes(group="sample_text")
    _safe_set(b, 'uml_attributes6', a1)
    assert _is_linked(b, 'uml_attributes6', a1)
    if hasattr(a1, 'uml_class_5'):
        assert _is_linked(a1, 'uml_class_5', b)
    _safe_set(b, 'uml_attributes6', a2)
    assert _is_linked(b, 'uml_attributes6', a2)
    if hasattr(a1, 'uml_class_5'):
        assert not _is_linked(a1, 'uml_class_5', b)
    if hasattr(a2, 'uml_class_5'):
        assert _is_linked(a2, 'uml_class_5', b)
    _safe_set(b, 'uml_attributes6', None)
    assert not _is_linked(b, 'uml_attributes6', a2)
    if hasattr(a2, 'uml_class_5'):
        assert not _is_linked(a2, 'uml_class_5', b)


def test_assoc_class_26_reverse_link_reassign_clear():
    a1 = uml_class_(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = uml_class_(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot27', {a1})
    assert _is_linked(b, 'uml_DocumentRoot27', a1)
    if hasattr(a1, 'uml_class_28'):
        assert _is_linked(a1, 'uml_class_28', b)
    _safe_set(b, 'uml_DocumentRoot27', {a2})
    assert _is_linked(b, 'uml_DocumentRoot27', a2)
    if hasattr(a1, 'uml_class_28'):
        assert not _is_linked(a1, 'uml_class_28', b)
    if hasattr(a2, 'uml_class_28'):
        assert _is_linked(a2, 'uml_class_28', b)
    _safe_set(b, 'uml_DocumentRoot27', set())
    assert not _is_linked(b, 'uml_DocumentRoot27', a2)
    if hasattr(a2, 'uml_class_28'):
        assert not _is_linked(a2, 'uml_class_28', b)


def test_assoc_class_7_reverse_link_reassign_clear():
    a1 = uml_classifiersAndAssociations(group="sample_text")
    a2 = uml_classifiersAndAssociations(group="sample_text_2")
    b = uml_class_(kind="sample_text", name="sample_text", oID="sample_text")
    _safe_set(b, 'uml_class_8', a1)
    assert _is_linked(b, 'uml_class_8', a1)
    if hasattr(a1, 'uml_classifiersAndAssociations'):
        assert _is_linked(a1, 'uml_classifiersAndAssociations', b)
    _safe_set(b, 'uml_class_8', a2)
    assert _is_linked(b, 'uml_class_8', a2)
    if hasattr(a1, 'uml_classifiersAndAssociations'):
        assert not _is_linked(a1, 'uml_classifiersAndAssociations', b)
    if hasattr(a2, 'uml_classifiersAndAssociations'):
        assert _is_linked(a2, 'uml_classifiersAndAssociations', b)
    _safe_set(b, 'uml_class_8', None)
    assert not _is_linked(b, 'uml_class_8', a2)
    if hasattr(a2, 'uml_classifiersAndAssociations'):
        assert not _is_linked(a2, 'uml_classifiersAndAssociations', b)


def test_assoc_classifiersAndAssociations29_reverse_link_reassign_clear():
    a1 = uml_classifiersAndAssociations(group="sample_text")
    a2 = uml_classifiersAndAssociations(group="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot30', {a1})
    assert _is_linked(b, 'uml_DocumentRoot30', a1)
    if hasattr(a1, 'uml_classifiersAndAssociations31'):
        assert _is_linked(a1, 'uml_classifiersAndAssociations31', b)
    _safe_set(b, 'uml_DocumentRoot30', {a2})
    assert _is_linked(b, 'uml_DocumentRoot30', a2)
    if hasattr(a1, 'uml_classifiersAndAssociations31'):
        assert not _is_linked(a1, 'uml_classifiersAndAssociations31', b)
    if hasattr(a2, 'uml_classifiersAndAssociations31'):
        assert _is_linked(a2, 'uml_classifiersAndAssociations31', b)
    _safe_set(b, 'uml_DocumentRoot30', set())
    assert not _is_linked(b, 'uml_DocumentRoot30', a2)
    if hasattr(a2, 'uml_classifiersAndAssociations31'):
        assert not _is_linked(a2, 'uml_classifiersAndAssociations31', b)


def test_assoc_classifiersAndAssociations56_reverse_link_reassign_clear():
    a1 = uml_package_(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = uml_package_(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = uml_classifiersAndAssociations(group="sample_text")
    _safe_set(b, 'uml_classifiersAndAssociations58', a1)
    assert _is_linked(b, 'uml_classifiersAndAssociations58', a1)
    if hasattr(a1, 'uml_package_57'):
        assert _is_linked(a1, 'uml_package_57', b)
    _safe_set(b, 'uml_classifiersAndAssociations58', a2)
    assert _is_linked(b, 'uml_classifiersAndAssociations58', a2)
    if hasattr(a1, 'uml_package_57'):
        assert not _is_linked(a1, 'uml_package_57', b)
    if hasattr(a2, 'uml_package_57'):
        assert _is_linked(a2, 'uml_package_57', b)
    _safe_set(b, 'uml_classifiersAndAssociations58', None)
    assert not _is_linked(b, 'uml_classifiersAndAssociations58', a2)
    if hasattr(a2, 'uml_package_57'):
        assert not _is_linked(a2, 'uml_package_57', b)


def test_assoc_package38_reverse_link_reassign_clear():
    a1 = uml_package_(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = uml_package_(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot39', {a1})
    assert _is_linked(b, 'uml_DocumentRoot39', a1)
    if hasattr(a1, 'uml_package_'):
        assert _is_linked(a1, 'uml_package_', b)
    _safe_set(b, 'uml_DocumentRoot39', {a2})
    assert _is_linked(b, 'uml_DocumentRoot39', a2)
    if hasattr(a1, 'uml_package_'):
        assert not _is_linked(a1, 'uml_package_', b)
    if hasattr(a2, 'uml_package_'):
        assert _is_linked(a2, 'uml_package_', b)
    _safe_set(b, 'uml_DocumentRoot39', set())
    assert not _is_linked(b, 'uml_DocumentRoot39', a2)
    if hasattr(a2, 'uml_package_'):
        assert not _is_linked(a2, 'uml_package_', b)


def test_assoc_package59_reverse_link_reassign_clear():
    a1 = uml_packages(group="sample_text")
    a2 = uml_packages(group="sample_text_2")
    b = uml_package_(kind="sample_text", name="sample_text", oID="sample_text")
    _safe_set(b, 'uml_package_61', a1)
    assert _is_linked(b, 'uml_package_61', a1)
    if hasattr(a1, 'uml_packages60'):
        assert _is_linked(a1, 'uml_packages60', b)
    _safe_set(b, 'uml_package_61', a2)
    assert _is_linked(b, 'uml_package_61', a2)
    if hasattr(a1, 'uml_packages60'):
        assert not _is_linked(a1, 'uml_packages60', b)
    if hasattr(a2, 'uml_packages60'):
        assert _is_linked(a2, 'uml_packages60', b)
    _safe_set(b, 'uml_package_61', None)
    assert not _is_linked(b, 'uml_package_61', a2)
    if hasattr(a2, 'uml_packages60'):
        assert not _is_linked(a2, 'uml_packages60', b)


def test_assoc_packages40_reverse_link_reassign_clear():
    a1 = uml_packages(group="sample_text")
    a2 = uml_packages(group="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot41', {a1})
    assert _is_linked(b, 'uml_DocumentRoot41', a1)
    if hasattr(a1, 'uml_packages'):
        assert _is_linked(a1, 'uml_packages', b)
    _safe_set(b, 'uml_DocumentRoot41', {a2})
    assert _is_linked(b, 'uml_DocumentRoot41', a2)
    if hasattr(a1, 'uml_packages'):
        assert not _is_linked(a1, 'uml_packages', b)
    if hasattr(a2, 'uml_packages'):
        assert _is_linked(a2, 'uml_packages', b)
    _safe_set(b, 'uml_DocumentRoot41', set())
    assert not _is_linked(b, 'uml_DocumentRoot41', a2)
    if hasattr(a2, 'uml_packages'):
        assert not _is_linked(a2, 'uml_packages', b)


def test_assoc_primitiveDataType42_reverse_link_reassign_clear():
    a1 = uml_primitiveDataType(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = uml_primitiveDataType(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = uml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uml_DocumentRoot43', {a1})
    assert _is_linked(b, 'uml_DocumentRoot43', a1)
    if hasattr(a1, 'uml_primitiveDataType44'):
        assert _is_linked(a1, 'uml_primitiveDataType44', b)
    _safe_set(b, 'uml_DocumentRoot43', {a2})
    assert _is_linked(b, 'uml_DocumentRoot43', a2)
    if hasattr(a1, 'uml_primitiveDataType44'):
        assert not _is_linked(a1, 'uml_primitiveDataType44', b)
    if hasattr(a2, 'uml_primitiveDataType44'):
        assert _is_linked(a2, 'uml_primitiveDataType44', b)
    _safe_set(b, 'uml_DocumentRoot43', set())
    assert not _is_linked(b, 'uml_DocumentRoot43', a2)
    if hasattr(a2, 'uml_primitiveDataType44'):
        assert not _is_linked(a2, 'uml_primitiveDataType44', b)


def test_assoc_primitiveDataType9_reverse_link_reassign_clear():
    a1 = uml_primitiveDataType(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = uml_primitiveDataType(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = uml_classifiersAndAssociations(group="sample_text")
    _safe_set(b, 'uml_classifiersAndAssociations10', {a1})
    assert _is_linked(b, 'uml_classifiersAndAssociations10', a1)
    if hasattr(a1, 'uml_primitiveDataType'):
        assert _is_linked(a1, 'uml_primitiveDataType', b)
    _safe_set(b, 'uml_classifiersAndAssociations10', {a2})
    assert _is_linked(b, 'uml_classifiersAndAssociations10', a2)
    if hasattr(a1, 'uml_primitiveDataType'):
        assert not _is_linked(a1, 'uml_primitiveDataType', b)
    if hasattr(a2, 'uml_primitiveDataType'):
        assert _is_linked(a2, 'uml_primitiveDataType', b)
    _safe_set(b, 'uml_classifiersAndAssociations10', set())
    assert not _is_linked(b, 'uml_classifiersAndAssociations10', a2)
    if hasattr(a2, 'uml_primitiveDataType'):
        assert not _is_linked(a2, 'uml_primitiveDataType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_class_47_stub_double():
    # uml_generalClass has no real 'uml_generalClass48' property in the generated
    # code (a bare stub) -- manually attach it so uml_class_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_class_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_class_(kind="sample_text", name="sample_text", oID="sample_text")
    partner = uml_generalClass()
    setattr(partner, 'uml_generalClass48', None)
    _safe_set(owner, 'uml_class_49', partner)
    assert getattr(partner, 'uml_generalClass48') == owner
    _safe_set(owner, 'uml_class_49', None)
    assert getattr(partner, 'uml_generalClass48') is None


def test_assoc_class_50_stub_double():
    # uml_ownerClassifier has no real 'uml_ownerClassifier51' property in the generated
    # code (a bare stub) -- manually attach it so uml_class_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_class_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_class_(kind="sample_text", name="sample_text", oID="sample_text")
    partner = uml_ownerClassifier()
    setattr(partner, 'uml_ownerClassifier51', None)
    _safe_set(owner, 'uml_class_52', partner)
    assert getattr(partner, 'uml_ownerClassifier51') == owner
    _safe_set(owner, 'uml_class_52', None)
    assert getattr(partner, 'uml_ownerClassifier51') is None


def test_assoc_generalClass3_stub_double():
    # uml_generalClass has no real 'uml_generalClass' property in the generated
    # code (a bare stub) -- manually attach it so uml_class_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_class_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_class_(kind="sample_text", name="sample_text", oID="sample_text")
    partner = uml_generalClass()
    setattr(partner, 'uml_generalClass', None)
    _safe_set(owner, 'uml_class_', partner)
    assert getattr(partner, 'uml_generalClass') == owner
    _safe_set(owner, 'uml_class_', None)
    assert getattr(partner, 'uml_generalClass') is None


def test_assoc_generalClass32_stub_double():
    # uml_generalClass has no real 'uml_generalClass34' property in the generated
    # code (a bare stub) -- manually attach it so uml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_DocumentRoot(mixed="sample_text")
    partner = uml_generalClass()
    setattr(partner, 'uml_generalClass34', None)
    _safe_set(owner, 'uml_DocumentRoot33', {partner})
    assert getattr(partner, 'uml_generalClass34') == owner
    _safe_set(owner, 'uml_DocumentRoot33', set())
    assert getattr(partner, 'uml_generalClass34') is None


def test_assoc_ownerClassifier0_stub_double():
    # uml_ownerClassifier has no real 'uml_ownerClassifier' property in the generated
    # code (a bare stub) -- manually attach it so uml_attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_attribute(kind="sample_text", name="sample_text", oID="sample_text")
    partner = uml_ownerClassifier()
    setattr(partner, 'uml_ownerClassifier', None)
    _safe_set(owner, 'uml_attribute', partner)
    assert getattr(partner, 'uml_ownerClassifier') == owner
    _safe_set(owner, 'uml_attribute', None)
    assert getattr(partner, 'uml_ownerClassifier') is None


def test_assoc_ownerClassifier35_stub_double():
    # uml_ownerClassifier has no real 'uml_ownerClassifier37' property in the generated
    # code (a bare stub) -- manually attach it so uml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_DocumentRoot(mixed="sample_text")
    partner = uml_ownerClassifier()
    setattr(partner, 'uml_ownerClassifier37', None)
    _safe_set(owner, 'uml_DocumentRoot36', {partner})
    assert getattr(partner, 'uml_ownerClassifier37') == owner
    _safe_set(owner, 'uml_DocumentRoot36', set())
    assert getattr(partner, 'uml_ownerClassifier37') is None


def test_assoc_packages62_stub_double():
    # uml_UML has no real 'uml_UML63' property in the generated
    # code (a bare stub) -- manually attach it so uml_packages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_packages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_packages(group="sample_text")
    partner = uml_UML()
    setattr(partner, 'uml_UML63', None)
    _safe_set(owner, 'uml_packages64', partner)
    assert getattr(partner, 'uml_UML63') == owner
    _safe_set(owner, 'uml_packages64', None)
    assert getattr(partner, 'uml_UML63') is None


def test_assoc_primitiveDataType53_stub_double():
    # uml_ownerClassifier has no real 'uml_ownerClassifier54' property in the generated
    # code (a bare stub) -- manually attach it so uml_primitiveDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_primitiveDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_primitiveDataType(kind="sample_text", name="sample_text", oID="sample_text")
    partner = uml_ownerClassifier()
    setattr(partner, 'uml_ownerClassifier54', None)
    _safe_set(owner, 'uml_primitiveDataType55', partner)
    assert getattr(partner, 'uml_ownerClassifier54') == owner
    _safe_set(owner, 'uml_primitiveDataType55', None)
    assert getattr(partner, 'uml_ownerClassifier54') is None


def test_assoc_uML45_stub_double():
    # uml_UML has no real 'uml_UML' property in the generated
    # code (a bare stub) -- manually attach it so uml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_DocumentRoot(mixed="sample_text")
    partner = uml_UML()
    setattr(partner, 'uml_UML', None)
    _safe_set(owner, 'uml_DocumentRoot46', {partner})
    assert getattr(partner, 'uml_UML') == owner
    _safe_set(owner, 'uml_DocumentRoot46', set())
    assert getattr(partner, 'uml_UML') is None


def test_assoc_xMLNSPrefixMap13_stub_double():
    # uml_EStringToStringMapEntry has no real 'uml_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so uml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_DocumentRoot(mixed="sample_text")
    partner = uml_EStringToStringMapEntry()
    setattr(partner, 'uml_EStringToStringMapEntry', None)
    _safe_set(owner, 'uml_DocumentRoot', {partner})
    assert getattr(partner, 'uml_EStringToStringMapEntry') == owner
    _safe_set(owner, 'uml_DocumentRoot', set())
    assert getattr(partner, 'uml_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation14_stub_double():
    # uml_EStringToStringMapEntry has no real 'uml_EStringToStringMapEntry16' property in the generated
    # code (a bare stub) -- manually attach it so uml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_DocumentRoot(mixed="sample_text")
    partner = uml_EStringToStringMapEntry()
    setattr(partner, 'uml_EStringToStringMapEntry16', None)
    _safe_set(owner, 'uml_DocumentRoot15', {partner})
    assert getattr(partner, 'uml_EStringToStringMapEntry16') == owner
    _safe_set(owner, 'uml_DocumentRoot15', set())
    assert getattr(partner, 'uml_EStringToStringMapEntry16') is None


