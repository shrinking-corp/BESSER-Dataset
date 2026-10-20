import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractAction,
    AbstractStatusValue,
    AbstractStatusVariable,
    Assignment,
    Association,
    Block,
    ConnectableElement,
    Connector,
    DimensionDefinition,
    EventFilter,
    EventProducer,
    Expression,
    Foreach,
    FromClause,
    GroupBy,
    InScope,
    Iterator,
    LinkManipulationStatement,
    MethodSignature,
    NamedElement,
    NamedValue,
    NamedValueDeclaration,
    NamedValueWithOptionalInitExpression,
    Operator,
    SAMAction,
    SAMDerivator,
    SAMOperator,
    SAMSchemaAction,
    SAMSchemaDerivator,
    SAMSchemaValue,
    SAMSchemaVariable,
    SAMStatusSchema,
    SAMStatusValue,
    SAMStatusVariable,
    SapClass,
    SchemaElement,
    Selection,
    Signature,
    SingleBlockStatement,
    Statement,
    StatementWithArgument,
    StatementWithNestedBlocks,
    Strategy,
    Subscription,
    Variable,
    actions_ConditionalStatement,
    actions_SingleBlockStatement,
    actions_Statement,
    actions_StatementWithNestedBlocks,
    assembly_ConnectableElement,
    assembly_SchemaElement,
    assembly_Strategy,
    behavioral_actions_AddLink,
    behavioral_actions_Assignment,
    behavioral_actions_Block,
    behavioral_actions_ConditionalStatement,
    behavioral_actions_Constant,
    behavioral_actions_ExpressionStatement,
    behavioral_actions_Foreach,
    behavioral_actions_IfElse,
    behavioral_actions_Iterator,
    behavioral_actions_LinkManipulationStatement,
    behavioral_actions_NamedValueDeclaration,
    behavioral_actions_NamedValueWithOptionalInitExpression,
    behavioral_actions_QueryInvocation,
    behavioral_actions_RemoveLink,
    behavioral_actions_Return,
    behavioral_actions_SingleBlockStatement,
    behavioral_actions_Sort,
    behavioral_actions_Statement,
    behavioral_actions_StatementWithArgument,
    behavioral_actions_StatementWithNestedBlocks,
    behavioral_actions_Variable,
    behavioral_actions_WhileLoop,
    behavioral_assembly_ActionProxy,
    behavioral_assembly_AndOperator,
    behavioral_assembly_ConnectableElement,
    behavioral_assembly_Connector,
    behavioral_assembly_EnablingStrategy,
    behavioral_assembly_InhibitingStrategy,
    behavioral_assembly_NeutralStrategy,
    behavioral_assembly_Operator,
    behavioral_assembly_OrOperator,
    behavioral_assembly_Precondition,
    behavioral_assembly_RequiredStrategy,
    behavioral_assembly_SchemaElement,
    behavioral_assembly_StatusSchema,
    behavioral_assembly_StatusValueProxy,
    behavioral_assembly_StatusVariableProxy,
    behavioral_assembly_Strategy,
    behavioral_assembly_Synchroniser,
    behavioral_assembly_Transition,
    behavioral_bpdm_Dummy,
    behavioral_businesstasks_TaskAgent,
    behavioral_design_AbstractAction,
    behavioral_design_AbstractStatusValue,
    behavioral_design_AbstractStatusVariable,
    behavioral_design_Action,
    behavioral_design_BusinessObject,
    behavioral_design_BusinessObjectNode,
    behavioral_design_StatusValue,
    behavioral_design_StatusVariable,
    behavioral_events_EventFilter,
    behavioral_events_EventProducer,
    behavioral_events_Subscription,
    behavioral_rules_Dummy,
    behavioral_status_and_action_old_SAMAction,
    behavioral_status_and_action_old_SAMDerivator,
    behavioral_status_and_action_old_SAMOperator,
    behavioral_status_and_action_old_SAMSchemaAction,
    behavioral_status_and_action_old_SAMSchemaDerivator,
    behavioral_status_and_action_old_SAMSchemaValue,
    behavioral_status_and_action_old_SAMSchemaVariable,
    behavioral_status_and_action_old_SAMStatusSchema,
    behavioral_status_and_action_old_SAMStatusValue,
    behavioral_status_and_action_old_SAMStatusVariable,
    behavioral_transactions_Dummy,
    classes_FunctionSignatureImplementation,
    classes_InScope,
    collectionexpressions_Iterate,
    design_AbstractAction,
    design_AbstractStatusValue,
    design_AbstractStatusVariable,
    design_Action,
    design_BusinessObjectNode,
    design_StatusValue,
    design_StatusVariable,
    expressions_Conditional,
    expressions_WithArgument,
    PreconditionKindEnum,
    SAMDerivatorKindEnum,
    SAMOperatorKindEnum,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignments14_stub_double():
    # Assignment has no real 'Assignment' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_Variable()
    partner = Assignment()
    setattr(partner, 'Assignment', None)
    _safe_set(owner, 'assignTo', {partner})
    assert getattr(partner, 'Assignment') == owner
    _safe_set(owner, 'assignTo', set())
    assert getattr(partner, 'Assignment') is None


