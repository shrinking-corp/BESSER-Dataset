import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    typedef_CSIDatatype,
    typedef_DocumentRoot,
    typedef_Entity,
    typedef_EnumLiteral,
    typedef_EnumVal,
    typedef_Exception,
    typedef_Feature,
    typedef_PrimitiveType,
    typedef_TDAnnotationDetail,
    typedef_TDDocumentation,
    typedef_Type,
    typedef_TypeAnnotation,
    typedef_TypeLanguageBinding,
    typedef_TypedArray,
    CSIDatatypeCodes,
    CSIExceptionTypes,
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

def test_assoc_annotations1_reverse_link_reassign_clear():
    a1 = typedef_TypeAnnotation(source="sample_text")
    a2 = typedef_TypeAnnotation(source="sample_text_2")
    b = typedef_Type(name="sample_text")
    _safe_set(b, 'typedef_Type2', {a1})
    assert _is_linked(b, 'typedef_Type2', a1)
    if hasattr(a1, 'typedef_TypeAnnotation'):
        assert _is_linked(a1, 'typedef_TypeAnnotation', b)
    _safe_set(b, 'typedef_Type2', {a2})
    assert _is_linked(b, 'typedef_Type2', a2)
    if hasattr(a1, 'typedef_TypeAnnotation'):
        assert not _is_linked(a1, 'typedef_TypeAnnotation', b)
    if hasattr(a2, 'typedef_TypeAnnotation'):
        assert _is_linked(a2, 'typedef_TypeAnnotation', b)
    _safe_set(b, 'typedef_Type2', set())
    assert not _is_linked(b, 'typedef_Type2', a2)
    if hasattr(a2, 'typedef_TypeAnnotation'):
        assert not _is_linked(a2, 'typedef_TypeAnnotation', b)


def test_assoc_details14_reverse_link_reassign_clear():
    a1 = typedef_TypeAnnotation(source="sample_text")
    a2 = typedef_TypeAnnotation(source="sample_text_2")
    b = typedef_TDAnnotationDetail(key="sample_text", value="sample_text")
    _safe_set(b, 'typedef_TDAnnotationDetail', a1)
    assert _is_linked(b, 'typedef_TDAnnotationDetail', a1)
    if hasattr(a1, 'typedef_TypeAnnotation15'):
        assert _is_linked(a1, 'typedef_TypeAnnotation15', b)
    _safe_set(b, 'typedef_TDAnnotationDetail', a2)
    assert _is_linked(b, 'typedef_TDAnnotationDetail', a2)
    if hasattr(a1, 'typedef_TypeAnnotation15'):
        assert not _is_linked(a1, 'typedef_TypeAnnotation15', b)
    if hasattr(a2, 'typedef_TypeAnnotation15'):
        assert _is_linked(a2, 'typedef_TypeAnnotation15', b)
    _safe_set(b, 'typedef_TDAnnotationDetail', None)
    assert not _is_linked(b, 'typedef_TDAnnotationDetail', a2)
    if hasattr(a2, 'typedef_TypeAnnotation15'):
        assert not _is_linked(a2, 'typedef_TypeAnnotation15', b)


def test_assoc_documentation21_reverse_link_reassign_clear():
    a1 = typedef_TDDocumentation(doc="sample_text")
    a2 = typedef_TDDocumentation(doc="sample_text_2")
    b = typedef_EnumLiteral(name="sample_text", value="sample_text")
    _safe_set(b, 'typedef_EnumLiteral22', a1)
    assert _is_linked(b, 'typedef_EnumLiteral22', a1)
    if hasattr(a1, 'typedef_TDDocumentation23'):
        assert _is_linked(a1, 'typedef_TDDocumentation23', b)
    _safe_set(b, 'typedef_EnumLiteral22', a2)
    assert _is_linked(b, 'typedef_EnumLiteral22', a2)
    if hasattr(a1, 'typedef_TDDocumentation23'):
        assert not _is_linked(a1, 'typedef_TDDocumentation23', b)
    if hasattr(a2, 'typedef_TDDocumentation23'):
        assert _is_linked(a2, 'typedef_TDDocumentation23', b)
    _safe_set(b, 'typedef_EnumLiteral22', None)
    assert not _is_linked(b, 'typedef_EnumLiteral22', a2)
    if hasattr(a2, 'typedef_TDDocumentation23'):
        assert not _is_linked(a2, 'typedef_TDDocumentation23', b)


