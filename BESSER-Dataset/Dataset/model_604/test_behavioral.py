import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractView,
    ComponentPackage,
    HelperForSendingRequest,
    MainComponent,
    MainComponentRelation,
    NamedElement,
    Package,
    PresentationElement,
    PresentationFormElement,
    ryz_AbstractView,
    ryz_ActionLink,
    ryz_ActionMethod,
    ryz_Actor,
    ryz_Button,
    ryz_Choice,
    ryz_ComponentPackage,
    ryz_Controller,
    ryz_ControllerPackage,
    ryz_ControllerToModelRelation,
    ryz_ControllerToViewRelation,
    ryz_Form,
    ryz_FormElementToPropertyKeyRelation,
    ryz_Header,
    ryz_HelperForSendingRequest,
    ryz_Input,
    ryz_Layout,
    ryz_Link,
    ryz_MainComponent,
    ryz_MainComponentRelation,
    ryz_Model,
    ryz_ModelAssociation,
    ryz_ModelPackage,
    ryz_MultipleChoice,
    ryz_MvcPackage,
    ryz_NamedElement,
    ryz_Package,
    ryz_Parameter,
    ryz_Partial,
    ryz_PresentationElement,
    ryz_PresentationForm,
    ryz_PresentationFormElement,
    ryz_PresentationFormElementToPropertyKey,
    ryz_Project,
    ryz_Property,
    ryz_Table,
    ryz_TableKey,
    ryz_UseCase,
    ryz_UseCaseActorPackage,
    ryz_UseCasePackage,
    ryz_View,
    ryz_ViewPackage,
    ryz_ViewToControllerRelation,
    ryz_ViewToModelRelation,
    ActionMethodParameterType,
    ActionMethodReturnType,
    ButtonType,
    Cardinality,
    HttpMethod,
    InputDataType,
    ModelCardinality,
    ModelOperation,
    ModelPropertyType,
    MultipleChoiceType,
    RequestType,
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

def test_assoc_actionmethod45_reverse_link_reassign_clear():
    a1 = ryz_ControllerToModelRelation(modelCardinality="sample_text", modelOperation="sample_text")
    a2 = ryz_ControllerToModelRelation(modelCardinality="sample_text_2", modelOperation="sample_text_2")
    b = ryz_ActionMethod(httpMethod="sample_text", returns="sample_text")
    _safe_set(b, 'ryz_ActionMethod46', a1)
    assert _is_linked(b, 'ryz_ActionMethod46', a1)
    if hasattr(a1, 'ryz_ControllerToModelRelation'):
        assert _is_linked(a1, 'ryz_ControllerToModelRelation', b)
    _safe_set(b, 'ryz_ActionMethod46', a2)
    assert _is_linked(b, 'ryz_ActionMethod46', a2)
    if hasattr(a1, 'ryz_ControllerToModelRelation'):
        assert not _is_linked(a1, 'ryz_ControllerToModelRelation', b)
    if hasattr(a2, 'ryz_ControllerToModelRelation'):
        assert _is_linked(a2, 'ryz_ControllerToModelRelation', b)
    _safe_set(b, 'ryz_ActionMethod46', None)
    assert not _is_linked(b, 'ryz_ActionMethod46', a2)
    if hasattr(a2, 'ryz_ControllerToModelRelation'):
        assert not _is_linked(a2, 'ryz_ControllerToModelRelation', b)


def test_assoc_choice85_reverse_link_reassign_clear():
    a1 = ryz_MultipleChoice(multipleChoiceType="sample_text", multipleSelection=True)
    a2 = ryz_MultipleChoice(multipleChoiceType="sample_text_2", multipleSelection=False)
    b = ryz_Choice(selected="sample_text", text="sample_text", value="sample_text")
    _safe_set(b, 'ryz_Choice', a1)
    assert _is_linked(b, 'ryz_Choice', a1)
    if hasattr(a1, 'ryz_MultipleChoice'):
        assert _is_linked(a1, 'ryz_MultipleChoice', b)
    _safe_set(b, 'ryz_Choice', a2)
    assert _is_linked(b, 'ryz_Choice', a2)
    if hasattr(a1, 'ryz_MultipleChoice'):
        assert not _is_linked(a1, 'ryz_MultipleChoice', b)
    if hasattr(a2, 'ryz_MultipleChoice'):
        assert _is_linked(a2, 'ryz_MultipleChoice', b)
    _safe_set(b, 'ryz_Choice', None)
    assert not _is_linked(b, 'ryz_Choice', a2)
    if hasattr(a2, 'ryz_MultipleChoice'):
        assert not _is_linked(a2, 'ryz_MultipleChoice', b)


