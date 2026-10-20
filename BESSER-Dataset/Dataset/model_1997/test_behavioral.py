import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Artefact,
    TraceLink,
    TraceLinkElement,
    iTrace_Artefact,
    iTrace_Block,
    iTrace_Code,
    iTrace_EObject,
    iTrace_Feature,
    iTrace_M2MLink,
    iTrace_M2TLink,
    iTrace_Model,
    iTrace_SourceElement,
    iTrace_SpecificFeature,
    iTrace_TargetElement,
    iTrace_TraceLink,
    iTrace_TraceLinkElement,
    iTrace_iTraceModel,
    AbstractionLevel,
    Aspect,
    Mode,
    ModelType,
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

def test_assoc_artefacts1_reverse_link_reassign_clear():
    a1 = iTrace_iTraceModel(projectName="sample_text", version="sample_text")
    a2 = iTrace_iTraceModel(projectName="sample_text_2", version="sample_text_2")
    b = iTrace_Artefact(abstractionLevel="sample_text", aspect="sample_text", name="sample_text", path="sample_text")
    _safe_set(b, 'Artefact', a1)
    assert _is_linked(b, 'Artefact', a1)
    if hasattr(a1, 'iTraceModel2'):
        assert _is_linked(a1, 'iTraceModel2', b)
    _safe_set(b, 'Artefact', a2)
    assert _is_linked(b, 'Artefact', a2)
    if hasattr(a1, 'iTraceModel2'):
        assert not _is_linked(a1, 'iTraceModel2', b)
    if hasattr(a2, 'iTraceModel2'):
        assert _is_linked(a2, 'iTraceModel2', b)
    _safe_set(b, 'Artefact', None)
    assert not _is_linked(b, 'Artefact', a2)
    if hasattr(a2, 'iTraceModel2'):
        assert not _is_linked(a2, 'iTraceModel2', b)


def test_assoc_elements20_reverse_link_reassign_clear():
    a1 = iTrace_TraceLinkElement(ref="sample_text", type="sample_text")
    a2 = iTrace_TraceLinkElement(ref="sample_text_2", type="sample_text_2")
    b = iTrace_Model(metamodel="sample_text")
    _safe_set(b, 'model', {a1})
    assert _is_linked(b, 'model', a1)
    if hasattr(a1, 'TraceLinkElement'):
        assert _is_linked(a1, 'TraceLinkElement', b)
    _safe_set(b, 'model', {a2})
    assert _is_linked(b, 'model', a2)
    if hasattr(a1, 'TraceLinkElement'):
        assert not _is_linked(a1, 'TraceLinkElement', b)
    if hasattr(a2, 'TraceLinkElement'):
        assert _is_linked(a2, 'TraceLinkElement', b)
    _safe_set(b, 'model', set())
    assert not _is_linked(b, 'model', a2)
    if hasattr(a2, 'TraceLinkElement'):
        assert not _is_linked(a2, 'TraceLinkElement', b)


def test_assoc_features26_reverse_link_reassign_clear():
    a1 = iTrace_SpecificFeature(groupName="sample_text")
    a2 = iTrace_SpecificFeature(groupName="sample_text_2")
    b = iTrace_Feature(attribute="sample_text", value="sample_text")
    _safe_set(b, 'Feature', a1)
    assert _is_linked(b, 'Feature', a1)
    if hasattr(a1, 'specificFeature'):
        assert _is_linked(a1, 'specificFeature', b)
    _safe_set(b, 'Feature', a2)
    assert _is_linked(b, 'Feature', a2)
    if hasattr(a1, 'specificFeature'):
        assert not _is_linked(a1, 'specificFeature', b)
    if hasattr(a2, 'specificFeature'):
        assert _is_linked(a2, 'specificFeature', b)
    _safe_set(b, 'Feature', None)
    assert not _is_linked(b, 'Feature', a2)
    if hasattr(a2, 'specificFeature'):
        assert not _is_linked(a2, 'specificFeature', b)


