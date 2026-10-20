from python_code import serviceInterfaces_Interface

def test_serviceInterfaces_Interface___init__():
    assert serviceInterfaces_Interface.__init__(serviceInterfaces_Interface('', '\x00'), '\x00\x00', '') == None


from python_code import serviceInterfaces_Package

def test_serviceInterfaces_Package___init__():
    assert serviceInterfaces_Package.__init__(serviceInterfaces_Package('', serviceInterfaces_Package=set()), '', serviceInterfaces_Package=set()) == None


from python_code import serviceInterfaces_codegen_Pointcut

def test_serviceInterfaces_codegen_Pointcut___init__():
    assert serviceInterfaces_codegen_Pointcut.__init__(serviceInterfaces_codegen_Pointcut(''), '') == None


from python_code import serviceInterfaces_codegen_TransformationLibrary

def test_serviceInterfaces_codegen_TransformationLibrary___init__():
    assert serviceInterfaces_codegen_TransformationLibrary.__init__(serviceInterfaces_codegen_TransformationLibrary('', '\x00'), '\x00\x00', '') == None


from python_code import serviceInterfaces_modelingenv_ExtensionPoint

def test_serviceInterfaces_modelingenv_ExtensionPoint___init__():
    assert serviceInterfaces_modelingenv_ExtensionPoint.__init__(serviceInterfaces_modelingenv_ExtensionPoint(''), '') == None


from python_code import serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0

def test_serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0___init__():
    assert serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0.__init__(serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0('', serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0=set()), '', serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0=set()) == None


from python_code import serviceInterfaces_modelingenv_JavaTypeDeclaration

def test_serviceInterfaces_modelingenv_JavaTypeDeclaration___init__():
    assert serviceInterfaces_modelingenv_JavaTypeDeclaration.__init__(serviceInterfaces_modelingenv_JavaTypeDeclaration(''), '') == None


from python_code import serviceInterfaces_modelingenv_Operation

def test_serviceInterfaces_modelingenv_Operation___init__():
    assert serviceInterfaces_modelingenv_Operation.__init__(serviceInterfaces_modelingenv_Operation(''), '') == None

