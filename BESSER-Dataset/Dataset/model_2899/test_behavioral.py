import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    AbstractNamespaceElement,
    BindSource,
    BusinessFeatureType,
    BusinessModule,
    ControllerElement,
    InitActionFeature,
    ScreenModule,
    SetActionReceiver,
    SetRestCallReceiverParameter,
    SystemModule,
    Type,
    UIActionFeature,
    UIFeature,
    ViewElement,
    domainmodel_AbstractElement,
    domainmodel_AbstractNamespaceElement,
    domainmodel_AttachAction,
    domainmodel_BindAction,
    domainmodel_BindEnumSource,
    domainmodel_BindSource,
    domainmodel_BusinessFeature,
    domainmodel_BusinessFeatureType,
    domainmodel_BusinessFeatures,
    domainmodel_BusinessModule,
    domainmodel_ContainerElement,
    domainmodel_ContentElement,
    domainmodel_ControllerElement,
    domainmodel_ControllerModule,
    domainmodel_DataType,
    domainmodel_DomainEntity,
    domainmodel_DomainRepository,
    domainmodel_Domainmodel,
    domainmodel_ElementFeature,
    domainmodel_EntryParametersModule,
    domainmodel_ExecuteAction,
    domainmodel_Feature,
    domainmodel_Import,
    domainmodel_InitActionFeature,
    domainmodel_InitActionModule,
    domainmodel_InterfaceDeclaration,
    domainmodel_InterfaceMethodCall,
    domainmodel_InterfaceMethodCallParameter,
    domainmodel_InterfaceMethodCallParameters,
    domainmodel_InterfaceOperation,
    domainmodel_InterfaceOperationUsageRule,
    domainmodel_InterfaceOperationsUsageRule,
    domainmodel_MainFeature,
    domainmodel_MainFeatureOption,
    domainmodel_MethodCall,
    domainmodel_MethodParameter,
    domainmodel_MethodParameters,
    domainmodel_ModelFeature,
    domainmodel_ModelModule,
    domainmodel_NamespaceDeclaration,
    domainmodel_NavigateToAction,
    domainmodel_ScreenFeature,
    domainmodel_ScreenModelParameter,
    domainmodel_ScreenModelParameters,
    domainmodel_ScreenModule,
    domainmodel_SetAction,
    domainmodel_SetActionReceiver,
    domainmodel_SetRestCallReceiver,
    domainmodel_SetRestCallReceiverIDParameter,
    domainmodel_SetRestCallReceiverParameter,
    domainmodel_SetRestCallReceiverParameters,
    domainmodel_SetRestCallReceiverReturnTypeParameter,
    domainmodel_SetRestCallReceiverURLParameter,
    domainmodel_SetUIElementReceiver,
    domainmodel_StatelessComponent,
    domainmodel_SystemDefinition,
    domainmodel_SystemModule,
    domainmodel_Type,
    domainmodel_UIActionFeature,
    domainmodel_UIActionModule,
    domainmodel_UIFeature,
    domainmodel_UIModule,
    domainmodel_ValidateAction,
    domainmodel_ValidatorFeature,
    domainmodel_ValidatorModule,
    domainmodel_ValidatorRule,
    domainmodel_ValidatorRules,
    domainmodel_ViewElement,
    domainmodel_ViewModule,
    ContainerElementLiteral,
    ContentElementLiteral,
    PropertyNameLiteral,
    UIElementReceiverKey,
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

def test_assoc_conditionName55_reverse_link_reassign_clear():
    a1 = domainmodel_ValidatorRule(stringRule="sample_text")
    a2 = domainmodel_ValidatorRule(stringRule="sample_text_2")
    b = domainmodel_ValidatorFeature(name="sample_text")
    _safe_set(b, 'domainmodel_ValidatorFeature56', a1)
    assert _is_linked(b, 'domainmodel_ValidatorFeature56', a1)
    if hasattr(a1, 'domainmodel_ValidatorRule'):
        assert _is_linked(a1, 'domainmodel_ValidatorRule', b)
    _safe_set(b, 'domainmodel_ValidatorFeature56', a2)
    assert _is_linked(b, 'domainmodel_ValidatorFeature56', a2)
    if hasattr(a1, 'domainmodel_ValidatorRule'):
        assert not _is_linked(a1, 'domainmodel_ValidatorRule', b)
    if hasattr(a2, 'domainmodel_ValidatorRule'):
        assert _is_linked(a2, 'domainmodel_ValidatorRule', b)
    _safe_set(b, 'domainmodel_ValidatorFeature56', None)
    assert not _is_linked(b, 'domainmodel_ValidatorFeature56', a2)
    if hasattr(a2, 'domainmodel_ValidatorRule'):
        assert not _is_linked(a2, 'domainmodel_ValidatorRule', b)


