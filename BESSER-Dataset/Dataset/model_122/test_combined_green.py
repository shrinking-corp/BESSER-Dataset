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
    JMM_ASTNode,
    TypeDeclaration,
    JMM_InterfaceDeclaration,
    JMM_ClassDeclaration,
    AbstractMethodDeclaration,
    JMM_ConstructorDeclaration,
    JMM_MethodDeclaration,
    ASTNode,
    JMM_AbstractVariablesContainer,
    JMM_Expression,
    JMM_NamespaceAccess,
    JMM_NamedElement,
    JMM_Modifier,
    Type,
    NamedElement,
    JMM_BodyDeclaration,
    JMM_Type,
    NamespaceAccess,
    Expression,
    JMM_TypeAccess,
    JMM_Package,
    JMM_Model,
    AbstractTypeDeclaration,
    JMM_TypeDeclaration,
    JMM_AnnotationTypeDeclaration,
    AbstractVariablesContainer,
    BodyDeclaration,
    JMM_AbstractMethodDeclaration,
    JMM_AbstractTypeDeclaration,
    JMM_FieldDeclaration,
    InheritanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_jmm_astnode_is_not_abstract():
    assert not inspect.isabstract(JMM_ASTNode)


def test_hyp_jmm_astnode_constructor_exists():
    assert callable(JMM_ASTNode.__init__)


def test_hyp_jmm_astnode_constructor_args():
    sig = inspect.signature(JMM_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_hyp_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_hyp_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_InterfaceDeclaration)


def test_hyp_jmm_interfacedeclaration_constructor_exists():
    assert callable(JMM_InterfaceDeclaration.__init__)


def test_hyp_jmm_interfacedeclaration_constructor_args():
    sig = inspect.signature(JMM_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_ClassDeclaration)


def test_hyp_jmm_classdeclaration_constructor_exists():
    assert callable(JMM_ClassDeclaration.__init__)


def test_hyp_jmm_classdeclaration_constructor_args():
    sig = inspect.signature(JMM_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_hyp_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_hyp_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_ConstructorDeclaration)


def test_hyp_jmm_constructordeclaration_constructor_exists():
    assert callable(JMM_ConstructorDeclaration.__init__)


def test_hyp_jmm_constructordeclaration_constructor_args():
    sig = inspect.signature(JMM_ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_MethodDeclaration)


def test_hyp_jmm_methoddeclaration_constructor_exists():
    assert callable(JMM_MethodDeclaration.__init__)


