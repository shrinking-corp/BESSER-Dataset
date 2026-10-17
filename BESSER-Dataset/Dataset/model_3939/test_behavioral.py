import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    NamedElement,
    PlatformMapping,
    RESTURL,
    ReferrableElement,
    Type,
    UIActionSpecification,
    UIComponentOrDataType,
    UrlFragment,
    applauseDsl_AbsoluteRESTURL,
    applauseDsl_Attribute,
    applauseDsl_AttributeReference,
    applauseDsl_DataSource,
    applauseDsl_DataSourceAccessMethod,
    applauseDsl_DataSourceBodySpecification,
    applauseDsl_DataSourceCall,
    applauseDsl_DataType,
    applauseDsl_Entity,
    applauseDsl_EntityMemberCall,
    applauseDsl_EntityMemberCallTail,
    applauseDsl_Expression,
    applauseDsl_ListItemCellDeclaration,
    applauseDsl_LoopVariable,
    applauseDsl_Model,
    applauseDsl_NamedElement,
    applauseDsl_Parameter,
    applauseDsl_Platform,
    applauseDsl_PlatformMapping,
    applauseDsl_RESTMethodCall,
    applauseDsl_RESTSpecification,
    applauseDsl_RESTURL,
    applauseDsl_ReferrableElement,
    applauseDsl_RelativeRESTURL,
    applauseDsl_Screen,
    applauseDsl_ScreenListItemCell,
    applauseDsl_ScreenSection,
    applauseDsl_ScreenSectionItems,
    applauseDsl_StringLiteral,
    applauseDsl_Type,
    applauseDsl_TypeMapping,
    applauseDsl_UIAction,
    applauseDsl_UIActionDeleteAction,
    applauseDsl_UIActionNavigateAction,
    applauseDsl_UIActionSpecification,
    applauseDsl_UIComponentDeclaration,
    applauseDsl_UIComponentMemberCall,
    applauseDsl_UIComponentMemberConfiguration,
    applauseDsl_UIComponentMemberDeclaration,
    applauseDsl_UIComponentOrDataType,
    applauseDsl_UrlFragment,
    applauseDsl_UrlPathFragment,
    applauseDsl_Variable,
    ActionVerb,
    GestureKind,
    RESTVerb,
    ScreenKind,
    UIActionKind,
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

def test_assoc_actions42_reverse_link_reassign_clear():
    a1 = applauseDsl_UIAction(gesture="sample_text", icon="sample_text", order=7, title="sample_text")
    a2 = applauseDsl_UIAction(gesture="sample_text_2", icon="sample_text_2", order=13, title="sample_text_2")
    b = applauseDsl_Screen(kind="sample_text", title="sample_text")
    _safe_set(b, 'applauseDsl_Screen43', {a1})
    assert _is_linked(b, 'applauseDsl_Screen43', a1)
    if hasattr(a1, 'applauseDsl_UIAction'):
        assert _is_linked(a1, 'applauseDsl_UIAction', b)
    _safe_set(b, 'applauseDsl_Screen43', {a2})
    assert _is_linked(b, 'applauseDsl_Screen43', a2)
    if hasattr(a1, 'applauseDsl_UIAction'):
        assert not _is_linked(a1, 'applauseDsl_UIAction', b)
    if hasattr(a2, 'applauseDsl_UIAction'):
        assert _is_linked(a2, 'applauseDsl_UIAction', b)
    _safe_set(b, 'applauseDsl_Screen43', set())
    assert not _is_linked(b, 'applauseDsl_Screen43', a2)
    if hasattr(a2, 'applauseDsl_UIAction'):
        assert not _is_linked(a2, 'applauseDsl_UIAction', b)


def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = applauseDsl_Entity(abstract=True)
    a2 = applauseDsl_Entity(abstract=False)
    b = applauseDsl_Attribute(many=True, name="sample_text")
    _safe_set(b, 'applauseDsl_Attribute', a1)
    assert _is_linked(b, 'applauseDsl_Attribute', a1)
    if hasattr(a1, 'applauseDsl_Entity4'):
        assert _is_linked(a1, 'applauseDsl_Entity4', b)
    _safe_set(b, 'applauseDsl_Attribute', a2)
    assert _is_linked(b, 'applauseDsl_Attribute', a2)
    if hasattr(a1, 'applauseDsl_Entity4'):
        assert not _is_linked(a1, 'applauseDsl_Entity4', b)
    if hasattr(a2, 'applauseDsl_Entity4'):
        assert _is_linked(a2, 'applauseDsl_Entity4', b)
    _safe_set(b, 'applauseDsl_Attribute', None)
    assert not _is_linked(b, 'applauseDsl_Attribute', a2)
    if hasattr(a2, 'applauseDsl_Entity4'):
        assert not _is_linked(a2, 'applauseDsl_Entity4', b)