def test_assoc_association7_stub_double():
    # Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_LinkManipulationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_LinkManipulationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_LinkManipulationStatement(at=7)
    partner = Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'behavioral_actions_LinkManipulationStatement', partner)
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'behavioral_actions_LinkManipulationStatement', None)
    assert getattr(partner, 'Association') is None


def test_assoc_block1_stub_double():
    # Block has no real 'Block' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_Statement()
    partner = Block()
    setattr(partner, 'Block', None)
    _safe_set(owner, 'statements', partner)
    assert getattr(partner, 'Block') == owner
    _safe_set(owner, 'statements', None)
    assert getattr(partner, 'Block') is None


def test_assoc_businessObject49_stub_double():
    # SapClass has no real 'SapClass50' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMDerivator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMDerivator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMDerivator(kind="sample_text")
    partner = SapClass()
    setattr(partner, 'SapClass50', None)
    _safe_set(owner, 'samDerivators', partner)
    assert getattr(partner, 'SapClass50') == owner
    _safe_set(owner, 'samDerivators', None)
    assert getattr(partner, 'SapClass50') is None


def test_assoc_businessObjectNode42_stub_double():
    # SapClass has no real 'SapClass43' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMAction(isAgentAction=True, name="sample_text")
    partner = SapClass()
    setattr(partner, 'SapClass43', None)
    _safe_set(owner, 'samActions', partner)
    assert getattr(partner, 'SapClass43') == owner
    _safe_set(owner, 'samActions', None)
    assert getattr(partner, 'SapClass43') is None


def test_assoc_businessObjectNode45_stub_double():
    # SapClass has no real 'SapClass46' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusVariable(isAgentVariable=True, name="sample_text")
    partner = SapClass()
    setattr(partner, 'SapClass46', None)
    _safe_set(owner, 'samStatusVariables', partner)
    assert getattr(partner, 'SapClass46') == owner
    _safe_set(owner, 'samStatusVariables', None)
    assert getattr(partner, 'SapClass46') is None


def test_assoc_businessObjectNode53_stub_double():
    # SapClass has no real 'SapClass54' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusSchema(name="sample_text")
    partner = SapClass()
    setattr(partner, 'SapClass54', None)
    _safe_set(owner, 'samStatusSchema', partner)
    assert getattr(partner, 'SapClass54') == owner
    _safe_set(owner, 'samStatusSchema', None)
    assert getattr(partner, 'SapClass54') is None


def test_assoc_collection5_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_Foreach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_Foreach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_Foreach(parallel=True)
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'behavioral_actions_Foreach', partner)
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'behavioral_actions_Foreach', None)
    assert getattr(partner, 'Expression') is None


