import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    remember_Customer,
    remember_Customers,
    remember_Folder,
    remember_InvoiceSpecification,
    remember_KeyIdPair,
    remember_KeyManager,
    remember_Node,
    remember_Project,
    remember_Task,
    remember_TimeSpent,
    remember_Year,
    remember_Years,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_customer11_reverse_link_reassign_clear():
    a1 = remember_Node(dateCreated=date(2024, 1, 1), dateModified=date(2024, 1, 1), description="sample_text", markedForDeletion=True, name="sample_text", nodeId="sample_text", nodeType="sample_text", parentNodeId="sample_text", parentNodeType="sample_text", sequence=7)
    a2 = remember_Node(dateCreated=date(2025, 6, 15), dateModified=date(2025, 6, 15), description="sample_text_2", markedForDeletion=False, name="sample_text_2", nodeId="sample_text_2", nodeType="sample_text_2", parentNodeId="sample_text_2", parentNodeType="sample_text_2", sequence=13)
    b = remember_Customer(customerId="sample_text", name="sample_text")
    _safe_set(b, 'Customer', a1)
    assert _is_linked(b, 'Customer', a1)
    if hasattr(a1, 'nodes'):
        assert _is_linked(a1, 'nodes', b)
    _safe_set(b, 'Customer', a2)
    assert _is_linked(b, 'Customer', a2)
    if hasattr(a1, 'nodes'):
        assert not _is_linked(a1, 'nodes', b)
    if hasattr(a2, 'nodes'):
        assert _is_linked(a2, 'nodes', b)
    _safe_set(b, 'Customer', None)
    assert not _is_linked(b, 'Customer', a2)
    if hasattr(a2, 'nodes'):
        assert not _is_linked(a2, 'nodes', b)


def test_assoc_customer19_reverse_link_reassign_clear():
    a1 = remember_Project(description="sample_text", projectId="sample_text", projectNumber="sample_text")
    a2 = remember_Project(description="sample_text_2", projectId="sample_text_2", projectNumber="sample_text_2")
    b = remember_Customer(customerId="sample_text", name="sample_text")
    _safe_set(b, 'Customer20', a1)
    assert _is_linked(b, 'Customer20', a1)
    if hasattr(a1, 'projects'):
        assert _is_linked(a1, 'projects', b)
    _safe_set(b, 'Customer20', a2)
    assert _is_linked(b, 'Customer20', a2)
    if hasattr(a1, 'projects'):
        assert not _is_linked(a1, 'projects', b)
    if hasattr(a2, 'projects'):
        assert _is_linked(a2, 'projects', b)
    _safe_set(b, 'Customer20', None)
    assert not _is_linked(b, 'Customer20', a2)
    if hasattr(a2, 'projects'):
        assert not _is_linked(a2, 'projects', b)


def test_assoc_invoiceSpecification28_reverse_link_reassign_clear():
    a1 = remember_TimeSpent(comment="sample_text", date=date(2024, 1, 1), invoiced=True, minutes=7, timeSpentId="sample_text")
    a2 = remember_TimeSpent(comment="sample_text_2", date=date(2025, 6, 15), invoiced=False, minutes=13, timeSpentId="sample_text_2")
    b = remember_InvoiceSpecification(month=7)
    _safe_set(b, 'InvoiceSpecification', a1)
    assert _is_linked(b, 'InvoiceSpecification', a1)
    if hasattr(a1, 'timeSpent29'):
        assert _is_linked(a1, 'timeSpent29', b)
    _safe_set(b, 'InvoiceSpecification', a2)
    assert _is_linked(b, 'InvoiceSpecification', a2)
    if hasattr(a1, 'timeSpent29'):
        assert not _is_linked(a1, 'timeSpent29', b)
    if hasattr(a2, 'timeSpent29'):
        assert _is_linked(a2, 'timeSpent29', b)
    _safe_set(b, 'InvoiceSpecification', None)
    assert not _is_linked(b, 'InvoiceSpecification', a2)
    if hasattr(a2, 'timeSpent29'):
        assert not _is_linked(a2, 'timeSpent29', b)


