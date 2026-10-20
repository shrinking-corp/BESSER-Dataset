from python_code import Package2_Allowance

def test_Package2_Allowance___init__():
    assert Package2_Allowance.__init__(Package2_Allowance(0, '', '', Allowance_Employee_086=set()), 0, '', '', Allowance_Employee_086=set()) == None


from python_code import Package2_Deductions

def test_Package2_Deductions___init__():
    assert Package2_Deductions.__init__(Package2_Deductions('', '\x00'), '\x00\x00', '') == None


from python_code import Package2_EPF
from python_code import Package2_UserUpdates

def test_Package2_EPF___init__():
    assert Package2_EPF.__init__(Package2_EPF(0, 0, Package2_UserUpdates()), 0, 0, Package2_UserUpdates()) == None


from python_code import Package2_EmployeeParoll

def test_Package2_EmployeeParoll___init__():
    assert Package2_EmployeeParoll.__init__(Package2_EmployeeParoll(0, 0, 0, 0, 0, 0, 0, '', Employee_EmployeeParoll_197=set()), 0, 0, 0, 0, 0, 0, 0, '', Employee_EmployeeParoll_197=set()) == None


from python_code import Package2_Shifts

def test_Package2_Shifts___init__():
    assert Package2_Shifts.__init__(Package2_Shifts('', '', '', '', Employee_Shifts_181=set()), '', '', '', '', Employee_Shifts_181=set()) == None


from python_code import Package_Allowance

def test_Package_Allowance___init__():
    assert Package_Allowance.__init__(Package_Allowance(0, '', '', Allowance_Employee_056=set()), 0, '', '', Allowance_Employee_056=set()) == None


from python_code import Package_Deductions

def test_Package_Deductions___init__():
    assert Package_Deductions.__init__(Package_Deductions('', '\x00'), '\x00\x00', '') == None


from python_code import Package_EPF
from python_code import Package_UserUpdates

def test_Package_EPF___init__():
    assert Package_EPF.__init__(Package_EPF(0, 0, Package_UserUpdates()), 0, 0, Package_UserUpdates()) == None


from python_code import Package_EmployeeParoll

def test_Package_EmployeeParoll___init__():
    assert Package_EmployeeParoll.__init__(Package_EmployeeParoll('\x00\x00', '', Employee_EmployeeParoll_167=set()), '', '', Employee_EmployeeParoll_167=set()) == None


from python_code import Package_Shifts

def test_Package_Shifts___init__():
    assert Package_Shifts.__init__(Package_Shifts('\x00\x00', '', Employee_Shifts_151=set()), '', '', Employee_Shifts_151=set()) == None

