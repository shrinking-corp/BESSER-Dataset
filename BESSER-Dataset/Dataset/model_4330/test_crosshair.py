from python_code import smm_Base1MeasureRelationship
from python_code import smm_Base2MeasureRelationship
from python_code import smm_BinaryMeasure

def test_smm_BinaryMeasure___init__():
    assert smm_BinaryMeasure.__init__(smm_BinaryMeasure('', BinaryMeasure=smm_Base1MeasureRelationship(), BinaryMeasure11=smm_Base2MeasureRelationship(), from_=smm_Base1MeasureRelationship(), from_22=smm_Base2MeasureRelationship()), '', BinaryMeasure=smm_Base1MeasureRelationship(), BinaryMeasure11=smm_Base2MeasureRelationship(), from_=smm_Base1MeasureRelationship(), from_22=smm_Base2MeasureRelationship()) == None


from python_code import smm_Base1MeasurementRelationship
from python_code import smm_Base2MeasurementRelationship
from python_code import smm_BinaryMeasurement

def test_smm_BinaryMeasurement___init__():
    assert smm_BinaryMeasurement.__init__(smm_BinaryMeasurement(True, BinaryMeasurement7=smm_Base2MeasurementRelationship(), BinaryMeasurement=smm_Base1MeasurementRelationship(), from_24=smm_Base1MeasurementRelationship(), from_26=smm_Base2MeasurementRelationship()), False, BinaryMeasurement7=smm_Base2MeasurementRelationship(), BinaryMeasurement=smm_Base1MeasurementRelationship(), from_24=smm_Base1MeasurementRelationship(), from_26=smm_Base2MeasurementRelationship()) == None


from python_code import smm_BaseMeasureRelationship
from python_code import smm_CollectiveMeasure

def test_smm_CollectiveMeasure___init__():
    assert smm_CollectiveMeasure.__init__(smm_CollectiveMeasure('', from_35=set(), CollectiveMeasure=smm_BaseMeasureRelationship()), '', from_35=set(), CollectiveMeasure=smm_BaseMeasureRelationship()) == None


from python_code import smm_BaseMeasurementRelationship
from python_code import smm_CollectiveMeasurement

def test_smm_CollectiveMeasurement___init__():
    assert smm_CollectiveMeasurement.__init__(smm_CollectiveMeasurement('\x00\x00', False, CollectiveMeasurement=smm_BaseMeasurementRelationship(), from_37=set()), '', True, CollectiveMeasurement=smm_BaseMeasurementRelationship(), from_37=set()) == None


from python_code import smm_Base1MeasureRelationship
from python_code import smm_Base2MeasureRelationship
from python_code import smm_BaseMeasureRelationship
from python_code import smm_DimensionalMeasure
from python_code import smm_RankingMeasureRelationship
from python_code import smm_RescaleMeasureRelationship

def test_smm_DimensionalMeasure___init__():
    assert smm_DimensionalMeasure.__init__(smm_DimensionalMeasure('', DimensionalMeasure=smm_Base1MeasureRelationship(), DimensionalMeasure13=smm_Base2MeasureRelationship(), to41=set(), DimensionalMeasure19=smm_BaseMeasureRelationship(), to=set(), to44=set(), from_47=smm_RescaleMeasureRelationship(), to49=set(), DimensionalMeasure161=smm_RankingMeasureRelationship(), DimensionalMeasure192=smm_RescaleMeasureRelationship()), '', DimensionalMeasure=smm_Base1MeasureRelationship(), DimensionalMeasure13=smm_Base2MeasureRelationship(), to41=set(), DimensionalMeasure19=smm_BaseMeasureRelationship(), to=set(), to44=set(), from_47=smm_RescaleMeasureRelationship(), to49=set(), DimensionalMeasure161=smm_RankingMeasureRelationship(), DimensionalMeasure192=smm_RescaleMeasureRelationship()) == None


from python_code import smm_MeasureLibrary
from python_code import smm_SmmModel

def test_smm_MeasureLibrary___init__():
    assert smm_MeasureLibrary.__init__(smm_MeasureLibrary(smm_MeasureLibrary218=smm_SmmModel(), smm_MeasureLibrary=set(), smm_MeasureLibrary116=set()), smm_MeasureLibrary218=smm_SmmModel(), smm_MeasureLibrary=set(), smm_MeasureLibrary116=set()) == None

def test_smm_MeasureLibrary_getOperations():
    assert smm_MeasureLibrary.getOperations(smm_MeasureLibrary(smm_MeasureLibrary218=smm_SmmModel(), smm_MeasureLibrary=set(), smm_MeasureLibrary116=set())) == None

def test_smm_MeasureLibrary_getOclOperations():
    assert smm_MeasureLibrary.getOclOperations(smm_MeasureLibrary(smm_MeasureLibrary218=smm_SmmModel(), smm_MeasureLibrary=set(), smm_MeasureLibrary116=set())) == None


from python_code import smm_OCLOperation

def test_smm_OCLOperation___init__():
    assert smm_OCLOperation.__init__(smm_OCLOperation('', '\x00'), '\x00\x00', '') == None


from python_code import smm_Ranking
from python_code import smm_RankingInterval

def test_smm_RankingInterval___init__():
    assert smm_RankingInterval.__init__(smm_RankingInterval(0.0, False, 0.0, False, '', RankingInterval=smm_Ranking(), interval=smm_Ranking()), 0.0, False, 0.0, True, '', RankingInterval=smm_Ranking(), interval=smm_Ranking()) == None


from python_code import smm_RescaleMeasureRelationship
from python_code import smm_RescaledMeasure

def test_smm_RescaledMeasure___init__():
    assert smm_RescaledMeasure.__init__(smm_RescaledMeasure('', to188=set(), RescaledMeasure=smm_RescaleMeasureRelationship()), '', to188=set(), RescaledMeasure=smm_RescaleMeasureRelationship()) == None


from python_code import smm_RescaleMeasurementRelationship
from python_code import smm_RescaledMeasurement

def test_smm_RescaledMeasurement___init__():
    assert smm_RescaledMeasurement.__init__(smm_RescaledMeasurement(False, to194=set(), RescaledMeasurement=smm_RescaleMeasurementRelationship()), False, to194=set(), RescaledMeasurement=smm_RescaleMeasurementRelationship()) == None

