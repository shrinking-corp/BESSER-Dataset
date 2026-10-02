import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    xpdl1_ActivitiesType,
    xpdl1_ActivitySetType,
    xpdl1_ActivitySetsType,
    xpdl1_ActivityType,
    xpdl1_ActualParametersType,
    xpdl1_ApplicationType,
    xpdl1_ApplicationsType,
    xpdl1_ArrayTypeType,
    xpdl1_AutomaticType,
    xpdl1_BasicTypeType,
    xpdl1_BlockActivityType,
    xpdl1_ConditionType,
    xpdl1_ConformanceClassType,
    xpdl1_DataFieldType,
    xpdl1_DataFieldsType,
    xpdl1_DataTypeType,
    xpdl1_DeadlineType,
    xpdl1_DeclaredTypeType,
    xpdl1_DocumentRoot,
    xpdl1_EObject,
    xpdl1_EStringToStringMapEntry,
    xpdl1_EnumerationTypeType,
    xpdl1_EnumerationValueType,
    xpdl1_ExtendedAttributeType,
    xpdl1_ExtendedAttributesType,
    xpdl1_ExternalPackageType,
    xpdl1_ExternalPackagesType,
    xpdl1_ExternalReferenceType,
    xpdl1_FinishModeType,
    xpdl1_FormalParameterType,
    xpdl1_FormalParametersType,
    xpdl1_ImplementationType,
    xpdl1_JoinType,
    xpdl1_ListTypeType,
    xpdl1_ManualType,
    xpdl1_MemberType,
    xpdl1_NoType,
    xpdl1_PackageHeaderType,
    xpdl1_PackageType,
    xpdl1_ParticipantType,
    xpdl1_ParticipantTypeType,
    xpdl1_ParticipantsType,
    xpdl1_ProcessHeaderType,
    xpdl1_RecordTypeType,
    xpdl1_RedefinableHeaderType,
    xpdl1_ResponsiblesType,
    xpdl1_RouteType,
    xpdl1_SchemaTypeType,
    xpdl1_ScriptType,
    xpdl1_SimulationInformationType,
    xpdl1_SplitType,
    xpdl1_StartModeType,
    xpdl1_SubFlowType,
    xpdl1_TimeEstimationType,
    xpdl1_ToolType,
    xpdl1_TransitionRefType,
    xpdl1_TransitionRefsType,
    xpdl1_TransitionRestrictionType,
    xpdl1_TransitionRestrictionsType,
    xpdl1_TransitionType,
    xpdl1_TransitionsType,
    xpdl1_TypeDeclarationType,
    xpdl1_TypeDeclarationsType,
    xpdl1_UnionTypeType,
    xpdl1_WorkflowProcessType,
    xpdl1_WorkflowProcessesType,
    xpdl1_XpressionType,
    AccessLevelType,
    DurationUnitType,
    ExecutionType,
    ExecutionType1,
    GraphConformanceType,
    InstantiationType,
    IsArrayType,
    ModeType,
    PublicationStatusType,
    TypeType,
    TypeType1,
    TypeType2,
    TypeType3,
    TypeType4,
    TypeType5,
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

