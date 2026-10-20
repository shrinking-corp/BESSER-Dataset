from python_code import simulink_Constant

def test_simulink_Constant___init__():
    assert simulink_Constant.__init__(simulink_Constant('', '\x00'), '\x00\x00', '') == None


from python_code import simulink_DigitalClock

def test_simulink_DigitalClock___init__():
    assert simulink_DigitalClock.__init__(simulink_DigitalClock(0.0), 0.0) == None


from python_code import simulink_Element

def test_simulink_Element___init__():
    assert simulink_Element.__init__(simulink_Element('', simulink_Element=set()), '', simulink_Element=set()) == None

def test_simulink_Element_getParameter():
    assert simulink_Element.getParameter(simulink_Element('', simulink_Element=set()), '') == None


from python_code import simulink_EmbeddedMatlabFunction

def test_simulink_EmbeddedMatlabFunction___init__():
    assert simulink_EmbeddedMatlabFunction.__init__(simulink_EmbeddedMatlabFunction(''), '') == None


from python_code import simulink_MiscBlock

def test_simulink_MiscBlock___init__():
    assert simulink_MiscBlock.__init__(simulink_MiscBlock(''), '') == None


from python_code import simulink_PortBlock

def test_simulink_PortBlock___init__():
    assert simulink_PortBlock.__init__(simulink_PortBlock('', '', '\x00\x00'), '', '', '') == None


from python_code import simulink_TriggerPort

def test_simulink_TriggerPort___init__():
    assert simulink_TriggerPort.__init__(simulink_TriggerPort(''), '') == None


from python_code import simulink_ZeroOrderHold

def test_simulink_ZeroOrderHold___init__():
    assert simulink_ZeroOrderHold.__init__(simulink_ZeroOrderHold(''), '') == None


from python_code import simulink_msglib_CommunicationSwitch

def test_simulink_msglib_CommunicationSwitch___init__():
    assert simulink_msglib_CommunicationSwitch.__init__(simulink_msglib_CommunicationSwitch(0), 0) == None


from python_code import simulink_msglib_LinkLayer

def test_simulink_msglib_LinkLayer___init__():
    assert simulink_msglib_LinkLayer.__init__(simulink_msglib_LinkLayer('', '', 0, False, False, 0, 0, ''), '', '', 0, False, False, 0, 0, '') == None


from python_code import simulink_reconfiguration_FadingComponent

def test_simulink_reconfiguration_FadingComponent___init__():
    assert simulink_reconfiguration_FadingComponent.__init__(simulink_reconfiguration_FadingComponent(0), 0) == None


from python_code import simulink_stateflow_Action

def test_simulink_stateflow_Action___init__():
    assert simulink_stateflow_Action.__init__(simulink_stateflow_Action(''), '') == None


from python_code import simulink_stateflow_Data

def test_simulink_stateflow_Data___init__():
    assert simulink_stateflow_Data.__init__(simulink_stateflow_Data('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import simulink_stateflow_EmbeddedFunction

def test_simulink_stateflow_EmbeddedFunction___init__():
    assert simulink_stateflow_EmbeddedFunction.__init__(simulink_stateflow_EmbeddedFunction('', '', simulink_stateflow_EmbeddedFunction=set(), simulink_stateflow_EmbeddedFunction102=set(), simulink_stateflow_EmbeddedFunction105=set(), simulink_stateflow_EmbeddedFunction108=set()), '\x00', '', simulink_stateflow_EmbeddedFunction=set(), simulink_stateflow_EmbeddedFunction102=set(), simulink_stateflow_EmbeddedFunction105=set(), simulink_stateflow_EmbeddedFunction108=set()) == None


from python_code import simulink_stateflow_Event

def test_simulink_stateflow_Event___init__():
    assert simulink_stateflow_Event.__init__(simulink_stateflow_Event(''), '') == None

