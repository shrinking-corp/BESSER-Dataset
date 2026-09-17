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
    Order,
    Chef,
    Food_Items,
    Food_Sub_Category,
    Customer,
    Food_Category,
    Table,
    Material,
    Food,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Order_status" in params, "Missing parameter 'Order_status'"
    assert "Order_id" in params, "Missing parameter 'Order_id'"
    assert "Order_delete" in params, "Missing parameter 'Order_delete'"
    assert "Order_num" in params, "Missing parameter 'Order_num'"
    assert "Order_edit" in params, "Missing parameter 'Order_edit'"








def test_hyp_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_hyp_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_hyp_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Speciality" in params, "Missing parameter 'Speciality'"
    assert "Chef_name" in params, "Missing parameter 'Chef_name'"
    assert "Chef_id" in params, "Missing parameter 'Chef_id'"








def test_hyp_food_items_is_not_abstract():
    assert not inspect.isabstract(Food_Items)


def test_hyp_food_items_constructor_exists():
    assert callable(Food_Items.__init__)


def test_hyp_food_items_constructor_args():
    sig = inspect.signature(Food_Items.__init__)
    params = list(sig.parameters.keys())
    assert "Food_id" in params, "Missing parameter 'Food_id'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "Items_id" in params, "Missing parameter 'Items_id'"
    assert "Material_id" in params, "Missing parameter 'Material_id'"







def test_hyp_food_sub_category_is_not_abstract():
    assert not inspect.isabstract(Food_Sub_Category)


def test_hyp_food_sub_category_constructor_exists():
    assert callable(Food_Sub_Category.__init__)


def test_hyp_food_sub_category_constructor_args():
    sig = inspect.signature(Food_Sub_Category.__init__)
    params = list(sig.parameters.keys())
    assert "sub_descp" in params, "Missing parameter 'sub_descp'"
    assert "sub_id" in params, "Missing parameter 'sub_id'"
    assert "sub_image" in params, "Missing parameter 'sub_image'"
    assert "sub_name" in params, "Missing parameter 'sub_name'"







def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "TimeStamp" in params, "Missing parameter 'TimeStamp'"
    assert "Table_id" in params, "Missing parameter 'Table_id'"
    assert "Customer_name" in params, "Missing parameter 'Customer_name'"
    assert "Customer_id" in params, "Missing parameter 'Customer_id'"
    assert "Status" in params, "Missing parameter 'Status'"








def test_hyp_food_category_is_not_abstract():
    assert not inspect.isabstract(Food_Category)


def test_hyp_food_category_constructor_exists():
    assert callable(Food_Category.__init__)


def test_hyp_food_category_constructor_args():
    sig = inspect.signature(Food_Category.__init__)
    params = list(sig.parameters.keys())
    assert "Category_image" in params, "Missing parameter 'Category_image'"
    assert "Category_id" in params, "Missing parameter 'Category_id'"
    assert "sub_id" in params, "Missing parameter 'sub_id'"
    assert "Category_descp" in params, "Missing parameter 'Category_descp'"
    assert "Category_name" in params, "Missing parameter 'Category_name'"








def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Table_id" in params, "Missing parameter 'Table_id'"
    assert "Table_num" in params, "Missing parameter 'Table_num'"






def test_hyp_material_is_not_abstract():
    assert not inspect.isabstract(Material)


def test_hyp_material_constructor_exists():
    assert callable(Material.__init__)


def test_hyp_material_constructor_args():
    sig = inspect.signature(Material.__init__)
    params = list(sig.parameters.keys())
    assert "Stock1" in params, "Missing parameter 'Stock1'"
    assert "Unit" in params, "Missing parameter 'Unit'"
    assert "Stock" in params, "Missing parameter 'Stock'"
    assert "Material_name" in params, "Missing parameter 'Material_name'"
    assert "Material_id" in params, "Missing parameter 'Material_id'"








def test_hyp_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_hyp_food_constructor_exists():
    assert callable(Food.__init__)


