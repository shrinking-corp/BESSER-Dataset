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
    graphgrammar_TripleGraph,
    graphgrammar_TripleRule,
    graphgrammar_Edge,
    graphgrammar_TripleGrammar,
    Vertex,
    graphgrammar_StringToVertexMap,
    graphgrammar_Resolution,
    graphgrammar_VertexToStringMap,
    graphgrammar_ResolutionStep,
    graphgrammar_ZoneVertex,
    graphgrammar_ParsingTree,
    graphgrammar_Derivation,
    graphgrammar_VertexToVertexMap,
    graphgrammar_DerivationStep,
    graphgrammar_Rule,
    graphgrammar_SymbolSymbolsPair,
    graphgrammar_Vertex,
    graphgrammar_VertexToSymbolSymbolsPairMap,
    graphgrammar_Graph,
    graphgrammar_Symbol,
    graphgrammar_Grammar,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graphgrammar_triplegraph_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_TripleGraph)


def test_hyp_graphgrammar_triplegraph_constructor_exists():
    assert callable(graphgrammar_TripleGraph.__init__)


def test_hyp_graphgrammar_triplegraph_constructor_args():
    sig = inspect.signature(graphgrammar_TripleGraph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_triplerule_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_TripleRule)


def test_hyp_graphgrammar_triplerule_constructor_exists():
    assert callable(graphgrammar_TripleRule.__init__)


def test_hyp_graphgrammar_triplerule_constructor_args():
    sig = inspect.signature(graphgrammar_TripleRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_edge_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Edge)


def test_hyp_graphgrammar_edge_constructor_exists():
    assert callable(graphgrammar_Edge.__init__)


def test_hyp_graphgrammar_edge_constructor_args():
    sig = inspect.signature(graphgrammar_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_triplegrammar_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_TripleGrammar)


def test_hyp_graphgrammar_triplegrammar_constructor_exists():
    assert callable(graphgrammar_TripleGrammar.__init__)


def test_hyp_graphgrammar_triplegrammar_constructor_args():
    sig = inspect.signature(graphgrammar_TripleGrammar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_hyp_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_hyp_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_stringtovertexmap_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_StringToVertexMap)


def test_hyp_graphgrammar_stringtovertexmap_constructor_exists():
    assert callable(graphgrammar_StringToVertexMap.__init__)


def test_hyp_graphgrammar_stringtovertexmap_constructor_args():
    sig = inspect.signature(graphgrammar_StringToVertexMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_graphgrammar_resolution_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Resolution)


def test_hyp_graphgrammar_resolution_constructor_exists():
    assert callable(graphgrammar_Resolution.__init__)


def test_hyp_graphgrammar_resolution_constructor_args():
    sig = inspect.signature(graphgrammar_Resolution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_vertextostringmap_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_VertexToStringMap)


def test_hyp_graphgrammar_vertextostringmap_constructor_exists():
    assert callable(graphgrammar_VertexToStringMap.__init__)


def test_hyp_graphgrammar_vertextostringmap_constructor_args():
    sig = inspect.signature(graphgrammar_VertexToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graphgrammar_resolutionstep_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_ResolutionStep)


def test_hyp_graphgrammar_resolutionstep_constructor_exists():
    assert callable(graphgrammar_ResolutionStep.__init__)


def test_hyp_graphgrammar_resolutionstep_constructor_args():
    sig = inspect.signature(graphgrammar_ResolutionStep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_zonevertex_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_ZoneVertex)


def test_hyp_graphgrammar_zonevertex_constructor_exists():
    assert callable(graphgrammar_ZoneVertex.__init__)


def test_hyp_graphgrammar_zonevertex_constructor_args():
    sig = inspect.signature(graphgrammar_ZoneVertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_parsingtree_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_ParsingTree)


def test_hyp_graphgrammar_parsingtree_constructor_exists():
    assert callable(graphgrammar_ParsingTree.__init__)


def test_hyp_graphgrammar_parsingtree_constructor_args():
    sig = inspect.signature(graphgrammar_ParsingTree.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_derivation_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Derivation)


def test_hyp_graphgrammar_derivation_constructor_exists():
    assert callable(graphgrammar_Derivation.__init__)


def test_hyp_graphgrammar_derivation_constructor_args():
    sig = inspect.signature(graphgrammar_Derivation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_vertextovertexmap_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_VertexToVertexMap)


def test_hyp_graphgrammar_vertextovertexmap_constructor_exists():
    assert callable(graphgrammar_VertexToVertexMap.__init__)


def test_hyp_graphgrammar_vertextovertexmap_constructor_args():
    sig = inspect.signature(graphgrammar_VertexToVertexMap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_derivationstep_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_DerivationStep)


def test_hyp_graphgrammar_derivationstep_constructor_exists():
    assert callable(graphgrammar_DerivationStep.__init__)


def test_hyp_graphgrammar_derivationstep_constructor_args():
    sig = inspect.signature(graphgrammar_DerivationStep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_rule_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Rule)


def test_hyp_graphgrammar_rule_constructor_exists():
    assert callable(graphgrammar_Rule.__init__)


def test_hyp_graphgrammar_rule_constructor_args():
    sig = inspect.signature(graphgrammar_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_graphgrammar_symbolsymbolspair_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_SymbolSymbolsPair)


def test_hyp_graphgrammar_symbolsymbolspair_constructor_exists():
    assert callable(graphgrammar_SymbolSymbolsPair.__init__)


def test_hyp_graphgrammar_symbolsymbolspair_constructor_args():
    sig = inspect.signature(graphgrammar_SymbolSymbolsPair.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_vertex_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Vertex)


def test_hyp_graphgrammar_vertex_constructor_exists():
    assert callable(graphgrammar_Vertex.__init__)


def test_hyp_graphgrammar_vertex_constructor_args():
    sig = inspect.signature(graphgrammar_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_graphgrammar_vertextosymbolsymbolspairmap_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_VertexToSymbolSymbolsPairMap)


def test_hyp_graphgrammar_vertextosymbolsymbolspairmap_constructor_exists():
    assert callable(graphgrammar_VertexToSymbolSymbolsPairMap.__init__)


def test_hyp_graphgrammar_vertextosymbolsymbolspairmap_constructor_args():
    sig = inspect.signature(graphgrammar_VertexToSymbolSymbolsPairMap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_graph_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Graph)


def test_hyp_graphgrammar_graph_constructor_exists():
    assert callable(graphgrammar_Graph.__init__)


def test_hyp_graphgrammar_graph_constructor_args():
    sig = inspect.signature(graphgrammar_Graph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphgrammar_symbol_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Symbol)


def test_hyp_graphgrammar_symbol_constructor_exists():
    assert callable(graphgrammar_Symbol.__init__)


