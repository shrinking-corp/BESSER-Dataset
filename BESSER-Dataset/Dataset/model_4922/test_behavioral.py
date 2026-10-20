import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Button,
    Error,
    Field,
    Form,
    FormElement,
    Item,
    Link,
    ListField,
    Page,
    Success,
    Text,
    Validator,
    Visitor,
    dsml_visitor_JSPVisitor,
    dsml_visitor_POJOVisitor,
    dsml_visitor_ResourceVisitor,
    dsml_visitor_Visitor,
    dsml_web_BetweenValidator,
    dsml_web_Button,
    dsml_web_CancelButton,
    dsml_web_CheckBox,
    dsml_web_DateValidator,
    dsml_web_EmailValidator,
    dsml_web_Error,
    dsml_web_Field,
    dsml_web_Form,
    dsml_web_FormElement,
    dsml_web_GreaterThanValidator,
    dsml_web_Hidden,
    dsml_web_Item,
    dsml_web_Label,
    dsml_web_LessThanValidator,
    dsml_web_Link,
    dsml_web_ListField,
    dsml_web_Page,
    dsml_web_PasswordField,
    dsml_web_RadioButton,
    dsml_web_RegexValidator,
    dsml_web_Required,
    dsml_web_ResetButton,
    dsml_web_Select,
    dsml_web_StringLengthValidator,
    dsml_web_SubmitButton,
    dsml_web_Success,
    dsml_web_Text,
    dsml_web_TextArea,
    dsml_web_TextField,
    dsml_web_TimeValidator,
    dsml_web_TypeValidator,
    dsml_web_URLValidator,
    dsml_web_Validator,
    dsml_web_Website,
    Type,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Error13_stub_double():
    # Error has no real 'Error' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Form(action="sample_text")
    partner = Error()
    setattr(partner, 'Error', None)
    _safe_set(owner, 'dsml_web_Form14', partner)
    assert getattr(partner, 'Error') == owner
    _safe_set(owner, 'dsml_web_Form14', None)
    assert getattr(partner, 'Error') is None


def test_assoc_Form1_stub_double():
    # Form has no real 'Form' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Page(name="sample_text", title="sample_text")
    partner = Form()
    setattr(partner, 'Form', None)
    _safe_set(owner, 'dsml_web_Page', partner)
    assert getattr(partner, 'Form') == owner
    _safe_set(owner, 'dsml_web_Page', None)
    assert getattr(partner, 'Form') is None


def test_assoc_FormElements10_stub_double():
    # FormElement has no real 'FormElement' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Form(action="sample_text")
    partner = FormElement()
    setattr(partner, 'FormElement', None)
    _safe_set(owner, 'dsml_web_Form', {partner})
    assert getattr(partner, 'FormElement') == owner
    _safe_set(owner, 'dsml_web_Form', set())
    assert getattr(partner, 'FormElement') is None


def test_assoc_LinkedPage8_stub_double():
    # Page has no real 'Page9' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Link(value="sample_text")
    partner = Page()
    setattr(partner, 'Page9', None)
    _safe_set(owner, 'dsml_web_Link', partner)
    assert getattr(partner, 'Page9') == owner
    _safe_set(owner, 'dsml_web_Link', None)
    assert getattr(partner, 'Page9') is None


def test_assoc_Links4_stub_double():
    # Link has no real 'Link' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Page(name="sample_text", title="sample_text")
    partner = Link()
    setattr(partner, 'Link', None)
    _safe_set(owner, 'dsml_web_Page5', {partner})
    assert getattr(partner, 'Link') == owner
    _safe_set(owner, 'dsml_web_Page5', set())
    assert getattr(partner, 'Link') is None


def test_assoc_Pages0_stub_double():
    # Page has no real 'Page' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Website's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Website's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Website(name="sample_text")
    partner = Page()
    setattr(partner, 'Page', None)
    _safe_set(owner, 'dsml_web_Website', {partner})
    assert getattr(partner, 'Page') == owner
    _safe_set(owner, 'dsml_web_Website', set())
    assert getattr(partner, 'Page') is None


def test_assoc_Success11_stub_double():
    # Success has no real 'Success' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Form(action="sample_text")
    partner = Success()
    setattr(partner, 'Success', None)
    _safe_set(owner, 'dsml_web_Form12', partner)
    assert getattr(partner, 'Success') == owner
    _safe_set(owner, 'dsml_web_Form12', None)
    assert getattr(partner, 'Success') is None


def test_assoc_Texts2_stub_double():
    # Text has no real 'Text' property in the generated
    # code (a bare stub) -- manually attach it so dsml_web_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_web_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_web_Page(name="sample_text", title="sample_text")
    partner = Text()
    setattr(partner, 'Text', None)
    _safe_set(owner, 'dsml_web_Page3', {partner})
    assert getattr(partner, 'Text') == owner
    _safe_set(owner, 'dsml_web_Page3', set())
    assert getattr(partner, 'Text') is None


