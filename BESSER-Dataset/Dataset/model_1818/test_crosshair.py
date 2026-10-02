from enum import Enum
from python_code import DataReaderStatus
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DataReaderStatus.SAMPLE_LOST_STATUS, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DataReaderStatus.SAMPLE_LOST_STATUS, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DataReaderStatus.SAMPLE_LOST_STATUS, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DataReaderStatus.SAMPLE_REJECTED_STATUS, '')

def test_Enum___new___2():
    assert Enum.__new__(DataReaderStatus.DATA_AVAILABLE_STATUS, 'SAMPLE_LOST_STATUS') == DataReaderStatus.SAMPLE_LOST_STATUS

from enum import Enum
from python_code import DataWriterStatus
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DataWriterStatus.LIVELINESS_LOST_STATUS, '\x00', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DataWriterStatus.LIVELINESS_LOST_STATUS, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DataWriterStatus.LIVELINESS_LOST_STATUS, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DataWriterStatus.LIVELINESS_LOST_STATUS, 0)

def test_Enum___new___2():
    assert Enum.__new__(DataWriterStatus.LIVELINESS_LOST_STATUS, 'LIVELINESS_LOST_STATUS') == DataWriterStatus.LIVELINESS_LOST_STATUS

from enum import Enum
from python_code import DestinationOrderQosPolicyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DestinationOrderQosPolicyKind.BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DestinationOrderQosPolicyKind.BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DestinationOrderQosPolicyKind.BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DestinationOrderQosPolicyKind.BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS, 0)

def test_Enum___new___2():
    assert Enum.__new__(DestinationOrderQosPolicyKind.BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS, 'BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS') == DestinationOrderQosPolicyKind.BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS

from enum import Enum
from python_code import DomainParticipantStatus
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DomainParticipantStatus.SAMPLE_LOST_STATUS, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DomainParticipantStatus.LIVELINESS_LOST_STATUS, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DomainParticipantStatus.SAMPLE_LOST_STATUS, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DomainParticipantStatus.INCONSISTENT_TOPIC_STATUS, '')

def test_Enum___new___2():
    assert Enum.__new__(DomainParticipantStatus.DATA_ON_READERS_STATUS, 'DATA_AVAILABLE_STATUS') == DomainParticipantStatus.DATA_AVAILABLE_STATUS

from enum import Enum
from python_code import DurabilityQosPolicyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DurabilityQosPolicyKind.TRANSIENT_DURABILITY_QOS, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DurabilityQosPolicyKind.VOLATILE_DURABILITY_QOS, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DurabilityQosPolicyKind.TRANSIENT_DURABILITY_QOS, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DurabilityQosPolicyKind.VOLATILE_DURABILITY_QOS, 0)

def test_Enum___new___2():
    assert Enum.__new__(DurabilityQosPolicyKind.VOLATILE_DURABILITY_QOS, 'VOLATILE_DURABILITY_QOS') == DurabilityQosPolicyKind.VOLATILE_DURABILITY_QOS

