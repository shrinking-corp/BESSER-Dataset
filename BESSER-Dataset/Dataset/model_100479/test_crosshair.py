from python_code import tfsm_EvaluateGuard

def test_tfsm_EvaluateGuard___init__():
    assert tfsm_EvaluateGuard.__init__(tfsm_EvaluateGuard(''), '') == None

def test_tfsm_EvaluateGuard_evaluate():
    assert tfsm_EvaluateGuard.evaluate(tfsm_EvaluateGuard('')) == None


from python_code import tfsm_NamedElement

def test_tfsm_NamedElement___init__():
    assert tfsm_NamedElement.__init__(tfsm_NamedElement(''), '') == None


from python_code import tfsm_TimedSystem

def test_tfsm_TimedSystem___init__():
    assert tfsm_TimedSystem.__init__(tfsm_TimedSystem(tfsm_TimedSystem=set(), tfsm_TimedSystem34=set(), tfsm_TimedSystem37=set()), tfsm_TimedSystem=set(), tfsm_TimedSystem34=set(), tfsm_TimedSystem37=set()) == None

def test_tfsm_TimedSystem_init():
    assert tfsm_TimedSystem.init(tfsm_TimedSystem(tfsm_TimedSystem=set(), tfsm_TimedSystem34=set(), tfsm_TimedSystem37=set())) == None

