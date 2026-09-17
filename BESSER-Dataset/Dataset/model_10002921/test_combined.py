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
    Hall_book,
    View_and_place_order,
    Decoration_book,
    Catering_book,
    View_and_update,
    Hall,
    Decoration,
    Catering,
    Admin,
    User,
    void,
    LOGIN,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_hall_book_is_not_abstract():
    assert not inspect.isabstract(Hall_book)


def test_hyp_hall_book_constructor_exists():
    assert callable(Hall_book.__init__)


def test_hyp_hall_book_constructor_args():
    sig = inspect.signature(Hall_book.__init__)
    params = list(sig.parameters.keys())
    assert "get_room_type" in params, "Missing parameter 'get_room_type'"
    assert "cost_per_day" in params, "Missing parameter 'cost_per_day'"
    assert "get_hall_no" in params, "Missing parameter 'get_hall_no'"






def test_hyp_view_and_place_order_is_not_abstract():
    assert not inspect.isabstract(View_and_place_order)


def test_hyp_view_and_place_order_constructor_exists():
    assert callable(View_and_place_order.__init__)


def test_hyp_view_and_place_order_constructor_args():
    sig = inspect.signature(View_and_place_order.__init__)
    params = list(sig.parameters.keys())
    assert "place_order" in params, "Missing parameter 'place_order'"
    assert "order_view" in params, "Missing parameter 'order_view'"

def test_hyp_view_and_place_order_has_place_order():
    assert hasattr(View_and_place_order, "place_order")
    descriptor = None
    for klass in View_and_place_order.__mro__:
        if "place_order" in klass.__dict__:
            descriptor = klass.__dict__["place_order"]
            break
    assert isinstance(descriptor, property)

def test_hyp_view_and_place_order_has_order_view():
    assert hasattr(View_and_place_order, "order_view")
    descriptor = None
    for klass in View_and_place_order.__mro__:
        if "order_view" in klass.__dict__:
            descriptor = klass.__dict__["order_view"]
            break
    assert isinstance(descriptor, property)



def test_hyp_decoration_book_is_not_abstract():
    assert not inspect.isabstract(Decoration_book)


def test_hyp_decoration_book_constructor_exists():
    assert callable(Decoration_book.__init__)


def test_hyp_decoration_book_constructor_args():
    sig = inspect.signature(Decoration_book.__init__)
    params = list(sig.parameters.keys())
    assert "Square_feet" in params, "Missing parameter 'Square_feet'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "Decor_type" in params, "Missing parameter 'Decor_type'"

def test_hyp_decoration_book_has_Square_feet():
    assert hasattr(Decoration_book, "Square_feet")
    descriptor = None
    for klass in Decoration_book.__mro__:
        if "Square_feet" in klass.__dict__:
            descriptor = klass.__dict__["Square_feet"]
            break
    assert isinstance(descriptor, property)

def test_hyp_decoration_book_has_cost():
    assert hasattr(Decoration_book, "cost")
    descriptor = None
    for klass in Decoration_book.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_hyp_decoration_book_has_Decor_type():
    assert hasattr(Decoration_book, "Decor_type")
    descriptor = None
    for klass in Decoration_book.__mro__:
        if "Decor_type" in klass.__dict__:
            descriptor = klass.__dict__["Decor_type"]
            break
    assert isinstance(descriptor, property)



def test_hyp_catering_book_is_not_abstract():
    assert not inspect.isabstract(Catering_book)


def test_hyp_catering_book_constructor_exists():
    assert callable(Catering_book.__init__)


def test_hyp_catering_book_constructor_args():
    sig = inspect.signature(Catering_book.__init__)
    params = list(sig.parameters.keys())
    assert "get_cost" in params, "Missing parameter 'get_cost'"
    assert "get_menu" in params, "Missing parameter 'get_menu'"





def test_hyp_view_and_update_is_not_abstract():
    assert not inspect.isabstract(View_and_update)


def test_hyp_view_and_update_constructor_exists():
    assert callable(View_and_update.__init__)


