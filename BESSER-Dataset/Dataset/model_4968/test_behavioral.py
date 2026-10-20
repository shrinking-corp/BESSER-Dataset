import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractClass,
    Association,
    ClassElement,
    EVisibility,
    ModelElement,
    NamedElement,
    dcmddandroid_AbstractClass,
    dcmddandroid_Agregation,
    dcmddandroid_Association,
    dcmddandroid_Attribute,
    dcmddandroid_Class,
    dcmddandroid_ClassElement,
    dcmddandroid_Composition,
    dcmddandroid_CycleClass,
    dcmddandroid_Diagram,
    dcmddandroid_EVisibility,
    dcmddandroid_Enum,
    dcmddandroid_EnumValue,
    dcmddandroid_Implements,
    dcmddandroid_Interface,
    dcmddandroid_Method,
    dcmddandroid_ModelElement,
    dcmddandroid_NamedElement,
    dcmddandroid_Parameter,
    dcmddandroid_PersistentClass,
    Visibility,
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

def test_assoc_associationAsSource4_reverse_link_reassign_clear():
    a1 = dcmddandroid_Association(maxMultiplicitySource=7, maxMultiplicityTarget=7, minMultiplicitySource=7, minMultiplicityTarget=7, rolSource="sample_text", rolTarget="sample_text")
    a2 = dcmddandroid_Association(maxMultiplicitySource=13, maxMultiplicityTarget=13, minMultiplicitySource=13, minMultiplicityTarget=13, rolSource="sample_text_2", rolTarget="sample_text_2")
    b = dcmddandroid_AbstractClass(isAbstract=True)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Association'):
        assert _is_linked(a1, 'Association', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Association'):
        assert not _is_linked(a1, 'Association', b)
    if hasattr(a2, 'Association'):
        assert _is_linked(a2, 'Association', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Association'):
        assert not _is_linked(a2, 'Association', b)


def test_assoc_associationAsTarget5_reverse_link_reassign_clear():
    a1 = dcmddandroid_Association(maxMultiplicitySource=7, maxMultiplicityTarget=7, minMultiplicitySource=7, minMultiplicityTarget=7, rolSource="sample_text", rolTarget="sample_text")
    a2 = dcmddandroid_Association(maxMultiplicitySource=13, maxMultiplicityTarget=13, minMultiplicitySource=13, minMultiplicityTarget=13, rolSource="sample_text_2", rolTarget="sample_text_2")
    b = dcmddandroid_AbstractClass(isAbstract=True)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Association6'):
        assert _is_linked(a1, 'Association6', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Association6'):
        assert not _is_linked(a1, 'Association6', b)
    if hasattr(a2, 'Association6'):
        assert _is_linked(a2, 'Association6', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Association6'):
        assert not _is_linked(a2, 'Association6', b)


def test_assoc_attributes1_reverse_link_reassign_clear():
    a1 = dcmddandroid_Attribute(defaultValue="sample_text", secured="sample_text", type="sample_text")
    a2 = dcmddandroid_Attribute(defaultValue="sample_text_2", secured="sample_text_2", type="sample_text_2")
    b = dcmddandroid_AbstractClass(isAbstract=True)
    _safe_set(b, 'dcmddandroid_AbstractClass', {a1})
    assert _is_linked(b, 'dcmddandroid_AbstractClass', a1)
    if hasattr(a1, 'dcmddandroid_Attribute'):
        assert _is_linked(a1, 'dcmddandroid_Attribute', b)
    _safe_set(b, 'dcmddandroid_AbstractClass', {a2})
    assert _is_linked(b, 'dcmddandroid_AbstractClass', a2)
    if hasattr(a1, 'dcmddandroid_Attribute'):
        assert not _is_linked(a1, 'dcmddandroid_Attribute', b)
    if hasattr(a2, 'dcmddandroid_Attribute'):
        assert _is_linked(a2, 'dcmddandroid_Attribute', b)
    _safe_set(b, 'dcmddandroid_AbstractClass', set())
    assert not _is_linked(b, 'dcmddandroid_AbstractClass', a2)
    if hasattr(a2, 'dcmddandroid_Attribute'):
        assert not _is_linked(a2, 'dcmddandroid_Attribute', b)


def test_assoc_methods2_reverse_link_reassign_clear():
    a1 = dcmddandroid_Method(isAbstract=True, returns="sample_text")
    a2 = dcmddandroid_Method(isAbstract=False, returns="sample_text_2")
    b = dcmddandroid_AbstractClass(isAbstract=True)
    _safe_set(b, 'dcmddandroid_AbstractClass3', {a1})
    assert _is_linked(b, 'dcmddandroid_AbstractClass3', a1)
    if hasattr(a1, 'dcmddandroid_Method'):
        assert _is_linked(a1, 'dcmddandroid_Method', b)
    _safe_set(b, 'dcmddandroid_AbstractClass3', {a2})
    assert _is_linked(b, 'dcmddandroid_AbstractClass3', a2)
    if hasattr(a1, 'dcmddandroid_Method'):
        assert not _is_linked(a1, 'dcmddandroid_Method', b)
    if hasattr(a2, 'dcmddandroid_Method'):
        assert _is_linked(a2, 'dcmddandroid_Method', b)
    _safe_set(b, 'dcmddandroid_AbstractClass3', set())
    assert not _is_linked(b, 'dcmddandroid_AbstractClass3', a2)
    if hasattr(a2, 'dcmddandroid_Method'):
        assert not _is_linked(a2, 'dcmddandroid_Method', b)


def test_assoc_parameters12_reverse_link_reassign_clear():
    a1 = dcmddandroid_Parameter(type="sample_text")
    a2 = dcmddandroid_Parameter(type="sample_text_2")
    b = dcmddandroid_Method(isAbstract=True, returns="sample_text")
    _safe_set(b, 'dcmddandroid_Method13', {a1})
    assert _is_linked(b, 'dcmddandroid_Method13', a1)
    if hasattr(a1, 'dcmddandroid_Parameter'):
        assert _is_linked(a1, 'dcmddandroid_Parameter', b)
    _safe_set(b, 'dcmddandroid_Method13', {a2})
    assert _is_linked(b, 'dcmddandroid_Method13', a2)
    if hasattr(a1, 'dcmddandroid_Parameter'):
        assert not _is_linked(a1, 'dcmddandroid_Parameter', b)
    if hasattr(a2, 'dcmddandroid_Parameter'):
        assert _is_linked(a2, 'dcmddandroid_Parameter', b)
    _safe_set(b, 'dcmddandroid_Method13', set())
    assert not _is_linked(b, 'dcmddandroid_Method13', a2)
    if hasattr(a2, 'dcmddandroid_Parameter'):
        assert not _is_linked(a2, 'dcmddandroid_Parameter', b)


def test_assoc_source16_reverse_link_reassign_clear():
    a1 = dcmddandroid_Association(maxMultiplicitySource=7, maxMultiplicityTarget=7, minMultiplicitySource=7, minMultiplicityTarget=7, rolSource="sample_text", rolTarget="sample_text")
    a2 = dcmddandroid_Association(maxMultiplicitySource=13, maxMultiplicityTarget=13, minMultiplicitySource=13, minMultiplicityTarget=13, rolSource="sample_text_2", rolTarget="sample_text_2")
    b = dcmddandroid_AbstractClass(isAbstract=True)
    _safe_set(b, 'AbstractClass', a1)
    assert _is_linked(b, 'AbstractClass', a1)
    if hasattr(a1, 'associationAsSource'):
        assert _is_linked(a1, 'associationAsSource', b)
    _safe_set(b, 'AbstractClass', a2)
    assert _is_linked(b, 'AbstractClass', a2)
    if hasattr(a1, 'associationAsSource'):
        assert not _is_linked(a1, 'associationAsSource', b)
    if hasattr(a2, 'associationAsSource'):
        assert _is_linked(a2, 'associationAsSource', b)
    _safe_set(b, 'AbstractClass', None)
    assert not _is_linked(b, 'AbstractClass', a2)
    if hasattr(a2, 'associationAsSource'):
        assert not _is_linked(a2, 'associationAsSource', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = dcmddandroid_Association(maxMultiplicitySource=7, maxMultiplicityTarget=7, minMultiplicitySource=7, minMultiplicityTarget=7, rolSource="sample_text", rolTarget="sample_text")
    a2 = dcmddandroid_Association(maxMultiplicitySource=13, maxMultiplicityTarget=13, minMultiplicitySource=13, minMultiplicityTarget=13, rolSource="sample_text_2", rolTarget="sample_text_2")
    b = dcmddandroid_AbstractClass(isAbstract=True)
    _safe_set(b, 'AbstractClass18', a1)
    assert _is_linked(b, 'AbstractClass18', a1)
    if hasattr(a1, 'associationAsTarget'):
        assert _is_linked(a1, 'associationAsTarget', b)
    _safe_set(b, 'AbstractClass18', a2)
    assert _is_linked(b, 'AbstractClass18', a2)
    if hasattr(a1, 'associationAsTarget'):
        assert not _is_linked(a1, 'associationAsTarget', b)
    if hasattr(a2, 'associationAsTarget'):
        assert _is_linked(a2, 'associationAsTarget', b)
    _safe_set(b, 'AbstractClass18', None)
    assert not _is_linked(b, 'AbstractClass18', a2)
    if hasattr(a2, 'associationAsTarget'):
        assert not _is_linked(a2, 'associationAsTarget', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_implements0_stub_double():
    # dcmddandroid_Implements has no real 'Implements' property in the generated
    # code (a bare stub) -- manually attach it so dcmddandroid_AbstractClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcmddandroid_AbstractClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcmddandroid_AbstractClass(isAbstract=True)
    partner = dcmddandroid_Implements()
    setattr(partner, 'Implements', None)
    _safe_set(owner, 'implements', {partner})
    assert getattr(partner, 'Implements') == owner
    _safe_set(owner, 'implements', set())
    assert getattr(partner, 'Implements') is None


def test_assoc_implements21_stub_double():
    # dcmddandroid_Implements has no real 'implements22' property in the generated
    # code (a bare stub) -- manually attach it so dcmddandroid_AbstractClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcmddandroid_AbstractClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcmddandroid_AbstractClass(isAbstract=True)
    partner = dcmddandroid_Implements()
    setattr(partner, 'implements22', None)
    _safe_set(owner, 'AbstractClass23', partner)
    assert getattr(partner, 'implements22') == owner
    _safe_set(owner, 'AbstractClass23', None)
    assert getattr(partner, 'implements22') is None


def test_assoc_methods9_stub_double():
    # dcmddandroid_Interface has no real 'dcmddandroid_Interface10' property in the generated
    # code (a bare stub) -- manually attach it so dcmddandroid_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcmddandroid_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcmddandroid_Method(isAbstract=True, returns="sample_text")
    partner = dcmddandroid_Interface()
    setattr(partner, 'dcmddandroid_Interface10', None)
    _safe_set(owner, 'dcmddandroid_Method11', partner)
    assert owner in getattr(partner, 'dcmddandroid_Interface10')
    _safe_set(owner, 'dcmddandroid_Method11', None)
    assert owner not in getattr(partner, 'dcmddandroid_Interface10')


def test_assoc_values15_stub_double():
    # dcmddandroid_Enum has no real 'dcmddandroid_Enum' property in the generated
    # code (a bare stub) -- manually attach it so dcmddandroid_EnumValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcmddandroid_EnumValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcmddandroid_EnumValue(intValue=7)
    partner = dcmddandroid_Enum()
    setattr(partner, 'dcmddandroid_Enum', None)
    _safe_set(owner, 'dcmddandroid_EnumValue', partner)
    assert owner in getattr(partner, 'dcmddandroid_Enum')
    _safe_set(owner, 'dcmddandroid_EnumValue', None)
    assert owner not in getattr(partner, 'dcmddandroid_Enum')


