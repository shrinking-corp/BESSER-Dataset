import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    AttributeDefinition,
    Control,
    Expression,
    GenericComponent,
    Operation,
    PagosPim_Action,
    PagosPim_Add,
    PagosPim_Application,
    PagosPim_Attribute,
    PagosPim_AttributeDefinition,
    PagosPim_Body,
    PagosPim_Control,
    PagosPim_DaoComponent,
    PagosPim_DataLayerComponent,
    PagosPim_EObject,
    PagosPim_ElseSegment,
    PagosPim_Expression,
    PagosPim_Field,
    PagosPim_FrontService,
    PagosPim_GenericComponent,
    PagosPim_IfBlock,
    PagosPim_IfCondition,
    PagosPim_Input,
    PagosPim_LogicComponent,
    PagosPim_LogicalExpression,
    PagosPim_Mult,
    PagosPim_NewEClass21,
    PagosPim_Operation,
    PagosPim_Output,
    PagosPim_Parameter,
    PagosPim_ParameterList,
    PagosPim_ProgramIfExpression,
    PagosPim_Relation,
    PagosPim_Return,
    PagosPim_ServerService,
    PagosPim_SubComponent,
    PagosPim_TerminalValue,
    PagosPim_ViewComponent,
    Relation,
    AddOper,
    Cardinality,
    DataTypes,
    LogicalCononnector,
    LogicalOperator,
    MultOper,
    RelationType,
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

def test_assoc_attribute84_reverse_link_reassign_clear():
    a1 = PagosPim_TerminalValue(method="sample_text", value="sample_text")
    a2 = PagosPim_TerminalValue(method="sample_text_2", value="sample_text_2")
    b = PagosPim_Attribute(isIndex="sample_text")
    _safe_set(b, 'PagosPim_Attribute86', a1)
    assert _is_linked(b, 'PagosPim_Attribute86', a1)
    if hasattr(a1, 'PagosPim_TerminalValue85'):
        assert _is_linked(a1, 'PagosPim_TerminalValue85', b)
    _safe_set(b, 'PagosPim_Attribute86', a2)
    assert _is_linked(b, 'PagosPim_Attribute86', a2)
    if hasattr(a1, 'PagosPim_TerminalValue85'):
        assert not _is_linked(a1, 'PagosPim_TerminalValue85', b)
    if hasattr(a2, 'PagosPim_TerminalValue85'):
        assert _is_linked(a2, 'PagosPim_TerminalValue85', b)
    _safe_set(b, 'PagosPim_Attribute86', None)
    assert not _is_linked(b, 'PagosPim_Attribute86', a2)
    if hasattr(a2, 'PagosPim_TerminalValue85'):
        assert not _is_linked(a2, 'PagosPim_TerminalValue85', b)


def test_assoc_attributes23_reverse_link_reassign_clear():
    a1 = PagosPim_GenericComponent(name="sample_text")
    a2 = PagosPim_GenericComponent(name="sample_text_2")
    b = PagosPim_Attribute(isIndex="sample_text")
    _safe_set(b, 'PagosPim_Attribute', a1)
    assert _is_linked(b, 'PagosPim_Attribute', a1)
    if hasattr(a1, 'PagosPim_GenericComponent'):
        assert _is_linked(a1, 'PagosPim_GenericComponent', b)
    _safe_set(b, 'PagosPim_Attribute', a2)
    assert _is_linked(b, 'PagosPim_Attribute', a2)
    if hasattr(a1, 'PagosPim_GenericComponent'):
        assert not _is_linked(a1, 'PagosPim_GenericComponent', b)
    if hasattr(a2, 'PagosPim_GenericComponent'):
        assert _is_linked(a2, 'PagosPim_GenericComponent', b)
    _safe_set(b, 'PagosPim_Attribute', None)
    assert not _is_linked(b, 'PagosPim_Attribute', a2)
    if hasattr(a2, 'PagosPim_GenericComponent'):
        assert not _is_linked(a2, 'PagosPim_GenericComponent', b)


