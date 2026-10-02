#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    DataReaderStatus,
    DataWriterStatus,
    DdsQosProfile,
    DdsReadCondition,
    DdsStatusCondition,
    DestinationOrderQosPolicyKind,
    DomainParticipantStatus,
    DurabilityQosPolicyKind,
    Enum,
    HistoryQosPolicyKind,
    InstanceStateKind,
    InvalidSampleVisibilityQosPolicy,
    LivelinessQosPolicyKind,
    OwnershipQosPolicyKind,
    PresentationQosPolicyAccessScopeKind,
    PublisherStatus,
    ReliabilityQosPolicyKind,
    SampleStateKind,
    SubscriberStatus,
    TopicStatus,
    ViewStateKind,
    date,
    datetime,
    ddsMetamodel_DdsApplication,
    ddsMetamodel_DdsDataField,
    ddsMetamodel_DdsDataModule,
    ddsMetamodel_DdsDataReader,
    ddsMetamodel_DdsDataReaderLifecycleQos,
    ddsMetamodel_DdsDataReaderListener,
    ddsMetamodel_DdsDataReaderQosProfile,
    ddsMetamodel_DdsDataReaderStatusCondition,
    ddsMetamodel_DdsDataStructure,
    ddsMetamodel_DdsDataWriter,
    ddsMetamodel_DdsDataWriterLifecycleQos,
    ddsMetamodel_DdsDataWriterListener,
    ddsMetamodel_DdsDataWriterQosProfile,
    ddsMetamodel_DdsDataWriterStatusCondition,
    ddsMetamodel_DdsDeadlineQos,
    ddsMetamodel_DdsDestinationOrderQos,
    ddsMetamodel_DdsDomainParticipant,
    ddsMetamodel_DdsDomainParticipantListener,
    ddsMetamodel_DdsDomainParticipantQosProfile,
    ddsMetamodel_DdsDomainParticipantStatusCondition,
    ddsMetamodel_DdsDurabilityQos,
    ddsMetamodel_DdsDurabilityServiceQos,
    ddsMetamodel_DdsDuration,
    ddsMetamodel_DdsEntityFactoryQos,
    ddsMetamodel_DdsGroupDataQos,
    ddsMetamodel_DdsHistoryQos,
    ddsMetamodel_DdsHost,
    ddsMetamodel_DdsLatencyBudgetQos,
    ddsMetamodel_DdsLifespan,
    ddsMetamodel_DdsLivelinessQos,
    ddsMetamodel_DdsOwnershipQos,
    ddsMetamodel_DdsOwnershipStrengthQos,
    ddsMetamodel_DdsPartitionQos,
    ddsMetamodel_DdsPresentationQos,
    ddsMetamodel_DdsPublisher,
    ddsMetamodel_DdsPublisherListener,
    ddsMetamodel_DdsPublisherQosProfile,
    ddsMetamodel_DdsPublisherStatusCondition,
    ddsMetamodel_DdsQosProfile,
    ddsMetamodel_DdsReadCondition,
    ddsMetamodel_DdsReliabilityQos,
    ddsMetamodel_DdsResourceLimits,
    ddsMetamodel_DdsStatusCondition,
    ddsMetamodel_DdsStructuredField,
    ddsMetamodel_DdsSubscriber,
    ddsMetamodel_DdsSubscriberListener,
    ddsMetamodel_DdsSubscriberQosProfile,
    ddsMetamodel_DdsSubscriberStatusCondition,
    ddsMetamodel_DdsSystem,
    ddsMetamodel_DdsTimeBasedFilterQos,
    ddsMetamodel_DdsTopic,
    ddsMetamodel_DdsTopicDataQos,
    ddsMetamodel_DdsTopicListener,
    ddsMetamodel_DdsTopicQosProfile,
    ddsMetamodel_DdsTopicStatusCondition,
    ddsMetamodel_DdsTransportPriorityQos,
    ddsMetamodel_DdsUserDataQos,
    ddsMetamodel_DdsWaitSet,
    ddsMetamodel_GuardCondition,
    ddsMetamodel_QueryCondition,
    time,
)


