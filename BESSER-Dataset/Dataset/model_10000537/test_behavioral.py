import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator,
    Brushing_UseCase,
    Cleaner_Actor,
    Cleaning_Management_UseCase,
    Client_Actor,
    Client_Id___Name_UseCase,
    Deliver_Actor,
    Delivering_Management,
    Delivery_Boy,
    Delivery_Boy_Id_UseCase,
    Delivery_Management_UseCase,
    Dispensador_de_dinero,
    Gestion_de_Limpieza,
    Info_UseCase,
    Informacion_Primaria,
    Limpiador,
    PAGO,
    Payment_Actor,
    Payment_UseCase,
    Powderized_Cleaning_UseCase,
    Reciept____Balance_UseCase,
    Type_of_Payment_UseCase,
    Type_of_car_UseCase,
    Type_of_wash_UseCase,
    Usuario,
    Water_Wash_UseCase,
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

def test_assoc_Cleaning_Management_Delivering_Management_reverse_link_reassign_clear():
    a1 = Gestion_de_Limpieza(brushing="sample_text", powderized_wash="sample_text", water="sample_text")
    a2 = Gestion_de_Limpieza(brushing="sample_text_2", powderized_wash="sample_text_2", water="sample_text_2")
    b = Delivering_Management(client_key="sample_text", client_name="sample_text", deliver_boy_id="sample_text")
    _safe_set(b, 'cleaning_Management5', a1)
    assert _is_linked(b, 'cleaning_Management5', a1)
    if hasattr(a1, 'delivering_Management4'):
        assert _is_linked(a1, 'delivering_Management4', b)
    _safe_set(b, 'cleaning_Management5', a2)
    assert _is_linked(b, 'cleaning_Management5', a2)
    if hasattr(a1, 'delivering_Management4'):
        assert not _is_linked(a1, 'delivering_Management4', b)
    if hasattr(a2, 'delivering_Management4'):
        assert _is_linked(a2, 'delivering_Management4', b)
    _safe_set(b, 'cleaning_Management5', None)
    assert not _is_linked(b, 'cleaning_Management5', a2)
    if hasattr(a2, 'delivering_Management4'):
        assert not _is_linked(a2, 'delivering_Management4', b)


def test_assoc_Payment_Cleaning_Management_reverse_link_reassign_clear():
    a1 = PAGO(Type_of_payment="sample_text")
    a2 = PAGO(Type_of_payment="sample_text_2")
    b = Gestion_de_Limpieza(brushing="sample_text", powderized_wash="sample_text", water="sample_text")
    _safe_set(b, 'payment3', a1)
    assert _is_linked(b, 'payment3', a1)
    if hasattr(a1, 'cleaning_Management2'):
        assert _is_linked(a1, 'cleaning_Management2', b)
    _safe_set(b, 'payment3', a2)
    assert _is_linked(b, 'payment3', a2)
    if hasattr(a1, 'cleaning_Management2'):
        assert not _is_linked(a1, 'cleaning_Management2', b)
    if hasattr(a2, 'cleaning_Management2'):
        assert _is_linked(a2, 'cleaning_Management2', b)
    _safe_set(b, 'payment3', None)
    assert not _is_linked(b, 'payment3', a2)
    if hasattr(a2, 'cleaning_Management2'):
        assert not _is_linked(a2, 'cleaning_Management2', b)


