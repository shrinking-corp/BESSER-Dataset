from python_code import cevinedit_CompartmentEReferenceCont

def test_cevinedit_CompartmentEReferenceCont___init__():
    assert cevinedit_CompartmentEReferenceCont.__init__(cevinedit_CompartmentEReferenceCont(False, '\x00'), False, '\x00') == None


from python_code import cevinedit_Link

def test_cevinedit_Link___init__():
    assert cevinedit_Link.__init__(cevinedit_Link('', '', '', '', '', '', 0, ''), '', '', '', '', '', '', 0, '') == None


from python_code import cevinedit_LinkEClass

def test_cevinedit_LinkEClass___init__():
    assert cevinedit_LinkEClass.__init__(cevinedit_LinkEClass('', '\x00'), '\x00\x00', '') == None


from python_code import cevinedit_NodeEClass

def test_cevinedit_NodeEClass___init__():
    assert cevinedit_NodeEClass.__init__(cevinedit_NodeEClass('', '', '', '', '', '', '', '', 0, '', '', False, ''), '', '', '', '', '', '', '', '', 0, '', '', False, '') == None