def test_0():
    var_0 = python_code_.ddsMetamodel_DdsDomainParticipantListener
    var_1 = python_code_.ddsMetamodel_DdsDataReaderStatusCondition(enabled_status=var_0)
    assert isinstance(var_1, python_code_.ddsMetamodel_DdsDataReaderStatusCondition)
    var_3 = ';bD0*G/7G6DfC"\r\r~6Q'
    python_code_.ddsMetamodel_DdsDomainParticipantListener(
        name=var_3, listenedStatus=var_3
    )
    python_code_.ddsMetamodel_DdsSystem(systemName=var_3)
    var_6 = "_78x@0._|+\t28"
    var_7 = python_code_.ddsMetamodel_QueryCondition(query=var_6, queryParameters=var_0)
    assert isinstance(var_7, python_code_.ddsMetamodel_QueryCondition)
    var_12 = "E$d\rYHSbFfG*'=V0\tw5"
    var_13 = python_code_.ddsMetamodel_DdsPublisherStatusCondition(
        enabled_status=var_12
    )
    assert isinstance(var_13, python_code_.ddsMetamodel_DdsPublisherStatusCondition)


@pytest.mark.xfail(strict=True)
def test_1():
    var_1 = "_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic13"
    var_2 = python_code_.ddsMetamodel_DdsDataReaderStatusCondition(enabled_status=-1)
    assert isinstance(var_2, python_code_.ddsMetamodel_DdsDataReaderStatusCondition)
    python_code_.ddsMetamodel_DdsDataReader(
        dataReaderName=var_1,
        ddsMetamodel_DdsDataReader=var_1,
        ddsMetamodel_DdsDataReader232=var_2,
    )


def test_2():
    var_0 = "Xm(*'ql"
    var_1 = python_code_.ddsMetamodel_DdsSubscriberStatusCondition(enabled_status=var_0)
    assert isinstance(var_1, python_code_.ddsMetamodel_DdsSubscriberStatusCondition)
    python_code_.ddsMetamodel_DdsEntityFactoryQos(
        autoenable_created_entities=b'<\xcd\xa5lJ\xbd\x19\xfc"\xd4\xaby`\x15\xbb\xf3\xaa\xcc',
        ddsMetamodel_DdsEntityFactoryQos116=(False, "D"),
    )
    var_6 = repr
    python_code_.ddsMetamodel_DdsDataWriterListener(
        name=var_6, listenedStatus=var_0, ddsMetamodel_DdsDataWriterListener=var_1
    )
    var_26 = "E$d\rYHSbFfG*'=V0\tw5"
    var_27 = python_code_.ddsMetamodel_DdsPublisherStatusCondition(
        enabled_status=var_26
    )
    assert isinstance(var_27, python_code_.ddsMetamodel_DdsPublisherStatusCondition)
    var_28 = python_code_.ddsMetamodel_DdsDataWriterQosProfile()
    python_code_.ddsMetamodel_DdsReliabilityQos(
        kind=var_26,
        ddsMetamodel_DdsReliabilityQos=[-1052.43],
        ddsMetamodel_DdsReliabilityQos143=var_28,
    )


