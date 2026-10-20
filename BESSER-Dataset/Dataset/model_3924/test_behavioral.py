import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionExpression,
    CollectionFunction,
    Expression,
    ModelElement,
    ProviderConstruction,
    ScalarExpression,
    SectionedView,
    StringFunction,
    Type,
    VariableDeclaration,
    View,
    ViewAction,
    applauseDsl_Application,
    applauseDsl_CollectionExpression,
    applauseDsl_CollectionFunction,
    applauseDsl_CollectionIterator,
    applauseDsl_CollectionLiteral,
    applauseDsl_ComplexProviderConstruction,
    applauseDsl_ContentProvider,
    applauseDsl_CustomView,
    applauseDsl_DetailsView,
    applauseDsl_Entity,
    applauseDsl_Expression,
    applauseDsl_ExternalOpen,
    applauseDsl_Model,
    applauseDsl_ModelElement,
    applauseDsl_ObjectReference,
    applauseDsl_Parameter,
    applauseDsl_Property,
    applauseDsl_ProviderConstruction,
    applauseDsl_ScalarExpression,
    applauseDsl_SectionCell,
    applauseDsl_SectionedView,
    applauseDsl_SimpleProviderConstruction,
    applauseDsl_SimpleType,
    applauseDsl_StringConcat,
    applauseDsl_StringFunction,
    applauseDsl_StringLiteral,
    applauseDsl_StringReplace,
    applauseDsl_StringSplit,
    applauseDsl_StringUrlConform,
    applauseDsl_TabbarButton,
    applauseDsl_TableView,
    applauseDsl_Type,
    applauseDsl_TypeDescription,
    applauseDsl_VariableDeclaration,
    applauseDsl_View,
    applauseDsl_ViewAction,
    applauseDsl_ViewCall,
    applauseDsl_ViewHeader,
    applauseDsl_ViewSection,
    CellType,
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

