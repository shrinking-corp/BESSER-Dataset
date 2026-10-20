from python_code import Door_relay

def test_Door_relay___init__():
    assert Door_relay.__init__(Door_relay(0, '\x00'), 0, '\x00') == None


from python_code import FireAlarm_Sensor

def test_FireAlarm_Sensor___init__():
    assert FireAlarm_Sensor.__init__(FireAlarm_Sensor(False, False), False, False) == None


from python_code import MQTT_Broker

def test_MQTT_Broker___init__():
    assert MQTT_Broker.__init__(MQTT_Broker(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Modbus_Meter

def test_Modbus_Meter___init__():
    assert Modbus_Meter.__init__(Modbus_Meter(0), 0) == None


from python_code import OPC_UA

def test_OPC_UA___init__():
    assert OPC_UA.__init__(OPC_UA(0), 0) == None


from python_code import UPS_SNMP

def test_UPS_SNMP___init__():
    assert UPS_SNMP.__init__(UPS_SNMP(''), '') == None

