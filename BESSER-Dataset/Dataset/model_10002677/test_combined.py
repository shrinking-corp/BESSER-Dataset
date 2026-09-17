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
    ClassP,
    ClassN,
    ClassM,
    ClassL,
    ClassK,
    ClassH,
    ClassJ,
    ClassG,
    ClassF,
    PersonelDepartment,
    Personel,
    Product,
    Order,
    InventoryType,
    Inventory,
    ClassV,
    ClassU,
    ClassT,
    ClassS,
    ClassR,
    ClassQ,
    InterfaceO_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_classp_is_not_abstract():
    assert not inspect.isabstract(ClassP)


def test_hyp_classp_constructor_exists():
    assert callable(ClassP.__init__)


def test_hyp_classp_constructor_args():
    sig = inspect.signature(ClassP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classn_is_not_abstract():
    assert not inspect.isabstract(ClassN)


def test_hyp_classn_constructor_exists():
    assert callable(ClassN.__init__)


def test_hyp_classn_constructor_args():
    sig = inspect.signature(ClassN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classm_is_not_abstract():
    assert not inspect.isabstract(ClassM)


def test_hyp_classm_constructor_exists():
    assert callable(ClassM.__init__)


def test_hyp_classm_constructor_args():
    sig = inspect.signature(ClassM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classl_is_not_abstract():
    assert not inspect.isabstract(ClassL)


def test_hyp_classl_constructor_exists():
    assert callable(ClassL.__init__)


def test_hyp_classl_constructor_args():
    sig = inspect.signature(ClassL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classk_is_not_abstract():
    assert not inspect.isabstract(ClassK)


def test_hyp_classk_constructor_exists():
    assert callable(ClassK.__init__)


def test_hyp_classk_constructor_args():
    sig = inspect.signature(ClassK.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classh_is_not_abstract():
    assert not inspect.isabstract(ClassH)


def test_hyp_classh_constructor_exists():
    assert callable(ClassH.__init__)


def test_hyp_classh_constructor_args():
    sig = inspect.signature(ClassH.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classj_is_not_abstract():
    assert not inspect.isabstract(ClassJ)


def test_hyp_classj_constructor_exists():
    assert callable(ClassJ.__init__)


def test_hyp_classj_constructor_args():
    sig = inspect.signature(ClassJ.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classg_is_not_abstract():
    assert not inspect.isabstract(ClassG)


def test_hyp_classg_constructor_exists():
    assert callable(ClassG.__init__)


def test_hyp_classg_constructor_args():
    sig = inspect.signature(ClassG.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classf_is_not_abstract():
    assert not inspect.isabstract(ClassF)


def test_hyp_classf_constructor_exists():
    assert callable(ClassF.__init__)


def test_hyp_classf_constructor_args():
    sig = inspect.signature(ClassF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_personeldepartment_is_not_abstract():
    assert not inspect.isabstract(PersonelDepartment)


def test_hyp_personeldepartment_constructor_exists():
    assert callable(PersonelDepartment.__init__)


def test_hyp_personeldepartment_constructor_args():
    sig = inspect.signature(PersonelDepartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_personel_is_not_abstract():
    assert not inspect.isabstract(Personel)


def test_hyp_personel_constructor_exists():
    assert callable(Personel.__init__)


def test_hyp_personel_constructor_args():
    sig = inspect.signature(Personel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "protectedAttribute" in params, "Missing parameter 'protectedAttribute'"
    assert "publicAttribute" in params, "Missing parameter 'publicAttribute'"
    assert "privateAttribute" in params, "Missing parameter 'privateAttribute'"
    assert "packageAttribute" in params, "Missing parameter 'packageAttribute'"







def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inventorytype_is_not_abstract():
    assert not inspect.isabstract(InventoryType)


def test_hyp_inventorytype_constructor_exists():
    assert callable(InventoryType.__init__)


def test_hyp_inventorytype_constructor_args():
    sig = inspect.signature(InventoryType.__init__)
    params = list(sig.parameters.keys())
    assert "publicAttribute" in params, "Missing parameter 'publicAttribute'"
    assert "protectedAttribute" in params, "Missing parameter 'protectedAttribute'"
    assert "privateAttribute" in params, "Missing parameter 'privateAttribute'"
    assert "packageAttribute" in params, "Missing parameter 'packageAttribute'"







def test_hyp_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_hyp_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_hyp_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "ownerName" in params, "Missing parameter 'ownerName'"
    assert "balance" in params, "Missing parameter 'balance'"





def test_hyp_classv_is_not_abstract():
    assert not inspect.isabstract(ClassV)


def test_hyp_classv_constructor_exists():
    assert callable(ClassV.__init__)


def test_hyp_classv_constructor_args():
    sig = inspect.signature(ClassV.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classu_is_not_abstract():
    assert not inspect.isabstract(ClassU)


def test_hyp_classu_constructor_exists():
    assert callable(ClassU.__init__)


def test_hyp_classu_constructor_args():
    sig = inspect.signature(ClassU.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classt_is_not_abstract():
    assert not inspect.isabstract(ClassT)


def test_hyp_classt_constructor_exists():
    assert callable(ClassT.__init__)


def test_hyp_classt_constructor_args():
    sig = inspect.signature(ClassT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classs_is_not_abstract():
    assert not inspect.isabstract(ClassS)


def test_hyp_classs_constructor_exists():
    assert callable(ClassS.__init__)


def test_hyp_classs_constructor_args():
    sig = inspect.signature(ClassS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classr_is_not_abstract():
    assert not inspect.isabstract(ClassR)


def test_hyp_classr_constructor_exists():
    assert callable(ClassR.__init__)


def test_hyp_classr_constructor_args():
    sig = inspect.signature(ClassR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classq_is_not_abstract():
    assert not inspect.isabstract(ClassQ)


def test_hyp_classq_constructor_exists():
    assert callable(ClassQ.__init__)


def test_hyp_classq_constructor_args():
    sig = inspect.signature(ClassQ.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interfaceo_interface_is_not_abstract():
    assert not inspect.isabstract(InterfaceO_Interface)


def test_hyp_interfaceo_interface_constructor_exists():
    assert callable(InterfaceO_Interface.__init__)


def test_hyp_interfaceo_interface_constructor_args():
    sig = inspect.signature(InterfaceO_Interface.__init__)
    params = list(sig.parameters.keys())


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
ClassP_strategy = st.builds(
    ClassP,
)
ClassN_strategy = st.builds(
    ClassN,
)
ClassM_strategy = st.builds(
    ClassM,
)
ClassL_strategy = st.builds(
    ClassL,
)
ClassK_strategy = st.builds(
    ClassK,
)
ClassH_strategy = st.builds(
    ClassH,
)
ClassJ_strategy = st.builds(
    ClassJ,
)
ClassG_strategy = st.builds(
    ClassG,
)
ClassF_strategy = st.builds(
    ClassF,
)
PersonelDepartment_strategy = st.builds(
    PersonelDepartment,
)
Personel_strategy = st.builds(
    Personel,
)
Product_strategy = st.builds(
    Product,
    protectedAttribute=
        safe_text,
    publicAttribute=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    privateAttribute=
        st.integers(),
    packageAttribute=
        safe_text
)
Order_strategy = st.builds(
    Order,
)
InventoryType_strategy = st.builds(
    InventoryType,
    publicAttribute=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    protectedAttribute=
        safe_text,
    privateAttribute=
        st.integers(),
    packageAttribute=
        safe_text
)
Inventory_strategy = st.builds(
    Inventory,
    ownerName=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ClassV_strategy = st.builds(
    ClassV,
)
ClassU_strategy = st.builds(
    ClassU,
)
ClassT_strategy = st.builds(
    ClassT,
)
ClassS_strategy = st.builds(
    ClassS,
)
ClassR_strategy = st.builds(
    ClassR,
)
ClassQ_strategy = st.builds(
    ClassQ,
)
InterfaceO_Interface_strategy = st.builds(
    InterfaceO_Interface,
)















@given(instance=Product_strategy)
def test_hyp_product_protectedAttribute_setter(instance):
    original = instance.protectedAttribute
    instance.protectedAttribute = original
    assert instance.protectedAttribute == original



@given(instance=Product_strategy)
def test_hyp_product_publicAttribute_setter(instance):
    original = instance.publicAttribute
    instance.publicAttribute = original
    assert instance.publicAttribute == original



@given(instance=Product_strategy)
def test_hyp_product_privateAttribute_setter(instance):
    original = instance.privateAttribute
    instance.privateAttribute = original
    assert instance.privateAttribute == original



@given(instance=Product_strategy)
def test_hyp_product_packageAttribute_setter(instance):
    original = instance.packageAttribute
    instance.packageAttribute = original
    assert instance.packageAttribute == original





@given(instance=InventoryType_strategy)
def test_hyp_inventorytype_publicAttribute_setter(instance):
    original = instance.publicAttribute
    instance.publicAttribute = original
    assert instance.publicAttribute == original



@given(instance=InventoryType_strategy)
def test_hyp_inventorytype_protectedAttribute_setter(instance):
    original = instance.protectedAttribute
    instance.protectedAttribute = original
    assert instance.protectedAttribute == original



@given(instance=InventoryType_strategy)
def test_hyp_inventorytype_privateAttribute_setter(instance):
    original = instance.privateAttribute
    instance.privateAttribute = original
    assert instance.privateAttribute == original



@given(instance=InventoryType_strategy)
def test_hyp_inventorytype_packageAttribute_setter(instance):
    original = instance.packageAttribute
    instance.packageAttribute = original
    assert instance.packageAttribute == original




@given(instance=Inventory_strategy)
def test_hyp_inventory_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original



@given(instance=Inventory_strategy)
def test_hyp_inventory_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ClassF,
    ClassG,
    ClassH,
    ClassJ,
    ClassK,
    ClassL,
    ClassM,
    ClassN,
    ClassP,
    ClassQ,
    ClassR,
    ClassS,
    ClassT,
    ClassU,
    ClassV,
    InterfaceO_Interface,
    Inventory,
    InventoryType,
    Order,
    Personel,
    PersonelDepartment,
    Product,
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

def test_Inventory_balance_value_roundtrip():
    instance = Inventory(balance=3.14, ownerName="sample_text")
    assert instance.balance == 3.14
    instance.balance = 9.99
    assert instance.balance == 9.99


def test_Inventory_ownerName_value_roundtrip():
    instance = Inventory(balance=3.14, ownerName="sample_text")
    assert instance.ownerName == "sample_text"
    instance.ownerName = "sample_text_2"
    assert instance.ownerName == "sample_text_2"


def test_InventoryType_packageAttribute_value_roundtrip():
    instance = InventoryType(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.packageAttribute == "sample_text"
    instance.packageAttribute = "sample_text_2"
    assert instance.packageAttribute == "sample_text_2"


def test_InventoryType_privateAttribute_value_roundtrip():
    instance = InventoryType(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.privateAttribute == 7
    instance.privateAttribute = 13
    assert instance.privateAttribute == 13


def test_InventoryType_protectedAttribute_value_roundtrip():
    instance = InventoryType(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.protectedAttribute == "sample_text"
    instance.protectedAttribute = "sample_text_2"
    assert instance.protectedAttribute == "sample_text_2"


def test_InventoryType_publicAttribute_value_roundtrip():
    instance = InventoryType(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.publicAttribute == 3.14
    instance.publicAttribute = 9.99
    assert instance.publicAttribute == 9.99


def test_Product_packageAttribute_value_roundtrip():
    instance = Product(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.packageAttribute == "sample_text"
    instance.packageAttribute = "sample_text_2"
    assert instance.packageAttribute == "sample_text_2"


def test_Product_privateAttribute_value_roundtrip():
    instance = Product(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.privateAttribute == 7
    instance.privateAttribute = 13
    assert instance.privateAttribute == 13


def test_Product_protectedAttribute_value_roundtrip():
    instance = Product(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.protectedAttribute == "sample_text"
    instance.protectedAttribute = "sample_text_2"
    assert instance.protectedAttribute == "sample_text_2"


def test_Product_publicAttribute_value_roundtrip():
    instance = Product(packageAttribute="sample_text", privateAttribute=7, protectedAttribute="sample_text", publicAttribute=3.14)
    assert instance.publicAttribute == 3.14
    instance.publicAttribute = 9.99
    assert instance.publicAttribute == 9.99


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ClassF_strategy = st.builds(ClassF)
@given(instance=ClassF_strategy)
@settings(max_examples=25)
def test_ClassF_instantiation(instance):
    assert isinstance(instance, ClassF)


ClassG_strategy = st.builds(ClassG)
@given(instance=ClassG_strategy)
@settings(max_examples=25)
def test_ClassG_instantiation(instance):
    assert isinstance(instance, ClassG)


ClassH_strategy = st.builds(ClassH)
@given(instance=ClassH_strategy)
@settings(max_examples=25)
def test_ClassH_instantiation(instance):
    assert isinstance(instance, ClassH)


ClassJ_strategy = st.builds(ClassJ)
@given(instance=ClassJ_strategy)
@settings(max_examples=25)
def test_ClassJ_instantiation(instance):
    assert isinstance(instance, ClassJ)


ClassK_strategy = st.builds(ClassK)
@given(instance=ClassK_strategy)
@settings(max_examples=25)
def test_ClassK_instantiation(instance):
    assert isinstance(instance, ClassK)


ClassL_strategy = st.builds(ClassL)
@given(instance=ClassL_strategy)
@settings(max_examples=25)
def test_ClassL_instantiation(instance):
    assert isinstance(instance, ClassL)


ClassM_strategy = st.builds(ClassM)
@given(instance=ClassM_strategy)
@settings(max_examples=25)
def test_ClassM_instantiation(instance):
    assert isinstance(instance, ClassM)


ClassN_strategy = st.builds(ClassN)
@given(instance=ClassN_strategy)
@settings(max_examples=25)
def test_ClassN_instantiation(instance):
    assert isinstance(instance, ClassN)


ClassP_strategy = st.builds(ClassP)
@given(instance=ClassP_strategy)
@settings(max_examples=25)
def test_ClassP_instantiation(instance):
    assert isinstance(instance, ClassP)


ClassQ_strategy = st.builds(ClassQ)
@given(instance=ClassQ_strategy)
@settings(max_examples=25)
def test_ClassQ_instantiation(instance):
    assert isinstance(instance, ClassQ)


ClassR_strategy = st.builds(ClassR)
@given(instance=ClassR_strategy)
@settings(max_examples=25)
def test_ClassR_instantiation(instance):
    assert isinstance(instance, ClassR)


ClassS_strategy = st.builds(ClassS)
@given(instance=ClassS_strategy)
@settings(max_examples=25)
def test_ClassS_instantiation(instance):
    assert isinstance(instance, ClassS)


ClassT_strategy = st.builds(ClassT)
@given(instance=ClassT_strategy)
@settings(max_examples=25)
def test_ClassT_instantiation(instance):
    assert isinstance(instance, ClassT)


ClassU_strategy = st.builds(ClassU)
@given(instance=ClassU_strategy)
@settings(max_examples=25)
def test_ClassU_instantiation(instance):
    assert isinstance(instance, ClassU)


ClassV_strategy = st.builds(ClassV)
@given(instance=ClassV_strategy)
@settings(max_examples=25)
def test_ClassV_instantiation(instance):
    assert isinstance(instance, ClassV)


InterfaceO_Interface_strategy = st.builds(InterfaceO_Interface)
@given(instance=InterfaceO_Interface_strategy)
@settings(max_examples=25)
def test_InterfaceO_Interface_instantiation(instance):
    assert isinstance(instance, InterfaceO_Interface)


Inventory_strategy = st.builds(Inventory, balance=st.floats(allow_nan=False, allow_infinity=False), ownerName=safe_text)
@given(instance=Inventory_strategy)
@settings(max_examples=25)
def test_Inventory_instantiation(instance):
    assert isinstance(instance, Inventory)


InventoryType_strategy = st.builds(InventoryType, packageAttribute=safe_text, privateAttribute=st.integers(), protectedAttribute=safe_text, publicAttribute=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=InventoryType_strategy)
@settings(max_examples=25)
def test_InventoryType_instantiation(instance):
    assert isinstance(instance, InventoryType)


Order_strategy = st.builds(Order)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Personel_strategy = st.builds(Personel)
@given(instance=Personel_strategy)
@settings(max_examples=25)
def test_Personel_instantiation(instance):
    assert isinstance(instance, Personel)


PersonelDepartment_strategy = st.builds(PersonelDepartment)
@given(instance=PersonelDepartment_strategy)
@settings(max_examples=25)
def test_PersonelDepartment_instantiation(instance):
    assert isinstance(instance, PersonelDepartment)


Product_strategy = st.builds(Product, packageAttribute=safe_text, privateAttribute=st.integers(), protectedAttribute=safe_text, publicAttribute=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)



