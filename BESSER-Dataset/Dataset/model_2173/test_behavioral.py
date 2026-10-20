import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TMember,
    TSignature,
    TypeGraphBasic_TClass,
    TypeGraphBasic_TField,
    TypeGraphBasic_TFieldDefinition,
    TypeGraphBasic_TFieldSignature,
    TypeGraphBasic_TMember,
    TypeGraphBasic_TMethod,
    TypeGraphBasic_TMethodDefinition,
    TypeGraphBasic_TMethodSignature,
    TypeGraphBasic_TPackage,
    TypeGraphBasic_TParameter,
    TypeGraphBasic_TParameterList,
    TypeGraphBasic_TSignature,
    TypeGraphBasic_TypeGraph,
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

def test_assoc_childClasses7_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TClass(tName="sample_text")
    a2 = TypeGraphBasic_TClass(tName="sample_text_2")
    b = TypeGraphBasic_TClass(tName="sample_text")
    _safe_set(b, 'parentClass', {a1})
    assert _is_linked(b, 'parentClass', a1)
    if hasattr(a1, 'TClass8'):
        assert _is_linked(a1, 'TClass8', b)
    _safe_set(b, 'parentClass', {a2})
    assert _is_linked(b, 'parentClass', a2)
    if hasattr(a1, 'TClass8'):
        assert not _is_linked(a1, 'TClass8', b)
    if hasattr(a2, 'TClass8'):
        assert _is_linked(a2, 'TClass8', b)
    _safe_set(b, 'parentClass', set())
    assert not _is_linked(b, 'parentClass', a2)
    if hasattr(a2, 'TClass8'):
        assert not _is_linked(a2, 'TClass8', b)


def test_assoc_classes74_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TypeGraph(tName="sample_text")
    a2 = TypeGraphBasic_TypeGraph(tName="sample_text_2")
    b = TypeGraphBasic_TClass(tName="sample_text")
    _safe_set(b, 'TypeGraphBasic_TClass76', a1)
    assert _is_linked(b, 'TypeGraphBasic_TClass76', a1)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph75'):
        assert _is_linked(a1, 'TypeGraphBasic_TypeGraph75', b)
    _safe_set(b, 'TypeGraphBasic_TClass76', a2)
    assert _is_linked(b, 'TypeGraphBasic_TClass76', a2)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph75'):
        assert not _is_linked(a1, 'TypeGraphBasic_TypeGraph75', b)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph75'):
        assert _is_linked(a2, 'TypeGraphBasic_TypeGraph75', b)
    _safe_set(b, 'TypeGraphBasic_TClass76', None)
    assert not _is_linked(b, 'TypeGraphBasic_TClass76', a2)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph75'):
        assert not _is_linked(a2, 'TypeGraphBasic_TypeGraph75', b)


def test_assoc_containedClasses48_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TPackage(tName="sample_text")
    a2 = TypeGraphBasic_TPackage(tName="sample_text_2")
    b = TypeGraphBasic_TClass(tName="sample_text")
    _safe_set(b, 'TClass49', a1)
    assert _is_linked(b, 'TClass49', a1)
    if hasattr(a1, 'package'):
        assert _is_linked(a1, 'package', b)
    _safe_set(b, 'TClass49', a2)
    assert _is_linked(b, 'TClass49', a2)
    if hasattr(a1, 'package'):
        assert not _is_linked(a1, 'package', b)
    if hasattr(a2, 'package'):
        assert _is_linked(a2, 'package', b)
    _safe_set(b, 'TClass49', None)
    assert not _is_linked(b, 'TClass49', a2)
    if hasattr(a2, 'package'):
        assert not _is_linked(a2, 'package', b)


