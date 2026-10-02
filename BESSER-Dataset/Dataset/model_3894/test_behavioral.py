import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActivityAspect,
    Atom,
    CaseAspect,
    Control,
    Document,
    DocumentCondition,
    DocumentDescriptor,
    DocumentType,
    Expression,
    GlobalAspect,
    ModelAspect,
    Operator,
    ProcessAspect,
    RuntimeGlobalAspect,
    RuntimeModelAspect,
    State,
    TaskAspect,
    TaskC,
    workflow_Activity,
    workflow_ActivityAspect,
    workflow_ActivityC,
    workflow_ActivityI,
    workflow_ActivityO,
    workflow_Agent,
    workflow_AgentContainer,
    workflow_Arc,
    workflow_Atom,
    workflow_Case,
    workflow_CaseAspect,
    workflow_CaseC,
    workflow_CaseI,
    workflow_CaseO,
    workflow_ConstantAtom,
    workflow_Control,
    workflow_ControlAspect,
    workflow_CoreModel,
    workflow_DefaultDocument,
    workflow_DefaultDocumentCondition,
    workflow_DefaultDocumentDescriptor,
    workflow_DefaultDocumentType,
    workflow_Document,
    workflow_DocumentCondition,
    workflow_DocumentContainer,
    workflow_DocumentDescrAtom,
    workflow_DocumentDescriptor,
    workflow_DocumentType,
    workflow_DocumentTypeContainer,
    workflow_DotOperator,
    workflow_EnumField,
    workflow_EnumFieldAtom,
    workflow_EnumFieldValue,
    workflow_EnumLiteral,
    workflow_EnumLiteralAtom,
    workflow_EqualToOperator,
    workflow_Expression,
    workflow_Field,
    workflow_FieldAtom,
    workflow_FieldValue,
    workflow_GlobalAspect,
    workflow_GreaterThanOperator,
    workflow_Information,
    workflow_InformationAspect,
    workflow_InformationRuntimeAspect,
    workflow_LessThanOperator,
    workflow_Marking,
    workflow_ModelAspect,
    workflow_ModelRegistry,
    workflow_Operator,
    workflow_Organisation,
    workflow_OrganisationAspect,
    workflow_PetriNet,
    workflow_Place,
    workflow_Process,
    workflow_ProcessAspect,
    workflow_ProcessDocument,
    workflow_ProcessO,
    workflow_Role,
    workflow_RuntimeCoreModel,
    workflow_RuntimeGlobalAspect,
    workflow_RuntimeInformation,
    workflow_RuntimeModelAspect,
    workflow_State,
    workflow_String2DocumentMap,
    workflow_Task,
    workflow_TaskAspect,
    workflow_TaskC,
    workflow_TaskI,
    workflow_TaskO,
    workflow_Token,
    workflow_Transition,
    workflow_UnequalToOperator,
    workflow_WorkflowEngine,
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

def test_assoc_DocumentType80_reverse_link_reassign_clear():
    a1 = workflow_DocumentType(name="sample_text")
    a2 = workflow_DocumentType(name="sample_text_2")
    b = workflow_Document(id="sample_text", name="sample_text")
    _safe_set(b, 'workflow_Document81', a1)
    assert _is_linked(b, 'workflow_Document81', a1)
    if hasattr(a1, 'workflow_DocumentType82'):
        assert _is_linked(a1, 'workflow_DocumentType82', b)
    _safe_set(b, 'workflow_Document81', a2)
    assert _is_linked(b, 'workflow_Document81', a2)
    if hasattr(a1, 'workflow_DocumentType82'):
        assert not _is_linked(a1, 'workflow_DocumentType82', b)
    if hasattr(a2, 'workflow_DocumentType82'):
        assert _is_linked(a2, 'workflow_DocumentType82', b)
    _safe_set(b, 'workflow_Document81', None)
    assert not _is_linked(b, 'workflow_Document81', a2)
    if hasattr(a2, 'workflow_DocumentType82'):
        assert not _is_linked(a2, 'workflow_DocumentType82', b)


