from python_code import package1_TestOperationAndParameterClass

def test_package1_TestOperationAndParameterClass___init__():
    assert package1_TestOperationAndParameterClass.__init__(package1_TestOperationAndParameterClass()) == None

def test_package1_TestOperationAndParameterClass_operationWithoutParameters():
    assert package1_TestOperationAndParameterClass.operationWithoutParameters(package1_TestOperationAndParameterClass()) == None

def test_package1_TestOperationAndParameterClass_voidOperationWithParameter():
    assert package1_TestOperationAndParameterClass.voidOperationWithParameter(package1_TestOperationAndParameterClass(), '') == None

def test_package1_TestOperationAndParameterClass_orderedMultipleOperation():
    assert package1_TestOperationAndParameterClass.orderedMultipleOperation(package1_TestOperationAndParameterClass()) == None

def test_package1_TestOperationAndParameterClass_uniqueMultipleOperation():
    assert package1_TestOperationAndParameterClass.uniqueMultipleOperation(package1_TestOperationAndParameterClass()) == None

def test_package1_TestOperationAndParameterClass_unorderedMultipleOperation():
    assert package1_TestOperationAndParameterClass.unorderedMultipleOperation(package1_TestOperationAndParameterClass()) == None

def test_package1_TestOperationAndParameterClass_nonuniqueMultipleOperation():
    assert package1_TestOperationAndParameterClass.nonuniqueMultipleOperation(package1_TestOperationAndParameterClass()) == None


from python_code import package1_TestPrimitiveTypeClass

def test_package1_TestPrimitiveTypeClass___init__():
    assert package1_TestPrimitiveTypeClass.__init__(package1_TestPrimitiveTypeClass('', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0.0, '', False, '', '', '', '', '', '', '', 0, '', '', '', '', '', 0.0, '\x00', ''), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00\x00', '', '\x00', 0.0, '', False, '', '', '', '', '', '', '', 0, '', '', '', '', '', 0.0, '', '\x00') == None


from python_code import package1_TestTypeClass2

def test_package1_TestTypeClass2___init__():
    assert package1_TestTypeClass2.__init__(package1_TestTypeClass2(True), False) == None

def test_package1_TestTypeClass2_operation2():
    assert package1_TestTypeClass2.operation2(package1_TestTypeClass2(False)) == None

