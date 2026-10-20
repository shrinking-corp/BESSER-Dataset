from python_code import Food

def test_Food___init__():
    assert Food.__init__(Food('', 0, False, '', '\x00', '', False, is_ordered_by1=set()), '', 0, False, '', '', '', False, is_ordered_by1=set()) == None


from python_code import RMS

def test_RMS___init__():
    assert RMS.__init__(RMS('', has6=set(), accesses9=set(), is_generated_by11=set()), '', has6=set(), accesses9=set(), is_generated_by11=set()) == None

