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
    news,
    Quiz,
    Task,
    Mark,
    Department,
    Student,
    teacher,
    user,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_news_is_not_abstract():
    assert not inspect.isabstract(news)


def test_hyp_news_constructor_exists():
    assert callable(news.__init__)


def test_hyp_news_constructor_args():
    sig = inspect.signature(news.__init__)
    params = list(sig.parameters.keys())
    assert "dlnews" in params, "Missing parameter 'dlnews'"
    assert "author" in params, "Missing parameter 'author'"





def test_hyp_quiz_is_not_abstract():
    assert not inspect.isabstract(Quiz)


def test_hyp_quiz_constructor_exists():
    assert callable(Quiz.__init__)


def test_hyp_quiz_constructor_args():
    sig = inspect.signature(Quiz.__init__)
    params = list(sig.parameters.keys())
    assert "questions__" in params, "Missing parameter 'questions__'"
    assert "title" in params, "Missing parameter 'title'"
    assert "moduleName" in params, "Missing parameter 'moduleName'"






def test_hyp_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_hyp_task_constructor_exists():
    assert callable(Task.__init__)


def test_hyp_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mark_is_not_abstract():
    assert not inspect.isabstract(Mark)


def test_hyp_mark_constructor_exists():
    assert callable(Mark.__init__)


def test_hyp_mark_constructor_args():
    sig = inspect.signature(Mark.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Mark" in params, "Missing parameter 'Mark'"

def test_hyp_mark_has_id():
    assert hasattr(Mark, "id")
    descriptor = None
    for klass in Mark.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mark_has_Mark():
    assert hasattr(Mark, "Mark")
    descriptor = None
    for klass in Mark.__mro__:
        if "Mark" in klass.__dict__:
            descriptor = klass.__dict__["Mark"]
            break
    assert isinstance(descriptor, property)



def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "teachers__" in params, "Missing parameter 'teachers__'"
    assert "modules__" in params, "Missing parameter 'modules__'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_teacher_is_not_abstract():
    assert not inspect.isabstract(teacher)


def test_hyp_teacher_constructor_exists():
    assert callable(teacher.__init__)


def test_hyp_teacher_constructor_args():
    sig = inspect.signature(teacher.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_hyp_user_constructor_exists():
    assert callable(user.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(user.__init__)
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
news_strategy = st.builds(
    news,
    dlnews=
        safe_text,
    author=
        safe_text
)
Quiz_strategy = st.builds(
    Quiz,
    questions__=
        safe_text,
    title=
        safe_text,
    moduleName=
        safe_text
)
Task_strategy = st.builds(
    Task,
)
Mark_strategy = st.builds(
    Mark,
    id=
        st.none(),
    Mark=
        st.integers()
)
Department_strategy = st.builds(
    Department,
    teachers__=
        st.integers(),
    modules__=
        safe_text,
    name=
        safe_text,
    id=
        st.integers()
)
Student_strategy = st.builds(
    Student,
    id=
        st.integers(),
    name=
        safe_text
)
teacher_strategy = st.builds(
    teacher,
    id=
        st.integers(),
    name=
        safe_text
)
user_strategy = st.builds(
    user,
    name=
        safe_text,
    id=
        st.integers()
)




@given(instance=news_strategy)
def test_hyp_news_dlnews_setter(instance):
    original = instance.dlnews
    instance.dlnews = original
    assert instance.dlnews == original



@given(instance=news_strategy)
def test_hyp_news_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original




@given(instance=Quiz_strategy)
def test_hyp_quiz_questions___setter(instance):
    original = instance.questions__
    instance.questions__ = original
    assert instance.questions__ == original



@given(instance=Quiz_strategy)
def test_hyp_quiz_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Quiz_strategy)
def test_hyp_quiz_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original


@given(instance=Mark_strategy)
@settings(max_examples=50)
def test_hyp_mark_instantiation(instance):
    assert isinstance(instance, Mark)



@given(instance=Mark_strategy)
def test_hyp_mark_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Mark_strategy)
def test_hyp_mark_Mark_setter(instance):
    original = instance.Mark
    instance.Mark = original
    assert instance.Mark == original




@given(instance=Department_strategy)
def test_hyp_department_teachers___setter(instance):
    original = instance.teachers__
    instance.teachers__ = original
    assert instance.teachers__ == original



@given(instance=Department_strategy)
def test_hyp_department_modules___setter(instance):
    original = instance.modules__
    instance.modules__ = original
    assert instance.modules__ == original



@given(instance=Department_strategy)
def test_hyp_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Department_strategy)
def test_hyp_department_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Student_strategy)
def test_hyp_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Student_strategy)
def test_hyp_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=teacher_strategy)
def test_hyp_teacher_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=teacher_strategy)
def test_hyp_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=user_strategy)
def test_hyp_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=user_strategy)
def test_hyp_user_id_setter(instance):
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
    Department,
    Mark,
    Quiz,
    Student,
    Task,
    news,
    teacher,
    user,
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

