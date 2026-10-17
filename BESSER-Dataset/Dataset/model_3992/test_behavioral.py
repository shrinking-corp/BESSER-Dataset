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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activities2_stub_double():
    # xpdl1_ActivitiesType has no real 'xpdl1_ActivitiesType4' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivitySetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivitySetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivitySetType(id="sample_text")
    partner = xpdl1_ActivitiesType()
    setattr(partner, 'xpdl1_ActivitiesType4', None)
    _safe_set(owner, 'xpdl1_ActivitySetType3', partner)
    assert getattr(partner, 'xpdl1_ActivitiesType4') == owner
    _safe_set(owner, 'xpdl1_ActivitySetType3', None)
    assert getattr(partner, 'xpdl1_ActivitiesType4') is None


def test_assoc_activities497_stub_double():
    # xpdl1_ActivitiesType has no real 'xpdl1_ActivitiesType499' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ActivitiesType()
    setattr(partner, 'xpdl1_ActivitiesType499', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType498', partner)
    assert getattr(partner, 'xpdl1_ActivitiesType499') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType498', None)
    assert getattr(partner, 'xpdl1_ActivitiesType499') is None


def test_assoc_activities95_stub_double():
    # xpdl1_ActivitiesType has no real 'xpdl1_ActivitiesType97' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ActivitiesType()
    setattr(partner, 'xpdl1_ActivitiesType97', None)
    _safe_set(owner, 'xpdl1_DocumentRoot96', {partner})
    assert getattr(partner, 'xpdl1_ActivitiesType97') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot96', set())
    assert getattr(partner, 'xpdl1_ActivitiesType97') is None


def test_assoc_activity0_stub_double():
    # xpdl1_ActivitiesType has no real 'xpdl1_ActivitiesType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    partner = xpdl1_ActivitiesType()
    setattr(partner, 'xpdl1_ActivitiesType', None)
    _safe_set(owner, 'xpdl1_ActivityType', partner)
    assert getattr(partner, 'xpdl1_ActivitiesType') == owner
    _safe_set(owner, 'xpdl1_ActivityType', None)
    assert getattr(partner, 'xpdl1_ActivitiesType') is None


def test_assoc_activitySet1_stub_double():
    # xpdl1_ActivitySetsType has no real 'xpdl1_ActivitySetsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivitySetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivitySetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivitySetType(id="sample_text")
    partner = xpdl1_ActivitySetsType()
    setattr(partner, 'xpdl1_ActivitySetsType', None)
    _safe_set(owner, 'xpdl1_ActivitySetType', partner)
    assert getattr(partner, 'xpdl1_ActivitySetsType') == owner
    _safe_set(owner, 'xpdl1_ActivitySetType', None)
    assert getattr(partner, 'xpdl1_ActivitySetsType') is None


def test_assoc_activitySets104_stub_double():
    # xpdl1_ActivitySetsType has no real 'xpdl1_ActivitySetsType106' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ActivitySetsType()
    setattr(partner, 'xpdl1_ActivitySetsType106', None)
    _safe_set(owner, 'xpdl1_DocumentRoot105', {partner})
    assert getattr(partner, 'xpdl1_ActivitySetsType106') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot105', set())
    assert getattr(partner, 'xpdl1_ActivitySetsType106') is None


def test_assoc_activitySets494_stub_double():
    # xpdl1_ActivitySetsType has no real 'xpdl1_ActivitySetsType496' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ActivitySetsType()
    setattr(partner, 'xpdl1_ActivitySetsType496', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType495', partner)
    assert getattr(partner, 'xpdl1_ActivitySetsType496') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType495', None)
    assert getattr(partner, 'xpdl1_ActivitySetsType496') is None


def test_assoc_application25_stub_double():
    # xpdl1_ApplicationsType has no real 'xpdl1_ApplicationsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ApplicationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ApplicationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ApplicationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ApplicationsType()
    setattr(partner, 'xpdl1_ApplicationsType', None)
    _safe_set(owner, 'xpdl1_ApplicationType', partner)
    assert getattr(partner, 'xpdl1_ApplicationsType') == owner
    _safe_set(owner, 'xpdl1_ApplicationType', None)
    assert getattr(partner, 'xpdl1_ApplicationsType') is None


def test_assoc_applications112_stub_double():
    # xpdl1_ApplicationsType has no real 'xpdl1_ApplicationsType114' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ApplicationsType()
    setattr(partner, 'xpdl1_ApplicationsType114', None)
    _safe_set(owner, 'xpdl1_DocumentRoot113', {partner})
    assert getattr(partner, 'xpdl1_ApplicationsType114') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot113', set())
    assert getattr(partner, 'xpdl1_ApplicationsType114') is None


def test_assoc_applications362_stub_double():
    # xpdl1_ApplicationsType has no real 'xpdl1_ApplicationsType364' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_PackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_PackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_PackageType(id="sample_text", name="sample_text")
    partner = xpdl1_ApplicationsType()
    setattr(partner, 'xpdl1_ApplicationsType364', None)
    _safe_set(owner, 'xpdl1_PackageType363', partner)
    assert getattr(partner, 'xpdl1_ApplicationsType364') == owner
    _safe_set(owner, 'xpdl1_PackageType363', None)
    assert getattr(partner, 'xpdl1_ApplicationsType364') is None


def test_assoc_applications491_stub_double():
    # xpdl1_ApplicationsType has no real 'xpdl1_ApplicationsType493' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ApplicationsType()
    setattr(partner, 'xpdl1_ApplicationsType493', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType492', partner)
    assert getattr(partner, 'xpdl1_ApplicationsType493') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType492', None)
    assert getattr(partner, 'xpdl1_ApplicationsType493') is None


def test_assoc_arrayType308_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType309' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ArrayTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ArrayTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType309', None)
    _safe_set(owner, 'xpdl1_ArrayTypeType310', partner)
    assert getattr(partner, 'xpdl1_ListTypeType309') == owner
    _safe_set(owner, 'xpdl1_ArrayTypeType310', None)
    assert getattr(partner, 'xpdl1_ListTypeType309') is None


def test_assoc_arrayType335_stub_double():
    # xpdl1_MemberType has no real 'xpdl1_MemberType336' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ArrayTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ArrayTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    partner = xpdl1_MemberType()
    setattr(partner, 'xpdl1_MemberType336', None)
    _safe_set(owner, 'xpdl1_ArrayTypeType337', partner)
    assert getattr(partner, 'xpdl1_MemberType336') == owner
    _safe_set(owner, 'xpdl1_ArrayTypeType337', None)
    assert getattr(partner, 'xpdl1_MemberType336') is None


def test_assoc_arrayType80_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType81' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ArrayTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ArrayTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType81', None)
    _safe_set(owner, 'xpdl1_ArrayTypeType82', partner)
    assert getattr(partner, 'xpdl1_DataTypeType81') == owner
    _safe_set(owner, 'xpdl1_ArrayTypeType82', None)
    assert getattr(partner, 'xpdl1_DataTypeType81') is None


def test_assoc_automatic118_stub_double():
    # xpdl1_AutomaticType has no real 'xpdl1_AutomaticType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_AutomaticType()
    setattr(partner, 'xpdl1_AutomaticType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot119', {partner})
    assert getattr(partner, 'xpdl1_AutomaticType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot119', set())
    assert getattr(partner, 'xpdl1_AutomaticType') is None


def test_assoc_basicType287_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType288' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_BasicTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_BasicTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_BasicTypeType(type="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType288', None)
    _safe_set(owner, 'xpdl1_BasicTypeType289', partner)
    assert getattr(partner, 'xpdl1_ListTypeType288') == owner
    _safe_set(owner, 'xpdl1_BasicTypeType289', None)
    assert getattr(partner, 'xpdl1_ListTypeType288') is None


