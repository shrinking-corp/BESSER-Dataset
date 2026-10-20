from python_code import mtpusecase_Association

def test_mtpusecase_Association___init__():
    assert mtpusecase_Association.__init__(mtpusecase_Association('', '\x00'), '\x00\x00', '') == None


from python_code import mtpusecase_DirectedAssociation

def test_mtpusecase_DirectedAssociation___init__():
    assert mtpusecase_DirectedAssociation.__init__(mtpusecase_DirectedAssociation(''), '') == None


from python_code import mtpusecase_NamedElement

def test_mtpusecase_NamedElement___init__():
    assert mtpusecase_NamedElement.__init__(mtpusecase_NamedElement(''), '') == None

