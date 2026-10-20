from python_code import test_Input

def test_test_Input___init__():
    assert test_Input.__init__(test_Input('', '\x00'), '\x00\x00', '') == None


from python_code import test_Output

def test_test_Output___init__():
    assert test_Output.__init__(test_Output(''), '') == None

def test_test_Output_test():
    assert test_Output.test(test_Output('')) == None

