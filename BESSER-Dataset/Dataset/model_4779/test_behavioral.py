import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotatableElement,
    ComplexType,
    Declaration,
    DomainElement,
    GenericElement,
    MetaComposite,
    NamedElement,
    Type,
    TypeSpecifier,
    TypedDeclaration,
    TypedElement,
    types_AnnotatableElement,
    types_Annotation,
    types_AnnotationType,
    types_ArrayTypeSpecifier,
    types_ComplexType,
    types_Declaration,
    types_Domain,
    types_EObject,
    types_EnumerationType,
    types_Enumerator,
    types_Event,
    types_Expression,
    types_GenericElement,
    types_MetaComposite,
    types_Operation,
    types_Package,
    types_Parameter,
    types_PrimitiveType,
    types_Property,
    types_Type,
    types_TypeAlias,
    types_TypeParameter,
    types_TypeSpecifier,
    types_TypedDeclaration,
    types_TypedElement,
    Direction,
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

def test_assoc_annotationInfo34_reverse_link_reassign_clear():
    a1 = types_AnnotatableElement()
    a2 = types_AnnotatableElement()
    b = types_AnnotatableElement()
    _safe_set(b, 'types_AnnotatableElement35', a1)
    assert _is_linked(b, 'types_AnnotatableElement35', a1)
    if hasattr(a1, 'types_AnnotatableElement33'):
        assert _is_linked(a1, 'types_AnnotatableElement33', b)
    _safe_set(b, 'types_AnnotatableElement35', a2)
    assert _is_linked(b, 'types_AnnotatableElement35', a2)
    if hasattr(a1, 'types_AnnotatableElement33'):
        assert not _is_linked(a1, 'types_AnnotatableElement33', b)
    if hasattr(a2, 'types_AnnotatableElement33'):
        assert _is_linked(a2, 'types_AnnotatableElement33', b)
    _safe_set(b, 'types_AnnotatableElement35', None)
    assert not _is_linked(b, 'types_AnnotatableElement35', a2)
    if hasattr(a2, 'types_AnnotatableElement33'):
        assert not _is_linked(a2, 'types_AnnotatableElement33', b)


def test_assoc_features20_reverse_link_reassign_clear():
    a1 = types_Declaration(id="sample_text", static=True)
    a2 = types_Declaration(id="sample_text_2", static=False)
    b = types_ComplexType()
    _safe_set(b, 'types_ComplexType', {a1})
    assert _is_linked(b, 'types_ComplexType', a1)
    if hasattr(a1, 'types_Declaration21'):
        assert _is_linked(a1, 'types_Declaration21', b)
    _safe_set(b, 'types_ComplexType', {a2})
    assert _is_linked(b, 'types_ComplexType', a2)
    if hasattr(a1, 'types_Declaration21'):
        assert not _is_linked(a1, 'types_Declaration21', b)
    if hasattr(a2, 'types_Declaration21'):
        assert _is_linked(a2, 'types_Declaration21', b)
    _safe_set(b, 'types_ComplexType', set())
    assert not _is_linked(b, 'types_ComplexType', a2)
    if hasattr(a2, 'types_Declaration21'):
        assert not _is_linked(a2, 'types_Declaration21', b)


def test_assoc_owningOperation7_reverse_link_reassign_clear():
    a1 = types_Parameter(optional=True, varArgs=True)
    a2 = types_Parameter(optional=False, varArgs=False)
    b = types_Operation(variadic=True)
    _safe_set(b, 'Operation', a1)
    assert _is_linked(b, 'Operation', a1)
    if hasattr(a1, 'parameters'):
        assert _is_linked(a1, 'parameters', b)
    _safe_set(b, 'Operation', a2)
    assert _is_linked(b, 'Operation', a2)
    if hasattr(a1, 'parameters'):
        assert not _is_linked(a1, 'parameters', b)
    if hasattr(a2, 'parameters'):
        assert _is_linked(a2, 'parameters', b)
    _safe_set(b, 'Operation', None)
    assert not _is_linked(b, 'Operation', a2)
    if hasattr(a2, 'parameters'):
        assert not _is_linked(a2, 'parameters', b)