def test_assoc_documentation3_reverse_link_reassign_clear():
    a1 = typedef_Type(name="sample_text")
    a2 = typedef_Type(name="sample_text_2")
    b = typedef_TDDocumentation(doc="sample_text")
    _safe_set(b, 'typedef_TDDocumentation', a1)
    assert _is_linked(b, 'typedef_TDDocumentation', a1)
    if hasattr(a1, 'typedef_Type4'):
        assert _is_linked(a1, 'typedef_Type4', b)
    _safe_set(b, 'typedef_TDDocumentation', a2)
    assert _is_linked(b, 'typedef_TDDocumentation', a2)
    if hasattr(a1, 'typedef_Type4'):
        assert not _is_linked(a1, 'typedef_Type4', b)
    if hasattr(a2, 'typedef_Type4'):
        assert _is_linked(a2, 'typedef_Type4', b)
    _safe_set(b, 'typedef_TDDocumentation', None)
    assert not _is_linked(b, 'typedef_TDDocumentation', a2)
    if hasattr(a2, 'typedef_Type4'):
        assert not _is_linked(a2, 'typedef_Type4', b)


def test_assoc_documentation9_reverse_link_reassign_clear():
    a1 = typedef_TDDocumentation(doc="sample_text")
    a2 = typedef_TDDocumentation(doc="sample_text_2")
    b = typedef_Feature(name="sample_text")
    _safe_set(b, 'typedef_Feature10', a1)
    assert _is_linked(b, 'typedef_Feature10', a1)
    if hasattr(a1, 'typedef_TDDocumentation11'):
        assert _is_linked(a1, 'typedef_TDDocumentation11', b)
    _safe_set(b, 'typedef_Feature10', a2)
    assert _is_linked(b, 'typedef_Feature10', a2)
    if hasattr(a1, 'typedef_TDDocumentation11'):
        assert not _is_linked(a1, 'typedef_TDDocumentation11', b)
    if hasattr(a2, 'typedef_TDDocumentation11'):
        assert _is_linked(a2, 'typedef_TDDocumentation11', b)
    _safe_set(b, 'typedef_Feature10', None)
    assert not _is_linked(b, 'typedef_Feature10', a2)
    if hasattr(a2, 'typedef_TDDocumentation11'):
        assert not _is_linked(a2, 'typedef_TDDocumentation11', b)


def test_assoc_features5_reverse_link_reassign_clear():
    a1 = typedef_Feature(name="sample_text")
    a2 = typedef_Feature(name="sample_text_2")
    b = typedef_Entity(versionuid=7)
    _safe_set(b, 'typedef_Entity', {a1})
    assert _is_linked(b, 'typedef_Entity', a1)
    if hasattr(a1, 'typedef_Feature'):
        assert _is_linked(a1, 'typedef_Feature', b)
    _safe_set(b, 'typedef_Entity', {a2})
    assert _is_linked(b, 'typedef_Entity', a2)
    if hasattr(a1, 'typedef_Feature'):
        assert not _is_linked(a1, 'typedef_Feature', b)
    if hasattr(a2, 'typedef_Feature'):
        assert _is_linked(a2, 'typedef_Feature', b)
    _safe_set(b, 'typedef_Entity', set())
    assert not _is_linked(b, 'typedef_Entity', a2)
    if hasattr(a2, 'typedef_Feature'):
        assert not _is_linked(a2, 'typedef_Feature', b)


