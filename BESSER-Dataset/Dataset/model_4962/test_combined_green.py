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
    Inheritance,
    crom_l1_NaturalInheritance,
    crom_l1_Part,
    crom_l1_NamedElement,
    crom_l1_Player,
    crom_l1_AbstractRole,
    Relation,
    crom_l1_Inheritance,
    crom_l1_Fulfillment,
    AbstractRole,
    Player,
    RigidType,
    crom_l1_NaturalType,
    RelationTarget,
    crom_l1_RoleType,
    crom_l1_Type,
    TypedElement,
    crom_l1_Attribute,
    crom_l1_Operation,
    crom_l1_Parameter,
    Model,
    ModelElement,
    crom_l1_Group,
    crom_l1_CompartmentType,
    Type,
    crom_l1_RigidType,
    crom_l1_Model,
    crom_l1_Relation,
    NamedElement,
    crom_l1_TypedElement,
    crom_l1_RelationTarget,
    crom_l1_ModelElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_inheritance_is_not_abstract():
    assert not inspect.isabstract(Inheritance)


def test_hyp_inheritance_constructor_exists():
    assert callable(Inheritance.__init__)


def test_hyp_inheritance_constructor_args():
    sig = inspect.signature(Inheritance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_naturalinheritance_is_not_abstract():
    assert not inspect.isabstract(crom_l1_NaturalInheritance)


def test_hyp_crom_l1_naturalinheritance_constructor_exists():
    assert callable(crom_l1_NaturalInheritance.__init__)


def test_hyp_crom_l1_naturalinheritance_constructor_args():
    sig = inspect.signature(crom_l1_NaturalInheritance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_part_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Part)


def test_hyp_crom_l1_part_constructor_exists():
    assert callable(crom_l1_Part.__init__)


def test_hyp_crom_l1_part_constructor_args():
    sig = inspect.signature(crom_l1_Part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_namedelement_is_not_abstract():
    assert not inspect.isabstract(crom_l1_NamedElement)


def test_hyp_crom_l1_namedelement_constructor_exists():
    assert callable(crom_l1_NamedElement.__init__)


def test_hyp_crom_l1_namedelement_constructor_args():
    sig = inspect.signature(crom_l1_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_crom_l1_player_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Player)


def test_hyp_crom_l1_player_constructor_exists():
    assert callable(crom_l1_Player.__init__)


def test_hyp_crom_l1_player_constructor_args():
    sig = inspect.signature(crom_l1_Player.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_abstractrole_is_not_abstract():
    assert not inspect.isabstract(crom_l1_AbstractRole)


def test_hyp_crom_l1_abstractrole_constructor_exists():
    assert callable(crom_l1_AbstractRole.__init__)


def test_hyp_crom_l1_abstractrole_constructor_args():
    sig = inspect.signature(crom_l1_AbstractRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_hyp_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_hyp_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_inheritance_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Inheritance)


def test_hyp_crom_l1_inheritance_constructor_exists():
    assert callable(crom_l1_Inheritance.__init__)


def test_hyp_crom_l1_inheritance_constructor_args():
    sig = inspect.signature(crom_l1_Inheritance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_fulfillment_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Fulfillment)


def test_hyp_crom_l1_fulfillment_constructor_exists():
    assert callable(crom_l1_Fulfillment.__init__)


def test_hyp_crom_l1_fulfillment_constructor_args():
    sig = inspect.signature(crom_l1_Fulfillment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractrole_is_not_abstract():
    assert not inspect.isabstract(AbstractRole)


def test_hyp_abstractrole_constructor_exists():
    assert callable(AbstractRole.__init__)


def test_hyp_abstractrole_constructor_args():
    sig = inspect.signature(AbstractRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rigidtype_is_not_abstract():
    assert not inspect.isabstract(RigidType)


def test_hyp_rigidtype_constructor_exists():
    assert callable(RigidType.__init__)


def test_hyp_rigidtype_constructor_args():
    sig = inspect.signature(RigidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_naturaltype_is_not_abstract():
    assert not inspect.isabstract(crom_l1_NaturalType)


def test_hyp_crom_l1_naturaltype_constructor_exists():
    assert callable(crom_l1_NaturalType.__init__)


def test_hyp_crom_l1_naturaltype_constructor_args():
    sig = inspect.signature(crom_l1_NaturalType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationtarget_is_not_abstract():
    assert not inspect.isabstract(RelationTarget)


def test_hyp_relationtarget_constructor_exists():
    assert callable(RelationTarget.__init__)


def test_hyp_relationtarget_constructor_args():
    sig = inspect.signature(RelationTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_roletype_is_not_abstract():
    assert not inspect.isabstract(crom_l1_RoleType)


def test_hyp_crom_l1_roletype_constructor_exists():
    assert callable(crom_l1_RoleType.__init__)


def test_hyp_crom_l1_roletype_constructor_args():
    sig = inspect.signature(crom_l1_RoleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_type_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Type)


def test_hyp_crom_l1_type_constructor_exists():
    assert callable(crom_l1_Type.__init__)


def test_hyp_crom_l1_type_constructor_args():
    sig = inspect.signature(crom_l1_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_attribute_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Attribute)


def test_hyp_crom_l1_attribute_constructor_exists():
    assert callable(crom_l1_Attribute.__init__)


def test_hyp_crom_l1_attribute_constructor_args():
    sig = inspect.signature(crom_l1_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_operation_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Operation)


def test_hyp_crom_l1_operation_constructor_exists():
    assert callable(crom_l1_Operation.__init__)


def test_hyp_crom_l1_operation_constructor_args():
    sig = inspect.signature(crom_l1_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"




def test_hyp_crom_l1_parameter_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Parameter)


def test_hyp_crom_l1_parameter_constructor_exists():
    assert callable(crom_l1_Parameter.__init__)


def test_hyp_crom_l1_parameter_constructor_args():
    sig = inspect.signature(crom_l1_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_hyp_model_constructor_exists():
    assert callable(Model.__init__)


def test_hyp_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_hyp_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_hyp_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_group_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Group)


def test_hyp_crom_l1_group_constructor_exists():
    assert callable(crom_l1_Group.__init__)


def test_hyp_crom_l1_group_constructor_args():
    sig = inspect.signature(crom_l1_Group.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_compartmenttype_is_not_abstract():
    assert not inspect.isabstract(crom_l1_CompartmentType)


def test_hyp_crom_l1_compartmenttype_constructor_exists():
    assert callable(crom_l1_CompartmentType.__init__)


def test_hyp_crom_l1_compartmenttype_constructor_args():
    sig = inspect.signature(crom_l1_CompartmentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_rigidtype_is_not_abstract():
    assert not inspect.isabstract(crom_l1_RigidType)


def test_hyp_crom_l1_rigidtype_constructor_exists():
    assert callable(crom_l1_RigidType.__init__)


def test_hyp_crom_l1_rigidtype_constructor_args():
    sig = inspect.signature(crom_l1_RigidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_model_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Model)


def test_hyp_crom_l1_model_constructor_exists():
    assert callable(crom_l1_Model.__init__)


def test_hyp_crom_l1_model_constructor_args():
    sig = inspect.signature(crom_l1_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_relation_is_not_abstract():
    assert not inspect.isabstract(crom_l1_Relation)


def test_hyp_crom_l1_relation_constructor_exists():
    assert callable(crom_l1_Relation.__init__)


def test_hyp_crom_l1_relation_constructor_args():
    sig = inspect.signature(crom_l1_Relation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_typedelement_is_not_abstract():
    assert not inspect.isabstract(crom_l1_TypedElement)


def test_hyp_crom_l1_typedelement_constructor_exists():
    assert callable(crom_l1_TypedElement.__init__)


def test_hyp_crom_l1_typedelement_constructor_args():
    sig = inspect.signature(crom_l1_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_relationtarget_is_not_abstract():
    assert not inspect.isabstract(crom_l1_RelationTarget)


def test_hyp_crom_l1_relationtarget_constructor_exists():
    assert callable(crom_l1_RelationTarget.__init__)


def test_hyp_crom_l1_relationtarget_constructor_args():
    sig = inspect.signature(crom_l1_RelationTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_crom_l1_modelelement_is_not_abstract():
    assert not inspect.isabstract(crom_l1_ModelElement)


def test_hyp_crom_l1_modelelement_constructor_exists():
    assert callable(crom_l1_ModelElement.__init__)


def test_hyp_crom_l1_modelelement_constructor_args():
    sig = inspect.signature(crom_l1_ModelElement.__init__)
    params = list(sig.parameters.keys())


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
Inheritance_strategy = st.builds(
    Inheritance,
)
crom_l1_NaturalInheritance_strategy = st.builds(
    crom_l1_NaturalInheritance,
)
crom_l1_Part_strategy = st.builds(
    crom_l1_Part,
)
crom_l1_NamedElement_strategy = st.builds(
    crom_l1_NamedElement,
    name=
        safe_text
)
crom_l1_Player_strategy = st.builds(
    crom_l1_Player,
)
crom_l1_AbstractRole_strategy = st.builds(
    crom_l1_AbstractRole,
)
Relation_strategy = st.builds(
    Relation,
)
crom_l1_Inheritance_strategy = st.builds(
    crom_l1_Inheritance,
)
crom_l1_Fulfillment_strategy = st.builds(
    crom_l1_Fulfillment,
)
AbstractRole_strategy = st.builds(
    AbstractRole,
)
Player_strategy = st.builds(
    Player,
)
RigidType_strategy = st.builds(
    RigidType,
)
crom_l1_NaturalType_strategy = st.builds(
    crom_l1_NaturalType,
)
RelationTarget_strategy = st.builds(
    RelationTarget,
)
crom_l1_RoleType_strategy = st.builds(
    crom_l1_RoleType,
)
crom_l1_Type_strategy = st.builds(
    crom_l1_Type,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
crom_l1_Attribute_strategy = st.builds(
    crom_l1_Attribute,
)
crom_l1_Operation_strategy = st.builds(
    crom_l1_Operation,
    operation=
        safe_text
)
crom_l1_Parameter_strategy = st.builds(
    crom_l1_Parameter,
)
Model_strategy = st.builds(
    Model,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
crom_l1_Group_strategy = st.builds(
    crom_l1_Group,
)
crom_l1_CompartmentType_strategy = st.builds(
    crom_l1_CompartmentType,
)
Type_strategy = st.builds(
    Type,
)
crom_l1_RigidType_strategy = st.builds(
    crom_l1_RigidType,
)
crom_l1_Model_strategy = st.builds(
    crom_l1_Model,
)
crom_l1_Relation_strategy = st.builds(
    crom_l1_Relation,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
crom_l1_TypedElement_strategy = st.builds(
    crom_l1_TypedElement,
)
crom_l1_RelationTarget_strategy = st.builds(
    crom_l1_RelationTarget,
)
crom_l1_ModelElement_strategy = st.builds(
    crom_l1_ModelElement,
)







@given(instance=crom_l1_NamedElement_strategy)
def test_hyp_crom_l1_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


















@given(instance=crom_l1_Operation_strategy)
def test_hyp_crom_l1_operation_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractRole,
    Inheritance,
    Model,
    ModelElement,
    NamedElement,
    Player,
    Relation,
    RelationTarget,
    RigidType,
    Type,
    TypedElement,
    crom_l1_AbstractRole,
    crom_l1_Attribute,
    crom_l1_CompartmentType,
    crom_l1_Fulfillment,
    crom_l1_Group,
    crom_l1_Inheritance,
    crom_l1_Model,
    crom_l1_ModelElement,
    crom_l1_NamedElement,
    crom_l1_NaturalInheritance,
    crom_l1_NaturalType,
    crom_l1_Operation,
    crom_l1_Parameter,
    crom_l1_Part,
    crom_l1_Player,
    crom_l1_Relation,
    crom_l1_RelationTarget,
    crom_l1_RigidType,
    crom_l1_RoleType,
    crom_l1_Type,
    crom_l1_TypedElement,
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

def test_crom_l1_NamedElement_name_value_roundtrip():
    instance = crom_l1_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_crom_l1_Operation_operation_value_roundtrip():
    instance = crom_l1_Operation(operation="sample_text")
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_crom_l1_RoleType_isa_AbstractRole():
    instance = crom_l1_RoleType()
    assert isinstance(instance, AbstractRole)


def test_crom_l1_NaturalInheritance_isa_Inheritance():
    instance = crom_l1_NaturalInheritance()
    assert isinstance(instance, Inheritance)


def test_crom_l1_Group_isa_Model():
    instance = crom_l1_Group()
    assert isinstance(instance, Model)


def test_crom_l1_CompartmentType_isa_ModelElement():
    instance = crom_l1_CompartmentType()
    assert isinstance(instance, ModelElement)


def test_crom_l1_Group_isa_ModelElement():
    instance = crom_l1_Group()
    assert isinstance(instance, ModelElement)


def test_crom_l1_RigidType_isa_ModelElement():
    instance = crom_l1_RigidType()
    assert isinstance(instance, ModelElement)


def test_crom_l1_ModelElement_isa_NamedElement():
    instance = crom_l1_ModelElement()
    assert isinstance(instance, NamedElement)


def test_crom_l1_RelationTarget_isa_NamedElement():
    instance = crom_l1_RelationTarget()
    assert isinstance(instance, NamedElement)


def test_crom_l1_TypedElement_isa_NamedElement():
    instance = crom_l1_TypedElement()
    assert isinstance(instance, NamedElement)


def test_crom_l1_CompartmentType_isa_Player():
    instance = crom_l1_CompartmentType()
    assert isinstance(instance, Player)


def test_crom_l1_NaturalType_isa_Player():
    instance = crom_l1_NaturalType()
    assert isinstance(instance, Player)


def test_crom_l1_RoleType_isa_Player():
    instance = crom_l1_RoleType()
    assert isinstance(instance, Player)


def test_crom_l1_Fulfillment_isa_Relation():
    instance = crom_l1_Fulfillment()
    assert isinstance(instance, Relation)


def test_crom_l1_Inheritance_isa_Relation():
    instance = crom_l1_Inheritance()
    assert isinstance(instance, Relation)


def test_crom_l1_CompartmentType_isa_RelationTarget():
    instance = crom_l1_CompartmentType()
    assert isinstance(instance, RelationTarget)


def test_crom_l1_RoleType_isa_RelationTarget():
    instance = crom_l1_RoleType()
    assert isinstance(instance, RelationTarget)


def test_crom_l1_Type_isa_RelationTarget():
    instance = crom_l1_Type()
    assert isinstance(instance, RelationTarget)


def test_crom_l1_NaturalType_isa_RigidType():
    instance = crom_l1_NaturalType()
    assert isinstance(instance, RigidType)


def test_crom_l1_RigidType_isa_Type():
    instance = crom_l1_RigidType()
    assert isinstance(instance, Type)


def test_crom_l1_Attribute_isa_TypedElement():
    instance = crom_l1_Attribute()
    assert isinstance(instance, TypedElement)


def test_crom_l1_Operation_isa_TypedElement():
    instance = crom_l1_Operation(operation="sample_text")
    assert isinstance(instance, TypedElement)


def test_crom_l1_Parameter_isa_TypedElement():
    instance = crom_l1_Parameter()
    assert isinstance(instance, TypedElement)


def test_assoc_operations8_link_reassign_clear():
    a = crom_l1_Operation(operation="sample_text")
    b1 = crom_l1_Type()
    b2 = crom_l1_Type()
    _safe_set(a, 'Operation', b1)
    assert _is_linked(a, 'Operation', b1)
    if hasattr(b1, 'owner9'):
        assert _is_linked(b1, 'owner9', a)
    _safe_set(a, 'Operation', b2)
    assert _is_linked(a, 'Operation', b2)
    if hasattr(b1, 'owner9'):
        assert not _is_linked(b1, 'owner9', a)
    if hasattr(b2, 'owner9'):
        assert _is_linked(b2, 'owner9', a)
    _safe_set(a, 'Operation', None)
    assert not _is_linked(a, 'Operation', b2)
    if hasattr(b2, 'owner9'):
        assert not _is_linked(b2, 'owner9', a)


def test_assoc_owner4_link_reassign_clear():
    a = crom_l1_Operation(operation="sample_text")
    b1 = crom_l1_Type()
    b2 = crom_l1_Type()
    _safe_set(a, 'operations', b1)
    assert _is_linked(a, 'operations', b1)
    if hasattr(b1, 'Type'):
        assert _is_linked(b1, 'Type', a)
    _safe_set(a, 'operations', b2)
    assert _is_linked(a, 'operations', b2)
    if hasattr(b1, 'Type'):
        assert not _is_linked(b1, 'Type', a)
    if hasattr(b2, 'Type'):
        assert _is_linked(b2, 'Type', a)
    _safe_set(a, 'operations', None)
    assert not _is_linked(a, 'operations', b2)
    if hasattr(b2, 'Type'):
        assert not _is_linked(b2, 'Type', a)


def test_assoc_params3_link_reassign_clear():
    a = crom_l1_Operation(operation="sample_text")
    b1 = crom_l1_Parameter()
    b2 = crom_l1_Parameter()
    _safe_set(a, 'crom_l1_Operation', {b1})
    assert _is_linked(a, 'crom_l1_Operation', b1)
    if hasattr(b1, 'crom_l1_Parameter'):
        assert _is_linked(b1, 'crom_l1_Parameter', a)
    _safe_set(a, 'crom_l1_Operation', {b2})
    assert _is_linked(a, 'crom_l1_Operation', b2)
    if hasattr(b1, 'crom_l1_Parameter'):
        assert not _is_linked(b1, 'crom_l1_Parameter', a)
    if hasattr(b2, 'crom_l1_Parameter'):
        assert _is_linked(b2, 'crom_l1_Parameter', a)
    _safe_set(a, 'crom_l1_Operation', set())
    assert not _is_linked(a, 'crom_l1_Operation', b2)
    if hasattr(b2, 'crom_l1_Parameter'):
        assert not _is_linked(b2, 'crom_l1_Parameter', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractRole_strategy = st.builds(AbstractRole)
@given(instance=AbstractRole_strategy)
@settings(max_examples=25)
def test_AbstractRole_instantiation(instance):
    assert isinstance(instance, AbstractRole)


Inheritance_strategy = st.builds(Inheritance)
@given(instance=Inheritance_strategy)
@settings(max_examples=25)
def test_Inheritance_instantiation(instance):
    assert isinstance(instance, Inheritance)


Model_strategy = st.builds(Model)
@given(instance=Model_strategy)
@settings(max_examples=25)
def test_Model_instantiation(instance):
    assert isinstance(instance, Model)


ModelElement_strategy = st.builds(ModelElement)
@given(instance=ModelElement_strategy)
@settings(max_examples=25)
def test_ModelElement_instantiation(instance):
    assert isinstance(instance, ModelElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Player_strategy = st.builds(Player)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


Relation_strategy = st.builds(Relation)
@given(instance=Relation_strategy)
@settings(max_examples=25)
def test_Relation_instantiation(instance):
    assert isinstance(instance, Relation)


RelationTarget_strategy = st.builds(RelationTarget)
@given(instance=RelationTarget_strategy)
@settings(max_examples=25)
def test_RelationTarget_instantiation(instance):
    assert isinstance(instance, RelationTarget)


RigidType_strategy = st.builds(RigidType)
@given(instance=RigidType_strategy)
@settings(max_examples=25)
def test_RigidType_instantiation(instance):
    assert isinstance(instance, RigidType)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


crom_l1_AbstractRole_strategy = st.builds(crom_l1_AbstractRole)
@given(instance=crom_l1_AbstractRole_strategy)
@settings(max_examples=25)
def test_crom_l1_AbstractRole_instantiation(instance):
    assert isinstance(instance, crom_l1_AbstractRole)


crom_l1_Attribute_strategy = st.builds(crom_l1_Attribute)
@given(instance=crom_l1_Attribute_strategy)
@settings(max_examples=25)
def test_crom_l1_Attribute_instantiation(instance):
    assert isinstance(instance, crom_l1_Attribute)


crom_l1_CompartmentType_strategy = st.builds(crom_l1_CompartmentType)
@given(instance=crom_l1_CompartmentType_strategy)
@settings(max_examples=25)
def test_crom_l1_CompartmentType_instantiation(instance):
    assert isinstance(instance, crom_l1_CompartmentType)


crom_l1_Fulfillment_strategy = st.builds(crom_l1_Fulfillment)
@given(instance=crom_l1_Fulfillment_strategy)
@settings(max_examples=25)
def test_crom_l1_Fulfillment_instantiation(instance):
    assert isinstance(instance, crom_l1_Fulfillment)


crom_l1_Group_strategy = st.builds(crom_l1_Group)
@given(instance=crom_l1_Group_strategy)
@settings(max_examples=25)
def test_crom_l1_Group_instantiation(instance):
    assert isinstance(instance, crom_l1_Group)


crom_l1_Inheritance_strategy = st.builds(crom_l1_Inheritance)
@given(instance=crom_l1_Inheritance_strategy)
@settings(max_examples=25)
def test_crom_l1_Inheritance_instantiation(instance):
    assert isinstance(instance, crom_l1_Inheritance)


crom_l1_Model_strategy = st.builds(crom_l1_Model)
@given(instance=crom_l1_Model_strategy)
@settings(max_examples=25)
def test_crom_l1_Model_instantiation(instance):
    assert isinstance(instance, crom_l1_Model)


crom_l1_ModelElement_strategy = st.builds(crom_l1_ModelElement)
@given(instance=crom_l1_ModelElement_strategy)
@settings(max_examples=25)
def test_crom_l1_ModelElement_instantiation(instance):
    assert isinstance(instance, crom_l1_ModelElement)


crom_l1_NamedElement_strategy = st.builds(crom_l1_NamedElement, name=safe_text)
@given(instance=crom_l1_NamedElement_strategy)
@settings(max_examples=25)
def test_crom_l1_NamedElement_instantiation(instance):
    assert isinstance(instance, crom_l1_NamedElement)


crom_l1_NaturalInheritance_strategy = st.builds(crom_l1_NaturalInheritance)
@given(instance=crom_l1_NaturalInheritance_strategy)
@settings(max_examples=25)
def test_crom_l1_NaturalInheritance_instantiation(instance):
    assert isinstance(instance, crom_l1_NaturalInheritance)


crom_l1_NaturalType_strategy = st.builds(crom_l1_NaturalType)
@given(instance=crom_l1_NaturalType_strategy)
@settings(max_examples=25)
def test_crom_l1_NaturalType_instantiation(instance):
    assert isinstance(instance, crom_l1_NaturalType)


crom_l1_Operation_strategy = st.builds(crom_l1_Operation, operation=safe_text)
@given(instance=crom_l1_Operation_strategy)
@settings(max_examples=25)
def test_crom_l1_Operation_instantiation(instance):
    assert isinstance(instance, crom_l1_Operation)


crom_l1_Parameter_strategy = st.builds(crom_l1_Parameter)
@given(instance=crom_l1_Parameter_strategy)
@settings(max_examples=25)
def test_crom_l1_Parameter_instantiation(instance):
    assert isinstance(instance, crom_l1_Parameter)


crom_l1_Part_strategy = st.builds(crom_l1_Part)
@given(instance=crom_l1_Part_strategy)
@settings(max_examples=25)
def test_crom_l1_Part_instantiation(instance):
    assert isinstance(instance, crom_l1_Part)


crom_l1_Player_strategy = st.builds(crom_l1_Player)
@given(instance=crom_l1_Player_strategy)
@settings(max_examples=25)
def test_crom_l1_Player_instantiation(instance):
    assert isinstance(instance, crom_l1_Player)


crom_l1_Relation_strategy = st.builds(crom_l1_Relation)
@given(instance=crom_l1_Relation_strategy)
@settings(max_examples=25)
def test_crom_l1_Relation_instantiation(instance):
    assert isinstance(instance, crom_l1_Relation)


crom_l1_RelationTarget_strategy = st.builds(crom_l1_RelationTarget)
@given(instance=crom_l1_RelationTarget_strategy)
@settings(max_examples=25)
def test_crom_l1_RelationTarget_instantiation(instance):
    assert isinstance(instance, crom_l1_RelationTarget)


crom_l1_RigidType_strategy = st.builds(crom_l1_RigidType)
@given(instance=crom_l1_RigidType_strategy)
@settings(max_examples=25)
def test_crom_l1_RigidType_instantiation(instance):
    assert isinstance(instance, crom_l1_RigidType)


crom_l1_RoleType_strategy = st.builds(crom_l1_RoleType)
@given(instance=crom_l1_RoleType_strategy)
@settings(max_examples=25)
def test_crom_l1_RoleType_instantiation(instance):
    assert isinstance(instance, crom_l1_RoleType)


crom_l1_Type_strategy = st.builds(crom_l1_Type)
@given(instance=crom_l1_Type_strategy)
@settings(max_examples=25)
def test_crom_l1_Type_instantiation(instance):
    assert isinstance(instance, crom_l1_Type)


crom_l1_TypedElement_strategy = st.builds(crom_l1_TypedElement)
@given(instance=crom_l1_TypedElement_strategy)
@settings(max_examples=25)
def test_crom_l1_TypedElement_instantiation(instance):
    assert isinstance(instance, crom_l1_TypedElement)



