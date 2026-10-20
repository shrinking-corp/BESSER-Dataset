from python_code import SmartHome_Activator

def test_SmartHome_Activator___init__():
    assert SmartHome_Activator.__init__(SmartHome_Activator()) == None

def test_SmartHome_Activator_activate():
    assert SmartHome_Activator.activate(SmartHome_Activator()) == None


from python_code import SmartHome_AnalValue

def test_SmartHome_AnalValue___init__():
    assert SmartHome_AnalValue.__init__(SmartHome_AnalValue(True), False) == None


from python_code import SmartHome_DigitValue

def test_SmartHome_DigitValue___init__():
    assert SmartHome_DigitValue.__init__(SmartHome_DigitValue(0.0), 0.0) == None


from python_code import SmartHome_Home

def test_SmartHome_Home___init__():
    assert SmartHome_Home.__init__(SmartHome_Home(0.0, 0.0, SmartHome_Home=set(), SmartHome_Home14=set()), 0.0, 0.0, SmartHome_Home=set(), SmartHome_Home14=set()) == None


from python_code import SmartHome_Light
from python_code import SmartHome_Room

def test_SmartHome_Light___init__():
    assert SmartHome_Light.__init__(SmartHome_Light(False, 0.0, SmartHome_Light=SmartHome_Room()), False, 0.0, SmartHome_Light=SmartHome_Room()) == None


from python_code import SmartHome_NamedElement

def test_SmartHome_NamedElement___init__():
    assert SmartHome_NamedElement.__init__(SmartHome_NamedElement(''), '') == None


from python_code import SmartHome_PhysicalContext
from python_code import SmartHome_Room

def test_SmartHome_PhysicalContext___init__():
    assert SmartHome_PhysicalContext.__init__(SmartHome_PhysicalContext(0.0, 0.0, SmartHome_PhysicalContext=SmartHome_Room()), 0.0, 0.0, SmartHome_PhysicalContext=SmartHome_Room()) == None


from python_code import SmartHome_IotComponent
from python_code import SmartHome_Rule
from python_code import SmartHome_RuleComposant
from python_code import SmartHome_Value

def test_SmartHome_RuleComposant___init__():
    assert SmartHome_RuleComposant.__init__(SmartHome_RuleComposant('', SmartHome_RuleComposant=SmartHome_Rule(), SmartHome_RuleComposant20=SmartHome_Rule(), SmartHome_RuleComposant22=SmartHome_Value(), SmartHome_RuleComposant24=SmartHome_IotComponent()), '', SmartHome_RuleComposant=SmartHome_Rule(), SmartHome_RuleComposant20=SmartHome_Rule(), SmartHome_RuleComposant22=SmartHome_Value(), SmartHome_RuleComposant24=SmartHome_IotComponent()) == None


from python_code import SmartHome_Room
from python_code import SmartHome_Shutter

def test_SmartHome_Shutter___init__():
    assert SmartHome_Shutter.__init__(SmartHome_Shutter(True, SmartHome_Shutter=SmartHome_Room()), False, SmartHome_Shutter=SmartHome_Room()) == None