from enum import Enum
from python_code import HistoryQosPolicyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(HistoryQosPolicyKind.KEEP_ALL_HISTORY_QOS, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(HistoryQosPolicyKind.KEEP_ALL_HISTORY_QOS, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(HistoryQosPolicyKind.KEEP_LAST_HISTORY_QOS, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(HistoryQosPolicyKind.KEEP_ALL_HISTORY_QOS, 0)

def test_Enum___new___2():
    assert Enum.__new__(HistoryQosPolicyKind.KEEP_ALL_HISTORY_QOS, 'KEEP_ALL_HISTORY_QOS') == HistoryQosPolicyKind.KEEP_ALL_HISTORY_QOS

from enum import Enum
from python_code import InstanceStateKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InstanceStateKind.ALIVE_INSTANCE_STATE, '\x00', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InstanceStateKind.ANY_INSTANCE_STATE, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InstanceStateKind.ANY_INSTANCE_STATE, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InstanceStateKind.ANY_INSTANCE_STATE, 0)

def test_Enum___new___2():
    assert Enum.__new__(InstanceStateKind.ANY_INSTANCE_STATE, 'ANY_INSTANCE_STATE') == InstanceStateKind.ANY_INSTANCE_STATE

from enum import Enum
from python_code import InvalidSampleVisibilityQosPolicy
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InvalidSampleVisibilityQosPolicy.NO_INVALID_SAMPLES, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InvalidSampleVisibilityQosPolicy.NO_INVALID_SAMPLES, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InvalidSampleVisibilityQosPolicy.NO_INVALID_SAMPLES, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InvalidSampleVisibilityQosPolicy.NO_INVALID_SAMPLES, 0)

def test_Enum___new___2():
    assert Enum.__new__(InvalidSampleVisibilityQosPolicy.NO_INVALID_SAMPLES, 'NO_INVALID_SAMPLES') == InvalidSampleVisibilityQosPolicy.NO_INVALID_SAMPLES

from enum import Enum
from python_code import LivelinessQosPolicyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LivelinessQosPolicyKind.MANUAL_LIVELINESS_QOS, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LivelinessQosPolicyKind.MANUAL_LIVELINESS_QOS, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LivelinessQosPolicyKind.MANUAL_LIVELINESS_QOS, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LivelinessQosPolicyKind.MANUAL_LIVELINESS_QOS, 0)

def test_Enum___new___2():
    assert Enum.__new__(LivelinessQosPolicyKind.MANUAL_LIVELINESS_QOS, 'MANUAL_LIVELINESS_QOS') == LivelinessQosPolicyKind.MANUAL_LIVELINESS_QOS

from enum import Enum
from python_code import OwnershipQosPolicyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(OwnershipQosPolicyKind.SHARED_OWNERSHIP_QOS, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(OwnershipQosPolicyKind.SHARED_OWNERSHIP_QOS, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(OwnershipQosPolicyKind.SHARED_OWNERSHIP_QOS, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(OwnershipQosPolicyKind.SHARED_OWNERSHIP_QOS, 0)

def test_Enum___new___2():
    assert Enum.__new__(OwnershipQosPolicyKind.SHARED_OWNERSHIP_QOS, 'SHARED_OWNERSHIP_QOS') == OwnershipQosPolicyKind.SHARED_OWNERSHIP_QOS

from enum import Enum
from python_code import PresentationQosPolicyAccessScopeKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PresentationQosPolicyAccessScopeKind.GROUP_PRESENTATION_QOS, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PresentationQosPolicyAccessScopeKind.GROUP_PRESENTATION_QOS, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PresentationQosPolicyAccessScopeKind.GROUP_PRESENTATION_QOS, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PresentationQosPolicyAccessScopeKind.GROUP_PRESENTATION_QOS, 0)

def test_Enum___new___2():
    assert Enum.__new__(PresentationQosPolicyAccessScopeKind.GROUP_PRESENTATION_QOS, 'GROUP_PRESENTATION_QOS') == PresentationQosPolicyAccessScopeKind.GROUP_PRESENTATION_QOS

from enum import Enum
from python_code import PublisherStatus
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PublisherStatus.LIVELINESS_LOST_STATUS, '\x00', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PublisherStatus.LIVELINESS_LOST_STATUS, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PublisherStatus.LIVELINESS_LOST_STATUS, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PublisherStatus.LIVELINESS_LOST_STATUS, 0)

def test_Enum___new___2():
    assert Enum.__new__(PublisherStatus.LIVELINESS_LOST_STATUS, 'LIVELINESS_LOST_STATUS') == PublisherStatus.LIVELINESS_LOST_STATUS

from enum import Enum
from python_code import ReliabilityQosPolicyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ReliabilityQosPolicyKind.RELIABLE_RELIABILITY_QOS, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ReliabilityQosPolicyKind.RELIABLE_RELIABILITY_QOS, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ReliabilityQosPolicyKind.RELIABLE_RELIABILITY_QOS, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ReliabilityQosPolicyKind.RELIABLE_RELIABILITY_QOS, 0)

def test_Enum___new___2():
    assert Enum.__new__(ReliabilityQosPolicyKind.RELIABLE_RELIABILITY_QOS, 'RELIABLE_RELIABILITY_QOS') == ReliabilityQosPolicyKind.RELIABLE_RELIABILITY_QOS

