#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    ActuatorType,
    Bridge,
    CommunicationType,
    ControllerType,
    DBType,
    Data,
    Device,
    Enum,
    MessageBrokerType,
    Port,
    PortType,
    SensorType,
    Server,
    abstractmethod,
    date,
    datetime,
    time,
    wsmodel3_AccesPoint,
    wsmodel3_Actuator,
    wsmodel3_Break,
    wsmodel3_Bridge,
    wsmodel3_Communication,
    wsmodel3_CommunicationData,
    wsmodel3_Controller,
    wsmodel3_DBServer,
    wsmodel3_Data,
    wsmodel3_Device,
    wsmodel3_DeviceData,
    wsmodel3_ExternalAPI,
    wsmodel3_Function,
    wsmodel3_InputBridge,
    wsmodel3_InputOrchestrator,
    wsmodel3_InputPort,
    wsmodel3_IntegrationPattern,
    wsmodel3_IoTNode,
    wsmodel3_MessageBroker,
    wsmodel3_Orchestrator,
    wsmodel3_OrchestratorData,
    wsmodel3_OutputBridge,
    wsmodel3_OutputOrchestrator,
    wsmodel3_OutputPort,
    wsmodel3_Port,
    wsmodel3_REST,
    wsmodel3_Sensor,
    wsmodel3_Server,
    wsmodel3_System,
    wsmodel3_WebServer,
    wsmodel3_WebService,
)


def test_0():
    var_33 = "eK8X"
    var_34 = python_code_.wsmodel3_Function(
        expression=var_33,
        wsmodel3_Function69=var_33,
        wsmodel3_Function75={131.69, "?>YV?sMM\tu:g", 2260.83},
    )
    assert isinstance(var_34, python_code_.wsmodel3_Function)


def test_1():
    var_33 = "eK8X3"
    var_34 = python_code_.wsmodel3_Function(expression=var_33)
    assert isinstance(var_34, python_code_.wsmodel3_Function)


def test_2():
    var_0 = python_code_.DBType.Undefined
    var_1 = python_code_.wsmodel3_Break(expression=var_0)
    var_3 = "wsmodel3_InputBridge._wsmodel3_Actuator__wsmodel3_Actuator42._wsmodel3_Communication__wsmodel3_Communication35"
    var_4 = python_code_.ActuatorType
    var_5 = {var_1, var_1}
    var_6 = python_code_.wsmodel3_Function(
        expression=var_3,
        wsmodel3_Function72=var_4,
        wsmodel3_Function75=var_5,
        wsmodel3_Function=-582,
    )
    assert isinstance(var_6, python_code_.wsmodel3_Function)
    var_34 = "1AM}\x0bM&~8H\\|l[\n\r"
    var_35 = python_code_.wsmodel3_Actuator(type=var_34, wsmodel3_Actuator42={-1})
    assert isinstance(var_35, python_code_.wsmodel3_Actuator)
    var_43 = -1904
    python_code_.wsmodel3_REST(URI=var_3, port=var_43)


def test_3():
    var_15 = "_wsmodel3_Bridge__wsmodel3_Bridge:Hum_dityG:wsmodel3_System6"
    python_code_.wsmodel3_Break(expression=var_15)


@pytest.mark.xfail(strict=True)
def test_4():
    var_26 = "_wsmodel3_InputBridge__wsmodel3_InputBridge"
    var_27 = "_wsmodel3_InputOrchestrator__wsmodel3_InputOrchestrator70wsmodel3_IntegrationPattern51"
    var_28 = -350
    var_29 = python_code_.wsmodel3_Bridge(
        topic=var_27, host=var_26, port=var_28, wsmodel3_Bridge49=None
    )
    assert isinstance(var_29, python_code_.wsmodel3_Bridge)
    python_code_.wsmodel3_REST(URI=None, port=False, wsmodel3_REST40=var_29)


def test_5():
    var_0 = "TiL)"
    python_code_.wsmodel3_System(
        name=var_0, wsmodel3_System6=set(), wsmodel3_System={-1536.54, -1664.88}
    )
    var_22 = python_code_.Port
    var_23 = python_code_.wsmodel3_Bridge(topic=var_22, host=var_0, port=True)
    assert isinstance(var_23, python_code_.wsmodel3_Bridge)


def test_6():
    var_0 = "hTiL)"
    var_2 = python_code_.wsmodel3_Orchestrator(
        port=var_0,
        name=var_0,
        wsmodel3_Orchestrator=var_0,
        wsmodel3_Orchestrator61=set(),
        wsmodel3_Orchestrator66=set(),
    )
    assert isinstance(var_2, python_code_.wsmodel3_Orchestrator)
    python_code_.wsmodel3_System(name=var_0)
    python_code_.wsmodel3_InputOrchestrator(URI=var_0)


def test_7():
    var_1 = "sv\r(3d8M\\Q@}]1"
    var_2 = python_code_.Data
    var_3 = python_code_.wsmodel3_Orchestrator(
        port=var_1, name=var_2, wsmodel3_Orchestrator66={}
    )
    assert isinstance(var_3, python_code_.wsmodel3_Orchestrator)
    var_5 = "\rW6y?_"
    python_code_.wsmodel3_Communication(type=var_2, name=var_5)
    python_code_.wsmodel3_ExternalAPI(URI="i!):x`n\r~`Gy\rI'in")


