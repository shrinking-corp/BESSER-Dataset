from python_code import MARTE_Library_BasicNFP_Types_NFP_Area

def test_MARTE_Library_BasicNFP_Types_NFP_Area___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Area.__init__(MARTE_Library_BasicNFP_Types_NFP_Area('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_AperiodicPattern
from python_code import MARTE_Library_BasicNFP_Types_NFP_Boolean

def test_MARTE_Library_BasicNFP_Types_NFP_Boolean___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Boolean.__init__(MARTE_Library_BasicNFP_Types_NFP_Boolean('', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()), '', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()) == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_CommonType

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.__init__(MARTE_Library_BasicNFP_Types_NFP_CommonType('', '', '', '', ''), '', '', '', '', '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_normal():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.normal(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '', '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_uniform():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.uniform(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '', '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_triangular():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.triangular(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '', '', '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_exp():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.exp(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_bernoulli():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.bernoulli(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_gamma():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.gamma(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '', '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_poisson():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.poisson(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_binomial():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.binomial(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '', '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_geometric():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.geometric(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '') == None

def test_MARTE_Library_BasicNFP_Types_NFP_CommonType_logarithmic():
    assert MARTE_Library_BasicNFP_Types_NFP_CommonType.logarithmic(MARTE_Library_BasicNFP_Types_NFP_CommonType('\x00', '\x00\x00', '', '', ''), '') == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_DataSize

def test_MARTE_Library_BasicNFP_Types_NFP_DataSize___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_DataSize.__init__(MARTE_Library_BasicNFP_Types_NFP_DataSize('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_DataTxRate

def test_MARTE_Library_BasicNFP_Types_NFP_DataTxRate___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_DataTxRate.__init__(MARTE_Library_BasicNFP_Types_NFP_DataTxRate('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_AperiodicPattern
from python_code import MARTE_Library_BasicNFP_Types_NFP_DateTime

def test_MARTE_Library_BasicNFP_Types_NFP_DateTime___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_DateTime.__init__(MARTE_Library_BasicNFP_Types_NFP_DateTime('', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()), '', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()) == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Duration

def test_MARTE_Library_BasicNFP_Types_NFP_Duration___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Duration.__init__(MARTE_Library_BasicNFP_Types_NFP_Duration('', '', '', '', ''), '', '', '', '', '') == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Energy

def test_MARTE_Library_BasicNFP_Types_NFP_Energy___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Energy.__init__(MARTE_Library_BasicNFP_Types_NFP_Energy('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Frequency

def test_MARTE_Library_BasicNFP_Types_NFP_Frequency___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Frequency.__init__(MARTE_Library_BasicNFP_Types_NFP_Frequency('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_AperiodicPattern
from python_code import MARTE_Library_BasicNFP_Types_NFP_Integer

def test_MARTE_Library_BasicNFP_Types_NFP_Integer___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Integer.__init__(MARTE_Library_BasicNFP_Types_NFP_Integer('', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()), '', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()) == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Length

def test_MARTE_Library_BasicNFP_Types_NFP_Length___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Length.__init__(MARTE_Library_BasicNFP_Types_NFP_Length('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_AperiodicPattern
from python_code import MARTE_Library_BasicNFP_Types_NFP_Natural

def test_MARTE_Library_BasicNFP_Types_NFP_Natural___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Natural.__init__(MARTE_Library_BasicNFP_Types_NFP_Natural('', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()), '', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()) == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Percentage

def test_MARTE_Library_BasicNFP_Types_NFP_Percentage___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Percentage.__init__(MARTE_Library_BasicNFP_Types_NFP_Percentage(''), '') == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Power

def test_MARTE_Library_BasicNFP_Types_NFP_Power___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Power.__init__(MARTE_Library_BasicNFP_Types_NFP_Power('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Price

def test_MARTE_Library_BasicNFP_Types_NFP_Price___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Price.__init__(MARTE_Library_BasicNFP_Types_NFP_Price(''), '') == None


from python_code import MARTE_Library_BasicNFP_Types_AperiodicPattern
from python_code import MARTE_Library_BasicNFP_Types_NFP_Real

def test_MARTE_Library_BasicNFP_Types_NFP_Real___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Real.__init__(MARTE_Library_BasicNFP_Types_NFP_Real('', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()), '', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()) == None


from python_code import MARTE_Library_BasicNFP_Types_AperiodicPattern
from python_code import MARTE_Library_BasicNFP_Types_NFP_String

def test_MARTE_Library_BasicNFP_Types_NFP_String___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_String.__init__(MARTE_Library_BasicNFP_Types_NFP_String('', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()), '', NFP_CommonType=MARTE_Library_BasicNFP_Types_AperiodicPattern()) == None


from python_code import MARTE_Library_BasicNFP_Types_NFP_Weight

def test_MARTE_Library_BasicNFP_Types_NFP_Weight___init__():
    assert MARTE_Library_BasicNFP_Types_NFP_Weight.__init__(MARTE_Library_BasicNFP_Types_NFP_Weight('', '\x00'), '\x00\x00', '') == None


from python_code import MARTE_Library_BasicNFP_Types_OpenPattern
from python_code import NFP_Duration
from python_code import NFP_Frequency

def test_MARTE_Library_BasicNFP_Types_OpenPattern___init__():
    assert MARTE_Library_BasicNFP_Types_OpenPattern.__init__(MARTE_Library_BasicNFP_Types_OpenPattern('', MARTE_Library_BasicNFP_Types_OpenPattern82=NFP_Frequency(), MARTE_Library_BasicNFP_Types_OpenPattern=NFP_Duration()), '', MARTE_Library_BasicNFP_Types_OpenPattern82=NFP_Frequency(), MARTE_Library_BasicNFP_Types_OpenPattern=NFP_Duration()) == None


from python_code import EDF_Parameters
from python_code import FixedPriorityParameters
from python_code import MARTE_Library_GRM_BasicTypes_PeriodicServerParameters
from python_code import MARTE_Library_GRM_BasicTypes_SchedParameters
from python_code import NFP_Duration
from python_code import NFP_Integer
from python_code import PeriodicServerParameters
from python_code import PoolingParameters

def test_MARTE_Library_GRM_BasicTypes_PeriodicServerParameters___init__():
    assert MARTE_Library_GRM_BasicTypes_PeriodicServerParameters.__init__(MARTE_Library_GRM_BasicTypes_PeriodicServerParameters('\x00\x00', '', MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20=NFP_Integer(), MARTE_Library_GRM_BasicTypes_PeriodicServerParameters=NFP_Duration(), MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17=NFP_Duration(), FixedPriorityParameters=MARTE_Library_GRM_BasicTypes_SchedParameters('', MARTE_Library_GRM_BasicTypes_SchedParameters=EDF_Parameters(), MARTE_Library_GRM_BasicTypes_SchedParameters3=FixedPriorityParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters5=PoolingParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters7=PeriodicServerParameters())), '', '', MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20=NFP_Integer(), MARTE_Library_GRM_BasicTypes_PeriodicServerParameters=NFP_Duration(), MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17=NFP_Duration(), FixedPriorityParameters=MARTE_Library_GRM_BasicTypes_SchedParameters('', MARTE_Library_GRM_BasicTypes_SchedParameters=EDF_Parameters(), MARTE_Library_GRM_BasicTypes_SchedParameters3=FixedPriorityParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters5=PoolingParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters7=PeriodicServerParameters())) == None


from python_code import EDF_Parameters
from python_code import FixedPriorityParameters
from python_code import MARTE_Library_GRM_BasicTypes_SchedParameters
from python_code import PeriodicServerParameters
from python_code import PoolingParameters

def test_MARTE_Library_GRM_BasicTypes_SchedParameters___init__():
    assert MARTE_Library_GRM_BasicTypes_SchedParameters.__init__(MARTE_Library_GRM_BasicTypes_SchedParameters('', MARTE_Library_GRM_BasicTypes_SchedParameters=EDF_Parameters(), MARTE_Library_GRM_BasicTypes_SchedParameters3=FixedPriorityParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters5=PoolingParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters7=PeriodicServerParameters()), '\x00', MARTE_Library_GRM_BasicTypes_SchedParameters=EDF_Parameters(), MARTE_Library_GRM_BasicTypes_SchedParameters3=FixedPriorityParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters5=PoolingParameters(), MARTE_Library_GRM_BasicTypes_SchedParameters7=PeriodicServerParameters()) == None


from python_code import MARTE_Library_MARTE_DataTypes_Array

def test_MARTE_Library_MARTE_DataTypes_Array___init__():
    assert MARTE_Library_MARTE_DataTypes_Array.__init__(MARTE_Library_MARTE_DataTypes_Array()) == None

def test_MARTE_Library_MARTE_DataTypes_Array_at():
    assert MARTE_Library_MARTE_DataTypes_Array.at(MARTE_Library_MARTE_DataTypes_Array(), '') == None


from python_code import MARTE_Library_MARTE_DataTypes_IntegerInterval

def test_MARTE_Library_MARTE_DataTypes_IntegerInterval___init__():
    assert MARTE_Library_MARTE_DataTypes_IntegerInterval.__init__(MARTE_Library_MARTE_DataTypes_IntegerInterval(''), '') == None


from python_code import MARTE_Library_MARTE_DataTypes_IntegerMatrix

def test_MARTE_Library_MARTE_DataTypes_IntegerMatrix___init__():
    assert MARTE_Library_MARTE_DataTypes_IntegerMatrix.__init__(MARTE_Library_MARTE_DataTypes_IntegerMatrix(MARTE_Library_MARTE_DataTypes_IntegerMatrix=set()), MARTE_Library_MARTE_DataTypes_IntegerMatrix=set()) == None

def test_MARTE_Library_MARTE_DataTypes_IntegerMatrix_at():
    assert MARTE_Library_MARTE_DataTypes_IntegerMatrix.at(MARTE_Library_MARTE_DataTypes_IntegerMatrix(MARTE_Library_MARTE_DataTypes_IntegerMatrix=set()), 0) == None


from python_code import MARTE_Library_MARTE_DataTypes_IntegerVector

def test_MARTE_Library_MARTE_DataTypes_IntegerVector___init__():
    assert MARTE_Library_MARTE_DataTypes_IntegerVector.__init__(MARTE_Library_MARTE_DataTypes_IntegerVector(''), '') == None

def test_MARTE_Library_MARTE_DataTypes_IntegerVector_at():
    assert MARTE_Library_MARTE_DataTypes_IntegerVector.at(MARTE_Library_MARTE_DataTypes_IntegerVector(''), 0) == None


from python_code import MARTE_Library_MARTE_DataTypes_RealMatrix

def test_MARTE_Library_MARTE_DataTypes_RealMatrix___init__():
    assert MARTE_Library_MARTE_DataTypes_RealMatrix.__init__(MARTE_Library_MARTE_DataTypes_RealMatrix(''), '') == None

def test_MARTE_Library_MARTE_DataTypes_RealMatrix_at():
    assert MARTE_Library_MARTE_DataTypes_RealMatrix.at(MARTE_Library_MARTE_DataTypes_RealMatrix(''), 0, '\x00\x00') == None


from python_code import MARTE_Library_MARTE_DataTypes_RealVector

def test_MARTE_Library_MARTE_DataTypes_RealVector___init__():
    assert MARTE_Library_MARTE_DataTypes_RealVector.__init__(MARTE_Library_MARTE_DataTypes_RealVector(''), '') == None

def test_MARTE_Library_MARTE_DataTypes_RealVector_at():
    assert MARTE_Library_MARTE_DataTypes_RealVector.at(MARTE_Library_MARTE_DataTypes_RealVector(''), 0) == None


from python_code import MARTE_Library_MARTE_DataTypes_Realnterval

def test_MARTE_Library_MARTE_DataTypes_Realnterval___init__():
    assert MARTE_Library_MARTE_DataTypes_Realnterval.__init__(MARTE_Library_MARTE_DataTypes_Realnterval(''), '') == None


from python_code import MARTE_Library_MARTE_DataTypes_UtilityType

def test_MARTE_Library_MARTE_DataTypes_UtilityType___init__():
    assert MARTE_Library_MARTE_DataTypes_UtilityType.__init__(MARTE_Library_MARTE_DataTypes_UtilityType()) == None

def test_MARTE_Library_MARTE_DataTypes_UtilityType_le():
    assert MARTE_Library_MARTE_DataTypes_UtilityType.le(MARTE_Library_MARTE_DataTypes_UtilityType(), '') == None

def test_MARTE_Library_MARTE_DataTypes_UtilityType_gt():
    assert MARTE_Library_MARTE_DataTypes_UtilityType.gt(MARTE_Library_MARTE_DataTypes_UtilityType(), '') == None

def test_MARTE_Library_MARTE_DataTypes_UtilityType_lt():
    assert MARTE_Library_MARTE_DataTypes_UtilityType.lt(MARTE_Library_MARTE_DataTypes_UtilityType(), '') == None

def test_MARTE_Library_MARTE_DataTypes_UtilityType_eq():
    assert MARTE_Library_MARTE_DataTypes_UtilityType.eq(MARTE_Library_MARTE_DataTypes_UtilityType(), '') == None

def test_MARTE_Library_MARTE_DataTypes_UtilityType_ge():
    assert MARTE_Library_MARTE_DataTypes_UtilityType.ge(MARTE_Library_MARTE_DataTypes_UtilityType(), '') == None

def test_MARTE_Library_MARTE_DataTypes_UtilityType_ne():
    assert MARTE_Library_MARTE_DataTypes_UtilityType.ne(MARTE_Library_MARTE_DataTypes_UtilityType(), '') == None


from python_code import MARTE_Library_RS_Library_ShapeSpecification

def test_MARTE_Library_RS_Library_ShapeSpecification___init__():
    assert MARTE_Library_RS_Library_ShapeSpecification.__init__(MARTE_Library_RS_Library_ShapeSpecification(''), '') == None


from python_code import MARTE_Library_TimeLibrary_IdealClock

def test_MARTE_Library_TimeLibrary_IdealClock___init__():
    assert MARTE_Library_TimeLibrary_IdealClock.__init__(MARTE_Library_TimeLibrary_IdealClock()) == None

def test_MARTE_Library_TimeLibrary_IdealClock_currentTime():
    assert MARTE_Library_TimeLibrary_IdealClock.currentTime(MARTE_Library_TimeLibrary_IdealClock()) == None


from python_code import MARTE_Library_TimeLibrary_TimedValueType

def test_MARTE_Library_TimeLibrary_TimedValueType___init__():
    assert MARTE_Library_TimeLibrary_TimedValueType.__init__(MARTE_Library_TimeLibrary_TimedValueType('\x00\x00', '', '', ''), '', '', '', '') == None

