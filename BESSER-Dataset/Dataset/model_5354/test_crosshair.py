from python_code import p2_Configuration

def test_p2_Configuration___init__():
    assert p2_Configuration.__init__(p2_Configuration('', '', '\x00\x00'), '', '', '') == None


from python_code import p2_ProfileDefinition

def test_p2_ProfileDefinition___init__():
    assert p2_ProfileDefinition.__init__(p2_ProfileDefinition(False, p2_ProfileDefinition=set(), p2_ProfileDefinition2=set()), False, p2_ProfileDefinition=set(), p2_ProfileDefinition2=set()) == None

def test_p2_ProfileDefinition_setRequirements():
    assert p2_ProfileDefinition.setRequirements(p2_ProfileDefinition(False, p2_ProfileDefinition=set(), p2_ProfileDefinition2=set()), '\x00') == None

def test_p2_ProfileDefinition_setRepositories():
    assert p2_ProfileDefinition.setRepositories(p2_ProfileDefinition(False, p2_ProfileDefinition=set(), p2_ProfileDefinition2=set()), '\x00') == None


from python_code import p2_RepositoryList

def test_p2_RepositoryList___init__():
    assert p2_RepositoryList.__init__(p2_RepositoryList('', p2_RepositoryList=set()), '', p2_RepositoryList=set()) == None

