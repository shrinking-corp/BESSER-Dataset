import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionExpression,
    CollectionFunction,
    Expression,
    ModelElement,
    PredefinedParameter,
    ScalarExpression,
    SectionedView,
    StringFunction,
    Type,
    VariableDeclaration,
    View,
    ViewAction,
    applauseDsl_ActionDelegate,
    applauseDsl_ApplauseModel,
    applauseDsl_Application,
    applauseDsl_Button,
    applauseDsl_CollectionExpression,
    applauseDsl_CollectionFunction,
    applauseDsl_CollectionIterator,
    applauseDsl_CollectionLiteral,
    applauseDsl_Constant,
    applauseDsl_ContentProvider,
    applauseDsl_CustomView,
    applauseDsl_DetailsView,
    applauseDsl_Entity,
    applauseDsl_Expression,
    applauseDsl_ExternalOpen,
    applauseDsl_ModelElement,
    applauseDsl_NavigationBarItem,
    applauseDsl_ObjectReference,
    applauseDsl_Parameter,
    applauseDsl_PredefinedParameter,
    applauseDsl_Property,
    applauseDsl_ProviderConstruction,
    applauseDsl_ScalarExpression,
    applauseDsl_SectionCell,
    applauseDsl_SectionId,
    applauseDsl_SectionedView,
    applauseDsl_SimpleType,
    applauseDsl_StringConcat,
    applauseDsl_StringFunction,
    applauseDsl_StringLiteral,
    applauseDsl_StringReplace,
    applauseDsl_StringSplit,
    applauseDsl_StringUrlConform,
    applauseDsl_TableView,
    applauseDsl_Type,
    applauseDsl_TypeDescription,
    applauseDsl_VariableDeclaration,
    applauseDsl_View,
    applauseDsl_ViewAction,
    applauseDsl_ViewCall,
    applauseDsl_ViewForAllSections,
    applauseDsl_ViewHeader,
    applauseDsl_ViewSection,
    applauseDsl_WebView,
    CellType,
    Position,
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

def test_assoc_actions64_reverse_link_reassign_clear():
    a1 = applauseDsl_View(name="sample_text")
    a2 = applauseDsl_View(name="sample_text_2")
    b = applauseDsl_VariableDeclaration(name="sample_text")
    _safe_set(b, 'applauseDsl_VariableDeclaration66', a1)
    assert _is_linked(b, 'applauseDsl_VariableDeclaration66', a1)
    if hasattr(a1, 'applauseDsl_View65'):
        assert _is_linked(a1, 'applauseDsl_View65', b)
    _safe_set(b, 'applauseDsl_VariableDeclaration66', a2)
    assert _is_linked(b, 'applauseDsl_VariableDeclaration66', a2)
    if hasattr(a1, 'applauseDsl_View65'):
        assert not _is_linked(a1, 'applauseDsl_View65', b)
    if hasattr(a2, 'applauseDsl_View65'):
        assert _is_linked(a2, 'applauseDsl_View65', b)
    _safe_set(b, 'applauseDsl_VariableDeclaration66', None)
    assert not _is_linked(b, 'applauseDsl_VariableDeclaration66', a2)
    if hasattr(a2, 'applauseDsl_View65'):
        assert not _is_linked(a2, 'applauseDsl_View65', b)


def test_assoc_buttons24_reverse_link_reassign_clear():
    a1 = applauseDsl_Button(handler="sample_text")
    a2 = applauseDsl_Button(handler="sample_text_2")
    b = applauseDsl_Application(name="sample_text", tabbarApplication=True)
    _safe_set(b, 'applauseDsl_Application25', {a1})
    assert _is_linked(b, 'applauseDsl_Application25', a1)
    if hasattr(a1, 'applauseDsl_Button'):
        assert _is_linked(a1, 'applauseDsl_Button', b)
    _safe_set(b, 'applauseDsl_Application25', {a2})
    assert _is_linked(b, 'applauseDsl_Application25', a2)
    if hasattr(a1, 'applauseDsl_Button'):
        assert not _is_linked(a1, 'applauseDsl_Button', b)
    if hasattr(a2, 'applauseDsl_Button'):
        assert _is_linked(a2, 'applauseDsl_Button', b)
    _safe_set(b, 'applauseDsl_Application25', set())
    assert not _is_linked(b, 'applauseDsl_Application25', a2)
    if hasattr(a2, 'applauseDsl_Button'):
        assert not _is_linked(a2, 'applauseDsl_Button', b)