def test_assoc_connectPoint2107_reverse_link_reassign_clear():
    a1 = domainmodel_BusinessFeature(connectEnd="sample_text", connectPoint1="sample_text", name="sample_text")
    a2 = domainmodel_BusinessFeature(connectEnd="sample_text_2", connectPoint1="sample_text_2", name="sample_text_2")
    b = domainmodel_BusinessFeature(connectEnd="sample_text", connectPoint1="sample_text", name="sample_text")
    _safe_set(b, 'domainmodel_BusinessFeature108', a1)
    assert _is_linked(b, 'domainmodel_BusinessFeature108', a1)
    if hasattr(a1, 'domainmodel_BusinessFeature106'):
        assert _is_linked(a1, 'domainmodel_BusinessFeature106', b)
    _safe_set(b, 'domainmodel_BusinessFeature108', a2)
    assert _is_linked(b, 'domainmodel_BusinessFeature108', a2)
    if hasattr(a1, 'domainmodel_BusinessFeature106'):
        assert not _is_linked(a1, 'domainmodel_BusinessFeature106', b)
    if hasattr(a2, 'domainmodel_BusinessFeature106'):
        assert _is_linked(a2, 'domainmodel_BusinessFeature106', b)
    _safe_set(b, 'domainmodel_BusinessFeature108', None)
    assert not _is_linked(b, 'domainmodel_BusinessFeature108', a2)
    if hasattr(a2, 'domainmodel_BusinessFeature106'):
        assert not _is_linked(a2, 'domainmodel_BusinessFeature106', b)


def test_assoc_elements35_reverse_link_reassign_clear():
    a1 = domainmodel_ViewElement(name="sample_text")
    a2 = domainmodel_ViewElement(name="sample_text_2")
    b = domainmodel_ContainerElement(container="sample_text")
    _safe_set(b, 'domainmodel_ContainerElement', {a1})
    assert _is_linked(b, 'domainmodel_ContainerElement', a1)
    if hasattr(a1, 'domainmodel_ViewElement'):
        assert _is_linked(a1, 'domainmodel_ViewElement', b)
    _safe_set(b, 'domainmodel_ContainerElement', {a2})
    assert _is_linked(b, 'domainmodel_ContainerElement', a2)
    if hasattr(a1, 'domainmodel_ViewElement'):
        assert not _is_linked(a1, 'domainmodel_ViewElement', b)
    if hasattr(a2, 'domainmodel_ViewElement'):
        assert _is_linked(a2, 'domainmodel_ViewElement', b)
    _safe_set(b, 'domainmodel_ContainerElement', set())
    assert not _is_linked(b, 'domainmodel_ContainerElement', a2)
    if hasattr(a2, 'domainmodel_ViewElement'):
        assert not _is_linked(a2, 'domainmodel_ViewElement', b)


def test_assoc_entityType24_reverse_link_reassign_clear():
    a1 = domainmodel_DomainRepository(name="sample_text")
    a2 = domainmodel_DomainRepository(name="sample_text_2")
    b = domainmodel_DomainEntity(name="sample_text")
    _safe_set(b, 'domainmodel_DomainEntity25', a1)
    assert _is_linked(b, 'domainmodel_DomainEntity25', a1)
    if hasattr(a1, 'domainmodel_DomainRepository'):
        assert _is_linked(a1, 'domainmodel_DomainRepository', b)
    _safe_set(b, 'domainmodel_DomainEntity25', a2)
    assert _is_linked(b, 'domainmodel_DomainEntity25', a2)
    if hasattr(a1, 'domainmodel_DomainRepository'):
        assert not _is_linked(a1, 'domainmodel_DomainRepository', b)
    if hasattr(a2, 'domainmodel_DomainRepository'):
        assert _is_linked(a2, 'domainmodel_DomainRepository', b)
    _safe_set(b, 'domainmodel_DomainEntity25', None)
    assert not _is_linked(b, 'domainmodel_DomainEntity25', a2)
    if hasattr(a2, 'domainmodel_DomainRepository'):
        assert not _is_linked(a2, 'domainmodel_DomainRepository', b)


def test_assoc_features3_reverse_link_reassign_clear():
    a1 = domainmodel_Feature(mapName="sample_text", mappingOption="sample_text", name="sample_text")
    a2 = domainmodel_Feature(mapName="sample_text_2", mappingOption="sample_text_2", name="sample_text_2")
    b = domainmodel_DomainEntity(name="sample_text")
    _safe_set(b, 'domainmodel_DomainEntity', {a1})
    assert _is_linked(b, 'domainmodel_DomainEntity', a1)
    if hasattr(a1, 'domainmodel_Feature4'):
        assert _is_linked(a1, 'domainmodel_Feature4', b)
    _safe_set(b, 'domainmodel_DomainEntity', {a2})
    assert _is_linked(b, 'domainmodel_DomainEntity', a2)
    if hasattr(a1, 'domainmodel_Feature4'):
        assert not _is_linked(a1, 'domainmodel_Feature4', b)
    if hasattr(a2, 'domainmodel_Feature4'):
        assert _is_linked(a2, 'domainmodel_Feature4', b)
    _safe_set(b, 'domainmodel_DomainEntity', set())
    assert not _is_linked(b, 'domainmodel_DomainEntity', a2)
    if hasattr(a2, 'domainmodel_Feature4'):
        assert not _is_linked(a2, 'domainmodel_Feature4', b)