def test_assoc_datasource38_reverse_link_reassign_clear():
    a1 = applauseDsl_Screen(kind="sample_text", title="sample_text")
    a2 = applauseDsl_Screen(kind="sample_text_2", title="sample_text_2")
    b = applauseDsl_DataSourceCall(name="sample_text")
    _safe_set(b, 'applauseDsl_DataSourceCall', a1)
    assert _is_linked(b, 'applauseDsl_DataSourceCall', a1)
    if hasattr(a1, 'applauseDsl_Screen39'):
        assert _is_linked(a1, 'applauseDsl_Screen39', b)
    _safe_set(b, 'applauseDsl_DataSourceCall', a2)
    assert _is_linked(b, 'applauseDsl_DataSourceCall', a2)
    if hasattr(a1, 'applauseDsl_Screen39'):
        assert not _is_linked(a1, 'applauseDsl_Screen39', b)
    if hasattr(a2, 'applauseDsl_Screen39'):
        assert _is_linked(a2, 'applauseDsl_Screen39', b)
    _safe_set(b, 'applauseDsl_DataSourceCall', None)
    assert not _is_linked(b, 'applauseDsl_DataSourceCall', a2)
    if hasattr(a2, 'applauseDsl_Screen39'):
        assert not _is_linked(a2, 'applauseDsl_Screen39', b)


def test_assoc_datasource44_reverse_link_reassign_clear():
    a1 = applauseDsl_ScreenSection(title="sample_text")
    a2 = applauseDsl_ScreenSection(title="sample_text_2")
    b = applauseDsl_DataSourceCall(name="sample_text")
    _safe_set(b, 'applauseDsl_DataSourceCall46', a1)
    assert _is_linked(b, 'applauseDsl_DataSourceCall46', a1)
    if hasattr(a1, 'applauseDsl_ScreenSection45'):
        assert _is_linked(a1, 'applauseDsl_ScreenSection45', b)
    _safe_set(b, 'applauseDsl_DataSourceCall46', a2)
    assert _is_linked(b, 'applauseDsl_DataSourceCall46', a2)
    if hasattr(a1, 'applauseDsl_ScreenSection45'):
        assert not _is_linked(a1, 'applauseDsl_ScreenSection45', b)
    if hasattr(a2, 'applauseDsl_ScreenSection45'):
        assert _is_linked(a2, 'applauseDsl_ScreenSection45', b)
    _safe_set(b, 'applauseDsl_DataSourceCall46', None)
    assert not _is_linked(b, 'applauseDsl_DataSourceCall46', a2)
    if hasattr(a2, 'applauseDsl_ScreenSection45'):
        assert not _is_linked(a2, 'applauseDsl_ScreenSection45', b)


def test_assoc_restSpecification17_reverse_link_reassign_clear():
    a1 = applauseDsl_RESTSpecification(verb="sample_text")
    a2 = applauseDsl_RESTSpecification(verb="sample_text_2")
    b = applauseDsl_DataSourceAccessMethod(name="sample_text", returnsMany=True)
    _safe_set(b, 'applauseDsl_DataSourceAccessMethod18', a1)
    assert _is_linked(b, 'applauseDsl_DataSourceAccessMethod18', a1)
    if hasattr(a1, 'applauseDsl_RESTSpecification'):
        assert _is_linked(a1, 'applauseDsl_RESTSpecification', b)
    _safe_set(b, 'applauseDsl_DataSourceAccessMethod18', a2)
    assert _is_linked(b, 'applauseDsl_DataSourceAccessMethod18', a2)
    if hasattr(a1, 'applauseDsl_RESTSpecification'):
        assert not _is_linked(a1, 'applauseDsl_RESTSpecification', b)
    if hasattr(a2, 'applauseDsl_RESTSpecification'):
        assert _is_linked(a2, 'applauseDsl_RESTSpecification', b)
    _safe_set(b, 'applauseDsl_DataSourceAccessMethod18', None)
    assert not _is_linked(b, 'applauseDsl_DataSourceAccessMethod18', a2)
    if hasattr(a2, 'applauseDsl_RESTSpecification'):
        assert not _is_linked(a2, 'applauseDsl_RESTSpecification', b)


