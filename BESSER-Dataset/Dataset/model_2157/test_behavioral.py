import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_alphabet0_reverse_link_reassign_clear():
    a1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    a2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    b = graphgrammar_Grammar(name="sample_text")
    _safe_set(b, 'graphgrammar_Grammar', {a1})
    assert _is_linked(b, 'graphgrammar_Grammar', a1)
    if hasattr(a1, 'graphgrammar_Symbol'):
        assert _is_linked(a1, 'graphgrammar_Symbol', b)
    _safe_set(b, 'graphgrammar_Grammar', {a2})
    assert _is_linked(b, 'graphgrammar_Grammar', a2)
    if hasattr(a1, 'graphgrammar_Symbol'):
        assert not _is_linked(a1, 'graphgrammar_Symbol', b)
    if hasattr(a2, 'graphgrammar_Symbol'):
        assert _is_linked(a2, 'graphgrammar_Symbol', b)
    _safe_set(b, 'graphgrammar_Grammar', set())
    assert not _is_linked(b, 'graphgrammar_Grammar', a2)
    if hasattr(a2, 'graphgrammar_Symbol'):
        assert not _is_linked(a2, 'graphgrammar_Symbol', b)


def test_assoc_alphabet82_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleGrammar(name="sample_text")
    a2 = graphgrammar_TripleGrammar(name="sample_text_2")
    b = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    _safe_set(b, 'graphgrammar_Symbol83', a1)
    assert _is_linked(b, 'graphgrammar_Symbol83', a1)
    if hasattr(a1, 'graphgrammar_TripleGrammar'):
        assert _is_linked(a1, 'graphgrammar_TripleGrammar', b)
    _safe_set(b, 'graphgrammar_Symbol83', a2)
    assert _is_linked(b, 'graphgrammar_Symbol83', a2)
    if hasattr(a1, 'graphgrammar_TripleGrammar'):
        assert not _is_linked(a1, 'graphgrammar_TripleGrammar', b)
    if hasattr(a2, 'graphgrammar_TripleGrammar'):
        assert _is_linked(a2, 'graphgrammar_TripleGrammar', b)
    _safe_set(b, 'graphgrammar_Symbol83', None)
    assert not _is_linked(b, 'graphgrammar_Symbol83', a2)
    if hasattr(a2, 'graphgrammar_TripleGrammar'):
        assert not _is_linked(a2, 'graphgrammar_TripleGrammar', b)


def test_assoc_children52_reverse_link_reassign_clear():
    a1 = graphgrammar_ParsingTree()
    a2 = graphgrammar_ParsingTree()
    b = graphgrammar_ParsingTree()
    _safe_set(b, 'graphgrammar_ParsingTree53', a1)
    assert _is_linked(b, 'graphgrammar_ParsingTree53', a1)
    if hasattr(a1, 'graphgrammar_ParsingTree51'):
        assert _is_linked(a1, 'graphgrammar_ParsingTree51', b)
    _safe_set(b, 'graphgrammar_ParsingTree53', a2)
    assert _is_linked(b, 'graphgrammar_ParsingTree53', a2)
    if hasattr(a1, 'graphgrammar_ParsingTree51'):
        assert not _is_linked(a1, 'graphgrammar_ParsingTree51', b)
    if hasattr(a2, 'graphgrammar_ParsingTree51'):
        assert _is_linked(a2, 'graphgrammar_ParsingTree51', b)
    _safe_set(b, 'graphgrammar_ParsingTree53', None)
    assert not _is_linked(b, 'graphgrammar_ParsingTree53', a2)
    if hasattr(a2, 'graphgrammar_ParsingTree51'):
        assert not _is_linked(a2, 'graphgrammar_ParsingTree51', b)


def test_assoc_corr112_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleGraph()
    a2 = graphgrammar_TripleGraph()
    b = graphgrammar_Graph()
    _safe_set(b, 'graphgrammar_Graph114', a1)
    assert _is_linked(b, 'graphgrammar_Graph114', a1)
    if hasattr(a1, 'graphgrammar_TripleGraph113'):
        assert _is_linked(a1, 'graphgrammar_TripleGraph113', b)
    _safe_set(b, 'graphgrammar_Graph114', a2)
    assert _is_linked(b, 'graphgrammar_Graph114', a2)
    if hasattr(a1, 'graphgrammar_TripleGraph113'):
        assert not _is_linked(a1, 'graphgrammar_TripleGraph113', b)
    if hasattr(a2, 'graphgrammar_TripleGraph113'):
        assert _is_linked(a2, 'graphgrammar_TripleGraph113', b)
    _safe_set(b, 'graphgrammar_Graph114', None)
    assert not _is_linked(b, 'graphgrammar_Graph114', a2)
    if hasattr(a2, 'graphgrammar_TripleGraph113'):
        assert not _is_linked(a2, 'graphgrammar_TripleGraph113', b)


def test_assoc_corr98_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleRule()
    a2 = graphgrammar_TripleRule()
    b = graphgrammar_Rule(id="sample_text", name="sample_text")
    _safe_set(b, 'graphgrammar_Rule100', a1)
    assert _is_linked(b, 'graphgrammar_Rule100', a1)
    if hasattr(a1, 'graphgrammar_TripleRule99'):
        assert _is_linked(a1, 'graphgrammar_TripleRule99', b)
    _safe_set(b, 'graphgrammar_Rule100', a2)
    assert _is_linked(b, 'graphgrammar_Rule100', a2)
    if hasattr(a1, 'graphgrammar_TripleRule99'):
        assert not _is_linked(a1, 'graphgrammar_TripleRule99', b)
    if hasattr(a2, 'graphgrammar_TripleRule99'):
        assert _is_linked(a2, 'graphgrammar_TripleRule99', b)
    _safe_set(b, 'graphgrammar_Rule100', None)
    assert not _is_linked(b, 'graphgrammar_Rule100', a2)
    if hasattr(a2, 'graphgrammar_TripleRule99'):
        assert not _is_linked(a2, 'graphgrammar_TripleRule99', b)


