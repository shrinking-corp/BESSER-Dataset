from python_code import mngr_ManagedElement
from python_code import mngr_Manager

def test_mngr_ManagedElement___init__():
    assert mngr_ManagedElement.__init__(mngr_ManagedElement('', ManagedElement=mngr_Manager(), managedElement=mngr_Manager()), '', ManagedElement=mngr_Manager(), managedElement=mngr_Manager()) == None