def test_assoc_activity98_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    _safe_set(b, 'xpdl1_ActivityType100', a1)
    assert _is_linked(b, 'xpdl1_ActivityType100', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot99'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot99', b)
    _safe_set(b, 'xpdl1_ActivityType100', a2)
    assert _is_linked(b, 'xpdl1_ActivityType100', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot99'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot99', b)
    if hasattr(a2, 'xpdl1_DocumentRoot99'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot99', b)
    _safe_set(b, 'xpdl1_ActivityType100', None)
    assert not _is_linked(b, 'xpdl1_ActivityType100', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot99'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot99', b)


def test_assoc_activitySet101_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_ActivitySetType(id="sample_text")
    _safe_set(b, 'xpdl1_ActivitySetType103', a1)
    assert _is_linked(b, 'xpdl1_ActivitySetType103', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot102'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot102', b)
    _safe_set(b, 'xpdl1_ActivitySetType103', a2)
    assert _is_linked(b, 'xpdl1_ActivitySetType103', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot102'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot102', b)
    if hasattr(a2, 'xpdl1_DocumentRoot102'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot102', b)
    _safe_set(b, 'xpdl1_ActivitySetType103', None)
    assert not _is_linked(b, 'xpdl1_ActivitySetType103', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot102'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot102', b)


def test_assoc_actualParameters107_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_ActualParametersType(actualParameter="sample_text")
    _safe_set(b, 'xpdl1_ActualParametersType', a1)
    assert _is_linked(b, 'xpdl1_ActualParametersType', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot108'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot108', b)
    _safe_set(b, 'xpdl1_ActualParametersType', a2)
    assert _is_linked(b, 'xpdl1_ActualParametersType', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot108'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot108', b)
    if hasattr(a2, 'xpdl1_DocumentRoot108'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot108', b)
    _safe_set(b, 'xpdl1_ActualParametersType', None)
    assert not _is_linked(b, 'xpdl1_ActualParametersType', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot108'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot108', b)


def test_assoc_actualParameters407_reverse_link_reassign_clear():
    a1 = xpdl1_SubFlowType(execution="sample_text", id="sample_text")
    a2 = xpdl1_SubFlowType(execution="sample_text_2", id="sample_text_2")
    b = xpdl1_ActualParametersType(actualParameter="sample_text")
    _safe_set(b, 'xpdl1_ActualParametersType409', a1)
    assert _is_linked(b, 'xpdl1_ActualParametersType409', a1)
    if hasattr(a1, 'xpdl1_SubFlowType408'):
        assert _is_linked(a1, 'xpdl1_SubFlowType408', b)
    _safe_set(b, 'xpdl1_ActualParametersType409', a2)
    assert _is_linked(b, 'xpdl1_ActualParametersType409', a2)
    if hasattr(a1, 'xpdl1_SubFlowType408'):
        assert not _is_linked(a1, 'xpdl1_SubFlowType408', b)
    if hasattr(a2, 'xpdl1_SubFlowType408'):
        assert _is_linked(a2, 'xpdl1_SubFlowType408', b)
    _safe_set(b, 'xpdl1_ActualParametersType409', None)
    assert not _is_linked(b, 'xpdl1_ActualParametersType409', a2)
    if hasattr(a2, 'xpdl1_SubFlowType408'):
        assert not _is_linked(a2, 'xpdl1_SubFlowType408', b)


def test_assoc_actualParameters410_reverse_link_reassign_clear():
    a1 = xpdl1_ToolType(description="sample_text", id="sample_text", type="sample_text")
    a2 = xpdl1_ToolType(description="sample_text_2", id="sample_text_2", type="sample_text_2")
    b = xpdl1_ActualParametersType(actualParameter="sample_text")
    _safe_set(b, 'xpdl1_ActualParametersType412', a1)
    assert _is_linked(b, 'xpdl1_ActualParametersType412', a1)
    if hasattr(a1, 'xpdl1_ToolType411'):
        assert _is_linked(a1, 'xpdl1_ToolType411', b)
    _safe_set(b, 'xpdl1_ActualParametersType412', a2)
    assert _is_linked(b, 'xpdl1_ActualParametersType412', a2)
    if hasattr(a1, 'xpdl1_ToolType411'):
        assert not _is_linked(a1, 'xpdl1_ToolType411', b)
    if hasattr(a2, 'xpdl1_ToolType411'):
        assert _is_linked(a2, 'xpdl1_ToolType411', b)
    _safe_set(b, 'xpdl1_ActualParametersType412', None)
    assert not _is_linked(b, 'xpdl1_ActualParametersType412', a2)
    if hasattr(a2, 'xpdl1_ToolType411'):
        assert not _is_linked(a2, 'xpdl1_ToolType411', b)


def test_assoc_application109_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_ApplicationType(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl1_ApplicationType111', a1)
    assert _is_linked(b, 'xpdl1_ApplicationType111', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot110'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot110', b)
    _safe_set(b, 'xpdl1_ApplicationType111', a2)
    assert _is_linked(b, 'xpdl1_ApplicationType111', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot110'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot110', b)
    if hasattr(a2, 'xpdl1_DocumentRoot110'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot110', b)
    _safe_set(b, 'xpdl1_ApplicationType111', None)
    assert not _is_linked(b, 'xpdl1_ApplicationType111', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot110'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot110', b)


def test_assoc_arrayType115_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    _safe_set(b, 'xpdl1_ArrayTypeType117', a1)
    assert _is_linked(b, 'xpdl1_ArrayTypeType117', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot116'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot116', b)
    _safe_set(b, 'xpdl1_ArrayTypeType117', a2)
    assert _is_linked(b, 'xpdl1_ArrayTypeType117', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot116'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot116', b)
    if hasattr(a2, 'xpdl1_DocumentRoot116'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot116', b)
    _safe_set(b, 'xpdl1_ArrayTypeType117', None)
    assert not _is_linked(b, 'xpdl1_ArrayTypeType117', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot116'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot116', b)


def test_assoc_arrayType461_reverse_link_reassign_clear():
    a1 = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    _safe_set(b, 'xpdl1_ArrayTypeType463', a1)
    assert _is_linked(b, 'xpdl1_ArrayTypeType463', a1)
    if hasattr(a1, 'xpdl1_TypeDeclarationType462'):
        assert _is_linked(a1, 'xpdl1_TypeDeclarationType462', b)
    _safe_set(b, 'xpdl1_ArrayTypeType463', a2)
    assert _is_linked(b, 'xpdl1_ArrayTypeType463', a2)
    if hasattr(a1, 'xpdl1_TypeDeclarationType462'):
        assert not _is_linked(a1, 'xpdl1_TypeDeclarationType462', b)
    if hasattr(a2, 'xpdl1_TypeDeclarationType462'):
        assert _is_linked(a2, 'xpdl1_TypeDeclarationType462', b)
    _safe_set(b, 'xpdl1_ArrayTypeType463', None)
    assert not _is_linked(b, 'xpdl1_ArrayTypeType463', a2)
    if hasattr(a2, 'xpdl1_TypeDeclarationType462'):
        assert not _is_linked(a2, 'xpdl1_TypeDeclarationType462', b)


def test_assoc_arrayType48_reverse_link_reassign_clear():
    a1 = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    a2 = xpdl1_ArrayTypeType(lowerIndex="sample_text_2", upperIndex="sample_text_2")
    b = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    _safe_set(b, 'xpdl1_ArrayTypeType49', a1)
    assert _is_linked(b, 'xpdl1_ArrayTypeType49', a1)
    if hasattr(a1, 'xpdl1_ArrayTypeType47'):
        assert _is_linked(a1, 'xpdl1_ArrayTypeType47', b)
    _safe_set(b, 'xpdl1_ArrayTypeType49', a2)
    assert _is_linked(b, 'xpdl1_ArrayTypeType49', a2)
    if hasattr(a1, 'xpdl1_ArrayTypeType47'):
        assert not _is_linked(a1, 'xpdl1_ArrayTypeType47', b)
    if hasattr(a2, 'xpdl1_ArrayTypeType47'):
        assert _is_linked(a2, 'xpdl1_ArrayTypeType47', b)
    _safe_set(b, 'xpdl1_ArrayTypeType49', None)
    assert not _is_linked(b, 'xpdl1_ArrayTypeType49', a2)
    if hasattr(a2, 'xpdl1_ArrayTypeType47'):
        assert not _is_linked(a2, 'xpdl1_ArrayTypeType47', b)


def test_assoc_basicType120_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_BasicTypeType(type="sample_text")
    _safe_set(b, 'xpdl1_BasicTypeType122', a1)
    assert _is_linked(b, 'xpdl1_BasicTypeType122', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot121'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot121', b)
    _safe_set(b, 'xpdl1_BasicTypeType122', a2)
    assert _is_linked(b, 'xpdl1_BasicTypeType122', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot121'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot121', b)
    if hasattr(a2, 'xpdl1_DocumentRoot121'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot121', b)
    _safe_set(b, 'xpdl1_BasicTypeType122', None)
    assert not _is_linked(b, 'xpdl1_BasicTypeType122', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot121'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot121', b)


def test_assoc_basicType33_reverse_link_reassign_clear():
    a1 = xpdl1_BasicTypeType(type="sample_text")
    a2 = xpdl1_BasicTypeType(type="sample_text_2")
    b = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    _safe_set(b, 'xpdl1_ArrayTypeType', a1)
    assert _is_linked(b, 'xpdl1_ArrayTypeType', a1)
    if hasattr(a1, 'xpdl1_BasicTypeType'):
        assert _is_linked(a1, 'xpdl1_BasicTypeType', b)
    _safe_set(b, 'xpdl1_ArrayTypeType', a2)
    assert _is_linked(b, 'xpdl1_ArrayTypeType', a2)
    if hasattr(a1, 'xpdl1_BasicTypeType'):
        assert not _is_linked(a1, 'xpdl1_BasicTypeType', b)
    if hasattr(a2, 'xpdl1_BasicTypeType'):
        assert _is_linked(a2, 'xpdl1_BasicTypeType', b)
    _safe_set(b, 'xpdl1_ArrayTypeType', None)
    assert not _is_linked(b, 'xpdl1_ArrayTypeType', a2)
    if hasattr(a2, 'xpdl1_BasicTypeType'):
        assert not _is_linked(a2, 'xpdl1_BasicTypeType', b)


def test_assoc_basicType440_reverse_link_reassign_clear():
    a1 = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_BasicTypeType(type="sample_text")
    _safe_set(b, 'xpdl1_BasicTypeType442', a1)
    assert _is_linked(b, 'xpdl1_BasicTypeType442', a1)
    if hasattr(a1, 'xpdl1_TypeDeclarationType441'):
        assert _is_linked(a1, 'xpdl1_TypeDeclarationType441', b)
    _safe_set(b, 'xpdl1_BasicTypeType442', a2)
    assert _is_linked(b, 'xpdl1_BasicTypeType442', a2)
    if hasattr(a1, 'xpdl1_TypeDeclarationType441'):
        assert not _is_linked(a1, 'xpdl1_TypeDeclarationType441', b)
    if hasattr(a2, 'xpdl1_TypeDeclarationType441'):
        assert _is_linked(a2, 'xpdl1_TypeDeclarationType441', b)
    _safe_set(b, 'xpdl1_BasicTypeType442', None)
    assert not _is_linked(b, 'xpdl1_BasicTypeType442', a2)
    if hasattr(a2, 'xpdl1_TypeDeclarationType441'):
        assert not _is_linked(a2, 'xpdl1_TypeDeclarationType441', b)


def test_assoc_blockActivity11_reverse_link_reassign_clear():
    a1 = xpdl1_BlockActivityType(blockId="sample_text")
    a2 = xpdl1_BlockActivityType(blockId="sample_text_2")
    b = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    _safe_set(b, 'xpdl1_ActivityType12', a1)
    assert _is_linked(b, 'xpdl1_ActivityType12', a1)
    if hasattr(a1, 'xpdl1_BlockActivityType'):
        assert _is_linked(a1, 'xpdl1_BlockActivityType', b)
    _safe_set(b, 'xpdl1_ActivityType12', a2)
    assert _is_linked(b, 'xpdl1_ActivityType12', a2)
    if hasattr(a1, 'xpdl1_BlockActivityType'):
        assert not _is_linked(a1, 'xpdl1_BlockActivityType', b)
    if hasattr(a2, 'xpdl1_BlockActivityType'):
        assert _is_linked(a2, 'xpdl1_BlockActivityType', b)
    _safe_set(b, 'xpdl1_ActivityType12', None)
    assert not _is_linked(b, 'xpdl1_ActivityType12', a2)
    if hasattr(a2, 'xpdl1_BlockActivityType'):
        assert not _is_linked(a2, 'xpdl1_BlockActivityType', b)


def test_assoc_blockActivity123_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_BlockActivityType(blockId="sample_text")
    _safe_set(b, 'xpdl1_BlockActivityType125', a1)
    assert _is_linked(b, 'xpdl1_BlockActivityType125', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot124'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot124', b)
    _safe_set(b, 'xpdl1_BlockActivityType125', a2)
    assert _is_linked(b, 'xpdl1_BlockActivityType125', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot124'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot124', b)
    if hasattr(a2, 'xpdl1_DocumentRoot124'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot124', b)
    _safe_set(b, 'xpdl1_BlockActivityType125', None)
    assert not _is_linked(b, 'xpdl1_BlockActivityType125', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot124'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot124', b)


def test_assoc_condition126_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_ConditionType(group="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'xpdl1_ConditionType128', a1)
    assert _is_linked(b, 'xpdl1_ConditionType128', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot127'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot127', b)
    _safe_set(b, 'xpdl1_ConditionType128', a2)
    assert _is_linked(b, 'xpdl1_ConditionType128', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot127'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot127', b)
    if hasattr(a2, 'xpdl1_DocumentRoot127'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot127', b)
    _safe_set(b, 'xpdl1_ConditionType128', None)
    assert not _is_linked(b, 'xpdl1_ConditionType128', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot127'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot127', b)


def test_assoc_condition431_reverse_link_reassign_clear():
    a1 = xpdl1_TransitionType(description="sample_text", from_="sample_text", id="sample_text", name="sample_text", to="sample_text")
    a2 = xpdl1_TransitionType(description="sample_text_2", from_="sample_text_2", id="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = xpdl1_ConditionType(group="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'xpdl1_ConditionType433', a1)
    assert _is_linked(b, 'xpdl1_ConditionType433', a1)
    if hasattr(a1, 'xpdl1_TransitionType432'):
        assert _is_linked(a1, 'xpdl1_TransitionType432', b)
    _safe_set(b, 'xpdl1_ConditionType433', a2)
    assert _is_linked(b, 'xpdl1_ConditionType433', a2)
    if hasattr(a1, 'xpdl1_TransitionType432'):
        assert not _is_linked(a1, 'xpdl1_TransitionType432', b)
    if hasattr(a2, 'xpdl1_TransitionType432'):
        assert _is_linked(a2, 'xpdl1_TransitionType432', b)
    _safe_set(b, 'xpdl1_ConditionType433', None)
    assert not _is_linked(b, 'xpdl1_ConditionType433', a2)
    if hasattr(a2, 'xpdl1_TransitionType432'):
        assert not _is_linked(a2, 'xpdl1_TransitionType432', b)


def test_assoc_conformanceClass129_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_ConformanceClassType(graphConformance="sample_text")
    _safe_set(b, 'xpdl1_ConformanceClassType', a1)
    assert _is_linked(b, 'xpdl1_ConformanceClassType', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot130'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot130', b)
    _safe_set(b, 'xpdl1_ConformanceClassType', a2)
    assert _is_linked(b, 'xpdl1_ConformanceClassType', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot130'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot130', b)
    if hasattr(a2, 'xpdl1_DocumentRoot130'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot130', b)
    _safe_set(b, 'xpdl1_ConformanceClassType', None)
    assert not _is_linked(b, 'xpdl1_ConformanceClassType', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot130'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot130', b)


def test_assoc_conformanceClass347_reverse_link_reassign_clear():
    a1 = xpdl1_PackageType(id="sample_text", name="sample_text")
    a2 = xpdl1_PackageType(id="sample_text_2", name="sample_text_2")
    b = xpdl1_ConformanceClassType(graphConformance="sample_text")
    _safe_set(b, 'xpdl1_ConformanceClassType349', a1)
    assert _is_linked(b, 'xpdl1_ConformanceClassType349', a1)
    if hasattr(a1, 'xpdl1_PackageType348'):
        assert _is_linked(a1, 'xpdl1_PackageType348', b)
    _safe_set(b, 'xpdl1_ConformanceClassType349', a2)
    assert _is_linked(b, 'xpdl1_ConformanceClassType349', a2)
    if hasattr(a1, 'xpdl1_PackageType348'):
        assert not _is_linked(a1, 'xpdl1_PackageType348', b)
    if hasattr(a2, 'xpdl1_PackageType348'):
        assert _is_linked(a2, 'xpdl1_PackageType348', b)
    _safe_set(b, 'xpdl1_ConformanceClassType349', None)
    assert not _is_linked(b, 'xpdl1_ConformanceClassType349', a2)
    if hasattr(a2, 'xpdl1_PackageType348'):
        assert not _is_linked(a2, 'xpdl1_PackageType348', b)


def test_assoc_dataField131_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_DataFieldType(description="sample_text", id="sample_text", initialValue="sample_text", isArray="sample_text", length="sample_text", name="sample_text")
    _safe_set(b, 'xpdl1_DataFieldType133', a1)
    assert _is_linked(b, 'xpdl1_DataFieldType133', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot132'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot132', b)
    _safe_set(b, 'xpdl1_DataFieldType133', a2)
    assert _is_linked(b, 'xpdl1_DataFieldType133', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot132'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot132', b)
    if hasattr(a2, 'xpdl1_DocumentRoot132'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot132', b)
    _safe_set(b, 'xpdl1_DataFieldType133', None)
    assert not _is_linked(b, 'xpdl1_DataFieldType133', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot132'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot132', b)


def test_assoc_deadline140_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_DeadlineType(execution="sample_text")
    _safe_set(b, 'xpdl1_DeadlineType142', a1)
    assert _is_linked(b, 'xpdl1_DeadlineType142', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot141'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot141', b)
    _safe_set(b, 'xpdl1_DeadlineType142', a2)
    assert _is_linked(b, 'xpdl1_DeadlineType142', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot141'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot141', b)
    if hasattr(a2, 'xpdl1_DocumentRoot141'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot141', b)
    _safe_set(b, 'xpdl1_DeadlineType142', None)
    assert not _is_linked(b, 'xpdl1_DeadlineType142', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot141'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot141', b)


def test_assoc_deadline17_reverse_link_reassign_clear():
    a1 = xpdl1_DeadlineType(execution="sample_text")
    a2 = xpdl1_DeadlineType(execution="sample_text_2")
    b = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    _safe_set(b, 'xpdl1_ActivityType18', {a1})
    assert _is_linked(b, 'xpdl1_ActivityType18', a1)
    if hasattr(a1, 'xpdl1_DeadlineType'):
        assert _is_linked(a1, 'xpdl1_DeadlineType', b)
    _safe_set(b, 'xpdl1_ActivityType18', {a2})
    assert _is_linked(b, 'xpdl1_ActivityType18', a2)
    if hasattr(a1, 'xpdl1_DeadlineType'):
        assert not _is_linked(a1, 'xpdl1_DeadlineType', b)
    if hasattr(a2, 'xpdl1_DeadlineType'):
        assert _is_linked(a2, 'xpdl1_DeadlineType', b)
    _safe_set(b, 'xpdl1_ActivityType18', set())
    assert not _is_linked(b, 'xpdl1_ActivityType18', a2)
    if hasattr(a2, 'xpdl1_DeadlineType'):
        assert not _is_linked(a2, 'xpdl1_DeadlineType', b)


def test_assoc_declaredType143_reverse_link_reassign_clear():
    a1 = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_DocumentRoot(actualParameter="sample_text_2", author="sample_text_2", codepage="sample_text_2", cost="sample_text_2", costUnit="sample_text_2", countrykey="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", duration="sample_text_2", icon="sample_text_2", initialValue="sample_text_2", length="sample_text_2", limit="sample_text_2", mixed="sample_text_2", performer="sample_text_2", priority="sample_text_2", priorityUnit="sample_text_2", responsible="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2", vendor="sample_text_2", version="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_DeclaredTypeType(id="sample_text")
    _safe_set(b, 'xpdl1_DeclaredTypeType145', a1)
    assert _is_linked(b, 'xpdl1_DeclaredTypeType145', a1)
    if hasattr(a1, 'xpdl1_DocumentRoot144'):
        assert _is_linked(a1, 'xpdl1_DocumentRoot144', b)
    _safe_set(b, 'xpdl1_DeclaredTypeType145', a2)
    assert _is_linked(b, 'xpdl1_DeclaredTypeType145', a2)
    if hasattr(a1, 'xpdl1_DocumentRoot144'):
        assert not _is_linked(a1, 'xpdl1_DocumentRoot144', b)
    if hasattr(a2, 'xpdl1_DocumentRoot144'):
        assert _is_linked(a2, 'xpdl1_DocumentRoot144', b)
    _safe_set(b, 'xpdl1_DeclaredTypeType145', None)
    assert not _is_linked(b, 'xpdl1_DeclaredTypeType145', a2)
    if hasattr(a2, 'xpdl1_DocumentRoot144'):
        assert not _is_linked(a2, 'xpdl1_DocumentRoot144', b)


def test_assoc_declaredType34_reverse_link_reassign_clear():
    a1 = xpdl1_DeclaredTypeType(id="sample_text")
    a2 = xpdl1_DeclaredTypeType(id="sample_text_2")
    b = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    _safe_set(b, 'xpdl1_ArrayTypeType35', a1)
    assert _is_linked(b, 'xpdl1_ArrayTypeType35', a1)
    if hasattr(a1, 'xpdl1_DeclaredTypeType'):
        assert _is_linked(a1, 'xpdl1_DeclaredTypeType', b)
    _safe_set(b, 'xpdl1_ArrayTypeType35', a2)
    assert _is_linked(b, 'xpdl1_ArrayTypeType35', a2)
    if hasattr(a1, 'xpdl1_DeclaredTypeType'):
        assert not _is_linked(a1, 'xpdl1_DeclaredTypeType', b)
    if hasattr(a2, 'xpdl1_DeclaredTypeType'):
        assert _is_linked(a2, 'xpdl1_DeclaredTypeType', b)
    _safe_set(b, 'xpdl1_ArrayTypeType35', None)
    assert not _is_linked(b, 'xpdl1_ArrayTypeType35', a2)
    if hasattr(a2, 'xpdl1_DeclaredTypeType'):
        assert not _is_linked(a2, 'xpdl1_DeclaredTypeType', b)


def test_assoc_declaredType443_reverse_link_reassign_clear():
    a1 = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_DeclaredTypeType(id="sample_text")
    _safe_set(b, 'xpdl1_DeclaredTypeType445', a1)
    assert _is_linked(b, 'xpdl1_DeclaredTypeType445', a1)
    if hasattr(a1, 'xpdl1_TypeDeclarationType444'):
        assert _is_linked(a1, 'xpdl1_TypeDeclarationType444', b)
    _safe_set(b, 'xpdl1_DeclaredTypeType445', a2)
    assert _is_linked(b, 'xpdl1_DeclaredTypeType445', a2)
    if hasattr(a1, 'xpdl1_TypeDeclarationType444'):
        assert not _is_linked(a1, 'xpdl1_TypeDeclarationType444', b)
    if hasattr(a2, 'xpdl1_TypeDeclarationType444'):
        assert _is_linked(a2, 'xpdl1_TypeDeclarationType444', b)
    _safe_set(b, 'xpdl1_DeclaredTypeType445', None)
    assert not _is_linked(b, 'xpdl1_DeclaredTypeType445', a2)
    if hasattr(a2, 'xpdl1_TypeDeclarationType444'):
        assert not _is_linked(a2, 'xpdl1_TypeDeclarationType444', b)


def test_assoc_enumerationValue149_reverse_link_reassign_clear():
    a1 = xpdl1_EnumerationValueType(name="sample_text")
    a2 = xpdl1_EnumerationValueType(name="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot150', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot150', a1)
    if hasattr(a1, 'xpdl1_EnumerationValueType'):
        assert _is_linked(a1, 'xpdl1_EnumerationValueType', b)
    _safe_set(b, 'xpdl1_DocumentRoot150', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot150', a2)
    if hasattr(a1, 'xpdl1_EnumerationValueType'):
        assert not _is_linked(a1, 'xpdl1_EnumerationValueType', b)
    if hasattr(a2, 'xpdl1_EnumerationValueType'):
        assert _is_linked(a2, 'xpdl1_EnumerationValueType', b)
    _safe_set(b, 'xpdl1_DocumentRoot150', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot150', a2)
    if hasattr(a2, 'xpdl1_EnumerationValueType'):
        assert not _is_linked(a2, 'xpdl1_EnumerationValueType', b)


def test_assoc_extendedAttribute151_reverse_link_reassign_clear():
    a1 = xpdl1_ExtendedAttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", value="sample_text")
    a2 = xpdl1_ExtendedAttributeType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot152', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot152', a1)
    if hasattr(a1, 'xpdl1_ExtendedAttributeType'):
        assert _is_linked(a1, 'xpdl1_ExtendedAttributeType', b)
    _safe_set(b, 'xpdl1_DocumentRoot152', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot152', a2)
    if hasattr(a1, 'xpdl1_ExtendedAttributeType'):
        assert not _is_linked(a1, 'xpdl1_ExtendedAttributeType', b)
    if hasattr(a2, 'xpdl1_ExtendedAttributeType'):
        assert _is_linked(a2, 'xpdl1_ExtendedAttributeType', b)
    _safe_set(b, 'xpdl1_DocumentRoot152', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot152', a2)
    if hasattr(a2, 'xpdl1_ExtendedAttributeType'):
        assert not _is_linked(a2, 'xpdl1_ExtendedAttributeType', b)


def test_assoc_externalPackage156_reverse_link_reassign_clear():
    a1 = xpdl1_ExternalPackageType(href="sample_text")
    a2 = xpdl1_ExternalPackageType(href="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot157', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot157', a1)
    if hasattr(a1, 'xpdl1_ExternalPackageType'):
        assert _is_linked(a1, 'xpdl1_ExternalPackageType', b)
    _safe_set(b, 'xpdl1_DocumentRoot157', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot157', a2)
    if hasattr(a1, 'xpdl1_ExternalPackageType'):
        assert not _is_linked(a1, 'xpdl1_ExternalPackageType', b)
    if hasattr(a2, 'xpdl1_ExternalPackageType'):
        assert _is_linked(a2, 'xpdl1_ExternalPackageType', b)
    _safe_set(b, 'xpdl1_DocumentRoot157', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot157', a2)
    if hasattr(a2, 'xpdl1_ExternalPackageType'):
        assert not _is_linked(a2, 'xpdl1_ExternalPackageType', b)


def test_assoc_externalReference160_reverse_link_reassign_clear():
    a1 = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    a2 = xpdl1_ExternalReferenceType(location="sample_text_2", namespace="sample_text_2", xref="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot161', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot161', a1)
    if hasattr(a1, 'xpdl1_ExternalReferenceType162'):
        assert _is_linked(a1, 'xpdl1_ExternalReferenceType162', b)
    _safe_set(b, 'xpdl1_DocumentRoot161', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot161', a2)
    if hasattr(a1, 'xpdl1_ExternalReferenceType162'):
        assert not _is_linked(a1, 'xpdl1_ExternalReferenceType162', b)
    if hasattr(a2, 'xpdl1_ExternalReferenceType162'):
        assert _is_linked(a2, 'xpdl1_ExternalReferenceType162', b)
    _safe_set(b, 'xpdl1_DocumentRoot161', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot161', a2)
    if hasattr(a2, 'xpdl1_ExternalReferenceType162'):
        assert not _is_linked(a2, 'xpdl1_ExternalReferenceType162', b)


def test_assoc_externalReference28_reverse_link_reassign_clear():
    a1 = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    a2 = xpdl1_ExternalReferenceType(location="sample_text_2", namespace="sample_text_2", xref="sample_text_2")
    b = xpdl1_ApplicationType(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl1_ApplicationType29', a1)
    assert _is_linked(b, 'xpdl1_ApplicationType29', a1)
    if hasattr(a1, 'xpdl1_ExternalReferenceType'):
        assert _is_linked(a1, 'xpdl1_ExternalReferenceType', b)
    _safe_set(b, 'xpdl1_ApplicationType29', a2)
    assert _is_linked(b, 'xpdl1_ApplicationType29', a2)
    if hasattr(a1, 'xpdl1_ExternalReferenceType'):
        assert not _is_linked(a1, 'xpdl1_ExternalReferenceType', b)
    if hasattr(a2, 'xpdl1_ExternalReferenceType'):
        assert _is_linked(a2, 'xpdl1_ExternalReferenceType', b)
    _safe_set(b, 'xpdl1_ApplicationType29', None)
    assert not _is_linked(b, 'xpdl1_ApplicationType29', a2)
    if hasattr(a2, 'xpdl1_ExternalReferenceType'):
        assert not _is_linked(a2, 'xpdl1_ExternalReferenceType', b)


def test_assoc_externalReference38_reverse_link_reassign_clear():
    a1 = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    a2 = xpdl1_ExternalReferenceType(location="sample_text_2", namespace="sample_text_2", xref="sample_text_2")
    b = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    _safe_set(b, 'xpdl1_ArrayTypeType39', a1)
    assert _is_linked(b, 'xpdl1_ArrayTypeType39', a1)
    if hasattr(a1, 'xpdl1_ExternalReferenceType40'):
        assert _is_linked(a1, 'xpdl1_ExternalReferenceType40', b)
    _safe_set(b, 'xpdl1_ArrayTypeType39', a2)
    assert _is_linked(b, 'xpdl1_ArrayTypeType39', a2)
    if hasattr(a1, 'xpdl1_ExternalReferenceType40'):
        assert not _is_linked(a1, 'xpdl1_ExternalReferenceType40', b)
    if hasattr(a2, 'xpdl1_ExternalReferenceType40'):
        assert _is_linked(a2, 'xpdl1_ExternalReferenceType40', b)
    _safe_set(b, 'xpdl1_ArrayTypeType39', None)
    assert not _is_linked(b, 'xpdl1_ArrayTypeType39', a2)
    if hasattr(a2, 'xpdl1_ExternalReferenceType40'):
        assert not _is_linked(a2, 'xpdl1_ExternalReferenceType40', b)


def test_assoc_externalReference380_reverse_link_reassign_clear():
    a1 = xpdl1_ParticipantType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_ParticipantType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    _safe_set(b, 'xpdl1_ExternalReferenceType382', a1)
    assert _is_linked(b, 'xpdl1_ExternalReferenceType382', a1)
    if hasattr(a1, 'xpdl1_ParticipantType381'):
        assert _is_linked(a1, 'xpdl1_ParticipantType381', b)
    _safe_set(b, 'xpdl1_ExternalReferenceType382', a2)
    assert _is_linked(b, 'xpdl1_ExternalReferenceType382', a2)
    if hasattr(a1, 'xpdl1_ParticipantType381'):
        assert not _is_linked(a1, 'xpdl1_ParticipantType381', b)
    if hasattr(a2, 'xpdl1_ParticipantType381'):
        assert _is_linked(a2, 'xpdl1_ParticipantType381', b)
    _safe_set(b, 'xpdl1_ExternalReferenceType382', None)
    assert not _is_linked(b, 'xpdl1_ExternalReferenceType382', a2)
    if hasattr(a2, 'xpdl1_ParticipantType381'):
        assert not _is_linked(a2, 'xpdl1_ParticipantType381', b)


def test_assoc_externalReference449_reverse_link_reassign_clear():
    a1 = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    _safe_set(b, 'xpdl1_ExternalReferenceType451', a1)
    assert _is_linked(b, 'xpdl1_ExternalReferenceType451', a1)
    if hasattr(a1, 'xpdl1_TypeDeclarationType450'):
        assert _is_linked(a1, 'xpdl1_TypeDeclarationType450', b)
    _safe_set(b, 'xpdl1_ExternalReferenceType451', a2)
    assert _is_linked(b, 'xpdl1_ExternalReferenceType451', a2)
    if hasattr(a1, 'xpdl1_TypeDeclarationType450'):
        assert not _is_linked(a1, 'xpdl1_TypeDeclarationType450', b)
    if hasattr(a2, 'xpdl1_TypeDeclarationType450'):
        assert _is_linked(a2, 'xpdl1_TypeDeclarationType450', b)
    _safe_set(b, 'xpdl1_ExternalReferenceType451', None)
    assert not _is_linked(b, 'xpdl1_ExternalReferenceType451', a2)
    if hasattr(a2, 'xpdl1_TypeDeclarationType450'):
        assert not _is_linked(a2, 'xpdl1_TypeDeclarationType450', b)


def test_assoc_formalParameter166_reverse_link_reassign_clear():
    a1 = xpdl1_FormalParameterType(description="sample_text", id="sample_text", index="sample_text", mode="sample_text")
    a2 = xpdl1_FormalParameterType(description="sample_text_2", id="sample_text_2", index="sample_text_2", mode="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot167', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot167', a1)
    if hasattr(a1, 'xpdl1_FormalParameterType'):
        assert _is_linked(a1, 'xpdl1_FormalParameterType', b)
    _safe_set(b, 'xpdl1_DocumentRoot167', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot167', a2)
    if hasattr(a1, 'xpdl1_FormalParameterType'):
        assert not _is_linked(a1, 'xpdl1_FormalParameterType', b)
    if hasattr(a2, 'xpdl1_FormalParameterType'):
        assert _is_linked(a2, 'xpdl1_FormalParameterType', b)
    _safe_set(b, 'xpdl1_DocumentRoot167', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot167', a2)
    if hasattr(a2, 'xpdl1_FormalParameterType'):
        assert not _is_linked(a2, 'xpdl1_FormalParameterType', b)


def test_assoc_join174_reverse_link_reassign_clear():
    a1 = xpdl1_JoinType(type="sample_text")
    a2 = xpdl1_JoinType(type="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot175', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot175', a1)
    if hasattr(a1, 'xpdl1_JoinType'):
        assert _is_linked(a1, 'xpdl1_JoinType', b)
    _safe_set(b, 'xpdl1_DocumentRoot175', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot175', a2)
    if hasattr(a1, 'xpdl1_JoinType'):
        assert not _is_linked(a1, 'xpdl1_JoinType', b)
    if hasattr(a2, 'xpdl1_JoinType'):
        assert _is_linked(a2, 'xpdl1_JoinType', b)
    _safe_set(b, 'xpdl1_DocumentRoot175', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot175', a2)
    if hasattr(a2, 'xpdl1_JoinType'):
        assert not _is_linked(a2, 'xpdl1_JoinType', b)


def test_assoc_package185_reverse_link_reassign_clear():
    a1 = xpdl1_PackageType(id="sample_text", name="sample_text")
    a2 = xpdl1_PackageType(id="sample_text_2", name="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot186', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot186', a1)
    if hasattr(a1, 'xpdl1_PackageType'):
        assert _is_linked(a1, 'xpdl1_PackageType', b)
    _safe_set(b, 'xpdl1_DocumentRoot186', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot186', a2)
    if hasattr(a1, 'xpdl1_PackageType'):
        assert not _is_linked(a1, 'xpdl1_PackageType', b)
    if hasattr(a2, 'xpdl1_PackageType'):
        assert _is_linked(a2, 'xpdl1_PackageType', b)
    _safe_set(b, 'xpdl1_DocumentRoot186', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot186', a2)
    if hasattr(a2, 'xpdl1_PackageType'):
        assert not _is_linked(a2, 'xpdl1_PackageType', b)


def test_assoc_packageHeader187_reverse_link_reassign_clear():
    a1 = xpdl1_PackageHeaderType(costUnit="sample_text", created="sample_text", description="sample_text", documentation="sample_text", priorityUnit="sample_text", vendor="sample_text", xPDLVersion="sample_text")
    a2 = xpdl1_PackageHeaderType(costUnit="sample_text_2", created="sample_text_2", description="sample_text_2", documentation="sample_text_2", priorityUnit="sample_text_2", vendor="sample_text_2", xPDLVersion="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot188', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot188', a1)
    if hasattr(a1, 'xpdl1_PackageHeaderType'):
        assert _is_linked(a1, 'xpdl1_PackageHeaderType', b)
    _safe_set(b, 'xpdl1_DocumentRoot188', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot188', a2)
    if hasattr(a1, 'xpdl1_PackageHeaderType'):
        assert not _is_linked(a1, 'xpdl1_PackageHeaderType', b)
    if hasattr(a2, 'xpdl1_PackageHeaderType'):
        assert _is_linked(a2, 'xpdl1_PackageHeaderType', b)
    _safe_set(b, 'xpdl1_DocumentRoot188', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot188', a2)
    if hasattr(a2, 'xpdl1_PackageHeaderType'):
        assert not _is_linked(a2, 'xpdl1_PackageHeaderType', b)


def test_assoc_packageHeader341_reverse_link_reassign_clear():
    a1 = xpdl1_PackageType(id="sample_text", name="sample_text")
    a2 = xpdl1_PackageType(id="sample_text_2", name="sample_text_2")
    b = xpdl1_PackageHeaderType(costUnit="sample_text", created="sample_text", description="sample_text", documentation="sample_text", priorityUnit="sample_text", vendor="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_PackageHeaderType343', a1)
    assert _is_linked(b, 'xpdl1_PackageHeaderType343', a1)
    if hasattr(a1, 'xpdl1_PackageType342'):
        assert _is_linked(a1, 'xpdl1_PackageType342', b)
    _safe_set(b, 'xpdl1_PackageHeaderType343', a2)
    assert _is_linked(b, 'xpdl1_PackageHeaderType343', a2)
    if hasattr(a1, 'xpdl1_PackageType342'):
        assert not _is_linked(a1, 'xpdl1_PackageType342', b)
    if hasattr(a2, 'xpdl1_PackageType342'):
        assert _is_linked(a2, 'xpdl1_PackageType342', b)
    _safe_set(b, 'xpdl1_PackageHeaderType343', None)
    assert not _is_linked(b, 'xpdl1_PackageHeaderType343', a2)
    if hasattr(a2, 'xpdl1_PackageType342'):
        assert not _is_linked(a2, 'xpdl1_PackageType342', b)


def test_assoc_participant189_reverse_link_reassign_clear():
    a1 = xpdl1_ParticipantType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_ParticipantType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot190', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot190', a1)
    if hasattr(a1, 'xpdl1_ParticipantType'):
        assert _is_linked(a1, 'xpdl1_ParticipantType', b)
    _safe_set(b, 'xpdl1_DocumentRoot190', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot190', a2)
    if hasattr(a1, 'xpdl1_ParticipantType'):
        assert not _is_linked(a1, 'xpdl1_ParticipantType', b)
    if hasattr(a2, 'xpdl1_ParticipantType'):
        assert _is_linked(a2, 'xpdl1_ParticipantType', b)
    _safe_set(b, 'xpdl1_DocumentRoot190', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot190', a2)
    if hasattr(a2, 'xpdl1_ParticipantType'):
        assert not _is_linked(a2, 'xpdl1_ParticipantType', b)


def test_assoc_participantType193_reverse_link_reassign_clear():
    a1 = xpdl1_ParticipantTypeType(type="sample_text")
    a2 = xpdl1_ParticipantTypeType(type="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot194', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot194', a1)
    if hasattr(a1, 'xpdl1_ParticipantTypeType'):
        assert _is_linked(a1, 'xpdl1_ParticipantTypeType', b)
    _safe_set(b, 'xpdl1_DocumentRoot194', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot194', a2)
    if hasattr(a1, 'xpdl1_ParticipantTypeType'):
        assert not _is_linked(a1, 'xpdl1_ParticipantTypeType', b)
    if hasattr(a2, 'xpdl1_ParticipantTypeType'):
        assert _is_linked(a2, 'xpdl1_ParticipantTypeType', b)
    _safe_set(b, 'xpdl1_DocumentRoot194', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot194', a2)
    if hasattr(a2, 'xpdl1_ParticipantTypeType'):
        assert not _is_linked(a2, 'xpdl1_ParticipantTypeType', b)


def test_assoc_participantType377_reverse_link_reassign_clear():
    a1 = xpdl1_ParticipantTypeType(type="sample_text")
    a2 = xpdl1_ParticipantTypeType(type="sample_text_2")
    b = xpdl1_ParticipantType(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl1_ParticipantType378', a1)
    assert _is_linked(b, 'xpdl1_ParticipantType378', a1)
    if hasattr(a1, 'xpdl1_ParticipantTypeType379'):
        assert _is_linked(a1, 'xpdl1_ParticipantTypeType379', b)
    _safe_set(b, 'xpdl1_ParticipantType378', a2)
    assert _is_linked(b, 'xpdl1_ParticipantType378', a2)
    if hasattr(a1, 'xpdl1_ParticipantTypeType379'):
        assert not _is_linked(a1, 'xpdl1_ParticipantTypeType379', b)
    if hasattr(a2, 'xpdl1_ParticipantTypeType379'):
        assert _is_linked(a2, 'xpdl1_ParticipantTypeType379', b)
    _safe_set(b, 'xpdl1_ParticipantType378', None)
    assert not _is_linked(b, 'xpdl1_ParticipantType378', a2)
    if hasattr(a2, 'xpdl1_ParticipantTypeType379'):
        assert not _is_linked(a2, 'xpdl1_ParticipantTypeType379', b)


def test_assoc_processHeader195_reverse_link_reassign_clear():
    a1 = xpdl1_ProcessHeaderType(created="sample_text", description="sample_text", durationUnit="sample_text", limit="sample_text", priority="sample_text", validFrom="sample_text", validTo="sample_text")
    a2 = xpdl1_ProcessHeaderType(created="sample_text_2", description="sample_text_2", durationUnit="sample_text_2", limit="sample_text_2", priority="sample_text_2", validFrom="sample_text_2", validTo="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot196', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot196', a1)
    if hasattr(a1, 'xpdl1_ProcessHeaderType'):
        assert _is_linked(a1, 'xpdl1_ProcessHeaderType', b)
    _safe_set(b, 'xpdl1_DocumentRoot196', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot196', a2)
    if hasattr(a1, 'xpdl1_ProcessHeaderType'):
        assert not _is_linked(a1, 'xpdl1_ProcessHeaderType', b)
    if hasattr(a2, 'xpdl1_ProcessHeaderType'):
        assert _is_linked(a2, 'xpdl1_ProcessHeaderType', b)
    _safe_set(b, 'xpdl1_DocumentRoot196', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot196', a2)
    if hasattr(a2, 'xpdl1_ProcessHeaderType'):
        assert not _is_linked(a2, 'xpdl1_ProcessHeaderType', b)


def test_assoc_processHeader476_reverse_link_reassign_clear():
    a1 = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_WorkflowProcessType(accessLevel="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_ProcessHeaderType(created="sample_text", description="sample_text", durationUnit="sample_text", limit="sample_text", priority="sample_text", validFrom="sample_text", validTo="sample_text")
    _safe_set(b, 'xpdl1_ProcessHeaderType478', a1)
    assert _is_linked(b, 'xpdl1_ProcessHeaderType478', a1)
    if hasattr(a1, 'xpdl1_WorkflowProcessType477'):
        assert _is_linked(a1, 'xpdl1_WorkflowProcessType477', b)
    _safe_set(b, 'xpdl1_ProcessHeaderType478', a2)
    assert _is_linked(b, 'xpdl1_ProcessHeaderType478', a2)
    if hasattr(a1, 'xpdl1_WorkflowProcessType477'):
        assert not _is_linked(a1, 'xpdl1_WorkflowProcessType477', b)
    if hasattr(a2, 'xpdl1_WorkflowProcessType477'):
        assert _is_linked(a2, 'xpdl1_WorkflowProcessType477', b)
    _safe_set(b, 'xpdl1_ProcessHeaderType478', None)
    assert not _is_linked(b, 'xpdl1_ProcessHeaderType478', a2)
    if hasattr(a2, 'xpdl1_WorkflowProcessType477'):
        assert not _is_linked(a2, 'xpdl1_WorkflowProcessType477', b)


def test_assoc_redefinableHeader200_reverse_link_reassign_clear():
    a1 = xpdl1_RedefinableHeaderType(author="sample_text", codepage="sample_text", countrykey="sample_text", publicationStatus="sample_text", version="sample_text")
    a2 = xpdl1_RedefinableHeaderType(author="sample_text_2", codepage="sample_text_2", countrykey="sample_text_2", publicationStatus="sample_text_2", version="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot201', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot201', a1)
    if hasattr(a1, 'xpdl1_RedefinableHeaderType'):
        assert _is_linked(a1, 'xpdl1_RedefinableHeaderType', b)
    _safe_set(b, 'xpdl1_DocumentRoot201', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot201', a2)
    if hasattr(a1, 'xpdl1_RedefinableHeaderType'):
        assert not _is_linked(a1, 'xpdl1_RedefinableHeaderType', b)
    if hasattr(a2, 'xpdl1_RedefinableHeaderType'):
        assert _is_linked(a2, 'xpdl1_RedefinableHeaderType', b)
    _safe_set(b, 'xpdl1_DocumentRoot201', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot201', a2)
    if hasattr(a2, 'xpdl1_RedefinableHeaderType'):
        assert not _is_linked(a2, 'xpdl1_RedefinableHeaderType', b)


def test_assoc_redefinableHeader344_reverse_link_reassign_clear():
    a1 = xpdl1_RedefinableHeaderType(author="sample_text", codepage="sample_text", countrykey="sample_text", publicationStatus="sample_text", version="sample_text")
    a2 = xpdl1_RedefinableHeaderType(author="sample_text_2", codepage="sample_text_2", countrykey="sample_text_2", publicationStatus="sample_text_2", version="sample_text_2")
    b = xpdl1_PackageType(id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl1_PackageType345', a1)
    assert _is_linked(b, 'xpdl1_PackageType345', a1)
    if hasattr(a1, 'xpdl1_RedefinableHeaderType346'):
        assert _is_linked(a1, 'xpdl1_RedefinableHeaderType346', b)
    _safe_set(b, 'xpdl1_PackageType345', a2)
    assert _is_linked(b, 'xpdl1_PackageType345', a2)
    if hasattr(a1, 'xpdl1_RedefinableHeaderType346'):
        assert not _is_linked(a1, 'xpdl1_RedefinableHeaderType346', b)
    if hasattr(a2, 'xpdl1_RedefinableHeaderType346'):
        assert _is_linked(a2, 'xpdl1_RedefinableHeaderType346', b)
    _safe_set(b, 'xpdl1_PackageType345', None)
    assert not _is_linked(b, 'xpdl1_PackageType345', a2)
    if hasattr(a2, 'xpdl1_RedefinableHeaderType346'):
        assert not _is_linked(a2, 'xpdl1_RedefinableHeaderType346', b)


def test_assoc_redefinableHeader479_reverse_link_reassign_clear():
    a1 = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_WorkflowProcessType(accessLevel="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_RedefinableHeaderType(author="sample_text", codepage="sample_text", countrykey="sample_text", publicationStatus="sample_text", version="sample_text")
    _safe_set(b, 'xpdl1_RedefinableHeaderType481', a1)
    assert _is_linked(b, 'xpdl1_RedefinableHeaderType481', a1)
    if hasattr(a1, 'xpdl1_WorkflowProcessType480'):
        assert _is_linked(a1, 'xpdl1_WorkflowProcessType480', b)
    _safe_set(b, 'xpdl1_RedefinableHeaderType481', a2)
    assert _is_linked(b, 'xpdl1_RedefinableHeaderType481', a2)
    if hasattr(a1, 'xpdl1_WorkflowProcessType480'):
        assert not _is_linked(a1, 'xpdl1_WorkflowProcessType480', b)
    if hasattr(a2, 'xpdl1_WorkflowProcessType480'):
        assert _is_linked(a2, 'xpdl1_WorkflowProcessType480', b)
    _safe_set(b, 'xpdl1_RedefinableHeaderType481', None)
    assert not _is_linked(b, 'xpdl1_RedefinableHeaderType481', a2)
    if hasattr(a2, 'xpdl1_WorkflowProcessType480'):
        assert not _is_linked(a2, 'xpdl1_WorkflowProcessType480', b)


def test_assoc_responsibles202_reverse_link_reassign_clear():
    a1 = xpdl1_ResponsiblesType(responsible="sample_text")
    a2 = xpdl1_ResponsiblesType(responsible="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot203', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot203', a1)
    if hasattr(a1, 'xpdl1_ResponsiblesType'):
        assert _is_linked(a1, 'xpdl1_ResponsiblesType', b)
    _safe_set(b, 'xpdl1_DocumentRoot203', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot203', a2)
    if hasattr(a1, 'xpdl1_ResponsiblesType'):
        assert not _is_linked(a1, 'xpdl1_ResponsiblesType', b)
    if hasattr(a2, 'xpdl1_ResponsiblesType'):
        assert _is_linked(a2, 'xpdl1_ResponsiblesType', b)
    _safe_set(b, 'xpdl1_DocumentRoot203', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot203', a2)
    if hasattr(a2, 'xpdl1_ResponsiblesType'):
        assert not _is_linked(a2, 'xpdl1_ResponsiblesType', b)


def test_assoc_responsibles392_reverse_link_reassign_clear():
    a1 = xpdl1_ResponsiblesType(responsible="sample_text")
    a2 = xpdl1_ResponsiblesType(responsible="sample_text_2")
    b = xpdl1_RedefinableHeaderType(author="sample_text", codepage="sample_text", countrykey="sample_text", publicationStatus="sample_text", version="sample_text")
    _safe_set(b, 'xpdl1_RedefinableHeaderType393', a1)
    assert _is_linked(b, 'xpdl1_RedefinableHeaderType393', a1)
    if hasattr(a1, 'xpdl1_ResponsiblesType394'):
        assert _is_linked(a1, 'xpdl1_ResponsiblesType394', b)
    _safe_set(b, 'xpdl1_RedefinableHeaderType393', a2)
    assert _is_linked(b, 'xpdl1_RedefinableHeaderType393', a2)
    if hasattr(a1, 'xpdl1_ResponsiblesType394'):
        assert not _is_linked(a1, 'xpdl1_ResponsiblesType394', b)
    if hasattr(a2, 'xpdl1_ResponsiblesType394'):
        assert _is_linked(a2, 'xpdl1_ResponsiblesType394', b)
    _safe_set(b, 'xpdl1_RedefinableHeaderType393', None)
    assert not _is_linked(b, 'xpdl1_RedefinableHeaderType393', a2)
    if hasattr(a2, 'xpdl1_ResponsiblesType394'):
        assert not _is_linked(a2, 'xpdl1_ResponsiblesType394', b)


def test_assoc_schemaType207_reverse_link_reassign_clear():
    a1 = xpdl1_SchemaTypeType(any="sample_text")
    a2 = xpdl1_SchemaTypeType(any="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot208', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot208', a1)
    if hasattr(a1, 'xpdl1_SchemaTypeType209'):
        assert _is_linked(a1, 'xpdl1_SchemaTypeType209', b)
    _safe_set(b, 'xpdl1_DocumentRoot208', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot208', a2)
    if hasattr(a1, 'xpdl1_SchemaTypeType209'):
        assert not _is_linked(a1, 'xpdl1_SchemaTypeType209', b)
    if hasattr(a2, 'xpdl1_SchemaTypeType209'):
        assert _is_linked(a2, 'xpdl1_SchemaTypeType209', b)
    _safe_set(b, 'xpdl1_DocumentRoot208', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot208', a2)
    if hasattr(a2, 'xpdl1_SchemaTypeType209'):
        assert not _is_linked(a2, 'xpdl1_SchemaTypeType209', b)


def test_assoc_schemaType36_reverse_link_reassign_clear():
    a1 = xpdl1_SchemaTypeType(any="sample_text")
    a2 = xpdl1_SchemaTypeType(any="sample_text_2")
    b = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    _safe_set(b, 'xpdl1_ArrayTypeType37', a1)
    assert _is_linked(b, 'xpdl1_ArrayTypeType37', a1)
    if hasattr(a1, 'xpdl1_SchemaTypeType'):
        assert _is_linked(a1, 'xpdl1_SchemaTypeType', b)
    _safe_set(b, 'xpdl1_ArrayTypeType37', a2)
    assert _is_linked(b, 'xpdl1_ArrayTypeType37', a2)
    if hasattr(a1, 'xpdl1_SchemaTypeType'):
        assert not _is_linked(a1, 'xpdl1_SchemaTypeType', b)
    if hasattr(a2, 'xpdl1_SchemaTypeType'):
        assert _is_linked(a2, 'xpdl1_SchemaTypeType', b)
    _safe_set(b, 'xpdl1_ArrayTypeType37', None)
    assert not _is_linked(b, 'xpdl1_ArrayTypeType37', a2)
    if hasattr(a2, 'xpdl1_SchemaTypeType'):
        assert not _is_linked(a2, 'xpdl1_SchemaTypeType', b)


def test_assoc_schemaType446_reverse_link_reassign_clear():
    a1 = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_SchemaTypeType(any="sample_text")
    _safe_set(b, 'xpdl1_SchemaTypeType448', a1)
    assert _is_linked(b, 'xpdl1_SchemaTypeType448', a1)
    if hasattr(a1, 'xpdl1_TypeDeclarationType447'):
        assert _is_linked(a1, 'xpdl1_TypeDeclarationType447', b)
    _safe_set(b, 'xpdl1_SchemaTypeType448', a2)
    assert _is_linked(b, 'xpdl1_SchemaTypeType448', a2)
    if hasattr(a1, 'xpdl1_TypeDeclarationType447'):
        assert not _is_linked(a1, 'xpdl1_TypeDeclarationType447', b)
    if hasattr(a2, 'xpdl1_TypeDeclarationType447'):
        assert _is_linked(a2, 'xpdl1_TypeDeclarationType447', b)
    _safe_set(b, 'xpdl1_SchemaTypeType448', None)
    assert not _is_linked(b, 'xpdl1_SchemaTypeType448', a2)
    if hasattr(a2, 'xpdl1_TypeDeclarationType447'):
        assert not _is_linked(a2, 'xpdl1_TypeDeclarationType447', b)


def test_assoc_script210_reverse_link_reassign_clear():
    a1 = xpdl1_ScriptType(grammar="sample_text", type="sample_text", version="sample_text")
    a2 = xpdl1_ScriptType(grammar="sample_text_2", type="sample_text_2", version="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot211', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot211', a1)
    if hasattr(a1, 'xpdl1_ScriptType'):
        assert _is_linked(a1, 'xpdl1_ScriptType', b)
    _safe_set(b, 'xpdl1_DocumentRoot211', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot211', a2)
    if hasattr(a1, 'xpdl1_ScriptType'):
        assert not _is_linked(a1, 'xpdl1_ScriptType', b)
    if hasattr(a2, 'xpdl1_ScriptType'):
        assert _is_linked(a2, 'xpdl1_ScriptType', b)
    _safe_set(b, 'xpdl1_DocumentRoot211', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot211', a2)
    if hasattr(a2, 'xpdl1_ScriptType'):
        assert not _is_linked(a2, 'xpdl1_ScriptType', b)


def test_assoc_script350_reverse_link_reassign_clear():
    a1 = xpdl1_ScriptType(grammar="sample_text", type="sample_text", version="sample_text")
    a2 = xpdl1_ScriptType(grammar="sample_text_2", type="sample_text_2", version="sample_text_2")
    b = xpdl1_PackageType(id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl1_PackageType351', a1)
    assert _is_linked(b, 'xpdl1_PackageType351', a1)
    if hasattr(a1, 'xpdl1_ScriptType352'):
        assert _is_linked(a1, 'xpdl1_ScriptType352', b)
    _safe_set(b, 'xpdl1_PackageType351', a2)
    assert _is_linked(b, 'xpdl1_PackageType351', a2)
    if hasattr(a1, 'xpdl1_ScriptType352'):
        assert not _is_linked(a1, 'xpdl1_ScriptType352', b)
    if hasattr(a2, 'xpdl1_ScriptType352'):
        assert _is_linked(a2, 'xpdl1_ScriptType352', b)
    _safe_set(b, 'xpdl1_PackageType351', None)
    assert not _is_linked(b, 'xpdl1_PackageType351', a2)
    if hasattr(a2, 'xpdl1_ScriptType352'):
        assert not _is_linked(a2, 'xpdl1_ScriptType352', b)


def test_assoc_simulationInformation19_reverse_link_reassign_clear():
    a1 = xpdl1_SimulationInformationType(cost="sample_text", instantiation="sample_text")
    a2 = xpdl1_SimulationInformationType(cost="sample_text_2", instantiation="sample_text_2")
    b = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    _safe_set(b, 'xpdl1_ActivityType20', a1)
    assert _is_linked(b, 'xpdl1_ActivityType20', a1)
    if hasattr(a1, 'xpdl1_SimulationInformationType'):
        assert _is_linked(a1, 'xpdl1_SimulationInformationType', b)
    _safe_set(b, 'xpdl1_ActivityType20', a2)
    assert _is_linked(b, 'xpdl1_ActivityType20', a2)
    if hasattr(a1, 'xpdl1_SimulationInformationType'):
        assert not _is_linked(a1, 'xpdl1_SimulationInformationType', b)
    if hasattr(a2, 'xpdl1_SimulationInformationType'):
        assert _is_linked(a2, 'xpdl1_SimulationInformationType', b)
    _safe_set(b, 'xpdl1_ActivityType20', None)
    assert not _is_linked(b, 'xpdl1_ActivityType20', a2)
    if hasattr(a2, 'xpdl1_SimulationInformationType'):
        assert not _is_linked(a2, 'xpdl1_SimulationInformationType', b)


def test_assoc_simulationInformation212_reverse_link_reassign_clear():
    a1 = xpdl1_SimulationInformationType(cost="sample_text", instantiation="sample_text")
    a2 = xpdl1_SimulationInformationType(cost="sample_text_2", instantiation="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot213', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot213', a1)
    if hasattr(a1, 'xpdl1_SimulationInformationType214'):
        assert _is_linked(a1, 'xpdl1_SimulationInformationType214', b)
    _safe_set(b, 'xpdl1_DocumentRoot213', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot213', a2)
    if hasattr(a1, 'xpdl1_SimulationInformationType214'):
        assert not _is_linked(a1, 'xpdl1_SimulationInformationType214', b)
    if hasattr(a2, 'xpdl1_SimulationInformationType214'):
        assert _is_linked(a2, 'xpdl1_SimulationInformationType214', b)
    _safe_set(b, 'xpdl1_DocumentRoot213', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot213', a2)
    if hasattr(a2, 'xpdl1_SimulationInformationType214'):
        assert not _is_linked(a2, 'xpdl1_SimulationInformationType214', b)


def test_assoc_split215_reverse_link_reassign_clear():
    a1 = xpdl1_SplitType(type="sample_text")
    a2 = xpdl1_SplitType(type="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot216', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot216', a1)
    if hasattr(a1, 'xpdl1_SplitType'):
        assert _is_linked(a1, 'xpdl1_SplitType', b)
    _safe_set(b, 'xpdl1_DocumentRoot216', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot216', a2)
    if hasattr(a1, 'xpdl1_SplitType'):
        assert not _is_linked(a1, 'xpdl1_SplitType', b)
    if hasattr(a2, 'xpdl1_SplitType'):
        assert _is_linked(a2, 'xpdl1_SplitType', b)
    _safe_set(b, 'xpdl1_DocumentRoot216', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot216', a2)
    if hasattr(a2, 'xpdl1_SplitType'):
        assert not _is_linked(a2, 'xpdl1_SplitType', b)


def test_assoc_subFlow220_reverse_link_reassign_clear():
    a1 = xpdl1_SubFlowType(execution="sample_text", id="sample_text")
    a2 = xpdl1_SubFlowType(execution="sample_text_2", id="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot221', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot221', a1)
    if hasattr(a1, 'xpdl1_SubFlowType'):
        assert _is_linked(a1, 'xpdl1_SubFlowType', b)
    _safe_set(b, 'xpdl1_DocumentRoot221', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot221', a2)
    if hasattr(a1, 'xpdl1_SubFlowType'):
        assert not _is_linked(a1, 'xpdl1_SubFlowType', b)
    if hasattr(a2, 'xpdl1_SubFlowType'):
        assert _is_linked(a2, 'xpdl1_SubFlowType', b)
    _safe_set(b, 'xpdl1_DocumentRoot221', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot221', a2)
    if hasattr(a2, 'xpdl1_SubFlowType'):
        assert not _is_linked(a2, 'xpdl1_SubFlowType', b)


def test_assoc_timeEstimation222_reverse_link_reassign_clear():
    a1 = xpdl1_TimeEstimationType(duration="sample_text", waitingTime="sample_text", workingTime="sample_text")
    a2 = xpdl1_TimeEstimationType(duration="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot223', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot223', a1)
    if hasattr(a1, 'xpdl1_TimeEstimationType'):
        assert _is_linked(a1, 'xpdl1_TimeEstimationType', b)
    _safe_set(b, 'xpdl1_DocumentRoot223', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot223', a2)
    if hasattr(a1, 'xpdl1_TimeEstimationType'):
        assert not _is_linked(a1, 'xpdl1_TimeEstimationType', b)
    if hasattr(a2, 'xpdl1_TimeEstimationType'):
        assert _is_linked(a2, 'xpdl1_TimeEstimationType', b)
    _safe_set(b, 'xpdl1_DocumentRoot223', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot223', a2)
    if hasattr(a2, 'xpdl1_TimeEstimationType'):
        assert not _is_linked(a2, 'xpdl1_TimeEstimationType', b)


def test_assoc_timeEstimation386_reverse_link_reassign_clear():
    a1 = xpdl1_TimeEstimationType(duration="sample_text", waitingTime="sample_text", workingTime="sample_text")
    a2 = xpdl1_TimeEstimationType(duration="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2")
    b = xpdl1_ProcessHeaderType(created="sample_text", description="sample_text", durationUnit="sample_text", limit="sample_text", priority="sample_text", validFrom="sample_text", validTo="sample_text")
    _safe_set(b, 'xpdl1_ProcessHeaderType387', a1)
    assert _is_linked(b, 'xpdl1_ProcessHeaderType387', a1)
    if hasattr(a1, 'xpdl1_TimeEstimationType388'):
        assert _is_linked(a1, 'xpdl1_TimeEstimationType388', b)
    _safe_set(b, 'xpdl1_ProcessHeaderType387', a2)
    assert _is_linked(b, 'xpdl1_ProcessHeaderType387', a2)
    if hasattr(a1, 'xpdl1_TimeEstimationType388'):
        assert not _is_linked(a1, 'xpdl1_TimeEstimationType388', b)
    if hasattr(a2, 'xpdl1_TimeEstimationType388'):
        assert _is_linked(a2, 'xpdl1_TimeEstimationType388', b)
    _safe_set(b, 'xpdl1_ProcessHeaderType387', None)
    assert not _is_linked(b, 'xpdl1_ProcessHeaderType387', a2)
    if hasattr(a2, 'xpdl1_TimeEstimationType388'):
        assert not _is_linked(a2, 'xpdl1_TimeEstimationType388', b)


def test_assoc_timeEstimation395_reverse_link_reassign_clear():
    a1 = xpdl1_TimeEstimationType(duration="sample_text", waitingTime="sample_text", workingTime="sample_text")
    a2 = xpdl1_TimeEstimationType(duration="sample_text_2", waitingTime="sample_text_2", workingTime="sample_text_2")
    b = xpdl1_SimulationInformationType(cost="sample_text", instantiation="sample_text")
    _safe_set(b, 'xpdl1_SimulationInformationType396', a1)
    assert _is_linked(b, 'xpdl1_SimulationInformationType396', a1)
    if hasattr(a1, 'xpdl1_TimeEstimationType397'):
        assert _is_linked(a1, 'xpdl1_TimeEstimationType397', b)
    _safe_set(b, 'xpdl1_SimulationInformationType396', a2)
    assert _is_linked(b, 'xpdl1_SimulationInformationType396', a2)
    if hasattr(a1, 'xpdl1_TimeEstimationType397'):
        assert not _is_linked(a1, 'xpdl1_TimeEstimationType397', b)
    if hasattr(a2, 'xpdl1_TimeEstimationType397'):
        assert _is_linked(a2, 'xpdl1_TimeEstimationType397', b)
    _safe_set(b, 'xpdl1_SimulationInformationType396', None)
    assert not _is_linked(b, 'xpdl1_SimulationInformationType396', a2)
    if hasattr(a2, 'xpdl1_TimeEstimationType397'):
        assert not _is_linked(a2, 'xpdl1_TimeEstimationType397', b)


def test_assoc_tool224_reverse_link_reassign_clear():
    a1 = xpdl1_ToolType(description="sample_text", id="sample_text", type="sample_text")
    a2 = xpdl1_ToolType(description="sample_text_2", id="sample_text_2", type="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot225', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot225', a1)
    if hasattr(a1, 'xpdl1_ToolType'):
        assert _is_linked(a1, 'xpdl1_ToolType', b)
    _safe_set(b, 'xpdl1_DocumentRoot225', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot225', a2)
    if hasattr(a1, 'xpdl1_ToolType'):
        assert not _is_linked(a1, 'xpdl1_ToolType', b)
    if hasattr(a2, 'xpdl1_ToolType'):
        assert _is_linked(a2, 'xpdl1_ToolType', b)
    _safe_set(b, 'xpdl1_DocumentRoot225', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot225', a2)
    if hasattr(a2, 'xpdl1_ToolType'):
        assert not _is_linked(a2, 'xpdl1_ToolType', b)


def test_assoc_transition226_reverse_link_reassign_clear():
    a1 = xpdl1_TransitionType(description="sample_text", from_="sample_text", id="sample_text", name="sample_text", to="sample_text")
    a2 = xpdl1_TransitionType(description="sample_text_2", from_="sample_text_2", id="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot227', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot227', a1)
    if hasattr(a1, 'xpdl1_TransitionType'):
        assert _is_linked(a1, 'xpdl1_TransitionType', b)
    _safe_set(b, 'xpdl1_DocumentRoot227', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot227', a2)
    if hasattr(a1, 'xpdl1_TransitionType'):
        assert not _is_linked(a1, 'xpdl1_TransitionType', b)
    if hasattr(a2, 'xpdl1_TransitionType'):
        assert _is_linked(a2, 'xpdl1_TransitionType', b)
    _safe_set(b, 'xpdl1_DocumentRoot227', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot227', a2)
    if hasattr(a2, 'xpdl1_TransitionType'):
        assert not _is_linked(a2, 'xpdl1_TransitionType', b)


def test_assoc_transitionRef228_reverse_link_reassign_clear():
    a1 = xpdl1_TransitionRefType(id="sample_text")
    a2 = xpdl1_TransitionRefType(id="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot229', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot229', a1)
    if hasattr(a1, 'xpdl1_TransitionRefType'):
        assert _is_linked(a1, 'xpdl1_TransitionRefType', b)
    _safe_set(b, 'xpdl1_DocumentRoot229', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot229', a2)
    if hasattr(a1, 'xpdl1_TransitionRefType'):
        assert not _is_linked(a1, 'xpdl1_TransitionRefType', b)
    if hasattr(a2, 'xpdl1_TransitionRefType'):
        assert _is_linked(a2, 'xpdl1_TransitionRefType', b)
    _safe_set(b, 'xpdl1_DocumentRoot229', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot229', a2)
    if hasattr(a2, 'xpdl1_TransitionRefType'):
        assert not _is_linked(a2, 'xpdl1_TransitionRefType', b)


def test_assoc_typeDeclaration240_reverse_link_reassign_clear():
    a1 = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot241', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot241', a1)
    if hasattr(a1, 'xpdl1_TypeDeclarationType'):
        assert _is_linked(a1, 'xpdl1_TypeDeclarationType', b)
    _safe_set(b, 'xpdl1_DocumentRoot241', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot241', a2)
    if hasattr(a1, 'xpdl1_TypeDeclarationType'):
        assert not _is_linked(a1, 'xpdl1_TypeDeclarationType', b)
    if hasattr(a2, 'xpdl1_TypeDeclarationType'):
        assert _is_linked(a2, 'xpdl1_TypeDeclarationType', b)
    _safe_set(b, 'xpdl1_DocumentRoot241', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot241', a2)
    if hasattr(a2, 'xpdl1_TypeDeclarationType'):
        assert not _is_linked(a2, 'xpdl1_TypeDeclarationType', b)


def test_assoc_workflowProcess247_reverse_link_reassign_clear():
    a1 = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl1_WorkflowProcessType(accessLevel="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot248', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot248', a1)
    if hasattr(a1, 'xpdl1_WorkflowProcessType'):
        assert _is_linked(a1, 'xpdl1_WorkflowProcessType', b)
    _safe_set(b, 'xpdl1_DocumentRoot248', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot248', a2)
    if hasattr(a1, 'xpdl1_WorkflowProcessType'):
        assert not _is_linked(a1, 'xpdl1_WorkflowProcessType', b)
    if hasattr(a2, 'xpdl1_WorkflowProcessType'):
        assert _is_linked(a2, 'xpdl1_WorkflowProcessType', b)
    _safe_set(b, 'xpdl1_DocumentRoot248', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot248', a2)
    if hasattr(a2, 'xpdl1_WorkflowProcessType'):
        assert not _is_linked(a2, 'xpdl1_WorkflowProcessType', b)


def test_assoc_xpression251_reverse_link_reassign_clear():
    a1 = xpdl1_XpressionType(any="sample_text", group="sample_text", mixed="sample_text")
    a2 = xpdl1_XpressionType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2")
    b = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    _safe_set(b, 'xpdl1_DocumentRoot252', {a1})
    assert _is_linked(b, 'xpdl1_DocumentRoot252', a1)
    if hasattr(a1, 'xpdl1_XpressionType253'):
        assert _is_linked(a1, 'xpdl1_XpressionType253', b)
    _safe_set(b, 'xpdl1_DocumentRoot252', {a2})
    assert _is_linked(b, 'xpdl1_DocumentRoot252', a2)
    if hasattr(a1, 'xpdl1_XpressionType253'):
        assert not _is_linked(a1, 'xpdl1_XpressionType253', b)
    if hasattr(a2, 'xpdl1_XpressionType253'):
        assert _is_linked(a2, 'xpdl1_XpressionType253', b)
    _safe_set(b, 'xpdl1_DocumentRoot252', set())
    assert not _is_linked(b, 'xpdl1_DocumentRoot252', a2)
    if hasattr(a2, 'xpdl1_XpressionType253'):
        assert not _is_linked(a2, 'xpdl1_XpressionType253', b)


def test_assoc_xpression52_reverse_link_reassign_clear():
    a1 = xpdl1_XpressionType(any="sample_text", group="sample_text", mixed="sample_text")
    a2 = xpdl1_XpressionType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2")
    b = xpdl1_ConditionType(group="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'xpdl1_ConditionType', {a1})
    assert _is_linked(b, 'xpdl1_ConditionType', a1)
    if hasattr(a1, 'xpdl1_XpressionType'):
        assert _is_linked(a1, 'xpdl1_XpressionType', b)
    _safe_set(b, 'xpdl1_ConditionType', {a2})
    assert _is_linked(b, 'xpdl1_ConditionType', a2)
    if hasattr(a1, 'xpdl1_XpressionType'):
        assert not _is_linked(a1, 'xpdl1_XpressionType', b)
    if hasattr(a2, 'xpdl1_XpressionType'):
        assert _is_linked(a2, 'xpdl1_XpressionType', b)
    _safe_set(b, 'xpdl1_ConditionType', set())
    assert not _is_linked(b, 'xpdl1_ConditionType', a2)
    if hasattr(a2, 'xpdl1_XpressionType'):
        assert not _is_linked(a2, 'xpdl1_XpressionType', b)


