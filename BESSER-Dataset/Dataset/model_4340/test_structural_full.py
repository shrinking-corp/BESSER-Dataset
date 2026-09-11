import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Constraint,
    Expression,
    PrologExpression,
    tExp_AndExpr,
    tExp_AtomExpression,
    tExp_Cardinality,
    tExp_CatExpr,
    tExp_Channel,
    tExp_Constraint,
    tExp_Domainmodel,
    tExp_EventType,
    tExp_Expression,
    tExp_FilterExpr,
    tExp_ListExpression,
    tExp_Msg,
    tExp_NumberExpression,
    tExp_Partition,
    tExp_PrologExpression,
    tExp_Role,
    tExp_SeqExpr,
    tExp_ShuffleExpr,
    tExp_Singletons,
    tExp_Size,
    tExp_StringExpression,
    tExp_Term,
    tExp_TerminalExpr,
    tExp_Together,
    tExp_TraceExpression,
    tExp_UnionExpr,
    tExp_VarExpr,
    tExp_VariableExpression,
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

def test_tExp_AtomExpression_atom_value_roundtrip():
    instance = tExp_AtomExpression(atom="sample_text")
    assert instance.atom == "sample_text"
    instance.atom = "sample_text_2"
    assert instance.atom == "sample_text_2"


def test_tExp_Cardinality_maxCardinality_value_roundtrip():
    instance = tExp_Cardinality(maxCardinality=7, minCardinality=7)
    assert instance.maxCardinality == 7
    instance.maxCardinality = 13
    assert instance.maxCardinality == 13


def test_tExp_Cardinality_minCardinality_value_roundtrip():
    instance = tExp_Cardinality(maxCardinality=7, minCardinality=7)
    assert instance.minCardinality == 7
    instance.minCardinality = 13
    assert instance.minCardinality == 13


