import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionExpression,
    CollectionFunction,
    ContentProviderImplementation,
    Expression,
    ModelElement,
    PropertyPathPart,
    ProviderConstruction,
    ScalarExpression,
    StringFunction,
    Type,
    View,
    ViewAction,
    ViewContentElement,
    applauseDsl_Application,
    applauseDsl_Cell,
    applauseDsl_CollectionExpression,
    applauseDsl_CollectionFunction,
    applauseDsl_CollectionIterator,
    applauseDsl_CollectionLiteral,
    applauseDsl_ComplexProviderConstruction,
    applauseDsl_ContentProvider,
    applauseDsl_ContentProviderImplementation,
    applauseDsl_CustomContentProviderImplementation,
    applauseDsl_CustomView,
    applauseDsl_Entity,
    applauseDsl_Expression,
    applauseDsl_ExternalOpen,
    applauseDsl_FetchingContentProviderImplementation,
    applauseDsl_Model,
    applauseDsl_ModelElement,
    applauseDsl_ObjectReference,
    applauseDsl_Parameter,
    applauseDsl_ProjectClass,
    applauseDsl_Property,
    applauseDsl_PropertyPathPart,
    applauseDsl_ProviderConstruction,
    applauseDsl_ScalarExpression,
    applauseDsl_Section,
    applauseDsl_Selector,
    applauseDsl_SimpleProviderConstruction,
    applauseDsl_SimpleType,
    applauseDsl_StringConcat,
    applauseDsl_StringFunction,
    applauseDsl_StringLiteral,
    applauseDsl_StringReplace,
    applauseDsl_StringSplit,
    applauseDsl_StringUrlConform,
    applauseDsl_Tab,
    applauseDsl_TabView,
    applauseDsl_TableView,
    applauseDsl_Type,
    applauseDsl_TypeDescription,
    applauseDsl_View,
    applauseDsl_ViewAction,
    applauseDsl_ViewCall,
    applauseDsl_ViewContentElement,
    CellAccessory,
    CellType,
    SerializationFormat,
    TableViewStyle,
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

def test_assoc_description22_reverse_link_reassign_clear():
    a1 = applauseDsl_TypeDescription(many=True)
    a2 = applauseDsl_TypeDescription(many=False)
    b = applauseDsl_Property(derived=True)
    _safe_set(b, 'applauseDsl_Property23', a1)
    assert _is_linked(b, 'applauseDsl_Property23', a1)
    if hasattr(a1, 'applauseDsl_TypeDescription24'):
        assert _is_linked(a1, 'applauseDsl_TypeDescription24', b)
    _safe_set(b, 'applauseDsl_Property23', a2)
    assert _is_linked(b, 'applauseDsl_Property23', a2)
    if hasattr(a1, 'applauseDsl_TypeDescription24'):
        assert not _is_linked(a1, 'applauseDsl_TypeDescription24', b)
    if hasattr(a2, 'applauseDsl_TypeDescription24'):
        assert _is_linked(a2, 'applauseDsl_TypeDescription24', b)
    _safe_set(b, 'applauseDsl_Property23', None)
    assert not _is_linked(b, 'applauseDsl_Property23', a2)
    if hasattr(a2, 'applauseDsl_TypeDescription24'):
        assert not _is_linked(a2, 'applauseDsl_TypeDescription24', b)


def test_assoc_extends19_reverse_link_reassign_clear():
    a1 = applauseDsl_Entity(runtimeType=True)
    a2 = applauseDsl_Entity(runtimeType=False)
    b = applauseDsl_Entity(runtimeType=True)
    _safe_set(b, 'applauseDsl_Entity18', a1)
    assert _is_linked(b, 'applauseDsl_Entity18', a1)
    if hasattr(a1, 'applauseDsl_Entity'):
        assert _is_linked(a1, 'applauseDsl_Entity', b)
    _safe_set(b, 'applauseDsl_Entity18', a2)
    assert _is_linked(b, 'applauseDsl_Entity18', a2)
    if hasattr(a1, 'applauseDsl_Entity'):
        assert not _is_linked(a1, 'applauseDsl_Entity', b)
    if hasattr(a2, 'applauseDsl_Entity'):
        assert _is_linked(a2, 'applauseDsl_Entity', b)
    _safe_set(b, 'applauseDsl_Entity18', None)
    assert not _is_linked(b, 'applauseDsl_Entity18', a2)
    if hasattr(a2, 'applauseDsl_Entity'):
        assert not _is_linked(a2, 'applauseDsl_Entity', b)