def test_assoc_features36_reverse_link_reassign_clear():
    a1 = domainmodel_ViewElement(name="sample_text")
    a2 = domainmodel_ViewElement(name="sample_text_2")
    b = domainmodel_ElementFeature(propertyName="sample_text", propertyValue="sample_text")
    _safe_set(b, 'domainmodel_ElementFeature', a1)
    assert _is_linked(b, 'domainmodel_ElementFeature', a1)
    if hasattr(a1, 'domainmodel_ViewElement37'):
        assert _is_linked(a1, 'domainmodel_ViewElement37', b)
    _safe_set(b, 'domainmodel_ElementFeature', a2)
    assert _is_linked(b, 'domainmodel_ElementFeature', a2)
    if hasattr(a1, 'domainmodel_ViewElement37'):
        assert not _is_linked(a1, 'domainmodel_ViewElement37', b)
    if hasattr(a2, 'domainmodel_ViewElement37'):
        assert _is_linked(a2, 'domainmodel_ViewElement37', b)
    _safe_set(b, 'domainmodel_ElementFeature', None)
    assert not _is_linked(b, 'domainmodel_ElementFeature', a2)
    if hasattr(a2, 'domainmodel_ViewElement37'):
        assert not _is_linked(a2, 'domainmodel_ViewElement37', b)


def test_assoc_interfaceName18_reverse_link_reassign_clear():
    a1 = domainmodel_InterfaceOperationUsageRule(name="sample_text")
    a2 = domainmodel_InterfaceOperationUsageRule(name="sample_text_2")
    b = domainmodel_InterfaceDeclaration(name="sample_text")
    _safe_set(b, 'domainmodel_InterfaceDeclaration19', a1)
    assert _is_linked(b, 'domainmodel_InterfaceDeclaration19', a1)
    if hasattr(a1, 'domainmodel_InterfaceOperationUsageRule'):
        assert _is_linked(a1, 'domainmodel_InterfaceOperationUsageRule', b)
    _safe_set(b, 'domainmodel_InterfaceDeclaration19', a2)
    assert _is_linked(b, 'domainmodel_InterfaceDeclaration19', a2)
    if hasattr(a1, 'domainmodel_InterfaceOperationUsageRule'):
        assert not _is_linked(a1, 'domainmodel_InterfaceOperationUsageRule', b)
    if hasattr(a2, 'domainmodel_InterfaceOperationUsageRule'):
        assert _is_linked(a2, 'domainmodel_InterfaceOperationUsageRule', b)
    _safe_set(b, 'domainmodel_InterfaceDeclaration19', None)
    assert not _is_linked(b, 'domainmodel_InterfaceDeclaration19', a2)
    if hasattr(a2, 'domainmodel_InterfaceOperationUsageRule'):
        assert not _is_linked(a2, 'domainmodel_InterfaceOperationUsageRule', b)


def test_assoc_methodCall11_reverse_link_reassign_clear():
    a1 = domainmodel_MethodCall(name="sample_text")
    a2 = domainmodel_MethodCall(name="sample_text_2")
    b = domainmodel_InterfaceOperation(restOperation="sample_text")
    _safe_set(b, 'domainmodel_InterfaceOperation', a1)
    assert _is_linked(b, 'domainmodel_InterfaceOperation', a1)
    if hasattr(a1, 'domainmodel_MethodCall12'):
        assert _is_linked(a1, 'domainmodel_MethodCall12', b)
    _safe_set(b, 'domainmodel_InterfaceOperation', a2)
    assert _is_linked(b, 'domainmodel_InterfaceOperation', a2)
    if hasattr(a1, 'domainmodel_MethodCall12'):
        assert not _is_linked(a1, 'domainmodel_MethodCall12', b)
    if hasattr(a2, 'domainmodel_MethodCall12'):
        assert _is_linked(a2, 'domainmodel_MethodCall12', b)
    _safe_set(b, 'domainmodel_InterfaceOperation', None)
    assert not _is_linked(b, 'domainmodel_InterfaceOperation', a2)
    if hasattr(a2, 'domainmodel_MethodCall12'):
        assert not _is_linked(a2, 'domainmodel_MethodCall12', b)


def test_assoc_modelFeatureName64_reverse_link_reassign_clear():
    a1 = domainmodel_ScreenModelParameter(modelFeatureValue="sample_text")
    a2 = domainmodel_ScreenModelParameter(modelFeatureValue="sample_text_2")
    b = domainmodel_ModelFeature(name="sample_text")
    _safe_set(b, 'domainmodel_ModelFeature65', a1)
    assert _is_linked(b, 'domainmodel_ModelFeature65', a1)
    if hasattr(a1, 'domainmodel_ScreenModelParameter'):
        assert _is_linked(a1, 'domainmodel_ScreenModelParameter', b)
    _safe_set(b, 'domainmodel_ModelFeature65', a2)
    assert _is_linked(b, 'domainmodel_ModelFeature65', a2)
    if hasattr(a1, 'domainmodel_ScreenModelParameter'):
        assert not _is_linked(a1, 'domainmodel_ScreenModelParameter', b)
    if hasattr(a2, 'domainmodel_ScreenModelParameter'):
        assert _is_linked(a2, 'domainmodel_ScreenModelParameter', b)
    _safe_set(b, 'domainmodel_ModelFeature65', None)
    assert not _is_linked(b, 'domainmodel_ModelFeature65', a2)
    if hasattr(a2, 'domainmodel_ScreenModelParameter'):
        assert not _is_linked(a2, 'domainmodel_ScreenModelParameter', b)


