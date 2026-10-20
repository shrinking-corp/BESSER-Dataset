from python_code import sexec_ExecutionFlow
from python_code import sexec_ExecutionNode
from python_code import sexec_ExecutionRegion
from python_code import sexec_TraceNodeExecuted

def test_sexec_ExecutionNode___init__():
    assert sexec_ExecutionNode.__init__(sexec_ExecutionNode('', sexec_ExecutionNode=sexec_ExecutionFlow(), sexec_ExecutionNode31=sexec_ExecutionRegion(), sexec_ExecutionNode68=sexec_TraceNodeExecuted()), '', sexec_ExecutionNode=sexec_ExecutionFlow(), sexec_ExecutionNode31=sexec_ExecutionRegion(), sexec_ExecutionNode68=sexec_TraceNodeExecuted()) == None


from python_code import sexec_ExecutionRegion
from python_code import sexec_SaveHistory

def test_sexec_SaveHistory___init__():
    assert sexec_SaveHistory.__init__(sexec_SaveHistory(True, sexec_SaveHistory=sexec_ExecutionRegion()), False, sexec_SaveHistory=sexec_ExecutionRegion()) == None


from python_code import sexec_ExecutionRegion
from python_code import sexec_StateSwitch

def test_sexec_StateSwitch___init__():
    assert sexec_StateSwitch.__init__(sexec_StateSwitch(0, sexec_StateSwitch49=sexec_ExecutionRegion(), sexec_StateSwitch=set()), 0, sexec_StateSwitch49=sexec_ExecutionRegion(), sexec_StateSwitch=set()) == None


from python_code import sexec_ExecutionFlow
from python_code import sexec_ExecutionRegion
from python_code import sexec_ExecutionScope
from python_code import sexec_StateVector

def test_sexec_StateVector___init__():
    assert sexec_StateVector.__init__(sexec_StateVector(0, 0, sexec_StateVector28=sexec_ExecutionRegion(), sexec_StateVector=sexec_ExecutionFlow(), sexec_StateVector20=sexec_ExecutionScope()), 0, 0, sexec_StateVector28=sexec_ExecutionRegion(), sexec_StateVector=sexec_ExecutionFlow(), sexec_StateVector20=sexec_ExecutionScope()) == None


from python_code import sexec_ScheduleTimeEvent
from python_code import sexec_TimeEvent
from python_code import sexec_UnscheduleTimeEvent

def test_sexec_TimeEvent___init__():
    assert sexec_TimeEvent.__init__(sexec_TimeEvent(True, sexec_TimeEvent=sexec_ScheduleTimeEvent(), sexec_TimeEvent46=sexec_UnscheduleTimeEvent()), False, sexec_TimeEvent=sexec_ScheduleTimeEvent(), sexec_TimeEvent46=sexec_UnscheduleTimeEvent()) == None

