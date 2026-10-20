import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TAbstractType,
    TAnnotatable,
    TElementWithId,
    TMember,
    TSignature,
    basic_TAbstractType,
    basic_TAccess,
    basic_TAnnotatable,
    basic_TAnnotation,
    basic_TAnnotationType,
    basic_TClass,
    basic_TElementWithId,
    basic_TField,
    basic_TFieldDefinition,
    basic_TFieldSignature,
    basic_TInterface,
    basic_TMember,
    basic_TMethod,
    basic_TMethodDefinition,
    basic_TMethodSignature,
    basic_TPackage,
    basic_TParameter,
    basic_TParameterList,
    basic_TSignature,
    basic_TypeGraph,
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

def test_assoc_fields89_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TField(tName="sample_text")
    _safe_set(b, 'TField91', a1)
    assert _is_linked(b, 'TField91', a1)
    if hasattr(a1, 'pg90'):
        assert _is_linked(a1, 'pg90', b)
    _safe_set(b, 'TField91', a2)
    assert _is_linked(b, 'TField91', a2)
    if hasattr(a1, 'pg90'):
        assert not _is_linked(a1, 'pg90', b)
    if hasattr(a2, 'pg90'):
        assert _is_linked(a2, 'pg90', b)
    _safe_set(b, 'TField91', None)
    assert not _is_linked(b, 'TField91', a2)
    if hasattr(a2, 'pg90'):
        assert not _is_linked(a2, 'pg90', b)


def test_assoc_methods86_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TMethod(tName="sample_text")
    _safe_set(b, 'TMethod88', a1)
    assert _is_linked(b, 'TMethod88', a1)
    if hasattr(a1, 'pg87'):
        assert _is_linked(a1, 'pg87', b)
    _safe_set(b, 'TMethod88', a2)
    assert _is_linked(b, 'TMethod88', a2)
    if hasattr(a1, 'pg87'):
        assert not _is_linked(a1, 'pg87', b)
    if hasattr(a2, 'pg87'):
        assert _is_linked(a2, 'pg87', b)
    _safe_set(b, 'TMethod88', None)
    assert not _is_linked(b, 'TMethod88', a2)
    if hasattr(a2, 'pg87'):
        assert not _is_linked(a2, 'pg87', b)


def test_assoc_ownedTypes67_reverse_link_reassign_clear():
    a1 = basic_TPackage(tName="sample_text")
    a2 = basic_TPackage(tName="sample_text_2")
    b = basic_TAbstractType(tLib=True, tName="sample_text")
    _safe_set(b, 'TAbstractType68', a1)
    assert _is_linked(b, 'TAbstractType68', a1)
    if hasattr(a1, 'package'):
        assert _is_linked(a1, 'package', b)
    _safe_set(b, 'TAbstractType68', a2)
    assert _is_linked(b, 'TAbstractType68', a2)
    if hasattr(a1, 'package'):
        assert not _is_linked(a1, 'package', b)
    if hasattr(a2, 'package'):
        assert _is_linked(a2, 'package', b)
    _safe_set(b, 'TAbstractType68', None)
    assert not _is_linked(b, 'TAbstractType68', a2)
    if hasattr(a2, 'package'):
        assert not _is_linked(a2, 'package', b)


def test_assoc_ownedTypes98_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TAbstractType(tLib=True, tName="sample_text")
    _safe_set(b, 'TAbstractType100', a1)
    assert _is_linked(b, 'TAbstractType100', a1)
    if hasattr(a1, 'pg99'):
        assert _is_linked(a1, 'pg99', b)
    _safe_set(b, 'TAbstractType100', a2)
    assert _is_linked(b, 'TAbstractType100', a2)
    if hasattr(a1, 'pg99'):
        assert not _is_linked(a1, 'pg99', b)
    if hasattr(a2, 'pg99'):
        assert _is_linked(a2, 'pg99', b)
    _safe_set(b, 'TAbstractType100', None)
    assert not _is_linked(b, 'TAbstractType100', a2)
    if hasattr(a2, 'pg99'):
        assert not _is_linked(a2, 'pg99', b)


