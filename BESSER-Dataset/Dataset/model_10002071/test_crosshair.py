from python_code import CentreHospitalier

def test_CentreHospitalier___init__():
    assert CentreHospitalier.__init__(CentreHospitalier(0, '', '', service15=set()), 0, '', '', service15=set()) == None