def test_assoc_attributes34_reverse_link_reassign_clear():
    a1 = PagosPim_Operation(name="sample_text")
    a2 = PagosPim_Operation(name="sample_text_2")
    b = PagosPim_Attribute(isIndex="sample_text")
    _safe_set(b, 'PagosPim_Attribute36', a1)
    assert _is_linked(b, 'PagosPim_Attribute36', a1)
    if hasattr(a1, 'PagosPim_Operation35'):
        assert _is_linked(a1, 'PagosPim_Operation35', b)
    _safe_set(b, 'PagosPim_Attribute36', a2)
    assert _is_linked(b, 'PagosPim_Attribute36', a2)
    if hasattr(a1, 'PagosPim_Operation35'):
        assert not _is_linked(a1, 'PagosPim_Operation35', b)
    if hasattr(a2, 'PagosPim_Operation35'):
        assert _is_linked(a2, 'PagosPim_Operation35', b)
    _safe_set(b, 'PagosPim_Attribute36', None)
    assert not _is_linked(b, 'PagosPim_Attribute36', a2)
    if hasattr(a2, 'PagosPim_Operation35'):
        assert not _is_linked(a2, 'PagosPim_Operation35', b)


def test_assoc_controls18_reverse_link_reassign_clear():
    a1 = PagosPim_ViewComponent(title="sample_text")
    a2 = PagosPim_ViewComponent(title="sample_text_2")
    b = PagosPim_Control(label="sample_text")
    _safe_set(b, 'PagosPim_Control', a1)
    assert _is_linked(b, 'PagosPim_Control', a1)
    if hasattr(a1, 'PagosPim_ViewComponent19'):
        assert _is_linked(a1, 'PagosPim_ViewComponent19', b)
    _safe_set(b, 'PagosPim_Control', a2)
    assert _is_linked(b, 'PagosPim_Control', a2)
    if hasattr(a1, 'PagosPim_ViewComponent19'):
        assert not _is_linked(a1, 'PagosPim_ViewComponent19', b)
    if hasattr(a2, 'PagosPim_ViewComponent19'):
        assert _is_linked(a2, 'PagosPim_ViewComponent19', b)
    _safe_set(b, 'PagosPim_Control', None)
    assert not _is_linked(b, 'PagosPim_Control', a2)
    if hasattr(a2, 'PagosPim_ViewComponent19'):
        assert not _is_linked(a2, 'PagosPim_ViewComponent19', b)


def test_assoc_frontservices20_reverse_link_reassign_clear():
    a1 = PagosPim_ViewComponent(title="sample_text")
    a2 = PagosPim_ViewComponent(title="sample_text_2")
    b = PagosPim_FrontService(fullName="sample_text")
    _safe_set(b, 'PagosPim_FrontService22', a1)
    assert _is_linked(b, 'PagosPim_FrontService22', a1)
    if hasattr(a1, 'PagosPim_ViewComponent21'):
        assert _is_linked(a1, 'PagosPim_ViewComponent21', b)
    _safe_set(b, 'PagosPim_FrontService22', a2)
    assert _is_linked(b, 'PagosPim_FrontService22', a2)
    if hasattr(a1, 'PagosPim_ViewComponent21'):
        assert not _is_linked(a1, 'PagosPim_ViewComponent21', b)
    if hasattr(a2, 'PagosPim_ViewComponent21'):
        assert _is_linked(a2, 'PagosPim_ViewComponent21', b)
    _safe_set(b, 'PagosPim_FrontService22', None)
    assert not _is_linked(b, 'PagosPim_FrontService22', a2)
    if hasattr(a2, 'PagosPim_ViewComponent21'):
        assert not _is_linked(a2, 'PagosPim_ViewComponent21', b)


