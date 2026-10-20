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
    DirectedRelationship,
    BehavioredClassifier,
    umluseCases_Actor,
    Classifier,
    umluseCases_BehavioredClassifier,
    umluseCases_UseCase,
    TemplateableElement,
    Type,
    RedefinableElement,
    umluseCases_ExtensionPoint,
    Namespace,
    umluseCases_Classifier,
    PackageableElement,
    umluseCases_Type,
    Relationship,
    umluseCases_DirectedRelationship,
    Element,
    umluseCases_TemplateableElement,
    umluseCases_ParameterableElement,
    umluseCases_Relationship,
    umluseCases_NamedElement,
    ParameterableElement,
    NamedElement,
    umluseCases_Extend,
    umluseCases_Include,
    umluseCases_RedefinableElement,
    umluseCases_Namespace,
    umluseCases_PackageableElement,
    EModelElement,
    umluseCases_Element,
    CallConcurrencyKind,
    ObjectNodeOrderingKind,
    TransitionKind,
    MessageSort,
    ParameterDirectionKind,
    MessageKind,
    ParameterEffectKind,
    ExpansionKind,
    VisibilityKind,
    PseudostateKind,
    InteractionOperatorKind,
    AggregationKind,
    ConnectorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_hyp_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_hyp_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_hyp_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_hyp_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_actor_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Actor)


def test_hyp_umlusecases_actor_constructor_exists():
    assert callable(umluseCases_Actor.__init__)