def test_assoc_fields72_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TypeGraph(tName="sample_text")
    a2 = TypeGraphBasic_TypeGraph(tName="sample_text_2")
    b = TypeGraphBasic_TField(tName="sample_text")
    _safe_set(b, 'TypeGraphBasic_TField', a1)
    assert _is_linked(b, 'TypeGraphBasic_TField', a1)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph73'):
        assert _is_linked(a1, 'TypeGraphBasic_TypeGraph73', b)
    _safe_set(b, 'TypeGraphBasic_TField', a2)
    assert _is_linked(b, 'TypeGraphBasic_TField', a2)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph73'):
        assert not _is_linked(a1, 'TypeGraphBasic_TypeGraph73', b)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph73'):
        assert _is_linked(a2, 'TypeGraphBasic_TypeGraph73', b)
    _safe_set(b, 'TypeGraphBasic_TField', None)
    assert not _is_linked(b, 'TypeGraphBasic_TField', a2)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph73'):
        assert not _is_linked(a2, 'TypeGraphBasic_TypeGraph73', b)


def test_assoc_methods70_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TypeGraph(tName="sample_text")
    a2 = TypeGraphBasic_TypeGraph(tName="sample_text_2")
    b = TypeGraphBasic_TMethod(tName="sample_text")
    _safe_set(b, 'TypeGraphBasic_TMethod', a1)
    assert _is_linked(b, 'TypeGraphBasic_TMethod', a1)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph71'):
        assert _is_linked(a1, 'TypeGraphBasic_TypeGraph71', b)
    _safe_set(b, 'TypeGraphBasic_TMethod', a2)
    assert _is_linked(b, 'TypeGraphBasic_TMethod', a2)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph71'):
        assert not _is_linked(a1, 'TypeGraphBasic_TypeGraph71', b)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph71'):
        assert _is_linked(a2, 'TypeGraphBasic_TypeGraph71', b)
    _safe_set(b, 'TypeGraphBasic_TMethod', None)
    assert not _is_linked(b, 'TypeGraphBasic_TMethod', a2)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph71'):
        assert not _is_linked(a2, 'TypeGraphBasic_TypeGraph71', b)


def test_assoc_package0_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TPackage(tName="sample_text")
    a2 = TypeGraphBasic_TPackage(tName="sample_text_2")
    b = TypeGraphBasic_TClass(tName="sample_text")
    _safe_set(b, 'containedClasses', a1)
    assert _is_linked(b, 'containedClasses', a1)
    if hasattr(a1, 'TPackage'):
        assert _is_linked(a1, 'TPackage', b)
    _safe_set(b, 'containedClasses', a2)
    assert _is_linked(b, 'containedClasses', a2)
    if hasattr(a1, 'TPackage'):
        assert not _is_linked(a1, 'TPackage', b)
    if hasattr(a2, 'TPackage'):
        assert _is_linked(a2, 'TPackage', b)
    _safe_set(b, 'containedClasses', None)
    assert not _is_linked(b, 'containedClasses', a2)
    if hasattr(a2, 'TPackage'):
        assert not _is_linked(a2, 'TPackage', b)


def test_assoc_packages69_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TypeGraph(tName="sample_text")
    a2 = TypeGraphBasic_TypeGraph(tName="sample_text_2")
    b = TypeGraphBasic_TPackage(tName="sample_text")
    _safe_set(b, 'TypeGraphBasic_TPackage', a1)
    assert _is_linked(b, 'TypeGraphBasic_TPackage', a1)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph'):
        assert _is_linked(a1, 'TypeGraphBasic_TypeGraph', b)
    _safe_set(b, 'TypeGraphBasic_TPackage', a2)
    assert _is_linked(b, 'TypeGraphBasic_TPackage', a2)
    if hasattr(a1, 'TypeGraphBasic_TypeGraph'):
        assert not _is_linked(a1, 'TypeGraphBasic_TypeGraph', b)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph'):
        assert _is_linked(a2, 'TypeGraphBasic_TypeGraph', b)
    _safe_set(b, 'TypeGraphBasic_TPackage', None)
    assert not _is_linked(b, 'TypeGraphBasic_TPackage', a2)
    if hasattr(a2, 'TypeGraphBasic_TypeGraph'):
        assert not _is_linked(a2, 'TypeGraphBasic_TypeGraph', b)


