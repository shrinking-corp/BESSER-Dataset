from python_code import lMS_LMS

def test_lMS_LMS___init__():
    assert lMS_LMS.__init__(lMS_LMS('\x00', lMS_LMS=set()), '', lMS_LMS=set()) == None

