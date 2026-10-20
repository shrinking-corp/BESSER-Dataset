from python_code import tracker_BirthDefect

def test_tracker_BirthDefect___init__():
    assert tracker_BirthDefect.__init__(tracker_BirthDefect(True), False) == None


from python_code import tracker_Birthing

def test_tracker_Birthing___init__():
    assert tracker_Birthing.__init__(tracker_Birthing(False, False, '\x00\x00'), False, False, '') == None


from python_code import tracker_BovineBeef

def test_tracker_BovineBeef___init__():
    assert tracker_BovineBeef.__init__(tracker_BovineBeef(''), '') == None


from python_code import tracker_BovineBison

def test_tracker_BovineBison___init__():
    assert tracker_BovineBison.__init__(tracker_BovineBison(''), '') == None


from python_code import tracker_BovineDairy

def test_tracker_BovineDairy___init__():
    assert tracker_BovineDairy.__init__(tracker_BovineDairy(''), '') == None


from python_code import tracker_Caprine

def test_tracker_Caprine___init__():
    assert tracker_Caprine.__init__(tracker_Caprine(''), '') == None


from python_code import tracker_Equine

def test_tracker_Equine___init__():
    assert tracker_Equine.__init__(tracker_Equine(''), '') == None


import datetime as _ch_datetime
from python_code import tracker_HerdTest

def test_tracker_HerdTest___init__():
    assert tracker_HerdTest.__init__(tracker_HerdTest(False, 0, _ch_datetime.date(1, 1, 1)), False, 0, _ch_datetime.date(1, 1, 2)) == None


from python_code import tracker_Mastitis

def test_tracker_Mastitis___init__():
    assert tracker_Mastitis.__init__(tracker_Mastitis('', '\x00'), '\x00\x00', '') == None


from python_code import tracker_MedicalTreatment

def test_tracker_MedicalTreatment___init__():
    assert tracker_MedicalTreatment.__init__(tracker_MedicalTreatment('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import tracker_MilkTest

def test_tracker_MilkTest___init__():
    assert tracker_MilkTest.__init__(tracker_MilkTest(0.0, 0.0, 0.0, 0, 0.0), 0.0, 0.0, 0.0, 0, 0.0) == None


from python_code import tracker_MovedIn

def test_tracker_MovedIn___init__():
    assert tracker_MovedIn.__init__(tracker_MovedIn(''), '') == None


from python_code import tracker_MovedOut

def test_tracker_MovedOut___init__():
    assert tracker_MovedOut.__init__(tracker_MovedOut(''), '') == None


from python_code import tracker_Ovine

def test_tracker_Ovine___init__():
    assert tracker_Ovine.__init__(tracker_Ovine('', '\x00'), '\x00\x00', '') == None


from python_code import tracker_Swine

def test_tracker_Swine___init__():
    assert tracker_Swine.__init__(tracker_Swine('', 0, 0), '\x00', 0, 0) == None


from python_code import tracker_USBeefGrading

def test_tracker_USBeefGrading___init__():
    assert tracker_USBeefGrading.__init__(tracker_USBeefGrading('', '', '\x00\x00'), '', '', '') == None


from python_code import tracker_USOvineGrading

def test_tracker_USOvineGrading___init__():
    assert tracker_USOvineGrading.__init__(tracker_USOvineGrading('', '\x00'), '\x00\x00', '') == None


from python_code import tracker_USSwineGrading

def test_tracker_USSwineGrading___init__():
    assert tracker_USSwineGrading.__init__(tracker_USSwineGrading(''), '') == None


from python_code import tracker_WeighIn

def test_tracker_WeighIn___init__():
    assert tracker_WeighIn.__init__(tracker_WeighIn('', '\x00'), '\x00\x00', '') == None

def test_tracker_WeighIn_previousWeighIn():
    assert tracker_WeighIn.previousWeighIn(tracker_WeighIn('', '')) == None

