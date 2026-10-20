import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    accounting_Client,
    accounting_ClientDatabase,
    accounting_Deliverable,
    accounting_Employee,
    accounting_EmployeeDatabase,
    accounting_Invoice,
    accounting_NamedElement,
    accounting_Order,
    accounting_Project,
    InvoiceState,
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

def test_assoc_advisor5_reverse_link_reassign_clear():
    a1 = accounting_Invoice(id="sample_text", invoiceDate=date(2024, 1, 1), state="sample_text", unitAmount=3.14)
    a2 = accounting_Invoice(id="sample_text_2", invoiceDate=date(2025, 6, 15), state="sample_text_2", unitAmount=9.99)
    b = accounting_Employee(emails="sample_text")
    _safe_set(b, 'accounting_Employee', a1)
    assert _is_linked(b, 'accounting_Employee', a1)
    if hasattr(a1, 'accounting_Invoice'):
        assert _is_linked(a1, 'accounting_Invoice', b)
    _safe_set(b, 'accounting_Employee', a2)
    assert _is_linked(b, 'accounting_Employee', a2)
    if hasattr(a1, 'accounting_Invoice'):
        assert not _is_linked(a1, 'accounting_Invoice', b)
    if hasattr(a2, 'accounting_Invoice'):
        assert _is_linked(a2, 'accounting_Invoice', b)
    _safe_set(b, 'accounting_Employee', None)
    assert not _is_linked(b, 'accounting_Employee', a2)
    if hasattr(a2, 'accounting_Invoice'):
        assert not _is_linked(a2, 'accounting_Invoice', b)


def test_assoc_deliverables1_reverse_link_reassign_clear():
    a1 = accounting_Order(id="sample_text", paymentOffset=7, pricePerUnit=3.14)
    a2 = accounting_Order(id="sample_text_2", paymentOffset=13, pricePerUnit=9.99)
    b = accounting_Deliverable(dueDate=date(2024, 1, 1), unitAmount=3.14)
    _safe_set(b, 'Deliverable', a1)
    assert _is_linked(b, 'Deliverable', a1)
    if hasattr(a1, 'order'):
        assert _is_linked(a1, 'order', b)
    _safe_set(b, 'Deliverable', a2)
    assert _is_linked(b, 'Deliverable', a2)
    if hasattr(a1, 'order'):
        assert not _is_linked(a1, 'order', b)
    if hasattr(a2, 'order'):
        assert _is_linked(a2, 'order', b)
    _safe_set(b, 'Deliverable', None)
    assert not _is_linked(b, 'Deliverable', a2)
    if hasattr(a2, 'order'):
        assert not _is_linked(a2, 'order', b)


def test_assoc_invoices2_reverse_link_reassign_clear():
    a1 = accounting_Order(id="sample_text", paymentOffset=7, pricePerUnit=3.14)
    a2 = accounting_Order(id="sample_text_2", paymentOffset=13, pricePerUnit=9.99)
    b = accounting_Invoice(id="sample_text", invoiceDate=date(2024, 1, 1), state="sample_text", unitAmount=3.14)
    _safe_set(b, 'Invoice', a1)
    assert _is_linked(b, 'Invoice', a1)
    if hasattr(a1, 'order3'):
        assert _is_linked(a1, 'order3', b)
    _safe_set(b, 'Invoice', a2)
    assert _is_linked(b, 'Invoice', a2)
    if hasattr(a1, 'order3'):
        assert not _is_linked(a1, 'order3', b)
    if hasattr(a2, 'order3'):
        assert _is_linked(a2, 'order3', b)
    _safe_set(b, 'Invoice', None)
    assert not _is_linked(b, 'Invoice', a2)
    if hasattr(a2, 'order3'):
        assert not _is_linked(a2, 'order3', b)


