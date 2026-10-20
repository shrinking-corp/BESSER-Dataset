from python_code import use_registered_classes_A

def test_use_registered_classes_A___init__():
    assert use_registered_classes_A.__init__(use_registered_classes_A(0, '', '\x00\x00'), 0, '', '') == None

