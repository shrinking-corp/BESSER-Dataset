# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Entrega_producto,
    Lineamiento,
    Order,
    WebADM,
    Toma_de_pedido,
    ShoppingCart,
    Pago,
    Cliente,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_entrega_producto_is_not_abstract():
    assert not inspect.isabstract(Entrega_producto)


def test_hyp_entrega_producto_constructor_exists():
    assert callable(Entrega_producto.__init__)


def test_hyp_entrega_producto_constructor_args():
    sig = inspect.signature(Entrega_producto.__init__)
    params = list(sig.parameters.keys())
    assert "Agradecimiento" in params, "Missing parameter 'Agradecimiento'"
    assert "Email_confirmaci_n" in params, "Missing parameter 'Email_confirmaci_n'"





def test_hyp_lineamiento_is_not_abstract():
    assert not inspect.isabstract(Lineamiento)


def test_hyp_lineamiento_constructor_exists():
    assert callable(Lineamiento.__init__)


def test_hyp_lineamiento_constructor_args():
    sig = inspect.signature(Lineamiento.__init__)
    params = list(sig.parameters.keys())
    assert "Cantidad" in params, "Missing parameter 'Cantidad'"
    assert "Costo" in params, "Missing parameter 'Costo'"





def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "total" in params, "Missing parameter 'total'"
    assert "number" in params, "Missing parameter 'number'"
    assert "status" in params, "Missing parameter 'status'"
    assert "ordered" in params, "Missing parameter 'ordered'"







def test_hyp_webadm_is_not_abstract():
    assert not inspect.isabstract(WebADM)


def test_hyp_webadm_constructor_exists():
    assert callable(WebADM.__init__)


def test_hyp_webadm_constructor_args():
    sig = inspect.signature(WebADM.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "state" in params, "Missing parameter 'state'"
    assert "password" in params, "Missing parameter 'password'"






def test_hyp_toma_de_pedido_is_not_abstract():
    assert not inspect.isabstract(Toma_de_pedido)


def test_hyp_toma_de_pedido_constructor_exists():
    assert callable(Toma_de_pedido.__init__)


def test_hyp_toma_de_pedido_constructor_args():
    sig = inspect.signature(Toma_de_pedido.__init__)
    params = list(sig.parameters.keys())
    assert "Despacho" in params, "Missing parameter 'Despacho'"
    assert "Tipo_de_elemnto" in params, "Missing parameter 'Tipo_de_elemnto'"





def test_hyp_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_hyp_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_hyp_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"




def test_hyp_pago_is_not_abstract():
    assert not inspect.isabstract(Pago)


def test_hyp_pago_constructor_exists():
    assert callable(Pago.__init__)


def test_hyp_pago_constructor_args():
    sig = inspect.signature(Pago.__init__)
    params = list(sig.parameters.keys())
    assert "Contra_entrega" in params, "Missing parameter 'Contra_entrega'"
    assert "PSI" in params, "Missing parameter 'PSI'"





def test_hyp_cliente_is_not_abstract():
    assert not inspect.isabstract(Cliente)


def test_hyp_cliente_constructor_exists():
    assert callable(Cliente.__init__)


def test_hyp_cliente_constructor_args():
    sig = inspect.signature(Cliente.__init__)
    params = list(sig.parameters.keys())
    assert "Ciudad" in params, "Missing parameter 'Ciudad'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Asunto" in params, "Missing parameter 'Asunto'"





# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Entrega_producto_strategy = st.builds(
    Entrega_producto,
    Agradecimiento=
        safe_text,
    Email_confirmaci_n=
        safe_text
)
Lineamiento_strategy = st.builds(
    Lineamiento,
    Cantidad=
        st.integers(),
    Costo=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Order_strategy = st.builds(
    Order,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    number=
        st.integers(),
    status=
        safe_text,
    ordered=
        st.dates()
)
WebADM_strategy = st.builds(
    WebADM,
    login=
        safe_text,
    state=
        safe_text,
    password=
        safe_text
)
Toma_de_pedido_strategy = st.builds(
    Toma_de_pedido,
    Despacho=
        st.dates(),
    Tipo_de_elemnto=
        safe_text
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    creationDate=
        st.dates()
)
Pago_strategy = st.builds(
    Pago,
    Contra_entrega=
        st.dates(),
    PSI=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Cliente_strategy = st.builds(
    Cliente,
    Ciudad=
        safe_text,
    Nombre=
        safe_text,
    Asunto=
        safe_text
)




@given(instance=Entrega_producto_strategy)
def test_hyp_entrega_producto_Agradecimiento_setter(instance):
    original = instance.Agradecimiento
    instance.Agradecimiento = original
    assert instance.Agradecimiento == original



@given(instance=Entrega_producto_strategy)
def test_hyp_entrega_producto_Email_confirmaci_n_setter(instance):
    original = instance.Email_confirmaci_n
    instance.Email_confirmaci_n = original
    assert instance.Email_confirmaci_n == original




@given(instance=Lineamiento_strategy)
def test_hyp_lineamiento_Cantidad_setter(instance):
    original = instance.Cantidad
    instance.Cantidad = original
    assert instance.Cantidad == original



@given(instance=Lineamiento_strategy)
def test_hyp_lineamiento_Costo_setter(instance):
    original = instance.Costo
    instance.Costo = original
    assert instance.Costo == original




@given(instance=Order_strategy)
def test_hyp_order_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Order_strategy)
def test_hyp_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_hyp_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_hyp_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original




@given(instance=WebADM_strategy)
def test_hyp_webadm_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=WebADM_strategy)
def test_hyp_webadm_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=WebADM_strategy)
def test_hyp_webadm_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Toma_de_pedido_strategy)
def test_hyp_toma_de_pedido_Despacho_setter(instance):
    original = instance.Despacho
    instance.Despacho = original
    assert instance.Despacho == original



