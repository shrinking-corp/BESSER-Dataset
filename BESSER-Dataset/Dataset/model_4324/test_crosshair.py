from python_code import metrics_ComplexMeasurement
from python_code import metrics_Measurement
from python_code import metrics_Observation

def test_metrics_Measurement___init__():
    assert metrics_Measurement.__init__(metrics_Measurement('', '', '\x00\x00', metrics_Measurement=metrics_ComplexMeasurement(), metrics_Measurement3=metrics_Observation()), '', '', '', metrics_Measurement=metrics_ComplexMeasurement(), metrics_Measurement3=metrics_Observation()) == None


from python_code import metrics_ValueMeasurement

def test_metrics_ValueMeasurement___init__():
    assert metrics_ValueMeasurement.__init__(metrics_ValueMeasurement(''), '') == None

