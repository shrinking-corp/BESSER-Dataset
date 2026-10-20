from python_code import mvc_MapComponent

def test_mvc_MapComponent___init__():
    assert mvc_MapComponent.__init__(mvc_MapComponent(False, 0.0, 0.0), True, 0.0, 0.0) == None


from python_code import mvc_MvcApplication

def test_mvc_MvcApplication___init__():
    assert mvc_MvcApplication.__init__(mvc_MvcApplication('\x00', '', '', '', '', mvc_MvcApplication=set(), mvc_MvcApplication2=set(), mvc_MvcApplication4=set()), '', '', '', '', '', mvc_MvcApplication=set(), mvc_MvcApplication2=set(), mvc_MvcApplication4=set()) == None


from python_code import mvc_SocialComponent

def test_mvc_SocialComponent___init__():
    assert mvc_SocialComponent.__init__(mvc_SocialComponent('', '\x00'), '\x00\x00', '') == None