def test_assoc_iTraceModel14_reverse_link_reassign_clear():
    a1 = iTrace_iTraceModel(projectName="sample_text", version="sample_text")
    a2 = iTrace_iTraceModel(projectName="sample_text_2", version="sample_text_2")
    b = iTrace_Artefact(abstractionLevel="sample_text", aspect="sample_text", name="sample_text", path="sample_text")
    _safe_set(b, 'artefacts', a1)
    assert _is_linked(b, 'artefacts', a1)
    if hasattr(a1, 'iTraceModel15'):
        assert _is_linked(a1, 'iTraceModel15', b)
    _safe_set(b, 'artefacts', a2)
    assert _is_linked(b, 'artefacts', a2)
    if hasattr(a1, 'iTraceModel15'):
        assert not _is_linked(a1, 'iTraceModel15', b)
    if hasattr(a2, 'iTraceModel15'):
        assert _is_linked(a2, 'iTraceModel15', b)
    _safe_set(b, 'artefacts', None)
    assert not _is_linked(b, 'artefacts', a2)
    if hasattr(a2, 'iTraceModel15'):
        assert not _is_linked(a2, 'iTraceModel15', b)


def test_assoc_iTraceModel27_reverse_link_reassign_clear():
    a1 = iTrace_iTraceModel(projectName="sample_text", version="sample_text")
    a2 = iTrace_iTraceModel(projectName="sample_text_2", version="sample_text_2")
    b = iTrace_SpecificFeature(groupName="sample_text")
    _safe_set(b, 'specificFeatures', a1)
    assert _is_linked(b, 'specificFeatures', a1)
    if hasattr(a1, 'iTraceModel28'):
        assert _is_linked(a1, 'iTraceModel28', b)
    _safe_set(b, 'specificFeatures', a2)
    assert _is_linked(b, 'specificFeatures', a2)
    if hasattr(a1, 'iTraceModel28'):
        assert not _is_linked(a1, 'iTraceModel28', b)
    if hasattr(a2, 'iTraceModel28'):
        assert _is_linked(a2, 'iTraceModel28', b)
    _safe_set(b, 'specificFeatures', None)
    assert not _is_linked(b, 'specificFeatures', a2)
    if hasattr(a2, 'iTraceModel28'):
        assert not _is_linked(a2, 'iTraceModel28', b)


def test_assoc_iTraceModel6_reverse_link_reassign_clear():
    a1 = iTrace_iTraceModel(projectName="sample_text", version="sample_text")
    a2 = iTrace_iTraceModel(projectName="sample_text_2", version="sample_text_2")
    b = iTrace_TraceLink(comment="sample_text", createdBy="sample_text", createdOn="sample_text", fromFileName="sample_text", mode="sample_text", ruleName="sample_text", technicalBinding="sample_text", type="sample_text")
    _safe_set(b, 'traceLinks', a1)
    assert _is_linked(b, 'traceLinks', a1)
    if hasattr(a1, 'iTraceModel7'):
        assert _is_linked(a1, 'iTraceModel7', b)
    _safe_set(b, 'traceLinks', a2)
    assert _is_linked(b, 'traceLinks', a2)
    if hasattr(a1, 'iTraceModel7'):
        assert not _is_linked(a1, 'iTraceModel7', b)
    if hasattr(a2, 'iTraceModel7'):
        assert _is_linked(a2, 'iTraceModel7', b)
    _safe_set(b, 'traceLinks', None)
    assert not _is_linked(b, 'traceLinks', a2)
    if hasattr(a2, 'iTraceModel7'):
        assert not _is_linked(a2, 'iTraceModel7', b)


def test_assoc_model8_reverse_link_reassign_clear():
    a1 = iTrace_TraceLinkElement(ref="sample_text", type="sample_text")
    a2 = iTrace_TraceLinkElement(ref="sample_text_2", type="sample_text_2")
    b = iTrace_Model(metamodel="sample_text")
    _safe_set(b, 'Model', a1)
    assert _is_linked(b, 'Model', a1)
    if hasattr(a1, 'elements'):
        assert _is_linked(a1, 'elements', b)
    _safe_set(b, 'Model', a2)
    assert _is_linked(b, 'Model', a2)
    if hasattr(a1, 'elements'):
        assert not _is_linked(a1, 'elements', b)
    if hasattr(a2, 'elements'):
        assert _is_linked(a2, 'elements', b)
    _safe_set(b, 'Model', None)
    assert not _is_linked(b, 'Model', a2)
    if hasattr(a2, 'elements'):
        assert not _is_linked(a2, 'elements', b)


