from python_code import dsl_Abort

def test_dsl_Abort___init__():
    assert dsl_Abort.__init__(dsl_Abort(''), '') == None


from python_code import dsl_Callprocess

def test_dsl_Callprocess___init__():
    assert dsl_Callprocess.__init__(dsl_Callprocess('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import dsl_ClickSendSms

def test_dsl_ClickSendSms___init__():
    assert dsl_ClickSendSms.__init__(dsl_ClickSendSms('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import dsl_Copydata

def test_dsl_Copydata___init__():
    assert dsl_Copydata.__init__(dsl_Copydata('', '', '\x00\x00'), '', '', '') == None


from python_code import dsl_Doozle

def test_dsl_Doozle___init__():
    assert dsl_Doozle.__init__(dsl_Doozle('', '', '\x00\x00'), '', '', '') == None


from python_code import dsl_Dropfile

def test_dsl_Dropfile___init__():
    assert dsl_Dropfile.__init__(dsl_Dropfile(''), '') == None


from python_code import dsl_ExecJava

def test_dsl_ExecJava___init__():
    assert dsl_ExecJava.__init__(dsl_ExecJava('', '', '\x00\x00'), '', '', '') == None


from python_code import dsl_FBCLead

def test_dsl_FBCLead___init__():
    assert dsl_FBCLead.__init__(dsl_FBCLead('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import dsl_FBFormDownload

def test_dsl_FBFormDownload___init__():
    assert dsl_FBFormDownload.__init__(dsl_FBFormDownload('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import dsl_Fetch

def test_dsl_Fetch___init__():
    assert dsl_Fetch.__init__(dsl_Fetch('', '\x00'), '\x00\x00', '') == None


from python_code import dsl_FirebaseDatabasePut

def test_dsl_FirebaseDatabasePut___init__():
    assert dsl_FirebaseDatabasePut.__init__(dsl_FirebaseDatabasePut('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import dsl_FirebaseReactiveNotification

def test_dsl_FirebaseReactiveNotification___init__():
    assert dsl_FirebaseReactiveNotification.__init__(dsl_FirebaseReactiveNotification('', '', '', '', ''), '', '', '', '', '') == None


from python_code import dsl_GooglecalPUT

def test_dsl_GooglecalPUT___init__():
    assert dsl_GooglecalPUT.__init__(dsl_GooglecalPUT('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import dsl_GooglecontactPUT

def test_dsl_GooglecontactPUT___init__():
    assert dsl_GooglecontactPUT.__init__(dsl_GooglecontactPUT('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import dsl_GooglecontactSelectAll

def test_dsl_GooglecontactSelectAll___init__():
    assert dsl_GooglecontactSelectAll.__init__(dsl_GooglecontactSelectAll('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import dsl_LoadCsv

def test_dsl_LoadCsv___init__():
    assert dsl_LoadCsv.__init__(dsl_LoadCsv('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import dsl_Rest

def test_dsl_Rest___init__():
    assert dsl_Rest.__init__(dsl_Rest('', '', '', '', '', '', '\x00', '', '', '', '', '', dsl_Rest=set()), '', '', '', '', '', '', '', '', '', '', '\x00', '', dsl_Rest=set()) == None


from python_code import dsl_SendMail

def test_dsl_SendMail___init__():
    assert dsl_SendMail.__init__(dsl_SendMail('', '', '', '', ''), '', '', '', '', '') == None


from python_code import dsl_SlackPUT

def test_dsl_SlackPUT___init__():
    assert dsl_SlackPUT.__init__(dsl_SlackPUT('', '', '\x00\x00'), '', '', '') == None


from python_code import dsl_SmsLeadSms

def test_dsl_SmsLeadSms___init__():
    assert dsl_SmsLeadSms.__init__(dsl_SmsLeadSms('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import dsl_Transform

def test_dsl_Transform___init__():
    assert dsl_Transform.__init__(dsl_Transform('', '\x00'), '\x00\x00', '') == None


from python_code import dsl_TrelloGET

def test_dsl_TrelloGET___init__():
    assert dsl_TrelloGET.__init__(dsl_TrelloGET('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import dsl_TrelloPUT

def test_dsl_TrelloPUT___init__():
    assert dsl_TrelloPUT.__init__(dsl_TrelloPUT('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import dsl_Updatedaudit

def test_dsl_Updatedaudit___init__():
    assert dsl_Updatedaudit.__init__(dsl_Updatedaudit('', '', '\x00\x00'), '', '', '') == None


from python_code import dsl_WriteCsv

def test_dsl_WriteCsv___init__():
    assert dsl_WriteCsv.__init__(dsl_WriteCsv('\x00\x00', '', '', ''), '', '', '', '') == None