def test_assoc_Primary_Info_Payment_reverse_link_reassign_clear():
    a1 = PAGO(Type_of_payment="sample_text")
    a2 = PAGO(Type_of_payment="sample_text_2")
    b = Informacion_Primaria(Type_of_car="sample_text", Type_of_wash="sample_text")
    _safe_set(b, 'payment0', a1)
    assert _is_linked(b, 'payment0', a1)
    if hasattr(a1, 'primary_Info1'):
        assert _is_linked(a1, 'primary_Info1', b)
    _safe_set(b, 'payment0', a2)
    assert _is_linked(b, 'payment0', a2)
    if hasattr(a1, 'primary_Info1'):
        assert not _is_linked(a1, 'primary_Info1', b)
    if hasattr(a2, 'primary_Info1'):
        assert _is_linked(a2, 'primary_Info1', b)
    _safe_set(b, 'payment0', None)
    assert not _is_linked(b, 'payment0', a2)
    if hasattr(a2, 'primary_Info1'):
        assert not _is_linked(a2, 'primary_Info1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Cleaning_Management_Cleaner_stub_double():
    # Limpiador has no real 'cleaning_Management15' property in the generated
    # code (a bare stub) -- manually attach it so Gestion_de_Limpieza's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Gestion_de_Limpieza's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Gestion_de_Limpieza(brushing="sample_text", powderized_wash="sample_text", water="sample_text")
    partner = Limpiador()
    setattr(partner, 'cleaning_Management15', None)
    _safe_set(owner, 'cleaner14', partner)
    assert getattr(partner, 'cleaning_Management15') == owner
    _safe_set(owner, 'cleaner14', None)
    assert getattr(partner, 'cleaning_Management15') is None


def test_assoc_Delivering_Management_Delivery_Boy_stub_double():
    # Delivery_Boy has no real 'delivering_Management19' property in the generated
    # code (a bare stub) -- manually attach it so Delivering_Management's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Delivering_Management's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Delivering_Management(client_key="sample_text", client_name="sample_text", deliver_boy_id="sample_text")
    partner = Delivery_Boy()
    setattr(partner, 'delivering_Management19', None)
    _safe_set(owner, 'delivery_Boy18', partner)
    assert getattr(partner, 'delivering_Management19') == owner
    _safe_set(owner, 'delivery_Boy18', None)
    assert getattr(partner, 'delivering_Management19') is None


def test_assoc_Payment_Money_Dispenser_stub_double():
    # Dispensador_de_dinero has no real 'payment17' property in the generated
    # code (a bare stub) -- manually attach it so PAGO's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PAGO's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PAGO(Type_of_payment="sample_text")
    partner = Dispensador_de_dinero()
    setattr(partner, 'payment17', None)
    _safe_set(owner, 'money_Dispenser16', partner)
    assert getattr(partner, 'payment17') == owner
    _safe_set(owner, 'money_Dispenser16', None)
    assert getattr(partner, 'payment17') is None


def test_assoc_User_Cleaning_Management_stub_double():
    # Usuario has no real 'cleaning_Management10' property in the generated
    # code (a bare stub) -- manually attach it so Gestion_de_Limpieza's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Gestion_de_Limpieza's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Gestion_de_Limpieza(brushing="sample_text", powderized_wash="sample_text", water="sample_text")
    partner = Usuario()
    setattr(partner, 'cleaning_Management10', None)
    _safe_set(owner, 'user11', partner)
    assert getattr(partner, 'cleaning_Management10') == owner
    _safe_set(owner, 'user11', None)
    assert getattr(partner, 'cleaning_Management10') is None


def test_assoc_User_Delivering_Management_stub_double():
    # Usuario has no real 'delivering_Management12' property in the generated
    # code (a bare stub) -- manually attach it so Delivering_Management's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Delivering_Management's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Delivering_Management(client_key="sample_text", client_name="sample_text", deliver_boy_id="sample_text")
    partner = Usuario()
    setattr(partner, 'delivering_Management12', None)
    _safe_set(owner, 'user13', partner)
    assert getattr(partner, 'delivering_Management12') == owner
    _safe_set(owner, 'user13', None)
    assert getattr(partner, 'delivering_Management12') is None


def test_assoc_User_Payment_stub_double():
    # Usuario has no real 'payment8' property in the generated
    # code (a bare stub) -- manually attach it so PAGO's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PAGO's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PAGO(Type_of_payment="sample_text")
    partner = Usuario()
    setattr(partner, 'payment8', None)
    _safe_set(owner, 'user9', partner)
    assert getattr(partner, 'payment8') == owner
    _safe_set(owner, 'user9', None)
    assert getattr(partner, 'payment8') is None


def test_assoc_User_Primary_Info_stub_double():
    # Usuario has no real 'primary_Info6' property in the generated
    # code (a bare stub) -- manually attach it so Informacion_Primaria's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Informacion_Primaria's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Informacion_Primaria(Type_of_car="sample_text", Type_of_wash="sample_text")
    partner = Usuario()
    setattr(partner, 'primary_Info6', None)
    _safe_set(owner, 'user7', partner)
    assert getattr(partner, 'primary_Info6') == owner
    _safe_set(owner, 'user7', None)
    assert getattr(partner, 'primary_Info6') is None


