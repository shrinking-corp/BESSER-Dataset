from python_code import fsm_AssignValueAction

def test_fsm_AssignValueAction___init__():
    assert fsm_AssignValueAction.__init__(fsm_AssignValueAction(True), False) == None

def test_fsm_AssignValueAction_execute():
    assert fsm_AssignValueAction.execute(fsm_AssignValueAction(False)) == None


from python_code import fsm_DecreaseValueAction

def test_fsm_DecreaseValueAction___init__():
    assert fsm_DecreaseValueAction.__init__(fsm_DecreaseValueAction(0), 0) == None

def test_fsm_DecreaseValueAction_execute():
    assert fsm_DecreaseValueAction.execute(fsm_DecreaseValueAction(0)) == None


from python_code import fsm_EqualNumberGuard

def test_fsm_EqualNumberGuard___init__():
    assert fsm_EqualNumberGuard.__init__(fsm_EqualNumberGuard()) == None

def test_fsm_EqualNumberGuard_holds():
    assert fsm_EqualNumberGuard.holds(fsm_EqualNumberGuard()) == None


from python_code import fsm_GreaterThanNumberGuard

def test_fsm_GreaterThanNumberGuard___init__():
    assert fsm_GreaterThanNumberGuard.__init__(fsm_GreaterThanNumberGuard()) == None

def test_fsm_GreaterThanNumberGuard_holds():
    assert fsm_GreaterThanNumberGuard.holds(fsm_GreaterThanNumberGuard()) == None


from python_code import fsm_IncreaseValueAction

def test_fsm_IncreaseValueAction___init__():
    assert fsm_IncreaseValueAction.__init__(fsm_IncreaseValueAction(0), 0) == None

def test_fsm_IncreaseValueAction_execute():
    assert fsm_IncreaseValueAction.execute(fsm_IncreaseValueAction(0)) == None


from python_code import fsm_LessThanNumberGuard

def test_fsm_LessThanNumberGuard___init__():
    assert fsm_LessThanNumberGuard.__init__(fsm_LessThanNumberGuard()) == None

def test_fsm_LessThanNumberGuard_holds():
    assert fsm_LessThanNumberGuard.holds(fsm_LessThanNumberGuard()) == None


from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None