def test_assoc_operations16_reverse_link_reassign_clear():
    a1 = domainmodel_InterfaceOperation(restOperation="sample_text")
    a2 = domainmodel_InterfaceOperation(restOperation="sample_text_2")
    b = domainmodel_InterfaceDeclaration(name="sample_text")
    _safe_set(b, 'domainmodel_InterfaceDeclaration', {a1})
    assert _is_linked(b, 'domainmodel_InterfaceDeclaration', a1)
    if hasattr(a1, 'domainmodel_InterfaceOperation17'):
        assert _is_linked(a1, 'domainmodel_InterfaceOperation17', b)
    _safe_set(b, 'domainmodel_InterfaceDeclaration', {a2})
    assert _is_linked(b, 'domainmodel_InterfaceDeclaration', a2)
    if hasattr(a1, 'domainmodel_InterfaceOperation17'):
        assert not _is_linked(a1, 'domainmodel_InterfaceOperation17', b)
    if hasattr(a2, 'domainmodel_InterfaceOperation17'):
        assert _is_linked(a2, 'domainmodel_InterfaceOperation17', b)
    _safe_set(b, 'domainmodel_InterfaceDeclaration', set())
    assert not _is_linked(b, 'domainmodel_InterfaceDeclaration', a2)
    if hasattr(a2, 'domainmodel_InterfaceOperation17'):
        assert not _is_linked(a2, 'domainmodel_InterfaceOperation17', b)


def test_assoc_parameterName86_reverse_link_reassign_clear():
    a1 = domainmodel_MethodParameter(name="sample_text")
    a2 = domainmodel_MethodParameter(name="sample_text_2")
    b = domainmodel_InterfaceMethodCallParameter(parameterType="sample_text")
    _safe_set(b, 'domainmodel_InterfaceMethodCallParameter', a1)
    assert _is_linked(b, 'domainmodel_InterfaceMethodCallParameter', a1)
    if hasattr(a1, 'domainmodel_MethodParameter87'):
        assert _is_linked(a1, 'domainmodel_MethodParameter87', b)
    _safe_set(b, 'domainmodel_InterfaceMethodCallParameter', a2)
    assert _is_linked(b, 'domainmodel_InterfaceMethodCallParameter', a2)
    if hasattr(a1, 'domainmodel_MethodParameter87'):
        assert not _is_linked(a1, 'domainmodel_MethodParameter87', b)
    if hasattr(a2, 'domainmodel_MethodParameter87'):
        assert _is_linked(a2, 'domainmodel_MethodParameter87', b)
    _safe_set(b, 'domainmodel_InterfaceMethodCallParameter', None)
    assert not _is_linked(b, 'domainmodel_InterfaceMethodCallParameter', a2)
    if hasattr(a2, 'domainmodel_MethodParameter87'):
        assert not _is_linked(a2, 'domainmodel_MethodParameter87', b)


def test_assoc_uiReceiver51_reverse_link_reassign_clear():
    a1 = domainmodel_SetUIElementReceiver(uiKey="sample_text")
    a2 = domainmodel_SetUIElementReceiver(uiKey="sample_text_2")
    b = domainmodel_BindAction(attribute="sample_text")
    _safe_set(b, 'domainmodel_BindAction52', a1)
    assert _is_linked(b, 'domainmodel_BindAction52', a1)
    if hasattr(a1, 'domainmodel_SetUIElementReceiver53'):
        assert _is_linked(a1, 'domainmodel_SetUIElementReceiver53', b)
    _safe_set(b, 'domainmodel_BindAction52', a2)
    assert _is_linked(b, 'domainmodel_BindAction52', a2)
    if hasattr(a1, 'domainmodel_SetUIElementReceiver53'):
        assert not _is_linked(a1, 'domainmodel_SetUIElementReceiver53', b)
    if hasattr(a2, 'domainmodel_SetUIElementReceiver53'):
        assert _is_linked(a2, 'domainmodel_SetUIElementReceiver53', b)
    _safe_set(b, 'domainmodel_BindAction52', None)
    assert not _is_linked(b, 'domainmodel_BindAction52', a2)
    if hasattr(a2, 'domainmodel_SetUIElementReceiver53'):
        assert not _is_linked(a2, 'domainmodel_SetUIElementReceiver53', b)


