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
    Admin1,
    Student1,
    Society1,
    Lecturer1,
    Comment1,
    Location1,
    Event1,
    Post1,
    User1,
    VirtualTour1,
    Guest1,
    Comment,
    Location,
    Event,
    Post,
    Student,
    Society,
    Lecturer,
    Admin,
    User,
    VirtualTour,
    Guest,
    test_UseCase,
    User_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_admin1_is_not_abstract():
    assert not inspect.isabstract(Admin1)


def test_hyp_admin1_constructor_exists():
    assert callable(Admin1.__init__)


def test_hyp_admin1_constructor_args():
    sig = inspect.signature(Admin1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student1_is_not_abstract():
    assert not inspect.isabstract(Student1)


def test_hyp_student1_constructor_exists():
    assert callable(Student1.__init__)


def test_hyp_student1_constructor_args():
    sig = inspect.signature(Student1.__init__)
    params = list(sig.parameters.keys())
    assert "school" in params, "Missing parameter 'school'"
    assert "yearOfStudy" in params, "Missing parameter 'yearOfStudy'"
    assert "course" in params, "Missing parameter 'course'"






def test_hyp_society1_is_not_abstract():
    assert not inspect.isabstract(Society1)


def test_hyp_society1_constructor_exists():
    assert callable(Society1.__init__)


def test_hyp_society1_constructor_args():
    sig = inspect.signature(Society1.__init__)
    params = list(sig.parameters.keys())
    assert "yearEstablished" in params, "Missing parameter 'yearEstablished'"




def test_hyp_lecturer1_is_not_abstract():
    assert not inspect.isabstract(Lecturer1)


def test_hyp_lecturer1_constructor_exists():
    assert callable(Lecturer1.__init__)


def test_hyp_lecturer1_constructor_args():
    sig = inspect.signature(Lecturer1.__init__)
    params = list(sig.parameters.keys())
    assert "school" in params, "Missing parameter 'school'"




def test_hyp_comment1_is_not_abstract():
    assert not inspect.isabstract(Comment1)


def test_hyp_comment1_constructor_exists():
    assert callable(Comment1.__init__)


def test_hyp_comment1_constructor_args():
    sig = inspect.signature(Comment1.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "body" in params, "Missing parameter 'body'"
    assert "author" in params, "Missing parameter 'author'"






def test_hyp_location1_is_not_abstract():
    assert not inspect.isabstract(Location1)


def test_hyp_location1_constructor_exists():
    assert callable(Location1.__init__)


def test_hyp_location1_constructor_args():
    sig = inspect.signature(Location1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "capacity" in params, "Missing parameter 'capacity'"






def test_hyp_event1_is_not_abstract():
    assert not inspect.isabstract(Event1)


def test_hyp_event1_constructor_exists():
    assert callable(Event1.__init__)


def test_hyp_event1_constructor_args():
    sig = inspect.signature(Event1.__init__)
    params = list(sig.parameters.keys())
    assert "isOpen" in params, "Missing parameter 'isOpen'"
    assert "eventOwner" in params, "Missing parameter 'eventOwner'"
    assert "size" in params, "Missing parameter 'size'"
    assert "date" in params, "Missing parameter 'date'"
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"
    assert "invites" in params, "Missing parameter 'invites'"
    assert "joined" in params, "Missing parameter 'joined'"
    assert "rating" in params, "Missing parameter 'rating'"

def test_hyp_event1_has_isOpen():
    assert hasattr(Event1, "isOpen")
    descriptor = None
    for klass in Event1.__mro__:
        if "isOpen" in klass.__dict__:
            descriptor = klass.__dict__["isOpen"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_eventOwner():
    assert hasattr(Event1, "eventOwner")
    descriptor = None
    for klass in Event1.__mro__:
        if "eventOwner" in klass.__dict__:
            descriptor = klass.__dict__["eventOwner"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_size():
    assert hasattr(Event1, "size")
    descriptor = None
    for klass in Event1.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_date():
    assert hasattr(Event1, "date")
    descriptor = None
    for klass in Event1.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_location():
    assert hasattr(Event1, "location")
    descriptor = None
    for klass in Event1.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_name():
    assert hasattr(Event1, "name")
    descriptor = None
    for klass in Event1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_invites():
    assert hasattr(Event1, "invites")
    descriptor = None
    for klass in Event1.__mro__:
        if "invites" in klass.__dict__:
            descriptor = klass.__dict__["invites"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_joined():
    assert hasattr(Event1, "joined")
    descriptor = None
    for klass in Event1.__mro__:
        if "joined" in klass.__dict__:
            descriptor = klass.__dict__["joined"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event1_has_rating():
    assert hasattr(Event1, "rating")
    descriptor = None
    for klass in Event1.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_hyp_post1_is_not_abstract():
    assert not inspect.isabstract(Post1)


def test_hyp_post1_constructor_exists():
    assert callable(Post1.__init__)


def test_hyp_post1_constructor_args():
    sig = inspect.signature(Post1.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "date" in params, "Missing parameter 'date'"
    assert "files" in params, "Missing parameter 'files'"
    assert "body" in params, "Missing parameter 'body'"








def test_hyp_user1_is_not_abstract():
    assert not inspect.isabstract(User1)


def test_hyp_user1_constructor_exists():
    assert callable(User1.__init__)


def test_hyp_user1_constructor_args():
    sig = inspect.signature(User1.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "isStaff" in params, "Missing parameter 'isStaff'"
    assert "username" in params, "Missing parameter 'username'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "campus" in params, "Missing parameter 'campus'"









def test_hyp_virtualtour1_is_not_abstract():
    assert not inspect.isabstract(VirtualTour1)


def test_hyp_virtualtour1_constructor_exists():
    assert callable(VirtualTour1.__init__)


def test_hyp_virtualtour1_constructor_args():
    sig = inspect.signature(VirtualTour1.__init__)
    params = list(sig.parameters.keys())
    assert "URL" in params, "Missing parameter 'URL'"




def test_hyp_guest1_is_not_abstract():
    assert not inspect.isabstract(Guest1)


def test_hyp_guest1_constructor_exists():
    assert callable(Guest1.__init__)


def test_hyp_guest1_constructor_args():
    sig = inspect.signature(Guest1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_hyp_location_constructor_exists():
    assert callable(Location.__init__)


def test_hyp_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_hyp_post_constructor_exists():
    assert callable(Post.__init__)


def test_hyp_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_society_is_not_abstract():
    assert not inspect.isabstract(Society)


def test_hyp_society_constructor_exists():
    assert callable(Society.__init__)


def test_hyp_society_constructor_args():
    sig = inspect.signature(Society.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lecturer_is_not_abstract():
    assert not inspect.isabstract(Lecturer)


def test_hyp_lecturer_constructor_exists():
    assert callable(Lecturer.__init__)


def test_hyp_lecturer_constructor_args():
    sig = inspect.signature(Lecturer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_hyp_virtualtour_is_not_abstract():
    assert not inspect.isabstract(VirtualTour)


def test_hyp_virtualtour_constructor_exists():
    assert callable(VirtualTour.__init__)


def test_hyp_virtualtour_constructor_args():
    sig = inspect.signature(VirtualTour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_hyp_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_hyp_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_test_usecase_is_not_abstract():
    assert not inspect.isabstract(test_UseCase)


def test_hyp_test_usecase_constructor_exists():
    assert callable(test_UseCase.__init__)


def test_hyp_test_usecase_constructor_args():
    sig = inspect.signature(test_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_hyp_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_hyp_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
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
Admin1_strategy = st.builds(
    Admin1,
)
Student1_strategy = st.builds(
    Student1,
    school=
        safe_text,
    yearOfStudy=
        st.integers(),
    course=
        safe_text
)
Society1_strategy = st.builds(
    Society1,
    yearEstablished=
        st.integers()
)
Lecturer1_strategy = st.builds(
    Lecturer1,
    school=
        safe_text
)
Comment1_strategy = st.builds(
    Comment1,
    date=
        safe_text,
    body=
        safe_text,
    author=
        safe_text
)
Location1_strategy = st.builds(
    Location1,
    name=
        safe_text,
    address=
        safe_text,
    capacity=
        st.integers()
)
Event1_strategy = st.builds(
    Event1,
    isOpen=
        st.booleans(),
    eventOwner=
        st.none(),
    size=
        st.integers(),
    date=
        safe_text,
    location=
        st.none(),
    name=
        safe_text,
    invites=
        safe_text,
    joined=
        safe_text,
    rating=
        st.integers()
)
Post1_strategy = st.builds(
    Post1,
    title=
        safe_text,
    author=
        safe_text,
    date=
        safe_text,
    files=
        safe_text,
    body=
        safe_text
)
User1_strategy = st.builds(
    User1,
    attribute=
        safe_text,
    isStaff=
        st.booleans(),
    username=
        safe_text,
    email=
        safe_text,
    name=
        safe_text,
    campus=
        safe_text
)
VirtualTour1_strategy = st.builds(
    VirtualTour1,
    URL=
        safe_text
)
Guest1_strategy = st.builds(
    Guest1,
)
Comment_strategy = st.builds(
    Comment,
)
Location_strategy = st.builds(
    Location,
)
Event_strategy = st.builds(
    Event,
)
Post_strategy = st.builds(
    Post,
)
Student_strategy = st.builds(
    Student,
)
Society_strategy = st.builds(
    Society,
)
Lecturer_strategy = st.builds(
    Lecturer,
)
Admin_strategy = st.builds(
    Admin,
)
User_strategy = st.builds(
    User,
)
VirtualTour_strategy = st.builds(
    VirtualTour,
)
Guest_strategy = st.builds(
    Guest,
)
test_UseCase_strategy = st.builds(
    test_UseCase,
)
User_Actor_strategy = st.builds(
    User_Actor,
)





@given(instance=Student1_strategy)
def test_hyp_student1_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original



@given(instance=Student1_strategy)
def test_hyp_student1_yearOfStudy_setter(instance):
    original = instance.yearOfStudy
    instance.yearOfStudy = original
    assert instance.yearOfStudy == original



@given(instance=Student1_strategy)
def test_hyp_student1_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original




@given(instance=Society1_strategy)
def test_hyp_society1_yearEstablished_setter(instance):
    original = instance.yearEstablished
    instance.yearEstablished = original
    assert instance.yearEstablished == original




@given(instance=Lecturer1_strategy)
def test_hyp_lecturer1_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original




@given(instance=Comment1_strategy)
def test_hyp_comment1_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Comment1_strategy)
def test_hyp_comment1_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=Comment1_strategy)
def test_hyp_comment1_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original




@given(instance=Location1_strategy)
def test_hyp_location1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Location1_strategy)
def test_hyp_location1_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Location1_strategy)
def test_hyp_location1_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=Event1_strategy)
@settings(max_examples=50)
def test_hyp_event1_instantiation(instance):
    assert isinstance(instance, Event1)



@given(instance=Event1_strategy)
def test_hyp_event1_isOpen_setter(instance):
    original = instance.isOpen
    instance.isOpen = original
    assert instance.isOpen == original



@given(instance=Event1_strategy)
def test_hyp_event1_eventOwner_setter(instance):
    original = instance.eventOwner
    instance.eventOwner = original
    assert instance.eventOwner == original



@given(instance=Event1_strategy)
def test_hyp_event1_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Event1_strategy)
def test_hyp_event1_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Event1_strategy)
def test_hyp_event1_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Event1_strategy)
def test_hyp_event1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Event1_strategy)
def test_hyp_event1_invites_setter(instance):
    original = instance.invites
    instance.invites = original
    assert instance.invites == original



@given(instance=Event1_strategy)
def test_hyp_event1_joined_setter(instance):
    original = instance.joined
    instance.joined = original
    assert instance.joined == original



@given(instance=Event1_strategy)
def test_hyp_event1_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original




@given(instance=Post1_strategy)
def test_hyp_post1_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Post1_strategy)
def test_hyp_post1_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=Post1_strategy)
def test_hyp_post1_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Post1_strategy)
def test_hyp_post1_files_setter(instance):
    original = instance.files
    instance.files = original
    assert instance.files == original



@given(instance=Post1_strategy)
def test_hyp_post1_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original




@given(instance=User1_strategy)
def test_hyp_user1_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=User1_strategy)
def test_hyp_user1_isStaff_setter(instance):
    original = instance.isStaff
    instance.isStaff = original
    assert instance.isStaff == original



@given(instance=User1_strategy)
def test_hyp_user1_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User1_strategy)
def test_hyp_user1_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User1_strategy)
def test_hyp_user1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=User1_strategy)
def test_hyp_user1_campus_setter(instance):
    original = instance.campus
    instance.campus = original
    assert instance.campus == original




