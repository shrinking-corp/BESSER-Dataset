from python_code import metrics_RuleSetMetrics

def test_metrics_RuleSetMetrics___init__():
    assert metrics_RuleSetMetrics.__init__(metrics_RuleSetMetrics(0, 0, 0, 0, metrics_RuleSetMetrics=set(), metrics_RuleSetMetrics2=set()), 0, 0, 0, 0, metrics_RuleSetMetrics=set(), metrics_RuleSetMetrics2=set()) == None

def test_metrics_RuleSetMetrics_findRuleMetrics():
    assert metrics_RuleSetMetrics.findRuleMetrics(metrics_RuleSetMetrics(0, 0, 0, 0, metrics_RuleSetMetrics=set(), metrics_RuleSetMetrics2=set()), '') == None

def test_metrics_RuleSetMetrics_createPresentationString():
    assert metrics_RuleSetMetrics.createPresentationString(metrics_RuleSetMetrics(0, 0, 0, 0, metrics_RuleSetMetrics=set(), metrics_RuleSetMetrics2=set())) == None