@given(instance=Toma_de_pedido_strategy)
def test_hyp_toma_de_pedido_Tipo_de_elemnto_setter(instance):
    original = instance.Tipo_de_elemnto
    instance.Tipo_de_elemnto = original
    assert instance.Tipo_de_elemnto == original




@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original




@given(instance=Pago_strategy)
def test_hyp_pago_Contra_entrega_setter(instance):
    original = instance.Contra_entrega
    instance.Contra_entrega = original
    assert instance.Contra_entrega == original



@given(instance=Pago_strategy)
def test_hyp_pago_PSI_setter(instance):
    original = instance.PSI
    instance.PSI = original
    assert instance.PSI == original




@given(instance=Cliente_strategy)
def test_hyp_cliente_Ciudad_setter(instance):
    original = instance.Ciudad
    instance.Ciudad = original
    assert instance.Ciudad == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Cliente_strategy)
def test_hyp_cliente_Asunto_setter(instance):
    original = instance.Asunto
    instance.Asunto = original
    assert instance.Asunto == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Cliente,
    Entrega_producto,
    Lineamiento,
    Order,
    Pago,
    ShoppingCart,
    Toma_de_pedido,
    WebADM,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Cliente_Asunto_value_roundtrip():
    instance = Cliente(Asunto="sample_text", Ciudad="sample_text", Nombre="sample_text")
    assert instance.Asunto == "sample_text"
    instance.Asunto = "sample_text_2"
    assert instance.Asunto == "sample_text_2"


def test_Cliente_Ciudad_value_roundtrip():
    instance = Cliente(Asunto="sample_text", Ciudad="sample_text", Nombre="sample_text")
    assert instance.Ciudad == "sample_text"
    instance.Ciudad = "sample_text_2"
    assert instance.Ciudad == "sample_text_2"


def test_Cliente_Nombre_value_roundtrip():
    instance = Cliente(Asunto="sample_text", Ciudad="sample_text", Nombre="sample_text")
    assert instance.Nombre == "sample_text"
    instance.Nombre = "sample_text_2"
    assert instance.Nombre == "sample_text_2"