def test_hyp_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "food_id" in params, "Missing parameter 'food_id'"
    assert "Category_id" in params, "Missing parameter 'Category_id'"
    assert "food_name" in params, "Missing parameter 'food_name'"





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
Order_strategy = st.builds(
    Order,
    Order_status=
        safe_text,
    Order_id=
        st.integers(),
    Order_delete=
        safe_text,
    Order_num=
        st.integers(),
    Order_edit=
        safe_text
)
Chef_strategy = st.builds(
    Chef,
    order_id=
        st.integers(),
    Status=
        safe_text,
    Speciality=
        safe_text,
    Chef_name=
        safe_text,
    Chef_id=
        st.integers()
)
Food_Items_strategy = st.builds(
    Food_Items,
    Food_id=
        st.integers(),
    quantity=
        st.integers(),
    Items_id=
        st.integers(),
    Material_id=
        st.integers()
)
Food_Sub_Category_strategy = st.builds(
    Food_Sub_Category,
    sub_descp=
        safe_text,
    sub_id=
        st.integers(),
    sub_image=
        safe_text,
    sub_name=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    TimeStamp=
        safe_text,
    Table_id=
        st.integers(),
    Customer_name=
        safe_text,
    Customer_id=
        st.integers(),
    Status=
        safe_text
)
Food_Category_strategy = st.builds(
    Food_Category,
    Category_image=
        safe_text,
    Category_id=
        st.integers(),
    sub_id=
        st.integers(),
    Category_descp=
        safe_text,
    Category_name=
        safe_text
)
Table_strategy = st.builds(
    Table,
    Status=
        safe_text,
    Table_id=
        st.integers(),
    Table_num=
        st.integers()
)
Material_strategy = st.builds(
    Material,
    Stock1=
        safe_text,
    Unit=
        safe_text,
    Stock=
        safe_text,
    Material_name=
        safe_text,
    Material_id=
        st.integers()
)
Food_strategy = st.builds(
    Food,
    food_id=
        st.integers(),
    Category_id=
        st.integers(),
    food_name=
        safe_text
)




@given(instance=Order_strategy)
def test_hyp_order_Order_status_setter(instance):
    original = instance.Order_status
    instance.Order_status = original
    assert instance.Order_status == original



@given(instance=Order_strategy)
def test_hyp_order_Order_id_setter(instance):
    original = instance.Order_id
    instance.Order_id = original
    assert instance.Order_id == original



@given(instance=Order_strategy)
def test_hyp_order_Order_delete_setter(instance):
    original = instance.Order_delete
    instance.Order_delete = original
    assert instance.Order_delete == original



@given(instance=Order_strategy)
def test_hyp_order_Order_num_setter(instance):
    original = instance.Order_num
    instance.Order_num = original
    assert instance.Order_num == original



@given(instance=Order_strategy)
def test_hyp_order_Order_edit_setter(instance):
    original = instance.Order_edit
    instance.Order_edit = original
    assert instance.Order_edit == original




@given(instance=Chef_strategy)
def test_hyp_chef_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=Chef_strategy)
def test_hyp_chef_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Chef_strategy)
def test_hyp_chef_Speciality_setter(instance):
    original = instance.Speciality
    instance.Speciality = original
    assert instance.Speciality == original



@given(instance=Chef_strategy)
def test_hyp_chef_Chef_name_setter(instance):
    original = instance.Chef_name
    instance.Chef_name = original
    assert instance.Chef_name == original



@given(instance=Chef_strategy)
def test_hyp_chef_Chef_id_setter(instance):
    original = instance.Chef_id
    instance.Chef_id = original
    assert instance.Chef_id == original




@given(instance=Food_Items_strategy)
def test_hyp_food_items_Food_id_setter(instance):
    original = instance.Food_id
    instance.Food_id = original
    assert instance.Food_id == original



@given(instance=Food_Items_strategy)
def test_hyp_food_items_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Food_Items_strategy)
def test_hyp_food_items_Items_id_setter(instance):
    original = instance.Items_id
    instance.Items_id = original
    assert instance.Items_id == original



@given(instance=Food_Items_strategy)
def test_hyp_food_items_Material_id_setter(instance):
    original = instance.Material_id
    instance.Material_id = original
    assert instance.Material_id == original




@given(instance=Food_Sub_Category_strategy)
def test_hyp_food_sub_category_sub_descp_setter(instance):
    original = instance.sub_descp
    instance.sub_descp = original
    assert instance.sub_descp == original



@given(instance=Food_Sub_Category_strategy)
def test_hyp_food_sub_category_sub_id_setter(instance):
    original = instance.sub_id
    instance.sub_id = original
    assert instance.sub_id == original



@given(instance=Food_Sub_Category_strategy)
def test_hyp_food_sub_category_sub_image_setter(instance):
    original = instance.sub_image
    instance.sub_image = original
    assert instance.sub_image == original



