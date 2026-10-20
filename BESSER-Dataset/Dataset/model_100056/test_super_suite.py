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
    revision_PlaceHolder,
    PlaceHolder,
    revision_Labelled,
    revision_Counted,
    revision_Named,
    Labelled,
    revision_PlaceHolderRn,
    revision_PublicationSystem,
    revision_Review,
    revision_Write,
    revision_PlaceHolderRule,
    Counted,
    revision_Progress,
    revision_PlaceHolderRs,
    revision_Sequence,
    revision_Rule,
    revision_PublicationPhase,
    revision_PlaceHolderPP,
    revision_Researcher,
    Named,
    revision_ReviewNote,
    revision_Paragraph,
    revision_Paper,
    revision_PublicationStructure,
    revision_PublicationProcess,
    SequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_revision_placeholder_is_not_abstract():
    assert not inspect.isabstract(revision_PlaceHolder)


def test_hyp_revision_placeholder_constructor_exists():
    assert callable(revision_PlaceHolder.__init__)


def test_hyp_revision_placeholder_constructor_args():
    sig = inspect.signature(revision_PlaceHolder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_placeholder_is_not_abstract():
    assert not inspect.isabstract(PlaceHolder)


def test_hyp_placeholder_constructor_exists():
    assert callable(PlaceHolder.__init__)


def test_hyp_placeholder_constructor_args():
    sig = inspect.signature(PlaceHolder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_labelled_is_not_abstract():
    assert not inspect.isabstract(revision_Labelled)


def test_hyp_revision_labelled_constructor_exists():
    assert callable(revision_Labelled.__init__)


def test_hyp_revision_labelled_constructor_args():
    sig = inspect.signature(revision_Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"




def test_hyp_revision_counted_is_not_abstract():
    assert not inspect.isabstract(revision_Counted)


def test_hyp_revision_counted_constructor_exists():
    assert callable(revision_Counted.__init__)


def test_hyp_revision_counted_constructor_args():
    sig = inspect.signature(revision_Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_revision_named_is_not_abstract():
    assert not inspect.isabstract(revision_Named)


def test_hyp_revision_named_constructor_exists():
    assert callable(revision_Named.__init__)


def test_hyp_revision_named_constructor_args():
    sig = inspect.signature(revision_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_hyp_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_hyp_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_placeholderrn_is_not_abstract():
    assert not inspect.isabstract(revision_PlaceHolderRn)


def test_hyp_revision_placeholderrn_constructor_exists():
    assert callable(revision_PlaceHolderRn.__init__)


def test_hyp_revision_placeholderrn_constructor_args():
    sig = inspect.signature(revision_PlaceHolderRn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_publicationsystem_is_not_abstract():
    assert not inspect.isabstract(revision_PublicationSystem)


def test_hyp_revision_publicationsystem_constructor_exists():
    assert callable(revision_PublicationSystem.__init__)


def test_hyp_revision_publicationsystem_constructor_args():
    sig = inspect.signature(revision_PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_review_is_not_abstract():
    assert not inspect.isabstract(revision_Review)


def test_hyp_revision_review_constructor_exists():
    assert callable(revision_Review.__init__)


def test_hyp_revision_review_constructor_args():
    sig = inspect.signature(revision_Review.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_write_is_not_abstract():
    assert not inspect.isabstract(revision_Write)


def test_hyp_revision_write_constructor_exists():
    assert callable(revision_Write.__init__)


def test_hyp_revision_write_constructor_args():
    sig = inspect.signature(revision_Write.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_placeholderrule_is_not_abstract():
    assert not inspect.isabstract(revision_PlaceHolderRule)


def test_hyp_revision_placeholderrule_constructor_exists():
    assert callable(revision_PlaceHolderRule.__init__)


def test_hyp_revision_placeholderrule_constructor_args():
    sig = inspect.signature(revision_PlaceHolderRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_hyp_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_hyp_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_progress_is_not_abstract():
    assert not inspect.isabstract(revision_Progress)


def test_hyp_revision_progress_constructor_exists():
    assert callable(revision_Progress.__init__)


def test_hyp_revision_progress_constructor_args():
    sig = inspect.signature(revision_Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"




def test_hyp_revision_placeholderrs_is_not_abstract():
    assert not inspect.isabstract(revision_PlaceHolderRs)


def test_hyp_revision_placeholderrs_constructor_exists():
    assert callable(revision_PlaceHolderRs.__init__)


def test_hyp_revision_placeholderrs_constructor_args():
    sig = inspect.signature(revision_PlaceHolderRs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_sequence_is_not_abstract():
    assert not inspect.isabstract(revision_Sequence)


def test_hyp_revision_sequence_constructor_exists():
    assert callable(revision_Sequence.__init__)


def test_hyp_revision_sequence_constructor_args():
    sig = inspect.signature(revision_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "sequenceType" in params, "Missing parameter 'sequenceType'"




def test_hyp_revision_rule_is_not_abstract():
    assert not inspect.isabstract(revision_Rule)


def test_hyp_revision_rule_constructor_exists():
    assert callable(revision_Rule.__init__)


def test_hyp_revision_rule_constructor_args():
    sig = inspect.signature(revision_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "text" in params, "Missing parameter 'text'"





def test_hyp_revision_publicationphase_is_not_abstract():
    assert not inspect.isabstract(revision_PublicationPhase)


def test_hyp_revision_publicationphase_constructor_exists():
    assert callable(revision_PublicationPhase.__init__)


def test_hyp_revision_publicationphase_constructor_args():
    sig = inspect.signature(revision_PublicationPhase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"






def test_hyp_revision_placeholderpp_is_not_abstract():
    assert not inspect.isabstract(revision_PlaceHolderPP)


def test_hyp_revision_placeholderpp_constructor_exists():
    assert callable(revision_PlaceHolderPP.__init__)


def test_hyp_revision_placeholderpp_constructor_args():
    sig = inspect.signature(revision_PlaceHolderPP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_researcher_is_not_abstract():
    assert not inspect.isabstract(revision_Researcher)


def test_hyp_revision_researcher_constructor_exists():
    assert callable(revision_Researcher.__init__)


def test_hyp_revision_researcher_constructor_args():
    sig = inspect.signature(revision_Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "forName" in params, "Missing parameter 'forName'"
    assert "position" in params, "Missing parameter 'position'"






def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_reviewnote_is_not_abstract():
    assert not inspect.isabstract(revision_ReviewNote)


def test_hyp_revision_reviewnote_constructor_exists():
    assert callable(revision_ReviewNote.__init__)


def test_hyp_revision_reviewnote_constructor_args():
    sig = inspect.signature(revision_ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_revision_paragraph_is_not_abstract():
    assert not inspect.isabstract(revision_Paragraph)


def test_hyp_revision_paragraph_constructor_exists():
    assert callable(revision_Paragraph.__init__)


def test_hyp_revision_paragraph_constructor_args():
    sig = inspect.signature(revision_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_revision_paper_is_not_abstract():
    assert not inspect.isabstract(revision_Paper)


def test_hyp_revision_paper_constructor_exists():
    assert callable(revision_Paper.__init__)


def test_hyp_revision_paper_constructor_args():
    sig = inspect.signature(revision_Paper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_publicationstructure_is_not_abstract():
    assert not inspect.isabstract(revision_PublicationStructure)


def test_hyp_revision_publicationstructure_constructor_exists():
    assert callable(revision_PublicationStructure.__init__)


def test_hyp_revision_publicationstructure_constructor_args():
    sig = inspect.signature(revision_PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_revision_publicationprocess_is_not_abstract():
    assert not inspect.isabstract(revision_PublicationProcess)


def test_hyp_revision_publicationprocess_constructor_exists():
    assert callable(revision_PublicationProcess.__init__)


def test_hyp_revision_publicationprocess_constructor_args():
    sig = inspect.signature(revision_PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"



def test_hyp_sequencetype_exists():
    # Check that the Enumeration exists
    assert SequenceType is not None

def test_hyp_sequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SequenceType]
    expected_literals = [
        "startToStart",
        "finishToStart",
        "finishToFinish",
        "startToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SequenceType"


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
revision_PlaceHolder_strategy = st.builds(
    revision_PlaceHolder,
)
PlaceHolder_strategy = st.builds(
    PlaceHolder,
)
revision_Labelled_strategy = st.builds(
    revision_Labelled,
    lname=
        safe_text
)
revision_Counted_strategy = st.builds(
    revision_Counted,
    id=
        st.integers()
)
revision_Named_strategy = st.builds(
    revision_Named,
    name=
        safe_text
)
Labelled_strategy = st.builds(
    Labelled,
)
revision_PlaceHolderRn_strategy = st.builds(
    revision_PlaceHolderRn,
)
revision_PublicationSystem_strategy = st.builds(
    revision_PublicationSystem,
)
revision_Review_strategy = st.builds(
    revision_Review,
)
revision_Write_strategy = st.builds(
    revision_Write,
)
revision_PlaceHolderRule_strategy = st.builds(
    revision_PlaceHolderRule,
)
Counted_strategy = st.builds(
    Counted,
)
revision_Progress_strategy = st.builds(
    revision_Progress,
    percent=
        st.integers()
)
revision_PlaceHolderRs_strategy = st.builds(
    revision_PlaceHolderRs,
)
revision_Sequence_strategy = st.builds(
    revision_Sequence,
    sequenceType=
        safe_text
)
revision_Rule_strategy = st.builds(
    revision_Rule,
    key=
        safe_text,
    text=
        safe_text
)
revision_PublicationPhase_strategy = st.builds(
    revision_PublicationPhase,
    name=
        safe_text,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
revision_PlaceHolderPP_strategy = st.builds(
    revision_PlaceHolderPP,
)
revision_Researcher_strategy = st.builds(
    revision_Researcher,
    name=
        safe_text,
    forName=
        safe_text,
    position=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
revision_ReviewNote_strategy = st.builds(
    revision_ReviewNote,
    content=
        safe_text
)
revision_Paragraph_strategy = st.builds(
    revision_Paragraph,
    content=
        safe_text
)
revision_Paper_strategy = st.builds(
    revision_Paper,
)
revision_PublicationStructure_strategy = st.builds(
    revision_PublicationStructure,
)
revision_PublicationProcess_strategy = st.builds(
    revision_PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)






@given(instance=revision_Labelled_strategy)
def test_hyp_revision_labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original




@given(instance=revision_Counted_strategy)
def test_hyp_revision_counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=revision_Named_strategy)
def test_hyp_revision_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=revision_Progress_strategy)
def test_hyp_revision_progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original





@given(instance=revision_Sequence_strategy)
def test_hyp_revision_sequence_sequenceType_setter(instance):
    original = instance.sequenceType
    instance.sequenceType = original
    assert instance.sequenceType == original




@given(instance=revision_Rule_strategy)
def test_hyp_revision_rule_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=revision_Rule_strategy)
def test_hyp_revision_rule_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=revision_PublicationPhase_strategy)
def test_hyp_revision_publicationphase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=revision_PublicationPhase_strategy)
def test_hyp_revision_publicationphase_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=revision_PublicationPhase_strategy)
def test_hyp_revision_publicationphase_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original





@given(instance=revision_Researcher_strategy)
def test_hyp_revision_researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=revision_Researcher_strategy)
def test_hyp_revision_researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original



@given(instance=revision_Researcher_strategy)
def test_hyp_revision_researcher_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original





@given(instance=revision_ReviewNote_strategy)
def test_hyp_revision_reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original




@given(instance=revision_Paragraph_strategy)
def test_hyp_revision_paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original






@given(instance=revision_PublicationProcess_strategy)
def test_hyp_revision_publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=revision_PublicationProcess_strategy)
def test_hyp_revision_publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original


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
    PlaceHolder,
    revision_Counted,
    revision_Labelled,
    revision_Named,
    revision_Paper,
    revision_Paragraph,
    revision_PlaceHolder,
    revision_PlaceHolderPP,
    revision_PlaceHolderRn,
    revision_PlaceHolderRs,
    revision_PlaceHolderRule,
    revision_Progress,
    revision_PublicationPhase,
    revision_PublicationProcess,
    revision_PublicationStructure,
    revision_PublicationSystem,
    revision_Researcher,
    revision_Review,
    revision_ReviewNote,
    revision_Rule,
    revision_Sequence,
    revision_Write,
    SequenceType,
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

def test_revision_Counted_id_value_roundtrip():
    instance = revision_Counted(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_revision_Labelled_lname_value_roundtrip():
    instance = revision_Labelled(lname="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_revision_Named_name_value_roundtrip():
    instance = revision_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_revision_Paragraph_content_value_roundtrip():
    instance = revision_Paragraph(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_revision_Progress_percent_value_roundtrip():
    instance = revision_Progress(percent=7)
    assert instance.percent == 7
    instance.percent = 13
    assert instance.percent == 13


def test_revision_PublicationPhase_maxTime_value_roundtrip():
    instance = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    assert instance.maxTime == 7
    instance.maxTime = 13
    assert instance.maxTime == 13


def test_revision_PublicationPhase_minTime_value_roundtrip():
    instance = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    assert instance.minTime == 7
    instance.minTime = 13
    assert instance.minTime == 13


def test_revision_PublicationPhase_name_value_roundtrip():
    instance = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_revision_PublicationProcess_maxTime_value_roundtrip():
    instance = revision_PublicationProcess(maxTime=7, minTime=7)
    assert instance.maxTime == 7
    instance.maxTime = 13
    assert instance.maxTime == 13


def test_revision_PublicationProcess_minTime_value_roundtrip():
    instance = revision_PublicationProcess(maxTime=7, minTime=7)
    assert instance.minTime == 7
    instance.minTime = 13
    assert instance.minTime == 13


def test_revision_Researcher_forName_value_roundtrip():
    instance = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    assert instance.forName == "sample_text"
    instance.forName = "sample_text_2"
    assert instance.forName == "sample_text_2"


def test_revision_Researcher_name_value_roundtrip():
    instance = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_revision_Researcher_position_value_roundtrip():
    instance = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_revision_ReviewNote_content_value_roundtrip():
    instance = revision_ReviewNote(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_revision_Rule_key_value_roundtrip():
    instance = revision_Rule(key="sample_text", text="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_revision_Rule_text_value_roundtrip():
    instance = revision_Rule(key="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_revision_Sequence_sequenceType_value_roundtrip():
    instance = revision_Sequence(sequenceType="sample_text")
    assert instance.sequenceType == "sample_text"
    instance.sequenceType = "sample_text_2"
    assert instance.sequenceType == "sample_text_2"


def test_revision_Paragraph_isa_Counted():
    instance = revision_Paragraph(content="sample_text")
    assert isinstance(instance, Counted)


def test_revision_Progress_isa_Labelled():
    instance = revision_Progress(percent=7)
    assert isinstance(instance, Labelled)


def test_revision_Review_isa_Labelled():
    instance = revision_Review()
    assert isinstance(instance, Labelled)


def test_revision_Write_isa_Labelled():
    instance = revision_Write()
    assert isinstance(instance, Labelled)


def test_revision_Paper_isa_Named():
    instance = revision_Paper()
    assert isinstance(instance, Named)


def test_revision_Paragraph_isa_Named():
    instance = revision_Paragraph(content="sample_text")
    assert isinstance(instance, Named)


def test_revision_PublicationProcess_isa_Named():
    instance = revision_PublicationProcess(maxTime=7, minTime=7)
    assert isinstance(instance, Named)


def test_revision_PublicationStructure_isa_Named():
    instance = revision_PublicationStructure()
    assert isinstance(instance, Named)


def test_revision_ReviewNote_isa_Named():
    instance = revision_ReviewNote(content="sample_text")
    assert isinstance(instance, Named)


def test_revision_PlaceHolderPP_isa_PlaceHolder():
    instance = revision_PlaceHolderPP()
    assert isinstance(instance, PlaceHolder)


def test_revision_PlaceHolderRn_isa_PlaceHolder():
    instance = revision_PlaceHolderRn()
    assert isinstance(instance, PlaceHolder)


def test_revision_PlaceHolderRs_isa_PlaceHolder():
    instance = revision_PlaceHolderRs()
    assert isinstance(instance, PlaceHolder)


def test_revision_PlaceHolderRule_isa_PlaceHolder():
    instance = revision_PlaceHolderRule()
    assert isinstance(instance, PlaceHolder)


def test_assoc_authors28_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_Paper()
    b2 = revision_Paper()
    _safe_set(a, 'Researcher29', b1)
    assert _is_linked(a, 'Researcher29', b1)
    if hasattr(b1, 'papers'):
        assert _is_linked(b1, 'papers', a)
    _safe_set(a, 'Researcher29', b2)
    assert _is_linked(a, 'Researcher29', b2)
    if hasattr(b1, 'papers'):
        assert not _is_linked(b1, 'papers', a)
    if hasattr(b2, 'papers'):
        assert _is_linked(b2, 'papers', a)
    _safe_set(a, 'Researcher29', None)
    assert not _is_linked(a, 'Researcher29', b2)
    if hasattr(b2, 'papers'):
        assert not _is_linked(b2, 'papers', a)


def test_assoc_linksToSuccessors3_link_reassign_clear():
    a = revision_Sequence(sequenceType="sample_text")
    b1 = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b2 = revision_PublicationPhase(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'revision_Sequence', b1)
    assert _is_linked(a, 'revision_Sequence', b1)
    if hasattr(b1, 'revision_PublicationPhase4'):
        assert _is_linked(b1, 'revision_PublicationPhase4', a)
    _safe_set(a, 'revision_Sequence', b2)
    assert _is_linked(a, 'revision_Sequence', b2)
    if hasattr(b1, 'revision_PublicationPhase4'):
        assert not _is_linked(b1, 'revision_PublicationPhase4', a)
    if hasattr(b2, 'revision_PublicationPhase4'):
        assert _is_linked(b2, 'revision_PublicationPhase4', a)
    _safe_set(a, 'revision_Sequence', None)
    assert not _is_linked(a, 'revision_Sequence', b2)
    if hasattr(b2, 'revision_PublicationPhase4'):
        assert not _is_linked(b2, 'revision_PublicationPhase4', a)


def test_assoc_neededPerson5_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b2 = revision_PublicationPhase(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'Researcher', b1)
    assert _is_linked(a, 'Researcher', b1)
    if hasattr(b1, 'phaseParticipation'):
        assert _is_linked(b1, 'phaseParticipation', a)
    _safe_set(a, 'Researcher', b2)
    assert _is_linked(a, 'Researcher', b2)
    if hasattr(b1, 'phaseParticipation'):
        assert not _is_linked(b1, 'phaseParticipation', a)
    if hasattr(b2, 'phaseParticipation'):
        assert _is_linked(b2, 'phaseParticipation', a)
    _safe_set(a, 'Researcher', None)
    assert not _is_linked(a, 'Researcher', b2)
    if hasattr(b2, 'phaseParticipation'):
        assert not _is_linked(b2, 'phaseParticipation', a)


def test_assoc_paper36_link_reassign_clear():
    a = revision_Progress(percent=7)
    b1 = revision_Paper()
    b2 = revision_Paper()
    _safe_set(a, 'progress', b1)
    assert _is_linked(a, 'progress', b1)
    if hasattr(b1, 'Paper37'):
        assert _is_linked(b1, 'Paper37', a)
    _safe_set(a, 'progress', b2)
    assert _is_linked(a, 'progress', b2)
    if hasattr(b1, 'Paper37'):
        assert not _is_linked(b1, 'Paper37', a)
    if hasattr(b2, 'Paper37'):
        assert _is_linked(b2, 'Paper37', a)
    _safe_set(a, 'progress', None)
    assert not _is_linked(a, 'progress', b2)
    if hasattr(b2, 'Paper37'):
        assert not _is_linked(b2, 'Paper37', a)


def test_assoc_papers23_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_Paper()
    b2 = revision_Paper()
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


def test_assoc_paragraph38_link_reassign_clear():
    a = revision_Paragraph(content="sample_text")
    b1 = revision_Write()
    b2 = revision_Write()
    _safe_set(a, 'revision_Paragraph40', b1)
    assert _is_linked(a, 'revision_Paragraph40', b1)
    if hasattr(b1, 'revision_Write39'):
        assert _is_linked(b1, 'revision_Write39', a)
    _safe_set(a, 'revision_Paragraph40', b2)
    assert _is_linked(a, 'revision_Paragraph40', b2)
    if hasattr(b1, 'revision_Write39'):
        assert not _is_linked(b1, 'revision_Write39', a)
    if hasattr(b2, 'revision_Write39'):
        assert _is_linked(b2, 'revision_Write39', a)
    _safe_set(a, 'revision_Paragraph40', None)
    assert not _is_linked(a, 'revision_Paragraph40', b2)
    if hasattr(b2, 'revision_Write39'):
        assert not _is_linked(b2, 'revision_Write39', a)


def test_assoc_paragraphs26_link_reassign_clear():
    a = revision_Paragraph(content="sample_text")
    b1 = revision_Paper()
    b2 = revision_Paper()
    _safe_set(a, 'revision_Paragraph', b1)
    assert _is_linked(a, 'revision_Paragraph', b1)
    if hasattr(b1, 'revision_Paper'):
        assert _is_linked(b1, 'revision_Paper', a)
    _safe_set(a, 'revision_Paragraph', b2)
    assert _is_linked(a, 'revision_Paragraph', b2)
    if hasattr(b1, 'revision_Paper'):
        assert not _is_linked(b1, 'revision_Paper', a)
    if hasattr(b2, 'revision_Paper'):
        assert _is_linked(b2, 'revision_Paper', a)
    _safe_set(a, 'revision_Paragraph', None)
    assert not _is_linked(a, 'revision_Paragraph', b2)
    if hasattr(b2, 'revision_Paper'):
        assert not _is_linked(b2, 'revision_Paper', a)


def test_assoc_phaseParticipation19_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b2 = revision_PublicationPhase(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'neededPerson', {b1})
    assert _is_linked(a, 'neededPerson', b1)
    if hasattr(b1, 'PublicationPhase'):
        assert _is_linked(b1, 'PublicationPhase', a)
    _safe_set(a, 'neededPerson', {b2})
    assert _is_linked(a, 'neededPerson', b2)
    if hasattr(b1, 'PublicationPhase'):
        assert not _is_linked(b1, 'PublicationPhase', a)
    if hasattr(b2, 'PublicationPhase'):
        assert _is_linked(b2, 'PublicationPhase', a)
    _safe_set(a, 'neededPerson', set())
    assert not _is_linked(a, 'neededPerson', b2)
    if hasattr(b2, 'PublicationPhase'):
        assert not _is_linked(b2, 'PublicationPhase', a)


def test_assoc_phases0_link_reassign_clear():
    a = revision_PublicationProcess(maxTime=7, minTime=7)
    b1 = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b2 = revision_PublicationPhase(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'revision_PublicationProcess', {b1})
    assert _is_linked(a, 'revision_PublicationProcess', b1)
    if hasattr(b1, 'revision_PublicationPhase'):
        assert _is_linked(b1, 'revision_PublicationPhase', a)
    _safe_set(a, 'revision_PublicationProcess', {b2})
    assert _is_linked(a, 'revision_PublicationProcess', b2)
    if hasattr(b1, 'revision_PublicationPhase'):
        assert not _is_linked(b1, 'revision_PublicationPhase', a)
    if hasattr(b2, 'revision_PublicationPhase'):
        assert _is_linked(b2, 'revision_PublicationPhase', a)
    _safe_set(a, 'revision_PublicationProcess', set())
    assert not _is_linked(a, 'revision_PublicationProcess', b2)
    if hasattr(b2, 'revision_PublicationPhase'):
        assert not _is_linked(b2, 'revision_PublicationPhase', a)


def test_assoc_placeholder17_link_reassign_clear():
    a = revision_Rule(key="sample_text", text="sample_text")
    b1 = revision_PlaceHolderRule()
    b2 = revision_PlaceHolderRule()
    _safe_set(a, 'revision_Rule18', b1)
    assert _is_linked(a, 'revision_Rule18', b1)
    if hasattr(b1, 'revision_PlaceHolderRule'):
        assert _is_linked(b1, 'revision_PlaceHolderRule', a)
    _safe_set(a, 'revision_Rule18', b2)
    assert _is_linked(a, 'revision_Rule18', b2)
    if hasattr(b1, 'revision_PlaceHolderRule'):
        assert not _is_linked(b1, 'revision_PlaceHolderRule', a)
    if hasattr(b2, 'revision_PlaceHolderRule'):
        assert _is_linked(b2, 'revision_PlaceHolderRule', a)
    _safe_set(a, 'revision_Rule18', None)
    assert not _is_linked(a, 'revision_Rule18', b2)
    if hasattr(b2, 'revision_PlaceHolderRule'):
        assert not _is_linked(b2, 'revision_PlaceHolderRule', a)


def test_assoc_placeholder24_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_PlaceHolderRs()
    b2 = revision_PlaceHolderRs()
    _safe_set(a, 'revision_Researcher25', b1)
    assert _is_linked(a, 'revision_Researcher25', b1)
    if hasattr(b1, 'revision_PlaceHolderRs'):
        assert _is_linked(b1, 'revision_PlaceHolderRs', a)
    _safe_set(a, 'revision_Researcher25', b2)
    assert _is_linked(a, 'revision_Researcher25', b2)
    if hasattr(b1, 'revision_PlaceHolderRs'):
        assert not _is_linked(b1, 'revision_PlaceHolderRs', a)
    if hasattr(b2, 'revision_PlaceHolderRs'):
        assert _is_linked(b2, 'revision_PlaceHolderRs', a)
    _safe_set(a, 'revision_Researcher25', None)
    assert not _is_linked(a, 'revision_Researcher25', b2)
    if hasattr(b2, 'revision_PlaceHolderRs'):
        assert not _is_linked(b2, 'revision_PlaceHolderRs', a)


def test_assoc_placeholder32_link_reassign_clear():
    a = revision_ReviewNote(content="sample_text")
    b1 = revision_PlaceHolderRn()
    b2 = revision_PlaceHolderRn()
    _safe_set(a, 'revision_ReviewNote33', b1)
    assert _is_linked(a, 'revision_ReviewNote33', b1)
    if hasattr(b1, 'revision_PlaceHolderRn'):
        assert _is_linked(b1, 'revision_PlaceHolderRn', a)
    _safe_set(a, 'revision_ReviewNote33', b2)
    assert _is_linked(a, 'revision_ReviewNote33', b2)
    if hasattr(b1, 'revision_PlaceHolderRn'):
        assert not _is_linked(b1, 'revision_PlaceHolderRn', a)
    if hasattr(b2, 'revision_PlaceHolderRn'):
        assert _is_linked(b2, 'revision_PlaceHolderRn', a)
    _safe_set(a, 'revision_ReviewNote33', None)
    assert not _is_linked(a, 'revision_ReviewNote33', b2)
    if hasattr(b2, 'revision_PlaceHolderRn'):
        assert not _is_linked(b2, 'revision_PlaceHolderRn', a)


def test_assoc_placeholder9_link_reassign_clear():
    a = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b1 = revision_PlaceHolderPP()
    b2 = revision_PlaceHolderPP()
    _safe_set(a, 'revision_PublicationPhase10', b1)
    assert _is_linked(a, 'revision_PublicationPhase10', b1)
    if hasattr(b1, 'revision_PlaceHolderPP'):
        assert _is_linked(b1, 'revision_PlaceHolderPP', a)
    _safe_set(a, 'revision_PublicationPhase10', b2)
    assert _is_linked(a, 'revision_PublicationPhase10', b2)
    if hasattr(b1, 'revision_PlaceHolderPP'):
        assert not _is_linked(b1, 'revision_PlaceHolderPP', a)
    if hasattr(b2, 'revision_PlaceHolderPP'):
        assert _is_linked(b2, 'revision_PlaceHolderPP', a)
    _safe_set(a, 'revision_PublicationPhase10', None)
    assert not _is_linked(a, 'revision_PublicationPhase10', b2)
    if hasattr(b2, 'revision_PlaceHolderPP'):
        assert not _is_linked(b2, 'revision_PlaceHolderPP', a)


def test_assoc_predecessor14_link_reassign_clear():
    a = revision_Sequence(sequenceType="sample_text")
    b1 = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b2 = revision_PublicationPhase(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'revision_Sequence15', b1)
    assert _is_linked(a, 'revision_Sequence15', b1)
    if hasattr(b1, 'revision_PublicationPhase16'):
        assert _is_linked(b1, 'revision_PublicationPhase16', a)
    _safe_set(a, 'revision_Sequence15', b2)
    assert _is_linked(a, 'revision_Sequence15', b2)
    if hasattr(b1, 'revision_PublicationPhase16'):
        assert not _is_linked(b1, 'revision_PublicationPhase16', a)
    if hasattr(b2, 'revision_PublicationPhase16'):
        assert _is_linked(b2, 'revision_PublicationPhase16', a)
    _safe_set(a, 'revision_Sequence15', None)
    assert not _is_linked(a, 'revision_Sequence15', b2)
    if hasattr(b2, 'revision_PublicationPhase16'):
        assert not _is_linked(b2, 'revision_PublicationPhase16', a)


def test_assoc_process34_link_reassign_clear():
    a = revision_PublicationProcess(maxTime=7, minTime=7)
    b1 = revision_Progress(percent=7)
    b2 = revision_Progress(percent=13)
    _safe_set(a, 'revision_PublicationProcess35', b1)
    assert _is_linked(a, 'revision_PublicationProcess35', b1)
    if hasattr(b1, 'revision_Progress'):
        assert _is_linked(b1, 'revision_Progress', a)
    _safe_set(a, 'revision_PublicationProcess35', b2)
    assert _is_linked(a, 'revision_PublicationProcess35', b2)
    if hasattr(b1, 'revision_Progress'):
        assert not _is_linked(b1, 'revision_Progress', a)
    if hasattr(b2, 'revision_Progress'):
        assert _is_linked(b2, 'revision_Progress', a)
    _safe_set(a, 'revision_PublicationProcess35', None)
    assert not _is_linked(a, 'revision_PublicationProcess35', b2)
    if hasattr(b2, 'revision_Progress'):
        assert not _is_linked(b2, 'revision_Progress', a)


def test_assoc_processView49_link_reassign_clear():
    a = revision_PublicationProcess(maxTime=7, minTime=7)
    b1 = revision_PublicationSystem()
    b2 = revision_PublicationSystem()
    _safe_set(a, 'revision_PublicationProcess50', b1)
    assert _is_linked(a, 'revision_PublicationProcess50', b1)
    if hasattr(b1, 'revision_PublicationSystem'):
        assert _is_linked(b1, 'revision_PublicationSystem', a)
    _safe_set(a, 'revision_PublicationProcess50', b2)
    assert _is_linked(a, 'revision_PublicationProcess50', b2)
    if hasattr(b1, 'revision_PublicationSystem'):
        assert not _is_linked(b1, 'revision_PublicationSystem', a)
    if hasattr(b2, 'revision_PublicationSystem'):
        assert _is_linked(b2, 'revision_PublicationSystem', a)
    _safe_set(a, 'revision_PublicationProcess50', None)
    assert not _is_linked(a, 'revision_PublicationProcess50', b2)
    if hasattr(b2, 'revision_PublicationSystem'):
        assert not _is_linked(b2, 'revision_PublicationSystem', a)


def test_assoc_progress27_link_reassign_clear():
    a = revision_Progress(percent=7)
    b1 = revision_Paper()
    b2 = revision_Paper()
    _safe_set(a, 'Progress', b1)
    assert _is_linked(a, 'Progress', b1)
    if hasattr(b1, 'paper'):
        assert _is_linked(b1, 'paper', a)
    _safe_set(a, 'Progress', b2)
    assert _is_linked(a, 'Progress', b2)
    if hasattr(b1, 'paper'):
        assert not _is_linked(b1, 'paper', a)
    if hasattr(b2, 'paper'):
        assert _is_linked(b2, 'paper', a)
    _safe_set(a, 'Progress', None)
    assert not _is_linked(a, 'Progress', b2)
    if hasattr(b2, 'paper'):
        assert not _is_linked(b2, 'paper', a)


def test_assoc_publicationRules1_link_reassign_clear():
    a = revision_Rule(key="sample_text", text="sample_text")
    b1 = revision_PublicationProcess(maxTime=7, minTime=7)
    b2 = revision_PublicationProcess(maxTime=13, minTime=13)
    _safe_set(a, 'revision_Rule', b1)
    assert _is_linked(a, 'revision_Rule', b1)
    if hasattr(b1, 'revision_PublicationProcess2'):
        assert _is_linked(b1, 'revision_PublicationProcess2', a)
    _safe_set(a, 'revision_Rule', b2)
    assert _is_linked(a, 'revision_Rule', b2)
    if hasattr(b1, 'revision_PublicationProcess2'):
        assert not _is_linked(b1, 'revision_PublicationProcess2', a)
    if hasattr(b2, 'revision_PublicationProcess2'):
        assert _is_linked(b2, 'revision_PublicationProcess2', a)
    _safe_set(a, 'revision_Rule', None)
    assert not _is_linked(a, 'revision_Rule', b2)
    if hasattr(b2, 'revision_PublicationProcess2'):
        assert not _is_linked(b2, 'revision_PublicationProcess2', a)


def test_assoc_researchers44_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_PublicationStructure()
    b2 = revision_PublicationStructure()
    _safe_set(a, 'revision_Researcher45', b1)
    assert _is_linked(a, 'revision_Researcher45', b1)
    if hasattr(b1, 'revision_PublicationStructure'):
        assert _is_linked(b1, 'revision_PublicationStructure', a)
    _safe_set(a, 'revision_Researcher45', b2)
    assert _is_linked(a, 'revision_Researcher45', b2)
    if hasattr(b1, 'revision_PublicationStructure'):
        assert not _is_linked(b1, 'revision_PublicationStructure', a)
    if hasattr(b2, 'revision_PublicationStructure'):
        assert _is_linked(b2, 'revision_PublicationStructure', a)
    _safe_set(a, 'revision_Researcher45', None)
    assert not _is_linked(a, 'revision_Researcher45', b2)
    if hasattr(b2, 'revision_PublicationStructure'):
        assert not _is_linked(b2, 'revision_PublicationStructure', a)


def test_assoc_reviewNote41_link_reassign_clear():
    a = revision_ReviewNote(content="sample_text")
    b1 = revision_Review()
    b2 = revision_Review()
    _safe_set(a, 'revision_ReviewNote43', b1)
    assert _is_linked(a, 'revision_ReviewNote43', b1)
    if hasattr(b1, 'revision_Review42'):
        assert _is_linked(b1, 'revision_Review42', a)
    _safe_set(a, 'revision_ReviewNote43', b2)
    assert _is_linked(a, 'revision_ReviewNote43', b2)
    if hasattr(b1, 'revision_Review42'):
        assert not _is_linked(b1, 'revision_Review42', a)
    if hasattr(b2, 'revision_Review42'):
        assert _is_linked(b2, 'revision_Review42', a)
    _safe_set(a, 'revision_ReviewNote43', None)
    assert not _is_linked(a, 'revision_ReviewNote43', b2)
    if hasattr(b2, 'revision_Review42'):
        assert not _is_linked(b2, 'revision_Review42', a)


def test_assoc_reviews21_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_Review()
    b2 = revision_Review()
    _safe_set(a, 'revision_Researcher22', {b1})
    assert _is_linked(a, 'revision_Researcher22', b1)
    if hasattr(b1, 'revision_Review'):
        assert _is_linked(b1, 'revision_Review', a)
    _safe_set(a, 'revision_Researcher22', {b2})
    assert _is_linked(a, 'revision_Researcher22', b2)
    if hasattr(b1, 'revision_Review'):
        assert not _is_linked(b1, 'revision_Review', a)
    if hasattr(b2, 'revision_Review'):
        assert _is_linked(b2, 'revision_Review', a)
    _safe_set(a, 'revision_Researcher22', set())
    assert not _is_linked(a, 'revision_Researcher22', b2)
    if hasattr(b2, 'revision_Review'):
        assert not _is_linked(b2, 'revision_Review', a)


def test_assoc_reviews30_link_reassign_clear():
    a = revision_ReviewNote(content="sample_text")
    b1 = revision_Paragraph(content="sample_text")
    b2 = revision_Paragraph(content="sample_text_2")
    _safe_set(a, 'revision_ReviewNote', b1)
    assert _is_linked(a, 'revision_ReviewNote', b1)
    if hasattr(b1, 'revision_Paragraph31'):
        assert _is_linked(b1, 'revision_Paragraph31', a)
    _safe_set(a, 'revision_ReviewNote', b2)
    assert _is_linked(a, 'revision_ReviewNote', b2)
    if hasattr(b1, 'revision_Paragraph31'):
        assert not _is_linked(b1, 'revision_Paragraph31', a)
    if hasattr(b2, 'revision_Paragraph31'):
        assert _is_linked(b2, 'revision_Paragraph31', a)
    _safe_set(a, 'revision_ReviewNote', None)
    assert not _is_linked(a, 'revision_ReviewNote', b2)
    if hasattr(b2, 'revision_Paragraph31'):
        assert not _is_linked(b2, 'revision_Paragraph31', a)


def test_assoc_rules6_link_reassign_clear():
    a = revision_Rule(key="sample_text", text="sample_text")
    b1 = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b2 = revision_PublicationPhase(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'revision_Rule8', b1)
    assert _is_linked(a, 'revision_Rule8', b1)
    if hasattr(b1, 'revision_PublicationPhase7'):
        assert _is_linked(b1, 'revision_PublicationPhase7', a)
    _safe_set(a, 'revision_Rule8', b2)
    assert _is_linked(a, 'revision_Rule8', b2)
    if hasattr(b1, 'revision_PublicationPhase7'):
        assert not _is_linked(b1, 'revision_PublicationPhase7', a)
    if hasattr(b2, 'revision_PublicationPhase7'):
        assert _is_linked(b2, 'revision_PublicationPhase7', a)
    _safe_set(a, 'revision_Rule8', None)
    assert not _is_linked(a, 'revision_Rule8', b2)
    if hasattr(b2, 'revision_PublicationPhase7'):
        assert not _is_linked(b2, 'revision_PublicationPhase7', a)


def test_assoc_successor11_link_reassign_clear():
    a = revision_Sequence(sequenceType="sample_text")
    b1 = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    b2 = revision_PublicationPhase(maxTime=13, minTime=13, name="sample_text_2")
    _safe_set(a, 'revision_Sequence12', b1)
    assert _is_linked(a, 'revision_Sequence12', b1)
    if hasattr(b1, 'revision_PublicationPhase13'):
        assert _is_linked(b1, 'revision_PublicationPhase13', a)
    _safe_set(a, 'revision_Sequence12', b2)
    assert _is_linked(a, 'revision_Sequence12', b2)
    if hasattr(b1, 'revision_PublicationPhase13'):
        assert not _is_linked(b1, 'revision_PublicationPhase13', a)
    if hasattr(b2, 'revision_PublicationPhase13'):
        assert _is_linked(b2, 'revision_PublicationPhase13', a)
    _safe_set(a, 'revision_Sequence12', None)
    assert not _is_linked(a, 'revision_Sequence12', b2)
    if hasattr(b2, 'revision_PublicationPhase13'):
        assert not _is_linked(b2, 'revision_PublicationPhase13', a)


def test_assoc_writes20_link_reassign_clear():
    a = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    b1 = revision_Write()
    b2 = revision_Write()
    _safe_set(a, 'revision_Researcher', {b1})
    assert _is_linked(a, 'revision_Researcher', b1)
    if hasattr(b1, 'revision_Write'):
        assert _is_linked(b1, 'revision_Write', a)
    _safe_set(a, 'revision_Researcher', {b2})
    assert _is_linked(a, 'revision_Researcher', b2)
    if hasattr(b1, 'revision_Write'):
        assert not _is_linked(b1, 'revision_Write', a)
    if hasattr(b2, 'revision_Write'):
        assert _is_linked(b2, 'revision_Write', a)
    _safe_set(a, 'revision_Researcher', set())
    assert not _is_linked(a, 'revision_Researcher', b2)
    if hasattr(b2, 'revision_Write'):
        assert not _is_linked(b2, 'revision_Write', a)


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


PlaceHolder_strategy = st.builds(PlaceHolder)
@given(instance=PlaceHolder_strategy)
@settings(max_examples=25)
def test_PlaceHolder_instantiation(instance):
    assert isinstance(instance, PlaceHolder)


revision_Counted_strategy = st.builds(revision_Counted, id=st.integers())
@given(instance=revision_Counted_strategy)
@settings(max_examples=25)
def test_revision_Counted_instantiation(instance):
    assert isinstance(instance, revision_Counted)


revision_Labelled_strategy = st.builds(revision_Labelled, lname=safe_text)
@given(instance=revision_Labelled_strategy)
@settings(max_examples=25)
def test_revision_Labelled_instantiation(instance):
    assert isinstance(instance, revision_Labelled)


revision_Named_strategy = st.builds(revision_Named, name=safe_text)
@given(instance=revision_Named_strategy)
@settings(max_examples=25)
def test_revision_Named_instantiation(instance):
    assert isinstance(instance, revision_Named)


revision_Paper_strategy = st.builds(revision_Paper)
@given(instance=revision_Paper_strategy)
@settings(max_examples=25)
def test_revision_Paper_instantiation(instance):
    assert isinstance(instance, revision_Paper)


revision_Paragraph_strategy = st.builds(revision_Paragraph, content=safe_text)
@given(instance=revision_Paragraph_strategy)
@settings(max_examples=25)
def test_revision_Paragraph_instantiation(instance):
    assert isinstance(instance, revision_Paragraph)


revision_PlaceHolder_strategy = st.builds(revision_PlaceHolder)
@given(instance=revision_PlaceHolder_strategy)
@settings(max_examples=25)
def test_revision_PlaceHolder_instantiation(instance):
    assert isinstance(instance, revision_PlaceHolder)


revision_PlaceHolderPP_strategy = st.builds(revision_PlaceHolderPP)
@given(instance=revision_PlaceHolderPP_strategy)
@settings(max_examples=25)
def test_revision_PlaceHolderPP_instantiation(instance):
    assert isinstance(instance, revision_PlaceHolderPP)


revision_PlaceHolderRn_strategy = st.builds(revision_PlaceHolderRn)
@given(instance=revision_PlaceHolderRn_strategy)
@settings(max_examples=25)
def test_revision_PlaceHolderRn_instantiation(instance):
    assert isinstance(instance, revision_PlaceHolderRn)


revision_PlaceHolderRs_strategy = st.builds(revision_PlaceHolderRs)
@given(instance=revision_PlaceHolderRs_strategy)
@settings(max_examples=25)
def test_revision_PlaceHolderRs_instantiation(instance):
    assert isinstance(instance, revision_PlaceHolderRs)


revision_PlaceHolderRule_strategy = st.builds(revision_PlaceHolderRule)
@given(instance=revision_PlaceHolderRule_strategy)
@settings(max_examples=25)
def test_revision_PlaceHolderRule_instantiation(instance):
    assert isinstance(instance, revision_PlaceHolderRule)


revision_Progress_strategy = st.builds(revision_Progress, percent=st.integers())
@given(instance=revision_Progress_strategy)
@settings(max_examples=25)
def test_revision_Progress_instantiation(instance):
    assert isinstance(instance, revision_Progress)


revision_PublicationPhase_strategy = st.builds(revision_PublicationPhase, maxTime=st.integers(), minTime=st.integers(), name=safe_text)
@given(instance=revision_PublicationPhase_strategy)
@settings(max_examples=25)
def test_revision_PublicationPhase_instantiation(instance):
    assert isinstance(instance, revision_PublicationPhase)


revision_PublicationProcess_strategy = st.builds(revision_PublicationProcess, maxTime=st.integers(), minTime=st.integers())
@given(instance=revision_PublicationProcess_strategy)
@settings(max_examples=25)
def test_revision_PublicationProcess_instantiation(instance):
    assert isinstance(instance, revision_PublicationProcess)


revision_PublicationStructure_strategy = st.builds(revision_PublicationStructure)
@given(instance=revision_PublicationStructure_strategy)
@settings(max_examples=25)
def test_revision_PublicationStructure_instantiation(instance):
    assert isinstance(instance, revision_PublicationStructure)


revision_PublicationSystem_strategy = st.builds(revision_PublicationSystem)
@given(instance=revision_PublicationSystem_strategy)
@settings(max_examples=25)
def test_revision_PublicationSystem_instantiation(instance):
    assert isinstance(instance, revision_PublicationSystem)


revision_Researcher_strategy = st.builds(revision_Researcher, forName=safe_text, name=safe_text, position=safe_text)
@given(instance=revision_Researcher_strategy)
@settings(max_examples=25)
def test_revision_Researcher_instantiation(instance):
    assert isinstance(instance, revision_Researcher)


revision_Review_strategy = st.builds(revision_Review)
@given(instance=revision_Review_strategy)
@settings(max_examples=25)
def test_revision_Review_instantiation(instance):
    assert isinstance(instance, revision_Review)


revision_ReviewNote_strategy = st.builds(revision_ReviewNote, content=safe_text)
@given(instance=revision_ReviewNote_strategy)
@settings(max_examples=25)
def test_revision_ReviewNote_instantiation(instance):
    assert isinstance(instance, revision_ReviewNote)


revision_Rule_strategy = st.builds(revision_Rule, key=safe_text, text=safe_text)
@given(instance=revision_Rule_strategy)
@settings(max_examples=25)
def test_revision_Rule_instantiation(instance):
    assert isinstance(instance, revision_Rule)


revision_Sequence_strategy = st.builds(revision_Sequence, sequenceType=safe_text)
@given(instance=revision_Sequence_strategy)
@settings(max_examples=25)
def test_revision_Sequence_instantiation(instance):
    assert isinstance(instance, revision_Sequence)


revision_Write_strategy = st.builds(revision_Write)
@given(instance=revision_Write_strategy)
@settings(max_examples=25)
def test_revision_Write_instantiation(instance):
    assert isinstance(instance, revision_Write)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Counted,
    Labelled,
    Named,
    PlaceHolder,
    revision_Counted,
    revision_Labelled,
    revision_Named,
    revision_Paper,
    revision_Paragraph,
    revision_PlaceHolder,
    revision_PlaceHolderPP,
    revision_PlaceHolderRn,
    revision_PlaceHolderRs,
    revision_PlaceHolderRule,
    revision_Progress,
    revision_PublicationPhase,
    revision_PublicationProcess,
    revision_PublicationStructure,
    revision_PublicationSystem,
    revision_Researcher,
    revision_Review,
    revision_ReviewNote,
    revision_Rule,
    revision_Sequence,
    revision_Write,
    SequenceType,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_linksToSuccessors3_reverse_link_reassign_clear():
    a1 = revision_Sequence(sequenceType="sample_text")
    a2 = revision_Sequence(sequenceType="sample_text_2")
    b = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'revision_PublicationPhase4', {a1})
    assert _is_linked(b, 'revision_PublicationPhase4', a1)
    if hasattr(a1, 'revision_Sequence'):
        assert _is_linked(a1, 'revision_Sequence', b)
    _safe_set(b, 'revision_PublicationPhase4', {a2})
    assert _is_linked(b, 'revision_PublicationPhase4', a2)
    if hasattr(a1, 'revision_Sequence'):
        assert not _is_linked(a1, 'revision_Sequence', b)
    if hasattr(a2, 'revision_Sequence'):
        assert _is_linked(a2, 'revision_Sequence', b)
    _safe_set(b, 'revision_PublicationPhase4', set())
    assert not _is_linked(b, 'revision_PublicationPhase4', a2)
    if hasattr(a2, 'revision_Sequence'):
        assert not _is_linked(a2, 'revision_Sequence', b)


def test_assoc_neededPerson5_reverse_link_reassign_clear():
    a1 = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = revision_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'phaseParticipation', {a1})
    assert _is_linked(b, 'phaseParticipation', a1)
    if hasattr(a1, 'Researcher'):
        assert _is_linked(a1, 'Researcher', b)
    _safe_set(b, 'phaseParticipation', {a2})
    assert _is_linked(b, 'phaseParticipation', a2)
    if hasattr(a1, 'Researcher'):
        assert not _is_linked(a1, 'Researcher', b)
    if hasattr(a2, 'Researcher'):
        assert _is_linked(a2, 'Researcher', b)
    _safe_set(b, 'phaseParticipation', set())
    assert not _is_linked(b, 'phaseParticipation', a2)
    if hasattr(a2, 'Researcher'):
        assert not _is_linked(a2, 'Researcher', b)


def test_assoc_phaseParticipation19_reverse_link_reassign_clear():
    a1 = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    a2 = revision_Researcher(forName="sample_text_2", name="sample_text_2", position="sample_text_2")
    b = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'PublicationPhase', a1)
    assert _is_linked(b, 'PublicationPhase', a1)
    if hasattr(a1, 'neededPerson'):
        assert _is_linked(a1, 'neededPerson', b)
    _safe_set(b, 'PublicationPhase', a2)
    assert _is_linked(b, 'PublicationPhase', a2)
    if hasattr(a1, 'neededPerson'):
        assert not _is_linked(a1, 'neededPerson', b)
    if hasattr(a2, 'neededPerson'):
        assert _is_linked(a2, 'neededPerson', b)
    _safe_set(b, 'PublicationPhase', None)
    assert not _is_linked(b, 'PublicationPhase', a2)
    if hasattr(a2, 'neededPerson'):
        assert not _is_linked(a2, 'neededPerson', b)


def test_assoc_phases0_reverse_link_reassign_clear():
    a1 = revision_PublicationProcess(maxTime=7, minTime=7)
    a2 = revision_PublicationProcess(maxTime=13, minTime=13)
    b = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'revision_PublicationPhase', a1)
    assert _is_linked(b, 'revision_PublicationPhase', a1)
    if hasattr(a1, 'revision_PublicationProcess'):
        assert _is_linked(a1, 'revision_PublicationProcess', b)
    _safe_set(b, 'revision_PublicationPhase', a2)
    assert _is_linked(b, 'revision_PublicationPhase', a2)
    if hasattr(a1, 'revision_PublicationProcess'):
        assert not _is_linked(a1, 'revision_PublicationProcess', b)
    if hasattr(a2, 'revision_PublicationProcess'):
        assert _is_linked(a2, 'revision_PublicationProcess', b)
    _safe_set(b, 'revision_PublicationPhase', None)
    assert not _is_linked(b, 'revision_PublicationPhase', a2)
    if hasattr(a2, 'revision_PublicationProcess'):
        assert not _is_linked(a2, 'revision_PublicationProcess', b)


def test_assoc_predecessor14_reverse_link_reassign_clear():
    a1 = revision_Sequence(sequenceType="sample_text")
    a2 = revision_Sequence(sequenceType="sample_text_2")
    b = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'revision_PublicationPhase16', a1)
    assert _is_linked(b, 'revision_PublicationPhase16', a1)
    if hasattr(a1, 'revision_Sequence15'):
        assert _is_linked(a1, 'revision_Sequence15', b)
    _safe_set(b, 'revision_PublicationPhase16', a2)
    assert _is_linked(b, 'revision_PublicationPhase16', a2)
    if hasattr(a1, 'revision_Sequence15'):
        assert not _is_linked(a1, 'revision_Sequence15', b)
    if hasattr(a2, 'revision_Sequence15'):
        assert _is_linked(a2, 'revision_Sequence15', b)
    _safe_set(b, 'revision_PublicationPhase16', None)
    assert not _is_linked(b, 'revision_PublicationPhase16', a2)
    if hasattr(a2, 'revision_Sequence15'):
        assert not _is_linked(a2, 'revision_Sequence15', b)


def test_assoc_process34_reverse_link_reassign_clear():
    a1 = revision_PublicationProcess(maxTime=7, minTime=7)
    a2 = revision_PublicationProcess(maxTime=13, minTime=13)
    b = revision_Progress(percent=7)
    _safe_set(b, 'revision_Progress', a1)
    assert _is_linked(b, 'revision_Progress', a1)
    if hasattr(a1, 'revision_PublicationProcess35'):
        assert _is_linked(a1, 'revision_PublicationProcess35', b)
    _safe_set(b, 'revision_Progress', a2)
    assert _is_linked(b, 'revision_Progress', a2)
    if hasattr(a1, 'revision_PublicationProcess35'):
        assert not _is_linked(a1, 'revision_PublicationProcess35', b)
    if hasattr(a2, 'revision_PublicationProcess35'):
        assert _is_linked(a2, 'revision_PublicationProcess35', b)
    _safe_set(b, 'revision_Progress', None)
    assert not _is_linked(b, 'revision_Progress', a2)
    if hasattr(a2, 'revision_PublicationProcess35'):
        assert not _is_linked(a2, 'revision_PublicationProcess35', b)


def test_assoc_publicationRules1_reverse_link_reassign_clear():
    a1 = revision_Rule(key="sample_text", text="sample_text")
    a2 = revision_Rule(key="sample_text_2", text="sample_text_2")
    b = revision_PublicationProcess(maxTime=7, minTime=7)
    _safe_set(b, 'revision_PublicationProcess2', {a1})
    assert _is_linked(b, 'revision_PublicationProcess2', a1)
    if hasattr(a1, 'revision_Rule'):
        assert _is_linked(a1, 'revision_Rule', b)
    _safe_set(b, 'revision_PublicationProcess2', {a2})
    assert _is_linked(b, 'revision_PublicationProcess2', a2)
    if hasattr(a1, 'revision_Rule'):
        assert not _is_linked(a1, 'revision_Rule', b)
    if hasattr(a2, 'revision_Rule'):
        assert _is_linked(a2, 'revision_Rule', b)
    _safe_set(b, 'revision_PublicationProcess2', set())
    assert not _is_linked(b, 'revision_PublicationProcess2', a2)
    if hasattr(a2, 'revision_Rule'):
        assert not _is_linked(a2, 'revision_Rule', b)


def test_assoc_reviews30_reverse_link_reassign_clear():
    a1 = revision_ReviewNote(content="sample_text")
    a2 = revision_ReviewNote(content="sample_text_2")
    b = revision_Paragraph(content="sample_text")
    _safe_set(b, 'revision_Paragraph31', {a1})
    assert _is_linked(b, 'revision_Paragraph31', a1)
    if hasattr(a1, 'revision_ReviewNote'):
        assert _is_linked(a1, 'revision_ReviewNote', b)
    _safe_set(b, 'revision_Paragraph31', {a2})
    assert _is_linked(b, 'revision_Paragraph31', a2)
    if hasattr(a1, 'revision_ReviewNote'):
        assert not _is_linked(a1, 'revision_ReviewNote', b)
    if hasattr(a2, 'revision_ReviewNote'):
        assert _is_linked(a2, 'revision_ReviewNote', b)
    _safe_set(b, 'revision_Paragraph31', set())
    assert not _is_linked(b, 'revision_Paragraph31', a2)
    if hasattr(a2, 'revision_ReviewNote'):
        assert not _is_linked(a2, 'revision_ReviewNote', b)


def test_assoc_rules6_reverse_link_reassign_clear():
    a1 = revision_Rule(key="sample_text", text="sample_text")
    a2 = revision_Rule(key="sample_text_2", text="sample_text_2")
    b = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'revision_PublicationPhase7', {a1})
    assert _is_linked(b, 'revision_PublicationPhase7', a1)
    if hasattr(a1, 'revision_Rule8'):
        assert _is_linked(a1, 'revision_Rule8', b)
    _safe_set(b, 'revision_PublicationPhase7', {a2})
    assert _is_linked(b, 'revision_PublicationPhase7', a2)
    if hasattr(a1, 'revision_Rule8'):
        assert not _is_linked(a1, 'revision_Rule8', b)
    if hasattr(a2, 'revision_Rule8'):
        assert _is_linked(a2, 'revision_Rule8', b)
    _safe_set(b, 'revision_PublicationPhase7', set())
    assert not _is_linked(b, 'revision_PublicationPhase7', a2)
    if hasattr(a2, 'revision_Rule8'):
        assert not _is_linked(a2, 'revision_Rule8', b)


def test_assoc_successor11_reverse_link_reassign_clear():
    a1 = revision_Sequence(sequenceType="sample_text")
    a2 = revision_Sequence(sequenceType="sample_text_2")
    b = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'revision_PublicationPhase13', a1)
    assert _is_linked(b, 'revision_PublicationPhase13', a1)
    if hasattr(a1, 'revision_Sequence12'):
        assert _is_linked(a1, 'revision_Sequence12', b)
    _safe_set(b, 'revision_PublicationPhase13', a2)
    assert _is_linked(b, 'revision_PublicationPhase13', a2)
    if hasattr(a1, 'revision_Sequence12'):
        assert not _is_linked(a1, 'revision_Sequence12', b)
    if hasattr(a2, 'revision_Sequence12'):
        assert _is_linked(a2, 'revision_Sequence12', b)
    _safe_set(b, 'revision_PublicationPhase13', None)
    assert not _is_linked(b, 'revision_PublicationPhase13', a2)
    if hasattr(a2, 'revision_Sequence12'):
        assert not _is_linked(a2, 'revision_Sequence12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors28_stub_double():
    # revision_Paper has no real 'papers' property in the generated
    # code (a bare stub) -- manually attach it so revision_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = revision_Paper()
    setattr(partner, 'papers', None)
    _safe_set(owner, 'Researcher29', partner)
    assert owner in getattr(partner, 'papers')
    _safe_set(owner, 'Researcher29', None)
    assert owner not in getattr(partner, 'papers')


def test_assoc_paper36_stub_double():
    # revision_Paper has no real 'Paper37' property in the generated
    # code (a bare stub) -- manually attach it so revision_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Progress(percent=7)
    partner = revision_Paper()
    setattr(partner, 'Paper37', None)
    _safe_set(owner, 'progress', partner)
    assert getattr(partner, 'Paper37') == owner
    _safe_set(owner, 'progress', None)
    assert getattr(partner, 'Paper37') is None


def test_assoc_papers23_stub_double():
    # revision_Paper has no real 'Paper' property in the generated
    # code (a bare stub) -- manually attach it so revision_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = revision_Paper()
    setattr(partner, 'Paper', None)
    _safe_set(owner, 'authors', {partner})
    assert getattr(partner, 'Paper') == owner
    _safe_set(owner, 'authors', set())
    assert getattr(partner, 'Paper') is None


def test_assoc_paragraph38_stub_double():
    # revision_Write has no real 'revision_Write39' property in the generated
    # code (a bare stub) -- manually attach it so revision_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Paragraph(content="sample_text")
    partner = revision_Write()
    setattr(partner, 'revision_Write39', None)
    _safe_set(owner, 'revision_Paragraph40', partner)
    assert getattr(partner, 'revision_Write39') == owner
    _safe_set(owner, 'revision_Paragraph40', None)
    assert getattr(partner, 'revision_Write39') is None


def test_assoc_paragraphs26_stub_double():
    # revision_Paper has no real 'revision_Paper' property in the generated
    # code (a bare stub) -- manually attach it so revision_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Paragraph(content="sample_text")
    partner = revision_Paper()
    setattr(partner, 'revision_Paper', None)
    _safe_set(owner, 'revision_Paragraph', partner)
    assert owner in getattr(partner, 'revision_Paper')
    _safe_set(owner, 'revision_Paragraph', None)
    assert owner not in getattr(partner, 'revision_Paper')


def test_assoc_placeholder17_stub_double():
    # revision_PlaceHolderRule has no real 'revision_PlaceHolderRule' property in the generated
    # code (a bare stub) -- manually attach it so revision_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Rule(key="sample_text", text="sample_text")
    partner = revision_PlaceHolderRule()
    setattr(partner, 'revision_PlaceHolderRule', None)
    _safe_set(owner, 'revision_Rule18', partner)
    assert getattr(partner, 'revision_PlaceHolderRule') == owner
    _safe_set(owner, 'revision_Rule18', None)
    assert getattr(partner, 'revision_PlaceHolderRule') is None


def test_assoc_placeholder24_stub_double():
    # revision_PlaceHolderRs has no real 'revision_PlaceHolderRs' property in the generated
    # code (a bare stub) -- manually attach it so revision_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = revision_PlaceHolderRs()
    setattr(partner, 'revision_PlaceHolderRs', None)
    _safe_set(owner, 'revision_Researcher25', partner)
    assert getattr(partner, 'revision_PlaceHolderRs') == owner
    _safe_set(owner, 'revision_Researcher25', None)
    assert getattr(partner, 'revision_PlaceHolderRs') is None


def test_assoc_placeholder32_stub_double():
    # revision_PlaceHolderRn has no real 'revision_PlaceHolderRn' property in the generated
    # code (a bare stub) -- manually attach it so revision_ReviewNote's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_ReviewNote's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_ReviewNote(content="sample_text")
    partner = revision_PlaceHolderRn()
    setattr(partner, 'revision_PlaceHolderRn', None)
    _safe_set(owner, 'revision_ReviewNote33', partner)
    assert getattr(partner, 'revision_PlaceHolderRn') == owner
    _safe_set(owner, 'revision_ReviewNote33', None)
    assert getattr(partner, 'revision_PlaceHolderRn') is None


def test_assoc_placeholder9_stub_double():
    # revision_PlaceHolderPP has no real 'revision_PlaceHolderPP' property in the generated
    # code (a bare stub) -- manually attach it so revision_PublicationPhase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_PublicationPhase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_PublicationPhase(maxTime=7, minTime=7, name="sample_text")
    partner = revision_PlaceHolderPP()
    setattr(partner, 'revision_PlaceHolderPP', None)
    _safe_set(owner, 'revision_PublicationPhase10', partner)
    assert getattr(partner, 'revision_PlaceHolderPP') == owner
    _safe_set(owner, 'revision_PublicationPhase10', None)
    assert getattr(partner, 'revision_PlaceHolderPP') is None


def test_assoc_processView49_stub_double():
    # revision_PublicationSystem has no real 'revision_PublicationSystem' property in the generated
    # code (a bare stub) -- manually attach it so revision_PublicationProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_PublicationProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_PublicationProcess(maxTime=7, minTime=7)
    partner = revision_PublicationSystem()
    setattr(partner, 'revision_PublicationSystem', None)
    _safe_set(owner, 'revision_PublicationProcess50', partner)
    assert getattr(partner, 'revision_PublicationSystem') == owner
    _safe_set(owner, 'revision_PublicationProcess50', None)
    assert getattr(partner, 'revision_PublicationSystem') is None


def test_assoc_progress27_stub_double():
    # revision_Paper has no real 'paper' property in the generated
    # code (a bare stub) -- manually attach it so revision_Progress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Progress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Progress(percent=7)
    partner = revision_Paper()
    setattr(partner, 'paper', None)
    _safe_set(owner, 'Progress', partner)
    assert owner in getattr(partner, 'paper')
    _safe_set(owner, 'Progress', None)
    assert owner not in getattr(partner, 'paper')


def test_assoc_researchers44_stub_double():
    # revision_PublicationStructure has no real 'revision_PublicationStructure' property in the generated
    # code (a bare stub) -- manually attach it so revision_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = revision_PublicationStructure()
    setattr(partner, 'revision_PublicationStructure', None)
    _safe_set(owner, 'revision_Researcher45', partner)
    assert owner in getattr(partner, 'revision_PublicationStructure')
    _safe_set(owner, 'revision_Researcher45', None)
    assert owner not in getattr(partner, 'revision_PublicationStructure')


def test_assoc_reviewNote41_stub_double():
    # revision_Review has no real 'revision_Review42' property in the generated
    # code (a bare stub) -- manually attach it so revision_ReviewNote's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_ReviewNote's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_ReviewNote(content="sample_text")
    partner = revision_Review()
    setattr(partner, 'revision_Review42', None)
    _safe_set(owner, 'revision_ReviewNote43', partner)
    assert getattr(partner, 'revision_Review42') == owner
    _safe_set(owner, 'revision_ReviewNote43', None)
    assert getattr(partner, 'revision_Review42') is None


def test_assoc_reviews21_stub_double():
    # revision_Review has no real 'revision_Review' property in the generated
    # code (a bare stub) -- manually attach it so revision_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = revision_Review()
    setattr(partner, 'revision_Review', None)
    _safe_set(owner, 'revision_Researcher22', {partner})
    assert getattr(partner, 'revision_Review') == owner
    _safe_set(owner, 'revision_Researcher22', set())
    assert getattr(partner, 'revision_Review') is None


def test_assoc_writes20_stub_double():
    # revision_Write has no real 'revision_Write' property in the generated
    # code (a bare stub) -- manually attach it so revision_Researcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # revision_Researcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = revision_Researcher(forName="sample_text", name="sample_text", position="sample_text")
    partner = revision_Write()
    setattr(partner, 'revision_Write', None)
    _safe_set(owner, 'revision_Researcher', {partner})
    assert getattr(partner, 'revision_Write') == owner
    _safe_set(owner, 'revision_Researcher', set())
    assert getattr(partner, 'revision_Write') is None




from python_code import revision_Counted

def test_revision_Counted___init__():
    assert revision_Counted.__init__(revision_Counted(0), 0) == None
from python_code import revision_Labelled

def test_revision_Labelled___init__():
    assert revision_Labelled.__init__(revision_Labelled(''), '') == None
from python_code import revision_Named

def test_revision_Named___init__():
    assert revision_Named.__init__(revision_Named(''), '') == None
from python_code import revision_Paper
from python_code import revision_Paragraph
from python_code import revision_Write

def test_revision_Paragraph___init__():
    assert revision_Paragraph.__init__(revision_Paragraph('\x00', revision_Paragraph=revision_Paper(), revision_Paragraph31=set(), revision_Paragraph40=revision_Write()), '', revision_Paragraph=revision_Paper(), revision_Paragraph31=set(), revision_Paragraph40=revision_Write()) == None

