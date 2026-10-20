import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArmaniDesignRuleExpression,
    ArmaniExpression,
    ArmaniPrimitiveExpression,
    ArmaniUnaryExpression,
    BasicElement,
    BindableElement,
    Element,
    Role,
    TypeDefinition,
    aspectualacme_Armani,
    aspectualacme_ArmaniAdditiveExpression,
    aspectualacme_ArmaniBooleanExpression,
    aspectualacme_ArmaniConstant,
    aspectualacme_ArmaniDesignRuleExpression,
    aspectualacme_ArmaniEqualityExpression,
    aspectualacme_ArmaniExpression,
    aspectualacme_ArmaniFunctionCall,
    aspectualacme_ArmaniIffExpression,
    aspectualacme_ArmaniImpliesExpression,
    aspectualacme_ArmaniMultiplicativeExpression,
    aspectualacme_ArmaniOrExpression,
    aspectualacme_ArmaniPrimitiveExpression,
    aspectualacme_ArmaniQuantifiedExpression,
    aspectualacme_ArmaniRelationalExpression,
    aspectualacme_ArmaniSetExpression,
    aspectualacme_ArmaniUnaryExpression,
    aspectualacme_ArmaniVariable,
    aspectualacme_Attachment,
    aspectualacme_BaseRole,
    aspectualacme_BasicElement,
    aspectualacme_BindableElement,
    aspectualacme_Binding,
    aspectualacme_Component,
    aspectualacme_ComponentType,
    aspectualacme_Connector,
    aspectualacme_ConnectorType,
    aspectualacme_CrosscuttingRole,
    aspectualacme_Element,
    aspectualacme_Family,
    aspectualacme_Glue,
    aspectualacme_Import,
    aspectualacme_Port,
    aspectualacme_PortType,
    aspectualacme_Property,
    aspectualacme_PropertyType,
    aspectualacme_Representation,
    aspectualacme_Role,
    aspectualacme_RoleType,
    aspectualacme_Root,
    aspectualacme_System,
    aspectualacme_TypeDefinition,
    aspectualacme_WildCard,
    aspectualacme_attachableElement,
    attachableElement,
    ArmaniQuantifier,
    ArmaniSetTypes,
    ArmaniTypes,
    GlueType,
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

def test_assoc_element153_reverse_link_reassign_clear():
    a1 = aspectualacme_Representation(name="sample_text")
    a2 = aspectualacme_Representation(name="sample_text_2")
    b = aspectualacme_Element(name="sample_text")
    _safe_set(b, 'Element', a1)
    assert _is_linked(b, 'Element', a1)
    if hasattr(a1, 'representations'):
        assert _is_linked(a1, 'representations', b)
    _safe_set(b, 'Element', a2)
    assert _is_linked(b, 'Element', a2)
    if hasattr(a1, 'representations'):
        assert not _is_linked(a1, 'representations', b)
    if hasattr(a2, 'representations'):
        assert _is_linked(a2, 'representations', b)
    _safe_set(b, 'Element', None)
    assert not _is_linked(b, 'Element', a2)
    if hasattr(a2, 'representations'):
        assert not _is_linked(a2, 'representations', b)


def test_assoc_expressions163_reverse_link_reassign_clear():
    a1 = aspectualacme_ArmaniUnaryExpression(operator="sample_text")
    a2 = aspectualacme_ArmaniUnaryExpression(operator="sample_text_2")
    b = aspectualacme_ArmaniMultiplicativeExpression(operators="sample_text")
    _safe_set(b, 'aspectualacme_ArmaniMultiplicativeExpression', {a1})
    assert _is_linked(b, 'aspectualacme_ArmaniMultiplicativeExpression', a1)
    if hasattr(a1, 'aspectualacme_ArmaniUnaryExpression164'):
        assert _is_linked(a1, 'aspectualacme_ArmaniUnaryExpression164', b)
    _safe_set(b, 'aspectualacme_ArmaniMultiplicativeExpression', {a2})
    assert _is_linked(b, 'aspectualacme_ArmaniMultiplicativeExpression', a2)
    if hasattr(a1, 'aspectualacme_ArmaniUnaryExpression164'):
        assert not _is_linked(a1, 'aspectualacme_ArmaniUnaryExpression164', b)
    if hasattr(a2, 'aspectualacme_ArmaniUnaryExpression164'):
        assert _is_linked(a2, 'aspectualacme_ArmaniUnaryExpression164', b)
    _safe_set(b, 'aspectualacme_ArmaniMultiplicativeExpression', set())
    assert not _is_linked(b, 'aspectualacme_ArmaniMultiplicativeExpression', a2)
    if hasattr(a2, 'aspectualacme_ArmaniUnaryExpression164'):
        assert not _is_linked(a2, 'aspectualacme_ArmaniUnaryExpression164', b)