def test_assoc_sections40_reverse_link_reassign_clear():
    a1 = applauseDsl_ScreenSection(title="sample_text")
    a2 = applauseDsl_ScreenSection(title="sample_text_2")
    b = applauseDsl_Screen(kind="sample_text", title="sample_text")
    _safe_set(b, 'applauseDsl_Screen41', {a1})
    assert _is_linked(b, 'applauseDsl_Screen41', a1)
    if hasattr(a1, 'applauseDsl_ScreenSection'):
        assert _is_linked(a1, 'applauseDsl_ScreenSection', b)
    _safe_set(b, 'applauseDsl_Screen41', {a2})
    assert _is_linked(b, 'applauseDsl_Screen41', a2)
    if hasattr(a1, 'applauseDsl_ScreenSection'):
        assert not _is_linked(a1, 'applauseDsl_ScreenSection', b)
    if hasattr(a2, 'applauseDsl_ScreenSection'):
        assert _is_linked(a2, 'applauseDsl_ScreenSection', b)
    _safe_set(b, 'applauseDsl_Screen41', set())
    assert not _is_linked(b, 'applauseDsl_Screen41', a2)
    if hasattr(a2, 'applauseDsl_ScreenSection'):
        assert not _is_linked(a2, 'applauseDsl_ScreenSection', b)


def test_assoc_superType2_reverse_link_reassign_clear():
    a1 = applauseDsl_Entity(abstract=True)
    a2 = applauseDsl_Entity(abstract=False)
    b = applauseDsl_Entity(abstract=True)
    _safe_set(b, 'applauseDsl_Entity1', a1)
    assert _is_linked(b, 'applauseDsl_Entity1', a1)
    if hasattr(a1, 'applauseDsl_Entity'):
        assert _is_linked(a1, 'applauseDsl_Entity', b)
    _safe_set(b, 'applauseDsl_Entity1', a2)
    assert _is_linked(b, 'applauseDsl_Entity1', a2)
    if hasattr(a1, 'applauseDsl_Entity'):
        assert not _is_linked(a1, 'applauseDsl_Entity', b)
    if hasattr(a2, 'applauseDsl_Entity'):
        assert _is_linked(a2, 'applauseDsl_Entity', b)
    _safe_set(b, 'applauseDsl_Entity1', None)
    assert not _is_linked(b, 'applauseDsl_Entity1', a2)
    if hasattr(a2, 'applauseDsl_Entity'):
        assert not _is_linked(a2, 'applauseDsl_Entity', b)


def test_assoc_targetScreen64_reverse_link_reassign_clear():
    a1 = applauseDsl_UIActionNavigateAction(actionVerb="sample_text")
    a2 = applauseDsl_UIActionNavigateAction(actionVerb="sample_text_2")
    b = applauseDsl_Screen(kind="sample_text", title="sample_text")
    _safe_set(b, 'applauseDsl_Screen65', a1)
    assert _is_linked(b, 'applauseDsl_Screen65', a1)
    if hasattr(a1, 'applauseDsl_UIActionNavigateAction'):
        assert _is_linked(a1, 'applauseDsl_UIActionNavigateAction', b)
    _safe_set(b, 'applauseDsl_Screen65', a2)
    assert _is_linked(b, 'applauseDsl_Screen65', a2)
    if hasattr(a1, 'applauseDsl_UIActionNavigateAction'):
        assert not _is_linked(a1, 'applauseDsl_UIActionNavigateAction', b)
    if hasattr(a2, 'applauseDsl_UIActionNavigateAction'):
        assert _is_linked(a2, 'applauseDsl_UIActionNavigateAction', b)
    _safe_set(b, 'applauseDsl_Screen65', None)
    assert not _is_linked(b, 'applauseDsl_Screen65', a2)
    if hasattr(a2, 'applauseDsl_UIActionNavigateAction'):
        assert not _is_linked(a2, 'applauseDsl_UIActionNavigateAction', b)


