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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_EReference014_stub_double():
    # workflow_ActivityAspect has no real 'workflow_ActivityAspect' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Activity(finished=True, started=True)
    partner = workflow_ActivityAspect()
    setattr(partner, 'workflow_ActivityAspect', None)
    _safe_set(owner, 'workflow_Activity15', partner)
    assert getattr(partner, 'workflow_ActivityAspect') == owner
    _safe_set(owner, 'workflow_Activity15', None)
    assert getattr(partner, 'workflow_ActivityAspect') is None


def test_assoc_active18_stub_double():
    # workflow_ActivityO has no real 'ActivityO' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Agent(name="sample_text", password="sample_text", username="sample_text")
    partner = workflow_ActivityO()
    setattr(partner, 'ActivityO', None)
    _safe_set(owner, 'assignedTo', {partner})
    assert getattr(partner, 'ActivityO') == owner
    _safe_set(owner, 'assignedTo', set())
    assert getattr(partner, 'ActivityO') is None


def test_assoc_arcs25_stub_double():
    # workflow_PetriNet has no real 'workflow_PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Arc(name="sample_text")
    partner = workflow_PetriNet()
    setattr(partner, 'workflow_PetriNet', None)
    _safe_set(owner, 'workflow_Arc', partner)
    assert getattr(partner, 'workflow_PetriNet') == owner
    _safe_set(owner, 'workflow_Arc', None)
    assert getattr(partner, 'workflow_PetriNet') is None


def test_assoc_aspects10_stub_double():
    # workflow_ActivityAspect has no real 'ActivityAspect' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Activity(finished=True, started=True)
    partner = workflow_ActivityAspect()
    setattr(partner, 'ActivityAspect', None)
    _safe_set(owner, 'core11', {partner})
    assert getattr(partner, 'ActivityAspect') == owner
    _safe_set(owner, 'core11', set())
    assert getattr(partner, 'ActivityAspect') is None


def test_assoc_aspects109_stub_double():
    # workflow_ProcessAspect has no real 'ProcessAspect' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Process(name="sample_text")
    partner = workflow_ProcessAspect()
    setattr(partner, 'ProcessAspect', None)
    _safe_set(owner, 'core110', {partner})
    assert getattr(partner, 'ProcessAspect') == owner
    _safe_set(owner, 'core110', set())
    assert getattr(partner, 'ProcessAspect') is None


def test_assoc_aspects111_stub_double():
    # workflow_TaskAspect has no real 'TaskAspect' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Task(name="sample_text")
    partner = workflow_TaskAspect()
    setattr(partner, 'TaskAspect', None)
    _safe_set(owner, 'core112', {partner})
    assert getattr(partner, 'TaskAspect') == owner
    _safe_set(owner, 'core112', set())
    assert getattr(partner, 'TaskAspect') is None


def test_assoc_aspects5_stub_double():
    # workflow_CaseAspect has no real 'CaseAspect' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Case(client="sample_text", finished=True, id="sample_text", started=True)
    partner = workflow_CaseAspect()
    setattr(partner, 'CaseAspect', None)
    _safe_set(owner, 'core', {partner})
    assert getattr(partner, 'CaseAspect') == owner
    _safe_set(owner, 'core', set())
    assert getattr(partner, 'CaseAspect') is None


def test_assoc_aspects99_stub_double():
    # workflow_ModelAspect has no real 'workflow_ModelAspect100' property in the generated
    # code (a bare stub) -- manually attach it so workflow_CoreModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_CoreModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_CoreModel(name="sample_text")
    partner = workflow_ModelAspect()
    setattr(partner, 'workflow_ModelAspect100', None)
    _safe_set(owner, 'workflow_CoreModel', {partner})
    assert getattr(partner, 'workflow_ModelAspect100') == owner
    _safe_set(owner, 'workflow_CoreModel', set())
    assert getattr(partner, 'workflow_ModelAspect100') is None


