from python_code import WIS_WeideBemerkung

def test_WIS_WeideBemerkung___init__():
    assert WIS_WeideBemerkung.__init__(WIS_WeideBemerkung('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Weidegang2

def test_Weidegang2___init__():
    assert Weidegang2.__init__(Weidegang2('', '', '', '', False, '', '', '', ''), '', '', '', '', False, '', '', '\x00', '') == None

