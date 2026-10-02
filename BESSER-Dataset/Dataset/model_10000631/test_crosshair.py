from python_code import PatientTO

def test_PatientTO___init__():
    assert PatientTO.__init__(PatientTO(0, '', '', '', datetime.date(1, 1, 1), '', 0, 0, 0), 0, '', '', '', datetime.date(1, 1, 1), '', 0, 0, 0) == None
