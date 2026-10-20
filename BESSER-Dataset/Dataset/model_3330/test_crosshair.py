from python_code import psample_Object

def test_psample_Object___init__():
    assert psample_Object.__init__(psample_Object(''), '') == None


from python_code import psample_Package

def test_psample_Package___init__():
    assert psample_Package.__init__(psample_Package('', psample_Package=set()), '', psample_Package=set()) == None