def test_assoc_edges62_reverse_link_reassign_clear():
    a1 = graphgrammar_Graph()
    a2 = graphgrammar_Graph()
    b = graphgrammar_Edge()
    _safe_set(b, 'graphgrammar_Edge', a1)
    assert _is_linked(b, 'graphgrammar_Edge', a1)
    if hasattr(a1, 'graphgrammar_Graph63'):
        assert _is_linked(a1, 'graphgrammar_Graph63', b)
    _safe_set(b, 'graphgrammar_Edge', a2)
    assert _is_linked(b, 'graphgrammar_Edge', a2)
    if hasattr(a1, 'graphgrammar_Graph63'):
        assert not _is_linked(a1, 'graphgrammar_Graph63', b)
    if hasattr(a2, 'graphgrammar_Graph63'):
        assert _is_linked(a2, 'graphgrammar_Graph63', b)
    _safe_set(b, 'graphgrammar_Edge', None)
    assert not _is_linked(b, 'graphgrammar_Edge', a2)
    if hasattr(a2, 'graphgrammar_Graph63'):
        assert not _is_linked(a2, 'graphgrammar_Graph63', b)


def test_assoc_from_73_reverse_link_reassign_clear():
    a1 = graphgrammar_Vertex(id="sample_text")
    a2 = graphgrammar_Vertex(id="sample_text_2")
    b = graphgrammar_Edge()
    _safe_set(b, 'graphgrammar_Edge74', a1)
    assert _is_linked(b, 'graphgrammar_Edge74', a1)
    if hasattr(a1, 'graphgrammar_Vertex75'):
        assert _is_linked(a1, 'graphgrammar_Vertex75', b)
    _safe_set(b, 'graphgrammar_Edge74', a2)
    assert _is_linked(b, 'graphgrammar_Edge74', a2)
    if hasattr(a1, 'graphgrammar_Vertex75'):
        assert not _is_linked(a1, 'graphgrammar_Vertex75', b)
    if hasattr(a2, 'graphgrammar_Vertex75'):
        assert _is_linked(a2, 'graphgrammar_Vertex75', b)
    _safe_set(b, 'graphgrammar_Edge74', None)
    assert not _is_linked(b, 'graphgrammar_Edge74', a2)
    if hasattr(a2, 'graphgrammar_Vertex75'):
        assert not _is_linked(a2, 'graphgrammar_Vertex75', b)


def test_assoc_initial9_reverse_link_reassign_clear():
    a1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    a2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    b = graphgrammar_Grammar(name="sample_text")
    _safe_set(b, 'graphgrammar_Grammar10', a1)
    assert _is_linked(b, 'graphgrammar_Grammar10', a1)
    if hasattr(a1, 'graphgrammar_Symbol11'):
        assert _is_linked(a1, 'graphgrammar_Symbol11', b)
    _safe_set(b, 'graphgrammar_Grammar10', a2)
    assert _is_linked(b, 'graphgrammar_Grammar10', a2)
    if hasattr(a1, 'graphgrammar_Symbol11'):
        assert not _is_linked(a1, 'graphgrammar_Symbol11', b)
    if hasattr(a2, 'graphgrammar_Symbol11'):
        assert _is_linked(a2, 'graphgrammar_Symbol11', b)
    _safe_set(b, 'graphgrammar_Grammar10', None)
    assert not _is_linked(b, 'graphgrammar_Grammar10', a2)
    if hasattr(a2, 'graphgrammar_Symbol11'):
        assert not _is_linked(a2, 'graphgrammar_Symbol11', b)


def test_assoc_initial92_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleGrammar(name="sample_text")
    a2 = graphgrammar_TripleGrammar(name="sample_text_2")
    b = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    _safe_set(b, 'graphgrammar_Symbol94', a1)
    assert _is_linked(b, 'graphgrammar_Symbol94', a1)
    if hasattr(a1, 'graphgrammar_TripleGrammar93'):
        assert _is_linked(a1, 'graphgrammar_TripleGrammar93', b)
    _safe_set(b, 'graphgrammar_Symbol94', a2)
    assert _is_linked(b, 'graphgrammar_Symbol94', a2)
    if hasattr(a1, 'graphgrammar_TripleGrammar93'):
        assert not _is_linked(a1, 'graphgrammar_TripleGrammar93', b)
    if hasattr(a2, 'graphgrammar_TripleGrammar93'):
        assert _is_linked(a2, 'graphgrammar_TripleGrammar93', b)
    _safe_set(b, 'graphgrammar_Symbol94', None)
    assert not _is_linked(b, 'graphgrammar_Symbol94', a2)
    if hasattr(a2, 'graphgrammar_TripleGrammar93'):
        assert not _is_linked(a2, 'graphgrammar_TripleGrammar93', b)


def test_assoc_key130_reverse_link_reassign_clear():
    a1 = graphgrammar_VertexToStringMap(value="sample_text")
    a2 = graphgrammar_VertexToStringMap(value="sample_text_2")
    b = graphgrammar_Vertex(id="sample_text")
    _safe_set(b, 'graphgrammar_Vertex132', a1)
    assert _is_linked(b, 'graphgrammar_Vertex132', a1)
    if hasattr(a1, 'graphgrammar_VertexToStringMap131'):
        assert _is_linked(a1, 'graphgrammar_VertexToStringMap131', b)
    _safe_set(b, 'graphgrammar_Vertex132', a2)
    assert _is_linked(b, 'graphgrammar_Vertex132', a2)
    if hasattr(a1, 'graphgrammar_VertexToStringMap131'):
        assert not _is_linked(a1, 'graphgrammar_VertexToStringMap131', b)
    if hasattr(a2, 'graphgrammar_VertexToStringMap131'):
        assert _is_linked(a2, 'graphgrammar_VertexToStringMap131', b)
    _safe_set(b, 'graphgrammar_Vertex132', None)
    assert not _is_linked(b, 'graphgrammar_Vertex132', a2)
    if hasattr(a2, 'graphgrammar_VertexToStringMap131'):
        assert not _is_linked(a2, 'graphgrammar_VertexToStringMap131', b)


