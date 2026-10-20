from python_code import smm_Base1MeasureRelationship
from python_code import smm_Base2MeasureRelationship
from python_code import smm_BinaryMeasure

def test_smm_BinaryMeasure___init__():
    assert smm_BinaryMeasure.__init__(smm_BinaryMeasure('', from_=smm_Base1MeasureRelationship(), from_20=smm_Base2MeasureRelationship(), BinaryMeasure=smm_Base1MeasureRelationship(), BinaryMeasure5=smm_Base2MeasureRelationship()), '', from_=smm_Base1MeasureRelationship(), from_20=smm_Base2MeasureRelationship(), BinaryMeasure=smm_Base1MeasureRelationship(), BinaryMeasure5=smm_Base2MeasureRelationship()) == None


from python_code import smm_Base1MeasurementRelationship
from python_code import smm_Base2MeasurementRelationship
from python_code import smm_BinaryMeasurement

def test_smm_BinaryMeasurement___init__():
    assert smm_BinaryMeasurement.__init__(smm_BinaryMeasurement('', from_22=smm_Base1MeasurementRelationship(), from_24=smm_Base2MeasurementRelationship(), BinaryMeasurement=smm_Base1MeasurementRelationship(), BinaryMeasurement9=smm_Base2MeasurementRelationship()), '', from_22=smm_Base1MeasurementRelationship(), from_24=smm_Base2MeasurementRelationship(), BinaryMeasurement=smm_Base1MeasurementRelationship(), BinaryMeasurement9=smm_Base2MeasurementRelationship()) == None


from python_code import smm_BaseMeasureRelationship
from python_code import smm_CollectiveMeasure

def test_smm_CollectiveMeasure___init__():
    assert smm_CollectiveMeasure.__init__(smm_CollectiveMeasure('', from_31=set(), CollectiveMeasure=smm_BaseMeasureRelationship()), '', from_31=set(), CollectiveMeasure=smm_BaseMeasureRelationship()) == None


from python_code import smm_BaseMeasurementRelationship
from python_code import smm_CollectiveMeasurement

def test_smm_CollectiveMeasurement___init__():
    assert smm_CollectiveMeasurement.__init__(smm_CollectiveMeasurement('\x00\x00', '', from_33=set(), CollectiveMeasurement=smm_BaseMeasurementRelationship()), '', '', from_33=set(), CollectiveMeasurement=smm_BaseMeasurementRelationship()) == None


from python_code import smm_Base1MeasureRelationship
from python_code import smm_Base2MeasureRelationship
from python_code import smm_BaseMeasureRelationship
from python_code import smm_DimensionalMeasure
from python_code import smm_RankingMeasureRelationship
from python_code import smm_RescaleMeasureRelationship

def test_smm_DimensionalMeasure___init__():
    assert smm_DimensionalMeasure.__init__(smm_DimensionalMeasure('\x00', DimensionalMeasure=smm_Base1MeasureRelationship(), DimensionalMeasure7=smm_Base2MeasureRelationship(), DimensionalMeasure14=smm_BaseMeasureRelationship(), to=set(), to37=set(), to40=set(), from_43=set(), to45=set(), DimensionalMeasure166=smm_RankingMeasureRelationship(), DimensionalMeasure197=smm_RescaleMeasureRelationship()), '', DimensionalMeasure=smm_Base1MeasureRelationship(), DimensionalMeasure7=smm_Base2MeasureRelationship(), DimensionalMeasure14=smm_BaseMeasureRelationship(), to=set(), to37=set(), to40=set(), from_43=set(), to45=set(), DimensionalMeasure166=smm_RankingMeasureRelationship(), DimensionalMeasure197=smm_RescaleMeasureRelationship()) == None


from python_code import smm_Base1MeasurementRelationship
from python_code import smm_Base2MeasurementRelationship
from python_code import smm_BaseMeasurementRelationship
from python_code import smm_DimensionalMeasurement
from python_code import smm_RankingMeasurementRelationship
from python_code import smm_RescaleMeasurementRelationship

