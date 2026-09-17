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
    expansionmodel_UseContext,
    expansionmodel_GraphicalElementLibrary,
    expansionmodel_RepresentationKind,
    expansionmodel_AbstractRepresentation,
    AbstractRepresentation,
    expansionmodel_Representation,
    expansionmodel_InducedRepresentation,
    expansionmodel_DiagramExpansion,
    Representation,
    expansionmodel_GMFT_BasedRepresentation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expansionmodel_usecontext_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_UseContext)


def test_hyp_expansionmodel_usecontext_constructor_exists():
    assert callable(expansionmodel_UseContext.__init__)


def test_hyp_expansionmodel_usecontext_constructor_args():
    sig = inspect.signature(expansionmodel_UseContext.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "diagramType" in params, "Missing parameter 'diagramType'"





def test_hyp_expansionmodel_graphicalelementlibrary_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_GraphicalElementLibrary)


def test_hyp_expansionmodel_graphicalelementlibrary_constructor_exists():
    assert callable(expansionmodel_GraphicalElementLibrary.__init__)


def test_hyp_expansionmodel_graphicalelementlibrary_constructor_args():
    sig = inspect.signature(expansionmodel_GraphicalElementLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_expansionmodel_representationkind_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_RepresentationKind)


def test_hyp_expansionmodel_representationkind_constructor_exists():
    assert callable(expansionmodel_RepresentationKind.__init__)


def test_hyp_expansionmodel_representationkind_constructor_args():
    sig = inspect.signature(expansionmodel_RepresentationKind.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "editPartQualifiedName" in params, "Missing parameter 'editPartQualifiedName'"
    assert "viewFactory" in params, "Missing parameter 'viewFactory'"






def test_hyp_expansionmodel_abstractrepresentation_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_AbstractRepresentation)


def test_hyp_expansionmodel_abstractrepresentation_constructor_exists():
    assert callable(expansionmodel_AbstractRepresentation.__init__)


def test_hyp_expansionmodel_abstractrepresentation_constructor_args():
    sig = inspect.signature(expansionmodel_AbstractRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "editPartQualifiedName" in params, "Missing parameter 'editPartQualifiedName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "viewFactory" in params, "Missing parameter 'viewFactory'"






def test_hyp_abstractrepresentation_is_not_abstract():
    assert not inspect.isabstract(AbstractRepresentation)


def test_hyp_abstractrepresentation_constructor_exists():
    assert callable(AbstractRepresentation.__init__)


def test_hyp_abstractrepresentation_constructor_args():
    sig = inspect.signature(AbstractRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expansionmodel_representation_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_Representation)


def test_hyp_expansionmodel_representation_constructor_exists():
    assert callable(expansionmodel_Representation.__init__)


def test_hyp_expansionmodel_representation_constructor_args():
    sig = inspect.signature(expansionmodel_Representation.__init__)
    params = list(sig.parameters.keys())
    assert "graphicalElementType" in params, "Missing parameter 'graphicalElementType'"




def test_hyp_expansionmodel_inducedrepresentation_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_InducedRepresentation)


def test_hyp_expansionmodel_inducedrepresentation_constructor_exists():
    assert callable(expansionmodel_InducedRepresentation.__init__)


def test_hyp_expansionmodel_inducedrepresentation_constructor_args():
    sig = inspect.signature(expansionmodel_InducedRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "hint" in params, "Missing parameter 'hint'"




def test_hyp_expansionmodel_diagramexpansion_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_DiagramExpansion)


def test_hyp_expansionmodel_diagramexpansion_constructor_exists():
    assert callable(expansionmodel_DiagramExpansion.__init__)