def test_8():
    var_0 = {}
    python_code_.wsmodel3_InputOrchestrator(URI=var_0, wsmodel3_InputOrchestrator=var_0)


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.DBType.Undefined
    var_1 = python_code_.wsmodel3_Break(expression=var_0)
    var_34 = "wsmodel3_InputBridge._wsmodel3_Actuator__wsmodel3_Actuator42._wsmodel3_Communication__wsmodel3_Communication35"
    var_35 = python_code_.ActuatorType
    var_36 = {var_1}
    var_37 = python_code_.wsmodel3_Function(
        expression=var_34,
        wsmodel3_Function72=var_35,
        wsmodel3_Function75=var_36,
        wsmodel3_Function=-582,
    )
    assert isinstance(var_37, python_code_.wsmodel3_Function)
    python_code_.wsmodel3_InputOrchestrator(
        URI=var_35, wsmodel3_InputOrchestrator70=var_37
    )


def test_10():
    var_0 = "hTiL)"
    python_code_.wsmodel3_InputOrchestrator(URI=var_0, wsmodel3_InputOrchestrator=var_0)
    var_27 = python_code_.wsmodel3_OutputOrchestrator()
    python_code_.wsmodel3_InputOrchestrator(
        URI=var_0,
        wsmodel3_InputOrchestrator78=var_27,
        wsmodel3_InputOrchestrator57=var_0,
    )


def test_11():
    var_0 = "hTiL)"
    python_code_.wsmodel3_InputOrchestrator(URI=var_0)


@pytest.mark.xfail(strict=True)
def test_12():
    var_18 = "1AM}\x0bM&~8OH\\|l[\n\r"
    var_19 = python_code_.wsmodel3_Actuator(type=var_18, wsmodel3_Actuator42={-1})
    assert isinstance(var_19, python_code_.wsmodel3_Actuator)
    var_20 = "wsmodel3_Orchestrator59"
    python_code_.wsmodel3_ExternalAPI(URI="i!):x`n\r~`Gy\rI'in")
    var_30 = python_code_.wsmodel3_MessageBroker
    var_31 = python_code_.wsmodel3_Bridge(topic=var_20, host=var_30, port=var_30)
    assert isinstance(var_31, python_code_.wsmodel3_Bridge)
    python_code_.wsmodel3_InputBridge(
        URI=var_20, wsmodel3_InputBridge=var_19, wsmodel3_InputBridge81=-2509
    )


def test_13():
    var_13 = "uGq[+=*_l`4@PJMr%\tX"
    var_14 = python_code_.wsmodel3_InputBridge(URI=var_13)
    assert isinstance(var_14, python_code_.wsmodel3_InputBridge)


def test_14():
    var_0 = python_code_.CommunicationType.Serial
    var_1 = "EwT"
    var_2 = python_code_.wsmodel3_Break(expression=468.34)
    var_3 = {var_2}
    var_4 = python_code_.wsmodel3_Function(
        expression=var_1, wsmodel3_Function69=var_0, wsmodel3_Function75=var_3
    )
    assert isinstance(var_4, python_code_.wsmodel3_Function)
    var_5 = python_code_.wsmodel3_Break(expression=var_1, wsmodel3_Break=var_4)
    assert isinstance(var_5, python_code_.wsmodel3_Break)
    var_8 = python_code_.wsmodel3_Port(id=4161, type=var_1)
    assert isinstance(var_8, python_code_.wsmodel3_Port)
    var_10 = "_wsmodel3_Controller__wsmodel3_Controller"
    python_code_.wsmodel3_Function(expression=var_10)
    python_code_.wsmodel3_InputOrchestrator(URI=var_10)
    var_46 = -1904
    python_code_.wsmodel3_REST(URI=var_10, port=var_46)
    var_48 = python_code_.wsmodel3_Port
    var_49 = python_code_.wsmodel3_InputBridge(URI=var_48, wsmodel3_InputBridge=-661.39)
    assert isinstance(var_49, python_code_.wsmodel3_InputBridge)
    var_50 = python_code_.wsmodel3_Controller(type=b"\xd7\xf8\xba\x13\x82\xe4")
    assert isinstance(var_50, python_code_.wsmodel3_Controller)


def test_15():
    var_1 = set()
    var_5 = python_code_.wsmodel3_InputBridge(URI=var_1, wsmodel3_InputBridge81=[])
    assert isinstance(var_5, python_code_.wsmodel3_InputBridge)
    var_13 = python_code_.wsmodel3_Sensor(type=var_5, wsmodel3_Sensor46=var_1)
    assert isinstance(var_13, python_code_.wsmodel3_Sensor)


def test_16():
    var_0 = "|:[\nww|-h"
    var_1 = set()
    var_2 = str
    python_code_.wsmodel3_Communication(
        type=var_0,
        name=var_0,
        wsmodel3_Communication=var_0,
        wsmodel3_Communication30=var_1,
        wsmodel3_Communication35=var_2,
    )
    var_4 = python_code_.wsmodel3_Port(id=var_2, type={})
    assert isinstance(var_4, python_code_.wsmodel3_Port)
    var_5 = python_code_.wsmodel3_InputBridge(URI=var_1, wsmodel3_InputBridge81=[])
    assert isinstance(var_5, python_code_.wsmodel3_InputBridge)
    python_code_.wsmodel3_InputBridge(
        URI="_wsmodel3_AccesPoint__wsmodel3_AccesPoint33,_wsmodel3_AccesPoint__wsmodel3_AccesPoint33"
    )


def test_17():
    var_2 = python_code_.Data
    var_5 = "\rW6y?_"
    python_code_.wsmodel3_Communication(type=var_2, name=var_5)
    python_code_.wsmodel3_ExternalAPI(URI="i!):x`n\r~`Gy\rI'in")