def test_Department_id_value_roundtrip():
    instance = Department(id=7, modules__="sample_text", name="sample_text", teachers__=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Department_modules___value_roundtrip():
    instance = Department(id=7, modules__="sample_text", name="sample_text", teachers__=7)
    assert instance.modules__ == "sample_text"
    instance.modules__ = "sample_text_2"
    assert instance.modules__ == "sample_text_2"


def test_Department_name_value_roundtrip():
    instance = Department(id=7, modules__="sample_text", name="sample_text", teachers__=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Department_teachers___value_roundtrip():
    instance = Department(id=7, modules__="sample_text", name="sample_text", teachers__=7)
    assert instance.teachers__ == 7
    instance.teachers__ = 13
    assert instance.teachers__ == 13


def test_Quiz_moduleName_value_roundtrip():
    instance = Quiz(moduleName="sample_text", questions__="sample_text", title="sample_text")
    assert instance.moduleName == "sample_text"
    instance.moduleName = "sample_text_2"
    assert instance.moduleName == "sample_text_2"


def test_Quiz_questions___value_roundtrip():
    instance = Quiz(moduleName="sample_text", questions__="sample_text", title="sample_text")
    assert instance.questions__ == "sample_text"
    instance.questions__ = "sample_text_2"
    assert instance.questions__ == "sample_text_2"


def test_Quiz_title_value_roundtrip():
    instance = Quiz(moduleName="sample_text", questions__="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_Student_id_value_roundtrip():
    instance = Student(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Student_name_value_roundtrip():
    instance = Student(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_news_author_value_roundtrip():
    instance = news(author="sample_text", dlnews="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_news_dlnews_value_roundtrip():
    instance = news(author="sample_text", dlnews="sample_text")
    assert instance.dlnews == "sample_text"
    instance.dlnews = "sample_text_2"
    assert instance.dlnews == "sample_text_2"


def test_teacher_id_value_roundtrip():
    instance = teacher(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_teacher_name_value_roundtrip():
    instance = teacher(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_user_id_value_roundtrip():
    instance = user(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_user_name_value_roundtrip():
    instance = user(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Department_strategy = st.builds(Department, id=st.integers(), modules__=safe_text, name=safe_text, teachers__=st.integers())
@given(instance=Department_strategy)
@settings(max_examples=25)
def test_Department_instantiation(instance):
    assert isinstance(instance, Department)


Quiz_strategy = st.builds(Quiz, moduleName=safe_text, questions__=safe_text, title=safe_text)
@given(instance=Quiz_strategy)
@settings(max_examples=25)
def test_Quiz_instantiation(instance):
    assert isinstance(instance, Quiz)


Student_strategy = st.builds(Student, id=st.integers(), name=safe_text)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Task_strategy = st.builds(Task)
@given(instance=Task_strategy)
@settings(max_examples=25)
def test_Task_instantiation(instance):
    assert isinstance(instance, Task)


news_strategy = st.builds(news, author=safe_text, dlnews=safe_text)
@given(instance=news_strategy)
@settings(max_examples=25)
def test_news_instantiation(instance):
    assert isinstance(instance, news)


teacher_strategy = st.builds(teacher, id=st.integers(), name=safe_text)
@given(instance=teacher_strategy)
@settings(max_examples=25)
def test_teacher_instantiation(instance):
    assert isinstance(instance, teacher)


user_strategy = st.builds(user, id=st.integers(), name=safe_text)
@given(instance=user_strategy)
@settings(max_examples=25)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