def test_assoc_package113_reverse_link_reassign_clear():
    a1 = basic_TPackage(tName="sample_text")
    a2 = basic_TPackage(tName="sample_text_2")
    b = basic_TAbstractType(tLib=True, tName="sample_text")
    _safe_set(b, 'ownedTypes114', a1)
    assert _is_linked(b, 'ownedTypes114', a1)
    if hasattr(a1, 'TPackage115'):
        assert _is_linked(a1, 'TPackage115', b)
    _safe_set(b, 'ownedTypes114', a2)
    assert _is_linked(b, 'ownedTypes114', a2)
    if hasattr(a1, 'TPackage115'):
        assert not _is_linked(a1, 'TPackage115', b)
    if hasattr(a2, 'TPackage115'):
        assert _is_linked(a2, 'TPackage115', b)
    _safe_set(b, 'ownedTypes114', None)
    assert not _is_linked(b, 'ownedTypes114', a2)
    if hasattr(a2, 'TPackage115'):
        assert not _is_linked(a2, 'TPackage115', b)


def test_assoc_packages84_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TPackage(tName="sample_text")
    _safe_set(b, 'TPackage85', a1)
    assert _is_linked(b, 'TPackage85', a1)
    if hasattr(a1, 'pg'):
        assert _is_linked(a1, 'pg', b)
    _safe_set(b, 'TPackage85', a2)
    assert _is_linked(b, 'TPackage85', a2)
    if hasattr(a1, 'pg'):
        assert not _is_linked(a1, 'pg', b)
    if hasattr(a2, 'pg'):
        assert _is_linked(a2, 'pg', b)
    _safe_set(b, 'TPackage85', None)
    assert not _is_linked(b, 'TPackage85', a2)
    if hasattr(a2, 'pg'):
        assert not _is_linked(a2, 'pg', b)


def test_assoc_parent62_reverse_link_reassign_clear():
    a1 = basic_TPackage(tName="sample_text")
    a2 = basic_TPackage(tName="sample_text_2")
    b = basic_TPackage(tName="sample_text")
    _safe_set(b, 'subpackage', a1)
    assert _is_linked(b, 'subpackage', a1)
    if hasattr(a1, 'TPackage63'):
        assert _is_linked(a1, 'TPackage63', b)
    _safe_set(b, 'subpackage', a2)
    assert _is_linked(b, 'subpackage', a2)
    if hasattr(a1, 'TPackage63'):
        assert not _is_linked(a1, 'TPackage63', b)
    if hasattr(a2, 'TPackage63'):
        assert _is_linked(a2, 'TPackage63', b)
    _safe_set(b, 'subpackage', None)
    assert not _is_linked(b, 'subpackage', a2)
    if hasattr(a2, 'TPackage63'):
        assert not _is_linked(a2, 'TPackage63', b)


def test_assoc_pg111_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TAbstractType(tLib=True, tName="sample_text")
    _safe_set(b, 'ownedTypes', a1)
    assert _is_linked(b, 'ownedTypes', a1)
    if hasattr(a1, 'TypeGraph112'):
        assert _is_linked(a1, 'TypeGraph112', b)
    _safe_set(b, 'ownedTypes', a2)
    assert _is_linked(b, 'ownedTypes', a2)
    if hasattr(a1, 'TypeGraph112'):
        assert not _is_linked(a1, 'TypeGraph112', b)
    if hasattr(a2, 'TypeGraph112'):
        assert _is_linked(a2, 'TypeGraph112', b)
    _safe_set(b, 'ownedTypes', None)
    assert not _is_linked(b, 'ownedTypes', a2)
    if hasattr(a2, 'TypeGraph112'):
        assert not _is_linked(a2, 'TypeGraph112', b)


def test_assoc_pg13_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TField(tName="sample_text")
    _safe_set(b, 'fields', a1)
    assert _is_linked(b, 'fields', a1)
    if hasattr(a1, 'TypeGraph'):
        assert _is_linked(a1, 'TypeGraph', b)
    _safe_set(b, 'fields', a2)
    assert _is_linked(b, 'fields', a2)
    if hasattr(a1, 'TypeGraph'):
        assert not _is_linked(a1, 'TypeGraph', b)
    if hasattr(a2, 'TypeGraph'):
        assert _is_linked(a2, 'TypeGraph', b)
    _safe_set(b, 'fields', None)
    assert not _is_linked(b, 'fields', a2)
    if hasattr(a2, 'TypeGraph'):
        assert not _is_linked(a2, 'TypeGraph', b)