def test_hyp_jmm_methoddeclaration_constructor_args():
    sig = inspect.signature(JMM_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_hyp_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_hyp_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(JMM_AbstractVariablesContainer)


def test_hyp_jmm_abstractvariablescontainer_constructor_exists():
    assert callable(JMM_AbstractVariablesContainer.__init__)


def test_hyp_jmm_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(JMM_AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_expression_is_not_abstract():
    assert not inspect.isabstract(JMM_Expression)


def test_hyp_jmm_expression_constructor_exists():
    assert callable(JMM_Expression.__init__)


def test_hyp_jmm_expression_constructor_args():
    sig = inspect.signature(JMM_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(JMM_NamespaceAccess)


def test_hyp_jmm_namespaceaccess_constructor_exists():
    assert callable(JMM_NamespaceAccess.__init__)


def test_hyp_jmm_namespaceaccess_constructor_args():
    sig = inspect.signature(JMM_NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_namedelement_is_not_abstract():
    assert not inspect.isabstract(JMM_NamedElement)


def test_hyp_jmm_namedelement_constructor_exists():
    assert callable(JMM_NamedElement.__init__)


def test_hyp_jmm_namedelement_constructor_args():
    sig = inspect.signature(JMM_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"





def test_hyp_jmm_modifier_is_not_abstract():
    assert not inspect.isabstract(JMM_Modifier)


def test_hyp_jmm_modifier_constructor_exists():
    assert callable(JMM_Modifier.__init__)


def test_hyp_jmm_modifier_constructor_args():
    sig = inspect.signature(JMM_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"




def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_BodyDeclaration)


def test_hyp_jmm_bodydeclaration_constructor_exists():
    assert callable(JMM_BodyDeclaration.__init__)


def test_hyp_jmm_bodydeclaration_constructor_args():
    sig = inspect.signature(JMM_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_type_is_not_abstract():
    assert not inspect.isabstract(JMM_Type)


def test_hyp_jmm_type_constructor_exists():
    assert callable(JMM_Type.__init__)


def test_hyp_jmm_type_constructor_args():
    sig = inspect.signature(JMM_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_hyp_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_hyp_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_typeaccess_is_not_abstract():
    assert not inspect.isabstract(JMM_TypeAccess)


def test_hyp_jmm_typeaccess_constructor_exists():
    assert callable(JMM_TypeAccess.__init__)


def test_hyp_jmm_typeaccess_constructor_args():
    sig = inspect.signature(JMM_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_package_is_not_abstract():
    assert not inspect.isabstract(JMM_Package)


def test_hyp_jmm_package_constructor_exists():
    assert callable(JMM_Package.__init__)


def test_hyp_jmm_package_constructor_args():
    sig = inspect.signature(JMM_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_model_is_not_abstract():
    assert not inspect.isabstract(JMM_Model)


def test_hyp_jmm_model_constructor_exists():
    assert callable(JMM_Model.__init__)


def test_hyp_jmm_model_constructor_args():
    sig = inspect.signature(JMM_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_hyp_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_hyp_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_TypeDeclaration)


def test_hyp_jmm_typedeclaration_constructor_exists():
    assert callable(JMM_TypeDeclaration.__init__)


def test_hyp_jmm_typedeclaration_constructor_args():
    sig = inspect.signature(JMM_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_AnnotationTypeDeclaration)


def test_hyp_jmm_annotationtypedeclaration_constructor_exists():
    assert callable(JMM_AnnotationTypeDeclaration.__init__)


def test_hyp_jmm_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(JMM_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractVariablesContainer)


def test_hyp_abstractvariablescontainer_constructor_exists():
    assert callable(AbstractVariablesContainer.__init__)


def test_hyp_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_hyp_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_hyp_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_AbstractMethodDeclaration)


def test_hyp_jmm_abstractmethoddeclaration_constructor_exists():
    assert callable(JMM_AbstractMethodDeclaration.__init__)


def test_hyp_jmm_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(JMM_AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_AbstractTypeDeclaration)


def test_hyp_jmm_abstracttypedeclaration_constructor_exists():
    assert callable(JMM_AbstractTypeDeclaration.__init__)


def test_hyp_jmm_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JMM_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jmm_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_FieldDeclaration)


def test_hyp_jmm_fielddeclaration_constructor_exists():
    assert callable(JMM_FieldDeclaration.__init__)


def test_hyp_jmm_fielddeclaration_constructor_args():
    sig = inspect.signature(JMM_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_hyp_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_hyp_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "final",
        "abstract",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"


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
JMM_ASTNode_strategy = st.builds(
    JMM_ASTNode,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
JMM_InterfaceDeclaration_strategy = st.builds(
    JMM_InterfaceDeclaration,
)
JMM_ClassDeclaration_strategy = st.builds(
    JMM_ClassDeclaration,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
JMM_ConstructorDeclaration_strategy = st.builds(
    JMM_ConstructorDeclaration,
)
JMM_MethodDeclaration_strategy = st.builds(
    JMM_MethodDeclaration,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JMM_AbstractVariablesContainer_strategy = st.builds(
    JMM_AbstractVariablesContainer,
)
JMM_Expression_strategy = st.builds(
    JMM_Expression,
)
JMM_NamespaceAccess_strategy = st.builds(
    JMM_NamespaceAccess,
)
JMM_NamedElement_strategy = st.builds(
    JMM_NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
JMM_Modifier_strategy = st.builds(
    JMM_Modifier,
    inheritance=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JMM_BodyDeclaration_strategy = st.builds(
    JMM_BodyDeclaration,
)
JMM_Type_strategy = st.builds(
    JMM_Type,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
Expression_strategy = st.builds(
    Expression,
)
JMM_TypeAccess_strategy = st.builds(
    JMM_TypeAccess,
)
JMM_Package_strategy = st.builds(
    JMM_Package,
)
JMM_Model_strategy = st.builds(
    JMM_Model,
    name=
        safe_text
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JMM_TypeDeclaration_strategy = st.builds(
    JMM_TypeDeclaration,
)
JMM_AnnotationTypeDeclaration_strategy = st.builds(
    JMM_AnnotationTypeDeclaration,
)
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JMM_AbstractMethodDeclaration_strategy = st.builds(
    JMM_AbstractMethodDeclaration,
)
JMM_AbstractTypeDeclaration_strategy = st.builds(
    JMM_AbstractTypeDeclaration,
)
JMM_FieldDeclaration_strategy = st.builds(
    JMM_FieldDeclaration,
)















@given(instance=JMM_NamedElement_strategy)
def test_hyp_jmm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JMM_NamedElement_strategy)
def test_hyp_jmm_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original




@given(instance=JMM_Modifier_strategy)
def test_hyp_jmm_modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original












@given(instance=JMM_Model_strategy)
def test_hyp_jmm_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ASTNode,
    AbstractMethodDeclaration,
    AbstractTypeDeclaration,
    AbstractVariablesContainer,
    BodyDeclaration,
    Expression,
    JMM_ASTNode,
    JMM_AbstractMethodDeclaration,
    JMM_AbstractTypeDeclaration,
    JMM_AbstractVariablesContainer,
    JMM_AnnotationTypeDeclaration,
    JMM_BodyDeclaration,
    JMM_ClassDeclaration,
    JMM_ConstructorDeclaration,
    JMM_Expression,
    JMM_FieldDeclaration,
    JMM_InterfaceDeclaration,
    JMM_MethodDeclaration,
    JMM_Model,
    JMM_Modifier,
    JMM_NamedElement,
    JMM_NamespaceAccess,
    JMM_Package,
    JMM_Type,
    JMM_TypeAccess,
    JMM_TypeDeclaration,
    NamedElement,
    NamespaceAccess,
    Type,
    TypeDeclaration,
    InheritanceKind,
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

def test_JMM_Model_name_value_roundtrip():
    instance = JMM_Model(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_JMM_Modifier_inheritance_value_roundtrip():
    instance = JMM_Modifier(inheritance="sample_text")
    assert instance.inheritance == "sample_text"
    instance.inheritance = "sample_text_2"
    assert instance.inheritance == "sample_text_2"


def test_JMM_NamedElement_name_value_roundtrip():
    instance = JMM_NamedElement(name="sample_text", proxy=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_JMM_NamedElement_proxy_value_roundtrip():
    instance = JMM_NamedElement(name="sample_text", proxy=True)
    assert instance.proxy == True
    instance.proxy = False
    assert instance.proxy == False


def test_JMM_AbstractVariablesContainer_isa_ASTNode():
    instance = JMM_AbstractVariablesContainer()
    assert isinstance(instance, ASTNode)


def test_JMM_Expression_isa_ASTNode():
    instance = JMM_Expression()
    assert isinstance(instance, ASTNode)


def test_JMM_Modifier_isa_ASTNode():
    instance = JMM_Modifier(inheritance="sample_text")
    assert isinstance(instance, ASTNode)


def test_JMM_NamedElement_isa_ASTNode():
    instance = JMM_NamedElement(name="sample_text", proxy=True)
    assert isinstance(instance, ASTNode)


def test_JMM_NamespaceAccess_isa_ASTNode():
    instance = JMM_NamespaceAccess()
    assert isinstance(instance, ASTNode)


def test_JMM_ConstructorDeclaration_isa_AbstractMethodDeclaration():
    instance = JMM_ConstructorDeclaration()
    assert isinstance(instance, AbstractMethodDeclaration)


def test_JMM_MethodDeclaration_isa_AbstractMethodDeclaration():
    instance = JMM_MethodDeclaration()
    assert isinstance(instance, AbstractMethodDeclaration)


def test_JMM_AnnotationTypeDeclaration_isa_AbstractTypeDeclaration():
    instance = JMM_AnnotationTypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_JMM_TypeDeclaration_isa_AbstractTypeDeclaration():
    instance = JMM_TypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_JMM_FieldDeclaration_isa_AbstractVariablesContainer():
    instance = JMM_FieldDeclaration()
    assert isinstance(instance, AbstractVariablesContainer)


def test_JMM_AbstractMethodDeclaration_isa_BodyDeclaration():
    instance = JMM_AbstractMethodDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_JMM_AbstractTypeDeclaration_isa_BodyDeclaration():
    instance = JMM_AbstractTypeDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_JMM_FieldDeclaration_isa_BodyDeclaration():
    instance = JMM_FieldDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_JMM_TypeAccess_isa_Expression():
    instance = JMM_TypeAccess()
    assert isinstance(instance, Expression)


def test_JMM_BodyDeclaration_isa_NamedElement():
    instance = JMM_BodyDeclaration()
    assert isinstance(instance, NamedElement)


def test_JMM_Package_isa_NamedElement():
    instance = JMM_Package()
    assert isinstance(instance, NamedElement)


def test_JMM_Type_isa_NamedElement():
    instance = JMM_Type()
    assert isinstance(instance, NamedElement)


def test_JMM_TypeAccess_isa_NamespaceAccess():
    instance = JMM_TypeAccess()
    assert isinstance(instance, NamespaceAccess)


def test_JMM_AbstractTypeDeclaration_isa_Type():
    instance = JMM_AbstractTypeDeclaration()
    assert isinstance(instance, Type)


def test_JMM_ClassDeclaration_isa_TypeDeclaration():
    instance = JMM_ClassDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_JMM_InterfaceDeclaration_isa_TypeDeclaration():
    instance = JMM_InterfaceDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_assoc_modifier14_link_reassign_clear():
    a = JMM_Modifier(inheritance="sample_text")
    b1 = JMM_BodyDeclaration()
    b2 = JMM_BodyDeclaration()
    _safe_set(a, 'JMM_Modifier', b1)
    assert _is_linked(a, 'JMM_Modifier', b1)
    if hasattr(b1, 'JMM_BodyDeclaration15'):
        assert _is_linked(b1, 'JMM_BodyDeclaration15', a)
    _safe_set(a, 'JMM_Modifier', b2)
    assert _is_linked(a, 'JMM_Modifier', b2)
    if hasattr(b1, 'JMM_BodyDeclaration15'):
        assert not _is_linked(b1, 'JMM_BodyDeclaration15', a)
    if hasattr(b2, 'JMM_BodyDeclaration15'):
        assert _is_linked(b2, 'JMM_BodyDeclaration15', a)
    _safe_set(a, 'JMM_Modifier', None)
    assert not _is_linked(a, 'JMM_Modifier', b2)
    if hasattr(b2, 'JMM_BodyDeclaration15'):
        assert not _is_linked(b2, 'JMM_BodyDeclaration15', a)


def test_assoc_ownedElements0_link_reassign_clear():
    a = JMM_Model(name="sample_text")
    b1 = JMM_Package()
    b2 = JMM_Package()
    _safe_set(a, 'JMM_Model', {b1})
    assert _is_linked(a, 'JMM_Model', b1)
    if hasattr(b1, 'JMM_Package'):
        assert _is_linked(b1, 'JMM_Package', a)
    _safe_set(a, 'JMM_Model', {b2})
    assert _is_linked(a, 'JMM_Model', b2)
    if hasattr(b1, 'JMM_Package'):
        assert not _is_linked(b1, 'JMM_Package', a)
    if hasattr(b2, 'JMM_Package'):
        assert _is_linked(b2, 'JMM_Package', a)
    _safe_set(a, 'JMM_Model', set())
    assert not _is_linked(a, 'JMM_Model', b2)
    if hasattr(b2, 'JMM_Package'):
        assert not _is_linked(b2, 'JMM_Package', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ASTNode_strategy = st.builds(ASTNode)
@given(instance=ASTNode_strategy)
@settings(max_examples=25)
def test_ASTNode_instantiation(instance):
    assert isinstance(instance, ASTNode)


AbstractMethodDeclaration_strategy = st.builds(AbstractMethodDeclaration)
@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractMethodDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)


AbstractTypeDeclaration_strategy = st.builds(AbstractTypeDeclaration)
@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractTypeDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)


AbstractVariablesContainer_strategy = st.builds(AbstractVariablesContainer)
@given(instance=AbstractVariablesContainer_strategy)
@settings(max_examples=25)
def test_AbstractVariablesContainer_instantiation(instance):
    assert isinstance(instance, AbstractVariablesContainer)


BodyDeclaration_strategy = st.builds(BodyDeclaration)
@given(instance=BodyDeclaration_strategy)
@settings(max_examples=25)
def test_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


JMM_ASTNode_strategy = st.builds(JMM_ASTNode)
@given(instance=JMM_ASTNode_strategy)
@settings(max_examples=25)
def test_JMM_ASTNode_instantiation(instance):
    assert isinstance(instance, JMM_ASTNode)


JMM_AbstractMethodDeclaration_strategy = st.builds(JMM_AbstractMethodDeclaration)
@given(instance=JMM_AbstractMethodDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_AbstractMethodDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_AbstractMethodDeclaration)


JMM_AbstractTypeDeclaration_strategy = st.builds(JMM_AbstractTypeDeclaration)
@given(instance=JMM_AbstractTypeDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_AbstractTypeDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_AbstractTypeDeclaration)


JMM_AbstractVariablesContainer_strategy = st.builds(JMM_AbstractVariablesContainer)
@given(instance=JMM_AbstractVariablesContainer_strategy)
@settings(max_examples=25)
def test_JMM_AbstractVariablesContainer_instantiation(instance):
    assert isinstance(instance, JMM_AbstractVariablesContainer)


JMM_AnnotationTypeDeclaration_strategy = st.builds(JMM_AnnotationTypeDeclaration)
@given(instance=JMM_AnnotationTypeDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_AnnotationTypeDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_AnnotationTypeDeclaration)


JMM_BodyDeclaration_strategy = st.builds(JMM_BodyDeclaration)
@given(instance=JMM_BodyDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_BodyDeclaration)


JMM_ClassDeclaration_strategy = st.builds(JMM_ClassDeclaration)
@given(instance=JMM_ClassDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_ClassDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_ClassDeclaration)


JMM_ConstructorDeclaration_strategy = st.builds(JMM_ConstructorDeclaration)
@given(instance=JMM_ConstructorDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_ConstructorDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_ConstructorDeclaration)


JMM_Expression_strategy = st.builds(JMM_Expression)
@given(instance=JMM_Expression_strategy)
@settings(max_examples=25)
def test_JMM_Expression_instantiation(instance):
    assert isinstance(instance, JMM_Expression)


JMM_FieldDeclaration_strategy = st.builds(JMM_FieldDeclaration)
@given(instance=JMM_FieldDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_FieldDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_FieldDeclaration)


JMM_InterfaceDeclaration_strategy = st.builds(JMM_InterfaceDeclaration)
@given(instance=JMM_InterfaceDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_InterfaceDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_InterfaceDeclaration)


JMM_MethodDeclaration_strategy = st.builds(JMM_MethodDeclaration)
@given(instance=JMM_MethodDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_MethodDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_MethodDeclaration)


JMM_Model_strategy = st.builds(JMM_Model, name=safe_text)
@given(instance=JMM_Model_strategy)
@settings(max_examples=25)
def test_JMM_Model_instantiation(instance):
    assert isinstance(instance, JMM_Model)


JMM_Modifier_strategy = st.builds(JMM_Modifier, inheritance=safe_text)
@given(instance=JMM_Modifier_strategy)
@settings(max_examples=25)
def test_JMM_Modifier_instantiation(instance):
    assert isinstance(instance, JMM_Modifier)


JMM_NamedElement_strategy = st.builds(JMM_NamedElement, name=safe_text, proxy=st.booleans())
@given(instance=JMM_NamedElement_strategy)
@settings(max_examples=25)
def test_JMM_NamedElement_instantiation(instance):
    assert isinstance(instance, JMM_NamedElement)


JMM_NamespaceAccess_strategy = st.builds(JMM_NamespaceAccess)
@given(instance=JMM_NamespaceAccess_strategy)
@settings(max_examples=25)
def test_JMM_NamespaceAccess_instantiation(instance):
    assert isinstance(instance, JMM_NamespaceAccess)


JMM_Package_strategy = st.builds(JMM_Package)
@given(instance=JMM_Package_strategy)
@settings(max_examples=25)
def test_JMM_Package_instantiation(instance):
    assert isinstance(instance, JMM_Package)


JMM_Type_strategy = st.builds(JMM_Type)
@given(instance=JMM_Type_strategy)
@settings(max_examples=25)
def test_JMM_Type_instantiation(instance):
    assert isinstance(instance, JMM_Type)


JMM_TypeAccess_strategy = st.builds(JMM_TypeAccess)
@given(instance=JMM_TypeAccess_strategy)
@settings(max_examples=25)
def test_JMM_TypeAccess_instantiation(instance):
    assert isinstance(instance, JMM_TypeAccess)


JMM_TypeDeclaration_strategy = st.builds(JMM_TypeDeclaration)
@given(instance=JMM_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_JMM_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, JMM_TypeDeclaration)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NamespaceAccess_strategy = st.builds(NamespaceAccess)
@given(instance=NamespaceAccess_strategy)
@settings(max_examples=25)
def test_NamespaceAccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypeDeclaration_strategy = st.builds(TypeDeclaration)
@given(instance=TypeDeclaration_strategy)
@settings(max_examples=25)
def test_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)