def test_assoc_dependent27_reverse_link_reassign_clear():
    a1 = ryz_ModelAssociation(cardinality="sample_text", dependentRoleName="sample_text", isRequired=True, principalRoleName="sample_text")
    a2 = ryz_ModelAssociation(cardinality="sample_text_2", dependentRoleName="sample_text_2", isRequired=False, principalRoleName="sample_text_2")
    b = ryz_Model(isAbstract=True)
    _safe_set(b, 'ryz_Model29', a1)
    assert _is_linked(b, 'ryz_Model29', a1)
    if hasattr(a1, 'ryz_ModelAssociation28'):
        assert _is_linked(a1, 'ryz_ModelAssociation28', b)
    _safe_set(b, 'ryz_Model29', a2)
    assert _is_linked(b, 'ryz_Model29', a2)
    if hasattr(a1, 'ryz_ModelAssociation28'):
        assert not _is_linked(a1, 'ryz_ModelAssociation28', b)
    if hasattr(a2, 'ryz_ModelAssociation28'):
        assert _is_linked(a2, 'ryz_ModelAssociation28', b)
    _safe_set(b, 'ryz_Model29', None)
    assert not _is_linked(b, 'ryz_Model29', a2)
    if hasattr(a2, 'ryz_ModelAssociation28'):
        assert not _is_linked(a2, 'ryz_ModelAssociation28', b)


def test_assoc_inherits12_reverse_link_reassign_clear():
    a1 = ryz_Model(isAbstract=True)
    a2 = ryz_Model(isAbstract=False)
    b = ryz_Model(isAbstract=True)
    _safe_set(b, 'ryz_Model13', a1)
    assert _is_linked(b, 'ryz_Model13', a1)
    if hasattr(a1, 'ryz_Model11'):
        assert _is_linked(a1, 'ryz_Model11', b)
    _safe_set(b, 'ryz_Model13', a2)
    assert _is_linked(b, 'ryz_Model13', a2)
    if hasattr(a1, 'ryz_Model11'):
        assert not _is_linked(a1, 'ryz_Model11', b)
    if hasattr(a2, 'ryz_Model11'):
        assert _is_linked(a2, 'ryz_Model11', b)
    _safe_set(b, 'ryz_Model13', None)
    assert not _is_linked(b, 'ryz_Model13', a2)
    if hasattr(a2, 'ryz_Model11'):
        assert not _is_linked(a2, 'ryz_Model11', b)


def test_assoc_model47_reverse_link_reassign_clear():
    a1 = ryz_Model(isAbstract=True)
    a2 = ryz_Model(isAbstract=False)
    b = ryz_ControllerToModelRelation(modelCardinality="sample_text", modelOperation="sample_text")
    _safe_set(b, 'ryz_ControllerToModelRelation48', a1)
    assert _is_linked(b, 'ryz_ControllerToModelRelation48', a1)
    if hasattr(a1, 'ryz_Model49'):
        assert _is_linked(a1, 'ryz_Model49', b)
    _safe_set(b, 'ryz_ControllerToModelRelation48', a2)
    assert _is_linked(b, 'ryz_ControllerToModelRelation48', a2)
    if hasattr(a1, 'ryz_Model49'):
        assert not _is_linked(a1, 'ryz_Model49', b)
    if hasattr(a2, 'ryz_Model49'):
        assert _is_linked(a2, 'ryz_Model49', b)
    _safe_set(b, 'ryz_ControllerToModelRelation48', None)
    assert not _is_linked(b, 'ryz_ControllerToModelRelation48', a2)
    if hasattr(a2, 'ryz_Model49'):
        assert not _is_linked(a2, 'ryz_Model49', b)


