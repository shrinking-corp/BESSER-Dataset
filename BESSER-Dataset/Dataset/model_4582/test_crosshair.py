from python_code import sparrow_Callprocess

def test_sparrow_Callprocess___init__():
    assert sparrow_Callprocess.__init__(sparrow_Callprocess('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import sparrow_Copydata

def test_sparrow_Copydata___init__():
    assert sparrow_Copydata.__init__(sparrow_Copydata('', '', '\x00\x00'), '', '', '') == None


from python_code import sparrow_Doozle

def test_sparrow_Doozle___init__():
    assert sparrow_Doozle.__init__(sparrow_Doozle('', '', '\x00\x00'), '', '', '') == None


from python_code import sparrow_Dropfile

def test_sparrow_Dropfile___init__():
    assert sparrow_Dropfile.__init__(sparrow_Dropfile(''), '') == None


from python_code import sparrow_FBCLead

def test_sparrow_FBCLead___init__():
    assert sparrow_FBCLead.__init__(sparrow_FBCLead('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import sparrow_Fetch

def test_sparrow_Fetch___init__():
    assert sparrow_Fetch.__init__(sparrow_Fetch('', '\x00'), '\x00\x00', '') == None


from python_code import sparrow_GooglecalPUT

def test_sparrow_GooglecalPUT___init__():
    assert sparrow_GooglecalPUT.__init__(sparrow_GooglecalPUT('', '', '', '', ''), '', '', '', '', '') == None


from python_code import sparrow_LoadCsv

def test_sparrow_LoadCsv___init__():
    assert sparrow_LoadCsv.__init__(sparrow_LoadCsv('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import sparrow_Rest

def test_sparrow_Rest___init__():
    assert sparrow_Rest.__init__(sparrow_Rest('', '', '', '', '', '', '\x00', '', '', '', '', '', sparrow_Rest=set()), '', '', '', '', '', '', '', '', '', '', '\x00', '', sparrow_Rest=set()) == None


from python_code import sparrow_SlackPUT

def test_sparrow_SlackPUT___init__():
    assert sparrow_SlackPUT.__init__(sparrow_SlackPUT('', '', '\x00\x00'), '', '', '') == None


from python_code import sparrow_Sms

def test_sparrow_Sms___init__():
    assert sparrow_Sms.__init__(sparrow_Sms('', '\x00'), '\x00\x00', '') == None


from python_code import sparrow_Transform

def test_sparrow_Transform___init__():
    assert sparrow_Transform.__init__(sparrow_Transform('', '\x00'), '\x00\x00', '') == None


from python_code import sparrow_TrelloGET

def test_sparrow_TrelloGET___init__():
    assert sparrow_TrelloGET.__init__(sparrow_TrelloGET('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import sparrow_TrelloPUT

def test_sparrow_TrelloPUT___init__():
    assert sparrow_TrelloPUT.__init__(sparrow_TrelloPUT('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import sparrow_Updatedaudit

def test_sparrow_Updatedaudit___init__():
    assert sparrow_Updatedaudit.__init__(sparrow_Updatedaudit('', '\x00'), '\x00\x00', '') == None


from python_code import sparrow_WriteCsv

def test_sparrow_WriteCsv___init__():
    assert sparrow_WriteCsv.__init__(sparrow_WriteCsv('\x00\x00', '', '', ''), '', '', '', '') == None