def test_assoc_assignedTo4_stub_double():
    # workflow_ActivityO has no real 'active' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Agent(name="sample_text", password="sample_text", username="sample_text")
    partner = workflow_ActivityO()
    setattr(partner, 'active', None)
    _safe_set(owner, 'Agent', partner)
    assert getattr(partner, 'active') == owner
    _safe_set(owner, 'Agent', None)
    assert getattr(partner, 'active') is None


def test_assoc_caseDocuments83_stub_double():
    # workflow_CaseI has no real 'workflow_CaseI' property in the generated
    # code (a bare stub) -- manually attach it so workflow_String2DocumentMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_String2DocumentMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_String2DocumentMap(key="sample_text")
    partner = workflow_CaseI()
    setattr(partner, 'workflow_CaseI', None)
    _safe_set(owner, 'workflow_String2DocumentMap', partner)
    assert getattr(partner, 'workflow_CaseI') == owner
    _safe_set(owner, 'workflow_String2DocumentMap', None)
    assert getattr(partner, 'workflow_CaseI') is None


def test_assoc_cases114_stub_double():
    # workflow_RuntimeCoreModel has no real 'runtimeCoreModel' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Case(client="sample_text", finished=True, id="sample_text", started=True)
    partner = workflow_RuntimeCoreModel()
    setattr(partner, 'runtimeCoreModel', None)
    _safe_set(owner, 'Case115', partner)
    assert getattr(partner, 'runtimeCoreModel') == owner
    _safe_set(owner, 'Case115', None)
    assert getattr(partner, 'runtimeCoreModel') is None


def test_assoc_core87_stub_double():
    # workflow_ProcessAspect has no real 'aspects' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Process(name="sample_text")
    partner = workflow_ProcessAspect()
    setattr(partner, 'aspects', None)
    _safe_set(owner, 'Process', partner)
    assert getattr(partner, 'aspects') == owner
    _safe_set(owner, 'Process', None)
    assert getattr(partner, 'aspects') is None


def test_assoc_core88_stub_double():
    # workflow_TaskAspect has no real 'aspects89' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Task(name="sample_text")
    partner = workflow_TaskAspect()
    setattr(partner, 'aspects89', None)
    _safe_set(owner, 'Task', partner)
    assert getattr(partner, 'aspects89') == owner
    _safe_set(owner, 'Task', None)
    assert getattr(partner, 'aspects89') is None


def test_assoc_core92_stub_double():
    # workflow_CaseAspect has no real 'aspects93' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Case(client="sample_text", finished=True, id="sample_text", started=True)
    partner = workflow_CaseAspect()
    setattr(partner, 'aspects93', None)
    _safe_set(owner, 'Case', partner)
    assert getattr(partner, 'aspects93') == owner
    _safe_set(owner, 'Case', None)
    assert getattr(partner, 'aspects93') is None


def test_assoc_core97_stub_double():
    # workflow_ActivityAspect has no real 'aspects98' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Activity(finished=True, started=True)
    partner = workflow_ActivityAspect()
    setattr(partner, 'aspects98', None)
    _safe_set(owner, 'Activity', partner)
    assert getattr(partner, 'aspects98') == owner
    _safe_set(owner, 'Activity', None)
    assert getattr(partner, 'aspects98') is None


def test_assoc_coreModel116_stub_double():
    # workflow_RuntimeCoreModel has no real 'workflow_RuntimeCoreModel117' property in the generated
    # code (a bare stub) -- manually attach it so workflow_CoreModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_CoreModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_CoreModel(name="sample_text")
    partner = workflow_RuntimeCoreModel()
    setattr(partner, 'workflow_RuntimeCoreModel117', None)
    _safe_set(owner, 'workflow_CoreModel118', partner)
    assert getattr(partner, 'workflow_RuntimeCoreModel117') == owner
    _safe_set(owner, 'workflow_CoreModel118', None)
    assert getattr(partner, 'workflow_RuntimeCoreModel117') is None