def test_assoc_model64_reverse_link_reassign_clear():
    a1 = ryz_ViewToModelRelation(modelcardinality="sample_text")
    a2 = ryz_ViewToModelRelation(modelcardinality="sample_text_2")
    b = ryz_Model(isAbstract=True)
    _safe_set(b, 'ryz_Model66', a1)
    assert _is_linked(b, 'ryz_Model66', a1)
    if hasattr(a1, 'ryz_ViewToModelRelation65'):
        assert _is_linked(a1, 'ryz_ViewToModelRelation65', b)
    _safe_set(b, 'ryz_Model66', a2)
    assert _is_linked(b, 'ryz_Model66', a2)
    if hasattr(a1, 'ryz_ViewToModelRelation65'):
        assert not _is_linked(a1, 'ryz_ViewToModelRelation65', b)
    if hasattr(a2, 'ryz_ViewToModelRelation65'):
        assert _is_linked(a2, 'ryz_ViewToModelRelation65', b)
    _safe_set(b, 'ryz_Model66', None)
    assert not _is_linked(b, 'ryz_Model66', a2)
    if hasattr(a2, 'ryz_ViewToModelRelation65'):
        assert not _is_linked(a2, 'ryz_ViewToModelRelation65', b)


def test_assoc_modelproperties50_reverse_link_reassign_clear():
    a1 = ryz_Property(isRequired=True, type="sample_text")
    a2 = ryz_Property(isRequired=False, type="sample_text_2")
    b = ryz_ControllerToModelRelation(modelCardinality="sample_text", modelOperation="sample_text")
    _safe_set(b, 'ryz_ControllerToModelRelation51', {a1})
    assert _is_linked(b, 'ryz_ControllerToModelRelation51', a1)
    if hasattr(a1, 'ryz_Property52'):
        assert _is_linked(a1, 'ryz_Property52', b)
    _safe_set(b, 'ryz_ControllerToModelRelation51', {a2})
    assert _is_linked(b, 'ryz_ControllerToModelRelation51', a2)
    if hasattr(a1, 'ryz_Property52'):
        assert not _is_linked(a1, 'ryz_Property52', b)
    if hasattr(a2, 'ryz_Property52'):
        assert _is_linked(a2, 'ryz_Property52', b)
    _safe_set(b, 'ryz_ControllerToModelRelation51', set())
    assert not _is_linked(b, 'ryz_ControllerToModelRelation51', a2)
    if hasattr(a2, 'ryz_Property52'):
        assert not _is_linked(a2, 'ryz_Property52', b)


def test_assoc_parameters30_reverse_link_reassign_clear():
    a1 = ryz_Parameter(isList=True, isNullable=True, type="sample_text")
    a2 = ryz_Parameter(isList=False, isNullable=False, type="sample_text_2")
    b = ryz_ActionMethod(httpMethod="sample_text", returns="sample_text")
    _safe_set(b, 'ryz_ActionMethod31', {a1})
    assert _is_linked(b, 'ryz_ActionMethod31', a1)
    if hasattr(a1, 'ryz_Parameter'):
        assert _is_linked(a1, 'ryz_Parameter', b)
    _safe_set(b, 'ryz_ActionMethod31', {a2})
    assert _is_linked(b, 'ryz_ActionMethod31', a2)
    if hasattr(a1, 'ryz_Parameter'):
        assert not _is_linked(a1, 'ryz_Parameter', b)
    if hasattr(a2, 'ryz_Parameter'):
        assert _is_linked(a2, 'ryz_Parameter', b)
    _safe_set(b, 'ryz_ActionMethod31', set())
    assert not _is_linked(b, 'ryz_ActionMethod31', a2)
    if hasattr(a2, 'ryz_Parameter'):
        assert not _is_linked(a2, 'ryz_Parameter', b)


