from python_code import smarthome_CSVSensor

def test_smarthome_CSVSensor___init__():
    assert smarthome_CSVSensor.__init__(smarthome_CSVSensor(''), '') == None


from python_code import smarthome_Duration
from python_code import smarthome_Rule

def test_smarthome_Duration___init__():
    assert smarthome_Duration.__init__(smarthome_Duration(0, '\x00', smarthome_Duration=smarthome_Rule()), 0, '\x00', smarthome_Duration=smarthome_Rule()) == None


from python_code import smarthome_Person
from python_code import smarthome_PersonPredicate

def test_smarthome_PersonPredicate___init__():
    assert smarthome_PersonPredicate.__init__(smarthome_PersonPredicate('', smarthome_PersonPredicate=smarthome_Person()), '', smarthome_PersonPredicate=smarthome_Person()) == None


from python_code import smarthome_Sensor
from python_code import smarthome_SensorPredicate

def test_smarthome_SensorPredicate___init__():
    assert smarthome_SensorPredicate.__init__(smarthome_SensorPredicate('\x00', 0.0, smarthome_SensorPredicate=smarthome_Sensor()), '', 0.0, smarthome_SensorPredicate=smarthome_Sensor()) == None

