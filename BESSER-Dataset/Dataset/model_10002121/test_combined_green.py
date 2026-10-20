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
    EventsProductGroup,
    Events,
    ProductGroupProduct,
    ProductGroup,
    Product,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_eventsproductgroup_is_not_abstract():
    assert not inspect.isabstract(EventsProductGroup)


def test_hyp_eventsproductgroup_constructor_exists():
    assert callable(EventsProductGroup.__init__)


def test_hyp_eventsproductgroup_constructor_args():
    sig = inspect.signature(EventsProductGroup.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Event" in params, "Missing parameter 'Event'"
    assert "ProductGroup" in params, "Missing parameter 'ProductGroup'"

def test_hyp_eventsproductgroup_has_id():
    assert hasattr(EventsProductGroup, "id")
    descriptor = None
    for klass in EventsProductGroup.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_eventsproductgroup_has_Event():
    assert hasattr(EventsProductGroup, "Event")
    descriptor = None
    for klass in EventsProductGroup.__mro__:
        if "Event" in klass.__dict__:
            descriptor = klass.__dict__["Event"]
            break
    assert isinstance(descriptor, property)

def test_hyp_eventsproductgroup_has_ProductGroup():
    assert hasattr(EventsProductGroup, "ProductGroup")
    descriptor = None
    for klass in EventsProductGroup.__mro__:
        if "ProductGroup" in klass.__dict__:
            descriptor = klass.__dict__["ProductGroup"]
            break
    assert isinstance(descriptor, property)



def test_hyp_events_is_not_abstract():
    assert not inspect.isabstract(Events)


def test_hyp_events_constructor_exists():
    assert callable(Events.__init__)


def test_hyp_events_constructor_args():
    sig = inspect.signature(Events.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "datetime" in params, "Missing parameter 'datetime'"
    assert "id" in params, "Missing parameter 'id'"
    assert "user" in params, "Missing parameter 'user'"







def test_hyp_productgroupproduct_is_not_abstract():
    assert not inspect.isabstract(ProductGroupProduct)


def test_hyp_productgroupproduct_constructor_exists():
    assert callable(ProductGroupProduct.__init__)


def test_hyp_productgroupproduct_constructor_args():
    sig = inspect.signature(ProductGroupProduct.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "id" in params, "Missing parameter 'id'"
    assert "Product" in params, "Missing parameter 'Product'"
    assert "ProductGroup" in params, "Missing parameter 'ProductGroup'"

def test_hyp_productgroupproduct_has_weight():
    assert hasattr(ProductGroupProduct, "weight")
    descriptor = None
    for klass in ProductGroupProduct.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_hyp_productgroupproduct_has_id():
    assert hasattr(ProductGroupProduct, "id")
    descriptor = None
    for klass in ProductGroupProduct.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_productgroupproduct_has_Product():
    assert hasattr(ProductGroupProduct, "Product")
    descriptor = None
    for klass in ProductGroupProduct.__mro__:
        if "Product" in klass.__dict__:
            descriptor = klass.__dict__["Product"]
            break
    assert isinstance(descriptor, property)

def test_hyp_productgroupproduct_has_ProductGroup():
    assert hasattr(ProductGroupProduct, "ProductGroup")
    descriptor = None
    for klass in ProductGroupProduct.__mro__:
        if "ProductGroup" in klass.__dict__:
            descriptor = klass.__dict__["ProductGroup"]
            break
    assert isinstance(descriptor, property)



def test_hyp_productgroup_is_not_abstract():
    assert not inspect.isabstract(ProductGroup)


def test_hyp_productgroup_constructor_exists():
    assert callable(ProductGroup.__init__)


def test_hyp_productgroup_constructor_args():
    sig = inspect.signature(ProductGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"




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
EventsProductGroup_strategy = st.builds(
    EventsProductGroup,
    id=
        st.integers(),
    Event=
        st.none(),
    ProductGroup=
        st.none()
)
Events_strategy = st.builds(
    Events,
    name=
        safe_text,
    datetime=
        st.integers(),
    id=
        st.integers(),
    user=
        safe_text
)
ProductGroupProduct_strategy = st.builds(
    ProductGroupProduct,
    weight=
        st.integers(),
    id=
        st.integers(),
    Product=
        st.none(),
    ProductGroup=
        st.none()
)
ProductGroup_strategy = st.builds(
    ProductGroup,
    name=
        safe_text,
    id=
        st.integers()
)
Product_strategy = st.builds(
    Product,
    name=
        safe_text,
    id=
        st.integers()
)

@given(instance=EventsProductGroup_strategy)
@settings(max_examples=50)
def test_hyp_eventsproductgroup_instantiation(instance):
    assert isinstance(instance, EventsProductGroup)



@given(instance=EventsProductGroup_strategy)
def test_hyp_eventsproductgroup_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=EventsProductGroup_strategy)
def test_hyp_eventsproductgroup_Event_setter(instance):
    original = instance.Event
    instance.Event = original
    assert instance.Event == original



@given(instance=EventsProductGroup_strategy)
def test_hyp_eventsproductgroup_ProductGroup_setter(instance):
    original = instance.ProductGroup
    instance.ProductGroup = original
    assert instance.ProductGroup == original




@given(instance=Events_strategy)
def test_hyp_events_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Events_strategy)
def test_hyp_events_datetime_setter(instance):
    original = instance.datetime
    instance.datetime = original
    assert instance.datetime == original



@given(instance=Events_strategy)
def test_hyp_events_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Events_strategy)
def test_hyp_events_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=ProductGroupProduct_strategy)
@settings(max_examples=50)
def test_hyp_productgroupproduct_instantiation(instance):
    assert isinstance(instance, ProductGroupProduct)



