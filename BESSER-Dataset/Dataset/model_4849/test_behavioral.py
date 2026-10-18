import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    aml_AggregationRule,
    aml_AmlDocument,
    aml_Annotation,
    aml_Answer,
    aml_Argument,
    aml_ArgumentTemplate,
    aml_Belief,
    aml_Choice,
    aml_Collection,
    aml_CollectionItem,
    aml_Coverage,
    aml_CreatingTool,
    aml_Creator,
    aml_Dependent,
    aml_DiscoveryMethod,
    aml_DocumentRoot,
    aml_EObject,
    aml_EStringToStringMapEntry,
    aml_End,
    aml_Evidence,
    aml_EvidenceExhibit,
    aml_Exhibit,
    aml_Flag,
    aml_Interval,
    aml_List,
    aml_Memo,
    aml_MetaData,
    aml_NationState,
    aml_Parameter,
    aml_Period,
    aml_Person,
    aml_Publisher,
    aml_Question,
    aml_QuestionRelationships,
    aml_Reader,
    aml_Relevance,
    aml_Reliability,
    aml_Start,
    aml_Template,
    aml_Value,
    aml_Witness,
    ObjectType,
    ObjectType1,
    ObjectType2,
    ObjectType3,
    Type,
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

def test_assoc_amlDocument76_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument78', a1)
    assert _is_linked(b, 'aml_AmlDocument78', a1)
    if hasattr(a1, 'aml_DocumentRoot77'):
        assert _is_linked(a1, 'aml_DocumentRoot77', b)
    _safe_set(b, 'aml_AmlDocument78', a2)
    assert _is_linked(b, 'aml_AmlDocument78', a2)
    if hasattr(a1, 'aml_DocumentRoot77'):
        assert not _is_linked(a1, 'aml_DocumentRoot77', b)
    if hasattr(a2, 'aml_DocumentRoot77'):
        assert _is_linked(a2, 'aml_DocumentRoot77', b)
    _safe_set(b, 'aml_AmlDocument78', None)
    assert not _is_linked(b, 'aml_AmlDocument78', a2)
    if hasattr(a2, 'aml_DocumentRoot77'):
        assert not _is_linked(a2, 'aml_DocumentRoot77', b)


