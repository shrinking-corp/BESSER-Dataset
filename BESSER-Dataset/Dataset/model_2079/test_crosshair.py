from python_code import goatInfrastructure_Cluster

def test_goatInfrastructure_Cluster___init__():
    assert goatInfrastructure_Cluster.__init__(goatInfrastructure_Cluster('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import goatInfrastructure_Infrastructure

def test_goatInfrastructure_Infrastructure___init__():
    assert goatInfrastructure_Infrastructure.__init__(goatInfrastructure_Infrastructure(''), '') == None


from python_code import goatInfrastructure_Ring

def test_goatInfrastructure_Ring___init__():
    assert goatInfrastructure_Ring.__init__(goatInfrastructure_Ring('', '', '\x00\x00'), '', '', '') == None


from python_code import goatInfrastructure_SingleServer

def test_goatInfrastructure_SingleServer___init__():
    assert goatInfrastructure_SingleServer.__init__(goatInfrastructure_SingleServer('', 0), '', 0) == None