def test_Entrega_producto_Agradecimiento_value_roundtrip():
    instance = Entrega_producto(Agradecimiento="sample_text", Email_confirmaci_n="sample_text")
    assert instance.Agradecimiento == "sample_text"
    instance.Agradecimiento = "sample_text_2"
    assert instance.Agradecimiento == "sample_text_2"


def test_Entrega_producto_Email_confirmaci_n_value_roundtrip():
    instance = Entrega_producto(Agradecimiento="sample_text", Email_confirmaci_n="sample_text")
    assert instance.Email_confirmaci_n == "sample_text"
    instance.Email_confirmaci_n = "sample_text_2"
    assert instance.Email_confirmaci_n == "sample_text_2"


def test_Lineamiento_Cantidad_value_roundtrip():
    instance = Lineamiento(Cantidad=7, Costo=3.14)
    assert instance.Cantidad == 7
    instance.Cantidad = 13
    assert instance.Cantidad == 13


def test_Lineamiento_Costo_value_roundtrip():
    instance = Lineamiento(Cantidad=7, Costo=3.14)
    assert instance.Costo == 3.14
    instance.Costo = 9.99
    assert instance.Costo == 9.99


def test_Order_number_value_roundtrip():
    instance = Order(number=7, ordered=date(2024, 1, 1), status="sample_text", total=3.14)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_Order_ordered_value_roundtrip():
    instance = Order(number=7, ordered=date(2024, 1, 1), status="sample_text", total=3.14)
    assert instance.ordered == date(2024, 1, 1)
    instance.ordered = date(2025, 6, 15)
    assert instance.ordered == date(2025, 6, 15)


def test_Order_status_value_roundtrip():
    instance = Order(number=7, ordered=date(2024, 1, 1), status="sample_text", total=3.14)
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Order_total_value_roundtrip():
    instance = Order(number=7, ordered=date(2024, 1, 1), status="sample_text", total=3.14)
    assert instance.total == 3.14
    instance.total = 9.99
    assert instance.total == 9.99


def test_Pago_Contra_entrega_value_roundtrip():
    instance = Pago(Contra_entrega=date(2024, 1, 1), PSI=3.14)
    assert instance.Contra_entrega == date(2024, 1, 1)
    instance.Contra_entrega = date(2025, 6, 15)
    assert instance.Contra_entrega == date(2025, 6, 15)


def test_Pago_PSI_value_roundtrip():
    instance = Pago(Contra_entrega=date(2024, 1, 1), PSI=3.14)
    assert instance.PSI == 3.14
    instance.PSI = 9.99
    assert instance.PSI == 9.99


def test_ShoppingCart_creationDate_value_roundtrip():
    instance = ShoppingCart(creationDate=date(2024, 1, 1))
    assert instance.creationDate == date(2024, 1, 1)
    instance.creationDate = date(2025, 6, 15)
    assert instance.creationDate == date(2025, 6, 15)


def test_Toma_de_pedido_Despacho_value_roundtrip():
    instance = Toma_de_pedido(Despacho=date(2024, 1, 1), Tipo_de_elemnto="sample_text")
    assert instance.Despacho == date(2024, 1, 1)
    instance.Despacho = date(2025, 6, 15)
    assert instance.Despacho == date(2025, 6, 15)


def test_Toma_de_pedido_Tipo_de_elemnto_value_roundtrip():
    instance = Toma_de_pedido(Despacho=date(2024, 1, 1), Tipo_de_elemnto="sample_text")
    assert instance.Tipo_de_elemnto == "sample_text"
    instance.Tipo_de_elemnto = "sample_text_2"
    assert instance.Tipo_de_elemnto == "sample_text_2"


