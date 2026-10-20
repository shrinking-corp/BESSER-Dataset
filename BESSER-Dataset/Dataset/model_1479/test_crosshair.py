from python_code import graphmodelling_Entity

def test_graphmodelling_Entity___init__():
    assert graphmodelling_Entity.__init__(graphmodelling_Entity('', '', '', '', '', '', '\x00', '', '', '', '', '', '', ''), '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '') == None


from python_code import graphmodelling_ModellingType

def test_graphmodelling_ModellingType___init__():
    assert graphmodelling_ModellingType.__init__(graphmodelling_ModellingType(''), '') == None

