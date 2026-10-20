from python_code import edd_Diagram
from python_code import edd_Model

def test_edd_Model___init__():
    assert edd_Model.__init__(edd_Model('', edd_Model=edd_Diagram(), edd_Model2=set()), '', edd_Model=edd_Diagram(), edd_Model2=set()) == None

