from python_code import tracker_BovineBeef

def test_tracker_BovineBeef___init__():
    assert tracker_BovineBeef.__init__(tracker_BovineBeef(''), '') == None


from python_code import tracker_BovineBison

def test_tracker_BovineBison___init__():
    assert tracker_BovineBison.__init__(tracker_BovineBison(''), '') == None


from python_code import tracker_BovineDairy

def test_tracker_BovineDairy___init__():
    assert tracker_BovineDairy.__init__(tracker_BovineDairy(''), '') == None


from python_code import tracker_FairRegistration

def test_tracker_FairRegistration___init__():
    assert tracker_FairRegistration.__init__(tracker_FairRegistration('', '', '', '', ''), '', '', '', '', '') == None


from python_code import tracker_MovedIn

def test_tracker_MovedIn___init__():
    assert tracker_MovedIn.__init__(tracker_MovedIn(''), '') == None


from python_code import tracker_MovedOut

def test_tracker_MovedOut___init__():
    assert tracker_MovedOut.__init__(tracker_MovedOut(''), '') == None


from python_code import tracker_Ovine

def test_tracker_Ovine___init__():
    assert tracker_Ovine.__init__(tracker_Ovine(''), '') == None


from python_code import tracker_Animals
from python_code import tracker_EventHistory
from python_code import tracker_Premises
from python_code import tracker_UnAppliedTags

def test_tracker_Premises___init__():
    assert tracker_Premises.__init__(tracker_Premises('', '\x00', tracker_Premises=tracker_Animals(), tracker_Premises5=tracker_EventHistory(), tracker_Premises7=tracker_UnAppliedTags()), '\x00\x00', '', tracker_Premises=tracker_Animals(), tracker_Premises5=tracker_EventHistory(), tracker_Premises7=tracker_UnAppliedTags()) == None


from python_code import tracker_ReplacedTag

def test_tracker_ReplacedTag___init__():
    assert tracker_ReplacedTag.__init__(tracker_ReplacedTag(''), '') == None


from python_code import tracker_Swine

def test_tracker_Swine___init__():
    assert tracker_Swine.__init__(tracker_Swine(''), '') == None


from python_code import tracker_WeighIn

def test_tracker_WeighIn___init__():
    assert tracker_WeighIn.__init__(tracker_WeighIn(0), 0) == None