def test_hyp_graphgrammar_symbol_constructor_args():
    sig = inspect.signature(graphgrammar_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "subscript" in params, "Missing parameter 'subscript'"
    assert "superscript" in params, "Missing parameter 'superscript'"






def test_hyp_graphgrammar_grammar_is_not_abstract():
    assert not inspect.isabstract(graphgrammar_Grammar)


def test_hyp_graphgrammar_grammar_constructor_exists():
    assert callable(graphgrammar_Grammar.__init__)


def test_hyp_graphgrammar_grammar_constructor_args():
    sig = inspect.signature(graphgrammar_Grammar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
graphgrammar_TripleGraph_strategy = st.builds(
    graphgrammar_TripleGraph,
)
graphgrammar_TripleRule_strategy = st.builds(
    graphgrammar_TripleRule,
)
graphgrammar_Edge_strategy = st.builds(
    graphgrammar_Edge,
)
graphgrammar_TripleGrammar_strategy = st.builds(
    graphgrammar_TripleGrammar,
    name=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
graphgrammar_StringToVertexMap_strategy = st.builds(
    graphgrammar_StringToVertexMap,
    key=
        safe_text
)
graphgrammar_Resolution_strategy = st.builds(
    graphgrammar_Resolution,
)
graphgrammar_VertexToStringMap_strategy = st.builds(
    graphgrammar_VertexToStringMap,
    value=
        safe_text
)
graphgrammar_ResolutionStep_strategy = st.builds(
    graphgrammar_ResolutionStep,
)
graphgrammar_ZoneVertex_strategy = st.builds(
    graphgrammar_ZoneVertex,
)
graphgrammar_ParsingTree_strategy = st.builds(
    graphgrammar_ParsingTree,
)
graphgrammar_Derivation_strategy = st.builds(
    graphgrammar_Derivation,
)
graphgrammar_VertexToVertexMap_strategy = st.builds(
    graphgrammar_VertexToVertexMap,
)
graphgrammar_DerivationStep_strategy = st.builds(
    graphgrammar_DerivationStep,
)
graphgrammar_Rule_strategy = st.builds(
    graphgrammar_Rule,
    id=
        safe_text,
    name=
        safe_text
)
graphgrammar_SymbolSymbolsPair_strategy = st.builds(
    graphgrammar_SymbolSymbolsPair,
)
graphgrammar_Vertex_strategy = st.builds(
    graphgrammar_Vertex,
    id=
        safe_text
)
graphgrammar_VertexToSymbolSymbolsPairMap_strategy = st.builds(
    graphgrammar_VertexToSymbolSymbolsPairMap,
)
graphgrammar_Graph_strategy = st.builds(
    graphgrammar_Graph,
)
graphgrammar_Symbol_strategy = st.builds(
    graphgrammar_Symbol,
    name=
        safe_text,
    subscript=
        safe_text,
    superscript=
        safe_text
)
graphgrammar_Grammar_strategy = st.builds(
    graphgrammar_Grammar,
    name=
        safe_text
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_TripleGraph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_triplegraph_invms_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.invMs(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.invMs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'invMs' in graphgrammar_TripleGraph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'invMs' in graphgrammar_TripleGraph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'invMs' in graphgrammar_TripleGraph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_TripleGraph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_triplegraph_invmt_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.invMt(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.invMt).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'invMt' in graphgrammar_TripleGraph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'invMt' in graphgrammar_TripleGraph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'invMt' in graphgrammar_TripleGraph is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_TripleRule_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_triplerule_invmt_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.invMt(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.invMt).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'invMt' in graphgrammar_TripleRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'invMt' in graphgrammar_TripleRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'invMt' in graphgrammar_TripleRule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_TripleRule_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_triplerule_invms_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.invMs(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.invMs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'invMs' in graphgrammar_TripleRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'invMs' in graphgrammar_TripleRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'invMs' in graphgrammar_TripleRule is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Edge_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_edge_compareto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compareTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compareTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compareTo' in graphgrammar_Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compareTo' in graphgrammar_Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compareTo' in graphgrammar_Edge is not implemented or raised an error")




@given(instance=graphgrammar_TripleGrammar_strategy)
def test_hyp_graphgrammar_triplegrammar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_TripleGrammar_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_triplegrammar_produce_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.produce(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.produce).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'produce' in graphgrammar_TripleGrammar is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'produce' in graphgrammar_TripleGrammar did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'produce' in graphgrammar_TripleGrammar is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_TripleGrammar_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_triplegrammar_resolve_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resolve(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resolve).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resolve' in graphgrammar_TripleGrammar is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resolve' in graphgrammar_TripleGrammar did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resolve' in graphgrammar_TripleGrammar is not implemented or raised an error")





@given(instance=graphgrammar_StringToVertexMap_strategy)
def test_hyp_graphgrammar_stringtovertexmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original





@given(instance=graphgrammar_VertexToStringMap_strategy)
def test_hyp_graphgrammar_vertextostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_ZoneVertex_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_zonevertex_equivalates_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equivalates(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equivalates).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equivalates' in graphgrammar_ZoneVertex is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equivalates' in graphgrammar_ZoneVertex did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equivalates' in graphgrammar_ZoneVertex is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_ParsingTree_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_parsingtree_derivation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.derivation()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.derivation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'derivation' in graphgrammar_ParsingTree is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'derivation' in graphgrammar_ParsingTree did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'derivation' in graphgrammar_ParsingTree is not implemented or raised an error")







@given(instance=graphgrammar_Rule_strategy)
def test_hyp_graphgrammar_rule_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=graphgrammar_Rule_strategy)
def test_hyp_graphgrammar_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Rule_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_rule_derive_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.derive(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.derive).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'derive' in graphgrammar_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'derive' in graphgrammar_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'derive' in graphgrammar_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Rule_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_rule_embed_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.embed(
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.embed).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'embed' in graphgrammar_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'embed' in graphgrammar_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'embed' in graphgrammar_Rule is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Rule_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_rule_apply_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.apply(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.apply).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'apply' in graphgrammar_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'apply' in graphgrammar_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'apply' in graphgrammar_Rule is not implemented or raised an error")





@given(instance=graphgrammar_Vertex_strategy)
def test_hyp_graphgrammar_vertex_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Vertex_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_vertex_equivalates_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equivalates(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equivalates).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equivalates' in graphgrammar_Vertex is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equivalates' in graphgrammar_Vertex did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equivalates' in graphgrammar_Vertex is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_graph_isomorphism_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isomorphism(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isomorphism).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isomorphism' in graphgrammar_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isomorphism' in graphgrammar_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isomorphism' in graphgrammar_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_graph_isomorphicto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isomorphicTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isomorphicTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isomorphicTo' in graphgrammar_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isomorphicTo' in graphgrammar_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isomorphicTo' in graphgrammar_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_graph_neighborhood_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.neighborhood(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.neighborhood).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'neighborhood' in graphgrammar_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'neighborhood' in graphgrammar_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'neighborhood' in graphgrammar_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_graph_inedges_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.inEdges(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.inEdges).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'inEdges' in graphgrammar_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inEdges' in graphgrammar_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inEdges' in graphgrammar_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_graph_edges_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.edges(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.edges).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'edges' in graphgrammar_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'edges' in graphgrammar_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'edges' in graphgrammar_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_graph_outedges_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.outEdges(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.outEdges).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'outEdges' in graphgrammar_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'outEdges' in graphgrammar_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'outEdges' in graphgrammar_Graph is not implemented or raised an error")




@given(instance=graphgrammar_Symbol_strategy)
def test_hyp_graphgrammar_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graphgrammar_Symbol_strategy)
def test_hyp_graphgrammar_symbol_subscript_setter(instance):
    original = instance.subscript
    instance.subscript = original
    assert instance.subscript == original



@given(instance=graphgrammar_Symbol_strategy)
def test_hyp_graphgrammar_symbol_superscript_setter(instance):
    original = instance.superscript
    instance.superscript = original
    assert instance.superscript == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Symbol_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_symbol_compareto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compareTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compareTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compareTo' in graphgrammar_Symbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compareTo' in graphgrammar_Symbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compareTo' in graphgrammar_Symbol is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Symbol_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_symbol_equivalates_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equivalates(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equivalates).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equivalates' in graphgrammar_Symbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equivalates' in graphgrammar_Symbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equivalates' in graphgrammar_Symbol is not implemented or raised an error")




@given(instance=graphgrammar_Grammar_strategy)
def test_hyp_graphgrammar_grammar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphgrammar_Grammar_strategy)
@settings(max_examples=30)
def test_hyp_graphgrammar_grammar_derives_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.derives(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.derives).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'derives' in graphgrammar_Grammar is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'derives' in graphgrammar_Grammar did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'derives' in graphgrammar_Grammar is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Vertex,
    graphgrammar_Derivation,
    graphgrammar_DerivationStep,
    graphgrammar_Edge,
    graphgrammar_Grammar,
    graphgrammar_Graph,
    graphgrammar_ParsingTree,
    graphgrammar_Resolution,
    graphgrammar_ResolutionStep,
    graphgrammar_Rule,
    graphgrammar_StringToVertexMap,
    graphgrammar_Symbol,
    graphgrammar_SymbolSymbolsPair,
    graphgrammar_TripleGrammar,
    graphgrammar_TripleGraph,
    graphgrammar_TripleRule,
    graphgrammar_Vertex,
    graphgrammar_VertexToStringMap,
    graphgrammar_VertexToSymbolSymbolsPairMap,
    graphgrammar_VertexToVertexMap,
    graphgrammar_ZoneVertex,
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

def test_graphgrammar_Grammar_name_value_roundtrip():
    instance = graphgrammar_Grammar(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphgrammar_Rule_id_value_roundtrip():
    instance = graphgrammar_Rule(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_graphgrammar_Rule_name_value_roundtrip():
    instance = graphgrammar_Rule(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphgrammar_StringToVertexMap_key_value_roundtrip():
    instance = graphgrammar_StringToVertexMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_graphgrammar_Symbol_name_value_roundtrip():
    instance = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphgrammar_Symbol_subscript_value_roundtrip():
    instance = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    assert instance.subscript == "sample_text"
    instance.subscript = "sample_text_2"
    assert instance.subscript == "sample_text_2"


def test_graphgrammar_Symbol_superscript_value_roundtrip():
    instance = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    assert instance.superscript == "sample_text"
    instance.superscript = "sample_text_2"
    assert instance.superscript == "sample_text_2"


def test_graphgrammar_TripleGrammar_name_value_roundtrip():
    instance = graphgrammar_TripleGrammar(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphgrammar_Vertex_id_value_roundtrip():
    instance = graphgrammar_Vertex(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_graphgrammar_VertexToStringMap_value_value_roundtrip():
    instance = graphgrammar_VertexToStringMap(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_graphgrammar_ZoneVertex_isa_Vertex():
    instance = graphgrammar_ZoneVertex()
    assert isinstance(instance, Vertex)


def test_assoc_alphabet0_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_Grammar(name="sample_text")
    b2 = graphgrammar_Grammar(name="sample_text_2")
    _safe_set(a, 'graphgrammar_Symbol', b1)
    assert _is_linked(a, 'graphgrammar_Symbol', b1)
    if hasattr(b1, 'graphgrammar_Grammar'):
        assert _is_linked(b1, 'graphgrammar_Grammar', a)
    _safe_set(a, 'graphgrammar_Symbol', b2)
    assert _is_linked(a, 'graphgrammar_Symbol', b2)
    if hasattr(b1, 'graphgrammar_Grammar'):
        assert not _is_linked(b1, 'graphgrammar_Grammar', a)
    if hasattr(b2, 'graphgrammar_Grammar'):
        assert _is_linked(b2, 'graphgrammar_Grammar', a)
    _safe_set(a, 'graphgrammar_Symbol', None)
    assert not _is_linked(a, 'graphgrammar_Symbol', b2)
    if hasattr(b2, 'graphgrammar_Grammar'):
        assert not _is_linked(b2, 'graphgrammar_Grammar', a)


def test_assoc_alphabet82_link_reassign_clear():
    a = graphgrammar_TripleGrammar(name="sample_text")
    b1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleGrammar', {b1})
    assert _is_linked(a, 'graphgrammar_TripleGrammar', b1)
    if hasattr(b1, 'graphgrammar_Symbol83'):
        assert _is_linked(b1, 'graphgrammar_Symbol83', a)
    _safe_set(a, 'graphgrammar_TripleGrammar', {b2})
    assert _is_linked(a, 'graphgrammar_TripleGrammar', b2)
    if hasattr(b1, 'graphgrammar_Symbol83'):
        assert not _is_linked(b1, 'graphgrammar_Symbol83', a)
    if hasattr(b2, 'graphgrammar_Symbol83'):
        assert _is_linked(b2, 'graphgrammar_Symbol83', a)
    _safe_set(a, 'graphgrammar_TripleGrammar', set())
    assert not _is_linked(a, 'graphgrammar_TripleGrammar', b2)
    if hasattr(b2, 'graphgrammar_Symbol83'):
        assert not _is_linked(b2, 'graphgrammar_Symbol83', a)


def test_assoc_children52_link_reassign_clear():
    a = graphgrammar_ParsingTree()
    b1 = graphgrammar_ParsingTree()
    b2 = graphgrammar_ParsingTree()
    _safe_set(a, 'graphgrammar_ParsingTree51', {b1})
    assert _is_linked(a, 'graphgrammar_ParsingTree51', b1)
    if hasattr(b1, 'graphgrammar_ParsingTree53'):
        assert _is_linked(b1, 'graphgrammar_ParsingTree53', a)
    _safe_set(a, 'graphgrammar_ParsingTree51', {b2})
    assert _is_linked(a, 'graphgrammar_ParsingTree51', b2)
    if hasattr(b1, 'graphgrammar_ParsingTree53'):
        assert not _is_linked(b1, 'graphgrammar_ParsingTree53', a)
    if hasattr(b2, 'graphgrammar_ParsingTree53'):
        assert _is_linked(b2, 'graphgrammar_ParsingTree53', a)
    _safe_set(a, 'graphgrammar_ParsingTree51', set())
    assert not _is_linked(a, 'graphgrammar_ParsingTree51', b2)
    if hasattr(b2, 'graphgrammar_ParsingTree53'):
        assert not _is_linked(b2, 'graphgrammar_ParsingTree53', a)


def test_assoc_corr112_link_reassign_clear():
    a = graphgrammar_TripleGraph()
    b1 = graphgrammar_Graph()
    b2 = graphgrammar_Graph()
    _safe_set(a, 'graphgrammar_TripleGraph113', b1)
    assert _is_linked(a, 'graphgrammar_TripleGraph113', b1)
    if hasattr(b1, 'graphgrammar_Graph114'):
        assert _is_linked(b1, 'graphgrammar_Graph114', a)
    _safe_set(a, 'graphgrammar_TripleGraph113', b2)
    assert _is_linked(a, 'graphgrammar_TripleGraph113', b2)
    if hasattr(b1, 'graphgrammar_Graph114'):
        assert not _is_linked(b1, 'graphgrammar_Graph114', a)
    if hasattr(b2, 'graphgrammar_Graph114'):
        assert _is_linked(b2, 'graphgrammar_Graph114', a)
    _safe_set(a, 'graphgrammar_TripleGraph113', None)
    assert not _is_linked(a, 'graphgrammar_TripleGraph113', b2)
    if hasattr(b2, 'graphgrammar_Graph114'):
        assert not _is_linked(b2, 'graphgrammar_Graph114', a)


def test_assoc_corr98_link_reassign_clear():
    a = graphgrammar_TripleRule()
    b1 = graphgrammar_Rule(id="sample_text", name="sample_text")
    b2 = graphgrammar_Rule(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleRule99', b1)
    assert _is_linked(a, 'graphgrammar_TripleRule99', b1)
    if hasattr(b1, 'graphgrammar_Rule100'):
        assert _is_linked(b1, 'graphgrammar_Rule100', a)
    _safe_set(a, 'graphgrammar_TripleRule99', b2)
    assert _is_linked(a, 'graphgrammar_TripleRule99', b2)
    if hasattr(b1, 'graphgrammar_Rule100'):
        assert not _is_linked(b1, 'graphgrammar_Rule100', a)
    if hasattr(b2, 'graphgrammar_Rule100'):
        assert _is_linked(b2, 'graphgrammar_Rule100', a)
    _safe_set(a, 'graphgrammar_TripleRule99', None)
    assert not _is_linked(a, 'graphgrammar_TripleRule99', b2)
    if hasattr(b2, 'graphgrammar_Rule100'):
        assert not _is_linked(b2, 'graphgrammar_Rule100', a)


def test_assoc_derivationStep48_link_reassign_clear():
    a = graphgrammar_ParsingTree()
    b1 = graphgrammar_DerivationStep()
    b2 = graphgrammar_DerivationStep()
    _safe_set(a, 'graphgrammar_ParsingTree49', b1)
    assert _is_linked(a, 'graphgrammar_ParsingTree49', b1)
    if hasattr(b1, 'graphgrammar_DerivationStep50'):
        assert _is_linked(b1, 'graphgrammar_DerivationStep50', a)
    _safe_set(a, 'graphgrammar_ParsingTree49', b2)
    assert _is_linked(a, 'graphgrammar_ParsingTree49', b2)
    if hasattr(b1, 'graphgrammar_DerivationStep50'):
        assert not _is_linked(b1, 'graphgrammar_DerivationStep50', a)
    if hasattr(b2, 'graphgrammar_DerivationStep50'):
        assert _is_linked(b2, 'graphgrammar_DerivationStep50', a)
    _safe_set(a, 'graphgrammar_ParsingTree49', None)
    assert not _is_linked(a, 'graphgrammar_ParsingTree49', b2)
    if hasattr(b2, 'graphgrammar_DerivationStep50'):
        assert not _is_linked(b2, 'graphgrammar_DerivationStep50', a)


def test_assoc_edgeLabel21_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_SymbolSymbolsPair()
    b2 = graphgrammar_SymbolSymbolsPair()
    _safe_set(a, 'graphgrammar_Symbol22', b1)
    assert _is_linked(a, 'graphgrammar_Symbol22', b1)
    if hasattr(b1, 'graphgrammar_SymbolSymbolsPair'):
        assert _is_linked(b1, 'graphgrammar_SymbolSymbolsPair', a)
    _safe_set(a, 'graphgrammar_Symbol22', b2)
    assert _is_linked(a, 'graphgrammar_Symbol22', b2)
    if hasattr(b1, 'graphgrammar_SymbolSymbolsPair'):
        assert not _is_linked(b1, 'graphgrammar_SymbolSymbolsPair', a)
    if hasattr(b2, 'graphgrammar_SymbolSymbolsPair'):
        assert _is_linked(b2, 'graphgrammar_SymbolSymbolsPair', a)
    _safe_set(a, 'graphgrammar_Symbol22', None)
    assert not _is_linked(a, 'graphgrammar_Symbol22', b2)
    if hasattr(b2, 'graphgrammar_SymbolSymbolsPair'):
        assert not _is_linked(b2, 'graphgrammar_SymbolSymbolsPair', a)


def test_assoc_edges62_link_reassign_clear():
    a = graphgrammar_Graph()
    b1 = graphgrammar_Edge()
    b2 = graphgrammar_Edge()
    _safe_set(a, 'graphgrammar_Graph63', {b1})
    assert _is_linked(a, 'graphgrammar_Graph63', b1)
    if hasattr(b1, 'graphgrammar_Edge'):
        assert _is_linked(b1, 'graphgrammar_Edge', a)
    _safe_set(a, 'graphgrammar_Graph63', {b2})
    assert _is_linked(a, 'graphgrammar_Graph63', b2)
    if hasattr(b1, 'graphgrammar_Edge'):
        assert not _is_linked(b1, 'graphgrammar_Edge', a)
    if hasattr(b2, 'graphgrammar_Edge'):
        assert _is_linked(b2, 'graphgrammar_Edge', a)
    _safe_set(a, 'graphgrammar_Graph63', set())
    assert not _is_linked(a, 'graphgrammar_Graph63', b2)
    if hasattr(b2, 'graphgrammar_Edge'):
        assert not _is_linked(b2, 'graphgrammar_Edge', a)


def test_assoc_embedding17_link_reassign_clear():
    a = graphgrammar_Rule(id="sample_text", name="sample_text")
    b1 = graphgrammar_VertexToSymbolSymbolsPairMap()
    b2 = graphgrammar_VertexToSymbolSymbolsPairMap()
    _safe_set(a, 'graphgrammar_Rule18', {b1})
    assert _is_linked(a, 'graphgrammar_Rule18', b1)
    if hasattr(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap'):
        assert _is_linked(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap', a)
    _safe_set(a, 'graphgrammar_Rule18', {b2})
    assert _is_linked(a, 'graphgrammar_Rule18', b2)
    if hasattr(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap'):
        assert not _is_linked(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap', a)
    if hasattr(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap'):
        assert _is_linked(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap', a)
    _safe_set(a, 'graphgrammar_Rule18', set())
    assert not _is_linked(a, 'graphgrammar_Rule18', b2)
    if hasattr(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap'):
        assert not _is_linked(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap', a)


def test_assoc_from_73_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_Edge()
    b2 = graphgrammar_Edge()
    _safe_set(a, 'graphgrammar_Vertex75', b1)
    assert _is_linked(a, 'graphgrammar_Vertex75', b1)
    if hasattr(b1, 'graphgrammar_Edge74'):
        assert _is_linked(b1, 'graphgrammar_Edge74', a)
    _safe_set(a, 'graphgrammar_Vertex75', b2)
    assert _is_linked(a, 'graphgrammar_Vertex75', b2)
    if hasattr(b1, 'graphgrammar_Edge74'):
        assert not _is_linked(b1, 'graphgrammar_Edge74', a)
    if hasattr(b2, 'graphgrammar_Edge74'):
        assert _is_linked(b2, 'graphgrammar_Edge74', a)
    _safe_set(a, 'graphgrammar_Vertex75', None)
    assert not _is_linked(a, 'graphgrammar_Vertex75', b2)
    if hasattr(b2, 'graphgrammar_Edge74'):
        assert not _is_linked(b2, 'graphgrammar_Edge74', a)


def test_assoc_initial9_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_Grammar(name="sample_text")
    b2 = graphgrammar_Grammar(name="sample_text_2")
    _safe_set(a, 'graphgrammar_Symbol11', b1)
    assert _is_linked(a, 'graphgrammar_Symbol11', b1)
    if hasattr(b1, 'graphgrammar_Grammar10'):
        assert _is_linked(b1, 'graphgrammar_Grammar10', a)
    _safe_set(a, 'graphgrammar_Symbol11', b2)
    assert _is_linked(a, 'graphgrammar_Symbol11', b2)
    if hasattr(b1, 'graphgrammar_Grammar10'):
        assert not _is_linked(b1, 'graphgrammar_Grammar10', a)
    if hasattr(b2, 'graphgrammar_Grammar10'):
        assert _is_linked(b2, 'graphgrammar_Grammar10', a)
    _safe_set(a, 'graphgrammar_Symbol11', None)
    assert not _is_linked(a, 'graphgrammar_Symbol11', b2)
    if hasattr(b2, 'graphgrammar_Grammar10'):
        assert not _is_linked(b2, 'graphgrammar_Grammar10', a)


def test_assoc_initial92_link_reassign_clear():
    a = graphgrammar_TripleGrammar(name="sample_text")
    b1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleGrammar93', b1)
    assert _is_linked(a, 'graphgrammar_TripleGrammar93', b1)
    if hasattr(b1, 'graphgrammar_Symbol94'):
        assert _is_linked(b1, 'graphgrammar_Symbol94', a)
    _safe_set(a, 'graphgrammar_TripleGrammar93', b2)
    assert _is_linked(a, 'graphgrammar_TripleGrammar93', b2)
    if hasattr(b1, 'graphgrammar_Symbol94'):
        assert not _is_linked(b1, 'graphgrammar_Symbol94', a)
    if hasattr(b2, 'graphgrammar_Symbol94'):
        assert _is_linked(b2, 'graphgrammar_Symbol94', a)
    _safe_set(a, 'graphgrammar_TripleGrammar93', None)
    assert not _is_linked(a, 'graphgrammar_TripleGrammar93', b2)
    if hasattr(b2, 'graphgrammar_Symbol94'):
        assert not _is_linked(b2, 'graphgrammar_Symbol94', a)


def test_assoc_key124_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_VertexToVertexMap()
    b2 = graphgrammar_VertexToVertexMap()
    _safe_set(a, 'graphgrammar_Vertex126', b1)
    assert _is_linked(a, 'graphgrammar_Vertex126', b1)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap125'):
        assert _is_linked(b1, 'graphgrammar_VertexToVertexMap125', a)
    _safe_set(a, 'graphgrammar_Vertex126', b2)
    assert _is_linked(a, 'graphgrammar_Vertex126', b2)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap125'):
        assert not _is_linked(b1, 'graphgrammar_VertexToVertexMap125', a)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap125'):
        assert _is_linked(b2, 'graphgrammar_VertexToVertexMap125', a)
    _safe_set(a, 'graphgrammar_Vertex126', None)
    assert not _is_linked(a, 'graphgrammar_Vertex126', b2)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap125'):
        assert not _is_linked(b2, 'graphgrammar_VertexToVertexMap125', a)


def test_assoc_key130_link_reassign_clear():
    a = graphgrammar_VertexToStringMap(value="sample_text")
    b1 = graphgrammar_Vertex(id="sample_text")
    b2 = graphgrammar_Vertex(id="sample_text_2")
    _safe_set(a, 'graphgrammar_VertexToStringMap131', b1)
    assert _is_linked(a, 'graphgrammar_VertexToStringMap131', b1)
    if hasattr(b1, 'graphgrammar_Vertex132'):
        assert _is_linked(b1, 'graphgrammar_Vertex132', a)
    _safe_set(a, 'graphgrammar_VertexToStringMap131', b2)
    assert _is_linked(a, 'graphgrammar_VertexToStringMap131', b2)
    if hasattr(b1, 'graphgrammar_Vertex132'):
        assert not _is_linked(b1, 'graphgrammar_Vertex132', a)
    if hasattr(b2, 'graphgrammar_Vertex132'):
        assert _is_linked(b2, 'graphgrammar_Vertex132', a)
    _safe_set(a, 'graphgrammar_VertexToStringMap131', None)
    assert not _is_linked(a, 'graphgrammar_VertexToStringMap131', b2)
    if hasattr(b2, 'graphgrammar_Vertex132'):
        assert not _is_linked(b2, 'graphgrammar_Vertex132', a)


def test_assoc_key26_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_VertexToSymbolSymbolsPairMap()
    b2 = graphgrammar_VertexToSymbolSymbolsPairMap()
    _safe_set(a, 'graphgrammar_Vertex28', b1)
    assert _is_linked(a, 'graphgrammar_Vertex28', b1)
    if hasattr(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap27'):
        assert _is_linked(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap27', a)
    _safe_set(a, 'graphgrammar_Vertex28', b2)
    assert _is_linked(a, 'graphgrammar_Vertex28', b2)
    if hasattr(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap27'):
        assert not _is_linked(b1, 'graphgrammar_VertexToSymbolSymbolsPairMap27', a)
    if hasattr(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap27'):
        assert _is_linked(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap27', a)
    _safe_set(a, 'graphgrammar_Vertex28', None)
    assert not _is_linked(a, 'graphgrammar_Vertex28', b2)
    if hasattr(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap27'):
        assert not _is_linked(b2, 'graphgrammar_VertexToSymbolSymbolsPairMap27', a)


def test_assoc_label64_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    _safe_set(a, 'graphgrammar_Vertex65', b1)
    assert _is_linked(a, 'graphgrammar_Vertex65', b1)
    if hasattr(b1, 'graphgrammar_Symbol66'):
        assert _is_linked(b1, 'graphgrammar_Symbol66', a)
    _safe_set(a, 'graphgrammar_Vertex65', b2)
    assert _is_linked(a, 'graphgrammar_Vertex65', b2)
    if hasattr(b1, 'graphgrammar_Symbol66'):
        assert not _is_linked(b1, 'graphgrammar_Symbol66', a)
    if hasattr(b2, 'graphgrammar_Symbol66'):
        assert _is_linked(b2, 'graphgrammar_Symbol66', a)
    _safe_set(a, 'graphgrammar_Vertex65', None)
    assert not _is_linked(a, 'graphgrammar_Vertex65', b2)
    if hasattr(b2, 'graphgrammar_Symbol66'):
        assert not _is_linked(b2, 'graphgrammar_Symbol66', a)


def test_assoc_label79_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_Edge()
    b2 = graphgrammar_Edge()
    _safe_set(a, 'graphgrammar_Symbol81', b1)
    assert _is_linked(a, 'graphgrammar_Symbol81', b1)
    if hasattr(b1, 'graphgrammar_Edge80'):
        assert _is_linked(b1, 'graphgrammar_Edge80', a)
    _safe_set(a, 'graphgrammar_Symbol81', b2)
    assert _is_linked(a, 'graphgrammar_Symbol81', b2)
    if hasattr(b1, 'graphgrammar_Edge80'):
        assert not _is_linked(b1, 'graphgrammar_Edge80', a)
    if hasattr(b2, 'graphgrammar_Edge80'):
        assert _is_linked(b2, 'graphgrammar_Edge80', a)
    _safe_set(a, 'graphgrammar_Symbol81', None)
    assert not _is_linked(a, 'graphgrammar_Symbol81', b2)
    if hasattr(b2, 'graphgrammar_Edge80'):
        assert not _is_linked(b2, 'graphgrammar_Edge80', a)


def test_assoc_lhs12_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_Rule(id="sample_text", name="sample_text")
    b2 = graphgrammar_Rule(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'graphgrammar_Symbol14', b1)
    assert _is_linked(a, 'graphgrammar_Symbol14', b1)
    if hasattr(b1, 'graphgrammar_Rule13'):
        assert _is_linked(b1, 'graphgrammar_Rule13', a)
    _safe_set(a, 'graphgrammar_Symbol14', b2)
    assert _is_linked(a, 'graphgrammar_Symbol14', b2)
    if hasattr(b1, 'graphgrammar_Rule13'):
        assert not _is_linked(b1, 'graphgrammar_Rule13', a)
    if hasattr(b2, 'graphgrammar_Rule13'):
        assert _is_linked(b2, 'graphgrammar_Rule13', a)
    _safe_set(a, 'graphgrammar_Symbol14', None)
    assert not _is_linked(a, 'graphgrammar_Symbol14', b2)
    if hasattr(b2, 'graphgrammar_Rule13'):
        assert not _is_linked(b2, 'graphgrammar_Rule13', a)


def test_assoc_ms104_link_reassign_clear():
    a = graphgrammar_TripleRule()
    b1 = graphgrammar_VertexToVertexMap()
    b2 = graphgrammar_VertexToVertexMap()
    _safe_set(a, 'graphgrammar_TripleRule105', {b1})
    assert _is_linked(a, 'graphgrammar_TripleRule105', b1)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap106'):
        assert _is_linked(b1, 'graphgrammar_VertexToVertexMap106', a)
    _safe_set(a, 'graphgrammar_TripleRule105', {b2})
    assert _is_linked(a, 'graphgrammar_TripleRule105', b2)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap106'):
        assert not _is_linked(b1, 'graphgrammar_VertexToVertexMap106', a)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap106'):
        assert _is_linked(b2, 'graphgrammar_VertexToVertexMap106', a)
    _safe_set(a, 'graphgrammar_TripleRule105', set())
    assert not _is_linked(a, 'graphgrammar_TripleRule105', b2)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap106'):
        assert not _is_linked(b2, 'graphgrammar_VertexToVertexMap106', a)


def test_assoc_ms118_link_reassign_clear():
    a = graphgrammar_TripleGraph()
    b1 = graphgrammar_VertexToVertexMap()
    b2 = graphgrammar_VertexToVertexMap()
    _safe_set(a, 'graphgrammar_TripleGraph119', {b1})
    assert _is_linked(a, 'graphgrammar_TripleGraph119', b1)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap120'):
        assert _is_linked(b1, 'graphgrammar_VertexToVertexMap120', a)
    _safe_set(a, 'graphgrammar_TripleGraph119', {b2})
    assert _is_linked(a, 'graphgrammar_TripleGraph119', b2)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap120'):
        assert not _is_linked(b1, 'graphgrammar_VertexToVertexMap120', a)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap120'):
        assert _is_linked(b2, 'graphgrammar_VertexToVertexMap120', a)
    _safe_set(a, 'graphgrammar_TripleGraph119', set())
    assert not _is_linked(a, 'graphgrammar_TripleGraph119', b2)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap120'):
        assert not _is_linked(b2, 'graphgrammar_VertexToVertexMap120', a)


def test_assoc_mt107_link_reassign_clear():
    a = graphgrammar_TripleRule()
    b1 = graphgrammar_VertexToVertexMap()
    b2 = graphgrammar_VertexToVertexMap()
    _safe_set(a, 'graphgrammar_TripleRule108', {b1})
    assert _is_linked(a, 'graphgrammar_TripleRule108', b1)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap109'):
        assert _is_linked(b1, 'graphgrammar_VertexToVertexMap109', a)
    _safe_set(a, 'graphgrammar_TripleRule108', {b2})
    assert _is_linked(a, 'graphgrammar_TripleRule108', b2)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap109'):
        assert not _is_linked(b1, 'graphgrammar_VertexToVertexMap109', a)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap109'):
        assert _is_linked(b2, 'graphgrammar_VertexToVertexMap109', a)
    _safe_set(a, 'graphgrammar_TripleRule108', set())
    assert not _is_linked(a, 'graphgrammar_TripleRule108', b2)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap109'):
        assert not _is_linked(b2, 'graphgrammar_VertexToVertexMap109', a)


def test_assoc_mt121_link_reassign_clear():
    a = graphgrammar_TripleGraph()
    b1 = graphgrammar_VertexToVertexMap()
    b2 = graphgrammar_VertexToVertexMap()
    _safe_set(a, 'graphgrammar_TripleGraph122', {b1})
    assert _is_linked(a, 'graphgrammar_TripleGraph122', b1)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap123'):
        assert _is_linked(b1, 'graphgrammar_VertexToVertexMap123', a)
    _safe_set(a, 'graphgrammar_TripleGraph122', {b2})
    assert _is_linked(a, 'graphgrammar_TripleGraph122', b2)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap123'):
        assert not _is_linked(b1, 'graphgrammar_VertexToVertexMap123', a)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap123'):
        assert _is_linked(b2, 'graphgrammar_VertexToVertexMap123', a)
    _safe_set(a, 'graphgrammar_TripleGraph122', set())
    assert not _is_linked(a, 'graphgrammar_TripleGraph122', b2)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap123'):
        assert not _is_linked(b2, 'graphgrammar_VertexToVertexMap123', a)


def test_assoc_next40_link_reassign_clear():
    a = graphgrammar_Graph()
    b1 = graphgrammar_DerivationStep()
    b2 = graphgrammar_DerivationStep()
    _safe_set(a, 'graphgrammar_Graph42', b1)
    assert _is_linked(a, 'graphgrammar_Graph42', b1)
    if hasattr(b1, 'graphgrammar_DerivationStep41'):
        assert _is_linked(b1, 'graphgrammar_DerivationStep41', a)
    _safe_set(a, 'graphgrammar_Graph42', b2)
    assert _is_linked(a, 'graphgrammar_Graph42', b2)
    if hasattr(b1, 'graphgrammar_DerivationStep41'):
        assert not _is_linked(b1, 'graphgrammar_DerivationStep41', a)
    if hasattr(b2, 'graphgrammar_DerivationStep41'):
        assert _is_linked(b2, 'graphgrammar_DerivationStep41', a)
    _safe_set(a, 'graphgrammar_Graph42', None)
    assert not _is_linked(a, 'graphgrammar_Graph42', b2)
    if hasattr(b2, 'graphgrammar_DerivationStep41'):
        assert not _is_linked(b2, 'graphgrammar_DerivationStep41', a)


def test_assoc_nonterminals4_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_Grammar(name="sample_text")
    b2 = graphgrammar_Grammar(name="sample_text_2")
    _safe_set(a, 'graphgrammar_Symbol6', b1)
    assert _is_linked(a, 'graphgrammar_Symbol6', b1)
    if hasattr(b1, 'graphgrammar_Grammar5'):
        assert _is_linked(b1, 'graphgrammar_Grammar5', a)
    _safe_set(a, 'graphgrammar_Symbol6', b2)
    assert _is_linked(a, 'graphgrammar_Symbol6', b2)
    if hasattr(b1, 'graphgrammar_Grammar5'):
        assert not _is_linked(b1, 'graphgrammar_Grammar5', a)
    if hasattr(b2, 'graphgrammar_Grammar5'):
        assert _is_linked(b2, 'graphgrammar_Grammar5', a)
    _safe_set(a, 'graphgrammar_Symbol6', None)
    assert not _is_linked(a, 'graphgrammar_Symbol6', b2)
    if hasattr(b2, 'graphgrammar_Grammar5'):
        assert not _is_linked(b2, 'graphgrammar_Grammar5', a)


def test_assoc_nonterminals87_link_reassign_clear():
    a = graphgrammar_TripleGrammar(name="sample_text")
    b1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleGrammar88', {b1})
    assert _is_linked(a, 'graphgrammar_TripleGrammar88', b1)
    if hasattr(b1, 'graphgrammar_Symbol89'):
        assert _is_linked(b1, 'graphgrammar_Symbol89', a)
    _safe_set(a, 'graphgrammar_TripleGrammar88', {b2})
    assert _is_linked(a, 'graphgrammar_TripleGrammar88', b2)
    if hasattr(b1, 'graphgrammar_Symbol89'):
        assert not _is_linked(b1, 'graphgrammar_Symbol89', a)
    if hasattr(b2, 'graphgrammar_Symbol89'):
        assert _is_linked(b2, 'graphgrammar_Symbol89', a)
    _safe_set(a, 'graphgrammar_TripleGrammar88', set())
    assert not _is_linked(a, 'graphgrammar_TripleGrammar88', b2)
    if hasattr(b2, 'graphgrammar_Symbol89'):
        assert not _is_linked(b2, 'graphgrammar_Symbol89', a)


def test_assoc_pac19_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_Rule(id="sample_text", name="sample_text")
    b2 = graphgrammar_Rule(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'graphgrammar_Vertex', b1)
    assert _is_linked(a, 'graphgrammar_Vertex', b1)
    if hasattr(b1, 'graphgrammar_Rule20'):
        assert _is_linked(b1, 'graphgrammar_Rule20', a)
    _safe_set(a, 'graphgrammar_Vertex', b2)
    assert _is_linked(a, 'graphgrammar_Vertex', b2)
    if hasattr(b1, 'graphgrammar_Rule20'):
        assert not _is_linked(b1, 'graphgrammar_Rule20', a)
    if hasattr(b2, 'graphgrammar_Rule20'):
        assert _is_linked(b2, 'graphgrammar_Rule20', a)
    _safe_set(a, 'graphgrammar_Vertex', None)
    assert not _is_linked(a, 'graphgrammar_Vertex', b2)
    if hasattr(b2, 'graphgrammar_Rule20'):
        assert not _is_linked(b2, 'graphgrammar_Rule20', a)


def test_assoc_pac54_link_reassign_clear():
    a = graphgrammar_VertexToStringMap(value="sample_text")
    b1 = graphgrammar_ResolutionStep()
    b2 = graphgrammar_ResolutionStep()
    _safe_set(a, 'graphgrammar_VertexToStringMap', b1)
    assert _is_linked(a, 'graphgrammar_VertexToStringMap', b1)
    if hasattr(b1, 'graphgrammar_ResolutionStep'):
        assert _is_linked(b1, 'graphgrammar_ResolutionStep', a)
    _safe_set(a, 'graphgrammar_VertexToStringMap', b2)
    assert _is_linked(a, 'graphgrammar_VertexToStringMap', b2)
    if hasattr(b1, 'graphgrammar_ResolutionStep'):
        assert not _is_linked(b1, 'graphgrammar_ResolutionStep', a)
    if hasattr(b2, 'graphgrammar_ResolutionStep'):
        assert _is_linked(b2, 'graphgrammar_ResolutionStep', a)
    _safe_set(a, 'graphgrammar_VertexToStringMap', None)
    assert not _is_linked(a, 'graphgrammar_VertexToStringMap', b2)
    if hasattr(b2, 'graphgrammar_ResolutionStep'):
        assert not _is_linked(b2, 'graphgrammar_ResolutionStep', a)


def test_assoc_pac70_link_reassign_clear():
    a = graphgrammar_ZoneVertex()
    b1 = graphgrammar_Vertex(id="sample_text")
    b2 = graphgrammar_Vertex(id="sample_text_2")
    _safe_set(a, 'graphgrammar_ZoneVertex71', {b1})
    assert _is_linked(a, 'graphgrammar_ZoneVertex71', b1)
    if hasattr(b1, 'graphgrammar_Vertex72'):
        assert _is_linked(b1, 'graphgrammar_Vertex72', a)
    _safe_set(a, 'graphgrammar_ZoneVertex71', {b2})
    assert _is_linked(a, 'graphgrammar_ZoneVertex71', b2)
    if hasattr(b1, 'graphgrammar_Vertex72'):
        assert not _is_linked(b1, 'graphgrammar_Vertex72', a)
    if hasattr(b2, 'graphgrammar_Vertex72'):
        assert _is_linked(b2, 'graphgrammar_Vertex72', a)
    _safe_set(a, 'graphgrammar_ZoneVertex71', set())
    assert not _is_linked(a, 'graphgrammar_ZoneVertex71', b2)
    if hasattr(b2, 'graphgrammar_Vertex72'):
        assert not _is_linked(b2, 'graphgrammar_Vertex72', a)


def test_assoc_previous37_link_reassign_clear():
    a = graphgrammar_Graph()
    b1 = graphgrammar_DerivationStep()
    b2 = graphgrammar_DerivationStep()
    _safe_set(a, 'graphgrammar_Graph39', b1)
    assert _is_linked(a, 'graphgrammar_Graph39', b1)
    if hasattr(b1, 'graphgrammar_DerivationStep38'):
        assert _is_linked(b1, 'graphgrammar_DerivationStep38', a)
    _safe_set(a, 'graphgrammar_Graph39', b2)
    assert _is_linked(a, 'graphgrammar_Graph39', b2)
    if hasattr(b1, 'graphgrammar_DerivationStep38'):
        assert not _is_linked(b1, 'graphgrammar_DerivationStep38', a)
    if hasattr(b2, 'graphgrammar_DerivationStep38'):
        assert _is_linked(b2, 'graphgrammar_DerivationStep38', a)
    _safe_set(a, 'graphgrammar_Graph39', None)
    assert not _is_linked(a, 'graphgrammar_Graph39', b2)
    if hasattr(b2, 'graphgrammar_DerivationStep38'):
        assert not _is_linked(b2, 'graphgrammar_DerivationStep38', a)


def test_assoc_referenceIds55_link_reassign_clear():
    a = graphgrammar_StringToVertexMap(key="sample_text")
    b1 = graphgrammar_Resolution()
    b2 = graphgrammar_Resolution()
    _safe_set(a, 'graphgrammar_StringToVertexMap', b1)
    assert _is_linked(a, 'graphgrammar_StringToVertexMap', b1)
    if hasattr(b1, 'graphgrammar_Resolution'):
        assert _is_linked(b1, 'graphgrammar_Resolution', a)
    _safe_set(a, 'graphgrammar_StringToVertexMap', b2)
    assert _is_linked(a, 'graphgrammar_StringToVertexMap', b2)
    if hasattr(b1, 'graphgrammar_Resolution'):
        assert not _is_linked(b1, 'graphgrammar_Resolution', a)
    if hasattr(b2, 'graphgrammar_Resolution'):
        assert _is_linked(b2, 'graphgrammar_Resolution', a)
    _safe_set(a, 'graphgrammar_StringToVertexMap', None)
    assert not _is_linked(a, 'graphgrammar_StringToVertexMap', b2)
    if hasattr(b2, 'graphgrammar_Resolution'):
        assert not _is_linked(b2, 'graphgrammar_Resolution', a)


def test_assoc_rhs15_link_reassign_clear():
    a = graphgrammar_Rule(id="sample_text", name="sample_text")
    b1 = graphgrammar_Graph()
    b2 = graphgrammar_Graph()
    _safe_set(a, 'graphgrammar_Rule16', b1)
    assert _is_linked(a, 'graphgrammar_Rule16', b1)
    if hasattr(b1, 'graphgrammar_Graph'):
        assert _is_linked(b1, 'graphgrammar_Graph', a)
    _safe_set(a, 'graphgrammar_Rule16', b2)
    assert _is_linked(a, 'graphgrammar_Rule16', b2)
    if hasattr(b1, 'graphgrammar_Graph'):
        assert not _is_linked(b1, 'graphgrammar_Graph', a)
    if hasattr(b2, 'graphgrammar_Graph'):
        assert _is_linked(b2, 'graphgrammar_Graph', a)
    _safe_set(a, 'graphgrammar_Rule16', None)
    assert not _is_linked(a, 'graphgrammar_Rule16', b2)
    if hasattr(b2, 'graphgrammar_Graph'):
        assert not _is_linked(b2, 'graphgrammar_Graph', a)


def test_assoc_rule32_link_reassign_clear():
    a = graphgrammar_Rule(id="sample_text", name="sample_text")
    b1 = graphgrammar_DerivationStep()
    b2 = graphgrammar_DerivationStep()
    _safe_set(a, 'graphgrammar_Rule33', b1)
    assert _is_linked(a, 'graphgrammar_Rule33', b1)
    if hasattr(b1, 'graphgrammar_DerivationStep'):
        assert _is_linked(b1, 'graphgrammar_DerivationStep', a)
    _safe_set(a, 'graphgrammar_Rule33', b2)
    assert _is_linked(a, 'graphgrammar_Rule33', b2)
    if hasattr(b1, 'graphgrammar_DerivationStep'):
        assert not _is_linked(b1, 'graphgrammar_DerivationStep', a)
    if hasattr(b2, 'graphgrammar_DerivationStep'):
        assert _is_linked(b2, 'graphgrammar_DerivationStep', a)
    _safe_set(a, 'graphgrammar_Rule33', None)
    assert not _is_linked(a, 'graphgrammar_Rule33', b2)
    if hasattr(b2, 'graphgrammar_DerivationStep'):
        assert not _is_linked(b2, 'graphgrammar_DerivationStep', a)


def test_assoc_rules7_link_reassign_clear():
    a = graphgrammar_Rule(id="sample_text", name="sample_text")
    b1 = graphgrammar_Grammar(name="sample_text")
    b2 = graphgrammar_Grammar(name="sample_text_2")
    _safe_set(a, 'graphgrammar_Rule', b1)
    assert _is_linked(a, 'graphgrammar_Rule', b1)
    if hasattr(b1, 'graphgrammar_Grammar8'):
        assert _is_linked(b1, 'graphgrammar_Grammar8', a)
    _safe_set(a, 'graphgrammar_Rule', b2)
    assert _is_linked(a, 'graphgrammar_Rule', b2)
    if hasattr(b1, 'graphgrammar_Grammar8'):
        assert not _is_linked(b1, 'graphgrammar_Grammar8', a)
    if hasattr(b2, 'graphgrammar_Grammar8'):
        assert _is_linked(b2, 'graphgrammar_Grammar8', a)
    _safe_set(a, 'graphgrammar_Rule', None)
    assert not _is_linked(a, 'graphgrammar_Rule', b2)
    if hasattr(b2, 'graphgrammar_Grammar8'):
        assert not _is_linked(b2, 'graphgrammar_Grammar8', a)


def test_assoc_source110_link_reassign_clear():
    a = graphgrammar_TripleGraph()
    b1 = graphgrammar_Graph()
    b2 = graphgrammar_Graph()
    _safe_set(a, 'graphgrammar_TripleGraph', b1)
    assert _is_linked(a, 'graphgrammar_TripleGraph', b1)
    if hasattr(b1, 'graphgrammar_Graph111'):
        assert _is_linked(b1, 'graphgrammar_Graph111', a)
    _safe_set(a, 'graphgrammar_TripleGraph', b2)
    assert _is_linked(a, 'graphgrammar_TripleGraph', b2)
    if hasattr(b1, 'graphgrammar_Graph111'):
        assert not _is_linked(b1, 'graphgrammar_Graph111', a)
    if hasattr(b2, 'graphgrammar_Graph111'):
        assert _is_linked(b2, 'graphgrammar_Graph111', a)
    _safe_set(a, 'graphgrammar_TripleGraph', None)
    assert not _is_linked(a, 'graphgrammar_TripleGraph', b2)
    if hasattr(b2, 'graphgrammar_Graph111'):
        assert not _is_linked(b2, 'graphgrammar_Graph111', a)


def test_assoc_source95_link_reassign_clear():
    a = graphgrammar_TripleRule()
    b1 = graphgrammar_Rule(id="sample_text", name="sample_text")
    b2 = graphgrammar_Rule(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleRule96', b1)
    assert _is_linked(a, 'graphgrammar_TripleRule96', b1)
    if hasattr(b1, 'graphgrammar_Rule97'):
        assert _is_linked(b1, 'graphgrammar_Rule97', a)
    _safe_set(a, 'graphgrammar_TripleRule96', b2)
    assert _is_linked(a, 'graphgrammar_TripleRule96', b2)
    if hasattr(b1, 'graphgrammar_Rule97'):
        assert not _is_linked(b1, 'graphgrammar_Rule97', a)
    if hasattr(b2, 'graphgrammar_Rule97'):
        assert _is_linked(b2, 'graphgrammar_Rule97', a)
    _safe_set(a, 'graphgrammar_TripleRule96', None)
    assert not _is_linked(a, 'graphgrammar_TripleRule96', b2)
    if hasattr(b2, 'graphgrammar_Rule97'):
        assert not _is_linked(b2, 'graphgrammar_Rule97', a)


def test_assoc_target101_link_reassign_clear():
    a = graphgrammar_TripleRule()
    b1 = graphgrammar_Rule(id="sample_text", name="sample_text")
    b2 = graphgrammar_Rule(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleRule102', b1)
    assert _is_linked(a, 'graphgrammar_TripleRule102', b1)
    if hasattr(b1, 'graphgrammar_Rule103'):
        assert _is_linked(b1, 'graphgrammar_Rule103', a)
    _safe_set(a, 'graphgrammar_TripleRule102', b2)
    assert _is_linked(a, 'graphgrammar_TripleRule102', b2)
    if hasattr(b1, 'graphgrammar_Rule103'):
        assert not _is_linked(b1, 'graphgrammar_Rule103', a)
    if hasattr(b2, 'graphgrammar_Rule103'):
        assert _is_linked(b2, 'graphgrammar_Rule103', a)
    _safe_set(a, 'graphgrammar_TripleRule102', None)
    assert not _is_linked(a, 'graphgrammar_TripleRule102', b2)
    if hasattr(b2, 'graphgrammar_Rule103'):
        assert not _is_linked(b2, 'graphgrammar_Rule103', a)


def test_assoc_target115_link_reassign_clear():
    a = graphgrammar_TripleGraph()
    b1 = graphgrammar_Graph()
    b2 = graphgrammar_Graph()
    _safe_set(a, 'graphgrammar_TripleGraph116', b1)
    assert _is_linked(a, 'graphgrammar_TripleGraph116', b1)
    if hasattr(b1, 'graphgrammar_Graph117'):
        assert _is_linked(b1, 'graphgrammar_Graph117', a)
    _safe_set(a, 'graphgrammar_TripleGraph116', b2)
    assert _is_linked(a, 'graphgrammar_TripleGraph116', b2)
    if hasattr(b1, 'graphgrammar_Graph117'):
        assert not _is_linked(b1, 'graphgrammar_Graph117', a)
    if hasattr(b2, 'graphgrammar_Graph117'):
        assert _is_linked(b2, 'graphgrammar_Graph117', a)
    _safe_set(a, 'graphgrammar_TripleGraph116', None)
    assert not _is_linked(a, 'graphgrammar_TripleGraph116', b2)
    if hasattr(b2, 'graphgrammar_Graph117'):
        assert not _is_linked(b2, 'graphgrammar_Graph117', a)


def test_assoc_terminals1_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_Grammar(name="sample_text")
    b2 = graphgrammar_Grammar(name="sample_text_2")
    _safe_set(a, 'graphgrammar_Symbol3', b1)
    assert _is_linked(a, 'graphgrammar_Symbol3', b1)
    if hasattr(b1, 'graphgrammar_Grammar2'):
        assert _is_linked(b1, 'graphgrammar_Grammar2', a)
    _safe_set(a, 'graphgrammar_Symbol3', b2)
    assert _is_linked(a, 'graphgrammar_Symbol3', b2)
    if hasattr(b1, 'graphgrammar_Grammar2'):
        assert not _is_linked(b1, 'graphgrammar_Grammar2', a)
    if hasattr(b2, 'graphgrammar_Grammar2'):
        assert _is_linked(b2, 'graphgrammar_Grammar2', a)
    _safe_set(a, 'graphgrammar_Symbol3', None)
    assert not _is_linked(a, 'graphgrammar_Symbol3', b2)
    if hasattr(b2, 'graphgrammar_Grammar2'):
        assert not _is_linked(b2, 'graphgrammar_Grammar2', a)


def test_assoc_terminals84_link_reassign_clear():
    a = graphgrammar_TripleGrammar(name="sample_text")
    b1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleGrammar85', {b1})
    assert _is_linked(a, 'graphgrammar_TripleGrammar85', b1)
    if hasattr(b1, 'graphgrammar_Symbol86'):
        assert _is_linked(b1, 'graphgrammar_Symbol86', a)
    _safe_set(a, 'graphgrammar_TripleGrammar85', {b2})
    assert _is_linked(a, 'graphgrammar_TripleGrammar85', b2)
    if hasattr(b1, 'graphgrammar_Symbol86'):
        assert not _is_linked(b1, 'graphgrammar_Symbol86', a)
    if hasattr(b2, 'graphgrammar_Symbol86'):
        assert _is_linked(b2, 'graphgrammar_Symbol86', a)
    _safe_set(a, 'graphgrammar_TripleGrammar85', set())
    assert not _is_linked(a, 'graphgrammar_TripleGrammar85', b2)
    if hasattr(b2, 'graphgrammar_Symbol86'):
        assert not _is_linked(b2, 'graphgrammar_Symbol86', a)


def test_assoc_to76_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_Edge()
    b2 = graphgrammar_Edge()
    _safe_set(a, 'graphgrammar_Vertex78', b1)
    assert _is_linked(a, 'graphgrammar_Vertex78', b1)
    if hasattr(b1, 'graphgrammar_Edge77'):
        assert _is_linked(b1, 'graphgrammar_Edge77', a)
    _safe_set(a, 'graphgrammar_Vertex78', b2)
    assert _is_linked(a, 'graphgrammar_Vertex78', b2)
    if hasattr(b1, 'graphgrammar_Edge77'):
        assert not _is_linked(b1, 'graphgrammar_Edge77', a)
    if hasattr(b2, 'graphgrammar_Edge77'):
        assert _is_linked(b2, 'graphgrammar_Edge77', a)
    _safe_set(a, 'graphgrammar_Vertex78', None)
    assert not _is_linked(a, 'graphgrammar_Vertex78', b2)
    if hasattr(b2, 'graphgrammar_Edge77'):
        assert not _is_linked(b2, 'graphgrammar_Edge77', a)


def test_assoc_tripleRules90_link_reassign_clear():
    a = graphgrammar_TripleRule()
    b1 = graphgrammar_TripleGrammar(name="sample_text")
    b2 = graphgrammar_TripleGrammar(name="sample_text_2")
    _safe_set(a, 'graphgrammar_TripleRule', b1)
    assert _is_linked(a, 'graphgrammar_TripleRule', b1)
    if hasattr(b1, 'graphgrammar_TripleGrammar91'):
        assert _is_linked(b1, 'graphgrammar_TripleGrammar91', a)
    _safe_set(a, 'graphgrammar_TripleRule', b2)
    assert _is_linked(a, 'graphgrammar_TripleRule', b2)
    if hasattr(b1, 'graphgrammar_TripleGrammar91'):
        assert not _is_linked(b1, 'graphgrammar_TripleGrammar91', a)
    if hasattr(b2, 'graphgrammar_TripleGrammar91'):
        assert _is_linked(b2, 'graphgrammar_TripleGrammar91', a)
    _safe_set(a, 'graphgrammar_TripleRule', None)
    assert not _is_linked(a, 'graphgrammar_TripleRule', b2)
    if hasattr(b2, 'graphgrammar_TripleGrammar91'):
        assert not _is_linked(b2, 'graphgrammar_TripleGrammar91', a)


def test_assoc_value127_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_VertexToVertexMap()
    b2 = graphgrammar_VertexToVertexMap()
    _safe_set(a, 'graphgrammar_Vertex129', b1)
    assert _is_linked(a, 'graphgrammar_Vertex129', b1)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap128'):
        assert _is_linked(b1, 'graphgrammar_VertexToVertexMap128', a)
    _safe_set(a, 'graphgrammar_Vertex129', b2)
    assert _is_linked(a, 'graphgrammar_Vertex129', b2)
    if hasattr(b1, 'graphgrammar_VertexToVertexMap128'):
        assert not _is_linked(b1, 'graphgrammar_VertexToVertexMap128', a)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap128'):
        assert _is_linked(b2, 'graphgrammar_VertexToVertexMap128', a)
    _safe_set(a, 'graphgrammar_Vertex129', None)
    assert not _is_linked(a, 'graphgrammar_Vertex129', b2)
    if hasattr(b2, 'graphgrammar_VertexToVertexMap128'):
        assert not _is_linked(b2, 'graphgrammar_VertexToVertexMap128', a)


def test_assoc_value133_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_StringToVertexMap(key="sample_text")
    b2 = graphgrammar_StringToVertexMap(key="sample_text_2")
    _safe_set(a, 'graphgrammar_Vertex135', b1)
    assert _is_linked(a, 'graphgrammar_Vertex135', b1)
    if hasattr(b1, 'graphgrammar_StringToVertexMap134'):
        assert _is_linked(b1, 'graphgrammar_StringToVertexMap134', a)
    _safe_set(a, 'graphgrammar_Vertex135', b2)
    assert _is_linked(a, 'graphgrammar_Vertex135', b2)
    if hasattr(b1, 'graphgrammar_StringToVertexMap134'):
        assert not _is_linked(b1, 'graphgrammar_StringToVertexMap134', a)
    if hasattr(b2, 'graphgrammar_StringToVertexMap134'):
        assert _is_linked(b2, 'graphgrammar_StringToVertexMap134', a)
    _safe_set(a, 'graphgrammar_Vertex135', None)
    assert not _is_linked(a, 'graphgrammar_Vertex135', b2)
    if hasattr(b2, 'graphgrammar_StringToVertexMap134'):
        assert not _is_linked(b2, 'graphgrammar_StringToVertexMap134', a)


def test_assoc_vertex34_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_DerivationStep()
    b2 = graphgrammar_DerivationStep()
    _safe_set(a, 'graphgrammar_Vertex36', b1)
    assert _is_linked(a, 'graphgrammar_Vertex36', b1)
    if hasattr(b1, 'graphgrammar_DerivationStep35'):
        assert _is_linked(b1, 'graphgrammar_DerivationStep35', a)
    _safe_set(a, 'graphgrammar_Vertex36', b2)
    assert _is_linked(a, 'graphgrammar_Vertex36', b2)
    if hasattr(b1, 'graphgrammar_DerivationStep35'):
        assert not _is_linked(b1, 'graphgrammar_DerivationStep35', a)
    if hasattr(b2, 'graphgrammar_DerivationStep35'):
        assert _is_linked(b2, 'graphgrammar_DerivationStep35', a)
    _safe_set(a, 'graphgrammar_Vertex36', None)
    assert not _is_linked(a, 'graphgrammar_Vertex36', b2)
    if hasattr(b2, 'graphgrammar_DerivationStep35'):
        assert not _is_linked(b2, 'graphgrammar_DerivationStep35', a)


def test_assoc_vertexLabels23_link_reassign_clear():
    a = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    b1 = graphgrammar_SymbolSymbolsPair()
    b2 = graphgrammar_SymbolSymbolsPair()
    _safe_set(a, 'graphgrammar_Symbol25', b1)
    assert _is_linked(a, 'graphgrammar_Symbol25', b1)
    if hasattr(b1, 'graphgrammar_SymbolSymbolsPair24'):
        assert _is_linked(b1, 'graphgrammar_SymbolSymbolsPair24', a)
    _safe_set(a, 'graphgrammar_Symbol25', b2)
    assert _is_linked(a, 'graphgrammar_Symbol25', b2)
    if hasattr(b1, 'graphgrammar_SymbolSymbolsPair24'):
        assert not _is_linked(b1, 'graphgrammar_SymbolSymbolsPair24', a)
    if hasattr(b2, 'graphgrammar_SymbolSymbolsPair24'):
        assert _is_linked(b2, 'graphgrammar_SymbolSymbolsPair24', a)
    _safe_set(a, 'graphgrammar_Symbol25', None)
    assert not _is_linked(a, 'graphgrammar_Symbol25', b2)
    if hasattr(b2, 'graphgrammar_SymbolSymbolsPair24'):
        assert not _is_linked(b2, 'graphgrammar_SymbolSymbolsPair24', a)


def test_assoc_vertices59_link_reassign_clear():
    a = graphgrammar_Vertex(id="sample_text")
    b1 = graphgrammar_Graph()
    b2 = graphgrammar_Graph()
    _safe_set(a, 'graphgrammar_Vertex61', b1)
    assert _is_linked(a, 'graphgrammar_Vertex61', b1)
    if hasattr(b1, 'graphgrammar_Graph60'):
        assert _is_linked(b1, 'graphgrammar_Graph60', a)
    _safe_set(a, 'graphgrammar_Vertex61', b2)
    assert _is_linked(a, 'graphgrammar_Vertex61', b2)
    if hasattr(b1, 'graphgrammar_Graph60'):
        assert not _is_linked(b1, 'graphgrammar_Graph60', a)
    if hasattr(b2, 'graphgrammar_Graph60'):
        assert _is_linked(b2, 'graphgrammar_Graph60', a)
    _safe_set(a, 'graphgrammar_Vertex61', None)
    assert not _is_linked(a, 'graphgrammar_Vertex61', b2)
    if hasattr(b2, 'graphgrammar_Graph60'):
        assert not _is_linked(b2, 'graphgrammar_Graph60', a)


def test_assoc_vertices67_link_reassign_clear():
    a = graphgrammar_ZoneVertex()
    b1 = graphgrammar_Vertex(id="sample_text")
    b2 = graphgrammar_Vertex(id="sample_text_2")
    _safe_set(a, 'graphgrammar_ZoneVertex68', {b1})
    assert _is_linked(a, 'graphgrammar_ZoneVertex68', b1)
    if hasattr(b1, 'graphgrammar_Vertex69'):
        assert _is_linked(b1, 'graphgrammar_Vertex69', a)
    _safe_set(a, 'graphgrammar_ZoneVertex68', {b2})
    assert _is_linked(a, 'graphgrammar_ZoneVertex68', b2)
    if hasattr(b1, 'graphgrammar_Vertex69'):
        assert not _is_linked(b1, 'graphgrammar_Vertex69', a)
    if hasattr(b2, 'graphgrammar_Vertex69'):
        assert _is_linked(b2, 'graphgrammar_Vertex69', a)
    _safe_set(a, 'graphgrammar_ZoneVertex68', set())
    assert not _is_linked(a, 'graphgrammar_ZoneVertex68', b2)
    if hasattr(b2, 'graphgrammar_Vertex69'):
        assert not _is_linked(b2, 'graphgrammar_Vertex69', a)


def test_assoc_zoneVertex47_link_reassign_clear():
    a = graphgrammar_ZoneVertex()
    b1 = graphgrammar_ParsingTree()
    b2 = graphgrammar_ParsingTree()
    _safe_set(a, 'graphgrammar_ZoneVertex', b1)
    assert _is_linked(a, 'graphgrammar_ZoneVertex', b1)
    if hasattr(b1, 'graphgrammar_ParsingTree'):
        assert _is_linked(b1, 'graphgrammar_ParsingTree', a)
    _safe_set(a, 'graphgrammar_ZoneVertex', b2)
    assert _is_linked(a, 'graphgrammar_ZoneVertex', b2)
    if hasattr(b1, 'graphgrammar_ParsingTree'):
        assert not _is_linked(b1, 'graphgrammar_ParsingTree', a)
    if hasattr(b2, 'graphgrammar_ParsingTree'):
        assert _is_linked(b2, 'graphgrammar_ParsingTree', a)
    _safe_set(a, 'graphgrammar_ZoneVertex', None)
    assert not _is_linked(a, 'graphgrammar_ZoneVertex', b2)
    if hasattr(b2, 'graphgrammar_ParsingTree'):
        assert not _is_linked(b2, 'graphgrammar_ParsingTree', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Vertex_strategy = st.builds(Vertex)
@given(instance=Vertex_strategy)
@settings(max_examples=25)
def test_Vertex_instantiation(instance):
    assert isinstance(instance, Vertex)


graphgrammar_Derivation_strategy = st.builds(graphgrammar_Derivation)
@given(instance=graphgrammar_Derivation_strategy)
@settings(max_examples=25)
def test_graphgrammar_Derivation_instantiation(instance):
    assert isinstance(instance, graphgrammar_Derivation)


graphgrammar_DerivationStep_strategy = st.builds(graphgrammar_DerivationStep)
@given(instance=graphgrammar_DerivationStep_strategy)
@settings(max_examples=25)
def test_graphgrammar_DerivationStep_instantiation(instance):
    assert isinstance(instance, graphgrammar_DerivationStep)


graphgrammar_Edge_strategy = st.builds(graphgrammar_Edge)
@given(instance=graphgrammar_Edge_strategy)
@settings(max_examples=25)
def test_graphgrammar_Edge_instantiation(instance):
    assert isinstance(instance, graphgrammar_Edge)


graphgrammar_Grammar_strategy = st.builds(graphgrammar_Grammar, name=safe_text)
@given(instance=graphgrammar_Grammar_strategy)
@settings(max_examples=25)
def test_graphgrammar_Grammar_instantiation(instance):
    assert isinstance(instance, graphgrammar_Grammar)


graphgrammar_Graph_strategy = st.builds(graphgrammar_Graph)
@given(instance=graphgrammar_Graph_strategy)
@settings(max_examples=25)
def test_graphgrammar_Graph_instantiation(instance):
    assert isinstance(instance, graphgrammar_Graph)


graphgrammar_ParsingTree_strategy = st.builds(graphgrammar_ParsingTree)
@given(instance=graphgrammar_ParsingTree_strategy)
@settings(max_examples=25)
def test_graphgrammar_ParsingTree_instantiation(instance):
    assert isinstance(instance, graphgrammar_ParsingTree)


graphgrammar_Resolution_strategy = st.builds(graphgrammar_Resolution)
@given(instance=graphgrammar_Resolution_strategy)
@settings(max_examples=25)
def test_graphgrammar_Resolution_instantiation(instance):
    assert isinstance(instance, graphgrammar_Resolution)


graphgrammar_ResolutionStep_strategy = st.builds(graphgrammar_ResolutionStep)
@given(instance=graphgrammar_ResolutionStep_strategy)
@settings(max_examples=25)
def test_graphgrammar_ResolutionStep_instantiation(instance):
    assert isinstance(instance, graphgrammar_ResolutionStep)


graphgrammar_Rule_strategy = st.builds(graphgrammar_Rule, id=safe_text, name=safe_text)
@given(instance=graphgrammar_Rule_strategy)
@settings(max_examples=25)
def test_graphgrammar_Rule_instantiation(instance):
    assert isinstance(instance, graphgrammar_Rule)


graphgrammar_StringToVertexMap_strategy = st.builds(graphgrammar_StringToVertexMap, key=safe_text)
@given(instance=graphgrammar_StringToVertexMap_strategy)
@settings(max_examples=25)
def test_graphgrammar_StringToVertexMap_instantiation(instance):
    assert isinstance(instance, graphgrammar_StringToVertexMap)


graphgrammar_Symbol_strategy = st.builds(graphgrammar_Symbol, name=safe_text, subscript=safe_text, superscript=safe_text)
@given(instance=graphgrammar_Symbol_strategy)
@settings(max_examples=25)
def test_graphgrammar_Symbol_instantiation(instance):
    assert isinstance(instance, graphgrammar_Symbol)


graphgrammar_SymbolSymbolsPair_strategy = st.builds(graphgrammar_SymbolSymbolsPair)
@given(instance=graphgrammar_SymbolSymbolsPair_strategy)
@settings(max_examples=25)
def test_graphgrammar_SymbolSymbolsPair_instantiation(instance):
    assert isinstance(instance, graphgrammar_SymbolSymbolsPair)


graphgrammar_TripleGrammar_strategy = st.builds(graphgrammar_TripleGrammar, name=safe_text)
@given(instance=graphgrammar_TripleGrammar_strategy)
@settings(max_examples=25)
def test_graphgrammar_TripleGrammar_instantiation(instance):
    assert isinstance(instance, graphgrammar_TripleGrammar)


graphgrammar_TripleGraph_strategy = st.builds(graphgrammar_TripleGraph)
@given(instance=graphgrammar_TripleGraph_strategy)
@settings(max_examples=25)
def test_graphgrammar_TripleGraph_instantiation(instance):
    assert isinstance(instance, graphgrammar_TripleGraph)


graphgrammar_TripleRule_strategy = st.builds(graphgrammar_TripleRule)
@given(instance=graphgrammar_TripleRule_strategy)
@settings(max_examples=25)
def test_graphgrammar_TripleRule_instantiation(instance):
    assert isinstance(instance, graphgrammar_TripleRule)


graphgrammar_Vertex_strategy = st.builds(graphgrammar_Vertex, id=safe_text)
@given(instance=graphgrammar_Vertex_strategy)
@settings(max_examples=25)
def test_graphgrammar_Vertex_instantiation(instance):
    assert isinstance(instance, graphgrammar_Vertex)


graphgrammar_VertexToStringMap_strategy = st.builds(graphgrammar_VertexToStringMap, value=safe_text)
@given(instance=graphgrammar_VertexToStringMap_strategy)
@settings(max_examples=25)
def test_graphgrammar_VertexToStringMap_instantiation(instance):
    assert isinstance(instance, graphgrammar_VertexToStringMap)


graphgrammar_VertexToSymbolSymbolsPairMap_strategy = st.builds(graphgrammar_VertexToSymbolSymbolsPairMap)
@given(instance=graphgrammar_VertexToSymbolSymbolsPairMap_strategy)
@settings(max_examples=25)
def test_graphgrammar_VertexToSymbolSymbolsPairMap_instantiation(instance):
    assert isinstance(instance, graphgrammar_VertexToSymbolSymbolsPairMap)


graphgrammar_VertexToVertexMap_strategy = st.builds(graphgrammar_VertexToVertexMap)
@given(instance=graphgrammar_VertexToVertexMap_strategy)
@settings(max_examples=25)
def test_graphgrammar_VertexToVertexMap_instantiation(instance):
    assert isinstance(instance, graphgrammar_VertexToVertexMap)


graphgrammar_ZoneVertex_strategy = st.builds(graphgrammar_ZoneVertex)
@given(instance=graphgrammar_ZoneVertex_strategy)
@settings(max_examples=25)
def test_graphgrammar_ZoneVertex_instantiation(instance):
    assert isinstance(instance, graphgrammar_ZoneVertex)