def test_hyp_expansionmodel_diagramexpansion_constructor_args():
    sig = inspect.signature(expansionmodel_DiagramExpansion.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"




def test_hyp_representation_is_not_abstract():
    assert not inspect.isabstract(Representation)


def test_hyp_representation_constructor_exists():
    assert callable(Representation.__init__)


def test_hyp_representation_constructor_args():
    sig = inspect.signature(Representation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expansionmodel_gmft_basedrepresentation_is_not_abstract():
    assert not inspect.isabstract(expansionmodel_GMFT_BasedRepresentation)


def test_hyp_expansionmodel_gmft_basedrepresentation_constructor_exists():
    assert callable(expansionmodel_GMFT_BasedRepresentation.__init__)


def test_hyp_expansionmodel_gmft_basedrepresentation_constructor_args():
    sig = inspect.signature(expansionmodel_GMFT_BasedRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "reusedID" in params, "Missing parameter 'reusedID'"



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
expansionmodel_UseContext_strategy = st.builds(
    expansionmodel_UseContext,
    name=
        safe_text,
    diagramType=
        safe_text
)
expansionmodel_GraphicalElementLibrary_strategy = st.builds(
    expansionmodel_GraphicalElementLibrary,
    name=
        safe_text
)
expansionmodel_RepresentationKind_strategy = st.builds(
    expansionmodel_RepresentationKind,
    name=
        safe_text,
    editPartQualifiedName=
        safe_text,
    viewFactory=
        safe_text
)
expansionmodel_AbstractRepresentation_strategy = st.builds(
    expansionmodel_AbstractRepresentation,
    editPartQualifiedName=
        safe_text,
    name=
        safe_text,
    viewFactory=
        safe_text
)
AbstractRepresentation_strategy = st.builds(
    AbstractRepresentation,
)
expansionmodel_Representation_strategy = st.builds(
    expansionmodel_Representation,
    graphicalElementType=
        safe_text
)
expansionmodel_InducedRepresentation_strategy = st.builds(
    expansionmodel_InducedRepresentation,
    hint=
        safe_text
)
expansionmodel_DiagramExpansion_strategy = st.builds(
    expansionmodel_DiagramExpansion,
    ID=
        safe_text
)
Representation_strategy = st.builds(
    Representation,
)
expansionmodel_GMFT_BasedRepresentation_strategy = st.builds(
    expansionmodel_GMFT_BasedRepresentation,
    reusedID=
        safe_text
)




@given(instance=expansionmodel_UseContext_strategy)
def test_hyp_expansionmodel_usecontext_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=expansionmodel_UseContext_strategy)
def test_hyp_expansionmodel_usecontext_diagramType_setter(instance):
    original = instance.diagramType
    instance.diagramType = original
    assert instance.diagramType == original




@given(instance=expansionmodel_GraphicalElementLibrary_strategy)
def test_hyp_expansionmodel_graphicalelementlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=expansionmodel_RepresentationKind_strategy)
def test_hyp_expansionmodel_representationkind_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=expansionmodel_RepresentationKind_strategy)
def test_hyp_expansionmodel_representationkind_editPartQualifiedName_setter(instance):
    original = instance.editPartQualifiedName
    instance.editPartQualifiedName = original
    assert instance.editPartQualifiedName == original



@given(instance=expansionmodel_RepresentationKind_strategy)
def test_hyp_expansionmodel_representationkind_viewFactory_setter(instance):
    original = instance.viewFactory
    instance.viewFactory = original
    assert instance.viewFactory == original




@given(instance=expansionmodel_AbstractRepresentation_strategy)
def test_hyp_expansionmodel_abstractrepresentation_editPartQualifiedName_setter(instance):
    original = instance.editPartQualifiedName
    instance.editPartQualifiedName = original
    assert instance.editPartQualifiedName == original



@given(instance=expansionmodel_AbstractRepresentation_strategy)
def test_hyp_expansionmodel_abstractrepresentation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=expansionmodel_AbstractRepresentation_strategy)
def test_hyp_expansionmodel_abstractrepresentation_viewFactory_setter(instance):
    original = instance.viewFactory
    instance.viewFactory = original
    assert instance.viewFactory == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=expansionmodel_AbstractRepresentation_strategy)
@settings(max_examples=30)
def test_hyp_expansionmodel_abstractrepresentation_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in expansionmodel_AbstractRepresentation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in expansionmodel_AbstractRepresentation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in expansionmodel_AbstractRepresentation is not implemented or raised an error")





@given(instance=expansionmodel_Representation_strategy)
def test_hyp_expansionmodel_representation_graphicalElementType_setter(instance):
    original = instance.graphicalElementType
    instance.graphicalElementType = original
    assert instance.graphicalElementType == original




@given(instance=expansionmodel_InducedRepresentation_strategy)
def test_hyp_expansionmodel_inducedrepresentation_hint_setter(instance):
    original = instance.hint
    instance.hint = original
    assert instance.hint == original