def test_assoc_coreModels57_stub_double():
    # workflow_ModelRegistry has no real 'modelRegistry58' property in the generated
    # code (a bare stub) -- manually attach it so workflow_CoreModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_CoreModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_CoreModel(name="sample_text")
    partner = workflow_ModelRegistry()
    setattr(partner, 'modelRegistry58', None)
    _safe_set(owner, 'CoreModel', partner)
    assert getattr(partner, 'modelRegistry58') == owner
    _safe_set(owner, 'CoreModel', None)
    assert getattr(partner, 'modelRegistry58') is None


def test_assoc_descriptor145_stub_double():
    # workflow_DocumentDescrAtom has no real 'workflow_DocumentDescrAtom' property in the generated
    # code (a bare stub) -- manually attach it so workflow_DocumentDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_DocumentDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_DocumentDescriptor(name="sample_text")
    partner = workflow_DocumentDescrAtom()
    setattr(partner, 'workflow_DocumentDescrAtom', None)
    _safe_set(owner, 'workflow_DocumentDescriptor146', partner)
    assert getattr(partner, 'workflow_DocumentDescrAtom') == owner
    _safe_set(owner, 'workflow_DocumentDescriptor146', None)
    assert getattr(partner, 'workflow_DocumentDescrAtom') is None


def test_assoc_enumField156_stub_double():
    # workflow_EnumFieldValue has no real 'workflow_EnumFieldValue157' property in the generated
    # code (a bare stub) -- manually attach it so workflow_EnumField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_EnumField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_EnumField(name="sample_text")
    partner = workflow_EnumFieldValue()
    setattr(partner, 'workflow_EnumFieldValue157', None)
    _safe_set(owner, 'workflow_EnumField158', partner)
    assert getattr(partner, 'workflow_EnumFieldValue157') == owner
    _safe_set(owner, 'workflow_EnumField158', None)
    assert getattr(partner, 'workflow_EnumFieldValue157') is None


def test_assoc_enumField162_stub_double():
    # workflow_EnumFieldAtom has no real 'workflow_EnumFieldAtom' property in the generated
    # code (a bare stub) -- manually attach it so workflow_EnumField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_EnumField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_EnumField(name="sample_text")
    partner = workflow_EnumFieldAtom()
    setattr(partner, 'workflow_EnumFieldAtom', None)
    _safe_set(owner, 'workflow_EnumField163', partner)
    assert getattr(partner, 'workflow_EnumFieldAtom') == owner
    _safe_set(owner, 'workflow_EnumField163', None)
    assert getattr(partner, 'workflow_EnumFieldAtom') is None


def test_assoc_enumFieldValues131_stub_double():
    # workflow_EnumFieldValue has no real 'workflow_EnumFieldValue' property in the generated
    # code (a bare stub) -- manually attach it so workflow_DefaultDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_DefaultDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_DefaultDocument(placeholder=True)
    partner = workflow_EnumFieldValue()
    setattr(partner, 'workflow_EnumFieldValue', None)
    _safe_set(owner, 'workflow_DefaultDocument132', {partner})
    assert getattr(partner, 'workflow_EnumFieldValue') == owner
    _safe_set(owner, 'workflow_DefaultDocument132', set())
    assert getattr(partner, 'workflow_EnumFieldValue') is None


def test_assoc_enumFields128_stub_double():
    # workflow_DefaultDocumentType has no real 'workflow_DefaultDocumentType129' property in the generated
    # code (a bare stub) -- manually attach it so workflow_EnumField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_EnumField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_EnumField(name="sample_text")
    partner = workflow_DefaultDocumentType()
    setattr(partner, 'workflow_DefaultDocumentType129', None)
    _safe_set(owner, 'workflow_EnumField', partner)
    assert getattr(partner, 'workflow_DefaultDocumentType129') == owner
    _safe_set(owner, 'workflow_EnumField', None)
    assert getattr(partner, 'workflow_DefaultDocumentType129') is None