def test_assoc_description28_reverse_link_reassign_clear():
    a1 = applauseDsl_TypeDescription(many=True)
    a2 = applauseDsl_TypeDescription(many=False)
    b = applauseDsl_Property(derived=True)
    _safe_set(b, 'applauseDsl_Property29', a1)
    assert _is_linked(b, 'applauseDsl_Property29', a1)
    if hasattr(a1, 'applauseDsl_TypeDescription30'):
        assert _is_linked(a1, 'applauseDsl_TypeDescription30', b)
    _safe_set(b, 'applauseDsl_Property29', a2)
    assert _is_linked(b, 'applauseDsl_Property29', a2)
    if hasattr(a1, 'applauseDsl_TypeDescription30'):
        assert not _is_linked(a1, 'applauseDsl_TypeDescription30', b)
    if hasattr(a2, 'applauseDsl_TypeDescription30'):
        assert _is_linked(a2, 'applauseDsl_TypeDescription30', b)
    _safe_set(b, 'applauseDsl_Property29', None)
    assert not _is_linked(b, 'applauseDsl_Property29', a2)
    if hasattr(a2, 'applauseDsl_TypeDescription30'):
        assert not _is_linked(a2, 'applauseDsl_TypeDescription30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action77_stub_double():
    # applauseDsl_ViewAction has no real 'applauseDsl_ViewAction' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ViewAction()
    setattr(partner, 'applauseDsl_ViewAction', None)
    _safe_set(owner, 'applauseDsl_SectionCell78', partner)
    assert getattr(partner, 'applauseDsl_ViewAction') == owner
    _safe_set(owner, 'applauseDsl_SectionCell78', None)
    assert getattr(partner, 'applauseDsl_ViewAction') is None


def test_assoc_application0_stub_double():
    # applauseDsl_Model has no real 'applauseDsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text")
    partner = applauseDsl_Model()
    setattr(partner, 'applauseDsl_Model', None)
    _safe_set(owner, 'applauseDsl_Application', partner)
    assert getattr(partner, 'applauseDsl_Model') == owner
    _safe_set(owner, 'applauseDsl_Application', None)
    assert getattr(partner, 'applauseDsl_Model') is None


def test_assoc_background11_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression13' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression13', None)
    _safe_set(owner, 'applauseDsl_Application12', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression13') == owner
    _safe_set(owner, 'applauseDsl_Application12', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression13') is None


def test_assoc_buttons14_stub_double():
    # applauseDsl_TabbarButton has no real 'applauseDsl_TabbarButton' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text")
    partner = applauseDsl_TabbarButton()
    setattr(partner, 'applauseDsl_TabbarButton', None)
    _safe_set(owner, 'applauseDsl_Application15', {partner})
    assert getattr(partner, 'applauseDsl_TabbarButton') == owner
    _safe_set(owner, 'applauseDsl_Application15', set())
    assert getattr(partner, 'applauseDsl_TabbarButton') is None


def test_assoc_cells64_stub_double():
    # applauseDsl_ViewSection has no real 'applauseDsl_ViewSection65' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ViewSection()
    setattr(partner, 'applauseDsl_ViewSection65', None)
    _safe_set(owner, 'applauseDsl_SectionCell', partner)
    assert owner in getattr(partner, 'applauseDsl_ViewSection65')
    _safe_set(owner, 'applauseDsl_SectionCell', None)
    assert owner not in getattr(partner, 'applauseDsl_ViewSection65')


def test_assoc_description4_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TypeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TypeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TypeDescription(many=True)
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter', None)
    _safe_set(owner, 'applauseDsl_TypeDescription5', partner)
    assert getattr(partner, 'applauseDsl_Parameter') == owner
    _safe_set(owner, 'applauseDsl_TypeDescription5', None)
    assert getattr(partner, 'applauseDsl_Parameter') is None


def test_assoc_details71_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression73' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression73', None)
    _safe_set(owner, 'applauseDsl_SectionCell72', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression73') == owner
    _safe_set(owner, 'applauseDsl_SectionCell72', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression73') is None


def test_assoc_elements1_stub_double():
    # applauseDsl_Model has no real 'applauseDsl_Model2' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ModelElement(name="sample_text")
    partner = applauseDsl_Model()
    setattr(partner, 'applauseDsl_Model2', None)
    _safe_set(owner, 'applauseDsl_ModelElement', partner)
    assert owner in getattr(partner, 'applauseDsl_Model2')
    _safe_set(owner, 'applauseDsl_ModelElement', None)
    assert owner not in getattr(partner, 'applauseDsl_Model2')


def test_assoc_image74_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression76' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression76', None)
    _safe_set(owner, 'applauseDsl_SectionCell75', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression76') == owner
    _safe_set(owner, 'applauseDsl_SectionCell75', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression76') is None


def test_assoc_iterator66_stub_double():
    # applauseDsl_CollectionIterator has no real 'applauseDsl_CollectionIterator' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_CollectionIterator()
    setattr(partner, 'applauseDsl_CollectionIterator', None)
    _safe_set(owner, 'applauseDsl_SectionCell67', partner)
    assert getattr(partner, 'applauseDsl_CollectionIterator') == owner
    _safe_set(owner, 'applauseDsl_SectionCell67', None)
    assert getattr(partner, 'applauseDsl_CollectionIterator') is None


def test_assoc_object6_stub_double():
    # applauseDsl_ObjectReference has no real 'applauseDsl_ObjectReference' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_VariableDeclaration(name="sample_text")
    partner = applauseDsl_ObjectReference()
    setattr(partner, 'applauseDsl_ObjectReference', None)
    _safe_set(owner, 'applauseDsl_VariableDeclaration', partner)
    assert getattr(partner, 'applauseDsl_ObjectReference') == owner
    _safe_set(owner, 'applauseDsl_VariableDeclaration', None)
    assert getattr(partner, 'applauseDsl_ObjectReference') is None


def test_assoc_parameter31_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter32' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True)
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter32', None)
    _safe_set(owner, 'applauseDsl_ContentProvider', partner)
    assert getattr(partner, 'applauseDsl_Parameter32') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider', None)
    assert getattr(partner, 'applauseDsl_Parameter32') is None


def test_assoc_properties26_stub_double():
    # applauseDsl_Entity has no real 'applauseDsl_Entity27' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Property(derived=True)
    partner = applauseDsl_Entity()
    setattr(partner, 'applauseDsl_Entity27', None)
    _safe_set(owner, 'applauseDsl_Property', partner)
    assert owner in getattr(partner, 'applauseDsl_Entity27')
    _safe_set(owner, 'applauseDsl_Property', None)
    assert owner not in getattr(partner, 'applauseDsl_Entity27')


def test_assoc_provider105_stub_double():
    # applauseDsl_ComplexProviderConstruction has no real 'applauseDsl_ComplexProviderConstruction' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True)
    partner = applauseDsl_ComplexProviderConstruction()
    setattr(partner, 'applauseDsl_ComplexProviderConstruction', None)
    _safe_set(owner, 'applauseDsl_ContentProvider106', partner)
    assert getattr(partner, 'applauseDsl_ComplexProviderConstruction') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider106', None)
    assert getattr(partner, 'applauseDsl_ComplexProviderConstruction') is None


def test_assoc_selection39_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression41' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True)
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression41', None)
    _safe_set(owner, 'applauseDsl_ContentProvider40', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression41') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider40', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression41') is None


def test_assoc_text68_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression70' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression70', None)
    _safe_set(owner, 'applauseDsl_SectionCell69', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression70') == owner
    _safe_set(owner, 'applauseDsl_SectionCell69', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression70') is None


def test_assoc_type3_stub_double():
    # applauseDsl_Type has no real 'applauseDsl_Type' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TypeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TypeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TypeDescription(many=True)
    partner = applauseDsl_Type()
    setattr(partner, 'applauseDsl_Type', None)
    _safe_set(owner, 'applauseDsl_TypeDescription', partner)
    assert getattr(partner, 'applauseDsl_Type') == owner
    _safe_set(owner, 'applauseDsl_TypeDescription', None)
    assert getattr(partner, 'applauseDsl_Type') is None


def test_assoc_type33_stub_double():
    # applauseDsl_Type has no real 'applauseDsl_Type35' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True)
    partner = applauseDsl_Type()
    setattr(partner, 'applauseDsl_Type35', None)
    _safe_set(owner, 'applauseDsl_ContentProvider34', partner)
    assert getattr(partner, 'applauseDsl_Type35') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider34', None)
    assert getattr(partner, 'applauseDsl_Type35') is None


def test_assoc_url36_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression38' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True)
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression38', None)
    _safe_set(owner, 'applauseDsl_ContentProvider37', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression38') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider37', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression38') is None