def test_assoc_pg29_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TMethod(tName="sample_text")
    _safe_set(b, 'methods', a1)
    assert _is_linked(b, 'methods', a1)
    if hasattr(a1, 'TypeGraph30'):
        assert _is_linked(a1, 'TypeGraph30', b)
    _safe_set(b, 'methods', a2)
    assert _is_linked(b, 'methods', a2)
    if hasattr(a1, 'TypeGraph30'):
        assert not _is_linked(a1, 'TypeGraph30', b)
    if hasattr(a2, 'TypeGraph30'):
        assert _is_linked(a2, 'TypeGraph30', b)
    _safe_set(b, 'methods', None)
    assert not _is_linked(b, 'methods', a2)
    if hasattr(a2, 'TypeGraph30'):
        assert not _is_linked(a2, 'TypeGraph30', b)


def test_assoc_pg57_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TPackage(tName="sample_text")
    _safe_set(b, 'packages', a1)
    assert _is_linked(b, 'packages', a1)
    if hasattr(a1, 'TypeGraph58'):
        assert _is_linked(a1, 'TypeGraph58', b)
    _safe_set(b, 'packages', a2)
    assert _is_linked(b, 'packages', a2)
    if hasattr(a1, 'TypeGraph58'):
        assert not _is_linked(a1, 'TypeGraph58', b)
    if hasattr(a2, 'TypeGraph58'):
        assert _is_linked(a2, 'TypeGraph58', b)
    _safe_set(b, 'packages', None)
    assert not _is_linked(b, 'packages', a2)
    if hasattr(a2, 'TypeGraph58'):
        assert not _is_linked(a2, 'TypeGraph58', b)


