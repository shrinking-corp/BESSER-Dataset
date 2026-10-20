from python_code import ioT_Address
from python_code import ioT_ConnectStatement

def test_ioT_Address___init__():
    assert ioT_Address.__init__(ioT_Address('', ioT_Address=ioT_ConnectStatement()), '', ioT_Address=ioT_ConnectStatement()) == None


from python_code import ioT_ComparisonOp
from python_code import ioT_EQL

def test_ioT_ComparisonOp___init__():
    assert ioT_ComparisonOp.__init__(ioT_ComparisonOp('', ioT_ComparisonOp=ioT_EQL()), '', ioT_ComparisonOp=ioT_EQL()) == None


from python_code import ioT_Config
from python_code import ioT_Model

def test_ioT_Config___init__():
    assert ioT_Config.__init__(ioT_Config('', ioT_Config6=set(), ioT_Config=ioT_Model()), '', ioT_Config6=set(), ioT_Config=ioT_Model()) == None


from python_code import ioT_ConnectStatement
from python_code import ioT_ConnectionConfig
from python_code import ioT_WifiStatement

def test_ioT_ConnectionConfig___init__():
    assert ioT_ConnectionConfig.__init__(ioT_ConnectionConfig('', ioT_ConnectionConfig30=ioT_ConnectStatement(), ioT_ConnectionConfig=ioT_WifiStatement()), '', ioT_ConnectionConfig30=ioT_ConnectStatement(), ioT_ConnectionConfig=ioT_WifiStatement()) == None


from python_code import ioT_ConnectStatement
from python_code import ioT_Device
from python_code import ioT_Model
from python_code import ioT_Program
from python_code import ioT_ReadConnection
from python_code import ioT_SendCommand

def test_ioT_Device___init__():
    assert ioT_Device.__init__(ioT_Device('', ioT_Device8=ioT_Program(), ioT_Device=ioT_Model(), ioT_Device25=ioT_ConnectStatement(), ioT_Device40=ioT_ReadConnection(), ioT_Device68=ioT_SendCommand()), '', ioT_Device8=ioT_Program(), ioT_Device=ioT_Model(), ioT_Device25=ioT_ConnectStatement(), ioT_Device40=ioT_ReadConnection(), ioT_Device68=ioT_SendCommand()) == None


from python_code import ioT_ExternalDeclaration
from python_code import ioT_ExternalOf
from python_code import ioT_ExternalRight
from python_code import ioT_Model

def test_ioT_ExternalDeclaration___init__():
    assert ioT_ExternalDeclaration.__init__(ioT_ExternalDeclaration('', ioT_ExternalDeclaration=ioT_Model(), ioT_ExternalDeclaration42=ioT_ExternalOf(), ioT_ExternalDeclaration50=ioT_ExternalRight()), '', ioT_ExternalDeclaration=ioT_Model(), ioT_ExternalDeclaration42=ioT_ExternalOf(), ioT_ExternalDeclaration50=ioT_ExternalRight()) == None


from python_code import ioT_IntExpression

def test_ioT_IntExpression___init__():
    assert ioT_IntExpression.__init__(ioT_IntExpression(0), 0) == None


from python_code import ioT_ItemInt

def test_ioT_ItemInt___init__():
    assert ioT_ItemInt.__init__(ioT_ItemInt(0), 0) == None


from python_code import ioT_LEDAction

def test_ioT_LEDAction___init__():
    assert ioT_LEDAction.__init__(ioT_LEDAction(''), '') == None


from python_code import ioT_ExpressionRight
from python_code import ioT_ListenStatement
from python_code import ioT_Program

def test_ioT_ListenStatement___init__():
    assert ioT_ListenStatement.__init__(ioT_ListenStatement('', 0, ioT_ListenStatement=ioT_Program(), ioT_ListenStatement20=ioT_ExpressionRight()), '', 0, ioT_ListenStatement=ioT_Program(), ioT_ListenStatement20=ioT_ExpressionRight()) == None


from python_code import ioT_ExternalOf
from python_code import ioT_Program
from python_code import ioT_VarAccess
from python_code import ioT_VarOrList

def test_ioT_VarOrList___init__():
    assert ioT_VarOrList.__init__(ioT_VarOrList('', ioT_VarOrList=ioT_Program(), ioT_VarOrList45=ioT_ExternalOf(), ioT_VarOrList62=ioT_VarAccess()), '', ioT_VarOrList=ioT_Program(), ioT_VarOrList45=ioT_ExternalOf(), ioT_VarOrList62=ioT_VarAccess()) == None