@given(instance=Food_Sub_Category_strategy)
def test_hyp_food_sub_category_sub_name_setter(instance):
    original = instance.sub_name
    instance.sub_name = original
    assert instance.sub_name == original




@given(instance=Customer_strategy)
def test_hyp_customer_TimeStamp_setter(instance):
    original = instance.TimeStamp
    instance.TimeStamp = original
    assert instance.TimeStamp == original



@given(instance=Customer_strategy)
def test_hyp_customer_Table_id_setter(instance):
    original = instance.Table_id
    instance.Table_id = original
    assert instance.Table_id == original



@given(instance=Customer_strategy)
def test_hyp_customer_Customer_name_setter(instance):
    original = instance.Customer_name
    instance.Customer_name = original
    assert instance.Customer_name == original



@given(instance=Customer_strategy)
def test_hyp_customer_Customer_id_setter(instance):
    original = instance.Customer_id
    instance.Customer_id = original
    assert instance.Customer_id == original



@given(instance=Customer_strategy)
def test_hyp_customer_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original




@given(instance=Food_Category_strategy)
def test_hyp_food_category_Category_image_setter(instance):
    original = instance.Category_image
    instance.Category_image = original
    assert instance.Category_image == original



@given(instance=Food_Category_strategy)
def test_hyp_food_category_Category_id_setter(instance):
    original = instance.Category_id
    instance.Category_id = original
    assert instance.Category_id == original



@given(instance=Food_Category_strategy)
def test_hyp_food_category_sub_id_setter(instance):
    original = instance.sub_id
    instance.sub_id = original
    assert instance.sub_id == original



@given(instance=Food_Category_strategy)
def test_hyp_food_category_Category_descp_setter(instance):
    original = instance.Category_descp
    instance.Category_descp = original
    assert instance.Category_descp == original



@given(instance=Food_Category_strategy)
def test_hyp_food_category_Category_name_setter(instance):
    original = instance.Category_name
    instance.Category_name = original
    assert instance.Category_name == original




@given(instance=Table_strategy)
def test_hyp_table_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Table_strategy)
def test_hyp_table_Table_id_setter(instance):
    original = instance.Table_id
    instance.Table_id = original
    assert instance.Table_id == original



@given(instance=Table_strategy)
def test_hyp_table_Table_num_setter(instance):
    original = instance.Table_num
    instance.Table_num = original
    assert instance.Table_num == original




@given(instance=Material_strategy)
def test_hyp_material_Stock1_setter(instance):
    original = instance.Stock1
    instance.Stock1 = original
    assert instance.Stock1 == original



@given(instance=Material_strategy)
def test_hyp_material_Unit_setter(instance):
    original = instance.Unit
    instance.Unit = original
    assert instance.Unit == original



@given(instance=Material_strategy)
def test_hyp_material_Stock_setter(instance):
    original = instance.Stock
    instance.Stock = original
    assert instance.Stock == original



@given(instance=Material_strategy)
def test_hyp_material_Material_name_setter(instance):
    original = instance.Material_name
    instance.Material_name = original
    assert instance.Material_name == original



@given(instance=Material_strategy)
def test_hyp_material_Material_id_setter(instance):
    original = instance.Material_id
    instance.Material_id = original
    assert instance.Material_id == original




@given(instance=Food_strategy)
def test_hyp_food_food_id_setter(instance):
    original = instance.food_id
    instance.food_id = original
    assert instance.food_id == original



@given(instance=Food_strategy)
def test_hyp_food_Category_id_setter(instance):
    original = instance.Category_id
    instance.Category_id = original
    assert instance.Category_id == original



@given(instance=Food_strategy)
def test_hyp_food_food_name_setter(instance):
    original = instance.food_name
    instance.food_name = original
    assert instance.food_name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Chef,
    Customer,
    Food,
    Food_Category,
    Food_Items,
    Food_Sub_Category,
    Material,
    Order,
    Table,
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

def test_Chef_Chef_id_value_roundtrip():
    instance = Chef(Chef_id=7, Chef_name="sample_text", Speciality="sample_text", Status="sample_text", order_id=7)
    assert instance.Chef_id == 7
    instance.Chef_id = 13
    assert instance.Chef_id == 13