def test_3():
    var_2 = "DdsSubscriber _ddsMetamodel_DdsDataReaderLifecycleQos__ddsMetamodel_DdsDataReaderLifecycleQos110 _ddsMetamodel_GuardCondition__ddsMetamodel_GuardCondition"
    python_code_.ddsMetamodel_DdsDestinationOrderQos(kind=var_2)
    var_4 = "ddsMetamodel_DdsLatencyBudgetQos,_ddsMetamodel_DdsTransportPriorityQos__ddsMetamodel_DdsTransportPriorityQos146"
    python_code_.ddsMetamodel_GuardCondition(
        name=var_4, ddsMetamodel_GuardCondition=None
    )
    python_code_.ddsMetamodel_DdsQosProfile(profileName=var_2)
    python_code_.ddsMetamodel_DdsDomainParticipantListener(
        name=var_4, listenedStatus="\tlj\x0bJ[1QrjpwA8SbWcn"
    )
    python_code_.ddsMetamodel_DdsSystem(systemName=var_4)
    var_35 = "E$d\rYHSbFfG*'=V0\tw5"
    var_36 = python_code_.ddsMetamodel_DdsPublisherStatusCondition(
        enabled_status=var_35
    )
    assert isinstance(var_36, python_code_.ddsMetamodel_DdsPublisherStatusCondition)