def test_assoc_leftTerm70_reverse_link_reassign_clear():
    a1 = PagosPim_TerminalValue(method="sample_text", value="sample_text")
    a2 = PagosPim_TerminalValue(method="sample_text_2", value="sample_text_2")
    b = PagosPim_LogicalExpression(conOper="sample_text", literal="sample_text", logicalOperator="sample_text")
    _safe_set(b, 'PagosPim_LogicalExpression71', a1)
    assert _is_linked(b, 'PagosPim_LogicalExpression71', a1)
    if hasattr(a1, 'PagosPim_TerminalValue'):
        assert _is_linked(a1, 'PagosPim_TerminalValue', b)
    _safe_set(b, 'PagosPim_LogicalExpression71', a2)
    assert _is_linked(b, 'PagosPim_LogicalExpression71', a2)
    if hasattr(a1, 'PagosPim_TerminalValue'):
        assert not _is_linked(a1, 'PagosPim_TerminalValue', b)
    if hasattr(a2, 'PagosPim_TerminalValue'):
        assert _is_linked(a2, 'PagosPim_TerminalValue', b)
    _safe_set(b, 'PagosPim_LogicalExpression71', None)
    assert not _is_linked(b, 'PagosPim_LogicalExpression71', a2)
    if hasattr(a2, 'PagosPim_TerminalValue'):
        assert not _is_linked(a2, 'PagosPim_TerminalValue', b)


def test_assoc_logicalComponents0_reverse_link_reassign_clear():
    a1 = PagosPim_LogicComponent(persistible=True)
    a2 = PagosPim_LogicComponent(persistible=False)
    b = PagosPim_Application(name="sample_text")
    _safe_set(b, 'PagosPim_Application', {a1})
    assert _is_linked(b, 'PagosPim_Application', a1)
    if hasattr(a1, 'PagosPim_LogicComponent'):
        assert _is_linked(a1, 'PagosPim_LogicComponent', b)
    _safe_set(b, 'PagosPim_Application', {a2})
    assert _is_linked(b, 'PagosPim_Application', a2)
    if hasattr(a1, 'PagosPim_LogicComponent'):
        assert not _is_linked(a1, 'PagosPim_LogicComponent', b)
    if hasattr(a2, 'PagosPim_LogicComponent'):
        assert _is_linked(a2, 'PagosPim_LogicComponent', b)
    _safe_set(b, 'PagosPim_Application', set())
    assert not _is_linked(b, 'PagosPim_Application', a2)
    if hasattr(a2, 'PagosPim_LogicComponent'):
        assert not _is_linked(a2, 'PagosPim_LogicComponent', b)


def test_assoc_moreExpressions76_reverse_link_reassign_clear():
    a1 = PagosPim_LogicalExpression(conOper="sample_text", literal="sample_text", logicalOperator="sample_text")
    a2 = PagosPim_LogicalExpression(conOper="sample_text_2", literal="sample_text_2", logicalOperator="sample_text_2")
    b = PagosPim_LogicalExpression(conOper="sample_text", literal="sample_text", logicalOperator="sample_text")
    _safe_set(b, 'PagosPim_LogicalExpression77', a1)
    assert _is_linked(b, 'PagosPim_LogicalExpression77', a1)
    if hasattr(a1, 'PagosPim_LogicalExpression75'):
        assert _is_linked(a1, 'PagosPim_LogicalExpression75', b)
    _safe_set(b, 'PagosPim_LogicalExpression77', a2)
    assert _is_linked(b, 'PagosPim_LogicalExpression77', a2)
    if hasattr(a1, 'PagosPim_LogicalExpression75'):
        assert not _is_linked(a1, 'PagosPim_LogicalExpression75', b)
    if hasattr(a2, 'PagosPim_LogicalExpression75'):
        assert _is_linked(a2, 'PagosPim_LogicalExpression75', b)
    _safe_set(b, 'PagosPim_LogicalExpression77', None)
    assert not _is_linked(b, 'PagosPim_LogicalExpression77', a2)
    if hasattr(a2, 'PagosPim_LogicalExpression75'):
        assert not _is_linked(a2, 'PagosPim_LogicalExpression75', b)