def test_smm_DimensionalMeasurement___init__():
    assert smm_DimensionalMeasurement.__init__(smm_DimensionalMeasurement('\x00', DimensionalMeasurement17=smm_BaseMeasurementRelationship(), DimensionalMeasurement=smm_Base1MeasurementRelationship(), DimensionalMeasurement11=smm_Base2MeasurementRelationship(), to47=set(), to50=set(), to53=set(), from_56=set(), to58=set(), DimensionalMeasurement171=smm_RankingMeasurementRelationship(), DimensionalMeasurement205=smm_RescaleMeasurementRelationship()), '', DimensionalMeasurement17=smm_BaseMeasurementRelationship(), DimensionalMeasurement=smm_Base1MeasurementRelationship(), DimensionalMeasurement11=smm_Base2MeasurementRelationship(), to47=set(), to50=set(), to53=set(), from_56=set(), to58=set(), DimensionalMeasurement171=smm_RankingMeasurementRelationship(), DimensionalMeasurement205=smm_RescaleMeasurementRelationship()) == None


from python_code import smm_Grade
from python_code import smm_RankingMeasurementRelationship

def test_smm_Grade___init__():
    assert smm_Grade.__init__(smm_Grade('', '\x00', from_71=smm_RankingMeasurementRelationship(), Grade=smm_RankingMeasurementRelationship()), '\x00\x00', '', from_71=smm_RankingMeasurementRelationship(), Grade=smm_RankingMeasurementRelationship()) == None


from python_code import smm_MeasureLibrary
from python_code import smm_SmmModel

def test_smm_MeasureLibrary___init__():
    assert smm_MeasureLibrary.__init__(smm_MeasureLibrary(smm_MeasureLibrary=set(), smm_MeasureLibrary116=set(), smm_MeasureLibrary220=smm_SmmModel()), smm_MeasureLibrary=set(), smm_MeasureLibrary116=set(), smm_MeasureLibrary220=smm_SmmModel()) == None

def test_smm_MeasureLibrary_getOperations():
    assert smm_MeasureLibrary.getOperations(smm_MeasureLibrary(smm_MeasureLibrary=set(), smm_MeasureLibrary116=set(), smm_MeasureLibrary220=smm_SmmModel())) == None

def test_smm_MeasureLibrary_getOclOperations():
    assert smm_MeasureLibrary.getOclOperations(smm_MeasureLibrary(smm_MeasureLibrary=set(), smm_MeasureLibrary116=set(), smm_MeasureLibrary220=smm_SmmModel())) == None


from python_code import smm_OCLOperation

def test_smm_OCLOperation___init__():
    assert smm_OCLOperation.__init__(smm_OCLOperation('', '\x00'), '\x00\x00', '') == None


from python_code import smm_Ranking
from python_code import smm_RankingInterval

def test_smm_RankingInterval___init__():
    assert smm_RankingInterval.__init__(smm_RankingInterval('', '', '', '', '', smm_RankingInterval=smm_Ranking()), '', '', '', '', '', smm_RankingInterval=smm_Ranking()) == None


from python_code import smm_RescaleMeasureRelationship
from python_code import smm_RescaledMeasure

def test_smm_RescaledMeasure___init__():
    assert smm_RescaledMeasure.__init__(smm_RescaledMeasure('', to193=set(), RescaledMeasure=smm_RescaleMeasureRelationship()), '', to193=set(), RescaledMeasure=smm_RescaleMeasureRelationship()) == None


from python_code import smm_RescaleMeasurementRelationship
from python_code import smm_RescaledMeasurement

def test_smm_RescaledMeasurement___init__():
    assert smm_RescaledMeasurement.__init__(smm_RescaledMeasurement('', to199=set(), RescaledMeasurement=smm_RescaleMeasurementRelationship()), '', to199=set(), RescaledMeasurement=smm_RescaleMeasurementRelationship()) == None