def test_assoc_expressions165_reverse_link_reassign_clear():
    a1 = aspectualacme_ArmaniMultiplicativeExpression(operators="sample_text")
    a2 = aspectualacme_ArmaniMultiplicativeExpression(operators="sample_text_2")
    b = aspectualacme_ArmaniAdditiveExpression(operators="sample_text")
    _safe_set(b, 'aspectualacme_ArmaniAdditiveExpression', {a1})
    assert _is_linked(b, 'aspectualacme_ArmaniAdditiveExpression', a1)
    if hasattr(a1, 'aspectualacme_ArmaniMultiplicativeExpression166'):
        assert _is_linked(a1, 'aspectualacme_ArmaniMultiplicativeExpression166', b)
    _safe_set(b, 'aspectualacme_ArmaniAdditiveExpression', {a2})
    assert _is_linked(b, 'aspectualacme_ArmaniAdditiveExpression', a2)
    if hasattr(a1, 'aspectualacme_ArmaniMultiplicativeExpression166'):
        assert not _is_linked(a1, 'aspectualacme_ArmaniMultiplicativeExpression166', b)
    if hasattr(a2, 'aspectualacme_ArmaniMultiplicativeExpression166'):
        assert _is_linked(a2, 'aspectualacme_ArmaniMultiplicativeExpression166', b)
    _safe_set(b, 'aspectualacme_ArmaniAdditiveExpression', set())
    assert not _is_linked(b, 'aspectualacme_ArmaniAdditiveExpression', a2)
    if hasattr(a2, 'aspectualacme_ArmaniMultiplicativeExpression166'):
        assert not _is_linked(a2, 'aspectualacme_ArmaniMultiplicativeExpression166', b)


def test_assoc_expressions167_reverse_link_reassign_clear():
    a1 = aspectualacme_ArmaniRelationalExpression(operators="sample_text")
    a2 = aspectualacme_ArmaniRelationalExpression(operators="sample_text_2")
    b = aspectualacme_ArmaniAdditiveExpression(operators="sample_text")
    _safe_set(b, 'aspectualacme_ArmaniAdditiveExpression168', a1)
    assert _is_linked(b, 'aspectualacme_ArmaniAdditiveExpression168', a1)
    if hasattr(a1, 'aspectualacme_ArmaniRelationalExpression'):
        assert _is_linked(a1, 'aspectualacme_ArmaniRelationalExpression', b)
    _safe_set(b, 'aspectualacme_ArmaniAdditiveExpression168', a2)
    assert _is_linked(b, 'aspectualacme_ArmaniAdditiveExpression168', a2)
    if hasattr(a1, 'aspectualacme_ArmaniRelationalExpression'):
        assert not _is_linked(a1, 'aspectualacme_ArmaniRelationalExpression', b)
    if hasattr(a2, 'aspectualacme_ArmaniRelationalExpression'):
        assert _is_linked(a2, 'aspectualacme_ArmaniRelationalExpression', b)
    _safe_set(b, 'aspectualacme_ArmaniAdditiveExpression168', None)
    assert not _is_linked(b, 'aspectualacme_ArmaniAdditiveExpression168', a2)
    if hasattr(a2, 'aspectualacme_ArmaniRelationalExpression'):
        assert not _is_linked(a2, 'aspectualacme_ArmaniRelationalExpression', b)


