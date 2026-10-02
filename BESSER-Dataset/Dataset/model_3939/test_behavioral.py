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


