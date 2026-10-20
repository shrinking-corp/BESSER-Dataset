from python_code import ftp_AnalogBattery
from python_code import ftp_ElectricalPort

def test_ftp_AnalogBattery___init__():
    assert ftp_AnalogBattery.__init__(ftp_AnalogBattery(0.0, ftp_AnalogBattery=ftp_ElectricalPort(), ftp_AnalogBattery34=ftp_ElectricalPort()), 0.0, ftp_AnalogBattery=ftp_ElectricalPort(), ftp_AnalogBattery34=ftp_ElectricalPort()) == None


from python_code import ftp_ElectricalValue

def test_ftp_ElectricalValue___init__():
    assert ftp_ElectricalValue.__init__(ftp_ElectricalValue(0.0, 0.0, False, True), 0.0, 0.0, False, True) == None


from python_code import ftp_Fault

def test_ftp_Fault___init__():
    assert ftp_Fault.__init__(ftp_Fault(''), '') == None


from python_code import ftp_FloatValue

def test_ftp_FloatValue___init__():
    assert ftp_FloatValue.__init__(ftp_FloatValue(0.0), 0.0) == None


from python_code import ftp_HydraulicValue

def test_ftp_HydraulicValue___init__():
    assert ftp_HydraulicValue.__init__(ftp_HydraulicValue(False, 0.0, 0.0, False), True, 0.0, 0.0, True) == None


from python_code import ftp_ComposedComponent
from python_code import ftp_Connection
from python_code import ftp_Port
from python_code import ftp_PortValue

def test_ftp_Port___init__():
    assert ftp_Port.__init__(ftp_Port('', '\x00', ftp_Port=ftp_Connection(), ftp_Port17=ftp_Connection(), ftp_Port24=ftp_PortValue(), ftp_Port21=ftp_ComposedComponent()), '\x00\x00', '', ftp_Port=ftp_Connection(), ftp_Port17=ftp_Connection(), ftp_Port24=ftp_PortValue(), ftp_Port21=ftp_ComposedComponent()) == None

def test_ftp_Port_newPortValue():
    assert ftp_Port.newPortValue(ftp_Port('', '', ftp_Port=ftp_Connection(), ftp_Port17=ftp_Connection(), ftp_Port24=ftp_PortValue(), ftp_Port21=ftp_ComposedComponent())) == None


from python_code import ftp_ElectricalPort
from python_code import ftp_Resistor

def test_ftp_Resistor___init__():
    assert ftp_Resistor.__init__(ftp_Resistor(0.0, ftp_Resistor=ftp_ElectricalPort(), ftp_Resistor29=ftp_ElectricalPort()), 0.0, ftp_Resistor=ftp_ElectricalPort(), ftp_Resistor29=ftp_ElectricalPort()) == None


from python_code import ftp_RootEvent

def test_ftp_RootEvent___init__():
    assert ftp_RootEvent.__init__(ftp_RootEvent('', ftp_RootEvent=set()), '', ftp_RootEvent=set()) == None


from python_code import ftp_SignalConstant
from python_code import ftp_SignalPort

def test_ftp_SignalConstant___init__():
    assert ftp_SignalConstant.__init__(ftp_SignalConstant('', ftp_SignalConstant=ftp_SignalPort()), '', ftp_SignalConstant=ftp_SignalPort()) == None


from python_code import ftp_SignalValue

def test_ftp_SignalValue___init__():
    assert ftp_SignalValue.__init__(ftp_SignalValue(''), '') == None


from python_code import ftp_VisualValue

def test_ftp_VisualValue___init__():
    assert ftp_VisualValue.__init__(ftp_VisualValue(''), '') == None

