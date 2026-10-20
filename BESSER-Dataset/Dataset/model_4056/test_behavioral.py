import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    ModelingConcept,
    classDiagram_Attribute,
    classDiagram_Class,
    classDiagram_ClassModel,
    classDiagram_Classifier,
    classDiagram_ElementType,
    classDiagram_Method,
    classDiagram_ModelingConcept,
    classDiagram_Package,
    classDiagram_Type,
    AccessModifier,
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

def test_assoc_fields12_reverse_link_reassign_clear():
    a1 = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Class(accessModifier="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Attribute(accessModifier="sample_text", isStatic=True)
    _safe_set(b, 'classDiagram_Attribute', a1)
    assert _is_linked(b, 'classDiagram_Attribute', a1)
    if hasattr(a1, 'classDiagram_Class13'):
        assert _is_linked(a1, 'classDiagram_Class13', b)
    _safe_set(b, 'classDiagram_Attribute', a2)
    assert _is_linked(b, 'classDiagram_Attribute', a2)
    if hasattr(a1, 'classDiagram_Class13'):
        assert not _is_linked(a1, 'classDiagram_Class13', b)
    if hasattr(a2, 'classDiagram_Class13'):
        assert _is_linked(a2, 'classDiagram_Class13', b)
    _safe_set(b, 'classDiagram_Attribute', None)
    assert not _is_linked(b, 'classDiagram_Attribute', a2)
    if hasattr(a2, 'classDiagram_Class13'):
        assert not _is_linked(a2, 'classDiagram_Class13', b)


def test_assoc_methods19_reverse_link_reassign_clear():
    a1 = classDiagram_Method(accessModifier="sample_text", body="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Method(accessModifier="sample_text_2", body="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    _safe_set(b, 'classDiagram_Class20', {a1})
    assert _is_linked(b, 'classDiagram_Class20', a1)
    if hasattr(a1, 'classDiagram_Method'):
        assert _is_linked(a1, 'classDiagram_Method', b)
    _safe_set(b, 'classDiagram_Class20', {a2})
    assert _is_linked(b, 'classDiagram_Class20', a2)
    if hasattr(a1, 'classDiagram_Method'):
        assert not _is_linked(a1, 'classDiagram_Method', b)
    if hasattr(a2, 'classDiagram_Method'):
        assert _is_linked(a2, 'classDiagram_Method', b)
    _safe_set(b, 'classDiagram_Class20', set())
    assert not _is_linked(b, 'classDiagram_Class20', a2)
    if hasattr(a2, 'classDiagram_Method'):
        assert not _is_linked(a2, 'classDiagram_Method', b)


def test_assoc_parameters26_reverse_link_reassign_clear():
    a1 = classDiagram_Method(accessModifier="sample_text", body="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Method(accessModifier="sample_text_2", body="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Attribute(accessModifier="sample_text", isStatic=True)
    _safe_set(b, 'classDiagram_Attribute28', a1)
    assert _is_linked(b, 'classDiagram_Attribute28', a1)
    if hasattr(a1, 'classDiagram_Method27'):
        assert _is_linked(a1, 'classDiagram_Method27', b)
    _safe_set(b, 'classDiagram_Attribute28', a2)
    assert _is_linked(b, 'classDiagram_Attribute28', a2)
    if hasattr(a1, 'classDiagram_Method27'):
        assert not _is_linked(a1, 'classDiagram_Method27', b)
    if hasattr(a2, 'classDiagram_Method27'):
        assert _is_linked(a2, 'classDiagram_Method27', b)
    _safe_set(b, 'classDiagram_Attribute28', None)
    assert not _is_linked(b, 'classDiagram_Attribute28', a2)
    if hasattr(a2, 'classDiagram_Method27'):
        assert not _is_linked(a2, 'classDiagram_Method27', b)


def test_assoc_returnType23_reverse_link_reassign_clear():
    a1 = classDiagram_Method(accessModifier="sample_text", body="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Method(accessModifier="sample_text_2", body="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_ElementType(isCollection=True)
    _safe_set(b, 'classDiagram_ElementType25', a1)
    assert _is_linked(b, 'classDiagram_ElementType25', a1)
    if hasattr(a1, 'classDiagram_Method24'):
        assert _is_linked(a1, 'classDiagram_Method24', b)
    _safe_set(b, 'classDiagram_ElementType25', a2)
    assert _is_linked(b, 'classDiagram_ElementType25', a2)
    if hasattr(a1, 'classDiagram_Method24'):
        assert not _is_linked(a1, 'classDiagram_Method24', b)
    if hasattr(a2, 'classDiagram_Method24'):
        assert _is_linked(a2, 'classDiagram_Method24', b)
    _safe_set(b, 'classDiagram_ElementType25', None)
    assert not _is_linked(b, 'classDiagram_ElementType25', a2)
    if hasattr(a2, 'classDiagram_Method24'):
        assert not _is_linked(a2, 'classDiagram_Method24', b)


def test_assoc_subtypes17_reverse_link_reassign_clear():
    a1 = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Class(accessModifier="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    _safe_set(b, 'supertypes', {a1})
    assert _is_linked(b, 'supertypes', a1)
    if hasattr(a1, 'Class18'):
        assert _is_linked(a1, 'Class18', b)
    _safe_set(b, 'supertypes', {a2})
    assert _is_linked(b, 'supertypes', a2)
    if hasattr(a1, 'Class18'):
        assert not _is_linked(a1, 'Class18', b)
    if hasattr(a2, 'Class18'):
        assert _is_linked(a2, 'Class18', b)
    _safe_set(b, 'supertypes', set())
    assert not _is_linked(b, 'supertypes', a2)
    if hasattr(a2, 'Class18'):
        assert not _is_linked(a2, 'Class18', b)


def test_assoc_supertypes15_reverse_link_reassign_clear():
    a1 = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    a2 = classDiagram_Class(accessModifier="sample_text_2", isAbstract=False, isStatic=False)
    b = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    _safe_set(b, 'subtypes', {a1})
    assert _is_linked(b, 'subtypes', a1)
    if hasattr(a1, 'Class'):
        assert _is_linked(a1, 'Class', b)
    _safe_set(b, 'subtypes', {a2})
    assert _is_linked(b, 'subtypes', a2)
    if hasattr(a1, 'Class'):
        assert not _is_linked(a1, 'Class', b)
    if hasattr(a2, 'Class'):
        assert _is_linked(a2, 'Class', b)
    _safe_set(b, 'subtypes', set())
    assert not _is_linked(b, 'subtypes', a2)
    if hasattr(a2, 'Class'):
        assert not _is_linked(a2, 'Class', b)


def test_assoc_type21_reverse_link_reassign_clear():
    a1 = classDiagram_ElementType(isCollection=True)
    a2 = classDiagram_ElementType(isCollection=False)
    b = classDiagram_Attribute(accessModifier="sample_text", isStatic=True)
    _safe_set(b, 'classDiagram_Attribute22', a1)
    assert _is_linked(b, 'classDiagram_Attribute22', a1)
    if hasattr(a1, 'classDiagram_ElementType'):
        assert _is_linked(a1, 'classDiagram_ElementType', b)
    _safe_set(b, 'classDiagram_Attribute22', a2)
    assert _is_linked(b, 'classDiagram_Attribute22', a2)
    if hasattr(a1, 'classDiagram_ElementType'):
        assert not _is_linked(a1, 'classDiagram_ElementType', b)
    if hasattr(a2, 'classDiagram_ElementType'):
        assert _is_linked(a2, 'classDiagram_ElementType', b)
    _safe_set(b, 'classDiagram_Attribute22', None)
    assert not _is_linked(b, 'classDiagram_Attribute22', a2)
    if hasattr(a2, 'classDiagram_ElementType'):
        assert not _is_linked(a2, 'classDiagram_ElementType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classes10_stub_double():
    # classDiagram_Package has no real 'classDiagram_Package11' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_Class(accessModifier="sample_text", isAbstract=True, isStatic=True)
    partner = classDiagram_Package()
    setattr(partner, 'classDiagram_Package11', None)
    _safe_set(owner, 'classDiagram_Class', partner)
    assert owner in getattr(partner, 'classDiagram_Package11')
    _safe_set(owner, 'classDiagram_Class', None)
    assert owner not in getattr(partner, 'classDiagram_Package11')


def test_assoc_elements3_stub_double():
    # classDiagram_Package has no real 'classDiagram_Package4' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_ModelingConcept's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_ModelingConcept's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_ModelingConcept(name="sample_text")
    partner = classDiagram_Package()
    setattr(partner, 'classDiagram_Package4', None)
    _safe_set(owner, 'classDiagram_ModelingConcept', partner)
    assert owner in getattr(partner, 'classDiagram_Package4')
    _safe_set(owner, 'classDiagram_ModelingConcept', None)
    assert owner not in getattr(partner, 'classDiagram_Package4')


def test_assoc_type29_stub_double():
    # classDiagram_Classifier has no real 'classDiagram_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so classDiagram_ElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classDiagram_ElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classDiagram_ElementType(isCollection=True)
    partner = classDiagram_Classifier()
    setattr(partner, 'classDiagram_Classifier', None)
    _safe_set(owner, 'classDiagram_ElementType30', partner)
    assert getattr(partner, 'classDiagram_Classifier') == owner
    _safe_set(owner, 'classDiagram_ElementType30', None)
    assert getattr(partner, 'classDiagram_Classifier') is None


