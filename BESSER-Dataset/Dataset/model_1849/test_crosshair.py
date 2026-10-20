from python_code import libsys_BarCodeScanner

def test_libsys_BarCodeScanner___init__():
    assert libsys_BarCodeScanner.__init__(libsys_BarCodeScanner()) == None

def test_libsys_BarCodeScanner_readUserNumber():
    assert libsys_BarCodeScanner.readUserNumber(libsys_BarCodeScanner()) == None


from python_code import libsys_Book

def test_libsys_Book___init__():
    assert libsys_Book.__init__(libsys_Book('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import libsys_CD

def test_libsys_CD___init__():
    assert libsys_CD.__init__(libsys_CD('', '', '\x00\x00'), '', '', '') == None


from python_code import libsys_IdentificationCard

def test_libsys_IdentificationCard___init__():
    assert libsys_IdentificationCard.__init__(libsys_IdentificationCard(0), 0) == None


from python_code import libsys_Magazine

def test_libsys_Magazine___init__():
    assert libsys_Magazine.__init__(libsys_Magazine('', '\x00'), '\x00\x00', '') == None


from python_code import libsys_UnpaidFee

def test_libsys_UnpaidFee___init__():
    assert libsys_UnpaidFee.__init__(libsys_UnpaidFee(0, '\x00'), 0, '\x00') == None


from python_code import libsys_UserAdministration

def test_libsys_UserAdministration___init__():
    assert libsys_UserAdministration.__init__(libsys_UserAdministration(libsys_UserAdministration=set()), libsys_UserAdministration=set()) == None

def test_libsys_UserAdministration_manageUserAccount():
    assert libsys_UserAdministration.manageUserAccount(libsys_UserAdministration(libsys_UserAdministration=set())) == None


from python_code import libsys_Video

def test_libsys_Video___init__():
    assert libsys_Video.__init__(libsys_Video('', '\x00'), '\x00\x00', '') == None

