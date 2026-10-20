from python_code import syswbeff106_Flow
from python_code import syswbeff106_Item

def test_syswbeff106_Item___init__():
    assert syswbeff106_Item.__init__(syswbeff106_Item('', syswbeff106_Item=syswbeff106_Flow()), '', syswbeff106_Item=syswbeff106_Flow()) == None


from python_code import syswbeff106_Port

def test_syswbeff106_Port___init__():
    assert syswbeff106_Port.__init__(syswbeff106_Port(''), '') == None


from python_code import syswbeff106_ProcessNode

def test_syswbeff106_ProcessNode___init__():
    assert syswbeff106_ProcessNode.__init__(syswbeff106_ProcessNode(''), '') == None


from python_code import syswbeff106_System
from python_code import syswbeff106_Workbench

def test_syswbeff106_Workbench___init__():
    assert syswbeff106_Workbench.__init__(syswbeff106_Workbench('', syswbeff106_Workbench=set(), syswbeff106_Workbench62=set(), syswbeff106_Workbench65=syswbeff106_System(), syswbeff106_Workbench68=set(), syswbeff106_Workbench71=set()), '', syswbeff106_Workbench=set(), syswbeff106_Workbench62=set(), syswbeff106_Workbench65=syswbeff106_System(), syswbeff106_Workbench68=set(), syswbeff106_Workbench71=set()) == None

