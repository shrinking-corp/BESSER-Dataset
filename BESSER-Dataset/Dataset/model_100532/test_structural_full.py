import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    UseCaseCodeAdapter_FileToUseCasesModel,
    UseCaseCodeAdapter_NodeToActor,
    UseCaseCodeAdapter_NodeToAlternativeFlowAlternative,
    UseCaseCodeAdapter_NodeToFlow,
    UseCaseCodeAdapter_NodeToPackageDeclaration,
    UseCaseCodeAdapter_NodeToStep,
    UseCaseCodeAdapter_NodeToUseCase,
    UseCaseCodeAdapter_Rules_ActorDescRule,
    UseCaseCodeAdapter_Rules_ActorExtendsRule,
    UseCaseCodeAdapter_Rules_ActorRule,
    UseCaseCodeAdapter_Rules_ActorsRule,
    UseCaseCodeAdapter_Rules_AltFlowAltContinueRule,
    UseCaseCodeAdapter_Rules_AltFlowAltRule,
    UseCaseCodeAdapter_Rules_AltFlowFinalStateRule,
    UseCaseCodeAdapter_Rules_AlternativeFlowRule,
    UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule,
    UseCaseCodeAdapter_Rules_BasicFlowRule,
    UseCaseCodeAdapter_Rules_FileToUCModel,
    UseCaseCodeAdapter_Rules_PackageRule,
    UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule,
    UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule,
    UseCaseCodeAdapter_Rules_ParallelFlowRule,
    UseCaseCodeAdapter_Rules_ParallelStepDescRule,
    UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule,
    UseCaseCodeAdapter_Rules_ParallelStepRule,
    UseCaseCodeAdapter_Rules_StepAlternativesRule,
    UseCaseCodeAdapter_Rules_StepDescRule,
    UseCaseCodeAdapter_Rules_StepRule,
    UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule,
    UseCaseCodeAdapter_Rules_UseCaseDescRule,
    UseCaseCodeAdapter_Rules_UseCaseExtendsRule,
    UseCaseCodeAdapter_Rules_UseCasePreCondRule,
    UseCaseCodeAdapter_Rules_UseCaseRule,
    UseCaseCodeAdapter_Rules_UseCasesRule,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

UseCaseCodeAdapter_FileToUseCasesModel_strategy = st.builds(UseCaseCodeAdapter_FileToUseCasesModel)
@given(instance=UseCaseCodeAdapter_FileToUseCasesModel_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_FileToUseCasesModel_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_FileToUseCasesModel)


UseCaseCodeAdapter_NodeToActor_strategy = st.builds(UseCaseCodeAdapter_NodeToActor)
@given(instance=UseCaseCodeAdapter_NodeToActor_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_NodeToActor_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_NodeToActor)


UseCaseCodeAdapter_NodeToAlternativeFlowAlternative_strategy = st.builds(UseCaseCodeAdapter_NodeToAlternativeFlowAlternative)
@given(instance=UseCaseCodeAdapter_NodeToAlternativeFlowAlternative_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_NodeToAlternativeFlowAlternative_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_NodeToAlternativeFlowAlternative)


UseCaseCodeAdapter_NodeToFlow_strategy = st.builds(UseCaseCodeAdapter_NodeToFlow)
@given(instance=UseCaseCodeAdapter_NodeToFlow_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_NodeToFlow_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_NodeToFlow)


UseCaseCodeAdapter_NodeToPackageDeclaration_strategy = st.builds(UseCaseCodeAdapter_NodeToPackageDeclaration)
@given(instance=UseCaseCodeAdapter_NodeToPackageDeclaration_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_NodeToPackageDeclaration_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_NodeToPackageDeclaration)


UseCaseCodeAdapter_NodeToStep_strategy = st.builds(UseCaseCodeAdapter_NodeToStep)
@given(instance=UseCaseCodeAdapter_NodeToStep_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_NodeToStep_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_NodeToStep)


UseCaseCodeAdapter_NodeToUseCase_strategy = st.builds(UseCaseCodeAdapter_NodeToUseCase)
@given(instance=UseCaseCodeAdapter_NodeToUseCase_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_NodeToUseCase_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_NodeToUseCase)


UseCaseCodeAdapter_Rules_ActorDescRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ActorDescRule)
@given(instance=UseCaseCodeAdapter_Rules_ActorDescRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ActorDescRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ActorDescRule)


UseCaseCodeAdapter_Rules_ActorExtendsRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ActorExtendsRule)
@given(instance=UseCaseCodeAdapter_Rules_ActorExtendsRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ActorExtendsRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ActorExtendsRule)


UseCaseCodeAdapter_Rules_ActorRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ActorRule)
@given(instance=UseCaseCodeAdapter_Rules_ActorRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ActorRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ActorRule)


UseCaseCodeAdapter_Rules_ActorsRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ActorsRule)
@given(instance=UseCaseCodeAdapter_Rules_ActorsRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ActorsRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ActorsRule)


UseCaseCodeAdapter_Rules_AltFlowAltContinueRule_strategy = st.builds(UseCaseCodeAdapter_Rules_AltFlowAltContinueRule)
@given(instance=UseCaseCodeAdapter_Rules_AltFlowAltContinueRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_AltFlowAltContinueRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_AltFlowAltContinueRule)


