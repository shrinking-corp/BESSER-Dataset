from python_code import KragsteinPackage_Generalization

def test_KragsteinPackage_Generalization___init__():
    assert KragsteinPackage_Generalization.__init__(KragsteinPackage_Generalization(''), '') == None


from python_code import KragsteinPackage_Note

def test_KragsteinPackage_Note___init__():
    assert KragsteinPackage_Note.__init__(KragsteinPackage_Note('', '\x00'), '\x00\x00', '') == None


from python_code import KragsteinPackage_Package

def test_KragsteinPackage_Package___init__():
    assert KragsteinPackage_Package.__init__(KragsteinPackage_Package('\x00\x00', '', KragsteinPackage_Package=set()), '', '', KragsteinPackage_Package=set()) == None

