from python_code import CentreHospitalier

def test_CentreHospitalier___init__():
    assert CentreHospitalier.__init__(CentreHospitalier(0, '', '', service3=set()), 0, '', '', service3=set()) == None


from python_code import Laboratoire

def test_Laboratoire___init__():
    assert Laboratoire.__init__(Laboratoire(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient(0, '', '', 0, '', ''), 0, '', '', 0, '\x00', '') == None


from python_code import Personne

def test_Personne___init__():
    assert Personne.__init__(Personne(0, '', '', '', '', 0, contact5=set()), 0, '', '', '', '', 0, contact5=set()) == None


from python_code import Rendez_vous

def test_Rendez_vous___init__():
    assert Rendez_vous.__init__(Rendez_vous('', '', 0), '\x00', '', 0) == None

