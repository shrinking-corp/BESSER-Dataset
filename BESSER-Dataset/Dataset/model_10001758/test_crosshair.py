from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee(0, '', 0, '', '', '', ''), 0, '\x00', 0, '', '', '', '') == None


from python_code import Nurse
from python_code import Room

def test_Room___init__():
    assert Room.__init__(Room('', 0, '', patient5=set(), nurse7=Nurse()), '', 0, '', patient5=set(), nurse7=Nurse()) == None


from python_code import patient

def test_patient___init__():
    assert patient.__init__(patient(0, '', '', 0, '', '', '', doctor1=set(), receiptionist3=set(), room4=set()), 0, '\x00', '', 0, '', '', '', doctor1=set(), receiptionist3=set(), room4=set()) == None