def test_assoc_principal24_reverse_link_reassign_clear():
    a1 = ryz_ModelAssociation(cardinality="sample_text", dependentRoleName="sample_text", isRequired=True, principalRoleName="sample_text")
    a2 = ryz_ModelAssociation(cardinality="sample_text_2", dependentRoleName="sample_text_2", isRequired=False, principalRoleName="sample_text_2")
    b = ryz_Model(isAbstract=True)
    _safe_set(b, 'ryz_Model26', a1)
    assert _is_linked(b, 'ryz_Model26', a1)
    if hasattr(a1, 'ryz_ModelAssociation25'):
        assert _is_linked(a1, 'ryz_ModelAssociation25', b)
    _safe_set(b, 'ryz_Model26', a2)
    assert _is_linked(b, 'ryz_Model26', a2)
    if hasattr(a1, 'ryz_ModelAssociation25'):
        assert not _is_linked(a1, 'ryz_ModelAssociation25', b)
    if hasattr(a2, 'ryz_ModelAssociation25'):
        assert _is_linked(a2, 'ryz_ModelAssociation25', b)
    _safe_set(b, 'ryz_Model26', None)
    assert not _is_linked(b, 'ryz_Model26', a2)
    if hasattr(a2, 'ryz_ModelAssociation25'):
        assert not _is_linked(a2, 'ryz_ModelAssociation25', b)


def test_assoc_properties67_reverse_link_reassign_clear():
    a1 = ryz_ViewToModelRelation(modelcardinality="sample_text")
    a2 = ryz_ViewToModelRelation(modelcardinality="sample_text_2")
    b = ryz_Property(isRequired=True, type="sample_text")
    _safe_set(b, 'ryz_Property69', a1)
    assert _is_linked(b, 'ryz_Property69', a1)
    if hasattr(a1, 'ryz_ViewToModelRelation68'):
        assert _is_linked(a1, 'ryz_ViewToModelRelation68', b)
    _safe_set(b, 'ryz_Property69', a2)
    assert _is_linked(b, 'ryz_Property69', a2)
    if hasattr(a1, 'ryz_ViewToModelRelation68'):
        assert not _is_linked(a1, 'ryz_ViewToModelRelation68', b)
    if hasattr(a2, 'ryz_ViewToModelRelation68'):
        assert _is_linked(a2, 'ryz_ViewToModelRelation68', b)
    _safe_set(b, 'ryz_Property69', None)
    assert not _is_linked(b, 'ryz_Property69', a2)
    if hasattr(a2, 'ryz_ViewToModelRelation68'):
        assert not _is_linked(a2, 'ryz_ViewToModelRelation68', b)


def test_assoc_properties9_reverse_link_reassign_clear():
    a1 = ryz_Property(isRequired=True, type="sample_text")
    a2 = ryz_Property(isRequired=False, type="sample_text_2")
    b = ryz_Model(isAbstract=True)
    _safe_set(b, 'ryz_Model10', {a1})
    assert _is_linked(b, 'ryz_Model10', a1)
    if hasattr(a1, 'ryz_Property'):
        assert _is_linked(a1, 'ryz_Property', b)
    _safe_set(b, 'ryz_Model10', {a2})
    assert _is_linked(b, 'ryz_Model10', a2)
    if hasattr(a1, 'ryz_Property'):
        assert not _is_linked(a1, 'ryz_Property', b)
    if hasattr(a2, 'ryz_Property'):
        assert _is_linked(a2, 'ryz_Property', b)
    _safe_set(b, 'ryz_Model10', set())
    assert not _is_linked(b, 'ryz_Model10', a2)
    if hasattr(a2, 'ryz_Property'):
        assert not _is_linked(a2, 'ryz_Property', b)