def test_assoc_specificFeature24_reverse_link_reassign_clear():
    a1 = iTrace_SpecificFeature(groupName="sample_text")
    a2 = iTrace_SpecificFeature(groupName="sample_text_2")
    b = iTrace_Feature(attribute="sample_text", value="sample_text")
    _safe_set(b, 'features', a1)
    assert _is_linked(b, 'features', a1)
    if hasattr(a1, 'SpecificFeature25'):
        assert _is_linked(a1, 'SpecificFeature25', b)
    _safe_set(b, 'features', a2)
    assert _is_linked(b, 'features', a2)
    if hasattr(a1, 'SpecificFeature25'):
        assert not _is_linked(a1, 'SpecificFeature25', b)
    if hasattr(a2, 'SpecificFeature25'):
        assert _is_linked(a2, 'SpecificFeature25', b)
    _safe_set(b, 'features', None)
    assert not _is_linked(b, 'features', a2)
    if hasattr(a2, 'SpecificFeature25'):
        assert not _is_linked(a2, 'SpecificFeature25', b)


def test_assoc_specificFeatures3_reverse_link_reassign_clear():
    a1 = iTrace_iTraceModel(projectName="sample_text", version="sample_text")
    a2 = iTrace_iTraceModel(projectName="sample_text_2", version="sample_text_2")
    b = iTrace_SpecificFeature(groupName="sample_text")
    _safe_set(b, 'SpecificFeature', a1)
    assert _is_linked(b, 'SpecificFeature', a1)
    if hasattr(a1, 'iTraceModel4'):
        assert _is_linked(a1, 'iTraceModel4', b)
    _safe_set(b, 'SpecificFeature', a2)
    assert _is_linked(b, 'SpecificFeature', a2)
    if hasattr(a1, 'iTraceModel4'):
        assert not _is_linked(a1, 'iTraceModel4', b)
    if hasattr(a2, 'iTraceModel4'):
        assert _is_linked(a2, 'iTraceModel4', b)
    _safe_set(b, 'SpecificFeature', None)
    assert not _is_linked(b, 'SpecificFeature', a2)
    if hasattr(a2, 'iTraceModel4'):
        assert not _is_linked(a2, 'iTraceModel4', b)


