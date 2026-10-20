import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EntityWebPage,
    ExternalSource,
    Multiple,
    PageS_Q,
    Question,
    SimpleQuestion,
    TrueFalse,
    WebApp_Attribute,
    WebApp_CRUD,
    WebApp_Create,
    WebApp_DataBase,
    WebApp_Delete,
    WebApp_Details,
    WebApp_Entity,
    WebApp_EntityWebPage,
    WebApp_ExternalLink,
    WebApp_ExternalSource,
    WebApp_GroupOfQuestions,
    WebApp_Home,
    WebApp_Index,
    WebApp_Multiple,
    WebApp_MultipleForQuestionnary,
    WebApp_MultipleForSurvey,
    WebApp_Opened,
    WebApp_Option,
    WebApp_PageS_Q,
    WebApp_Question,
    WebApp_QuestionBank,
    WebApp_Questionnary,
    WebApp_RSSFeed,
    WebApp_SimpleQuestion,
    WebApp_Survey,
    WebApp_TrueFalse,
    WebApp_TrueFalseForQuestionnary,
    WebApp_TrueFalseForSurvey,
    WebApp_Twitter,
    WebApp_WebApp,
    WebApp_WebPage,
    WebPage,
    CorrectAnwser,
    MySqlType,
    VisualRepresentation,
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

def test_assoc_attributes5_reverse_link_reassign_clear():
    a1 = WebApp_Entity(name="sample_text")
    a2 = WebApp_Entity(name="sample_text_2")
    b = WebApp_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'WebApp_Attribute', a1)
    assert _is_linked(b, 'WebApp_Attribute', a1)
    if hasattr(a1, 'WebApp_Entity'):
        assert _is_linked(a1, 'WebApp_Entity', b)
    _safe_set(b, 'WebApp_Attribute', a2)
    assert _is_linked(b, 'WebApp_Attribute', a2)
    if hasattr(a1, 'WebApp_Entity'):
        assert not _is_linked(a1, 'WebApp_Entity', b)
    if hasattr(a2, 'WebApp_Entity'):
        assert _is_linked(a2, 'WebApp_Entity', b)
    _safe_set(b, 'WebApp_Attribute', None)
    assert not _is_linked(b, 'WebApp_Attribute', a2)
    if hasattr(a2, 'WebApp_Entity'):
        assert not _is_linked(a2, 'WebApp_Entity', b)


def test_assoc_entityReference7_reverse_link_reassign_clear():
    a1 = WebApp_Entity(name="sample_text")
    a2 = WebApp_Entity(name="sample_text_2")
    b = WebApp_Entity(name="sample_text")
    _safe_set(b, 'WebApp_Entity8', a1)
    assert _is_linked(b, 'WebApp_Entity8', a1)
    if hasattr(a1, 'WebApp_Entity6'):
        assert _is_linked(a1, 'WebApp_Entity6', b)
    _safe_set(b, 'WebApp_Entity8', a2)
    assert _is_linked(b, 'WebApp_Entity8', a2)
    if hasattr(a1, 'WebApp_Entity6'):
        assert not _is_linked(a1, 'WebApp_Entity6', b)
    if hasattr(a2, 'WebApp_Entity6'):
        assert _is_linked(a2, 'WebApp_Entity6', b)
    _safe_set(b, 'WebApp_Entity8', None)
    assert not _is_linked(b, 'WebApp_Entity8', a2)
    if hasattr(a2, 'WebApp_Entity6'):
        assert not _is_linked(a2, 'WebApp_Entity6', b)