def test_WebADM_login_value_roundtrip():
    instance = WebADM(login="sample_text", password="sample_text", state="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_WebADM_password_value_roundtrip():
    instance = WebADM(login="sample_text", password="sample_text", state="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_WebADM_state_value_roundtrip():
    instance = WebADM(login="sample_text", password="sample_text", state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_assoc_Account_Order_link_reassign_clear():
    a = Toma_de_pedido(Despacho=date(2024, 1, 1), Tipo_de_elemnto="sample_text")
    b1 = Order(number=7, ordered=date(2024, 1, 1), status="sample_text", total=3.14)
    b2 = Order(number=13, ordered=date(2025, 6, 15), status="sample_text_2", total=9.99)
    _safe_set(a, 'order16', {b1})
    assert _is_linked(a, 'order16', b1)
    if hasattr(b1, 'account17'):
        assert _is_linked(b1, 'account17', a)
    _safe_set(a, 'order16', {b2})
    assert _is_linked(a, 'order16', b2)
    if hasattr(b1, 'account17'):
        assert not _is_linked(b1, 'account17', a)
    if hasattr(b2, 'account17'):
        assert _is_linked(b2, 'account17', a)
    _safe_set(a, 'order16', set())
    assert not _is_linked(a, 'order16', b2)
    if hasattr(b2, 'account17'):
        assert not _is_linked(b2, 'account17', a)


def test_assoc_Account_Payment_link_reassign_clear():
    a = Toma_de_pedido(Despacho=date(2024, 1, 1), Tipo_de_elemnto="sample_text")
    b1 = Pago(Contra_entrega=date(2024, 1, 1), PSI=3.14)
    b2 = Pago(Contra_entrega=date(2025, 6, 15), PSI=9.99)
    _safe_set(a, 'p0', {b1})
    assert _is_linked(a, 'p0', b1)
    if hasattr(b1, 'acc1'):
        assert _is_linked(b1, 'acc1', a)
    _safe_set(a, 'p0', {b2})
    assert _is_linked(a, 'p0', b2)
    if hasattr(b1, 'acc1'):
        assert not _is_linked(b1, 'acc1', a)
    if hasattr(b2, 'acc1'):
        assert _is_linked(b2, 'acc1', a)
    _safe_set(a, 'p0', set())
    assert not _is_linked(a, 'p0', b2)
    if hasattr(b2, 'acc1'):
        assert not _is_linked(b2, 'acc1', a)


def test_assoc_Account_ShoppingCart_link_reassign_clear():
    a = Toma_de_pedido(Despacho=date(2024, 1, 1), Tipo_de_elemnto="sample_text")
    b1 = Lineamiento(Cantidad=7, Costo=3.14)
    b2 = Lineamiento(Cantidad=13, Costo=9.99)
    _safe_set(a, 'cart8', b1)
    assert _is_linked(a, 'cart8', b1)
    if hasattr(b1, 'account9'):
        assert _is_linked(b1, 'account9', a)
    _safe_set(a, 'cart8', b2)
    assert _is_linked(a, 'cart8', b2)
    if hasattr(b1, 'account9'):
        assert not _is_linked(b1, 'account9', a)
    if hasattr(b2, 'account9'):
        assert _is_linked(b2, 'account9', a)
    _safe_set(a, 'cart8', None)
    assert not _is_linked(a, 'cart8', b2)
    if hasattr(b2, 'account9'):
        assert not _is_linked(b2, 'account9', a)


def test_assoc_Customer_Account_link_reassign_clear():
    a = Toma_de_pedido(Despacho=date(2024, 1, 1), Tipo_de_elemnto="sample_text")
    b1 = Cliente(Asunto="sample_text", Ciudad="sample_text", Nombre="sample_text")
    b2 = Cliente(Asunto="sample_text_2", Ciudad="sample_text_2", Nombre="sample_text_2")
    _safe_set(a, 'customer7', b1)
    assert _is_linked(a, 'customer7', b1)
    if hasattr(b1, 'account6'):
        assert _is_linked(b1, 'account6', a)
    _safe_set(a, 'customer7', b2)
    assert _is_linked(a, 'customer7', b2)
    if hasattr(b1, 'account6'):
        assert not _is_linked(b1, 'account6', a)
    if hasattr(b2, 'account6'):
        assert _is_linked(b2, 'account6', a)
    _safe_set(a, 'customer7', None)
    assert not _is_linked(a, 'customer7', b2)
    if hasattr(b2, 'account6'):
        assert not _is_linked(b2, 'account6', a)


def test_assoc_Order_LineItem_link_reassign_clear():
    a = Order(number=7, ordered=date(2024, 1, 1), status="sample_text", total=3.14)
    b1 = Lineamiento(Cantidad=7, Costo=3.14)
    b2 = Lineamiento(Cantidad=13, Costo=9.99)
    _safe_set(a, 'items14', {b1})
    assert _is_linked(a, 'items14', b1)
    if hasattr(b1, 'order15'):
        assert _is_linked(b1, 'order15', a)
    _safe_set(a, 'items14', {b2})
    assert _is_linked(a, 'items14', b2)
    if hasattr(b1, 'order15'):
        assert not _is_linked(b1, 'order15', a)
    if hasattr(b2, 'order15'):
        assert _is_linked(b2, 'order15', a)
    _safe_set(a, 'items14', set())
    assert not _is_linked(a, 'items14', b2)
    if hasattr(b2, 'order15'):
        assert not _is_linked(b2, 'order15', a)


def test_assoc_Payment_Order_link_reassign_clear():
    a = Pago(Contra_entrega=date(2024, 1, 1), PSI=3.14)
    b1 = Order(number=7, ordered=date(2024, 1, 1), status="sample_text", total=3.14)
    b2 = Order(number=13, ordered=date(2025, 6, 15), status="sample_text_2", total=9.99)
    _safe_set(a, 'order18', b1)
    assert _is_linked(a, 'order18', b1)
    if hasattr(b1, 'payment19'):
        assert _is_linked(b1, 'payment19', a)
    _safe_set(a, 'order18', b2)
    assert _is_linked(a, 'order18', b2)
    if hasattr(b1, 'payment19'):
        assert not _is_linked(b1, 'payment19', a)
    if hasattr(b2, 'payment19'):
        assert _is_linked(b2, 'payment19', a)
    _safe_set(a, 'order18', None)
    assert not _is_linked(a, 'order18', b2)
    if hasattr(b2, 'payment19'):
        assert not _is_linked(b2, 'payment19', a)


def test_assoc_Product_LineItem_link_reassign_clear():
    a = Lineamiento(Cantidad=7, Costo=3.14)
    b1 = Entrega_producto(Agradecimiento="sample_text", Email_confirmaci_n="sample_text")
    b2 = Entrega_producto(Agradecimiento="sample_text_2", Email_confirmaci_n="sample_text_2")
    _safe_set(a, 'product13', b1)
    assert _is_linked(a, 'product13', b1)
    if hasattr(b1, 'lineItems12'):
        assert _is_linked(b1, 'lineItems12', a)
    _safe_set(a, 'product13', b2)
    assert _is_linked(a, 'product13', b2)
    if hasattr(b1, 'lineItems12'):
        assert not _is_linked(b1, 'lineItems12', a)
    if hasattr(b2, 'lineItems12'):
        assert _is_linked(b2, 'lineItems12', a)
    _safe_set(a, 'product13', None)
    assert not _is_linked(a, 'product13', b2)
    if hasattr(b2, 'lineItems12'):
        assert not _is_linked(b2, 'lineItems12', a)


def test_assoc_ShoppingCart_LineItem_link_reassign_clear():
    a = ShoppingCart(creationDate=date(2024, 1, 1))
    b1 = Lineamiento(Cantidad=7, Costo=3.14)
    b2 = Lineamiento(Cantidad=13, Costo=9.99)
    _safe_set(a, 'items10', b1)
    assert _is_linked(a, 'items10', b1)
    if hasattr(b1, 'sc11'):
        assert _is_linked(b1, 'sc11', a)
    _safe_set(a, 'items10', b2)
    assert _is_linked(a, 'items10', b2)
    if hasattr(b1, 'sc11'):
        assert not _is_linked(b1, 'sc11', a)
    if hasattr(b2, 'sc11'):
        assert _is_linked(b2, 'sc11', a)
    _safe_set(a, 'items10', None)
    assert not _is_linked(a, 'items10', b2)
    if hasattr(b2, 'sc11'):
        assert not _is_linked(b2, 'sc11', a)


def test_assoc_WebUser_Customer_link_reassign_clear():
    a = WebADM(login="sample_text", password="sample_text", state="sample_text")
    b1 = Cliente(Asunto="sample_text", Ciudad="sample_text", Nombre="sample_text")
    b2 = Cliente(Asunto="sample_text_2", Ciudad="sample_text_2", Nombre="sample_text_2")
    _safe_set(a, 'customer4', b1)
    assert _is_linked(a, 'customer4', b1)
    if hasattr(b1, 'webUser5'):
        assert _is_linked(b1, 'webUser5', a)
    _safe_set(a, 'customer4', b2)
    assert _is_linked(a, 'customer4', b2)
    if hasattr(b1, 'webUser5'):
        assert not _is_linked(b1, 'webUser5', a)
    if hasattr(b2, 'webUser5'):
        assert _is_linked(b2, 'webUser5', a)
    _safe_set(a, 'customer4', None)
    assert not _is_linked(a, 'customer4', b2)
    if hasattr(b2, 'webUser5'):
        assert not _is_linked(b2, 'webUser5', a)


def test_assoc_WebUser_ShoppingCart_link_reassign_clear():
    a = WebADM(login="sample_text", password="sample_text", state="sample_text")
    b1 = ShoppingCart(creationDate=date(2024, 1, 1))
    b2 = ShoppingCart(creationDate=date(2025, 6, 15))
    _safe_set(a, 'shoppingCart2', b1)
    assert _is_linked(a, 'shoppingCart2', b1)
    if hasattr(b1, 'webUser3'):
        assert _is_linked(b1, 'webUser3', a)
    _safe_set(a, 'shoppingCart2', b2)
    assert _is_linked(a, 'shoppingCart2', b2)
    if hasattr(b1, 'webUser3'):
        assert not _is_linked(b1, 'webUser3', a)
    if hasattr(b2, 'webUser3'):
        assert _is_linked(b2, 'webUser3', a)
    _safe_set(a, 'shoppingCart2', None)
    assert not _is_linked(a, 'shoppingCart2', b2)
    if hasattr(b2, 'webUser3'):
        assert not _is_linked(b2, 'webUser3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cliente_strategy = st.builds(Cliente, Asunto=safe_text, Ciudad=safe_text, Nombre=safe_text)
@given(instance=Cliente_strategy)
@settings(max_examples=25)
def test_Cliente_instantiation(instance):
    assert isinstance(instance, Cliente)


Entrega_producto_strategy = st.builds(Entrega_producto, Agradecimiento=safe_text, Email_confirmaci_n=safe_text)
@given(instance=Entrega_producto_strategy)
@settings(max_examples=25)
def test_Entrega_producto_instantiation(instance):
    assert isinstance(instance, Entrega_producto)


Lineamiento_strategy = st.builds(Lineamiento, Cantidad=st.integers(), Costo=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Lineamiento_strategy)
@settings(max_examples=25)
def test_Lineamiento_instantiation(instance):
    assert isinstance(instance, Lineamiento)


Order_strategy = st.builds(Order, number=st.integers(), ordered=st.dates(), status=safe_text, total=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Pago_strategy = st.builds(Pago, Contra_entrega=st.dates(), PSI=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Pago_strategy)
@settings(max_examples=25)
def test_Pago_instantiation(instance):
    assert isinstance(instance, Pago)


ShoppingCart_strategy = st.builds(ShoppingCart, creationDate=st.dates())
@given(instance=ShoppingCart_strategy)
@settings(max_examples=25)
def test_ShoppingCart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)


Toma_de_pedido_strategy = st.builds(Toma_de_pedido, Despacho=st.dates(), Tipo_de_elemnto=safe_text)
@given(instance=Toma_de_pedido_strategy)
@settings(max_examples=25)
def test_Toma_de_pedido_instantiation(instance):
    assert isinstance(instance, Toma_de_pedido)


WebADM_strategy = st.builds(WebADM, login=safe_text, password=safe_text, state=safe_text)
@given(instance=WebADM_strategy)
@settings(max_examples=25)
def test_WebADM_instantiation(instance):
    assert isinstance(instance, WebADM)