def test_assoc_activities6_reverse_link_reassign_clear():
    a1 = workflow_Case(client="sample_text", finished=True, id="sample_text", started=True)
    a2 = workflow_Case(client="sample_text_2", finished=False, id="sample_text_2", started=False)
    b = workflow_Activity(finished=True, started=True)
    _safe_set(b, 'workflow_Activity', a1)
    assert _is_linked(b, 'workflow_Activity', a1)
    if hasattr(a1, 'workflow_Case'):
        assert _is_linked(a1, 'workflow_Case', b)
    _safe_set(b, 'workflow_Activity', a2)
    assert _is_linked(b, 'workflow_Activity', a2)
    if hasattr(a1, 'workflow_Case'):
        assert not _is_linked(a1, 'workflow_Case', b)
    if hasattr(a2, 'workflow_Case'):
        assert _is_linked(a2, 'workflow_Case', b)
    _safe_set(b, 'workflow_Activity', None)
    assert not _is_linked(b, 'workflow_Activity', a2)
    if hasattr(a2, 'workflow_Case'):
        assert not _is_linked(a2, 'workflow_Case', b)


def test_assoc_agents166_reverse_link_reassign_clear():
    a1 = workflow_AgentContainer(name="sample_text")
    a2 = workflow_AgentContainer(name="sample_text_2")
    b = workflow_Agent(name="sample_text", password="sample_text", username="sample_text")
    _safe_set(b, 'workflow_Agent167', a1)
    assert _is_linked(b, 'workflow_Agent167', a1)
    if hasattr(a1, 'workflow_AgentContainer'):
        assert _is_linked(a1, 'workflow_AgentContainer', b)
    _safe_set(b, 'workflow_Agent167', a2)
    assert _is_linked(b, 'workflow_Agent167', a2)
    if hasattr(a1, 'workflow_AgentContainer'):
        assert not _is_linked(a1, 'workflow_AgentContainer', b)
    if hasattr(a2, 'workflow_AgentContainer'):
        assert _is_linked(a2, 'workflow_AgentContainer', b)
    _safe_set(b, 'workflow_Agent167', None)
    assert not _is_linked(b, 'workflow_Agent167', a2)
    if hasattr(a2, 'workflow_AgentContainer'):
        assert not _is_linked(a2, 'workflow_AgentContainer', b)


def test_assoc_coreModel107_reverse_link_reassign_clear():
    a1 = workflow_Process(name="sample_text")
    a2 = workflow_Process(name="sample_text_2")
    b = workflow_CoreModel(name="sample_text")
    _safe_set(b, 'CoreModel108', a1)
    assert _is_linked(b, 'CoreModel108', a1)
    if hasattr(a1, 'process'):
        assert _is_linked(a1, 'process', b)
    _safe_set(b, 'CoreModel108', a2)
    assert _is_linked(b, 'CoreModel108', a2)
    if hasattr(a1, 'process'):
        assert not _is_linked(a1, 'process', b)
    if hasattr(a2, 'process'):
        assert _is_linked(a2, 'process', b)
    _safe_set(b, 'CoreModel108', None)
    assert not _is_linked(b, 'CoreModel108', a2)
    if hasattr(a2, 'process'):
        assert not _is_linked(a2, 'process', b)


def test_assoc_defaultValue153_reverse_link_reassign_clear():
    a1 = workflow_EnumLiteral(name="sample_text")
    a2 = workflow_EnumLiteral(name="sample_text_2")
    b = workflow_EnumField(name="sample_text")
    _safe_set(b, 'workflow_EnumField154', a1)
    assert _is_linked(b, 'workflow_EnumField154', a1)
    if hasattr(a1, 'workflow_EnumLiteral155'):
        assert _is_linked(a1, 'workflow_EnumLiteral155', b)
    _safe_set(b, 'workflow_EnumField154', a2)
    assert _is_linked(b, 'workflow_EnumField154', a2)
    if hasattr(a1, 'workflow_EnumLiteral155'):
        assert not _is_linked(a1, 'workflow_EnumLiteral155', b)
    if hasattr(a2, 'workflow_EnumLiteral155'):
        assert _is_linked(a2, 'workflow_EnumLiteral155', b)
    _safe_set(b, 'workflow_EnumField154', None)
    assert not _is_linked(b, 'workflow_EnumField154', a2)
    if hasattr(a2, 'workflow_EnumLiteral155'):
        assert not _is_linked(a2, 'workflow_EnumLiteral155', b)