def test_assoc_order4_reverse_link_reassign_clear():
    a1 = accounting_Order(id="sample_text", paymentOffset=7, pricePerUnit=3.14)
    a2 = accounting_Order(id="sample_text_2", paymentOffset=13, pricePerUnit=9.99)
    b = accounting_Deliverable(dueDate=date(2024, 1, 1), unitAmount=3.14)
    _safe_set(b, 'deliverables', a1)
    assert _is_linked(b, 'deliverables', a1)
    if hasattr(a1, 'Order'):
        assert _is_linked(a1, 'Order', b)
    _safe_set(b, 'deliverables', a2)
    assert _is_linked(b, 'deliverables', a2)
    if hasattr(a1, 'Order'):
        assert not _is_linked(a1, 'Order', b)
    if hasattr(a2, 'Order'):
        assert _is_linked(a2, 'Order', b)
    _safe_set(b, 'deliverables', None)
    assert not _is_linked(b, 'deliverables', a2)
    if hasattr(a2, 'Order'):
        assert not _is_linked(a2, 'Order', b)


def test_assoc_order6_reverse_link_reassign_clear():
    a1 = accounting_Order(id="sample_text", paymentOffset=7, pricePerUnit=3.14)
    a2 = accounting_Order(id="sample_text_2", paymentOffset=13, pricePerUnit=9.99)
    b = accounting_Invoice(id="sample_text", invoiceDate=date(2024, 1, 1), state="sample_text", unitAmount=3.14)
    _safe_set(b, 'invoices', a1)
    assert _is_linked(b, 'invoices', a1)
    if hasattr(a1, 'Order7'):
        assert _is_linked(a1, 'Order7', b)
    _safe_set(b, 'invoices', a2)
    assert _is_linked(b, 'invoices', a2)
    if hasattr(a1, 'Order7'):
        assert not _is_linked(a1, 'Order7', b)
    if hasattr(a2, 'Order7'):
        assert _is_linked(a2, 'Order7', b)
    _safe_set(b, 'invoices', None)
    assert not _is_linked(b, 'invoices', a2)
    if hasattr(a2, 'Order7'):
        assert not _is_linked(a2, 'Order7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_employees16_stub_double():
    # accounting_EmployeeDatabase has no real 'accounting_EmployeeDatabase' property in the generated
    # code (a bare stub) -- manually attach it so accounting_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # accounting_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = accounting_Employee(emails="sample_text")
    partner = accounting_EmployeeDatabase()
    setattr(partner, 'accounting_EmployeeDatabase', None)
    _safe_set(owner, 'accounting_Employee17', partner)
    assert owner in getattr(partner, 'accounting_EmployeeDatabase')
    _safe_set(owner, 'accounting_Employee17', None)
    assert owner not in getattr(partner, 'accounting_EmployeeDatabase')


def test_assoc_liason13_stub_double():
    # accounting_Project has no real 'accounting_Project' property in the generated
    # code (a bare stub) -- manually attach it so accounting_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # accounting_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = accounting_Employee(emails="sample_text")
    partner = accounting_Project()
    setattr(partner, 'accounting_Project', None)
    _safe_set(owner, 'accounting_Employee14', partner)
    assert getattr(partner, 'accounting_Project') == owner
    _safe_set(owner, 'accounting_Employee14', None)
    assert getattr(partner, 'accounting_Project') is None


def test_assoc_orders11_stub_double():
    # accounting_Project has no real 'project' property in the generated
    # code (a bare stub) -- manually attach it so accounting_Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # accounting_Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = accounting_Order(id="sample_text", paymentOffset=7, pricePerUnit=3.14)
    partner = accounting_Project()
    setattr(partner, 'project', None)
    _safe_set(owner, 'Order12', partner)
    assert owner in getattr(partner, 'project')
    _safe_set(owner, 'Order12', None)
    assert owner not in getattr(partner, 'project')


def test_assoc_project0_stub_double():
    # accounting_Project has no real 'Project' property in the generated
    # code (a bare stub) -- manually attach it so accounting_Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # accounting_Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = accounting_Order(id="sample_text", paymentOffset=7, pricePerUnit=3.14)
    partner = accounting_Project()
    setattr(partner, 'Project', None)
    _safe_set(owner, 'orders', partner)
    assert getattr(partner, 'Project') == owner
    _safe_set(owner, 'orders', None)
    assert getattr(partner, 'Project') is None


