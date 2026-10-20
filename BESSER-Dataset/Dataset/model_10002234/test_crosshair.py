from python_code import ExaminationDate

def test_ExaminationDate___init__():
    assert ExaminationDate.__init__(ExaminationDate('', '\x00'), '\x00\x00', '') == None