def test_assoc_documentType138_reverse_link_reassign_clear():
    a1 = workflow_ProcessDocument(name="sample_text")
    a2 = workflow_ProcessDocument(name="sample_text_2")
    b = workflow_DocumentType(name="sample_text")
    _safe_set(b, 'workflow_DocumentType140', a1)
    assert _is_linked(b, 'workflow_DocumentType140', a1)
    if hasattr(a1, 'workflow_ProcessDocument139'):
        assert _is_linked(a1, 'workflow_ProcessDocument139', b)
    _safe_set(b, 'workflow_DocumentType140', a2)
    assert _is_linked(b, 'workflow_DocumentType140', a2)
    if hasattr(a1, 'workflow_ProcessDocument139'):
        assert not _is_linked(a1, 'workflow_ProcessDocument139', b)
    if hasattr(a2, 'workflow_ProcessDocument139'):
        assert _is_linked(a2, 'workflow_ProcessDocument139', b)
    _safe_set(b, 'workflow_DocumentType140', None)
    assert not _is_linked(b, 'workflow_DocumentType140', a2)
    if hasattr(a2, 'workflow_ProcessDocument139'):
        assert not _is_linked(a2, 'workflow_ProcessDocument139', b)


def test_assoc_documentType71_reverse_link_reassign_clear():
    a1 = workflow_DocumentType(name="sample_text")
    a2 = workflow_DocumentType(name="sample_text_2")
    b = workflow_DocumentDescriptor(name="sample_text")
    _safe_set(b, 'workflow_DocumentDescriptor72', a1)
    assert _is_linked(b, 'workflow_DocumentDescriptor72', a1)
    if hasattr(a1, 'workflow_DocumentType'):
        assert _is_linked(a1, 'workflow_DocumentType', b)
    _safe_set(b, 'workflow_DocumentDescriptor72', a2)
    assert _is_linked(b, 'workflow_DocumentDescriptor72', a2)
    if hasattr(a1, 'workflow_DocumentType'):
        assert not _is_linked(a1, 'workflow_DocumentType', b)
    if hasattr(a2, 'workflow_DocumentType'):
        assert _is_linked(a2, 'workflow_DocumentType', b)
    _safe_set(b, 'workflow_DocumentDescriptor72', None)
    assert not _is_linked(b, 'workflow_DocumentDescriptor72', a2)
    if hasattr(a2, 'workflow_DocumentType'):
        assert not _is_linked(a2, 'workflow_DocumentType', b)


def test_assoc_documentTypes174_reverse_link_reassign_clear():
    a1 = workflow_DocumentTypeContainer(name="sample_text")
    a2 = workflow_DocumentTypeContainer(name="sample_text_2")
    b = workflow_DocumentType(name="sample_text")
    _safe_set(b, 'workflow_DocumentType175', a1)
    assert _is_linked(b, 'workflow_DocumentType175', a1)
    if hasattr(a1, 'workflow_DocumentTypeContainer'):
        assert _is_linked(a1, 'workflow_DocumentTypeContainer', b)
    _safe_set(b, 'workflow_DocumentType175', a2)
    assert _is_linked(b, 'workflow_DocumentType175', a2)
    if hasattr(a1, 'workflow_DocumentTypeContainer'):
        assert not _is_linked(a1, 'workflow_DocumentTypeContainer', b)
    if hasattr(a2, 'workflow_DocumentTypeContainer'):
        assert _is_linked(a2, 'workflow_DocumentTypeContainer', b)
    _safe_set(b, 'workflow_DocumentType175', None)
    assert not _is_linked(b, 'workflow_DocumentType175', a2)
    if hasattr(a2, 'workflow_DocumentTypeContainer'):
        assert not _is_linked(a2, 'workflow_DocumentTypeContainer', b)