from enum import Enum
from python_code import SampleStateKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SampleStateKind.READ_SAMPLE_STATE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SampleStateKind.READ_SAMPLE_STATE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SampleStateKind.READ_SAMPLE_STATE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SampleStateKind.READ_SAMPLE_STATE, 0)

def test_Enum___new___2():
    assert Enum.__new__(SampleStateKind.READ_SAMPLE_STATE, 'READ_SAMPLE_STATE') == SampleStateKind.READ_SAMPLE_STATE

from enum import Enum
from python_code import SubscriberStatus
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SubscriberStatus.SAMPLE_LOST_STATUS, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SubscriberStatus.SAMPLE_LOST_STATUS, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SubscriberStatus.SAMPLE_LOST_STATUS, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SubscriberStatus.DATA_AVAILABLE_STATUS, '')

def test_Enum___new___2():
    assert Enum.__new__(SubscriberStatus.SAMPLE_LOST_STATUS, 'DATA_AVAILABLE_STATUS') == SubscriberStatus.DATA_AVAILABLE_STATUS

from enum import Enum
from python_code import TopicStatus
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TopicStatus.INCONSISTENT_TOPIC_STATUS, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TopicStatus.INCONSISTENT_TOPIC_STATUS, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TopicStatus.INCONSISTENT_TOPIC_STATUS, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TopicStatus.INCONSISTENT_TOPIC_STATUS, 0)

def test_Enum___new___2():
    assert Enum.__new__(TopicStatus.INCONSISTENT_TOPIC_STATUS, 'INCONSISTENT_TOPIC_STATUS') == TopicStatus.INCONSISTENT_TOPIC_STATUS

from enum import Enum
from python_code import ViewStateKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ViewStateKind.ANY_VIEW_STATE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ViewStateKind.NEW_VIEW_STATE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ViewStateKind.NEW_VIEW_STATE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ViewStateKind.ANY_VIEW_STATE, 0)

def test_Enum___new___2():
    assert Enum.__new__(ViewStateKind.ANY_VIEW_STATE, 'ANY_VIEW_STATE') == ViewStateKind.ANY_VIEW_STATE

from python_code import ddsMetamodel_DdsDataReaderQosProfile
from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsDestinationOrderQos
from python_code import ddsMetamodel_DdsTopicQosProfile

def test_ddsMetamodel_DdsDestinationOrderQos___init__():
    assert ddsMetamodel_DdsDestinationOrderQos.__init__(ddsMetamodel_DdsDestinationOrderQos('', ddsMetamodel_DdsDestinationOrderQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsDestinationOrderQos200=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsDestinationOrderQos152=ddsMetamodel_DdsDataWriterQosProfile()), '', ddsMetamodel_DdsDestinationOrderQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsDestinationOrderQos200=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsDestinationOrderQos152=ddsMetamodel_DdsDataWriterQosProfile()) == None

from python_code import ddsMetamodel_DdsDataReaderQosProfile
from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsDurabilityQos
from python_code import ddsMetamodel_DdsTopicQosProfile

def test_ddsMetamodel_DdsDurabilityQos___init__():
    assert ddsMetamodel_DdsDurabilityQos.__init__(ddsMetamodel_DdsDurabilityQos('', ddsMetamodel_DdsDurabilityQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsDurabilityQos126=ddsMetamodel_DdsDataWriterQosProfile(), ddsMetamodel_DdsDurabilityQos179=ddsMetamodel_DdsDataReaderQosProfile()), '', ddsMetamodel_DdsDurabilityQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsDurabilityQos126=ddsMetamodel_DdsDataWriterQosProfile(), ddsMetamodel_DdsDurabilityQos179=ddsMetamodel_DdsDataReaderQosProfile()) == None

from python_code import ddsMetamodel_DdsDomainParticipantQosProfile
from python_code import ddsMetamodel_DdsEntityFactoryQos
from python_code import ddsMetamodel_DdsPublisherQosProfile
from python_code import ddsMetamodel_DdsSubscriberQosProfile

