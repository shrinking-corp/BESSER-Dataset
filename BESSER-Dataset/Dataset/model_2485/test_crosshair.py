from python_code import fsmProv_Trigger

def test_fsmProv_Trigger___init__():
    assert fsmProv_Trigger.__init__(fsmProv_Trigger(''), '') == None

def test_fsmProv_Trigger_evalTrigger():
    assert fsmProv_Trigger.evalTrigger(fsmProv_Trigger(''), 0) == None