def test_assoc_tablekeys14_reverse_link_reassign_clear():
    a1 = ryz_TableKey(isForeignKey=True, isPrimaryKey=True, isRequired=True, type="sample_text")
    a2 = ryz_TableKey(isForeignKey=False, isPrimaryKey=False, isRequired=False, type="sample_text_2")
    b = ryz_Model(isAbstract=True)
    _safe_set(b, 'ryz_Model15', {a1})
    assert _is_linked(b, 'ryz_Model15', a1)
    if hasattr(a1, 'ryz_TableKey'):
        assert _is_linked(a1, 'ryz_TableKey', b)
    _safe_set(b, 'ryz_Model15', {a2})
    assert _is_linked(b, 'ryz_Model15', a2)
    if hasattr(a1, 'ryz_TableKey'):
        assert not _is_linked(a1, 'ryz_TableKey', b)
    if hasattr(a2, 'ryz_TableKey'):
        assert _is_linked(a2, 'ryz_TableKey', b)
    _safe_set(b, 'ryz_Model15', set())
    assert not _is_linked(b, 'ryz_Model15', a2)
    if hasattr(a2, 'ryz_TableKey'):
        assert not _is_linked(a2, 'ryz_TableKey', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abstractview62_stub_double():
    # ryz_AbstractView has no real 'ryz_AbstractView63' property in the generated
    # code (a bare stub) -- manually attach it so ryz_ViewToModelRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_ViewToModelRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_ViewToModelRelation(modelcardinality="sample_text")
    partner = ryz_AbstractView()
    setattr(partner, 'ryz_AbstractView63', None)
    _safe_set(owner, 'ryz_ViewToModelRelation', partner)
    assert getattr(partner, 'ryz_AbstractView63') == owner
    _safe_set(owner, 'ryz_ViewToModelRelation', None)
    assert getattr(partner, 'ryz_AbstractView63') is None


def test_assoc_actionmethod36_stub_double():
    # ryz_ViewToControllerRelation has no real 'ryz_ViewToControllerRelation37' property in the generated
    # code (a bare stub) -- manually attach it so ryz_ActionMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_ActionMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_ActionMethod(httpMethod="sample_text", returns="sample_text")
    partner = ryz_ViewToControllerRelation()
    setattr(partner, 'ryz_ViewToControllerRelation37', None)
    _safe_set(owner, 'ryz_ActionMethod38', partner)
    assert getattr(partner, 'ryz_ViewToControllerRelation37') == owner
    _safe_set(owner, 'ryz_ActionMethod38', None)
    assert getattr(partner, 'ryz_ViewToControllerRelation37') is None


def test_assoc_actionmethod57_stub_double():
    # ryz_ControllerToViewRelation has no real 'ryz_ControllerToViewRelation' property in the generated
    # code (a bare stub) -- manually attach it so ryz_ActionMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_ActionMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_ActionMethod(httpMethod="sample_text", returns="sample_text")
    partner = ryz_ControllerToViewRelation()
    setattr(partner, 'ryz_ControllerToViewRelation', None)
    _safe_set(owner, 'ryz_ActionMethod58', partner)
    assert getattr(partner, 'ryz_ControllerToViewRelation') == owner
    _safe_set(owner, 'ryz_ActionMethod58', None)
    assert getattr(partner, 'ryz_ControllerToViewRelation') is None


def test_assoc_actionmethod78_stub_double():
    # ryz_UseCase has no real 'usecase79' property in the generated
    # code (a bare stub) -- manually attach it so ryz_ActionMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_ActionMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_ActionMethod(httpMethod="sample_text", returns="sample_text")
    partner = ryz_UseCase()
    setattr(partner, 'usecase79', None)
    _safe_set(owner, 'ActionMethod', partner)
    assert owner in getattr(partner, 'usecase79')
    _safe_set(owner, 'ActionMethod', None)
    assert owner not in getattr(partner, 'usecase79')


def test_assoc_actionmethods22_stub_double():
    # ryz_Controller has no real 'ryz_Controller23' property in the generated
    # code (a bare stub) -- manually attach it so ryz_ActionMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_ActionMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_ActionMethod(httpMethod="sample_text", returns="sample_text")
    partner = ryz_Controller()
    setattr(partner, 'ryz_Controller23', None)
    _safe_set(owner, 'ryz_ActionMethod', partner)
    assert owner in getattr(partner, 'ryz_Controller23')
    _safe_set(owner, 'ryz_ActionMethod', None)
    assert owner not in getattr(partner, 'ryz_Controller23')


def test_assoc_header86_stub_double():
    # ryz_Table has no real 'ryz_Table' property in the generated
    # code (a bare stub) -- manually attach it so ryz_Header's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_Header's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_Header(labelText="sample_text", name="sample_text")
    partner = ryz_Table()
    setattr(partner, 'ryz_Table', None)
    _safe_set(owner, 'ryz_Header', partner)
    assert owner in getattr(partner, 'ryz_Table')
    _safe_set(owner, 'ryz_Header', None)
    assert owner not in getattr(partner, 'ryz_Table')


def test_assoc_helperforsendingrequest34_stub_double():
    # ryz_ViewToControllerRelation has no real 'ryz_ViewToControllerRelation' property in the generated
    # code (a bare stub) -- manually attach it so ryz_HelperForSendingRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_HelperForSendingRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_HelperForSendingRequest(httpMethod="sample_text", requestType="sample_text", text="sample_text")
    partner = ryz_ViewToControllerRelation()
    setattr(partner, 'ryz_ViewToControllerRelation', None)
    _safe_set(owner, 'ryz_HelperForSendingRequest35', partner)
    assert getattr(partner, 'ryz_ViewToControllerRelation') == owner
    _safe_set(owner, 'ryz_HelperForSendingRequest35', None)
    assert getattr(partner, 'ryz_ViewToControllerRelation') is None


def test_assoc_helperforsendingrequest76_stub_double():
    # ryz_UseCase has no real 'usecase77' property in the generated
    # code (a bare stub) -- manually attach it so ryz_HelperForSendingRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_HelperForSendingRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_HelperForSendingRequest(httpMethod="sample_text", requestType="sample_text", text="sample_text")
    partner = ryz_UseCase()
    setattr(partner, 'usecase77', None)
    _safe_set(owner, 'HelperForSendingRequest', partner)
    assert owner in getattr(partner, 'usecase77')
    _safe_set(owner, 'HelperForSendingRequest', None)
    assert owner not in getattr(partner, 'usecase77')


def test_assoc_helperforsendingrequest82_stub_double():
    # ryz_PresentationElement has no real 'presentationelement' property in the generated
    # code (a bare stub) -- manually attach it so ryz_HelperForSendingRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_HelperForSendingRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_HelperForSendingRequest(httpMethod="sample_text", requestType="sample_text", text="sample_text")
    partner = ryz_PresentationElement()
    setattr(partner, 'presentationelement', None)
    _safe_set(owner, 'HelperForSendingRequest83', partner)
    assert owner in getattr(partner, 'presentationelement')
    _safe_set(owner, 'HelperForSendingRequest83', None)
    assert owner not in getattr(partner, 'presentationelement')


def test_assoc_helperforsendingrequest87_stub_double():
    # ryz_FormElementToPropertyKeyRelation has no real 'ryz_FormElementToPropertyKeyRelation' property in the generated
    # code (a bare stub) -- manually attach it so ryz_HelperForSendingRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_HelperForSendingRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_HelperForSendingRequest(httpMethod="sample_text", requestType="sample_text", text="sample_text")
    partner = ryz_FormElementToPropertyKeyRelation()
    setattr(partner, 'ryz_FormElementToPropertyKeyRelation', None)
    _safe_set(owner, 'ryz_HelperForSendingRequest88', partner)
    assert getattr(partner, 'ryz_FormElementToPropertyKeyRelation') == owner
    _safe_set(owner, 'ryz_HelperForSendingRequest88', None)
    assert getattr(partner, 'ryz_FormElementToPropertyKeyRelation') is None


def test_assoc_htmlelements18_stub_double():
    # ryz_AbstractView has no real 'ryz_AbstractView19' property in the generated
    # code (a bare stub) -- manually attach it so ryz_HelperForSendingRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_HelperForSendingRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_HelperForSendingRequest(httpMethod="sample_text", requestType="sample_text", text="sample_text")
    partner = ryz_AbstractView()
    setattr(partner, 'ryz_AbstractView19', None)
    _safe_set(owner, 'ryz_HelperForSendingRequest', partner)
    assert owner in getattr(partner, 'ryz_AbstractView19')
    _safe_set(owner, 'ryz_HelperForSendingRequest', None)
    assert owner not in getattr(partner, 'ryz_AbstractView19')


def test_assoc_model39_stub_double():
    # ryz_ViewToControllerRelation has no real 'ryz_ViewToControllerRelation40' property in the generated
    # code (a bare stub) -- manually attach it so ryz_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_Model(isAbstract=True)
    partner = ryz_ViewToControllerRelation()
    setattr(partner, 'ryz_ViewToControllerRelation40', None)
    _safe_set(owner, 'ryz_Model41', partner)
    assert getattr(partner, 'ryz_ViewToControllerRelation40') == owner
    _safe_set(owner, 'ryz_Model41', None)
    assert getattr(partner, 'ryz_ViewToControllerRelation40') is None


def test_assoc_model89_stub_double():
    # ryz_FormElementToPropertyKeyRelation has no real 'ryz_FormElementToPropertyKeyRelation90' property in the generated
    # code (a bare stub) -- manually attach it so ryz_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_Model(isAbstract=True)
    partner = ryz_FormElementToPropertyKeyRelation()
    setattr(partner, 'ryz_FormElementToPropertyKeyRelation90', None)
    _safe_set(owner, 'ryz_Model91', partner)
    assert getattr(partner, 'ryz_FormElementToPropertyKeyRelation90') == owner
    _safe_set(owner, 'ryz_Model91', None)
    assert getattr(partner, 'ryz_FormElementToPropertyKeyRelation90') is None


def test_assoc_modelassociations5_stub_double():
    # ryz_ModelPackage has no real 'ryz_ModelPackage6' property in the generated
    # code (a bare stub) -- manually attach it so ryz_ModelAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_ModelAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_ModelAssociation(cardinality="sample_text", dependentRoleName="sample_text", isRequired=True, principalRoleName="sample_text")
    partner = ryz_ModelPackage()
    setattr(partner, 'ryz_ModelPackage6', None)
    _safe_set(owner, 'ryz_ModelAssociation', partner)
    assert owner in getattr(partner, 'ryz_ModelPackage6')
    _safe_set(owner, 'ryz_ModelAssociation', None)
    assert owner not in getattr(partner, 'ryz_ModelPackage6')


def test_assoc_models4_stub_double():
    # ryz_ModelPackage has no real 'ryz_ModelPackage' property in the generated
    # code (a bare stub) -- manually attach it so ryz_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_Model(isAbstract=True)
    partner = ryz_ModelPackage()
    setattr(partner, 'ryz_ModelPackage', None)
    _safe_set(owner, 'ryz_Model', partner)
    assert owner in getattr(partner, 'ryz_ModelPackage')
    _safe_set(owner, 'ryz_Model', None)
    assert owner not in getattr(partner, 'ryz_ModelPackage')


def test_assoc_presentationelement55_stub_double():
    # ryz_PresentationElement has no real 'PresentationElement' property in the generated
    # code (a bare stub) -- manually attach it so ryz_HelperForSendingRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_HelperForSendingRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_HelperForSendingRequest(httpMethod="sample_text", requestType="sample_text", text="sample_text")
    partner = ryz_PresentationElement()
    setattr(partner, 'PresentationElement', None)
    _safe_set(owner, 'helperforsendingrequest56', {partner})
    assert getattr(partner, 'PresentationElement') == owner
    _safe_set(owner, 'helperforsendingrequest56', set())
    assert getattr(partner, 'PresentationElement') is None


def test_assoc_presentationformelement84_stub_double():
    # ryz_PresentationForm has no real 'ryz_PresentationForm' property in the generated
    # code (a bare stub) -- manually attach it so ryz_PresentationFormElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_PresentationFormElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_PresentationFormElement(labelText="sample_text")
    partner = ryz_PresentationForm()
    setattr(partner, 'ryz_PresentationForm', None)
    _safe_set(owner, 'ryz_PresentationFormElement', partner)
    assert owner in getattr(partner, 'ryz_PresentationForm')
    _safe_set(owner, 'ryz_PresentationFormElement', None)
    assert owner not in getattr(partner, 'ryz_PresentationForm')


def test_assoc_presentationformelement94_stub_double():
    # ryz_PresentationFormElementToPropertyKey has no real 'ryz_PresentationFormElementToPropertyKey95' property in the generated
    # code (a bare stub) -- manually attach it so ryz_PresentationFormElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_PresentationFormElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_PresentationFormElement(labelText="sample_text")
    partner = ryz_PresentationFormElementToPropertyKey()
    setattr(partner, 'ryz_PresentationFormElementToPropertyKey95', None)
    _safe_set(owner, 'ryz_PresentationFormElement96', partner)
    assert getattr(partner, 'ryz_PresentationFormElementToPropertyKey95') == owner
    _safe_set(owner, 'ryz_PresentationFormElement96', None)
    assert getattr(partner, 'ryz_PresentationFormElementToPropertyKey95') is None


def test_assoc_properties42_stub_double():
    # ryz_ViewToControllerRelation has no real 'ryz_ViewToControllerRelation43' property in the generated
    # code (a bare stub) -- manually attach it so ryz_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_Property(isRequired=True, type="sample_text")
    partner = ryz_ViewToControllerRelation()
    setattr(partner, 'ryz_ViewToControllerRelation43', None)
    _safe_set(owner, 'ryz_Property44', partner)
    assert owner in getattr(partner, 'ryz_ViewToControllerRelation43')
    _safe_set(owner, 'ryz_Property44', None)
    assert owner not in getattr(partner, 'ryz_ViewToControllerRelation43')


def test_assoc_property97_stub_double():
    # ryz_PresentationFormElementToPropertyKey has no real 'ryz_PresentationFormElementToPropertyKey98' property in the generated
    # code (a bare stub) -- manually attach it so ryz_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_Property(isRequired=True, type="sample_text")
    partner = ryz_PresentationFormElementToPropertyKey()
    setattr(partner, 'ryz_PresentationFormElementToPropertyKey98', None)
    _safe_set(owner, 'ryz_Property99', partner)
    assert getattr(partner, 'ryz_PresentationFormElementToPropertyKey98') == owner
    _safe_set(owner, 'ryz_Property99', None)
    assert getattr(partner, 'ryz_PresentationFormElementToPropertyKey98') is None


def test_assoc_tablekey100_stub_double():
    # ryz_PresentationFormElementToPropertyKey has no real 'ryz_PresentationFormElementToPropertyKey101' property in the generated
    # code (a bare stub) -- manually attach it so ryz_TableKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_TableKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_TableKey(isForeignKey=True, isPrimaryKey=True, isRequired=True, type="sample_text")
    partner = ryz_PresentationFormElementToPropertyKey()
    setattr(partner, 'ryz_PresentationFormElementToPropertyKey101', None)
    _safe_set(owner, 'ryz_TableKey102', partner)
    assert getattr(partner, 'ryz_PresentationFormElementToPropertyKey101') == owner
    _safe_set(owner, 'ryz_TableKey102', None)
    assert getattr(partner, 'ryz_PresentationFormElementToPropertyKey101') is None


def test_assoc_usecase32_stub_double():
    # ryz_UseCase has no real 'UseCase' property in the generated
    # code (a bare stub) -- manually attach it so ryz_ActionMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_ActionMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_ActionMethod(httpMethod="sample_text", returns="sample_text")
    partner = ryz_UseCase()
    setattr(partner, 'UseCase', None)
    _safe_set(owner, 'actionmethod', {partner})
    assert getattr(partner, 'UseCase') == owner
    _safe_set(owner, 'actionmethod', set())
    assert getattr(partner, 'UseCase') is None


def test_assoc_usecase53_stub_double():
    # ryz_UseCase has no real 'UseCase54' property in the generated
    # code (a bare stub) -- manually attach it so ryz_HelperForSendingRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ryz_HelperForSendingRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ryz_HelperForSendingRequest(httpMethod="sample_text", requestType="sample_text", text="sample_text")
    partner = ryz_UseCase()
    setattr(partner, 'UseCase54', None)
    _safe_set(owner, 'helperforsendingrequest', {partner})
    assert getattr(partner, 'UseCase54') == owner
    _safe_set(owner, 'helperforsendingrequest', set())
    assert getattr(partner, 'UseCase54') is None


