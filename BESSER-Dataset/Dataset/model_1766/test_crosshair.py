from python_code import MediaLibrary_DurationArtifact

def test_MediaLibrary_DurationArtifact___init__():
    assert MediaLibrary_DurationArtifact.__init__(MediaLibrary_DurationArtifact(0), 0) == None


from python_code import MediaLibrary_EReader

def test_MediaLibrary_EReader___init__():
    assert MediaLibrary_EReader.__init__(MediaLibrary_EReader('', '\x00'), '\x00\x00', '') == None


from python_code import MediaLibrary_ExternalSource

def test_MediaLibrary_ExternalSource___init__():
    assert MediaLibrary_ExternalSource.__init__(MediaLibrary_ExternalSource(''), '') == None


from python_code import MediaLibrary_NamedElement

def test_MediaLibrary_NamedElement___init__():
    assert MediaLibrary_NamedElement.__init__(MediaLibrary_NamedElement(''), '') == None