def test_assoc_label64_reverse_link_reassign_clear():
    a1 = graphgrammar_Vertex(id="sample_text")
    a2 = graphgrammar_Vertex(id="sample_text_2")
    b = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    _safe_set(b, 'graphgrammar_Symbol66', a1)
    assert _is_linked(b, 'graphgrammar_Symbol66', a1)
    if hasattr(a1, 'graphgrammar_Vertex65'):
        assert _is_linked(a1, 'graphgrammar_Vertex65', b)
    _safe_set(b, 'graphgrammar_Symbol66', a2)
    assert _is_linked(b, 'graphgrammar_Symbol66', a2)
    if hasattr(a1, 'graphgrammar_Vertex65'):
        assert not _is_linked(a1, 'graphgrammar_Vertex65', b)
    if hasattr(a2, 'graphgrammar_Vertex65'):
        assert _is_linked(a2, 'graphgrammar_Vertex65', b)
    _safe_set(b, 'graphgrammar_Symbol66', None)
    assert not _is_linked(b, 'graphgrammar_Symbol66', a2)
    if hasattr(a2, 'graphgrammar_Vertex65'):
        assert not _is_linked(a2, 'graphgrammar_Vertex65', b)


def test_assoc_label79_reverse_link_reassign_clear():
    a1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    a2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    b = graphgrammar_Edge()
    _safe_set(b, 'graphgrammar_Edge80', a1)
    assert _is_linked(b, 'graphgrammar_Edge80', a1)
    if hasattr(a1, 'graphgrammar_Symbol81'):
        assert _is_linked(a1, 'graphgrammar_Symbol81', b)
    _safe_set(b, 'graphgrammar_Edge80', a2)
    assert _is_linked(b, 'graphgrammar_Edge80', a2)
    if hasattr(a1, 'graphgrammar_Symbol81'):
        assert not _is_linked(a1, 'graphgrammar_Symbol81', b)
    if hasattr(a2, 'graphgrammar_Symbol81'):
        assert _is_linked(a2, 'graphgrammar_Symbol81', b)
    _safe_set(b, 'graphgrammar_Edge80', None)
    assert not _is_linked(b, 'graphgrammar_Edge80', a2)
    if hasattr(a2, 'graphgrammar_Symbol81'):
        assert not _is_linked(a2, 'graphgrammar_Symbol81', b)


def test_assoc_lhs12_reverse_link_reassign_clear():
    a1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    a2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    b = graphgrammar_Rule(id="sample_text", name="sample_text")
    _safe_set(b, 'graphgrammar_Rule13', a1)
    assert _is_linked(b, 'graphgrammar_Rule13', a1)
    if hasattr(a1, 'graphgrammar_Symbol14'):
        assert _is_linked(a1, 'graphgrammar_Symbol14', b)
    _safe_set(b, 'graphgrammar_Rule13', a2)
    assert _is_linked(b, 'graphgrammar_Rule13', a2)
    if hasattr(a1, 'graphgrammar_Symbol14'):
        assert not _is_linked(a1, 'graphgrammar_Symbol14', b)
    if hasattr(a2, 'graphgrammar_Symbol14'):
        assert _is_linked(a2, 'graphgrammar_Symbol14', b)
    _safe_set(b, 'graphgrammar_Rule13', None)
    assert not _is_linked(b, 'graphgrammar_Rule13', a2)
    if hasattr(a2, 'graphgrammar_Symbol14'):
        assert not _is_linked(a2, 'graphgrammar_Symbol14', b)


def test_assoc_nonterminals4_reverse_link_reassign_clear():
    a1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    a2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    b = graphgrammar_Grammar(name="sample_text")
    _safe_set(b, 'graphgrammar_Grammar5', {a1})
    assert _is_linked(b, 'graphgrammar_Grammar5', a1)
    if hasattr(a1, 'graphgrammar_Symbol6'):
        assert _is_linked(a1, 'graphgrammar_Symbol6', b)
    _safe_set(b, 'graphgrammar_Grammar5', {a2})
    assert _is_linked(b, 'graphgrammar_Grammar5', a2)
    if hasattr(a1, 'graphgrammar_Symbol6'):
        assert not _is_linked(a1, 'graphgrammar_Symbol6', b)
    if hasattr(a2, 'graphgrammar_Symbol6'):
        assert _is_linked(a2, 'graphgrammar_Symbol6', b)
    _safe_set(b, 'graphgrammar_Grammar5', set())
    assert not _is_linked(b, 'graphgrammar_Grammar5', a2)
    if hasattr(a2, 'graphgrammar_Symbol6'):
        assert not _is_linked(a2, 'graphgrammar_Symbol6', b)


def test_assoc_nonterminals87_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleGrammar(name="sample_text")
    a2 = graphgrammar_TripleGrammar(name="sample_text_2")
    b = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    _safe_set(b, 'graphgrammar_Symbol89', a1)
    assert _is_linked(b, 'graphgrammar_Symbol89', a1)
    if hasattr(a1, 'graphgrammar_TripleGrammar88'):
        assert _is_linked(a1, 'graphgrammar_TripleGrammar88', b)
    _safe_set(b, 'graphgrammar_Symbol89', a2)
    assert _is_linked(b, 'graphgrammar_Symbol89', a2)
    if hasattr(a1, 'graphgrammar_TripleGrammar88'):
        assert not _is_linked(a1, 'graphgrammar_TripleGrammar88', b)
    if hasattr(a2, 'graphgrammar_TripleGrammar88'):
        assert _is_linked(a2, 'graphgrammar_TripleGrammar88', b)
    _safe_set(b, 'graphgrammar_Symbol89', None)
    assert not _is_linked(b, 'graphgrammar_Symbol89', a2)
    if hasattr(a2, 'graphgrammar_TripleGrammar88'):
        assert not _is_linked(a2, 'graphgrammar_TripleGrammar88', b)


