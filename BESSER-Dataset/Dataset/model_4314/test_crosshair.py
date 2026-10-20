from python_code import MetricModel_ActivityMetric

def test_MetricModel_ActivityMetric___init__():
    assert MetricModel_ActivityMetric.__init__(MetricModel_ActivityMetric('', '\x00'), '\x00\x00', '') == None


from python_code import MetricModel_MetricPlanModel

def test_MetricModel_MetricPlanModel___init__():
    assert MetricModel_MetricPlanModel.__init__(MetricModel_MetricPlanModel('\x00', MetricModel_MetricPlanModel=set()), '', MetricModel_MetricPlanModel=set()) == None


from python_code import MetricModel_TaskMetric

def test_MetricModel_TaskMetric___init__():
    assert MetricModel_TaskMetric.__init__(MetricModel_TaskMetric(''), '') == None

