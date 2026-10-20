from python_code import pokerleague_DataStructureVersion

def test_pokerleague_DataStructureVersion___init__():
    assert pokerleague_DataStructureVersion.__init__(pokerleague_DataStructureVersion(0, '\x00'), 0, '\x00') == None


from python_code import pokerleague_DataVersion

def test_pokerleague_DataVersion___init__():
    assert pokerleague_DataVersion.__init__(pokerleague_DataVersion(0, '\x00'), 0, '\x00') == None


from python_code import pokerleague_DescribedEntity

def test_pokerleague_DescribedEntity___init__():
    assert pokerleague_DescribedEntity.__init__(pokerleague_DescribedEntity('', '\x00'), '\x00\x00', '') == None


from python_code import pokerleague_IdentifiableEntity

def test_pokerleague_IdentifiableEntity___init__():
    assert pokerleague_IdentifiableEntity.__init__(pokerleague_IdentifiableEntity(0, False, False), 0, False, False) == None


from python_code import pokerleague_Settings

def test_pokerleague_Settings___init__():
    assert pokerleague_Settings.__init__(pokerleague_Settings(0, '', '', '', '\x00', '', '', '', ''), 0, '', '', '', '', '\x00', '', '', '') == None