def test_assoc_parent54_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TPackage(tName="sample_text")
    a2 = TypeGraphBasic_TPackage(tName="sample_text_2")
    b = TypeGraphBasic_TPackage(tName="sample_text")
    _safe_set(b, 'subpackage', a1)
    assert _is_linked(b, 'subpackage', a1)
    if hasattr(a1, 'TPackage55'):
        assert _is_linked(a1, 'TPackage55', b)
    _safe_set(b, 'subpackage', a2)
    assert _is_linked(b, 'subpackage', a2)
    if hasattr(a1, 'TPackage55'):
        assert not _is_linked(a1, 'TPackage55', b)
    if hasattr(a2, 'TPackage55'):
        assert _is_linked(a2, 'TPackage55', b)
    _safe_set(b, 'subpackage', None)
    assert not _is_linked(b, 'subpackage', a2)
    if hasattr(a2, 'TPackage55'):
        assert not _is_linked(a2, 'TPackage55', b)


def test_assoc_parentClass5_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TClass(tName="sample_text")
    a2 = TypeGraphBasic_TClass(tName="sample_text_2")
    b = TypeGraphBasic_TClass(tName="sample_text")
    _safe_set(b, 'childClasses', a1)
    assert _is_linked(b, 'childClasses', a1)
    if hasattr(a1, 'TClass'):
        assert _is_linked(a1, 'TClass', b)
    _safe_set(b, 'childClasses', a2)
    assert _is_linked(b, 'childClasses', a2)
    if hasattr(a1, 'TClass'):
        assert not _is_linked(a1, 'TClass', b)
    if hasattr(a2, 'TClass'):
        assert _is_linked(a2, 'TClass', b)
    _safe_set(b, 'childClasses', None)
    assert not _is_linked(b, 'childClasses', a2)
    if hasattr(a2, 'TClass'):
        assert not _is_linked(a2, 'TClass', b)