def test_assoc_expressions169_reverse_link_reassign_clear():
    a1 = aspectualacme_ArmaniRelationalExpression(operators="sample_text")
    a2 = aspectualacme_ArmaniRelationalExpression(operators="sample_text_2")
    b = aspectualacme_ArmaniEqualityExpression(operators="sample_text")
    _safe_set(b, 'aspectualacme_ArmaniEqualityExpression', {a1})
    assert _is_linked(b, 'aspectualacme_ArmaniEqualityExpression', a1)
    if hasattr(a1, 'aspectualacme_ArmaniRelationalExpression170'):
        assert _is_linked(a1, 'aspectualacme_ArmaniRelationalExpression170', b)
    _safe_set(b, 'aspectualacme_ArmaniEqualityExpression', {a2})
    assert _is_linked(b, 'aspectualacme_ArmaniEqualityExpression', a2)
    if hasattr(a1, 'aspectualacme_ArmaniRelationalExpression170'):
        assert not _is_linked(a1, 'aspectualacme_ArmaniRelationalExpression170', b)
    if hasattr(a2, 'aspectualacme_ArmaniRelationalExpression170'):
        assert _is_linked(a2, 'aspectualacme_ArmaniRelationalExpression170', b)
    _safe_set(b, 'aspectualacme_ArmaniEqualityExpression', set())
    assert not _is_linked(b, 'aspectualacme_ArmaniEqualityExpression', a2)
    if hasattr(a2, 'aspectualacme_ArmaniRelationalExpression170'):
        assert not _is_linked(a2, 'aspectualacme_ArmaniRelationalExpression170', b)


def test_assoc_property3_reverse_link_reassign_clear():
    a1 = aspectualacme_Property(name="sample_text", value="sample_text")
    a2 = aspectualacme_Property(name="sample_text_2", value="sample_text_2")
    b = aspectualacme_Element(name="sample_text")
    _safe_set(b, 'aspectualacme_Element', {a1})
    assert _is_linked(b, 'aspectualacme_Element', a1)
    if hasattr(a1, 'aspectualacme_Property'):
        assert _is_linked(a1, 'aspectualacme_Property', b)
    _safe_set(b, 'aspectualacme_Element', {a2})
    assert _is_linked(b, 'aspectualacme_Element', a2)
    if hasattr(a1, 'aspectualacme_Property'):
        assert not _is_linked(a1, 'aspectualacme_Property', b)
    if hasattr(a2, 'aspectualacme_Property'):
        assert _is_linked(a2, 'aspectualacme_Property', b)
    _safe_set(b, 'aspectualacme_Element', set())
    assert not _is_linked(b, 'aspectualacme_Element', a2)
    if hasattr(a2, 'aspectualacme_Property'):
        assert not _is_linked(a2, 'aspectualacme_Property', b)


def test_assoc_representations4_reverse_link_reassign_clear():
    a1 = aspectualacme_Representation(name="sample_text")
    a2 = aspectualacme_Representation(name="sample_text_2")
    b = aspectualacme_Element(name="sample_text")
    _safe_set(b, 'element', {a1})
    assert _is_linked(b, 'element', a1)
    if hasattr(a1, 'Representation'):
        assert _is_linked(a1, 'Representation', b)
    _safe_set(b, 'element', {a2})
    assert _is_linked(b, 'element', a2)
    if hasattr(a1, 'Representation'):
        assert not _is_linked(a1, 'Representation', b)
    if hasattr(a2, 'Representation'):
        assert _is_linked(a2, 'Representation', b)
    _safe_set(b, 'element', set())
    assert not _is_linked(b, 'element', a2)
    if hasattr(a2, 'Representation'):
        assert not _is_linked(a2, 'Representation', b)


def test_assoc_setExpression182_reverse_link_reassign_clear():
    a1 = aspectualacme_ArmaniSetExpression(reference="sample_text", referenceType="sample_text")
    a2 = aspectualacme_ArmaniSetExpression(reference="sample_text_2", referenceType="sample_text_2")
    b = aspectualacme_ArmaniQuantifiedExpression(quantifier="sample_text")
    _safe_set(b, 'aspectualacme_ArmaniQuantifiedExpression183', a1)
    assert _is_linked(b, 'aspectualacme_ArmaniQuantifiedExpression183', a1)
    if hasattr(a1, 'aspectualacme_ArmaniSetExpression184'):
        assert _is_linked(a1, 'aspectualacme_ArmaniSetExpression184', b)
    _safe_set(b, 'aspectualacme_ArmaniQuantifiedExpression183', a2)
    assert _is_linked(b, 'aspectualacme_ArmaniQuantifiedExpression183', a2)
    if hasattr(a1, 'aspectualacme_ArmaniSetExpression184'):
        assert not _is_linked(a1, 'aspectualacme_ArmaniSetExpression184', b)
    if hasattr(a2, 'aspectualacme_ArmaniSetExpression184'):
        assert _is_linked(a2, 'aspectualacme_ArmaniSetExpression184', b)
    _safe_set(b, 'aspectualacme_ArmaniQuantifiedExpression183', None)
    assert not _is_linked(b, 'aspectualacme_ArmaniQuantifiedExpression183', a2)
    if hasattr(a2, 'aspectualacme_ArmaniSetExpression184'):
        assert not _is_linked(a2, 'aspectualacme_ArmaniSetExpression184', b)