def test_18():
    var_1 = '%bdz$_o"E\x0b`,c;'
    var_2 = "z\x0bu^g<L7c\ti"
    var_3 = python_code_.wsmodel3_Communication(
        type=var_1, name=var_2, wsmodel3_Communication32={3, 1, 1680}
    )
    var_4 = "1AM}\x0bM&~8OH\\|l[\n\r"
    var_5 = python_code_.wsmodel3_Actuator(type=var_4, wsmodel3_Actuator42={-1})
    assert isinstance(var_5, python_code_.wsmodel3_Actuator)
    var_6 = "wsmodel3_Orchestrator59"
    python_code_.wsmodel3_ExternalAPI(
        URI=var_6, wsmodel3_ExternalAPI=var_3, wsmodel3_ExternalAPI89=var_2
    )
    python_code_.wsmodel3_ExternalAPI(URI=var_1, wsmodel3_ExternalAPI89=var_2)
    var_10 = python_code_.wsmodel3_MessageBroker
    var_11 = python_code_.wsmodel3_Bridge(topic=var_1, host=var_10, port=var_10)
    assert isinstance(var_11, python_code_.wsmodel3_Bridge)
    python_code_.wsmodel3_InputOrchestrator(
        URI=var_6, wsmodel3_InputOrchestrator=var_11
    )


def test_19():
    var_1 = '%bdz$_o"E\x0b`,c;'
    var_2 = "z\x0bu^g<L7c\ti"
    var_3 = python_code_.wsmodel3_Communication(
        type=var_1, name=var_2, wsmodel3_Communication32={3, 1, 1680}
    )
    var_6 = "wsmodel3_Orchestrator59"
    python_code_.wsmodel3_ExternalAPI(
        URI=var_6, wsmodel3_ExternalAPI=var_3, wsmodel3_ExternalAPI89=var_2
    )
    var_8 = python_code_.wsmodel3_ExternalAPI(URI=var_1, wsmodel3_ExternalAPI89=var_2)
    python_code_.wsmodel3_InputOrchestrator(
        URI="_wsmodel3_Orchestrator__wsmodel3_Orchestrator56-wsmodel3_Orchestrator-Vibration-wsmodel3_WebService16",
        wsmodel3_InputOrchestrator=var_8,
    )


def test_20():
    var_13 = python_code_.SensorType.CO2
    var_20 = python_code_.wsmodel3_Port(
        id=var_13, type=None, wsmodel3_Port=[False, "F|\x0ct"]
    )
    assert isinstance(var_20, python_code_.wsmodel3_Port)


def test_21():
    var_0 = "hTiL)"
    python_code_.wsmodel3_System(name=var_0)
    python_code_.wsmodel3_InputOrchestrator(URI=var_0)
    var_24 = -1904
    var_25 = python_code_.wsmodel3_REST(URI=var_0, port=var_24)
    var_26 = python_code_.wsmodel3_Port(id=var_25, type=var_0)
    assert isinstance(var_26, python_code_.wsmodel3_Port)


def test_22():
    var_32 = python_code_.wsmodel3_Actuator(type="4;F\n#_l< >ge\nUm @(R")
    assert isinstance(var_32, python_code_.wsmodel3_Actuator)


def test_23():
    python_code_.wsmodel3_Break(expression=complex(-403.5, -1570.7782))
    var_18 = "1AM}\x0bM&~8OH\\|l[\n\r"
    var_19 = python_code_.wsmodel3_Actuator(type=var_18, wsmodel3_Actuator42={-1})
    assert isinstance(var_19, python_code_.wsmodel3_Actuator)
    var_23 = python_code_.wsmodel3_MessageBroker
    var_24 = python_code_.wsmodel3_Bridge(topic=var_18, host=var_23, port=var_23)
    assert isinstance(var_24, python_code_.wsmodel3_Bridge)


def test_24():
    var_7 = python_code_.wsmodel3_Sensor(
        type="wsmodel3_IntegrationPattern51:_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI89"
    )
    assert isinstance(var_7, python_code_.wsmodel3_Sensor)
    var_19 = python_code_.wsmodel3_OutputPort()
    var_20 = python_code_.wsmodel3_Actuator(
        type=complex(807.8539, -2156.0312744), wsmodel3_Actuator=var_19
    )
    assert isinstance(var_20, python_code_.wsmodel3_Actuator)


def test_25():
    var_25 = python_code_.wsmodel3_IoTNode()
    var_29 = python_code_.wsmodel3_Sensor(
        type="wsmodel3_IntegrationPattern51:_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI89"
    )
    assert isinstance(var_29, python_code_.wsmodel3_Sensor)
    var_30 = set()
    var_31 = python_code_.wsmodel3_Controller(
        type=var_25, wsmodel3_Controller=var_30, wsmodel3_Controller28=var_30
    )
    assert isinstance(var_31, python_code_.wsmodel3_Controller)


def test_26():
    var_5 = python_code_.wsmodel3_Port(
        id="s",
        type="_wsmodel3_Server__wsmodel3_Server_wsmodel3_Function__wsmodel3_Function",
    )
    assert isinstance(var_5, python_code_.wsmodel3_Port)
    var_8 = "_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI _wsmodel3_Actuator__wsmodel3_Actuator wsmodel3_OutputPort"
    var_9 = python_code_.wsmodel3_Actuator(type=var_8)
    assert isinstance(var_9, python_code_.wsmodel3_Actuator)
    var_13 = -180
    var_14 = python_code_.wsmodel3_DBServer(
        database="^!svF<9QS2ARS=@",
        usser=var_8,
        pass_="_wsmodel3_AccesPoint__wsmodel3_AccesPoint:_wsmodel3_DBServer__wsmodel3_DBServer",
        type="cg]a.xE`R8F\x0b",
        port=var_13,
    )
    assert isinstance(var_14, python_code_.wsmodel3_DBServer)
    var_21 = python_code_.wsmodel3_Controller(type="lv|0p")
    assert isinstance(var_21, python_code_.wsmodel3_Controller)