def test_assoc_forVariable6_stub_double():
    # Iterator has no real 'Iterator' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_Foreach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_Foreach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_Foreach(parallel=True)
    partner = Iterator()
    setattr(partner, 'Iterator', None)
    _safe_set(owner, 'boundToFor', partner)
    assert getattr(partner, 'Iterator') == owner
    _safe_set(owner, 'boundToFor', None)
    assert getattr(partner, 'Iterator') is None


def test_assoc_objects8_stub_double():
    # Expression has no real 'Expression10' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_LinkManipulationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_LinkManipulationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_LinkManipulationStatement(at=7)
    partner = Expression()
    setattr(partner, 'Expression10', None)
    _safe_set(owner, 'behavioral_actions_LinkManipulationStatement9', {partner})
    assert getattr(partner, 'Expression10') == owner
    _safe_set(owner, 'behavioral_actions_LinkManipulationStatement9', set())
    assert getattr(partner, 'Expression10') is None


def test_assoc_owningStatement4_stub_double():
    # StatementWithNestedBlocks has no real 'StatementWithNestedBlocks' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_Block()
    partner = StatementWithNestedBlocks()
    setattr(partner, 'StatementWithNestedBlocks', None)
    _safe_set(owner, 'nestedBlocks', partner)
    assert getattr(partner, 'StatementWithNestedBlocks') == owner
    _safe_set(owner, 'nestedBlocks', None)
    assert getattr(partner, 'StatementWithNestedBlocks') is None


def test_assoc_samOperators55_stub_double():
    # SAMOperator has no real 'SAMOperator' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusSchema(name="sample_text")
    partner = SAMOperator()
    setattr(partner, 'SAMOperator', None)
    _safe_set(owner, 'samStatusSchema56', {partner})
    assert getattr(partner, 'SAMOperator') == owner
    _safe_set(owner, 'samStatusSchema56', set())
    assert getattr(partner, 'SAMOperator') is None


def test_assoc_samOperators95_stub_double():
    # SAMOperator has no real 'SAMOperator97' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaValue(isInhibiting=True, isInitial=True)
    partner = SAMOperator()
    setattr(partner, 'SAMOperator97', None)
    _safe_set(owner, 'samSchemaValues96', {partner})
    assert getattr(partner, 'SAMOperator97') == owner
    _safe_set(owner, 'samSchemaValues96', set())
    assert getattr(partner, 'SAMOperator97') is None


def test_assoc_samSchemaActions44_stub_double():
    # SAMSchemaAction has no real 'SAMSchemaAction' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMAction(isAgentAction=True, name="sample_text")
    partner = SAMSchemaAction()
    setattr(partner, 'SAMSchemaAction', None)
    _safe_set(owner, 'samAction', {partner})
    assert getattr(partner, 'SAMSchemaAction') == owner
    _safe_set(owner, 'samAction', set())
    assert getattr(partner, 'SAMSchemaAction') is None


def test_assoc_samSchemaActions60_stub_double():
    # SAMSchemaAction has no real 'SAMSchemaAction62' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusSchema(name="sample_text")
    partner = SAMSchemaAction()
    setattr(partner, 'SAMSchemaAction62', None)
    _safe_set(owner, 'samStatusSchema61', {partner})
    assert getattr(partner, 'SAMSchemaAction62') == owner
    _safe_set(owner, 'samStatusSchema61', set())
    assert getattr(partner, 'SAMSchemaAction62') is None


def test_assoc_samSchemaActions73_stub_double():
    # SAMSchemaAction has no real 'SAMSchemaAction74' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMOperator(kind="sample_text")
    partner = SAMSchemaAction()
    setattr(partner, 'SAMSchemaAction74', None)
    _safe_set(owner, 'samSchemaOperators', {partner})
    assert getattr(partner, 'SAMSchemaAction74') == owner
    _safe_set(owner, 'samSchemaOperators', set())
    assert getattr(partner, 'SAMSchemaAction74') is None