def test_ddsMetamodel_DdsEntityFactoryQos___init__():
    assert ddsMetamodel_DdsEntityFactoryQos.__init__(ddsMetamodel_DdsEntityFactoryQos(True, ddsMetamodel_DdsEntityFactoryQos=ddsMetamodel_DdsDomainParticipantQosProfile(), ddsMetamodel_DdsEntityFactoryQos116=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsEntityFactoryQos167=ddsMetamodel_DdsSubscriberQosProfile()), False, ddsMetamodel_DdsEntityFactoryQos=ddsMetamodel_DdsDomainParticipantQosProfile(), ddsMetamodel_DdsEntityFactoryQos116=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsEntityFactoryQos167=ddsMetamodel_DdsSubscriberQosProfile()) == None

from python_code import ddsMetamodel_DdsGroupDataQos
from python_code import ddsMetamodel_DdsPublisherQosProfile
from python_code import ddsMetamodel_DdsSubscriberQosProfile

def test_ddsMetamodel_DdsGroupDataQos___init__():
    assert ddsMetamodel_DdsGroupDataQos.__init__(ddsMetamodel_DdsGroupDataQos('', ddsMetamodel_DdsGroupDataQos=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsGroupDataQos164=ddsMetamodel_DdsSubscriberQosProfile()), '', ddsMetamodel_DdsGroupDataQos=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsGroupDataQos164=ddsMetamodel_DdsSubscriberQosProfile()) == None

from python_code import ddsMetamodel_DdsDataReaderQosProfile
from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsHistoryQos
from python_code import ddsMetamodel_DdsTopicQosProfile

def test_ddsMetamodel_DdsHistoryQos___init__():
    assert ddsMetamodel_DdsHistoryQos.__init__(ddsMetamodel_DdsHistoryQos('', '\x00', ddsMetamodel_DdsHistoryQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsHistoryQos203=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsHistoryQos155=ddsMetamodel_DdsDataWriterQosProfile()), '\x00\x00', '', ddsMetamodel_DdsHistoryQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsHistoryQos203=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsHistoryQos155=ddsMetamodel_DdsDataWriterQosProfile()) == None

from python_code import ddsMetamodel_DdsDataReaderQosProfile
from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsOwnershipQos
from python_code import ddsMetamodel_DdsTopicQosProfile

def test_ddsMetamodel_DdsOwnershipQos___init__():
    assert ddsMetamodel_DdsOwnershipQos.__init__(ddsMetamodel_DdsOwnershipQos('', ddsMetamodel_DdsOwnershipQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsOwnershipQos191=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsOwnershipQos135=ddsMetamodel_DdsDataWriterQosProfile()), '', ddsMetamodel_DdsOwnershipQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsOwnershipQos191=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsOwnershipQos135=ddsMetamodel_DdsDataWriterQosProfile()) == None

from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsOwnershipStrengthQos

def test_ddsMetamodel_DdsOwnershipStrengthQos___init__():
    assert ddsMetamodel_DdsOwnershipStrengthQos.__init__(ddsMetamodel_DdsOwnershipStrengthQos('', ddsMetamodel_DdsOwnershipStrengthQos=ddsMetamodel_DdsDataWriterQosProfile()), '', ddsMetamodel_DdsOwnershipStrengthQos=ddsMetamodel_DdsDataWriterQosProfile()) == None

from python_code import ddsMetamodel_DdsPartitionQos
from python_code import ddsMetamodel_DdsPublisherQosProfile
from python_code import ddsMetamodel_DdsSubscriberQosProfile

def test_ddsMetamodel_DdsPartitionQos___init__():
    assert ddsMetamodel_DdsPartitionQos.__init__(ddsMetamodel_DdsPartitionQos('', ddsMetamodel_DdsPartitionQos=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsPartitionQos173=ddsMetamodel_DdsSubscriberQosProfile()), '', ddsMetamodel_DdsPartitionQos=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsPartitionQos173=ddsMetamodel_DdsSubscriberQosProfile()) == None

