from python_code import stateMachine_Call

def test_stateMachine_Call___init__():
    assert stateMachine_Call.__init__(stateMachine_Call('', '\x00'), '\x00\x00', '') == None


from python_code import stateMachine_Key

def test_stateMachine_Key___init__():
    assert stateMachine_Key.__init__(stateMachine_Key(''), '') == None


from python_code import stateMachine_Managed

def test_stateMachine_Managed___init__():
    assert stateMachine_Managed.__init__(stateMachine_Managed(False, 0), False, 0) == None


from python_code import stateMachine_Play

def test_stateMachine_Play___init__():
    assert stateMachine_Play.__init__(stateMachine_Play('', '\x00'), '\x00\x00', '') == None


from python_code import stateMachine_Recorderd

def test_stateMachine_Recorderd___init__():
    assert stateMachine_Recorderd.__init__(stateMachine_Recorderd(''), '') == None


from python_code import stateMachine_SMS
from python_code import stateMachine_SMSReceived
from python_code import stateMachine_SendSms

def test_stateMachine_SMS___init__():
    assert stateMachine_SMS.__init__(stateMachine_SMS('', '', '\x00\x00', stateMachine_SMS=stateMachine_SendSms(), stateMachine_SMS19=stateMachine_SMSReceived()), '', '', '', stateMachine_SMS=stateMachine_SendSms(), stateMachine_SMS19=stateMachine_SMSReceived()) == None


from python_code import stateMachine_SetTimer

def test_stateMachine_SetTimer___init__():
    assert stateMachine_SetTimer.__init__(stateMachine_SetTimer(0.0), 0.0) == None

