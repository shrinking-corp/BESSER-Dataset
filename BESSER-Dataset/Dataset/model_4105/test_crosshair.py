from python_code import railDsl_Derailer

def test_railDsl_Derailer___init__():
    assert railDsl_Derailer.__init__(railDsl_Derailer(True), False) == None


from python_code import railDsl_LevelCrossing

def test_railDsl_LevelCrossing___init__():
    assert railDsl_LevelCrossing.__init__(railDsl_LevelCrossing(False, 0.0), False, 0.0) == None


from python_code import railDsl_NamedElement

def test_railDsl_NamedElement___init__():
    assert railDsl_NamedElement.__init__(railDsl_NamedElement(''), '') == None


from python_code import railDsl_Platform

def test_railDsl_Platform___init__():
    assert railDsl_Platform.__init__(railDsl_Platform(0.0), 0.0) == None


from python_code import railDsl_RouteObject

def test_railDsl_RouteObject___init__():
    assert railDsl_RouteObject.__init__(railDsl_RouteObject('', False), '', False) == None


from python_code import railDsl_Track
from python_code import railDsl_TrackObject

def test_railDsl_TrackObject___init__():
    assert railDsl_TrackObject.__init__(railDsl_TrackObject(0.0, railDsl_TrackObject=railDsl_Track()), 0.0, railDsl_TrackObject=railDsl_Track()) == None