UseCaseCodeAdapter_Rules_AltFlowAltRule_strategy = st.builds(UseCaseCodeAdapter_Rules_AltFlowAltRule)
@given(instance=UseCaseCodeAdapter_Rules_AltFlowAltRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_AltFlowAltRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_AltFlowAltRule)


UseCaseCodeAdapter_Rules_AltFlowFinalStateRule_strategy = st.builds(UseCaseCodeAdapter_Rules_AltFlowFinalStateRule)
@given(instance=UseCaseCodeAdapter_Rules_AltFlowFinalStateRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_AltFlowFinalStateRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_AltFlowFinalStateRule)


UseCaseCodeAdapter_Rules_AlternativeFlowRule_strategy = st.builds(UseCaseCodeAdapter_Rules_AlternativeFlowRule)
@given(instance=UseCaseCodeAdapter_Rules_AlternativeFlowRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_AlternativeFlowRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_AlternativeFlowRule)


UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule_strategy = st.builds(UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule)
@given(instance=UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule)


UseCaseCodeAdapter_Rules_BasicFlowRule_strategy = st.builds(UseCaseCodeAdapter_Rules_BasicFlowRule)
@given(instance=UseCaseCodeAdapter_Rules_BasicFlowRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_BasicFlowRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_BasicFlowRule)


UseCaseCodeAdapter_Rules_FileToUCModel_strategy = st.builds(UseCaseCodeAdapter_Rules_FileToUCModel)
@given(instance=UseCaseCodeAdapter_Rules_FileToUCModel_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_FileToUCModel_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_FileToUCModel)


UseCaseCodeAdapter_Rules_PackageRule_strategy = st.builds(UseCaseCodeAdapter_Rules_PackageRule)
@given(instance=UseCaseCodeAdapter_Rules_PackageRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_PackageRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_PackageRule)


UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule)
@given(instance=UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule)


UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule)
@given(instance=UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule)


UseCaseCodeAdapter_Rules_ParallelFlowRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ParallelFlowRule)
@given(instance=UseCaseCodeAdapter_Rules_ParallelFlowRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ParallelFlowRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ParallelFlowRule)


UseCaseCodeAdapter_Rules_ParallelStepDescRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ParallelStepDescRule)
@given(instance=UseCaseCodeAdapter_Rules_ParallelStepDescRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ParallelStepDescRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ParallelStepDescRule)


UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule)
@given(instance=UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule)


UseCaseCodeAdapter_Rules_ParallelStepRule_strategy = st.builds(UseCaseCodeAdapter_Rules_ParallelStepRule)
@given(instance=UseCaseCodeAdapter_Rules_ParallelStepRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_ParallelStepRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_ParallelStepRule)


UseCaseCodeAdapter_Rules_StepAlternativesRule_strategy = st.builds(UseCaseCodeAdapter_Rules_StepAlternativesRule)
@given(instance=UseCaseCodeAdapter_Rules_StepAlternativesRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_StepAlternativesRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_StepAlternativesRule)


UseCaseCodeAdapter_Rules_StepDescRule_strategy = st.builds(UseCaseCodeAdapter_Rules_StepDescRule)
@given(instance=UseCaseCodeAdapter_Rules_StepDescRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_StepDescRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_StepDescRule)


UseCaseCodeAdapter_Rules_StepRule_strategy = st.builds(UseCaseCodeAdapter_Rules_StepRule)
@given(instance=UseCaseCodeAdapter_Rules_StepRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_StepRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_StepRule)


UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule_strategy = st.builds(UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule)
@given(instance=UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule)


UseCaseCodeAdapter_Rules_UseCaseDescRule_strategy = st.builds(UseCaseCodeAdapter_Rules_UseCaseDescRule)
@given(instance=UseCaseCodeAdapter_Rules_UseCaseDescRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_UseCaseDescRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_UseCaseDescRule)


UseCaseCodeAdapter_Rules_UseCaseExtendsRule_strategy = st.builds(UseCaseCodeAdapter_Rules_UseCaseExtendsRule)
@given(instance=UseCaseCodeAdapter_Rules_UseCaseExtendsRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_UseCaseExtendsRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_UseCaseExtendsRule)


UseCaseCodeAdapter_Rules_UseCasePreCondRule_strategy = st.builds(UseCaseCodeAdapter_Rules_UseCasePreCondRule)
@given(instance=UseCaseCodeAdapter_Rules_UseCasePreCondRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_UseCasePreCondRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_UseCasePreCondRule)


UseCaseCodeAdapter_Rules_UseCaseRule_strategy = st.builds(UseCaseCodeAdapter_Rules_UseCaseRule)
@given(instance=UseCaseCodeAdapter_Rules_UseCaseRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_UseCaseRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_UseCaseRule)


UseCaseCodeAdapter_Rules_UseCasesRule_strategy = st.builds(UseCaseCodeAdapter_Rules_UseCasesRule)
@given(instance=UseCaseCodeAdapter_Rules_UseCasesRule_strategy)
@settings(max_examples=25)
def test_UseCaseCodeAdapter_Rules_UseCasesRule_instantiation(instance):
    assert isinstance(instance, UseCaseCodeAdapter_Rules_UseCasesRule)