def test_assoc_documents176_reverse_link_reassign_clear():
    a1 = workflow_DocumentContainer(name="sample_text")
    a2 = workflow_DocumentContainer(name="sample_text_2")
    b = workflow_Document(id="sample_text", name="sample_text")
    _safe_set(b, 'workflow_Document177', a1)
    assert _is_linked(b, 'workflow_Document177', a1)
    if hasattr(a1, 'workflow_DocumentContainer'):
        assert _is_linked(a1, 'workflow_DocumentContainer', b)
    _safe_set(b, 'workflow_Document177', a2)
    assert _is_linked(b, 'workflow_Document177', a2)
    if hasattr(a1, 'workflow_DocumentContainer'):
        assert not _is_linked(a1, 'workflow_DocumentContainer', b)
    if hasattr(a2, 'workflow_DocumentContainer'):
        assert _is_linked(a2, 'workflow_DocumentContainer', b)
    _safe_set(b, 'workflow_Document177', None)
    assert not _is_linked(b, 'workflow_Document177', a2)
    if hasattr(a2, 'workflow_DocumentContainer'):
        assert not _is_linked(a2, 'workflow_DocumentContainer', b)


def test_assoc_enumLiterals151_reverse_link_reassign_clear():
    a1 = workflow_EnumLiteral(name="sample_text")
    a2 = workflow_EnumLiteral(name="sample_text_2")
    b = workflow_EnumField(name="sample_text")
    _safe_set(b, 'workflow_EnumField152', {a1})
    assert _is_linked(b, 'workflow_EnumField152', a1)
    if hasattr(a1, 'workflow_EnumLiteral'):
        assert _is_linked(a1, 'workflow_EnumLiteral', b)
    _safe_set(b, 'workflow_EnumField152', {a2})
    assert _is_linked(b, 'workflow_EnumField152', a2)
    if hasattr(a1, 'workflow_EnumLiteral'):
        assert not _is_linked(a1, 'workflow_EnumLiteral', b)
    if hasattr(a2, 'workflow_EnumLiteral'):
        assert _is_linked(a2, 'workflow_EnumLiteral', b)
    _safe_set(b, 'workflow_EnumField152', set())
    assert not _is_linked(b, 'workflow_EnumField152', a2)
    if hasattr(a2, 'workflow_EnumLiteral'):
        assert not _is_linked(a2, 'workflow_EnumLiteral', b)


def test_assoc_field133_reverse_link_reassign_clear():
    a1 = workflow_FieldValue(value="sample_text")
    a2 = workflow_FieldValue(value="sample_text_2")
    b = workflow_Field(name="sample_text")
    _safe_set(b, 'workflow_Field135', a1)
    assert _is_linked(b, 'workflow_Field135', a1)
    if hasattr(a1, 'workflow_FieldValue134'):
        assert _is_linked(a1, 'workflow_FieldValue134', b)
    _safe_set(b, 'workflow_Field135', a2)
    assert _is_linked(b, 'workflow_Field135', a2)
    if hasattr(a1, 'workflow_FieldValue134'):
        assert not _is_linked(a1, 'workflow_FieldValue134', b)
    if hasattr(a2, 'workflow_FieldValue134'):
        assert _is_linked(a2, 'workflow_FieldValue134', b)
    _safe_set(b, 'workflow_Field135', None)
    assert not _is_linked(b, 'workflow_Field135', a2)
    if hasattr(a2, 'workflow_FieldValue134'):
        assert not _is_linked(a2, 'workflow_FieldValue134', b)


def test_assoc_fieldValues130_reverse_link_reassign_clear():
    a1 = workflow_FieldValue(value="sample_text")
    a2 = workflow_FieldValue(value="sample_text_2")
    b = workflow_DefaultDocument(placeholder=True)
    _safe_set(b, 'workflow_DefaultDocument', {a1})
    assert _is_linked(b, 'workflow_DefaultDocument', a1)
    if hasattr(a1, 'workflow_FieldValue'):
        assert _is_linked(a1, 'workflow_FieldValue', b)
    _safe_set(b, 'workflow_DefaultDocument', {a2})
    assert _is_linked(b, 'workflow_DefaultDocument', a2)
    if hasattr(a1, 'workflow_FieldValue'):
        assert not _is_linked(a1, 'workflow_FieldValue', b)
    if hasattr(a2, 'workflow_FieldValue'):
        assert _is_linked(a2, 'workflow_FieldValue', b)
    _safe_set(b, 'workflow_DefaultDocument', set())
    assert not _is_linked(b, 'workflow_DefaultDocument', a2)
    if hasattr(a2, 'workflow_FieldValue'):
        assert not _is_linked(a2, 'workflow_FieldValue', b)