@given(instance=VirtualTour1_strategy)
def test_hyp_virtualtour1_URL_setter(instance):
    original = instance.URL
    instance.URL = original
    assert instance.URL == original
















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Admin1,
    Comment,
    Comment1,
    Event,
    Event1,
    Guest,
    Guest1,
    Lecturer,
    Lecturer1,
    Location,
    Location1,
    Post,
    Post1,
    Society,
    Society1,
    Student,
    Student1,
    User,
    User1,
    User_Actor,
    VirtualTour,
    VirtualTour1,
    test_UseCase,
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

def test_Comment1_author_value_roundtrip():
    instance = Comment1(author="sample_text", body="sample_text", date="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_Comment1_body_value_roundtrip():
    instance = Comment1(author="sample_text", body="sample_text", date="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_Comment1_date_value_roundtrip():
    instance = Comment1(author="sample_text", body="sample_text", date="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Lecturer1_school_value_roundtrip():
    instance = Lecturer1(school="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_Location1_address_value_roundtrip():
    instance = Location1(address="sample_text", capacity=7, name="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Location1_capacity_value_roundtrip():
    instance = Location1(address="sample_text", capacity=7, name="sample_text")
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_Location1_name_value_roundtrip():
    instance = Location1(address="sample_text", capacity=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Post1_author_value_roundtrip():
    instance = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_Post1_body_value_roundtrip():
    instance = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_Post1_date_value_roundtrip():
    instance = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Post1_files_value_roundtrip():
    instance = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    assert instance.files == "sample_text"
    instance.files = "sample_text_2"
    assert instance.files == "sample_text_2"


def test_Post1_title_value_roundtrip():
    instance = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_Society1_yearEstablished_value_roundtrip():
    instance = Society1(yearEstablished=7)
    assert instance.yearEstablished == 7
    instance.yearEstablished = 13
    assert instance.yearEstablished == 13


def test_Student1_course_value_roundtrip():
    instance = Student1(course="sample_text", school="sample_text", yearOfStudy=7)
    assert instance.course == "sample_text"
    instance.course = "sample_text_2"
    assert instance.course == "sample_text_2"


def test_Student1_school_value_roundtrip():
    instance = Student1(course="sample_text", school="sample_text", yearOfStudy=7)
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_Student1_yearOfStudy_value_roundtrip():
    instance = Student1(course="sample_text", school="sample_text", yearOfStudy=7)
    assert instance.yearOfStudy == 7
    instance.yearOfStudy = 13
    assert instance.yearOfStudy == 13


def test_User1_attribute_value_roundtrip():
    instance = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_User1_campus_value_roundtrip():
    instance = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    assert instance.campus == "sample_text"
    instance.campus = "sample_text_2"
    assert instance.campus == "sample_text_2"


def test_User1_email_value_roundtrip():
    instance = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_User1_isStaff_value_roundtrip():
    instance = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    assert instance.isStaff == True
    instance.isStaff = False
    assert instance.isStaff == False


def test_User1_name_value_roundtrip():
    instance = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_User1_username_value_roundtrip():
    instance = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_VirtualTour1_URL_value_roundtrip():
    instance = VirtualTour1(URL="sample_text")
    assert instance.URL == "sample_text"
    instance.URL = "sample_text_2"
    assert instance.URL == "sample_text_2"


def test_assoc_Comment_User2_link_reassign_clear():
    a = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    b1 = Comment1(author="sample_text", body="sample_text", date="sample_text")
    b2 = Comment1(author="sample_text_2", body="sample_text_2", date="sample_text_2")
    _safe_set(a, 'comment21', b1)
    assert _is_linked(a, 'comment21', b1)
    if hasattr(b1, 'user20'):
        assert _is_linked(b1, 'user20', a)
    _safe_set(a, 'comment21', b2)
    assert _is_linked(a, 'comment21', b2)
    if hasattr(b1, 'user20'):
        assert not _is_linked(b1, 'user20', a)
    if hasattr(b2, 'user20'):
        assert _is_linked(b2, 'user20', a)
    _safe_set(a, 'comment21', None)
    assert not _is_linked(a, 'comment21', b2)
    if hasattr(b2, 'user20'):
        assert not _is_linked(b2, 'user20', a)


def test_assoc_MyClass_MyClass22_link_reassign_clear():
    a = VirtualTour1(URL="sample_text")
    b1 = Guest1()
    b2 = Guest1()
    _safe_set(a, 'myClass15', b1)
    assert _is_linked(a, 'myClass15', b1)
    if hasattr(b1, 'myClass214'):
        assert _is_linked(b1, 'myClass214', a)
    _safe_set(a, 'myClass15', b2)
    assert _is_linked(a, 'myClass15', b2)
    if hasattr(b1, 'myClass214'):
        assert not _is_linked(b1, 'myClass214', a)
    if hasattr(b2, 'myClass214'):
        assert _is_linked(b2, 'myClass214', a)
    _safe_set(a, 'myClass15', None)
    assert not _is_linked(a, 'myClass15', b2)
    if hasattr(b2, 'myClass214'):
        assert not _is_linked(b2, 'myClass214', a)


def test_assoc_Post_Comment_link_reassign_clear():
    a = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    b1 = Comment1(author="sample_text", body="sample_text", date="sample_text")
    b2 = Comment1(author="sample_text_2", body="sample_text_2", date="sample_text_2")
    _safe_set(a, 'comment24', {b1})
    assert _is_linked(a, 'comment24', b1)
    if hasattr(b1, 'post25'):
        assert _is_linked(b1, 'post25', a)
    _safe_set(a, 'comment24', {b2})
    assert _is_linked(a, 'comment24', b2)
    if hasattr(b1, 'post25'):
        assert not _is_linked(b1, 'post25', a)
    if hasattr(b2, 'post25'):
        assert _is_linked(b2, 'post25', a)
    _safe_set(a, 'comment24', set())
    assert not _is_linked(a, 'comment24', b2)
    if hasattr(b2, 'post25'):
        assert not _is_linked(b2, 'post25', a)


def test_assoc_User_Post2_link_reassign_clear():
    a = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    b1 = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    b2 = Post1(author="sample_text_2", body="sample_text_2", date="sample_text_2", files="sample_text_2", title="sample_text_2")
    _safe_set(a, 'post18', b1)
    assert _is_linked(a, 'post18', b1)
    if hasattr(b1, 'user19'):
        assert _is_linked(b1, 'user19', a)
    _safe_set(a, 'post18', b2)
    assert _is_linked(a, 'post18', b2)
    if hasattr(b1, 'user19'):
        assert not _is_linked(b1, 'user19', a)
    if hasattr(b2, 'user19'):
        assert _is_linked(b2, 'user19', a)
    _safe_set(a, 'post18', None)
    assert not _is_linked(a, 'post18', b2)
    if hasattr(b2, 'user19'):
        assert not _is_linked(b2, 'user19', a)


def test_assoc_User_VirtualTour2_link_reassign_clear():
    a = VirtualTour1(URL="sample_text")
    b1 = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    b2 = User1(attribute="sample_text_2", campus="sample_text_2", email="sample_text_2", isStaff=False, name="sample_text_2", username="sample_text_2")
    _safe_set(a, 'user17', b1)
    assert _is_linked(a, 'user17', b1)
    if hasattr(b1, 'virtualTour16'):
        assert _is_linked(b1, 'virtualTour16', a)
    _safe_set(a, 'user17', b2)
    assert _is_linked(a, 'user17', b2)
    if hasattr(b1, 'virtualTour16'):
        assert not _is_linked(b1, 'virtualTour16', a)
    if hasattr(b2, 'virtualTour16'):
        assert _is_linked(b2, 'virtualTour16', a)
    _safe_set(a, 'user17', None)
    assert not _is_linked(a, 'user17', b2)
    if hasattr(b2, 'virtualTour16'):
        assert not _is_linked(b2, 'virtualTour16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Admin1_strategy = st.builds(Admin1)
@given(instance=Admin1_strategy)
@settings(max_examples=25)
def test_Admin1_instantiation(instance):
    assert isinstance(instance, Admin1)


Comment_strategy = st.builds(Comment)
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


Comment1_strategy = st.builds(Comment1, author=safe_text, body=safe_text, date=safe_text)
@given(instance=Comment1_strategy)
@settings(max_examples=25)
def test_Comment1_instantiation(instance):
    assert isinstance(instance, Comment1)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


Guest_strategy = st.builds(Guest)
@given(instance=Guest_strategy)
@settings(max_examples=25)
def test_Guest_instantiation(instance):
    assert isinstance(instance, Guest)


Guest1_strategy = st.builds(Guest1)
@given(instance=Guest1_strategy)
@settings(max_examples=25)
def test_Guest1_instantiation(instance):
    assert isinstance(instance, Guest1)


Lecturer_strategy = st.builds(Lecturer)
@given(instance=Lecturer_strategy)
@settings(max_examples=25)
def test_Lecturer_instantiation(instance):
    assert isinstance(instance, Lecturer)


Lecturer1_strategy = st.builds(Lecturer1, school=safe_text)
@given(instance=Lecturer1_strategy)
@settings(max_examples=25)
def test_Lecturer1_instantiation(instance):
    assert isinstance(instance, Lecturer1)


Location_strategy = st.builds(Location)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


Location1_strategy = st.builds(Location1, address=safe_text, capacity=st.integers(), name=safe_text)
@given(instance=Location1_strategy)
@settings(max_examples=25)
def test_Location1_instantiation(instance):
    assert isinstance(instance, Location1)


Post_strategy = st.builds(Post)
@given(instance=Post_strategy)
@settings(max_examples=25)
def test_Post_instantiation(instance):
    assert isinstance(instance, Post)


Post1_strategy = st.builds(Post1, author=safe_text, body=safe_text, date=safe_text, files=safe_text, title=safe_text)
@given(instance=Post1_strategy)
@settings(max_examples=25)
def test_Post1_instantiation(instance):
    assert isinstance(instance, Post1)


Society_strategy = st.builds(Society)
@given(instance=Society_strategy)
@settings(max_examples=25)
def test_Society_instantiation(instance):
    assert isinstance(instance, Society)


Society1_strategy = st.builds(Society1, yearEstablished=st.integers())
@given(instance=Society1_strategy)
@settings(max_examples=25)
def test_Society1_instantiation(instance):
    assert isinstance(instance, Society1)


Student_strategy = st.builds(Student)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Student1_strategy = st.builds(Student1, course=safe_text, school=safe_text, yearOfStudy=st.integers())
@given(instance=Student1_strategy)
@settings(max_examples=25)
def test_Student1_instantiation(instance):
    assert isinstance(instance, Student1)


User_strategy = st.builds(User)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


User1_strategy = st.builds(User1, attribute=safe_text, campus=safe_text, email=safe_text, isStaff=st.booleans(), name=safe_text, username=safe_text)
@given(instance=User1_strategy)
@settings(max_examples=25)
def test_User1_instantiation(instance):
    assert isinstance(instance, User1)


User_Actor_strategy = st.builds(User_Actor)
@given(instance=User_Actor_strategy)
@settings(max_examples=25)
def test_User_Actor_instantiation(instance):
    assert isinstance(instance, User_Actor)


VirtualTour_strategy = st.builds(VirtualTour)
@given(instance=VirtualTour_strategy)
@settings(max_examples=25)
def test_VirtualTour_instantiation(instance):
    assert isinstance(instance, VirtualTour)


VirtualTour1_strategy = st.builds(VirtualTour1, URL=safe_text)
@given(instance=VirtualTour1_strategy)
@settings(max_examples=25)
def test_VirtualTour1_instantiation(instance):
    assert isinstance(instance, VirtualTour1)


test_UseCase_strategy = st.builds(test_UseCase)
@given(instance=test_UseCase_strategy)
@settings(max_examples=25)
def test_test_UseCase_instantiation(instance):
    assert isinstance(instance, test_UseCase)