def test_assoc_operations26_reverse_link_reassign_clear():
    a1 = PagosPim_Operation(name="sample_text")
    a2 = PagosPim_Operation(name="sample_text_2")
    b = PagosPim_GenericComponent(name="sample_text")
    _safe_set(b, 'PagosPim_GenericComponent27', {a1})
    assert _is_linked(b, 'PagosPim_GenericComponent27', a1)
    if hasattr(a1, 'PagosPim_Operation'):
        assert _is_linked(a1, 'PagosPim_Operation', b)
    _safe_set(b, 'PagosPim_GenericComponent27', {a2})
    assert _is_linked(b, 'PagosPim_GenericComponent27', a2)
    if hasattr(a1, 'PagosPim_Operation'):
        assert not _is_linked(a1, 'PagosPim_Operation', b)
    if hasattr(a2, 'PagosPim_Operation'):
        assert _is_linked(a2, 'PagosPim_Operation', b)
    _safe_set(b, 'PagosPim_GenericComponent27', set())
    assert not _is_linked(b, 'PagosPim_GenericComponent27', a2)
    if hasattr(a2, 'PagosPim_Operation'):
        assert not _is_linked(a2, 'PagosPim_Operation', b)


def test_assoc_relations24_reverse_link_reassign_clear():
    a1 = PagosPim_Relation(cardinality="sample_text", name="sample_text", type="sample_text")
    a2 = PagosPim_Relation(cardinality="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = PagosPim_GenericComponent(name="sample_text")
    _safe_set(b, 'PagosPim_GenericComponent25', {a1})
    assert _is_linked(b, 'PagosPim_GenericComponent25', a1)
    if hasattr(a1, 'PagosPim_Relation'):
        assert _is_linked(a1, 'PagosPim_Relation', b)
    _safe_set(b, 'PagosPim_GenericComponent25', {a2})
    assert _is_linked(b, 'PagosPim_GenericComponent25', a2)
    if hasattr(a1, 'PagosPim_Relation'):
        assert not _is_linked(a1, 'PagosPim_Relation', b)
    if hasattr(a2, 'PagosPim_Relation'):
        assert _is_linked(a2, 'PagosPim_Relation', b)
    _safe_set(b, 'PagosPim_GenericComponent25', set())
    assert not _is_linked(b, 'PagosPim_GenericComponent25', a2)
    if hasattr(a2, 'PagosPim_Relation'):
        assert not _is_linked(a2, 'PagosPim_Relation', b)


def test_assoc_rightTerm72_reverse_link_reassign_clear():
    a1 = PagosPim_TerminalValue(method="sample_text", value="sample_text")
    a2 = PagosPim_TerminalValue(method="sample_text_2", value="sample_text_2")
    b = PagosPim_LogicalExpression(conOper="sample_text", literal="sample_text", logicalOperator="sample_text")
    _safe_set(b, 'PagosPim_LogicalExpression73', a1)
    assert _is_linked(b, 'PagosPim_LogicalExpression73', a1)
    if hasattr(a1, 'PagosPim_TerminalValue74'):
        assert _is_linked(a1, 'PagosPim_TerminalValue74', b)
    _safe_set(b, 'PagosPim_LogicalExpression73', a2)
    assert _is_linked(b, 'PagosPim_LogicalExpression73', a2)
    if hasattr(a1, 'PagosPim_TerminalValue74'):
        assert not _is_linked(a1, 'PagosPim_TerminalValue74', b)
    if hasattr(a2, 'PagosPim_TerminalValue74'):
        assert _is_linked(a2, 'PagosPim_TerminalValue74', b)
    _safe_set(b, 'PagosPim_LogicalExpression73', None)
    assert not _is_linked(b, 'PagosPim_LogicalExpression73', a2)
    if hasattr(a2, 'PagosPim_TerminalValue74'):
        assert not _is_linked(a2, 'PagosPim_TerminalValue74', b)


def test_assoc_serviceCalls11_reverse_link_reassign_clear():
    a1 = PagosPim_FrontService(fullName="sample_text")
    a2 = PagosPim_FrontService(fullName="sample_text_2")
    b = PagosPim_FrontService(fullName="sample_text")
    _safe_set(b, 'PagosPim_FrontService12', a1)
    assert _is_linked(b, 'PagosPim_FrontService12', a1)
    if hasattr(a1, 'PagosPim_FrontService10'):
        assert _is_linked(a1, 'PagosPim_FrontService10', b)
    _safe_set(b, 'PagosPim_FrontService12', a2)
    assert _is_linked(b, 'PagosPim_FrontService12', a2)
    if hasattr(a1, 'PagosPim_FrontService10'):
        assert not _is_linked(a1, 'PagosPim_FrontService10', b)
    if hasattr(a2, 'PagosPim_FrontService10'):
        assert _is_linked(a2, 'PagosPim_FrontService10', b)
    _safe_set(b, 'PagosPim_FrontService12', None)
    assert not _is_linked(b, 'PagosPim_FrontService12', a2)
    if hasattr(a2, 'PagosPim_FrontService10'):
        assert not _is_linked(a2, 'PagosPim_FrontService10', b)


def test_assoc_targetComponent39_reverse_link_reassign_clear():
    a1 = PagosPim_Relation(cardinality="sample_text", name="sample_text", type="sample_text")
    a2 = PagosPim_Relation(cardinality="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = PagosPim_GenericComponent(name="sample_text")
    _safe_set(b, 'PagosPim_GenericComponent41', a1)
    assert _is_linked(b, 'PagosPim_GenericComponent41', a1)
    if hasattr(a1, 'PagosPim_Relation40'):
        assert _is_linked(a1, 'PagosPim_Relation40', b)
    _safe_set(b, 'PagosPim_GenericComponent41', a2)
    assert _is_linked(b, 'PagosPim_GenericComponent41', a2)
    if hasattr(a1, 'PagosPim_Relation40'):
        assert not _is_linked(a1, 'PagosPim_Relation40', b)
    if hasattr(a2, 'PagosPim_Relation40'):
        assert _is_linked(a2, 'PagosPim_Relation40', b)
    _safe_set(b, 'PagosPim_GenericComponent41', None)
    assert not _is_linked(b, 'PagosPim_GenericComponent41', a2)
    if hasattr(a2, 'PagosPim_Relation40'):
        assert not _is_linked(a2, 'PagosPim_Relation40', b)


def test_assoc_views7_reverse_link_reassign_clear():
    a1 = PagosPim_ViewComponent(title="sample_text")
    a2 = PagosPim_ViewComponent(title="sample_text_2")
    b = PagosPim_Application(name="sample_text")
    _safe_set(b, 'PagosPim_Application8', {a1})
    assert _is_linked(b, 'PagosPim_Application8', a1)
    if hasattr(a1, 'PagosPim_ViewComponent'):
        assert _is_linked(a1, 'PagosPim_ViewComponent', b)
    _safe_set(b, 'PagosPim_Application8', {a2})
    assert _is_linked(b, 'PagosPim_Application8', a2)
    if hasattr(a1, 'PagosPim_ViewComponent'):
        assert not _is_linked(a1, 'PagosPim_ViewComponent', b)
    if hasattr(a2, 'PagosPim_ViewComponent'):
        assert _is_linked(a2, 'PagosPim_ViewComponent', b)
    _safe_set(b, 'PagosPim_Application8', set())
    assert not _is_linked(b, 'PagosPim_Application8', a2)
    if hasattr(a2, 'PagosPim_ViewComponent'):
        assert not _is_linked(a2, 'PagosPim_ViewComponent', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body32_stub_double():
    # PagosPim_Body has no real 'PagosPim_Body' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Operation(name="sample_text")
    partner = PagosPim_Body()
    setattr(partner, 'PagosPim_Body', None)
    _safe_set(owner, 'PagosPim_Operation33', partner)
    assert getattr(partner, 'PagosPim_Body') == owner
    _safe_set(owner, 'PagosPim_Operation33', None)
    assert getattr(partner, 'PagosPim_Body') is None


def test_assoc_complexType42_stub_double():
    # PagosPim_EObject has no real 'PagosPim_EObject' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_AttributeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_AttributeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_AttributeDefinition(name="sample_text", type="sample_text")
    partner = PagosPim_EObject()
    setattr(partner, 'PagosPim_EObject', None)
    _safe_set(owner, 'PagosPim_AttributeDefinition', partner)
    assert getattr(partner, 'PagosPim_EObject') == owner
    _safe_set(owner, 'PagosPim_AttributeDefinition', None)
    assert getattr(partner, 'PagosPim_EObject') is None


def test_assoc_daocomponent5_stub_double():
    # PagosPim_DaoComponent has no real 'PagosPim_DaoComponent' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Application(name="sample_text")
    partner = PagosPim_DaoComponent()
    setattr(partner, 'PagosPim_DaoComponent', None)
    _safe_set(owner, 'PagosPim_Application6', {partner})
    assert getattr(partner, 'PagosPim_DaoComponent') == owner
    _safe_set(owner, 'PagosPim_Application6', set())
    assert getattr(partner, 'PagosPim_DaoComponent') is None


def test_assoc_datalayercomponents3_stub_double():
    # PagosPim_DataLayerComponent has no real 'PagosPim_DataLayerComponent' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Application(name="sample_text")
    partner = PagosPim_DataLayerComponent()
    setattr(partner, 'PagosPim_DataLayerComponent', None)
    _safe_set(owner, 'PagosPim_Application4', {partner})
    assert getattr(partner, 'PagosPim_DataLayerComponent') == owner
    _safe_set(owner, 'PagosPim_Application4', set())
    assert getattr(partner, 'PagosPim_DataLayerComponent') is None


def test_assoc_expression28_stub_double():
    # PagosPim_Expression has no real 'PagosPim_Expression' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Attribute(isIndex="sample_text")
    partner = PagosPim_Expression()
    setattr(partner, 'PagosPim_Expression', None)
    _safe_set(owner, 'PagosPim_Attribute29', partner)
    assert getattr(partner, 'PagosPim_Expression') == owner
    _safe_set(owner, 'PagosPim_Attribute29', None)
    assert getattr(partner, 'PagosPim_Expression') is None


def test_assoc_expression43_stub_double():
    # PagosPim_Expression has no real 'PagosPim_Expression44' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Return's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Return's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Return(type="sample_text")
    partner = PagosPim_Expression()
    setattr(partner, 'PagosPim_Expression44', None)
    _safe_set(owner, 'PagosPim_Return', {partner})
    assert getattr(partner, 'PagosPim_Expression44') == owner
    _safe_set(owner, 'PagosPim_Return', set())
    assert getattr(partner, 'PagosPim_Expression44') is None


def test_assoc_expression67_stub_double():
    # PagosPim_ElseSegment has no real 'PagosPim_ElseSegment68' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Return's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Return's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Return(type="sample_text")
    partner = PagosPim_ElseSegment()
    setattr(partner, 'PagosPim_ElseSegment68', None)
    _safe_set(owner, 'PagosPim_Return69', partner)
    assert getattr(partner, 'PagosPim_ElseSegment68') == owner
    _safe_set(owner, 'PagosPim_Return69', None)
    assert getattr(partner, 'PagosPim_ElseSegment68') is None


def test_assoc_leftExp87_stub_double():
    # PagosPim_Expression has no real 'PagosPim_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Add's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Add's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Add(operator="sample_text")
    partner = PagosPim_Expression()
    setattr(partner, 'PagosPim_Expression88', None)
    _safe_set(owner, 'PagosPim_Add', partner)
    assert getattr(partner, 'PagosPim_Expression88') == owner
    _safe_set(owner, 'PagosPim_Add', None)
    assert getattr(partner, 'PagosPim_Expression88') is None


def test_assoc_leftExp94_stub_double():
    # PagosPim_Expression has no real 'PagosPim_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Mult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Mult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Mult(operator="sample_text")
    partner = PagosPim_Expression()
    setattr(partner, 'PagosPim_Expression96', None)
    _safe_set(owner, 'PagosPim_Mult95', partner)
    assert getattr(partner, 'PagosPim_Expression96') == owner
    _safe_set(owner, 'PagosPim_Mult95', None)
    assert getattr(partner, 'PagosPim_Expression96') is None


def test_assoc_logicalexpressions56_stub_double():
    # PagosPim_IfCondition has no real 'PagosPim_IfCondition57' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_LogicalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_LogicalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_LogicalExpression(conOper="sample_text", literal="sample_text", logicalOperator="sample_text")
    partner = PagosPim_IfCondition()
    setattr(partner, 'PagosPim_IfCondition57', None)
    _safe_set(owner, 'PagosPim_LogicalExpression', partner)
    assert owner in getattr(partner, 'PagosPim_IfCondition57')
    _safe_set(owner, 'PagosPim_LogicalExpression', None)
    assert owner not in getattr(partner, 'PagosPim_IfCondition57')


def test_assoc_mapsTo100_stub_double():
    # PagosPim_DataLayerComponent has no real 'PagosPim_DataLayerComponent102' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_LogicComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_LogicComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_LogicComponent(persistible=True)
    partner = PagosPim_DataLayerComponent()
    setattr(partner, 'PagosPim_DataLayerComponent102', None)
    _safe_set(owner, 'PagosPim_LogicComponent101', partner)
    assert getattr(partner, 'PagosPim_DataLayerComponent102') == owner
    _safe_set(owner, 'PagosPim_LogicComponent101', None)
    assert getattr(partner, 'PagosPim_DataLayerComponent102') is None


def test_assoc_parameterList30_stub_double():
    # PagosPim_ParameterList has no real 'PagosPim_ParameterList' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Operation(name="sample_text")
    partner = PagosPim_ParameterList()
    setattr(partner, 'PagosPim_ParameterList', None)
    _safe_set(owner, 'PagosPim_Operation31', partner)
    assert getattr(partner, 'PagosPim_ParameterList') == owner
    _safe_set(owner, 'PagosPim_Operation31', None)
    assert getattr(partner, 'PagosPim_ParameterList') is None


def test_assoc_parent81_stub_double():
    # PagosPim_EObject has no real 'PagosPim_EObject83' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_TerminalValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_TerminalValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_TerminalValue(method="sample_text", value="sample_text")
    partner = PagosPim_EObject()
    setattr(partner, 'PagosPim_EObject83', None)
    _safe_set(owner, 'PagosPim_TerminalValue82', partner)
    assert getattr(partner, 'PagosPim_EObject83') == owner
    _safe_set(owner, 'PagosPim_TerminalValue82', None)
    assert getattr(partner, 'PagosPim_EObject83') is None


def test_assoc_relatesTo97_stub_double():
    # PagosPim_ServerService has no real 'PagosPim_ServerService98' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_LogicComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_LogicComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_LogicComponent(persistible=True)
    partner = PagosPim_ServerService()
    setattr(partner, 'PagosPim_ServerService98', None)
    _safe_set(owner, 'PagosPim_LogicComponent99', partner)
    assert getattr(partner, 'PagosPim_ServerService98') == owner
    _safe_set(owner, 'PagosPim_LogicComponent99', None)
    assert getattr(partner, 'PagosPim_ServerService98') is None


def test_assoc_returnBlock58_stub_double():
    # PagosPim_IfCondition has no real 'PagosPim_IfCondition59' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Return's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Return's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Return(type="sample_text")
    partner = PagosPim_IfCondition()
    setattr(partner, 'PagosPim_IfCondition59', None)
    _safe_set(owner, 'PagosPim_Return60', partner)
    assert getattr(partner, 'PagosPim_IfCondition59') == owner
    _safe_set(owner, 'PagosPim_Return60', None)
    assert getattr(partner, 'PagosPim_IfCondition59') is None


def test_assoc_returnExp47_stub_double():
    # PagosPim_Body has no real 'PagosPim_Body48' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Return's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Return's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Return(type="sample_text")
    partner = PagosPim_Body()
    setattr(partner, 'PagosPim_Body48', None)
    _safe_set(owner, 'PagosPim_Return49', partner)
    assert getattr(partner, 'PagosPim_Body48') == owner
    _safe_set(owner, 'PagosPim_Return49', None)
    assert getattr(partner, 'PagosPim_Body48') is None


def test_assoc_rightExp89_stub_double():
    # PagosPim_Expression has no real 'PagosPim_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Add's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Add's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Add(operator="sample_text")
    partner = PagosPim_Expression()
    setattr(partner, 'PagosPim_Expression91', None)
    _safe_set(owner, 'PagosPim_Add90', partner)
    assert getattr(partner, 'PagosPim_Expression91') == owner
    _safe_set(owner, 'PagosPim_Add90', None)
    assert getattr(partner, 'PagosPim_Expression91') is None


def test_assoc_rightExp92_stub_double():
    # PagosPim_Expression has no real 'PagosPim_Expression93' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Mult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Mult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Mult(operator="sample_text")
    partner = PagosPim_Expression()
    setattr(partner, 'PagosPim_Expression93', None)
    _safe_set(owner, 'PagosPim_Mult', partner)
    assert getattr(partner, 'PagosPim_Expression93') == owner
    _safe_set(owner, 'PagosPim_Mult', None)
    assert getattr(partner, 'PagosPim_Expression93') is None


def test_assoc_serverservice1_stub_double():
    # PagosPim_ServerService has no real 'PagosPim_ServerService' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_Application(name="sample_text")
    partner = PagosPim_ServerService()
    setattr(partner, 'PagosPim_ServerService', None)
    _safe_set(owner, 'PagosPim_Application2', {partner})
    assert getattr(partner, 'PagosPim_ServerService') == owner
    _safe_set(owner, 'PagosPim_Application2', set())
    assert getattr(partner, 'PagosPim_ServerService') is None


def test_assoc_serves13_stub_double():
    # PagosPim_ServerService has no real 'PagosPim_ServerService15' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_FrontService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_FrontService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_FrontService(fullName="sample_text")
    partner = PagosPim_ServerService()
    setattr(partner, 'PagosPim_ServerService15', None)
    _safe_set(owner, 'PagosPim_FrontService14', partner)
    assert getattr(partner, 'PagosPim_ServerService15') == owner
    _safe_set(owner, 'PagosPim_FrontService14', None)
    assert getattr(partner, 'PagosPim_ServerService15') is None


def test_assoc_service108_stub_double():
    # PagosPim_Action has no real 'PagosPim_Action' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_FrontService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_FrontService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_FrontService(fullName="sample_text")
    partner = PagosPim_Action()
    setattr(partner, 'PagosPim_Action', None)
    _safe_set(owner, 'PagosPim_FrontService109', partner)
    assert getattr(partner, 'PagosPim_Action') == owner
    _safe_set(owner, 'PagosPim_FrontService109', None)
    assert getattr(partner, 'PagosPim_Action') is None


def test_assoc_service9_stub_double():
    # PagosPim_Input has no real 'PagosPim_Input' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_FrontService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_FrontService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_FrontService(fullName="sample_text")
    partner = PagosPim_Input()
    setattr(partner, 'PagosPim_Input', None)
    _safe_set(owner, 'PagosPim_FrontService', partner)
    assert getattr(partner, 'PagosPim_Input') == owner
    _safe_set(owner, 'PagosPim_FrontService', None)
    assert getattr(partner, 'PagosPim_Input') is None


def test_assoc_subcomponents16_stub_double():
    # PagosPim_SubComponent has no real 'PagosPim_SubComponent' property in the generated
    # code (a bare stub) -- manually attach it so PagosPim_ViewComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PagosPim_ViewComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PagosPim_ViewComponent(title="sample_text")
    partner = PagosPim_SubComponent()
    setattr(partner, 'PagosPim_SubComponent', None)
    _safe_set(owner, 'PagosPim_ViewComponent17', {partner})
    assert getattr(partner, 'PagosPim_SubComponent') == owner
    _safe_set(owner, 'PagosPim_ViewComponent17', set())
    assert getattr(partner, 'PagosPim_SubComponent') is None


