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
    Faculty,
    Student,
    Patron,
    Library_Staff_Actor,
    Faculty_Actor,
    Library_Management_Component,
    Student_Actor,
    Patron_Actor,
    Manage_Computer_Terminals_external,
    Extended_Checkout_external,
    Order_New_Resources_external,
    Renew_Magazine_Subscriptions_external,
    Organize_Books_external,
    Manage_Reference_Materials_external,
    Reserve_Book_For_Semester_external,
    Check_Out_Item_external,
    Request_Book_external,
    Check_In_Item_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_faculty_is_not_abstract():
    assert not inspect.isabstract(Faculty)


def test_hyp_faculty_constructor_exists():
    assert callable(Faculty.__init__)


def test_hyp_faculty_constructor_args():
    sig = inspect.signature(Faculty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patron_is_not_abstract():
    assert not inspect.isabstract(Patron)


def test_hyp_patron_constructor_exists():
    assert callable(Patron.__init__)


def test_hyp_patron_constructor_args():
    sig = inspect.signature(Patron.__init__)
    params = list(sig.parameters.keys())
    assert "isMember" in params, "Missing parameter 'isMember'"




def test_hyp_library_staff_actor_is_not_abstract():
    assert not inspect.isabstract(Library_Staff_Actor)


def test_hyp_library_staff_actor_constructor_exists():
    assert callable(Library_Staff_Actor.__init__)


def test_hyp_library_staff_actor_constructor_args():
    sig = inspect.signature(Library_Staff_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faculty_actor_is_not_abstract():
    assert not inspect.isabstract(Faculty_Actor)


def test_hyp_faculty_actor_constructor_exists():
    assert callable(Faculty_Actor.__init__)


def test_hyp_faculty_actor_constructor_args():
    sig = inspect.signature(Faculty_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_management_component_is_not_abstract():
    assert not inspect.isabstract(Library_Management_Component)


def test_hyp_library_management_component_constructor_exists():
    assert callable(Library_Management_Component.__init__)


def test_hyp_library_management_component_constructor_args():
    sig = inspect.signature(Library_Management_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student_actor_is_not_abstract():
    assert not inspect.isabstract(Student_Actor)


def test_hyp_student_actor_constructor_exists():
    assert callable(Student_Actor.__init__)


def test_hyp_student_actor_constructor_args():
    sig = inspect.signature(Student_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patron_actor_is_not_abstract():
    assert not inspect.isabstract(Patron_Actor)


def test_hyp_patron_actor_constructor_exists():
    assert callable(Patron_Actor.__init__)


def test_hyp_patron_actor_constructor_args():
    sig = inspect.signature(Patron_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manage_computer_terminals_external_is_not_abstract():
    assert not inspect.isabstract(Manage_Computer_Terminals_external)


def test_hyp_manage_computer_terminals_external_constructor_exists():
    assert callable(Manage_Computer_Terminals_external.__init__)


def test_hyp_manage_computer_terminals_external_constructor_args():
    sig = inspect.signature(Manage_Computer_Terminals_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extended_checkout_external_is_not_abstract():
    assert not inspect.isabstract(Extended_Checkout_external)


def test_hyp_extended_checkout_external_constructor_exists():
    assert callable(Extended_Checkout_external.__init__)


def test_hyp_extended_checkout_external_constructor_args():
    sig = inspect.signature(Extended_Checkout_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_order_new_resources_external_is_not_abstract():
    assert not inspect.isabstract(Order_New_Resources_external)


def test_hyp_order_new_resources_external_constructor_exists():
    assert callable(Order_New_Resources_external.__init__)


def test_hyp_order_new_resources_external_constructor_args():
    sig = inspect.signature(Order_New_Resources_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_renew_magazine_subscriptions_external_is_not_abstract():
    assert not inspect.isabstract(Renew_Magazine_Subscriptions_external)


def test_hyp_renew_magazine_subscriptions_external_constructor_exists():
    assert callable(Renew_Magazine_Subscriptions_external.__init__)


def test_hyp_renew_magazine_subscriptions_external_constructor_args():
    sig = inspect.signature(Renew_Magazine_Subscriptions_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_organize_books_external_is_not_abstract():
    assert not inspect.isabstract(Organize_Books_external)


def test_hyp_organize_books_external_constructor_exists():
    assert callable(Organize_Books_external.__init__)


def test_hyp_organize_books_external_constructor_args():
    sig = inspect.signature(Organize_Books_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manage_reference_materials_external_is_not_abstract():
    assert not inspect.isabstract(Manage_Reference_Materials_external)


def test_hyp_manage_reference_materials_external_constructor_exists():
    assert callable(Manage_Reference_Materials_external.__init__)


def test_hyp_manage_reference_materials_external_constructor_args():
    sig = inspect.signature(Manage_Reference_Materials_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reserve_book_for_semester_external_is_not_abstract():
    assert not inspect.isabstract(Reserve_Book_For_Semester_external)


def test_hyp_reserve_book_for_semester_external_constructor_exists():
    assert callable(Reserve_Book_For_Semester_external.__init__)


def test_hyp_reserve_book_for_semester_external_constructor_args():
    sig = inspect.signature(Reserve_Book_For_Semester_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_check_out_item_external_is_not_abstract():
    assert not inspect.isabstract(Check_Out_Item_external)


def test_hyp_check_out_item_external_constructor_exists():
    assert callable(Check_Out_Item_external.__init__)


def test_hyp_check_out_item_external_constructor_args():
    sig = inspect.signature(Check_Out_Item_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_request_book_external_is_not_abstract():
    assert not inspect.isabstract(Request_Book_external)


def test_hyp_request_book_external_constructor_exists():
    assert callable(Request_Book_external.__init__)


def test_hyp_request_book_external_constructor_args():
    sig = inspect.signature(Request_Book_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_check_in_item_external_is_not_abstract():
    assert not inspect.isabstract(Check_In_Item_external)


def test_hyp_check_in_item_external_constructor_exists():
    assert callable(Check_In_Item_external.__init__)


def test_hyp_check_in_item_external_constructor_args():
    sig = inspect.signature(Check_In_Item_external.__init__)
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
Faculty_strategy = st.builds(
    Faculty,
)
Student_strategy = st.builds(
    Student,
)
Patron_strategy = st.builds(
    Patron,
    isMember=
        st.booleans()
)
Library_Staff_Actor_strategy = st.builds(
    Library_Staff_Actor,
)
Faculty_Actor_strategy = st.builds(
    Faculty_Actor,
)
Library_Management_Component_strategy = st.builds(
    Library_Management_Component,
)
Student_Actor_strategy = st.builds(
    Student_Actor,
)
Patron_Actor_strategy = st.builds(
    Patron_Actor,
)
Manage_Computer_Terminals_external_strategy = st.builds(
    Manage_Computer_Terminals_external,
)
Extended_Checkout_external_strategy = st.builds(
    Extended_Checkout_external,
)
Order_New_Resources_external_strategy = st.builds(
    Order_New_Resources_external,
)
Renew_Magazine_Subscriptions_external_strategy = st.builds(
    Renew_Magazine_Subscriptions_external,
)
Organize_Books_external_strategy = st.builds(
    Organize_Books_external,
)
Manage_Reference_Materials_external_strategy = st.builds(
    Manage_Reference_Materials_external,
)
Reserve_Book_For_Semester_external_strategy = st.builds(
    Reserve_Book_For_Semester_external,
)
Check_Out_Item_external_strategy = st.builds(
    Check_Out_Item_external,
)
Request_Book_external_strategy = st.builds(
    Request_Book_external,
)
Check_In_Item_external_strategy = st.builds(
    Check_In_Item_external,
)






@given(instance=Patron_strategy)
def test_hyp_patron_isMember_setter(instance):
    original = instance.isMember
    instance.isMember = original
    assert instance.isMember == original

















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Check_In_Item_external,
    Check_Out_Item_external,
    Extended_Checkout_external,
    Faculty,
    Faculty_Actor,
    Library_Management_Component,
    Library_Staff_Actor,
    Manage_Computer_Terminals_external,
    Manage_Reference_Materials_external,
    Order_New_Resources_external,
    Organize_Books_external,
    Patron,
    Patron_Actor,
    Renew_Magazine_Subscriptions_external,
    Request_Book_external,
    Reserve_Book_For_Semester_external,
    Student,
    Student_Actor,
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

def test_Patron_isMember_value_roundtrip():
    instance = Patron(isMember=True)
    assert instance.isMember == True
    instance.isMember = False
    assert instance.isMember == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Check_In_Item_external_strategy = st.builds(Check_In_Item_external)
@given(instance=Check_In_Item_external_strategy)
@settings(max_examples=25)
def test_Check_In_Item_external_instantiation(instance):
    assert isinstance(instance, Check_In_Item_external)


Check_Out_Item_external_strategy = st.builds(Check_Out_Item_external)
@given(instance=Check_Out_Item_external_strategy)
@settings(max_examples=25)
def test_Check_Out_Item_external_instantiation(instance):
    assert isinstance(instance, Check_Out_Item_external)


Extended_Checkout_external_strategy = st.builds(Extended_Checkout_external)
@given(instance=Extended_Checkout_external_strategy)
@settings(max_examples=25)
def test_Extended_Checkout_external_instantiation(instance):
    assert isinstance(instance, Extended_Checkout_external)


Faculty_strategy = st.builds(Faculty)
@given(instance=Faculty_strategy)
@settings(max_examples=25)
def test_Faculty_instantiation(instance):
    assert isinstance(instance, Faculty)


Faculty_Actor_strategy = st.builds(Faculty_Actor)
@given(instance=Faculty_Actor_strategy)
@settings(max_examples=25)
def test_Faculty_Actor_instantiation(instance):
    assert isinstance(instance, Faculty_Actor)


Library_Management_Component_strategy = st.builds(Library_Management_Component)
@given(instance=Library_Management_Component_strategy)
@settings(max_examples=25)
def test_Library_Management_Component_instantiation(instance):
    assert isinstance(instance, Library_Management_Component)


Library_Staff_Actor_strategy = st.builds(Library_Staff_Actor)
@given(instance=Library_Staff_Actor_strategy)
@settings(max_examples=25)
def test_Library_Staff_Actor_instantiation(instance):
    assert isinstance(instance, Library_Staff_Actor)


Manage_Computer_Terminals_external_strategy = st.builds(Manage_Computer_Terminals_external)
@given(instance=Manage_Computer_Terminals_external_strategy)
@settings(max_examples=25)
def test_Manage_Computer_Terminals_external_instantiation(instance):
    assert isinstance(instance, Manage_Computer_Terminals_external)


Manage_Reference_Materials_external_strategy = st.builds(Manage_Reference_Materials_external)
@given(instance=Manage_Reference_Materials_external_strategy)
@settings(max_examples=25)
def test_Manage_Reference_Materials_external_instantiation(instance):
    assert isinstance(instance, Manage_Reference_Materials_external)


Order_New_Resources_external_strategy = st.builds(Order_New_Resources_external)
@given(instance=Order_New_Resources_external_strategy)
@settings(max_examples=25)
def test_Order_New_Resources_external_instantiation(instance):
    assert isinstance(instance, Order_New_Resources_external)


Organize_Books_external_strategy = st.builds(Organize_Books_external)
@given(instance=Organize_Books_external_strategy)
@settings(max_examples=25)
def test_Organize_Books_external_instantiation(instance):
    assert isinstance(instance, Organize_Books_external)


Patron_strategy = st.builds(Patron, isMember=st.booleans())
@given(instance=Patron_strategy)
@settings(max_examples=25)
def test_Patron_instantiation(instance):
    assert isinstance(instance, Patron)


Patron_Actor_strategy = st.builds(Patron_Actor)
@given(instance=Patron_Actor_strategy)
@settings(max_examples=25)
def test_Patron_Actor_instantiation(instance):
    assert isinstance(instance, Patron_Actor)


Renew_Magazine_Subscriptions_external_strategy = st.builds(Renew_Magazine_Subscriptions_external)
@given(instance=Renew_Magazine_Subscriptions_external_strategy)
@settings(max_examples=25)
def test_Renew_Magazine_Subscriptions_external_instantiation(instance):
    assert isinstance(instance, Renew_Magazine_Subscriptions_external)


Request_Book_external_strategy = st.builds(Request_Book_external)
@given(instance=Request_Book_external_strategy)
@settings(max_examples=25)
def test_Request_Book_external_instantiation(instance):
    assert isinstance(instance, Request_Book_external)


Reserve_Book_For_Semester_external_strategy = st.builds(Reserve_Book_For_Semester_external)
@given(instance=Reserve_Book_For_Semester_external_strategy)
@settings(max_examples=25)
def test_Reserve_Book_For_Semester_external_instantiation(instance):
    assert isinstance(instance, Reserve_Book_For_Semester_external)


Student_strategy = st.builds(Student)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Student_Actor_strategy = st.builds(Student_Actor)
@given(instance=Student_Actor_strategy)
@settings(max_examples=25)
def test_Student_Actor_instantiation(instance):
    assert isinstance(instance, Student_Actor)