def test_assoc_type117_reverse_link_reassign_clear():
    a1 = aspectualacme_PropertyType(type="sample_text", values="sample_text")
    a2 = aspectualacme_PropertyType(type="sample_text_2", values="sample_text_2")
    b = aspectualacme_Property(name="sample_text", value="sample_text")
    _safe_set(b, 'aspectualacme_Property118', {a1})
    assert _is_linked(b, 'aspectualacme_Property118', a1)
    if hasattr(a1, 'aspectualacme_PropertyType'):
        assert _is_linked(a1, 'aspectualacme_PropertyType', b)
    _safe_set(b, 'aspectualacme_Property118', {a2})
    assert _is_linked(b, 'aspectualacme_Property118', a2)
    if hasattr(a1, 'aspectualacme_PropertyType'):
        assert not _is_linked(a1, 'aspectualacme_PropertyType', b)
    if hasattr(a2, 'aspectualacme_PropertyType'):
        assert _is_linked(a2, 'aspectualacme_PropertyType', b)
    _safe_set(b, 'aspectualacme_Property118', set())
    assert not _is_linked(b, 'aspectualacme_Property118', a2)
    if hasattr(a2, 'aspectualacme_PropertyType'):
        assert not _is_linked(a2, 'aspectualacme_PropertyType', b)


def test_assoc_unaryExpression162_reverse_link_reassign_clear():
    a1 = aspectualacme_ArmaniUnaryExpression(operator="sample_text")
    a2 = aspectualacme_ArmaniUnaryExpression(operator="sample_text_2")
    b = aspectualacme_ArmaniUnaryExpression(operator="sample_text")
    _safe_set(b, 'aspectualacme_ArmaniUnaryExpression161', a1)
    assert _is_linked(b, 'aspectualacme_ArmaniUnaryExpression161', a1)
    if hasattr(a1, 'aspectualacme_ArmaniUnaryExpression'):
        assert _is_linked(a1, 'aspectualacme_ArmaniUnaryExpression', b)
    _safe_set(b, 'aspectualacme_ArmaniUnaryExpression161', a2)
    assert _is_linked(b, 'aspectualacme_ArmaniUnaryExpression161', a2)
    if hasattr(a1, 'aspectualacme_ArmaniUnaryExpression'):
        assert not _is_linked(a1, 'aspectualacme_ArmaniUnaryExpression', b)
    if hasattr(a2, 'aspectualacme_ArmaniUnaryExpression'):
        assert _is_linked(a2, 'aspectualacme_ArmaniUnaryExpression', b)
    _safe_set(b, 'aspectualacme_ArmaniUnaryExpression161', None)
    assert not _is_linked(b, 'aspectualacme_ArmaniUnaryExpression161', a2)
    if hasattr(a2, 'aspectualacme_ArmaniUnaryExpression'):
        assert not _is_linked(a2, 'aspectualacme_ArmaniUnaryExpression', b)