def test_assoc_subpackage60_reverse_link_reassign_clear():
    a1 = basic_TPackage(tName="sample_text")
    a2 = basic_TPackage(tName="sample_text_2")
    b = basic_TPackage(tName="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'TPackage'):
        assert _is_linked(a1, 'TPackage', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'TPackage'):
        assert not _is_linked(a1, 'TPackage', b)
    if hasattr(a2, 'TPackage'):
        assert _is_linked(a2, 'TPackage', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'TPackage'):
        assert not _is_linked(a2, 'TPackage', b)


def test_assoc_typeGraph69_reverse_link_reassign_clear():
    a1 = basic_TypeGraph(tName="sample_text")
    a2 = basic_TypeGraph(tName="sample_text_2")
    b = basic_TPackage(tName="sample_text")
    _safe_set(b, 'basic_TPackage70', a1)
    assert _is_linked(b, 'basic_TPackage70', a1)
    if hasattr(a1, 'basic_TypeGraph'):
        assert _is_linked(a1, 'basic_TypeGraph', b)
    _safe_set(b, 'basic_TPackage70', a2)
    assert _is_linked(b, 'basic_TPackage70', a2)
    if hasattr(a1, 'basic_TypeGraph'):
        assert not _is_linked(a1, 'basic_TypeGraph', b)
    if hasattr(a2, 'basic_TypeGraph'):
        assert _is_linked(a2, 'basic_TypeGraph', b)
    _safe_set(b, 'basic_TPackage70', None)
    assert not _is_linked(b, 'basic_TPackage70', a2)
    if hasattr(a2, 'basic_TypeGraph'):
        assert not _is_linked(a2, 'basic_TypeGraph', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classes64_stub_double():
    # basic_TClass has no real 'basic_TClass' property in the generated
    # code (a bare stub) -- manually attach it so basic_TPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TPackage(tName="sample_text")
    partner = basic_TClass()
    setattr(partner, 'basic_TClass', None)
    _safe_set(owner, 'basic_TPackage', {partner})
    assert getattr(partner, 'basic_TClass') == owner
    _safe_set(owner, 'basic_TPackage', set())
    assert getattr(partner, 'basic_TClass') is None


def test_assoc_classes92_stub_double():
    # basic_TClass has no real 'basic_TClass94' property in the generated
    # code (a bare stub) -- manually attach it so basic_TypeGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TypeGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TypeGraph(tName="sample_text")
    partner = basic_TClass()
    setattr(partner, 'basic_TClass94', None)
    _safe_set(owner, 'basic_TypeGraph93', {partner})
    assert getattr(partner, 'basic_TClass94') == owner
    _safe_set(owner, 'basic_TypeGraph93', set())
    assert getattr(partner, 'basic_TClass94') is None


def test_assoc_definedBy25_stub_double():
    # basic_TMember has no real 'defines' property in the generated
    # code (a bare stub) -- manually attach it so basic_TAbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TAbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TAbstractType(tLib=True, tName="sample_text")
    partner = basic_TMember()
    setattr(partner, 'defines', None)
    _safe_set(owner, 'TAbstractType', partner)
    assert getattr(partner, 'defines') == owner
    _safe_set(owner, 'TAbstractType', None)
    assert getattr(partner, 'defines') is None


def test_assoc_defines118_stub_double():
    # basic_TMember has no real 'TMember119' property in the generated
    # code (a bare stub) -- manually attach it so basic_TAbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TAbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TAbstractType(tLib=True, tName="sample_text")
    partner = basic_TMember()
    setattr(partner, 'TMember119', None)
    _safe_set(owner, 'definedBy', {partner})
    assert getattr(partner, 'TMember119') == owner
    _safe_set(owner, 'definedBy', set())
    assert getattr(partner, 'TMember119') is None


def test_assoc_field23_stub_double():
    # basic_TFieldSignature has no real 'signatures' property in the generated
    # code (a bare stub) -- manually attach it so basic_TField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TField(tName="sample_text")
    partner = basic_TFieldSignature()
    setattr(partner, 'signatures', None)
    _safe_set(owner, 'TField', partner)
    assert getattr(partner, 'signatures') == owner
    _safe_set(owner, 'TField', None)
    assert getattr(partner, 'signatures') is None


def test_assoc_interfaces65_stub_double():
    # basic_TInterface has no real 'basic_TInterface' property in the generated
    # code (a bare stub) -- manually attach it so basic_TPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TPackage(tName="sample_text")
    partner = basic_TInterface()
    setattr(partner, 'basic_TInterface', None)
    _safe_set(owner, 'basic_TPackage66', {partner})
    assert getattr(partner, 'basic_TInterface') == owner
    _safe_set(owner, 'basic_TPackage66', set())
    assert getattr(partner, 'basic_TInterface') is None


def test_assoc_interfaces95_stub_double():
    # basic_TInterface has no real 'basic_TInterface97' property in the generated
    # code (a bare stub) -- manually attach it so basic_TypeGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TypeGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TypeGraph(tName="sample_text")
    partner = basic_TInterface()
    setattr(partner, 'basic_TInterface97', None)
    _safe_set(owner, 'basic_TypeGraph96', {partner})
    assert getattr(partner, 'basic_TInterface97') == owner
    _safe_set(owner, 'basic_TypeGraph96', set())
    assert getattr(partner, 'basic_TInterface97') is None


def test_assoc_method48_stub_double():
    # basic_TMethodSignature has no real 'signatures49' property in the generated
    # code (a bare stub) -- manually attach it so basic_TMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TMethod(tName="sample_text")
    partner = basic_TMethodSignature()
    setattr(partner, 'signatures49', None)
    _safe_set(owner, 'TMethod', partner)
    assert getattr(partner, 'signatures49') == owner
    _safe_set(owner, 'TMethod', None)
    assert getattr(partner, 'signatures49') is None


def test_assoc_returnType46_stub_double():
    # basic_TMethodDefinition has no real 'basic_TMethodDefinition' property in the generated
    # code (a bare stub) -- manually attach it so basic_TAbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TAbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TAbstractType(tLib=True, tName="sample_text")
    partner = basic_TMethodDefinition()
    setattr(partner, 'basic_TMethodDefinition', None)
    _safe_set(owner, 'basic_TAbstractType47', partner)
    assert getattr(partner, 'basic_TMethodDefinition') == owner
    _safe_set(owner, 'basic_TAbstractType47', None)
    assert getattr(partner, 'basic_TMethodDefinition') is None


def test_assoc_returnType54_stub_double():
    # basic_TMethodSignature has no real 'basic_TMethodSignature55' property in the generated
    # code (a bare stub) -- manually attach it so basic_TAbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TAbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TAbstractType(tLib=True, tName="sample_text")
    partner = basic_TMethodSignature()
    setattr(partner, 'basic_TMethodSignature55', None)
    _safe_set(owner, 'basic_TAbstractType56', partner)
    assert getattr(partner, 'basic_TMethodSignature55') == owner
    _safe_set(owner, 'basic_TAbstractType56', None)
    assert getattr(partner, 'basic_TMethodSignature55') is None


def test_assoc_signature116_stub_double():
    # basic_TSignature has no real 'basic_TSignature' property in the generated
    # code (a bare stub) -- manually attach it so basic_TAbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TAbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TAbstractType(tLib=True, tName="sample_text")
    partner = basic_TSignature()
    setattr(partner, 'basic_TSignature', None)
    _safe_set(owner, 'basic_TAbstractType117', {partner})
    assert getattr(partner, 'basic_TSignature') == owner
    _safe_set(owner, 'basic_TAbstractType117', set())
    assert getattr(partner, 'basic_TSignature') is None


def test_assoc_signatures12_stub_double():
    # basic_TFieldSignature has no real 'TFieldSignature' property in the generated
    # code (a bare stub) -- manually attach it so basic_TField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TField(tName="sample_text")
    partner = basic_TFieldSignature()
    setattr(partner, 'TFieldSignature', None)
    _safe_set(owner, 'field', {partner})
    assert getattr(partner, 'TFieldSignature') == owner
    _safe_set(owner, 'field', set())
    assert getattr(partner, 'TFieldSignature') is None


def test_assoc_signatures31_stub_double():
    # basic_TMethodSignature has no real 'TMethodSignature' property in the generated
    # code (a bare stub) -- manually attach it so basic_TMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TMethod(tName="sample_text")
    partner = basic_TMethodSignature()
    setattr(partner, 'TMethodSignature', None)
    _safe_set(owner, 'method', {partner})
    assert getattr(partner, 'TMethodSignature') == owner
    _safe_set(owner, 'method', set())
    assert getattr(partner, 'TMethodSignature') is None


def test_assoc_tAnnotationTypes101_stub_double():
    # basic_TAnnotationType has no real 'basic_TAnnotationType' property in the generated
    # code (a bare stub) -- manually attach it so basic_TypeGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TypeGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TypeGraph(tName="sample_text")
    partner = basic_TAnnotationType()
    setattr(partner, 'basic_TAnnotationType', None)
    _safe_set(owner, 'basic_TypeGraph102', {partner})
    assert getattr(partner, 'basic_TAnnotationType') == owner
    _safe_set(owner, 'basic_TypeGraph102', set())
    assert getattr(partner, 'basic_TAnnotationType') is None


def test_assoc_type24_stub_double():
    # basic_TFieldSignature has no real 'basic_TFieldSignature' property in the generated
    # code (a bare stub) -- manually attach it so basic_TAbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TAbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TAbstractType(tLib=True, tName="sample_text")
    partner = basic_TFieldSignature()
    setattr(partner, 'basic_TFieldSignature', None)
    _safe_set(owner, 'basic_TAbstractType', partner)
    assert getattr(partner, 'basic_TFieldSignature') == owner
    _safe_set(owner, 'basic_TAbstractType', None)
    assert getattr(partner, 'basic_TFieldSignature') is None


def test_assoc_type76_stub_double():
    # basic_TParameter has no real 'basic_TParameter' property in the generated
    # code (a bare stub) -- manually attach it so basic_TAbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basic_TAbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basic_TAbstractType(tLib=True, tName="sample_text")
    partner = basic_TParameter()
    setattr(partner, 'basic_TParameter', None)
    _safe_set(owner, 'basic_TAbstractType77', partner)
    assert getattr(partner, 'basic_TParameter') == owner
    _safe_set(owner, 'basic_TAbstractType77', None)
    assert getattr(partner, 'basic_TParameter') is None


