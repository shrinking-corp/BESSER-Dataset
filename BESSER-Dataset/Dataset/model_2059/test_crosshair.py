from python_code import activitydiagram_ActivityFinalNode

def test_activitydiagram_ActivityFinalNode___init__():
    assert activitydiagram_ActivityFinalNode.__init__(activitydiagram_ActivityFinalNode()) == None

def test_activitydiagram_ActivityFinalNode_execute():
    assert activitydiagram_ActivityFinalNode.execute(activitydiagram_ActivityFinalNode()) == None


from python_code import activitydiagram_BooleanValue

def test_activitydiagram_BooleanValue___init__():
    assert activitydiagram_BooleanValue.__init__(activitydiagram_BooleanValue(True), False) == None


from python_code import activitydiagram_FlowFinalNode

def test_activitydiagram_FlowFinalNode___init__():
    assert activitydiagram_FlowFinalNode.__init__(activitydiagram_FlowFinalNode()) == None

def test_activitydiagram_FlowFinalNode_execute():
    assert activitydiagram_FlowFinalNode.execute(activitydiagram_FlowFinalNode()) == None


from python_code import activitydiagram_IntegerValue

def test_activitydiagram_IntegerValue___init__():
    assert activitydiagram_IntegerValue.__init__(activitydiagram_IntegerValue(0), 0) == None


from python_code import activitydiagram_NamedElement

def test_activitydiagram_NamedElement___init__():
    assert activitydiagram_NamedElement.__init__(activitydiagram_NamedElement(True), False) == None

def test_activitydiagram_NamedElement_execute():
    assert activitydiagram_NamedElement.execute(activitydiagram_NamedElement(False)) == None


from python_code import activitydiagram_OpaqueAction

def test_activitydiagram_OpaqueAction___init__():
    assert activitydiagram_OpaqueAction.__init__(activitydiagram_OpaqueAction(activitydiagram_OpaqueAction=set()), activitydiagram_OpaqueAction=set()) == None

def test_activitydiagram_OpaqueAction_execute():
    assert activitydiagram_OpaqueAction.execute(activitydiagram_OpaqueAction(activitydiagram_OpaqueAction=set())) == None

def test_activitydiagram_OpaqueAction_sendOffer():
    assert activitydiagram_OpaqueAction.sendOffer(activitydiagram_OpaqueAction(activitydiagram_OpaqueAction=set()), 0) == None

def test_activitydiagram_OpaqueAction_hasOffers():
    assert activitydiagram_OpaqueAction.hasOffers(activitydiagram_OpaqueAction(activitydiagram_OpaqueAction=set())) == None