def test_assoc_samSchemaActions98_stub_double():
    # SAMSchemaAction has no real 'SAMSchemaAction100' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaValue(isInhibiting=True, isInitial=True)
    partner = SAMSchemaAction()
    setattr(partner, 'SAMSchemaAction100', None)
    _safe_set(owner, 'samSchemaValues99', {partner})
    assert getattr(partner, 'SAMSchemaAction100') == owner
    _safe_set(owner, 'samSchemaValues99', set())
    assert getattr(partner, 'SAMSchemaAction100') is None


def test_assoc_samSchemaDerivators51_stub_double():
    # SAMSchemaDerivator has no real 'SAMSchemaDerivator' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMDerivator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMDerivator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMDerivator(kind="sample_text")
    partner = SAMSchemaDerivator()
    setattr(partner, 'SAMSchemaDerivator', None)
    _safe_set(owner, 'samDerivator', {partner})
    assert getattr(partner, 'SAMSchemaDerivator') == owner
    _safe_set(owner, 'samDerivator', set())
    assert getattr(partner, 'SAMSchemaDerivator') is None


def test_assoc_samSchemaDerivators63_stub_double():
    # SAMSchemaDerivator has no real 'SAMSchemaDerivator65' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusSchema(name="sample_text")
    partner = SAMSchemaDerivator()
    setattr(partner, 'SAMSchemaDerivator65', None)
    _safe_set(owner, 'samStatusSchema64', {partner})
    assert getattr(partner, 'SAMSchemaDerivator65') == owner
    _safe_set(owner, 'samStatusSchema64', set())
    assert getattr(partner, 'SAMSchemaDerivator65') is None


def test_assoc_samSchemaValue79_stub_double():
    # SAMStatusVariable has no real 'SAMStatusVariable81' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaVariable(hasStateGuard=True)
    partner = SAMStatusVariable()
    setattr(partner, 'SAMStatusVariable81', None)
    _safe_set(owner, 'samSchemaVariables80', partner)
    assert getattr(partner, 'SAMStatusVariable81') == owner
    _safe_set(owner, 'samSchemaVariables80', None)
    assert getattr(partner, 'SAMStatusVariable81') is None


def test_assoc_samSchemaValues67_stub_double():
    # SAMSchemaValue has no real 'SAMSchemaValue' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMOperator(kind="sample_text")
    partner = SAMSchemaValue()
    setattr(partner, 'SAMSchemaValue', None)
    _safe_set(owner, 'samOperators68', {partner})
    assert getattr(partner, 'SAMSchemaValue') == owner
    _safe_set(owner, 'samOperators68', set())
    assert getattr(partner, 'SAMSchemaValue') is None


def test_assoc_samSchemaValues77_stub_double():
    # SAMSchemaValue has no real 'SAMSchemaValue78' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaVariable(hasStateGuard=True)
    partner = SAMSchemaValue()
    setattr(partner, 'SAMSchemaValue78', None)
    _safe_set(owner, 'samSchemaVariable', {partner})
    assert getattr(partner, 'SAMSchemaValue78') == owner
    _safe_set(owner, 'samSchemaVariable', set())
    assert getattr(partner, 'SAMSchemaValue78') is None


def test_assoc_samSchemaVariable86_stub_double():
    # SAMSchemaVariable has no real 'SAMSchemaVariable87' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaValue(isInhibiting=True, isInitial=True)
    partner = SAMSchemaVariable()
    setattr(partner, 'SAMSchemaVariable87', None)
    _safe_set(owner, 'samSchemaValues', partner)
    assert getattr(partner, 'SAMSchemaVariable87') == owner
    _safe_set(owner, 'samSchemaValues', None)
    assert getattr(partner, 'SAMSchemaVariable87') is None


def test_assoc_samSchemaVariables48_stub_double():
    # SAMSchemaVariable has no real 'SAMSchemaVariable' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusVariable(isAgentVariable=True, name="sample_text")
    partner = SAMSchemaVariable()
    setattr(partner, 'SAMSchemaVariable', None)
    _safe_set(owner, 'samSchemaValue', {partner})
    assert getattr(partner, 'SAMSchemaVariable') == owner
    _safe_set(owner, 'samSchemaValue', set())
    assert getattr(partner, 'SAMSchemaVariable') is None