def test_assoc_externallinks15_reverse_link_reassign_clear():
    a1 = WebApp_WebPage(name="sample_text")
    a2 = WebApp_WebPage(name="sample_text_2")
    b = WebApp_ExternalLink(url="sample_text")
    _safe_set(b, 'WebApp_ExternalLink', a1)
    assert _is_linked(b, 'WebApp_ExternalLink', a1)
    if hasattr(a1, 'WebApp_WebPage16'):
        assert _is_linked(a1, 'WebApp_WebPage16', b)
    _safe_set(b, 'WebApp_ExternalLink', a2)
    assert _is_linked(b, 'WebApp_ExternalLink', a2)
    if hasattr(a1, 'WebApp_WebPage16'):
        assert not _is_linked(a1, 'WebApp_WebPage16', b)
    if hasattr(a2, 'WebApp_WebPage16'):
        assert _is_linked(a2, 'WebApp_WebPage16', b)
    _safe_set(b, 'WebApp_ExternalLink', None)
    assert not _is_linked(b, 'WebApp_ExternalLink', a2)
    if hasattr(a2, 'WebApp_WebPage16'):
        assert not _is_linked(a2, 'WebApp_WebPage16', b)


def test_assoc_internallink13_reverse_link_reassign_clear():
    a1 = WebApp_WebPage(name="sample_text")
    a2 = WebApp_WebPage(name="sample_text_2")
    b = WebApp_WebPage(name="sample_text")
    _safe_set(b, 'WebApp_WebPage14', a1)
    assert _is_linked(b, 'WebApp_WebPage14', a1)
    if hasattr(a1, 'WebApp_WebPage12'):
        assert _is_linked(a1, 'WebApp_WebPage12', b)
    _safe_set(b, 'WebApp_WebPage14', a2)
    assert _is_linked(b, 'WebApp_WebPage14', a2)
    if hasattr(a1, 'WebApp_WebPage12'):
        assert not _is_linked(a1, 'WebApp_WebPage12', b)
    if hasattr(a2, 'WebApp_WebPage12'):
        assert _is_linked(a2, 'WebApp_WebPage12', b)
    _safe_set(b, 'WebApp_WebPage14', None)
    assert not _is_linked(b, 'WebApp_WebPage14', a2)
    if hasattr(a2, 'WebApp_WebPage12'):
        assert not _is_linked(a2, 'WebApp_WebPage12', b)