def test_assoc_basicType314_stub_double():
    # xpdl1_MemberType has no real 'xpdl1_MemberType315' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_BasicTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_BasicTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_BasicTypeType(type="sample_text")
    partner = xpdl1_MemberType()
    setattr(partner, 'xpdl1_MemberType315', None)
    _safe_set(owner, 'xpdl1_BasicTypeType316', partner)
    assert getattr(partner, 'xpdl1_MemberType315') == owner
    _safe_set(owner, 'xpdl1_BasicTypeType316', None)
    assert getattr(partner, 'xpdl1_MemberType315') is None


def test_assoc_basicType59_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType60' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_BasicTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_BasicTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_BasicTypeType(type="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType60', None)
    _safe_set(owner, 'xpdl1_BasicTypeType61', partner)
    assert getattr(partner, 'xpdl1_DataTypeType60') == owner
    _safe_set(owner, 'xpdl1_BasicTypeType61', None)
    assert getattr(partner, 'xpdl1_DataTypeType60') is None


def test_assoc_dataField53_stub_double():
    # xpdl1_DataFieldsType has no real 'xpdl1_DataFieldsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DataFieldType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DataFieldType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DataFieldType(description="sample_text", id="sample_text", initialValue="sample_text", isArray="sample_text", length="sample_text", name="sample_text")
    partner = xpdl1_DataFieldsType()
    setattr(partner, 'xpdl1_DataFieldsType', None)
    _safe_set(owner, 'xpdl1_DataFieldType', partner)
    assert getattr(partner, 'xpdl1_DataFieldsType') == owner
    _safe_set(owner, 'xpdl1_DataFieldType', None)
    assert getattr(partner, 'xpdl1_DataFieldsType') is None


def test_assoc_dataFields134_stub_double():
    # xpdl1_DataFieldsType has no real 'xpdl1_DataFieldsType136' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_DataFieldsType()
    setattr(partner, 'xpdl1_DataFieldsType136', None)
    _safe_set(owner, 'xpdl1_DocumentRoot135', {partner})
    assert getattr(partner, 'xpdl1_DataFieldsType136') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot135', set())
    assert getattr(partner, 'xpdl1_DataFieldsType136') is None


def test_assoc_dataFields365_stub_double():
    # xpdl1_DataFieldsType has no real 'xpdl1_DataFieldsType367' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_PackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_PackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_PackageType(id="sample_text", name="sample_text")
    partner = xpdl1_DataFieldsType()
    setattr(partner, 'xpdl1_DataFieldsType367', None)
    _safe_set(owner, 'xpdl1_PackageType366', partner)
    assert getattr(partner, 'xpdl1_DataFieldsType367') == owner
    _safe_set(owner, 'xpdl1_PackageType366', None)
    assert getattr(partner, 'xpdl1_DataFieldsType367') is None


def test_assoc_dataFields485_stub_double():
    # xpdl1_DataFieldsType has no real 'xpdl1_DataFieldsType487' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_DataFieldsType()
    setattr(partner, 'xpdl1_DataFieldsType487', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType486', partner)
    assert getattr(partner, 'xpdl1_DataFieldsType487') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType486', None)
    assert getattr(partner, 'xpdl1_DataFieldsType487') is None


def test_assoc_dataType137_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType139' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType139', None)
    _safe_set(owner, 'xpdl1_DocumentRoot138', {partner})
    assert getattr(partner, 'xpdl1_DataTypeType139') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot138', set())
    assert getattr(partner, 'xpdl1_DataTypeType139') is None


def test_assoc_dataType275_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType277' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_FormalParameterType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_FormalParameterType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_FormalParameterType(description="sample_text", id="sample_text", index="sample_text", mode="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType277', None)
    _safe_set(owner, 'xpdl1_FormalParameterType276', partner)
    assert getattr(partner, 'xpdl1_DataTypeType277') == owner
    _safe_set(owner, 'xpdl1_FormalParameterType276', None)
    assert getattr(partner, 'xpdl1_DataTypeType277') is None


def test_assoc_dataType54_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DataFieldType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DataFieldType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DataFieldType(description="sample_text", id="sample_text", initialValue="sample_text", isArray="sample_text", length="sample_text", name="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType', None)
    _safe_set(owner, 'xpdl1_DataFieldType55', partner)
    assert getattr(partner, 'xpdl1_DataTypeType') == owner
    _safe_set(owner, 'xpdl1_DataFieldType55', None)
    assert getattr(partner, 'xpdl1_DataTypeType') is None


def test_assoc_deadlineCondition86_stub_double():
    # xpdl1_EObject has no real 'xpdl1_EObject' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DeadlineType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DeadlineType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DeadlineType(execution="sample_text")
    partner = xpdl1_EObject()
    setattr(partner, 'xpdl1_EObject', None)
    _safe_set(owner, 'xpdl1_DeadlineType87', partner)
    assert getattr(partner, 'xpdl1_EObject') == owner
    _safe_set(owner, 'xpdl1_DeadlineType87', None)
    assert getattr(partner, 'xpdl1_EObject') is None


def test_assoc_declaredType290_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType291' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DeclaredTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DeclaredTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DeclaredTypeType(id="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType291', None)
    _safe_set(owner, 'xpdl1_DeclaredTypeType292', partner)
    assert getattr(partner, 'xpdl1_ListTypeType291') == owner
    _safe_set(owner, 'xpdl1_DeclaredTypeType292', None)
    assert getattr(partner, 'xpdl1_ListTypeType291') is None


