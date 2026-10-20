from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Course_Adminstrator

def test_Course_Adminstrator___init__():
    assert Course_Adminstrator.__init__(Course_Adminstrator(''), '') == None