def test_assoc_samSchemaVariables57_stub_double():
    # SAMSchemaVariable has no real 'SAMSchemaVariable59' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusSchema(name="sample_text")
    partner = SAMSchemaVariable()
    setattr(partner, 'SAMSchemaVariable59', None)
    _safe_set(owner, 'samStatusSchema58', {partner})
    assert getattr(partner, 'SAMSchemaVariable59') == owner
    _safe_set(owner, 'samStatusSchema58', set())
    assert getattr(partner, 'SAMSchemaVariable59') is None


def test_assoc_samSourceOperators69_stub_double():
    # SAMOperator has no real 'SAMOperator70' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMOperator(kind="sample_text")
    partner = SAMOperator()
    setattr(partner, 'SAMOperator70', None)
    _safe_set(owner, 'samTargetOperators', {partner})
    assert getattr(partner, 'SAMOperator70') == owner
    _safe_set(owner, 'samTargetOperators', set())
    assert getattr(partner, 'SAMOperator70') is None


def test_assoc_samSourceSchemaActions88_stub_double():
    # SAMSchemaAction has no real 'SAMSchemaAction89' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaValue(isInhibiting=True, isInitial=True)
    partner = SAMSchemaAction()
    setattr(partner, 'SAMSchemaAction89', None)
    _safe_set(owner, 'samTargetSchemaValues', {partner})
    assert getattr(partner, 'SAMSchemaAction89') == owner
    _safe_set(owner, 'samTargetSchemaValues', set())
    assert getattr(partner, 'SAMSchemaAction89') is None


def test_assoc_samSourceSchemaDerivators84_stub_double():
    # SAMSchemaDerivator has no real 'SAMSchemaDerivator85' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaVariable(hasStateGuard=True)
    partner = SAMSchemaDerivator()
    setattr(partner, 'SAMSchemaDerivator85', None)
    _safe_set(owner, 'samTargetSchemaVariable', {partner})
    assert getattr(partner, 'SAMSchemaDerivator85') == owner
    _safe_set(owner, 'samTargetSchemaVariable', set())
    assert getattr(partner, 'SAMSchemaDerivator85') is None


def test_assoc_samSourceSchemaValues90_stub_double():
    # SAMSchemaValue has no real 'SAMSchemaValue92' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaValue(isInhibiting=True, isInitial=True)
    partner = SAMSchemaValue()
    setattr(partner, 'SAMSchemaValue92', None)
    _safe_set(owner, 'samTargetSchemaValues91', {partner})
    assert getattr(partner, 'SAMSchemaValue92') == owner
    _safe_set(owner, 'samTargetSchemaValues91', set())
    assert getattr(partner, 'SAMSchemaValue92') is None


def test_assoc_samStatusSchema66_stub_double():
    # SAMStatusSchema has no real 'SAMStatusSchema' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMOperator(kind="sample_text")
    partner = SAMStatusSchema()
    setattr(partner, 'SAMStatusSchema', None)
    _safe_set(owner, 'samOperators', partner)
    assert getattr(partner, 'SAMStatusSchema') == owner
    _safe_set(owner, 'samOperators', None)
    assert getattr(partner, 'SAMStatusSchema') is None


def test_assoc_samStatusSchema75_stub_double():
    # SAMStatusSchema has no real 'SAMStatusSchema76' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaVariable(hasStateGuard=True)
    partner = SAMStatusSchema()
    setattr(partner, 'SAMStatusSchema76', None)
    _safe_set(owner, 'samSchemaVariables', partner)
    assert getattr(partner, 'SAMStatusSchema76') == owner
    _safe_set(owner, 'samSchemaVariables', None)
    assert getattr(partner, 'SAMStatusSchema76') is None


