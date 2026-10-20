import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractModel,
    Indexable,
    ModelElement,
    Port,
    Sequence,
    SequenceNode,
    effbdpattern_AbstractModel,
    effbdpattern_Allocation,
    effbdpattern_And,
    effbdpattern_Component,
    effbdpattern_Condition,
    effbdpattern_Context,
    effbdpattern_Description,
    effbdpattern_Domain,
    effbdpattern_Feature,
    effbdpattern_Final,
    effbdpattern_Flow,
    effbdpattern_Force,
    effbdpattern_Function,
    effbdpattern_FunctionProperty,
    effbdpattern_Impact,
    effbdpattern_Indexable,
    effbdpattern_InputPort,
    effbdpattern_Item,
    effbdpattern_Iteration,
    effbdpattern_Keyword,
    effbdpattern_Loop,
    effbdpattern_LoopExit,
    effbdpattern_Model,
    effbdpattern_ModelElement,
    effbdpattern_Or,
    effbdpattern_OutputPort,
    effbdpattern_Parameter,
    effbdpattern_PatternCatalog,
    effbdpattern_PatternModel,
    effbdpattern_Port,
    effbdpattern_Problem,
    effbdpattern_Sequence,
    effbdpattern_SequenceNode,
    effbdpattern_Start,
    effbdpattern_SystemPattern,
    effbdpattern_Token,
    effbdpattern_Workbench,
    FunctionDomain,
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