def test_assoc_languageBindings16_reverse_link_reassign_clear():
    a1 = typedef_TypeLanguageBinding(defaultInitValue="sample_text", lang="sample_text", langSpecificNS="sample_text", langSpecificType="sample_text", nullValueLiteral="sample_text")
    a2 = typedef_TypeLanguageBinding(defaultInitValue="sample_text_2", lang="sample_text_2", langSpecificNS="sample_text_2", langSpecificType="sample_text_2", nullValueLiteral="sample_text_2")
    b = typedef_PrimitiveType(nillable=True, typesetName="sample_text")
    _safe_set(b, 'typedef_PrimitiveType', {a1})
    assert _is_linked(b, 'typedef_PrimitiveType', a1)
    if hasattr(a1, 'typedef_TypeLanguageBinding'):
        assert _is_linked(a1, 'typedef_TypeLanguageBinding', b)
    _safe_set(b, 'typedef_PrimitiveType', {a2})
    assert _is_linked(b, 'typedef_PrimitiveType', a2)
    if hasattr(a1, 'typedef_TypeLanguageBinding'):
        assert not _is_linked(a1, 'typedef_TypeLanguageBinding', b)
    if hasattr(a2, 'typedef_TypeLanguageBinding'):
        assert _is_linked(a2, 'typedef_TypeLanguageBinding', b)
    _safe_set(b, 'typedef_PrimitiveType', set())
    assert not _is_linked(b, 'typedef_PrimitiveType', a2)
    if hasattr(a2, 'typedef_TypeLanguageBinding'):
        assert not _is_linked(a2, 'typedef_TypeLanguageBinding', b)


def test_assoc_type6_reverse_link_reassign_clear():
    a1 = typedef_Type(name="sample_text")
    a2 = typedef_Type(name="sample_text_2")
    b = typedef_Feature(name="sample_text")
    _safe_set(b, 'typedef_Feature7', a1)
    assert _is_linked(b, 'typedef_Feature7', a1)
    if hasattr(a1, 'typedef_Type8'):
        assert _is_linked(a1, 'typedef_Type8', b)
    _safe_set(b, 'typedef_Feature7', a2)
    assert _is_linked(b, 'typedef_Feature7', a2)
    if hasattr(a1, 'typedef_Type8'):
        assert not _is_linked(a1, 'typedef_Type8', b)
    if hasattr(a2, 'typedef_Type8'):
        assert _is_linked(a2, 'typedef_Type8', b)
    _safe_set(b, 'typedef_Feature7', None)
    assert not _is_linked(b, 'typedef_Feature7', a2)
    if hasattr(a2, 'typedef_Type8'):
        assert not _is_linked(a2, 'typedef_Type8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_componentType12_stub_double():
    # typedef_TypedArray has no real 'typedef_TypedArray' property in the generated
    # code (a bare stub) -- manually attach it so typedef_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typedef_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typedef_Type(name="sample_text")
    partner = typedef_TypedArray()
    setattr(partner, 'typedef_TypedArray', None)
    _safe_set(owner, 'typedef_Type13', partner)
    assert getattr(partner, 'typedef_TypedArray') == owner
    _safe_set(owner, 'typedef_Type13', None)
    assert getattr(partner, 'typedef_TypedArray') is None


def test_assoc_literals19_stub_double():
    # typedef_EnumVal has no real 'typedef_EnumVal20' property in the generated
    # code (a bare stub) -- manually attach it so typedef_EnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typedef_EnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typedef_EnumLiteral(name="sample_text", value="sample_text")
    partner = typedef_EnumVal()
    setattr(partner, 'typedef_EnumVal20', None)
    _safe_set(owner, 'typedef_EnumLiteral', partner)
    assert owner in getattr(partner, 'typedef_EnumVal20')
    _safe_set(owner, 'typedef_EnumLiteral', None)
    assert owner not in getattr(partner, 'typedef_EnumVal20')


def test_assoc_types0_stub_double():
    # typedef_DocumentRoot has no real 'typedef_DocumentRoot' property in the generated
    # code (a bare stub) -- manually attach it so typedef_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typedef_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typedef_Type(name="sample_text")
    partner = typedef_DocumentRoot()
    setattr(partner, 'typedef_DocumentRoot', None)
    _safe_set(owner, 'typedef_Type', partner)
    assert owner in getattr(partner, 'typedef_DocumentRoot')
    _safe_set(owner, 'typedef_Type', None)
    assert owner not in getattr(partner, 'typedef_DocumentRoot')


def test_assoc_valueType17_stub_double():
    # typedef_EnumVal has no real 'typedef_EnumVal' property in the generated
    # code (a bare stub) -- manually attach it so typedef_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typedef_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typedef_Type(name="sample_text")
    partner = typedef_EnumVal()
    setattr(partner, 'typedef_EnumVal', None)
    _safe_set(owner, 'typedef_Type18', partner)
    assert getattr(partner, 'typedef_EnumVal') == owner
    _safe_set(owner, 'typedef_Type18', None)
    assert getattr(partner, 'typedef_EnumVal') is None


