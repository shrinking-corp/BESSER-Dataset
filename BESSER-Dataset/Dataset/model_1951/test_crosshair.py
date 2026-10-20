from python_code import model_ExperimentState

def test_model_ExperimentState___init__():
    assert model_ExperimentState.__init__(model_ExperimentState('', '', model_ExperimentState=set(), model_ExperimentState20=set()), '', '', model_ExperimentState=set(), model_ExperimentState20=set()) == None


from python_code import model_ExternalDomainModel

def test_model_ExternalDomainModel___init__():
    assert model_ExternalDomainModel.__init__(model_ExternalDomainModel(''), '') == None


from python_code import model_ISynchable

def test_model_ISynchable___init__():
    assert model_ISynchable.__init__(model_ISynchable(''), '') == None


from python_code import model_StringToStringMap

def test_model_StringToStringMap___init__():
    assert model_StringToStringMap.__init__(model_StringToStringMap('', '\x00'), '\x00\x00', '') == None


from python_code import datasources_model_GeppettoLibrary
from python_code import model_datasources_DataSourceLibraryConfiguration

def test_model_datasources_DataSourceLibraryConfiguration___init__():
    assert model_datasources_DataSourceLibraryConfiguration.__init__(model_datasources_DataSourceLibraryConfiguration('', '\x00', model_datasources_DataSourceLibraryConfiguration=datasources_model_GeppettoLibrary()), '\x00\x00', '', model_datasources_DataSourceLibraryConfiguration=datasources_model_GeppettoLibrary()) == None


from python_code import Type
from python_code import model_datasources_Query

def test_model_datasources_Query___init__():
    assert model_datasources_Query.__init__(model_datasources_Query('', '', model_datasources_Query=set(), model_datasources_Query152=Type()), '', '', model_datasources_Query=set(), model_datasources_Query152=Type()) == None


from python_code import model_datasources_QueryResult
from python_code import model_datasources_QueryResults

def test_model_datasources_QueryResult___init__():
    assert model_datasources_QueryResult.__init__(model_datasources_QueryResult('', AQueryResult=model_datasources_QueryResults('', '', model_datasources_QueryResults=set())), '', AQueryResult=model_datasources_QueryResults('', '', model_datasources_QueryResults=set())) == None


from python_code import model_datasources_QueryResults

def test_model_datasources_QueryResults___init__():
    assert model_datasources_QueryResults.__init__(model_datasources_QueryResults('\x00\x00', '', model_datasources_QueryResults=set()), '', '', model_datasources_QueryResults=set()) == None

def test_model_datasources_QueryResults_getValue():
    assert model_datasources_QueryResults.getValue(model_datasources_QueryResults('', '\x00', model_datasources_QueryResults=set()), '', '') == None


from python_code import model_datasources_RunnableQuery

def test_model_datasources_RunnableQuery___init__():
    assert model_datasources_RunnableQuery.__init__(model_datasources_RunnableQuery('', '', '\x00\x00'), '', '', '') == None


from python_code import model_datasources_QueryResults
from python_code import model_datasources_SerializableQueryResult

def test_model_datasources_SerializableQueryResult___init__():
    assert model_datasources_SerializableQueryResult.__init__(model_datasources_SerializableQueryResult('', AQueryResult=model_datasources_QueryResults('', '', model_datasources_QueryResults=set())), '', AQueryResult=model_datasources_QueryResults('', '', model_datasources_QueryResults=set())) == None

