from python_code import SBCS_Pump
from python_code import SBCS_PumpControler

def test_SBCS_Pump___init__():
    assert SBCS_Pump.__init__(SBCS_Pump('', SBCS_Pump=SBCS_PumpControler()), '', SBCS_Pump=SBCS_PumpControler()) == None