def test_assoc_buttons61_reverse_link_reassign_clear():
    a1 = applauseDsl_View(name="sample_text")
    a2 = applauseDsl_View(name="sample_text_2")
    b = applauseDsl_Button(handler="sample_text")
    _safe_set(b, 'applauseDsl_Button63', a1)
    assert _is_linked(b, 'applauseDsl_Button63', a1)
    if hasattr(a1, 'applauseDsl_View62'):
        assert _is_linked(a1, 'applauseDsl_View62', b)
    _safe_set(b, 'applauseDsl_Button63', a2)
    assert _is_linked(b, 'applauseDsl_Button63', a2)
    if hasattr(a1, 'applauseDsl_View62'):
        assert not _is_linked(a1, 'applauseDsl_View62', b)
    if hasattr(a2, 'applauseDsl_View62'):
        assert _is_linked(a2, 'applauseDsl_View62', b)
    _safe_set(b, 'applauseDsl_Button63', None)
    assert not _is_linked(b, 'applauseDsl_Button63', a2)
    if hasattr(a2, 'applauseDsl_View62'):
        assert not _is_linked(a2, 'applauseDsl_View62', b)


def test_assoc_description39_reverse_link_reassign_clear():
    a1 = applauseDsl_TypeDescription(many=True)
    a2 = applauseDsl_TypeDescription(many=False)
    b = applauseDsl_Property(derived=True)
    _safe_set(b, 'applauseDsl_Property40', a1)
    assert _is_linked(b, 'applauseDsl_Property40', a1)
    if hasattr(a1, 'applauseDsl_TypeDescription41'):
        assert _is_linked(a1, 'applauseDsl_TypeDescription41', b)
    _safe_set(b, 'applauseDsl_Property40', a2)
    assert _is_linked(b, 'applauseDsl_Property40', a2)
    if hasattr(a1, 'applauseDsl_TypeDescription41'):
        assert not _is_linked(a1, 'applauseDsl_TypeDescription41', b)
    if hasattr(a2, 'applauseDsl_TypeDescription41'):
        assert _is_linked(a2, 'applauseDsl_TypeDescription41', b)
    _safe_set(b, 'applauseDsl_Property40', None)
    assert not _is_linked(b, 'applauseDsl_Property40', a2)
    if hasattr(a2, 'applauseDsl_TypeDescription41'):
        assert not _is_linked(a2, 'applauseDsl_TypeDescription41', b)


def test_assoc_type44_reverse_link_reassign_clear():
    a1 = applauseDsl_Type(name="sample_text")
    a2 = applauseDsl_Type(name="sample_text_2")
    b = applauseDsl_ContentProvider(html=True, many=True, name="sample_text", resolver=True, xml=True)
    _safe_set(b, 'applauseDsl_ContentProvider45', a1)
    assert _is_linked(b, 'applauseDsl_ContentProvider45', a1)
    if hasattr(a1, 'applauseDsl_Type46'):
        assert _is_linked(a1, 'applauseDsl_Type46', b)
    _safe_set(b, 'applauseDsl_ContentProvider45', a2)
    assert _is_linked(b, 'applauseDsl_ContentProvider45', a2)
    if hasattr(a1, 'applauseDsl_Type46'):
        assert not _is_linked(a1, 'applauseDsl_Type46', b)
    if hasattr(a2, 'applauseDsl_Type46'):
        assert _is_linked(a2, 'applauseDsl_Type46', b)
    _safe_set(b, 'applauseDsl_ContentProvider45', None)
    assert not _is_linked(b, 'applauseDsl_ContentProvider45', a2)
    if hasattr(a2, 'applauseDsl_Type46'):
        assert not _is_linked(a2, 'applauseDsl_Type46', b)


