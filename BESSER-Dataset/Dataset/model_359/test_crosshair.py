from python_code import libraryExample_Asset

def test_libraryExample_Asset___init__():
    assert libraryExample_Asset.__init__(libraryExample_Asset(0.0), 0.0) == None


from python_code import libraryExample_Library

def test_libraryExample_Library___init__():
    assert libraryExample_Library.__init__(libraryExample_Library('', libraryExample_Library=set(), libraryExample_Library2=set()), '', libraryExample_Library=set(), libraryExample_Library2=set()) == None


from python_code import libraryExample_SchoolLibrary

def test_libraryExample_SchoolLibrary___init__():
    assert libraryExample_SchoolLibrary.__init__(libraryExample_SchoolLibrary(''), '') == None