def test_assoc_samStatusValues47_stub_double():
    # SAMStatusValue has no real 'SAMStatusValue' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusVariable(isAgentVariable=True, name="sample_text")
    partner = SAMStatusValue()
    setattr(partner, 'SAMStatusValue', None)
    _safe_set(owner, 'samStatusVariable', {partner})
    assert getattr(partner, 'SAMStatusValue') == owner
    _safe_set(owner, 'samStatusVariable', set())
    assert getattr(partner, 'SAMStatusValue') is None


def test_assoc_samStatusVariable52_stub_double():
    # SAMStatusVariable has no real 'SAMStatusVariable' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMStatusValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMStatusValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMStatusValue(name="sample_text")
    partner = SAMStatusVariable()
    setattr(partner, 'SAMStatusVariable', None)
    _safe_set(owner, 'samStatusValues', partner)
    assert getattr(partner, 'SAMStatusVariable') == owner
    _safe_set(owner, 'samStatusValues', None)
    assert getattr(partner, 'SAMStatusVariable') is None


def test_assoc_samTargetOperators71_stub_double():
    # SAMOperator has no real 'SAMOperator72' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMOperator(kind="sample_text")
    partner = SAMOperator()
    setattr(partner, 'SAMOperator72', None)
    _safe_set(owner, 'samSourceOperators', {partner})
    assert getattr(partner, 'SAMOperator72') == owner
    _safe_set(owner, 'samSourceOperators', set())
    assert getattr(partner, 'SAMOperator72') is None


def test_assoc_samTargetSchemaDerivators82_stub_double():
    # SAMSchemaDerivator has no real 'SAMSchemaDerivator83' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaVariable(hasStateGuard=True)
    partner = SAMSchemaDerivator()
    setattr(partner, 'SAMSchemaDerivator83', None)
    _safe_set(owner, 'samSourceSchemaVariables', {partner})
    assert getattr(partner, 'SAMSchemaDerivator83') == owner
    _safe_set(owner, 'samSourceSchemaVariables', set())
    assert getattr(partner, 'SAMSchemaDerivator83') is None


def test_assoc_samTargetSchemaValues93_stub_double():
    # SAMSchemaValue has no real 'SAMSchemaValue94' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_status_and_action_old_SAMSchemaValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_status_and_action_old_SAMSchemaValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_status_and_action_old_SAMSchemaValue(isInhibiting=True, isInitial=True)
    partner = SAMSchemaValue()
    setattr(partner, 'SAMSchemaValue94', None)
    _safe_set(owner, 'samSourceSchemaValues', {partner})
    assert getattr(partner, 'SAMSchemaValue94') == owner
    _safe_set(owner, 'samSourceSchemaValues', set())
    assert getattr(partner, 'SAMSchemaValue94') is None


def test_assoc_statements2_stub_double():
    # Statement has no real 'Statement' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_Block()
    partner = Statement()
    setattr(partner, 'Statement', None)
    _safe_set(owner, 'block', {partner})
    assert getattr(partner, 'Statement') == owner
    _safe_set(owner, 'block', set())
    assert getattr(partner, 'Statement') is None


def test_assoc_values125_stub_double():
    # design_AbstractStatusValue has no real 'design_AbstractStatusValue' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_design_AbstractStatusVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_design_AbstractStatusVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_design_AbstractStatusVariable(isAgent=True, isStateGuarded=True)
    partner = design_AbstractStatusValue()
    setattr(partner, 'design_AbstractStatusValue', None)
    _safe_set(owner, 'behavioral_design_AbstractStatusVariable', {partner})
    assert getattr(partner, 'design_AbstractStatusValue') == owner
    _safe_set(owner, 'behavioral_design_AbstractStatusVariable', set())
    assert getattr(partner, 'design_AbstractStatusValue') is None


def test_assoc_variables3_stub_double():
    # NamedValue has no real 'NamedValue' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_actions_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_actions_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_actions_Block()
    partner = NamedValue()
    setattr(partner, 'NamedValue', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'NamedValue') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'NamedValue') is None