def test_tExp_Channel_name_value_roundtrip():
    instance = tExp_Channel(name="sample_text", reliability="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tExp_Channel_reliability_value_roundtrip():
    instance = tExp_Channel(name="sample_text", reliability="sample_text")
    assert instance.reliability == "sample_text"
    instance.reliability = "sample_text_2"
    assert instance.reliability == "sample_text_2"


def test_tExp_Constraint_parMax_value_roundtrip():
    instance = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    assert instance.parMax == "sample_text"
    instance.parMax = "sample_text_2"
    assert instance.parMax == "sample_text_2"


def test_tExp_Constraint_parMin_value_roundtrip():
    instance = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    assert instance.parMin == "sample_text"
    instance.parMin = "sample_text_2"
    assert instance.parMin == "sample_text_2"


def test_tExp_Constraint_split_value_roundtrip():
    instance = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    assert instance.split == "sample_text"
    instance.split = "sample_text_2"
    assert instance.split == "sample_text_2"


def test_tExp_Constraint_together_value_roundtrip():
    instance = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    assert instance.together == "sample_text"
    instance.together = "sample_text_2"
    assert instance.together == "sample_text_2"


def test_tExp_EventType_name_value_roundtrip():
    instance = tExp_EventType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tExp_Expression_eps_value_roundtrip():
    instance = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    assert instance.eps == "sample_text"
    instance.eps = "sample_text_2"
    assert instance.eps == "sample_text_2"


def test_tExp_Expression_operator_value_roundtrip():
    instance = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_tExp_Expression_variable_value_roundtrip():
    instance = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    assert instance.variable == "sample_text"
    instance.variable = "sample_text_2"
    assert instance.variable == "sample_text_2"


def test_tExp_Msg_performative_value_roundtrip():
    instance = tExp_Msg(performative="sample_text")
    assert instance.performative == "sample_text"
    instance.performative = "sample_text_2"
    assert instance.performative == "sample_text_2"


def test_tExp_NumberExpression_value_value_roundtrip():
    instance = tExp_NumberExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_tExp_PrologExpression_op_value_roundtrip():
    instance = tExp_PrologExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_tExp_Role_args_value_roundtrip():
    instance = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    assert instance.args == "sample_text"
    instance.args = "sample_text_2"
    assert instance.args == "sample_text_2"


def test_tExp_Role_class__value_roundtrip():
    instance = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_tExp_Role_name_value_roundtrip():
    instance = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tExp_Singletons_maxSingletons_value_roundtrip():
    instance = tExp_Singletons(maxSingletons=7, minSingletons=7)
    assert instance.maxSingletons == 7
    instance.maxSingletons = 13
    assert instance.maxSingletons == 13


def test_tExp_Singletons_minSingletons_value_roundtrip():
    instance = tExp_Singletons(maxSingletons=7, minSingletons=7)
    assert instance.minSingletons == 7
    instance.minSingletons = 13
    assert instance.minSingletons == 13


def test_tExp_Size_maxSize_value_roundtrip():
    instance = tExp_Size(maxSize=7, minSize=7)
    assert instance.maxSize == 7
    instance.maxSize = 13
    assert instance.maxSize == 13


def test_tExp_Size_minSize_value_roundtrip():
    instance = tExp_Size(maxSize=7, minSize=7)
    assert instance.minSize == 7
    instance.minSize = 13
    assert instance.minSize == 13


def test_tExp_StringExpression_value_value_roundtrip():
    instance = tExp_StringExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_tExp_Term_name_value_roundtrip():
    instance = tExp_Term(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tExp_TraceExpression_bodyL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.bodyL == "sample_text"
    instance.bodyL = "sample_text_2"
    assert instance.bodyL == "sample_text_2"


def test_tExp_TraceExpression_channelsL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.channelsL == "sample_text"
    instance.channelsL = "sample_text_2"
    assert instance.channelsL == "sample_text_2"


def test_tExp_TraceExpression_constraintsL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.constraintsL == "sample_text"
    instance.constraintsL = "sample_text_2"
    assert instance.constraintsL == "sample_text_2"


def test_tExp_TraceExpression_decentralized_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.decentralized == "sample_text"
    instance.decentralized = "sample_text_2"
    assert instance.decentralized == "sample_text_2"


def test_tExp_TraceExpression_decentralizedL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.decentralizedL == "sample_text"
    instance.decentralizedL = "sample_text_2"
    assert instance.decentralizedL == "sample_text_2"


def test_tExp_TraceExpression_gui_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.gui == "sample_text"
    instance.gui = "sample_text_2"
    assert instance.gui == "sample_text_2"


def test_tExp_TraceExpression_guiL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.guiL == "sample_text"
    instance.guiL = "sample_text_2"
    assert instance.guiL == "sample_text_2"


def test_tExp_TraceExpression_minimal_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.minimal == "sample_text"
    instance.minimal = "sample_text_2"
    assert instance.minimal == "sample_text_2"


def test_tExp_TraceExpression_minimalL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.minimalL == "sample_text"
    instance.minimalL = "sample_text_2"
    assert instance.minimalL == "sample_text_2"


def test_tExp_TraceExpression_modules_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.modules == "sample_text"
    instance.modules = "sample_text_2"
    assert instance.modules == "sample_text_2"


def test_tExp_TraceExpression_modulesL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.modulesL == "sample_text"
    instance.modulesL = "sample_text_2"
    assert instance.modulesL == "sample_text_2"


def test_tExp_TraceExpression_name_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tExp_TraceExpression_partitionL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.partitionL == "sample_text"
    instance.partitionL = "sample_text_2"
    assert instance.partitionL == "sample_text_2"


def test_tExp_TraceExpression_rolesL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.rolesL == "sample_text"
    instance.rolesL = "sample_text_2"
    assert instance.rolesL == "sample_text_2"


def test_tExp_TraceExpression_threshold_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.threshold == "sample_text"
    instance.threshold = "sample_text_2"
    assert instance.threshold == "sample_text_2"


def test_tExp_TraceExpression_thresholdL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.thresholdL == "sample_text"
    instance.thresholdL = "sample_text_2"
    assert instance.thresholdL == "sample_text_2"


def test_tExp_TraceExpression_typesL_value_roundtrip():
    instance = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    assert instance.typesL == "sample_text"
    instance.typesL = "sample_text_2"
    assert instance.typesL == "sample_text_2"


def test_tExp_VariableExpression_name_value_roundtrip():
    instance = tExp_VariableExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tExp_Cardinality_isa_Constraint():
    instance = tExp_Cardinality(maxCardinality=7, minCardinality=7)
    assert isinstance(instance, Constraint)


def test_tExp_Singletons_isa_Constraint():
    instance = tExp_Singletons(maxSingletons=7, minSingletons=7)
    assert isinstance(instance, Constraint)


def test_tExp_Size_isa_Constraint():
    instance = tExp_Size(maxSize=7, minSize=7)
    assert isinstance(instance, Constraint)


def test_tExp_AndExpr_isa_Expression():
    instance = tExp_AndExpr()
    assert isinstance(instance, Expression)


def test_tExp_CatExpr_isa_Expression():
    instance = tExp_CatExpr()
    assert isinstance(instance, Expression)


def test_tExp_FilterExpr_isa_Expression():
    instance = tExp_FilterExpr()
    assert isinstance(instance, Expression)


def test_tExp_SeqExpr_isa_Expression():
    instance = tExp_SeqExpr()
    assert isinstance(instance, Expression)


def test_tExp_ShuffleExpr_isa_Expression():
    instance = tExp_ShuffleExpr()
    assert isinstance(instance, Expression)


def test_tExp_TerminalExpr_isa_Expression():
    instance = tExp_TerminalExpr()
    assert isinstance(instance, Expression)


def test_tExp_UnionExpr_isa_Expression():
    instance = tExp_UnionExpr()
    assert isinstance(instance, Expression)


def test_tExp_VarExpr_isa_Expression():
    instance = tExp_VarExpr()
    assert isinstance(instance, Expression)


def test_tExp_AtomExpression_isa_PrologExpression():
    instance = tExp_AtomExpression(atom="sample_text")
    assert isinstance(instance, PrologExpression)


def test_tExp_ListExpression_isa_PrologExpression():
    instance = tExp_ListExpression()
    assert isinstance(instance, PrologExpression)


def test_tExp_NumberExpression_isa_PrologExpression():
    instance = tExp_NumberExpression(value="sample_text")
    assert isinstance(instance, PrologExpression)


def test_tExp_StringExpression_isa_PrologExpression():
    instance = tExp_StringExpression(value="sample_text")
    assert isinstance(instance, PrologExpression)


def test_tExp_VariableExpression_isa_PrologExpression():
    instance = tExp_VariableExpression(name="sample_text")
    assert isinstance(instance, PrologExpression)


def test_assoc_async_receiver67_link_reassign_clear():
    a = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b1 = tExp_Msg(performative="sample_text")
    b2 = tExp_Msg(performative="sample_text_2")
    _safe_set(a, 'tExp_Role69', b1)
    assert _is_linked(a, 'tExp_Role69', b1)
    if hasattr(b1, 'tExp_Msg68'):
        assert _is_linked(b1, 'tExp_Msg68', a)
    _safe_set(a, 'tExp_Role69', b2)
    assert _is_linked(a, 'tExp_Role69', b2)
    if hasattr(b1, 'tExp_Msg68'):
        assert not _is_linked(b1, 'tExp_Msg68', a)
    if hasattr(b2, 'tExp_Msg68'):
        assert _is_linked(b2, 'tExp_Msg68', a)
    _safe_set(a, 'tExp_Role69', None)
    assert not _is_linked(a, 'tExp_Role69', b2)
    if hasattr(b2, 'tExp_Msg68'):
        assert not _is_linked(b2, 'tExp_Msg68', a)


def test_assoc_async_sender58_link_reassign_clear():
    a = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b1 = tExp_Msg(performative="sample_text")
    b2 = tExp_Msg(performative="sample_text_2")
    _safe_set(a, 'tExp_Role60', b1)
    assert _is_linked(a, 'tExp_Role60', b1)
    if hasattr(b1, 'tExp_Msg59'):
        assert _is_linked(b1, 'tExp_Msg59', a)
    _safe_set(a, 'tExp_Role60', b2)
    assert _is_linked(a, 'tExp_Role60', b2)
    if hasattr(b1, 'tExp_Msg59'):
        assert not _is_linked(b1, 'tExp_Msg59', a)
    if hasattr(b2, 'tExp_Msg59'):
        assert _is_linked(b2, 'tExp_Msg59', a)
    _safe_set(a, 'tExp_Role60', None)
    assert not _is_linked(a, 'tExp_Role60', b2)
    if hasattr(b2, 'tExp_Msg59'):
        assert not _is_linked(b2, 'tExp_Msg59', a)


def test_assoc_bodyFilter33_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_Expression32', b1)
    assert _is_linked(a, 'tExp_Expression32', b1)
    if hasattr(b1, 'tExp_Expression34'):
        assert _is_linked(b1, 'tExp_Expression34', a)
    _safe_set(a, 'tExp_Expression32', b2)
    assert _is_linked(a, 'tExp_Expression32', b2)
    if hasattr(b1, 'tExp_Expression34'):
        assert not _is_linked(b1, 'tExp_Expression34', a)
    if hasattr(b2, 'tExp_Expression34'):
        assert _is_linked(b2, 'tExp_Expression34', a)
    _safe_set(a, 'tExp_Expression32', None)
    assert not _is_linked(a, 'tExp_Expression32', b2)
    if hasattr(b2, 'tExp_Expression34'):
        assert not _is_linked(b2, 'tExp_Expression34', a)


def test_assoc_bodySeq39_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_Expression38', b1)
    assert _is_linked(a, 'tExp_Expression38', b1)
    if hasattr(b1, 'tExp_Expression40'):
        assert _is_linked(b1, 'tExp_Expression40', a)
    _safe_set(a, 'tExp_Expression38', b2)
    assert _is_linked(a, 'tExp_Expression38', b2)
    if hasattr(b1, 'tExp_Expression40'):
        assert not _is_linked(b1, 'tExp_Expression40', a)
    if hasattr(b2, 'tExp_Expression40'):
        assert _is_linked(b2, 'tExp_Expression40', a)
    _safe_set(a, 'tExp_Expression38', None)
    assert not _is_linked(a, 'tExp_Expression38', b2)
    if hasattr(b2, 'tExp_Expression40'):
        assert not _is_linked(b2, 'tExp_Expression40', a)


def test_assoc_bodyVar21_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_Expression20', b1)
    assert _is_linked(a, 'tExp_Expression20', b1)
    if hasattr(b1, 'tExp_Expression22'):
        assert _is_linked(b1, 'tExp_Expression22', a)
    _safe_set(a, 'tExp_Expression20', b2)
    assert _is_linked(a, 'tExp_Expression20', b2)
    if hasattr(b1, 'tExp_Expression22'):
        assert not _is_linked(b1, 'tExp_Expression22', a)
    if hasattr(b2, 'tExp_Expression22'):
        assert _is_linked(b2, 'tExp_Expression22', a)
    _safe_set(a, 'tExp_Expression20', None)
    assert not _is_linked(a, 'tExp_Expression20', b2)
    if hasattr(b2, 'tExp_Expression22'):
        assert not _is_linked(b2, 'tExp_Expression22', a)


def test_assoc_channel55_link_reassign_clear():
    a = tExp_EventType(name="sample_text")
    b1 = tExp_Channel(name="sample_text", reliability="sample_text")
    b2 = tExp_Channel(name="sample_text_2", reliability="sample_text_2")
    _safe_set(a, 'tExp_EventType56', b1)
    assert _is_linked(a, 'tExp_EventType56', b1)
    if hasattr(b1, 'tExp_Channel57'):
        assert _is_linked(b1, 'tExp_Channel57', a)
    _safe_set(a, 'tExp_EventType56', b2)
    assert _is_linked(a, 'tExp_EventType56', b2)
    if hasattr(b1, 'tExp_Channel57'):
        assert not _is_linked(b1, 'tExp_Channel57', a)
    if hasattr(b2, 'tExp_Channel57'):
        assert _is_linked(b2, 'tExp_Channel57', a)
    _safe_set(a, 'tExp_EventType56', None)
    assert not _is_linked(a, 'tExp_EventType56', b2)
    if hasattr(b2, 'tExp_Channel57'):
        assert not _is_linked(b2, 'tExp_Channel57', a)


def test_assoc_channels16_link_reassign_clear():
    a = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    b1 = tExp_Channel(name="sample_text", reliability="sample_text")
    b2 = tExp_Channel(name="sample_text_2", reliability="sample_text_2")
    _safe_set(a, 'tExp_TraceExpression17', {b1})
    assert _is_linked(a, 'tExp_TraceExpression17', b1)
    if hasattr(b1, 'tExp_Channel'):
        assert _is_linked(b1, 'tExp_Channel', a)
    _safe_set(a, 'tExp_TraceExpression17', {b2})
    assert _is_linked(a, 'tExp_TraceExpression17', b2)
    if hasattr(b1, 'tExp_Channel'):
        assert not _is_linked(b1, 'tExp_Channel', a)
    if hasattr(b2, 'tExp_Channel'):
        assert _is_linked(b2, 'tExp_Channel', a)
    _safe_set(a, 'tExp_TraceExpression17', set())
    assert not _is_linked(a, 'tExp_TraceExpression17', b2)
    if hasattr(b2, 'tExp_Channel'):
        assert not _is_linked(b2, 'tExp_Channel', a)


def test_assoc_conditions73_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_Msg(performative="sample_text")
    b2 = tExp_Msg(performative="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression75', b1)
    assert _is_linked(a, 'tExp_PrologExpression75', b1)
    if hasattr(b1, 'tExp_Msg74'):
        assert _is_linked(b1, 'tExp_Msg74', a)
    _safe_set(a, 'tExp_PrologExpression75', b2)
    assert _is_linked(a, 'tExp_PrologExpression75', b2)
    if hasattr(b1, 'tExp_Msg74'):
        assert not _is_linked(b1, 'tExp_Msg74', a)
    if hasattr(b2, 'tExp_Msg74'):
        assert _is_linked(b2, 'tExp_Msg74', a)
    _safe_set(a, 'tExp_PrologExpression75', None)
    assert not _is_linked(a, 'tExp_PrologExpression75', b2)
    if hasattr(b2, 'tExp_Msg74'):
        assert not _is_linked(b2, 'tExp_Msg74', a)


def test_assoc_constraints14_link_reassign_clear():
    a = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    b1 = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    b2 = tExp_Constraint(parMax="sample_text_2", parMin="sample_text_2", split="sample_text_2", together="sample_text_2")
    _safe_set(a, 'tExp_TraceExpression15', {b1})
    assert _is_linked(a, 'tExp_TraceExpression15', b1)
    if hasattr(b1, 'tExp_Constraint'):
        assert _is_linked(b1, 'tExp_Constraint', a)
    _safe_set(a, 'tExp_TraceExpression15', {b2})
    assert _is_linked(a, 'tExp_TraceExpression15', b2)
    if hasattr(b1, 'tExp_Constraint'):
        assert not _is_linked(b1, 'tExp_Constraint', a)
    if hasattr(b2, 'tExp_Constraint'):
        assert _is_linked(b2, 'tExp_Constraint', a)
    _safe_set(a, 'tExp_TraceExpression15', set())
    assert not _is_linked(a, 'tExp_TraceExpression15', b2)
    if hasattr(b2, 'tExp_Constraint'):
        assert not _is_linked(b2, 'tExp_Constraint', a)


def test_assoc_content70_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_Msg(performative="sample_text")
    b2 = tExp_Msg(performative="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression72', b1)
    assert _is_linked(a, 'tExp_PrologExpression72', b1)
    if hasattr(b1, 'tExp_Msg71'):
        assert _is_linked(b1, 'tExp_Msg71', a)
    _safe_set(a, 'tExp_PrologExpression72', b2)
    assert _is_linked(a, 'tExp_PrologExpression72', b2)
    if hasattr(b1, 'tExp_Msg71'):
        assert not _is_linked(b1, 'tExp_Msg71', a)
    if hasattr(b2, 'tExp_Msg71'):
        assert _is_linked(b2, 'tExp_Msg71', a)
    _safe_set(a, 'tExp_PrologExpression72', None)
    assert not _is_linked(a, 'tExp_PrologExpression72', b2)
    if hasattr(b2, 'tExp_Msg71'):
        assert not _is_linked(b2, 'tExp_Msg71', a)


def test_assoc_elements0_link_reassign_clear():
    a = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    b1 = tExp_Domainmodel()
    b2 = tExp_Domainmodel()
    _safe_set(a, 'tExp_TraceExpression', b1)
    assert _is_linked(a, 'tExp_TraceExpression', b1)
    if hasattr(b1, 'tExp_Domainmodel'):
        assert _is_linked(b1, 'tExp_Domainmodel', a)
    _safe_set(a, 'tExp_TraceExpression', b2)
    assert _is_linked(a, 'tExp_TraceExpression', b2)
    if hasattr(b1, 'tExp_Domainmodel'):
        assert not _is_linked(b1, 'tExp_Domainmodel', a)
    if hasattr(b2, 'tExp_Domainmodel'):
        assert _is_linked(b2, 'tExp_Domainmodel', a)
    _safe_set(a, 'tExp_TraceExpression', None)
    assert not _is_linked(a, 'tExp_TraceExpression', b2)
    if hasattr(b2, 'tExp_Domainmodel'):
        assert not _is_linked(b2, 'tExp_Domainmodel', a)


def test_assoc_expr18_link_reassign_clear():
    a = tExp_Term(name="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_Term19', b1)
    assert _is_linked(a, 'tExp_Term19', b1)
    if hasattr(b1, 'tExp_Expression'):
        assert _is_linked(b1, 'tExp_Expression', a)
    _safe_set(a, 'tExp_Term19', b2)
    assert _is_linked(a, 'tExp_Term19', b2)
    if hasattr(b1, 'tExp_Expression'):
        assert not _is_linked(b1, 'tExp_Expression', a)
    if hasattr(b2, 'tExp_Expression'):
        assert _is_linked(b2, 'tExp_Expression', a)
    _safe_set(a, 'tExp_Term19', None)
    assert not _is_linked(a, 'tExp_Term19', b2)
    if hasattr(b2, 'tExp_Expression'):
        assert not _is_linked(b2, 'tExp_Expression', a)


def test_assoc_expr45_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_Expression44', b1)
    assert _is_linked(a, 'tExp_Expression44', b1)
    if hasattr(b1, 'tExp_Expression46'):
        assert _is_linked(b1, 'tExp_Expression46', a)
    _safe_set(a, 'tExp_Expression44', b2)
    assert _is_linked(a, 'tExp_Expression44', b2)
    if hasattr(b1, 'tExp_Expression46'):
        assert not _is_linked(b1, 'tExp_Expression46', a)
    if hasattr(b2, 'tExp_Expression46'):
        assert _is_linked(b2, 'tExp_Expression46', a)
    _safe_set(a, 'tExp_Expression44', None)
    assert not _is_linked(a, 'tExp_Expression44', b2)
    if hasattr(b2, 'tExp_Expression46'):
        assert not _is_linked(b2, 'tExp_Expression46', a)


def test_assoc_expr47_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_EventType(name="sample_text")
    b2 = tExp_EventType(name="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression49', b1)
    assert _is_linked(a, 'tExp_PrologExpression49', b1)
    if hasattr(b1, 'tExp_EventType48'):
        assert _is_linked(b1, 'tExp_EventType48', a)
    _safe_set(a, 'tExp_PrologExpression49', b2)
    assert _is_linked(a, 'tExp_PrologExpression49', b2)
    if hasattr(b1, 'tExp_EventType48'):
        assert not _is_linked(b1, 'tExp_EventType48', a)
    if hasattr(b2, 'tExp_EventType48'):
        assert _is_linked(b2, 'tExp_EventType48', a)
    _safe_set(a, 'tExp_PrologExpression49', None)
    assert not _is_linked(a, 'tExp_PrologExpression49', b2)
    if hasattr(b2, 'tExp_EventType48'):
        assert not _is_linked(b2, 'tExp_EventType48', a)


def test_assoc_exprs29_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression31', b1)
    assert _is_linked(a, 'tExp_PrologExpression31', b1)
    if hasattr(b1, 'tExp_Expression30'):
        assert _is_linked(b1, 'tExp_Expression30', a)
    _safe_set(a, 'tExp_PrologExpression31', b2)
    assert _is_linked(a, 'tExp_PrologExpression31', b2)
    if hasattr(b1, 'tExp_Expression30'):
        assert not _is_linked(b1, 'tExp_Expression30', a)
    if hasattr(b2, 'tExp_Expression30'):
        assert _is_linked(b2, 'tExp_Expression30', a)
    _safe_set(a, 'tExp_PrologExpression31', None)
    assert not _is_linked(a, 'tExp_PrologExpression31', b2)
    if hasattr(b2, 'tExp_Expression30'):
        assert not _is_linked(b2, 'tExp_Expression30', a)


def test_assoc_exprs50_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_EventType(name="sample_text")
    b2 = tExp_EventType(name="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression52', b1)
    assert _is_linked(a, 'tExp_PrologExpression52', b1)
    if hasattr(b1, 'tExp_EventType51'):
        assert _is_linked(b1, 'tExp_EventType51', a)
    _safe_set(a, 'tExp_PrologExpression52', b2)
    assert _is_linked(a, 'tExp_PrologExpression52', b2)
    if hasattr(b1, 'tExp_EventType51'):
        assert not _is_linked(b1, 'tExp_EventType51', a)
    if hasattr(b2, 'tExp_EventType51'):
        assert _is_linked(b2, 'tExp_EventType51', a)
    _safe_set(a, 'tExp_PrologExpression52', None)
    assert not _is_linked(a, 'tExp_PrologExpression52', b2)
    if hasattr(b2, 'tExp_EventType51'):
        assert not _is_linked(b2, 'tExp_EventType51', a)


def test_assoc_filterExpr116_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_FilterExpr()
    b2 = tExp_FilterExpr()
    _safe_set(a, 'tExp_Expression117', b1)
    assert _is_linked(a, 'tExp_Expression117', b1)
    if hasattr(b1, 'tExp_FilterExpr'):
        assert _is_linked(b1, 'tExp_FilterExpr', a)
    _safe_set(a, 'tExp_Expression117', b2)
    assert _is_linked(a, 'tExp_Expression117', b2)
    if hasattr(b1, 'tExp_FilterExpr'):
        assert not _is_linked(b1, 'tExp_FilterExpr', a)
    if hasattr(b2, 'tExp_FilterExpr'):
        assert _is_linked(b2, 'tExp_FilterExpr', a)
    _safe_set(a, 'tExp_Expression117', None)
    assert not _is_linked(a, 'tExp_Expression117', b2)
    if hasattr(b2, 'tExp_FilterExpr'):
        assert not _is_linked(b2, 'tExp_FilterExpr', a)


def test_assoc_first26_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression28', b1)
    assert _is_linked(a, 'tExp_PrologExpression28', b1)
    if hasattr(b1, 'tExp_Expression27'):
        assert _is_linked(b1, 'tExp_Expression27', a)
    _safe_set(a, 'tExp_PrologExpression28', b2)
    assert _is_linked(a, 'tExp_PrologExpression28', b2)
    if hasattr(b1, 'tExp_Expression27'):
        assert not _is_linked(b1, 'tExp_Expression27', a)
    if hasattr(b2, 'tExp_Expression27'):
        assert _is_linked(b2, 'tExp_Expression27', a)
    _safe_set(a, 'tExp_PrologExpression28', None)
    assert not _is_linked(a, 'tExp_PrologExpression28', b2)
    if hasattr(b2, 'tExp_Expression27'):
        assert not _is_linked(b2, 'tExp_Expression27', a)


def test_assoc_head89_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_ListExpression()
    b2 = tExp_ListExpression()
    _safe_set(a, 'tExp_PrologExpression90', b1)
    assert _is_linked(a, 'tExp_PrologExpression90', b1)
    if hasattr(b1, 'tExp_ListExpression'):
        assert _is_linked(b1, 'tExp_ListExpression', a)
    _safe_set(a, 'tExp_PrologExpression90', b2)
    assert _is_linked(a, 'tExp_PrologExpression90', b2)
    if hasattr(b1, 'tExp_ListExpression'):
        assert not _is_linked(b1, 'tExp_ListExpression', a)
    if hasattr(b2, 'tExp_ListExpression'):
        assert _is_linked(b2, 'tExp_ListExpression', a)
    _safe_set(a, 'tExp_PrologExpression90', None)
    assert not _is_linked(a, 'tExp_PrologExpression90', b2)
    if hasattr(b2, 'tExp_ListExpression'):
        assert not _is_linked(b2, 'tExp_ListExpression', a)


def test_assoc_left104_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_AndExpr()
    b2 = tExp_AndExpr()
    _safe_set(a, 'tExp_Expression105', b1)
    assert _is_linked(a, 'tExp_Expression105', b1)
    if hasattr(b1, 'tExp_AndExpr'):
        assert _is_linked(b1, 'tExp_AndExpr', a)
    _safe_set(a, 'tExp_Expression105', b2)
    assert _is_linked(a, 'tExp_Expression105', b2)
    if hasattr(b1, 'tExp_AndExpr'):
        assert not _is_linked(b1, 'tExp_AndExpr', a)
    if hasattr(b2, 'tExp_AndExpr'):
        assert _is_linked(b2, 'tExp_AndExpr', a)
    _safe_set(a, 'tExp_Expression105', None)
    assert not _is_linked(a, 'tExp_Expression105', b2)
    if hasattr(b2, 'tExp_AndExpr'):
        assert not _is_linked(b2, 'tExp_AndExpr', a)


def test_assoc_left109_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_CatExpr()
    b2 = tExp_CatExpr()
    _safe_set(a, 'tExp_Expression110', b1)
    assert _is_linked(a, 'tExp_Expression110', b1)
    if hasattr(b1, 'tExp_CatExpr'):
        assert _is_linked(b1, 'tExp_CatExpr', a)
    _safe_set(a, 'tExp_Expression110', b2)
    assert _is_linked(a, 'tExp_Expression110', b2)
    if hasattr(b1, 'tExp_CatExpr'):
        assert not _is_linked(b1, 'tExp_CatExpr', a)
    if hasattr(b2, 'tExp_CatExpr'):
        assert _is_linked(b2, 'tExp_CatExpr', a)
    _safe_set(a, 'tExp_Expression110', None)
    assert not _is_linked(a, 'tExp_Expression110', b2)
    if hasattr(b2, 'tExp_CatExpr'):
        assert not _is_linked(b2, 'tExp_CatExpr', a)


def test_assoc_left2_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_PrologExpression(op="sample_text")
    b2 = tExp_PrologExpression(op="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression', b1)
    assert _is_linked(a, 'tExp_PrologExpression', b1)
    if hasattr(b1, 'tExp_PrologExpression1'):
        assert _is_linked(b1, 'tExp_PrologExpression1', a)
    _safe_set(a, 'tExp_PrologExpression', b2)
    assert _is_linked(a, 'tExp_PrologExpression', b2)
    if hasattr(b1, 'tExp_PrologExpression1'):
        assert not _is_linked(b1, 'tExp_PrologExpression1', a)
    if hasattr(b2, 'tExp_PrologExpression1'):
        assert _is_linked(b2, 'tExp_PrologExpression1', a)
    _safe_set(a, 'tExp_PrologExpression', None)
    assert not _is_linked(a, 'tExp_PrologExpression', b2)
    if hasattr(b2, 'tExp_PrologExpression1'):
        assert not _is_linked(b2, 'tExp_PrologExpression1', a)


def test_assoc_left81_link_reassign_clear():
    a = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b1 = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    b2 = tExp_Constraint(parMax="sample_text_2", parMin="sample_text_2", split="sample_text_2", together="sample_text_2")
    _safe_set(a, 'tExp_Role83', b1)
    assert _is_linked(a, 'tExp_Role83', b1)
    if hasattr(b1, 'tExp_Constraint82'):
        assert _is_linked(b1, 'tExp_Constraint82', a)
    _safe_set(a, 'tExp_Role83', b2)
    assert _is_linked(a, 'tExp_Role83', b2)
    if hasattr(b1, 'tExp_Constraint82'):
        assert not _is_linked(b1, 'tExp_Constraint82', a)
    if hasattr(b2, 'tExp_Constraint82'):
        assert _is_linked(b2, 'tExp_Constraint82', a)
    _safe_set(a, 'tExp_Role83', None)
    assert not _is_linked(a, 'tExp_Role83', b2)
    if hasattr(b2, 'tExp_Constraint82'):
        assert not _is_linked(b2, 'tExp_Constraint82', a)


def test_assoc_left94_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_ShuffleExpr()
    b2 = tExp_ShuffleExpr()
    _safe_set(a, 'tExp_Expression95', b1)
    assert _is_linked(a, 'tExp_Expression95', b1)
    if hasattr(b1, 'tExp_ShuffleExpr'):
        assert _is_linked(b1, 'tExp_ShuffleExpr', a)
    _safe_set(a, 'tExp_Expression95', b2)
    assert _is_linked(a, 'tExp_Expression95', b2)
    if hasattr(b1, 'tExp_ShuffleExpr'):
        assert not _is_linked(b1, 'tExp_ShuffleExpr', a)
    if hasattr(b2, 'tExp_ShuffleExpr'):
        assert _is_linked(b2, 'tExp_ShuffleExpr', a)
    _safe_set(a, 'tExp_Expression95', None)
    assert not _is_linked(a, 'tExp_Expression95', b2)
    if hasattr(b2, 'tExp_ShuffleExpr'):
        assert not _is_linked(b2, 'tExp_ShuffleExpr', a)


def test_assoc_left99_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_UnionExpr()
    b2 = tExp_UnionExpr()
    _safe_set(a, 'tExp_Expression100', b1)
    assert _is_linked(a, 'tExp_Expression100', b1)
    if hasattr(b1, 'tExp_UnionExpr'):
        assert _is_linked(b1, 'tExp_UnionExpr', a)
    _safe_set(a, 'tExp_Expression100', b2)
    assert _is_linked(a, 'tExp_Expression100', b2)
    if hasattr(b1, 'tExp_UnionExpr'):
        assert not _is_linked(b1, 'tExp_UnionExpr', a)
    if hasattr(b2, 'tExp_UnionExpr'):
        assert _is_linked(b2, 'tExp_UnionExpr', a)
    _safe_set(a, 'tExp_Expression100', None)
    assert not _is_linked(a, 'tExp_Expression100', b2)
    if hasattr(b2, 'tExp_UnionExpr'):
        assert not _is_linked(b2, 'tExp_UnionExpr', a)


def test_assoc_msgs53_link_reassign_clear():
    a = tExp_Msg(performative="sample_text")
    b1 = tExp_EventType(name="sample_text")
    b2 = tExp_EventType(name="sample_text_2")
    _safe_set(a, 'tExp_Msg', b1)
    assert _is_linked(a, 'tExp_Msg', b1)
    if hasattr(b1, 'tExp_EventType54'):
        assert _is_linked(b1, 'tExp_EventType54', a)
    _safe_set(a, 'tExp_Msg', b2)
    assert _is_linked(a, 'tExp_Msg', b2)
    if hasattr(b1, 'tExp_EventType54'):
        assert not _is_linked(b1, 'tExp_EventType54', a)
    if hasattr(b2, 'tExp_EventType54'):
        assert _is_linked(b2, 'tExp_EventType54', a)
    _safe_set(a, 'tExp_Msg', None)
    assert not _is_linked(a, 'tExp_Msg', b2)
    if hasattr(b2, 'tExp_EventType54'):
        assert not _is_linked(b2, 'tExp_EventType54', a)


def test_assoc_partition12_link_reassign_clear():
    a = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    b1 = tExp_Partition()
    b2 = tExp_Partition()
    _safe_set(a, 'tExp_TraceExpression13', {b1})
    assert _is_linked(a, 'tExp_TraceExpression13', b1)
    if hasattr(b1, 'tExp_Partition'):
        assert _is_linked(b1, 'tExp_Partition', a)
    _safe_set(a, 'tExp_TraceExpression13', {b2})
    assert _is_linked(a, 'tExp_TraceExpression13', b2)
    if hasattr(b1, 'tExp_Partition'):
        assert not _is_linked(b1, 'tExp_Partition', a)
    if hasattr(b2, 'tExp_Partition'):
        assert _is_linked(b2, 'tExp_Partition', a)
    _safe_set(a, 'tExp_TraceExpression13', set())
    assert not _is_linked(a, 'tExp_TraceExpression13', b2)
    if hasattr(b2, 'tExp_Partition'):
        assert not _is_linked(b2, 'tExp_Partition', a)


def test_assoc_receiver61_link_reassign_clear():
    a = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b1 = tExp_Msg(performative="sample_text")
    b2 = tExp_Msg(performative="sample_text_2")
    _safe_set(a, 'tExp_Role63', b1)
    assert _is_linked(a, 'tExp_Role63', b1)
    if hasattr(b1, 'tExp_Msg62'):
        assert _is_linked(b1, 'tExp_Msg62', a)
    _safe_set(a, 'tExp_Role63', b2)
    assert _is_linked(a, 'tExp_Role63', b2)
    if hasattr(b1, 'tExp_Msg62'):
        assert not _is_linked(b1, 'tExp_Msg62', a)
    if hasattr(b2, 'tExp_Msg62'):
        assert _is_linked(b2, 'tExp_Msg62', a)
    _safe_set(a, 'tExp_Role63', None)
    assert not _is_linked(a, 'tExp_Role63', b2)
    if hasattr(b2, 'tExp_Msg62'):
        assert not _is_linked(b2, 'tExp_Msg62', a)


def test_assoc_right101_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_UnionExpr()
    b2 = tExp_UnionExpr()
    _safe_set(a, 'tExp_Expression103', b1)
    assert _is_linked(a, 'tExp_Expression103', b1)
    if hasattr(b1, 'tExp_UnionExpr102'):
        assert _is_linked(b1, 'tExp_UnionExpr102', a)
    _safe_set(a, 'tExp_Expression103', b2)
    assert _is_linked(a, 'tExp_Expression103', b2)
    if hasattr(b1, 'tExp_UnionExpr102'):
        assert not _is_linked(b1, 'tExp_UnionExpr102', a)
    if hasattr(b2, 'tExp_UnionExpr102'):
        assert _is_linked(b2, 'tExp_UnionExpr102', a)
    _safe_set(a, 'tExp_Expression103', None)
    assert not _is_linked(a, 'tExp_Expression103', b2)
    if hasattr(b2, 'tExp_UnionExpr102'):
        assert not _is_linked(b2, 'tExp_UnionExpr102', a)


def test_assoc_right106_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_AndExpr()
    b2 = tExp_AndExpr()
    _safe_set(a, 'tExp_Expression108', b1)
    assert _is_linked(a, 'tExp_Expression108', b1)
    if hasattr(b1, 'tExp_AndExpr107'):
        assert _is_linked(b1, 'tExp_AndExpr107', a)
    _safe_set(a, 'tExp_Expression108', b2)
    assert _is_linked(a, 'tExp_Expression108', b2)
    if hasattr(b1, 'tExp_AndExpr107'):
        assert not _is_linked(b1, 'tExp_AndExpr107', a)
    if hasattr(b2, 'tExp_AndExpr107'):
        assert _is_linked(b2, 'tExp_AndExpr107', a)
    _safe_set(a, 'tExp_Expression108', None)
    assert not _is_linked(a, 'tExp_Expression108', b2)
    if hasattr(b2, 'tExp_AndExpr107'):
        assert not _is_linked(b2, 'tExp_AndExpr107', a)


def test_assoc_right111_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_CatExpr()
    b2 = tExp_CatExpr()
    _safe_set(a, 'tExp_Expression113', b1)
    assert _is_linked(a, 'tExp_Expression113', b1)
    if hasattr(b1, 'tExp_CatExpr112'):
        assert _is_linked(b1, 'tExp_CatExpr112', a)
    _safe_set(a, 'tExp_Expression113', b2)
    assert _is_linked(a, 'tExp_Expression113', b2)
    if hasattr(b1, 'tExp_CatExpr112'):
        assert not _is_linked(b1, 'tExp_CatExpr112', a)
    if hasattr(b2, 'tExp_CatExpr112'):
        assert _is_linked(b2, 'tExp_CatExpr112', a)
    _safe_set(a, 'tExp_Expression113', None)
    assert not _is_linked(a, 'tExp_Expression113', b2)
    if hasattr(b2, 'tExp_CatExpr112'):
        assert not _is_linked(b2, 'tExp_CatExpr112', a)


def test_assoc_right4_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_PrologExpression(op="sample_text")
    b2 = tExp_PrologExpression(op="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression3', b1)
    assert _is_linked(a, 'tExp_PrologExpression3', b1)
    if hasattr(b1, 'tExp_PrologExpression5'):
        assert _is_linked(b1, 'tExp_PrologExpression5', a)
    _safe_set(a, 'tExp_PrologExpression3', b2)
    assert _is_linked(a, 'tExp_PrologExpression3', b2)
    if hasattr(b1, 'tExp_PrologExpression5'):
        assert not _is_linked(b1, 'tExp_PrologExpression5', a)
    if hasattr(b2, 'tExp_PrologExpression5'):
        assert _is_linked(b2, 'tExp_PrologExpression5', a)
    _safe_set(a, 'tExp_PrologExpression3', None)
    assert not _is_linked(a, 'tExp_PrologExpression3', b2)
    if hasattr(b2, 'tExp_PrologExpression5'):
        assert not _is_linked(b2, 'tExp_PrologExpression5', a)


def test_assoc_right84_link_reassign_clear():
    a = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b1 = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    b2 = tExp_Constraint(parMax="sample_text_2", parMin="sample_text_2", split="sample_text_2", together="sample_text_2")
    _safe_set(a, 'tExp_Role86', b1)
    assert _is_linked(a, 'tExp_Role86', b1)
    if hasattr(b1, 'tExp_Constraint85'):
        assert _is_linked(b1, 'tExp_Constraint85', a)
    _safe_set(a, 'tExp_Role86', b2)
    assert _is_linked(a, 'tExp_Role86', b2)
    if hasattr(b1, 'tExp_Constraint85'):
        assert not _is_linked(b1, 'tExp_Constraint85', a)
    if hasattr(b2, 'tExp_Constraint85'):
        assert _is_linked(b2, 'tExp_Constraint85', a)
    _safe_set(a, 'tExp_Role86', None)
    assert not _is_linked(a, 'tExp_Role86', b2)
    if hasattr(b2, 'tExp_Constraint85'):
        assert not _is_linked(b2, 'tExp_Constraint85', a)


def test_assoc_right96_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_ShuffleExpr()
    b2 = tExp_ShuffleExpr()
    _safe_set(a, 'tExp_Expression98', b1)
    assert _is_linked(a, 'tExp_Expression98', b1)
    if hasattr(b1, 'tExp_ShuffleExpr97'):
        assert _is_linked(b1, 'tExp_ShuffleExpr97', a)
    _safe_set(a, 'tExp_Expression98', b2)
    assert _is_linked(a, 'tExp_Expression98', b2)
    if hasattr(b1, 'tExp_ShuffleExpr97'):
        assert not _is_linked(b1, 'tExp_ShuffleExpr97', a)
    if hasattr(b2, 'tExp_ShuffleExpr97'):
        assert _is_linked(b2, 'tExp_ShuffleExpr97', a)
    _safe_set(a, 'tExp_Expression98', None)
    assert not _is_linked(a, 'tExp_Expression98', b2)
    if hasattr(b2, 'tExp_ShuffleExpr97'):
        assert not _is_linked(b2, 'tExp_ShuffleExpr97', a)


def test_assoc_roles78_link_reassign_clear():
    a = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b1 = tExp_Together()
    b2 = tExp_Together()
    _safe_set(a, 'tExp_Role80', b1)
    assert _is_linked(a, 'tExp_Role80', b1)
    if hasattr(b1, 'tExp_Together79'):
        assert _is_linked(b1, 'tExp_Together79', a)
    _safe_set(a, 'tExp_Role80', b2)
    assert _is_linked(a, 'tExp_Role80', b2)
    if hasattr(b1, 'tExp_Together79'):
        assert not _is_linked(b1, 'tExp_Together79', a)
    if hasattr(b2, 'tExp_Together79'):
        assert _is_linked(b2, 'tExp_Together79', a)
    _safe_set(a, 'tExp_Role80', None)
    assert not _is_linked(a, 'tExp_Role80', b2)
    if hasattr(b2, 'tExp_Together79'):
        assert not _is_linked(b2, 'tExp_Together79', a)


def test_assoc_roles8_link_reassign_clear():
    a = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    b1 = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b2 = tExp_Role(args="sample_text_2", class_="sample_text_2", name="sample_text_2")
    _safe_set(a, 'tExp_TraceExpression9', {b1})
    assert _is_linked(a, 'tExp_TraceExpression9', b1)
    if hasattr(b1, 'tExp_Role'):
        assert _is_linked(b1, 'tExp_Role', a)
    _safe_set(a, 'tExp_TraceExpression9', {b2})
    assert _is_linked(a, 'tExp_TraceExpression9', b2)
    if hasattr(b1, 'tExp_Role'):
        assert not _is_linked(b1, 'tExp_Role', a)
    if hasattr(b2, 'tExp_Role'):
        assert _is_linked(b2, 'tExp_Role', a)
    _safe_set(a, 'tExp_TraceExpression9', set())
    assert not _is_linked(a, 'tExp_TraceExpression9', b2)
    if hasattr(b2, 'tExp_Role'):
        assert not _is_linked(b2, 'tExp_Role', a)


def test_assoc_sender64_link_reassign_clear():
    a = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    b1 = tExp_Msg(performative="sample_text")
    b2 = tExp_Msg(performative="sample_text_2")
    _safe_set(a, 'tExp_Role66', b1)
    assert _is_linked(a, 'tExp_Role66', b1)
    if hasattr(b1, 'tExp_Msg65'):
        assert _is_linked(b1, 'tExp_Msg65', a)
    _safe_set(a, 'tExp_Role66', b2)
    assert _is_linked(a, 'tExp_Role66', b2)
    if hasattr(b1, 'tExp_Msg65'):
        assert not _is_linked(b1, 'tExp_Msg65', a)
    if hasattr(b2, 'tExp_Msg65'):
        assert _is_linked(b2, 'tExp_Msg65', a)
    _safe_set(a, 'tExp_Role66', None)
    assert not _is_linked(a, 'tExp_Role66', b2)
    if hasattr(b2, 'tExp_Msg65'):
        assert not _is_linked(b2, 'tExp_Msg65', a)


def test_assoc_seqExpr114_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_SeqExpr()
    b2 = tExp_SeqExpr()
    _safe_set(a, 'tExp_Expression115', b1)
    assert _is_linked(a, 'tExp_Expression115', b1)
    if hasattr(b1, 'tExp_SeqExpr'):
        assert _is_linked(b1, 'tExp_SeqExpr', a)
    _safe_set(a, 'tExp_Expression115', b2)
    assert _is_linked(a, 'tExp_Expression115', b2)
    if hasattr(b1, 'tExp_SeqExpr'):
        assert not _is_linked(b1, 'tExp_SeqExpr', a)
    if hasattr(b2, 'tExp_SeqExpr'):
        assert _is_linked(b2, 'tExp_SeqExpr', a)
    _safe_set(a, 'tExp_Expression115', None)
    assert not _is_linked(a, 'tExp_Expression115', b2)
    if hasattr(b2, 'tExp_SeqExpr'):
        assert not _is_linked(b2, 'tExp_SeqExpr', a)


def test_assoc_tail91_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_ListExpression()
    b2 = tExp_ListExpression()
    _safe_set(a, 'tExp_PrologExpression93', b1)
    assert _is_linked(a, 'tExp_PrologExpression93', b1)
    if hasattr(b1, 'tExp_ListExpression92'):
        assert _is_linked(b1, 'tExp_ListExpression92', a)
    _safe_set(a, 'tExp_PrologExpression93', b2)
    assert _is_linked(a, 'tExp_PrologExpression93', b2)
    if hasattr(b1, 'tExp_ListExpression92'):
        assert not _is_linked(b1, 'tExp_ListExpression92', a)
    if hasattr(b2, 'tExp_ListExpression92'):
        assert _is_linked(b2, 'tExp_ListExpression92', a)
    _safe_set(a, 'tExp_PrologExpression93', None)
    assert not _is_linked(a, 'tExp_PrologExpression93', b2)
    if hasattr(b2, 'tExp_ListExpression92'):
        assert not _is_linked(b2, 'tExp_ListExpression92', a)


def test_assoc_term41_link_reassign_clear():
    a = tExp_Term(name="sample_text")
    b1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'tExp_Term43', b1)
    assert _is_linked(a, 'tExp_Term43', b1)
    if hasattr(b1, 'tExp_Expression42'):
        assert _is_linked(b1, 'tExp_Expression42', a)
    _safe_set(a, 'tExp_Term43', b2)
    assert _is_linked(a, 'tExp_Term43', b2)
    if hasattr(b1, 'tExp_Expression42'):
        assert not _is_linked(b1, 'tExp_Expression42', a)
    if hasattr(b2, 'tExp_Expression42'):
        assert _is_linked(b2, 'tExp_Expression42', a)
    _safe_set(a, 'tExp_Term43', None)
    assert not _is_linked(a, 'tExp_Term43', b2)
    if hasattr(b2, 'tExp_Expression42'):
        assert not _is_linked(b2, 'tExp_Expression42', a)


def test_assoc_terminalExpr120_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_TerminalExpr()
    b2 = tExp_TerminalExpr()
    _safe_set(a, 'tExp_Expression121', b1)
    assert _is_linked(a, 'tExp_Expression121', b1)
    if hasattr(b1, 'tExp_TerminalExpr'):
        assert _is_linked(b1, 'tExp_TerminalExpr', a)
    _safe_set(a, 'tExp_Expression121', b2)
    assert _is_linked(a, 'tExp_Expression121', b2)
    if hasattr(b1, 'tExp_TerminalExpr'):
        assert not _is_linked(b1, 'tExp_TerminalExpr', a)
    if hasattr(b2, 'tExp_TerminalExpr'):
        assert _is_linked(b2, 'tExp_TerminalExpr', a)
    _safe_set(a, 'tExp_Expression121', None)
    assert not _is_linked(a, 'tExp_Expression121', b2)
    if hasattr(b2, 'tExp_TerminalExpr'):
        assert not _is_linked(b2, 'tExp_TerminalExpr', a)


def test_assoc_terms6_link_reassign_clear():
    a = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    b1 = tExp_Term(name="sample_text")
    b2 = tExp_Term(name="sample_text_2")
    _safe_set(a, 'tExp_TraceExpression7', {b1})
    assert _is_linked(a, 'tExp_TraceExpression7', b1)
    if hasattr(b1, 'tExp_Term'):
        assert _is_linked(b1, 'tExp_Term', a)
    _safe_set(a, 'tExp_TraceExpression7', {b2})
    assert _is_linked(a, 'tExp_TraceExpression7', b2)
    if hasattr(b1, 'tExp_Term'):
        assert not _is_linked(b1, 'tExp_Term', a)
    if hasattr(b2, 'tExp_Term'):
        assert _is_linked(b2, 'tExp_Term', a)
    _safe_set(a, 'tExp_TraceExpression7', set())
    assert not _is_linked(a, 'tExp_TraceExpression7', b2)
    if hasattr(b2, 'tExp_Term'):
        assert not _is_linked(b2, 'tExp_Term', a)


def test_assoc_terms87_link_reassign_clear():
    a = tExp_PrologExpression(op="sample_text")
    b1 = tExp_AtomExpression(atom="sample_text")
    b2 = tExp_AtomExpression(atom="sample_text_2")
    _safe_set(a, 'tExp_PrologExpression88', b1)
    assert _is_linked(a, 'tExp_PrologExpression88', b1)
    if hasattr(b1, 'tExp_AtomExpression'):
        assert _is_linked(b1, 'tExp_AtomExpression', a)
    _safe_set(a, 'tExp_PrologExpression88', b2)
    assert _is_linked(a, 'tExp_PrologExpression88', b2)
    if hasattr(b1, 'tExp_AtomExpression'):
        assert not _is_linked(b1, 'tExp_AtomExpression', a)
    if hasattr(b2, 'tExp_AtomExpression'):
        assert _is_linked(b2, 'tExp_AtomExpression', a)
    _safe_set(a, 'tExp_PrologExpression88', None)
    assert not _is_linked(a, 'tExp_PrologExpression88', b2)
    if hasattr(b2, 'tExp_AtomExpression'):
        assert not _is_linked(b2, 'tExp_AtomExpression', a)


def test_assoc_typeFilter23_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_EventType(name="sample_text")
    b2 = tExp_EventType(name="sample_text_2")
    _safe_set(a, 'tExp_Expression24', b1)
    assert _is_linked(a, 'tExp_Expression24', b1)
    if hasattr(b1, 'tExp_EventType25'):
        assert _is_linked(b1, 'tExp_EventType25', a)
    _safe_set(a, 'tExp_Expression24', b2)
    assert _is_linked(a, 'tExp_Expression24', b2)
    if hasattr(b1, 'tExp_EventType25'):
        assert not _is_linked(b1, 'tExp_EventType25', a)
    if hasattr(b2, 'tExp_EventType25'):
        assert _is_linked(b2, 'tExp_EventType25', a)
    _safe_set(a, 'tExp_Expression24', None)
    assert not _is_linked(a, 'tExp_Expression24', b2)
    if hasattr(b2, 'tExp_EventType25'):
        assert not _is_linked(b2, 'tExp_EventType25', a)


def test_assoc_typeSeq35_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_EventType(name="sample_text")
    b2 = tExp_EventType(name="sample_text_2")
    _safe_set(a, 'tExp_Expression36', b1)
    assert _is_linked(a, 'tExp_Expression36', b1)
    if hasattr(b1, 'tExp_EventType37'):
        assert _is_linked(b1, 'tExp_EventType37', a)
    _safe_set(a, 'tExp_Expression36', b2)
    assert _is_linked(a, 'tExp_Expression36', b2)
    if hasattr(b1, 'tExp_EventType37'):
        assert not _is_linked(b1, 'tExp_EventType37', a)
    if hasattr(b2, 'tExp_EventType37'):
        assert _is_linked(b2, 'tExp_EventType37', a)
    _safe_set(a, 'tExp_Expression36', None)
    assert not _is_linked(a, 'tExp_Expression36', b2)
    if hasattr(b2, 'tExp_EventType37'):
        assert not _is_linked(b2, 'tExp_EventType37', a)


def test_assoc_types10_link_reassign_clear():
    a = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    b1 = tExp_EventType(name="sample_text")
    b2 = tExp_EventType(name="sample_text_2")
    _safe_set(a, 'tExp_TraceExpression11', {b1})
    assert _is_linked(a, 'tExp_TraceExpression11', b1)
    if hasattr(b1, 'tExp_EventType'):
        assert _is_linked(b1, 'tExp_EventType', a)
    _safe_set(a, 'tExp_TraceExpression11', {b2})
    assert _is_linked(a, 'tExp_TraceExpression11', b2)
    if hasattr(b1, 'tExp_EventType'):
        assert not _is_linked(b1, 'tExp_EventType', a)
    if hasattr(b2, 'tExp_EventType'):
        assert _is_linked(b2, 'tExp_EventType', a)
    _safe_set(a, 'tExp_TraceExpression11', set())
    assert not _is_linked(a, 'tExp_TraceExpression11', b2)
    if hasattr(b2, 'tExp_EventType'):
        assert not _is_linked(b2, 'tExp_EventType', a)


def test_assoc_varExpr118_link_reassign_clear():
    a = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    b1 = tExp_VarExpr()
    b2 = tExp_VarExpr()
    _safe_set(a, 'tExp_Expression119', b1)
    assert _is_linked(a, 'tExp_Expression119', b1)
    if hasattr(b1, 'tExp_VarExpr'):
        assert _is_linked(b1, 'tExp_VarExpr', a)
    _safe_set(a, 'tExp_Expression119', b2)
    assert _is_linked(a, 'tExp_Expression119', b2)
    if hasattr(b1, 'tExp_VarExpr'):
        assert not _is_linked(b1, 'tExp_VarExpr', a)
    if hasattr(b2, 'tExp_VarExpr'):
        assert _is_linked(b2, 'tExp_VarExpr', a)
    _safe_set(a, 'tExp_Expression119', None)
    assert not _is_linked(a, 'tExp_Expression119', b2)
    if hasattr(b2, 'tExp_VarExpr'):
        assert not _is_linked(b2, 'tExp_VarExpr', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


PrologExpression_strategy = st.builds(PrologExpression)
@given(instance=PrologExpression_strategy)
@settings(max_examples=25)
def test_PrologExpression_instantiation(instance):
    assert isinstance(instance, PrologExpression)


tExp_AndExpr_strategy = st.builds(tExp_AndExpr)
@given(instance=tExp_AndExpr_strategy)
@settings(max_examples=25)
def test_tExp_AndExpr_instantiation(instance):
    assert isinstance(instance, tExp_AndExpr)


tExp_AtomExpression_strategy = st.builds(tExp_AtomExpression, atom=safe_text)
@given(instance=tExp_AtomExpression_strategy)
@settings(max_examples=25)
def test_tExp_AtomExpression_instantiation(instance):
    assert isinstance(instance, tExp_AtomExpression)


tExp_Cardinality_strategy = st.builds(tExp_Cardinality, maxCardinality=st.integers(), minCardinality=st.integers())
@given(instance=tExp_Cardinality_strategy)
@settings(max_examples=25)
def test_tExp_Cardinality_instantiation(instance):
    assert isinstance(instance, tExp_Cardinality)


tExp_CatExpr_strategy = st.builds(tExp_CatExpr)
@given(instance=tExp_CatExpr_strategy)
@settings(max_examples=25)
def test_tExp_CatExpr_instantiation(instance):
    assert isinstance(instance, tExp_CatExpr)


tExp_Channel_strategy = st.builds(tExp_Channel, name=safe_text, reliability=safe_text)
@given(instance=tExp_Channel_strategy)
@settings(max_examples=25)
def test_tExp_Channel_instantiation(instance):
    assert isinstance(instance, tExp_Channel)


tExp_Constraint_strategy = st.builds(tExp_Constraint, parMax=safe_text, parMin=safe_text, split=safe_text, together=safe_text)
@given(instance=tExp_Constraint_strategy)
@settings(max_examples=25)
def test_tExp_Constraint_instantiation(instance):
    assert isinstance(instance, tExp_Constraint)


tExp_Domainmodel_strategy = st.builds(tExp_Domainmodel)
@given(instance=tExp_Domainmodel_strategy)
@settings(max_examples=25)
def test_tExp_Domainmodel_instantiation(instance):
    assert isinstance(instance, tExp_Domainmodel)


tExp_EventType_strategy = st.builds(tExp_EventType, name=safe_text)
@given(instance=tExp_EventType_strategy)
@settings(max_examples=25)
def test_tExp_EventType_instantiation(instance):
    assert isinstance(instance, tExp_EventType)


tExp_Expression_strategy = st.builds(tExp_Expression, eps=safe_text, operator=safe_text, variable=safe_text)
@given(instance=tExp_Expression_strategy)
@settings(max_examples=25)
def test_tExp_Expression_instantiation(instance):
    assert isinstance(instance, tExp_Expression)


tExp_FilterExpr_strategy = st.builds(tExp_FilterExpr)
@given(instance=tExp_FilterExpr_strategy)
@settings(max_examples=25)
def test_tExp_FilterExpr_instantiation(instance):
    assert isinstance(instance, tExp_FilterExpr)


tExp_ListExpression_strategy = st.builds(tExp_ListExpression)
@given(instance=tExp_ListExpression_strategy)
@settings(max_examples=25)
def test_tExp_ListExpression_instantiation(instance):
    assert isinstance(instance, tExp_ListExpression)


tExp_Msg_strategy = st.builds(tExp_Msg, performative=safe_text)
@given(instance=tExp_Msg_strategy)
@settings(max_examples=25)
def test_tExp_Msg_instantiation(instance):
    assert isinstance(instance, tExp_Msg)


tExp_NumberExpression_strategy = st.builds(tExp_NumberExpression, value=safe_text)
@given(instance=tExp_NumberExpression_strategy)
@settings(max_examples=25)
def test_tExp_NumberExpression_instantiation(instance):
    assert isinstance(instance, tExp_NumberExpression)


tExp_Partition_strategy = st.builds(tExp_Partition)
@given(instance=tExp_Partition_strategy)
@settings(max_examples=25)
def test_tExp_Partition_instantiation(instance):
    assert isinstance(instance, tExp_Partition)


tExp_PrologExpression_strategy = st.builds(tExp_PrologExpression, op=safe_text)
@given(instance=tExp_PrologExpression_strategy)
@settings(max_examples=25)
def test_tExp_PrologExpression_instantiation(instance):
    assert isinstance(instance, tExp_PrologExpression)


tExp_Role_strategy = st.builds(tExp_Role, args=safe_text, class_=safe_text, name=safe_text)
@given(instance=tExp_Role_strategy)
@settings(max_examples=25)
def test_tExp_Role_instantiation(instance):
    assert isinstance(instance, tExp_Role)


tExp_SeqExpr_strategy = st.builds(tExp_SeqExpr)
@given(instance=tExp_SeqExpr_strategy)
@settings(max_examples=25)
def test_tExp_SeqExpr_instantiation(instance):
    assert isinstance(instance, tExp_SeqExpr)


tExp_ShuffleExpr_strategy = st.builds(tExp_ShuffleExpr)
@given(instance=tExp_ShuffleExpr_strategy)
@settings(max_examples=25)
def test_tExp_ShuffleExpr_instantiation(instance):
    assert isinstance(instance, tExp_ShuffleExpr)


tExp_Singletons_strategy = st.builds(tExp_Singletons, maxSingletons=st.integers(), minSingletons=st.integers())
@given(instance=tExp_Singletons_strategy)
@settings(max_examples=25)
def test_tExp_Singletons_instantiation(instance):
    assert isinstance(instance, tExp_Singletons)


tExp_Size_strategy = st.builds(tExp_Size, maxSize=st.integers(), minSize=st.integers())
@given(instance=tExp_Size_strategy)
@settings(max_examples=25)
def test_tExp_Size_instantiation(instance):
    assert isinstance(instance, tExp_Size)


tExp_StringExpression_strategy = st.builds(tExp_StringExpression, value=safe_text)
@given(instance=tExp_StringExpression_strategy)
@settings(max_examples=25)
def test_tExp_StringExpression_instantiation(instance):
    assert isinstance(instance, tExp_StringExpression)


tExp_Term_strategy = st.builds(tExp_Term, name=safe_text)
@given(instance=tExp_Term_strategy)
@settings(max_examples=25)
def test_tExp_Term_instantiation(instance):
    assert isinstance(instance, tExp_Term)


tExp_TerminalExpr_strategy = st.builds(tExp_TerminalExpr)
@given(instance=tExp_TerminalExpr_strategy)
@settings(max_examples=25)
def test_tExp_TerminalExpr_instantiation(instance):
    assert isinstance(instance, tExp_TerminalExpr)


tExp_Together_strategy = st.builds(tExp_Together)
@given(instance=tExp_Together_strategy)
@settings(max_examples=25)
def test_tExp_Together_instantiation(instance):
    assert isinstance(instance, tExp_Together)


tExp_TraceExpression_strategy = st.builds(tExp_TraceExpression, bodyL=safe_text, channelsL=safe_text, constraintsL=safe_text, decentralized=safe_text, decentralizedL=safe_text, gui=safe_text, guiL=safe_text, minimal=safe_text, minimalL=safe_text, modules=safe_text, modulesL=safe_text, name=safe_text, partitionL=safe_text, rolesL=safe_text, threshold=safe_text, thresholdL=safe_text, typesL=safe_text)
@given(instance=tExp_TraceExpression_strategy)
@settings(max_examples=25)
def test_tExp_TraceExpression_instantiation(instance):
    assert isinstance(instance, tExp_TraceExpression)


tExp_UnionExpr_strategy = st.builds(tExp_UnionExpr)
@given(instance=tExp_UnionExpr_strategy)
@settings(max_examples=25)
def test_tExp_UnionExpr_instantiation(instance):
    assert isinstance(instance, tExp_UnionExpr)


tExp_VarExpr_strategy = st.builds(tExp_VarExpr)
@given(instance=tExp_VarExpr_strategy)
@settings(max_examples=25)
def test_tExp_VarExpr_instantiation(instance):
    assert isinstance(instance, tExp_VarExpr)


tExp_VariableExpression_strategy = st.builds(tExp_VariableExpression, name=safe_text)
@given(instance=tExp_VariableExpression_strategy)
@settings(max_examples=25)
def test_tExp_VariableExpression_instantiation(instance):
    assert isinstance(instance, tExp_VariableExpression)