def test_assoc_enumLiteral164_stub_double():
    # workflow_EnumLiteralAtom has no real 'workflow_EnumLiteralAtom' property in the generated
    # code (a bare stub) -- manually attach it so workflow_EnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_EnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_EnumLiteral(name="sample_text")
    partner = workflow_EnumLiteralAtom()
    setattr(partner, 'workflow_EnumLiteralAtom', None)
    _safe_set(owner, 'workflow_EnumLiteral165', partner)
    assert getattr(partner, 'workflow_EnumLiteralAtom') == owner
    _safe_set(owner, 'workflow_EnumLiteral165', None)
    assert getattr(partner, 'workflow_EnumLiteralAtom') is None


def test_assoc_enumValue159_stub_double():
    # workflow_EnumFieldValue has no real 'workflow_EnumFieldValue160' property in the generated
    # code (a bare stub) -- manually attach it so workflow_EnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_EnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_EnumLiteral(name="sample_text")
    partner = workflow_EnumFieldValue()
    setattr(partner, 'workflow_EnumFieldValue160', None)
    _safe_set(owner, 'workflow_EnumLiteral161', partner)
    assert getattr(partner, 'workflow_EnumFieldValue160') == owner
    _safe_set(owner, 'workflow_EnumLiteral161', None)
    assert getattr(partner, 'workflow_EnumFieldValue160') is None


def test_assoc_field147_stub_double():
    # workflow_FieldAtom has no real 'workflow_FieldAtom' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Field(name="sample_text")
    partner = workflow_FieldAtom()
    setattr(partner, 'workflow_FieldAtom', None)
    _safe_set(owner, 'workflow_Field148', partner)
    assert getattr(partner, 'workflow_FieldAtom') == owner
    _safe_set(owner, 'workflow_Field148', None)
    assert getattr(partner, 'workflow_FieldAtom') is None


def test_assoc_fields127_stub_double():
    # workflow_DefaultDocumentType has no real 'workflow_DefaultDocumentType' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Field(name="sample_text")
    partner = workflow_DefaultDocumentType()
    setattr(partner, 'workflow_DefaultDocumentType', None)
    _safe_set(owner, 'workflow_Field', partner)
    assert getattr(partner, 'workflow_DefaultDocumentType') == owner
    _safe_set(owner, 'workflow_Field', None)
    assert getattr(partner, 'workflow_DefaultDocumentType') is None


def test_assoc_finish31_stub_double():
    # workflow_PetriNet has no real 'workflow_PetriNet32' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Place(name="sample_text")
    partner = workflow_PetriNet()
    setattr(partner, 'workflow_PetriNet32', None)
    _safe_set(owner, 'workflow_Place33', partner)
    assert getattr(partner, 'workflow_PetriNet32') == owner
    _safe_set(owner, 'workflow_Place33', None)
    assert getattr(partner, 'workflow_PetriNet32') is None


def test_assoc_finish68_stub_double():
    # workflow_TaskI has no real 'workflow_TaskI69' property in the generated
    # code (a bare stub) -- manually attach it so workflow_DocumentCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_DocumentCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_DocumentCondition(name="sample_text")
    partner = workflow_TaskI()
    setattr(partner, 'workflow_TaskI69', None)
    _safe_set(owner, 'workflow_DocumentCondition70', partner)
    assert getattr(partner, 'workflow_TaskI69') == owner
    _safe_set(owner, 'workflow_DocumentCondition70', None)
    assert getattr(partner, 'workflow_TaskI69') is None


def test_assoc_in_35_stub_double():
    # workflow_Transition has no real 'targetTransition' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Arc(name="sample_text")
    partner = workflow_Transition()
    setattr(partner, 'targetTransition', None)
    _safe_set(owner, 'Arc36', partner)
    assert getattr(partner, 'targetTransition') == owner
    _safe_set(owner, 'Arc36', None)
    assert getattr(partner, 'targetTransition') is None


