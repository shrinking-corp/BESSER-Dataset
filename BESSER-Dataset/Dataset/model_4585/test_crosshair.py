from python_code import activity_Activity
from python_code import activity_ActivityGroup

def test_activity_ActivityGroup___init__():
    assert activity_ActivityGroup.__init__(activity_ActivityGroup('', activity_ActivityGroup=activity_Activity()), '', activity_ActivityGroup=activity_Activity()) == None


from python_code import activity_Activity
from python_code import activity_ActivityParameterNode

def test_activity_ActivityParameterNode___init__():
    assert activity_ActivityParameterNode.__init__(activity_ActivityParameterNode('', activity_ActivityParameterNode=activity_Activity(), activity_ActivityParameterNode10=set()), '', activity_ActivityParameterNode=activity_Activity(), activity_ActivityParameterNode10=set()) == None


from python_code import activity_NamedElement

def test_activity_NamedElement___init__():
    assert activity_NamedElement.__init__(activity_NamedElement('', '\x00'), '\x00\x00', '') == None