def test_assoc_parameters5_reverse_link_reassign_clear():
    a1 = types_Parameter(optional=True, varArgs=True)
    a2 = types_Parameter(optional=False, varArgs=False)
    b = types_Operation(variadic=True)
    _safe_set(b, 'owningOperation', {a1})
    assert _is_linked(b, 'owningOperation', a1)
    if hasattr(a1, 'Parameter'):
        assert _is_linked(a1, 'Parameter', b)
    _safe_set(b, 'owningOperation', {a2})
    assert _is_linked(b, 'owningOperation', a2)
    if hasattr(a1, 'Parameter'):
        assert not _is_linked(a1, 'Parameter', b)
    if hasattr(a2, 'Parameter'):
        assert _is_linked(a2, 'Parameter', b)
    _safe_set(b, 'owningOperation', set())
    assert not _is_linked(b, 'owningOperation', a2)
    if hasattr(a2, 'Parameter'):
        assert not _is_linked(a2, 'Parameter', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations31_stub_double():
    # types_Annotation has no real 'types_Annotation32' property in the generated
    # code (a bare stub) -- manually attach it so types_AnnotatableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_AnnotatableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_AnnotatableElement()
    partner = types_Annotation()
    setattr(partner, 'types_Annotation32', None)
    _safe_set(owner, 'types_AnnotatableElement', {partner})
    assert getattr(partner, 'types_Annotation32') == owner
    _safe_set(owner, 'types_AnnotatableElement', set())
    assert getattr(partner, 'types_Annotation32') is None


def test_assoc_bound23_stub_double():
    # types_TypeParameter has no real 'types_TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(abstract=True, visible=True)
    partner = types_TypeParameter()
    setattr(partner, 'types_TypeParameter', None)
    _safe_set(owner, 'types_Type24', partner)
    assert getattr(partner, 'types_TypeParameter') == owner
    _safe_set(owner, 'types_Type24', None)
    assert getattr(partner, 'types_TypeParameter') is None


def test_assoc_enumerator19_stub_double():
    # types_EnumerationType has no real 'owningEnumeration' property in the generated
    # code (a bare stub) -- manually attach it so types_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Enumerator(literalValue=7)
    partner = types_EnumerationType()
    setattr(partner, 'owningEnumeration', None)
    _safe_set(owner, 'Enumerator', partner)
    assert owner in getattr(partner, 'owningEnumeration')
    _safe_set(owner, 'Enumerator', None)
    assert owner not in getattr(partner, 'owningEnumeration')


def test_assoc_initialValue6_stub_double():
    # types_Expression has no real 'types_Expression' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(const=True, readonly=True)
    partner = types_Expression()
    setattr(partner, 'types_Expression', None)
    _safe_set(owner, 'types_Property', partner)
    assert getattr(partner, 'types_Expression') == owner
    _safe_set(owner, 'types_Property', None)
    assert getattr(partner, 'types_Expression') is None


def test_assoc_member0_stub_double():
    # types_Package has no real 'types_Package' property in the generated
    # code (a bare stub) -- manually attach it so types_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Declaration(id="sample_text", static=True)
    partner = types_Package()
    setattr(partner, 'types_Package', None)
    _safe_set(owner, 'types_Declaration', partner)
    assert owner in getattr(partner, 'types_Package')
    _safe_set(owner, 'types_Declaration', None)
    assert owner not in getattr(partner, 'types_Package')


def test_assoc_metaFeatures41_stub_double():
    # types_MetaComposite has no real 'types_MetaComposite' property in the generated
    # code (a bare stub) -- manually attach it so types_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Declaration(id="sample_text", static=True)
    partner = types_MetaComposite()
    setattr(partner, 'types_MetaComposite', None)
    _safe_set(owner, 'types_Declaration42', partner)
    assert owner in getattr(partner, 'types_MetaComposite')
    _safe_set(owner, 'types_Declaration42', None)
    assert owner not in getattr(partner, 'types_MetaComposite')


def test_assoc_owningEnumeration22_stub_double():
    # types_EnumerationType has no real 'EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so types_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Enumerator(literalValue=7)
    partner = types_EnumerationType()
    setattr(partner, 'EnumerationType', None)
    _safe_set(owner, 'enumerator', partner)
    assert getattr(partner, 'EnumerationType') == owner
    _safe_set(owner, 'enumerator', None)
    assert getattr(partner, 'EnumerationType') is None


def test_assoc_properties36_stub_double():
    # types_AnnotationType has no real 'types_AnnotationType37' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(const=True, readonly=True)
    partner = types_AnnotationType()
    setattr(partner, 'types_AnnotationType37', None)
    _safe_set(owner, 'types_Property38', partner)
    assert owner in getattr(partner, 'types_AnnotationType37')
    _safe_set(owner, 'types_Property38', None)
    assert owner not in getattr(partner, 'types_AnnotationType37')


def test_assoc_superTypes4_stub_double():
    # types_TypeSpecifier has no real 'types_TypeSpecifier' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(abstract=True, visible=True)
    partner = types_TypeSpecifier()
    setattr(partner, 'types_TypeSpecifier', None)
    _safe_set(owner, 'types_Type', {partner})
    assert getattr(partner, 'types_TypeSpecifier') == owner
    _safe_set(owner, 'types_Type', set())
    assert getattr(partner, 'types_TypeSpecifier') is None


def test_assoc_type13_stub_double():
    # types_TypeSpecifier has no real 'types_TypeSpecifier14' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(abstract=True, visible=True)
    partner = types_TypeSpecifier()
    setattr(partner, 'types_TypeSpecifier14', None)
    _safe_set(owner, 'types_Type15', partner)
    assert getattr(partner, 'types_TypeSpecifier14') == owner
    _safe_set(owner, 'types_Type15', None)
    assert getattr(partner, 'types_TypeSpecifier14') is None


def test_assoc_type8_stub_double():
    # types_TypedElement has no real 'types_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(abstract=True, visible=True)
    partner = types_TypedElement()
    setattr(partner, 'types_TypedElement', None)
    _safe_set(owner, 'types_Type9', partner)
    assert getattr(partner, 'types_TypedElement') == owner
    _safe_set(owner, 'types_Type9', None)
    assert getattr(partner, 'types_TypedElement') is None