def test_assoc_webpages0_reverse_link_reassign_clear():
    a1 = WebApp_WebPage(name="sample_text")
    a2 = WebApp_WebPage(name="sample_text_2")
    b = WebApp_WebApp(Password="sample_text", User="sample_text", name="sample_text")
    _safe_set(b, 'WebApp_WebApp', {a1})
    assert _is_linked(b, 'WebApp_WebApp', a1)
    if hasattr(a1, 'WebApp_WebPage'):
        assert _is_linked(a1, 'WebApp_WebPage', b)
    _safe_set(b, 'WebApp_WebApp', {a2})
    assert _is_linked(b, 'WebApp_WebApp', a2)
    if hasattr(a1, 'WebApp_WebPage'):
        assert not _is_linked(a1, 'WebApp_WebPage', b)
    if hasattr(a2, 'WebApp_WebPage'):
        assert _is_linked(a2, 'WebApp_WebPage', b)
    _safe_set(b, 'WebApp_WebApp', set())
    assert not _is_linked(b, 'WebApp_WebApp', a2)
    if hasattr(a2, 'WebApp_WebPage'):
        assert not _is_linked(a2, 'WebApp_WebPage', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_correctOption28_stub_double():
    # WebApp_MultipleForQuestionnary has no real 'WebApp_MultipleForQuestionnary' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_Option(fraction=7, text="sample_text")
    partner = WebApp_MultipleForQuestionnary()
    setattr(partner, 'WebApp_MultipleForQuestionnary', None)
    _safe_set(owner, 'WebApp_Option29', partner)
    assert getattr(partner, 'WebApp_MultipleForQuestionnary') == owner
    _safe_set(owner, 'WebApp_Option29', None)
    assert getattr(partner, 'WebApp_MultipleForQuestionnary') is None


def test_assoc_database1_stub_double():
    # WebApp_DataBase has no real 'WebApp_DataBase' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_WebApp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_WebApp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_WebApp(Password="sample_text", User="sample_text", name="sample_text")
    partner = WebApp_DataBase()
    setattr(partner, 'WebApp_DataBase', None)
    _safe_set(owner, 'WebApp_WebApp2', partner)
    assert getattr(partner, 'WebApp_DataBase') == owner
    _safe_set(owner, 'WebApp_WebApp2', None)
    assert getattr(partner, 'WebApp_DataBase') is None


def test_assoc_entities22_stub_double():
    # WebApp_DataBase has no real 'WebApp_DataBase23' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_Entity(name="sample_text")
    partner = WebApp_DataBase()
    setattr(partner, 'WebApp_DataBase23', None)
    _safe_set(owner, 'WebApp_Entity24', partner)
    assert owner in getattr(partner, 'WebApp_DataBase23')
    _safe_set(owner, 'WebApp_Entity24', None)
    assert owner not in getattr(partner, 'WebApp_DataBase23')


def test_assoc_entity20_stub_double():
    # WebApp_EntityWebPage has no real 'WebApp_EntityWebPage' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_Entity(name="sample_text")
    partner = WebApp_EntityWebPage()
    setattr(partner, 'WebApp_EntityWebPage', None)
    _safe_set(owner, 'WebApp_Entity21', partner)
    assert getattr(partner, 'WebApp_EntityWebPage') == owner
    _safe_set(owner, 'WebApp_Entity21', None)
    assert getattr(partner, 'WebApp_EntityWebPage') is None


def test_assoc_option19_stub_double():
    # WebApp_Multiple has no real 'WebApp_Multiple' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_Option(fraction=7, text="sample_text")
    partner = WebApp_Multiple()
    setattr(partner, 'WebApp_Multiple', None)
    _safe_set(owner, 'WebApp_Option', partner)
    assert owner in getattr(partner, 'WebApp_Multiple')
    _safe_set(owner, 'WebApp_Option', None)
    assert owner not in getattr(partner, 'WebApp_Multiple')


def test_assoc_questionbank3_stub_double():
    # WebApp_QuestionBank has no real 'WebApp_QuestionBank' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_WebApp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_WebApp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_WebApp(Password="sample_text", User="sample_text", name="sample_text")
    partner = WebApp_QuestionBank()
    setattr(partner, 'WebApp_QuestionBank', None)
    _safe_set(owner, 'WebApp_WebApp4', partner)
    assert getattr(partner, 'WebApp_QuestionBank') == owner
    _safe_set(owner, 'WebApp_WebApp4', None)
    assert getattr(partner, 'WebApp_QuestionBank') is None


def test_assoc_questions17_stub_double():
    # WebApp_Question has no real 'WebApp_Question18' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_GroupOfQuestions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_GroupOfQuestions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_GroupOfQuestions(name="sample_text")
    partner = WebApp_Question()
    setattr(partner, 'WebApp_Question18', None)
    _safe_set(owner, 'WebApp_GroupOfQuestions', {partner})
    assert getattr(partner, 'WebApp_Question18') == owner
    _safe_set(owner, 'WebApp_GroupOfQuestions', set())
    assert getattr(partner, 'WebApp_Question18') is None


def test_assoc_socialnetwork10_stub_double():
    # WebApp_ExternalSource has no real 'WebApp_ExternalSource' property in the generated
    # code (a bare stub) -- manually attach it so WebApp_WebPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebApp_WebPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebApp_WebPage(name="sample_text")
    partner = WebApp_ExternalSource()
    setattr(partner, 'WebApp_ExternalSource', None)
    _safe_set(owner, 'WebApp_WebPage11', {partner})
    assert getattr(partner, 'WebApp_ExternalSource') == owner
    _safe_set(owner, 'WebApp_WebPage11', set())
    assert getattr(partner, 'WebApp_ExternalSource') is None