def test_4():
    var_0 = "_ddsMetamodel_DdsDataWriterLifecycleQos__ddsMetamodel_DdsDataWriterLifecycleQos161.ddsMetamodel_DdsDataReaderQosProfile199._ddsMetamodel_DdsLivelinessQos__ddsMetamodel_DdsLivelinessQos.ddsMetamodel_DdsSubscriber228"
    python_code_.ddsMetamodel_DdsTopic(topicName=var_0)
    python_code_.ddsMetamodel_DdsPartitionQos(name=var_0)
    var_47 = "ddsMetamodel_DdsPublisherQosProfile,_ddsMetamodel_DdsEntityFactoryQos__ddsMetamodel_DdsEntityFactoryQos,MANUAL_BY_PARTICIPANT_LIVELINESS_QOS"
    python_code_.ddsMetamodel_DdsWaitSet(name=var_47)
    var_50 = False
    python_code_.ddsMetamodel_DdsDataReaderLifecycleQos(
        autopurge_dispose_all=var_50, enable_invalid_samples=()
    )
    var_53 = "@[8{2"
    var_63 = python_code_.ddsMetamodel_DdsTopicListener
    python_code_.ddsMetamodel_DdsDurabilityServiceQos(
        history_kind=var_0,
        history_depth=var_53,
        max_samples=True,
        max_instances=var_63,
        max_samples_per_instances=var_0,
        ddsMetamodel_DdsDurabilityServiceQos=complex(-513.32, 952.75568),
        ddsMetamodel_DdsDurabilityServiceQos84=True,
    )
    var_59 = "*4L"
    python_code_.ddsMetamodel_DdsGroupDataQos(value=var_59)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "Uk$v!w5L"
    python_code_.ddsMetamodel_GuardCondition(name=var_0)
    var_3 = complex
    var_4 = python_code_.ddsMetamodel_DdsDataReaderLifecycleQos(
        autopurge_dispose_all=None,
        enable_invalid_samples=None,
        ddsMetamodel_DdsDataReaderLifecycleQos110=complex(2874.0, 1040.76),
    )
    python_code_.ddsMetamodel_DdsDuration(
        sec=var_3, nanoSec=var_0, ddsMetamodel_DdsDuration111=var_4
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_1 = "containerDataModule"
    var_2 = python_code_.ddsMetamodel_DdsTopicQosProfile()
    python_code_.ddsMetamodel_DdsDestinationOrderQos(
        kind=var_1,
        ddsMetamodel_DdsDestinationOrderQos=var_2,
        ddsMetamodel_DdsDestinationOrderQos152=[-1635.39],
    )
    var_4 = python_code_.ddsMetamodel_DdsDataReaderLifecycleQos
    python_code_.ddsMetamodel_DdsDataReaderLifecycleQos(
        autopurge_dispose_all=var_1,
        enable_invalid_samples=var_1,
        ddsMetamodel_DdsDataReaderLifecycleQos110=var_4,
    )
    var_6 = python_code_.ddsMetamodel_DdsDataReaderStatusCondition(enabled_status=var_2)
    assert isinstance(var_6, python_code_.ddsMetamodel_DdsDataReaderStatusCondition)
    python_code_.ddsMetamodel_DdsDataReader(
        dataReaderName=var_1, ddsdatareader=var_4, ddsMetamodel_DdsDataReader232=var_6
    )


def test_7():
    var_0 = python_code_.ddsMetamodel_DdsTopicQosProfile()
    var_1 = python_code_.DomainParticipantStatus
    var_2 = 'f"y&,Y^q[}Z/+H%'
    var_3 = python_code_.ddsMetamodel_DdsDataWriterQosProfile()
    python_code_.ddsMetamodel_DdsResourceLimits(
        max_samples=var_0,
        max_instances=var_1,
        max_samples_per_instances=var_2,
        ddsMetamodel_DdsResourceLimits158=var_3,
    )
    python_code_.ddsMetamodel_DdsOwnershipStrengthQos(
        value=set(), ddsMetamodel_DdsOwnershipStrengthQos=var_3
    )
    python_code_.ddsMetamodel_DdsDurabilityServiceQos(
        history_kind=None,
        history_depth=var_2,
        max_samples=var_1,
        max_instances={
            "_ddsMetamodel_DdsStructuredField__DdsStructuredField ddsMetamodel_DdsTopicQosProfile78 _ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic13 ddsMetamodel_DdsDataReaderStatusCondition": 620.94,
            "Dtxky|@Bpw": 2689.13,
            "SLQ": False,
        },
        max_samples_per_instances=-3676.04,
        ddsMetamodel_DdsDurabilityServiceQos=[False, True],
    )


def test_8():
    var_1 = "containerDataModule"
    var_2 = python_code_.ddsMetamodel_DdsTopicQosProfile()
    python_code_.ddsMetamodel_DdsDestinationOrderQos(
        kind=var_1,
        ddsMetamodel_DdsDestinationOrderQos=var_2,
        ddsMetamodel_DdsDestinationOrderQos152=[-1635.39],
    )
    var_4 = python_code_.ddsMetamodel_DdsDataReaderLifecycleQos
    var_42 = -779
    var_45 = "_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration90"
    python_code_.ddsMetamodel_DdsDataReader(
        dataReaderName=var_45,
        DdsDataReader=complex(275.8, -1008.2),
        ddsdatareader=var_42,
    )
    var_47 = str
    python_code_.ddsMetamodel_DdsApplication(
        applicationName=var_4, ddsMetamodel_DdsApplication245=var_47
    )
    var_77 = python_code_.ddsMetamodel_DdsDataReaderListener
    python_code_.ddsMetamodel_DdsPublisherListener(
        name=var_45, listenedStatus=var_77, ddsMetamodel_DdsPublisherListener=var_2
    )
    python_code_.ddsMetamodel_DdsTopicDataQos(
        value=var_1, ddsMetamodel_DdsTopicDataQos=False
    )
    var_56 = python_code_.OwnershipQosPolicyKind.EXCLUSIVE_OWNERSHIP_QOS
    var_57 = -661
    var_58 = False
    python_code_.ddsMetamodel_DdsStructuredField(
        fieldName=var_1, maxMultiplicity=var_57, isKey=var_58
    )
    python_code_.ddsMetamodel_DdsWaitSet(
        name="ddsMetamodel_DdsWaitSet211NO_INVALID_SAMPLESDdsSubscriberDdsSubscriber",
        ddsMetamodel_DdsWaitSet=var_56,
        containingWaitset=b";?Ng\x17D>r\x83",
        DdsWaitSet=var_47,
    )
    var_63 = "_ddsMetamodel_DdsDataModule__DdsDataModule"
    var_64 = True
    var_65 = "ddsdatareader_ddsMetamodel_DdsDataWriter__ddsMetamodel_DdsDataWriter230ddsMetamodel_DdsPublisher31"
    var_66 = "rSp~x \rsh kDSp,y"
    python_code_.ddsMetamodel_DdsDurabilityServiceQos(
        history_kind=var_65,
        history_depth=None,
        max_samples=var_66,
        max_instances=var_45,
        max_samples_per_instances=var_63,
    )
    var_68 = ";!GkqX\x0b~"
    python_code_.ddsMetamodel_DdsReliabilityQos(
        kind=var_68, ddsMetamodel_DdsReliabilityQos97=var_47
    )
    python_code_.ddsMetamodel_DdsOwnershipStrengthQos(
        value="PERSISTENT_DURABILITY_QOS:_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant6:_ddsMetamodel_DdsDurabilityServiceQos__ddsMetamodel_DdsDurabilityServiceQos:ddsMetamodel_DdsSystem241"
    )
    var_71 = python_code_.ddsMetamodel_QueryCondition(
        query=var_1, queryParameters=var_64
    )
    assert isinstance(var_71, python_code_.ddsMetamodel_QueryCondition)


def test_9():
    var_0 = python_code_.ddsMetamodel_DdsDomainParticipantListener
    var_1 = python_code_.ddsMetamodel_DdsDataReaderStatusCondition(enabled_status=var_0)
    assert isinstance(var_1, python_code_.ddsMetamodel_DdsDataReaderStatusCondition)
    var_3 = ';bD0*G/7G6DfC"\r\r~6Q'
    python_code_.ddsMetamodel_DdsDomainParticipantListener(
        name=var_3, listenedStatus=var_3
    )
    python_code_.ddsMetamodel_DdsSystem(systemName=var_3)
    var_6 = '_78x"@0._|+\t28'
    var_7 = python_code_.ddsMetamodel_QueryCondition(query=var_6, queryParameters=var_0)
    assert isinstance(var_7, python_code_.ddsMetamodel_QueryCondition)
    var_8 = -1372
    python_code_.ddsMetamodel_DdsDataField(
        fieldType={}, fieldName=var_3, isKey=var_0, maxMultiplicity=var_8
    )
    var_12 = "E$d\rYHSbFfG*'=V0\tw5"
    var_13 = python_code_.ddsMetamodel_DdsPublisherStatusCondition(
        enabled_status=var_12
    )
    assert isinstance(var_13, python_code_.ddsMetamodel_DdsPublisherStatusCondition)
    var_14 = python_code_.ddsMetamodel_DdsDataWriterQosProfile()
    python_code_.ddsMetamodel_DdsReliabilityQos(
        kind=var_12,
        ddsMetamodel_DdsReliabilityQos=[-1052.43],
        ddsMetamodel_DdsReliabilityQos143=var_14,
    )


def test_10():
    var_6 = 'Sw"WEF]\ndY.N'
    var_7 = python_code_.ddsMetamodel_DdsQosProfile(profileName=set())
    var_8 = "O/1QOIjbH:YW^?"
    var_9 = python_code_.ddsMetamodel_DdsQosProfile(profileName=var_8)
    var_10 = {var_7, var_7, var_9, var_7, var_9}
    python_code_.ddsMetamodel_DdsSystem(
        systemName=var_6, ddsMetamodel_DdsSystem237=var_10
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = "Xm(*'ql"
    var_1 = python_code_.ddsMetamodel_DdsSubscriberStatusCondition(enabled_status=var_0)
    assert isinstance(var_1, python_code_.ddsMetamodel_DdsSubscriberStatusCondition)
    var_4 = python_code_.DdsQosProfile()
    python_code_.ddsMetamodel_DdsEntityFactoryQos(
        autoenable_created_entities=b'<\xcd\xa5lJ\xbd\x19\xfc"\xd4\xaby`\x15\xbb\xf3\xaa\xcc',
        ddsMetamodel_DdsEntityFactoryQos116=(False, "D"),
    )
    var_6 = repr
    python_code_.ddsMetamodel_DdsDataWriterListener(
        name=var_6, listenedStatus=var_0, ddsMetamodel_DdsDataWriterListener=var_1
    )
    var_9 = python_code_.ddsMetamodel_DdsDataModule(moduleName=var_4)
    var_10 = python_code_.ddsMetamodel_DdsDataStructure(structureName=var_0)
    var_11 = {var_10, var_10, var_10, var_10, var_10}
    var_12 = python_code_.ddsMetamodel_DdsDataModule(
        moduleName=var_0,
        containerDataModule=var_11,
        DdsDataModule=var_9,
        DdsDataModule52=var_4,
    )
    python_code_.ddsMetamodel_DdsDataStructure(
        structureName=var_0,
        ddsMetamodel_DdsDataStructure49=-3058.82,
        dataStructures=var_12,
        DdsDataStructure221=(
            859.22,
            "_ddsMetamodel_DdsDataWriterLifecycleQos__ddsMetamodel_DdsDataWriterLifecycleQos105:ddsMetamodel_DdsDataWriterLifecycleQos:ddsMetamodel_DdsPublisher",
            82,
        ),
    )


def test_12():
    var_1 = "O(q"
    var_2 = -3464
    var_3 = False
    python_code_.ddsMetamodel_DdsStructuredField(
        fieldName=var_1, maxMultiplicity=var_2, isKey=var_3
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = "_ddsMetamodel_DdsDataWriterLifecycleQos__ddsMetamodel_DdsDataWriterLifecycleQos161.ddsMetamodel_DdsDataReaderQosProfile199._ddsMetamodel_DdsLivelinessQos__ddsMetamodel_DdsLivelinessQos.ddsMetamodel_DdsSubscriber228"
    python_code_.ddsMetamodel_DdsTopic(topicName=var_0)
    var_2 = python_code_.ddsMetamodel_DdsDataWriterQosProfile()
    python_code_.ddsMetamodel_DdsPartitionQos(name=var_2)
    var_5 = "'lIu=."
    var_6 = python_code_.ddsMetamodel_DdsSubscriberListener(
        name=var_5, listenedStatus=var_5
    )
    var_7 = -779
    var_8 = python_code_.ddsMetamodel_DdsApplication(applicationName=var_5)
    var_9 = python_code_.ddsMetamodel_DdsDomainParticipant(
        domainParticipantName=var_5,
        domainId=var_7,
        ddsMetamodel_DdsDomainParticipant=var_8,
        ddsMetamodel_DdsDomainParticipant8="\x0c]:|1",
        ddsMetamodel_DdsDomainParticipant10=var_6,
    )
    var_10 = "_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration90"
    python_code_.ddsMetamodel_DdsDataReader(
        dataReaderName=var_10,
        DdsDataReader=complex(275.8, -1008.2),
        ddsdatareader=var_7,
    )
    var_12 = python_code_.ddsMetamodel_DdsPublisher
    var_13 = python_code_.ddsMetamodel_DdsSubscriberQosProfile()
    var_14 = python_code_.ddsMetamodel_DdsSubscriber(
        subscriberName=var_9,
        ddsMetamodel_DdsSubscriber20=var_13,
        DdsSubscriber={
            "P%#\rh\t@ju:'of,}nWK": True,
            "d0a9H(\n-/": False,
            "_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant8": -464.79,
        },
    )
    python_code_.ddsMetamodel_DdsDataReader(
        dataReaderName=var_12,
        ddsMetamodel_DdsDataReader26=complex(1830.2542881, 1039.243),
        ddsdatareader=var_14,
    )


def test_14():
    python_code_.ddsMetamodel_DdsQosProfile(profileName=set())


def test_15():
    var_0 = python_code_.ddsMetamodel_DdsDomainParticipantListener
    var_1 = python_code_.ddsMetamodel_DdsDataReaderStatusCondition(enabled_status=var_0)
    assert isinstance(var_1, python_code_.ddsMetamodel_DdsDataReaderStatusCondition)
    var_3 = ';bD0*G/7G6DfC"\r\r~6Q'
    python_code_.ddsMetamodel_DdsDomainParticipantListener(
        name=var_3, listenedStatus=var_3
    )
    python_code_.ddsMetamodel_DdsSystem(systemName=var_3)
    python_code_.ddsMetamodel_DdsDataStructure(structureName=var_3)


@pytest.mark.xfail(strict=True)
def test_16():
    var_0 = python_code_.OwnershipQosPolicyKind.EXCLUSIVE_OWNERSHIP_QOS
    var_1 = "9$}cmb/+_~.MbCqY5"
    var_2 = python_code_.ddsMetamodel_DdsTopicListener(name=var_0, listenedStatus=None)
    python_code_.ddsMetamodel_DdsTopic(topicName=var_1, ddsMetamodel_DdsTopic=var_2)


@pytest.mark.xfail(strict=True)
def test_17():
    var_2 = "DdsSubscriber _ddsMetamodel_DdsDataReaderLifecycleQos__ddsMetamodel_DdsDataReaderLifecycleQos110 _ddsMetamodel_GuardCondition__ddsMetamodel_GuardCondition"
    python_code_.ddsMetamodel_DdsDestinationOrderQos(kind=var_2)
    var_4 = "ddsMetamodel_DdsLatencyBudgetQos,_ddsMetamodel_DdsTransportPriorityQos__ddsMetamodel_DdsTransportPriorityQos146"
    var_5 = python_code_.ddsMetamodel_GuardCondition(
        name=var_4, ddsMetamodel_GuardCondition=None
    )
    python_code_.ddsMetamodel_DdsQosProfile(profileName=var_2)
    python_code_.ddsMetamodel_DdsTopicListener(
        name=var_5, listenedStatus=710.12, ddsMetamodel_DdsTopicListener=var_4
    )
    var_12 = lambda *args, **kwargs: []
    var_13 = "\rf_r5"
    python_code_.ddsMetamodel_DdsDataStructure(structureName=var_13)
    var_15 = " [uKY{55K='"
    python_code_.ddsMetamodel_DdsDataStructure(
        structureName=var_15, ddsMetamodel_DdsDataStructure49=var_12
    )


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = "KEEP_ALL_HISTORY_QOS-_ddsMetamodel_DdsDataStructure__DdsDataStructure-_ddsMetamodel_DdsApplication__ddsMetamodel_DdsApplication2"
    var_1 = python_code_.ddsMetamodel_DdsDomainParticipant(
        domainParticipantName=var_0, domainId=var_0
    )
    var_2 = {var_1}
    var_3 = python_code_.ddsMetamodel_DdsApplication(
        applicationName=(1569,), ddsMetamodel_DdsApplication=var_2
    )
    python_code_.ddsMetamodel_DdsWaitSet(name=(), ddsMetamodel_DdsWaitSet=var_3)


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = python_code_.ddsMetamodel_DdsLifespan()
    var_2 = python_code_.ddsMetamodel_DdsTopicQosProfile()
    var_6 = python_code_.ddsMetamodel_DdsDataReaderStatusCondition(enabled_status=var_2)
    assert isinstance(var_6, python_code_.ddsMetamodel_DdsDataReaderStatusCondition)
    var_14 = "ddsMetamodel_DdsPublisherQos~Profile,_ddsMetamodel_DdsEntityFactoryQos__ddsMetamodel_DdsEntityFactoryQos,MANUAL_BY_PARTICIPANT_LIVELINESS_QOS"
    var_15 = python_code_.ddsMetamodel_DdsWaitSet(
        name=var_14, ddsMetamodel_DdsWaitSet214={2839}
    )
    var_19 = False
    python_code_.ddsMetamodel_DdsDataReaderLifecycleQos(
        autopurge_dispose_all=var_19, enable_invalid_samples=()
    )
    python_code_.ddsMetamodel_DdsApplication(
        applicationName=var_0,
        ddsMetamodel_DdsApplication=384.89,
        ddsMetamodel_DdsApplication2=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = python_code_.ddsMetamodel_DdsLifespan()
    var_2 = python_code_.ddsMetamodel_DdsTopicQosProfile()
    var_6 = python_code_.ddsMetamodel_DdsDataReaderStatusCondition(enabled_status=var_2)
    assert isinstance(var_6, python_code_.ddsMetamodel_DdsDataReaderStatusCondition)
    var_14 = "ddsMetamodel_DdsPublisherQosProfile,_ddsMetamodel_DdsEntityFactoryQos__ddsMetamodel_DdsEntityFactoryQos,MANUAL_BY_PARTICIPANT_LIVELINESS_QOS"
    var_15 = python_code_.ddsMetamodel_DdsWaitSet(name=var_14)
    var_19 = False
    python_code_.ddsMetamodel_DdsDataReaderLifecycleQos(
        autopurge_dispose_all=var_19, enable_invalid_samples=()
    )
    python_code_.ddsMetamodel_DdsApplication(
        applicationName=var_0,
        ddsMetamodel_DdsApplication=384.89,
        ddsMetamodel_DdsApplication2=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = "_ddsMetamodel_DdsDataWriterLifecycleQos__ddsMetamodel_DdsDataWriterLifecycleQos161.ddsMetamodel_DdsDataReaderQosProfile199._ddsMetamodel_DdsLivelinessQos__ddsMetamodel_DdsLivelinessQos.ddsMetamodel_DdsSubscriber228"
    python_code_.ddsMetamodel_DdsTopic(topicName=var_0)
    var_2 = python_code_.ddsMetamodel_DdsDataWriterQosProfile()
    python_code_.ddsMetamodel_DdsPartitionQos(name=var_0)
    var_47 = "ddsMetamodel_DdsPublisherQosProfile,_ddsMetamodel_DdsEntityFactoryQos__ddsMetamodel_DdsEntityFactoryQos,MANUAL_BY_PARTICIPANT_LIVELINESS_QOS"
    python_code_.ddsMetamodel_DdsWaitSet(name=var_47)
    var_50 = False
    python_code_.ddsMetamodel_DdsDataReaderLifecycleQos(
        autopurge_dispose_all=var_50, enable_invalid_samples=()
    )
    var_53 = "@[8{2"
    var_63 = python_code_.ddsMetamodel_DdsTopicListener
    python_code_.ddsMetamodel_DdsDurabilityServiceQos(
        history_kind=var_0,
        history_depth=var_53,
        max_samples=True,
        max_instances=var_63,
        max_samples_per_instances=var_0,
        ddsMetamodel_DdsDurabilityServiceQos=complex(-513.32, 952.75568),
        ddsMetamodel_DdsDurabilityServiceQos84=True,
    )
    var_59 = "*4L"
    python_code_.ddsMetamodel_DdsGroupDataQos(value=var_59)
    var_65 = "_ddsMetamodel_DdsDataStructure__ddsMetamodel_DdsDataStructure49"
    var_66 = 3359
    python_code_.ddsMetamodel_DdsDataField(
        fieldType=var_63,
        fieldName=var_65,
        isKey=(
            "_ddsMetamodel_DdsGroupDataQos__ddsMetamodel_DdsGroupDataQos164 _ddsMetamodel_DdsPresentationQos__ddsMetamodel_DdsPresentationQos170",
        ),
        maxMultiplicity=var_66,
        ddsMetamodel_DdsDataField=var_2,
    )
    python_code_.ddsMetamodel_DdsDataModule(moduleName=True)
    var_72 = python_code_.ddsMetamodel_DdsDataStructure(structureName=var_53)
    python_code_.ddsMetamodel_DdsStructuredField(
        fieldName=var_65,
        maxMultiplicity=var_66,
        isKey=var_50,
        DdsStructuredField=var_63,
        structuredFields=var_72,
    )