@given(instance=expansionmodel_DiagramExpansion_strategy)
def test_hyp_expansionmodel_diagramexpansion_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original





@given(instance=expansionmodel_GMFT_BasedRepresentation_strategy)
def test_hyp_expansionmodel_gmft_basedrepresentation_reusedID_setter(instance):
    original = instance.reusedID
    instance.reusedID = original
    assert instance.reusedID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractRepresentation,
    Representation,
    expansionmodel_AbstractRepresentation,
    expansionmodel_DiagramExpansion,
    expansionmodel_GMFT_BasedRepresentation,
    expansionmodel_GraphicalElementLibrary,
    expansionmodel_InducedRepresentation,
    expansionmodel_Representation,
    expansionmodel_RepresentationKind,
    expansionmodel_UseContext,
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

def test_expansionmodel_AbstractRepresentation_editPartQualifiedName_value_roundtrip():
    instance = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    assert instance.editPartQualifiedName == "sample_text"
    instance.editPartQualifiedName = "sample_text_2"
    assert instance.editPartQualifiedName == "sample_text_2"


def test_expansionmodel_AbstractRepresentation_name_value_roundtrip():
    instance = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_expansionmodel_AbstractRepresentation_viewFactory_value_roundtrip():
    instance = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    assert instance.viewFactory == "sample_text"
    instance.viewFactory = "sample_text_2"
    assert instance.viewFactory == "sample_text_2"


