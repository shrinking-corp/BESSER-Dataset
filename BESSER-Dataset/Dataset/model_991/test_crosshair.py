from enum import Enum
from python_code import EdgeType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EdgeType.FORWARD_EDGE, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EdgeType.TREE_EDGE, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EdgeType.CROSS_EDGE, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EdgeType.TREE_EDGE, 0)

def test_Enum___new___2():
    assert Enum.__new__(EdgeType.TREE_EDGE, 'TREE_EDGE') == EdgeType.TREE_EDGE

from python_code import dfs_DepthFirstSearch

def test_dfs_DepthFirstSearch___init__():
    assert dfs_DepthFirstSearch.__init__(dfs_DepthFirstSearch(0, 0), 0, 0) == None

def test_dfs_DepthFirstSearch_processEdge():
    assert dfs_DepthFirstSearch.processEdge(dfs_DepthFirstSearch(0, 0), '') == None

def test_dfs_DepthFirstSearch_incrementPreTraversalCounter():
    assert dfs_DepthFirstSearch.incrementPreTraversalCounter(dfs_DepthFirstSearch(0, 0)) == None

def test_dfs_DepthFirstSearch_incrementPostTraversalCounter():
    assert dfs_DepthFirstSearch.incrementPostTraversalCounter(dfs_DepthFirstSearch(0, 0)) == None

def test_dfs_DepthFirstSearch_processNode():
    assert dfs_DepthFirstSearch.processNode(dfs_DepthFirstSearch(0, 0), '') == None