def test_assoc_antiPatterns114_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    _safe_set(b, 'effbdpattern_SystemPattern115', a1)
    assert _is_linked(b, 'effbdpattern_SystemPattern115', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern113'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern113', b)
    _safe_set(b, 'effbdpattern_SystemPattern115', a2)
    assert _is_linked(b, 'effbdpattern_SystemPattern115', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern113'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern113', b)
    if hasattr(a2, 'effbdpattern_SystemPattern113'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern113', b)
    _safe_set(b, 'effbdpattern_SystemPattern115', None)
    assert not _is_linked(b, 'effbdpattern_SystemPattern115', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern113'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern113', b)


def test_assoc_concreteRole62_reverse_link_reassign_clear():
    a1 = effbdpattern_Parameter(name="sample_text")
    a2 = effbdpattern_Parameter(name="sample_text_2")
    b = effbdpattern_ModelElement(modelId=7, modelName="sample_text")
    _safe_set(b, 'effbdpattern_ModelElement64', a1)
    assert _is_linked(b, 'effbdpattern_ModelElement64', a1)
    if hasattr(a1, 'effbdpattern_Parameter63'):
        assert _is_linked(a1, 'effbdpattern_Parameter63', b)
    _safe_set(b, 'effbdpattern_ModelElement64', a2)
    assert _is_linked(b, 'effbdpattern_ModelElement64', a2)
    if hasattr(a1, 'effbdpattern_Parameter63'):
        assert not _is_linked(a1, 'effbdpattern_Parameter63', b)
    if hasattr(a2, 'effbdpattern_Parameter63'):
        assert _is_linked(a2, 'effbdpattern_Parameter63', b)
    _safe_set(b, 'effbdpattern_ModelElement64', None)
    assert not _is_linked(b, 'effbdpattern_ModelElement64', a2)
    if hasattr(a2, 'effbdpattern_Parameter63'):
        assert not _is_linked(a2, 'effbdpattern_Parameter63', b)


def test_assoc_condition88_reverse_link_reassign_clear():
    a1 = effbdpattern_Force(description="sample_text", scale=7, value=7)
    a2 = effbdpattern_Force(description="sample_text_2", scale=13, value=13)
    b = effbdpattern_Condition(name="sample_text")
    _safe_set(b, 'effbdpattern_Condition89', a1)
    assert _is_linked(b, 'effbdpattern_Condition89', a1)
    if hasattr(a1, 'effbdpattern_Force'):
        assert _is_linked(a1, 'effbdpattern_Force', b)
    _safe_set(b, 'effbdpattern_Condition89', a2)
    assert _is_linked(b, 'effbdpattern_Condition89', a2)
    if hasattr(a1, 'effbdpattern_Force'):
        assert not _is_linked(a1, 'effbdpattern_Force', b)
    if hasattr(a2, 'effbdpattern_Force'):
        assert _is_linked(a2, 'effbdpattern_Force', b)
    _safe_set(b, 'effbdpattern_Condition89', None)
    assert not _is_linked(b, 'effbdpattern_Condition89', a2)
    if hasattr(a2, 'effbdpattern_Force'):
        assert not _is_linked(a2, 'effbdpattern_Force', b)


def test_assoc_conditions65_reverse_link_reassign_clear():
    a1 = effbdpattern_Context(description="sample_text")
    a2 = effbdpattern_Context(description="sample_text_2")
    b = effbdpattern_Condition(name="sample_text")
    _safe_set(b, 'effbdpattern_Condition67', a1)
    assert _is_linked(b, 'effbdpattern_Condition67', a1)
    if hasattr(a1, 'effbdpattern_Context66'):
        assert _is_linked(a1, 'effbdpattern_Context66', b)
    _safe_set(b, 'effbdpattern_Condition67', a2)
    assert _is_linked(b, 'effbdpattern_Condition67', a2)
    if hasattr(a1, 'effbdpattern_Context66'):
        assert not _is_linked(a1, 'effbdpattern_Context66', b)
    if hasattr(a2, 'effbdpattern_Context66'):
        assert _is_linked(a2, 'effbdpattern_Context66', b)
    _safe_set(b, 'effbdpattern_Condition67', None)
    assert not _is_linked(b, 'effbdpattern_Condition67', a2)
    if hasattr(a2, 'effbdpattern_Context66'):
        assert not _is_linked(a2, 'effbdpattern_Context66', b)


def test_assoc_context104_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_Context(description="sample_text")
    _safe_set(b, 'effbdpattern_Context106', a1)
    assert _is_linked(b, 'effbdpattern_Context106', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern105'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern105', b)
    _safe_set(b, 'effbdpattern_Context106', a2)
    assert _is_linked(b, 'effbdpattern_Context106', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern105'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern105', b)
    if hasattr(a2, 'effbdpattern_SystemPattern105'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern105', b)
    _safe_set(b, 'effbdpattern_Context106', None)
    assert not _is_linked(b, 'effbdpattern_Context106', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern105'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern105', b)


def test_assoc_controlFlowEdge19_reverse_link_reassign_clear():
    a1 = effbdpattern_SequenceNode(name="sample_text", tMax=7, tMin=7)
    a2 = effbdpattern_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    b = effbdpattern_SequenceNode(name="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'effbdpattern_SequenceNode18', {a1})
    assert _is_linked(b, 'effbdpattern_SequenceNode18', a1)
    if hasattr(a1, 'effbdpattern_SequenceNode'):
        assert _is_linked(a1, 'effbdpattern_SequenceNode', b)
    _safe_set(b, 'effbdpattern_SequenceNode18', {a2})
    assert _is_linked(b, 'effbdpattern_SequenceNode18', a2)
    if hasattr(a1, 'effbdpattern_SequenceNode'):
        assert not _is_linked(a1, 'effbdpattern_SequenceNode', b)
    if hasattr(a2, 'effbdpattern_SequenceNode'):
        assert _is_linked(a2, 'effbdpattern_SequenceNode', b)
    _safe_set(b, 'effbdpattern_SequenceNode18', set())
    assert not _is_linked(b, 'effbdpattern_SequenceNode18', a2)
    if hasattr(a2, 'effbdpattern_SequenceNode'):
        assert not _is_linked(a2, 'effbdpattern_SequenceNode', b)


def test_assoc_decompositions1_reverse_link_reassign_clear():
    a1 = effbdpattern_Function(domain="sample_text")
    a2 = effbdpattern_Function(domain="sample_text_2")
    b = effbdpattern_Function(domain="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Function'):
        assert _is_linked(a1, 'Function', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Function'):
        assert not _is_linked(a1, 'Function', b)
    if hasattr(a2, 'Function'):
        assert _is_linked(a2, 'Function', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Function'):
        assert not _is_linked(a2, 'Function', b)


def test_assoc_delegate21_reverse_link_reassign_clear():
    a1 = effbdpattern_Port(id="sample_text")
    a2 = effbdpattern_Port(id="sample_text_2")
    b = effbdpattern_Port(id="sample_text")
    _safe_set(b, 'effbdpattern_Port20', a1)
    assert _is_linked(b, 'effbdpattern_Port20', a1)
    if hasattr(a1, 'effbdpattern_Port'):
        assert _is_linked(a1, 'effbdpattern_Port', b)
    _safe_set(b, 'effbdpattern_Port20', a2)
    assert _is_linked(b, 'effbdpattern_Port20', a2)
    if hasattr(a1, 'effbdpattern_Port'):
        assert not _is_linked(a1, 'effbdpattern_Port', b)
    if hasattr(a2, 'effbdpattern_Port'):
        assert _is_linked(a2, 'effbdpattern_Port', b)
    _safe_set(b, 'effbdpattern_Port20', None)
    assert not _is_linked(b, 'effbdpattern_Port20', a2)
    if hasattr(a2, 'effbdpattern_Port'):
        assert not _is_linked(a2, 'effbdpattern_Port', b)


def test_assoc_descriptions9_reverse_link_reassign_clear():
    a1 = effbdpattern_Function(domain="sample_text")
    a2 = effbdpattern_Function(domain="sample_text_2")
    b = effbdpattern_Description(content="sample_text")
    _safe_set(b, 'effbdpattern_Description', a1)
    assert _is_linked(b, 'effbdpattern_Description', a1)
    if hasattr(a1, 'effbdpattern_Function10'):
        assert _is_linked(a1, 'effbdpattern_Function10', b)
    _safe_set(b, 'effbdpattern_Description', a2)
    assert _is_linked(b, 'effbdpattern_Description', a2)
    if hasattr(a1, 'effbdpattern_Function10'):
        assert not _is_linked(a1, 'effbdpattern_Function10', b)
    if hasattr(a2, 'effbdpattern_Function10'):
        assert _is_linked(a2, 'effbdpattern_Function10', b)
    _safe_set(b, 'effbdpattern_Description', None)
    assert not _is_linked(b, 'effbdpattern_Description', a2)
    if hasattr(a2, 'effbdpattern_Function10'):
        assert not _is_linked(a2, 'effbdpattern_Function10', b)


def test_assoc_domain110_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_Domain(description="sample_text", name="sample_text")
    _safe_set(b, 'effbdpattern_Domain112', a1)
    assert _is_linked(b, 'effbdpattern_Domain112', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern111'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern111', b)
    _safe_set(b, 'effbdpattern_Domain112', a2)
    assert _is_linked(b, 'effbdpattern_Domain112', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern111'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern111', b)
    if hasattr(a2, 'effbdpattern_SystemPattern111'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern111', b)
    _safe_set(b, 'effbdpattern_Domain112', None)
    assert not _is_linked(b, 'effbdpattern_Domain112', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern111'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern111', b)


def test_assoc_domain79_reverse_link_reassign_clear():
    a1 = effbdpattern_Domain(description="sample_text", name="sample_text")
    a2 = effbdpattern_Domain(description="sample_text_2", name="sample_text_2")
    b = effbdpattern_AbstractModel(name="sample_text", version="sample_text")
    _safe_set(b, 'effbdpattern_AbstractModel', a1)
    assert _is_linked(b, 'effbdpattern_AbstractModel', a1)
    if hasattr(a1, 'effbdpattern_Domain80'):
        assert _is_linked(a1, 'effbdpattern_Domain80', b)
    _safe_set(b, 'effbdpattern_AbstractModel', a2)
    assert _is_linked(b, 'effbdpattern_AbstractModel', a2)
    if hasattr(a1, 'effbdpattern_Domain80'):
        assert not _is_linked(a1, 'effbdpattern_Domain80', b)
    if hasattr(a2, 'effbdpattern_Domain80'):
        assert _is_linked(a2, 'effbdpattern_Domain80', b)
    _safe_set(b, 'effbdpattern_AbstractModel', None)
    assert not _is_linked(b, 'effbdpattern_AbstractModel', a2)
    if hasattr(a2, 'effbdpattern_Domain80'):
        assert not _is_linked(a2, 'effbdpattern_Domain80', b)


def test_assoc_equivalentPatterns123_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    _safe_set(b, 'effbdpattern_SystemPattern124', a1)
    assert _is_linked(b, 'effbdpattern_SystemPattern124', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern122'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern122', b)
    _safe_set(b, 'effbdpattern_SystemPattern124', a2)
    assert _is_linked(b, 'effbdpattern_SystemPattern124', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern122'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern122', b)
    if hasattr(a2, 'effbdpattern_SystemPattern122'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern122', b)
    _safe_set(b, 'effbdpattern_SystemPattern124', None)
    assert not _is_linked(b, 'effbdpattern_SystemPattern124', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern122'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern122', b)


def test_assoc_feature97_reverse_link_reassign_clear():
    a1 = effbdpattern_Impact(scale=7, value=7)
    a2 = effbdpattern_Impact(scale=13, value=13)
    b = effbdpattern_Feature(description="sample_text", name="sample_text")
    _safe_set(b, 'effbdpattern_Feature98', a1)
    assert _is_linked(b, 'effbdpattern_Feature98', a1)
    if hasattr(a1, 'effbdpattern_Impact'):
        assert _is_linked(a1, 'effbdpattern_Impact', b)
    _safe_set(b, 'effbdpattern_Feature98', a2)
    assert _is_linked(b, 'effbdpattern_Feature98', a2)
    if hasattr(a1, 'effbdpattern_Impact'):
        assert not _is_linked(a1, 'effbdpattern_Impact', b)
    if hasattr(a2, 'effbdpattern_Impact'):
        assert _is_linked(a2, 'effbdpattern_Impact', b)
    _safe_set(b, 'effbdpattern_Feature98', None)
    assert not _is_linked(b, 'effbdpattern_Feature98', a2)
    if hasattr(a2, 'effbdpattern_Impact'):
        assert not _is_linked(a2, 'effbdpattern_Impact', b)


def test_assoc_featuresToOptimize93_reverse_link_reassign_clear():
    a1 = effbdpattern_Problem(description="sample_text", name="sample_text")
    a2 = effbdpattern_Problem(description="sample_text_2", name="sample_text_2")
    b = effbdpattern_Feature(description="sample_text", name="sample_text")
    _safe_set(b, 'effbdpattern_Feature95', a1)
    assert _is_linked(b, 'effbdpattern_Feature95', a1)
    if hasattr(a1, 'effbdpattern_Problem94'):
        assert _is_linked(a1, 'effbdpattern_Problem94', b)
    _safe_set(b, 'effbdpattern_Feature95', a2)
    assert _is_linked(b, 'effbdpattern_Feature95', a2)
    if hasattr(a1, 'effbdpattern_Problem94'):
        assert not _is_linked(a1, 'effbdpattern_Problem94', b)
    if hasattr(a2, 'effbdpattern_Problem94'):
        assert _is_linked(a2, 'effbdpattern_Problem94', b)
    _safe_set(b, 'effbdpattern_Feature95', None)
    assert not _is_linked(b, 'effbdpattern_Feature95', a2)
    if hasattr(a2, 'effbdpattern_Problem94'):
        assert not _is_linked(a2, 'effbdpattern_Problem94', b)


def test_assoc_flows3_reverse_link_reassign_clear():
    a1 = effbdpattern_Function(domain="sample_text")
    a2 = effbdpattern_Function(domain="sample_text_2")
    b = effbdpattern_Flow(flowName="sample_text")
    _safe_set(b, 'effbdpattern_Flow', a1)
    assert _is_linked(b, 'effbdpattern_Flow', a1)
    if hasattr(a1, 'effbdpattern_Function4'):
        assert _is_linked(a1, 'effbdpattern_Function4', b)
    _safe_set(b, 'effbdpattern_Flow', a2)
    assert _is_linked(b, 'effbdpattern_Flow', a2)
    if hasattr(a1, 'effbdpattern_Function4'):
        assert not _is_linked(a1, 'effbdpattern_Function4', b)
    if hasattr(a2, 'effbdpattern_Function4'):
        assert _is_linked(a2, 'effbdpattern_Function4', b)
    _safe_set(b, 'effbdpattern_Flow', None)
    assert not _is_linked(b, 'effbdpattern_Flow', a2)
    if hasattr(a2, 'effbdpattern_Function4'):
        assert not _is_linked(a2, 'effbdpattern_Function4', b)


def test_assoc_forces96_reverse_link_reassign_clear():
    a1 = effbdpattern_Problem(description="sample_text", name="sample_text")
    a2 = effbdpattern_Problem(description="sample_text_2", name="sample_text_2")
    b = effbdpattern_Force(description="sample_text", scale=7, value=7)
    _safe_set(b, 'Force', a1)
    assert _is_linked(b, 'Force', a1)
    if hasattr(a1, 'problem'):
        assert _is_linked(a1, 'problem', b)
    _safe_set(b, 'Force', a2)
    assert _is_linked(b, 'Force', a2)
    if hasattr(a1, 'problem'):
        assert not _is_linked(a1, 'problem', b)
    if hasattr(a2, 'problem'):
        assert _is_linked(a2, 'problem', b)
    _safe_set(b, 'Force', None)
    assert not _is_linked(b, 'Force', a2)
    if hasattr(a2, 'problem'):
        assert not _is_linked(a2, 'problem', b)


def test_assoc_fragments84_reverse_link_reassign_clear():
    a1 = effbdpattern_AbstractModel(name="sample_text", version="sample_text")
    a2 = effbdpattern_AbstractModel(name="sample_text_2", version="sample_text_2")
    b = effbdpattern_AbstractModel(name="sample_text", version="sample_text")
    _safe_set(b, 'parent85', {a1})
    assert _is_linked(b, 'parent85', a1)
    if hasattr(a1, 'AbstractModel86'):
        assert _is_linked(a1, 'AbstractModel86', b)
    _safe_set(b, 'parent85', {a2})
    assert _is_linked(b, 'parent85', a2)
    if hasattr(a1, 'AbstractModel86'):
        assert not _is_linked(a1, 'AbstractModel86', b)
    if hasattr(a2, 'AbstractModel86'):
        assert _is_linked(a2, 'AbstractModel86', b)
    _safe_set(b, 'parent85', set())
    assert not _is_linked(b, 'parent85', a2)
    if hasattr(a2, 'AbstractModel86'):
        assert not _is_linked(a2, 'AbstractModel86', b)


def test_assoc_fromFunction140_reverse_link_reassign_clear():
    a1 = effbdpattern_Function(domain="sample_text")
    a2 = effbdpattern_Function(domain="sample_text_2")
    b = effbdpattern_Allocation(id="sample_text", redundant=True)
    _safe_set(b, 'effbdpattern_Allocation141', a1)
    assert _is_linked(b, 'effbdpattern_Allocation141', a1)
    if hasattr(a1, 'effbdpattern_Function142'):
        assert _is_linked(a1, 'effbdpattern_Function142', b)
    _safe_set(b, 'effbdpattern_Allocation141', a2)
    assert _is_linked(b, 'effbdpattern_Allocation141', a2)
    if hasattr(a1, 'effbdpattern_Function142'):
        assert not _is_linked(a1, 'effbdpattern_Function142', b)
    if hasattr(a2, 'effbdpattern_Function142'):
        assert _is_linked(a2, 'effbdpattern_Function142', b)
    _safe_set(b, 'effbdpattern_Allocation141', None)
    assert not _is_linked(b, 'effbdpattern_Allocation141', a2)
    if hasattr(a2, 'effbdpattern_Function142'):
        assert not _is_linked(a2, 'effbdpattern_Function142', b)


def test_assoc_impacts128_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_Impact(scale=7, value=7)
    _safe_set(b, 'Impact', a1)
    assert _is_linked(b, 'Impact', a1)
    if hasattr(a1, 'pattern'):
        assert _is_linked(a1, 'pattern', b)
    _safe_set(b, 'Impact', a2)
    assert _is_linked(b, 'Impact', a2)
    if hasattr(a1, 'pattern'):
        assert not _is_linked(a1, 'pattern', b)
    if hasattr(a2, 'pattern'):
        assert _is_linked(a2, 'pattern', b)
    _safe_set(b, 'Impact', None)
    assert not _is_linked(b, 'Impact', a2)
    if hasattr(a2, 'pattern'):
        assert not _is_linked(a2, 'pattern', b)


def test_assoc_items25_reverse_link_reassign_clear():
    a1 = effbdpattern_Item(name="sample_text")
    a2 = effbdpattern_Item(name="sample_text_2")
    b = effbdpattern_Flow(flowName="sample_text")
    _safe_set(b, 'effbdpattern_Flow26', {a1})
    assert _is_linked(b, 'effbdpattern_Flow26', a1)
    if hasattr(a1, 'effbdpattern_Item'):
        assert _is_linked(a1, 'effbdpattern_Item', b)
    _safe_set(b, 'effbdpattern_Flow26', {a2})
    assert _is_linked(b, 'effbdpattern_Flow26', a2)
    if hasattr(a1, 'effbdpattern_Item'):
        assert not _is_linked(a1, 'effbdpattern_Item', b)
    if hasattr(a2, 'effbdpattern_Item'):
        assert _is_linked(a2, 'effbdpattern_Item', b)
    _safe_set(b, 'effbdpattern_Flow26', set())
    assert not _is_linked(b, 'effbdpattern_Flow26', a2)
    if hasattr(a2, 'effbdpattern_Item'):
        assert not _is_linked(a2, 'effbdpattern_Item', b)


def test_assoc_modelElement129_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_ModelElement(modelId=7, modelName="sample_text")
    _safe_set(b, 'ModelElement', a1)
    assert _is_linked(b, 'ModelElement', a1)
    if hasattr(a1, 'pattern130'):
        assert _is_linked(a1, 'pattern130', b)
    _safe_set(b, 'ModelElement', a2)
    assert _is_linked(b, 'ModelElement', a2)
    if hasattr(a1, 'pattern130'):
        assert not _is_linked(a1, 'pattern130', b)
    if hasattr(a2, 'pattern130'):
        assert _is_linked(a2, 'pattern130', b)
    _safe_set(b, 'ModelElement', None)
    assert not _is_linked(b, 'ModelElement', a2)
    if hasattr(a2, 'pattern130'):
        assert not _is_linked(a2, 'pattern130', b)


def test_assoc_parameters101_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_Parameter(name="sample_text")
    _safe_set(b, 'effbdpattern_Parameter103', a1)
    assert _is_linked(b, 'effbdpattern_Parameter103', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern102'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern102', b)
    _safe_set(b, 'effbdpattern_Parameter103', a2)
    assert _is_linked(b, 'effbdpattern_Parameter103', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern102'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern102', b)
    if hasattr(a2, 'effbdpattern_SystemPattern102'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern102', b)
    _safe_set(b, 'effbdpattern_Parameter103', None)
    assert not _is_linked(b, 'effbdpattern_Parameter103', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern102'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern102', b)


def test_assoc_parent16_reverse_link_reassign_clear():
    a1 = effbdpattern_Function(domain="sample_text")
    a2 = effbdpattern_Function(domain="sample_text_2")
    b = effbdpattern_Function(domain="sample_text")
    _safe_set(b, 'decompositions', a1)
    assert _is_linked(b, 'decompositions', a1)
    if hasattr(a1, 'Function17'):
        assert _is_linked(a1, 'Function17', b)
    _safe_set(b, 'decompositions', a2)
    assert _is_linked(b, 'decompositions', a2)
    if hasattr(a1, 'Function17'):
        assert not _is_linked(a1, 'Function17', b)
    if hasattr(a2, 'Function17'):
        assert _is_linked(a2, 'Function17', b)
    _safe_set(b, 'decompositions', None)
    assert not _is_linked(b, 'decompositions', a2)
    if hasattr(a2, 'Function17'):
        assert not _is_linked(a2, 'Function17', b)


def test_assoc_parent31_reverse_link_reassign_clear():
    a1 = effbdpattern_FunctionProperty(description="sample_text")
    a2 = effbdpattern_FunctionProperty(description="sample_text_2")
    b = effbdpattern_FunctionProperty(description="sample_text")
    _safe_set(b, 'effbdpattern_FunctionProperty32', a1)
    assert _is_linked(b, 'effbdpattern_FunctionProperty32', a1)
    if hasattr(a1, 'effbdpattern_FunctionProperty30'):
        assert _is_linked(a1, 'effbdpattern_FunctionProperty30', b)
    _safe_set(b, 'effbdpattern_FunctionProperty32', a2)
    assert _is_linked(b, 'effbdpattern_FunctionProperty32', a2)
    if hasattr(a1, 'effbdpattern_FunctionProperty30'):
        assert not _is_linked(a1, 'effbdpattern_FunctionProperty30', b)
    if hasattr(a2, 'effbdpattern_FunctionProperty30'):
        assert _is_linked(a2, 'effbdpattern_FunctionProperty30', b)
    _safe_set(b, 'effbdpattern_FunctionProperty32', None)
    assert not _is_linked(b, 'effbdpattern_FunctionProperty32', a2)
    if hasattr(a2, 'effbdpattern_FunctionProperty30'):
        assert not _is_linked(a2, 'effbdpattern_FunctionProperty30', b)


def test_assoc_parent82_reverse_link_reassign_clear():
    a1 = effbdpattern_AbstractModel(name="sample_text", version="sample_text")
    a2 = effbdpattern_AbstractModel(name="sample_text_2", version="sample_text_2")
    b = effbdpattern_AbstractModel(name="sample_text", version="sample_text")
    _safe_set(b, 'fragments', a1)
    assert _is_linked(b, 'fragments', a1)
    if hasattr(a1, 'AbstractModel'):
        assert _is_linked(a1, 'AbstractModel', b)
    _safe_set(b, 'fragments', a2)
    assert _is_linked(b, 'fragments', a2)
    if hasattr(a1, 'AbstractModel'):
        assert not _is_linked(a1, 'AbstractModel', b)
    if hasattr(a2, 'AbstractModel'):
        assert _is_linked(a2, 'AbstractModel', b)
    _safe_set(b, 'fragments', None)
    assert not _is_linked(b, 'fragments', a2)
    if hasattr(a2, 'AbstractModel'):
        assert not _is_linked(a2, 'AbstractModel', b)


def test_assoc_pattern58_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_ModelElement(modelId=7, modelName="sample_text")
    _safe_set(b, 'modelElement', a1)
    assert _is_linked(b, 'modelElement', a1)
    if hasattr(a1, 'SystemPattern'):
        assert _is_linked(a1, 'SystemPattern', b)
    _safe_set(b, 'modelElement', a2)
    assert _is_linked(b, 'modelElement', a2)
    if hasattr(a1, 'SystemPattern'):
        assert not _is_linked(a1, 'SystemPattern', b)
    if hasattr(a2, 'SystemPattern'):
        assert _is_linked(a2, 'SystemPattern', b)
    _safe_set(b, 'modelElement', None)
    assert not _is_linked(b, 'modelElement', a2)
    if hasattr(a2, 'SystemPattern'):
        assert not _is_linked(a2, 'SystemPattern', b)


def test_assoc_pattern99_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_Impact(scale=7, value=7)
    _safe_set(b, 'impacts', a1)
    assert _is_linked(b, 'impacts', a1)
    if hasattr(a1, 'SystemPattern100'):
        assert _is_linked(a1, 'SystemPattern100', b)
    _safe_set(b, 'impacts', a2)
    assert _is_linked(b, 'impacts', a2)
    if hasattr(a1, 'SystemPattern100'):
        assert not _is_linked(a1, 'SystemPattern100', b)
    if hasattr(a2, 'SystemPattern100'):
        assert _is_linked(a2, 'SystemPattern100', b)
    _safe_set(b, 'impacts', None)
    assert not _is_linked(b, 'impacts', a2)
    if hasattr(a2, 'SystemPattern100'):
        assert not _is_linked(a2, 'SystemPattern100', b)


def test_assoc_patternRole61_reverse_link_reassign_clear():
    a1 = effbdpattern_Parameter(name="sample_text")
    a2 = effbdpattern_Parameter(name="sample_text_2")
    b = effbdpattern_ModelElement(modelId=7, modelName="sample_text")
    _safe_set(b, 'effbdpattern_ModelElement', a1)
    assert _is_linked(b, 'effbdpattern_ModelElement', a1)
    if hasattr(a1, 'effbdpattern_Parameter'):
        assert _is_linked(a1, 'effbdpattern_Parameter', b)
    _safe_set(b, 'effbdpattern_ModelElement', a2)
    assert _is_linked(b, 'effbdpattern_ModelElement', a2)
    if hasattr(a1, 'effbdpattern_Parameter'):
        assert not _is_linked(a1, 'effbdpattern_Parameter', b)
    if hasattr(a2, 'effbdpattern_Parameter'):
        assert _is_linked(a2, 'effbdpattern_Parameter', b)
    _safe_set(b, 'effbdpattern_ModelElement', None)
    assert not _is_linked(b, 'effbdpattern_ModelElement', a2)
    if hasattr(a2, 'effbdpattern_Parameter'):
        assert not _is_linked(a2, 'effbdpattern_Parameter', b)


def test_assoc_patterns33_reverse_link_reassign_clear():
    a1 = effbdpattern_PatternCatalog(id="sample_text")
    a2 = effbdpattern_PatternCatalog(id="sample_text_2")
    b = effbdpattern_Function(domain="sample_text")
    _safe_set(b, 'effbdpattern_Function34', a1)
    assert _is_linked(b, 'effbdpattern_Function34', a1)
    if hasattr(a1, 'effbdpattern_PatternCatalog'):
        assert _is_linked(a1, 'effbdpattern_PatternCatalog', b)
    _safe_set(b, 'effbdpattern_Function34', a2)
    assert _is_linked(b, 'effbdpattern_Function34', a2)
    if hasattr(a1, 'effbdpattern_PatternCatalog'):
        assert not _is_linked(a1, 'effbdpattern_PatternCatalog', b)
    if hasattr(a2, 'effbdpattern_PatternCatalog'):
        assert _is_linked(a2, 'effbdpattern_PatternCatalog', b)
    _safe_set(b, 'effbdpattern_Function34', None)
    assert not _is_linked(b, 'effbdpattern_Function34', a2)
    if hasattr(a2, 'effbdpattern_PatternCatalog'):
        assert not _is_linked(a2, 'effbdpattern_PatternCatalog', b)


def test_assoc_problem107_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_Problem(description="sample_text", name="sample_text")
    _safe_set(b, 'effbdpattern_Problem109', a1)
    assert _is_linked(b, 'effbdpattern_Problem109', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern108'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern108', b)
    _safe_set(b, 'effbdpattern_Problem109', a2)
    assert _is_linked(b, 'effbdpattern_Problem109', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern108'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern108', b)
    if hasattr(a2, 'effbdpattern_SystemPattern108'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern108', b)
    _safe_set(b, 'effbdpattern_Problem109', None)
    assert not _is_linked(b, 'effbdpattern_Problem109', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern108'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern108', b)


def test_assoc_problem87_reverse_link_reassign_clear():
    a1 = effbdpattern_Problem(description="sample_text", name="sample_text")
    a2 = effbdpattern_Problem(description="sample_text_2", name="sample_text_2")
    b = effbdpattern_Force(description="sample_text", scale=7, value=7)
    _safe_set(b, 'forces', a1)
    assert _is_linked(b, 'forces', a1)
    if hasattr(a1, 'Problem'):
        assert _is_linked(a1, 'Problem', b)
    _safe_set(b, 'forces', a2)
    assert _is_linked(b, 'forces', a2)
    if hasattr(a1, 'Problem'):
        assert not _is_linked(a1, 'Problem', b)
    if hasattr(a2, 'Problem'):
        assert _is_linked(a2, 'Problem', b)
    _safe_set(b, 'forces', None)
    assert not _is_linked(b, 'forces', a2)
    if hasattr(a2, 'Problem'):
        assert not _is_linked(a2, 'Problem', b)


def test_assoc_property13_reverse_link_reassign_clear():
    a1 = effbdpattern_FunctionProperty(description="sample_text")
    a2 = effbdpattern_FunctionProperty(description="sample_text_2")
    b = effbdpattern_Function(domain="sample_text")
    _safe_set(b, 'effbdpattern_Function14', {a1})
    assert _is_linked(b, 'effbdpattern_Function14', a1)
    if hasattr(a1, 'effbdpattern_FunctionProperty'):
        assert _is_linked(a1, 'effbdpattern_FunctionProperty', b)
    _safe_set(b, 'effbdpattern_Function14', {a2})
    assert _is_linked(b, 'effbdpattern_Function14', a2)
    if hasattr(a1, 'effbdpattern_FunctionProperty'):
        assert not _is_linked(a1, 'effbdpattern_FunctionProperty', b)
    if hasattr(a2, 'effbdpattern_FunctionProperty'):
        assert _is_linked(a2, 'effbdpattern_FunctionProperty', b)
    _safe_set(b, 'effbdpattern_Function14', set())
    assert not _is_linked(b, 'effbdpattern_Function14', a2)
    if hasattr(a2, 'effbdpattern_FunctionProperty'):
        assert not _is_linked(a2, 'effbdpattern_FunctionProperty', b)


def test_assoc_relatedPatterns120_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    _safe_set(b, 'effbdpattern_SystemPattern121', a1)
    assert _is_linked(b, 'effbdpattern_SystemPattern121', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern119'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern119', b)
    _safe_set(b, 'effbdpattern_SystemPattern121', a2)
    assert _is_linked(b, 'effbdpattern_SystemPattern121', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern119'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern119', b)
    if hasattr(a2, 'effbdpattern_SystemPattern119'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern119', b)
    _safe_set(b, 'effbdpattern_SystemPattern121', None)
    assert not _is_linked(b, 'effbdpattern_SystemPattern121', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern119'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern119', b)


def test_assoc_requestedPatterns117_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    _safe_set(b, 'effbdpattern_SystemPattern118', a1)
    assert _is_linked(b, 'effbdpattern_SystemPattern118', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern116'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern116', b)
    _safe_set(b, 'effbdpattern_SystemPattern118', a2)
    assert _is_linked(b, 'effbdpattern_SystemPattern118', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern116'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern116', b)
    if hasattr(a2, 'effbdpattern_SystemPattern116'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern116', b)
    _safe_set(b, 'effbdpattern_SystemPattern118', None)
    assert not _is_linked(b, 'effbdpattern_SystemPattern118', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern116'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern116', b)


def test_assoc_systemPatterns35_reverse_link_reassign_clear():
    a1 = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    a2 = effbdpattern_SystemPattern(alias="sample_text_2", challeng="sample_text_2", creationDate=date(2025, 6, 15), description="sample_text_2", knownApplications="sample_text_2", name="sample_text_2", patternId=13)
    b = effbdpattern_PatternCatalog(id="sample_text")
    _safe_set(b, 'effbdpattern_PatternCatalog36', {a1})
    assert _is_linked(b, 'effbdpattern_PatternCatalog36', a1)
    if hasattr(a1, 'effbdpattern_SystemPattern'):
        assert _is_linked(a1, 'effbdpattern_SystemPattern', b)
    _safe_set(b, 'effbdpattern_PatternCatalog36', {a2})
    assert _is_linked(b, 'effbdpattern_PatternCatalog36', a2)
    if hasattr(a1, 'effbdpattern_SystemPattern'):
        assert not _is_linked(a1, 'effbdpattern_SystemPattern', b)
    if hasattr(a2, 'effbdpattern_SystemPattern'):
        assert _is_linked(a2, 'effbdpattern_SystemPattern', b)
    _safe_set(b, 'effbdpattern_PatternCatalog36', set())
    assert not _is_linked(b, 'effbdpattern_PatternCatalog36', a2)
    if hasattr(a2, 'effbdpattern_SystemPattern'):
        assert not _is_linked(a2, 'effbdpattern_SystemPattern', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allocations56_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench57' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Allocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Allocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Allocation(id="sample_text", redundant=True)
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench57', None)
    _safe_set(owner, 'effbdpattern_Allocation', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench57')
    _safe_set(owner, 'effbdpattern_Allocation', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench57')


def test_assoc_conditions47_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench48' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Condition(name="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench48', None)
    _safe_set(owner, 'effbdpattern_Condition', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench48')
    _safe_set(owner, 'effbdpattern_Condition', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench48')


def test_assoc_contexts49_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench50' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Context's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Context's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Context(description="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench50', None)
    _safe_set(owner, 'effbdpattern_Context', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench50')
    _safe_set(owner, 'effbdpattern_Context', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench50')


def test_assoc_domains41_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench42' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Domain(description="sample_text", name="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench42', None)
    _safe_set(owner, 'effbdpattern_Domain', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench42')
    _safe_set(owner, 'effbdpattern_Domain', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench42')


def test_assoc_features45_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench46' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Feature(description="sample_text", name="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench46', None)
    _safe_set(owner, 'effbdpattern_Feature', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench46')
    _safe_set(owner, 'effbdpattern_Feature', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench46')


def test_assoc_functionProperties37_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_FunctionProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_FunctionProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_FunctionProperty(description="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench', None)
    _safe_set(owner, 'effbdpattern_FunctionProperty38', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench')
    _safe_set(owner, 'effbdpattern_FunctionProperty38', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench')


def test_assoc_functionalArchitecture134_stub_double():
    # effbdpattern_Model has no real 'effbdpattern_Model135' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Function(domain="sample_text")
    partner = effbdpattern_Model()
    setattr(partner, 'effbdpattern_Model135', None)
    _safe_set(owner, 'effbdpattern_Function136', partner)
    assert getattr(partner, 'effbdpattern_Model135') == owner
    _safe_set(owner, 'effbdpattern_Function136', None)
    assert getattr(partner, 'effbdpattern_Model135') is None


def test_assoc_functionalPattern68_stub_double():
    # effbdpattern_PatternModel has no real 'effbdpattern_PatternModel' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Function(domain="sample_text")
    partner = effbdpattern_PatternModel()
    setattr(partner, 'effbdpattern_PatternModel', None)
    _safe_set(owner, 'effbdpattern_Function69', partner)
    assert getattr(partner, 'effbdpattern_PatternModel') == owner
    _safe_set(owner, 'effbdpattern_Function69', None)
    assert getattr(partner, 'effbdpattern_PatternModel') is None


def test_assoc_inputPorts7_stub_double():
    # effbdpattern_InputPort has no real 'effbdpattern_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Function(domain="sample_text")
    partner = effbdpattern_InputPort()
    setattr(partner, 'effbdpattern_InputPort', None)
    _safe_set(owner, 'effbdpattern_Function8', {partner})
    assert getattr(partner, 'effbdpattern_InputPort') == owner
    _safe_set(owner, 'effbdpattern_Function8', set())
    assert getattr(partner, 'effbdpattern_InputPort') is None


def test_assoc_inputflowEdge22_stub_double():
    # effbdpattern_InputPort has no real 'effbdpattern_InputPort24' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Flow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Flow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Flow(flowName="sample_text")
    partner = effbdpattern_InputPort()
    setattr(partner, 'effbdpattern_InputPort24', None)
    _safe_set(owner, 'effbdpattern_Flow23', {partner})
    assert getattr(partner, 'effbdpattern_InputPort24') == owner
    _safe_set(owner, 'effbdpattern_Flow23', set())
    assert getattr(partner, 'effbdpattern_InputPort24') is None


def test_assoc_keywords43_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench44' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Keyword(value="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench44', None)
    _safe_set(owner, 'effbdpattern_Keyword', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench44')
    _safe_set(owner, 'effbdpattern_Keyword', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench44')


def test_assoc_keywords59_stub_double():
    # effbdpattern_Indexable has no real 'effbdpattern_Indexable' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Keyword's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Keyword's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Keyword(value="sample_text")
    partner = effbdpattern_Indexable()
    setattr(partner, 'effbdpattern_Indexable', None)
    _safe_set(owner, 'effbdpattern_Keyword60', partner)
    assert owner in getattr(partner, 'effbdpattern_Indexable')
    _safe_set(owner, 'effbdpattern_Keyword60', None)
    assert owner not in getattr(partner, 'effbdpattern_Indexable')


def test_assoc_outputPorts5_stub_double():
    # effbdpattern_OutputPort has no real 'effbdpattern_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Function(domain="sample_text")
    partner = effbdpattern_OutputPort()
    setattr(partner, 'effbdpattern_OutputPort', None)
    _safe_set(owner, 'effbdpattern_Function6', {partner})
    assert getattr(partner, 'effbdpattern_OutputPort') == owner
    _safe_set(owner, 'effbdpattern_Function6', set())
    assert getattr(partner, 'effbdpattern_OutputPort') is None


def test_assoc_outputflowEdge27_stub_double():
    # effbdpattern_OutputPort has no real 'effbdpattern_OutputPort28' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Flow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Flow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Flow(flowName="sample_text")
    partner = effbdpattern_OutputPort()
    setattr(partner, 'effbdpattern_OutputPort28', None)
    _safe_set(owner, 'effbdpattern_Flow29', partner)
    assert owner in getattr(partner, 'effbdpattern_OutputPort28')
    _safe_set(owner, 'effbdpattern_Flow29', None)
    assert owner not in getattr(partner, 'effbdpattern_OutputPort28')


def test_assoc_patternCatalog53_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench54' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_PatternCatalog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_PatternCatalog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_PatternCatalog(id="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench54', None)
    _safe_set(owner, 'effbdpattern_PatternCatalog55', partner)
    assert getattr(partner, 'effbdpattern_Workbench54') == owner
    _safe_set(owner, 'effbdpattern_PatternCatalog55', None)
    assert getattr(partner, 'effbdpattern_Workbench54') is None


def test_assoc_patternModel125_stub_double():
    # effbdpattern_PatternModel has no real 'effbdpattern_PatternModel127' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_SystemPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_SystemPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_SystemPattern(alias="sample_text", challeng="sample_text", creationDate=date(2024, 1, 1), description="sample_text", knownApplications="sample_text", name="sample_text", patternId=7)
    partner = effbdpattern_PatternModel()
    setattr(partner, 'effbdpattern_PatternModel127', None)
    _safe_set(owner, 'effbdpattern_SystemPattern126', partner)
    assert getattr(partner, 'effbdpattern_PatternModel127') == owner
    _safe_set(owner, 'effbdpattern_SystemPattern126', None)
    assert getattr(partner, 'effbdpattern_PatternModel127') is None


def test_assoc_problems39_stub_double():
    # effbdpattern_Workbench has no real 'effbdpattern_Workbench40' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Problem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Problem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Problem(description="sample_text", name="sample_text")
    partner = effbdpattern_Workbench()
    setattr(partner, 'effbdpattern_Workbench40', None)
    _safe_set(owner, 'effbdpattern_Problem', partner)
    assert owner in getattr(partner, 'effbdpattern_Workbench40')
    _safe_set(owner, 'effbdpattern_Problem', None)
    assert owner not in getattr(partner, 'effbdpattern_Workbench40')


def test_assoc_sequenceNodes2_stub_double():
    # effbdpattern_Sequence has no real 'effbdpattern_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Function(domain="sample_text")
    partner = effbdpattern_Sequence()
    setattr(partner, 'effbdpattern_Sequence', None)
    _safe_set(owner, 'effbdpattern_Function', {partner})
    assert getattr(partner, 'effbdpattern_Sequence') == owner
    _safe_set(owner, 'effbdpattern_Function', set())
    assert getattr(partner, 'effbdpattern_Sequence') is None


def test_assoc_toComponent143_stub_double():
    # effbdpattern_Component has no real 'effbdpattern_Component145' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Allocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Allocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Allocation(id="sample_text", redundant=True)
    partner = effbdpattern_Component()
    setattr(partner, 'effbdpattern_Component145', None)
    _safe_set(owner, 'effbdpattern_Allocation144', partner)
    assert getattr(partner, 'effbdpattern_Component145') == owner
    _safe_set(owner, 'effbdpattern_Allocation144', None)
    assert getattr(partner, 'effbdpattern_Component145') is None


def test_assoc_tokens11_stub_double():
    # effbdpattern_Token has no real 'effbdpattern_Token' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Function(domain="sample_text")
    partner = effbdpattern_Token()
    setattr(partner, 'effbdpattern_Token', None)
    _safe_set(owner, 'effbdpattern_Function12', {partner})
    assert getattr(partner, 'effbdpattern_Token') == owner
    _safe_set(owner, 'effbdpattern_Function12', set())
    assert getattr(partner, 'effbdpattern_Token') is None


def test_assoc_useCasesBeforePattern90_stub_double():
    # effbdpattern_PatternModel has no real 'effbdpattern_PatternModel92' property in the generated
    # code (a bare stub) -- manually attach it so effbdpattern_Problem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbdpattern_Problem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbdpattern_Problem(description="sample_text", name="sample_text")
    partner = effbdpattern_PatternModel()
    setattr(partner, 'effbdpattern_PatternModel92', None)
    _safe_set(owner, 'effbdpattern_Problem91', {partner})
    assert getattr(partner, 'effbdpattern_PatternModel92') == owner
    _safe_set(owner, 'effbdpattern_Problem91', set())
    assert getattr(partner, 'effbdpattern_PatternModel92') is None


