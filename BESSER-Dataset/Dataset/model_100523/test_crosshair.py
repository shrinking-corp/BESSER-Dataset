from python_code import umluseCases_Actor

def test_umluseCases_Actor___init__():
    assert umluseCases_Actor.__init__(umluseCases_Actor()) == None

def test_umluseCases_Actor_must_have_name():
    assert umluseCases_Actor.must_have_name(umluseCases_Actor(), '', '') == None

def test_umluseCases_Actor_associations():
    assert umluseCases_Actor.associations(umluseCases_Actor(), '', '') == None