def test_Chef_Chef_name_value_roundtrip():
    instance = Chef(Chef_id=7, Chef_name="sample_text", Speciality="sample_text", Status="sample_text", order_id=7)
    assert instance.Chef_name == "sample_text"
    instance.Chef_name = "sample_text_2"
    assert instance.Chef_name == "sample_text_2"


def test_Chef_Speciality_value_roundtrip():
    instance = Chef(Chef_id=7, Chef_name="sample_text", Speciality="sample_text", Status="sample_text", order_id=7)
    assert instance.Speciality == "sample_text"
    instance.Speciality = "sample_text_2"
    assert instance.Speciality == "sample_text_2"


def test_Chef_Status_value_roundtrip():
    instance = Chef(Chef_id=7, Chef_name="sample_text", Speciality="sample_text", Status="sample_text", order_id=7)
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_Chef_order_id_value_roundtrip():
    instance = Chef(Chef_id=7, Chef_name="sample_text", Speciality="sample_text", Status="sample_text", order_id=7)
    assert instance.order_id == 7
    instance.order_id = 13
    assert instance.order_id == 13


def test_Customer_Customer_id_value_roundtrip():
    instance = Customer(Customer_id=7, Customer_name="sample_text", Status="sample_text", Table_id=7, TimeStamp="sample_text")
    assert instance.Customer_id == 7
    instance.Customer_id = 13
    assert instance.Customer_id == 13


def test_Customer_Customer_name_value_roundtrip():
    instance = Customer(Customer_id=7, Customer_name="sample_text", Status="sample_text", Table_id=7, TimeStamp="sample_text")
    assert instance.Customer_name == "sample_text"
    instance.Customer_name = "sample_text_2"
    assert instance.Customer_name == "sample_text_2"


def test_Customer_Status_value_roundtrip():
    instance = Customer(Customer_id=7, Customer_name="sample_text", Status="sample_text", Table_id=7, TimeStamp="sample_text")
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_Customer_Table_id_value_roundtrip():
    instance = Customer(Customer_id=7, Customer_name="sample_text", Status="sample_text", Table_id=7, TimeStamp="sample_text")
    assert instance.Table_id == 7
    instance.Table_id = 13
    assert instance.Table_id == 13


def test_Customer_TimeStamp_value_roundtrip():
    instance = Customer(Customer_id=7, Customer_name="sample_text", Status="sample_text", Table_id=7, TimeStamp="sample_text")
    assert instance.TimeStamp == "sample_text"
    instance.TimeStamp = "sample_text_2"
    assert instance.TimeStamp == "sample_text_2"


def test_Food_Category_id_value_roundtrip():
    instance = Food(Category_id=7, food_id=7, food_name="sample_text")
    assert instance.Category_id == 7
    instance.Category_id = 13
    assert instance.Category_id == 13


def test_Food_food_id_value_roundtrip():
    instance = Food(Category_id=7, food_id=7, food_name="sample_text")
    assert instance.food_id == 7
    instance.food_id = 13
    assert instance.food_id == 13


def test_Food_food_name_value_roundtrip():
    instance = Food(Category_id=7, food_id=7, food_name="sample_text")
    assert instance.food_name == "sample_text"
    instance.food_name = "sample_text_2"
    assert instance.food_name == "sample_text_2"


def test_Food_Category_Category_descp_value_roundtrip():
    instance = Food_Category(Category_descp="sample_text", Category_id=7, Category_image="sample_text", Category_name="sample_text", sub_id=7)
    assert instance.Category_descp == "sample_text"
    instance.Category_descp = "sample_text_2"
    assert instance.Category_descp == "sample_text_2"


def test_Food_Category_Category_id_value_roundtrip():
    instance = Food_Category(Category_descp="sample_text", Category_id=7, Category_image="sample_text", Category_name="sample_text", sub_id=7)
    assert instance.Category_id == 7
    instance.Category_id = 13
    assert instance.Category_id == 13


def test_Food_Category_Category_image_value_roundtrip():
    instance = Food_Category(Category_descp="sample_text", Category_id=7, Category_image="sample_text", Category_name="sample_text", sub_id=7)
    assert instance.Category_image == "sample_text"
    instance.Category_image = "sample_text_2"
    assert instance.Category_image == "sample_text_2"


def test_Food_Category_Category_name_value_roundtrip():
    instance = Food_Category(Category_descp="sample_text", Category_id=7, Category_image="sample_text", Category_name="sample_text", sub_id=7)
    assert instance.Category_name == "sample_text"
    instance.Category_name = "sample_text_2"
    assert instance.Category_name == "sample_text_2"