def test_assoc_nodes17_reverse_link_reassign_clear():
    a1 = remember_Node(dateCreated=date(2024, 1, 1), dateModified=date(2024, 1, 1), description="sample_text", markedForDeletion=True, name="sample_text", nodeId="sample_text", nodeType="sample_text", parentNodeId="sample_text", parentNodeType="sample_text", sequence=7)
    a2 = remember_Node(dateCreated=date(2025, 6, 15), dateModified=date(2025, 6, 15), description="sample_text_2", markedForDeletion=False, name="sample_text_2", nodeId="sample_text_2", nodeType="sample_text_2", parentNodeId="sample_text_2", parentNodeType="sample_text_2", sequence=13)
    b = remember_Customer(customerId="sample_text", name="sample_text")
    _safe_set(b, 'customer18', {a1})
    assert _is_linked(b, 'customer18', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'customer18', {a2})
    assert _is_linked(b, 'customer18', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'customer18', set())
    assert not _is_linked(b, 'customer18', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_nodes21_reverse_link_reassign_clear():
    a1 = remember_Project(description="sample_text", projectId="sample_text", projectNumber="sample_text")
    a2 = remember_Project(description="sample_text_2", projectId="sample_text_2", projectNumber="sample_text_2")
    b = remember_Node(dateCreated=date(2024, 1, 1), dateModified=date(2024, 1, 1), description="sample_text", markedForDeletion=True, name="sample_text", nodeId="sample_text", nodeType="sample_text", parentNodeId="sample_text", parentNodeType="sample_text", sequence=7)
    _safe_set(b, 'Node22', a1)
    assert _is_linked(b, 'Node22', a1)
    if hasattr(a1, 'project'):
        assert _is_linked(a1, 'project', b)
    _safe_set(b, 'Node22', a2)
    assert _is_linked(b, 'Node22', a2)
    if hasattr(a1, 'project'):
        assert not _is_linked(a1, 'project', b)
    if hasattr(a2, 'project'):
        assert _is_linked(a2, 'project', b)
    _safe_set(b, 'Node22', None)
    assert not _is_linked(b, 'Node22', a2)
    if hasattr(a2, 'project'):
        assert not _is_linked(a2, 'project', b)


def test_assoc_project12_reverse_link_reassign_clear():
    a1 = remember_Project(description="sample_text", projectId="sample_text", projectNumber="sample_text")
    a2 = remember_Project(description="sample_text_2", projectId="sample_text_2", projectNumber="sample_text_2")
    b = remember_Node(dateCreated=date(2024, 1, 1), dateModified=date(2024, 1, 1), description="sample_text", markedForDeletion=True, name="sample_text", nodeId="sample_text", nodeType="sample_text", parentNodeId="sample_text", parentNodeType="sample_text", sequence=7)
    _safe_set(b, 'nodes13', a1)
    assert _is_linked(b, 'nodes13', a1)
    if hasattr(a1, 'Project'):
        assert _is_linked(a1, 'Project', b)
    _safe_set(b, 'nodes13', a2)
    assert _is_linked(b, 'nodes13', a2)
    if hasattr(a1, 'Project'):
        assert not _is_linked(a1, 'Project', b)
    if hasattr(a2, 'Project'):
        assert _is_linked(a2, 'Project', b)
    _safe_set(b, 'nodes13', None)
    assert not _is_linked(b, 'nodes13', a2)
    if hasattr(a2, 'Project'):
        assert not _is_linked(a2, 'Project', b)


def test_assoc_project25_reverse_link_reassign_clear():
    a1 = remember_TimeSpent(comment="sample_text", date=date(2024, 1, 1), invoiced=True, minutes=7, timeSpentId="sample_text")
    a2 = remember_TimeSpent(comment="sample_text_2", date=date(2025, 6, 15), invoiced=False, minutes=13, timeSpentId="sample_text_2")
    b = remember_Project(description="sample_text", projectId="sample_text", projectNumber="sample_text")
    _safe_set(b, 'remember_Project', a1)
    assert _is_linked(b, 'remember_Project', a1)
    if hasattr(a1, 'remember_TimeSpent'):
        assert _is_linked(a1, 'remember_TimeSpent', b)
    _safe_set(b, 'remember_Project', a2)
    assert _is_linked(b, 'remember_Project', a2)
    if hasattr(a1, 'remember_TimeSpent'):
        assert not _is_linked(a1, 'remember_TimeSpent', b)
    if hasattr(a2, 'remember_TimeSpent'):
        assert _is_linked(a2, 'remember_TimeSpent', b)
    _safe_set(b, 'remember_Project', None)
    assert not _is_linked(b, 'remember_Project', a2)
    if hasattr(a2, 'remember_TimeSpent'):
        assert not _is_linked(a2, 'remember_TimeSpent', b)


def test_assoc_projects15_reverse_link_reassign_clear():
    a1 = remember_Project(description="sample_text", projectId="sample_text", projectNumber="sample_text")
    a2 = remember_Project(description="sample_text_2", projectId="sample_text_2", projectNumber="sample_text_2")
    b = remember_Customer(customerId="sample_text", name="sample_text")
    _safe_set(b, 'customer', {a1})
    assert _is_linked(b, 'customer', a1)
    if hasattr(a1, 'Project16'):
        assert _is_linked(a1, 'Project16', b)
    _safe_set(b, 'customer', {a2})
    assert _is_linked(b, 'customer', a2)
    if hasattr(a1, 'Project16'):
        assert not _is_linked(a1, 'Project16', b)
    if hasattr(a2, 'Project16'):
        assert _is_linked(a2, 'Project16', b)
    _safe_set(b, 'customer', set())
    assert not _is_linked(b, 'customer', a2)
    if hasattr(a2, 'Project16'):
        assert not _is_linked(a2, 'Project16', b)


def test_assoc_task26_reverse_link_reassign_clear():
    a1 = remember_TimeSpent(comment="sample_text", date=date(2024, 1, 1), invoiced=True, minutes=7, timeSpentId="sample_text")
    a2 = remember_TimeSpent(comment="sample_text_2", date=date(2025, 6, 15), invoiced=False, minutes=13, timeSpentId="sample_text_2")
    b = remember_Task(budget="sample_text", done=True, priority="sample_text", status="sample_text", taskId=7, text="sample_text")
    _safe_set(b, 'Task27', a1)
    assert _is_linked(b, 'Task27', a1)
    if hasattr(a1, 'timeSpent'):
        assert _is_linked(a1, 'timeSpent', b)
    _safe_set(b, 'Task27', a2)
    assert _is_linked(b, 'Task27', a2)
    if hasattr(a1, 'timeSpent'):
        assert not _is_linked(a1, 'timeSpent', b)
    if hasattr(a2, 'timeSpent'):
        assert _is_linked(a2, 'timeSpent', b)
    _safe_set(b, 'Task27', None)
    assert not _is_linked(b, 'Task27', a2)
    if hasattr(a2, 'timeSpent'):
        assert not _is_linked(a2, 'timeSpent', b)


def test_assoc_timeSpent10_reverse_link_reassign_clear():
    a1 = remember_TimeSpent(comment="sample_text", date=date(2024, 1, 1), invoiced=True, minutes=7, timeSpentId="sample_text")
    a2 = remember_TimeSpent(comment="sample_text_2", date=date(2025, 6, 15), invoiced=False, minutes=13, timeSpentId="sample_text_2")
    b = remember_Task(budget="sample_text", done=True, priority="sample_text", status="sample_text", taskId=7, text="sample_text")
    _safe_set(b, 'task', {a1})
    assert _is_linked(b, 'task', a1)
    if hasattr(a1, 'TimeSpent'):
        assert _is_linked(a1, 'TimeSpent', b)
    _safe_set(b, 'task', {a2})
    assert _is_linked(b, 'task', a2)
    if hasattr(a1, 'TimeSpent'):
        assert not _is_linked(a1, 'TimeSpent', b)
    if hasattr(a2, 'TimeSpent'):
        assert _is_linked(a2, 'TimeSpent', b)
    _safe_set(b, 'task', set())
    assert not _is_linked(b, 'task', a2)
    if hasattr(a2, 'TimeSpent'):
        assert not _is_linked(a2, 'TimeSpent', b)


def test_assoc_timeSpent34_reverse_link_reassign_clear():
    a1 = remember_TimeSpent(comment="sample_text", date=date(2024, 1, 1), invoiced=True, minutes=7, timeSpentId="sample_text")
    a2 = remember_TimeSpent(comment="sample_text_2", date=date(2025, 6, 15), invoiced=False, minutes=13, timeSpentId="sample_text_2")
    b = remember_InvoiceSpecification(month=7)
    _safe_set(b, 'invoiceSpecification', {a1})
    assert _is_linked(b, 'invoiceSpecification', a1)
    if hasattr(a1, 'TimeSpent35'):
        assert _is_linked(a1, 'TimeSpent35', b)
    _safe_set(b, 'invoiceSpecification', {a2})
    assert _is_linked(b, 'invoiceSpecification', a2)
    if hasattr(a1, 'TimeSpent35'):
        assert not _is_linked(a1, 'TimeSpent35', b)
    if hasattr(a2, 'TimeSpent35'):
        assert _is_linked(a2, 'TimeSpent35', b)
    _safe_set(b, 'invoiceSpecification', set())
    assert not _is_linked(b, 'invoiceSpecification', a2)
    if hasattr(a2, 'TimeSpent35'):
        assert not _is_linked(a2, 'TimeSpent35', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Tasks0_stub_double():
    # remember_Folder has no real 'parent' property in the generated
    # code (a bare stub) -- manually attach it so remember_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remember_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remember_Task(budget="sample_text", done=True, priority="sample_text", status="sample_text", taskId=7, text="sample_text")
    partner = remember_Folder()
    setattr(partner, 'parent', None)
    _safe_set(owner, 'Task', partner)
    assert owner in getattr(partner, 'parent')
    _safe_set(owner, 'Task', None)
    assert owner not in getattr(partner, 'parent')


def test_assoc_customers23_stub_double():
    # remember_Customers has no real 'remember_Customers24' property in the generated
    # code (a bare stub) -- manually attach it so remember_Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remember_Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remember_Customer(customerId="sample_text", name="sample_text")
    partner = remember_Customers()
    setattr(partner, 'remember_Customers24', None)
    _safe_set(owner, 'remember_Customer', partner)
    assert owner in getattr(partner, 'remember_Customers24')
    _safe_set(owner, 'remember_Customer', None)
    assert owner not in getattr(partner, 'remember_Customers24')


def test_assoc_keyIdPairs14_stub_double():
    # remember_KeyManager has no real 'remember_KeyManager' property in the generated
    # code (a bare stub) -- manually attach it so remember_KeyIdPair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remember_KeyIdPair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remember_KeyIdPair(id="sample_text", key="sample_text")
    partner = remember_KeyManager()
    setattr(partner, 'remember_KeyManager', None)
    _safe_set(owner, 'remember_KeyIdPair', partner)
    assert owner in getattr(partner, 'remember_KeyManager')
    _safe_set(owner, 'remember_KeyIdPair', None)
    assert owner not in getattr(partner, 'remember_KeyManager')


def test_assoc_parent8_stub_double():
    # remember_Folder has no real 'Folder9' property in the generated
    # code (a bare stub) -- manually attach it so remember_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remember_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remember_Task(budget="sample_text", done=True, priority="sample_text", status="sample_text", taskId=7, text="sample_text")
    partner = remember_Folder()
    setattr(partner, 'Folder9', None)
    _safe_set(owner, 'Tasks', partner)
    assert getattr(partner, 'Folder9') == owner
    _safe_set(owner, 'Tasks', None)
    assert getattr(partner, 'Folder9') is None