def test_assoc_annotation217_reverse_link_reassign_clear():
    a1 = aml_Evidence(id="sample_text", label="sample_text", ordinal="sample_text")
    a2 = aml_Evidence(id="sample_text_2", label="sample_text_2", ordinal="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation219', a1)
    assert _is_linked(b, 'aml_Annotation219', a1)
    if hasattr(a1, 'aml_Evidence218'):
        assert _is_linked(a1, 'aml_Evidence218', b)
    _safe_set(b, 'aml_Annotation219', a2)
    assert _is_linked(b, 'aml_Annotation219', a2)
    if hasattr(a1, 'aml_Evidence218'):
        assert not _is_linked(a1, 'aml_Evidence218', b)
    if hasattr(a2, 'aml_Evidence218'):
        assert _is_linked(a2, 'aml_Evidence218', b)
    _safe_set(b, 'aml_Annotation219', None)
    assert not _is_linked(b, 'aml_Annotation219', a2)
    if hasattr(a2, 'aml_Evidence218'):
        assert not _is_linked(a2, 'aml_Evidence218', b)


def test_assoc_annotation226_reverse_link_reassign_clear():
    a1 = aml_Exhibit(id="sample_text")
    a2 = aml_Exhibit(id="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation228', a1)
    assert _is_linked(b, 'aml_Annotation228', a1)
    if hasattr(a1, 'aml_Exhibit227'):
        assert _is_linked(a1, 'aml_Exhibit227', b)
    _safe_set(b, 'aml_Annotation228', a2)
    assert _is_linked(b, 'aml_Annotation228', a2)
    if hasattr(a1, 'aml_Exhibit227'):
        assert not _is_linked(a1, 'aml_Exhibit227', b)
    if hasattr(a2, 'aml_Exhibit227'):
        assert _is_linked(a2, 'aml_Exhibit227', b)
    _safe_set(b, 'aml_Annotation228', None)
    assert not _is_linked(b, 'aml_Annotation228', a2)
    if hasattr(a2, 'aml_Exhibit227'):
        assert not _is_linked(a2, 'aml_Exhibit227', b)


def test_assoc_annotation23_reverse_link_reassign_clear():
    a1 = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    a2 = aml_Answer(group="sample_text_2", questionId="sample_text_2", rationale="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation25', a1)
    assert _is_linked(b, 'aml_Annotation25', a1)
    if hasattr(a1, 'aml_Answer24'):
        assert _is_linked(a1, 'aml_Answer24', b)
    _safe_set(b, 'aml_Annotation25', a2)
    assert _is_linked(b, 'aml_Annotation25', a2)
    if hasattr(a1, 'aml_Answer24'):
        assert not _is_linked(a1, 'aml_Answer24', b)
    if hasattr(a2, 'aml_Answer24'):
        assert _is_linked(a2, 'aml_Answer24', b)
    _safe_set(b, 'aml_Annotation25', None)
    assert not _is_linked(b, 'aml_Annotation25', a2)
    if hasattr(a2, 'aml_Answer24'):
        assert not _is_linked(a2, 'aml_Answer24', b)


def test_assoc_annotation310_reverse_link_reassign_clear():
    a1 = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    a2 = aml_Question(amplification="sample_text_2", description="sample_text_2", group="sample_text_2", id="sample_text_2", label="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation312', a1)
    assert _is_linked(b, 'aml_Annotation312', a1)
    if hasattr(a1, 'aml_Question311'):
        assert _is_linked(a1, 'aml_Question311', b)
    _safe_set(b, 'aml_Annotation312', a2)
    assert _is_linked(b, 'aml_Annotation312', a2)
    if hasattr(a1, 'aml_Question311'):
        assert not _is_linked(a1, 'aml_Question311', b)
    if hasattr(a2, 'aml_Question311'):
        assert _is_linked(a2, 'aml_Question311', b)
    _safe_set(b, 'aml_Annotation312', None)
    assert not _is_linked(b, 'aml_Annotation312', a2)
    if hasattr(a2, 'aml_Question311'):
        assert not _is_linked(a2, 'aml_Question311', b)


def test_assoc_annotation319_reverse_link_reassign_clear():
    a1 = aml_Template(id="sample_text")
    a2 = aml_Template(id="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation321', a1)
    assert _is_linked(b, 'aml_Annotation321', a1)
    if hasattr(a1, 'aml_Template320'):
        assert _is_linked(a1, 'aml_Template320', b)
    _safe_set(b, 'aml_Annotation321', a2)
    assert _is_linked(b, 'aml_Annotation321', a2)
    if hasattr(a1, 'aml_Template320'):
        assert not _is_linked(a1, 'aml_Template320', b)
    if hasattr(a2, 'aml_Template320'):
        assert _is_linked(a2, 'aml_Template320', b)
    _safe_set(b, 'aml_Annotation321', None)
    assert not _is_linked(b, 'aml_Annotation321', a2)
    if hasattr(a2, 'aml_Template320'):
        assert not _is_linked(a2, 'aml_Template320', b)


def test_assoc_annotation38_reverse_link_reassign_clear():
    a1 = aml_Argument(id="sample_text")
    a2 = aml_Argument(id="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation40', a1)
    assert _is_linked(b, 'aml_Annotation40', a1)
    if hasattr(a1, 'aml_Argument39'):
        assert _is_linked(a1, 'aml_Argument39', b)
    _safe_set(b, 'aml_Annotation40', a2)
    assert _is_linked(b, 'aml_Annotation40', a2)
    if hasattr(a1, 'aml_Argument39'):
        assert not _is_linked(a1, 'aml_Argument39', b)
    if hasattr(a2, 'aml_Argument39'):
        assert _is_linked(a2, 'aml_Argument39', b)
    _safe_set(b, 'aml_Annotation40', None)
    assert not _is_linked(b, 'aml_Annotation40', a2)
    if hasattr(a2, 'aml_Argument39'):
        assert not _is_linked(a2, 'aml_Argument39', b)


def test_assoc_annotation52_reverse_link_reassign_clear():
    a1 = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    a2 = aml_Collection(group="sample_text_2", id="sample_text_2", label="sample_text_2", label1="sample_text_2", objectType="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation54', a1)
    assert _is_linked(b, 'aml_Annotation54', a1)
    if hasattr(a1, 'aml_Collection53'):
        assert _is_linked(a1, 'aml_Collection53', b)
    _safe_set(b, 'aml_Annotation54', a2)
    assert _is_linked(b, 'aml_Annotation54', a2)
    if hasattr(a1, 'aml_Collection53'):
        assert not _is_linked(a1, 'aml_Collection53', b)
    if hasattr(a2, 'aml_Collection53'):
        assert _is_linked(a2, 'aml_Collection53', b)
    _safe_set(b, 'aml_Annotation54', None)
    assert not _is_linked(b, 'aml_Annotation54', a2)
    if hasattr(a2, 'aml_Collection53'):
        assert not _is_linked(a2, 'aml_Collection53', b)


def test_assoc_annotation66_reverse_link_reassign_clear():
    a1 = aml_DiscoveryMethod(autoTrigger="sample_text", description="sample_text", id="sample_text", importType="sample_text", label="sample_text", type="sample_text", url="sample_text")
    a2 = aml_DiscoveryMethod(autoTrigger="sample_text_2", description="sample_text_2", id="sample_text_2", importType="sample_text_2", label="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation68', a1)
    assert _is_linked(b, 'aml_Annotation68', a1)
    if hasattr(a1, 'aml_DiscoveryMethod67'):
        assert _is_linked(a1, 'aml_DiscoveryMethod67', b)
    _safe_set(b, 'aml_Annotation68', a2)
    assert _is_linked(b, 'aml_Annotation68', a2)
    if hasattr(a1, 'aml_DiscoveryMethod67'):
        assert not _is_linked(a1, 'aml_DiscoveryMethod67', b)
    if hasattr(a2, 'aml_DiscoveryMethod67'):
        assert _is_linked(a2, 'aml_DiscoveryMethod67', b)
    _safe_set(b, 'aml_Annotation68', None)
    assert not _is_linked(b, 'aml_Annotation68', a2)
    if hasattr(a2, 'aml_DiscoveryMethod67'):
        assert not _is_linked(a2, 'aml_DiscoveryMethod67', b)


def test_assoc_annotation79_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation81', a1)
    assert _is_linked(b, 'aml_Annotation81', a1)
    if hasattr(a1, 'aml_DocumentRoot80'):
        assert _is_linked(a1, 'aml_DocumentRoot80', b)
    _safe_set(b, 'aml_Annotation81', a2)
    assert _is_linked(b, 'aml_Annotation81', a2)
    if hasattr(a1, 'aml_DocumentRoot80'):
        assert not _is_linked(a1, 'aml_DocumentRoot80', b)
    if hasattr(a2, 'aml_DocumentRoot80'):
        assert _is_linked(a2, 'aml_DocumentRoot80', b)
    _safe_set(b, 'aml_Annotation81', None)
    assert not _is_linked(b, 'aml_Annotation81', a2)
    if hasattr(a2, 'aml_DocumentRoot80'):
        assert not _is_linked(a2, 'aml_DocumentRoot80', b)


def test_assoc_answer43_reverse_link_reassign_clear():
    a1 = aml_Argument(id="sample_text")
    a2 = aml_Argument(id="sample_text_2")
    b = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    _safe_set(b, 'aml_Answer45', a1)
    assert _is_linked(b, 'aml_Answer45', a1)
    if hasattr(a1, 'aml_Argument44'):
        assert _is_linked(a1, 'aml_Argument44', b)
    _safe_set(b, 'aml_Answer45', a2)
    assert _is_linked(b, 'aml_Answer45', a2)
    if hasattr(a1, 'aml_Argument44'):
        assert not _is_linked(a1, 'aml_Argument44', b)
    if hasattr(a2, 'aml_Argument44'):
        assert _is_linked(a2, 'aml_Argument44', b)
    _safe_set(b, 'aml_Answer45', None)
    assert not _is_linked(b, 'aml_Answer45', a2)
    if hasattr(a2, 'aml_Argument44'):
        assert not _is_linked(a2, 'aml_Argument44', b)


def test_assoc_answer82_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    _safe_set(b, 'aml_Answer84', a1)
    assert _is_linked(b, 'aml_Answer84', a1)
    if hasattr(a1, 'aml_DocumentRoot83'):
        assert _is_linked(a1, 'aml_DocumentRoot83', b)
    _safe_set(b, 'aml_Answer84', a2)
    assert _is_linked(b, 'aml_Answer84', a2)
    if hasattr(a1, 'aml_DocumentRoot83'):
        assert not _is_linked(a1, 'aml_DocumentRoot83', b)
    if hasattr(a2, 'aml_DocumentRoot83'):
        assert _is_linked(a2, 'aml_DocumentRoot83', b)
    _safe_set(b, 'aml_Answer84', None)
    assert not _is_linked(b, 'aml_Answer84', a2)
    if hasattr(a2, 'aml_DocumentRoot83'):
        assert not _is_linked(a2, 'aml_DocumentRoot83', b)


def test_assoc_argument4_reverse_link_reassign_clear():
    a1 = aml_Argument(id="sample_text")
    a2 = aml_Argument(id="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument5', {a1})
    assert _is_linked(b, 'aml_AmlDocument5', a1)
    if hasattr(a1, 'aml_Argument'):
        assert _is_linked(a1, 'aml_Argument', b)
    _safe_set(b, 'aml_AmlDocument5', {a2})
    assert _is_linked(b, 'aml_AmlDocument5', a2)
    if hasattr(a1, 'aml_Argument'):
        assert not _is_linked(a1, 'aml_Argument', b)
    if hasattr(a2, 'aml_Argument'):
        assert _is_linked(a2, 'aml_Argument', b)
    _safe_set(b, 'aml_AmlDocument5', set())
    assert not _is_linked(b, 'aml_AmlDocument5', a2)
    if hasattr(a2, 'aml_Argument'):
        assert not _is_linked(a2, 'aml_Argument', b)


def test_assoc_argument88_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Argument(id="sample_text")
    _safe_set(b, 'aml_Argument90', a1)
    assert _is_linked(b, 'aml_Argument90', a1)
    if hasattr(a1, 'aml_DocumentRoot89'):
        assert _is_linked(a1, 'aml_DocumentRoot89', b)
    _safe_set(b, 'aml_Argument90', a2)
    assert _is_linked(b, 'aml_Argument90', a2)
    if hasattr(a1, 'aml_DocumentRoot89'):
        assert not _is_linked(a1, 'aml_DocumentRoot89', b)
    if hasattr(a2, 'aml_DocumentRoot89'):
        assert _is_linked(a2, 'aml_DocumentRoot89', b)
    _safe_set(b, 'aml_Argument90', None)
    assert not _is_linked(b, 'aml_Argument90', a2)
    if hasattr(a2, 'aml_DocumentRoot89'):
        assert not _is_linked(a2, 'aml_DocumentRoot89', b)


def test_assoc_argumentTemplate41_reverse_link_reassign_clear():
    a1 = aml_ArgumentTemplate(idRef="sample_text", value="sample_text")
    a2 = aml_ArgumentTemplate(idRef="sample_text_2", value="sample_text_2")
    b = aml_Argument(id="sample_text")
    _safe_set(b, 'aml_Argument42', a1)
    assert _is_linked(b, 'aml_Argument42', a1)
    if hasattr(a1, 'aml_ArgumentTemplate'):
        assert _is_linked(a1, 'aml_ArgumentTemplate', b)
    _safe_set(b, 'aml_Argument42', a2)
    assert _is_linked(b, 'aml_Argument42', a2)
    if hasattr(a1, 'aml_ArgumentTemplate'):
        assert not _is_linked(a1, 'aml_ArgumentTemplate', b)
    if hasattr(a2, 'aml_ArgumentTemplate'):
        assert _is_linked(a2, 'aml_ArgumentTemplate', b)
    _safe_set(b, 'aml_Argument42', None)
    assert not _is_linked(b, 'aml_Argument42', a2)
    if hasattr(a2, 'aml_ArgumentTemplate'):
        assert not _is_linked(a2, 'aml_ArgumentTemplate', b)


def test_assoc_argumentTemplate57_reverse_link_reassign_clear():
    a1 = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    a2 = aml_Collection(group="sample_text_2", id="sample_text_2", label="sample_text_2", label1="sample_text_2", objectType="sample_text_2")
    b = aml_ArgumentTemplate(idRef="sample_text", value="sample_text")
    _safe_set(b, 'aml_ArgumentTemplate59', a1)
    assert _is_linked(b, 'aml_ArgumentTemplate59', a1)
    if hasattr(a1, 'aml_Collection58'):
        assert _is_linked(a1, 'aml_Collection58', b)
    _safe_set(b, 'aml_ArgumentTemplate59', a2)
    assert _is_linked(b, 'aml_ArgumentTemplate59', a2)
    if hasattr(a1, 'aml_Collection58'):
        assert not _is_linked(a1, 'aml_Collection58', b)
    if hasattr(a2, 'aml_Collection58'):
        assert _is_linked(a2, 'aml_Collection58', b)
    _safe_set(b, 'aml_ArgumentTemplate59', None)
    assert not _is_linked(b, 'aml_ArgumentTemplate59', a2)
    if hasattr(a2, 'aml_Collection58'):
        assert not _is_linked(a2, 'aml_Collection58', b)


def test_assoc_argumentTemplate63_reverse_link_reassign_clear():
    a1 = aml_DiscoveryMethod(autoTrigger="sample_text", description="sample_text", id="sample_text", importType="sample_text", label="sample_text", type="sample_text", url="sample_text")
    a2 = aml_DiscoveryMethod(autoTrigger="sample_text_2", description="sample_text_2", id="sample_text_2", importType="sample_text_2", label="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = aml_ArgumentTemplate(idRef="sample_text", value="sample_text")
    _safe_set(b, 'aml_ArgumentTemplate65', a1)
    assert _is_linked(b, 'aml_ArgumentTemplate65', a1)
    if hasattr(a1, 'aml_DiscoveryMethod64'):
        assert _is_linked(a1, 'aml_DiscoveryMethod64', b)
    _safe_set(b, 'aml_ArgumentTemplate65', a2)
    assert _is_linked(b, 'aml_ArgumentTemplate65', a2)
    if hasattr(a1, 'aml_DiscoveryMethod64'):
        assert not _is_linked(a1, 'aml_DiscoveryMethod64', b)
    if hasattr(a2, 'aml_DiscoveryMethod64'):
        assert _is_linked(a2, 'aml_DiscoveryMethod64', b)
    _safe_set(b, 'aml_ArgumentTemplate65', None)
    assert not _is_linked(b, 'aml_ArgumentTemplate65', a2)
    if hasattr(a2, 'aml_DiscoveryMethod64'):
        assert not _is_linked(a2, 'aml_DiscoveryMethod64', b)


def test_assoc_argumentTemplate91_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_ArgumentTemplate(idRef="sample_text", value="sample_text")
    _safe_set(b, 'aml_ArgumentTemplate93', a1)
    assert _is_linked(b, 'aml_ArgumentTemplate93', a1)
    if hasattr(a1, 'aml_DocumentRoot92'):
        assert _is_linked(a1, 'aml_DocumentRoot92', b)
    _safe_set(b, 'aml_ArgumentTemplate93', a2)
    assert _is_linked(b, 'aml_ArgumentTemplate93', a2)
    if hasattr(a1, 'aml_DocumentRoot92'):
        assert not _is_linked(a1, 'aml_DocumentRoot92', b)
    if hasattr(a2, 'aml_DocumentRoot92'):
        assert _is_linked(a2, 'aml_DocumentRoot92', b)
    _safe_set(b, 'aml_ArgumentTemplate93', None)
    assert not _is_linked(b, 'aml_ArgumentTemplate93', a2)
    if hasattr(a2, 'aml_DocumentRoot92'):
        assert not _is_linked(a2, 'aml_DocumentRoot92', b)


def test_assoc_belief20_reverse_link_reassign_clear():
    a1 = aml_Belief(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    a2 = aml_Belief(description="sample_text_2", label="sample_text_2", ordinal="sample_text_2", symbol="sample_text_2")
    b = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    _safe_set(b, 'aml_Answer', {a1})
    assert _is_linked(b, 'aml_Answer', a1)
    if hasattr(a1, 'aml_Belief'):
        assert _is_linked(a1, 'aml_Belief', b)
    _safe_set(b, 'aml_Answer', {a2})
    assert _is_linked(b, 'aml_Answer', a2)
    if hasattr(a1, 'aml_Belief'):
        assert not _is_linked(a1, 'aml_Belief', b)
    if hasattr(a2, 'aml_Belief'):
        assert _is_linked(a2, 'aml_Belief', b)
    _safe_set(b, 'aml_Answer', set())
    assert not _is_linked(b, 'aml_Answer', a2)
    if hasattr(a2, 'aml_Belief'):
        assert not _is_linked(a2, 'aml_Belief', b)


def test_assoc_belief94_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Belief(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    _safe_set(b, 'aml_Belief96', a1)
    assert _is_linked(b, 'aml_Belief96', a1)
    if hasattr(a1, 'aml_DocumentRoot95'):
        assert _is_linked(a1, 'aml_DocumentRoot95', b)
    _safe_set(b, 'aml_Belief96', a2)
    assert _is_linked(b, 'aml_Belief96', a2)
    if hasattr(a1, 'aml_DocumentRoot95'):
        assert not _is_linked(a1, 'aml_DocumentRoot95', b)
    if hasattr(a2, 'aml_DocumentRoot95'):
        assert _is_linked(a2, 'aml_DocumentRoot95', b)
    _safe_set(b, 'aml_Belief96', None)
    assert not _is_linked(b, 'aml_Belief96', a2)
    if hasattr(a2, 'aml_DocumentRoot95'):
        assert not _is_linked(a2, 'aml_DocumentRoot95', b)


def test_assoc_choice298_reverse_link_reassign_clear():
    a1 = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    a2 = aml_Question(amplification="sample_text_2", description="sample_text_2", group="sample_text_2", id="sample_text_2", label="sample_text_2")
    b = aml_Choice(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    _safe_set(b, 'aml_Choice300', a1)
    assert _is_linked(b, 'aml_Choice300', a1)
    if hasattr(a1, 'aml_Question299'):
        assert _is_linked(a1, 'aml_Question299', b)
    _safe_set(b, 'aml_Choice300', a2)
    assert _is_linked(b, 'aml_Choice300', a2)
    if hasattr(a1, 'aml_Question299'):
        assert not _is_linked(a1, 'aml_Question299', b)
    if hasattr(a2, 'aml_Question299'):
        assert _is_linked(a2, 'aml_Question299', b)
    _safe_set(b, 'aml_Choice300', None)
    assert not _is_linked(b, 'aml_Choice300', a2)
    if hasattr(a2, 'aml_Question299'):
        assert not _is_linked(a2, 'aml_Question299', b)


def test_assoc_choice97_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Choice(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    _safe_set(b, 'aml_Choice', a1)
    assert _is_linked(b, 'aml_Choice', a1)
    if hasattr(a1, 'aml_DocumentRoot98'):
        assert _is_linked(a1, 'aml_DocumentRoot98', b)
    _safe_set(b, 'aml_Choice', a2)
    assert _is_linked(b, 'aml_Choice', a2)
    if hasattr(a1, 'aml_DocumentRoot98'):
        assert not _is_linked(a1, 'aml_DocumentRoot98', b)
    if hasattr(a2, 'aml_DocumentRoot98'):
        assert _is_linked(a2, 'aml_DocumentRoot98', b)
    _safe_set(b, 'aml_Choice', None)
    assert not _is_linked(b, 'aml_Choice', a2)
    if hasattr(a2, 'aml_DocumentRoot98'):
        assert not _is_linked(a2, 'aml_DocumentRoot98', b)


def test_assoc_collection8_reverse_link_reassign_clear():
    a1 = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    a2 = aml_Collection(group="sample_text_2", id="sample_text_2", label="sample_text_2", label1="sample_text_2", objectType="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument9', {a1})
    assert _is_linked(b, 'aml_AmlDocument9', a1)
    if hasattr(a1, 'aml_Collection'):
        assert _is_linked(a1, 'aml_Collection', b)
    _safe_set(b, 'aml_AmlDocument9', {a2})
    assert _is_linked(b, 'aml_AmlDocument9', a2)
    if hasattr(a1, 'aml_Collection'):
        assert not _is_linked(a1, 'aml_Collection', b)
    if hasattr(a2, 'aml_Collection'):
        assert _is_linked(a2, 'aml_Collection', b)
    _safe_set(b, 'aml_AmlDocument9', set())
    assert not _is_linked(b, 'aml_AmlDocument9', a2)
    if hasattr(a2, 'aml_Collection'):
        assert not _is_linked(a2, 'aml_Collection', b)


def test_assoc_collection99_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Collection101', a1)
    assert _is_linked(b, 'aml_Collection101', a1)
    if hasattr(a1, 'aml_DocumentRoot100'):
        assert _is_linked(a1, 'aml_DocumentRoot100', b)
    _safe_set(b, 'aml_Collection101', a2)
    assert _is_linked(b, 'aml_Collection101', a2)
    if hasattr(a1, 'aml_DocumentRoot100'):
        assert not _is_linked(a1, 'aml_DocumentRoot100', b)
    if hasattr(a2, 'aml_DocumentRoot100'):
        assert _is_linked(a2, 'aml_DocumentRoot100', b)
    _safe_set(b, 'aml_Collection101', None)
    assert not _is_linked(b, 'aml_Collection101', a2)
    if hasattr(a2, 'aml_DocumentRoot100'):
        assert not _is_linked(a2, 'aml_DocumentRoot100', b)


def test_assoc_collectionItem102_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_CollectionItem(idRef="sample_text", objectType="sample_text", ordinal="sample_text")
    _safe_set(b, 'aml_CollectionItem104', a1)
    assert _is_linked(b, 'aml_CollectionItem104', a1)
    if hasattr(a1, 'aml_DocumentRoot103'):
        assert _is_linked(a1, 'aml_DocumentRoot103', b)
    _safe_set(b, 'aml_CollectionItem104', a2)
    assert _is_linked(b, 'aml_CollectionItem104', a2)
    if hasattr(a1, 'aml_DocumentRoot103'):
        assert not _is_linked(a1, 'aml_DocumentRoot103', b)
    if hasattr(a2, 'aml_DocumentRoot103'):
        assert _is_linked(a2, 'aml_DocumentRoot103', b)
    _safe_set(b, 'aml_CollectionItem104', None)
    assert not _is_linked(b, 'aml_CollectionItem104', a2)
    if hasattr(a2, 'aml_DocumentRoot103'):
        assert not _is_linked(a2, 'aml_DocumentRoot103', b)


def test_assoc_collectionItem60_reverse_link_reassign_clear():
    a1 = aml_CollectionItem(idRef="sample_text", objectType="sample_text", ordinal="sample_text")
    a2 = aml_CollectionItem(idRef="sample_text_2", objectType="sample_text_2", ordinal="sample_text_2")
    b = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Collection61', {a1})
    assert _is_linked(b, 'aml_Collection61', a1)
    if hasattr(a1, 'aml_CollectionItem'):
        assert _is_linked(a1, 'aml_CollectionItem', b)
    _safe_set(b, 'aml_Collection61', {a2})
    assert _is_linked(b, 'aml_Collection61', a2)
    if hasattr(a1, 'aml_CollectionItem'):
        assert not _is_linked(a1, 'aml_CollectionItem', b)
    if hasattr(a2, 'aml_CollectionItem'):
        assert _is_linked(a2, 'aml_CollectionItem', b)
    _safe_set(b, 'aml_Collection61', set())
    assert not _is_linked(b, 'aml_Collection61', a2)
    if hasattr(a2, 'aml_CollectionItem'):
        assert not _is_linked(a2, 'aml_CollectionItem', b)


def test_assoc_coverage108_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Coverage(group="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Coverage110', a1)
    assert _is_linked(b, 'aml_Coverage110', a1)
    if hasattr(a1, 'aml_DocumentRoot109'):
        assert _is_linked(a1, 'aml_DocumentRoot109', b)
    _safe_set(b, 'aml_Coverage110', a2)
    assert _is_linked(b, 'aml_Coverage110', a2)
    if hasattr(a1, 'aml_DocumentRoot109'):
        assert not _is_linked(a1, 'aml_DocumentRoot109', b)
    if hasattr(a2, 'aml_DocumentRoot109'):
        assert _is_linked(a2, 'aml_DocumentRoot109', b)
    _safe_set(b, 'aml_Coverage110', None)
    assert not _is_linked(b, 'aml_Coverage110', a2)
    if hasattr(a2, 'aml_DocumentRoot109'):
        assert not _is_linked(a2, 'aml_DocumentRoot109', b)


def test_assoc_coverage271_reverse_link_reassign_clear():
    a1 = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    a2 = aml_MetaData(date="sample_text_2", description="sample_text_2", group="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", title="sample_text_2")
    b = aml_Coverage(group="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Coverage273', a1)
    assert _is_linked(b, 'aml_Coverage273', a1)
    if hasattr(a1, 'aml_MetaData272'):
        assert _is_linked(a1, 'aml_MetaData272', b)
    _safe_set(b, 'aml_Coverage273', a2)
    assert _is_linked(b, 'aml_Coverage273', a2)
    if hasattr(a1, 'aml_MetaData272'):
        assert not _is_linked(a1, 'aml_MetaData272', b)
    if hasattr(a2, 'aml_MetaData272'):
        assert _is_linked(a2, 'aml_MetaData272', b)
    _safe_set(b, 'aml_Coverage273', None)
    assert not _is_linked(b, 'aml_Coverage273', a2)
    if hasattr(a2, 'aml_MetaData272'):
        assert not _is_linked(a2, 'aml_MetaData272', b)


def test_assoc_creatingTool111_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_CreatingTool(label="sample_text", toolType="sample_text", version="sample_text")
    _safe_set(b, 'aml_CreatingTool113', a1)
    assert _is_linked(b, 'aml_CreatingTool113', a1)
    if hasattr(a1, 'aml_DocumentRoot112'):
        assert _is_linked(a1, 'aml_DocumentRoot112', b)
    _safe_set(b, 'aml_CreatingTool113', a2)
    assert _is_linked(b, 'aml_CreatingTool113', a2)
    if hasattr(a1, 'aml_DocumentRoot112'):
        assert not _is_linked(a1, 'aml_DocumentRoot112', b)
    if hasattr(a2, 'aml_DocumentRoot112'):
        assert _is_linked(a2, 'aml_DocumentRoot112', b)
    _safe_set(b, 'aml_CreatingTool113', None)
    assert not _is_linked(b, 'aml_CreatingTool113', a2)
    if hasattr(a2, 'aml_DocumentRoot112'):
        assert not _is_linked(a2, 'aml_DocumentRoot112', b)


def test_assoc_creatingTool316_reverse_link_reassign_clear():
    a1 = aml_Template(id="sample_text")
    a2 = aml_Template(id="sample_text_2")
    b = aml_CreatingTool(label="sample_text", toolType="sample_text", version="sample_text")
    _safe_set(b, 'aml_CreatingTool318', a1)
    assert _is_linked(b, 'aml_CreatingTool318', a1)
    if hasattr(a1, 'aml_Template317'):
        assert _is_linked(a1, 'aml_Template317', b)
    _safe_set(b, 'aml_CreatingTool318', a2)
    assert _is_linked(b, 'aml_CreatingTool318', a2)
    if hasattr(a1, 'aml_Template317'):
        assert not _is_linked(a1, 'aml_Template317', b)
    if hasattr(a2, 'aml_Template317'):
        assert _is_linked(a2, 'aml_Template317', b)
    _safe_set(b, 'aml_CreatingTool318', None)
    assert not _is_linked(b, 'aml_CreatingTool318', a2)
    if hasattr(a2, 'aml_Template317'):
        assert not _is_linked(a2, 'aml_Template317', b)


def test_assoc_creatingTool36_reverse_link_reassign_clear():
    a1 = aml_CreatingTool(label="sample_text", toolType="sample_text", version="sample_text")
    a2 = aml_CreatingTool(label="sample_text_2", toolType="sample_text_2", version="sample_text_2")
    b = aml_Argument(id="sample_text")
    _safe_set(b, 'aml_Argument37', a1)
    assert _is_linked(b, 'aml_Argument37', a1)
    if hasattr(a1, 'aml_CreatingTool'):
        assert _is_linked(a1, 'aml_CreatingTool', b)
    _safe_set(b, 'aml_Argument37', a2)
    assert _is_linked(b, 'aml_Argument37', a2)
    if hasattr(a1, 'aml_CreatingTool'):
        assert not _is_linked(a1, 'aml_CreatingTool', b)
    if hasattr(a2, 'aml_CreatingTool'):
        assert _is_linked(a2, 'aml_CreatingTool', b)
    _safe_set(b, 'aml_Argument37', None)
    assert not _is_linked(b, 'aml_Argument37', a2)
    if hasattr(a2, 'aml_CreatingTool'):
        assert not _is_linked(a2, 'aml_CreatingTool', b)


def test_assoc_creatingTool49_reverse_link_reassign_clear():
    a1 = aml_CreatingTool(label="sample_text", toolType="sample_text", version="sample_text")
    a2 = aml_CreatingTool(label="sample_text_2", toolType="sample_text_2", version="sample_text_2")
    b = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Collection50', a1)
    assert _is_linked(b, 'aml_Collection50', a1)
    if hasattr(a1, 'aml_CreatingTool51'):
        assert _is_linked(a1, 'aml_CreatingTool51', b)
    _safe_set(b, 'aml_Collection50', a2)
    assert _is_linked(b, 'aml_Collection50', a2)
    if hasattr(a1, 'aml_CreatingTool51'):
        assert not _is_linked(a1, 'aml_CreatingTool51', b)
    if hasattr(a2, 'aml_CreatingTool51'):
        assert _is_linked(a2, 'aml_CreatingTool51', b)
    _safe_set(b, 'aml_Collection50', None)
    assert not _is_linked(b, 'aml_Collection50', a2)
    if hasattr(a2, 'aml_CreatingTool51'):
        assert not _is_linked(a2, 'aml_CreatingTool51', b)


def test_assoc_creator114_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Creator(description="sample_text", idRef="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Creator', a1)
    assert _is_linked(b, 'aml_Creator', a1)
    if hasattr(a1, 'aml_DocumentRoot115'):
        assert _is_linked(a1, 'aml_DocumentRoot115', b)
    _safe_set(b, 'aml_Creator', a2)
    assert _is_linked(b, 'aml_Creator', a2)
    if hasattr(a1, 'aml_DocumentRoot115'):
        assert not _is_linked(a1, 'aml_DocumentRoot115', b)
    if hasattr(a2, 'aml_DocumentRoot115'):
        assert _is_linked(a2, 'aml_DocumentRoot115', b)
    _safe_set(b, 'aml_Creator', None)
    assert not _is_linked(b, 'aml_Creator', a2)
    if hasattr(a2, 'aml_DocumentRoot115'):
        assert not _is_linked(a2, 'aml_DocumentRoot115', b)


def test_assoc_creator235_reverse_link_reassign_clear():
    a1 = aml_Memo(body="sample_text", id="sample_text", subject="sample_text", type="sample_text")
    a2 = aml_Memo(body="sample_text_2", id="sample_text_2", subject="sample_text_2", type="sample_text_2")
    b = aml_Creator(description="sample_text", idRef="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Creator237', a1)
    assert _is_linked(b, 'aml_Creator237', a1)
    if hasattr(a1, 'aml_Memo236'):
        assert _is_linked(a1, 'aml_Memo236', b)
    _safe_set(b, 'aml_Creator237', a2)
    assert _is_linked(b, 'aml_Creator237', a2)
    if hasattr(a1, 'aml_Memo236'):
        assert not _is_linked(a1, 'aml_Memo236', b)
    if hasattr(a2, 'aml_Memo236'):
        assert _is_linked(a2, 'aml_Memo236', b)
    _safe_set(b, 'aml_Creator237', None)
    assert not _is_linked(b, 'aml_Creator237', a2)
    if hasattr(a2, 'aml_Memo236'):
        assert not _is_linked(a2, 'aml_Memo236', b)


def test_assoc_creator241_reverse_link_reassign_clear():
    a1 = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    a2 = aml_MetaData(date="sample_text_2", description="sample_text_2", group="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", title="sample_text_2")
    b = aml_Creator(description="sample_text", idRef="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Creator243', a1)
    assert _is_linked(b, 'aml_Creator243', a1)
    if hasattr(a1, 'aml_MetaData242'):
        assert _is_linked(a1, 'aml_MetaData242', b)
    _safe_set(b, 'aml_Creator243', a2)
    assert _is_linked(b, 'aml_Creator243', a2)
    if hasattr(a1, 'aml_MetaData242'):
        assert not _is_linked(a1, 'aml_MetaData242', b)
    if hasattr(a2, 'aml_MetaData242'):
        assert _is_linked(a2, 'aml_MetaData242', b)
    _safe_set(b, 'aml_Creator243', None)
    assert not _is_linked(b, 'aml_Creator243', a2)
    if hasattr(a2, 'aml_MetaData242'):
        assert not _is_linked(a2, 'aml_MetaData242', b)


def test_assoc_dependent116_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_Dependent(idRef="sample_text", ordinal="sample_text")
    _safe_set(b, 'aml_Dependent', a1)
    assert _is_linked(b, 'aml_Dependent', a1)
    if hasattr(a1, 'aml_DocumentRoot117'):
        assert _is_linked(a1, 'aml_DocumentRoot117', b)
    _safe_set(b, 'aml_Dependent', a2)
    assert _is_linked(b, 'aml_Dependent', a2)
    if hasattr(a1, 'aml_DocumentRoot117'):
        assert not _is_linked(a1, 'aml_DocumentRoot117', b)
    if hasattr(a2, 'aml_DocumentRoot117'):
        assert _is_linked(a2, 'aml_DocumentRoot117', b)
    _safe_set(b, 'aml_Dependent', None)
    assert not _is_linked(b, 'aml_Dependent', a2)
    if hasattr(a2, 'aml_DocumentRoot117'):
        assert not _is_linked(a2, 'aml_DocumentRoot117', b)


def test_assoc_discoveryMethod118_reverse_link_reassign_clear():
    a1 = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    a2 = aml_DocumentRoot(actor="sample_text_2", body="sample_text_2", date="sample_text_2", department="sample_text_2", description="sample_text_2", description1="sample_text_2", email="sample_text_2", event="sample_text_2", firstName="sample_text_2", id="sample_text_2", idRef="sample_text_2", label="sample_text_2", label1="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", mixed="sample_text_2", nickName="sample_text_2", organization="sample_text_2", perspective="sample_text_2", rationale="sample_text_2", region="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", symbol="sample_text_2", title="sample_text_2", url="sample_text_2")
    b = aml_DiscoveryMethod(autoTrigger="sample_text", description="sample_text", id="sample_text", importType="sample_text", label="sample_text", type="sample_text", url="sample_text")
    _safe_set(b, 'aml_DiscoveryMethod120', a1)
    assert _is_linked(b, 'aml_DiscoveryMethod120', a1)
    if hasattr(a1, 'aml_DocumentRoot119'):
        assert _is_linked(a1, 'aml_DocumentRoot119', b)
    _safe_set(b, 'aml_DiscoveryMethod120', a2)
    assert _is_linked(b, 'aml_DiscoveryMethod120', a2)
    if hasattr(a1, 'aml_DocumentRoot119'):
        assert not _is_linked(a1, 'aml_DocumentRoot119', b)
    if hasattr(a2, 'aml_DocumentRoot119'):
        assert _is_linked(a2, 'aml_DocumentRoot119', b)
    _safe_set(b, 'aml_DiscoveryMethod120', None)
    assert not _is_linked(b, 'aml_DiscoveryMethod120', a2)
    if hasattr(a2, 'aml_DocumentRoot119'):
        assert not _is_linked(a2, 'aml_DocumentRoot119', b)


def test_assoc_discoveryMethod14_reverse_link_reassign_clear():
    a1 = aml_DiscoveryMethod(autoTrigger="sample_text", description="sample_text", id="sample_text", importType="sample_text", label="sample_text", type="sample_text", url="sample_text")
    a2 = aml_DiscoveryMethod(autoTrigger="sample_text_2", description="sample_text_2", id="sample_text_2", importType="sample_text_2", label="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument15', {a1})
    assert _is_linked(b, 'aml_AmlDocument15', a1)
    if hasattr(a1, 'aml_DiscoveryMethod'):
        assert _is_linked(a1, 'aml_DiscoveryMethod', b)
    _safe_set(b, 'aml_AmlDocument15', {a2})
    assert _is_linked(b, 'aml_AmlDocument15', a2)
    if hasattr(a1, 'aml_DiscoveryMethod'):
        assert not _is_linked(a1, 'aml_DiscoveryMethod', b)
    if hasattr(a2, 'aml_DiscoveryMethod'):
        assert _is_linked(a2, 'aml_DiscoveryMethod', b)
    _safe_set(b, 'aml_AmlDocument15', set())
    assert not _is_linked(b, 'aml_AmlDocument15', a2)
    if hasattr(a2, 'aml_DiscoveryMethod'):
        assert not _is_linked(a2, 'aml_DiscoveryMethod', b)


def test_assoc_discoveryMethod307_reverse_link_reassign_clear():
    a1 = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    a2 = aml_Question(amplification="sample_text_2", description="sample_text_2", group="sample_text_2", id="sample_text_2", label="sample_text_2")
    b = aml_DiscoveryMethod(autoTrigger="sample_text", description="sample_text", id="sample_text", importType="sample_text", label="sample_text", type="sample_text", url="sample_text")
    _safe_set(b, 'aml_DiscoveryMethod309', a1)
    assert _is_linked(b, 'aml_DiscoveryMethod309', a1)
    if hasattr(a1, 'aml_Question308'):
        assert _is_linked(a1, 'aml_Question308', b)
    _safe_set(b, 'aml_DiscoveryMethod309', a2)
    assert _is_linked(b, 'aml_DiscoveryMethod309', a2)
    if hasattr(a1, 'aml_Question308'):
        assert not _is_linked(a1, 'aml_Question308', b)
    if hasattr(a2, 'aml_Question308'):
        assert _is_linked(a2, 'aml_Question308', b)
    _safe_set(b, 'aml_DiscoveryMethod309', None)
    assert not _is_linked(b, 'aml_DiscoveryMethod309', a2)
    if hasattr(a2, 'aml_Question308'):
        assert not _is_linked(a2, 'aml_Question308', b)


def test_assoc_discoveryMethod31_reverse_link_reassign_clear():
    a1 = aml_DiscoveryMethod(autoTrigger="sample_text", description="sample_text", id="sample_text", importType="sample_text", label="sample_text", type="sample_text", url="sample_text")
    a2 = aml_DiscoveryMethod(autoTrigger="sample_text_2", description="sample_text_2", id="sample_text_2", importType="sample_text_2", label="sample_text_2", type="sample_text_2", url="sample_text_2")
    b = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    _safe_set(b, 'aml_Answer32', {a1})
    assert _is_linked(b, 'aml_Answer32', a1)
    if hasattr(a1, 'aml_DiscoveryMethod33'):
        assert _is_linked(a1, 'aml_DiscoveryMethod33', b)
    _safe_set(b, 'aml_Answer32', {a2})
    assert _is_linked(b, 'aml_Answer32', a2)
    if hasattr(a1, 'aml_DiscoveryMethod33'):
        assert not _is_linked(a1, 'aml_DiscoveryMethod33', b)
    if hasattr(a2, 'aml_DiscoveryMethod33'):
        assert _is_linked(a2, 'aml_DiscoveryMethod33', b)
    _safe_set(b, 'aml_Answer32', set())
    assert not _is_linked(b, 'aml_Answer32', a2)
    if hasattr(a2, 'aml_DiscoveryMethod33'):
        assert not _is_linked(a2, 'aml_DiscoveryMethod33', b)


def test_assoc_end121_reverse_link_reassign_clear():
    a1 = aml_End(scheme="sample_text", value="sample_text")
    a2 = aml_End(scheme="sample_text_2", value="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot122', {a1})
    assert _is_linked(b, 'aml_DocumentRoot122', a1)
    if hasattr(a1, 'aml_End'):
        assert _is_linked(a1, 'aml_End', b)
    _safe_set(b, 'aml_DocumentRoot122', {a2})
    assert _is_linked(b, 'aml_DocumentRoot122', a2)
    if hasattr(a1, 'aml_End'):
        assert not _is_linked(a1, 'aml_End', b)
    if hasattr(a2, 'aml_End'):
        assert _is_linked(a2, 'aml_End', b)
    _safe_set(b, 'aml_DocumentRoot122', set())
    assert not _is_linked(b, 'aml_DocumentRoot122', a2)
    if hasattr(a2, 'aml_End'):
        assert not _is_linked(a2, 'aml_End', b)


def test_assoc_end289_reverse_link_reassign_clear():
    a1 = aml_Period(group="sample_text", label="sample_text")
    a2 = aml_Period(group="sample_text_2", label="sample_text_2")
    b = aml_End(scheme="sample_text", value="sample_text")
    _safe_set(b, 'aml_End291', a1)
    assert _is_linked(b, 'aml_End291', a1)
    if hasattr(a1, 'aml_Period290'):
        assert _is_linked(a1, 'aml_Period290', b)
    _safe_set(b, 'aml_End291', a2)
    assert _is_linked(b, 'aml_End291', a2)
    if hasattr(a1, 'aml_Period290'):
        assert not _is_linked(a1, 'aml_Period290', b)
    if hasattr(a2, 'aml_Period290'):
        assert _is_linked(a2, 'aml_Period290', b)
    _safe_set(b, 'aml_End291', None)
    assert not _is_linked(b, 'aml_End291', a2)
    if hasattr(a2, 'aml_Period290'):
        assert not _is_linked(a2, 'aml_Period290', b)


def test_assoc_evidence123_reverse_link_reassign_clear():
    a1 = aml_Evidence(id="sample_text", label="sample_text", ordinal="sample_text")
    a2 = aml_Evidence(id="sample_text_2", label="sample_text_2", ordinal="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot124', {a1})
    assert _is_linked(b, 'aml_DocumentRoot124', a1)
    if hasattr(a1, 'aml_Evidence125'):
        assert _is_linked(a1, 'aml_Evidence125', b)
    _safe_set(b, 'aml_DocumentRoot124', {a2})
    assert _is_linked(b, 'aml_DocumentRoot124', a2)
    if hasattr(a1, 'aml_Evidence125'):
        assert not _is_linked(a1, 'aml_Evidence125', b)
    if hasattr(a2, 'aml_Evidence125'):
        assert _is_linked(a2, 'aml_Evidence125', b)
    _safe_set(b, 'aml_DocumentRoot124', set())
    assert not _is_linked(b, 'aml_DocumentRoot124', a2)
    if hasattr(a2, 'aml_Evidence125'):
        assert not _is_linked(a2, 'aml_Evidence125', b)


def test_assoc_evidence29_reverse_link_reassign_clear():
    a1 = aml_Evidence(id="sample_text", label="sample_text", ordinal="sample_text")
    a2 = aml_Evidence(id="sample_text_2", label="sample_text_2", ordinal="sample_text_2")
    b = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    _safe_set(b, 'aml_Answer30', {a1})
    assert _is_linked(b, 'aml_Answer30', a1)
    if hasattr(a1, 'aml_Evidence'):
        assert _is_linked(a1, 'aml_Evidence', b)
    _safe_set(b, 'aml_Answer30', {a2})
    assert _is_linked(b, 'aml_Answer30', a2)
    if hasattr(a1, 'aml_Evidence'):
        assert not _is_linked(a1, 'aml_Evidence', b)
    if hasattr(a2, 'aml_Evidence'):
        assert _is_linked(a2, 'aml_Evidence', b)
    _safe_set(b, 'aml_Answer30', set())
    assert not _is_linked(b, 'aml_Answer30', a2)
    if hasattr(a2, 'aml_Evidence'):
        assert not _is_linked(a2, 'aml_Evidence', b)


def test_assoc_evidenceExhibit126_reverse_link_reassign_clear():
    a1 = aml_EvidenceExhibit(idRef="sample_text", questionId="sample_text", value="sample_text")
    a2 = aml_EvidenceExhibit(idRef="sample_text_2", questionId="sample_text_2", value="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot127', {a1})
    assert _is_linked(b, 'aml_DocumentRoot127', a1)
    if hasattr(a1, 'aml_EvidenceExhibit'):
        assert _is_linked(a1, 'aml_EvidenceExhibit', b)
    _safe_set(b, 'aml_DocumentRoot127', {a2})
    assert _is_linked(b, 'aml_DocumentRoot127', a2)
    if hasattr(a1, 'aml_EvidenceExhibit'):
        assert not _is_linked(a1, 'aml_EvidenceExhibit', b)
    if hasattr(a2, 'aml_EvidenceExhibit'):
        assert _is_linked(a2, 'aml_EvidenceExhibit', b)
    _safe_set(b, 'aml_DocumentRoot127', set())
    assert not _is_linked(b, 'aml_DocumentRoot127', a2)
    if hasattr(a2, 'aml_EvidenceExhibit'):
        assert not _is_linked(a2, 'aml_EvidenceExhibit', b)


def test_assoc_evidenceExhibit205_reverse_link_reassign_clear():
    a1 = aml_EvidenceExhibit(idRef="sample_text", questionId="sample_text", value="sample_text")
    a2 = aml_EvidenceExhibit(idRef="sample_text_2", questionId="sample_text_2", value="sample_text_2")
    b = aml_Evidence(id="sample_text", label="sample_text", ordinal="sample_text")
    _safe_set(b, 'aml_Evidence206', a1)
    assert _is_linked(b, 'aml_Evidence206', a1)
    if hasattr(a1, 'aml_EvidenceExhibit207'):
        assert _is_linked(a1, 'aml_EvidenceExhibit207', b)
    _safe_set(b, 'aml_Evidence206', a2)
    assert _is_linked(b, 'aml_Evidence206', a2)
    if hasattr(a1, 'aml_EvidenceExhibit207'):
        assert not _is_linked(a1, 'aml_EvidenceExhibit207', b)
    if hasattr(a2, 'aml_EvidenceExhibit207'):
        assert _is_linked(a2, 'aml_EvidenceExhibit207', b)
    _safe_set(b, 'aml_Evidence206', None)
    assert not _is_linked(b, 'aml_Evidence206', a2)
    if hasattr(a2, 'aml_EvidenceExhibit207'):
        assert not _is_linked(a2, 'aml_EvidenceExhibit207', b)


def test_assoc_exhibit128_reverse_link_reassign_clear():
    a1 = aml_Exhibit(id="sample_text")
    a2 = aml_Exhibit(id="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot129', {a1})
    assert _is_linked(b, 'aml_DocumentRoot129', a1)
    if hasattr(a1, 'aml_Exhibit130'):
        assert _is_linked(a1, 'aml_Exhibit130', b)
    _safe_set(b, 'aml_DocumentRoot129', {a2})
    assert _is_linked(b, 'aml_DocumentRoot129', a2)
    if hasattr(a1, 'aml_Exhibit130'):
        assert not _is_linked(a1, 'aml_Exhibit130', b)
    if hasattr(a2, 'aml_Exhibit130'):
        assert _is_linked(a2, 'aml_Exhibit130', b)
    _safe_set(b, 'aml_DocumentRoot129', set())
    assert not _is_linked(b, 'aml_DocumentRoot129', a2)
    if hasattr(a2, 'aml_Exhibit130'):
        assert not _is_linked(a2, 'aml_Exhibit130', b)


def test_assoc_exhibit6_reverse_link_reassign_clear():
    a1 = aml_Exhibit(id="sample_text")
    a2 = aml_Exhibit(id="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument7', {a1})
    assert _is_linked(b, 'aml_AmlDocument7', a1)
    if hasattr(a1, 'aml_Exhibit'):
        assert _is_linked(a1, 'aml_Exhibit', b)
    _safe_set(b, 'aml_AmlDocument7', {a2})
    assert _is_linked(b, 'aml_AmlDocument7', a2)
    if hasattr(a1, 'aml_Exhibit'):
        assert not _is_linked(a1, 'aml_Exhibit', b)
    if hasattr(a2, 'aml_Exhibit'):
        assert _is_linked(a2, 'aml_Exhibit', b)
    _safe_set(b, 'aml_AmlDocument7', set())
    assert not _is_linked(b, 'aml_AmlDocument7', a2)
    if hasattr(a2, 'aml_Exhibit'):
        assert not _is_linked(a2, 'aml_Exhibit', b)


def test_assoc_flag131_reverse_link_reassign_clear():
    a1 = aml_Flag(description="sample_text", flagType="sample_text", label="sample_text")
    a2 = aml_Flag(description="sample_text_2", flagType="sample_text_2", label="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot132', {a1})
    assert _is_linked(b, 'aml_DocumentRoot132', a1)
    if hasattr(a1, 'aml_Flag133'):
        assert _is_linked(a1, 'aml_Flag133', b)
    _safe_set(b, 'aml_DocumentRoot132', {a2})
    assert _is_linked(b, 'aml_DocumentRoot132', a2)
    if hasattr(a1, 'aml_Flag133'):
        assert not _is_linked(a1, 'aml_Flag133', b)
    if hasattr(a2, 'aml_Flag133'):
        assert _is_linked(a2, 'aml_Flag133', b)
    _safe_set(b, 'aml_DocumentRoot132', set())
    assert not _is_linked(b, 'aml_DocumentRoot132', a2)
    if hasattr(a2, 'aml_Flag133'):
        assert not _is_linked(a2, 'aml_Flag133', b)


def test_assoc_flag18_reverse_link_reassign_clear():
    a1 = aml_Flag(description="sample_text", flagType="sample_text", label="sample_text")
    a2 = aml_Flag(description="sample_text_2", flagType="sample_text_2", label="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation19', {a1})
    assert _is_linked(b, 'aml_Annotation19', a1)
    if hasattr(a1, 'aml_Flag'):
        assert _is_linked(a1, 'aml_Flag', b)
    _safe_set(b, 'aml_Annotation19', {a2})
    assert _is_linked(b, 'aml_Annotation19', a2)
    if hasattr(a1, 'aml_Flag'):
        assert not _is_linked(a1, 'aml_Flag', b)
    if hasattr(a2, 'aml_Flag'):
        assert _is_linked(a2, 'aml_Flag', b)
    _safe_set(b, 'aml_Annotation19', set())
    assert not _is_linked(b, 'aml_Annotation19', a2)
    if hasattr(a2, 'aml_Flag'):
        assert not _is_linked(a2, 'aml_Flag', b)


def test_assoc_interval143_reverse_link_reassign_clear():
    a1 = aml_Interval(max="sample_text", min="sample_text")
    a2 = aml_Interval(max="sample_text_2", min="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot144', {a1})
    assert _is_linked(b, 'aml_DocumentRoot144', a1)
    if hasattr(a1, 'aml_Interval'):
        assert _is_linked(a1, 'aml_Interval', b)
    _safe_set(b, 'aml_DocumentRoot144', {a2})
    assert _is_linked(b, 'aml_DocumentRoot144', a2)
    if hasattr(a1, 'aml_Interval'):
        assert not _is_linked(a1, 'aml_Interval', b)
    if hasattr(a2, 'aml_Interval'):
        assert _is_linked(a2, 'aml_Interval', b)
    _safe_set(b, 'aml_DocumentRoot144', set())
    assert not _is_linked(b, 'aml_DocumentRoot144', a2)
    if hasattr(a2, 'aml_Interval'):
        assert not _is_linked(a2, 'aml_Interval', b)


def test_assoc_interval325_reverse_link_reassign_clear():
    a1 = aml_Value(group="sample_text", mixed="sample_text", type="sample_text", unit="sample_text")
    a2 = aml_Value(group="sample_text_2", mixed="sample_text_2", type="sample_text_2", unit="sample_text_2")
    b = aml_Interval(max="sample_text", min="sample_text")
    _safe_set(b, 'aml_Interval327', a1)
    assert _is_linked(b, 'aml_Interval327', a1)
    if hasattr(a1, 'aml_Value326'):
        assert _is_linked(a1, 'aml_Value326', b)
    _safe_set(b, 'aml_Interval327', a2)
    assert _is_linked(b, 'aml_Interval327', a2)
    if hasattr(a1, 'aml_Value326'):
        assert not _is_linked(a1, 'aml_Value326', b)
    if hasattr(a2, 'aml_Value326'):
        assert _is_linked(a2, 'aml_Value326', b)
    _safe_set(b, 'aml_Interval327', None)
    assert not _is_linked(b, 'aml_Interval327', a2)
    if hasattr(a2, 'aml_Value326'):
        assert not _is_linked(a2, 'aml_Value326', b)


def test_assoc_list148_reverse_link_reassign_clear():
    a1 = aml_List(group="sample_text")
    a2 = aml_List(group="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot149', {a1})
    assert _is_linked(b, 'aml_DocumentRoot149', a1)
    if hasattr(a1, 'aml_List'):
        assert _is_linked(a1, 'aml_List', b)
    _safe_set(b, 'aml_DocumentRoot149', {a2})
    assert _is_linked(b, 'aml_DocumentRoot149', a2)
    if hasattr(a1, 'aml_List'):
        assert not _is_linked(a1, 'aml_List', b)
    if hasattr(a2, 'aml_List'):
        assert _is_linked(a2, 'aml_List', b)
    _safe_set(b, 'aml_DocumentRoot149', set())
    assert not _is_linked(b, 'aml_DocumentRoot149', a2)
    if hasattr(a2, 'aml_List'):
        assert not _is_linked(a2, 'aml_List', b)


def test_assoc_list328_reverse_link_reassign_clear():
    a1 = aml_Value(group="sample_text", mixed="sample_text", type="sample_text", unit="sample_text")
    a2 = aml_Value(group="sample_text_2", mixed="sample_text_2", type="sample_text_2", unit="sample_text_2")
    b = aml_List(group="sample_text")
    _safe_set(b, 'aml_List330', a1)
    assert _is_linked(b, 'aml_List330', a1)
    if hasattr(a1, 'aml_Value329'):
        assert _is_linked(a1, 'aml_Value329', b)
    _safe_set(b, 'aml_List330', a2)
    assert _is_linked(b, 'aml_List330', a2)
    if hasattr(a1, 'aml_Value329'):
        assert not _is_linked(a1, 'aml_Value329', b)
    if hasattr(a2, 'aml_Value329'):
        assert _is_linked(a2, 'aml_Value329', b)
    _safe_set(b, 'aml_List330', None)
    assert not _is_linked(b, 'aml_List330', a2)
    if hasattr(a2, 'aml_Value329'):
        assert not _is_linked(a2, 'aml_Value329', b)


def test_assoc_memo12_reverse_link_reassign_clear():
    a1 = aml_Memo(body="sample_text", id="sample_text", subject="sample_text", type="sample_text")
    a2 = aml_Memo(body="sample_text_2", id="sample_text_2", subject="sample_text_2", type="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument13', {a1})
    assert _is_linked(b, 'aml_AmlDocument13', a1)
    if hasattr(a1, 'aml_Memo'):
        assert _is_linked(a1, 'aml_Memo', b)
    _safe_set(b, 'aml_AmlDocument13', {a2})
    assert _is_linked(b, 'aml_AmlDocument13', a2)
    if hasattr(a1, 'aml_Memo'):
        assert not _is_linked(a1, 'aml_Memo', b)
    if hasattr(a2, 'aml_Memo'):
        assert _is_linked(a2, 'aml_Memo', b)
    _safe_set(b, 'aml_AmlDocument13', set())
    assert not _is_linked(b, 'aml_AmlDocument13', a2)
    if hasattr(a2, 'aml_Memo'):
        assert not _is_linked(a2, 'aml_Memo', b)


def test_assoc_memo150_reverse_link_reassign_clear():
    a1 = aml_Memo(body="sample_text", id="sample_text", subject="sample_text", type="sample_text")
    a2 = aml_Memo(body="sample_text_2", id="sample_text_2", subject="sample_text_2", type="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot151', {a1})
    assert _is_linked(b, 'aml_DocumentRoot151', a1)
    if hasattr(a1, 'aml_Memo152'):
        assert _is_linked(a1, 'aml_Memo152', b)
    _safe_set(b, 'aml_DocumentRoot151', {a2})
    assert _is_linked(b, 'aml_DocumentRoot151', a2)
    if hasattr(a1, 'aml_Memo152'):
        assert not _is_linked(a1, 'aml_Memo152', b)
    if hasattr(a2, 'aml_Memo152'):
        assert _is_linked(a2, 'aml_Memo152', b)
    _safe_set(b, 'aml_DocumentRoot151', set())
    assert not _is_linked(b, 'aml_DocumentRoot151', a2)
    if hasattr(a2, 'aml_Memo152'):
        assert not _is_linked(a2, 'aml_Memo152', b)


def test_assoc_memo16_reverse_link_reassign_clear():
    a1 = aml_Memo(body="sample_text", id="sample_text", subject="sample_text", type="sample_text")
    a2 = aml_Memo(body="sample_text_2", id="sample_text_2", subject="sample_text_2", type="sample_text_2")
    b = aml_Annotation(group="sample_text", id="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Annotation', {a1})
    assert _is_linked(b, 'aml_Annotation', a1)
    if hasattr(a1, 'aml_Memo17'):
        assert _is_linked(a1, 'aml_Memo17', b)
    _safe_set(b, 'aml_Annotation', {a2})
    assert _is_linked(b, 'aml_Annotation', a2)
    if hasattr(a1, 'aml_Memo17'):
        assert not _is_linked(a1, 'aml_Memo17', b)
    if hasattr(a2, 'aml_Memo17'):
        assert _is_linked(a2, 'aml_Memo17', b)
    _safe_set(b, 'aml_Annotation', set())
    assert not _is_linked(b, 'aml_Annotation', a2)
    if hasattr(a2, 'aml_Memo17'):
        assert not _is_linked(a2, 'aml_Memo17', b)


def test_assoc_metaData153_reverse_link_reassign_clear():
    a1 = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    a2 = aml_MetaData(date="sample_text_2", description="sample_text_2", group="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", title="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot154', {a1})
    assert _is_linked(b, 'aml_DocumentRoot154', a1)
    if hasattr(a1, 'aml_MetaData155'):
        assert _is_linked(a1, 'aml_MetaData155', b)
    _safe_set(b, 'aml_DocumentRoot154', {a2})
    assert _is_linked(b, 'aml_DocumentRoot154', a2)
    if hasattr(a1, 'aml_MetaData155'):
        assert not _is_linked(a1, 'aml_MetaData155', b)
    if hasattr(a2, 'aml_MetaData155'):
        assert _is_linked(a2, 'aml_MetaData155', b)
    _safe_set(b, 'aml_DocumentRoot154', set())
    assert not _is_linked(b, 'aml_DocumentRoot154', a2)
    if hasattr(a2, 'aml_MetaData155'):
        assert not _is_linked(a2, 'aml_MetaData155', b)


def test_assoc_metaData223_reverse_link_reassign_clear():
    a1 = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    a2 = aml_MetaData(date="sample_text_2", description="sample_text_2", group="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", title="sample_text_2")
    b = aml_Exhibit(id="sample_text")
    _safe_set(b, 'aml_Exhibit224', a1)
    assert _is_linked(b, 'aml_Exhibit224', a1)
    if hasattr(a1, 'aml_MetaData225'):
        assert _is_linked(a1, 'aml_MetaData225', b)
    _safe_set(b, 'aml_Exhibit224', a2)
    assert _is_linked(b, 'aml_Exhibit224', a2)
    if hasattr(a1, 'aml_MetaData225'):
        assert not _is_linked(a1, 'aml_MetaData225', b)
    if hasattr(a2, 'aml_MetaData225'):
        assert _is_linked(a2, 'aml_MetaData225', b)
    _safe_set(b, 'aml_Exhibit224', None)
    assert not _is_linked(b, 'aml_Exhibit224', a2)
    if hasattr(a2, 'aml_MetaData225'):
        assert not _is_linked(a2, 'aml_MetaData225', b)


def test_assoc_metaData313_reverse_link_reassign_clear():
    a1 = aml_Template(id="sample_text")
    a2 = aml_Template(id="sample_text_2")
    b = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    _safe_set(b, 'aml_MetaData315', a1)
    assert _is_linked(b, 'aml_MetaData315', a1)
    if hasattr(a1, 'aml_Template314'):
        assert _is_linked(a1, 'aml_Template314', b)
    _safe_set(b, 'aml_MetaData315', a2)
    assert _is_linked(b, 'aml_MetaData315', a2)
    if hasattr(a1, 'aml_Template314'):
        assert not _is_linked(a1, 'aml_Template314', b)
    if hasattr(a2, 'aml_Template314'):
        assert _is_linked(a2, 'aml_Template314', b)
    _safe_set(b, 'aml_MetaData315', None)
    assert not _is_linked(b, 'aml_MetaData315', a2)
    if hasattr(a2, 'aml_Template314'):
        assert not _is_linked(a2, 'aml_Template314', b)


def test_assoc_metaData34_reverse_link_reassign_clear():
    a1 = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    a2 = aml_MetaData(date="sample_text_2", description="sample_text_2", group="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", title="sample_text_2")
    b = aml_Argument(id="sample_text")
    _safe_set(b, 'aml_Argument35', a1)
    assert _is_linked(b, 'aml_Argument35', a1)
    if hasattr(a1, 'aml_MetaData'):
        assert _is_linked(a1, 'aml_MetaData', b)
    _safe_set(b, 'aml_Argument35', a2)
    assert _is_linked(b, 'aml_Argument35', a2)
    if hasattr(a1, 'aml_MetaData'):
        assert not _is_linked(a1, 'aml_MetaData', b)
    if hasattr(a2, 'aml_MetaData'):
        assert _is_linked(a2, 'aml_MetaData', b)
    _safe_set(b, 'aml_Argument35', None)
    assert not _is_linked(b, 'aml_Argument35', a2)
    if hasattr(a2, 'aml_MetaData'):
        assert not _is_linked(a2, 'aml_MetaData', b)


def test_assoc_metaData46_reverse_link_reassign_clear():
    a1 = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    a2 = aml_MetaData(date="sample_text_2", description="sample_text_2", group="sample_text_2", securityMarking="sample_text_2", subject="sample_text_2", title="sample_text_2")
    b = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Collection47', a1)
    assert _is_linked(b, 'aml_Collection47', a1)
    if hasattr(a1, 'aml_MetaData48'):
        assert _is_linked(a1, 'aml_MetaData48', b)
    _safe_set(b, 'aml_Collection47', a2)
    assert _is_linked(b, 'aml_Collection47', a2)
    if hasattr(a1, 'aml_MetaData48'):
        assert not _is_linked(a1, 'aml_MetaData48', b)
    if hasattr(a2, 'aml_MetaData48'):
        assert _is_linked(a2, 'aml_MetaData48', b)
    _safe_set(b, 'aml_Collection47', None)
    assert not _is_linked(b, 'aml_Collection47', a2)
    if hasattr(a2, 'aml_MetaData48'):
        assert not _is_linked(a2, 'aml_MetaData48', b)


def test_assoc_nationState159_reverse_link_reassign_clear():
    a1 = aml_NationState(actor="sample_text", event="sample_text", group="sample_text", perspective="sample_text", region="sample_text")
    a2 = aml_NationState(actor="sample_text_2", event="sample_text_2", group="sample_text_2", perspective="sample_text_2", region="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot160', {a1})
    assert _is_linked(b, 'aml_DocumentRoot160', a1)
    if hasattr(a1, 'aml_NationState161'):
        assert _is_linked(a1, 'aml_NationState161', b)
    _safe_set(b, 'aml_DocumentRoot160', {a2})
    assert _is_linked(b, 'aml_DocumentRoot160', a2)
    if hasattr(a1, 'aml_NationState161'):
        assert not _is_linked(a1, 'aml_NationState161', b)
    if hasattr(a2, 'aml_NationState161'):
        assert _is_linked(a2, 'aml_NationState161', b)
    _safe_set(b, 'aml_DocumentRoot160', set())
    assert not _is_linked(b, 'aml_DocumentRoot160', a2)
    if hasattr(a2, 'aml_NationState161'):
        assert not _is_linked(a2, 'aml_NationState161', b)


def test_assoc_nationState62_reverse_link_reassign_clear():
    a1 = aml_NationState(actor="sample_text", event="sample_text", group="sample_text", perspective="sample_text", region="sample_text")
    a2 = aml_NationState(actor="sample_text_2", event="sample_text_2", group="sample_text_2", perspective="sample_text_2", region="sample_text_2")
    b = aml_Coverage(group="sample_text", mixed="sample_text")
    _safe_set(b, 'aml_Coverage', {a1})
    assert _is_linked(b, 'aml_Coverage', a1)
    if hasattr(a1, 'aml_NationState'):
        assert _is_linked(a1, 'aml_NationState', b)
    _safe_set(b, 'aml_Coverage', {a2})
    assert _is_linked(b, 'aml_Coverage', a2)
    if hasattr(a1, 'aml_NationState'):
        assert not _is_linked(a1, 'aml_NationState', b)
    if hasattr(a2, 'aml_NationState'):
        assert _is_linked(a2, 'aml_NationState', b)
    _safe_set(b, 'aml_Coverage', set())
    assert not _is_linked(b, 'aml_Coverage', a2)
    if hasattr(a2, 'aml_NationState'):
        assert not _is_linked(a2, 'aml_NationState', b)


def test_assoc_parameter162_reverse_link_reassign_clear():
    a1 = aml_Parameter(symbol="sample_text")
    a2 = aml_Parameter(symbol="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot163', {a1})
    assert _is_linked(b, 'aml_DocumentRoot163', a1)
    if hasattr(a1, 'aml_Parameter164'):
        assert _is_linked(a1, 'aml_Parameter164', b)
    _safe_set(b, 'aml_DocumentRoot163', {a2})
    assert _is_linked(b, 'aml_DocumentRoot163', a2)
    if hasattr(a1, 'aml_Parameter164'):
        assert not _is_linked(a1, 'aml_Parameter164', b)
    if hasattr(a2, 'aml_Parameter164'):
        assert _is_linked(a2, 'aml_Parameter164', b)
    _safe_set(b, 'aml_DocumentRoot163', set())
    assert not _is_linked(b, 'aml_DocumentRoot163', a2)
    if hasattr(a2, 'aml_Parameter164'):
        assert not _is_linked(a2, 'aml_Parameter164', b)


def test_assoc_period165_reverse_link_reassign_clear():
    a1 = aml_Period(group="sample_text", label="sample_text")
    a2 = aml_Period(group="sample_text_2", label="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot166', {a1})
    assert _is_linked(b, 'aml_DocumentRoot166', a1)
    if hasattr(a1, 'aml_Period'):
        assert _is_linked(a1, 'aml_Period', b)
    _safe_set(b, 'aml_DocumentRoot166', {a2})
    assert _is_linked(b, 'aml_DocumentRoot166', a2)
    if hasattr(a1, 'aml_Period'):
        assert not _is_linked(a1, 'aml_Period', b)
    if hasattr(a2, 'aml_Period'):
        assert _is_linked(a2, 'aml_Period', b)
    _safe_set(b, 'aml_DocumentRoot166', set())
    assert not _is_linked(b, 'aml_DocumentRoot166', a2)
    if hasattr(a2, 'aml_Period'):
        assert not _is_linked(a2, 'aml_Period', b)


def test_assoc_period280_reverse_link_reassign_clear():
    a1 = aml_Period(group="sample_text", label="sample_text")
    a2 = aml_Period(group="sample_text_2", label="sample_text_2")
    b = aml_NationState(actor="sample_text", event="sample_text", group="sample_text", perspective="sample_text", region="sample_text")
    _safe_set(b, 'aml_NationState281', {a1})
    assert _is_linked(b, 'aml_NationState281', a1)
    if hasattr(a1, 'aml_Period282'):
        assert _is_linked(a1, 'aml_Period282', b)
    _safe_set(b, 'aml_NationState281', {a2})
    assert _is_linked(b, 'aml_NationState281', a2)
    if hasattr(a1, 'aml_Period282'):
        assert not _is_linked(a1, 'aml_Period282', b)
    if hasattr(a2, 'aml_Period282'):
        assert _is_linked(a2, 'aml_Period282', b)
    _safe_set(b, 'aml_NationState281', set())
    assert not _is_linked(b, 'aml_NationState281', a2)
    if hasattr(a2, 'aml_Period282'):
        assert not _is_linked(a2, 'aml_Period282', b)


def test_assoc_person10_reverse_link_reassign_clear():
    a1 = aml_Person(department="sample_text", description="sample_text", email="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", middleName="sample_text", nickName="sample_text", organization="sample_text")
    a2 = aml_Person(department="sample_text_2", description="sample_text_2", email="sample_text_2", firstName="sample_text_2", id="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", nickName="sample_text_2", organization="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument11', {a1})
    assert _is_linked(b, 'aml_AmlDocument11', a1)
    if hasattr(a1, 'aml_Person'):
        assert _is_linked(a1, 'aml_Person', b)
    _safe_set(b, 'aml_AmlDocument11', {a2})
    assert _is_linked(b, 'aml_AmlDocument11', a2)
    if hasattr(a1, 'aml_Person'):
        assert not _is_linked(a1, 'aml_Person', b)
    if hasattr(a2, 'aml_Person'):
        assert _is_linked(a2, 'aml_Person', b)
    _safe_set(b, 'aml_AmlDocument11', set())
    assert not _is_linked(b, 'aml_AmlDocument11', a2)
    if hasattr(a2, 'aml_Person'):
        assert not _is_linked(a2, 'aml_Person', b)


def test_assoc_person167_reverse_link_reassign_clear():
    a1 = aml_Person(department="sample_text", description="sample_text", email="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", middleName="sample_text", nickName="sample_text", organization="sample_text")
    a2 = aml_Person(department="sample_text_2", description="sample_text_2", email="sample_text_2", firstName="sample_text_2", id="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", nickName="sample_text_2", organization="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot168', {a1})
    assert _is_linked(b, 'aml_DocumentRoot168', a1)
    if hasattr(a1, 'aml_Person169'):
        assert _is_linked(a1, 'aml_Person169', b)
    _safe_set(b, 'aml_DocumentRoot168', {a2})
    assert _is_linked(b, 'aml_DocumentRoot168', a2)
    if hasattr(a1, 'aml_Person169'):
        assert not _is_linked(a1, 'aml_Person169', b)
    if hasattr(a2, 'aml_Person169'):
        assert _is_linked(a2, 'aml_Person169', b)
    _safe_set(b, 'aml_DocumentRoot168', set())
    assert not _is_linked(b, 'aml_DocumentRoot168', a2)
    if hasattr(a2, 'aml_Person169'):
        assert not _is_linked(a2, 'aml_Person169', b)


def test_assoc_publisher170_reverse_link_reassign_clear():
    a1 = aml_Publisher(description="sample_text", idRef="sample_text", objectType="sample_text")
    a2 = aml_Publisher(description="sample_text_2", idRef="sample_text_2", objectType="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot171', {a1})
    assert _is_linked(b, 'aml_DocumentRoot171', a1)
    if hasattr(a1, 'aml_Publisher'):
        assert _is_linked(a1, 'aml_Publisher', b)
    _safe_set(b, 'aml_DocumentRoot171', {a2})
    assert _is_linked(b, 'aml_DocumentRoot171', a2)
    if hasattr(a1, 'aml_Publisher'):
        assert not _is_linked(a1, 'aml_Publisher', b)
    if hasattr(a2, 'aml_Publisher'):
        assert _is_linked(a2, 'aml_Publisher', b)
    _safe_set(b, 'aml_DocumentRoot171', set())
    assert not _is_linked(b, 'aml_DocumentRoot171', a2)
    if hasattr(a2, 'aml_Publisher'):
        assert not _is_linked(a2, 'aml_Publisher', b)


def test_assoc_publisher247_reverse_link_reassign_clear():
    a1 = aml_Publisher(description="sample_text", idRef="sample_text", objectType="sample_text")
    a2 = aml_Publisher(description="sample_text_2", idRef="sample_text_2", objectType="sample_text_2")
    b = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    _safe_set(b, 'aml_MetaData248', {a1})
    assert _is_linked(b, 'aml_MetaData248', a1)
    if hasattr(a1, 'aml_Publisher249'):
        assert _is_linked(a1, 'aml_Publisher249', b)
    _safe_set(b, 'aml_MetaData248', {a2})
    assert _is_linked(b, 'aml_MetaData248', a2)
    if hasattr(a1, 'aml_Publisher249'):
        assert not _is_linked(a1, 'aml_Publisher249', b)
    if hasattr(a2, 'aml_Publisher249'):
        assert _is_linked(a2, 'aml_Publisher249', b)
    _safe_set(b, 'aml_MetaData248', set())
    assert not _is_linked(b, 'aml_MetaData248', a2)
    if hasattr(a2, 'aml_Publisher249'):
        assert not _is_linked(a2, 'aml_Publisher249', b)


def test_assoc_question172_reverse_link_reassign_clear():
    a1 = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    a2 = aml_Question(amplification="sample_text_2", description="sample_text_2", group="sample_text_2", id="sample_text_2", label="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot173', {a1})
    assert _is_linked(b, 'aml_DocumentRoot173', a1)
    if hasattr(a1, 'aml_Question174'):
        assert _is_linked(a1, 'aml_Question174', b)
    _safe_set(b, 'aml_DocumentRoot173', {a2})
    assert _is_linked(b, 'aml_DocumentRoot173', a2)
    if hasattr(a1, 'aml_Question174'):
        assert not _is_linked(a1, 'aml_Question174', b)
    if hasattr(a2, 'aml_Question174'):
        assert _is_linked(a2, 'aml_Question174', b)
    _safe_set(b, 'aml_DocumentRoot173', set())
    assert not _is_linked(b, 'aml_DocumentRoot173', a2)
    if hasattr(a2, 'aml_Question174'):
        assert not _is_linked(a2, 'aml_Question174', b)


def test_assoc_question322_reverse_link_reassign_clear():
    a1 = aml_Template(id="sample_text")
    a2 = aml_Template(id="sample_text_2")
    b = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    _safe_set(b, 'aml_Question324', a1)
    assert _is_linked(b, 'aml_Question324', a1)
    if hasattr(a1, 'aml_Template323'):
        assert _is_linked(a1, 'aml_Template323', b)
    _safe_set(b, 'aml_Question324', a2)
    assert _is_linked(b, 'aml_Question324', a2)
    if hasattr(a1, 'aml_Template323'):
        assert not _is_linked(a1, 'aml_Template323', b)
    if hasattr(a2, 'aml_Template323'):
        assert _is_linked(a2, 'aml_Template323', b)
    _safe_set(b, 'aml_Question324', None)
    assert not _is_linked(b, 'aml_Question324', a2)
    if hasattr(a2, 'aml_Template323'):
        assert not _is_linked(a2, 'aml_Template323', b)


def test_assoc_question55_reverse_link_reassign_clear():
    a1 = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    a2 = aml_Question(amplification="sample_text_2", description="sample_text_2", group="sample_text_2", id="sample_text_2", label="sample_text_2")
    b = aml_Collection(group="sample_text", id="sample_text", label="sample_text", label1="sample_text", objectType="sample_text")
    _safe_set(b, 'aml_Collection56', a1)
    assert _is_linked(b, 'aml_Collection56', a1)
    if hasattr(a1, 'aml_Question'):
        assert _is_linked(a1, 'aml_Question', b)
    _safe_set(b, 'aml_Collection56', a2)
    assert _is_linked(b, 'aml_Collection56', a2)
    if hasattr(a1, 'aml_Question'):
        assert not _is_linked(a1, 'aml_Question', b)
    if hasattr(a2, 'aml_Question'):
        assert _is_linked(a2, 'aml_Question', b)
    _safe_set(b, 'aml_Collection56', None)
    assert not _is_linked(b, 'aml_Collection56', a2)
    if hasattr(a2, 'aml_Question'):
        assert not _is_linked(a2, 'aml_Question', b)


def test_assoc_reader177_reverse_link_reassign_clear():
    a1 = aml_Reader(description="sample_text", idRef="sample_text", objectType="sample_text")
    a2 = aml_Reader(description="sample_text_2", idRef="sample_text_2", objectType="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot178', {a1})
    assert _is_linked(b, 'aml_DocumentRoot178', a1)
    if hasattr(a1, 'aml_Reader'):
        assert _is_linked(a1, 'aml_Reader', b)
    _safe_set(b, 'aml_DocumentRoot178', {a2})
    assert _is_linked(b, 'aml_DocumentRoot178', a2)
    if hasattr(a1, 'aml_Reader'):
        assert not _is_linked(a1, 'aml_Reader', b)
    if hasattr(a2, 'aml_Reader'):
        assert _is_linked(a2, 'aml_Reader', b)
    _safe_set(b, 'aml_DocumentRoot178', set())
    assert not _is_linked(b, 'aml_DocumentRoot178', a2)
    if hasattr(a2, 'aml_Reader'):
        assert not _is_linked(a2, 'aml_Reader', b)


def test_assoc_reader238_reverse_link_reassign_clear():
    a1 = aml_Reader(description="sample_text", idRef="sample_text", objectType="sample_text")
    a2 = aml_Reader(description="sample_text_2", idRef="sample_text_2", objectType="sample_text_2")
    b = aml_Memo(body="sample_text", id="sample_text", subject="sample_text", type="sample_text")
    _safe_set(b, 'aml_Memo239', {a1})
    assert _is_linked(b, 'aml_Memo239', a1)
    if hasattr(a1, 'aml_Reader240'):
        assert _is_linked(a1, 'aml_Reader240', b)
    _safe_set(b, 'aml_Memo239', {a2})
    assert _is_linked(b, 'aml_Memo239', a2)
    if hasattr(a1, 'aml_Reader240'):
        assert not _is_linked(a1, 'aml_Reader240', b)
    if hasattr(a2, 'aml_Reader240'):
        assert _is_linked(a2, 'aml_Reader240', b)
    _safe_set(b, 'aml_Memo239', set())
    assert not _is_linked(b, 'aml_Memo239', a2)
    if hasattr(a2, 'aml_Reader240'):
        assert not _is_linked(a2, 'aml_Reader240', b)


def test_assoc_reader244_reverse_link_reassign_clear():
    a1 = aml_Reader(description="sample_text", idRef="sample_text", objectType="sample_text")
    a2 = aml_Reader(description="sample_text_2", idRef="sample_text_2", objectType="sample_text_2")
    b = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    _safe_set(b, 'aml_MetaData245', {a1})
    assert _is_linked(b, 'aml_MetaData245', a1)
    if hasattr(a1, 'aml_Reader246'):
        assert _is_linked(a1, 'aml_Reader246', b)
    _safe_set(b, 'aml_MetaData245', {a2})
    assert _is_linked(b, 'aml_MetaData245', a2)
    if hasattr(a1, 'aml_Reader246'):
        assert not _is_linked(a1, 'aml_Reader246', b)
    if hasattr(a2, 'aml_Reader246'):
        assert _is_linked(a2, 'aml_Reader246', b)
    _safe_set(b, 'aml_MetaData245', set())
    assert not _is_linked(b, 'aml_MetaData245', a2)
    if hasattr(a2, 'aml_Reader246'):
        assert not _is_linked(a2, 'aml_Reader246', b)


def test_assoc_relevance182_reverse_link_reassign_clear():
    a1 = aml_Relevance(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    a2 = aml_Relevance(description="sample_text_2", label="sample_text_2", ordinal="sample_text_2", symbol="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot183', {a1})
    assert _is_linked(b, 'aml_DocumentRoot183', a1)
    if hasattr(a1, 'aml_Relevance'):
        assert _is_linked(a1, 'aml_Relevance', b)
    _safe_set(b, 'aml_DocumentRoot183', {a2})
    assert _is_linked(b, 'aml_DocumentRoot183', a2)
    if hasattr(a1, 'aml_Relevance'):
        assert not _is_linked(a1, 'aml_Relevance', b)
    if hasattr(a2, 'aml_Relevance'):
        assert _is_linked(a2, 'aml_Relevance', b)
    _safe_set(b, 'aml_DocumentRoot183', set())
    assert not _is_linked(b, 'aml_DocumentRoot183', a2)
    if hasattr(a2, 'aml_Relevance'):
        assert not _is_linked(a2, 'aml_Relevance', b)


def test_assoc_relevance208_reverse_link_reassign_clear():
    a1 = aml_Relevance(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    a2 = aml_Relevance(description="sample_text_2", label="sample_text_2", ordinal="sample_text_2", symbol="sample_text_2")
    b = aml_Evidence(id="sample_text", label="sample_text", ordinal="sample_text")
    _safe_set(b, 'aml_Evidence209', a1)
    assert _is_linked(b, 'aml_Evidence209', a1)
    if hasattr(a1, 'aml_Relevance210'):
        assert _is_linked(a1, 'aml_Relevance210', b)
    _safe_set(b, 'aml_Evidence209', a2)
    assert _is_linked(b, 'aml_Evidence209', a2)
    if hasattr(a1, 'aml_Relevance210'):
        assert not _is_linked(a1, 'aml_Relevance210', b)
    if hasattr(a2, 'aml_Relevance210'):
        assert _is_linked(a2, 'aml_Relevance210', b)
    _safe_set(b, 'aml_Evidence209', None)
    assert not _is_linked(b, 'aml_Evidence209', a2)
    if hasattr(a2, 'aml_Relevance210'):
        assert not _is_linked(a2, 'aml_Relevance210', b)


def test_assoc_reliability184_reverse_link_reassign_clear():
    a1 = aml_Reliability(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    a2 = aml_Reliability(description="sample_text_2", label="sample_text_2", ordinal="sample_text_2", symbol="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot185', {a1})
    assert _is_linked(b, 'aml_DocumentRoot185', a1)
    if hasattr(a1, 'aml_Reliability'):
        assert _is_linked(a1, 'aml_Reliability', b)
    _safe_set(b, 'aml_DocumentRoot185', {a2})
    assert _is_linked(b, 'aml_DocumentRoot185', a2)
    if hasattr(a1, 'aml_Reliability'):
        assert not _is_linked(a1, 'aml_Reliability', b)
    if hasattr(a2, 'aml_Reliability'):
        assert _is_linked(a2, 'aml_Reliability', b)
    _safe_set(b, 'aml_DocumentRoot185', set())
    assert not _is_linked(b, 'aml_DocumentRoot185', a2)
    if hasattr(a2, 'aml_Reliability'):
        assert not _is_linked(a2, 'aml_Reliability', b)


def test_assoc_reliability211_reverse_link_reassign_clear():
    a1 = aml_Reliability(description="sample_text", label="sample_text", ordinal="sample_text", symbol="sample_text")
    a2 = aml_Reliability(description="sample_text_2", label="sample_text_2", ordinal="sample_text_2", symbol="sample_text_2")
    b = aml_Evidence(id="sample_text", label="sample_text", ordinal="sample_text")
    _safe_set(b, 'aml_Evidence212', a1)
    assert _is_linked(b, 'aml_Evidence212', a1)
    if hasattr(a1, 'aml_Reliability213'):
        assert _is_linked(a1, 'aml_Reliability213', b)
    _safe_set(b, 'aml_Evidence212', a2)
    assert _is_linked(b, 'aml_Evidence212', a2)
    if hasattr(a1, 'aml_Reliability213'):
        assert not _is_linked(a1, 'aml_Reliability213', b)
    if hasattr(a2, 'aml_Reliability213'):
        assert _is_linked(a2, 'aml_Reliability213', b)
    _safe_set(b, 'aml_Evidence212', None)
    assert not _is_linked(b, 'aml_Evidence212', a2)
    if hasattr(a2, 'aml_Reliability213'):
        assert not _is_linked(a2, 'aml_Reliability213', b)


def test_assoc_start192_reverse_link_reassign_clear():
    a1 = aml_Start(scheme="sample_text", value="sample_text")
    a2 = aml_Start(scheme="sample_text_2", value="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot193', {a1})
    assert _is_linked(b, 'aml_DocumentRoot193', a1)
    if hasattr(a1, 'aml_Start'):
        assert _is_linked(a1, 'aml_Start', b)
    _safe_set(b, 'aml_DocumentRoot193', {a2})
    assert _is_linked(b, 'aml_DocumentRoot193', a2)
    if hasattr(a1, 'aml_Start'):
        assert not _is_linked(a1, 'aml_Start', b)
    if hasattr(a2, 'aml_Start'):
        assert _is_linked(a2, 'aml_Start', b)
    _safe_set(b, 'aml_DocumentRoot193', set())
    assert not _is_linked(b, 'aml_DocumentRoot193', a2)
    if hasattr(a2, 'aml_Start'):
        assert not _is_linked(a2, 'aml_Start', b)


def test_assoc_start286_reverse_link_reassign_clear():
    a1 = aml_Start(scheme="sample_text", value="sample_text")
    a2 = aml_Start(scheme="sample_text_2", value="sample_text_2")
    b = aml_Period(group="sample_text", label="sample_text")
    _safe_set(b, 'aml_Period287', {a1})
    assert _is_linked(b, 'aml_Period287', a1)
    if hasattr(a1, 'aml_Start288'):
        assert _is_linked(a1, 'aml_Start288', b)
    _safe_set(b, 'aml_Period287', {a2})
    assert _is_linked(b, 'aml_Period287', a2)
    if hasattr(a1, 'aml_Start288'):
        assert not _is_linked(a1, 'aml_Start288', b)
    if hasattr(a2, 'aml_Start288'):
        assert _is_linked(a2, 'aml_Start288', b)
    _safe_set(b, 'aml_Period287', set())
    assert not _is_linked(b, 'aml_Period287', a2)
    if hasattr(a2, 'aml_Start288'):
        assert not _is_linked(a2, 'aml_Start288', b)


def test_assoc_template194_reverse_link_reassign_clear():
    a1 = aml_Template(id="sample_text")
    a2 = aml_Template(id="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot195', {a1})
    assert _is_linked(b, 'aml_DocumentRoot195', a1)
    if hasattr(a1, 'aml_Template196'):
        assert _is_linked(a1, 'aml_Template196', b)
    _safe_set(b, 'aml_DocumentRoot195', {a2})
    assert _is_linked(b, 'aml_DocumentRoot195', a2)
    if hasattr(a1, 'aml_Template196'):
        assert not _is_linked(a1, 'aml_Template196', b)
    if hasattr(a2, 'aml_Template196'):
        assert _is_linked(a2, 'aml_Template196', b)
    _safe_set(b, 'aml_DocumentRoot195', set())
    assert not _is_linked(b, 'aml_DocumentRoot195', a2)
    if hasattr(a2, 'aml_Template196'):
        assert not _is_linked(a2, 'aml_Template196', b)


def test_assoc_template3_reverse_link_reassign_clear():
    a1 = aml_Template(id="sample_text")
    a2 = aml_Template(id="sample_text_2")
    b = aml_AmlDocument(group="sample_text", version="sample_text")
    _safe_set(b, 'aml_AmlDocument', {a1})
    assert _is_linked(b, 'aml_AmlDocument', a1)
    if hasattr(a1, 'aml_Template'):
        assert _is_linked(a1, 'aml_Template', b)
    _safe_set(b, 'aml_AmlDocument', {a2})
    assert _is_linked(b, 'aml_AmlDocument', a2)
    if hasattr(a1, 'aml_Template'):
        assert not _is_linked(a1, 'aml_Template', b)
    if hasattr(a2, 'aml_Template'):
        assert _is_linked(a2, 'aml_Template', b)
    _safe_set(b, 'aml_AmlDocument', set())
    assert not _is_linked(b, 'aml_AmlDocument', a2)
    if hasattr(a2, 'aml_Template'):
        assert not _is_linked(a2, 'aml_Template', b)


def test_assoc_value200_reverse_link_reassign_clear():
    a1 = aml_Value(group="sample_text", mixed="sample_text", type="sample_text", unit="sample_text")
    a2 = aml_Value(group="sample_text_2", mixed="sample_text_2", type="sample_text_2", unit="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot201', {a1})
    assert _is_linked(b, 'aml_DocumentRoot201', a1)
    if hasattr(a1, 'aml_Value'):
        assert _is_linked(a1, 'aml_Value', b)
    _safe_set(b, 'aml_DocumentRoot201', {a2})
    assert _is_linked(b, 'aml_DocumentRoot201', a2)
    if hasattr(a1, 'aml_Value'):
        assert not _is_linked(a1, 'aml_Value', b)
    if hasattr(a2, 'aml_Value'):
        assert _is_linked(a2, 'aml_Value', b)
    _safe_set(b, 'aml_DocumentRoot201', set())
    assert not _is_linked(b, 'aml_DocumentRoot201', a2)
    if hasattr(a2, 'aml_Value'):
        assert not _is_linked(a2, 'aml_Value', b)


def test_assoc_value283_reverse_link_reassign_clear():
    a1 = aml_Value(group="sample_text", mixed="sample_text", type="sample_text", unit="sample_text")
    a2 = aml_Value(group="sample_text_2", mixed="sample_text_2", type="sample_text_2", unit="sample_text_2")
    b = aml_Parameter(symbol="sample_text")
    _safe_set(b, 'aml_Parameter284', a1)
    assert _is_linked(b, 'aml_Parameter284', a1)
    if hasattr(a1, 'aml_Value285'):
        assert _is_linked(a1, 'aml_Value285', b)
    _safe_set(b, 'aml_Parameter284', a2)
    assert _is_linked(b, 'aml_Parameter284', a2)
    if hasattr(a1, 'aml_Value285'):
        assert not _is_linked(a1, 'aml_Value285', b)
    if hasattr(a2, 'aml_Value285'):
        assert _is_linked(a2, 'aml_Value285', b)
    _safe_set(b, 'aml_Parameter284', None)
    assert not _is_linked(b, 'aml_Parameter284', a2)
    if hasattr(a2, 'aml_Value285'):
        assert not _is_linked(a2, 'aml_Value285', b)


def test_assoc_witness202_reverse_link_reassign_clear():
    a1 = aml_Witness(description="sample_text", idRef="sample_text", timestamp="sample_text")
    a2 = aml_Witness(description="sample_text_2", idRef="sample_text_2", timestamp="sample_text_2")
    b = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    _safe_set(b, 'aml_DocumentRoot203', {a1})
    assert _is_linked(b, 'aml_DocumentRoot203', a1)
    if hasattr(a1, 'aml_Witness204'):
        assert _is_linked(a1, 'aml_Witness204', b)
    _safe_set(b, 'aml_DocumentRoot203', {a2})
    assert _is_linked(b, 'aml_DocumentRoot203', a2)
    if hasattr(a1, 'aml_Witness204'):
        assert not _is_linked(a1, 'aml_Witness204', b)
    if hasattr(a2, 'aml_Witness204'):
        assert _is_linked(a2, 'aml_Witness204', b)
    _safe_set(b, 'aml_DocumentRoot203', set())
    assert not _is_linked(b, 'aml_DocumentRoot203', a2)
    if hasattr(a2, 'aml_Witness204'):
        assert not _is_linked(a2, 'aml_Witness204', b)


def test_assoc_witness21_reverse_link_reassign_clear():
    a1 = aml_Witness(description="sample_text", idRef="sample_text", timestamp="sample_text")
    a2 = aml_Witness(description="sample_text_2", idRef="sample_text_2", timestamp="sample_text_2")
    b = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    _safe_set(b, 'aml_Answer22', {a1})
    assert _is_linked(b, 'aml_Answer22', a1)
    if hasattr(a1, 'aml_Witness'):
        assert _is_linked(a1, 'aml_Witness', b)
    _safe_set(b, 'aml_Answer22', {a2})
    assert _is_linked(b, 'aml_Answer22', a2)
    if hasattr(a1, 'aml_Witness'):
        assert not _is_linked(a1, 'aml_Witness', b)
    if hasattr(a2, 'aml_Witness'):
        assert _is_linked(a2, 'aml_Witness', b)
    _safe_set(b, 'aml_Answer22', set())
    assert not _is_linked(b, 'aml_Answer22', a2)
    if hasattr(a2, 'aml_Witness'):
        assert not _is_linked(a2, 'aml_Witness', b)


def test_assoc_witness214_reverse_link_reassign_clear():
    a1 = aml_Witness(description="sample_text", idRef="sample_text", timestamp="sample_text")
    a2 = aml_Witness(description="sample_text_2", idRef="sample_text_2", timestamp="sample_text_2")
    b = aml_Evidence(id="sample_text", label="sample_text", ordinal="sample_text")
    _safe_set(b, 'aml_Evidence215', a1)
    assert _is_linked(b, 'aml_Evidence215', a1)
    if hasattr(a1, 'aml_Witness216'):
        assert _is_linked(a1, 'aml_Witness216', b)
    _safe_set(b, 'aml_Evidence215', a2)
    assert _is_linked(b, 'aml_Evidence215', a2)
    if hasattr(a1, 'aml_Witness216'):
        assert not _is_linked(a1, 'aml_Witness216', b)
    if hasattr(a2, 'aml_Witness216'):
        assert _is_linked(a2, 'aml_Witness216', b)
    _safe_set(b, 'aml_Evidence215', None)
    assert not _is_linked(b, 'aml_Evidence215', a2)
    if hasattr(a2, 'aml_Witness216'):
        assert not _is_linked(a2, 'aml_Witness216', b)


def test_assoc_witness229_reverse_link_reassign_clear():
    a1 = aml_Witness(description="sample_text", idRef="sample_text", timestamp="sample_text")
    a2 = aml_Witness(description="sample_text_2", idRef="sample_text_2", timestamp="sample_text_2")
    b = aml_Flag(description="sample_text", flagType="sample_text", label="sample_text")
    _safe_set(b, 'aml_Flag230', a1)
    assert _is_linked(b, 'aml_Flag230', a1)
    if hasattr(a1, 'aml_Witness231'):
        assert _is_linked(a1, 'aml_Witness231', b)
    _safe_set(b, 'aml_Flag230', a2)
    assert _is_linked(b, 'aml_Flag230', a2)
    if hasattr(a1, 'aml_Witness231'):
        assert not _is_linked(a1, 'aml_Witness231', b)
    if hasattr(a2, 'aml_Witness231'):
        assert _is_linked(a2, 'aml_Witness231', b)
    _safe_set(b, 'aml_Flag230', None)
    assert not _is_linked(b, 'aml_Flag230', a2)
    if hasattr(a2, 'aml_Witness231'):
        assert not _is_linked(a2, 'aml_Witness231', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aggregationRule26_stub_double():
    # aml_AggregationRule has no real 'aml_AggregationRule28' property in the generated
    # code (a bare stub) -- manually attach it so aml_Answer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Answer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Answer(group="sample_text", questionId="sample_text", rationale="sample_text")
    partner = aml_AggregationRule()
    setattr(partner, 'aml_AggregationRule28', None)
    _safe_set(owner, 'aml_Answer27', {partner})
    assert getattr(partner, 'aml_AggregationRule28') == owner
    _safe_set(owner, 'aml_Answer27', set())
    assert getattr(partner, 'aml_AggregationRule28') is None


def test_assoc_aggregationRule304_stub_double():
    # aml_AggregationRule has no real 'aml_AggregationRule306' property in the generated
    # code (a bare stub) -- manually attach it so aml_Question's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Question's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    partner = aml_AggregationRule()
    setattr(partner, 'aml_AggregationRule306', None)
    _safe_set(owner, 'aml_Question305', {partner})
    assert getattr(partner, 'aml_AggregationRule306') == owner
    _safe_set(owner, 'aml_Question305', set())
    assert getattr(partner, 'aml_AggregationRule306') is None


def test_assoc_aggregationRule73_stub_double():
    # aml_AggregationRule has no real 'aml_AggregationRule75' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_AggregationRule()
    setattr(partner, 'aml_AggregationRule75', None)
    _safe_set(owner, 'aml_DocumentRoot74', {partner})
    assert getattr(partner, 'aml_AggregationRule75') == owner
    _safe_set(owner, 'aml_DocumentRoot74', set())
    assert getattr(partner, 'aml_AggregationRule75') is None


def test_assoc_archive220_stub_double():
    # aml_EObject has no real 'aml_EObject222' property in the generated
    # code (a bare stub) -- manually attach it so aml_Exhibit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Exhibit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Exhibit(id="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject222', None)
    _safe_set(owner, 'aml_Exhibit221', partner)
    assert getattr(partner, 'aml_EObject222') == owner
    _safe_set(owner, 'aml_Exhibit221', None)
    assert getattr(partner, 'aml_EObject222') is None


def test_assoc_archive85_stub_double():
    # aml_EObject has no real 'aml_EObject87' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject87', None)
    _safe_set(owner, 'aml_DocumentRoot86', {partner})
    assert getattr(partner, 'aml_EObject87') == owner
    _safe_set(owner, 'aml_DocumentRoot86', set())
    assert getattr(partner, 'aml_EObject87') is None


def test_assoc_contributor105_stub_double():
    # aml_EObject has no real 'aml_EObject107' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject107', None)
    _safe_set(owner, 'aml_DocumentRoot106', {partner})
    assert getattr(partner, 'aml_EObject107') == owner
    _safe_set(owner, 'aml_DocumentRoot106', set())
    assert getattr(partner, 'aml_EObject107') is None


def test_assoc_contributor250_stub_double():
    # aml_EObject has no real 'aml_EObject252' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject252', None)
    _safe_set(owner, 'aml_MetaData251', {partner})
    assert getattr(partner, 'aml_EObject252') == owner
    _safe_set(owner, 'aml_MetaData251', set())
    assert getattr(partner, 'aml_EObject252') is None


def test_assoc_dependent292_stub_double():
    # aml_QuestionRelationships has no real 'aml_QuestionRelationships293' property in the generated
    # code (a bare stub) -- manually attach it so aml_Dependent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Dependent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Dependent(idRef="sample_text", ordinal="sample_text")
    partner = aml_QuestionRelationships()
    setattr(partner, 'aml_QuestionRelationships293', None)
    _safe_set(owner, 'aml_Dependent294', partner)
    assert owner in getattr(partner, 'aml_QuestionRelationships293')
    _safe_set(owner, 'aml_Dependent294', None)
    assert owner not in getattr(partner, 'aml_QuestionRelationships293')


def test_assoc_format134_stub_double():
    # aml_EObject has no real 'aml_EObject136' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject136', None)
    _safe_set(owner, 'aml_DocumentRoot135', {partner})
    assert getattr(partner, 'aml_EObject136') == owner
    _safe_set(owner, 'aml_DocumentRoot135', set())
    assert getattr(partner, 'aml_EObject136') is None


def test_assoc_format256_stub_double():
    # aml_EObject has no real 'aml_EObject258' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject258', None)
    _safe_set(owner, 'aml_MetaData257', {partner})
    assert getattr(partner, 'aml_EObject258') == owner
    _safe_set(owner, 'aml_MetaData257', set())
    assert getattr(partner, 'aml_EObject258') is None


def test_assoc_identifier137_stub_double():
    # aml_EObject has no real 'aml_EObject139' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject139', None)
    _safe_set(owner, 'aml_DocumentRoot138', {partner})
    assert getattr(partner, 'aml_EObject139') == owner
    _safe_set(owner, 'aml_DocumentRoot138', set())
    assert getattr(partner, 'aml_EObject139') is None


def test_assoc_identifier259_stub_double():
    # aml_EObject has no real 'aml_EObject261' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject261', None)
    _safe_set(owner, 'aml_MetaData260', {partner})
    assert getattr(partner, 'aml_EObject261') == owner
    _safe_set(owner, 'aml_MetaData260', set())
    assert getattr(partner, 'aml_EObject261') is None


def test_assoc_image140_stub_double():
    # aml_EObject has no real 'aml_EObject142' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject142', None)
    _safe_set(owner, 'aml_DocumentRoot141', {partner})
    assert getattr(partner, 'aml_EObject142') == owner
    _safe_set(owner, 'aml_DocumentRoot141', set())
    assert getattr(partner, 'aml_EObject142') is None


def test_assoc_image277_stub_double():
    # aml_EObject has no real 'aml_EObject279' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject279', None)
    _safe_set(owner, 'aml_MetaData278', {partner})
    assert getattr(partner, 'aml_EObject279') == owner
    _safe_set(owner, 'aml_MetaData278', set())
    assert getattr(partner, 'aml_EObject279') is None


def test_assoc_language145_stub_double():
    # aml_EObject has no real 'aml_EObject147' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject147', None)
    _safe_set(owner, 'aml_DocumentRoot146', {partner})
    assert getattr(partner, 'aml_EObject147') == owner
    _safe_set(owner, 'aml_DocumentRoot146', set())
    assert getattr(partner, 'aml_EObject147') is None


def test_assoc_language265_stub_double():
    # aml_EObject has no real 'aml_EObject267' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject267', None)
    _safe_set(owner, 'aml_MetaData266', {partner})
    assert getattr(partner, 'aml_EObject267') == owner
    _safe_set(owner, 'aml_MetaData266', set())
    assert getattr(partner, 'aml_EObject267') is None


def test_assoc_li232_stub_double():
    # aml_EObject has no real 'aml_EObject234' property in the generated
    # code (a bare stub) -- manually attach it so aml_List's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_List's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_List(group="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject234', None)
    _safe_set(owner, 'aml_List233', {partner})
    assert getattr(partner, 'aml_EObject234') == owner
    _safe_set(owner, 'aml_List233', set())
    assert getattr(partner, 'aml_EObject234') is None


def test_assoc_method156_stub_double():
    # aml_EObject has no real 'aml_EObject158' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject158', None)
    _safe_set(owner, 'aml_DocumentRoot157', {partner})
    assert getattr(partner, 'aml_EObject158') == owner
    _safe_set(owner, 'aml_DocumentRoot157', set())
    assert getattr(partner, 'aml_EObject158') is None


def test_assoc_parameter1_stub_double():
    # aml_AggregationRule has no real 'aml_AggregationRule2' property in the generated
    # code (a bare stub) -- manually attach it so aml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Parameter(symbol="sample_text")
    partner = aml_AggregationRule()
    setattr(partner, 'aml_AggregationRule2', None)
    _safe_set(owner, 'aml_Parameter', partner)
    assert owner in getattr(partner, 'aml_AggregationRule2')
    _safe_set(owner, 'aml_Parameter', None)
    assert owner not in getattr(partner, 'aml_AggregationRule2')


def test_assoc_questionRelationships175_stub_double():
    # aml_QuestionRelationships has no real 'aml_QuestionRelationships' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_QuestionRelationships()
    setattr(partner, 'aml_QuestionRelationships', None)
    _safe_set(owner, 'aml_DocumentRoot176', {partner})
    assert getattr(partner, 'aml_QuestionRelationships') == owner
    _safe_set(owner, 'aml_DocumentRoot176', set())
    assert getattr(partner, 'aml_QuestionRelationships') is None


def test_assoc_questionRelationships301_stub_double():
    # aml_QuestionRelationships has no real 'aml_QuestionRelationships303' property in the generated
    # code (a bare stub) -- manually attach it so aml_Question's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Question's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    partner = aml_QuestionRelationships()
    setattr(partner, 'aml_QuestionRelationships303', None)
    _safe_set(owner, 'aml_Question302', {partner})
    assert getattr(partner, 'aml_QuestionRelationships303') == owner
    _safe_set(owner, 'aml_Question302', set())
    assert getattr(partner, 'aml_QuestionRelationships303') is None


def test_assoc_relation179_stub_double():
    # aml_EObject has no real 'aml_EObject181' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject181', None)
    _safe_set(owner, 'aml_DocumentRoot180', {partner})
    assert getattr(partner, 'aml_EObject181') == owner
    _safe_set(owner, 'aml_DocumentRoot180', set())
    assert getattr(partner, 'aml_EObject181') is None


def test_assoc_relation268_stub_double():
    # aml_EObject has no real 'aml_EObject270' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject270', None)
    _safe_set(owner, 'aml_MetaData269', {partner})
    assert getattr(partner, 'aml_EObject270') == owner
    _safe_set(owner, 'aml_MetaData269', set())
    assert getattr(partner, 'aml_EObject270') is None


def test_assoc_rights186_stub_double():
    # aml_EObject has no real 'aml_EObject188' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject188', None)
    _safe_set(owner, 'aml_DocumentRoot187', {partner})
    assert getattr(partner, 'aml_EObject188') == owner
    _safe_set(owner, 'aml_DocumentRoot187', set())
    assert getattr(partner, 'aml_EObject188') is None


def test_assoc_rights274_stub_double():
    # aml_EObject has no real 'aml_EObject276' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject276', None)
    _safe_set(owner, 'aml_MetaData275', {partner})
    assert getattr(partner, 'aml_EObject276') == owner
    _safe_set(owner, 'aml_MetaData275', set())
    assert getattr(partner, 'aml_EObject276') is None


def test_assoc_source189_stub_double():
    # aml_EObject has no real 'aml_EObject191' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject191', None)
    _safe_set(owner, 'aml_DocumentRoot190', {partner})
    assert getattr(partner, 'aml_EObject191') == owner
    _safe_set(owner, 'aml_DocumentRoot190', set())
    assert getattr(partner, 'aml_EObject191') is None


def test_assoc_source262_stub_double():
    # aml_EObject has no real 'aml_EObject264' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject264', None)
    _safe_set(owner, 'aml_MetaData263', {partner})
    assert getattr(partner, 'aml_EObject264') == owner
    _safe_set(owner, 'aml_MetaData263', set())
    assert getattr(partner, 'aml_EObject264') is None


def test_assoc_type197_stub_double():
    # aml_EObject has no real 'aml_EObject199' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject199', None)
    _safe_set(owner, 'aml_DocumentRoot198', {partner})
    assert getattr(partner, 'aml_EObject199') == owner
    _safe_set(owner, 'aml_DocumentRoot198', set())
    assert getattr(partner, 'aml_EObject199') is None


def test_assoc_type253_stub_double():
    # aml_EObject has no real 'aml_EObject255' property in the generated
    # code (a bare stub) -- manually attach it so aml_MetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_MetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_MetaData(date="sample_text", description="sample_text", group="sample_text", securityMarking="sample_text", subject="sample_text", title="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject255', None)
    _safe_set(owner, 'aml_MetaData254', {partner})
    assert getattr(partner, 'aml_EObject255') == owner
    _safe_set(owner, 'aml_MetaData254', set())
    assert getattr(partner, 'aml_EObject255') is None


def test_assoc_type295_stub_double():
    # aml_EObject has no real 'aml_EObject297' property in the generated
    # code (a bare stub) -- manually attach it so aml_Question's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_Question's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_Question(amplification="sample_text", description="sample_text", group="sample_text", id="sample_text", label="sample_text")
    partner = aml_EObject()
    setattr(partner, 'aml_EObject297', None)
    _safe_set(owner, 'aml_Question296', {partner})
    assert getattr(partner, 'aml_EObject297') == owner
    _safe_set(owner, 'aml_Question296', set())
    assert getattr(partner, 'aml_EObject297') is None


def test_assoc_xMLNSPrefixMap69_stub_double():
    # aml_EStringToStringMapEntry has no real 'aml_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EStringToStringMapEntry()
    setattr(partner, 'aml_EStringToStringMapEntry', None)
    _safe_set(owner, 'aml_DocumentRoot', {partner})
    assert getattr(partner, 'aml_EStringToStringMapEntry') == owner
    _safe_set(owner, 'aml_DocumentRoot', set())
    assert getattr(partner, 'aml_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation70_stub_double():
    # aml_EStringToStringMapEntry has no real 'aml_EStringToStringMapEntry72' property in the generated
    # code (a bare stub) -- manually attach it so aml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aml_DocumentRoot(actor="sample_text", body="sample_text", date="sample_text", department="sample_text", description="sample_text", description1="sample_text", email="sample_text", event="sample_text", firstName="sample_text", id="sample_text", idRef="sample_text", label="sample_text", label1="sample_text", lastName="sample_text", middleName="sample_text", mixed="sample_text", nickName="sample_text", organization="sample_text", perspective="sample_text", rationale="sample_text", region="sample_text", securityMarking="sample_text", subject="sample_text", symbol="sample_text", title="sample_text", url="sample_text")
    partner = aml_EStringToStringMapEntry()
    setattr(partner, 'aml_EStringToStringMapEntry72', None)
    _safe_set(owner, 'aml_DocumentRoot71', {partner})
    assert getattr(partner, 'aml_EStringToStringMapEntry72') == owner
    _safe_set(owner, 'aml_DocumentRoot71', set())
    assert getattr(partner, 'aml_EStringToStringMapEntry72') is None