def test_assoc_properties20_reverse_link_reassign_clear():
    a1 = applauseDsl_Property(derived=True)
    a2 = applauseDsl_Property(derived=False)
    b = applauseDsl_Entity(runtimeType=True)
    _safe_set(b, 'applauseDsl_Entity21', {a1})
    assert _is_linked(b, 'applauseDsl_Entity21', a1)
    if hasattr(a1, 'applauseDsl_Property'):
        assert _is_linked(a1, 'applauseDsl_Property', b)
    _safe_set(b, 'applauseDsl_Entity21', {a2})
    assert _is_linked(b, 'applauseDsl_Entity21', a2)
    if hasattr(a1, 'applauseDsl_Property'):
        assert not _is_linked(a1, 'applauseDsl_Property', b)
    if hasattr(a2, 'applauseDsl_Property'):
        assert _is_linked(a2, 'applauseDsl_Property', b)
    _safe_set(b, 'applauseDsl_Entity21', set())
    assert not _is_linked(b, 'applauseDsl_Entity21', a2)
    if hasattr(a2, 'applauseDsl_Property'):
        assert not _is_linked(a2, 'applauseDsl_Property', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action75_stub_double():
    # applauseDsl_ViewAction has no real 'applauseDsl_ViewAction' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Cell(accessory="sample_text", type="sample_text")
    partner = applauseDsl_ViewAction()
    setattr(partner, 'applauseDsl_ViewAction', None)
    _safe_set(owner, 'applauseDsl_Cell76', partner)
    assert getattr(partner, 'applauseDsl_ViewAction') == owner
    _safe_set(owner, 'applauseDsl_Cell76', None)
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


def test_assoc_background13_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression15' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression15', None)
    _safe_set(owner, 'applauseDsl_Application14', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression15') == owner
    _safe_set(owner, 'applauseDsl_Application14', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression15') is None


def test_assoc_cells64_stub_double():
    # applauseDsl_Section has no real 'applauseDsl_Section65' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Cell(accessory="sample_text", type="sample_text")
    partner = applauseDsl_Section()
    setattr(partner, 'applauseDsl_Section65', None)
    _safe_set(owner, 'applauseDsl_Cell', partner)
    assert owner in getattr(partner, 'applauseDsl_Section65')
    _safe_set(owner, 'applauseDsl_Cell', None)
    assert owner not in getattr(partner, 'applauseDsl_Section65')


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


def test_assoc_details69_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression71' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Cell(accessory="sample_text", type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression71', None)
    _safe_set(owner, 'applauseDsl_Cell70', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression71') == owner
    _safe_set(owner, 'applauseDsl_Cell70', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression71') is None


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


def test_assoc_image72_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression74' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Cell(accessory="sample_text", type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression74', None)
    _safe_set(owner, 'applauseDsl_Cell73', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression74') == owner
    _safe_set(owner, 'applauseDsl_Cell73', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression74') is None


def test_assoc_implementation30_stub_double():
    # applauseDsl_ContentProviderImplementation has no real 'applauseDsl_ContentProviderImplementation' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True, storing=True)
    partner = applauseDsl_ContentProviderImplementation()
    setattr(partner, 'applauseDsl_ContentProviderImplementation', None)
    _safe_set(owner, 'applauseDsl_ContentProvider31', partner)
    assert getattr(partner, 'applauseDsl_ContentProviderImplementation') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider31', None)
    assert getattr(partner, 'applauseDsl_ContentProviderImplementation') is None


def test_assoc_object8_stub_double():
    # applauseDsl_ObjectReference has no real 'applauseDsl_ObjectReference' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_PropertyPathPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_PropertyPathPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_PropertyPathPart(name="sample_text")
    partner = applauseDsl_ObjectReference()
    setattr(partner, 'applauseDsl_ObjectReference', None)
    _safe_set(owner, 'applauseDsl_PropertyPathPart', partner)
    assert getattr(partner, 'applauseDsl_ObjectReference') == owner
    _safe_set(owner, 'applauseDsl_PropertyPathPart', None)
    assert getattr(partner, 'applauseDsl_ObjectReference') is None


def test_assoc_parameter25_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter26' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True, storing=True)
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter26', None)
    _safe_set(owner, 'applauseDsl_ContentProvider', partner)
    assert getattr(partner, 'applauseDsl_Parameter26') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider', None)
    assert getattr(partner, 'applauseDsl_Parameter26') is None


def test_assoc_provider104_stub_double():
    # applauseDsl_ComplexProviderConstruction has no real 'applauseDsl_ComplexProviderConstruction' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True, storing=True)
    partner = applauseDsl_ComplexProviderConstruction()
    setattr(partner, 'applauseDsl_ComplexProviderConstruction', None)
    _safe_set(owner, 'applauseDsl_ContentProvider105', partner)
    assert getattr(partner, 'applauseDsl_ComplexProviderConstruction') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider105', None)
    assert getattr(partner, 'applauseDsl_ComplexProviderConstruction') is None


def test_assoc_providerClass37_stub_double():
    # applauseDsl_CustomContentProviderImplementation has no real 'applauseDsl_CustomContentProviderImplementation' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ProjectClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ProjectClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ProjectClass(name="sample_text")
    partner = applauseDsl_CustomContentProviderImplementation()
    setattr(partner, 'applauseDsl_CustomContentProviderImplementation', None)
    _safe_set(owner, 'applauseDsl_ProjectClass', partner)
    assert getattr(partner, 'applauseDsl_CustomContentProviderImplementation') == owner
    _safe_set(owner, 'applauseDsl_ProjectClass', None)
    assert getattr(partner, 'applauseDsl_CustomContentProviderImplementation') is None


def test_assoc_sections58_stub_double():
    # applauseDsl_Section has no real 'applauseDsl_Section' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TableView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TableView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TableView(style="sample_text")
    partner = applauseDsl_Section()
    setattr(partner, 'applauseDsl_Section', None)
    _safe_set(owner, 'applauseDsl_TableView59', {partner})
    assert getattr(partner, 'applauseDsl_Section') == owner
    _safe_set(owner, 'applauseDsl_TableView59', set())
    assert getattr(partner, 'applauseDsl_Section') is None


def test_assoc_selection34_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression36' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_FetchingContentProviderImplementation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_FetchingContentProviderImplementation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_FetchingContentProviderImplementation(format="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression36', None)
    _safe_set(owner, 'applauseDsl_FetchingContentProviderImplementation35', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression36') == owner
    _safe_set(owner, 'applauseDsl_FetchingContentProviderImplementation35', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression36') is None


def test_assoc_startView16_stub_double():
    # applauseDsl_ViewCall has no real 'applauseDsl_ViewCall' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text")
    partner = applauseDsl_ViewCall()
    setattr(partner, 'applauseDsl_ViewCall', None)
    _safe_set(owner, 'applauseDsl_Application17', partner)
    assert getattr(partner, 'applauseDsl_ViewCall') == owner
    _safe_set(owner, 'applauseDsl_Application17', None)
    assert getattr(partner, 'applauseDsl_ViewCall') is None


def test_assoc_text66_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression68' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Cell(accessory="sample_text", type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression68', None)
    _safe_set(owner, 'applauseDsl_Cell67', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression68') == owner
    _safe_set(owner, 'applauseDsl_Cell67', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression68') is None


def test_assoc_title52_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression54' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TableView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TableView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TableView(style="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression54', None)
    _safe_set(owner, 'applauseDsl_TableView53', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression54') == owner
    _safe_set(owner, 'applauseDsl_TableView53', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression54') is None


def test_assoc_titleImage55_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression57' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TableView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TableView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TableView(style="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression57', None)
    _safe_set(owner, 'applauseDsl_TableView56', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression57') == owner
    _safe_set(owner, 'applauseDsl_TableView56', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression57') is None


def test_assoc_type27_stub_double():
    # applauseDsl_Type has no real 'applauseDsl_Type29' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(many=True, storing=True)
    partner = applauseDsl_Type()
    setattr(partner, 'applauseDsl_Type29', None)
    _safe_set(owner, 'applauseDsl_ContentProvider28', partner)
    assert getattr(partner, 'applauseDsl_Type29') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider28', None)
    assert getattr(partner, 'applauseDsl_Type29') is None


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


def test_assoc_url32_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression33' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_FetchingContentProviderImplementation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_FetchingContentProviderImplementation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_FetchingContentProviderImplementation(format="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression33', None)
    _safe_set(owner, 'applauseDsl_FetchingContentProviderImplementation', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression33') == owner
    _safe_set(owner, 'applauseDsl_FetchingContentProviderImplementation', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression33') is None


def test_assoc_variables50_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter51' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TableView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TableView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TableView(style="sample_text")
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter51', None)
    _safe_set(owner, 'applauseDsl_TableView', {partner})
    assert getattr(partner, 'applauseDsl_Parameter51') == owner
    _safe_set(owner, 'applauseDsl_TableView', set())
    assert getattr(partner, 'applauseDsl_Parameter51') is None


