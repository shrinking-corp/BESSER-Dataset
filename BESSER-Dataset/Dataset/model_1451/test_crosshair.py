from python_code import graph_GButton

def test_graph_GButton___init__():
    assert graph_GButton.__init__(graph_GButton(True), False) == None


from python_code import graph_GBoundsAware
from python_code import graph_GDimension

def test_graph_GDimension___init__():
    assert graph_GDimension.__init__(graph_GDimension(0.0, 0.0, graph_GDimension=graph_GBoundsAware()), 0.0, 0.0, graph_GDimension=graph_GBoundsAware()) == None


from python_code import graph_GEdgeLayoutable
from python_code import graph_GEdgePlacement

def test_graph_GEdgePlacement___init__():
    assert graph_GEdgePlacement.__init__(graph_GEdgePlacement('\x00\x00', '', '', True, graph_GEdgePlacement=graph_GEdgeLayoutable()), '', '', '', False, graph_GEdgePlacement=graph_GEdgeLayoutable()) == None


from python_code import graph_GHtmlRoot

def test_graph_GHtmlRoot___init__():
    assert graph_GHtmlRoot.__init__(graph_GHtmlRoot(''), '') == None


from python_code import graph_GIssue
from python_code import graph_GIssueMarker

def test_graph_GIssue___init__():
    assert graph_GIssue.__init__(graph_GIssue('', '\x00', graph_GIssue=graph_GIssueMarker()), '\x00\x00', '', graph_GIssue=graph_GIssueMarker()) == None


from python_code import graph_GLabel

def test_graph_GLabel___init__():
    assert graph_GLabel.__init__(graph_GLabel(''), '') == None


from python_code import graph_GPreRenderedElement

def test_graph_GPreRenderedElement___init__():
    assert graph_GPreRenderedElement.__init__(graph_GPreRenderedElement(''), '') == None