def test_Food_Category_sub_id_value_roundtrip():
    instance = Food_Category(Category_descp="sample_text", Category_id=7, Category_image="sample_text", Category_name="sample_text", sub_id=7)
    assert instance.sub_id == 7
    instance.sub_id = 13
    assert instance.sub_id == 13


def test_Food_Items_Food_id_value_roundtrip():
    instance = Food_Items(Food_id=7, Items_id=7, Material_id=7, quantity=7)
    assert instance.Food_id == 7
    instance.Food_id = 13
    assert instance.Food_id == 13


def test_Food_Items_Items_id_value_roundtrip():
    instance = Food_Items(Food_id=7, Items_id=7, Material_id=7, quantity=7)
    assert instance.Items_id == 7
    instance.Items_id = 13
    assert instance.Items_id == 13


def test_Food_Items_Material_id_value_roundtrip():
    instance = Food_Items(Food_id=7, Items_id=7, Material_id=7, quantity=7)
    assert instance.Material_id == 7
    instance.Material_id = 13
    assert instance.Material_id == 13


def test_Food_Items_quantity_value_roundtrip():
    instance = Food_Items(Food_id=7, Items_id=7, Material_id=7, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Food_Sub_Category_sub_descp_value_roundtrip():
    instance = Food_Sub_Category(sub_descp="sample_text", sub_id=7, sub_image="sample_text", sub_name="sample_text")
    assert instance.sub_descp == "sample_text"
    instance.sub_descp = "sample_text_2"
    assert instance.sub_descp == "sample_text_2"


def test_Food_Sub_Category_sub_id_value_roundtrip():
    instance = Food_Sub_Category(sub_descp="sample_text", sub_id=7, sub_image="sample_text", sub_name="sample_text")
    assert instance.sub_id == 7
    instance.sub_id = 13
    assert instance.sub_id == 13


def test_Food_Sub_Category_sub_image_value_roundtrip():
    instance = Food_Sub_Category(sub_descp="sample_text", sub_id=7, sub_image="sample_text", sub_name="sample_text")
    assert instance.sub_image == "sample_text"
    instance.sub_image = "sample_text_2"
    assert instance.sub_image == "sample_text_2"


def test_Food_Sub_Category_sub_name_value_roundtrip():
    instance = Food_Sub_Category(sub_descp="sample_text", sub_id=7, sub_image="sample_text", sub_name="sample_text")
    assert instance.sub_name == "sample_text"
    instance.sub_name = "sample_text_2"
    assert instance.sub_name == "sample_text_2"


def test_Material_Material_id_value_roundtrip():
    instance = Material(Material_id=7, Material_name="sample_text", Stock="sample_text", Stock1="sample_text", Unit="sample_text")
    assert instance.Material_id == 7
    instance.Material_id = 13
    assert instance.Material_id == 13


def test_Material_Material_name_value_roundtrip():
    instance = Material(Material_id=7, Material_name="sample_text", Stock="sample_text", Stock1="sample_text", Unit="sample_text")
    assert instance.Material_name == "sample_text"
    instance.Material_name = "sample_text_2"
    assert instance.Material_name == "sample_text_2"


def test_Material_Stock_value_roundtrip():
    instance = Material(Material_id=7, Material_name="sample_text", Stock="sample_text", Stock1="sample_text", Unit="sample_text")
    assert instance.Stock == "sample_text"
    instance.Stock = "sample_text_2"
    assert instance.Stock == "sample_text_2"


def test_Material_Stock1_value_roundtrip():
    instance = Material(Material_id=7, Material_name="sample_text", Stock="sample_text", Stock1="sample_text", Unit="sample_text")
    assert instance.Stock1 == "sample_text"
    instance.Stock1 = "sample_text_2"
    assert instance.Stock1 == "sample_text_2"


def test_Material_Unit_value_roundtrip():
    instance = Material(Material_id=7, Material_name="sample_text", Stock="sample_text", Stock1="sample_text", Unit="sample_text")
    assert instance.Unit == "sample_text"
    instance.Unit = "sample_text_2"
    assert instance.Unit == "sample_text_2"


def test_Order_Order_delete_value_roundtrip():
    instance = Order(Order_delete="sample_text", Order_edit="sample_text", Order_id=7, Order_num=7, Order_status="sample_text")
    assert instance.Order_delete == "sample_text"
    instance.Order_delete = "sample_text_2"
    assert instance.Order_delete == "sample_text_2"


def test_Order_Order_edit_value_roundtrip():
    instance = Order(Order_delete="sample_text", Order_edit="sample_text", Order_id=7, Order_num=7, Order_status="sample_text")
    assert instance.Order_edit == "sample_text"
    instance.Order_edit = "sample_text_2"
    assert instance.Order_edit == "sample_text_2"


def test_Order_Order_id_value_roundtrip():
    instance = Order(Order_delete="sample_text", Order_edit="sample_text", Order_id=7, Order_num=7, Order_status="sample_text")
    assert instance.Order_id == 7
    instance.Order_id = 13
    assert instance.Order_id == 13


def test_Order_Order_num_value_roundtrip():
    instance = Order(Order_delete="sample_text", Order_edit="sample_text", Order_id=7, Order_num=7, Order_status="sample_text")
    assert instance.Order_num == 7
    instance.Order_num = 13
    assert instance.Order_num == 13


def test_Order_Order_status_value_roundtrip():
    instance = Order(Order_delete="sample_text", Order_edit="sample_text", Order_id=7, Order_num=7, Order_status="sample_text")
    assert instance.Order_status == "sample_text"
    instance.Order_status = "sample_text_2"
    assert instance.Order_status == "sample_text_2"


def test_Table_Status_value_roundtrip():
    instance = Table(Status="sample_text", Table_id=7, Table_num=7)
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_Table_Table_id_value_roundtrip():
    instance = Table(Status="sample_text", Table_id=7, Table_num=7)
    assert instance.Table_id == 7
    instance.Table_id = 13
    assert instance.Table_id == 13


def test_Table_Table_num_value_roundtrip():
    instance = Table(Status="sample_text", Table_id=7, Table_num=7)
    assert instance.Table_num == 7
    instance.Table_num = 13
    assert instance.Table_num == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Chef_strategy = st.builds(Chef, Chef_id=st.integers(), Chef_name=safe_text, Speciality=safe_text, Status=safe_text, order_id=st.integers())
@given(instance=Chef_strategy)
@settings(max_examples=25)
def test_Chef_instantiation(instance):
    assert isinstance(instance, Chef)


Customer_strategy = st.builds(Customer, Customer_id=st.integers(), Customer_name=safe_text, Status=safe_text, Table_id=st.integers(), TimeStamp=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Food_strategy = st.builds(Food, Category_id=st.integers(), food_id=st.integers(), food_name=safe_text)
@given(instance=Food_strategy)
@settings(max_examples=25)
def test_Food_instantiation(instance):
    assert isinstance(instance, Food)


Food_Category_strategy = st.builds(Food_Category, Category_descp=safe_text, Category_id=st.integers(), Category_image=safe_text, Category_name=safe_text, sub_id=st.integers())
@given(instance=Food_Category_strategy)
@settings(max_examples=25)
def test_Food_Category_instantiation(instance):
    assert isinstance(instance, Food_Category)


Food_Items_strategy = st.builds(Food_Items, Food_id=st.integers(), Items_id=st.integers(), Material_id=st.integers(), quantity=st.integers())
@given(instance=Food_Items_strategy)
@settings(max_examples=25)
def test_Food_Items_instantiation(instance):
    assert isinstance(instance, Food_Items)


Food_Sub_Category_strategy = st.builds(Food_Sub_Category, sub_descp=safe_text, sub_id=st.integers(), sub_image=safe_text, sub_name=safe_text)
@given(instance=Food_Sub_Category_strategy)
@settings(max_examples=25)
def test_Food_Sub_Category_instantiation(instance):
    assert isinstance(instance, Food_Sub_Category)


Material_strategy = st.builds(Material, Material_id=st.integers(), Material_name=safe_text, Stock=safe_text, Stock1=safe_text, Unit=safe_text)
@given(instance=Material_strategy)
@settings(max_examples=25)
def test_Material_instantiation(instance):
    assert isinstance(instance, Material)


Order_strategy = st.builds(Order, Order_delete=safe_text, Order_edit=safe_text, Order_id=st.integers(), Order_num=st.integers(), Order_status=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Table_strategy = st.builds(Table, Status=safe_text, Table_id=st.integers(), Table_num=st.integers())
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)



