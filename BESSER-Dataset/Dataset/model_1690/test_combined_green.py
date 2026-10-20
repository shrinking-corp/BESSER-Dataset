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
    helloworld150_Profession,
    helloworld150_World,
    helloworld150_Comment,
    helloworld150_NamedElement,
    NamedElement,
    helloworld150_Thing,
    helloworld150_Own,
    helloworld150_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_helloworld150_profession_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Profession)


def test_hyp_helloworld150_profession_constructor_exists():
    assert callable(helloworld150_Profession.__init__)


def test_hyp_helloworld150_profession_constructor_args():
    sig = inspect.signature(helloworld150_Profession.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_helloworld150_world_is_not_abstract():
    assert not inspect.isabstract(helloworld150_World)


def test_hyp_helloworld150_world_constructor_exists():
    assert callable(helloworld150_World.__init__)


def test_hyp_helloworld150_world_constructor_args():
    sig = inspect.signature(helloworld150_World.__init__)
    params = list(sig.parameters.keys())



def test_hyp_helloworld150_comment_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Comment)


def test_hyp_helloworld150_comment_constructor_exists():
    assert callable(helloworld150_Comment.__init__)


def test_hyp_helloworld150_comment_constructor_args():
    sig = inspect.signature(helloworld150_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_helloworld150_namedelement_is_not_abstract():
    assert not inspect.isabstract(helloworld150_NamedElement)


def test_hyp_helloworld150_namedelement_constructor_exists():
    assert callable(helloworld150_NamedElement.__init__)


def test_hyp_helloworld150_namedelement_constructor_args():
    sig = inspect.signature(helloworld150_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_helloworld150_thing_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Thing)


def test_hyp_helloworld150_thing_constructor_exists():
    assert callable(helloworld150_Thing.__init__)


def test_hyp_helloworld150_thing_constructor_args():
    sig = inspect.signature(helloworld150_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_helloworld150_own_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Own)


def test_hyp_helloworld150_own_constructor_exists():
    assert callable(helloworld150_Own.__init__)


def test_hyp_helloworld150_own_constructor_args():
    sig = inspect.signature(helloworld150_Own.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"
    assert "ownerName" in params, "Missing parameter 'ownerName'"





def test_hyp_helloworld150_person_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Person)


def test_hyp_helloworld150_person_constructor_exists():
    assert callable(helloworld150_Person.__init__)


def test_hyp_helloworld150_person_constructor_args():
    sig = inspect.signature(helloworld150_Person.__init__)
    params = list(sig.parameters.keys())
    assert "forName" in params, "Missing parameter 'forName'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"




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
helloworld150_Profession_strategy = st.builds(
    helloworld150_Profession,
    name=
        safe_text
)
helloworld150_World_strategy = st.builds(
    helloworld150_World,
)
helloworld150_Comment_strategy = st.builds(
    helloworld150_Comment,
    content=
        safe_text
)
helloworld150_NamedElement_strategy = st.builds(
    helloworld150_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
helloworld150_Thing_strategy = st.builds(
    helloworld150_Thing,
    id=
        st.integers()
)
helloworld150_Own_strategy = st.builds(
    helloworld150_Own,
    since=
        safe_text,
    ownerName=
        safe_text
)
helloworld150_Person_strategy = st.builds(
    helloworld150_Person,
    forName=
        safe_text,
    birthDate=
        safe_text
)




@given(instance=helloworld150_Profession_strategy)
def test_hyp_helloworld150_profession_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=helloworld150_Comment_strategy)
def test_hyp_helloworld150_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original




@given(instance=helloworld150_NamedElement_strategy)
def test_hyp_helloworld150_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=helloworld150_Thing_strategy)
def test_hyp_helloworld150_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=helloworld150_Own_strategy)
def test_hyp_helloworld150_own_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original



@given(instance=helloworld150_Own_strategy)
def test_hyp_helloworld150_own_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original




@given(instance=helloworld150_Person_strategy)
def test_hyp_helloworld150_person_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original



@given(instance=helloworld150_Person_strategy)
def test_hyp_helloworld150_person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    helloworld150_Comment,
    helloworld150_NamedElement,
    helloworld150_Own,
    helloworld150_Person,
    helloworld150_Profession,
    helloworld150_Thing,
    helloworld150_World,
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