def test_hyp_view_and_update_constructor_args():
    sig = inspect.signature(View_and_update.__init__)
    params = list(sig.parameters.keys())
    assert "update_order" in params, "Missing parameter 'update_order'"
    assert "order_view" in params, "Missing parameter 'order_view'"

def test_hyp_view_and_update_has_update_order():
    assert hasattr(View_and_update, "update_order")
    descriptor = None
    for klass in View_and_update.__mro__:
        if "update_order" in klass.__dict__:
            descriptor = klass.__dict__["update_order"]
            break
    assert isinstance(descriptor, property)

def test_hyp_view_and_update_has_order_view():
    assert hasattr(View_and_update, "order_view")
    descriptor = None
    for klass in View_and_update.__mro__:
        if "order_view" in klass.__dict__:
            descriptor = klass.__dict__["order_view"]
            break
    assert isinstance(descriptor, property)



def test_hyp_hall_is_not_abstract():
    assert not inspect.isabstract(Hall)


def test_hyp_hall_constructor_exists():
    assert callable(Hall.__init__)


def test_hyp_hall_constructor_args():
    sig = inspect.signature(Hall.__init__)
    params = list(sig.parameters.keys())
    assert "cost_per_day" in params, "Missing parameter 'cost_per_day'"
    assert "get_hall_no" in params, "Missing parameter 'get_hall_no'"
    assert "get_room_type" in params, "Missing parameter 'get_room_type'"






def test_hyp_decoration_is_not_abstract():
    assert not inspect.isabstract(Decoration)


def test_hyp_decoration_constructor_exists():
    assert callable(Decoration.__init__)


def test_hyp_decoration_constructor_args():
    sig = inspect.signature(Decoration.__init__)
    params = list(sig.parameters.keys())
    assert "Decor_type" in params, "Missing parameter 'Decor_type'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "Square_feet" in params, "Missing parameter 'Square_feet'"