def test_27():
    python_code_.wsmodel3_System(
        name="Analog", wsmodel3_System2=set(), wsmodel3_System4={658.45, -467.93}
    )


def test_28():
    python_code_.wsmodel3_System(
        name="wsmodel3_ExternalAPI64", wsmodel3_System10=set(), wsmodel3_System12=set()
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = python_code_.PortType.Analog
    var_20 = "wsmodel3_Orchestrator59"
    python_code_.wsmodel3_ExternalAPI(URI="i!):x`n\r~`Gy\rI'in")
    var_36 = 4448
    var_37 = python_code_.wsmodel3_OutputOrchestrator()
    var_38 = python_code_.wsmodel3_REST(URI=var_20, port=var_0, wsmodel3_REST86=var_37)
    var_39 = {var_38, var_38, var_38, var_38}
    python_code_.wsmodel3_Break(expression=var_20)
    python_code_.wsmodel3_Orchestrator(
        port=var_36,
        name=var_20,
        wsmodel3_Orchestrator=b"g\x11\xbe",
        wsmodel3_Orchestrator66=var_39,
        wsmodel3_Orchestrator59=var_38,
    )


def test_30():
    var_0 = "hTiL)"
    var_2 = python_code_.wsmodel3_Orchestrator(
        port=var_0,
        name=var_0,
        wsmodel3_Orchestrator=var_0,
        wsmodel3_Orchestrator61=set(),
        wsmodel3_Orchestrator66=set(),
    )
    assert isinstance(var_2, python_code_.wsmodel3_Orchestrator)
    var_3 = python_code_.wsmodel3_System(name=var_0)
    python_code_.wsmodel3_InputOrchestrator(URI=var_0)
    var_12 = ";W|Op6\x0cw|>md"
    var_13 = -349
    var_14 = python_code_.wsmodel3_Bridge(topic=var_0, host=var_12, port=var_13)
    assert isinstance(var_14, python_code_.wsmodel3_Bridge)
    var_15 = python_code_.wsmodel3_WebService()
    var_16 = python_code_.wsmodel3_OutputOrchestrator()
    python_code_.wsmodel3_REST(
        URI=var_0, port=var_13, wsmodel3_REST=var_15, wsmodel3_REST86=var_16
    )
    var_20 = lambda *args, **kwargs: '\\`"_hc;{dlu'
    python_code_.wsmodel3_REST(
        URI=var_3,
        port=(),
        wsmodel3_REST="_wsmodel3_Orchestrator__wsmodel3_Orchestrator66",
        wsmodel3_REST40=var_20,
        wsmodel3_REST67=complex(-1682.04, 424.88438),
    )


@pytest.mark.xfail(strict=True)
def test_31():
    var_15 = "%S<o\n\x0bc"
    var_16 = python_code_.wsmodel3_CommunicationData
    var_17 = 1437
    var_18 = python_code_.wsmodel3_REST(URI=var_16, port=var_17, wsmodel3_REST22=var_16)
    python_code_.wsmodel3_Device(name=var_15, wsmodel3_Device23=var_18)


def test_32():
    var_7 = python_code_.wsmodel3_Sensor(
        type="wsmodel3_IntegrationPattern51:_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI89"
    )
    assert isinstance(var_7, python_code_.wsmodel3_Sensor)
    var_20 = python_code_.Data
    var_21 = python_code_.wsmodel3_Device(
        name={")3Zb[2\x0c?~Pj9>": "b\x0cIGR?0ZVOvK{hl3p"}, wsmodel3_Device23=var_20
    )
    assert isinstance(var_21, python_code_.wsmodel3_Device)


def test_33():
    var_38 = python_code_.Server()
    var_41 = "6"
    var_42 = python_code_.wsmodel3_IoTNode()
    var_43 = python_code_.wsmodel3_Device(name=var_41, wsmodel3_Device=var_42)
    assert isinstance(var_43, python_code_.wsmodel3_Device)
    var_52 = python_code_.wsmodel3_Controller(type=var_42)
    assert isinstance(var_52, python_code_.wsmodel3_Controller)
    var_46 = "wsmodel3_MessageBroker"
    var_48 = "K\\{~$M*LN5"
    python_code_.wsmodel3_ExternalAPI(URI=var_48)
    python_code_.wsmodel3_Device(name=var_38, wsmodel3_Device25=var_46)


def test_34():
    var_3 = python_code_.wsmodel3_IoTNode()
    var_4 = "78:"
    var_5 = python_code_.wsmodel3_Port(id=var_3, type=var_4)
    assert isinstance(var_5, python_code_.wsmodel3_Port)
    python_code_.wsmodel3_AccesPoint(ssid=[], pass_=var_4)
    var_27 = python_code_.Port
    var_28 = set()
    var_29 = python_code_.wsmodel3_Device(name=var_27, wsmodel3_Device25=var_28)
    assert isinstance(var_29, python_code_.wsmodel3_Device)
    var_32 = {var_5, var_5, var_5, var_5}
    var_33 = python_code_.wsmodel3_Controller(type=var_27, wsmodel3_Controller=var_32)
    assert isinstance(var_33, python_code_.wsmodel3_Controller)


def test_35():
    var_23 = "K6\\{~$M*LN5"
    python_code_.wsmodel3_ExternalAPI(URI=var_23)


def test_36():
    python_code_.wsmodel3_InputOrchestrator(URI="mCBX0cH\rms1fC..")
    var_15 = "_wsmodel3_Orchestrator__wsmodel3_Orchestrator"
    var_16 = python_code_.wsmodel3_Function(
        expression=var_15,
        wsmodel3_Function69={
            -929.33,
            "_wsmodel3_AccesPoint__wsmodel3_AccesPoint33",
            "Temperature-_wsmodel3_System__wsmodel3_System4-wsmodel3_InputOrchestrator57-Digital",
        },
    )
    assert isinstance(var_16, python_code_.wsmodel3_Function)
    var_17 = python_code_.SensorType.Contact
    python_code_.wsmodel3_ExternalAPI(
        URI=var_15, wsmodel3_ExternalAPI=var_17, wsmodel3_ExternalAPI64=None
    )


def test_37():
    var_0 = "xH1%h4"
    var_1 = python_code_.wsmodel3_InputBridge(URI=var_0)
    assert isinstance(var_1, python_code_.wsmodel3_InputBridge)
    var_2 = 0
    var_3 = "wsmodel3_Orchestrator66"
    var_4 = python_code_.wsmodel3_AccesPoint
    python_code_.wsmodel3_MessageBroker(
        type=var_1, port=var_2, host=var_0, usser=var_3, pass_=var_4
    )
    python_code_.wsmodel3_InputOrchestrator(
        URI=":47'",
        wsmodel3_InputOrchestrator=b"\xb3\x0e\x9f0",
        wsmodel3_InputOrchestrator78=488.32,
    )
    var_12 = python_code_.wsmodel3_CommunicationData()
    var_13 = " !I7W@auW='Cw"
    python_code_.wsmodel3_ExternalAPI(
        URI=var_13, wsmodel3_ExternalAPI64=var_4, wsmodel3_ExternalAPI89=var_3
    )
    var_15 = python_code_.wsmodel3_OutputOrchestrator()
    var_16 = python_code_.wsmodel3_Actuator(type=var_3)
    assert isinstance(var_16, python_code_.wsmodel3_Actuator)
    var_18 = "6"
    var_19 = python_code_.wsmodel3_IoTNode()
    var_20 = python_code_.wsmodel3_Device(name=var_18, wsmodel3_Device=var_19)
    assert isinstance(var_20, python_code_.wsmodel3_Device)
    python_code_.wsmodel3_InputBridge(URI=var_12, wsmodel3_InputBridge81=var_15)
    var_31 = '"G'
    var_32 = "wsmodel3_MessageBroker"
    var_33 = python_code_.wsmodel3_DBServer(
        database=var_31, usser=var_4, pass_=var_32, type=var_31, port=()
    )
    assert isinstance(var_33, python_code_.wsmodel3_DBServer)
    var_35 = "K\\{~$M*LN5"
    python_code_.wsmodel3_ExternalAPI(URI=var_35)


def test_38():
    var_33 = "eK8X3"
    var_34 = python_code_.wsmodel3_Function(expression=var_33)
    assert isinstance(var_34, python_code_.wsmodel3_Function)
    var_38 = python_code_.wsmodel3_MessageBroker
    var_39 = "?B#];@Ho/Q(|B'F"
    var_40 = -1158
    var_41 = python_code_.wsmodel3_MessageBroker(
        type=var_39, port=var_40, host=var_39, usser=var_40, pass_=var_33
    )
    var_42 = python_code_.wsmodel3_Bridge(
        topic=var_33, host={}, port=var_38, wsmodel3_Bridge49=var_41
    )
    assert isinstance(var_42, python_code_.wsmodel3_Bridge)


def test_39():
    var_2 = "z\x0bu^g<L7c\ti"
    var_15 = "wsmodel3_Orchestrator56"
    var_18 = "a@XSIs'pE7o"
    var_19 = python_code_.wsmodel3_AccesPoint(ssid=var_2, pass_=var_2)
    var_20 = {var_19, var_19, var_19}
    var_21 = python_code_.wsmodel3_System(
        name=var_18, wsmodel3_System4=var_15, wsmodel3_System6=var_20
    )
    assert isinstance(var_21, python_code_.wsmodel3_System)
    var_23 = python_code_.wsmodel3_Function(expression=var_18, wsmodel3_Function=None)
    assert isinstance(var_23, python_code_.wsmodel3_Function)
    python_code_.wsmodel3_System(
        name=var_2,
        wsmodel3_System6=var_20,
        wsmodel3_System10=var_20,
        wsmodel3_System=var_20,
    )


def test_40():
    python_code_.SensorType.CO2


def test_41():
    var_0 = "qS"
    var_1 = "sv\r(3d8M\\Q@}]1"
    var_2 = python_code_.Data
    var_3 = python_code_.wsmodel3_Orchestrator(
        port=var_1, name=var_2, wsmodel3_Orchestrator66={}
    )
    assert isinstance(var_3, python_code_.wsmodel3_Orchestrator)
    var_4 = python_code_.wsmodel3_Function(expression=var_0, wsmodel3_Function=var_3)
    assert isinstance(var_4, python_code_.wsmodel3_Function)
    var_5 = "W6y?_"
    python_code_.wsmodel3_Communication(type=var_2, name=var_5)
    var_9 = python_code_.Bridge()
    var_14 = 4448
    var_15 = "&a5e{ow"
    python_code_.wsmodel3_MessageBroker(
        type=var_0, port=var_14, host=var_2, usser=var_15, pass_=var_9
    )
    var_17 = "9\x0ceUNO"
    var_18 = "AAh"
    var_19 = python_code_.wsmodel3_Data(
        id=var_17,
        Date=var_18,
        Time=var_2,
        Location=var_17,
        Attribute=29,
        Artefact=var_1,
    )
    assert isinstance(var_19, python_code_.wsmodel3_Data)


def test_42():
    var_0 = python_code_.DBType.Undefined
    var_1 = python_code_.wsmodel3_Break(expression=var_0)
    var_2 = python_code_.Server()
    var_3 = python_code_.wsmodel3_IoTNode()
    var_4 = python_code_.ActuatorType
    var_5 = {var_1, var_1}
    var_6 = python_code_.wsmodel3_Function(
        expression="D!{#~6ftx/{+gO>4lw",
        wsmodel3_Function69=var_1,
        wsmodel3_Function75={False, var_2},
    )
    assert isinstance(var_6, python_code_.wsmodel3_Function)
    var_9 = python_code_.wsmodel3_Controller(type=complex(-1700.67, 475.7708))
    assert isinstance(var_9, python_code_.wsmodel3_Controller)
    var_10 = python_code_.wsmodel3_Communication(
        type=var_3,
        name=var_4,
        wsmodel3_Communication=var_9,
        wsmodel3_Communication35="e0x8YoO4\\<",
    )
    assert var_10.wsmodel3_Communication35 == "e0x8YoO4\\<"
    python_code_.wsmodel3_Controller(
        type=var_3, wsmodel3_Controller=var_5, wsmodel3_Controller28=var_5
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = python_code_.CommunicationType.Serial
    var_1 = "EwT"
    var_2 = python_code_.wsmodel3_Break(expression=468.34)
    var_3 = {var_2}
    var_4 = python_code_.wsmodel3_Function(
        expression=var_1, wsmodel3_Function69=var_0, wsmodel3_Function75=var_3
    )
    assert isinstance(var_4, python_code_.wsmodel3_Function)
    var_5 = python_code_.wsmodel3_Break(expression=var_1, wsmodel3_Break=var_4)
    assert isinstance(var_5, python_code_.wsmodel3_Break)
    var_8 = python_code_.wsmodel3_Port(id=4161, type=var_1)
    assert isinstance(var_8, python_code_.wsmodel3_Port)
    var_10 = "_wsmodel3_Controller__wsmodel3_Controller"
    python_code_.wsmodel3_Function(expression=var_10)
    var_12 = python_code_.wsmodel3_InputOrchestrator
    var_13 = python_code_.wsmodel3_Controller(type=var_12, wsmodel3_Controller=var_3)
    assert isinstance(var_13, python_code_.wsmodel3_Controller)
    python_code_.wsmodel3_InputOrchestrator(
        URI=complex(-618.9794503, -1291.0), wsmodel3_InputOrchestrator70=var_12
    )
    var_18 = python_code_.wsmodel3_Actuator(type=set())
    assert isinstance(var_18, python_code_.wsmodel3_Actuator)
    var_20 = python_code_.wsmodel3_InputBridge(URI=True)
    assert isinstance(var_20, python_code_.wsmodel3_InputBridge)
    var_21 = "_wsmodel3_MessageBroker__wsmodel3_MessageBroker-wsmodel3_WebService-_wsmodel3_Orchestrator__wsmodel3_Orchestrator61-wsmodel3_Orchestrator59"
    python_code_.wsmodel3_Port(
        id=complex(2311.4768, -3205.57), type=var_21, wsmodel3_Port=var_1
    )
    var_23 = python_code_.wsmodel3_ExternalAPI(URI=var_12, wsmodel3_ExternalAPI=None)
    var_24 = python_code_.wsmodel3_Sensor(type=var_10, wsmodel3_Sensor46=var_12)
    assert isinstance(var_24, python_code_.wsmodel3_Sensor)
    var_25 = python_code_.SensorType.Button
    var_26 = "|+"
    var_28 = 'o5S\x0b">w?AW>8\x0c!/#uQ'
    var_29 = "\x0c#Y"
    var_30 = python_code_.wsmodel3_Data(
        id={1093, -3533.88},
        Date=var_21,
        Time=var_10,
        Location=[],
        Attribute=var_28,
        Artefact=var_29,
    )
    assert isinstance(var_30, python_code_.wsmodel3_Data)
    python_code_.wsmodel3_REST(URI=var_28, port=var_23)
    var_37 = python_code_.wsmodel3_Bridge(topic=var_26, host=var_12, port=var_25)
    assert isinstance(var_37, python_code_.wsmodel3_Bridge)
    python_code_.wsmodel3_REST(
        URI=var_5, port="2w0J--92", wsmodel3_REST22=var_10, wsmodel3_REST40=var_37
    )


def test_44():
    var_17 = python_code_.wsmodel3_Actuator(type="4;F\n#_l< >ge\nUm @(R")
    assert isinstance(var_17, python_code_.wsmodel3_Actuator)
    var_18 = "O#14Y5=Z"
    var_19 = python_code_.wsmodel3_DBServer(
        database=var_18, usser=var_18, pass_=var_18, type=var_18, port=332.32
    )
    assert isinstance(var_19, python_code_.wsmodel3_DBServer)


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = python_code_.PortType.Analog
    var_1 = python_code_.wsmodel3_Break(
        expression="HwLvdo\x0cm{;+j DXmubI", wsmodel3_Break=var_0
    )
    var_3 = "wsmodel3_Orchestrator56"
    var_4 = python_code_.wsmodel3_Port(id=var_1, type=var_3, wsmodel3_Port=var_3)
    assert isinstance(var_4, python_code_.wsmodel3_Port)
    var_7 = "a@XSIs'pE7o"
    var_8 = python_code_.wsmodel3_AccesPoint(ssid=474.96, pass_=False)
    var_9 = {var_8, var_8, var_8}
    var_10 = python_code_.wsmodel3_System(
        name=var_7, wsmodel3_System4=var_3, wsmodel3_System6=var_9
    )
    assert isinstance(var_10, python_code_.wsmodel3_System)
    var_12 = python_code_.wsmodel3_Function(expression=var_3)
    assert isinstance(var_12, python_code_.wsmodel3_Function)
    var_13 = python_code_.wsmodel3_DeviceData
    var_14 = lambda *args, **kwargs: False
    python_code_.wsmodel3_System(
        name=var_13,
        wsmodel3_System2=var_14,
        wsmodel3_System8=var_9,
        wsmodel3_System10=var_14,
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_3 = python_code_.wsmodel3_CommunicationData()
    var_5 = "Jo#y-f&BQz9c"
    var_6 = python_code_.wsmodel3_Port(id=var_5, type=var_5)
    assert isinstance(var_6, python_code_.wsmodel3_Port)
    var_8 = python_code_.wsmodel3_Data(
        id=None, Date=var_5, Time=var_5, Location=var_5, Attribute=var_5, Artefact=True
    )
    assert isinstance(var_8, python_code_.wsmodel3_Data)
    var_9 = "wsmodel3_InputOrchestrator57"
    var_10 = ")dr0[4"
    var_11 = python_code_.wsmodel3_AccesPoint(ssid=var_9, pass_=var_10)
    var_12 = {var_11, var_11, var_11, var_11, var_11}
    var_13 = python_code_.wsmodel3_System(
        name=var_3, wsmodel3_System6=var_12, wsmodel3_System12=var_12
    )
    assert isinstance(var_13, python_code_.wsmodel3_System)
    var_14 = python_code_.wsmodel3_Bridge
    var_15 = 2140
    var_16 = python_code_.wsmodel3_OutputOrchestrator()
    python_code_.wsmodel3_REST(URI=var_14, port=var_15, wsmodel3_REST86=var_16)
    var_19 = "0O rx]C=;M|g$1"
    python_code_.wsmodel3_Communication(
        type=var_19,
        name=var_5,
        wsmodel3_Communication32={False, -3582},
        wsmodel3_Communication35=var_14,
    )
    var_21 = lambda *args, **kwargs: -1
    var_22 = python_code_.wsmodel3_OutputBridge()
    var_23 = python_code_.wsmodel3_Sensor(type=var_21, wsmodel3_Sensor46=var_22)
    assert isinstance(var_23, python_code_.wsmodel3_Sensor)
    var_29 = python_code_.wsmodel3_Server(host=var_9)
    assert isinstance(var_29, python_code_.wsmodel3_Server)
    var_31 = "_NJPHwF,JS\n}bk7ps"
    var_32 = python_code_.wsmodel3_Communication(
        type=b"\xe6/'1\xe5\xdc\xd4\xd9M\r`{\xc9p", name=var_31
    )
    python_code_.wsmodel3_MessageBroker(
        type=complex(-974.021, -4550.7),
        port=var_15,
        host={},
        usser=var_6,
        pass_=var_9,
        wsmodel3_MessageBroker36=var_32,
    )
    python_code_.wsmodel3_Actuator(type=True)
    python_code_.wsmodel3_Device(
        name=b"q&\xbb\xe8\x9f\xcf\xccV", wsmodel3_Device23=var_32
    )
    python_code_.wsmodel3_InputBridge(URI=var_31, wsmodel3_InputBridge=var_14)


@pytest.mark.xfail(strict=True)
def test_47():
    var_1 = "Contact._wsmodel3_REST__wsmodel3_REST22.wsmodel3_OutputBridge45"
    var_2 = python_code_.wsmodel3_Controller(type=var_1)
    assert isinstance(var_2, python_code_.wsmodel3_Controller)
    var_3 = "_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI64"
    var_4 = repr
    var_5 = python_code_.wsmodel3_AccesPoint(ssid=(-474.83, False), pass_=var_4)
    var_6 = {var_5}
    python_code_.wsmodel3_System(
        name=complex(792.1237, 2327.8764),
        wsmodel3_System6=var_6,
        wsmodel3_System8=var_3,
        wsmodel3_System10=var_4,
        wsmodel3_System=var_6,
    )


@pytest.mark.xfail(strict=True)
def test_48():
    var_0 = "hTiL)"
    var_1 = python_code_.wsmodel3_OutputOrchestrator
    var_2 = python_code_.wsmodel3_Orchestrator(
        port=var_0,
        name=var_0,
        wsmodel3_Orchestrator=var_0,
        wsmodel3_Orchestrator61=set(),
        wsmodel3_Orchestrator66=set(),
    )
    assert isinstance(var_2, python_code_.wsmodel3_Orchestrator)
    var_3 = python_code_.wsmodel3_System(name=var_0)
    python_code_.wsmodel3_InputOrchestrator(URI=var_0)
    var_6 = python_code_.wsmodel3_Port(id=var_1, type=var_0, wsmodel3_Port=var_2)
    assert isinstance(var_6, python_code_.wsmodel3_Port)
    var_7 = python_code_.Data()
    var_8 = python_code_.wsmodel3_AccesPoint(
        ssid={False, -933}, pass_=var_1, wsmodel3_AccesPoint33=var_3
    )
    python_code_.wsmodel3_Communication(
        type=var_7, name=set(), wsmodel3_Communication32=var_8
    )


@pytest.mark.xfail(strict=True)
def test_49():
    var_0 = ">B."
    var_1 = python_code_.wsmodel3_Orchestrator(
        port=b"1\xbc\xc5\x1dh%", name=var_0, wsmodel3_Orchestrator=var_0
    )
    assert isinstance(var_1, python_code_.wsmodel3_Orchestrator)
    var_3 = python_code_.wsmodel3_OutputOrchestrator()
    var_5 = python_code_.Data()
    var_6 = "(@ABQ[%\rr}{}?Y.:"
    var_7 = "pI&."
    var_8 = python_code_.wsmodel3_Data(
        id=var_6,
        Date=var_0,
        Time=var_0,
        Location=var_0,
        Attribute=var_0,
        Artefact=var_7,
    )
    assert isinstance(var_8, python_code_.wsmodel3_Data)
    var_10 = "y;lTDU52yP`\r"
    var_11 = python_code_.wsmodel3_Controller(
        type=var_10, wsmodel3_Controller=["OM)3p+C"]
    )
    assert isinstance(var_11, python_code_.wsmodel3_Controller)
    var_12 = python_code_.wsmodel3_OutputBridge()
    python_code_.wsmodel3_InputOrchestrator(
        URI=var_7, wsmodel3_InputOrchestrator=var_12, wsmodel3_InputOrchestrator57=True
    )
    var_14 = "Light"
    var_15 = "CMPiE<wI?=H4oD"
    python_code_.wsmodel3_Orchestrator(
        port=var_14, name=var_15, wsmodel3_Orchestrator63=var_7
    )
    var_18 = python_code_.wsmodel3_WebService()
    var_19 = python_code_.wsmodel3_DBServer(
        database=var_10,
        usser=var_14,
        pass_=var_6,
        type=[755, False],
        port=var_10,
        wsmodel3_DBServer=var_18,
    )
    assert isinstance(var_19, python_code_.wsmodel3_DBServer)
    python_code_.wsmodel3_AccesPoint(ssid=var_6, pass_=complex(1156.7, -1692.1))
    var_21 = python_code_.ControllerType
    var_22 = python_code_.wsmodel3_Sensor(type=var_21, wsmodel3_Sensor=-1802.78)
    assert isinstance(var_22, python_code_.wsmodel3_Sensor)
    var_23 = python_code_.wsmodel3_Device(name='Fzk):W*-"ILMdWW$39')
    assert isinstance(var_23, python_code_.wsmodel3_Device)
    var_26 = "/EVy=tz5a/X"
    var_27 = {var_3, var_3}
    python_code_.wsmodel3_Orchestrator(
        port=var_26,
        name=var_21,
        wsmodel3_Orchestrator=var_5,
        wsmodel3_Orchestrator61=var_27,
        wsmodel3_Orchestrator66=var_27,
        wsmodel3_Orchestrator56=-870,
        wsmodel3_Orchestrator59=var_22,
    )


def test_50():
    var_12 = python_code_.wsmodel3_MessageBroker
    var_13 = "?B#];@o/Q(|B'F"
    var_14 = -1158
    python_code_.wsmodel3_MessageBroker(
        type="=__V'#_o",
        port=var_14,
        host='\ry`SD_^NE]i\r"v.KRQ9',
        usser="wsmodel3_OutputOrchestrator73",
        pass_=var_13,
        wsmodel3_MessageBroker48={var_12, -238},
    )


@pytest.mark.xfail(strict=True)
def test_51():
    var_0 = '[a"nt'
    var_1 = python_code_.wsmodel3_ExternalAPI
    python_code_.wsmodel3_Break(expression=var_0, wsmodel3_Break=var_1)
    var_3 = python_code_.wsmodel3_Device(name=var_0)
    assert isinstance(var_3, python_code_.wsmodel3_Device)
    var_4 = python_code_.wsmodel3_InputOrchestrator(URI=var_1)
    var_5 = "_wsmodel3_System__wsmodel3_System"
    var_6 = python_code_.wsmodel3_Data(
        id=var_4,
        Date=complex(536.3, 522.542564),
        Time=-2591.42,
        Location=var_4,
        Attribute=var_0,
        Artefact=var_5,
    )
    assert isinstance(var_6, python_code_.wsmodel3_Data)
    var_7 = python_code_.wsmodel3_WebServer()
    var_10 = "x-\nI"
    var_11 = 1228
    var_12 = python_code_.wsmodel3_Bridge(
        topic=var_10,
        host=var_4,
        port=var_11,
        wsmodel3_Bridge49=complex(470.713, -75.57),
    )
    assert isinstance(var_12, python_code_.wsmodel3_Bridge)
    var_13 = python_code_.wsmodel3_OutputBridge()
    python_code_.wsmodel3_InputOrchestrator(
        URI=var_7, wsmodel3_InputOrchestrator=var_13
    )
    var_17 = "wsmodel3_REST40._wsmodel3_InputBridge__wsmodel3_InputBridge.wsmodel3_OutputBridge"
    python_code_.wsmodel3_Orchestrator(
        port=(-408, -2852.08),
        name=var_17,
        wsmodel3_Orchestrator56=complex(-790.47498, 670.82),
    )