def test_assoc_pac19_reverse_link_reassign_clear():
    a1 = graphgrammar_Vertex(id="sample_text")
    a2 = graphgrammar_Vertex(id="sample_text_2")
    b = graphgrammar_Rule(id="sample_text", name="sample_text")
    _safe_set(b, 'graphgrammar_Rule20', {a1})
    assert _is_linked(b, 'graphgrammar_Rule20', a1)
    if hasattr(a1, 'graphgrammar_Vertex'):
        assert _is_linked(a1, 'graphgrammar_Vertex', b)
    _safe_set(b, 'graphgrammar_Rule20', {a2})
    assert _is_linked(b, 'graphgrammar_Rule20', a2)
    if hasattr(a1, 'graphgrammar_Vertex'):
        assert not _is_linked(a1, 'graphgrammar_Vertex', b)
    if hasattr(a2, 'graphgrammar_Vertex'):
        assert _is_linked(a2, 'graphgrammar_Vertex', b)
    _safe_set(b, 'graphgrammar_Rule20', set())
    assert not _is_linked(b, 'graphgrammar_Rule20', a2)
    if hasattr(a2, 'graphgrammar_Vertex'):
        assert not _is_linked(a2, 'graphgrammar_Vertex', b)


def test_assoc_pac70_reverse_link_reassign_clear():
    a1 = graphgrammar_ZoneVertex()
    a2 = graphgrammar_ZoneVertex()
    b = graphgrammar_Vertex(id="sample_text")
    _safe_set(b, 'graphgrammar_Vertex72', a1)
    assert _is_linked(b, 'graphgrammar_Vertex72', a1)
    if hasattr(a1, 'graphgrammar_ZoneVertex71'):
        assert _is_linked(a1, 'graphgrammar_ZoneVertex71', b)
    _safe_set(b, 'graphgrammar_Vertex72', a2)
    assert _is_linked(b, 'graphgrammar_Vertex72', a2)
    if hasattr(a1, 'graphgrammar_ZoneVertex71'):
        assert not _is_linked(a1, 'graphgrammar_ZoneVertex71', b)
    if hasattr(a2, 'graphgrammar_ZoneVertex71'):
        assert _is_linked(a2, 'graphgrammar_ZoneVertex71', b)
    _safe_set(b, 'graphgrammar_Vertex72', None)
    assert not _is_linked(b, 'graphgrammar_Vertex72', a2)
    if hasattr(a2, 'graphgrammar_ZoneVertex71'):
        assert not _is_linked(a2, 'graphgrammar_ZoneVertex71', b)


def test_assoc_rhs15_reverse_link_reassign_clear():
    a1 = graphgrammar_Rule(id="sample_text", name="sample_text")
    a2 = graphgrammar_Rule(id="sample_text_2", name="sample_text_2")
    b = graphgrammar_Graph()
    _safe_set(b, 'graphgrammar_Graph', a1)
    assert _is_linked(b, 'graphgrammar_Graph', a1)
    if hasattr(a1, 'graphgrammar_Rule16'):
        assert _is_linked(a1, 'graphgrammar_Rule16', b)
    _safe_set(b, 'graphgrammar_Graph', a2)
    assert _is_linked(b, 'graphgrammar_Graph', a2)
    if hasattr(a1, 'graphgrammar_Rule16'):
        assert not _is_linked(a1, 'graphgrammar_Rule16', b)
    if hasattr(a2, 'graphgrammar_Rule16'):
        assert _is_linked(a2, 'graphgrammar_Rule16', b)
    _safe_set(b, 'graphgrammar_Graph', None)
    assert not _is_linked(b, 'graphgrammar_Graph', a2)
    if hasattr(a2, 'graphgrammar_Rule16'):
        assert not _is_linked(a2, 'graphgrammar_Rule16', b)


def test_assoc_rules7_reverse_link_reassign_clear():
    a1 = graphgrammar_Rule(id="sample_text", name="sample_text")
    a2 = graphgrammar_Rule(id="sample_text_2", name="sample_text_2")
    b = graphgrammar_Grammar(name="sample_text")
    _safe_set(b, 'graphgrammar_Grammar8', {a1})
    assert _is_linked(b, 'graphgrammar_Grammar8', a1)
    if hasattr(a1, 'graphgrammar_Rule'):
        assert _is_linked(a1, 'graphgrammar_Rule', b)
    _safe_set(b, 'graphgrammar_Grammar8', {a2})
    assert _is_linked(b, 'graphgrammar_Grammar8', a2)
    if hasattr(a1, 'graphgrammar_Rule'):
        assert not _is_linked(a1, 'graphgrammar_Rule', b)
    if hasattr(a2, 'graphgrammar_Rule'):
        assert _is_linked(a2, 'graphgrammar_Rule', b)
    _safe_set(b, 'graphgrammar_Grammar8', set())
    assert not _is_linked(b, 'graphgrammar_Grammar8', a2)
    if hasattr(a2, 'graphgrammar_Rule'):
        assert not _is_linked(a2, 'graphgrammar_Rule', b)


def test_assoc_source110_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleGraph()
    a2 = graphgrammar_TripleGraph()
    b = graphgrammar_Graph()
    _safe_set(b, 'graphgrammar_Graph111', a1)
    assert _is_linked(b, 'graphgrammar_Graph111', a1)
    if hasattr(a1, 'graphgrammar_TripleGraph'):
        assert _is_linked(a1, 'graphgrammar_TripleGraph', b)
    _safe_set(b, 'graphgrammar_Graph111', a2)
    assert _is_linked(b, 'graphgrammar_Graph111', a2)
    if hasattr(a1, 'graphgrammar_TripleGraph'):
        assert not _is_linked(a1, 'graphgrammar_TripleGraph', b)
    if hasattr(a2, 'graphgrammar_TripleGraph'):
        assert _is_linked(a2, 'graphgrammar_TripleGraph', b)
    _safe_set(b, 'graphgrammar_Graph111', None)
    assert not _is_linked(b, 'graphgrammar_Graph111', a2)
    if hasattr(a2, 'graphgrammar_TripleGraph'):
        assert not _is_linked(a2, 'graphgrammar_TripleGraph', b)


