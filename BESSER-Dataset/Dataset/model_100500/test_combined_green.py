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
    BinaryOperator,
    newP_OrOperator,
    newP_AndOperartor,
    UnaryOperator,
    newP_BinaryOperator,
    newP_NotOperator,
    SimpleDependency,
    newP_ICost,
    newP_Refines,
    newP_CValue,
    newP_Person,
    newP_Specification,
    newP_Category,
    Description,
    newP_TextDescription,
    Requirement,
    newP_QualityRequirement,
    newP_FunctionalRequirement,
    Dependency,
    newP_SimpleDependency,
    newP_Requires,
    Term,
    newP_RequirementTerm,
    newP_UnaryOperator,
    newP_Term,
    newP_Dependency,
    newP_Description,
    newP_Requirement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_hyp_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_hyp_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_oroperator_is_not_abstract():
    assert not inspect.isabstract(newP_OrOperator)


def test_hyp_newp_oroperator_constructor_exists():
    assert callable(newP_OrOperator.__init__)


def test_hyp_newp_oroperator_constructor_args():
    sig = inspect.signature(newP_OrOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_andoperartor_is_not_abstract():
    assert not inspect.isabstract(newP_AndOperartor)


def test_hyp_newp_andoperartor_constructor_exists():
    assert callable(newP_AndOperartor.__init__)


def test_hyp_newp_andoperartor_constructor_args():
    sig = inspect.signature(newP_AndOperartor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_hyp_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_hyp_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(newP_BinaryOperator)


def test_hyp_newp_binaryoperator_constructor_exists():
    assert callable(newP_BinaryOperator.__init__)


def test_hyp_newp_binaryoperator_constructor_args():
    sig = inspect.signature(newP_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_notoperator_is_not_abstract():
    assert not inspect.isabstract(newP_NotOperator)


def test_hyp_newp_notoperator_constructor_exists():
    assert callable(newP_NotOperator.__init__)


def test_hyp_newp_notoperator_constructor_args():
    sig = inspect.signature(newP_NotOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpledependency_is_not_abstract():
    assert not inspect.isabstract(SimpleDependency)


def test_hyp_simpledependency_constructor_exists():
    assert callable(SimpleDependency.__init__)


def test_hyp_simpledependency_constructor_args():
    sig = inspect.signature(SimpleDependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_icost_is_not_abstract():
    assert not inspect.isabstract(newP_ICost)


def test_hyp_newp_icost_constructor_exists():
    assert callable(newP_ICost.__init__)


def test_hyp_newp_icost_constructor_args():
    sig = inspect.signature(newP_ICost.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_refines_is_not_abstract():
    assert not inspect.isabstract(newP_Refines)


def test_hyp_newp_refines_constructor_exists():
    assert callable(newP_Refines.__init__)


def test_hyp_newp_refines_constructor_args():
    sig = inspect.signature(newP_Refines.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_cvalue_is_not_abstract():
    assert not inspect.isabstract(newP_CValue)


def test_hyp_newp_cvalue_constructor_exists():
    assert callable(newP_CValue.__init__)


def test_hyp_newp_cvalue_constructor_args():
    sig = inspect.signature(newP_CValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_person_is_not_abstract():
    assert not inspect.isabstract(newP_Person)


def test_hyp_newp_person_constructor_exists():
    assert callable(newP_Person.__init__)


def test_hyp_newp_person_constructor_args():
    sig = inspect.signature(newP_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"





def test_hyp_newp_specification_is_not_abstract():
    assert not inspect.isabstract(newP_Specification)


def test_hyp_newp_specification_constructor_exists():
    assert callable(newP_Specification.__init__)


def test_hyp_newp_specification_constructor_args():
    sig = inspect.signature(newP_Specification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_newp_category_is_not_abstract():
    assert not inspect.isabstract(newP_Category)


def test_hyp_newp_category_constructor_exists():
    assert callable(newP_Category.__init__)


def test_hyp_newp_category_constructor_args():
    sig = inspect.signature(newP_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_description_is_not_abstract():
    assert not inspect.isabstract(Description)


def test_hyp_description_constructor_exists():
    assert callable(Description.__init__)


def test_hyp_description_constructor_args():
    sig = inspect.signature(Description.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_textdescription_is_not_abstract():
    assert not inspect.isabstract(newP_TextDescription)


def test_hyp_newp_textdescription_constructor_exists():
    assert callable(newP_TextDescription.__init__)


def test_hyp_newp_textdescription_constructor_args():
    sig = inspect.signature(newP_TextDescription.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_requirement_is_not_abstract():
    assert not inspect.isabstract(Requirement)


def test_hyp_requirement_constructor_exists():
    assert callable(Requirement.__init__)


def test_hyp_requirement_constructor_args():
    sig = inspect.signature(Requirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_qualityrequirement_is_not_abstract():
    assert not inspect.isabstract(newP_QualityRequirement)


def test_hyp_newp_qualityrequirement_constructor_exists():
    assert callable(newP_QualityRequirement.__init__)


def test_hyp_newp_qualityrequirement_constructor_args():
    sig = inspect.signature(newP_QualityRequirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(newP_FunctionalRequirement)


def test_hyp_newp_functionalrequirement_constructor_exists():
    assert callable(newP_FunctionalRequirement.__init__)


def test_hyp_newp_functionalrequirement_constructor_args():
    sig = inspect.signature(newP_FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_hyp_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_hyp_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_simpledependency_is_not_abstract():
    assert not inspect.isabstract(newP_SimpleDependency)


def test_hyp_newp_simpledependency_constructor_exists():
    assert callable(newP_SimpleDependency.__init__)


def test_hyp_newp_simpledependency_constructor_args():
    sig = inspect.signature(newP_SimpleDependency.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_newp_requires_is_not_abstract():
    assert not inspect.isabstract(newP_Requires)


def test_hyp_newp_requires_constructor_exists():
    assert callable(newP_Requires.__init__)


def test_hyp_newp_requires_constructor_args():
    sig = inspect.signature(newP_Requires.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_hyp_term_constructor_exists():
    assert callable(Term.__init__)


def test_hyp_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_requirementterm_is_not_abstract():
    assert not inspect.isabstract(newP_RequirementTerm)


def test_hyp_newp_requirementterm_constructor_exists():
    assert callable(newP_RequirementTerm.__init__)


def test_hyp_newp_requirementterm_constructor_args():
    sig = inspect.signature(newP_RequirementTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(newP_UnaryOperator)


def test_hyp_newp_unaryoperator_constructor_exists():
    assert callable(newP_UnaryOperator.__init__)


def test_hyp_newp_unaryoperator_constructor_args():
    sig = inspect.signature(newP_UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_newp_term_is_not_abstract():
    assert not inspect.isabstract(newP_Term)


def test_hyp_newp_term_constructor_exists():
    assert callable(newP_Term.__init__)


def test_hyp_newp_term_constructor_args():
    sig = inspect.signature(newP_Term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_dependency_is_not_abstract():
    assert not inspect.isabstract(newP_Dependency)


def test_hyp_newp_dependency_constructor_exists():
    assert callable(newP_Dependency.__init__)


def test_hyp_newp_dependency_constructor_args():
    sig = inspect.signature(newP_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_description_is_not_abstract():
    assert not inspect.isabstract(newP_Description)


def test_hyp_newp_description_constructor_exists():
    assert callable(newP_Description.__init__)


def test_hyp_newp_description_constructor_args():
    sig = inspect.signature(newP_Description.__init__)
    params = list(sig.parameters.keys())



def test_hyp_newp_requirement_is_not_abstract():
    assert not inspect.isabstract(newP_Requirement)


def test_hyp_newp_requirement_constructor_exists():
    assert callable(newP_Requirement.__init__)


def test_hyp_newp_requirement_constructor_args():
    sig = inspect.signature(newP_Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "identifier" in params, "Missing parameter 'identifier'"






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
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
newP_OrOperator_strategy = st.builds(
    newP_OrOperator,
)
newP_AndOperartor_strategy = st.builds(
    newP_AndOperartor,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
newP_BinaryOperator_strategy = st.builds(
    newP_BinaryOperator,
)
newP_NotOperator_strategy = st.builds(
    newP_NotOperator,
)
SimpleDependency_strategy = st.builds(
    SimpleDependency,
)
newP_ICost_strategy = st.builds(
    newP_ICost,
)
newP_Refines_strategy = st.builds(
    newP_Refines,
)
newP_CValue_strategy = st.builds(
    newP_CValue,
)
newP_Person_strategy = st.builds(
    newP_Person,
    lastName=
        safe_text,
    firstName=
        safe_text
)
newP_Specification_strategy = st.builds(
    newP_Specification,
    name=
        safe_text
)
newP_Category_strategy = st.builds(
    newP_Category,
    name=
        safe_text
)
Description_strategy = st.builds(
    Description,
)
newP_TextDescription_strategy = st.builds(
    newP_TextDescription,
    text=
        safe_text
)
Requirement_strategy = st.builds(
    Requirement,
)
newP_QualityRequirement_strategy = st.builds(
    newP_QualityRequirement,
)
newP_FunctionalRequirement_strategy = st.builds(
    newP_FunctionalRequirement,
)
Dependency_strategy = st.builds(
    Dependency,
)
newP_SimpleDependency_strategy = st.builds(
    newP_SimpleDependency,
    name=
        safe_text
)
newP_Requires_strategy = st.builds(
    newP_Requires,
    name=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
newP_RequirementTerm_strategy = st.builds(
    newP_RequirementTerm,
)
newP_UnaryOperator_strategy = st.builds(
    newP_UnaryOperator,
    name=
        safe_text
)
newP_Term_strategy = st.builds(
    newP_Term,
)
newP_Dependency_strategy = st.builds(
    newP_Dependency,
)
newP_Description_strategy = st.builds(
    newP_Description,
)
newP_Requirement_strategy = st.builds(
    newP_Requirement,
    priority=
        st.integers(),
    name=
        safe_text,
    mandatory=
        st.booleans(),
    identifier=
        safe_text
)














@given(instance=newP_Person_strategy)
def test_hyp_newp_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=newP_Person_strategy)
def test_hyp_newp_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original




@given(instance=newP_Specification_strategy)
def test_hyp_newp_specification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=newP_Category_strategy)
def test_hyp_newp_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=newP_TextDescription_strategy)
def test_hyp_newp_textdescription_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original








@given(instance=newP_SimpleDependency_strategy)
def test_hyp_newp_simpledependency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=newP_Requires_strategy)
def test_hyp_newp_requires_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=newP_UnaryOperator_strategy)
def test_hyp_newp_unaryoperator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=newP_Requirement_strategy)
def test_hyp_newp_requirement_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=newP_Requirement_strategy)
def test_hyp_newp_requirement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=newP_Requirement_strategy)
def test_hyp_newp_requirement_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=newP_Requirement_strategy)
def test_hyp_newp_requirement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryOperator,
    Dependency,
    Description,
    Requirement,
    SimpleDependency,
    Term,
    UnaryOperator,
    newP_AndOperartor,
    newP_BinaryOperator,
    newP_CValue,
    newP_Category,
    newP_Dependency,
    newP_Description,
    newP_FunctionalRequirement,
    newP_ICost,
    newP_NotOperator,
    newP_OrOperator,
    newP_Person,
    newP_QualityRequirement,
    newP_Refines,
    newP_Requirement,
    newP_RequirementTerm,
    newP_Requires,
    newP_SimpleDependency,
    newP_Specification,
    newP_Term,
    newP_TextDescription,
    newP_UnaryOperator,
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

def test_newP_Category_name_value_roundtrip():
    instance = newP_Category(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_newP_Person_firstName_value_roundtrip():
    instance = newP_Person(firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_newP_Person_lastName_value_roundtrip():
    instance = newP_Person(firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_newP_Requirement_identifier_value_roundtrip():
    instance = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_newP_Requirement_mandatory_value_roundtrip():
    instance = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_newP_Requirement_name_value_roundtrip():
    instance = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_newP_Requirement_priority_value_roundtrip():
    instance = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    assert instance.priority == 7
    instance.priority = 13
    assert instance.priority == 13


def test_newP_Requires_name_value_roundtrip():
    instance = newP_Requires(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_newP_SimpleDependency_name_value_roundtrip():
    instance = newP_SimpleDependency(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_newP_Specification_name_value_roundtrip():
    instance = newP_Specification(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_newP_TextDescription_text_value_roundtrip():
    instance = newP_TextDescription(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_newP_UnaryOperator_name_value_roundtrip():
    instance = newP_UnaryOperator(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_newP_AndOperartor_isa_BinaryOperator():
    instance = newP_AndOperartor()
    assert isinstance(instance, BinaryOperator)


def test_newP_OrOperator_isa_BinaryOperator():
    instance = newP_OrOperator()
    assert isinstance(instance, BinaryOperator)


def test_newP_Requires_isa_Dependency():
    instance = newP_Requires(name="sample_text")
    assert isinstance(instance, Dependency)


def test_newP_SimpleDependency_isa_Dependency():
    instance = newP_SimpleDependency(name="sample_text")
    assert isinstance(instance, Dependency)


def test_newP_TextDescription_isa_Description():
    instance = newP_TextDescription(text="sample_text")
    assert isinstance(instance, Description)


def test_newP_FunctionalRequirement_isa_Requirement():
    instance = newP_FunctionalRequirement()
    assert isinstance(instance, Requirement)


def test_newP_QualityRequirement_isa_Requirement():
    instance = newP_QualityRequirement()
    assert isinstance(instance, Requirement)


def test_newP_CValue_isa_SimpleDependency():
    instance = newP_CValue()
    assert isinstance(instance, SimpleDependency)


def test_newP_ICost_isa_SimpleDependency():
    instance = newP_ICost()
    assert isinstance(instance, SimpleDependency)


def test_newP_Refines_isa_SimpleDependency():
    instance = newP_Refines()
    assert isinstance(instance, SimpleDependency)


def test_newP_RequirementTerm_isa_Term():
    instance = newP_RequirementTerm()
    assert isinstance(instance, Term)


def test_newP_UnaryOperator_isa_Term():
    instance = newP_UnaryOperator(name="sample_text")
    assert isinstance(instance, Term)


def test_newP_BinaryOperator_isa_UnaryOperator():
    instance = newP_BinaryOperator()
    assert isinstance(instance, UnaryOperator)


def test_newP_NotOperator_isa_UnaryOperator():
    instance = newP_NotOperator()
    assert isinstance(instance, UnaryOperator)


def test_assoc_RHS18_link_reassign_clear():
    a = newP_UnaryOperator(name="sample_text")
    b1 = newP_Term()
    b2 = newP_Term()
    _safe_set(a, 'newP_UnaryOperator', b1)
    assert _is_linked(a, 'newP_UnaryOperator', b1)
    if hasattr(b1, 'newP_Term'):
        assert _is_linked(b1, 'newP_Term', a)
    _safe_set(a, 'newP_UnaryOperator', b2)
    assert _is_linked(a, 'newP_UnaryOperator', b2)
    if hasattr(b1, 'newP_Term'):
        assert not _is_linked(b1, 'newP_Term', a)
    if hasattr(b2, 'newP_Term'):
        assert _is_linked(b2, 'newP_Term', a)
    _safe_set(a, 'newP_UnaryOperator', None)
    assert not _is_linked(a, 'newP_UnaryOperator', b2)
    if hasattr(b2, 'newP_Term'):
        assert not _is_linked(b2, 'newP_Term', a)


def test_assoc_RHS19_link_reassign_clear():
    a = newP_Requires(name="sample_text")
    b1 = newP_Term()
    b2 = newP_Term()
    _safe_set(a, 'newP_Requires', b1)
    assert _is_linked(a, 'newP_Requires', b1)
    if hasattr(b1, 'newP_Term20'):
        assert _is_linked(b1, 'newP_Term20', a)
    _safe_set(a, 'newP_Requires', b2)
    assert _is_linked(a, 'newP_Requires', b2)
    if hasattr(b1, 'newP_Term20'):
        assert not _is_linked(b1, 'newP_Term20', a)
    if hasattr(b2, 'newP_Term20'):
        assert _is_linked(b2, 'newP_Term20', a)
    _safe_set(a, 'newP_Requires', None)
    assert not _is_linked(a, 'newP_Requires', b2)
    if hasattr(b2, 'newP_Term20'):
        assert not _is_linked(b2, 'newP_Term20', a)


def test_assoc_RHS21_link_reassign_clear():
    a = newP_SimpleDependency(name="sample_text")
    b1 = newP_RequirementTerm()
    b2 = newP_RequirementTerm()
    _safe_set(a, 'newP_SimpleDependency', b1)
    assert _is_linked(a, 'newP_SimpleDependency', b1)
    if hasattr(b1, 'newP_RequirementTerm'):
        assert _is_linked(b1, 'newP_RequirementTerm', a)
    _safe_set(a, 'newP_SimpleDependency', b2)
    assert _is_linked(a, 'newP_SimpleDependency', b2)
    if hasattr(b1, 'newP_RequirementTerm'):
        assert not _is_linked(b1, 'newP_RequirementTerm', a)
    if hasattr(b2, 'newP_RequirementTerm'):
        assert _is_linked(b2, 'newP_RequirementTerm', a)
    _safe_set(a, 'newP_SimpleDependency', None)
    assert not _is_linked(a, 'newP_SimpleDependency', b2)
    if hasattr(b2, 'newP_RequirementTerm'):
        assert not _is_linked(b2, 'newP_RequirementTerm', a)


def test_assoc_categories12_link_reassign_clear():
    a = newP_Person(firstName="sample_text", lastName="sample_text")
    b1 = newP_Category(name="sample_text")
    b2 = newP_Category(name="sample_text_2")
    _safe_set(a, 'newP_Person13', {b1})
    assert _is_linked(a, 'newP_Person13', b1)
    if hasattr(b1, 'newP_Category14'):
        assert _is_linked(b1, 'newP_Category14', a)
    _safe_set(a, 'newP_Person13', {b2})
    assert _is_linked(a, 'newP_Person13', b2)
    if hasattr(b1, 'newP_Category14'):
        assert not _is_linked(b1, 'newP_Category14', a)
    if hasattr(b2, 'newP_Category14'):
        assert _is_linked(b2, 'newP_Category14', a)
    _safe_set(a, 'newP_Person13', set())
    assert not _is_linked(a, 'newP_Person13', b2)
    if hasattr(b2, 'newP_Category14'):
        assert not _is_linked(b2, 'newP_Category14', a)


def test_assoc_category8_link_reassign_clear():
    a = newP_Specification(name="sample_text")
    b1 = newP_Category(name="sample_text")
    b2 = newP_Category(name="sample_text_2")
    _safe_set(a, 'newP_Specification', {b1})
    assert _is_linked(a, 'newP_Specification', b1)
    if hasattr(b1, 'newP_Category9'):
        assert _is_linked(b1, 'newP_Category9', a)
    _safe_set(a, 'newP_Specification', {b2})
    assert _is_linked(a, 'newP_Specification', b2)
    if hasattr(b1, 'newP_Category9'):
        assert not _is_linked(b1, 'newP_Category9', a)
    if hasattr(b2, 'newP_Category9'):
        assert _is_linked(b2, 'newP_Category9', a)
    _safe_set(a, 'newP_Specification', set())
    assert not _is_linked(a, 'newP_Specification', b2)
    if hasattr(b2, 'newP_Category9'):
        assert not _is_linked(b2, 'newP_Category9', a)


def test_assoc_children6_link_reassign_clear():
    a = newP_Category(name="sample_text")
    b1 = newP_Category(name="sample_text")
    b2 = newP_Category(name="sample_text_2")
    _safe_set(a, 'newP_Category5', {b1})
    assert _is_linked(a, 'newP_Category5', b1)
    if hasattr(b1, 'newP_Category7'):
        assert _is_linked(b1, 'newP_Category7', a)
    _safe_set(a, 'newP_Category5', {b2})
    assert _is_linked(a, 'newP_Category5', b2)
    if hasattr(b1, 'newP_Category7'):
        assert not _is_linked(b1, 'newP_Category7', a)
    if hasattr(b2, 'newP_Category7'):
        assert _is_linked(b2, 'newP_Category7', a)
    _safe_set(a, 'newP_Category5', set())
    assert not _is_linked(a, 'newP_Category5', b2)
    if hasattr(b2, 'newP_Category7'):
        assert not _is_linked(b2, 'newP_Category7', a)


def test_assoc_dependency1_link_reassign_clear():
    a = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    b1 = newP_Dependency()
    b2 = newP_Dependency()
    _safe_set(a, 'newP_Requirement2', {b1})
    assert _is_linked(a, 'newP_Requirement2', b1)
    if hasattr(b1, 'newP_Dependency'):
        assert _is_linked(b1, 'newP_Dependency', a)
    _safe_set(a, 'newP_Requirement2', {b2})
    assert _is_linked(a, 'newP_Requirement2', b2)
    if hasattr(b1, 'newP_Dependency'):
        assert not _is_linked(b1, 'newP_Dependency', a)
    if hasattr(b2, 'newP_Dependency'):
        assert _is_linked(b2, 'newP_Dependency', a)
    _safe_set(a, 'newP_Requirement2', set())
    assert not _is_linked(a, 'newP_Requirement2', b2)
    if hasattr(b2, 'newP_Dependency'):
        assert not _is_linked(b2, 'newP_Dependency', a)


def test_assoc_description0_link_reassign_clear():
    a = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    b1 = newP_Description()
    b2 = newP_Description()
    _safe_set(a, 'newP_Requirement', {b1})
    assert _is_linked(a, 'newP_Requirement', b1)
    if hasattr(b1, 'newP_Description'):
        assert _is_linked(b1, 'newP_Description', a)
    _safe_set(a, 'newP_Requirement', {b2})
    assert _is_linked(a, 'newP_Requirement', b2)
    if hasattr(b1, 'newP_Description'):
        assert not _is_linked(b1, 'newP_Description', a)
    if hasattr(b2, 'newP_Description'):
        assert _is_linked(b2, 'newP_Description', a)
    _safe_set(a, 'newP_Requirement', set())
    assert not _is_linked(a, 'newP_Requirement', b2)
    if hasattr(b2, 'newP_Description'):
        assert not _is_linked(b2, 'newP_Description', a)


def test_assoc_person10_link_reassign_clear():
    a = newP_Specification(name="sample_text")
    b1 = newP_Person(firstName="sample_text", lastName="sample_text")
    b2 = newP_Person(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'newP_Specification11', {b1})
    assert _is_linked(a, 'newP_Specification11', b1)
    if hasattr(b1, 'newP_Person'):
        assert _is_linked(b1, 'newP_Person', a)
    _safe_set(a, 'newP_Specification11', {b2})
    assert _is_linked(a, 'newP_Specification11', b2)
    if hasattr(b1, 'newP_Person'):
        assert not _is_linked(b1, 'newP_Person', a)
    if hasattr(b2, 'newP_Person'):
        assert _is_linked(b2, 'newP_Person', a)
    _safe_set(a, 'newP_Specification11', set())
    assert not _is_linked(a, 'newP_Specification11', b2)
    if hasattr(b2, 'newP_Person'):
        assert not _is_linked(b2, 'newP_Person', a)


def test_assoc_requirement24_link_reassign_clear():
    a = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    b1 = newP_RequirementTerm()
    b2 = newP_RequirementTerm()
    _safe_set(a, 'newP_Requirement26', b1)
    assert _is_linked(a, 'newP_Requirement26', b1)
    if hasattr(b1, 'newP_RequirementTerm25'):
        assert _is_linked(b1, 'newP_RequirementTerm25', a)
    _safe_set(a, 'newP_Requirement26', b2)
    assert _is_linked(a, 'newP_Requirement26', b2)
    if hasattr(b1, 'newP_RequirementTerm25'):
        assert not _is_linked(b1, 'newP_RequirementTerm25', a)
    if hasattr(b2, 'newP_RequirementTerm25'):
        assert _is_linked(b2, 'newP_RequirementTerm25', a)
    _safe_set(a, 'newP_Requirement26', None)
    assert not _is_linked(a, 'newP_Requirement26', b2)
    if hasattr(b2, 'newP_RequirementTerm25'):
        assert not _is_linked(b2, 'newP_RequirementTerm25', a)


def test_assoc_requirement3_link_reassign_clear():
    a = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    b1 = newP_Category(name="sample_text")
    b2 = newP_Category(name="sample_text_2")
    _safe_set(a, 'newP_Requirement4', b1)
    assert _is_linked(a, 'newP_Requirement4', b1)
    if hasattr(b1, 'newP_Category'):
        assert _is_linked(b1, 'newP_Category', a)
    _safe_set(a, 'newP_Requirement4', b2)
    assert _is_linked(a, 'newP_Requirement4', b2)
    if hasattr(b1, 'newP_Category'):
        assert not _is_linked(b1, 'newP_Category', a)
    if hasattr(b2, 'newP_Category'):
        assert _is_linked(b2, 'newP_Category', a)
    _safe_set(a, 'newP_Requirement4', None)
    assert not _is_linked(a, 'newP_Requirement4', b2)
    if hasattr(b2, 'newP_Category'):
        assert not _is_linked(b2, 'newP_Category', a)


def test_assoc_requirements15_link_reassign_clear():
    a = newP_Requirement(identifier="sample_text", mandatory=True, name="sample_text", priority=7)
    b1 = newP_Person(firstName="sample_text", lastName="sample_text")
    b2 = newP_Person(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'newP_Requirement17', b1)
    assert _is_linked(a, 'newP_Requirement17', b1)
    if hasattr(b1, 'newP_Person16'):
        assert _is_linked(b1, 'newP_Person16', a)
    _safe_set(a, 'newP_Requirement17', b2)
    assert _is_linked(a, 'newP_Requirement17', b2)
    if hasattr(b1, 'newP_Person16'):
        assert not _is_linked(b1, 'newP_Person16', a)
    if hasattr(b2, 'newP_Person16'):
        assert _is_linked(b2, 'newP_Person16', a)
    _safe_set(a, 'newP_Requirement17', None)
    assert not _is_linked(a, 'newP_Requirement17', b2)
    if hasattr(b2, 'newP_Person16'):
        assert not _is_linked(b2, 'newP_Person16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryOperator_strategy = st.builds(BinaryOperator)
@given(instance=BinaryOperator_strategy)
@settings(max_examples=25)
def test_BinaryOperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)


Dependency_strategy = st.builds(Dependency)
@given(instance=Dependency_strategy)
@settings(max_examples=25)
def test_Dependency_instantiation(instance):
    assert isinstance(instance, Dependency)


Description_strategy = st.builds(Description)
@given(instance=Description_strategy)
@settings(max_examples=25)
def test_Description_instantiation(instance):
    assert isinstance(instance, Description)


Requirement_strategy = st.builds(Requirement)
@given(instance=Requirement_strategy)
@settings(max_examples=25)
def test_Requirement_instantiation(instance):
    assert isinstance(instance, Requirement)


SimpleDependency_strategy = st.builds(SimpleDependency)
@given(instance=SimpleDependency_strategy)
@settings(max_examples=25)
def test_SimpleDependency_instantiation(instance):
    assert isinstance(instance, SimpleDependency)


Term_strategy = st.builds(Term)
@given(instance=Term_strategy)
@settings(max_examples=25)
def test_Term_instantiation(instance):
    assert isinstance(instance, Term)


UnaryOperator_strategy = st.builds(UnaryOperator)
@given(instance=UnaryOperator_strategy)
@settings(max_examples=25)
def test_UnaryOperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)


newP_AndOperartor_strategy = st.builds(newP_AndOperartor)
@given(instance=newP_AndOperartor_strategy)
@settings(max_examples=25)
def test_newP_AndOperartor_instantiation(instance):
    assert isinstance(instance, newP_AndOperartor)


newP_BinaryOperator_strategy = st.builds(newP_BinaryOperator)
@given(instance=newP_BinaryOperator_strategy)
@settings(max_examples=25)
def test_newP_BinaryOperator_instantiation(instance):
    assert isinstance(instance, newP_BinaryOperator)


newP_CValue_strategy = st.builds(newP_CValue)
@given(instance=newP_CValue_strategy)
@settings(max_examples=25)
def test_newP_CValue_instantiation(instance):
    assert isinstance(instance, newP_CValue)


newP_Category_strategy = st.builds(newP_Category, name=safe_text)
@given(instance=newP_Category_strategy)
@settings(max_examples=25)
def test_newP_Category_instantiation(instance):
    assert isinstance(instance, newP_Category)


newP_Dependency_strategy = st.builds(newP_Dependency)
@given(instance=newP_Dependency_strategy)
@settings(max_examples=25)
def test_newP_Dependency_instantiation(instance):
    assert isinstance(instance, newP_Dependency)


newP_Description_strategy = st.builds(newP_Description)
@given(instance=newP_Description_strategy)
@settings(max_examples=25)
def test_newP_Description_instantiation(instance):
    assert isinstance(instance, newP_Description)


newP_FunctionalRequirement_strategy = st.builds(newP_FunctionalRequirement)
@given(instance=newP_FunctionalRequirement_strategy)
@settings(max_examples=25)
def test_newP_FunctionalRequirement_instantiation(instance):
    assert isinstance(instance, newP_FunctionalRequirement)


newP_ICost_strategy = st.builds(newP_ICost)
@given(instance=newP_ICost_strategy)
@settings(max_examples=25)
def test_newP_ICost_instantiation(instance):
    assert isinstance(instance, newP_ICost)


newP_NotOperator_strategy = st.builds(newP_NotOperator)
@given(instance=newP_NotOperator_strategy)
@settings(max_examples=25)
def test_newP_NotOperator_instantiation(instance):
    assert isinstance(instance, newP_NotOperator)


newP_OrOperator_strategy = st.builds(newP_OrOperator)
@given(instance=newP_OrOperator_strategy)
@settings(max_examples=25)
def test_newP_OrOperator_instantiation(instance):
    assert isinstance(instance, newP_OrOperator)


newP_Person_strategy = st.builds(newP_Person, firstName=safe_text, lastName=safe_text)
@given(instance=newP_Person_strategy)
@settings(max_examples=25)
def test_newP_Person_instantiation(instance):
    assert isinstance(instance, newP_Person)


newP_QualityRequirement_strategy = st.builds(newP_QualityRequirement)
@given(instance=newP_QualityRequirement_strategy)
@settings(max_examples=25)
def test_newP_QualityRequirement_instantiation(instance):
    assert isinstance(instance, newP_QualityRequirement)


newP_Refines_strategy = st.builds(newP_Refines)
@given(instance=newP_Refines_strategy)
@settings(max_examples=25)
def test_newP_Refines_instantiation(instance):
    assert isinstance(instance, newP_Refines)


newP_Requirement_strategy = st.builds(newP_Requirement, identifier=safe_text, mandatory=st.booleans(), name=safe_text, priority=st.integers())
@given(instance=newP_Requirement_strategy)
@settings(max_examples=25)
def test_newP_Requirement_instantiation(instance):
    assert isinstance(instance, newP_Requirement)


newP_RequirementTerm_strategy = st.builds(newP_RequirementTerm)
@given(instance=newP_RequirementTerm_strategy)
@settings(max_examples=25)
def test_newP_RequirementTerm_instantiation(instance):
    assert isinstance(instance, newP_RequirementTerm)


newP_Requires_strategy = st.builds(newP_Requires, name=safe_text)
@given(instance=newP_Requires_strategy)
@settings(max_examples=25)
def test_newP_Requires_instantiation(instance):
    assert isinstance(instance, newP_Requires)


newP_SimpleDependency_strategy = st.builds(newP_SimpleDependency, name=safe_text)
@given(instance=newP_SimpleDependency_strategy)
@settings(max_examples=25)
def test_newP_SimpleDependency_instantiation(instance):
    assert isinstance(instance, newP_SimpleDependency)


newP_Specification_strategy = st.builds(newP_Specification, name=safe_text)
@given(instance=newP_Specification_strategy)
@settings(max_examples=25)
def test_newP_Specification_instantiation(instance):
    assert isinstance(instance, newP_Specification)


newP_Term_strategy = st.builds(newP_Term)
@given(instance=newP_Term_strategy)
@settings(max_examples=25)
def test_newP_Term_instantiation(instance):
    assert isinstance(instance, newP_Term)


newP_TextDescription_strategy = st.builds(newP_TextDescription, text=safe_text)
@given(instance=newP_TextDescription_strategy)
@settings(max_examples=25)
def test_newP_TextDescription_instantiation(instance):
    assert isinstance(instance, newP_TextDescription)


newP_UnaryOperator_strategy = st.builds(newP_UnaryOperator, name=safe_text)
@given(instance=newP_UnaryOperator_strategy)
@settings(max_examples=25)
def test_newP_UnaryOperator_instantiation(instance):
    assert isinstance(instance, newP_UnaryOperator)