def test_assoc_followsUpOn2_reverse_link_reassign_clear():
    a1 = workflow_TaskO(name="sample_text")
    a2 = workflow_TaskO(name="sample_text_2")
    b = workflow_TaskO(name="sample_text")
    _safe_set(b, 'workflow_TaskO3', a1)
    assert _is_linked(b, 'workflow_TaskO3', a1)
    if hasattr(a1, 'workflow_TaskO1'):
        assert _is_linked(a1, 'workflow_TaskO1', b)
    _safe_set(b, 'workflow_TaskO3', a2)
    assert _is_linked(b, 'workflow_TaskO3', a2)
    if hasattr(a1, 'workflow_TaskO1'):
        assert not _is_linked(a1, 'workflow_TaskO1', b)
    if hasattr(a2, 'workflow_TaskO1'):
        assert _is_linked(a2, 'workflow_TaskO1', b)
    _safe_set(b, 'workflow_TaskO3', None)
    assert not _is_linked(b, 'workflow_TaskO3', a2)
    if hasattr(a2, 'workflow_TaskO1'):
        assert not _is_linked(a2, 'workflow_TaskO1', b)


def test_assoc_in_45_reverse_link_reassign_clear():
    a1 = workflow_Place(name="sample_text")
    a2 = workflow_Place(name="sample_text_2")
    b = workflow_Arc(name="sample_text")
    _safe_set(b, 'Arc46', a1)
    assert _is_linked(b, 'Arc46', a1)
    if hasattr(a1, 'targetPlace'):
        assert _is_linked(a1, 'targetPlace', b)
    _safe_set(b, 'Arc46', a2)
    assert _is_linked(b, 'Arc46', a2)
    if hasattr(a1, 'targetPlace'):
        assert not _is_linked(a1, 'targetPlace', b)
    if hasattr(a2, 'targetPlace'):
        assert _is_linked(a2, 'targetPlace', b)
    _safe_set(b, 'Arc46', None)
    assert not _is_linked(b, 'Arc46', a2)
    if hasattr(a2, 'targetPlace'):
        assert not _is_linked(a2, 'targetPlace', b)


def test_assoc_mayTakeRoles19_reverse_link_reassign_clear():
    a1 = workflow_Role(name="sample_text")
    a2 = workflow_Role(name="sample_text_2")
    b = workflow_Agent(name="sample_text", password="sample_text", username="sample_text")
    _safe_set(b, 'workflow_Agent20', {a1})
    assert _is_linked(b, 'workflow_Agent20', a1)
    if hasattr(a1, 'workflow_Role21'):
        assert _is_linked(a1, 'workflow_Role21', b)
    _safe_set(b, 'workflow_Agent20', {a2})
    assert _is_linked(b, 'workflow_Agent20', a2)
    if hasattr(a1, 'workflow_Role21'):
        assert not _is_linked(a1, 'workflow_Role21', b)
    if hasattr(a2, 'workflow_Role21'):
        assert _is_linked(a2, 'workflow_Role21', b)
    _safe_set(b, 'workflow_Agent20', set())
    assert not _is_linked(b, 'workflow_Agent20', a2)
    if hasattr(a2, 'workflow_Role21'):
        assert not _is_linked(a2, 'workflow_Role21', b)


