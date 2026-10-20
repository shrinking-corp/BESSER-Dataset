from python_code import ActiveRecord
from python_code import ConnectionInterface_Interface

def test_ActiveRecord___init__():
    assert ActiveRecord.__init__(ActiveRecord(ConnectionInterface_Interface(), 0), ConnectionInterface_Interface(), 0) == None


from python_code import Car

def test_Car___init__():
    assert Car.__init__(Car('\x00\x00', '', 0, ''), '', '', 0, '') == None


from python_code import RepairPart

def test_RepairPart___init__():
    assert RepairPart.__init__(RepairPart('', 0, '\x00\x00'), '', 0, '') == None