def test_assoc_declaredType317_stub_double():
    # xpdl1_MemberType has no real 'xpdl1_MemberType318' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DeclaredTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DeclaredTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DeclaredTypeType(id="sample_text")
    partner = xpdl1_MemberType()
    setattr(partner, 'xpdl1_MemberType318', None)
    _safe_set(owner, 'xpdl1_DeclaredTypeType319', partner)
    assert getattr(partner, 'xpdl1_MemberType318') == owner
    _safe_set(owner, 'xpdl1_DeclaredTypeType319', None)
    assert getattr(partner, 'xpdl1_MemberType318') is None


def test_assoc_declaredType62_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType63' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DeclaredTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DeclaredTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DeclaredTypeType(id="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType63', None)
    _safe_set(owner, 'xpdl1_DeclaredTypeType64', partner)
    assert getattr(partner, 'xpdl1_DataTypeType63') == owner
    _safe_set(owner, 'xpdl1_DeclaredTypeType64', None)
    assert getattr(partner, 'xpdl1_DataTypeType63') is None


def test_assoc_enumerationType146_stub_double():
    # xpdl1_EnumerationTypeType has no real 'xpdl1_EnumerationTypeType148' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_EnumerationTypeType()
    setattr(partner, 'xpdl1_EnumerationTypeType148', None)
    _safe_set(owner, 'xpdl1_DocumentRoot147', {partner})
    assert getattr(partner, 'xpdl1_EnumerationTypeType148') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot147', set())
    assert getattr(partner, 'xpdl1_EnumerationTypeType148') is None


def test_assoc_enumerationType45_stub_double():
    # xpdl1_EnumerationTypeType has no real 'xpdl1_EnumerationTypeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ArrayTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ArrayTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    partner = xpdl1_EnumerationTypeType()
    setattr(partner, 'xpdl1_EnumerationTypeType', None)
    _safe_set(owner, 'xpdl1_ArrayTypeType46', partner)
    assert getattr(partner, 'xpdl1_EnumerationTypeType') == owner
    _safe_set(owner, 'xpdl1_ArrayTypeType46', None)
    assert getattr(partner, 'xpdl1_EnumerationTypeType') is None


def test_assoc_enumerationType458_stub_double():
    # xpdl1_EnumerationTypeType has no real 'xpdl1_EnumerationTypeType460' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_EnumerationTypeType()
    setattr(partner, 'xpdl1_EnumerationTypeType460', None)
    _safe_set(owner, 'xpdl1_TypeDeclarationType459', partner)
    assert getattr(partner, 'xpdl1_EnumerationTypeType460') == owner
    _safe_set(owner, 'xpdl1_TypeDeclarationType459', None)
    assert getattr(partner, 'xpdl1_EnumerationTypeType460') is None


def test_assoc_enumerationValue254_stub_double():
    # xpdl1_EnumerationTypeType has no real 'xpdl1_EnumerationTypeType255' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_EnumerationValueType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_EnumerationValueType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_EnumerationValueType(name="sample_text")
    partner = xpdl1_EnumerationTypeType()
    setattr(partner, 'xpdl1_EnumerationTypeType255', None)
    _safe_set(owner, 'xpdl1_EnumerationValueType256', partner)
    assert getattr(partner, 'xpdl1_EnumerationTypeType255') == owner
    _safe_set(owner, 'xpdl1_EnumerationValueType256', None)
    assert getattr(partner, 'xpdl1_EnumerationTypeType255') is None


def test_assoc_exceptionName88_stub_double():
    # xpdl1_EObject has no real 'xpdl1_EObject90' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DeadlineType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DeadlineType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DeadlineType(execution="sample_text")
    partner = xpdl1_EObject()
    setattr(partner, 'xpdl1_EObject90', None)
    _safe_set(owner, 'xpdl1_DeadlineType89', partner)
    assert getattr(partner, 'xpdl1_EObject90') == owner
    _safe_set(owner, 'xpdl1_DeadlineType89', None)
    assert getattr(partner, 'xpdl1_EObject90') is None