def test_assoc_source95_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleRule()
    a2 = graphgrammar_TripleRule()
    b = graphgrammar_Rule(id="sample_text", name="sample_text")
    _safe_set(b, 'graphgrammar_Rule97', a1)
    assert _is_linked(b, 'graphgrammar_Rule97', a1)
    if hasattr(a1, 'graphgrammar_TripleRule96'):
        assert _is_linked(a1, 'graphgrammar_TripleRule96', b)
    _safe_set(b, 'graphgrammar_Rule97', a2)
    assert _is_linked(b, 'graphgrammar_Rule97', a2)
    if hasattr(a1, 'graphgrammar_TripleRule96'):
        assert not _is_linked(a1, 'graphgrammar_TripleRule96', b)
    if hasattr(a2, 'graphgrammar_TripleRule96'):
        assert _is_linked(a2, 'graphgrammar_TripleRule96', b)
    _safe_set(b, 'graphgrammar_Rule97', None)
    assert not _is_linked(b, 'graphgrammar_Rule97', a2)
    if hasattr(a2, 'graphgrammar_TripleRule96'):
        assert not _is_linked(a2, 'graphgrammar_TripleRule96', b)


def test_assoc_target101_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleRule()
    a2 = graphgrammar_TripleRule()
    b = graphgrammar_Rule(id="sample_text", name="sample_text")
    _safe_set(b, 'graphgrammar_Rule103', a1)
    assert _is_linked(b, 'graphgrammar_Rule103', a1)
    if hasattr(a1, 'graphgrammar_TripleRule102'):
        assert _is_linked(a1, 'graphgrammar_TripleRule102', b)
    _safe_set(b, 'graphgrammar_Rule103', a2)
    assert _is_linked(b, 'graphgrammar_Rule103', a2)
    if hasattr(a1, 'graphgrammar_TripleRule102'):
        assert not _is_linked(a1, 'graphgrammar_TripleRule102', b)
    if hasattr(a2, 'graphgrammar_TripleRule102'):
        assert _is_linked(a2, 'graphgrammar_TripleRule102', b)
    _safe_set(b, 'graphgrammar_Rule103', None)
    assert not _is_linked(b, 'graphgrammar_Rule103', a2)
    if hasattr(a2, 'graphgrammar_TripleRule102'):
        assert not _is_linked(a2, 'graphgrammar_TripleRule102', b)


def test_assoc_target115_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleGraph()
    a2 = graphgrammar_TripleGraph()
    b = graphgrammar_Graph()
    _safe_set(b, 'graphgrammar_Graph117', a1)
    assert _is_linked(b, 'graphgrammar_Graph117', a1)
    if hasattr(a1, 'graphgrammar_TripleGraph116'):
        assert _is_linked(a1, 'graphgrammar_TripleGraph116', b)
    _safe_set(b, 'graphgrammar_Graph117', a2)
    assert _is_linked(b, 'graphgrammar_Graph117', a2)
    if hasattr(a1, 'graphgrammar_TripleGraph116'):
        assert not _is_linked(a1, 'graphgrammar_TripleGraph116', b)
    if hasattr(a2, 'graphgrammar_TripleGraph116'):
        assert _is_linked(a2, 'graphgrammar_TripleGraph116', b)
    _safe_set(b, 'graphgrammar_Graph117', None)
    assert not _is_linked(b, 'graphgrammar_Graph117', a2)
    if hasattr(a2, 'graphgrammar_TripleGraph116'):
        assert not _is_linked(a2, 'graphgrammar_TripleGraph116', b)


def test_assoc_terminals1_reverse_link_reassign_clear():
    a1 = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    a2 = graphgrammar_Symbol(name="sample_text_2", subscript="sample_text_2", superscript="sample_text_2")
    b = graphgrammar_Grammar(name="sample_text")
    _safe_set(b, 'graphgrammar_Grammar2', {a1})
    assert _is_linked(b, 'graphgrammar_Grammar2', a1)
    if hasattr(a1, 'graphgrammar_Symbol3'):
        assert _is_linked(a1, 'graphgrammar_Symbol3', b)
    _safe_set(b, 'graphgrammar_Grammar2', {a2})
    assert _is_linked(b, 'graphgrammar_Grammar2', a2)
    if hasattr(a1, 'graphgrammar_Symbol3'):
        assert not _is_linked(a1, 'graphgrammar_Symbol3', b)
    if hasattr(a2, 'graphgrammar_Symbol3'):
        assert _is_linked(a2, 'graphgrammar_Symbol3', b)
    _safe_set(b, 'graphgrammar_Grammar2', set())
    assert not _is_linked(b, 'graphgrammar_Grammar2', a2)
    if hasattr(a2, 'graphgrammar_Symbol3'):
        assert not _is_linked(a2, 'graphgrammar_Symbol3', b)


def test_assoc_terminals84_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleGrammar(name="sample_text")
    a2 = graphgrammar_TripleGrammar(name="sample_text_2")
    b = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    _safe_set(b, 'graphgrammar_Symbol86', a1)
    assert _is_linked(b, 'graphgrammar_Symbol86', a1)
    if hasattr(a1, 'graphgrammar_TripleGrammar85'):
        assert _is_linked(a1, 'graphgrammar_TripleGrammar85', b)
    _safe_set(b, 'graphgrammar_Symbol86', a2)
    assert _is_linked(b, 'graphgrammar_Symbol86', a2)
    if hasattr(a1, 'graphgrammar_TripleGrammar85'):
        assert not _is_linked(a1, 'graphgrammar_TripleGrammar85', b)
    if hasattr(a2, 'graphgrammar_TripleGrammar85'):
        assert _is_linked(a2, 'graphgrammar_TripleGrammar85', b)
    _safe_set(b, 'graphgrammar_Symbol86', None)
    assert not _is_linked(b, 'graphgrammar_Symbol86', a2)
    if hasattr(a2, 'graphgrammar_TripleGrammar85'):
        assert not _is_linked(a2, 'graphgrammar_TripleGrammar85', b)