from python_code import ddsMetamodel_DdsPresentationQos
from python_code import ddsMetamodel_DdsPublisherQosProfile
from python_code import ddsMetamodel_DdsSubscriberQosProfile

def test_ddsMetamodel_DdsPresentationQos___init__():
    assert ddsMetamodel_DdsPresentationQos.__init__(ddsMetamodel_DdsPresentationQos('', False, False, ddsMetamodel_DdsPresentationQos=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsPresentationQos170=ddsMetamodel_DdsSubscriberQosProfile()), '\x00', False, False, ddsMetamodel_DdsPresentationQos=ddsMetamodel_DdsPublisherQosProfile(), ddsMetamodel_DdsPresentationQos170=ddsMetamodel_DdsSubscriberQosProfile()) == None

from python_code import ddsMetamodel_DdsDataReaderQosProfile
from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsResourceLimits
from python_code import ddsMetamodel_DdsTopicQosProfile

def test_ddsMetamodel_DdsResourceLimits___init__():
    assert ddsMetamodel_DdsResourceLimits.__init__(ddsMetamodel_DdsResourceLimits('', '', '\x00\x00', ddsMetamodel_DdsResourceLimits=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsResourceLimits206=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsResourceLimits158=ddsMetamodel_DdsDataWriterQosProfile()), '', '', '', ddsMetamodel_DdsResourceLimits=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsResourceLimits206=ddsMetamodel_DdsDataReaderQosProfile(), ddsMetamodel_DdsResourceLimits158=ddsMetamodel_DdsDataWriterQosProfile()) == None

from python_code import ddsMetamodel_DdsTopicDataQos
from python_code import ddsMetamodel_DdsTopicQosProfile

def test_ddsMetamodel_DdsTopicDataQos___init__():
    assert ddsMetamodel_DdsTopicDataQos.__init__(ddsMetamodel_DdsTopicDataQos('', ddsMetamodel_DdsTopicDataQos=ddsMetamodel_DdsTopicQosProfile()), '', ddsMetamodel_DdsTopicDataQos=ddsMetamodel_DdsTopicQosProfile()) == None

from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsTopicQosProfile
from python_code import ddsMetamodel_DdsTransportPriorityQos

def test_ddsMetamodel_DdsTransportPriorityQos___init__():
    assert ddsMetamodel_DdsTransportPriorityQos.__init__(ddsMetamodel_DdsTransportPriorityQos('', ddsMetamodel_DdsTransportPriorityQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsTransportPriorityQos146=ddsMetamodel_DdsDataWriterQosProfile()), '', ddsMetamodel_DdsTransportPriorityQos=ddsMetamodel_DdsTopicQosProfile(), ddsMetamodel_DdsTransportPriorityQos146=ddsMetamodel_DdsDataWriterQosProfile()) == None

from python_code import ddsMetamodel_DdsDataReaderQosProfile
from python_code import ddsMetamodel_DdsDataWriterQosProfile
from python_code import ddsMetamodel_DdsDomainParticipantQosProfile
from python_code import ddsMetamodel_DdsUserDataQos

def test_ddsMetamodel_DdsUserDataQos___init__():
    assert ddsMetamodel_DdsUserDataQos.__init__(ddsMetamodel_DdsUserDataQos('', ddsMetamodel_DdsUserDataQos=ddsMetamodel_DdsDomainParticipantQosProfile(), ddsMetamodel_DdsUserDataQos123=ddsMetamodel_DdsDataWriterQosProfile(), ddsMetamodel_DdsUserDataQos176=ddsMetamodel_DdsDataReaderQosProfile()), '', ddsMetamodel_DdsUserDataQos=ddsMetamodel_DdsDomainParticipantQosProfile(), ddsMetamodel_DdsUserDataQos123=ddsMetamodel_DdsDataWriterQosProfile(), ddsMetamodel_DdsUserDataQos176=ddsMetamodel_DdsDataReaderQosProfile()) == None

from python_code import ddsMetamodel_QueryCondition

def test_ddsMetamodel_QueryCondition___init__():
    assert ddsMetamodel_QueryCondition.__init__(ddsMetamodel_QueryCondition('', '\x00'), '\x00\x00', '') == None
