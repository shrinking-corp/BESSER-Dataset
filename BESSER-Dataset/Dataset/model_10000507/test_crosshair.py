from python_code import checkers_CheckerFrame

def test_checkers_CheckerFrame___init__():
    assert checkers_CheckerFrame.__init__(checkers_CheckerFrame('', '\x00'), '\x00\x00', '') == None


from python_code import checkers_CheckerMove

def test_checkers_CheckerMove___init__():
    assert checkers_CheckerMove.__init__(checkers_CheckerMove(0, 0, 0), 0, 0, 0) == None


from python_code import checkers_GameEngine

def test_checkers_GameEngine___init__():
    assert checkers_GameEngine.__init__(checkers_GameEngine(0, 0, 0, 0, 0), 0, 0, 0, 0, 0) == None


from python_code import checkers_GameWin
from python_code import genmymodelreverse_java_awt_Point
from python_code import genmymodelreverse_javax_swing_JLabel

def test_checkers_GameWin___init__():
    assert checkers_GameWin.__init__(checkers_GameWin(genmymodelreverse_java_awt_Point(), genmymodelreverse_javax_swing_JLabel()), genmymodelreverse_java_awt_Point(), genmymodelreverse_javax_swing_JLabel()) == None


from python_code import checkers_PlaySound

def test_checkers_PlaySound___init__():
    assert checkers_PlaySound.__init__(checkers_PlaySound('', 0), '', 0) == None