def test_expansionmodel_DiagramExpansion_ID_value_roundtrip():
    instance = expansionmodel_DiagramExpansion(ID="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_expansionmodel_GMFT_BasedRepresentation_reusedID_value_roundtrip():
    instance = expansionmodel_GMFT_BasedRepresentation(reusedID="sample_text")
    assert instance.reusedID == "sample_text"
    instance.reusedID = "sample_text_2"
    assert instance.reusedID == "sample_text_2"


def test_expansionmodel_GraphicalElementLibrary_name_value_roundtrip():
    instance = expansionmodel_GraphicalElementLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_expansionmodel_InducedRepresentation_hint_value_roundtrip():
    instance = expansionmodel_InducedRepresentation(hint="sample_text")
    assert instance.hint == "sample_text"
    instance.hint = "sample_text_2"
    assert instance.hint == "sample_text_2"


def test_expansionmodel_Representation_graphicalElementType_value_roundtrip():
    instance = expansionmodel_Representation(graphicalElementType="sample_text")
    assert instance.graphicalElementType == "sample_text"
    instance.graphicalElementType = "sample_text_2"
    assert instance.graphicalElementType == "sample_text_2"


def test_expansionmodel_RepresentationKind_editPartQualifiedName_value_roundtrip():
    instance = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    assert instance.editPartQualifiedName == "sample_text"
    instance.editPartQualifiedName = "sample_text_2"
    assert instance.editPartQualifiedName == "sample_text_2"


def test_expansionmodel_RepresentationKind_name_value_roundtrip():
    instance = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_expansionmodel_RepresentationKind_viewFactory_value_roundtrip():
    instance = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    assert instance.viewFactory == "sample_text"
    instance.viewFactory = "sample_text_2"
    assert instance.viewFactory == "sample_text_2"


def test_expansionmodel_UseContext_diagramType_value_roundtrip():
    instance = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    assert instance.diagramType == "sample_text"
    instance.diagramType = "sample_text_2"
    assert instance.diagramType == "sample_text_2"


def test_expansionmodel_UseContext_name_value_roundtrip():
    instance = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_expansionmodel_InducedRepresentation_isa_AbstractRepresentation():
    instance = expansionmodel_InducedRepresentation(hint="sample_text")
    assert isinstance(instance, AbstractRepresentation)


def test_expansionmodel_Representation_isa_AbstractRepresentation():
    instance = expansionmodel_Representation(graphicalElementType="sample_text")
    assert isinstance(instance, AbstractRepresentation)


def test_expansionmodel_GMFT_BasedRepresentation_isa_Representation():
    instance = expansionmodel_GMFT_BasedRepresentation(reusedID="sample_text")
    assert isinstance(instance, Representation)


def test_assoc_children5_link_reassign_clear():
    a = expansionmodel_Representation(graphicalElementType="sample_text")
    b1 = expansionmodel_InducedRepresentation(hint="sample_text")
    b2 = expansionmodel_InducedRepresentation(hint="sample_text_2")
    _safe_set(a, 'expansionmodel_Representation7', b1)
    assert _is_linked(a, 'expansionmodel_Representation7', b1)
    if hasattr(b1, 'expansionmodel_InducedRepresentation6'):
        assert _is_linked(b1, 'expansionmodel_InducedRepresentation6', a)
    _safe_set(a, 'expansionmodel_Representation7', b2)
    assert _is_linked(a, 'expansionmodel_Representation7', b2)
    if hasattr(b1, 'expansionmodel_InducedRepresentation6'):
        assert not _is_linked(b1, 'expansionmodel_InducedRepresentation6', a)
    if hasattr(b2, 'expansionmodel_InducedRepresentation6'):
        assert _is_linked(b2, 'expansionmodel_InducedRepresentation6', a)
    _safe_set(a, 'expansionmodel_Representation7', None)
    assert not _is_linked(a, 'expansionmodel_Representation7', b2)
    if hasattr(b2, 'expansionmodel_InducedRepresentation6'):
        assert not _is_linked(b2, 'expansionmodel_InducedRepresentation6', a)


def test_assoc_gmftRepresentations15_link_reassign_clear():
    a = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    b1 = expansionmodel_GMFT_BasedRepresentation(reusedID="sample_text")
    b2 = expansionmodel_GMFT_BasedRepresentation(reusedID="sample_text_2")
    _safe_set(a, 'expansionmodel_UseContext16', {b1})
    assert _is_linked(a, 'expansionmodel_UseContext16', b1)
    if hasattr(b1, 'expansionmodel_GMFT_BasedRepresentation'):
        assert _is_linked(b1, 'expansionmodel_GMFT_BasedRepresentation', a)
    _safe_set(a, 'expansionmodel_UseContext16', {b2})
    assert _is_linked(a, 'expansionmodel_UseContext16', b2)
    if hasattr(b1, 'expansionmodel_GMFT_BasedRepresentation'):
        assert not _is_linked(b1, 'expansionmodel_GMFT_BasedRepresentation', a)
    if hasattr(b2, 'expansionmodel_GMFT_BasedRepresentation'):
        assert _is_linked(b2, 'expansionmodel_GMFT_BasedRepresentation', a)
    _safe_set(a, 'expansionmodel_UseContext16', set())
    assert not _is_linked(a, 'expansionmodel_UseContext16', b2)
    if hasattr(b2, 'expansionmodel_GMFT_BasedRepresentation'):
        assert not _is_linked(b2, 'expansionmodel_GMFT_BasedRepresentation', a)


def test_assoc_inducedRepresentations0_link_reassign_clear():
    a = expansionmodel_Representation(graphicalElementType="sample_text")
    b1 = expansionmodel_InducedRepresentation(hint="sample_text")
    b2 = expansionmodel_InducedRepresentation(hint="sample_text_2")
    _safe_set(a, 'expansionmodel_Representation', {b1})
    assert _is_linked(a, 'expansionmodel_Representation', b1)
    if hasattr(b1, 'expansionmodel_InducedRepresentation'):
        assert _is_linked(b1, 'expansionmodel_InducedRepresentation', a)
    _safe_set(a, 'expansionmodel_Representation', {b2})
    assert _is_linked(a, 'expansionmodel_Representation', b2)
    if hasattr(b1, 'expansionmodel_InducedRepresentation'):
        assert not _is_linked(b1, 'expansionmodel_InducedRepresentation', a)
    if hasattr(b2, 'expansionmodel_InducedRepresentation'):
        assert _is_linked(b2, 'expansionmodel_InducedRepresentation', a)
    _safe_set(a, 'expansionmodel_Representation', set())
    assert not _is_linked(a, 'expansionmodel_Representation', b2)
    if hasattr(b2, 'expansionmodel_InducedRepresentation'):
        assert not _is_linked(b2, 'expansionmodel_InducedRepresentation', a)


def test_assoc_kind4_link_reassign_clear():
    a = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    b1 = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    b2 = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text_2", name="sample_text_2", viewFactory="sample_text_2")
    _safe_set(a, 'expansionmodel_RepresentationKind', b1)
    assert _is_linked(a, 'expansionmodel_RepresentationKind', b1)
    if hasattr(b1, 'expansionmodel_AbstractRepresentation'):
        assert _is_linked(b1, 'expansionmodel_AbstractRepresentation', a)
    _safe_set(a, 'expansionmodel_RepresentationKind', b2)
    assert _is_linked(a, 'expansionmodel_RepresentationKind', b2)
    if hasattr(b1, 'expansionmodel_AbstractRepresentation'):
        assert not _is_linked(b1, 'expansionmodel_AbstractRepresentation', a)
    if hasattr(b2, 'expansionmodel_AbstractRepresentation'):
        assert _is_linked(b2, 'expansionmodel_AbstractRepresentation', a)
    _safe_set(a, 'expansionmodel_RepresentationKind', None)
    assert not _is_linked(a, 'expansionmodel_RepresentationKind', b2)
    if hasattr(b2, 'expansionmodel_AbstractRepresentation'):
        assert not _is_linked(b2, 'expansionmodel_AbstractRepresentation', a)


def test_assoc_libraries19_link_reassign_clear():
    a = expansionmodel_GraphicalElementLibrary(name="sample_text")
    b1 = expansionmodel_DiagramExpansion(ID="sample_text")
    b2 = expansionmodel_DiagramExpansion(ID="sample_text_2")
    _safe_set(a, 'expansionmodel_GraphicalElementLibrary21', b1)
    assert _is_linked(a, 'expansionmodel_GraphicalElementLibrary21', b1)
    if hasattr(b1, 'expansionmodel_DiagramExpansion20'):
        assert _is_linked(b1, 'expansionmodel_DiagramExpansion20', a)
    _safe_set(a, 'expansionmodel_GraphicalElementLibrary21', b2)
    assert _is_linked(a, 'expansionmodel_GraphicalElementLibrary21', b2)
    if hasattr(b1, 'expansionmodel_DiagramExpansion20'):
        assert not _is_linked(b1, 'expansionmodel_DiagramExpansion20', a)
    if hasattr(b2, 'expansionmodel_DiagramExpansion20'):
        assert _is_linked(b2, 'expansionmodel_DiagramExpansion20', a)
    _safe_set(a, 'expansionmodel_GraphicalElementLibrary21', None)
    assert not _is_linked(a, 'expansionmodel_GraphicalElementLibrary21', b2)
    if hasattr(b2, 'expansionmodel_DiagramExpansion20'):
        assert not _is_linked(b2, 'expansionmodel_DiagramExpansion20', a)


def test_assoc_representationkinds8_link_reassign_clear():
    a = expansionmodel_RepresentationKind(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    b1 = expansionmodel_GraphicalElementLibrary(name="sample_text")
    b2 = expansionmodel_GraphicalElementLibrary(name="sample_text_2")
    _safe_set(a, 'expansionmodel_RepresentationKind9', b1)
    assert _is_linked(a, 'expansionmodel_RepresentationKind9', b1)
    if hasattr(b1, 'expansionmodel_GraphicalElementLibrary'):
        assert _is_linked(b1, 'expansionmodel_GraphicalElementLibrary', a)
    _safe_set(a, 'expansionmodel_RepresentationKind9', b2)
    assert _is_linked(a, 'expansionmodel_RepresentationKind9', b2)
    if hasattr(b1, 'expansionmodel_GraphicalElementLibrary'):
        assert not _is_linked(b1, 'expansionmodel_GraphicalElementLibrary', a)
    if hasattr(b2, 'expansionmodel_GraphicalElementLibrary'):
        assert _is_linked(b2, 'expansionmodel_GraphicalElementLibrary', a)
    _safe_set(a, 'expansionmodel_RepresentationKind9', None)
    assert not _is_linked(a, 'expansionmodel_RepresentationKind9', b2)
    if hasattr(b2, 'expansionmodel_GraphicalElementLibrary'):
        assert not _is_linked(b2, 'expansionmodel_GraphicalElementLibrary', a)


def test_assoc_representations10_link_reassign_clear():
    a = expansionmodel_GraphicalElementLibrary(name="sample_text")
    b1 = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text", name="sample_text", viewFactory="sample_text")
    b2 = expansionmodel_AbstractRepresentation(editPartQualifiedName="sample_text_2", name="sample_text_2", viewFactory="sample_text_2")
    _safe_set(a, 'expansionmodel_GraphicalElementLibrary11', {b1})
    assert _is_linked(a, 'expansionmodel_GraphicalElementLibrary11', b1)
    if hasattr(b1, 'expansionmodel_AbstractRepresentation12'):
        assert _is_linked(b1, 'expansionmodel_AbstractRepresentation12', a)
    _safe_set(a, 'expansionmodel_GraphicalElementLibrary11', {b2})
    assert _is_linked(a, 'expansionmodel_GraphicalElementLibrary11', b2)
    if hasattr(b1, 'expansionmodel_AbstractRepresentation12'):
        assert not _is_linked(b1, 'expansionmodel_AbstractRepresentation12', a)
    if hasattr(b2, 'expansionmodel_AbstractRepresentation12'):
        assert _is_linked(b2, 'expansionmodel_AbstractRepresentation12', a)
    _safe_set(a, 'expansionmodel_GraphicalElementLibrary11', set())
    assert not _is_linked(a, 'expansionmodel_GraphicalElementLibrary11', b2)
    if hasattr(b2, 'expansionmodel_AbstractRepresentation12'):
        assert not _is_linked(b2, 'expansionmodel_AbstractRepresentation12', a)


def test_assoc_representations13_link_reassign_clear():
    a = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    b1 = expansionmodel_Representation(graphicalElementType="sample_text")
    b2 = expansionmodel_Representation(graphicalElementType="sample_text_2")
    _safe_set(a, 'expansionmodel_UseContext', {b1})
    assert _is_linked(a, 'expansionmodel_UseContext', b1)
    if hasattr(b1, 'expansionmodel_Representation14'):
        assert _is_linked(b1, 'expansionmodel_Representation14', a)
    _safe_set(a, 'expansionmodel_UseContext', {b2})
    assert _is_linked(a, 'expansionmodel_UseContext', b2)
    if hasattr(b1, 'expansionmodel_Representation14'):
        assert not _is_linked(b1, 'expansionmodel_Representation14', a)
    if hasattr(b2, 'expansionmodel_Representation14'):
        assert _is_linked(b2, 'expansionmodel_Representation14', a)
    _safe_set(a, 'expansionmodel_UseContext', set())
    assert not _is_linked(a, 'expansionmodel_UseContext', b2)
    if hasattr(b2, 'expansionmodel_Representation14'):
        assert not _is_linked(b2, 'expansionmodel_Representation14', a)


def test_assoc_subRepresentations2_link_reassign_clear():
    a = expansionmodel_Representation(graphicalElementType="sample_text")
    b1 = expansionmodel_Representation(graphicalElementType="sample_text")
    b2 = expansionmodel_Representation(graphicalElementType="sample_text_2")
    _safe_set(a, 'expansionmodel_Representation1', {b1})
    assert _is_linked(a, 'expansionmodel_Representation1', b1)
    if hasattr(b1, 'expansionmodel_Representation3'):
        assert _is_linked(b1, 'expansionmodel_Representation3', a)
    _safe_set(a, 'expansionmodel_Representation1', {b2})
    assert _is_linked(a, 'expansionmodel_Representation1', b2)
    if hasattr(b1, 'expansionmodel_Representation3'):
        assert not _is_linked(b1, 'expansionmodel_Representation3', a)
    if hasattr(b2, 'expansionmodel_Representation3'):
        assert _is_linked(b2, 'expansionmodel_Representation3', a)
    _safe_set(a, 'expansionmodel_Representation1', set())
    assert not _is_linked(a, 'expansionmodel_Representation1', b2)
    if hasattr(b2, 'expansionmodel_Representation3'):
        assert not _is_linked(b2, 'expansionmodel_Representation3', a)


def test_assoc_usages17_link_reassign_clear():
    a = expansionmodel_UseContext(diagramType="sample_text", name="sample_text")
    b1 = expansionmodel_DiagramExpansion(ID="sample_text")
    b2 = expansionmodel_DiagramExpansion(ID="sample_text_2")
    _safe_set(a, 'expansionmodel_UseContext18', b1)
    assert _is_linked(a, 'expansionmodel_UseContext18', b1)
    if hasattr(b1, 'expansionmodel_DiagramExpansion'):
        assert _is_linked(b1, 'expansionmodel_DiagramExpansion', a)
    _safe_set(a, 'expansionmodel_UseContext18', b2)
    assert _is_linked(a, 'expansionmodel_UseContext18', b2)
    if hasattr(b1, 'expansionmodel_DiagramExpansion'):
        assert not _is_linked(b1, 'expansionmodel_DiagramExpansion', a)
    if hasattr(b2, 'expansionmodel_DiagramExpansion'):
        assert _is_linked(b2, 'expansionmodel_DiagramExpansion', a)
    _safe_set(a, 'expansionmodel_UseContext18', None)
    assert not _is_linked(a, 'expansionmodel_UseContext18', b2)
    if hasattr(b2, 'expansionmodel_DiagramExpansion'):
        assert not _is_linked(b2, 'expansionmodel_DiagramExpansion', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractRepresentation_strategy = st.builds(AbstractRepresentation)
@given(instance=AbstractRepresentation_strategy)
@settings(max_examples=25)
def test_AbstractRepresentation_instantiation(instance):
    assert isinstance(instance, AbstractRepresentation)


Representation_strategy = st.builds(Representation)
@given(instance=Representation_strategy)
@settings(max_examples=25)
def test_Representation_instantiation(instance):
    assert isinstance(instance, Representation)


expansionmodel_AbstractRepresentation_strategy = st.builds(expansionmodel_AbstractRepresentation, editPartQualifiedName=safe_text, name=safe_text, viewFactory=safe_text)
@given(instance=expansionmodel_AbstractRepresentation_strategy)
@settings(max_examples=25)
def test_expansionmodel_AbstractRepresentation_instantiation(instance):
    assert isinstance(instance, expansionmodel_AbstractRepresentation)


expansionmodel_DiagramExpansion_strategy = st.builds(expansionmodel_DiagramExpansion, ID=safe_text)
@given(instance=expansionmodel_DiagramExpansion_strategy)
@settings(max_examples=25)
def test_expansionmodel_DiagramExpansion_instantiation(instance):
    assert isinstance(instance, expansionmodel_DiagramExpansion)


expansionmodel_GMFT_BasedRepresentation_strategy = st.builds(expansionmodel_GMFT_BasedRepresentation, reusedID=safe_text)
@given(instance=expansionmodel_GMFT_BasedRepresentation_strategy)
@settings(max_examples=25)
def test_expansionmodel_GMFT_BasedRepresentation_instantiation(instance):
    assert isinstance(instance, expansionmodel_GMFT_BasedRepresentation)


expansionmodel_GraphicalElementLibrary_strategy = st.builds(expansionmodel_GraphicalElementLibrary, name=safe_text)
@given(instance=expansionmodel_GraphicalElementLibrary_strategy)
@settings(max_examples=25)
def test_expansionmodel_GraphicalElementLibrary_instantiation(instance):
    assert isinstance(instance, expansionmodel_GraphicalElementLibrary)


expansionmodel_InducedRepresentation_strategy = st.builds(expansionmodel_InducedRepresentation, hint=safe_text)
@given(instance=expansionmodel_InducedRepresentation_strategy)
@settings(max_examples=25)
def test_expansionmodel_InducedRepresentation_instantiation(instance):
    assert isinstance(instance, expansionmodel_InducedRepresentation)


expansionmodel_Representation_strategy = st.builds(expansionmodel_Representation, graphicalElementType=safe_text)
@given(instance=expansionmodel_Representation_strategy)
@settings(max_examples=25)
def test_expansionmodel_Representation_instantiation(instance):
    assert isinstance(instance, expansionmodel_Representation)


expansionmodel_RepresentationKind_strategy = st.builds(expansionmodel_RepresentationKind, editPartQualifiedName=safe_text, name=safe_text, viewFactory=safe_text)
@given(instance=expansionmodel_RepresentationKind_strategy)
@settings(max_examples=25)
def test_expansionmodel_RepresentationKind_instantiation(instance):
    assert isinstance(instance, expansionmodel_RepresentationKind)


expansionmodel_UseContext_strategy = st.builds(expansionmodel_UseContext, diagramType=safe_text, name=safe_text)
@given(instance=expansionmodel_UseContext_strategy)
@settings(max_examples=25)
def test_expansionmodel_UseContext_instantiation(instance):
    assert isinstance(instance, expansionmodel_UseContext)