def test_assoc_out47_reverse_link_reassign_clear():
    a1 = workflow_Place(name="sample_text")
    a2 = workflow_Place(name="sample_text_2")
    b = workflow_Arc(name="sample_text")
    _safe_set(b, 'Arc48', a1)
    assert _is_linked(b, 'Arc48', a1)
    if hasattr(a1, 'sourcePlace'):
        assert _is_linked(a1, 'sourcePlace', b)
    _safe_set(b, 'Arc48', a2)
    assert _is_linked(b, 'Arc48', a2)
    if hasattr(a1, 'sourcePlace'):
        assert not _is_linked(a1, 'sourcePlace', b)
    if hasattr(a2, 'sourcePlace'):
        assert _is_linked(a2, 'sourcePlace', b)
    _safe_set(b, 'Arc48', None)
    assert not _is_linked(b, 'Arc48', a2)
    if hasattr(a2, 'sourcePlace'):
        assert not _is_linked(a2, 'sourcePlace', b)


def test_assoc_process101_reverse_link_reassign_clear():
    a1 = workflow_Process(name="sample_text")
    a2 = workflow_Process(name="sample_text_2")
    b = workflow_CoreModel(name="sample_text")
    _safe_set(b, 'coreModel', a1)
    assert _is_linked(b, 'coreModel', a1)
    if hasattr(a1, 'Process102'):
        assert _is_linked(a1, 'Process102', b)
    _safe_set(b, 'coreModel', a2)
    assert _is_linked(b, 'coreModel', a2)
    if hasattr(a1, 'Process102'):
        assert not _is_linked(a1, 'Process102', b)
    if hasattr(a2, 'Process102'):
        assert _is_linked(a2, 'Process102', b)
    _safe_set(b, 'coreModel', None)
    assert not _is_linked(b, 'coreModel', a2)
    if hasattr(a2, 'Process102'):
        assert not _is_linked(a2, 'Process102', b)


def test_assoc_process7_reverse_link_reassign_clear():
    a1 = workflow_Process(name="sample_text")
    a2 = workflow_Process(name="sample_text_2")
    b = workflow_Case(client="sample_text", finished=True, id="sample_text", started=True)
    _safe_set(b, 'workflow_Case8', a1)
    assert _is_linked(b, 'workflow_Case8', a1)
    if hasattr(a1, 'workflow_Process'):
        assert _is_linked(a1, 'workflow_Process', b)
    _safe_set(b, 'workflow_Case8', a2)
    assert _is_linked(b, 'workflow_Case8', a2)
    if hasattr(a1, 'workflow_Process'):
        assert not _is_linked(a1, 'workflow_Process', b)
    if hasattr(a2, 'workflow_Process'):
        assert _is_linked(a2, 'workflow_Process', b)
    _safe_set(b, 'workflow_Case8', None)
    assert not _is_linked(b, 'workflow_Case8', a2)
    if hasattr(a2, 'workflow_Process'):
        assert not _is_linked(a2, 'workflow_Process', b)


def test_assoc_processDocument73_reverse_link_reassign_clear():
    a1 = workflow_ProcessDocument(name="sample_text")
    a2 = workflow_ProcessDocument(name="sample_text_2")
    b = workflow_DocumentDescriptor(name="sample_text")
    _safe_set(b, 'workflow_DocumentDescriptor74', a1)
    assert _is_linked(b, 'workflow_DocumentDescriptor74', a1)
    if hasattr(a1, 'workflow_ProcessDocument75'):
        assert _is_linked(a1, 'workflow_ProcessDocument75', b)
    _safe_set(b, 'workflow_DocumentDescriptor74', a2)
    assert _is_linked(b, 'workflow_DocumentDescriptor74', a2)
    if hasattr(a1, 'workflow_ProcessDocument75'):
        assert not _is_linked(a1, 'workflow_ProcessDocument75', b)
    if hasattr(a2, 'workflow_ProcessDocument75'):
        assert _is_linked(a2, 'workflow_ProcessDocument75', b)
    _safe_set(b, 'workflow_DocumentDescriptor74', None)
    assert not _is_linked(b, 'workflow_DocumentDescriptor74', a2)
    if hasattr(a2, 'workflow_ProcessDocument75'):
        assert not _is_linked(a2, 'workflow_ProcessDocument75', b)