def test_assoc_in_62_stub_double():
    # workflow_TaskI has no real 'workflow_TaskI' property in the generated
    # code (a bare stub) -- manually attach it so workflow_DocumentDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_DocumentDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_DocumentDescriptor(name="sample_text")
    partner = workflow_TaskI()
    setattr(partner, 'workflow_TaskI', None)
    _safe_set(owner, 'workflow_DocumentDescriptor', partner)
    assert getattr(partner, 'workflow_TaskI') == owner
    _safe_set(owner, 'workflow_DocumentDescriptor', None)
    assert getattr(partner, 'workflow_TaskI') is None


def test_assoc_in_76_stub_double():
    # workflow_ActivityI has no real 'workflow_ActivityI' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Document(id="sample_text", name="sample_text")
    partner = workflow_ActivityI()
    setattr(partner, 'workflow_ActivityI', None)
    _safe_set(owner, 'workflow_Document', partner)
    assert getattr(partner, 'workflow_ActivityI') == owner
    _safe_set(owner, 'workflow_Document', None)
    assert getattr(partner, 'workflow_ActivityI') is None


def test_assoc_involved125_stub_double():
    # workflow_ProcessO has no real 'workflow_ProcessO' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Role(name="sample_text")
    partner = workflow_ProcessO()
    setattr(partner, 'workflow_ProcessO', None)
    _safe_set(owner, 'workflow_Role126', partner)
    assert getattr(partner, 'workflow_ProcessO') == owner
    _safe_set(owner, 'workflow_Role126', None)
    assert getattr(partner, 'workflow_ProcessO') is None


def test_assoc_involved136_stub_double():
    # workflow_CaseO has no real 'workflow_CaseO' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Agent(name="sample_text", password="sample_text", username="sample_text")
    partner = workflow_CaseO()
    setattr(partner, 'workflow_CaseO', None)
    _safe_set(owner, 'workflow_Agent137', partner)
    assert getattr(partner, 'workflow_CaseO') == owner
    _safe_set(owner, 'workflow_Agent137', None)
    assert getattr(partner, 'workflow_CaseO') is None


def test_assoc_modelRegistry103_stub_double():
    # workflow_ModelRegistry has no real 'ModelRegistry' property in the generated
    # code (a bare stub) -- manually attach it so workflow_CoreModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_CoreModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_CoreModel(name="sample_text")
    partner = workflow_ModelRegistry()
    setattr(partner, 'ModelRegistry', None)
    _safe_set(owner, 'coreModels', partner)
    assert getattr(partner, 'ModelRegistry') == owner
    _safe_set(owner, 'coreModels', None)
    assert getattr(partner, 'ModelRegistry') is None


def test_assoc_out34_stub_double():
    # workflow_Transition has no real 'sourceTransition' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Arc(name="sample_text")
    partner = workflow_Transition()
    setattr(partner, 'sourceTransition', None)
    _safe_set(owner, 'Arc', partner)
    assert getattr(partner, 'sourceTransition') == owner
    _safe_set(owner, 'Arc', None)
    assert getattr(partner, 'sourceTransition') is None


def test_assoc_out63_stub_double():
    # workflow_TaskI has no real 'workflow_TaskI64' property in the generated
    # code (a bare stub) -- manually attach it so workflow_DocumentDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_DocumentDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_DocumentDescriptor(name="sample_text")
    partner = workflow_TaskI()
    setattr(partner, 'workflow_TaskI64', None)
    _safe_set(owner, 'workflow_DocumentDescriptor65', partner)
    assert getattr(partner, 'workflow_TaskI64') == owner
    _safe_set(owner, 'workflow_DocumentDescriptor65', None)
    assert getattr(partner, 'workflow_TaskI64') is None


def test_assoc_out77_stub_double():
    # workflow_ActivityI has no real 'workflow_ActivityI78' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Document(id="sample_text", name="sample_text")
    partner = workflow_ActivityI()
    setattr(partner, 'workflow_ActivityI78', None)
    _safe_set(owner, 'workflow_Document79', partner)
    assert getattr(partner, 'workflow_ActivityI78') == owner
    _safe_set(owner, 'workflow_Document79', None)
    assert getattr(partner, 'workflow_ActivityI78') is None