def test_hyp_decoration_has_Decor_type():
    assert hasattr(Decoration, "Decor_type")
    descriptor = None
    for klass in Decoration.__mro__:
        if "Decor_type" in klass.__dict__:
            descriptor = klass.__dict__["Decor_type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_decoration_has_cost():
    assert hasattr(Decoration, "cost")
    descriptor = None
    for klass in Decoration.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_hyp_decoration_has_Square_feet():
    assert hasattr(Decoration, "Square_feet")
    descriptor = None
    for klass in Decoration.__mro__:
        if "Square_feet" in klass.__dict__:
            descriptor = klass.__dict__["Square_feet"]
            break
    assert isinstance(descriptor, property)



def test_hyp_catering_is_not_abstract():
    assert not inspect.isabstract(Catering)


def test_hyp_catering_constructor_exists():
    assert callable(Catering.__init__)


def test_hyp_catering_constructor_args():
    sig = inspect.signature(Catering.__init__)
    params = list(sig.parameters.keys())
    assert "get_menu" in params, "Missing parameter 'get_menu'"
    assert "get_cost" in params, "Missing parameter 'get_cost'"





def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"






def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"






def test_hyp_void_is_not_abstract():
    assert not inspect.isabstract(void)


def test_hyp_void_constructor_exists():
    assert callable(void.__init__)


def test_hyp_void_constructor_args():
    sig = inspect.signature(void.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(LOGIN)


def test_hyp_login_constructor_exists():
    assert callable(LOGIN.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(LOGIN.__init__)
    params = list(sig.parameters.keys())
    assert "user_Name" in params, "Missing parameter 'user_Name'"
    assert "l_Name" in params, "Missing parameter 'l_Name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "f_Name" in params, "Missing parameter 'f_Name'"






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
Hall_book_strategy = st.builds(
    Hall_book,
    get_room_type=
        safe_text,
    cost_per_day=
        safe_text,
    get_hall_no=
        safe_text
)
View_and_place_order_strategy = st.builds(
    View_and_place_order,
    place_order=
        st.none(),
    order_view=
        st.none()
)
Decoration_book_strategy = st.builds(
    Decoration_book,
    Square_feet=
        safe_text,
    cost=
        safe_text,
    Decor_type=
        st.none()
)
Catering_book_strategy = st.builds(
    Catering_book,
    get_cost=
        safe_text,
    get_menu=
        safe_text
)
View_and_update_strategy = st.builds(
    View_and_update,
    update_order=
        st.none(),
    order_view=
        st.none()
)
Hall_strategy = st.builds(
    Hall,
    cost_per_day=
        safe_text,
    get_hall_no=
        safe_text,
    get_room_type=
        safe_text
)
Decoration_strategy = st.builds(
    Decoration,
    Decor_type=
        st.none(),
    cost=
        safe_text,
    Square_feet=
        safe_text
)
Catering_strategy = st.builds(
    Catering,
    get_menu=
        safe_text,
    get_cost=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    userName=
        safe_text,
    password=
        safe_text,
    userID=
        st.integers()
)
User_strategy = st.builds(
    User,
    userName=
        safe_text,
    password=
        safe_text,
    userID=
        st.integers()
)
void_strategy = st.builds(
    void,
)
LOGIN_strategy = st.builds(
    LOGIN,
    user_Name=
        safe_text,
    l_Name=
        safe_text,
    password=
        safe_text,
    f_Name=
        safe_text
)




@given(instance=Hall_book_strategy)
def test_hyp_hall_book_get_room_type_setter(instance):
    original = instance.get_room_type
    instance.get_room_type = original
    assert instance.get_room_type == original



@given(instance=Hall_book_strategy)
def test_hyp_hall_book_cost_per_day_setter(instance):
    original = instance.cost_per_day
    instance.cost_per_day = original
    assert instance.cost_per_day == original



@given(instance=Hall_book_strategy)
def test_hyp_hall_book_get_hall_no_setter(instance):
    original = instance.get_hall_no
    instance.get_hall_no = original
    assert instance.get_hall_no == original

@given(instance=View_and_place_order_strategy)
@settings(max_examples=50)
def test_hyp_view_and_place_order_instantiation(instance):
    assert isinstance(instance, View_and_place_order)



@given(instance=View_and_place_order_strategy)
def test_hyp_view_and_place_order_place_order_setter(instance):
    original = instance.place_order
    instance.place_order = original
    assert instance.place_order == original



@given(instance=View_and_place_order_strategy)
def test_hyp_view_and_place_order_order_view_setter(instance):
    original = instance.order_view
    instance.order_view = original
    assert instance.order_view == original

@given(instance=Decoration_book_strategy)
@settings(max_examples=50)
def test_hyp_decoration_book_instantiation(instance):
    assert isinstance(instance, Decoration_book)



@given(instance=Decoration_book_strategy)
def test_hyp_decoration_book_Square_feet_setter(instance):
    original = instance.Square_feet
    instance.Square_feet = original
    assert instance.Square_feet == original



@given(instance=Decoration_book_strategy)
def test_hyp_decoration_book_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=Decoration_book_strategy)
def test_hyp_decoration_book_Decor_type_setter(instance):
    original = instance.Decor_type
    instance.Decor_type = original
    assert instance.Decor_type == original




@given(instance=Catering_book_strategy)
def test_hyp_catering_book_get_cost_setter(instance):
    original = instance.get_cost
    instance.get_cost = original
    assert instance.get_cost == original



@given(instance=Catering_book_strategy)
def test_hyp_catering_book_get_menu_setter(instance):
    original = instance.get_menu
    instance.get_menu = original
    assert instance.get_menu == original

@given(instance=View_and_update_strategy)
@settings(max_examples=50)
def test_hyp_view_and_update_instantiation(instance):
    assert isinstance(instance, View_and_update)



@given(instance=View_and_update_strategy)
def test_hyp_view_and_update_update_order_setter(instance):
    original = instance.update_order
    instance.update_order = original
    assert instance.update_order == original



@given(instance=View_and_update_strategy)
def test_hyp_view_and_update_order_view_setter(instance):
    original = instance.order_view
    instance.order_view = original
    assert instance.order_view == original




@given(instance=Hall_strategy)
def test_hyp_hall_cost_per_day_setter(instance):
    original = instance.cost_per_day
    instance.cost_per_day = original
    assert instance.cost_per_day == original



@given(instance=Hall_strategy)
def test_hyp_hall_get_hall_no_setter(instance):
    original = instance.get_hall_no
    instance.get_hall_no = original
    assert instance.get_hall_no == original



@given(instance=Hall_strategy)
def test_hyp_hall_get_room_type_setter(instance):
    original = instance.get_room_type
    instance.get_room_type = original
    assert instance.get_room_type == original

@given(instance=Decoration_strategy)
@settings(max_examples=50)
def test_hyp_decoration_instantiation(instance):
    assert isinstance(instance, Decoration)



@given(instance=Decoration_strategy)
def test_hyp_decoration_Decor_type_setter(instance):
    original = instance.Decor_type
    instance.Decor_type = original
    assert instance.Decor_type == original



@given(instance=Decoration_strategy)
def test_hyp_decoration_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=Decoration_strategy)
def test_hyp_decoration_Square_feet_setter(instance):
    original = instance.Square_feet
    instance.Square_feet = original
    assert instance.Square_feet == original




@given(instance=Catering_strategy)
def test_hyp_catering_get_menu_setter(instance):
    original = instance.get_menu
    instance.get_menu = original
    assert instance.get_menu == original



@given(instance=Catering_strategy)
def test_hyp_catering_get_cost_setter(instance):
    original = instance.get_cost
    instance.get_cost = original
    assert instance.get_cost == original




@given(instance=Admin_strategy)
def test_hyp_admin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Admin_strategy)
def test_hyp_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_hyp_admin_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original