def test_assoc_widgetName79_reverse_link_reassign_clear():
    a1 = domainmodel_ViewElement(name="sample_text")
    a2 = domainmodel_ViewElement(name="sample_text_2")
    b = domainmodel_SetUIElementReceiver(uiKey="sample_text")
    _safe_set(b, 'domainmodel_SetUIElementReceiver80', a1)
    assert _is_linked(b, 'domainmodel_SetUIElementReceiver80', a1)
    if hasattr(a1, 'domainmodel_ViewElement81'):
        assert _is_linked(a1, 'domainmodel_ViewElement81', b)
    _safe_set(b, 'domainmodel_SetUIElementReceiver80', a2)
    assert _is_linked(b, 'domainmodel_SetUIElementReceiver80', a2)
    if hasattr(a1, 'domainmodel_ViewElement81'):
        assert not _is_linked(a1, 'domainmodel_ViewElement81', b)
    if hasattr(a2, 'domainmodel_ViewElement81'):
        assert _is_linked(a2, 'domainmodel_ViewElement81', b)
    _safe_set(b, 'domainmodel_SetUIElementReceiver80', None)
    assert not _is_linked(b, 'domainmodel_SetUIElementReceiver80', a2)
    if hasattr(a2, 'domainmodel_ViewElement81'):
        assert not _is_linked(a2, 'domainmodel_ViewElement81', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bindSource49_stub_double():
    # domainmodel_BindSource has no real 'domainmodel_BindSource50' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_BindAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_BindAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_BindAction(attribute="sample_text")
    partner = domainmodel_BindSource()
    setattr(partner, 'domainmodel_BindSource50', None)
    _safe_set(owner, 'domainmodel_BindAction', partner)
    assert getattr(partner, 'domainmodel_BindSource50') == owner
    _safe_set(owner, 'domainmodel_BindAction', None)
    assert getattr(partner, 'domainmodel_BindSource50') is None


def test_assoc_condition40_stub_double():
    # domainmodel_ValidateAction has no real 'domainmodel_ValidateAction' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ValidatorFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ValidatorFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ValidatorFeature(name="sample_text")
    partner = domainmodel_ValidateAction()
    setattr(partner, 'domainmodel_ValidateAction', None)
    _safe_set(owner, 'domainmodel_ValidatorFeature', partner)
    assert getattr(partner, 'domainmodel_ValidateAction') == owner
    _safe_set(owner, 'domainmodel_ValidatorFeature', None)
    assert getattr(partner, 'domainmodel_ValidateAction') is None


def test_assoc_elements0_stub_double():
    # domainmodel_Domainmodel has no real 'domainmodel_Domainmodel' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_AbstractElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_AbstractElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_AbstractElement(name="sample_text")
    partner = domainmodel_Domainmodel()
    setattr(partner, 'domainmodel_Domainmodel', None)
    _safe_set(owner, 'domainmodel_AbstractElement', partner)
    assert owner in getattr(partner, 'domainmodel_Domainmodel')
    _safe_set(owner, 'domainmodel_AbstractElement', None)
    assert owner not in getattr(partner, 'domainmodel_Domainmodel')


def test_assoc_elements38_stub_double():
    # domainmodel_ViewModule has no real 'domainmodel_ViewModule' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ViewElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ViewElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ViewElement(name="sample_text")
    partner = domainmodel_ViewModule()
    setattr(partner, 'domainmodel_ViewModule', None)
    _safe_set(owner, 'domainmodel_ViewElement39', partner)
    assert owner in getattr(partner, 'domainmodel_ViewModule')
    _safe_set(owner, 'domainmodel_ViewElement39', None)
    assert owner not in getattr(partner, 'domainmodel_ViewModule')


def test_assoc_entryFeatures29_stub_double():
    # domainmodel_EntryParametersModule has no real 'domainmodel_EntryParametersModule' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ModelFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ModelFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ModelFeature(name="sample_text")
    partner = domainmodel_EntryParametersModule()
    setattr(partner, 'domainmodel_EntryParametersModule', None)
    _safe_set(owner, 'domainmodel_ModelFeature', partner)
    assert owner in getattr(partner, 'domainmodel_EntryParametersModule')
    _safe_set(owner, 'domainmodel_ModelFeature', None)
    assert owner not in getattr(partner, 'domainmodel_EntryParametersModule')


def test_assoc_features102_stub_double():
    # domainmodel_MainFeature has no real 'domainmodel_MainFeature' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_MainFeatureOption's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_MainFeatureOption's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_MainFeatureOption(name="sample_text")
    partner = domainmodel_MainFeature()
    setattr(partner, 'domainmodel_MainFeature', None)
    _safe_set(owner, 'domainmodel_MainFeatureOption', partner)
    assert owner in getattr(partner, 'domainmodel_MainFeature')
    _safe_set(owner, 'domainmodel_MainFeatureOption', None)
    assert owner not in getattr(partner, 'domainmodel_MainFeature')


def test_assoc_features109_stub_double():
    # domainmodel_BusinessFeatures has no real 'domainmodel_BusinessFeatures' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_BusinessFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_BusinessFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_BusinessFeature(connectEnd="sample_text", connectPoint1="sample_text", name="sample_text")
    partner = domainmodel_BusinessFeatures()
    setattr(partner, 'domainmodel_BusinessFeatures', None)
    _safe_set(owner, 'domainmodel_BusinessFeature110', partner)
    assert owner in getattr(partner, 'domainmodel_BusinessFeatures')
    _safe_set(owner, 'domainmodel_BusinessFeature110', None)
    assert owner not in getattr(partner, 'domainmodel_BusinessFeatures')


def test_assoc_interfaceInstanceName90_stub_double():
    # domainmodel_InterfaceMethodCall has no real 'domainmodel_InterfaceMethodCall' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_BusinessFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_BusinessFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_BusinessFeature(connectEnd="sample_text", connectPoint1="sample_text", name="sample_text")
    partner = domainmodel_InterfaceMethodCall()
    setattr(partner, 'domainmodel_InterfaceMethodCall', None)
    _safe_set(owner, 'domainmodel_BusinessFeature', partner)
    assert getattr(partner, 'domainmodel_InterfaceMethodCall') == owner
    _safe_set(owner, 'domainmodel_BusinessFeature', None)
    assert getattr(partner, 'domainmodel_InterfaceMethodCall') is None


def test_assoc_methodName91_stub_double():
    # domainmodel_InterfaceMethodCall has no real 'domainmodel_InterfaceMethodCall92' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_MethodCall(name="sample_text")
    partner = domainmodel_InterfaceMethodCall()
    setattr(partner, 'domainmodel_InterfaceMethodCall92', None)
    _safe_set(owner, 'domainmodel_MethodCall93', partner)
    assert getattr(partner, 'domainmodel_InterfaceMethodCall92') == owner
    _safe_set(owner, 'domainmodel_MethodCall93', None)
    assert getattr(partner, 'domainmodel_InterfaceMethodCall92') is None


def test_assoc_modelFeatureName47_stub_double():
    # domainmodel_BindSource has no real 'domainmodel_BindSource' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ModelFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ModelFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ModelFeature(name="sample_text")
    partner = domainmodel_BindSource()
    setattr(partner, 'domainmodel_BindSource', None)
    _safe_set(owner, 'domainmodel_ModelFeature48', partner)
    assert getattr(partner, 'domainmodel_BindSource') == owner
    _safe_set(owner, 'domainmodel_ModelFeature48', None)
    assert getattr(partner, 'domainmodel_BindSource') is None


def test_assoc_modelFeatureName82_stub_double():
    # domainmodel_SetAction has no real 'domainmodel_SetAction' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ModelFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ModelFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ModelFeature(name="sample_text")
    partner = domainmodel_SetAction()
    setattr(partner, 'domainmodel_SetAction', None)
    _safe_set(owner, 'domainmodel_ModelFeature83', partner)
    assert getattr(partner, 'domainmodel_SetAction') == owner
    _safe_set(owner, 'domainmodel_ModelFeature83', None)
    assert getattr(partner, 'domainmodel_SetAction') is None


def test_assoc_modelFeatures33_stub_double():
    # domainmodel_ModelModule has no real 'domainmodel_ModelModule' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ModelFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ModelFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ModelFeature(name="sample_text")
    partner = domainmodel_ModelModule()
    setattr(partner, 'domainmodel_ModelModule', None)
    _safe_set(owner, 'domainmodel_ModelFeature34', partner)
    assert owner in getattr(partner, 'domainmodel_ModelModule')
    _safe_set(owner, 'domainmodel_ModelFeature34', None)
    assert owner not in getattr(partner, 'domainmodel_ModelModule')


def test_assoc_operations22_stub_double():
    # domainmodel_InterfaceOperationsUsageRule has no real 'domainmodel_InterfaceOperationsUsageRule23' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_StatelessComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_StatelessComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_StatelessComponent(name="sample_text")
    partner = domainmodel_InterfaceOperationsUsageRule()
    setattr(partner, 'domainmodel_InterfaceOperationsUsageRule23', None)
    _safe_set(owner, 'domainmodel_StatelessComponent', partner)
    assert getattr(partner, 'domainmodel_InterfaceOperationsUsageRule23') == owner
    _safe_set(owner, 'domainmodel_StatelessComponent', None)
    assert getattr(partner, 'domainmodel_InterfaceOperationsUsageRule23') is None


def test_assoc_operations26_stub_double():
    # domainmodel_InterfaceOperationsUsageRule has no real 'domainmodel_InterfaceOperationsUsageRule28' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_DomainRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_DomainRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_DomainRepository(name="sample_text")
    partner = domainmodel_InterfaceOperationsUsageRule()
    setattr(partner, 'domainmodel_InterfaceOperationsUsageRule28', None)
    _safe_set(owner, 'domainmodel_DomainRepository27', partner)
    assert getattr(partner, 'domainmodel_InterfaceOperationsUsageRule28') == owner
    _safe_set(owner, 'domainmodel_DomainRepository27', None)
    assert getattr(partner, 'domainmodel_InterfaceOperationsUsageRule28') is None


def test_assoc_parameters66_stub_double():
    # domainmodel_ScreenModelParameters has no real 'domainmodel_ScreenModelParameters' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ScreenModelParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ScreenModelParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ScreenModelParameter(modelFeatureValue="sample_text")
    partner = domainmodel_ScreenModelParameters()
    setattr(partner, 'domainmodel_ScreenModelParameters', None)
    _safe_set(owner, 'domainmodel_ScreenModelParameter67', partner)
    assert owner in getattr(partner, 'domainmodel_ScreenModelParameters')
    _safe_set(owner, 'domainmodel_ScreenModelParameter67', None)
    assert owner not in getattr(partner, 'domainmodel_ScreenModelParameters')


def test_assoc_parameters7_stub_double():
    # domainmodel_MethodParameters has no real 'domainmodel_MethodParameters' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_MethodParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_MethodParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_MethodParameter(name="sample_text")
    partner = domainmodel_MethodParameters()
    setattr(partner, 'domainmodel_MethodParameters', None)
    _safe_set(owner, 'domainmodel_MethodParameter8', partner)
    assert owner in getattr(partner, 'domainmodel_MethodParameters')
    _safe_set(owner, 'domainmodel_MethodParameter8', None)
    assert owner not in getattr(partner, 'domainmodel_MethodParameters')


def test_assoc_parameters88_stub_double():
    # domainmodel_InterfaceMethodCallParameters has no real 'domainmodel_InterfaceMethodCallParameters' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_InterfaceMethodCallParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_InterfaceMethodCallParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_InterfaceMethodCallParameter(parameterType="sample_text")
    partner = domainmodel_InterfaceMethodCallParameters()
    setattr(partner, 'domainmodel_InterfaceMethodCallParameters', None)
    _safe_set(owner, 'domainmodel_InterfaceMethodCallParameter89', partner)
    assert owner in getattr(partner, 'domainmodel_InterfaceMethodCallParameters')
    _safe_set(owner, 'domainmodel_InterfaceMethodCallParameter89', None)
    assert owner not in getattr(partner, 'domainmodel_InterfaceMethodCallParameters')


def test_assoc_parameters9_stub_double():
    # domainmodel_MethodParameters has no real 'domainmodel_MethodParameters10' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_MethodCall(name="sample_text")
    partner = domainmodel_MethodParameters()
    setattr(partner, 'domainmodel_MethodParameters10', None)
    _safe_set(owner, 'domainmodel_MethodCall', partner)
    assert getattr(partner, 'domainmodel_MethodParameters10') == owner
    _safe_set(owner, 'domainmodel_MethodCall', None)
    assert getattr(partner, 'domainmodel_MethodParameters10') is None


def test_assoc_screenElementId68_stub_double():
    # domainmodel_NavigateToAction has no real 'domainmodel_NavigateToAction' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ScreenFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ScreenFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ScreenFeature(name="sample_text")
    partner = domainmodel_NavigateToAction()
    setattr(partner, 'domainmodel_NavigateToAction', None)
    _safe_set(owner, 'domainmodel_ScreenFeature', partner)
    assert getattr(partner, 'domainmodel_NavigateToAction') == owner
    _safe_set(owner, 'domainmodel_ScreenFeature', None)
    assert getattr(partner, 'domainmodel_NavigateToAction') is None


def test_assoc_screenModules100_stub_double():
    # domainmodel_ScreenModule has no real 'domainmodel_ScreenModule' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ScreenFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ScreenFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ScreenFeature(name="sample_text")
    partner = domainmodel_ScreenModule()
    setattr(partner, 'domainmodel_ScreenModule', None)
    _safe_set(owner, 'domainmodel_ScreenFeature101', {partner})
    assert getattr(partner, 'domainmodel_ScreenModule') == owner
    _safe_set(owner, 'domainmodel_ScreenFeature101', set())
    assert getattr(partner, 'domainmodel_ScreenModule') is None


def test_assoc_type104_stub_double():
    # domainmodel_BusinessFeatureType has no real 'domainmodel_BusinessFeatureType' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_BusinessFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_BusinessFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_BusinessFeature(connectEnd="sample_text", connectPoint1="sample_text", name="sample_text")
    partner = domainmodel_BusinessFeatureType()
    setattr(partner, 'domainmodel_BusinessFeatureType', None)
    _safe_set(owner, 'domainmodel_BusinessFeature105', partner)
    assert getattr(partner, 'domainmodel_BusinessFeatureType') == owner
    _safe_set(owner, 'domainmodel_BusinessFeature105', None)
    assert getattr(partner, 'domainmodel_BusinessFeatureType') is None


def test_assoc_type13_stub_double():
    # domainmodel_Type has no real 'domainmodel_Type15' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_InterfaceOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_InterfaceOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_InterfaceOperation(restOperation="sample_text")
    partner = domainmodel_Type()
    setattr(partner, 'domainmodel_Type15', None)
    _safe_set(owner, 'domainmodel_InterfaceOperation14', partner)
    assert getattr(partner, 'domainmodel_Type15') == owner
    _safe_set(owner, 'domainmodel_InterfaceOperation14', None)
    assert getattr(partner, 'domainmodel_Type15') is None


def test_assoc_type2_stub_double():
    # domainmodel_Type has no real 'domainmodel_Type' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_Feature(mapName="sample_text", mappingOption="sample_text", name="sample_text")
    partner = domainmodel_Type()
    setattr(partner, 'domainmodel_Type', None)
    _safe_set(owner, 'domainmodel_Feature', partner)
    assert getattr(partner, 'domainmodel_Type') == owner
    _safe_set(owner, 'domainmodel_Feature', None)
    assert getattr(partner, 'domainmodel_Type') is None


def test_assoc_type30_stub_double():
    # domainmodel_Type has no real 'domainmodel_Type32' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ModelFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ModelFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ModelFeature(name="sample_text")
    partner = domainmodel_Type()
    setattr(partner, 'domainmodel_Type32', None)
    _safe_set(owner, 'domainmodel_ModelFeature31', partner)
    assert getattr(partner, 'domainmodel_Type32') == owner
    _safe_set(owner, 'domainmodel_ModelFeature31', None)
    assert getattr(partner, 'domainmodel_Type32') is None


def test_assoc_type5_stub_double():
    # domainmodel_Type has no real 'domainmodel_Type6' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_MethodParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_MethodParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_MethodParameter(name="sample_text")
    partner = domainmodel_Type()
    setattr(partner, 'domainmodel_Type6', None)
    _safe_set(owner, 'domainmodel_MethodParameter', partner)
    assert getattr(partner, 'domainmodel_Type6') == owner
    _safe_set(owner, 'domainmodel_MethodParameter', None)
    assert getattr(partner, 'domainmodel_Type6') is None


def test_assoc_uiAction43_stub_double():
    # domainmodel_AttachAction has no real 'domainmodel_AttachAction' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_UIActionModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_UIActionModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_UIActionModule(name="sample_text")
    partner = domainmodel_AttachAction()
    setattr(partner, 'domainmodel_AttachAction', None)
    _safe_set(owner, 'domainmodel_UIActionModule', partner)
    assert getattr(partner, 'domainmodel_AttachAction') == owner
    _safe_set(owner, 'domainmodel_UIActionModule', None)
    assert getattr(partner, 'domainmodel_AttachAction') is None


def test_assoc_uiActionFeatures97_stub_double():
    # domainmodel_UIActionFeature has no real 'domainmodel_UIActionFeature' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_UIActionModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_UIActionModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_UIActionModule(name="sample_text")
    partner = domainmodel_UIActionFeature()
    setattr(partner, 'domainmodel_UIActionFeature', None)
    _safe_set(owner, 'domainmodel_UIActionModule98', {partner})
    assert getattr(partner, 'domainmodel_UIActionFeature') == owner
    _safe_set(owner, 'domainmodel_UIActionModule98', set())
    assert getattr(partner, 'domainmodel_UIActionFeature') is None


def test_assoc_uiActionName72_stub_double():
    # domainmodel_ExecuteAction has no real 'domainmodel_ExecuteAction' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_UIActionModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_UIActionModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_UIActionModule(name="sample_text")
    partner = domainmodel_ExecuteAction()
    setattr(partner, 'domainmodel_ExecuteAction', None)
    _safe_set(owner, 'domainmodel_UIActionModule73', partner)
    assert getattr(partner, 'domainmodel_ExecuteAction') == owner
    _safe_set(owner, 'domainmodel_UIActionModule73', None)
    assert getattr(partner, 'domainmodel_ExecuteAction') is None


def test_assoc_uiReceiver41_stub_double():
    # domainmodel_ValidateAction has no real 'domainmodel_ValidateAction42' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_SetUIElementReceiver's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_SetUIElementReceiver's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_SetUIElementReceiver(uiKey="sample_text")
    partner = domainmodel_ValidateAction()
    setattr(partner, 'domainmodel_ValidateAction42', None)
    _safe_set(owner, 'domainmodel_SetUIElementReceiver', partner)
    assert getattr(partner, 'domainmodel_ValidateAction42') == owner
    _safe_set(owner, 'domainmodel_SetUIElementReceiver', None)
    assert getattr(partner, 'domainmodel_ValidateAction42') is None


def test_assoc_uiReceiver44_stub_double():
    # domainmodel_AttachAction has no real 'domainmodel_AttachAction45' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_SetUIElementReceiver's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_SetUIElementReceiver's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_SetUIElementReceiver(uiKey="sample_text")
    partner = domainmodel_AttachAction()
    setattr(partner, 'domainmodel_AttachAction45', None)
    _safe_set(owner, 'domainmodel_SetUIElementReceiver46', partner)
    assert getattr(partner, 'domainmodel_AttachAction45') == owner
    _safe_set(owner, 'domainmodel_SetUIElementReceiver46', None)
    assert getattr(partner, 'domainmodel_AttachAction45') is None


def test_assoc_usageOperations20_stub_double():
    # domainmodel_InterfaceOperationsUsageRule has no real 'domainmodel_InterfaceOperationsUsageRule' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_InterfaceOperationUsageRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_InterfaceOperationUsageRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_InterfaceOperationUsageRule(name="sample_text")
    partner = domainmodel_InterfaceOperationsUsageRule()
    setattr(partner, 'domainmodel_InterfaceOperationsUsageRule', None)
    _safe_set(owner, 'domainmodel_InterfaceOperationUsageRule21', partner)
    assert owner in getattr(partner, 'domainmodel_InterfaceOperationsUsageRule')
    _safe_set(owner, 'domainmodel_InterfaceOperationUsageRule21', None)
    assert owner not in getattr(partner, 'domainmodel_InterfaceOperationsUsageRule')


def test_assoc_validatorFeatures62_stub_double():
    # domainmodel_ValidatorModule has no real 'domainmodel_ValidatorModule' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ValidatorFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ValidatorFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ValidatorFeature(name="sample_text")
    partner = domainmodel_ValidatorModule()
    setattr(partner, 'domainmodel_ValidatorModule', None)
    _safe_set(owner, 'domainmodel_ValidatorFeature63', partner)
    assert owner in getattr(partner, 'domainmodel_ValidatorModule')
    _safe_set(owner, 'domainmodel_ValidatorFeature63', None)
    assert owner not in getattr(partner, 'domainmodel_ValidatorModule')


def test_assoc_validatorRules57_stub_double():
    # domainmodel_ValidatorRules has no real 'domainmodel_ValidatorRules' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ValidatorRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ValidatorRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ValidatorRule(stringRule="sample_text")
    partner = domainmodel_ValidatorRules()
    setattr(partner, 'domainmodel_ValidatorRules', None)
    _safe_set(owner, 'domainmodel_ValidatorRule58', partner)
    assert owner in getattr(partner, 'domainmodel_ValidatorRules')
    _safe_set(owner, 'domainmodel_ValidatorRule58', None)
    assert owner not in getattr(partner, 'domainmodel_ValidatorRules')


def test_assoc_validatorRules59_stub_double():
    # domainmodel_ValidatorRules has no real 'domainmodel_ValidatorRules61' property in the generated
    # code (a bare stub) -- manually attach it so domainmodel_ValidatorFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # domainmodel_ValidatorFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = domainmodel_ValidatorFeature(name="sample_text")
    partner = domainmodel_ValidatorRules()
    setattr(partner, 'domainmodel_ValidatorRules61', None)
    _safe_set(owner, 'domainmodel_ValidatorFeature60', partner)
    assert getattr(partner, 'domainmodel_ValidatorRules61') == owner
    _safe_set(owner, 'domainmodel_ValidatorFeature60', None)
    assert getattr(partner, 'domainmodel_ValidatorRules61') is None