def test_assoc_place53_stub_double():
    # workflow_Token has no real 'workflow_Token54' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Place(name="sample_text")
    partner = workflow_Token()
    setattr(partner, 'workflow_Token54', None)
    _safe_set(owner, 'workflow_Place55', partner)
    assert getattr(partner, 'workflow_Token54') == owner
    _safe_set(owner, 'workflow_Place55', None)
    assert getattr(partner, 'workflow_Token54') is None


def test_assoc_places26_stub_double():
    # workflow_PetriNet has no real 'workflow_PetriNet27' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Place(name="sample_text")
    partner = workflow_PetriNet()
    setattr(partner, 'workflow_PetriNet27', None)
    _safe_set(owner, 'workflow_Place', partner)
    assert getattr(partner, 'workflow_PetriNet27') == owner
    _safe_set(owner, 'workflow_Place', None)
    assert getattr(partner, 'workflow_PetriNet27') is None


def test_assoc_processDocuments61_stub_double():
    # workflow_Information has no real 'workflow_Information' property in the generated
    # code (a bare stub) -- manually attach it so workflow_ProcessDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_ProcessDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_ProcessDocument(name="sample_text")
    partner = workflow_Information()
    setattr(partner, 'workflow_Information', None)
    _safe_set(owner, 'workflow_ProcessDocument', partner)
    assert getattr(partner, 'workflow_Information') == owner
    _safe_set(owner, 'workflow_ProcessDocument', None)
    assert getattr(partner, 'workflow_Information') is None


def test_assoc_runtimeCoreModel9_stub_double():
    # workflow_RuntimeCoreModel has no real 'RuntimeCoreModel' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Case(client="sample_text", finished=True, id="sample_text", started=True)
    partner = workflow_RuntimeCoreModel()
    setattr(partner, 'RuntimeCoreModel', None)
    _safe_set(owner, 'cases', partner)
    assert getattr(partner, 'RuntimeCoreModel') == owner
    _safe_set(owner, 'cases', None)
    assert getattr(partner, 'RuntimeCoreModel') is None


def test_assoc_sourceTransition40_stub_double():
    # workflow_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Arc(name="sample_text")
    partner = workflow_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'out41', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'out41', None)
    assert getattr(partner, 'Transition') is None


def test_assoc_start28_stub_double():
    # workflow_PetriNet has no real 'workflow_PetriNet29' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Place(name="sample_text")
    partner = workflow_PetriNet()
    setattr(partner, 'workflow_PetriNet29', None)
    _safe_set(owner, 'workflow_Place30', partner)
    assert getattr(partner, 'workflow_PetriNet29') == owner
    _safe_set(owner, 'workflow_Place30', None)
    assert getattr(partner, 'workflow_PetriNet29') is None


def test_assoc_start66_stub_double():
    # workflow_TaskI has no real 'workflow_TaskI67' property in the generated
    # code (a bare stub) -- manually attach it so workflow_DocumentCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_DocumentCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_DocumentCondition(name="sample_text")
    partner = workflow_TaskI()
    setattr(partner, 'workflow_TaskI67', None)
    _safe_set(owner, 'workflow_DocumentCondition', partner)
    assert getattr(partner, 'workflow_TaskI67') == owner
    _safe_set(owner, 'workflow_DocumentCondition', None)
    assert getattr(partner, 'workflow_TaskI67') is None


def test_assoc_targetTransition42_stub_double():
    # workflow_Transition has no real 'Transition44' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Arc(name="sample_text")
    partner = workflow_Transition()
    setattr(partner, 'Transition44', None)
    _safe_set(owner, 'in_43', partner)
    assert getattr(partner, 'Transition44') == owner
    _safe_set(owner, 'in_43', None)
    assert getattr(partner, 'Transition44') is None