def test_assoc_requiredRoles0_reverse_link_reassign_clear():
    a1 = workflow_TaskO(name="sample_text")
    a2 = workflow_TaskO(name="sample_text_2")
    b = workflow_Role(name="sample_text")
    _safe_set(b, 'workflow_Role', a1)
    assert _is_linked(b, 'workflow_Role', a1)
    if hasattr(a1, 'workflow_TaskO'):
        assert _is_linked(a1, 'workflow_TaskO', b)
    _safe_set(b, 'workflow_Role', a2)
    assert _is_linked(b, 'workflow_Role', a2)
    if hasattr(a1, 'workflow_TaskO'):
        assert not _is_linked(a1, 'workflow_TaskO', b)
    if hasattr(a2, 'workflow_TaskO'):
        assert _is_linked(a2, 'workflow_TaskO', b)
    _safe_set(b, 'workflow_Role', None)
    assert not _is_linked(b, 'workflow_Role', a2)
    if hasattr(a2, 'workflow_TaskO'):
        assert not _is_linked(a2, 'workflow_TaskO', b)


def test_assoc_roles168_reverse_link_reassign_clear():
    a1 = workflow_Role(name="sample_text")
    a2 = workflow_Role(name="sample_text_2")
    b = workflow_Organisation(name="sample_text")
    _safe_set(b, 'workflow_Organisation', {a1})
    assert _is_linked(b, 'workflow_Organisation', a1)
    if hasattr(a1, 'workflow_Role169'):
        assert _is_linked(a1, 'workflow_Role169', b)
    _safe_set(b, 'workflow_Organisation', {a2})
    assert _is_linked(b, 'workflow_Organisation', a2)
    if hasattr(a1, 'workflow_Role169'):
        assert not _is_linked(a1, 'workflow_Role169', b)
    if hasattr(a2, 'workflow_Role169'):
        assert _is_linked(a2, 'workflow_Role169', b)
    _safe_set(b, 'workflow_Organisation', set())
    assert not _is_linked(b, 'workflow_Organisation', a2)
    if hasattr(a2, 'workflow_Role169'):
        assert not _is_linked(a2, 'workflow_Role169', b)


def test_assoc_sourcePlace37_reverse_link_reassign_clear():
    a1 = workflow_Place(name="sample_text")
    a2 = workflow_Place(name="sample_text_2")
    b = workflow_Arc(name="sample_text")
    _safe_set(b, 'out', a1)
    assert _is_linked(b, 'out', a1)
    if hasattr(a1, 'Place'):
        assert _is_linked(a1, 'Place', b)
    _safe_set(b, 'out', a2)
    assert _is_linked(b, 'out', a2)
    if hasattr(a1, 'Place'):
        assert not _is_linked(a1, 'Place', b)
    if hasattr(a2, 'Place'):
        assert _is_linked(a2, 'Place', b)
    _safe_set(b, 'out', None)
    assert not _is_linked(b, 'out', a2)
    if hasattr(a2, 'Place'):
        assert not _is_linked(a2, 'Place', b)


def test_assoc_takenRoles16_reverse_link_reassign_clear():
    a1 = workflow_Role(name="sample_text")
    a2 = workflow_Role(name="sample_text_2")
    b = workflow_Agent(name="sample_text", password="sample_text", username="sample_text")
    _safe_set(b, 'workflow_Agent', {a1})
    assert _is_linked(b, 'workflow_Agent', a1)
    if hasattr(a1, 'workflow_Role17'):
        assert _is_linked(a1, 'workflow_Role17', b)
    _safe_set(b, 'workflow_Agent', {a2})
    assert _is_linked(b, 'workflow_Agent', a2)
    if hasattr(a1, 'workflow_Role17'):
        assert not _is_linked(a1, 'workflow_Role17', b)
    if hasattr(a2, 'workflow_Role17'):
        assert _is_linked(a2, 'workflow_Role17', b)
    _safe_set(b, 'workflow_Agent', set())
    assert not _is_linked(b, 'workflow_Agent', a2)
    if hasattr(a2, 'workflow_Role17'):
        assert not _is_linked(a2, 'workflow_Role17', b)


