from python_code import Course

def test_Course___init__():
    assert Course.__init__(Course(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Course2

def test_Course2___init__():
    assert Course2.__init__(Course2('', 0, '\x00\x00'), '', 0, '') == None


from python_code import Course3

def test_Course3___init__():
    assert Course3.__init__(Course3(0, '', '\x00\x00'), 0, '', '') == None


from python_code import ServiceCourse

def test_ServiceCourse___init__():
    assert ServiceCourse.__init__(ServiceCourse('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import ServiceCourse2

def test_ServiceCourse2___init__():
    assert ServiceCourse2.__init__(ServiceCourse2('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import ServiceCourse3

def test_ServiceCourse3___init__():
    assert ServiceCourse3.__init__(ServiceCourse3('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None