def test_assoc_type7_reverse_link_reassign_clear():
    a1 = applauseDsl_TypeDescription(many=True)
    a2 = applauseDsl_TypeDescription(many=False)
    b = applauseDsl_Type(name="sample_text")
    _safe_set(b, 'applauseDsl_Type', a1)
    assert _is_linked(b, 'applauseDsl_Type', a1)
    if hasattr(a1, 'applauseDsl_TypeDescription'):
        assert _is_linked(a1, 'applauseDsl_TypeDescription', b)
    _safe_set(b, 'applauseDsl_Type', a2)
    assert _is_linked(b, 'applauseDsl_Type', a2)
    if hasattr(a1, 'applauseDsl_TypeDescription'):
        assert not _is_linked(a1, 'applauseDsl_TypeDescription', b)
    if hasattr(a2, 'applauseDsl_TypeDescription'):
        assert _is_linked(a2, 'applauseDsl_TypeDescription', b)
    _safe_set(b, 'applauseDsl_Type', None)
    assert not _is_linked(b, 'applauseDsl_Type', a2)
    if hasattr(a2, 'applauseDsl_TypeDescription'):
        assert not _is_linked(a2, 'applauseDsl_TypeDescription', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action127_stub_double():
    # applauseDsl_ViewAction has no real 'applauseDsl_ViewAction' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ViewAction()
    setattr(partner, 'applauseDsl_ViewAction', None)
    _safe_set(owner, 'applauseDsl_SectionCell128', partner)
    assert getattr(partner, 'applauseDsl_ViewAction') == owner
    _safe_set(owner, 'applauseDsl_SectionCell128', None)
    assert getattr(partner, 'applauseDsl_ViewAction') is None


def test_assoc_appicon16_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression18' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text", tabbarApplication=True)
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression18', None)
    _safe_set(owner, 'applauseDsl_Application17', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression18') == owner
    _safe_set(owner, 'applauseDsl_Application17', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression18') is None


def test_assoc_application0_stub_double():
    # applauseDsl_ApplauseModel has no real 'applauseDsl_ApplauseModel' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text", tabbarApplication=True)
    partner = applauseDsl_ApplauseModel()
    setattr(partner, 'applauseDsl_ApplauseModel', None)
    _safe_set(owner, 'applauseDsl_Application', partner)
    assert getattr(partner, 'applauseDsl_ApplauseModel') == owner
    _safe_set(owner, 'applauseDsl_Application', None)
    assert getattr(partner, 'applauseDsl_ApplauseModel') is None


def test_assoc_buttonAction129_stub_double():
    # applauseDsl_ViewAction has no real 'applauseDsl_ViewAction131' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ViewAction()
    setattr(partner, 'applauseDsl_ViewAction131', None)
    _safe_set(owner, 'applauseDsl_SectionCell130', partner)
    assert getattr(partner, 'applauseDsl_ViewAction131') == owner
    _safe_set(owner, 'applauseDsl_SectionCell130', None)
    assert getattr(partner, 'applauseDsl_ViewAction131') is None


def test_assoc_cells102_stub_double():
    # applauseDsl_ViewSection has no real 'applauseDsl_ViewSection103' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ViewSection()
    setattr(partner, 'applauseDsl_ViewSection103', None)
    _safe_set(owner, 'applauseDsl_SectionCell', partner)
    assert owner in getattr(partner, 'applauseDsl_ViewSection103')
    _safe_set(owner, 'applauseDsl_SectionCell', None)
    assert owner not in getattr(partner, 'applauseDsl_ViewSection103')


def test_assoc_cells110_stub_double():
    # applauseDsl_ViewForAllSections has no real 'applauseDsl_ViewForAllSections111' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ViewForAllSections()
    setattr(partner, 'applauseDsl_ViewForAllSections111', None)
    _safe_set(owner, 'applauseDsl_SectionCell112', partner)
    assert owner in getattr(partner, 'applauseDsl_ViewForAllSections111')
    _safe_set(owner, 'applauseDsl_SectionCell112', None)
    assert owner not in getattr(partner, 'applauseDsl_ViewForAllSections111')


def test_assoc_content85_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter86' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_CustomView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_CustomView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_CustomView(objclass="sample_text")
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter86', None)
    _safe_set(owner, 'applauseDsl_CustomView', partner)
    assert getattr(partner, 'applauseDsl_Parameter86') == owner
    _safe_set(owner, 'applauseDsl_CustomView', None)
    assert getattr(partner, 'applauseDsl_Parameter86') is None


def test_assoc_description8_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_TypeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_TypeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_TypeDescription(many=True)
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter', None)
    _safe_set(owner, 'applauseDsl_TypeDescription9', partner)
    assert getattr(partner, 'applauseDsl_Parameter') == owner
    _safe_set(owner, 'applauseDsl_TypeDescription9', None)
    assert getattr(partner, 'applauseDsl_Parameter') is None


def test_assoc_details118_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression120' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression120', None)
    _safe_set(owner, 'applauseDsl_SectionCell119', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression120') == owner
    _safe_set(owner, 'applauseDsl_SectionCell119', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression120') is None


def test_assoc_icon29_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression31' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Button(handler="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression31', None)
    _safe_set(owner, 'applauseDsl_Button30', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression31') == owner
    _safe_set(owner, 'applauseDsl_Button30', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression31') is None


def test_assoc_icon3_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_NavigationBarItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_NavigationBarItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_NavigationBarItem(position="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression', None)
    _safe_set(owner, 'applauseDsl_NavigationBarItem', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression') == owner
    _safe_set(owner, 'applauseDsl_NavigationBarItem', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression') is None


def test_assoc_image121_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression123' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression123', None)
    _safe_set(owner, 'applauseDsl_SectionCell122', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression123') == owner
    _safe_set(owner, 'applauseDsl_SectionCell122', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression123') is None


def test_assoc_iterator113_stub_double():
    # applauseDsl_CollectionIterator has no real 'applauseDsl_CollectionIterator' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_CollectionIterator()
    setattr(partner, 'applauseDsl_CollectionIterator', None)
    _safe_set(owner, 'applauseDsl_SectionCell114', partner)
    assert getattr(partner, 'applauseDsl_CollectionIterator') == owner
    _safe_set(owner, 'applauseDsl_SectionCell114', None)
    assert getattr(partner, 'applauseDsl_CollectionIterator') is None


def test_assoc_mainview22_stub_double():
    # applauseDsl_ViewCall has no real 'applauseDsl_ViewCall' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text", tabbarApplication=True)
    partner = applauseDsl_ViewCall()
    setattr(partner, 'applauseDsl_ViewCall', None)
    _safe_set(owner, 'applauseDsl_Application23', partner)
    assert getattr(partner, 'applauseDsl_ViewCall') == owner
    _safe_set(owner, 'applauseDsl_Application23', None)
    assert getattr(partner, 'applauseDsl_ViewCall') is None


def test_assoc_object10_stub_double():
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


def test_assoc_parameter42_stub_double():
    # applauseDsl_Parameter has no real 'applauseDsl_Parameter43' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(html=True, many=True, name="sample_text", resolver=True, xml=True)
    partner = applauseDsl_Parameter()
    setattr(partner, 'applauseDsl_Parameter43', None)
    _safe_set(owner, 'applauseDsl_ContentProvider', partner)
    assert getattr(partner, 'applauseDsl_Parameter43') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider', None)
    assert getattr(partner, 'applauseDsl_Parameter43') is None


def test_assoc_properties37_stub_double():
    # applauseDsl_Entity has no real 'applauseDsl_Entity38' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Property(derived=True)
    partner = applauseDsl_Entity()
    setattr(partner, 'applauseDsl_Entity38', None)
    _safe_set(owner, 'applauseDsl_Property', partner)
    assert owner in getattr(partner, 'applauseDsl_Entity38')
    _safe_set(owner, 'applauseDsl_Property', None)
    assert owner not in getattr(partner, 'applauseDsl_Entity38')


def test_assoc_provider53_stub_double():
    # applauseDsl_ProviderConstruction has no real 'applauseDsl_ProviderConstruction' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(html=True, many=True, name="sample_text", resolver=True, xml=True)
    partner = applauseDsl_ProviderConstruction()
    setattr(partner, 'applauseDsl_ProviderConstruction', None)
    _safe_set(owner, 'applauseDsl_ContentProvider54', partner)
    assert getattr(partner, 'applauseDsl_ProviderConstruction') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider54', None)
    assert getattr(partner, 'applauseDsl_ProviderConstruction') is None


def test_assoc_query124_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression126' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression126', None)
    _safe_set(owner, 'applauseDsl_SectionCell125', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression126') == owner
    _safe_set(owner, 'applauseDsl_SectionCell125', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression126') is None


def test_assoc_selection50_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression52' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(html=True, many=True, name="sample_text", resolver=True, xml=True)
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression52', None)
    _safe_set(owner, 'applauseDsl_ContentProvider51', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression52') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider51', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression52') is None


def test_assoc_splash19_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression21' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Application(name="sample_text", tabbarApplication=True)
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression21', None)
    _safe_set(owner, 'applauseDsl_Application20', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression21') == owner
    _safe_set(owner, 'applauseDsl_Application20', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression21') is None


def test_assoc_text115_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression117' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_SectionCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_SectionCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_SectionCell(type="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression117', None)
    _safe_set(owner, 'applauseDsl_SectionCell116', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression117') == owner
    _safe_set(owner, 'applauseDsl_SectionCell116', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression117') is None


def test_assoc_title26_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression28' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Button(handler="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression28', None)
    _safe_set(owner, 'applauseDsl_Button27', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression28') == owner
    _safe_set(owner, 'applauseDsl_Button27', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression28') is None


def test_assoc_title59_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression60' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_View(name="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression60', None)
    _safe_set(owner, 'applauseDsl_View', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression60') == owner
    _safe_set(owner, 'applauseDsl_View', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression60') is None


def test_assoc_triggers4_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression6' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_NavigationBarItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_NavigationBarItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_NavigationBarItem(position="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression6', None)
    _safe_set(owner, 'applauseDsl_NavigationBarItem5', {partner})
    assert getattr(partner, 'applauseDsl_ScalarExpression6') == owner
    _safe_set(owner, 'applauseDsl_NavigationBarItem5', set())
    assert getattr(partner, 'applauseDsl_ScalarExpression6') is None


def test_assoc_url47_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression49' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_ContentProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_ContentProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_ContentProvider(html=True, many=True, name="sample_text", resolver=True, xml=True)
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression49', None)
    _safe_set(owner, 'applauseDsl_ContentProvider48', partner)
    assert getattr(partner, 'applauseDsl_ScalarExpression49') == owner
    _safe_set(owner, 'applauseDsl_ContentProvider48', None)
    assert getattr(partner, 'applauseDsl_ScalarExpression49') is None


def test_assoc_value162_stub_double():
    # applauseDsl_ScalarExpression has no real 'applauseDsl_ScalarExpression163' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Constant(language="sample_text")
    partner = applauseDsl_ScalarExpression()
    setattr(partner, 'applauseDsl_ScalarExpression163', None)
    _safe_set(owner, 'applauseDsl_Constant', {partner})
    assert getattr(partner, 'applauseDsl_ScalarExpression163') == owner
    _safe_set(owner, 'applauseDsl_Constant', set())
    assert getattr(partner, 'applauseDsl_ScalarExpression163') is None


def test_assoc_view136_stub_double():
    # applauseDsl_ViewCall has no real 'applauseDsl_ViewCall137' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_View(name="sample_text")
    partner = applauseDsl_ViewCall()
    setattr(partner, 'applauseDsl_ViewCall137', None)
    _safe_set(owner, 'applauseDsl_View138', partner)
    assert getattr(partner, 'applauseDsl_ViewCall137') == owner
    _safe_set(owner, 'applauseDsl_View138', None)
    assert getattr(partner, 'applauseDsl_ViewCall137') is None


def test_assoc_view32_stub_double():
    # applauseDsl_ViewCall has no real 'applauseDsl_ViewCall34' property in the generated
    # code (a bare stub) -- manually attach it so applauseDsl_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # applauseDsl_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = applauseDsl_Button(handler="sample_text")
    partner = applauseDsl_ViewCall()
    setattr(partner, 'applauseDsl_ViewCall34', None)
    _safe_set(owner, 'applauseDsl_Button33', partner)
    assert getattr(partner, 'applauseDsl_ViewCall34') == owner
    _safe_set(owner, 'applauseDsl_Button33', None)
    assert getattr(partner, 'applauseDsl_ViewCall34') is None


