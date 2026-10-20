from python_code import eel_EnergyComputation

def test_eel_EnergyComputation___init__():
    assert eel_EnergyComputation.__init__(eel_EnergyComputation()) == None

def test_eel_EnergyComputation_type():
    assert eel_EnergyComputation.type(eel_EnergyComputation()) == None

def test_eel_EnergyComputation_value():
    assert eel_EnergyComputation.value(eel_EnergyComputation()) == None


from python_code import eel_Integral
from python_code import eel_Interval

def test_eel_Integral___init__():
    assert eel_Integral.__init__(eel_Integral('', eel_Integral=eel_Interval()), '', eel_Integral=eel_Interval()) == None


from python_code import eel_MeasureAttribute

def test_eel_MeasureAttribute___init__():
    assert eel_MeasureAttribute.__init__(eel_MeasureAttribute(''), '') == None


from python_code import eel_MeasureBinaryProductOperation

def test_eel_MeasureBinaryProductOperation___init__():
    assert eel_MeasureBinaryProductOperation.__init__(eel_MeasureBinaryProductOperation()) == None

def test_eel_MeasureBinaryProductOperation_value():
    assert eel_MeasureBinaryProductOperation.value(eel_MeasureBinaryProductOperation()) == None


from python_code import eel_MeasureBinarySumOperation

def test_eel_MeasureBinarySumOperation___init__():
    assert eel_MeasureBinarySumOperation.__init__(eel_MeasureBinarySumOperation()) == None

def test_eel_MeasureBinarySumOperation_value():
    assert eel_MeasureBinarySumOperation.value(eel_MeasureBinarySumOperation()) == None


from python_code import eel_MeasureOCL

def test_eel_MeasureOCL___init__():
    assert eel_MeasureOCL.__init__(eel_MeasureOCL(''), '') == None


from python_code import eel_MeasureUnboundProductOperation

def test_eel_MeasureUnboundProductOperation___init__():
    assert eel_MeasureUnboundProductOperation.__init__(eel_MeasureUnboundProductOperation()) == None

def test_eel_MeasureUnboundProductOperation_value():
    assert eel_MeasureUnboundProductOperation.value(eel_MeasureUnboundProductOperation()) == None


from python_code import eel_MeasureUnboundSumOperation

def test_eel_MeasureUnboundSumOperation___init__():
    assert eel_MeasureUnboundSumOperation.__init__(eel_MeasureUnboundSumOperation()) == None

def test_eel_MeasureUnboundSumOperation_value():
    assert eel_MeasureUnboundSumOperation.value(eel_MeasureUnboundSumOperation()) == None


from python_code import eel_MeasureValue

def test_eel_MeasureValue___init__():
    assert eel_MeasureValue.__init__(eel_MeasureValue(''), '') == None

def test_eel_MeasureValue_value():
    assert eel_MeasureValue.value(eel_MeasureValue('')) == None


from python_code import eel_NormalDistribution

def test_eel_NormalDistribution___init__():
    assert eel_NormalDistribution.__init__(eel_NormalDistribution('', '\x00'), '\x00\x00', '') == None


from python_code import eel_Platform

def test_eel_Platform___init__():
    assert eel_Platform.__init__(eel_Platform('', eel_Platform=set(), eel_Platform2=set()), '', eel_Platform=set(), eel_Platform2=set()) == None


from python_code import eel_PowerComputation

def test_eel_PowerComputation___init__():
    assert eel_PowerComputation.__init__(eel_PowerComputation()) == None

def test_eel_PowerComputation_value():
    assert eel_PowerComputation.value(eel_PowerComputation()) == None

def test_eel_PowerComputation_type():
    assert eel_PowerComputation.type(eel_PowerComputation()) == None


from python_code import eel_RealTimeDuration

def test_eel_RealTimeDuration___init__():
    assert eel_RealTimeDuration.__init__(eel_RealTimeDuration()) == None

def test_eel_RealTimeDuration_type():
    assert eel_RealTimeDuration.type(eel_RealTimeDuration()) == None


from python_code import eel_Sampling

def test_eel_Sampling___init__():
    assert eel_Sampling.__init__(eel_Sampling('', eel_Sampling=set()), '', eel_Sampling=set()) == None


from python_code import eel_TypedMeasure

def test_eel_TypedMeasure___init__():
    assert eel_TypedMeasure.__init__(eel_TypedMeasure(''), '') == None

def test_eel_TypedMeasure_type():
    assert eel_TypedMeasure.type(eel_TypedMeasure('')) == None

def test_eel_TypedMeasure_name():
    assert eel_TypedMeasure.name(eel_TypedMeasure('')) == None