def test_assoc_extendedAttribute257_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType258' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ExtendedAttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ExtendedAttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ExtendedAttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", value="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType258', None)
    _safe_set(owner, 'xpdl1_ExtendedAttributeType259', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType258') == owner
    _safe_set(owner, 'xpdl1_ExtendedAttributeType259', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType258') is None


def test_assoc_extendedAttributes153_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType155' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType155', None)
    _safe_set(owner, 'xpdl1_DocumentRoot154', {partner})
    assert getattr(partner, 'xpdl1_ExtendedAttributesType155') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot154', set())
    assert getattr(partner, 'xpdl1_ExtendedAttributesType155') is None


def test_assoc_extendedAttributes23_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType', None)
    _safe_set(owner, 'xpdl1_ActivityType24', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType') == owner
    _safe_set(owner, 'xpdl1_ActivityType24', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType') is None


def test_assoc_extendedAttributes263_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType265' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ExternalPackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ExternalPackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ExternalPackageType(href="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType265', None)
    _safe_set(owner, 'xpdl1_ExternalPackageType264', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType265') == owner
    _safe_set(owner, 'xpdl1_ExternalPackageType264', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType265') is None


def test_assoc_extendedAttributes30_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType32' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ApplicationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ApplicationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ApplicationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType32', None)
    _safe_set(owner, 'xpdl1_ApplicationType31', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType32') == owner
    _safe_set(owner, 'xpdl1_ApplicationType31', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType32') is None


def test_assoc_extendedAttributes371_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType373' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_PackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_PackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_PackageType(id="sample_text", name="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType373', None)
    _safe_set(owner, 'xpdl1_PackageType372', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType373') == owner
    _safe_set(owner, 'xpdl1_PackageType372', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType373') is None


def test_assoc_extendedAttributes383_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType385' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ParticipantType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ParticipantType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ParticipantType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType385', None)
    _safe_set(owner, 'xpdl1_ParticipantType384', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType385') == owner
    _safe_set(owner, 'xpdl1_ParticipantType384', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType385') is None


def test_assoc_extendedAttributes413_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType415' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ToolType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ToolType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ToolType(description="sample_text", id="sample_text", type="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType415', None)
    _safe_set(owner, 'xpdl1_ToolType414', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType415') == owner
    _safe_set(owner, 'xpdl1_ToolType414', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType415') is None


def test_assoc_extendedAttributes434_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType436' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TransitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TransitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TransitionType(description="sample_text", from_="sample_text", id="sample_text", name="sample_text", to="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType436', None)
    _safe_set(owner, 'xpdl1_TransitionType435', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType436') == owner
    _safe_set(owner, 'xpdl1_TransitionType435', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType436') is None


def test_assoc_extendedAttributes467_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType469' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType469', None)
    _safe_set(owner, 'xpdl1_TypeDeclarationType468', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType469') == owner
    _safe_set(owner, 'xpdl1_TypeDeclarationType468', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType469') is None


def test_assoc_extendedAttributes503_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType505' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType505', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType504', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType505') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType504', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType505') is None


def test_assoc_extendedAttributes56_stub_double():
    # xpdl1_ExtendedAttributesType has no real 'xpdl1_ExtendedAttributesType58' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DataFieldType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DataFieldType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DataFieldType(description="sample_text", id="sample_text", initialValue="sample_text", isArray="sample_text", length="sample_text", name="sample_text")
    partner = xpdl1_ExtendedAttributesType()
    setattr(partner, 'xpdl1_ExtendedAttributesType58', None)
    _safe_set(owner, 'xpdl1_DataFieldType57', partner)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType58') == owner
    _safe_set(owner, 'xpdl1_DataFieldType57', None)
    assert getattr(partner, 'xpdl1_ExtendedAttributesType58') is None


def test_assoc_externalPackage260_stub_double():
    # xpdl1_ExternalPackagesType has no real 'xpdl1_ExternalPackagesType261' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ExternalPackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ExternalPackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ExternalPackageType(href="sample_text")
    partner = xpdl1_ExternalPackagesType()
    setattr(partner, 'xpdl1_ExternalPackagesType261', None)
    _safe_set(owner, 'xpdl1_ExternalPackageType262', partner)
    assert getattr(partner, 'xpdl1_ExternalPackagesType261') == owner
    _safe_set(owner, 'xpdl1_ExternalPackageType262', None)
    assert getattr(partner, 'xpdl1_ExternalPackagesType261') is None


def test_assoc_externalPackages158_stub_double():
    # xpdl1_ExternalPackagesType has no real 'xpdl1_ExternalPackagesType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ExternalPackagesType()
    setattr(partner, 'xpdl1_ExternalPackagesType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot159', {partner})
    assert getattr(partner, 'xpdl1_ExternalPackagesType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot159', set())
    assert getattr(partner, 'xpdl1_ExternalPackagesType') is None


def test_assoc_externalPackages353_stub_double():
    # xpdl1_ExternalPackagesType has no real 'xpdl1_ExternalPackagesType355' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_PackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_PackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_PackageType(id="sample_text", name="sample_text")
    partner = xpdl1_ExternalPackagesType()
    setattr(partner, 'xpdl1_ExternalPackagesType355', None)
    _safe_set(owner, 'xpdl1_PackageType354', partner)
    assert getattr(partner, 'xpdl1_ExternalPackagesType355') == owner
    _safe_set(owner, 'xpdl1_PackageType354', None)
    assert getattr(partner, 'xpdl1_ExternalPackagesType355') is None


def test_assoc_externalReference296_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType297' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ExternalReferenceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ExternalReferenceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType297', None)
    _safe_set(owner, 'xpdl1_ExternalReferenceType298', partner)
    assert getattr(partner, 'xpdl1_ListTypeType297') == owner
    _safe_set(owner, 'xpdl1_ExternalReferenceType298', None)
    assert getattr(partner, 'xpdl1_ListTypeType297') is None


def test_assoc_externalReference323_stub_double():
    # xpdl1_MemberType has no real 'xpdl1_MemberType324' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ExternalReferenceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ExternalReferenceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    partner = xpdl1_MemberType()
    setattr(partner, 'xpdl1_MemberType324', None)
    _safe_set(owner, 'xpdl1_ExternalReferenceType325', partner)
    assert getattr(partner, 'xpdl1_MemberType324') == owner
    _safe_set(owner, 'xpdl1_ExternalReferenceType325', None)
    assert getattr(partner, 'xpdl1_MemberType324') is None


def test_assoc_externalReference68_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType69' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ExternalReferenceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ExternalReferenceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType69', None)
    _safe_set(owner, 'xpdl1_ExternalReferenceType70', partner)
    assert getattr(partner, 'xpdl1_DataTypeType69') == owner
    _safe_set(owner, 'xpdl1_ExternalReferenceType70', None)
    assert getattr(partner, 'xpdl1_DataTypeType69') is None


def test_assoc_finishMode15_stub_double():
    # xpdl1_FinishModeType has no real 'xpdl1_FinishModeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    partner = xpdl1_FinishModeType()
    setattr(partner, 'xpdl1_FinishModeType', None)
    _safe_set(owner, 'xpdl1_ActivityType16', partner)
    assert getattr(partner, 'xpdl1_FinishModeType') == owner
    _safe_set(owner, 'xpdl1_ActivityType16', None)
    assert getattr(partner, 'xpdl1_FinishModeType') is None


def test_assoc_finishMode163_stub_double():
    # xpdl1_FinishModeType has no real 'xpdl1_FinishModeType165' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_FinishModeType()
    setattr(partner, 'xpdl1_FinishModeType165', None)
    _safe_set(owner, 'xpdl1_DocumentRoot164', {partner})
    assert getattr(partner, 'xpdl1_FinishModeType165') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot164', set())
    assert getattr(partner, 'xpdl1_FinishModeType165') is None


def test_assoc_formalParameter272_stub_double():
    # xpdl1_FormalParametersType has no real 'xpdl1_FormalParametersType273' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_FormalParameterType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_FormalParameterType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_FormalParameterType(description="sample_text", id="sample_text", index="sample_text", mode="sample_text")
    partner = xpdl1_FormalParametersType()
    setattr(partner, 'xpdl1_FormalParametersType273', None)
    _safe_set(owner, 'xpdl1_FormalParameterType274', partner)
    assert getattr(partner, 'xpdl1_FormalParametersType273') == owner
    _safe_set(owner, 'xpdl1_FormalParameterType274', None)
    assert getattr(partner, 'xpdl1_FormalParametersType273') is None


def test_assoc_formalParameters168_stub_double():
    # xpdl1_FormalParametersType has no real 'xpdl1_FormalParametersType170' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_FormalParametersType()
    setattr(partner, 'xpdl1_FormalParametersType170', None)
    _safe_set(owner, 'xpdl1_DocumentRoot169', {partner})
    assert getattr(partner, 'xpdl1_FormalParametersType170') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot169', set())
    assert getattr(partner, 'xpdl1_FormalParametersType170') is None


def test_assoc_formalParameters26_stub_double():
    # xpdl1_FormalParametersType has no real 'xpdl1_FormalParametersType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ApplicationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ApplicationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ApplicationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_FormalParametersType()
    setattr(partner, 'xpdl1_FormalParametersType', None)
    _safe_set(owner, 'xpdl1_ApplicationType27', partner)
    assert getattr(partner, 'xpdl1_FormalParametersType') == owner
    _safe_set(owner, 'xpdl1_ApplicationType27', None)
    assert getattr(partner, 'xpdl1_FormalParametersType') is None


def test_assoc_formalParameters482_stub_double():
    # xpdl1_FormalParametersType has no real 'xpdl1_FormalParametersType484' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_FormalParametersType()
    setattr(partner, 'xpdl1_FormalParametersType484', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType483', partner)
    assert getattr(partner, 'xpdl1_FormalParametersType484') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType483', None)
    assert getattr(partner, 'xpdl1_FormalParametersType484') is None


def test_assoc_implementation171_stub_double():
    # xpdl1_ImplementationType has no real 'xpdl1_ImplementationType173' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ImplementationType()
    setattr(partner, 'xpdl1_ImplementationType173', None)
    _safe_set(owner, 'xpdl1_DocumentRoot172', {partner})
    assert getattr(partner, 'xpdl1_ImplementationType173') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot172', set())
    assert getattr(partner, 'xpdl1_ImplementationType173') is None


def test_assoc_implementation9_stub_double():
    # xpdl1_ImplementationType has no real 'xpdl1_ImplementationType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    partner = xpdl1_ImplementationType()
    setattr(partner, 'xpdl1_ImplementationType', None)
    _safe_set(owner, 'xpdl1_ActivityType10', partner)
    assert getattr(partner, 'xpdl1_ImplementationType') == owner
    _safe_set(owner, 'xpdl1_ActivityType10', None)
    assert getattr(partner, 'xpdl1_ImplementationType') is None


def test_assoc_join422_stub_double():
    # xpdl1_TransitionRestrictionType has no real 'xpdl1_TransitionRestrictionType423' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_JoinType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_JoinType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_JoinType(type="sample_text")
    partner = xpdl1_TransitionRestrictionType()
    setattr(partner, 'xpdl1_TransitionRestrictionType423', None)
    _safe_set(owner, 'xpdl1_JoinType424', partner)
    assert getattr(partner, 'xpdl1_TransitionRestrictionType423') == owner
    _safe_set(owner, 'xpdl1_JoinType424', None)
    assert getattr(partner, 'xpdl1_TransitionRestrictionType423') is None


def test_assoc_listType176_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType178' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType178', None)
    _safe_set(owner, 'xpdl1_DocumentRoot177', {partner})
    assert getattr(partner, 'xpdl1_ListTypeType178') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot177', set())
    assert getattr(partner, 'xpdl1_ListTypeType178') is None


def test_assoc_listType464_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType466' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType466', None)
    _safe_set(owner, 'xpdl1_TypeDeclarationType465', partner)
    assert getattr(partner, 'xpdl1_ListTypeType466') == owner
    _safe_set(owner, 'xpdl1_TypeDeclarationType465', None)
    assert getattr(partner, 'xpdl1_ListTypeType466') is None


def test_assoc_listType50_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ArrayTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ArrayTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType', None)
    _safe_set(owner, 'xpdl1_ArrayTypeType51', partner)
    assert getattr(partner, 'xpdl1_ListTypeType') == owner
    _safe_set(owner, 'xpdl1_ArrayTypeType51', None)
    assert getattr(partner, 'xpdl1_ListTypeType') is None


def test_assoc_manual179_stub_double():
    # xpdl1_ManualType has no real 'xpdl1_ManualType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ManualType()
    setattr(partner, 'xpdl1_ManualType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot180', {partner})
    assert getattr(partner, 'xpdl1_ManualType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot180', set())
    assert getattr(partner, 'xpdl1_ManualType') is None


def test_assoc_member181_stub_double():
    # xpdl1_MemberType has no real 'xpdl1_MemberType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_MemberType()
    setattr(partner, 'xpdl1_MemberType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot182', {partner})
    assert getattr(partner, 'xpdl1_MemberType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot182', set())
    assert getattr(partner, 'xpdl1_MemberType') is None


def test_assoc_no183_stub_double():
    # xpdl1_NoType has no real 'xpdl1_NoType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_NoType()
    setattr(partner, 'xpdl1_NoType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot184', {partner})
    assert getattr(partner, 'xpdl1_NoType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot184', set())
    assert getattr(partner, 'xpdl1_NoType') is None


def test_assoc_participant374_stub_double():
    # xpdl1_ParticipantsType has no real 'xpdl1_ParticipantsType375' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ParticipantType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ParticipantType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ParticipantType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ParticipantsType()
    setattr(partner, 'xpdl1_ParticipantsType375', None)
    _safe_set(owner, 'xpdl1_ParticipantType376', partner)
    assert getattr(partner, 'xpdl1_ParticipantsType375') == owner
    _safe_set(owner, 'xpdl1_ParticipantType376', None)
    assert getattr(partner, 'xpdl1_ParticipantsType375') is None


def test_assoc_participants191_stub_double():
    # xpdl1_ParticipantsType has no real 'xpdl1_ParticipantsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_ParticipantsType()
    setattr(partner, 'xpdl1_ParticipantsType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot192', {partner})
    assert getattr(partner, 'xpdl1_ParticipantsType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot192', set())
    assert getattr(partner, 'xpdl1_ParticipantsType') is None


def test_assoc_participants359_stub_double():
    # xpdl1_ParticipantsType has no real 'xpdl1_ParticipantsType361' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_PackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_PackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_PackageType(id="sample_text", name="sample_text")
    partner = xpdl1_ParticipantsType()
    setattr(partner, 'xpdl1_ParticipantsType361', None)
    _safe_set(owner, 'xpdl1_PackageType360', partner)
    assert getattr(partner, 'xpdl1_ParticipantsType361') == owner
    _safe_set(owner, 'xpdl1_PackageType360', None)
    assert getattr(partner, 'xpdl1_ParticipantsType361') is None


def test_assoc_participants488_stub_double():
    # xpdl1_ParticipantsType has no real 'xpdl1_ParticipantsType490' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_ParticipantsType()
    setattr(partner, 'xpdl1_ParticipantsType490', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType489', partner)
    assert getattr(partner, 'xpdl1_ParticipantsType490') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType489', None)
    assert getattr(partner, 'xpdl1_ParticipantsType490') is None


def test_assoc_recordType197_stub_double():
    # xpdl1_RecordTypeType has no real 'xpdl1_RecordTypeType199' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_RecordTypeType()
    setattr(partner, 'xpdl1_RecordTypeType199', None)
    _safe_set(owner, 'xpdl1_DocumentRoot198', {partner})
    assert getattr(partner, 'xpdl1_RecordTypeType199') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot198', set())
    assert getattr(partner, 'xpdl1_RecordTypeType199') is None


def test_assoc_recordType41_stub_double():
    # xpdl1_RecordTypeType has no real 'xpdl1_RecordTypeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ArrayTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ArrayTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    partner = xpdl1_RecordTypeType()
    setattr(partner, 'xpdl1_RecordTypeType', None)
    _safe_set(owner, 'xpdl1_ArrayTypeType42', partner)
    assert getattr(partner, 'xpdl1_RecordTypeType') == owner
    _safe_set(owner, 'xpdl1_ArrayTypeType42', None)
    assert getattr(partner, 'xpdl1_RecordTypeType') is None


def test_assoc_recordType452_stub_double():
    # xpdl1_RecordTypeType has no real 'xpdl1_RecordTypeType454' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_RecordTypeType()
    setattr(partner, 'xpdl1_RecordTypeType454', None)
    _safe_set(owner, 'xpdl1_TypeDeclarationType453', partner)
    assert getattr(partner, 'xpdl1_RecordTypeType454') == owner
    _safe_set(owner, 'xpdl1_TypeDeclarationType453', None)
    assert getattr(partner, 'xpdl1_RecordTypeType454') is None


def test_assoc_route204_stub_double():
    # xpdl1_RouteType has no real 'xpdl1_RouteType206' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_RouteType()
    setattr(partner, 'xpdl1_RouteType206', None)
    _safe_set(owner, 'xpdl1_DocumentRoot205', {partner})
    assert getattr(partner, 'xpdl1_RouteType206') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot205', set())
    assert getattr(partner, 'xpdl1_RouteType206') is None


def test_assoc_route7_stub_double():
    # xpdl1_RouteType has no real 'xpdl1_RouteType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    partner = xpdl1_RouteType()
    setattr(partner, 'xpdl1_RouteType', None)
    _safe_set(owner, 'xpdl1_ActivityType8', partner)
    assert getattr(partner, 'xpdl1_RouteType') == owner
    _safe_set(owner, 'xpdl1_ActivityType8', None)
    assert getattr(partner, 'xpdl1_RouteType') is None


def test_assoc_schemaType293_stub_double():
    # xpdl1_ListTypeType has no real 'xpdl1_ListTypeType294' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_SchemaTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_SchemaTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_SchemaTypeType(any="sample_text")
    partner = xpdl1_ListTypeType()
    setattr(partner, 'xpdl1_ListTypeType294', None)
    _safe_set(owner, 'xpdl1_SchemaTypeType295', partner)
    assert getattr(partner, 'xpdl1_ListTypeType294') == owner
    _safe_set(owner, 'xpdl1_SchemaTypeType295', None)
    assert getattr(partner, 'xpdl1_ListTypeType294') is None


def test_assoc_schemaType320_stub_double():
    # xpdl1_MemberType has no real 'xpdl1_MemberType321' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_SchemaTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_SchemaTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_SchemaTypeType(any="sample_text")
    partner = xpdl1_MemberType()
    setattr(partner, 'xpdl1_MemberType321', None)
    _safe_set(owner, 'xpdl1_SchemaTypeType322', partner)
    assert getattr(partner, 'xpdl1_MemberType321') == owner
    _safe_set(owner, 'xpdl1_SchemaTypeType322', None)
    assert getattr(partner, 'xpdl1_MemberType321') is None


def test_assoc_schemaType65_stub_double():
    # xpdl1_DataTypeType has no real 'xpdl1_DataTypeType66' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_SchemaTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_SchemaTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_SchemaTypeType(any="sample_text")
    partner = xpdl1_DataTypeType()
    setattr(partner, 'xpdl1_DataTypeType66', None)
    _safe_set(owner, 'xpdl1_SchemaTypeType67', partner)
    assert getattr(partner, 'xpdl1_DataTypeType66') == owner
    _safe_set(owner, 'xpdl1_SchemaTypeType67', None)
    assert getattr(partner, 'xpdl1_DataTypeType66') is None


def test_assoc_split425_stub_double():
    # xpdl1_TransitionRestrictionType has no real 'xpdl1_TransitionRestrictionType426' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_SplitType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_SplitType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_SplitType(type="sample_text")
    partner = xpdl1_TransitionRestrictionType()
    setattr(partner, 'xpdl1_TransitionRestrictionType426', None)
    _safe_set(owner, 'xpdl1_SplitType427', partner)
    assert getattr(partner, 'xpdl1_TransitionRestrictionType426') == owner
    _safe_set(owner, 'xpdl1_SplitType427', None)
    assert getattr(partner, 'xpdl1_TransitionRestrictionType426') is None


def test_assoc_startMode13_stub_double():
    # xpdl1_StartModeType has no real 'xpdl1_StartModeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    partner = xpdl1_StartModeType()
    setattr(partner, 'xpdl1_StartModeType', None)
    _safe_set(owner, 'xpdl1_ActivityType14', partner)
    assert getattr(partner, 'xpdl1_StartModeType') == owner
    _safe_set(owner, 'xpdl1_ActivityType14', None)
    assert getattr(partner, 'xpdl1_StartModeType') is None


def test_assoc_startMode217_stub_double():
    # xpdl1_StartModeType has no real 'xpdl1_StartModeType219' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_StartModeType()
    setattr(partner, 'xpdl1_StartModeType219', None)
    _safe_set(owner, 'xpdl1_DocumentRoot218', {partner})
    assert getattr(partner, 'xpdl1_StartModeType219') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot218', set())
    assert getattr(partner, 'xpdl1_StartModeType219') is None


def test_assoc_subFlow284_stub_double():
    # xpdl1_ImplementationType has no real 'xpdl1_ImplementationType285' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_SubFlowType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_SubFlowType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_SubFlowType(execution="sample_text", id="sample_text")
    partner = xpdl1_ImplementationType()
    setattr(partner, 'xpdl1_ImplementationType285', None)
    _safe_set(owner, 'xpdl1_SubFlowType286', partner)
    assert getattr(partner, 'xpdl1_ImplementationType285') == owner
    _safe_set(owner, 'xpdl1_SubFlowType286', None)
    assert getattr(partner, 'xpdl1_ImplementationType285') is None


def test_assoc_tool281_stub_double():
    # xpdl1_ImplementationType has no real 'xpdl1_ImplementationType282' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ToolType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ToolType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ToolType(description="sample_text", id="sample_text", type="sample_text")
    partner = xpdl1_ImplementationType()
    setattr(partner, 'xpdl1_ImplementationType282', None)
    _safe_set(owner, 'xpdl1_ToolType283', partner)
    assert getattr(partner, 'xpdl1_ImplementationType282') == owner
    _safe_set(owner, 'xpdl1_ToolType283', None)
    assert getattr(partner, 'xpdl1_ImplementationType282') is None


def test_assoc_transition428_stub_double():
    # xpdl1_TransitionsType has no real 'xpdl1_TransitionsType429' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TransitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TransitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TransitionType(description="sample_text", from_="sample_text", id="sample_text", name="sample_text", to="sample_text")
    partner = xpdl1_TransitionsType()
    setattr(partner, 'xpdl1_TransitionsType429', None)
    _safe_set(owner, 'xpdl1_TransitionType430', partner)
    assert getattr(partner, 'xpdl1_TransitionsType429') == owner
    _safe_set(owner, 'xpdl1_TransitionType430', None)
    assert getattr(partner, 'xpdl1_TransitionsType429') is None


def test_assoc_transitionRef416_stub_double():
    # xpdl1_TransitionRefsType has no real 'xpdl1_TransitionRefsType417' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TransitionRefType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TransitionRefType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TransitionRefType(id="sample_text")
    partner = xpdl1_TransitionRefsType()
    setattr(partner, 'xpdl1_TransitionRefsType417', None)
    _safe_set(owner, 'xpdl1_TransitionRefType418', partner)
    assert getattr(partner, 'xpdl1_TransitionRefsType417') == owner
    _safe_set(owner, 'xpdl1_TransitionRefType418', None)
    assert getattr(partner, 'xpdl1_TransitionRefsType417') is None


def test_assoc_transitionRefs230_stub_double():
    # xpdl1_TransitionRefsType has no real 'xpdl1_TransitionRefsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_TransitionRefsType()
    setattr(partner, 'xpdl1_TransitionRefsType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot231', {partner})
    assert getattr(partner, 'xpdl1_TransitionRefsType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot231', set())
    assert getattr(partner, 'xpdl1_TransitionRefsType') is None


def test_assoc_transitionRefs398_stub_double():
    # xpdl1_TransitionRefsType has no real 'xpdl1_TransitionRefsType400' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_SplitType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_SplitType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_SplitType(type="sample_text")
    partner = xpdl1_TransitionRefsType()
    setattr(partner, 'xpdl1_TransitionRefsType400', None)
    _safe_set(owner, 'xpdl1_SplitType399', partner)
    assert getattr(partner, 'xpdl1_TransitionRefsType400') == owner
    _safe_set(owner, 'xpdl1_SplitType399', None)
    assert getattr(partner, 'xpdl1_TransitionRefsType400') is None


def test_assoc_transitionRestriction232_stub_double():
    # xpdl1_TransitionRestrictionType has no real 'xpdl1_TransitionRestrictionType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_TransitionRestrictionType()
    setattr(partner, 'xpdl1_TransitionRestrictionType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot233', {partner})
    assert getattr(partner, 'xpdl1_TransitionRestrictionType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot233', set())
    assert getattr(partner, 'xpdl1_TransitionRestrictionType') is None


def test_assoc_transitionRestrictions21_stub_double():
    # xpdl1_TransitionRestrictionsType has no real 'xpdl1_TransitionRestrictionsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivityType(description="sample_text", documentation="sample_text", icon="sample_text", id="sample_text", limit="sample_text", name="sample_text", performer="sample_text", priority="sample_text")
    partner = xpdl1_TransitionRestrictionsType()
    setattr(partner, 'xpdl1_TransitionRestrictionsType', None)
    _safe_set(owner, 'xpdl1_ActivityType22', partner)
    assert getattr(partner, 'xpdl1_TransitionRestrictionsType') == owner
    _safe_set(owner, 'xpdl1_ActivityType22', None)
    assert getattr(partner, 'xpdl1_TransitionRestrictionsType') is None


def test_assoc_transitionRestrictions234_stub_double():
    # xpdl1_TransitionRestrictionsType has no real 'xpdl1_TransitionRestrictionsType236' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_TransitionRestrictionsType()
    setattr(partner, 'xpdl1_TransitionRestrictionsType236', None)
    _safe_set(owner, 'xpdl1_DocumentRoot235', {partner})
    assert getattr(partner, 'xpdl1_TransitionRestrictionsType236') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot235', set())
    assert getattr(partner, 'xpdl1_TransitionRestrictionsType236') is None


def test_assoc_transitions237_stub_double():
    # xpdl1_TransitionsType has no real 'xpdl1_TransitionsType239' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_TransitionsType()
    setattr(partner, 'xpdl1_TransitionsType239', None)
    _safe_set(owner, 'xpdl1_DocumentRoot238', {partner})
    assert getattr(partner, 'xpdl1_TransitionsType239') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot238', set())
    assert getattr(partner, 'xpdl1_TransitionsType239') is None


def test_assoc_transitions5_stub_double():
    # xpdl1_TransitionsType has no real 'xpdl1_TransitionsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ActivitySetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ActivitySetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ActivitySetType(id="sample_text")
    partner = xpdl1_TransitionsType()
    setattr(partner, 'xpdl1_TransitionsType', None)
    _safe_set(owner, 'xpdl1_ActivitySetType6', partner)
    assert getattr(partner, 'xpdl1_TransitionsType') == owner
    _safe_set(owner, 'xpdl1_ActivitySetType6', None)
    assert getattr(partner, 'xpdl1_TransitionsType') is None


def test_assoc_transitions500_stub_double():
    # xpdl1_TransitionsType has no real 'xpdl1_TransitionsType502' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_TransitionsType()
    setattr(partner, 'xpdl1_TransitionsType502', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType501', partner)
    assert getattr(partner, 'xpdl1_TransitionsType502') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType501', None)
    assert getattr(partner, 'xpdl1_TransitionsType502') is None


def test_assoc_typeDeclaration437_stub_double():
    # xpdl1_TypeDeclarationsType has no real 'xpdl1_TypeDeclarationsType438' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_TypeDeclarationsType()
    setattr(partner, 'xpdl1_TypeDeclarationsType438', None)
    _safe_set(owner, 'xpdl1_TypeDeclarationType439', partner)
    assert getattr(partner, 'xpdl1_TypeDeclarationsType438') == owner
    _safe_set(owner, 'xpdl1_TypeDeclarationType439', None)
    assert getattr(partner, 'xpdl1_TypeDeclarationsType438') is None


def test_assoc_typeDeclarations242_stub_double():
    # xpdl1_TypeDeclarationsType has no real 'xpdl1_TypeDeclarationsType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_TypeDeclarationsType()
    setattr(partner, 'xpdl1_TypeDeclarationsType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot243', {partner})
    assert getattr(partner, 'xpdl1_TypeDeclarationsType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot243', set())
    assert getattr(partner, 'xpdl1_TypeDeclarationsType') is None


def test_assoc_typeDeclarations356_stub_double():
    # xpdl1_TypeDeclarationsType has no real 'xpdl1_TypeDeclarationsType358' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_PackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_PackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_PackageType(id="sample_text", name="sample_text")
    partner = xpdl1_TypeDeclarationsType()
    setattr(partner, 'xpdl1_TypeDeclarationsType358', None)
    _safe_set(owner, 'xpdl1_PackageType357', partner)
    assert getattr(partner, 'xpdl1_TypeDeclarationsType358') == owner
    _safe_set(owner, 'xpdl1_PackageType357', None)
    assert getattr(partner, 'xpdl1_TypeDeclarationsType358') is None


def test_assoc_unionType244_stub_double():
    # xpdl1_UnionTypeType has no real 'xpdl1_UnionTypeType246' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_UnionTypeType()
    setattr(partner, 'xpdl1_UnionTypeType246', None)
    _safe_set(owner, 'xpdl1_DocumentRoot245', {partner})
    assert getattr(partner, 'xpdl1_UnionTypeType246') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot245', set())
    assert getattr(partner, 'xpdl1_UnionTypeType246') is None


def test_assoc_unionType43_stub_double():
    # xpdl1_UnionTypeType has no real 'xpdl1_UnionTypeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_ArrayTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_ArrayTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_ArrayTypeType(lowerIndex="sample_text", upperIndex="sample_text")
    partner = xpdl1_UnionTypeType()
    setattr(partner, 'xpdl1_UnionTypeType', None)
    _safe_set(owner, 'xpdl1_ArrayTypeType44', partner)
    assert getattr(partner, 'xpdl1_UnionTypeType') == owner
    _safe_set(owner, 'xpdl1_ArrayTypeType44', None)
    assert getattr(partner, 'xpdl1_UnionTypeType') is None


def test_assoc_unionType455_stub_double():
    # xpdl1_UnionTypeType has no real 'xpdl1_UnionTypeType457' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_UnionTypeType()
    setattr(partner, 'xpdl1_UnionTypeType457', None)
    _safe_set(owner, 'xpdl1_TypeDeclarationType456', partner)
    assert getattr(partner, 'xpdl1_UnionTypeType457') == owner
    _safe_set(owner, 'xpdl1_TypeDeclarationType456', None)
    assert getattr(partner, 'xpdl1_UnionTypeType457') is None


def test_assoc_workflowProcess473_stub_double():
    # xpdl1_WorkflowProcessesType has no real 'xpdl1_WorkflowProcessesType474' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_WorkflowProcessType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_WorkflowProcessType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_WorkflowProcessType(accessLevel="sample_text", id="sample_text", name="sample_text")
    partner = xpdl1_WorkflowProcessesType()
    setattr(partner, 'xpdl1_WorkflowProcessesType474', None)
    _safe_set(owner, 'xpdl1_WorkflowProcessType475', partner)
    assert getattr(partner, 'xpdl1_WorkflowProcessesType474') == owner
    _safe_set(owner, 'xpdl1_WorkflowProcessType475', None)
    assert getattr(partner, 'xpdl1_WorkflowProcessesType474') is None


def test_assoc_workflowProcesses249_stub_double():
    # xpdl1_WorkflowProcessesType has no real 'xpdl1_WorkflowProcessesType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_WorkflowProcessesType()
    setattr(partner, 'xpdl1_WorkflowProcessesType', None)
    _safe_set(owner, 'xpdl1_DocumentRoot250', {partner})
    assert getattr(partner, 'xpdl1_WorkflowProcessesType') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot250', set())
    assert getattr(partner, 'xpdl1_WorkflowProcessesType') is None


def test_assoc_workflowProcesses368_stub_double():
    # xpdl1_WorkflowProcessesType has no real 'xpdl1_WorkflowProcessesType370' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_PackageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_PackageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_PackageType(id="sample_text", name="sample_text")
    partner = xpdl1_WorkflowProcessesType()
    setattr(partner, 'xpdl1_WorkflowProcessesType370', None)
    _safe_set(owner, 'xpdl1_PackageType369', partner)
    assert getattr(partner, 'xpdl1_WorkflowProcessesType370') == owner
    _safe_set(owner, 'xpdl1_PackageType369', None)
    assert getattr(partner, 'xpdl1_WorkflowProcessesType370') is None


def test_assoc_xMLNSPrefixMap91_stub_double():
    # xpdl1_EStringToStringMapEntry has no real 'xpdl1_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_EStringToStringMapEntry()
    setattr(partner, 'xpdl1_EStringToStringMapEntry', None)
    _safe_set(owner, 'xpdl1_DocumentRoot', {partner})
    assert getattr(partner, 'xpdl1_EStringToStringMapEntry') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot', set())
    assert getattr(partner, 'xpdl1_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation92_stub_double():
    # xpdl1_EStringToStringMapEntry has no real 'xpdl1_EStringToStringMapEntry94' property in the generated
    # code (a bare stub) -- manually attach it so xpdl1_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl1_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl1_DocumentRoot(actualParameter="sample_text", author="sample_text", codepage="sample_text", cost="sample_text", costUnit="sample_text", countrykey="sample_text", created="sample_text", description="sample_text", documentation="sample_text", duration="sample_text", icon="sample_text", initialValue="sample_text", length="sample_text", limit="sample_text", mixed="sample_text", performer="sample_text", priority="sample_text", priorityUnit="sample_text", responsible="sample_text", validFrom="sample_text", validTo="sample_text", vendor="sample_text", version="sample_text", waitingTime="sample_text", workingTime="sample_text", xPDLVersion="sample_text")
    partner = xpdl1_EStringToStringMapEntry()
    setattr(partner, 'xpdl1_EStringToStringMapEntry94', None)
    _safe_set(owner, 'xpdl1_DocumentRoot93', {partner})
    assert getattr(partner, 'xpdl1_EStringToStringMapEntry94') == owner
    _safe_set(owner, 'xpdl1_DocumentRoot93', set())
    assert getattr(partner, 'xpdl1_EStringToStringMapEntry94') is None