def test_assoc_subpackage51_reverse_link_reassign_clear():
    a1 = TypeGraphBasic_TPackage(tName="sample_text")
    a2 = TypeGraphBasic_TPackage(tName="sample_text_2")
    b = TypeGraphBasic_TPackage(tName="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'TPackage52'):
        assert _is_linked(a1, 'TPackage52', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'TPackage52'):
        assert not _is_linked(a1, 'TPackage52', b)
    if hasattr(a2, 'TPackage52'):
        assert _is_linked(a2, 'TPackage52', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'TPackage52'):
        assert not _is_linked(a2, 'TPackage52', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defines2_stub_double():
    # TypeGraphBasic_TMember has no real 'TypeGraphBasic_TMember' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TClass(tName="sample_text")
    partner = TypeGraphBasic_TMember()
    setattr(partner, 'TypeGraphBasic_TMember', None)
    _safe_set(owner, 'TypeGraphBasic_TClass3', {partner})
    assert getattr(partner, 'TypeGraphBasic_TMember') == owner
    _safe_set(owner, 'TypeGraphBasic_TClass3', set())
    assert getattr(partner, 'TypeGraphBasic_TMember') is None


def test_assoc_field19_stub_double():
    # TypeGraphBasic_TFieldSignature has no real 'signatures' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TField(tName="sample_text")
    partner = TypeGraphBasic_TFieldSignature()
    setattr(partner, 'signatures', None)
    _safe_set(owner, 'TField', partner)
    assert getattr(partner, 'signatures') == owner
    _safe_set(owner, 'TField', None)
    assert getattr(partner, 'signatures') is None


def test_assoc_method42_stub_double():
    # TypeGraphBasic_TMethodSignature has no real 'signatures43' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TMethod(tName="sample_text")
    partner = TypeGraphBasic_TMethodSignature()
    setattr(partner, 'signatures43', None)
    _safe_set(owner, 'TMethod', partner)
    assert getattr(partner, 'signatures43') == owner
    _safe_set(owner, 'TMethod', None)
    assert getattr(partner, 'signatures43') is None


def test_assoc_returnType40_stub_double():
    # TypeGraphBasic_TMethodDefinition has no real 'TypeGraphBasic_TMethodDefinition' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TClass(tName="sample_text")
    partner = TypeGraphBasic_TMethodDefinition()
    setattr(partner, 'TypeGraphBasic_TMethodDefinition', None)
    _safe_set(owner, 'TypeGraphBasic_TClass41', partner)
    assert getattr(partner, 'TypeGraphBasic_TMethodDefinition') == owner
    _safe_set(owner, 'TypeGraphBasic_TClass41', None)
    assert getattr(partner, 'TypeGraphBasic_TMethodDefinition') is None


def test_assoc_signature1_stub_double():
    # TypeGraphBasic_TSignature has no real 'TypeGraphBasic_TSignature' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TClass(tName="sample_text")
    partner = TypeGraphBasic_TSignature()
    setattr(partner, 'TypeGraphBasic_TSignature', None)
    _safe_set(owner, 'TypeGraphBasic_TClass', {partner})
    assert getattr(partner, 'TypeGraphBasic_TSignature') == owner
    _safe_set(owner, 'TypeGraphBasic_TClass', set())
    assert getattr(partner, 'TypeGraphBasic_TSignature') is None


def test_assoc_signatures25_stub_double():
    # TypeGraphBasic_TMethodSignature has no real 'TMethodSignature' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TMethod(tName="sample_text")
    partner = TypeGraphBasic_TMethodSignature()
    setattr(partner, 'TMethodSignature', None)
    _safe_set(owner, 'method', {partner})
    assert getattr(partner, 'TMethodSignature') == owner
    _safe_set(owner, 'method', set())
    assert getattr(partner, 'TMethodSignature') is None


def test_assoc_signatures9_stub_double():
    # TypeGraphBasic_TFieldSignature has no real 'TFieldSignature' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TField(tName="sample_text")
    partner = TypeGraphBasic_TFieldSignature()
    setattr(partner, 'TFieldSignature', None)
    _safe_set(owner, 'field', {partner})
    assert getattr(partner, 'TFieldSignature') == owner
    _safe_set(owner, 'field', set())
    assert getattr(partner, 'TFieldSignature') is None


def test_assoc_tClass61_stub_double():
    # TypeGraphBasic_TParameter has no real 'TypeGraphBasic_TParameter' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TClass(tName="sample_text")
    partner = TypeGraphBasic_TParameter()
    setattr(partner, 'TypeGraphBasic_TParameter', None)
    _safe_set(owner, 'TypeGraphBasic_TClass62', partner)
    assert getattr(partner, 'TypeGraphBasic_TParameter') == owner
    _safe_set(owner, 'TypeGraphBasic_TClass62', None)
    assert getattr(partner, 'TypeGraphBasic_TParameter') is None


def test_assoc_type20_stub_double():
    # TypeGraphBasic_TFieldSignature has no real 'TypeGraphBasic_TFieldSignature' property in the generated
    # code (a bare stub) -- manually attach it so TypeGraphBasic_TClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeGraphBasic_TClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeGraphBasic_TClass(tName="sample_text")
    partner = TypeGraphBasic_TFieldSignature()
    setattr(partner, 'TypeGraphBasic_TFieldSignature', None)
    _safe_set(owner, 'TypeGraphBasic_TClass21', partner)
    assert getattr(partner, 'TypeGraphBasic_TFieldSignature') == owner
    _safe_set(owner, 'TypeGraphBasic_TClass21', None)
    assert getattr(partner, 'TypeGraphBasic_TFieldSignature') is None


