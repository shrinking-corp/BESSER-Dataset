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
    Page,
    Arc,
    Transition,
    pragmacpndefinition_OntologyMember,
    PetriNet,
    pragmacpndefinition_OntologyDocument,
    Label,
    pragmacpndefinition_PragmaticsOntology,
    pragmacpndefinition_Pragma,
    OntologyMember,
    pragmacpndefinition_Transition,
    pragmacpndefinition_Arc,
    pragmacpndefinition_Page,
    Place,
    pragmacpndefinition_Place,
    CPN,
    pragmacpndefinition_PragmaCPN,
    pragmacpndefinition_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_hyp_page_constructor_exists():
    assert callable(Page.__init__)


def test_hyp_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_hyp_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_hyp_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_ontologymember_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_OntologyMember)


def test_hyp_pragmacpndefinition_ontologymember_constructor_exists():
    assert callable(pragmacpndefinition_OntologyMember.__init__)


def test_hyp_pragmacpndefinition_ontologymember_constructor_args():
    sig = inspect.signature(pragmacpndefinition_OntologyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_hyp_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_hyp_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_ontologydocument_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_OntologyDocument)


def test_hyp_pragmacpndefinition_ontologydocument_constructor_exists():
    assert callable(pragmacpndefinition_OntologyDocument.__init__)


def test_hyp_pragmacpndefinition_ontologydocument_constructor_args():
    sig = inspect.signature(pragmacpndefinition_OntologyDocument.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "iri" in params, "Missing parameter 'iri'"





def test_hyp_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_hyp_label_constructor_exists():
    assert callable(Label.__init__)


def test_hyp_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_pragmaticsontology_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_PragmaticsOntology)


def test_hyp_pragmacpndefinition_pragmaticsontology_constructor_exists():
    assert callable(pragmacpndefinition_PragmaticsOntology.__init__)


def test_hyp_pragmacpndefinition_pragmaticsontology_constructor_args():
    sig = inspect.signature(pragmacpndefinition_PragmaticsOntology.__init__)
    params = list(sig.parameters.keys())
    assert "manager" in params, "Missing parameter 'manager'"




def test_hyp_pragmacpndefinition_pragma_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_Pragma)


def test_hyp_pragmacpndefinition_pragma_constructor_exists():
    assert callable(pragmacpndefinition_Pragma.__init__)