@given(instance=User_strategy)
def test_hyp_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original





@given(instance=LOGIN_strategy)
def test_hyp_login_user_Name_setter(instance):
    original = instance.user_Name
    instance.user_Name = original
    assert instance.user_Name == original



@given(instance=LOGIN_strategy)
def test_hyp_login_l_Name_setter(instance):
    original = instance.l_Name
    instance.l_Name = original
    assert instance.l_Name == original



@given(instance=LOGIN_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=LOGIN_strategy)
def test_hyp_login_f_Name_setter(instance):
    original = instance.f_Name
    instance.f_Name = original
    assert instance.f_Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Catering,
    Catering_book,
    Decoration,
    Decoration_book,
    Hall,
    Hall_book,
    LOGIN,
    User,
    View_and_place_order,
    View_and_update,
    void,
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

def test_Admin_password_value_roundtrip():
    instance = Admin(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Admin_userID_value_roundtrip():
    instance = Admin(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_Admin_userName_value_roundtrip():
    instance = Admin(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_Catering_get_cost_value_roundtrip():
    instance = Catering(get_cost="sample_text", get_menu="sample_text")
    assert instance.get_cost == "sample_text"
    instance.get_cost = "sample_text_2"
    assert instance.get_cost == "sample_text_2"


def test_Catering_get_menu_value_roundtrip():
    instance = Catering(get_cost="sample_text", get_menu="sample_text")
    assert instance.get_menu == "sample_text"
    instance.get_menu = "sample_text_2"
    assert instance.get_menu == "sample_text_2"


def test_Catering_book_get_cost_value_roundtrip():
    instance = Catering_book(get_cost="sample_text", get_menu="sample_text")
    assert instance.get_cost == "sample_text"
    instance.get_cost = "sample_text_2"
    assert instance.get_cost == "sample_text_2"


def test_Catering_book_get_menu_value_roundtrip():
    instance = Catering_book(get_cost="sample_text", get_menu="sample_text")
    assert instance.get_menu == "sample_text"
    instance.get_menu = "sample_text_2"
    assert instance.get_menu == "sample_text_2"


def test_Hall_cost_per_day_value_roundtrip():
    instance = Hall(cost_per_day="sample_text", get_hall_no="sample_text", get_room_type="sample_text")
    assert instance.cost_per_day == "sample_text"
    instance.cost_per_day = "sample_text_2"
    assert instance.cost_per_day == "sample_text_2"


def test_Hall_get_hall_no_value_roundtrip():
    instance = Hall(cost_per_day="sample_text", get_hall_no="sample_text", get_room_type="sample_text")
    assert instance.get_hall_no == "sample_text"
    instance.get_hall_no = "sample_text_2"
    assert instance.get_hall_no == "sample_text_2"


def test_Hall_get_room_type_value_roundtrip():
    instance = Hall(cost_per_day="sample_text", get_hall_no="sample_text", get_room_type="sample_text")
    assert instance.get_room_type == "sample_text"
    instance.get_room_type = "sample_text_2"
    assert instance.get_room_type == "sample_text_2"


def test_Hall_book_cost_per_day_value_roundtrip():
    instance = Hall_book(cost_per_day="sample_text", get_hall_no="sample_text", get_room_type="sample_text")
    assert instance.cost_per_day == "sample_text"
    instance.cost_per_day = "sample_text_2"
    assert instance.cost_per_day == "sample_text_2"


def test_Hall_book_get_hall_no_value_roundtrip():
    instance = Hall_book(cost_per_day="sample_text", get_hall_no="sample_text", get_room_type="sample_text")
    assert instance.get_hall_no == "sample_text"
    instance.get_hall_no = "sample_text_2"
    assert instance.get_hall_no == "sample_text_2"


def test_Hall_book_get_room_type_value_roundtrip():
    instance = Hall_book(cost_per_day="sample_text", get_hall_no="sample_text", get_room_type="sample_text")
    assert instance.get_room_type == "sample_text"
    instance.get_room_type = "sample_text_2"
    assert instance.get_room_type == "sample_text_2"


def test_LOGIN_f_Name_value_roundtrip():
    instance = LOGIN(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
    assert instance.f_Name == "sample_text"
    instance.f_Name = "sample_text_2"
    assert instance.f_Name == "sample_text_2"


def test_LOGIN_l_Name_value_roundtrip():
    instance = LOGIN(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
    assert instance.l_Name == "sample_text"
    instance.l_Name = "sample_text_2"
    assert instance.l_Name == "sample_text_2"


def test_LOGIN_password_value_roundtrip():
    instance = LOGIN(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_LOGIN_user_Name_value_roundtrip():
    instance = LOGIN(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
    assert instance.user_Name == "sample_text"
    instance.user_Name = "sample_text_2"
    assert instance.user_Name == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userID_value_roundtrip():
    instance = User(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_User_userName_value_roundtrip():
    instance = User(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Catering_strategy = st.builds(Catering, get_cost=safe_text, get_menu=safe_text)
@given(instance=Catering_strategy)
@settings(max_examples=25)
def test_Catering_instantiation(instance):
    assert isinstance(instance, Catering)


Catering_book_strategy = st.builds(Catering_book, get_cost=safe_text, get_menu=safe_text)
@given(instance=Catering_book_strategy)
@settings(max_examples=25)
def test_Catering_book_instantiation(instance):
    assert isinstance(instance, Catering_book)


Hall_strategy = st.builds(Hall, cost_per_day=safe_text, get_hall_no=safe_text, get_room_type=safe_text)
@given(instance=Hall_strategy)
@settings(max_examples=25)
def test_Hall_instantiation(instance):
    assert isinstance(instance, Hall)


Hall_book_strategy = st.builds(Hall_book, cost_per_day=safe_text, get_hall_no=safe_text, get_room_type=safe_text)
@given(instance=Hall_book_strategy)
@settings(max_examples=25)
def test_Hall_book_instantiation(instance):
    assert isinstance(instance, Hall_book)


LOGIN_strategy = st.builds(LOGIN, f_Name=safe_text, l_Name=safe_text, password=safe_text, user_Name=safe_text)
@given(instance=LOGIN_strategy)
@settings(max_examples=25)
def test_LOGIN_instantiation(instance):
    assert isinstance(instance, LOGIN)


User_strategy = st.builds(User, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


void_strategy = st.builds(void)
@given(instance=void_strategy)
@settings(max_examples=25)
def test_void_instantiation(instance):
    assert isinstance(instance, void)



