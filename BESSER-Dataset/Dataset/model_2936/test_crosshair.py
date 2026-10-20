from python_code import extended_DataType

def test_extended_DataType___init__():
    assert extended_DataType.__init__(extended_DataType(''), '') == None


from python_code import extended_Domainmodel

def test_extended_Domainmodel___init__():
    assert extended_Domainmodel.__init__(extended_Domainmodel('', extended_Domainmodel=set()), '', extended_Domainmodel=set()) == None


from python_code import extended_Form

def test_extended_Form___init__():
    assert extended_Form.__init__(extended_Form('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import extended_FormReport

def test_extended_FormReport___init__():
    assert extended_FormReport.__init__(extended_FormReport('', '', '\x00\x00'), '', '', '') == None


from python_code import extended_Import

def test_extended_Import___init__():
    assert extended_Import.__init__(extended_Import(''), '') == None


from python_code import extended_PackageDeclaration

def test_extended_PackageDeclaration___init__():
    assert extended_PackageDeclaration.__init__(extended_PackageDeclaration('', extended_PackageDeclaration=set()), '', extended_PackageDeclaration=set()) == None


from python_code import extended_Page

def test_extended_Page___init__():
    assert extended_Page.__init__(extended_Page('', '', '', '', extended_Page=set()), '', '', '', '', extended_Page=set()) == None