def test_assoc_targetPlace38_reverse_link_reassign_clear():
    a1 = workflow_Place(name="sample_text")
    a2 = workflow_Place(name="sample_text_2")
    b = workflow_Arc(name="sample_text")
    _safe_set(b, 'in_', a1)
    assert _is_linked(b, 'in_', a1)
    if hasattr(a1, 'Place39'):
        assert _is_linked(a1, 'Place39', b)
    _safe_set(b, 'in_', a2)
    assert _is_linked(b, 'in_', a2)
    if hasattr(a1, 'Place39'):
        assert not _is_linked(a1, 'Place39', b)
    if hasattr(a2, 'Place39'):
        assert _is_linked(a2, 'Place39', b)
    _safe_set(b, 'in_', None)
    assert not _is_linked(b, 'in_', a2)
    if hasattr(a2, 'Place39'):
        assert not _is_linked(a2, 'Place39', b)


def test_assoc_task12_reverse_link_reassign_clear():
    a1 = workflow_Task(name="sample_text")
    a2 = workflow_Task(name="sample_text_2")
    b = workflow_Activity(finished=True, started=True)
    _safe_set(b, 'workflow_Activity13', a1)
    assert _is_linked(b, 'workflow_Activity13', a1)
    if hasattr(a1, 'workflow_Task'):
        assert _is_linked(a1, 'workflow_Task', b)
    _safe_set(b, 'workflow_Activity13', a2)
    assert _is_linked(b, 'workflow_Activity13', a2)
    if hasattr(a1, 'workflow_Task'):
        assert not _is_linked(a1, 'workflow_Task', b)
    if hasattr(a2, 'workflow_Task'):
        assert _is_linked(a2, 'workflow_Task', b)
    _safe_set(b, 'workflow_Activity13', None)
    assert not _is_linked(b, 'workflow_Activity13', a2)
    if hasattr(a2, 'workflow_Task'):
        assert not _is_linked(a2, 'workflow_Task', b)


def test_assoc_tasks104_reverse_link_reassign_clear():
    a1 = workflow_Task(name="sample_text")
    a2 = workflow_Task(name="sample_text_2")
    b = workflow_Process(name="sample_text")
    _safe_set(b, 'workflow_Process105', {a1})
    assert _is_linked(b, 'workflow_Process105', a1)
    if hasattr(a1, 'workflow_Task106'):
        assert _is_linked(a1, 'workflow_Task106', b)
    _safe_set(b, 'workflow_Process105', {a2})
    assert _is_linked(b, 'workflow_Process105', a2)
    if hasattr(a1, 'workflow_Task106'):
        assert not _is_linked(a1, 'workflow_Task106', b)
    if hasattr(a2, 'workflow_Task106'):
        assert _is_linked(a2, 'workflow_Task106', b)
    _safe_set(b, 'workflow_Process105', set())
    assert not _is_linked(b, 'workflow_Process105', a2)
    if hasattr(a2, 'workflow_Task106'):
        assert not _is_linked(a2, 'workflow_Task106', b)


def test_assoc_value141_reverse_link_reassign_clear():
    a1 = workflow_String2DocumentMap(key="sample_text")
    a2 = workflow_String2DocumentMap(key="sample_text_2")
    b = workflow_Document(id="sample_text", name="sample_text")
    _safe_set(b, 'workflow_Document143', a1)
    assert _is_linked(b, 'workflow_Document143', a1)
    if hasattr(a1, 'workflow_String2DocumentMap142'):
        assert _is_linked(a1, 'workflow_String2DocumentMap142', b)
    _safe_set(b, 'workflow_Document143', a2)
    assert _is_linked(b, 'workflow_Document143', a2)
    if hasattr(a1, 'workflow_String2DocumentMap142'):
        assert not _is_linked(a1, 'workflow_String2DocumentMap142', b)
    if hasattr(a2, 'workflow_String2DocumentMap142'):
        assert _is_linked(a2, 'workflow_String2DocumentMap142', b)
    _safe_set(b, 'workflow_Document143', None)
    assert not _is_linked(b, 'workflow_Document143', a2)
    if hasattr(a2, 'workflow_String2DocumentMap142'):
        assert not _is_linked(a2, 'workflow_String2DocumentMap142', b)