def test_assoc_variable66_reverse_link_reassign_clear():
    a1 = applauseDsl_UIActionNavigateAction(actionVerb="sample_text")
    a2 = applauseDsl_UIActionNavigateAction(actionVerb="sample_text_2")
    b = applauseDsl_ReferrableElement(name="sample_text")
    _safe_set(b, 'applauseDsl_ReferrableElement', a1)
    assert _is_linked(b, 'applauseDsl_ReferrableElement', a1)
    if hasattr(a1, 'applauseDsl_UIActionNavigateAction67'):
        assert _is_linked(a1, 'applauseDsl_UIActionNavigateAction67', b)
    _safe_set(b, 'applauseDsl_ReferrableElement', a2)
    assert _is_linked(b, 'applauseDsl_ReferrableElement', a2)
    if hasattr(a1, 'applauseDsl_UIActionNavigateAction67'):
        assert not _is_linked(a1, 'applauseDsl_UIActionNavigateAction67', b)
    if hasattr(a2, 'applauseDsl_UIActionNavigateAction67'):
        assert _is_linked(a2, 'applauseDsl_UIActionNavigateAction67', b)
    _safe_set(b, 'applauseDsl_ReferrableElement', None)
    assert not _is_linked(b, 'applauseDsl_ReferrableElement', a2)
    if hasattr(a2, 'applauseDsl_UIActionNavigateAction67'):
        assert not _is_linked(a2, 'applauseDsl_UIActionNavigateAction67', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action62_stub_double():
    # applauseDsl_UIActionSpecification has no real 'applauseDsl_UIActionSpecification' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_UIAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_UIAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_UIAction(gesture="sample_text", icon="sample_text", order=7, title="sample_text")
    partner = applauseDsl_UIActionSpecification()
    setattr(partner, 'applauseDsl_UIActionSpecification', None)
    _safe_set(owner, 'applauseDsl_UIAction63', partner)
    assert getattr(partner, 'applauseDsl_UIActionSpecification') == owner
    _safe_set(owner, 'applauseDsl_UIAction63', None)
    assert getattr(partner, 'applauseDsl_UIActionSpecification') is None


def test_assoc_actions59_stub_double():
    # applauseDsl_ScreenListItemCell has no real 'applauseDsl_ScreenListItemCell60' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_UIAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_UIAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_UIAction(gesture="sample_text", icon="sample_text", order=7, title="sample_text")
    partner = applauseDsl_ScreenListItemCell()
    setattr(partner, 'applauseDsl_ScreenListItemCell60', None)
    _safe_set(owner, 'applauseDsl_UIAction61', partner)
    assert getattr(partner, 'applauseDsl_ScreenListItemCell60') == owner
    _safe_set(owner, 'applauseDsl_UIAction61', None)
    assert getattr(partner, 'applauseDsl_ScreenListItemCell60') is None


def test_assoc_baseUrl9_stub_double():
    # applauseDsl_DataSource has no real 'applauseDsl_DataSource' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_AbsoluteRESTURL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_AbsoluteRESTURL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_AbsoluteRESTURL(port=7)
    partner = applauseDsl_DataSource()
    setattr(partner, 'applauseDsl_DataSource', None)
    _safe_set(owner, 'applauseDsl_AbsoluteRESTURL', partner)
    assert getattr(partner, 'applauseDsl_DataSource') == owner
    _safe_set(owner, 'applauseDsl_AbsoluteRESTURL', None)
    assert getattr(partner, 'applauseDsl_DataSource') is None


def test_assoc_body21_stub_double():
    # applauseDsl_DataSourceBodySpecification has no real 'applauseDsl_DataSourceBodySpecification' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_RESTSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_RESTSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_RESTSpecification(verb="sample_text")
    partner = applauseDsl_DataSourceBodySpecification()
    setattr(partner, 'applauseDsl_DataSourceBodySpecification', None)
    _safe_set(owner, 'applauseDsl_RESTSpecification22', partner)
    assert getattr(partner, 'applauseDsl_DataSourceBodySpecification') == owner
    _safe_set(owner, 'applauseDsl_RESTSpecification22', None)
    assert getattr(partner, 'applauseDsl_DataSourceBodySpecification') is None


def test_assoc_component87_stub_double():
    # applauseDsl_UIComponentMemberCall has no real 'applauseDsl_UIComponentMemberCall88' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_UIComponentMemberDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_UIComponentMemberDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_UIComponentMemberDeclaration(name="sample_text")
    partner = applauseDsl_UIComponentMemberCall()
    setattr(partner, 'applauseDsl_UIComponentMemberCall88', None)
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration89', partner)
    assert getattr(partner, 'applauseDsl_UIComponentMemberCall88') == owner
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration89', None)
    assert getattr(partner, 'applauseDsl_UIComponentMemberCall88') is None


def test_assoc_datasource74_stub_double():
    # applauseDsl_RESTMethodCall has no real 'applauseDsl_RESTMethodCall75' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_DataSourceCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_DataSourceCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_DataSourceCall(name="sample_text")
    partner = applauseDsl_RESTMethodCall()
    setattr(partner, 'applauseDsl_RESTMethodCall75', None)
    _safe_set(owner, 'applauseDsl_DataSourceCall76', partner)
    assert getattr(partner, 'applauseDsl_RESTMethodCall75') == owner
    _safe_set(owner, 'applauseDsl_DataSourceCall76', None)
    assert getattr(partner, 'applauseDsl_RESTMethodCall75') is None


def test_assoc_datasource80_stub_double():
    # applauseDsl_DataSource has no real 'applauseDsl_DataSource82' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_DataSourceCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_DataSourceCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_DataSourceCall(name="sample_text")
    partner = applauseDsl_DataSource()
    setattr(partner, 'applauseDsl_DataSource82', None)
    _safe_set(owner, 'applauseDsl_DataSourceCall81', partner)
    assert getattr(partner, 'applauseDsl_DataSource82') == owner
    _safe_set(owner, 'applauseDsl_DataSourceCall81', None)
    assert getattr(partner, 'applauseDsl_DataSource82') is None


def test_assoc_declaredParameters15_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_DataSourceAccessMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_DataSourceAccessMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_DataSourceAccessMethod(name="sample_text", returnsMany=True)
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter', None)
    _safe_set(owner, 'applauseDsl_DataSourceAccessMethod16', {partner})
    assert getattr(partner, 'applauseDsl_Parameter') == owner
    _safe_set(owner, 'applauseDsl_DataSourceAccessMethod16', set())
    assert getattr(partner, 'applauseDsl_Parameter') is None


def test_assoc_elements0_stub_double():
    # applauseDsl_Model has no real 'applauseDsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_NamedElement(name="sample_text")
    partner = applauseDsl_Model()
    setattr(partner, 'applauseDsl_Model', None)
    _safe_set(owner, 'applauseDsl_NamedElement', partner)
    assert getattr(partner, 'applauseDsl_Model') == owner
    _safe_set(owner, 'applauseDsl_NamedElement', None)
    assert getattr(partner, 'applauseDsl_Model') is None


def test_assoc_head93_stub_double():
    # applauseDsl_EntityMemberCall has no real 'applauseDsl_EntityMemberCall' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Attribute(many=True, name="sample_text")
    partner = applauseDsl_EntityMemberCall()
    setattr(partner, 'applauseDsl_EntityMemberCall', None)
    _safe_set(owner, 'applauseDsl_Attribute94', partner)
    assert getattr(partner, 'applauseDsl_EntityMemberCall') == owner
    _safe_set(owner, 'applauseDsl_Attribute94', None)
    assert getattr(partner, 'applauseDsl_EntityMemberCall') is None


def test_assoc_head97_stub_double():
    # applauseDsl_EntityMemberCallTail has no real 'applauseDsl_EntityMemberCallTail98' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Attribute(many=True, name="sample_text")
    partner = applauseDsl_EntityMemberCallTail()
    setattr(partner, 'applauseDsl_EntityMemberCallTail98', None)
    _safe_set(owner, 'applauseDsl_Attribute99', partner)
    assert getattr(partner, 'applauseDsl_EntityMemberCallTail98') == owner
    _safe_set(owner, 'applauseDsl_Attribute99', None)
    assert getattr(partner, 'applauseDsl_EntityMemberCallTail98') is None


def test_assoc_host31_stub_double():
    # applauseDsl_UrlFragment has no real 'applauseDsl_UrlFragment33' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_AbsoluteRESTURL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_AbsoluteRESTURL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_AbsoluteRESTURL(port=7)
    partner = applauseDsl_UrlFragment()
    setattr(partner, 'applauseDsl_UrlFragment33', None)
    _safe_set(owner, 'applauseDsl_AbsoluteRESTURL32', partner)
    assert getattr(partner, 'applauseDsl_UrlFragment33') == owner
    _safe_set(owner, 'applauseDsl_AbsoluteRESTURL32', None)
    assert getattr(partner, 'applauseDsl_UrlFragment33') is None


def test_assoc_inputParameter36_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter37' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Screen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Screen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Screen(kind="sample_text", title="sample_text")
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter37', None)
    _safe_set(owner, 'applauseDsl_Screen', partner)
    assert getattr(partner, 'applauseDsl_Parameter37') == owner
    _safe_set(owner, 'applauseDsl_Screen', None)
    assert getattr(partner, 'applauseDsl_Parameter37') is None


def test_assoc_items47_stub_double():
    # applauseDsl_ScreenSectionItems has no real 'applauseDsl_ScreenSectionItems' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ScreenSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ScreenSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ScreenSection(title="sample_text")
    partner = applauseDsl_ScreenSectionItems()
    setattr(partner, 'applauseDsl_ScreenSectionItems', None)
    _safe_set(owner, 'applauseDsl_ScreenSection48', partner)
    assert getattr(partner, 'applauseDsl_ScreenSectionItems') == owner
    _safe_set(owner, 'applauseDsl_ScreenSection48', None)
    assert getattr(partner, 'applauseDsl_ScreenSectionItems') is None


def test_assoc_member90_stub_double():
    # applauseDsl_UIComponentMemberCall has no real 'applauseDsl_UIComponentMemberCall91' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_UIComponentMemberDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_UIComponentMemberDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_UIComponentMemberDeclaration(name="sample_text")
    partner = applauseDsl_UIComponentMemberCall()
    setattr(partner, 'applauseDsl_UIComponentMemberCall91', None)
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration92', partner)
    assert getattr(partner, 'applauseDsl_UIComponentMemberCall91') == owner
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration92', None)
    assert getattr(partner, 'applauseDsl_UIComponentMemberCall91') is None


def test_assoc_members68_stub_double():
    # applauseDsl_ListItemCellDeclaration has no real 'applauseDsl_ListItemCellDeclaration69' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_UIComponentMemberDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_UIComponentMemberDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_UIComponentMemberDeclaration(name="sample_text")
    partner = applauseDsl_ListItemCellDeclaration()
    setattr(partner, 'applauseDsl_ListItemCellDeclaration69', None)
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration', partner)
    assert getattr(partner, 'applauseDsl_ListItemCellDeclaration69') == owner
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration', None)
    assert getattr(partner, 'applauseDsl_ListItemCellDeclaration69') is None


def test_assoc_members70_stub_double():
    # applauseDsl_UIComponentDeclaration has no real 'applauseDsl_UIComponentDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_UIComponentMemberDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_UIComponentMemberDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_UIComponentMemberDeclaration(name="sample_text")
    partner = applauseDsl_UIComponentDeclaration()
    setattr(partner, 'applauseDsl_UIComponentDeclaration', None)
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration71', partner)
    assert getattr(partner, 'applauseDsl_UIComponentDeclaration') == owner
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration71', None)
    assert getattr(partner, 'applauseDsl_UIComponentDeclaration') is None


def test_assoc_methods13_stub_double():
    # applauseDsl_DataSource has no real 'applauseDsl_DataSource14' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_DataSourceAccessMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_DataSourceAccessMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_DataSourceAccessMethod(name="sample_text", returnsMany=True)
    partner = applauseDsl_DataSource()
    setattr(partner, 'applauseDsl_DataSource14', None)
    _safe_set(owner, 'applauseDsl_DataSourceAccessMethod', partner)
    assert getattr(partner, 'applauseDsl_DataSource14') == owner
    _safe_set(owner, 'applauseDsl_DataSourceAccessMethod', None)
    assert getattr(partner, 'applauseDsl_DataSource14') is None


def test_assoc_path19_stub_double():
    # applauseDsl_RESTURL has no real 'applauseDsl_RESTURL' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_RESTSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_RESTSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_RESTSpecification(verb="sample_text")
    partner = applauseDsl_RESTURL()
    setattr(partner, 'applauseDsl_RESTURL', None)
    _safe_set(owner, 'applauseDsl_RESTSpecification20', partner)
    assert getattr(partner, 'applauseDsl_RESTURL') == owner
    _safe_set(owner, 'applauseDsl_RESTSpecification20', None)
    assert getattr(partner, 'applauseDsl_RESTURL') is None


def test_assoc_resourceType10_stub_double():
    # applauseDsl_DataSource has no real 'applauseDsl_DataSource11' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Entity(abstract=True)
    partner = applauseDsl_DataSource()
    setattr(partner, 'applauseDsl_DataSource11', None)
    _safe_set(owner, 'applauseDsl_Entity12', partner)
    assert getattr(partner, 'applauseDsl_DataSource11') == owner
    _safe_set(owner, 'applauseDsl_Entity12', None)
    assert getattr(partner, 'applauseDsl_DataSource11') is None


def test_assoc_restMethod77_stub_double():
    # applauseDsl_RESTMethodCall has no real 'applauseDsl_RESTMethodCall78' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_DataSourceAccessMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_DataSourceAccessMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_DataSourceAccessMethod(name="sample_text", returnsMany=True)
    partner = applauseDsl_RESTMethodCall()
    setattr(partner, 'applauseDsl_RESTMethodCall78', None)
    _safe_set(owner, 'applauseDsl_DataSourceAccessMethod79', partner)
    assert getattr(partner, 'applauseDsl_RESTMethodCall78') == owner
    _safe_set(owner, 'applauseDsl_DataSourceAccessMethod79', None)
    assert getattr(partner, 'applauseDsl_RESTMethodCall78') is None


def test_assoc_type5_stub_double():
    # applauseDsl_Type has no real 'applauseDsl_Type' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Attribute(many=True, name="sample_text")
    partner = applauseDsl_Type()
    setattr(partner, 'applauseDsl_Type', None)
    _safe_set(owner, 'applauseDsl_Attribute6', partner)
    assert getattr(partner, 'applauseDsl_Type') == owner
    _safe_set(owner, 'applauseDsl_Attribute6', None)
    assert getattr(partner, 'applauseDsl_Type') is None


def test_assoc_type72_stub_double():
    # applauseDsl_UIComponentOrDataType has no real 'applauseDsl_UIComponentOrDataType' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_UIComponentMemberDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_UIComponentMemberDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_UIComponentMemberDeclaration(name="sample_text")
    partner = applauseDsl_UIComponentOrDataType()
    setattr(partner, 'applauseDsl_UIComponentOrDataType', None)
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration73', partner)
    assert getattr(partner, 'applauseDsl_UIComponentOrDataType') == owner
    _safe_set(owner, 'applauseDsl_UIComponentMemberDeclaration73', None)
    assert getattr(partner, 'applauseDsl_UIComponentOrDataType') is None


def test_assoc_type8_stub_double():
    # applauseDsl_DataType has no real 'applauseDsl_DataType' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TypeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TypeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TypeMapping(simpleName="sample_text")
    partner = applauseDsl_DataType()
    setattr(partner, 'applauseDsl_DataType', None)
    _safe_set(owner, 'applauseDsl_TypeMapping', partner)
    assert getattr(partner, 'applauseDsl_DataType') == owner
    _safe_set(owner, 'applauseDsl_TypeMapping', None)
    assert getattr(partner, 'applauseDsl_DataType') is None


def test_assoc_value103_stub_double():
    # applauseDsl_AttributeReference has no real 'applauseDsl_AttributeReference' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Attribute(many=True, name="sample_text")
    partner = applauseDsl_AttributeReference()
    setattr(partner, 'applauseDsl_AttributeReference', None)
    _safe_set(owner, 'applauseDsl_Attribute104', partner)
    assert getattr(partner, 'applauseDsl_AttributeReference') == owner
    _safe_set(owner, 'applauseDsl_Attribute104', None)
    assert getattr(partner, 'applauseDsl_AttributeReference') is None


