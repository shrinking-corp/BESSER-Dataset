from python_code import Volunteer_Forms

def test_Volunteer_Forms___init__():
    assert Volunteer_Forms.__init__(Volunteer_Forms(0, '', '\x00\x00'), 0, '', '') == None