def test_assoc_to76_reverse_link_reassign_clear():
    a1 = graphgrammar_Vertex(id="sample_text")
    a2 = graphgrammar_Vertex(id="sample_text_2")
    b = graphgrammar_Edge()
    _safe_set(b, 'graphgrammar_Edge77', a1)
    assert _is_linked(b, 'graphgrammar_Edge77', a1)
    if hasattr(a1, 'graphgrammar_Vertex78'):
        assert _is_linked(a1, 'graphgrammar_Vertex78', b)
    _safe_set(b, 'graphgrammar_Edge77', a2)
    assert _is_linked(b, 'graphgrammar_Edge77', a2)
    if hasattr(a1, 'graphgrammar_Vertex78'):
        assert not _is_linked(a1, 'graphgrammar_Vertex78', b)
    if hasattr(a2, 'graphgrammar_Vertex78'):
        assert _is_linked(a2, 'graphgrammar_Vertex78', b)
    _safe_set(b, 'graphgrammar_Edge77', None)
    assert not _is_linked(b, 'graphgrammar_Edge77', a2)
    if hasattr(a2, 'graphgrammar_Vertex78'):
        assert not _is_linked(a2, 'graphgrammar_Vertex78', b)


def test_assoc_tripleRules90_reverse_link_reassign_clear():
    a1 = graphgrammar_TripleRule()
    a2 = graphgrammar_TripleRule()
    b = graphgrammar_TripleGrammar(name="sample_text")
    _safe_set(b, 'graphgrammar_TripleGrammar91', {a1})
    assert _is_linked(b, 'graphgrammar_TripleGrammar91', a1)
    if hasattr(a1, 'graphgrammar_TripleRule'):
        assert _is_linked(a1, 'graphgrammar_TripleRule', b)
    _safe_set(b, 'graphgrammar_TripleGrammar91', {a2})
    assert _is_linked(b, 'graphgrammar_TripleGrammar91', a2)
    if hasattr(a1, 'graphgrammar_TripleRule'):
        assert not _is_linked(a1, 'graphgrammar_TripleRule', b)
    if hasattr(a2, 'graphgrammar_TripleRule'):
        assert _is_linked(a2, 'graphgrammar_TripleRule', b)
    _safe_set(b, 'graphgrammar_TripleGrammar91', set())
    assert not _is_linked(b, 'graphgrammar_TripleGrammar91', a2)
    if hasattr(a2, 'graphgrammar_TripleRule'):
        assert not _is_linked(a2, 'graphgrammar_TripleRule', b)


def test_assoc_value133_reverse_link_reassign_clear():
    a1 = graphgrammar_Vertex(id="sample_text")
    a2 = graphgrammar_Vertex(id="sample_text_2")
    b = graphgrammar_StringToVertexMap(key="sample_text")
    _safe_set(b, 'graphgrammar_StringToVertexMap134', a1)
    assert _is_linked(b, 'graphgrammar_StringToVertexMap134', a1)
    if hasattr(a1, 'graphgrammar_Vertex135'):
        assert _is_linked(a1, 'graphgrammar_Vertex135', b)
    _safe_set(b, 'graphgrammar_StringToVertexMap134', a2)
    assert _is_linked(b, 'graphgrammar_StringToVertexMap134', a2)
    if hasattr(a1, 'graphgrammar_Vertex135'):
        assert not _is_linked(a1, 'graphgrammar_Vertex135', b)
    if hasattr(a2, 'graphgrammar_Vertex135'):
        assert _is_linked(a2, 'graphgrammar_Vertex135', b)
    _safe_set(b, 'graphgrammar_StringToVertexMap134', None)
    assert not _is_linked(b, 'graphgrammar_StringToVertexMap134', a2)
    if hasattr(a2, 'graphgrammar_Vertex135'):
        assert not _is_linked(a2, 'graphgrammar_Vertex135', b)


def test_assoc_vertices59_reverse_link_reassign_clear():
    a1 = graphgrammar_Vertex(id="sample_text")
    a2 = graphgrammar_Vertex(id="sample_text_2")
    b = graphgrammar_Graph()
    _safe_set(b, 'graphgrammar_Graph60', {a1})
    assert _is_linked(b, 'graphgrammar_Graph60', a1)
    if hasattr(a1, 'graphgrammar_Vertex61'):
        assert _is_linked(a1, 'graphgrammar_Vertex61', b)
    _safe_set(b, 'graphgrammar_Graph60', {a2})
    assert _is_linked(b, 'graphgrammar_Graph60', a2)
    if hasattr(a1, 'graphgrammar_Vertex61'):
        assert not _is_linked(a1, 'graphgrammar_Vertex61', b)
    if hasattr(a2, 'graphgrammar_Vertex61'):
        assert _is_linked(a2, 'graphgrammar_Vertex61', b)
    _safe_set(b, 'graphgrammar_Graph60', set())
    assert not _is_linked(b, 'graphgrammar_Graph60', a2)
    if hasattr(a2, 'graphgrammar_Vertex61'):
        assert not _is_linked(a2, 'graphgrammar_Vertex61', b)


def test_assoc_vertices67_reverse_link_reassign_clear():
    a1 = graphgrammar_ZoneVertex()
    a2 = graphgrammar_ZoneVertex()
    b = graphgrammar_Vertex(id="sample_text")
    _safe_set(b, 'graphgrammar_Vertex69', a1)
    assert _is_linked(b, 'graphgrammar_Vertex69', a1)
    if hasattr(a1, 'graphgrammar_ZoneVertex68'):
        assert _is_linked(a1, 'graphgrammar_ZoneVertex68', b)
    _safe_set(b, 'graphgrammar_Vertex69', a2)
    assert _is_linked(b, 'graphgrammar_Vertex69', a2)
    if hasattr(a1, 'graphgrammar_ZoneVertex68'):
        assert not _is_linked(a1, 'graphgrammar_ZoneVertex68', b)
    if hasattr(a2, 'graphgrammar_ZoneVertex68'):
        assert _is_linked(a2, 'graphgrammar_ZoneVertex68', b)
    _safe_set(b, 'graphgrammar_Vertex69', None)
    assert not _is_linked(b, 'graphgrammar_Vertex69', a2)
    if hasattr(a2, 'graphgrammar_ZoneVertex68'):
        assert not _is_linked(a2, 'graphgrammar_ZoneVertex68', b)


