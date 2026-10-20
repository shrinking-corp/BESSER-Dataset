from python_code import library_Add

def test_library_Add___init__():
    assert library_Add.__init__(library_Add('', '', '', library_Add=set()), '', '', '', library_Add=set()) == None


from python_code import library_AddUser

def test_library_AddUser___init__():
    assert library_AddUser.__init__(library_AddUser('', '', '\x00\x00'), '', '', '') == None


from python_code import library_ByYear

def test_library_ByYear___init__():
    assert library_ByYear.__init__(library_ByYear(''), '') == None


from python_code import library_Check

def test_library_Check___init__():
    assert library_Check.__init__(library_Check(''), '') == None


from python_code import library_Lend

def test_library_Lend___init__():
    assert library_Lend.__init__(library_Lend('', '', '\x00\x00'), '', '', '') == None


from python_code import library_Remove

def test_library_Remove___init__():
    assert library_Remove.__init__(library_Remove(''), '') == None


from python_code import library_Return

def test_library_Return___init__():
    assert library_Return.__init__(library_Return('', '', '\x00\x00'), '', '', '') == None


from python_code import library_Show

def test_library_Show___init__():
    assert library_Show.__init__(library_Show(''), '') == None


from python_code import library_ShowUserAccount

def test_library_ShowUserAccount___init__():
    assert library_ShowUserAccount.__init__(library_ShowUserAccount('', '\x00'), '\x00\x00', '') == None