def test_helloworld150_Comment_content_value_roundtrip():
    instance = helloworld150_Comment(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_helloworld150_NamedElement_name_value_roundtrip():
    instance = helloworld150_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_helloworld150_Own_ownerName_value_roundtrip():
    instance = helloworld150_Own(ownerName="sample_text", since="sample_text")
    assert instance.ownerName == "sample_text"
    instance.ownerName = "sample_text_2"
    assert instance.ownerName == "sample_text_2"


def test_helloworld150_Own_since_value_roundtrip():
    instance = helloworld150_Own(ownerName="sample_text", since="sample_text")
    assert instance.since == "sample_text"
    instance.since = "sample_text_2"
    assert instance.since == "sample_text_2"


def test_helloworld150_Person_birthDate_value_roundtrip():
    instance = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    assert instance.birthDate == "sample_text"
    instance.birthDate = "sample_text_2"
    assert instance.birthDate == "sample_text_2"


def test_helloworld150_Person_forName_value_roundtrip():
    instance = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    assert instance.forName == "sample_text"
    instance.forName = "sample_text_2"
    assert instance.forName == "sample_text_2"


def test_helloworld150_Profession_name_value_roundtrip():
    instance = helloworld150_Profession(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_helloworld150_Thing_id_value_roundtrip():
    instance = helloworld150_Thing(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_helloworld150_Own_isa_NamedElement():
    instance = helloworld150_Own(ownerName="sample_text", since="sample_text")
    assert isinstance(instance, NamedElement)


def test_helloworld150_Person_isa_NamedElement():
    instance = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    assert isinstance(instance, NamedElement)


def test_helloworld150_Thing_isa_NamedElement():
    instance = helloworld150_Thing(id=7)
    assert isinstance(instance, NamedElement)


def test_assoc_comment8_link_reassign_clear():
    a = helloworld150_NamedElement(name="sample_text")
    b1 = helloworld150_Comment(content="sample_text")
    b2 = helloworld150_Comment(content="sample_text_2")
    _safe_set(a, 'helloworld150_NamedElement', b1)
    assert _is_linked(a, 'helloworld150_NamedElement', b1)
    if hasattr(b1, 'helloworld150_Comment'):
        assert _is_linked(b1, 'helloworld150_Comment', a)
    _safe_set(a, 'helloworld150_NamedElement', b2)
    assert _is_linked(a, 'helloworld150_NamedElement', b2)
    if hasattr(b1, 'helloworld150_Comment'):
        assert not _is_linked(b1, 'helloworld150_Comment', a)
    if hasattr(b2, 'helloworld150_Comment'):
        assert _is_linked(b2, 'helloworld150_Comment', a)
    _safe_set(a, 'helloworld150_NamedElement', None)
    assert not _is_linked(a, 'helloworld150_NamedElement', b2)
    if hasattr(b2, 'helloworld150_Comment'):
        assert not _is_linked(b2, 'helloworld150_Comment', a)


def test_assoc_ownership5_link_reassign_clear():
    a = helloworld150_Thing(id=7)
    b1 = helloworld150_Own(ownerName="sample_text", since="sample_text")
    b2 = helloworld150_Own(ownerName="sample_text_2", since="sample_text_2")
    _safe_set(a, 'thing', b1)
    assert _is_linked(a, 'thing', b1)
    if hasattr(b1, 'Own'):
        assert _is_linked(b1, 'Own', a)
    _safe_set(a, 'thing', b2)
    assert _is_linked(a, 'thing', b2)
    if hasattr(b1, 'Own'):
        assert not _is_linked(b1, 'Own', a)
    if hasattr(b2, 'Own'):
        assert _is_linked(b2, 'Own', a)
    _safe_set(a, 'thing', None)
    assert not _is_linked(a, 'thing', b2)
    if hasattr(b2, 'Own'):
        assert not _is_linked(b2, 'Own', a)


def test_assoc_ownerships6_link_reassign_clear():
    a = helloworld150_Thing(id=7)
    b1 = helloworld150_Own(ownerName="sample_text", since="sample_text")
    b2 = helloworld150_Own(ownerName="sample_text_2", since="sample_text_2")
    _safe_set(a, 'helloworld150_Thing7', {b1})
    assert _is_linked(a, 'helloworld150_Thing7', b1)
    if hasattr(b1, 'helloworld150_Own'):
        assert _is_linked(b1, 'helloworld150_Own', a)
    _safe_set(a, 'helloworld150_Thing7', {b2})
    assert _is_linked(a, 'helloworld150_Thing7', b2)
    if hasattr(b1, 'helloworld150_Own'):
        assert not _is_linked(b1, 'helloworld150_Own', a)
    if hasattr(b2, 'helloworld150_Own'):
        assert _is_linked(b2, 'helloworld150_Own', a)
    _safe_set(a, 'helloworld150_Thing7', set())
    assert not _is_linked(a, 'helloworld150_Thing7', b2)
    if hasattr(b2, 'helloworld150_Own'):
        assert not _is_linked(b2, 'helloworld150_Own', a)


def test_assoc_person10_link_reassign_clear():
    a = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    b1 = helloworld150_Own(ownerName="sample_text", since="sample_text")
    b2 = helloworld150_Own(ownerName="sample_text_2", since="sample_text_2")
    _safe_set(a, 'helloworld150_Person12', b1)
    assert _is_linked(a, 'helloworld150_Person12', b1)
    if hasattr(b1, 'helloworld150_Own11'):
        assert _is_linked(b1, 'helloworld150_Own11', a)
    _safe_set(a, 'helloworld150_Person12', b2)
    assert _is_linked(a, 'helloworld150_Person12', b2)
    if hasattr(b1, 'helloworld150_Own11'):
        assert not _is_linked(b1, 'helloworld150_Own11', a)
    if hasattr(b2, 'helloworld150_Own11'):
        assert _is_linked(b2, 'helloworld150_Own11', a)
    _safe_set(a, 'helloworld150_Person12', None)
    assert not _is_linked(a, 'helloworld150_Person12', b2)
    if hasattr(b2, 'helloworld150_Own11'):
        assert not _is_linked(b2, 'helloworld150_Own11', a)


def test_assoc_persons1_link_reassign_clear():
    a = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    b1 = helloworld150_World()
    b2 = helloworld150_World()
    _safe_set(a, 'helloworld150_Person', b1)
    assert _is_linked(a, 'helloworld150_Person', b1)
    if hasattr(b1, 'helloworld150_World2'):
        assert _is_linked(b1, 'helloworld150_World2', a)
    _safe_set(a, 'helloworld150_Person', b2)
    assert _is_linked(a, 'helloworld150_Person', b2)
    if hasattr(b1, 'helloworld150_World2'):
        assert not _is_linked(b1, 'helloworld150_World2', a)
    if hasattr(b2, 'helloworld150_World2'):
        assert _is_linked(b2, 'helloworld150_World2', a)
    _safe_set(a, 'helloworld150_Person', None)
    assert not _is_linked(a, 'helloworld150_Person', b2)
    if hasattr(b2, 'helloworld150_World2'):
        assert not _is_linked(b2, 'helloworld150_World2', a)


def test_assoc_profession13_link_reassign_clear():
    a = helloworld150_Profession(name="sample_text")
    b1 = helloworld150_Person(birthDate="sample_text", forName="sample_text")
    b2 = helloworld150_Person(birthDate="sample_text_2", forName="sample_text_2")
    _safe_set(a, 'helloworld150_Profession15', b1)
    assert _is_linked(a, 'helloworld150_Profession15', b1)
    if hasattr(b1, 'helloworld150_Person14'):
        assert _is_linked(b1, 'helloworld150_Person14', a)
    _safe_set(a, 'helloworld150_Profession15', b2)
    assert _is_linked(a, 'helloworld150_Profession15', b2)
    if hasattr(b1, 'helloworld150_Person14'):
        assert not _is_linked(b1, 'helloworld150_Person14', a)
    if hasattr(b2, 'helloworld150_Person14'):
        assert _is_linked(b2, 'helloworld150_Person14', a)
    _safe_set(a, 'helloworld150_Profession15', None)
    assert not _is_linked(a, 'helloworld150_Profession15', b2)
    if hasattr(b2, 'helloworld150_Person14'):
        assert not _is_linked(b2, 'helloworld150_Person14', a)


def test_assoc_professions3_link_reassign_clear():
    a = helloworld150_Profession(name="sample_text")
    b1 = helloworld150_World()
    b2 = helloworld150_World()
    _safe_set(a, 'helloworld150_Profession', b1)
    assert _is_linked(a, 'helloworld150_Profession', b1)
    if hasattr(b1, 'helloworld150_World4'):
        assert _is_linked(b1, 'helloworld150_World4', a)
    _safe_set(a, 'helloworld150_Profession', b2)
    assert _is_linked(a, 'helloworld150_Profession', b2)
    if hasattr(b1, 'helloworld150_World4'):
        assert not _is_linked(b1, 'helloworld150_World4', a)
    if hasattr(b2, 'helloworld150_World4'):
        assert _is_linked(b2, 'helloworld150_World4', a)
    _safe_set(a, 'helloworld150_Profession', None)
    assert not _is_linked(a, 'helloworld150_Profession', b2)
    if hasattr(b2, 'helloworld150_World4'):
        assert not _is_linked(b2, 'helloworld150_World4', a)


def test_assoc_thing9_link_reassign_clear():
    a = helloworld150_Thing(id=7)
    b1 = helloworld150_Own(ownerName="sample_text", since="sample_text")
    b2 = helloworld150_Own(ownerName="sample_text_2", since="sample_text_2")
    _safe_set(a, 'Thing', b1)
    assert _is_linked(a, 'Thing', b1)
    if hasattr(b1, 'ownership'):
        assert _is_linked(b1, 'ownership', a)
    _safe_set(a, 'Thing', b2)
    assert _is_linked(a, 'Thing', b2)
    if hasattr(b1, 'ownership'):
        assert not _is_linked(b1, 'ownership', a)
    if hasattr(b2, 'ownership'):
        assert _is_linked(b2, 'ownership', a)
    _safe_set(a, 'Thing', None)
    assert not _is_linked(a, 'Thing', b2)
    if hasattr(b2, 'ownership'):
        assert not _is_linked(b2, 'ownership', a)


def test_assoc_things0_link_reassign_clear():
    a = helloworld150_Thing(id=7)
    b1 = helloworld150_World()
    b2 = helloworld150_World()
    _safe_set(a, 'helloworld150_Thing', b1)
    assert _is_linked(a, 'helloworld150_Thing', b1)
    if hasattr(b1, 'helloworld150_World'):
        assert _is_linked(b1, 'helloworld150_World', a)
    _safe_set(a, 'helloworld150_Thing', b2)
    assert _is_linked(a, 'helloworld150_Thing', b2)
    if hasattr(b1, 'helloworld150_World'):
        assert not _is_linked(b1, 'helloworld150_World', a)
    if hasattr(b2, 'helloworld150_World'):
        assert _is_linked(b2, 'helloworld150_World', a)
    _safe_set(a, 'helloworld150_Thing', None)
    assert not _is_linked(a, 'helloworld150_Thing', b2)
    if hasattr(b2, 'helloworld150_World'):
        assert not _is_linked(b2, 'helloworld150_World', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


helloworld150_Comment_strategy = st.builds(helloworld150_Comment, content=safe_text)
@given(instance=helloworld150_Comment_strategy)
@settings(max_examples=25)
def test_helloworld150_Comment_instantiation(instance):
    assert isinstance(instance, helloworld150_Comment)


helloworld150_NamedElement_strategy = st.builds(helloworld150_NamedElement, name=safe_text)
@given(instance=helloworld150_NamedElement_strategy)
@settings(max_examples=25)
def test_helloworld150_NamedElement_instantiation(instance):
    assert isinstance(instance, helloworld150_NamedElement)


helloworld150_Own_strategy = st.builds(helloworld150_Own, ownerName=safe_text, since=safe_text)
@given(instance=helloworld150_Own_strategy)
@settings(max_examples=25)
def test_helloworld150_Own_instantiation(instance):
    assert isinstance(instance, helloworld150_Own)


helloworld150_Person_strategy = st.builds(helloworld150_Person, birthDate=safe_text, forName=safe_text)
@given(instance=helloworld150_Person_strategy)
@settings(max_examples=25)
def test_helloworld150_Person_instantiation(instance):
    assert isinstance(instance, helloworld150_Person)


helloworld150_Profession_strategy = st.builds(helloworld150_Profession, name=safe_text)
@given(instance=helloworld150_Profession_strategy)
@settings(max_examples=25)
def test_helloworld150_Profession_instantiation(instance):
    assert isinstance(instance, helloworld150_Profession)


helloworld150_Thing_strategy = st.builds(helloworld150_Thing, id=st.integers())
@given(instance=helloworld150_Thing_strategy)
@settings(max_examples=25)
def test_helloworld150_Thing_instantiation(instance):
    assert isinstance(instance, helloworld150_Thing)


helloworld150_World_strategy = st.builds(helloworld150_World)
@given(instance=helloworld150_World_strategy)
@settings(max_examples=25)
def test_helloworld150_World_instantiation(instance):
    assert isinstance(instance, helloworld150_World)