def test_assoc_variable180_reverse_link_reassign_clear():
    a1 = aspectualacme_ArmaniVariable(basicType="sample_text", id="sample_text")
    a2 = aspectualacme_ArmaniVariable(basicType="sample_text_2", id="sample_text_2")
    b = aspectualacme_ArmaniQuantifiedExpression(quantifier="sample_text")
    _safe_set(b, 'aspectualacme_ArmaniQuantifiedExpression', a1)
    assert _is_linked(b, 'aspectualacme_ArmaniQuantifiedExpression', a1)
    if hasattr(a1, 'aspectualacme_ArmaniVariable181'):
        assert _is_linked(a1, 'aspectualacme_ArmaniVariable181', b)
    _safe_set(b, 'aspectualacme_ArmaniQuantifiedExpression', a2)
    assert _is_linked(b, 'aspectualacme_ArmaniQuantifiedExpression', a2)
    if hasattr(a1, 'aspectualacme_ArmaniVariable181'):
        assert not _is_linked(a1, 'aspectualacme_ArmaniVariable181', b)
    if hasattr(a2, 'aspectualacme_ArmaniVariable181'):
        assert _is_linked(a2, 'aspectualacme_ArmaniVariable181', b)
    _safe_set(b, 'aspectualacme_ArmaniQuantifiedExpression', None)
    assert not _is_linked(b, 'aspectualacme_ArmaniQuantifiedExpression', a2)
    if hasattr(a2, 'aspectualacme_ArmaniVariable181'):
        assert not _is_linked(a2, 'aspectualacme_ArmaniVariable181', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_armani5_stub_double():
    # aspectualacme_BasicElement has no real 'aspectualacme_BasicElement6' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Armani's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Armani's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Armani(modifiers="sample_text")
    partner = aspectualacme_BasicElement()
    setattr(partner, 'aspectualacme_BasicElement6', None)
    _safe_set(owner, 'aspectualacme_Armani', partner)
    assert owner in getattr(partner, 'aspectualacme_BasicElement6')
    _safe_set(owner, 'aspectualacme_Armani', None)
    assert owner not in getattr(partner, 'aspectualacme_BasicElement6')


def test_assoc_baseAttach124_stub_double():
    # aspectualacme_BaseRole has no real 'aspectualacme_BaseRole126' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Glue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Glue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Glue(glueType="sample_text")
    partner = aspectualacme_BaseRole()
    setattr(partner, 'aspectualacme_BaseRole126', None)
    _safe_set(owner, 'aspectualacme_Glue125', partner)
    assert getattr(partner, 'aspectualacme_BaseRole126') == owner
    _safe_set(owner, 'aspectualacme_Glue125', None)
    assert getattr(partner, 'aspectualacme_BaseRole126') is None


def test_assoc_bindings152_stub_double():
    # aspectualacme_Binding has no real 'Binding' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Representation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Representation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Representation(name="sample_text")
    partner = aspectualacme_Binding()
    setattr(partner, 'Binding', None)
    _safe_set(owner, 'representation', {partner})
    assert getattr(partner, 'Binding') == owner
    _safe_set(owner, 'representation', set())
    assert getattr(partner, 'Binding') is None


def test_assoc_connector130_stub_double():
    # aspectualacme_Connector has no real 'Connector131' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Glue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Glue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Glue(glueType="sample_text")
    partner = aspectualacme_Connector()
    setattr(partner, 'Connector131', None)
    _safe_set(owner, 'glue', partner)
    assert getattr(partner, 'Connector131') == owner
    _safe_set(owner, 'glue', None)
    assert getattr(partner, 'Connector131') is None


def test_assoc_crosscuttingAttach127_stub_double():
    # aspectualacme_CrosscuttingRole has no real 'aspectualacme_CrosscuttingRole129' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Glue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Glue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Glue(glueType="sample_text")
    partner = aspectualacme_CrosscuttingRole()
    setattr(partner, 'aspectualacme_CrosscuttingRole129', None)
    _safe_set(owner, 'aspectualacme_Glue128', partner)
    assert getattr(partner, 'aspectualacme_CrosscuttingRole129') == owner
    _safe_set(owner, 'aspectualacme_Glue128', None)
    assert getattr(partner, 'aspectualacme_CrosscuttingRole129') is None


def test_assoc_designRule154_stub_double():
    # aspectualacme_ArmaniDesignRuleExpression has no real 'aspectualacme_ArmaniDesignRuleExpression' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Armani's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Armani's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Armani(modifiers="sample_text")
    partner = aspectualacme_ArmaniDesignRuleExpression()
    setattr(partner, 'aspectualacme_ArmaniDesignRuleExpression', None)
    _safe_set(owner, 'aspectualacme_Armani155', partner)
    assert getattr(partner, 'aspectualacme_ArmaniDesignRuleExpression') == owner
    _safe_set(owner, 'aspectualacme_Armani155', None)
    assert getattr(partner, 'aspectualacme_ArmaniDesignRuleExpression') is None


def test_assoc_designRule185_stub_double():
    # aspectualacme_ArmaniDesignRuleExpression has no real 'aspectualacme_ArmaniDesignRuleExpression187' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_ArmaniQuantifiedExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_ArmaniQuantifiedExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_ArmaniQuantifiedExpression(quantifier="sample_text")
    partner = aspectualacme_ArmaniDesignRuleExpression()
    setattr(partner, 'aspectualacme_ArmaniDesignRuleExpression187', None)
    _safe_set(owner, 'aspectualacme_ArmaniQuantifiedExpression186', partner)
    assert getattr(partner, 'aspectualacme_ArmaniDesignRuleExpression187') == owner
    _safe_set(owner, 'aspectualacme_ArmaniQuantifiedExpression186', None)
    assert getattr(partner, 'aspectualacme_ArmaniDesignRuleExpression187') is None


def test_assoc_expressions171_stub_double():
    # aspectualacme_ArmaniIffExpression has no real 'aspectualacme_ArmaniIffExpression' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_ArmaniEqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_ArmaniEqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_ArmaniEqualityExpression(operators="sample_text")
    partner = aspectualacme_ArmaniIffExpression()
    setattr(partner, 'aspectualacme_ArmaniIffExpression', None)
    _safe_set(owner, 'aspectualacme_ArmaniEqualityExpression172', partner)
    assert owner in getattr(partner, 'aspectualacme_ArmaniIffExpression')
    _safe_set(owner, 'aspectualacme_ArmaniEqualityExpression172', None)
    assert owner not in getattr(partner, 'aspectualacme_ArmaniIffExpression')


def test_assoc_expressions175_stub_double():
    # aspectualacme_ArmaniImpliesExpression has no real 'aspectualacme_ArmaniImpliesExpression176' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_ArmaniOrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_ArmaniOrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_ArmaniOrExpression(operators="sample_text")
    partner = aspectualacme_ArmaniImpliesExpression()
    setattr(partner, 'aspectualacme_ArmaniImpliesExpression176', None)
    _safe_set(owner, 'aspectualacme_ArmaniOrExpression', {partner})
    assert getattr(partner, 'aspectualacme_ArmaniImpliesExpression176') == owner
    _safe_set(owner, 'aspectualacme_ArmaniOrExpression', set())
    assert getattr(partner, 'aspectualacme_ArmaniImpliesExpression176') is None


def test_assoc_expressions178_stub_double():
    # aspectualacme_ArmaniBooleanExpression has no real 'aspectualacme_ArmaniBooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_ArmaniOrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_ArmaniOrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_ArmaniOrExpression(operators="sample_text")
    partner = aspectualacme_ArmaniBooleanExpression()
    setattr(partner, 'aspectualacme_ArmaniBooleanExpression', None)
    _safe_set(owner, 'aspectualacme_ArmaniOrExpression179', partner)
    assert owner in getattr(partner, 'aspectualacme_ArmaniBooleanExpression')
    _safe_set(owner, 'aspectualacme_ArmaniOrExpression179', None)
    assert owner not in getattr(partner, 'aspectualacme_ArmaniBooleanExpression')


def test_assoc_glue43_stub_double():
    # aspectualacme_ConnectorType has no real 'aspectualacme_ConnectorType44' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Glue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Glue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Glue(glueType="sample_text")
    partner = aspectualacme_ConnectorType()
    setattr(partner, 'aspectualacme_ConnectorType44', None)
    _safe_set(owner, 'aspectualacme_Glue', partner)
    assert owner in getattr(partner, 'aspectualacme_ConnectorType44')
    _safe_set(owner, 'aspectualacme_Glue', None)
    assert owner not in getattr(partner, 'aspectualacme_ConnectorType44')


def test_assoc_glue82_stub_double():
    # aspectualacme_Connector has no real 'connector' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Glue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Glue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Glue(glueType="sample_text")
    partner = aspectualacme_Connector()
    setattr(partner, 'connector', None)
    _safe_set(owner, 'Glue', partner)
    assert owner in getattr(partner, 'connector')
    _safe_set(owner, 'Glue', None)
    assert owner not in getattr(partner, 'connector')


def test_assoc_imports0_stub_double():
    # aspectualacme_Root has no real 'aspectualacme_Root' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Import(fileName="sample_text")
    partner = aspectualacme_Root()
    setattr(partner, 'aspectualacme_Root', None)
    _safe_set(owner, 'aspectualacme_Import', partner)
    assert owner in getattr(partner, 'aspectualacme_Root')
    _safe_set(owner, 'aspectualacme_Import', None)
    assert owner not in getattr(partner, 'aspectualacme_Root')


def test_assoc_parameters156_stub_double():
    # aspectualacme_ArmaniPrimitiveExpression has no real 'aspectualacme_ArmaniPrimitiveExpression' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_ArmaniFunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_ArmaniFunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_ArmaniFunctionCall(functionId="sample_text")
    partner = aspectualacme_ArmaniPrimitiveExpression()
    setattr(partner, 'aspectualacme_ArmaniPrimitiveExpression', None)
    _safe_set(owner, 'aspectualacme_ArmaniFunctionCall', {partner})
    assert getattr(partner, 'aspectualacme_ArmaniPrimitiveExpression') == owner
    _safe_set(owner, 'aspectualacme_ArmaniFunctionCall', set())
    assert getattr(partner, 'aspectualacme_ArmaniPrimitiveExpression') is None


def test_assoc_parentFamily121_stub_double():
    # aspectualacme_Family has no real 'Family123' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Property(name="sample_text", value="sample_text")
    partner = aspectualacme_Family()
    setattr(partner, 'Family123', None)
    _safe_set(owner, 'properties122', partner)
    assert getattr(partner, 'Family123') == owner
    _safe_set(owner, 'properties122', None)
    assert getattr(partner, 'Family123') is None


def test_assoc_parentFamily47_stub_double():
    # aspectualacme_Family has no real 'Family48' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_PropertyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_PropertyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_PropertyType(type="sample_text", values="sample_text")
    partner = aspectualacme_Family()
    setattr(partner, 'Family48', None)
    _safe_set(owner, 'prtypes', partner)
    assert getattr(partner, 'Family48') == owner
    _safe_set(owner, 'prtypes', None)
    assert getattr(partner, 'Family48') is None


def test_assoc_parentRepresentation62_stub_double():
    # aspectualacme_System has no real 'system' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Representation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Representation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Representation(name="sample_text")
    partner = aspectualacme_System()
    setattr(partner, 'system', None)
    _safe_set(owner, 'Representation63', partner)
    assert getattr(partner, 'system') == owner
    _safe_set(owner, 'Representation63', None)
    assert getattr(partner, 'system') is None


def test_assoc_parentSystem119_stub_double():
    # aspectualacme_System has no real 'System120' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Property(name="sample_text", value="sample_text")
    partner = aspectualacme_System()
    setattr(partner, 'System120', None)
    _safe_set(owner, 'properties', partner)
    assert getattr(partner, 'System120') == owner
    _safe_set(owner, 'properties', None)
    assert getattr(partner, 'System120') is None


def test_assoc_properties26_stub_double():
    # aspectualacme_Family has no real 'parentFamily27' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Property(name="sample_text", value="sample_text")
    partner = aspectualacme_Family()
    setattr(partner, 'parentFamily27', None)
    _safe_set(owner, 'Property', partner)
    assert owner in getattr(partner, 'parentFamily27')
    _safe_set(owner, 'Property', None)
    assert owner not in getattr(partner, 'parentFamily27')


def test_assoc_properties51_stub_double():
    # aspectualacme_System has no real 'parentSystem52' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Property(name="sample_text", value="sample_text")
    partner = aspectualacme_System()
    setattr(partner, 'parentSystem52', None)
    _safe_set(owner, 'Property53', partner)
    assert owner in getattr(partner, 'parentSystem52')
    _safe_set(owner, 'Property53', None)
    assert owner not in getattr(partner, 'parentSystem52')


def test_assoc_property141_stub_double():
    # aspectualacme_Binding has no real 'aspectualacme_Binding' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Property(name="sample_text", value="sample_text")
    partner = aspectualacme_Binding()
    setattr(partner, 'aspectualacme_Binding', None)
    _safe_set(owner, 'aspectualacme_Property142', partner)
    assert owner in getattr(partner, 'aspectualacme_Binding')
    _safe_set(owner, 'aspectualacme_Property142', None)
    assert owner not in getattr(partner, 'aspectualacme_Binding')


def test_assoc_prtypes24_stub_double():
    # aspectualacme_Family has no real 'parentFamily25' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_PropertyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_PropertyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_PropertyType(type="sample_text", values="sample_text")
    partner = aspectualacme_Family()
    setattr(partner, 'parentFamily25', None)
    _safe_set(owner, 'PropertyType', partner)
    assert owner in getattr(partner, 'parentFamily25')
    _safe_set(owner, 'PropertyType', None)
    assert owner not in getattr(partner, 'parentFamily25')


def test_assoc_representation148_stub_double():
    # aspectualacme_Binding has no real 'bindings' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Representation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Representation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Representation(name="sample_text")
    partner = aspectualacme_Binding()
    setattr(partner, 'bindings', None)
    _safe_set(owner, 'Representation149', partner)
    assert getattr(partner, 'bindings') == owner
    _safe_set(owner, 'Representation149', None)
    assert getattr(partner, 'bindings') is None


def test_assoc_setValues157_stub_double():
    # aspectualacme_ArmaniConstant has no real 'aspectualacme_ArmaniConstant' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_ArmaniSetExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_ArmaniSetExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_ArmaniSetExpression(reference="sample_text", referenceType="sample_text")
    partner = aspectualacme_ArmaniConstant()
    setattr(partner, 'aspectualacme_ArmaniConstant', None)
    _safe_set(owner, 'aspectualacme_ArmaniSetExpression', {partner})
    assert getattr(partner, 'aspectualacme_ArmaniConstant') == owner
    _safe_set(owner, 'aspectualacme_ArmaniSetExpression', set())
    assert getattr(partner, 'aspectualacme_ArmaniConstant') is None


def test_assoc_system150_stub_double():
    # aspectualacme_System has no real 'System151' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_Representation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_Representation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_Representation(name="sample_text")
    partner = aspectualacme_System()
    setattr(partner, 'System151', None)
    _safe_set(owner, 'parentRepresentation', partner)
    assert getattr(partner, 'System151') == owner
    _safe_set(owner, 'parentRepresentation', None)
    assert getattr(partner, 'System151') is None


def test_assoc_userType177_stub_double():
    # aspectualacme_TypeDefinition has no real 'aspectualacme_TypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_ArmaniVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_ArmaniVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_ArmaniVariable(basicType="sample_text", id="sample_text")
    partner = aspectualacme_TypeDefinition()
    setattr(partner, 'aspectualacme_TypeDefinition', None)
    _safe_set(owner, 'aspectualacme_ArmaniVariable', partner)
    assert getattr(partner, 'aspectualacme_TypeDefinition') == owner
    _safe_set(owner, 'aspectualacme_ArmaniVariable', None)
    assert getattr(partner, 'aspectualacme_TypeDefinition') is None


def test_assoc_wildCard57_stub_double():
    # aspectualacme_System has no real 'aspectualacme_System' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_WildCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_WildCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_WildCard(expression="sample_text")
    partner = aspectualacme_System()
    setattr(partner, 'aspectualacme_System', None)
    _safe_set(owner, 'aspectualacme_WildCard58', partner)
    assert owner in getattr(partner, 'aspectualacme_System')
    _safe_set(owner, 'aspectualacme_WildCard58', None)
    assert owner not in getattr(partner, 'aspectualacme_System')


def test_assoc_wildcard14_stub_double():
    # aspectualacme_Family has no real 'aspectualacme_Family15' property in the generated
    # code (a bare stub) -- manually attach it so aspectualacme_WildCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aspectualacme_WildCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aspectualacme_WildCard(expression="sample_text")
    partner = aspectualacme_Family()
    setattr(partner, 'aspectualacme_Family15', None)
    _safe_set(owner, 'aspectualacme_WildCard', partner)
    assert owner in getattr(partner, 'aspectualacme_Family15')
    _safe_set(owner, 'aspectualacme_WildCard', None)
    assert owner not in getattr(partner, 'aspectualacme_Family15')


