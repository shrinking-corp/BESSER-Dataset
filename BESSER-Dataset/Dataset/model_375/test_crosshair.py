from python_code import library_GuideBookWriter

def test_library_GuideBookWriter___init__():
    assert library_GuideBookWriter.__init__(library_GuideBookWriter(''), '') == None


from python_code import library_GuideSpecialistBookWriter

def test_library_GuideSpecialistBookWriter___init__():
    assert library_GuideSpecialistBookWriter.__init__(library_GuideSpecialistBookWriter(''), '') == None


from python_code import library_Library

def test_library_Library___init__():
    assert library_Library.__init__(library_Library('', library_Library=set()), '', library_Library=set()) == None


from python_code import library_SpecialistBookWriter

def test_library_SpecialistBookWriter___init__():
    assert library_SpecialistBookWriter.__init__(library_SpecialistBookWriter(''), '') == None

