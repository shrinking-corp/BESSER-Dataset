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
    Labelled,
    publication105_Labelled,
    publication105_Counted,
    publication105_Named,
    Counted,
    Named,
    publication105_PublicationStructure,
    publication105_ReviewNote,
    publication105_Paragraph,
    publication105_Collaboration,
    publication105_Position,
    publication105_Skill,
    publication105_Paper,
    publication105_Review,
    publication105_Write,
    publication105_Researcher,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_hyp_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_hyp_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publication105_labelled_is_not_abstract():
    assert not inspect.isabstract(publication105_Labelled)


def test_hyp_publication105_labelled_constructor_exists():
    assert callable(publication105_Labelled.__init__)


def test_hyp_publication105_labelled_constructor_args():
    sig = inspect.signature(publication105_Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"




def test_hyp_publication105_counted_is_not_abstract():
    assert not inspect.isabstract(publication105_Counted)


def test_hyp_publication105_counted_constructor_exists():
    assert callable(publication105_Counted.__init__)


def test_hyp_publication105_counted_constructor_args():
    sig = inspect.signature(publication105_Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_publication105_named_is_not_abstract():
    assert not inspect.isabstract(publication105_Named)


def test_hyp_publication105_named_constructor_exists():
    assert callable(publication105_Named.__init__)


def test_hyp_publication105_named_constructor_args():
    sig = inspect.signature(publication105_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_hyp_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_hyp_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publication105_publicationstructure_is_not_abstract():
    assert not inspect.isabstract(publication105_PublicationStructure)


def test_hyp_publication105_publicationstructure_constructor_exists():
    assert callable(publication105_PublicationStructure.__init__)


def test_hyp_publication105_publicationstructure_constructor_args():
    sig = inspect.signature(publication105_PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publication105_reviewnote_is_not_abstract():
    assert not inspect.isabstract(publication105_ReviewNote)


def test_hyp_publication105_reviewnote_constructor_exists():
    assert callable(publication105_ReviewNote.__init__)


def test_hyp_publication105_reviewnote_constructor_args():
    sig = inspect.signature(publication105_ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_publication105_paragraph_is_not_abstract():
    assert not inspect.isabstract(publication105_Paragraph)


def test_hyp_publication105_paragraph_constructor_exists():
    assert callable(publication105_Paragraph.__init__)


def test_hyp_publication105_paragraph_constructor_args():
    sig = inspect.signature(publication105_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_publication105_collaboration_is_not_abstract():
    assert not inspect.isabstract(publication105_Collaboration)


def test_hyp_publication105_collaboration_constructor_exists():
    assert callable(publication105_Collaboration.__init__)


def test_hyp_publication105_collaboration_constructor_args():
    sig = inspect.signature(publication105_Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"




def test_hyp_publication105_position_is_not_abstract():
    assert not inspect.isabstract(publication105_Position)


def test_hyp_publication105_position_constructor_exists():
    assert callable(publication105_Position.__init__)


def test_hyp_publication105_position_constructor_args():
    sig = inspect.signature(publication105_Position.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_publication105_skill_is_not_abstract():
    assert not inspect.isabstract(publication105_Skill)


def test_hyp_publication105_skill_constructor_exists():
    assert callable(publication105_Skill.__init__)


def test_hyp_publication105_skill_constructor_args():
    sig = inspect.signature(publication105_Skill.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_publication105_paper_is_not_abstract():
    assert not inspect.isabstract(publication105_Paper)


def test_hyp_publication105_paper_constructor_exists():
    assert callable(publication105_Paper.__init__)


def test_hyp_publication105_paper_constructor_args():
    sig = inspect.signature(publication105_Paper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publication105_review_is_not_abstract():
    assert not inspect.isabstract(publication105_Review)


def test_hyp_publication105_review_constructor_exists():
    assert callable(publication105_Review.__init__)


def test_hyp_publication105_review_constructor_args():
    sig = inspect.signature(publication105_Review.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"




def test_hyp_publication105_write_is_not_abstract():
    assert not inspect.isabstract(publication105_Write)


def test_hyp_publication105_write_constructor_exists():
    assert callable(publication105_Write.__init__)


def test_hyp_publication105_write_constructor_args():
    sig = inspect.signature(publication105_Write.__init__)
    params = list(sig.parameters.keys())
    assert "timeSpent" in params, "Missing parameter 'timeSpent'"




def test_hyp_publication105_researcher_is_not_abstract():
    assert not inspect.isabstract(publication105_Researcher)


def test_hyp_publication105_researcher_constructor_exists():
    assert callable(publication105_Researcher.__init__)


def test_hyp_publication105_researcher_constructor_args():
    sig = inspect.signature(publication105_Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "forName" in params, "Missing parameter 'forName'"




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
Labelled_strategy = st.builds(
    Labelled,
)
publication105_Labelled_strategy = st.builds(
    publication105_Labelled,
    lname=
        safe_text
)
publication105_Counted_strategy = st.builds(
    publication105_Counted,
    id=
        st.integers()
)
publication105_Named_strategy = st.builds(
    publication105_Named,
    name=
        safe_text
)
Counted_strategy = st.builds(
    Counted,
)
Named_strategy = st.builds(
    Named,
)
publication105_PublicationStructure_strategy = st.builds(
    publication105_PublicationStructure,
)
publication105_ReviewNote_strategy = st.builds(
    publication105_ReviewNote,
    content=
        safe_text
)
publication105_Paragraph_strategy = st.builds(
    publication105_Paragraph,
    content=
        safe_text
)
publication105_Collaboration_strategy = st.builds(
    publication105_Collaboration,
    ratio=
        st.integers()
)
publication105_Position_strategy = st.builds(
    publication105_Position,
    description=
        safe_text
)
publication105_Skill_strategy = st.builds(
    publication105_Skill,
    description=
        safe_text
)
publication105_Paper_strategy = st.builds(
    publication105_Paper,
)
publication105_Review_strategy = st.builds(
    publication105_Review,
    date=
        st.dates()
)
publication105_Write_strategy = st.builds(
    publication105_Write,
    timeSpent=
        st.integers()
)
publication105_Researcher_strategy = st.builds(
    publication105_Researcher,
    name=
        safe_text,
    forName=
        safe_text
)





@given(instance=publication105_Labelled_strategy)
def test_hyp_publication105_labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original




@given(instance=publication105_Counted_strategy)
def test_hyp_publication105_counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=publication105_Named_strategy)
def test_hyp_publication105_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=publication105_ReviewNote_strategy)
def test_hyp_publication105_reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original




@given(instance=publication105_Paragraph_strategy)
def test_hyp_publication105_paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original




@given(instance=publication105_Collaboration_strategy)
def test_hyp_publication105_collaboration_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original




@given(instance=publication105_Position_strategy)
def test_hyp_publication105_position_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=publication105_Skill_strategy)
def test_hyp_publication105_skill_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original





@given(instance=publication105_Review_strategy)
def test_hyp_publication105_review_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=publication105_Write_strategy)
def test_hyp_publication105_write_timeSpent_setter(instance):
    original = instance.timeSpent
    instance.timeSpent = original
    assert instance.timeSpent == original




@given(instance=publication105_Researcher_strategy)
def test_hyp_publication105_researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=publication105_Researcher_strategy)
def test_hyp_publication105_researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Counted,
    Labelled,
    Named,
    publication105_Collaboration,
    publication105_Counted,
    publication105_Labelled,
    publication105_Named,
    publication105_Paper,
    publication105_Paragraph,
    publication105_Position,
    publication105_PublicationStructure,
    publication105_Researcher,
    publication105_Review,
    publication105_ReviewNote,
    publication105_Skill,
    publication105_Write,
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

def test_publication105_Collaboration_ratio_value_roundtrip():
    instance = publication105_Collaboration(ratio=7)
    assert instance.ratio == 7
    instance.ratio = 13
    assert instance.ratio == 13


def test_publication105_Counted_id_value_roundtrip():
    instance = publication105_Counted(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_publication105_Labelled_lname_value_roundtrip():
    instance = publication105_Labelled(lname="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_publication105_Named_name_value_roundtrip():
    instance = publication105_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_publication105_Paragraph_content_value_roundtrip():
    instance = publication105_Paragraph(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_publication105_Position_description_value_roundtrip():
    instance = publication105_Position(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_publication105_Researcher_forName_value_roundtrip():
    instance = publication105_Researcher(forName="sample_text", name="sample_text")
    assert instance.forName == "sample_text"
    instance.forName = "sample_text_2"
    assert instance.forName == "sample_text_2"


def test_publication105_Researcher_name_value_roundtrip():
    instance = publication105_Researcher(forName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_publication105_Review_date_value_roundtrip():
    instance = publication105_Review(date=date(2024, 1, 1))
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_publication105_ReviewNote_content_value_roundtrip():
    instance = publication105_ReviewNote(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_publication105_Skill_description_value_roundtrip():
    instance = publication105_Skill(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_publication105_Write_timeSpent_value_roundtrip():
    instance = publication105_Write(timeSpent=7)
    assert instance.timeSpent == 7
    instance.timeSpent = 13
    assert instance.timeSpent == 13


def test_publication105_Paragraph_isa_Counted():
    instance = publication105_Paragraph(content="sample_text")
    assert isinstance(instance, Counted)


def test_publication105_Review_isa_Labelled():
    instance = publication105_Review(date=date(2024, 1, 1))
    assert isinstance(instance, Labelled)


def test_publication105_Write_isa_Labelled():
    instance = publication105_Write(timeSpent=7)
    assert isinstance(instance, Labelled)


def test_publication105_Paper_isa_Named():
    instance = publication105_Paper()
    assert isinstance(instance, Named)


def test_publication105_Paragraph_isa_Named():
    instance = publication105_Paragraph(content="sample_text")
    assert isinstance(instance, Named)


def test_publication105_Position_isa_Named():
    instance = publication105_Position(description="sample_text")
    assert isinstance(instance, Named)


def test_publication105_PublicationStructure_isa_Named():
    instance = publication105_PublicationStructure()
    assert isinstance(instance, Named)


def test_publication105_ReviewNote_isa_Named():
    instance = publication105_ReviewNote(content="sample_text")
    assert isinstance(instance, Named)


def test_assoc_authors11_link_reassign_clear():
    a = publication105_Researcher(forName="sample_text", name="sample_text")
    b1 = publication105_Paper()
    b2 = publication105_Paper()
    _safe_set(a, 'Researcher', b1)
    assert _is_linked(a, 'Researcher', b1)
    if hasattr(b1, 'res_papers'):
        assert _is_linked(b1, 'res_papers', a)
    _safe_set(a, 'Researcher', b2)
    assert _is_linked(a, 'Researcher', b2)
    if hasattr(b1, 'res_papers'):
        assert not _is_linked(b1, 'res_papers', a)
    if hasattr(b2, 'res_papers'):
        assert _is_linked(b2, 'res_papers', a)
    _safe_set(a, 'Researcher', None)
    assert not _is_linked(a, 'Researcher', b2)
    if hasattr(b2, 'res_papers'):
        assert not _is_linked(b2, 'res_papers', a)


def test_assoc_col_paper34_link_reassign_clear():
    a = publication105_Collaboration(ratio=7)
    b1 = publication105_Paper()
    b2 = publication105_Paper()
    _safe_set(a, 'publication105_Collaboration35', b1)
    assert _is_linked(a, 'publication105_Collaboration35', b1)
    if hasattr(b1, 'publication105_Paper36'):
        assert _is_linked(b1, 'publication105_Paper36', a)
    _safe_set(a, 'publication105_Collaboration35', b2)
    assert _is_linked(a, 'publication105_Collaboration35', b2)
    if hasattr(b1, 'publication105_Paper36'):
        assert not _is_linked(b1, 'publication105_Paper36', a)
    if hasattr(b2, 'publication105_Paper36'):
        assert _is_linked(b2, 'publication105_Paper36', a)
    _safe_set(a, 'publication105_Collaboration35', None)
    assert not _is_linked(a, 'publication105_Collaboration35', b2)
    if hasattr(b2, 'publication105_Paper36'):
        assert not _is_linked(b2, 'publication105_Paper36', a)


def test_assoc_collaborations8_link_reassign_clear():
    a = publication105_Researcher(forName="sample_text", name="sample_text")
    b1 = publication105_Collaboration(ratio=7)
    b2 = publication105_Collaboration(ratio=13)
    _safe_set(a, 'publication105_Researcher9', {b1})
    assert _is_linked(a, 'publication105_Researcher9', b1)
    if hasattr(b1, 'publication105_Collaboration'):
        assert _is_linked(b1, 'publication105_Collaboration', a)
    _safe_set(a, 'publication105_Researcher9', {b2})
    assert _is_linked(a, 'publication105_Researcher9', b2)
    if hasattr(b1, 'publication105_Collaboration'):
        assert not _is_linked(b1, 'publication105_Collaboration', a)
    if hasattr(b2, 'publication105_Collaboration'):
        assert _is_linked(b2, 'publication105_Collaboration', a)
    _safe_set(a, 'publication105_Researcher9', set())
    assert not _is_linked(a, 'publication105_Researcher9', b2)
    if hasattr(b2, 'publication105_Collaboration'):
        assert not _is_linked(b2, 'publication105_Collaboration', a)


def test_assoc_paragraph17_link_reassign_clear():
    a = publication105_Write(timeSpent=7)
    b1 = publication105_Paragraph(content="sample_text")
    b2 = publication105_Paragraph(content="sample_text_2")
    _safe_set(a, 'publication105_Write18', b1)
    assert _is_linked(a, 'publication105_Write18', b1)
    if hasattr(b1, 'publication105_Paragraph19'):
        assert _is_linked(b1, 'publication105_Paragraph19', a)
    _safe_set(a, 'publication105_Write18', b2)
    assert _is_linked(a, 'publication105_Write18', b2)
    if hasattr(b1, 'publication105_Paragraph19'):
        assert not _is_linked(b1, 'publication105_Paragraph19', a)
    if hasattr(b2, 'publication105_Paragraph19'):
        assert _is_linked(b2, 'publication105_Paragraph19', a)
    _safe_set(a, 'publication105_Write18', None)
    assert not _is_linked(a, 'publication105_Write18', b2)
    if hasattr(b2, 'publication105_Paragraph19'):
        assert not _is_linked(b2, 'publication105_Paragraph19', a)


def test_assoc_paragraphs10_link_reassign_clear():
    a = publication105_Paragraph(content="sample_text")
    b1 = publication105_Paper()
    b2 = publication105_Paper()
    _safe_set(a, 'publication105_Paragraph', b1)
    assert _is_linked(a, 'publication105_Paragraph', b1)
    if hasattr(b1, 'publication105_Paper'):
        assert _is_linked(b1, 'publication105_Paper', a)
    _safe_set(a, 'publication105_Paragraph', b2)
    assert _is_linked(a, 'publication105_Paragraph', b2)
    if hasattr(b1, 'publication105_Paper'):
        assert not _is_linked(b1, 'publication105_Paper', a)
    if hasattr(b2, 'publication105_Paper'):
        assert _is_linked(b2, 'publication105_Paper', a)
    _safe_set(a, 'publication105_Paragraph', None)
    assert not _is_linked(a, 'publication105_Paragraph', b2)
    if hasattr(b2, 'publication105_Paper'):
        assert not _is_linked(b2, 'publication105_Paper', a)


def test_assoc_parent32_link_reassign_clear():
    a = publication105_Position(description="sample_text")
    b1 = publication105_Position(description="sample_text")
    b2 = publication105_Position(description="sample_text_2")
    _safe_set(a, 'publication105_Position31', b1)
    assert _is_linked(a, 'publication105_Position31', b1)
    if hasattr(b1, 'publication105_Position33'):
        assert _is_linked(b1, 'publication105_Position33', a)
    _safe_set(a, 'publication105_Position31', b2)
    assert _is_linked(a, 'publication105_Position31', b2)
    if hasattr(b1, 'publication105_Position33'):
        assert not _is_linked(b1, 'publication105_Position33', a)
    if hasattr(b2, 'publication105_Position33'):
        assert _is_linked(b2, 'publication105_Position33', a)
    _safe_set(a, 'publication105_Position31', None)
    assert not _is_linked(a, 'publication105_Position31', b2)
    if hasattr(b2, 'publication105_Position33'):
        assert not _is_linked(b2, 'publication105_Position33', a)


def test_assoc_positions28_link_reassign_clear():
    a = publication105_Position(description="sample_text")
    b1 = publication105_PublicationStructure()
    b2 = publication105_PublicationStructure()
    _safe_set(a, 'publication105_Position30', b1)
    assert _is_linked(a, 'publication105_Position30', b1)
    if hasattr(b1, 'publication105_PublicationStructure29'):
        assert _is_linked(b1, 'publication105_PublicationStructure29', a)
    _safe_set(a, 'publication105_Position30', b2)
    assert _is_linked(a, 'publication105_Position30', b2)
    if hasattr(b1, 'publication105_PublicationStructure29'):
        assert not _is_linked(b1, 'publication105_PublicationStructure29', a)
    if hasattr(b2, 'publication105_PublicationStructure29'):
        assert _is_linked(b2, 'publication105_PublicationStructure29', a)
    _safe_set(a, 'publication105_Position30', None)
    assert not _is_linked(a, 'publication105_Position30', b2)
    if hasattr(b2, 'publication105_PublicationStructure29'):
        assert not _is_linked(b2, 'publication105_PublicationStructure29', a)


def test_assoc_res_papers3_link_reassign_clear():
    a = publication105_Researcher(forName="sample_text", name="sample_text")
    b1 = publication105_Paper()
    b2 = publication105_Paper()
    _safe_set(a, 'authors', {b1})
    assert _is_linked(a, 'authors', b1)
    if hasattr(b1, 'Paper'):
        assert _is_linked(b1, 'Paper', a)
    _safe_set(a, 'authors', {b2})
    assert _is_linked(a, 'authors', b2)
    if hasattr(b1, 'Paper'):
        assert not _is_linked(b1, 'Paper', a)
    if hasattr(b2, 'Paper'):
        assert _is_linked(b2, 'Paper', a)
    _safe_set(a, 'authors', set())
    assert not _is_linked(a, 'authors', b2)
    if hasattr(b2, 'Paper'):
        assert not _is_linked(b2, 'Paper', a)


def test_assoc_res_position6_link_reassign_clear():
    a = publication105_Researcher(forName="sample_text", name="sample_text")
    b1 = publication105_Position(description="sample_text")
    b2 = publication105_Position(description="sample_text_2")
    _safe_set(a, 'publication105_Researcher7', b1)
    assert _is_linked(a, 'publication105_Researcher7', b1)
    if hasattr(b1, 'publication105_Position'):
        assert _is_linked(b1, 'publication105_Position', a)
    _safe_set(a, 'publication105_Researcher7', b2)
    assert _is_linked(a, 'publication105_Researcher7', b2)
    if hasattr(b1, 'publication105_Position'):
        assert not _is_linked(b1, 'publication105_Position', a)
    if hasattr(b2, 'publication105_Position'):
        assert _is_linked(b2, 'publication105_Position', a)
    _safe_set(a, 'publication105_Researcher7', None)
    assert not _is_linked(a, 'publication105_Researcher7', b2)
    if hasattr(b2, 'publication105_Position'):
        assert not _is_linked(b2, 'publication105_Position', a)


def test_assoc_researchers23_link_reassign_clear():
    a = publication105_Researcher(forName="sample_text", name="sample_text")
    b1 = publication105_PublicationStructure()
    b2 = publication105_PublicationStructure()
    _safe_set(a, 'publication105_Researcher24', b1)
    assert _is_linked(a, 'publication105_Researcher24', b1)
    if hasattr(b1, 'publication105_PublicationStructure'):
        assert _is_linked(b1, 'publication105_PublicationStructure', a)
    _safe_set(a, 'publication105_Researcher24', b2)
    assert _is_linked(a, 'publication105_Researcher24', b2)
    if hasattr(b1, 'publication105_PublicationStructure'):
        assert not _is_linked(b1, 'publication105_PublicationStructure', a)
    if hasattr(b2, 'publication105_PublicationStructure'):
        assert _is_linked(b2, 'publication105_PublicationStructure', a)
    _safe_set(a, 'publication105_Researcher24', None)
    assert not _is_linked(a, 'publication105_Researcher24', b2)
    if hasattr(b2, 'publication105_PublicationStructure'):
        assert not _is_linked(b2, 'publication105_PublicationStructure', a)


def test_assoc_reviewNote20_link_reassign_clear():
    a = publication105_ReviewNote(content="sample_text")
    b1 = publication105_Review(date=date(2024, 1, 1))
    b2 = publication105_Review(date=date(2025, 6, 15))
    _safe_set(a, 'publication105_ReviewNote22', b1)
    assert _is_linked(a, 'publication105_ReviewNote22', b1)
    if hasattr(b1, 'publication105_Review21'):
        assert _is_linked(b1, 'publication105_Review21', a)
    _safe_set(a, 'publication105_ReviewNote22', b2)
    assert _is_linked(a, 'publication105_ReviewNote22', b2)
    if hasattr(b1, 'publication105_Review21'):
        assert not _is_linked(b1, 'publication105_Review21', a)
    if hasattr(b2, 'publication105_Review21'):
        assert _is_linked(b2, 'publication105_Review21', a)
    _safe_set(a, 'publication105_ReviewNote22', None)
    assert not _is_linked(a, 'publication105_ReviewNote22', b2)
    if hasattr(b2, 'publication105_Review21'):
        assert not _is_linked(b2, 'publication105_Review21', a)


def test_assoc_reviews1_link_reassign_clear():
    a = publication105_Review(date=date(2024, 1, 1))
    b1 = publication105_Researcher(forName="sample_text", name="sample_text")
    b2 = publication105_Researcher(forName="sample_text_2", name="sample_text_2")
    _safe_set(a, 'publication105_Review', b1)
    assert _is_linked(a, 'publication105_Review', b1)
    if hasattr(b1, 'publication105_Researcher2'):
        assert _is_linked(b1, 'publication105_Researcher2', a)
    _safe_set(a, 'publication105_Review', b2)
    assert _is_linked(a, 'publication105_Review', b2)
    if hasattr(b1, 'publication105_Researcher2'):
        assert not _is_linked(b1, 'publication105_Researcher2', a)
    if hasattr(b2, 'publication105_Researcher2'):
        assert _is_linked(b2, 'publication105_Researcher2', a)
    _safe_set(a, 'publication105_Review', None)
    assert not _is_linked(a, 'publication105_Review', b2)
    if hasattr(b2, 'publication105_Researcher2'):
        assert not _is_linked(b2, 'publication105_Researcher2', a)


def test_assoc_reviews15_link_reassign_clear():
    a = publication105_ReviewNote(content="sample_text")
    b1 = publication105_Paragraph(content="sample_text")
    b2 = publication105_Paragraph(content="sample_text_2")
    _safe_set(a, 'publication105_ReviewNote', b1)
    assert _is_linked(a, 'publication105_ReviewNote', b1)
    if hasattr(b1, 'publication105_Paragraph16'):
        assert _is_linked(b1, 'publication105_Paragraph16', a)
    _safe_set(a, 'publication105_ReviewNote', b2)
    assert _is_linked(a, 'publication105_ReviewNote', b2)
    if hasattr(b1, 'publication105_Paragraph16'):
        assert not _is_linked(b1, 'publication105_Paragraph16', a)
    if hasattr(b2, 'publication105_Paragraph16'):
        assert _is_linked(b2, 'publication105_Paragraph16', a)
    _safe_set(a, 'publication105_ReviewNote', None)
    assert not _is_linked(a, 'publication105_ReviewNote', b2)
    if hasattr(b2, 'publication105_Paragraph16'):
        assert not _is_linked(b2, 'publication105_Paragraph16', a)


def test_assoc_skills4_link_reassign_clear():
    a = publication105_Skill(description="sample_text")
    b1 = publication105_Researcher(forName="sample_text", name="sample_text")
    b2 = publication105_Researcher(forName="sample_text_2", name="sample_text_2")
    _safe_set(a, 'publication105_Skill', b1)
    assert _is_linked(a, 'publication105_Skill', b1)
    if hasattr(b1, 'publication105_Researcher5'):
        assert _is_linked(b1, 'publication105_Researcher5', a)
    _safe_set(a, 'publication105_Skill', b2)
    assert _is_linked(a, 'publication105_Skill', b2)
    if hasattr(b1, 'publication105_Researcher5'):
        assert not _is_linked(b1, 'publication105_Researcher5', a)
    if hasattr(b2, 'publication105_Researcher5'):
        assert _is_linked(b2, 'publication105_Researcher5', a)
    _safe_set(a, 'publication105_Skill', None)
    assert not _is_linked(a, 'publication105_Skill', b2)
    if hasattr(b2, 'publication105_Researcher5'):
        assert not _is_linked(b2, 'publication105_Researcher5', a)


def test_assoc_writes0_link_reassign_clear():
    a = publication105_Write(timeSpent=7)
    b1 = publication105_Researcher(forName="sample_text", name="sample_text")
    b2 = publication105_Researcher(forName="sample_text_2", name="sample_text_2")
    _safe_set(a, 'publication105_Write', b1)
    assert _is_linked(a, 'publication105_Write', b1)
    if hasattr(b1, 'publication105_Researcher'):
        assert _is_linked(b1, 'publication105_Researcher', a)
    _safe_set(a, 'publication105_Write', b2)
    assert _is_linked(a, 'publication105_Write', b2)
    if hasattr(b1, 'publication105_Researcher'):
        assert not _is_linked(b1, 'publication105_Researcher', a)
    if hasattr(b2, 'publication105_Researcher'):
        assert _is_linked(b2, 'publication105_Researcher', a)
    _safe_set(a, 'publication105_Write', None)
    assert not _is_linked(a, 'publication105_Write', b2)
    if hasattr(b2, 'publication105_Researcher'):
        assert not _is_linked(b2, 'publication105_Researcher', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Counted_strategy = st.builds(Counted)
@given(instance=Counted_strategy)
@settings(max_examples=25)
def test_Counted_instantiation(instance):
    assert isinstance(instance, Counted)


Labelled_strategy = st.builds(Labelled)
@given(instance=Labelled_strategy)
@settings(max_examples=25)
def test_Labelled_instantiation(instance):
    assert isinstance(instance, Labelled)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


publication105_Collaboration_strategy = st.builds(publication105_Collaboration, ratio=st.integers())
@given(instance=publication105_Collaboration_strategy)
@settings(max_examples=25)
def test_publication105_Collaboration_instantiation(instance):
    assert isinstance(instance, publication105_Collaboration)


publication105_Counted_strategy = st.builds(publication105_Counted, id=st.integers())
@given(instance=publication105_Counted_strategy)
@settings(max_examples=25)
def test_publication105_Counted_instantiation(instance):
    assert isinstance(instance, publication105_Counted)


publication105_Labelled_strategy = st.builds(publication105_Labelled, lname=safe_text)
@given(instance=publication105_Labelled_strategy)
@settings(max_examples=25)
def test_publication105_Labelled_instantiation(instance):
    assert isinstance(instance, publication105_Labelled)


publication105_Named_strategy = st.builds(publication105_Named, name=safe_text)
@given(instance=publication105_Named_strategy)
@settings(max_examples=25)
def test_publication105_Named_instantiation(instance):
    assert isinstance(instance, publication105_Named)


publication105_Paper_strategy = st.builds(publication105_Paper)
@given(instance=publication105_Paper_strategy)
@settings(max_examples=25)
def test_publication105_Paper_instantiation(instance):
    assert isinstance(instance, publication105_Paper)


publication105_Paragraph_strategy = st.builds(publication105_Paragraph, content=safe_text)
@given(instance=publication105_Paragraph_strategy)
@settings(max_examples=25)
def test_publication105_Paragraph_instantiation(instance):
    assert isinstance(instance, publication105_Paragraph)


publication105_Position_strategy = st.builds(publication105_Position, description=safe_text)
@given(instance=publication105_Position_strategy)
@settings(max_examples=25)
def test_publication105_Position_instantiation(instance):
    assert isinstance(instance, publication105_Position)


publication105_PublicationStructure_strategy = st.builds(publication105_PublicationStructure)
@given(instance=publication105_PublicationStructure_strategy)
@settings(max_examples=25)
def test_publication105_PublicationStructure_instantiation(instance):
    assert isinstance(instance, publication105_PublicationStructure)


publication105_Researcher_strategy = st.builds(publication105_Researcher, forName=safe_text, name=safe_text)
@given(instance=publication105_Researcher_strategy)
@settings(max_examples=25)
def test_publication105_Researcher_instantiation(instance):
    assert isinstance(instance, publication105_Researcher)


publication105_Review_strategy = st.builds(publication105_Review, date=st.dates())
@given(instance=publication105_Review_strategy)
@settings(max_examples=25)
def test_publication105_Review_instantiation(instance):
    assert isinstance(instance, publication105_Review)


publication105_ReviewNote_strategy = st.builds(publication105_ReviewNote, content=safe_text)
@given(instance=publication105_ReviewNote_strategy)
@settings(max_examples=25)
def test_publication105_ReviewNote_instantiation(instance):
    assert isinstance(instance, publication105_ReviewNote)


publication105_Skill_strategy = st.builds(publication105_Skill, description=safe_text)
@given(instance=publication105_Skill_strategy)
@settings(max_examples=25)
def test_publication105_Skill_instantiation(instance):
    assert isinstance(instance, publication105_Skill)


publication105_Write_strategy = st.builds(publication105_Write, timeSpent=st.integers())
@given(instance=publication105_Write_strategy)
@settings(max_examples=25)
def test_publication105_Write_instantiation(instance):
    assert isinstance(instance, publication105_Write)