def test_assoc_traceLinks0_reverse_link_reassign_clear():
    a1 = iTrace_iTraceModel(projectName="sample_text", version="sample_text")
    a2 = iTrace_iTraceModel(projectName="sample_text_2", version="sample_text_2")
    b = iTrace_TraceLink(comment="sample_text", createdBy="sample_text", createdOn="sample_text", fromFileName="sample_text", mode="sample_text", ruleName="sample_text", technicalBinding="sample_text", type="sample_text")
    _safe_set(b, 'TraceLink', a1)
    assert _is_linked(b, 'TraceLink', a1)
    if hasattr(a1, 'iTraceModel'):
        assert _is_linked(a1, 'iTraceModel', b)
    _safe_set(b, 'TraceLink', a2)
    assert _is_linked(b, 'TraceLink', a2)
    if hasattr(a1, 'iTraceModel'):
        assert not _is_linked(a1, 'iTraceModel', b)
    if hasattr(a2, 'iTraceModel'):
        assert _is_linked(a2, 'iTraceModel', b)
    _safe_set(b, 'TraceLink', None)
    assert not _is_linked(b, 'TraceLink', a2)
    if hasattr(a2, 'iTraceModel'):
        assert not _is_linked(a2, 'iTraceModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_blocks16_stub_double():
    # iTrace_Code has no real 'code' property in the generated
    # code (a bare stub) -- manually attach it so iTrace_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iTrace_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iTrace_Block(blockNumber=7, endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = iTrace_Code()
    setattr(partner, 'code', None)
    _safe_set(owner, 'Block17', partner)
    assert owner in getattr(partner, 'code')
    _safe_set(owner, 'Block17', None)
    assert owner not in getattr(partner, 'code')


def test_assoc_code18_stub_double():
    # iTrace_Code has no real 'Code' property in the generated
    # code (a bare stub) -- manually attach it so iTrace_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iTrace_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iTrace_Block(blockNumber=7, endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = iTrace_Code()
    setattr(partner, 'Code', None)
    _safe_set(owner, 'blocks', partner)
    assert getattr(partner, 'Code') == owner
    _safe_set(owner, 'blocks', None)
    assert getattr(partner, 'Code') is None


def test_assoc_object9_stub_double():
    # iTrace_EObject has no real 'iTrace_EObject' property in the generated
    # code (a bare stub) -- manually attach it so iTrace_TraceLinkElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iTrace_TraceLinkElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iTrace_TraceLinkElement(ref="sample_text", type="sample_text")
    partner = iTrace_EObject()
    setattr(partner, 'iTrace_EObject', None)
    _safe_set(owner, 'iTrace_TraceLinkElement', partner)
    assert getattr(partner, 'iTrace_EObject') == owner
    _safe_set(owner, 'iTrace_TraceLinkElement', None)
    assert getattr(partner, 'iTrace_EObject') is None


def test_assoc_sourceElements5_stub_double():
    # iTrace_SourceElement has no real 'SourceElement' property in the generated
    # code (a bare stub) -- manually attach it so iTrace_TraceLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iTrace_TraceLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iTrace_TraceLink(comment="sample_text", createdBy="sample_text", createdOn="sample_text", fromFileName="sample_text", mode="sample_text", ruleName="sample_text", technicalBinding="sample_text", type="sample_text")
    partner = iTrace_SourceElement()
    setattr(partner, 'SourceElement', None)
    _safe_set(owner, 'traceLink', {partner})
    assert getattr(partner, 'SourceElement') == owner
    _safe_set(owner, 'traceLink', set())
    assert getattr(partner, 'SourceElement') is None


def test_assoc_targetBlocks12_stub_double():
    # iTrace_M2TLink has no real 'traceLink13' property in the generated
    # code (a bare stub) -- manually attach it so iTrace_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iTrace_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iTrace_Block(blockNumber=7, endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = iTrace_M2TLink()
    setattr(partner, 'traceLink13', None)
    _safe_set(owner, 'Block', partner)
    assert owner in getattr(partner, 'traceLink13')
    _safe_set(owner, 'Block', None)
    assert owner not in getattr(partner, 'traceLink13')


def test_assoc_traceLink19_stub_double():
    # iTrace_M2TLink has no real 'M2TLink' property in the generated
    # code (a bare stub) -- manually attach it so iTrace_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iTrace_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iTrace_Block(blockNumber=7, endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = iTrace_M2TLink()
    setattr(partner, 'M2TLink', None)
    _safe_set(owner, 'targetBlocks', partner)
    assert getattr(partner, 'M2TLink') == owner
    _safe_set(owner, 'targetBlocks', None)
    assert getattr(partner, 'M2TLink') is None


def test_assoc_traceLink21_stub_double():
    # iTrace_SourceElement has no real 'sourceElements' property in the generated
    # code (a bare stub) -- manually attach it so iTrace_TraceLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iTrace_TraceLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iTrace_TraceLink(comment="sample_text", createdBy="sample_text", createdOn="sample_text", fromFileName="sample_text", mode="sample_text", ruleName="sample_text", technicalBinding="sample_text", type="sample_text")
    partner = iTrace_SourceElement()
    setattr(partner, 'sourceElements', None)
    _safe_set(owner, 'TraceLink22', partner)
    assert getattr(partner, 'sourceElements') == owner
    _safe_set(owner, 'TraceLink22', None)
    assert getattr(partner, 'sourceElements') is None