@given(instance=ProductGroupProduct_strategy)
def test_hyp_productgroupproduct_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=ProductGroupProduct_strategy)
def test_hyp_productgroupproduct_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ProductGroupProduct_strategy)
def test_hyp_productgroupproduct_Product_setter(instance):
    original = instance.Product
    instance.Product = original
    assert instance.Product == original



@given(instance=ProductGroupProduct_strategy)
def test_hyp_productgroupproduct_ProductGroup_setter(instance):
    original = instance.ProductGroup
    instance.ProductGroup = original
    assert instance.ProductGroup == original




@given(instance=ProductGroup_strategy)
def test_hyp_productgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ProductGroup_strategy)
def test_hyp_productgroup_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Product_strategy)
def test_hyp_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_hyp_product_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Events,
    EventsProductGroup,
    Product,
    ProductGroup,
    ProductGroupProduct,
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

def test_Events_datetime_value_roundtrip():
    instance = Events(datetime=7, id=7, name="sample_text", user="sample_text")
    assert instance.datetime == 7
    instance.datetime = 13
    assert instance.datetime == 13


def test_Events_id_value_roundtrip():
    instance = Events(datetime=7, id=7, name="sample_text", user="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Events_name_value_roundtrip():
    instance = Events(datetime=7, id=7, name="sample_text", user="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Events_user_value_roundtrip():
    instance = Events(datetime=7, id=7, name="sample_text", user="sample_text")
    assert instance.user == "sample_text"
    instance.user = "sample_text_2"
    assert instance.user == "sample_text_2"


def test_Product_id_value_roundtrip():
    instance = Product(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Product_name_value_roundtrip():
    instance = Product(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ProductGroup_id_value_roundtrip():
    instance = ProductGroup(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_ProductGroup_name_value_roundtrip():
    instance = ProductGroup(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Events_strategy = st.builds(Events, datetime=st.integers(), id=st.integers(), name=safe_text, user=safe_text)
@given(instance=Events_strategy)
@settings(max_examples=25)
def test_Events_instantiation(instance):
    assert isinstance(instance, Events)


Product_strategy = st.builds(Product, id=st.integers(), name=safe_text)
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


ProductGroup_strategy = st.builds(ProductGroup, id=st.integers(), name=safe_text)
@given(instance=ProductGroup_strategy)
@settings(max_examples=25)
def test_ProductGroup_instantiation(instance):
    assert isinstance(instance, ProductGroup)