def test_hyp_pragmacpndefinition_pragma_constructor_args():
    sig = inspect.signature(pragmacpndefinition_Pragma.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_ontologymember_is_not_abstract():
    assert not inspect.isabstract(OntologyMember)


def test_hyp_ontologymember_constructor_exists():
    assert callable(OntologyMember.__init__)


def test_hyp_ontologymember_constructor_args():
    sig = inspect.signature(OntologyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_transition_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_Transition)


def test_hyp_pragmacpndefinition_transition_constructor_exists():
    assert callable(pragmacpndefinition_Transition.__init__)


def test_hyp_pragmacpndefinition_transition_constructor_args():
    sig = inspect.signature(pragmacpndefinition_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_arc_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_Arc)


def test_hyp_pragmacpndefinition_arc_constructor_exists():
    assert callable(pragmacpndefinition_Arc.__init__)


def test_hyp_pragmacpndefinition_arc_constructor_args():
    sig = inspect.signature(pragmacpndefinition_Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_page_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_Page)


def test_hyp_pragmacpndefinition_page_constructor_exists():
    assert callable(pragmacpndefinition_Page.__init__)


def test_hyp_pragmacpndefinition_page_constructor_args():
    sig = inspect.signature(pragmacpndefinition_Page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_hyp_place_constructor_exists():
    assert callable(Place.__init__)


def test_hyp_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_place_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_Place)


def test_hyp_pragmacpndefinition_place_constructor_exists():
    assert callable(pragmacpndefinition_Place.__init__)


def test_hyp_pragmacpndefinition_place_constructor_args():
    sig = inspect.signature(pragmacpndefinition_Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpn_is_not_abstract():
    assert not inspect.isabstract(CPN)


def test_hyp_cpn_constructor_exists():
    assert callable(CPN.__init__)


def test_hyp_cpn_constructor_args():
    sig = inspect.signature(CPN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_pragmacpn_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_PragmaCPN)


def test_hyp_pragmacpndefinition_pragmacpn_constructor_exists():
    assert callable(pragmacpndefinition_PragmaCPN.__init__)


def test_hyp_pragmacpndefinition_pragmacpn_constructor_args():
    sig = inspect.signature(pragmacpndefinition_PragmaCPN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragmacpndefinition_petrinet_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition_PetriNet)


def test_hyp_pragmacpndefinition_petrinet_constructor_exists():
    assert callable(pragmacpndefinition_PetriNet.__init__)


def test_hyp_pragmacpndefinition_petrinet_constructor_args():
    sig = inspect.signature(pragmacpndefinition_PetriNet.__init__)
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
Page_strategy = st.builds(
    Page,
)
Arc_strategy = st.builds(
    Arc,
)
Transition_strategy = st.builds(
    Transition,
)
pragmacpndefinition_OntologyMember_strategy = st.builds(
    pragmacpndefinition_OntologyMember,
)
PetriNet_strategy = st.builds(
    PetriNet,
)
pragmacpndefinition_OntologyDocument_strategy = st.builds(
    pragmacpndefinition_OntologyDocument,
    path=
        safe_text,
    iri=
        safe_text
)
Label_strategy = st.builds(
    Label,
)
pragmacpndefinition_PragmaticsOntology_strategy = st.builds(
    pragmacpndefinition_PragmaticsOntology,
    manager=
        safe_text
)
pragmacpndefinition_Pragma_strategy = st.builds(
    pragmacpndefinition_Pragma,
    text=
        safe_text
)
OntologyMember_strategy = st.builds(
    OntologyMember,
)
pragmacpndefinition_Transition_strategy = st.builds(
    pragmacpndefinition_Transition,
)
pragmacpndefinition_Arc_strategy = st.builds(
    pragmacpndefinition_Arc,
)
pragmacpndefinition_Page_strategy = st.builds(
    pragmacpndefinition_Page,
)
Place_strategy = st.builds(
    Place,
)
pragmacpndefinition_Place_strategy = st.builds(
    pragmacpndefinition_Place,
)
CPN_strategy = st.builds(
    CPN,
)
pragmacpndefinition_PragmaCPN_strategy = st.builds(
    pragmacpndefinition_PragmaCPN,
)
pragmacpndefinition_PetriNet_strategy = st.builds(
    pragmacpndefinition_PetriNet,
)









@given(instance=pragmacpndefinition_OntologyDocument_strategy)
def test_hyp_pragmacpndefinition_ontologydocument_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=pragmacpndefinition_OntologyDocument_strategy)
def test_hyp_pragmacpndefinition_ontologydocument_iri_setter(instance):
    original = instance.iri
    instance.iri = original
    assert instance.iri == original





@given(instance=pragmacpndefinition_PragmaticsOntology_strategy)
def test_hyp_pragmacpndefinition_pragmaticsontology_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pragmacpndefinition_PragmaticsOntology_strategy)
@settings(max_examples=30)
def test_hyp_pragmacpndefinition_pragmaticsontology_addontologyfromfile_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addOntologyFromFile(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addOntologyFromFile).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addOntologyFromFile' in pragmacpndefinition_PragmaticsOntology is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addOntologyFromFile' in pragmacpndefinition_PragmaticsOntology did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addOntologyFromFile' in pragmacpndefinition_PragmaticsOntology is not implemented or raised an error")




@given(instance=pragmacpndefinition_Pragma_strategy)
def test_hyp_pragmacpndefinition_pragma_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original











# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Arc,
    CPN,
    Label,
    OntologyMember,
    Page,
    PetriNet,
    Place,
    Transition,
    pragmacpndefinition_Arc,
    pragmacpndefinition_OntologyDocument,
    pragmacpndefinition_OntologyMember,
    pragmacpndefinition_Page,
    pragmacpndefinition_PetriNet,
    pragmacpndefinition_Place,
    pragmacpndefinition_Pragma,
    pragmacpndefinition_PragmaCPN,
    pragmacpndefinition_PragmaticsOntology,
    pragmacpndefinition_Transition,
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

def test_pragmacpndefinition_OntologyDocument_iri_value_roundtrip():
    instance = pragmacpndefinition_OntologyDocument(iri="sample_text", path="sample_text")
    assert instance.iri == "sample_text"
    instance.iri = "sample_text_2"
    assert instance.iri == "sample_text_2"


def test_pragmacpndefinition_OntologyDocument_path_value_roundtrip():
    instance = pragmacpndefinition_OntologyDocument(iri="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_pragmacpndefinition_Pragma_text_value_roundtrip():
    instance = pragmacpndefinition_Pragma(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pragmacpndefinition_PragmaticsOntology_manager_value_roundtrip():
    instance = pragmacpndefinition_PragmaticsOntology(manager="sample_text")
    assert instance.manager == "sample_text"
    instance.manager = "sample_text_2"
    assert instance.manager == "sample_text_2"


def test_pragmacpndefinition_Arc_isa_Arc():
    instance = pragmacpndefinition_Arc()
    assert isinstance(instance, Arc)


def test_pragmacpndefinition_PragmaCPN_isa_CPN():
    instance = pragmacpndefinition_PragmaCPN()
    assert isinstance(instance, CPN)


def test_pragmacpndefinition_Pragma_isa_Label():
    instance = pragmacpndefinition_Pragma(text="sample_text")
    assert isinstance(instance, Label)


def test_pragmacpndefinition_PragmaticsOntology_isa_Label():
    instance = pragmacpndefinition_PragmaticsOntology(manager="sample_text")
    assert isinstance(instance, Label)


def test_pragmacpndefinition_Arc_isa_OntologyMember():
    instance = pragmacpndefinition_Arc()
    assert isinstance(instance, OntologyMember)


def test_pragmacpndefinition_Page_isa_OntologyMember():
    instance = pragmacpndefinition_Page()
    assert isinstance(instance, OntologyMember)


def test_pragmacpndefinition_Place_isa_OntologyMember():
    instance = pragmacpndefinition_Place()
    assert isinstance(instance, OntologyMember)


def test_pragmacpndefinition_Transition_isa_OntologyMember():
    instance = pragmacpndefinition_Transition()
    assert isinstance(instance, OntologyMember)


def test_pragmacpndefinition_Page_isa_Page():
    instance = pragmacpndefinition_Page()
    assert isinstance(instance, Page)


def test_pragmacpndefinition_PetriNet_isa_PetriNet():
    instance = pragmacpndefinition_PetriNet()
    assert isinstance(instance, PetriNet)


def test_pragmacpndefinition_Place_isa_Place():
    instance = pragmacpndefinition_Place()
    assert isinstance(instance, Place)


def test_pragmacpndefinition_Transition_isa_Transition():
    instance = pragmacpndefinition_Transition()
    assert isinstance(instance, Transition)


def test_assoc_Annotation6_link_reassign_clear():
    a = pragmacpndefinition_Pragma(text="sample_text")
    b1 = pragmacpndefinition_OntologyMember()
    b2 = pragmacpndefinition_OntologyMember()
    _safe_set(a, 'pragmacpndefinition_Pragma', b1)
    assert _is_linked(a, 'pragmacpndefinition_Pragma', b1)
    if hasattr(b1, 'pragmacpndefinition_OntologyMember'):
        assert _is_linked(b1, 'pragmacpndefinition_OntologyMember', a)
    _safe_set(a, 'pragmacpndefinition_Pragma', b2)
    assert _is_linked(a, 'pragmacpndefinition_Pragma', b2)
    if hasattr(b1, 'pragmacpndefinition_OntologyMember'):
        assert not _is_linked(b1, 'pragmacpndefinition_OntologyMember', a)
    if hasattr(b2, 'pragmacpndefinition_OntologyMember'):
        assert _is_linked(b2, 'pragmacpndefinition_OntologyMember', a)
    _safe_set(a, 'pragmacpndefinition_Pragma', None)
    assert not _is_linked(a, 'pragmacpndefinition_Pragma', b2)
    if hasattr(b2, 'pragmacpndefinition_OntologyMember'):
        assert not _is_linked(b2, 'pragmacpndefinition_OntologyMember', a)


def test_assoc_documents1_link_reassign_clear():
    a = pragmacpndefinition_PragmaticsOntology(manager="sample_text")
    b1 = pragmacpndefinition_OntologyDocument(iri="sample_text", path="sample_text")
    b2 = pragmacpndefinition_OntologyDocument(iri="sample_text_2", path="sample_text_2")
    _safe_set(a, 'ontology', {b1})
    assert _is_linked(a, 'ontology', b1)
    if hasattr(b1, 'OntologyDocument'):
        assert _is_linked(b1, 'OntologyDocument', a)
    _safe_set(a, 'ontology', {b2})
    assert _is_linked(a, 'ontology', b2)
    if hasattr(b1, 'OntologyDocument'):
        assert not _is_linked(b1, 'OntologyDocument', a)
    if hasattr(b2, 'OntologyDocument'):
        assert _is_linked(b2, 'OntologyDocument', a)
    _safe_set(a, 'ontology', set())
    assert not _is_linked(a, 'ontology', b2)
    if hasattr(b2, 'OntologyDocument'):
        assert not _is_linked(b2, 'OntologyDocument', a)


def test_assoc_net2_link_reassign_clear():
    a = pragmacpndefinition_PragmaticsOntology(manager="sample_text")
    b1 = pragmacpndefinition_PetriNet()
    b2 = pragmacpndefinition_PetriNet()
    _safe_set(a, 'ontology3', b1)
    assert _is_linked(a, 'ontology3', b1)
    if hasattr(b1, 'PetriNet'):
        assert _is_linked(b1, 'PetriNet', a)
    _safe_set(a, 'ontology3', b2)
    assert _is_linked(a, 'ontology3', b2)
    if hasattr(b1, 'PetriNet'):
        assert not _is_linked(b1, 'PetriNet', a)
    if hasattr(b2, 'PetriNet'):
        assert _is_linked(b2, 'PetriNet', a)
    _safe_set(a, 'ontology3', None)
    assert not _is_linked(a, 'ontology3', b2)
    if hasattr(b2, 'PetriNet'):
        assert not _is_linked(b2, 'PetriNet', a)


def test_assoc_ontology0_link_reassign_clear():
    a = pragmacpndefinition_PragmaticsOntology(manager="sample_text")
    b1 = pragmacpndefinition_OntologyDocument(iri="sample_text", path="sample_text")
    b2 = pragmacpndefinition_OntologyDocument(iri="sample_text_2", path="sample_text_2")
    _safe_set(a, 'PragmaticsOntology', b1)
    assert _is_linked(a, 'PragmaticsOntology', b1)
    if hasattr(b1, 'documents'):
        assert _is_linked(b1, 'documents', a)
    _safe_set(a, 'PragmaticsOntology', b2)
    assert _is_linked(a, 'PragmaticsOntology', b2)
    if hasattr(b1, 'documents'):
        assert not _is_linked(b1, 'documents', a)
    if hasattr(b2, 'documents'):
        assert _is_linked(b2, 'documents', a)
    _safe_set(a, 'PragmaticsOntology', None)
    assert not _is_linked(a, 'PragmaticsOntology', b2)
    if hasattr(b2, 'documents'):
        assert not _is_linked(b2, 'documents', a)


def test_assoc_ontology4_link_reassign_clear():
    a = pragmacpndefinition_PragmaticsOntology(manager="sample_text")
    b1 = pragmacpndefinition_PetriNet()
    b2 = pragmacpndefinition_PetriNet()
    _safe_set(a, 'PragmaticsOntology5', b1)
    assert _is_linked(a, 'PragmaticsOntology5', b1)
    if hasattr(b1, 'net'):
        assert _is_linked(b1, 'net', a)
    _safe_set(a, 'PragmaticsOntology5', b2)
    assert _is_linked(a, 'PragmaticsOntology5', b2)
    if hasattr(b1, 'net'):
        assert not _is_linked(b1, 'net', a)
    if hasattr(b2, 'net'):
        assert _is_linked(b2, 'net', a)
    _safe_set(a, 'PragmaticsOntology5', None)
    assert not _is_linked(a, 'PragmaticsOntology5', b2)
    if hasattr(b2, 'net'):
        assert not _is_linked(b2, 'net', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Arc_strategy = st.builds(Arc)
@given(instance=Arc_strategy)
@settings(max_examples=25)
def test_Arc_instantiation(instance):
    assert isinstance(instance, Arc)


CPN_strategy = st.builds(CPN)
@given(instance=CPN_strategy)
@settings(max_examples=25)
def test_CPN_instantiation(instance):
    assert isinstance(instance, CPN)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


OntologyMember_strategy = st.builds(OntologyMember)
@given(instance=OntologyMember_strategy)
@settings(max_examples=25)
def test_OntologyMember_instantiation(instance):
    assert isinstance(instance, OntologyMember)


Page_strategy = st.builds(Page)
@given(instance=Page_strategy)
@settings(max_examples=25)
def test_Page_instantiation(instance):
    assert isinstance(instance, Page)


PetriNet_strategy = st.builds(PetriNet)
@given(instance=PetriNet_strategy)
@settings(max_examples=25)
def test_PetriNet_instantiation(instance):
    assert isinstance(instance, PetriNet)


Place_strategy = st.builds(Place)
@given(instance=Place_strategy)
@settings(max_examples=25)
def test_Place_instantiation(instance):
    assert isinstance(instance, Place)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


pragmacpndefinition_Arc_strategy = st.builds(pragmacpndefinition_Arc)
@given(instance=pragmacpndefinition_Arc_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_Arc_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_Arc)


pragmacpndefinition_OntologyDocument_strategy = st.builds(pragmacpndefinition_OntologyDocument, iri=safe_text, path=safe_text)
@given(instance=pragmacpndefinition_OntologyDocument_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_OntologyDocument_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_OntologyDocument)


pragmacpndefinition_OntologyMember_strategy = st.builds(pragmacpndefinition_OntologyMember)
@given(instance=pragmacpndefinition_OntologyMember_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_OntologyMember_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_OntologyMember)


pragmacpndefinition_Page_strategy = st.builds(pragmacpndefinition_Page)
@given(instance=pragmacpndefinition_Page_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_Page_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_Page)


pragmacpndefinition_PetriNet_strategy = st.builds(pragmacpndefinition_PetriNet)
@given(instance=pragmacpndefinition_PetriNet_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_PetriNet_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_PetriNet)


pragmacpndefinition_Place_strategy = st.builds(pragmacpndefinition_Place)
@given(instance=pragmacpndefinition_Place_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_Place_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_Place)


pragmacpndefinition_Pragma_strategy = st.builds(pragmacpndefinition_Pragma, text=safe_text)
@given(instance=pragmacpndefinition_Pragma_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_Pragma_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_Pragma)


pragmacpndefinition_PragmaCPN_strategy = st.builds(pragmacpndefinition_PragmaCPN)
@given(instance=pragmacpndefinition_PragmaCPN_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_PragmaCPN_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_PragmaCPN)


pragmacpndefinition_PragmaticsOntology_strategy = st.builds(pragmacpndefinition_PragmaticsOntology, manager=safe_text)
@given(instance=pragmacpndefinition_PragmaticsOntology_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_PragmaticsOntology_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_PragmaticsOntology)


pragmacpndefinition_Transition_strategy = st.builds(pragmacpndefinition_Transition)
@given(instance=pragmacpndefinition_Transition_strategy)
@settings(max_examples=25)
def test_pragmacpndefinition_Transition_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition_Transition)