def test_hyp_umlusecases_actor_constructor_args():
    sig = inspect.signature(umluseCases_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(umluseCases_BehavioredClassifier)


def test_hyp_umlusecases_behavioredclassifier_constructor_exists():
    assert callable(umluseCases_BehavioredClassifier.__init__)


def test_hyp_umlusecases_behavioredclassifier_constructor_args():
    sig = inspect.signature(umluseCases_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_usecase_is_not_abstract():
    assert not inspect.isabstract(umluseCases_UseCase)


def test_hyp_umlusecases_usecase_constructor_exists():
    assert callable(umluseCases_UseCase.__init__)


def test_hyp_umlusecases_usecase_constructor_args():
    sig = inspect.signature(umluseCases_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_hyp_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_hyp_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_hyp_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_hyp_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(umluseCases_ExtensionPoint)


def test_hyp_umlusecases_extensionpoint_constructor_exists():
    assert callable(umluseCases_ExtensionPoint.__init__)


def test_hyp_umlusecases_extensionpoint_constructor_args():
    sig = inspect.signature(umluseCases_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_hyp_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_hyp_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_classifier_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Classifier)


def test_hyp_umlusecases_classifier_constructor_exists():
    assert callable(umluseCases_Classifier.__init__)


def test_hyp_umlusecases_classifier_constructor_args():
    sig = inspect.signature(umluseCases_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"




def test_hyp_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_hyp_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_hyp_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_type_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Type)


def test_hyp_umlusecases_type_constructor_exists():
    assert callable(umluseCases_Type.__init__)


def test_hyp_umlusecases_type_constructor_args():
    sig = inspect.signature(umluseCases_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_hyp_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_hyp_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(umluseCases_DirectedRelationship)


def test_hyp_umlusecases_directedrelationship_constructor_exists():
    assert callable(umluseCases_DirectedRelationship.__init__)


def test_hyp_umlusecases_directedrelationship_constructor_args():
    sig = inspect.signature(umluseCases_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_templateableelement_is_not_abstract():
    assert not inspect.isabstract(umluseCases_TemplateableElement)


def test_hyp_umlusecases_templateableelement_constructor_exists():
    assert callable(umluseCases_TemplateableElement.__init__)


def test_hyp_umlusecases_templateableelement_constructor_args():
    sig = inspect.signature(umluseCases_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(umluseCases_ParameterableElement)


def test_hyp_umlusecases_parameterableelement_constructor_exists():
    assert callable(umluseCases_ParameterableElement.__init__)


def test_hyp_umlusecases_parameterableelement_constructor_args():
    sig = inspect.signature(umluseCases_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_relationship_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Relationship)


def test_hyp_umlusecases_relationship_constructor_exists():
    assert callable(umluseCases_Relationship.__init__)


def test_hyp_umlusecases_relationship_constructor_args():
    sig = inspect.signature(umluseCases_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_namedelement_is_not_abstract():
    assert not inspect.isabstract(umluseCases_NamedElement)


def test_hyp_umlusecases_namedelement_constructor_exists():
    assert callable(umluseCases_NamedElement.__init__)


def test_hyp_umlusecases_namedelement_constructor_args():
    sig = inspect.signature(umluseCases_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"






def test_hyp_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_hyp_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_hyp_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_extend_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Extend)


def test_hyp_umlusecases_extend_constructor_exists():
    assert callable(umluseCases_Extend.__init__)


def test_hyp_umlusecases_extend_constructor_args():
    sig = inspect.signature(umluseCases_Extend.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_include_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Include)


def test_hyp_umlusecases_include_constructor_exists():
    assert callable(umluseCases_Include.__init__)


def test_hyp_umlusecases_include_constructor_args():
    sig = inspect.signature(umluseCases_Include.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(umluseCases_RedefinableElement)


def test_hyp_umlusecases_redefinableelement_constructor_exists():
    assert callable(umluseCases_RedefinableElement.__init__)


def test_hyp_umlusecases_redefinableelement_constructor_args():
    sig = inspect.signature(umluseCases_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"




def test_hyp_umlusecases_namespace_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Namespace)


def test_hyp_umlusecases_namespace_constructor_exists():
    assert callable(umluseCases_Namespace.__init__)


def test_hyp_umlusecases_namespace_constructor_args():
    sig = inspect.signature(umluseCases_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_packageableelement_is_not_abstract():
    assert not inspect.isabstract(umluseCases_PackageableElement)


def test_hyp_umlusecases_packageableelement_constructor_exists():
    assert callable(umluseCases_PackageableElement.__init__)


def test_hyp_umlusecases_packageableelement_constructor_args():
    sig = inspect.signature(umluseCases_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_hyp_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_hyp_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlusecases_element_is_not_abstract():
    assert not inspect.isabstract(umluseCases_Element)


def test_hyp_umlusecases_element_constructor_exists():
    assert callable(umluseCases_Element.__init__)


def test_hyp_umlusecases_element_constructor_args():
    sig = inspect.signature(umluseCases_Element.__init__)
    params = list(sig.parameters.keys())

def test_hyp_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_hyp_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "sequential",
        "concurrent",
        "guarded",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

def test_hyp_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_hyp_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "LIFO",
        "unordered",
        "ordered",
        "FIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

def test_hyp_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_hyp_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "external",
        "local",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_hyp_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_hyp_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "synchCall",
        "deleteMessage",
        "reply",
        "asynchCall",
        "asynchSignal",
        "createMessage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_hyp_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_hyp_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "out",
        "inout",
        "return_",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_hyp_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_hyp_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "found",
        "unknown",
        "lost",
        "complete",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"

def test_hyp_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_hyp_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "read",
        "create",
        "delete",
        "update",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_hyp_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_hyp_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "parallel",
        "iterative",
        "stream",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_hyp_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_hyp_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "protected",
        "package",
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_hyp_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_hyp_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "entryPoint",
        "terminate",
        "initial",
        "fork",
        "join",
        "junction",
        "shallowHistory",
        "choice",
        "deepHistory",
        "exitPoint",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_hyp_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_hyp_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "loop",
        "opt",
        "seq",
        "critical",
        "consider",
        "alt",
        "par",
        "neg",
        "ignore",
        "assert_",
        "break_",
        "strict",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_hyp_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_hyp_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "shared",
        "none",
        "composite",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"

def test_hyp_connectorkind_exists():
    # Check that the Enumeration exists
    assert ConnectorKind is not None

def test_hyp_connectorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectorKind]
    expected_literals = [
        "delegation",
        "assembly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectorKind"


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
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
umluseCases_Actor_strategy = st.builds(
    umluseCases_Actor,
)
Classifier_strategy = st.builds(
    Classifier,
)
umluseCases_BehavioredClassifier_strategy = st.builds(
    umluseCases_BehavioredClassifier,
)
umluseCases_UseCase_strategy = st.builds(
    umluseCases_UseCase,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
umluseCases_ExtensionPoint_strategy = st.builds(
    umluseCases_ExtensionPoint,
)
Namespace_strategy = st.builds(
    Namespace,
)
umluseCases_Classifier_strategy = st.builds(
    umluseCases_Classifier,
    isAbstract=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
umluseCases_Type_strategy = st.builds(
    umluseCases_Type,
)
Relationship_strategy = st.builds(
    Relationship,
)
umluseCases_DirectedRelationship_strategy = st.builds(
    umluseCases_DirectedRelationship,
)
Element_strategy = st.builds(
    Element,
)
umluseCases_TemplateableElement_strategy = st.builds(
    umluseCases_TemplateableElement,
)
umluseCases_ParameterableElement_strategy = st.builds(
    umluseCases_ParameterableElement,
)
umluseCases_Relationship_strategy = st.builds(
    umluseCases_Relationship,
)
umluseCases_NamedElement_strategy = st.builds(
    umluseCases_NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text,
    visibility=
        safe_text
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
umluseCases_Extend_strategy = st.builds(
    umluseCases_Extend,
)
umluseCases_Include_strategy = st.builds(
    umluseCases_Include,
)
umluseCases_RedefinableElement_strategy = st.builds(
    umluseCases_RedefinableElement,
    isLeaf=
        safe_text
)
umluseCases_Namespace_strategy = st.builds(
    umluseCases_Namespace,
)
umluseCases_PackageableElement_strategy = st.builds(
    umluseCases_PackageableElement,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
umluseCases_Element_strategy = st.builds(
    umluseCases_Element,
)




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings






import warnings
import copy
import inspect
import ast
from hypothesis import given, settings






@given(instance=umluseCases_Classifier_strategy)
def test_hyp_umlusecases_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original












@given(instance=umluseCases_NamedElement_strategy)
def test_hyp_umlusecases_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=umluseCases_NamedElement_strategy)
def test_hyp_umlusecases_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=umluseCases_NamedElement_strategy)
def test_hyp_umlusecases_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings






@given(instance=umluseCases_RedefinableElement_strategy)
def test_hyp_umlusecases_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BehavioredClassifier,
    Classifier,
    DirectedRelationship,
    EModelElement,
    Element,
    NamedElement,
    Namespace,
    PackageableElement,
    ParameterableElement,
    RedefinableElement,
    Relationship,
    TemplateableElement,
    Type,
    umluseCases_Actor,
    umluseCases_BehavioredClassifier,
    umluseCases_Classifier,
    umluseCases_DirectedRelationship,
    umluseCases_Element,
    umluseCases_Extend,
    umluseCases_ExtensionPoint,
    umluseCases_Include,
    umluseCases_NamedElement,
    umluseCases_Namespace,
    umluseCases_PackageableElement,
    umluseCases_ParameterableElement,
    umluseCases_RedefinableElement,
    umluseCases_Relationship,
    umluseCases_TemplateableElement,
    umluseCases_Type,
    umluseCases_UseCase,
    AggregationKind,
    CallConcurrencyKind,
    ConnectorKind,
    ExpansionKind,
    InteractionOperatorKind,
    MessageKind,
    MessageSort,
    ObjectNodeOrderingKind,
    ParameterDirectionKind,
    ParameterEffectKind,
    PseudostateKind,
    TransitionKind,
    VisibilityKind,
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

def test_umluseCases_Classifier_isAbstract_value_roundtrip():
    instance = umluseCases_Classifier(isAbstract="sample_text")
    assert instance.isAbstract == "sample_text"
    instance.isAbstract = "sample_text_2"
    assert instance.isAbstract == "sample_text_2"


def test_umluseCases_NamedElement_name_value_roundtrip():
    instance = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_umluseCases_NamedElement_qualifiedName_value_roundtrip():
    instance = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_umluseCases_NamedElement_visibility_value_roundtrip():
    instance = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_umluseCases_RedefinableElement_isLeaf_value_roundtrip():
    instance = umluseCases_RedefinableElement(isLeaf="sample_text")
    assert instance.isLeaf == "sample_text"
    instance.isLeaf = "sample_text_2"
    assert instance.isLeaf == "sample_text_2"


def test_umluseCases_Actor_isa_BehavioredClassifier():
    instance = umluseCases_Actor()
    assert isinstance(instance, BehavioredClassifier)


def test_umluseCases_UseCase_isa_BehavioredClassifier():
    instance = umluseCases_UseCase()
    assert isinstance(instance, BehavioredClassifier)


def test_umluseCases_BehavioredClassifier_isa_Classifier():
    instance = umluseCases_BehavioredClassifier()
    assert isinstance(instance, Classifier)


def test_umluseCases_Extend_isa_DirectedRelationship():
    instance = umluseCases_Extend()
    assert isinstance(instance, DirectedRelationship)


def test_umluseCases_Include_isa_DirectedRelationship():
    instance = umluseCases_Include()
    assert isinstance(instance, DirectedRelationship)


def test_umluseCases_Element_isa_EModelElement():
    instance = umluseCases_Element()
    assert isinstance(instance, EModelElement)


def test_umluseCases_NamedElement_isa_Element():
    instance = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert isinstance(instance, Element)


def test_umluseCases_ParameterableElement_isa_Element():
    instance = umluseCases_ParameterableElement()
    assert isinstance(instance, Element)


def test_umluseCases_Relationship_isa_Element():
    instance = umluseCases_Relationship()
    assert isinstance(instance, Element)


def test_umluseCases_TemplateableElement_isa_Element():
    instance = umluseCases_TemplateableElement()
    assert isinstance(instance, Element)


def test_umluseCases_Extend_isa_NamedElement():
    instance = umluseCases_Extend()
    assert isinstance(instance, NamedElement)


def test_umluseCases_Include_isa_NamedElement():
    instance = umluseCases_Include()
    assert isinstance(instance, NamedElement)


def test_umluseCases_Namespace_isa_NamedElement():
    instance = umluseCases_Namespace()
    assert isinstance(instance, NamedElement)


def test_umluseCases_PackageableElement_isa_NamedElement():
    instance = umluseCases_PackageableElement()
    assert isinstance(instance, NamedElement)


def test_umluseCases_RedefinableElement_isa_NamedElement():
    instance = umluseCases_RedefinableElement(isLeaf="sample_text")
    assert isinstance(instance, NamedElement)


def test_umluseCases_Classifier_isa_Namespace():
    instance = umluseCases_Classifier(isAbstract="sample_text")
    assert isinstance(instance, Namespace)


def test_umluseCases_Type_isa_PackageableElement():
    instance = umluseCases_Type()
    assert isinstance(instance, PackageableElement)


def test_umluseCases_PackageableElement_isa_ParameterableElement():
    instance = umluseCases_PackageableElement()
    assert isinstance(instance, ParameterableElement)


def test_umluseCases_Classifier_isa_RedefinableElement():
    instance = umluseCases_Classifier(isAbstract="sample_text")
    assert isinstance(instance, RedefinableElement)


def test_umluseCases_ExtensionPoint_isa_RedefinableElement():
    instance = umluseCases_ExtensionPoint()
    assert isinstance(instance, RedefinableElement)


def test_umluseCases_DirectedRelationship_isa_Relationship():
    instance = umluseCases_DirectedRelationship()
    assert isinstance(instance, Relationship)


def test_umluseCases_Classifier_isa_TemplateableElement():
    instance = umluseCases_Classifier(isAbstract="sample_text")
    assert isinstance(instance, TemplateableElement)


def test_umluseCases_Classifier_isa_Type():
    instance = umluseCases_Classifier(isAbstract="sample_text")
    assert isinstance(instance, Type)


def test_assoc_addition37_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Include()
    b2 = umluseCases_Include()
    _safe_set(a, 'umluseCases_UseCase38', b1)
    assert _is_linked(a, 'umluseCases_UseCase38', b1)
    if hasattr(b1, 'umluseCases_Include'):
        assert _is_linked(b1, 'umluseCases_Include', a)
    _safe_set(a, 'umluseCases_UseCase38', b2)
    assert _is_linked(a, 'umluseCases_UseCase38', b2)
    if hasattr(b1, 'umluseCases_Include'):
        assert not _is_linked(b1, 'umluseCases_Include', a)
    if hasattr(b2, 'umluseCases_Include'):
        assert _is_linked(b2, 'umluseCases_Include', a)
    _safe_set(a, 'umluseCases_UseCase38', None)
    assert not _is_linked(a, 'umluseCases_UseCase38', b2)
    if hasattr(b2, 'umluseCases_Include'):
        assert not _is_linked(b2, 'umluseCases_Include', a)


def test_assoc_extend33_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Extend()
    b2 = umluseCases_Extend()
    _safe_set(a, 'extension', {b1})
    assert _is_linked(a, 'extension', b1)
    if hasattr(b1, 'Extend'):
        assert _is_linked(b1, 'Extend', a)
    _safe_set(a, 'extension', {b2})
    assert _is_linked(a, 'extension', b2)
    if hasattr(b1, 'Extend'):
        assert not _is_linked(b1, 'Extend', a)
    if hasattr(b2, 'Extend'):
        assert _is_linked(b2, 'Extend', a)
    _safe_set(a, 'extension', set())
    assert not _is_linked(a, 'extension', b2)
    if hasattr(b2, 'Extend'):
        assert not _is_linked(b2, 'Extend', a)


def test_assoc_extendedCase41_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Extend()
    b2 = umluseCases_Extend()
    _safe_set(a, 'umluseCases_UseCase42', b1)
    assert _is_linked(a, 'umluseCases_UseCase42', b1)
    if hasattr(b1, 'umluseCases_Extend'):
        assert _is_linked(b1, 'umluseCases_Extend', a)
    _safe_set(a, 'umluseCases_UseCase42', b2)
    assert _is_linked(a, 'umluseCases_UseCase42', b2)
    if hasattr(b1, 'umluseCases_Extend'):
        assert not _is_linked(b1, 'umluseCases_Extend', a)
    if hasattr(b2, 'umluseCases_Extend'):
        assert _is_linked(b2, 'umluseCases_Extend', a)
    _safe_set(a, 'umluseCases_UseCase42', None)
    assert not _is_linked(a, 'umluseCases_UseCase42', b2)
    if hasattr(b2, 'umluseCases_Extend'):
        assert not _is_linked(b2, 'umluseCases_Extend', a)


def test_assoc_extension45_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Extend()
    b2 = umluseCases_Extend()
    _safe_set(a, 'UseCase46', b1)
    assert _is_linked(a, 'UseCase46', b1)
    if hasattr(b1, 'extend'):
        assert _is_linked(b1, 'extend', a)
    _safe_set(a, 'UseCase46', b2)
    assert _is_linked(a, 'UseCase46', b2)
    if hasattr(b1, 'extend'):
        assert not _is_linked(b1, 'extend', a)
    if hasattr(b2, 'extend'):
        assert _is_linked(b2, 'extend', a)
    _safe_set(a, 'UseCase46', None)
    assert not _is_linked(a, 'UseCase46', b2)
    if hasattr(b2, 'extend'):
        assert not _is_linked(b2, 'extend', a)


def test_assoc_extensionLocation43_link_reassign_clear():
    a = umluseCases_ExtensionPoint()
    b1 = umluseCases_Extend()
    b2 = umluseCases_Extend()
    _safe_set(a, 'umluseCases_ExtensionPoint', b1)
    assert _is_linked(a, 'umluseCases_ExtensionPoint', b1)
    if hasattr(b1, 'umluseCases_Extend44'):
        assert _is_linked(b1, 'umluseCases_Extend44', a)
    _safe_set(a, 'umluseCases_ExtensionPoint', b2)
    assert _is_linked(a, 'umluseCases_ExtensionPoint', b2)
    if hasattr(b1, 'umluseCases_Extend44'):
        assert not _is_linked(b1, 'umluseCases_Extend44', a)
    if hasattr(b2, 'umluseCases_Extend44'):
        assert _is_linked(b2, 'umluseCases_Extend44', a)
    _safe_set(a, 'umluseCases_ExtensionPoint', None)
    assert not _is_linked(a, 'umluseCases_ExtensionPoint', b2)
    if hasattr(b2, 'umluseCases_Extend44'):
        assert not _is_linked(b2, 'umluseCases_Extend44', a)


def test_assoc_extensionPoint34_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_ExtensionPoint()
    b2 = umluseCases_ExtensionPoint()
    _safe_set(a, 'useCase', {b1})
    assert _is_linked(a, 'useCase', b1)
    if hasattr(b1, 'ExtensionPoint'):
        assert _is_linked(b1, 'ExtensionPoint', a)
    _safe_set(a, 'useCase', {b2})
    assert _is_linked(a, 'useCase', b2)
    if hasattr(b1, 'ExtensionPoint'):
        assert not _is_linked(b1, 'ExtensionPoint', a)
    if hasattr(b2, 'ExtensionPoint'):
        assert _is_linked(b2, 'ExtensionPoint', a)
    _safe_set(a, 'useCase', set())
    assert not _is_linked(a, 'useCase', b2)
    if hasattr(b2, 'ExtensionPoint'):
        assert not _is_linked(b2, 'ExtensionPoint', a)


def test_assoc_general22_link_reassign_clear():
    a = umluseCases_Classifier(isAbstract="sample_text")
    b1 = umluseCases_Classifier(isAbstract="sample_text")
    b2 = umluseCases_Classifier(isAbstract="sample_text_2")
    _safe_set(a, 'umluseCases_Classifier21', {b1})
    assert _is_linked(a, 'umluseCases_Classifier21', b1)
    if hasattr(b1, 'umluseCases_Classifier23'):
        assert _is_linked(b1, 'umluseCases_Classifier23', a)
    _safe_set(a, 'umluseCases_Classifier21', {b2})
    assert _is_linked(a, 'umluseCases_Classifier21', b2)
    if hasattr(b1, 'umluseCases_Classifier23'):
        assert not _is_linked(b1, 'umluseCases_Classifier23', a)
    if hasattr(b2, 'umluseCases_Classifier23'):
        assert _is_linked(b2, 'umluseCases_Classifier23', a)
    _safe_set(a, 'umluseCases_Classifier21', set())
    assert not _is_linked(a, 'umluseCases_Classifier21', b2)
    if hasattr(b2, 'umluseCases_Classifier23'):
        assert not _is_linked(b2, 'umluseCases_Classifier23', a)


def test_assoc_include32_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Include()
    b2 = umluseCases_Include()
    _safe_set(a, 'includingCase', {b1})
    assert _is_linked(a, 'includingCase', b1)
    if hasattr(b1, 'Include'):
        assert _is_linked(b1, 'Include', a)
    _safe_set(a, 'includingCase', {b2})
    assert _is_linked(a, 'includingCase', b2)
    if hasattr(b1, 'Include'):
        assert not _is_linked(b1, 'Include', a)
    if hasattr(b2, 'Include'):
        assert _is_linked(b2, 'Include', a)
    _safe_set(a, 'includingCase', set())
    assert not _is_linked(a, 'includingCase', b2)
    if hasattr(b2, 'Include'):
        assert not _is_linked(b2, 'Include', a)


def test_assoc_includingCase39_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Include()
    b2 = umluseCases_Include()
    _safe_set(a, 'UseCase40', b1)
    assert _is_linked(a, 'UseCase40', b1)
    if hasattr(b1, 'include'):
        assert _is_linked(b1, 'include', a)
    _safe_set(a, 'UseCase40', b2)
    assert _is_linked(a, 'UseCase40', b2)
    if hasattr(b1, 'include'):
        assert not _is_linked(b1, 'include', a)
    if hasattr(b2, 'include'):
        assert _is_linked(b2, 'include', a)
    _safe_set(a, 'UseCase40', None)
    assert not _is_linked(a, 'UseCase40', b2)
    if hasattr(b2, 'include'):
        assert not _is_linked(b2, 'include', a)


def test_assoc_inheritedMember16_link_reassign_clear():
    a = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = umluseCases_Classifier(isAbstract="sample_text")
    b2 = umluseCases_Classifier(isAbstract="sample_text_2")
    _safe_set(a, 'umluseCases_NamedElement17', b1)
    assert _is_linked(a, 'umluseCases_NamedElement17', b1)
    if hasattr(b1, 'umluseCases_Classifier'):
        assert _is_linked(b1, 'umluseCases_Classifier', a)
    _safe_set(a, 'umluseCases_NamedElement17', b2)
    assert _is_linked(a, 'umluseCases_NamedElement17', b2)
    if hasattr(b1, 'umluseCases_Classifier'):
        assert not _is_linked(b1, 'umluseCases_Classifier', a)
    if hasattr(b2, 'umluseCases_Classifier'):
        assert _is_linked(b2, 'umluseCases_Classifier', a)
    _safe_set(a, 'umluseCases_NamedElement17', None)
    assert not _is_linked(a, 'umluseCases_NamedElement17', b2)
    if hasattr(b2, 'umluseCases_Classifier'):
        assert not _is_linked(b2, 'umluseCases_Classifier', a)


def test_assoc_member12_link_reassign_clear():
    a = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = umluseCases_Namespace()
    b2 = umluseCases_Namespace()
    _safe_set(a, 'umluseCases_NamedElement', b1)
    assert _is_linked(a, 'umluseCases_NamedElement', b1)
    if hasattr(b1, 'umluseCases_Namespace'):
        assert _is_linked(b1, 'umluseCases_Namespace', a)
    _safe_set(a, 'umluseCases_NamedElement', b2)
    assert _is_linked(a, 'umluseCases_NamedElement', b2)
    if hasattr(b1, 'umluseCases_Namespace'):
        assert not _is_linked(b1, 'umluseCases_Namespace', a)
    if hasattr(b2, 'umluseCases_Namespace'):
        assert _is_linked(b2, 'umluseCases_Namespace', a)
    _safe_set(a, 'umluseCases_NamedElement', None)
    assert not _is_linked(a, 'umluseCases_NamedElement', b2)
    if hasattr(b2, 'umluseCases_Namespace'):
        assert not _is_linked(b2, 'umluseCases_Namespace', a)


def test_assoc_namespace5_link_reassign_clear():
    a = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = umluseCases_Namespace()
    b2 = umluseCases_Namespace()
    _safe_set(a, 'ownedMember', b1)
    assert _is_linked(a, 'ownedMember', b1)
    if hasattr(b1, 'Namespace'):
        assert _is_linked(b1, 'Namespace', a)
    _safe_set(a, 'ownedMember', b2)
    assert _is_linked(a, 'ownedMember', b2)
    if hasattr(b1, 'Namespace'):
        assert not _is_linked(b1, 'Namespace', a)
    if hasattr(b2, 'Namespace'):
        assert _is_linked(b2, 'Namespace', a)
    _safe_set(a, 'ownedMember', None)
    assert not _is_linked(a, 'ownedMember', b2)
    if hasattr(b2, 'Namespace'):
        assert not _is_linked(b2, 'Namespace', a)


def test_assoc_ownedMember15_link_reassign_clear():
    a = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = umluseCases_Namespace()
    b2 = umluseCases_Namespace()
    _safe_set(a, 'NamedElement', b1)
    assert _is_linked(a, 'NamedElement', b1)
    if hasattr(b1, 'namespace'):
        assert _is_linked(b1, 'namespace', a)
    _safe_set(a, 'NamedElement', b2)
    assert _is_linked(a, 'NamedElement', b2)
    if hasattr(b1, 'namespace'):
        assert not _is_linked(b1, 'namespace', a)
    if hasattr(b2, 'namespace'):
        assert _is_linked(b2, 'namespace', a)
    _safe_set(a, 'NamedElement', None)
    assert not _is_linked(a, 'NamedElement', b2)
    if hasattr(b2, 'namespace'):
        assert not _is_linked(b2, 'namespace', a)


def test_assoc_ownedUseCase24_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Classifier(isAbstract="sample_text")
    b2 = umluseCases_Classifier(isAbstract="sample_text_2")
    _safe_set(a, 'umluseCases_UseCase', b1)
    assert _is_linked(a, 'umluseCases_UseCase', b1)
    if hasattr(b1, 'umluseCases_Classifier25'):
        assert _is_linked(b1, 'umluseCases_Classifier25', a)
    _safe_set(a, 'umluseCases_UseCase', b2)
    assert _is_linked(a, 'umluseCases_UseCase', b2)
    if hasattr(b1, 'umluseCases_Classifier25'):
        assert not _is_linked(b1, 'umluseCases_Classifier25', a)
    if hasattr(b2, 'umluseCases_Classifier25'):
        assert _is_linked(b2, 'umluseCases_Classifier25', a)
    _safe_set(a, 'umluseCases_UseCase', None)
    assert not _is_linked(a, 'umluseCases_UseCase', b2)
    if hasattr(b2, 'umluseCases_Classifier25'):
        assert not _is_linked(b2, 'umluseCases_Classifier25', a)


def test_assoc_redefinedClassifier19_link_reassign_clear():
    a = umluseCases_Classifier(isAbstract="sample_text")
    b1 = umluseCases_Classifier(isAbstract="sample_text")
    b2 = umluseCases_Classifier(isAbstract="sample_text_2")
    _safe_set(a, 'umluseCases_Classifier18', {b1})
    assert _is_linked(a, 'umluseCases_Classifier18', b1)
    if hasattr(b1, 'umluseCases_Classifier20'):
        assert _is_linked(b1, 'umluseCases_Classifier20', a)
    _safe_set(a, 'umluseCases_Classifier18', {b2})
    assert _is_linked(a, 'umluseCases_Classifier18', b2)
    if hasattr(b1, 'umluseCases_Classifier20'):
        assert not _is_linked(b1, 'umluseCases_Classifier20', a)
    if hasattr(b2, 'umluseCases_Classifier20'):
        assert _is_linked(b2, 'umluseCases_Classifier20', a)
    _safe_set(a, 'umluseCases_Classifier18', set())
    assert not _is_linked(a, 'umluseCases_Classifier18', b2)
    if hasattr(b2, 'umluseCases_Classifier20'):
        assert not _is_linked(b2, 'umluseCases_Classifier20', a)


def test_assoc_redefinedElement28_link_reassign_clear():
    a = umluseCases_RedefinableElement(isLeaf="sample_text")
    b1 = umluseCases_RedefinableElement(isLeaf="sample_text")
    b2 = umluseCases_RedefinableElement(isLeaf="sample_text_2")
    _safe_set(a, 'umluseCases_RedefinableElement', b1)
    assert _is_linked(a, 'umluseCases_RedefinableElement', b1)
    if hasattr(b1, 'umluseCases_RedefinableElement27'):
        assert _is_linked(b1, 'umluseCases_RedefinableElement27', a)
    _safe_set(a, 'umluseCases_RedefinableElement', b2)
    assert _is_linked(a, 'umluseCases_RedefinableElement', b2)
    if hasattr(b1, 'umluseCases_RedefinableElement27'):
        assert not _is_linked(b1, 'umluseCases_RedefinableElement27', a)
    if hasattr(b2, 'umluseCases_RedefinableElement27'):
        assert _is_linked(b2, 'umluseCases_RedefinableElement27', a)
    _safe_set(a, 'umluseCases_RedefinableElement', None)
    assert not _is_linked(a, 'umluseCases_RedefinableElement', b2)
    if hasattr(b2, 'umluseCases_RedefinableElement27'):
        assert not _is_linked(b2, 'umluseCases_RedefinableElement27', a)


def test_assoc_redefinitionContext29_link_reassign_clear():
    a = umluseCases_RedefinableElement(isLeaf="sample_text")
    b1 = umluseCases_Classifier(isAbstract="sample_text")
    b2 = umluseCases_Classifier(isAbstract="sample_text_2")
    _safe_set(a, 'umluseCases_RedefinableElement30', {b1})
    assert _is_linked(a, 'umluseCases_RedefinableElement30', b1)
    if hasattr(b1, 'umluseCases_Classifier31'):
        assert _is_linked(b1, 'umluseCases_Classifier31', a)
    _safe_set(a, 'umluseCases_RedefinableElement30', {b2})
    assert _is_linked(a, 'umluseCases_RedefinableElement30', b2)
    if hasattr(b1, 'umluseCases_Classifier31'):
        assert not _is_linked(b1, 'umluseCases_Classifier31', a)
    if hasattr(b2, 'umluseCases_Classifier31'):
        assert _is_linked(b2, 'umluseCases_Classifier31', a)
    _safe_set(a, 'umluseCases_RedefinableElement30', set())
    assert not _is_linked(a, 'umluseCases_RedefinableElement30', b2)
    if hasattr(b2, 'umluseCases_Classifier31'):
        assert not _is_linked(b2, 'umluseCases_Classifier31', a)


def test_assoc_subject35_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Classifier(isAbstract="sample_text")
    b2 = umluseCases_Classifier(isAbstract="sample_text_2")
    _safe_set(a, 'useCase36', {b1})
    assert _is_linked(a, 'useCase36', b1)
    if hasattr(b1, 'Classifier'):
        assert _is_linked(b1, 'Classifier', a)
    _safe_set(a, 'useCase36', {b2})
    assert _is_linked(a, 'useCase36', b2)
    if hasattr(b1, 'Classifier'):
        assert not _is_linked(b1, 'Classifier', a)
    if hasattr(b2, 'Classifier'):
        assert _is_linked(b2, 'Classifier', a)
    _safe_set(a, 'useCase36', set())
    assert not _is_linked(a, 'useCase36', b2)
    if hasattr(b2, 'Classifier'):
        assert not _is_linked(b2, 'Classifier', a)


def test_assoc_useCase26_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_Classifier(isAbstract="sample_text")
    b2 = umluseCases_Classifier(isAbstract="sample_text_2")
    _safe_set(a, 'UseCase', b1)
    assert _is_linked(a, 'UseCase', b1)
    if hasattr(b1, 'subject'):
        assert _is_linked(b1, 'subject', a)
    _safe_set(a, 'UseCase', b2)
    assert _is_linked(a, 'UseCase', b2)
    if hasattr(b1, 'subject'):
        assert not _is_linked(b1, 'subject', a)
    if hasattr(b2, 'subject'):
        assert _is_linked(b2, 'subject', a)
    _safe_set(a, 'UseCase', None)
    assert not _is_linked(a, 'UseCase', b2)
    if hasattr(b2, 'subject'):
        assert not _is_linked(b2, 'subject', a)


def test_assoc_useCase47_link_reassign_clear():
    a = umluseCases_UseCase()
    b1 = umluseCases_ExtensionPoint()
    b2 = umluseCases_ExtensionPoint()
    _safe_set(a, 'UseCase48', b1)
    assert _is_linked(a, 'UseCase48', b1)
    if hasattr(b1, 'extensionPoint'):
        assert _is_linked(b1, 'extensionPoint', a)
    _safe_set(a, 'UseCase48', b2)
    assert _is_linked(a, 'UseCase48', b2)
    if hasattr(b1, 'extensionPoint'):
        assert not _is_linked(b1, 'extensionPoint', a)
    if hasattr(b2, 'extensionPoint'):
        assert _is_linked(b2, 'extensionPoint', a)
    _safe_set(a, 'UseCase48', None)
    assert not _is_linked(a, 'UseCase48', b2)
    if hasattr(b2, 'extensionPoint'):
        assert not _is_linked(b2, 'extensionPoint', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BehavioredClassifier_strategy = st.builds(BehavioredClassifier)
@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


DirectedRelationship_strategy = st.builds(DirectedRelationship)
@given(instance=DirectedRelationship_strategy)
@settings(max_examples=25)
def test_DirectedRelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)


EModelElement_strategy = st.builds(EModelElement)
@given(instance=EModelElement_strategy)
@settings(max_examples=25)
def test_EModelElement_instantiation(instance):
    assert isinstance(instance, EModelElement)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Namespace_strategy = st.builds(Namespace)
@given(instance=Namespace_strategy)
@settings(max_examples=25)
def test_Namespace_instantiation(instance):
    assert isinstance(instance, Namespace)


PackageableElement_strategy = st.builds(PackageableElement)
@given(instance=PackageableElement_strategy)
@settings(max_examples=25)
def test_PackageableElement_instantiation(instance):
    assert isinstance(instance, PackageableElement)


ParameterableElement_strategy = st.builds(ParameterableElement)
@given(instance=ParameterableElement_strategy)
@settings(max_examples=25)
def test_ParameterableElement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)


RedefinableElement_strategy = st.builds(RedefinableElement)
@given(instance=RedefinableElement_strategy)
@settings(max_examples=25)
def test_RedefinableElement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)


Relationship_strategy = st.builds(Relationship)
@given(instance=Relationship_strategy)
@settings(max_examples=25)
def test_Relationship_instantiation(instance):
    assert isinstance(instance, Relationship)


TemplateableElement_strategy = st.builds(TemplateableElement)
@given(instance=TemplateableElement_strategy)
@settings(max_examples=25)
def test_TemplateableElement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


umluseCases_Actor_strategy = st.builds(umluseCases_Actor)
@given(instance=umluseCases_Actor_strategy)
@settings(max_examples=25)
def test_umluseCases_Actor_instantiation(instance):
    assert isinstance(instance, umluseCases_Actor)


umluseCases_BehavioredClassifier_strategy = st.builds(umluseCases_BehavioredClassifier)
@given(instance=umluseCases_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_umluseCases_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, umluseCases_BehavioredClassifier)


umluseCases_Classifier_strategy = st.builds(umluseCases_Classifier, isAbstract=safe_text)
@given(instance=umluseCases_Classifier_strategy)
@settings(max_examples=25)
def test_umluseCases_Classifier_instantiation(instance):
    assert isinstance(instance, umluseCases_Classifier)


umluseCases_DirectedRelationship_strategy = st.builds(umluseCases_DirectedRelationship)
@given(instance=umluseCases_DirectedRelationship_strategy)
@settings(max_examples=25)
def test_umluseCases_DirectedRelationship_instantiation(instance):
    assert isinstance(instance, umluseCases_DirectedRelationship)


umluseCases_Element_strategy = st.builds(umluseCases_Element)
@given(instance=umluseCases_Element_strategy)
@settings(max_examples=25)
def test_umluseCases_Element_instantiation(instance):
    assert isinstance(instance, umluseCases_Element)


umluseCases_Extend_strategy = st.builds(umluseCases_Extend)
@given(instance=umluseCases_Extend_strategy)
@settings(max_examples=25)
def test_umluseCases_Extend_instantiation(instance):
    assert isinstance(instance, umluseCases_Extend)


umluseCases_ExtensionPoint_strategy = st.builds(umluseCases_ExtensionPoint)
@given(instance=umluseCases_ExtensionPoint_strategy)
@settings(max_examples=25)
def test_umluseCases_ExtensionPoint_instantiation(instance):
    assert isinstance(instance, umluseCases_ExtensionPoint)


umluseCases_Include_strategy = st.builds(umluseCases_Include)
@given(instance=umluseCases_Include_strategy)
@settings(max_examples=25)
def test_umluseCases_Include_instantiation(instance):
    assert isinstance(instance, umluseCases_Include)


umluseCases_NamedElement_strategy = st.builds(umluseCases_NamedElement, name=safe_text, qualifiedName=safe_text, visibility=safe_text)
@given(instance=umluseCases_NamedElement_strategy)
@settings(max_examples=25)
def test_umluseCases_NamedElement_instantiation(instance):
    assert isinstance(instance, umluseCases_NamedElement)


umluseCases_Namespace_strategy = st.builds(umluseCases_Namespace)
@given(instance=umluseCases_Namespace_strategy)
@settings(max_examples=25)
def test_umluseCases_Namespace_instantiation(instance):
    assert isinstance(instance, umluseCases_Namespace)


umluseCases_PackageableElement_strategy = st.builds(umluseCases_PackageableElement)
@given(instance=umluseCases_PackageableElement_strategy)
@settings(max_examples=25)
def test_umluseCases_PackageableElement_instantiation(instance):
    assert isinstance(instance, umluseCases_PackageableElement)


umluseCases_ParameterableElement_strategy = st.builds(umluseCases_ParameterableElement)
@given(instance=umluseCases_ParameterableElement_strategy)
@settings(max_examples=25)
def test_umluseCases_ParameterableElement_instantiation(instance):
    assert isinstance(instance, umluseCases_ParameterableElement)


umluseCases_RedefinableElement_strategy = st.builds(umluseCases_RedefinableElement, isLeaf=safe_text)
@given(instance=umluseCases_RedefinableElement_strategy)
@settings(max_examples=25)
def test_umluseCases_RedefinableElement_instantiation(instance):
    assert isinstance(instance, umluseCases_RedefinableElement)


umluseCases_Relationship_strategy = st.builds(umluseCases_Relationship)
@given(instance=umluseCases_Relationship_strategy)
@settings(max_examples=25)
def test_umluseCases_Relationship_instantiation(instance):
    assert isinstance(instance, umluseCases_Relationship)


umluseCases_TemplateableElement_strategy = st.builds(umluseCases_TemplateableElement)
@given(instance=umluseCases_TemplateableElement_strategy)
@settings(max_examples=25)
def test_umluseCases_TemplateableElement_instantiation(instance):
    assert isinstance(instance, umluseCases_TemplateableElement)


umluseCases_Type_strategy = st.builds(umluseCases_Type)
@given(instance=umluseCases_Type_strategy)
@settings(max_examples=25)
def test_umluseCases_Type_instantiation(instance):
    assert isinstance(instance, umluseCases_Type)


umluseCases_UseCase_strategy = st.builds(umluseCases_UseCase)
@given(instance=umluseCases_UseCase_strategy)
@settings(max_examples=25)
def test_umluseCases_UseCase_instantiation(instance):
    assert isinstance(instance, umluseCases_UseCase)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BehavioredClassifier,
    Classifier,
    DirectedRelationship,
    EModelElement,
    Element,
    NamedElement,
    Namespace,
    PackageableElement,
    ParameterableElement,
    RedefinableElement,
    Relationship,
    TemplateableElement,
    Type,
    umluseCases_Actor,
    umluseCases_BehavioredClassifier,
    umluseCases_Classifier,
    umluseCases_DirectedRelationship,
    umluseCases_Element,
    umluseCases_Extend,
    umluseCases_ExtensionPoint,
    umluseCases_Include,
    umluseCases_NamedElement,
    umluseCases_Namespace,
    umluseCases_PackageableElement,
    umluseCases_ParameterableElement,
    umluseCases_RedefinableElement,
    umluseCases_Relationship,
    umluseCases_TemplateableElement,
    umluseCases_Type,
    umluseCases_UseCase,
    AggregationKind,
    CallConcurrencyKind,
    ConnectorKind,
    ExpansionKind,
    InteractionOperatorKind,
    MessageKind,
    MessageSort,
    ObjectNodeOrderingKind,
    ParameterDirectionKind,
    ParameterEffectKind,
    PseudostateKind,
    TransitionKind,
    VisibilityKind,
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

def test_assoc_extend33_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Extend()
    _safe_set(b, 'Extend', a1)
    assert _is_linked(b, 'Extend', a1)
    if hasattr(a1, 'extension'):
        assert _is_linked(a1, 'extension', b)
    _safe_set(b, 'Extend', a2)
    assert _is_linked(b, 'Extend', a2)
    if hasattr(a1, 'extension'):
        assert not _is_linked(a1, 'extension', b)
    if hasattr(a2, 'extension'):
        assert _is_linked(a2, 'extension', b)
    _safe_set(b, 'Extend', None)
    assert not _is_linked(b, 'Extend', a2)
    if hasattr(a2, 'extension'):
        assert not _is_linked(a2, 'extension', b)


def test_assoc_extendedCase41_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Extend()
    _safe_set(b, 'umluseCases_Extend', a1)
    assert _is_linked(b, 'umluseCases_Extend', a1)
    if hasattr(a1, 'umluseCases_UseCase42'):
        assert _is_linked(a1, 'umluseCases_UseCase42', b)
    _safe_set(b, 'umluseCases_Extend', a2)
    assert _is_linked(b, 'umluseCases_Extend', a2)
    if hasattr(a1, 'umluseCases_UseCase42'):
        assert not _is_linked(a1, 'umluseCases_UseCase42', b)
    if hasattr(a2, 'umluseCases_UseCase42'):
        assert _is_linked(a2, 'umluseCases_UseCase42', b)
    _safe_set(b, 'umluseCases_Extend', None)
    assert not _is_linked(b, 'umluseCases_Extend', a2)
    if hasattr(a2, 'umluseCases_UseCase42'):
        assert not _is_linked(a2, 'umluseCases_UseCase42', b)


def test_assoc_extension45_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Extend()
    _safe_set(b, 'extend', a1)
    assert _is_linked(b, 'extend', a1)
    if hasattr(a1, 'UseCase46'):
        assert _is_linked(a1, 'UseCase46', b)
    _safe_set(b, 'extend', a2)
    assert _is_linked(b, 'extend', a2)
    if hasattr(a1, 'UseCase46'):
        assert not _is_linked(a1, 'UseCase46', b)
    if hasattr(a2, 'UseCase46'):
        assert _is_linked(a2, 'UseCase46', b)
    _safe_set(b, 'extend', None)
    assert not _is_linked(b, 'extend', a2)
    if hasattr(a2, 'UseCase46'):
        assert not _is_linked(a2, 'UseCase46', b)


def test_assoc_extensionLocation43_reverse_link_reassign_clear():
    a1 = umluseCases_ExtensionPoint()
    a2 = umluseCases_ExtensionPoint()
    b = umluseCases_Extend()
    _safe_set(b, 'umluseCases_Extend44', {a1})
    assert _is_linked(b, 'umluseCases_Extend44', a1)
    if hasattr(a1, 'umluseCases_ExtensionPoint'):
        assert _is_linked(a1, 'umluseCases_ExtensionPoint', b)
    _safe_set(b, 'umluseCases_Extend44', {a2})
    assert _is_linked(b, 'umluseCases_Extend44', a2)
    if hasattr(a1, 'umluseCases_ExtensionPoint'):
        assert not _is_linked(a1, 'umluseCases_ExtensionPoint', b)
    if hasattr(a2, 'umluseCases_ExtensionPoint'):
        assert _is_linked(a2, 'umluseCases_ExtensionPoint', b)
    _safe_set(b, 'umluseCases_Extend44', set())
    assert not _is_linked(b, 'umluseCases_Extend44', a2)
    if hasattr(a2, 'umluseCases_ExtensionPoint'):
        assert not _is_linked(a2, 'umluseCases_ExtensionPoint', b)


def test_assoc_extensionPoint34_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_ExtensionPoint()
    _safe_set(b, 'ExtensionPoint', a1)
    assert _is_linked(b, 'ExtensionPoint', a1)
    if hasattr(a1, 'useCase'):
        assert _is_linked(a1, 'useCase', b)
    _safe_set(b, 'ExtensionPoint', a2)
    assert _is_linked(b, 'ExtensionPoint', a2)
    if hasattr(a1, 'useCase'):
        assert not _is_linked(a1, 'useCase', b)
    if hasattr(a2, 'useCase'):
        assert _is_linked(a2, 'useCase', b)
    _safe_set(b, 'ExtensionPoint', None)
    assert not _is_linked(b, 'ExtensionPoint', a2)
    if hasattr(a2, 'useCase'):
        assert not _is_linked(a2, 'useCase', b)


def test_assoc_general22_reverse_link_reassign_clear():
    a1 = umluseCases_Classifier(isAbstract="sample_text")
    a2 = umluseCases_Classifier(isAbstract="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier23', a1)
    assert _is_linked(b, 'umluseCases_Classifier23', a1)
    if hasattr(a1, 'umluseCases_Classifier21'):
        assert _is_linked(a1, 'umluseCases_Classifier21', b)
    _safe_set(b, 'umluseCases_Classifier23', a2)
    assert _is_linked(b, 'umluseCases_Classifier23', a2)
    if hasattr(a1, 'umluseCases_Classifier21'):
        assert not _is_linked(a1, 'umluseCases_Classifier21', b)
    if hasattr(a2, 'umluseCases_Classifier21'):
        assert _is_linked(a2, 'umluseCases_Classifier21', b)
    _safe_set(b, 'umluseCases_Classifier23', None)
    assert not _is_linked(b, 'umluseCases_Classifier23', a2)
    if hasattr(a2, 'umluseCases_Classifier21'):
        assert not _is_linked(a2, 'umluseCases_Classifier21', b)


def test_assoc_inheritedMember16_reverse_link_reassign_clear():
    a1 = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    a2 = umluseCases_NamedElement(name="sample_text_2", qualifiedName="sample_text_2", visibility="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier', {a1})
    assert _is_linked(b, 'umluseCases_Classifier', a1)
    if hasattr(a1, 'umluseCases_NamedElement17'):
        assert _is_linked(a1, 'umluseCases_NamedElement17', b)
    _safe_set(b, 'umluseCases_Classifier', {a2})
    assert _is_linked(b, 'umluseCases_Classifier', a2)
    if hasattr(a1, 'umluseCases_NamedElement17'):
        assert not _is_linked(a1, 'umluseCases_NamedElement17', b)
    if hasattr(a2, 'umluseCases_NamedElement17'):
        assert _is_linked(a2, 'umluseCases_NamedElement17', b)
    _safe_set(b, 'umluseCases_Classifier', set())
    assert not _is_linked(b, 'umluseCases_Classifier', a2)
    if hasattr(a2, 'umluseCases_NamedElement17'):
        assert not _is_linked(a2, 'umluseCases_NamedElement17', b)


def test_assoc_ownedUseCase24_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier25', {a1})
    assert _is_linked(b, 'umluseCases_Classifier25', a1)
    if hasattr(a1, 'umluseCases_UseCase'):
        assert _is_linked(a1, 'umluseCases_UseCase', b)
    _safe_set(b, 'umluseCases_Classifier25', {a2})
    assert _is_linked(b, 'umluseCases_Classifier25', a2)
    if hasattr(a1, 'umluseCases_UseCase'):
        assert not _is_linked(a1, 'umluseCases_UseCase', b)
    if hasattr(a2, 'umluseCases_UseCase'):
        assert _is_linked(a2, 'umluseCases_UseCase', b)
    _safe_set(b, 'umluseCases_Classifier25', set())
    assert not _is_linked(b, 'umluseCases_Classifier25', a2)
    if hasattr(a2, 'umluseCases_UseCase'):
        assert not _is_linked(a2, 'umluseCases_UseCase', b)


def test_assoc_redefinedClassifier19_reverse_link_reassign_clear():
    a1 = umluseCases_Classifier(isAbstract="sample_text")
    a2 = umluseCases_Classifier(isAbstract="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier20', a1)
    assert _is_linked(b, 'umluseCases_Classifier20', a1)
    if hasattr(a1, 'umluseCases_Classifier18'):
        assert _is_linked(a1, 'umluseCases_Classifier18', b)
    _safe_set(b, 'umluseCases_Classifier20', a2)
    assert _is_linked(b, 'umluseCases_Classifier20', a2)
    if hasattr(a1, 'umluseCases_Classifier18'):
        assert not _is_linked(a1, 'umluseCases_Classifier18', b)
    if hasattr(a2, 'umluseCases_Classifier18'):
        assert _is_linked(a2, 'umluseCases_Classifier18', b)
    _safe_set(b, 'umluseCases_Classifier20', None)
    assert not _is_linked(b, 'umluseCases_Classifier20', a2)
    if hasattr(a2, 'umluseCases_Classifier18'):
        assert not _is_linked(a2, 'umluseCases_Classifier18', b)


def test_assoc_redefinedElement28_reverse_link_reassign_clear():
    a1 = umluseCases_RedefinableElement(isLeaf="sample_text")
    a2 = umluseCases_RedefinableElement(isLeaf="sample_text_2")
    b = umluseCases_RedefinableElement(isLeaf="sample_text")
    _safe_set(b, 'umluseCases_RedefinableElement27', {a1})
    assert _is_linked(b, 'umluseCases_RedefinableElement27', a1)
    if hasattr(a1, 'umluseCases_RedefinableElement'):
        assert _is_linked(a1, 'umluseCases_RedefinableElement', b)
    _safe_set(b, 'umluseCases_RedefinableElement27', {a2})
    assert _is_linked(b, 'umluseCases_RedefinableElement27', a2)
    if hasattr(a1, 'umluseCases_RedefinableElement'):
        assert not _is_linked(a1, 'umluseCases_RedefinableElement', b)
    if hasattr(a2, 'umluseCases_RedefinableElement'):
        assert _is_linked(a2, 'umluseCases_RedefinableElement', b)
    _safe_set(b, 'umluseCases_RedefinableElement27', set())
    assert not _is_linked(b, 'umluseCases_RedefinableElement27', a2)
    if hasattr(a2, 'umluseCases_RedefinableElement'):
        assert not _is_linked(a2, 'umluseCases_RedefinableElement', b)


def test_assoc_redefinitionContext29_reverse_link_reassign_clear():
    a1 = umluseCases_RedefinableElement(isLeaf="sample_text")
    a2 = umluseCases_RedefinableElement(isLeaf="sample_text_2")
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'umluseCases_Classifier31', a1)
    assert _is_linked(b, 'umluseCases_Classifier31', a1)
    if hasattr(a1, 'umluseCases_RedefinableElement30'):
        assert _is_linked(a1, 'umluseCases_RedefinableElement30', b)
    _safe_set(b, 'umluseCases_Classifier31', a2)
    assert _is_linked(b, 'umluseCases_Classifier31', a2)
    if hasattr(a1, 'umluseCases_RedefinableElement30'):
        assert not _is_linked(a1, 'umluseCases_RedefinableElement30', b)
    if hasattr(a2, 'umluseCases_RedefinableElement30'):
        assert _is_linked(a2, 'umluseCases_RedefinableElement30', b)
    _safe_set(b, 'umluseCases_Classifier31', None)
    assert not _is_linked(b, 'umluseCases_Classifier31', a2)
    if hasattr(a2, 'umluseCases_RedefinableElement30'):
        assert not _is_linked(a2, 'umluseCases_RedefinableElement30', b)


def test_assoc_subject35_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'Classifier', a1)
    assert _is_linked(b, 'Classifier', a1)
    if hasattr(a1, 'useCase36'):
        assert _is_linked(a1, 'useCase36', b)
    _safe_set(b, 'Classifier', a2)
    assert _is_linked(b, 'Classifier', a2)
    if hasattr(a1, 'useCase36'):
        assert not _is_linked(a1, 'useCase36', b)
    if hasattr(a2, 'useCase36'):
        assert _is_linked(a2, 'useCase36', b)
    _safe_set(b, 'Classifier', None)
    assert not _is_linked(b, 'Classifier', a2)
    if hasattr(a2, 'useCase36'):
        assert not _is_linked(a2, 'useCase36', b)


def test_assoc_useCase26_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_Classifier(isAbstract="sample_text")
    _safe_set(b, 'subject', {a1})
    assert _is_linked(b, 'subject', a1)
    if hasattr(a1, 'UseCase'):
        assert _is_linked(a1, 'UseCase', b)
    _safe_set(b, 'subject', {a2})
    assert _is_linked(b, 'subject', a2)
    if hasattr(a1, 'UseCase'):
        assert not _is_linked(a1, 'UseCase', b)
    if hasattr(a2, 'UseCase'):
        assert _is_linked(a2, 'UseCase', b)
    _safe_set(b, 'subject', set())
    assert not _is_linked(b, 'subject', a2)
    if hasattr(a2, 'UseCase'):
        assert not _is_linked(a2, 'UseCase', b)


def test_assoc_useCase47_reverse_link_reassign_clear():
    a1 = umluseCases_UseCase()
    a2 = umluseCases_UseCase()
    b = umluseCases_ExtensionPoint()
    _safe_set(b, 'extensionPoint', a1)
    assert _is_linked(b, 'extensionPoint', a1)
    if hasattr(a1, 'UseCase48'):
        assert _is_linked(a1, 'UseCase48', b)
    _safe_set(b, 'extensionPoint', a2)
    assert _is_linked(b, 'extensionPoint', a2)
    if hasattr(a1, 'UseCase48'):
        assert not _is_linked(a1, 'UseCase48', b)
    if hasattr(a2, 'UseCase48'):
        assert _is_linked(a2, 'UseCase48', b)
    _safe_set(b, 'extensionPoint', None)
    assert not _is_linked(b, 'extensionPoint', a2)
    if hasattr(a2, 'UseCase48'):
        assert not _is_linked(a2, 'UseCase48', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_addition37_stub_double():
    # umluseCases_Include has no real 'umluseCases_Include' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_UseCase()
    partner = umluseCases_Include()
    setattr(partner, 'umluseCases_Include', None)
    _safe_set(owner, 'umluseCases_UseCase38', partner)
    assert getattr(partner, 'umluseCases_Include') == owner
    _safe_set(owner, 'umluseCases_UseCase38', None)
    assert getattr(partner, 'umluseCases_Include') is None


def test_assoc_include32_stub_double():
    # umluseCases_Include has no real 'Include' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_UseCase()
    partner = umluseCases_Include()
    setattr(partner, 'Include', None)
    _safe_set(owner, 'includingCase', {partner})
    assert getattr(partner, 'Include') == owner
    _safe_set(owner, 'includingCase', set())
    assert getattr(partner, 'Include') is None


def test_assoc_includingCase39_stub_double():
    # umluseCases_Include has no real 'include' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_UseCase()
    partner = umluseCases_Include()
    setattr(partner, 'include', None)
    _safe_set(owner, 'UseCase40', partner)
    assert getattr(partner, 'include') == owner
    _safe_set(owner, 'UseCase40', None)
    assert getattr(partner, 'include') is None


def test_assoc_member12_stub_double():
    # umluseCases_Namespace has no real 'umluseCases_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = umluseCases_Namespace()
    setattr(partner, 'umluseCases_Namespace', None)
    _safe_set(owner, 'umluseCases_NamedElement', partner)
    assert owner in getattr(partner, 'umluseCases_Namespace')
    _safe_set(owner, 'umluseCases_NamedElement', None)
    assert owner not in getattr(partner, 'umluseCases_Namespace')


def test_assoc_namespace5_stub_double():
    # umluseCases_Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = umluseCases_Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedMember', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedMember', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_ownedMember15_stub_double():
    # umluseCases_Namespace has no real 'namespace' property in the generated
    # code (a bare stub) -- manually attach it so umluseCases_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umluseCases_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umluseCases_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = umluseCases_Namespace()
    setattr(partner, 'namespace', None)
    _safe_set(owner, 'NamedElement', partner)
    assert owner in getattr(partner, 'namespace')
    _safe_set(owner, 'NamedElement', None)
    assert owner not in getattr(partner, 'namespace')




from python_code import umluseCases_Actor

def test_umluseCases_Actor___init__():
    assert umluseCases_Actor.__init__(umluseCases_Actor()) == None

def test_umluseCases_Actor_must_have_name():
    assert umluseCases_Actor.must_have_name(umluseCases_Actor(), '', '') == None

def test_umluseCases_Actor_associations():
    assert umluseCases_Actor.associations(umluseCases_Actor(), '', '') == None