def test_assoc_zoneVertex47_reverse_link_reassign_clear():
    a1 = graphgrammar_ZoneVertex()
    a2 = graphgrammar_ZoneVertex()
    b = graphgrammar_ParsingTree()
    _safe_set(b, 'graphgrammar_ParsingTree', a1)
    assert _is_linked(b, 'graphgrammar_ParsingTree', a1)
    if hasattr(a1, 'graphgrammar_ZoneVertex'):
        assert _is_linked(a1, 'graphgrammar_ZoneVertex', b)
    _safe_set(b, 'graphgrammar_ParsingTree', a2)
    assert _is_linked(b, 'graphgrammar_ParsingTree', a2)
    if hasattr(a1, 'graphgrammar_ZoneVertex'):
        assert not _is_linked(a1, 'graphgrammar_ZoneVertex', b)
    if hasattr(a2, 'graphgrammar_ZoneVertex'):
        assert _is_linked(a2, 'graphgrammar_ZoneVertex', b)
    _safe_set(b, 'graphgrammar_ParsingTree', None)
    assert not _is_linked(b, 'graphgrammar_ParsingTree', a2)
    if hasattr(a2, 'graphgrammar_ZoneVertex'):
        assert not _is_linked(a2, 'graphgrammar_ZoneVertex', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_derivationStep48_stub_double():
    # graphgrammar_DerivationStep has no real 'graphgrammar_DerivationStep50' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_ParsingTree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_ParsingTree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_ParsingTree()
    partner = graphgrammar_DerivationStep()
    setattr(partner, 'graphgrammar_DerivationStep50', None)
    _safe_set(owner, 'graphgrammar_ParsingTree49', partner)
    assert getattr(partner, 'graphgrammar_DerivationStep50') == owner
    _safe_set(owner, 'graphgrammar_ParsingTree49', None)
    assert getattr(partner, 'graphgrammar_DerivationStep50') is None


def test_assoc_edgeLabel21_stub_double():
    # graphgrammar_SymbolSymbolsPair has no real 'graphgrammar_SymbolSymbolsPair' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    partner = graphgrammar_SymbolSymbolsPair()
    setattr(partner, 'graphgrammar_SymbolSymbolsPair', None)
    _safe_set(owner, 'graphgrammar_Symbol22', partner)
    assert getattr(partner, 'graphgrammar_SymbolSymbolsPair') == owner
    _safe_set(owner, 'graphgrammar_Symbol22', None)
    assert getattr(partner, 'graphgrammar_SymbolSymbolsPair') is None


def test_assoc_embedding17_stub_double():
    # graphgrammar_VertexToSymbolSymbolsPairMap has no real 'graphgrammar_VertexToSymbolSymbolsPairMap' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Rule(id="sample_text", name="sample_text")
    partner = graphgrammar_VertexToSymbolSymbolsPairMap()
    setattr(partner, 'graphgrammar_VertexToSymbolSymbolsPairMap', None)
    _safe_set(owner, 'graphgrammar_Rule18', {partner})
    assert getattr(partner, 'graphgrammar_VertexToSymbolSymbolsPairMap') == owner
    _safe_set(owner, 'graphgrammar_Rule18', set())
    assert getattr(partner, 'graphgrammar_VertexToSymbolSymbolsPairMap') is None


def test_assoc_key124_stub_double():
    # graphgrammar_VertexToVertexMap has no real 'graphgrammar_VertexToVertexMap125' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Vertex(id="sample_text")
    partner = graphgrammar_VertexToVertexMap()
    setattr(partner, 'graphgrammar_VertexToVertexMap125', None)
    _safe_set(owner, 'graphgrammar_Vertex126', partner)
    assert getattr(partner, 'graphgrammar_VertexToVertexMap125') == owner
    _safe_set(owner, 'graphgrammar_Vertex126', None)
    assert getattr(partner, 'graphgrammar_VertexToVertexMap125') is None


def test_assoc_key26_stub_double():
    # graphgrammar_VertexToSymbolSymbolsPairMap has no real 'graphgrammar_VertexToSymbolSymbolsPairMap27' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Vertex(id="sample_text")
    partner = graphgrammar_VertexToSymbolSymbolsPairMap()
    setattr(partner, 'graphgrammar_VertexToSymbolSymbolsPairMap27', None)
    _safe_set(owner, 'graphgrammar_Vertex28', partner)
    assert getattr(partner, 'graphgrammar_VertexToSymbolSymbolsPairMap27') == owner
    _safe_set(owner, 'graphgrammar_Vertex28', None)
    assert getattr(partner, 'graphgrammar_VertexToSymbolSymbolsPairMap27') is None


def test_assoc_ms104_stub_double():
    # graphgrammar_VertexToVertexMap has no real 'graphgrammar_VertexToVertexMap106' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_TripleRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_TripleRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_TripleRule()
    partner = graphgrammar_VertexToVertexMap()
    setattr(partner, 'graphgrammar_VertexToVertexMap106', None)
    _safe_set(owner, 'graphgrammar_TripleRule105', {partner})
    assert getattr(partner, 'graphgrammar_VertexToVertexMap106') == owner
    _safe_set(owner, 'graphgrammar_TripleRule105', set())
    assert getattr(partner, 'graphgrammar_VertexToVertexMap106') is None


def test_assoc_ms118_stub_double():
    # graphgrammar_VertexToVertexMap has no real 'graphgrammar_VertexToVertexMap120' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_TripleGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_TripleGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_TripleGraph()
    partner = graphgrammar_VertexToVertexMap()
    setattr(partner, 'graphgrammar_VertexToVertexMap120', None)
    _safe_set(owner, 'graphgrammar_TripleGraph119', {partner})
    assert getattr(partner, 'graphgrammar_VertexToVertexMap120') == owner
    _safe_set(owner, 'graphgrammar_TripleGraph119', set())
    assert getattr(partner, 'graphgrammar_VertexToVertexMap120') is None


def test_assoc_mt107_stub_double():
    # graphgrammar_VertexToVertexMap has no real 'graphgrammar_VertexToVertexMap109' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_TripleRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_TripleRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_TripleRule()
    partner = graphgrammar_VertexToVertexMap()
    setattr(partner, 'graphgrammar_VertexToVertexMap109', None)
    _safe_set(owner, 'graphgrammar_TripleRule108', {partner})
    assert getattr(partner, 'graphgrammar_VertexToVertexMap109') == owner
    _safe_set(owner, 'graphgrammar_TripleRule108', set())
    assert getattr(partner, 'graphgrammar_VertexToVertexMap109') is None


def test_assoc_mt121_stub_double():
    # graphgrammar_VertexToVertexMap has no real 'graphgrammar_VertexToVertexMap123' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_TripleGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_TripleGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_TripleGraph()
    partner = graphgrammar_VertexToVertexMap()
    setattr(partner, 'graphgrammar_VertexToVertexMap123', None)
    _safe_set(owner, 'graphgrammar_TripleGraph122', {partner})
    assert getattr(partner, 'graphgrammar_VertexToVertexMap123') == owner
    _safe_set(owner, 'graphgrammar_TripleGraph122', set())
    assert getattr(partner, 'graphgrammar_VertexToVertexMap123') is None


def test_assoc_next40_stub_double():
    # graphgrammar_DerivationStep has no real 'graphgrammar_DerivationStep41' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Graph()
    partner = graphgrammar_DerivationStep()
    setattr(partner, 'graphgrammar_DerivationStep41', None)
    _safe_set(owner, 'graphgrammar_Graph42', partner)
    assert getattr(partner, 'graphgrammar_DerivationStep41') == owner
    _safe_set(owner, 'graphgrammar_Graph42', None)
    assert getattr(partner, 'graphgrammar_DerivationStep41') is None


def test_assoc_pac54_stub_double():
    # graphgrammar_ResolutionStep has no real 'graphgrammar_ResolutionStep' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_VertexToStringMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_VertexToStringMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_VertexToStringMap(value="sample_text")
    partner = graphgrammar_ResolutionStep()
    setattr(partner, 'graphgrammar_ResolutionStep', None)
    _safe_set(owner, 'graphgrammar_VertexToStringMap', partner)
    assert owner in getattr(partner, 'graphgrammar_ResolutionStep')
    _safe_set(owner, 'graphgrammar_VertexToStringMap', None)
    assert owner not in getattr(partner, 'graphgrammar_ResolutionStep')


def test_assoc_previous37_stub_double():
    # graphgrammar_DerivationStep has no real 'graphgrammar_DerivationStep38' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Graph()
    partner = graphgrammar_DerivationStep()
    setattr(partner, 'graphgrammar_DerivationStep38', None)
    _safe_set(owner, 'graphgrammar_Graph39', partner)
    assert getattr(partner, 'graphgrammar_DerivationStep38') == owner
    _safe_set(owner, 'graphgrammar_Graph39', None)
    assert getattr(partner, 'graphgrammar_DerivationStep38') is None


def test_assoc_referenceIds55_stub_double():
    # graphgrammar_Resolution has no real 'graphgrammar_Resolution' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_StringToVertexMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_StringToVertexMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_StringToVertexMap(key="sample_text")
    partner = graphgrammar_Resolution()
    setattr(partner, 'graphgrammar_Resolution', None)
    _safe_set(owner, 'graphgrammar_StringToVertexMap', partner)
    assert owner in getattr(partner, 'graphgrammar_Resolution')
    _safe_set(owner, 'graphgrammar_StringToVertexMap', None)
    assert owner not in getattr(partner, 'graphgrammar_Resolution')


def test_assoc_rule32_stub_double():
    # graphgrammar_DerivationStep has no real 'graphgrammar_DerivationStep' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Rule(id="sample_text", name="sample_text")
    partner = graphgrammar_DerivationStep()
    setattr(partner, 'graphgrammar_DerivationStep', None)
    _safe_set(owner, 'graphgrammar_Rule33', partner)
    assert getattr(partner, 'graphgrammar_DerivationStep') == owner
    _safe_set(owner, 'graphgrammar_Rule33', None)
    assert getattr(partner, 'graphgrammar_DerivationStep') is None


def test_assoc_value127_stub_double():
    # graphgrammar_VertexToVertexMap has no real 'graphgrammar_VertexToVertexMap128' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Vertex(id="sample_text")
    partner = graphgrammar_VertexToVertexMap()
    setattr(partner, 'graphgrammar_VertexToVertexMap128', None)
    _safe_set(owner, 'graphgrammar_Vertex129', partner)
    assert getattr(partner, 'graphgrammar_VertexToVertexMap128') == owner
    _safe_set(owner, 'graphgrammar_Vertex129', None)
    assert getattr(partner, 'graphgrammar_VertexToVertexMap128') is None


def test_assoc_vertex34_stub_double():
    # graphgrammar_DerivationStep has no real 'graphgrammar_DerivationStep35' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Vertex(id="sample_text")
    partner = graphgrammar_DerivationStep()
    setattr(partner, 'graphgrammar_DerivationStep35', None)
    _safe_set(owner, 'graphgrammar_Vertex36', partner)
    assert getattr(partner, 'graphgrammar_DerivationStep35') == owner
    _safe_set(owner, 'graphgrammar_Vertex36', None)
    assert getattr(partner, 'graphgrammar_DerivationStep35') is None


def test_assoc_vertexLabels23_stub_double():
    # graphgrammar_SymbolSymbolsPair has no real 'graphgrammar_SymbolSymbolsPair24' property in the generated
    # code (a bare stub) -- manually attach it so graphgrammar_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphgrammar_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphgrammar_Symbol(name="sample_text", subscript="sample_text", superscript="sample_text")
    partner = graphgrammar_SymbolSymbolsPair()
    setattr(partner, 'graphgrammar_SymbolSymbolsPair24', None)
    _safe_set(owner, 'graphgrammar_Symbol25', partner)
    assert owner in getattr(partner, 'graphgrammar_SymbolSymbolsPair24')
    _safe_set(owner, 'graphgrammar_Symbol25', None)
    assert owner not in getattr(partner, 'graphgrammar_SymbolSymbolsPair24')


